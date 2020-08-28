# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from chirpstack_api.as_pb.external.api import remoteMulticastGroup_pb2 as chirpstack__api_dot_as__pb_dot_external_dot_api_dot_remoteMulticastGroup__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2


class RemoteMulticastGroupServiceStub(object):
    """RemoteMulticastGroupService is the service managing multicast-groups.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Create = channel.unary_unary(
                '/api.RemoteMulticastGroupService/Create',
                request_serializer=chirpstack__api_dot_as__pb_dot_external_dot_api_dot_remoteMulticastGroup__pb2.CreateRemoteMulticastGroupRequest.SerializeToString,
                response_deserializer=chirpstack__api_dot_as__pb_dot_external_dot_api_dot_remoteMulticastGroup__pb2.CreateRemoteMulticastGroupResponse.FromString,
                )
        self.Get = channel.unary_unary(
                '/api.RemoteMulticastGroupService/Get',
                request_serializer=chirpstack__api_dot_as__pb_dot_external_dot_api_dot_remoteMulticastGroup__pb2.GetRemoteMulticastGroupRequest.SerializeToString,
                response_deserializer=chirpstack__api_dot_as__pb_dot_external_dot_api_dot_remoteMulticastGroup__pb2.GetRemoteMulticastGroupResponse.FromString,
                )
        self.Update = channel.unary_unary(
                '/api.RemoteMulticastGroupService/Update',
                request_serializer=chirpstack__api_dot_as__pb_dot_external_dot_api_dot_remoteMulticastGroup__pb2.UpdateRemoteMulticastGroupRequest.SerializeToString,
                response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                )
        self.Delete = channel.unary_unary(
                '/api.RemoteMulticastGroupService/Delete',
                request_serializer=chirpstack__api_dot_as__pb_dot_external_dot_api_dot_remoteMulticastGroup__pb2.DeleteRemoteMulticastGroupRequest.SerializeToString,
                response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                )
        self.List = channel.unary_unary(
                '/api.RemoteMulticastGroupService/List',
                request_serializer=chirpstack__api_dot_as__pb_dot_external_dot_api_dot_remoteMulticastGroup__pb2.ListRemoteMulticastGroupRequest.SerializeToString,
                response_deserializer=chirpstack__api_dot_as__pb_dot_external_dot_api_dot_remoteMulticastGroup__pb2.ListRemoteMulticastGroupResponse.FromString,
                )
        self.AddDevice = channel.unary_unary(
                '/api.RemoteMulticastGroupService/AddDevice',
                request_serializer=chirpstack__api_dot_as__pb_dot_external_dot_api_dot_remoteMulticastGroup__pb2.AddDeviceToRemoteMulticastGroupRequest.SerializeToString,
                response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                )
        self.ResetDevice = channel.unary_unary(
                '/api.RemoteMulticastGroupService/ResetDevice',
                request_serializer=chirpstack__api_dot_as__pb_dot_external_dot_api_dot_remoteMulticastGroup__pb2.ResetRemoteMulticastDeviceRequest.SerializeToString,
                response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                )
        self.RemoveDevice = channel.unary_unary(
                '/api.RemoteMulticastGroupService/RemoveDevice',
                request_serializer=chirpstack__api_dot_as__pb_dot_external_dot_api_dot_remoteMulticastGroup__pb2.RemoveDeviceFromRemoteMulticastGroupRequest.SerializeToString,
                response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                )
        self.ListDevicesForRemoteMulticast = channel.unary_unary(
                '/api.RemoteMulticastGroupService/ListDevicesForRemoteMulticast',
                request_serializer=chirpstack__api_dot_as__pb_dot_external_dot_api_dot_remoteMulticastGroup__pb2.ListRemoteMulticastDeviceRequest.SerializeToString,
                response_deserializer=chirpstack__api_dot_as__pb_dot_external_dot_api_dot_remoteMulticastGroup__pb2.ListRemoteMulticastDeviceResponse.FromString,
                )
        self.GetDevicesList = channel.unary_unary(
                '/api.RemoteMulticastGroupService/GetDevicesList',
                request_serializer=chirpstack__api_dot_as__pb_dot_external_dot_api_dot_remoteMulticastGroup__pb2.ListRemoteMulticastDeviceRequest.SerializeToString,
                response_deserializer=chirpstack__api_dot_as__pb_dot_external_dot_api_dot_remoteMulticastGroup__pb2.ListRemoteMulticastDevicesResponse.FromString,
                )
        self.GetDeploymentDevice = channel.unary_unary(
                '/api.RemoteMulticastGroupService/GetDeploymentDevice',
                request_serializer=chirpstack__api_dot_as__pb_dot_external_dot_api_dot_remoteMulticastGroup__pb2.GetRemoteMulticastDeploymentDeviceRequest.SerializeToString,
                response_deserializer=chirpstack__api_dot_as__pb_dot_external_dot_api_dot_remoteMulticastGroup__pb2.GetRemoteMulticastDeploymentDeviceResponse.FromString,
                )
        self.Enqueue = channel.unary_unary(
                '/api.RemoteMulticastGroupService/Enqueue',
                request_serializer=chirpstack__api_dot_as__pb_dot_external_dot_api_dot_remoteMulticastGroup__pb2.EnqueueRemoteMulticastQueueItemRequest.SerializeToString,
                response_deserializer=chirpstack__api_dot_as__pb_dot_external_dot_api_dot_remoteMulticastGroup__pb2.EnqueueRemoteMulticastQueueItemResponse.FromString,
                )
        self.FlushQueue = channel.unary_unary(
                '/api.RemoteMulticastGroupService/FlushQueue',
                request_serializer=chirpstack__api_dot_as__pb_dot_external_dot_api_dot_remoteMulticastGroup__pb2.FlushRemoteMulticastGroupQueueItemsRequest.SerializeToString,
                response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                )
        self.ListQueue = channel.unary_unary(
                '/api.RemoteMulticastGroupService/ListQueue',
                request_serializer=chirpstack__api_dot_as__pb_dot_external_dot_api_dot_remoteMulticastGroup__pb2.ListRemoteMulticastGroupQueueItemsRequest.SerializeToString,
                response_deserializer=chirpstack__api_dot_as__pb_dot_external_dot_api_dot_remoteMulticastGroup__pb2.ListRemoteMulticastGroupQueueItemsResponse.FromString,
                )


class RemoteMulticastGroupServiceServicer(object):
    """RemoteMulticastGroupService is the service managing multicast-groups.
    """

    def Create(self, request, context):
        """Create creates the given remote multicast-group.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Get(self, request, context):
        """Get returns a remote multicast-group given an ID.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Update(self, request, context):
        """Update updates the given remote multicast-group.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Delete(self, request, context):
        """Delete deletes a remote multicast-group given an ID.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def List(self, request, context):
        """List lists the available remote multicast-groups.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def AddDevice(self, request, context):
        """AddDevice adds the given device to the remote multicast-group.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ResetDevice(self, request, context):
        """ResetDevice Restart the remote multicast process of given device.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def RemoveDevice(self, request, context):
        """RemoveDevice removes the given device from the remote multicast-group.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListDevicesForRemoteMulticast(self, request, context):
        """ListDevicesForRemoteMulticast Lists the available devices for joining to
        remote multicast-group for given application id.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetDevicesList(self, request, context):
        """GetDevicesList Lists the available devices in remote multicast-groups.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetDeploymentDevice(self, request, context):
        """GetDeploymentDevice returns the deployment device.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Enqueue(self, request, context):
        """Enqueue adds the given item to the remote multicast-queue.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def FlushQueue(self, request, context):
        """FlushQueue flushes the remote multicast-group queue.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListQueue(self, request, context):
        """ListQueue lists the items in the remote multicast-group queue.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_RemoteMulticastGroupServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Create': grpc.unary_unary_rpc_method_handler(
                    servicer.Create,
                    request_deserializer=chirpstack__api_dot_as__pb_dot_external_dot_api_dot_remoteMulticastGroup__pb2.CreateRemoteMulticastGroupRequest.FromString,
                    response_serializer=chirpstack__api_dot_as__pb_dot_external_dot_api_dot_remoteMulticastGroup__pb2.CreateRemoteMulticastGroupResponse.SerializeToString,
            ),
            'Get': grpc.unary_unary_rpc_method_handler(
                    servicer.Get,
                    request_deserializer=chirpstack__api_dot_as__pb_dot_external_dot_api_dot_remoteMulticastGroup__pb2.GetRemoteMulticastGroupRequest.FromString,
                    response_serializer=chirpstack__api_dot_as__pb_dot_external_dot_api_dot_remoteMulticastGroup__pb2.GetRemoteMulticastGroupResponse.SerializeToString,
            ),
            'Update': grpc.unary_unary_rpc_method_handler(
                    servicer.Update,
                    request_deserializer=chirpstack__api_dot_as__pb_dot_external_dot_api_dot_remoteMulticastGroup__pb2.UpdateRemoteMulticastGroupRequest.FromString,
                    response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            ),
            'Delete': grpc.unary_unary_rpc_method_handler(
                    servicer.Delete,
                    request_deserializer=chirpstack__api_dot_as__pb_dot_external_dot_api_dot_remoteMulticastGroup__pb2.DeleteRemoteMulticastGroupRequest.FromString,
                    response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            ),
            'List': grpc.unary_unary_rpc_method_handler(
                    servicer.List,
                    request_deserializer=chirpstack__api_dot_as__pb_dot_external_dot_api_dot_remoteMulticastGroup__pb2.ListRemoteMulticastGroupRequest.FromString,
                    response_serializer=chirpstack__api_dot_as__pb_dot_external_dot_api_dot_remoteMulticastGroup__pb2.ListRemoteMulticastGroupResponse.SerializeToString,
            ),
            'AddDevice': grpc.unary_unary_rpc_method_handler(
                    servicer.AddDevice,
                    request_deserializer=chirpstack__api_dot_as__pb_dot_external_dot_api_dot_remoteMulticastGroup__pb2.AddDeviceToRemoteMulticastGroupRequest.FromString,
                    response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            ),
            'ResetDevice': grpc.unary_unary_rpc_method_handler(
                    servicer.ResetDevice,
                    request_deserializer=chirpstack__api_dot_as__pb_dot_external_dot_api_dot_remoteMulticastGroup__pb2.ResetRemoteMulticastDeviceRequest.FromString,
                    response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            ),
            'RemoveDevice': grpc.unary_unary_rpc_method_handler(
                    servicer.RemoveDevice,
                    request_deserializer=chirpstack__api_dot_as__pb_dot_external_dot_api_dot_remoteMulticastGroup__pb2.RemoveDeviceFromRemoteMulticastGroupRequest.FromString,
                    response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            ),
            'ListDevicesForRemoteMulticast': grpc.unary_unary_rpc_method_handler(
                    servicer.ListDevicesForRemoteMulticast,
                    request_deserializer=chirpstack__api_dot_as__pb_dot_external_dot_api_dot_remoteMulticastGroup__pb2.ListRemoteMulticastDeviceRequest.FromString,
                    response_serializer=chirpstack__api_dot_as__pb_dot_external_dot_api_dot_remoteMulticastGroup__pb2.ListRemoteMulticastDeviceResponse.SerializeToString,
            ),
            'GetDevicesList': grpc.unary_unary_rpc_method_handler(
                    servicer.GetDevicesList,
                    request_deserializer=chirpstack__api_dot_as__pb_dot_external_dot_api_dot_remoteMulticastGroup__pb2.ListRemoteMulticastDeviceRequest.FromString,
                    response_serializer=chirpstack__api_dot_as__pb_dot_external_dot_api_dot_remoteMulticastGroup__pb2.ListRemoteMulticastDevicesResponse.SerializeToString,
            ),
            'GetDeploymentDevice': grpc.unary_unary_rpc_method_handler(
                    servicer.GetDeploymentDevice,
                    request_deserializer=chirpstack__api_dot_as__pb_dot_external_dot_api_dot_remoteMulticastGroup__pb2.GetRemoteMulticastDeploymentDeviceRequest.FromString,
                    response_serializer=chirpstack__api_dot_as__pb_dot_external_dot_api_dot_remoteMulticastGroup__pb2.GetRemoteMulticastDeploymentDeviceResponse.SerializeToString,
            ),
            'Enqueue': grpc.unary_unary_rpc_method_handler(
                    servicer.Enqueue,
                    request_deserializer=chirpstack__api_dot_as__pb_dot_external_dot_api_dot_remoteMulticastGroup__pb2.EnqueueRemoteMulticastQueueItemRequest.FromString,
                    response_serializer=chirpstack__api_dot_as__pb_dot_external_dot_api_dot_remoteMulticastGroup__pb2.EnqueueRemoteMulticastQueueItemResponse.SerializeToString,
            ),
            'FlushQueue': grpc.unary_unary_rpc_method_handler(
                    servicer.FlushQueue,
                    request_deserializer=chirpstack__api_dot_as__pb_dot_external_dot_api_dot_remoteMulticastGroup__pb2.FlushRemoteMulticastGroupQueueItemsRequest.FromString,
                    response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            ),
            'ListQueue': grpc.unary_unary_rpc_method_handler(
                    servicer.ListQueue,
                    request_deserializer=chirpstack__api_dot_as__pb_dot_external_dot_api_dot_remoteMulticastGroup__pb2.ListRemoteMulticastGroupQueueItemsRequest.FromString,
                    response_serializer=chirpstack__api_dot_as__pb_dot_external_dot_api_dot_remoteMulticastGroup__pb2.ListRemoteMulticastGroupQueueItemsResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'api.RemoteMulticastGroupService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class RemoteMulticastGroupService(object):
    """RemoteMulticastGroupService is the service managing multicast-groups.
    """

    @staticmethod
    def Create(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/api.RemoteMulticastGroupService/Create',
            chirpstack__api_dot_as__pb_dot_external_dot_api_dot_remoteMulticastGroup__pb2.CreateRemoteMulticastGroupRequest.SerializeToString,
            chirpstack__api_dot_as__pb_dot_external_dot_api_dot_remoteMulticastGroup__pb2.CreateRemoteMulticastGroupResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Get(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/api.RemoteMulticastGroupService/Get',
            chirpstack__api_dot_as__pb_dot_external_dot_api_dot_remoteMulticastGroup__pb2.GetRemoteMulticastGroupRequest.SerializeToString,
            chirpstack__api_dot_as__pb_dot_external_dot_api_dot_remoteMulticastGroup__pb2.GetRemoteMulticastGroupResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Update(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/api.RemoteMulticastGroupService/Update',
            chirpstack__api_dot_as__pb_dot_external_dot_api_dot_remoteMulticastGroup__pb2.UpdateRemoteMulticastGroupRequest.SerializeToString,
            google_dot_protobuf_dot_empty__pb2.Empty.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Delete(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/api.RemoteMulticastGroupService/Delete',
            chirpstack__api_dot_as__pb_dot_external_dot_api_dot_remoteMulticastGroup__pb2.DeleteRemoteMulticastGroupRequest.SerializeToString,
            google_dot_protobuf_dot_empty__pb2.Empty.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def List(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/api.RemoteMulticastGroupService/List',
            chirpstack__api_dot_as__pb_dot_external_dot_api_dot_remoteMulticastGroup__pb2.ListRemoteMulticastGroupRequest.SerializeToString,
            chirpstack__api_dot_as__pb_dot_external_dot_api_dot_remoteMulticastGroup__pb2.ListRemoteMulticastGroupResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def AddDevice(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/api.RemoteMulticastGroupService/AddDevice',
            chirpstack__api_dot_as__pb_dot_external_dot_api_dot_remoteMulticastGroup__pb2.AddDeviceToRemoteMulticastGroupRequest.SerializeToString,
            google_dot_protobuf_dot_empty__pb2.Empty.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ResetDevice(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/api.RemoteMulticastGroupService/ResetDevice',
            chirpstack__api_dot_as__pb_dot_external_dot_api_dot_remoteMulticastGroup__pb2.ResetRemoteMulticastDeviceRequest.SerializeToString,
            google_dot_protobuf_dot_empty__pb2.Empty.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def RemoveDevice(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/api.RemoteMulticastGroupService/RemoveDevice',
            chirpstack__api_dot_as__pb_dot_external_dot_api_dot_remoteMulticastGroup__pb2.RemoveDeviceFromRemoteMulticastGroupRequest.SerializeToString,
            google_dot_protobuf_dot_empty__pb2.Empty.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ListDevicesForRemoteMulticast(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/api.RemoteMulticastGroupService/ListDevicesForRemoteMulticast',
            chirpstack__api_dot_as__pb_dot_external_dot_api_dot_remoteMulticastGroup__pb2.ListRemoteMulticastDeviceRequest.SerializeToString,
            chirpstack__api_dot_as__pb_dot_external_dot_api_dot_remoteMulticastGroup__pb2.ListRemoteMulticastDeviceResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetDevicesList(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/api.RemoteMulticastGroupService/GetDevicesList',
            chirpstack__api_dot_as__pb_dot_external_dot_api_dot_remoteMulticastGroup__pb2.ListRemoteMulticastDeviceRequest.SerializeToString,
            chirpstack__api_dot_as__pb_dot_external_dot_api_dot_remoteMulticastGroup__pb2.ListRemoteMulticastDevicesResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetDeploymentDevice(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/api.RemoteMulticastGroupService/GetDeploymentDevice',
            chirpstack__api_dot_as__pb_dot_external_dot_api_dot_remoteMulticastGroup__pb2.GetRemoteMulticastDeploymentDeviceRequest.SerializeToString,
            chirpstack__api_dot_as__pb_dot_external_dot_api_dot_remoteMulticastGroup__pb2.GetRemoteMulticastDeploymentDeviceResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Enqueue(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/api.RemoteMulticastGroupService/Enqueue',
            chirpstack__api_dot_as__pb_dot_external_dot_api_dot_remoteMulticastGroup__pb2.EnqueueRemoteMulticastQueueItemRequest.SerializeToString,
            chirpstack__api_dot_as__pb_dot_external_dot_api_dot_remoteMulticastGroup__pb2.EnqueueRemoteMulticastQueueItemResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def FlushQueue(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/api.RemoteMulticastGroupService/FlushQueue',
            chirpstack__api_dot_as__pb_dot_external_dot_api_dot_remoteMulticastGroup__pb2.FlushRemoteMulticastGroupQueueItemsRequest.SerializeToString,
            google_dot_protobuf_dot_empty__pb2.Empty.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ListQueue(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/api.RemoteMulticastGroupService/ListQueue',
            chirpstack__api_dot_as__pb_dot_external_dot_api_dot_remoteMulticastGroup__pb2.ListRemoteMulticastGroupQueueItemsRequest.SerializeToString,
            chirpstack__api_dot_as__pb_dot_external_dot_api_dot_remoteMulticastGroup__pb2.ListRemoteMulticastGroupQueueItemsResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
