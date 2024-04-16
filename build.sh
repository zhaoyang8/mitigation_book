#!/bin/bash


# Define names and paths
action_name="build_book"
dataname="${action_name}"
base_dir="./${action_name}"
bash_dir="./bash/${base_dir}"
job_out_dir="./job-outs/${base_dir}"

# Create directories if they do not exist
mkdir -p "${job_out_dir}"
mkdir -p "${bash_dir}"

# Create run script
run_script="${bash_dir}/run.sh"
cat > "${run_script}" <<EOF
#!/bin/bash

#SBATCH --account=pi-lhansen
#SBATCH --job-name=action_${action_name}
#SBATCH --output=${job_out_dir}/run.out
#SBATCH --error=${job_out_dir}/run.err
#SBATCH --time=1-11:00:00
#SBATCH --partition=caslake
#SBATCH --nodes=1
#SBATCH --cpus-per-task=4
#SBATCH --mem=21G

module load python/anaconda-2022.05

echo "\$SLURM_JOB_NAME"
echo "Program starts \$(date)"
start_time=\$(date +%s)

jupyter-book build /project/lhansen/HMC_book/Amazon/docs

echo "Program ends \$(date)"
end_time=\$(date +%s)
elapsed=\$((end_time - start_time))
echo "Elapsed time: \$(date -ud "@\$elapsed" +'%d days %H hr %M min %S sec')"
EOF

# Submit the batch script
sbatch "${run_script}"
