# Helpful Bot

A console personal assistant for contacts, phone numbers, and birthdays.

The app runs only as an interactive command-line program. It does not need an HTTP port.

## Requirements

- Python 3.13
- [Poetry](https://python-poetry.org/docs/#installation) 2.x

## Local setup

1. Install dependencies (Poetry creates the virtual environment):

```bash
poetry install
```

2. Run the assistant:

```bash
poetry run python src/main.py
```

Type `exit` or `close` to quit.

## Docker

Build the image:

```bash
docker build -t helpful-bot .
```

Run it interactively (`-it` is required because the bot reads commands from the terminal):

```bash
docker run -it --rm helpful-bot
```
