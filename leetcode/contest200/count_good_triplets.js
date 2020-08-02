function countGoodTriplets(arr, a, b, c) {
  const abs = Math.abs;
  let count = 0;

  for (let i = 0; i < arr.length - 2; i++)
    for (let j = i + 1; j < arr.length - 1; j++)
      for (let z = j + 1; z < arr.length; z++) {
        dis1 = abs(arr[i] - arr[j]);
        dis2 = abs(arr[j] - arr[z]);
        dis3 = abs(arr[i] - arr[z]);

        if (dis1 <= a && dis2 <= b && dis3 <= c)
          count++;
      }

  return count;
}
