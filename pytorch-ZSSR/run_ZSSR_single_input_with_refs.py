import sys
import os
import configs
import ZSSR


def main(input_img, ground_truth, kernels, gpu, conf_str, results_path):
    # Choose the wanted GPU

    # 0 input for ground-truth or kernels means None
    ground_truth = None if ground_truth == '0' else ground_truth
    print('*****', kernels)
    kernels = None if kernels == '0' else kernels.split(';')[:-1]

    # # Setup configuration and results directory
    # conf = configs.Config()
    # if conf_str is not None:
    #     exec ('conf = configs.%s' % conf_str)
    # conf.result_path = results_path

    # Setup configuration and results directory
    conf = configs.Config()
    if conf_str is not None:
        dic={"conf":conf, "configs":configs}
        exec ('conf = configs.%s' % conf_str, dic)
        conf=dic["conf"]
    conf.result_path = results_path

    if not os.path.exists(conf.result_path):
        os.makedirs(conf.result_path)

    # Run ZSSR on the image
    # NOTE: hack some references to the input image

    # ref_imgs_paths = ['/home/khiem/workspace/ilim-projects/super-resolution/srntt-pytorch/data/CUFED_small/012_1.png',
    #                   '/home/khiem/workspace/ilim-projects/super-resolution/srntt-pytorch/data/CUFED_small/012_2.png',
    #                   '/home/khiem/workspace/ilim-projects/super-resolution/srntt-pytorch/data/CUFED_small/012_3.png',
    #                   '/home/khiem/workspace/ilim-projects/super-resolution/srntt-pytorch/data/CUFED_small/012_4.png']

    ref_imgs_paths = []

    net = ZSSR.ZSSR(input_img, ref_imgs_paths, conf, ground_truth, kernels)
    net.run()


if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5], sys.argv[6])
