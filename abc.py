#Bubble sort in python for Avtivity 02
def bubbleSort(xlist):
    for passnum in range(len(xlist)-1,0,-1):
        for i in range(passnum):
            if xlist[i]>xlist[i+1]:
                temp = xlist[i]
                xlist[i] = xlist[i+1]
                xlist[i+1] = temp

xlist = [14,45,21,70,46,43,27,57,41]
bubbleSort(xlist)
print(xlist)





#Merge sort in python



def mergeSort(nlist):
    if len(nlist) > 1:
        mid = len(nlist) // 2
        left = nlist[:mid]
        right = nlist[mid:]
        mergeSort(left)
        mergeSort(right)
        i = 0
        j = 0
        
        k = 0
        
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
              nlist[k] = left[i]
              i += 1
            else:
                nlist[k] = right[j]
                j += 1
           
            k += 1
            
        while i < len(left):
            nlist[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            nlist[k]=right[j]
            j += 1
            k += 1

nlist = [14,46,43,27,57,41,45,21,70]
mergeSort(nlist)
print(nlist)
