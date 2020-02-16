import random
import time

# res = ''.join(random.choices("yn", k=1))
# print(res)
class Human_Computer:
    def __init__(self):
        self.score_1 = 0
        self.score_2 = 0
        self.player1 = input('Enter the name of player 1:').capitalize()

    def human_player(self):

        while self.score_1 <= 100 and self.score_2 <= 100:

            input('{} press enter to roll the dice:'.format(self.player1))

            player1_dice_1 = random.randrange(1, 7)
            player1_dice_2 = random.randrange(1, 7)
            print('{} turn:'.format(self.player1))
            print(player1_dice_1)
            print(player1_dice_2)

            if player1_dice_1 == 1 and player1_dice_2 == 1:
                self.score_1 = self.score_1 * 0
                print('Sorry! {} you lost your turn and total score:'.format(self.player1))
                obj.computer_player()

            elif player1_dice_1 == 1 or player1_dice_2 == 1:
                self.score_1 = self.score_1 + 0
                print('Sorry! {} you lost your turn and points of turn:'.format(self.player1))
                obj.computer_player()

            else:
                player_1 = player1_dice_1 + player1_dice_2
                print('{} your point of the current turn is'.format(self.player1), player_1)
                print('{} you want to hold?'.format(self.player1))
                choose1 = input("Enter Y for yes or N for no.").lower()

                if choose1 == 'y':
                    self.score_1 = self.score_1 + player_1
                    if self.score_1 >= 100:
                        print('{} your score is'.format(self.player1), 100)
                    else:
                        print('{} your score is'.format(self.player1), self.score_1)
                    if self.score_1 >= 100:
                        print('Congratulations {} you are  winner!'.format(self.player1))

                else:
                    self.score_1 = self.score_1
                    print('{} score'.format(self.player1), self.score_1)

            self.score_1 = self.score_1

    def computer_player(self):

        while self.score_1 < 100 and self.score_2 < 100:
            time.sleep(2)
            computer_dice_1 = random.randrange(1, 7)
            computer_dice_2 = random.randrange(1, 7)
            print('computer turn:')
            print(computer_dice_1)
            print(computer_dice_2)

            if computer_dice_1 == 1 and computer_dice_2 == 1:
                self.score_2 = self.score_2 * 0
                print('Sorry! computer you lost your turn and total score:')
                obj.human_player()

            elif computer_dice_1 == 1 or computer_dice_2 == 1:
                self.score_2 = self.score_2 + 0
                print('Sorry! computer has lost its turn and points of current turn:')
                obj.human_player()

            else:
                computer = computer_dice_1 + computer_dice_2
                print('computer points of the turn is', computer)
                # print('{} you want to hold?'.format(computer))
                # choose2 = input("Enter Y for yes or N for no.").lower()

                # if choose2 == 'y':
                self.score_2 = self.score_2 + computer
                if self.score_2 >= 100:
                    print('Computer score is ', 100)
                else:
                    print('Computer score is', self.score_2)

                if self.score_2 >= 100:
                    print('Congratulations, computer is winner.')

            self.score_2 = self.score_2

if __name__=='__main__':
    obj = Human_Computer()
    obj.human_player()