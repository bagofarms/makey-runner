# Makey Runner

A simple infinite runner starring Makey for Maker Faire Orlando 2022. Runs at 64x64 pixels, and is intended to be displayed on an RGB LED Matrix panel.

## Running (Pun Intended)

1. Install all possible dependencies

```bash
sudo apt update
sudo apt install libsdl-gfx1.2-5 libsdl-image1.2 libsdl-kitchensink1 libsdl-mixer1.2 libsdl-sound1.2 libsdl-ttf2.0-0 libsdl1.2debian libsdl2-2.0-0 libsdl2-gfx-1.0-0 libsdl2-image-2.0-0 libsdl2-mixer-2.0-0 libsdl2-ttf-2.0-0
```

2. Clone the repository

```bash
git clone https://github.com/bagofarms/makey-runner.git
cd makey-runner
```

3. Create and activate the virtual environment

```bash
python3 -m venv venv
source /venv/bin/activate
```

4. Install requirements

```bash
pip install -r requirements.txt
```

5. Run the app

```bash
pgzrun main.py
```
