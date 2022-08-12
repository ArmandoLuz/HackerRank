if __name__ == '__main__':
    list_records = []
    list_scores = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        list_scores.append(score)
        list_records.append([name, score])

    #Eliminando valores repetidos
    list_scores = list(set(list_scores))

    #Ordenando os scores em ordem crescente
    list_scores.sort()

    print(list_scores)

    #Pegando o segundo maior valor
    val = list_scores[1]

    #Ordenando os nomes em ordem alfabética
    list_records.sort()

    for i in range(len(list_records)):
        if list_records[i][1] == val:
            print(list_records[i][0])
            

    