from ctypes import windll, Structure, c_long, byref
import time
import mss
from mss import tools
import json


class POINT(Structure):
    _fields_ = [("x", c_long), ("y", c_long)]


def queryMousePosition():  # определяем позицию мышки
    pt = POINT()
    windll.user32.GetCursorPos(byref(pt))
    return {"x": pt.x, "y": pt.y}


def mouse_position():
    sct = mss.mss()
    print("STARTING after 5 seconds")
    time.sleep(5)
    print("Started ...")

    print('Приготовиться к захвату позиции курсора')
    print("Старт захвата через 3 секунды")
    time.sleep(3)
    cur = queryMousePosition()
    mon = {"top": cur['y'] - 1, "left": cur['x'], "width": 25, "height": 18}  # передача координат мышки для скриншота
    # mon = {"top": 500, "left": 0, "width": 370, "height": 285}
    # передача координат мышки для скриншота
    # top - верх (поднять вверх - убывание)
    # left левая нижняя(сдвинуть в право - увеличение)
    # width - правая (утянуть в право - увеличение)
    # height - низ(утянуть вниз - увеличение)
    print('Позиция захвачена')
    output = f"screen_control_mouse_poss.png".format(**mon)
    img2 = sct.grab(mon)
    mss.tools.to_png(img2.rgb, img2.size, output=output)

    if mon:
        with open("mouse_poss.json", "w") as file:
            json.dump(mon, file)

if __name__ == "__main__":
    mouse_position()