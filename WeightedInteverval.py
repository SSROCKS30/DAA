def find_latest_non_overlapping(jobs, index):
    for i in range(index - 1, -1, -1):
        if jobs[i][1] <= jobs[index][0]:
            return i
    return -1
    
def weighted_interval_scheduling(jobs):
    jobs.sort(key=lambda x: x[1])

    n = len(jobs)
    p = [0] * n
    for j in range(n):
        p[j] = find_latest_non_overlapping(jobs, j)

    M = [0] * (n) 
    def M_compute_OPT(j):
        if j == -1:
            return 0
        if M[j] == 0:
            M[j] = max(jobs[j][2] + M_compute_OPT(p[j]), M_compute_OPT(j - 1))
        return M[j]

    return M_compute_OPT(n - 1)

num = int(input('Enter the number of jobs: '))
jobs = []
for i in range(num): # jobs = [(1, 2, 50), (3, 5, 20), (6, 19, 100), (2, 100, 200)]
    start, end, weight = map(int, input(f"Enter the (start, end, weight) of job {i + 1}: ").split())
    jobs.append((start, end, weight))

max_weight = weighted_interval_scheduling(jobs)
print("Maximum weight of non-overlapping intervals:", max_weight)