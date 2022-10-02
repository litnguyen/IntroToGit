def copySub(string,i,l): 
    j = i
    s = ""
    while j< i+l:
        s = s + string[j]
        j = j+1
    return s

def count_substring(string, sub_string):
    i = 0
    count = 0
    for i in range(len(string)-len(sub_string)+1):
        print(i)
        s = copySub(string,i,len(sub_string))
        if s == sub_string:
            count += 1
    return count

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    s = copySub(string,0,len(sub_string))
    print(s)
    count = count_substring(string, sub_string)
    print(count)
    
    l = [1, 2, 3, 5, 0]
    print(any(l))
    l = [0, False]
    print(any(l))
    l = [0, False, 8]
    print(any(l))
    l = []
    print(any(l))

    print([char.isalnum() for char in string])