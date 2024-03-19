#!/usr/bin/env python
# encoding: utf-8

# The MIT License


import os
from setuptools import setup, find_packages
import versioneer

KEYWORDS = '''
speech-segmentation
audio-analysis
music-detection
speech-detection
speech-music
gender-equality
gender-classification
speaker-gender
speech
music
voice-activity-detection
praat'''.strip().split('\n')

CLASSIFIERS=[
    'Development Status :: 4 - Beta',
    'Intended Audience :: Developers',
    'Intended Audience :: Education',
    'Intended Audience :: Science/Research',
    'License :: OSI Approved :: MIT License',
    'Operating System :: OS Independent',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3 :: Only',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
    'Programming Language :: Python :: 3.9',
    'Programming Language :: Python :: 3.10', 
    'Programming Language :: Python :: 3.11',   
    'Topic :: Multimedia :: Sound/Audio',
    'Topic :: Multimedia :: Sound/Audio :: Analysis',
    'Topic :: Multimedia :: Sound/Audio :: Speech',
    'Topic :: Scientific/Engineering',
    'Topic :: Scientific/Engineering :: Artificial Intelligence',
    'Topic :: Software Development',
    'Topic :: Software Development :: Libraries',
    'Topic :: Software Development :: Libraries :: Python Modules',
    'Topic :: Sociology',
]

DESCRIPTION='CNN-based audio segmentation toolkit. Does voice activity detection, speech detection, music detection, noise detection, speaker gender recognition.'
LONGDESCRIPTION='''Split audio signal into homogeneous zones of speech, music and noise. Then detects speaker gender.  

inaSpeechSegmenter has been presented at the IEEE International Conference on Acoustics, Speech and Signal Processing (ICASSP) 2018 conference in Calgary, Canada. If you use this toolbox in your research, you can cite the following work in your publications :


```bibtex
@inproceedings{ddoukhanicassp2018,
  author = {Doukhan, David and Carrive, Jean and Vallet, Félicien and Larcher, Anthony and Meignier, Sylvain},
  title = {An Open-Source Speaker Gender Detection Framework for Monitoring Gender Equality},
  year = {2018},
  organization={IEEE},
  booktitle={Acoustics Speech and Signal Processing (ICASSP), 2018 IEEE International Conference on}
}
```

inaSpeechSegmenter won MIREX 2018 speech detection challenge.  
http://www.music-ir.org/mirex/wiki/2018:Music_and_or_Speech_Detection_Results  
Details on the speech detection submodule can be found bellow:  


```bibtex
@inproceedings{ddoukhanmirex2018,
  author = {Doukhan, David and Lechapt, Eliott and Evrard, Marc and Carrive, Jean},
  title = {INA’S MIREX 2018 MUSIC AND SPEECH DETECTION SYSTEM},
  year = {2018},
  booktitle={Music Information Retrieval Evaluation eXchange (MIREX 2018)}
}
```
'''

setup(
    name = "SpeechPartition",
    version = versioneer.get_version(),
    cmdclass = versioneer.get_cmdclass(),
    author = "Kshitiz Tripathi",
    author_email = "tripathikshitiz08@gmail.com",
    test_suite="run_test.py",
    description = DESCRIPTION,
    license = "MIT",
    install_requires=['tensorflow', 'numpy', 'pandas', 'scikit-image', 'pyannote.core', 'matplotlib', 'Pyro4', 'pytextgrid', 'soundfile', 'onnxruntime-gpu'], #'torch'
 #   keywords = "example documentation tutorial",
    url = "https://github.com/ina-foss/inaSpeechSegmenter",
#    packages=['inaSpeechSegmenter'],
    keywords = KEYWORDS,
    packages = find_packages(),
    include_package_data = True,
    data_files = ['LICENSE'],
    long_description=LONGDESCRIPTION,
    long_description_content_type='text/markdown',
    scripts=[os.path.join('scripts', script) for script in \
             ['speech_partition.py', 'speech_partition_pyro_client.py', 'speech_partition_pyro_server.py', 'speech_partition_pyro_client_setjobs.py']],
    classifiers=CLASSIFIERS,
    python_requires='>=3.6',
)
