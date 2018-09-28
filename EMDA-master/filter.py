l1 = ['Attack',
'Attacked',
'Attacks',
'Violent',
'Assault',
'Fight',
'Incident',
'Sudden',
'Beaten',
'Assaulted',
'Assault'
]
l5 = [
'Terror',
'Terrorist',
'Suicide bomber',
'Isis',
'IED',
'Vehicle Ramming',
'Lone Wolf',
'Suicide Bomber',
'Acid Attack',
'Explosive Device',
'Terrorism'
]
l9 = [
'Disaster',
'Fire',
'Earthquake',
'Tornado',
'Flood',
'Hurricane',
'Collapsed Building',
'Trapped',
'Collapsed'
]
l2 = [
'Protest',
'Protesting', 
'Protests',
'Demonstration',
'Revolt'
]
l6 = [
'Robbery',
'Robbing',
'Rob',
'Robbed',
'Theft',
'Stolen',
'Burglar',
'Burglary'
]
l10 = [
'Crash',
'Accident',
'Emergency',
'Disaster',
'Hazard',
'Mishap'
]
l3 = [
'Stab',
'Stabbed',
'Stabbing',
'Knifed',
'Knife',
'Knives'
]
l7 = [
'Explosion',
'Exploded',
'Explode',
'Bomb',
'Bombing', 
'Bomber'
]
l11 = [
'murder',
'Deadly',
'Massacre',
'Execution',
'Homicide',
'slaughter'
]
l4 = [
'Shoot',
'Shot',
'Shooting',
'Active Shooter',
'Gunmen',
'Gunman'
]
l8 = [
'Rape',
'Raped',
'Raping'
]
l12 = [
'Heart Attack',
'MVA',
'CVA',
'Cardiac arrest',
'Wounded',
'Chest wound',
'Medical Emergency'
]

f=open("headlines.txt", "r")
if f.mode == 'r':
    contents =f.read()
f.close()
f=open("streetnames.txt", "r")
if f.mode == 'r':
    streets =f.read()
f.close()
streets = streets.split('\r\n')
#print streets
contents = [s.strip() for s in contents.splitlines()]
for s in contents:
    print str(s)
    m = str(s)
    #print type(k)
    #print len(k)
    m = m.split()
    m = map(lambda x: x.lower(), m)
    print m
    c = 0
    tt = 0
    for k in l1:
        if k.lower() in str(s).lower():
            print "Icon : icon 1 " + str(k)
            tt = 1
    for k in l2:
        if k.lower() in str(s).lower():
            print "Icon : icon 2 " + str(k)
            tt = 1
    for k in l3:
        if k.lower() in str(s).lower():
            print "Icon : icon 3 " + str(k)
            tt = 1
    for k in l4:
        if k.lower() in str(s).lower():
            print "Icon : icon 4 " + str(k)
            tt = 1
    for k in l5:
        if k.lower() in str(s).lower():
            print "Icon : icon 5 " + str(k)
            tt = 1
    for k in l6:
        if k.lower() in str(s).lower():
            print "Icon : icon 6 " + str(k)
            tt = 1
    for k in l7:
        if k.lower() in str(s).lower():
            print "Icon : icon 7 " + str(k)
            tt = 1
    for k in l8:
        if k.lower() in str(s).lower():
            print "Icon : icon 8 " + str(k)
            tt = 1
    for k in l9:
        if k.lower() in str(s).lower():
            print "Icon : icon 9 " + str(k)
            tt = 1
    for k in l10:
        if k.lower() in str(s).lower():
            print "Icon : icon 10 " + str(k)
            tt = 1
    for k in l11:
        if k.lower() in str(s).lower():
            print "Icon : icon 11 " + str(k)
            tt = 1
    for k in l12:
        if k.lower() in str(s).lower():
            print "Icon : icon 12 " + str(k)
            tt = 1
    if tt == 1:
        for k in streets:
            if k.lower() in m:
                print "Location : "+str(k) + " Street"
                c = 1

    if c==0:
        print "Location : Not Detected"
        
    print
    print




