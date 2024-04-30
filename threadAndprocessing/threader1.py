from threading import Thread,Lock
import time

db_values =0

def increase(lock):
    global db_values # modifying the global db_values
    lock.acquire()
    
    # get value from db_values and store it locally
    local_cpy=db_values
    
    # process values
    local_cpy += 1
    time.sleep(0.1)
    db_values=local_cpy
    
    lock.release()

if __name__ == "__main__":
    print("Starting ",db_values)
    locker=Lock() #lock object
    thread1=Thread(target=increase, args=(locker,)) #comma bcos we want python to know that that args is a tuple
    thread2=Thread(target=increase,args=(locker,))
    
    thread1.start()
    thread2.start()
    
    thread1.join()
    thread2.join()
    
    print("end value: ",db_values)
    
    print("end main")
    
    
    # race condition happens when 2 or more threads try to modify the same value/variable at the same time
    #  to prevent race condition we use the lock object