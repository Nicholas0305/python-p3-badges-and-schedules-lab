def badge_maker(name):
    badge = "Hello, my name is "+name+"."
    return badge

def batch_badge_creator(names):
    list_of_badges = []
    for name in names:
        name = "Hello, my name is "+name+"."
        list_of_badges.append(name)
    return list_of_badges

def assign_rooms(names):
    rooms = []
    index = 1
    for name in names:
        name = "Hello, "+name+"! You'll be assigned to room "+str(index)+"!"
        rooms.append(name)
        index += 1
    return rooms
def printer(names):
    for badge in batch_badge_creator(names):
        badge = badge
        print(badge)
    for room in assign_rooms(names):
        room = room 
        print(room)
