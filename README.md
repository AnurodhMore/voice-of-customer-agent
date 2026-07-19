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

LLM (Ollama)

↓

AI Product Manager Insights

↓

Dashboard

## Architecture Diagram

Customer Reviews CSV

        │

        ▼

 Review Analyzer

        │

 ┌──────────────┐
 │ Sentiment    │
 │ Pain Points  │
 │ Features     │
 │ User Stories │
 └──────────────┘

        │

        ▼

   Dashboard

        │

 Streamlit

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

| Layer           | Technology |
| --------------- | ---------- |
| Frontend        | Streamlit  |
| Language        | Python     |
| AI              | Ollama     |
| LLM             | Llama 3.2  |
| Data            | Pandas     |
| Version Control | Git        |

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

git clone

cd voice-of-customer-agent

pip install -r requirements.txt

ollama run llama3.2

streamlit run app.py

---

## Future Roadmap

Upcoming Features

Multi-language analysis

RAG support

Jira integration

Slack notifications

Cloud deployment

---
