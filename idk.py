# uppgift14.py

FRUITS = ['banana', 'apple', 'orange']
CARS = ['volvo', 'ford', 'tesla']
COLORS = ['pink', 'blue', 'red']

def run():
    basket = [
        'volvo', 'is', 'an', 'orange', 'apple', 'red'
    ]
    cars = []
    fruits = []
    colors = []
    rest = []
    for item in basket:
        if item in CARS:
            cars.append(item)
        elif item in FRUITS:
            fruits.append(item)
        elif item in COLORS:
            colors.append(item)
        else:
            rest.append(item)
    write_things(sorted(cars), 'Cars')
    write_things(sorted(fruits), 'Fruits')
    write_things(sorted(colors), 'Colors')
    write_things(sorted(rest), 'Misc')


def write_things(items, kind):
    print(f"{kind.upper()} {len(items)}")
    for item in items:
        print(f" {item}")


if __name__ == '__main__':
    run()



