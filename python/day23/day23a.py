import numpy as np

HALL = ["." for k in range(11)]
ROOMS = {2: 'DB', 4: 'AC', 6: 'CB', 8: 'DA'}

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
        if self.rooms[2] == "AA":
            if self.rooms[4] == "BB":
                if self.rooms[6] == "CC":
                    if self.rooms[8] == "DD":
                        return True
        return False

    def get_legal_moves(self):
        moves = []
        for room in self.rooms:
            if self.rooms[room] == "..":
                continue
            contents = self.rooms[room]
            if contents[0] == contents[1]:
                if DEST_ROOMS[contents[0]] == room:
                    continue
            if contents[0] == ".":
                if DEST_ROOMS[contents[1]] == room:
                    continue
            if self.rooms[room][0] == ".":
                for k in LEGAL_HALL_INDICIES:
                    anthro = self.rooms[room][1]
                    if self.is_legal_hall_move(room, k):
                        moves.append([anthro, room, k, (np.abs(k - room) + 2) * COSTS[anthro]])
            else:
                for k in LEGAL_HALL_INDICIES:
                    anthro = self.rooms[room][0]
                    if self.is_legal_hall_move(room, k):
                        moves.append([anthro, room, k, (np.abs(k - room) + 1) * COSTS[anthro]])
        for k in range(len(self.hall)):
            anthro = self.hall[k]
            if anthro != '.':
                if self.is_legal_room_move(k, DEST_ROOMS[anthro]):
                    room = DEST_ROOMS[anthro]
                    if self.rooms[DEST_ROOMS[anthro]] == "..":
                        moves.append([anthro, k, room, (np.abs(k - room) + 2) * COSTS[anthro]])
                    elif self.rooms[DEST_ROOMS[anthro]] == "." + anthro:
                        moves.append([anthro, k, room, (np.abs(k - room) + 1) * COSTS[anthro]])
        return moves

    def move(self, anthro, start_index, end_index, cost):
        self.incurred_cost += cost
        if start_index in self.rooms:
            if self.rooms[start_index][0] == ".":
                self.rooms[start_index] = ".."
            else:
                self.rooms[start_index] = "." + self.rooms[start_index][1]
            self.hall[end_index] = anthro
        else:
            if self.rooms[end_index][1] == ".":
                self.rooms[end_index] = "." + anthro
            else:
                self.rooms[end_index] = anthro + anthro
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
