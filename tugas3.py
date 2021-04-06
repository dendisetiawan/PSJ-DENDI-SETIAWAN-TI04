import subprocess
p=subprocess.Popen(["dmesg"],stdout=subprocess.PIPE)
print(p.stdout.readline())
print(p.stdout.readline())
print(p.stdout.readlines())
p.stdout.close()

import subprocess
p1=subprocess.Popen(["dmesg"],stdout=subprocess.PIPE)
P2=subprocess.Popen(["grep","disk"],stdin=p1.stdout,stdout=subprocess.PIPE)
p1.stdout.close()
output=p2.communicate()[0]
print(output)
