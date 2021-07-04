# assignment 1
from my understanding, the first case, to ensure the ip are protected, we need po to determine what table or column can be share to new db.
To ensure all requirements are follows by guidelines, we need urs(user requirements specification) to ensure all data been pull out have permission from product owners.
Since all solution been parked into Azure, we need to use data factory as ETL tools.The tools can be use in graphical or writing code base on user desire.Plus, data factory is a serverless data integration which means the we wont pay anything if we dont use etl service(pay per use).
For the sap database(on-premise), we need to use etl on-premise(ssis) to transfer to cloud storage. It may need some firewall configuration to ensure connection on premise (vpn) reach ip cloud services.
And for another csv files need to be push to new data warehouse,we can park to cloud storage. Im suggested for data warehouse, we are using azure database sql because it provide serverless compute and storage scale out.

# assignment 2
For the assignment 2, i am using combination of selenium and beautiful soup package. Unfortunately, i cant scrapping 
Market Cap
,Last Price
,Price–earnings ratio (PE)
,Dividend yield (DY)
,Return on equity (ROE) due to i had problem with using
Xpath. And im using windows task scheduler to manage the python. Due to my laptop cant install postgresdb(laptop office-need team IT to install it-i dont have permission),
so,i just putting the coding using sqlalchemy package.

Scrappingbursa.csv- data bursa has been scrape
bursa_scrapping.ipynb - coding been use in jupyter notebook (development)
bursa_scrapping.py- coding scraping without script ingestion postgres
bursa_scrapping_postgressql.py- coding scraping with script ingestion postgres

