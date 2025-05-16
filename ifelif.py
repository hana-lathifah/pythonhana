score = 75
min_criteria = 75

if score == min_criteria:
    print("anda berhasil naik level!")

if score >= min_criteria:
    print("anda berhasil naik level!")

elif score < min_criteria:
    print("anda belum berhasil naik level!")
else: 
    print("nilai anda tidak ditemukan")



    




#memberikan nilai berdasarkan skor

nilai = input("masukkan nilai")
nilai = int(nilai)

if nilai >= 85:
    print("A")
elif nilai >= 70 :
    print("B")
else :
    print("C")