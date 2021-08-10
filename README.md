# HR-AWARDS-PREDICTION
This Dataset consist of awards prediction by an employee

 

                                                                    PROJECT   NAME-
                                                                EMPLOYEE AWARD PREDICTOR


Project Title


  - This project is an HR Analysis for a company which have various Department

   - This project may help hr of company to predict whether to give an particular employee award on basis of different factos as mention in the above ipynb file and                  helping  them to see the various insight of the dataset which is difficult to see by Raw dataset



Deployment
        
        To deploy this project run

        streamlit run hr_prediction.py


        
        
CONTENT-

    1]PURPOSE 

    2]WORKDONE 

    3]CONCLUSION 

    4]RESULT


PURPOSE –

    1] TO Ease in work of department of allocating the awards

    2] TO give them an short overview of the whole company EmployeeStructure

    3] To have an Look which Factor are Important for Promotion or salary Hike 

WORK DONE-

    A] EDA  ( Handling of missingvalue, Balancing the dataset )

    B] VISUALISATION 

    C] BUILDING THE MODEL

    D] HYPER PARAMETER TUNING OF BEST ACCURACY MODELS


CONCLUSION-





    A] PREPROCESSING

        1] we can determine that the mean average age in data set is 60 years

        2] Maximum  length of service is of 34 years

        3]  shape of dataset is (23490, 13)

        4] That data is highly scatter and imbalanced

    B] VISUALISATION

        1] There are almost 9 department out of whcich Sales & Marketing have maximum count of people in ti followed by operations

        2] We came to conclusion that Sales & Marketing have won most of tha award

        3] There are almost 14k+ candidate having Bacherlor's degree while 6k+ having master degree

        4] The most Educated candidate are from Sales & Marketing as they have to deal with different customer base  

        5] There are almost 16k candidate who have received training once so company's hr can take this into consideration while hiring the candidiate

        6] The rating is also and imp factor in term of hr candidate selection as this tell how an employee is handling his work

        7] There are more then 194 people having more then 20 years of exp which company can hire for main managing positions

    C] BUILDING MODEL

       -we can conclude that  Model was imbalanced and after balancing the dataset the accuracy that was obtained was
        highest for random forest,Decision Tree,Knn models

              Accuracy  Before all the hyperparameter Tuning for K NEIGHBOR CLASSIFIER , RANDOM FOREST, DECISION  TREE

                      ACCURACY[K NEIGHBOR CLASSIFIER]==91.45
                      ACCURACY[RANDOM FOREST]==97.21
                      ACCURACY[DECISION  TREE]==95.62
                      ACCURACY[GRADIENT BOOSTING]==73.46

              After hyperparameter Tuning for K NEIGHBOR CLASSIFIER , DECISION  TREE

                      ACCURACY[K NEIGHBOR CLASSIFIER]==95.36
                      ACCURACY[DECISION  TREE]==95.74
                  
                  
 RESULT 
  
    1] From above accuracycharts we can conclude that RANDOM FOREST CLASSIFIER gave the maximum accuracy

    2] Overall Accuracy of Model was 97.56% 

       
       
Lessons Learned

    1] handling imbalanced dataset

    2] Using different model to find the best fit model for it and inorder to improve it accuracy the different hyperparameter Tuning
