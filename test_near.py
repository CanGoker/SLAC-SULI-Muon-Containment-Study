def test_near(input_file, numID):
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
    segments = input_file['segments']
    event_segments = segments[segments['eventID'] == numID]
    arr = np.array(event_segments['pdgId'])
    indexes = np.where(arr  == 13)[0]
    event_segments = np.delete(event_segments, indexes)
    seg_num = len(event_segments['x_start'])
    #return dictionary with fits, total energy number, amount contained, percentage contained
    return_vals = {'working_config': True, 'totalE': sum(event_segments['dE']), 'containedE': 0, 'percent': 0, 'missing': find_missing(input_file)}
    startx = min(event_segments['x_start'])
    endx = max(event_segments['x_end'])
    starty = min(event_segments['y_start'])
    endy = max(event_segments['y_end'])
    startz = min(event_segments['z_start'])
    endz = max(event_segments['z_end'])
    xdist = abs(startx - endx)
    ydist = abs(starty - endy)
    zdist = abs(startz - endz)
    dimensions = np.array([startx, starty, startz])
    def Econt(input_file, numID):
        excluded = 0
        percent = 1
        energy = 0
        segments = input_file['segments']
        event_segments = segments[segments['eventID'] == numID]
        arr = np.array(event_segments['pdgId'])
        indexes = np.where(arr  == 13)[0]
        event_segments = np.delete(event_segments, indexes)
        seg_num = len(event_segments['x_start'])
        for i in range(seg_num):
            if event_segments['x_start'][i] < dimensions[0] or event_segments['x_end'][i] > (dimensions[0] + 5000) or event_segments['y_start'][i] < dimensions[1] or event_segments['y_end'][i] > dimensions[1] + 7000 or event_segments['z_start'][i] < dimensions[2] or event_segments['z_end'][i] > dimensions[2] + 3000:
                excluded += event_segments['dE'][i]
        percent = 1 - excluded/sum(event_segments['dE'])
        return percent
    if xdist < 5000 and ydist < 7000 and zdist < 3000:
        return_vals['containedE'] += sum(event_segments['dE'])
        return_vals['percent'] = 1
        print('pass1')
    elif return_vals['percent'] != 1:
        return_vals['percent'] = Econt(input_file, numID)
        print ('pass2')
    elif return_vals['percent'] < 0.95:
        return_vals['working_config'] = False
    return return_vals


def test_all(input_file):
    prob = []
    for x in range(0, 1000):
        if x in missing:
            continue
        if test_near(input_file, x)['working_config'] == False:
            prob.append(x)
    return prob

def Econt(input_file, numID):
    excluded = 0
    percent = 1
    segments = input_file['segments']
    event_segments = segments[segments['eventID'] == numID]
    seg_num = len(event_segments['x_start'])
    for i in range(seg_num):
        if event_segments['x_start'][i] < dimensions[0] or event_segments['x_end'][i] > (dimensions[0] + 5000) or event_segments['y_start'][i] < dimensions[1] or event_segments['y_end'][i] > dimensions[1] + 7000 or event_segments['z_start'][i] < dimensions[2] or event_segments['z_end'][i] > dimensions[2] + 3000:
            excluded += event_segments['dE'][i]
    percent = 1- excluded/sum(event_segments['dE'])
    return percen


t
 def find_muon(input_file):
    #checks where Muons are indexed
    muons = []
    segments = input_file['segments']
    event_segments = segments[segments['eventID'] == numID]
    arr = np.array(event_segments['pdgId'])
    indexes = np.where(arr  == 13)[0]
        return missing
