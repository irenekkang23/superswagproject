_**The Sound of Art**_


**Introduction**

Hello! This is The Sound of Art, an interactive Python application created using Pygame in PyCharm, built to engage primary school students in Years 4-6. 

Users can draw while listening to live audio feedback that changes in response to their mouse's current position. 

**Features:**
- Multiple colours
- Adjustable brush & eraser sizes
- A button to clear your drawing from the screen
- A "save drawing" feature that will save your current drawing as a .png image in the project folder
- A small easter egg -> a small colour indicator at the top right of the screen - try changing colours and see what happens!

**How To Setup and Run The Sound of Art**
1. Install Python 3 and PyCharm on your computer.
2. Download or copy this repository. If downloading as a ZIP folder, you will need to extract the repository ZIP.
3. Open PyCharm, select Open and choose this/paste this repository. (Open the extracted folder in PyCharm).
4. Select a **Python** interpreter for the project if asked.
5. Install Pygame in PyCharm by writing:
   python -m pip install pygame
6. Make sure these audio files are in the same folder as main.py:
   marimba high .wav
   marimba middle.wav
   marimba low.wav
   The filenames **must match the code exactly, including the space before .wav in "**marimba high .wav****
7. Open main.py, right click inside the editor and select Run.
8. A separate window titled "The Sound of Art" will open.
9. Hold the left mouse button and drag to start drawing and hear audio feedback. Make sure the volume is up!

**How To Use The Sound of Art Features**
  1. Pressing 1-6 on the keyboard will change brush colour:
     1 = Red, 2 = Blue, 3 = Black, 4 = Green, 5 = Pink, 6 = Yellow
  2. Change the brush size by pressing 7-9 on the keyboard:
     7 = Small, 8 = Medium, 9 = Large
  3. Press E to activate the eraser.
  4. Eraser size changes using the same 7,8,9 brush sizes.
  5. The "Mode:Eraser" bubble on the left will let you know if you are currently using the eraser or brush!
  6. The top right "Clear Drawing" will clear any brush strokes on the current screen.
  7. Beneath, the "Save Drawing" will save your current drawing as a .png in your project folder in PyCharm.
  8. Put your volume up before you begin!

**Coding Examples in my Application** 
1. Saving a drawing:
When "Save Drawing"is clicked, the canvas is saved as a PNG image in the project folder.

```python
elif save_button.collidepoint(event.pos):
    pygame.image.save(canvas, str(folder / "my_soundofart.png"))
    print("Drawing saved as my_soundofart.png")
```

This condition sits inside the left mouse-button event handler. 
```event.pos``` stores the position where the mouse was clicked. 
```"collidepoint"``` checks if "Save Drawing" was clicked. 
```(folder/ "my_soundofart.png")``` sets where it is saved and it's filename.
```print()``` confirms the save in PyCharm's console. 
(Pressing "Save Drawing" will replace the previously saved image!)


2. Selecting the right sound depending on mouse position 

The mouse position is stored as an (x, y) pair. point[1] represents the vertical position. 
(These conditions select a sound based on how far down the window the mouse is!)

```python
point = pygame.mouse.get_pos()

if point[1] < 250:
    sound = high
elif point[1] < 400:
    sound = middle
else:
    sound = low
```

```point = pygame.mouse.get_pos()``` gets the mouse position as (x,y):
point [0] is the horizontal position
point [1] is the vertical position 
The top of the screen is y = 0. The number increases as the mouse moves downwards.
Using ```if, elif and else``` statements selects the high, middle or low sound according to the mouse’s vertical position.

3. Creating continuous strokes 

```python
if previous is not None:
     pygame.draw.line(canvas, colour, previous, point, brush_size * 2)

pygame.draw.circle(canvas, colour, point, brush_size)
previous = point
```

as point contains the current mouse position from ```point = pygame.mouse.get_pos()```, ```previous = point``` stores that position so it can be used as the starting point for the next line. 

```if previous is not None:``` = checks whether a previous position exists 
```pygame.draw.line``` draws a line on the canvas between 'previous' and 'point'. 
```brush_size * 2``` sets the line thickness to match the circle's diameter. 
```pygame.draw.circle()``` draws a circle at the current mouse position to give rounded ends. 

**Challenges**
Learning how to code with minimal to no knowledge on coding or Python and its libraries was the biggest challenge. 

**Planned Improvements**
1. Get peers to test and review to make any final adjustments.
2. The text caption box is currently not aligned.

**Future Goals**
1. Different audio sounds
2. Play and stop buttons
3. Undo button
4. Redo button
5. Opacity feature
6. Mode to collaborate so multiple users can access the same canvas. 

**Project Overview**
My application, The Sound of Art, can successfully provide live audio feedback when drawing on the canvas. However, it does not fully encapsulate the full-featured version I had originally planned. Due to unforeseen circumstances and the underestimated time constraints, I was unable to implement more features such as "undo/redo", a wider range of sounds and opacity. However, I was able to reflect and learn valuable lessons and am proud of what my application can provide in the current version. 

**Acknowledgements**
Official Pygame documentation: https://www.pygame.org/docs/
Project inspiration: https://playmusictheory.net/play
Python Learning Career Hub: https://www.linkedin.com/learning/python-for-students-2023
In-class seminar/tutorials assisted in the development of interface and creating shapes and inserting colour. 

Audio credits: 
marimba high .wav: https://freesound.org/people/heyheytheree/sounds/873077/
marimba middle.wav:https://freesound.org/people/zagi2/sounds/240347/
marimba low.wav: https://freesound.org/people/nickgar/sounds/120541/






