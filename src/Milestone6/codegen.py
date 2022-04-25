from calendar import c
from scope import *
from utils import *


class Register:
    def __init__(self):

        # Counter for the used for spilling of registers
        # while using LRU strategy
        # Used for both GPR and FPR
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
            self.regsSavedF[f'$f{i}'] = [None, 0]

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
        self.cur_func_size = 0
        self._sp = 0

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
                        minn = self.regsSavedF[reg][1]
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
                    if new_loc is None:
                        if reg in self.regs and self.regs[reg][0]:
                            self.locations[self.regs[reg][0]] = [1, self._sp]
                        elif reg in self.regsSaved and self.regsSaved[reg][0]:
                            self.locations[self.regsSaved[reg][0]] = [1, self._sp]

                        new_loc_i = self._sp
                    elif new_loc[i] != None:  # To be stored in memory
                        new_loc_i = new_loc[i]
                    else:
                        raise Exception("Please provide a valid memory location")

                    if (reg.startswith('$s') and self.regsSaved[reg][0] != None) or (reg in self.regs and self.regs[reg][0] != None):
                        suffix = getsizeSuffix(size, isFloat, isUnsigned)
                        self._sp -= 4
                        new_loc_i -= 4
                        mips.append("\tadd $sp, $sp, -4")
                        mips.append("\ts" + suffix + "\t" + reg +
                                "," + str(self._sp - self.cur_func_size - 32) + "($fp)\n")

                    # Reset after shifting
                    
                    if reg in self.regs and self.regs[reg][0] != None:
                        self.locations[self.regs[reg][0]][0] = 1
                        self.locations[self.regs[reg][0]][1] = new_loc_i
                        self.regs[reg][0] = None
                        self.regs[reg][1] = 0
                    elif reg in self.regsSaved and self.regsSaved[reg][0] != None:
                        self.locations[self.regsSaved[reg][0]][0] = 1
                        self.locations[self.regsSaved[reg][0]][1] = new_loc_i
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
                    if new_loc is None:
                        if reg in self.regsF and self.regsF[reg][0]:
                            self.locations[self.regsF[reg][0]] = [1, self._sp]
                        elif reg in self.regsSavedF and self.regsSavedF[reg][0]:
                            self.locations[self.regsSavedF[reg][0]] = [1, self._sp]

                        new_loc_i = self._sp
                    elif new_loc[i] != None:  # To be stored in memory
                        new_loc_i = new_loc[i]
                    else:
                        raise Exception("Please provide a valid memory location")

                    if (reg.startswith('$s') and self.regsSavedF[reg][0]) or (self.regsF[reg][0]):
                        suffix = getsizeSuffix(size, isFloat, isUnsigned)
                        self._sp -= 4
                        mips.append("\tStoring {var}")
                        mips.append('\taddi $sp, $sp, -4')
                        mips.append("\ts" + suffix + "\t" + reg +
                                "," + str(self._sp-self.cur_func_size-32) + "($fp)\n")

                    # Reset after shifting
                    
                    if reg in self.regsF and self.regsF[reg][0]:
                        self.locations[self.regsF[reg][0]][0] = 1
                        self.locations[self.regsF[reg][0]][1] = new_loc_i
                        self.regsF[reg][0] = None
                        self.regsF[reg][1] = 0
                    elif reg in self.regsSavedF and self.regsSavedF[reg][0]:
                        self.locations[self.regsSavedF[reg][0]][0] = 1
                        self.locations[self.regsSavedF[reg][0]][1] = new_loc_i
                        self.regsSavedF[reg][0] = None
                        self.regsSavedF[reg][1] = 0

            print("Instruction generated: ", mips)
            return mips

    # Function that returns a tuple of register and instructions
    # for a variable var. This function also has to be used while
    # fetching location for a variable for execution of LRU policy
    def get_register(self, var=None, size=None, isFloat=False, isUnsigned=False, funcName = None):
        mips = []   
        if var in self.locations and self.locations[var][0] == 0:
            self.count += 1
            if not isFloat:
                if self.locations[var][1].startswith('$s'):
                    self.regsSaved[self.locations[var][1]][1] = self.count    
                else:
                    self.regs[self.locations[var][1]][1] = self.count
                return (self.locations[var][1], [])
            else:
                if self.locations[var][1] in self.regsSavedF:
                    self.regsSavedF[self.locations[var][1]][1] = self.count    
                else:
                    self.regsF[self.locations[var][1]][1] = self.count
                return (self.locations[var][1], [])

        else:  # Need a new register
            new_reg = self.find_new_reg(isFloat=isFloat)
            mips.extend(self.move_reg([new_reg]))

            self.count += 1
            if not isFloat:
                if new_reg.startswith('$s'):
                    self.regsSaved[new_reg][0] = var
                    self.regsSaved[new_reg][1] = self.count
                else: 
                    self.regs[new_reg][0] = var
                    self.regs[new_reg][1] = self.count
            else:
                if new_reg.startswith('$s'):
                    self.regsSavedF[new_reg][0] = var
                    self.regsSavedF[new_reg][1] = self.count
                else:
                    self.regsF[new_reg][0] = var
                    self.regsF[new_reg][1] = self.count

            # It is stored in memory
            if var in self.locations and self.locations[var][0] == 1:
                self.locations[var][0] = 0
                temp = self.locations[var][1]
                self.locations[var][1] = new_reg
                mips.append(f'\t# Swapping out reg {new_reg} for variable {var}')
                suffix = getsizeSuffix(size, isFloat, isUnsigned)
                # print("ASD: ", self.locations[var], var)
                mips.append(f"\t# Changed {var}")
                mips.append("\tl" + suffix + "\t" +
                          str(new_reg) + "," +  str(temp - self.cur_func_size - 32) + "($fp)")
            elif var is not None:
                self.locations[var] = [0, new_reg]

            return (new_reg, mips)

    def _func_arg_size_on_stack(self, stm, funcname, local_var_size):
        param_size = 0 
        params = stm.get(funcname)['params']
        if len(params) > 4: 
            for i in range(4, len(params)):
                param_size += params[i]['size']
        tot_size = param_size
        self.cur_func_size = local_var_size
        return tot_size

class ActivationRecord:
    def __init__(self, local_var_space = None):
        self.returnval_space = None 
        self.param_space = None
        self.old_base_ptr_space = 4
        self.localvar_space = local_var_space
        self.saved_registers_space = 128
        self.return_address_space = 4

        self.local_var = {}
        self.args = {}

# Class to implement code generation from 3AC and symtable to MIPS
class MIPS:

    def __init__(self, code, stm):
        self.regs = Register()
        self.instr = []
        self.INDENT = " " * 4
        self.tac_code  = code
        self.stm: SymTableMaker = stm
        self.builtins = ['Print', 'Scan', 'Typecast']
        self.fpOffset = 0  # Offset from frame pointer

        self.global_var = {}
        self.global_var_size=0
        self.act_records: dict[str, ActivationRecord] = {}
        self.curr_func = ""
        self.curr_pkg = None

    def _location(self, label, isFloat = False):
        if label in self.act_records[self.curr_func].local_var:
            return (f'{self.act_records[self.curr_func].local_var[label]["offset"]-32}($fp)', [], 1)
        elif label in self.global_var:
            return (f'{self.global_var[label]["offset"]}($gp)', [], 1)
        elif label[0].isnumeric() and '_' in label:
            label = label.split('.')

            if len(label) > 1:
                temp_reg, code = self.regs.get_register()
                code.append(f'\tlw {temp_reg}, {self.act_records[self.curr_func].local_var[label[0]]["offset"]}($fp)')
                if label[1] == 'addr':
                    code.append(f"\tlw {temp_reg}, 0({temp_reg})")
                elif label[1] == 'len':
                    code.append(f"\tlw {temp_reg}, 4({temp_reg})")
                elif label[1] == 'cap':
                    code.append(f"\tlw {temp_reg}, 8({temp_reg})")
                else:
                    raise Exception("Some syntax error in 3ac code")

                return (temp_reg, code, 0)

            offset = self.regs.locations[label[0]][1] - self.act_records[self.curr_func].localvar_space

            return (f"{offset-32}($fp)", [f"\t### LOCATION {label} : {offset}"], 1)
        elif label in self.regs.locations:
            reg, mips = self.regs.get_register(label, isFloat = isFloat)
            mips.append(f"\t# {reg}, {label}")
            return (reg, mips, 0)
        else:
            raise NotImplementedError

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
                if var == '_':
                    continue
                code.append(self._getDataCode(detail))
                self.global_var[detail['tmp']] = {'size': detail['dataType']['size'], 'offset': self.global_var_size}
                self.global_var_size += detail['dataType']['size']

        for var, detail in self.stm.symTable[0].localsymTable.items():
            if var == '_':
                continue
            code.append(self._getDataCode(detail))
            self.global_var[detail['tmp']] = {'size': detail['dataType']['size'], 'offset': self.global_var_size}
            self.global_var_size += detail['dataType']['size']

        code.append("\t_nl: .asciiz \"\\n\"")

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
        code = ['.text', '.globl main\n']
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

    def _addLocalCompositeVars(self):
        code = []
        for local_var, lv_info in self.act_records[self.curr_func].local_var.items():
            if lv_info['dataType']['name'] in compositeTypes:
                # code.append('COMPOSITE')
                
                code.append('\tli $a0, 12')
                code.append('\tli $v0, 9')
                code.append('\tsyscall')
                code.append(f'\tsw $v0, {lv_info["offset"]}($fp)')
            
                if lv_info['dataType']['name'] == 'array':
                    code.append(f"\tli $a0, {lv_info['dataType']['baseType']['size']*lv_info['dataType']['length']}")
                    code.append(f"\tsw $a0, 4($v0)")
                    code.append(f"\tsw $a0, 8($v0)")
                    new_reg , _code = self.regs.get_register(local_var)
                    code.extend(_code)
                    code.append('\tli $v0, 9')
                    code.append('\tsyscall')
                    code.append(f'\tsw $v0, 0({new_reg})')
                    
            
                if lv_info['dataType']['name'] == 'slice':
                    code.append(f"\tli $a0, {lv_info['dataType']['baseType']['size']*lv_info['dataType']['length']}")
                    code.append(f"\tsw $a0, 4($v0)")
                    code.append(f"\tsw $a0, 8($v0)")

        return code

    def addFunction(self, lineno):
        code = []
        funcname = self.tac_code[lineno].split(' ')[1]
        self.curr_func = funcname
        if funcname != 'main':
            code.extend(self.handle_label('_'+funcname))
        else:
            code.extend(self.handle_label(funcname))
            code.append('\taddi $sp, $sp, -128')
            code.append('\tadd $fp, $sp, $0')

        self.act_records[funcname] = ActivationRecord()

        local_var_size = 0

        if funcname in self.stm.functions and self.stm.symTable[self.stm.functions[funcname]['scope']+1].parentScope == self.stm.functions[funcname]['scope']:
            for local_var, lv_info in self.stm.symTable[self.stm.functions[funcname]['scope']+1].localsymTable.items():
                local_var_size += lv_info['dataType']['size']
                self.act_records[funcname].local_var[lv_info['tmp']] = {'size': lv_info['dataType']['size'], 'offset': -local_var_size, 'dataType': lv_info['dataType']}
                self.regs.locations[lv_info['tmp']] = [1, -local_var_size]

        if funcname in self.stm.functions and self.stm.symTable[self.stm.functions[funcname]['scope']+1].parentScope == self.stm.functions[funcname]['scope']:
            for local_var, lv_info in self.stm.symTable[self.stm.functions[funcname]['scope']+1].localsymTable.items():
                self.regs.locations[lv_info['tmp']][1] += local_var_size

        for key in self.stm.pkgs:
            if funcname in self.stm.pkgs[key].functions:
                self.curr_pkg = key
                for local_var, lv_info in self.stm.pkgs[key].symTable[self.stm.pkgs[key].functions[funcname]['scope']+1].localsymTable.items():
                    local_var_size += lv_info['dataType']['size']
                    self.act_records[funcname].local_var[lv_info['tmp']] = {'size': lv_info['dataType']['size'], 'offset': -local_var_size}
                    self.regs.locations[lv_info['tmp']] = [1, -local_var_size]

            if funcname in self.stm.pkgs[key].functions:
                self.curr_pkg = key
                for local_var, lv_info in self.stm.pkgs[key].symTable[self.stm.pkgs[key].functions[funcname]['scope']+1].localsymTable.items():
                    self.regs.locations[lv_info['tmp']][1] += local_var_size

        self.act_records[self.curr_func].localvar_space = local_var_size
        stack_return_size = self.regs._func_arg_size_on_stack(self.stm, funcname, local_var_size)
        
        code.append(f'\taddi $sp, $sp, -4')
        code.append(f'\tsw $ra, 0($sp)')
        code.append(f'\taddi $sp, $sp, -4')
        code.append(f'\tsw $fp, 0($sp)')
        code.append(f'\tadd $fp, $sp, $0')
        code.append(f'\taddi $sp, $sp, -{local_var_size}')

        code.append(f'\t### Saving $s registers')
        for reg in self.regs.regsSaved:
            self.regs._sp -= 4
            code.append(f'\tadd $sp, $sp, -4')
            code.append(f'\tsw {reg}, 0($sp)')
            self.regs.regsSaved[reg][0] = None

        code.extend(self._addLocalCompositeVars())

        for i in range(lineno+1, len(self.tac_code)):
            print(f"Handling TAC line: {self.tac_code[i]}")
            items = self.tac_code[i].split(' ')
            if self.tac_code[i].startswith('Func END'):
                code.append(f'\t_return_{funcname}:')
                code.append(f'\t### Restoring $s registers')
                saved_regs = list(self.regs.regsSaved.keys())
                saved_regs.reverse()
                for reg in saved_regs:
                    self.regs._sp += 4
                    code.append(f'\tlw {reg}, 0($sp)')
                    code.append(f'\tadd $sp, $sp, 4')
                    self.regs.regsSaved[reg][0] = None
                code.append(f'\tlw $ra, 4($fp)')
                code.append(f'\taddi $sp, $fp, {stack_return_size + 8}')
                code.append(f'\tlw $fp, 0($fp)')
                self.regs._sp = 0

                if funcname != 'main':
                    code.append(f'\tjr $ra')
                else:
                    code.extend(self.exit())
                return code

            elif self.tac_code[i].startswith('return'):
                j = 1
                retValues = []
                retTypes = []
                while self.tac_code[i-j].startswith('retparams'):
                    if 'float' in self.tac_code[i-j]:
                        retTypes.append('float')
                    else:
                        retTypes.append('int')
                    ret_items = self.tac_code[i-j].split()
                    retValues.append(ret_items[1])
                    j += 1

                retValues.reverse()
                retTypes.reverse()
                retReg, _code = self._get_label(retValues[0], isFloat=(retTypes[0] == 'float'))
                code.extend(_code)
                if len(self.stm.functions[funcname]['return']) == 1 and not retValues[0].startswith("vartemp"):
                    if retTypes[0] == 'float':
                        code.append(f"\tmov.s $f0, {retReg}")  # Check later if it doesn't work
                    else:
                        code.append(f"\taddi $v0, {retReg}, 0") 
                else:
                    retSize = 0
                    for retVal in self.stm.functions[funcname]['return']:
                        retSize += retVal['size']
                    code.extend(self.malloc(retSize))

                    offset = 0
                    for idx, retVal in enumerate(self.stm.functions[funcname]['return']):
                        retReg, _code = self._get_label(retValues[idx], isFloat=(retTypes[idx]=='float'))
                        code.extend(_code)
                        var = ''
                        if((retTypes[idx]=='float')):
                            var='c1'
                        code.append(f"\tsw{var} {retReg}, {offset}($v0)")
                        offset += retVal['size']
                    code.append(f"\taddi $v1, $0, {retSize}")

            if self.tac_code[i].startswith('temp'):
                reg, mips = self.handle_temp(items)
                code.extend(mips)
            elif self.tac_code[i].startswith('vartemp'):
                pass
            elif self.tac_code[i].startswith('*') or self.tac_code[i].startswith('[]'):
                # * a = b
                # * a = unop b
                # * a = b binop c
                items = self.tac_code[i].split(' ')
                isFloat = 'float' in items[2]
                var = 'c1' if isFloat else ''
                if items[1].startswith('temp'):
                    if len(items) == 4:
                        loc, _mips, type_loc = self._location(items[1])
                        reg, mips = self.regs.get_register(items[3], isFloat=isFloat)
                        code.extend(_mips)
                        code.extend(mips)
                        if type_loc == 1:
                            empty_reg, mips = self.regs.get_register(isFloat=False)
                            code.extend(mips)
                            code.append(f'\tlw {empty_reg} {loc}')
                            code.append(f'\tsw{var} {reg}, 0({empty_reg})')
                        else:
                            code.append(f'\tsw{var} {reg}, 0({loc})')
                    elif len(items) == 5: 
                        reg, mips = self.regs.get_register(isFloat=isFloat)
                        code.extend(mips)
                        code.extend(self.handle_unOp(items[3], items[4], reg))
                        loc, _mips, type_loc = self._location(items[1])
                        code.extend(_mips)
                        if type_loc == 1:
                            empty_reg, mips = self.regs.get_register()
                            code.extend(mips)
                            code.append(f'\tlw {empty_reg} {loc}')
                            code.append(f'\tsw{var} {reg}, 0({empty_reg})')
                        else:
                            code.append(f'\tsw{var} {reg}, 0({loc})')
                    elif len(items) == 6:
                        reg, mips = self.regs.get_register(isFloat=isFloat)
                        code.extend(mips)
                        code.extend(self.handle_binOp(items[3], items[5], items[4], reg))
                        loc, _mips, type_loc = self._location(items[1])
                        code.extend(_mips)
                        if type_loc == 1:
                            empty_reg, mips = self.regs.get_register()
                            code.extend(mips)
                            code.append(f'\tlw {empty_reg} {loc}')
                            code.append(f'\tsw{var} {reg}, 0({empty_reg})')
                        else:
                            code.append(f'\tsw{var} {reg}, 0({loc})')
                elif items[1][0].isnumeric() and '_' in items[1]:
                    loc, _mips, type_loc = self._location(items[1])
                    new_items = items[1:] 
                    new_items[0] = "temp_{fixxx}" 
                    reg, mips = self.handle_temp(new_items, isFloat=isFloat)
                    code.extend(mips)
                    if type_loc == 1:
                        empty_reg, mips = self.regs.get_register()
                        code.extend(mips)
                        code.append(f'\tlw {empty_reg} {loc}')
                        code.append(f'\tsw{var} {reg}, 0({empty_reg})')
                    else:
                        code.append(f'\tsw{var} {reg}, 0({loc})')
                elif items[1].startswith('arg'):
                    reg, mips = self._get_label(items[1])
                    code.extend(mips)
                    # empty_reg, mips = self.regs.get_register()
                    # code.extend(mips)
                    if items[3] == "__syscall":
                        code.append(f"\tsw $v0, 0({reg})")
                    else:
                        reg2, mips = self.regs.get_register(items[3])
                        code.extend(mips)
                        code.append(f'\tsw {reg2} 0({reg})')
                elif items[1].startswith('vartemp'):
                    # TODO
                    pass
            elif self.tac_code[i].startswith('call'):
                ## TODO 
                j = 1
                paramValues = []
                while self.tac_code[i-j].startswith('params'):
                    paramValues.append(self.tac_code[i-j].split()[1])
                    j += 1

                if len(paramValues) > 4:
                    paramValues = paramValues[:-4] 
                    paramValues.reverse()
                    for param in paramValues:
                        reg, mips = self._get_label(param)
                        code.extend(mips)
                        code.append("\tadd $sp, $sp, -4")
                        code.append(f"\tsw {reg}, 0($sp)")

                items = self.tac_code[i].split(' ')
                if i >= 1 and not self.tac_code[i-1].startswith('params'):
                    code.append("\t#### Saving temporary registers")
                    for reg in self.regs.regs:
                        code.append(f"\tadd $sp, $sp, -4")
                        code.append(f"\tsw {reg}, 0($sp)")
                        self.regs._sp -= 4
                    code.append("\t#### Done saving temporary registers")
                    code.append("\t#### Saving argument registers")
                    for reg in self.regs.arg_regs:
                        code.append(f"\tadd $sp, $sp, -4")
                        code.append(f"\tsw {reg}, 0($sp)")
                        self.regs._sp -= 4
                    code.append("\t#### Done saving argument registers")
                    code.append("\t#### Saving Floating Point registers")
                    for reg in self.regs.regsF:
                        code.append(f"\tadd $sp, $sp, -4")
                        code.append(f"\tswc1 {reg}, 0($sp)")
                        self.regs._sp -= 4
                    code.append("\t#### Done saving Floating Point registers")
                    code.append("\t#### Saving Floating Point Argument registers")
                    for reg in self.regs.args_regsF:
                        code.append(f"\tadd $sp, $sp, -4")
                        code.append(f"\tswc1 {reg}, 0($sp)")
                        self.regs._sp -= 4
                    code.append("\t#### Done saving Floating Point Argument registers")
                    # print("MYLOG: ", funcname, self.regs._sp)

                if items[1].startswith('#syscall'):
                    param_count = 0
                    while self.tac_code[i-param_count-1].startswith('params'):
                        param_count -= 1
                    code.insert(len(code)-param_count, f"\tli $v0, {items[1].split('_')[-1]}")
                    code.append('\tsyscall') 
                else:
                    code.append(f'\tjal _{items[1]}')
                for i in range(4):
                    self.regs.arg_regs[f"$a{i}"][0] = None
                code.append(f"\t### Restoring argument registers")
                for i in range(3, -1, -1):
                    code.append(f"\tlw $a{i}, 0($sp)")
                    code.append(f"\tadd $sp, $sp, 4")
                    self.regs._sp += 4
                code.append(f"\t### Done restoring argument registers")
                for i in range(9, -1, -1):
                    code.append(f"\tlw $t{i}, 0($sp)")
                    code.append(f"\tadd $sp, $sp, 4")
                    self.regs._sp += 4
                # print("MYLOG: ", funcname, self.regs._sp)

                pass
            elif self.tac_code[i].startswith('new'):
                ## TODO 
                items = self.tac_code[i].split(' ')
                code.append(f"\taddi $sp, $sp, -12")
                space = int(items[2])
                code.extend(self.malloc(space))
                code.append(f'\tsw $v0, 0($sp)')
                code.append(f'\tsw {space}, 4($sp)')
                code.append(f'\tsw {space}, 8($sp)')
                code.append(f'\tadd $sp, $sp, -12')
            elif self.tac_code[i].startswith('params'):
                items = self.tac_code[i].split(' ')
                if len(items) == 3 and items[1] == '*':
                    items[1] = f"{items[2]}#point"
                    new_reg, _code = self.regs.get_register(items[1])
                    code.extend(_code)
                    param_reg, _code = self.regs.get_register(items[2])
                    code.extend(_code)
                    code.append(f"\tlw {new_reg}, 0({param_reg})")

                code.extend(self.handle_param(items[1], isFloat=items[0].endswith('float')))
                
            elif self.tac_code[i].startswith('retparams'):
                pass ## Done inside addFunction
            elif self.tac_code[i].startswith('retval'):
                retval_items = self.tac_code[i].split(' ')
                reg, mips = self.handle_returns(retval_items[0], isFloat=retval_items[0].endswith('float'))
                code.extend(mips)
                return code
            elif self.tac_code[i].startswith('if'):
                cond = items[2]
                elselab = items[5]
                code.extend(self.handle_ifStmt(cond, elselab))
            elif self.tac_code[i].startswith('goto'):
                code.extend(self.handle_goto(self.tac_code[i].split(' ')[1]))
            elif self.tac_code[i].endswith(':'):  # label
                code.extend(self.handle_label(self.tac_code[i][:-1]))
            elif self.tac_code[i].startswith('arg'):
                ## TODO : Handle composite literal
                items = self.tac_code[i].split(' ')
                code.extend(self.handle_args(items)) 
                pass
            elif len(self.tac_code[i]) > 0 and self.tac_code[i][0].isnumeric():
                items = self.tac_code[i].split(' ')
                code.extend(self.handle_localvars(items))  
                pass
            elif self.tac_code[i].startswith('return'):
                code.append(f'\tj _return_{self.curr_func}')
        return code

    def _get_label(self, label, isFloat = False):
        code = []
        if label.startswith("temp") or (label[0].isdigit() and ('_' in label)):
            _type, offset, type_loc =self._location(label, isFloat = isFloat)
            if type_loc == 1:
                reg, mips = self.regs.get_register(isFloat=isFloat)
                code.extend(mips)
                if isFloat:
                    code.append(f'\tlwc1 {reg}, {_type}')
                else:
                    code.append(f'\tlw {reg}, {_type}')
                return reg, code
            else:
                return _type, offset
        elif label.startswith("arg"):
            stm_entry = self.stm.get(self.curr_func)
            offset = -int(label.split('_')[-1].split('.')[0][:-1])
            j = 0
            curr_offset = 0
            for param in stm_entry['params']:
                curr_offset += param['size']
                if curr_offset == offset:
                    break  
                j += 1 
            if j <= 4:
                return f"$a{j-1}", []
            reg, mips = self.regs.get_register(isFloat = isFloat)
            code.extend(mips)
            if len(label.split('_')[-1].split('.')) > 1: 
                if label.split('_')[-1].split('.')[1] == 'length':
                    offset += 4 
                else:
                    offset += 8
            code.append(f'\tlw {reg}, {offset}($fp)')
            return reg, code
        elif label.startswith("vartemp"):
            loc, _mips, type_loc = self._location(label.split('.')[0])
            code.extend(_mips)
            reg = None
            if label.endswith('.addr'):
                reg, mips = self.regs.get_register(isFloat = isFloat)
                code.extend(mips)
                if type_loc == 1:
                    code.append(f'\tlw {reg}, {loc}')
                else:
                    code.append('\tadd {reg}, {loc}, $0')
            elif label.endswith('.length'):
                reg, mips = self.regs.get_register(isFloat = isFloat)
                code.extend(mips)
                code.append(f'\tlw {reg}, {offset + 4}')
            elif label.endswith('.capacity'):
                reg, mips = self.regs.get_register(isFloat = isFloat)
                code.extend(mips)
                code.append(f'\tlw {reg}, {offset + 8}')
            # else:
            #     reg1, mips = self.regs.get_register(isFloat = isFloat)
            #     code.extend(mips)
            #     code.append(f'\tlw {reg}, {offset}')
            #     reg2, mips = self.regs.get_register(isFloat = isFloat)
            #     code.extend(mips)
            #     code.append(f'\tlw {reg2}, {offset + 4}')
            #     reg3, mips = self.regs.get_register(isFloat = isFloat)
            #     code.extend(mips)
            #     code.append(f'\tlw {reg3}, {offset + 8}')
            #     return [reg1, reg2, reg3], code
        elif label.startswith('retval'):
            return self.handle_returns(label, isFloat=isFloat)
        else:
            reg, mips = self.regs.get_register(isFloat=isFloat)
            code.extend(mips)
            if isFloat:
                code.append(f'\tli.s {reg}, {label}')
            else:
                code.append(f'\tli {reg}, {label}')

        return reg, code

    def handle_newvartemp(self, items):
        code = []
        var_temp = items[1]
        var_temp_sz = int(items[2])
        code.extend(self.malloc(var_temp_sz))
        pass

    def handle_varTempPointers(self):
        ## TODO
        pass

    def handle_localvars(self, items):
        code = []

        if items[0] not in self.regs.locations:
            self.regs._sp -= 4
            code.append("\tadd $sp, $sp, -4")
            self.regs.locations[items[0]] = [1, -self.regs._sp]

        if len(items) == 3:
            # a = b
            isFloat = False
            if 'float' in items[1]:
                isFloat = True
            if items[2].startswith('temp'):
                loc, _mips, type_loc = self._location(items[0], isFloat=isFloat)
                code.extend(_mips)
                find_new_reg, mips, type_new_reg = self._location(items[2], isFloat=isFloat)
                code.extend(mips)
                var = ''
                if isFloat:
                    var = 'c1'
                if type_loc == 1:
                    code.append(f'\tsw{var} {find_new_reg}, {loc}')
                else:
                    if isFloat:
                        code.append(f'\tmov.s {loc}, {find_new_reg}')
                    else:
                        code.append(f'\tadd {loc}, {find_new_reg}, $0')
            elif items[2].startswith('args'):
                loc, _mips, type_loc = self._location(items[0], isFloat=isFloat)
                code.extend(_mips)
                offset2 = -int(items[2].split('_')[-1].split('.')[0][:-1])
                if len(items[2].split('_')[-1].split('.')) > 1: 
                    if items[2].split('_')[-1].split('.')[1] == 'length':
                        offset2 += 4 
                    else:
                        offset2 += 8
                helper_reg, mips = self.regs.get_register(isFloat=isFloat)
                code.extend(mips)  
                var = ''
                if isFloat:
                    var = 'c1'
                code.append(f'\tlw{var} {helper_reg}, {offset2}($fp)')
                if type_loc == 1:
                    code.append(f'\tsw{var} {helper_reg}, {loc}')
                else:
                    if isFloat:
                        code.append(f'\tmov.s {loc}, {helper_reg}')
                    else:
                        code.append(f'\tadd {loc}, {helper_reg}, $0')

            elif items[2].startswith('var_temp'):
                retReg, mips = self._get_label(items[2], isFloat=isFloat)
                code.extend(mips)
                retReg = retReg[0] ## Both point to same location
                loc, _mips, type_loc = self._location(items[0], isFloat=isFloat)[1]
                code.extend(_mips)
                var = ''
                if isFloat:
                    var = 'c1'
                if type_loc == 1:  
                    code.append(f'\tsw{var} {retReg}, {loc}')
                else:
                    if isFloat:
                        code.append(f'\tmov.s {loc}, {retReg}')
                    else:
                        code.append(f'\tadd {loc}, {retReg}, $0')
            elif items[2].startswith('retval'):
                funcName = '_'.join(items[2].split('_')[1:-1])
                if self.curr_pkg != None and funcName in self.stm.pkgs[self.curr_pkg].functions:
                    new_stm = self.stm.pkgs[self.curr_pkg]
                else:
                    new_stm = self.stm
                num_returns = len(
                    new_stm.functions[funcName]['return'])
                if num_returns == 1:
                    reg, mips = self.regs.get_register(items[0], isFloat=isFloat)
                    code.extend(mips)
                    if isFloat:
                        code.append(f'\t mov.s {reg}, $f0')
                    else:
                        code.append(f'\taddi {reg}, $v0, 0')
                else:
                    ret_reg, mips = self.handle_returns(items[2], isFloat=isFloat)
                    code.extend(mips)
                    loc, _mips, type_loc = self._location(items[0], isFloat=isFloat)
                    var = ''
                    if isFloat:
                        var = 'c1'
                    if type_loc == 1:
                        code.append(f'\tlw{var} {ret_reg}, {loc}')
                    else:
                        if isFloat:
                            code.append(f'\tmov.s {loc}, {ret_reg}')
                        else:
                            code.append(f'\tadd {loc}, {ret_reg}, $0')

            elif items[2].startswith('__syscall'):
                raise Exception("Bypassed. Shouldn't be called")
                loc, _mips, type_loc = self._location(items[0])
                code.extend(_mips)
                if type_loc == 1:
                    # if isFloat:
                        # code.append(f'\tswc1 $v0, {loc}')
                    code.append(f'\tsw $v0, {loc}')
                else:
                    code.append(f'\tadd {loc}, $v0, $0')
            else:
                if items[2][0] == '"':
                    # string: TODO
                    pass
                elif self.isInt(items[2]):
                    # integer
                    loc, _mips, type_loc = self._location(items[0], isFloat=isFloat)
                    code.extend(_mips)
                    helper_reg, mips = self.regs.get_register(isFloat=isFloat)
                    code.extend(mips) 
                    if isFloat:
                        code.append(f'\tli.s {helper_reg}, {float(items[2])}')
                    else:
                        code.append(f'\tli {helper_reg}, {items[2]}')
                    var = '' if not isFloat else 'c1'
                    if type_loc == 1:
                        code.append(f'\tsw{var} {helper_reg}, {loc}')
                    else:
                        if isFloat:
                            code.append(f'\tmov.s {loc}, {helper_reg}')
                        else:
                            code.append(f'\tadd {loc}, {helper_reg}, $0')
                    pass
                elif self.isFloat(items[2]):
                    # float
                    loc, _mips, type_loc = self._location(items[0], isFloat=isFloat)
                    code.extend(_mips)
                    helper_reg, mips = self.regs.get_register(items[0], isFloat = True)
                    code.extend(mips)
                    code.append(f'\tli.s {helper_reg}, {items[2]}')
                    if type_loc == 1:
                        code.append(f'\tswc1 {helper_reg}, {loc}')
                    else:
                        code.append(f'\tmov.s {loc}, {helper_reg}')
                    pass                        
                elif items[2][0] == "'":
                    # rune
                    loc, _mips, type_loc = self._location(items[0])
                    code.extend(_mips)
                    helper_reg, mips = self.regs.get_register(items[0])
                    code.extend(mips)
                    code.append(f'\tli {helper_reg}, {items[2]}')
                    if type_loc == 1:
                        code.append(f'\tsw {helper_reg}, {loc}')
                    else:
                        code.append(f'\tadd {loc}, {helper_reg}, $0')                    
                    pass
                else:
                    raise NotImplementedError
        elif len(items) == 4:
            isFloat = False
            if 'float' in items[1]:
                isFloat = True
            # a = unop b
            loc, _mips, type_loc = self._location(items[0], isFloat=isFloat)
            code.extend(_mips)
            reg, mips = self.regs.get_register(isFloat=isFloat)
            code.extend(mips)
            code.extend(self.handle_unOp(items[2], items[3], reg))
            if type_loc == 1:
                if isFloat:
                    code.append(f'\tswc1 {reg} {loc}')
                else:
                    code.append(f'\tsw {reg}, {loc}')
            else:
                if isFloat:
                    code.append(f'\tmov.s {loc}, {reg}')
                else:
                    code.append(f'\tadd {loc}, {reg}, $0')

        elif len(items) == 5:
            # a = b binop c
            # a = & * b
            isFloat = False
            if 'float' in items[1]:
                isFloat = True
            if items[2] == '&' and items[3] == '*': 
                if isFloat:
                    raise Exception("Can store address in FPR")
                loc, _mips, type_loc = self._location(items[0])
                code.extend(_mips)
                old_reg, mips = self.regs.get_register(items[2])
                code.extend(mips)

                if type_loc == 1:
                    code.append(f'\tsw {old_reg}, {loc}')
                else:
                    code.append(f'\tadd {loc}, {old_reg}, $0')
            else:
                reg, mips = self.regs.get_register(isFloat=isFloat)
                code.extend(mips)
                code.extend(self.handle_binOp(items[2], items[4], items[3], reg))
                reg2, mips2 = self.regs.get_register(isFloat=isFloat)
                code.extend(mips2)
                if isFloat:
                    code.append(f'\tmov.s {reg2}, {reg}')
                else:
                    code.append(f'\tadd {reg2}, {reg}, $0')
                loc, _mips, type_loc = self._location(items[0], isFloat=isFloat)
                code.extend(_mips)
                if type_loc == 1:
                    if isFloat:
                        code.append(f'\tswc1 {reg2}, {loc}')
                    else:
                        code.append(f'\tsw {reg2}, {loc}')
                else:
                    if isFloat:
                        code.append(f'\tmov.s {loc}, {reg2}')
                    else:
                        code.append(f'\tadd {loc}, {reg2}, $0')
        elif len(items) == 6:
            # a = * b binop c
            # a = b binop * c
            isFloat = False
            if 'float' in items[1]:
                isFloat = True
            if items[2] == '*': 
                loc, _mips, type_loc = self._location(items[0], isFloat=isFloat)
                code.extend(_mips)
                reg, mips = self.regs.get_register(isFloat=isFloat)
                code.extend(mips)
                new_reg, mips = self.regs.get_register(isFloat=isFloat)
                code.extend(mips)
                code.extend(self.handle_unOp(items[2], items[3], new_reg))
                binop_reg, mips = self.regs.get_register(isFloat=isFloat)
                code.extend(mips)
                code.extend(self.handle_binOp(new_reg, items[4], binop_reg, isreg1 = True))
                if isFloat:
                    code.append(f'\tmov.s {reg}, {binop_reg}')
                else:
                    code.append(f"\tadd {reg}, {binop_reg}, $0")
                
                if type_loc == 1:
                    if isFloat:
                        code.append(f'\tswc1 {reg}, {loc}')
                    else:
                        code.append(f'\tsw {reg}, {loc}')
                else:
                    if isFloat:
                        code.append(f'\tmov.s {loc}, {reg}')
                    else:
                        code.append(f'\tadd {loc}, {reg}, $0')
            elif items[4] == '*':
                loc, _mips, type_loc = self._location(items[0], isFloat=isFloat)
                code.extend(_mips)
                reg, mips = self.regs.get_register(isFloat=isFloat)
                code.extend(mips)
                new_reg, mips = self.regs.get_register(isFloat=isFloat)
                code.extend(mips)
                code.extend(self.handle_unOp(items[4], items[5], new_reg))
                binop_reg, mips = self.regs.get_register(isFloat=isFloat)
                code.extend(mips)
                code.extend(self.handle_binOp(items[2], new_reg, binop_reg, isreg2 = True))
                code.append(f"\tadd {reg}, {binop_reg}, $0")

                if isFloat:
                    code.append(f'\tmov.s {reg}, {binop_reg}')
                else:
                    code.append(f"\tadd {reg}, {binop_reg}, $0")
                
                if type_loc == 1:
                    if isFloat:
                        code.append(f'\tswc1 {reg}, {loc}')
                    else:
                        code.append(f'\tsw {reg}, {loc}')
                else:
                    if isFloat:
                        code.append(f'\tmov.s {loc}, {reg}')
                    else:
                        code.append(f'\tadd {loc}, {reg}, $0')
        else:
            raise NotImplementedError

        return code

    def isNumeric(self, x):
        return self.isInt(x) | self.isFloat(x)

    def isInt(self, x):
        try:
            y = int(x)
        except Exception as e:
            return False
        return True
    
    def isFloat(self, x):
        try:
            y = float(x)
        except Exception as e:
            return False
        return True

    def handle_temp(self, items):
        code = []
        if len(items) == 3:
            # a = b
            isFloat = False
            if 'float' in items[1]:
                isFloat = True
            if items[2].startswith('temp'):
                old_reg, mips = self.regs.get_register(items[2], isFloat=isFloat)
                code.extend(mips)
                find_new_reg, mips = self.regs.get_register(items[0], isFloat=isFloat)
                code.extend(mips)
                if isFloat:
                    code.append(f'\tmov.s {find_new_reg}, {old_reg}')
                else:
                    code.append(f'\tadd {find_new_reg}, {old_reg}, $0')
                return find_new_reg, code
            elif items[2].startswith('args'):
                find_new_reg, mips = self.regs.get_register(items[0], isFloat=isFloat)
                code.extend(mips)
                offset = -int(items[2].split('_')[-1].split('.')[0][:-1])
                if len(items[2].split('_')[-1].split('.')) > 1: 
                    if items[2].split('_')[-1].split('.')[1] == 'length':
                        offset += 4 
                    else:
                        offset += 8
                var = ''
                if isFloat:
                    var = 'c1'
                code.append(f'\tlw{var} {find_new_reg}, {offset}($fp)')
                return find_new_reg, code
            elif items[2].startswith('var_temp'):
                retReg, mips = self._get_label(items[2], isFloat=isFloat)
                code.extend(mips)
                retReg = retReg[0] ## Both point to same location
                find_new_reg, mips = self.regs.get_register(items[0], isFloat=isFloat)
                code.extend(mips)
                if isFloat:
                    code.append(f'\tmov.s {find_new_reg}, {retReg}')
                else:
                    code.append(f'\tadd {find_new_reg}, {retReg}, $0')
                return find_new_reg, code

            elif items[2].startswith('retval'):
                funcName = '_'.join(items[2].split('_')[1:-1])
                print(funcName)
                if self.curr_pkg != None and funcName in self.stm.pkgs[self.curr_pkg].functions:
                    new_stm = self.stm.pkgs[self.curr_pkg]
                else:
                    new_stm = self.stm
                num_returns = len(new_stm.functions[funcName]['return'])
                if num_returns == 1:
                    code.append(f"\t### STACK1: {self.regs._sp}, {items[0]}")
                    code.append(f"\t### {items[0] in self.regs.locations}")
                    reg, mips = self.regs.get_register(items[0], isFloat=isFloat)
                    code.extend(mips)
                    code.append(f"\t### STACK2: {self.regs._sp}")
                    if isFloat:
                        code.append(f'\tmov.s {reg}, $f0')
                    else:
                        code.append(f'\taddi {reg}, $v0, 0')
                    return reg, code
                else:
                    ret_reg, mips = self.handle_returns(items[2], isFloat=isFloat)
                    code.extend(mips)
                    reg, mips = self.regs.get_register(items[0], isFloat=isFloat)
                    code.extend(mips)
                    if isFloat:
                        code.append(f'\tmov.s {reg}, {ret_reg}')
                    else:
                        code.append(f'\taddi {reg}, {ret_reg}, 0')
                    return reg, code
            else:
                if items[2][0] == '"':
                    # string: TODO
                    pass
                elif self.isInt(items[2]):
                    # integer
                    reg, mips = self.regs.get_register(items[0], isFloat=isFloat)
                    code.extend(mips)
                    if isFloat:
                        code.append(f'\tli.s {reg}, {float(items[2])}')
                    else:
                        code.append(f'\tli {reg}, {items[2]}')
                    return reg, code
                elif self.isFloat(items[2]):
                    # float
                    reg, mips = self.regs.get_register(items[0], isFloat = True)
                    code.extend(mips)
                    code.append(f'\tli.s {reg}, {items[2]}')
                    return reg, code
                elif items[2][0] == "'":
                    # rune
                    if isFloat:
                        raise Exception("Rune can't be typecast into float.")
                    reg, mips = self.regs.get_register(items[0])
                    code.extend(mips)
                    code.append(f'\tli {reg}, {items[2]}')
                    return reg, code
                else:
                    raise NotImplementedError
        elif len(items) == 4:
            # a = unop b
            reg, mips = self.regs.get_register(items[0], isFloat=('float' in items[1]))
            code.extend(mips)
            # Float case handled from items[2]
            code.extend(self.handle_unOp(items[2], items[3], reg))
            return reg, code
        elif len(items) == 5:
            # a = b binop c
            # a = & * b
            isFloat = False
            if 'float' in items[1]:
                isFloat = True
            if items[2] == '&' and items[3] == '*':
                if isFloat:
                    raise Exception("Pointer can't be stored in FPR") 
                old_reg, mips = self.regs.get_register(items[2])
                code.extend(mips)
                find_new_reg, mips = self.regs.get_register(items[0])
                code.extend(mips)
                code.append(f'\tadd {find_new_reg}, {old_reg}, $0')
                return find_new_reg, code
            else:
                reg, mips = self.regs.get_register(isFloat=isFloat)
                code.extend(mips)
                code.extend(self.handle_binOp(items[2], items[4], items[3], reg))
                reg2, mips2 = self.regs.get_register(items[0], isFloat=isFloat)
                code.extend(mips2)
                if isFloat:
                    code.append(f'\tmov.s {reg2}, {reg}')
                else:
                    code.append(f'\tadd {reg2}, {reg}, $0')
                return reg2, code
        elif len(items) == 6:
            # a = * b binop c
            # a = b binop * c
            isFloat = False
            if 'float' in items[1]:
                isFloat = True
            if items[2] == '*': 
                reg, mips = self.regs.get_register(items[0], isFloat=isFloat)
                code.extend(mips)
                new_reg, mips = self.regs.get_register(isFloat=isFloat)
                code.extend(mips)
                code.extend(self.handle_unOp(items[2], items[3], new_reg))
                binop_reg, mips = self.regs.get_register(isFloat=isFloat)
                code.extend(mips)
                code.extend(self.handle_binOp(new_reg, items[4], binop_reg, isreg1 = True))
                if isFloat:
                    code.append(f'\tmov.s {reg}, {binop_reg}')
                else:
                    code.append(f"\tadd {reg}, {binop_reg}, $0")
                return reg, code
            elif items[4] == '*':
                reg, mips = self.regs.get_register(items[0], isFloat=isFloat)
                code.extend(mips)
                new_reg, mips = self.regs.get_register(isFloat=isFloat)
                code.extend(mips)
                code.extend(self.handle_unOp(items[4], items[5], new_reg))
                binop_reg, mips = self.regs.get_register(isFloat=isFloat)
                code.extend(mips)
                code.extend(self.handle_binOp(items[2], new_reg, items[4], binop_reg, isreg2 = True))
                if isFloat:
                    code.append(f'\tmov.s {reg}, {binop_reg}')
                else:
                    code.append(f"\tadd {reg}, {binop_reg}, $0")
                return reg, code
        else:
            raise NotImplementedError

    def get_args(self, label):
        stm_entry = self.stm.get(self.curr_func)
        offset = -int(label.split('_')[-1].split('.')[0][:-1])
        j = 0
        curr_offset = 0
        for param in stm_entry['params']:
            curr_offset += param['size']
            if curr_offset == offset:
                break  
            j += 1 
        if j <= 4:
            return 0, f"$a{j-1}"
        else:
            offset = int(label.split('_')[-1].split('.')[0][:-1])

            if len(label.split('_')[-1].split('.')) > 1:
                if label.split('_')[-1].split('.')[1] == 'length':
                    offset += 4 
                else:
                    offset += 8
            return 1, -offset-16

    def handle_args(self, items): 
        code = []
        isFloat = False
        var = ''
        if 'float' in items[1]:
            isFloat = True
            var = 'c1'
        if len(items) == 3:
            # a = b
            if items[2].startswith('temp'):
                _type, offset = self.get_args(items[0])
                find_new_reg, mips = self._get_label(items[2], isFloat=isFloat)
                code.extend(mips)
                if _type == 0:
                    code.append(f'\tadd {offset}, {find_new_reg}, $0')
                    return code
                code.append(f'\tsw {find_new_reg}, {offset}($fp)')
            elif items[2].startswith('args'):
                _type1, offset1 = self.get_args(items[0])
                _type2, offset2 = self.get_args(items[2])
                helper_reg, mips = self.regs.get_register(isFloat=isFloat)
                code.extend(mips)  
                
                if _type1 == 1:
                    code.append(f'\tlw{var} {helper_reg}, {offset2}($fp)')
                else:
                    code.append(f'\tlw{var} {offset1}, {helper_reg}, $0')
                if _type2 == 1:
                    code.append(f'\tsw{var} {helper_reg}, {offset1}($fp)')
                else:
                    code.append(f'\tlw{var} {offset2}, {helper_reg}, $0')
 
            elif items[2].startswith('var_temp'):
                retReg, mips = self._get_label(items[2], isFloat=isFloat)
                code.extend(mips)
                retReg = retReg[0] ## Both point to same location
                _type, offset = self.get_args(items[0]) 
                if _type == 1:

                    code.append(f'\tsw{var} {retReg}, {offset}($fp)')
                else:
                    if isFloat:
                        code.append(f'\tmov.s {offset}, {retReg}')
                    else:
                        code.append(f'\tadd {offset}, {retReg}, $0')

            elif items[2].startswith('retval'):
                funcName = '_'.join(items[2].split('_')[1:-1])
                if self.curr_pkg != None and funcName in self.stm.pkgs[self.curr_pkg].functions:
                    new_stm = self.stm.pkgs[self.curr_pkg]
                else:
                    new_stm = self.stm
                num_returns = len(
                    new_stm.functions[funcName]['return'])
                if num_returns == 1:
                    reg, mips = self._get_label(items[0], isFloat=isFloat)
                    code.extend(mips)
                    if isFloat:
                        code.append(f'\tmov.s {reg}, $f0')
                    else:
                        code.append(f'\taddi {reg}, $v0, 0')
                else:
                    ret_reg, mips = self.handle_returns(items[2], isFloat=isFloat)
                    code.extend(mips)
                    _type, offset = self.get_args(items[0])
                    if _type == 1:
                        code.append(f'\tlw{var} {ret_reg}, {offset}($fp)')
                    else:
                        if isFloat:
                            code.append(f'\tmov.s {offset}, {ret_reg}')
                        else:
                            code.append(f'\tadd {offset}, {ret_reg}, $0')
            else:
                if items[2][0] == '"':
                    # string: TODO
                    pass
                elif self.isInt(items[2]):
                    # integer
                    _type, offset = self.get_args(items[0])
                    helper_reg, mips = self.regs.get_register(isFloat=isFloat)
                    code.extend(mips) 
                    if isFloat:
                        code.append(f'\tli.s {helper_reg}, {float(items[2])}')
                    else:
                        code.append(f'\tli {helper_reg}, {items[2]}')

                    if _type == 1:
                        code.append(f'\tsw{var} {helper_reg}, {offset}($fp)')
                    else:
                        if isFloat:
                            code.append(f'\tmov.s {offset}, {helper_reg}')
                        else:
                            code.append(f'\tadd {offset}, {helper_reg}, $0')
                    pass
                elif self.isFloat(items[2]):
                    # float
                    _type, offset = self.get_args(items[0])
                    helper_reg, mips = self._get_label(items[0], isFloat = True)
                    code.extend(mips)
                    code.append(f'\tli.s {helper_reg}, {items[2]}')
                    if _type == 1:
                        code.append(f'\tswc1 {helper_reg}, {offset}($fp)')
                    else:
                        if isFloat:
                            code.append(f'\tmov.s {offset}, {helper_reg}')
                        else:
                            code.append(f'\tadd {offset}, {helper_reg}, $0')
                        pass
                elif items[2][0] == "'":
                    # rune
                    _type, offset = self.get_args(items[0])
                    helper_reg, mips = self._get_label(items[0])
                    code.extend(mips)
                    code.append(f'\tli {helper_reg}, {items[2]}')
                    if _type == 1:
                        code.append(f'\tsw {helper_reg}, {offset}($fp)')
                    else:
                        code.append(f'\tadd {offset}, {helper_reg}, $0')                    
                        pass
                else:
                    raise NotImplementedError
        elif len(items) == 4:
            # a = unop b
            _type, offset = self.get_args(items[0])
            reg, mips = self.regs.get_register(isFloat=isFloat)
            code.extend(mips)
            code.extend(self.handle_unOp(items[2], items[3], reg))
            if _type == 1:
                code.append(f'\tsw{var} {reg}, {offset}($fp)')
            else:
                if isFloat:
                    code.append(f'\tmov.s {offset}, {reg}')
                else:
                    code.append(f'\tadd {offset}, {reg}, $0')
        elif len(items) == 5:
            # a = b binop c
            # a = & * b
            if items[2] == '&' and items[3] == '*': 
                _type, offset = self.get_args(items[0])
                old_reg, mips = self.regs.get_register(items[2], isFloat=isFloat)
                code.extend(mips)
                if _type == 1:
                    code.append(f'\tsw{var} {old_reg}, {offset}($fp)')
                else:
                    if isFloat:
                        code.append(f'\tmov.s {offset}, {old_reg}')
                    else:
                        code.append(f'\tadd {offset}, {old_reg}, $0')
            else:
                _type, offset = self.get_args(items[0])
                reg, mips = self.regs.get_register(isFloat=isFloat)
                code.extend(mips)
                code.extend(self.handle_binOp(items[2], items[4], items[3], reg))
                reg2, mips2 = self.regs.get_register(isFloat=isFloat)
                code.extend(mips2)
                if isFloat:
                    code.append(f'\tmov.s {reg2}, {reg}')
                else:
                    code.append(f'\tadd {reg2}, {reg}, $0')
                if _type == 1:
                    code.append(f'\tsw{var} {reg2}, {offset}($fp)')
                else:
                    if isFloat:
                        code.append(f'\tmov.s {offset}, {reg2}')
                    else:
                        code.append(f'\tadd {offset}, {reg2}, $0')
        elif len(items) == 6:
            # a = * b binop c
            # a = b binop * c
            if items[2] == '*': 
                _type, offset = self.get_args(items[0])
                reg, mips = self.regs.get_register(isFloat=isFloat)
                code.extend(mips)
                new_reg, mips = self.regs.get_register(isFloat=isFloat)
                code.extend(mips)
                code.extend(self.handle_unOp(items[2], items[3], new_reg))
                binop_reg, mips = self.regs.get_register(isFloat=isFloat)
                code.extend(mips)
                code.extend(self.handle_binOp(new_reg, items[4], binop_reg, isreg1 = True))
                if isFloat:
                    code.append(f'\tmov.s {reg}, {binop_reg}')
                else:
                    code.append(f'\tadd {reg}, {binop_reg}, $0')
                if _type == 1:
                    code.append(f'\tsw{var} {binop_reg}, {offset}($fp)')
                else:
                    if isFloat:
                        code.append(f'\tmov.s {offset}, {binop_reg}')
                    else:
                        code.append(f'\tadd {offset}, {binop_reg}, $0')
        elif items[4] == '*':
                _type, offset = self.get_args(items[0])  
                reg, mips = self.regs.get_register(isFloat=isFloat)
                code.extend(mips)
                new_reg, mips = self.regs.get_register(isFloat=isFloat)
                code.extend(mips)
                code.extend(self.handle_unOp(items[4], items[5], new_reg))
                binop_reg, mips = self.regs.get_register(isFloat=isFloat)
                code.extend(mips)
                code.extend(self.handle_binOp(items[2], new_reg, binop_reg, isreg2 = True))
                if isFloat:
                    code.append(f'\tmov.s {reg}, {binop_reg}')
                else:
                    code.append(f'\tadd {reg}, {binop_reg}, $0')
                if _type == 1:
                    code.append(f'\tsw{var} {reg}, {offset}($fp)')
                else:
                    if isFloat:
                        code.append(f'\tmov.s {offset}, {reg}')
                    else:
                        code.append(f'\tadd {offset}, {reg}, $0')
        else:
            raise NotImplementedError

        return code

    def handle_floatparam(self, param, isFloat=False):
        code = []
        # If the parameter is a float
        for i in range(12, 20):
            # Floating point registers can take $f12 ... $f19 as such
            if self.regs.args_regsF [f"$f{i}"][0] == None:
                # No need to save registers; we should be saving in handle call?
                # Assuming saving happens there correctly
                found = 1
                if param.startswith('temp'):
                    # Floating point value in temp
                    self.regs.args_regsF[f'$f{i}'][0] = param
                    self.regs.args_regsF[f'$f{i}'][1] = self.regs.count
                    self.regs.count += 1
                    offset = self.regs.locations[param]
                    if offset[0] == 1:
                        # Value in memory(spilled before?)
                        code.append(f'\tlwc1 $f{i}, {offset[1] - self.act_records[self.curr_func].localvar_space}($fp)')
                    else:
                        # Value in some register
                        code.append(f'\tmov.s $f{i}, {offset[1]}')
                    break
                elif param.startswith('arg'):
                    # Floating point value in the current stack
                    self.regs.args_regsF[f'$f{i}'][0] = param
                    self.regs.args_regsF[f'$f{i}'][1] = self.regs.count
                    self.regs.count += 1
                    # Hoping that _get_label does its job
                    regs, mips = self._get_label(param, isFloat=isFloat)
                    code.extend(mips)
                    code.append(f'\tmov.s $f{i}, {regs}')
                    break
                elif param[0].isnumeric() and '_' in param:
                    # Floating point value is a scope variable
                    self.regs.args_regsF[f'$f{i}'][0] = param
                    self.regs.args_regsF[f'$f{i}'][1] = self.regs.count
                    self.regs.count += 1
                    regs, mips = self._get_label(param, isFloat=isFloat)
                    code.extend(mips)
                    code.append(f'\tmov.s $f{i}, {regs}')
                    break
                elif param.startswith('var_temp'):
                    raise Exception('None of var temp attributes are to be stored on floating point register')
                else:
                    raise NotImplementedError(param)

        if not found:
            # Store on stack
            if not param.startswith('var_temp'):
                # not a var_temp
                reg, mips = self.regs.get_register(param, isFloat=isFloat)
                code.extend(mips)
                code.append(f'\taddi $sp, $sp, -4')
                code.append(f'\tswc1 {reg} 0($sp)') # Storing float point register value on stack
            else:
                raise Exception('None of var temp attributes are to be stored on floating point register')
            pass
        return code
    
    def handle_param(self, param: str, isFloat=False):
        """
        This function puts the function call 
        parameters on stack and argument registers
        before jal is executed.
        """
        # TODO : Handle vartemp and sizes
        print("M: ", param, isFloat)
        code = []
        if isFloat:
            code.extend(self.handle_floatparam(param, isFloat=isFloat))
        else:   
            # If the parameter is not a float; say int or vartemp(maybe implemented later)
            found = 0            
            
            for i in range(4):
                if self.regs.arg_regs[f'$a{i}'][0] == None:
                    if i == 0:
                        # Shouldn't call handle the register saving part?
                        code.append("\t#### Saving temporary registers")
                        for reg in self.regs.regs:
                            code.append(f"\tadd $sp, $sp, -4")
                            code.append(f"\tsw {reg}, 0($sp)")
                            self.regs._sp -= 4 
                        code.append("\t#### Done saving temporary registers")
                        code.append("\t#### Saving argument registers")
                        for reg in self.regs.arg_regs:
                            code.append(f"\tadd $sp, $sp, -4")
                            code.append(f"\tsw {reg}, 0($sp)")
                            self.regs._sp -= 4
                        code.append("\t#### Done saving argument registers")
                        # print("MYLOG: ", self.curr_func, self.regs._sp)
                    found = 1 
                    code.append(f"\t#### YAYYY {param}")
                    if param.startswith('temp'):
                        self.regs.arg_regs[f'$a{i}'][0] = param
                        self.regs.arg_regs[f'$a{i}'][1] = self.regs.count
                        self.regs.count += 1
                        offset = self.regs.locations[param]
                        code.append(f"\t### offset: {offset}, {param}")
                        if offset[0] == 1:
                            code.append(f"\tlw $a{i}, {offset[1] - self.act_records[self.curr_func].localvar_space}($fp)")
                        else:
                            code.append(f"\tadd $a{i}, {offset[1]}, $0")
                        code.append(f"\t### STACK: {self.regs._sp}")
                        break
                    elif param.startswith('arg'):
                        self.regs.arg_regs[f'$a{i}'][0] = param
                        self.regs.arg_regs[f'$a{i}'][1] = self.regs.count
                        self.regs.count += 1
                        regs, mips = self._get_label(param)
                        code.extend(mips)
                        code.append(f"\tadd $a{i}, {regs}, $0")
                        break
                    elif param[0].isnumeric() and '_' in param:
                        self.regs.arg_regs[f'$a{i}'][0] = param
                        self.regs.arg_regs[f'$a{i}'][1] = self.regs.count
                        self.regs.count += 1
                        regs, mips = self._get_label(param)
                        code.extend(mips)
                        code.append(f"\tadd $a{i}, {regs}, $0")
                        break
                    else:
                        loc, _mips, type_loc = self._location(param.split('.')[0])
                        code.extend(_mips)
                        if param.endswith('.addr'):
                            # params var_temp#x.addr
                            self.regs.arg_regs[f'$a{i}'][0] = param
                            self.regs.arg_regs[f'$a{i}'][1] = self.regs.count
                            self.regs.count += 1
                            if type_loc:
                                code.append(f'\tlw $a{i}, {loc}')
                            else:
                                code.append(f'\tadd $a{i}, {loc}, $0')
                        elif param.endswith('.length'):
                            # params var_temp#x.length
                            self.regs.arg_regs[f'$a{i}'][0] = param
                            self.regs.arg_regs[f'$a{i}'][1] = self.regs.count
                            self.regs.count += 1
                            code.append(f'\tlw $a{i}, {int(loc.split("(")[0]) + 4}($fp)')
                        elif param.endswith('.capacity'):
                            self.regs.arg_regs[f'$a{i}'][0] = param
                            self.regs.arg_regs[f'$a{i}'][1] = self.regs.count
                            self.regs.count += 1
                            code.append(f'\tlw $a{i}, {int(loc.split("(")[0]) + 8}($fp)')
                        else:
                            ## TODO
                            # which case is this? only var temp?
                            raise NotImplementedError(param)

            if not found:
                if not param.startswith('var_temp'):
                    reg, mips = self.regs.get_register(param)
                    code.extend(mips)
                    code.append(f'\taddi $sp, $sp, -4')
                    code.append(f'\tsw {reg} 0($sp)')
                else:
                    loc, _mips, type_loc = self._location(param.split('.')[0])
                    code.extend(mips)
                    if param.endswith('.addr'):
                        reg, mips = self.regs.get_register()
                        code.extend(mips)
                        if type_loc == 1:
                            code.append(f'\tlw {reg}, {loc}')
                        else:
                            code.append(f'\tadd {reg}, {loc}, $0')
                        code.append(f'addi $sp, $sp, -4')
                        code.append(f'\tsw {reg} 0($sp)')
                    elif param.endswith('.length'):
                        reg, mips = self.regs.get_register()
                        code.extend(mips)
                        code.append(f'\tlw {reg}, {int(loc.split("(")[0]) + 4}($fp)')
                        code.append(f'addi $sp, $sp, -4')
                        code.append(f'\tsw {reg} 0($sp)')
                    elif param.endswith('.capacity'):
                        reg, mips = self.regs.get_register()
                        code.extend(mips)
                        code.append(f'\tlw {reg}, {int(loc.split("(")[0]) + 8}($fp)')
                        code.append(f'addi $sp, $sp, -4')
                        code.append(f'\tsw {reg} 0($sp)')
                    else:
                        reg, mips = self.regs.get_register()
                        code.extend(mips)
                        code.append(f'\tlw {reg}, {loc}')
                        code.append(f'addi $sp, $sp, -4')
                        code.append(f'\tsw {reg} 0($sp)')
                        code.append(f'\tlw {reg}, {int(loc.split("(")[0]) + 4}($fp)')
                        code.append(f'addi $sp, $sp, -4')
                        code.append(f'\tsw {reg} 0($sp)')
                        code.append(f'\tlw {reg}, {int(loc.split("(")[0]) + 8}($fp)')
                        code.append(f'addi $sp, $sp, -4')
                        code.append(f'\tsw {reg} 0($sp)')
        # print(param, code)
        return code

    def handle_returns(self, returnval, isFloat=False):
        """
        Handles return value from functions
        Stores the return value in registers that can be used later
        """
        funcName = '_'.join(returnval.split('_')[1:-1])
        num = int(returnval.split('_')[-1])

        code = []
        offset = 0
        if self.curr_pkg != None and funcName in self.stm.pkgs[self.curr_pkg].functions:
            new_stm = self.stm.pkgs[self.curr_pkg]
        else:
            new_stm = self.stm
        for idx, retVal in enumerate(new_stm.functions[funcName]['return']):
            if idx == num:
                break
            offset += retVal['size']

        reg, mips = self.regs.get_register(isFloat=isFloat) 
        # The stack can contain a floating point value to be put into a register
        code.extend(mips)
        if isFloat:
            code.append(f'\tlwc1 {reg} {offset}($v0)')
        else:
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
        reg3, mips = self.regs.get_register(isFloat=True)
        code.extend(mips)

        if operator.startswith('+'):
            code.append(f'\tadd.s {reg3}, {reg1}, {reg2}')
            if finalreg.startswith('$f'):
                code.append(f'\tmov.s {finalreg}, {reg3}')
            else:
                code.append(f'\tmfc1 {finalreg}, {reg3}')
        elif operator.startswith('-'):
            code.append(f'\tsub.s {reg3}, {reg1}, {reg2}')
            if finalreg.startswith('$f'):
                code.append(f'\tmov.s {finalreg}, {reg3}')
            else:
                code.append(f'\tmfc1 {finalreg}, {reg3}')
        elif operator.startswith('*'):
            code.append(f'\tmul.s {reg3}, {reg1}, {reg2}')
            if finalreg.startswith('$f'):
                code.append(f'\tmov.s {finalreg}, {reg3}')
            else:
                code.append(f'\tmfc1 {finalreg}, {reg3}')
        elif operator.startswith('/'):
            code.append(f'\tdiv.s {reg3}, {reg1}, {reg2}')
            if finalreg.startswith('$f'):
                code.append(f'\tmov.s {finalreg}, {reg3}')
            else:
                code.append(f'\tmfc1 {finalreg}, {reg3}')
        elif operator.startswith('<='):
            code.append(f'\tc.le.s {reg1}, {reg2}')
            code.append(f'\tcfc1 {finalreg}, $f31')
        elif operator.startswith('>='):
            code.append(f'\tc.lt.s {reg2}, {reg1}')
            code.append(f'\tcfc1 {finalreg},  $f31')
        elif operator.startswith('<'):
            code.append(f'\tc.lt.s {reg1}, {reg2}')
            code.append(f'\tcfc1 {finalreg},  $f31')
        elif operator.startswith('>'):
            code.append(f'\tc.le.s {reg2}, {reg1}')
            code.append(f'\tcfc1 {finalreg},  $f31')
        elif operator.startswith('=='):
            code.append(f'\tc.eq.s {reg1}, {reg2}')
            code.append(f'\tcfc1 {finalreg},  $f31')
        elif operator.startswith('!='):
            code.append(f'\tc.ne.s {reg1}, {reg2}')
            code.append(f'\tcfc1 {finalreg},  $f31')
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
            # Noice: Float handled
            return self.handle_floatBinOp(operand1, operand2, operator, finalreg, isreg1, isreg2)
        else:
            return self.handle_intBinOp(operand1, operand2, operator, finalreg, isreg1, isreg2)

    def handle_unOp(self, opr, operand, finalreg):
        code = []
        if opr == '+':
            return []

        elif opr[0] == '-':
            # Float case handled
            if 'float' in opr:
                isFloat = True 
            reg, mips = self._get_label(operand, isFloat = isFloat)
            code.extend(mips)
            code.append(f'\tsubi {finalreg}, 0, {reg}')
            return code

        elif opr[0] == '*':
            reg, mips = self._get_label(operand)
            code.extend(mips)

            code.append(f"\tlw {finalreg}, 0({reg})")
            return code

        elif opr[0] == '&':
            loc, _mips, type_loc = self._location(operand)
            code.extend(_mips)
            if type_loc == 1:
                offset = loc.split('$')[0][:-1]
                reg = loc.split('$')[1][:-1] 
                code.append(f'\taddi {finalreg}, ${reg}, {offset}')
            else:
                code.append(f'\tadd {finalreg}, {loc}, $0')
            return code

        elif opr[0] == '!':
            reg, mips = self._get_label(operand)
            code.extend(mips)
            code.append(f'\tnor {finalreg}, {reg}, $0')

        elif opr[0] == '^':
            reg, mips = self._get_label(operand)
            code.extend(mips)
            reg_helper, mips = self.regs.get_register()
            code.extend(mips)
            code.append(f'\tli {reg_helper} -1')
            code.append(f'\txor {finalreg}, {reg}, {reg_helper}')

        return code

    def handle_typecast(self):
        ## TODO
        # To convert int to float

        # To convert float to int

        # To convert int to string

        # To convert string to in
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
