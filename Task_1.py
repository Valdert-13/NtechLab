
def findMaxSubArray(A: list) -> list:
    """
    Обработчик масивов, находит непрерывный подмассив в массиве, содержащий хотя бы одно число,
    который имеет наибольшую сумму.
    :param A: list[int]
        Массив целых чисел

    :return: list[int]

    """

    assert len(A) > 0, 'Function findMaxSubArray expects a non-zero-length list'
    assert type(A) == list, 'Function findMaxSubArray expects to get a list'
    assert all(type(i) == int for i in A), 'List should contain all values of type int'

    len_arr = len(A)
    sum_arr = min(A)
    index = [min(A)]
    for i in range(len_arr):
        for j in range(i, len_arr):
            sum_val = sum(A[i:j+1])
            if sum_val > sum_arr:
                sum_arr = sum_val
                index = A[i: j+1]

    # if not index:
    #     index = [A[0]] # Для одинаковых отрицательный значений [-1, -1]

    return index

ls = [[5]*5, [0]*5, [-1]*5, [-2,1,-3,4,-1,2,1,-5,4], [-5, -2, -3, -4]]
for A in ls:
    print(findMaxSubArray(A))

