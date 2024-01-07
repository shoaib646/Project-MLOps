from cnnClassifier.config.configuration import ConfigurationManager
from cnnClassifier.components.evaluation import Evaluation
from cnnClassifier import logger




STAGE_NAME = "Evaluation stage"


class EvaluationPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        val_config = config.get_validation_config()
        evaluation = Evaluation(val_config)
        evaluation.evaluation()
        evaluation.save_score()



if __name__ == '__main__':
    try:
        logger.info('----------- %s Started ---------------', STAGE_NAME)
        obj = EvaluationPipeline()
        obj.main()
        logger.info('----------- %s Ended ---------------', STAGE_NAME)
    except Exception as e:
        logger.error('----------- %s Failed ---------------', STAGE_NAME)
        logger.error('Exception: {e}')
        raise e