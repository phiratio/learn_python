# Code Listing #1

"""

Maximum subarray problem - original version

"""

import itertools


# max_subarray: v1
def max_subarray(sequence):
    """ Find sub-sequence in sequence having maximum sum """

    sums = []

    for i in range(len(sequence)):
        # Create all sub-sequences in given size
        for sub_seq in itertools.combinations(sequence, i):
            # Append sum
            print(sub_seq, '=>', sums)
            sums.append(sum(sub_seq))

    return max(sums)

if __name__ == '__main__':
    print(max_subarray([-5, 20, -10, 30, 15]))