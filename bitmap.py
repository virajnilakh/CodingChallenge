import urllib.request
from PIL import Image
import numpy as np

w=128
h=128

image=np.zeros((h, w, 3), dtype=np.uint8)
imageLine=[]

for i in range(0,128):
    for j in range(0,128):
        if int(random) <= 0:
            random = urllib.request.urlopen(
                "https://www.random.org/integers/?num=1&min=19999999&max=999999999&col=1&base=10&format=plain&rnd=new").read()
        r=int(random%256)
        random=random/10
        g=int(random%256)
        random=random/10
        b=int(random%256)
        random=random/10
        image[i][j]=[r,g,b]

img = Image.fromarray(image, 'RGB')
img.save('my.png')
img.show()

