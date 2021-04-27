import termcolor

from utils import TICKET_PRICES, WRISTBAND_PRICE


def get_total_price(children: int, adults: int, seniors: int, wristbands: int) -> int:
    """
    Returns the total price to buy these tickets
    :param children: The amount of children attending
    :param adults: The amount of adults attending
    :param seniors: The amount of seniors attending
    :param wristbands: The amount of wristbands wanted
    :return: The total price for all tickets
    """
    children_price = children * TICKET_PRICES['child']
    adult_prices = adults * TICKET_PRICES['adult']
    senior_prices = seniors * TICKET_PRICES['senior']
    wristband_price = wristbands * WRISTBAND_PRICE

    return children_price + adult_prices + senior_prices + wristband_price


def prompt_ticket_category(name: str) -> int:
    """
    Promts the user to enter the count of indivdual tickets
    :param name: The name of the ticket type they would like to buy
    :return: An integer representing their input
    """

    try:
        value = int(input(f"How many {name} tickets?: "))

        if value < 0:
            raise ValueError("You")

        return value
    except ValueError:
        print(termcolor.colored("Uh oh! You must only enter a valid number above or equal to 0.", "red"))
        return prompt_ticket_category(name)


def prompt_ticket_input() -> tuple[int, int, int, int]:
    """
    Prompts the user for the amount of tickets & wristbands they would like to purchase
    :return: A tuple of total tickets in order `children, adults, senior, wristbands`
    """
    children = prompt_ticket_category("child")
    adults = prompt_ticket_category("adult")
    senior = prompt_ticket_category("senior")

    if children + adults + senior == 0:
        print(termcolor.colored("Oh oh! There must be at least one person attending!", "red"))
        return prompt_ticket_input()

    wristbands = prompt_ticket_category("wristband")

    return children, adults, senior, wristbands
