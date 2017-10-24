s = float(input('What size would you like?'))
text = input('What would you like to write?')

import char

char.setup()

charLink = {'a': 'char.a2(s)', 'b': 'char.b2(s)', 'c': 'char.c1(s)', 'd': 'char.d1(s)', 'e': 'char.e2(s)',
            'f': 'char.f2(s)', 'g': 'char.g1(s)', 'h': 'char.h1(s)', 'i': 'char.i1(s)', 'j': 'char.j1(s)',
            'k': 'char.k1(s)', 'l': 'char.l1(s)', 'm': 'char.m2(s)', 'n': 'char.n1(s)', 'o': 'char.o1(s)',
            'p': 'char.p1(s)', 'q': 'char.q1(s)', 'r': 'char.r1(s)', 's': 'char.s1(s)', 't': 'char.t1(s)',
            'u': 'char.u1(s)', 'v': 'char.v1(s)', 'w': 'char.w2(s)', 'x': 'char.x1(s)', 'y': 'char.y2(s)',
            'z': 'char.z1(s)', ' ': 'char.space(s)', '.': 'char.period(s)', ',': 'char.comma(s)',
            '!': 'char.exclamation(s)', '?': 'char.interrogation(s)', '<': 'char.less(s)', '>': 'char.greater(s)',
            '1': 'char.one(s)', '2': 'char.two(s)', '3': 'char.three(s)', '4': 'char.four(s)', '5': 'char.five(s)',
            '6': 'char.six(s)', '7': 'char.seven(s)', '8': 'char.eight(s)', '9': 'char.nine(s)', '0': 'char.o1(s)',
            '+': 'char.plus(s)', '-': 'char.minus(s)', '*': 'char.times(s)', '/': 'char.over(s)',
            '\'': 'char.apostrophe(s)'}

for i in range(len(text)):
    exec(charLink[text[i]])

char.loop()
