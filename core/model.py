class Contact:
    def __init__(self, id: int, name: str, phone: int) -> None:
        self.id: int = id
        self.name: str = name
        self.phone: int = phone

class Contacts:
    def __init__(self):
        self.agency: list = []

    def add_contacts(self, contact: Contact):
        self.agency.append(contact)