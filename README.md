# retrofun
Code from my "[SQLAlchemy 2 In Practice](https://amzn.to/3S0diwc)" book.

[![SQLAlchemy 2 In Practice](https://blog.miguelgrinberg.com/static/sqlalchemy-small.png)](https://amzn.to/3S0diwc)

## Environment Setup

This project uses [uv](https://docs.astral.sh/uv/) for dependency management.

### 1. Install uv

If you don't have uv installed, install it first:

**Linux/macOS:**
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

**Windows:**
```powershell
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

**Or with pip:**
```bash
pip install uv
```

### 2. Clone the repository

```bash
git clone https://github.com/miguelgrinberg/retrofun.git
cd retrofun
```

### 3. Install dependencies

Install the base dependencies:

```bash
uv sync
```

This creates a `.venv` virtual environment and installs all required packages.

### 4. Install optional dependencies (if needed)

For **FastAPI** examples (chapter 9):
```bash
uv sync --extra fastapi
```

For **Flask** examples (chapter 9):
```bash
uv sync --extra flask
```

To install both:
```bash
uv sync --extra fastapi --extra flask
```

### 5. Run scripts

Use `uv run` to execute scripts within the virtual environment:

```bash
uv run python chapter2/db.py
```

Or activate the virtual environment manually:

**Linux/macOS:**
```bash
source .venv/bin/activate
python chapter2/db.py
```

**Windows:**
```cmd
.venv\Scripts\activate
python chapter2/db.py
```

### 6. Set up environment variables

Some scripts require a `DATABASE_URL` environment variable. Create a `.env` file in the project root:

```bash
DATABASE_URL=sqlite:///app.sqlite
```

Or set it directly:

```bash
export DATABASE_URL=sqlite:///app.sqlite  # Linux/macOS
set DATABASE_URL=sqlite:///app.sqlite     # Windows cmd
$env:DATABASE_URL="sqlite:///app.sqlite"  # Windows PowerShell
```
