from dataclasses import dataclass
from functools import reduce
from heapq import nlargest

@dataclass
class Monkey:
    items: list[int]
    operation: str
    operation_arg: int | str
    test_arg: int
    true: int
    false: int
    inspections: int = 0

def parse_input(debug) -> list[int]:
    with open(f"input/{'test' if debug else '11'}.txt", 'r') as f:
        raw = f.read().strip().split('\n\n')
    monkeys = []
    for monkey_data in raw:
        data = monkey_data.split('\n')
        items_line = data[1].strip()
        items = list(map(int, items_line[len('Starting items: '):].split(', ')))
        operation_line = data[2].strip()
        operation = operation_line[len('Operation: new = old ')]
        operation_arg = operation_line[len('Operation: new = old _ '):]
        test_line = data[3].strip()
        test_arg = int(test_line[len('Test: divisible by'):])
        true_line = data[4].strip()
        true = int(true_line[len('If true: throw to monkey'):])
        false_line = data[5].strip()
        false = int(false_line[len('If false: throw to monkey '):])
        monkeys.append(Monkey(items, operation, operation_arg, test_arg, true, false))
    return monkeys

def process(debug: bool, rounds: int, reduction=None, modulo=None):
    monkeys: list[Monkey] = parse_input(debug)
    for round in range(rounds):
        for monkey in monkeys:
            num_items = len(monkey.items)
            for _ in range(num_items):
                item = monkey.items.pop(0)
                monkey.inspections += 1
                if monkey.operation == '*':
                    if monkey.operation_arg == 'old':
                        item **= 2
                    else:
                        item = item * int(monkey.operation_arg)
                else:
                    if monkey.operation_arg == 'old':
                        item *= 2
                    else:
                        item = item + int(monkey.operation_arg)
                if reduction:
                    item //= reduction
                elif modulo:
                    item %= modulo
                test = item % monkey.test_arg == 0
                dest = monkey.true if test else monkey.false
                monkeys[dest].items.append(item)
    inspections = list(map(lambda monkey: monkey.inspections, monkeys))
    largest = nlargest(2, inspections)
    return largest[0] * largest[1]

def compute_divisor_product(debug: bool):
    monkeys: list[Monkey] = parse_input(debug)
    test_args = map(lambda x: x.test_arg, monkeys)
    return reduce(lambda x, y: x * y, test_args)

def part1(debug=False):
    return process(debug, 20, reduction=3)

def part2(debug=False):
    return process(debug, 10000, modulo=compute_divisor_product(debug))

print(part1())
print(part2())
