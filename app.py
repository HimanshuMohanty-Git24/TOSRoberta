import streamlit as st
import pandas as pd
import torch
from transformers import AutoTokenizer, AutoModelForSequenceClassification
from utils.text_processing import extract_text_from_pdf, split_into_clauses
from utils.model_utils import predict_unfairness

# Set page title and favicon
st.set_page_config(
    page_title="Terms of Service Analyzer",
    page_icon="📜",
    layout="wide"
)

# Load model and tokenizer from Hugging Face
@st.cache_resource
def load_model():
    model = AutoModelForSequenceClassification.from_pretrained("CodeHima/Tos-Roberta")
    tokenizer = AutoTokenizer.from_pretrained("CodeHima/Tos-Roberta")
    return model, tokenizer

model, tokenizer = load_model()

st.title("📜 Terms of Service Analyzer")

# File upload
uploaded_file = st.file_uploader("Choose a PDF or text file", type=["pdf", "txt"])

# Text input
text_input = st.text_area("Or paste your Terms of Service here")

if uploaded_file is not None or text_input:
    # Create a progress bar
    progress_bar = st.progress(0)
    
    # Create a status text
    status_text = st.empty()
    
    if uploaded_file is not None:
        status_text.text("Reading file...")
        progress_bar.progress(10)
        if uploaded_file.type == "application/pdf":
            text = extract_text_from_pdf(uploaded_file)
        else:
            text = uploaded_file.getvalue().decode("utf-8")
    else:
        text = text_input
    
    status_text.text("Splitting into clauses...")
    progress_bar.progress(30)
    clauses = split_into_clauses(text)
    
    results = []
    total_clauses = len(clauses)
    
    for i, clause in enumerate(clauses):
        status_text.text(f"Analyzing clause {i+1} of {total_clauses}...")
        # Update progress calculation to ensure it's always between 0 and 100
        progress = min(30 + int((i+1) / total_clauses * 60), 90)
        progress_bar.progress(progress)
        label, probabilities = predict_unfairness(clause, model, tokenizer)
        results.append({
            "clause": clause,
            "label": label,
            "probabilities": probabilities
        })
    
    status_text.text("Preparing results...")
    progress_bar.progress(100)
    
    df = pd.DataFrame(results)
    
    # Calculate summary
    total_clauses = len(df)
    clearly_fair = sum(df['label'] == 'clearly_fair')
    potentially_unfair = sum(df['label'] == 'potentially_unfair')
    clearly_unfair = sum(df['label'] == 'clearly_unfair')
    
    # Clear the progress bar and status text
    progress_bar.empty()
    status_text.empty()
    
    # Display summary
    st.header("Summary")
    col1, col2, col3 = st.columns(3)
    col1.metric("Clearly Fair", clearly_fair, f"{clearly_fair/total_clauses:.1%}")
    col2.metric("Potentially Unfair", potentially_unfair, f"{potentially_unfair/total_clauses:.1%}")
    col3.metric("Clearly Unfair", clearly_unfair, f"{clearly_unfair/total_clauses:.1%}")
    
    # Recommendation
    if clearly_unfair > 0 or potentially_unfair / total_clauses > 0.3:
        st.warning("⚠️ Exercise caution! This ToS contains unfair or potentially unfair clauses.")
    elif potentially_unfair > 0:
        st.info("ℹ️ Proceed with awareness. This ToS contains some potentially unfair clauses.")
    else:
        st.success("✅ This ToS appears to be fair. Always read carefully nonetheless.")
    
    # Display results
    st.header("Detailed Analysis")
    for _, row in df.iterrows():
        if row['label'] == 'clearly_fair':
            st.success(f"**{row['label'].replace('_', ' ').title()}:** {row['clause']}")
        elif row['label'] == 'potentially_unfair':
            st.warning(f"**{row['label'].replace('_', ' ').title()}:** {row['clause']}")
        else:
            st.error(f"**{row['label'].replace('_', ' ').title()}:** {row['clause']}")
        
        st.write(f"Probabilities: Clearly Fair: {row['probabilities'][0]:.2f}, "
                 f"Potentially Unfair: {row['probabilities'][1]:.2f}, "
                 f"Clearly Unfair: {row['probabilities'][2]:.2f}")
        st.divider()
else:
    st.info("Please upload a file or paste your Terms of Service to begin analysis.")