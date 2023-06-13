import cv2

def apply_mosaic(image, block_size):
    # 获取图像的宽度和高度
    height, width, _ = image.shape

    # 计算图像中每个块的数量
    num_blocks_x = width // block_size
    num_blocks_y = height // block_size

    # 对每个块进行马赛克处理
    for i in range(num_blocks_y):
        for j in range(num_blocks_x):
            # 获取当前块的起始和结束位置
            x_start = j * block_size
            y_start = i * block_size
            x_end = x_start + block_size
            y_end = y_start + block_size

            # 获取当前块的图像数据
            block = image[y_start:y_end, x_start:x_end]

            # 计算当前块的平均像素值
            avg_color = block.mean(axis=(0, 1)).astype(int)

            # 将当前块的像素值设为平均像素值
            image[y_start:y_end, x_start:x_end] = avg_color

    return image

if __name__ == '__main__':
    # 读取图像
    image = cv2.imread('img.png')
    mosaic_image =image.copy()
    # 应用马赛克效果
    mosaic_image = apply_mosaic(mosaic_image, block_size=20)
    print(image.shape,mosaic_image.shape)
    # 显示原始图像和马赛克图像
    cv2.imshow('Original Image', image)
    cv2.imshow('Mosaic Image', mosaic_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
