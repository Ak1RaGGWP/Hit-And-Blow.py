from datetime import datetime
import locale
locale.setlocale(locale.LC_CTYPE, "Japanese_Japan.932")
import random
from string import Template


class DeltaTemplate(Template):
    delimiter = "%"


def strfdelta(tdelta, fmt):
    d = {"D": tdelta.days}
    d["H"], rem = divmod(tdelta.seconds, 3600)
    d["M"], d["S"] = divmod(rem, 60)
    t = DeltaTemplate(fmt)
    return t.substitute(**d)


def generator(length):
    ans = []
    while len(ans) < length:
        rand = random.randint(0, 9)
        if rand in ans:
            pass
        else:
            ans += [rand]
    return ans


def hitblow(command, ans):
    hit = 0
    blow = 0
    for i in range(len(command)):
        if command[i] == ans[i]:
            hit += 1
        else:
            if command[i] in ans:
                blow += 1
    return [hit, blow]


while True:
    print("桁数を3～9の間で選択してください")
    digit = input()
    int_digit = int(digit)

    if 3 <= int_digit <=9:
        print(str(int_digit) + "桁に設定しました")
        break
    else:
        print("範囲外の桁数が入力されました。もう一度入力してください")

ans = generator(int_digit)
count = 0
st = (datetime.now())

while True:
    count += 1
    print("設定された" + str(int_digit) + "桁の値を予想し入力してください \n外れると当たりの数と桁違いの数がヒントとして表示されます")
    command = input()
    your_ans = [int(command[i]) for i in range(len(command))]
    [hit, blow] = hitblow(your_ans, ans)
    if hit == len(ans):
        et = (datetime.now())
        ct = (et-st)
        print(f"おめでとうございます！正解です！ \n{count}回目 入力した値:{command} タイム:" + strfdelta(ct, "%H時間%M分%S秒")) 
        break
    else:
        print(f"{count}回目 入力した値:{command} \n 当たり:{hit}  桁違い:{blow}")