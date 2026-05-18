# DinDoZo — Backend

Personal finance system built to import, categorize and analyze Nubank transactions.

---

## Tech Stack

- **Python** — main language
- **FastAPI** — REST API framework
- **SQLAlchemy** — ORM
- **SQLite** — database
- **Alembic** — database migrations
- **Pandas** — CSV parsing and data manipulation
- **Pydantic** — data validation

---

## Features

- Import CSV exports from Nubank (checking account and credit card)
- Automatic transaction categorization based on keyword rules
- Category and rule management
- Transaction listing with pagination and month/year filtering
- Dashboard KPIs (total income, expenses and balance)
- Import log with categorization stats

---

## Project Structure

```
dindozo-backend/
│
├── app/
│   ├── main.py
│   ├── api/
│   │   └── routes/
│   │       ├── categories.py
│   │       ├── transactions.py
│   │       ├── imports.py
│   │       ├── rules.py
│   │       └── summary.py
│   ├── core/
│   │   ├── config.py
│   │   └── database.py
│   ├── models/
│   │   ├── category.py
│   │   ├── transaction.py
│   │   ├── import_log.py
│   │   └── categorization_rules.py
│   ├── schemas/
│   │   ├── category.py
│   │   ├── transaction.py
│   │   ├── import_log.py
│   │   ├── rules.py
│   │   └── summary.py
│   ├── services/
│   │   ├── csv_parser.py
│   │   ├── categorizer.py
│   │   └── summary.py
│   └── repositories/
│       ├── category.py
│       ├── transaction.py
│       ├── import_log.py
│       └── rules.py
│
├── alembic/
├── tests/
├── .env.example
├── .gitignore
├── alembic.ini
└── requirements.txt
```

---

## Getting Started

**1. Clone the repository**
```bash
git clone https://github.com/seu-usuario/dindozo-backend.git
cd dindozo-backend
```

**2. Create and activate virtual environment**
```bash
python -m venv venv

# Windows
.\venv\Scripts\activate

# Linux/Mac
source venv/bin/activate
```

**3. Install dependencies**
```bash
pip install -r requirements.txt
```

**4. Configure environment variables**
```bash
cp .env.example .env
```

Edit `.env`:
```
DB_URL=sqlite:///./dindozo.db
APP_NAME=DinDoZo
```

**5. Run migrations**
```bash
alembic upgrade head
```

**6. Start the server**
```bash
uvicorn app.main:app --reload
```

API will be available at `http://localhost:8000`
Interactive docs at `http://localhost:8000/docs`

---

## API Endpoints

### Categories
| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/api/categories` | List all categories |
| GET | `/api/categories/{id}` | Get category by id |
| POST | `/api/categories` | Create category |
| DELETE | `/api/categories/{id}` | Delete category |

### Transactions
| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/api/transactions` | List transactions (supports `skip`, `limit`, `month`, `year`) |
| GET | `/api/transactions/{id}` | Get transaction by id |
| POST | `/api/transactions` | Create manual transaction |

### Rules
| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/api/rules` | List all categorization rules |
| POST | `/api/rules` | Create rule |
| DELETE | `/api/rules/{id}` | Delete rule |

### Imports
| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/api/imports` | Upload and process Nubank CSV |

### Summary
| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/api/summary` | Get dashboard KPIs (supports `month`, `year`) |

---

## How CSV Import Works

1. Upload a Nubank CSV (checking account or credit card format)
2. Python reads and normalizes the data
3. Each transaction is matched against categorization rules
4. Unmatched transactions get `category_id: null`
5. All transactions are saved to the database
6. An import log is created with stats

---

## Environment Variables

| Variable | Description | Example |
|----------|-------------|---------|
| `DATABASE_URL` | SQLite connection string | `sqlite:///./dindozo.db` |
| `APP_NAME` | Application name | `DinDoZo` |
| `DEBUG` | Debug mode | `True` |