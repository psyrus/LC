"""
An image is represented by an m x n integer grid image where image[i][j] represents the pixel value of the image.

You are also given three integers sr, sc, and newColor. You should perform a flood fill on the image starting from the pixel image[sr][sc].

To perform a flood fill, consider the starting pixel, plus any pixels connected 4-directionally to the starting pixel of the same color as the starting pixel, plus any pixels connected 4-directionally to those pixels (also with the same color), and so on. Replace the color of all of the aforementioned pixels with newColor.

Return the modified array after performing the flood fill.

Input: image = [[1,1,1],[1,1,0],[1,0,1]], sr = 1, sc = 1, newColor = 2
Output: [[2,2,2],[2,2,0],[2,0,1]]
Explanation: From the center of the image with position (sr, sc) = (1, 1) (i.e., the red pixel), all pixels connected by a path of the same color as the starting pixel (i.e., the blue pixels) are colored with the new color.
Note the bottom corner is not colored 2, because it is not 4-directionally connected to the starting pixel.
"""
from typing import List
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:

        original_color = image[sr][sc]

        def visitNeighbors(row_idx, col_idx, color):
            # Need to visit up one, left one, right one, down one
            # Ensure we do not visit the same node twice by checking the color
            if row_idx >= len(image) or col_idx >= len(image[0]):
                return

            if row_idx < 0 or col_idx < 0:
                return

            if image[row_idx][col_idx] != original_color:
                return

            image[row_idx][col_idx] = color

            visitNeighbors(row_idx + 1, col_idx, color)
            visitNeighbors(row_idx - 1, col_idx, color)
            visitNeighbors(row_idx, col_idx + 1, color)
            visitNeighbors(row_idx, col_idx - 1, color)


        if original_color != newColor:
            visitNeighbors(sr, sc, newColor)

        return image


class SolutionOld:
    image_ref = []
    passed = {}
    def fillSurrounding(self, this_row_idx: int, this_col_idx: int, original_color: int, color_to_set: int) -> None:
        self.image_ref[this_row_idx][this_col_idx] = color_to_set
        self.passed[(this_row_idx, this_col_idx)] = True

        for vertical in range(-1, 2):
            for horizontal in range(-1, 2):
                if abs(vertical) == abs(horizontal):
                    # Skip diagonal values
                    continue
                new_row_idx = this_row_idx + vertical
                new_col_idx = this_col_idx + horizontal

                # Ignore out of bounds
                if new_row_idx < 0 or new_row_idx >= len(self.image_ref):
                    continue
                if new_col_idx < 0 or new_col_idx >= len(self.image_ref[0]):
                    continue
                if self.image_ref[new_row_idx][new_col_idx] == original_color and (new_row_idx, new_col_idx) not in self.passed:
                    self.fillSurrounding(new_row_idx, new_col_idx, original_color, color_to_set)

    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        self.passed = {}
        self.image_ref = image

        self.fillSurrounding(sr, sc, image[sr][sc], newColor)

        return self.image_ref


x = Solution()

print(x.floodFill([[0,0,0],[0,0,0]], 0, 0, 2))
print(x.floodFill([[0,0,0],[0,1,1]], 1,1,1))
print(x.floodFill([[1,1,1],[1,1,0],[1,0,1]], 1,1,2))
print(x.floodFill([[0,0,0],[0,0,0]], 0, 0, 2))