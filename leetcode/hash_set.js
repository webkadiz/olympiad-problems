class MyHashSet {
  constructor() {
    this._hash = {}
  }

  add(item) {
    this._hash[item] = true
  }

  remove(item) {
    this._hash[item] = false
  }

  contains(item) {
    return Boolean(this._hash[item])
  }
}
