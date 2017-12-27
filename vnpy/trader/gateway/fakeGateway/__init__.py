# encoding: UTF-8

from vnpy.trader import vtConstant
from .fakeGateway import FakeGateway

gatewayClass = FakeGateway
gatewayName = 'Fake'
gatewayDisplayName = gatewayName
gatewayType = vtConstant.GATEWAYTYPE_INTERNATIONAL
gatewayQryEnabled = False