
import streamlit as st
from streamlit_option_menu import option_menu
from annotated_text import annotated_text




st.set_page_config(page_title="Cancer Prediction System", page_icon=":hospital:", layout="wide")


selected = option_menu(
            menu_title=None,  # required
            options=["Home", "Prediction"],  # required
            icons=["house","activity"],  # optional
            menu_icon="cast",  # optional
            default_index=0,  # optional
            orientation="horizontal",
        )
  
 
if selected == "Home":
            
            with st.container():
                    st.title("Overview")
                    st.write("Machine learning is a branch of artificial intelligence that employs a variety of statistical, probabilistic and optimization techniques that allows computers to “learn” from past examples and to detect hard-to-discern patterns from large, noisy or complex data sets. This capability is particularly well-suited to medical applications, especially those that depend on complex proteomic and genomic measurements. As a result, machine learning is frequently used in cancer diagnosis and detection. More recently machine learning has been applied to cancer prognosis and prediction. This latter approach is particularly interesting as it is part of a growing trend towards personalized, predictive medicine. In assembling this review we conducted a broad survey of the different types of machine learning methods being used, the types of data being integrated and the performance of these methods in cancer prediction and prognosis. A number of trends are noted, including a growing dependence on protein biomarkers and microarray data, a strong bias towards applications in prostate and breast cancer, and a heavy reliance on “older” technologies such artificial neural networks (ANNs) instead of more recently developed or more easily interpretable machine learning methods. A number of published studies also appear to lack an appropriate level of validation or testing. Among the better designed and validated studies it is clear that machine learning methods can be used to substantially (15–25%) improve the accuracy of predicting cancer susceptibility, recurrence and mortality. At a more fundamental level, it is also evident that machine learning is also helping to improve our basic understanding of cancer development and progression.")
            
            import streamlit as st
            from streamlit_option_menu import option_menu
            selected = option_menu(
                        menu_title=None,  # required
                        options=["Lung cancer", "Breast cancer", "Prostate cancer"],  # required
                        menu_icon="cast",  # optional
                        default_index=0,  # optional
                        orientation="horizontal",
                    )
            
if selected == "Lung cancer":
          with st.container():
                  st.write("---")
                  left_column, right_column = st.columns(2)
          with left_column:
                  st.header("What is a Lung cancer?")
                  st.write("Cancer is a disease in which cells in the body grow out of control. When cancer starts in the lungs, it is called lung cancer.Lung cancer begins in the lungs and may spread to lymph nodes or other organs in the body, such as the brain. Cancer from other organs also may spread to the lungs. When cancer cells spread from one organ to another, they are called metastases.Lung cancers usually are grouped into two main types called small cell and non-small cell (including adenocarcinoma and squamous cell carcinoma). These types of lung cancer grow differently and are treated differently. Non-small cell lung cancer is more common than small cell lung cancer.")
                  st.write("Your lungs are 2 sponge-like organs in your chest. Your right lung has 3 sections, called lobes. Your left lung has 2 lobes. The left lung is smaller because the heart takes up more room on that side of the body.When you breathe in, air enters through your mouth or nose and goes into your lungs through the trachea (windpipe). The trachea divides into tubes called bronchi, which enter the lungs and divide into smaller bronchi. These divide to form smaller branches called bronchioles. At the end of the bronchioles are tiny air sacs known as alveoli.The alveoli absorb oxygen into your blood from the inhaled air and remove carbon dioxide from the blood when you exhale. Taking in oxygen and getting rid of carbon dioxide are your lungs’ main functions.Lung cancers typically start in the cells lining the bronchi and parts of the lung such as the bronchioles or alveoli.")
                  st.header("Types of lung cancer")
                  st.write("There are 2 main types of lung cancer and they are treated very differently.")
                  st.subheader("Non-small cell lung cancer (NSCLC)")
                  st.write("About 80% to 85% of lung cancers are NSCLC. The main subtypes of NSCLC are adenocarcinoma, squamous cell carcinoma, and large cell carcinoma. These subtypes, which start from different types of lung cells are grouped together as NSCLC because their treatment and prognoses (outlook) are often similar.Adenocarcinoma: Adenocarcinomas start in the cells that would normally secrete substances such as mucus.This type of lung cancer occurs mainly in people who currently smoke or formerly smoked, but it is also the most common type of lung cancer seen in people who don't smoke. It is more common in women than in men, and it is more likely to occur in younger people than other types of lung cancer.")
                  st.subheader("Small cell lung cancer (SCLC)")
                  st.write("About 10% to 15% of all lung cancers are SCLC and it is sometimes called oat cell cancer. This type of lung cancer tends to grow and spread faster than NSCLC. About 70% of people with SCLC will have cancer that has already spread at the time they are diagnosed. Since this cancer grows quickly, it tends to respond well to chemotherapy and radiation therapy. Unfortunately, for most people, the cancer will return at some point.")
                  st.header("Symptoms")
                  st.write("People with lung cancer may not have any symptoms until a later stage. If lung cancer signs do appear, they can resemble those of a respiratory infection.")
                  st.write("Some possible symptoms includeTrusted Source:changes to a person’s voice, such as hoarseness frequent chest infections, such as bronchitis or pneumonia,swelling in the lymph nodes in the middle of the chest, a lingering cough that may start to get worse, chest pain, shortness of breath and wheezing, In time, a person may also experience more severe symptoms, such as: severe chest pain,bone pain and bone fractures, headaches, coughing up blood, blood clots, appetite loss and weight loss,fatigue")
                    
          with right_column:
                  
                  from PIL import Image
                  st.image("https://www.cdc.gov/cancer/lung/images/lung-diagram-750.jpg?_=49525",width=(int(500)))
                  st.text(" ")
                  st.text(" ")
                  st.text(" ")
                  st.text(" ")
                  
                  st.image("data:image/jpeg;base64,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",width=(int(500)))
                  st.text(" ")
                  st.text(" ")
                  st.text(" ")
                  st.image("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT3r3R5yB6cCwoX3O9Nl-rg4x1jncbpBRhdJQ&usqp=CAU",width=(int(500)))
if selected == "Breast cancer":
                  st.header("What is a Breast cancer?")
                  st.write("Breast cancer is cancer that forms in the cells of the breasts.After skin cancer, breast cancer is the most common cancer diagnosed in women in the United States. Breast cancer can occur in both men and women, but it's far more common in women.Substantial support for breast cancer awareness and research funding has helped created advances in the diagnosis and treatment of breast cancer. Breast cancer survival rates have increased, and the number of deaths associated with this disease is steadily declining, largely due to factors such as earlier detection, a new personalized approach to treatment and a better understanding of the disease.")
                  st.write("It’s important to understand that most breast lumps are benign and not cancer (malignant). Non-cancer breast tumors are abnormal growths, but they do not spread outside of the breast. They are not life threatening, but some types of benign breast lumps can increase a woman's risk of getting breast cancer. Any breast lump or change needs to be checked by a health care professional to find out if it is benign or malignant (cancer) and if it might affect your future cancer risk.")
                  st.header("Types of Breast Cancer")
                  st.write("types of breast cancer include ductal carcinoma in situ, invasive ductal carcinoma, inflammatory breast cancer, and metastatic breast cancer.")
                  st.subheader("Invasive breast cancer")
                  st.write("When breast cancer is called invasive (or infiltrating), it means it has spread into the surrounding breast tissue. The two most common types of invasive breast cancer are defined by where in the breast they begin to grow:")
                  st.write("Invasive ductal carcinoma (IDC) is invasive breast cancer that starts in the milk ducts, the tubes that carry milk from the lobules to the nipple. It is the most common type of breast cancer; about 80% of all breast cancers are invasive ductal carcinomas.")
                  st.write("Invasive lobular carcinoma (ILC) is invasive breast cancer that starts in the lobules, the glands in the breast that produce milk. It is the second most common type of breast cancer; about 10% of all invasive breast cancers are invasive lobular carcinomas.")
                  st.subheader("Non-invasive breast cancer")
                  st.write("When breast cancer is called non-invasive (or in situ) it means it has not spread beyond the breast tissue where it started. Non-invasive breast cancers are also called precancers. There are two main types of non-invasive breast cancer:")
                  st.write("Ductal carcinoma in situ (DCIS), is non-invasive breast cancer that has not spread outside the milk ducts where it started. DCIS isn’t life threatening, but is considered a precursor to invasive breast cancer and increases the risk of developing an invasive breast cancer later in life. About 16% of all breast cancer diagnoses are DCIS.")
                  st.write("Lobular carcinoma in situ (LCIS), is non-invasive breast cancer that has not spread outside the lobules where it started. Despite its name, LCIS is a benign breast condition and is not a true breast cancer.")
                  st.subheader("Cancerous phyllodes tumors of the breast")
                  st.write("Phyllodes tumors of the breast are rare and make up fewer than 1% of all breast tumors. Most phyllodes tumors are benign (not cancerous), but about 25% are cancerous.")
                  st.header("What Are the Symptoms of Breast Cancer?")
                  st.write("Different people have different symptoms of breast cancer. Some people do not have any signs or symptoms at all.")
                  st.write("New lump in the breast or underarm (armpit),Thickening or swelling of part of the breast,Irritation or dimpling of breast skin,Redness or flaky skin in the nipple area or the breast,Pulling in of the nipple or pain in the nipple area,Nipple discharge other than breast milk, including blood,Any change in the size or the shape of the breast,Pain in any area of the breast.")
if selected == "Prostate cancer":
                  st.header("What Is Prostate Cancer?")
                  st.write("Prostate cancer begins when cells in the prostate gland start to grow out of control. The prostate is a gland found only in males. It makes some of the fluid that is part of semen.The prostate is below the bladder (the hollow organ where urine is stored) and in front of the rectum (the last part of the intestines). Just behind the prostate are glands called seminal vesicles that make most of the fluid for semen. The urethra, which is the tube that carries urine and semen out of the body through the penis, goes through the center of the prostate.")
                  st.write("The size of the prostate can change as a man ages. In younger men, it is about the size of a walnut, but it can be much larger in older men.")
                  st.write("Prostate cancer is the most common type of cancer found in men in the United State, aside from skin cancer, and often begins without symptoms. Prostate cancer can be slow-growing, such that many men die of other diseases before the prostate cancer causes significant problems. However, many prostate cancers are more aggressive and can spread outside the confines of the prostate gland, which can be deadly. The prostate cancer survival rate is greatly improved with early detection and personalized treatment.")
                  st.header("Types of prostate cancer")
                  st.write("Almost all prostate cancers are adenocarcinomas. These cancers develop from the gland cells (the cells that make the prostate fluid that is added to the semen).")
                  st.write("Other types of cancer that can start in the prostate include: Small cell carcinomas,Neuroendocrine tumors (other than small cell carcinomas),Transitional cell carcinomas,Sarcomas")
                  st.write("These other types of prostate cancer are rare. If you are told you have prostate cancer, it is almost certain to be an adenocarcinoma.Some prostate cancers grow and spread quickly, but most grow slowly. In fact, autopsy studies show that many older men (and even some younger men) who died of other causes also had prostate cancer that never affected them during their lives. In many cases, neither they nor their doctors even knew they had it.")
                  st.subheader("Prostatic intraepithelial neoplasia (PIN)")
                  st.write("In PIN, there are changes in how the prostate gland cells look when seen with a microscope, but the abnormal cells don’t look like they are growing into other parts of the prostate (like cancer cells would). Based on how abnormal the patterns of cells look, they are classified as:")
                  st.write("Low-grade PIN: The patterns of prostate cells appear almost normal, High-grade PIN: The patterns of cells look more abnormal.")
                  st.write("Low-grade PIN is not thought to be related to a man’s risk of prostate cancer. On the other hand, high-grade PIN is thought to be a possible precursor to prostate cancer. If you have a prostate biopsy and high-grade PIN is found, there is a greater chance that you might develop prostate cancer over time.PIN begins to appear in the prostates of some men as early as in their 20s. But many men with PIN will never develop prostate cancer.")
                  st.subheader("Proliferative inflammatory atrophy (PIA)")
                  st.write("In PIA, the prostate cells look smaller than normal, and there are signs of inflammation in the area. PIA is not cancer, but researchers believe that PIA may sometimes lead to high-grade PIN, or perhaps directly to prostate cancer.")
                  st.header("What are the symptoms of Prostate cancer")
                  st.write("A symptom is something that only the person experiencing it can identify and describe, such as fatigue, nausea, or pain. A sign is something that other people can identify and measure, such as a fever, rash, or an elevated pulse. Together, signs and symptoms can help describe a medical problem. While most prostate cancer does not cause any symptoms at all, the symptoms and signs of prostate cancer may include:")
                  st.write("Frequent urination,Weak or interrupted urine flow or the need to strain to empty the bladder,The urge to urinate frequently at night,Blood in the urine,New onset of erectile dysfunction,Pain or burning during urination, which is much less common,Discomfort or pain when sitting, caused by an enlarged prostate")
if selected == "Contact":

                st.header(":mailbox: Get In Touch With Me!")
                
                
                contact_form = """
                <form action="https://formsubmit.co/farizmuhammed07@gmail.com" method="POST">
                     <input type="hidden" name="_captcha" value="false">
                     <input type="text" name="name" placeholder="Your name" required>
                     <input type="email" name="email" placeholder="Your email" required>
                     <textarea name="message" placeholder="Your message here"></textarea>
                     <button type="submit">Send</button>
                </form>
                """
                
                st.markdown(contact_form, unsafe_allow_html=True)
                
                # Use Local CSS File
                def local_css(file_name):
                    with open(file_name) as f:
                        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
                
                
                    local_css("style/style.css")

if selected == "Prediction":
                    import pickle
                    import streamlit as st
                    from streamlit_option_menu import option_menu
        
        
                    #loading the saved models
        
                    prostate_cancer_model = pickle.load(open('C:/Users/fariz/Desktop/cancer prediction/models/trained_model_prost.sav','rb'))
        
                    lung_cancer_model = pickle.load(open('C:/Users/fariz/Desktop/cancer prediction/models/model_lung.sav','rb'))
        
                    breast_cancer_model = pickle.load(open('C:/Users/fariz/Desktop/cancer prediction/models/breast_model.sav','rb'))
        
        
                    #sidebar for naviaget
        
        
                        
                    selected = option_menu( 'Cancer Prediction Systems',
                                               ['Prostate Cancer Prediction',
                                                'Lung Cancer Prediction',
                                                'Breast Cancer Prediction'],
                                               icons = ['x-octagon','activity','file-earmark-medical-fill'],
                                               default_index = 0,
                                               orientation="horizontal",
                                               styles={
                                                  "nav-link":{
                                                      "font-size":"15px",
                                                      "text-align":"left",
                                                      "margin":"0px",
                                                      "--hover-color":"#ff4b4b",
                                                      },
                                                  "container":{
                                                      "width":"100vw",
                                                      "padding":"0!important",
                                                      "background-color":"grey"}})
                        
                    if(selected == 'Prostate Cancer Prediction'):
                        
                        
                        #page title
                        st.title('Prostate Cancer Prediction using ML')
                    
                            
                        radius = st.text_input('radius')
                       
                        texture =st.text_input('texture')
                       
                        perimeter = st.text_input('perimeter')
                        area = st.text_input('area')
                        smoothness = st.text_input('smoothness')
                        #compactness = st.text_input('compactness')
                        #symmetry = st.text_input('symmetry')
                        #fractal_dimension = st.text_input('factal dimension')
                       
                        prostate_diagnosis = ''
    
                        if st.button('Predict'):
                            prostate_prediction = prostate_cancer_model.predict([[ radius,texture,perimeter,area,smoothness]])
         
                            if (prostate_prediction == 1):
                                
                                prostate_diagnosis = "the person have Prostate Cancer"
                            if(prostate_prediction == 0):
                                prostate_diagnosis = "the person is healthy"
                        st.success(prostate_diagnosis)
                      
                        
                    if(selected == 'Lung Cancer Prediction'):
                        
                        #page title
                        st.title('Lung Cancer Prediction System using ML')
                        
        
                        
                        Age=st.text_input('enter Your Age')
                        Smokes=st.text_input('Smoking level of the patient.')
                        AreaQ =st.text_input('Air Quality of the area where patient resides')
                        Alkhol =st.text_input('Alkohol Level Of the Patient')
                        
                        
                        
                        
                        lung_diagnosis = ''
                        
                        if st.button('Predict'):
                             lung_cancer_prediction =lung_cancer_model.predict([[Age,Smokes,AreaQ,Alkhol]])
                      
                             
                             if (lung_cancer_prediction  == 0):
                                 lung_diagnosis = "safe"
                             else:
                                lung_diagnosis = 'the person have lung Cancer'
                        st.success( lung_diagnosis)
                              
                             
                           
                      
                        
        
                    if(selected == 'Breast Cancer Prediction'):
                        
                        #page title
                        st.title('Breast Cancer Prediction System using ML')
                       
                       
        
        
                        
                        mean_radius = st.text_input('mean radius')
                        mean_texture = st.text_input('mean texture')
                        mean_perimeter = st.text_input('mean perimeter value')
                        mean_area = st.text_input('mean area')
                        mean_smoothness = st.text_input('mean smoothness')
                        mean_compactness = st.text_input('mean compactness')
                        mean_concavity = st.text_input('mean concavity')
                        mean_concave_points = st.text_input('mean concave')
                        mean_symmetry = st.text_input('mean symmetry')
                        mean_fractal_dimension = st.text_input('mean fractal dimension')
                        radius_error = st.text_input('radius error')
                        texture_error = st.text_input('texture error')
                        perimeter_error = st.text_input('perimeter error')
                        area_error = st.text_input('area error')
                        smoothness_error = st.text_input('smoothness error')
                        compactness_error = st.text_input('compactness error')
                        concavity_error = st.text_input('concavity error')
                        concave_points_error = st.text_input('concave points error')
                        symmetry_error = st.text_input('symmetry error')
                        fractal_dimension_error = st.text_input('fractal dimension error')
                        worst_radius = st.text_input('worst radius')
                        worst_texture = st.text_input('worst texture')
                        worst_perimeter = st.text_input('worst perimeter')
                        worst_area = st.text_input('worst area')
                        worst_smoothness = st.text_input('worst smoothness')
                        worst_compactness = st.text_input('worst compactness')
                        worst_concavity = st.text_input('worst concavity')
                        worst_concave_points = st.text_input('worst concave points')
                        worst_symmetry = st.text_input('worst symmetry')
                        worst_fractal_dimension = st.text_input('worst fractal dimension')
                        
                        
                        
                            
                        
                        breast_dignosis = ''
                        
                        
                        #creating a button for prediction
                        
                        if st.button('Predict'):
                             breast_prediction = breast_cancer_model.predict([[mean_radius,mean_texture,mean_perimeter,mean_area,mean_smoothness,mean_compactness,mean_concavity,mean_concave_points,mean_symmetry,mean_fractal_dimension,radius_error,texture_error,perimeter_error,area_error,smoothness_error,compactness_error,concavity_error,concave_points_error,symmetry_error,fractal_dimension_error,worst_radius,worst_texture,worst_perimeter,worst_area,worst_smoothness,worst_compactness,worst_concavity,worst_concave_points,worst_symmetry,worst_fractal_dimension]])
                             
                             if (breast_prediction == 0):
                                 breast_dignosis = "The Breast cancer is Malignant"
                             else:
                                breast_dignosis = 'The Breast Cancer is Benign'
                        st.success(breast_dignosis)
                      
                        

                        
                        
                        
                        
                        
                    
                    

