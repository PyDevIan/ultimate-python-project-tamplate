# 🏗️ Ultimate Python Project Architect

A modern, full-stack project scaffold combining:

- ⚙️ **FastAPI** for scalable, Pythonic backend APIs
- 🎨 **React + Vite + Tailwind CSS + ShadCN UI** for lightning-fast frontend development
- 🐳 Docker-based dev environments for backend and frontend
- 🧪 Integrated testing, CI/CD workflows, and modular architecture

> Designed for teams and individuals who want production-grade structure from day zero.

---

## 📐 Architecture Overview



my_epic_app/

├── .env                         # 🔐 Environment variables

├── .gitignore                   # 🧼 Git & environment hygiene

├── LICENSE                      # 📜 Choose your license

├── README.md                    # 📘 This file

├── docker-compose.yml           # 🐳 Orchestration of services

├── .pre-commit-config.yaml      # ✅ Autoformat, lint, etc.

├── backend/                     # 🧠 FastAPI backend app

│   ├── main.py                  # Entrypoint

│   ├── config.py, settings.py   # Config system

│   ├── requirements.txt, pyproject.toml

│   ├── Dockerfile

│   └── app/                     # Modular architecture

│       ├── api/, core/, db/, models/, services/, utils/

│       └── tests/               # Pytest-based

├── frontend/                    # 🎨 React + Vite + Tailwind + ShadCN UI

│   ├── src/                     # Pages, components, hooks, etc.

│   ├── vite.config.ts, tailwind.config.js, shadcn.config.js

│   ├── Dockerfile, README.md

│   └── public/

├── scripts/                     # 🛠 CLI tools & automation

│   ├── seed_data.py, generate_openapi.py

├── docs/                        # 📚 Markdown documentation

│   └── architecture.md, usage.md, etc.

└── .github/                     # 🚀 GitHub Actions (CI/CD)

└── workflows/

├── test.yml

└── deploy.yml


## 🚀 How to Scaffold a New Project

You can use this repository as a **Copier template** to instantly scaffold your own project.

### ✨ Prerequisites

- Python 3.8+
- Node.js 18+
- [Copier](https://copier.readthedocs.io/en/stable/) installed:

```


```bash
pip install copier
```

---

### 🧙‍♂️ Scaffold Your Own Project

```bash
copier copy gh:PyDevIan/ultimate-python-project-template my_new_project
```

This will prompt you to enter:

* Project name
* Project slug (used as folder name)
* Replace my_new_project with your preffered name

Once done, you'll have your own fresh copy of the architecture in `my_new_project/`.

---

### 📦 Frontend Installation

After generation:

```bash
cd my_new_project/frontend
npm install
npm run dev
```

> Tailwind CSS and ShadCN UI are already preconfigured. You're ready to build immediately.

---

### 🐍 Backend Setup

In a separate terminal:

```bash
cd my_new_project/backend
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
uvicorn main:app --reload
```

---

### 🐳 Use Docker (Optional)

Spin up backend + frontend together:

```bash
docker-compose up --build
```

---

### ✅ Testing & Dev Tools

* Lint, format, type-check using [Pre-commit](https://pre-commit.com/):
  ```bash
  pre-commit install
  pre-commit run --all-files
  ```
* Run backend tests:
  ```bash
  cd backend
  pytest
  ```

---

## 🧩 Customization

This template is built with flexibility in mind. You can:

* Modify `copier.yaml` to prompt for additional setup logic
* Extend `docker-compose.yml` to support Postgres, Redis, etc.
* Use conditionals in Jinja (`{% if %}`) to toggle features like frontend, tests, CI/CD

---

## 🧠 Credits & Inspirations

* [Copier](https://copier.readthedocs.io/)
* [FastAPI](https://fastapi.tiangolo.com/)
* [Vite](https://vitejs.dev/)
* [Tailwind CSS](https://tailwindcss.com/)
* [ShadCN UI](https://ui.shadcn.dev/)
* [Ruff](https://docs.astral.sh/ruff/)
* [Pytest](https://docs.pytest.org/)
* [Pre-commit](https://pre-commit.com/)

---

## 💬 Need Help?

Feel free to open issues, fork the template, or contribute. This project is battle-tested for full-stack Python excellence.
