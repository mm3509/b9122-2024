import random
import timeit

NUM_RUNS = int(1e4)

def imperative_search(sorted_list, needle):
    # TODO: complete this.
    pass

def recursive_search(sorted_list, needle):
    # TODO: complete this.
    pass

def benchmark(fn, l, needle):
    return fn(l, l[i])
		
durations = []
# Functions are first-class objects, we can iterate over them!
for fn in [imperative_search, recursive_search_wrapper]:
    # TODO: complete this.
    pass

print(durations, durations[0]/durations[1])
