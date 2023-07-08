# Super Resolution


## SR with External Database
```
cd SwinIR/
```
Put all the images into ```../test_data/cropped_imgs_png/```, and run SwinSR:

```
python main_test_swinir.py --task real_sr --scale 4 --large_model --model_path model_zoo/swinir/003_realSR_BSRGAN_DFOWMFC_s64w8_SwinIR-L_x4_GAN.pth --folder_lq ../test_data/cropped_imgs_png/
```


## SR with Reference Images
```
cd TTSR/
```

Pre-trained models can be downloaded from [google drive](https://drive.google.com/drive/folders/1CTm-r3hSbdYVCySuQ27GsrqXhhVOS-qh?usp=sharing). Put them in ```./weights/```.


Inside ```test.sh```, change ```save_dir```, ```lr_path```, ```ref_path```, ```model_path``` to your own path:
```
python main.py --save_dir ./results/selfies/ \
               --reset True \
               --log_file_name test.log \
               --test True \
               --num_workers 1 \
               --lr_path ../test_data/selfies/s26_m_small.png \
               --ref_path ../test_data/selfies/s20_m.jpg ../test_data/selfies/s23_m.jpg ../test_data/selfies/s25_m.jpg ../test_data/selfies/s27_m.jpg \
               --model_path ./weights/TTSR.pt
```

Run ```test.sh```:
```
sh test.sh
```

## SR with Single Image
```
cd pytorch-ZSSR/
```

Run this script to train/inference on ```random.png``` and save results to ```./results```. Change ```X8_REAL_CONF``` (scale factors + some settings) in ```configs.py``` if needed.
```
python run_ZSSR_single_input_with_refs.py ../test_data/cropped_imgs_png/random.png 0 0 0 X8_REAL_CONF ./results/
```