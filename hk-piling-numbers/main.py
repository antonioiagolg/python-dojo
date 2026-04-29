from collections import deque

def can_pile(cubes):
    
    ground = 2147483649 # Start ground as the biggest possible lengt, above the scope of the challenge

    while len(cubes) > 1:
        cube_right = cubes.pop()
        cube_left = cubes.popleft()
        aux = 0

        if cube_right > cube_left:
            aux = cube_right
            cubes.appendleft(cube_left)
        else:
            aux = cube_left
            cubes.append(cube_right)

        if aux > ground:
            return "No" # impossible to pile up
        else:
            ground = aux # now the cube will be the ground for the others


    if cubes.pop() <= ground:
        return "Yes"
    else:
        return "No"

    

if __name__ == "__main__":
    test_cases = int(input())
    print(test_cases)
    answers = []

    for test in range(test_cases):
        try:
            total_cubes = int(input())
            cubes = deque(map(int, input().split()))
            answers.append(can_pile(cubes))
        except EOFError:
            break

    for result in answers:
        print(result)

