from util.db_conn_util import get_connection
from dao.order_processor import ConcreteOrderProcessor
from entity.users import Users
from entity.electronics import Electronics
from entity.clothing import Clothing
from entity.order import Order
from entity.order_detail import OrderDetails
from entity.products import Products

def view_table_data(table_name: str):
    """
    Fetches and prints all rows from the given table.
    """
    conn = None
    cursor = None
    try:
        conn = get_connection()
        cursor = conn.cursor()

        query = f"SELECT * FROM {table_name}"
        cursor.execute(query)

        # Print column headers
        columns = [col[0] for col in cursor.description]
        print(" | ".join(columns))
        print("-" * len(" | ".join(columns)))

        # Print each row
        for row in cursor.fetchall():
            print(" | ".join(str(cell) for cell in row))

    except Exception as e:
        print(f"Error: {e}")
    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()


def main():
    processor = ConcreteOrderProcessor()

    while True:
        print("\nMenu:")
        print("1. Create User")
        print("2. Create Product")
        print("3. Create Order")
        print("4. Cancel Order")
        print("5. Get All Products")
        print("6. Get Order by User")
        print("7. View Table Data")
        print("8. Exit")

        choice = input("Enter choice: ")

        if choice == '1':
            try:
                user_id = int(input("Enter User ID: "))
                username = input("Enter Username: ")
                password = input("Enter Password: ")
                role = input("Enter Role (Admin/User): ")
                user = Users(user_id, username, password, role)
                processor.create_user(user)
                print("✅ User created successfully.")

            except Exception as e:
                print(f"Error: {e}")

        elif choice == '2':
            try:
                admin_id = int(input("Enter Admin User ID: "))
                username = input("Enter Admin Username: ")
                password = input("Enter Admin Password: ")
                role = "Admin"
                admin_user = Users(admin_id, username, password, role)

                product_id = int(input("Enter Product ID: "))
                name = input("Enter Product Name: ")
                desc = input("Enter Description: ")
                price = float(input("Enter Price: "))
                stock = int(input("Enter Quantity In Stock: "))
                type_ = input("Enter Type (Electronics/Clothing): ")

                if type_.lower() == 'electronics':
                    brand = input("Enter Brand: ")
                    warranty = int(input("Enter Warranty Period (months): "))
                    product = Electronics(product_id, name, desc, price, stock, brand, warranty)
                elif type_.lower() == 'clothing':
                    size = input("Enter Size: ")
                    color = input("Enter Color: ")
                    product = Clothing(product_id, name, desc, price, stock, size, color)
                else:
                    print("Invalid product type.")
                    continue

                processor.create_product(admin_user, product)
                print("✅ Product created successfully.")

            except Exception as e:
                print(f"Error: {e}")

        elif choice == '3':
            try:
                user_id = int(input("Enter User ID: "))
                username = input("Enter Username: ")
                password = input("Enter Password: ")
                role = "User"
                user = Users(user_id, username, password, role)

                num_items = int(input("How many products to order? "))
                products = []

                for i in range(num_items):
                    product_id = int(input(f"Enter Product ID #{i+1}: "))
                    # Dummy product with just ID
                    product = Products(product_id, "", "", 0.0, 0)
                    products.append(product)

                order_id = int(input("Enter Order ID: "))
                order = Order(order_id, user, products)
                processor.create_order(order)
                print("✅ Order created successfully.")

            except Exception as e:
                print(f"Error: {e}")

        elif choice == '4':
            try:
                user_id = int(input("Enter User ID: "))
                order_id = int(input("Enter Order ID: "))
                processor.cancel_order(user_id, order_id)
                print("✅ Order cancelled successfully.")

            except Exception as e:
                print(f"Error: {e}")

        elif choice == '5':
            try:
                products = processor.get_all_products()
                for row in products:
                    print(row)
                print("✅ Successfully fetched all products.")

            except Exception as e:
                print(f"Error: {e}")

        elif choice == '6':
            try:
                user_id = int(input("Enter User ID: "))
                username = input("Enter Username: ")
                password = input("Enter Password: ")
                role = "User"
                user = Users(user_id, username, password, role)

                orders = processor.get_orders_by_user(user)
                for order in orders:
                    print(order)
                print("✅ Successfully fetched orders by user.")

            except Exception as e:
                print(f"Error: {e}")

        elif choice == '7':
            try:
                table_to_view = input("Enter table name to view: ")
                view_table_data(table_to_view)

            except Exception as e:
                print(f"Error: {e}")

        elif choice == '8':
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
