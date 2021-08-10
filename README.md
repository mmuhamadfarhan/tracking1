# assignment 1
from my understanding, the first case, to ensure the ip are protected, we need po to determine what table or column can be share to new db.
To ensure all requirements are follows by guidelines, we need urs(user requirements specification) to ensure all data been pull out have permission from product owners.
Since all solution been parked into Azure, we need to use data factory as ETL tools.The tools can be use in graphical or writing code base on user desire.Plus, data factory is a serverless data integration which means the we wont pay anything if we dont use etl service(pay per use).
For the sap database(on-premise), we need to use etl on-premise(ssis) to transfer to cloud storage. It may need some firewall configuration to ensure connection on premise (vpn) reach ip cloud services.
And for another csv files need to be push to new data warehouse,we can park to cloud storage. Im suggested for data warehouse, we are using azure database sql because it provide serverless compute and storage scale out.

# assignment 2
For the assignment 2, i am using combination of selenium and beautiful soup package.Attach the coding and data as per sharing in files.
I need to design 2 coding python for scrapping (0-k and l-z)because if im using single coding, the respond on the website are getting long will hiccup scrapping process.
After that, the code will merge both file. Please refer to master.py.
Then, another script python(change_deli.py),im design code for change delimeter from ',' to '|'. 
Im using nifi as the tool to schedule flow python, transform the data to sql coding (split text and makesure insert into maximum 100 rows) and then ingest to postgresql db.

Attach also the detail connection postgresql db to setup in nifi.
Database Connection URL:jdbc:postgresql://127.0.0.1:5432/big
Database Driver Class Name:org.postgresql.Driver
Database Driver Location(s):file:////C:/Users/mmuha/Downloads/driver/postgresql-42.2.23.jar
Database User:nifi


Attach the structure db been create in my db.
    "stockcode" character varying,
    "stockshortname" character varying,
    "shariah" character varying,
    "sector" character varying,
    "companyfullname" character varying,
    "marketcap" character varying,
    "lastprice" character varying,
    "peratio" character varying,
    "divyield" character varying,
    "roequity" character varying,
    "dates" character varying

In nifi,
I create 3 progress group to easier the monitoring.
  1.run_python
  2.re-design structure for postgressql(transform csv to sql coding and split text maximum 100 row)
  3.load data into postgresql db.

Attach the script and picture for your reference.
bursa_scrapping0K.py(the code will scrape from website malaysia stock biz company listed 0-K)
bursa_scrappingLZ.py(the code will scrape from website malaysia stock biz company listed L-Z)
master.py(the code will run subsequent coding scrapping bursa_scrapping0K.py & bursa_scrappingLZ.py.After that, merge both csv)
change_deli.py(change delimeter ',' to '|' to ensure minimal impact when convert to sql coding)


GeneralFlow.JPG(General group for this flow assignment)
![GeneralFlow](https://user-images.githubusercontent.com/86910354/128871665-51994a9a-b77f-468c-a4da-10826d4c8d38.JPG)

SchedulerRun.JPG(the scheduler flow for this task is every Monday to Friday; 6.00pm)
![SchedulerRun](https://user-images.githubusercontent.com/86910354/128871723-8331a8df-73d0-4dc3-9d87-7f467cbbe1e1.JPG)

flowrunpython.JPG(process flow been implement in run_python group)
![flowrunpython](https://user-images.githubusercontent.com/86910354/128871789-6444ce97-183d-4ab1-9c60-ce08d8edb4c9.JPG)

flowredesignstructure.JPG(process flow been implement in re-design structure for postgressql group)
![flowredesignstructure](https://user-images.githubusercontent.com/86910354/128871822-9ec76e4b-571e-4b27-8453-a7ad0669809b.JPG)

flowingest.JPG(process flow been implement in load data into postgresql db group)
![flowingest](https://user-images.githubusercontent.com/86910354/128871855-f8fb171d-f8ca-45be-84d0-6b36119f1c1f.JPG)
