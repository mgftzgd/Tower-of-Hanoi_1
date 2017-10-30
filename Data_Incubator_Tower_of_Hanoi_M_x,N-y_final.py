# -*- coding: utf-8 -*-
"""
Created on Thu Jul 20 11:49:38 2017

@author: Michael Fitzgerald for Data Incubato Challenge
"""

def tower(n, from_, inter_, to_, count, d):    
    if n > 0:
        #1)	Move a tower of height n-1 from original pole to target pole, using the intermediate pole        
        tower(n - 1, from_, inter_, to_, count, d)
        
        #2)	Move the remaining disk from original pole to intermediate pole
        if from_[0]:
            # disk moved from original peg to target peg
            if (pegs%2 == 0) and (distance == 0) and (inter_[0].count(0) == 0):
                flag_ = True
            else:
                flag_ = False
                
            if flag_ == False:
                disk = disk_move(from_[0], inter_[0])
                center_of_mass_2(disk, from_[1], inter_[1], from_, inter_, to_ ,count, d)
                
        #3)	Move a tower of height n-1 from target pole to original pole, using the intermediate pole
        tower(n - 1, to_, inter_, from_, count, d)

        #4)	Move the remaining disk from intermediate pole to final pole
        if inter_[0]:
            # disk moved from intermediate peg to target peg
            if (pegs%2 == 0) and (distance == 0) and (inter_[0].count(0) == 0):
                flag_ = True
            else:
                flag_ = False

            if flag_ == False:
                disk = disk_move(inter_[0], to_[0])
                center_of_mass_2(disk, inter_[1], to_[1], from_, inter_, to_, count, d)

        #5)	Move a tower of height n-1 from original pole to target pole, using the intermediate pole
        tower(n - 1, from_, inter_, to_, count, d)

###################################################################################################

def disk_move(a,z):
    disk = a.pop()
    z.append(disk)
    return disk
    
###################################################################################################

def remove_value_from_list(list_, val):
    return [value for value in list_ if value != val]

###################################################################################################

from math import sqrt 

def s_dev(n): 

    """Calculates the standard dev. of the center of mass.""" 

    how_many = len(n) 
    mean = float(sum(n)*1. / how_many)
    diffs = [x - mean for x in n] 
    sq_diff = [d ** 2 for d in diffs] 
    ssd = sum(sq_diff) 
     
    var = ssd / how_many
    sd = float(sqrt(var)) 

    print('The standard deviation of the Mean Center of Mass is %0.10f.' % sd) 

###################################################################################################

def center_of_mass_2(disk, x, y, from_, inter_, to_, count, d):
      
    print 'Now moving %d from %d position to %d position' % (disk, x+d, y+d)
    
    if len(moves) == 0:
        count +=1
    else:
        count = max(moves) + 1
    moves.append(count)
    print '%d move(s) completed' % max(moves)
    
    if x > y:
        f = to_[0]
        h = from_[0]
    else:
        f = from_[0]
        h = to_[0]            
    g = inter_[0]
    j = to_[0]
        
    # Determine mass statisics after move, replace Nans with '0s'
    if numb-len(f) > 0:
        for i in range(numb-len(f)):
            f.insert(0,0)
    if numb-len(f) < 0:
        for i in range(abs(numb-len(f))):
            f.remove(0)
   
    if numb-len(g) > 0:
        for i in range(numb-len(g)):
            g.insert(0,0)
    if numb-len(g) < 0:
        for i in range(abs(numb-len(g))):
            g.remove(0)
       
    if numb-len(h) > 0:
        for i in range(numb-len(h)):
            h.insert(0,0)
    if numb-len(h) < 0:
        for i in range(abs(numb-len(h))):
            h.remove(0)
         
    print 'The mass for source location is %d' % sum(f)
    print 'The mass for intermediate location is %d' % sum(g)
    print 'The mass for target location is %d' % sum(h)
    
    Current_C_O_M = float(sum(f)*(0+d) + sum(g)*(1+d) + sum(h)*(2+d))/(sum(f) + sum(g) + sum(h))

    print 'The center of mass from original location is now %0.10f units' % Current_C_O_M
    Mean_C_O_M.append(Current_C_O_M)
    print """The mean center of mass from original location is now %0.10f units""" % float(sum(Mean_C_O_M)/len(Mean_C_O_M))

    s_dev(Mean_C_O_M)

    f = remove_value_from_list(f,0)
    f = f[::-1]

    g = remove_value_from_list(g,0)
    g = g[::-1]

    h = remove_value_from_list(h,0)
    h = h[::-1]
    
    j = remove_value_from_list(j,0)
    j = j[::-1]
   
    print 'The pegs are now: Peg %d %s  Peg %d %s  Peg %d %s\n' % (d, f, d+1, g, d+2, h)
     
###################################################################################################

def set_up_pegs():
    
    x = []
    for i in range (1,numb+1):  # build stack in starting position
        x.append(i)
    
    a = (x[::-1], 0)  # tuple for position 0 + reverse order from above
    b = ([], 1)   # tuple for position 1
    c = ([], 2)   # tuple for position 2
    
     
    # fill the empty arrays with requisite number of '0's
    if numb-len(b[0]) > 0:
        for i in range(numb-len(b[0])):
            b[0].insert(0,0)   
    if numb-len(c[0]) > 0:
        for i in range(numb-len(c[0])):
            c[0].insert(0,0)
    
    return a,b,c,x

###################################################################################################

# Take input from console
try:
    numb = int(raw_input('How many disks in the stack?: '))
    pegs = int(raw_input('How many stacks?: '))
except ValueError:
    print 'Not a Number'

# set variables
Mean_C_O_M = []   # array for COMs
c = 0  # count moves; initially 0
moves=[]   # tracks moves
zero = 0
src, i_1, tgt, x = set_up_pegs()

print '''
The original setup in Position 0 is as follows: 
        %d disks %s with largest number %d on bottom of peg
''' % (len(x), x, max(x))

# calculate how many times to run loop below
if pegs%2 == 0:
    how_many = pegs/2
else:
    how_many = (pegs-1)/2

distance = 0
for i in range (1, how_many+1):
    tower( len(src[0]), src, i_1, tgt, c, distance)
    if (i == 1) and (pegs%2 == 0):
        distance = distance + 1
        
    else: 
        distance = distance + 2
    src, i_1, tgt, x = set_up_pegs()
    
###################################################################################################
