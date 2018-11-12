from collections import deque

def changeRoot(parent, newRoot):
	# make an undirected graph of all the connections
	n = len(parent)

	graph = {}
	for i in range(n):
		graph[i] = []
	
	for i in range(n):
		if i != parent[i]:
			graph[i].append(parent[i])
			graph[parent[i]].append(i)
    
	# make a new array (to be filled in)     
	arr = [None] * n

	# start by filling in the root
	arr[newRoot] = newRoot

	# make a line of the nodes who might need to be counted as parents 
	parents_queue = deque([newRoot])

	# while we still have stuff to fill in
	while None in arr:
		# get the next potential parent in line, p
		p = parents_queue.popleft()
		# and add the nodes p is linked to to the end of the line of potential parents
		parents_queue.extend(graph[p])
        
		# claim any node p is linked to that doesn't already have a parent as p's child
		for child in graph[p]:
			if arr[child] == None:
				arr[child] = p
				
	return arr
