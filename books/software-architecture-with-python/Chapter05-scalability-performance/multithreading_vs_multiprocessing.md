Use multithreading in the following cases:

1. The program needs to maintain a lot of shared states, especially mutable ones.
 A lot of the standard data structures in Python, such as lists, dictionaries, and others, are thread-safe, so it costs
  much less to maintain a mutable shared state using threads than via processes.
2. The program needs to keep a low memory foot-print.
3. The program spends a lot of time doing I/O. Since the GIL is released by threads doing I/O,
 it doesn't affect the time taken by the threads to perform I/O.
4. The program doesn't have a lot of data parallel operations which it can scale across multiple processes



Use multiprocessing in these scenarios:

1. The program performs a lot of CPU-bound heavy computing: byte-code operations, number crunching,
 and the like on reasonably large inputs.
2. The program has inputs which can be parallelized into chunks and whose results can be combined afterwards
 – in other words, the input of the program yields well to data-parallel computations.
3. The program doesn't have any limitations on memory usage, and you are on a modern machine with
 a multicore CPU and large enough RAM.
4. There is not much shared mutable state between processes that need to be synchronized—this
 can slow down the system, and offset any benefits gained from multiple processes.
5. Your program is not heavily dependent on I/O—file or disk I/O or socket I/O.