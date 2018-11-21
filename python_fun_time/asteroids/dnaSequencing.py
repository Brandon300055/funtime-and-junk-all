"""
Write your code in this file.

DO NOT RENAME THIS FILE
if you do, the unittests will not run.
"""
import os
import difflib


# Takes a filename(str) and returns a list of the contents
def fileToList(filename):
    if not os.path.exists(filename):
        return []
    return [line.strip() for line in open(filename, 'r')]

#Takes a string list and returns the first string.
def returnFirstString(strings):
    if len(strings) < 1:
        return ''
    else:
        for i in range(len(strings)):
            return strings[0]


def strandsAreNotEmpty(strand1, strand2):
    if len(strand1) >= 1:
        if len(strand2) >= 1:
            return True
        else:
            return False
    else:
        return False
        
def strandsAreEqualLengths(strand1, strand2):
    if len(strand1) == len(strand2):
        return True
    else:
        return False
        
#def findLargestOverlap(target, candidate):



def findLargestOverlap(target, candidate):
    #check they are same size
    if not strandsAreEqualLengths(target, candidate):
        return -1
    # check they are not empty
    if not strandsAreNotEmpty(target, candidate):
        return -1
        # check they are the same
    if target == candidate:
        return len(target)
    for i in range(len(target)):
        if target[i:] == candidate[:-i]:
            return len(target)-i
    return 0


# Takes str and string list as input
# returns tuple of (string, int)
def findBestCandidate(target, candidates):
    num = 0
    string = ''
    for candidate in candidates:
        find = findLargestOverlap(target, candidate)
        if find > num:
            num = find
            string = candidate

    return (string, num)
        
    
#joinTwoStrands
        
def joinTwoStrands(target, candidate, overlap):
    ans = ''
    first = target
    final = candidate[overlap:]
    ans = first + final
    return ans


def main():

    target_filename = input("Target strand filename:")
    candidate_filename = input("Candidate strands filename:")
    
    target = returnFirstString(fileToList(target_filename))
    candidate_list = fileToList(candidate_filename)
    (best, index) = findBestCandidate(target, candidate_list)
    
    print(joinTwoStrands(target, best, index))
    

     
if __name__ == "__main__":
    main()