def minion_game(s: str) -> None:
    vowels = ['A','E','I','O','U']
    kevin = 0
    stuart = 0
    size = len(s)

    for i in range(size):
        if s[i] in vowels:
            kevin += size - i
        else:
            stuart += size - i

    if kevin > stuart:
        print(f"Kevin {kevin}")
    elif kevin < stuart:
        print(f"Stuart {stuart}")
    else:
        print('Draw')

if __name__ == '__main__':
    s = input("Enter the word: ")
    minion_game(s)