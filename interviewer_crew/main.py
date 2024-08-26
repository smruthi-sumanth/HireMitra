import os
from dotenv import load_dotenv
load_dotenv()

from interviewer_crew.crew import InterviewerCrew

def run():
    inputs = {
        'job_description' : """ An NLP Intern is sought after by companies aiming 
        to harness the power of artificial intelligence through natural language processing. 
        This role involves assisting in the development of algorithms that enable computers to 
        understand, interpret, and manipulate human language. Interns will participate in 
        creating and refining NLP models for various applications, including chatbots, 
        sentiment analysis, and language translation. They will work closely with 
        data scientists and software developers to integrate these models into 
        real-world applications, contributing to the advancement of AI-powered products. 
        This position requires a solid foundation in computer science, along with a 
        keen interest in AI and NLP. Ideal candidates will possess strong analytical skills, 
        proficiency in programming languages such as Python, and a willingness to continuously learn and adapt to new technologies.""",
        'resume_content': """Smruthi Rao
        +91 8431129169 | smruthisumanthrao.com | linkedin.com/in/Smruthi | github.com/Smruthi |
        Kaggle/Smruthi| Medium/Smruthi
        Experience
        Research Intern (May 2024 - August 2024) NITK, Surathkal
        • Conducted Research on Automatic Music Transcription of Carnatic Classical Music.
        • Utilized advanced machine learning models and techniques, including deep learning and signal processing, to
        enhance transcription accuracy.
        • Worked extensively with open-source models and frameworks, leveraging their capabilities to build and optimize
        transcription algorithms.
        • Presented research findings to stakeholders and documented the research process and results in detailed reports,
        contributing to the broader knowledge base in the field.
        NLP Intern (August 2024 - present) EDCULTS Consulting
        • Developed OCR software for passport recognition, mapping results to fields using Claude and integrating Bedrock
        for enhanced functionality.
        • Created an LLM dashboard that translates natural language queries and commands into SQL queries and generates
        visualizations accordingly.
        • Researched and evaluated open-source alternatives to enterprise software, identifying viable options for
        cost-effective solutions.
        • Collaborated effectively with team members, demonstrating strong teamwork skills for project alignment and
        progress
        Projects
        Amino - PyTorch Lightning, Python, WebGL, Flask, Git, Sidechainnet, 3Dmol
        • Developed a protein structure predictor and visualizer, utilizing SidechainNet and PyTorch Lightning to accurately
        model and predict protein structures
        • Developed and optimized a PyTorch Lightning-based transformer model for accurate protein sidechain angle
        prediction
        • Created an interactive 3D visualization tool using WebGL and 3Dmol.js, enabling users to explore protein
        structures in a web-based environment.
        DROPEX - Unity3D, C#, Python, PyTorch, OpenCV, Barracuda,
        • Designed and developed a Unity3D-based drone simulation with a camera-equipped drone for real-time surveillance
        and detection tasks.
        • Implemented YOLO and DETr models within the simulation for accurate real-time detection of people in distress.
        • Developed a custom image processing pipeline for the drone’s camera, enabling efficient object detection and
        tracking.
        Perspective - Python, Wolfram Mathematica, Echo3D, MongoDB, GridFS, Flask, Git
        • Designed and implemented a comprehensive application that generates 3D models from mathematical expressions
        using Wolfram Language and exports them as OBJ files.
        • Integrated the application with Echo3D’s API to upload and manage 3D models, enabling Augmented Reality view
        of complex mathematical plots.
        • Implemented functionality to store and retrieve 3D models using MongoDB and GridFS, ensuring efficient data
        handling and scalability.
        • Utilized Flask for backend development and integrated a frontend form, creating a seamless and interactive user
        experience for generating and visualizing 3D plots.
        Education
        Bachelor of Engineering in Computer Science and Design CGPA – 9.07
        Dayananda Sagar College of Engineering 2021 - Present
        Certifications
        • Mathematics for Machine Learning Specialisation DeepLearning.AI
        • Deep Learning Specialisation DeepLearning.AI
        • Quantum Computing Career Accelerator Program Quetzal
        Achievements
        • Reached the semi-finals in the Karnataka State Police Hackathon, developing a federated learning model
        to enhance data privacy for victims
        • Selected as a MATLAB Student Ambassador for the DSCE campus, representing MATLAB and
        facilitating its use among students.
        • Ranked up to Kaggle Expert on the datascience platform
        • Presented a paper titled ”A Comparative Study of Principal Component Analysis: Supervised vs.
        Unsupervised Data” at ICAETIS 2023,
        Technical Skills
        Languages: Python,MATLAB, C/C++, SQL, C#, HTML/CSS
        Frameworks: Tensorflow, Keras, Scikit-Learn, PyTorch, OpenCV, Flask, Streamlit, Langchain, Ollama
        Developer Tools: Git, Google Colabs, PyCharm, Unity
        Libraries: Pandas, NumPy, Matplotlib, Scipy, Seaborn, AutoJAX """
        }
    InterviewerCrew().crew().kickoff(inputs=inputs)

if __name__ == "__main__":
    run()
