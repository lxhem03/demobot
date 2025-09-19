FROM python:3.10.6
RUN mkdir /bot && chmod 777 /bot
WORKDIR /bot
ENV DEBIAN_FRONTEND=noninteractive
RUN apt -qq update && \
    apt -qq install -y git wget pv jq python3-dev mediainfo neofetch && \
    apt-get install wget -y -f && \
    apt-get install fontconfig -y -f

# Install latest FFmpeg static build with support for libx264, libx265, VP9 (libvpx), AV1 (libaom, librav1e, libsvtav1), and other common codecs
RUN wget https://johnvansickle.com/ffmpeg/releases/ffmpeg-release-amd64-static.tar.xz && \
    tar xJf ffmpeg-release-amd64-static.tar.xz && \
    mv ffmpeg-*/ffmpeg /usr/local/bin/ffmpeg && \
    mv ffmpeg-*/ffprobe /usr/local/bin/ffprobe && \
    rm -rf ffmpeg-* && \
    rm ffmpeg-release-amd64-static.tar.xz

COPY . .
RUN pip3 install -r requirements.txt
CMD ["bash", "run.sh"]
