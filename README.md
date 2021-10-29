# We are working on a security system for a badged-access room in our company's building.

# Given an ordered list of employees who used their badge to enter or exit the room, write a function that returns two collections:

# 1. All employees who didn't use their badge while exiting the room - they recorded an enter without a matching exit. (All employees are required to leave the room before the log ends.)

# 2. All employees who didn't use their badge while entering the room - they recorded an exit without a matching enter. (The room is empty when the log begins.)

# Each collection should contain no duplicates, regardless of how many times a given employee matches the criteria for belonging to it.

# badge_records_1 = [
#   ["Martha",   "exit"],
#   ["Paul",     "enter"],
#   ["Martha",   "enter"],
#   ["Steve",    "enter"],
#   ["Martha",   "exit"],
#   ["Jennifer", "enter"],
#   ["Paul",     "enter"],
#   ["Curtis",   "exit"],
#   ["Curtis",   "enter"],
#   ["Paul",     "exit"],
#   ["Martha",   "enter"],
#   ["Martha",   "exit"],
#   ["Jennifer", "exit"],
#   ["Paul",     "enter"],
#   ["Paul",     "enter"],
#   ["Martha",   "exit"],
#   ["Paul",     "enter"],
#   ["Paul",     "enter"],
#   ["Paul",     "exit"],
#   ["Paul",     "exit"] 
# ]

# Expected output: ["Paul", "Curtis", "Steve"], ["Martha", "Curtis", "Paul"]

# Other test cases:

# badge_records_2 = [
#   ["Paul", "enter"],
#   ["Paul", "exit"],
# ]

# Expected output: [], []

# badge_records_3 = [
#   ["Paul", "enter"],
#   ["Paul", "enter"],
#   ["Paul", "exit"],
#   ["Paul", "exit"],
# ]

# Expected output: ["Paul"], ["Paul"]

# badge_records_4 = [
#   ["Paul", "enter"],
#   ["Paul", "exit"],
#   ["Paul", "exit"],
#   ["Paul", "enter"],
# ]

# Expected output: ["Paul"], ["Paul"]

# n: length of the badge records array

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