# My attempt at the coding test for indeed.
# See README.md for the requirements and test cases.
def func(badge_records: list) -> tuple[set, set]:

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

    return first, second
    
    

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

badge_records = [
  ["Paul", "enter"],
  ["Paul", "exit"],
  ["Paul", "exit"],
  ["Paul", "enter"],
]

print(func(badge_records_1))