import time
from datetime import datetime
from tqdm import tqdm
loop = tqdm(total = 4, position=0, leave=False)
now = datetime.now()
current_time = now
print("Start Time = ", current_time)
for k in range(4):

    subloop = tqdm(total = 2500, position=1, leave=False)
    for m in range(2500):
        subloop.update(1)
        sub_description = str(m+1) + "/2500"
        subloop.set_description(sub_description)
    subloop.close()
    loop.update(1)
    description = str(k+1) + "/2500"
    loop.set_description(description)
    time.sleep(1)
loop.close()

now = datetime.now()
current_time = now
print("End Time = ", current_time)
