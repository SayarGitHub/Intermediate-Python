# The aim here is to use greater amount of CPU cores simultaneously. It may not
# result in faster performance in all cases.

import multiprocessing
import time


def spawn(num):
    print("Spawned {}".format(num))


if __name__ == "__main__":
    start = time.time()
    # The order of numbers is incorrect without p.join(), as they all start on
    # their turn, and don't wait for the previous to finish. If we use p.join(),
    # we will get ordered processes as they wait for previous to finish.
    for i in range(55):
        p = multiprocessing.Process(target=spawn, args=(i,))
        p.start()
        # p.join()
    # for i in range(55):
    #     spawn(i)
    print(time.time() - start)

