Disesase Predictions
==============================
* Parkinson Disease
   * Parkinson Disease is a brain neurological disorder. It leads to shaking of the body, hands and provides stiffness to the body. No proper cure or treatment is available yet at the advanced stage. Treatment is possible only when done at the early or onset of the disease. These will not only reduce the cost of the disease but will also possibly save a life. Most methods available can detect Parkinson in an advanced stage; which means loss of approx.. 60% dopamine in basal ganglia and is responsible for controlling the movement of the body with a small amount of dopamine. More than 145,000 people have been found alone suffering in the U.K and in India, almost one million population suffers from this disease and it’s spreading fast in the entire world.
     We will make use of XGBoost, KNN, SVMs, and Random Forest,Logistic Regression Algorithm to check which is the best algorithm for detection of the onset of disease.
* Heart Disease
   *  Heart disease is the one of the most common disease. This disease is quite common now a days we used different attributes which can relate to this heart diseases well to find the better method to predict and we also used algorithms for prediction. Random Forest, algorithm is analyzed on dataset based on risk factors. We also used decision trees and combination of algorithms for the prediction of heart disease based on the above attributes.

* Thyroid Disease
   *  Thyroid disease is a common cause of medical diagnosis and prediction, with an onset that is difficult to forecast in medical research. The thyroid gland is one of our body's most vital organs. Thyroid hormone releases are responsible for metabolic regulation. Hyperthyroidism and hypothyroidism are one of the two common diseases of the thyroid that releases thyroid hormones in regulating the rate of body's metabolism.

About Dataset
================================
* Parkinson Dataset
  * The dataset consists of 24 columns including the target column and the columns includes:
	name - ASCII subject name and recording number,
	MDVP:Fo(Hz) - Average vocal fundamental frequency,
	MDVP:Fhi(Hz) - Maximum vocal fundamental frequency,
	MDVP:Flo(Hz) - Minimum vocal fundamental frequency,
	MDVP:Jitter(%),MDVP:Jitter(Abs),MDVP:RAP,MDVP:PPQ,
	Jitter:DDP - Several measures of variation in fundamental frequency
	MDVP:Shimmer,MDVP:Shimmer(dB),Shimmer:APQ3,Shimmer:APQ5,MDVP:APQ,Shimmer:DDA - Several measures of variation in amplitude
	NHR,HNR - Two measures of ratio of noise to tonal components in the voice
	status - Health status of the subject (one) - Parkinson's, (zero) - healthy
	RPDE,D2 - Two nonlinear dynamical complexity measures
	DFA - Signal fractal scaling exponent
	spread1,spread2,PPE - Three nonlinear measures of fundamental frequency variation
	
 Dataset link: https://archive.ics.uci.edu/ml/machine-learning-databases/parkinsons/

* Heart Disease Dataset
  * The dataset consists of 14 columns including the target column and the columns includes:
	age,sex,Chest pain(cp),resting blood pressure,serum cholestoral in mg/dl,fasting blood sugar > 120 mg/dl,resting electrocardiographic results (values 0,1,2),
	maximum heart rate achieved,exercise induced angina, oldpeak = ST depression induced by exercise relative to rest, the slope of the peak exercise ST segment,
	number of major vessels (0-3) colored by flourosopy,thal: 0 = normal; 1 = fixed defect; 2 = reversable defect,target column
 
  Dataset link: https://www.kaggle.com/johnsmith88/heart-disease-dataset

* Thyroid Dataset
  * The dataset consists of 30 columns including the target column and the columns include:

	Attribute Name			Possible Values
	--------------			---------------
	age:				continuous.
	sex:				M, F.
	on thyroxine:			f, t.
	query on thyroxine:		f, t.
	on antithyroid medication:	f, t.
	sick:				f, t.
	pregnant:			f, t.
	thyroid surgery:		f, t.
	I131 treatment:			f, t.
	query hypothyroid:		f, t.
	query hyperthyroid:		f, t.
	lithium:			f, t.
	goitre:				f, t.
	tumor:				f, t.
	hypopituitary:			f, t.
	psych:				f, t.
	TSH measured:			f, t.
	TSH:				continuous.
	T3 measured:			f, t.
	T3:				continuous.
	TT4 measured:			f, t.
	TT4:				continuous.
	T4U measured:			f, t.
	T4U:				continuous.
	FTI measured:			f, t.
	FTI:				continuous.
	TBG measured:			f, t.
	TBG:				continuous.
	referral source:		WEST, STMW, SVHC, SVI, SVHD, other.
	hyperthyroid conditions:        negative,compensated_hypothyroid,primary_hypothyroid,secondary_hypothyroid 
   
    Dataset link: https://www.kaggle.com/yasserhessein/thyroid-disease-data-set

	

Approach:
=================================
* Data Description
  * We will be using Parkinson,Thyroid,Heart disease datasets. This Data set is satisfying our data requirement.

* Data Splitting
  * We split the data here for our train and test data for further uses.

* Data Preprocessing
  * Parkinson Dataset:
    All values are numerical and We have applied the StandardScaler to convert them into a common scale
  
  * Heart Dataset:
    All values are numerical and We have applied the StandardScaler to convert them into a common scale
     
  * Thyroid Dataset:
    There are many Categorical values so We have used LabelEncoding to convert them and then applied the log transformation
  
* Model Training
  * Parkinson Dataset:
    We have trained our dataset with various techniques like logistic regression,Random Forest Classifier, SVC, Decision Tree Classifier,KNN,XGB Classifier.
    Out of all the classifiers Random Forest has given a better accuracy of 93%.

  * Heart Dataset:
    We have trained our dataset with various techniques like logistic regression,Random Forest Classifier, SVC, Decision Tree Classifier,KNN,XGB Classifier.
    Out of all the classifiers Logistic Regression has given a better accuracy of 86%.

  * Thyroid Dataset:
    We have trained our dataset with various techniques like logistic regression,Random Forest Classifier, SVC, Decision Tree Classifier,KNN,XGB Classifier.
    Out of all the classifiers Random Forest has given a better accuracy of 99%.
  
* Model Evaluation
  * Model evaluation done by classification and report was saved to .pkl file

* Model Saving
  * we will save our modelsso that we can use them for prediction purpose.

* Push to app
  * Here we also create our Streamlit app and user interface and integrate our model with Streamlit and UI

* Data from client side for prediction purpose
  * Now our application on cloud is ready for doing prediction. The prediction data which we receive from client side.

* Data processing and Prediction
  * Client data will also go along the same process Data pre-processing and according to that we will predict those data.

  
 Web Deployment
 ===================================
Multiple Disease Predictions Web App : https://multiapp3.herokuapp.com/

Screenshots
====================================
* Parkinson Prediction
**Homepage interface:**

![parkinson-1](https://user-images.githubusercontent.com/24864663/156575981-25ecd06f-f05e-42b8-b6c6-eaffae9cdf73.PNG)
![parkinson-2](https://user-images.githubusercontent.com/24864663/156575969-47e73b10-3963-47fc-af9b-20dd100470d5.PNG)
![parkinson-3](https://user-images.githubusercontent.com/24864663/156575973-b5054bb9-48f1-4de6-b5f3-51535b8debc2.PNG)

**Prediction:**

![parkinson-pred](https://user-images.githubusercontent.com/24864663/156575977-17588eb3-cac4-48fa-ba3f-359abf1d05b7.PNG)

* Heart Disease Prediction
**Homepage interface:**

![heart-1](https://user-images.githubusercontent.com/24864663/156575591-74f72013-537c-432d-b693-e087ba1c3d5a.PNG)
![heart-2](https://user-images.githubusercontent.com/24864663/156575606-e6ba7859-86be-485b-9c1a-8ce33ad00be6.PNG)
![heart-3](https://user-images.githubusercontent.com/24864663/156575564-f44c6d15-2929-42ed-b10b-d01c88fe7f2c.PNG)

**Prediction:**

![heart-pred](https://user-images.githubusercontent.com/24864663/156575572-13da66f1-b93d-41ce-8ee9-5f9f8f2ac452.PNG)

* Thyroid Disease Prediction
**Homepage interface:**

![Thyroid-1](https://user-images.githubusercontent.com/24864663/156576127-de89ae18-24f8-46e7-9dfb-a68b6d4f771e.PNG)
![Thyroid-2](https://user-images.githubusercontent.com/24864663/156576134-4d09372d-515a-496a-9b9d-9d8bf8eec4d9.PNG)

**Prediction:**

![Thyroid-pred](https://user-images.githubusercontent.com/24864663/156576137-96087028-de95-4979-a9fa-7dc57ba4d950.PNG)


**Summary for the Prediction**

By using the radio buttons we can select the model that we want to use

If the user has selected:
	* Parkinson Disease
		The output will be whether the patient has Parkinson disease or not
	* Thyroid Disease
		The output will be whether the patient has Thyroid disease or not
	* Heart Disease
		The output will be whether the patient has Heart disease or not
