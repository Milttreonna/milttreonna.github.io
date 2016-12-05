import random


def show_grid(grid):
    """ grid -> str
    """
    return "\n".join(map(show_row, grid))


def show_row(row):
    """ [cell] -> str
    """
    return "|".join(map(show_cell, row))


def show_cell(cell):
    """ cell -> str
    """
    if cell is None:
        return ' '
    elif cell == "M":
        return '*'
    else:
        return str(cell)


def in_bounds(r, c, grid):
    """ (int, int, list) -> bool
    """
    return r >= 0 and r < len(grid) and c >= 0 and c < len(grid[r])


def is_mine(r, c, grid):
    """ (int, int, list) -> bool
    """
    return grid[r][c] == 'M'


def main():

    mine_grid = []
    while len(mine_grid) < 8:
        mine_grid.append([0, 0, 0, 0, 0, 0, 0, 0])

    visible_grid = [[None, None, None, None, None, None, None, None],
                    [None, None, None, None, None, None, None, None],
                    [None, None, None, None, None, None, None, None],
                    [None, None, None, None, None, None, None, None],
                    [None, None, None, None, None, None, None, None],
                    [None, None, None, None, None, None, None, None],
                    [None, None, None, None, None, None, None, None],
                    [None, None, None, None, None, None, None, None]]

    mines = 10
    mine_locations = set()

    while len(mine_locations) < mines:
        row = random.randint(0, 7)
        col = random.randint(0, 7)
        mine_locations.add((row, col))
        mine_grid[row][col] = "M"
    for row in range(len(mine_grid)):
        for col in range(len(mine_grid[row])):
            if mine_grid[row][col] == "M":
                continue
            count = 0
            for i in range(-1, 2):
                for j in range(-1, 2):
                    if in_bounds(row + i, col + j, mine_grid) and is_mine(
                            row + i, col + j, mine_grid):
                        count += 1

            mine_grid[row][col] = count

    while True:
        choice = input(
            'Pick two numbers between 1 and 8. (row, column)\n').strip()
        numbers = choice.split(',')
        row = int(numbers[0].strip()) - 1
        col = int(numbers[1].strip()) - 1

        if row > 7 or row < 0 or col > 7 or col < 0:
            print('Invalid Input')
            continue
        elif mine_grid[row][col] == "M":
            visible_grid[row][col] = mine_grid[row][col]
            print("You got hit!")
            for col in range(len(mine_grid)):
                for row in range(len(mine_grid[col])):
                    if mine_grid[col][row] == "M":
                        visible_grid[col][row] = "M"
            break
        else:
            visible_grid[row][col] = mine_grid[row][col]

        print(show_grid(visible_grid))
    print(show_grid(visible_grid))


if __name__ == '__main__':
    main()
