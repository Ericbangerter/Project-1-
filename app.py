import streamlit as st
import barcode
from barcode.writer import ImageWriter

# Function to generate and display a barcode
def generate_and_display_barcode(data):
    code = barcode.get('code128', data, writer=ImageWriter(), add_checksum=False)
    barcode_image = code.save('temp_barcode')
    st.image('temp_barcode.png', use_column_width=True)

# Streamlit app
def main():
    st.title("Barcode Generator")
    
    # User input for data to encode
    data_to_encode = st.text_input("Enter data to encode:")
    
    if st.button("Generate Barcode"):
        if data_to_encode:
            generate_and_display_barcode(data_to_encode)
        else:
            st.warning("Please enter data to encode.")

if __name__ == "__main__":
    main()