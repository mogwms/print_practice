# Python Print Practice

print("Angry Guy: Hello, world... I'm going to rain infinite cats down onto Earth!")
response = "No! Don't do that! And those poor cats. Leave them alone!"
print("Jimmy: " + response)

for crowd in range(1, 5):
    print("Bystander " + str(crowd) + ": Yeah! Don't do it!")

monstersInTheOutskirts = [
    ["Zombie", "Buurgh.. Don't destroy the world with cats.. We got lives too..brhh.."],
    ["Ogre", "Graaaah! I'll smash youuur face!"],
    ["Bigfoot", "*runs away and hides*"],
    ["Wendigo", "Grauuuuuahhh!!!!!"]
]

for monster, message in monstersInTheOutskirts:
    print(f"{monster}: {message}")

militaryRanks = [
    ["Soldier", 5, "Why am I here again..?"],
    ["General", 1, "We should intercept the angry guy immediately. We must mobilize all units."],
    ["Captain", 3, "Okay. I'll send word to my troops!"],
    ["Officer", 4, "Ready to move out!"],
    ["Commander", 2, "Sir, Yes, Sir! I will send word to all the troops!"],
]
militaryRanks.sort(key=lambda x: x[1])

print("In the War Room...")

for position, (title, rank, message) in enumerate(militaryRanks, start=1):
    print(f"{title} (Rank {rank}): {message}")