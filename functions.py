def query(toask, acceptableinputs=None, charonly=False, numonly=False):
    queryanswr = input(toask)
    if acceptableinputs != None:
        for i in acceptableinputs:
            print("INPUTCHECKING: "+i)
            if queryanswr.lower() in i:
                return queryanswr.lower()
        print("ERROR: NOT FOUND IN ACCEPTABLEINPUTS")
        queryanswr = query(toask, acceptableinputs, charonly, numonly)
    if charonly == True:
        if queryanswr.isalpha() == True:
            return queryanswr
        else:
            print("ERROR: NOT ALPHABETIC")
            query(toask, acceptableinputs, charonly, numonly)
    if numonly == True:
        if queryanswr.isnumeric() == True:
            return queryanswr
        else:
            print("ERROR: NOT NUMERIC")
            query(toask, acceptableinputs, charonly, numonly)
    return queryanswr