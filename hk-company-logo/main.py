if __name__ == "__main__":
    company_name = input()
    letter_freq = {}

    for letter in company_name:
        if letter_freq.get(letter):
            letter_freq[letter] += 1
        else:
            letter_freq[letter] = 1
    
    arr = list(letter_freq.items())
    arr.sort(key=lambda x: x[0])
    arr.sort(key=lambda x: x[1], reverse=True)
    arr = arr[:3]
    
    for occur in arr:
        print(f"{occur[0]} {occur[1]}")
