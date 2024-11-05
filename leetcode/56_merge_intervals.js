/*
https://leetcode.com/problems/merge-intervals/

Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.

Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]

Input: intervals = [[1,4],[4,5]]
Output: [[1,5]]

Constraints:
  1 <= intervals.length <= 104
  intervals[i].length == 2
  0 <= starti <= endi <= 104

*/

/**
 * @param {number[][]} intervals
 * @return {number[][]}
 */
var merge = function (ints) {
  const newInts = []

  ints.sort((int1, int2) => int1[0] - int2[0])

  for (let i = 1; i < ints.length; i++) {
    if (ints[i][0] <= ints[i - 1][1]) {
      ints[i][0] = ints[i - 1][0]
      ints[i][1] = Math.max(ints[i][1], ints[i - 1][1])
    } else {
      newInts.push([ints[i - 1][0], ints[i - 1][1]])
    }
  }

  newInts.push([ints[ints.length - 1][0], ints[ints.length - 1][1]])

  return newInts
}
