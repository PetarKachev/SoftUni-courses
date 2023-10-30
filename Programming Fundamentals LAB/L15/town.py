class Catalogue:
    products = []

    def __init__(self, name):
        self.name = name

    def add_product(self, product_name: str):
        Catalogue.products.append(product_name)

    def get_by_letter(self, first_letter: str):
        first_letter_products = [product for product in self.products if product[0] == first_letter]
        return first_letter_products

    def __repr__(self):
        given_catalogue = ""
        given_catalogue += f"Items in the {self.name} catalogue:\n"
        given_catalogue += '\n'.join(sorted(self.products))
        return given_catalogue