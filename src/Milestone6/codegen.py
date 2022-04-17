from scope import *
from utils import *

class Register:
    def __init__(self):

        ## Store an array for registers, first value denotes var it stores, 
        ## second value stores last time it has been used (for use in LRU algo)
        self.regs = {'$t0': [None, 0], 
                     '$t1': [None, 0], 
                     '$t2': [None, 0],
                     '$t3': [None, 0],
                     '$t4': [None, 0],
                     '$t5': [None, 0],
                     '$t6': [None, 0],
                     '$t7': [None, 0],
                     '$t8': [None, 0],
                     '$t9': [None, 0],
                    }

        ## To be saved across func calls 
        self.regsSaved = {'$s0': [None, 0],
                          '$s1': [None, 0],
                          '$s2': [None, 0],
                          '$s3': [None, 0],
                          '$s4': [None, 0],
                          '$s5': [None, 0],
                          '$s6': [None, 0],
                          '$s7': [None, 0],
                         }

        ## Registers for storing results  
        self.result_regs = {'$v0': [None, 0], 
                            '$v1': [None, 0],
                           }

        ## Registers for storing arguments  
        self.arg_regs = {'$a0': [None, 0], 
                         '$a1': [None, 0],
                         '$a2': [None, 0], 
                         '$a3': [None, 0] 
                        }

        ## These are special registers storing the assembly name and current address 
        self.gp = {'$gp': None} ## Global pointer 
        self.sp = {'$sp': None} ## Stack pointer
        self.fp = {'$fp': None} ## Frame pointer 
        self.ra = {'$r31': None} ## Return Address 

        ## Similar variables for floats 
        self.regsF = {'$f1': [None, 0],
                      '$f3': [None, 0],
                     } 

        for i in range(4, 12):
            self.regsF[f'$f{i}'] = [None, 0] 
        for i in range(20, 24):
            self.regsF[f'$f{i}'] = [None, 0] 

        self.regsSavedF = {}
        for i in range(24, 32):
            self.regsF[f'$f{i}'] = [None, 0] 
        
        self.args_regsF = {}
        for i in range(12, 20):
            self.args_regsF[f'$f{i}'] = [None, 0]

        ## Registers for storing results  
        self.result_regsF = {'$f0': [None, 0], 
                             '$f2': [None, 0],
                            }        

        ## Map to store {variables : location (register or offset on stack)}
        ## Value is an array -> first index stores type (0/1 based on reg or offset)
        ## Second value stores the value (regName or offsetAmt)
        self.locations = {} 

    ## Function to return the least recently used register  
    def find_new_reg(self, isFloat = False):  
        minn = 1e9
        final_reg = None 
        foundEmpty = 0

        if not isFloat: 
            for reg in self.regs:
                if self.regs[reg][0] == None: 
                    foundEmpty = True  
                
                if self.regs[reg][1] <= minn:
                    minn = self.regs[reg][1] 
                    final_reg = reg 

            ## Only look in saved registers if temps are not available
            if not foundEmpty:
                for reg in self.regsSaved:
                    if self.regsSaved[reg][1] <= minn:
                        minn = self.regsSaved[reg][1] 
                        final_reg = reg

            return final_reg
        else:
            for reg in self.regsF:
                if self.regsF[reg][0] == None: 
                    foundEmpty = True 
            
                if self.regsF[reg][1] <= minn:
                    minn = self.regsF[reg][1] 
                    final_reg = reg 

            ## Only look in saved registers if temps are not available
            if not foundEmpty:
                for reg in self.regsSavedF:
                    if self.regsSavedF[reg][1] <= minn:
                        minn = self.regsSaved[reg][1] 
                        final_reg = reg

            return final_reg

    ## Function to be called to shift contents of register to memory, additionally 
    ## location of variables to be shifted has to be given while calling this function 
    ## NOTE: Flushes everything if regs is None 
    def move_reg(self, regList = None, new_loc = None, size = None, isFloat = False, isUnsigned = False):
        if not isFloat:  
            if regList:
                print("Requested to shift: ", regList)
            if regList in None:
                regList = self.regs.keys()

            mips = []
            for i, reg in enumerate(regList):
                ## If someone occupied the register previously
                if self.regs[reg][0]:
                    print('Going to free register ', reg) 
                    if new_loc[i] != None: ## To be stored in memory
                        suffix = getsizeSuffix(size, isFloat, isUnsigned)   
                        mips.append("\ts" + suffix + "\t" + reg + "," + str(new_loc) + "($fp)\n")   
                    else:
                        print("Please provide a valid memory location") 
                    
                    ## Reset after shifting
                    self.locations[self.regs[reg][0]][0] = 1
                    self.locations[self.regs[reg][0]][1] = new_loc[i]
                    self.regs[reg][0] = None
                    self.regs[reg][1] = 0 

                elif self.regsSaved[reg][0]:
                    print('Going to free register ', reg) 
                    if new_loc[i] != None: ## To be stored in memory 
                        suffix = getsizeSuffix(size, isFloat, isUnsigned)  
                        mips.append("\ts" + suffix + "\t" + reg + "," + str(new_loc) + "($fp)\n")   
                    else:
                        print("Please provide a valid memory location") 
                    
                    ## Reset after shifting
                    self.locations[self.regsSaved[reg][0]][0] = 1
                    self.locations[self.regsSaved[reg][0]][1] = new_loc[i] 
                    self.regsSaved[reg][0] = None
                    self.regsSaved[reg][1] = 0 
            
            print("Instruction generated: ", mips) 
            return mips

        else:   
            if regList:
                print("Requested to shift: ", regList)
            if regList in None:
                regList = self.regsF.keys()

            mips = []
            for i, reg in enumerate(regList):
                ## If someone occupied the register previously
                if self.regsF[reg][0]:
                    print('Going to free register ', reg) 
                    if new_loc[i] != None: ## To be stored in memory 
                        suffix = getsizeSuffix(size, isFloat, isUnsigned)  
                        mips.append("\ts" + suffix + "\t" + reg + "," + str(new_loc) + "($fp)\n")   
                    else:
                        print("Please provide a valid memory location") 
                    
                    ## Reset after shifting
                    self.locations[self.regsF[reg][0]][0] = 1
                    self.locations[self.regsF[reg][0]][1] = new_loc[i] 
                    self.regsF[reg][0] = None
                    self.regsF[reg][1] = 0 

                elif self.regsSavedF[reg][0]:
                    print('Going to free register ', reg) 
                    if new_loc[i] != None: ## To be stored in memory 
                        suffix = getsizeSuffix(size, isFloat, isUnsigned)  
                        mips.append("\ts" + suffix + "\t" + reg + "," + str(new_loc) + "($fp)\n")   
                    else:
                        print("Please provide a valid memory location") 
                    
                    ## Reset after shifting
                    self.locations[self.regsSavedF[reg][0]][0] = 1
                    self.locations[self.regsSavedF[reg][0]][1] = new_loc[i]
                    self.regsSavedF[reg][0] = None
                    self.regsSavedF[reg][1] = 0 

            print("Instruction generated: ", mips) 
            return mips

    ## Function to be called to copy contents of register to memory, additionally 
    ## location of variables to be shifted has to be given while calling this function 
    ## NOTE: Flushes everything if regs is None 
    def copy_reg_to_memory(self, regList = None, new_loc = None, size = None, isFloat = False, isUnsigned = False):
        if not isFloat:  
            if regList:
                print("Requested to shift: ", regList)
            if regList in None:
                regList = self.regs.keys()

            mips = []
            for i, reg in enumerate(regList):
                ## If someone occupied the register previously
                if self.regs[reg][0]:
                    mips.append('\t#Going to free register ', reg) 
                    if new_loc != None: ## To be stored in memory 
                        suffix = getsizeSuffix(size, isFloat, isUnsigned)   
                        mips.append("\ts" + suffix + "\t" + reg + "," + str(new_loc) + "($fp)\n")   
                    else:
                        print("Please provide a valid memory location") 

                elif self.regsSaved[reg][0]:
                    mips.append('\t#Going to free register ', reg) 
                    if new_loc != None: ## To be stored in memory
                        suffix = getsizeSuffix(size, isFloat, isUnsigned)   
                        mips.append("\ts" + suffix + "\t" + reg + "," + str(new_loc) + "($fp)\n")   
                    else:
                        print("Please provide a valid memory location") 
            
            print("Instruction generated: ", mips) 
            return mips

        else:   
            if regList:
                mips.append("\t# Requested to shift: ", regList)
            if regList in None:
                regList = self.regsF.keys()

            mips = []
            for i, reg in enumerate(regList):
                ## If someone occupied the register previously
                if self.regsF[reg][0]:
                    mips.append('\t# Going to free register ', reg) 
                    if new_loc != None: ## To be stored in memory 
                        suffix = getsizeSuffix(size, isFloat, isUnsigned)  
                        mips.append("\ts" + suffix + "\t" + reg + "," + str(new_loc) + "($fp)\n")   
                    else:
                        print("Please provide a valid memory location") 

                elif self.regsSavedF[reg][0]:
                    mips.append('\t# Going to free register ', reg) 
                    if new_loc != None: ## To be stored in memory 
                        suffix = getsizeSuffix(size, isFloat, isUnsigned)  
                        mips.append("\ts" + suffix + "\t" + reg + "," + str(new_loc) + "($fp)\n")   
                    else:
                        print("Please provide a valid memory location") 

            print("Instruction generated: ", mips) 
            return mips

    ## Function that returns a tuple of register and instructions
    ## for a variable var. This function also has to be used while
    ## fetching location for a variable for execution of LRU policy
    def get_register(self, var = None, size = None, isFloat = False, isUnsigned = False): 
        if var in self.locations and self.locations[var][0] == 0:
            self.count += 1

            if not isFloat:
                self.regs[self.locations[var][1]][1] = self.count  
                return (self.locations[var][1], [])
            else:
                self.regsF[self.locations[var][1]][1] = self.count
                return (self.locations[var][1], [])

        else: ## Need a new register
            new_reg = self.find_new_register(isFloat = isFloat)
            mips = self.move_reg([new_reg])
            
            self.count += 1 
            if not isFloat:
                self.regs[new_reg][0] = var 
                self.regs[new_reg][1] = self.count 
            else:
                self.regsF[new_reg][0] = var 
                self.regsF[new_reg][1] = self.count 

            if var in self.locations and self.locations[var][0] == 1: ## It is stored in memory
                self.locations[var][0] = 0
                self.locations[var][1] = new_reg 
                mips.append(f'\t# Swapping out reg {new_reg} for variable {var}')
                suffix = getsizeSuffix(size, isFloat, isUnsigned)
                mips.append("\tl" + suffix + "\t" + str(self.locations[var][1]) + "($fp)" + "," + f"{new_reg}")
            else:
                self.locations[var] = [0, new_reg]

## Class to implement code generation from 3AC and symtable to MIPS
class MIPS:
    
    def __init__(self, ):
        print('Init MIPS')
        self.regs = Register()
        self.instr = []
        self.INDENT = " " * 4
        self.code = None
        self.stm = None

    def addSections(self):
        code = ""
        code += '\t.data\n'
        code += '\t.text\n\t.globl main\n\n'
        return code

    def tac2mips(self, code, stm):
        self.code = code
        self.stm = stm
        
        return self.instr
    
    def dosyscall(self, number):
        return f"\tli $v0 {number}\n\tsyscall"
    
    def malloc(self, space):
        code = ""
        if type(space) != str:
            code += f"\tli $a0 {space}"
        else:
            code += f"\tadd $a0 r0 {space}"
        code += self.dosyscall(9)