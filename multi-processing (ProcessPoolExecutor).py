from concurrent.futures import ProcessPoolExecutor

with ProcessPoolExecutor(max_workers = 2) as pool:
    pool.submit(#something here)
    pool.submit(  # something here)