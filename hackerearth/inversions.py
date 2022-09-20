# name = input()                  # Reading input from STDIN
# print('Hi, %s.' % name)         # Writing output to STDOUT
T = input()
assert 1<= int(T) <= 100

for _ in range(int(T)):
    N = input()
    # print(N)
    assert len(N) > 0
    matrix = []
    for _ in range(int(N)):
        row = input().split(" ")
        row = [int(i) for i in row]
        matrix.append(row)

    inversions = 0

    # matrix_flat = [i for j in matrix for i in j]
    inversion_array = [y2
    for i1,x1 in enumerate(matrix)
    for j1,y1 in enumerate(x1)
    for i2,x2 in enumerate(matrix)
    for j2,y2 in enumerate(x2)            
    if ((i1 <= i2) and
    (j1<=j2) and
    y1>y2)
    ]
 
    print(len(inversion_array))
                


        
