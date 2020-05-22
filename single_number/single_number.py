'''
Input: a List of integers where every int except one shows up twice
Returns: an integer
'''
def single_number_with_arr(nums):
    no_dups = []

    for x in nums:
        if x not in no_dups:
            no_dups.append(x)
        else:
            no_dups.remove(x)
    return no_dups[0]
def single_number(nums):
    # keep track of the counts of how many times we've seen a particular number
    # dictionaries are better at being searched
    counts = {}

    # O(n)
    # Loop through nums to tally up how many times we've seen each number
    for x in nums:
        if x in counts:
            del counts[x]
        else:
            counts[x] = 1

    # loop through all of the key-value pairs in counts to find the one pair 
    # whose value is 1
    # o(1)
    for num in counts:
        if counts[num] == 1:
            return num


if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]

    print(f"The odd-number-out is {single_number(arr)}")