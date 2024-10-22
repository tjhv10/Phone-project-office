import time
import random
import threading
from common_area import *


def tap_users(d, users_template_path="icons/tiktok_icons/users.png"):
    """
    Takes a screenshot and tries to tap on the like button if found.
    """
    screenshot_path = take_screenshot(d,threading.current_thread().name,"tik")
    best_coordinates = find_best_match(screenshot_path, users_template_path,d)
    if best_coordinates:
        d.click(int(best_coordinates[0]), int(best_coordinates[1]))
    else:
        print(f"{threading.current_thread().name}:{d.wlan_ip} Users button not found on the screen.")
   

def search(d, text):
    """
    Searches for a specific user on TikTok by simulating clicks and typing.
    """
    screen_width = d.info['displayWidth']
    screen_height = d.info['displayHeight']
    
    x = screen_width * (650 / 720)
    y = screen_height * (100 / 1560)

    
    d.click(x, y)  # Click on the search bar
    time.sleep(4)
    tap_keyboard(d,text)
    time.sleep(5)
    d.press(66)  # Press the search button
    time.sleep(6)

    tap_users(d)  # Click to go to users
    time.sleep(5)

    d.click(700, 300)  # Click to go into the first result
    time.sleep(4)
    
        

def tap_like_button(d, like_button_template_path="icons/tiktok_icons/like.png"):
    print(f"{threading.current_thread().name}:{d.wlan_ip} Starting tap_like_button function")
    screenshot_path = take_screenshot(d,threading.current_thread().name,"tik")
    time.sleep(2)
    best_coordinates = find_best_match(screenshot_path, like_button_template_path,d)
    time.sleep(2)
    if best_coordinates:
        print(f"{threading.current_thread().name}:{d.wlan_ip} Like button found at {best_coordinates}, tapping...")
        d.click(int(best_coordinates[0]), int(best_coordinates[1]))
        print(f"{threading.current_thread().name}:{d.wlan_ip} Tapped best match at {best_coordinates}.")
        time.sleep(1)
    else:
        print(f"{threading.current_thread().name}:{d.wlan_ip} Like button not found on the screen.")
    print(f"{threading.current_thread().name}:{d.wlan_ip} Finished tap_like_button function")

def comment_text(d, text):
    """
    Comments on a post using the regular keyboard.
    """
    d.click(670, 1000)  # Click on the comment button
    print(f"{threading.current_thread().name}:{d.wlan_ip} Clicked on the comment button.")
    time.sleep(3)
    d.click(310, 1500)  # Click on the comment input field
    print(f"{threading.current_thread().name}:{d.wlan_ip} Commenting: {text}")
    
    time.sleep(4)  # Wait for the input field to be ready
    
    tap_keyboard(d,text)
    
    time.sleep(2)  # Give some time for the input to be registered
    
    d.click(650, 1000)  # Click the submit button for the comment
    print(f"{threading.current_thread().name}:{d.wlan_ip} Comment submitted.")
    time.sleep(3)
    d.press("back")

def scroll_random_number(d):
    """
    Scrolls down a random number of times in a scrollable view.
    """
    screen_width = d.info['displayWidth']
    screen_height = d.info['displayHeight']
    
    if d(scrollable=True).exists:
        print(f"{threading.current_thread().name}:{d.wlan_ip} Found a scrollable view! Swiping down...")
        num_swipes = random.randint(1, 2)
        print(f"{threading.current_thread().name}:{d.wlan_ip} Number of swipes: {num_swipes}")

        for i in range(num_swipes):
            x_start = screen_width * (500 / 720)
            y_start = screen_height * (1200 / 1560)
            x_end = screen_width * (500 / 720)
            y_end = screen_height * (300 / 1560)
            d.swipe(x_start, y_start, x_end, y_end, duration=0.05)
            random_time = random.randint(2, 15)
            time.sleep(random_time)
            print(f"{threading.current_thread().name}:{d.wlan_ip} Swiped down {i + 1} time(s).")
    else:
        print(f"{threading.current_thread().name}:{d.wlan_ip} No scrollable view found!")


def scroll_like_and_comment(d):
    """
    Scrolls the view and likes posts.
    """
    tap_like_button(d)
    screen_width = d.info['displayWidth']
    screen_height = d.info['displayHeight']

    for i in range(3):
        if d(scrollable=True).exists:
            x_start = screen_width * (500 / 720)
            y_start = screen_height * (1200 / 1560)
            x_end = screen_width * (500 / 720)
            y_end = screen_height * (300 / 1560)
            d.swipe(x_start, y_start, x_end, y_end, duration=0.05)
            random_time = random.randint(2, 15)
            time.sleep(random_time)
            print(f"{threading.current_thread().name}:{d.wlan_ip} Swiped down {i + 1} time(s).")
        else:
            print(f"{threading.current_thread().name}:{d.wlan_ip} No scrollable view found!")
        num = random.choice([1, 2, 3, 4, 5])
        if  num <= 2:
            print("like")
            tap_like_button(d)
            time.sleep(1)
        elif num>2 and num<=4:
            print("like and comment")
            tap_like_button(d)
            time.sleep(2)
            comment_text(d,random.choice(israel_support_comments))
            time.sleep(1)
        else:
            print("none")
    d.press("back")
    d.press("back")
    time.sleep(2)
    d.press("back")
    time.sleep(2)
    d.press("back")
    time.sleep(4)
    d.press("back")


def like_the_page(d, page):
    search(d, page)
    time.sleep(2)
    d.click(120, 1300) # Get in the first page
    time.sleep(3)
    scroll_like_and_comment(d)


def main(d):
    """
    Main function to connect to the device and perform actions on TikTok.
    """
    d.app_start("com.zhiliaoapp.musically")  # Open TikTok app
    print(f"{threading.current_thread().name}:{d.wlan_ip} :Opened TikTok!")
    time.sleep(15)
    if "com.zhiliaoapp.musically" in d.app_list_running():
        print(f"{threading.current_thread().name}:{d.wlan_ip} TikTok is running!")
        for _ in range(3):
            scroll_random_number(d)
            # time.sleep(1)
            # tap_like_button(d)
            time.sleep(4)
            like_the_page(d,random.choice(tiktok_accounts))
            scroll_random_number(d)
            time.sleep(10)
        d.app_stop("com.zhiliaoapp.musically")
        time.sleep(4)
    else:
        print(f"{threading.current_thread().name}:{d.wlan_ip} TikTok is not running!")
    print(f"{threading.current_thread().name}:{d.wlan_ip} done")
