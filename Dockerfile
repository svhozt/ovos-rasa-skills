ARG TAG=alpha
FROM smartgic/ovos-skill-base:${TAG}

ARG BUILD_DATE=07/12/2023
ARG VERSION=2.5

LABEL org.opencontainers.image.title="Rasa Skill"
LABEL org.opencontainers.image.description="An OVOS skill for integrating with Rasa using Socket.IO"
LABEL org.opencontainers.image.version=${VERSION}
LABEL org.opencontainers.image.created=${BUILD_DATE}
LABEL org.opencontainers.image.documentation="https://openvoiceos.github.io/community-docs"
LABEL org.opencontainers.image.source="https://github.com/OpenVoiceOS/ovos-docker"
LABEL org.opencontainers.image.vendor="Open Voice OS"

ARG ALPHA=false

RUN if [ "${ALPHA}" == "true" ]; then \
    pip3 install git+https://github.com/ravindukathri/ovos-rasa-skill.git; \
    fi \
    && rm -rf "${HOME}/.cache"

ENTRYPOINT ["ovos-skill-launcher", "ovos-rasa-skill.ravindukathri"]
