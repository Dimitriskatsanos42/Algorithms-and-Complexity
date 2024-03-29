from functions import brute_force, create_dna_sequense, lcs 
from itertools import combinations

def main():
    n = 5  
    chars = 10  # 2000
    available_chars = "AGCT"

    dna_sequences = create_dna_sequense(n=n, chars=chars, available_chars=available_chars)

    # Δημιουργήστε όλους τους συνδυασμούς και εκτελέστε τον αλγόριθμο
    combs = combinations(dna_sequences, 2)
    max_length = 0
    max_length2 = 0
    result1 = list()
    result2 = list()
    for sequence1 , sequence2  in combs:
        max, maxsub = brute_force(sequence2 , sequence2)
        if max > max_length:
            result1 = list()
            result1.append((sequence2 , sequence2 , maxsub, max))
            max_length = max
        elif max == max_length:
            result1.append((sequence2 , sequence2 , maxsub, max))

        max2, maxsub2 = lcs(sequence1 , sequence2 )
        if max2 > max_length2:
            result2 = list()
            result2.append((sequence1 , sequence2 , maxsub2, max2))
            max_length2 = max2
        elif max2 == max_length2:
            result2.append((sequence1 , sequence2 , maxsub2, max2))


    print(f"\nThe results from brute force algorithm are\n {result1}")
    print(f"\nThe results from  algorithm are Longest Common Subsequence\n {result2}")


if __name__ == "__main__":
    main()