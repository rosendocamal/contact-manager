from core.model import Contacts, Contact
from core.contacts import ManagerContact
from utils.input_validations import get_name, get_phone

class Forms:
    def __init__(self, contacts: ManagerContact) -> None:
        self.contacts: ManagerContact = contacts

    def display_add_contact(self):
        print('·' * 50)
        print('AÑADIR CONTACTO'.center(50))
        print('·' * 50)
        print('Ingrese los datos del nuevo contacto'.center(50))
        print('·' * 50, end='\n')

        prompt_name: str = '>>> Nombre: '
        prompt_phone: str = '>>> Teléfono: '
        error: str = '\t Dato inválido. Por favor, reintente de nuevo.'

        contact_name: str = get_name(prompt_name, error)
        contact_phone: int = get_phone(prompt_phone, error)

        print('·' * 50)
        try:
            self.contacts.add_contact(contact_name, contact_phone)
        except Exception:
            print('¡No se agregó el contacto!'.center(50))
        else:
            print('¡El contacto ha sido agregado!'.center(50))
        print('·' * 50)

    def display_show_contact(self):
        print('·' * 50)
        print('MOSTRAR TODOS LOS CONTACTOS'.center(50))
        print('·' * 50)
        print('Núm.'.center(8),'·', 'Nombre'.center(20),'·', 'Teléfono'.center(20))
        print('·' * 50, end='\n')

        contacts: Contacts = self.contacts.search_contact()

        if not contacts.contacts:
            for contact in contacts.contacts:
                print(f'{contact.id}·{contact.name}·{contact.phone}')

        print()
        print('·' * 50)

    def display_search_contact(self):
        print('·' * 50)
        print('BUSCAR CONTACTO'.center(50))
        print('·' * 50)
        print('Ingrese los datos del contacto'.center(50))
        print('·' * 50, end='\n')

        prompt_name: str = '>>> Nombre del Contacto: '
        prompt_phone: str = '>>> Teléfono del Contacto: '
        error: str = '\t Dato inválido. Por favor, reintente de nuevo.'

        contact_name: str = get_name(prompt_name, error)
        contact_phone: int = get_phone(prompt_phone, error)

        contacts: Contacts = self.contacts.search_contact(2, contact_name, contact_phone)

        print('·' * 50)
        print('Núm.'.center(8),'·', 'Nombre'.center(20),'·', 'Teléfono'.center(20))
        print('·' * 50, end='\n')

        if not contacts.contacts:
            for contact in contacts.contacts:
                print(f'{contact.id}·{contact.name}·{contact.phone}')

        print()
        print('·' * 50)

    def display_edit_contact(self):
        print('·' * 50)
        print('EDITAR CONTACTO'.center(50))
        print('·' * 50)
        print('Edición de los datos del contacto'.center(50))
        print('·' * 50, end='\n')

        prompt_name: str = '>>> Nombre del Contacto: '
        prompt_phone: str = '>>> Teléfono del Contacto: '
        error: str = '\t Dato inválido. Por favor, reintente de nuevo.'

        name: str = get_name(prompt_name, error)
        contact: Contacts = self.contacts.search_contact(2, name)
        
        if not contact.contacts:
            contact_name: str = get_name(prompt_name, error)
            contact_phone: int = get_phone(prompt_phone, error)
            print('·' * 50)
            try:
                self.contacts.edit_contact(contact_name, contact_phone)
            except Exception:
                print('¡No se modificó el contacto!'.center(50))
            else:
                print('¡El contacto ha sido modificado!'.center(50))
        else:
            print('¡No se existe el contacto!'.center(50))
            print('·' * 50)

    def display_delete_contact(self):
        print('·' * 50)
        print('ELIMINAR CONTACTO'.center(50))
        print('·' * 50)
        print('Ingrese los datos del contacto'.center(50))
        print('·' * 50, end='\n')

        prompt_name: str = '>>> Nombre del Contacto: '
        error: str = '\t Dato inválido. Por favor, reintente de nuevo.'

        contact_name: str = get_name(prompt_name, error)

        print('·' * 50)
        try:
            self.contacts.delete_contact(contact_name)
        except Exception:
            print('¡No se eliminó el contacto!'.center(50))
        else:
            print('¡El contacto ha sido eliminado!'.center(50))
        print('·' * 50)

    # import datos
    def display_import_contacts(self):
        pass
    # export datos
    def display_export_contacts(self):
        pass

    # salir
    def display_exit_menu(self) -> bool:
        print()
        print('·' * 50)
        print('CERRAR PROGRAMA'.center(50))
        print('·' * 50)
        print('Gracias por usarme'.center(50))
        print('·' * 50, end='\n')
        return True
