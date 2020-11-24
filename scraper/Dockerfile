From ubuntu:latest
RUN apt-get update -y
RUN apt-get install python3 -y
RUN apt-get install python3-pip -y
RUN apt-get install cron -y
RUN apt-get install nano -y
RUN mkdir app
COPY ["requirements.txt","/app"]
WORKDIR app
RUN pip3 install -r requirements.txt
RUN (crontab -l 2>/dev/null; echo "*/30 6 * * * cd /app/auto &&  ./news_feed.sh") | crontab -
