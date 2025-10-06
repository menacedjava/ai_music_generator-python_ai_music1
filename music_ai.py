# AI Music Generator (skeleton)
# Uses MIDI + Transformer placeholder
import random

NOTES = ['C', 'D', 'E', 'F', 'G', 'A', 'B']

def generate_melody(length=8):
    return [random.choice(NOTES) for _ in range(length)]

if __name__ == '__main__':
    melody = generate_melody()
    print("Generated melody:", melody)
