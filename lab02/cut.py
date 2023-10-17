import sys


def cut(lines, fieldsList, delimiter="\t"):

    for line in lines:
        fields = line.split(delimiter)
        fields = getListItemByIndexFromList(fields, getIndexListFromString(fieldsList))
        print(fields)
def getListItemByIndexFromList(array, ids):
    return [a for i, a in enumerate(array) if i+1 in ids]

def getIndexListFromString(string):

    result = []
    if str.isnumeric(string):
        result.append(int(string))
        return result

    ranges = string.split(",")
    for singlerange in ranges:
        if '-' in singlerange:
            start, end = singlerange.split('-')
            print([int(start),end])
            result.extend(range(int(start), int(end)+1))
        else:
            result.append(int(singlerange))
    return result

def cutWithParserDecorator(argv):
    if len(argv) < 1:
        print("Za mało argumentów")
        return

    delimiter = "\t"
    fields = ""

    bodyStart = 0

    for idx, arg in enumerate(argv):
        if arg == "-d" or arg == "--delimiter":
            delimiter = argv[idx+1]
            bodyStart = idx+2
        elif arg == "-f" or arg == "--fields":
            fields = argv[idx+1]
            bodyStart = idx+2

    fieldsList = argv[bodyStart:]

    cut(fieldsList, fields, delimiter)
    
#py .\cut.py -d : -f 1,10,9,8,1,6 root:x:0:0:root:/root:/bin/bash bin:x:1:1:bin:/bin:/sbin/nologin daemon:x:2:2:daemon:/sbin:/sbin/nologin
#cutWithParserDecorator(sys.argv)