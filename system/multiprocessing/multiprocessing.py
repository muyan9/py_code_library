import multiprocessing, time, sys


def test(fn, tname):
    for i in range(fn):
        print(tname, i)
        time.sleep(1)


def addtask():
    n = num_threads-len(l_threads)
    if n > 0:
        print("should add %s tasks" % n)
    for i in range(n):
        if len(l_tasks) == 0: continue
        fn = l_tasks.pop()
        p = multiprocessing.Process(target=test, args=(fn, fn))
        l_threads.append(p)
        p.start()
        #p.join()
    for i in l_threads:
        i.join()


num_threads = 2
l_tasks = []
l_threads = []


if __name__ == '__main__':
    l_tasks = list(range(1, 5))
    l_threads = []

    while 1:
        for t in l_threads:
            if not t.is_alive():
                l_threads.remove(t)
                print("remove task %s" % t)

        if len(l_threads) == 0 and len(l_tasks) == 0:
            break

        addtask()
        time.sleep(5)
