def parse_input(input_text):
    lines = input_text.strip().split('\n')
    rules = []
    updates = []
    
    for line in lines:
        line = line.strip()
        if not line:
            continue
        
        if '|' in line:
            before, after = line.split('|')
            rules.append((int(before), int(after)))
        elif ',' in line:
            pages = [int(page) for page in line.split(',')]
            updates.append(pages)
    
    return rules, updates

def is_correctly_ordered(update, rules):
    page_positions = {page: i for i, page in enumerate(update)}
    
    for before, after in rules:
        if before in page_positions and after in page_positions:
            if page_positions[before] > page_positions[after]:
                return False
    
    return True

def get_middle_page(update):
    middle_index = len(update) // 2
    return update[middle_index]

def reorder_update(update, rules):
    graph = {page: [] for page in update}
    
    for before, after in rules:
        if before in update and after in update:
            graph[before].append(after)
    
    in_degree = {page: 0 for page in update}
    for page in update:
        for after in graph.get(page, []):
            in_degree[after] += 1
    
    from heapq import heappush, heappop
    heap = []
    for page in update:
        if in_degree[page] == 0:
            heappush(heap, (-page, page))
    
    sorted_pages = []
    while heap:
        _, current = heappop(heap)
        sorted_pages.append(current)
        
        for after in graph.get(current, []):
            in_degree[after] -= 1
            if in_degree[after] == 0:
                heappush(heap, (-after, after))
    
    return sorted_pages

def solve_both_parts(input_text):
    rules, updates = parse_input(input_text)
    
    correct_updates = []
    incorrect_updates = []
    
    for update in updates:
        if is_correctly_ordered(update, rules):
            correct_updates.append(update)
        else:
            incorrect_updates.append(update)
    
    part1_sum = sum(get_middle_page(update) for update in correct_updates)
    
    corrected_updates = [reorder_update(update, rules) for update in incorrect_updates]
    part2_sum = sum(get_middle_page(update) for update in corrected_updates)
    
    return part1_sum, part2_sum

def main():
    with open("input.txt", "r") as f:
        input_text = f.read()
    
    part1, part2 = solve_both_parts(input_text)
    print(f"Part 1: {part1}")
    print(f"Part 2: {part2}")

if __name__ == "__main__":
    main()