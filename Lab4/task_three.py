# Pacman Game with Simple Reflex Agent + Keyboard Control
# Grid: 4x4 (positions 0–15)

# Legend:
# "F" = food pellet
# "P" = power pellet
# "G" = ghost
# " " = empty
# "C" = Pacman

environment = [
    " ", "P", "F", "P",
    "F", "G", "F", "P",
    "P", "F", "P", "G",
    "P", "F", "G", "F"
]

pacman_position = 0
has_power = False


def reflex_agent(percept):
    global has_power
    if percept == "F":
        return "EAT_FOOD"
    elif percept == "P":
        has_power = True
        return "EAT_POWER"
    elif percept == "G":
        if has_power:
            return "PASS_GHOST"
        else:
            return "AVOID_GHOST"
    else:
        return "MOVE"


def move_pacman(position, move):
    row, col = divmod(position, 4)

    if move == "w" and row > 0:      # Up
        return position - 4
    elif move == "s" and row < 3:    # Down
        return position + 4
    elif move == "a" and col > 0:    # Left
        return position - 1
    elif move == "d" and col < 3:    # Right
        return position + 1
    else:
        return position  # invalid move → stay


def print_grid():
    """Show the 4x4 grid with Pacman (C)"""
    for i in range(16):
        if i == pacman_position:
            print(" C ", end=" ")
        else:
            print(f" {environment[i]} ", end=" ")
        if (i + 1) % 4 == 0:
            print()
    print()


# --- Simulation loop ---
while any(item in ["F", "P"] for item in environment):
    percept = environment[pacman_position]
    action = reflex_agent(percept)

    print(f"\nPacman at {pacman_position} sees {percept} → {action}")
    print_grid()

    if action in ["EAT_FOOD", "EAT_POWER"]:
        environment[pacman_position] = " "
    elif action == "AVOID_GHOST":
        print("❌ Pacman hit a ghost and lost!")
        break

    # Ask user for move
    move = input("Move (W=Up, S=Down, A=Left, D=Right): ").lower()
    pacman_position = move_pacman(pacman_position, move)

else:
    print("✅ All pellets eaten! Pacman wins.")
