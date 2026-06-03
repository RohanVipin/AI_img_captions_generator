import streamlit as st
from PIL import Image
from captions_service import generate_captions

# ---------------------------------
# Page Configuration
# ---------------------------------
st.set_page_config(
    page_title="AI Image Caption Generator",
    page_icon="📷",
    layout="centered"
)

# ---------------------------------
# Header
# ---------------------------------
st.title("📷 AI Image Caption Generator")
st.write(
    "Upload a JPG/JPEG image and generate captions in Formal, Casual, SEO, and Alt-Text formats."
)

# ---------------------------------
# File Upload
# ---------------------------------
uploaded_file = st.file_uploader(
    "Upload an Image",
    type=["jpg", "jpeg"]
)

# ---------------------------------
# Display Uploaded Image
# ---------------------------------
if uploaded_file is not None:

    image = Image.open(uploaded_file)

    st.image(
        image,
        caption="Uploaded Image",
        use_container_width=True
    )

    # ---------------------------------
    # Generate Captions Button
    # ---------------------------------
    if st.button("Generate Captions"):

        with st.spinner("Generating captions..."):

            try:
                image_bytes = uploaded_file.getvalue()

                captions = generate_captions(
                    image_bytes=image_bytes,
                    mime_type=uploaded_file.type
                )

                st.success("Captions generated successfully!")

                # -------------------------
                # Formal Caption
                # -------------------------
                st.subheader("📄 Formal Caption")
                st.write(captions["formal"])

                # -------------------------
                # Casual Caption
                # -------------------------
                st.subheader("😊 Casual Caption")
                st.write(captions["casual"])

                # -------------------------
                # SEO Caption
                # -------------------------
                st.subheader("🔍 SEO Caption")
                st.write(captions["seo"])

                # -------------------------
                # Alt Text
                # -------------------------
                st.subheader("♿ Alt Text")
                st.write(captions["alt_text"])

            except Exception as e:
                st.error(f"Error generating captions: {e}")