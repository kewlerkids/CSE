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
            "EAST"
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
    'RBIDY': {
        'NAME': "Balcony",
        'DESCRIPTION': "",
        'PATHS': {
            'DOWN': "R34",

        }
    },
    'REST': {
        'NAME': "Bench",
        'DESCRIPTION': "This is just an old bench...",
        'PATHS': {
            'EAST': "R1B"
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
    }
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
