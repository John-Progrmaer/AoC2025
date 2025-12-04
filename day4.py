class Unpacker:
    def __init__(self, source, mode=0):
        self.data = []      # imported dataset
        self.dupe = []      # independent clone for layering
        self.source = source
        self.sum = 0        # final answer
        self.limit = 4      # value defined by problem
        self.bound = 0
        self.mode = mode    # part_1 == 0, part_2 == 1
        self.flag = 0       # set to 1 when recursive loop is done

    def download(self):
        """Extract specified source file"""
        with open(self.source, "r") as file:
            for line in file:
                line = line.strip()
                subsequence = []
                for char in line:
                    subsequence.append(char)
                self.data.append(subsequence)
        self.bound = len(self.data) - 1
        while self.flag == 0:
            self.parse(self.mode)
        print(f"{self.sum}\n")

    def parse(self, loop):
        """Iterate through each item of the dataset, recursion optional."""
        if loop == 1:
            self.dupe = deepcopy(self.data)
            temp = self.sum
        i = 0
        for series in self.data:
            j = 0
            for item in series:
                if item == "@":
                    check = self.test(i, j)
                    if check == 1 and loop == 1:
                        self.dupe[i][j] = "."
                    self.sum += check
                j += 1
            i += 1
        if loop == 1:
            self.data = deepcopy(self.dupe)
            if temp == self.sum:
                self.flag = 1
            

    def test(self, row, column):
        """For a given position, test surroundings"""
        tracker = 0
        for x in range((row - 1), (row + 2)):
            if x < 0 or x > self.bound:
                continue
            for y in range((column - 1), (column + 2)):
                if y < 0 or y > self.bound:
                    continue
                if x == row and y == column:
                    continue
                if self.data[x][y] == "@":
                    tracker += 1
                if tracker == self.limit:
                    return 0
        return 1

if __name__ == "__main__":
    from copy import deepcopy
    tool = Unpacker("input.txt", 1)
    tool.download()
