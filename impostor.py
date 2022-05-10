# Author: Morgan Sandler (sandle20@msu.edu)
# This program generates impostor score baseline

from audioop import reverse
from nis import match
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
import itertools
from tqdm import tqdm
# TODO: Add your own link to CREMA-D data here. This is where I store mine
samples = glob.glob('/Users/morgan/Work/MSU/IPROBE/data/AudioWAV/1*1*_IWL_NEU_XX.wav')

combos = itertools.combinations(samples, r=2) 
tests = [t for t in combos]

impostors = []
for t in tqdm(tests):
    impostor = match_scorer(t[0], t[1])
    impostors.append(float(impostor[0][0]))
print(impostors)
# save this to impostor.txt manually