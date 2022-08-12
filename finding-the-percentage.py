if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()

    soma = 0
    for note in student_marks[query_name]:
        soma += note
    
    print("{0:.2f}".format(round(soma/len(student_marks[query_name]), 2)))