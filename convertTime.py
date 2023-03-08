
def convertTime(originalUnit,value):
    # converting military time to normal time
    if originalUnit == 'military':
        print(militaryToNormalTime(value))
    else:
        print(normaltoMilitaryTime(value))
    return None

def militaryToNormalTime(mTime):
    # militaryTime XXXX
    # - if the first XX is > 12
    timeList = []
    firstOct = int(mTime[:2])
    secondOct = mTime[-2:]
    if firstOct >= 12:
        if firstOct == 12:
            timeList.append('12')
        else:
            timeList.append(str(firstOct-12))
        timeList.append(secondOct)
        timeList.append('pm')
    else:
        if firstOct == 00:
            timeList.append('12')
        else:
            timeList.append(str(firstOct))
        timeList.append(secondOct)
        timeList.append('am')
    normalTime = timeList[0] + ':' + timeList[1] + ' ' + timeList[2]
    return f'{mTime} -> {normalTime}'

def normaltoMilitaryTime(nTime):
    # normal time: 'xx:xx am/pm'
    timeList = []
    sep = nTime.find(':')
    firstOct = nTime[:sep]
    secondOct = nTime[sep+1:sep+3]
    thirdOct = nTime[-2:]
    if thirdOct == 'am':
        if firstOct == '12':
            timeList.append('00')
            timeList.append(secondOct)
            militaryTime = ''.join(timeList)
        else:
            if len(firstOct) == 1:
                timeList.insert(0,'0')
            timeList.append(firstOct)
            timeList.append(secondOct)
            militaryTime = ''.join(timeList)
    elif thirdOct == 'pm':
        if firstOct == '12':
            timeList.append('12')
            timeList.append(secondOct)
            militaryTime = ''.join(timeList)
        else:
            timeList.append(str(int(firstOct)+12))
            timeList.append(secondOct)
            militaryTime = ''.join(timeList)
    return f'{nTime} -> {militaryTime}'

# def test0_m2n_func():
#     assert militaryToNormalTime('0045') == '12:45 am'
# def test1_m2n_func():
#     assert militaryToNormalTime('0730') == '7:30 am'
# def test2_m2n_func():
#     assert militaryToNormalTime('1130') == '11:30 am'
# def test3_m2n_func():
#     assert militaryToNormalTime('1347') == '1:47 pm'
# def test4_m2n_func():
#     assert militaryToNormalTime('1203') == '12:03 pm'
# def test5_m2n_func():
#     assert militaryToNormalTime('1757') == '5:57 pm'
# def test6_m2n_func():
#     assert militaryToNormalTime('0030') == '12:30 am'

# def test0_n2m_func():
#     assert normaltoMilitaryTime('1:17 am') == '0117'
# def test1_n2m_func():
#     assert normaltoMilitaryTime('04:50 am') == '0450'
# def test2_n2m_func():
#     assert normaltoMilitaryTime('10:30 am') == '1030'
# def test3_n2m_func():
#     assert normaltoMilitaryTime('2:37 pm') == '1437'
# def test4_n2m_func():
#     assert normaltoMilitaryTime('06:50 pm') == '1850'
# def test5_n2m_func():
#     assert normaltoMilitaryTime('12:30 pm') == '1230'
# def test6_n2m_func():
#     assert normaltoMilitaryTime('12:30 am') == '0030'