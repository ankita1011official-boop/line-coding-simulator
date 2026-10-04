# Polar & Bipolar Line Coding Simulator

A simple Streamlit application for visualizing:

- Polar NRZ-L
- Bipolar AMI

## Run locally

### 1. Open a terminal in this folder

### 2. Create a virtual environment

Windows:

```bash
python -m venv venv
```

### 3. Activate it

Windows Command Prompt:

```bash
venv\Scripts\activate
```

PowerShell:

```powershell
venv\Scripts\Activate.ps1
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

### 5. Run the app

```bash
streamlit run app.py
```

Then open the address shown by Streamlit, usually:

http://localhost:8501

## Deploy to Streamlit Community Cloud

1. Create a GitHub repository.
2. Upload `app.py` and `requirements.txt`.
3. Open Streamlit Community Cloud.
4. Select your GitHub repository.
5. Set the main file to `app.py`.
6. Deploy.

Do not upload the `venv` folder.

## Project structure

```text
line-coding-simulator/
├── app.py
├── requirements.txt
└── README.md
```
