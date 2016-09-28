from ..utils.errors import IndicoError
from ..utils.decorators import detect_batch_decorator

MULTIAPI_NOT_SUPPORTED = [
    'relevance',
    'personas'
]

def multi(data, datatype, apis, accepted_apis, batch=False,**kwargs):
    """
    Helper to make multi requests of different types.

    :param data: Data to be sent in API request
    :param datatype: String type of API request
    :param apis: List of apis to use.
    :param batch: Is this a batch request?
    :rtype: Dictionary of api responses
    """
    # Client side api name checking - strictly only accept func name api
    invalid_apis = [api for api in apis if api not in accepted_apis or api in MULTIAPI_NOT_SUPPORTED]
    if invalid_apis:
        raise IndicoError(
            "The following are not valid %s APIs: %s. Please reference the available APIs below:\n%s"
            % (datatype, ", ".join(invalid_apis),  ", ".join(accepted_apis.keys()))
        )

    # Convert client api names to server names before sending request
    cloud = kwargs.pop("cloud", None)
    api_key = kwargs.pop('api_key', None)

    api_results = {}
    for api in apis:
        api_results[api] = accepted_apis[api](data, cloud=cloud, api_key=api_key, batch=batch, **kwargs)

    if not batch:
        return api_results

    batch_results = []
    for i in xrange(len(data)):
        batch_results.append({api: result[i] for api, result in api_results.iteritems()})
    return batch_results
