def interp(low, hi, fraction):
    return low + (hi - low) * fraction 

ln_low = 2
ln_hi = 1
ln_fraction = 4

print(interp(ln_low, ln_hi, ln_fraction))

def flipside(s):
    """ flipside(s): spiegel s!
    input s: een string
    """