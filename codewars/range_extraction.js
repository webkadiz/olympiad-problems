function formRange(range) {
  if (range.length < 3) {
    return range[0]
  }
  return range[0] + "-" + range[range.length - 1]
}

function pushToListRange(range, listRange) {
  if (range.length < 3) {
    listRange.push(...range)
  } else {
    listRange.push(formRange(range))
  }
}

function solution(list) {
  const listRange = []
  let curRange = []

  for (let i = 0; i < list.length; i++) {
    const prevEl = curRange.length === 0 ? null : curRange[curRange.length - 1]
    const curEl = list[i]

    if (prevEl !== null && prevEl !== curEl - 1) {
      pushToListRange(curRange, listRange)
      curRange = []
    }

    curRange.push(curEl)
  }

  pushToListRange(curRange, listRange)

  return listRange.join(",")
}
