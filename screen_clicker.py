'''
author: CALL1CE
LastEditors: CALL1CE
'''
import win32gui
import win32con
import win32api
import time

class WindowClicker:
  def __init__(self, window_title):
    self.window_title = window_title
    self.hwnd = win32gui.FindWindow(None, window_title)
    if not self.hwnd:
      raise Exception(f"Window '{window_title}' not found.")
    
    rect = win32gui.GetWindowRect(self.hwnd)
    self.width = rect[2] - rect[0]
    self.height = rect[3] - rect[1]

  def click(self, x, y):
    # Bring window to foreground
    win32gui.SetForegroundWindow(self.hwnd)
    # Calculate absolute screen coordinates
    rect = win32gui.GetWindowRect(self.hwnd)
    abs_x = rect[0] + x
    abs_y = rect[1] + y
    # Move mouse and click
    win32api.SetCursorPos((abs_x, abs_y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, abs_x, abs_y, 0, 0)
    time.sleep(0.02)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, abs_x, abs_y, 0, 0)