# Inventory Management System (CLI)

## Project Overview

This is a command-line Inventory Management System built with Python. It allows users to manage products and categories directly from the terminal. The application supports adding, viewing, searching, and deleting products, as well as organizing them under categories.

The system uses:

- Python 3.8+
- SQLAlchemy (Object Relational Mapper)
- SQLite (local database)
- Alembic (optional, for managing migrations)

## Features

- Add, view, and delete products
- Create and manage categories
- Products are assigned to categories (one-to-many relationship)
- Search for products by name
- User-friendly CLI with menus and input validation


shell
Copy
Edit

## Getting Started

### 1. Clone the Repository

git clone https://github.com/your-username/3proj.git
cd 3proj

mathematica
Copy
Edit

### 2. Set Up the Environment

Install pipenv if you haven't already:

pip install pipenv

yaml
Copy
Edit

Then install the dependencies:

pipenv install

cpp
Copy
Edit

Activate the virtual environment:

pipenv shell

vbnet
Copy
Edit

### 3. Set Up the Database

If you're using Alembic for migrations:

alembic upgrade head

css
Copy
Edit

Or, to create the tables manually:

```python
from app.database import Base, engine
Base.metadata.create_all(engine)
4. Run the Application
arduino
Copy
Edit
python run.py
Example Usage
Create a category such as "Books" or "Electronics"

Add products and assign them to a category

View the list of all products or categories

Search for a product by name
```

Delete a product when necessary

Author
Darwin Osingo
Moringa School — Software Development
Contact: darwin.osingo@student.moringaschool.com
