#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2020.2.4post1),
    on March 04, 2021, at 22:59
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

from __future__ import absolute_import, division

from psychopy import locale_setup
from psychopy import prefs
from psychopy import sound, gui, visual, core, data, event, logging, clock
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle
import os  # handy system and path functions
import sys  # to get file system encoding

from psychopy.hardware import keyboard



# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
psychopyVersion = '2020.2.4post1'
expName = 'two-armed-bandit'  # from the Builder filename that created this script
expInfo = {'participant': ''}
dlg = gui.DlgFromDict(dictionary=expInfo, sort_keys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/sub-%s_task-%s' % (expInfo['participant'], expName)

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='C:\\Users\\Shawn\\Box Sync\\Georgetown University\\20211 - Course\\gu-psyc-347\\docs\\tasks\\two-armed-bandit\\two-armed-bandit.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run before the window creation

# Setup the Window
win = visual.Window(
    size=[1920, 1080], fullscr=True, screen=0, 
    winType='pyglet', allowGUI=False, allowStencil=False,
    monitor='testMonitor', color='black', colorSpace='rgb',
    blendMode='avg', useFBO=True, 
    units='height')
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard()

# Initialize components for Routine "intro"
introClock = core.Clock()
ptsSelf = 1000
ptsSocial = 1000

seed = int(expInfo['participant'])

order_file = f"orders/sub-{expInfo['participant']}_stim-order.csv"

#from psychopy import logging
#logging.log(level=logging.EXP, msg=(f'Order loaded from file: {order_file}'))
#logging.flush()


key_resp_1 = keyboard.Keyboard()
intro_text = visual.TextStim(win=win, name='intro_text',
    text='In this experiment you will see two slot machines appear on the screen and you need to select one of them.\n\nBased on your choices, you can win points. Points are converted into REAL MONEY at the end of the experiment.\n\nPress SPACE to continue.',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);

# Initialize components for Routine "instr1"
instr1Clock = core.Clock()
instr_1 = visual.TextStim(win=win, name='instr_1',
    text='Some slot machines will give you points more or less often than others. Your job is to figure out which machine is the best to choose, and select it using your arrow keys. \n\nPress SPACE to continue.',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
key_resp_2 = keyboard.Keyboard()

# Initialize components for Routine "instr2"
instr2Clock = core.Clock()
instr_2 = visual.TextStim(win=win, name='instr_2',
    text='Respond using the LEFT and RIGHT arrow keys matching whichever side the machine you choose appears. Sometimes the machine might appear on the left while other times it might appear on the right. \n\nTry to respond as quickly and accurately as possible. You have about 2 seconds to make your choice.\n\nPress SPACE to continue.',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
key_resp_4 = keyboard.Keyboard()

# Initialize components for Routine "instr3"
instr3Clock = core.Clock()
instr_3 = visual.TextStim(win=win, name='instr_3',
    text='After each choice, you will see feedback. \n\nSometimes you will win points, +100 points!\nSometimes you will not win points, 0 points\n\nPress SPACE to continue.',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
key_resp_3 = keyboard.Keyboard()

# Initialize components for Routine "prac_instr"
prac_instrClock = core.Clock()
read_prac = visual.TextStim(win=win, name='read_prac',
    text='Let’s try a few practice rounds. \n\nSometimes you will play to win points. Other times, you will play to avoid losing points. The task will tell you which condition you are in. \n\nPress SPACE to begin the practice.',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
key_resp_7 = keyboard.Keyboard()

# Initialize components for Routine "BlockInstruct"
BlockInstructClock = core.Clock()
BlockInstr_disp = visual.TextStim(win=win, name='BlockInstr_disp',
    text='default text',
    font='Arial',
    pos=(0, 0), height=0.08, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);

# Initialize components for Routine "fixation"
fixationClock = core.Clock()
iti = visual.ShapeStim(
    win=win, name='iti', vertices='cross',
    size=(0.05, 0.05),
    ori=0, pos=(0, 0),
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=1, depth=0.0, interpolate=True)

# Initialize components for Routine "stimuli"
stimuliClock = core.Clock()
left = visual.ImageStim(
    win=win,
    name='left', 
    image='sin', mask=None,
    ori=0, pos=(-0.4, 0), size=(0.4, 0.4),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
right = visual.ImageStim(
    win=win,
    name='right', 
    image='sin', mask=None,
    ori=0, pos=(0.4, 0), size=(0.4, 0.4),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
key_resp = keyboard.Keyboard()

# Initialize components for Routine "stimuli_feedback"
stimuli_feedbackClock = core.Clock()
left_feedback = visual.ImageStim(
    win=win,
    name='left_feedback', 
    image='sin', mask=None,
    ori=0, pos=(-0.4, 0), size=(0.4, 0.4),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
right_feedback = visual.ImageStim(
    win=win,
    name='right_feedback', 
    image='sin', mask=None,
    ori=0, pos=(0.4, 0), size=(0.4, 0.4),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)

# Initialize components for Routine "fixation"
fixationClock = core.Clock()
iti = visual.ShapeStim(
    win=win, name='iti', vertices='cross',
    size=(0.05, 0.05),
    ori=0, pos=(0, 0),
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=1, depth=0.0, interpolate=True)

# Initialize components for Routine "feedback"
feedbackClock = core.Clock()
feedback_text = visual.TextStim(win=win, name='feedback_text',
    text='default text',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);

# Initialize components for Routine "instr4"
instr4Clock = core.Clock()
instr_4 = visual.TextStim(win=win, name='instr_4',
    text='Now you will play the task for real.\n\nYou can win up to 3 dollars.\n\nPress SPACE to continue.',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
key_resp_8 = keyboard.Keyboard()

# Initialize components for Routine "exp_instr"
exp_instrClock = core.Clock()
ready_exp = visual.TextStim(win=win, name='ready_exp',
    text='Remember, your performance from now on will result in REAL MONETARY outcomes!\n\nYou will receive any money you win. \n\nPress SPACE to begin the experiment.',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
key_resp_5 = keyboard.Keyboard()

# Initialize components for Routine "BlockInstruct"
BlockInstructClock = core.Clock()
BlockInstr_disp = visual.TextStim(win=win, name='BlockInstr_disp',
    text='default text',
    font='Arial',
    pos=(0, 0), height=0.08, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);

# Initialize components for Routine "fixation"
fixationClock = core.Clock()
iti = visual.ShapeStim(
    win=win, name='iti', vertices='cross',
    size=(0.05, 0.05),
    ori=0, pos=(0, 0),
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=1, depth=0.0, interpolate=True)

# Initialize components for Routine "stimuli"
stimuliClock = core.Clock()
left = visual.ImageStim(
    win=win,
    name='left', 
    image='sin', mask=None,
    ori=0, pos=(-0.4, 0), size=(0.4, 0.4),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
right = visual.ImageStim(
    win=win,
    name='right', 
    image='sin', mask=None,
    ori=0, pos=(0.4, 0), size=(0.4, 0.4),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
key_resp = keyboard.Keyboard()

# Initialize components for Routine "stimuli_feedback"
stimuli_feedbackClock = core.Clock()
left_feedback = visual.ImageStim(
    win=win,
    name='left_feedback', 
    image='sin', mask=None,
    ori=0, pos=(-0.4, 0), size=(0.4, 0.4),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
right_feedback = visual.ImageStim(
    win=win,
    name='right_feedback', 
    image='sin', mask=None,
    ori=0, pos=(0.4, 0), size=(0.4, 0.4),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)

# Initialize components for Routine "fixation"
fixationClock = core.Clock()
iti = visual.ShapeStim(
    win=win, name='iti', vertices='cross',
    size=(0.05, 0.05),
    ori=0, pos=(0, 0),
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=1, depth=0.0, interpolate=True)

# Initialize components for Routine "feedback"
feedbackClock = core.Clock()
feedback_text = visual.TextStim(win=win, name='feedback_text',
    text='default text',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);

# Initialize components for Routine "ender"
enderClock = core.Clock()
end_heading = visual.TextStim(win=win, name='end_heading',
    text='Experiment complete!',
    font='Arial',
    pos=(0, 0.4), height=0.075, wrapWidth=None, ori=0, 
    color='yellow', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
end_text = visual.TextStim(win=win, name='end_text',
    text='default text',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
key_resp_6 = keyboard.Keyboard()
text_4 = visual.TextStim(win=win, name='text_4',
    text='Press SPACE to exit.',
    font='Arial',
    pos=(0, -0.4), height=0.08, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-4.0);

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "intro"-------
continueRoutine = True
# update component parameters for each repeat
key_resp_1.keys = []
key_resp_1.rt = []
_key_resp_1_allKeys = []
# keep track of which components have finished
introComponents = [key_resp_1, intro_text]
for thisComponent in introComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
introClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "intro"-------
while continueRoutine:
    # get current time
    t = introClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=introClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *key_resp_1* updates
    waitOnFlip = False
    if key_resp_1.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_1.frameNStart = frameN  # exact frame index
        key_resp_1.tStart = t  # local t and not account for scr refresh
        key_resp_1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_1, 'tStartRefresh')  # time at next scr refresh
        key_resp_1.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_1.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_1.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_1.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_1.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_1_allKeys.extend(theseKeys)
        if len(_key_resp_1_allKeys):
            key_resp_1.keys = _key_resp_1_allKeys[-1].name  # just the last key pressed
            key_resp_1.rt = _key_resp_1_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # *intro_text* updates
    if intro_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        intro_text.frameNStart = frameN  # exact frame index
        intro_text.tStart = t  # local t and not account for scr refresh
        intro_text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(intro_text, 'tStartRefresh')  # time at next scr refresh
        intro_text.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in introComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "intro"-------
for thisComponent in introComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "intro" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "instr1"-------
continueRoutine = True
# update component parameters for each repeat
key_resp_2.keys = []
key_resp_2.rt = []
_key_resp_2_allKeys = []
# keep track of which components have finished
instr1Components = [instr_1, key_resp_2]
for thisComponent in instr1Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
instr1Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "instr1"-------
while continueRoutine:
    # get current time
    t = instr1Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=instr1Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *instr_1* updates
    if instr_1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instr_1.frameNStart = frameN  # exact frame index
        instr_1.tStart = t  # local t and not account for scr refresh
        instr_1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instr_1, 'tStartRefresh')  # time at next scr refresh
        instr_1.setAutoDraw(True)
    
    # *key_resp_2* updates
    waitOnFlip = False
    if key_resp_2.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_2.frameNStart = frameN  # exact frame index
        key_resp_2.tStart = t  # local t and not account for scr refresh
        key_resp_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_2, 'tStartRefresh')  # time at next scr refresh
        key_resp_2.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_2.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_2.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_2.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_2.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_2_allKeys.extend(theseKeys)
        if len(_key_resp_2_allKeys):
            key_resp_2.keys = _key_resp_2_allKeys[-1].name  # just the last key pressed
            key_resp_2.rt = _key_resp_2_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in instr1Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "instr1"-------
for thisComponent in instr1Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "instr1" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "instr2"-------
continueRoutine = True
# update component parameters for each repeat
key_resp_4.keys = []
key_resp_4.rt = []
_key_resp_4_allKeys = []
# keep track of which components have finished
instr2Components = [instr_2, key_resp_4]
for thisComponent in instr2Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
instr2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "instr2"-------
while continueRoutine:
    # get current time
    t = instr2Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=instr2Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *instr_2* updates
    if instr_2.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
        # keep track of start time/frame for later
        instr_2.frameNStart = frameN  # exact frame index
        instr_2.tStart = t  # local t and not account for scr refresh
        instr_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instr_2, 'tStartRefresh')  # time at next scr refresh
        instr_2.setAutoDraw(True)
    
    # *key_resp_4* updates
    waitOnFlip = False
    if key_resp_4.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_4.frameNStart = frameN  # exact frame index
        key_resp_4.tStart = t  # local t and not account for scr refresh
        key_resp_4.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_4, 'tStartRefresh')  # time at next scr refresh
        key_resp_4.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_4.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_4.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_4.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_4.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_4_allKeys.extend(theseKeys)
        if len(_key_resp_4_allKeys):
            key_resp_4.keys = _key_resp_4_allKeys[-1].name  # just the last key pressed
            key_resp_4.rt = _key_resp_4_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in instr2Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "instr2"-------
for thisComponent in instr2Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "instr2" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "instr3"-------
continueRoutine = True
# update component parameters for each repeat
key_resp_3.keys = []
key_resp_3.rt = []
_key_resp_3_allKeys = []
# keep track of which components have finished
instr3Components = [instr_3, key_resp_3]
for thisComponent in instr3Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
instr3Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "instr3"-------
while continueRoutine:
    # get current time
    t = instr3Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=instr3Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *instr_3* updates
    if instr_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instr_3.frameNStart = frameN  # exact frame index
        instr_3.tStart = t  # local t and not account for scr refresh
        instr_3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instr_3, 'tStartRefresh')  # time at next scr refresh
        instr_3.setAutoDraw(True)
    
    # *key_resp_3* updates
    waitOnFlip = False
    if key_resp_3.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_3.frameNStart = frameN  # exact frame index
        key_resp_3.tStart = t  # local t and not account for scr refresh
        key_resp_3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_3, 'tStartRefresh')  # time at next scr refresh
        key_resp_3.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_3.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_3.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_3.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_3.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_3_allKeys.extend(theseKeys)
        if len(_key_resp_3_allKeys):
            key_resp_3.keys = _key_resp_3_allKeys[-1].name  # just the last key pressed
            key_resp_3.rt = _key_resp_3_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in instr3Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "instr3"-------
for thisComponent in instr3Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "instr3" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "prac_instr"-------
continueRoutine = True
# update component parameters for each repeat
key_resp_7.keys = []
key_resp_7.rt = []
_key_resp_7_allKeys = []
# keep track of which components have finished
prac_instrComponents = [read_prac, key_resp_7]
for thisComponent in prac_instrComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
prac_instrClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "prac_instr"-------
while continueRoutine:
    # get current time
    t = prac_instrClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=prac_instrClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *read_prac* updates
    if read_prac.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        read_prac.frameNStart = frameN  # exact frame index
        read_prac.tStart = t  # local t and not account for scr refresh
        read_prac.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(read_prac, 'tStartRefresh')  # time at next scr refresh
        read_prac.setAutoDraw(True)
    
    # *key_resp_7* updates
    waitOnFlip = False
    if key_resp_7.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_7.frameNStart = frameN  # exact frame index
        key_resp_7.tStart = t  # local t and not account for scr refresh
        key_resp_7.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_7, 'tStartRefresh')  # time at next scr refresh
        key_resp_7.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_7.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_7.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_7.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_7.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_7_allKeys.extend(theseKeys)
        if len(_key_resp_7_allKeys):
            key_resp_7.keys = _key_resp_7_allKeys[-1].name  # just the last key pressed
            key_resp_7.rt = _key_resp_7_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in prac_instrComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "prac_instr"-------
for thisComponent in prac_instrComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "prac_instr" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
practice_round = data.TrialHandler(nReps=1, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('orders\\prac_stim-order.csv'),
    seed=None, name='practice_round')
thisExp.addLoop(practice_round)  # add the loop to the experiment
thisPractice_round = practice_round.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisPractice_round.rgb)
if thisPractice_round != None:
    for paramName in thisPractice_round:
        exec('{} = thisPractice_round[paramName]'.format(paramName))

for thisPractice_round in practice_round:
    currentLoop = practice_round
    # abbreviate parameter names if possible (e.g. rgb = thisPractice_round.rgb)
    if thisPractice_round != None:
        for paramName in thisPractice_round:
            exec('{} = thisPractice_round[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "BlockInstruct"-------
    continueRoutine = True
    routineTimer.add(5.000000)
    # update component parameters for each repeat
    BlockInstr_disp.setText(block_instr_text)
    # keep track of which components have finished
    BlockInstructComponents = [BlockInstr_disp]
    for thisComponent in BlockInstructComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    BlockInstructClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "BlockInstruct"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = BlockInstructClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=BlockInstructClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        if trial_num != 0:
            continueRoutine = False
        
        # *BlockInstr_disp* updates
        if BlockInstr_disp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            BlockInstr_disp.frameNStart = frameN  # exact frame index
            BlockInstr_disp.tStart = t  # local t and not account for scr refresh
            BlockInstr_disp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(BlockInstr_disp, 'tStartRefresh')  # time at next scr refresh
            BlockInstr_disp.setAutoDraw(True)
        if BlockInstr_disp.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > BlockInstr_disp.tStartRefresh + 5-frameTolerance:
                # keep track of stop time/frame for later
                BlockInstr_disp.tStop = t  # not accounting for scr refresh
                BlockInstr_disp.frameNStop = frameN  # exact frame index
                win.timeOnFlip(BlockInstr_disp, 'tStopRefresh')  # time at next scr refresh
                BlockInstr_disp.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in BlockInstructComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "BlockInstruct"-------
    for thisComponent in BlockInstructComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    practice_round.addData('BlockInstr_disp.started', BlockInstr_disp.tStartRefresh)
    practice_round.addData('BlockInstr_disp.stopped', BlockInstr_disp.tStopRefresh)
    
    # ------Prepare to start Routine "fixation"-------
    continueRoutine = True
    routineTimer.add(0.500000)
    # update component parameters for each repeat
    # keep track of which components have finished
    fixationComponents = [iti]
    for thisComponent in fixationComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    fixationClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "fixation"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = fixationClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=fixationClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *iti* updates
        if iti.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            iti.frameNStart = frameN  # exact frame index
            iti.tStart = t  # local t and not account for scr refresh
            iti.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(iti, 'tStartRefresh')  # time at next scr refresh
            iti.setAutoDraw(True)
        if iti.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > iti.tStartRefresh + 0.5-frameTolerance:
                # keep track of stop time/frame for later
                iti.tStop = t  # not accounting for scr refresh
                iti.frameNStop = frameN  # exact frame index
                win.timeOnFlip(iti, 'tStopRefresh')  # time at next scr refresh
                iti.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in fixationComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "fixation"-------
    for thisComponent in fixationComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    practice_round.addData('iti.started', iti.tStartRefresh)
    practice_round.addData('iti.stopped', iti.tStopRefresh)
    
    # ------Prepare to start Routine "stimuli"-------
    continueRoutine = True
    routineTimer.add(2.000000)
    # update component parameters for each repeat
    left.setImage(stim_left_name)
    right.setImage(stim_right_name)
    key_resp.keys = []
    key_resp.rt = []
    _key_resp_allKeys = []
    # keep track of which components have finished
    stimuliComponents = [left, right, key_resp]
    for thisComponent in stimuliComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    stimuliClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "stimuli"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = stimuliClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=stimuliClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *left* updates
        if left.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            left.frameNStart = frameN  # exact frame index
            left.tStart = t  # local t and not account for scr refresh
            left.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(left, 'tStartRefresh')  # time at next scr refresh
            left.setAutoDraw(True)
        if left.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > left.tStartRefresh + 2-frameTolerance:
                # keep track of stop time/frame for later
                left.tStop = t  # not accounting for scr refresh
                left.frameNStop = frameN  # exact frame index
                win.timeOnFlip(left, 'tStopRefresh')  # time at next scr refresh
                left.setAutoDraw(False)
        
        # *right* updates
        if right.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            right.frameNStart = frameN  # exact frame index
            right.tStart = t  # local t and not account for scr refresh
            right.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(right, 'tStartRefresh')  # time at next scr refresh
            right.setAutoDraw(True)
        if right.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > right.tStartRefresh + 2-frameTolerance:
                # keep track of stop time/frame for later
                right.tStop = t  # not accounting for scr refresh
                right.frameNStop = frameN  # exact frame index
                win.timeOnFlip(right, 'tStopRefresh')  # time at next scr refresh
                right.setAutoDraw(False)
        
        # *key_resp* updates
        waitOnFlip = False
        if key_resp.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            key_resp.frameNStart = frameN  # exact frame index
            key_resp.tStart = t  # local t and not account for scr refresh
            key_resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp, 'tStartRefresh')  # time at next scr refresh
            key_resp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > key_resp.tStartRefresh + 2-frameTolerance:
                # keep track of stop time/frame for later
                key_resp.tStop = t  # not accounting for scr refresh
                key_resp.frameNStop = frameN  # exact frame index
                win.timeOnFlip(key_resp, 'tStopRefresh')  # time at next scr refresh
                key_resp.status = FINISHED
        if key_resp.status == STARTED and not waitOnFlip:
            theseKeys = key_resp.getKeys(keyList=['left', 'right'], waitRelease=False)
            _key_resp_allKeys.extend(theseKeys)
            if len(_key_resp_allKeys):
                key_resp.keys = _key_resp_allKeys[0].name  # just the first key pressed
                key_resp.rt = _key_resp_allKeys[0].rt
                # was this correct?
                if (key_resp.keys == str(optimal_choice)) or (key_resp.keys == optimal_choice):
                    key_resp.corr = 1
                else:
                    key_resp.corr = 0
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in stimuliComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "stimuli"-------
    for thisComponent in stimuliComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    practice_round.addData('left.started', left.tStartRefresh)
    practice_round.addData('left.stopped', left.tStopRefresh)
    practice_round.addData('right.started', right.tStartRefresh)
    practice_round.addData('right.stopped', right.tStopRefresh)
    # check responses
    if key_resp.keys in ['', [], None]:  # No response was made
        key_resp.keys = None
        # was no response the correct answer?!
        if str(optimal_choice).lower() == 'none':
           key_resp.corr = 1;  # correct non-response
        else:
           key_resp.corr = 0;  # failed to respond (incorrectly)
    # store data for practice_round (TrialHandler)
    practice_round.addData('key_resp.keys',key_resp.keys)
    practice_round.addData('key_resp.corr', key_resp.corr)
    if key_resp.keys != None:  # we had a response
        practice_round.addData('key_resp.rt', key_resp.rt)
    practice_round.addData('key_resp.started', key_resp.tStartRefresh)
    practice_round.addData('key_resp.stopped', key_resp.tStopRefresh)
    if position_changed == 0:
        if key_resp.keys == 'left':
            thisExp.addData('chosen_stim_name', stim_0)
            thisExp.addData('chosen_stim_0', 1)
            thisExp.addData('chosen_stim_1', 0)
            
            if goal == 'win':
                thisExp.addData('true_accuracy', 1)
            elif goal == 'avoidloss':
                thisExp.addData('true_accuracy', 0) 
    
        elif key_resp.keys == 'right':
            thisExp.addData('chosen_stim_name', stim_1)
            thisExp.addData('chosen_stim_0', 0)
            thisExp.addData('chosen_stim_1', 1)
            
            if goal == 'win':
                thisExp.addData('true_accuracy', 0)
            elif goal == 'avoidloss':
                thisExp.addData('true_accuracy', 1) 
    
    elif position_changed == 1:
        if key_resp.keys == 'left':
            thisExp.addData('chosen_stim_name', stim_1)
            thisExp.addData('chosen_stim_0', 0)
            thisExp.addData('chosen_stim_1', 1)
            
            if goal == 'win':
                thisExp.addData('true_accuracy', 0)
            elif goal == 'avoidloss':
                thisExp.addData('true_accuracy', 1) 
    
        elif key_resp.keys == 'right':
            thisExp.addData('chosen_stim_name', stim_0)
            thisExp.addData('chosen_stim_0', 1)
            thisExp.addData('chosen_stim_1', 0)
            
            if goal == 'win':
                thisExp.addData('true_accuracy', 1)
            elif goal == 'avoidloss':
                thisExp.addData('true_accuracy', 0) 
    
            
    
    # ------Prepare to start Routine "stimuli_feedback"-------
    continueRoutine = True
    routineTimer.add(0.500000)
    # update component parameters for each repeat
    if key_resp.keys == 'left':
        feedback_stim_right = stim_right_name
        feedback_stim_left = stim_left_name_feedback
    elif key_resp.keys == 'right':
        feedback_stim_right = stim_right_name_feedback
        feedback_stim_left = stim_left_name
    else:
        feedback_stim_right = stim_right_name
        feedback_stim_left = stim_left_name
    left_feedback.setImage(feedback_stim_left)
    right_feedback.setImage(feedback_stim_right)
    # keep track of which components have finished
    stimuli_feedbackComponents = [left_feedback, right_feedback]
    for thisComponent in stimuli_feedbackComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    stimuli_feedbackClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "stimuli_feedback"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = stimuli_feedbackClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=stimuli_feedbackClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *left_feedback* updates
        if left_feedback.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            left_feedback.frameNStart = frameN  # exact frame index
            left_feedback.tStart = t  # local t and not account for scr refresh
            left_feedback.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(left_feedback, 'tStartRefresh')  # time at next scr refresh
            left_feedback.setAutoDraw(True)
        if left_feedback.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > left_feedback.tStartRefresh + 0.5-frameTolerance:
                # keep track of stop time/frame for later
                left_feedback.tStop = t  # not accounting for scr refresh
                left_feedback.frameNStop = frameN  # exact frame index
                win.timeOnFlip(left_feedback, 'tStopRefresh')  # time at next scr refresh
                left_feedback.setAutoDraw(False)
        
        # *right_feedback* updates
        if right_feedback.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            right_feedback.frameNStart = frameN  # exact frame index
            right_feedback.tStart = t  # local t and not account for scr refresh
            right_feedback.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(right_feedback, 'tStartRefresh')  # time at next scr refresh
            right_feedback.setAutoDraw(True)
        if right_feedback.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > right_feedback.tStartRefresh + 0.5-frameTolerance:
                # keep track of stop time/frame for later
                right_feedback.tStop = t  # not accounting for scr refresh
                right_feedback.frameNStop = frameN  # exact frame index
                win.timeOnFlip(right_feedback, 'tStopRefresh')  # time at next scr refresh
                right_feedback.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in stimuli_feedbackComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "stimuli_feedback"-------
    for thisComponent in stimuli_feedbackComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    practice_round.addData('left_feedback.started', left_feedback.tStartRefresh)
    practice_round.addData('left_feedback.stopped', left_feedback.tStopRefresh)
    practice_round.addData('right_feedback.started', right_feedback.tStartRefresh)
    practice_round.addData('right_feedback.stopped', right_feedback.tStopRefresh)
    
    # ------Prepare to start Routine "fixation"-------
    continueRoutine = True
    routineTimer.add(0.500000)
    # update component parameters for each repeat
    # keep track of which components have finished
    fixationComponents = [iti]
    for thisComponent in fixationComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    fixationClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "fixation"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = fixationClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=fixationClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *iti* updates
        if iti.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            iti.frameNStart = frameN  # exact frame index
            iti.tStart = t  # local t and not account for scr refresh
            iti.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(iti, 'tStartRefresh')  # time at next scr refresh
            iti.setAutoDraw(True)
        if iti.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > iti.tStartRefresh + 0.5-frameTolerance:
                # keep track of stop time/frame for later
                iti.tStop = t  # not accounting for scr refresh
                iti.frameNStop = frameN  # exact frame index
                win.timeOnFlip(iti, 'tStopRefresh')  # time at next scr refresh
                iti.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in fixationComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "fixation"-------
    for thisComponent in fixationComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    practice_round.addData('iti.started', iti.tStartRefresh)
    practice_round.addData('iti.stopped', iti.tStopRefresh)
    
    # ------Prepare to start Routine "feedback"-------
    continueRoutine = True
    routineTimer.add(1.500000)
    # update component parameters for each repeat
    if not key_resp.keys:
        outcome = "missed"
        thisExp.addData('cumulativePts_self', ptsSelf) 
        if condition != "practice": 
            thisExp.addData('outcomeDescr', "missed")
    
    else:
        if key_resp.corr:
            if goal == "win":
                if condition == "self":
                    outcome = "YOU\n\n+100 points"
                    ptsSelf += 100
                    thisExp.addData('cumulativePts_self', ptsSelf) 
                    thisExp.addData('outcomeDescr', "self win") 
                    thisExp.addData('outcome', 1)
                    
                elif condition == "practice":
                    outcome = "+100 points"
                    
        else:
            if goal == "win":
                if condition == "self":
                    outcome = "YOU\n\n0 points"
                    ptsSelf += 0
                    thisExp.addData('cumulativePts_self', ptsSelf) 
                    thisExp.addData('outcomeDescr', "self avoid win") 
                    thisExp.addData('outcome', 0)
                    
                elif condition == "practice":
                    outcome = "0 points"
    
    if condition == "practice":
        thisExp.addData('cumulativePts_self', 1000) 
        thisExp.addData('outcomeDescr', "practice") 
    feedback_text.setText(outcome)
    # keep track of which components have finished
    feedbackComponents = [feedback_text]
    for thisComponent in feedbackComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    feedbackClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "feedback"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = feedbackClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=feedbackClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *feedback_text* updates
        if feedback_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            feedback_text.frameNStart = frameN  # exact frame index
            feedback_text.tStart = t  # local t and not account for scr refresh
            feedback_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(feedback_text, 'tStartRefresh')  # time at next scr refresh
            feedback_text.setAutoDraw(True)
        if feedback_text.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > feedback_text.tStartRefresh + 1.5-frameTolerance:
                # keep track of stop time/frame for later
                feedback_text.tStop = t  # not accounting for scr refresh
                feedback_text.frameNStop = frameN  # exact frame index
                win.timeOnFlip(feedback_text, 'tStopRefresh')  # time at next scr refresh
                feedback_text.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in feedbackComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "feedback"-------
    for thisComponent in feedbackComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    practice_round.addData('feedback_text.started', feedback_text.tStartRefresh)
    practice_round.addData('feedback_text.stopped', feedback_text.tStopRefresh)
# completed 1 repeats of 'practice_round'


# ------Prepare to start Routine "instr4"-------
continueRoutine = True
# update component parameters for each repeat
key_resp_8.keys = []
key_resp_8.rt = []
_key_resp_8_allKeys = []
# keep track of which components have finished
instr4Components = [instr_4, key_resp_8]
for thisComponent in instr4Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
instr4Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "instr4"-------
while continueRoutine:
    # get current time
    t = instr4Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=instr4Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *instr_4* updates
    if instr_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instr_4.frameNStart = frameN  # exact frame index
        instr_4.tStart = t  # local t and not account for scr refresh
        instr_4.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instr_4, 'tStartRefresh')  # time at next scr refresh
        instr_4.setAutoDraw(True)
    
    # *key_resp_8* updates
    waitOnFlip = False
    if key_resp_8.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_8.frameNStart = frameN  # exact frame index
        key_resp_8.tStart = t  # local t and not account for scr refresh
        key_resp_8.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_8, 'tStartRefresh')  # time at next scr refresh
        key_resp_8.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_8.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_8.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_8.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_8.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_8_allKeys.extend(theseKeys)
        if len(_key_resp_8_allKeys):
            key_resp_8.keys = _key_resp_8_allKeys[-1].name  # just the last key pressed
            key_resp_8.rt = _key_resp_8_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in instr4Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "instr4"-------
for thisComponent in instr4Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "instr4" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "exp_instr"-------
continueRoutine = True
# update component parameters for each repeat
key_resp_5.keys = []
key_resp_5.rt = []
_key_resp_5_allKeys = []
# keep track of which components have finished
exp_instrComponents = [ready_exp, key_resp_5]
for thisComponent in exp_instrComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
exp_instrClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "exp_instr"-------
while continueRoutine:
    # get current time
    t = exp_instrClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=exp_instrClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *ready_exp* updates
    if ready_exp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        ready_exp.frameNStart = frameN  # exact frame index
        ready_exp.tStart = t  # local t and not account for scr refresh
        ready_exp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(ready_exp, 'tStartRefresh')  # time at next scr refresh
        ready_exp.setAutoDraw(True)
    
    # *key_resp_5* updates
    waitOnFlip = False
    if key_resp_5.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_5.frameNStart = frameN  # exact frame index
        key_resp_5.tStart = t  # local t and not account for scr refresh
        key_resp_5.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_5, 'tStartRefresh')  # time at next scr refresh
        key_resp_5.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_5.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_5.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_5.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_5.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_5_allKeys.extend(theseKeys)
        if len(_key_resp_5_allKeys):
            key_resp_5.keys = _key_resp_5_allKeys[-1].name  # just the last key pressed
            key_resp_5.rt = _key_resp_5_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in exp_instrComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "exp_instr"-------
for thisComponent in exp_instrComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "exp_instr" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trials = data.TrialHandler(nReps=1, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions(order_file),
    seed=None, name='trials')
thisExp.addLoop(trials)  # add the loop to the experiment
thisTrial = trials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
if thisTrial != None:
    for paramName in thisTrial:
        exec('{} = thisTrial[paramName]'.format(paramName))

for thisTrial in trials:
    currentLoop = trials
    # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
    if thisTrial != None:
        for paramName in thisTrial:
            exec('{} = thisTrial[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "BlockInstruct"-------
    continueRoutine = True
    routineTimer.add(5.000000)
    # update component parameters for each repeat
    BlockInstr_disp.setText(block_instr_text)
    # keep track of which components have finished
    BlockInstructComponents = [BlockInstr_disp]
    for thisComponent in BlockInstructComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    BlockInstructClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "BlockInstruct"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = BlockInstructClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=BlockInstructClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        if trial_num != 0:
            continueRoutine = False
        
        # *BlockInstr_disp* updates
        if BlockInstr_disp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            BlockInstr_disp.frameNStart = frameN  # exact frame index
            BlockInstr_disp.tStart = t  # local t and not account for scr refresh
            BlockInstr_disp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(BlockInstr_disp, 'tStartRefresh')  # time at next scr refresh
            BlockInstr_disp.setAutoDraw(True)
        if BlockInstr_disp.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > BlockInstr_disp.tStartRefresh + 5-frameTolerance:
                # keep track of stop time/frame for later
                BlockInstr_disp.tStop = t  # not accounting for scr refresh
                BlockInstr_disp.frameNStop = frameN  # exact frame index
                win.timeOnFlip(BlockInstr_disp, 'tStopRefresh')  # time at next scr refresh
                BlockInstr_disp.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in BlockInstructComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "BlockInstruct"-------
    for thisComponent in BlockInstructComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials.addData('BlockInstr_disp.started', BlockInstr_disp.tStartRefresh)
    trials.addData('BlockInstr_disp.stopped', BlockInstr_disp.tStopRefresh)
    
    # ------Prepare to start Routine "fixation"-------
    continueRoutine = True
    routineTimer.add(0.500000)
    # update component parameters for each repeat
    # keep track of which components have finished
    fixationComponents = [iti]
    for thisComponent in fixationComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    fixationClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "fixation"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = fixationClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=fixationClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *iti* updates
        if iti.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            iti.frameNStart = frameN  # exact frame index
            iti.tStart = t  # local t and not account for scr refresh
            iti.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(iti, 'tStartRefresh')  # time at next scr refresh
            iti.setAutoDraw(True)
        if iti.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > iti.tStartRefresh + 0.5-frameTolerance:
                # keep track of stop time/frame for later
                iti.tStop = t  # not accounting for scr refresh
                iti.frameNStop = frameN  # exact frame index
                win.timeOnFlip(iti, 'tStopRefresh')  # time at next scr refresh
                iti.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in fixationComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "fixation"-------
    for thisComponent in fixationComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials.addData('iti.started', iti.tStartRefresh)
    trials.addData('iti.stopped', iti.tStopRefresh)
    
    # ------Prepare to start Routine "stimuli"-------
    continueRoutine = True
    routineTimer.add(2.000000)
    # update component parameters for each repeat
    left.setImage(stim_left_name)
    right.setImage(stim_right_name)
    key_resp.keys = []
    key_resp.rt = []
    _key_resp_allKeys = []
    # keep track of which components have finished
    stimuliComponents = [left, right, key_resp]
    for thisComponent in stimuliComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    stimuliClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "stimuli"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = stimuliClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=stimuliClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *left* updates
        if left.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            left.frameNStart = frameN  # exact frame index
            left.tStart = t  # local t and not account for scr refresh
            left.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(left, 'tStartRefresh')  # time at next scr refresh
            left.setAutoDraw(True)
        if left.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > left.tStartRefresh + 2-frameTolerance:
                # keep track of stop time/frame for later
                left.tStop = t  # not accounting for scr refresh
                left.frameNStop = frameN  # exact frame index
                win.timeOnFlip(left, 'tStopRefresh')  # time at next scr refresh
                left.setAutoDraw(False)
        
        # *right* updates
        if right.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            right.frameNStart = frameN  # exact frame index
            right.tStart = t  # local t and not account for scr refresh
            right.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(right, 'tStartRefresh')  # time at next scr refresh
            right.setAutoDraw(True)
        if right.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > right.tStartRefresh + 2-frameTolerance:
                # keep track of stop time/frame for later
                right.tStop = t  # not accounting for scr refresh
                right.frameNStop = frameN  # exact frame index
                win.timeOnFlip(right, 'tStopRefresh')  # time at next scr refresh
                right.setAutoDraw(False)
        
        # *key_resp* updates
        waitOnFlip = False
        if key_resp.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            key_resp.frameNStart = frameN  # exact frame index
            key_resp.tStart = t  # local t and not account for scr refresh
            key_resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp, 'tStartRefresh')  # time at next scr refresh
            key_resp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > key_resp.tStartRefresh + 2-frameTolerance:
                # keep track of stop time/frame for later
                key_resp.tStop = t  # not accounting for scr refresh
                key_resp.frameNStop = frameN  # exact frame index
                win.timeOnFlip(key_resp, 'tStopRefresh')  # time at next scr refresh
                key_resp.status = FINISHED
        if key_resp.status == STARTED and not waitOnFlip:
            theseKeys = key_resp.getKeys(keyList=['left', 'right'], waitRelease=False)
            _key_resp_allKeys.extend(theseKeys)
            if len(_key_resp_allKeys):
                key_resp.keys = _key_resp_allKeys[0].name  # just the first key pressed
                key_resp.rt = _key_resp_allKeys[0].rt
                # was this correct?
                if (key_resp.keys == str(optimal_choice)) or (key_resp.keys == optimal_choice):
                    key_resp.corr = 1
                else:
                    key_resp.corr = 0
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in stimuliComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "stimuli"-------
    for thisComponent in stimuliComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials.addData('left.started', left.tStartRefresh)
    trials.addData('left.stopped', left.tStopRefresh)
    trials.addData('right.started', right.tStartRefresh)
    trials.addData('right.stopped', right.tStopRefresh)
    # check responses
    if key_resp.keys in ['', [], None]:  # No response was made
        key_resp.keys = None
        # was no response the correct answer?!
        if str(optimal_choice).lower() == 'none':
           key_resp.corr = 1;  # correct non-response
        else:
           key_resp.corr = 0;  # failed to respond (incorrectly)
    # store data for trials (TrialHandler)
    trials.addData('key_resp.keys',key_resp.keys)
    trials.addData('key_resp.corr', key_resp.corr)
    if key_resp.keys != None:  # we had a response
        trials.addData('key_resp.rt', key_resp.rt)
    trials.addData('key_resp.started', key_resp.tStartRefresh)
    trials.addData('key_resp.stopped', key_resp.tStopRefresh)
    if position_changed == 0:
        if key_resp.keys == 'left':
            thisExp.addData('chosen_stim_name', stim_0)
            thisExp.addData('chosen_stim_0', 1)
            thisExp.addData('chosen_stim_1', 0)
            
            if goal == 'win':
                thisExp.addData('true_accuracy', 1)
            elif goal == 'avoidloss':
                thisExp.addData('true_accuracy', 0) 
    
        elif key_resp.keys == 'right':
            thisExp.addData('chosen_stim_name', stim_1)
            thisExp.addData('chosen_stim_0', 0)
            thisExp.addData('chosen_stim_1', 1)
            
            if goal == 'win':
                thisExp.addData('true_accuracy', 0)
            elif goal == 'avoidloss':
                thisExp.addData('true_accuracy', 1) 
    
    elif position_changed == 1:
        if key_resp.keys == 'left':
            thisExp.addData('chosen_stim_name', stim_1)
            thisExp.addData('chosen_stim_0', 0)
            thisExp.addData('chosen_stim_1', 1)
            
            if goal == 'win':
                thisExp.addData('true_accuracy', 0)
            elif goal == 'avoidloss':
                thisExp.addData('true_accuracy', 1) 
    
        elif key_resp.keys == 'right':
            thisExp.addData('chosen_stim_name', stim_0)
            thisExp.addData('chosen_stim_0', 1)
            thisExp.addData('chosen_stim_1', 0)
            
            if goal == 'win':
                thisExp.addData('true_accuracy', 1)
            elif goal == 'avoidloss':
                thisExp.addData('true_accuracy', 0) 
    
            
    
    # ------Prepare to start Routine "stimuli_feedback"-------
    continueRoutine = True
    routineTimer.add(0.500000)
    # update component parameters for each repeat
    if key_resp.keys == 'left':
        feedback_stim_right = stim_right_name
        feedback_stim_left = stim_left_name_feedback
    elif key_resp.keys == 'right':
        feedback_stim_right = stim_right_name_feedback
        feedback_stim_left = stim_left_name
    else:
        feedback_stim_right = stim_right_name
        feedback_stim_left = stim_left_name
    left_feedback.setImage(feedback_stim_left)
    right_feedback.setImage(feedback_stim_right)
    # keep track of which components have finished
    stimuli_feedbackComponents = [left_feedback, right_feedback]
    for thisComponent in stimuli_feedbackComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    stimuli_feedbackClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "stimuli_feedback"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = stimuli_feedbackClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=stimuli_feedbackClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *left_feedback* updates
        if left_feedback.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            left_feedback.frameNStart = frameN  # exact frame index
            left_feedback.tStart = t  # local t and not account for scr refresh
            left_feedback.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(left_feedback, 'tStartRefresh')  # time at next scr refresh
            left_feedback.setAutoDraw(True)
        if left_feedback.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > left_feedback.tStartRefresh + 0.5-frameTolerance:
                # keep track of stop time/frame for later
                left_feedback.tStop = t  # not accounting for scr refresh
                left_feedback.frameNStop = frameN  # exact frame index
                win.timeOnFlip(left_feedback, 'tStopRefresh')  # time at next scr refresh
                left_feedback.setAutoDraw(False)
        
        # *right_feedback* updates
        if right_feedback.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            right_feedback.frameNStart = frameN  # exact frame index
            right_feedback.tStart = t  # local t and not account for scr refresh
            right_feedback.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(right_feedback, 'tStartRefresh')  # time at next scr refresh
            right_feedback.setAutoDraw(True)
        if right_feedback.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > right_feedback.tStartRefresh + 0.5-frameTolerance:
                # keep track of stop time/frame for later
                right_feedback.tStop = t  # not accounting for scr refresh
                right_feedback.frameNStop = frameN  # exact frame index
                win.timeOnFlip(right_feedback, 'tStopRefresh')  # time at next scr refresh
                right_feedback.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in stimuli_feedbackComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "stimuli_feedback"-------
    for thisComponent in stimuli_feedbackComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials.addData('left_feedback.started', left_feedback.tStartRefresh)
    trials.addData('left_feedback.stopped', left_feedback.tStopRefresh)
    trials.addData('right_feedback.started', right_feedback.tStartRefresh)
    trials.addData('right_feedback.stopped', right_feedback.tStopRefresh)
    
    # ------Prepare to start Routine "fixation"-------
    continueRoutine = True
    routineTimer.add(0.500000)
    # update component parameters for each repeat
    # keep track of which components have finished
    fixationComponents = [iti]
    for thisComponent in fixationComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    fixationClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "fixation"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = fixationClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=fixationClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *iti* updates
        if iti.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            iti.frameNStart = frameN  # exact frame index
            iti.tStart = t  # local t and not account for scr refresh
            iti.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(iti, 'tStartRefresh')  # time at next scr refresh
            iti.setAutoDraw(True)
        if iti.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > iti.tStartRefresh + 0.5-frameTolerance:
                # keep track of stop time/frame for later
                iti.tStop = t  # not accounting for scr refresh
                iti.frameNStop = frameN  # exact frame index
                win.timeOnFlip(iti, 'tStopRefresh')  # time at next scr refresh
                iti.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in fixationComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "fixation"-------
    for thisComponent in fixationComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials.addData('iti.started', iti.tStartRefresh)
    trials.addData('iti.stopped', iti.tStopRefresh)
    
    # ------Prepare to start Routine "feedback"-------
    continueRoutine = True
    routineTimer.add(1.500000)
    # update component parameters for each repeat
    if not key_resp.keys:
        outcome = "missed"
        thisExp.addData('cumulativePts_self', ptsSelf) 
        if condition != "practice": 
            thisExp.addData('outcomeDescr', "missed")
    
    else:
        if key_resp.corr:
            if goal == "win":
                if condition == "self":
                    outcome = "YOU\n\n+100 points"
                    ptsSelf += 100
                    thisExp.addData('cumulativePts_self', ptsSelf) 
                    thisExp.addData('outcomeDescr', "self win") 
                    thisExp.addData('outcome', 1)
                    
                elif condition == "practice":
                    outcome = "+100 points"
                    
        else:
            if goal == "win":
                if condition == "self":
                    outcome = "YOU\n\n0 points"
                    ptsSelf += 0
                    thisExp.addData('cumulativePts_self', ptsSelf) 
                    thisExp.addData('outcomeDescr', "self avoid win") 
                    thisExp.addData('outcome', 0)
                    
                elif condition == "practice":
                    outcome = "0 points"
    
    if condition == "practice":
        thisExp.addData('cumulativePts_self', 1000) 
        thisExp.addData('outcomeDescr', "practice") 
    feedback_text.setText(outcome)
    # keep track of which components have finished
    feedbackComponents = [feedback_text]
    for thisComponent in feedbackComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    feedbackClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "feedback"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = feedbackClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=feedbackClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *feedback_text* updates
        if feedback_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            feedback_text.frameNStart = frameN  # exact frame index
            feedback_text.tStart = t  # local t and not account for scr refresh
            feedback_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(feedback_text, 'tStartRefresh')  # time at next scr refresh
            feedback_text.setAutoDraw(True)
        if feedback_text.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > feedback_text.tStartRefresh + 1.5-frameTolerance:
                # keep track of stop time/frame for later
                feedback_text.tStop = t  # not accounting for scr refresh
                feedback_text.frameNStop = frameN  # exact frame index
                win.timeOnFlip(feedback_text, 'tStopRefresh')  # time at next scr refresh
                feedback_text.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in feedbackComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "feedback"-------
    for thisComponent in feedbackComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials.addData('feedback_text.started', feedback_text.tStartRefresh)
    trials.addData('feedback_text.stopped', feedback_text.tStopRefresh)
    thisExp.nextEntry()
    
# completed 1 repeats of 'trials'

# get names of stimulus parameters
if trials.trialList in ([], [None], None):
    params = []
else:
    params = trials.trialList[0].keys()
# save data for this loop
trials.saveAsText(filename + 'trials.csv', delim=',',
    stimOut=params,
    dataOut=['n','all_mean','all_std', 'all_raw'])

# ------Prepare to start Routine "ender"-------
continueRoutine = True
# update component parameters for each repeat
if (ptsSelf > 0):
    end_result = f"You won {ptsSelf} points for YOURSELF!"
else:
    end_result = "You did not win any points."
    
#from psychopy import logging
#logging.log(level=logging.WARN, msg=(f'Participant wins: {points} points'))
#logging.flush() 
#

end_text.setText(end_result)
key_resp_6.keys = []
key_resp_6.rt = []
_key_resp_6_allKeys = []
# keep track of which components have finished
enderComponents = [end_heading, end_text, key_resp_6, text_4]
for thisComponent in enderComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
enderClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "ender"-------
while continueRoutine:
    # get current time
    t = enderClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=enderClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *end_heading* updates
    if end_heading.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        end_heading.frameNStart = frameN  # exact frame index
        end_heading.tStart = t  # local t and not account for scr refresh
        end_heading.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(end_heading, 'tStartRefresh')  # time at next scr refresh
        end_heading.setAutoDraw(True)
    
    # *end_text* updates
    if end_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        end_text.frameNStart = frameN  # exact frame index
        end_text.tStart = t  # local t and not account for scr refresh
        end_text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(end_text, 'tStartRefresh')  # time at next scr refresh
        end_text.setAutoDraw(True)
    
    # *key_resp_6* updates
    waitOnFlip = False
    if key_resp_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_6.frameNStart = frameN  # exact frame index
        key_resp_6.tStart = t  # local t and not account for scr refresh
        key_resp_6.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_6, 'tStartRefresh')  # time at next scr refresh
        key_resp_6.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_6.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_6.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_6.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_6.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_6_allKeys.extend(theseKeys)
        if len(_key_resp_6_allKeys):
            key_resp_6.keys = _key_resp_6_allKeys[-1].name  # just the last key pressed
            key_resp_6.rt = _key_resp_6_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # *text_4* updates
    if text_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_4.frameNStart = frameN  # exact frame index
        text_4.tStart = t  # local t and not account for scr refresh
        text_4.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_4, 'tStartRefresh')  # time at next scr refresh
        text_4.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in enderComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "ender"-------
for thisComponent in enderComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "ender" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv', delim='auto')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
