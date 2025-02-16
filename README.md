# 3dprinting
3d printing tools

## Install

- Ensure Poetry is installed
- Install dependencies with `poetry install`

## Generate test file

```bash
# create a 3d printed word - in thise case 'hello'
poetry run python text_to_stl.py
# as above but with a spike to put it into the ground
poetry run python text_to_stl_with_spike.py
```


### Notes

 The spike is a cone positioned below the text, and you can adjust its height and radius with the spike_height and spike_radius parameters.

### Fonts

#### **1. Ensure the font file exists**
Make sure the font file is available at the specified path. If you're on Linux, you can find system fonts in:
```sh
ls /usr/share/fonts/truetype/
```
On Windows, fonts are usually in `C:\Windows\Fonts\`.

#### **2. Use a full path to a font file**
Instead of `"arial.ttf"`, provide the full absolute path to a font, such as:
```python
font_path = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
```

#### **3. Try a different font**
If `arial.ttf` is missing, try using a different font that you know exists:
```python
font = ImageFont.load_default()  # Uses a built-in font
```
However, this built-in font is bitmap-based and might not scale well.

#### **4. Debug the font path**
Add the following before loading the font to verify its existence:
```python
import os
if not os.path.exists(font_path):
    raise FileNotFoundError(f"Font file not found: {font_path}")
```
If the file doesn’t exist, it will raise a clear error.

#### **5. Install missing fonts**
If you don’t have a required font installed, you can install it (on Linux):
```sh
sudo apt install fonts-dejavu
```
On macOS:
```sh
brew install font-dejavu
```

