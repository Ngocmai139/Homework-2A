Cinput = {'Tom' : (5464512, 24) , 'Sara' : (5446987, 32) , 'Mary' : (1557896, 20)}
def sort_dictionary(dictionary) :
  return list((k, v[0]) for k, v in sorted(dictionary.items(), key=lambda v: v[1][1]))


Coutput = [('Mary', 1557896), ('Tom', 5464512), ('Sara', 5446987)]

(sort_dictionary(Cinput)) == Coutput

