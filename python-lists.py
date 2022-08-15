if __name__=="__main__":
    list_values = []
    N = int(input(""))
    
    for i in range(N):
        arr = list(input().split())

        if arr[0] == 'insert':
            list_values.insert(int(arr[1]), int(arr[2]))
        elif arr[0] == 'print':
            print(list_values)
        elif arr[0] == 'remove':
            list_values.remove(int(arr[1]))
        elif arr[0] == 'append':
            list_values.append(int(arr[1]))
        elif arr[0] == 'sort':
            list_values.sort()
        elif arr[0] == 'pop':
            list_values.pop()
        elif arr[0] == 'reverse':
            list_values.reverse()