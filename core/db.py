import sqlite3, csv

class DatabaseManager:
    def __init__(self, db_path: str) -> None:
        self.db_path: str = db_path 
        self.table: str = 'contacts'

    def get_connection(self) -> sqlite3.Connection:
        db_conn: sqlite3.Connection = sqlite3.connect(self.db_path)
        return db_conn

    def initialize_database(self) -> None:
        try:
            with self.get_connection() as database:
                cursor = database.cursor()
                create_main_table: str = f'''
                    CREATE TABLE IF NOT EXISTS {self.table} (
                        id      INTEGER PRIMARY KEY AUTOINCREMENT,
                        name    TEXT,
                        surname TEXT,
                        phone   INT
                    );
                    '''
                cursor.execute(create_main_table)
        except sqlite3.OperationalError as error:
            pass
        else:
            database.commit()
    
    def query_data(self, option: int, param: tuple[str | int, ...] = ()) -> list | None:
        try:
            with self.get_connection() as database:
                cursor: sqlite3.Cursor = database.cursor()
                query_statement: str = ''
                match option:
                    case 1: # Ver todos los contactos
                        query_statement = f'''
                            SELECT name, surname, phone
                            FROM {self.table}
                            ORDER BY name ASC;
                        '''
                    case 2: # Buscar un contacto por su nombre
                        query_statement = f'''
                            SELECT name, surname, phone
                            FROM {self.table}
                            WHERE
                                name = ?
                            ORDER BY name ASC;
                        '''
                    case 3: # Buscar un contacto por su apellido
                        query_statement = f'''
                            SELECT name, surname, phone
                            FROM {self.table}
                            WHERE
                                surname = ?
                            ORDER BY name ASC;
                        '''
                    case 4: # Buscar un contacto por su número
                        query_statement = f'''
                            SELECT name, surname, phone
                            FROM {self.table}
                            WHERE phone = ?
                            ORDER BY name ASC;
                        '''

                cursor.execute(query_statement, param)
                rows: list = cursor.fetchall()
        except sqlite3.OperationalError as error:
            pass
        except sqlite3.DataError:
            pass
        else:
            return rows

    def insert_data(self, params: tuple[str, str, int]) -> None:
        try:
            with self.get_connection() as database:
                cursor: sqlite3.Cursor = database.cursor()
                insert_statement: str = f'INSERT INTO {self.table} (name, surname, phone) VALUES (?, ?, ?)'
                cursor.execute(insert_statement, params)
                # añadir database.rollback() en los errores
        except sqlite3.OperationalError as error:
            pass
        except sqlite3.IntegrityError as error:
            pass
        else:
            database.commit()

    def update_data(self, params: tuple[str, str, int, int]) -> None:
        try:
            with self.get_connection() as database:
                cursor: sqlite3.Cursor = database.cursor()
                update_statement: str = f'UPDATE {self.table} SET name = ?, surname = ?, phone = ? WHERE  id = ?'
                cursor.execute(update_statement, params)
                # añadir database.rollback() en los errores
        except sqlite3.OperationalError as error:
            pass
        except sqlite3.Error as error:
            pass
        else:
            database.commit()

    def delete_data(self, param: tuple[int]) -> None:
        try:
            with self.get_connection() as database:
                cursor: sqlite3.Cursor = database.cursor()
                delete_statement: str = f'DELETE FROM {self.table} WHERE id = ?'
                cursor.execute(delete_statement, param)
                # añadir database.rollback() en los errores
        except sqlite3.OperationalError as error:
            pass
        except sqlite3.Error as error:
            pass
        else:
            database.commit()

#    def import_data(self, csv_source_path: str) -> None:
#        # Hacer más macizo este código
#        # En proceso
#        try:
#            with self.get_connection() as database:
#                cursor: sqlite3.Cursor = database.cursor()
#                with open(csv_source_path) as restore:
#                    contents = csv.reader(restore)
#                    insert_statement: str = f'INSERT INTO {self.table} (name, surname, phone) VALUES (?, ?, ?)'
#                    cursor.executemany(insert_statement, contents)
#       # añadir database.rollback() en los errores
#        except FileNotFoundError as error:
#            print('Ocurrió un error inesperado.')
#        except csv.Error as error:
#           pass
#        except sqlite3.Error as error:
#           pass
#        else:
#            database.commit()
#
#    def export_data(self, csv_final_path: str) -> None:
#        # En proceso
#        try:
#            data = self.query_data(1)
#            with self.get_connection() as database:
#                cursor: sqlite3.Cursor = database.cursor()
#                headers: list[str] = [i[0] for i in cursor.description]
#                preserve = csv.writer(open(csv_final_path, 'w', newline=''),
#                                      delimiter=',', lineterminator='\r\n',
#                                      quoting=csv.QUOTE_ALL, escapechar='\\')
#                preserve.writerow(headers)
#                preserve.writerows(data)
#        except PermisionError as error:
#           pass
#       except OSError:
#           pass