# Data-Group-Challenge



**The high level problem**

In the file Data_Pipeline_Architecture.pdf I propose an architecture to solve the problem encountered by the tech lead of the data product Squad.

Customer Behavior Data Visualization:

The above architecture is showing with QuickSight connected to the data warehouse in RedShift and the processed data in S3, Analyst can be able to make their own reports with data that comes from all sources  

Risk Assessment for Home Buyers seeking a Mortgage: 

The above architecture also shows that when applying ETL process on raw data using Glue and the stored the features in RedShift, data scientist can ingest the data to the machine learning models using SageMaker.

Fraud Monitoring:

With this architecture Data scientist can develop fraud detection algorithm by ingesting data either from the warehouse in RedShift or directely from the JSON API and the S3 bucket processed data. 




**The low level problem**

Kindly find my solution in the file Paths_in_DAG.py containing the code I wrote.  




**The Scenario Problem**

Reaction 1 : The other team : The first response of the other squad will be they have troubles of merging the branches of the code written by their developpers to their mocks in staging and they need time to check that all the branches are well merged in the same version of the code.

Me : I will recommend to the team to use CI/CD pipelines instead of mocks in order to ensure that the code changes are well commited and centralize in the same repository.     

Reaction 2 : The tech lead of the other team will say they have the neccessaries to deal will their issue and so they don’t need to change the method in other to hundle the situation
   
Me : I will ask them to suggest an efficient and quick solution in other deal with the situation  

Reaction 3: The tech lead will say to give them the time to find an efficient solution. This solution could be inefficient or temporary due to the imergency.

Me : My team will repport the problem to a higher management level with the discontentment of our team and aware the director of the financial cost to the company of not adressing this issue.
