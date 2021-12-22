import random
class GameLogic:
    
    @staticmethod
    def roll_dice(num_dice_thrown):
        dice_list = []
        for _ in range(num_dice_thrown):
            dice_list.append(random.randint(1,6))
        return dice_list

    @staticmethod
    def calculate_score():
        pass
    