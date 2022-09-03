import itertools
import random
import time

def id_dfs(puzzle, goal, get_moves):
    def idfs(path, depth):
        # unable to search when depth is 0
        if depth == 0:
            return
        # check if goal has been reached
        if path[-1] == goal:
            return path
        # iterate through possible moves
        for move in get_moves(path[-1]):
            # run this function on unvisited nodes, decrementing depth
            if move not in path:
                next_path = idfs(path + [move], depth - 1)
                if next_path:
                    return next_path
    # runs dfs up to a limit of depth
    # depth increases until goal is found
    for depth in itertools.count():
        path = idfs([puzzle], depth)
        if path:
            return path
            
def num_matrix(rows, cols, steps=25):
    # fill default puzzle
    nums = list(range(1, rows * cols)) + [0]
    goal = [ nums[i:i+rows] for i in range(0, len(nums), rows) ]

    get_moves = num_moves(rows, cols)
    puzzle = goal
    # shuffle puzzle
    for steps in range(steps):
        puzzle = random.choice(get_moves(puzzle))

    return puzzle, goal
    
def num_moves(rows, cols):
    def get_moves(subject):
        moves = []

        zrow, zcol = next((r, c)
            for r, l in enumerate(subject)
                for c, v in enumerate(l) if v == 0)

        def swap(row, col):
            import copy
            s = copy.deepcopy(subject)
            s[zrow][zcol], s[row][col] = s[row][col], s[zrow][zcol]
            return s

        # north
        if zrow > 0:
            moves.append(swap(zrow - 1, zcol))
        # east
        if zcol < cols - 1:
            moves.append(swap(zrow, zcol + 1))
        # south
        if zrow < rows - 1:
            moves.append(swap(zrow + 1, zcol))
        # west
        if zcol > 0:
            moves.append(swap(zrow, zcol - 1))

        return moves
    return get_moves
    

if __name__ == '__main__':
    reps = 10
    # Iterative depth first search
    total_time = 0
    for i in range(reps):
        puzzle, goal = num_matrix(3, 3)
        t0 = time.time()
        solution = id_dfs(puzzle, goal, num_moves(3, 3))
        print(solution)
        t1 = time.time()
        total_time += t1 - t0
    total_time /= reps
    print('Puzzle solved using iterative depth first search in', total_time, 'seconds.') # 0.20 seconds
    