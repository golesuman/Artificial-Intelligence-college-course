import itertools
import random
import time

         
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
    

        
def bfs(puzzle, goal, get_moves):
    # maintain a queue of paths
    queue = []
    # push the first path into the queue
    queue.append([puzzle])
    while queue:
        # get the first path from the queue
        path = queue.pop(0)
        # get the last node from the path
        node = path[-1]
        # path found
        if node == goal:
            return path
        # enumerate all adjacent nodes, construct a new path and push it into the queue
        for adjacent in (get_moves(node)):
            if adjacent not in path:
                new_path = list(path)
                new_path.append(adjacent)
                queue.append(new_path)

if __name__ == '__main__':
    reps = 10
   

    
    # Breadth first search
    total_time = 0
    for i in range(reps):
        puzzle, goal = num_matrix(3, 3)
        t0 = time.time()
        solution = bfs(puzzle, goal, num_moves(3, 3))
        print(solution)
        t1 = time.time()
        total_time += t1 - t0
    total_time /= reps
    print('Puzzle solved using breadth depth first search in', total_time, 'seconds.') # 0.04 seconds