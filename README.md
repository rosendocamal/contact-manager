# Agenda de Contactos

Agenda de Contactos realizado en `Python` utilizando Programación Orientada a Objetos (`POO`), utilizando modularización, gestionando una base de datos en `SQLite` y validando entradas del usuario.

<img src="img/.menu.png" alt="PANTALLA DE MENU" width="500">

> Menú

<img src="img/.show.png" alt="PANTALLA DE MOSTRAR" width="500">

> Ventana de Listar contactos

<img src="img/.delete.png" alt="PANTALLA DE DELETE" width="500">

> Ventana de Eliminar un contacto

<img src="img/.export.png" alt="PANTALLA DE EXPORTAR" width="500">

> Ventana de Exportar contactos

<img src="img/.exit.png" alt="PANTALLA DE SALIR" width="500">

> Cierre del programa

## Base de Datos

He utilizado `SQlite` para la persistencia de los datos. He utilizado una tabla bastante sencilla para ello:

| id | name | phone |
|----|------|-------|
|1|CONTACTO1|1231231234|
|2|CONTACTO2|3213213214|

## Detalles del programa

La estructura del programa se muestra en el diagrama realizado con `mermaid`:

```mermaid
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

## Instrucciones de uso

1. Clona el repositorio. Para ello, ejecuta el siguiente comando:

```
git clone https://github.com/rosendocamal/contact-manager.git
```

2. Ubícate en la carpeta principal del repositorio y ejecuta:

```
python3 app.py
```

3. Sigue las intrucciones del menú interactivo.

## Tecnologías y herramientas

![Python](https://img.shields.io/badge/python-3562A5?style=for-the-badge&logo=python&logoColor=white)
![CSV](https://img.shields.io/badge/csv-4285F4?style=for-the-badge&logo=google-sheets&logoColor=white)
![SQLite](https://img.shields.io/badge/SQLite-07405E?style=for-the-badge&logo=sqlite&logoColor=white)
![SQL](https://img.shields.io/badge/SQL-CC2927?style=for-the-badge&logo=sqlite&logoColor=white)
![Fedora](https://img.shields.io/badge/Fedora-51A2DA?style=for-the-badge&logo=fedora&logoColor=white)
![VS Code](https://img.shields.io/badge/Visual%20Studio%20Code-007ACC?style=for-the-badge&logo=visualstudiocode&logoColor=white) 
![Neovim](https://img.shields.io/badge/Neovim-57A143?style=for-the-badge&logo=neovim&logoColor=white)
![Git](https://img.shields.io/badge/Git-F05032?style=for-the-badge&logo=git&logoColor=white)
![GitHub](https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white)


## Licencia

Este proyecto está licenciado bajo la Licencia MIT. Para más detalles consulta el archivo [LICENSE](LICENSE).

## Autor

Proyecto desarrollado por **Rosendo Camal**.

Contacto:
* [GitHub](https://github.com/rosendocamal)
* [Linkedin](https://www.linkedin.com/in/rosendocamal)