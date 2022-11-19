def swap_List(lst):
	last = lst[len(lst)-1] 
	mid = lst[int((len(lst)-1)/2)] 
	lst[len(lst)-1] = mid
	lst[int((len(lst)-1)/2)] = last
	for i in range(len(lst)):
		if(lst[i] == mid): #the two functions are to swap between middle and last element
			lst[i] = last
		elif(lst[i] == last): #the two functions are to swap between last and middle element
			lst[i] = mid
		elif(len(lst)%2==1):
			return odd #this is to check the it is odd 
		else(len(lst)%2==0):
            		return even #this is to check if it is even
		return lst

lst1= [12, 35, 5, 9, 56, 24] 
lst2= [3, 35, 11]
lst3 = [3]


