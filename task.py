import random
import datetime


class Task:

    # taskid: int
    # it is the id of the taskid
    # taskWeightage: int of chois 1, 2, 3
    #     where 1 is highWeightage, 2 is mediumWeightage and 3 is lowEighatge
    # masDelay: float
    #     it is the maximum delay tolarable by Task
    # arrivalTime: datetime
    #     it is the task arrval time
    # startTime: datetime
    #     it is the starting time of task execution
    # responseTime:datetime
    #     it is the response time of Task
    # completionTime:datetime
    #     it is the completionTime of task

    def __init__(self, taskid, instructionlength):
        self.taskid = taskid
        self.instructionlength = instructionlength
        if(instructionlength >= 10000 and instructionlength < 20000):
            self.taskWeightage = 3
        elif (instructionlength >= 20000 and instructionlength < 30000):
            self.taskWeightage = 2
        else:
            self.taskWeightage = 1
        # self.maxDelay = random.choice([0.009, 0.01, 0.02])
        # self.arrivalTime = datetime.datetime.now()
        # self.startTime = datetime.datetime.now()
        # self.responseTime = datetime.datetime.now()
        # self.completionTime = datetime.datetime.now()
