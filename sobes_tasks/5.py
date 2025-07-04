matrix = [[12, -4, 9],
          [9, 0, -51],
          [1, 4, 6]]

main_diag_sum = 0
secondary_diag_sum = 0
n = 3

for i in range(n):
    main_diag_sum += matrix[i][i]
    secondary_diag_sum += matrix[i][n - 1 - i]

print(abs(main_diag_sum - secondary_diag_sum))

