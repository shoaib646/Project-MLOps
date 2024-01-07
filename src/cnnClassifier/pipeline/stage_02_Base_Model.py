from cnnClassifier.config.configuration import ConfigurationManager
from cnnClassifier.components.base_Model import BaseModel
from cnnClassifier import logger

STAGE_NAME = "Creating Base Model Stage"


class BaseModelTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        base_model_config = config.get_base_model_config()
        base_model = BaseModel(config=base_model_config)
        base_model.get_base_model()
        base_model.update_base_model()


if __name__ == '__main__':
    try:
        logger.info('----------- %s Started ---------------', STAGE_NAME)
        obj = BaseModelTrainingPipeline()
        obj.main()
        logger.info('----------- %s Ended ---------------', STAGE_NAME)
    except Exception as e:
        logger.error('----------- %s Failed ---------------', STAGE_NAME)
        logger.error('Exception: {e}')
        raise e 