def subset_sum(weights, maxweight, num):
    M = [[0] * (maxweight + 1) for _ in range(num + 1)]

    for i in range(1, num + 1):
        for w in range(1, maxweight + 1):
            if weights[i] > w:
                M[i][w] = M[i - 1][w]
            else:
                M[i][w] = max(M[i - 1][w], weights[i] + M[i - 1][w - weights[i]])

    return M

def FindSolution(M, n, W):
    i,w = n,W
    included = []
    while i:
        if weights[i]<=w and M[i][maxweight] > M[i-1][w]:
            included.append(weights[i])
            w -= weights[i]
        i -= 1
    return included

num = int(input('Enter the number of items: '))
weights = [0] * (num + 1)

for i in range(1, num + 1):
    weights[i] = int(input(f'Enter the weight of item {i}: '))
maxweight = int(input('Enter the maximum weight: '))
M = subset_sum(weights, maxweight, num)
max = M[num][maxweight]
if max != maxweight:
    print('No solution')
    exit()
print('Maximum value: ', max)
print('Items included: ', FindSolution(M, num, maxweight))