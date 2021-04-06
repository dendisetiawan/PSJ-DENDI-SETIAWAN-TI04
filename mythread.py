import time
import threading
T1 = time.perf_counter()
def do_something():
    print ("diam sejenak . . 1 detik")
    time.sleep(1)
    print("selesai berdiam . .")
    p1 = threading.Thread(target=do_something)
    p2 = threading.Thread(target=do_something)

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    T2 = time.perf_counter()
    print(f"selesai dalam ... {round(T2-T1,2)} detik")
