class Result:

    def __init__(self, _rewards: int, _steps_per_reward_mean: int, _rewards_per_step: float,_qmatrix_step:int):
        self.rewards = _rewards
        self.steps_per_reward_mean = _steps_per_reward_mean # steps per reward
        self.rewards_per_step = _rewards_per_step
        self.qmatrix_step = _qmatrix_step

