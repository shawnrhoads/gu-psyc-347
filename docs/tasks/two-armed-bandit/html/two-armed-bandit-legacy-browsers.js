/************************* 
 * Two-Armed-Bandit Test *
 *************************/

// init psychoJS:
const psychoJS = new PsychoJS({
  debug: true
});

// open window:
psychoJS.openWindow({
  fullscr: true,
  color: new util.Color('black'),
  units: 'height',
  waitBlanking: true
});

// store info about the experiment session:
let expName = 'two-armed-bandit';  // from the Builder filename that created this script
let expInfo = {'participant': ''};

// schedule the experiment:
psychoJS.schedule(psychoJS.gui.DlgFromDict({
  dictionary: expInfo,
  title: expName
}));

const flowScheduler = new Scheduler(psychoJS);
const dialogCancelScheduler = new Scheduler(psychoJS);
psychoJS.scheduleCondition(function() { return (psychoJS.gui.dialogComponent.button === 'OK'); }, flowScheduler, dialogCancelScheduler);

// flowScheduler gets run if the participants presses OK
flowScheduler.add(updateInfo); // add timeStamp
flowScheduler.add(experimentInit);
flowScheduler.add(introRoutineBegin());
flowScheduler.add(introRoutineEachFrame());
flowScheduler.add(introRoutineEnd());
flowScheduler.add(instr1RoutineBegin());
flowScheduler.add(instr1RoutineEachFrame());
flowScheduler.add(instr1RoutineEnd());
flowScheduler.add(instr2RoutineBegin());
flowScheduler.add(instr2RoutineEachFrame());
flowScheduler.add(instr2RoutineEnd());
flowScheduler.add(instr3RoutineBegin());
flowScheduler.add(instr3RoutineEachFrame());
flowScheduler.add(instr3RoutineEnd());
flowScheduler.add(prac_instrRoutineBegin());
flowScheduler.add(prac_instrRoutineEachFrame());
flowScheduler.add(prac_instrRoutineEnd());
const practice_roundLoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(practice_roundLoopBegin, practice_roundLoopScheduler);
flowScheduler.add(practice_roundLoopScheduler);
flowScheduler.add(practice_roundLoopEnd);
flowScheduler.add(instr4RoutineBegin());
flowScheduler.add(instr4RoutineEachFrame());
flowScheduler.add(instr4RoutineEnd());
flowScheduler.add(exp_instrRoutineBegin());
flowScheduler.add(exp_instrRoutineEachFrame());
flowScheduler.add(exp_instrRoutineEnd());
const trialsLoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(trialsLoopBegin, trialsLoopScheduler);
flowScheduler.add(trialsLoopScheduler);
flowScheduler.add(trialsLoopEnd);
flowScheduler.add(enderRoutineBegin());
flowScheduler.add(enderRoutineEachFrame());
flowScheduler.add(enderRoutineEnd());
flowScheduler.add(quitPsychoJS, '', true);

// quit if user presses Cancel in dialog box:
dialogCancelScheduler.add(quitPsychoJS, '', false);

psychoJS.start({
  expName: expName,
  expInfo: expInfo,
  });

psychoJS.experimentLogger.setLevel(core.Logger.ServerLevel.EXP);


var frameDur;
function updateInfo() {
  expInfo['date'] = util.MonotonicClock.getDateStr();  // add a simple timestamp
  expInfo['expName'] = expName;
  expInfo['psychopyVersion'] = '2020.2.4post1';
  expInfo['OS'] = window.navigator.platform;

  // store frame rate of monitor if we can measure it successfully
  expInfo['frameRate'] = psychoJS.window.getActualFrameRate();
  if (typeof expInfo['frameRate'] !== 'undefined')
    frameDur = 1.0 / Math.round(expInfo['frameRate']);
  else
    frameDur = 1.0 / 60.0; // couldn't get a reliable measure so guess

  // add info from the URL:
  util.addInfoFromUrl(expInfo);
  
  return Scheduler.Event.NEXT;
}


var introClock;
var ptsSelf;
var ptsSocial;
var seed;
var order_file;
var key_resp_1;
var intro_text;
var thisExp;
var instr1Clock;
var instr_1;
var key_resp_2;
var instr2Clock;
var instr_2;
var key_resp_4;
var instr3Clock;
var instr_3;
var key_resp_3;
var prac_instrClock;
var read_prac;
var key_resp_7;
var BlockInstructClock;
var BlockInstr_disp;
var fixationClock;
var iti;
var stimuliClock;
var left;
var right;
var key_resp;
var stimuli_feedbackClock;
var left_feedback;
var right_feedback;
var feedbackClock;
var feedback_text;
var instr4Clock;
var instr_4;
var key_resp_8;
var exp_instrClock;
var ready_exp;
var key_resp_5;
var enderClock;
var end_heading;
var end_text;
var key_resp_6;
var text_4;
var globalClock;
var routineTimer;
function experimentInit() {
  // Initialize components for Routine "intro"
  introClock = new util.Clock();
  ptsSelf = 1000;
  ptsSocial = 1000;
  seed = Number.parseInt(expInfo["participant"]);
  order_file = `orders/sub-${expInfo["participant"]}_stim-order.csv`;
  
  key_resp_1 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  intro_text = new visual.TextStim({
    win: psychoJS.window,
    name: 'intro_text',
    text: 'In this experiment you will see two slot machines appear on the screen and you need to select one of them.\n\nBased on your choices, you can win points. Points are converted into REAL MONEY at the end of the experiment.\n\nPress SPACE to continue.',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.05,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -2.0 
  });
  
  thisExp=psychoJS.experiment;
  // Initialize components for Routine "instr1"
  instr1Clock = new util.Clock();
  instr_1 = new visual.TextStim({
    win: psychoJS.window,
    name: 'instr_1',
    text: 'Some slot machines will give you points more or less often than others. Your job is to figure out which machine is the best to choose, and select it using your arrow keys. \n\nPress SPACE to continue.',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.05,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: 0.0 
  });
  
  key_resp_2 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "instr2"
  instr2Clock = new util.Clock();
  instr_2 = new visual.TextStim({
    win: psychoJS.window,
    name: 'instr_2',
    text: 'Respond using the LEFT and RIGHT arrow keys matching whichever side the machine you choose appears. Sometimes the machine might appear on the left while other times it might appear on the right. \n\nTry to respond as quickly and accurately as possible. You have about 2 seconds to make your choice.\n\nPress SPACE to continue.',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.05,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: 0.0 
  });
  
  key_resp_4 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "instr3"
  instr3Clock = new util.Clock();
  instr_3 = new visual.TextStim({
    win: psychoJS.window,
    name: 'instr_3',
    text: 'After each choice, you will see feedback. \n\nSometimes you will win points, +100 points!\nSometimes you will not win points, 0 points\n\nPress SPACE to continue.',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.05,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: 0.0 
  });
  
  key_resp_3 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "prac_instr"
  prac_instrClock = new util.Clock();
  read_prac = new visual.TextStim({
    win: psychoJS.window,
    name: 'read_prac',
    text: 'Let’s try a few practice rounds. \n\nSometimes you will play to win points. Other times, you will play to avoid losing points. The task will tell you which condition you are in. \n\nPress SPACE to begin the practice.',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.05,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: 0.0 
  });
  
  key_resp_7 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "BlockInstruct"
  BlockInstructClock = new util.Clock();
  BlockInstr_disp = new visual.TextStim({
    win: psychoJS.window,
    name: 'BlockInstr_disp',
    text: 'default text',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.08,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -1.0 
  });
  
  // Initialize components for Routine "fixation"
  fixationClock = new util.Clock();
  iti = new visual.ShapeStim ({
    win: psychoJS.window, name: 'iti', 
    vertices: 'cross', size:[0.05, 0.05],
    ori: 0, pos: [0, 0],
    lineWidth: 1, lineColor: new util.Color([1, 1, 1]),
    fillColor: new util.Color([1, 1, 1]),
    opacity: 1, depth: 0, interpolate: true,
  });
  
  // Initialize components for Routine "stimuli"
  stimuliClock = new util.Clock();
  left = new visual.ImageStim({
    win : psychoJS.window,
    name : 'left', units : undefined, 
    image : undefined, mask : undefined,
    ori : 0, pos : [(- 0.4), 0], size : [0.4, 0.4],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : 0.0 
  });
  right = new visual.ImageStim({
    win : psychoJS.window,
    name : 'right', units : undefined, 
    image : undefined, mask : undefined,
    ori : 0, pos : [0.4, 0], size : [0.4, 0.4],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -1.0 
  });
  key_resp = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "stimuli_feedback"
  stimuli_feedbackClock = new util.Clock();
  left_feedback = new visual.ImageStim({
    win : psychoJS.window,
    name : 'left_feedback', units : undefined, 
    image : undefined, mask : undefined,
    ori : 0, pos : [(- 0.4), 0], size : [0.4, 0.4],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -1.0 
  });
  right_feedback = new visual.ImageStim({
    win : psychoJS.window,
    name : 'right_feedback', units : undefined, 
    image : undefined, mask : undefined,
    ori : 0, pos : [0.4, 0], size : [0.4, 0.4],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -2.0 
  });
  // Initialize components for Routine "fixation"
  fixationClock = new util.Clock();
  iti = new visual.ShapeStim ({
    win: psychoJS.window, name: 'iti', 
    vertices: 'cross', size:[0.05, 0.05],
    ori: 0, pos: [0, 0],
    lineWidth: 1, lineColor: new util.Color([1, 1, 1]),
    fillColor: new util.Color([1, 1, 1]),
    opacity: 1, depth: 0, interpolate: true,
  });
  
  // Initialize components for Routine "feedback"
  feedbackClock = new util.Clock();
  feedback_text = new visual.TextStim({
    win: psychoJS.window,
    name: 'feedback_text',
    text: 'default text',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.1,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -1.0 
  });
  
  // Initialize components for Routine "instr4"
  instr4Clock = new util.Clock();
  instr_4 = new visual.TextStim({
    win: psychoJS.window,
    name: 'instr_4',
    text: 'Now you will play the task for real.\n\nYou can win up to 3 dollars.\n\nPress SPACE to continue.',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.05,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: 0.0 
  });
  
  key_resp_8 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "exp_instr"
  exp_instrClock = new util.Clock();
  ready_exp = new visual.TextStim({
    win: psychoJS.window,
    name: 'ready_exp',
    text: 'Remember, your performance from now on will result in REAL MONETARY outcomes!\n\nYou will receive any money you win. \n\nPress SPACE to begin the experiment.',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.05,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: 0.0 
  });
  
  key_resp_5 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "BlockInstruct"
  BlockInstructClock = new util.Clock();
  BlockInstr_disp = new visual.TextStim({
    win: psychoJS.window,
    name: 'BlockInstr_disp',
    text: 'default text',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.08,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -1.0 
  });
  
  // Initialize components for Routine "fixation"
  fixationClock = new util.Clock();
  iti = new visual.ShapeStim ({
    win: psychoJS.window, name: 'iti', 
    vertices: 'cross', size:[0.05, 0.05],
    ori: 0, pos: [0, 0],
    lineWidth: 1, lineColor: new util.Color([1, 1, 1]),
    fillColor: new util.Color([1, 1, 1]),
    opacity: 1, depth: 0, interpolate: true,
  });
  
  // Initialize components for Routine "stimuli"
  stimuliClock = new util.Clock();
  left = new visual.ImageStim({
    win : psychoJS.window,
    name : 'left', units : undefined, 
    image : undefined, mask : undefined,
    ori : 0, pos : [(- 0.4), 0], size : [0.4, 0.4],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : 0.0 
  });
  right = new visual.ImageStim({
    win : psychoJS.window,
    name : 'right', units : undefined, 
    image : undefined, mask : undefined,
    ori : 0, pos : [0.4, 0], size : [0.4, 0.4],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -1.0 
  });
  key_resp = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "stimuli_feedback"
  stimuli_feedbackClock = new util.Clock();
  left_feedback = new visual.ImageStim({
    win : psychoJS.window,
    name : 'left_feedback', units : undefined, 
    image : undefined, mask : undefined,
    ori : 0, pos : [(- 0.4), 0], size : [0.4, 0.4],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -1.0 
  });
  right_feedback = new visual.ImageStim({
    win : psychoJS.window,
    name : 'right_feedback', units : undefined, 
    image : undefined, mask : undefined,
    ori : 0, pos : [0.4, 0], size : [0.4, 0.4],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -2.0 
  });
  // Initialize components for Routine "fixation"
  fixationClock = new util.Clock();
  iti = new visual.ShapeStim ({
    win: psychoJS.window, name: 'iti', 
    vertices: 'cross', size:[0.05, 0.05],
    ori: 0, pos: [0, 0],
    lineWidth: 1, lineColor: new util.Color([1, 1, 1]),
    fillColor: new util.Color([1, 1, 1]),
    opacity: 1, depth: 0, interpolate: true,
  });
  
  // Initialize components for Routine "feedback"
  feedbackClock = new util.Clock();
  feedback_text = new visual.TextStim({
    win: psychoJS.window,
    name: 'feedback_text',
    text: 'default text',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.1,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -1.0 
  });
  
  // Initialize components for Routine "ender"
  enderClock = new util.Clock();
  end_heading = new visual.TextStim({
    win: psychoJS.window,
    name: 'end_heading',
    text: 'Experiment complete!',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0.4], height: 0.075,  wrapWidth: undefined, ori: 0,
    color: new util.Color('yellow'),  opacity: 1,
    depth: -1.0 
  });
  
  end_text = new visual.TextStim({
    win: psychoJS.window,
    name: 'end_text',
    text: 'default text',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.05,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -2.0 
  });
  
  key_resp_6 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  text_4 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_4',
    text: 'Press SPACE to exit.',
    font: 'Arial',
    units: undefined, 
    pos: [0, (- 0.4)], height: 0.08,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -4.0 
  });
  
  // Create some handy timers
  globalClock = new util.Clock();  // to track the time since experiment started
  routineTimer = new util.CountdownTimer();  // to track time remaining of each (non-slip) routine
  
  return Scheduler.Event.NEXT;
}


var t;
var frameN;
var _key_resp_1_allKeys;
var introComponents;
function introRoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'intro'-------
    t = 0;
    introClock.reset(); // clock
    frameN = -1;
    // update component parameters for each repeat
    key_resp_1.keys = undefined;
    key_resp_1.rt = undefined;
    _key_resp_1_allKeys = [];
    // keep track of which components have finished
    introComponents = [];
    introComponents.push(key_resp_1);
    introComponents.push(intro_text);
    
    introComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    
    return Scheduler.Event.NEXT;
  };
}


var continueRoutine;
function introRoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'intro'-------
    let continueRoutine = true; // until we're told otherwise
    // get current time
    t = introClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *key_resp_1* updates
    if (t >= 0 && key_resp_1.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp_1.tStart = t;  // (not accounting for frame time here)
      key_resp_1.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp_1.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp_1.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp_1.clearEvents(); });
    }

    if (key_resp_1.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp_1.getKeys({keyList: ['space'], waitRelease: false});
      _key_resp_1_allKeys = _key_resp_1_allKeys.concat(theseKeys);
      if (_key_resp_1_allKeys.length > 0) {
        key_resp_1.keys = _key_resp_1_allKeys[_key_resp_1_allKeys.length - 1].name;  // just the last key pressed
        key_resp_1.rt = _key_resp_1_allKeys[_key_resp_1_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    
    // *intro_text* updates
    if (t >= 0.0 && intro_text.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      intro_text.tStart = t;  // (not accounting for frame time here)
      intro_text.frameNStart = frameN;  // exact frame index
      
      intro_text.setAutoDraw(true);
    }

    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    introComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function introRoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'intro'-------
    introComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    // the Routine "intro" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var _key_resp_2_allKeys;
var instr1Components;
function instr1RoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'instr1'-------
    t = 0;
    instr1Clock.reset(); // clock
    frameN = -1;
    // update component parameters for each repeat
    key_resp_2.keys = undefined;
    key_resp_2.rt = undefined;
    _key_resp_2_allKeys = [];
    // keep track of which components have finished
    instr1Components = [];
    instr1Components.push(instr_1);
    instr1Components.push(key_resp_2);
    
    instr1Components.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    
    return Scheduler.Event.NEXT;
  };
}


function instr1RoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'instr1'-------
    let continueRoutine = true; // until we're told otherwise
    // get current time
    t = instr1Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *instr_1* updates
    if (t >= 0.0 && instr_1.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      instr_1.tStart = t;  // (not accounting for frame time here)
      instr_1.frameNStart = frameN;  // exact frame index
      
      instr_1.setAutoDraw(true);
    }

    
    // *key_resp_2* updates
    if (t >= 0 && key_resp_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp_2.tStart = t;  // (not accounting for frame time here)
      key_resp_2.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp_2.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp_2.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp_2.clearEvents(); });
    }

    if (key_resp_2.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp_2.getKeys({keyList: ['space'], waitRelease: false});
      _key_resp_2_allKeys = _key_resp_2_allKeys.concat(theseKeys);
      if (_key_resp_2_allKeys.length > 0) {
        key_resp_2.keys = _key_resp_2_allKeys[_key_resp_2_allKeys.length - 1].name;  // just the last key pressed
        key_resp_2.rt = _key_resp_2_allKeys[_key_resp_2_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    instr1Components.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function instr1RoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'instr1'-------
    instr1Components.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    // the Routine "instr1" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var _key_resp_4_allKeys;
var instr2Components;
function instr2RoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'instr2'-------
    t = 0;
    instr2Clock.reset(); // clock
    frameN = -1;
    // update component parameters for each repeat
    key_resp_4.keys = undefined;
    key_resp_4.rt = undefined;
    _key_resp_4_allKeys = [];
    // keep track of which components have finished
    instr2Components = [];
    instr2Components.push(instr_2);
    instr2Components.push(key_resp_4);
    
    instr2Components.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    
    return Scheduler.Event.NEXT;
  };
}


function instr2RoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'instr2'-------
    let continueRoutine = true; // until we're told otherwise
    // get current time
    t = instr2Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *instr_2* updates
    if (t >= 0 && instr_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      instr_2.tStart = t;  // (not accounting for frame time here)
      instr_2.frameNStart = frameN;  // exact frame index
      
      instr_2.setAutoDraw(true);
    }

    
    // *key_resp_4* updates
    if (t >= 0 && key_resp_4.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp_4.tStart = t;  // (not accounting for frame time here)
      key_resp_4.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp_4.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp_4.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp_4.clearEvents(); });
    }

    if (key_resp_4.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp_4.getKeys({keyList: ['space'], waitRelease: false});
      _key_resp_4_allKeys = _key_resp_4_allKeys.concat(theseKeys);
      if (_key_resp_4_allKeys.length > 0) {
        key_resp_4.keys = _key_resp_4_allKeys[_key_resp_4_allKeys.length - 1].name;  // just the last key pressed
        key_resp_4.rt = _key_resp_4_allKeys[_key_resp_4_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    instr2Components.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function instr2RoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'instr2'-------
    instr2Components.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    // the Routine "instr2" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var _key_resp_3_allKeys;
var instr3Components;
function instr3RoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'instr3'-------
    t = 0;
    instr3Clock.reset(); // clock
    frameN = -1;
    // update component parameters for each repeat
    key_resp_3.keys = undefined;
    key_resp_3.rt = undefined;
    _key_resp_3_allKeys = [];
    // keep track of which components have finished
    instr3Components = [];
    instr3Components.push(instr_3);
    instr3Components.push(key_resp_3);
    
    instr3Components.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    
    return Scheduler.Event.NEXT;
  };
}


function instr3RoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'instr3'-------
    let continueRoutine = true; // until we're told otherwise
    // get current time
    t = instr3Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *instr_3* updates
    if (t >= 0.0 && instr_3.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      instr_3.tStart = t;  // (not accounting for frame time here)
      instr_3.frameNStart = frameN;  // exact frame index
      
      instr_3.setAutoDraw(true);
    }

    
    // *key_resp_3* updates
    if (t >= 0 && key_resp_3.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp_3.tStart = t;  // (not accounting for frame time here)
      key_resp_3.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp_3.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp_3.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp_3.clearEvents(); });
    }

    if (key_resp_3.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp_3.getKeys({keyList: ['space'], waitRelease: false});
      _key_resp_3_allKeys = _key_resp_3_allKeys.concat(theseKeys);
      if (_key_resp_3_allKeys.length > 0) {
        key_resp_3.keys = _key_resp_3_allKeys[_key_resp_3_allKeys.length - 1].name;  // just the last key pressed
        key_resp_3.rt = _key_resp_3_allKeys[_key_resp_3_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    instr3Components.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function instr3RoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'instr3'-------
    instr3Components.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    // the Routine "instr3" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var _key_resp_7_allKeys;
var prac_instrComponents;
function prac_instrRoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'prac_instr'-------
    t = 0;
    prac_instrClock.reset(); // clock
    frameN = -1;
    // update component parameters for each repeat
    key_resp_7.keys = undefined;
    key_resp_7.rt = undefined;
    _key_resp_7_allKeys = [];
    // keep track of which components have finished
    prac_instrComponents = [];
    prac_instrComponents.push(read_prac);
    prac_instrComponents.push(key_resp_7);
    
    prac_instrComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    
    return Scheduler.Event.NEXT;
  };
}


function prac_instrRoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'prac_instr'-------
    let continueRoutine = true; // until we're told otherwise
    // get current time
    t = prac_instrClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *read_prac* updates
    if (t >= 0.0 && read_prac.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      read_prac.tStart = t;  // (not accounting for frame time here)
      read_prac.frameNStart = frameN;  // exact frame index
      
      read_prac.setAutoDraw(true);
    }

    
    // *key_resp_7* updates
    if (t >= 0.0 && key_resp_7.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp_7.tStart = t;  // (not accounting for frame time here)
      key_resp_7.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp_7.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp_7.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp_7.clearEvents(); });
    }

    if (key_resp_7.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp_7.getKeys({keyList: ['space'], waitRelease: false});
      _key_resp_7_allKeys = _key_resp_7_allKeys.concat(theseKeys);
      if (_key_resp_7_allKeys.length > 0) {
        key_resp_7.keys = _key_resp_7_allKeys[_key_resp_7_allKeys.length - 1].name;  // just the last key pressed
        key_resp_7.rt = _key_resp_7_allKeys[_key_resp_7_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    prac_instrComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function prac_instrRoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'prac_instr'-------
    prac_instrComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    // the Routine "prac_instr" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var practice_round;
var currentLoop;
function practice_roundLoopBegin(practice_roundLoopScheduler) {
  // set up handler to look after randomisation of conditions etc
  practice_round = new TrialHandler({
    psychoJS: psychoJS,
    nReps: 1, method: TrialHandler.Method.SEQUENTIAL,
    extraInfo: expInfo, originPath: undefined,
    trialList: 'orders/prac_stim-order.csv',
    seed: undefined, name: 'practice_round'
  });
  psychoJS.experiment.addLoop(practice_round); // add the loop to the experiment
  currentLoop = practice_round;  // we're now the current loop

  // Schedule all the trials in the trialList:
  practice_round.forEach(function() {
    const snapshot = practice_round.getSnapshot();

    practice_roundLoopScheduler.add(importConditions(snapshot));
    practice_roundLoopScheduler.add(BlockInstructRoutineBegin(snapshot));
    practice_roundLoopScheduler.add(BlockInstructRoutineEachFrame(snapshot));
    practice_roundLoopScheduler.add(BlockInstructRoutineEnd(snapshot));
    practice_roundLoopScheduler.add(fixationRoutineBegin(snapshot));
    practice_roundLoopScheduler.add(fixationRoutineEachFrame(snapshot));
    practice_roundLoopScheduler.add(fixationRoutineEnd(snapshot));
    practice_roundLoopScheduler.add(stimuliRoutineBegin(snapshot));
    practice_roundLoopScheduler.add(stimuliRoutineEachFrame(snapshot));
    practice_roundLoopScheduler.add(stimuliRoutineEnd(snapshot));
    practice_roundLoopScheduler.add(stimuli_feedbackRoutineBegin(snapshot));
    practice_roundLoopScheduler.add(stimuli_feedbackRoutineEachFrame(snapshot));
    practice_roundLoopScheduler.add(stimuli_feedbackRoutineEnd(snapshot));
    practice_roundLoopScheduler.add(fixationRoutineBegin(snapshot));
    practice_roundLoopScheduler.add(fixationRoutineEachFrame(snapshot));
    practice_roundLoopScheduler.add(fixationRoutineEnd(snapshot));
    practice_roundLoopScheduler.add(feedbackRoutineBegin(snapshot));
    practice_roundLoopScheduler.add(feedbackRoutineEachFrame(snapshot));
    practice_roundLoopScheduler.add(feedbackRoutineEnd(snapshot));
    practice_roundLoopScheduler.add(endLoopIteration(practice_roundLoopScheduler, snapshot));
  });

  return Scheduler.Event.NEXT;
}


function practice_roundLoopEnd() {
  psychoJS.experiment.removeLoop(practice_round);

  return Scheduler.Event.NEXT;
}


var trials;
function trialsLoopBegin(trialsLoopScheduler) {
  // set up handler to look after randomisation of conditions etc
  trials = new TrialHandler({
    psychoJS: psychoJS,
    nReps: 1, method: TrialHandler.Method.SEQUENTIAL,
    extraInfo: expInfo, originPath: undefined,
    trialList: order_file,
    seed: undefined, name: 'trials'
  });
  psychoJS.experiment.addLoop(trials); // add the loop to the experiment
  currentLoop = trials;  // we're now the current loop

  // Schedule all the trials in the trialList:
  trials.forEach(function() {
    const snapshot = trials.getSnapshot();

    trialsLoopScheduler.add(importConditions(snapshot));
    trialsLoopScheduler.add(BlockInstructRoutineBegin(snapshot));
    trialsLoopScheduler.add(BlockInstructRoutineEachFrame(snapshot));
    trialsLoopScheduler.add(BlockInstructRoutineEnd(snapshot));
    trialsLoopScheduler.add(fixationRoutineBegin(snapshot));
    trialsLoopScheduler.add(fixationRoutineEachFrame(snapshot));
    trialsLoopScheduler.add(fixationRoutineEnd(snapshot));
    trialsLoopScheduler.add(stimuliRoutineBegin(snapshot));
    trialsLoopScheduler.add(stimuliRoutineEachFrame(snapshot));
    trialsLoopScheduler.add(stimuliRoutineEnd(snapshot));
    trialsLoopScheduler.add(stimuli_feedbackRoutineBegin(snapshot));
    trialsLoopScheduler.add(stimuli_feedbackRoutineEachFrame(snapshot));
    trialsLoopScheduler.add(stimuli_feedbackRoutineEnd(snapshot));
    trialsLoopScheduler.add(fixationRoutineBegin(snapshot));
    trialsLoopScheduler.add(fixationRoutineEachFrame(snapshot));
    trialsLoopScheduler.add(fixationRoutineEnd(snapshot));
    trialsLoopScheduler.add(feedbackRoutineBegin(snapshot));
    trialsLoopScheduler.add(feedbackRoutineEachFrame(snapshot));
    trialsLoopScheduler.add(feedbackRoutineEnd(snapshot));
    trialsLoopScheduler.add(endLoopIteration(trialsLoopScheduler, snapshot));
  });

  return Scheduler.Event.NEXT;
}


function trialsLoopEnd() {
  psychoJS.experiment.removeLoop(trials);

  return Scheduler.Event.NEXT;
}


var BlockInstructComponents;
function BlockInstructRoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'BlockInstruct'-------
    t = 0;
    BlockInstructClock.reset(); // clock
    frameN = -1;
    routineTimer.add(5.000000);
    // update component parameters for each repeat
    BlockInstr_disp.setText(block_instr_text);
    // keep track of which components have finished
    BlockInstructComponents = [];
    BlockInstructComponents.push(BlockInstr_disp);
    
    BlockInstructComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    
    return Scheduler.Event.NEXT;
  };
}


var frameRemains;
function BlockInstructRoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'BlockInstruct'-------
    let continueRoutine = true; // until we're told otherwise
    // get current time
    t = BlockInstructClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    if ((trial_num !== 0)) {
        continueRoutine = false;
    }
    
    
    // *BlockInstr_disp* updates
    if (t >= 0.0 && BlockInstr_disp.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      BlockInstr_disp.tStart = t;  // (not accounting for frame time here)
      BlockInstr_disp.frameNStart = frameN;  // exact frame index
      
      BlockInstr_disp.setAutoDraw(true);
    }

    frameRemains = 0.0 + 5 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (BlockInstr_disp.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      BlockInstr_disp.setAutoDraw(false);
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    BlockInstructComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function BlockInstructRoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'BlockInstruct'-------
    BlockInstructComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    return Scheduler.Event.NEXT;
  };
}


var fixationComponents;
function fixationRoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'fixation'-------
    t = 0;
    fixationClock.reset(); // clock
    frameN = -1;
    routineTimer.add(0.500000);
    // update component parameters for each repeat
    // keep track of which components have finished
    fixationComponents = [];
    fixationComponents.push(iti);
    
    fixationComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    
    return Scheduler.Event.NEXT;
  };
}


function fixationRoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'fixation'-------
    let continueRoutine = true; // until we're told otherwise
    // get current time
    t = fixationClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *iti* updates
    if (t >= 0.0 && iti.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      iti.tStart = t;  // (not accounting for frame time here)
      iti.frameNStart = frameN;  // exact frame index
      
      iti.setAutoDraw(true);
    }

    frameRemains = 0.0 + 0.5 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (iti.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      iti.setAutoDraw(false);
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    fixationComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function fixationRoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'fixation'-------
    fixationComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    return Scheduler.Event.NEXT;
  };
}


var _key_resp_allKeys;
var stimuliComponents;
function stimuliRoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'stimuli'-------
    t = 0;
    stimuliClock.reset(); // clock
    frameN = -1;
    routineTimer.add(2.000000);
    // update component parameters for each repeat
    left.setImage(stim_left_name);
    right.setImage(stim_right_name);
    key_resp.keys = undefined;
    key_resp.rt = undefined;
    _key_resp_allKeys = [];
    // keep track of which components have finished
    stimuliComponents = [];
    stimuliComponents.push(left);
    stimuliComponents.push(right);
    stimuliComponents.push(key_resp);
    
    stimuliComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    
    return Scheduler.Event.NEXT;
  };
}


function stimuliRoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'stimuli'-------
    let continueRoutine = true; // until we're told otherwise
    // get current time
    t = stimuliClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *left* updates
    if (t >= 0.0 && left.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      left.tStart = t;  // (not accounting for frame time here)
      left.frameNStart = frameN;  // exact frame index
      
      left.setAutoDraw(true);
    }

    frameRemains = 0.0 + 2 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (left.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      left.setAutoDraw(false);
    }
    
    // *right* updates
    if (t >= 0.0 && right.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      right.tStart = t;  // (not accounting for frame time here)
      right.frameNStart = frameN;  // exact frame index
      
      right.setAutoDraw(true);
    }

    frameRemains = 0.0 + 2 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (right.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      right.setAutoDraw(false);
    }
    
    // *key_resp* updates
    if (t >= 0 && key_resp.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp.tStart = t;  // (not accounting for frame time here)
      key_resp.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp.clearEvents(); });
    }

    frameRemains = 0 + 2 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (key_resp.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      key_resp.status = PsychoJS.Status.FINISHED;
  }

    if (key_resp.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp.getKeys({keyList: ['left', 'right'], waitRelease: false});
      _key_resp_allKeys = _key_resp_allKeys.concat(theseKeys);
      if (_key_resp_allKeys.length > 0) {
        key_resp.keys = _key_resp_allKeys[0].name;  // just the first key pressed
        key_resp.rt = _key_resp_allKeys[0].rt;
        // was this correct?
        if (key_resp.keys == optimal_choice) {
            key_resp.corr = 1;
        } else {
            key_resp.corr = 0;
        }
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    stimuliComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function stimuliRoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'stimuli'-------
    stimuliComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    // was no response the correct answer?!
    if (key_resp.keys === undefined) {
      if (['None','none',undefined].includes(optimal_choice)) {
         key_resp.corr = 1;  // correct non-response
      } else {
         key_resp.corr = 0;  // failed to respond (incorrectly)
      }
    }
    // store data for thisExp (ExperimentHandler)
    psychoJS.experiment.addData('key_resp.keys', key_resp.keys);
    psychoJS.experiment.addData('key_resp.corr', key_resp.corr);
    if (typeof key_resp.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_resp.rt', key_resp.rt);
        routineTimer.reset();
        }
    
    key_resp.stop();
    if ((position_changed === 0)) {
        if ((key_resp.keys === "left")) {
            thisExp.addData("chosen_stim_name", stim_0);
            thisExp.addData("chosen_stim_0", 1);
            thisExp.addData("chosen_stim_1", 0);
            if ((goal === "win")) {
                thisExp.addData("true_accuracy", 1);
            } else {
                if ((goal === "avoidloss")) {
                    thisExp.addData("true_accuracy", 0);
                }
            }
        } else {
            if ((key_resp.keys === "right")) {
                thisExp.addData("chosen_stim_name", stim_1);
                thisExp.addData("chosen_stim_0", 0);
                thisExp.addData("chosen_stim_1", 1);
                if ((goal === "win")) {
                    thisExp.addData("true_accuracy", 0);
                } else {
                    if ((goal === "avoidloss")) {
                        thisExp.addData("true_accuracy", 1);
                    }
                }
            }
        }
    } else {
        if ((position_changed === 1)) {
            if ((key_resp.keys === "left")) {
                thisExp.addData("chosen_stim_name", stim_1);
                thisExp.addData("chosen_stim_0", 0);
                thisExp.addData("chosen_stim_1", 1);
                if ((goal === "win")) {
                    thisExp.addData("true_accuracy", 0);
                } else {
                    if ((goal === "avoidloss")) {
                        thisExp.addData("true_accuracy", 1);
                    }
                }
            } else {
                if ((key_resp.keys === "right")) {
                    thisExp.addData("chosen_stim_name", stim_0);
                    thisExp.addData("chosen_stim_0", 1);
                    thisExp.addData("chosen_stim_1", 0);
                    if ((goal === "win")) {
                        thisExp.addData("true_accuracy", 1);
                    } else {
                        if ((goal === "avoidloss")) {
                            thisExp.addData("true_accuracy", 0);
                        }
                    }
                }
            }
        }
    }
    
    return Scheduler.Event.NEXT;
  };
}


var feedback_stim_right;
var feedback_stim_left;
var stimuli_feedbackComponents;
function stimuli_feedbackRoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'stimuli_feedback'-------
    t = 0;
    stimuli_feedbackClock.reset(); // clock
    frameN = -1;
    routineTimer.add(0.500000);
    // update component parameters for each repeat
    if ((key_resp.keys === "left")) {
        feedback_stim_right = stim_right_name;
        feedback_stim_left = stim_left_name_feedback;
    } else {
        if ((key_resp.keys === "right")) {
            feedback_stim_right = stim_right_name_feedback;
            feedback_stim_left = stim_left_name;
        } else {
            feedback_stim_right = stim_right_name;
            feedback_stim_left = stim_left_name;
        }
    }
    
    left_feedback.setImage(feedback_stim_left);
    right_feedback.setImage(feedback_stim_right);
    // keep track of which components have finished
    stimuli_feedbackComponents = [];
    stimuli_feedbackComponents.push(left_feedback);
    stimuli_feedbackComponents.push(right_feedback);
    
    stimuli_feedbackComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    
    return Scheduler.Event.NEXT;
  };
}


function stimuli_feedbackRoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'stimuli_feedback'-------
    let continueRoutine = true; // until we're told otherwise
    // get current time
    t = stimuli_feedbackClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *left_feedback* updates
    if (t >= 0.0 && left_feedback.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      left_feedback.tStart = t;  // (not accounting for frame time here)
      left_feedback.frameNStart = frameN;  // exact frame index
      
      left_feedback.setAutoDraw(true);
    }

    frameRemains = 0.0 + 0.5 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (left_feedback.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      left_feedback.setAutoDraw(false);
    }
    
    // *right_feedback* updates
    if (t >= 0.0 && right_feedback.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      right_feedback.tStart = t;  // (not accounting for frame time here)
      right_feedback.frameNStart = frameN;  // exact frame index
      
      right_feedback.setAutoDraw(true);
    }

    frameRemains = 0.0 + 0.5 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (right_feedback.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      right_feedback.setAutoDraw(false);
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    stimuli_feedbackComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function stimuli_feedbackRoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'stimuli_feedback'-------
    stimuli_feedbackComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    return Scheduler.Event.NEXT;
  };
}


var outcome;
var feedbackComponents;
function feedbackRoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'feedback'-------
    t = 0;
    feedbackClock.reset(); // clock
    frameN = -1;
    routineTimer.add(1.500000);
    // update component parameters for each repeat
    if ((! key_resp.keys)) {
        outcome = "missed";
        thisExp.addData("cumulativePts_self", ptsSelf);
        if ((condition !== "practice")) {
            thisExp.addData("outcomeDescr", "missed");
        }
    } else {
        if (key_resp.corr) {
            if ((goal === "win")) {
                if ((condition === "self")) {
                    outcome = "YOU\n\n+100 points";
                    ptsSelf += 100;
                    thisExp.addData("cumulativePts_self", ptsSelf);
                    thisExp.addData("outcomeDescr", "self win");
                    thisExp.addData("outcome", 1);
                } else {
                    if ((condition === "practice")) {
                        outcome = "+100 points";
                    }
                }
            }
        } else {
            if ((goal === "win")) {
                if ((condition === "self")) {
                    outcome = "YOU\n\n0 points";
                    ptsSelf += 0;
                    thisExp.addData("cumulativePts_self", ptsSelf);
                    thisExp.addData("outcomeDescr", "self avoid win");
                    thisExp.addData("outcome", 0);
                } else {
                    if ((condition === "practice")) {
                        outcome = "0 points";
                    }
                }
            }
        }
    }
    if ((condition === "practice")) {
        thisExp.addData("cumulativePts_self", 1000);
        thisExp.addData("outcomeDescr", "practice");
    }
    
    feedback_text.setText(outcome);
    // keep track of which components have finished
    feedbackComponents = [];
    feedbackComponents.push(feedback_text);
    
    feedbackComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    
    return Scheduler.Event.NEXT;
  };
}


function feedbackRoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'feedback'-------
    let continueRoutine = true; // until we're told otherwise
    // get current time
    t = feedbackClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *feedback_text* updates
    if (t >= 0.0 && feedback_text.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      feedback_text.tStart = t;  // (not accounting for frame time here)
      feedback_text.frameNStart = frameN;  // exact frame index
      
      feedback_text.setAutoDraw(true);
    }

    frameRemains = 0.0 + 1.5 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (feedback_text.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      feedback_text.setAutoDraw(false);
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    feedbackComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function feedbackRoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'feedback'-------
    feedbackComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    return Scheduler.Event.NEXT;
  };
}


var _key_resp_8_allKeys;
var instr4Components;
function instr4RoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'instr4'-------
    t = 0;
    instr4Clock.reset(); // clock
    frameN = -1;
    // update component parameters for each repeat
    key_resp_8.keys = undefined;
    key_resp_8.rt = undefined;
    _key_resp_8_allKeys = [];
    // keep track of which components have finished
    instr4Components = [];
    instr4Components.push(instr_4);
    instr4Components.push(key_resp_8);
    
    instr4Components.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    
    return Scheduler.Event.NEXT;
  };
}


function instr4RoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'instr4'-------
    let continueRoutine = true; // until we're told otherwise
    // get current time
    t = instr4Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *instr_4* updates
    if (t >= 0.0 && instr_4.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      instr_4.tStart = t;  // (not accounting for frame time here)
      instr_4.frameNStart = frameN;  // exact frame index
      
      instr_4.setAutoDraw(true);
    }

    
    // *key_resp_8* updates
    if (t >= 0 && key_resp_8.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp_8.tStart = t;  // (not accounting for frame time here)
      key_resp_8.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp_8.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp_8.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp_8.clearEvents(); });
    }

    if (key_resp_8.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp_8.getKeys({keyList: ['space'], waitRelease: false});
      _key_resp_8_allKeys = _key_resp_8_allKeys.concat(theseKeys);
      if (_key_resp_8_allKeys.length > 0) {
        key_resp_8.keys = _key_resp_8_allKeys[_key_resp_8_allKeys.length - 1].name;  // just the last key pressed
        key_resp_8.rt = _key_resp_8_allKeys[_key_resp_8_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    instr4Components.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function instr4RoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'instr4'-------
    instr4Components.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    // the Routine "instr4" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var _key_resp_5_allKeys;
var exp_instrComponents;
function exp_instrRoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'exp_instr'-------
    t = 0;
    exp_instrClock.reset(); // clock
    frameN = -1;
    // update component parameters for each repeat
    key_resp_5.keys = undefined;
    key_resp_5.rt = undefined;
    _key_resp_5_allKeys = [];
    // keep track of which components have finished
    exp_instrComponents = [];
    exp_instrComponents.push(ready_exp);
    exp_instrComponents.push(key_resp_5);
    
    exp_instrComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    
    return Scheduler.Event.NEXT;
  };
}


function exp_instrRoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'exp_instr'-------
    let continueRoutine = true; // until we're told otherwise
    // get current time
    t = exp_instrClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *ready_exp* updates
    if (t >= 0.0 && ready_exp.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      ready_exp.tStart = t;  // (not accounting for frame time here)
      ready_exp.frameNStart = frameN;  // exact frame index
      
      ready_exp.setAutoDraw(true);
    }

    
    // *key_resp_5* updates
    if (t >= 0 && key_resp_5.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp_5.tStart = t;  // (not accounting for frame time here)
      key_resp_5.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp_5.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp_5.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp_5.clearEvents(); });
    }

    if (key_resp_5.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp_5.getKeys({keyList: ['space'], waitRelease: false});
      _key_resp_5_allKeys = _key_resp_5_allKeys.concat(theseKeys);
      if (_key_resp_5_allKeys.length > 0) {
        key_resp_5.keys = _key_resp_5_allKeys[_key_resp_5_allKeys.length - 1].name;  // just the last key pressed
        key_resp_5.rt = _key_resp_5_allKeys[_key_resp_5_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    exp_instrComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function exp_instrRoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'exp_instr'-------
    exp_instrComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    // the Routine "exp_instr" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var end_result;
var _key_resp_6_allKeys;
var enderComponents;
function enderRoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'ender'-------
    t = 0;
    enderClock.reset(); // clock
    frameN = -1;
    // update component parameters for each repeat
    if ((ptsSelf > 0)) {
        end_result = `You won ${ptsSelf} points for YOURSELF!`;
    } else {
        end_result = "You did not win any points.";
    }
    
    end_text.setText(end_result);
    key_resp_6.keys = undefined;
    key_resp_6.rt = undefined;
    _key_resp_6_allKeys = [];
    // keep track of which components have finished
    enderComponents = [];
    enderComponents.push(end_heading);
    enderComponents.push(end_text);
    enderComponents.push(key_resp_6);
    enderComponents.push(text_4);
    
    enderComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    
    return Scheduler.Event.NEXT;
  };
}


function enderRoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'ender'-------
    let continueRoutine = true; // until we're told otherwise
    // get current time
    t = enderClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *end_heading* updates
    if (t >= 0.0 && end_heading.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      end_heading.tStart = t;  // (not accounting for frame time here)
      end_heading.frameNStart = frameN;  // exact frame index
      
      end_heading.setAutoDraw(true);
    }

    
    // *end_text* updates
    if (t >= 0.0 && end_text.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      end_text.tStart = t;  // (not accounting for frame time here)
      end_text.frameNStart = frameN;  // exact frame index
      
      end_text.setAutoDraw(true);
    }

    
    // *key_resp_6* updates
    if (t >= 0.0 && key_resp_6.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp_6.tStart = t;  // (not accounting for frame time here)
      key_resp_6.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp_6.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp_6.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp_6.clearEvents(); });
    }

    if (key_resp_6.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp_6.getKeys({keyList: ['space'], waitRelease: false});
      _key_resp_6_allKeys = _key_resp_6_allKeys.concat(theseKeys);
      if (_key_resp_6_allKeys.length > 0) {
        key_resp_6.keys = _key_resp_6_allKeys[_key_resp_6_allKeys.length - 1].name;  // just the last key pressed
        key_resp_6.rt = _key_resp_6_allKeys[_key_resp_6_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    
    // *text_4* updates
    if (t >= 0.0 && text_4.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_4.tStart = t;  // (not accounting for frame time here)
      text_4.frameNStart = frameN;  // exact frame index
      
      text_4.setAutoDraw(true);
    }

    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    enderComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function enderRoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'ender'-------
    enderComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    // the Routine "ender" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


function endLoopIteration(scheduler, snapshot) {
  // ------Prepare for next entry------
  return function () {
    if (typeof snapshot !== 'undefined') {
      // ------Check if user ended loop early------
      if (snapshot.finished) {
        // Check for and save orphaned data
        if (psychoJS.experiment.isEntryEmpty()) {
          psychoJS.experiment.nextEntry(snapshot);
        }
        scheduler.stop();
      } else {
        const thisTrial = snapshot.getCurrentTrial();
        if (typeof thisTrial === 'undefined' || !('isTrials' in thisTrial) || thisTrial.isTrials) {
          psychoJS.experiment.nextEntry(snapshot);
        }
      }
    return Scheduler.Event.NEXT;
    }
  };
}


function importConditions(currentLoop) {
  return function () {
    psychoJS.importAttributes(currentLoop.getCurrentTrial());
    return Scheduler.Event.NEXT;
    };
}


function quitPsychoJS(message, isCompleted) {
  // Check for and save orphaned data
  if (psychoJS.experiment.isEntryEmpty()) {
    psychoJS.experiment.nextEntry();
  }
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  psychoJS.window.close();
  psychoJS.quit({message: message, isCompleted: isCompleted});
  
  return Scheduler.Event.QUIT;
}
