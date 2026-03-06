from .model import Contacts, Contact
import sqlite3

class DatabaseManager:
    def __init__(self, db_path: str) -> None:
        self.db_path: str = db_path 
        self.table: str = 'contacts'
        self.initialize_database()

    def get_connection(self) -> sqlite3.Connection:
        connection: sqlite3.Connection = sqlite3.connect(self.db_path)
        connection.row_factory = sqlite3.Row
        return connection

    def basic_fn_structure(self, sql_statement: str, params: tuple[str | int, ...] = ()) -> bool:
        try:
            with self.get_connection() as connection:
                connection.execute(sql_statement, params)
        except sqlite3.Error as error:
            print(error) # En proceso: en planeación el logging
            return False
        else:
            return True

    def initialize_database(self) -> None:
        create_table: str = f'''
            CREATE TABLE IF NOT EXISTS {self.table} (
                id      INTEGER PRIMARY KEY AUTOINCREMENT,
                name    TEXT UNIQUE NOT NULL,
                phone   INTEGER UNIQUE NOT NULL
            );
        '''
        self.basic_fn_structure(create_table)
        
    def query_data(self, option: int, param: tuple[str | int, ...] = ()) -> tuple[Contacts, bool]:
        query_statements: dict[int, str] = {
            1: f'SELECT id, name, phone FROM {self.table} ORDER BY name ASC;',
            2: f'SELECT id, name, phone FROM {self.table} WHERE name = ? or phone = ? ORDER BY name ASC;',
        }
        try:
            with self.get_connection() as connection:
                cursor: sqlite3.Cursor = connection.cursor()
                cursor.execute(query_statements[option], param)
                rows: list = cursor.fetchall()

                clean_data: Contacts = Contacts()
                for row in rows:
                    data: Contact = Contact(row['id'], row['name'], row['phone'])
                    clean_data.agency.append(data)
                return (clean_data, True,)
        except sqlite3.Error as error:
            print(error) # En proceso: en planeación el logging
            return (Contacts(), False,)

    def insert_data(self, params: tuple[str, int]) -> bool:
        insert_statement: str = f'INSERT INTO {self.table} (name, phone) VALUES (?, ?)'
        status: bool = self.basic_fn_structure(insert_statement, params)
        return status

    def update_data(self, params: tuple[str, int, int]) -> bool:
        update_statement: str = f'UPDATE {self.table} SET name = ?, phone = ? WHERE id = ?'
        status: bool = self.basic_fn_structure(update_statement, params)
        return status

    def delete_data(self, param: tuple[int]) -> bool:
        delete_statement: str = f'DELETE FROM {self.table} WHERE id = ?'
        status: bool = self.basic_fn_structure(delete_statement, param)
        return status
