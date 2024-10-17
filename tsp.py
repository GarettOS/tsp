import random
import numpy as np

# Traveling Salesman problem using random greedy search. M = nxn Matrix, K = max # of steps
def tsp(M, K):

	### Starting Variables ### 

	optimal_tour = [] # initialize list where the minimal tour will be stored
	optimal_value = np.inf # stores cost of best tour found
	num_cities = M.shape[0] 
	curr_steps_taken = 0 # count the steps taken from the starting city, must be less than k
	current_city = 0 # represents starting city 1

	# Main Random Greedy Algorithm
	

