from collections import defaultdict
def picking_numbers(num_list):
    ocurrencies = defaultdict(int)
    
    for num in num_list:
        ocurrencies[num] += 1
    
    biggest_array = 0
    
    for i in range(0,100):
        current_big = ocurrencies[i] + ocurrencies[i+1]
        biggest_array = max(biggest_array, current_big)
        
    return biggest_array 



if __name__ == "__main__":
    answer = picking_numbers([4,6,5,3,3,1])
    print(answer)
