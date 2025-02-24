import streamlit as st

# Add a `run()` function to encapsulate the logic for this page
def run():
    st.title("📞 Contact Us 💬")
    
    st.write("""
        If you have any questions, feedback, or just want to say hello, feel free to reach out to us:

        ✉️ **Email**: [your-email@example.com](mailto:your-email@example.com)

        💻 **GitHub**: [Your GitHub Profile](https://github.com/your-github-profile)

        📱 **Follow us** on social media for updates and more:
        - [Twitter](https://twitter.com/your-twitter-profile) 🐦
        - [Instagram](https://instagram.com/your-instagram-profile) 📸
        
        🔄 Or you can use the contact form below to send us a message!
    """)

    # Optional: Contact form
    st.subheader("📬 Send us a message:")
    name = st.text_input("Your Name:")
    email = st.text_input("Your Email:")
    message = st.text_area("Your Message:")

    if st.button("Send Message"):
        if name and email and message:
            st.success("Your message has been sent! We'll get back to you soon. 😊")
        else:
            st.error("Please fill out all fields before sending your message. ❌")
