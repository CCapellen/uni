#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 13 22:54:19 2016

@author: catherine
"""
import random

wetGrass = {"phi1":{"1":0.2,"0":0.8},
            "phi2":{"1":0.1,"0":0.9},
            "phi31":{"11":1,"10":0.2,"01":0, "00":0.8},
            "phi412":{"110":1,"010":0,
                      "111":1,"011":0,
                      "101":0.9,"001":0.1,
                      "100":0,"000":1}
            }
 
names_map = {"R":"1","S":"2","J":"3","T":"4"}            
wetGrassSchedule = ["phi1","phi2","phi31","phi412"]
wetGrassDependencies = {"phi1":0,"phi2":0,"phi31":[1],"phi412":[1,2]}
wetGrassEvidence = [3,1]

def draw_uniform_sample(variable,dependencies):
    r = random.random()
    if r <= variable["1"+dependencies]:
        return 1
    else:
        return 0
 
def draw_sample_of_all_variables(schedule,dependencies,model):
    sample = []
    for i in schedule:
        d = ""
        if dependencies[i]:
            for dep in dependencies[i]:
               d += str(sample[dep-1])  
        sample.append(draw_uniform_sample(model[i],d))
    return sample
           
def forward_sampling(model,evidence,schedule, dependencies,num_samples):
    samples = []
    counter = 0
    while len(samples)<num_samples:
        counter +=1
        s = draw_sample_of_all_variables(schedule,dependencies,model)
        if s[evidence[0]] == evidence[1]:
            samples.append(s)
    print str(counter) + " samples needed to be drawn to get " + str(num_samples)  + " examples."
    return samples
        
wetGrassSamples = forward_sampling(wetGrass,wetGrassEvidence,wetGrassSchedule,wetGrassDependencies,1000)

# task 2.2

samplesWithT1 = [s for s in wetGrassSamples if s[3]==1]
samplesWithS1givenT1 = [s for s in samplesWithT1 if s[1]==1]


print "p(S=1|T=1) = ", len(samplesWithS1givenT1)/float(len(samplesWithT1))
