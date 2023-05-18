print("This program uses a function to sing happy birthday and explode the name of the birthday person") 
print("***********************************************************************************************")

def singandexplode_happy_birthday(name):
    print("Happy Birthday To You")
    print("Happy Birthday To You")
    print(f"Happy Birthday Dear {name}")
    print("Happy Birthday To You") 
    bdayperson=list(name)
    print(bdayperson)

singandexplode_happy_birthday("Michelle")

print("This program uses a function to sing happy birthday and explode the name of the birthday person") 
print("***********************************************************************************************")

def singandexplode(name):
    print(f"Happy happy Birthday Dear {name}!!!")
    name=list(name)
    return(name)

def implodebdayname(name):
    name="".join(name)
    return(name)


print("EXPLODING BIRTHDAY NAME ===>:\n", singandexplode("Joey"))
print("IMPLODING BIRTHDAY NAME ===>:\n", implodebdayname(singandexplode("Joey")))


       


