def array (nama) :
    perempuan="IAUETLiauetl"
    laki="BDObdo"
    jumlahperempuan=""
    jumlahlaki=""

    for karakter in nama:
        if karakter in perempuan: #pada kode ini, akan mencari huruf perempuan pada nama yang telah diinput
            jumlahperempuan+=karakter #huruf perempuan yang terdapat pada nama, akan ditampung dalam bentuk jumlah huruf misal (iaau)
        if karakter in laki: #pada kode ini, akan mencari huruf laki-laki pada nama yang telah diinput
            jumlahlaki+=karakter #huruf laki-laki yang terdapat pada nama, akan ditampung dalam bentuk jumlah huruf misal (boob)

    print ("Jenis Kelamin : ")
    if len (jumlahperempuan) > len (jumlahlaki): #fungsi len disini adalah, menghitung jumlah huruf yang telah disimpan,
        #jadi output yang dibandingkan berupa angka, bukan huruf yang disimpan, misal (iaau berarti jika menggunakan len, menjadi 4, karena terdapat 4 huruf)
        #lalu jumlah huruf yang disimpan akan dibandingkan
       print ('Perempuan')
    if len (jumlahperempuan) == len (jumlahlaki):
        print ('Tidak Diketahui')
    if len(jumlahperempuan) < len(jumlahlaki):
        print ('Laki-Laki')

    print ("")
    print ("Huruf Perempuan :")
    print (jumlahperempuan) #kode ini akan menampilkan huruf yang disimpan
    print (len (jumlahperempuan)) #kode ini akan menampilkan jumlah huruf yang disimpan, karena menggunakan len
    print ("Huruf Laki-Laki :")
    print (jumlahlaki)
    print (len (jumlahlaki))

print ('\nMenentukan Jenis Kelamin\n')
nama=input("Masukkan nama :")
array(nama)
