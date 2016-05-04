digit_lengths = [3, 3, 5, 4, 4, 3, 5, 5, 4]
teen_lengths = [3, 6, 6, 8, 8, 7, 7, 9, 8, 8]
tens_lengths = [6, 6, 5, 5, 5, 7, 6, 6]
hundreds_lengths = [digit_length + 7 for digit_length in digit_lengths]

sum_100 = 9*sum(digit_lengths) + sum(teen_lengths) + 10*sum(tens_lengths)
sum_1000 = 100*sum(hundreds_lengths) + 99*9*3 + 10*sum_100 + 11

print sum_1000
