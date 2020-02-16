
import random


# res = ''.join(random.choices("yn", k=1))
# print(res)
class Human_Human:
    def __init__(self):
        self.score_1 = 0
        self.score_2 = 0
        self.player1 = input('Enter the name of player 1:').capitalize()
        self.player2 = input('Enter the name of player 2:').capitalize()

    def player_one(self):

        while self.score_1 < 100 and self.score_2 < 100:

            input('{} press enter to roll the dice:'.format(self.player1))

            player1_dice_1 = random.randrange(1, 7)
            player1_dice_2 = random.randrange(1, 7)
            print('{} turn:'.format(self.player1))
            print(player1_dice_1)
            print(player1_dice_2)

            if player1_dice_1 == 1 and player1_dice_2 == 1:
                self.score_1 = self.score_1 * 0
                print('Sorry! {} you lost your turn and total score:'.format(self.player1))
                obj.player_two()

            elif player1_dice_1 == 1 or player1_dice_2 == 1:
                self.score_1 = self.score_1 + 0
                print('Sorry! {} you lost your turn and points of turn:'.format(self.player1))
                obj.player_two()

            else:
                player_1 = player1_dice_1 + player1_dice_2
                print('{} points of the current turn is'.format(self.player1), player_1)
                print('{} you want to hold?'.format(self.player1))
                choose1 = input("Enter Y for yes or N for no.").lower()

                if choose1 == 'y':
                    self.score_1 = self.score_1 + player_1
                    if self.score_1 >= 100:
                        print('{} your score is'.format(self.player1), 100)
                    else:
                        print('{} your score is'.format(self.player1), self.score_1)

                    if self.score_1 >= 100:
                        print('Congratulations! {} you are  winner!'.format(self.player1))
                else:
                    self.score_1 = self.score_1
                    print('{} score'.format(self.player1), self.score_1)

            self.score_1 = self.score_1

    def player_two(self):

        while self.score_1 < 100 and self.score_2 < 100:

            input('{} press enter to roll the dice:'.format(self.player2))

            player2_dice_1 = random.randrange(1, 7)
            player2_dice_2 = random.randrange(1, 7)
            print('{} turn:'.format(self.player2))
            print(player2_dice_1)
            print(player2_dice_2)

            if player2_dice_1 == 1 and player2_dice_2 == 1:
                self.score_2 = self.score_2 * 0
                print('Sorry! {} you lost your turn and total score:'.format(self.player2))
                obj.player_one()

            elif player2_dice_1 == 1 or player2_dice_2 == 1:
                self.score_2 = self.score_2 + 0
                print('Sorry! {} you lost your turn and points of current turn:'.format(self.player2))
                obj.player_one()
            else:
                # print("Player 2 - dice 1 and dice 2=", player2_dice_1, player2_dice_2)
                player_2 = player2_dice_1 + player2_dice_2
                print('{} points of the current turn is'.format(self.player2), player_2)
                print('{} you want to hold?'.format(self.player2))
                choose2 = input("Enter Y for yes or N for no.").lower()

                if choose2 == 'y':
                    self.score_2 = self.score_2 + player_2
                    if self.score_2 >= 100:
                        print('{} your score is'.format(self.player1), 100)
                    else:
                        print('{} your score is'.format(self.player1), self.score_2)

                    if self.score_2 >= 100:
                        print('Congratulations! {} you are winner'.format(self.player2))
                else:
                    self.score_2 = self.score_2
                    print('{} your score'.format(self.player2), self.score_2)

            self.score_2 = self.score_2



# obj = Human_Human()
#
# obj.player_one()
