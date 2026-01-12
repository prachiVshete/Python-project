import random

# Add random , funny subjects
subjects = [
    "A laptop that works only near deadline",
    "A student who said 'bas last episode'",
    "A WhatsApp uncle with fake PhD",
    "A phone charger that works only at 32° angle",
    "A topper saying 'kuch nahi padha'",
    "A Zomato rider stuck 100 meters away",
    "A government website powered by hope",
    "Hostel mess food with criminal intentions",
    "An alarm clock with personal revenge",
    "A Wi-Fi router during online exam",
    "A relative who knows Sharma ji ka beta"
]

# Add funny, chaotic actions 
actions = [
    "goes into full emotional breakdown over",
    "chooses violence after seeing",
    "starts overthinking career because of",
    "blames past life karma for",
    "creates unnecessary WhatsApp status about",
    "pretends everything is fine while facing",
    "starts motivational speech nobody asked for on",
    "questions existence after encountering",
    "panics in 4 different languages due to",
    "starts crying internally because of",
    "files imaginary complaint against"
]

# Add random places or the things
places_or_things = [
    "Monday morning alarm",
    "OTP that arrives after timeout",
    "group project where no one replies",
    "exam question from parallel universe",
    "camera turning on accidentally",
    "salary disappearing in 2 days",
    "random relative asking 'package kitna hai?'",
    "buffering circle of death",
    "unexpected family guests",
    "online exam server crash",
    "one unread message from crush"
]

# Generate the fake news using the loop
while True:
    subject = random.choice(subjects)
    action = random.choice(actions)
    place_or_thing = random.choice(places_or_things)

    headline = f"BREAKING NEWS: {subject} {action} {place_or_thing}!!!"
    print("\n" + headline)

    user_input = input("\nGenerate another Fake News? (yes/no): ").strip().lower()
    if user_input == "no":
        break

print("\nThanks for using the Fake News Generator. Have a good day.")
