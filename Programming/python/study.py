# import threading
# import time

# counter = 10
# mutex = threading.RLock()

# def worker1():
#     global counter
#     for i in range(5):
#         mutex.acquire()
#         counter += 1
#         print("Thread 1", counter)
#         time.sleep(1)
#         mutex.release()

# def worker2():
#     global counter
#     for i in range(10):
#         mutex.acquire()
#         counter -= 1
#         print("Thread 2", counter)
#         time.sleep(2)
#         mutex.release()

# if __name__ == "__main__":
#     t1 = threading.Thread(target=worker1)
#     t2 = threading.Thread(target=worker2)
#     t1.start()
#     t2.start()
#     t1.join()
#     t2.join()
#     print("Counter value:", counter)



# import time
# def countdown(n):
#     while n > 0:
#         print('T-minus', n)
#         n -= 1
#         time.sleep(5)
# from threading import Thread
# t = Thread(target = countdown, args =(10, ))
# t.start()



# import time 
# from threading import Thread
# class CountdownTask:
#     def __init__(self):
#         self._running = True
        
        
#     def terminate(self):
#         self._running = False
        
    
#     def run(self,n):
#         while self._running and n > 0:
#             print('T-minus',n)
#             n-=1
#             time.sleep(1)
            
            
# c = CountdownTask()
# t = Thread(target = c.run, args =(10, ))
# t.start()

# t.join()

# print("Waited\n")

# c.terminate()




# import threading
# event = threading.Event()
# def worker1():
#     print("Worker 1 started\n")
#     event.wait()
#     print("Worker 1 completed\n")

# def worker2():
#     print("Worker 2 started\n")
#     threading.Timer(3, event.set).start()
#     print("Worker 2 completed\n")

# if __name__ == "__main__":
#     t1 = threading.Thread(target=worker1)
#     t2 = threading.Thread(target=worker2)
#     t1.start()
#     t2.start()
#     t1.join()
#     t2.join()