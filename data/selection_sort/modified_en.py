def selection_sort(list):
    """
    Sorts a list using the selection sort algorithm.

    Principle:
    Every iteration, the smallest element from the unsorted part of the
    list is selected and swapped with the current element.

    list: List of elements to sort
    return: Sorted list (in-place sorting)

    Complexity:
    - Time: O(n^2)
    - Space: O(1) (in-place sorting)
    """

    n = len(list)

    # Go through the entire list
    for i in range(n):
        # Suppose that the minimum is at the beginning of the unsorted zone
        
        min_index= i

        # Search for the smallest element in the rest of the list
        for j in range(i + 1, n):
            if list[j] < list[min_index]:
                min_index = j

        # Swap if a smaller element was found
        if min_index != i:
            list[i], list[min_index] = list[min_index], list[i]

    return list