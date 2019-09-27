import threading
event = threading.Event()

def fire():
    print('Firing eveent')
    event.set()


def listen():
    event.wait()
    print('Event fireed')



t1 = threading.Thread(target=fire)
t2 = threading.Thread(target=listen)
t2.start()  # listener first
t1.start()
