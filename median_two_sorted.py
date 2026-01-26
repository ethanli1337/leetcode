def findMedianSortedArrays(a,b):
    if len(a) > len(b):
        a,b=b,a 
    
    lenA, lenB=len(a), len(b)

    low,high=0,lenA

    while low<=high: 
        splitA=(low+high)//2 
        splitB=(lenA+lenB+1)//2-splitA 


        maxLeftA=float('-inf') if splitA==0 else a[splitA-1]
        minRightA=float('inf') if splitA==lenA else a[splitA]

        maxLeftB=float('-inf') if splitB==0 else b[splitB-1]
        minRightB=float('inf') if splitB==lenB else b[splitB]

        if maxLeftA <= minRightB and maxLeftB <= minRightA:
            if (lenA+lenB)%2==0:
                return (max(maxLeftA, maxLeftB) + min(minRightA,minRightB))/2 
            else:
                return max(maxLeftA,maxLeftB)
        elif maxLeftA>minRightB:
            high=splitA-1 
        else:
            low=splitA+1
        

           
           

a=[1,3,5]
b=[2,4,6]
print(findMedianSortedArrays(a,b))

        