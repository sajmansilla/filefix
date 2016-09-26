import easygui as eg

msg = "Enter your personal information"
title = "Credit Card Application"
fieldNames = ["Name", "Street Address", "City", "State", "ZipCode"]
fieldValues = []  # we start with blanks for the values
fieldValues = eg.choicebox(msg, title, fieldNames)

# make sure that none of the fields was left blank
while 1:
    if fieldValues == None: break
    errmsg = ""
    for i in range(len(fieldNames)):
        if fieldValues[i].strip() == "":
            errmsg = errmsg + ('"%s" is a required field.' % fieldNames[i])
    if errmsg == "": break # no problems found
    fieldValues = choicebox(errmsg, title, fieldNames, fieldValues)

print("Reply was:", fieldValues)