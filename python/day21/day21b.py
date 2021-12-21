START_A = 9
START_B = 3

WIN_CONDITION = 21

POSSIBLE_ROLL_COUNTS = [1, 3, 6, 7, 6, 3, 1]

class Game:
    def __init__(self, start_1, start_2, score_1, score_2, turn):
        self.pos_1 = start_1
        self.pos_2 = start_2
        self.score_1 = score_1
        self.score_2 = score_2
        self.turn = turn

    def is_won(self):
        if self.score_1 >= WIN_CONDITION:
            return 1
        if self.score_2 >= WIN_CONDITION:
            return 2
        return None

    def move(self, die_roll_sum):
        if self.turn == 1:
            self.pos_1 = (self.pos_1 + die_roll_sum) % 10
            self.score_1 += self.pos_1 + 1
            self.turn = 2
            return
        if self.turn == 2:
            self.pos_2 = (self.pos_2 + die_roll_sum) % 10
            self.score_2 += self.pos_2 + 1
            self.turn = 1
            return



def games_won(start_game):
    outcome = start_game.is_won()
    if outcome:
        output = [0, 0]
        output[outcome-1] = 1
        return output
    games = [Game(start_game.pos_1, start_game.pos_2, start_game.score_1,
                  start_game.score_2, start_game.turn) for k in range(3, 10)]
    for k in range(3, 10):
        games[k-3].move(die_roll_sum=k)
    outcomes = [games_won(game) for game in games]
    outcomes = [[POSSIBLE_ROLL_COUNTS[i]*outcome for outcome in outcomes[i]] for i in range(len(outcomes))]
    return [sum([outcome[i] for outcome in outcomes]) for i in range(2)]


if __name__ == '__main__':
    print(games_won(Game(START_A, START_B, 0, 0, 1)))