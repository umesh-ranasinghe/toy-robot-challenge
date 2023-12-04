import re
directions = {'NORTH' : [0,1], 'EAST' : [1,0], 'SOUTH' : [0,-1], 'WEST' : [-1,0]}
turns = {'LEFT', 'RIGHT'}


def place(instruction):
    global position, facing_direction
    place = re.match('PLACE (\d),(\d),([A-z]+)', instruction)
    if place:
        suggested_x = int(place[1])
        suggested_y = int(place[2])
        suggested_direction = place[3]
        if (0 <= suggested_x <=4) and (0 <= suggested_y <= 4) and suggested_direction in directions:
             position = [int(suggested_x),int(suggested_y)]
             facing_direction = directions[suggested_direction]


def get_direction_name(direction_cordinates):
     for (direction_name, cordinates) in directions.items():
          if cordinates == direction_cordinates:
               return direction_name


def move_with_care():
     global position, facing_direction
     suggested_position = [pos_a + fac_a for pos_a, fac_a in zip(position, facing_direction)]
     if (0 <= suggested_position[0] <=4) and (0 <= suggested_position[1] <= 4):
          position = suggested_position


def turn(side):
     global facing_direction
     if side == 'LEFT':
          facing_direction = [-facing_direction[1], facing_direction[0]]
     elif side == 'RIGHT':
          facing_direction = [facing_direction[1], -facing_direction[0]]


def proceed(instruction):
    if instruction.startswith('PLACE'):
         place(instruction)
    elif instruction in turns:
         turn(instruction)
    elif instruction == 'MOVE':
         move_with_care()


def initialize():
    global position, facing_direction
    position = [-1,-1]          #default values out of table
    facing_direction = [0,0]    #default values for no facing direction


if __name__ == '__main__':
    initialize()
    with open('test-case.txt', 'r') as test_sequence:
            instruction = test_sequence.readline().strip()
            while instruction != "REPORT":
                proceed(instruction)
                instruction = test_sequence.readline().strip()
            if not position == [-1, -1]:
                print(f'{position[0]},{position[1]},{get_direction_name(facing_direction)}')