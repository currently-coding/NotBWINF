from time import sleep
from pprint import pprint  # Added to use pprint for pretty printing


def read_file(path):
    with open(path, "r") as f:
        lines = f.readlines()
    # Removed f.close() since 'with' statement handles it
    amount = int(lines[0])  # Converted amount to an integer
    periods = [
        int(period.strip()) for period in lines[1:]
    ]  # Convert periods to integers

    # Debug: File reading information
    print(f"Read file '{path}':")
    print(f"Total periods: {amount}")
    print("Periods:", end=" ")
    pprint(periods)  # Pretty print the periods

    return periods


class Maze:
    def __init__(self, path) -> None:
        self.periods = {i: int(period) for i, period in enumerate(read_file(path))}
        self.minute = 0
        self.status = [False for _ in self.periods]
        self.persons = [False for _ in self.periods]

        # Debug: Initial values
        print("\nInitial Values:")
        print("Status:", end=" ")
        pprint(self.status)  # Pretty print initial status
        print("Persons:", end=" ")
        pprint(self.persons)  # Pretty print initial persons
        print("Periods:", end=" ")
        pprint(self.periods)  # Pretty print periods mapping

    def update(self):
        """
        Call every move to simulate the movements of the Maze.
        """
        self.minute += 1
        change = (
            False  # If nothing has changed, don't bother calculating possible moves
        )

        # Debug: Update status
        print(f"\nUpdating maze status for minute: {self.minute}")
        for i in self.periods.keys():
            period = self.periods[i]
            if (self.minute % period) == 0:
                self.status[i] = not self.status[i]
                change = True
                print(f"Period {i} toggled to {'ON' if self.status[i] else 'OFF'}")

        print("\nCurrent Maze Status:")
        pprint(self.status)  # Pretty print the maze status
        print("Maze did", "not " if not change else "", "update.")
        return change

    def move(self):
        iteration = 0
        while (not self.persons[-1]) and iteration < 15:
            print("\n" + " - " * 30)  # Separator for clarity
            iteration += 1
            sleep(0.5)

            # Debug: Iteration and persons status
            print(f"Iteration: {iteration}")
            print("Persons status:", end=" ")
            pprint(self.persons)  # Pretty print persons status

            if self.update():
                for position, _ in enumerate(self.persons):
                    if self.dead(position):
                        self.persons[position] = False
                        print(f"Person at position {position} is dead and removed.")
                        continue
                    if self.can_move("left", position):
                        self.persons[position - 1] = True
                        print(
                            f"Person moved left from position {position} to {position - 1}."
                        )
                    if self.can_move("right", position):
                        self.persons[position + 1] = True
                        print(
                            f"Person moved right from position {position} to {position + 1}."
                        )
                if self.status[0]:
                    self.persons[0] = (
                        True  # Assuming we want to activate the first person
                    )

    def dead(self, position):
        return not self.status[position]  # True = not dead -> return False

    def can_move(self, direction, position):
        match (direction):
            case "left":
                direction = -1
            case "right":
                direction = 1
            case _:
                raise ValueError("Invalid direction")  # Added error message for clarity

        try:
            return not self.status[position + direction]
        except IndexError:
            return False

    def solve(self):
        self.move()
        print("\nFinished the maze")  # Debug: Finished the maze


maze = Maze("grabmal0.txt").solve()
