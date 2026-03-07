```
classDiagram
    class Menu {
        -contacts: ManagerContact
        -forms: Forms
        +run()
        +display_menu()
    }

    class Forms {
        -contacts: ManagerContact
        +display_add_contact()
        +display_show_contact()
        +display_search_contact()
        +display_edit_contact()
        +display_delete_contact()
        +display_import_contacts()
        +display_export_contacts()
    }

    class ManagerContact {
        -dbm: DatabaseManager
        +add_contact(name, phone)
        +search_contact(option, name, phone)
        +edit_contact(orig, name, phone)
        +delete_contact(name)
        +csv_import_contacts(path)
        +csv_export_contacts(path)
    }

    class DatabaseManager {
        -db_path: str
        -logs: str
        +get_connection()
        +initialize_database()
        +query_data(option, params)
        +insert_data(params)
        +update_data(params)
        +delete_data(param)
    }

    class Validations {
        <<Utility>>
        +get_name(prompt, error)
        +get_phone(prompt, error)
        +get_option(prompt, error)
    }

    class Models {
        <<Data>>
        +Contact
        +Contacts
    }

    %% Relaciones
    Menu *-- Forms : utiliza
    Menu *-- ManagerContact : orquesta
    Forms --> ManagerContact : llama a lógica
    Forms ..> Validations : valida inputs
    ManagerContact *-- DatabaseManager : persiste datos
    ManagerContact ..> Models : estructura datos
    DatabaseManager ..> Models : mapea filas
```