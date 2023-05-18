print("Lieutenant Uhura is visiting the space station K7 from the USS Enterprise. ")
print("While there, she meets a man named Cyrano Jones who sells her a pet:")
print("a ball of fur called a Tribble. Doctor McCoy later examines the Tribble and makes the following observations:")
print("Tribbles are born pregnant and reproduce asexually.\n")
print("Tribbles never die except by poisoning.After twelve hours of life—and every twelve hours thereafter—a Tribble will give birth to a litter of ten baby Tribbles.\n")
print("Assuming the Tribble that Lieutenant Uhura purchased was a newborn and it was the only one brought back from the space station,")
print("after three Earth days, how many Tribbles will there be on the Enterprise? After four days? \n")
print("This python programs make it possible  to predict the number of Tribbles after any length of time (in hours).\n\n")

def tribbles(timehrs):

    if timehrs == 0:
        return 0
    return 11 ** (timehrs//12)

       


print("The first day there was only the {}st baby tribble rolling around.".format(tribbles(0)+1))
print("After twelve hours, that first lil tribble gave birth to 10 baby tribbles, now Lieutenant Uhura has {} baby tribbles.".format(tribbles(12)))
print("By the next morning, all 11 tribbles had 10 more babies! Lieutenant Uhura woke up to a total of {} lil tribbles.".format(tribbles(24)))
print("Two days later, all 121 tribbles had 10 more babies which gave Lieutenant Uhura now, {} baby tribbles.".format(tribbles(36)))
print("Three days later, Lieutenant Uhura woke up scared because each one had multiplied again making it {} tribbles rolling around!".format(tribbles(48)))
print("On the fourth day, Lieutenant Uhura had to sell some tribbles because she now had {} BABY TRIBBLES!!!!!\n".format(tribbles(60)))
print("To summarize this up:\n")
print("Day 1          ==> {} Tribble".format(tribbles(0+1)))
print("12 hours later ==> {} Tribbles".format(tribbles(12)))
print("24 Hours later ==> {} Tribbles".format(tribbles(24)))
print("36 Hours later ==> {} Tribbles".format(tribbles(36)))
print("48 Hours later ==> {} Tribbles".format(tribbles(48)))
print("60 Hours later ==> {} Tribbles\n".format(tribbles(60)))
print("That is a lot of Tribbles!!!!!!!!!\n")

