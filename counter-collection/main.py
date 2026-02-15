from collections import Counter

if __name__ == "__main__":
    size_list_shoes  = int(input())
    list_sizes       = [int(i) for i in input().split(" ")]
    number_customers = int(input())
    costumers        = []
    counter_sizes    = Counter(list_sizes)
    sum_sales        = 0

    for i in range(number_customers):
        costumers.append([int(i) for i in input().split(" ")])



    for costumer in costumers:
        if counter_sizes[costumer[0]] == 0:
            continue
        sum_sales += costumer[1]
        counter_sizes[costumer[0]] -= 1

    print(sum_sales)
