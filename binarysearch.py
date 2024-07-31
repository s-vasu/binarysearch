
def binary_search(lst,low,high,key):

    if(not (low>high)):
        m = (low+high)//2
        if lst[m]==key:
            return True
        elif key < lst[m]:
            high = m-1
            return binary_search(lst,low,high,key)
        else:
            low = m+1

            return binary_search(lst,low,high,key)
    
    return False

lst = [1,2,3,4]
n = len(lst)-1
print(binary_search(lst,0,n,1))

        