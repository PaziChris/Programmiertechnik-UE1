#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 21 16:02:19 2020

@author: nother
"""
import numpy as np

module = [2,3,5,10, 15, 20, 25, 30]


def designe_prothese(restlaenge,aktuell = []):
    elemente = None
    if restlaenge < 0:
        return None
    if restlaenge == 0:
        return aktuell
    for modul in module:
        benoetigt = designe_prothese(restlaenge - modul,aktuell + [modul])
        if benoetigt is not None:
            if elemente is None or len(elemente) > len(benoetigt):
                elemente = benoetigt
    return elemente

def designe_prothese_besser(restlaenge,aktuell = [],totest=module):
    elemente = None
    if restlaenge < 0:
        return None
    if restlaenge == 0:
        return aktuell
    for modulindex,modul in enumerate(reversed(totest)): # module[::-1]
        benoetigt = designe_prothese_besser(restlaenge - modul,aktuell + [modul],totest=totest[:len(totest)-modulindex])
        if benoetigt is not None:
            return benoetigt
    return None

if __name__ == '__main__':
    print(designe_prothese_besser(87))
