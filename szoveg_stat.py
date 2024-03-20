massalh = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z']
dupla_massalh = ["sz", "zs", "ty", "ly", "gy", "dz", "cs", "ny"]
maganh = ["a", "á", "e", "é", "i", "í", "o", "ó", "ö", "ő", "u", "ú", "ü", "ű"]

# alprogramok

def beolvas():
    with open("info.txt", "r", encoding="UTF-8") as fm:
        m = fm.read().strip()
    return m

def visszafele(s):
    v = ""
    i = len(s)-1
    while i >= 0:
        v+=s[i]
        i-=1
    return v

def megszamol(l):
    db = 0
    for s in l:
        db += 1
    return db

def lh_szo(l):
    e = []
    for s in l:
        if "!" in s:
            s = s.replace("!", "")
        elif "," in s:
            s = s.replace(",", "")
        e.append(s)
    
    lh=""    
    for s in e:
        if len(lh) < len(s):
            lh = s
    return lh

def kiir(hs, v, l, lh, mag, mas):
    print(f"A szöveg {hs} szóból áll.")
    print(f"A szöveg visszafelé: {v}")
    print(f"Szavak listája (split): {l}")
    print(f"A leghosszabb szó a mondatból: {lh}")
    print(f"""A teljes szövegre:
Magánhangzók száma: {sum(mag)}
Mássalhangzók száma: {sum(mas)}""")
    print("Egyes szavakra:")
    for i in range(len(l)):
        print(f"{i+1}. szó: magánhangzó: {mag[i]} db; mássalhangzó: {mas[i]} db")

def betu_csop_szavak(l):
    mag_lista = []
    mas_lista = []
    for s in l:
        mag = 0
        mas = 0
        i = 0
        while i < len(s):
            if s[i].lower() in maganh:
                mag += 1
            elif s[i].lower() in massalh:
                if i+1 < len(s) and (s[i:i+2].lower() in dupla_massalh):
                    mas += 1
                    i+=1
                else:
                    mas += 1
            i+=1
        mag_lista.append(mag)
        mas_lista.append(mas)
    return mag_lista, mas_lista

# főprogram
# input
mondat = beolvas()
# számítás
szavak = mondat.split(" ")
szavak_szama = megszamol(szavak)
leghosszabb_szo = lh_szo(szavak)
mondat_visszafele = visszafele(mondat)
maganh_szavankent, massalh_szavankent = betu_csop_szavak(szavak)
# output
kiir(szavak_szama, mondat_visszafele, szavak, leghosszabb_szo, maganh_szavankent, massalh_szavankent)