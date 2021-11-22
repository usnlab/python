from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm 
import re
import collections

file_content = open('../Data/LoremIpsum.txt', encoding="utf-8").read()
spwords = set(STOPWORDS)
spwords.add('efficitur')

wc = WordCloud(max_font_size=200, stopwords=spwords, background_color='white', width=800, height=800)
wc.generate(file_content)

plt.figure(figsize=(10,8))
plt.imshow(wc)
plt.tight_layout(pad=0)
plt.axis('off')
#plt.show()    # To save the image, show() should follow savefig()
plt.savefig('../Data/LoremIpsum.png')
plt.show()