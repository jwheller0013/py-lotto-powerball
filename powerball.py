# lotto picker by manny juan  (juanm@wellsfargo.com or manny@bdt.com)
import random
from random import randint
def pick_lotto():
    maxm = 69
    maxj = 5
    m = maxm

    r = list(range(m+1))
    v = []
    for j in range(maxj):
        # get ith number from r...
        i = randint(1, m)
        n = r[i]
        # remove it from r...
        r.pop(i)
        m = m - 1
        # and append to the result
        v.append(n)
    #the above code covers the first 5 for the tuple pair
    pballmax= 26
    p = (random.randint(1, pballmax))
    x = []
    x.append(p)
    return tuple(v) + tuple(x)

def run():
    done = 0
    while not done:
        try:
            x = input('\npress Enter for Lotto picks (Q to quit). ')
        except EOFError:
            x = 'q'
        if x and (x[0] == 'q' or x[0] == 'Q'):
            done = 1
            print('done')
        else:
            print(pick_lotto())

# immediate-mode commands, for drag-and-drop or execfile() execution
if __name__ == '__main__':
	run()
else:
	print("Module lotto imported.")
	print("To run, type: lotto.run()")
	print("To reload after changes to the source, type: reload(lotto)")
# end of lotto.py