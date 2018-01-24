def array (nama) :
    perempuan="IAUETLiauetl"
    laki="BDObdo"
    jumlahperempuan=""
    jumlahlaki=""

    for karakter in nama:
        if karakter in perempuan:
            jumlahperempuan+=karakter
        if karakter in laki:
            jumlahlaki+=karakter

    print ("Jenis Kelamin : ")
    if len (jumlahperempuan) > len (jumlahlaki):
       print ('Perempuan')
    if len (jumlahperempuan) == len (jumlahlaki):
        print ('Tidak Diketahui')
    if len(jumlahperempuan) < len(jumlahlaki):
        print ('Laki-Laki')

    print ("")
    print ("Huruf Perempuan :")
    print (jumlahperempuan)
    print (len (jumlahperempuan))
    print ("Huruf Laki-Laki :")
    print (jumlahlaki)
    print (len (jumlahlaki))

print ('\nMenentukan Jenis Kelamin\n')
nama=input("Masukkan nama :")
array(nama)
