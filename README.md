## NSTDProject
# Project Model
- First started by exploring the data to get insights of how the data looks by checking the summary of the data and description for each column(mean, median, quartiles, etc), checked for the missing numbers to which there was none, and then did the value count of variables for each column . 
- Cleaning and processing of the data followed where I focused on the review_text column and dropping some columns which of no great use to the model. 
- I dropped the timestamp column, user_id column, and the review_id column. 
- Under the review_text column, I removed the special characters and stopwords, then joined the English words again and made all letters to be lower case. 
- I replaced all the reviews with numbers since there were only 14 of them repeated on different encounters. 
- On the ratings column, I changed the rates to sentiments where 1 and 2 were for negative, 3 for neutral, 4 and 5 for positive, and this column will be the target column using the product_id and review_text columns as independent variables. 
- For the model, I described my x and y variables, then split the data to train set and test set using the 80/20 scale. I described the mode, fitted it(train), did prediction, and then evaluated it using four metrices, accuracy, precision, recall, and f1 sore. 

# App Deployment
- The API backend worked well, it was able to take in inputs and give predictions based on the values given to it. 
- The frontend did not work well because it kept on reading from the backend and was not linking well with the html file. 
- It was able to take in values as inputs by giving a dropdown where one can choose which product id they will be a rating or giving a review and then give a review, but it failed to predict the sentiments. 
- The API is run by the localhost link Sneaker Predict – Django REST framework.
- Docker managed to build images of the API and the model, and also containerized them but it failed to run the application as it could not access the dataset for the model created. 
- And I managed to create necessary platforms in the aws cloud but failed to push images and deploy the API because aws got an error about improper configurations on docker. 
