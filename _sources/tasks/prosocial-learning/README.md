# Prosocial Learning task
created by [Shawn A Rhoads](https://github.com/shawnrhoads) in PsychoPy v2020.2.4post1; adapted from [Harrison et al. (2016)](https://www.biologicalpsychiatryjournal.com/article/S0006-3223(15)00637-X/fulltext); and inspired by [Lockwood et al. (2016)](https://www.pnas.org/content/113/35/9763)

## 4 conditions/blocks
- self, win
- self, avoid loss
- social, win
- social, avoid loss

## Each block contains 24 trials
- 2 stimuli per trial (counterbalanced wrt side)
- outcomes associated with each stimulus is probabilistic (75%, 25%)


### Data output key
- `key_resp.keys`: selected key response (left or right)
- `key_resp.corr`: 1 if (+1 during win trials) or (0 during avoidloss trials); 0 if (0 during win trials) or (-1 during avoidloss trials)
- `key_resp.rt`: reaction time in seconds
- `chosen_stim_name`: selected stimulus file, blank if missed
- `chosen_stim_0`: 1 if selected `stim_0`; 0 if selected `stim_1`; blank if missed
- `chosen_stim_1`: 1 if selected `stim_1`; 0 if selected `stim_0`; blank if missed
- `true_accuracy`: 1 if selected stimulus with highest probability of winning or avoid losing
- `outcome`: outcome for trial (`+1`, `0`, `-1`); blank if missed
- `outcomeDescr`: text description of outcome (practice, social win, social avoid win, social loss, social avoidloss, self win, self avoid win, self loss, self avoidloss)
- `cumulativePts_self`: running total of points for self
- `cumulativePts_social`: running total of points for social

### Data input key
- `index`: order in which trials are displayed throughout entire experiment (100-115 for practice trials; 0-95 for experimental trials)
- `condition`: (play for self); (play for next participant)
- `goal`: (win) or (avoid loss)
- `block`: self/win, self/avoidloss, social/win, social/avoidloss
- `block_num`: 0, 1, 2, 3 (corresponding to `block`)
- `block_instr_text`: block instructions
- `trial_num`: order in which trials are displayed within a block (0-23)
- `stim_0`: stimulus number that yields +1 (win condition) or -1 (avoidloss condition) 75% of trials within block; or +0 25% of the time
- `stim_0_value`: stimulus filename that yields +1 (win condition) or -1 (avoidloss condition) 75% of trials within block; or +0 25% of the time
- `stim_1`: stimulus number that yields +1 (win condition) or -1 (avoidloss condition) 25% of trials within block; or +0 25% of the time
- `stim_1_value`: stimulus filename that yields +1 (win condition) or -1 (avoidloss condition) 75% of trials within block; or +0 25% of the time
- `position_changed`: 1 if position of `stim_0` changed to right side (0 if default on left side)
- `stim_left`: stimulus number displayed on left side for each trial 
- `stim_right`: stimulus number displayed on right side for each trial
- `stim_left_name`: stimulus filename displayed on left side for each trial 
- `stim_right_name`: stimulus filename displayed on right side for each trial
- `optimal_stim`: stimulus that will yield optimal outcome (+1 for win condition; 0 for avoidloss condition)
- `optimal_choice`: key response (`key_resp.keys`) that will yield optimal outcome (+1 for win condition; 0 for avoidloss condition)
- `participant`: ID number
- `date`: YYYY-MM-DD_TIME
