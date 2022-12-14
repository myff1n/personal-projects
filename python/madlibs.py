#user prompt
print("Give me an ADJECTIVE")
adj_1 = input("")

import time
import random

#startup
print("MadLibs v0.01")
print("Initializing...")
time.sleep(random.randint(1, 5))

#user prompts
print("Give me an ADJECTIVE")
adjective = input("")

print("Now give me a FOOD")
food = input("")

print("Past tense VERB?")
past_tense_verb = input("")

print("What about a PERSON?")
person = input("")

print("Ok, now a RELATIVE")
relative = input("")

print("Give me a SINGULAR NOUN")
first_noun = input("")

print("Alright, now a LIQUID")
liquid = input("")

print("A VERB ending in -ING")
verb-ing = input("")

print("I need a PLURAL NOUN")
plural_noun = input("")

print("A piece of FURNITURE")
furniture = input("")

print("Last one! Another VERB ending in ING")
second_verb-ing = input("")

#"wait time" - waits between 1 to 3 seconds
print("Generating story...")
time.sleep(random.randint(1, 3))


#print story
print(f"It was a cold, {adjective}, winter day.")
print(f"I woke up to the smell of {food} cooking downstairs.")
print(f"I {past_tense_verb} down the stairs to help with the {food}.")
print(f"My {person} told me to see if my {relative} needed a fresh {first_noun}.")
print(f"So I carried a tray of glasses full of {liquid} into the {verb-ing} room.")
print(f"When I came into the {verb-ing} room, I couldn't believe my eyes!")
print(f"There were {plural_noun} {second_verb-ing} on the {furniture}!")

