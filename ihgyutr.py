import random

# List of out-of-pocket, random phrases
phrases = [
    "Flap your elbows like a confused flamingo",
    "In the end, all pizzas become frisbees",
    "Always hydrate your cactus with compliments",
    "A rainbow’s purpose is to distract the unicorns",
    "Run like a microwave chasing its popcorn dreams",
    "When in doubt, hug an imaginary giraffe",
    "The moon naps with sunglasses on",
    "Feed your inner llama spicy nachos",
    "Carve your destiny with a spork",
    "Befriend the toaster and it might share its secrets",
    "Dream big, like a goldfish with Wi-Fi",
    "Eat your salad with the energy of a hyperactive koala",
    "Dodge life's lemons like a ninja at a fruit stand",
    "Always smell your socks before they smell you",
    "Fly high, like a banana-powered skateboard",
    "Whisper sweet nothings to your pet refrigerator",
    "The universe is just a giant marshmallow waiting to be roasted",
    "Believe in your flip-flops even when they squeak",
    "Navigate the storm like a penguin with a jetpack",
    "Dance with the wind, but remember, the wind can't dance",
    "Call your ex just to remind them they owe you $12 for that burrito",
    "Quit your job and become a professional napper, you’ve got the face for it",
    "Lie about knowing karate to impress people at awkward parties",
    "Text your boss 'I love you' and blame autocorrect",
    "If they don’t reply, send 47 more texts, because you're a priority",
    "Buy a yacht just to tell people you don’t use it",
    "Make your bed, then never sleep in it, just to confuse your enemies",
    "Ask strangers if they think you’re a good kisser for ‘science’",
    "Post gym selfies to remind people that they’ll never be you",
    "Argue with your reflection in the mirror to build self-confidence",
    "Put 'world’s okayest human' on your resume, it's accurate",
    "Start jogging just to run away from your responsibilities",
    "Take a selfie at a funeral to remind people you’re still alive",
    "Tell your barber you ‘just want to feel something’",
    "Tell your dentist you're flossing spiritually, if not physically",
    "Pay for groceries with coins to assert dominance",
    "Start a podcast where you just whisper all your regrets",
    "Invite yourself to weddings you weren’t invited to, for the cake",
    "Tell your therapist you're the reason their plants are thriving",
    "Start a rumor about yourself to see how fast it spreads",
]

# Function to generate more random and bizarre "inspirational" quotes
def generate_inspirational_quote(phrases):
    part1 = random.choice(phrases).split()[0:3]  # First 3 words of a random phrase
    part2 = random.choice(phrases).split()[3:]   # Last part of a different random phrase

    # Combine parts into a new quote
    quote = ' '.join(part1 + part2)

    # Capitalize the first letter and return the result
    return quote.capitalize()

# Generate and print 10 random "inspirational" quotes
for _ in range(10):
    print(generate_inspirational_quote(phrases))
