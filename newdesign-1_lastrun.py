﻿#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2023.2.2),
    on 十月 01, 2023, at 09:40
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

# --- Import packages ---
from psychopy import locale_setup
from psychopy import prefs
from psychopy import plugins
plugins.activatePlugins()
prefs.hardware['audioLib'] = 'ptb'
prefs.hardware['audioLatencyMode'] = '3'
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors, layout
from psychopy.tools import environmenttools
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER, priority)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle, choice as randchoice
import os  # handy system and path functions
import sys  # to get file system encoding

import psychopy.iohub as io
from psychopy.hardware import keyboard

# --- Setup global variables (available in all functions) ---
# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
# Store info about the experiment session
psychopyVersion = '2023.2.2'
expName = 'newdesign-1'  # from the Builder filename that created this script
expInfo = {
    'participant': '',
    'date': data.getDateStr(),  # add a simple timestamp
    'expName': expName,
    'psychopyVersion': psychopyVersion,
}


def showExpInfoDlg(expInfo):
    """
    Show participant info dialog.
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    
    Returns
    ==========
    dict
        Information about this experiment.
    """
    # temporarily remove keys which the dialog doesn't need to show
    poppedKeys = {
        'date': expInfo.pop('date', data.getDateStr()),
        'expName': expInfo.pop('expName', expName),
        'psychopyVersion': expInfo.pop('psychopyVersion', psychopyVersion),
    }
    # show participant info dialog
    dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
    if dlg.OK == False:
        core.quit()  # user pressed cancel
    # restore hidden keys
    expInfo.update(poppedKeys)
    # return expInfo
    return expInfo


def setupData(expInfo, dataDir=None):
    """
    Make an ExperimentHandler to handle trials and saving.
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    dataDir : Path, str or None
        Folder to save the data to, leave as None to create a folder in the current directory.    
    Returns
    ==========
    psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    """
    
    # data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
    if dataDir is None:
        dataDir = _thisDir
    filename = u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])
    # make sure filename is relative to dataDir
    if os.path.isabs(filename):
        dataDir = os.path.commonprefix([dataDir, filename])
        filename = os.path.relpath(filename, dataDir)
    
    # an ExperimentHandler isn't essential but helps with data saving
    thisExp = data.ExperimentHandler(
        name=expName, version='',
        extraInfo=expInfo, runtimeInfo=None,
        originPath='D:\\PSYCHOPY\\eyehand_baseline\\newdesign-1_lastrun.py',
        savePickle=True, saveWideText=True,
        dataFileName=dataDir + os.sep + filename, sortColumns='time'
    )
    thisExp.setPriority('thisRow.t', priority.CRITICAL)
    thisExp.setPriority('expName', priority.LOW)
    # return experiment handler
    return thisExp


def setupLogging(filename):
    """
    Setup a log file and tell it what level to log at.
    
    Parameters
    ==========
    filename : str or pathlib.Path
        Filename to save log file and data files as, doesn't need an extension.
    
    Returns
    ==========
    psychopy.logging.LogFile
        Text stream to receive inputs from the logging system.
    """
    # this outputs to the screen, not a file
    logging.console.setLevel(logging.EXP)
    # save a log file for detail verbose info
    logFile = logging.LogFile(filename+'.log', level=logging.EXP)
    
    return logFile


def setupWindow(expInfo=None, win=None):
    """
    Setup the Window
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    win : psychopy.visual.Window
        Window to setup - leave as None to create a new window.
    
    Returns
    ==========
    psychopy.visual.Window
        Window in which to run this experiment.
    """
    if win is None:
        # if not given a window to setup, make one
        win = visual.Window(
            size=[1920, 1080], fullscr=True, screen=0,
            winType='pyglet', allowStencil=False,
            monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
            backgroundImage='', backgroundFit='none',
            blendMode='avg', useFBO=True,
            units='cm'
        )
        if expInfo is not None:
            # store frame rate of monitor if we can measure it
            expInfo['frameRate'] = win.getActualFrameRate()
    else:
        # if we have a window, just set the attributes which are safe to set
        win.color = [0,0,0]
        win.colorSpace = 'rgb'
        win.backgroundImage = ''
        win.backgroundFit = 'none'
        win.units = 'cm'
    win.mouseVisible = False
    win.hideMessage()
    return win


def setupInputs(expInfo, thisExp, win):
    """
    Setup whatever inputs are available (mouse, keyboard, eyetracker, etc.)
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    win : psychopy.visual.Window
        Window in which to run this experiment.
    Returns
    ==========
    dict
        Dictionary of input devices by name.
    """
    # --- Setup input devices ---
    inputs = {}
    ioConfig = {}
    
    # Setup iohub keyboard
    ioConfig['Keyboard'] = dict(use_keymap='psychopy')
    
    ioSession = '1'
    if 'session' in expInfo:
        ioSession = str(expInfo['session'])
    ioServer = io.launchHubServer(window=win, **ioConfig)
    eyetracker = None
    
    # create a default keyboard (e.g. to check for escape)
    defaultKeyboard = keyboard.Keyboard(backend='iohub')
    # return inputs dict
    return {
        'ioServer': ioServer,
        'defaultKeyboard': defaultKeyboard,
        'eyetracker': eyetracker,
    }

def pauseExperiment(thisExp, inputs=None, win=None, timers=[], playbackComponents=[]):
    """
    Pause this experiment, preventing the flow from advancing to the next routine until resumed.
    
    Parameters
    ==========
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    inputs : dict
        Dictionary of input devices by name.
    win : psychopy.visual.Window
        Window for this experiment.
    timers : list, tuple
        List of timers to reset once pausing is finished.
    playbackComponents : list, tuple
        List of any components with a `pause` method which need to be paused.
    """
    # if we are not paused, do nothing
    if thisExp.status != PAUSED:
        return
    
    # pause any playback components
    for comp in playbackComponents:
        comp.pause()
    # prevent components from auto-drawing
    win.stashAutoDraw()
    # run a while loop while we wait to unpause
    while thisExp.status == PAUSED:
        # make sure we have a keyboard
        if inputs is None:
            inputs = {
                'defaultKeyboard': keyboard.Keyboard(backend='ioHub')
            }
        # check for quit (typically the Esc key)
        if inputs['defaultKeyboard'].getKeys(keyList=['escape']):
            endExperiment(thisExp, win=win, inputs=inputs)
        # flip the screen
        win.flip()
    # if stop was requested while paused, quit
    if thisExp.status == FINISHED:
        endExperiment(thisExp, inputs=inputs, win=win)
    # resume any playback components
    for comp in playbackComponents:
        comp.play()
    # restore auto-drawn components
    win.retrieveAutoDraw()
    # reset any timers
    for timer in timers:
        timer.reset()


def run(expInfo, thisExp, win, inputs, globalClock=None, thisSession=None):
    """
    Run the experiment flow.
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    psychopy.visual.Window
        Window in which to run this experiment.
    inputs : dict
        Dictionary of input devices by name.
    globalClock : psychopy.core.clock.Clock or None
        Clock to get global time from - supply None to make a new one.
    thisSession : psychopy.session.Session or None
        Handle of the Session object this experiment is being run from, if any.
    """
    # mark experiment as started
    thisExp.status = STARTED
    # make sure variables created by exec are available globally
    exec = environmenttools.setExecEnvironment(globals())
    # get device handles from dict of input devices
    ioServer = inputs['ioServer']
    defaultKeyboard = inputs['defaultKeyboard']
    eyetracker = inputs['eyetracker']
    # make sure we're running in the directory for this experiment
    os.chdir(_thisDir)
    # get filename from ExperimentHandler for convenience
    filename = thisExp.dataFileName
    frameTolerance = 0.001  # how close to onset before 'same' frame
    endExpNow = False  # flag for 'escape' or other condition => quit the exp
    # get frame duration from frame rate in expInfo
    if 'frameRate' in expInfo and expInfo['frameRate'] is not None:
        frameDur = 1.0 / round(expInfo['frameRate'])
    else:
        frameDur = 1.0 / 60.0  # could not measure, so guess
    
    # Start Code - component code to be run after the window creation
    
    # --- Initialize components for Routine "instruction_baseline" ---
    instruction_baseline_text = visual.TextStim(win=win, name='instruction_baseline_text',
        text='The green cursor represents the position of your hand movement.\n\nYou must start from the starting point in the center of the screen and move towards to hit the black target point that appears.\n\nYou should move in a straight line as fast and accurately as you can towards the target.\n\nOnce you hit the target, return to the starting point and wait for the next target to appear.\n\nClick anywhere to continue...',
        font='Open Sans',
        pos=(0, 0), height=1.0, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=1.0, 
        languageStyle='LTR',
        depth=0.0);
    instruction_baseline_mouse = event.Mouse(win=win)
    x, y = [None, None]
    instruction_baseline_mouse.mouseClock = core.Clock()
    
    # --- Initialize components for Routine "baseline" ---
    # Run 'Begin Experiment' code from code_baseline
    from psychopy.tools.coordinatetools import cart2pol
    from psychopy.tools.coordinatetools import pol2cart
    
    # 计算欧氏距离
    def euclidean_dist(vec1, vec2):
        return sqrt((vec1[0] - vec2[0])**2 + (vec1[1] - vec2[1])**2)
        
    # might change depending on which computer/screen is being used
    target_radius = 12
    # rotation angle
    angle = 30.0
    mouse_baseline = event.Mouse(win=win)
    x, y = [None, None]
    mouse_baseline.mouseClock = core.Clock()
    ring_baseline = visual.Polygon(
        win=win, name='ring_baseline',units='cm', 
        edges=50, size=[1.0, 1.0],
        ori=0.0, pos=(0, 0), anchor='center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor=None,
        opacity=1.0, depth=-2.0, interpolate=True)
    fixation_ring_baseline = visual.Polygon(
        win=win, name='fixation_ring_baseline',units='cm', 
        edges=36, size=(0.8, 0.8),
        ori=0.0, pos=(0, 0), anchor='center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
        opacity=0.0, depth=-3.0, interpolate=True)
    mouse_startpoint_ring_baseline = visual.Polygon(
        win=win, name='mouse_startpoint_ring_baseline',units='cm', 
        edges=36, size=(0.5, 0.5),
        ori=0.0, pos=[0,0], anchor='center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor='green', fillColor='green',
        opacity=0.0, depth=-4.0, interpolate=True)
    target_baseline = visual.Polygon(
        win=win, name='target_baseline',units='cm', 
        edges=36, size=(0.5, 0.5),
        ori=0.0, pos=[0,0], anchor='center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor='black', fillColor='black',
        opacity=0.0, depth=-5.0, interpolate=True)
    feedback_ring_baseline = visual.Polygon(
        win=win, name='feedback_ring_baseline',units='cm', 
        edges=36, size=(0.5, 0.5),
        ori=0.0, pos=[0,0], anchor='center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='red',
        opacity=0.0, depth=-6.0, interpolate=True)
    
    # --- Initialize components for Routine "instruction_rotation" ---
    instruction_rotation_text = visual.TextStim(win=win, name='instruction_rotation_text',
        text='Brief Rest Period\n\nIn the next trials, the green cursor still represents your hand movements, but it will appear on the screen with some deviation.\n\nAs before, you must try to hit the black target point with the green cursor. \n\n\nClick anywhere to continue the experiment...\n',
        font='Open Sans',
        pos=(0, 0), height=1.0, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    instruction_rotation_mouse = event.Mouse(win=win)
    x, y = [None, None]
    instruction_rotation_mouse.mouseClock = core.Clock()
    
    # --- Initialize components for Routine "rotation" ---
    mouse_rotation = event.Mouse(win=win)
    x, y = [None, None]
    mouse_rotation.mouseClock = core.Clock()
    ring_rotation = visual.Polygon(
        win=win, name='ring_rotation',units='cm', 
        edges=50, size=[1.0, 1.0],
        ori=0.0, pos=(0, 0), anchor='center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor=None,
        opacity=1.0, depth=-2.0, interpolate=True)
    fixation_ring_rotation = visual.Polygon(
        win=win, name='fixation_ring_rotation',units='cm', 
        edges=36, size=(0.8, 0.8),
        ori=0.0, pos=(0, 0), anchor='center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
        opacity=0.0, depth=-3.0, interpolate=True)
    mouse_startpoint_ring_rotation = visual.Polygon(
        win=win, name='mouse_startpoint_ring_rotation',units='cm', 
        edges=36, size=(0.5, 0.5),
        ori=0.0, pos=[0,0], anchor='center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor='green', fillColor='green',
        opacity=0.0, depth=-4.0, interpolate=True)
    target_rotation = visual.Polygon(
        win=win, name='target_rotation',units='cm', 
        edges=36, size=(0.5, 0.5),
        ori=0.0, pos=[0,0], anchor='center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor='black', fillColor='black',
        opacity=0.0, depth=-5.0, interpolate=True)
    feedback_ring_rotation = visual.Polygon(
        win=win, name='feedback_ring_rotation',units='cm', 
        edges=36, size=(0.5, 0.5),
        ori=0.0, pos=[0,0], anchor='center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='red',
        opacity=0.0, depth=-6.0, interpolate=True)
    
    # --- Initialize components for Routine "instruction_aftereffect" ---
    instruction_aftereffect_text = visual.TextStim(win=win, name='instruction_aftereffect_text',
        text='End of Cursor Movement Phase\n\n\nYou need to move to target points directly with your hand, without using any strategy.\n\nHowever, there will be no cursor to indicate the position of your hand movement in the next trials.\n\nClick anywhere to continue the experiment...\n',
        font='Open Sans',
        pos=(0, 0), height=1.0, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    instruction_aftereffect_mouse = event.Mouse(win=win)
    x, y = [None, None]
    instruction_aftereffect_mouse.mouseClock = core.Clock()
    
    # --- Initialize components for Routine "aftereffect" ---
    mouse_aftereffect = event.Mouse(win=win)
    x, y = [None, None]
    mouse_aftereffect.mouseClock = core.Clock()
    ring_aftereffect = visual.Polygon(
        win=win, name='ring_aftereffect',units='cm', 
        edges=50, size=[1.0, 1.0],
        ori=0.0, pos=(0, 0), anchor='center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor=None,
        opacity=1.0, depth=-2.0, interpolate=True)
    fixation_ring_aftereffect = visual.Polygon(
        win=win, name='fixation_ring_aftereffect',units='cm', 
        edges=36, size=(0.8, 0.8),
        ori=0.0, pos=(0, 0), anchor='center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
        opacity=0.0, depth=-3.0, interpolate=True)
    mouse_startpoint_ring_aftereffect = visual.Polygon(
        win=win, name='mouse_startpoint_ring_aftereffect',units='cm', 
        edges=36, size=(0.5, 0.5),
        ori=0.0, pos=[0,0], anchor='center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor='green', fillColor='green',
        opacity=0.0, depth=-4.0, interpolate=True)
    target_aftereffect = visual.Polygon(
        win=win, name='target_aftereffect',units='cm', 
        edges=36, size=(0.5, 0.5),
        ori=0.0, pos=[0,0], anchor='center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor='black', fillColor='black',
        opacity=0.0, depth=-5.0, interpolate=True)
    feedback_ring_aftereffect = visual.Polygon(
        win=win, name='feedback_ring_aftereffect',units='cm', 
        edges=36, size=(0.5, 0.5),
        ori=0.0, pos=[0,0], anchor='center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='red',
        opacity=0.0, depth=-6.0, interpolate=True)
    
    # --- Initialize components for Routine "end" ---
    text = visual.TextStim(win=win, name='text',
        text='thanks',
        font='Open Sans',
        pos=(0, 0), height=1.0, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    key_resp = keyboard.Keyboard()
    
    # create some handy timers
    if globalClock is None:
        globalClock = core.Clock()  # to track the time since experiment started
    if ioServer is not None:
        ioServer.syncClock(globalClock)
    logging.setDefaultClock(globalClock)
    routineTimer = core.Clock()  # to track time remaining of each (possibly non-slip) routine
    win.flip()  # flip window to reset last flip timer
    # store the exact time the global clock started
    expInfo['expStart'] = data.getDateStr(format='%Y-%m-%d %Hh%M.%S.%f %z', fractionalSecondDigits=6)
    
    # --- Prepare to start Routine "instruction_baseline" ---
    continueRoutine = True
    # update component parameters for each repeat
    thisExp.addData('instruction_baseline.started', globalClock.getTime())
    # setup some python lists for storing info about the instruction_baseline_mouse
    gotValidClick = False  # until a click is received
    instruction_baseline_mouse.mouseClock.reset()
    # keep track of which components have finished
    instruction_baselineComponents = [instruction_baseline_text, instruction_baseline_mouse]
    for thisComponent in instruction_baselineComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "instruction_baseline" ---
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *instruction_baseline_text* updates
        
        # if instruction_baseline_text is starting this frame...
        if instruction_baseline_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            instruction_baseline_text.frameNStart = frameN  # exact frame index
            instruction_baseline_text.tStart = t  # local t and not account for scr refresh
            instruction_baseline_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(instruction_baseline_text, 'tStartRefresh')  # time at next scr refresh
            # update status
            instruction_baseline_text.status = STARTED
            instruction_baseline_text.setAutoDraw(True)
        
        # if instruction_baseline_text is active this frame...
        if instruction_baseline_text.status == STARTED:
            # update params
            pass
        # *instruction_baseline_mouse* updates
        
        # if instruction_baseline_mouse is starting this frame...
        if instruction_baseline_mouse.status == NOT_STARTED and t >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            instruction_baseline_mouse.frameNStart = frameN  # exact frame index
            instruction_baseline_mouse.tStart = t  # local t and not account for scr refresh
            instruction_baseline_mouse.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(instruction_baseline_mouse, 'tStartRefresh')  # time at next scr refresh
            # update status
            instruction_baseline_mouse.status = STARTED
            prevButtonState = [0, 0, 0]  # if now button is down we will treat as 'new' click
        if instruction_baseline_mouse.status == STARTED:  # only update if started and not finished!
            buttons = instruction_baseline_mouse.getPressed()
            if buttons != prevButtonState:  # button state changed?
                prevButtonState = buttons
                if sum(buttons) > 0:  # state changed to a new click
                    continueRoutine = False  # end routine on response        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, inputs=inputs, win=win)
            return
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in instruction_baselineComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "instruction_baseline" ---
    for thisComponent in instruction_baselineComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData('instruction_baseline.stopped', globalClock.getTime())
    # store data for thisExp (ExperimentHandler)
    thisExp.nextEntry()
    # the Routine "instruction_baseline" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    baseline_trials = data.TrialHandler(nReps=1.0, method='sequential', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions('conditions_baseline.xlsx'),
        seed=None, name='baseline_trials')
    thisExp.addLoop(baseline_trials)  # add the loop to the experiment
    thisBaseline_trial = baseline_trials.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisBaseline_trial.rgb)
    if thisBaseline_trial != None:
        for paramName in thisBaseline_trial:
            globals()[paramName] = thisBaseline_trial[paramName]
    
    for thisBaseline_trial in baseline_trials:
        currentLoop = baseline_trials
        thisExp.timestampOnFlip(win, 'thisRow.t')
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                inputs=inputs, 
                win=win, 
                timers=[routineTimer], 
                playbackComponents=[]
        )
        # abbreviate parameter names if possible (e.g. rgb = thisBaseline_trial.rgb)
        if thisBaseline_trial != None:
            for paramName in thisBaseline_trial:
                globals()[paramName] = thisBaseline_trial[paramName]
        
        # --- Prepare to start Routine "baseline" ---
        continueRoutine = True
        # update component parameters for each repeat
        thisExp.addData('baseline.started', globalClock.getTime())
        # Run 'Begin Routine' code from code_baseline
        win.mouseVisible = False
        
        # 初始化必要的变量和标志位
        move_start = False
        feedback_start = False
        
        mouse_startpoint_time = core.Clock()  # 用于记录mouse_startpoint_ring出现的时间
        target_show_time = core.Clock()
        move_start_time = core.Clock()  # 用于记录运动开始的时间
        move_end_time = core.Clock()
        feedback_start_time = core.Clock()
        mouse_startpoint_time.reset()
        target_show_time.reset()
        move_start_time.reset()
        move_end_time.reset()
        feedback_start_time.reset()
        
        movement_frames = []  # 用于保存mouse运动的每一帧位置
        
        lastPos = mouse_baseline.getPos()
        
        # 计算ring的半径
        x_mouse, y_mouse = mouse_baseline.getPos()
        #ring_radius = euclidean_dist([fixation_ring.pos[0],fixation_ring.pos[1]], [x_mouse,y_mouse])
        ring_radius = euclidean_dist([0,0], [x_mouse,y_mouse])
        
        Ring_W = ring_radius
        Ring_H = ring_radius
        
        # feedback位置的转换
        [theta_mouse, rho_mouse] = cart2pol(x_mouse, y_mouse)
        [feedback_x, feedback_y] = pol2cart(theta_mouse, target_radius)
        
        if not move_start and not feedback_start:
            # 在此处设置ring的大小
            ring_baseline.size = (ring_radius, ring_radius)  # 设置ring的大小
        
        mouse_startpoint_ring_baseline.opacity = 0
        
        # setup some python lists for storing info about the mouse_baseline
        gotValidClick = False  # until a click is received
        mouse_baseline.mouseClock.reset()
        target_baseline.setPos([target_x, target_y])
        # keep track of which components have finished
        baselineComponents = [mouse_baseline, ring_baseline, fixation_ring_baseline, mouse_startpoint_ring_baseline, target_baseline, feedback_ring_baseline]
        for thisComponent in baselineComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "baseline" ---
        routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            # Run 'Each Frame' code from code_baseline
            # update mouse pos
            x_mouse,y_mouse = mouse_baseline.getPos()
            ring_radius = euclidean_dist([fixation_ring_baseline.pos[0],fixation_ring_baseline.pos[1]], [x_mouse,y_mouse])
            Ring_W = ring_radius
            Ring_H = ring_radius
            # save last pos
            thisPos = mouse_baseline.getPos()
            mouseDist = euclidean_dist(lastPos, thisPos)
            lastPos = thisPos
            # hide rings
            fixation_ring_baseline.opacity = 0
            ring_baseline.opacity = 0
            mouse_startpoint_ring_baseline.opacity = 0
            feedback_ring_baseline.opacity = 0
                
            ## 【before start】
            if not move_start and not feedback_start:
                # see if fixation ring shows
                if ring_radius <= 0.8:
                    fixation_ring_baseline.opacity = 1
                    ring_baseline.opacity = 0  
                    mouse_startpoint_ring_baseline.opacity = 0
                    # see if mouse_startpoint_ring shows
                    if ring_radius < 0.5:
                        mouse_startpoint_ring_baseline.opacity = 1
                    else:
                        mouse_startpoint_ring_baseline.opacity = 0
                        mouse_startpoint_time.reset()
                else:
                    ring_baseline.opacity = 1
                    fixation_ring_baseline.opacity = 0
                    mouse_startpoint_ring_baseline.opacity = 0
                
                # 判断鼠标在原点是否停留足够的时间（2s）以致于target出现
                if mouse_startpoint_ring_baseline.opacity == 1 and mouse_startpoint_time.getTime() >= 2:
                    target_baseline.opacity = 1
                    #判断movement何时开始
                    if mouseDist > 0.05:
                        move_start = 1
                        RT = target_show_time.getTime()
                    else:
                        move_start = 0
                        move_start_time.reset()
                else:
                    target_baseline.opacity = 0
                    target_show_time.reset()
            #    #判断movement何时开始
            #    if target_baseline.opacity == 1 and mouseDist > 0.1:
            #        move_start = 1
            #        RT = target_show_time.getTime()
            #    else:
            #        move_start = 0
            #        move_start_time.reset()
            
            ## move start
            if move_start == 1:
                movement_frames.append(mouse_baseline.getPos())
                target_baseline.opacity = 0
                mouse_startpoint_ring_baseline.opacity = 0
                ring_baseline.opacity = 0
                # move end
                #if mouseDist < 0.01 or move_start_time.getTime() > 2:
                if move_start_time.getTime() > 1.5:
                    move_start = 0
                    feedback_start = 1
                else:
                    move_start = 1
                    feedback_start = 0
                    move_end_time.reset()
            
            ## feedback start
            if feedback_start == 1:
                if move_end_time.getTime() >= 2:  # feedback delay暂时设为2s
                    # feedback位置的转换
                    [theta_mouse, rho_mouse] = cart2pol(x_mouse, y_mouse)
                    [feedback_x, feedback_y] = pol2cart(theta_mouse, target_radius)
                    feedback_ring_baseline.opacity = 1
                    target_baseline.opacity = 1
                else:
                    feedback_ring_baseline.opacity = 0
                    target_baseline.opacity = 0
                    feedback_start_time.reset()
                
                if feedback_ring_baseline.opacity == 1 and feedback_start_time.getTime() >= 1:  # feedback duration暂时设为1s
                    feedback_ring_baseline.opacity = 0
                    target_baseline.opacity = 0
                    continueRoutine = False
            else:
                feedback_ring_baseline.opacity = 0
            
            # *mouse_baseline* updates
            
            # if mouse_baseline is starting this frame...
            if mouse_baseline.status == NOT_STARTED and t >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                mouse_baseline.frameNStart = frameN  # exact frame index
                mouse_baseline.tStart = t  # local t and not account for scr refresh
                mouse_baseline.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(mouse_baseline, 'tStartRefresh')  # time at next scr refresh
                # update status
                mouse_baseline.status = STARTED
                prevButtonState = mouse_baseline.getPressed()  # if button is down already this ISN'T a new click
            
            # *ring_baseline* updates
            
            # if ring_baseline is starting this frame...
            if ring_baseline.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                ring_baseline.frameNStart = frameN  # exact frame index
                ring_baseline.tStart = t  # local t and not account for scr refresh
                ring_baseline.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(ring_baseline, 'tStartRefresh')  # time at next scr refresh
                # update status
                ring_baseline.status = STARTED
                ring_baseline.setAutoDraw(True)
            
            # if ring_baseline is active this frame...
            if ring_baseline.status == STARTED:
                # update params
                ring_baseline.setSize([Ring_W, Ring_H], log=False)
            
            # *fixation_ring_baseline* updates
            
            # if fixation_ring_baseline is starting this frame...
            if fixation_ring_baseline.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                fixation_ring_baseline.frameNStart = frameN  # exact frame index
                fixation_ring_baseline.tStart = t  # local t and not account for scr refresh
                fixation_ring_baseline.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(fixation_ring_baseline, 'tStartRefresh')  # time at next scr refresh
                # update status
                fixation_ring_baseline.status = STARTED
                fixation_ring_baseline.setAutoDraw(True)
            
            # if fixation_ring_baseline is active this frame...
            if fixation_ring_baseline.status == STARTED:
                # update params
                pass
            
            # *mouse_startpoint_ring_baseline* updates
            
            # if mouse_startpoint_ring_baseline is starting this frame...
            if mouse_startpoint_ring_baseline.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                mouse_startpoint_ring_baseline.frameNStart = frameN  # exact frame index
                mouse_startpoint_ring_baseline.tStart = t  # local t and not account for scr refresh
                mouse_startpoint_ring_baseline.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(mouse_startpoint_ring_baseline, 'tStartRefresh')  # time at next scr refresh
                # update status
                mouse_startpoint_ring_baseline.status = STARTED
                mouse_startpoint_ring_baseline.setAutoDraw(True)
            
            # if mouse_startpoint_ring_baseline is active this frame...
            if mouse_startpoint_ring_baseline.status == STARTED:
                # update params
                mouse_startpoint_ring_baseline.setPos([x_mouse,y_mouse], log=False)
            
            # *target_baseline* updates
            
            # if target_baseline is starting this frame...
            if target_baseline.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                target_baseline.frameNStart = frameN  # exact frame index
                target_baseline.tStart = t  # local t and not account for scr refresh
                target_baseline.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(target_baseline, 'tStartRefresh')  # time at next scr refresh
                # update status
                target_baseline.status = STARTED
                target_baseline.setAutoDraw(True)
            
            # if target_baseline is active this frame...
            if target_baseline.status == STARTED:
                # update params
                pass
            
            # *feedback_ring_baseline* updates
            
            # if feedback_ring_baseline is starting this frame...
            if feedback_ring_baseline.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                feedback_ring_baseline.frameNStart = frameN  # exact frame index
                feedback_ring_baseline.tStart = t  # local t and not account for scr refresh
                feedback_ring_baseline.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(feedback_ring_baseline, 'tStartRefresh')  # time at next scr refresh
                # update status
                feedback_ring_baseline.status = STARTED
                feedback_ring_baseline.setAutoDraw(True)
            
            # if feedback_ring_baseline is active this frame...
            if feedback_ring_baseline.status == STARTED:
                # update params
                feedback_ring_baseline.setPos([feedback_x, feedback_y], log=False)
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, inputs=inputs, win=win)
                return
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in baselineComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "baseline" ---
        for thisComponent in baselineComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        thisExp.addData('baseline.stopped', globalClock.getTime())
        # Run 'End Routine' code from code_baseline
        thisExp.addData('RT', RT)
        thisExp.addData('movement_frames', movement_frames)
        # store data for baseline_trials (TrialHandler)
        # the Routine "baseline" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
        if thisSession is not None:
            # if running in a Session with a Liaison client, send data up to now
            thisSession.sendExperimentData()
    # completed 1.0 repeats of 'baseline_trials'
    
    
    # --- Prepare to start Routine "instruction_rotation" ---
    continueRoutine = True
    # update component parameters for each repeat
    thisExp.addData('instruction_rotation.started', globalClock.getTime())
    # setup some python lists for storing info about the instruction_rotation_mouse
    gotValidClick = False  # until a click is received
    instruction_rotation_mouse.mouseClock.reset()
    # keep track of which components have finished
    instruction_rotationComponents = [instruction_rotation_text, instruction_rotation_mouse]
    for thisComponent in instruction_rotationComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "instruction_rotation" ---
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *instruction_rotation_text* updates
        
        # if instruction_rotation_text is starting this frame...
        if instruction_rotation_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            instruction_rotation_text.frameNStart = frameN  # exact frame index
            instruction_rotation_text.tStart = t  # local t and not account for scr refresh
            instruction_rotation_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(instruction_rotation_text, 'tStartRefresh')  # time at next scr refresh
            # update status
            instruction_rotation_text.status = STARTED
            instruction_rotation_text.setAutoDraw(True)
        
        # if instruction_rotation_text is active this frame...
        if instruction_rotation_text.status == STARTED:
            # update params
            pass
        # *instruction_rotation_mouse* updates
        
        # if instruction_rotation_mouse is starting this frame...
        if instruction_rotation_mouse.status == NOT_STARTED and t >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            instruction_rotation_mouse.frameNStart = frameN  # exact frame index
            instruction_rotation_mouse.tStart = t  # local t and not account for scr refresh
            instruction_rotation_mouse.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(instruction_rotation_mouse, 'tStartRefresh')  # time at next scr refresh
            # update status
            instruction_rotation_mouse.status = STARTED
            prevButtonState = instruction_rotation_mouse.getPressed()  # if button is down already this ISN'T a new click
        if instruction_rotation_mouse.status == STARTED:  # only update if started and not finished!
            buttons = instruction_rotation_mouse.getPressed()
            if buttons != prevButtonState:  # button state changed?
                prevButtonState = buttons
                if sum(buttons) > 0:  # state changed to a new click
                    continueRoutine = False  # end routine on response        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, inputs=inputs, win=win)
            return
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in instruction_rotationComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "instruction_rotation" ---
    for thisComponent in instruction_rotationComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData('instruction_rotation.stopped', globalClock.getTime())
    # store data for thisExp (ExperimentHandler)
    thisExp.nextEntry()
    # the Routine "instruction_rotation" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    rotation_trials = data.TrialHandler(nReps=1.0, method='sequential', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions('conditions_rotation.xlsx'),
        seed=None, name='rotation_trials')
    thisExp.addLoop(rotation_trials)  # add the loop to the experiment
    thisRotation_trial = rotation_trials.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisRotation_trial.rgb)
    if thisRotation_trial != None:
        for paramName in thisRotation_trial:
            globals()[paramName] = thisRotation_trial[paramName]
    
    for thisRotation_trial in rotation_trials:
        currentLoop = rotation_trials
        thisExp.timestampOnFlip(win, 'thisRow.t')
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                inputs=inputs, 
                win=win, 
                timers=[routineTimer], 
                playbackComponents=[]
        )
        # abbreviate parameter names if possible (e.g. rgb = thisRotation_trial.rgb)
        if thisRotation_trial != None:
            for paramName in thisRotation_trial:
                globals()[paramName] = thisRotation_trial[paramName]
        
        # --- Prepare to start Routine "rotation" ---
        continueRoutine = True
        # update component parameters for each repeat
        thisExp.addData('rotation.started', globalClock.getTime())
        # Run 'Begin Routine' code from code_rotation
        win.mouseVisible = False
        
        # 初始化必要的变量和标志位
        move_start = False
        feedback_start = False
        
        mouse_startpoint_time = core.Clock()  # 用于记录mouse_startpoint_ring出现的时间
        target_show_time = core.Clock()
        move_start_time = core.Clock()  # 用于记录运动开始的时间
        move_end_time = core.Clock()
        feedback_start_time = core.Clock()
        mouse_startpoint_time.reset()
        target_show_time.reset()
        move_start_time.reset()
        move_end_time.reset()
        feedback_start_time.reset()
        
        movement_frames = []  # 用于保存mouse运动的每一帧位置
        
        lastPos = mouse_rotation.getPos()
        
        # 计算ring的半径
        x_mouse,y_mouse = mouse_rotation.getPos()
        #ring_radius = euclidean_dist([fixation_ring.pos[0],fixation_ring.pos[1]], [x_mouse,y_mouse])
        ring_radius = euclidean_dist([0,0], [x_mouse,y_mouse])
        
        Ring_W = ring_radius
        Ring_H = ring_radius
        # feedback位置的转换
        [theta_mouse, rho_mouse] = cart2pol(x_mouse, y_mouse)
        [feedback_x, feedback_y] = pol2cart(theta_mouse - angle, target_radius)
        
        if not move_start and not feedback_start:
            # 在此处设置ring的大小
            ring_rotation.size = (ring_radius, ring_radius)  # 设置ring的大小
        
        mouse_startpoint_ring_rotation.opacity = 0
        # setup some python lists for storing info about the mouse_rotation
        gotValidClick = False  # until a click is received
        mouse_rotation.mouseClock.reset()
        target_rotation.setPos([target_x, target_y])
        # keep track of which components have finished
        rotationComponents = [mouse_rotation, ring_rotation, fixation_ring_rotation, mouse_startpoint_ring_rotation, target_rotation, feedback_ring_rotation]
        for thisComponent in rotationComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "rotation" ---
        routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            # Run 'Each Frame' code from code_rotation
            x_mouse,y_mouse = mouse_rotation.getPos()
            ring_radius = euclidean_dist([fixation_ring_rotation.pos[0],fixation_ring_rotation.pos[1]], [x_mouse,y_mouse])
            Ring_W = ring_radius
            Ring_H = ring_radius
            
            thisPos = mouse_rotation.getPos()
            mouseDist = euclidean_dist(lastPos, thisPos)
            lastPos = thisPos
            
            fixation_ring_rotation.opacity = 0
            ring_rotation.opacity = 0
            mouse_startpoint_ring_rotation.opacity = 0
            feedback_ring_rotation.opacity = 0
                
            ## 【before start】
            if not move_start and not feedback_start:
                
                # 判断是否该出现fixation ring
                if ring_radius <= 0.8:
                    fixation_ring_rotation.opacity = 1
                    ring_rotation.opacity = 0  # 隐藏ring
                    mouse_startpoint_ring_rotation.opacity = 0
                    # 判断是否该出现mouse_startpoint_ring
                    if ring_radius < 0.5:
                        mouse_startpoint_ring_rotation.opacity = 1
                    else:
                        mouse_startpoint_ring_rotation.opacity = 0
                        mouse_startpoint_time.reset()
                else:
                    ring_rotation.opacity = 1
                    fixation_ring_rotation.opacity = 0
                    mouse_startpoint_ring_rotation.opacity = 0
                
                # 判断鼠标在原点是否停留足够的时间（2s）以致于target出现
                if mouse_startpoint_ring_rotation.opacity == 1 and mouse_startpoint_time.getTime() >= 2:
                    target_rotation.opacity = 1
                    # 判断movement何时开始
                    if mouseDist > 0.05:
                        move_start = 1
                        RT = target_show_time.getTime()
                    else:
                        move_start = 0
                        move_start_time.reset()
                else:
                    target_rotation.opacity = 0
                    target_show_time.reset()
            
            ## move start
            if move_start == 1:
                movement_frames.append(mouse_rotation.getPos())
                
                target_rotation.opacity = 0
                mouse_startpoint_ring_rotation.opacity = 0
                ring_rotation.opacity = 0
                # move end
                #if mouseDist < 0.01 or move_start_time.getTime() > 2:
                if move_start_time.getTime() > 1.5:
                    move_start = 0
                    feedback_start = 1
                else:
                    move_start = 1
                    feedback_start = 0
                    move_end_time.reset()
            
            ## feedback start
            if feedback_start == 1:
                if move_end_time.getTime() >= 2:  # feedback delay暂时设为2s
                    # feedback位置的转换
                    [theta_mouse, rho_mouse] = cart2pol(x_mouse, y_mouse)
                    [feedback_x, feedback_y] = pol2cart(theta_mouse - angle, target_radius)
                    feedback_ring_rotation.opacity = 1
                    target_rotation.opacity = 1
                else:
                    feedback_ring_rotation.opacity = 0
                    target_rotation.opacity = 0
                    feedback_start_time.reset()
                
                if feedback_ring_rotation.opacity == 1 and feedback_start_time.getTime() >= 1:  # feedback duration暂时设为1s
                    feedback_ring_rotation.opacity = 0
                    target_rotation.opacity = 0
                    continueRoutine = False
            else:
                feedback_ring_rotation.opacity = 0
            
            # *mouse_rotation* updates
            
            # if mouse_rotation is starting this frame...
            if mouse_rotation.status == NOT_STARTED and t >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                mouse_rotation.frameNStart = frameN  # exact frame index
                mouse_rotation.tStart = t  # local t and not account for scr refresh
                mouse_rotation.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(mouse_rotation, 'tStartRefresh')  # time at next scr refresh
                # update status
                mouse_rotation.status = STARTED
                prevButtonState = mouse_rotation.getPressed()  # if button is down already this ISN'T a new click
            
            # *ring_rotation* updates
            
            # if ring_rotation is starting this frame...
            if ring_rotation.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                ring_rotation.frameNStart = frameN  # exact frame index
                ring_rotation.tStart = t  # local t and not account for scr refresh
                ring_rotation.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(ring_rotation, 'tStartRefresh')  # time at next scr refresh
                # update status
                ring_rotation.status = STARTED
                ring_rotation.setAutoDraw(True)
            
            # if ring_rotation is active this frame...
            if ring_rotation.status == STARTED:
                # update params
                ring_rotation.setSize([Ring_W, Ring_H], log=False)
            
            # *fixation_ring_rotation* updates
            
            # if fixation_ring_rotation is starting this frame...
            if fixation_ring_rotation.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                fixation_ring_rotation.frameNStart = frameN  # exact frame index
                fixation_ring_rotation.tStart = t  # local t and not account for scr refresh
                fixation_ring_rotation.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(fixation_ring_rotation, 'tStartRefresh')  # time at next scr refresh
                # update status
                fixation_ring_rotation.status = STARTED
                fixation_ring_rotation.setAutoDraw(True)
            
            # if fixation_ring_rotation is active this frame...
            if fixation_ring_rotation.status == STARTED:
                # update params
                pass
            
            # *mouse_startpoint_ring_rotation* updates
            
            # if mouse_startpoint_ring_rotation is starting this frame...
            if mouse_startpoint_ring_rotation.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                mouse_startpoint_ring_rotation.frameNStart = frameN  # exact frame index
                mouse_startpoint_ring_rotation.tStart = t  # local t and not account for scr refresh
                mouse_startpoint_ring_rotation.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(mouse_startpoint_ring_rotation, 'tStartRefresh')  # time at next scr refresh
                # update status
                mouse_startpoint_ring_rotation.status = STARTED
                mouse_startpoint_ring_rotation.setAutoDraw(True)
            
            # if mouse_startpoint_ring_rotation is active this frame...
            if mouse_startpoint_ring_rotation.status == STARTED:
                # update params
                mouse_startpoint_ring_rotation.setPos([x_mouse, y_mouse], log=False)
            
            # *target_rotation* updates
            
            # if target_rotation is starting this frame...
            if target_rotation.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                target_rotation.frameNStart = frameN  # exact frame index
                target_rotation.tStart = t  # local t and not account for scr refresh
                target_rotation.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(target_rotation, 'tStartRefresh')  # time at next scr refresh
                # update status
                target_rotation.status = STARTED
                target_rotation.setAutoDraw(True)
            
            # if target_rotation is active this frame...
            if target_rotation.status == STARTED:
                # update params
                pass
            
            # *feedback_ring_rotation* updates
            
            # if feedback_ring_rotation is starting this frame...
            if feedback_ring_rotation.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                feedback_ring_rotation.frameNStart = frameN  # exact frame index
                feedback_ring_rotation.tStart = t  # local t and not account for scr refresh
                feedback_ring_rotation.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(feedback_ring_rotation, 'tStartRefresh')  # time at next scr refresh
                # update status
                feedback_ring_rotation.status = STARTED
                feedback_ring_rotation.setAutoDraw(True)
            
            # if feedback_ring_rotation is active this frame...
            if feedback_ring_rotation.status == STARTED:
                # update params
                feedback_ring_rotation.setPos([feedback_x, feedback_y], log=False)
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, inputs=inputs, win=win)
                return
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in rotationComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "rotation" ---
        for thisComponent in rotationComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        thisExp.addData('rotation.stopped', globalClock.getTime())
        # Run 'End Routine' code from code_rotation
        thisExp.addData('RT', RT)
        thisExp.addData('movement_frames', movement_frames)
        # store data for rotation_trials (TrialHandler)
        # the Routine "rotation" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
        if thisSession is not None:
            # if running in a Session with a Liaison client, send data up to now
            thisSession.sendExperimentData()
    # completed 1.0 repeats of 'rotation_trials'
    
    
    # --- Prepare to start Routine "instruction_aftereffect" ---
    continueRoutine = True
    # update component parameters for each repeat
    thisExp.addData('instruction_aftereffect.started', globalClock.getTime())
    # setup some python lists for storing info about the instruction_aftereffect_mouse
    gotValidClick = False  # until a click is received
    instruction_aftereffect_mouse.mouseClock.reset()
    # keep track of which components have finished
    instruction_aftereffectComponents = [instruction_aftereffect_text, instruction_aftereffect_mouse]
    for thisComponent in instruction_aftereffectComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "instruction_aftereffect" ---
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *instruction_aftereffect_text* updates
        
        # if instruction_aftereffect_text is starting this frame...
        if instruction_aftereffect_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            instruction_aftereffect_text.frameNStart = frameN  # exact frame index
            instruction_aftereffect_text.tStart = t  # local t and not account for scr refresh
            instruction_aftereffect_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(instruction_aftereffect_text, 'tStartRefresh')  # time at next scr refresh
            # update status
            instruction_aftereffect_text.status = STARTED
            instruction_aftereffect_text.setAutoDraw(True)
        
        # if instruction_aftereffect_text is active this frame...
        if instruction_aftereffect_text.status == STARTED:
            # update params
            pass
        # *instruction_aftereffect_mouse* updates
        
        # if instruction_aftereffect_mouse is starting this frame...
        if instruction_aftereffect_mouse.status == NOT_STARTED and t >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            instruction_aftereffect_mouse.frameNStart = frameN  # exact frame index
            instruction_aftereffect_mouse.tStart = t  # local t and not account for scr refresh
            instruction_aftereffect_mouse.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(instruction_aftereffect_mouse, 'tStartRefresh')  # time at next scr refresh
            # update status
            instruction_aftereffect_mouse.status = STARTED
            prevButtonState = instruction_aftereffect_mouse.getPressed()  # if button is down already this ISN'T a new click
        if instruction_aftereffect_mouse.status == STARTED:  # only update if started and not finished!
            buttons = instruction_aftereffect_mouse.getPressed()
            if buttons != prevButtonState:  # button state changed?
                prevButtonState = buttons
                if sum(buttons) > 0:  # state changed to a new click
                    continueRoutine = False  # end routine on response        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, inputs=inputs, win=win)
            return
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in instruction_aftereffectComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "instruction_aftereffect" ---
    for thisComponent in instruction_aftereffectComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData('instruction_aftereffect.stopped', globalClock.getTime())
    # store data for thisExp (ExperimentHandler)
    thisExp.nextEntry()
    # the Routine "instruction_aftereffect" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    aftereffect_trials = data.TrialHandler(nReps=1.0, method='sequential', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions('conditions_aftereffect.xlsx'),
        seed=None, name='aftereffect_trials')
    thisExp.addLoop(aftereffect_trials)  # add the loop to the experiment
    thisAftereffect_trial = aftereffect_trials.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisAftereffect_trial.rgb)
    if thisAftereffect_trial != None:
        for paramName in thisAftereffect_trial:
            globals()[paramName] = thisAftereffect_trial[paramName]
    
    for thisAftereffect_trial in aftereffect_trials:
        currentLoop = aftereffect_trials
        thisExp.timestampOnFlip(win, 'thisRow.t')
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                inputs=inputs, 
                win=win, 
                timers=[routineTimer], 
                playbackComponents=[]
        )
        # abbreviate parameter names if possible (e.g. rgb = thisAftereffect_trial.rgb)
        if thisAftereffect_trial != None:
            for paramName in thisAftereffect_trial:
                globals()[paramName] = thisAftereffect_trial[paramName]
        
        # --- Prepare to start Routine "aftereffect" ---
        continueRoutine = True
        # update component parameters for each repeat
        thisExp.addData('aftereffect.started', globalClock.getTime())
        # Run 'Begin Routine' code from code_aftereffect
        win.mouseVisible = False
        
        # 初始化必要的变量和标志位
        move_start = False
        feedback_start = False
        
        mouse_startpoint_time = core.Clock()  # 用于记录mouse_startpoint_ring出现的时间
        target_show_time = core.Clock()
        move_start_time = core.Clock()  # 用于记录运动开始的时间
        move_end_time = core.Clock()
        feedback_start_time = core.Clock()
        mouse_startpoint_time.reset()
        target_show_time.reset()
        move_start_time.reset()
        move_end_time.reset()
        feedback_start_time.reset()
        
        movement_frames = []  # 用于保存mouse运动的每一帧位置
        
        lastPos = mouse_aftereffect.getPos()
        
        # 计算ring的半径
        x_mouse,y_mouse = mouse_aftereffect.getPos()
        #ring_radius = euclidean_dist([fixation_ring.pos[0],fixation_ring.pos[1]], [x_mouse,y_mouse])
        ring_radius = euclidean_dist([0,0], [x_mouse,y_mouse])
        
        Ring_W = ring_radius
        Ring_H = ring_radius
        # feedback位置的转换
        [theta_mouse, rho_mouse] = cart2pol(x_mouse, y_mouse)
        [feedback_x, feedback_y] = pol2cart(theta_mouse, target_radius)
        
        if not move_start and not feedback_start:
            # 在此处设置ring的大小
            ring_aftereffect.size = (ring_radius, ring_radius)  # 设置ring的大小
        
        mouse_startpoint_ring_aftereffect.opacity = 0
        # setup some python lists for storing info about the mouse_aftereffect
        gotValidClick = False  # until a click is received
        mouse_aftereffect.mouseClock.reset()
        target_aftereffect.setPos([target_x, target_y])
        # keep track of which components have finished
        aftereffectComponents = [mouse_aftereffect, ring_aftereffect, fixation_ring_aftereffect, mouse_startpoint_ring_aftereffect, target_aftereffect, feedback_ring_aftereffect]
        for thisComponent in aftereffectComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "aftereffect" ---
        routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            # Run 'Each Frame' code from code_aftereffect
            x_mouse,y_mouse = mouse_aftereffect.getPos()
            ring_radius = euclidean_dist([fixation_ring_aftereffect.pos[0],fixation_ring_aftereffect.pos[1]], [x_mouse,y_mouse])
            Ring_W = ring_radius
            Ring_H = ring_radius
            
            thisPos = mouse_aftereffect.getPos()
            mouseDist = euclidean_dist(lastPos, thisPos)
            lastPos = thisPos
            
            fixation_ring_aftereffect.opacity = 0
            ring_aftereffect.opacity = 0
            mouse_startpoint_ring_aftereffect.opacity = 0
            feedback_ring_aftereffect.opacity = 0
                
            ## 【before start】
            if not move_start and not feedback_start:
                
                # 判断是否该出现fixation ring
                if ring_radius <= 0.8:
                    fixation_ring_aftereffect.opacity = 1
                    ring_aftereffect.opacity = 0  # 隐藏ring
                    mouse_startpoint_ring_aftereffect.opacity = 0
                    # 判断是否该出现mouse_startpoint_ring
                    if ring_radius < 0.5:
                        mouse_startpoint_ring_aftereffect.opacity = 1
                    else:
                        mouse_startpoint_ring_aftereffect.opacity = 0
                        mouse_startpoint_time.reset()
                else:
                    ring_aftereffect.opacity = 1
                    fixation_ring_aftereffect.opacity = 0
                    mouse_startpoint_ring_aftereffect.opacity = 0
                
                # 判断鼠标在原点是否停留足够的时间（2s）以致于target出现
                if mouse_startpoint_ring_aftereffect.opacity == 1 and mouse_startpoint_time.getTime() >= 2:
                    target_aftereffect.opacity = 1
                else:
                    target_aftereffect.opacity = 0
                    target_show_time.reset()
                #判断movement何时开始
                if target_aftereffect.opacity == 1 and mouseDist > 0.05:
                    move_start = 1
                    RT = target_show_time.getTime()
                else:
                    move_start = 0
                    move_start_time.reset()
            
            ## move start
            if move_start == 1:
                movement_frames.append(mouse_aftereffect.getPos())
                
                target_aftereffect.opacity = 0
                mouse_startpoint_ring_aftereffect.opacity = 0
                ring_aftereffect.opacity = 0
                # move end
                #if mouseDist < 0.01 or move_start_time.getTime() > 2:
                if move_start_time.getTime() > 1.5:
                    move_start = 0
                    feedback_start = 1
                else:
                    move_start = 1
                    feedback_start = 0
                    move_end_time.reset()
            
            ## feedback start
            if feedback_start == 1:
                if move_end_time.getTime() >= 2:  # feedback delay暂时设为2s
                    target_aftereffect.opacity = 1
                else:
                    feedback_ring_aftereffect.opacity = 0
                    target_aftereffect.opacity = 0
                    feedback_start_time.reset()
                if target_aftereffect.opacity == 1 and feedback_start_time.getTime() >= 1:  # feedback duration暂时设为1s
                    feedback_ring_aftereffect.opacity = 0
                    target_aftereffect.opacity = 0
                    continueRoutine = False
            else:
                feedback_ring_aftereffect.opacity = 0
            
            # *mouse_aftereffect* updates
            
            # if mouse_aftereffect is starting this frame...
            if mouse_aftereffect.status == NOT_STARTED and t >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                mouse_aftereffect.frameNStart = frameN  # exact frame index
                mouse_aftereffect.tStart = t  # local t and not account for scr refresh
                mouse_aftereffect.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(mouse_aftereffect, 'tStartRefresh')  # time at next scr refresh
                # update status
                mouse_aftereffect.status = STARTED
                prevButtonState = mouse_aftereffect.getPressed()  # if button is down already this ISN'T a new click
            
            # *ring_aftereffect* updates
            
            # if ring_aftereffect is starting this frame...
            if ring_aftereffect.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                ring_aftereffect.frameNStart = frameN  # exact frame index
                ring_aftereffect.tStart = t  # local t and not account for scr refresh
                ring_aftereffect.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(ring_aftereffect, 'tStartRefresh')  # time at next scr refresh
                # update status
                ring_aftereffect.status = STARTED
                ring_aftereffect.setAutoDraw(True)
            
            # if ring_aftereffect is active this frame...
            if ring_aftereffect.status == STARTED:
                # update params
                ring_aftereffect.setSize([Ring_W, Ring_H], log=False)
            
            # *fixation_ring_aftereffect* updates
            
            # if fixation_ring_aftereffect is starting this frame...
            if fixation_ring_aftereffect.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                fixation_ring_aftereffect.frameNStart = frameN  # exact frame index
                fixation_ring_aftereffect.tStart = t  # local t and not account for scr refresh
                fixation_ring_aftereffect.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(fixation_ring_aftereffect, 'tStartRefresh')  # time at next scr refresh
                # update status
                fixation_ring_aftereffect.status = STARTED
                fixation_ring_aftereffect.setAutoDraw(True)
            
            # if fixation_ring_aftereffect is active this frame...
            if fixation_ring_aftereffect.status == STARTED:
                # update params
                pass
            
            # *mouse_startpoint_ring_aftereffect* updates
            
            # if mouse_startpoint_ring_aftereffect is starting this frame...
            if mouse_startpoint_ring_aftereffect.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                mouse_startpoint_ring_aftereffect.frameNStart = frameN  # exact frame index
                mouse_startpoint_ring_aftereffect.tStart = t  # local t and not account for scr refresh
                mouse_startpoint_ring_aftereffect.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(mouse_startpoint_ring_aftereffect, 'tStartRefresh')  # time at next scr refresh
                # update status
                mouse_startpoint_ring_aftereffect.status = STARTED
                mouse_startpoint_ring_aftereffect.setAutoDraw(True)
            
            # if mouse_startpoint_ring_aftereffect is active this frame...
            if mouse_startpoint_ring_aftereffect.status == STARTED:
                # update params
                mouse_startpoint_ring_aftereffect.setPos([x_mouse, y_mouse], log=False)
            
            # *target_aftereffect* updates
            
            # if target_aftereffect is starting this frame...
            if target_aftereffect.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                target_aftereffect.frameNStart = frameN  # exact frame index
                target_aftereffect.tStart = t  # local t and not account for scr refresh
                target_aftereffect.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(target_aftereffect, 'tStartRefresh')  # time at next scr refresh
                # update status
                target_aftereffect.status = STARTED
                target_aftereffect.setAutoDraw(True)
            
            # if target_aftereffect is active this frame...
            if target_aftereffect.status == STARTED:
                # update params
                pass
            
            # *feedback_ring_aftereffect* updates
            
            # if feedback_ring_aftereffect is starting this frame...
            if feedback_ring_aftereffect.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                feedback_ring_aftereffect.frameNStart = frameN  # exact frame index
                feedback_ring_aftereffect.tStart = t  # local t and not account for scr refresh
                feedback_ring_aftereffect.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(feedback_ring_aftereffect, 'tStartRefresh')  # time at next scr refresh
                # update status
                feedback_ring_aftereffect.status = STARTED
                feedback_ring_aftereffect.setAutoDraw(True)
            
            # if feedback_ring_aftereffect is active this frame...
            if feedback_ring_aftereffect.status == STARTED:
                # update params
                feedback_ring_aftereffect.setPos([feedback_x, feedback_y], log=False)
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, inputs=inputs, win=win)
                return
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in aftereffectComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "aftereffect" ---
        for thisComponent in aftereffectComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        thisExp.addData('aftereffect.stopped', globalClock.getTime())
        # Run 'End Routine' code from code_aftereffect
        thisExp.addData('RT', RT)
        thisExp.addData('movement_frames', movement_frames)
        # store data for aftereffect_trials (TrialHandler)
        # the Routine "aftereffect" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
        if thisSession is not None:
            # if running in a Session with a Liaison client, send data up to now
            thisSession.sendExperimentData()
    # completed 1.0 repeats of 'aftereffect_trials'
    
    
    # --- Prepare to start Routine "end" ---
    continueRoutine = True
    # update component parameters for each repeat
    thisExp.addData('end.started', globalClock.getTime())
    key_resp.keys = []
    key_resp.rt = []
    _key_resp_allKeys = []
    # keep track of which components have finished
    endComponents = [text, key_resp]
    for thisComponent in endComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "end" ---
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text* updates
        
        # if text is starting this frame...
        if text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text.frameNStart = frameN  # exact frame index
            text.tStart = t  # local t and not account for scr refresh
            text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text, 'tStartRefresh')  # time at next scr refresh
            # update status
            text.status = STARTED
            text.setAutoDraw(True)
        
        # if text is active this frame...
        if text.status == STARTED:
            # update params
            pass
        
        # *key_resp* updates
        
        # if key_resp is starting this frame...
        if key_resp.status == NOT_STARTED and t >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp.frameNStart = frameN  # exact frame index
            key_resp.tStart = t  # local t and not account for scr refresh
            key_resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp, 'tStartRefresh')  # time at next scr refresh
            # update status
            key_resp.status = STARTED
            # keyboard checking is just starting
            key_resp.clock.reset()  # now t=0
            key_resp.clearEvents(eventType='keyboard')
        if key_resp.status == STARTED:
            theseKeys = key_resp.getKeys(keyList=['y','n','left','right','space'], ignoreKeys=["escape"], waitRelease=False)
            _key_resp_allKeys.extend(theseKeys)
            if len(_key_resp_allKeys):
                key_resp.keys = _key_resp_allKeys[-1].name  # just the last key pressed
                key_resp.rt = _key_resp_allKeys[-1].rt
                key_resp.duration = _key_resp_allKeys[-1].duration
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, inputs=inputs, win=win)
            return
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in endComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "end" ---
    for thisComponent in endComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData('end.stopped', globalClock.getTime())
    # the Routine "end" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # mark experiment as finished
    endExperiment(thisExp, win=win, inputs=inputs)


def saveData(thisExp):
    """
    Save data from this experiment
    
    Parameters
    ==========
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    """
    filename = thisExp.dataFileName
    # these shouldn't be strictly necessary (should auto-save)
    thisExp.saveAsWideText(filename + '.csv', delim='auto')
    thisExp.saveAsPickle(filename)


def endExperiment(thisExp, inputs=None, win=None):
    """
    End this experiment, performing final shut down operations.
    
    This function does NOT close the window or end the Python process - use `quit` for this.
    
    Parameters
    ==========
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    inputs : dict
        Dictionary of input devices by name.
    win : psychopy.visual.Window
        Window for this experiment.
    """
    if win is not None:
        # remove autodraw from all current components
        win.clearAutoDraw()
        # Flip one final time so any remaining win.callOnFlip() 
        # and win.timeOnFlip() tasks get executed
        win.flip()
    # mark experiment handler as finished
    thisExp.status = FINISHED
    # shut down eyetracker, if there is one
    if inputs is not None:
        if 'eyetracker' in inputs and inputs['eyetracker'] is not None:
            inputs['eyetracker'].setConnectionState(False)
    logging.flush()


def quit(thisExp, win=None, inputs=None, thisSession=None):
    """
    Fully quit, closing the window and ending the Python process.
    
    Parameters
    ==========
    win : psychopy.visual.Window
        Window to close.
    inputs : dict
        Dictionary of input devices by name.
    thisSession : psychopy.session.Session or None
        Handle of the Session object this experiment is being run from, if any.
    """
    thisExp.abort()  # or data files will save again on exit
    # make sure everything is closed down
    if win is not None:
        # Flip one final time so any remaining win.callOnFlip() 
        # and win.timeOnFlip() tasks get executed before quitting
        win.flip()
        win.close()
    if inputs is not None:
        if 'eyetracker' in inputs and inputs['eyetracker'] is not None:
            inputs['eyetracker'].setConnectionState(False)
    logging.flush()
    if thisSession is not None:
        thisSession.stop()
    # terminate Python process
    core.quit()


# if running this experiment as a script...
if __name__ == '__main__':
    # call all functions in order
    expInfo = showExpInfoDlg(expInfo=expInfo)
    thisExp = setupData(expInfo=expInfo)
    logFile = setupLogging(filename=thisExp.dataFileName)
    win = setupWindow(expInfo=expInfo)
    inputs = setupInputs(expInfo=expInfo, thisExp=thisExp, win=win)
    run(
        expInfo=expInfo, 
        thisExp=thisExp, 
        win=win, 
        inputs=inputs
    )
    saveData(thisExp=thisExp)
    quit(thisExp=thisExp, win=win, inputs=inputs)
