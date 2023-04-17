from pathlib import Path

import streamlit as st
from PIL import Image

#--- PATH SETTINGS ---
current_dir = Path(_file_).parent if "_file_" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets" / "CV.pdf"
pic_image = current_dir / "assets" / "pic.jpg"


# --- GENERAL SETTINGS ---
PAGE_TITLE = "Digital CV | Iqbal Matnoor"
PAGE_ICON = "random"
NAME = "MUHAMMAD IQBAL NUR RIFQI BIN HAJI MATNOOR"
DESCRIPTION = """
IT Support Technician with excellent troubleshooting skills and good interpersonal skills to assist customers with computer issues.
An in-depth understanding of computer hardware and software applications is required.
Worked as an IT Support Technician for two years after receiving a Bachelor's Degree in Computer Science."""
EMAIL = "iqbalmatnoor22@gmail.com"
SOCIAL_MEDIA = {
    "LinkedIn": "https://www.linkedin.com/in/iqbal-haji-matnoor"
    }



st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)


# --- LOAD CSS, PDF & PROFILE PIC ---
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
pic_image = Image.open(pic_image)


# --- HERO SECTION ---

col1, col2 = st.columns(2, gap="small")
with col1:
    st.image(pic_image, width=230)

with col2:
    st.title(NAME)
    st.write(DESCRIPTION)
    st.download_button(
        label="📄Download Resume",
        data=PDFbyte,
        file_name=resume_file.name,
        mime="application/octet-stream",
        )
    st.write("📧",EMAIL)


# --- SOCIAL LINKS ---
st.write("#")
cols = st.columns(len(SOCIAL_MEDIA))
for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
    cols[index].write(f"[{platform}]({link})")


# --- WORK HISTORY ---
st.write("#")
st.subheader("Work History")
st.write("---")

#--- JOB 1
st.write("**IT Officer | Jabatan Pengajian Islam**")
st.write("22 May 2021 - 21 November 2022")
st.write(
    """
- ✔ Manage track record in delivering exceptional service to end-users and company clients.
- ✔ Maintain accurate, comprehensive reports of all IT-related systems including desktops and laptops and IT hardware.
- ✔ Ensure proper maintenance of computers peripherals, printer, networking, internet & e-mail, security, data backup and recovery.
- ✔ Assist to install software, network, internet, email, printer and update antivirus.
- ✔ Train and guide user on using new software, PC maintenance and troubleshoot.
- ✔ Interact with third-party service providers and vendors as needed top support core duties.
- ✔ Updates user data and produces activity reports.
- ✔ Manage new and existing users in Microsoft Endpoint Manager and Office365
"""
    )


#--- JOB 2
st.write("**IT Technician | OKVY Enterprise**")
st.write("1 October 2020 - 20 May 2021")
st.write(
    """
- ✔ Perform troubleshooting to diagnose and resolve problems (repair or replace parts, debugging etc.).
- ✔ Provide orientation and guidance to users on how to operate new software and computer
equipment.
- ✔ Re-imaging of laptops and desktops and software deployment.
- ✔ Maintain records/logs of repairs and fixes and maintenance schedule.
- ✔ Developing positive relationships with all departments and colleagues.

"""
    )


#--- JOB 3
st.write("**IT Support | Universiti Brunei Darussalam**")
st.write("1 April 2016 - 31 July 2016")
st.write(
    """
- ✔ Resolving IT support requests from employees.
- ✔ Answering employee questions regarding computer systems.
- ✔ Gathering and analyzing data to diagnose problems with computer systems.
- ✔ Changing configurations, settings and permissions to fix computer issues.
- ✔ Generating sign ins for new hires during the onboarding process.
- ✔ Installing new software and hardware drivers and updating existing ones as needed.
- ✔ Logging all service requests and updating tickets as needed.

"""
    )

# --- Course Attended ---
st.write('\n')
st.subheader("Course Attended ")
st.write(
    """
- ✔️ Implementing and Administering Cisco Solution (CCNA) 200-301
"""
)

# --- SKILLS ---
st.write('\n')
st.subheader("Hard Skills")
st.write(
    """
- 👩‍💻 Programming: Python, HTML, Javascript, CSS and PHP.
- 📊 Data Visulization: MS Excel
- 🖥📱💻 Technical Troubleshooting
"""
)


