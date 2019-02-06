world_map = {
    'R1A': {
        'NAME': "Lower Mid",
        'DESCRIPTION': "You are at a narrow path and all you can do is go forward.",
        'PATHS': {
            'NORTH': "R1B"
        }

    },
    'R1B': {
        'NAME': "Mid",
        'DESCRIPTION': "You are at a narrow path and you have directions every way.",
        'PATHS': {
            'NORTH': "R1C",
            'EAST': "R34",
            'WEST': "REST",
            'SOUTH': "R1A"
        }
    },
    'REST': {
        'NAME': "Bench",
        'DESCRIPTION': "This is just an old bench...",
        'PATHS': {
            'EAST': "R1B"
        }
    },
    'R34': {
        'NAME': "HayStack",
        'DESCRIPTION': "You are near a balcony and you can go west or east.",
        'PATHS': {
            'UP': "RBIDY",
            'WEST': "R1B",
            'EAST': "ALL",
        }
    },
    'ALL': {
        'NAME': "Alley",
        'DESCRIPTION': "There is a door in front of you.",
        'PATHS': {
            'NORTH': "STR",
            'WEST': "R34"
        }
    },
    'STR': {
        'NAME': "Stairs",
        'DESCRIPTION': "You can go up some stairs",
        'PATHS': {
            'UP': "",
            'SOUTH': "ALL"
        }
    },
    'RBIDY': {
        'NAME': "Balcony",
        'DESCRIPTION': "You are on a balcony you can jump into the haystacks or go through the window.",
        'PATHS': {
            'DOWN': "R34",
            'NORTH': "RWN"
        }
    },
    'RWN': {
        'NAME': "West Bedroom",
        'DESCRIPTION': "You are at the west end of a bedroom there "
                       "is a drawer and a bed to the east and a door in front of you.",
        'PATHS': {
            'NORTH': "APT",
            'EAST': "REN",
            'SOUTH': "RBIDY"
        }
    },
    'REN': {
        'NAME': "East Bedroom",
        'DESCRIPTION': "You are at the east end of the bedroom there is a drawer and bed.",
        'PATHS': {
           'WEST': "RWN"
        }
    },
    'WAPT': {
        'NAME': " West Apartments",
        'DESCRIPTION': "There are so stairs going down and a hallway east.",
        'PATHS': {
            'EAST': "EAPT",
            'DOWN': "BLR",
            'SOUTH': "RWN"
        }
    },
    'EAPT': {
        'NAME': "East Apartments",
        'DESCRIPTION': "",
        'PATHS': {
            'DOWN': "",
            'WEST': "WAPT",
        }
    },
    'BLR': {
        'NAME': "Boiler Room",
        'DESCRIPTION': "There's a boiler behind me and a door in front.",
        'PATHS': {
            'NORTH': "RBLD",
            'UP': "WAPT"
        }
    },
    'R1C': {
        'NAME': "Upper Mid",
        'DESCRIPTION': "There is a wall North and you have paths every other way.",
        'PATHS': {
            'SOUTH': "R1B",
            'EAST': "RBLD",
            'WEST': "RCLA"
        }
    },
    'RCLA': {
        'NAME': "Close",
        'DESCRIPTION': "It's a small corner you can go straight or back",
        'PATHS': {
            'EAST': "R1C",
            'WEST': "LARCH"
        }
    },
    'RBLD': {
        'NAME': "Boiler Room Door",
        'DESCRIPTION': "You are next to a nice wooden door to your back but there is also a path right.",
        'PATHS': {
            'WEST': "R1C",
            'EAST': "",
            'SOUTH': ""
        }
    },
    'LARCH': {
        'NAME': "Lower Arch Side",
        'DESCRIPTION': "You can go into a little corner or continue.",
        'PATHS': {
            'NORTH': "",
            'SOUTH': "",
            'EAST': "RCLA"
        }
    },
}

current_node = world_map['R1A']
directions = ["NORTH", "SOUTH", "EAST", "WEST", "UP", "DOWN"]
playing = True

while playing:
    print(current_node["NAME"])
    print(current_node["DESCRIPTION"])
    command = input(">_")
    if command.lower() in ['q', 'quit', 'exit']:
        playing = False
    elif command.upper()in directions:
        try:
            room_name = current_node['PATHS'][command.upper()]
            current_node = world_map[room_name]
        except KeyError:
            print("I can't go that way.")
    else:
        print("Command Not Recognized")
