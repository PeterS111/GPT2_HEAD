import os 

for i in range(1,75):
    ch = str(i) + "0000"
    for s in range(0,101):
        os.system('python run_serial_generation.py --model_type gpt2 --temperature 1.0 --top_k 50 --top_p 1.0 --model_name_or_path output/checkpoint-{} --length 700 --prompt "The eternal sky " --seed {} --num_samples 1'.format(ch, s)) 

