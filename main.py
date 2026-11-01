#import relevant libraries
import pygame

# Initialize a window or screen for display
pygame.init()
screen = pygame.display.set_mode((800, 600))
canvas = pygame.Surface((800, 600))
white = (255, 255, 255)
red = (255, 0, 0)
pink = (255, 182, 193)
brush_size = 4
pygame.display.set_caption("The Sound of Art")
clock = pygame.time.Clock()


#fill canvas screen with color
canvas.fill ("white")
blue = (0, 100, 255)
black = (0, 0, 0)
green = (0, 128, 0)
yellow = (255, 255, 143)
colour = red

#import sound and make sure where audio is e.g c scale is lower than e scale
from pathlib import Path
folder = Path(__file__).parent
high = pygame.mixer.Sound(str(folder / "marimba high .wav"))
middle = pygame.mixer.Sound(str(folder / "marimba middle.wav"))
low = pygame.mixer.Sound(str(folder / "marimba low.wav"))
previous = None

channel = pygame.mixer.Channel(1)
current_sound = None

#font for captions + caption
font = pygame.font.SysFont("Arial", 15)
mode_font = pygame.font.SysFont("Arial", 13)
stop_button = pygame.Rect(650,15,130,40)

#save button
save_button = pygame.Rect(650, 65, 130, 40)

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                if stop_button.collidepoint(event.pos):
                    canvas.fill(white)
                    channel.stop()
                    current_sound = None
                    previous = None

                elif save_button.collidepoint(event.pos):
                    pygame.image.save(canvas, str(folder / "my_soundofart.png"))
                    print ("Drawing saved as my_soundofart.png")

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                canvas.fill(white)
                channel.stop()
                previous = None
            elif event.key == pygame.K_1:
                colour = red
            elif event.key == pygame.K_2:
                colour = blue
            elif event.key == pygame.K_3:
                colour = black
            elif event.key == pygame.K_4:
                colour = green
            elif event.key == pygame.K_5:
                colour = pink
            elif event.key == pygame.K_6:
                colour = yellow
            elif event.key == pygame.K_7:
                brush_size = 2
            elif event.key == pygame.K_8:
                brush_size = 4
            elif event.key == pygame.K_9:
                brush_size = 8
            elif event.key == pygame.K_e:
                colour = white



    # pinpoint where mouse is
    point = pygame.mouse.get_pos()

    # differentiating audio feedback
    if point[1] < 250:
        sound = high
    elif point[1] < 400:
        sound = middle
    else:
        sound = low
#drawing strokes
    if pygame.mouse.get_pressed()[0] and point[0] > 0:
        if colour == white:
            channel.stop()
            current_sound = None
        elif previous is None or sound!= current_sound:
            channel.play(sound)
            current_sound = sound



        if previous is not None:
            pygame.draw.line(canvas, colour, previous, point, brush_size * 2)

        pygame.draw.circle(canvas, colour, point, brush_size)
        previous = point
    else:
        channel.stop()
        current_sound = None
        previous = None

    # puts canvas in window TOP LEFT CORNER
    screen.blit(canvas, (0, 0))

    #instruction bubble because game starts immediately
    pygame.draw.rect(screen, (245, 214, 149), (20, 10, 300, 150),border_radius=12
    )

    lines = [
        "Start Drawing to hear the Sound of Art!",
        "For more colour options,",
        "Press 1 on the keypad for Red,",
        "2 for Blue, "
        "3 for Black",
        "4 for Green, "
        "5 for Pink & 6 for Yellow!"
    ]

    for i, text in enumerate(lines):
        message = font.render(text, True, (black))
        screen.blit(message, (30, 30 + i * 25))

#brush size
    pygame.draw.rect(screen, (245, 214, 149), (20, 180, 300, 70), border_radius = 12)
    message = font.render ("For Brush Sizes, Press 7 for Small,", True, black)
    screen.blit(message, (25, 195))

    message = font.render ("8 for Medium & 9 for Large!", True, black)
    screen.blit(message, (25, 220))

#clear button
    pygame.draw.rect(
        screen, (245, 214, 149), stop_button, border_radius=10)

    label = font.render("Clear Drawing", True, black)
    screen.blit(label, (stop_button.x + 10, stop_button.y + 10))


    #save button
    pygame.draw.rect(screen, (245, 214, 149), save_button, border_radius=10)
    label = font.render("Save Drawing", True, (black))
    screen.blit(label, (save_button.x +10, stop_button.y +60))

    # colour selector explanation
    pygame.draw.rect(screen, (245, 214, 149), (15, 350, 300, 100), border_radius=12)
    eraser_text = font.render("Press E to use the Eraser!", True, black)
    screen.blit(eraser_text, (20, 355))
    eraser_font = pygame.font.SysFont("Arial", 12)
    eraserbrushsize_text = eraser_font.render("(Pssst: Use the Brush Size buttons", True, black)
    screen.blit(eraserbrushsize_text, (20, 380))
    eraserbrushsize_text = eraser_font.render("to change the size of the eraser!)", True, black)
    screen.blit(eraserbrushsize_text, (20, 410))

    #differentiating between eraser and brush size
    if colour == white:
        mode_text = "Mode: Eraser"
    else:
        mode_text = "Mode: Brush"
    mode_box = pygame.Rect(15, 270, 300, 60)
    pygame.draw.rect(screen, (245, 214, 149), mode_box , border_radius=10)
    mode_label = font.render(mode_text, True, black)
    screen.blit(mode_label, (mode_box.x + 15, mode_box.y + 10))
    explanation_text = eraser_font.render ("To change back to brush,", True, black)
    screen.blit(explanation_text, (mode_box.x +15, mode_box.y + 30))
    explanation_text = eraser_font.render ("simply press 1-6 on the keypad & 7-9 for the eraser!", True, black)
    screen.blit(explanation_text, (mode_box.x + 15, mode_box.y + 45))

    #select colour button
    pygame.draw.circle(screen,colour, (600,35), 12)
    pygame.draw.circle(screen,black, (600,35), 12, 1)

    #guess what this button does
    pygame.draw.rect(screen, (245, 214, 149), (325, 10, 260, 50), border_radius=12)
    hint_text = mode_font.render("Can you guess what this circle shows -->?", True, black)
    screen.blit(hint_text, (330, 20))
    hint_text = mode_font.render("Press 1-6 and watch!", True, black)
    screen.blit(hint_text, (330, 40))


    pygame.display.flip()
    clock.tick(60)

pygame.quit()







