from flask import Flask, request, render_template

import numpy as np

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def sandpile():

    maxPile = 4

    row = request.form['row']
    col = request.form['col']
    pile = request.form['pile']

    sandPile = np.zeros([int(row),int(col)], dtype=int)

    i = (int(row)-1)/2
    j = (int(col)-1)/2
    sandPile[int(i)][int(j)] = pile #Insert first pile

    temp = sandPile

    powerOn = True

    # Matrix creation
    # gridTotal = temp
    while powerOn:

        # Print Matrix
        # print(temp)

        # When value in matrix >= maxPile, that block value got subtract with maxPile
        temp = np.where(temp>=maxPile, temp-maxPile, temp)

        # Topple sandpile
        mask = (sandPile >= maxPile)

        # print(mask)

        temp[:, :-1] += mask[:, 1:] # topple left
        temp[:, 1:] += mask[:, :-1] # topple right
        temp[:-1, :] += mask[1:, :] # topple up
        temp[1:, :] += mask[:-1, :] # topple down

        # Check if there's no more to topple
        COMPARISON = sandPile == temp
        CHECK_EQUAL = COMPARISON.all()

        # gridTotal = np.insert(gridTotal, temp, axis=0)
        
        sandPile = temp

        
        if CHECK_EQUAL == powerOn:
            powerOn = False
            # print("Shutting Down...")

    # data = np.load('arr.npz')
    return render_template('sandpile.html', row=row, col=col, pile=pile, grid=temp)
    # return str(temp)

if __name__ == "__main__":
    app.run()