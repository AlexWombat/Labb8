# Syntaxkontroll
from LinkedQfile import LinkedQ
import string


class Molekylfel(Exception):
    pass


def readMolekyl(q):
    readAtom(q)
    if q.peek() == '.':
        q.dequeue()
    elif q.peek().isalpha():
        readMolekyl(q)
    else:
        readNumber(q)
        if q.peek() == '.':
            q.dequeue()
        else:
            readMolekyl(q)


def readAtom(q):
    readLETTER(q)
    if q.peek().islower():
        readLetter(q)


def readLETTER(q):
    storboks = q.dequeue()
    #print(storboks)
    sbokstäver = string.ascii_uppercase
    for i in sbokstäver:
        if storboks == i:
            return
    raise Molekylfel('Saknad stor bokstav')


def readLetter(q):
    litenboks = q.dequeue()
    #print(litenboks)
    lbokstäver = string.ascii_lowercase
    for i in lbokstäver:
        if litenboks == i:
            return
    raise Molekylfel('Fel liten bokstav: ' + i)


def readNumber(q):
    nummer = q.dequeue()
    #print(nummer)
    if int(nummer) > 1:
        return
    raise Molekylfel('För litet tal vid radslutet')

def storeMolekyl(molekyl):
    q = LinkedQ()
    molekyl = molekyl.split()
    for tecken in molekyl:
        q.enqueue(tecken)
    q.enqueue('.')
    return q


def kollaMolekyl(molekyl):
    q = storeMolekyl(molekyl)
    try:
        readMolekyl(q)
        return 'Följer syntaxen!'
    except Molekylfel as fel:
        return str(fel)


def main():
    test = 'a a'
    resultat = kollaMolekyl(test)
    print(resultat)


main()
