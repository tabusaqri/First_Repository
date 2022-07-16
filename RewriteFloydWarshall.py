# Python Program for Rewrite Floyd Warshall Algorithm for Practical Programming Assignment.

# Importing sys module for various functions and variables.

import sys

# Define a large value to be used for vertices that are not connected to each other using sys.maxsize function.
INF = sys.maxsize

# Floyd Warshall Algorithm
def RewritefloydWarshall(graph):

	# creating the solution matrix that very same size as the input graph matrix

	""" distance[][] is the output matrix with the shortest
	distances between each pair of vertices """

	distance = list(map(lambda i: list(map(lambda j: j, i)), graph))

	""" Add all vertices to the set of intermediate vertices one by one """

	# Loop for n number of vertices or nodes in the graph
	for k in range(len(distance)):

		# One by one, select all vertices as sources.
		for i in range(len(distance)):

			# Select all vertices as the destination for the previously selected source
			for j in range(len(distance)):

				# If vertex k is on the shortest path from i to j, then the value of distance[i][j] should be updated.
				distance[i][j] = min(distance[i][j],
								distance[i][k] + distance[k][j]
								)
	RewritePrintSolution(distance)


# Function to print the solution and the output matrix
def RewritePrintSolution(distance):
	print("The matrix below displays the shortest distances between each pair of vertices:")
	for i in range(len(distance)):

		for j in range(len(distance)):
			if(distance[i][j] == INF):
				prin("%7s" % ("INF"),end=" ")
			else:
				if j == 0:
					print("[""%7d\t" % (distance[i][j]), end=' ')
				else:
					print("%7d\t" % (distance[i][j]), end=' ')
				if j == len(distance) - 1:
					print("]")


graph = [[0, 8, INF, 1],
		[INF, 0, 1, INF],
		[4, INF, 0, INF],
		[INF, 2, 9, 0]
		]
# Print the solution

RewritefloydWarshall(graph)


