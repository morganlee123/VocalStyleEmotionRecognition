# Author: Morgan Sandler (sandle20@msu.edu)
# Generates baseline.txt
#

from audioop import reverse
import sys
import csv
import numpy as np
import os
import torch
import torchaudio
from speechbrain.pretrained import SpeakerRecognition
from os import listdir, lseek
from os.path import isfile, join

# Model is downloaded from the speechbrain HuggingFace repo
#tmpdir = getfixture("tmpdir")
verification = SpeakerRecognition.from_hparams(
    source="speechbrain/spkrec-ecapa-voxceleb",
    savedir="pretrained_models/spkrec-ecapa-voxceleb",
)


def match_scorer(sample, target):
    signal1, fs = torchaudio.load(sample)
    signal2, fs = torchaudio.load(target)
    score_1, prediction_1 = verification.verify_batch(signal1,signal2)


    return score_1

import glob
neutral_samples = glob.glob('../../sandle20/CREMA-D/AudioWAV/1012_*_NEU_XX.wav')
import itertools
combos = itertools.combinations(neutral_samples, r=2)
neu_scores = []
from tqdm import tqdm
for file1, file2 in tqdm(combos):
#file1='../../sandle20/CREMA-D/AudioWAV/1012_IWL_NEU_XX.wav'
#file2='../../sandle20/CREMA-D/AudioWAV/1012_WSI_NEU_XX.wav'
    score1=match_scorer(file1,file2)
    neu_scores.append(float(score1[0][0]))

print(neu_scores)
print(len(neu_scores))
print(np.mean(neu_scores), np.std(neu_scores), np.median(neu_scores))

f = open("baseline.txt", "w")
f.write(str(neu_scores))
f.close()
