from fabric.api import *
from datetime import datetime
import urllib
import requests
import random as _random
import time

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
        'limit': 'https://www.youtube.com/watch?v=DZz3y6r-5H8',
        'jurrbs': 'https://www.youtube.com/watch?v=rHfQQY2WqCQ',
        'funkoverload': 'https://www.youtube.com/watch?v=Wga5A6R9BJg',
        'christmastree': 'https://www.youtube.com/watch?v=Sy1Qlxgo2ek',
        'batman': 'https://www.youtube.com/watch?v=VSaDPc1Cs5U',
        'montage':'https://www.youtube.com/watch?v=pFrMLRQIT_k'}

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

def spotify(cmd=None):
    """ spotify:(track, skip, play, stop, status) """
    #http://www.instructables.com/id/RFID-Controls-for-Spotify-on-OSX-using-hacked-Mir/step3/Spotify-osascript-commands/
    cmds = {'track': 'name of current track',\
            'skip': 'next track',\
            'play': 'play',\
            'stop': 'pause',\
            'status' : 'player state'}

    if cmd is None:
        cmd = 'track'
    elif cmd == 'list':
        print cmds.keys()
        return
    else:
        cmd = cmd.strip().lower()

    if cmd not in cmds:
        print 'Unknown command %s' % (cmd)
    else:
        run("osascript -e 'tell application \"Spotify\" to %s'" % (cmds[cmd]))

def quicktime(cmd=None):
    """ quicktime:(play, stop, pause, resume, fullscreen, quit) """
    cmds = {'play': 'play the front document',\
            'stop': 'stop the front document',\
            'pause': 'pause the front document',\
            'resume': 'play the front document',\
            'fullscreen': 'present the front document',\
            'quit': 'close the application'}

    if cmd is None:
        cmd = 'list'
    elif cmd == 'list':
        print cmds.keys()
        return
    else:
        cmd = cmd.strip().lower()

    if cmd not in cmds:
        print 'Unknown command %s' % (cmd)
    else:
        run("osascript -e 'tell application \"QuickTime Player\" to %s'" % (cmds[cmd]))


def freshpots():
    """ Dave Grohl needs a fresh fucking pot! """
    
    # Pause Spotify if it is playing and crank volume
    spotifystatus = run("osascript -e 'tell application \"Spotify\" to player state'")
    if spotifystatus == 'playing':
        run("osascript -e 'tell application \"Spotify\" to pause'")
    oldvol = run("osascript -e 'output volume of (get volume settings)'")
    run("osascript -e 'set volume output volume 75'")
    time.sleep(1)
    with cd('~/shenanigans/freshpots'):
        filename = './fp%s.mp3' % (str(_random.choice(range(1,6))))
        run('afplay %s' % (filename))
    time.sleep(10)
    
    # Reset volume and resume Spotify
    run("osascript -e 'set volume output volume %s'" % (oldvol))
    if spotifystatus == 'playing':
        run("osascript -e 'tell application \"Spotify\" to play'")

def ytlaf():
    with cd('~/shenanigans/misc'):
        run('afplay ytlaf.wav')

def fakechat():
    with cd('~/shenanigans/misc'):
        run('afplay fakechat.wav')

def shitstorm():
    with cd('~/shenanigans/misc'):
        run('afplay air.wav')

def coffee():
    """ put the coffee cam up on the TV """
    run('open http://support-coffeecam.jaalam.net')
    # run("osascript -e 'tell app \"Chrome\" to activate'")
    time.sleep(1)
    run("osascript -e 'tell app \"System Events\" to keystroke \"F\" using command down'")

def attack_map():
    """ put the Norse IP Attack Map on the TV """
    run('open http://map.ipviking.com/')
    # run("osascript -e 'tell app \"Chrome\" to activate'")
    time.sleep(1)
    run("osascript -e 'tell app \"System Events\" to keystroke \"F\" using command down'")

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

def coffeetemp():
    """ poll coffeecam for latest temp data and speak it unto the support loft
    """
    r = requests.get('http://support-coffeecam.jaalam.net/coffeepot-temperature.php')
    if r.ok:
        temp = "The coffee is currently " + r.text + " degrees celcius"
        run('say %s' % (temp))

def milktemp():
    """ poll coffeecam for latest temp data and speak it unto the support loft
    """
    r = requests.get('http://support-coffeecam.jaalam.net/milk-temperature.php')
    if r.ok:
        temp = "The temperature in the milk fridge the is currently " + r.text + " degrees celcius"
        run('say %s' % (temp))

def beertemp():
    """ poll coffeecam for latest temp data and speak it unto the support loft
    """
    r = requests.get('http://support-coffeecam.jaalam.net/beer-temperature.php')
    if r.ok:
        temp = "The temperature in the beer fridge the is currently " + r.text + " degrees celcius"
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

def clean():
    """ Clean up the accumulated crap """
    run (" ps -ef | grep -i chrome | grep -v grep | awk '{ print $2 }' | xargs -I {} kill -9 {} ")
    run (" ps -ef | grep -i safari | grep -v grep | awk '{ print $2 }' | xargs -I {} kill -9 {} ")
    run (" ps -ef | grep -i spotify | grep -v grep | awk '{ print $2 }' | xargs -I {} kill -9 {} ")
    run (" ps -ef | grep -i vlc | grep -v grep | awk '{ print $2 }' | xargs -I {} kill -9 {} ")
    run (" ps -ef | grep -i gotomeeting | grep -v grep | awk '{ print $2 }' | xargs -I {} kill -9 {} ")

def reboot():
    """ Reboots the MacMini """
    run (" sudo shutdown -r now ")

def talisker():
    """ Load the Talisker Internet Radar """
    run('open http://www.securitywizardry.com/radar.htm')
    
def map():
    """ Load Google Earth """
    run('open http://support-coffeecam/ge.html')
   
def hoopla():
    """show the hoopla dashboard for sales"""
    run('open https://tv.hoopla.net/hoopla_tv/Y72HMJpuBz3GcowcPaNm')

def clocks():
    """ Add four time zone tabs to rotation """
    run('open http://free.timeanddate.com/clock/i4afqskf/n256/fn6/fs48/fc9ff/tc000/ftb/bas4/bacfff/pa12/tt0/tw1/th1/ta1/tb4')
    run('open http://free.timeanddate.com/clock/i4afqskf/fn6/fs48/fc9ff/tc000/ftb/bas4/bacfff/pa12/tt0/tw1/th1/ta1/tb4')
    run('open http://free.timeanddate.com/clock/i4afqskf/n43/fn6/fs48/fc9ff/tc000/ftb/bas4/bacfff/pa12/tt0/tw1/th1/ta1/tb4')
    run('open http://free.timeanddate.com/clock/i4afqskf/n240/fn6/fs48/fc9ff/tc000/ftb/bas4/bacfff/pa12/tt0/tw1/th1/ta1/tb4')

def chrome(cmd='list'):
    """ chrome:(presenter, fullscreen, zoomin, zoomout, closetab, nexttab, prevtab, reload) """
    cmds = {'presenter': 'tell app "System Events" to keystroke "F" using command down',\
            'fullscreen': 'tell app "System Events" to keystroke "f" using command down control down',\
            'zoomin': 'tell app "System Events" to keystroke "+" using command down',\
            'zoomout': 'tell app "System Events" to keystroke "-" using command down',\
            'closetab' : 'tell app "Google Chrome" to close active tab of window 1',\
            'nexttab' : 'tell app "System Events" to key code 48 using control down',\
            'reload' : 'tell app "Google Chrome" to reload active tab of window 1'}

    if cmd == 'list':
        print cmds.keys()
        return
    else:
        cmd = cmd.strip()
        
	#Need to hide warnings because Activating chrome returns a non-zero
  	with settings(
        hide('warnings', 'running', 'stdout', 'stderr'),
        warn_only=True
       	): 
        		
    		if cmd not in cmds:
        		print 'Unknown command %s' % (cmd)
    		else:
        		if "System Events" in (cmds[cmd]):
           			run("osascript -e 'tell application \"Chrome\" to activate'")
           			
        		run("osascript -e '%s'" % (cmds[cmd]))
