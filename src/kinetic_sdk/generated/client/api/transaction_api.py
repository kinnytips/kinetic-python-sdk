"""
    @kin-kinetic/api

    The OpenAPI definition of the Kinetic API  # noqa: E501

    The version of the OpenAPI document: 1.0.0-rc.12
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401
import sys  # noqa: F401

from kinetic_sdk.generated.client.api_client import ApiClient, Endpoint as _Endpoint
from kinetic_sdk.generated.client.model_utils import (  # noqa: F401
    check_allowed_values,
    check_validations,
    date,
    datetime,
    file_type,
    none_type,
    validate_and_convert_types
)
from kinetic_sdk.generated.client.model.commitment import Commitment
from kinetic_sdk.generated.client.model.get_transaction_response import GetTransactionResponse
from kinetic_sdk.generated.client.model.latest_blockhash_response import LatestBlockhashResponse
from kinetic_sdk.generated.client.model.make_transfer_request import MakeTransferRequest
from kinetic_sdk.generated.client.model.minimum_rent_exemption_balance_response import MinimumRentExemptionBalanceResponse
from kinetic_sdk.generated.client.model.transaction import Transaction


class TransactionApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client
        self.get_latest_blockhash_endpoint = _Endpoint(
            settings={
                'response_type': (LatestBlockhashResponse,),
                'auth': [],
                'endpoint_path': '/api/transaction/latest-blockhash/{environment}/{index}',
                'operation_id': 'get_latest_blockhash',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'environment',
                    'index',
                ],
                'required': [
                    'environment',
                    'index',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'environment':
                        (str,),
                    'index':
                        (int,),
                },
                'attribute_map': {
                    'environment': 'environment',
                    'index': 'index',
                },
                'location_map': {
                    'environment': 'path',
                    'index': 'path',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client
        )
        self.get_minimum_rent_exemption_balance_endpoint = _Endpoint(
            settings={
                'response_type': (MinimumRentExemptionBalanceResponse,),
                'auth': [],
                'endpoint_path': '/api/transaction/minimum-rent-exemption-balance/{environment}/{index}',
                'operation_id': 'get_minimum_rent_exemption_balance',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'environment',
                    'index',
                    'data_length',
                ],
                'required': [
                    'environment',
                    'index',
                    'data_length',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'environment':
                        (str,),
                    'index':
                        (int,),
                    'data_length':
                        (int,),
                },
                'attribute_map': {
                    'environment': 'environment',
                    'index': 'index',
                    'data_length': 'dataLength',
                },
                'location_map': {
                    'environment': 'path',
                    'index': 'path',
                    'data_length': 'query',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client
        )
        self.get_transaction_endpoint = _Endpoint(
            settings={
                'response_type': (GetTransactionResponse,),
                'auth': [],
                'endpoint_path': '/api/transaction/transaction/{environment}/{index}/{signature}',
                'operation_id': 'get_transaction',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'environment',
                    'index',
                    'signature',
                    'commitment',
                ],
                'required': [
                    'environment',
                    'index',
                    'signature',
                    'commitment',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'environment':
                        (str,),
                    'index':
                        (int,),
                    'signature':
                        (str,),
                    'commitment':
                        (Commitment,),
                },
                'attribute_map': {
                    'environment': 'environment',
                    'index': 'index',
                    'signature': 'signature',
                    'commitment': 'commitment',
                },
                'location_map': {
                    'environment': 'path',
                    'index': 'path',
                    'signature': 'path',
                    'commitment': 'query',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client
        )
        self.make_transfer_endpoint = _Endpoint(
            settings={
                'response_type': (Transaction,),
                'auth': [],
                'endpoint_path': '/api/transaction/make-transfer',
                'operation_id': 'make_transfer',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'make_transfer_request',
                ],
                'required': [
                    'make_transfer_request',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'make_transfer_request':
                        (MakeTransferRequest,),
                },
                'attribute_map': {
                },
                'location_map': {
                    'make_transfer_request': 'body',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [
                    'application/json'
                ]
            },
            api_client=api_client
        )

    def get_latest_blockhash(
        self,
        environment,
        index,
        **kwargs
    ):
        """  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_latest_blockhash(environment, index, async_req=True)
        >>> result = thread.get()

        Args:
            environment (str):
            index (int):

        Keyword Args:
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            _request_auths (list): set to override the auth_settings for an a single
                request; this effectively ignores the authentication
                in the spec for a single request.
                Default is None
            async_req (bool): execute request asynchronously

        Returns:
            LatestBlockhashResponse
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['_request_auths'] = kwargs.get('_request_auths', None)
        kwargs['environment'] = \
            environment
        kwargs['index'] = \
            index
        return self.get_latest_blockhash_endpoint.call_with_http_info(**kwargs)

    def get_minimum_rent_exemption_balance(
        self,
        environment,
        index,
        data_length,
        **kwargs
    ):
        """  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_minimum_rent_exemption_balance(environment, index, data_length, async_req=True)
        >>> result = thread.get()

        Args:
            environment (str):
            index (int):
            data_length (int):

        Keyword Args:
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            _request_auths (list): set to override the auth_settings for an a single
                request; this effectively ignores the authentication
                in the spec for a single request.
                Default is None
            async_req (bool): execute request asynchronously

        Returns:
            MinimumRentExemptionBalanceResponse
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['_request_auths'] = kwargs.get('_request_auths', None)
        kwargs['environment'] = \
            environment
        kwargs['index'] = \
            index
        kwargs['data_length'] = \
            data_length
        return self.get_minimum_rent_exemption_balance_endpoint.call_with_http_info(**kwargs)

    def get_transaction(
        self,
        environment,
        index,
        signature,
        commitment,
        **kwargs
    ):
        """  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_transaction(environment, index, signature, commitment, async_req=True)
        >>> result = thread.get()

        Args:
            environment (str):
            index (int):
            signature (str):
            commitment (Commitment):

        Keyword Args:
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            _request_auths (list): set to override the auth_settings for an a single
                request; this effectively ignores the authentication
                in the spec for a single request.
                Default is None
            async_req (bool): execute request asynchronously

        Returns:
            GetTransactionResponse
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['_request_auths'] = kwargs.get('_request_auths', None)
        kwargs['environment'] = \
            environment
        kwargs['index'] = \
            index
        kwargs['signature'] = \
            signature
        kwargs['commitment'] = \
            commitment
        return self.get_transaction_endpoint.call_with_http_info(**kwargs)

    def make_transfer(
        self,
        make_transfer_request,
        **kwargs
    ):
        """  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.make_transfer(make_transfer_request, async_req=True)
        >>> result = thread.get()

        Args:
            make_transfer_request (MakeTransferRequest):

        Keyword Args:
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            _request_auths (list): set to override the auth_settings for an a single
                request; this effectively ignores the authentication
                in the spec for a single request.
                Default is None
            async_req (bool): execute request asynchronously

        Returns:
            Transaction
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['_request_auths'] = kwargs.get('_request_auths', None)
        kwargs['make_transfer_request'] = \
            make_transfer_request
        return self.make_transfer_endpoint.call_with_http_info(**kwargs)

