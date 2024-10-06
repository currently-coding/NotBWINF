from time import sleep
from pprint import pprint  # Added to use pprint for pretty printing


def read_file(path):
    with open(path, "r") as f:
        lines = f.readlines()
    f.close()
    periods = [int(period.strip()) for period in lines[1:]]

    print(periods)
    return periods


class Maze:
    def __init__(self, path) -> None:
        self.periods = {i: int(period) for i, period in enumerate(read_file(path))}
        self.minute = 0
        self.status = [False for _ in self.periods]
        self.persons = [False for _ in self.periods]
        self.path = []

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
        while not self.persons[-1]:
            print("Minute: ", iteration)
            self.path.append({})
            if self.update():
                print("UPDATED")
                pprint(self.status)
                print("Persons before moving:")
                pprint(self.persons)
                # self.path[iteration] = {}
                for position, _ in enumerate(self.persons):
                    if not self.persons[position]:
                        continue
                    if self.dead(position):
                        self.persons[position] = False
                        continue
                    if self.can_move(-1, position):

                        self.path[iteration][position] = position - 1
                        print("moving left")
                        self.persons[position - 1] = True
                    if self.can_move(1, position):

                        self.path[iteration][position] = position + 1

                        print("moving right")
                        self.persons[position + 1] = True
                if self.status[0]:
                    print("Spawing new person at the start")
                    self.persons[0] = True
                    self.path[iteration][-1] = 0
                    print("Persons after moving: ")
                    pprint(self.persons)

            iteration += 1
            pprint(self.path)
        print(f"Person reached the end after {iteration} Minutes.")

    def dead(self, position):
        return not self.status[position]  # True = not dead -> return False

    def can_move(self, direction, position):
        if not self.status:
            return False
        length = len(self.status)
        if position + direction >= length:
            return False
        if position + direction < 1:
            return False
        if not self.status[position + direction]:
            return False
        return True

    def calc_path(self):
        solution = []
        pos_to_find = len(self.status) - 1
        print("TO FIND: ", pos_to_find)
        for minute in range(len(self.path) - 1, 0, -1):
            index = len(self.path) - minute - 1
            print(index)
            print("Checking minute: ", minute)
            for key in self.path[minute].keys():
                value = self.path[minute][key]

                print("Checking move: ", key, ": ", value)
                if value == pos_to_find:
                    solution.append({index: value})
                    print(solution)
                    print(minute)
                    pos_to_find = key
                    print("added to path")
        print(solution)

    def output(self):

        pprint(self.status)
        pprint(self.persons)
        self.calc_path()

    def solve(self):
        self.move()
        self.output()


maze = Maze("grabmal0.txt").solve()
