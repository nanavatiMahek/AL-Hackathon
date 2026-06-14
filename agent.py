from openai import OpenAI
from dotenv import load_dotenv
import os
import PyPDF2

load_dotenv()

client = OpenAI(
    base_url="https://models.inference.ai.azure.com",
    api_key=os.getenv("GITHUB_TOKEN")
)

def extract_pdf_text(pdf_path, max_chars=2000):
    try:
        with open(pdf_path, "rb") as f:
            reader = PyPDF2.PdfReader(f)
            text = ""
            for page in reader.pages:
                text += page.extract_text() or ""
                if len(text) >= max_chars:
                    break
        return text[:max_chars]
    except:
        return ""

# old		
rti_act        = extract_pdf_text("rti_act.pdf")
consumer_act   = extract_pdf_text("consumer_act.pdf")
rti_fees       = extract_pdf_text("rti_fees.pdf")

#  new
constitution   = extract_pdf_text("CONSTITUTION OF INDIA.pdf")
cpio           = extract_pdf_text("CPIO.pdf")
rti_misuse     = extract_pdf_text("rti misue order.pdf")
rera           = extract_pdf_text("the_real_estate_(regulation_and_development)_act,_2016.pdf")

SYSTEM_PROMPT = f"""
You are LegalEagle Lite — an AI agent that helps Indian citizens file RTI requests and consumer complaints.

You have access to these legal documents:

=== RTI ACT 2005 ===
{rti_act}

=== CONSUMER PROTECTION ACT 2019 ===
{consumer_act}

=== RTI FEE RULES 2005 ===
{rti_fees}

=== CONSTITUTION OF INDIA ===
{constitution}

=== CPIO GUIDELINES ===
{cpio}

=== RTI MISUSE ORDER ===
{rti_misuse}

=== RERA 2016 (Real Estate Regulation & Development Act) ===
{rera}

Your job:
1. Listen to the user's problem carefully
2. Identify if it is an RTI case, consumer complaint, RERA complaint, or constitutional rights issue
3. Ask ONE clarifying question at a time if needed
4. Once you have enough info generate a complete ready-to-submit formal application letter
5. Cite exact sections from the relevant law
6. Tell the user exact fee to pay and where to submit
7. Explain next steps in simple language

When to use each document:
- RTI ACT + RTI FEES + CPIO: for information requests from government bodies
- RTI MISUSE ORDER: if the user's RTI was rejected or misused by a CPIO
- CONSUMER PROTECTION ACT: for complaints against companies, services, products
- RERA: for complaints against builders, developers, housing projects
- CONSTITUTION: for fundamental rights violations (Article 19, 21, 32 etc.)

Always respond in simple English or Hindi if user prefers.
For RTI: application fee is Rs 10, additional pages Rs 2 each, BPL applicants are exempt.
Never give false legal advice. For complex cases recommend a lawyer.
"""

def chat_with_agent(messages):
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "system", "content": SYSTEM_PROMPT}] + messages,
        temperature=0.7,
        max_tokens=1000
    )
    return response.choices[0].message.content