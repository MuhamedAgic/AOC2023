import pandas as pd
from scipy.spatial.distance import cityblock
from scipy.spatial.distance import cdist
import numpy as np

def expand_cosmos(cosmos_df):
    print(cosmos_df)

    # Rijen en kolommen met alleen puntjes
    dots_rows = (cosmos_df == ".").all(axis=1) # boolean array, voldoet row
    dots_columns = (cosmos_df == ".").all(axis=0)

    # voeg puntjes toe rows
    for idx, row in enumerate(dots_rows):
        if row:
            cosmos_df.loc[idx+0.5] = pd.Series(["."] * cosmos_df.shape[1])
            cosmos_df = cosmos_df.sort_index().reset_index(drop=True)

    # Add a column of dots
    move_x = 0
    for idx, col in enumerate(dots_columns):
        if col:
            move_x += 1
            cosmos_df.insert(loc=idx+move_x, column="e" + str(idx), value=".")

    print("\n\n* * * * * * * C O S M I C * * * E X P A N S I O N * * * * * *\n\n")
    print(cosmos_df)
    return cosmos_df

def calc_dist(coord1, coord2):
    return abs(coord2[0] - coord1[0]) + abs(coord2[1] - coord1[1])

def get_distances_from_galaxy_coordinates(galaxy_coordinates):
    print("TOTAAL: ", len(galaxy_coordinates))
    distances_all_galaxies = []
    for idx, coordinate in enumerate(galaxy_coordinates):
        distances_current_galaxy = []
        for idy, other_coordinate in enumerate(galaxy_coordinates):
            if (idx == idy) and (idx > 0) and (idx != len(galaxy_coordinates) - 1): #...
                continue
            distances_current_galaxy.append(calc_dist(coordinate, other_coordinate)) # bij hetzelfde, 0

        distances_current_galaxy = distances_current_galaxy[idx+1:] # je mag steeds eentje minder vanaf het begin tellen
        print(len(distances_current_galaxy))
        distances_all_galaxies.append(distances_current_galaxy)

    #print(f"Einde: {distances_all_galaxies}")
    return sum([sum(distances) for distances in distances_all_galaxies])

def get_galaxy_coordinates(expanded_cosmos):
    row, col = (expanded_cosmos.map(lambda x: str(x).startswith('#'))).values.nonzero()
    coordinates = list(zip(row, col))
    #print(coordinates)
    return coordinates

def day_eleven_part_one(filename):
    with open(filename, 'r') as f:
        lines = f.readlines()

    cosmos_width = len(lines[0]) - 1
    columns = []
    for i in range(cosmos_width):
        columns.append(1)

    cosmos_df = pd.read_fwf(filename, widths=columns, header=None)
    expanded_cosmos_df = expand_cosmos(cosmos_df)
    galaxy_coordinates = get_galaxy_coordinates(expanded_cosmos_df)
    summed_distances = get_distances_from_galaxy_coordinates(galaxy_coordinates)
    return summed_distances


filename = "D:/git/magic/aoc2023/aoc2023/src/eleven/input.txt"
ans1 = day_eleven_part_one(filename)
print(f"Part one {ans1}")

#9301789 te laag
#9317135 fout
#9317146 fout
#9334968 te hoog
#9337771 te hoog

# ans2 = day_eight_part_two(filename)
# print(f"Part two {ans2}")
