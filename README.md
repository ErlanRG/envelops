# Envelopes

Web application to calculate how much to add to each savings envelope based on your monthly budget.

## How it works

You define envelopes with their monthly amount and an optional cap. Then you
enter how much you currently have in each one, and the app instantly calculates
how much to add:

- **Without a cap**: always adds `monthly_amount / 2`
- **With a cap**: adds up to `cap / 2`, without exceeding `monthly_amount / 2`

## Requirements

- Python 3.10+
- Flask

## Installation

```bash
git clone <repo>
cd envelopes
python3 -m venv .venv
.venv/bin/pip install -r requirements.txt
```

## Usage

```bash
.venv/bin/python app.py
```

Open http://localhost:5000

## Configuration

Optional environment variables:

| Variable | Default | Description |
|----------|---------|-------------|
| `ENVELOPES_PATH` | `data/envelopes.json` | Path to the data file |
| `SECRET_KEY` | `change-this-to-a-random-secret-in-production` | Flask secret key |
