import urllib.request
id = '3000'
nachname = '3101'
vorname = '3102'
geb = '3103'
sex = '3110'
with open('test.gdt', encoding="utf8") as fp:
    # read all lines in a list
    lines = fp.readlines()
    for line in lines:
        # check if string present on a current line
        if line.find(id) != -1:
            v_id = line[7:].strip('\n')
            print (v_id)
            break
with open('test.gdt', encoding="utf8") as fp:
    # read all lines in a list
    lines = fp.readlines()
    for line in lines:
        # check if string present on a current line
        if line.find(vorname) != -1:
            v_vorname = line[7:].strip('\n')
            print (v_vorname)
        elif line.find(geb) != -1:
            v_geb = line[7:].strip('\n')
            print (v_geb)
        elif line.find(sex) != -1:
            v_sex = line[7:].strip('\n')
            print (v_sex)
        elif line.find(nachname) != -1:
            v_nachname = line[7:].strip('\n')
            print (v_nachname)
url = "http://192.168.178.24:8042/worklist/add?id="+v_id+"&lastname="+v_nachname+"&firstname="+v_vorname+"&birthdate="+v_geb+"&sex="+v_sex+"&modality=US&scheduledStation=US01&procedure=Exam&physician=Doctor"
print (url)
contents = urllib.request.urlopen(url)
