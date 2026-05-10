# AI Application — Product Demo API

A simple web application built with Python and Flask for managing educational products through a REST API and an HTML interface.

The project allows users to view products, search for a product by ID or name, add new products, and update product prices.

## Features

- Display all products from the database
- Search product by ID
- Search product by name
- Add a new product
- Update product price
- Web interface built with HTML, CSS, and Jinja2
- API endpoint testing using `.bat` files

## Technologies Used

- Python
- Flask
- SQLite
- HTML
- CSS
- JavaScript
- Jinja2

## Project Structure

```txt
AI-APPLICATION/
│
├── database/
│   ├── db_init.py
│   └── db.py
│
├── routes/
│   ├── add_produse.py
│   ├── frontend.py
│   ├── init.py
│   ├── update.py
│   └── view_produse.py
│
├── templates/
│   ├── adauga.html
│   ├── base.html
│   ├── cauta.html
│   ├── index.html
│   └── produse.html
│
├── tests/
│   ├── test_api1.bat
│   └── test_api2.bat
│
├── app.py
├── config.py
├── educational_products.db
├── exceptions.py
├── requirements.txt
├── service.py
├── validators.py
└── README.md
```

## Installation and Setup

Clone the repository:

```bash
git clone <repository-link>
```

Move into the project folder:

```bash
cd AI-APPLICATION
```

Create a virtual environment:

```bash
python -m venv project-venv
```

Activate the virtual environment:

```bash
project-venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
python app.py
```

The application will run locally at:

```txt
http://127.0.0.1:5000
```

or on the local network depending on the Flask configuration.

## Available Pages

```txt
/                  - home page
/pagina/produse    - display all products
/pagina/cauta      - search product
/pagina/add_produs - add product
```

## API Endpoints

### Get all products

```http
GET /produse
```

Returns all products from the database.

### Get product by ID

```http
GET /produs/<id>
```

Example:

```http
GET /produs/1
```

### Search product by name

```http
GET /produs/nume/<name>
```

Example:

```http
GET /produs/nume/Mathematics
```

### Add a new product

```http
POST /produs
```

JSON Body:

```json
{
  "name": "Mathematics",
  "price": 45
}
```

### Update product price

```http
PATCH /produs/<id>/pret
```

Example:

```http
PATCH /produs/1/pret
```

JSON Body:

```json
{
  "price": 60
}
```

## Database

The project uses SQLite, and the database is stored in:

```txt
educational_products.db
```

Database connection and initialization logic can be found inside:

```txt
database/
```

## Project Purpose

This project was created to practice core backend and frontend development concepts such as:

- building REST APIs
- working with Flask routes
- connecting to a SQLite database
- using Jinja2 templates
- sending requests with `fetch`
- validating user input
- organizing a Python project structure
