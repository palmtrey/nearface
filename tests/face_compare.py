# Title: face_compare.py
#
# Purpose/Function: Compares all morphed faces found in /images/morphs to each of the images 
# found in /images/stills using the DeepFace libary. Writes a csv file containing the 
# closest 65 faces to the morph, and saves under /csvs.
#
# Developer: Cameron Palmer, campalme@clarkson.edu
#
# Last Modified: March 17th, 2022
#

from nearface import NearFace
import os
from tqdm import tqdm


def compare(morphs_dir:str, stills_dir:str, output_csvs_dir:str):
  for filename in tqdm(os.listdir(morphs_dir)):
    try:
      df = NearFace.find(img_path = morphs_dir + '/' + filename, db_path = stills_dir, enforce_detection= False, use_threshold=False)
      if not os.path.isdir(output_csvs_dir):
        os.mkdir(output_csvs_dir)
      df.to_csv(output_csvs_dir + '/' + filename + '.csv', sep='\t')
      
    except AttributeError:
      print('AttributeError encountered... skipping morph ' + filename)

if __name__ == '__main__':
  compare(
    morphs_dir='images/morphs_renamed',
    stills_dir='images/stills_renamed_reduced',
    output_csvs_dir='output_csvs'
  )