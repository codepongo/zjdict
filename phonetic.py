tbl = {
    '\xd3\x99':'E',
    '\xca\x8a':'U',
    '\xc9\xaa':'I',
    '\xc3\xa6':'Q',
    '\xc9\x91':'A',
    '\xc9\x9c':'C',
    '\xc9\x94':'C',
    '\xca\x8c':'V',
    '\xce\xb8':'T',
    '\xc5\x8b':'N',
    '\xc3\xb0':'D',
    '\xca\x83':'S',
    '\xca\x92':'Z',
    '\xc9\xa1':'g',
    '\xcb\x88':"`",
    '\xcb\x8c':',',
    '\xc9\x9b':'e',
    '\xc9\x92':'o',
}

def phonetic_readability(s, tbl):
    for k, v in tbl.items():
        s = s.replace(k, v)
    return s






