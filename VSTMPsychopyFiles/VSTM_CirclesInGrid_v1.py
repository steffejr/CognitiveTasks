#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy2 Experiment Builder (v1.85.1),
    on Tue Aug 22 11:30:00 2017
If you publish work using this script please cite the PsychoPy publications:
    Peirce, JW (2007) PsychoPy - Psychophysics software in Python.
        Journal of Neuroscience Methods, 162(1-2), 8-13.
    Peirce, JW (2009) Generating stimuli for neuroscience using PsychoPy.
        Frontiers in Neuroinformatics, 2:10. doi: 10.3389/neuro.11.010.2008

The changes to this version are as follows.
The "old" responses were not being cleared at the start of each probe period. 
The result was that if a response was made after the probe letter went away it was technically
made during the next trial. The result was that when the next probe letter was displayed
there already was a response waiting to be recorded. This showed up as one trial having a none
response and the next having an RT of 7.0 seconds.
To fix this I moved the ITI to the end of the trial and allowed the RT to take place while the probe was
on the screen or even if it was made during this post trial ITI period of one second.
Therefore, the participant has 3.5 seconds to respond, otherwise the response is missed. 

I also simplified and shortened the code using a second for loop for blocks.
"""

from __future__ import absolute_import, division
from psychopy import locale_setup, gui, visual, core, data, event, logging
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)
import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle
import os  # handy system and path functions
import sys  # to get file system encoding
import random

# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__)).decode(sys.getfilesystemencoding())
os.chdir(_thisDir)

# Store info about the experiment session
expName = u'VSTM_Block'  # from the Builder filename that created this script
expInfo = {'Participant ID':'', 'Session':'001'}
PartDataFolder = 'unorganized'
if len(sys.argv) > 2:
    #tempFile.write("Entered if clause\n")
    #tempFile.write('%s\n'%(sys.argv[2]))
    expInfo['Participant ID'] = sys.argv[1]
    #tempFile.write('%s\n'%(sys.argv[1]))
    #tempFile.write('%s\n'%(sys.argv[2]))
    LoadList = sys.argv[2].split(' ')
    LoadList = np.array(LoadList)
    LoadList = LoadList.astype(np.int)
    PartDataFolder = sys.argv[1]
else:
    dlg = gui.DlgFromDict(dictionary=expInfo)
    if dlg.OK == False:
        core.quit()  # user pressed cancel
    LoadList = np.array(range(1,6,1)) ### <<<<<<<<<<<<<<<<<<<
    LoadList = LoadList.astype(np.int)
#tempFile.write("Loaded inputs\n")
expInfo['date'] = data.getDateStr()  # add a simple timestamp


# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
OutDir = '..' + os.sep + '..' + os.sep + 'data' + os.sep + PartDataFolder + os.sep
filename = OutDir + '%s_%s_%s' % (expName, expInfo['Participant ID'], expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath=u'/home/jsteffe/Dropbox/SteffenerColumbia/Projects/MyProjects/NeuralCognitiveMapping/DMSPsychopyFiles/DMS_Adaptive.psyexp',
    savePickle=True, saveWideText=True,
    dataFileName=filename)

logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp

# Start Code - component code to be run before the window creation

FontSize = 60
FontSizeUnits = 'pix'
GridCount = 7 # Number of circles to have on each row
GridSize = 160 # The size of the grid for which the circles on on
CircleSize = (GridSize*2)/GridCount # The circle size so that they are all just touching
OffSet = range(-GridSize+int(CircleSize/2),GridSize-int(CircleSize/2),int(CircleSize))

# units=FontSizeUnits
# height=FontSize
StimOnTime = 2.5
RetOnTime = 3.5
ProbeOnTime= 2.5
# This is the intertrial interval. This experimental component is part of the trial.
ITITime = 1.0
# This is the time between blocks. Note that between each block of trials there
# is also the 3-2-1 countdown. Therefore, the full interblock interval is this value PLUS 
# the countdown time, which is 3 seconds.
InterBlockTime = 1#13.0
# This is a delay component for use after instructions and before the first Block and at the
# the end before the thank you screen
ShortDelayTime = 1#16.0
NumberOfBlocks = 5

## These are great for testing quickly
#  StimOnTime = .25
#RetOnTime = .25
#ProbeOnTime= .25
#ITITime = .25
TotalTrialTime = StimOnTime + RetOnTime + ProbeOnTime + ITITime

# Setup the Window
win = visual.Window(
    size=(1920, 1080), fullscr=True, screen=0,
    allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
    blendMode='avg', useFBO=True,
    units=FontSizeUnits)

# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

circle = visual.Polygon(
    win=win, name='polygon',units='pix', 
    edges=128, size=(CircleSize, CircleSize),
    ori=0, pos=(0, 0),
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor='white', fillColorSpace='rgb',
    opacity=1, depth=0.0, interpolate=True)

textDelay = visual.TextStim(win=win, name='textDelay',
    text='+',
    font='Times New Roman',
    units=FontSizeUnits, pos=(0, 0), height=FontSize, wrapWidth=None, ori=0, 
    color='green', colorSpace='rgb', opacity=1,
    depth=-9.0);
    
textProbe = visual.TextStim(win=win, name='textProbe',
    text='default text',
    font='Times New Roman',
    units=FontSizeUnits, pos=(0, 0), height=FontSize, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-10.0);
    
textITI = visual.TextStim(win=win, name='textITI',
    text='+',
    font='Times New Roman',
    units=FontSizeUnits, pos=(0, 0), height=FontSize, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-11.0); 
# Initialize components for Routine "Instructions"
InstructionsClock = core.Clock()
textInstr1 = visual.TextStim(win=win, name='textInstr1',
    text='Ready to start the main experiment?\nRemember:\nPress [LEFT] if the circle WAS in the set.\nPress [DOWN] if the circle was NOT in the set.\n\nTry to respond as quickly and as accurately as possible.\n\nWhen you are ready to proceed press any key.',
    font='Times New Roman',
    units=FontSizeUnits, pos=(0, 0), height=FontSize*0.75, wrapWidth=None, ori=0, 
    color='yellow', colorSpace='rgb', opacity=1,
    depth=0.0);

# Initialize components for Routine "ShortDelay"
ShortDelayClock = core.Clock()
textEndDelay = visual.TextStim(win=win, name='textEndDelay',
    text='+',
    font='Times New Roman',
    units=FontSizeUnits, pos=(0, 0), height=FontSize, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0);

# Initialize components for Routine "Countdown"
CountdownClock = core.Clock()
text3 = visual.TextStim(win=win, name='text3',
    text='3',
    font='Times New Roman',
    units=FontSizeUnits, pos=(0, 0), height=FontSize, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0);
text2 = visual.TextStim(win=win, name='text2',
    text='2',
    font='Times New Roman',
    units=FontSizeUnits, pos=(0, 0), height=FontSize, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-1.0);
text1 = visual.TextStim(win=win, name='text1',
    text='1',
    font='Times New Roman',
    units=FontSizeUnits, pos=(0, 0), height=FontSize, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-2.0);

# Initialize components for Routine "trial"
trialClock = core.Clock()

# Initialize components for Routine "Interblock"
InterblockClock = core.Clock()
textInterblock = visual.TextStim(win=win, name='textInterblock',
    text='+',
    font='Times New Roman',
    units=FontSizeUnits, pos=(0, 0), height=FontSize, wrapWidth=None, ori=0, 
    color='red', colorSpace='rgb', opacity=1,
    depth=0.0);

# Initialize components for Routine "ShortDelay"
ShortDelayClock = core.Clock()
textEndDelay = visual.TextStim(win=win, name='textEndDelay',
    text='+',
    font='Times New Roman',
    units=FontSizeUnits, pos=(0, 0), height=FontSize, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0);

# Initialize components for Routine "Thankyou"
ThankyouClock = core.Clock()
textThankyou = visual.TextStim(win=win, name='textThankyou',
    text='Thank you for participating!',
    font='Times New Roman',
    units=FontSizeUnits, pos=(0, 0), height=FontSize, wrapWidth=None, ori=0, 
    color='yellow', colorSpace='rgb', opacity=1,
    depth=0.0);

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "Instructions"-------
t = 0
InstructionsClock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
OK1 = event.BuilderKeyResponse()
# keep track of which components have finished
InstructionsComponents = [textInstr1, OK1]
for thisComponent in InstructionsComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "Instructions"-------
while continueRoutine:
    # get current time
    t = InstructionsClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *textInstr1* updates
    if t >= 0.0 and textInstr1.status == NOT_STARTED:
        # keep track of start time/frame for later
        textInstr1.tStart = t
        textInstr1.frameNStart = frameN  # exact frame index
        textInstr1.setAutoDraw(True)
    
    # *OK1* updates
    if t >= 0.0 and OK1.status == NOT_STARTED:
        # keep track of start time/frame for later
        OK1.tStart = t
        OK1.frameNStart = frameN  # exact frame index
        OK1.status = STARTED
        # keyboard checking is just starting
        event.clearEvents(eventType='keyboard')
    if OK1.status == STARTED:
        theseKeys = event.getKeys()
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            # a response ends the routine
            continueRoutine = False
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in InstructionsComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Instructions"-------
for thisComponent in InstructionsComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "Instructions" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "ShortDelay"-------
t = 0
globalClock.reset()
thisExp.addData('StartTime', globalClock.getTime())


ShortDelayClock.reset()  # clock
frameN = -1
continueRoutine = True
routineTimer.add(ShortDelayTime)
# update component parameters for each repeat
# keep track of which components have finished
ShortDelayComponents = [textEndDelay]
for thisComponent in ShortDelayComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "ShortDelay"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = ShortDelayClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *textEndDelay* updates
    if t >= 0.0 and textEndDelay.status == NOT_STARTED:
        # keep track of start time/frame for later
        textEndDelay.tStart = t
        textEndDelay.frameNStart = frameN  # exact frame index
        textEndDelay.setAutoDraw(True)
    frameRemains = 0.0 + ShortDelayTime- win.monitorFramePeriod * 0.75  # most of one frame period left
    if textEndDelay.status == STARTED and t >= frameRemains:
        textEndDelay.setAutoDraw(False)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in ShortDelayComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "ShortDelay"-------
for thisComponent in ShortDelayComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)



# set up handler to look after randomisation of conditions etc
Blocks = data.TrialHandler(nReps=NumberOfBlocks, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='Blocks')
thisExp.addLoop(Blocks)  # add the loop to the experiment
thisBlock = Blocks.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisBlock.rgb)
if thisBlock != None:
    for paramName in thisBlock.keys():
        exec(paramName + '= thisBlock.' + paramName)
# This counter is used to keep track of which block of the experiment is being presented.
# It is also used to index the block load level list. This allows each block to dynamically be
# set to different load levels based on their capacity.

BlockCount = 1
for thisBlock in Blocks:
    currentLoop = Blocks
    # abbreviate parameter names if possible (e.g. rgb = thisBlock.rgb)
    if thisBlock != None:
        for paramName in thisBlock.keys():
            exec(paramName + '= thisBlock.' + paramName)
    ## Set up which rows to select 
    print "Block = %d"%(BlockCount)
    print LoadList
    CurrentLoad = LoadList[BlockCount-1]
    print "CurrentLoad = %d"%(CurrentLoad)
    SelectionList = np.array(range(0,NumberOfBlocks,1)) + (CurrentLoad - 1)*NumberOfBlocks
    
    # ------Prepare to start Routine "Countdown"-------
    t = 0
    CountdownClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    routineTimer.add(3.000000)
    # update component parameters for each repeat
    # keep track of which components have finished
    CountdownComponents = [text3, text2, text1]
    for thisComponent in CountdownComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "Countdown"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = CountdownClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text3* updates
        if t >= 0.0 and text3.status == NOT_STARTED:
            # keep track of start time/frame for later
            text3.tStart = t
            text3.frameNStart = frameN  # exact frame index
            text3.setAutoDraw(True)
        frameRemains = 0.0 + 1.0- win.monitorFramePeriod * 0.75  # most of one frame period left
        if text3.status == STARTED and t >= frameRemains:
            text3.setAutoDraw(False)
        
        # *text2* updates
        if t >= 1.0 and text2.status == NOT_STARTED:
            # keep track of start time/frame for later
            text2.tStart = t
            text2.frameNStart = frameN  # exact frame index
            text2.setAutoDraw(True)
        frameRemains = 1.0 + 1.0- win.monitorFramePeriod * 0.75  # most of one frame period left
        if text2.status == STARTED and t >= frameRemains:
            text2.setAutoDraw(False)
        
        # *text1* updates
        if t >= 2.0 and text1.status == NOT_STARTED:
            # keep track of start time/frame for later
            text1.tStart = t
            text1.frameNStart = frameN  # exact frame index
            text1.setAutoDraw(True)
        frameRemains = 2.0 + 1.0- win.monitorFramePeriod * 0.75  # most of one frame period left
        if text1.status == STARTED and t >= frameRemains:
            text1.setAutoDraw(False)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in CountdownComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Countdown"-------
    for thisComponent in CountdownComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    
    # set up handler to look after randomisation of conditions etc
    trials = data.TrialHandler(nReps=1, method='sequential', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions('../VSTMPsychopyFiles/VSTMBlockListv1.csv', selection=SelectionList),
        seed=None, name='trials')
    thisExp.addLoop(trials)  # add the loop to the experiment
    thisTrial = trials.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
    if thisTrial != None:
        for paramName in thisTrial.keys():
            exec(paramName + '= thisTrial.' + paramName)
    
    for thisTrial in trials:
        currentLoop = trials
        thisExp.addData('StartTime', globalClock.getTime())
        # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
        if thisTrial != None:
            for paramName in thisTrial.keys():
                exec(paramName + '= thisTrial.' + paramName)
        
        # ------Prepare to start Routine "trial"-------
        t = 0
        trialClock.reset()  # clock
        frameN = -1
        continueRoutine = True
        routineTimer.add(TotalTrialTime)
        # update component parameters for each repeat
        # Generate a random set of locations
        # Create the list of possible locations
        Locations = (np.arange(0,GridCount**2,1))
        # shuffle the list
        random.shuffle(Locations)
        # pick out some
        Locations = Locations[0:Load]
        
        
        resp = event.BuilderKeyResponse()
        # keep track of which components have finished
        trialComponents = [circle, textDelay, textITI, resp]
        
        for thisComponent in trialComponents:
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        
        # -------Start Routine "trial"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = trialClock.getTime()
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            count = 0
            for y_offset in OffSet:
                for x_offset in OffSet:
                    for stim in [circle]:
                        stim.pos = [x_offset, y_offset]
                        if (count+1 in Locations):
                            stim.draw()
                        count += 1
            
            
            # ##############################################
            # Draw the circles
            
           
            win.flip()
            core.wait(StimOnTime)
            win.flip()
            
            
            t = trialClock.getTime()
            # *textDelay* updates
            if t >= StimOnTime and textDelay.status == NOT_STARTED:
                # keep track of start time/frame for later
                textDelay.tStart = t
                textDelay.frameNStart = frameN  # exact frame index
                textDelay.setAutoDraw(True)
            frameRemains = StimOnTime + RetOnTime- win.monitorFramePeriod * 0.75  # most of one frame period left
            if textDelay.status == STARTED and t >= frameRemains:
                textDelay.setAutoDraw(False)
            
            # *textProbe* updates
#            if t >= (StimOnTime+RetOnTime) and textProbe.status == NOT_STARTED:
#                # keep track of start time/frame for later
#                textProbe.tStart = t
#                textProbe.frameNStart = frameN  # exact frame index
#                textProbe.setAutoDraw(True)
#            frameRemains = (StimOnTime+RetOnTime) + ProbeOnTime- win.monitorFramePeriod * 0.75  # most of one frame period left
#            if textProbe.status == STARTED and t >= frameRemains:
#                textProbe.setAutoDraw(False)
            
            # *textITI* updates
            if t >= (StimOnTime+RetOnTime+ProbeOnTime) and textITI.status == NOT_STARTED:
                # keep track of start time/frame for later
                textITI.tStart = t
                textITI.frameNStart = frameN  # exact frame index
                textITI.setAutoDraw(True)
            frameRemains = (StimOnTime+RetOnTime)+ProbeOnTime + ITITime- win.monitorFramePeriod * 0.75  # most of one frame period left
            if textITI.status == STARTED and t >= frameRemains:
                textITI.setAutoDraw(False)
            
            # *resp* updates
            if t >= (StimOnTime+RetOnTime) and resp.status == NOT_STARTED:
                # keep track of start time/frame for later
                resp.tStart = t
                resp.frameNStart = frameN  # exact frame index
                resp.status = STARTED
                # keyboard checking is just starting
                win.callOnFlip(resp.clock.reset)  # t=0 on next screen flip
                event.clearEvents(eventType='keyboard')
            frameRemains = (StimOnTime+RetOnTime) + (ProbeOnTime+ITITime)- win.monitorFramePeriod * 0.75  # most of one frame period left
            if resp.status == STARTED and t >= frameRemains:
                resp.status = STOPPED
            if resp.status == STARTED:
                theseKeys = event.getKeys(keyList=['left', 'down'])
                
                # check for quit:
                if "escape" in theseKeys:
                    endExpNow = True
                if len(theseKeys) > 0:  # at least one key was pressed
                    resp.keys = theseKeys[-1]  # just the last key pressed
                    resp.rt = resp.clock.getTime()
                    # was this 'correct'?
                    if (resp.keys == str(corr)) or (resp.keys == corr):
                        resp.corr = 1
                    else:
                        resp.corr = 0
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in trialComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # check for quit (the Esc key)
            if endExpNow or event.getKeys(keyList=["escape"]):
                core.quit()
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "trial"-------
        for thisComponent in trialComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # check responses
        if resp.keys in ['', [], None]:  # No response was made
            resp.keys=None
            # was no response the correct answer?!
            if str(corr).lower() == 'none':
               resp.corr = 1  # correct non-response
            else:
               resp.corr = 0  # failed to respond (incorrectly)
        # store data for trials (TrialHandler)
        trials.addData('resp.keys',resp.keys)
        trials.addData('resp.corr', resp.corr)
        if resp.keys != None:  # we had a response
            trials.addData('resp.rt', resp.rt)
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
    
    # ------Prepare to start Routine "Interblock"-------
    t = 0
    InterblockClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    routineTimer.add(InterBlockTime)
    # update component parameters for each repeat
    # keep track of which components have finished
    InterblockComponents = [textInterblock]
    for thisComponent in InterblockComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "Interblock"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = InterblockClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *textInterblock* updates
        if t >= 0.0 and textInterblock.status == NOT_STARTED:
            # keep track of start time/frame for later
            textInterblock.tStart = t
            textInterblock.frameNStart = frameN  # exact frame index
            textInterblock.setAutoDraw(True)
        frameRemains = 0.0 + InterBlockTime- win.monitorFramePeriod * 0.75  # most of one frame period left
        if textInterblock.status == STARTED and t >= frameRemains:
            textInterblock.setAutoDraw(False)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in InterblockComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Interblock"-------
    for thisComponent in InterblockComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.nextEntry()
    
    ## Update the block counter
    BlockCount += 1
# completed 6 repeats of 'Blocks'

# get names of stimulus parameters
if Blocks.trialList in ([], [None], None):
    params = []
else:
    params = Blocks.trialList[0].keys()
# save data for this loop
Blocks.saveAsText(filename + 'Blocks.csv', delim=',',
    stimOut=params,
    dataOut=['n','all_mean','all_std', 'all_raw'])

# ------Prepare to start Routine "ShortDelay"-------
t = 0
ShortDelayClock.reset()  # clock
frameN = -1
continueRoutine = True
routineTimer.add(ShortDelayTime)
# update component parameters for each repeat
# keep track of which components have finished
ShortDelayComponents = [textEndDelay]
for thisComponent in ShortDelayComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "ShortDelay"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = ShortDelayClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *textEndDelay* updates
    if t >= 0.0 and textEndDelay.status == NOT_STARTED:
        # keep track of start time/frame for later
        textEndDelay.tStart = t
        textEndDelay.frameNStart = frameN  # exact frame index
        textEndDelay.setAutoDraw(True)
    frameRemains = 0.0 + ShortDelayTime- win.monitorFramePeriod * 0.75  # most of one frame period left
    if textEndDelay.status == STARTED and t >= frameRemains:
        textEndDelay.setAutoDraw(False)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in ShortDelayComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "ShortDelay"-------
for thisComponent in ShortDelayComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)

# ------Prepare to start Routine "ThankYou"-------
t = 0
ThankYouClock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
OK2 = event.BuilderKeyResponse()
# keep track of which components have finished
ThankYouComponents = [textThankYou, OK2]
for thisComponent in ThankYouComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "ThankYou"-------

while continueRoutine:
    # get current time
    t = ThankYouClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *textThankYou* updates
    if t >= 0.0 and textThankYou.status == NOT_STARTED:
        # keep track of start time/frame for later
        textThankYou.tStart = t
        textThankYou.frameNStart = frameN  # exact frame index
        textThankYou.setAutoDraw(True)
    
    # *OK2* updates
    if t >= 0.0 and OK2.status == NOT_STARTED:
        # keep track of start time/frame for later
        OK2.tStart = t
        OK2.frameNStart = frameN  # exact frame index
        OK2.status = STARTED
        # keyboard checking is just starting
        event.clearEvents(eventType='keyboard')
    if OK2.status == STARTED:
        theseKeys = event.getKeys(keyList=['q'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            # a response ends the routine
            continueRoutine = False
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in ThankYouComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "ThankYou"-------
for thisComponent in ThankYouComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "ThankYou" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

        
        
# the Routine "Thankyou" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()
# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv')
thisExp.saveAsPickle(filename)
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
