"""Render standalone charts from a verified frozen public aggregate release."""
import json
import sys
from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D

root = Path(sys.argv[1])
report = json.loads((root / "verification.json").read_text(encoding="utf-8"))
if report["status"] != "passed":
    raise SystemExit("Verify the release before drawing charts")
data = json.loads((root / "chart-inputs.json").read_text(encoding="utf-8"))
out = root / "charts"
out.mkdir(exist_ok=True)
plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 11, "svg.fonttype": "none",
                     "axes.spines.top": False, "axes.spines.right": False})
blue, pale, ink = "#1864ab", "#9bc3e5", "#243746"
snapshot_date = data["capturedAt"][:10]
current = data.get("methodology") == "individual-score-sd-v2"
source = f"Source: UniversalIQTest aggregate CSVs • Snapshot {snapshot_date}"

def save(fig, stem, title, description):
    for ext in ("png", "svg", "pdf"):
        fig.savefig(out / f"{stem}.{ext}", dpi=180, facecolor="white")
    svg_path = out / f"{stem}.svg"
    svg_path.write_text("\n".join(line.rstrip() for line in svg_path.read_text(encoding="utf-8").splitlines()) + "\n", encoding="utf-8")
    (out / f"{stem}.alt.txt").write_text(title + "\n\n" + description + "\n", encoding="utf-8")
    plt.close(fig)

def setup(title, subtitle, n, left=.25):
    fig, ax = plt.subplots(figsize=(11, max(5.8, 3.1 + n * .44)))
    fig.subplots_adjust(left=left, right=.88, top=.72, bottom=.25)
    fig.text(.05, .94, title, fontsize=20, weight="bold", color=ink, va="top")
    fig.text(.05, .855, subtitle, fontsize=10.5, color=ink, va="top", linespacing=1.55)
    ax.set_axisbelow(True)
    ax.grid(axis="x", color="#e5ebf0")
    ax.spines["left"].set_visible(False)
    ax.tick_params(axis="y", length=0, pad=12)
    return fig, ax

age_text = {
 "en": ("Age bands: spread exceeds the group differences", "Quality-screened, self-selected online test results. Bars show the middle 50% of scores.\nDots show the transformed mean percentile; these are not individual IQ norms.", "IQ-style score", ["12–18 years", "19–35 years", "36–65 years", "66–100 years"], "Bars = 25th–75th percentiles; dots = transformed group statistic. Not confidence intervals."),
 "fr": ("Âge : la dispersion dépasse les écarts entre groupes", "Résultats en ligne auto-sélectionnés, après filtrage qualité. Barres : 50 % centraux des scores.\nPoints : percentile moyen transformé ; il ne s’agit pas de normes individuelles de QI.", "Score de type QI", ["12–18 ans", "19–35 ans", "36–65 ans", "66–100 ans"], "Barres = 25e–75e percentiles ; points = statistique de groupe. Pas des intervalles de confiance."),
 "ru": ("Возраст: разброс больше различий между группами", "Онлайн-выборка после проверки качества, с самостоятельным отбором участников.\nПолосы: центральные 50% результатов; точки: преобразованный средний процентиль.", "Балл теста в формате IQ", ["12–18 лет", "19–35 лет", "36–65 лет", "66–100 лет"], "Полосы = 25–75-й процентили; точки = групповой показатель. Это не доверительные интервалы.")
}
if current:
    age_text["en"] = (age_text["en"][0], "Quality-screened, self-selected online test results. Bars show the middle 50% of scores.\nDots show the mean individual scaled score in each age band.", *age_text["en"][2:4], "Bars = 25th–75th percentiles; dots = mean individual score. Not confidence intervals.")
    age_text["fr"] = (age_text["fr"][0], "Résultats en ligne auto-sélectionnés, après filtrage qualité. Barres : 50 % centraux des scores.\nPoints : moyenne des scores individuels de chaque tranche d’âge.", *age_text["fr"][2:4], "Barres = 25e–75e percentiles ; points = score individuel moyen. Pas des intervalles de confiance.")
    age_text["ru"] = (age_text["ru"][0], "Онлайн-выборка после проверки качества, с самостоятельным отбором участников.\nПолосы: центральные 50% результатов; точки: среднее индивидуальных баллов.", *age_text["ru"][2:4], "Полосы = 25–75-й процентили; точки = средний индивидуальный балл. Это не доверительные интервалы.")
for language, (title, subtitle, xlabel, labels, note) in age_text.items():
    rows = data["ages"]
    fig, ax = setup(title, subtitle, len(rows), left=.24)
    fig.subplots_adjust(bottom=.31)
    for i, row in enumerate(rows):
        y = len(rows) - 1 - i
        ax.plot([float(row["p25"]), float(row["p75"])], [y, y], color=pale, lw=9, solid_capstyle="round")
        ax.scatter(float(row["meanIQ"]), y, color=blue, s=70, zorder=3)
        ax.text(116.4, y, f'n = {int(row["n"]):,}', va="center", fontsize=10)
    ax.set_yticks(range(len(rows)), labels[::-1])
    ax.set_xlim(75, 133)
    ax.set_xticks([80, 90, 100, 110])
    ax.set_ylim(-.55, len(rows) - .45)
    ax.set_xlabel(xlabel, labelpad=12)
    fig.text(.05, .14, note, fontsize=9.3, color=ink)
    age_limits = {"en": "Sampling bias remains; quality screening is not psychometric validation.",
                  "fr": "Le biais de sélection demeure ; le filtrage qualité n’est pas une validation psychométrique.",
                  "ru": "Смещение выборки сохраняется; проверка качества не означает психометрическую валидность."}
    age_sources = {"en": source, "fr": "Source : CSV agrégés publics UniversalIQTest • Capture du 10 octobre 2026",
                   "ru": "Источник: открытые агрегированные CSV UniversalIQTest • Снимок от 10 октября 2026 г."}
    if current:
        age_sources = {"en": source, "fr": f"Source : CSV agrégés UniversalIQTest • Capture : {snapshot_date}", "ru": f"Источник: агрегированные CSV UniversalIQTest • Снимок: {snapshot_date}"}
    fig.text(.05, .10, age_limits[language], fontsize=9.2, color=ink)
    fig.text(.05, .055, age_sources[language], fontsize=9, color="#566b7e")
    description = f'Four age bands, quality-screened n={sum(int(r["n"]) for r in rows):,}. ' + "; ".join(
        f'{r["ageRange"]}: group score {r["meanIQ"]}, p25–p75 {r["p25"]}–{r["p75"]}, n={r["n"]}' for r in rows)
    save(fig, f"age-spread-{language}", title, description)

country_text = {
 "en": ("Selected cohorts: show sample size with every score", "Age-normalized scores from self-selected, quality-screened online results.\nSelected countries in country-code order; this is not a ranking of populations.", "Transformed group score", {"BG":"Bulgaria", "CZ":"Czechia", "FR":"France", "IT":"Italy", "PL":"Poland", "PT":"Portugal", "RU":"Russia", "SK":"Slovakia", "UA":"Ukraine"}),
 "it": ("Campioni selezionati: mostrare sempre la numerosità", "Punteggi normalizzati per età, da test online auto-selezionati dopo il filtro qualità.\nPaesi selezionati in ordine alfabetico del codice; non è una classifica delle popolazioni.", "Punteggio di gruppo trasformato", {"BG":"Bulgaria", "CZ":"Cechia", "FR":"Francia", "IT":"Italia", "PL":"Polonia", "PT":"Portogallo", "RU":"Russia", "SK":"Slovacchia", "UA":"Ucraina"}),
 "pl": ("Wybrane próby: liczebność przy każdym wyniku", "Wyniki z dobrowolnych testów online po kontroli jakości, z normalizacją względem wieku.\nKolejność według kodu kraju; to nie jest ranking inteligencji populacji.", "Przekształcony wynik grupy", {"BG":"Bułgaria", "CZ":"Czechy", "FR":"Francja", "IT":"Włochy", "PL":"Polska", "PT":"Portugalia", "RU":"Rosja", "SK":"Słowacja", "UA":"Ukraina"})
}
if current:
    for language, label in {"en": "Mean individual scaled score", "it": "Media dei punteggi individuali", "pl": "Średni wynik indywidualny"}.items():
        title, subtitle, _, names = country_text[language]
        country_text[language] = (title, subtitle, label, names)
for language, (title, subtitle, xlabel, names) in country_text.items():
    rows = [r for r in data["countries"] if int(r["validatedN"]) >= 200]
    fig, ax = setup(title, subtitle, len(rows), left=.22)
    minimum = min(float(row["ciLower"]) for row in rows)
    maximum = max(float(row["ciUpper"]) for row in rows)
    label_x = maximum + 1
    for i, row in enumerate(rows):
        y = len(rows) - 1 - i
        mean, low, high = (float(row[k]) for k in ("meanIQ", "ciLower", "ciUpper"))
        ax.errorbar(mean, y, xerr=[[mean - low], [high - mean]], fmt="o", color=blue, capsize=4, markersize=6, lw=2)
        ax.text(label_x, y, f'n = {int(row["validatedN"]):,}', va="center", fontsize=10)
    ax.set_yticks(range(len(rows)), [names[r["countryCode"]] for r in rows][::-1])
    ax.set_xlim(minimum - 1, label_x + 4)
    ax.set_ylim(-.55, len(rows) - .45)
    ax.set_xlabel(xlabel, labelpad=12)
    country_notes = {
        "en": ("Bars: exported approximate 95% intervals, based on IQR-derived spread and sample size.",
               "Intervals omit selection bias; confidence coverage for the transformed statistic is unvalidated.", source),
        "it": ("Barre: intervalli approssimati al 95%, basati sulla dispersione stimata dall’IQR e sulla numerosità.",
               "Gli intervalli non includono il bias di selezione; la copertura per questa statistica non è validata.",
               "Fonte: CSV aggregati pubblici UniversalIQTest • Dati acquisiti il 10 ottobre 2026"),
        "pl": ("Przedziały: przybliżone 95%, obliczone z rozstępu kwartylowego i liczebności próby.",
               "Nie obejmują błędu selekcji; pokrycie dla przekształconej statystyki nie zostało zweryfikowane.",
               "Źródło: publiczne agregaty CSV UniversalIQTest • Zapis z 10 października 2026")}
    if current:
        country_notes = {
            "en": ("Bars: exported approximate 95% intervals, using sample SD of individual scores and sample size.", "Intervals omit selection bias and measurement uncertainty; population coverage is unvalidated.", source),
            "it": ("Barre: intervalli approssimati al 95%, dalla deviazione standard campionaria dei punteggi individuali.", "Non includono bias di selezione ed errore di misura; la copertura della popolazione non è validata.", f"Fonte: CSV aggregati UniversalIQTest • Acquisizione: {snapshot_date}"),
            "pl": ("Przedziały: przybliżone 95%, obliczone z odchylenia standardowego wyników indywidualnych i liczebności.", "Nie obejmują błędu selekcji ani pomiaru; pokrycie populacyjne nie zostało zweryfikowane.", f"Źródło: agregaty CSV UniversalIQTest • Zapis: {snapshot_date}"),
        }
    for ypos, text in zip((.14, .10, .055), country_notes[language]):
        fig.text(.05, ypos, text, fontsize=9.2, color=ink)
    description = "Not national population estimates. " + "; ".join(
        f'{r["countryCode"]}: score {r["meanIQ"]}, approximate interval {float(r["ciLower"]):.2f}–{float(r["ciUpper"]):.2f}, n={r["validatedN"]}' for r in rows)
    save(fig, f"country-samples-{language}", title, description)

rows = data["countries"]
screening_subtitle = "Share of included reference-cohort tests passing the automated quality checks.\nThis measures screening coverage, not intelligence or a psychometric validity rate." if current else "Share of all recorded tests retained by the site’s automated quality rules.\nThis measures screening coverage, not intelligence or a psychometric validity rate."
fig, ax = setup("The screening step changes the country samples", screening_subtitle, len(rows), left=.22)
for i, row in enumerate(rows):
    y = len(rows) - 1 - i
    rate = float(row["validationRate"])
    ax.barh(y, rate, color=blue, height=.5)
    ax.text(rate + 1.2, y, f'{rate:.1f}%  ({int(row["validatedN"]):,}/{int(row["allN"]):,})', va="center", fontsize=9.5)
ax.set_yticks(range(len(rows)), [country_text["en"][3][r["countryCode"]] for r in rows][::-1])
max_rate = max(float(row["validationRate"]) for row in rows)
ax.set_xlim(0, max_rate + 28)
ticks = list(range(0, int(max_rate) + 1, 10))
ax.set_xticks(ticks)
ax.set_xticklabels([f"{tick}%" for tick in ticks])
ax.set_xlabel("Quality-screened tests / included reference-cohort tests" if current else "Quality-screened tests / all recorded tests", labelpad=12)
examples = [row for row in rows if row["countryCode"] in ("PT", "PL")]
example_note = "; ".join(f'{country_text["en"][3][row["countryCode"]]}: {int(row["validatedN"]):,} of {int(row["allN"]):,} ({float(row["validationRate"]):.1f}%)' for row in examples)
fig.text(.05, .14, example_note, fontsize=9.3, color=ink)
fig.text(.05, .10, "Aggregate exports alone cannot explain why retention differs or correct selection bias.", fontsize=9.3, color=ink)
fig.text(.05, .055, source, fontsize=9, color="#566b7e")
save(fig, "country-screening-en", "The screening step changes the country samples",
     "; ".join(f'{r["countryCode"]}: {r["validationRate"]}%, {r["validatedN"]} of {r["allN"]}' for r in rows))
(out / "runtime.json").write_text(json.dumps({"python": sys.version, "matplotlib": matplotlib.__version__}, indent=2) + "\n", encoding="utf-8")
print(f"Rendered 7 charts in PNG, SVG and PDF to {out}")
