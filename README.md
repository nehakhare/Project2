# Project2
How to Run
ssh user@hadoop-gate-0.eecs.uc.edu

vi mapper.py
vi reducer.py
hadoop jar /usr/hdp/current/hadoop-mapreduce-client/hadoop-streaming.jar -file /home/kharena/mapper.py -mapper mapper.py -file /home/kharena/reducer.py -reducer reducer.py -input /user/tatavag/weather/* -output weather2_output

Results are stored in the output

Filter for abnormalities
missing_on_first_day: Checks to see if there is a -9999 listed in column 4 or has a P in column 5. If either ise true, then data is missing on the first day.
is_tmin_or_tmax: Checks to make sure the data is only a TMIN or TMAX value.
is_quality_reading: If there is any value in column 6, the data is classified as a bad and removed.
source_exists: If a source does not exist in column 7, the data is removed.
