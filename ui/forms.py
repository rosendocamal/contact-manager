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
        status: bool = self.contacts.add_contact(contact_name, contact_phone)
        if status:
            print('¡El contacto ha sido agregado!'.center(50))
        else:
            print('¡No se agregó el contacto!'.center(50))
        print('·' * 50)

    def display_show_contact(self):
        print('·' * 50)
        print('MOSTRAR TODOS LOS CONTACTOS'.center(50))
        print('·' * 50)
        print('Núm.'.center(8),'·', 'Nombre'.center(20),'·', 'Teléfono'.center(20))
        print('·' * 50, end='\n')

        result: tuple[Contacts, bool] = self.contacts.search_contact()

        contacts: Contacts = result[0]
        status: bool = result[1]

        if status:
            if contacts.agency:
                for contact in contacts.agency:
                    print(f'{contact.id}'.center(8),'·', f'{contact.name}'.center(20), '·', f'{contact.phone}'.center(20))
        else:
            print('Ocurrió un error inesperado'.center(50))
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

        result: tuple[Contacts, bool] = self.contacts.search_contact(2, contact_name)

        contacts: Contacts = result[0]
        status: bool = result[1]

        if status: 
            print('·' * 50)
            print('Núm.'.center(8),'·', 'Nombre'.center(20),'·', 'Teléfono'.center(20))
            print('·' * 50, end='\n')

            if contacts.agency:
                for contact in contacts.agency:
                    print(f'{contact.id}'.center(8),'·', f'{contact.name}'.center(20), '·', f'{contact.phone}'.center(20))
        else:
            print('Ocurrió un error inesperado'.center(50))
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
        result: tuple[Contacts, bool] = self.contacts.search_contact(2, name)

        contact: Contacts = result[0]
        status: bool = result[1]
        
        if status:
            if contact.agency:
                contact_name: str = get_name(prompt_name, error)
                contact_phone: int = get_phone(prompt_phone, error)
                print('·' * 50)

                status: bool = self.contacts.edit_contact(name, contact_name, contact_phone)

                if status:
                    print('¡El contacto ha sido modificado!'.center(50))
                else:
                    print('¡No se modificó el contacto!'.center(50))
            else:
                print('·' * 50)
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

        status: bool = self.contacts.delete_contact(contact_name)
        if status:
            print('¡El contacto ha sido eliminado!'.center(50))
        else:
            print('¡No se eliminó el contacto!'.center(50))
        print('·' * 50)

    # import datos
    def display_import_contacts(self):
        print('·' * 50)
        print('IMPORTAR CONTACTOS'.center(50))
        print('·' * 50, end='\n')

        prompt_name: str = '>>> Ruta del archivo de importación: '
        error: str = '\t Dato inválido. Por favor, reintente de nuevo.'

        csv_path: str = get_name(prompt_name, error)

        print('·' * 50)

        status: bool = self.contacts.csv_import_contacts(csv_path)
        if status:
            print('¡Los contactos han sido importados!'.center(50))
        else:
            print('¡Los contactos no fueron importados!'.center(50))
            print('FORMATO CSV: id,name,phone')
        print('·' * 50)
    
    def display_export_contacts(self):
        print('·' * 50)
        print('EXPORTAR CONTACTOS'.center(50))
        print('·' * 50, end='\n')

        prompt_name: str = '>>> Ruta del archivo de exportación: '
        error: str = '\t Dato inválido. Por favor, reintente de nuevo.'

        csv_path: str = get_name(prompt_name, error)

        print('·' * 50)

        status: bool = self.contacts.csv_export_contacts(csv_path)
        if status:
            print('¡Los contactos han sido exportados!'.center(50))
        else:
            print('¡Los contactos no fueron exportados!'.center(50))
        print('·' * 50)

    def display_exit_menu(self) -> bool:
        print()
        print('·' * 50)
        print('CERRAR PROGRAMA'.center(50))
        print('·' * 50)
        print('Gracias por usarme'.center(50))
        print('·' * 50, end='\n')
        return True