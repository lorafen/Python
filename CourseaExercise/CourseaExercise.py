#def computepay(h,r):
#    if (h > 40):
#        result = ( (h - 40) * 1.5 * r ) + ( 40 * r )
#    else:
#        result = h * r            
#    return result

#try:
#    hrs = float(input("Enter Hours:"))
#    rate = float(input("Enter Rate:"))
#except:
#    print("yes")
#    quit()
        
#p = computepay(hrs,rate)
#print(p)

#largest = None
#smallest = None
#while True:
#    number = raw_input("Enter a number: ")  
    
#    if len(number) < 1:
#        break
    
#    if number == "done" : 
#        break
    
#    try:
#        num = float(number)
#    except:
#        print("Invalid input")
#        continue
    
#    if (largest == None):
#        largest = num
        
    
#    elif ((largest > num) and (smallest == None)):
#        smallest = num
    
#    elif ((largest > num) and (smallest != None)):
     
#        if (smallest > num):
#            smallest = num
    
#    elif (largest < num):
#        largest = num

        
        
#print("Maximum is", int(largest))
#print("Minimum is", int(smallest))

#text = "X-DSPAM-Confidence:    0.8475";
#sign = []
#number = []
## counting how many char is in string
#count = len(text)

## looking for number
#num_address = text.find('0')

#number = text[int(num_address):int(count)]
#print(number)

## Use word.txt as the file name
#fname = input("Enter file name: ")
#fh = open(fname)

#for line in fh:
#    line = line.rstrip().upper()
#    print(line)

## Use the file name mbox-short.txt as the file name
#fname = input("Enter file name: ")
#file = open(fname)
#count = 0
#average = 0
#total = 0
#for line in file:
#	# Looking for text "X-DSPAM-Confidence:" and float value then count an average    
#    if not line.startswith("X-DSPAM-Confidence:") : 
#        continue
#    count += 1
#    numAddress = line.find(':')
#    number = float(line[numAddress+1:len(line)]) 
#    total += number
#average = total/count 
#print("Average spam confidence: " + str(average))