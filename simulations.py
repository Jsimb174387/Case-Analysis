import csv
from spectrum2 import *
from caseCollections import *

def simulate(amount):
    #simulates spectrum. This is left this as legacy code tbh, don't want to break anything by changing
    spec2 = spectrum('The Spectrum 2 Collection')

    spec = spectrum('The Spectrum Collection')

    spec2.sim_case_opens(amount)
    spec.sim_case_opens(amount)
    spec2_unique_hash = []
    spec2_every_hash = []
    for  skinObject in spec2.simInventory:
        #gets every hash name, then every unique hash name
        hash = skinObject.hash
        spec2_every_hash.append(hash)
        if not hash in spec2_unique_hash:
            spec2_unique_hash.append(hash)

    spec_unique_hash = []
    spec_every_hash = []
    for skinObject in spec.simInventory:
        #gets every hash name, then every unique hash name
        hash = skinObject.hash
        spec_every_hash.append(hash)
        if not hash in spec_unique_hash:
            spec_unique_hash.append(hash)
    save('s2unique.csv', spec2_unique_hash)
    save('s2every.csv', spec2_every_hash)
    save('spectunique.csv', spec_unique_hash)
    save('spectevery.csv', spec_every_hash)


def simCase(caseType, amount, fileName, collection = None):
    #generic verion of simulate.
    #collection is the normal collection names we have been using.
    #Case types is used to determine the case in caseCollection. As of now it is chroma, prisma, horizon / dangerzone.
    # checking for str identical to the class name.
    #file name is simply a str that will be added to to get the name for the csv. If fileName = prisma, then
    # prismaUnique.csv and prismaEvery.csv will be generated.

    if caseType == 'chroma':
        case = chroma(collection)
    if caseType == 'prisma':
        case = prisma(collection)
    if caseType == 'horizon':
        case = horizon(collection)

    case.sim_case_opens(amount)

    case_unique_hash = []
    case_every_hash = []
    for skinObject in case.simInventory:
        # gets every hash name, then every unique hash name
        hash = skinObject.hash
        case_every_hash.append(hash)
        if not hash in case_unique_hash:
            case_unique_hash.append(hash)

    save(fileName + 'Unique.csv', case_unique_hash)
    save(fileName + 'Every.csv', case_every_hash)
    return case


def save(name, array):
    #then saves to csv
    with open(name, 'w') as csvfile:
        filewriter = csv.writer(csvfile, delimiter=',')
        for value in array:
             filewriter.writerow([value])
