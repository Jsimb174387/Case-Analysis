import csv
from spectrum2 import *

def simulate(amount):
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

def save(name, array):
    #then saves to csv
    with open(name, 'w') as csvfile:
        filewriter = csv.writer(csvfile, delimiter=',')
        for value in array:
             filewriter.writerow([value])



