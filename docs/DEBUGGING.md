# Debugging Deployments

- Build succeeds but 404 → wrong publish dir (`dist/`, `build/`, or root).
- Works locally, fails remotely → missing env vars; set them in project settings.
- CORS errors → add CORS middleware (Express `cors()` / FastAPI CORSMiddleware).
- Case-sensitive paths → Linux servers are case-sensitive; fix imports.
- Free tier sleeping → first request slow; warm it up before the demo.
