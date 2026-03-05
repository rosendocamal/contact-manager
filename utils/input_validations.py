def get_phone(prompt: str, error: str) -> int:
    while True:
        try:
            phone: int = int(input(prompt))
        except ValueError:
            print(error)
        else:
            return phone

def get_name(prompt: str, error: str) -> str:
    while True:
        try:
            name: str = input(prompt)
        except ValueError:
            print(error)
        else:
            return name
        
def get_option(prompt: str, error: str) -> int:
    options: set = {1, 2}
    while True:
        try:
            option: int = int(input(prompt))

            if option not in options:
                print(error)
                continue
        except ValueError:
            print(error)
        else:
            return option