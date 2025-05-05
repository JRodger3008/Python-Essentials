# This is a short program that compares the drawn lottery numbers with the
# chosen bet numbers using a simple for loop

# Note that for larger datasets, converting 'drawn' to a set would improve
# performance: drawn = {4, 99, 27, 2, 7, 63, 78} # Note the curly brackets.

# This is because sets are implemented internally as a hash table, allowing the
# 'in' operator to run in constant time (O(1)), compared to a list that runs at
# linear time (O(n)).
# (O(1)) means it takes the same amount of time to execute, regardless of the
# input size.

# However, the downsides to sets are:
# - Sets do not preserve order
# - Sets cannot contain duplicates (True and 1 are considered the same value)
# - Sets themselves are considered mutable (elements can be removed/added), but
# the elements inside are immutable (you cannot change the existing items).

drawn = [4, 99, 27, 2, 7, 63, 78]
bets = [99, 63, 2, 16, 80, 27, 51]
hits = 0

for number in bets:
    if number in drawn:
        hits += 1

print(hits) # 4


# Use of sets below to achieve the same functionality above, but with better
# performance, however, this is only relevant with (1,000 x 1,000+) data points:

hits_2 = len(set(drawn) & set(bets))

print(hits_2) # 4

