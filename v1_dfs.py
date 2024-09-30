from time import sleep
from pprint import pprint  # Added to use pprint for pretty printing


def read_file(path):
    with open(path, "r") as f:
        lines = f.readlines()
    f.close()
    amount = lines[0]
    periods = [period for period in lines[1:]]

    return periods


class Maze:
    def __init__(self, path) -> None:
        self.periods = {i: int(period) for i, period in enumerate(read_file(path))}
        self.minute = 0
        self.status = [False for _ in self.periods]
        self.persons = [False for _ in self.periods]

    def update(self):
        """
        call every move to simulate the movements of the Maze
        """
        self.minute += 1
        change = False  # if nothing has changed dont bother calculating possible moves
        for i in self.periods.keys():
            period = self.periods[i]
            if (self.minute % period) == 0:
                self.status[i] = not self.status[i]
                change = True
        return change

    def move(self):
        iteration = 0
        while (not self.persons[-1]) and iteration < 15:
            iteration += 1
            sleep(0.5)
            if self.update():
                for position, _ in enumerate(self.persons):
                    if self.dead(position):
                        self.persons[position] = False
                        continue
                    if self.can_move("left", position):
                        self.persons[position - 1] = True
                    if self.can_move("right", position):
                        self.persons[position + 1] = True
                if self.status[0]:
                    self.persons[0] = True

    def dead(self, position):
        return not self.status[position]  # True = not dead -> return False

    def can_move(self, direction, position):
        match (direction):
            case "left":
                direction = -1
            case "right":
                direction = 1
            case _:
                raise ValueError

        try:
            self.status[position + direction]
        except IndexError:
            return False
        return not self.status[position + direction]

    def solve(self):
        self.move()


maze = Maze("grabmal0.txt").solve()
