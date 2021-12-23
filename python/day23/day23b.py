import numpy as np

HALL = ["." for k in range(11)]
ROOMS = {2: 'DDDB', 4: 'ACBC', 6: 'CBAB', 8: 'DACA'}
ROOM_LENGTH = 4

LEGAL_HALL_INDICIES = [0, 1, 3, 5, 7, 9, 10]

COSTS = {'A': 1,
         'B': 10,
         'C': 100,
         'D': 1000}

DEST_ROOMS = {'A': 2,
              'B': 4,
              'C': 6,
              'D': 8}

PAST_COST_COMPUTATION = {}


class Game:
    def __init__(self, hall, rooms, incurred_cost):
        self.hall = hall
        self.rooms = rooms
        self.incurred_cost = incurred_cost

    def is_legal_hall_move(self, room, destination_index):
        for k in range(destination_index, room + 1):
            if self.hall[k] != '.':
                return False
        for k in range(room, destination_index + 1):
            if self.hall[k] != '.':
                return False
        return True

    def is_legal_room_move(self, start_index, room):
        for k in range(start_index + 1, room + 1):
            if self.hall[k] != '.':
                return False
        for k in range(room + 1, start_index):
            if self.hall[k] != '.':
                return False
        return True

    def is_complete(self):
        if self.rooms[2] == "A" * ROOM_LENGTH:
            if self.rooms[4] == "B" * ROOM_LENGTH:
                if self.rooms[6] == "C" * ROOM_LENGTH:
                    if self.rooms[8] == "D" * ROOM_LENGTH:
                        return True
        return False

    def only_contents_at_destination(self, room):
        for char in self.rooms[room]:
            if char == ".":
                continue
            if DEST_ROOMS[char] != room:
                return False
        return True

    def get_legal_moves(self):
        moves = []
        for room in self.rooms:
            if self.only_contents_at_destination(room):
                continue
            j = 0
            while self.rooms[room][j] == ".":
                j += 1
            for k in LEGAL_HALL_INDICIES:
                anthro = self.rooms[room][j]
                if self.is_legal_hall_move(room, k):
                    moves.append([anthro, room, k, (np.abs(k - room) + 1 + j) * COSTS[anthro]])

        for k in range(len(self.hall)):
            anthro = self.hall[k]
            if anthro != '.':
                room = DEST_ROOMS[anthro]
                if self.is_legal_room_move(k, room):
                    if self.only_contents_at_destination(room):
                        j = ROOM_LENGTH - 1
                        while self.rooms[room][j] != ".":
                            j -= 1
                        moves.append([anthro, k, room, (np.abs(k - room) + j + 1) * COSTS[anthro]])
        return moves

    def move(self, anthro, start_index, end_index, cost):
        self.incurred_cost += cost
        if start_index in self.rooms:
            j = 0
            while self.rooms[start_index][j] == ".":
                j += 1
            self.rooms[start_index] = (j + 1) * "." + self.rooms[start_index][j + 1:]
            self.hall[end_index] = anthro
        else:
            j = ROOM_LENGTH - 1
            contents = self.rooms[end_index]
            while contents[j] != ".":
                j -= 1
            self.rooms[end_index] = "." * j + anthro + contents[j + 1:]
            self.hall[start_index] = "."


def get_minimum_cost(current_game):
    if current_game.is_complete():
        print("COMPLETE!", current_game.incurred_cost)
        return current_game.incurred_cost
    hash = str(current_game.hall) + str(current_game.rooms)
    if hash in PAST_COST_COMPUTATION:
        return current_game.incurred_cost + PAST_COST_COMPUTATION[hash]
    else:
        moves = current_game.get_legal_moves()
        if len(moves) == 0:
            return None
        games = [Game(current_game.hall.copy(), current_game.rooms.copy(), 0) for _ in moves]
        for k in range(len(moves)):
            games[k].move(moves[k][0], moves[k][1], moves[k][2], moves[k][3])
        costs = [get_minimum_cost(game) for game in games]
        costs = [cost for cost in costs if cost is not None]
        if len(costs) == 0:
            return None
        PAST_COST_COMPUTATION[hash] = min(costs)
        return current_game.incurred_cost + min(costs)


if __name__ == "__main__":
    new_game = Game(HALL.copy(), ROOMS.copy(), 0)
    print(get_minimum_cost(new_game))
