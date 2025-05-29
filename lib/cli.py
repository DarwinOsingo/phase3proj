from lib.database import engine, Base, session
from lib.models import Category, Product
from sqlalchemy.exc import SQLAlchemyError

# Auto-create tables if they don't exist yet
Base.metadata.create_all(engine)

def create_category():
    name = input("Enter category name: ").strip()
    if not name:
        print("Category name cannot be empty.")
        return
    try:
        category = Category(name=name)
        session.add(category)
        session.commit()
        print(f"Created category: {category}")
    except SQLAlchemyError as e:
        print(f"Error creating category: {e}")
        session.rollback()

def create_product():
    try:
        name = input("Enter product name: ").strip()
        quantity = int(input("Enter quantity: "))
        price = float(input("Enter price: "))
        category_id = input("Enter category ID: ").strip()

        if not category_id.isdigit():
            print("Category ID must be a number.")
            return
        category_id = int(category_id)

        category = session.query(Category).filter_by(id=category_id).first()
        if not category:
            print("Category not found.")
            return

        product = Product(name=name, quantity=quantity, price=price, category_id=category_id)
        session.add(product)
        session.commit()
        print(f"Created product: {product}")
    except ValueError:
        print("Invalid input. Please enter numbers where required.")
    except SQLAlchemyError as e:
        print(f"Error creating product: {e}")
        session.rollback()

def view_all_categories():
    categories = session.query(Category).all()
    if categories:
        print("\nCategories:")
        for c in categories:
            print(c)
    else:
        print("No categories found.")

def view_all_products():
    products = session.query(Product).all()
    if products:
        print("\nProducts:")
        for p in products:
            print(p)
    else:
        print("No products found.")

def find_product_by_name():
    name = input("Enter product name to search: ").strip()
    products = session.query(Product).filter(Product.name.ilike(f"%{name}%")).all()
    if products:
        print(f"\nSearch results for '{name}':")
        for p in products:
            print(p)
    else:
        print("No matching products found.")

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
        confirm = input(f"Are you sure you want to delete {product.name}? (y/n): ").lower()
        if confirm == 'y':
            try:
                session.delete(product)
                session.commit()
                print(f"Deleted product: {product}")
            except SQLAlchemyError as e:
                print(f"Error deleting product: {e}")
                session.rollback()
        else:
            print("Delete cancelled.")

def update_product():
    try:
        product_id = int(input("Enter product ID to update: "))
        product = session.query(Product).filter_by(id=product_id).first()
        if not product:
            print("Product not found.")
            return

        new_name = input(f"New name (current: {product.name}): ").strip() or product.name
        new_quantity = input(f"New quantity (current: {product.quantity}): ").strip()
        new_price = input(f"New price (current: {product.price}): ").strip()

        product.name = new_name
        product.quantity = int(new_quantity) if new_quantity else product.quantity
        product.price = float(new_price) if new_price else product.price

        session.commit()
        print(f"Updated product: {product}")
    except ValueError:
        print("Invalid input.")
    except SQLAlchemyError as e:
        print(f"Error updating product: {e}")
        session.rollback()

def menu():
    while True:
        print("\n--- Main Menu ---")
        print("1️⃣  Create Category")
        print("2️⃣  Create Product")
        print("3️⃣  View All Categories")
        print("4️⃣  View All Products")
        print("5️⃣  Find Product by Name")
        print("6️⃣  Delete Product")
        print("8️⃣  Update Product")
        print("7️⃣  Exit")
        choice = input("Enter your choice: ").strip()

        if choice == "1":
            create_category()
        elif choice == "2":
            create_product()
        elif choice == "3":
            view_all_categories()
        elif choice == "4":
            view_all_products()
        elif choice == "5":
            find_product_by_name()
        elif choice == "6":
            delete_product()
        elif choice == "8":
            update_product()
        elif choice == "7":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please choose a valid option.")

if __name__ == "__main__":
    menu()
