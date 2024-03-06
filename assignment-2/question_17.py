# In a company, worker efficiency is determined on the basis of the time required for a worker
# to complete a particular job. If the time taken by the worker is between 2 – 3 hours, then the
# worker is said to be highly efficient. If the time required by the worker is between 3 – 4
# hours, then the worker is ordered to improve speed. If the time taken is between 4 – 5 hours,
# the worker is given training to improve his speed, and if the time taken by the worker is
# more than 5 hours, then the worker has to leave the company. If the time taken by the
# worker is input through the keyboard, find the efficiency of the worker

input_time=float(input("the time taken by the worker:"))
work_time=60*input_time
if work_time >=120 and work_time < 180:
    print("highly efficient")
elif work_time >=180 and work_time < 240:
    print(" improve speed")
elif work_time >=240 and work_time < 300:
    print("given training to improve his speed")
else:
    print("leave the company")