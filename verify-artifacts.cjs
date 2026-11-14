const fs=require('fs'),path=require('path'),crypto=require('crypto');
const m=JSON.parse(fs.readFileSync(path.join(__dirname,'companion-manifest.json')));
for(const f of m.files){const b=fs.readFileSync(path.join(__dirname,f.path));if(b.length!==f.bytes||crypto.createHash('sha256').update(b).digest('hex')!==f.sha256)throw Error('Checksum mismatch: '+f.path);}
console.log(JSON.stringify({verifiedFiles:m.files.length,version:m.version}));
