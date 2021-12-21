START_A = 9
START_B = 3


class Game:
    def __init__(self, start_1, start_2):
        self.pos_1 = start_1
        self.pos_2 = start_2
        self.score_1 = 0
        self.score_2 = 0
        self.deterministic_die_rolls = 0

    def is_won(self):
        if self.score_1 >= 1000:
            return True
        if self.score_2 >= 1000:
            return True
        return False

    def move_deterministic(self):
        move = 0
        for k in range(3):
            move += ((self.deterministic_die_rolls) % 100) + 1
            self.deterministic_die_rolls += 1
        self.pos_1 = (self.pos_1 + move) % 10
        self.score_1 += self.pos_1 + 1
        if self.is_won():
            return None
        move = 0
        for k in range(3):
            move += ((self.deterministic_die_rolls) % 100) + 1
            self.deterministic_die_rolls += 1
        self.pos_2 = (self.pos_2 + move) % 10
        self.score_2 += self.pos_2 + 1

    def play_deterministic_game(self):
        while not self.is_won():
            self.move_deterministic()

if __name__ == '__main__':
    game = Game(START_A,START_B)
    game.play_deterministic_game()
    if game.score_1 >= 1000:
        print(game.score_2*game.deterministic_die_rolls)
    if game.score_2 >= 1000:
        print(game.score_1*game.deterministic_die_rolls)
