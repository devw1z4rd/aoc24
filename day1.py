from collections import Counter

def read_input(file_path):
    left_list = []
    right_list = []
    with open(file_path, "r") as file:
        for line in file:
            left, right = map(int, line.split())
            left_list.append(left)
            right_list.append(right)
    return left_list, right_list

def calculate_total_distance(left_list, right_list):
    left_list.sort()
    right_list.sort()
    return sum(abs(l - r) for l, r in zip(left_list, right_list))

def calculate_similarity_score(left_list, right_list):
    right_counts = Counter(right_list)
    return sum(num * right_counts[num] for num in left_list)

def main():
    left_list, right_list = read_input("input.txt")
    
    total_distance = calculate_total_distance(left_list, right_list)
    print(total_distance)
    
    similarity_score = calculate_similarity_score(left_list, right_list)
    print(similarity_score)

if __name__ == "__main__":
    main()
