# exception/custom_exception.py

class UserNotFoundException(Exception):
    def __init__(self, message):
        super().__init__(message)
        self.message = message

    def __str__(self):
        return f"UserNotFoundException: {self.message}"

class OrderNotFoundException(Exception):
    def __init__(self, message):
        super().__init__(message)
        self.message = message

    def __str__(self):
        return f"OrderNotFoundException: {self.message}"

class ProductNotFoundException(Exception):
    def __init__(self, message):
        super().__init__(message)
        self.message = message

    def __str__(self):
        return f"ProductNotFoundException: {self.message}"
