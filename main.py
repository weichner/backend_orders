from fastapi import FastAPI, status
from fastapi.responses import JSONResponse
import mongodb_operations as mongodb
from schemas import Order, TablesNumbersEnum, GetManyChecksResponse
from exceptions import OrderInsertionError

app = FastAPI()


@app.post("/order/", status_code=status.HTTP_201_CREATED)
async def handle_form_mongo(order_info: Order):
    try:
        order_data = await mongodb.create_order(order_info)

    except OrderInsertionError as e:
        return JSONResponse(status_code=e.status_code, content=e.detail)

    return order_data


@app.get('/check/', response_model=GetManyChecksResponse)
async def get_by_table_and_group(table_number: TablesNumbersEnum, group_number: int):
    checks = await mongodb.get_checks_by_table_number(table_number, group_number)
    return checks

