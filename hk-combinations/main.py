from itertools import combinations

if __name__ == '__main__':
    info = input().split()
    word = sorted(info[0])
    size = int(info[1])
    all_combinations = []

    for i in range(size):
        i_combinations = list(map(lambda x: "".join(x), combinations(word, i + 1)))
        all_combinations.extend(i_combinations)

    for comb in all_combinations:
        print(comb)

