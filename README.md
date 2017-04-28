### Hadoop_Map_Reduce     

Using the Hadoop streaming API built mapper and reducer scripts that analyze the data and yield summary counts for each vehicle that
describe the total count, per vehicle type, that the vehicle type was involved in an incident. If the same
type of vehicle was involved more than once in an incident, the vehicle is counted twice for the purpose of the
summary statistic. 

Please refer to * https://data.cityofnewyork.us/Public-Safety/NYPD-Motor-VehicleCollisions/h9gi-nx95 *
for more information about the dataset.

Hadoop Map-Reduce program in python to find count of different types of vehicles in given dataset.      
1. Use mapper.py and reducer.py to run mapreduce on hadoop cluster.     
2. Use the below commands:     
     
### *To run mapreduce on hadoop cluster*     
      
 *_ hadoop jar /opt/hadoop-2.7.1/share/hadoop/tools/lib/hadoop-streaming-2.7.1.jar -file /home/tetaliah/mapper.py    -mapper /home/tetaliah/mapper.py -file /home/tetaliah/reducer.py   -reducer /home/tetaliah/reducer.py -input /data/nyc/nyc-traffic.csv  -output /user/tetaliah/nyc_output _*     
####In the above command,      
 1. mapper file is mapper.py     
 2. reducer file is reducer.py     
 3. input dataset is nyc-traffic.csv #which is in hadoop file system      
 4. output is stored in nyc_output directory in hadoop file system     
     
##To get the file from hadoop file system to your local system     
 * hadoop fs -get <filename in HDFS> *     
      
##To put the file from your local file system to HDFS     
 * hadoop fs -put <filename in your local system> *     
      
 ##To list all the files in HDFS       
  * hadoop fs -ls *
