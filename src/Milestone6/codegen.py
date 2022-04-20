from calendar import c
from scope import *
from utils import *


class Register:
    def __init__(self):

        self.count = 0

        # Store an array for registers, first value denotes var it stores,
        # second value stores last time it has been used (for use in LRU algo)
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

        # To be saved across func calls
        self.regsSaved = {'$s0': [None, 0],
                          '$s1': [None, 0],
                          '$s2': [None, 0],
                          '$s3': [None, 0],
                          '$s4': [None, 0],
                          '$s5': [None, 0],
                          '$s6': [None, 0],
                          '$s7': [None, 0],
                          }

        # Registers for storing results
        self.result_regs = {'$v0': [None, 0],
                            '$v1': [None, 0],
                            }

        # Registers for storing arguments
        self.arg_regs = {'$a0': [None, 0],
                         '$a1': [None, 0],
                         '$a2': [None, 0],
                         '$a3': [None, 0]
                         }

        # These are special registers storing the assembly name and current address
        self.gp = {'$gp': None}  # Global pointer
        self.sp = {'$sp': None}  # Stack pointer
        self.fp = {'$fp': None}  # Frame pointer
        self.ra = {'$r31': None}  # Return Address

        # Similar variables for floats
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

        # Registers for storing results
        self.result_regsF = {'$f0': [None, 0],
                             '$f2': [None, 0],
                             }

        # Map to store {variables : location (register or offset on stack)}
        # Value is an array -> first index stores type (0/1 based on reg or offset)
        # Second value stores the value (regName or offsetAmt)
        self.locations = {}

    # Function to return the least recently used register
    def find_new_reg(self, isFloat=False):
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

            # Only look in saved registers if temps are not available
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

            # Only look in saved registers if temps are not available
            if not foundEmpty:
                for reg in self.regsSavedF:
                    if self.regsSavedF[reg][1] <= minn:
                        minn = self.regsSaved[reg][1]
                        final_reg = reg

            return final_reg

    # Function to be called to shift contents of register to memory, additionally
    # location of variables to be shifted has to be given while calling this function
    # NOTE: Flushes everything if regs is None
    def move_reg(self, regList=None, new_loc=None, size=None, isFloat=False, isUnsigned=False):
        if not isFloat:
            if regList:
                print("Requested to shift: ", regList)
            if regList is None:
                regList = self.regs.keys()

            mips = []
            for i, reg in enumerate(regList):
                # If someone occupied the register previously
                if reg in self.regs and self.regs[reg][0]:
                    print('Going to free register ', reg)
                    if new_loc[i] != None:  # To be stored in memory
                        suffix = getsizeSuffix(size, isFloat, isUnsigned)
                        mips.append("\ts" + suffix + "\t" + reg +
                                    "," + str(new_loc) + "($fp)\n")
                    else:
                        print("Please provide a valid memory location")

                    # Reset after shifting
                    self.locations[self.regs[reg][0]][0] = 1
                    self.locations[self.regs[reg][0]][1] = new_loc[i]
                    self.regs[reg][0] = None
                    self.regs[reg][1] = 0

                elif reg in self.regsSaved and self.regsSaved[reg][0]:
                    print('Going to free register ', reg)
                    if new_loc[i] != None:  # To be stored in memory
                        suffix = getsizeSuffix(size, isFloat, isUnsigned)
                        mips.append("\ts" + suffix + "\t" + reg +
                                    "," + str(new_loc) + "($fp)\n")
                    else:
                        print("Please provide a valid memory location")

                    # Reset after shifting
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
                # If someone occupied the register previously
                if self.regsF[reg][0]:
                    print('Going to free register ', reg)
                    if new_loc[i] != None:  # To be stored in memory
                        suffix = getsizeSuffix(size, isFloat, isUnsigned)
                        mips.append("\ts" + suffix + "\t" + reg +
                                    "," + str(new_loc) + "($fp)\n")
                    else:
                        print("Please provide a valid memory location")

                    # Reset after shifting
                    self.locations[self.regsF[reg][0]][0] = 1
                    self.locations[self.regsF[reg][0]][1] = new_loc[i]
                    self.regsF[reg][0] = None
                    self.regsF[reg][1] = 0

                elif self.regsSavedF[reg][0]:
                    print('Going to free register ', reg)
                    if new_loc[i] != None:  # To be stored in memory
                        suffix = getsizeSuffix(size, isFloat, isUnsigned)
                        mips.append("\ts" + suffix + "\t" + reg +
                                    "," + str(new_loc) + "($fp)\n")
                    else:
                        print("Please provide a valid memory location")

                    # Reset after shifting
                    self.locations[self.regsSavedF[reg][0]][0] = 1
                    self.locations[self.regsSavedF[reg][0]][1] = new_loc[i]
                    self.regsSavedF[reg][0] = None
                    self.regsSavedF[reg][1] = 0

            print("Instruction generated: ", mips)
            return mips

    # Function to be called to copy contents of register to memory, additionally
    # location of variables to be shifted has to be given while calling this function
    # NOTE: Flushes everything if regs is None
    def copy_reg_to_memory(self, regList=None, new_loc=None, size=None, isFloat=False, isUnsigned=False):
        if not isFloat:
            if regList:
                print("Requested to shift: ", regList)
            if regList in None:
                regList = self.regs.keys()

            mips = []
            for i, reg in enumerate(regList):
                # If someone occupied the register previously
                if self.regs[reg][0]:
                    mips.append('\t#Going to free register ', reg)
                    if new_loc != None:  # To be stored in memory
                        suffix = getsizeSuffix(size, isFloat, isUnsigned)
                        mips.append("\ts" + suffix + "\t" + reg +
                                    "," + str(new_loc) + "($fp)\n")
                    else:
                        print("Please provide a valid memory location")

                elif self.regsSaved[reg][0]:
                    mips.append('\t#Going to free register ', reg)
                    if new_loc != None:  # To be stored in memory
                        suffix = getsizeSuffix(size, isFloat, isUnsigned)
                        mips.append("\ts" + suffix + "\t" + reg +
                                    "," + str(new_loc) + "($fp)\n")
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
                # If someone occupied the register previously
                if self.regsF[reg][0]:
                    mips.append('\t# Going to free register ', reg)
                    if new_loc != None:  # To be stored in memory
                        suffix = getsizeSuffix(size, isFloat, isUnsigned)
                        mips.append("\ts" + suffix + "\t" + reg +
                                    "," + str(new_loc) + "($fp)\n")
                    else:
                        print("Please provide a valid memory location")

                elif self.regsSavedF[reg][0]:
                    mips.append('\t# Going to free register ', reg)
                    if new_loc != None:  # To be stored in memory
                        suffix = getsizeSuffix(size, isFloat, isUnsigned)
                        mips.append("\ts" + suffix + "\t" + reg +
                                    "," + str(new_loc) + "($fp)\n")
                    else:
                        print("Please provide a valid memory location")

            print("Instruction generated: ", mips)
            return mips

    # Function that returns a tuple of register and instructions
    # for a variable var. This function also has to be used while
    # fetching location for a variable for execution of LRU policy
    def get_register(self, var=None, size=None, isFloat=False, isUnsigned=False):
        if var in self.locations and self.locations[var][0] == 0:
            self.count += 1

            if not isFloat:
                self.regs[self.locations[var][1]][1] = self.count
                return (self.locations[var][1], [])
            else:
                self.regsF[self.locations[var][1]][1] = self.count
                return (self.locations[var][1], [])

        else:  # Need a new register
            new_reg = self.find_new_reg(isFloat=isFloat)
            mips = self.move_reg([new_reg])

            self.count += 1
            if not isFloat:
                self.regs[new_reg][0] = var
                self.regs[new_reg][1] = self.count
            else:
                self.regsF[new_reg][0] = var
                self.regsF[new_reg][1] = self.count

            # It is stored in memory
            if var in self.locations and self.locations[var][0] == 1:
                self.locations[var][0] = 0
                self.locations[var][1] = new_reg
                mips.append(
                    f'\t# Swapping out reg {new_reg} for variable {var}')
                suffix = getsizeSuffix(size, isFloat, isUnsigned)
                mips.append("\tl" + suffix + "\t" +
                            str(self.locations[var][1]) + "($fp)" + "," + f"{new_reg}")
            else:
                self.locations[var] = [0, new_reg]

            return (new_reg, mips)

# Class to implement code generation from 3AC and symtable to MIPS


class MIPS:

    def __init__(self, code, stm):
        print('Init MIPS')
        self.regs = Register()
        self.instr = []
        self.INDENT = " " * 4
        self.tac_code = code
        self.stm: SymTableMaker = stm
        self.builtins = ['Print', 'Scan', 'Typecast']
        self.fpOffset = 0  # Offset from frame pointer

    def tac2mips(self):
        code = self.addDataSection()
        code.extend(self.addTextHeader())
        code.extend(self.addTextSection())
        return code

    def addDataSection(self):
        code = []
        code.append(f'.data\n')

        for scope in self.stm.pkgs.values():
            for var, detail in scope.symTable[0].localsymTable.items():
                if var not in self.stm.functions:
                    code.extend(self._getDataCode(detail))

        for var, detail in self.stm.symTable[0].localsymTable.items():
            if var not in self.stm.functions:
                code.extend(self._getDataCode(detail))

        code.extend(['', ''])
        return code

    def _getDataCode(self, detail):
        if detail['dataType']['name'] in ['byte', 'int8', 'uint8', 'bool']:
            return f'\t_{detail["tmp"]}: .byte 0'
        elif detail['dataType']['name'] in ['int16', 'uint16', 'rune']:
            return f'\t_{detail["tmp"]}: .half 0'
        elif detail['dataType']['name'] in ['int', 'int32', 'float32', 'uint32']:
            return f'\t_{detail["tmp"]}: .word 0'
        elif detail['dataType']['name'] in ['int64', 'uint64', 'float64']:
            return f'\t_{detail["tmp"]}: .? 0'
        elif detail['dataType']['name'] in ['struct', 'array', 'slice', 'map', 'string']:
            return f'\t_{detail["tmp"]}: .word 0, 0, 0'
        else:
            return ''

    def addTextHeader(self):
        code = ['.text', '.globl main']
        return code

    def addTextSection(self):
        code = []
        for i, codeline in enumerate(self.tac_code):
            if codeline.startswith('package') or codeline.startswith('import'):
                continue
            elif codeline.startswith('\nFunc'):
                code.extend(self.addFunction(i))
            else:
                continue
        return code

    def addFunction(self, lineno):
        code = []
        funcname = self.tac_code[lineno].split(' ')[1]
        if funcname != 'main':
            code.extend(self.handle_label('_'+funcname))
        else:
            code.extend(self.handle_label(funcname))
        for i in range(lineno+1, len(self.tac_code)):
            if self.tac_code[i].startswith('Func END'):
                if not self.tac_code[i-1].startswith('return'):
                    if funcname != 'main':
                        code.append(f'\tjr $ra')
                    else:
                        code.extend(self.exit())
                else:
                    j = 2
                    retValues = []
                    while self.tac_code[i-j].startswith('retparams'):
                        retValues.append(self.tac_code[i-j].split()[1])
                        j += 1

                    retReg, _code = self._get_label(retValues[0])
                    code.extend(_code)
                    if len(self.stm.functions[funcname]['return']) == 1 and not retValues[0].startswith("vartemp"):
                        retReg = retReg[0]
                        code.append(f"\taddi $v0, {retReg}, $0")
                        code.append(f'\tjr $ra')
                    else:
                        retSize = 0
                        for retVal in self.stm.functions[funcname]['return']:
                            retSize += retVal['size']
                        code.extend(self.malloc(retSize))

                        print(retValues, self.stm.functions[funcname]['return'])
                        offset = 0
                        for idx, retVal in enumerate(self.stm.functions[funcname]['return']):
                            retReg, _code = self._get_label(retValues[idx])
                            retReg = retReg[0] ## TODO: Make it general for returning Composite DTs
                            code.extend(_code)
                            code.append(f"\tsw {retReg}, {offset}($v0)")
                            offset += retVal['size']
                        code.append(f"\taddi $v1, $0, {retSize}")
                        code.append(f'\tjr $ra')

            if self.tac_code[i].startswith('temp'):
                items = self.tac_code[i].split(' ')
                code.extend(self.handle_temp(items))
            elif self.tac_code[i].startswith('vartemp'):
                pass
            elif self.tac_code[i].startswith('*'):
                # * a = b
                # * a = unop b
                # * a = b binop c
                items = self.tac_code[i].split(' ')  
                if self.tac_code[i].startswith('temp'):
                    if len(items) == 4:
                        location = self.regs.locations[items[1]][1]
                        reg, mips = self.regs.get_register(items[3])
                        code.extend(mips)
                        code.append(f'\tsw {reg}, {location}($fp)')
                    elif len(items) == 5: 
                        reg, mips = self.regs.get_register()
                        code.extend(mips)
                        code.extend(self.handle_unOp(items[3], items[4], reg))
                        location = self.regs.locations[items[1]][1]
                        code.append(f'\tsw {reg}, {location}($fp)')    
                    elif len(items) == 6:
                        reg, mips = self.regs.get_register()
                        code.extend(mips)
                        code.extend(self.handle_binOp(items[3], items[5], items[4], reg))
                        location = self.regs.locations[items[1]][1]
                        code.append(f'\tsw {reg}, {location}($fp)')  
                elif self.tac_code[i].startswith('vartemp'):
                    # TODO
                    pass
            elif self.tac_code[i].startswith('call'):
                ## TODO 
                pass
            elif self.tac_code[i].startswith('new'):
                ## TODO 
                pass
            elif self.tac_code[i].startswith('params'):
                code.extend(self.handle_param(self.tac_code[i].split(' ')[1]))
            elif self.tac_code[i].startswith('retparams'):
                pass ## Done inside addFunction
            elif self.tac_code[i].startswith('retval'):
                reg, mips = self.handle_returns(self.tac_code[i].split(' ')[0])
                code.extend(mips)
                return code
            elif self.tac_code[i].startswith('if'):
                items = self.tac_code[i].split(' ')
                cond = items[2]
                elselab = items[5]
                code.extend(self.handle_ifStmt(cond, elselab))
            elif self.tac_code[i].startswith('goto'):
                code.extend(self.handle_goto(self.tac_code[i].split(' ')[1]))
            elif self.tac_code[i].endswith(':'):  # label
                code.extend(self.handle_label(self.tac_code[i][:-1]))
            elif self.tac_code[i].startswith('arg'):
                ## TODO : Handle composite literal
                code.extend(self.handle_args(items)) 
                pass
            elif len(self.tac_code[i]) > 0 and self.tac_code[i][0].isnumeric():
                code.extend(self.handle_localvars(items))  
                pass
            elif self.tac_code[i].startswith('return'):
                if funcname != 'main':
                    code.append(f'\tjr $ra')
                else:
                    code.extend(self.exit())
        return code

    def _get_label(self, label, isFloat = False):
        code = []
        if label.startswith("temp") or label[0].isdigit():
            return self.regs.get_register(label, isFloat = isFloat)
        elif label.startswith("arg"):
            reg, mips = self.regs.get_register(isFloat = isFloat)
            offset = int(label.split('_')[-1].split('.')[0][:-1])
            code.extend(mips)
            if len(label.split('_')[-1].split('.')) > 1: 
                if label.split('_')[-1].split('.')[1] == 'length':
                    offset += 4 
                else:
                    offset += 8
            code.append(f'\tsw {reg} {offset}($fp)')
            return reg, code
        else:
            offset = self.regs.locations[label.split('.')[0]]
            if label.endswith('.addr'):
                reg, mips = self.regs.get_register(isFloat = isFloat)
                code.extend(mips)
                code.append(f'\tlw {reg} {offset}($fp)')
            elif label.endswith('.length'):
                reg, mips = self.regs.get_register(isFloat = isFloat)
                code.extend(mips)
                code.append(f'\tlw {reg} {offset + 4}($fp)')
            elif label.endswith('.capacity'):
                reg, mips = self.regs.get_register(isFloat = isFloat)
                code.extend(mips)
                code.append(f'\tlw {reg} {offset + 8}($fp)')
            else:
                reg1, mips = self.regs.get_register(isFloat = isFloat)
                code.extend(mips)
                code.append(f'\tlw {reg} {offset}($fp)')
                reg2, mips = self.regs.get_register(isFloat = isFloat)
                code.extend(mips)
                code.append(f'\tlw {reg2} {offset + 4}($fp)')
                reg3, mips = self.regs.get_register(isFloat = isFloat)
                code.extend(mips)
                code.append(f'\tlw {reg3} {offset + 8}($fp)')
                return [reg1, reg2, reg3], code

            return [reg], code

    def handle_newvartemp(self):
        ## TODO
        pass

    def handle_varTempPointers(self):
        ## TODO
        pass

    def handle_funcCall(self):
        ## TODO
        code = []
        pass

    def handle_localvars(self, items):
        code = []
        if len(items) == 3:
            # a = b
            if items[2].startswith('temp'):
                offset = self.locations[items[0]][1]
                find_new_reg, mips = self.regs.get_register(items[0])
                code.extend(mips)
                code.append(f'\tsw {find_new_reg}, {offset}($fp)')
            elif items[2].startswith('args'):
                offset1 = self.locations[items[0]][1]
                offset2 = items[2].split('_')[-1].split('.')[0][:-1]
                if len(items[2].split('_')[-1].split('.')) > 1: 
                    if items[2].split('_')[-1].split('.')[1] == 'length':
                        offset2 += 4 
                    else:
                        offset2 += 8
                helper_reg, mips = self.regs.get_register()
                code.extend(mips)  
                code.append(f'\tlw {helper_reg}, {offset2}($fp)')
                code.append(f'\tsw {helper_reg}, {offset1}($fp)') 
            elif items[2].startswith('var_temp'):
                retReg, mips = self._get_label(items[2])
                retReg = retReg[0] ## Both point to same location
                offset = self.locations[items[0]][1]
                code.append(f'\tsw {retReg}, {offset}($fp)')

            elif items[2].startswith('retval'):
                funcName = items[2].split('_')[1]
                num_returns = len(
                    self.stm.functions[funcName]['return'])
                if num_returns == 1:
                    reg, mips = self.regs.get_register(items[0])
                    code.append(f'\taddi {reg}, $v0, $0')
                else:
                    ret_reg, mips = self.handle_returns(items[2])
                    code.extend(mips)
                    offset = self.locations[items[0]][1]
                    code.append(f'\tlw {ret_reg}, {offset}($fp)')
            else:
                if items[2][0] == '"':
                    # string: TODO
                    pass
                elif items[2].isnumeric():
                    if str(int(items[2])) == items[2]:
                        # integer
                        offset = self.locations[items[0]][1]
                        helper_reg, mips = self.regs.get_register()
                        code.extend(mips) 
                        code.append(f'\tli {helper_reg}, {items[2]}')
                        code.append(f'\tsw {reg}, {offset}($fp)')
                        pass
                    else:
                        # float
                        offset = self.locations[items[0]][1]
                        helper_reg, mips = self.regs.get_register(items[0], isFloat = True)
                        code.extend(mips)
                        code.append(f'\tli.s {helper_reg}, {items[2]}')
                        code.append(f'\s.s {helper_reg}, {offset}($fp)')
                        pass
                elif items[2][0] == "'":
                    # rune
                    offset = self.locations[items[0]][1]
                    helper_reg, mips = self.regs.get_register(items[0])
                    code.extend(mips)
                    code.append(f'\tli {helper_reg} {items[2]}')
                    code.append(f'\tsw {helper_reg}, {offset}($fp)')
                    pass
                else:
                    print(items[2])
                    raise NotImplementedError
        elif len(items) == 4:
            # a = unop b
            offset = self.locations[items[0]][1]
            reg, mips = self.regs.get_register()
            code.extend(mips)
            code.extend(self.handle_unOp(items[2], items[3], reg))
            code.append(f'\tsw {reg}, {offset}($fp)')

        elif len(items) == 5:
            # a = b binop c
            # a = & * b
            if items[2] == '&' and items[3] == '*': 
                offset = self.locations[items[0]][1]
                old_reg, mips = self.regs.get_register(items[2])
                code.extend(mips)
                code.append(f'\tsw {old_reg}, {offset}($fp)')
            else:
                offset = self.locations[items[0]][1]
                reg, mips = self.regs.get_register()
                code.extend(mips)
                code.extend(self.handle_binOp(items[2], items[4], items[3], reg))
                reg2, mips2 = self.regs.get_register()
                code.extend(mips2)
                code.append(f'\tadd {reg2}, {reg}, $0')
                code.append(f'\tsw {reg2}, {offset}($fp)')
        elif len(items) == 6:
            # a = * b binop c
            # a = b binop * c
            if items[2] == '*': 
                offset = self.locations[items[0]][1]
                reg, mips = self.regs.get_register()
                code.extend(mips)
                new_reg, mips = self.regs.get_register()
                code.extend(mips)
                code.extend(self.handle_unOp(items[2], items[3], new_reg))
                binop_reg, mips = self.regs.get_register()
                code.extend(mips)
                code.extend(self.handle_binOp(new_reg, items[4], binop_reg, isreg1 = True))
                code.append("\tadd {reg}, {binop_reg}, $0")
                code.append('\tsw {binop_reg}, {offset}($fp)')
            elif p[4] == '*':
                offset = self.locations[items[0]][1]
                reg, mips = self.regs.get_register()
                code.extend(mips)
                new_reg, mips = self.regs.get_register()
                code.extend(mips)
                code.extend(self.handle_unOp(items[4], items[5], new_reg))
                binop_reg, mips = self.regs.get_register
                code.extend(mips)
                code.extend(self.handle_binOp(items[2], new_reg, binop_reg, isreg2 = True))
                code.append("\tadd {reg}, {binop_reg}, $0")
                code.append('\tadd {reg}, {offset}($fp)')
        else:
            print(items)
            raise NotImplementedError

        return code


    def handle_temp(self, items):
        code = []
        if len(items) == 3:
            # a = b
            if items[2].startswith('temp'):
                old_reg, mips = self.regs.get_register(items[2])
                code.extend(mips)
                find_new_reg, mips = self.regs.get_register(items[0])
                code.extend(mips)
                code.append(f'\tadd {find_new_reg}, {old_reg}, $0')
            elif items[2].startswith('args'):
                find_new_reg, mips = self.regs.get_register(items[0])
                code.extend(mips)
                offset = items[2].split('_')[-1].split('.')[0][:-1]
                if len(items[2].split('_')[-1].split('.')) > 1: 
                    if items[2].split('_')[-1].split('.')[1] == 'length':
                        offset += 4 
                    else:
                        offset += 8
                code.append(f'\tlw {find_new_reg}, {offset}($fp)')
            elif items[2].startswith('var_temp'):
                retReg, mips = self._get_label(items[2])
                retReg = retReg[0] ## Both point to same location
                find_new_reg, mips = self.regs.get_register(items[0])
                code.extend(mips)
                code.append(f'\tadd {find_new_reg}, {retReg}, $0')

            elif items[2].startswith('retval'):
                funcName = items[2].split('_')[1]
                num_returns = len(
                    self.stm.functions[funcName]['return'])
                if num_returns == 1:
                    reg, mips = self.regs.get_register(items[0])
                    code.append(f'\taddi {reg}, $v0, $0')
                else:
                    ret_reg, mips = self.handle_returns(items[2])
                    code.extend(mips)
                    reg, mips = self.regs.get_register(items[0])
                    code.extend(mips)
                    code.append(f'\taddi {reg}, {ret_reg}, $0')
            else:
                if items[2][0] == '"':
                    # string: TODO
                    pass
                elif items[2].isnumeric():
                    if str(int(items[2])) == items[2]:
                        # integer
                        reg, mips = self.regs.get_register(items[0]):
                        code.extend(mips)
                        code.append(f'\tli {reg}, {items[2]}')
                        pass
                    else:
                        # float
                        reg, mips = self.regs.get_register(items[0], isFloat = True)
                        code.extend(mips)
                        code.append(f'\tli.s {reg}, {items[2]}')
                        pass
                elif items[2][0] == "'":
                    # rune
                    reg, mips = self.regs.get_register(items[0])
                    code.extend(mips)
                    code.append(f'\tli {reg} {items[2]}')
                    pass
                else:
                    print(items[2])
                    raise NotImplementedError
        elif len(items) == 4:
            # a = unop b
            reg, mips = self.regs.get_register(items[0])
            code.extend(mips)
            code.extend(self.handle_unOp(items[2], items[3], reg))

        elif len(items) == 5:
            # a = b binop c
            # a = & * b
            if items[2] == '&' and items[3] == '*': 
                old_reg, mips = self.regs.get_register(items[2])
                code.extend(mips)
                find_new_reg, mips = self.regs.get_register(items[0])
                code.extend(mips)
                code.append(f'\tadd {find_new_reg}, {old_reg}, $0')
            else:
                reg, mips = self.regs.get_register()
                code.extend(mips)
                code.extend(self.handle_binOp(items[2], items[4], items[3], reg))
                reg2, mips2 = self.regs.get_register(items[0])
                code.extend(mips2)
                code.append(f'\tadd {reg2}, {reg}, $0')
        elif len(items) == 6:
            # a = * b binop c
            # a = b binop * c
            if items[2] == '*': 
                reg, mips = self.regs.get_register(items[0])
                code.extend(mips)
                new_reg, mips = self.regs.get_register()
                code.extend(mips)
                code.extend(self.handle_unOp(items[2], items[3], new_reg))
                binop_reg, mips = self.regs.get_register
                code.extend(mips)
                code.extend(self.handle_binOp(new_reg, items[4], binop_reg, isreg1 = True))
                code.append("\tadd {reg}, {binop_reg}, $0")
            elif p[4] == '*':
                reg, mips = self.regs.get_register(items[0])
                code.extend(mips)
                new_reg, mips = self.regs.get_register()
                code.extend(mips)
                code.extend(self.handle_unOp(items[4], items[5], new_reg))
                binop_reg, mips = self.regs.get_register
                code.extend(mips)
                code.extend(self.handle_binOp(items[2], new_reg, binop_reg, isreg2 = True))
                code.append("\tadd {reg}, {binop_reg}, $0")

        else:
            print(items)
            raise NotImplementedError

        return code

    def handle_args(self, items): 
        code = []
        if len(items) == 3:
            # a = b
            if items[2].startswith('temp'):
                offset = items[0].split('_')[-1].split('.')[0][:-1]
                find_new_reg, mips = self.regs.get_register(items[0])
                code.extend(mips)
                code.append(f'\tsw {find_new_reg}, {offset}($fp)')
            elif items[2].startswith('args'):
                offset1 = items[0].split('_')[-1].split('.')[0][:-1]
                offset2 = items[2].split('_')[-1].split('.')[0][:-1]
                if len(items[2].split('_')[-1].split('.')) > 1: 
                    if items[2].split('_')[-1].split('.')[1] == 'length':
                        offset2 += 4 
                    else:
                        offset2 += 8
                helper_reg, mips = self.regs.get_register()
                code.extend(mips)  
                code.append(f'\tlw {helper_reg}, {offset2}($fp)')
                code.append(f'\tsw {helper_reg}, {offset1}($fp)') 
            elif items[2].startswith('var_temp'):
                retReg, mips = self._get_label(items[2])
                retReg = retReg[0] ## Both point to same location
                offset = items[0].split('_')[-1].split('.')[0][:-1]
                code.append(f'\tsw {retReg}, {offset}($fp)')

            elif items[2].startswith('retval'):
                funcName = items[2].split('_')[1]
                num_returns = len(
                    self.stm.functions[funcName]['return'])
                if num_returns == 1:
                    reg, mips = self.regs.get_register(items[0])
                    code.append(f'\taddi {reg}, $v0, $0')
                else:
                    ret_reg, mips = self.handle_returns(items[2])
                    code.extend(mips)
                    offset = items[0].split('_')[-1].split('.')[0][:-1]
                    code.append(f'\tlw {ret_reg}, {offset}($fp)')
            else:
                if items[2][0] == '"':
                    # string: TODO
                    pass
                elif items[2].isnumeric():
                    if str(int(items[2])) == items[2]:
                        # integer
                        offset = items[0].split('_')[-1].split('.')[0][:-1]
                        helper_reg, mips = self.regs.get_register()
                        code.extend(mips) 
                        code.append(f'\tli {helper_reg}, {items[2]}')
                        code.append(f'\tsw {reg}, {offset}($fp)')
                        pass
                    else:
                        # float
                        offset = items[0].split('_')[-1].split('.')[0][:-1]
                        helper_reg, mips = self.regs.get_register(items[0], isFloat = True)
                        code.extend(mips)
                        code.append(f'\tli.s {helper_reg}, {items[2]}')
                        code.append(f'\s.s {helper_reg}, {offset}($fp)')
                        pass
                elif items[2][0] == "'":
                    # rune
                    offset = items[0].split('_')[-1].split('.')[0][:-1]
                    helper_reg, mips = self.regs.get_register(items[0])
                    code.extend(mips)
                    code.append(f'\tli {helper_reg} {items[2]}')
                    code.append(f'\tsw {helper_reg}, {offset}($fp)')
                    pass
                else:
                    print(items[2])
                    raise NotImplementedError
        elif len(items) == 4:
            # a = unop b
            offset = items[0].split('_')[-1].split('.')[0][:-1]
            reg, mips = self.regs.get_register()
            code.extend(mips)
            code.extend(self.handle_unOp(items[2], items[3], reg))
            code.append(f'\tsw {reg}, {offset}($fp)')

        elif len(items) == 5:
            # a = b binop c
            # a = & * b
            if items[2] == '&' and items[3] == '*': 
                offset = items[0].split('_')[-1].split('.')[0][:-1]
                old_reg, mips = self.regs.get_register(items[2])
                code.extend(mips)
                code.append(f'\tsw {old_reg}, {offset}($fp)')
            else:
                offset = items[0].split('_')[-1].split('.')[0][:-1]
                reg, mips = self.regs.get_register()
                code.extend(mips)
                code.extend(self.handle_binOp(items[2], items[4], items[3], reg))
                reg2, mips2 = self.regs.get_register()
                code.extend(mips2)
                code.append(f'\tadd {reg2}, {reg}, $0')
                code.append(f'\tsw {reg2}, {offset}($fp)')
        elif len(items) == 6:
            # a = * b binop c
            # a = b binop * c
            if items[2] == '*': 
                offset = items[0].split('_')[-1].split('.')[0][:-1]
                reg, mips = self.regs.get_register()
                code.extend(mips)
                new_reg, mips = self.regs.get_register()
                code.extend(mips)
                code.extend(self.handle_unOp(items[2], items[3], new_reg))
                binop_reg, mips = self.regs.get_register()
                code.extend(mips)
                code.extend(self.handle_binOp(new_reg, items[4], binop_reg, isreg1 = True))
                code.append("\tadd {reg}, {binop_reg}, $0")
                code.append('\tsw {binop_reg}, {offset}($fp)')
            elif p[4] == '*':
                offset = items[0].split('_')[-1].split('.')[0][:-1]  
                reg, mips = self.regs.get_register()
                code.extend(mips)
                new_reg, mips = self.regs.get_register()
                code.extend(mips)
                code.extend(self.handle_unOp(items[4], items[5], new_reg))
                binop_reg, mips = self.regs.get_register
                code.extend(mips)
                code.extend(self.handle_binOp(items[2], new_reg, binop_reg, isreg2 = True))
                code.append("\tadd {reg}, {binop_reg}, $0")
                code.append('\tadd {reg}, {offset}($fp)')
        else:
            print(items)
            raise NotImplementedError

        return code

    def handle_param(self, param):
        # print(self.stm.get(param))
        # TODO : Handle vartemp and sizes
        found = 0
        code = []
        for i in range(4):
            if self.regs.arg_regs[f'$a{i}'][0] != None:
                found = 1
                if not param.startswith('var_temp'):
                    self.regs.arg_regs[f'$a{i}'][0] = param
                    self.regs.arg_regs[f'$a{i}'][1] = self.count
                    self.count += 1
                    reg, mips = self.regs.get_register(param)
                    code.extend(mips)
                    code.append(f'\tadd $a{i}, {reg}, $0')
                    break
                else:
                    offset = self.regs.locations[param.split('.')[0]][1]
                    if param.endswith('.addr'):
                        # params var_temp#x.addr
                        self.regs.arg_regs[f'$a{i}'][0] = param
                        self.regs.arg_regs[f'$a{i}'][1] = self.count
                        self.count += 1
                        code.append(f'\tlw $a{i}, {offset}($fp)')
                    elif param.endswith('.length'):
                        # params var_temp#x.length
                        self.regs.arg_regs[f'$a{i}'][0] = param
                        self.regs.arg_regs[f'$a{i}'][1] = self.count
                        self.count += 1
                        code.append(f'\tlw $a{i}, {offset + 4}($fp)')
                    elif param.endswith('.capacity'):
                        self.regs.arg_regs[f'$a{i}'][0] = param
                        self.regs.arg_regs[f'$a{i}'][1] = self.count
                        self.count += 1
                        code.append(f'\tlw $a{i}, {offset + 8}($fp)')
                    else:
                        pass

        if not found:
            if not param.startswith('var_temp'):
                reg, mips = self.regs.get_register(param)
                code.extend(mips)
                code.append(f'\taddi $sp, $sp, -4')
                code.append(f'\tsw {reg} ($sp)')
            else:
                offset = self.regs.locations[param.split('.')[0]][1]
                if param.endswith('.addr'):
                    reg, mips = self.regs.get_register()
                    code.extend(mips)
                    code.append(f'\tlw {reg} {offset}($fp)')
                    code.append(f'addi $sp, $sp, -4')
                    code.append(f'\tsw {reg} ($sp)')
                elif param.endswith('.length'):
                    reg, mips = self.regs.get_register()
                    code.extend(mips)
                    code.append(f'\tlw {reg} {offset + 4}($fp)')
                    code.append(f'addi $sp, $sp, -4')
                    code.append(f'\tsw {reg} ($sp)')
                elif param.endswith('.capacity'):
                    reg, mips = self.regs.get_register()
                    code.extend(mips)
                    code.append(f'\tlw {reg} {offset + 8}($fp)')
                    code.append(f'addi $sp, $sp, -4')
                    code.append(f'\tsw {reg} ($sp)')
                else:
                    reg, mips = self.regs.get_register()
                    code.extend(mips)
                    code.append(f'\tlw {reg} {offset}($fp)')
                    code.append(f'addi $sp, $sp, -4')
                    code.append(f'\tsw {reg} ($sp)')
                    code.append(f'\tlw {reg} {offset + 4}($fp)')
                    code.append(f'addi $sp, $sp, -4')
                    code.append(f'\tsw {reg} ($sp)')
                    code.append(f'\tlw {reg} {offset + 8}($fp)')
                    code.append(f'addi $sp, $sp, -4')
                    code.append(f'\tsw {reg} ($sp)')

        return code

    def handle_returns(self, returnval):
        funcName = returnval.split['_'][1]
        num = int(returnval.split['_'][2])

        code = []
        offset = 0
        for idx, retVal in enumerate(self.stm.functions[funcName]['return']):
            if idx == num:
                break
            offset += retVal['size']

        reg, mips = self.regs.get_register()
        code.extend(mips)
        code.append(f'\tlw {reg}, {offset}($v0)')
        return reg, code

    def handle_label(self, label):
        return [f"{label}:"]

    def handle_goto(self, label):
        code = []
        code.append(f"\tj {label}")
        return code

    def handle_ifStmt(self, cond, elselab):
        code = []
        reg = self.regs.get_register(cond)
        code.extend(reg[1])
        code.append(f"\tbeqz {reg[0]}, {elselab}")
        return code

    def handle_floatBinOp(self, operand1, operand2, operator, finalreg, isreg1 = False, isreg2 = False):
        code = []
        reg1 = operand1  
        reg2 = operand2 
        if not isreg1:
            reg1, mips = self._get_label(operand1, isFloat=True)
            code.extend(mips)
        if not isreg2:
            reg2, mips = self._get_label(operand2, isFloat=True)
            code.extend(mips)
        reg3, mips = self.get_register(isFloat=True)
        code.extend(mips)

        if operator.startswith('+'):
            code.append(f'\tadd.s {reg3}, {reg1}, {reg2}')
            code.append(f'\tmfc1 {finalreg}, {reg3}')
        elif operator.startswith('-'):
            code.append(f'\tsub.s {reg3}, {reg1}, {reg2}')
            code.append(f'\tmfc1 {finalreg}, {reg3}')
        elif operator.startswith('*'):
            code.append(f'\tmul.s {reg3}, {reg1}, {reg2}')
            code.append(f'\tmfc1 {finalreg}, {reg3}')
        elif operator.startswith('/'):
            code.append(f'\tdiv.s {reg3}, {reg1}, {reg2}')
            code.append(f'\tmfc1 {finalreg}, {reg3}')
        elif operator.startswith('<='):
            code.append(f'\tc.le.s {reg1}, {reg2}')
            code.append(f'cfc1 {finalreg}, {reg3}')
        elif operator.startswith('>='):
            code.append(f'\tc.ge.s {reg1}, {reg2}')
            code.append(f'cfc1 {finalreg}, {reg3}')
        elif operator.startswith('<'):
            code.append(f'\tc.lt.s {reg1}, {reg2}')
            code.append(f'cfc1 {finalreg}, {reg3}')
        elif operator.startswith('>'):
            code.append(f'\tc.gt.s {reg1}, {reg2}')
            code.append(f'cfc1 {finalreg}, {reg3}')
        elif operator.startswith('=='):
            code.append(f'\tc.eq.s {reg1}, {reg2}')
            code.append(f'cfc1 {finalreg}, {reg3}')
        elif operator.startswith('!='):
            code.append(f'\tc.ne.s {reg1}, {reg2}')
            code.append(f'cfc1 {finalreg}, {reg3}')
        return code

    def handle_intBinOp(self, operand1, operand2, operator, finalreg, isreg1 = False, isreg2 = False):
        code = []
        reg1 = operand1
        reg2 = operand2
        if not isreg1:
            reg1, mips = self._get_label(operand1)
            code.extend(mips)
        if not isreg2:
            reg2, mips = self._get_label(operand2)
            code.extend(mips)
        if operator.startswith('+'):
            code.append(f'\tadd {finalreg}, {reg1}, {reg2}')

        elif operator.startswith('||') or operator.startswith('|'):
            code.append(f'\tor {finalreg}, {reg1}, {reg2}')

        elif operator.startswith('&&') or operator.startswith('&'):
            code.append(f'\tand {finalreg}, {reg1}, {reg2}')

        elif operator.startswith('-'):
            code.append(f'\tsub {finalreg}, {reg1}, {reg2}')

        elif operator.startswith('*'):
            code.append(f'\tmult {reg1}, {reg2}')
            code.append(f'\tmflo {finalreg}')

        elif operator.startswith('/'):
            code.append(f'\tdiv {reg1}, {reg2}')
            code.append(f'\tmflo {finalreg}')

        elif operator.startswith('%'):
            code.append(f'\tdiv {reg1}, {reg2}')
            code.append(f'\tmfhi {finalreg}')

        elif operator.startswith('>>'):
            code.append(f'\tsrav {finalreg}, {reg1}, {reg2}')

        elif operator.startswith('<<'):
            code.append(f'\tsllv {finalreg}, {reg1}, {reg2}')

        elif operator.startswith('<='):
            code.append(f'\tslt {finalreg}, {reg2}, {reg1}')
            code.append(f'\txori {finalreg}, {finalreg}, 1')

        elif operator.startswith('>='):
            code.append(f'\tslt {finalreg}, {reg1}, {reg2}')
            code.append(f'\txori {finalreg}, {finalreg}, 1')

        elif operator.startswith('^'):
            code.append(f'\txor {finalreg}, {reg1}, {reg2}')

        elif operator.startswith('<'):
            code.append(f'\tslt {finalreg}, {reg1}, {reg2}')

        elif operator.startswith('>'):
            code.append(f'\tslt {finalreg}, {reg2}, {reg1}')

        elif operator.startswith('=='):
            reg3, mips = self.regs.get_register()
            code.extend(mips)
            code.append(f'\tslt {finalreg}, {reg1}, {reg2}')
            code.append(f'\txori {finalreg}, {finalreg}, 1')
            code.append(f'\tslt {reg3}, {reg2}, {reg1}')
            code.append(f'\txori {reg3}, {reg3}, 1')
            code.append(f'\tand {finalreg}, {finalreg}, {reg3}')

        elif operator.startswith('!='):
            reg3, mips = self.regs.get_register()
            code.extend(mips)
            code.append(f'\tslt {finalreg}, {reg1}, {reg2}')
            code.append(f'\tslt {reg3}, {reg2}, {reg1}')
            code.append(f'\tor {finalreg}, {finalreg}, {reg3}')

        return code

    def handle_binOp(self, operand1, operand2, operator, finalreg, isreg1 = False, isreg2 = False):

        if 'float' in operator:
            return self.handle_floatBinOp(operand1, operand2, operator, finalreg, isreg1, isreg2)
        else:
            return self.handle_intBinOp(operand1, operand2, operator, finalreg, isreg1, isreg2)

    def handle_unOp(self, opr, operand, finalreg):
        code = []
        if opr == '+':
            return []

        elif opr[0] == '-':
            if 'float' in opr:
                isFloat = True 
            reg, mips = self.regs.get_register(operand, isFloat = isFloat)
            code.extend(mips)
            code.append(f'\tsubi {finalreg}, 0, {reg}')
            return code

        elif opr[0] == '*':
            reg, mips = self.regs.get_register(operand)
            code.extend(mips)

            code.append("\tlw {finalreg} (reg)")
            return code

        elif opr[0] == '&':
            addr = self.regs.locations[operand][1]

            code.append(f'\tla {finalreg}, {addr}')
            return code

        elif opr[0] == '!':
            reg, mips = self.regs.get_register(operand)
            code.extend(mips)
            code.append(f'\tnor {finalreg}, {reg}, $0')

        elif opr[0] == '^':
            reg, mips = self.regs.get_register(operand)
            code.extend(mips)
            reg_helper, mips = self.regs.get_register()
            code.extend(mips)
            code.append(f'\tli {reg_helper} -1')
            code.append(f'\txor {finalreg}, {reg}, {reg_helper}')

        return code

    def handle_typecast(self):
        ## TODO
        pass

    def dosyscall(self, number):
        return [f"\tli $v0 {number}", "\tsyscall"]

    def malloc(self, space):
        code = []
        if type(space) != str:
            code.append(f"\tli $a0 {space}")
        else:
            code.append(f"\tadd $a0 $0 {space}")
        code.extend(self.dosyscall(9))
        return code

    def exit(self):
        return self.dosyscall(10)
