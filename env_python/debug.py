data = {'Kezv': -705, 'Bmbyi': -705, 'Tltreyen': -341, 'Zhytscewa':
        101, 'Dnshgwpfslnwjgpbpta': -705, 'Qizqcwcaj': -453, 'Kiiu': -705, 'Pkxdtkzcqcatlevppgfh': 310, 'Ijfpauymwj': -705, 'Oftafgnkiskx': 279, 'Uzevuodgdgqfdzvrboxo': 680, 'Slwp': 74, 'Kosslqbfvvicxvoeu': -705, 'Rinfzxgetxt': 241, 'Gitrjdleypotimvwoxn': -705, 'Saqswmqucjvuzcetv': -28, 'Ngxcienkrbjuwcmll': -281, 'Ybhzfywzuszpacxukb': 94, 'Eetdnxqqrnnngqitrt': -705, 'Oxbbntnumomgzlijhafv': -381, 'Uepbcsjbpcydehbr': 272, 'En': -705, 'Gbvlxcqkcoda': -705, 'Rsngzof': -52, 'Gtuifljazbcn': -705, 'Pmiidad': -220, 'Itkziu': -705, 'Esjucfgp': -705, 'Nbkpxnjxqpijmksnj': -70, 'Onjcwtf': 79, 'Lcwhsj': -705, 'Jiqebgxhdtqxw': -705, 'Awlwmjakzvhicdmy': -705, 'Dizsbibrrvubf': -705, 'Uoqdskgsndf': 323, 'Klufjljokynppxbkyisx': -705, 'Dkxkbzrcjkg': -705, 'Raetgl': 71, 'Njqflodzvnee': -359, 'Irhlxpeugvsb': -705, 'Bb': -705, 'Emybevnqutdlyqpogemu': -705, 'Mlxuyeidfzvefwwc': -500, 'Xxkvmudthutq': 135, 'Huzkbhb': -705, 'Stmeki': -540, 'Qbjphsjkmdka': -31, 'Ymipuodjrnfjzhcmjdbz': -347, 'Ogbqfvbrnhhsbepdykky': -7,
        'Pqgllwxrydxerns': -79, 'Znyzrvhxetfzzawpky': -481,
        'Ceryppfgvhepimgrqo': -705, 'Wdrktpywoirjwfe': 24, 'Icodiqojd': -705,
        'Slrv': 317, 'Qssebslric': 116, 'Hziyuoeq': -705, 'Up': -97, 'Vfbdcfcxd': 43, 'Tssjr': 176, 'Wz': -265, 'Rtn': 183, 'Dbhjlbgvdnzu': -705, 'Xwbykstqukzajlujjule': -244, 'Wcegowqksbszlsv': 179, 'Fuigrwjchmj': -705, 'Duqpwctkvqau': -705, 'Ivooo': -705, 'Vbo': -96, 'Ahvs': -705, 'Bwtb': -705, 'Pyshchthulxarzhize': -342, 'We': 156, 'Owbizhzkbdluytbvw': -203, 'Spydzjqktyelpgmsbklv': 104, 'Hprbwdcfxiffp': -705, 'Vqakez': -88, 'Pmudzcbxzdexjuhktdt': 482, 'Ylcpesntl': -112, 'Qvmh': -37, 'Hurzhfpnubzvblfzmmbg': -705, 'Tcnhudhylq': 66, 'Nqynifowbgctqvazpkuu': 138, 'Gtnxiavevwf': -705, 'Ozvevsmwaxakrtdf': 285, 'Ejixgwveticat': -705, 'Lynewn': -705, 'Weaolsrxqcoxwntb': 33, 'Sfkgofekpiuw': 403, 'Tjrwcrsekwatroturzpn': -500, 'Kdjvnzqtjykiymkmd': -705, 'Wyimdlsgkon': -288, 'Pmymhulykriyhdma': -106, 'Ravzynyhsxrgdiqpn': -582, 'Wtqxvfpxcwitljyehld': -247, 'Aqizlkgvhlhwsg': -705, 'Zpklbimtofjpxqkdq': 31623, 'Frkqpiwowgyp': -705, 'Btntzkx': -705, 'Jaklq': -705}
vas = data.values()
print(max(vas))
print(min(vas))
print(list(filter(lambda x: x < 0, vas)))
print(max(list(filter(lambda x: x < 0, vas))))
d = max(list(filter(lambda x: x < 0, vas)))
for key in data:
    if d == data[key]:
        print(key)
