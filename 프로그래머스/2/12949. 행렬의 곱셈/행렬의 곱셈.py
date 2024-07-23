def solution(arr1, arr2):
    # M * N // N * P // --> M * P
  # arr1의 행 개수 (m)과 열 개수 (n)

    m = len(arr1)
    n = len(arr1[0]) # len(arr2)

  # arr2의 열 개수 (p)
    p = len(arr2[0])

  # 결과 행렬 C의 초기화 (m x p 크기)
    result = [[0] * p for _ in range(m)]

  # 행렬 곱셈
    for i in range(m):
        for j in range(p):
            for k in range(n):
                result[i][j] += arr1[i][k] * arr2[k][j]

    return result