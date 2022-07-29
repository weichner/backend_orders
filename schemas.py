from pydantic import BaseModel
from enum import Enum


class TablesNumbersEnum(str, Enum):
    table_1 = '1'
    table_2 = '2'
    table_3 = '3'
    table_4 = '4'
    table_5 = '5'


class Order(BaseModel):
    table_number: TablesNumbersEnum
    group_number: int
    client_name: str
    products: dict


class OrderWithCheckDb(Order):
    tip: float
    total: float


class GetManyChecksResponse(BaseModel):
    checks: list[OrderWithCheckDb]
    count: int


