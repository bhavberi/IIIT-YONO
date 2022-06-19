def navigate_special(special_code):
    if special_code == "Lib":
        path = ["Enter from A6 gate"]
        return path

    elif special_code == "WS1":
        path = ["Enter from A6 gate and turn left"]
        return path

    elif special_code == "WS2":
        path = ["Enter from A6 gate and walk straight"]
        return path

    elif special_code == "WS3":
        path = ["Enter from A6 gate and climb up one floor",
                "do a about-turn and walk straight"]
        return path

    elif special_code == "WS4":
        path = ["Enter from A6 gate and climb up one floor",
                "do a about turn and walk straight", "cross the workspace and enter the next one"]
        return path

    elif special_code == "SShop":
        path = ["Enter from the A6 gate and climb up one floor"]
        return path

    elif special_code == "RSpace":
        path = ["Enter from the A6 gate and turn left"]
        return path

    elif special_code == "SH1":
        path = ["Enter from the C6 gate and climb up two floors",
                "take a right turn and then again a left turn"]
        return path

    elif special_code == "SH2":
        path = ["En`ter from the C2 gate and climb up one floor",
                "take a right turn and then again a right turn"]
        return path

    elif special_code == "TL1" or special_code == "TL2":
        path = ["Enter from the C6 gate and climb up one floor",
                "take a right turn"]
        return path

    elif special_code == "TL3":
        path = ["Enter from the C6 gate and climb up one floor",
                "take a left turn and then again a left turn"]
        return path

    elif special_code == "SBI":
        path = ["Enter from the C6 gate"]
        return path

    elif special_code == "CompFac":
        path = ["Enter from the C2 gate, climb up two floors and take a left turn",
                "take a right turn at the junction", "walk straight till you find it on your right"]
        return path

    elif special_code == "SciLab":
        path = ["Enter from the C2 gate, climb up two floors and take a left turn",
                "walk straight till the end and turn left"]
        return path

    elif special_code == "CCNSB":
        path = ["Enter from the C2 gate, climb up two floors and take a left turn",
                "walk straight till you find them"]
        return path

    elif special_code == "CVEST":
        path = ["Enter fromt the A6 gate, climb up two floors and take a left",
                "walk straight till you find them"]
        return path

    elif special_code == "CSG":
        path = ["Enter from the C2 gate, climb up two floors and take a left",
                "walk straight till the end", "take a left and walk straight till you find them"]
        return path

    elif special_code == "ERC" or special_code == "RRC":
        path = ["Enter from the A4 gate, climb up two floors and take a about-turn",
                "take a left at the intersection"]
        return path

    elif special_code == "IT":
        path = ["Enter from the A4 gate, climb up one floor and tank a left",
                "walk till the end and again take a left", "walk towards the end till you find them"]
        return path

    elif special_code == "SpcInfo":
        path = ["Enter from the A4 gate, climb up one floor and tank a left",
                "walk straight till the end"]
        return path

    else:
        return -1


def navigate_room(block, room_no):
    instr_straight = "Walk straight till you find your room"
    instr_left = "Turn left and walk till you find your room"
    instr_right = "Turn right and walk till you find your room"

    floor = room_no // 100
    path = navigate_block(block, floor)

    if floor == 1:
        if block == "B6" and room_no == 102:
            path.append("Cross the First Workspace.")
        return path

    if floor == 2:
        if block == "A3" or block == "B2" or block == "B4" or block == "B5":
            path.append(instr_straight)

        elif block == "B3":
            if room_no <= 205:  # to be changed
                path.append(instr_right)

            else:
                path.append(instr_left)
        
        if block == "B6" and room_no == 203:
            return navigate_special("TL1")

        return path

    elif floor == 3:
        if block == "B3" and 306 <= room_no <= 310:
            path.append("Walk straight and take a left into the airlock")

        elif block == "B2" or block == "B3" or block == "B4" or block == "A3" or block == "B5" or block == "A5" or block == "B6" or block == "A6" or block == "A7" or block == "C7":
            path.append(instr_straight)

        return path


def navigate_block(block, floor):
    if floor == 1:
        if block == "A5" or block == "A6":
            return navigate_special("Lib")

        elif block == "A7":
            return navigate_special("WS1")

        elif block == "B6":
            return navigate_special("WS2")

        elif block == "C7":
            return navigate_special("TL3")

    elif floor == 2:
        path1 = ["A3", "A2", "B2", "C1"]
        path2 = ["B4", "B3"]
        path3 = ["B4", "B5"]

        if block == "B6":
            return navigate_special("Wk4")

        if (block in path1):
            with open("./Vindhya_Navigation/Directions/Floor_2/path_1.txt", "r") as txt_file:
                lines = txt_file.readlines()
                lines = list(map(lambda x: x.strip("\n"), lines))
                return (lines[0:path1.index(block)+1])

        elif (block in path2):
            with open("./Vindhya_Navigation/Directions/Floor_2/path_2.txt", "r") as txt_file:
                lines = txt_file.readlines()
                lines = list(map(lambda x: x.strip("\n"), lines))
                return (lines[0:path2.index(block)+1])

        elif (block in path3):
            with open("./Vindhya_Navigation/Directions/Floor_2/path_3.txt", "r") as txt_file:
                lines = txt_file.readlines()
                lines = list(map(lambda x: x.strip("\n"), lines))
                return (lines[0:path3.index(block)+2])

    else:
        path1 = ["B2", "B3"]
        path2 = ["A3", "A2"]
        path3 = ["B4", "B5"]
        path4 = ["A6", "A7"]
        path5 = ["A5"]
        path6 = ["B6"]

        if block == "C6":
            path = ["Enter from the C6 gate and climb up two floors",
                    "take a right turn"]
            return path

        if block == "C7":
            return navigate_special("SH1")

        if (block in path1):
            with open("./Vindhya_Navigation/Directions/Floor_3/path_1.txt", "r") as txt_file:
                lines = txt_file.readlines()
                lines = list(map(lambda x: x.strip("\n"), lines))
                return (lines[0:path1.index(block)+1])

        elif (block in path2):
            with open("./Vindhya_Navigation/Directions/Floor_3/path_2.txt", "r") as txt_file:
                lines = txt_file.readlines()
                lines = list(map(lambda x: x.strip("\n"), lines))
                return (lines[0:path2.index(block)+1])

        elif (block in path3):
            with open("./Vindhya_Navigation/Directions/Floor_3/path_3.txt", "r") as txt_file:
                lines = txt_file.readlines()
                lines = list(map(lambda x: x.strip("\n"), lines))
                return (lines[0:path3.index(block)+1])

        elif (block in path4):
            with open("./Vindhya_Navigation/Directions/Floor_3/path_4.txt", "r") as txt_file:
                lines = txt_file.readlines()
                lines = list(map(lambda x: x.strip("\n"), lines))
                return (lines[0:path4.index(block)+1])

        elif (block in path5):
            with open("./Vindhya_Navigation/Directions/Floor_3/path_5.txt", "r") as txt_file:
                lines = txt_file.readlines()
                lines = list(map(lambda x: x.strip("\n"), lines))
                return (lines[0:path5.index(block)+1])

        elif (block in path6):
            with open("./Vindhya_Navigation/Directions/Floor_3/path_6.txt", "r") as txt_file:
                lines = txt_file.readlines()
                lines = list(map(lambda x: x.strip("\n"), lines))
                return (lines[0:path6.index(block)+1])


def navigate(block=-1, floor=-1, room_no=-1, special_code=-1):
    if special_code != -1:
        return navigate_special(special_code)

    elif block != -1 and room_no != -1:
        return navigate_room(block, room_no)

    elif block != -1 and floor != -1:
        return navigate_block(block, floor)

    else:
        return -1
