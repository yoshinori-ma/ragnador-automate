import os
import win32gui
import pyautogui
import pydirectinput
import time
import win32con
import win32api
import sys
import input

sys.stdout = open("pyautogui.log", "w")
sys.stderr = open("pyautogui-err.log", "w")

KEEP_DIR = './screenshots'
if not os.path.exists(KEEP_DIR):
    # ディレクトリが存在しない場合、ディレクトリを作成する
    os.makedirs(KEEP_DIR)

def get_locate_from_filename(filename, sleep=0.1, confidence=0.95, timeout=None):
    locate = None
    elapsed_time=0
    while locate == None:
        time.sleep(sleep)
        #グレイスケールで検索
        locate = pyautogui.locateCenterOnScreen(filename, grayscale=True, confidence=confidence)
        #フルカラーで検索(遅い)
        #locate = pg.locateCenterOnScreen(filename)

        # timeout設定がある場合、sleepの時間で判定
        # TODO: ERROR投げる
        # TODO: 実実行時間で判定する
        # 実実行時間なら呼び出し側でやったほうがいいかな？
        if timeout:
           print(elapsed_time)
           elapsed_time = elapsed_time + sleep
           timeout <= elapsed_time
           break
    print(locate)
    return locate

# ラグナドのウィンドウ探してサイズ変更して左上に配置
def set_ragnador_window():
    rag = win32gui.FindWindow(None, 'ラグナド')
    win32gui.SetForegroundWindow(rag)
   #  time.sleep(1)
   #  hwnd = win32gui.GetForegroundWindow()
    win32gui.MoveWindow(rag, 0, 0, 800, 1200, True)

def click(x,y):
    while True:
        # pyautogui.moveTo(x,y,1)
        pydirectinput.moveTo(x,y)
        input.set_pos(x,y)
        now_x, now_y = pyautogui.position()
        print('expected', x, y)
        print('now', now_x, now_y)
        time.sleep(1)
        if (now_x == x) and (now_y == y):
            break
        set_ragnador_window()

    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,x,y,0,0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,x,y,0,0)

def click_by_file_name(file_name):
   button_position = get_locate_from_filename(file_name, confidence=0.65, timeout=5)
   x,y= button_position
   click(x,y);

# クエスト開始からの処理
def quest_routine():
    click(700, 300)

    while True:
        time.sleep(1);
        for file in ['images/retry.png', 'images/skip.png', 'images/close.png', 'images/ok.png']:
            pos= get_locate_from_filename(file, sleep=0.1, confidence=0.5, timeout=1)
            if pos:
                print(f'{file}見つけた{pos}')
                x,y=pos
                click(x, y)
                break


if __name__ == "__main__":
    # set_ragnador_window()
   # pyautogui.screenshot('screenshots/test.png' ,region=(0,0, 900,1200))
   # click_by_file_name('images/quest_icon.png')
    x,y = [1200,400]
    time.sleep(2)
    # pydirectinput.moveTo(x,y)
    time.sleep(2)
    # pyautogui.moveTo(x,y, 3)
    time.sleep(2)
    input.set_pos(x,y)
#    quest_routine()

    pass