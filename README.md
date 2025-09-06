📱 **USSD Customer Churn Prediction App**  

This web application predicts whether a USSD customer is likely to **churn (stop using the service)** or **stay**,   
based on their profile and transaction history. It is built with **Streamlit** and powered by a machine learning model   
trained on simulated customer data.  


**✨ Features**  

* 🔮 **Churn Prediction** – Predicts the probability that a customer will churn.  
* 📊 **Interactive Input** – Users can adjust customer details (age, location, account type, transactions, etc.).  
* 📈 **Probability Scores** – Shows how confident the model is about churn vs stay.  
* 🖥️ **Web-based** – No setup needed beyond running the Streamlit app.  

**🛠️ Tech Stack**  

* **Python**  
* **Streamlit** – user interface  
* **scikit-learn** – machine learning model   
* **pandas, numpy** – data manipulation  
* **joblib** – model saving/loading  

---

**🚀 Getting Started**  

**1. Clone this repository**  

git clone https://github.com/your-username/ussd-customer-churn.git  
cd ussd-customer-churn  

**2. Create a virtual environment (optional but recommended)** 

python -m venv venv    
source venv/bin/activate   # On Mac/Linux  
venv\Scripts\activate      # On Windows  


**3. Install dependencies**  


pip install -r requirements.txt  

**4. Run the app**  

streamlit run src/streamlit_app.py  



Open your browser at http://localhost:8501 to interact with the app.  

**📂 Project Structure**  

📦 ussd-customer-churn  
 ├── 📂 src  
 │    ├── streamlit_app.py      # Main Streamlit app  
 │    └── churn_model.pkl       # Trained ML model  
 ├── requirements.txt           # Dependencies  
 ├── README.md                  # Project documentation 

**Example Usage**  

* A young urban customer with high transaction activity may have a **low churn probability**.  
* A rural customer with multiple failed transactions and complaints may show a **high churn probability**.  

**🔮 Future Enhancements**  

* Add data visualization dashboards. 
* Train on real USSD transaction datasets.  
* Integrate with telecom APIs for live predictions.   

**📜 License**

This project is for educational and research purposes.  
