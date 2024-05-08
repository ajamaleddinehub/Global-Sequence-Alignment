import numpy as np

MATCH_SCORE = 1
MISMATCH_SCORE = -1
GAP_SCORE = -2

# READING CUSTOM SEQUENCES
# sequence_one = input("Input the first sequence: ")
# sequence_two = input("Input the second sequence: ")

# USING DEFINED SEQUENCES
sequence_one = "ATCGTAATTGCC"
sequence_two = "ACGTTAATTGC"

score_matrix = np.zeros((len(sequence_one) + 1, len(sequence_two) + 1))
match_checker_matrix = np.zeros((len(sequence_one), len(sequence_two)))

for i in range(len(sequence_one)):
    for j in range(len(sequence_two)):
        if sequence_one[i] == sequence_two[j]:
            match_checker_matrix[i][j] = MATCH_SCORE
        else:
            match_checker_matrix[i][j] = MISMATCH_SCORE

# NEEDLEMAN-WUNSCH ALGORITHM
for i in range(len(sequence_one)):
    score_matrix[i][0] = i * GAP_SCORE
for j in range(len(sequence_two)):
    score_matrix[0][j] = j * GAP_SCORE

for i in range(1, len(sequence_one) + 1):
    for j in range(1, len(sequence_two) + 1):
        score_matrix[i][j] = max(
            score_matrix[i - 1][j - 1] + match_checker_matrix[i - 1][j - 1],
            score_matrix[i - 1][j] + GAP_SCORE,
            score_matrix[i][j - 1] + GAP_SCORE,
        )
print(f"SCORE MATRIX:\n{score_matrix}")

# ALIGNMENT COMPARISON
sequence_one_alignment = ""
sequence_two_alignment = ""

sequence_one_length = len(sequence_one)
sequence_two_length = len(sequence_two)

while sequence_one_length > 0 and sequence_two_length > 0:
    if (
        sequence_one_length > 0
        and sequence_two_length > 0
        and score_matrix[sequence_one_length][sequence_two_length]
        == score_matrix[sequence_one_length - 1][sequence_two_length - 1]
        + match_checker_matrix[sequence_one_length - 1][sequence_two_length - 1]
    ):
        sequence_one_alignment = (
            sequence_one[sequence_one_length - 1] + sequence_one_alignment
        )
        sequence_two_alignment = (
            sequence_two[sequence_two_length - 1] + sequence_two_alignment
        )
        sequence_one_length = sequence_one_length - 1
        sequence_two_length = sequence_two_length - 1
    elif (
        sequence_one_length > 0
        and score_matrix[sequence_one_length][sequence_two_length]
        == score_matrix[sequence_one_length - 1][sequence_two_length] + GAP_SCORE
    ):
        sequence_one_alignment = (
            sequence_one[sequence_one_length - 1] + sequence_one_alignment
        )
        sequence_two_alignment = "-" + sequence_two_alignment
        sequence_one_length = sequence_one_length - 1
    else:
        sequence_one_alignment = "-" + sequence_one_alignment
        sequence_two_alignment = (
            sequence_two[sequence_two_length - 1] + sequence_two_alignment
        )
        sequence_two_length = sequence_two_length - 1

print(
    f"\n\nALIGNMENT:\nSequence one: {sequence_one_alignment}\nSequence two: {sequence_two_alignment}"
)
