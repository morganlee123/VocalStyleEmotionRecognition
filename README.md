A Vocal Style Neutral Network for Recognizing Speaker Emotions
===============================

A Speech Emotion Recognition System that uses Vocal Style embeddings as features. The network used for encoding embeddings is based on the implementation of the architecture described in *A Neural Network for Recognizing Speaker Emotions* by M. Sandler and A. Ross. This program provides utilities and scripts to transfer knowledge learned to the Speech Emotion Recognition Domain.

## Research Article

[Morgan Sandler](https://github.com/morganlee123), [Arun Ross](http://www.cse.msu.edu/~rossarun/), *A Neural Network for Recognizing Speaker Emotions*
- arXiv: [COMING SOON](https://arxiv.org/abs/2012.05084)

## Description

add description here


**Downloading the DeepTalk code**

REFINE THESE INSTRUCTIONS

1) Clone the git repository

```
git clone git@github.com:ChowdhuryAnurag/DeepTalk-Deployment.git
```

2) Now you should have a folder named 'DeepTalk-Deployment'

3) Go into the folder 'DeepTalk-Deployment'
```
cd DeepTalk-Deployment
```

4) Please contact the maintainer of this repository at [chowdh51@msu.edu] for access to the pretrained DeepTalk models. Unzip 'trained_models.zip' (received separately from the maintainer) into this folder
```
unzip trained_models.zip
```

5) Now you should have a folder named 'trained_models' with several pretrained models in it

6) The Generic model is primarily used as a starting point for fine-tuning with speech data from a target speaker. The other models (Hannah, Ted, and Gordon Smith) are some sample finetuned models based on speech data from internal sources.

7) The Generic model is trained on the [LibriSpeech](http://www.openslr.org/resources/12/train-other-500.tar.gz) and [VoxCeleb 1 and 2](http://www.robots.ox.ac.uk/~vgg/data/voxceleb/) datasets.


**Setting up the python environment for running the DeepTalk code**

1) The model was implemented in PyTorch 1.3.1 and tensorflow 1.14 using Python 3.6.8 and may be compatible with different versions of PyTorch, tensorflow, and Python, but it has not been tested. (The GPU versions of pytorch and tensorflow is recommended for faster training and inference)

    1.1) Install anaconda python distribution from https://www.anaconda.com/products/individual

    1.2) Create an anaconda environment called 'deeptalk'
    ```
    conda create -n deeptalk python=3.6.8
    ```
    Type [y] when prompted to Proceed([y]/n)
    
    1.3) Activate the deeptalk python environment
    ```
    conda activate deeptalk
    ```

2) Additional requirements are listed in the [./requirements.txt](./requirements.txt) file. Install them as follows:
    ```
    pip install -r requirements.txt
    ```

3) Now, we need to install [Montreal-Forced-Aligner](https://montreal-forced-aligner.readthedocs.io/en/latest/). For this project it could be done in the following two ways:

    3.1) Download and install the Montreal-Forced-Aligner following the instructions [here](https://montreal-forced-aligner.readthedocs.io/en/latest/installation.html). We have included a copy of Montreal-Forced-Aligner (both for Linux and Mac OS) with this repository to serve as a template for the directory structure expected by the DeepTalk implementation. Please note that the *librispeech-lexicon.txt* file included in both the montreal_forced_aligned_mac and montreal_forced_aligned_linux are important for this project and should be retained in this final installation of Montreal-Forced-Aligner.
    
    3.2) Alternatively, you can also run the [install_MFA_linux.sh](./install_MFA_linux.sh) script (only works for Linux machines) to automatically download and install Montreal-Forced-Aligner. This script also fixes some of the most common installation [issues](https://github.com/MontrealCorpusTools/Montreal-Forced-Aligner/issues/109) associated with running Montreal-Forced-Aligner on linux machines.
    ```
    ./install_MFA_linux.sh
    ```

    3.3) Now, run the following command to ensure Montreal-Forced-Aligner was installed correctly and is working fine.
    ```
    montreal_forced_aligner_linux/bin/mfa_align
    ```
    You should get the following output if everything is working fine:
    ```
    usage: mfa_align [-h] [-s SPEAKER_CHARACTERS] [-b BEAM] [-t TEMP_DIRECTORY]
                    [-j NUM_JOBS] [-v] [-n] [-c] [-d] [-e] [-i] [-q]
                    corpus_directory dictionary_path acoustic_model_path
                    output_directory
    mfa_align: error: the following arguments are required: corpus_directory, dictionary_path, acoustic_model_path, output_directory

**Acknowledgement**

Portions of this implementation are based on [this](https://github.com/CorentinJ/Real-Time-Voice-Cloning) repository.

## Citation
If you use this repository then please cite:

```bibtex
@InProceedings{chowdhDeepTalk21,
  author       = "Chowdhury, A. and Ross, A. and David, P.",
  title        = "DeepTalk: Vocal Style Encoding for Speaker Recognition and Speech Synthesis",
  booktitle    = "ICASSP",
  year         = "2021",
}
```
