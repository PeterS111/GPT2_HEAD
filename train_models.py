import os 

os.system("python run_lm_finetuning.py --output_dir=output  --model_type=gpt2 --model_name_or_path=output/checkpoint-125000 --do_train --eval_data_file=input_data/Shelley_4a_val.txt --do_eval --evaluate_during_training --train_data_file=input_data/Shelley_4a_train.txt --overwrite_output_dir --block_size=200 --per_gpu_train_batch_size=1 --save_steps 10000 --save_total_limit 1000 --num_train_epochs=5000 --logging_steps=50")
