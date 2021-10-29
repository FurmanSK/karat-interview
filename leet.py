# My attempt at the coding test for indeed.
# See README.md for the requirements and test cases.
import time

'''
Uses sets so as to not have duplicates so no explicit check if name in set.
'''
def setfunc(badge_records: list) -> tuple[list, list]:

    # hash table
    ds = {}
    first = set()
    second = set()

    for p in badge_records:
        name = p[0]
        # Initalize the person into the hash
        if name not in ds:
            ds[name] = [False, False]
        
        if p[1] == "enter":
            if ds[name][0]:
                # first case
                first.add(name)
            else:
                ds[name][0] = True
        
        if p[1] == "exit":
            if (not ds[name][0]) :
                # second case
                second.add(name)
                ds[name][1] = False
            else:
                #clear as valid enter/exit
                ds[name][0] = False
                ds[name][1] = False
    # If end of log but have left over enters flag as first case
    for p in ds:
        if ds[p][0]:
            first.add(p)

    return list(first), list(second)

'''
  Uses a list and checks if name is in list method vs set
'''
def listfunc(badge_records: list) -> tuple[list, list]:
    
    # hash table
    ds = {}
    first = []
    second = []

    for p in badge_records:
        name = p[0]
        # Initalize the person into the hash
        if name not in ds:
            ds[name] = [False, False]
        
        if p[1] == "enter":
            if ds[name][0]:
                # first case
                if name not in first:
                  first.append(name)
            else:
                ds[name][0] = True
        
        if p[1] == "exit":
            if (not ds[name][0]) :
                # second case
                if name not in second:
                  second.append(name)
                ds[name][1] = False
            else:
                #clear as valid enter/exit
                ds[name][0] = False
                ds[name][1] = False
    # If end of log but have left over enters flag as first case
    for p in ds:
        if ds[p][0]:
          if p not in first:
            first.append(p)

    return list(first), list(second)  

badge_records_1 = [
  ["Martha",   "exit"],
  ["Paul",     "enter"],
  ["Martha",   "enter"],
  ["Steve",    "enter"],
  ["Martha",   "exit"],
  ["Jennifer", "enter"],
  ["Paul",     "enter"],
  ["Curtis",   "exit"],
  ["Curtis",   "enter"],
  ["Paul",     "exit"],
  ["Martha",   "enter"],
  ["Martha",   "exit"],
  ["Jennifer", "exit"],
  ["Paul",     "enter"],
  ["Paul",     "enter"],
  ["Martha",   "exit"],
  ["Paul",     "enter"],
  ["Paul",     "enter"],
  ["Paul",     "exit"],
  ["Paul",     "exit"] 
]

badge_records_2 = [
  ["Paul", "enter"],
  ["Paul", "exit"],
]

badge_records_3 = [
  ["Paul", "enter"],
  ["Paul", "enter"],
  ["Paul", "exit"],
  ["Paul", "exit"],
]

badge_records_4 = [
  ["Paul", "enter"],
  ["Paul", "exit"],
  ["Paul", "exit"],
  ["Paul", "enter"],
]

t0 = time.time()
print(setfunc(badge_records_1))
print(setfunc(badge_records_2))
print(setfunc(badge_records_3))
print(setfunc(badge_records_4))
t1 = time.time()
total = t1 - t0
print(total)
print(total*1000)

t0 = time.time()
print(listfunc(badge_records_1))
print(listfunc(badge_records_2))
print(listfunc(badge_records_3))
print(listfunc(badge_records_4))
t1 = time.time()
total = t1 - t0
print(total)
print(total*1000)