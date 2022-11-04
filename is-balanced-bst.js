// Definition for a binary tree node.
function TreeNode(val, left, right) {
    this.val = val === undefined ? 0 : val
    this.left = left === undefined ? null : left
    this.right = right === undefined ? null : right
}

const height = (node, curHeight = 0) => {
    if (!node) return curHeight

    return Math.max(
        height(node.left, curHeight + 1),
        height(node.right, curHeight + 1)
    )
}

/**
 * @param {TreeNode} root
 * @return {boolean}
 */
var isBalanced = function (root) {
    if (!root) return true

    return Math.abs(height(root.left) - height(root.right)) <= 1 && isBalanced(root.left) && isBalanced(root.right)
}

//           1
//      2          3
//   4     5     6
// 8
const tree1 = new TreeNode(
    1,
    new TreeNode(2, new TreeNode(4, new TreeNode(8)), new TreeNode(5)),
    new TreeNode(3, new TreeNode(6))
)

//              1
//         2            2
//    3                        3
// 4                                  4

const tree2 = new TreeNode(
    1,
    new TreeNode(2, new TreeNode(3, new TreeNode(5))),
    new TreeNode(2, null, new TreeNode(3, null, new TreeNode(4)))
)
console.log(isBalanced(tree1)) // true
console.log(isBalanced(tree2)) // false
console.log(isBalanced()) // true
