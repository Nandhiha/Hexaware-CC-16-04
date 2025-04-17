class Order:
    def __init__(self, orderid: int, userid: int):
        self.orderid = orderid
        self.userid = userid

    def __str__(self):
        return f"Order(orderid={self.orderid}, userid={self.userid})"
