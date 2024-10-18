import random
import numpy as np

# Traveling Salesman problem using random greedy search. M = nxn Matrix, K = max # of steps
def tsp(M, K):

	# Starting Variables
	optimal_value = float('inf') # stores cost of best tour found
	optimal_tour = []
	num_cities = M.shape[0] 
	curr_steps_taken = 0 # count the steps taken from the starting city, must be less than k
	current_city = 0 # set as starting city
	tour = [0]
	excluded_cities = [] # Tuples of (source_city, destination city)

	# Main Random Greedy Algorithm
	# Must only have max K steps
	while (curr_steps_taken < K):
		potential_cities = [] # Tuples of (city, cost)

		# Check if all cities have been visited
		if (len(tour) == num_cities):
			# See if we can return back to the original city
			if (M[current_city, 0] > 0):
				tour.append(0) # Add the starting city aat the end of the tour

				# Calculate the cost of the tour
				cost = 0
				for i in range(len(tour) - 1):
					cost += M[tour[i], tour[i+1]]

				# Check if this tours cost is the minimum so far
				if cost < optimal_value:
					# If it is, update the best values
					optimal_value = cost
					optimal_tour = tour[:]

				break # finished

		# Find the next best city to visit
		for city in range(num_cities):
			# If there is a path between current city and the next, and we haven't vistited or excluded the next city
			if (M[current_city, city] > 0) and (city not in tour) and ((current_city, city) not in excluded_cities):
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
			tour.append(min_cost_city[0])
			curr_steps_taken += 1
		else:
			# Backtrack to a random city in the visited cities
			# Select random city thats not the one we are on from our visited
			if (len(tour) > 1):

				# Filter to look for cities besides the current city
				available_cities = []
				for city in tour:
					if city != current_city:
						available_cities.append(city)

				# Select a random city from the filtered list
				random_city = random.choice(available_cities)
			
				# Find the index of the random city in the tour
				idx = -1
				for i in range(len(tour)):
					if (tour[i] == random_city):
						idx = i 

				excluded_cities.append((random_city, idx+1))

				# Cut off the tour back to the random city chosen
				tour = tour[:idx+1]
				current_city = random_city
			else:
				break # Nowhere to backtrack to, 
	if (len(optimal_tour) > 1):
		return optimal_tour, optimal_value
	else:
		print("No tours for this matrix")
		return [], None

