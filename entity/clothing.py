from entity.products import Products

class Clothing(Products):
    def __init__(
        self,
        productid: int,
        productname: str,
        description: str,
        price: float,
        quantityinstock: int,
        type: str,
        size: str,
        color: str
    ):
        super().__init__(productid, productname, description, price, quantityinstock, type)
        self.size = size
        self.color = color

    def __str__(self):
        base = super().__str__().rstrip(")")
        return f"{base}, size={self.size}, color={self.color})"
