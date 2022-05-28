i=0
coll1 = 0
coll2 = 0
coll3 = 0
while i<6:
    coll = int(input("Cuantos colillas reciclo: "))
    i=i+1   
    if coll <= 100:
            coll1 = coll1 +1
    elif coll < 100 and coll <= 200:
            coll2 = coll2 +1
    else :
            coll3 = coll3 +1

g1 = coll1*100//i
g2 = coll2*100//i
g3 = coll3*100//i

print(f"menos de 100 personas : {g1} %")
print(f"entre 100 y 200 personas: {g2} %")
print(f"mas de 200 personas: {g3} %")
