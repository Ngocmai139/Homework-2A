def sort_dictionary(dictionary): #this is function sort value of dictionary
    for i in range (1, len(dictionary)):
    	for j in range (len(dictionary)-i):
    		if dictionary[j] > dictionary[j+1]: #compare value of the dictionary
	       		dictionary[j], dictionary[j+1] = dictionary[j+1], dictionary[j]
    return list(dictionary.items())
    
sort_dictionary(dictionary)		
		
Cinput={'Tom' : (5464512, 24) , 'Sara' : (5446987, 32) , 'Mary' : (1557896, 20)}
Coutput = [('Mary', 1557896), ('Tom', 5464512), ('Sara', 5446987)]
(sort_dictionary(Cinput)) == Coutput
