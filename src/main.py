from typing import List

def linear_search(arr: List[int],x: int):
    """
    pre: True

    post: (x in arr) == __return__
    """
    if len(arr)==0:
        return False;
    for y in arr:
        if x==y:
            return True;
    return False;

def binary_search(arr: List[int], x: int):
    """
    pre: forall([arr[i+1]>=arr[i] for i in range(len(arr)-1)])
    post: __return__>=-1 and __return__ < len(arr) and ((x in arr)==(__return__!=-1))
    """
    return binary_search_primitive(arr,0,len(arr)-1,x)

def binary_search_primitive(arr: List[int], low: int, high: int, x: int):
    """
    pre: low>=0 and high<len(arr) and forall([arr[i+1]>=arr[i] for i in range(len(arr)-1)])
    post: __return__>=-1 and __return__ < len(arr)
    """
    if len(arr)==0:
        return -1;
    # Check base case
    if high >= low:

        mid = (high + low) // 2

        # If element is present at the middle itself
        if arr[mid] == x:
            return mid

        # If element is smaller than mid, then it can only
        # be present in left subarray
        elif arr[mid] > x:
            return binary_search_primitive(arr, low, mid - 1, x)

        # Else the element can only be present in right subarray
        else:
            return binary_search_primitive(arr, mid + 1, high, x)

    else:
        # Element is not present in the array
        return -1


if __name__=='__main__':
    print(binary_search_primitive([0], 0, 0, 0))
