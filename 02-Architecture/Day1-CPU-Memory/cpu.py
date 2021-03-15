
# print(my_a)

#components of a computer to make
# RAM
# CPU

# opcodes
LOAD_NUM = 0b000000
PRINT_NUM = 0b000001
HALT = 0b000010
PRINT_NAME = 0b101000



# Memory
ram = [0] * 255

# program counter
pc = 0

# registers
# r0 - r7

registers = [0] * 8

# running loop
while True:
    # fetch
    inst = ram[pc]

    # decode
    if inst == PRINT_NAME:
        #execute
        print("Tom")
    
    # decode
    elif inst == HALT:
        running = False

    # decode
    elif inst = LOAD_NUM:
        pass

    # decode
    elif inst = PRINT_NUM:
        pass