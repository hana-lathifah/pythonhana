#membuatlist
names = ["Andi", "Cahyo", "Beni"]

#membuat list dengan list constructor
names = list("Andi", "Beni", "Cahyo")

#membuat list dari iterable object

name = "Andi"
Letters = list(name)

print(names[2])

names.append("Dodi")
print(names.append("Dodi"))
names[1]= "Beni Saputra"

names.remove = ("Andi")

#membuat tuple
names= ("Andi", "Beni","Cahyo")

#membuat tuple dengan tuple constructor
names = tuple((names))

#membuat tuple dari iterable object
name = "Andi"
letters = tuple(name)

names = ("Andi", "Cahyo","Beni")
print(names[1])

#konversi ke dalam list
names_list = list(names)

#lakukan manipulasi
names_list.append("Dodi")
names_list[2]= "Cahyo Saputra"  
names_list.remove("Andi")

#konversi ke dalam tuple
names= tuple(names_list)


#membuat set dengan biasa
names = {"Andi","Beni","Cahyo"}

#membuat tuple dengan set constructor 
names = set(("Andi","Beni","Cahyo"))

#membuat set dari iterable object
name= "Andi"
letters = set(names)

names = {"Andi", "Beni", "Cahyo"}
print(names)

#item dalam set tidak bisa diakses 
print(names[2]) 
#ini akan error

#menambahkan item baru
names.add("Dodi")

#menghapus item 
names.discard("aNDI")
names.remove("Ega")
#jika item tidak ada, error

#menghapus secara acak 
names.pop() 

#membuat dicitionary dengan biasa
student = {"name" : "Andi", "Address" : "jakarta"}

student = dict(  "name" : "Andi", "Address" : "jakarta )
                
