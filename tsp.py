import random
import numpy as np

# Traveling Salesman problem using random greedy search. M = nxn Matrix, K = max # of steps
def tsp(M, K):

	# Starting Variables
	optimal_value = float('inf') # stores cost of best tour found
	num_cities = M.shape[0] 
	curr_steps_taken = 0 # count the steps taken from the starting city, must be less than k
	current_city = 0 # set as starting city
	optimal_tour = [current_city]
	visited_cities = [current_city]
	excluded_cities = [] # Tuples of (source_city, destination city)

	# Main Random Greedy Algorithm
	# Must only have max K steps
	while (curr_steps_taken < K):
		potential_cities = [] # Tuples of (city, cost)

		# Check if all cities have been visited
		if (len(visited_cities) == num_cities):
			# See if we can return back to the original city
			if (M[current_city, 0] > -1):
				optimal_tour.append(0) # Add the starting city aat the end of the tour

				# Calculate the cost of the tour
				cost = 0
				for i in range(len(optimal_tour) - 1):
					cost += M[optimal_tour[i], optimal_tour[i+1]]

				# Check if this tours cost is the minimum so far
				if cost < optimal_value:
					# If it is, update the best values
					optimal_value = cost
					break # finished finding tour

		# Find the next best city to visit
		for city in range(num_cities):
			# If there is a path between current city and the next, and we haven't vistited or excluded the next city
			if (M[current_city, city] > -1) and (city not in visited_cities) and ((current_city, city) not in excluded_cities):
				potential_cities.append((city, M[current_city, city])) # City is avalible to go to

		# If there are available cities, choose the one with the least cost
		if (len(potential_cities) > 0):
			# Find the least cost city
			min_cost_city = (-1, float('inf'))
			for city, cost in potential_cities:
				if cost < min_cost_city[1]:
					min_cost_city = (city, cost)
			
			# Visit that city
			visited_cities.append(min_cost_city[0])
			current_city = min_cost_city[0]
			optimal_tour.append(min_cost_city[0])
			curr_steps_taken += 1
		else:
			break

	return optimal_tour, optimal_value

def main():
	# Expect 0,1,3,2,0 with cost 7 (no backtracking necessary)
	M41 = np.array(
	[[-1, 1, 2, 5],
	[1, -1, 2, 1],
	[2, 2, -1, 3],
	[5, 1, 3, -1]])

	output = tsp(M41, 50)
	print(output)

main()

