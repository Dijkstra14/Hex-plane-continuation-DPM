
EXPR_ID="--1"
DATA_DIR = "--img"
CHECKPOINT_DIR="--checkpoints"

mpirun --allow-run-as-root  -np 2 -npernode 1 bash -c \
python train_vae.py --data $DATA_DIR/renders_1st --root $CHECKPOINT_DIR --save $EXPR_ID/vae --dataset lego
--num_channels_enc 64 --num_channels_dec 64 --epochs 200 --num_postprocess_cells 2 --num_preprocess_cells 2
--num_latent_per_group 20 --num_cell_per_cond_enc 2 --num_cell_per_cond_dec 2 --num_preprocess_blocks 1
--num_postprocess_blocks 1 --weight_decay_norm 3e-2 --num_latent_scales 3 --num_groups_per_scale 8 --num_nf 2
--batch_size 4 --kl_anneal_portion 1. --kl_max_coeff 1. --channel_mult 1 1 2 4 --num_x_bits 5 --decoder_dist dml
--progressive_input_vae input_skip --arch_instance res_mbconv --num_process_per_node 1 --use_se
--num_proc_node 1