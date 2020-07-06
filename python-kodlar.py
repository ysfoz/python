# bu hesap makinasi programi- if kullanimi icin yapildi.

print("""*****************************

Hesap Makinesi Programi

Islemeler:
1-Toplama islemi

2-cikarma islemi

3-carpma islem

4-bolme islemi

*******************************

""")

x = int(input('birinci sayi'))
y = int(input('ikinci sayi'))
islem = input('islemi giriniz')
if islem == "1" :
    print(f'{x} ve {y} nin toplami {x + y} dir')
elif islem == "2" :
    print(f'{x} ve {y} nin farki {x - y} dir')
elif islem == "3" :
    print(f'{x} ve {y} nin carpimi {x * y} dir')
elif islem == "4" :
    print(f'{x} ve {y} nin bolumu {x / y} dir')
    

  #  sifre programi 

  print('$\t\t$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$\n\n\nSISTEM GIRISI----LUTFEN KULLANICI ADI VE SIFRENIZI GIRINIniz\n\n\n\t\t$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$')

x = 'yusuf'
y = 12345
ad = input('lutfen kullanici adiniz giriniz')
sifre = int(input('lutfen sifrenizi giriniz'))
if(x == ad) and (y == sifre):
    print('sisteme giris yapildi')
elif(x == ad) and (y != sifre):
    print('yanlis sifre girdiniz')
elif(x != ad) and (y == sifre):
    print('yanlis kullanici adi girdiniz')
else:
    print('yanlis kullanici adi ve sifre girdiniz')  
