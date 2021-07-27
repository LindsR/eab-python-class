# -*- coding: utf-8 -*-
"""
Created on Mon Jul 26 09:56:08 2021

@author: CPaulson
"""
## import packages 
import numpy

## base set first interaction number
no_interact = input("Number of impact interactions (q to quit)? ")

## establish quitting while loop
while no_interact != "q": 
    
    ## establish while loop that will prevent error on invalid interaction 
    ## number
    while True: 
        try:
            ## convert input to integer
            no_interact = int(no_interact)
        
            print("Number of interactions: " + str(no_interact))
            
            ## if else loop to determine renewal chance
            if no_interact == 0:
                renew_chance = 0.30
            elif no_interact == 1 or no_interact == 2:
                renew_chance = 0.50 
            elif no_interact == 3 or no_interact == 4:
                renew_chance = 0.70 
            elif no_interact >= 5:
                renew_chance = 0.80
        
            print("Chance of renewal: " + str(renew_chance))
            
            ## set renewals and drops back to 0
            renewals = 0
            drops = 0
            
            ## run for loop to randomly determine renewals and drops based off
            ## renewal chance from above 
            for i in range(no_interact):
                renewal_test = numpy.random.choice(numpy.arange(0, 2), 
                                p=[1 - renew_chance, renew_chance])
            
                if renewal_test == 0:
                    drops += 1
                elif renewal_test == 1: 
                    renewals += 1
        
            print("Number of Drops: " + str(drops))
            print("Number of Renewals: " + str(renewals))
            
            ## setting next loop's number of interactions
            no_interact = input("Number of impact interactions (q to quit)? ")

            break
        
        except ValueError:
            print("Input a valid number.")
            
            ## setting next loop's number of interactions
            no_interact = input("Number of impact interactions (q to quit)? ")
            
            break

print("Quitting.")


