class Menu:
    def __init__(self, source, mode):
        self.mode = mode        # Part 1 or part 2
        self.catalogues = []    # track our fresh indexes
        self.data = []          # track our current inventory
        self.sum = 0            # how many fresh items do we have
        self.source = source    # the code explains the code
        self.download()         # me downloading the enemy midlaner's entire playbook

    def download(self):
        """Extract specified source file"""
        with open(self.source, "r") as file:
            for line in file:
                line = line.strip()     # so scandalous
                if "-" in line:         # handles indexes
                    pos = line.find("-")
                    start = ''
                    end = ''
                    for i in range(0, pos):
                        start += line[i]
                    for j in range((pos + 1), len(line)):
                        end += line[j]
                    self.catalogues.append([int(start), int(end)])
                elif self.mode == 1:    # skips unnecessary work for p2
                    break
                elif len(line) == 0:    # won't be needing the gap
                    continue
                else:                   # handles individual items
                    subsequence = ''
                    for char in line:
                        subsequence += char
                    self.data.append(int(subsequence))
        self.extract()
        print(f"\ntotal fresh ingredients: {self.sum}\n")

    def extract(self):
        if self.mode == 1:
            self.overlap()
            print(self.catalogues)
            for i in range(0, len(self.catalogues)):
                self.sum += self.catalogues[i][1] - self.catalogues[i][0] + 1
            return None
        for i in range(0, len(self.data)):
            flag = 0
            if flag == 1:
                continue
            for j in range(0, len(self.catalogues)):
                if self.data[i] in range(self.catalogues[j][0], self.catalogues[j][1] + 1):
                    self.sum += 1
                    flag = 1
                    break

    def overlap(self):
        for i in range(0, len(self.catalogues)):
            print(f"\ntesting overlap for catalogue {i}:\n  {self.catalogues[i]}")
            for j in range(0, len(self.catalogues)):
                if i == j:      # don't test a catalogue against itself!
                    continue
                print(f"\ttesting catalogue {i} against catalogue {j}:\n\t  {self.catalogues[j]}")
                start = self.catalogues[i][0]
                end = self.catalogues[i][1]
                bound1 = self.catalogues[j][0]
                bound2 = self.catalogues[j][1] + 1
                if start in range(bound1, bound2):
                    print(f"\t...start of catalogue {i} ({start}) overlaps catalogue {j}\n\t  {self.catalogues[j]}")
                    print("\t  ...adjusting up...")
                    self.catalogues[i][0] += bound2 - start
                    print(f"\tstart of catalogue {i} has been adjusted from {start} to {self.catalogues[i][0]}")
                    print(f"\t  proof: {self.catalogues[i]}")
                if end in range(bound1, bound2):
                    print(f"\t...end of catalogue {i} ({end}) overlaps catalogue {j}\n\t  {self.catalogues[j]}")
                    print("\t ...adjusting down...")
                    self.catalogues[i][1] -= end - bound1 + 1
                    print(f"\tend of catalogue {i} has been adjusted from {end} to {self.catalogues[i][1]}")
                    print(f"\t  proof: {self.catalogues[i]}")

answer = Menu("sample.txt", 1)