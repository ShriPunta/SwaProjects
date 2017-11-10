import re

regex = r"([\(\[]).*?([\)\]])"

test_str = ("Saawariya-(MyMp3Singer.com.red.oo).mp3\n"
            "Saawariya-(MyMp3Singercom).mp3\n"
            "Samjhawan (Unplugged) - DownloadMing.SE\n"
            "jannat mash-up by dj kiran kamath - kbps [www.djmaza.com].mp3khalbali(mympsong.com).mp3")
ss = {1:'jannat mash-up by dj kiran kamath - kbps [www.djmaza.com].mp3khalbali(mympsong.com)',2:'Samjhawan (Unplugged) - DownloadMing.SE'}
for ke,ite in ss.items():
    matches = re.finditer(regex,ite, re.IGNORECASE | re.MULTILINE)
    print(ite)
    print('---------')
    diff = 0
    for matchNum, match in enumerate(matches):
        matchNum = matchNum + 1

        print("Match {matchNum} was found at {start}-{end}: {match}".format(matchNum=matchNum, start=match.start(),
                                                                            end=match.end(), match=match.group()))

        ite = ite.replace(ite[(match.start()-diff):(match.end()-diff)], '')
        print(ite)

        diff = match.end() - match.start()
        print(diff)

        '''for groupNum in range(0, len(match.groups())):
            groupNum = groupNum + 1
            print("Group {groupNum} found at {start}-{end}: {group}".format(groupNum=groupNum, start=match.start(groupNum),
                                                                            end=match.end(groupNum),
                                                                            group=match.group(groupNum)))'''

import random
import math
rand = random.random()
print(rand)
if rand < 1:
    print('Cool')
    rand = math.floor(rand * 100000)
print(rand)
