from collections import OrderedDict

if __name__ == "__main__":
    size = int(input())
    result = OrderedDict()

    for i in range(size):
        sell_info = input().split()
        
        value = int(sell_info[-1]) # Always the last
        product = " ".join(sell_info[0:len(sell_info) - 1]) # Cases where the product is composed with more than 2 words

        if result.get(product):
            result[product] += value
        else:
            result[product] = value

    for product, net_price in result.items():
        print(f"{product} {net_price}")
