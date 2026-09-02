import json
from collections import Counter
from pathlib import Path
data=json.loads(Path('/workspace/well-lab-index/data/labs-wi.json').read_text())
meta=json.loads(Path('/tmp/wi-build/meta.json').read_text())
print('cats', Counter(l['category'] for l in data['labs']))
print('verified', [(l['name'], l['phone']) for l in data['labs'] if l.get('accepts_private_well_samples')=='yes'])
print('lab_count', data['lab_count'], 'verified_count', data['verified_private_well_count'])
print('health_bacti', len(meta['health_bacti']), 'commercial_bacti', len(meta['commercial_bacti']))
for b in meta['commercial_bacti']:
    if 'COUNTY' in b['name'].upper() or 'PARKS' in b['name'].upper():
        print('commercial county?', b['name'])
