def ask_yes_no(question):
    response = None

    expected_responses = ('no', 'n', 'yes', 'y')

    while response not in expected_responses:
        response = input(question + "\n").lower()

        # Error message
        if response not in expected_responses:
            print('Wrong input please <yes/no>')

    if response == 'yes' or response == 'y':
        return True
    else:
        return False


def ask_for_value(question):
    """The solution for asking for a integer value without using exceptions """

    answer = ""

    while not answer.isdigit():
        answer = input(question)

        # Error message
        if not answer.isdigit():
            print("Input must be a number!")
        else:
            # Cast for answer
            return int(answer)

    return answer

def ask_to_keep_playing():
    return ask_yes_no("Do you want to keep playing?")
