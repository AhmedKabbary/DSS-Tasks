class AprioriAlgorithm:

    def __init__(self, items: list, min_supply: int) -> None:
        self.items = items
        self.min_supply = min_supply
        self.answer = []

    def solve(self) -> list:
        s = set()
        for key in self.items:
            key: str
            for element in key.split(','):
                s.add(element)

        self.recurse(s)
        return self.answer

    def recurse(self, keys: list):
        # calculate frequency
        map = self.calc_freq(keys)

        if len(keys) <= 1:
            return

        # eliminate according to minimum supply
        for key in map.copy():
            if map[key] < self.min_supply:
                map.pop(key)

        # record scan answers
        self.answer.append(map)

        # combining all possibilities
        new_keys = set()
        for i1, e1 in enumerate(map.keys()):
            for i2, e2 in enumerate(map.keys()):
                if i2 <= i1 and len(map.keys()) > 1:
                    continue
                new_keys.add(self.combine(e1, e2))

        self.recurse(new_keys)

    def calc_freq(self, keys: list) -> dict:
        map = {}
        for key in keys:
            for item in self.items:
                if self.contains(item, key):
                    if key in map:
                        map[key] += 1
                    else:
                        map[key] = 1

        return map

    def combine(self, e1: str, e2: str) -> str:
        s = set((e1 + ',' + e2).split(','))
        return ','.join(sorted(s))

    def contains(self, string: str, sub_string: str) -> bool:
        parent_list = string.split(',')
        child_list = sub_string.split(',')

        for e in child_list:
            if e not in parent_list:
                return False

        return True
