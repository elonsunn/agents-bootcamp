FROM python:3.13-slim

WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy project source
COPY . .

# Default: run the language-mentor notebook as a script via nbconvert
# Override CMD to run tests: docker run <image> pytest tests/
CMD ["jupyter", "nbconvert", "--to", "script", "--execute", \
     "language-mentor/language-mentor-v0.4.ipynb"]
