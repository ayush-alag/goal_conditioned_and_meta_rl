"""Run the Q-network on the environment for fixed steps.

Complete the code marked TODO."""
import numpy as np # pylint: disable=unused-import
import torch # pylint: disable=unused-import


def run_episode(
    env,
    q_net, # pylint: disable=unused-argument
    steps_per_episode,
):
    """Runs the current policy on the given environment.

    Args:
        env (gym): environment to generate the state transition
        q_net (QNetwork): Q-Network used for computing the next action
        steps_per_episode (int): number of steps to run the policy for

    Returns:
        episode_experience (list): list containing the transitions
                        (state, action, reward, next_state, goal_state)
        episodic_return (float): reward collected during the episode
        succeeded (bool): DQN succeeded to reach the goal state or not
    """

    # list for recording what happened in the episode
    episode_experience = []
    succeeded = False
    episodic_return = 0.0

    # reset the environment to get the initial state
    state, goal_state = env.reset() # pylint: disable=unused-variable
    goal_state = torch.from_numpy(goal_state.astype(np.float32)).unsqueeze(0)

    for _ in range(steps_per_episode):

        # ======================== TODO modify code ========================
        pass

        # append goal state to input, and prepare for feeding to the q-network
        # Hint: state and goal_state are 1d numpy arrays of size (N,). After being
        # combined, you should have a 1d numpy array of size (2*N,)
        state = torch.from_numpy(state.astype(np.float32)).unsqueeze(0)
        concat_state = torch.cat((state, goal_state), dim=1)

        # forward pass to find action
        # Hint 1: Remember that you need to pass a torch tensor into your Q Network that
        # is batched since the Q Network expects a batched input. A batch size of 1 is fine.
        # Hint 2: Remember that Q Networks return an array with size equal to the action space
        # such that each value represents the estimated value for taking that action. You
        # want to GREEDILY select the action based on these estimated values.
        with torch.no_grad():
            outputs = q_net(concat_state)

        greedy_action = torch.argmax(outputs, dim=1).item()

        # take action, use env.step
        # Hint: Remember that env.step is going to return a tuple
        # (next_state, reward_this_step, done, info) where info is a dict
        (next_state, reward_this_step, done, info) = env.step(greedy_action)

        # add transition to episode_experience as a tuple of
        # (state, action, reward, next_state, goal)
        episode_experience.append((state, greedy_action, reward_this_step, next_state, goal_state))

        # update episodic return
        episodic_return += reward_this_step

        # update state
        state = next_state

        # update succeeded bool from the info returned by env.step
        # Hint: Use the key 'successful_this_state' from the info dictionary
        if info["successful_this_state"]:
            succeeded = True

        # break the episode if done=True
        if done:
            break

        # ========================      END TODO       ========================

    return episode_experience, episodic_return, succeeded
