import streamlit as st

# Page Configuration
st.set_page_config(page_title="Dev Patel | Portfolio", layout="wide")

# Sidebar Navigation
st.sidebar.title("Navigation")
pages = ["Home", "About Me", "Projects", "Skills", "Experience", "Contact"]
selected_page = st.sidebar.radio("Go to:", pages)

# Custom CSS for Styling (Aligned to the left, no black line effect)
st.markdown("""
    <style>
        body {
            background-color: #121212;
            color: #ffffff;
            font-family: 'Arial', sans-serif;
        }
        .sidebar .sidebar-content {
            background-color: #1f1f1f;
        }
        .section {
            margin: 40px auto;
            padding: 20px;
            background-color: transparent; /* Transparent to avoid any boxed effect */
        }
        .section-header {
            font-size: 24px;
            color: #BB86FC;
            margin-bottom: 20px;
        }
        .stButton button {
            background-color: #BB86FC;
            color: #ffffff;
            border: none;
            padding: 10px 15px;
            border-radius: 5px;
            font-size: 14px;
            cursor: pointer;
            transition: background-color 0.3s ease;
        }
        .stButton button:hover {
            background-color: #3700B3;
        }
        a {
            color: #03DAC6;
            text-decoration: none;
        }
        a:hover {
            text-decoration: underline;
        }
    </style>
""", unsafe_allow_html=True)

# Home Section
if selected_page == "Home":
    st.markdown("<div class='section'>", unsafe_allow_html=True)
    st.title("👋 Hi, I'm Dev Patel")
    st.markdown("""
    Welcome to my portfolio!  
    I am a **junior at the University of Illinois Chicago (UIC)**, majoring in **Information and Decision Sciences** with a minor in **Finance**.  

    I specialize in building impactful **AI and Machine Learning solutions** to solve real-world problems.  

    🌟 **Highlights**:  
    - Developed high-accuracy machine learning models.  
    - Designed and deployed responsive, full-stack web applications.  
    - Solved technical challenges using scalable, efficient approaches.  
    """)
    st.markdown("</div>", unsafe_allow_html=True)

# About Me Section
elif selected_page == "About Me":
    st.markdown("<div class='section'>", unsafe_allow_html=True)
    st.header("🚀 About Me")
    st.markdown("""
    I am an **AI and ML enthusiast** passionate about delivering data-driven solutions that create a positive impact.  
    My professional journey revolves around solving technical challenges, optimizing workflows, and developing innovative software.

    **What Drives Me**:  
    - Curiosity to learn new technologies.  
    - Commitment to delivering high-quality solutions.  
    - Collaboration to foster innovation.

    **Outside of Work**:  
    - 🏀 Former high school basketball player with leadership and teamwork skills.  
    - 🐾 Volunteer at animal shelters, advocating for pet adoption.  
    - 🎤 Public speaking enthusiast, continuously honing my communication skills.  
    """)
    st.markdown("</div>", unsafe_allow_html=True)

# Projects Section
elif selected_page == "Projects":
    st.markdown("<div class='section'>", unsafe_allow_html=True)
    st.header("📂 Projects")
    projects = [
        {
            "name": "Customer Churn Prediction Model",
            "description": """
            Built an ANN-based model to predict customer churn for a bank.  
            - Achieved **87% accuracy** and **92% recall**.  
            - Tackled class imbalance with advanced preprocessing techniques.  
            """,
            "tech": "Python, TensorFlow, NumPy",
            "demo": "https://customer-churn-prediction-model-kmab3vph4dsajmceqk2apn.streamlit.app/",
            "code": "https://github.com/Devpatel954/Customer-churn-prediction-model-using-ANN"
        },
        {
            "name": "PostPulse",
            "description": """
            Developed a real-time data platform for content analysis.  
            - Enhanced user engagement by 30% through intuitive design.  
            - Optimized backend APIs, reducing response time by 45%.  
            """,
            "tech": "Node.js, MongoDB, Tailwind CSS",
            "code": "https://github.com/Devpatel954/Post-Pulse"
        },
        {
            "name": "Heart Disease Prediction Model",
            "description": """
            Created a machine learning app to predict heart disease likelihood.  
            - Achieved **93% precision**, aiding in healthcare decisions.  
            """,
            "tech": "Python, Scikit-learn, Pandas",
            "demo": "https://heart-disease-prediction-model-edenagbrbbdwb5ojfxked3.streamlit.app/",
            "code": "https://github.com/Devpatel954/Heart-disease-prediction-model"
        },
        {
            "name": "Movie Review Sentiment Analysis",
            "description": """
            Built an RNN-based model for classifying movie review sentiments.  
            - Delivered actionable insights to entertainment platforms.  
            """,
            "tech": "Python, TensorFlow",
            "demo": "https://movie-review-analysis-using-rnn-ahfykazpgavxmgvbar6kuk.streamlit.app/",
            "code": "https://github.com/Devpatel954/Movie-Review-analysis-using-RNN"
        },
    ]

    for idx, project in enumerate(projects):
        st.subheader(project["name"])
        st.write(project["description"])
        st.write(f"**Technologies Used:** {project['tech']}")
        col1, col2 = st.columns(2)
        with col1:
            if project.get("demo"):
                st.markdown(f"[Live Demo]({project['demo']})", unsafe_allow_html=True)
        with col2:
            if project.get("code"):
                st.markdown(f"[Code Repository]({project['code']})", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

# Skills Section
elif selected_page == "Skills":
    st.markdown("<div class='section'>", unsafe_allow_html=True)
    st.header("🔧 Skills")
    st.markdown("""
    - **Programming Languages**: Python, JavaScript, C++, SQL, Java  
    - **Frameworks & Libraries**: TensorFlow, Scikit-learn, React.js, Node.js, MongoDB  
    - **Tools**: Git & GitHub, Docker, Jupyter Notebook  
    - **Machine Learning**: ANN, RNN, NLP, Data Preprocessing, Model Building  
    """)
    st.markdown("</div>", unsafe_allow_html=True)

# Experience Section
elif selected_page == "Experience":
    st.markdown("<div class='section'>", unsafe_allow_html=True)
    st.header("💼 Work Experience")
    st.subheader("Technology Solution Specialist, UIC")
    st.markdown("""
    - Designed a diagnostic framework, reducing resolution time by **30%**.  
    - Provided technical support to 200+ students and staff, enhancing efficiency.  
    - Decreased system downtime by **50%**, boosting operational performance.  
    """)
    st.subheader("Software Engineering Intern, C-DAC, India")
    st.markdown("""
    - Developed AI/ML solutions, increasing customer engagement by **40%**.  
    - Reduced negative sentiment by **15%** with NLP-based feedback analysis.  
    - Boosted user satisfaction by **18%** with improved recommendation systems.  
    """)
    st.markdown("</div>", unsafe_allow_html=True)

# Contact Section
elif selected_page == "Contact":
    st.markdown("<div class='section'>", unsafe_allow_html=True)
    st.header("📫 Contact Me")
    st.markdown("""
    Feel free to connect or reach out for opportunities:
    """)
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("[Connect on LinkedIn](https://www.linkedin.com/in/devpatel117/)", unsafe_allow_html=True)
    with col2:
        st.markdown("[View GitHub](https://github.com/Devpatel954)", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

st.markdown("---")
st.markdown("© 2024 Dev Patel | Thank you for visiting my portfolio!")

















