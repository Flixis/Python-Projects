import subprocess
import random


item = subprocess.Popen(["test.bat", str(random.randrange(0,20))] , 
                         shell=True, stdout=subprocess.PIPE)
for line in item.stdout:
    print(line)