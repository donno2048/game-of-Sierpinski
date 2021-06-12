from typing import List
from itertools import chain
from matplotlib.pyplot import subplots, show
from matplotlib.animation import FuncAnimation
def new_gen(size: int) -> List[bool]:
    global state
    ret = []
    for i in range(size ** 2):
        neighbours = state[i - 1] + state[(i + 1) % (size ** 2)] + state[(i - size - 1) % (size ** 2)] + state[(i - size) % (size ** 2)] + state[(i - size + 1) % (size ** 2)] + state[(i + size - 1) % (size ** 2)] + state[(i + size) % (size ** 2)] + state[(i + size + 1) % (size ** 2)]
        '''
        Using the:
        neighbours = grid[j][i - 1] + grid[j][(i + 1) % size] + grid[j - 1][i - 1] + grid[j - 1][i] + grid[j - 1][(i + 1) % size] + grid[(j + 1) % size][i - 1] + grid[(j + 1) % size][i] + grid[(j + 1) % size][(i + 1) % size]
        method or something like that makes no sense
        '''
        if (state[i] and neighbours in [2, 3]) or (not state[i] and neighbours == 3): ret += [True]
        # If you comment the next line it is the standard game of life
        elif state[(i + size) % (size ** 2)]: ret += [True]
        else: ret += [False]
    return ret
def update(frame, img, size):
    global state
    state = new_gen(size)
    img.set_data([state[i: i + size] for i in range(0, size ** 2, size)])
    return img,
def main():
    global state
    # Use an initial grid of just a square at the bottom
    grid = [[0] * 500] * 498 + [[0] * 249 + [1, 1] + [0] * 249] * 2
    state = list(chain(*grid))
    fig, ax = subplots()
    img = ax.imshow(grid, interpolation='nearest')
    _ = FuncAnimation(fig, update, fargs=(img, round(len(state) ** 0.5), ))
    show()

main()