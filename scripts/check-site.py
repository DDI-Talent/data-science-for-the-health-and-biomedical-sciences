"""Check that tutorial development materials cannot leak into the built site."""
from pathlib import Path
import re
import sys
from urllib.parse import urlsplit

site = Path('docs')
errors = []
if not (site / 'index.html').exists():
    errors.append('Render the site before running this check.')
for path in site.rglob('*'):
    if not path.is_file():
        continue
    relative = path.relative_to(site)
    if 'tutorials' in relative.parts or re.search(r'tutorial(?:_week\d+)?\.html$', path.name):
        errors.append(f'Tutorial output: {relative}')
    if path.suffix in {'.html', '.json', '.xml'}:
        text = path.read_text()
        for link in re.findall(r"(?:href|src)=[\"']([^\"']+)", text):
            url = urlsplit(link)
            if not url.scheme and not url.netloc and re.search(r'(?:^|/)tutorials/|/tutorial(?:_week\d+)?\.html$', url.path):
                errors.append(f'Tutorial link: {relative}')
        if re.search(r'website-ug-data-science|Autumn 2025|STUDENT-2526|data-science-for-health-bms-24-25|24-25/dpt|2024-25 Handbook|Thursday and Friday', text):
            errors.append(f'Cohort-specific content: {relative}')
for week in range(1, 11):
    if not Path(f'tutorials/week-{week}/README.md').exists():
        errors.append(f'Missing tutorial workspace for week {week}')
if errors:
    sys.exit('\n'.join(errors))
print('Site checks passed: tutorial workspace excluded; no old cohort details.')
