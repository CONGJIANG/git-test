def dict_interdiff(d1, d2):
    # symmetric difference, keys in either d1 or d2 but not both.
    sym_diff = d1.viewkeys() ^ d2
    # intersection, keys that are common to both d1 and d2.
    intersect = d1.viewkeys() & d2
    # apply f on values of the keys that common to both dicts.
    a = {k: f(d1[k], d2[k]) for k in intersect}
    b = {k: d1[k] for k in sym_diff & d1.viewkeys()}
    # add key/value pairings from d2 using keys that appear in sym_diff 
    b.update({k: d2[k] for k in sym_diff & d2.viewkeys()})
    return a,b

def f(a,b):
    return a+b
