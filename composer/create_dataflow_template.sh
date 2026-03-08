python3 wordcount.py \
    --runner DataflowRunner \
    --project gcp-data-engineer-curso05 \
    --region us-central1 \
    --staging_location gs://gcs-bucket-curso05/staging \
    --temp_location gs://gcs-bucket-curso05/temp \
    --template_location gs://gcs-bucket-curso05/templates/wordcount_template

    pip install apache-beam == 2.48.0
    pip install protobuf == 6.28.0