#dice.py
import numpy as np
import matplotlib.pyplot as plt
from random import randint

class Dice():
    def __init__(self, faces = 6):
        self.faces = faces
        self.value = None
        # Stats stuff
        self.occurrence = dict(zip(range(1, self.faces+1), [0]*self.faces))
        self.rolls = 0

    def roll(self, true_roll = True):
        self.value = randint(1, self.faces)
        self.occurrence[self.value] += int(true_roll)
        self.rolls += int(true_roll)
        return self.value

    def __call__(self):
        print(self)

    def __repr__(self):
        return "Dice: " + str(self.value)

    def __str__(self):
        return f"[{self.faces}] Face Dice\t| Total Rolls [{self.rolls}]\t| Current value "+ str(self.value)

    def plot_probabilities(self):
        fig, ax = plt.subplots()

        index = np.arange(1,self.faces+1)
        bar_width = self.faces/12

        opacity = 0.4

        rects = ax.bar(index, (self.occurrence.values()), bar_width,
                        alpha=opacity, color='red',
                        label='Occurrences')
        rect_labels = []
        for rect in rects:
            width = int(rect.get_width())
            height = int(rect.get_height())
            xloc = rect.get_x() + width/2.0
            yloc = height-int(self.rolls*1e-2)
            label = ax.text(xloc, yloc, "{:.2f}%".format(height/(self.rolls)*100), horizontalalignment='left',
                         verticalalignment='center', color='black', weight='bold', size=bar_width*16,
                         clip_on=True)
            rect_labels.append(label)
        ax.set_xlabel('Numbers')
        ax.set_ylabel('Frequency')
        ax.set_title('Occurrence of each number on the dice with percentages')
        fig.tight_layout()
        arts = {
            'fig':fig,
            'perc_labels': rect_labels
        }
        plt.show()

    def __eq__(self, other):
        return self.value == other
