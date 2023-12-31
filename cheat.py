import pytesseract
import cv2
import re
import pyautogui
import time
import keyboard
import ctypes

""" Answer Dictionary """

answers = {
    "Name a day of the week": "Wednesday",
    "Name any popular animal that starts with the letter C": "Caterpillar",
    "Name any capital city in Europe": "Andorra la Vella",
    "Name a country that starts with the letterrN": "Antigua and Barbuda",
    "Name a popular electronic device": "PlayStation Controller",
    "Name a famous Roblox Youtuber" : "Inquisitormaster",
    "Name one of the fastest animals" : "Swordfish",
    "Name an animal that can fly" : "Western Honey Bee",
    "Name a food that starts with the letter P" : "Passion Fruit",
    "Name any month that has 31 days" : "December",
    "Name a musical instrument" : "Orchestral Bells",
    "Name any natural hair color" : "Brunette",
    "Name one of the four seasons" : "Autumn",
    "Name any part of the head" : "Forehead",
    "Name a planet in our solar system" : "Mercury",
    "Name a popular Superhero" : "Captain America",
    "Name a popular fruit" : "Passion Fruit",
    "Name one of the world's most popular car colors" : "Orange",
    "Name a popular game on Roblox" : "Natural Disaster Survival",
    "Name a popular vegetable" : "Cauliflower",
    "Name a red fruit" : "Red Passionfruit",
    "Santa's Reindeers" : "Rudolph",
    "Name a social media app" : "Facebook Messenger",
    "Name something people wear" : "Contact Lenses",
    "What is something you can sit on" : "rockingchair",
    "Name something you do at school" : "Physical Education",
    "Name something you do in your sleep" : "Nightmare",
    "Name something you eat with" : "Ice Cream Spoon",
    "What is something you eat with yourhands" : "Chicken Nuggets",
    "Name something you find on pizza" : "Mozzarella Cheese",
    "Something we know" : "Copy and Paste",
    "Name a famous sport that is played inteams" : "American Football",
    "Santa's reindeers" : "Rudolph",
    "Name a topping that is usually in ahamburger" : "American Cheese",
    "Name a type of transport" : "Skateboard",
    "Name a type of weather" : "Thunderstorm",
    "Name one of the world's coldest countries" : "United States of America",
    "Name one of the world's hottest countries" : "Democratic Republic of the Congo",
    "Name a shape" : "Parallelogram",
    "Name an animal that walks slowly" : "caterpillar",
    "Name a planet that is part of our solarsystem" : "Jupiter"
}

def is_caps_lock_on():
    return ctypes.windll.user32.GetKeyState(0x14) != 0

""" Code: """


while True:
    
    if is_caps_lock_on():
        print("Disabled")
    else:
        
        """ Get Screenshot """

        # Path to the Tesseract executable (change this to your Tesseract installation path)
        pytesseract.pytesseract.tesseract_cmd = r'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

        # Capture a screenshot of the screen
        screenshot = pyautogui.screenshot(region=(565,60,800,100))

        # Save the screenshot to a file (optional)
        screenshot.save('screenshot.jpg')
        
        # Determine pixel color
        image = cv2.imread('screenshot.jpg')
        pixel_color = image[5,5]
        
        # Extract the RGB values
        blue, green, red = pixel_color

        # Print the RGB values
        print(f"Red: {red}, Green: {green}, Blue: {blue}")
        
        red_bool = (red >= 39) and (red <= 43)
        green_bool = (green >= 165) and (green <= 175)
        blue_bool = (blue >= 248) and (blue <= 258)
        
        if (red_bool and green_bool and blue_bool):

            im_gray = cv2.imread('screenshot.jpg', cv2.IMREAD_GRAYSCALE)
            (thresh, im_bw) = cv2.threshold(im_gray, 128, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)

            cv2.imwrite('screen_bw.png', im_bw)

            #test = cv2.imread('screen_bw.png')
            #cv2.imshow('ah', test)

            #cv2.waitKey(0)
            #cv2.destroyAllWindows()

            text = pytesseract.image_to_string('screen_bw.png')

            # Print the extracted text
            print(repr(f"Question: {text}"))

            """ Clean input """
            text = re.sub("\n", "", text)



            """ Get answer """

            try: 
                
                answer = answers[text]
                
                print(f"The Answer: {answer}")
                
                # Click text box and type
                pyautogui.click(960, 1075)
                pyautogui.click(960, 1080)
                pyautogui.click(960, 1085)
                time.sleep(0.1)
                pyautogui.typewrite(answer)
                
                # Click Enter
                keyboard.press_and_release('enter')
                
            except KeyError:
                print('NOT IN ANSWERS')














