from src.components.data_ingestion import DataIngestion
from src.components.data_transformation import DataTransformation

data_ingestion = DataIngestion()
data_transformation = DataTransformation()

data_ingestion.initiate_data_ingestion()
data_transformation.get_data_transformation_object()

