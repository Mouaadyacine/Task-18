ca=input("svp entrer categorie de produit")
ht=float( input("svp enter lhors taxe de produit"))
n=int( input("svp entrer le nombre des produits"))
match ca:
    case"A":ttc=n*ht*0.07
    case"B":ttc=n*ht*0.2
    case"C":ttc=n*ht*0.25
print("TTC=",ttc)
