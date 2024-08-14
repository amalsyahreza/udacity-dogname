# How to Run

```bash
# Setup a new conda environment
# The Udacity workspace is running with python 3.6, however it's no longer supported with conda
# Instead using python 3.8 getting no issues so far.
conda create --name udacity_dogname python==3.8

# Activate environment
conda activate udacity_dogname

# Install pytorch
conda install pytorch -c pytorch
```

## Logging

The logs can be found under `logs/` directoreies

## Results

The scripts for run*models*\*.sh modified a bit to generate the .txt under `results/` directory
