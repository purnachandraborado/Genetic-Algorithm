import task
import virtualmachine
import ga

import random
import copy

highWeightageVmlist = []
mediumWeightageVmlist = []
lowWeightageVmlist = []

Tasklist = []
VirtualmachineList = []

previousfitness = 1000


def displayChromosome(dict):
    chromosomeStr = ""
    for keys in dict:
        if(keys != "Fitness_value"):
            chromosomeStr += "T" + str(keys.taskid) + \
                "->VM" + str(dict[keys].vmid) + "  "
        else:
            chromosomeStr += f"Fitness \
                {dict[keys]}  "

    return chromosomeStr


no_of_tasks = int(input("Enter number of tasks:: "))

# no_of_virtualmachine = int(input("Enter number of virtual machines:: "))

no_of_high = int(input("Enter number of high weightage virtual machines::"))
no_of_medium = int(
    input("Enter number of medium weightage virtual machines::"))
no_of_low = int(
    input("Enter number of low weightage virtual machines::"))
no_of_virtualmachine = no_of_high+no_of_medium+no_of_low
print(
    f"Total number of virtual machine ::{no_of_virtualmachine}")


print("Simulation started......")
print("\nTask entries initiated......\n")
for i in range(no_of_tasks):
    taskobj = task.Task(i, random.randint(10000, 50000-1))
    Tasklist.append(taskobj)
print("Task entities completed......\n")


print("Virtual machine entities has been started....\n")
j = 0
for i in range(no_of_high):
    vmobj = virtualmachine.VirtualMachine(j, 1)
    highWeightageVmlist.append(vmobj)
    VirtualmachineList.append(vmobj)
    j = j+1
for i in range(no_of_medium):
    vmobj = virtualmachine.VirtualMachine(j, 2)
    mediumWeightageVmlist.append(vmobj)
    VirtualmachineList.append(vmobj)
    j = j+1
for i in range(no_of_low):
    vmobj = virtualmachine.VirtualMachine(j, 3)
    lowWeightageVmlist.append(vmobj)
    VirtualmachineList.append(vmobj)
    j = j+1


initialPopulation = ga.GA.Create_intial_population(
    Tasklist, VirtualmachineList, highWeightageVmlist, mediumWeightageVmlist, lowWeightageVmlist)

i = 1
print()
print('_'*40)
print("\n" + " "*11 + "INITIAL POPULATION")
print('-'*40)
print("CHROMOSOME NO.  |       SOLUTION       ")
print('-'*40)
for i in range(15):
    print("\t" + str(i+1) + "\t| " +
          displayChromosome(initialPopulation[i]) + " ")

print("\nFitness value added to the chromosome\n")

initialPopulation = ga.GA.FitnessOfPopulation(initialPopulation)


for j in range(5):
    print("\n"+"="*40+"Generation"+str(j)+"="*40)
    i = 1
    print()
    print('_'*40)
    print("\n" + " "*11 + "FITNESS VALUES")
    print('-'*40)
    print("CHROMOSOME NO.  |       FITNESS VALUE       ")
    print('-'*40)
    for Chromosome in initialPopulation:
        print(f"\t  {i}  \t| {Chromosome['Fitness_value']} ")
        i = i+1

    parentlist = ga.GA.Parent(initialPopulation)

    print("\nparent list\n")

    i = 1
    print()
    print('_'*40)
    print("\n" + " "*11 + "PARENT LIST")
    print('-'*40)
    print("CHROMOSOME NO.  |       SOLUTION       ")
    print('-'*40)
    for i in range(len(parentlist)):
        print(f"\t {parentlist[i][0]+1} \t| " +
              displayChromosome(parentlist[i][1]) + " ")

    print("\noffspring\n")
    bestParent, notBestParent = parentlist[0][1].copy(
    ), parentlist[1][1].copy()
    offspring = ga.GA.Crossover(bestParent, notBestParent, 10)

    # i = 1
    # print()
    # print('_'*40)
    # print("\n" + " "*11 + "After OFFSPRING INITIAL POPULATION")
    # print('-'*40)
    # print("CHROMOSOME NO.  |       SOLUTION       ")
    # print('-'*40)
    # for i in range(len(initialPopulation)):
    #     print("\t" + str(i+1) + "\t| " +
    #           displayChromosome(initialPopulation[i]) + " ")

    i = 1
    print()
    print('_'*40)
    print("\n" + " "*11 + "CROSS OVER")
    print('-'*40)
    print("CHROMOSOME NO.  |       OFFSPRING       ")
    print('-'*40)
    print(f"\t {parentlist[0][0]+1}x{parentlist[1][0]+1} \t| " +
          displayChromosome(offspring) + " ")

    print("\nMutation..\n")

    mutatedOffspring = ga.GA.Mutation(offspring, 5)

    i = 1
    print()
    print('_'*40)
    print("\n" + " "*11 + "MUTATION")
    print('-'*40)
    print("CHROMOSOME NO.  |       OFFSPRING       ")
    print('-'*40)
    print(f"\t {parentlist[0][0]+1}x{parentlist[1][0]+1} \t| " +
          displayChromosome(mutatedOffspring) + " ")

    # i = 1
    # print()
    # print('_'*40)
    # print("\n" + " "*11 + "BEFORE UPDATED INITIAL POPULATION")
    # print('-'*40)
    # print("CHROMOSOME NO.  |       SOLUTION       ")
    # print('-'*40)
    # for i in range(len(initialPopulation)):
    #     print("\t" + str(i+1) + "\t| " +
    #           displayChromosome(initialPopulation[i]) + " ")

    if(ga.GA.SimulatedAnnealing(mutatedOffspring, previousfitness) == True):
        if(mutatedOffspring["Fitness_value"] != previousfitness):
            print("\n Mutated Offspring has been added to the Initial Population")
            initialPopulation.append(mutatedOffspring)
        previousfitness = mutatedOffspring["Fitness_value"]
        initialPopulation = ga.GA.SurvivalSelection(initialPopulation)
        initialPopulation = ga.GA.SurvivalSelection(initialPopulation)

print("\nFinal Intial Population \n")

i = 1
print()
print('_'*40)
print("\n" + " "*11 + "UPDATED INITIAL POPULATION")
print('-'*40)
print("CHROMOSOME NO.  |       SOLUTION       ")
print('-'*40)
for i in range(len(initialPopulation)):
    print("\t" + str(i+1) + "\t| " +
          displayChromosome(initialPopulation[i]) + " ")

BestOffspring = ga.GA.BestOffspring(initialPopulation)

i = 1
print()
print('_'*40)
print("\n" + " "*11 + "BEST OFFSPRING")
print('-'*40)
print("CHROMOSOME NO.  |       SOLUTION       ")
print('-'*40)
print("\t" + str(BestOffspring[0]+1) + "\t| " +
      displayChromosome(BestOffspring[1]) + " ")
