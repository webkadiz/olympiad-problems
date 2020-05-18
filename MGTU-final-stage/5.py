
def bin_search(arr, el):
	left = -1
	right = len(arr)

	while right - left > 1:
		middle = (left + right) // 2

		if arr[middle] < el:
			left = middle
		else:
			right = middle
	
	return left+1


def update_tree(node, node_height, child, graph_parents, vertex_data):
	if node > child:
		height_side = 0
	else:
		height_side = 1
	
	vertex_data[node][height_side] = node_height

	height1 = vertex_data[node][0]
	height2 = vertex_data[node][1]
	diff_height = abs(height1 - height2)

	real_height = max(height1, height2)
	vertex_data[node][2] = real_height

	if diff_height > 1:
		vertex_data[node][3] = 'unbalanced'
	else:
		vertex_data[node][3] = 'balanced'

	if graph_parents.get(node):
		parent = graph_parents[node]
		update_tree(parent, real_height + 1, node, graph_parents, vertex_data)
	else:
		return
	

def init_node(node, vertex_data):
	vertex_data[node] = [1, 1, 1, 'balanced']


sorted_vertex = []

graph_parents = {}
vertex_data = {}

root = node = int(input())
while True:

	init_node(node, vertex_data)

	node_idx = bin_search(sorted_vertex, node)
	sorted_vertex.insert(node_idx, node)

	parent = 0
	parent1 = parent2 = 0
	parent1_height = parent2_height = -1
	if node_idx - 1 >= 0:
		parent1 = sorted_vertex[node_idx - 1]
	if node_idx + 1 < len(sorted_vertex):
		parent2 = sorted_vertex[node_idx + 1]

	if parent1:
		parent1_height = vertex_data[parent1][1]
	if parent2:
		parent2_height = vertex_data[parent2][0]
	
	if parent1_height < parent2_height and parent1_height > -1:
		parent = parent1
	elif parent2_height > -1:
		parent = parent2


	if parent:
		if node != parent:
			graph_parents[node] = parent

		update_tree(parent, 2, node, graph_parents, vertex_data)

	
	node = input()
	if node == '.': break
	node = int(node)

is_balanced = True
for data in vertex_data.values():
	if data[3] == 'unbalanced':
		is_balanced = False
		break

if is_balanced:
	print('YES')
else:
	print('NO')

print(vertex_data[root][2])