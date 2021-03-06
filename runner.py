# coding=utf-8
from utils.script_functions import set_parameter
from os import system

if __name__ == "__main__":
    parameters_filepath = "parameters.ini"

    # Keep as all 5
    train_methods = ['dfgsm_k', 'rfgsm_k', 'natural', 'grosse', 'topkr']
    evasion_methods = ['dfgsm_k', 'rfgsm_k', 'natural', 'grosse', 'topkr']
    # evasion_methods = []
    

    for train_method in train_methods:

        set_parameter(parameters_filepath, "general", "train_model_from_scratch", "True")
        set_parameter(parameters_filepath, "general", "load_model_weights", "False")
        set_parameter(parameters_filepath, "general", "experiment_suffix", "run_experiments")

        set_parameter(parameters_filepath, "general", "training_method", train_method)
        set_parameter(parameters_filepath, "general", "evasion_method", train_method)
        system("source activate nn_mal;python DAMROC.py")

    for train_method in train_methods:
        model_filepath = "./helper_files/[training:{train_meth}|evasion:{train_meth}]_run_experiments-model.pt".format(
            train_meth=train_method)

        set_parameter(parameters_filepath, "general", "training_method", train_method)
        set_parameter(parameters_filepath, "general", "train_model_from_scratch", "False")
        set_parameter(parameters_filepath, "general", "load_model_weights", "True")
        set_parameter(parameters_filepath, "general", "model_weights_path", model_filepath)

        for evasion_method in evasion_methods:
            set_parameter(parameters_filepath, "general", "evasion_method", evasion_method)
            system("source activate nn_mal;python DAMROC.py")
