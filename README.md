# Axiopedia

Static site for **Axiopedia** — age-appropriate summaries from the Stanford Encyclopedia of Philosophy.

## Local preview

```bash
python -m http.server 5173
```

Open `http://localhost:5173/`.

## Data

The browser initially loads only `data/index.json`. Full articles in
`data/entries/` are fetched when opened.

To refresh articles from the pipeline repo:

```bash
# from phil-encyclopedia root
phil-encyclopedia export-public --output data/public_export.json
python apps/web/build_data.py data/public_export.json --output apps/web/data
```

Then commit and push this repo so Netlify redeploys.

Commit `data/index.json` and `data/entries/`, but do not commit the source
`public_export.json`, databases, caches, batch files, or environment files.

## Netlify

- Publish directory: `/` (repo root)
- No build command
- Deploy on every push to `main`
