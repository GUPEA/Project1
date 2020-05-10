from Cell import Cell
# Semi-Hiddent Test that Cell has the correct fields (and only the correct fields) (1 point)
c = Cell(5,5,"Blue",2)

from hashlib import sha256
hash_fun = lambda x : sha256(str(x).encode()).hexdigest()
print(sorted(vars(c).keys()))
print (hash_fun(sorted(vars(c).keys())))
#assert(hash_fun(sorted(vars(c).keys())) == '67f748721c49d3634ffb4f1735cd5341049d0c744277b4ab8e2fbeec74479e48')