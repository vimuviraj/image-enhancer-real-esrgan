## Dependencies and Installation

### Dependencies:
- Python >= 3.7 (Recommend to use Anaconda or Miniconda)
- PyTorch >= 1.7

### Installation:

1. **Clone the repository:**

    ```
    git clone https://github.com/xinntao/Real-ESRGAN.git
    cd Real-ESRGAN
    ```

2. **Install dependent packages:**

    ```
    pip install -r requirements.txt
    python setup.py develop
    ```

3. **Download pre-trained models: RealESRGAN_x4plus.pth**

    ```
    wget https://github.com/xinntao/Real-ESRGAN/releases/download/v0.1.0/RealESRGAN_x4plus.pth -OutFile weights/RealESRGAN_x4plus.pth
    ```
