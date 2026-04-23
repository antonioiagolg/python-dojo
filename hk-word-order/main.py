from collections import OrderedDict

if __name__ == "__main__":
    size = int(input())
    result = OrderedDict()
    
    for i in range(size):
        word = input()
        if result.get(word):
            result[word] += 1
        else:
            result[word] = 1
            
    print(len(result.keys())) 
    print(" ".join(map(str, result.values())))
