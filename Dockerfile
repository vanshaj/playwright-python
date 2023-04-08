FROM python:3.11 AS base
WORKDIR /home/user
COPY . /home/user/
RUN  pip3 install -r requirements.txt && playwright install && playwright install-deps
RUN apt install wget && wget https://repo.maven.apache.org/maven2/io/qameta/allure/allure-commandline/2.21.0/allure-commandline-2.21.0.tgz\
 && apt install tar && tar -xvzf allure-commandline-2.21.0.tgz && mv allure-2.21.0/bin/allure /usr/local/bin/allure

FROM base AS test
CMD ["./run.sh"]