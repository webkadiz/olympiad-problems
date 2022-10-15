class Trie {
    constructor() {
        this.tree = {}
    }

    insert(word) {
        let curTree = this.tree

        for (const char of word) {
            if (!curTree[char]) curTree[char] = {}

            curTree = curTree[char]
        }

        curTree.value = word
    }

    search(word) {
        let curTree = this.tree

        for (const char of word) {
            if (!curTree[char]) return false

            curTree = curTree[char]
        }

        return "value" in curTree
    }

    startsWith(prefix) {
        let curTree = this.tree

        for (const char of prefix) {
            if (!curTree[char]) return false

            curTree = curTree[char]
        }

        return true
    }
}

const trie = new Trie()

trie.insert("apple")
trie.insert("app")
trie.insert("")
console.log(trie.search("apple")) // true
console.log(trie.search("app")) // false
console.log(trie.search("ttt")) // false
console.log(trie.startsWith("app")) // true
console.log(trie.search("app")) // true
console.log(trie.search("")) // true
console.log(trie.startsWith("")) // true
