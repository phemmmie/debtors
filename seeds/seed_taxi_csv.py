import dbt.clients as clients

from dbt.adapters.pandas import PandasAdapter

s3_adapter = clients.get_adapter('s3')
db_adapter = clients.get_adapter('databricks')

source_table = s3_adapter.table('raw_taxi_trips.csv', 's3://bronzetaxi/raw_taxi_trips.csv')
target_table = db_adapter.table('taxi_data', 'pullet')

# Load the data from the S3 CSV file into the Databricks table.
source_table.to_target(target_table, method='write_truncate')