import sys


def input():
    return sys.stdin.readline().rstrip()


def drawLine(N: int, cnt: int):
    print(
        " " * (cnt)
        + "*"
        + " " * (N - 2)
        + "*"
        + " " * ((N - cnt - 2) * 2 + 1)
        + "*"
        + " " * (N - 2)
        + "*"
    )


N = int(input())
print("*" * (N) + " " * ((N - 2) * 2 + 1) + "*" * (N))
for i in range(1, N - 1):
    drawLine(N, i)
print(" " * (N - 1) + "*" + " " * (N - 2) + "*" + " " * (N - 2) + "*")
for i in range(N - 2, 0, -1):
    drawLine(N, i)
print("*" * (N) + " " * ((N - 2) * 2 + 1) + "*" * (N))


"""
*****       *****
 *   *     *   *
  *   *   *   *
   *   * *   *
    *   *   *
   *   * *   *
  *   *   *   *
 *   *     *   *
*****       *****
"""
