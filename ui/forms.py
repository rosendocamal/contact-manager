from core.contacts import ManagerContact
from utils.input_validations import get_name, get_phone

class Forms:
    def __init__(self, contacts: ManagerContact) -> None:
        self.contacts: ManagerContact = contacts

    def display_add_contact(self):
        print('·' * 50)
        print('AÑADIR CONTACTO'.center(50))
        print('·' * 50)
        print('Ingrese los datos del usuario'.center(50))
        print('·' * 50, end='\n')

        prompt_name: str = '>>> Nombre: '
        prompt_phone: str = '>>> Teléfono: '
        error: str = '\t Dato inválido. Por favor, reintente de nuevo.'

        contact_name: str = get_name(prompt_name, error)
        contact_phone: int = get_phone(prompt_phone, error)

        print('·' * 50)
        try:
            self.contacts.add_contact(contact_name, contact_phone)
        except:
            print('¡No se agregó el contacto!'.center(50))
        else:
            print('¡El contacto ha sido agregado!'.center(50))
        print('·' * 50)

    def display_show_contact(self):
        print('·' * 50)
        print('MOSTRAR TODOS LOS CONTACTOS'.center(50))
        print('·' * 50)
        print('Núm.'.center(8),'·', 'Nombre'.center(20),'·', 'Teléfono'.center(20))
        print('·' * 50, end='\n\n')

        contacts: list[dict] = self.contacts.search_contact()

        for contact in contacts:
            print(f'{contact['id']:7d}·{contact['name']:18}·{contact['phone']:18}')

        print()
        print('·' * 50)

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