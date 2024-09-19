# 设置变量
VIDEO_PATH="videos/video07.mp4"
OUTPUT_DIR="data_resize/video07"
TIME_SEGMENT=1800  # 30分钟，单位为秒
FRAME_COUNT=1  # 初始化图像计数器

# 获取视频总时长
DURATION=$(ffprobe -v error -show_entries format=duration -of default=noprint_wrappers=1:nokey=1 $VIDEO_PATH)
SEGMENT_FRAMES=1800  # 每段的帧数，假设视频是1fps

# 计算需要多少段
SEGMENTS=$(echo "scale=0; $DURATION / $TIME_SEGMENT" | bc)

# 处理每一段
for (( i=0; i<$SEGMENTS; i++ ))
do
    START_TIME=$(echo "$i * $TIME_SEGMENT" | bc)
    END_TIME=$(echo "$START_TIME + $TIME_SEGMENT" | bc)
    if [ $i -eq $(($SEGMENTS - 1)) ]; then
        # 最后一段使用视频的实际结束时间
        END_TIME=$DURATION
    fi
    
    # 生成图像序列，从上一段的最后一帧开始编号
    ffmpeg -ss $START_TIME -i $VIDEO_PATH -t $(echo "$END_TIME - $START_TIME" | bc) -vf "scale=250:250,fps=1" -r 1 -q:v 2 -f image2 -start_number $((FRAME_COUNT)) $OUTPUT_DIR/video07-%d.png
    
    # 更新帧计数器
    FRAME_COUNT=$(echo "$FRAME_COUNT + $SEGMENT_FRAMES" | bc)
done


# 设置变量
VIDEO_PATH="videos/video03.mp4"
OUTPUT_DIR="data_resize/video03"
TIME_SEGMENT=1800  # 30分钟，单位为秒
FRAME_COUNT=1  # 初始化图像计数器

# 获取视频总时长
DURATION=$(ffprobe -v error -show_entries format=duration -of default=noprint_wrappers=1:nokey=1 $VIDEO_PATH)
SEGMENT_FRAMES=1800  # 每段的帧数，假设视频是1fps

# 计算需要多少段
SEGMENTS=$(echo "scale=0; $DURATION / $TIME_SEGMENT" | bc)

# 处理每一段
for (( i=0; i<$SEGMENTS; i++ ))
do
    START_TIME=$(echo "$i * $TIME_SEGMENT" | bc)
    END_TIME=$(echo "$START_TIME + $TIME_SEGMENT" | bc)
    if [ $i -eq $(($SEGMENTS - 1)) ]; then
        # 最后一段使用视频的实际结束时间
        END_TIME=$DURATION
    fi
    
    # 生成图像序列，从上一段的最后一帧开始编号
    ffmpeg -ss $START_TIME -i $VIDEO_PATH -t $(echo "$END_TIME - $START_TIME" | bc) -vf "scale=250:250,fps=1" -r 1 -q:v 2 -f image2 -start_number $((FRAME_COUNT)) $OUTPUT_DIR/video03-%d.png
    
    # 更新帧计数器
    FRAME_COUNT=$(echo "$FRAME_COUNT + $SEGMENT_FRAMES" | bc)
done


