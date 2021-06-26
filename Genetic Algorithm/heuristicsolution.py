import random
import operator


class Heuristc:

    # Chromosome :dictonay
    #     contains key as task object and value as Virtual machone object

    def FCFS(tasklist, vmlist):
        # returns a chromosome dictonary in which task and virtualmachine are scheduled according to FCFS
        c = 0
        Chromosome = {}
        for task in tasklist:
            Chromosome[task] = vmlist[c]
            c = (c+1) % len(vmlist)
        return Chromosome

    def SJF(tasklist, vmlist):
        # returns a chromosome dictonary in which task and virtualmachine are scheduled according to SJF
        c = 0
        Chromosome = {}
        # sorted according to instruction length
        sortedtask = sorted(tasklist,
                            key=operator.attrgetter('instructionlength'))
        for task in sortedtask:
            Chromosome[task] = vmlist[c]
            c = (c+1) % len(vmlist)
        return Chromosome

    def WMR(tasklist, highWeightageVmlist, mediumWeightagevmlist, lowWeightageVmlist):
        # returns Chromsome dictonary where virtual machine are assigned according to the weightage of the task level
        Chromosome = {}
        for task in tasklist:
            if(task.taskWeightage == 1):
                Chromosome[task] = random.choice(highWeightageVmlist)
            elif(task.taskWeightage == 2):
                Chromosome[task] = random.choice(mediumWeightagevmlist)
            else:
                Chromosome[task] = random.choice(lowWeightageVmlist)
        return Chromosome

    def PurelyRandom(tasklist, vmlist):
        # returns Chromosome dictonary where virtual machine are assigned randomly
        Chromosome = {}
        for task in tasklist:
            Chromosome[task] = random.choice(vmlist)
        return Chromosome
