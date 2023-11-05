import math

def birinciTerimBul():
    kesmeHatasi=gercekDeger-birinciTerim
    return kesmeHatasi

def ikinciTerimBul():
    kesmeHatasi=gercekDeger-ikinciTerim
    return kesmeHatasi

gercekDeger=math.cos(math.radians(36))

birinciTerim=math.cos(math.radians(0))

ikinciTerim=math.cos(math.radians(0))+(-math.sin(math.radians(0)))*(math.pi/5-0) +((-math.cos(math.radians(0)))*(math.pi/5*math.pi/5))/2

birinciKesmeHatasi=birinciTerimBul()
print("Taylor serisini bir kere açtığımızda = Gerçek değer = ",gercekDeger," Hesaplanan değer = ",birinciTerim," Kesme hatası = ",birinciKesmeHatasi)

ikinciKesmeHatasi=ikinciTerimBul()
print("Taylor serisini iki kere açtığımızda = Gerçek değer = ",gercekDeger," Hesaplanan değer = ",ikinciTerim," Kesme hatası = ",ikinciKesmeHatasi)