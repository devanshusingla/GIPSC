import os, sys

basepath = os.environ.get("ROOT_PATH")

for (root, dir, files) in os.walk(basepath + "tests/Milestone3/", topdown = True):
    files = sorted(files)
    for file in files:
        if file.endswith("go"):
            returnval = os.system("python3 " + basepath + "src/Milestone3/parser.py " + basepath + "tests/Milestone3/" +  file + " > /dev/null")
            if returnval == 0 and file.startswith("c"):
                print("File " + file + " passed")
            elif returnval != 0 and file.startswith("w"): 
                print("File " + file + " passed")
            else: 
                print("File " + file + " failed")
            