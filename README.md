# Test File Detector Advance

Test File Detector Advance is a tool that scans project directories and automatically detects test files based on common naming patterns and folder structures. It helps developers quickly identify and organize test files in large codebases.

## 🚀 Features

- Scans directories recursively
- Detects test files using common naming patterns
- Supports different project structures
- Helps developers separate test files from source files
- Lightweight and easy to use

## 🔍 How It Works

The tool analyzes file names and folder names to identify test files.

Common detection patterns include:

- Files starting with `test_`
- Files ending with `_test`
- Files located inside `test` or `tests` folders

Example project structure:

```
project/
│
├── src/
│   └── app.py
│
├── tests/
│   └── test_app.py
│
└── utils_test.py
```

Detected test files:

- `test_app.py`
- `utils_test.py`

## ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/monishvijai/Test-File-Detector_Advance.git
cd Test-File-Detector_Advance
```

## ▶️ Usage

Run the program:

```bash
python detector.py
```

Or scan a specific directory:

```bash
python detector.py /path/to/project
```

## 📌 Use Cases

- Codebase analysis
- Identifying test files quickly
- Project organization
- Continuous Integration (CI) pipelines
- Developer productivity tools

## 🛠 Technologies Used

- Python
- File System Operations
- Pattern Matching

## 📄 License

This project is open source and available under the MIT License.

## 👤 Author

Monish Vijai  
Tech Enthusiast | Aspiring AI Engineer
