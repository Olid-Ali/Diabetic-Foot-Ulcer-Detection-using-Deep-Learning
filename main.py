import streamlit as st
from PIL import Image
from util import predictor
import smtplib



# Function to run the image classifier
def run_image_classifier():
    st.markdown('<div style="text-align: center;"><h1 style="color: #F2F7A1;">Predict Foot Ulcer</h1></div>', unsafe_allow_html=True)


    # Sidebar for user input
    crop_image = st.sidebar.checkbox("Crop Image", value=False)

    # File uploader
    uploaded_file = st.file_uploader("Add Image", type=["jpg", "jpeg", "png"])

    if uploaded_file is not None:
        # Convert the uploaded file to an OpenCV image
        image = Image.open(uploaded_file).convert("RGB")

        # Display the uploaded image
        st.image(image, caption="Uploaded Image", use_column_width=True)

        # Run prediction when the user clicks the button
        if st.button("Run Prediction"):
            probability, index = predictor(image)

            if index == 0:
                class_name = "Foot Ulcer"
            else:
                class_name = "Normal"

            if class_name is not None:
                st.success(f"Predicted Class: {class_name}, Probability: {probability*100:.2f}%")
            else:
                st.warning("Prediction failed.")
    else:
        st.info("Please upload an image.")



# Function for the contact page
def contact_page():
    st.markdown('<div style="text-align: center;"><h1 style="color: #F2F7A1;">Contact us</h1></div>', unsafe_allow_html=True)


    # Form for user input
    with st.form("contact_form"):
        email = st.text_input("Your Email:")
        message = st.text_area("Message:")
        submit_button = st.form_submit_button("Submit")

        if submit_button:
            # Send email notification (you need to configure your SMTP server)
            send_email(email, message)
            st.success("Message sent successfully!")


# Email Sent Notification

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_email(email, message):
    # Configure Gmail SMTP server
    smtp_server = "smtp.gmail.com"
    smtp_port = 587
    smtp_username = "mahmudislam2025@gmail.com"  # Your Gmail address
    smtp_password = "rjug wzkp lskn ggmn"  # Generate an app password for your Gmail account

    # Create an SMTP connection
    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.starttls()
        server.login(smtp_username, smtp_password)

        # Compose the email
        subject = "New Contact Form Submission"
        body = f"Email: {email}\nMessage: {message}"

        # Create a multipart message and set headers
        msg = MIMEMultipart()
        msg["From"] = smtp_username
        msg["To"] = "mahmudislam2025@gmail.com"
        msg["Subject"] = subject

        # Attach the body to the email
        msg.attach(MIMEText(body, "plain"))

        # Send the email
        server.sendmail(smtp_username, "mahmudislam2025@gmail.com", msg.as_string())


# Function to create a two-column layout with an image and text
        
def homepage():
    st.markdown('<div style="text-align: center;"><h1 style="color: #F2F7A1;">Diabetic Foot Ulcer Detection</h1></div>', unsafe_allow_html=True)
    st.markdown('<div style="text-align: center;"><h5 style="color: #A5D7E8;">Developed and maintained by Monirul, Hafeza and Olid</h5></div>', unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)

    # Create a two-column layout
    col1, col2 = st.columns(2)

    # Column 1: Display an image
    with col1:
        st.image("https://sa1s3optim.patientpop.com/assets/images/provider/photos/2069609.jpg", caption="Diabetic Foot Ulcer", use_column_width=True)
        st.image("https://static.bangkokpost.com/media/content/20231110/4955333.jpg", caption="Foot Ulcer and Wound", use_column_width=True)

    # Column 2: Display text
    with col2:
        st.markdown(
            """
            <div style="text-align: justify;">
            Diabetic Foot Ulcers (DFUs) are a common complication of diabetes and can lead to serious consequences 
            if not detected and treated early. In recent years, the intersection of healthcare and cutting-edge technology 
            has paved the way for transformative advancements, offering innovative solutions to longstanding challenges. 
            One such critical issue is the early detection and management of diabetic foot ulcers, a complication that significantly 
            impacts the quality of life for individuals living with diabetes. In response to this pressing healthcare concern, the 
            present project, titled "Diabetic Foot Ulcer Detection using Machine Learning," embarks on a journey to leverage the 
            prowess of state-of-the-art technologies to revolutionize the diagnostic landscape. Our web app leverages machine learning 
            to assist in the early detection 
            of diabetic foot ulcers through the analysis of uploaded images. By using advanced image classification 
            techniques, our app aims to provide a quick and accurate assessment, helping individuals and healthcare 
            professionals in making informed decisions about preventive measures and treatments.

        At its core, this project employs a sophisticated ensemble of Deep Learning models, namely EfficientNet, DenseNet, and MobileNet, to address the complexities inherent in diabetic foot ulcer detection. The utilization of these models underscores a commitment to harnessing the power of neural networks, known for their capability to discern intricate patterns and features within medical images, thereby facilitating precise and early identification of diabetic foot ulcers. A pivotal aspect of the project lies in its emphasis on interpretability and transparency. To demystify the decision-making processes of the deep learning models employed, the project incorporates Explainable AI, specifically Local Interpretable Model-agnostic Explanations (LIME). By providing insights into the rationale behind each prediction, LIME not only enhances the trustworthiness of the model but also aids healthcare practitioners in understanding and validating the diagnostic outcomes.

            
        <br>Features:
        - Upload an image to check for the presence of foot ulcers.
        - Optional cropping of the uploaded image for better analysis.
        - Receive real-time predictions with probabilities.            </div>
            """, unsafe_allow_html=True
        )




# Main function to control the app
def main():

    st.set_page_config(page_title='CSE 498R - DFU',  layout = 'wide', initial_sidebar_state = 'auto')
    # favicon being an object of the same kind as the one you should provide st.image() with (ie. a PIL array for example) or a string (url or local file path)
    # Create radio buttons in the sidebar for navigation
    selected_page = st.sidebar.radio("Menu", ["Home", "Predict", "Contact"])

    # Show content based on the selected radio button
    if selected_page == "Home":
        homepage()
    elif selected_page == "Predict":
        run_image_classifier()
    elif selected_page == "Contact":
        contact_page()
    else:
        homepage()



# Run the Streamlit app
if __name__ == "__main__":
    main()
