import unittest
from mock import Mock
from cloudshell.power.pdu.managed_devices.connected_to_pdu_resource import ConnectedToPduResource, LiveStatus
from cloudshell.shell.core.driver_context import ResourceContextDetails
from cloudshell.api.cloudshell_api import CloudShellAPISession


class TestConnectedToPduResource(unittest.TestCase):
    def setUp(self):
        endpoint1 = Mock(fullname='PowerManagedResource/PowerPort1', spec=ResourceContextDetails)
        endpoint2 = Mock(fullname='PowerManagedResource/PowerPort2', spec=ResourceContextDetails)
        self.power_managed_resource = ConnectedToPduResource(endpoints=[endpoint1, endpoint2],
                               api=Mock(spec=CloudShellAPISession))

    def test_online(self):
        result = self.power_managed_resource.online()
        expected_result = 'PowerManagedResource/PowerPort1 powered on\nPowerManagedResource/PowerPort2 powered on'
        self.assertEqual(expected_result, result)

    def test_offline(self):
        result = self.power_managed_resource.offline()
        expected_result = 'PowerManagedResource/PowerPort1 powered off\nPowerManagedResource/PowerPort2 powered off'
        self.assertEqual(expected_result, result)
