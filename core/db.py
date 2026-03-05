import sqlite3

class DatabaseManager:
    def __init__(self, db_path: str) -> None:
        self.db_path: str = db_path 
        self.table: str = 'contacts'

    def get_connection(self) -> sqlite3.Connection:
        connection: sqlite3.Connection = sqlite3.connect(self.db_path)
        connection.row_factory = sqlite3.Row
        return connection

    def basic_fn_structure(self, sql_statement: str, params: tuple[str | int, ...] = ()) -> None:
        try:
            with self.get_connection() as connection:
                connection.execute(sql_statement, params)
        except sqlite3.Error as error:
            print(error) # En proceso: en planeación el logging

    def initialize_database(self) -> None:
        create_table: str = f'''
            CREATE TABLE IF NOT EXISTS {self.table} (
                id      INTEGER PRIMARY KEY AUTOINCREMENT,
                name    TEXT NOT NULL,
                phone   INTEGER UNIQUE NOT NULL
            );
        '''
        self.basic_fn_structure(create_table)
        
    def query_data(self, option: int, param: tuple[str | int, ...] = ()) -> list[dict]:
        query_statements: dict[int, str] = {
            1: f'SELECT id, name, phone FROM {self.table} ORDER BY name ASC;',
            2: f'SELECT id, name, phone FROM {self.table} WHERE name = ? or phone = ? ORDER BY name ASC;',
        }
        try:
            with self.get_connection() as connection:
                cursor: sqlite3.Cursor = connection.cursor()
                cursor.execute(query_statements[option], param)
                return [dict(row) for row in cursor.fetchall()]
        except sqlite3.Error as error:
            print(error) # En proceso: en planeación el logging
            return [{}]

    def insert_data(self, params: tuple[str, int]) -> None:
        insert_statement: str = f'INSERT INTO {self.table} (name, phone) VALUES (?, ?)'
        self.basic_fn_structure(insert_statement, params)

    def update_data(self, params: tuple[str, int, int]) -> None:
        update_statement: str = f'UPDATE {self.table} SET name = ?, phone = ? WHERE id = ?'
        self.basic_fn_structure(update_statement, params)

    def delete_data(self, param: tuple[int]) -> None:
        delete_statement: str = f'DELETE FROM {self.table} WHERE id = ?'
        self.basic_fn_structure(delete_statement, param)