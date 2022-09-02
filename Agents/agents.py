import random
locationCondition = {}

# randomize conditions in locations A and B
locationCondition['A'] = random.randint(0, 1)
locationCondition['B'] = random.randint(0, 1)
Score = 0
type(locationCondition)
dict
vacuumLocation = random.randint(0, 1)
        # if vacuum at A
if vacuumLocation == 0:
    print("Vacuum is randomly placed at Location A.")
        # and Location A is Dirty.
    if locationCondition['A'] == 1:
        print ("Location A is Dirty.")
        # suck the dirt  and mark it clean
        locationCondition['A'] = 0;
        Score += 1
        print ("Location A has been Cleaned.")
        # move to B
        print ("Moving to Location B...")
        Score -= 1
        # if B is Dirty
        if locationCondition['B'] == 1:
            print("Location B is Dirty.")
            # suck and mark clean
            locationCondition['B'] = 0;
            Score += 1
            print ("Location B has been Cleaned.")
    else:
        # move to B
        Score-= 1
        print ("Moving to Location B...")
        # if B is Dirty
        if locationCondition['B'] == 1:
            print("Location B is Dirty.")
            # suck and mark clean
            locationCondition['B'] = 0;
            Score += 1
            print ("Location B has been Cleaned.")
else:
    if(vacuumLocation == 1):
        print("Vacuum randomly placed at Location B.")
        # and B is Dirty
    if locationCondition['B'] == 1:
        print ("Location B is Dirty.")
        # suck and mark clean
        locationCondition['B'] = 0;
        Score += 1
        print ("Location B has been Cleaned.")
        # move to A
        Score -= 1
        print ("Moving to Location A...")
        # if A is Dirty
        if locationCondition['A'] == 1:
            print ("Location A is Dirty.")
            # suck and mark clean
            locationCondition['A'] = 0;
            Score += 1
            print ("Location A has been Cleaned.")
        else:
            # move to A
            print ("Moving to Location A...")
            Score -= 1
            # if A is Dirty
            if locationCondition['A'] == 1:
                print ("Location A is Dirty.")
                # suck and mark clean
                locationCondition['A'] = 0;
                Score += 1
                print ("Location A has been Cleaned.")
        # done cleaning
print(locationCondition)
print("Performance Measurement: " + str(Score))
