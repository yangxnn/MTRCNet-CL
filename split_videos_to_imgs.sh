mkdir -p data_resize/video01
ffmpeg -i videos/video01.mp4 -vf scale=250:250 -r 1 -q:v 2 -f image2 data_resize/video01/video01-%d.png
mkdir -p data_resize/video02
ffmpeg -i videos/video02.mp4 -vf scale=250:250 -r 1 -q:v 2 -f image2 data_resize/video02/video02-%d.png
mkdir -p data_resize/video03
ffmpeg -i videos/video03.mp4 -vf scale=250:250 -r 1 -q:v 2 -f image2 data_resize/video03/video03-%d.png
mkdir -p data_resize/video04
ffmpeg -i videos/video04.mp4 -vf scale=250:250 -r 1 -q:v 2 -f image2 data_resize/video04/video04-%d.png
mkdir -p data_resize/video05
ffmpeg -i videos/video05.mp4 -vf scale=250:250 -r 1 -q:v 2 -f image2 data_resize/video05/video05-%d.png
mkdir -p data_resize/video06
ffmpeg -i videos/video06.mp4 -vf scale=250:250 -r 1 -q:v 2 -f image2 data_resize/video06/video06-%d.png
mkdir -p data_resize/video07
ffmpeg -i videos/video07.mp4 -vf scale=250:250 -r 1 -q:v 2 -f image2 data_resize/video07/video07-%d.png
mkdir -p data_resize/video08
ffmpeg -i videos/video08.mp4 -vf scale=250:250 -r 1 -q:v 2 -f image2 data_resize/video08/video08-%d.png
mkdir -p data_resize/video09
ffmpeg -i videos/video09.mp4 -vf scale=250:250 -r 1 -q:v 2 -f image2 data_resize/video09/video09-%d.png
mkdir -p data_resize/video10
ffmpeg -i videos/video10.mp4 -vf scale=250:250 -r 1 -q:v 2 -f image2 data_resize/video10/video10-%d.png

