# Import time
import time

# defining a decorator
def timeme(func):
    def wrapper():
        # Store start time
        begin = time.time()
        
        # Store end time
        end = time.time()
    
        # Print total time taken
        print("Total time X ",end - begin)
        func()
    return wrapper
  
 


