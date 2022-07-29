from mongodb_connection import checks_mongodb
from schemas import Order, OrderWithCheckDb, GetManyChecksResponse


MENU_USD = {
    'pizza': 10.50,
    'burger': 5.00,
    'salad': 6.20,
    'coke': 2.00,
    'beer': 1.50
}


async def create_order(order: Order):
    order_dict = order.dict()
    total = 0
    for product, amount in order_dict['products'].items():
        total += MENU_USD[product] * amount
    tip = round(0.10 * total, 2)
    full_order_info = {**order_dict, **{"total": total, "tip": tip}}
    print(full_order_info)
    order_result = await checks_mongodb.insert_one_order(order=OrderWithCheckDb(**full_order_info).dict())
    return OrderWithCheckDb(**full_order_info)


async def get_checks_by_table_number(table_number: str, group_number: int):
    filtered_checks = await checks_mongodb.get_by_table_number(table_number, group_number)
    checks = []
    for check in filtered_checks['docs']:
        checks.append(OrderWithCheckDb(**check))
    invoices_result_dict = {
        'checks': checks,
        'count': filtered_checks['count'],
    }
    return GetManyChecksResponse(**invoices_result_dict)






