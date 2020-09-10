# Zaki Ahmed
# 04 Apr 2020
# Assignment 2

# CS 162 : Sp 2020
# Description: A store that runs with products, customers, and store checkouts


class InvalidCheckoutError(Exception):
    pass

# BEGIN 3 CLASSES...
class Product:
    """
    Summary: Creates a product has 5 parameter values, 0 additional data members
    Parameters: Product ID, Title, Description, Price, Quantity Available
    Returns: Get methods for all above mentioned + Decrease Quantity
    """
    def __init__(self, product_id, title, description, price, quantity_available):
        self._product_id = product_id
        self._title = title
        self._description = description
        self._price = price
        self._quantity_available = quantity_available

    def get_product_id(self):
        return self._product_id

    def get_title(self):
        return self._title

    def get_description(self):
        return self._description

    def get_price(self):
        return self._price

    def get_quantity_available(self):
        return self._quantity_available

    def decrease_quantity(self):
        """Decreases item quantity by 1"""
        self._quantity_available -= 1
        return self._quantity_available


class Customer:
    """
    Summary: Creates a customer has 3 parameter values, 2 additional data members
    Parameters: Name, Customer ID, Premium Member Status (as a boolean)
    Returns: Get methods for all above mentioned + Add Product to Cart, Empty Cart + Get Cart (for testing)
    """
    def __init__(self, name, customer_id, premium_member):
        self._name = name
        self._customer_id = customer_id
        self._premium_member = premium_member
        self._cart = []
        self._checkout_cart = []

    def get_name(self):
        return self._name

    def get_customer_id(self):
        return self._customer_id

    def is_premium_member(self):
        if self._premium_member is True:
            return True
        if self._premium_member is False:
            return False

    def add_product_to_cart(self, product_id):
        """Takes in product ID code and adds that to the customer's cart"""
        self._cart.append(product_id.get_product_id())
        self._checkout_cart.append(product_id)
        return self._cart

    def empty_cart(self):
        """Completely empties out the customer's cart"""
        del self._cart[::1]
        del self._checkout_cart[::1]
        return self._cart

    # FOR TESTING PURPOSES
    def get_cart(self):
        return self._cart

    # FOR TESTING PURPOSES
    def get_checkout_cart(self):
        return self._checkout_cart


class Store:
    """
    Summary: Creates a store has 0 parameter values, 2 additional data members
    Parameters:
    Returns: Add Product to Cart, Empty Cart + Get Cart
    """
    def __init__(self):
        self._inventory = []
        self._membership = []

    # FOR TESTING PURPOSES
    def get_inventory(self):
        return self._inventory

    # FOR TESTING PURPOSES
    def get_membership(self):
        return self._membership

    def add_product(self, product):
        """Adds product to store inventory listing"""
        return self._inventory.append(product)

    def add_member(self, member):
        """Adds customer to store membership listing"""
        return self._membership.append(member)

    def get_product_from_id(self, product_id):
        """Retrieve a product using a Product ID"""
        for product in self._inventory:
            if str(product_id) == str(product.get_product_id()):
                return product
        else:
            return None

    def get_member_from_id(self, customer_id):
        """Retrieve a member using a Customer ID"""
        for member in self._membership:
            if str(customer_id) == str(member.get_customer_id()):
                return member
        else:
            return None

    def product_search(self, search):
        """Search for a product by entering a descriptive term or title"""

        # Initialize empty lists
        product_results = []
        product_results2 = []
        search = str(search)

        # Run a search across all product titles in store inventory
        for product in self._inventory:
            if search.lower() in product.get_title().lower():
                product_results.append(product.get_product_id())

        # Run a search across all product descriptions in store inventory
        for product in self._inventory:
            if search.lower() in product.get_description().lower():
                product_results2.append(product.get_product_id())

        # Combine search results
        combined_results = product_results + product_results2
        combined_results.sort()

        # Remove any duplicates in search results
        for product in self._inventory:
            if search.lower() in product.get_title().lower() and search.lower() in product.get_description().lower():
                combined_results.remove(product.get_product_id())

        combined_results.sort()
        return combined_results

    def add_product_to_member_cart(self, product_id, customer_id):
        """Adds a product to a members cart if both items exist in store directory"""

        # Check for match on inventory, then membership, if so - add to cart
        for product in self._inventory:
            if str(product_id) in str(product.get_product_id()):

                for member in self._membership:
                    if str(customer_id) in str(member.get_customer_id()):

                        if product.get_quantity_available() > 0:
                            member.add_product_to_cart(product)
                            return "product added to cart"
                        else:
                            return "product out of stock"
                return "member ID not found"
        return "product ID not found"


    def check_out_member(self, customer_id):
        """
        Ring up a customer to give them a total price
        Premium Members: free shipping
        Regular Members: pay 7% of cart total
        """
        # Initialize a zero sum total
        total = 0
        blank = 0

        # Check member listing for match and calculate values
        for member in self._membership:
            if str(customer_id) in str(member.get_customer_id()):
                final_cart = member.get_checkout_cart()

                # If cart empty, return $0 total.
                if final_cart == []:
                    return total

                # Otherwise, calculate total
                else:
                    # Initialize empty cart
                    purchase_cart = []
                    for item in final_cart:

                        # If item is in inventory, add to purchase list and decrease respective quantity
                        if item in self._inventory:
                            if item.get_quantity_available() > 0:
                                purchase_cart.append(item)
                                item.decrease_quantity()

                        # If item is in inventory, but out of stock, DO NOT add to purchase list
                            elif item.get_quantity_available() <= 0:
                                blank = blank

                        # If item is in not inventory, add to purchase list and decrease respective quantity
                        if item not in self._inventory:
                            blank = blank

                    # Total calculation of all items eligible for purchase (premium vs regular)
                    for product in purchase_cart:
                        total = total + product.get_price()
                    if member.is_premium_member() is False:
                        total = total * 1.07
                        member.empty_cart()
                        return total
                    elif member.is_premium_member() is True:
                        total = total
                        member.empty_cart()
                        return total
        else:
            raise InvalidCheckoutError
            # return print("Sorry, this member was not found.")

# BEGIN EXCEPTION CLASS...
# class InvalidCheckoutError(Exception):
#     pass


# BEGIN MAIN FUNCTION
def main():
    try:
        myStore = Store()
        p1 = Product("889", "Rodent of unusual size", "when a rodent of the usual size just won't do", 33.45, 8)
        c1 = Customer("Yinsheng", "QWF", False)

        p2 = Product("123", "Apple", "Gala apples from California", 1.00, 1)
        p3 = Product("456", "Milk", " milk fresh from the farm", 4.00, 0)
        p4 = Product("789", "Bananapples", "Ripe banana APPLE from Honduras", 0.50, 50)
        p5 = Product("999", "Clorox Apple Scented Wipes", "Sanitizing wipes", 7.00, 25)
        p6 = Product("666", "Hahaha", "I don't even exist", 100.00, 25)
        c2 = Customer("Jessica", "SGJ", True)
        c3 = Customer("Marcus", "AMG", True)
        c4 = Customer("Fakey", "FAK", True)

        myStore.add_product(p1)
        myStore.add_member(c1)

        myStore.add_product(p1)
        myStore.add_product(p1)
        myStore.add_product(p1)
        myStore.add_product(p2)
        myStore.add_product(p3)
        myStore.add_product(p4)
        myStore.add_product(p5)

        myStore.add_member(c2)
        myStore.add_member(c3)

        myStore.add_product_to_member_cart("889", "QWF")
        result = myStore.check_out_member("FAK")
        myStore.check_out_member(c1.get_customer_id())
    except InvalidCheckoutError:
        print("Sorry, this member was not found.")
    # return myStore

if __name__ == '__main__':
    main()

