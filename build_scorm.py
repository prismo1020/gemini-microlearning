"""Build a SCORM 1.2 ZIP using only Python's standard library."""
from pathlib import Path
from zipfile import ZipFile, ZIP_DEFLATED
import xml.etree.ElementTree as ET
ROOT = Path(__file__).resolve().parent
manifest = ET.parse(ROOT / 'imsmanifest.xml')
files = ['imsmanifest.xml'] + [n.attrib['href'] for n in manifest.iter() if n.tag.endswith('}file')]
output = ROOT / 'prompt-it-scorm12.zip'
with ZipFile(output, 'w', ZIP_DEFLATED) as archive:
    for name in files:
        path = ROOT / name
        if not path.is_file():
            raise FileNotFoundError(name)
        archive.write(path, name)
print(f'Built {output.name}: {len(files)} files')
