# lib/cli.py

from lib.database import session, Base, engine
from lib.models import Category, Product

def init_db():
    """Initialize the database tables."""
    Base.metadata.create_all(engine)

def menu():
    """Display the main CLI menu and loop until the user exits."""
    init_db()
    print("Welcome to the Inventory Management CLI!")
    
    while True:
        print("\n--- Main Menu ---")
        print("1. Create Category")
        print("2. Create Product")
        print("3. View All Categories")
        print("4. View All Products")
        print("5. Find Product by Name")
        print("6. Delete Product")
        print("7. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            create_category()
        elif choice == "2":
            create_product()
        elif choice == "3":
            view_categories()
        elif choice == "4":
            view_products()
        elif choice == "5":
            find_product()
        elif choice == "6":
            delete_product()
        elif choice == "7":
            print("Later, skater!")
            break
        else:
            print("Invalid option. Try again.")

def create_category():
    name = input("Enter category name: ").strip()
    if not name:
        print("Category name cannot be empty.")
        return
    category = Category(name=name)
    session.add(category)
    session.commit()
    print(f"Created category: {category}")

def create_product():
    name = input("Enter product name: ").strip()
    if not name:
        print("Product name cannot be empty.")
        return
    
    try:
        quantity = int(input("Enter quantity: "))
        price = float(input("Enter price: "))
    except ValueError:
        print("Quantity must be an integer and price must be a number.")
        return

    # Show available categories for selection
    view_categories()
    try:
        category_id = int(input("Enter category ID for the product: "))
    except ValueError:
        print("Invalid category ID.")
        return
    
    category = session.query(Category).filter_by(id=category_id).first()
    if not category:
        print("Category not found.")
        return

    product = Product(name=name, quantity=quantity, price=price, category=category)
    session.add(product)
    session.commit()
    print(f"Created product: {product}")

def view_categories():
    categories = session.query(Category).all()
    if not categories:
        print("No categories found.")
    else:
        print("\nCategories:")
        for c in categories:
            print(c)

def view_products():
    products = session.query(Product).all()
    if not products:
        print("No products found.")
    else:
        print("\nProducts:")
        for p in products:
            print(p)

def find_product():
    name = input("Enter product name to search: ").strip()
    products = session.query(Product).filter(Product.name.like(f"%{name}%")).all()
    if not products:
        print("No matching products found.")
    else:
        print("\nFound Products:")
        for p in products:
            print(p)

def delete_product():
    try:
        product_id = int(input("Enter product ID to delete: "))
    except ValueError:
        print("Invalid ID.")
        return
    product = session.query(Product).filter_by(id=product_id).first()
    if not product:
        print("Product not found.")
    else:
        session.delete(product)
        session.commit()
        print(f"Deleted product: {product}")

if __name__ == '__main__':
    menu()
