from copy import deepcopy

class Cephalopoder:
    def __init__(self, source, mode=1):
        self.source = source
        self.mode = mode    # 1 for part 1, 2 for part 2
        self.data = []
        self.active = []
        self.sum = 0
        self.pull_data()
        self.reorganize()
        print(self.sum)

    def pull_data(self):
        with open(self.source, "r") as file:
            if self.mode == 1:
                for line in file:
                    print(line)
                    print(line.strip().split())
                    self.data.append(line.strip().split())
                return None
            i = 0
            for line in file:
                print(f"\nline {i}: {line.strip()}")
                j = 0
                for char in line:
                    if char == "\n":
                        continue
                    print(f"  char {j}: ({char})")
                    j += 1
                items = line.strip().split()
                try:
                    ignore = int(items[0])
                except ValueError:
                    print(f"items:\n  {items}\n  length: {len(items)}\n")
                print(f"number of characters ({j}) compared to number of entries ({len(items)})")
                i += 1

    def reorganize(self):
        if self.mode == 1:
            for i in range(0, len(self.data[0])):
                for j in range(0, len(self.data)):
                    try:
                        self.active.append(int(self.data[j][i]))
                    except ValueError:
                        self.active.append(self.data[j][i])
                self.math_time()
                self.active.clear()
            return None
        for i in range(0, len(self.data[0])):
            for j in range(0, len(self.data)):
                self.active.append(self.data[j][i])
            print(f"\nactive line: {self.active}")
            temp = deepcopy(self.active)
            temp.sort(key=len, reverse=True)
            print(f"  ...sorted by length: {temp}\n  (active line remains: {self.active})")
            self.nonsense(temp)
            self.math_time()
            self.active.clear()

    def math_time(self):
        temp = 0
        for i in range(0, len(self.active)):
            if not isinstance(self.active[i], int):
                self.sum += temp
                break
            if i == 0:
                temp = self.active[i]
                continue
            match self.active[-1]:
                case "+":
                    temp += self.active[i]
                case "*":
                    temp *= self.active[i]

    def nonsense(self, list):
        temp = ""
        for i in range(0, len(list)):
            if i == 0:
                sample = list[i]
            print(f"testing list {list} at instance {i}; {list[i]}")

            test = len(list[i])
            print(test)

answer = Cephalopoder("sample.txt", 2)
