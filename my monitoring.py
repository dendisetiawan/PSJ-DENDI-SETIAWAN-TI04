import time
T1 =time.perf_counter()
def do_something():
 print("mulai monitor ... 1 detik ")
time.sleep(1)
print("mulai monitor . . ")
do_something()
T2= time.perf_counter()
print (f"selesai dalam ... {round(T2-T1,3)} detik") ("192.168.1.1  Down ")
print(f"192.168.1.2 up")
print(f"192.168.1.3 down")
print(f"8.8.8.8 up")
print(f"8.8.4.4 down")

