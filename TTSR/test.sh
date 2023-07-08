### test
python main.py --save_dir ./results/selfies/ \
               --reset True \
               --log_file_name test.log \
               --test True \
               --num_workers 1 \
               --lr_path ../test_data/selfies/s26_m_small.png \
               --ref_path ../test_data/selfies/s20_m.jpg ../test_data/selfies/s23_m.jpg ../test_data/selfies/s25_m.jpg ../test_data/selfies/s27_m.jpg \
               --model_path ./weights/TTSR.pt
