import urllib
import urllib2
import re
import os
import mp3play
import socket
sound_dir = 'sound'
def download(url):
#    try:
#        import proxy
#        url = 'http://%s:%s' % (proxy.ip, proxy.port)
#        proxy = urllib2.ProxyHandler({'http:':url})
#        opener = urllib2.build_opener(proxy)
#        urllib2.install_opener(opener)
#    except ImportError, e:
#        pass
    mp3_path = os.path.join(sound_dir, w + '.mp3')
    try:
        if not os.path.isfile(mp3_path):
            conn = urllib2.urlopen(url)
            with open(os.path.join(sound_dir, w + '.mp3'), 'wb') as f:
                f.write(conn.read())
        return mp3_path
    except socket.error, e:
        if e.errno == 10054:
            return ''
        raise e
def play(f):
    clip = mp3play.load(f)
    clip.play() 
    # Let it play for up to 30 seconds, then stop it.
    import time
    time.sleep(clip.seconds())
    clip.stop()

def sound(w):
    if not os.path.exists(sound_dir):
        os.mkdir(sound_dir)
    urls = [
        'http://media.shanbay.com/audio/us/%s.mp3' % (w),
        'http://media.engkoo.com:8129/en-us/%s.mp3' % (w),
    ]
    for url in urls:
        f = download(url)
        if f != '':
            play(f)
            return


if __name__ == '__main__':
    import sys
    w = sys.argv[1].decode(sys.stdin.encoding).encode('gbk')
    urls = [
        'http://media.shanbay.com/audio/us/%s.mp3' % (w),
        'http://media.engkoo.com:8129/en-us/%s.mp3' % (w),
    ]
    for url in urls:
        f = download(url)
        if f != '':
            print url, '->', f
            play(f)
        else:
            print 'fail to download ', url
