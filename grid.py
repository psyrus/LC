def traverse(grid, current_indx, word, word_idx):

    # Check right
    right_check = traverse(grid, current_indx + [(current_indx[-1][0], current_indx[-1][1] + 1)], word, word_idx + 1)

    # Check down
    down_check = traverse(grid, current_indx + [(current_indx[-1][0] + 1, current_indx[-1][1])], word, word_idx + 1)

    return right_check if len(right_check) == (len(word) - word_idx) else down_check


def find_word_location(grid, word):

    for row_idx in range(len(grid)):
        for col_idx in range(len(grid[0])):
            if grid[row_idx][col_idx] == word[0]:
                # Traverse from here to figure out if we can find the rest of the word
                matched_indeces = traverse(grid, [(row_idx, col_idx)], word, 0)
                if len(matched_indeces) == len(word):
                    return matched_indeces

    return []

print(find_word_location(grid1, word1))
