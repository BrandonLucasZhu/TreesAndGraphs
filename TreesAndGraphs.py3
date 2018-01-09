

#Uses backtracking until it finds a solution
def recursive_dfs(graph, start, end, path = []):

	path = path + [start]
	if start == end:
		return path
	if not graph.has_key(start):
		return None
	for node in graph[start]:
		if node not in path:
			newpath = BacktrackingFindPath		
			if newpath: 
				return newpath
	return None			

def iterative_dfs(graph, start, path = [])

	q = start
	while q:
		v = q.pop(0)
		if v not in path:
			path = path + [v]
			q = graph[v] + q
	return path		


def bfs (graph, start, end):
	todo = [[start, [start]]]
	while 0 < len(todo):
		(node, path) = todo.pop(0)
		for next_node in graph[node]:
			if next_node in path:
				continue
			elif next_node == end:
				yield path + [next_node]
			else:
				todo.append([next_node, path + [next_node]])

def bi_directional_search ():
	

if __name__ == "__main__": 

	graph = {'A': ['B', 'C'], 
			'B': ['C','D'],
			'C':['D'],
			'D':['C'],
			'E':['F'],
			'F':['C']}

