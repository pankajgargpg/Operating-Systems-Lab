import os 

print("Before Fork")
print("Current PID:", os.getpid())

pid = os.fork()

if pid == 0:
    print("\nChild Process")
    print("Child PID : " , os.getpid())
    print("Parent PID : " , os.getpid())
else :
    os.wait()

    print("\n Parent Process")
    print("\n Parent PID : "  , os.getpid())
    print("\n Child PID : " , pid)
    