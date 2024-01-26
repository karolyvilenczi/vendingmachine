FROM python:3.11-slim-buster


COPY requirements.txt .
RUN pip install --upgrade pip && pip install -r requirements.txt && pip cache purge

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


COPY --chown=${USER_ID}:${GROUP_ID} app/* app/
