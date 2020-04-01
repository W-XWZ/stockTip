import realtime_sina as sina
import tkinter
import tkinter.messagebox  # 这个是消息框，对话框的关键
import time
import traceback


def loopAndTip(symbol, close_price, percent, lowerPercent):
    data = []
    try:
        data = sina.singleStockData(symbol)
        price = float(data[3])
        print(price)
        if price > close_price * (1 + percent / 100):
            tkinter.messagebox.showinfo('提示', '人生苦短')
            return True
        elif price < close_price * (1 - lowerPercent / 100):
            tkinter.messagebox.showwarning('警告', '明日有大雨')
            return True
        else:
            return False
    except Exception:
        traceback.print_exc()
        tkinter.messagebox.showwarning('警告', '爬取失败"')
        return True


while True:
    if loopAndTip('603220', 20.81, 5, 5):
        break
    time.sleep(5)
