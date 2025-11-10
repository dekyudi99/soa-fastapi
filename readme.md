# FastAPI-based Library Management API
A modular FastAPI-based Library Management API built with Python 3.11, providing structured CRUD endpoints for managing books, authors, borrowers, and borrowing transactions.

The project demonstrates clean architectural design using:
- SQLAlchemy ORM for database modeling
- Pydantic for request/response validation
- FastAPI Routers for modular API structure
- Hypercorn (HTTP/2) and Uvicorn (HTTP/1.1) for flexible async performance testing
- Locust for load benchmarking

This setup highlights scalability, performance comparison between HTTP/1.1 and HTTP/2, and clean modular patterns for extending new API modules.

## Project structure
```
app/
├── api/v1/
│   ├── router.py
│   └── routes/
│       ├── authors.py
│       ├── books.py
│       ├── borrowers.py
│       └── borrowed_books.py
├── core/
│   ├── config.py
│   └── database.py
├── models/
│   ├── author.py
│   ├── book.py
│   ├── borrower.py
│   └── borrowed_book.py
├── schemas/
│   ├── author.py
│   ├── book.py
│   ├── borrower.py
│   └── borrowed_book.py
├── main.py
├── locustfile.py
├── locustfile_http2.py
├── load_test_start.sh
├── hypercorn_start.sh
├── uvicorn_start.sh
└── requirements.txt
```

## Key Features
- FastAPI - High-performance async REST API framework
- SQLAlchemy ORM - Clean model design with soft delete support
- Pydantic - Request & response data validation
- Modular Routers - Blueprint-style routing for easy module expansion
- HTTP/2 Ready - Supports Hypercorn for HTTP/2 performance testing
- Locust Integration - Benchmark and compare HTTP/1.1 vs HTTP/2
- Environment Configuration - .env support for flexible setup

## Instalation
- `git clone git@github.com:firmangel8/soa-fastapi.git`
- `pip install -r requirements.txt`

## Run Projects

### run with uvicorn by default (without tls)
`uvicorn app.main:app --host 0.0.0.0 --port 8000`

### run with uvicorn by default (with tls)
```
uvicorn app.main:app --host 0.0.0.0 --port 8000 --ssl-keyfile=key.pem --ssl-certfile=cert.pem
```

### create certificate to enable http2
```
openssl req -x509 -newkey rsa:2048 -keyout key.pem -out cert.pem -days 365 -nodes -subj "/CN=localhost"
```

### Run with http2 (Hypercorn)
```
hypercorn app.main:app \
 --bind 127.0.0.1:8000 \
 --certfile cert.pem \
 --keyfile key.pem
```

### Check run to verify http2 enabled
`curl -v -k --http2 https://127.0.0.1:8000/api/v1/authors/`

### run project with shortuct uvicorn
`./uvicorn_start.sh`

### run project with shortuct hypercorn
`./hypercorn_start.sh`

### Run load testing
```
cd app
./load_test_start.sh
```
