from cnnClassifier.config.configuration import ConfigurationManager
from cnnClassifier.components.callbacks import Callbacks
from cnnClassifier.components.training import Training
from cnnClassifier import logger

STAGE_NAME = "Training Stage"


class ModelTrainingPipeline:
    def __init__(self):
        pass

    def main(self):

        config = ConfigurationManager()
        callbacks_config = config.get_callback_config()
        callbacks = Callbacks(config=callbacks_config)
        callbacks_list = callbacks.get_tb_ckpt_callbacks()


        training_config = config.get_training_config()
        training = Training(config=training_config)
        training.get_base_model()
        training.train_valid_generator()
        training.train(
            callback_list=callbacks_list
        )


if __name__ == '__main__':
    try:
        logger.info('----------- %s Started ---------------', STAGE_NAME)
        obj = ModelTrainingPipeline()
        obj.main()
        logger.info('----------- %s Ended ---------------', STAGE_NAME)
    except Exception as e:
        logger.error('----------- %s Failed ---------------', STAGE_NAME)
        logger.error('Exception: {e}')
        raise e