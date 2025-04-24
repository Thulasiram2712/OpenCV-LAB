import cv2
def read_display():
    img_paths=[
        'HP.jpg',
        'Output_img.bmp',
        'lion.png',
        'sample.tiff'
    ]
    for img_path in img_paths:
        img=cv2.imread(img_path)
        if img is None:
            print(f"Error: Image '{img_path}'not Found!")
            continue
        format_name=img_path.split('.')[-1].upper()
        cv2.imshow(f"Image as {format_name}",img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
read_display()