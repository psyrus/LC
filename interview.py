word1 = "catnip"
word2 = "cccc"
word3 = "s" 
word4 = "ant"
word5 = "aoi"
word6 = "ki"
word7 = "aaoo"
word8 = "ooo"

grid2 = [['a']]
word9 = "a"

grid1 = [
    ['c', 'c', 't', 'n', 'a', 'x'],
    ['c', 'c', 'a', 't', 'n', 't'],
    ['a', 'c', 'n', 'n', 't', 't'],
    ['t', 'n', 'i', 'i', 'p', 'p'],
    ['a', 'o', 'o', 'o', 'a', 'a'],
    ['s', 'a', 'a', 'a', 'o', 'o'],
    ['k', 'a', 'i', 'o', 'k', 'i']
]

def traverse(grid, row, col, word, word_idx):
    if word_idx > len(word) - 1 or row > len(grid) or col > len(grid[row]):
        return []

    grid_val = grid[row][col]
    word_char = word[word_idx]

    if grid_val != word_char:
        return []

    # Check right
    right_check = traverse(grid, row, col + 1, word, word_idx + 1)

    # Check down
    down_check = traverse(grid, row + 1, col, word, word_idx + 1)

    return [(row, col)] + (right_check if len(right_check) >= len(down_check) else down_check)


def find_word_location(grid, word):

    for row_idx in range(len(grid)):
        for col_idx in range(len(grid[0])):
            if grid[row_idx][col_idx] == word[0]:
                # Traverse from here to figure out if we can find the rest of the word
                matched_indeces = traverse(grid, row_idx, col_idx, word, 0)
                if len(matched_indeces) == len(word):
                    return matched_indeces

    return []

print(find_word_location(grid1, word1))
print(find_word_location(grid1, word2))
print(find_word_location(grid1, word3))