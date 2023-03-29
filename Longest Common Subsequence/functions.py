from itertools import product
import random
from collections import defaultdict


# brute force algorithm
def brute_force(sequence1, sequence2):
    max = 0
    max_sub = str()
    # Δημιουργία λίστας με όλους τους πιθανούς συνδιασμούς True - False, ώστε να πάρουμε και όλες τις υποακολουθίες της πρώτης ακολουθίας
    true_false_list = [x for x in product([True, False], repeat=len(sequence1))]
    for true_false in true_false_list:
        subsequence = str()
        for index, boolean in enumerate(true_false):
            if boolean == True:
                subsequence += sequence1[index]
        if len(subsequence) == 0:
            continue
        found = 0   # Εύρεση της μέγιστης κοινής υποακολουθίας και του μήκους της
        for letter in sequence2:
            if letter == subsequence[found]:
                found += 1
            if found == len(subsequence):
                if len(subsequence) > max:
                    max = len(subsequence)
                    max_sub = subsequence
                break

    return max, max_sub


# Κατασκευή τυχαίων ακολουθιών dna
def create_dna_sequense(n, chars, available_chars):
    dna_sequences = list()
    for _ in range(n):
        new_sequence = str()
        for _ in range(chars):
            new_sequence += available_chars[random.randint(0, 3)]
        dna_sequences.append(new_sequence)
    return dna_sequences


# Longest Common Subsequence Algorithm
def lcs(sequence1, sequence2):
    length_sequence1 = len(sequence1)
    length_sequence2 = len(sequence2)
    dp = dp_table(sequence1, sequence2)
    if length_sequence1 == 0 or length_sequence2 == 0:
        return str()
    common_subsequnce = str()
    i  =  length_sequence1
    j  =  length_sequence1

    while i >= 0 and j >= 0:
        current = dp[i][j]
        up = dp[i][j - 1]
        left = dp[i - 1][j]
        if current > left and current > up:
            common_subsequnce += sequence1[i-1] 
            i -= 1
            j -= 1
        elif dp[i-1][j] > dp[i][j-1]:
            i -= 1
        else:
            j -= 1
    return len(common_subsequnce), common_subsequnce[::-1]


# create a table algorithm lcs
def dp_table(sequence1, sequence2):
    n = len(sequence1)
    m = len(sequence2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if sequence1[i-1] == sequence2[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    return dp
