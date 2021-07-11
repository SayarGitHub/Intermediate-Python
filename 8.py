from multiprocessing import Pool
import time


def job(number):
    return number * 2


# A pool of processes available to distribute the workload
if __name__ == "__main__":
    start = time.time()
    p = Pool(processes=20)
    data = p.map(job, range(40))
    data2 = p.map(job, range(100, 200))
    p.close()
    # data = []
    # for i in range(40):
    #     data.append(job(i))
    print(data)
    print(data2)
    print(time.time() - start)
