# -*- coding: utf-8 -*-
"""
Created on Wed Nov 01 22:45:52 2017

@author: Andira
"""
import tellurium as te
from tellurium import ParameterScan as ps
import roadrunner
import pylab
import numpy as np
import matplotlib.pyplot as plt

r = te.loada('''
    model pathway()

  $X -> P; 0.84*ln(2)*C/5.5 - c*P
  $X -> A; (a-b)*A + 3*(P/(d+P)) + 2*(P/(e+P))

A=0;
P=0.001;
C=0.0001;
a=1;
b=1.1;
c=0.5;
d=30;
e=20;
end
''')
   

res = r.simulate(0, 50, 1000, ['TIME','A','P'])
r.plot()

print r.getSteadyStateValues() 
print r.getFullEigenValues()

p = ps(r)

p.endTime = 100
p.numberOfPoints = 500
p.polyNumber = 5
p.startValue = 0.00005
p.endValue = 0.00025
p.value = 'C'
p.selection = ['A']

p.plotGraduatedArray()
