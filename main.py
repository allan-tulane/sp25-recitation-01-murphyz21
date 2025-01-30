"""
CMPS 2200  Recitation 1
"""

### the only imports needed are here
import tabulate
import time
###

def linear_search(mylist, key):
	""" done. """
	for i,v in enumerate(mylist):
		if v == key:
			return i
	return -1


def binary_search(mylist, key):
	""" done. """
	return _binary_search(mylist, key, 0, len(mylist)-1)

def _binary_search(mylist, key, left, right):
	"""
	Recursive implementation of binary search.

	Params:
	  mylist....list to search
	  key.......search key
	  left......left index into list to search
	  right.....right index into list to search

	Returns:
	  index of key in mylist, or -1 if not present.
	"""
	### TODO

	# This is the base case
	if left > right: 
		return -1
	# This determines the middle number
	middle = (left + right) // 2

	# If the middle of the list is the key, return that middle value
	if mylist[middle] == key:
		return middle

	# If the middle of the list is less than the key, search the right half of the list
	elif mylist[middle] > key:
		# Recursive call to keep the whole process going again (but the middle space has shifted)
		return _binary_search(mylist, key, left, middle-1)
	# If the middle of the list is greater than the key, search the left half of the list
	else:
		return _binary_search(mylist, key, middle+1, right)

	###




def time_search(search_fn, mylist, key):
	"""
	Return the number of milliseconds to run this
	search function on this list.

	Note 1: `search_fn` parameter is a function.
	Note 2: time.time() returns the current time in seconds. 
	You'll have to multiple by 1000 to get milliseconds.

	Params:
	  sort_fn.....the search function
	  mylist......the list to search
	  key.........the search key 

	Returns:
	  the number of milliseconds it takes to run this
	  search function on this input.
	"""
	### TODO
	start = time.time() # Takes note of the start time
	search_fn(mylist, key) # Runs the search function
	end = time.time() # Takes note of the end time
	seconds = end - start # Gives us the seconds it took to run the search function
	milliseconds = seconds * 1000 # Puts seconsds into milliseconds
	return milliseconds # Returns the milliseconds it took to run the search function on the list
	
	###

def compare_search(sizes=[1e1, 1e2, 1e3, 1e4, 1e5, 1e6, 1e7]):
	"""
	Compare the running time of linear_search and binary_search
	for input sizes as given. The key for each search should be
	-1. The list to search for each size contains the numbers from 0 to n-1,
	sorted in ascending order. 

	You'll use the time_search function to time each call.

	Returns:
	  A list of tuples of the form
	  (n, linear_search_time, binary_search_time)
	  indicating the number of milliseconds it takes
	  for each method to run on each value of n
	"""
	### TODO
	# Creates a list for us to add the tuples into 
	results = []
	# For loop that runs through the input size list
	for size in sizes:
		# Makes the sizes an int and easier to work with
		n = int(size)
		# Creates a list of numbers from 0 to n-1
		mylist = list(range(n))
		# Creates the linear_serach_time variables with the required parameters
		linear_search_time = time_search(linear_search, mylist, -1)
		binary_search_time = time_search(binary_search, mylist, -1)
		# Adds the result tuples from the linear_search_time and binary_search_time into the results list
		results.append((n, linear_search_time, binary_search_time))
	return results

	###

def print_results(results):
	""" done """
	print(tabulate.tabulate(results,
							headers=['n', 'linear', 'binary'],
							floatfmt=".3f",
							tablefmt="github"))


