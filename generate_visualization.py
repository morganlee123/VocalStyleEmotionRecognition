# Author: Morgan Sandler (sandle20@msu.edu)
# This program generates Figure 1 in the paper
# All datapoints plot in this figure are precomputed and loaded from sv_similarity_emotion_impact.txt,
# baseline.txt, and impost.txt

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Load average scores file 
data = open('sv_similarity_emotion_impact.txt', 'r')
lines = data.readlines()

combos_emotion_data = []
combos_emotion_labels = []
for line in lines:
    combo = line[0:8]
    arr_str = line[8:].replace("[", "")
    arr_str = arr_str.replace("]", "")
    arr_str = arr_str.split(', ')
    arr_float = [float(i) for i in arr_str]
    arr = np.array(arr_float)
    combos_emotion_data.append(arr)
    combos_emotion_labels.append(combo[0:7])

# LOAD BASELINE
baseline = np.fromfile('./baseline.txt', sep=', ')
impost = np.fromfile('./impost.txt', sep=', ')
combos_emotion_data.append(baseline)
combos_emotion_data.append(impost)
combos_emotion_labels.append('GENUINE (NEU-NEU)')
combos_emotion_labels.append('IMPOSTOR (NEU-NEU)')

fig = plt.figure(figsize =(10, 7))
ax = fig.add_subplot(111)
 
# Creating axes instance
bp = ax.boxplot(combos_emotion_data, patch_artist = True,
                notch ='True', vert = 0)
 
import random
colors = ['#FFC107', '#FFC107', '#FFC107', '#FFC107', '#FFC107', '#FFC107', '#FFC107', '#FFC107', '#FFC107', '#FFC107', '#FFC107', '#FFC107', '#FFC107', '#FFC107', '#FFC107', '#005AB5', '#DC3220']
 
for patch, color in zip(bp['boxes'], colors):
    patch.set_facecolor(color)
 
# changing color and linewidth of
# whiskers
for whisker in bp['whiskers']:
    whisker.set(color ='#8B008B',
                linewidth = 1.5,
                linestyle =":")
 
# changing color and linewidth of
# caps
for cap in bp['caps']:
    cap.set(color ='#8B008B',
            linewidth = 2)
 
# changing color and linewidth of
# medians
for median in bp['medians']:
    median.set(color ='red',
               linewidth = 3)
 
# changing style of fliers
for flier in bp['fliers']:
    flier.set(marker ='D',
              color ='#e7298a',
              alpha = 0.5)
     
# x-axis labels
ax.set_yticklabels(combos_emotion_labels)
 
# Adding title
plt.title("Speaker Verification Score Variation Over Different Emotions")
plt.xlabel('Similarity Score (Cosine Similarity)')
 
# Removing top axes and right axes
# ticks
ax.get_xaxis().tick_bottom()
ax.get_yaxis().tick_left()

import matplotlib.patches as mpatches


gen = mpatches.Patch(color='#005AB5', label='Intra-Emotion Genuine Score')
imp = mpatches.Patch(color='#DC3220', label='Intra-Emotion Impostor Score')
inter = mpatches.Patch(color='#FFC107', label='Inter-Emotion Genuine Score')
plt.legend(handles=[gen,imp, inter], loc='lower left')
# show plot
plt.show()


"""
import random
c = ["#"+''.join([random.choice('0123456789ABCDEF') for j in range(6)])
             for i in range(15)]

plt.bar(scores['comp'], scores['sim'], color=c, edgecolor='black')
plt.xticks(rotation = 45)
plt.show()
"""