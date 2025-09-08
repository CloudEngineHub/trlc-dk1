from trlc_dk1.follower import DK1Follower, DK1FollowerConfig
from trlc_dk1.leader import DK1Leader, DK1LeaderConfig
import time


follower_config = DK1FollowerConfig(
    port="/dev/tty.usbmodem00000000050C1",
    joint_velocity_scaling=1.0,
)

leader_config = DK1LeaderConfig(
    port="/dev/tty.usbmodem58FA0824311"
)

leader = DK1Leader(leader_config)
leader.connect()

follower = DK1Follower(follower_config)
follower.connect()

freq = 200 # Hz
duration = 60 # s

try:
    while True:
        action = leader.get_action()
        follower.send_action(action)    
        time.sleep(1/freq)
except KeyboardInterrupt:
    print("\nStopping teleop...")
    leader.disconnect()
    follower.disconnect()
