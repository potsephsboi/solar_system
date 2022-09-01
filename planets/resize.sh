#!/bin/bash

for img in *
do
    convert -resize 20% $img $img
done


