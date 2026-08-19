# 🤖 AI Customer Support Ticket Analyzer

An AI-powered IT support ticket analysis and automation tool designed to help support teams classify tickets, identify root causes, recommend actions, surface relevant Microsoft Learn resources, and generate customer-ready responses.

**Built by Zeeshan Hassan**  
Python • AI Automation • Microsoft 365

## 🚀 Live Demo

👉 **[Launch the Live Application](https://zeesh-cyber-ai-customer-support-ticket-analyzer-app-jxzvcv.streamlit.app/)**

Try the live application to analyze an IT support ticket, classify the issue, receive troubleshooting recommendations, and find relevant Microsoft Learn resources.

---

## 🚀 Overview

The AI Customer Support Ticket Analyzer transforms an unstructured IT support ticket into a structured support assessment.

The application analyzes the ticket and provides:

- Ticket category
- Issue type
- Sentiment
- Priority
- Root cause
- Recommended action
- Relevant Microsoft Learn resources
- Customer response
- Automation quality score
- Human-review requirement

The goal is to demonstrate how AI-assisted automation can improve the speed, consistency, and quality of IT support operations.

---

## ✨ Key Features

### 🎫 Automated Ticket Classification

Automatically identifies the appropriate:

- Category
- Issue type
- Priority
- Sentiment

### 🔎 Root Cause Analysis

Identifies the likely root cause based on the ticket description and provides a structured troubleshooting assessment.

### 🛠️ Recommended Action

Provides a suggested next step for the support engineer while keeping human review in the workflow.

### 📚 Microsoft Knowledge Base Integration

The application connects ticket classifications with relevant Microsoft Learn resources.

For example:

**Entra ID → Password / MFA**

can return relevant Microsoft documentation for:

- Microsoft Entra sign-in troubleshooting
- MFA sign-in investigations
- Azure/Microsoft Entra MFA troubleshooting

### 💬 Customer Response Generation

Generates a professional customer-facing response based on the ticket analysis.

### ⚙️ Automation Assessment

Provides:

- Quality score
- Human-review requirement

This helps distinguish between cases that may be suitable for automation and cases that should receive human oversight.

---

## 🏗️ Application Architecture

```text
Customer Support Ticket
          │
          ▼
      app.py
          │
          ▼
ticket_automation.py
          │
          ├── Category
          ├── Issue Type
          ├── Sentiment
          ├── Priority
          ├── Root Cause
          ├── Recommended Action
          ├── Customer Response
          └── Automation Assessment
          │
          ▼
   knowledge_base.py
          │
          ▼
   Microsoft Learn Resources
          │
          ▼
     Streamlit UI
