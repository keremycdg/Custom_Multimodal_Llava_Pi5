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

