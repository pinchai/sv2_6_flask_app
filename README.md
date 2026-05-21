# Flask E-commerce Application

A simple e-commerce web application built with Python and Flask. This project serves as a demonstration of a multi-page web application with product listings, product details, and user account pages.

## Tech Stack

- **Language:** Python
- **Framework:** [Flask](https://flask.palletsprojects.com/)
- **Templating:** Jinja2
- **Styling:** Bootstrap & Custom CSS
- **Data:** Static JSON-like data in `product.py`

## Project Structure

```text
sv2_6_flask_app/
├── static/                 # Static assets
│   ├── image/             # Product images
│   └── style/             # CSS files (Bootstrap & Custom)
├── templates/              # Jinja2 templates
│   └── front/             # Frontend page templates
│       └── share/         # Shared components (Header, Footer, Navbar)
├── app.py                  # Main application entry point
├── product.py              # Static product data
├── requirements.txt        # Project dependencies
└── README.md               # Project documentation
```

## Requirements

- Python 3.x
- pip (Python package manager)

## Setup & Installation

1. **Clone the repository:**
   ```bash
   git clone <repository-url>
   cd sv2_6_flask_app
   ```

2. **Create a virtual environment (optional but recommended):**
   ```bash
   python -m venv venv
   # On Windows:
   .\venv\Scripts\activate
   # On macOS/Linux:
   source venv/bin/activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

## Running the Application

To start the Flask development server, run:

```bash
python app.py
```

The application will be accessible at `http://127.0.0.1:5000/`.

## Available Routes

- `/` or `/home`: Home page with product listings.
- `/products`: Full product list.
- `/product/<product_id>`: Individual product details (TODO: Implement dynamic data loading for this route).
- `/cart`: Shopping cart page.
- `/checkout`: Checkout page.
- `/account`: User account page.
- `/login`: User login page.
- `/create-user`: User registration page.
- `/forgot-password`: Password recovery page.

## Scripts & Tasks

- **Development Server:** `python app.py` starts the local development server.
- **Tests:** TODO: Add unit and integration tests.

## Environment Variables

Currently, the application does not use external environment variables. 
TODO: Implement `.env` support for configuration (e.g., `FLASK_ENV`, `SECRET_KEY`).

## License

TODO: Add license information.
