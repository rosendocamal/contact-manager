import sqlite3

class DatabaseManager:
    def __init__(self, db_path: str, table_name: str) -> None:
        self.db_path: str = db_path 
        self.table: str = table_name

    def get_connection(self) -> sqlite3.Connection:
        db_conn: sqlite3.Connection = sqlite3.connect(self.db_path)
        return db_conn

    def initialize_database(self) -> None:
        try:
            with self.get_connection() as database:
                create_main_table: str = f'''
                    CREATE TABLE IF NOT EXISTS {self.table} (
                        id      INTEGER PRIMARY KEY AUTOINCREMENT,
                        name    TEXT,
                        surname TEXT,
                        phone   INT
                    );
                    '''
                database.cursor().execute(create_main_table)
        except (sqlite3.OperationalError, ModuleNotFoundError) as error:
            print("Ocurrió un error inesperado.")
        else:
            database.commit()
    
    def query_data(self, option: int):
        match option:
            case 1: # ver todos los contactos
                pass
            case 2: # ver un contacto
                pass
            case _: # no sé
                pass
        try:
            with self.get_connection() as database:
                database.cursor().execute('', ())
        except (sqlite3.OperationalError, ModuleNotFoundError) as error:
            print("Ocurrió un error inesperado.")
        else:
            database.commit()
    """
        try:
            with self.get_connection() as database:

                database.cursor().execute(query, params)
        except (sqlite3.OperationalError, ModuleNotFoundError) as error:
            print("Ocurrió un error inesperado.")
        else:
            database.commit()
    """

    def insert_data(self, params: tuple[str, str, int]) -> None:
        try:
            with self.get_connection() as database:
                insert_statement: str = f'INSERT INTO {self.table} (name, surname, phone) VALUES (?, ?, ?)'
                database.cursor().execute(insert_statement, params)
        except (sqlite3.OperationalError, ModuleNotFoundError, ValueError, IndexError) as error:
            print("Ocurrió un error inesperado.")
        else:
            database.commit()

    def update_data(self, params: tuple[str, str, int, int]) -> None:
        try:
            with self.get_connection() as database:
                update_statement: str = f'UPDATE {self.table} SET name = ?, surname = ?, phone = ? WHERE id = ?'
                database.cursor().execute(update_statement, params)
        except (sqlite3.OperationalError, ModuleNotFoundError, ValueError, IndexError) as error:
            print("Ocurrió un error inesperado.")
        else:
            database.commit()

    def delete_data(self, param: tuple[int]) -> None:
        try:
            with self.get_connection() as database:
                delete_statement: str = f'DELETE FROM {self.table} WHERE id = ?'
                database.cursor().execute(delete_statement, param)
        except (sqlite3.OperationalError, ModuleNotFoundError) as error:
            print("Ocurrió un error inesperado.")
        else:
            database.commit()


    def import_data(self):
        pass

    def export_data(self):
        pass
