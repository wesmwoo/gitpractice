'''def fixstrings(myStrings):
    newlist = []
    for i in myStrings:
        newitem = i[1:-1]
        for j in len(newitem):
            if newitem[j] = int:
                pass
            else:
                newitem[j] = newitem[j].capitalize()
                return newitem
        newlist.append(newitem)
    newlist.reverse()
    return newlist

myList = ['25maroon', 'ComBInE', 'apple', '0315']

print fixstrings(myList)


numbers = {1:'one', 2:'two'}
print numbers.get(2)

a = ["hi","hello", "bye"]
v = list(range(3))
dict1 = {}
count = 0
for item in a:
	dict1[item] = v[count]
	count += 1
print dict1

list1 = [1,2,3,4]
list2 = [2,4,7]

def fun(list1,list2):
	newlist = []
	for item in list1:
		if item in list2:
			newlist.append(item)
	return newlist
'''

x = raw_input("PASSWORD: ")
print "LOADING......."
print ""
print ""
print "VERIFYING USER..."
print ""
print ""
if x == "***********":
        running = True
        print "WELCOME TO THE CIA MAINFRAME DATABASE"
        while running == True:
            y = raw_input("QUERY?")
            if y == 'METIN SAY':
                    print ' '
                    print "FROM ISTANBUL TURKEY"
                    print ' '
                    print "CURRENTLY ATTENDS MIT"
                    print ' '
                    print "TERRORIST THREAT LEVEL: MODERATE"
            elif y  == "CAMERON KORB" or y == "CAMERON A KORB":
                    print ' '
                    print "FROM LOS GATOS, CALIFORNIA"
                    print ' '
                    print "CURRENTLY ATTENDS MIT"
                    print ' '
                    print "TERRORIST THREAT LEVEL: NEGLIGIBLE"
            elif y == "WESLEY WOO":
                    print ' '
                    print "FROM PALO ALTO, CALIFORNIA"
                    print ' '
                    print "CURRENTLY ATTENDS MIT"
                    print ' '
                    print "TERRORIST THREAT LEVEL: LOW"
            elif y == "LOGAN MCLAUGHLIN" or y == "LOGAN S MCLAUGHLIN":
                    print ' '
                    print "FROM PARK CITY, UTAH"
                    print ' '
                    print "CURRENTLY ATTENDS MIT"
                    print ' '
                    print "TERRORIST THREAT LEVEL: LAUGHABLE"
            elif y == "ANDY RODRIGUEZ":
                    print ' '
                    print "FROM CUMMINGS, GEORGIA"
                    print ' '
                    print "CURRENTLY ATTENDS MIT"
                    print ' '
                    print "TERRORIST THREAT LEVEL: NEGLIGIBLE"
            elif y == "BINH LE":
                    print ' '
                    print "FROM PORTAGE, MICHIGAN"
                    print ' '
                    print "CURRENTLY ATTENDS MIT"
                    print ' '
                    print "TERRORIST THREAT LEVEL: NEGLIGIBLE"
            elif y == "TRAVIS LEATHRUM":
                    print ' '
                    print "UNKNOWN ORIGINS"
                    print ' '
                    print "UNKNOWN EDUCATION STATUS"
                    print ' '
                    print "TERRORIST THREAT LEVEL: HIGH"
            elif y == "QUIT":
                running = False
            else:
                    print ' '
                    print "SECURITY CLEARANCE ERROR"
                
else:
        print "ERROR"
        
