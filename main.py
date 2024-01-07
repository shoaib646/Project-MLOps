from cnnClassifier import logger
from cnnClassifier.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from cnnClassifier.pipeline.stage_02_Base_Model import BaseModelTrainingPipeline
from cnnClassifier.pipeline.stage_03_training import ModelTrainingPipeline
from cnnClassifier.pipeline.stage_04_evaluation import EvaluationPipeline

STAGE_NAME = "Data Ingestion Stage"


try:
    logger.info('----------- %s Started ---------------', STAGE_NAME)
    obj = DataIngestionTrainingPipeline()
    obj.main()
    logger.info('----------- %s Ended ---------------', STAGE_NAME)
except Exception as e:
    logger.error('----------- %s Failed ---------------', STAGE_NAME)
    logger.error('Exception: {e}')
    raise e 


STAGE_NAME = "Base Model Stage"


try:
    logger.info("*************************************************")
    logger.info('----------- %s Started ---------------', STAGE_NAME)
    obj = BaseModelTrainingPipeline()
    obj.main()
    logger.info('----------- %s Ended ---------------', STAGE_NAME)
except Exception as e:
    logger.error('----------- %s Failed ---------------', STAGE_NAME)
    logger.error('Exception: {e}')
    raise e 


STAGE_NAME = "Training Stage"

try:
    logger.info("*************************************************")
    logger.info('----------- %s Started ---------------', STAGE_NAME)
    obj = ModelTrainingPipeline()
    obj.main()
    logger.info('----------- %s Ended ---------------', STAGE_NAME)
except Exception as e:
    logger.error('----------- %s Failed ---------------', STAGE_NAME)
    logger.error('Exception: {e}')
    raise e


STAGE_NAME = "Evaluation Stage"

try:
    logger.info('----------- %s Started ---------------', STAGE_NAME)
    obj = EvaluationPipeline()
    obj.main()
    logger.info('----------- %s Ended ---------------', STAGE_NAME)
except Exception as e:
    logger.error('----------- %s Failed ---------------', STAGE_NAME)
    logger.error('Exception: {e}')
    raise e