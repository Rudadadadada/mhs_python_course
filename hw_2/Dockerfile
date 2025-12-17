FROM python:3.12-slim

RUN apt-get update && \
    DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends \
        texlive-latex-base texlive-latex-recommended texlive-fonts-recommended \
        texlive-latex-extra && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

WORKDIR /app
COPY pyproject.toml ./
COPY hw_2 ./hw_2

RUN pip install --no-cache-dir .

WORKDIR /app/hw_2
CMD ["python", "generate_artifacts.py", "--pdf"]
 