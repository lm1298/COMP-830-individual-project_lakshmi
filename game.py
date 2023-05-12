"""
Project-Individual Project
Author-Lakshmi Prasanna
File-game.py
"""


class Question:
    """
    A class to represent a yes/no question in the game.

    Attributes:
    - text (str): The text of the question.
    - yes_question (Question): The follow-up question if the answer is "yes".
    - no_question (Question): The follow-up question if the answer is "no".

    Methods:
    - follow_up_question(answer): Returns the follow-up question based on the answer.
    """

    def __init__(self, text, yes_question=None, no_question=None):
        """
        Initialize a new Question object.

        Parameters:
        - text (str): The text of the question.
        - yes_question (Question): The follow-up question if the answer is "yes". Default is None.
        - no_question (Question): The follow-up question if the answer is "no". Default is None.
        """
        self.text = text
        self.yes_question = yes_question
        self.no_question = no_question

    def follow_up_question(self, answer):
        """
        Returns the follow-up question based on the answer.

        Parameters:
        - answer (str): The answer to the current question ("yes" or "no").

        Returns:
        - The follow-up question if the answer is "yes" or "no".
        - Raises a ValueError if the answer is not "yes" or "no".
        """
        if answer == "yes":
            return self.yes_question
        elif answer == "no":
            return self.no_question
        else:
            raise ValueError("Invalid answer. Please answer 'yes' or 'no'.")


class Game:
    """
    A class to represent the game.

    Attributes:
    - root_question (Question): The root question of the game.

    Methods:
    - start(): Starts the game.
    - ask_question(question): Asks a question and follows up with a new question based on the answer.
    - end_game(): Ends the game.
    """

    def __init__(self, root_question):
        """
        Initialize a new Game object.

        Parameters:
        - root_question (Question): The root question of the game.
        """
        self.root_question = root_question

    def reset_game(self):
        """
        Restart the game from the beginning.
        """
        print("Resetting game...")
        self.start()

    def start(self):
        """
        Starts the game by printing a message and asking the root question.
        """
        print("Start")
        self.ask_question(self.root_question)

    def ask_question(self, question):
        """
        Asks a question and follows up with a new question based on the answer.

        Parameters:
        - question (Question): The question to ask.

        Returns:
        - If the answer is "yes" or "no", the follow-up question is returned.
        - If the answer is invalid, the same question is asked again.
        """
        answer = input(question.text + " (yes/no) ")
        if answer == "yes":
            follow_up = question.yes_question
        elif answer == "no":
            follow_up = question.no_question
        else:
            print("Invalid answer. Please answer 'yes' or 'no'.")
            self.ask_question(question)
            return

        if follow_up is None:
            self.end(answer)
        else:
            self.ask_question(follow_up)

    def end(self, answer):
        """
        Ends the game and asks if the user wants to play again.
        """
        # answer = input("Do you want to try again? (yes/no) ")
        if answer == "yes":
            self.reset_game()
        elif answer == "no":
            print("End")
            exit()


def main():
    q1 = Question(
        "Welcome to the game! Think of a design pattern and answer these following yes/no questions. Ready?",
        yes_question=Question(
            "Does it provide the object creation mechanism that enhance the flexibilities of existing code?",
            yes_question=Question(
                "Does it ensure you to have at most one instance of a class in your application?",
                yes_question=Question("Is it Singleton pattern?",
                                      yes_question=Question("Woohoo! I guessed it! Try again?"),
                                      no_question=Question("Oops! Something went wrong! Try again?")),
                no_question=Question("Is it Builder pattern?",
                                     yes_question=Question("Woohoo! I guessed it! Try again?"),
                                     no_question=Question(
                                         "Oops! Something went wrong! Try again?"))),
            no_question=Question("Is it responsible for how one class communicates with others ?",
                                 no_question=Question(
                                     "Does it explain how to assemble objects and classes into a larger structure and "
                                     "simplifies the structure by identifying the relationships?",

                                     yes_question=Question("Does it attach additional behaviour to object at run-time?",
                                                           yes_question=Question("Is it Decorator pattern?",
                                                                                 yes_question=Question(
                                                                                     "Woohoo! I guessed it! Try again?"),
                                                                                 no_question=Question(
                                                                                     "Oops! Something went wrong! Try "
                                                                                     "again?")),
                                                           no_question=Question("Is it Adapter pattern?",
                                                                                yes_question=Question(
                                                                                    "Woohoo! I guessed it! Try again?"),
                                                                                no_question=Question(
                                                                                    "Oops! Something went wrong! Try "
                                                                                    "again? "))),
                                     no_question=Question(
                                         "Oops! Something went wrong! "
                                         "Try" "again?")),
                                 yes_question=Question(
                                     "Does it provide a mechanism to the context to change its behaviour?",
                                     yes_question=Question("Is changing behaviour built into its scheme?",
                                                           yes_question=Question("Is it State pattern?",
                                                                                 yes_question=Question(
                                                                                     "Woohoo! I guessed it! Try again?"),
                                                                                 no_question=Question(
                                                                                     "Oops! Something went wrong! Try "
                                                                                     "again?")),
                                                           no_question=Question("Is it Strategy pattern?",
                                                                                yes_question=Question(
                                                                                    "Woohoo! I guessed it! Try again?"),
                                                                                no_question=Question(
                                                                                    "Oops! Something went wrong! Try "
                                                                                    "again?"))),
                                     no_question=Question("Does it allow group of objects to be notified "
                                                          "when some state changes?",
                                                          yes_question=Question("Is it Observer pattern?",
                                                                                yes_question=Question(
                                                                                    "Woohoo! I guessed it! Try again?"),
                                                                                no_question=Question(
                                                                                    "Oops! Something went wrong! Try "
                                                                                    "again?")),
                                                          no_question=Question("Is it Command pattern?",
                                                                               yes_question=Question(
                                                                                   "Woohoo! I guessed it! Try again?"),
                                                                               no_question=Question(
                                                                                   "Oops! Something went wrong! Try "
                                                                                   "again?")))))))

    # Create and start the game
    game = Game(q1)
    game.start()


if __name__ == '__main__':
    main()
