'''
Created on Oct 28, 2015

@author: buckd
'''

import sys

# Add to these if needed
COMMON_RESISTOR_MULTIPLES = [10, 12, 15, 18, 22, 27, 33, 39, 47, 56, 68, 82]


def pick(V_cc, V_b):
    # Ratio of R1 to R2 is calcualted here
    ratio = (V_cc - V_b) / V_b
    
    print "\n=> Ratio of R1 to R2:  " + str(ratio)
    
    best_r1 = None
    best_r2 = None
    
    # Really high to start
    best = 999999999
    
    # Base the magnitude off of the ratio of R1 to R2
    magnitude = 1;
    
    # Lazy...
    if ratio > 1:
        magnitude = 1
    if ratio > 10:
        magnitude = 10
    if ratio > 100:
        magnitude = 100
    if ratio > 1000:
        magnitude = 1000
    
    # Now loop through all combinations to try and get close to the ratio
    for r1 in COMMON_RESISTOR_MULTIPLES:
        r1 = r1 * magnitude
        
        for r2 in COMMON_RESISTOR_MULTIPLES:
            thisRatio = r1 / float(r2)
            
            difference = abs(ratio - thisRatio)
            
            # Test against previous best match
            if difference < best:
                best = difference
                
                # Save our better match
                best_r1 = r1
                best_r2 = r2
    
    print "\n=> Best match:"
    print "R1:     " + str(best_r1)
    print "R2:     " + str(best_r2)
    
    newratio =  best_r1 / float(best_r2)
    new_V_b  = V_cc * best_r2 / (best_r1 + best_r2)

    print "Ratio:  " + str(newratio)
    print "V_b:    " + str(new_V_b)
    
    
    # Reset
    best = 999999999
    best_r1_1 = None
    best_r1_2 = None
    best_r2   = None
        
    # Loop through everything again, but add an option to check the addition of
    # two resistors in series for the numerator
    for r1_1 in COMMON_RESISTOR_MULTIPLES:
        r1_1 = r1_1 * magnitude
        
        for r1_2 in COMMON_RESISTOR_MULTIPLES:
            r1_2 = r1_2 * magnitude
            
            for r2 in COMMON_RESISTOR_MULTIPLES:
                thisRatio = (r1_1 + r1_2) / float(r2)
                
                difference = abs(ratio - thisRatio)
                
                # Test against previous best match
                if difference < best:
                    best = difference
                    
                    # Save our better match
                    best_r1_1 = r1_1
                    best_r1_2 = r1_2
                    best_r2   = r2

    print "\n=> If you're willing to use 2 resistors for R1:"
    print "R1:     " + str(best_r1_1) + " + " + str(best_r1_2)
    print "R2:     " + str(best_r2)

    best_r1 = best_r1_1 + best_r1_2
    newratio =  best_r1 / float(best_r2)
    new_V_b  = V_cc * best_r2 / (best_r1 + best_r2)

    print "Ratio:  " + str( newratio )
    print "V_b:    " + str( new_V_b )
    
    pass


def main():
    # You can hard code these if wanted
    V_cc = None
    V_b  = None
    
    
    # Test for parameters
    if not (V_cc and V_b) and len(sys.argv) < 3:
        print "BJT Base biasing"
        print "Usage: python " + sys.argv[0] + " [V_cc] [V_b]"
        print
        print "Example:"
        print "  " + sys.argv[0] + " 9 1.083"
        sys.exit(2)
    
    
    # Grab 
    if not (V_cc and V_b):
        V_cc = float(sys.argv[1])
        V_b = float(sys.argv[2])
        
    
    pick(float(V_cc), float(V_b))
    
    print "\nNOTE: These are multiples.  Scale these if needed."
    
    pass



if __name__ == '__main__':
    main()
    pass

