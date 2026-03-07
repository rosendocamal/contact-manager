from .forms import Forms
from core.contacts import ManagerContact
from utils.input_validations import get_option
class Menu:
    def __init__(self, dbm_rute: str, dbm_logs: str) -> None:
        self.contacts: ManagerContact = ManagerContact(dbm_rute, dbm_logs)
        self.forms = Forms(self.contacts)

    def run(self):
        prompt: str = '>>> Seleccione una opción: '
        error: str = '>>>>>> Opción inválida. Reintente de nuevo.'
        try:
            while True:
                self.display_menu()
                option: int = get_option(prompt, error)
                print('·' * 50)

                match option:
                    case 1:
                        self.forms.display_add_contact()
                    case 2:
                        self.forms.display_show_contact()
                    case 3:
                        self.forms.display_search_contact()
                    case 4:
                        self.forms.display_edit_contact()
                    case 5:
                        self.forms.display_delete_contact()
                    case 6:
                        self.forms.display_import_contacts()
                    case 7:
                        self.forms.display_export_contacts()
                    case 8:
                        if self.forms.display_exit_menu():
                            break

                input('>>> Presione una ENTER para continuar. ')
                        
        except KeyboardInterrupt:
            self.forms.display_exit_menu()

    def display_menu(self):
        print('·' * 50)
        print('MENÚ'.center(50))
        print('·' * 50)
        print('¡Bienvenido!'.center(50))
        print('·' * 50, end='\n')
        print()
        print('>>> [1] Añadir un contacto')
        print('>>> [2] Listar contactos')
        print('>>> [3] Buscar un contacto')
        print('>>> [4] Editar un contacto')
        print('>>> [5] Borrar un contacto')
        print('>>> [6] Importar')
        print('>>> [7] Exportar')
        print('>>> [8] Cerrar programa')
        print()
        print('·' * 50)
        print('·' * 50)