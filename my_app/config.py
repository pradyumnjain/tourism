INTENT_CLASSIFIER_CONFIG = {
    'model_type': 'text',
    'model_settings': {
        'classifier_type': 'dtree'
    },
    'param_selection': {
        'type': 'k-fold',
        'k': 10,
        'grid': {
            'max_features': ['log2', 'sqrt', 0.01, 0.1]
        },
    },
    "features": {
        "exact": {},
    }
}

DOMAIN_CLASSIFIER_CONFIG = {
    'model_type': 'text',
    'model_settings': {
        'classifier_type': 'logreg'
    },
    'param_selection': {
        'type': 'k-fold',
        'k': 10,
        'grid': {
            'fit_intercept': [True, False],
            'C': [10, 100, 1000, 10000, 100000]
        },
    },
    'features': {
        "bag-of-words": {
            "lengths": [1, 2]
        },
        "edge-ngrams": {"lengths": [1, 2]},
        "in-gaz": {},
        "exact": {"scaling": 10},
        "gaz-freq": {},
        "freq": {"bins": 5}
    }
}

# TEST_ENTITY_RECOGNIZER_CONFIG = {
#     'model_type': 'tagger',
#     'label_type': 'entities',
#     'model_settings': {
#         'classifier_type': 'memm',
#         'tag_scheme': 'IOB',
#         'feature_scaler': 'max-abs'
#     },
#     'params': {
#         'penalty': 'l1',
#         'C': 50
#     },
#     'features': {
#         'bag-of-words-seq': {
#             'ngram_lengths_to_start_positions': {
#                 1: [-2, -1, 0, 1, 2],
#                 2: [-2, -1, 0, 1]
#             }
#         },
#         'in-gaz-span-seq': {},
#         'sys-candidates-seq': {
#             'start_positions': [-1, 0, 1]
#         },
#         'enable-stemming': True
#     },
#     'train_label_set': 'testtrain.*\.txt',  # noqa: W605
#     'test_label_set': 'testtrain.*\.txt'  # noqa: W605
# }


# def get_entity_recognizer_config(domain, intent):
#     if domain == 'store_info' and intent == 'get_store_hours':
#         return TEST_ENTITY_RECOGNIZER_CONFIG
#     return ENTITY_RECOGNIZER_CONFIG
