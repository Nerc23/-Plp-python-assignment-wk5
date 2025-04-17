class Product:
    """
    A base class representing a generic product.
    """
    def __init__(self, name, price):
        """
        Constructor to initialize a Product object.

        Args:
            name (str): The name of the product.
            price (float): The price of the product.
        """
        self.name = name
        self.price = price

    def get_details(self):
        """
        Returns a string with the basic details of the product.
        """
        return f"Product: {self.name}, Price: ${self.price:.2f}"

    def apply_discount(self, discount_percentage):
        """
        Applies a discount to the product's price.

        Args:
            discount_percentage (float): The discount percentage (e.g., 0.1 for 10%).
        """
        if 0 <= discount_percentage <= 1:
            self.price *= (1 - discount_percentage)
            print(f"{self.name} price updated after {discount_percentage*100}% discount: ${self.price:.2f}")
        else:
            print("Invalid discount percentage.")

class Smartphone(Product):
    """
    A class representing a smartphone, inheriting from Product.
    """
    def __init__(self, name, price, brand, model, storage, camera_mp):
        """
        Constructor to initialize a Smartphone object.

        Args:
            name (str): The name of the smartphone.
            price (float): The price of the smartphone.
            brand (str): The brand of the smartphone.
            model (str): The model of the smartphone.
            storage (str): The storage capacity of the smartphone (e.g., "128GB").
            camera_mp (int): The megapixels of the main camera.
        """
        super().__init__(name, price)  # Call the constructor of the parent class
        self.brand = brand
        self.model = model
        self.storage = storage
        self.camera_mp = camera_mp
        self._is_on = False  # Encapsulated attribute (protected with a single underscore)

    def get_details(self):
        """
        Overrides the get_details method of the parent class to include smartphone-specific details.
        """
        return f"{super().get_details()}, Brand: {self.brand}, Model: {self.model}, Storage: {self.storage}, Camera: {self.camera_mp}MP"

    def power_on(self):
        """
        Turns the smartphone on.
        """
        if not self._is_on:
            self._is_on = True
            print(f"{self.brand} {self.model} is now ON.")
        else:
            print(f"{self.brand} {self.model} is already ON.")

    def power_off(self):
        """
        Turns the smartphone off.
        """
        if self._is_on:
            self._is_on = False
            print(f"{self.brand} {self.model} is now OFF.")
        else:
            print(f"{self.brand} {self.model} is already OFF.")

    def take_photo(self):
        """
        Simulates taking a photo.
        """
        if self._is_on:
            print(f"{self.brand} {self.model} clicked a {self.camera_mp}MP photo.")
        else:
            print(f"Cannot take a photo. {self.brand} {self.model} is OFF.")

class SamsungSmartphone(Smartphone):
    """
    A class representing a Samsung smartphone, inheriting from Smartphone.
    This demonstrates further specialization.
    """
    def __init__(self, name, price, model, storage, camera_mp, has_stylus=False):
        """
        Constructor for SamsungSmartphone, adding a specific feature.
        """
        super().__init__(name, price, "Samsung", model, storage, camera_mp)
        self.has_stylus = has_stylus

    def get_details(self):
        """
        Overrides the get_details method to include the stylus information.
        """
        stylus_info = "with S Pen" if self.has_stylus else "without S Pen"
        return f"{super().get_details()}, Features: {stylus_info}"

    def use_stylus(self):
        """
        Simulates using the stylus.
        """
        if self._is_on and self.has_stylus:
            print(f"Using the S Pen on the {self.model}.")
        elif not self.has_stylus:
            print(f"{self.model} does not have an S Pen.")
        else:
            print(f"Cannot use the stylus. {self.model} is OFF.")

# Creating instances of the classes
generic_product = Product("Generic Item", 50.00)
smartphone1 = Smartphone("AwesomePhone X", 799.99, "Generic", "X1", "128GB", 48)
samsung_s21 = SamsungSmartphone("Galaxy S21", 699.99, "S21", "256GB", 64)
samsung_note20 = SamsungSmartphone("Galaxy Note 20", 999.99, "Note 20", "256GB", 108, has_stylus=True)

# Demonstrating the methods and attributes
print(generic_product.get_details())
generic_product.apply_discount(0.1)
print("-" * 20)

print(smartphone1.get_details())
smartphone1.power_on()
smartphone1.take_photo()
smartphone1.power_off()
smartphone1.apply_discount(0.05)
print("-" * 20)

print(samsung_s21.get_details())
samsung_s21.power_on()
samsung_s21.take_photo()
samsung_s21.power_off()
print("-" * 20)

print(samsung_note20.get_details())
samsung_note20.power_on()
samsung_note20.use_stylus()
samsung_note20.power_off()
samsung_note20.apply_discount(0.15)

# Polymorphism example:
print("\n--- Polymorphism Example ---")
devices = [smartphone1, samsung_s21, samsung_note20]
for device in devices:
    print(f"Device Details: {device.get_details()}")
    if isinstance(device, Smartphone):
        device.power_on()
        device.power_off()
    print("-" * 10)

