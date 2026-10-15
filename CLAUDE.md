# Instructions for Claude

This repo hosts private Vektor Advisors client audit pages (Cloudflare Pages, `audits.vektoradvisors.org`). See README.md. Rules:

- Each audit goes in its own folder named with a lowercase slug: `<slug>/index.html` (e.g. `sante/`, `b-and-b-butchers/`). Never rename or move existing audit folders; their URLs are printed on QR codes.
- Audit pages are single self-contained HTML files: inline CSS and JS only. Google Fonts is the only permitted external resource.
- Never create any page, sitemap, or index that lists or links to clients. The root `index.html` stays a holding page with no audit links.
- Keep `robots.txt` (Disallow: /) and `_headers` (X-Robots-Tag: noindex) intact.
- No analytics, trackers, or third-party scripts.
- After adding an audit, generate its QR code: `python3 scripts/qr.py <slug>` (output in `qr/<slug>.png`).
- Do not configure anything on the root domain `vektoradvisors.org`.
- Ask before deleting anything.
