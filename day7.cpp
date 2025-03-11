#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <sstream>

long long concatenate(long long a, long long b) {
    std::string b_str = std::to_string(b);
    long long multiplier = 1;
    for (int i = 0; i < b_str.length(); ++i) {
        multiplier *= 10;
    }
    return a * multiplier + b;
}

bool solvePartOne(long long test_value, const std::vector<int>& numbers) {
    int n = numbers.size();
    long long num_combinations = 1LL << (n - 1);

    for (long long combo = 0; combo < num_combinations; combo++) {
        long long result = numbers[0];

        for (int i = 1; i < n; i++) {
            bool is_multiply = (combo >> (i - 1)) & 1;
            if (is_multiply) {
                result *= numbers[i];
            }
            else {
                result += numbers[i];
            }
        }

        if (result == test_value) {
            return true;
        }
    }

    return false;
}

bool solvePartTwo(long long test_value, const std::vector<int>& numbers) {
    int n = numbers.size();
    long long num_combinations = 1;

    for (int i = 0; i < n - 1; ++i) {
        num_combinations *= 3;
    }

    for (long long combo = 0; combo < num_combinations; combo++) {
        long long result = numbers[0];
        long long temp_combo = combo;

        for (int i = 1; i < n; i++) {
            int op = temp_combo % 3;
            temp_combo /= 3;

            switch (op) {
            case 0: result += numbers[i]; break;
            case 1: result *= numbers[i]; break;
            case 2: result = concatenate(result, numbers[i]); break;
            }
        }

        if (result == test_value) {
            return true;
        }
    }

    return false;
}

std::vector<int> parseNumbers(const std::string& str) {
    std::vector<int> numbers;
    std::istringstream iss(str);
    int num;

    while (iss >> num) {
        numbers.push_back(num);
    }

    return numbers;
}

int main() {
    std::ifstream file("input.txt");
    std::string line;
    long long part1_sum = 0;
    long long part2_sum = 0;

    if (!file.is_open()) {
        std::cerr << "Error opening file: input.txt" << std::endl;
        return 1;
    }

    while (std::getline(file, line)) {
        if (line.empty()) continue;

        size_t colon_pos = line.find(':');
        if (colon_pos == std::string::npos) continue;

        long long test_value = std::stoll(line.substr(0, colon_pos));
        std::vector<int> numbers = parseNumbers(line.substr(colon_pos + 1));

        if (numbers.empty()) continue;

        if (solvePartOne(test_value, numbers)) {
            part1_sum += test_value;
        }

        if (solvePartTwo(test_value, numbers)) {
            part2_sum += test_value;
        }
    }

    std::cout << "Part 1: " << part1_sum << std::endl;
    std::cout << "Part 2: " << part2_sum << std::endl;

    file.close();
    return 0;
}