from entity.products import Products

class Electronics(Products):
    def __init__(
        self,
        productid: int,
        productname: str,
        description: str,
        price: float,
        quantityinstock: int,
        type: str,
        brand: str,
        warrantyperiod: int
    ):
        super().__init__(productid, productname, description, price, quantityinstock, type)
        self.brand = brand
        self.warrantyperiod = warrantyperiod

    def __str__(self):
        base = super().__str__().rstrip(")")
        return f"{base}, brand={self.brand}, warranty={self.warrantyperiod}yrs)"
