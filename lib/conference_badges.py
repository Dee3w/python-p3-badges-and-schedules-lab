def badge_maker(name):
    return f'Hello, my name is {name}.'

def batch_badge_creator(names):
    my_list = [f'Hello, my name is {name}.' for name in names]
    return my_list

def assign_rooms(names):
    my_list = [f"Hello, {name}! You'll be assigned to room {names.index(name)+1}!" for name in names]
    return my_list

def printer(names):
     [print(x) for x in batch_badge_creator(names)]
     [print(x) for x in assign_rooms(names)]
     return None
