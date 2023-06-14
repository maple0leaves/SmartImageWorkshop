import os
import numpy as np
from PIL import Image
import cv2

import torch
import torch.nn as nn
import torch.nn.functional as F
import torchvision.transforms as transforms

from MODnet.models.modnet import MODNet


def combine(image, matte, bg):
    # obtain predicted foreground
    image = np.asarray(image)
    if len(image.shape) == 2:
        image = image[:, :, None]
    if image.shape[2] == 1:
        image = np.repeat(image, 3, axis=2)
    elif image.shape[2] == 4:
        image = image[:, :, 0:3]
    matte = np.repeat(np.asarray(matte)[:, :, None], 3, axis=2) / 255
    # print(matte)
    # foreground = image * matte + np.full(image.shape, 255) * (1 - matte)
    # 就这一步有问题
    # print(bg)
    # print(bg.shape)
    # print(np.around((1 - matte)))
    # print(matte.shape)
    # print(bg * (1 - matte))
    # print((bg * (1 - matte)).shape)
    foreground = image * matte + bg * (1 - matte)
    # foreground = image * matte + bg * np.around((1 - matte))

    return foreground


# 如果background是数组 则代表(red, green, blue)
def get_bg(_background, img_shape):
    _bg = np.zeros(img_shape)
    if isinstance(_background, tuple):
        _bg[:, :, 2] = _background[2]
        _bg[:, :, 1] = _background[1]
        _bg[:, :, 0] = _background[0]
    else:
        _bg = cv2.imread(_background)
        _bg = cv2.cvtColor(_bg, cv2.COLOR_RGB2BGR)
        _bg = cv2.resize(_bg, (img_shape[1], img_shape[0]))
    return _bg


def get_image_tensor(_image, _ref_size, _im_transform):
    # unify image channels to 3
    _im = np.asarray(_image)
    if len(_im.shape) == 2:
        _im = _im[:, :, None]
    if _im.shape[2] == 1:
        _im = np.repeat(_im, 3, axis=2)
    elif _im.shape[2] == 4:
        _im = _im[:, :, 0:3]

    # convert image to PyTorch tensor
    _im = Image.fromarray(_im)
    _im = _im_transform(_im)

    # add mini-batch dim
    _im = _im[None, :, :, :]

    # resize image for input
    _im_b, _im_c, _im_h, _im_w = _im.shape
    if max(_im_h, _im_w) < _ref_size or min(_im_h, _im_w) > _ref_size:
        if _im_w >= _im_h:
            _im_rh = _ref_size
            _im_rw = int(_im_w / _im_h * _ref_size)
        elif _im_w < _im_h:
            _im_rw = _ref_size
            _im_rh = int(_im_h / _im_w * _ref_size)
    else:
        _im_rh = _im_h
        _im_rw = _im_w

    _im_rw = _im_rw - _im_rw % 32
    _im_rh = _im_rh - _im_rh % 32
    _im = F.interpolate(_im, size=(_im_rh, _im_rw), mode='area')

    return _im, _im_h, _im_w


def run(input_image, background_image,output_path='.'):
    # define hyper-parameters
    ref_size = 512

    # define image to tensor transform
    im_transform = transforms.Compose(
        [
            transforms.ToTensor(),
            transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5))
        ]
    )

    modnet = MODNet(backbone_pretrained=False)
    modnet = nn.DataParallel(modnet)

    model_path = "./MODnet/modnet_photographic_portrait_matting.ckpt"
    # input_dir = "./inputimage/"
    # background_dir = "."
    # output_dir = "."

    # input_path = os.path.join(input_dir, input_image)
    input_path = input_image
    # output_path = os.path.join(output_dir, output_image)
    # output_path = output_image
    background_path = background_image
    # if not isinstance(background_image, tuple):
    #     background_path = os.path.join(background_dir, background_image)
    # else:
    #     background_path = background_image

    if torch.cuda.is_available():
        modnet = modnet.cuda()
        weights = torch.load(model_path)
    else:
        weights = torch.load(model_path, map_location=torch.device('cpu'))
    modnet.load_state_dict(weights)
    modnet.eval()

    # read image
    im = Image.open(input_path)

    image_torch, image_torch_h, image_torch_w = get_image_tensor(im, ref_size, im_transform)

    # inference
    _, _, matte = modnet(image_torch.cuda() if torch.cuda.is_available() else image_torch, True)

    # resize and save matte
    matte = F.interpolate(matte, size=(image_torch_h, image_torch_w), mode='area')
    matte = matte[0][0].data.cpu().numpy()
    # matte_name = input_path.split('.')[1] + '.png'
    matte = Image.fromarray(((matte * 255).astype('uint8')), mode='L')
    bg = get_bg(background_path, np.asarray(im).shape)
    foreground = combine(im, matte, bg)

    # Image.fryomarray(np.uint8(foreground)).save(output_path)
    return np.uint8(foreground)

if __name__ == '__main__':
    # input_image_file = "img_1.png"
    # background_image_file = "img_2.png"
    # # 格式为(red, green, blue)
    # # background_image_file = (255, 0, 0)
    # output_image_file = "output_bg.jpg"
    # run(input_image_file, background_image_file, output_image_file)
    ''' input_image,background_image,output_image'''
    run('./inputimage/img_1.png','img_2.png','out.jpg')

