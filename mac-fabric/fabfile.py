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
        'yepyep': 'https://www.youtube.com/watch?v=vh3tuL_DVsE'}

def yepyep():
    run('open %s' % (youtube_urls['yepyep']))

def pizza():
    run('open %s' % (youtube_urls['pizza']))

def manamana():
    run('open %s' % (youtube_urls['manamana']))

def lobster():
    run('open %s' % (youtube_urls['lobster']))

def happy():
    run('open %s' % (youtube_urls['happy']))

def random():
    x = _random.choice(youtube_urls.values())
    run('open %s' % (x))

def say(say_this=None):
    if say_this is not None:
        run('say %s' % (say_this))

def vol(level=None):
    """ vol - get current volume / vol:## - set current volume """
    if level is None:
        run("osascript -e 'output volume of (get volume settings)'")
        return

    #set the volume
    try:
        volume = int(level)
    except ValueError:
        print 'Invalid volume value. Valid range: 0-100'
        return
    run("osascript -e 'set volume output volume %s'" % (volume))

def snap():
    tmpfile = '/tmp/mac-mini %s.jpg' % (datetime.now())
    run('imagesnap %s' % (tmpfile.replace(' ','\ ')))
    files = get(tmpfile, local_path='.')
    if files.succeeded:
        run('rm %s' % (tmpfile.replace(' ', '\ ')))
