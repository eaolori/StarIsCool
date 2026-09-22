import pyttsx3

engine = pyttsx3.init()

voices = engine.getProperty("voices")

print("Available voices:")

for index, voice in enumerate(voices):
    print(f"{index}: {voice.id}")

choice1 = int(input("Choose the first voice: "))
choice2 = int(input("Choose the second voice: "))


sentence = input("What do you want me to say? ")

chosen_voices = [voices[choice1], voices[choice2]]

for voice in chosen_voices:
    engine.setProperty("voice", voice.id)
    engine.say(sentence)
    engine.runAndWait()

print(sentence)