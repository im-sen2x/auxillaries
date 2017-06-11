"""Recursive call to Towers of Hanoi Problem with np.array visualization."""

import numpy as np


def hanoi(n, mat, arr, fr, to, spare):

	if n == 1:
		fr_val = None
		print(arr)
		print("\n")

		for r in range(mat):
			if arr[r][fr] != 0:
				fr_val = arr[r][fr]
				arr[r][fr] = 0
				break

		for r1 in range(1, mat+1, 1):
			if arr[-r1][to] == 0:
				arr[-r1][to] = fr_val
				break
		return arr

	else:
		hanoi(n-1, mat, arr, fr, spare, to)
		hanoi(1, mat, arr, fr, to, spare)
		hanoi(n-1, mat, arr, spare, to, fr)

		return arr




arr = np.array([[0, 1, 0],
				[0, 2, 0],
	   			[0, 3, 0]])

arr1 = np.array([[1, 0, 0],
				[2, 0, 0],
				[3, 0, 0],
				[4, 0, 0]])

arr2 = np.array([[0, 0, 1],
				[0, 0, 2],
				[0, 0, 3],
				[0, 0, 4],
				[0, 0, 5]])

#print(hanoi(3, 3, np.copy(arr), 1, 2, 0))
#print(hanoi(3, 3, np.copy(arr), 1, 0, 2))
#print(hanoi(4, 4, np.copy(arr1), 0, 2, 1))
#print(hanoi(4, 4, np.copy(arr1), 0, 1, 2))
print(hanoi(5, 5, np.copy(arr2), 2, 0, 1))

print(arr2)
