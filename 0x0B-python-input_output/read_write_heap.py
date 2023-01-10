#!/usr/bin/python3
"""This module contains a script that finds a string in the heap of a
    running process, and replaces it.
"""
import sys


def error():
    print("Usage: read_write_heap.py pid search_string replace_string",
          file=sys.stdout)
    exit(1)


args = sys.argv
if len(args) != 4:
    error()

pid = args[1]
string = args[2]
new_string = args[3]

fmaps = "/proc/{}/maps".format(pid)
fmem = "/proc/{}/mem".format(pid)


with open(fmaps, 'r') as map_file:
    for line in map_file:
        if ("[heap]") in line:
            heap = line
            break

heap = heap.split()
addr_start = int(heap[0].split("-")[0], 16)
addr_end = int(heap[0].split("-")[1], 16)
print("=" * 50)
print("[*] Path:\t{}".format(heap[5]))
print("  [.] Address:\tbeg-[{}]\tend-[{}]".format(
    heap[0].split("-")[0], heap[0].split("-")[1]))
print("  [.] Perms:\t{}".format(heap[1]))
print("  [.] Offset:\t{}".format(heap[2]))
print("  [.] Dev:\t{}".format(heap[3]))
print("  [.] Inode :\t{}".format(heap[4]))

if "r" not in heap[1] or "w" not in heap[1]:
    print("Permissions error", file=sys.stdout)
    exit(1)

with open(fmem, 'rb+') as mem_file:
    mem_file.seek(addr_start)
    heap = mem_file.read(addr_end - addr_start)
    print("=" * 50)
    try:
        i = heap.index(bytes(string, "ASCII"))
    except Exception:
        print("Can't find '{}'".format(string), file=sys.stdout)
        exit(1)
    print("[*] Found '{}' at {}".format(string, i))

    print("=" * 50)
    print("[*] Writing '{}' at {:x}".format(new_string, addr_start + i))
    mem_file.seek(addr_start + i)
    mem_file.write(bytes(new_string, "ASCII"))
