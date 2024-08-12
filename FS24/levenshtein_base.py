# Student Name: Ishana Rana
# Matriculation Number: 21-727-078


def levenshtein(a: str | list[str], b: str | list[str], insertion_cost=1, deletion_cost=1, substitution_cost=1) -> float:
    n, m = len(a), len(b)
    dp_matrix = [[0 for _ in range(m + 1)] for _ in range(n + 1)]

    # Base Case: Cost for inserting characters into an empty 'a' to match 'b'
    for j in range(m + 1):
        dp_matrix[0][j] = j * insertion_cost
    # Base Case: Cost for deleting characters from 'a' to match an empty 'b'
    for i in range(n + 1):
        dp_matrix[i][0] = i * deletion_cost

    # Transitions
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if a[i-1] == b[j-1]:
                dp_matrix[i][j] = dp_matrix[i-1][j-1]
            else:
                dp_matrix[i][j] = min(
                    dp_matrix[i-1][j] + insertion_cost,  # Insertion
                    dp_matrix[i][j-1]+ deletion_cost,  # Deletion
                    dp_matrix[i-1][j-1]+ substitution_cost # Replacement

                )

    return dp_matrix[n][m]

    
