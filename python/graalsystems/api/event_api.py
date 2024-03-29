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
from graalsystems.model.event import Event


class EventApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client
        self.create_event_for_job_and_run_endpoint = _Endpoint(
            settings={
                'response_type': (Event,),
                'auth': [
                    'internal'
                ],
                'endpoint_path': '/jobs/{jobId}/runs/{runId}/events',
                'operation_id': 'create_event_for_job_and_run',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'x_tenant',
                    'job_id',
                    'run_id',
                    'event',
                ],
                'required': [
                    'x_tenant',
                    'job_id',
                    'run_id',
                    'event',
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
                    'job_id':
                        (str,),
                    'run_id':
                        (str,),
                    'event':
                        (Event,),
                },
                'attribute_map': {
                    'x_tenant': 'X-Tenant',
                    'job_id': 'jobId',
                    'run_id': 'runId',
                },
                'location_map': {
                    'x_tenant': 'header',
                    'job_id': 'path',
                    'run_id': 'path',
                    'event': 'body',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/vnd.graal.systems.v1.event+json',
                    'application/vnd.graal.systems.v1.error+json'
                ],
                'content_type': [
                    'application/vnd.graal.systems.v1.event+json'
                ]
            },
            api_client=api_client
        )
        self.create_event_for_workflow_and_run_endpoint = _Endpoint(
            settings={
                'response_type': (Event,),
                'auth': [
                    'internal'
                ],
                'endpoint_path': '/workflows/{workflowId}/runs/{runId}/events',
                'operation_id': 'create_event_for_workflow_and_run',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'x_tenant',
                    'workflow_id',
                    'run_id',
                    'event',
                ],
                'required': [
                    'x_tenant',
                    'workflow_id',
                    'run_id',
                    'event',
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
                    'workflow_id':
                        (str,),
                    'run_id':
                        (str,),
                    'event':
                        (Event,),
                },
                'attribute_map': {
                    'x_tenant': 'X-Tenant',
                    'workflow_id': 'workflowId',
                    'run_id': 'runId',
                },
                'location_map': {
                    'x_tenant': 'header',
                    'workflow_id': 'path',
                    'run_id': 'path',
                    'event': 'body',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/vnd.graal.systems.v1.event+json',
                    'application/vnd.graal.systems.v1.error+json'
                ],
                'content_type': [
                    'application/vnd.graal.systems.v1.event+json'
                ]
            },
            api_client=api_client
        )
        self.find_events_by_job_id_and_run_id_endpoint = _Endpoint(
            settings={
                'response_type': ([Event],),
                'auth': [
                    'internal'
                ],
                'endpoint_path': '/jobs/{jobId}/runs/{runId}/events',
                'operation_id': 'find_events_by_job_id_and_run_id',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'x_tenant',
                    'job_id',
                    'run_id',
                ],
                'required': [
                    'x_tenant',
                    'job_id',
                    'run_id',
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
                    'job_id':
                        (str,),
                    'run_id':
                        (str,),
                },
                'attribute_map': {
                    'x_tenant': 'X-Tenant',
                    'job_id': 'jobId',
                    'run_id': 'runId',
                },
                'location_map': {
                    'x_tenant': 'header',
                    'job_id': 'path',
                    'run_id': 'path',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/vnd.graal.systems.v1.event+json',
                    'application/vnd.graal.systems.v1.error+json'
                ],
                'content_type': [],
            },
            api_client=api_client
        )
        self.find_events_by_workflow_id_and_run_id_endpoint = _Endpoint(
            settings={
                'response_type': ([Event],),
                'auth': [
                    'internal'
                ],
                'endpoint_path': '/workflows/{workflowId}/runs/{runId}/events',
                'operation_id': 'find_events_by_workflow_id_and_run_id',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'x_tenant',
                    'workflow_id',
                    'run_id',
                ],
                'required': [
                    'x_tenant',
                    'workflow_id',
                    'run_id',
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
                    'workflow_id':
                        (str,),
                    'run_id':
                        (str,),
                },
                'attribute_map': {
                    'x_tenant': 'X-Tenant',
                    'workflow_id': 'workflowId',
                    'run_id': 'runId',
                },
                'location_map': {
                    'x_tenant': 'header',
                    'workflow_id': 'path',
                    'run_id': 'path',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/vnd.graal.systems.v1.event+json',
                    'application/vnd.graal.systems.v1.error+json'
                ],
                'content_type': [],
            },
            api_client=api_client
        )

    def create_event_for_job_and_run(
        self,
        x_tenant,
        job_id,
        run_id,
        event,
        **kwargs
    ):
        """Add event for a run and a job  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.create_event_for_job_and_run(x_tenant, job_id, run_id, event, async_req=True)
        >>> result = thread.get()

        Args:
            x_tenant (str):
            job_id (str): Id of the Job
            run_id (str): Id of the Run
            event (Event): The event to be created

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
            Event
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
        kwargs['job_id'] = \
            job_id
        kwargs['run_id'] = \
            run_id
        kwargs['event'] = \
            event
        return self.create_event_for_job_and_run_endpoint.call_with_http_info(**kwargs)

    def create_event_for_workflow_and_run(
        self,
        x_tenant,
        workflow_id,
        run_id,
        event,
        **kwargs
    ):
        """Add event for a run and a workflow  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.create_event_for_workflow_and_run(x_tenant, workflow_id, run_id, event, async_req=True)
        >>> result = thread.get()

        Args:
            x_tenant (str):
            workflow_id (str): Id of the Workflow
            run_id (str): Id of the Run
            event (Event): The event to be created

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
            Event
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
        kwargs['workflow_id'] = \
            workflow_id
        kwargs['run_id'] = \
            run_id
        kwargs['event'] = \
            event
        return self.create_event_for_workflow_and_run_endpoint.call_with_http_info(**kwargs)

    def find_events_by_job_id_and_run_id(
        self,
        x_tenant,
        job_id,
        run_id,
        **kwargs
    ):
        """Find the events related to a run  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.find_events_by_job_id_and_run_id(x_tenant, job_id, run_id, async_req=True)
        >>> result = thread.get()

        Args:
            x_tenant (str):
            job_id (str): Id of the Job
            run_id (str): Id of the Run

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
            [Event]
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
        kwargs['job_id'] = \
            job_id
        kwargs['run_id'] = \
            run_id
        return self.find_events_by_job_id_and_run_id_endpoint.call_with_http_info(**kwargs)

    def find_events_by_workflow_id_and_run_id(
        self,
        x_tenant,
        workflow_id,
        run_id,
        **kwargs
    ):
        """Find the events related to a run  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.find_events_by_workflow_id_and_run_id(x_tenant, workflow_id, run_id, async_req=True)
        >>> result = thread.get()

        Args:
            x_tenant (str):
            workflow_id (str): Id of the Workflow
            run_id (str): Id of the Run

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
            [Event]
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
        kwargs['workflow_id'] = \
            workflow_id
        kwargs['run_id'] = \
            run_id
        return self.find_events_by_workflow_id_and_run_id_endpoint.call_with_http_info(**kwargs)

