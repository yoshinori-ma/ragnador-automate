import os
import pyautogui
import time
import sys
import subprocess

# sys.stdout = open("pyautogui.log", "w")
# sys.stderr = open("pyautogui-err.log", "w")

retry_pushed = False
quest_started = False
REGION=(0,100,860,1750)
KEEP_DIR = './screenshots'
if not os.path.exists(KEEP_DIR):
    # ディレクトリが存在しない場合、ディレクトリを作成する
    os.makedirs(KEEP_DIR)

class Position:
    def __iter__(self):
        yield from [self.x, self.y]

def get_locate_from_filename(filename, sleep=0.1, confidence=0.95, times=1, grayscale=True):
    locate = None
    done = 0
    while locate == None:
        locate = pyautogui.locateCenterOnScreen(filename, grayscale=grayscale, confidence=confidence, region=REGION)
        # print(filename,locate)

        if times:
           done = done + 1
           if done >= times:
             break
            
           time.sleep(sleep)
    # print(locate)
    return locate

def click(x,y):
    pyautogui.moveTo(x,y)
    pyautogui.dragTo(button='left')

def is_good_friends(c1, c2, threshold=15):
    r,g,b = c1
    r2, g2, b2 = c2
    ret = subprocess.run('node index.js {} {} {} {} {} {}'.format(r,g,b,r2,g2,b2), stdout=subprocess.PIPE, shell=True, text=True).stdout.strip()
    print(ret)
    result = float(ret) < threshold

    return result


def quest_target_locate():
    pos = get_locate_from_filename('images/quest_target.png', confidence=0.6, times=1, grayscale=True)


    if pos:
        x,y = pos
        # 範囲が正しいか確認
        # (520,450,300,100)
        if 520 <= x and x <= 820 and 450 <= y and y <= 550:
            print(f'quest_target見つけた{pos}')
            p = Position()
            p.x = x + 140
            p.y = y + 30
            pyautogui.moveTo(530/2,492/2)
            rgb = pyautogui.pixel(530, 492)
            print(rgb)
            threshold = int(os.environ.get('THRESHOLD', 22))
            if is_good_friends([43,64,90], rgb, threshold):
                print('青い')
                global quest_started
                quest_started = True
                return p
            else:
                print('青くないので押さない')

    return None

def retry_locate():
    pos = get_locate_from_filename('images/retry.png', confidence=0.8, times=1, grayscale=True)
    if pos:
        global retry_pushed
        retry_pushed = True
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
        x,y = pos
        # 範囲が正しいか確認
        # (520,450,300,100)
        if y >= 1200:
            print(f'close見つけた{pos}')
            return pos

    return None

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
    global quest_started, retry_pushed

    start = time.time()
    last_cleared_at = time.time()
    functions = [quest_target_locate, retry_locate, skip_ok_locate, quest_skip_locate, touch_locate, close_locate, ok_locate]
    quest_clear_count = 0
    last_match_index = None
    reset_continue_count = 0
    while True:
        if (not quest_started) and retry_pushed:
            # 再挑戦からスタートしたとき対策
            retry_pushed = False
            quest_started = False
            reset_continue_count = reset_continue_count + 1
            if reset_continue_count > 10:
                # 何回も再挑戦押してて進まないので終了
                print('終了')
                print('-----------------------------------------------')
                print(f'{quest_clear_count}回周回')
                print(f'合計: {time.time() - start}秒')
                print('-----------------------------------------------')
                break
        else:
            reset_continue_count = 0


        if retry_pushed and quest_started:
            quest_clear_count = quest_clear_count + 1
            print('-----------------------------------------------')
            print(f'{quest_clear_count}回周回')
            print(f'今回の周回: {time.time() - last_cleared_at}秒')
            print(f'合計: {time.time() - start}秒')
            print('-----------------------------------------------')
            retry_pushed = False
            quest_started = False
            last_cleared_at = time.time()

        for index, f in enumerate(functions):
            pos = f()
            if pos:
                if last_match_index == index:
                    x,y=pos
                    click(x/2, y/2)
                    time.sleep(1);
                else:
                    last_match_index = index

                # for 最初から
                break


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
    # quest_target_locate()
    # pyautogui.screenshot('screenshots/test.png' ,region=(0,100, 860,1750))
    # x,y = [1200,400]
    # x,y = [0,0]
    # pyautogui.moveTo(x,y, 1)

    pass