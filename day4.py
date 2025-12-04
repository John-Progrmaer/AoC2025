class Unpacker:
    def __init__(self, source):
        self.data = []
        self.source = source
        self.sum = 0
        self.limit = 4
        self.bound = 0

    def download(self):
        with open(self.source, "r") as file:
            for line in file:
                line = line.strip()
                subsequence = []
                for char in line:
                    subsequence.append(char)
                self.data.append(subsequence)   
        self.bound = len(self.data) - 1
        print(f"sequence created with {self.bound} rows and columns...")
        self.parse()

    def parse(self):
        i = 0
        for row in self.data:
            j = 0
            for item in row:
                print(f"\nTesting for data surrounding {self.data[i][j]} at row {i}, column {j}...")
                if self.data[i][j] == "@":
                    self.sum += self.test(i, j)
                else:
                    print(f"point {self.data[i][j]} != @, disregard...")
                j += 1
            i += 1
        print(self.sum)

    def test(self, row, column):
        tracker = 0
        for x in range((row - 1), (row + 2)):
            if x < 0 or x > self.bound:
                print(f"\trow {x} outside of bounds...")
                continue
            for y in range((column - 1), (column + 2)):
                if y < 0 or y > self.bound:
                    print(f"\tcolumn {y} outside of bounds...")
                    continue
                if x == row and y == column:
                    continue
                print(f"\trow {x}, column {y}: {self.data[x][y]}")
                if self.data[x][y] == "@":
                    tracker += 1
                    print(f"\t\t@ detected, tracker now at {tracker}")
                else:
                    print(f"\t\tclear!")
                if tracker == self.limit:
                    print("\ttoo many rolls, throw it out!")
                    return 0
        return 1

if __name__ == "__main__":
    tool = Unpacker("input.txt")
    tool.download()