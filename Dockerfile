FROM python:3.11-slim-buster

RUN apt-get update && apt-get -y upgrade

COPY requirements.txt .
RUN pip install --upgrade pip && pip install --no-cache-dir  --upgrade -r requirements.txt && pip cache purge

# AS ROOT: pick up user & grp ids
ARG USER_ID
ARG GROUP_ID
ARG USER_NAME

RUN addgroup --gid ${GROUP_ID} ${USER_NAME}
RUN echo "Adding ${USER_NAME}"
RUN adduser --disabled-password --gecos '' --uid $USER_ID --gid $GROUP_ID ${USER_NAME}

# ----------------
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Switch to USER
USER ${USER_NAME}

RUN mkdir -p /home/${USER_NAME}/app && chown ${USER_ID}:${GROUP_ID} /home/${USER_NAME}/app 
WORKDIR /home/${USER_NAME}/app

ENV PATH=/home/"${USER_NAME}"/.local/bin:$PATH
RUN echo $PATH
RUN echo $(pwd)

COPY ./app /home/${USER_NAME}/app
# RUN pwd
CMD ["uvicorn", "app:ep_app ", "--host", "0.0.0.0", "--port", "80"]
