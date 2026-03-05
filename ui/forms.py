from core.contacts import ManagerContact
import utils.input_validations
class Forms:
    def __init__(self, contacts: ManagerContact) -> None:
        self.contacts: ManagerContact = contacts

    def display_add_contact(self):
        print('·' * 50)
        print('AÑADIR CONTACTO'.center(50))
        print('·' * 50)
        print('Ingrese los datos del usuario'.center(50))
        print('·' * 50, end='\n')
        print()

        print('>>> Nombre: ')
        contact_name: str = str()

        print()

        print('>>> Teléfono: ')
        contact_phone: int = int()

        self.contacts.add_contact(contact_name, contact_phone)

        print('·' * 50)
        print('¡El contacto ha sido agregado!')
        print('·' * 50)

    def display_show_contact(self):
        pass
    # buscar contacto
    def display_search_contact(self):
        pass
    # editar contactos
    def display_edit_contact(self):
        pass
    # eliminar contactos
    def display_delete_contact(self):
        pass
    # import datos
    def display_import_contacts(self):
        pass
    # export datos
    def display_export_contacts(self):
        pass
    # salir
    def display_exit_menu(self):
        pass