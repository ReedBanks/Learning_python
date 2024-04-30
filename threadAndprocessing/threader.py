
from threading import Thread


if __name__ == "__main__":
    threads = []
    num_thread=10

def squares():
    for i in range(100):
        i*i
    


# create thread
for i in range(num_thread):
    p=Thread(target=squares)
    threads.append(p)
    
    
# start
for p in threads:
    p.start()
    
    
# join thread
#threads live in the same memory


for p in threads: 
    p.join()
    
print("end of threading")