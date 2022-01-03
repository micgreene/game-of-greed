
from game_of_greed.game_logic import GameLogic
from game_of_greed.banker import Banker 
from textwrap import dedent

class Game:

    def __init__(self):
        self.round = 1
        self.banker = Banker()
        self.num_dice = 6
        
    def play(self, roller = GameLogic.roll_dice):
        starting = self.start_game()
        if starting:  
            while True:
                self.roll_dice(roller)
                selection = input('> ')
                if selection.lower() == 'q':
                    break
                self.select_dice(selection)
                selection = input('> ')
                if selection.lower() == 'b':
                    self.handle_banking()
                elif selection.lower() == 'q':
                    break
            self.exit_game()
        else:
            print('OK. Maybe another time')


    def start_game(self):
        welcome_msg = dedent('''\
        Welcome to Game of Greed
        (y)es to play or (n)o to decline''')
        print(welcome_msg)
        selection = input('> ')
        starting = selection.lower() == 'y'
        if starting:
            print(f'Starting round 1')
        return starting
    
    def exit_game(self):
        print(f'Thanks for playing. You earned {self.banker.balance} points')
        #reset game settings
        self.banker.clear_shelf()
        self.banker.balance = 0
        self.round = 1
        self.num_dice = 6

    def roll_dice(self, roller):
        print(f'Rolling {self.num_dice} dice...')
        roll_str = ''
        for roll in roller(self.num_dice):
            roll_str += str(roll) + ' '
        print(f'*** {roll_str}***')
        print('Enter dice to keep, or (q)uit:')
    
    def select_dice(self, selected):
        dice = tuple(map(int, list(selected))) # Adapted from https://www.geeksforgeeks.org/python-convert-string-to-tuple/
        score = GameLogic.calculate_score(dice)
        self.banker.shelf(score)
        self.num_dice -= len(dice)
        print(f'You have {self.banker.shelved} unbanked points and {self.num_dice} dice remaining')
        print('(r)oll again, (b)ank your points or (q)uit:')

    def handle_banking(self):
        print(f'You banked {self.banker.shelved} points in round {self.round}')
        self.banker.bank()
        self.banker.clear_shelf()
        print(f'Total score is {self.banker.balance} points')
        self.round += 1
        self.num_dice = 6
        print(f'Starting round {self.round}')

if __name__ == '__main__':
    game = Game()
    game.play()
        