class Result:
    run_time: float = 0
    attempts: int = 0
    pattern_size: int = -1
    successfull: bool = False

    def __init__(self, run_time: float, attempts: int, pattern_size: int, successfull: bool):
        self.run_time = run_time
        self.attempts = attempts
        self.pattern_size = pattern_size
        self.successfull = successfull
