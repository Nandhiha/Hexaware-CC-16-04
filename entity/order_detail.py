class OrderDetails:
    def __init__(self, orderdetailid: int, orderid: int, productid: int, quantity: int):
        self.orderdetailid = orderdetailid
        self.orderid = orderid
        self.productid = productid
        self.quantity = quantity

    def __str__(self):
        return (f"OrderDetails(id={self.orderdetailid}, orderid={self.orderid}, "
                f"productid={self.productid}, quantity={self.quantity})")
