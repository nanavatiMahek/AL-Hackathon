# Verity ⚖️

**Know Your Rights. File Your Complaint. Get Justice.**

Verity is an AI-powered legal assistant designed to help Indian citizens exercise their constitutional and statutory rights. It provides guidance on filing RTI requests, consumer complaints, property disputes, and more—completely free, with no data storage.

---

## 🎯 Features

### 1. **RTI Request Filing**
- Guide users through Right to Information Act (RTI) 2005 requests
- Extract relevant sections from the RTI Act
- Calculate exact application fees (₹10 base + ₹2 per additional page)
- Handle BPL applicant exemptions
- Provide CPIO (Chief Public Information Officer) guidelines

### 2. **Consumer Complaint Assistance**
- Help file complaints under Consumer Protection Act 2019
- Address product defects, poor services, and unfair practices
- Generate formal complaint letters ready for submission

### 3. **Property & RERA Disputes**
- Guide users through Real Estate Regulation and Development Act (RERA) 2016
- Address builder misconduct, project delays, and construction defects
- Reference relevant RERA sections

### 4. **Workplace & Harassment Issues**
- Address sexual harassment and misconduct (POSH - Prevention of Sexual Harassment)
- Workplace rights guidance under constitutional provisions

### 5. **Banking & UPI Fraud**
- Assistance with failed transactions
- Guidance on fraud reporting and resolution

### 6. **Online Fraud & Scams**
- Support for scam victims
- Information on complaint mechanisms

### 7. **Constitutional Rights**
- Reference to Articles 19, 21, 32 for fundamental rights violations
- Access to Constitution of India content

---

## 🛠️ Tech Stack

- **Frontend**: Streamlit (Python web framework)
- **AI Model**: GPT-4o-mini via GitHub Models (Azure inference)
- **PDF Processing**: PyPDF2
- **Environment Management**: python-dotenv
- **API Client**: OpenAI Python library

---

## 📋 Legal Documents Embedded

The agent is trained on:
- **RTI Act 2005** - Right to Information framework
- **Consumer Protection Act 2019** - Consumer rights and remedies
- **Real Estate Regulation & Development Act (RERA) 2016** - Property disputes
- **Constitution of India** - Fundamental and constitutional rights
- **CPIO Guidelines** - Chief Public Information Officer procedures
- **RTI Misuse Prevention Order** - Protection against RTI abuse

---

## ⚙️ Setup & Installation

### Prerequisites
- Python 3.8 or higher
- GitHub Copilot token (for API access)

### Installation Steps

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd Mahke-hackathon-code
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**
   Create a `.env` file in the root directory:
   ```
   GITHUB_TOKEN=your_github_token_here
   ```

5. **Run the application**
   ```bash
   streamlit run app.py
   ```

   The app will be available at `http://localhost:8501`

---

## 📖 How It Works

### User Flow

1. **Welcome Screen**
   - User sees the Verity interface with quick-select buttons for common issues
   - Options include: RTI requests, consumer complaints, property disputes, workplace issues, fraud reporting, etc.

2. **Interactive Chat**
   - User describes their problem in natural language
   - AI agent asks clarifying questions to understand the issue better
   - Agent identifies the applicable law (RTI Act, Consumer Act, RERA, etc.)

3. **Legal Analysis**
   - Agent references relevant legal sections from embedded documents
   - Generates a formal, ready-to-submit application letter
   - Provides exact fees and submission procedures

4. **Guidance & Next Steps**
   - Clear instructions on where and how to submit the complaint
   - Timeline expectations
   - Contact details for relevant authorities

### Technical Flow

```
User Input (Streamlit Chat)
         ↓
    Agent Processing
         ↓
System Prompt + Legal Documents + Chat History
         ↓
OpenAI GPT-4o-mini (via GitHub Models)
         ↓
Response Generation
         ↓
Formatted Output to User
```

---

## 🔒 Privacy & Data Security

- **No data storage**: All conversations are ephemeral and not stored on our servers
- **No cookies**: The app respects user privacy completely
- **BPL friendly**: Free for all, with special provisions for Below Poverty Line applicants
- **Secure**: Uses HTTPS and secure API endpoints

---

## 🚀 Usage Examples

### Example 1: Filing an RTI Request
```
User: "I want to know how much money our local municipality spent on road repairs last year"
Verity: Identifies RTI case → Asks for municipality name → Generates RTI application → Shows fee (₹10) → Provides CPIO contact
```

### Example 2: Consumer Complaint
```
User: "I bought a phone that stopped working after 2 weeks"
Verity: Identifies consumer complaint → Asks for purchase date and warranty info → Generates complaint letter → References Consumer Protection Act 2019
```

### Example 3: RERA Property Dispute
```
User: "My builder hasn't completed my apartment on the promised date"
Verity: Identifies RERA complaint → Asks for project details → Generates RERA complaint → References relevant RERA sections
```

---

## ⚖️ Legal Disclaimer

**Verity is an educational tool, not a substitute for professional legal advice.**

- This AI assistant provides general legal guidance based on Indian laws
- For complex cases, consulting a qualified lawyer is recommended
- Users are responsible for accuracy of information they provide
- The application is provided as-is without any warranties

---

## 👥 Project Structure

```
.
├── app.py                           # Main Streamlit application
├── hanny code/
│   ├── agent.py                     # AI agent logic & system prompts
│   └── api.py                       # API utilities
├── requirements.txt                 # Python dependencies
├── .env                             # Environment variables (not in repo)
├── *.pdf                            # Legal document PDFs
└── README.md                        # This file
```

### Key Files

- **app.py**: Streamlit UI with custom styling, chat interface, and quick-select buttons
- **agent.py**: OpenAI integration, PDF text extraction, system prompts with legal knowledge
- **requirements.txt**: Lists all Python dependencies

---

## 📚 Dependencies

| Package | Purpose |
|---------|---------|
| `streamlit` | Web framework for the UI |
| `openai` | OpenAI API client |
| `python-dotenv` | Load environment variables |
| `PyPDF2` | Extract text from PDF documents |

---

## 🎨 UI Features

- **Dark theme** with gold accents (⚖️ scales of justice color scheme)
- **Responsive design** - works on desktop, tablet, and mobile
- **Quick-select chips** for common legal issues
- **Real-time chat interface** with AI responses
- **Custom avatars** for user and bot messages
- **Smooth animations** and hover effects

---

## 🔧 Configuration

### Adjusting Model Parameters

In `hanny code/agent.py`, you can modify:
- `temperature=0.7` - Adjust creativity vs. consistency
- `max_tokens=1000` - Maximum response length
- `model="gpt-4o-mini"` - Switch to different OpenAI models

### Adding More Legal Documents

To add more legal references:
1. Add the PDF to the root directory
2. Extract text in `agent.py` using `extract_pdf_text()`
3. Include in `SYSTEM_PROMPT`

---

## 🤝 Contributing

Contributions are welcome! Areas for improvement:
- Add support for more Indian laws
- Improve PDF extraction accuracy
- Multi-language support
- Better handling of special cases
- Extended legal document coverage

---

## 📝 License

This project is designed for public good and educational purposes. Specify your license here.

---

## 📧 Support & Feedback

For issues, suggestions, or feedback, please open an issue in the repository.

---

## 🙏 Acknowledgments

- Built during **Mahke Hackathon**
- Powered by **GitHub Models** and **OpenAI**
- Dedicated to making justice more accessible for all Indian citizens

---

**Last Updated**: 2026-06-14  
**Version**: 1.0.0
