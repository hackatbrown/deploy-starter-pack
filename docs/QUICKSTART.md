# Quickstart (2 minutes)

## Static site (Netlify)
1) Push `frontend/static-site` to GitHub.
2) Netlify → New site from Git → pick repo.
3) Build: none | Publish: `frontend/static-site`.

## React (Vercel)
1) Push `frontend/react-vite` to GitHub.
2) Vercel → New Project → Import repo.
3) Build: `npm run build` | Output: `dist/`.

## Next.js (Vercel)
1) Push `frontend/nextjs`.
2) Vercel detects Next.js → Deploy.
3) Env vars: Project → Settings → Environment Variables.

## Express API (Render)
1) Push `backend/node-express` (has `render.yaml`).
2) Render → New → Blueprint → select repo.
3) After deploy, open the URL → `/ping`.

## FastAPI (Render)
1) Push `backend/python-fastapi`.
2) Render → New → Blueprint.
3) Health check at `/`.

## Streamlit / Gradio (HF Spaces)
Create Space → pick Streamlit/Gradio → upload folder → it builds automatically.
