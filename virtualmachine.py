import random


class VirtualMachine:

    # vmid:int
    #     it is the id of virtual VirtualMachine
    # mips:int
    #     instrcution length
    # vmWeightage:int of chois 1, 2, 3
    #      where 1 is highWeightage, 2 is mediumWeightage and 3 is lowweighatge

    def __init__(self, vmid, vmWeightage):
        self.vmTasklist = []
        self.vmid = vmid
        self.vmWeightage = vmWeightage
        if(self.vmWeightage == 1):
            self.mips = random.randint(3000, 4000)
        elif(self.vmWeightage == 2):
            self.mips = random.randint(2000, 3000-1)
        else:
            self.mips = random.randint(1000, 2000-1)
        print(
            f"virtual machine of id {self.vmid} of weightage {self.vmWeightage} is created")
