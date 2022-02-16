import sys,os

def c_toint(s):
    ans = 0
    i = 0
    while (s[i].isdigit()):
        ans = 10*ans + int(s[i])
        i+=1
    
    return ans 

def c_tolabel(s):
    s = ""
    i = 0
    # print(s.split)

def generate_list(f):
    for line in f:
        line = line.split(" ")
        source = int(line[0])
        i = 3
        while i < len(line):
            if line[i][0] == '-':
                i += 2
                continue
            dest = c_toint(line[i])
            label = line[i-1].split('\'')[1]
            to_append = str(source) + " -> " + str(dest) + " [ label=\"" + label + "\" ];\n"
            out_file.write(to_append)
            ad_list[source].append(dest)
            i += 2
    

ad_list = []

f = open("action.txt", "r")

read_file = f.read()
sep_list = read_file.split("\n")

num_states = len(sep_list) - 1

for x in range(num_states):
    ad_list.append([])

out_file = open("test.dot", "w")
out_file.write("digraph G {\n")


f = open("action.txt", "r")
generate_list(f)

f = open("goto.txt", "r")
generate_list(f)

out_file.write("}")

print(ad_list)
