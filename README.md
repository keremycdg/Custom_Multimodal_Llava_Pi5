# Custom_Multimodal_Llava_Pi5

wget https://huggingface.co/second-state/Llava-v1.5-7B-GGUF/resolve/main/llava-v1.5-7b-Q4_K_M.gguf \
     -O models/llava-v1.5-7b-q4_0.gguf


---

## 🧪 Getting Started

### 🔧 1. Setup Environment

```bash
python3 -m venv multimodal_llava
source multimodal_llava/bin/activate
pip install --upgrade pip
pip install llama-cpp-python --extra-index-url https://abetlen.github.io/llama-cpp-python/whl/cpu
pip install langchain langchain_community langchainhub sentence-transformers pillow


sudo apt update
sudo apt install -y build-essential cmake libopenblas-dev libomp-dev

# Start in your project folder
cd ~/Custom_Multimodal_Llava_Pi5

# 1. Clone the LLaVA C++ CLI repo
git clone https://github.com/haotian-liu/llava.cpp.git

# 2. Build the project
cd llava.cpp
mkdir build && cd build
cmake .. -DCMAKE_BUILD_TYPE=Release
cmake --build . -j$(nproc)

# 3. Create the destination folder (if not already created)
cd ~/Custom_Multimodal_Llava_Pi5
mkdir -p llava.cpp

# 4. Copy the compiled binary into your project structure
cp llava.cpp/build/bin/llava llava.cpp/llava


