# Author: Morgan Sandler (sandle20@msu.edu)
# generate crema confusion
import matplotlib.pyplot as plt
import seaborn as sns

""" conf_mat from CREMA multiclass
conf_mat = [[162, 24, 68, 66],
            [ 20, 232, 66,   2],
            [ 43  ,54 ,212,  11],
            [ 44  , 6,  27, 243]]
"""
# visualization data from conf_matrix in DT_EmoRecog
# CONF MAT FROM DUAL SVM (SAD-OTHER) and (OTHER->ANG, HAP, NEU)
conf_mat = [[192 ,  61  ,41,  26],
        [ 15,   269  ,33  , 3],
        [ 21 ,  122, 168,   9],
        [ 24  , 14,  19 , 263]]

ax= plt.subplot()
sns.heatmap(conf_mat, annot=True, fmt='g', cmap='Blues')
plt.xlabel('Predicted')
plt.ylabel('True')
plt.title('CREMA-D Speech Emotion Recognition (Hierarchical Classifier)')
labels = ['Happy', 'Sad', 'Neutral', 'Angry']
ax.xaxis.set_ticklabels(labels)
ax.yaxis.set_ticklabels(labels)
plt.show()
