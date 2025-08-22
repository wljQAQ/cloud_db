from schemas.database_schema import DBConnect


class DatabaseService:
    def connect_test(self, connect_params: DBConnect):
        print(connect_params)


database_service = DatabaseService()
