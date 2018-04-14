from PIL import Image
from scipy import misc
import numpy as np

image3d = misc.imread('test.png')


nx = 20
ny = 20
nz = 3

encrypt_1d = np.zeros(1200)
encrypt_count = 0
for i in range(nx):
    for j in range(ny):
        for k in range(nz):
            encrypt_1d[encrypt_count] = image3d[i,j,k]
            encrypt_count += 1

count = 0
encrypt_3d = np.zeros((20,20,3), dtype=int)
for i in range(nx):
    for j in range(ny):
        for k in range(nz):
            val =  encrypt_1d[count]
            encrypt_3d[i,j,k] = int(val)
            count += 1

print("******************* Encrypted Image ***********************")
print("")
print(encrypt_3d)
print("")
print("******************* OG Image ***********************")
print(image3d)

final_img = Image.fromarray(encrypt_3d, 'RGB')
final_img.save('encrypt_img.png')
final_img.show()

og_img = Image.fromarray(image3d, 'RGB')
og_img.save('og_img.png')
og_img.show()