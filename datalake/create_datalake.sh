# PASO 1: Crear un bucket de Cloud Storage para almacenar los datos del datalake

gsutil mb -l US gs://ecommerce-datalake-tp/

# PASO 2: Subir archivos CSV de ejemplo al bucket de Cloud Storage

# bash 
# Copy code
gsutil cp users.csv gs://ecommerce-datalake-tp/
gsutil cp orders.csv gs://ecommerce-datalake-tp/
