import os

import re
brr = {1:'Saawariya-(MyMp3Singer.com.red.oo).mp3',2:'Saawariya-(MyMp3Singercom).mp3',3:'Samjhawan (Unplugged) - DownloadMing.SE',8:'jannat mash-up by dj kiran kamath - kbps [www.djmaza.com].mp3khalbali(mympsong.com).mp3'}

regex = r"([\(\[]).*?([\)\]])"
i =1
test_str = ("Saawariya-(MyMp3Singer.com.red.oo).mp3\n"
            "Saawariya-(MyMp3Singercom).mp3\n"
            "Samjhawan (Unplugged) - DownloadMing.SE\n"
            "jannat mash-up by dj kiran kamath - kbps [www.djmaza.com].mp3khalbali(mympsong.com).mp3")
for val in brr.values():
    matches = re.finditer(val, test_str, re.IGNORECASE)
    print(i)
    print(matches.__class__)
    for matchNum, match in enumerate(matches):
        matchNum = matchNum + 1

        print("Match {matchNum} was found at {start}-{end}: {match}".format(matchNum=matchNum, start=match.start(),
                                                                            end=match.end(), match=match.group()))

        for groupNum in range(0, len(match.groups())):
            groupNum = groupNum + 1

            print("Group {groupNum} found at {start}-{end}: {group}".format(groupNum=groupNum, start=match.start(groupNum),
                                                                            end=match.end(groupNum),
                                                                            group=match.group(groupNum)))

