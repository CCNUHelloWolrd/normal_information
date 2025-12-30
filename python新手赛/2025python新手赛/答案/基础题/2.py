def m_input():
    a = []
    for _ in range(5):
        while True:
            line = input().strip().split()
            if len(line) == 6:
                row = [float(num) for num in line]
                a.append(row)
                break
    return a

A = m_input()

for k in range(5):
    pivot = A[k][k]
    for j in range(6):
        A[k][j] /= pivot
    for i in range(5):
        if i != k:
            factor = A[i][k]
            for j in range(6):
                A[i][j] -= factor * A[k][j]

for row in A:
    print(row)

solutions = [row[5] for row in A]
print("方程组的解为:%.4f",solutions)