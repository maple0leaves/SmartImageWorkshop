import torch
import cv2
import numpy as np
import os
import shutil
from animegan2.model import Generator
# from torchvision.transforms.functional import to_pil_image
# from PIL import Image


def load_image(image_path):
    img = cv2.imread(image_path).astype(np.float32)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    img = torch.from_numpy(img)
    img = img/127.5 - 1.0

    return img

def animestart(path):
    #加载图片
    image = load_image(path)   #RGB  此处需要加载自己的图片
    #image.shape  #HWC
    # models=['face_paint_512_v2','face_paint_512_v1','paprika','celeba_distill']
    model='./animegan2/face_paint_512_v2'
    model_path=f'{model}.pt'
    # if os.path.exists('./animegan_outs/'):
    #     shutil.rmtree('./animegan_outs')
    #     os.makedirs('./animegan_outs/')
    # else:
    #     os.makedirs('./animegan_outs/')
    device= 'cuda' if torch.cuda.is_available() else 'cpu'
    net = Generator()
    # images=[]
    # for model,model_path in zip(models,models_path):
    # net.load_state_dict(torch.load(model_path, map_location="cpu"))
    net.load_state_dict(torch.load(model_path))
    net.to(device).eval()
    with torch.no_grad():
        input = image.permute(2, 0, 1).unsqueeze(0).to(device)   #BCHW
        out = net(input, False).squeeze(0).permute(1, 2, 0).cpu().numpy()  #HWC
        out = (out + 1)*127.5
        out = np.clip(out, 0, 255).astype(np.uint8)
#opencv里就是HWC
    return out
        #opencv 里面就是np unit8类型
        # pil_out=to_pil_image(out)
        # pil_out.save(f'./animegan_outs/{model}.jpg')   #保存处理过后的图片
            # images.append(pil_out)

#
# #在每个处理过的图片上添加使用的模型，并进行合并
# font=cv2.FONT_HERSHEY_SIMPLEX    #使用默认字体
# UNIT_WIDTH_SIZE,UNIT_HEIGHT_SIZE=images[0].size[:2]
#
#
# images_add_font=[]      #保存加了文字之后的图片
# for model,image in zip(models,images):
#     image_font=cv2.putText(np.array(image),model,(280,50),font,1.2,(0,0,0),3)
#     #添加文字，1.2表示字体大小，（280,50）是初始的位置，(0,0,0)表示颜色，3表示粗细
#
#     images_add_font.append(Image.fromarray(image_font))
#
#
# target = Image.new('RGB', (UNIT_WIDTH_SIZE * 2, UNIT_HEIGHT_SIZE * 2))   #创建成品图的画布
# #第一个参数RGB表示创建RGB彩色图，第二个参数传入元组指定图片大小，第三个参数可指定颜色，默认为黑色
# for row in range(2):
#     for col in range(2):
#         #对图片进行逐行拼接
#         #paste方法第一个参数指定需要拼接的图片，第二个参数为二元元组（指定复制位置的左上角坐标）
#         #或四元元组（指定复制位置的左上角和右下角坐标）
#         target.paste(images_add_font[2*row+col], (0 + UNIT_WIDTH_SIZE*col, 0 + UNIT_HEIGHT_SIZE*row))
#
#
# target.save('./animegan_outs/out_all.jpg', quality=100) #保存合并的图片