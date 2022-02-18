from gym.envs.registration import register

register(
    id='slippary-bandit-walk-env01-v0',
    entry_point='gym_env.envs:SlipparyBanditWalkEnv01'
)

register(
    id='maze-world-env01-v0',
    entry_point='gym_env.envs:MazeWorldEnv01'
)

register(
    id='maze-world-env02-v0',
    entry_point='gym_env.envs:MazeWorldEnv02'
)

register(
    id='two-arm-bernoulli-bandit-env01-v0',
    entry_point='gym_env.envs:TwoArmBernoulliBanditEnv01'
)
