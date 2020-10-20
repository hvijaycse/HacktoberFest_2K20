#! /usr/bin/python3
filename = input("Enter the file name: ")
lines = 0
with open(filename, 'r') as f:
    for line in f:
        lines += 1
print("Number of lines:")
print(lines)
