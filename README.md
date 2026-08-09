# PrismaCore

The API layer of Prismalite's bot system. An open-source project built to provide the architecture to expand PrismaBot to any platform.

## Features

* Supabase connection

## Tech Stack

* **Language:** Python
* **Database:** Supabase (PostgreSQL)

## Development

This repository contains the source code for PrismaCore.

Branches:

* `dev` (DEFAULT) - Active development branch used for testing new features
* `main` - Stable version, ready for use.

## Setup

1. Clone the repository:

```bash
git clone <repository-url>
cd PrismaBot
```

2. Create a virtual environment:

```bash
python -m venv .venv
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Add your environment variables/configuration files.

5. Run the bot:

```bash
uvicorn main:app --host 0.0.0.0 --port 8000
```

## Notes

This project is in early development and is not currently live.