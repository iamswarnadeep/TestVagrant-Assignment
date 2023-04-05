import itertools

class Newspaper:
    def __init__(self, name, price):
        self.name = name
        self.price = price

newspapers = [
    Newspaper("TOI", 26),
    Newspaper("Hindu", 20.5),
    Newspaper("ET", 34),
    Newspaper("BM", 10.5),
    Newspaper("HT", 18)
]

budget = float(input("Enter your budget: "))

result = set()
for i in range(2, len(newspapers)+1):
    for combination in itertools.combinations(newspapers, i):
        total_price = sum(newspaper.price for newspaper in combination)
        if total_price <= budget:
            result.add(frozenset([f'"{newspaper.name}"' for newspaper in combination]))

output = "{" + "}, {".join(", ".join(sorted(r)) for r in result) + "}"
print(output)
