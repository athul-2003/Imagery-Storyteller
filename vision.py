from dotenv import load_dotenv
import os
import streamlit as st
import google.generativeai as genai
from PIL import Image

# Load environment variables
load_dotenv()

# Configure Gemini API
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Load Gemini Pro model
model = genai.GenerativeModel("gemini-pro-vision")

def get_gemini_response(input_prompt, story_type, image):
    """Generate content using the Gemini model."""
    try:
        if input_prompt:
            response = model.generate_content([input_prompt, story_type, image])
        else:
            response = model.generate_content([story_type, image])
        return response.text
    except Exception as e:
        st.error(f"An error occurred: {e}")
        return None

def main():
    """Main function to run the Streamlit app."""
    # Initialize Streamlit app
    st.set_page_config(page_title="Gemini Application")
    st.title("🔮 Imagery Storyteller 📖")
    st.markdown("\n")

    # User input
    input_prompt = st.text_area("🚀 Enter Your Story Prompt:", key="input", help="e.g., 'Write a story which starts as 'In a world where....''")

    # Dropdown for story type
    story_type = st.selectbox("📚 Select Story Type:", ["","Sci-Fi", "Mystery", "Fantasy", "Adventure", "Romance", "Other"], index=0)

    uploaded_file = st.file_uploader("🖼️ Choose an image ...", type=["jpg", "jpeg", "png"])
    image = None
    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        st.image(image, caption='Uploaded Image.', use_column_width=True)

    # Submit button
    if st.button("Write Story 🤖"):
        # Input validation
        if not input_prompt:
            st.warning("Please provide a prompt for your story.")
        else:
            with st.spinner("Generating your story..."):
                # Generate story
                response_text = get_gemini_response(input_prompt, story_type, image)
                
                # Display the response text
                if response_text is not None:
                    st.subheader("Your Story:")
                    st.write(response_text)

                    # Positive feedback
                    st.success("Story successfully generated!")

if __name__ == "__main__":
    main()






    




       





   


   



