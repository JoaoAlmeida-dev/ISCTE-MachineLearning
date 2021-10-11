from Week3_Remake.Logic.World import World


def main():
    # randomQWalk()
    side_size = 10
    world = World(_collumns=side_size, _rows=side_size, _reward_state=(10, 10))
    print(world.pretty_print())

if __name__ == "__main__":
    main()
