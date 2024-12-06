from typing import Tuple

with open("Day_6/input.txt", "r") as f:
    data = f.readlines()
map = [line.strip("\n") for line in data]


def find_current_position(map: list[str]) -> Tuple[int, int]:
    for i in range(len(map)):
        for j in range(len(map[i])):
            if map[i][j] == "^":
                return (i, j)


def take_step(current_position: Tuple[int, int], direction: str) -> Tuple[int, int]:
    if direction == "^":
        new_position = (current_position[0] - 1, current_position[1])
    elif direction == ">":
        new_position = (current_position[0], current_position[1] + 1)
    elif direction == "<":
        new_position = (current_position[0], current_position[1] - 1)
    elif direction == "v":
        new_position = (current_position[0] + 1, current_position[1])

    return new_position


def exit(current_pos: Tuple[int, int], direction: str) -> bool:
    if direction == "^" and current_pos[0] == 0:
        return True
    elif direction == ">" and current_pos[1] == len(map[current_pos[0]]) - 1:
        return True
    elif direction == "<" and current_pos[1] == 0:
        return True
    elif direction == "v" and current_pos[0] == len(map) - 1:
        return True
    else:
        return False


def turn(
    current_pos: Tuple[int, int],
    obstacles: list[Tuple[int, int]],
    direction: str,
) -> str:
    if direction == "^" and (current_pos[0] - 1, current_pos[1]) in obstacles:
        return ">"
    elif direction == ">" and (current_pos[0], current_pos[1] + 1) in obstacles:
        return "v"
    elif direction == "<" and (current_pos[0], current_pos[1] - 1) in obstacles:
        return "^"
    elif direction == "v" and (current_pos[0] + 1, current_pos[1]) in obstacles:
        return "<"
    else:
        return direction


def map_obstacles(map: list[str]) -> list[Tuple[int, int]]:
    obstacles = set()
    for i in range(len(map)):
        for j in range(len(map[i])):
            if map[i][j] == "#":
                obstacles.add((i, j))
    return obstacles


positions = []
direction = "^"
current_position = find_current_position(map)
obstacles = map_obstacles(map)
loop_counter = 0


def find_path(
    current_position: Tuple[int, int],
    direction: (str),
    obstacles: list[Tuple[int, int]],
) -> int:
    positions = []
    positions.append(current_position)
    while not exit(current_position, direction):
        direction = turn(current_position, obstacles, direction)
        current_position = take_step(current_position, direction)
        positions.append(current_position)

    return set(positions)


print(len(find_path(find_current_position(map), direction, map_obstacles(map))))

######################################## PART 2

initial_position = find_current_position(map)
initial_direction = "^"
initial_state = (initial_position[0], initial_position[1], initial_direction)
guard_positions = find_path(find_current_position(map), direction, map_obstacles(map))
initial_obstacles = map_obstacles(map)
loop_counter = 0


def move(state, obstacles):
    new_position = take_step((state[0], state[1]), state[2])
    if (new_position[0], new_position[1]) not in obstacles:
        return (new_position[0], new_position[1], state[2])
    else:
        new_direction = turn((state[0], state[1]), obstacles, state[2])
        return (state[0], state[1], new_direction)


def add_obstacle(pos, obstacles):
    new_obs = obstacles.copy()
    new_obs.add(pos)
    return new_obs


def detect_loop(state, obstacles):
    seen = set()
    seen.add(initial_state)

    while True:
        state = move(state, obstacles)
        if state in seen:
            return True
        seen.add(state)

        if state[2] == "^" and state[0] == 0:
            break
        elif state[2] == ">" and state[1] == len(map[state[0]]) - 1:
            break
        elif state[2] == "<" and state[1] == 0:
            break
        elif state[2] == "v" and state[0] == len(map) - 1:
            break

    return False


for i in range(len(map)):
    for j in range(len(map[i])):
        if (i, j) not in initial_obstacles and (i, j) != initial_position:
            obstacles = add_obstacle((i, j), initial_obstacles)
            if detect_loop(initial_state, obstacles):
                loop_counter += 1
print(loop_counter)
