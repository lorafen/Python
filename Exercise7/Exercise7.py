# Well, let's play
import re
 
def NumberFromText(strings):
    numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    Sentence = []
    num = []
    address = []
    # Divide string to single sign list
    for i in strings:
        Sentence.append(i)
    # check numbers in sentence
    for char in Sentence:
        for number in numbers:
            if (str(number) == char):
                num.append(char)
    # remove numbers from sentence
    for number in num:
        Sentence.remove(number)  
    # List return to string
    StringText = ''.join(Sentence)
    # Finding dot in text
    address = StringText.find(".")
    # Divide sentences
    sentence1 = StringText.split(".")
    for i in range(len(sentence1)):
        print('Zdanie ' + str(i+1) + ': ' + str(sentence1[i])); 

    print(num)
    return

# Read text from user
#string1 = input('Podaj ciag znakow: ')
string1 = 'A111la m2a kota 444 duzego. T3en spi6 wciaz'
NumberFromText(string1)