import timeit
NUM_RUNS = int(1e7)


# This code is repeated, not DRY, to ensure we evaluate only the time
# taken the reference comparison.

def compare_ref(i):

    a = i
    b = i

    return a is b


def compare_val(i):

    a = i
    b = i

    return a == b


# Compute time taken for each comparison using the functions above and
# a lambda function.
d_42_fun_ref = timeit.Timer(lambda: compare_ref(42)).timeit(number=NUM_RUNS)
d_42_fun_val = timeit.Timer(lambda: compare_val(42)).timeit(number=NUM_RUNS)

# Same computation, but using only a "lambda" or anonymous function.
d_42_lambda_ref = timeit.Timer(lambda: 42 is 42).timeit(number=NUM_RUNS)
d_42_lambda_val = timeit.Timer(lambda: 42 == 42).timeit(number=NUM_RUNS)


# Same for 257.
d_257_fun_ref = timeit.Timer(lambda: compare_ref(257)).timeit(number=NUM_RUNS)
d_257_fun_val = timeit.Timer(lambda: compare_val(257)).timeit(number=NUM_RUNS)

d_257_lambda_ref = timeit.Timer(lambda: 257 is 257).timeit(number=NUM_RUNS)
d_257_lambda_val = timeit.Timer(lambda: 257 == 257).timeit(number=NUM_RUNS)


# To avoid repetion, now I can use eval(), which converts a string into code.
for n in [42, 257]:
    for method in ["fun", "lambda"]:
        # Get a prefix for the variables.
        prefix = "d_%d_%s" % (n, method)
        factor = eval("%s_val / %s_ref" % (prefix, prefix))

        msg = ("For integer %d and using %s, comparing by value takes %2.2f" +
               " longer than reference") % (n, method, factor)
        print(msg)


# Alternatively, I could use this function, which is refactored and
# DRY, but most of the computing time is on exec and eval, not 
def compare(i, op):

    # Compare with exec and eval. Both convert strings into code, and
    # then run the code; exec() is for statements, like assignments;
    # eval() is for expressions, like comparisons.
    exec("a = %d" % i)
    exec("b = %d" % i)
    return eval("a %s b" % op)

        
