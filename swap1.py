def swapList(input_list) :
  #this is to check the len of the list
  if len(input_list) == 1:
    return input_list
  #the two functions are to define the last and middle element to get
  last = input_list[len(input_list)-1]
  mid = input_list[int((len(input_list)-1)/2)]
  #the two functions are to swap between middle and last element
  input_list[len(input_list)-1] = mid
  input_list[int((len(input_list)-1)/2)] = last
  return input_list
  


