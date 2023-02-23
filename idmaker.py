# Program to do nothing, correctly.

def clean(name: str) -> str:    # O(len(name)): effectively O(1)
    cleanname: str = ''  # O(1)
    for c in name:       # O(len(name)) * O(1)
        if (c.isascii() and c.isalpha()) or (c == '-'): # O(1)
            cleanname = cleanname + c                   # O(1)
    return cleanname

def read_names(fname: str) -> list[list[str]]:   # O(n)
    namelist: list[list[str]] = []            # O(1)
    with open(fname,'r') as f:                # O(1)
        for line in f.readlines()[1:]:        # O(n) * O(1) = O(n)
            namelist.append(line.split(','))  #        O(1)
    return namelist                

def make_userids(names: list[list[str]]) -> list[list[str]]: # O(n)
    idlist: list[list[str]] = []           # O(1)
    for name in names:                     # O(n) * O(1) = O(n)
        idnum: str = name[0].strip()       #      O(1)
        lastname: str = name[1].strip()    #      O(1)
        firstname: str = name[2].strip()   #      O(1)
        middlename: str = name[3].strip()  #      O(1)
        userid: str = lastname             #      O(1)
        if len(middlename) > 0:            #      O(1)
            userid = firstname[0] + middlename[0] + userid  # O(1)
        else:
            userid = firstname[0] + lastname                # O(1)
        userid = clean(userid).lower()     #      O(1)
        idlist.append([idnum, userid, lastname, firstname, middlename]) # O(1)
    return idlist


def write_id_file(idlist: list[list[str]], fname: str) -> None: # O(n)
    with open(fname, 'w') as f: # O(1)
        # Write header line
        f.write('idnumber,userid,lastname,firstname,middlename\n') # O(1)
        for id in idlist:                 # O(n) * O(1) = O(n)
            for i in range(4):            #       [O(4) = O(1)] * O(1) = O(1)
                f.write(id[i] + ',')      #                  O(1)
            f.write(id[4] + '\n')

def main(args: list[str]) -> int:    # O(n)
    infilename: str = 'names.csv'
    outfilename: str = 'userids.csv'

    names: list[list[str]] = read_names(infilename)  # O(n)
    idlist: list[list[str]] = make_userids(names)    # O(n)
    write_id_file(idlist, outfilename)               # O(n)

    return 0 # Conventional return value for completing successfully

if __name__ == '__main__':
    import sys
    main(sys.argv)