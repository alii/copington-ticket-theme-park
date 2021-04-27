import termcolor


def prompt_input_bill(note_type: int) -> int:
    """
    Prompts the user for a single note count
    :param note_type: The note type to insert into the machine
    :return: A validated count of all notes inserted for this note_type
    """
    try:
        value = int(input(f"How many {str(note_type)} pound notes are you inserting?: "))

        if value < 0:
            raise ValueError("Must be above 0")

        return value
    except ValueError:
        print(termcolor.colored("Uh oh! You must insert a valid number of notes.", "red"))
        return prompt_input_bill(note_type)


def ensure_paid_enough(total: int):
    """
    Ensures that a user has paid enough money for the total.
    Recurses until enough money has been paid. Does not account for change!
    :param total: The total amount needed to pay
    :return: The total amount paid (for calculating change)
    """
    grand_total_paid = 0

    def closure():
        nonlocal grand_total_paid

        tens, twenties = prompt_input_bills()
        iteration_paid = (tens * 10) + (twenties * 20)
        grand_total_paid += iteration_paid

        if total > iteration_paid:
            return closure()

        return grand_total_paid

    return closure()


def prompt_input_bills() -> tuple[int, int]:
    """
    Prompts the user to insert all types of notes
    :return: A tuple of order ten pound notes, twenty pound notes
    """
    ten_pound_notes = prompt_input_bill(10)
    twenty_pound_notes = prompt_input_bill(20)

    return ten_pound_notes, twenty_pound_notes
