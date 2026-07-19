# 💬 Voice of Customer AI Agent

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

(Add architecture image)

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

## Screenshots

(Add dashboard image)

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