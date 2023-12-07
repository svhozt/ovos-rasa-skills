## Code in the skill compose file

ovos_rasa_skill:  
    <<: *podman
    container_name: ovos_rasa_skill
    hostname: ovos_rasa_skill
    restart: unless-stopped
    build:
      context: ../skills/rasa-skill
      dockerfile: Dockerfile
    logging: *default-logging
    pull_policy: $PULL_POLICY
    environment:
      TZ: $TZ
    network_mode: host
    volumes:
      - ${OVOS_CONFIG_FOLDER}:/home/${OVOS_USER}/.config/mycroft
      - ${TMP_FOLDER}:/tmp/mycroft
    depends_on:
      ovos_core:
        condition: service_started
