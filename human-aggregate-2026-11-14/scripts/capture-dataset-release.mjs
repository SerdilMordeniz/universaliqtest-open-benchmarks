import { mkdir, readFile, writeFile } from 'node:fs/promises';
import { createHash } from 'node:crypto';
import { resolve, join } from 'node:path';
import { fileURLToPath } from 'node:url';

// Capture public aggregate exports only. Never reads credentials or test records.
export function parseCsv(text) {
  const rows = []; let row = [], value = '', quoted = false;
  for (let i = 0; i < text.length; i++) {
    const c = text[i];
    if (c === '"') {
      if (quoted && text[i + 1] === '"') { value += '"'; i++; }
      else if (quoted || value === '') quoted = !quoted;
      else throw new Error('Unexpected quote in CSV');
    } else if (!quoted && c === ',') { row.push(value); value = ''; }
    else if (!quoted && (c === '\n' || c === '\r')) {
      if (c === '\r' && text[i + 1] === '\n') i++;
      row.push(value); if (row.some(v => v !== '')) rows.push(row);
      row = []; value = '';
    } else value += c;
  }
  if (quoted) throw new Error('Unclosed CSV quote');
  if (row.length || value) { row.push(value); rows.push(row); }
  const [headers, ...values] = rows;
  if (!headers || new Set(headers).size !== headers.length) throw new Error('Missing/duplicate CSV header');
  return { headers, rows: values.map((r, i) => {
    if (r.length !== headers.length) throw new Error(`CSV row ${i + 2}: wrong column count`);
    return Object.fromEntries(headers.map((h, j) => [h, r[j]]));
  }) };
}

export const sha256 = bytes => createHash('sha256').update(bytes).digest('hex');
export async function capture(output) {
  await mkdir(join(output, 'data'), { recursive: true });
  try { await readFile(join(output, 'manifest.json')); throw new Error('Snapshot already exists; use a new output directory'); }
  catch (error) { if (error.code !== 'ENOENT') throw error; }
  const startedAt = new Date().toISOString();
  const files = [];
  for (const dimension of ['country', 'age', 'gender', 'education-level', 'study-area']) {
    for (const view of ['validated', 'all']) {
      const url = `https://www.universaliqtest.com/api/statistics/average-iq-by-${dimension}.csv${view === 'all' ? '?view=all' : ''}`;
      const retrievedAt = new Date().toISOString();
      const response = await fetch(url, { signal: AbortSignal.timeout(60000) });
      if (!response.ok) throw new Error(`${url}: HTTP ${response.status}`);
      const bytes = Buffer.from(await response.arrayBuffer());
      const parsed = parseCsv(bytes.toString('utf8').replace(/^\uFEFF/, ''));
      if (!parsed.rows.length || !parsed.headers.includes('meanIQ')) throw new Error(`${url}: empty or unexpected response`);
      const file = `data/${dimension}-${view}.csv`;
      await writeFile(join(output, file), bytes);
      files.push({ file, dimension, view, sourceUrl: url, resolvedUrl: response.url, retrievedAt,
        httpDate: response.headers.get('date'), contentType: response.headers.get('content-type'),
        bytes: bytes.length, sha256: sha256(bytes), rows: parsed.rows.length, columns: parsed.headers });
      console.log(`${file}: ${parsed.rows.length} rows`);
    }
  }
  const url = 'https://www.universaliqtest.com/dataset-overview-and-sources';
  const response = await fetch(url, { signal: AbortSignal.timeout(60000) });
  if (!response.ok) throw new Error(`${url}: HTTP ${response.status}`);
  const html = await response.text();
  const nextData = html.match(/<script[^>]*id="__NEXT_DATA__"[^>]*>([\s\S]*?)<\/script>/)?.[1];
  const pageProps = nextData ? JSON.parse(nextData).props?.pageProps : null;
  // Store only counts and public page metadata, not the page's translation bundle.
  const counts = pageProps?.totals ?? pageProps?.datasetCounts ?? pageProps?.counts ?? null;
  const pageEvidence = { sourceUrl: url, resolvedUrl: response.url, retrievedAt: new Date().toISOString(),
    counts, publicCountMentions: [...new Set(html.match(/(?:334[,.\s]?915|109[,.\s]?433)/g) ?? [])],
    pagePropKeys: pageProps ? Object.keys(pageProps) : [] };
  await writeFile(join(output, 'overview-evidence.json'), JSON.stringify(pageEvidence, null, 2) + '\n');
  const manifest = { version: 1, publisher: 'UniversalIQTest', startedAt, completedAt: new Date().toISOString(),
    scope: 'Public all-time aggregate CSV exports, quality-screened and all-test views. Separate requests; not an atomic database snapshot.',
    rights: { status: 'Existing site terms; no new licence granted by this capture', url: 'https://www.universaliqtest.com/terms-of-service' },
    independentReview: 'pending', files };
  await writeFile(join(output, 'manifest.json'), JSON.stringify(manifest, null, 2) + '\n');
  return manifest;
}

if (process.argv[1] && resolve(process.argv[1]) === fileURLToPath(import.meta.url)) {
  const output = process.argv[2];
  if (!output) throw new Error('Usage: node scripts/capture-dataset-release.mjs NEW_OUTPUT_DIRECTORY');
  await capture(resolve(output));
}
