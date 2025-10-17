
---

# 🏗️ Ultimate Python Project Architect

A modern, **full-stack scaffold** for real-world apps:

* ⚙️ **FastAPI** backend — modular, typed, production-grade
* 🎨 **React + TypeScript + Vite + ShadCN UI** frontend — ultra-fast and extendable
* 🐳 **Docker-ready** dev & deployment environment
* 🧩 **Copier-based** scaffolding for instant reuse across projects
* 🧪 Testing, linting, and pre-commit workflows baked in

> Build once. Clone endlessly. Ship clean code every time.

---

## 📐 Architecture Overview

```
my_epic_app/
├── .env
├── .gitignore
├── README.md
├── docker-compose.yml
│
├── backend/                     # 🧠 FastAPI backend
│   ├── Dockerfile
│   ├── pyproject.toml
│   ├── requirements.txt
│   ├── settings.py
│   └── app/
│       ├── main.py              # Entrypoint (FastAPI app)
│       ├── core/
│       │   └── logging_setup.py
│       ├── api/
│       │   └── routes.py
│       ├── models/
│       │   └── base.py
│       ├── services/
│       │   └── openai_client.py
│       ├── utils/
│       │   └── file_ops.py
│       └── tests/
│           └── test_smoke.py
│
├── frontend/                    # 🎨 React + TS + Vite + ShadCN
│   ├── Dockerfile
│   ├── index.html
│   ├── package.json
│   ├── tsconfig.json
│   ├── tsconfig.app.json
│   ├── vite.config.ts
│   ├── .env.example
│   ├── src/
│   │   ├── main.tsx
│   │   ├── App.tsx
│   │   └── lib/
│   │       └── api.ts
│   └── public/
│       └── .gitkeep
│
└── .github/
    └── workflows/
        ├── test.yml
        └── deploy.yml
```

---

## 🚀 How to Scaffold a New Project

Use **Copier** to clone this architecture as a ready-to-build template.

### ✨ Prerequisites

* Python ≥ 3.10
* Node.js ≥ 18
* [Copier](https://copier.readthedocs.io/en/stable/)
  ```bash
  pip install copier
  ```

### 🧙‍♂️ Generate Your Own Project

```bash
copier copy gh:PyDevIan/ultimate-python-project-template my_new_project
```

During the prompt:

* Enter project name
* Enter project slug (folder name)

You’ll end up with a fresh, minimal, production-ready folder structure.

---

## 🐍 Backend Setup

```bash
cd my_new_project/backend
python -m venv .venv
source .venv/bin/activate  # or .venv\Scripts\activate on Windows
pip install -r requirements.txt
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

Logs automatically go to `backend/data/logs/app.log` via Loguru.

---

## ⚛️ Frontend Setup

```bash
cd my_new_project/frontend
cp .env.example .env
npm install
npm run dev
```

Then open [http://localhost:5173](http://localhost:5173/).

The app will auto-proxy API calls to your FastAPI backend on port 8000.

---

## 🐳 Docker Workflow (Optional)

Spin up both services together:

```bash
docker-compose up --build
```

* **Frontend** served on `http://localhost:5173`
* **Backend** available at `http://localhost:8000`

Both containers use the same `.env` configuration for consistency.

---

## 🧪 Developer Tools

| Task                     | Command                        |
| ------------------------ | ------------------------------ |
| Run backend tests        | `pytest backend/app/tests`   |
| Run linter & formatter   | `pre-commit run --all-files` |
| Install pre-commit hooks | `pre-commit install`         |
| Start both services      | `docker compose up --build`  |

---

## 🧩 Extend the Template

* Add Postgres or Redis services in `docker-compose.yml`
* Modify `vite.config.ts` proxy to match your backend routes
* Extend `copier.yaml` to include prompts for custom stacks (e.g. auth, AI, analytics)

---

## 🧠 Tech Highlights

* **Backend:** FastAPI · Loguru · Pytest · Pydantic Settings
* **Frontend:** React · Vite · TypeScript · Tailwind CSS · ShadCN UI
* **Tooling:** ESLint · Prettier · Docker · Copier · Pre-commit · GitHub Actions

---

## 💬 Need Help?

Open an issue or fork the template.

This scaffold is designed for **AI-driven, API-heavy, and data-intensive apps** — stable, scalable, and dev-friendly.
