import sys, getopt, os
import json
from pprint import pprint
import csv
import random

#with open('HackathonData2019/Data/json/data01.INT.json') as f:
#    data = json.load(f)

#pprint(data)

fake_identities = []
identityMap = {}

def obfuscation(input, output):
    outString = []
    with open(input) as f:
        data = json.load(f)

        # preprocess: match each user to a random identity
        for user in data:
            randomIdx = random.randint(1, len(fake_identities))
            identityMap[user["Name"]] = fake_identities[randomIdx]#fake_identities[randomIdx]["Username"]

        # anonymize each json block   
        for user in data:
            outString.append(anonymize(user))

        with open(output, "w") as write_file:
            json.dump(outString, write_file)

def anonymize(user):

    #pprint(user['Id'])
    print( user["Name"] )
    pprint( identityMap.get(user["Name"]) )
    #user["Id"] = fake_identities[identityMap.get(user["Name"])
   # print(fake_identities[identityMap[user["Name"])
    return user


# Get input/output file names from command line
def main(argv):
    inputFile = ''  
    outputFile = ''
    try:
        opts, args = getopt.getopt(argv,"hi:o:",["ifile=","ofile="])
    except getopt.GetoptError:
        print('test.py -i <inputfile> -o <outputfile>')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print('test.py -i <inputfile> -o <outputfile>')
            sys.exit()
        elif opt in ("-i", "--ifile"):
            inputFile = arg
        elif opt in ("-o", "--ofile"):
            outputFile = arg
    #print('Input file is: ', inputFile)
    #print('Output file is: ', outputFile) 

    # Parse in fake identities, save to a map
    with open('fake_identities.csv', mode='r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                line_count += 1
            else:
                fake_identities.append(row)
                line_count += 1

    obfuscation(inputFile, outputFile)  


if __name__ == "__main__":
   main(sys.argv[1:])

