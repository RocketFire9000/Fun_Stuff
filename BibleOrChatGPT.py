import pygame
import pyttsx3
import random
import time


# Initialize pyttsx3 for text-to-speech
engine = pyttsx3.init()

# Define file paths
BIBLE_FILE = 'Bible.txt'
CHATGPT_FILE = 'ChatGPT.txt'
REFERENCES_FILE = 'References.txt'

# Load Bible verses, ChatGPT fake lines, and references
with open(BIBLE_FILE, 'r', encoding='utf-8') as bible_file:
    bible_verses = bible_file.readlines()
    print("BOI we gettin those bible verse")

with open(CHATGPT_FILE, 'r', encoding='utf-8') as chatgpt_file:
    fake_verses = chatgpt_file.readlines()
    print("BOIO we gettin the fake verses")

with open(REFERENCES_FILE, 'r', encoding='utf-8') as ref_file:
    references = ref_file.readlines()
    print("We got du references")

# Set up Pygame
pygame.init()
screen = pygame.display.set_mode((800, 600), pygame.RESIZABLE)
pygame.display.set_caption('Bible Verse or ChatGPT Fake Line?')
font = pygame.font.Font(None, 48)
clock = pygame.time.Clock()

# Colors
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Keys
KEY_CLEAR_SCREEN = pygame.key.key_code('1')
KEY_SHOW_NEW_CLUE = pygame.key.key_code('2')
KEY_SHOW_ANSWER = pygame.key.key_code('3')
KEY_REPLAY_AUDIO = pygame.key.key_code('4')
KEY_RESTART_TIMER = pygame.key.key_code('5')

# Game variables
current_text = ""
current_reference = ""
show_answer = False
is_bible_verse = False
timer_start = None
timer_running = True

# Utility functions
def get_random_text():
    global current_reference, is_bible_verse
    if random.choice([True, False]):
        # Pick a Bible verse
        index = random.randint(0, len(bible_verses) - 1)
        current_reference = references[index].strip()
        is_bible_verse = True
        print("def get random text if: dis will be a real verse")
        return bible_verses[index].strip()
    else:
        # Pick a ChatGPT fake line
        current_reference = ""
        is_bible_verse = False
        print("def get random text else: dis will be a fake verse")
        return fake_verses[random.randint(0, len(fake_verses) - 1)].strip()


def speak_text(text):
    print("def speak_text: about to talk")
    engine.say(text)
    engine.runAndWait()

def wrap_text(text, font, max_width):
    #print("boots and cats")
    words = text.split(' ')
    lines = []
    current_line = ""

    for word in words:
        test_line = current_line + word + " "
        if font.size(test_line)[0] <= max_width:
            current_line = test_line
        else:
            lines.append(current_line)
            current_line = word + " "
    lines.append(current_line)
    return lines

# Main game loop
print("before game loop 1: running")
running = True
current_text = ""
print("before game loop 2: current text should be blank")
timer_running = False
print("before game loop 3: timer is not running")
# BillyBob = True
# keys = ['F13', 'F14', 'F15', 'F16', 'F17']
while running:
    screen.fill(BLUE)
    width, height = screen.get_size()
    font = pygame.font.Font(None, int(height / 15))

    # Display the clue text
    wrapped_text = wrap_text(current_text, font, width - 40)
    y_offset = 50
    for line in wrapped_text:
        text_surface = font.render(line, True, WHITE)
        screen.blit(text_surface, (20, y_offset))
        y_offset += text_surface.get_height() + 10

    # Display the answer if needed
    if show_answer:
        print("showing answer")
        answer_text = "This is a Bible verse." if is_bible_verse else "This is NOT a Bible verse."
        answer_color = GREEN if is_bible_verse else RED
        answer_surface = font.render(answer_text, True, answer_color)
        screen.blit(answer_surface, (20, y_offset))
        y_offset += answer_surface.get_height() + 10
        speak_text(answer_text)




    if is_bible_verse:
        print("game loop if is bible verse: is bible verse")
        reference_surface = font.render(current_reference, True, GREEN)
        screen.blit(reference_surface, (20, y_offset))

    pygame.display.flip()
    #print("flipped the display, whatever that means")

    # Timer logic
    if timer_running and timer_start is None:
        print("timer logic if: timer start")
        timer_start = time.time()
    elif timer_running and time.time() - timer_start >= 10:
        print("timer logic elif 1: show answer")
        show_answer = True
        print("timer logic elif 2: stop timer")
        timer_running = False
        print("timer logic elif 3: speak text")
        # speak_text(current_text)

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == KEY_CLEAR_SCREEN: # F13
                print("1 pressed f13 to clear screen")
                current_text = ""
                print("2 f13 text is ",current_text)
                show_answer = False
                print("3 f13 not showing answer")
                timer_start = None
                print("4 f13 timer is not start")
                timer_running = False
                print("5 f13 timer is not running")
            elif event.key == KEY_SHOW_NEW_CLUE: # F14
                print("1 F14 pressed F14 to show new clue")
                show_answer = True
                print("2 F14 not showing answer")
                current_text = get_random_text()
                print("3 F14 text is ",current_text)
                timer_running = False
                print("4 F14 timer is not running")
                timer_start = None
                print("5 F14 timer is start")
                timer_running = True
                print("6 F14 timer is now running")
            elif event.key == KEY_SHOW_ANSWER: # F15
                print("1 F15 pressed F15 to show answer manually and stop timer")
                show_answer = True
                print("2 F15 showing answer")
                timer_running = False
                print("3 F15 timer is not running")
                #speak_text(current_text)
            elif event.key == KEY_REPLAY_AUDIO: # F16
                print("1 F16 speaking ", current_text)
                speak_text(current_text)
            elif event.key == KEY_RESTART_TIMER: # D17
                timer_running = False
                print("1 F17 timer is not running")
                timer_start = time.time()
                print("2 F17 timer is not start")
                timer_running = True
                print("3 F17 timer is now running")

    clock.tick(30)

pygame.quit()
