# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
#
# Code generated by aaz-dev-tools
# --------------------------------------------------------------------------------------------

# pylint: skip-file
# flake8: noqa

from azure.cli.core.aaz import *


@register_command(
    "lab custom-image list",
    is_preview=True,
)
class List(AAZCommand):
    """List custom images in a given lab.
    """

    _aaz_info = {
        "version": "2018-09-15",
        "resources": [
            ["mgmt-plane", "/subscriptions/{}/resourcegroups/{}/providers/microsoft.devtestlab/labs/{}/customimages", "2018-09-15"],
        ]
    }

    AZ_SUPPORT_PAGINATION = True

    def _handler(self, command_args):
        super()._handler(command_args)
        return self.build_paging(self._execute_operations, self._output)

    _args_schema = None

    @classmethod
    def _build_arguments_schema(cls, *args, **kwargs):
        if cls._args_schema is not None:
            return cls._args_schema
        cls._args_schema = super()._build_arguments_schema(*args, **kwargs)

        # define Arg Group ""

        _args_schema = cls._args_schema
        _args_schema.lab_name = AAZStrArg(
            options=["--lab-name"],
            help="The name of the lab.",
            required=True,
        )
        _args_schema.resource_group = AAZResourceGroupNameArg(
            required=True,
        )
        _args_schema.expand = AAZStrArg(
            options=["--expand"],
            help="Specify the $expand query. Example: 'properties($select=vm)'",
        )
        _args_schema.filter = AAZStrArg(
            options=["--filter"],
            help="The filter to apply to the operation. Example: '$filter=contains(name,'myName')",
        )
        _args_schema.orderby = AAZStrArg(
            options=["--orderby"],
            help="The ordering expression for the results, using OData notation. Example: '$orderby=name desc'",
        )
        _args_schema.top = AAZIntArg(
            options=["--top"],
            help="The maximum number of resources to return from the operation. Example: '$top=10'",
        )
        return cls._args_schema

    def _execute_operations(self):
        self.pre_operations()
        self.CustomImagesList(ctx=self.ctx)()
        self.post_operations()

    @register_callback
    def pre_operations(self):
        pass

    @register_callback
    def post_operations(self):
        pass

    def _output(self, *args, **kwargs):
        result = self.deserialize_output(self.ctx.vars.instance.value, client_flatten=True)
        next_link = self.deserialize_output(self.ctx.vars.instance.next_link)
        return result, next_link

    class CustomImagesList(AAZHttpOperation):
        CLIENT_TYPE = "MgmtClient"

        def __call__(self, *args, **kwargs):
            request = self.make_request()
            session = self.client.send_request(request=request, stream=False, **kwargs)
            if session.http_response.status_code in [200]:
                return self.on_200(session)

            return self.on_error(session.http_response)

        @property
        def url(self):
            return self.client.format_url(
                "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DevTestLab/labs/{labName}/customimages",
                **self.url_parameters
            )

        @property
        def method(self):
            return "GET"

        @property
        def error_format(self):
            return "ODataV4Format"

        @property
        def url_parameters(self):
            parameters = {
                **self.serialize_url_param(
                    "labName", self.ctx.args.lab_name,
                    required=True,
                ),
                **self.serialize_url_param(
                    "resourceGroupName", self.ctx.args.resource_group,
                    required=True,
                ),
                **self.serialize_url_param(
                    "subscriptionId", self.ctx.subscription_id,
                    required=True,
                ),
            }
            return parameters

        @property
        def query_parameters(self):
            parameters = {
                **self.serialize_query_param(
                    "$expand", self.ctx.args.expand,
                ),
                **self.serialize_query_param(
                    "$filter", self.ctx.args.filter,
                ),
                **self.serialize_query_param(
                    "$orderby", self.ctx.args.orderby,
                ),
                **self.serialize_query_param(
                    "$top", self.ctx.args.top,
                ),
                **self.serialize_query_param(
                    "api-version", "2018-09-15",
                    required=True,
                ),
            }
            return parameters

        @property
        def header_parameters(self):
            parameters = {
                **self.serialize_header_param(
                    "Accept", "application/json",
                ),
            }
            return parameters

        def on_200(self, session):
            data = self.deserialize_http_content(session)
            self.ctx.set_var(
                "instance",
                data,
                schema_builder=self._build_schema_on_200
            )

        _schema_on_200 = None

        @classmethod
        def _build_schema_on_200(cls):
            if cls._schema_on_200 is not None:
                return cls._schema_on_200

            cls._schema_on_200 = AAZObjectType()

            _schema_on_200 = cls._schema_on_200
            _schema_on_200.next_link = AAZStrType(
                serialized_name="nextLink",
            )
            _schema_on_200.value = AAZListType()

            value = cls._schema_on_200.value
            value.Element = AAZObjectType()

            _element = cls._schema_on_200.value.Element
            _element.id = AAZStrType(
                flags={"read_only": True},
            )
            _element.location = AAZStrType()
            _element.name = AAZStrType(
                flags={"read_only": True},
            )
            _element.properties = AAZObjectType(
                flags={"required": True, "client_flatten": True},
            )
            _element.tags = AAZDictType()
            _element.type = AAZStrType(
                flags={"read_only": True},
            )

            properties = cls._schema_on_200.value.Element.properties
            properties.author = AAZStrType()
            properties.creation_date = AAZStrType(
                serialized_name="creationDate",
                flags={"read_only": True},
            )
            properties.custom_image_plan = AAZObjectType(
                serialized_name="customImagePlan",
            )
            properties.data_disk_storage_info = AAZListType(
                serialized_name="dataDiskStorageInfo",
            )
            properties.description = AAZStrType()
            properties.is_plan_authorized = AAZBoolType(
                serialized_name="isPlanAuthorized",
            )
            properties.managed_image_id = AAZStrType(
                serialized_name="managedImageId",
            )
            properties.managed_snapshot_id = AAZStrType(
                serialized_name="managedSnapshotId",
            )
            properties.provisioning_state = AAZStrType(
                serialized_name="provisioningState",
                flags={"read_only": True},
            )
            properties.unique_identifier = AAZStrType(
                serialized_name="uniqueIdentifier",
                flags={"read_only": True},
            )
            properties.vhd = AAZObjectType()
            properties.vm = AAZObjectType()

            custom_image_plan = cls._schema_on_200.value.Element.properties.custom_image_plan
            custom_image_plan.id = AAZStrType()
            custom_image_plan.offer = AAZStrType()
            custom_image_plan.publisher = AAZStrType()

            data_disk_storage_info = cls._schema_on_200.value.Element.properties.data_disk_storage_info
            data_disk_storage_info.Element = AAZObjectType()

            _element = cls._schema_on_200.value.Element.properties.data_disk_storage_info.Element
            _element.lun = AAZStrType()
            _element.storage_type = AAZStrType(
                serialized_name="storageType",
            )

            vhd = cls._schema_on_200.value.Element.properties.vhd
            vhd.image_name = AAZStrType(
                serialized_name="imageName",
            )
            vhd.os_type = AAZStrType(
                serialized_name="osType",
                flags={"required": True},
            )
            vhd.sys_prep = AAZBoolType(
                serialized_name="sysPrep",
            )

            vm = cls._schema_on_200.value.Element.properties.vm
            vm.linux_os_info = AAZObjectType(
                serialized_name="linuxOsInfo",
            )
            vm.source_vm_id = AAZStrType(
                serialized_name="sourceVmId",
            )
            vm.windows_os_info = AAZObjectType(
                serialized_name="windowsOsInfo",
            )

            linux_os_info = cls._schema_on_200.value.Element.properties.vm.linux_os_info
            linux_os_info.linux_os_state = AAZStrType(
                serialized_name="linuxOsState",
            )

            windows_os_info = cls._schema_on_200.value.Element.properties.vm.windows_os_info
            windows_os_info.windows_os_state = AAZStrType(
                serialized_name="windowsOsState",
            )

            tags = cls._schema_on_200.value.Element.tags
            tags.Element = AAZStrType()

            return cls._schema_on_200


class _ListHelper:
    """Helper class for List"""


__all__ = ["List"]
