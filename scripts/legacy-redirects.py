"""Keep previously published weekly page URLs working after the folder move."""
from pathlib import Path
import html

site = Path('_site')
for source in Path('.').glob('week-*/*.qmd'):
    target = '../../' + source.with_suffix('.html').as_posix()
    destination = site / 'content' / source.with_suffix('.html')
    destination.parent.mkdir(parents=True, exist_ok=True)
    destination.write_text(
        '<!doctype html><html lang="en"><head><meta charset="utf-8">'
        '<meta name="robots" content="noindex"><title>Page moved</title>'
        f'<meta http-equiv="refresh" content="0;url={html.escape(target)}">'
        '</head><body>'
        f'<p>This page has moved. <a href="{html.escape(target)}">Continue to the lesson</a>.</p>'
        f'<script>location.replace({target!r} + location.search + location.hash);</script>'
        '</body></html>\n'
    )
