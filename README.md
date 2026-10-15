# Vektor Advisors — Client Audits

Static site served by Cloudflare Pages at **https://audits.vektoradvisors.org**.
Each client audit lives at `https://audits.vektoradvisors.org/<client-slug>/`.

## Conventions
- **One folder per audit**, named with a lowercase slug (letters, digits, hyphens): `kirby/index.html`, `sante/index.html`, `b-and-b-butchers/index.html`.
- **Pages are fully self-contained single HTML files**: inline CSS and JS. Google Fonts is the only allowed external resource.
- **Never add a page that lists or links to all clients.** The root `index.html` is a holding page and must not reference any audit.
- No analytics, trackers, or third-party scripts.
- Do not touch the root domain `vektoradvisors.org`; it is reserved for the main website.

## Privacy
- `robots.txt` disallows all crawlers.
- `_headers` sends `X-Robots-Tag: noindex` on every path.
- Audits are unlisted, not secret: anyone with the link can view them.

## Adding an audit
1. Create `<slug>/index.html` (self-contained).
2. `python3 scripts/qr.py <slug>` → writes `qr/<slug>.png` pointing at `https://<domain>/<slug>/` (domain from `config.json`).
3. Commit and push to `main`; Cloudflare Pages deploys automatically.

## Deployment
Cloudflare Pages, connected to this repo: framework preset None, no build command, output directory `/`, custom domain `audits.vektoradvisors.org`.
