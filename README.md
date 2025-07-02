# Transformer Models Analysis: BERT, GPT-2, and Llama

A comprehensive exploration and visualization of transformer model architectures, embeddings, and attention mechanisms.

## 📋 Overview

This project provides an in-depth analysis of three major transformer architectures:
- **BERT** (Bidirectional Encoder Representations from Transformers)
- **GPT-2** (Generative Pre-trained Transformer 2)
- **Llama** (Large Language Model Meta AI)

The notebook demonstrates how these models process text, visualizes their attention patterns, and compares their internal representations.

## 🎯 Features

- **Embedding Analysis**
  - Word embeddings exploration
  - Position embeddings visualization
  - Token type embeddings (for BERT)
  - Embedding dimension comparisons across models

- **Attention Visualization**
  - Layer-wise attention pattern visualization
  - Head-specific attention analysis
  - Interactive heatmaps showing token relationships

- **Model Comparison**
  - Side-by-side comparison of BERT vs GPT-2 vs Llama
  - Architecture differences exploration
  - Output representation analysis

- **Practical Demonstrations**
  - Text processing pipelines
  - Hidden state extraction
  - Sentence embedding generation (using Sentence-BERT)

## 🛠️ Installation

### Prerequisites
- Python 3.8+
- CUDA-capable GPU (recommended for faster processing)

### Setup

1. Clone the repository:
```bash
git clone <repository-url>
cd <repository-name>
```

2. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install required packages:
```bash
pip install -r requirements.txt
```

### Required Libraries
```txt
torch>=1.9.0
transformers>=4.20.0
numpy>=1.21.0
pandas>=1.3.0
matplotlib>=3.4.0
seaborn>=0.11.0
scikit-learn>=0.24.0
jupyter>=1.0.0
ipywidgets>=7.6.0
```

## 📁 Project Structure

```
NLP Project/
└── Transformers/
    ├── Transformers_BERT_SBERT_GPT_2_Llama.ipynb  # Main notebook
    ├── data/
    │   └── data_clean_finance.pkl                  # Sample finance data
    ├── README.md                                    # This file
    └── requirements.txt                             # Dependencies
```

## 🚀 Usage

### Running the Notebook

1. Start Jupyter Notebook:
```bash
jupyter notebook
```

2. Navigate to `Transformers_BERT_SBERT_GPT_2_Llama.ipynb`

3. Run cells sequentially for the complete analysis

### Key Sections

#### Part 1: BERT Analysis
- Loading pre-trained BERT models
- Extracting and analyzing embeddings
- Visualizing attention patterns
- Sentence-BERT implementation

#### Part 2: GPT-2 & Llama Comparison
- Loading generative models
- Comparing architectures with BERT
- Analyzing directional vs bidirectional attention
- Performance benchmarking

### Example Code Snippets

**Loading a BERT model:**
```python
from transformers import BertModel, BertTokenizer

tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
model = BertModel.from_pretrained('bert-base-uncased')
```

**Extracting attention weights:**
```python
outputs = model(input_ids, output_attentions=True)
attention_weights = outputs.attentions
```

**Visualizing attention patterns:**
```python
# The notebook includes custom visualization functions
plot_attention_heatmap(attention_weights, tokens)
```

## 📊 Visualizations

The notebook generates several types of visualizations:

1. **Embedding Space Plots**
   - 2D/3D representations of word embeddings
   - Position embedding patterns

2. **Attention Heatmaps**
   - Token-to-token attention scores
   - Layer-wise attention evolution
   - Head-specific attention patterns

3. **Model Comparison Charts**
   - Architecture parameter comparisons
   - Performance metrics visualization

## 🔍 Key Findings

- **BERT**: Bidirectional attention allows for better context understanding
- **GPT-2**: Unidirectional attention suitable for generation tasks
- **Llama**: Optimized architecture with improved efficiency
- **Embedding Insights**: Each model uses different strategies for position encoding

## 📚 Resources

- [BERT Paper](https://arxiv.org/abs/1810.04805)
- [GPT-2 Paper](https://openai.com/blog/better-language-models/)
- [Llama Documentation](https://github.com/facebookresearch/llama)
- [Hugging Face Transformers](https://huggingface.co/docs/transformers/index)

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request. For major changes, please open an issue first to discuss what you would like to change.

## 📝 License

This project is licensed under the MIT License.

---

**Note**: This project is for educational and research purposes. Make sure to comply with the respective model licenses when using them in production.
