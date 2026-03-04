from collections import defaultdict

if __name__ == "__main__":
    a, b = (int(x) for x in input().split())
    groups = defaultdict(list)

    for i in range(a):
        groups['A'].append(input())

    for i in range(b):
        groups['B'].append(input())
    print(len(groups['B']))


    for bv in groups['B']:
        result = ""
        for i, v in enumerate(groups['A']):
            if v == bv:
                result += f"{i + 1} " # 1 based indexed,as the challenge asks
        
        print("-1" if result == "" else result)
