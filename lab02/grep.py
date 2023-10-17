import re

def grep(lines, pattern, ignore_case=False, whole_word=False):
    flags = 0
    if ignore_case:
        flags |= re.IGNORECASE

    if whole_word:
        pattern = fr'\b{pattern}\b'

    regex = re.compile(pattern, flags)

    for line in lines:
        if regex.search(line):
            print(line.strip())

def grepWithParserDecorator(args):
    if len(args) < 1:
        print("Za mało argumentów")
        return

    ignore_case = False
    whole_word = False

    bodyStart = 0

    for idx, arg in enumerate(args):
        if arg == "-i" or arg == "--ignore-case":
            ignore_case = True
            bodyStart = idx+1
        elif arg == "-w" or arg == "--word-regexp":
            whole_word = True
            bodyStart = idx+1

    pattern = args[bodyStart]

    grep(args[bodyStart+1:], pattern, ignore_case, whole_word)
