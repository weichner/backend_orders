import os
from motor.motor_asyncio import AsyncIOMotorClient


class DatabaseMongoDB:
    def __init__(self, conn_str: str, database: str, collection: str):
        """Init method for DatabaseMongoDB"""
        self.__client = AsyncIOMotorClient(conn_str)
        self.__db = self.__client[database]
        self.collection = self.__db[collection]

    async def get_by_table_number(self, table_number: str, group_number: int):
        cursor = self.collection.find({'table_number': table_number, 'group_number': group_number})
        results = [doc async for doc in cursor]
        results_count = await self.collection.count_documents({'table_number': table_number, 'group_number': group_number})
        return {
            'docs': results,
            'count': results_count
        }

    async def insert_one_order(self, order: dict):
        result = await self.collection.insert_one(order)
        return result


checks_mongodb = DatabaseMongoDB(conn_str=f"mongodb+srv://user:{os.getenv('database_password')}@cluster0.smw1pff.mongodb.net/?retryWrites=true&w=majority",
                                   database="FairPayDB",
                                   collection='checks')
