def findMedianSortedArrays(a,b):
    if len(a) > len(b):
        a,b=b,a 
    
    lenA, lenB=len(a), len(b)

    low,high=0,lenA 

    while low<=high: 
        splitA=(low+high)//2
        splitB=(lenA+lenB+1)//2-splitA 