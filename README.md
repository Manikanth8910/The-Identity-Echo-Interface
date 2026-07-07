# The Identity Echo Interface

![Python](https://img.shields.io/badge/Python-3.x-blue.svg)
![Streamlit](https://img.shields.io/badge/Streamlit-Framework-FF4B4B.svg)

## 📌 Project Overview
"The Identity Echo Interface" is a frontend web application developed as part of the **MirAI School of Technology Virtual Summer Internship 2026**. Built with Streamlit, this project demonstrates rapid UI development in Python, abstracting away complex HTML/JS to focus on core data logic, user interaction, and edge-case handling.

## 🚀 Features
- **Interactive UI Shell:** A clean, responsive user interface utilizing Streamlit's native components.
- **Multi-Data Collection:** Captures user inputs (Name and Message) using streamlined text fields.
- **Conditional Action Gates:** Execution logic is strictly gated behind user triggers, ensuring data is only processed upon explicit command.
- **Robust Edge Case Handling:** Built-in form validation utilizing Python's string methods to prevent empty or whitespace-only submissions, delivering appropriate UI feedback (warnings/errors) to the user.
- **Token Cost Estimator (Advanced Feature):** Simulates LLM API context window management by calculating the character length of user messages and rendering an estimated token consumption metric (assuming 1 token ≈ 4 characters).

## 🛠️ Technology Stack
- **Language:** Python
- **Framework:** [Streamlit](https://streamlit.io/)

## 💻 Getting Started

### Prerequisites
Ensure you have Python installed, then install the required Streamlit package:
```bash
pip install streamlit
```

### Installation & Execution
1. Clone the repository:
   ```bash
   git clone https://github.com/Manikanth8910/The-Identity-Echo-Interface.git
   ```
2. Navigate into the project directory:
   ```bash
   cd The-Identity-Echo-Interface
   ```
3. Boot the local Streamlit server:
   ```bash
   streamlit run app.py
   ```
4. Access the application in your browser via the provided `Local URL` (typically `http://localhost:8501`).

---
*Developed for the MirAI School of Technology: AI Builder Track*
