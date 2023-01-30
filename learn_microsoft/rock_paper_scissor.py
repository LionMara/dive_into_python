#!/usr/bin/python3


'''
Rock, paper, scissors is a game played by two participants.
 The game consists of rounds. In each round,
 a participant chooses a symbol from rock, paper, or scissors,
 and the other participant does the same.
 Then a winner of the round is determined by comparing the chosen symbols.
 The rules of the game state that rock wins over scissors,
 scissors beats (cuts) paper, and paper beats (covers) rock.
 The winner of the round is awarded a point.
 The game goes on for as many rounds as the participants agree on.
 The winner is the participant with the most points.

;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;

Actors - participants_1, participant_2, game, gameround
Behavior - participants choose a symbol
           gameround comparing chosen symbols
           compare symbols RvS - R wins
                          RvP - P wins
                          PvS - S wins
           accumulate points, Win = 1
Data - choice - rock, scissors, paper

'''
class Participant():
    '''Class that will have particpant 1 and 2 '''

    def __init__(self, name):
        self.name = name
        self.points = 0
        self.choice = ''

    def choose(self):
        ''' a method to make choice'''
        self.choice = input("{name}, select rock, paper, scissor, lizard, or Spock: "
                            .format(name=self.name))
        print("{name} selects {choice}"
              .format(name=self.name, choice=self.choice))
    def to_numerical_choice(self):
        switcher = {
            "rock": 0,
            "paper": 1,
            "scissor": 2,
            "lizard": 3,
            "spock" : 4
            }
        return switcher[self.choice]

    def increment_point(self):
        self.points += 1


class GameRound():
    '''Class for game sequence'''
    def __init__(self, p1, p2):
        self.rules = [
            [0, -1, 1, 1, -1],
            [1, 0, -1, -1, 1],
            [-1, 1, 0, 1, -1],
            [-1, 1, -1, 0, 1],
            [1, -1, 1, -1, 0]
            ]

        p1.choose()
        p2.choose()
        result = self.compare_choices(p1, p2)
        print("Round resulted in a {result}"
              .format(result = self.get_result_as_string(result)))

        if result > 0:
            p1.increment_point()
        elif result < 0:
            p2.increment_point()


    def compare_choices(self, p1, p2):
        return self.rules[p1.to_numerical_choice()][p2.to_numerical_choice()]

    def get_result_as_string(self, result):
        res = {
            0: "draw",
            1: "win",
            -1: "loss"
            }
        return res[result]
    def award_points(self):
        print("implement")


class Game():
    '''The game begins here '''
    def __init__(self):
        self.end_game = False
        self.participant =Participant("Spock")
        self.second_participant = Participant("Kirk")

    def start(self):
        while not self.end_game:
            game_round = GameRound(self.participant, self.second_participant)

    def check_end_condition(self):
        answer = input("Continue game y/n: ")
        if answer =='y':
            GameRound(self.participant, self.second_participant)
            self.check_end_condition()
        else:
            print("Game ended, {p1name} has {p1points}, and {p2name} has {p2points}"
                  .format(p1name = self.participant.name,
                          p1points = self.participant.points,
                          p2name = self.second_participant.name,
                          p2points = self.second_participant.points))
            self.determine_winner()
            self.end_game = True
    def determine_winner(self):
        result_string = "it's a draw"
        if self.participant.points > self.second_participant.points:
            result_string = "Winner is {name}".format(name=self.participant.name)
        elif self.participant.points < self.second_participant.points:
            result_string = "Winner is {name}".format(name=self.second_participant.name)

        print(result_string)

game = Game()
game.start()
