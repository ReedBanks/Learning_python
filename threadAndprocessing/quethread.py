from threading import Thread,Lock,current_thread
import time
from queue import Queue

db_val=0

if __name__ == "__main__":
    print ("Starting main")
    q=Queue() # Queue object
    
    # q.put(1)
    # q.put(2)
    # q.put(3)
    
    # q.empty()
    
    # when we are done with a process involving queues
    # q.task_done()
    
    # q.join() # blocks the main thread until all tasks are done
    
    num_threads=10
    
    def worker(q,locker):
        while True:
            value=q.get() #get first value
            
            # processing
            with locker:
                print (f"in {current_thread().name} got {value}")
            q.task_done()
    
    locker=Lock()
    
    for i in range(num_threads):
        thread=Thread(target=worker, args=(q,locker)) 
        thread.daemon = True
        thread.start()
    
    
    # filling queue
    for i in range(1,21):
        q.put(i)
        
    q.join()
    
    print("End of main")
    
# deamon thread => this is a background thread that will die when the main thread dies