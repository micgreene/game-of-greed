import random
from collections import Counter
class GameLogic:
    
    @staticmethod
    def roll_dice(num):
        rolls = []
        for _ in range(num):
            rolls.append(random.randint(1,6))
        return tuple(rolls)

    @staticmethod
    def calculate_score(dice):
        score = 0
        counter = Counter(dice)
        n = len(counter)
        if n == 6 and all(count == 1 for count in counter.values()):
            return 1500 #handle straight
        elif n == 3 and all(count == 2 for count in counter.values()):
            return 1500 #handle three pairs
        else:
            for num, count in counter.items(): 
                if count >= 3:
                    #handle 3-6 of a kind
                    score += GameLogic.calc_triples_and_above(num, count)
                else:
                    #handle single 1's and 5's 
                    score += GameLogic.calc_singles(num, count) 
        return score

    @staticmethod
    def calc_triples_and_above(num, count):
        if num == 1:
            return 1000 * (count-2)
        else:
            return (100*num) * (count-2)

    @staticmethod
    def calc_singles(num, count):
        score = 0
        if num == 1: 
            score += 100 * count
        elif num == 5:
            score += 50 * count
        return score
