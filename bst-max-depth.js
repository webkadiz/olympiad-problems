/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */

const height = (node, curHeight = 0) => {
    if (!node) return curHeight

    return Math.max(
        height(node.left, curHeight + 1),
        height(node.right, curHeight + 1)
    )
}

/**
 * @param {TreeNode} root
 * @return {number}
 */
var maxDepth = function(root) {
    return height(root)
};