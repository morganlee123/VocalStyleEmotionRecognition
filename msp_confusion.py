# Author: Morgan Sandler (sandle20@msu.edu)
# generate msp confusion
import matplotlib.pyplot as plt
import seaborn as sns

# visualization data from conf_matrix in DT_EmoRecog
conf_mat = [[158, 88, 106,  98],
            [ 52 ,184 ,170,  44],
            [ 77 ,130 ,203,  40],
            [102  ,43 , 72 ,233]]

ax= plt.subplot()
sns.heatmap(conf_mat, annot=True, fmt='g', cmap='Blues')
plt.xlabel('Predicted')
plt.ylabel('True')
plt.title('MSP-Podcast Speech Emotion Recognition')
labels = ['Happy', 'Sad', 'Neutral', 'Angry']
ax.xaxis.set_ticklabels(labels)
ax.yaxis.set_ticklabels(labels)
plt.show()
