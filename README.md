# Bem-vindo Vinicius — VinIA Cinema

Site estático de boas-vindas com **animação estilo cinema**: cortinas vermelhas abrem, título "Bem-vindo" + nome "Vinicius" aparecem com luz de projetor, e pipoca dourada cai. Hospedado em `bemvindo.vs2b.com.br` via Cloudflare + Coolify.

## Stack

- **HTML + CSS + JS puro** (sem framework)
- **Servidor:** stdlib Python (`http.server`)
- **Container:** python:3.13-alpine (~25 MB final)
- **Deploy:** Coolify via Dockerfile + GitHub

## Estrutura

```
.
├── server.py            # http.server minimalista
├── templates/
│   └── index.html       # HTML com cortinas + título
├── static/
│   ├── style.css        # animação CSS (keyframes)
│   └── script.js        # sequencia: cortinas → título → pipoca
├── Dockerfile           # multi-stage
├── .dockerignore
├── requirements.txt     # só pro metadata, sem deps externas
└── README.md
```

## Local dev

```bash
python3 server.py
# http://127.0.0.1:8000
# ou custom: PORT=8102 python3 server.py
```

## Deploy

Push pra GitHub → Coolify lê via `build_pack=dockerfile` → expõe via `bemvindo.vs2b.com.br`.

## Licença

MIT