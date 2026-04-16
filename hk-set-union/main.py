if __name__ == "__main__":
    size_student_english = int(input())
    eng_students = set(map(int, input().split()))
    size_stundent_france = int(input())
    fr_students = set(map(int, input().split()))

    result = eng_students | fr_students

    print(len(result))
