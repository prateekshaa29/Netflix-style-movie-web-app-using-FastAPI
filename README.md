# Netflix Web Demo 🎬

A simple Netflix-style web application built using FastAPI and Python.

## Features
- Movie cards UI
- JSON API
- Visitor counter
- FastAPI backend
- HTML, CSS, JavaScript frontend

## Technologies Used
- Python
- FastAPI
- Uvicorn
- HTML
- CSS
- JavaScript

## Project Structure

```bash
netflix-web-demo/
│
├── hello.py
├── server.py
├── requirements.txt
├── README.md
└── .gitignore
```

## Installation

Install required packages:

```bash
py -m pip install -r requirements.txt
```

## Run the Application

Start the server:

```bash
py -m uvicorn server:app --host 0.0.0.0 --port 8000 --reload
```

## Open in Browser

```bash
http://localhost:8000
```

## API Endpoint

```bash
http://localhost:8000/movies
```

## Screenshot

Netflix-style movie recommendation page with:
- Movie name
- Genre
- Rating
- Duration
- Language

## Author

Created by Prateekshaa 