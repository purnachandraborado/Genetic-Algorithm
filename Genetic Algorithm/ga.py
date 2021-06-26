import heuristicsolution
import random


class GA:

    @classmethod
    def Create_intial_population(cls, Tasklist, VirtualmachineList, highWeightageVmlist, mediumWeightageVmlist, lowWeightageVmlist):
        # calculates initial population and returns the value
        initialPopulation = []
        print("Initial Population being generated......")
        initialPopulation.append(
            heuristicsolution.Heuristc.FCFS(Tasklist, VirtualmachineList))
        initialPopulation.append(
            heuristicsolution.Heuristc.SJF(Tasklist, VirtualmachineList))
        for i in range(5):
            initialPopulation.append(heuristicsolution.Heuristc.WMR(
                Tasklist, highWeightageVmlist, mediumWeightageVmlist, lowWeightageVmlist))
        for i in range(8):
            initialPopulation.append(
                heuristicsolution.Heuristc.PurelyRandom(Tasklist, VirtualmachineList))
        return initialPopulation

    @classmethod
    def FitnessOfPopulation(cls, initialPopulation):
        # returns the Fitness value of population
        for Chromosome in initialPopulation:
            completionTime = 0
            for key, value in Chromosome.items():
                completionTime = completionTime + \
                    (key.instructionlength/value.mips)
            Chromosome["Fitness_value"] = completionTime/len(Chromosome)
        return initialPopulation

    @classmethod
    def FitnessOfChromosome(cls, Chromosome):
        # returns the fitness value of Chromosome
        completionTime = 0
        for key, value in Chromosome.items():
            if(key != "Fitness_value"):
                completionTime = completionTime + \
                    (key.instructionlength/value.mips)
        Chromosome["Fitness_value"] = completionTime/len(Chromosome)
        return Chromosome

    @classmethod
    def Parent(cls, intialPopulation):
        # returns the parentlist which is the last two min value form population on the basis of fitness value
        parentlist = []
        lowest = intialPopulation[0]
        # print("intial 0 ", intialPopulation[0])
        lowest2 = None
        for item in intialPopulation:
            if item["Fitness_value"] < lowest["Fitness_value"]:
                lowest2 = lowest
                lowest = item
            elif lowest2 == None or lowest2["Fitness_value"] > item["Fitness_value"]:
                lowest2 = item
        parentlist.append([intialPopulation.index(lowest), lowest])
        parentlist.append([intialPopulation.index(lowest2), lowest2])
        return parentlist

    @classmethod
    def GeneCompletionTime(cls, instructionlength, mips):
        return instructionlength/mips

    @classmethod
    def Crossover(cls, Bestparent, Notbestparent, noOfChecks):
        # calculates crossover
        #     offspring:dict
        #         stores offspring
        #     CompletionTimeparent:dict
        #         stores the copy of the best parent
        offspring = Bestparent
        CompletionTimeparent = Bestparent
        countChecks = 0
        for key, value in Bestparent.items():
            if(countChecks == noOfChecks):
                break
            if(random.choice([1, 0]) == 1):
                countChecks += 1
                # print(f"check number = {countChecks}")
                if(key != "Fitness_value"):
                    if(key.instructionlength/value.mips > key.instructionlength/Notbestparent[key].mips):
                        tempMips1 = value.mips
                        tempvm1 = value
                        tempMips2 = Notbestparent[key].mips
                        tempvm2 = Notbestparent[key]
                        #newCompletionTime1 = key.instructionlength/tempMips2
                        CompletionTimeparent[key] = tempvm2
                        #newVm = None
                        CompletionTimeReduced = False
                        for key1, value1 in Bestparent.items():
                            if(key1 != "Fitness_value"):
                                if(Bestparent[key1] == tempvm2):
                                    #newCompletionTime2 = key1.instructionlength/tempMips1
                                    CompletionTimeparent[key1] = tempvm1
                                    CompletionTimeparent = cls.FitnessOfChromosome(
                                        CompletionTimeparent)
                                    if(CompletionTimeparent["Fitness_value"] < offspring["Fitness_value"]):
                                        CompletionTimeReduced = True
                                        break
                                    else:
                                        CompletionTimeparent[key1] = tempvm2

                        if(CompletionTimeReduced == True):
                            offspring = CompletionTimeparent
                        else:
                            CompletionTimeparent = offspring
        return offspring

    @classmethod
    def Mutation(cls, offspring, noOfSwaps):
        tempOffSpring = offspring
        for i in range(noOfSwaps):
            key1 = random.choice(list(tempOffSpring.keys()))
            key2 = random.choice(list(tempOffSpring.keys()))

            if (key1 != key2 and key1 != 'Fitness_value' and key2 != 'Fitness_value'):
                tempOffSpring[key1], tempOffSpring[key2] = tempOffSpring[key2], tempOffSpring[key1]
                tempOffSpring = cls.FitnessOfChromosome(tempOffSpring)
                if tempOffSpring['Fitness_value'] < offspring['Fitness_value']:
                    offspring = tempOffSpring
                    offspring = cls.FitnessOfChromosome(offspring)
                else:
                    tempOffSpring[key1], tempOffSpring[key2] = tempOffSpring[key2], tempOffSpring[key1]
                    tempOffSpring = cls.FitnessOfChromosome(tempOffSpring)
            else:
                noOfSwaps += 1
        return offspring

    @classmethod
    def SimulatedAnnealing(cls, mutatedOffspring, previousfitness):
        if(mutatedOffspring["Fitness_value"] < previousfitness):
            return True
        elif (random.choice([True, False]) == True):
            return True
        else:
            return False

    @classmethod
    def SurvivalSelection(cls, initialPopulation):
        highest = initialPopulation[0]
        for item in initialPopulation:
            if item["Fitness_value"] > highest["Fitness_value"]:
                highest = item
        initialPopulation.remove(highest)
        return initialPopulation
