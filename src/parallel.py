from multiprocessing import Pool, cpu_count

def parallel_map(func, args):
    num_processes = cpu_count()
    pool = Pool(processes = num_processes)
    results = pool.map(func, args)
    pool.close()
    pool.join()
    return results