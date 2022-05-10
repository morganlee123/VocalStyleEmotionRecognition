# Author: Morgan Sandler (sandle20@msu.edu)
# This program generates all inter emotion datapoints and saves to sv_similarity_emotion_impact.txt

from audioop import reverse
import sys
import csv
import numpy as np
import os
import torch
import torchaudio
from speechbrain.pretrained import SpeakerRecognition
from deeptalk_matcher import dt_verify
from os import listdir, lseek
from os.path import isfile, join

# Model is downloaded from the speechbrain HuggingFace repo
tmpdir = getfixture("tmpdir")
verification = SpeakerRecognition.from_hparams(
    source="speechbrain/spkrec-ecapa-voxceleb",
    savedir="pretrained_models/spkrec-ecapa-voxceleb",
)


def match_scorer(sample, target):
    signal1, fs = torchaudio.load(sample)
    signal2, fs = torchaudio.load(target)
    score_1, prediction_1 = verification.verify_batch(signal1,signal2)
    #score_1 = dt_verify(sample, target)

    return score_1


def main(argv):
    file1=argv[0]
    file2=argv[1]
    score1=match_scorer(file1,file2)
    print(score1)

if __name__ == "__main__":
    #main(sys.argv[1:])

    import itertools
    import glob
    import numpy as np

    #TODO: add your own crema path
    all_samples = glob.glob('../../sandle20/CREMA-D/AudioWAV/*')
    subjects_dict = {}
    for s in list(range(1001, 1092)):
        subjects_dict[s] = []
    for s in all_samples:
        part=s.split('_')
        subject = int(part[0].split('/')[5]) # subject number
        #print(subject)
        if part[1] == 'IWL':
            subjects_dict[subject].append( (subject, part[2], part[3], s) )
        
    tests = []
    subjects = list(range(1001, 1092))
    for sub in subjects:
        tests_sub = list(itertools.combinations(subjects_dict[sub], r=2))
        for t in tests_sub:
            tests.append(t)
    
    print(len(tests), 'to perform')
    print(tests[0])

    # scores[subject # ] = [[ANG, SAD, 0.51], [NEU, ANG, .32], ... 15 of these]
    scores = {}
    for s in list(range(1001, 1092)):
        scores[s] = []
    from tqdm import tqdm
    for test in tqdm(tests): # TODO: temp remove slice
        
        if test[0][1] < test[1][1]:
            if test[0][0] == test[1][0]:
                scores[test[0][0]].append( (  test[0][1], test[1][1] ,match_scorer(test[0][3],test[1][3])) )# index 3 is the filepath
        else:
            if test[0][0] == test[1][0]:
                scores[test[0][0]].append( (  test[1][1], test[0][1] ,match_scorer(test[0][3],test[1][3])) )# index 3 is the filepath
    #print(scores)
    #sorted_by_score = sorted(scores, key=lambda tup: tup[2], reverse=True)

    #ang, dis, fea, hap, neu, sad = [], [], [], [], [], []

    ang_dis, ang_fea, ang_hap, ang_neu, ang_sad = [], [], [], [], []
    dis_fea, dis_hap, dis_neu, dis_sad = [], [], [], []
    fea_hap, fea_neu, fea_sad = [], [], []
    hap_neu, hap_sad = [], []
    neu_sad = []
    
    for sub in subjects:
        for score in scores[sub]:
            if score[0] == 'ANG' and score[1] == 'DIS':
                ang_dis.append(float(score[2][0][0]))
            elif score[0] == 'ANG' and score[1] == 'FEA':
                ang_fea.append(float(score[2][0][0]))
            elif score[0] == 'ANG' and score[1] == 'HAP':
                ang_hap.append(float(score[2][0][0]))
            elif score[0] == 'ANG' and score[1] == 'NEU':
                ang_neu.append(float(score[2][0][0]))
            elif score[0] == 'ANG' and score[1] == 'SAD':
                ang_sad.append(float(score[2][0][0]))
            elif score[0] == 'DIS' and score[1] == 'FEA':
                dis_fea.append(float(score[2][0][0]))
            elif score[0] == 'DIS' and score[1] == 'HAP':
                dis_hap.append(float(score[2][0][0]))
            elif score[0] == 'DIS' and score[1] == 'NEU':
                dis_neu.append(float(score[2][0][0]))
            elif score[0] == 'DIS' and score[1] == 'SAD':
                dis_sad.append(float(score[2][0][0]))
            elif score[0] == 'FEA' and score[1] == 'HAP':
                fea_hap.append(float(score[2][0][0]))
            elif score[0] == 'FEA' and score[1] == 'NEU':
                fea_neu.append(float(score[2][0][0]))
            elif score[0] == 'FEA' and score[1] == 'SAD':
                fea_sad.append(float(score[2][0][0]))
            elif score[0] == 'HAP' and score[1] == 'NEU':
                hap_neu.append(float(score[2][0][0]))
            elif score[0] == 'HAP' and score[1] == 'SAD':
                hap_sad.append(float(score[2][0][0]))
            elif score[0] == 'NEU' and score[1] == 'SAD':
                neu_sad.append(float(score[2][0][0]))




print(' ANG-DIS', ang_dis)
print(' ANG-FEA', ang_fea)
print(' ANG-HAP', ang_hap)
print(' ANG-NEU', ang_neu)
print(' ANG-SAD', ang_sad)

print(' DIS-FEA', dis_fea)
print(' DIS-HAP', dis_hap)
print(' DIS-NEU', dis_neu)
print(' DIS-SAD', dis_sad)

print(' FEA-HAP', fea_hap)
print(' FEA-NEU', fea_neu)
print(' FEA-SAD', fea_sad)

print(' HAP-NEU', hap_neu)
print(' HAP-SAD', hap_sad)

print(' NEU-SAD', neu_sad)

f = open("sv_similarity_emotion_impact.txt", "w")

f.write('ANG-DIS ' + str(ang_dis) + '\n')
f.write('ANG-FEA ' + str(ang_fea) + '\n')
f.write('ANG-HAP ' + str(ang_hap) + '\n')
f.write('ANG-NEU ' + str(ang_neu) + '\n')
f.write('ANG-SAD ' + str(ang_sad) + '\n')

f.write('DIS-FEA ' + str(dis_fea) + '\n')
f.write('DIS-HAP ' + str(dis_hap) + '\n')
f.write('DIS-NEU ' + str(dis_neu) + '\n')
f.write('DIS-SAD ' + str(dis_sad) + '\n')

f.write('FEA-HAP ' + str(fea_hap) + '\n')
f.write('FEA-NEU ' + str(fea_neu) + '\n')
f.write('FEA-SAD ' + str(fea_sad) + '\n')

f.write('HAP-NEU ' + str(hap_neu) + '\n')
f.write('HAP-SAD ' + str(hap_sad) + '\n')

f.write('NEU-SAD ' + str(neu_sad) + '\n')

f.close()



