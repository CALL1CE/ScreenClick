from screen_clicker import WindowClicker
import win32api
import time
def main():
    print("Hello from screenclick!")
    start_time = time.time()
    while True:
        # 如果按ESC则推出循环
        if win32api.GetAsyncKeyState(0x1B):
            print("ESC pressed, exiting...")
            break
        window_clicker = WindowClicker("23013RK75C")
        print(f"Window Clicker initialized for: {window_clicker.window_title}")
        window_clicker.click(int(window_clicker.width * 0.5),int( window_clicker.height * 0.5))  # Example click at (100, 100) relative to the window
        time.sleep(0.2)
    time_elapsed = time.time() - start_time
    hours = int(time_elapsed // 3600)
    minutes = int((time_elapsed % 3600) // 60)
    seconds = int(time_elapsed % 60)
    print(f"Time elapsed: {hours} hours, {minutes} minutes, {seconds} seconds")
if __name__ == "__main__":
    main()
