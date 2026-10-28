"""Empacota apenas este projeto; não remove nem move qualquer arquivo."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json
import zipfile

root = Path(__file__).resolve().parents[1]
out = root / 'delivery'
out.mkdir(exist_ok=True)
archive = out / 'Terra-Monitor-v1.0.zip'
files = sorted(p for p in root.rglob('*') if p.is_file() and 'delivery' not in p.relative_to(root).parts and p.name != 'refine.mjs' and '__pycache__' not in p.parts)
with zipfile.ZipFile(archive, 'w', zipfile.ZIP_DEFLATED) as z:
    for path in files:
        z.write(path, path.relative_to(root).as_posix())
target = out / ('verificacao-' + datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%S'))
target.mkdir(exist_ok=False)
with zipfile.ZipFile(archive) as z:
    assert z.testzip() is None, 'Falha CRC'
    assert 'index.html' in z.namelist(), 'Entrada fora da raiz'
    for name in z.namelist():
        resolved = (target / name).resolve()
        assert resolved.is_relative_to(target.resolve()), 'Caminho inseguro no ZIP'
    z.extractall(target)
    for path in files:
        assert hashlib.sha256(path.read_bytes()).digest() == hashlib.sha256((target / path.relative_to(root)).read_bytes()).digest(), str(path)
result = {'arquivo': str(archive), 'bytes': archive.stat().st_size, 'sha256': hashlib.sha256(archive.read_bytes()).hexdigest(), 'arquivos': len(files), 'crc': 'aprovado', 'hashes_extraidos': 'todos iguais', 'extracao': str(target)}
(out / 'integridade.json').write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding='utf-8')
print(json.dumps(result, ensure_ascii=False, indent=2))
