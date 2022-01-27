import os
import pyautogui
import time
import sys

# sys.stdout = open("pyautogui.log", "w")
# sys.stderr = open("pyautogui-err.log", "w")

REGION=(0,100,860,1750)
KEEP_DIR = './screenshots'
if not os.path.exists(KEEP_DIR):
    # ディレクトリが存在しない場合、ディレクトリを作成する
    os.makedirs(KEEP_DIR)

def get_locate_from_filename(filename, sleep=0.1, confidence=0.95, times=1, grayscale=True):
    locate = None
    done = 0
    while locate == None:
        locate = pyautogui.locateCenterOnScreen(filename, grayscale=grayscale, confidence=confidence, region=REGION)
        print(filename,locate)

        if times:
           done = done + 1
           if done >= times:
             break
            
           time.sleep(sleep)
    print(locate)
    return locate

def click(x,y):
    pyautogui.moveTo(x,y)
    pyautogui.dragTo(button='left')

def click_by_file_name(file_name):
   button_position = get_locate_from_filename(file_name, confidence=0.55, timeout=5)
   x,y= button_position
   # retinaなので半分にする
   click(x/2,y/2);

def quest_target_locate():
    pos = get_locate_from_filename('images/quest_target.png', confidence=0.6, times=1, grayscale=True)


    if pos:
        x,y = pos
        # 範囲が正しいか確認
        # (520,450,300,100)
        if 520 <= x and x <= 820 and 450 <= y and y <= 550:
            print(f'quest_target見つけた{pos}')
            return pos

    return None

def retry_locate():
    pos = get_locate_from_filename('images/retry.png', confidence=0.7, times=1, grayscale=True)
    if pos:
        print(f'retry見つけた{pos}')
    return pos

# 一旦無視
def skip_locate():
    pos = get_locate_from_filename('images/skip.png', confidence=0.7, times=1, grayscale=True)
    if pos:
        print(f'skip見つけた{pos}')
    return pos

def skip_ok_locate():
    pos = get_locate_from_filename('images/skip_ok.png', confidence=0.7, times=1, grayscale=True)
    if pos:
        print(f'skip_ok見つけた{pos}')
    return pos

def quest_skip_locate():
    pos = get_locate_from_filename('images/quest_skip.png', confidence=0.7, times=1, grayscale=True)
    if pos:
        print(f'quest_skip見つけた{pos}')
    return pos

def close_locate():
    pos = get_locate_from_filename('images/close.png', confidence=0.7, times=1, grayscale=True)
    if pos:
        print(f'close見つけた{pos}')
    return pos

def touch_locate():
    pos = get_locate_from_filename('images/touch.png', confidence=0.7, times=1, grayscale=True)
    if pos:
        print(f'touch見つけた{pos}')
    return pos

def ok_locate():
    pos = get_locate_from_filename('images/quest_ok.png', confidence=0.7, times=1, grayscale=True)
    if pos:
        print(f'ok見つけた{pos}')
    return pos

# クエスト開始からの処理
def quest_routine():
    while True:
        result1 = [quest_target_locate(), retry_locate(), skip_ok_locate(), touch_locate(), quest_skip_locate(), close_locate(), ok_locate()]

        # 見つかったものが一つも無ければbreak
        if not any(result1):
            print('1個も見つからず')
            continue

        result2 = [quest_target_locate(), retry_locate(), skip_ok_locate(), touch_locate(), quest_skip_locate(), close_locate(), ok_locate()]

        # 2回とも認識できた画像が同じでなければbreak
        if not list(map(lambda x: x != None, result1)) == list(map(lambda x: x != None, result2)):
            print('2回同じじゃない')

            continue

        # 見つかった中で一番優先度が高いものを取得
        pos = next(filter(lambda x: x != None, result1), None)

        x,y=pos
        click(x/2, y/2)
        time.sleep(3);


if __name__ == "__main__":
    # set_ragnador_window()
    # pyautogui.screenshot('screenshots/test.png' ,region=REGION)
   # click_by_file_name('images/quest_icon.png')
#    (0,100,860,1750)
    # pyautogui.screenshot('screenshots/skip.png' ,region=(520,450,300,100))
    # アクティブにする
    click(100,100)
    # click_by_file_name('images/quest_target.png')
    quest_routine();
    # pyautogui.screenshot('screenshots/test.png' ,region=(0,100, 860,1750))
    # x,y = [1200,400]
    # x,y = [0,0]
    # pyautogui.moveTo(x,y, 1)

    pass