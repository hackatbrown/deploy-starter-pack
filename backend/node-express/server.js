import express from "express"
import cors from "cors"

const app = express()
app.use(cors())
app.get("/", (_req, res) => res.json({ ok: true, service: "Hack@Brown Express" }))
app.get("/ping", (_req, res) => res.send("pong"))

const port = process.env.PORT || 3000
app.listen(port, () => console.log(`Server on :${port}`))
