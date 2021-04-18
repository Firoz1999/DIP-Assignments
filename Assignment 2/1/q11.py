class Mat:
    def __init__(self,row,col):
        self.row=row
        self.col=col

class Index:
    def __init__(self,x,y):
        self.x=x
        self.y=y

def func_update(value,beg,end):
    return max(beg,min(value,end))

def average_filtering(img,filter_size=Mat(3,3),filter_center=Index(1,1)):
    row,col,ch=img.shape
    print("Shape ",img.shape)
    filter_area=filter_size.row*filter_size.col
    total=100/(row*col)
    counter=0
    img_copy=img.copy()
    for i in range(row):
        for j in range(col):
            x_start=func_update(i-filter_center.x,0,row)
            y_start=func_update(j-filter_center.y,0,col)
            x_end=func_update(x_start+filter_size.row-1,0,row)
            y_end=func_update(y_start+filter_size.col-1,0,col)    
            for cha in range(ch):
                img_copy[i][j][cha]=np.sum(img[x_start:x_end+1,y_start:y_end,cha])/filter_area
        
            print(">>> {0:.2f}% Percent Complete   ".format(counter*total),end="\r")
            counter+=1
    print()
    return img_copy

def multishow(rows=1,columns=1,*all_images):
    for i in range(len(all_images)):
        plt.subplot(rows,columns,i+1)
        plt.axis("off")
        plt.title("Image "+str(i+1))
        plt.imshow(all_images[i])
    plt.show()

def main():
    img=mpimg.imread("./lena.jpg")
    lena_img_noise_level=[]
    for i in range(1,10+1):
        lena_img_noise_level.append(random_noise(img, mode='s&p',amount=i/10))
    plt.figure(figsize=(10,5),dpi=150)
    for i in range(1,10+1):
        plt.subplot(2,5,i)
        plt.axis("off")
        plt.title("Image Noise\nLevel "+str(i)+"/10")
        plt.imshow(lena_img_noise_level[i-1])
    plt.savefig("q11_output/out_noise_level.jpg")
    # print("Noisy Images")
    plt.show()
    
    img_noisy=lena_img_noise_level[5]
    plt.imshow(img_noisy)
    plt.savefig("q11_output/out_noisy.jpg",dpi=300)

    img_avg_3x3=average_filtering(img_noisy,Mat(3,3),Index(1,1))
    plt.imshow(img_avg_3x3)
    plt.savefig("q11_output/out_avg_3x3.jpg",dpi=300)
    
    img_avg_5x5=average_filtering(img_noisy,Mat(5,5),Index(1,1))
    plt.imshow(img_avg_5x5)
    plt.savefig("q11_output/out_avg_5x5.jpg",dpi=300)
    
    img_avg_7x7=average_filtering(img_noisy,Mat(7,7),Index(1,1))
    plt.imshow(img_avg_7x7)
    plt.savefig("q11_output/out_avg_7x7.jpg",dpi=300)
    
    multishow(1,5,img,img_noisy,img_avg_3x3,img_avg_5x5,img_avg_7x7)

if (__name__=="__main__"):
    from skimage.util import random_noise
    from matplotlib import pyplot as plt,image as mpimg
    import numpy as np
    main()