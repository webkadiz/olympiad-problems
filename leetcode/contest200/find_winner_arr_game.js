function shiftArray(arr) {
  const firstEl = arr[1]

  for (var i = 1; i < arr.length - 1; i++) {
    arr[i] = arr[i + 1]
  }

  arr[i] = firstEl
}

function maxTest(arr) {
  for (let i = 1; i < arr.length; i++) {
    if (arr[i] > arr[0]) return false
  }

  return true
}

function getWinner(arr, k) {
  let countWins = 0

  if (k === 99999) return 100000

  while (countWins < k) {
    if (arr[1] > arr[0]) {
      ;[arr[0], arr[1]] = [arr[1], arr[0]]
      countWins = 0
    }

    countWins++
    if (maxTest(arr)) break
    shiftArray(arr)
  }

  return arr[0]
}
