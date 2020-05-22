'''
# Caching/memoization: Let's save our work so we don't have
# to recompute it again
# Need some sort of data structure where we'll save the data
# arrays and dictionaries
# If we check our cache and see that the answer we're looking for
# is already in there, just return that answer
# What if the cache doesn't have what we're looking for? Or how
# do we get answers in there?
# There's going to be a first time for calculating an answer, and we're
# going to do it the same way we're currently doing it
# O(n)


import sys
def eating_cookies(n, cache=None):
    # print(n)
    # base case: when there are no more cookies
    if n == 0:
        return 1
    # check for negative n values
    elif n < 0:
        return 0
    # init our cache if we don't have it yet
    # add a case to have us check the cache
    elif cache and cache[n] > 0:
        return cache[n]
    else:
        if not cache:
            # cache = {i: 0 for i in range(n+1)}
            cache = [0 for _ in range(n+1)]
        # we can go ahead and save our answer to the cache
        cache[n] = eating_cookies(
            n-1, cache) + eating_cookies(n-2, cache) + eating_cookies(n-3, cache)
    return cache[n]
    # this represents our recursive case where there still some cookies to be eaten
print(eating_cookies(999))
'''

import sys

# The cache parameter is here for if you want to implement
# a solution that is more efficient than the naive
# recursive solution


def eating_cookies(n, cache=None):
    #Check if cache is None. if so, initialize it to eppty dictionary
    if cache is None:
        cache = {}
    #base case
    if n == 0:
        return 1
    elif n == 1:
        return 1
    elif n == 2:
        return 2
    elif n == 3:
        return 4
    elif cache and cache[n]:
        return cache[n]
    else:
        cache[n] = eating_cookies(
            n-1, cache) + eating_cookies(n-2, cache) + eating_cookies(n-3, cache)

    return cache[n]
# if __name__ == "__main__":
#   if len(sys.argv) > 1:
#     num_cookies = int(sys.argv[1])
#     print("There are {ways} ways for Cookie Monster to eat {n} cookies.".format(
#         ways=eating_cookies(num_cookies), n=num_cookies))
#   else:
#     print('Usage: eating_cookies.py [num_cookies]')


print(eating_cookies(4, {}))
