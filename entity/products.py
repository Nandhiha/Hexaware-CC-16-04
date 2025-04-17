class Products:
    def __init__(
        self,
        productid: int,
        productname: str,
        description: str,
        price: float,
        quantityinstock: int,
        type: str
    ):
        self.productid = productid
        self.productname = productname
        self.description = description
        self.price = price
        self.quantityinstock = quantityinstock
        self.type = type  # e.g. 'Electronics' or 'Clothing'

    def __str__(self):
        return (f"Products(productid={self.productid}, name={self.productname}, "
                f"price={self.price}, in_stock={self.quantityinstock}, type={self.type})")
