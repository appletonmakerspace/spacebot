# Usage:
# docker build . --network=host -t appletonmakerspace/spacebot
# docker run --network=host appletonmakerspace/spacebot
#
# The "onbuild" image automatically runs pip install -r requirements.txt for us
FROM python:3.6-onbuild
WORKDIR /usr/src/app
COPY . /usr/src/app
ENTRYPOINT python run.py
EXPOSE 5000
