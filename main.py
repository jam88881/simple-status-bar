import time
from tqdm import tqdm
loop = tqdm(total = 4, position=0, leave=False)
for k in range(4):

    #print("substart")
    subloop = tqdm(total = 2500, position=1, leave=False)
    for m in range(2500):
        subloop.update(1)
        description = str(m)/"2500"
        subloop.set_description(description)
    subloop.close()
    loop.update(1)
    loop.set_description("Processing...".format(k))
    time.sleep(1)
loop.close()
