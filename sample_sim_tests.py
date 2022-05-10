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

    # TODO: Add your own CREMA data path here
    samples = glob.glob('/Users/morgan/Work/MSU/IPROBE/data/AudioWAV/*')
    
    combos = itertools.combinations(samples, r=2) 
    tests = [t for t in combos]

    scores = []
    from tqdm import tqdm

    

    for test in tqdm(tests):
        if test[0].split('_')[1] == test[1].split('_')[1]:
            scores.append((test[0].split('_')[1], 
            (test[0].split('_')[0]+test[0].split('_')[2]).split('/')[2], 
            (test[1].split('_')[0]+test[1].split('_')[2]).split('/')[2], 
            str(float(match_scorer(test[0],test[1])[0][0]))))
    
    sorted_by_score = sorted(scores, key=lambda tup: tup[2], reverse=True)

    # mapping {0:ang, 1:sad, 2:neu, 3:hap, 4:fea, 5:dis}
    def emo_map(emotion):
        if emotion == 'ANG':
            return 0
        elif emotion == 'SAD':
            return 1
        elif emotion == 'NEU':
            return 2
        elif emotion == 'HAP':
            return 3
        elif emotion == 'FEA':
            return 4
        elif emotion == 'DIS':
            return 5
        return -1 # error case

    #print('BASELINE TEST: SAME SPEAKER DIFFERENT VOICE LINES',match_scorer('./samples/1012_IWL_NEU_XX.wav', './samples/1013_WSI_NEU_XX.wav')[0][0])

    print('Same speaker, different acted emotion, same voice sentence spoke')
    score_file = open("scores.txt", "w")

    for sentence, sample1, sample2, score in sorted_by_score:
        emo1 = sample1[4:7]
        sub1 = sample1[0:4]
        
        emo2 = sample2[4:7]
        sub2 = sample2[0:4]

        # if same subject
        if int(sub1) == int(sub2):
            print('SENTENCE', sentence,'- Subject', sub1, 'Emotion 1:', emo1, 'Emotion 2:', emo2, 'Speaker similarity score', round(float(score),3))
            score_file.write(sentence + ' ' + sub1 + ' ' + emo1 + ' ' + emo2 + ' ' + str(round(float(score),3)) + '\n')
    score_file.close()
    
    
    

    #for row in comparison_matrix:
    #    print(row)

    #score_file = open("scores.txt", "w")
    #for element in sorted_by_score:
    #    score_file.write(element[0] + ' ' + element[1] + ' ' + element[2] + "\n")
    #score_file.close()
    