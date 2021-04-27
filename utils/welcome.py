from utils.constants import PARK_NAME, TICKET_PRICES
from termcolor import colored


def print_welcome() -> None:
    """
    Prints a welcome message to the console
    :return: Nothing
    """
    message = f"Welcome to {PARK_NAME}"
    separators = colored("•" * len(message), "green")

    print(separators)
    print(colored(message, "blue"))
    print(separators)

    print(colored("Prices:", "red", attrs=["bold"]))
    print(f'''
    Entrance Ticket
        Adult			£{TICKET_PRICES['adult']}
        Child			£{TICKET_PRICES['child']}
        Senior Citizen	£{TICKET_PRICES['senior']}
        
        
    Wristband
        All             £20
        
    Parking
        Free (car pass must be displayed)
    ''')
