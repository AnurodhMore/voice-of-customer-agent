# 💬 Voice of Customer AI Agent

## Screenshots

<img width="1466" height="786" alt="Screenshot 2026-07-19 at 15 16 56" src="https://github.com/user-attachments/assets/2c3b85b5-2c13-4292-80b1-a85b485f9294" />

<img width="1466" height="786" alt="Screenshot 2026-07-19 at 15 17 43" src="https://github.com/user-attachments/assets/4729113c-d076-44cf-be06-d727adc0d3c4" />

<img width="1466" height="786" alt="Screenshot 2026-07-19 at 15 20 19" src="https://github.com/user-attachments/assets/93d5e7f9-657f-4ab3-bcc5-701d5891a1db" />

<img width="1466" height="786" alt="Screenshot 2026-07-19 at 15 20 59" src="https://github.com/user-attachments/assets/fdff92d7-2d63-4bf3-a547-9cf7aad9bd97" />

---

## Overview

Analyze thousands of customer reviews using AI and automatically discover product pain points, prioritize issues, extract feature requests, and generate product-ready user stories.

---

## Problem Statement

Product Managers receive thousands of customer reviews every month.

Reading each review manually is impossible.

Important issues often remain unnoticed.

Feature requests are scattered.

Engineering teams struggle to prioritize work.

This project solves that problem using AI.

---

## Solution

The Voice of Customer AI Agent automatically:

✓ Reads CSV customer reviews

✓ Categorizes issues

✓ Detects feature requests

✓ Prioritizes issues

✓ Generates User Stories

✓ Provides AI Product Manager recommendations

---

## Architecture
 CSV Reviews

↓

Streamlit

↓

Issue Analyzer

↓

Feature Detector

↓

Priority Engine

↓

LLM (Gemini Flash)
↓

AI Product Manager Insights

↓

Dashboard

## Architecture Diagram

                ┌───────────────────────────┐
                │      Streamlit UI         │
                └─────────────┬─────────────┘
                              │
                     Upload CSV / Excel
                              │
                              ▼
                ┌───────────────────────────┐
                │      Data Processing      │
                │         (Pandas)          │
                └─────────────┬─────────────┘
                              │
             Sentiment • Feature Detection • Prioritization
                              │
                              ▼
                ┌───────────────────────────┐
                │      Google Gemini API    │
                │      (Gemini Flash)       │
                └─────────────┬─────────────┘
                              │
                              ▼
                ┌───────────────────────────┐
                │ AI User Stories           │
                │ Executive Summary         │
                │ Product Insights          │
                └───────────────────────────┘

---

## Features

✓ Upload CSV

✓ Upload Excel

✓ Sentiment Summary

✓ Priority Matrix

✓ AI Insights

✓ Feature Detection

✓ User Story Generator

✓ Export CSV

---
## Dashboard

---
## Tech Stack

| Layer           | Technology  |
| --------------- | ----------  |
| Frontend        | Streamlit   |
| Language        | Python      |
| AI              | Gemini API  |
| LLM             | Gemini Flash|
| Data            | Pandas      |
| Visualization   | Plotly      |
| Version Control | Git         |

---
## Folder Structure

voice-of-customer-agent/

app.py

services/

agents/

utils/

data/

README.md

requirements.txt

---
# How to Run

---



## Installation

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/AnurodhMore/voice-of-customer-agent.git
cd voice-of-customer-agent
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Configure your Gemini API Key

Create a `.env` file in the project root:

```env
GEMINI_API_KEY=your_gemini_api_key
```

You can generate a free API key from **Google AI Studio**:
https://aistudio.google.com/

### 4. Run the application

```bash
streamlit run app.py
```

---

## Future Roadmap

Upcoming Features

Multi-language analysis

RAG support

Jira integration

Slack notifications

Cloud deployment

---
