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
            'UP': "EAPT",
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
            'NORTH': "WAPT",
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
        'DESCRIPTION': "There are so stairs going down and a hallway east plus a door behind.",
        'PATHS': {
            'EAST': "EAPT",
            'DOWN': "BLR",
            'SOUTH': "RWN"
        }
    },
    'EAPT': {
        'NAME': "East Apartments",
        'DESCRIPTION': "You are next to a long hall and stairs.",
        'PATHS': {
            'DOWN': "STR",
            'WEST': "WAPT",
            'NORTH': "HALL"
        }
    },
    'HALL': {
        'NAME': "Long Hall",
        'DESCRIPTION': "You are in the middle of a narrow and dark hall.",
        'PATHS': {
            'NORTH': "DRO",
            'SOUTH': "EAPT"
        }
    },
    'DRO': {
        'NAME': "Door to second balcony.",
        'DESCRIPTION': "You are next to a white wooden door and the narrow hall.",
        'PATHS': {
            'NORTH': "BALL",
            'SOUTH': "HALL"
        }
    },
    'BALL': {
        'NAME': "Second Balcony",
        'DESCRIPTION': "You are at a very high place but you see a building below.",
        'PATHS': {
            'DOWN': "VROOM",
            'SOUTH': "DRO",
        }
    },
    'BLR': {
        'NAME': "Boiler Room",
        'DESCRIPTION': "There's a boiler behind me and a door in front plus some stairs.",
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
            'EAST': "PAT",
            'SOUTH': "BLR"
        }
    },
    'VROOM': {
        'NAME': "Hay Wagon",
        'DESCRIPTION': "You are on a soft wagon of hay you can jump onto a balcony or get down...",
        'PATHS': {
            'UP': "BALL",
            'DOWN': "TS"
        }
    },
    'TS': {
        'NAME': "Truck Side",
        'DESCRIPTION': "You are next to a wagon and a building.",
        'PATHS': {
            'UP': "VROOM",
            'NORTH': "FGR",
            'SOUTH': "PAT",
            'WEST': "BOOT"
        }
    },
    'PAT': {
        'NAME': "Patio",
        'DESCRIPTION': "You are underneath a patio that has sacks on the floor...",
        'PATHS': {
            'NORTH': "TS",
            'WEST': "RBLD"
        }

    },
    'LARCH': {
        'NAME': "Lower Arch Side",
        'DESCRIPTION': "You can go into a little corner or continue.",
        'PATHS': {
            'NORTH': "UARCH",
            'SOUTH': "CUB",
            'EAST': "RCLA"
        }
    },
    'CUB': {
        'NAME': "CUBBY",
        'DESCRIPTION': "You are in a small corner with a little wooden box...",
        'PATHS': {
            'NORTH': "LARCH"
        }
    },
    'UARCH': {
        'NAME': "Upper Arch Side",
        'DESCRIPTION': "You see a door in front of you and a building to your east.",
        'PATHS': {
            'NORTH': "LDR",
            'SOUTH': "LARCH",
            'EAST': "MCRH"
        }
    },
    'LDR': {
        'NAME': "Library",
        'DESCRIPTION': "It smells like fresh paper and there are shelves of books and a small hall west. ",
        'PATHS': {
            'SOUTH': "UARCH",
            'WEST': "KIT",
        }
    },
    'KIT': {
        'NAME': "Kitchen",
        'DESCRIPTION': "There is a kitchen here with pots pans and cabinets.",
        'PATHS': {
            'EAST': "LDR"
        }
    },
    'MCRH': {
        'NAME': "Moto Near Arch",
        'DESCRIPTION': "You are near a small corner to your north and a building east.",
        'PATHS': {
            'WEST': "UARCH",
            'EAST': "OFF",
            'NORTH': "MOT"
        }
    },
    'MOT': {
        'NAME': "Moto",
        'DESCRIPTION': "You are in a small corner and there is a plain cardboard box.",
        'PATHS': {
            'SOUTH': "MCRH"
        }
    },
    'OFF': {
        'NAME': "Off A Site",
        'DESCRIPTION': "There is a wall North but directions every way.",
        'PATHS': {
            'WEST': "MCRH",
            'EAST': "FGR",
            'SOUTH': "AST"
        }
    },
    'FGR': {
        'NAME': "Front of GraveYard",
        'DESCRIPTION': "There is a graveyard north a slope east and a building west.",
        'PATHS': {
            'NORTH': "GRR",
            'SOUTH': "TS",
            'WEST': "OFF",
            'EAST': "PT"
        }
    },
    'GRR': {
        'NAME': "GraveYard",
        'DESCRIPTION': "There are graves around you and one seems to be dug up already...",
        'PATHS': {
            'SOUTH': "FGR"
        }
    },
    'AST': {
        'NAME': "A Site",
        'DESCRIPTION': "You can go to the back or east.",
        'PATHS': {
            'SOUTH': "DEF",
            'NORTH': "OFF",
            'EAST': "BACK",
        }
    },
    'PT': {
        'NAME': "Pit",
        'DESCRIPTION': "",
        'PATHS': {
            'NORTH': "NPT"
        }
    },
    'BOOT': {
        'NAME': "Boost",
        'DESCRIPTION': "",
        'PATHS': {

        }
    },
    'BACK': {
        'NAME': "Back A Site",
        'DESCRIPTION': "",
        'PATHS': {

        }
    },
    'DEF': {
        'NAME': "Default Box",
        'DESCRIPTION': "",
        'PATHS': {

        }
    },
    'NPT': {
        'NAME': "North of Pit",
        'DESCRIPTION': "",
        'PATHS': {

        }
    },
}

current_node = world_map['R1A']
directions = ["NORTH", "SOUTH", "EAST", "WEST", "UP", "DOWN"]
playing = True

while playing:
    print(current_node["NAME"])
    print(current_node["DESCRIPTION"])
    print("")
    command = input(">_")
    if command.lower() in ['q', 'quit', 'exit']:
        playing = False
    elif command.upper()in directions:
        try:
            room_name = current_node['PATHS'][command.upper()]
            current_node = world_map[room_name]
        except KeyError:
            print("**I can't go that way.**")
    else:
        print("Command Not Recognized")
