import numpy as np

NTAB = 32
IA = 16807
#Equal to MAX_RANDOM_RANGE
IM = 2147483647
IQ = 127773
IR = 2836
NDIV = 1+(IM-1)//NTAB
#hexadecimal value for highest positive integer
MAX_RANDOM_RANGE = 0x7FFFFFFF
AM = 1.0/IM
EPS = 1.2e-7
RNMX = 1.0-EPS

class Stream:
    
    def __init__(self):
        self.mIdum = None
        self.mIy = None
        self.mIv = [0] * NTAB

    def SetSeed(self, iSeed: int):
        self.mIdum = iSeed
        if iSeed >= 0:
            self.mIdum = -iSeed

        self.mIy = 0

    def GenerateRandomNumber(self) -> int:
        k = 0

        if self.mIdum <= 0 or self.mIy == 0:
            if -self.mIdum < 1:
                self.mIdum = 1
            else:
                self.mIdum = -self.mIdum

            j = NTAB+7
            while j >= 0:
                k = self.mIdum // IQ
                self.mIdum = IA*(self.mIdum-(k*IQ))-(IR*k)
                if self.mIdum < 0:
                    self.mIdum += IM

                if j < NTAB:
                    self.mIv[j] = self.mIdum

                j -= 1

        
            self.mIy = self.mIv[0]
        
        k = self.mIdum // IQ
        self.mIdum = IA * (self.mIdum - k * IQ) - IR*k

        if self.mIdum < 0:
            self.mIdum += IM

        j = self.mIy // NDIV

        self.mIy = self.mIv[int(j)]
        self.mIv[int(j)] = self.mIdum

        return self.mIy

    def RandomFloat(self, flLow: np.float32, flHigh: np.float32) -> np.float32:
        # float in [0, 1)
        fl = AM * np.float32(self.GenerateRandomNumber())

        if fl > RNMX:
            fl = RNMX

        return (fl * (flHigh - flLow)) + flLow # float in [low,high)]

    def RandomFloatExp(self, flMinVal: np.float32, flMaxVal: np.float32, flExponent: np.float32) -> np.float32:
        # float in [0, 1)
        fl = AM * np.float32(self.GenerateRandomNumber())

        if flExponent != 1.0:
            fl = np.float32(np.power(np.float64(fl), np.float64(flExponent)))

        return (fl * (flMaxVal - flMinVal)) + flMinVal # float in [low,high)

    def RandomInt(self, iLow: int, iHigh: int) -> int:
        x = iHigh - iLow + 1

        if x <= 1 or MAX_RANDOM_RANGE < x-1:
            return iLow

        # From Source Engine 2007:
	    # The following maps a uniform distribution on the interval [0,MAX_RANDOM_RANGE]
	    # to a smaller, client-specified range of [0,x-1] in a way that doesn't bias
	    # the uniform distribution unfavorably. Even for a worst case x, the loop is
	    # guaranteed to be taken no more than half the time, so for that worst case x,
	    # the average number of times through the loop is 2. For cases where x is
	    # much smaller than MAX_RANDOM_RANGE, the average number of times through the
	    # loop is very close to 1. 
        maxAcceptable = MAX_RANDOM_RANGE - ((MAX_RANDOM_RANGE+1) % x)

        while True:
            n = self.GenerateRandomNumber()
            print(n)
            if n <= maxAcceptable:
                break

        return iLow + (n % x)

def main():
    print("It works. Trust me...")

if __name__ == "__main__":
    main()