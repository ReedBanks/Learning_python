# process               ||            thread
# instance of a program  || is an entity of a process
# takes advantage of multiple cpu and memory || great for I/O bound tasks
# starting a process is slower than starting a thread || faster start time
# heavy programs  || lightweight programs
# killable || not killable 

#   GIL( global interpreter lock )
#  is a lock in python that allows only one thread to run at a time
# Avoid :
#       -use multiprocessing


from multiprocessing import Process
import os


processes = []
num_processes=os.cpu_count()

def squares():
    for i in range(100):
        i*i
    


# create process
for i in range(num_processes):
    p=Process(target=squares)
    processes.append(p)
    
    
# start
for p in processes:
    p.start()
    
    
# join processes
# waiting for all processes to finish by blocking the main thread when it contains a process

for p in processes: 
    p.join()
    
print("end of process")