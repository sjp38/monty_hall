#!/bin/env python

import sys
import random

def do_game(do_change):
    "Returns true for win, false for lose"
    answer = random.randint(0, 2)
    selection = random.randint(0, 2)
    if selection == answer:
        return True
    if do_change:
        candidate = [0, 1, 2]
        candidate.remove(selection)
        selection = candidate[random.randint(0,1)]
    if selection == answer:
        return True
    return False

if __name__ == "__main__":
    nr_games = int(sys.argv[1])
    print("do %d games" % nr_games)

    for change in [True, False]:
        game = 0
        nr_win = 0
        nr_lose = 0
        random.seed(42)

        while True:
            game += 1
            if game > nr_games:
                break
            if do_game(change):
                nr_win += 1
            else:
                nr_lose += 1
        print "strategy: %s:\t%5d wins, %5d lose (%.4f win probability)" % (
                "change" if change else "no_change", nr_win, nr_lose,
                float(nr_win) / nr_games)
