#!/bin/bash

input_path=ustims/segmentation/input
detected_path=ustims/segmentation/detected


for input_file in $input_path/*
do
    name=$(basename "$input_file")
    echo $input_file

    CUDA_VISIBLE_DEVICES="0" python NPP_proposal/search.py --datadir $input_file --outdir $detected_path
    # CUDA_VISIBLE_DEVICES="0" python NPP_segmentation/train.py --datadir "${detected_path}/${name}" --basedir ./results --p_topk 3
done

