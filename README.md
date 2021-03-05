# CreativeEmbeddedSystemsProj3

Description: This is a program for a wireless mood tracker that takes in data from a keypad connected to the esp32 and transmits that input via wifi to a laptop or other computer. 

Video Link: https://youtu.be/j6JdFV1zxEE

Hardware Required:
  -esp32
  -lipo battery (this is used in my example but can be substituted for two AA batteries)
  -numbered keypad
  -10 male to male wires
  
Wiring:
  **moving from left to right on the keypad inputs if the keypad is placed infront of you** 
  -input 1 to GPIO 13
  -input 2 to GPIO 27
  -input 3 to GPIO 26
  -input 4 to GPIO 25
  -input 5 to GPIO 13
  -input 6 to GPIO 21
  -input 7 to GPIO 22
  -input 8 to GPIO 23
  
  -For the lipo battery, connect red to 5v and black to ground
  
How To:
  1. Connect the keypad by wiring as stated above
  2. Upload the .ino code to the esp32 via the Arduino IDE
  3. Use the serial monitor to print the ip of the esp32 and replace my ip with yours in the python code
  4. Connect the battery to the esp32
  5. Run the python program on your laptop or other computer and enjoy!



Enclosure:
  The enclosure is an old keyboard box painted over and decorated. I used an exacto knife to cut a hole for the heypad
 and stacked small books inside to prop it up so that it was easy to press!

![IMG_5706](https://user-images.githubusercontent.com/46966950/110146560-b6d01500-7da8-11eb-9fda-7ecd588e9ea8.jpg)

![IMG_5693](https://user-images.githubusercontent.com/46966950/110135597-b16ccd80-7d9c-11eb-83e5-527cd9f817da.jpg)
![IMG_5692](https://user-images.githubusercontent.com/46966950/110135719-d7926d80-7d9c-11eb-90b5-db27fadd6d34.jpg)
![IMG_5708](https://user-images.githubusercontent.com/46966950/110150385-37911000-7dad-11eb-8be2-dde70736b0fc.jpg)
