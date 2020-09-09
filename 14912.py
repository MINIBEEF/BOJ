# problem : https://www.acmicpc.net/problem/14912
def solve(n, d):
    answer = 0
    for digit in range(1, n + 1):
        answer += str(digit).count(d)
    return answer

if __name__ == '__main__':    
    n, d = input().split()
    n = int(n)
    d = d
    print(solve(n, d))