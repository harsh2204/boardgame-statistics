from dice import Dice
if __name__ == "__main__":
    di = Dice()
    di.roll()
    i=0
    while(i<100):
        di.roll()
        i+=1
    di.plot_probabilities()