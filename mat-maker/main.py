if __name__ == '__main__':
    dimensions = input().split(' ')
    rows, columns = int(dimensions[0]), int(dimensions[1])
    stick = '.|.'
    hifen = '-'
    sentence = 'WELCOME'

    middle_mat_y = int(((rows + 1)/2) - 1)
    middle_mat_x = int(((columns + 1)/2) - 1)

    aux = 0

    for i in range(middle_mat_y):
        aux = i
        print((stick * i).rjust(middle_mat_x - 1,hifen) + stick + (stick * i).ljust(middle_mat_x - 1, hifen))

    print(sentence.center(columns, hifen))

    for i in range(aux, -1, -1):
        print((stick * i).rjust(middle_mat_x - 1, hifen) + stick + (stick * i).ljust(middle_mat_x - 1, hifen))
