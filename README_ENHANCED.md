# MarkItDown

[![PyPI](https://img.shields.io/pypi/v/markitdown.svg)](https://pypi.org/project/markitdown/)
![PyPI - Downloads](https://img.shields.io/pypi/dd/markitdown)
[![Built by AutoGen Team](https://img.shields.io/badge/Built%20by-AutoGen%20Team-blue)](https://github.com/microsoft/autogen)

> [!TIP]
> MarkItDown now offers an MCP (Model Context Protocol) server for integration with LLM applications like Claude Desktop. See [markitdown-mcp](https://github.com/microsoft/markitdown/tree/main/packages/markitdown-mcp) for more information.

MarkItDown is a lightweight Python utility for converting various files to Markdown for use with LLMs and related text analysis pipelines. With enhanced multi-language support, it preserves important document structure and content as Markdown, including headings, lists, tables, links, and proper character encoding for international documents.

## ✨ Key Features

- **🔄 Multi-format Support**: PDF, PowerPoint, Word, Excel, Images, Audio, HTML, and more
- **🌍 Enhanced International Support**: Improved encoding detection for German, European, and other languages
- **📝 Smart Structure Preservation**: Maintains document hierarchy, formatting, and semantic structure
- **🔌 Extensible Plugin System**: Support for 3rd-party plugins and custom converters
- **🐳 Docker Ready**: Containerized deployment support
- **🤖 LLM Optimized**: Output designed for consumption by language models

## Supported File Formats

MarkItDown currently supports conversion from:

- **Documents**: PDF, Word (.docx), PowerPoint (.pptx), Excel (.xlsx, .xls)
- **Images**: JPEG, PNG, GIF, BMP (with EXIF metadata and OCR)
- **Audio**: WAV, MP3 (with metadata and speech transcription)
- **Web**: HTML, EPub, YouTube URLs
- **Data**: CSV, JSON, XML
- **Archives**: ZIP files (iterates over contents)
- **Email**: Outlook messages (.msg)

## Why Markdown?

Markdown is extremely close to plain text with minimal markup, while still providing a way to represent important document structure. Mainstream LLMs natively understand Markdown and often incorporate it into responses unprompted, suggesting extensive training on Markdown-formatted text. As a bonus, Markdown conventions are highly token-efficient.

## 🚀 Quick Start

### Installation

```bash
# Install with all optional dependencies
pip install 'markitdown[all]'

# Or install from source
git clone https://github.com/microsoft/markitdown.git
cd markitdown
pip install -e 'packages/markitdown[all]'
```

### Basic Usage

**Command Line:**
```bash
# Convert to stdout
markitdown document.pdf

# Save to file
markitdown document.pdf -o output.md

# Pipe content
cat document.pdf | markitdown
```

**Python API:**
```python
from markitdown import MarkItDown

md = MarkItDown()
result = md.convert("document.pdf")
print(result.text_content)
```

## 📋 Prerequisites

- **Python**: 3.10 or higher
- **Virtual Environment**: Recommended to avoid dependency conflicts

### Setting up Virtual Environment

**Standard Python:**
```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\\Scripts\\activate
```

**Using uv:**
```bash
uv venv --python=3.12 .venv
source .venv/bin/activate
```

**Using Conda:**
```bash
conda create -n markitdown python=3.12
conda activate markitdown
```

## 🔧 Advanced Configuration

### Optional Dependencies

Install only what you need:

```bash
# PDF support only
pip install 'markitdown[pdf]'

# Multiple formats
pip install 'markitdown[pdf,docx,pptx]'

# All available options
pip install 'markitdown[all]'
```

Available dependency groups:
- `[pdf]` - PDF files
- `[docx]` - Word documents
- `[pptx]` - PowerPoint presentations
- `[xlsx]` - Excel files
- `[xls]` - Legacy Excel files
- `[outlook]` - Outlook messages
- `[az-doc-intel]` - Azure Document Intelligence
- `[audio-transcription]` - Audio file transcription
- `[youtube-transcription]` - YouTube video transcription

### Enhanced International Support

MarkItDown includes improved encoding detection for international documents, particularly:

- **German documents**: Automatic handling of ä, ö, ü, ß characters
- **European languages**: Enhanced Latin-1, CP1252, ISO-8859-1 support
- **Smart fallback**: Multiple encoding attempts with intelligent selection

### Plugin System

**List available plugins:**
```bash
markitdown --list-plugins
```

**Enable plugins:**
```bash
markitdown --use-plugins document.pdf
```

**Find community plugins:** Search GitHub for `#markitdown-plugin`

### Azure Document Intelligence

For enhanced PDF processing:

```bash
markitdown document.pdf -d -e "<your_document_intelligence_endpoint>"
```

**Python API with Document Intelligence:**
```python
from markitdown import MarkItDown

md = MarkItDown(docintel_endpoint="<your_endpoint>")
result = md.convert("document.pdf")
```

### LLM Integration for Images

Use Large Language Models for enhanced image descriptions:

```python
from markitdown import MarkItDown
from openai import OpenAI

client = OpenAI()
md = MarkItDown(
    llm_client=client, 
    llm_model="gpt-4o", 
    llm_prompt="Describe this image in detail"
)
result = md.convert("image.jpg")
```

## 🐳 Docker Usage

```bash
# Build image
docker build -t markitdown:latest .

# Convert files
docker run --rm -i markitdown:latest < document.pdf > output.md
```

## 🏗️ Architecture

MarkItDown uses a modular converter architecture:

- **Core Engine**: Central conversion orchestration
- **Format Converters**: Specialized handlers for each file type
- **Encoding Detection**: Multi-pass character encoding resolution
- **Plugin System**: Extensible third-party integration
- **Stream Processing**: Memory-efficient file handling

## 🧪 Development

### Running Tests

```bash
cd packages/markitdown
pip install hatch
hatch shell
hatch test
```

### Code Quality

```bash
# Run pre-commit checks
pre-commit run --all-files
```

### Creating Plugins

See `packages/markitdown-sample-plugin` for plugin development examples.

## 🤝 Contributing

We welcome contributions! Please see our [Contributing Guidelines](CONTRIBUTING.md) for details.

**Quick contribution areas:**
- 🐛 [Bug fixes](https://github.com/microsoft/markitdown/issues?q=is%3Aissue+is%3Aopen+label%3A%22open+for+contribution%22)
- 📝 [Documentation improvements](https://github.com/microsoft/markitdown/pulls?q=is%3Apr+is%3Aopen+label%3A%22open+for+reviewing%22)
- 🔌 Third-party plugins
- 🌍 International language support

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🔒 Security

For security concerns, please see our [Security Policy](SECURITY.md).

## 📞 Support

- 📖 [Documentation](https://github.com/microsoft/markitdown)
- 🐛 [Issue Tracker](https://github.com/microsoft/markitdown/issues)
- 💬 [Discussions](https://github.com/microsoft/markitdown/discussions)

---

**Built with ❤️ by the Microsoft AutoGen Team**