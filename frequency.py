str=input("enter string")
l=list(str)
freq=[l.count(ele) for ele in l]
d=dict(zip(l,freq))
print(d)
