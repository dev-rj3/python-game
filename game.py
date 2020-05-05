from random import randint
import sys


class GuessGame:

    def __init__(self, lower_bound=1, upper_bound=100):
        self.__MIN = lower_bound
        self.__MAX = upper_bound

    def play(self):
        self.__NUMBER = randint(self.__MIN, self.__MAX)
        self.__guesses = 1
        while 1:

            number = self.__get_guess()

            if number > self.__NUMBER:
                print('Guess is too high.')
            elif number < self.__NUMBER:
                print('Guess is too low.')
            else:
                break
            self.__guesses += 1

        print(f'Guessed with {self.__guesses}')
        self.__play_again()

    def __play_again(self):
        respose = input('Want to play again? y/n ')
        respose = respose.lower().strip()
        if respose[0] == 'y':
            self.play()
        else:
            sys.exit(1)

    def __get_guess(self):
        response = input(
            f'Guess a number from {self.__MIN} to {self.__MAX}: ')

        parsed_response = self.__is_valid_number(response)
        if (parsed_response):
            number = int(response)
            return number

        print("Please enter a valid number")
        return self.__get_guess()

    def __is_valid_number(self, response):
        try:
            number = int(response)
        except:
            return False
        return self.__MIN <= number <= self.__MAX
