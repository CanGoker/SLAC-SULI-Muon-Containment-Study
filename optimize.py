def test_far(input_file, numID):
    import numpy as np
    def find_missing(input_file):
        #checks if any trials don't have values for some reason
        missing = []
        arr = np.array(input_file['segments']['eventID'])
        for y in range (0, 1000):
            indexes = np.where(arr  == y)[0]
            if len(indexes) == 0:
                missing.append(y)
        return missing
    "iterates through and searches whether will fit"
    "If fits, returns specific parameters"
    segments = input_file['segments']
    event_segments = segments[segments['eventID'] == numID]
    seg_num = len(event_segments['x_start'])
    excluded = 0
    #return dictionary with fits, total energy number, amount contained, percentage contained
    return_vals = {'working_config': True, 'totalE': sum(event_segments['dE']), 'containedE': 0, 'percent': 0}
    startx = min(event_segments['x_start'])
    endx = max(event_segments['x_end'])
    starty = min(event_segments['y_start'])
    endy = max(event_segments['y_end'])
    startz = min(event_segments['z_start'])
    endz = max(event_segments['z_end'])
    xdist = abs(startx - endx)
    ydist = abs(starty - endy)
    zdist = abs(startz - endz)
    if xdist < 60000 and ydist < 13500 and zdist < 13000:
        return_vals['containedE'] += sum(event_segments['dE'])
        return_vals['percent'] = 1
    else:
        return_vals['working_config'] = False
    return return_vals

def test_all(input_file):
    prob = []
    for x in range(0, 1000):
        if x in missing:
            continue
        if test_far(input_file, x)['working_config'] == False:
            prob.append(x)
    return prob

#for easier testing in terminal
for x in range(0,1000):
    if x in missing:
        continue
    if test_far(f1, x)['working_config'] == False:
        prob.append(x)
    print(prob)



