from PIL import Image
import numpy as np
import time
import random
from collections import deque


def dig(r, c):
    pixels[r, c] = 255


maze_width = int(input("Enter a number height for the Width: "))
maze_height = int(input("Enter a number height for the maze: "))
input("Give the start num position for the maze: ")
input("Give the start position for the maze: ")
input("Give the end num position for the maze: ")
input("Give the end position for the maze: ")


width = maze_width * 2 + 1
height = maze_height * 2 + 1

pixels = np.zeros((height, width), dtype=np.uint8)

paths = []
all_positions = maze_width * maze_height

start = time.time()

row = random.randrange(1, height-1, 2)
col = random.randrange(1, width-1, 2)

dig(row, col)
paths.append([row, col, 0])

directions = ['up', 'down', 'left', 'right']

iterations = 0
in_deadend = 0


direction_to_coords = {
    'up': {'y':-2, 'half': 1},
    'down': {'y': 2, 'half': -1},
    'left': { 'x': -2, 'half': 1},
    'right': { 'x': 2, 'half': -1}
}


visited = 1

while visited < all_positions:
    iterations += 1

    if len(directions) == 0:
        in_deadend += 1

        row, col, deadend = random.choice(paths)

        directions = ['up', 'down', 'left', 'right']

    else:
        direction = random.choice(directions)

        direction_action = direction_to_coords[direction]

        if 'y' in direction_action:
            if 0 < row + direction_action['y'] <= height - 2 and pixels[row + direction_action['y'], col] != 255:
                row += direction_action['y']
                dig(row + direction_action['half'], col)
                dig(row, col)
                directions = ['up', 'down', 'left', 'right']
                visited += 1
                paths.append([row, col, 0])
            else:
                directions.remove(direction)
        else:
            if 0 < col + direction_action['x'] <= width - 2 and pixels[row, col + direction_action['x']] != 255:
                col += direction_action['x']
                dig(row, col + direction_action['half'])
                dig(row, col)
                directions = ['up', 'down', 'left', 'right']
                visited += 1
                paths.append([row, col, 0])
            else:
                directions.remove(direction)
    def bfs(self, s, e):
        """BFS algorithm solve the maze"""
        frontier = deque()  # μέτωπο αναζήτησης
        frontier.append(s)
        visited = set()  # κορυφές που έχουν επισκεφτεί
        visited.add(s)
        prev = {s: None}  # για κάθε κορυφή, η προηγούμενη κορυφή
        while frontier:  # όσο το μέτωπο αναζήτησης δεν είναι κενό
            current_node = frontier.popleft()
            for next_node in self.adjacency_map[current_node]:
                if not next_node in visited:
                    frontier.append(next_node)
                    visited.add(next_node)
                    prev[next_node] = current_node

        path = []
        at = e
        while at != None:
            path.append(at)
            at = prev[at]

        path = path[::-1]

        if path[0] == s:
            return path
        return []


    def visualize_maze(self):
        """Visualize maze with matplotlibs cmap"""
        grid = [[1 for _ in range(3 * self._length)] for _ in range(3 * self._height)]

        for point, direction in [
            (self._entrance, self._entrance_direction),
            (self._exit, self._exit_direction),
        ]:
            point_x = ((point - 1) % self._length) * 3 + 1
            point_y = ((point - 1) // self._length) * 3 + 1

            grid[point_y][point_x] = 0
            if direction == "UP":
                grid[point_y - 1][point_x] = 0
            elif direction == "RIGHT":
                grid[point_y][point_x + 1] = 0
            elif direction == "DOWN":
                grid[point_y + 1][point_x] = 0
            elif direction == "LEFT":
                grid[point_y][point_x - 1] = 0

        for e1, e2 in self._adjacency_list:
            if e1 > e2:
                e1, e2 = e2, e1

            point_x = ((e2 - 1) % self._length) * 3 + 1
            point_y = ((e2 - 1) // self._length) * 3 + 1
            grid[point_y][point_x] = 0

            point_x = ((e1 - 1) % self._length) * 3 + 1
            point_y = ((e1 - 1) // self._length) * 3 + 1
            grid[point_y][point_x] = 0

            if (e1 - 1) // self._length == (e2 - 1) // self._length:
                grid[point_y][point_x + 1] = 0
                grid[point_y][point_x + 2] = 0
            else:
                grid[point_y + 1][point_x] = 0
                grid[point_y + 2][point_x] = 0


print('iterations: ', iterations)
print('been in deadend: ', in_deadend )

pixels[0, random.randrange(1, width-1, 2)] = 255
pixels[height-1, random.randrange(1, width-1, 2)] = 255

print("\ncreated in %.30f" % (time.time() - start))

size = int(width * 10), int(height * 10)

img = Image.fromarray(pixels)
img = img.resize(size, Image.NEAREST)
img.save('maze.png')
img.show()
