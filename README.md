# Axiopedia

Static site for **Axiopedia** — age-appropriate summaries from the Stanford Encyclopedia of Philosophy.

## Local preview

```bash
python -m http.server 5173
```

Open `http://localhost:5173/`.

## Data

Articles load from `public_export.json` in this folder.

To refresh articles from the pipeline repo:

```bash
# from phil-encyclopedia root
phil-encyclopedia export-public --output data/public_export.json
cp data/public_export.json apps/web/public_export.json
```

Then commit and push this repo so Netlify redeploys.

## Netlify

- Publish directory: `/` (repo root)
- No build command
- Deploy on every push to `main`
