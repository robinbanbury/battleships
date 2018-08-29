import random
import datetime

# from ship_status import ShipStatus

directions = [[1,0], [-1,0], [0,1], [0,-1]]  # represents up, down, left, right (not in that order!)


# We need to generate an array of ship coordinates, then render them as a grid.
def generate_starting_grid(grid_width=10, grid_height=10):
    ship_sizes = [4, 3, 3, 2, 2, 2, 1, 1, 1, 1]
    all_ship_coordinates = list()

    random.seed(datetime.datetime.now())

    for ship_size in ship_sizes:
        valid_ship_chosen = False
        while not valid_ship_chosen:
            ship_coordinates = list()
            chosen_direction = random.randrange(4)  # for navigating 'directions' array

            for i in range(ship_size):
                if i == 0:
                    x = random.randrange(grid_width)
                    y = random.randrange(grid_height)
                else:
                    x = ship_coordinates[i - 1][0] + directions[chosen_direction][0]
                    y = ship_coordinates[i - 1][1] + directions[chosen_direction][1]
                ship_coordinates.append([x, y])

            if validate_ship_coordinates(ship_coordinates, all_ship_coordinates, grid_width, grid_height):
                print('Valid choice: {}'.format(ship_coordinates))
                all_ship_coordinates.append(ship_coordinates)
                valid_ship_chosen = True
            else:
                # re-select
                print('INVALID CHOICE! {}'.format(ship_coordinates))

    print('---------')
    for ship in all_ship_coordinates:
        print(ship)

    matrix = generate_grid_coordinates_with_statues(all_ship_coordinates, grid_width, grid_height)
    print('---------')
    for row in matrix:
        print(row)


# Check that a given ship does not excede the boundaries of the grid, and do not use any coordinates already in use
def validate_ship_coordinates(ship_coordinates, existing_ships, grid_width=10, grid_height=10):
    for coordinate in ship_coordinates:
        if coordinate[0] >= grid_width or coordinate[0] < 0 or coordinate[1] >= grid_height or coordinate[1] < 0:
            return False
        for existing_ship in existing_ships:
            for existing_coordinate in existing_ship:
                if coordinate[0] == existing_coordinate[0] and coordinate[1] == existing_coordinate[1]:
                    return False
    return True


def generate_grid_coordinates_with_statues(all_ship_coordinates, grid_width=10, grid_height=10):
    grid_coordinates = list()
    for x in range(grid_width):
        row_coordinates = list()
        for y in range(grid_height):
            if coordinate_is_in_ships_coordinates(x, y, all_ship_coordinates):
                row_coordinates.append([x, y, 1])  # ShipStatus.SHIP
            else:
                row_coordinates.append([x, y, 0])  # ShipStatus.NO_SHIP

        grid_coordinates.append(row_coordinates)

    return grid_coordinates


def coordinate_is_in_ships_coordinates(x_coord, y_coord, all_ship_coordinates):
    for ship_coordinates in all_ship_coordinates:
        for coordinate in ship_coordinates:
            if x_coord == coordinate[0] and y_coord == coordinate[1]:
                return True
    return False

generate_starting_grid()
