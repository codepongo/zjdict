import urllib
import urllib2
import re
import os
import mp3play
sound_dir = 'sound'
def soundByShanbay(w):
    if not os.path.exists(sound_dir):
        os.mkdir(sound_dir)
    mp3_path = os.path.join(sound_dir, w + '.mp3')
    if not os.path.isfile(mp3_path):
        url = 'http://media.shanbay.com/audio/us/%s.mp3' % (w)
        conn = urllib2.urlopen(url)
        with open(os.path.join(sound_dir, w + '.mp3'), 'wb') as f:
            f.write(conn.read())
    clip = mp3play.load(mp3_path)
    clip.play() 
    # Let it play for up to 30 seconds, then stop it.
    import time
    time.sleep(clip.seconds())
    clip.stop()

if __name__ == '__main__':
    import sys
    w = sys.argv[1].decode(sys.stdin.encoding).encode('gbk')
    soundByShanbay(w)
        
