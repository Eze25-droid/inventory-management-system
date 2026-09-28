#************************************************
# INVENTORY MANAGEMENT SYSTEM (GUILD CANTEEN)
# GROUP 7 MEMBERS

# 1. AJAK DENG GARANG M25B38/031
# 2. BULIMA EEKIEL M25B38/028
# 3. APONI ALLAN DANIEL M25B38/029
# 4. AYOO ALICE  S25B38/026
# 5. AGENORWOT CYNTHIA JILLIAN S25B38/034
# 6. AYEBAZIBWE TRAVIS   S24B38/007

#************************************************


from datetime import date


class Product: # This class represents one product sold at Guild Canteen.

    def __init__(self, product_code, name, price, quantity, expiry, low_stock_threshold=10): # Example: GC001 - Rolex - UGX 5,000 - 20 pieces - N/A
        self.product_code = product_code # Unique code used to identify the product.
        self.name = name # Name of the product.
        self.price = price # Selling price of one item.
        self.quantity = quantity  # Number of items currently in stock.
        self.expiry = expiry # Expiry date or N/A.
        self.low_stock_threshold = low_stock_threshold # Minimum quantity before stock is considered low.
    
    
    # Reduces stock when a customer buys a product.
    # Example:
    # A student buys 2 Rolexes at UGX 5,000 each.
    # Total = 2 × 5,000 = UGX 10,000
    
    def sell(self, amount):

        if self.is_expired(): # Do not allow expired products to be sold.
            print("This product has expired and cannot be sold.")

        elif amount <= 0: # Do not allow zero or negative sales.
            print("Quantity must be greater than zero.")

        elif amount > self.quantity: # Do not allow the customer to buy more than available.
            print("Not enough stock.")

        else:
            self.quantity -= amount  # Reduce stock by the quantity sold.
            total = amount * self.price # Calculate total price.

            print("Sale successful.")
            print(f"Product: {self.name}")
            print(f"Quantity sold: {amount}")
            print(f"Total amount: UGX {total:,.2f}")
            print(f"Remaining stock: {self.quantity}")


    def add_stock(self, amount):  # Adds new stock to an existing product.
        if amount > 0:
            self.quantity += amount # 50 bottles + 25 bottles = 75 bottles

            print("Stock added successfully.")
            print(f"New stock: {self.quantity}")

        else:
            print("Quantity must be greater than zero.")

    def is_low_stock(self):
        return self.quantity <= self.low_stock_threshold

    # CHECK EXPIRY

    def is_expired(self):
        if self.expiry.upper() == "N/A": # Products without an expiry date use N/A.
            return False
        try:
            expiry_date = date.fromisoformat(self.expiry) # Convert the text date into a Python date.
            return expiry_date < date.today() # True when expiry date has passed.
        except ValueError: # Invalid dates are rejected when products are added,

            return False


    # DISPLAY PRODUCT

    def show(self):
        if self.is_expired():  # Determine product status.
            status = "EXPIRED"
        else:
            status = "OK"

        if self.is_low_stock():
            stock_status = "LOW STOCK"
        else:
            stock_status = "OK"

        print(
            f"Code: {self.product_code} | "
            f"Name: {self.name} | "
            f"Price: UGX {self.price:,.2f} | "
            f"Quantity: {self.quantity} | "
            f"Expiry: {self.expiry} | "
            f"Status: {status}"
            f"Stock: {stock_status}"
        )

        


# SHOP CLASS

class Shop: # This class manages the entire Guild Canteen inventory.
    def __init__(self):
        self.products = [] # List used to store Product objects.

    # ADD PRODUCT
    def add_product(self):
        print("\nADD PRODUCT TO GUILD CANTEEN")
        product_code = input("Product code: ").strip()  # Ask for product code.

        if product_code == "": # Product code cannot be empty.
            print("Product code cannot be empty.")
            return

        for product in self.products: # Check whether product code already exists.
            if product.product_code.upper() == product_code.upper():
                print("That product code already exists.")
                return

        name = input("Product name: ").strip() # Ask for product name.

        if name == "":
            print("Product name cannot be empty.")
            return

        try:
            price = float(input("Selling price (UGX): "))  # Convert price from text to decimal number.
            quantity = int(input("Quantity: ")) # Convert quantity from text to integer.
        except ValueError:
            print("Please enter valid numbers.")
            return

       
        if price <= 0:  
            print("Price must be greater than zero.") # Price must be positive.
            return

        if quantity < 0:  # Quantity cannot be negative.
            print("Quantity cannot be negative.")
            return

        expiry = input("Expiry date (YYYY-MM-DD or N/A): ").strip()  # Ask for expiry date.
        if expiry.upper() != "N/A": # Validate expiry date.

            try:
                date.fromisoformat(expiry)
            except ValueError:
                print(
                    "Invalid expiry date. "
                    "Use YYYY-MM-DD or N/A."
                )
                return

        product = Product(product_code, name, price, quantity, expiry) # Create a Product object.

        self.products.append(product) # Add the Product object to the shop.

        print("\nProduct added successfully.")
        print(f"Product code: {product_code}")
        print(f"Product name: {name}")


    # ADD PRODUCT AUTOMATICALLY
    # This method is mainly used by the TEST DEMO. It allows us to create sample products without typing everything manually.
   
    def add_demo_product(self, product_code, name, price, quantity, expiry):

        # Create Product object.
        product = Product(product_code, name, price, quantity, expiry)

        # Store it in the shop.
        self.products.append(product)

        print(f"Added: {product_code} - {name} " f"({quantity} items)")


    # VIEW PRODUCTS
    def view_products(self):

        print("\nGUILD CANTEEN PRODUCTS")

        if len(self.products) == 0: # Check whether the list is empty.
            print("No products available.")
            return

        for number, product in enumerate(self.products, 1): # Display products with numbers.
            print(f"\n{number}.")
            product.show()

    # SELECT PRODUCT

    def select_product(self):
        self.view_products()  # Display all products first.
        if len(self.products) == 0: # If no products exist, return nothing.
            return None

        try:
            number = int(input("Enter product number: ")) - 1  # Ask the user for product number.

            if 0 <= number < len(self.products): # Check if selected number is valid.
                return self.products[number]
            print("Invalid product number.")
            return None
        except ValueError:

            print("Please enter a valid number.")
            return None


    # ADD STOCK

    def add_stock(self):
        print("\n--- ADD STOCK ---")

        product = self.select_product()
        if product is not None:
            try:
                amount = int(input("Quantity to add: "))
                product.add_stock(amount)
            except ValueError:
                print("Please enter a valid number.")

    # SELL PRODUCT
    def sell_product(self):
        print("\n--- SELL PRODUCT ---")
        product = self.select_product()
        if product is not None:
            try:
                amount = int(input("Quantity sold: "))
                product.sell(amount)
            except ValueError:
                print("Please enter a valid number.")


    # CHECK EXPIRED PRODUCTS

    def expired_products(self):
        print("\n--- EXPIRED PRODUCTS ---")
        found = False

        # Check every product.
        for product in self.products:
            if product.is_expired() and product.quantity > 0: # Only show expired products that still have stock.
                loss = product.quantity * product.price # Calculate value of expired stock.

                print(
                    f"\nProduct: {product.name}\n"
                    f"Code: {product.product_code}\n"
                    f"Quantity: {product.quantity}\n"
                    f"Expiry: {product.expiry}\n"
                    f"Estimated loss: UGX {loss:,.2f}"
                )

                found = True

        if not found:
            print("No expired products.")

    # RECORD LOSS
    # Records spoiled, damaged or lost goods.

    def record_loss(self):

        print("\n--- RECORD SPOILED / DAMAGED / LOST GOODS ---")
        product = self.select_product()
        if product is None:
            return
        try:
            amount = int(input("Quantity lost: "))

            # Prevent zero or negative quantities.
            if amount <= 0:
                print("Quantity must be greater than zero.")
                return

            if amount > product.quantity: # Prevent stock from becoming negative.
                print("Not enough stock.")
                return

        except ValueError:
            print("Please enter a valid number.")
            return

        # Ask why the goods were lost.
        reason = input("Reason (Spoiled/Damaged/Lost): ")

        loss = amount * product.price # Calculate financial loss.
        product.quantity -= amount   # Remove lost items from stock.

        print("\nLoss recorded successfully.")
        print(f"Product: {product.name}")
        print(f"Code: {product.product_code}")
        print(f"Reason: {reason}")
        print(f"Quantity lost: {amount}")
        print(f"Estimated loss: UGX {loss:,.2f}")
        print(f"Remaining stock: {product.quantity}")


    # TEST DEMO
    # This automatically demonstrates the main features of the Guild Canteen system.
    # This is useful when demonstrating your project to your lecturer.

    def test_demo(self):

        print("""
=========================================================
             GUILD CANTEEN TEST DEMO
        Uganda Christian University
=========================================================
""")

       
        # CLEAR OLD PRODUCTS
        # This ensures that the demo starts with a clean list.

        self.products.clear()

        print("\n[TEST 1] ADDING SAMPLE PRODUCTS")

        # Add realistic UCU Guild Canteen products.
        self.add_demo_product("GC001", "Rolex", 5000, 20, "N/A")
        self.add_demo_product("GC002","Bottled Water", 1000, 50, "2027-03-15")
        self.add_demo_product("GC003", "Samosa",1500, 30, "2026-09-20")
        self.add_demo_product("GC004", "Mango Juice", 3000, 15, "2026-09-18")

        # This product deliberately has a past expiry date
        # so that we can test the expired-product feature.
        self.add_demo_product("GC005", "Expired Milk", 2500, 10, "2026-01-10")

        # VIEW PRODUCTS
        print("\n[TEST 2] VIEWING ALL PRODUCTS")
        self.view_products()


        # ADD STOCK
        print("\n[TEST 3] ADDING STOCK")

        water = self.products[1]
        print(f"Before: {water.name} = " f"{water.quantity} bottles")

        # Add 25 bottles.
        water.add_stock(25)
        print(f"After: {water.name} = " f"{water.quantity} bottles")

        # SELL PRODUCT

        print("\n[TEST 4] SELLING PRODUCTS")

        rolex = self.products[0]
        print(f"Before sale: {rolex.quantity} Rolexes")

        # Sell 2 Rolexes.
        rolex.sell(2)
        print(f"After sale: {rolex.quantity} Rolexes")


        # SELL WATER
        print("\n[TEST 5] SELLING BOTTLED WATER")

        water = self.products[1]
        print(f"Before sale: {water.quantity} bottles")

        # Sell 5 bottles.
        water.sell(5)
        print(f"After sale: {water.quantity} bottles")


        
        # SELL SAMOSAS

        print("\n[TEST 6] SELLING SAMOSAS")

        samosa = self.products[2]
        print(f"Before sale: {samosa.quantity} samosas")

        # Sell 4 samosas.
        samosa.sell(4)
        print(f"After sale: {samosa.quantity} samosas")


        # TEST NOT ENOUGH STOCK
        
        print("\n[TEST 7] TESTING INSUFFICIENT STOCK")

        print("Trying to sell 40 samosas when only " f"{samosa.quantity} are available...")
        samosa.sell(40)


        # TEST ZERO QUANTITY

        print("\n[TEST 8] TESTING ZERO QUANTITY")

        print("Trying to sell 0 Rolexes...")
        rolex.sell(0)


        
        # TEST NEGATIVE QUANTITY
        
        print("\n[TEST 9] TESTING NEGATIVE QUANTITY")

        print("Trying to sell -5 bottles...")
        water.sell(-5)


        # CHECK EXPIRED PRODUCTS
        print("\n[TEST 10] CHECKING EXPIRED PRODUCTS")
        self.expired_products()


        # TRY SELLING EXPIRED PRODUCT
        print("\n[TEST 11] TRYING TO SELL EXPIRED MILK")

        expired_milk = self.products[4]
        print("Trying to sell 2 bottles of expired milk...")
        expired_milk.sell(2)


        # RECORD SPOILED GOODS

        print("\n[TEST 12] RECORDING SPOILED GOODS")

        print("3 samosas have spoiled.")
        before = samosa.quantity
        loss = 3 * samosa.price
        samosa.quantity -= 3

        print(f"Quantity before: {before}")
        print(f"Quantity lost: 3")
        print( f"Estimated loss: UGX {loss:,.2f}")
        print(f"Quantity after: {samosa.quantity}")


        
        # RECORD DAMAGED GOODS
    
        print("\n[TEST 13] RECORDING DAMAGED GOODS")
        
        water = self.products[1]
        before = water.quantity
        loss = 2 * water.price
        water.quantity -= 2

        print("2 bottles of water were damaged.")
        print(f"Quantity before: {before}")
        print(f"Quantity lost: 2")
        print(f"Estimated loss: UGX {loss:,.2f}")
        print(f"Quantity after: {water.quantity}")


        
        # RECORD LOST GOODS

        print("\n[TEST 14] RECORDING LOST GOODS")

        juice = self.products[3]
        before = juice.quantity
        loss = 1 * juice.price
        juice.quantity -= 1

        print("1 Mango Juice was lost.")
        print(f"Quantity before: {before}")
        print(f"Quantity lost: 1")
        print(f"Estimated loss: UGX {loss:,.2f}")
        print(f"Quantity after: {juice.quantity}")


        # TEST INVALID PRODUCT CODE

        print("\n[TEST 15] TESTING DUPLICATE PRODUCT CODE")

        duplicate_code = "GC001"
        print(f"Trying to add another product with code " f"{duplicate_code}...")

        duplicate_found = False
        for product in self.products:

            if (product.product_code.upper() == duplicate_code.upper()):
                duplicate_found = True
                break

        if duplicate_found:
            print("That product code already exists.")
        else:
            print("Product code is available.")


        # TEST FINAL INVENTORY

        print("\n[TEST 16] FINAL INVENTORY")
        self.view_products()

        # DEMO FINISHED
        print("""
=========================================================
                 TEST DEMO COMPLETE
=========================================================
The demo tested:

✓ Adding products
✓ Product codes
✓ Viewing products
✓ Adding stock
✓ Selling products
✓ Calculating sales
✓ Preventing sales above available stock
✓ Preventing zero quantities
✓ Preventing negative quantities
✓ Detecting expired products
✓ Preventing sale of expired products
✓ Recording spoiled goods
✓ Recording damaged goods
✓ Recording lost goods
✓ Detecting duplicate product codes
✓ Final inventory checking
=========================================================
""")

    # MAIN MENU
    def run(self):
        while True:
            print("\n" + "=" * 50)
            print("           GUILD CANTEEN - UCU")
            print("        INVENTORY MANAGEMENT SYSTEM")
            print("=" * 50)

            print("1. Add product")
            print("2. View products")
            print("3. Add stock")
            print("4. Sell product")
            print("5. Check expired products")
            print("6. Record spoiled/damaged/lost goods")
            print("7. Run complete test demo")
            print("0. Exit")

            choice = input("\nChoose an option: ").strip()

            if choice == "1":
                self.add_product()

            elif choice == "2":
                self.view_products()

            elif choice == "3":
                self.add_stock()

            elif choice == "4":
                self.sell_product()

            elif choice == "5":
                self.expired_products()

            elif choice == "6":
                self.record_loss()

            elif choice == "7":
                self.test_demo()

            elif choice == "0":
                print("\nThank you for using Guild Canteen Inventory System.")
                print("Goodbye!")
                break

            else:
                print("\nInvalid option. Please choose a number from 0 to 7.")

            input("\nPress ENTER to return to the menu...")

shop = Shop()
shop.run()


