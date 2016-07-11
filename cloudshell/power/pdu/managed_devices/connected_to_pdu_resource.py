import inject


class LiveStatus:
    """
    Constants class for Live Status
    Online denotes powered on, Offline denotes powered off
    """

    @staticmethod
    def ONLINE():
        return 'Online'

    @staticmethod
    def OFFLINE():
        return 'Offline'


class ConnectedToPduResource:
    """
    Details on device that is connected to PDU.
    """
    def __init__(self, endpoints, api=None):
        """
        :param endpoints: list of strs representing selected power ports on device connected to pdu
         example - ['connectedDeviceName//connectedDevicePortName']
        :param api: cloudshell api session, should be able to return GetResourceDetails
        """
        self.name = self._get_root_resource_name_by_path(endpoints)
        self._endpoints = endpoints
        if api is None:
            api = inject.instance('api')
        self._api = api
        self._details = self._get_resource_details(api)

    @property
    def details(self):
        """
        :rtype: ResourceInfo
        """
        return self._details

    def online(self):
        """
        sets device live status to power on
        """
        status = 'Powered on'
        self._set_live_status_on_device(LiveStatus.ONLINE(), status)
        return self._output_for_all_endpoints(status.lower())

    def offline(self):
        """
        sets device live status to powered off
        """
        status = 'Powered off'
        self._set_live_status_on_device(LiveStatus.OFFLINE(), status)
        return self._output_for_all_endpoints(status.lower())

    def _get_root_resource_name_by_path(self, endpoints):
        return endpoints[0].fullname.split('/')[0]

    def _get_resource_details(self, api):
        return api.GetResourceDetails(self.name)

    def _set_live_status_on_device(self, status, description=''):
        self._api.SetResourceLiveStatus(self.name, status, description)

    def _output_for_all_endpoints(self, msg):
        result = [r.fullname + ' ' + msg for r in self._endpoints]
        out = '\n'.join(result)
        return out
