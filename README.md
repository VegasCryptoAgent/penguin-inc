# Penguin Inc.

WebGL experience for **Penguin** — engineered crystal growth / synthetic crystallography.

High-purity crystals for semiconductors, lasers, optics, quantum devices, and advanced materials. Built as a static site (Svelte loader + Three.js), deployed on Vercel.

## Live

Production deploy is linked after Vercel setup (see Actions / Vercel dashboard).

## Local development

```bash
# Option A — Python SPA server
python3 server.py 5173

# Option B — any static server (portfolio routes need SPA fallback)
npx serve -s .
```

Open http://127.0.0.1:5173/

## Stack

- Static `index.html` + Vite/Svelte bootstrap
- WebGL scene (Draco meshes, KTX2 textures, Basis transcoder)
- SPA routes: `/` and `/portfolio/:project`

## Deploy (Vercel)

Static hosting with SPA rewrites in `vercel.json`. No build step required.

```bash
vercel --prod
```

## Social

- [LinkedIn](https://www.linkedin.com/in/the-bret-a74969b)
- [X / Twitter](https://x.com/6framestudios)
- [Site](https://6framestudio.com/)
