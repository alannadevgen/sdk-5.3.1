"""
    Tenant API

    Tenant API  # noqa: E501

    The version of the OpenAPI document: 0.0.1
    Contact: abc@layer.fr
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401
import sys  # noqa: F401

from graalsystems.api_client import ApiClient, Endpoint as _Endpoint
from graalsystems.model_utils import (  # noqa: F401
    check_allowed_values,
    check_validations,
    date,
    datetime,
    file_type,
    none_type,
    validate_and_convert_types
)
from graalsystems.model.error import Error
from graalsystems.model.file_or_directory import FileOrDirectory


class DataApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client
        self.delete_files_endpoint = _Endpoint(
            settings={
                'response_type': None,
                'auth': [
                    'internal'
                ],
                'endpoint_path': '/buckets/{bucketId}/data',
                'operation_id': 'delete_files',
                'http_method': 'DELETE',
                'servers': None,
            },
            params_map={
                'all': [
                    'x_tenant',
                    'bucket_id',
                    'path',
                ],
                'required': [
                    'x_tenant',
                    'bucket_id',
                    'path',
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
                    'x_tenant':
                        (str,),
                    'bucket_id':
                        (str,),
                    'path':
                        ([str],),
                },
                'attribute_map': {
                    'x_tenant': 'X-Tenant',
                    'bucket_id': 'bucketId',
                    'path': 'path',
                },
                'location_map': {
                    'x_tenant': 'header',
                    'bucket_id': 'path',
                    'path': 'query',
                },
                'collection_format_map': {
                    'path': 'multi',
                }
            },
            headers_map={
                'accept': [
                    'application/vnd.graal.systems.v1.error+json'
                ],
                'content_type': [],
            },
            api_client=api_client
        )
        self.download_file_endpoint = _Endpoint(
            settings={
                'response_type': (file_type,),
                'auth': [
                    'internal'
                ],
                'endpoint_path': '/buckets/{bucketId}/data?download',
                'operation_id': 'download_file',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'x_tenant',
                    'bucket_id',
                    'path',
                ],
                'required': [
                    'x_tenant',
                    'bucket_id',
                    'path',
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
                    'x_tenant':
                        (str,),
                    'bucket_id':
                        (str,),
                    'path':
                        (str,),
                },
                'attribute_map': {
                    'x_tenant': 'X-Tenant',
                    'bucket_id': 'bucketId',
                    'path': 'path',
                },
                'location_map': {
                    'x_tenant': 'header',
                    'bucket_id': 'path',
                    'path': 'query',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/octet-stream',
                    'application/vnd.graal.systems.v1.error+json'
                ],
                'content_type': [],
            },
            api_client=api_client
        )
        self.get_data_files_endpoint = _Endpoint(
            settings={
                'response_type': ([FileOrDirectory],),
                'auth': [
                    'internal'
                ],
                'endpoint_path': '/buckets/{bucketId}/data',
                'operation_id': 'get_data_files',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'x_tenant',
                    'bucket_id',
                    'path',
                ],
                'required': [
                    'x_tenant',
                    'bucket_id',
                    'path',
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
                    'x_tenant':
                        (str,),
                    'bucket_id':
                        (str,),
                    'path':
                        (str,),
                },
                'attribute_map': {
                    'x_tenant': 'X-Tenant',
                    'bucket_id': 'bucketId',
                    'path': 'path',
                },
                'location_map': {
                    'x_tenant': 'header',
                    'bucket_id': 'path',
                    'path': 'query',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/vnd.graal.systems.v1.file+json',
                    'application/vnd.graal.systems.v1.error+json'
                ],
                'content_type': [],
            },
            api_client=api_client
        )
        self.upload_file_endpoint = _Endpoint(
            settings={
                'response_type': None,
                'auth': [
                    'internal'
                ],
                'endpoint_path': '/buckets/{bucketId}/data',
                'operation_id': 'upload_file',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'x_tenant',
                    'bucket_id',
                    'path',
                    'filename',
                ],
                'required': [
                    'x_tenant',
                    'bucket_id',
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
                    'x_tenant':
                        (str,),
                    'bucket_id':
                        (str,),
                    'path':
                        (str,),
                    'filename':
                        ([file_type],),
                },
                'attribute_map': {
                    'x_tenant': 'X-Tenant',
                    'bucket_id': 'bucketId',
                    'path': 'path',
                    'filename': 'filename',
                },
                'location_map': {
                    'x_tenant': 'header',
                    'bucket_id': 'path',
                    'path': 'query',
                    'filename': 'form',
                },
                'collection_format_map': {
                    'filename': 'csv',
                }
            },
            headers_map={
                'accept': [],
                'content_type': [
                    'multipart/form-data'
                ]
            },
            api_client=api_client
        )

    def delete_files(
        self,
        x_tenant,
        bucket_id,
        path,
        **kwargs
    ):
        """Delete files  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.delete_files(x_tenant, bucket_id, path, async_req=True)
        >>> result = thread.get()

        Args:
            x_tenant (str):
            bucket_id (str): Id of the bucket
            path ([str]): path

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
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            async_req (bool): execute request asynchronously

        Returns:
            None
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
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['x_tenant'] = \
            x_tenant
        kwargs['bucket_id'] = \
            bucket_id
        kwargs['path'] = \
            path
        return self.delete_files_endpoint.call_with_http_info(**kwargs)

    def download_file(
        self,
        x_tenant,
        bucket_id,
        path,
        **kwargs
    ):
        """Download data by path  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.download_file(x_tenant, bucket_id, path, async_req=True)
        >>> result = thread.get()

        Args:
            x_tenant (str):
            bucket_id (str): Id of the bucket
            path (str): path

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
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            async_req (bool): execute request asynchronously

        Returns:
            file_type
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
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['x_tenant'] = \
            x_tenant
        kwargs['bucket_id'] = \
            bucket_id
        kwargs['path'] = \
            path
        return self.download_file_endpoint.call_with_http_info(**kwargs)

    def get_data_files(
        self,
        x_tenant,
        bucket_id,
        path,
        **kwargs
    ):
        """Get files  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_data_files(x_tenant, bucket_id, path, async_req=True)
        >>> result = thread.get()

        Args:
            x_tenant (str):
            bucket_id (str): Id of the bucket
            path (str): path

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
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            async_req (bool): execute request asynchronously

        Returns:
            [FileOrDirectory]
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
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['x_tenant'] = \
            x_tenant
        kwargs['bucket_id'] = \
            bucket_id
        kwargs['path'] = \
            path
        return self.get_data_files_endpoint.call_with_http_info(**kwargs)

    def upload_file(
        self,
        x_tenant,
        bucket_id,
        **kwargs
    ):
        """Upload a file  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.upload_file(x_tenant, bucket_id, async_req=True)
        >>> result = thread.get()

        Args:
            x_tenant (str):
            bucket_id (str): Id of the bucket

        Keyword Args:
            path (str): path. [optional]
            filename ([file_type]): [optional]
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
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            async_req (bool): execute request asynchronously

        Returns:
            None
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
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['x_tenant'] = \
            x_tenant
        kwargs['bucket_id'] = \
            bucket_id
        return self.upload_file_endpoint.call_with_http_info(**kwargs)

