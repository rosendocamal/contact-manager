from ui.menu import Menu

DB_NAME: str = 'contacts.db'
DB_PATH: str = f'db/{DB_NAME}'

try:
    agency = Menu(DB_PATH)
    agency.run()
except Exception as error:
    print(f'Ocurrió un error inesperado: {error}'.center(50))