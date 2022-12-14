from fastapi import HTTPException


class OrderInsertionError(HTTPException):
    def __init__(self, status_code, detail):
        self.status_code = status_code
        self.detail = detail
        super().__init__(self.status_code, self.detail)