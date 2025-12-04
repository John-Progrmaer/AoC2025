class Voltage:
    def __init__(self):
        """Track intended battery length, Sum total."""
        self.battery_length = 12
        self.joltage = 0

    def identify(self, sequence, position=0, remaining=0):
        wiggle_room = len(sequence) - position - remaining
        for option in reversed(range(10)):
            temp = sequence.find(str(option), position, position + wiggle_room + 1)
            if temp == -1:
                continue
            val1 = str(sequence[temp])
            remaining -= 1
            if remaining == 0:
                return val1
            val2 = self.identify(sequence, temp + 1, remaining)
            break
        return val1 + val2

tool = Voltage()

with open("input.txt", "r") as file:
    for line in file:
        tool.joltage += int(tool.identify(line.strip(), 0, tool.battery_length))

    print(f"{tool.joltage}\n")
