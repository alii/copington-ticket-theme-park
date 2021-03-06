import datetime
from time import sleep

import termcolor

from utils import print_welcome, prompt_ticket_input, get_total_price, is_positive, ensure_paid_enough, PARK_NAME, \
    id_generator, MAXIMUM_PARK_CAPACITY

"""
The total amount of tickets purchased today
"""
total_day_tickets = 0


def start_purchase_flow(show_welcome=True) -> None:
    """
    Starts the purchase flow for a user. This can be regarded as the main loop
    as it resets after a purchase.
    :return:
    """

    global total_day_tickets

    try:
        if total_day_tickets > MAXIMUM_PARK_CAPACITY:
            print(termcolor.colored("Uh oh! The park is at maximum capacity for today!"))
            return

        if show_welcome:
            print_welcome()

        children, adults, seniors, wristbands = prompt_ticket_input()

        total_tickets = children + adults + seniors

        if total_tickets + total_day_tickets > MAXIMUM_PARK_CAPACITY:
            message = termcolor.colored("You cannot purchase that many tickets as the park will be at full capacity",
                                        "red")
            print(message)
            print(f"There are {MAXIMUM_PARK_CAPACITY - total_day_tickets} remaining for today.")
            return start_purchase_flow(show_welcome=False)

        total_day_tickets += total_tickets

        total = get_total_price(children, adults, seniors, wristbands)

        surname = input("What is your surname for the order?: ")
        requires_parking_pass = is_positive(input("Do you require a parking pass?: "))

        print(f"Okay {surname}, that will be £" + str(total))

        total_paid = ensure_paid_enough(total)
        change = total_paid - total

        if change > 0:
            green_change = termcolor.colored(str(change), "green")
            print(f"Paying you £{green_change} change!")

        if requires_parking_pass:
            code = id_generator()
            print(f"Your parking pass is {code}")

        ticket_id = id_generator()
        today = datetime.date.today()

        print(
            f"Your ticket on {today} is {ticket_id}. You purchase {wristbands} wristbands & {total_tickets} total tickets.")
        print(f"Thank you for visiting {PARK_NAME}")

        # Finalised, we can start the flow now.
        sleep(10)
        start_purchase_flow()

    except KeyboardInterrupt:
        start_purchase_flow()


if __name__ == '__main__':
    start_purchase_flow()
