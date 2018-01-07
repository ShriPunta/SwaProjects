import re

regex = r"([\(\[]).*?([\)\]])"

test_str = ("Saawariya-(MyMp3Singer.com.red.oo).mp3\n"
            "Saawariya-(MyMp3Singercom).mp3\n"
            "Samjhawan (Unplugged) - DownloadMing.SE\n"
            "jannat mash-up by dj kiran kamath - kbps [www.djmaza.com].mp3khalbali(mympsong.com).mp3")
ss = {1:'jannat mash-up by dj kiran kamath www.getlost.com - kbps [www.djmaza.com].mp3khalbali(mympsong.com)',2:'Samjhawan (Unplugged) www.somuchno.uk - DownloadMing.SE'}
for ke,ite in ss.items():
    matches = re.finditer(regex,ite, re.IGNORECASE | re.MULTILINE)
    print(ite)
    print('---------')
    diff = 0
    for matchNum, match in enumerate(matches):
        matchNum = matchNum + 1

        #print("Match {matchNum} was found at {start}-{end}: {match}".format(matchNum=matchNum, start=match.start(),
                                                         #                   end=match.end(), match=match.group()))

        ite = ite.replace(ite[(match.start()-diff):(match.end()-diff)], '')
        #print(ite)

        diff = match.end() - match.start()
        #print(diff)
        print(ite)

        ss[ke] = ite

        '''for groupNum in range(0, len(match.groups())):
            groupNum = groupNum + 1
            print("Group {groupNum} found at {start}-{end}: {group}".format(groupNum=groupNum, start=match.start(groupNum),
                                                                            end=match.end(groupNum),
                                                                            group=match.group(groupNum)))'''

regex2 = r"(\s?www.(.*?).com)|(\s?www.(.*?).pk)"

for ke, ite in ss.items():
    print('#################')
    matches = re.finditer(regex2, ite, re.IGNORECASE | re.MULTILINE)
    #print(ite)
    #print('---------')
    diff = 0
    for matchNum, match in enumerate(matches):
        matchNum = matchNum + 1

        #print("Match {matchNum} was found at {start}-{end}: {match}".format(matchNum=matchNum, start=match.start(),
                                                                            #end=match.end(), match=match.group()))
        print(ite)
        ite = ite.replace(ite[(match.start() - diff):(match.end() - diff)], '')
        print(ite)

        diff = match.end() - match.start()
        #print(diff)

        ss[ke] = ite

lkm = ["([\(\[]).*?([\)\]])","(\s?www.(.*?).com)|(\s?www.(.*?).pk)","(\s?([A-Z]*[a-z]*[0-9]*))\.com|((\s?([A-Z]*[a-z]*[0-9]*))\.pk)"]
for thing in lkm:
    print(r"{lk}".format(lk=thing))

non_dup_set = ['1','2','3','4','5','6','7','7','8','8','0','1','2','4','3','2','5','6']
dupl = {}
i = 1
for val in non_dup_set:
    dupl[val] = 0

print(dupl)

i=0
for val in non_dup_set:
    if val in dupl:
        i = i + 1
        if i > len(dupl) and i not in dupl:
            continue
        else:
            dupl[i] = dupl[i] + 1

print(dupl)

from collections import Counter
ma = Counter(non_dup_set)
print(ma)

print(abs(1-5))

lkms = {'aaaa':}

