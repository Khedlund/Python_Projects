# Q naming for this function could be better? Nplus1? or n? instead of next
# @author Katharine Hedlund
import math

def newton(f, f_pr, x_0, tol, max_iter):
    # Implements the Newton-Raphson Method, which approximates the roots of a differentiable real-valued function.
    # Parameters:
    #   f is a function that implements f(x). Assume that f takes a single numerical argument and returns a single numerical value.
    #   f_pr is a function that implements f′(x). Assume that f_pr takes a single numerical argument and returns a single numerical value.
    #   x_0 is an initial guess at a root.
    #   tol is the absolute tolerance used to end the recurrence.
    #   max_iter is the maximum number of recurrences.
    # Returns: next, which results from either tol or max iter being reached, as described above.

    next = x_0 - (f(x_0)/f_pr(x_0))

    for i in range(max_iter-1):
        current = next
        next = next - (f(next)/f_pr(next))

        if math.fabs(next-current) < tol:
            return next
    return next
