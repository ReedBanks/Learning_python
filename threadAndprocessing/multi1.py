from multiprocessing import Process,Value,Array,Lock
import os
import time

def multipyBy10(num,locker):
        for i in range(100):
            time.sleep(0.01)
            locker.acquire()
            num.value=(num.value*10)+1
            locker.release()
            return num.value

def multipyBy10_arr(num,locker):
        for i in range(100):
            time.sleep(0.01)
            
            for i in range(len(num)):
                locker.acquire()
                num[i] +=2
                locker.release()
            


if __name__ == '__main__':
    print("Starting")
    
    process=[]
    num_processes=os.cpu_count()
    locker=Lock()
    
    # sharing data between processes using the shared memory interprocess communication method
    # we can use a value or array
    
    shared_value=Value('i',0) # take data type and start value as argument
    print("Number at beginning of process : {}".format(shared_value.value))
    
    p1=Process(target=multipyBy10,args=(shared_value,locker,))
    p2=Process(target=multipyBy10,args=(shared_value,locker,))
    
    p1.start()
    p2.start()
    
    p1.join()
    p2.join()
    
    print(f"Number at end of process : {shared_value.value}")   
    
    # end of sharing variable   
    
    # sharing array
    
    print("starting processes 3&4")
    
    shared_array=Array('d',[0.0,1.1,2.2,3.3,4.4])
    print("Array at beginning of process : {}".format(shared_array[:]))
    
    p3=Process(target=multipyBy10_arr,args=(shared_array,locker,))
    p4=Process(target=multipyBy10_arr,args=(shared_array,locker,))
    
    p3.start()
    p4.start()
    
    p3.join()
    p4.join()
    
    print(f"Array at end of process : {shared_array[:]}")   
    
    
    
    
    
    print("End of main")
