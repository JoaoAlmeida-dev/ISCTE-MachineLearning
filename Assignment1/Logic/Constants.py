
ACTIONS = ["left", "right", "down", "up"]

EXPERIMENT_MAX_STEPS = 20001
EXPERIMENT_NUMBER = 30
STARTING_POS = (0, 0)
# STEPS_FOR_TESTS = [100, 1000, 10000, 20000]
_step = int(EXPERIMENT_MAX_STEPS / 9)

#STEPS_FOR_TESTS = [i for i in range(_step, EXPERIMENT_MAX_STEPS, _step)]
# STEPS_FOR_TESTS = [0,1,10,50,100,20000]
STEPS_FOR_TESTS = [100, 200, 500, 600, 700, 800, 900, 1000, 2500, 5000, 7500, 10000, 12500, 15000, 17500, 20000]

CONSTANT_GREED = 0.9
GREED_THRESHOLD = 30
STARTING_GREED_INCREMENTAL = 0.3

if __name__ == '__main__':
    step = int(EXPERIMENT_MAX_STEPS / 9)
    for i in range(step, EXPERIMENT_MAX_STEPS, step):
        print(i)
    steps = [[i] for i in range(_step, EXPERIMENT_MAX_STEPS, _step)]
    print("steps =", steps)
