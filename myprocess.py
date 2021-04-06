import time
T1 =time.perf_counter()
def do_something():
 print("diam sejenak... 1 detik ")
time.sleep(1)
print("selesai berdiam . . ")
do_something()
T2= time.perf_counter()
print (f"selesai dalam ... {round(T2-T1,2)} detik")
