import pyautogui
import cv2
import numpy as np

resolution = pyautogui.size()
fps = 60
codec = cv2.VideoWriter.fourcc(*"XVID")
filename = "test.avi"
main_screen = cv2.imread("main_screen.png")

output = cv2.VideoWriter(filename, codec, fps, resolution)

print("[Screen redorder]: Start recording...")
while True:
    screenshot = pyautogui.screenshot()
    frame = np.array(screenshot)
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    output.write(frame)


    # Doing this to check only the last bits,
    # It might differ from platform the most significant bits, but the end is quite
    # same
    cv2.imshow('Live', main_screen)
    if cv2.waitKey(1) == ord("q"):
        break

output.release()
cv2.destroyAllWindows()
print(f"[Screen recorder]: Recording stopped, saved on {filename}")

