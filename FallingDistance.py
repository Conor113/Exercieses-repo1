
G=9.8
def falling_distance(t):
    formula_distance=1/2*G*t**2
    return formula_distance


def main ():
    for t in range(1, 11):
        print (t,"Distance =",(format(falling_distance(t),'.1f')))

main()