import RPi.GPIO as GPIO
import pygame
import time

# ======================
# GPIO Setup
# ======================
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

IN1 = 24
IN2 = 23
IN3 = 17
IN4 = 27
ENA = 25
ENB = 22

GPIO.setup(IN1, GPIO.OUT)
GPIO.setup(IN2, GPIO.OUT)
GPIO.setup(IN3, GPIO.OUT)
GPIO.setup(IN4, GPIO.OUT)
GPIO.setup(ENA, GPIO.OUT)
GPIO.setup(ENB, GPIO.OUT)

# PWM setup
pwmA = GPIO.PWM(ENA, 1000)
pwmB = GPIO.PWM(ENB, 1000)
pwmA.start(70)
pwmB.start(70)

# ======================
# Motor Functions
# ======================
def forward():
    GPIO.output(IN1, 1)
    GPIO.output(IN2, 0)
    GPIO.output(IN3, 1)
    GPIO.output(IN4, 0)

def backward():
    GPIO.output(IN1, 0)
    GPIO.output(IN2, 1)
    GPIO.output(IN3, 0)
    GPIO.output(IN4, 1)

def left():
    GPIO.output(IN1, 0)
    GPIO.output(IN2, 1)
    GPIO.output(IN3, 1)
    GPIO.output(IN4, 0)

def right():
    GPIO.output(IN1, 1)
    GPIO.output(IN2, 0)
    GPIO.output(IN3, 0)
    GPIO.output(IN4, 1)

def stop():
    GPIO.output(IN1, 0)
    GPIO.output(IN2, 0)
    GPIO.output(IN3, 0)
    GPIO.output(IN4, 0)

# ======================
# Pygame Setup
# ======================
pygame.init()
screen = pygame.display.set_mode((300, 200))
pygame.display.set_caption("Car Control")

print("Hold keys: W A S D")

# ======================
# Main Loop
# ======================
try:
    running = True
    while running:
        pygame.event.pump()  # process events
        keys = pygame.key.get_pressed()

        if keys[pygame.K_w]:
            forward()
        elif keys[pygame.K_s]:
            backward()
        elif keys[pygame.K_a]:
            left()
        elif keys[pygame.K_d]:
            right()
        else:
            stop()

        # Exit
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        time.sleep(0.05)

except KeyboardInterrupt:
    pass

finally:
    stop()
    GPIO.cleanup()
    pygame.quit()
    print("Program Ended")
