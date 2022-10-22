// Definition for a Node.
function Node(val, neighbors) {
    this.val = val === undefined ? 0 : val
    this.neighbors = neighbors === undefined ? [] : neighbors
}

/**
 * @param {Node} node
 * @return {Node}
 */
var cloneGraph = function (node, childFunc) {
    if (!childFunc) {
        cloneGraph.nodes = []
    }

    if (!node) return null

    if (cloneGraph.nodes[node.val]) return cloneGraph.nodes[node.val]

    const clonedNode = new Node(node.val)

    cloneGraph.nodes[clonedNode.val] = clonedNode

    for (const neighbor of node.neighbors) {
        const clonedNeighbor = cloneGraph(neighbor, true)

        clonedNode.neighbors.push(clonedNeighbor)
    }

    return clonedNode
}
