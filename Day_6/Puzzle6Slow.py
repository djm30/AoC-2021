test_data = "testinput.txt"
real_data = "input.txt"


file = real_data

class Lanternfish():
    def __init__(self, timer=8, new=True) -> None:
        self.timer = timer
        self.new = new

    def __eq__(self, __o: object) -> bool:
        return self.timer == __o

    def __sub__(self, num) -> int:
        self.timer -= num
        return self.timer

    def reset_timer(self) -> None:
        self.timer = 6

    def __bool__(self) -> bool:
        return self.new

    def __repr__(self) -> str:
        return f"Timer: {self.timer}, New: {self.new}"

    def set_new(self, new):
        self.new = new



num_days = 80
data = [Lanternfish(timer=lantern, new=False) for lantern in list(map(int, open(file, mode="r").read().replace("\n", "").split(sep=",")))]


##Inefficient but clean part one
for i in range(num_days):
    print(f"Day {i}")
    for lantern in data:
        if not lantern:
            if lantern - 1 == -1:
                lantern.reset_timer()
                data.append(Lanternfish())
            continue
        else:
            lantern.set_new(new=False)
    print(len(data))

print(len(data))






