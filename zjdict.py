#/usr/bin/python
#coding=utf-8
import os
import pystardict
import sys
import re
import ConfigParser
class zjdictmod(object):
    def __init__(self):
        self._key = ''
        self._values = ''
        self._dicts_dir = os.path.join(os.path.dirname(__file__))
        self._dicts_dir += os.sep + 'dictionary' + os.sep
        self._dicts = list()
        self.cache = list()
    def loadCfg(self):
        cfg = ConfigParser.ConfigParser()
        try:
            cfg.read('zjdict.ini')
            path = cfg.get('newword', 'path')
            cfg.read('zjdict.ini')
            auto = cfg.get('online', 'auto').lower() == str(True).lower()
            phonetic_show = cfg.get('phonetic', 'show').lower() == str(True).lower()
        except:
            path = 'newword.txt'
            auto = True
            phonetic_show = True
        return path, auto, phonetic_show
    def appendDicts(self):
        try:
            self._dicts.append(\
                    pystardict.Dictionary(os.path.join(self._dicts_dir, \
                        'stardict-cedict-gb-2.4.2', \
                        'cedict-gb')))
            self._dicts.append(
                    pystardict.Dictionary(os.path.join(self._dicts_dir, \
                            'stardict-kdic-computer-gb-2.4.2', \
                            'kdic-computer-gb')))
            if 'linux2' != sys.platform:
                self._dicts.append(
                        pystardict.Dictionary(os.path.join(self._dicts_dir, \
                                'stardict-langdao-ce-gb-2.4.2', \
                                'langdao-ce-gb')))
                self._dicts.append(\
                        pystardict.Dictionary(os.path.join(self._dicts_dir, \
                                'stardict-langdao-ec-gb-2.4.2', \
                                'langdao-ec-gb')))
        except:
            pass
    def lsdict(self):
        pass
    def words(self):
        pass
    def translate(self,key):
        self._key, self._values = key, ''
        for d in self._dicts:
            if d.has_key(key):
                value = d.dict[key]
                self._values += value + '\n'
        return self._values
    def save(self, fname):
        if ('' != self._key) and ('' != self._values):
            f = open(fname, 'a+')
            f.write('\n')
            f.write(self._key)
            f.write('\n')
            f.write(self._values)
            f.write('\n')
            f.close()
    def search(self, grep):
        cache = list()
        for d in self._dicts:
            for key in d.keys():
                m = re.match(grep, key)
                if m is not None:
                    cache.append(str(key))
        return cache
    def value(self, v):
        self._values = v
    def show_phonetic(self):
        try:
            import phonetic_with_bing
            print '>>>[%s]' % (phonetic_with_bing.get_from_bing(self._key)['us'])
        except:
            pass
    def sound(self):
        return self.sound_with_word(self._key)
    def sound_with_word(self, source):
        import sound
        return sound.sound(source)
if '__main__' == __name__:
    pass
