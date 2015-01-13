# Coursea exercises
import itertools

def computepay(h,r):
    if (h > 40):
        result = ( (h - 40) * 1.5 * r ) + ( 40 * r )
    else:
        result = h * r            
    return result

def LargestSmallest():
    largest = None
    smallest = None
    print("Write DONE to end")
    while True:
        number = input("Enter a number: ")  
        if len(number) < 1:
            break
    
        if number == "done" : 
            break
    
        try:
            num = float(number)
        except:
            print("Invalid input")
            continue
    
        if (largest == None):
            largest = num
        
    
        elif ((largest > num) and (smallest == None)):
            smallest = num
    
        elif ((largest > num) and (smallest != None)):
     
            if (smallest > num):
                smallest = num
    
        elif (largest < num):
            largest = num

    print("Maximum is", int(largest))
    print("Minimum is", int(smallest))
    return

def NumberFromString():
    text = "X-DSPAM-Confidence:    0.8475";
    print(text)
    
    # counting how many char is in string
    count = len(text)

    # looking for number
    num_address = text.find('0')

    number = text[int(num_address):int(count)]
    print(number)
    return

def OpenAndChange():
    # Use word.txt as the file name
    print("File name: word.txt")
    fname = input("Enter file name: ")
    fh = open(fname)
    for line in fh:
        line = line.rstrip().upper()
        print(line)
    return

def AverageFromFile():
    # Use the file name mbox-short.txt as the file name
    print("File name: mbox-short.txt")
    fname = input("Enter file name: ")
    file = open(fname)
    count = 0
    average = 0
    total = 0
    # Looking for text "X-DSPAM-Confidence:" and float value then count an average   
    for line in file: 
        if not line.startswith("X-DSPAM-Confidence:") : 
            continue
        count += 1
        numAddress = line.find(':')
        number = float(line[numAddress+1:len(line)]) 
        total += number
    average = total/count 
    print("Average spam confidence: " + str(average))
    return

def CreateListFromFile():
    #print("File name: romeo.txt")
    #fname = input("Enter file name: ")
    fh = open("romeo.txt")
    lst = list()
    
    for line in fh:
        line = line.split()
        count = 0
        [lst.append(word) for word in line if word not in lst]
    lst.sort()
    print(lst)
    return
    
def AddressFromFile():
    fname = input("Enter file name: ")
    if len(fname) < 1 : 
        fname = "mbox-short.txt"
    fh = open(fname)
    lst = list()
    words = list()
    count = 0
    for line in fh:
        line = line.rstrip()
        if line.startswith("From "):
            count += 1
            line = line.split()
            del line[0]
            del line[1]
            del line[1]
            del line[1]
            del line[1]
            del line[1]
            print(''.join(line))

    print( "There were " + str(count) + " lines in the file with From as the first word")
    return

# program to read through the mbox-short.txt and figure out who has the sent the greatest number of mail messages
def WhoSentMail():
    name = input("Enter file:")
    if len(name) < 1 : 
        name = "mbox-short.txt"
    
    handle = open(name)
    
    emails = list()
    # etract e-mail from text
    for line in handle:
        if (line.find('Author') != -1):
            word = line.split()
            del word[0]
            emails.append(word[0])
  
    counts = dict()
    for email in emails:
        counts[email] = counts.get(email,0) + 1
    
    # maxsimum loop
    max = None
    maxMail = None
    for mail, val in counts.items():
        if max == None:
            max = val
            maxMail = mail
        if max < val:
            max = val
            maxMail = mail

    print(maxMail, max) 
           
    return

def HourFromFile():
    name = input("Enter file:")
    if len(name) < 1 : 
        name = "mbox-short.txt"

    handle = open(name)
    dateFromFile = list()
    counts = dict()
    for line in handle:
        if line.startswith('From '):
            words = line.split()
            numbers = words[5].split(':')
            dateFromFile.append(numbers[0])

    for element in dateFromFile:
        counts[element] = counts.get(element, 0) + 1
    
    hours = list()
    for k, val in counts.items():
        newTup = (k, val)
        hours.append(newTup)
    
    hours.sort()

    for k, val in hours:
        print(k, val)
    return


while True:
    # Menu
    print("1 - Compute pay")
    print("2 - Smallest and largest number")
    print("3 - Getting number from string")
    print("4 - Open and read modyfing text file")
    print("5 - Counting average from text file")
    print("6 - Create List")
    print("7 - Address From File")
    print("8 - Who has sent the greatest number of email messages")
    print("9 - Hour and how many times")
    print("0 - End of program")
    choose = input("Your choice: ")


    if (choose == '0'):
        break
    elif (choose == '1'):
        try:
            hrs = float(input("Enter Hours:"))
            rate = float(input("Enter Rate:"))
        except:
            print("yes")
            quit()
        p = computepay(hrs,rate)
        print(p)
    elif (choose == '2'):
        LargestSmallest()
    elif (choose == '3'):
        NumberFromString()
    elif (choose == '4'):
        OpenAndChange()
    elif (choose == '5'):
        AverageFromFile()
    elif (choose == '6'):
        CreateListFromFile()
    elif (choose == '7'):
        AddressFromFile()
    elif (choose == '8'):
        WhoSentMail()
    elif (choose == '9'):
        HourFromFile()
    else:
        print("Wrong choice, try again!")