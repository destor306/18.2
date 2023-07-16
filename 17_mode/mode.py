def mode(nums):
    """Return most-common number in list.

    For this function, there will always be a single-most-common value;
    you do not need to worry about handling cases where more than one item
    occurs the same number of times.

        >>> mode([1, 2, 1])
        1

        >>> mode([2, 2, 3, 3, 2])
        2
    """
    temp = {}
    for ele in nums:
        temp[ele] = temp.get(ele, 0) +1
    max_val = max(temp.values())
    
    for k,v in temp.items():
        if v == max_val:
            return k