# find lucky triples in an array of positive integers
# x,y,z is a lucky triple if y is divisible by x and z is divisible by y and their indexes appear in order xi<yi<zi

def solution(a):

    total = 0
    for x in range(len(a)):
        for y in range(x+1, len(a)):
            for z in range(y+1, len(a)):
                if a[z]%a[y]==0 and a[y]%a[x]==0:
                    total+=1

    return total


def solution2(l):

    # div_matrix element i,j is 1 if l[j] is divisible by l[i], else 0; identities are 0
    # cumulative_matrix i,j is n if until jth element of l, n total elements were divisible by l[i] - including l[j]
    # last column of each row of cumulative matrix gives total count of divisible elements by l[row_number]
    # logic to solve is O(n^2) - find each element j divisible by i from div_matrix, add last element of jth row from cumulative matrix
    n = len(l)
    div_matrix = [[0]*n for _ in range(n)]
    cumulative_list = [0]*n
    for i in range(n-1):
        cumulative_divs = 0
        for j in range(i+1,n):
            if l[j]%l[i]==0:
                div_matrix[i][j]=1
                cumulative_divs += 1
                
        cumulative_list[i] = cumulative_divs
        
    total = 0
    for i in range(n-2):
        for j in range(i+1, n-1):
            if div_matrix[i][j]==1:
                total += cumulative_list[j]
                
    return total