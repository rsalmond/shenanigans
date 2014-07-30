from fabric.api import *
from datetime import datetime
import urllib
import requests
import random as _random

env.use_ssh_config = True
env.hosts = ['support-mini']

youtube_urls = {'pizza': 'https://www.youtube.com/watch?v=SIt2CdbBo_w',
        'manamana': 'https://www.youtube.com/watch?v=8N_tupPBtWQ',
        'lobster': 'https://www.youtube.com/watch?v=qf_LzWQ0jpI', 
        'happy': 'https://www.youtube.com/watch?v=d-diB65scQU',
        'yepyep': 'https://www.youtube.com/watch?v=vh3tuL_DVsE',
        'systemisdown': 'https://www.youtube.com/watch?v=ILVfzx5Pe-A',
        'wompwomp': 'https://www.youtube.com/watch?v=sC75aU47GRk',
        'yaketysax': 'https://www.youtube.com/watch?v=ZnHmskwqCCQ',
        'limit': 'https://www.youtube.com/watch?v=DZz3y6r-5H8'}

def yt(vid=None):
    """ 'vid' random vid / 'vid:<name>' plays <name> / 'vid:list' list vids """
    if vid is None:
        vid = _random.choice(youtube_urls.keys())
    if vid == 'list':
        print youtube_urls.keys()
        print ' - or -'
        print 'yt:[video id]'
        return
    if vid in youtube_urls.keys():
        run('open %s' % (youtube_urls[vid]))
        return
    run('open https://www.youtube.com/watch?v=%s' % (vid))


def freshpots():
    """ Dave Grohl needs a fresh fucking pot! """
    with cd('~/shenanigans/freshpots'):
        filename = './fp%s.mp3' % (str(_random.choice(range(1,6))))
        run('afplay %s' % (filename))

def coffee():
    """ put the coffee cam up on the TV """
    run('open http://support-coffeecam.jaalam.net')

def say(say_this=None):
    """ say:"any damn thing you please" """
    if say_this is not None:
        run('say %s' % (say_this))

def temperature():
    """ poll coffeecam for latest temp data and speak it unto the support loft
    """
    r = requests.get('http://support-coffeecam.jaalam.net/kitchen-temperature.php')
    if r.ok:
        temp = "The kitchen is currently " + r.text + " degrees celcius"
        run('say %s' % (temp))

def vol(level=None, delta=None):
    """ 'vol' get vol / 'vol:##' or vol:'-##' or '+##' set vol """
    if level is None:
        run("osascript -e 'output volume of (get volume settings)'")
        return

    #set the volume
    try:
        newvol = int(level)
    except ValueError:
        print 'Invalid volume value. Valid range: 0-100'
        return

    if level[:1] in ('-','+'):
        delta = True

    if delta:
        oldvol = run("osascript -e 'output volume of (get volume settings)'")
        run("osascript -e 'set volume output volume %s'" % (int(oldvol) +
            newvol))
    else:
        run("osascript -e 'set volume output volume %s'" % (newvol))

def snap():
    """ snap a pic from the webcam and throw it in hipchat """
    tmpfile = 'mac-mini %s.jpg' % (datetime.now())
    run('imagesnap ~/Sites/snaps/%s' % (tmpfile.replace(' ', '\ ')))
    img = '<img src = "http://support-mini.jaalam.net/~support/snaps/%s" width=320 height=240>' % (tmpfile)
    with cd('~/shenanigans/'):
        run('./hipchat.sh %s' % (urllib.quote_plus(img)))

def clean():
    """ Clean up the accumulated crap """
    run (" ps -ef | grep -i chrome | grep -v grep | awk '{ print $2 }' | xargs -I {} kill -9 {} ")
    run (" ps -ef | grep -i safari | grep -v grep | awk '{ print $2 }' | xargs -I {} kill -9 {} ")
    run (" ps -ef | grep -i spotify | grep -v grep | awk '{ print $2 }' | xargs -I {} kill -9 {} ")

