# Maillist
Libraries and utilities for checking and cleaning email lists

## Introduction

Provides a pluggable framework for checking the validity of email addresses. Validators currently exist for:

-   Syntax
-   Host MX Record

This is still work in progress and I have plans of extending this to include validators that communicate directly with the SMTP servers to confirm the validity of an email address.

Its key features are its extensibility and scalebility. Host and SMTP validation requires a lot of network calls with high latency. To overcome this problem the application uses `futures` to validate an email list concurrently, resulting in a dramatic speed up.

## Installation

Check out the maillist directory to a location on your `PYTHONPATH`. Then symlink to the `maillist` script in a directory in your `PATH`:

```bash
cd bin
ln -s ../lib/python/maillist/bin/maillist .
```

## Usage

```bash
maillist -h
usage: maillist [-h] [-i INPUT] [-o OUTPUT] [-c] [-m MAX_WORKERS] [-v]

Creates a maillist of unique email addresses together with their respective
counts.

optional arguments:
  -h, --help            show this help message and exit
  -i INPUT, --input INPUT
                        The list of email addresses
  -o OUTPUT, --out OUTPUT
                        The file where the unparseable lines should be written
                        (default: write to stdout)
  -c, --check           Run all validator checks
  -m MAX_WORKERS, --max_workers MAX_WORKERS
                        Maximum number of worker threads to use
  -v, --verbose         output parse errors

```
Examples

```bash
# de-duplicates a list of email addresses
maillist -i subscribers.csv -o subscribers_counts.csv
# de-duplicate and validate
maillist -v -c -i subscribers.csv -o subscribers_counts.csv
```

## Testing

```bash
cd maillist
python3 -m maillist.tests.syntax_test
```

## Requirements

1.  Python 3.4+
1.  python3-dns
