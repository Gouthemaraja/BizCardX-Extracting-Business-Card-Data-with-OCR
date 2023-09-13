# BizCardX-Extracting-Business-Card-Data-with-OCR
# Project Description
Develop a Python application using Streamlit, easyOCR, and a database system (e.g., SQLite or MySQL) to extract and display key information from uploaded business card images, including company name, card holder name, contact details, and location. Users can upload, view, update, and delete entries within the application. This project involves image processing, OCR, GUI development, and robust database management, emphasizing scalability, maintainability, and well-organized code.

**User Interface (UI):**

Users interact with a web-based graphical user interface (GUI) created using Streamlit.
The GUI provides an option for uploading business card images and viewing extracted information.

**Image Upload and OCR:**
Users upload a business card image through the UI.
The application utilizes the easyOCR library to perform Optical Character Recognition (OCR) on the uploaded image.
OCR extracts text from the image, which includes company name, card holder name, contact details, and location.

**Displaying Extracted Information:**
The extracted information is displayed neatly within the UI, making it easy for users to review and verify.

**Database Management:**
The application uses a database system (e.g., SQLite or MySQL) to store entries.
When a new business card is uploaded, the extracted information, along with the image, is stored in the database.


## Approach

1. **Set Up a Virtual Environment (Optional)**:
   - Consider creating a virtual environment to isolate project dependencies. You can use tools like `virtualenv` or `conda` for this purpose.

2. **Install the Required Packages**:
   - Ensure you have Python, Streamlit, easyOCR, and a database management system like SQLite or MySQL installed within your virtual environment.

3. **Design the User Interface**:
   - Create an intuitive user interface using Streamlit, guiding users through the process of uploading business card images and displaying extracted information. Utilize widgets such as file uploaders, buttons, and text boxes to enhance interactivity.

4. **Implement Image Processing and OCR**:
   - Use easyOCR to extract pertinent details from uploaded business card images. Apply image processing techniques (e.g., resizing, cropping, thresholding) to improve image quality before OCR.

5. **Display Extracted Information**:
   - Present the extracted information cleanly within the Streamlit GUI. Employ widgets like tables, text boxes, and labels for organized data presentation.

6. **Integrate Database**:
   - Utilize a database system (e.g., SQLite or MySQL) to store extracted data alongside uploaded business card images. Employ SQL queries for table creation and data insertion, all accessible through the Streamlit UI.

7. **Testing**:
   - Rigorously test the application within your virtual environment to ensure it performs as expected. Run the application locally using the command `streamlit run app.py`, where `app.py` is your Streamlit application file.

8. **Continuous Improvement**:
   - Continuously enhance the application by adding new features, optimizing code, and resolving bugs. Consider implementing user authentication and authorization for enhanced security.

By following this approach, you can efficiently develop and maintain your business card information extraction application within a controlled virtual environment, focusing solely on the extraction and display of information.
