from .forms import Forms
from core.contacts import ManagerContact
class Menu:
    def __init__(self, dbm_rute: str) -> None:
        self.contacts: ManagerContact = ManagerContact(dbm_rute)
        self.forms = Forms(self.contacts)