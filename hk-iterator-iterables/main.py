from itertools import combinations

if __name__ == "__main__":
    size = int(input())
    letters = input().split()
    sub_size = int(input())
   
    a_occurrency = 0
    all_combinations = list(combinations(letters, sub_size))
    for comb in all_combinations:
        if 'a' in comb:
            a_occurrency += 1

    result = a_occurrency / len(all_combinations)

    print(f"{result:.3f}")
