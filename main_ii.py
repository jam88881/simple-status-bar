from tqdm import tqdm
loop = tqdm(total = 2500, position=1, leave=False)
for m in range(2500):
    loop.update(1)
    loop.set_description("processing...".format(m))
loop.close()
