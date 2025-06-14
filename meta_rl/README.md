## Using Meta_RL Environment

Everything should already be installed on your AWS EC2 Instance if you used the given AMI.

All you need to do to be able to run the meta_rl folder's code is to switch to the meta_rl conda environment
```bash
conda deactivate
conda activatae meta_rl
```

## Run the Code

To run the DREAM code, invoke the following command:

```
python dream.py exp_name -b environment=\"map\"
```

This will create a directory `experiments/exp_name`, which will contain:

- A tensorboard subdirectory at `experiments/exp_name/tensorboard`, which logs
  statistics, such as accumulated returns vs. number of training episodes, and
  also vs. number of training steps.
- A visualization subdirectory at `experiments/exp_name/visualize`, which will
  contain videos of the learned agent.
- A checkpoints subdirectory at `experiments/exp_name/checkpoints`, which will
  periodically save model checkpoints.
- Metadata about the run, such as the configs used.

You can pass different values for `exp_name` as convenient.

To run the RL^2 code, similarly run:

```
python rl2.py exp_name -b environment=\"map\"
```
