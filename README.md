# Lululemon Product Scraper API

## Overview
This project is a Python-based web scraper API for fetching product details from Lululemon's website. The API provides a single GET endpoint that extracts data from specified URLs and returns product details such as display name, category, image, price, currency, and URL.

## Features
 - Fetches product data from Lululemon API.
 - Caching mechanism to avoid excessive API calls.
 - RESTful API design using Django and Django REST framework.
 - Swagger documentation for easy API exploration.
 - Unit tests to ensure the correctness of the implementation.
 - Optional serverless deployment using AWS Lambda and API Gateway.

## Requirements
 - Python 3.9
 - Django
 - Django REST framework
 - Requests
 - Cachetools
 - drf-yasg (for Swagger documentation)

## Installation

### Run everything on docker

1. Clone the repository:

```bash
git clone https://github.com/plenzjr/python-web-scraper.git
cd python-web-scraper
```

2. Setup the `.env` file

```bash
cp .env-dist .env
```

3. Build and run the Docker containers:

```bash
docker-compose up -d --build
```

4. Access the API:

 - The API endpoint is available at: http://127.0.0.1:8000/api/scrape/
 - Swagger documentation is available at: http://127.0.0.1:8000/swagger/
 - ReDoc documentation is available at: http://127.0.0.1:8000/redoc/

### Running Django locally

1. Clone the repository:

```bash
git clone https://github.com/plenzjr/python-web-scraper.git
cd python-web-scraper
```

2. Create and activate a virtual environment:

```bash
python3.9 -m venv .venv
source .venv/bin/activate # On Windows use .venv\Scripts\activate
```

3. Install the dependencies:

```bash
pip install -r lululemon/requirements.txt
```

4. Setup the `.env` file

```bash
cp .env-dist .env
```

5. Run database container:


```bash
docker compose up -d db
```

6. Apply migrations:

```bash
python lululemon/manage.py migrate
```

7. Run the Django development server:

```bash
python lululemon/manage.py runserver
```

8. Access the API:

 - The API endpoint is available at: http://127.0.0.1:8000/api/scrape/
 - Swagger documentation is available at: http://127.0.0.1:8000/swagger/
 - ReDoc documentation is available at: http://127.0.0.1:8000/redoc/

## API Endpoints

### GET /api/scrape/

Fetch product data from predefined Lululemon URLs.

Response
```json
[
    {
        "displayName": "Align Pant 28",
        "category": "Women's Leggings",
        "first_image": "https://example.com/image.jpg",
        "price": 98.0,
        "currency": "USD",
        "url": "https://shop.lululemon.com/product/123"
    },
    ...
]
```

## Testing

1. Run unit test on docker:

```bash
docker-compose run web python manage.py test scraper
```

1. Run unit tests locally:

```bash
python lululemon/manage.py test scraper
```
