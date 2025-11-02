##Sum of First 10 Natural Numbers
sum=0
for i in range(1,11):
    sum = sum + i 
    print(sum)



git config --global user.name "sampathk-data"

git config --global user.email "sampath.kodisherla03@gmail.com"


bq load --source_format=.csv --autodetect DATASET.TABLE PATH_TO_SOURCE [SCHEMA_DEFINITION]
bq load --source_format=CSV --autodetect --skip_leading_rows=1 my_dataset.my_table data.csv


bq load \
    --source_format=CSV \
    --autodetect \
    dataset_1.cust_1 \
    gs://new-b43-bucket-2/customer_details.csv