import time 
# Decorator:: timeme #to create a decorator named timeme
def timeme(): 
     
    
    begin = time.time() #this is to start time
    end = time.time() # this is to store end time
    return end-begin 
 
