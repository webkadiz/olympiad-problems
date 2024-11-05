/*
https://leetcode.com/problems/number-of-islands/

Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.


Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1


Input: grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Output: 3


Constraints:
  m == grid.length
  n == grid[i].length
  1 <= m, n <= 300
  grid[i][j] is '0' or '1'.

*/

/**
 * @param {character[][]} grid
 * @return {number}
 */
var numIslands = function (grid) {
  function bypassVertex(i, j) {
    if (!grid[i]) return false
    if (!grid[i][j]) return false
    if (handledGrid[i][j]) return false

    handledGrid[i][j] = 1

    if (grid[i][j] === "0") return false

    bypassVertex(i + 1, j)
    bypassVertex(i - 1, j)
    bypassVertex(i, j + 1)
    bypassVertex(i, j - 1)

    return grid[i][j] === "1"
  }

  const handledGrid = Array(grid.length).fill(0)

  for (let i = 0; i < grid.length; i++) {
    handledGrid[i] = Array(grid[i].length).fill(0)
  }

  let count = 0
  for (let i = 0; i < grid.length; i++) {
    for (let j = 0; j < grid[i].length; j++) {
      count += bypassVertex(i, j)
    }
  }

  return count
}
