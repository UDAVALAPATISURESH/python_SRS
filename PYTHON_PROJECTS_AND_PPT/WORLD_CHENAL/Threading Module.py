# class Apple:
#     def runs(self):
#         for rons in range(10):
#             print("Hello suresh")
#
#     def run(self):
#         for run in range(20):
#             print("Good Morning")
# c = Apple()
# c.run()
# c.runs()

# ________________________________________________________________________________________________________________________________

# import time
#
# class App:
#     def run(self):
#         for run in range(10):
#             time.sleep(2)                    # *** time.sleep
#             print("Hello sures Good Morning!")
# class Apps:
#     def run(self):
#         for run in range(20):
#             print("my name is a suresh")
# c = App()
# b = Apps()
# c.run()
# print("")
# b.run()

# ____________________________________________________________________________________________________________________________________

# import time
# class Apples:
#     def run(self):
#         for rum in range(10):
#             time.sleep(1)
#             print("Hello loves")
# class Apples1:
#     def run(self):
#         for run in range(10):
#             time.sleep(1)
#             print("Hello suresh!")
# b = Apples()
# a = Apples1()
# stat_time = time.perf_counter()      # ** perf_counter
# b.run()
# print("")
# a.run()
# end_time = time.perf_counter()
# print(f'processed in {round(end_time-stat_time)}secods')

# #____________________________________________________________________________________________________________________________________

# from threading import *    # *** threading
# import time
# class Apple(Thread):      # threading
#     def run(self):
#         for run in range(10):
#             time.sleep(1)
#             print("Hello Suresh!")
# class Apples(Thread):      # threading
#     def run(self):
#         for run in range(10):
#             time.sleep(1)
#             print("Good morning!")
# a = Apple()
# b = Apples()
# stat_time = time.perf_counter()
#
# a.start()
# b.start()
#
# end_time = time.perf_counter()
# print(f"minumum{round(end_time-stat_time)}second")

# #____________________________________________________________________________________________________________________________________
# from  threading import *
# import time
# class Apple(Thread):
#     def run(self):
#         for run in range(10):
#             time.sleep(1)
#             print("Hello suresh!")
# class Apples(Thread):
#     def run(self):
#         for run in range(10):
#             time.sleep(1)
#             print("Good morning!")
#
#
# a = Apple()
# b = Apples()
# stat_time = time.perf_counter()
# a.start()
# time.sleep(0.1)
# b.start()
#
# a.join()
# b.join()
# end_time = time.perf_counter()
#
# print(f"minu{round(end_time-stat_time)}second")

#_______________________________________________________________________________________________________________________________________
   # function Threading
# from threading import *
# def Hello():
#     for x in range(5):
#         time.sleep(1)
#         print("Hello")
# def Hi():
#     for i in range(5):
#         time.sleep(1)
#         print("Hi")
# stat_time = time.perf_counter()
#
# obj = Thread(target=Hello)
# obj1 = Thread(target=Hi)
#
# obj.start()
# time.sleep(0.1)
# obj1.start()
#
# obj.join()
# obj1.join()
#
# end_time = time.perf_counter()
#
# print(round(end_time - stat_time))














































