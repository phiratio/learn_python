Concurrent futures vs Multi-processing:
    Concurrent futures provide an elegant way to parallelize your tasks using either a thread or process pool executor.
Hence, it is ideal if the underlying application has similar scalability metrics with either threads or processes,
since it's very easy to switch from one to the other as we've seen in a previous example. Concurrent futures can be
chosen also when the result of the operation needn't be immediately available. Concurrent futures is a good option when
the data can be finely parallelized and the operation can be executed asynchronously, and when the operations involve
simple callables without requiring complex synchronization techniques.
    Multi-processing should be chosen if the concurrent execution is more complex, and not just based on data
parallelism, but has aspects like synchronization, shared memory, and so on. For example, if the program requires
processes, synchronization primitives, and IPC, the only way to truly scale up then is to write a concurrent program
using the primitives provided by the multiprocessing module. Similarly when your muti-threaded logic involves simple
parallelization of data across multiple tasks, one can choose concurrent futures with a thread pool. However if there is
a lot of shared state to be managed with complex thread synchronization objects – one has to use thread objects and
switch to multiple threads using threading module to get finer control of the state.

Asynchronous I/O vs Threaded concurrency:
    When your program doesn't need true concurrency (parallelism), but is dependent more on asynchronous processing and
callbacks, then asyncio is the way to go. Asyncio is a good choice when there are lot of waits or sleep cycles involved
in the application, such as waiting for user input, waiting for I/O, and so on, and one needs to take advantage of such
wait or sleep times by yielding to other tasks via co-routines. Asyncio is not suitable for CPU-heavy concurrent
processing, or for tasks involving true data parallelism.