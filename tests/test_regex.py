import os
import re
from inspect import isfunction

RED   = "\033[1;31m"  
GREEN = "\033[0;32m"
CYAN  = "\033[1;36m"
RESET = "\033[0;0m"

VERBOSE = False

path_to_testcases = "tests/Milestone2/regex"
regex = {}
test_dict = {
    'total' : 0,
    'passed' : 0
}

def get_regex():
    import src.Milestone2.lexer as lexer
    dict = lexer.__dict__
    for inst in dict:
        if isfunction(dict[inst]):
            if inst.startswith("t_") and not inst.endswith("error"):
                regex[inst[2:]] = dict[inst].__doc__
        elif isinstance(dict[inst],str):
            regex[inst[2:]] = dict[inst]

def get_data():
    if not os.path.exists(path_to_testcases):
        print("Invalid path to Regex Testcases: ", path_to_testcases)
        exit(0)

def validate(test_case, result, pattern, token, tc_id):
    """Validate a particular test case

    Parameters
    ----------
    test_case : str
        Describes the test case
    result : bool
        Expected Result
    pattern : 
        re pattern matching object
    token : str
        current token class
    tc_id : int
        test ID for the current token
    """
    test_dict['total'] += 1
    if (pattern.fullmatch(test_case) != None) == result:
        test_dict['passed'] += 1
        if VERBOSE:
            print(f"{tc_id}:\t{GREEN}Passed: {test_case}{RESET}")
    else:
        exp = ("Match" if result is True else "No Match")
        print(f"{tc_id}:\t{RED}Failed: {test_case} - Expected : {exp} for {token}{RESET}")

def check_testcases():
    current_token = None
    pattern = None
    tc_id = 0
    with open(path_to_testcases, 'r') as f:
        line = f.readline().strip("\n")
        while(line):
            line = line.strip("\n")
            if len(line) == 0:
                pass
            elif(line[-1] == ':'):
                # New Token Class
                tc_id = 0
                current_token = line[:-1]
                if current_token not in regex:
                    print(f"Token {current_token} not found!")
                    exit(0)

                pattern = re.compile((regex[current_token]))
                if VERBOSE:
                    print(f"{CYAN}Testcases for {current_token} - {regex[current_token]}{RESET}")
            else:
                # Get Expected Result
                expected_result = None
                if(line[0] == '-'):
                    expected_result = True
                elif line[0] == '!':
                    expected_result = False
                else:
                    print("Invalid character in test file!")
                    exit(0)
                
                tc_id += 1
                if not current_token:
                    print("Invalid Regex Testcases file at: ", path_to_testcases)
                    exit(0)
                validate(line[3:-1], expected_result, pattern, current_token, tc_id)

            line = f.readline()
            
if __name__ == "__main__":
    import sys
    sys.path.append(os.getcwd())
    get_data()
    get_regex()
    check_testcases()
    test_dict['failed'] = test_dict['total'] - test_dict["passed"]
    print(f"{CYAN}Passed: {GREEN}{test_dict['passed']}/{test_dict['total']} {CYAN}Failed: {RED}{test_dict['failed']}/{test_dict['total']}{RESET}")
