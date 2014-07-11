from fabric.api import *
from datetime import datetime
import random as _random
from time import sleep

env.use_ssh_config = True
env.hosts = ['support-mini']

youtube_urls = {'pizza': 'https://www.youtube.com/watch?v=SIt2CdbBo_w',
        'manamana': 'https://www.youtube.com/watch?v=8N_tupPBtWQ',
        'lobster': 'https://www.youtube.com/watch?v=qf_LzWQ0jpI', 
        'happy': 'https://www.youtube.com/watch?v=d-diB65scQU',
        'yepyep': 'https://www.youtube.com/watch?v=vh3tuL_DVsE',
        'systemisdown': 'https://www.youtube.com/watch?v=ILVfzx5Pe-A',
        'wompwomp': 'https://www.youtube.com/watch?v=sC75aU47GRk',
        'yaketysax': 'https://www.youtube.com/watch?v=ZnHmskwqCCQ'}

def yt(vid=None):
    if vid is None:
        vid = _random.choice(youtube_urls.keys())
    run('open %s' % (youtube_urls[vid]))

def coffee():
    run('open http://support-coffeecam.jaalam.net')

def say(say_this=None):
    if say_this is not None:
        run('say %s' % (say_this))

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

def test():
    run("stuff=`ls -alh`; echo $stuff")

def snap():
    tmpfile = '/tmp/mac-mini %s.jpg' % (datetime.now())
    run('imagesnap %s' % (tmpfile.replace(' ','\ ')))
    files = get(tmpfile, local_path='.')
    if files.succeeded:
        run('rm %s' % (tmpfile.replace(' ', '\ ')))
