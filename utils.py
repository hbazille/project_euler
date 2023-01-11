
def parse_line_int(filename):
    l = []
    lines = open(filename, 'r').readlines()
    for line in lines:
        t = line.split()
        for e in t:
            l.append(e)
    return l
    
    
    
def parse_line_ints(filename):
    """
    integers separated by spaces
    """
    l = []
    lines = open(filename, 'r').readlines()
    for line in lines:
        l.append([])
        t = line.split()
        for e in t:
            l[-1].append(int(e))
    return l
