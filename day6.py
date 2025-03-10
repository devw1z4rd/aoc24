def solve_guard_patrol(input_text):
    grid = input_text.strip().split('\n')
    rows, cols = len(grid), len(grid[0])
    
    guard_r, guard_c, guard_dir = find_guard(grid)
    
    directions = {'^': (-1, 0), '>': (0, 1), 'v': (1, 0), '<': (0, -1)}
    right_turn = {'^': '>', '>': 'v', 'v': '<', '<': '^'}
    
    part1_result = count_visited_positions(grid, guard_r, guard_c, guard_dir, directions, right_turn)
    
    part2_result = count_loop_positions(grid, guard_r, guard_c, guard_dir, directions, right_turn)
    
    return part1_result, part2_result

def find_guard(grid):
    for r in range(len(grid)):
        for c in range(len(grid[r])):
            if grid[r][c] in ['^', 'v', '<', '>']:
                return r, c, grid[r][c]
    return None, None, None

def count_visited_positions(grid, guard_r, guard_c, guard_dir, directions, right_turn):
    rows, cols = len(grid), len(grid[0])
    r, c = guard_r, guard_c
    dir_char = guard_dir
    
    visited = set([(r, c)])
    
    while True:
        dr, dc = directions[dir_char]
        next_r, next_c = r + dr, c + dc
        
        if not (0 <= next_r < rows and 0 <= next_c < cols):
            break
        
        if grid[next_r][next_c] == '#':
            dir_char = right_turn[dir_char]
        else:
            r, c = next_r, next_c
            visited.add((r, c))
    
    return len(visited)

def count_loop_positions(grid, guard_r, guard_c, guard_dir, directions, right_turn):
    rows, cols = len(grid), len(grid[0])
    loop_positions = []
    
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] != '.' or (r == guard_r and c == guard_c):
                continue
            
            new_grid = create_grid_with_obstruction(grid, r, c)
            
            if is_loop_created(new_grid, guard_r, guard_c, guard_dir, directions, right_turn):
                loop_positions.append((r, c))
    
    return len(loop_positions)

def create_grid_with_obstruction(grid, obs_r, obs_c):
    new_grid = []
    for r, row in enumerate(grid):
        if r == obs_r:
            new_row = row[:obs_c] + '#' + row[obs_c+1:]
        else:
            new_row = row
        new_grid.append(new_row)
    return new_grid

def is_loop_created(grid, start_r, start_c, start_dir, directions, right_turn, max_steps=1000):
    rows, cols = len(grid), len(grid[0])
    r, c = start_r, start_c
    dir_char = start_dir
    
    visited_states = set()
    
    for _ in range(max_steps):
        state = (r, c, dir_char)
        if state in visited_states:
            return True
        
        visited_states.add(state)
        
        dr, dc = directions[dir_char]
        next_r, next_c = r + dr, c + dc
        
        if not (0 <= next_r < rows and 0 <= next_c < cols):
            return False
        
        if grid[next_r][next_c] == '#':
            dir_char = right_turn[dir_char]
        else:
            r, c = next_r, next_c
    
    return True

def visualize_path(grid, guard_r, guard_c, guard_dir, obstruction_r=None, obstruction_c=None):
    directions = {'^': (-1, 0), '>': (0, 1), 'v': (1, 0), '<': (0, -1)}
    right_turn = {'^': '>', '>': 'v', 'v': '<', '<': '^'}
    
    if obstruction_r is not None and obstruction_c is not None:
        grid = create_grid_with_obstruction(grid, obstruction_r, obstruction_c)
    
    vis_grid = [list(row) for row in grid]
    
    horizontal_moves = set()
    vertical_moves = set()
    
    r, c = guard_r, guard_c
    dir_char = guard_dir
    
    visited_states = {}
    step = 0
    loop_start = None
    
    while True:
        state = (r, c, dir_char)
        if state in visited_states:
            loop_start = visited_states[state]
            break
        
        visited_states[state] = step
        step += 1
        
        dr, dc = directions[dir_char]
        next_r, next_c = r + dr, c + dc
        
        if not (0 <= next_r < len(grid) or 0 <= next_c < len(grid[0])):
            break
        
        if next_r >= len(grid) or next_c >= len(grid[next_r]) or grid[next_r][next_c] == '#':
            dir_char = right_turn[dir_char]
        else:
            if dir_char in ['^', 'v']:
                vertical_moves.add((r, c))
            else:
                horizontal_moves.add((r, c))
            
            r, c = next_r, next_c
    
    for r in range(len(vis_grid)):
        for c in range(len(vis_grid[r])):
            if (r, c) in horizontal_moves and (r, c) in vertical_moves:
                vis_grid[r][c] = '+'
            elif (r, c) in horizontal_moves:
                vis_grid[r][c] = '-'
            elif (r, c) in vertical_moves:
                vis_grid[r][c] = '|'
    
    if obstruction_r is not None and obstruction_c is not None:
        vis_grid[obstruction_r][obstruction_c] = 'O'
    
    return '\n'.join([''.join(row) for row in vis_grid])

def main():
    with open("input.txt", "r") as f:
        input_text = f.read()
    
    part1, part2 = solve_guard_patrol(input_text)
    
    print(f"Part 1: {part1}")
    print(f"Part 2: {part2}")
    

if __name__ == "__main__":
    main()