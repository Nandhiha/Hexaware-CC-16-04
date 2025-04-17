class Users:
    def __init__(self, userid: int, username: str, password: str, role: str):
        self.userid = userid
        self.username = username
        self.password = password
        self.role = role

    def __str__(self):
        return f"Users(userid={self.userid}, username={self.username}, role={self.role})"
