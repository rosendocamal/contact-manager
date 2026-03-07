import csv
from .db import DatabaseManager
from .model import Contacts

class ManagerContact:
    def __init__(self, dbm_rute: str, dbm_logs: str) -> None:
        self.dbm = DatabaseManager(dbm_rute, dbm_logs)

    def add_contact(self, contact_name: str, contact_phone: int) -> bool:
        status: bool = self.dbm.insert_data((contact_name, contact_phone,))
        return status

    def search_contact(self, option: int = 1, search_name: str = str(), search_phone: int = int()) -> tuple[Contacts, bool]:
        match option:
            case 1:
                return self.dbm.query_data(option)
            case 2:
                return self.dbm.query_data(option, (search_name, search_phone,))
            case _:
                return (Contacts(), False,)

    def edit_contact(self, orig_name: str, edit_name: str, edit_phone: int) -> bool:
        result: tuple[Contacts, bool] = self.search_contact(2, orig_name)
        contact_list: Contacts = result[0]
        status: bool = result[1]
        if status:
            contact_id: int = contact_list.agency[0].id
            status = self.dbm.update_data((edit_name, edit_phone, contact_id))
            return status
        else:
            return status

    def delete_contact(self, delete_name: str) -> bool:
        result: tuple[Contacts, bool] = self.search_contact(2, delete_name)
        contact_list: Contacts = result[0]
        status: bool = result[1]
        if status:
            contact_id = contact_list.agency[0].id
            status: bool = self.dbm.delete_data((contact_id,))
            return status
        else:
            return status
        
    def csv_import_contacts(self, csv_import_path: str) -> bool:
        try:
            with open(csv_import_path, 'r') as csv_file:
                next(csv_file)
                for ln in csv_file:
                    try:
                        try:
                            ln = ln.split(',')
                        except:
                            ln = ln.split(';')
                        
                        status: bool = self.add_contact(ln[1], int(ln[2]))
                    except Exception as error:
                        with open(f'{self.dbm.logs}import.log', 'a') as log:
                            log.write(f'{error}\n')
                        continue
        except Exception as error:
            with open(f'{self.dbm.logs}import.log', 'a') as log:
                    log.write(f'{error}\n')
            return False
        else:
            return True
        
    def csv_export_contacts(self, csv_export_path: str) -> bool:
        result: tuple[Contacts, bool] = self.search_contact(1)
        contacts: Contacts = result[0]
        status: bool = result[1]

        if status:
            try:
                with open(csv_export_path, 'w', newline='') as csv_file:
                    writer = csv.writer(csv_file)
                    column_names: list[str] = [column for column in self.dbm.columns]
                    writer.writerow(column_names)
                    for c in contacts.agency:
                        writer.writerow([c.id, c.name, c.phone])
            except Exception as error:
                with open(f'{self.dbm.logs}export.log', 'a') as log:
                    log.write(f'{error}\n')
                return False
            else:
                return True
        else:
            return False