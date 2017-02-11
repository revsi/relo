#!/usr/bin/python3
# Research Center : LTRC, IIIT Hyderabad
__author__ = ["Akirato","revsi"]

import codecs

debug = True


def main():
    with codecs.open('input.txt', 'r', encoding='utf-8') as myfile:
        text=myfile.read()
    print "============================RELO============================"
    print "Input Story : "+text
    print "===========================Results===========================\n\n"

   


main()
