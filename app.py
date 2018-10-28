import jieba
import matplotlib.pyplot as plt
import numpy as np
from wordcloud import WordCloud
from PIL import Image

with open('./可不可以.txt') as file:
    text = file.read()
cut_text = jieba.cut(text)

result = '/'.join(cut_text)

img = Image.open('./20180502212744299.png')
img_array = np.array(img)

wc = WordCloud(
    font_path='思源宋体.otf',
    background_color='pink',
    width=800,
    height=600,
    max_font_size=50,
    max_words=100,
    mask=img_array
)
wc.generate(result)
wc.to_file('./可不可以.png')

plt.figure('Word Cloud')
plt.imshow(wc)
plt.axis('off')
plt.show()
