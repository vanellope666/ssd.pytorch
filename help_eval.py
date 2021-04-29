import os

if __name__ == '__main__':
    target = [130000, 140000, 150000, 160000, 170000]
    for i in target:
        op = "python eval.py --trained_model weights/5e_4_4/ssd300_VOC_{}.pth > weights/5e_4_4/{}.txt".format(i, i)
        print(op)
        os.system(op)
