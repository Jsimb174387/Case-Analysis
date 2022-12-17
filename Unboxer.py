import random
import csv
import numpy as np
from weapon import skin
from keyvalues import KeyValues
import vdf
from case import *
from spectrum2 import *

spec2 = spectrum('The Spectrum 2 Collection')

spec = spectrum('The Spectrum Collection')

spec2.knife_unbox()
#spec.sim_case_opens(10000)

"""with open('OpenedCases.csv', 'w') as lootFile:
    filewriter = csv.writer(csvfile, delimiter=',')
    #Creates header row
    filewriter.writerow(['hash_name', 'stattrak', 'market_low'])

    for """
