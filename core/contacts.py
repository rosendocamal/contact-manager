from .db import DatabaseManager
from .model import Contacts, Contact

class ManagerContact:
    def __init__(self, dbm_rute: str) -> None:
        self.dbm = DatabaseManager(dbm_rute)

    def add_contact(self, contact_name: str, contact_phone: int):
        self.dbm.insert_data((contact_name, contact_phone,))

    def search_contact(self, option: int = 1, search_name: str = str(), search_phone: int = int()) -> Contacts:
        match option:
            case 1:
                return self.dbm.query_data(option)
            case 2:
                return self.dbm.query_data(option, (search_name, search_phone,))
            case _:
                return Contacts()

    def edit_contact(self, edit_name: str, edit_phone: int):
        contact_list: Contacts = self.search_contact(2, edit_name, edit_phone)
        contact_id: int = contact_list.contacts[0].id
        self.dbm.update_data((edit_name, edit_phone, contact_id))

    def delete_contact(self, delete_name: str):
        contact_list: Contacts = self.search_contact(2, delete_name)
        contact_id = contact_list.contacts[0].id
        self.dbm.delete_data((contact_id,))