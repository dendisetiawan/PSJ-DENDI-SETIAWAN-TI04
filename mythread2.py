import time
import threading
T1 = time.perf_counter()
def do_something():
    print ("diam sejenak . . 1 detik ")
    time.sleep(1)
    print ("selesai berdiam . . ")
Threads =[]
for x in range (10):
      T = threading.Thread (target=do_something)
      T.start()
      Threads.Append(T)
for t in Threads :
          t.join()
T2 = time.perf_counter()
print (f"selesai dalam ... {round (T2-T1,2)} detik") 
    
