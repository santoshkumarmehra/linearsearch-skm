def linearsearch(arr,ele,n):
	for i in range(n):
		if arr[i]==ele:
			return i
	return -1


arr=[1,5,10,15,16,30,35]
n=len(arr)
ele=3
res=linearsearch(arr,ele,n)
print(res)
