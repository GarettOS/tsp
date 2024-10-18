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
	excluded_cities = [] # Tuples of (source_city, destination city)

	# Main Random Greedy Algorithm
	# Must only have max K steps
	while (curr_steps_taken < K):
		potential_cities = [] # Tuples of (city, cost)

		# Check if all cities have been visited
		if (len(optimal_tour) == num_cities):
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
			if (M[current_city, city] > -1) and (city not in optimal_tour) and ((current_city, city) not in excluded_cities):
				potential_cities.append((city, M[current_city, city])) # City is avalible to go to

		# If there are available cities, choose the one with the least cost
		if (len(potential_cities) > 0):
			# Find the least cost city
			min_cost_city = (-1, float('inf'))
			for city, cost in potential_cities:
				if cost < min_cost_city[1]:
					min_cost_city = (city, cost)
			
			# Visit that city
			current_city = min_cost_city[0]
			optimal_tour.append(min_cost_city[0])
			curr_steps_taken += 1
		else:
			# Backtrack to a random city in the visited cities
			# Select random city thats not the one we are on from our visited
			if (len(optimal_tour) > 1):
				random_city = -1
				while (random_city != current_city):
					# Select random city thats not the current one
					random_city = random.choice(optimal_tour)
					excluded_cities.append((random_city, current_city))
					current_city = random_city
					
					# Cut off the tour back to the random city chosen
					# Find the index of the random city in the tour
					idx = -1
					for i in range(len(optimal_tour)):
						if (optimal_tour[i] == random_city):
							idx = i
					optimal_tour = optimal_tour[:idx]
			else:
				break # Nowhere to backtrack to, 
	if (len(optimal_tour) > 1):
		return optimal_tour, optimal_value
	else:
		print("No tours for this matrix")
		return [], None

