def solve(content: str) -> str:
    lines = content.split("\n")
    n = int(lines[0])
    current_line_index = 1
    result = []
    for i in range(n):
        print("\n") 
        values = lines[current_line_index].split(" ")
        x,y,z = int(values[0]), int(values[1]), float(values[2])
        current_line_index += 1
        print(f"x: {x}, y: {y}, z: {z}")
        result.append(aliens_positions(x,y,z,lines[current_line_index:current_line_index + x]))
        current_line_index += x
    return "\n".join(result)

def aliens_positions(x: int, y: int, z: int, lines: list[str]) -> str:

    alien_map = []
    for line in lines:
        alien_map.append(line.split(" "))
    
    ships = {}
    for i in range(x):
        for j in range(y):
            ship = alien_map[i][j]
            if ship >= "A" and ship <= "Z" or ship >= "a" and ship <= "z":
                if ship not in ships.keys():
                    ships[ship] = [i,j,i,j]
                else:
                    x1, y1, x2, y2 = ships[ship][0], ships[ship][1], ships[ship][2], ships[ship][3]
                    ships[ship] = [min(x1,i), min(y1,j), max(x2,i), max(y2,j)]
    
    ships = dict(sorted(ships.items(), key=lambda ship: (calculate_area(ship[1]), ship[0])))

    print(f"total ships found: {len(ships)}")

    result = []
    while len(ships) > 0:
        layer_result = []
        del_list = []

        for ship in ships.items():
            coordinates = ship[1]
            x1, y1, x2, y2 = coordinates[0], coordinates[1], coordinates[2], coordinates[3]
            check = len([alien_map[i][j] for i in range(x1, x2 + 1) for j in range(y1, y2 + 1) if alien_map[i][j] == ship[0] or alien_map[i][j] == " "])
            if check == calculate_area(coordinates):
                layer_result.append(f"{ship[0]}:{calculate_position(ship[1], z)}")
                del_list.append(ship[0])
        
        for ship in del_list:
            coordinates = ships[ship]
            x1, y1, x2, y2 = coordinates[0], coordinates[1], coordinates[2], coordinates[3]
            for i in range(x1, x2 + 1):
                for j in range(y1, y2 + 1):
                    alien_map[i][j] = " "

        ships = {ship: ships[ship] for ship in ships if ship not in del_list}
        result.append(layer_result)
    
    return " ".join([";".join(layer) for layer in result])



def calculate_position(coordinates: list[int], z: float) -> str:
    x1, y1, x2, y2 = coordinates[0], coordinates[1], coordinates[2], coordinates[3]
    x = round(((x1 + x2) / 2 + 0.5) * z, 3)
    y = round(((y1 + y2) / 2 + 0.5) * z, 3)
    return f"{x:.3f},{y:.3f}"
    
def calculate_area(coordinates: list[int]) -> int:
    x1, y1, x2, y2 = coordinates[0], coordinates[1], coordinates[2], coordinates[3]
    return (x2 - x1 + 1) * (y2 - y1 + 1)           