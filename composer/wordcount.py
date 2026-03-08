import apache_beam as beam
from apache_beam.options.pipeline_options import PipelineOptions

def run():
    #Configuracion del pipeline
    options = PipelineOptions(
        runner='DataflowRunner',  # Cambia a 'DirectRunner' para local. Con DataFlowRunner se ejecuta lo mismo pero en lugar de ejecutarse localmente, se ejecuta en la nube de Google Cloud Dataflow.
        project='gcp-data-engineer-curso05',  # Reemplaza con tu ID de proyecto
        region = 'us-central1',
        temp_location='gs://gcs-bucket-curso05/temp',  # Reemplaza con tu bucket de Cloud Storage
    )

    with beam.Pipeline(options=options) as p:
        (
            p
            | "Leer archivo" >> beam.io.ReadFromText('gs://dataflow-samples/shakespeare/kinglear.txt')  # Reemplaza con la ruta de tu archivo de entrada
            | "Separar palabras" >> beam.FlatMap(lambda line: line.split())
            | "Contar palabras" >> beam.combiners.Count.PerElement()
            | "Guardar resultados" >> beam.io.WriteToText('gs://gcs-bucket-curso05/output/wordcount')  # Reemplaza con la ruta de tu archivo de salida
        )

    result = p.run()
    result.wait_until_finish()
    
    print("Pipeline ejecutado exitosamente.")
if __name__ == "__main__":
    run()
