FROM ghcr.io/mamba-org/micromamba:git-8e479d6-bookworm

COPY --chown=$MAMBA_USER:$MAMBA_USER env.yml /tmp/env.yml

RUN micromamba install -y -n base -f /tmp/env.yml && \
    micromamba clean --all --yes

WORKDIR /proj

COPY ./app ./app

EXPOSE 3000

CMD ["fastapi", "run", "app/main.py", "--port", "3000"]
