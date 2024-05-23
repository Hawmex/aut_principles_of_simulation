import time


def logPerformance(func, *args):
    start_time = time.time()
    result = func(*args)
    end_time = time.time()
    print(f"{end_time - start_time:.2f} seconds")
    return result


# old method
# start_time = time.time()
# LCG.generate(123_457, 7**5, 0, 2**31 - 1, int(1e9))
# end_time = time.time()
# print(f"{end_time - start_time:.2f} seconds")

# new method
# start_time = time.time()
# random_number = lcg_yield(123_457, 7**5, 0, 2**31 - 1)
# for _ in range(int(1e9)):
#     next(random_number)
# end_time = time.time()
# print(f"{end_time - start_time:.2f} seconds")
