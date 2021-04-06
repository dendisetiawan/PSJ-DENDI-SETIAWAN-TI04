import concurrent.futures
import time
T1 = time.perf_counter()
def do_something (sec):
    print(f"diam sejenak . . {sec} detik")
    time.sleep (sec)
    return "selesai berdiam . . "
with concurrent.futures.ThreadPoolexecutor () as executor :
    f = executor.submit (do_something,2)
    print (f.result())
T2 = time.perf_counter ()
print("selesai dalam ... {round(T2-T1,2) detik")

import concurrent.futures
import time
T1 = time.perf_counter()
def do_something (sec):
    print (f"diam sejenak . . {sec} detik ")
    time.sleep(sec)
    return "selesai berdiam .. "
with concurrent.futures.threadpoolExecutor () as executor:
      results = [executor.submit (do_something,1) for _ in range (10)]
      for f in  concurrent .futures.as_completed(results):
           print (f.result())
T2 = TIME.Perf_counter()
print ("selesai dalam ... {round (T2-T1,2} detik ")
