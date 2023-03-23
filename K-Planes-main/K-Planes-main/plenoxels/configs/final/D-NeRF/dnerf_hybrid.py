config = {
 'expname': 'contin_2nd_half_plane',
 'logdir': './logs/syntheticdynamic',
 'device': 'cuda:0',

 'data_downsample': 4.0, # was 1.0
 'data_dirs': ['./plenoxels/data/dnerf/lego'],
 'contract': False,
 'ndc': False,
 'isg': False,
 'isg_step': -1,
 'ist_step': -1,
 'keyframes': False,
 'scene_bbox': [[-1.3, -1.3, -1.3], [1.3, 1.3, 1.3]],

 # Optimization settings

 'num_steps': 30001, # was 30001
 'batch_size': 4096,
 'scheduler_type': 'warmup_cosine',
 'optim_type': 'adam',
 'lr': 0.1,

 # Regularization
 'distortion_loss_weight': 0.00,
 'histogram_loss_weight': 1.0,
 'l1_time_planes': 0.0001,
 'l1_time_planes_proposal_net': 0.0001,
 'plane_tv_weight': 0.0001,
 'plane_tv_weight_proposal_net': 0.0001,
 'time_smoothness_weight': 0.1,
 'time_smoothness_weight_proposal_net': 0.001,

 # Training settings
 'save_every': 30000, # was 30000
 'valid_every': 30000, # was 30000
 'save_outputs': True,
 'train_fp16': True,

 # Raymarching settings
 'single_jitter': False,
 'num_samples': 48,
 'num_proposal_iterations': 2,
 'num_proposal_samples': [256, 128],
 'use_same_proposal_network': False,
 'use_proposal_weight_anneal': True,
 'proposal_net_args_list': [
  {'num_input_coords': 4, 'num_output_coords': 8, 'resolution': [64, 64, 64, 50]},
  {'num_input_coords': 4, 'num_output_coords': 8, 'resolution': [128, 128, 128, 50]}
 ],

 # Model settings
 'concat_features_across_scales': True,
 'density_activation': 'trunc_exp',
 'linear_decoder': False,
 'multiscale_res': [1, 2, 4, 8],
 # Use time reso = half the number of frames
 # Lego: 25 (50 frames)
 # Hell Warrior and Hook: 50 (100 frames)
 # Mutant, Bouncing Balls, and Stand Up: 75 (150 frames)
 # T-Rex and Jumping Jacks: 100 (200 frames)
 'grid_config': [{
  'grid_dimensions': 2,
  'input_coordinate_dim': 4,
  'output_coordinate_dim': 32,
  'resolution': [64, 64, 64, 25]
 }],
 'using_DPM_guidance': True,
'DPM_dir':'./logs/model-10.pt',
'distill_steps': 30001}
