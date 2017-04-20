########################################
# Name: Brad Raynaud
# Date: 4/19/2017
# Description: Paper piano (v2).
########################################
import RPi.GPIO as GPIO
from time import sleep, time
import pygame
from array import array

MIXER_FREQ = 44100
MIXER_SIZE = -16
MIXER_CHANS = 1
MIXER_BUFF = 1024


# the note generator class
class Note(pygame.mixer.Sound):
    # note that volume ranges from 0.0 to 1.0
    def __init__(self, frequency, volume, wavetype):
        self.frequency = frequency
        self.wavetype = wavetype  # instance variable determining wave type
        # initialize the note using an array of samples
        pygame.mixer.Sound.__init__(self, buffer=self.build_samples())
        self.set_volume(volume)

    # builds an array of samples for the current note
    def build_samples(self):
        # calculate the period and amplitude of the note's wave
        period = int(round(MIXER_FREQ / self.frequency))
        amplitude = 2 ** (abs(MIXER_SIZE) - 1) - 1
        # initialize the note's samples (using an array of
        # signed 16-bit "shorts")
        samples = array("h", [0] * period)
        # generate the note's samples
        for t in range(period):
            # implemented the square wavetype
            if self.wavetype == "Square":  # yellow
                if t < period / 2:
                    samples[t] = amplitude
                else:
                    samples[t] = -amplitude

            # implemented the triangle wavetype
            # amplitude follows graph provided in the activity
            elif self.wavetype == "Triangle":  # Green
                if t >= period * 3 / 4:
                    for n in range(-amplitude, 0, amplitude / 42):
                        samples[t] = n
                if t < period / 4:
                    for n in range(0, amplitude, amplitude / 42):
                        samples[t] = n
                else:
                    for n in range(amplitude, -amplitude, -amplitude / 85):
                        samples[t] = n
            # Implemented the sawtooth wavetype
            # amplitude goes from 0 to max amp then from min amp to 0
            elif self.wavetype == "Sawtooth":  # Blue
                if t < period / 2:
                    for n in range(0, amplitude, amplitude / 85):
                        samples[t] = n
                else:
                    for n in range(-amplitude, 0, amplitude / 85):
                        samples[t] = n
        return samples


# waits until a note is pressed
def wait_for_note_start():
    while (True):
        # first, check for notes
        for key in range(len(keys)):
            if (GPIO.input(keys[key])):
                return key
        sleep(0.01)


# waits until a note is released
def wait_for_note_stop(key):
    while (GPIO.input(key)):
        sleep(0.1)


# preset mixer initialization arguments: frequency (44.1K), size
# (16 bits signed), channels (mono), and buffer size (1KB)
# then, initialize the pygame library
pygame.mixer.pre_init(MIXER_FREQ, MIXER_SIZE, MIXER_CHANS, MIXER_BUFF)
pygame.init()

# use the Broadcom pin mode
GPIO.setmode(GPIO.BCM)

# setup the pins and frequencies for the notes (C, D, E, F)
keys = [26, 6, 12, 20]
waveType = ["Square", "Triangle", "Sawtooth"]  # list of wavetypes
notes = []

# setup the input pins
GPIO.setup(keys, GPIO.IN, GPIO.PUD_DOWN)

# create the actual notes
for n in range(len(waveType)):
    notes.append(Note(261.6, 1, waveType[n]))

# the main part of the program
print "Welcome to Paper Piano!"
print "Press Ctrl+C to exit..."

try:
    while (True):
        # play a note when pressed...until released
        key = wait_for_note_start()
        notes[key].play(-1)
        wait_for_note_stop(keys[key])
        notes[key].stop()

# detect when Ctrl+C is pressed so that we can reset the GPIO
except KeyboardInterrupt:
    GPIO.cleanup()
