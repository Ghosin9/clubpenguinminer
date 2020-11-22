from PIL import ImageGrab
import numpy as np
import cv2
import time
import pyautogui

# game coords= top left: 470, 222, bot right: 1450x840, size: 980 x 618
# sand area [[640, 770], [640, 660], [770, 660], [770, 590], [1170, 590], [1280, 670], [1230, 770]]
vertices = np.array([[170, 548], [170, 448], [300, 448], [300, 378], [700, 378], [810, 458], [760, 548]])
#starting time of program
start_time = time.time()

#points
points = [[1100, 600], [1030, 600], [1030, 670], [1030, 740], [960, 740], [1030, 740], [1030, 670], [960, 670], [960, 600], [960, 670], [1030, 670], [1100, 670], [1100, 740]]

def roi(img, vertices) :
    mask = np.zeros_like(img)
    cv2.fillPoly(mask, vertices, color=[255, 255, 255])
    masked = cv2.bitwise_and(img, mask)
    masked = cv2.cvtColor(masked, cv2.COLOR_BGR2RGB)
    return masked

def main():
    loop = True
    x = 0
    while loop:

        screen = np.array(ImageGrab.grab(bbox=(470, 222, 1450, 840)))
        new_screen = roi(screen, [vertices])
        cv2.imshow("window", new_screen)
        print(screen[points[x][1]-222, points[x][0]-470])

        pyautogui.click(points[x][0], points[x][1], button="left", duration=0.5)
        time.sleep(1)
        pyautogui.press("d")
        time.sleep(10)

        if x < 12:
            x += 1
        else:
            x = 0

        if cv2.waitKey(25) & 0xFF == ord("q"):
            cv2.destroyAllWindows()
            loop = False
            break

main()