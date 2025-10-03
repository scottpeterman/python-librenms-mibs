# SNMP MIB module (SLE-DEVICE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\dasan\SLE-DEVICE-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:34:23 2025
# On host DESKTOP-ORUUBP9 platform Windows version 11 by user speterman
# Using Python version 3.12.8 (tags/v3.12.8:2dc476b, Dec  3 2024, 19:30:04) [MSC v.1942 64 bit (AMD64)]

if 'mibBuilder' not in globals():
    import sys

    sys.stderr.write(__doc__)
    sys.exit(1)

# Import base ASN.1 objects even if this MIB does not use it

(Integer,
 OctetString,
 ObjectIdentifier) = mibBuilder.importSymbols(
    "ASN1",
    "Integer",
    "OctetString",
    "ObjectIdentifier")

(NamedValues,) = mibBuilder.importSymbols(
    "ASN1-ENUMERATION",
    "NamedValues")
(ConstraintsIntersection,
 ConstraintsUnion,
 SingleValueConstraint,
 ValueRangeConstraint,
 ValueSizeConstraint) = mibBuilder.importSymbols(
    "ASN1-REFINEMENT",
    "ConstraintsIntersection",
    "ConstraintsUnion",
    "SingleValueConstraint",
    "ValueRangeConstraint",
    "ValueSizeConstraint")

# Import SMI symbols from the MIBs this MIB depends on

(sleMgmt,) = mibBuilder.importSymbols(
    "DASAN-SMI",
    "sleMgmt")

(SleControlRequestResultType,
 SleControlStatusType) = mibBuilder.importSymbols(
    "SLE-TC-MIB",
    "SleControlRequestResultType",
    "SleControlStatusType")

(ModuleCompliance,
 NotificationGroup,
 ObjectGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup",
    "ObjectGroup")

(Bits,
 Bits,
 Counter32,
 Counter64,
 Gauge32,
 Integer32,
 IpAddress,
 ModuleIdentity,
 MibIdentifier,
 NotificationType,
 ObjectIdentity,
 MibScalar,
 MibTable,
 MibTableRow,
 MibTableColumn,
 TimeTicks,
 Unsigned32,
 iso) = mibBuilder.importSymbols(
    "SNMPv2-SMI",
    "Bits",
    "Bits",
    "Counter32",
    "Counter64",
    "Gauge32",
    "Integer32",
    "IpAddress",
    "ModuleIdentity",
    "MibIdentifier",
    "NotificationType",
    "ObjectIdentity",
    "MibScalar",
    "MibTable",
    "MibTableRow",
    "MibTableColumn",
    "TimeTicks",
    "Unsigned32",
    "iso")

(DisplayString,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

sleDevice = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_SleDeviceBase_ObjectIdentity = ObjectIdentity
sleDeviceBase = _SleDeviceBase_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 1)
)
_SleDeviceBaseInfo_ObjectIdentity = ObjectIdentity
sleDeviceBaseInfo = _SleDeviceBaseInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 1, 1)
)
_SleDeviceEthernetPortNum_Type = Integer32
_SleDeviceEthernetPortNum_Object = MibScalar
sleDeviceEthernetPortNum = _SleDeviceEthernetPortNum_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 1, 1, 1),
    _SleDeviceEthernetPortNum_Type()
)
sleDeviceEthernetPortNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleDeviceEthernetPortNum.setStatus("current")
_SleDevicePowerNum_Type = Integer32
_SleDevicePowerNum_Object = MibScalar
sleDevicePowerNum = _SleDevicePowerNum_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 1, 1, 2),
    _SleDevicePowerNum_Type()
)
sleDevicePowerNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleDevicePowerNum.setStatus("current")
_SleDeviceFanModuleNum_Type = Integer32
_SleDeviceFanModuleNum_Object = MibScalar
sleDeviceFanModuleNum = _SleDeviceFanModuleNum_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 1, 1, 3),
    _SleDeviceFanModuleNum_Type()
)
sleDeviceFanModuleNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleDeviceFanModuleNum.setStatus("current")
_SleDeviceTemperatureNum_Type = Integer32
_SleDeviceTemperatureNum_Object = MibScalar
sleDeviceTemperatureNum = _SleDeviceTemperatureNum_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 1, 1, 4),
    _SleDeviceTemperatureNum_Type()
)
sleDeviceTemperatureNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleDeviceTemperatureNum.setStatus("current")
_SleDeviceFanStartTemperature_Type = Integer32
_SleDeviceFanStartTemperature_Object = MibScalar
sleDeviceFanStartTemperature = _SleDeviceFanStartTemperature_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 1, 1, 5),
    _SleDeviceFanStartTemperature_Type()
)
sleDeviceFanStartTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleDeviceFanStartTemperature.setStatus("current")
_SleDeviceFanStopTemperature_Type = Integer32
_SleDeviceFanStopTemperature_Object = MibScalar
sleDeviceFanStopTemperature = _SleDeviceFanStopTemperature_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 1, 1, 6),
    _SleDeviceFanStopTemperature_Type()
)
sleDeviceFanStopTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleDeviceFanStopTemperature.setStatus("current")


class _SleDeviceJumboFrameStatus_Type(Integer32):
    """Custom type sleDeviceJumboFrameStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_SleDeviceJumboFrameStatus_Type.__name__ = "Integer32"
_SleDeviceJumboFrameStatus_Object = MibScalar
sleDeviceJumboFrameStatus = _SleDeviceJumboFrameStatus_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 1, 1, 7),
    _SleDeviceJumboFrameStatus_Type()
)
sleDeviceJumboFrameStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleDeviceJumboFrameStatus.setStatus("current")


class _SleDeviceEnvironmentMonitoringStatus_Type(Integer32):
    """Custom type sleDeviceEnvironmentMonitoringStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notInstallAIU", 0),
          ("normalOpen", 1),
          ("normalClose", 2))
    )


_SleDeviceEnvironmentMonitoringStatus_Type.__name__ = "Integer32"
_SleDeviceEnvironmentMonitoringStatus_Object = MibScalar
sleDeviceEnvironmentMonitoringStatus = _SleDeviceEnvironmentMonitoringStatus_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 1, 1, 8),
    _SleDeviceEnvironmentMonitoringStatus_Type()
)
sleDeviceEnvironmentMonitoringStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleDeviceEnvironmentMonitoringStatus.setStatus("current")
_SleDeviceBaseControl_ObjectIdentity = ObjectIdentity
sleDeviceBaseControl = _SleDeviceBaseControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 1, 2)
)


class _SleDeviceControlRequest_Type(Integer32):
    """Custom type sleDeviceControlRequest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("setDeviceTemperatureThreshold", 1),
          ("setDeviceJumboFrameStatus", 2),
          ("setDeviceLEDTest", 3),
          ("setEnvironmentMonitoringStatus", 4))
    )


_SleDeviceControlRequest_Type.__name__ = "Integer32"
_SleDeviceControlRequest_Object = MibScalar
sleDeviceControlRequest = _SleDeviceControlRequest_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 1, 2, 1),
    _SleDeviceControlRequest_Type()
)
sleDeviceControlRequest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleDeviceControlRequest.setStatus("current")
_SleDeviceControlStatus_Type = SleControlStatusType
_SleDeviceControlStatus_Object = MibScalar
sleDeviceControlStatus = _SleDeviceControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 1, 2, 2),
    _SleDeviceControlStatus_Type()
)
sleDeviceControlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleDeviceControlStatus.setStatus("current")
_SleDeviceControlTimer_Type = Gauge32
_SleDeviceControlTimer_Object = MibScalar
sleDeviceControlTimer = _SleDeviceControlTimer_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 1, 2, 3),
    _SleDeviceControlTimer_Type()
)
sleDeviceControlTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleDeviceControlTimer.setStatus("current")
_SleDeviceControlTimeStamp_Type = TimeTicks
_SleDeviceControlTimeStamp_Object = MibScalar
sleDeviceControlTimeStamp = _SleDeviceControlTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 1, 2, 4),
    _SleDeviceControlTimeStamp_Type()
)
sleDeviceControlTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleDeviceControlTimeStamp.setStatus("current")
_SleDeviceControlReqResult_Type = SleControlRequestResultType
_SleDeviceControlReqResult_Object = MibScalar
sleDeviceControlReqResult = _SleDeviceControlReqResult_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 1, 2, 5),
    _SleDeviceControlReqResult_Type()
)
sleDeviceControlReqResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleDeviceControlReqResult.setStatus("current")
_SleDeviceControlFanStartTemperature_Type = Integer32
_SleDeviceControlFanStartTemperature_Object = MibScalar
sleDeviceControlFanStartTemperature = _SleDeviceControlFanStartTemperature_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 1, 2, 6),
    _SleDeviceControlFanStartTemperature_Type()
)
sleDeviceControlFanStartTemperature.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleDeviceControlFanStartTemperature.setStatus("current")
_SleDeviceControlFanStopTemperature_Type = Integer32
_SleDeviceControlFanStopTemperature_Object = MibScalar
sleDeviceControlFanStopTemperature = _SleDeviceControlFanStopTemperature_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 1, 2, 7),
    _SleDeviceControlFanStopTemperature_Type()
)
sleDeviceControlFanStopTemperature.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleDeviceControlFanStopTemperature.setStatus("current")


class _SleDeviceControlJumboFrameStatus_Type(Integer32):
    """Custom type sleDeviceControlJumboFrameStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_SleDeviceControlJumboFrameStatus_Type.__name__ = "Integer32"
_SleDeviceControlJumboFrameStatus_Object = MibScalar
sleDeviceControlJumboFrameStatus = _SleDeviceControlJumboFrameStatus_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 1, 2, 8),
    _SleDeviceControlJumboFrameStatus_Type()
)
sleDeviceControlJumboFrameStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleDeviceControlJumboFrameStatus.setStatus("current")


class _SleDeviceControlEnvironmentMonitoringStatus_Type(Integer32):
    """Custom type sleDeviceControlEnvironmentMonitoringStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("normalOpen", 1),
          ("normalClose", 2))
    )


_SleDeviceControlEnvironmentMonitoringStatus_Type.__name__ = "Integer32"
_SleDeviceControlEnvironmentMonitoringStatus_Object = MibScalar
sleDeviceControlEnvironmentMonitoringStatus = _SleDeviceControlEnvironmentMonitoringStatus_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 1, 2, 9),
    _SleDeviceControlEnvironmentMonitoringStatus_Type()
)
sleDeviceControlEnvironmentMonitoringStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleDeviceControlEnvironmentMonitoringStatus.setStatus("current")
_SleDeviceBaseNotification_ObjectIdentity = ObjectIdentity
sleDeviceBaseNotification = _SleDeviceBaseNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 1, 3)
)
_SleEthernetPort_ObjectIdentity = ObjectIdentity
sleEthernetPort = _SleEthernetPort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 2)
)
_SleEthernetPortTable_Object = MibTable
sleEthernetPortTable = _SleEthernetPortTable_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 2, 1)
)
if mibBuilder.loadTexts:
    sleEthernetPortTable.setStatus("current")
_SleEthernetPortEntry_Object = MibTableRow
sleEthernetPortEntry = _SleEthernetPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 2, 1, 1)
)
sleEthernetPortEntry.setIndexNames(
    (0, "SLE-DEVICE-MIB", "sleEthernetPortIndex"),
)
if mibBuilder.loadTexts:
    sleEthernetPortEntry.setStatus("current")


class _SleEthernetPortIndex_Type(Integer32):
    """Custom type sleEthernetPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_SleEthernetPortIndex_Type.__name__ = "Integer32"
_SleEthernetPortIndex_Object = MibTableColumn
sleEthernetPortIndex = _SleEthernetPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 2, 1, 1, 1),
    _SleEthernetPortIndex_Type()
)
sleEthernetPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleEthernetPortIndex.setStatus("current")
_SleEthernetPortPhyIndex_Type = Integer32
_SleEthernetPortPhyIndex_Object = MibTableColumn
sleEthernetPortPhyIndex = _SleEthernetPortPhyIndex_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 2, 1, 1, 2),
    _SleEthernetPortPhyIndex_Type()
)
sleEthernetPortPhyIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleEthernetPortPhyIndex.setStatus("current")


class _SleEthernetPortType_Type(Integer32):
    """Custom type sleEthernetPortType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 0),
          ("electrical", 1),
          ("optical", 2))
    )


_SleEthernetPortType_Type.__name__ = "Integer32"
_SleEthernetPortType_Object = MibTableColumn
sleEthernetPortType = _SleEthernetPortType_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 2, 1, 1, 3),
    _SleEthernetPortType_Type()
)
sleEthernetPortType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleEthernetPortType.setStatus("current")


class _SleEthernetPortAdminStatus_Type(Integer32):
    """Custom type sleEthernetPortAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("up", 1),
          ("down", 2),
          ("notAvailable", 3))
    )


_SleEthernetPortAdminStatus_Type.__name__ = "Integer32"
_SleEthernetPortAdminStatus_Object = MibTableColumn
sleEthernetPortAdminStatus = _SleEthernetPortAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 2, 1, 1, 4),
    _SleEthernetPortAdminStatus_Type()
)
sleEthernetPortAdminStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleEthernetPortAdminStatus.setStatus("current")


class _SleEthernetPortOperStatus_Type(Integer32):
    """Custom type sleEthernetPortOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("up", 1),
          ("down", 2),
          ("notAvailable", 3))
    )


_SleEthernetPortOperStatus_Type.__name__ = "Integer32"
_SleEthernetPortOperStatus_Object = MibTableColumn
sleEthernetPortOperStatus = _SleEthernetPortOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 2, 1, 1, 5),
    _SleEthernetPortOperStatus_Type()
)
sleEthernetPortOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleEthernetPortOperStatus.setStatus("current")


class _SleEthernetPortTransmissionRate_Type(Integer32):
    """Custom type sleEthernetPortTransmissionRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 10),
        ValueRangeConstraint(100, 100),
        ValueRangeConstraint(1000, 1000),
        ValueRangeConstraint(2500, 2500),
        ValueRangeConstraint(10000, 10000),
    )


_SleEthernetPortTransmissionRate_Type.__name__ = "Integer32"
_SleEthernetPortTransmissionRate_Object = MibTableColumn
sleEthernetPortTransmissionRate = _SleEthernetPortTransmissionRate_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 2, 1, 1, 6),
    _SleEthernetPortTransmissionRate_Type()
)
sleEthernetPortTransmissionRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleEthernetPortTransmissionRate.setStatus("current")


class _SleEthernetPortDuplexMode_Type(Integer32):
    """Custom type sleEthernetPortDuplexMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("full", 1),
          ("half", 2),
          ("notAvailable", 3))
    )


_SleEthernetPortDuplexMode_Type.__name__ = "Integer32"
_SleEthernetPortDuplexMode_Object = MibTableColumn
sleEthernetPortDuplexMode = _SleEthernetPortDuplexMode_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 2, 1, 1, 7),
    _SleEthernetPortDuplexMode_Type()
)
sleEthernetPortDuplexMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleEthernetPortDuplexMode.setStatus("current")


class _SleEthernetPortFlowControl_Type(Integer32):
    """Custom type sleEthernetPortFlowControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabledSymetrical", 2),
          ("enabledAsymetrical", 3),
          ("enabledBoth", 4),
          ("notAvailable", 5))
    )


_SleEthernetPortFlowControl_Type.__name__ = "Integer32"
_SleEthernetPortFlowControl_Object = MibTableColumn
sleEthernetPortFlowControl = _SleEthernetPortFlowControl_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 2, 1, 1, 8),
    _SleEthernetPortFlowControl_Type()
)
sleEthernetPortFlowControl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleEthernetPortFlowControl.setStatus("current")


class _SleEthernetPortNegotiationMode_Type(Integer32):
    """Custom type sleEthernetPortNegotiationMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("auto", 1),
          ("force", 2),
          ("notAvailable", 3))
    )


_SleEthernetPortNegotiationMode_Type.__name__ = "Integer32"
_SleEthernetPortNegotiationMode_Object = MibTableColumn
sleEthernetPortNegotiationMode = _SleEthernetPortNegotiationMode_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 2, 1, 1, 9),
    _SleEthernetPortNegotiationMode_Type()
)
sleEthernetPortNegotiationMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleEthernetPortNegotiationMode.setStatus("current")


class _SleEthernetPortJumboFrameSize_Type(Integer32):
    """Custom type sleEthernetPortJumboFrameSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1518, 12288),
    )


_SleEthernetPortJumboFrameSize_Type.__name__ = "Integer32"
_SleEthernetPortJumboFrameSize_Object = MibTableColumn
sleEthernetPortJumboFrameSize = _SleEthernetPortJumboFrameSize_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 2, 1, 1, 10),
    _SleEthernetPortJumboFrameSize_Type()
)
sleEthernetPortJumboFrameSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleEthernetPortJumboFrameSize.setStatus("current")


class _SleEthernetPortSfpTransceiver_Type(Integer32):
    """Custom type sleEthernetPortSfpTransceiver based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 0),
          ("electrical", 1),
          ("electricalCoaxial", 2),
          ("opticalLongHaul", 3),
          ("opticalShortHaul", 4),
          ("optical10G", 5),
          ("opticalGpon", 6))
    )


_SleEthernetPortSfpTransceiver_Type.__name__ = "Integer32"
_SleEthernetPortSfpTransceiver_Object = MibTableColumn
sleEthernetPortSfpTransceiver = _SleEthernetPortSfpTransceiver_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 2, 1, 1, 11),
    _SleEthernetPortSfpTransceiver_Type()
)
sleEthernetPortSfpTransceiver.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleEthernetPortSfpTransceiver.setStatus("current")
_SleEthernetPortSfpVendorName_Type = OctetString
_SleEthernetPortSfpVendorName_Object = MibTableColumn
sleEthernetPortSfpVendorName = _SleEthernetPortSfpVendorName_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 2, 1, 1, 12),
    _SleEthernetPortSfpVendorName_Type()
)
sleEthernetPortSfpVendorName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleEthernetPortSfpVendorName.setStatus("current")
_SleEthernetPortSfpVendorPartNumber_Type = OctetString
_SleEthernetPortSfpVendorPartNumber_Object = MibTableColumn
sleEthernetPortSfpVendorPartNumber = _SleEthernetPortSfpVendorPartNumber_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 2, 1, 1, 13),
    _SleEthernetPortSfpVendorPartNumber_Type()
)
sleEthernetPortSfpVendorPartNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleEthernetPortSfpVendorPartNumber.setStatus("current")
_SleEthernetPortSfpVendorRevision_Type = OctetString
_SleEthernetPortSfpVendorRevision_Object = MibTableColumn
sleEthernetPortSfpVendorRevision = _SleEthernetPortSfpVendorRevision_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 2, 1, 1, 14),
    _SleEthernetPortSfpVendorRevision_Type()
)
sleEthernetPortSfpVendorRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleEthernetPortSfpVendorRevision.setStatus("current")
_SleEthernetPortSfpVendorSerialNumber_Type = OctetString
_SleEthernetPortSfpVendorSerialNumber_Object = MibTableColumn
sleEthernetPortSfpVendorSerialNumber = _SleEthernetPortSfpVendorSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 2, 1, 1, 15),
    _SleEthernetPortSfpVendorSerialNumber_Type()
)
sleEthernetPortSfpVendorSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleEthernetPortSfpVendorSerialNumber.setStatus("current")
_SleEthernetPortSfpDateCode_Type = OctetString
_SleEthernetPortSfpDateCode_Object = MibTableColumn
sleEthernetPortSfpDateCode = _SleEthernetPortSfpDateCode_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 2, 1, 1, 16),
    _SleEthernetPortSfpDateCode_Type()
)
sleEthernetPortSfpDateCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleEthernetPortSfpDateCode.setStatus("current")
_SleEthernetPortPhysicalRemoteChassis_Type = OctetString
_SleEthernetPortPhysicalRemoteChassis_Object = MibTableColumn
sleEthernetPortPhysicalRemoteChassis = _SleEthernetPortPhysicalRemoteChassis_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 2, 1, 1, 17),
    _SleEthernetPortPhysicalRemoteChassis_Type()
)
sleEthernetPortPhysicalRemoteChassis.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleEthernetPortPhysicalRemoteChassis.setStatus("current")
_SleEthernetPortPhysicalRemoteSlot_Type = Integer32
_SleEthernetPortPhysicalRemoteSlot_Object = MibTableColumn
sleEthernetPortPhysicalRemoteSlot = _SleEthernetPortPhysicalRemoteSlot_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 2, 1, 1, 18),
    _SleEthernetPortPhysicalRemoteSlot_Type()
)
sleEthernetPortPhysicalRemoteSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleEthernetPortPhysicalRemoteSlot.setStatus("current")
_SleEthernetPortPhysicalRemotePort_Type = Integer32
_SleEthernetPortPhysicalRemotePort_Object = MibTableColumn
sleEthernetPortPhysicalRemotePort = _SleEthernetPortPhysicalRemotePort_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 2, 1, 1, 19),
    _SleEthernetPortPhysicalRemotePort_Type()
)
sleEthernetPortPhysicalRemotePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleEthernetPortPhysicalRemotePort.setStatus("current")


class _SleEthernetPortPhysicalLinkDiscoveryMode_Type(Integer32):
    """Custom type sleEthernetPortPhysicalLinkDiscoveryMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("manual", 2),
          ("automatic", 3))
    )


_SleEthernetPortPhysicalLinkDiscoveryMode_Type.__name__ = "Integer32"
_SleEthernetPortPhysicalLinkDiscoveryMode_Object = MibTableColumn
sleEthernetPortPhysicalLinkDiscoveryMode = _SleEthernetPortPhysicalLinkDiscoveryMode_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 2, 1, 1, 20),
    _SleEthernetPortPhysicalLinkDiscoveryMode_Type()
)
sleEthernetPortPhysicalLinkDiscoveryMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleEthernetPortPhysicalLinkDiscoveryMode.setStatus("current")


class _SleEthernetPortSfpTransceiverType_Type(Integer32):
    """Custom type sleEthernetPortSfpTransceiverType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              255)
        )
    )
    namedValues = NamedValues(
        *(("sfp", 1),
          ("gbit", 2),
          ("xfp", 3),
          ("unknown", 255))
    )


_SleEthernetPortSfpTransceiverType_Type.__name__ = "Integer32"
_SleEthernetPortSfpTransceiverType_Object = MibTableColumn
sleEthernetPortSfpTransceiverType = _SleEthernetPortSfpTransceiverType_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 2, 1, 1, 21),
    _SleEthernetPortSfpTransceiverType_Type()
)
sleEthernetPortSfpTransceiverType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleEthernetPortSfpTransceiverType.setStatus("current")


class _SleEthernetPortSfpTransceiverDetailType_Type(Integer32):
    """Custom type sleEthernetPortSfpTransceiverDetailType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              255)
        )
    )
    namedValues = NamedValues(
        *(("fiber1000Sx", 1),
          ("fiber1000Lx", 2),
          ("fiber1000Cx", 3),
          ("fiber1000T", 4),
          ("fiber100lLxLx10", 5),
          ("fiber100Fx", 6),
          ("fiberBx10", 7),
          ("fiberPx", 8),
          ("fiberOc3MmSr", 9),
          ("fiberOc3SmIr", 10),
          ("fiberOc3SmLr", 11),
          ("fiber1000Zx", 12),
          ("unknown", 255))
    )


_SleEthernetPortSfpTransceiverDetailType_Type.__name__ = "Integer32"
_SleEthernetPortSfpTransceiverDetailType_Object = MibTableColumn
sleEthernetPortSfpTransceiverDetailType = _SleEthernetPortSfpTransceiverDetailType_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 2, 1, 1, 22),
    _SleEthernetPortSfpTransceiverDetailType_Type()
)
sleEthernetPortSfpTransceiverDetailType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleEthernetPortSfpTransceiverDetailType.setStatus("current")
_SleEthernetPortSlotIndex_Type = Integer32
_SleEthernetPortSlotIndex_Object = MibTableColumn
sleEthernetPortSlotIndex = _SleEthernetPortSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 2, 1, 1, 23),
    _SleEthernetPortSlotIndex_Type()
)
sleEthernetPortSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleEthernetPortSlotIndex.setStatus("current")
_SleEthernetPortSlotPortIndex_Type = Integer32
_SleEthernetPortSlotPortIndex_Object = MibTableColumn
sleEthernetPortSlotPortIndex = _SleEthernetPortSlotPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 2, 1, 1, 24),
    _SleEthernetPortSlotPortIndex_Type()
)
sleEthernetPortSlotPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleEthernetPortSlotPortIndex.setStatus("current")


class _SleEthernetPortAdminTransmissionRate_Type(Integer32):
    """Custom type sleEthernetPortAdminTransmissionRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 10),
        ValueRangeConstraint(100, 100),
        ValueRangeConstraint(1000, 1000),
        ValueRangeConstraint(10000, 10000),
    )


_SleEthernetPortAdminTransmissionRate_Type.__name__ = "Integer32"
_SleEthernetPortAdminTransmissionRate_Object = MibTableColumn
sleEthernetPortAdminTransmissionRate = _SleEthernetPortAdminTransmissionRate_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 2, 1, 1, 25),
    _SleEthernetPortAdminTransmissionRate_Type()
)
sleEthernetPortAdminTransmissionRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleEthernetPortAdminTransmissionRate.setStatus("current")


class _SleEthernetPortAdminDuplexMode_Type(Integer32):
    """Custom type sleEthernetPortAdminDuplexMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("full", 1),
          ("half", 2),
          ("notAvailable", 255))
    )


_SleEthernetPortAdminDuplexMode_Type.__name__ = "Integer32"
_SleEthernetPortAdminDuplexMode_Object = MibTableColumn
sleEthernetPortAdminDuplexMode = _SleEthernetPortAdminDuplexMode_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 2, 1, 1, 26),
    _SleEthernetPortAdminDuplexMode_Type()
)
sleEthernetPortAdminDuplexMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleEthernetPortAdminDuplexMode.setStatus("current")


class _SleEthernetPortAdminFlowControl_Type(Integer32):
    """Custom type sleEthernetPortAdminFlowControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enableSend", 2),
          ("enableReceive", 3),
          ("enabledBoth", 4))
    )


_SleEthernetPortAdminFlowControl_Type.__name__ = "Integer32"
_SleEthernetPortAdminFlowControl_Object = MibTableColumn
sleEthernetPortAdminFlowControl = _SleEthernetPortAdminFlowControl_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 2, 1, 1, 27),
    _SleEthernetPortAdminFlowControl_Type()
)
sleEthernetPortAdminFlowControl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleEthernetPortAdminFlowControl.setStatus("current")


class _SleEthernetPortAdminNegotiationMode_Type(Integer32):
    """Custom type sleEthernetPortAdminNegotiationMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("auto", 1),
          ("force", 2),
          ("notAvailable", 255))
    )


_SleEthernetPortAdminNegotiationMode_Type.__name__ = "Integer32"
_SleEthernetPortAdminNegotiationMode_Object = MibTableColumn
sleEthernetPortAdminNegotiationMode = _SleEthernetPortAdminNegotiationMode_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 2, 1, 1, 28),
    _SleEthernetPortAdminNegotiationMode_Type()
)
sleEthernetPortAdminNegotiationMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleEthernetPortAdminNegotiationMode.setStatus("current")


class _SleEthernetPortAdminReason_Type(Integer32):
    """Custom type sleEthernetPortAdminReason based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("user", 1),
          ("xllcf", 2),
          ("all", 3))
    )


_SleEthernetPortAdminReason_Type.__name__ = "Integer32"
_SleEthernetPortAdminReason_Object = MibTableColumn
sleEthernetPortAdminReason = _SleEthernetPortAdminReason_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 2, 1, 1, 29),
    _SleEthernetPortAdminReason_Type()
)
sleEthernetPortAdminReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleEthernetPortAdminReason.setStatus("current")


class _SleEthernetPortLinkCheckTimer_Type(Integer32):
    """Custom type sleEthernetPortLinkCheckTimer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(20, 1000),
    )


_SleEthernetPortLinkCheckTimer_Type.__name__ = "Integer32"
_SleEthernetPortLinkCheckTimer_Object = MibTableColumn
sleEthernetPortLinkCheckTimer = _SleEthernetPortLinkCheckTimer_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 2, 1, 1, 30),
    _SleEthernetPortLinkCheckTimer_Type()
)
sleEthernetPortLinkCheckTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleEthernetPortLinkCheckTimer.setStatus("current")


class _SleEthernetPortLinkDebounceTime_Type(Integer32):
    """Custom type sleEthernetPortLinkDebounceTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(10, 5000),
    )


_SleEthernetPortLinkDebounceTime_Type.__name__ = "Integer32"
_SleEthernetPortLinkDebounceTime_Object = MibTableColumn
sleEthernetPortLinkDebounceTime = _SleEthernetPortLinkDebounceTime_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 2, 1, 1, 31),
    _SleEthernetPortLinkDebounceTime_Type()
)
sleEthernetPortLinkDebounceTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleEthernetPortLinkDebounceTime.setStatus("current")


class _SleEthernetPortCpuStatisticsLimitUnicast_Type(Integer32):
    """Custom type sleEthernetPortCpuStatisticsLimitUnicast based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(10, 100),
    )


_SleEthernetPortCpuStatisticsLimitUnicast_Type.__name__ = "Integer32"
_SleEthernetPortCpuStatisticsLimitUnicast_Object = MibTableColumn
sleEthernetPortCpuStatisticsLimitUnicast = _SleEthernetPortCpuStatisticsLimitUnicast_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 2, 1, 1, 32),
    _SleEthernetPortCpuStatisticsLimitUnicast_Type()
)
sleEthernetPortCpuStatisticsLimitUnicast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleEthernetPortCpuStatisticsLimitUnicast.setStatus("current")


class _SleEthernetPortCpuStatisticsLimitMulticast_Type(Integer32):
    """Custom type sleEthernetPortCpuStatisticsLimitMulticast based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(10, 100),
    )


_SleEthernetPortCpuStatisticsLimitMulticast_Type.__name__ = "Integer32"
_SleEthernetPortCpuStatisticsLimitMulticast_Object = MibTableColumn
sleEthernetPortCpuStatisticsLimitMulticast = _SleEthernetPortCpuStatisticsLimitMulticast_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 2, 1, 1, 33),
    _SleEthernetPortCpuStatisticsLimitMulticast_Type()
)
sleEthernetPortCpuStatisticsLimitMulticast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleEthernetPortCpuStatisticsLimitMulticast.setStatus("current")


class _SleEthernetPortCpuStatisticsLimitBroadcast_Type(Integer32):
    """Custom type sleEthernetPortCpuStatisticsLimitBroadcast based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(10, 100),
    )


_SleEthernetPortCpuStatisticsLimitBroadcast_Type.__name__ = "Integer32"
_SleEthernetPortCpuStatisticsLimitBroadcast_Object = MibTableColumn
sleEthernetPortCpuStatisticsLimitBroadcast = _SleEthernetPortCpuStatisticsLimitBroadcast_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 2, 1, 1, 34),
    _SleEthernetPortCpuStatisticsLimitBroadcast_Type()
)
sleEthernetPortCpuStatisticsLimitBroadcast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleEthernetPortCpuStatisticsLimitBroadcast.setStatus("current")


class _SleEthernetPortFloodBlockBroadcastState_Type(Integer32):
    """Custom type sleEthernetPortFloodBlockBroadcastState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_SleEthernetPortFloodBlockBroadcastState_Type.__name__ = "Integer32"
_SleEthernetPortFloodBlockBroadcastState_Object = MibTableColumn
sleEthernetPortFloodBlockBroadcastState = _SleEthernetPortFloodBlockBroadcastState_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 2, 1, 1, 35),
    _SleEthernetPortFloodBlockBroadcastState_Type()
)
sleEthernetPortFloodBlockBroadcastState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleEthernetPortFloodBlockBroadcastState.setStatus("current")


class _SleEthernetPortFloodBlockDlfState_Type(Integer32):
    """Custom type sleEthernetPortFloodBlockDlfState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_SleEthernetPortFloodBlockDlfState_Type.__name__ = "Integer32"
_SleEthernetPortFloodBlockDlfState_Object = MibTableColumn
sleEthernetPortFloodBlockDlfState = _SleEthernetPortFloodBlockDlfState_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 2, 1, 1, 36),
    _SleEthernetPortFloodBlockDlfState_Type()
)
sleEthernetPortFloodBlockDlfState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleEthernetPortFloodBlockDlfState.setStatus("current")
_SleEthernetPortControl_ObjectIdentity = ObjectIdentity
sleEthernetPortControl = _SleEthernetPortControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 2, 2)
)


class _SleEthernetPortControlRequest_Type(Integer32):
    """Custom type sleEthernetPortControlRequest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("setEthernetPortProfile", 1),
          ("setEthernetPortLinkProfile", 2),
          ("setEhternetPortCpuStatisticsLimitProfile", 3),
          ("setEthernetPortFloodBlockStateProfile", 4))
    )


_SleEthernetPortControlRequest_Type.__name__ = "Integer32"
_SleEthernetPortControlRequest_Object = MibScalar
sleEthernetPortControlRequest = _SleEthernetPortControlRequest_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 2, 2, 1),
    _SleEthernetPortControlRequest_Type()
)
sleEthernetPortControlRequest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleEthernetPortControlRequest.setStatus("current")
_SleEthernetPortControlStatus_Type = SleControlStatusType
_SleEthernetPortControlStatus_Object = MibScalar
sleEthernetPortControlStatus = _SleEthernetPortControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 2, 2, 2),
    _SleEthernetPortControlStatus_Type()
)
sleEthernetPortControlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleEthernetPortControlStatus.setStatus("current")
_SleEthernetPortControlTimer_Type = Gauge32
_SleEthernetPortControlTimer_Object = MibScalar
sleEthernetPortControlTimer = _SleEthernetPortControlTimer_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 2, 2, 3),
    _SleEthernetPortControlTimer_Type()
)
sleEthernetPortControlTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleEthernetPortControlTimer.setStatus("current")
_SleEthernetPortControlTimeStamp_Type = TimeTicks
_SleEthernetPortControlTimeStamp_Object = MibScalar
sleEthernetPortControlTimeStamp = _SleEthernetPortControlTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 2, 2, 4),
    _SleEthernetPortControlTimeStamp_Type()
)
sleEthernetPortControlTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleEthernetPortControlTimeStamp.setStatus("current")
_SleEthernetPortControlReqResult_Type = SleControlRequestResultType
_SleEthernetPortControlReqResult_Object = MibScalar
sleEthernetPortControlReqResult = _SleEthernetPortControlReqResult_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 2, 2, 5),
    _SleEthernetPortControlReqResult_Type()
)
sleEthernetPortControlReqResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleEthernetPortControlReqResult.setStatus("current")
_SleEthernetPortControlIndex_Type = Integer32
_SleEthernetPortControlIndex_Object = MibScalar
sleEthernetPortControlIndex = _SleEthernetPortControlIndex_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 2, 2, 6),
    _SleEthernetPortControlIndex_Type()
)
sleEthernetPortControlIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleEthernetPortControlIndex.setStatus("current")


class _SleEthernetPortControlType_Type(Integer32):
    """Custom type sleEthernetPortControlType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 0),
          ("electrical", 1),
          ("optical", 2))
    )


_SleEthernetPortControlType_Type.__name__ = "Integer32"
_SleEthernetPortControlType_Object = MibScalar
sleEthernetPortControlType = _SleEthernetPortControlType_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 2, 2, 7),
    _SleEthernetPortControlType_Type()
)
sleEthernetPortControlType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleEthernetPortControlType.setStatus("current")


class _SleEthernetPortControlAdminStatus_Type(Integer32):
    """Custom type sleEthernetPortControlAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("up", 1),
          ("down", 2),
          ("notAvailable", 3))
    )


_SleEthernetPortControlAdminStatus_Type.__name__ = "Integer32"
_SleEthernetPortControlAdminStatus_Object = MibScalar
sleEthernetPortControlAdminStatus = _SleEthernetPortControlAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 2, 2, 8),
    _SleEthernetPortControlAdminStatus_Type()
)
sleEthernetPortControlAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleEthernetPortControlAdminStatus.setStatus("current")


class _SleEthernetPortControlTransmissionRate_Type(Integer32):
    """Custom type sleEthernetPortControlTransmissionRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 10),
        ValueRangeConstraint(100, 100),
        ValueRangeConstraint(1000, 1000),
        ValueRangeConstraint(2500, 2500),
        ValueRangeConstraint(10000, 10000),
    )


_SleEthernetPortControlTransmissionRate_Type.__name__ = "Integer32"
_SleEthernetPortControlTransmissionRate_Object = MibScalar
sleEthernetPortControlTransmissionRate = _SleEthernetPortControlTransmissionRate_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 2, 2, 9),
    _SleEthernetPortControlTransmissionRate_Type()
)
sleEthernetPortControlTransmissionRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleEthernetPortControlTransmissionRate.setStatus("current")


class _SleEthernetPortControlDuplexMode_Type(Integer32):
    """Custom type sleEthernetPortControlDuplexMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("full", 1),
          ("half", 2),
          ("notAvailable", 3))
    )


_SleEthernetPortControlDuplexMode_Type.__name__ = "Integer32"
_SleEthernetPortControlDuplexMode_Object = MibScalar
sleEthernetPortControlDuplexMode = _SleEthernetPortControlDuplexMode_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 2, 2, 10),
    _SleEthernetPortControlDuplexMode_Type()
)
sleEthernetPortControlDuplexMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleEthernetPortControlDuplexMode.setStatus("current")


class _SleEthernetPortControlFlowControl_Type(Integer32):
    """Custom type sleEthernetPortControlFlowControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabledSymetrical", 2),
          ("enabledAsymetrical", 3),
          ("enabledBoth", 4),
          ("notAvailable", 5))
    )


_SleEthernetPortControlFlowControl_Type.__name__ = "Integer32"
_SleEthernetPortControlFlowControl_Object = MibScalar
sleEthernetPortControlFlowControl = _SleEthernetPortControlFlowControl_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 2, 2, 11),
    _SleEthernetPortControlFlowControl_Type()
)
sleEthernetPortControlFlowControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleEthernetPortControlFlowControl.setStatus("current")


class _SleEthernetPortControlNegotiationMode_Type(Integer32):
    """Custom type sleEthernetPortControlNegotiationMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("auto", 1),
          ("force", 2),
          ("notAvailable", 3))
    )


_SleEthernetPortControlNegotiationMode_Type.__name__ = "Integer32"
_SleEthernetPortControlNegotiationMode_Object = MibScalar
sleEthernetPortControlNegotiationMode = _SleEthernetPortControlNegotiationMode_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 2, 2, 12),
    _SleEthernetPortControlNegotiationMode_Type()
)
sleEthernetPortControlNegotiationMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleEthernetPortControlNegotiationMode.setStatus("current")


class _SleEthernetPortControlJumboFrameSize_Type(Integer32):
    """Custom type sleEthernetPortControlJumboFrameSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1518, 12288),
    )


_SleEthernetPortControlJumboFrameSize_Type.__name__ = "Integer32"
_SleEthernetPortControlJumboFrameSize_Object = MibScalar
sleEthernetPortControlJumboFrameSize = _SleEthernetPortControlJumboFrameSize_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 2, 2, 13),
    _SleEthernetPortControlJumboFrameSize_Type()
)
sleEthernetPortControlJumboFrameSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleEthernetPortControlJumboFrameSize.setStatus("current")
_SleEthernetPortControlPhysicalRemoteChassis_Type = OctetString
_SleEthernetPortControlPhysicalRemoteChassis_Object = MibScalar
sleEthernetPortControlPhysicalRemoteChassis = _SleEthernetPortControlPhysicalRemoteChassis_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 2, 2, 14),
    _SleEthernetPortControlPhysicalRemoteChassis_Type()
)
sleEthernetPortControlPhysicalRemoteChassis.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleEthernetPortControlPhysicalRemoteChassis.setStatus("current")
_SleEthernetPortControlPhysicalRemoteSlot_Type = Integer32
_SleEthernetPortControlPhysicalRemoteSlot_Object = MibScalar
sleEthernetPortControlPhysicalRemoteSlot = _SleEthernetPortControlPhysicalRemoteSlot_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 2, 2, 15),
    _SleEthernetPortControlPhysicalRemoteSlot_Type()
)
sleEthernetPortControlPhysicalRemoteSlot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleEthernetPortControlPhysicalRemoteSlot.setStatus("current")
_SleEthernetPortControlPhysicalRemotePort_Type = Integer32
_SleEthernetPortControlPhysicalRemotePort_Object = MibScalar
sleEthernetPortControlPhysicalRemotePort = _SleEthernetPortControlPhysicalRemotePort_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 2, 2, 16),
    _SleEthernetPortControlPhysicalRemotePort_Type()
)
sleEthernetPortControlPhysicalRemotePort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleEthernetPortControlPhysicalRemotePort.setStatus("current")


class _SleEthernetPortControlPhysicalLinkDiscoveryMode_Type(Integer32):
    """Custom type sleEthernetPortControlPhysicalLinkDiscoveryMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("manual", 2),
          ("automatic", 3))
    )


_SleEthernetPortControlPhysicalLinkDiscoveryMode_Type.__name__ = "Integer32"
_SleEthernetPortControlPhysicalLinkDiscoveryMode_Object = MibScalar
sleEthernetPortControlPhysicalLinkDiscoveryMode = _SleEthernetPortControlPhysicalLinkDiscoveryMode_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 2, 2, 17),
    _SleEthernetPortControlPhysicalLinkDiscoveryMode_Type()
)
sleEthernetPortControlPhysicalLinkDiscoveryMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleEthernetPortControlPhysicalLinkDiscoveryMode.setStatus("current")


class _SleEthernetPortControlLinkCheckTimer_Type(Integer32):
    """Custom type sleEthernetPortControlLinkCheckTimer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(20, 1000),
    )


_SleEthernetPortControlLinkCheckTimer_Type.__name__ = "Integer32"
_SleEthernetPortControlLinkCheckTimer_Object = MibScalar
sleEthernetPortControlLinkCheckTimer = _SleEthernetPortControlLinkCheckTimer_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 2, 2, 18),
    _SleEthernetPortControlLinkCheckTimer_Type()
)
sleEthernetPortControlLinkCheckTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleEthernetPortControlLinkCheckTimer.setStatus("current")


class _SleEthernetPortControlLinkDebounceTime_Type(Integer32):
    """Custom type sleEthernetPortControlLinkDebounceTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(10, 5000),
    )


_SleEthernetPortControlLinkDebounceTime_Type.__name__ = "Integer32"
_SleEthernetPortControlLinkDebounceTime_Object = MibScalar
sleEthernetPortControlLinkDebounceTime = _SleEthernetPortControlLinkDebounceTime_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 2, 2, 19),
    _SleEthernetPortControlLinkDebounceTime_Type()
)
sleEthernetPortControlLinkDebounceTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleEthernetPortControlLinkDebounceTime.setStatus("current")


class _SleEthernetPortControlCpuStatisticsLimitUnicast_Type(Integer32):
    """Custom type sleEthernetPortControlCpuStatisticsLimitUnicast based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(10, 100),
    )


_SleEthernetPortControlCpuStatisticsLimitUnicast_Type.__name__ = "Integer32"
_SleEthernetPortControlCpuStatisticsLimitUnicast_Object = MibScalar
sleEthernetPortControlCpuStatisticsLimitUnicast = _SleEthernetPortControlCpuStatisticsLimitUnicast_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 2, 2, 20),
    _SleEthernetPortControlCpuStatisticsLimitUnicast_Type()
)
sleEthernetPortControlCpuStatisticsLimitUnicast.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleEthernetPortControlCpuStatisticsLimitUnicast.setStatus("current")


class _SleEthernetPortControlCpuStatisticsLimitMulticast_Type(Integer32):
    """Custom type sleEthernetPortControlCpuStatisticsLimitMulticast based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(10, 100),
    )


_SleEthernetPortControlCpuStatisticsLimitMulticast_Type.__name__ = "Integer32"
_SleEthernetPortControlCpuStatisticsLimitMulticast_Object = MibScalar
sleEthernetPortControlCpuStatisticsLimitMulticast = _SleEthernetPortControlCpuStatisticsLimitMulticast_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 2, 2, 21),
    _SleEthernetPortControlCpuStatisticsLimitMulticast_Type()
)
sleEthernetPortControlCpuStatisticsLimitMulticast.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleEthernetPortControlCpuStatisticsLimitMulticast.setStatus("current")


class _SleEthernetPortControlCpuStatisticsLimitBroadcast_Type(Integer32):
    """Custom type sleEthernetPortControlCpuStatisticsLimitBroadcast based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(10, 100),
    )


_SleEthernetPortControlCpuStatisticsLimitBroadcast_Type.__name__ = "Integer32"
_SleEthernetPortControlCpuStatisticsLimitBroadcast_Object = MibScalar
sleEthernetPortControlCpuStatisticsLimitBroadcast = _SleEthernetPortControlCpuStatisticsLimitBroadcast_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 2, 2, 22),
    _SleEthernetPortControlCpuStatisticsLimitBroadcast_Type()
)
sleEthernetPortControlCpuStatisticsLimitBroadcast.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleEthernetPortControlCpuStatisticsLimitBroadcast.setStatus("current")


class _SleEthernetPortControlFloodBlockBroadcastState_Type(Integer32):
    """Custom type sleEthernetPortControlFloodBlockBroadcastState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_SleEthernetPortControlFloodBlockBroadcastState_Type.__name__ = "Integer32"
_SleEthernetPortControlFloodBlockBroadcastState_Object = MibScalar
sleEthernetPortControlFloodBlockBroadcastState = _SleEthernetPortControlFloodBlockBroadcastState_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 2, 2, 23),
    _SleEthernetPortControlFloodBlockBroadcastState_Type()
)
sleEthernetPortControlFloodBlockBroadcastState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleEthernetPortControlFloodBlockBroadcastState.setStatus("current")


class _SleEthernetPortControlFloodBlockDlfState_Type(Integer32):
    """Custom type sleEthernetPortControlFloodBlockDlfState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_SleEthernetPortControlFloodBlockDlfState_Type.__name__ = "Integer32"
_SleEthernetPortControlFloodBlockDlfState_Object = MibScalar
sleEthernetPortControlFloodBlockDlfState = _SleEthernetPortControlFloodBlockDlfState_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 2, 2, 24),
    _SleEthernetPortControlFloodBlockDlfState_Type()
)
sleEthernetPortControlFloodBlockDlfState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleEthernetPortControlFloodBlockDlfState.setStatus("current")
_SleEthernetPortNotification_ObjectIdentity = ObjectIdentity
sleEthernetPortNotification = _SleEthernetPortNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 2, 3)
)
_SleEthernetPortDMITable_Object = MibTable
sleEthernetPortDMITable = _SleEthernetPortDMITable_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 2, 4)
)
if mibBuilder.loadTexts:
    sleEthernetPortDMITable.setStatus("current")
_SleEthernetPortDMIEntry_Object = MibTableRow
sleEthernetPortDMIEntry = _SleEthernetPortDMIEntry_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 2, 4, 1)
)
sleEthernetPortDMIEntry.setIndexNames(
    (0, "SLE-DEVICE-MIB", "sleEthernetPortDMIIndex"),
)
if mibBuilder.loadTexts:
    sleEthernetPortDMIEntry.setStatus("current")


class _SleEthernetPortDMIIndex_Type(Integer32):
    """Custom type sleEthernetPortDMIIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_SleEthernetPortDMIIndex_Type.__name__ = "Integer32"
_SleEthernetPortDMIIndex_Object = MibTableColumn
sleEthernetPortDMIIndex = _SleEthernetPortDMIIndex_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 2, 4, 1, 1),
    _SleEthernetPortDMIIndex_Type()
)
sleEthernetPortDMIIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleEthernetPortDMIIndex.setStatus("current")
_SleEthernetPortDMITemper_Type = OctetString
_SleEthernetPortDMITemper_Object = MibTableColumn
sleEthernetPortDMITemper = _SleEthernetPortDMITemper_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 2, 4, 1, 2),
    _SleEthernetPortDMITemper_Type()
)
sleEthernetPortDMITemper.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleEthernetPortDMITemper.setStatus("current")
_SleEthernetPortDMIVoltage_Type = OctetString
_SleEthernetPortDMIVoltage_Object = MibTableColumn
sleEthernetPortDMIVoltage = _SleEthernetPortDMIVoltage_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 2, 4, 1, 3),
    _SleEthernetPortDMIVoltage_Type()
)
sleEthernetPortDMIVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleEthernetPortDMIVoltage.setStatus("current")
_SleEthernetPortDMITxBias_Type = OctetString
_SleEthernetPortDMITxBias_Object = MibTableColumn
sleEthernetPortDMITxBias = _SleEthernetPortDMITxBias_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 2, 4, 1, 4),
    _SleEthernetPortDMITxBias_Type()
)
sleEthernetPortDMITxBias.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleEthernetPortDMITxBias.setStatus("current")
_SleEthernetPortDMITxPower_Type = OctetString
_SleEthernetPortDMITxPower_Object = MibTableColumn
sleEthernetPortDMITxPower = _SleEthernetPortDMITxPower_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 2, 4, 1, 5),
    _SleEthernetPortDMITxPower_Type()
)
sleEthernetPortDMITxPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleEthernetPortDMITxPower.setStatus("current")
_SleEthernetPortDMIRxPower_Type = OctetString
_SleEthernetPortDMIRxPower_Object = MibTableColumn
sleEthernetPortDMIRxPower = _SleEthernetPortDMIRxPower_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 2, 4, 1, 6),
    _SleEthernetPortDMIRxPower_Type()
)
sleEthernetPortDMIRxPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleEthernetPortDMIRxPower.setStatus("current")
_SleEthernetSFPTable_Object = MibTable
sleEthernetSFPTable = _SleEthernetSFPTable_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 2, 5)
)
if mibBuilder.loadTexts:
    sleEthernetSFPTable.setStatus("current")
_SleEthernetSFPEntry_Object = MibTableRow
sleEthernetSFPEntry = _SleEthernetSFPEntry_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 2, 5, 1)
)
sleEthernetSFPEntry.setIndexNames(
    (0, "SLE-DEVICE-MIB", "sleEthernetSfpIndex"),
)
if mibBuilder.loadTexts:
    sleEthernetSFPEntry.setStatus("current")


class _SleEthernetSfpIndex_Type(Integer32):
    """Custom type sleEthernetSfpIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65556),
    )


_SleEthernetSfpIndex_Type.__name__ = "Integer32"
_SleEthernetSfpIndex_Object = MibTableColumn
sleEthernetSfpIndex = _SleEthernetSfpIndex_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 2, 5, 1, 1),
    _SleEthernetSfpIndex_Type()
)
sleEthernetSfpIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleEthernetSfpIndex.setStatus("current")


class _SleEthernetSfpTransceiver_Type(Integer32):
    """Custom type sleEthernetSfpTransceiver based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 0),
          ("electrical", 1),
          ("electricalCoaxial", 2),
          ("opticalLongHaul", 3),
          ("opticalShortHaul", 4),
          ("optical10G", 5),
          ("opticalGpon", 6))
    )


_SleEthernetSfpTransceiver_Type.__name__ = "Integer32"
_SleEthernetSfpTransceiver_Object = MibTableColumn
sleEthernetSfpTransceiver = _SleEthernetSfpTransceiver_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 2, 5, 1, 2),
    _SleEthernetSfpTransceiver_Type()
)
sleEthernetSfpTransceiver.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleEthernetSfpTransceiver.setStatus("current")
_SleEthernetSfpVendorName_Type = OctetString
_SleEthernetSfpVendorName_Object = MibTableColumn
sleEthernetSfpVendorName = _SleEthernetSfpVendorName_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 2, 5, 1, 3),
    _SleEthernetSfpVendorName_Type()
)
sleEthernetSfpVendorName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleEthernetSfpVendorName.setStatus("current")
_SleEthernetSfpVendorPartNumber_Type = OctetString
_SleEthernetSfpVendorPartNumber_Object = MibTableColumn
sleEthernetSfpVendorPartNumber = _SleEthernetSfpVendorPartNumber_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 2, 5, 1, 4),
    _SleEthernetSfpVendorPartNumber_Type()
)
sleEthernetSfpVendorPartNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleEthernetSfpVendorPartNumber.setStatus("current")
_SleEthernetSfpVendorRevision_Type = OctetString
_SleEthernetSfpVendorRevision_Object = MibTableColumn
sleEthernetSfpVendorRevision = _SleEthernetSfpVendorRevision_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 2, 5, 1, 5),
    _SleEthernetSfpVendorRevision_Type()
)
sleEthernetSfpVendorRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleEthernetSfpVendorRevision.setStatus("current")
_SleEthernetSfpVendorSerialNumber_Type = OctetString
_SleEthernetSfpVendorSerialNumber_Object = MibTableColumn
sleEthernetSfpVendorSerialNumber = _SleEthernetSfpVendorSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 2, 5, 1, 6),
    _SleEthernetSfpVendorSerialNumber_Type()
)
sleEthernetSfpVendorSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleEthernetSfpVendorSerialNumber.setStatus("current")
_SleEthernetSfpDateCode_Type = OctetString
_SleEthernetSfpDateCode_Object = MibTableColumn
sleEthernetSfpDateCode = _SleEthernetSfpDateCode_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 2, 5, 1, 7),
    _SleEthernetSfpDateCode_Type()
)
sleEthernetSfpDateCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleEthernetSfpDateCode.setStatus("current")


class _SleEthernetSfpTransceiverType_Type(Integer32):
    """Custom type sleEthernetSfpTransceiverType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              255)
        )
    )
    namedValues = NamedValues(
        *(("sfp", 1),
          ("gbic", 2),
          ("xfp", 3),
          ("unknown", 255))
    )


_SleEthernetSfpTransceiverType_Type.__name__ = "Integer32"
_SleEthernetSfpTransceiverType_Object = MibTableColumn
sleEthernetSfpTransceiverType = _SleEthernetSfpTransceiverType_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 2, 5, 1, 8),
    _SleEthernetSfpTransceiverType_Type()
)
sleEthernetSfpTransceiverType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleEthernetSfpTransceiverType.setStatus("current")


class _SleEthernetSfpTransceiverDetailType_Type(Integer32):
    """Custom type sleEthernetSfpTransceiverDetailType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              64,
              65,
              66,
              67,
              68,
              69,
              70,
              71,
              255)
        )
    )
    namedValues = NamedValues(
        *(("fiber1000Sx", 1),
          ("fiber1000Lx", 2),
          ("fiber1000Cx", 3),
          ("fiber1000T", 4),
          ("fiber100lLxLx10", 5),
          ("fiber100Fx", 6),
          ("fiberBx10", 7),
          ("fiberPx", 8),
          ("fiberOc3MmSr", 9),
          ("fiberOc3SmIr", 10),
          ("fiberOc3SmLr", 11),
          ("fiber1000Zx", 12),
          ("base10GSR", 64),
          ("base10GLR", 65),
          ("base10GER", 66),
          ("base10GLRM", 67),
          ("base10GSW", 68),
          ("base10GLW", 69),
          ("base10GEW", 70),
          ("base10GEWorZW", 71),
          ("unknown", 255))
    )


_SleEthernetSfpTransceiverDetailType_Type.__name__ = "Integer32"
_SleEthernetSfpTransceiverDetailType_Object = MibTableColumn
sleEthernetSfpTransceiverDetailType = _SleEthernetSfpTransceiverDetailType_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 2, 5, 1, 9),
    _SleEthernetSfpTransceiverDetailType_Type()
)
sleEthernetSfpTransceiverDetailType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleEthernetSfpTransceiverDetailType.setStatus("current")


class _SleEthernetSfpTransceiverCodes_Type(OctetString):
    """Custom type sleEthernetSfpTransceiverCodes based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 8),
    )


_SleEthernetSfpTransceiverCodes_Type.__name__ = "OctetString"
_SleEthernetSfpTransceiverCodes_Object = MibTableColumn
sleEthernetSfpTransceiverCodes = _SleEthernetSfpTransceiverCodes_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 2, 5, 1, 10),
    _SleEthernetSfpTransceiverCodes_Type()
)
sleEthernetSfpTransceiverCodes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleEthernetSfpTransceiverCodes.setStatus("current")
_SleEthernetSfpSpeed_Type = OctetString
_SleEthernetSfpSpeed_Object = MibTableColumn
sleEthernetSfpSpeed = _SleEthernetSfpSpeed_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 2, 5, 1, 11),
    _SleEthernetSfpSpeed_Type()
)
sleEthernetSfpSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleEthernetSfpSpeed.setStatus("current")
_SleEthernetSfpLength_Type = Integer32
_SleEthernetSfpLength_Object = MibTableColumn
sleEthernetSfpLength = _SleEthernetSfpLength_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 2, 5, 1, 12),
    _SleEthernetSfpLength_Type()
)
sleEthernetSfpLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleEthernetSfpLength.setStatus("current")
_SleEthernetSfpWaveLength_Type = Integer32
_SleEthernetSfpWaveLength_Object = MibTableColumn
sleEthernetSfpWaveLength = _SleEthernetSfpWaveLength_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 2, 5, 1, 13),
    _SleEthernetSfpWaveLength_Type()
)
sleEthernetSfpWaveLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleEthernetSfpWaveLength.setStatus("current")
_SleEthernetSfpMultimodeLengthOm1_Type = Integer32
_SleEthernetSfpMultimodeLengthOm1_Object = MibTableColumn
sleEthernetSfpMultimodeLengthOm1 = _SleEthernetSfpMultimodeLengthOm1_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 2, 5, 1, 14),
    _SleEthernetSfpMultimodeLengthOm1_Type()
)
sleEthernetSfpMultimodeLengthOm1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleEthernetSfpMultimodeLengthOm1.setStatus("current")
_SleEthernetSfpMultimodeLengthOm2_Type = Integer32
_SleEthernetSfpMultimodeLengthOm2_Object = MibTableColumn
sleEthernetSfpMultimodeLengthOm2 = _SleEthernetSfpMultimodeLengthOm2_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 2, 5, 1, 15),
    _SleEthernetSfpMultimodeLengthOm2_Type()
)
sleEthernetSfpMultimodeLengthOm2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleEthernetSfpMultimodeLengthOm2.setStatus("current")
_SleEthernetSfpMultimodeLengthOm3_Type = Integer32
_SleEthernetSfpMultimodeLengthOm3_Object = MibTableColumn
sleEthernetSfpMultimodeLengthOm3 = _SleEthernetSfpMultimodeLengthOm3_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 2, 5, 1, 16),
    _SleEthernetSfpMultimodeLengthOm3_Type()
)
sleEthernetSfpMultimodeLengthOm3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleEthernetSfpMultimodeLengthOm3.setStatus("current")
_SleEthernetSfpTransceiverDetailTypeStr_Type = OctetString
_SleEthernetSfpTransceiverDetailTypeStr_Object = MibTableColumn
sleEthernetSfpTransceiverDetailTypeStr = _SleEthernetSfpTransceiverDetailTypeStr_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 2, 5, 1, 17),
    _SleEthernetSfpTransceiverDetailTypeStr_Type()
)
sleEthernetSfpTransceiverDetailTypeStr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleEthernetSfpTransceiverDetailTypeStr.setStatus("current")
_SleEthernetSfpTransceiverLengthStr_Type = OctetString
_SleEthernetSfpTransceiverLengthStr_Object = MibTableColumn
sleEthernetSfpTransceiverLengthStr = _SleEthernetSfpTransceiverLengthStr_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 2, 5, 1, 18),
    _SleEthernetSfpTransceiverLengthStr_Type()
)
sleEthernetSfpTransceiverLengthStr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleEthernetSfpTransceiverLengthStr.setStatus("current")
_SleEthernetSfpWaveLengthStr_Type = OctetString
_SleEthernetSfpWaveLengthStr_Object = MibTableColumn
sleEthernetSfpWaveLengthStr = _SleEthernetSfpWaveLengthStr_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 2, 5, 1, 19),
    _SleEthernetSfpWaveLengthStr_Type()
)
sleEthernetSfpWaveLengthStr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleEthernetSfpWaveLengthStr.setStatus("current")
_SleEthernetSfpConnectorType_Type = OctetString
_SleEthernetSfpConnectorType_Object = MibTableColumn
sleEthernetSfpConnectorType = _SleEthernetSfpConnectorType_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 2, 5, 1, 20),
    _SleEthernetSfpConnectorType_Type()
)
sleEthernetSfpConnectorType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleEthernetSfpConnectorType.setStatus("current")


class _SleEthernetSfpDdmState_Type(Integer32):
    """Custom type sleEthernetSfpDdmState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_SleEthernetSfpDdmState_Type.__name__ = "Integer32"
_SleEthernetSfpDdmState_Object = MibTableColumn
sleEthernetSfpDdmState = _SleEthernetSfpDdmState_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 2, 5, 1, 21),
    _SleEthernetSfpDdmState_Type()
)
sleEthernetSfpDdmState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleEthernetSfpDdmState.setStatus("current")


class _SleEthernetSfpNegoState_Type(Integer32):
    """Custom type sleEthernetSfpNegoState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_SleEthernetSfpNegoState_Type.__name__ = "Integer32"
_SleEthernetSfpNegoState_Object = MibTableColumn
sleEthernetSfpNegoState = _SleEthernetSfpNegoState_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 2, 5, 1, 22),
    _SleEthernetSfpNegoState_Type()
)
sleEthernetSfpNegoState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleEthernetSfpNegoState.setStatus("current")
_SleEthernetSFPControl_ObjectIdentity = ObjectIdentity
sleEthernetSFPControl = _SleEthernetSFPControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 2, 6)
)


class _SleEthernetSFPControlRequest_Type(Integer32):
    """Custom type sleEthernetSFPControlRequest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("setSFPRemoteReset", 1),
          ("setSFPDdmState", 2))
    )


_SleEthernetSFPControlRequest_Type.__name__ = "Integer32"
_SleEthernetSFPControlRequest_Object = MibScalar
sleEthernetSFPControlRequest = _SleEthernetSFPControlRequest_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 2, 6, 1),
    _SleEthernetSFPControlRequest_Type()
)
sleEthernetSFPControlRequest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleEthernetSFPControlRequest.setStatus("current")
_SleEthernetSFPControlStatus_Type = SleControlStatusType
_SleEthernetSFPControlStatus_Object = MibScalar
sleEthernetSFPControlStatus = _SleEthernetSFPControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 2, 6, 2),
    _SleEthernetSFPControlStatus_Type()
)
sleEthernetSFPControlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleEthernetSFPControlStatus.setStatus("current")
_SleEthernetSFPControlTimer_Type = Gauge32
_SleEthernetSFPControlTimer_Object = MibScalar
sleEthernetSFPControlTimer = _SleEthernetSFPControlTimer_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 2, 6, 3),
    _SleEthernetSFPControlTimer_Type()
)
sleEthernetSFPControlTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleEthernetSFPControlTimer.setStatus("current")
_SleEthernetSFPControlTimeStamp_Type = TimeTicks
_SleEthernetSFPControlTimeStamp_Object = MibScalar
sleEthernetSFPControlTimeStamp = _SleEthernetSFPControlTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 2, 6, 4),
    _SleEthernetSFPControlTimeStamp_Type()
)
sleEthernetSFPControlTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleEthernetSFPControlTimeStamp.setStatus("current")
_SleEthernetSFPControlReqResult_Type = SleControlRequestResultType
_SleEthernetSFPControlReqResult_Object = MibScalar
sleEthernetSFPControlReqResult = _SleEthernetSFPControlReqResult_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 2, 6, 5),
    _SleEthernetSFPControlReqResult_Type()
)
sleEthernetSFPControlReqResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleEthernetSFPControlReqResult.setStatus("current")
_SleEthernetSFPControlIndex_Type = Integer32
_SleEthernetSFPControlIndex_Object = MibScalar
sleEthernetSFPControlIndex = _SleEthernetSFPControlIndex_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 2, 6, 6),
    _SleEthernetSFPControlIndex_Type()
)
sleEthernetSFPControlIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleEthernetSFPControlIndex.setStatus("current")


class _SleEthernetSfpControlDdmState_Type(Integer32):
    """Custom type sleEthernetSfpControlDdmState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_SleEthernetSfpControlDdmState_Type.__name__ = "Integer32"
_SleEthernetSfpControlDdmState_Object = MibScalar
sleEthernetSfpControlDdmState = _SleEthernetSfpControlDdmState_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 2, 6, 7),
    _SleEthernetSfpControlDdmState_Type()
)
sleEthernetSfpControlDdmState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleEthernetSfpControlDdmState.setStatus("current")
_SleEthernetSFPNotification_ObjectIdentity = ObjectIdentity
sleEthernetSFPNotification = _SleEthernetSFPNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 2, 7)
)
_SleEthernetSFPThresholdTable_Object = MibTable
sleEthernetSFPThresholdTable = _SleEthernetSFPThresholdTable_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 2, 8)
)
if mibBuilder.loadTexts:
    sleEthernetSFPThresholdTable.setStatus("current")
_SleEthernetSFPThresholdEntry_Object = MibTableRow
sleEthernetSFPThresholdEntry = _SleEthernetSFPThresholdEntry_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 2, 8, 1)
)
sleEthernetSFPThresholdEntry.setIndexNames(
    (0, "SLE-DEVICE-MIB", "sleEthernetSFPThresholdIfIndex"),
    (0, "SLE-DEVICE-MIB", "sleEthernetSFPThresholdType"),
)
if mibBuilder.loadTexts:
    sleEthernetSFPThresholdEntry.setStatus("current")


class _SleEthernetSFPThresholdIfIndex_Type(Integer32):
    """Custom type sleEthernetSFPThresholdIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_SleEthernetSFPThresholdIfIndex_Type.__name__ = "Integer32"
_SleEthernetSFPThresholdIfIndex_Object = MibTableColumn
sleEthernetSFPThresholdIfIndex = _SleEthernetSFPThresholdIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 2, 8, 1, 1),
    _SleEthernetSFPThresholdIfIndex_Type()
)
sleEthernetSFPThresholdIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleEthernetSFPThresholdIfIndex.setStatus("current")


class _SleEthernetSFPThresholdType_Type(Integer32):
    """Custom type sleEthernetSFPThresholdType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10)
        )
    )
    namedValues = NamedValues(
        *(("temperWarning", 1),
          ("temperAlarm", 2),
          ("voltageWarning", 3),
          ("voltageAlarm", 4),
          ("txbiasWarning", 5),
          ("txbiasAlarm", 6),
          ("txpowerWarning", 7),
          ("txpowerAlarm", 8),
          ("rxpowerWarning", 9),
          ("rxpowerAlarm", 10))
    )


_SleEthernetSFPThresholdType_Type.__name__ = "Integer32"
_SleEthernetSFPThresholdType_Object = MibTableColumn
sleEthernetSFPThresholdType = _SleEthernetSFPThresholdType_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 2, 8, 1, 2),
    _SleEthernetSFPThresholdType_Type()
)
sleEthernetSFPThresholdType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleEthernetSFPThresholdType.setStatus("current")
_SleEthernetSFPThresholdSfpLow_Type = OctetString
_SleEthernetSFPThresholdSfpLow_Object = MibTableColumn
sleEthernetSFPThresholdSfpLow = _SleEthernetSFPThresholdSfpLow_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 2, 8, 1, 3),
    _SleEthernetSFPThresholdSfpLow_Type()
)
sleEthernetSFPThresholdSfpLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleEthernetSFPThresholdSfpLow.setStatus("current")
_SleEthernetSFPThresholdSfpHigh_Type = OctetString
_SleEthernetSFPThresholdSfpHigh_Object = MibTableColumn
sleEthernetSFPThresholdSfpHigh = _SleEthernetSFPThresholdSfpHigh_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 2, 8, 1, 4),
    _SleEthernetSFPThresholdSfpHigh_Type()
)
sleEthernetSFPThresholdSfpHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleEthernetSFPThresholdSfpHigh.setStatus("current")
_SleEthernetSFPThresholdSystemLow_Type = OctetString
_SleEthernetSFPThresholdSystemLow_Object = MibTableColumn
sleEthernetSFPThresholdSystemLow = _SleEthernetSFPThresholdSystemLow_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 2, 8, 1, 5),
    _SleEthernetSFPThresholdSystemLow_Type()
)
sleEthernetSFPThresholdSystemLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleEthernetSFPThresholdSystemLow.setStatus("current")
_SleEthernetSFPThresholdSystemHigh_Type = OctetString
_SleEthernetSFPThresholdSystemHigh_Object = MibTableColumn
sleEthernetSFPThresholdSystemHigh = _SleEthernetSFPThresholdSystemHigh_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 2, 8, 1, 6),
    _SleEthernetSFPThresholdSystemHigh_Type()
)
sleEthernetSFPThresholdSystemHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleEthernetSFPThresholdSystemHigh.setStatus("current")
_SleEthernetSFPThresholdControl_ObjectIdentity = ObjectIdentity
sleEthernetSFPThresholdControl = _SleEthernetSFPThresholdControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 2, 9)
)


class _SleEthernetSFPThresholdControlRequest_Type(Integer32):
    """Custom type sleEthernetSFPThresholdControlRequest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("setSfpThresholdModule", 1),
          ("setSystemThresholdModule", 2),
          ("delThresholdModule", 3))
    )


_SleEthernetSFPThresholdControlRequest_Type.__name__ = "Integer32"
_SleEthernetSFPThresholdControlRequest_Object = MibScalar
sleEthernetSFPThresholdControlRequest = _SleEthernetSFPThresholdControlRequest_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 2, 9, 1),
    _SleEthernetSFPThresholdControlRequest_Type()
)
sleEthernetSFPThresholdControlRequest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleEthernetSFPThresholdControlRequest.setStatus("current")
_SleEthernetSFPThresholdControlStatus_Type = SleControlStatusType
_SleEthernetSFPThresholdControlStatus_Object = MibScalar
sleEthernetSFPThresholdControlStatus = _SleEthernetSFPThresholdControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 2, 9, 2),
    _SleEthernetSFPThresholdControlStatus_Type()
)
sleEthernetSFPThresholdControlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleEthernetSFPThresholdControlStatus.setStatus("current")
_SleEthernetSFPThresholdControlTimer_Type = Gauge32
_SleEthernetSFPThresholdControlTimer_Object = MibScalar
sleEthernetSFPThresholdControlTimer = _SleEthernetSFPThresholdControlTimer_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 2, 9, 3),
    _SleEthernetSFPThresholdControlTimer_Type()
)
sleEthernetSFPThresholdControlTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleEthernetSFPThresholdControlTimer.setStatus("current")
_SleEthernetSFPThresholdControlTimeStamp_Type = TimeTicks
_SleEthernetSFPThresholdControlTimeStamp_Object = MibScalar
sleEthernetSFPThresholdControlTimeStamp = _SleEthernetSFPThresholdControlTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 2, 9, 4),
    _SleEthernetSFPThresholdControlTimeStamp_Type()
)
sleEthernetSFPThresholdControlTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleEthernetSFPThresholdControlTimeStamp.setStatus("current")
_SleEthernetSFPThresholdControlReqResult_Type = SleControlRequestResultType
_SleEthernetSFPThresholdControlReqResult_Object = MibScalar
sleEthernetSFPThresholdControlReqResult = _SleEthernetSFPThresholdControlReqResult_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 2, 9, 5),
    _SleEthernetSFPThresholdControlReqResult_Type()
)
sleEthernetSFPThresholdControlReqResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleEthernetSFPThresholdControlReqResult.setStatus("current")
_SleEthernetSFPThresholdControlIfIndex_Type = Integer32
_SleEthernetSFPThresholdControlIfIndex_Object = MibScalar
sleEthernetSFPThresholdControlIfIndex = _SleEthernetSFPThresholdControlIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 2, 9, 6),
    _SleEthernetSFPThresholdControlIfIndex_Type()
)
sleEthernetSFPThresholdControlIfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleEthernetSFPThresholdControlIfIndex.setStatus("current")


class _SleEthernetSFPThresholdControlType_Type(Integer32):
    """Custom type sleEthernetSFPThresholdControlType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10)
        )
    )
    namedValues = NamedValues(
        *(("temperWarning", 1),
          ("temperAlarm", 2),
          ("voltageWarning", 3),
          ("voltageAlarm", 4),
          ("txbiasWarning", 5),
          ("txbiasAlarm", 6),
          ("txpowerWarning", 7),
          ("txpowerAlarm", 8),
          ("rxpowerWarning", 9),
          ("rxpowerAlarm", 10))
    )


_SleEthernetSFPThresholdControlType_Type.__name__ = "Integer32"
_SleEthernetSFPThresholdControlType_Object = MibScalar
sleEthernetSFPThresholdControlType = _SleEthernetSFPThresholdControlType_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 2, 9, 7),
    _SleEthernetSFPThresholdControlType_Type()
)
sleEthernetSFPThresholdControlType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleEthernetSFPThresholdControlType.setStatus("current")
_SleEthernetSFPThresholdControlSfpLow_Type = OctetString
_SleEthernetSFPThresholdControlSfpLow_Object = MibScalar
sleEthernetSFPThresholdControlSfpLow = _SleEthernetSFPThresholdControlSfpLow_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 2, 9, 8),
    _SleEthernetSFPThresholdControlSfpLow_Type()
)
sleEthernetSFPThresholdControlSfpLow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleEthernetSFPThresholdControlSfpLow.setStatus("current")
_SleEthernetSFPThresholdControlSfpHigh_Type = OctetString
_SleEthernetSFPThresholdControlSfpHigh_Object = MibScalar
sleEthernetSFPThresholdControlSfpHigh = _SleEthernetSFPThresholdControlSfpHigh_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 2, 9, 9),
    _SleEthernetSFPThresholdControlSfpHigh_Type()
)
sleEthernetSFPThresholdControlSfpHigh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleEthernetSFPThresholdControlSfpHigh.setStatus("current")
_SleEthernetSFPThresholdControlSystemLow_Type = OctetString
_SleEthernetSFPThresholdControlSystemLow_Object = MibScalar
sleEthernetSFPThresholdControlSystemLow = _SleEthernetSFPThresholdControlSystemLow_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 2, 9, 10),
    _SleEthernetSFPThresholdControlSystemLow_Type()
)
sleEthernetSFPThresholdControlSystemLow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleEthernetSFPThresholdControlSystemLow.setStatus("current")
_SleEthernetSFPThresholdControlSystemHigh_Type = OctetString
_SleEthernetSFPThresholdControlSystemHigh_Object = MibScalar
sleEthernetSFPThresholdControlSystemHigh = _SleEthernetSFPThresholdControlSystemHigh_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 2, 9, 11),
    _SleEthernetSFPThresholdControlSystemHigh_Type()
)
sleEthernetSFPThresholdControlSystemHigh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleEthernetSFPThresholdControlSystemHigh.setStatus("current")
_SleEthernetSFPThresholdNotification_ObjectIdentity = ObjectIdentity
sleEthernetSFPThresholdNotification = _SleEthernetSFPThresholdNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 2, 10)
)
_SlePower_ObjectIdentity = ObjectIdentity
slePower = _SlePower_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 3)
)
_SlePowerTable_Object = MibTable
slePowerTable = _SlePowerTable_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 3, 1)
)
if mibBuilder.loadTexts:
    slePowerTable.setStatus("current")
_SlePowerEntry_Object = MibTableRow
slePowerEntry = _SlePowerEntry_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 3, 1, 1)
)
slePowerEntry.setIndexNames(
    (0, "SLE-DEVICE-MIB", "slePowerIndex"),
)
if mibBuilder.loadTexts:
    slePowerEntry.setStatus("current")


class _SlePowerIndex_Type(Integer32):
    """Custom type slePowerIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_SlePowerIndex_Type.__name__ = "Integer32"
_SlePowerIndex_Object = MibTableColumn
slePowerIndex = _SlePowerIndex_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 3, 1, 1, 1),
    _SlePowerIndex_Type()
)
slePowerIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slePowerIndex.setStatus("current")
_SlePowerPhyIndex_Type = Integer32
_SlePowerPhyIndex_Object = MibTableColumn
slePowerPhyIndex = _SlePowerPhyIndex_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 3, 1, 1, 2),
    _SlePowerPhyIndex_Type()
)
slePowerPhyIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slePowerPhyIndex.setStatus("current")


class _SlePowerState_Type(Integer32):
    """Custom type slePowerState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("failure", 0),
          ("ok", 1))
    )


_SlePowerState_Type.__name__ = "Integer32"
_SlePowerState_Object = MibTableColumn
slePowerState = _SlePowerState_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 3, 1, 1, 3),
    _SlePowerState_Type()
)
slePowerState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slePowerState.setStatus("current")


class _SlePowerType_Type(Integer32):
    """Custom type slePowerType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("ac", 1),
          ("dc", 2),
          ("unknown", 3),
          ("psu", 4))
    )


_SlePowerType_Type.__name__ = "Integer32"
_SlePowerType_Object = MibTableColumn
slePowerType = _SlePowerType_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 3, 1, 1, 4),
    _SlePowerType_Type()
)
slePowerType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slePowerType.setStatus("current")


class _SlePowerPSUType_Type(Integer32):
    """Custom type slePowerPSUType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("psuA", 1),
          ("psuS", 2),
          ("unknown", 255))
    )


_SlePowerPSUType_Type.__name__ = "Integer32"
_SlePowerPSUType_Object = MibTableColumn
slePowerPSUType = _SlePowerPSUType_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 3, 1, 1, 5),
    _SlePowerPSUType_Type()
)
slePowerPSUType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slePowerPSUType.setStatus("current")
_SleFanModule_ObjectIdentity = ObjectIdentity
sleFanModule = _SleFanModule_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 4)
)
_SleFanModuleTable_Object = MibTable
sleFanModuleTable = _SleFanModuleTable_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 4, 1)
)
if mibBuilder.loadTexts:
    sleFanModuleTable.setStatus("current")
_SleFanModuleEntry_Object = MibTableRow
sleFanModuleEntry = _SleFanModuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 4, 1, 1)
)
sleFanModuleEntry.setIndexNames(
    (0, "SLE-DEVICE-MIB", "sleFanModuleIndex"),
)
if mibBuilder.loadTexts:
    sleFanModuleEntry.setStatus("current")


class _SleFanModuleIndex_Type(Integer32):
    """Custom type sleFanModuleIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_SleFanModuleIndex_Type.__name__ = "Integer32"
_SleFanModuleIndex_Object = MibTableColumn
sleFanModuleIndex = _SleFanModuleIndex_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 4, 1, 1, 1),
    _SleFanModuleIndex_Type()
)
sleFanModuleIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleFanModuleIndex.setStatus("current")
_SleFanModulePhyIndex_Type = Integer32
_SleFanModulePhyIndex_Object = MibTableColumn
sleFanModulePhyIndex = _SleFanModulePhyIndex_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 4, 1, 1, 2),
    _SleFanModulePhyIndex_Type()
)
sleFanModulePhyIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleFanModulePhyIndex.setStatus("current")
_SleFanModuleUnitNum_Type = Integer32
_SleFanModuleUnitNum_Object = MibTableColumn
sleFanModuleUnitNum = _SleFanModuleUnitNum_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 4, 1, 1, 3),
    _SleFanModuleUnitNum_Type()
)
sleFanModuleUnitNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleFanModuleUnitNum.setStatus("current")


class _SleFanModuleAdminState_Type(Integer32):
    """Custom type sleFanModuleAdminState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1),
          ("auto", 2))
    )


_SleFanModuleAdminState_Type.__name__ = "Integer32"
_SleFanModuleAdminState_Object = MibTableColumn
sleFanModuleAdminState = _SleFanModuleAdminState_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 4, 1, 1, 4),
    _SleFanModuleAdminState_Type()
)
sleFanModuleAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleFanModuleAdminState.setStatus("current")
_SleFanModuleSpeedThreshold_Type = Integer32
_SleFanModuleSpeedThreshold_Object = MibTableColumn
sleFanModuleSpeedThreshold = _SleFanModuleSpeedThreshold_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 4, 1, 1, 5),
    _SleFanModuleSpeedThreshold_Type()
)
sleFanModuleSpeedThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleFanModuleSpeedThreshold.setStatus("current")
_SleFanModuleControl_ObjectIdentity = ObjectIdentity
sleFanModuleControl = _SleFanModuleControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 4, 2)
)


class _SleFanModuleControlRequest_Type(Integer32):
    """Custom type sleFanModuleControlRequest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("setFanAdminState", 1),
          ("setFanSpeedThreshold", 2))
    )


_SleFanModuleControlRequest_Type.__name__ = "Integer32"
_SleFanModuleControlRequest_Object = MibScalar
sleFanModuleControlRequest = _SleFanModuleControlRequest_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 4, 2, 1),
    _SleFanModuleControlRequest_Type()
)
sleFanModuleControlRequest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleFanModuleControlRequest.setStatus("current")
_SleFanModuleControlStatus_Type = SleControlStatusType
_SleFanModuleControlStatus_Object = MibScalar
sleFanModuleControlStatus = _SleFanModuleControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 4, 2, 2),
    _SleFanModuleControlStatus_Type()
)
sleFanModuleControlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleFanModuleControlStatus.setStatus("current")
_SleFanModuleControlTimer_Type = Gauge32
_SleFanModuleControlTimer_Object = MibScalar
sleFanModuleControlTimer = _SleFanModuleControlTimer_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 4, 2, 3),
    _SleFanModuleControlTimer_Type()
)
sleFanModuleControlTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleFanModuleControlTimer.setStatus("current")
_SleFanModuleControlTimeStamp_Type = TimeTicks
_SleFanModuleControlTimeStamp_Object = MibScalar
sleFanModuleControlTimeStamp = _SleFanModuleControlTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 4, 2, 4),
    _SleFanModuleControlTimeStamp_Type()
)
sleFanModuleControlTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleFanModuleControlTimeStamp.setStatus("current")
_SleFanModuleControlReqResult_Type = SleControlRequestResultType
_SleFanModuleControlReqResult_Object = MibScalar
sleFanModuleControlReqResult = _SleFanModuleControlReqResult_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 4, 2, 5),
    _SleFanModuleControlReqResult_Type()
)
sleFanModuleControlReqResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleFanModuleControlReqResult.setStatus("current")
_SleFanModuleControlIndex_Type = Integer32
_SleFanModuleControlIndex_Object = MibScalar
sleFanModuleControlIndex = _SleFanModuleControlIndex_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 4, 2, 6),
    _SleFanModuleControlIndex_Type()
)
sleFanModuleControlIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleFanModuleControlIndex.setStatus("current")


class _SleFanModuleControlAdminState_Type(Integer32):
    """Custom type sleFanModuleControlAdminState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1),
          ("auto", 2))
    )


_SleFanModuleControlAdminState_Type.__name__ = "Integer32"
_SleFanModuleControlAdminState_Object = MibScalar
sleFanModuleControlAdminState = _SleFanModuleControlAdminState_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 4, 2, 7),
    _SleFanModuleControlAdminState_Type()
)
sleFanModuleControlAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleFanModuleControlAdminState.setStatus("current")
_SleFanModuleControlSpeedThreshold_Type = Integer32
_SleFanModuleControlSpeedThreshold_Object = MibScalar
sleFanModuleControlSpeedThreshold = _SleFanModuleControlSpeedThreshold_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 4, 2, 8),
    _SleFanModuleControlSpeedThreshold_Type()
)
sleFanModuleControlSpeedThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleFanModuleControlSpeedThreshold.setStatus("current")
_SleFanModuleNotification_ObjectIdentity = ObjectIdentity
sleFanModuleNotification = _SleFanModuleNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 4, 3)
)
_SleFanUnit_ObjectIdentity = ObjectIdentity
sleFanUnit = _SleFanUnit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 5)
)
_SleFanUnitTable_Object = MibTable
sleFanUnitTable = _SleFanUnitTable_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 5, 1)
)
if mibBuilder.loadTexts:
    sleFanUnitTable.setStatus("current")
_SleFanUnitEntry_Object = MibTableRow
sleFanUnitEntry = _SleFanUnitEntry_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 5, 1, 1)
)
sleFanUnitEntry.setIndexNames(
    (0, "SLE-DEVICE-MIB", "sleFanModuleIndex"),
    (0, "SLE-DEVICE-MIB", "sleFanUnitIndex"),
)
if mibBuilder.loadTexts:
    sleFanUnitEntry.setStatus("current")


class _SleFanUnitIndex_Type(Integer32):
    """Custom type sleFanUnitIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_SleFanUnitIndex_Type.__name__ = "Integer32"
_SleFanUnitIndex_Object = MibTableColumn
sleFanUnitIndex = _SleFanUnitIndex_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 5, 1, 1, 1),
    _SleFanUnitIndex_Type()
)
sleFanUnitIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleFanUnitIndex.setStatus("current")


class _SleFanUnitOperState_Type(Integer32):
    """Custom type sleFanUnitOperState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("failure", 0),
          ("ok", 1),
          ("stop", 2))
    )


_SleFanUnitOperState_Type.__name__ = "Integer32"
_SleFanUnitOperState_Object = MibTableColumn
sleFanUnitOperState = _SleFanUnitOperState_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 5, 1, 1, 2),
    _SleFanUnitOperState_Type()
)
sleFanUnitOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleFanUnitOperState.setStatus("current")
_SleFanUnitSpeed_Type = Integer32
_SleFanUnitSpeed_Object = MibTableColumn
sleFanUnitSpeed = _SleFanUnitSpeed_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 5, 1, 1, 3),
    _SleFanUnitSpeed_Type()
)
sleFanUnitSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleFanUnitSpeed.setStatus("current")
_SleTemperature_ObjectIdentity = ObjectIdentity
sleTemperature = _SleTemperature_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 6)
)
_SleTemperatureTable_Object = MibTable
sleTemperatureTable = _SleTemperatureTable_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 6, 1)
)
if mibBuilder.loadTexts:
    sleTemperatureTable.setStatus("current")
_SleTemperatureEntry_Object = MibTableRow
sleTemperatureEntry = _SleTemperatureEntry_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 6, 1, 1)
)
sleTemperatureEntry.setIndexNames(
    (0, "SLE-DEVICE-MIB", "sleTemperatureIndex"),
)
if mibBuilder.loadTexts:
    sleTemperatureEntry.setStatus("current")


class _SleTemperatureIndex_Type(Integer32):
    """Custom type sleTemperatureIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_SleTemperatureIndex_Type.__name__ = "Integer32"
_SleTemperatureIndex_Object = MibTableColumn
sleTemperatureIndex = _SleTemperatureIndex_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 6, 1, 1, 1),
    _SleTemperatureIndex_Type()
)
sleTemperatureIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleTemperatureIndex.setStatus("current")


class _SleTemperatureState_Type(Integer32):
    """Custom type sleTemperatureState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("failure", 0),
          ("ok", 1),
          ("others", 2))
    )


_SleTemperatureState_Type.__name__ = "Integer32"
_SleTemperatureState_Object = MibTableColumn
sleTemperatureState = _SleTemperatureState_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 6, 1, 1, 2),
    _SleTemperatureState_Type()
)
sleTemperatureState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleTemperatureState.setStatus("current")
_SleTemperatureValue_Type = Integer32
_SleTemperatureValue_Object = MibTableColumn
sleTemperatureValue = _SleTemperatureValue_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 6, 1, 1, 3),
    _SleTemperatureValue_Type()
)
sleTemperatureValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleTemperatureValue.setStatus("current")
_SleTemperatureHighThreshold_Type = Integer32
_SleTemperatureHighThreshold_Object = MibTableColumn
sleTemperatureHighThreshold = _SleTemperatureHighThreshold_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 6, 1, 1, 4),
    _SleTemperatureHighThreshold_Type()
)
sleTemperatureHighThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleTemperatureHighThreshold.setStatus("current")
_SleTemperatureLowThreshold_Type = Integer32
_SleTemperatureLowThreshold_Object = MibTableColumn
sleTemperatureLowThreshold = _SleTemperatureLowThreshold_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 6, 1, 1, 5),
    _SleTemperatureLowThreshold_Type()
)
sleTemperatureLowThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleTemperatureLowThreshold.setStatus("current")


class _SleTemperatureWarnHighThreshold_Type(Integer32):
    """Custom type sleTemperatureWarnHighThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-40, 100),
    )


_SleTemperatureWarnHighThreshold_Type.__name__ = "Integer32"
_SleTemperatureWarnHighThreshold_Object = MibTableColumn
sleTemperatureWarnHighThreshold = _SleTemperatureWarnHighThreshold_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 6, 1, 1, 6),
    _SleTemperatureWarnHighThreshold_Type()
)
sleTemperatureWarnHighThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleTemperatureWarnHighThreshold.setStatus("current")


class _SleTemperatureWarnLowThreshold_Type(Integer32):
    """Custom type sleTemperatureWarnLowThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-40, 100),
    )


_SleTemperatureWarnLowThreshold_Type.__name__ = "Integer32"
_SleTemperatureWarnLowThreshold_Object = MibTableColumn
sleTemperatureWarnLowThreshold = _SleTemperatureWarnLowThreshold_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 6, 1, 1, 7),
    _SleTemperatureWarnLowThreshold_Type()
)
sleTemperatureWarnLowThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleTemperatureWarnLowThreshold.setStatus("current")


class _SleTemperatureWarnDuration_Type(Integer32):
    """Custom type sleTemperatureWarnDuration based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 300),
    )


_SleTemperatureWarnDuration_Type.__name__ = "Integer32"
_SleTemperatureWarnDuration_Object = MibTableColumn
sleTemperatureWarnDuration = _SleTemperatureWarnDuration_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 6, 1, 1, 8),
    _SleTemperatureWarnDuration_Type()
)
sleTemperatureWarnDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleTemperatureWarnDuration.setStatus("current")


class _SleTemperatureAlarmHighThreshold_Type(Integer32):
    """Custom type sleTemperatureAlarmHighThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-40, 100),
    )


_SleTemperatureAlarmHighThreshold_Type.__name__ = "Integer32"
_SleTemperatureAlarmHighThreshold_Object = MibTableColumn
sleTemperatureAlarmHighThreshold = _SleTemperatureAlarmHighThreshold_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 6, 1, 1, 9),
    _SleTemperatureAlarmHighThreshold_Type()
)
sleTemperatureAlarmHighThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleTemperatureAlarmHighThreshold.setStatus("current")


class _SleTemperatureAlarmLowThreshold_Type(Integer32):
    """Custom type sleTemperatureAlarmLowThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-40, 100),
    )


_SleTemperatureAlarmLowThreshold_Type.__name__ = "Integer32"
_SleTemperatureAlarmLowThreshold_Object = MibTableColumn
sleTemperatureAlarmLowThreshold = _SleTemperatureAlarmLowThreshold_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 6, 1, 1, 10),
    _SleTemperatureAlarmLowThreshold_Type()
)
sleTemperatureAlarmLowThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleTemperatureAlarmLowThreshold.setStatus("current")


class _SleTemperatureAlarmDuration_Type(Integer32):
    """Custom type sleTemperatureAlarmDuration based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 300),
    )


_SleTemperatureAlarmDuration_Type.__name__ = "Integer32"
_SleTemperatureAlarmDuration_Object = MibTableColumn
sleTemperatureAlarmDuration = _SleTemperatureAlarmDuration_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 6, 1, 1, 11),
    _SleTemperatureAlarmDuration_Type()
)
sleTemperatureAlarmDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleTemperatureAlarmDuration.setStatus("current")
_SleTemperatureControl_ObjectIdentity = ObjectIdentity
sleTemperatureControl = _SleTemperatureControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 6, 2)
)


class _SleTemperatureControlRequest_Type(Integer32):
    """Custom type sleTemperatureControlRequest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("setTempThreshold", 1),
          ("setTempAlarmThreshold", 2),
          ("setTempWarnThreshold", 3))
    )


_SleTemperatureControlRequest_Type.__name__ = "Integer32"
_SleTemperatureControlRequest_Object = MibScalar
sleTemperatureControlRequest = _SleTemperatureControlRequest_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 6, 2, 1),
    _SleTemperatureControlRequest_Type()
)
sleTemperatureControlRequest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleTemperatureControlRequest.setStatus("current")
_SleTemperatureControlStatus_Type = SleControlStatusType
_SleTemperatureControlStatus_Object = MibScalar
sleTemperatureControlStatus = _SleTemperatureControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 6, 2, 2),
    _SleTemperatureControlStatus_Type()
)
sleTemperatureControlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleTemperatureControlStatus.setStatus("current")
_SleTemperatureControlTimer_Type = Gauge32
_SleTemperatureControlTimer_Object = MibScalar
sleTemperatureControlTimer = _SleTemperatureControlTimer_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 6, 2, 3),
    _SleTemperatureControlTimer_Type()
)
sleTemperatureControlTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleTemperatureControlTimer.setStatus("current")
_SleTemperatureControlTimeStamp_Type = TimeTicks
_SleTemperatureControlTimeStamp_Object = MibScalar
sleTemperatureControlTimeStamp = _SleTemperatureControlTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 6, 2, 4),
    _SleTemperatureControlTimeStamp_Type()
)
sleTemperatureControlTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleTemperatureControlTimeStamp.setStatus("current")
_SleTemperatureControlReqResult_Type = SleControlRequestResultType
_SleTemperatureControlReqResult_Object = MibScalar
sleTemperatureControlReqResult = _SleTemperatureControlReqResult_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 6, 2, 5),
    _SleTemperatureControlReqResult_Type()
)
sleTemperatureControlReqResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleTemperatureControlReqResult.setStatus("current")
_SleTemperatureControlIndex_Type = Integer32
_SleTemperatureControlIndex_Object = MibScalar
sleTemperatureControlIndex = _SleTemperatureControlIndex_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 6, 2, 6),
    _SleTemperatureControlIndex_Type()
)
sleTemperatureControlIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleTemperatureControlIndex.setStatus("current")
_SleTemperatureControlHighThreshold_Type = Integer32
_SleTemperatureControlHighThreshold_Object = MibScalar
sleTemperatureControlHighThreshold = _SleTemperatureControlHighThreshold_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 6, 2, 7),
    _SleTemperatureControlHighThreshold_Type()
)
sleTemperatureControlHighThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleTemperatureControlHighThreshold.setStatus("current")
_SleTemperatureControlLowThreshold_Type = Integer32
_SleTemperatureControlLowThreshold_Object = MibScalar
sleTemperatureControlLowThreshold = _SleTemperatureControlLowThreshold_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 6, 2, 8),
    _SleTemperatureControlLowThreshold_Type()
)
sleTemperatureControlLowThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleTemperatureControlLowThreshold.setStatus("current")


class _SleTemperatureControlDuration_Type(Integer32):
    """Custom type sleTemperatureControlDuration based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 300),
    )


_SleTemperatureControlDuration_Type.__name__ = "Integer32"
_SleTemperatureControlDuration_Object = MibScalar
sleTemperatureControlDuration = _SleTemperatureControlDuration_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 6, 2, 9),
    _SleTemperatureControlDuration_Type()
)
sleTemperatureControlDuration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleTemperatureControlDuration.setStatus("current")
_SleTemperatureNotification_ObjectIdentity = ObjectIdentity
sleTemperatureNotification = _SleTemperatureNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 6, 3)
)
_SleBattery_ObjectIdentity = ObjectIdentity
sleBattery = _SleBattery_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 7)
)
_SleBatteryTable_Object = MibTable
sleBatteryTable = _SleBatteryTable_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 7, 1)
)
if mibBuilder.loadTexts:
    sleBatteryTable.setStatus("current")
_SleBatteryEntry_Object = MibTableRow
sleBatteryEntry = _SleBatteryEntry_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 7, 1, 1)
)
sleBatteryEntry.setIndexNames(
    (0, "SLE-DEVICE-MIB", "sleBatteryIndex"),
)
if mibBuilder.loadTexts:
    sleBatteryEntry.setStatus("current")


class _SleBatteryIndex_Type(Integer32):
    """Custom type sleBatteryIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 256),
    )


_SleBatteryIndex_Type.__name__ = "Integer32"
_SleBatteryIndex_Object = MibTableColumn
sleBatteryIndex = _SleBatteryIndex_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 7, 1, 1, 1),
    _SleBatteryIndex_Type()
)
sleBatteryIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleBatteryIndex.setStatus("current")


class _SleOperationPowerType_Type(Integer32):
    """Custom type sleOperationPowerType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ac", 0),
          ("rbu", 1))
    )


_SleOperationPowerType_Type.__name__ = "Integer32"
_SleOperationPowerType_Object = MibTableColumn
sleOperationPowerType = _SleOperationPowerType_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 7, 1, 1, 2),
    _SleOperationPowerType_Type()
)
sleOperationPowerType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleOperationPowerType.setStatus("current")
_SleOperationPowerInfo_Type = OctetString
_SleOperationPowerInfo_Object = MibTableColumn
sleOperationPowerInfo = _SleOperationPowerInfo_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 7, 1, 1, 3),
    _SleOperationPowerInfo_Type()
)
sleOperationPowerInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleOperationPowerInfo.setStatus("current")


class _SlePSUACPowerState_Type(Integer32):
    """Custom type slePSUACPowerState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ok", 0),
          ("fault", 1))
    )


_SlePSUACPowerState_Type.__name__ = "Integer32"
_SlePSUACPowerState_Object = MibTableColumn
slePSUACPowerState = _SlePSUACPowerState_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 7, 1, 1, 4),
    _SlePSUACPowerState_Type()
)
slePSUACPowerState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slePSUACPowerState.setStatus("current")
_SlePSUTemperture_Type = Integer32
_SlePSUTemperture_Object = MibTableColumn
slePSUTemperture = _SlePSUTemperture_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 7, 1, 1, 5),
    _SlePSUTemperture_Type()
)
slePSUTemperture.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slePSUTemperture.setStatus("current")
_SlePSUTempThreshold_Type = Integer32
_SlePSUTempThreshold_Object = MibTableColumn
slePSUTempThreshold = _SlePSUTempThreshold_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 7, 1, 1, 6),
    _SlePSUTempThreshold_Type()
)
slePSUTempThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slePSUTempThreshold.setStatus("current")
_SlePSUOutVoltage_Type = OctetString
_SlePSUOutVoltage_Object = MibTableColumn
slePSUOutVoltage = _SlePSUOutVoltage_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 7, 1, 1, 7),
    _SlePSUOutVoltage_Type()
)
slePSUOutVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slePSUOutVoltage.setStatus("current")


class _SlePSUOverTemp_Type(Integer32):
    """Custom type slePSUOverTemp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("normal", 0),
          ("over", 1))
    )


_SlePSUOverTemp_Type.__name__ = "Integer32"
_SlePSUOverTemp_Object = MibTableColumn
slePSUOverTemp = _SlePSUOverTemp_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 7, 1, 1, 8),
    _SlePSUOverTemp_Type()
)
slePSUOverTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slePSUOverTemp.setStatus("current")
_SlePSUFirmwareVer_Type = Integer32
_SlePSUFirmwareVer_Object = MibTableColumn
slePSUFirmwareVer = _SlePSUFirmwareVer_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 7, 1, 1, 9),
    _SlePSUFirmwareVer_Type()
)
slePSUFirmwareVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slePSUFirmwareVer.setStatus("current")


class _SleRBUEquipState_Type(Integer32):
    """Custom type sleRBUEquipState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("equipped", 0),
          ("empty", 1))
    )


_SleRBUEquipState_Type.__name__ = "Integer32"
_SleRBUEquipState_Object = MibTableColumn
sleRBUEquipState = _SleRBUEquipState_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 7, 1, 1, 10),
    _SleRBUEquipState_Type()
)
sleRBUEquipState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleRBUEquipState.setStatus("current")
_SleRBUModeStaus_Type = OctetString
_SleRBUModeStaus_Object = MibTableColumn
sleRBUModeStaus = _SleRBUModeStaus_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 7, 1, 1, 11),
    _SleRBUModeStaus_Type()
)
sleRBUModeStaus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleRBUModeStaus.setStatus("current")
_SleRBUTemperature1_Type = Integer32
_SleRBUTemperature1_Object = MibTableColumn
sleRBUTemperature1 = _SleRBUTemperature1_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 7, 1, 1, 12),
    _SleRBUTemperature1_Type()
)
sleRBUTemperature1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleRBUTemperature1.setStatus("current")
_SleRBUTemperature2_Type = Integer32
_SleRBUTemperature2_Object = MibTableColumn
sleRBUTemperature2 = _SleRBUTemperature2_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 7, 1, 1, 13),
    _SleRBUTemperature2_Type()
)
sleRBUTemperature2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleRBUTemperature2.setStatus("current")
_SleRBUTempLowThreshold_Type = Integer32
_SleRBUTempLowThreshold_Object = MibTableColumn
sleRBUTempLowThreshold = _SleRBUTempLowThreshold_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 7, 1, 1, 14),
    _SleRBUTempLowThreshold_Type()
)
sleRBUTempLowThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleRBUTempLowThreshold.setStatus("current")
_SleRBUOutVoltage_Type = OctetString
_SleRBUOutVoltage_Object = MibTableColumn
sleRBUOutVoltage = _SleRBUOutVoltage_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 7, 1, 1, 15),
    _SleRBUOutVoltage_Type()
)
sleRBUOutVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleRBUOutVoltage.setStatus("current")
_SleRBUChargeCurrent_Type = Integer32
_SleRBUChargeCurrent_Object = MibTableColumn
sleRBUChargeCurrent = _SleRBUChargeCurrent_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 7, 1, 1, 16),
    _SleRBUChargeCurrent_Type()
)
sleRBUChargeCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleRBUChargeCurrent.setStatus("current")
_SleRBURemainCapacity_Type = Integer32
_SleRBURemainCapacity_Object = MibTableColumn
sleRBURemainCapacity = _SleRBURemainCapacity_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 7, 1, 1, 17),
    _SleRBURemainCapacity_Type()
)
sleRBURemainCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleRBURemainCapacity.setStatus("current")


class _SleRBUOverTemp_Type(Integer32):
    """Custom type sleRBUOverTemp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("normal", 0),
          ("over", 1),
          ("under", 2))
    )


_SleRBUOverTemp_Type.__name__ = "Integer32"
_SleRBUOverTemp_Object = MibTableColumn
sleRBUOverTemp = _SleRBUOverTemp_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 7, 1, 1, 18),
    _SleRBUOverTemp_Type()
)
sleRBUOverTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleRBUOverTemp.setStatus("current")


class _SleBatteryLow_Type(Integer32):
    """Custom type sleBatteryLow based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("normal", 0),
          ("low", 1),
          ("notAvailable", 2))
    )


_SleBatteryLow_Type.__name__ = "Integer32"
_SleBatteryLow_Object = MibTableColumn
sleBatteryLow = _SleBatteryLow_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 7, 1, 1, 19),
    _SleBatteryLow_Type()
)
sleBatteryLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleBatteryLow.setStatus("current")
_SleRBUTempHighThreshold_Type = Integer32
_SleRBUTempHighThreshold_Object = MibTableColumn
sleRBUTempHighThreshold = _SleRBUTempHighThreshold_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 7, 1, 1, 20),
    _SleRBUTempHighThreshold_Type()
)
sleRBUTempHighThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleRBUTempHighThreshold.setStatus("current")


class _SleRBUBTStatus_Type(Integer32):
    """Custom type sleRBUBTStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_SleRBUBTStatus_Type.__name__ = "Integer32"
_SleRBUBTStatus_Object = MibTableColumn
sleRBUBTStatus = _SleRBUBTStatus_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 7, 1, 1, 21),
    _SleRBUBTStatus_Type()
)
sleRBUBTStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleRBUBTStatus.setStatus("current")
_SleRBUBTThreshold_Type = Integer32
_SleRBUBTThreshold_Object = MibTableColumn
sleRBUBTThreshold = _SleRBUBTThreshold_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 7, 1, 1, 22),
    _SleRBUBTThreshold_Type()
)
sleRBUBTThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleRBUBTThreshold.setStatus("current")
_SleRBURechargeVoltage_Type = Integer32
_SleRBURechargeVoltage_Object = MibTableColumn
sleRBURechargeVoltage = _SleRBURechargeVoltage_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 7, 1, 1, 23),
    _SleRBURechargeVoltage_Type()
)
sleRBURechargeVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleRBURechargeVoltage.setStatus("current")


class _SleBatteryCellStatus_Type(Integer32):
    """Custom type sleBatteryCellStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ok", 1),
          ("failure", 2))
    )


_SleBatteryCellStatus_Type.__name__ = "Integer32"
_SleBatteryCellStatus_Object = MibTableColumn
sleBatteryCellStatus = _SleBatteryCellStatus_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 7, 1, 1, 24),
    _SleBatteryCellStatus_Type()
)
sleBatteryCellStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleBatteryCellStatus.setStatus("current")
_SleBPSUACHardwareVer_Type = Integer32
_SleBPSUACHardwareVer_Object = MibTableColumn
sleBPSUACHardwareVer = _SleBPSUACHardwareVer_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 7, 1, 1, 25),
    _SleBPSUACHardwareVer_Type()
)
sleBPSUACHardwareVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleBPSUACHardwareVer.setStatus("current")
_SleBatteryControl_ObjectIdentity = ObjectIdentity
sleBatteryControl = _SleBatteryControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 7, 2)
)


class _SleBatteryControlRequest_Type(Integer32):
    """Custom type sleBatteryControlRequest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8)
        )
    )
    namedValues = NamedValues(
        *(("setBatteryForceCharge", 1),
          ("setBatteryChargingStart", 2),
          ("setBatteryForceChargeNonStop", 3),
          ("setBatteryBootingTimeStatus", 4),
          ("setBatteryBootingTime", 5),
          ("setBatteryRechargeVoltage", 6),
          ("setPsuAcTemperature", 7),
          ("setBatteryTemperature", 8))
    )


_SleBatteryControlRequest_Type.__name__ = "Integer32"
_SleBatteryControlRequest_Object = MibScalar
sleBatteryControlRequest = _SleBatteryControlRequest_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 7, 2, 1),
    _SleBatteryControlRequest_Type()
)
sleBatteryControlRequest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleBatteryControlRequest.setStatus("current")
_SleBatteryControlStatus_Type = Integer32
_SleBatteryControlStatus_Object = MibScalar
sleBatteryControlStatus = _SleBatteryControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 7, 2, 2),
    _SleBatteryControlStatus_Type()
)
sleBatteryControlStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleBatteryControlStatus.setStatus("current")
_SleBatteryControlTimer_Type = Integer32
_SleBatteryControlTimer_Object = MibScalar
sleBatteryControlTimer = _SleBatteryControlTimer_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 7, 2, 3),
    _SleBatteryControlTimer_Type()
)
sleBatteryControlTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleBatteryControlTimer.setStatus("current")
_SleBatteryControlTimeStamp_Type = Integer32
_SleBatteryControlTimeStamp_Object = MibScalar
sleBatteryControlTimeStamp = _SleBatteryControlTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 7, 2, 4),
    _SleBatteryControlTimeStamp_Type()
)
sleBatteryControlTimeStamp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleBatteryControlTimeStamp.setStatus("current")
_SleBatteryControlReqResult_Type = Integer32
_SleBatteryControlReqResult_Object = MibScalar
sleBatteryControlReqResult = _SleBatteryControlReqResult_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 7, 2, 5),
    _SleBatteryControlReqResult_Type()
)
sleBatteryControlReqResult.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleBatteryControlReqResult.setStatus("current")


class _SleBatteryControlRBUBTStatus_Type(Integer32):
    """Custom type sleBatteryControlRBUBTStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_SleBatteryControlRBUBTStatus_Type.__name__ = "Integer32"
_SleBatteryControlRBUBTStatus_Object = MibScalar
sleBatteryControlRBUBTStatus = _SleBatteryControlRBUBTStatus_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 7, 2, 6),
    _SleBatteryControlRBUBTStatus_Type()
)
sleBatteryControlRBUBTStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleBatteryControlRBUBTStatus.setStatus("current")
_SleBatteryControlRBUBTThreshold_Type = Integer32
_SleBatteryControlRBUBTThreshold_Object = MibScalar
sleBatteryControlRBUBTThreshold = _SleBatteryControlRBUBTThreshold_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 7, 2, 7),
    _SleBatteryControlRBUBTThreshold_Type()
)
sleBatteryControlRBUBTThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleBatteryControlRBUBTThreshold.setStatus("current")
_SleBatteryControlRBURechargeVoltage_Type = Integer32
_SleBatteryControlRBURechargeVoltage_Object = MibScalar
sleBatteryControlRBURechargeVoltage = _SleBatteryControlRBURechargeVoltage_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 7, 2, 8),
    _SleBatteryControlRBURechargeVoltage_Type()
)
sleBatteryControlRBURechargeVoltage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleBatteryControlRBURechargeVoltage.setStatus("current")
_SleBatteryControlTemperThresh1_Type = Integer32
_SleBatteryControlTemperThresh1_Object = MibScalar
sleBatteryControlTemperThresh1 = _SleBatteryControlTemperThresh1_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 7, 2, 9),
    _SleBatteryControlTemperThresh1_Type()
)
sleBatteryControlTemperThresh1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleBatteryControlTemperThresh1.setStatus("current")
_SleBatteryControlTemperThresh2_Type = Integer32
_SleBatteryControlTemperThresh2_Object = MibScalar
sleBatteryControlTemperThresh2 = _SleBatteryControlTemperThresh2_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 7, 2, 10),
    _SleBatteryControlTemperThresh2_Type()
)
sleBatteryControlTemperThresh2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleBatteryControlTemperThresh2.setStatus("current")
_SleBatteryNotification_ObjectIdentity = ObjectIdentity
sleBatteryNotification = _SleBatteryNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 7, 3)
)
_SleBatteryBackupTable_Object = MibTable
sleBatteryBackupTable = _SleBatteryBackupTable_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 7, 4)
)
if mibBuilder.loadTexts:
    sleBatteryBackupTable.setStatus("current")
_SleBatteryBackupEntry_Object = MibTableRow
sleBatteryBackupEntry = _SleBatteryBackupEntry_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 7, 4, 1)
)
sleBatteryBackupEntry.setIndexNames(
    (0, "SLE-DEVICE-MIB", "sleBatteryBackupFile"),
)
if mibBuilder.loadTexts:
    sleBatteryBackupEntry.setStatus("current")


class _SleBatteryBackupFile_Type(OctetString):
    """Custom type sleBatteryBackupFile based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_SleBatteryBackupFile_Type.__name__ = "OctetString"
_SleBatteryBackupFile_Object = MibTableColumn
sleBatteryBackupFile = _SleBatteryBackupFile_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 7, 4, 1, 1),
    _SleBatteryBackupFile_Type()
)
sleBatteryBackupFile.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleBatteryBackupFile.setStatus("current")
_SleBatteryBackupControl_ObjectIdentity = ObjectIdentity
sleBatteryBackupControl = _SleBatteryBackupControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 7, 5)
)


class _SleBatteryBackupControlRequest_Type(Integer32):
    """Custom type sleBatteryBackupControlRequest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("setBatteryBackupProfile", 1),
          ("setBatteryUpgrade", 2),
          ("clearBatteryBackupTable", 3))
    )


_SleBatteryBackupControlRequest_Type.__name__ = "Integer32"
_SleBatteryBackupControlRequest_Object = MibScalar
sleBatteryBackupControlRequest = _SleBatteryBackupControlRequest_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 7, 5, 1),
    _SleBatteryBackupControlRequest_Type()
)
sleBatteryBackupControlRequest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleBatteryBackupControlRequest.setStatus("current")
_SleBatteryBackupControlStatus_Type = SleControlStatusType
_SleBatteryBackupControlStatus_Object = MibScalar
sleBatteryBackupControlStatus = _SleBatteryBackupControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 7, 5, 2),
    _SleBatteryBackupControlStatus_Type()
)
sleBatteryBackupControlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleBatteryBackupControlStatus.setStatus("current")
_SleBatteryBackupControlTimer_Type = Gauge32
_SleBatteryBackupControlTimer_Object = MibScalar
sleBatteryBackupControlTimer = _SleBatteryBackupControlTimer_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 7, 5, 3),
    _SleBatteryBackupControlTimer_Type()
)
sleBatteryBackupControlTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleBatteryBackupControlTimer.setStatus("current")
_SleBatteryBackupControlTimeStamp_Type = TimeTicks
_SleBatteryBackupControlTimeStamp_Object = MibScalar
sleBatteryBackupControlTimeStamp = _SleBatteryBackupControlTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 7, 5, 4),
    _SleBatteryBackupControlTimeStamp_Type()
)
sleBatteryBackupControlTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleBatteryBackupControlTimeStamp.setStatus("current")
_SleBatteryBackupControlReqResult_Type = SleControlRequestResultType
_SleBatteryBackupControlReqResult_Object = MibScalar
sleBatteryBackupControlReqResult = _SleBatteryBackupControlReqResult_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 7, 5, 5),
    _SleBatteryBackupControlReqResult_Type()
)
sleBatteryBackupControlReqResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleBatteryBackupControlReqResult.setStatus("current")
_SleBatteryBackupControlServerIP_Type = IpAddress
_SleBatteryBackupControlServerIP_Object = MibScalar
sleBatteryBackupControlServerIP = _SleBatteryBackupControlServerIP_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 7, 5, 6),
    _SleBatteryBackupControlServerIP_Type()
)
sleBatteryBackupControlServerIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleBatteryBackupControlServerIP.setStatus("current")


class _SleBatteryBackupControlUserID_Type(OctetString):
    """Custom type sleBatteryBackupControlUserID based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_SleBatteryBackupControlUserID_Type.__name__ = "OctetString"
_SleBatteryBackupControlUserID_Object = MibScalar
sleBatteryBackupControlUserID = _SleBatteryBackupControlUserID_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 7, 5, 7),
    _SleBatteryBackupControlUserID_Type()
)
sleBatteryBackupControlUserID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleBatteryBackupControlUserID.setStatus("current")


class _SleBatteryBackupControlPassword_Type(OctetString):
    """Custom type sleBatteryBackupControlPassword based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_SleBatteryBackupControlPassword_Type.__name__ = "OctetString"
_SleBatteryBackupControlPassword_Object = MibScalar
sleBatteryBackupControlPassword = _SleBatteryBackupControlPassword_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 7, 5, 8),
    _SleBatteryBackupControlPassword_Type()
)
sleBatteryBackupControlPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleBatteryBackupControlPassword.setStatus("current")


class _SleBatteryBackupControlFlag_Type(Integer32):
    """Custom type sleBatteryBackupControlFlag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("download", 1),
          ("upload", 2))
    )


_SleBatteryBackupControlFlag_Type.__name__ = "Integer32"
_SleBatteryBackupControlFlag_Object = MibScalar
sleBatteryBackupControlFlag = _SleBatteryBackupControlFlag_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 7, 5, 9),
    _SleBatteryBackupControlFlag_Type()
)
sleBatteryBackupControlFlag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleBatteryBackupControlFlag.setStatus("current")


class _SleBatteryBackupControlLocalFile_Type(OctetString):
    """Custom type sleBatteryBackupControlLocalFile based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_SleBatteryBackupControlLocalFile_Type.__name__ = "OctetString"
_SleBatteryBackupControlLocalFile_Object = MibScalar
sleBatteryBackupControlLocalFile = _SleBatteryBackupControlLocalFile_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 7, 5, 10),
    _SleBatteryBackupControlLocalFile_Type()
)
sleBatteryBackupControlLocalFile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleBatteryBackupControlLocalFile.setStatus("current")


class _SleBatteryBackupControlRemoteFile_Type(OctetString):
    """Custom type sleBatteryBackupControlRemoteFile based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_SleBatteryBackupControlRemoteFile_Type.__name__ = "OctetString"
_SleBatteryBackupControlRemoteFile_Object = MibScalar
sleBatteryBackupControlRemoteFile = _SleBatteryBackupControlRemoteFile_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 7, 5, 11),
    _SleBatteryBackupControlRemoteFile_Type()
)
sleBatteryBackupControlRemoteFile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleBatteryBackupControlRemoteFile.setStatus("current")
_SleBatterBackupNotification_ObjectIdentity = ObjectIdentity
sleBatterBackupNotification = _SleBatterBackupNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 7, 6)
)
_SleDoor_ObjectIdentity = ObjectIdentity
sleDoor = _SleDoor_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 8)
)
_SleDoorInfo_ObjectIdentity = ObjectIdentity
sleDoorInfo = _SleDoorInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 8, 1)
)


class _SleDoorStatus_Type(Integer32):
    """Custom type sleDoorStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("close", 0),
          ("open", 1))
    )


_SleDoorStatus_Type.__name__ = "Integer32"
_SleDoorStatus_Object = MibScalar
sleDoorStatus = _SleDoorStatus_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 8, 1, 1),
    _SleDoorStatus_Type()
)
sleDoorStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleDoorStatus.setStatus("current")
_SleCpu_ObjectIdentity = ObjectIdentity
sleCpu = _SleCpu_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 9)
)
_SleCpuInfo_ObjectIdentity = ObjectIdentity
sleCpuInfo = _SleCpuInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 9, 1)
)
_SleCpuProcessor_Type = OctetString
_SleCpuProcessor_Object = MibScalar
sleCpuProcessor = _SleCpuProcessor_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 9, 1, 1),
    _SleCpuProcessor_Type()
)
sleCpuProcessor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleCpuProcessor.setStatus("current")
_SleCpuModel_Type = OctetString
_SleCpuModel_Object = MibScalar
sleCpuModel = _SleCpuModel_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 9, 1, 2),
    _SleCpuModel_Type()
)
sleCpuModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleCpuModel.setStatus("current")
_SleCpuRevision_Type = OctetString
_SleCpuRevision_Object = MibScalar
sleCpuRevision = _SleCpuRevision_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 9, 1, 3),
    _SleCpuRevision_Type()
)
sleCpuRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleCpuRevision.setStatus("current")
_SleCpuBogomips_Type = OctetString
_SleCpuBogomips_Object = MibScalar
sleCpuBogomips = _SleCpuBogomips_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 9, 1, 4),
    _SleCpuBogomips_Type()
)
sleCpuBogomips.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleCpuBogomips.setStatus("current")
_SleCpuManufacturer_Type = OctetString
_SleCpuManufacturer_Object = MibScalar
sleCpuManufacturer = _SleCpuManufacturer_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 9, 1, 5),
    _SleCpuManufacturer_Type()
)
sleCpuManufacturer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleCpuManufacturer.setStatus("current")
_SleCpuClock_Type = Integer32
_SleCpuClock_Object = MibScalar
sleCpuClock = _SleCpuClock_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 9, 1, 6),
    _SleCpuClock_Type()
)
sleCpuClock.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleCpuClock.setStatus("current")
_SleCpuBusClock_Type = Integer32
_SleCpuBusClock_Object = MibScalar
sleCpuBusClock = _SleCpuBusClock_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 9, 1, 7),
    _SleCpuBusClock_Type()
)
sleCpuBusClock.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleCpuBusClock.setStatus("current")
_SleClockModule_ObjectIdentity = ObjectIdentity
sleClockModule = _SleClockModule_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 10)
)
_SleClockModuleTable_Object = MibTable
sleClockModuleTable = _SleClockModuleTable_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 10, 1)
)
if mibBuilder.loadTexts:
    sleClockModuleTable.setStatus("current")
_SleClockModuleEntry_Object = MibTableRow
sleClockModuleEntry = _SleClockModuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 10, 1, 1)
)
sleClockModuleEntry.setIndexNames(
    (0, "SLE-DEVICE-MIB", "sleClockModuleIndex"),
)
if mibBuilder.loadTexts:
    sleClockModuleEntry.setStatus("current")


class _SleClockModuleIndex_Type(Integer32):
    """Custom type sleClockModuleIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_SleClockModuleIndex_Type.__name__ = "Integer32"
_SleClockModuleIndex_Object = MibTableColumn
sleClockModuleIndex = _SleClockModuleIndex_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 10, 1, 1, 1),
    _SleClockModuleIndex_Type()
)
sleClockModuleIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleClockModuleIndex.setStatus("current")


class _SleClockModuleBoardId_Type(Integer32):
    """Custom type sleClockModuleBoardId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("sfuA", 1),
          ("sfuB", 2))
    )


_SleClockModuleBoardId_Type.__name__ = "Integer32"
_SleClockModuleBoardId_Object = MibTableColumn
sleClockModuleBoardId = _SleClockModuleBoardId_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 10, 1, 1, 2),
    _SleClockModuleBoardId_Type()
)
sleClockModuleBoardId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleClockModuleBoardId.setStatus("current")


class _SleClockModuleInstallStatus_Type(Integer32):
    """Custom type sleClockModuleInstallStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("removed", 0),
          ("installed", 1))
    )


_SleClockModuleInstallStatus_Type.__name__ = "Integer32"
_SleClockModuleInstallStatus_Object = MibTableColumn
sleClockModuleInstallStatus = _SleClockModuleInstallStatus_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 10, 1, 1, 3),
    _SleClockModuleInstallStatus_Type()
)
sleClockModuleInstallStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleClockModuleInstallStatus.setStatus("current")


class _SleClockModuleInitStatus_Type(Integer32):
    """Custom type sleClockModuleInitStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("failure", 0),
          ("ok", 1))
    )


_SleClockModuleInitStatus_Type.__name__ = "Integer32"
_SleClockModuleInitStatus_Object = MibTableColumn
sleClockModuleInitStatus = _SleClockModuleInitStatus_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 10, 1, 1, 4),
    _SleClockModuleInitStatus_Type()
)
sleClockModuleInitStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleClockModuleInitStatus.setStatus("current")


class _SleClockModuleOPMode_Type(Integer32):
    """Custom type sleClockModuleOPMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              255)
        )
    )
    namedValues = NamedValues(
        *(("freerun", 1),
          ("holdover", 2),
          ("locked", 3),
          ("prelocked2", 4),
          ("prelocked", 5),
          ("lostphase", 6),
          ("unknown", 255))
    )


_SleClockModuleOPMode_Type.__name__ = "Integer32"
_SleClockModuleOPMode_Object = MibTableColumn
sleClockModuleOPMode = _SleClockModuleOPMode_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 10, 1, 1, 5),
    _SleClockModuleOPMode_Type()
)
sleClockModuleOPMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleClockModuleOPMode.setStatus("current")
_SleClockInfo_ObjectIdentity = ObjectIdentity
sleClockInfo = _SleClockInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 10, 2)
)


class _SleClockInfoInSrcType_Type(Integer32):
    """Custom type sleClockInfoInSrcType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              255)
        )
    )
    namedValues = NamedValues(
        *(("ntt", 1),
          ("ntt2", 2),
          ("e1", 3),
          ("t1", 4),
          ("unknown", 255))
    )


_SleClockInfoInSrcType_Type.__name__ = "Integer32"
_SleClockInfoInSrcType_Object = MibScalar
sleClockInfoInSrcType = _SleClockInfoInSrcType_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 10, 2, 1),
    _SleClockInfoInSrcType_Type()
)
sleClockInfoInSrcType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    sleClockInfoInSrcType.setStatus("current")


class _SleClockInfoInSrcStatus_Type(Integer32):
    """Custom type sleClockInfoInSrcStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("true", 1),
          ("false", 2))
    )


_SleClockInfoInSrcStatus_Type.__name__ = "Integer32"
_SleClockInfoInSrcStatus_Object = MibScalar
sleClockInfoInSrcStatus = _SleClockInfoInSrcStatus_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 10, 2, 2),
    _SleClockInfoInSrcStatus_Type()
)
sleClockInfoInSrcStatus.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    sleClockInfoInSrcStatus.setStatus("current")


class _SleClockInfoInSrcAISStatus_Type(Integer32):
    """Custom type sleClockInfoInSrcAISStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("true", 1),
          ("false", 2))
    )


_SleClockInfoInSrcAISStatus_Type.__name__ = "Integer32"
_SleClockInfoInSrcAISStatus_Object = MibScalar
sleClockInfoInSrcAISStatus = _SleClockInfoInSrcAISStatus_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 10, 2, 3),
    _SleClockInfoInSrcAISStatus_Type()
)
sleClockInfoInSrcAISStatus.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    sleClockInfoInSrcAISStatus.setStatus("current")


class _SleClockInfoInSrcLoSStatus_Type(Integer32):
    """Custom type sleClockInfoInSrcLoSStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("true", 1),
          ("false", 2))
    )


_SleClockInfoInSrcLoSStatus_Type.__name__ = "Integer32"
_SleClockInfoInSrcLoSStatus_Object = MibScalar
sleClockInfoInSrcLoSStatus = _SleClockInfoInSrcLoSStatus_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 10, 2, 4),
    _SleClockInfoInSrcLoSStatus_Type()
)
sleClockInfoInSrcLoSStatus.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    sleClockInfoInSrcLoSStatus.setStatus("current")


class _SleClockInfoInSrcLDSCStatus_Type(Integer32):
    """Custom type sleClockInfoInSrcLDSCStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("true", 1),
          ("false", 2))
    )


_SleClockInfoInSrcLDSCStatus_Type.__name__ = "Integer32"
_SleClockInfoInSrcLDSCStatus_Object = MibScalar
sleClockInfoInSrcLDSCStatus = _SleClockInfoInSrcLDSCStatus_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 10, 2, 5),
    _SleClockInfoInSrcLDSCStatus_Type()
)
sleClockInfoInSrcLDSCStatus.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    sleClockInfoInSrcLDSCStatus.setStatus("current")


class _SleClockInfoInSrcNtrClockType_Type(Bits):
    """Custom type sleClockInfoInSrcNtrClockType based on Bits"""
    namedValues = NamedValues(
        *(("bit64Khz", 0),
          ("bit8Khz", 1),
          ("bit04Khz", 2))
    )

_SleClockInfoInSrcNtrClockType_Type.__name__ = "Bits"
_SleClockInfoInSrcNtrClockType_Object = MibScalar
sleClockInfoInSrcNtrClockType = _SleClockInfoInSrcNtrClockType_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 10, 2, 6),
    _SleClockInfoInSrcNtrClockType_Type()
)
sleClockInfoInSrcNtrClockType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    sleClockInfoInSrcNtrClockType.setStatus("current")
_SleSlot_ObjectIdentity = ObjectIdentity
sleSlot = _SleSlot_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 11)
)
_SleSlotSystemInfo_ObjectIdentity = ObjectIdentity
sleSlotSystemInfo = _SleSlotSystemInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 11, 1)
)
_SleSlotSystemInfoTable_Object = MibTable
sleSlotSystemInfoTable = _SleSlotSystemInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 11, 1, 1)
)
if mibBuilder.loadTexts:
    sleSlotSystemInfoTable.setStatus("current")
_SleSlotSystemInfoEntry_Object = MibTableRow
sleSlotSystemInfoEntry = _SleSlotSystemInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 11, 1, 1, 1)
)
sleSlotSystemInfoEntry.setIndexNames(
    (0, "SLE-DEVICE-MIB", "sleSlotSystemIndex"),
)
if mibBuilder.loadTexts:
    sleSlotSystemInfoEntry.setStatus("current")


class _SleSlotSystemIndex_Type(Integer32):
    """Custom type sleSlotSystemIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_SleSlotSystemIndex_Type.__name__ = "Integer32"
_SleSlotSystemIndex_Object = MibTableColumn
sleSlotSystemIndex = _SleSlotSystemIndex_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 11, 1, 1, 1, 1),
    _SleSlotSystemIndex_Type()
)
sleSlotSystemIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleSlotSystemIndex.setStatus("current")
_SleSlotSystemUptime_Type = TimeTicks
_SleSlotSystemUptime_Object = MibTableColumn
sleSlotSystemUptime = _SleSlotSystemUptime_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 11, 1, 1, 1, 2),
    _SleSlotSystemUptime_Type()
)
sleSlotSystemUptime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleSlotSystemUptime.setStatus("current")
_SleSlotSystemModelName_Type = OctetString
_SleSlotSystemModelName_Object = MibTableColumn
sleSlotSystemModelName = _SleSlotSystemModelName_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 11, 1, 1, 1, 3),
    _SleSlotSystemModelName_Type()
)
sleSlotSystemModelName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleSlotSystemModelName.setStatus("current")
_SleSlotSystemSerialNumber_Type = OctetString
_SleSlotSystemSerialNumber_Object = MibTableColumn
sleSlotSystemSerialNumber = _SleSlotSystemSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 11, 1, 1, 1, 4),
    _SleSlotSystemSerialNumber_Type()
)
sleSlotSystemSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleSlotSystemSerialNumber.setStatus("current")
_SleSlotSystemHWVersion_Type = OctetString
_SleSlotSystemHWVersion_Object = MibTableColumn
sleSlotSystemHWVersion = _SleSlotSystemHWVersion_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 11, 1, 1, 1, 5),
    _SleSlotSystemHWVersion_Type()
)
sleSlotSystemHWVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleSlotSystemHWVersion.setStatus("current")
_SleSlotSystemBLVersion_Type = OctetString
_SleSlotSystemBLVersion_Object = MibTableColumn
sleSlotSystemBLVersion = _SleSlotSystemBLVersion_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 11, 1, 1, 1, 6),
    _SleSlotSystemBLVersion_Type()
)
sleSlotSystemBLVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleSlotSystemBLVersion.setStatus("current")
_SleSlotSystemSWCompatibility_Type = OctetString
_SleSlotSystemSWCompatibility_Object = MibTableColumn
sleSlotSystemSWCompatibility = _SleSlotSystemSWCompatibility_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 11, 1, 1, 1, 7),
    _SleSlotSystemSWCompatibility_Type()
)
sleSlotSystemSWCompatibility.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleSlotSystemSWCompatibility.setStatus("current")
_SleSlotSystemOSVersion_Type = OctetString
_SleSlotSystemOSVersion_Object = MibTableColumn
sleSlotSystemOSVersion = _SleSlotSystemOSVersion_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 11, 1, 1, 1, 8),
    _SleSlotSystemOSVersion_Type()
)
sleSlotSystemOSVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleSlotSystemOSVersion.setStatus("current")
_SleSlotSystemMacAddress_Type = OctetString
_SleSlotSystemMacAddress_Object = MibTableColumn
sleSlotSystemMacAddress = _SleSlotSystemMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 11, 1, 1, 1, 9),
    _SleSlotSystemMacAddress_Type()
)
sleSlotSystemMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleSlotSystemMacAddress.setStatus("current")
_SleSlotSystemCPULoadAll_Type = OctetString
_SleSlotSystemCPULoadAll_Object = MibTableColumn
sleSlotSystemCPULoadAll = _SleSlotSystemCPULoadAll_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 11, 1, 1, 1, 10),
    _SleSlotSystemCPULoadAll_Type()
)
sleSlotSystemCPULoadAll.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleSlotSystemCPULoadAll.setStatus("current")
_SleSlotSystemCPULoadInterrupt_Type = OctetString
_SleSlotSystemCPULoadInterrupt_Object = MibTableColumn
sleSlotSystemCPULoadInterrupt = _SleSlotSystemCPULoadInterrupt_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 11, 1, 1, 1, 11),
    _SleSlotSystemCPULoadInterrupt_Type()
)
sleSlotSystemCPULoadInterrupt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleSlotSystemCPULoadInterrupt.setStatus("current")
_SleSlotSystemMemoryTotal_Type = Gauge32
_SleSlotSystemMemoryTotal_Object = MibTableColumn
sleSlotSystemMemoryTotal = _SleSlotSystemMemoryTotal_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 11, 1, 1, 1, 12),
    _SleSlotSystemMemoryTotal_Type()
)
sleSlotSystemMemoryTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleSlotSystemMemoryTotal.setStatus("current")
_SleSlotSystemMemoryFree_Type = Gauge32
_SleSlotSystemMemoryFree_Object = MibTableColumn
sleSlotSystemMemoryFree = _SleSlotSystemMemoryFree_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 11, 1, 1, 1, 13),
    _SleSlotSystemMemoryFree_Type()
)
sleSlotSystemMemoryFree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleSlotSystemMemoryFree.setStatus("current")
_SleSlotSystemMemoryShared_Type = Gauge32
_SleSlotSystemMemoryShared_Object = MibTableColumn
sleSlotSystemMemoryShared = _SleSlotSystemMemoryShared_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 11, 1, 1, 1, 14),
    _SleSlotSystemMemoryShared_Type()
)
sleSlotSystemMemoryShared.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleSlotSystemMemoryShared.setStatus("current")
_SleSlotSystemMemoryBuffers_Type = Gauge32
_SleSlotSystemMemoryBuffers_Object = MibTableColumn
sleSlotSystemMemoryBuffers = _SleSlotSystemMemoryBuffers_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 11, 1, 1, 1, 15),
    _SleSlotSystemMemoryBuffers_Type()
)
sleSlotSystemMemoryBuffers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleSlotSystemMemoryBuffers.setStatus("current")
_SleSlotSystemMemoryCached_Type = Gauge32
_SleSlotSystemMemoryCached_Object = MibTableColumn
sleSlotSystemMemoryCached = _SleSlotSystemMemoryCached_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 11, 1, 1, 1, 16),
    _SleSlotSystemMemoryCached_Type()
)
sleSlotSystemMemoryCached.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleSlotSystemMemoryCached.setStatus("current")
_SleSlotSystemMemorySwapTotal_Type = Gauge32
_SleSlotSystemMemorySwapTotal_Object = MibTableColumn
sleSlotSystemMemorySwapTotal = _SleSlotSystemMemorySwapTotal_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 11, 1, 1, 1, 17),
    _SleSlotSystemMemorySwapTotal_Type()
)
sleSlotSystemMemorySwapTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleSlotSystemMemorySwapTotal.setStatus("current")
_SleSlotSystemMemorySwapFree_Type = Gauge32
_SleSlotSystemMemorySwapFree_Object = MibTableColumn
sleSlotSystemMemorySwapFree = _SleSlotSystemMemorySwapFree_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 11, 1, 1, 1, 18),
    _SleSlotSystemMemorySwapFree_Type()
)
sleSlotSystemMemorySwapFree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleSlotSystemMemorySwapFree.setStatus("current")


class _SleSlotSystemBootReason_Type(Integer32):
    """Custom type sleSlotSystemBootReason based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              10,
              11,
              12,
              13,
              14,
              20,
              21,
              30,
              31,
              32,
              255)
        )
    )
    namedValues = NamedValues(
        *(("powerBoot", 1),
          ("powerBootByLocal", 2),
          ("hwResetBySW", 3),
          ("hardWdogByLocal", 4),
          ("hwRebootByMate", 5),
          ("hwRebootBySwitchover", 6),
          ("swReboot", 10),
          ("swRebootByLocal", 11),
          ("swRebootBySFU", 12),
          ("swRebootBySwitchover", 13),
          ("swRebootByPanic", 14),
          ("watchdog", 20),
          ("watchdogByLocal", 21),
          ("swWatchdog", 30),
          ("swWatchdogByCpuOver", 31),
          ("swWatchdogByMemoryLow", 32),
          ("error", 255))
    )


_SleSlotSystemBootReason_Type.__name__ = "Integer32"
_SleSlotSystemBootReason_Object = MibTableColumn
sleSlotSystemBootReason = _SleSlotSystemBootReason_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 11, 1, 1, 1, 19),
    _SleSlotSystemBootReason_Type()
)
sleSlotSystemBootReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleSlotSystemBootReason.setStatus("current")
_SleSlotSystemBootTime_Type = Gauge32
_SleSlotSystemBootTime_Object = MibTableColumn
sleSlotSystemBootTime = _SleSlotSystemBootTime_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 11, 1, 1, 1, 20),
    _SleSlotSystemBootTime_Type()
)
sleSlotSystemBootTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleSlotSystemBootTime.setStatus("current")
if mibBuilder.loadTexts:
    sleSlotSystemBootTime.setUnits("1 second")
_SleSlotSystemVoltage_Type = Gauge32
_SleSlotSystemVoltage_Object = MibTableColumn
sleSlotSystemVoltage = _SleSlotSystemVoltage_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 11, 1, 1, 1, 21),
    _SleSlotSystemVoltage_Type()
)
sleSlotSystemVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleSlotSystemVoltage.setStatus("current")
if mibBuilder.loadTexts:
    sleSlotSystemVoltage.setUnits("0.1 v")


class _SleSlotSystemPowerLevelStatus_Type(Integer32):
    """Custom type sleSlotSystemPowerLevelStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("good", 1),
          ("bad", 2))
    )


_SleSlotSystemPowerLevelStatus_Type.__name__ = "Integer32"
_SleSlotSystemPowerLevelStatus_Object = MibTableColumn
sleSlotSystemPowerLevelStatus = _SleSlotSystemPowerLevelStatus_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 11, 1, 1, 1, 22),
    _SleSlotSystemPowerLevelStatus_Type()
)
sleSlotSystemPowerLevelStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleSlotSystemPowerLevelStatus.setStatus("current")


class _SleSlotSystemInfoLEDStatus_Type(Bits):
    """Custom type sleSlotSystemInfoLEDStatus based on Bits"""
    namedValues = NamedValues(
        *(("pwr", 0),
          ("run", 1),
          ("critical", 2),
          ("major", 3),
          ("minor", 4),
          ("error", 5))
    )

_SleSlotSystemInfoLEDStatus_Type.__name__ = "Bits"
_SleSlotSystemInfoLEDStatus_Object = MibTableColumn
sleSlotSystemInfoLEDStatus = _SleSlotSystemInfoLEDStatus_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 11, 1, 1, 1, 23),
    _SleSlotSystemInfoLEDStatus_Type()
)
sleSlotSystemInfoLEDStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleSlotSystemInfoLEDStatus.setStatus("current")
_SleSlotSystemInfoPackageVersion_Type = OctetString
_SleSlotSystemInfoPackageVersion_Object = MibTableColumn
sleSlotSystemInfoPackageVersion = _SleSlotSystemInfoPackageVersion_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 11, 1, 1, 1, 24),
    _SleSlotSystemInfoPackageVersion_Type()
)
sleSlotSystemInfoPackageVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleSlotSystemInfoPackageVersion.setStatus("current")
_SleSlotSystemInfoManufacturer_Type = OctetString
_SleSlotSystemInfoManufacturer_Object = MibTableColumn
sleSlotSystemInfoManufacturer = _SleSlotSystemInfoManufacturer_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 11, 1, 1, 1, 25),
    _SleSlotSystemInfoManufacturer_Type()
)
sleSlotSystemInfoManufacturer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleSlotSystemInfoManufacturer.setStatus("current")
_SleSlotSystemInfoManufactureDate_Type = OctetString
_SleSlotSystemInfoManufactureDate_Object = MibTableColumn
sleSlotSystemInfoManufactureDate = _SleSlotSystemInfoManufactureDate_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 11, 1, 1, 1, 26),
    _SleSlotSystemInfoManufactureDate_Type()
)
sleSlotSystemInfoManufactureDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleSlotSystemInfoManufactureDate.setStatus("current")
_SleSlotSystemCPULoadHighThreshold_Type = Integer32
_SleSlotSystemCPULoadHighThreshold_Object = MibTableColumn
sleSlotSystemCPULoadHighThreshold = _SleSlotSystemCPULoadHighThreshold_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 11, 1, 1, 1, 27),
    _SleSlotSystemCPULoadHighThreshold_Type()
)
sleSlotSystemCPULoadHighThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleSlotSystemCPULoadHighThreshold.setStatus("current")


class _SleSlotSystemCPULoadHighThresholdTimer_Type(Integer32):
    """Custom type sleSlotSystemCPULoadHighThresholdTimer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("timerInverval5", 1),
          ("timerInverval60", 2),
          ("timerInverval600", 3))
    )


_SleSlotSystemCPULoadHighThresholdTimer_Type.__name__ = "Integer32"
_SleSlotSystemCPULoadHighThresholdTimer_Object = MibTableColumn
sleSlotSystemCPULoadHighThresholdTimer = _SleSlotSystemCPULoadHighThresholdTimer_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 11, 1, 1, 1, 28),
    _SleSlotSystemCPULoadHighThresholdTimer_Type()
)
sleSlotSystemCPULoadHighThresholdTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleSlotSystemCPULoadHighThresholdTimer.setStatus("current")
_SleSlotSystemCPULoadLowThreshold_Type = Integer32
_SleSlotSystemCPULoadLowThreshold_Object = MibTableColumn
sleSlotSystemCPULoadLowThreshold = _SleSlotSystemCPULoadLowThreshold_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 11, 1, 1, 1, 29),
    _SleSlotSystemCPULoadLowThreshold_Type()
)
sleSlotSystemCPULoadLowThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleSlotSystemCPULoadLowThreshold.setStatus("current")


class _SleSlotSystemCPULoadLowThresholdTimer_Type(Integer32):
    """Custom type sleSlotSystemCPULoadLowThresholdTimer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("timerInverval5", 1),
          ("timerInverval60", 2),
          ("timerInverval600", 3))
    )


_SleSlotSystemCPULoadLowThresholdTimer_Type.__name__ = "Integer32"
_SleSlotSystemCPULoadLowThresholdTimer_Object = MibTableColumn
sleSlotSystemCPULoadLowThresholdTimer = _SleSlotSystemCPULoadLowThresholdTimer_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 11, 1, 1, 1, 30),
    _SleSlotSystemCPULoadLowThresholdTimer_Type()
)
sleSlotSystemCPULoadLowThresholdTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleSlotSystemCPULoadLowThresholdTimer.setStatus("current")
_SleSlotSystemCPULoadCurrent_Type = Integer32
_SleSlotSystemCPULoadCurrent_Object = MibTableColumn
sleSlotSystemCPULoadCurrent = _SleSlotSystemCPULoadCurrent_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 11, 1, 1, 1, 31),
    _SleSlotSystemCPULoadCurrent_Type()
)
sleSlotSystemCPULoadCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleSlotSystemCPULoadCurrent.setStatus("current")


class _SleSlotSystemCPUOverallStatus_Type(Integer32):
    """Custom type sleSlotSystemCPUOverallStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("good", 1),
          ("bad", 2))
    )


_SleSlotSystemCPUOverallStatus_Type.__name__ = "Integer32"
_SleSlotSystemCPUOverallStatus_Object = MibTableColumn
sleSlotSystemCPUOverallStatus = _SleSlotSystemCPUOverallStatus_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 11, 1, 1, 1, 32),
    _SleSlotSystemCPUOverallStatus_Type()
)
sleSlotSystemCPUOverallStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleSlotSystemCPUOverallStatus.setStatus("current")


class _SleSlotSystemTemperOverallStatus_Type(Integer32):
    """Custom type sleSlotSystemTemperOverallStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("good", 1),
          ("bad", 2))
    )


_SleSlotSystemTemperOverallStatus_Type.__name__ = "Integer32"
_SleSlotSystemTemperOverallStatus_Object = MibTableColumn
sleSlotSystemTemperOverallStatus = _SleSlotSystemTemperOverallStatus_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 11, 1, 1, 1, 33),
    _SleSlotSystemTemperOverallStatus_Type()
)
sleSlotSystemTemperOverallStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleSlotSystemTemperOverallStatus.setStatus("current")
_SleSlotSystemControl_ObjectIdentity = ObjectIdentity
sleSlotSystemControl = _SleSlotSystemControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 11, 1, 2)
)


class _SleSlotSystemControlRequest_Type(Integer32):
    """Custom type sleSlotSystemControlRequest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("setSlotRestart", 1),
          ("setSlotCpuloadThreshold", 2),
          ("delSlotCpuloadThreshold", 3))
    )


_SleSlotSystemControlRequest_Type.__name__ = "Integer32"
_SleSlotSystemControlRequest_Object = MibScalar
sleSlotSystemControlRequest = _SleSlotSystemControlRequest_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 11, 1, 2, 1),
    _SleSlotSystemControlRequest_Type()
)
sleSlotSystemControlRequest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleSlotSystemControlRequest.setStatus("current")
_SleSlotSystemControlStatus_Type = SleControlStatusType
_SleSlotSystemControlStatus_Object = MibScalar
sleSlotSystemControlStatus = _SleSlotSystemControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 11, 1, 2, 2),
    _SleSlotSystemControlStatus_Type()
)
sleSlotSystemControlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleSlotSystemControlStatus.setStatus("current")
_SleSlotSystemControlTimer_Type = Gauge32
_SleSlotSystemControlTimer_Object = MibScalar
sleSlotSystemControlTimer = _SleSlotSystemControlTimer_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 11, 1, 2, 3),
    _SleSlotSystemControlTimer_Type()
)
sleSlotSystemControlTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleSlotSystemControlTimer.setStatus("current")
_SleSlotSystemControlTimeStamp_Type = TimeTicks
_SleSlotSystemControlTimeStamp_Object = MibScalar
sleSlotSystemControlTimeStamp = _SleSlotSystemControlTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 11, 1, 2, 4),
    _SleSlotSystemControlTimeStamp_Type()
)
sleSlotSystemControlTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleSlotSystemControlTimeStamp.setStatus("current")
_SleSlotSystemControlReqResult_Type = SleControlRequestResultType
_SleSlotSystemControlReqResult_Object = MibScalar
sleSlotSystemControlReqResult = _SleSlotSystemControlReqResult_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 11, 1, 2, 5),
    _SleSlotSystemControlReqResult_Type()
)
sleSlotSystemControlReqResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleSlotSystemControlReqResult.setStatus("current")
_SleSlotSystemControlSlotIndex_Type = Integer32
_SleSlotSystemControlSlotIndex_Object = MibScalar
sleSlotSystemControlSlotIndex = _SleSlotSystemControlSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 11, 1, 2, 6),
    _SleSlotSystemControlSlotIndex_Type()
)
sleSlotSystemControlSlotIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleSlotSystemControlSlotIndex.setStatus("current")


class _SleSlotSystemControlCPULoadHighThreshold_Type(Integer32):
    """Custom type sleSlotSystemControlCPULoadHighThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(21, 100),
    )


_SleSlotSystemControlCPULoadHighThreshold_Type.__name__ = "Integer32"
_SleSlotSystemControlCPULoadHighThreshold_Object = MibScalar
sleSlotSystemControlCPULoadHighThreshold = _SleSlotSystemControlCPULoadHighThreshold_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 11, 1, 2, 7),
    _SleSlotSystemControlCPULoadHighThreshold_Type()
)
sleSlotSystemControlCPULoadHighThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleSlotSystemControlCPULoadHighThreshold.setStatus("current")


class _SleSlotSystemControlCPULoadHighThresholdTimer_Type(Integer32):
    """Custom type sleSlotSystemControlCPULoadHighThresholdTimer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("timerInverval5", 1),
          ("timerInverval60", 2),
          ("timerInverval600", 3))
    )


_SleSlotSystemControlCPULoadHighThresholdTimer_Type.__name__ = "Integer32"
_SleSlotSystemControlCPULoadHighThresholdTimer_Object = MibScalar
sleSlotSystemControlCPULoadHighThresholdTimer = _SleSlotSystemControlCPULoadHighThresholdTimer_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 11, 1, 2, 8),
    _SleSlotSystemControlCPULoadHighThresholdTimer_Type()
)
sleSlotSystemControlCPULoadHighThresholdTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleSlotSystemControlCPULoadHighThresholdTimer.setStatus("current")


class _SleSlotSystemControlCPULoadLowThreshold_Type(Integer32):
    """Custom type sleSlotSystemControlCPULoadLowThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(20, 100),
    )


_SleSlotSystemControlCPULoadLowThreshold_Type.__name__ = "Integer32"
_SleSlotSystemControlCPULoadLowThreshold_Object = MibScalar
sleSlotSystemControlCPULoadLowThreshold = _SleSlotSystemControlCPULoadLowThreshold_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 11, 1, 2, 9),
    _SleSlotSystemControlCPULoadLowThreshold_Type()
)
sleSlotSystemControlCPULoadLowThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleSlotSystemControlCPULoadLowThreshold.setStatus("current")


class _SleSlotSystemControlCPULoadLowThresholdTimer_Type(Integer32):
    """Custom type sleSlotSystemControlCPULoadLowThresholdTimer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("timerInverval5", 1),
          ("timerInverval60", 2),
          ("timerInverval600", 3))
    )


_SleSlotSystemControlCPULoadLowThresholdTimer_Type.__name__ = "Integer32"
_SleSlotSystemControlCPULoadLowThresholdTimer_Object = MibScalar
sleSlotSystemControlCPULoadLowThresholdTimer = _SleSlotSystemControlCPULoadLowThresholdTimer_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 11, 1, 2, 10),
    _SleSlotSystemControlCPULoadLowThresholdTimer_Type()
)
sleSlotSystemControlCPULoadLowThresholdTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleSlotSystemControlCPULoadLowThresholdTimer.setStatus("current")
_SleSlotSystemNotification_ObjectIdentity = ObjectIdentity
sleSlotSystemNotification = _SleSlotSystemNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 11, 1, 3)
)
_SleSlotStatusInfo_ObjectIdentity = ObjectIdentity
sleSlotStatusInfo = _SleSlotStatusInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 11, 2)
)
_SleSlotStatusInfoTable_Object = MibTable
sleSlotStatusInfoTable = _SleSlotStatusInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 11, 2, 1)
)
if mibBuilder.loadTexts:
    sleSlotStatusInfoTable.setStatus("current")
_SleSlotStatusInfoEntry_Object = MibTableRow
sleSlotStatusInfoEntry = _SleSlotStatusInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 11, 2, 1, 1)
)
sleSlotStatusInfoEntry.setIndexNames(
    (0, "SLE-DEVICE-MIB", "sleSlotSystemIndex"),
)
if mibBuilder.loadTexts:
    sleSlotStatusInfoEntry.setStatus("current")


class _SleSlotStatusPlan_Type(Integer32):
    """Custom type sleSlotStatusPlan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notPlanned", 1),
          ("planned", 2))
    )


_SleSlotStatusPlan_Type.__name__ = "Integer32"
_SleSlotStatusPlan_Object = MibTableColumn
sleSlotStatusPlan = _SleSlotStatusPlan_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 11, 2, 1, 1, 1),
    _SleSlotStatusPlan_Type()
)
sleSlotStatusPlan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleSlotStatusPlan.setStatus("current")


class _SleSlotStatusPlanCardType_Type(Integer32):
    """Custom type sleSlotStatusPlanCardType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19,
              20,
              21,
              22,
              23,
              24,
              25,
              26,
              27,
              28,
              29,
              30,
              31,
              32,
              33,
              34,
              35,
              36,
              37,
              38,
              39,
              40,
              41,
              42,
              43)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 1),
          ("siuGE12", 2),
          ("siuEPON12", 3),
          ("siuGPON4", 4),
          ("niuGE12", 5),
          ("sfu", 6),
          ("v5548gGE12", 7),
          ("siuGPON4r", 8),
          ("niuGE8", 9),
          ("siuGE4", 10),
          ("niu10GPlus", 11),
          ("iu10GE", 12),
          ("iuGE6", 13),
          ("iuGE4", 14),
          ("siuTDM", 15),
          ("siuGE24", 16),
          ("siuFE48", 17),
          ("niu10GE2", 18),
          ("siu10GE48", 19),
          ("siuGE10", 20),
          ("niu10Ge2Plus", 21),
          ("iuGT4", 22),
          ("iuGT6", 23),
          ("iuTDM6", 24),
          ("siuGE6", 25),
          ("siuGE8", 26),
          ("siuGT6", 27),
          ("niuGE2", 28),
          ("niuGE4", 29),
          ("iuGEPON4", 30),
          ("iu10GE8", 31),
          ("iuGEPON8", 32),
          ("iu10GEPON8", 33),
          ("iuGE8", 34),
          ("siu10GEPON8", 35),
          ("niu10GE4", 36),
          ("sfu10GE4", 37),
          ("siuGPON16", 38),
          ("iu10GE4", 39),
          ("siuGT24", 40),
          ("iu10GE2", 41),
          ("cwdm", 42),
          ("iuGT8", 43))
    )


_SleSlotStatusPlanCardType_Type.__name__ = "Integer32"
_SleSlotStatusPlanCardType_Object = MibTableColumn
sleSlotStatusPlanCardType = _SleSlotStatusPlanCardType_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 11, 2, 1, 1, 2),
    _SleSlotStatusPlanCardType_Type()
)
sleSlotStatusPlanCardType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleSlotStatusPlanCardType.setStatus("current")


class _SleSlotStatusCurrentInstall_Type(Integer32):
    """Custom type sleSlotStatusCurrentInstall based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("notInstalled", 1),
          ("installed", 2),
          ("failed", 3))
    )


_SleSlotStatusCurrentInstall_Type.__name__ = "Integer32"
_SleSlotStatusCurrentInstall_Object = MibTableColumn
sleSlotStatusCurrentInstall = _SleSlotStatusCurrentInstall_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 11, 2, 1, 1, 3),
    _SleSlotStatusCurrentInstall_Type()
)
sleSlotStatusCurrentInstall.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleSlotStatusCurrentInstall.setStatus("current")


class _SleSlotStatusCurrentInstallCardType_Type(Integer32):
    """Custom type sleSlotStatusCurrentInstallCardType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19,
              20,
              21,
              22,
              23,
              24,
              25,
              26,
              27,
              28,
              29,
              30,
              31,
              32,
              33,
              34,
              35,
              36,
              37,
              38,
              39,
              40,
              41,
              42,
              43)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 1),
          ("siuGE12", 2),
          ("siuEPON12", 3),
          ("siuGPON4", 4),
          ("niuGE12", 5),
          ("sfu", 6),
          ("v5548gGE12", 7),
          ("siuGPON4r", 8),
          ("niuGE8", 9),
          ("siuGE4", 10),
          ("niu10GPlus", 11),
          ("iuGE10", 12),
          ("iuGE6", 13),
          ("iuGE4", 14),
          ("siuTDM", 15),
          ("siuGE24", 16),
          ("siuFE48", 17),
          ("niu10GE2", 18),
          ("siu10GE48", 19),
          ("siuGE10", 20),
          ("niu10Ge2Plus", 21),
          ("iuGT4", 22),
          ("iuGT6", 23),
          ("iuTDM6", 24),
          ("siuGE6", 25),
          ("siuGE8", 26),
          ("siuGT6", 27),
          ("niuGE2", 28),
          ("niuGE4", 29),
          ("iuGEPON4", 30),
          ("iu10GE8", 31),
          ("iuGEPON8", 32),
          ("iu10GEPON8", 33),
          ("iuGE8", 34),
          ("siu10GEPON8", 35),
          ("niu10GE4", 36),
          ("sfu10GE4", 37),
          ("siuGPON16", 38),
          ("iu10GE4", 39),
          ("siuGT24", 40),
          ("iu10GE2", 41),
          ("cwdm", 42),
          ("iuGT8", 43))
    )


_SleSlotStatusCurrentInstallCardType_Type.__name__ = "Integer32"
_SleSlotStatusCurrentInstallCardType_Object = MibTableColumn
sleSlotStatusCurrentInstallCardType = _SleSlotStatusCurrentInstallCardType_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 11, 2, 1, 1, 4),
    _SleSlotStatusCurrentInstallCardType_Type()
)
sleSlotStatusCurrentInstallCardType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleSlotStatusCurrentInstallCardType.setStatus("current")


class _SleSlotStatusCardOperation_Type(Integer32):
    """Custom type sleSlotStatusCardOperation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("init", 2),
          ("enable", 3),
          ("enableActive", 4),
          ("enableStandby", 5))
    )


_SleSlotStatusCardOperation_Type.__name__ = "Integer32"
_SleSlotStatusCardOperation_Object = MibTableColumn
sleSlotStatusCardOperation = _SleSlotStatusCardOperation_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 11, 2, 1, 1, 5),
    _SleSlotStatusCardOperation_Type()
)
sleSlotStatusCardOperation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleSlotStatusCardOperation.setStatus("current")


class _SleSlotStatusLock_Type(Integer32):
    """Custom type sleSlotStatusLock based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("unlocked", 1),
          ("locked", 2))
    )


_SleSlotStatusLock_Type.__name__ = "Integer32"
_SleSlotStatusLock_Object = MibTableColumn
sleSlotStatusLock = _SleSlotStatusLock_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 11, 2, 1, 1, 6),
    _SleSlotStatusLock_Type()
)
sleSlotStatusLock.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleSlotStatusLock.setStatus("current")


class _SleSlotStatusUpgradeMode_Type(Integer32):
    """Custom type sleSlotStatusUpgradeMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("manual", 1),
          ("auto", 2))
    )


_SleSlotStatusUpgradeMode_Type.__name__ = "Integer32"
_SleSlotStatusUpgradeMode_Object = MibTableColumn
sleSlotStatusUpgradeMode = _SleSlotStatusUpgradeMode_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 11, 2, 1, 1, 7),
    _SleSlotStatusUpgradeMode_Type()
)
sleSlotStatusUpgradeMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleSlotStatusUpgradeMode.setStatus("current")


class _SleSlotStatusActionEvent_Type(Integer32):
    """Custom type sleSlotStatusActionEvent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11)
        )
    )
    namedValues = NamedValues(
        *(("uninstallAction", 1),
          ("installAction", 2),
          ("noPlanningAction", 3),
          ("planningAction", 4),
          ("lockAction", 5),
          ("unlockAction", 6),
          ("matchedEvent", 7),
          ("unMatchedEvent", 8),
          ("bootEndEvent", 9),
          ("configEndEvent", 10),
          ("configFailEvent", 11))
    )


_SleSlotStatusActionEvent_Type.__name__ = "Integer32"
_SleSlotStatusActionEvent_Object = MibTableColumn
sleSlotStatusActionEvent = _SleSlotStatusActionEvent_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 11, 2, 1, 1, 8),
    _SleSlotStatusActionEvent_Type()
)
sleSlotStatusActionEvent.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    sleSlotStatusActionEvent.setStatus("current")


class _SleSlotStatusState_Type(Integer32):
    """Custom type sleSlotStatusState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10)
        )
    )
    namedValues = NamedValues(
        *(("default", 1),
          ("planningWait", 2),
          ("installWait", 3),
          ("operationReady", 4),
          ("actionBootReady", 5),
          ("actionConfig", 6),
          ("actionEnableReady", 7),
          ("actionEnable", 8),
          ("actionEnableLock", 9),
          ("actionDisable", 10))
    )


_SleSlotStatusState_Type.__name__ = "Integer32"
_SleSlotStatusState_Object = MibTableColumn
sleSlotStatusState = _SleSlotStatusState_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 11, 2, 1, 1, 9),
    _SleSlotStatusState_Type()
)
sleSlotStatusState.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    sleSlotStatusState.setStatus("current")


class _SleSlotStatusPower_Type(Integer32):
    """Custom type sleSlotStatusPower based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("up", 1),
          ("down", 2))
    )


_SleSlotStatusPower_Type.__name__ = "Integer32"
_SleSlotStatusPower_Object = MibTableColumn
sleSlotStatusPower = _SleSlotStatusPower_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 11, 2, 1, 1, 10),
    _SleSlotStatusPower_Type()
)
sleSlotStatusPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleSlotStatusPower.setStatus("current")
_SleSlotStatusSerialNumber_Type = OctetString
_SleSlotStatusSerialNumber_Object = MibTableColumn
sleSlotStatusSerialNumber = _SleSlotStatusSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 11, 2, 1, 1, 11),
    _SleSlotStatusSerialNumber_Type()
)
sleSlotStatusSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleSlotStatusSerialNumber.setStatus("current")


class _SleSlotStatusHealthState_Type(Integer32):
    """Custom type sleSlotStatusHealthState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("well", 0),
          ("warning", 1),
          ("timeout", 2))
    )


_SleSlotStatusHealthState_Type.__name__ = "Integer32"
_SleSlotStatusHealthState_Object = MibTableColumn
sleSlotStatusHealthState = _SleSlotStatusHealthState_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 11, 2, 1, 1, 12),
    _SleSlotStatusHealthState_Type()
)
sleSlotStatusHealthState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleSlotStatusHealthState.setStatus("current")


class _SleslotStatusOverallState_Type(Integer32):
    """Custom type sleslotStatusOverallState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("good", 0),
          ("bad", 1))
    )


_SleslotStatusOverallState_Type.__name__ = "Integer32"
_SleslotStatusOverallState_Object = MibTableColumn
sleslotStatusOverallState = _SleslotStatusOverallState_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 11, 2, 1, 1, 13),
    _SleslotStatusOverallState_Type()
)
sleslotStatusOverallState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleslotStatusOverallState.setStatus("current")


class _SleslotStatusSyncState_Type(Integer32):
    """Custom type sleslotStatusSyncState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("disable", 1),
          ("process", 2),
          ("done", 3))
    )


_SleslotStatusSyncState_Type.__name__ = "Integer32"
_SleslotStatusSyncState_Object = MibTableColumn
sleslotStatusSyncState = _SleslotStatusSyncState_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 11, 2, 1, 1, 14),
    _SleslotStatusSyncState_Type()
)
sleslotStatusSyncState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleslotStatusSyncState.setStatus("current")
_SleSlotStatusControl_ObjectIdentity = ObjectIdentity
sleSlotStatusControl = _SleSlotStatusControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 11, 2, 2)
)


class _SleSlotStatusControlRequest_Type(Integer32):
    """Custom type sleSlotStatusControlRequest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8)
        )
    )
    namedValues = NamedValues(
        *(("setSlotLock", 1),
          ("setSlotUnlock", 2),
          ("setSlotPlanning", 3),
          ("setSlotNoplanning", 4),
          ("setSlotUpgradeMode", 5),
          ("setSlotPowerUp", 6),
          ("setSlotPowerDown", 7),
          ("setSlotPowerReset", 8))
    )


_SleSlotStatusControlRequest_Type.__name__ = "Integer32"
_SleSlotStatusControlRequest_Object = MibScalar
sleSlotStatusControlRequest = _SleSlotStatusControlRequest_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 11, 2, 2, 1),
    _SleSlotStatusControlRequest_Type()
)
sleSlotStatusControlRequest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleSlotStatusControlRequest.setStatus("current")
_SleSlotStatusControlStatus_Type = SleControlStatusType
_SleSlotStatusControlStatus_Object = MibScalar
sleSlotStatusControlStatus = _SleSlotStatusControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 11, 2, 2, 2),
    _SleSlotStatusControlStatus_Type()
)
sleSlotStatusControlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleSlotStatusControlStatus.setStatus("current")
_SleSlotStatusControlTimer_Type = Gauge32
_SleSlotStatusControlTimer_Object = MibScalar
sleSlotStatusControlTimer = _SleSlotStatusControlTimer_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 11, 2, 2, 3),
    _SleSlotStatusControlTimer_Type()
)
sleSlotStatusControlTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleSlotStatusControlTimer.setStatus("current")
_SleSlotStatusControlTimeStamp_Type = TimeTicks
_SleSlotStatusControlTimeStamp_Object = MibScalar
sleSlotStatusControlTimeStamp = _SleSlotStatusControlTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 11, 2, 2, 4),
    _SleSlotStatusControlTimeStamp_Type()
)
sleSlotStatusControlTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleSlotStatusControlTimeStamp.setStatus("current")
_SleSlotStatusControlReqResult_Type = SleControlRequestResultType
_SleSlotStatusControlReqResult_Object = MibScalar
sleSlotStatusControlReqResult = _SleSlotStatusControlReqResult_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 11, 2, 2, 5),
    _SleSlotStatusControlReqResult_Type()
)
sleSlotStatusControlReqResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleSlotStatusControlReqResult.setStatus("current")
_SleSlotStatusControlSlotIndex_Type = Integer32
_SleSlotStatusControlSlotIndex_Object = MibScalar
sleSlotStatusControlSlotIndex = _SleSlotStatusControlSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 11, 2, 2, 6),
    _SleSlotStatusControlSlotIndex_Type()
)
sleSlotStatusControlSlotIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleSlotStatusControlSlotIndex.setStatus("current")


class _SleSlotStatusControlPlanCardType_Type(Integer32):
    """Custom type sleSlotStatusControlPlanCardType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19,
              20,
              21,
              22,
              23,
              24,
              25,
              26,
              27,
              28,
              29,
              30,
              31,
              32,
              33,
              34,
              35,
              36,
              37,
              38,
              39,
              40,
              41,
              42,
              43)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 1),
          ("siuGE12", 2),
          ("siuEPON12", 3),
          ("siuGPON4", 4),
          ("niuGE12", 5),
          ("sfu", 6),
          ("v5548gGE12", 7),
          ("siuGPON4r", 8),
          ("niuGE8", 9),
          ("siuGE4", 10),
          ("niu10GPlus", 11),
          ("iuGE10", 12),
          ("iuGE6", 13),
          ("iuGE4", 14),
          ("siuTDM", 15),
          ("siuGE24", 16),
          ("siuFE48", 17),
          ("niu10GE2", 18),
          ("siu10GE48", 19),
          ("siuGE10", 20),
          ("niu10Ge2Plus", 21),
          ("iuGT4", 22),
          ("iuGT6", 23),
          ("iuTDM6", 24),
          ("siuGE6", 25),
          ("siuGE8", 26),
          ("siuGT6", 27),
          ("niuGE2", 28),
          ("niuGE4", 29),
          ("iuGEPON4", 30),
          ("iu10GE8", 31),
          ("iuGEPON8", 32),
          ("iu10GEPON8", 33),
          ("iuGE8", 34),
          ("siu10GEPON8", 35),
          ("niu10GE4", 36),
          ("sfu10GE4", 37),
          ("siuGPON16", 38),
          ("iu10GE4", 39),
          ("siuGT24", 40),
          ("iu10GE2", 41),
          ("cwdm", 42),
          ("iuGT8", 43))
    )


_SleSlotStatusControlPlanCardType_Type.__name__ = "Integer32"
_SleSlotStatusControlPlanCardType_Object = MibScalar
sleSlotStatusControlPlanCardType = _SleSlotStatusControlPlanCardType_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 11, 2, 2, 7),
    _SleSlotStatusControlPlanCardType_Type()
)
sleSlotStatusControlPlanCardType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleSlotStatusControlPlanCardType.setStatus("current")


class _SleSlotStatusControlUpgradeMode_Type(Integer32):
    """Custom type sleSlotStatusControlUpgradeMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("manual", 1),
          ("auto", 2),
          ("autoUpgradeManualReset", 3))
    )


_SleSlotStatusControlUpgradeMode_Type.__name__ = "Integer32"
_SleSlotStatusControlUpgradeMode_Object = MibScalar
sleSlotStatusControlUpgradeMode = _SleSlotStatusControlUpgradeMode_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 11, 2, 2, 8),
    _SleSlotStatusControlUpgradeMode_Type()
)
sleSlotStatusControlUpgradeMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleSlotStatusControlUpgradeMode.setStatus("current")
_SleSlotStatusNotification_ObjectIdentity = ObjectIdentity
sleSlotStatusNotification = _SleSlotStatusNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 11, 2, 3)
)
_SleSlotNosInfo_ObjectIdentity = ObjectIdentity
sleSlotNosInfo = _SleSlotNosInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 11, 3)
)
_SleSlotNosInfoTable_Object = MibTable
sleSlotNosInfoTable = _SleSlotNosInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 11, 3, 1)
)
if mibBuilder.loadTexts:
    sleSlotNosInfoTable.setStatus("current")
_SleSlotNosInfoEntry_Object = MibTableRow
sleSlotNosInfoEntry = _SleSlotNosInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 11, 3, 1, 1)
)
sleSlotNosInfoEntry.setIndexNames(
    (0, "SLE-DEVICE-MIB", "sleSlotSystemIndex"),
)
if mibBuilder.loadTexts:
    sleSlotNosInfoEntry.setStatus("current")
_SleSlotNosVersion_Type = OctetString
_SleSlotNosVersion_Object = MibTableColumn
sleSlotNosVersion = _SleSlotNosVersion_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 11, 3, 1, 1, 1),
    _SleSlotNosVersion_Type()
)
sleSlotNosVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleSlotNosVersion.setStatus("current")
_SleSlotNosRevision_Type = OctetString
_SleSlotNosRevision_Object = MibTableColumn
sleSlotNosRevision = _SleSlotNosRevision_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 11, 3, 1, 1, 2),
    _SleSlotNosRevision_Type()
)
sleSlotNosRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleSlotNosRevision.setStatus("current")
_SleSlotNosSize_Type = Unsigned32
_SleSlotNosSize_Object = MibTableColumn
sleSlotNosSize = _SleSlotNosSize_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 11, 3, 1, 1, 3),
    _SleSlotNosSize_Type()
)
sleSlotNosSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleSlotNosSize.setStatus("current")


class _SleSlotNosUpgradeStatus_Type(Integer32):
    """Custom type sleSlotNosUpgradeStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("upgradeIdle", 1),
          ("upgradeStart", 2),
          ("upgradeDone", 3),
          ("upgradeFail", 4))
    )


_SleSlotNosUpgradeStatus_Type.__name__ = "Integer32"
_SleSlotNosUpgradeStatus_Object = MibTableColumn
sleSlotNosUpgradeStatus = _SleSlotNosUpgradeStatus_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 11, 3, 1, 1, 4),
    _SleSlotNosUpgradeStatus_Type()
)
sleSlotNosUpgradeStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleSlotNosUpgradeStatus.setStatus("current")
_SleSlotNosStbVersion_Type = OctetString
_SleSlotNosStbVersion_Object = MibTableColumn
sleSlotNosStbVersion = _SleSlotNosStbVersion_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 11, 3, 1, 1, 5),
    _SleSlotNosStbVersion_Type()
)
sleSlotNosStbVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleSlotNosStbVersion.setStatus("current")
_SleSlotNosStbRevision_Type = OctetString
_SleSlotNosStbRevision_Object = MibTableColumn
sleSlotNosStbRevision = _SleSlotNosStbRevision_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 11, 3, 1, 1, 6),
    _SleSlotNosStbRevision_Type()
)
sleSlotNosStbRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleSlotNosStbRevision.setStatus("current")
_SleSlotNosStbSize_Type = Unsigned32
_SleSlotNosStbSize_Object = MibTableColumn
sleSlotNosStbSize = _SleSlotNosStbSize_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 11, 3, 1, 1, 7),
    _SleSlotNosStbSize_Type()
)
sleSlotNosStbSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleSlotNosStbSize.setStatus("current")
_SleSlotNosControl_ObjectIdentity = ObjectIdentity
sleSlotNosControl = _SleSlotNosControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 11, 3, 2)
)


class _SleSlotNosControlRequest_Type(Integer32):
    """Custom type sleSlotNosControlRequest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("setSlotUpgarde", 1),
          ("downloadSlotNos", 2),
          ("upgradeSlotBootloader", 3))
    )


_SleSlotNosControlRequest_Type.__name__ = "Integer32"
_SleSlotNosControlRequest_Object = MibScalar
sleSlotNosControlRequest = _SleSlotNosControlRequest_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 11, 3, 2, 1),
    _SleSlotNosControlRequest_Type()
)
sleSlotNosControlRequest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleSlotNosControlRequest.setStatus("current")
_SleSlotNosControlStatus_Type = SleControlStatusType
_SleSlotNosControlStatus_Object = MibScalar
sleSlotNosControlStatus = _SleSlotNosControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 11, 3, 2, 2),
    _SleSlotNosControlStatus_Type()
)
sleSlotNosControlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleSlotNosControlStatus.setStatus("current")
_SleSlotNosControlTimer_Type = Gauge32
_SleSlotNosControlTimer_Object = MibScalar
sleSlotNosControlTimer = _SleSlotNosControlTimer_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 11, 3, 2, 3),
    _SleSlotNosControlTimer_Type()
)
sleSlotNosControlTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleSlotNosControlTimer.setStatus("current")
_SleSlotNosControlTimeStamp_Type = TimeTicks
_SleSlotNosControlTimeStamp_Object = MibScalar
sleSlotNosControlTimeStamp = _SleSlotNosControlTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 11, 3, 2, 4),
    _SleSlotNosControlTimeStamp_Type()
)
sleSlotNosControlTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleSlotNosControlTimeStamp.setStatus("current")
_SleSlotNosControlReqResult_Type = SleControlRequestResultType
_SleSlotNosControlReqResult_Object = MibScalar
sleSlotNosControlReqResult = _SleSlotNosControlReqResult_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 11, 3, 2, 5),
    _SleSlotNosControlReqResult_Type()
)
sleSlotNosControlReqResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleSlotNosControlReqResult.setStatus("current")
_SleSlotNosControlSlotIndex_Type = Integer32
_SleSlotNosControlSlotIndex_Object = MibScalar
sleSlotNosControlSlotIndex = _SleSlotNosControlSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 11, 3, 2, 6),
    _SleSlotNosControlSlotIndex_Type()
)
sleSlotNosControlSlotIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleSlotNosControlSlotIndex.setStatus("current")


class _SleSlotNosControlUpDownMethod_Type(Integer32):
    """Custom type sleSlotNosControlUpDownMethod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ftp", 1),
          ("tftp", 2))
    )


_SleSlotNosControlUpDownMethod_Type.__name__ = "Integer32"
_SleSlotNosControlUpDownMethod_Object = MibScalar
sleSlotNosControlUpDownMethod = _SleSlotNosControlUpDownMethod_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 11, 3, 2, 7),
    _SleSlotNosControlUpDownMethod_Type()
)
sleSlotNosControlUpDownMethod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleSlotNosControlUpDownMethod.setStatus("current")


class _SleSlotNosControlUpDownFlag_Type(Integer32):
    """Custom type sleSlotNosControlUpDownFlag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("upload", 1),
          ("download", 2))
    )


_SleSlotNosControlUpDownFlag_Type.__name__ = "Integer32"
_SleSlotNosControlUpDownFlag_Object = MibScalar
sleSlotNosControlUpDownFlag = _SleSlotNosControlUpDownFlag_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 11, 3, 2, 8),
    _SleSlotNosControlUpDownFlag_Type()
)
sleSlotNosControlUpDownFlag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleSlotNosControlUpDownFlag.setStatus("current")
_SleSlotNosControlServerAddress_Type = IpAddress
_SleSlotNosControlServerAddress_Object = MibScalar
sleSlotNosControlServerAddress = _SleSlotNosControlServerAddress_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 11, 3, 2, 9),
    _SleSlotNosControlServerAddress_Type()
)
sleSlotNosControlServerAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleSlotNosControlServerAddress.setStatus("current")
_SleSlotNosControlUserID_Type = OctetString
_SleSlotNosControlUserID_Object = MibScalar
sleSlotNosControlUserID = _SleSlotNosControlUserID_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 11, 3, 2, 10),
    _SleSlotNosControlUserID_Type()
)
sleSlotNosControlUserID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleSlotNosControlUserID.setStatus("current")
_SleSlotNosControlPassword_Type = OctetString
_SleSlotNosControlPassword_Object = MibScalar
sleSlotNosControlPassword = _SleSlotNosControlPassword_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 11, 3, 2, 11),
    _SleSlotNosControlPassword_Type()
)
sleSlotNosControlPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleSlotNosControlPassword.setStatus("current")
_SleSlotNosControlFileName_Type = OctetString
_SleSlotNosControlFileName_Object = MibScalar
sleSlotNosControlFileName = _SleSlotNosControlFileName_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 11, 3, 2, 12),
    _SleSlotNosControlFileName_Type()
)
sleSlotNosControlFileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleSlotNosControlFileName.setStatus("current")
_SleSlotNosNotification_ObjectIdentity = ObjectIdentity
sleSlotNosNotification = _SleSlotNosNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 11, 3, 3)
)
_SleSlotReleasedIUNosInfo_ObjectIdentity = ObjectIdentity
sleSlotReleasedIUNosInfo = _SleSlotReleasedIUNosInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 11, 4)
)
_SleSlotReleasedNIUNosVersion_Type = OctetString
_SleSlotReleasedNIUNosVersion_Object = MibScalar
sleSlotReleasedNIUNosVersion = _SleSlotReleasedNIUNosVersion_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 11, 4, 1),
    _SleSlotReleasedNIUNosVersion_Type()
)
sleSlotReleasedNIUNosVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleSlotReleasedNIUNosVersion.setStatus("current")
_SleSlotReleasedNIUNosRevision_Type = OctetString
_SleSlotReleasedNIUNosRevision_Object = MibScalar
sleSlotReleasedNIUNosRevision = _SleSlotReleasedNIUNosRevision_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 11, 4, 2),
    _SleSlotReleasedNIUNosRevision_Type()
)
sleSlotReleasedNIUNosRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleSlotReleasedNIUNosRevision.setStatus("current")
_SleSlotReleasedNIUNosSize_Type = Unsigned32
_SleSlotReleasedNIUNosSize_Object = MibScalar
sleSlotReleasedNIUNosSize = _SleSlotReleasedNIUNosSize_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 11, 4, 3),
    _SleSlotReleasedNIUNosSize_Type()
)
sleSlotReleasedNIUNosSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleSlotReleasedNIUNosSize.setStatus("current")
_SleSlotReleasedGPIUNosVersion_Type = OctetString
_SleSlotReleasedGPIUNosVersion_Object = MibScalar
sleSlotReleasedGPIUNosVersion = _SleSlotReleasedGPIUNosVersion_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 11, 4, 4),
    _SleSlotReleasedGPIUNosVersion_Type()
)
sleSlotReleasedGPIUNosVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleSlotReleasedGPIUNosVersion.setStatus("current")
_SleSlotReleasedGPIUNosRevision_Type = OctetString
_SleSlotReleasedGPIUNosRevision_Object = MibScalar
sleSlotReleasedGPIUNosRevision = _SleSlotReleasedGPIUNosRevision_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 11, 4, 5),
    _SleSlotReleasedGPIUNosRevision_Type()
)
sleSlotReleasedGPIUNosRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleSlotReleasedGPIUNosRevision.setStatus("current")
_SleSlotReleasedGPIUNosSize_Type = Unsigned32
_SleSlotReleasedGPIUNosSize_Object = MibScalar
sleSlotReleasedGPIUNosSize = _SleSlotReleasedGPIUNosSize_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 11, 4, 6),
    _SleSlotReleasedGPIUNosSize_Type()
)
sleSlotReleasedGPIUNosSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleSlotReleasedGPIUNosSize.setStatus("current")
_SleSlotReleasedSIUNosVersion_Type = OctetString
_SleSlotReleasedSIUNosVersion_Object = MibScalar
sleSlotReleasedSIUNosVersion = _SleSlotReleasedSIUNosVersion_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 11, 4, 7),
    _SleSlotReleasedSIUNosVersion_Type()
)
sleSlotReleasedSIUNosVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleSlotReleasedSIUNosVersion.setStatus("current")
_SleSlotReleasedSIUNosRevision_Type = OctetString
_SleSlotReleasedSIUNosRevision_Object = MibScalar
sleSlotReleasedSIUNosRevision = _SleSlotReleasedSIUNosRevision_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 11, 4, 8),
    _SleSlotReleasedSIUNosRevision_Type()
)
sleSlotReleasedSIUNosRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleSlotReleasedSIUNosRevision.setStatus("current")
_SleSlotReleasedSIUNosSize_Type = Integer32
_SleSlotReleasedSIUNosSize_Object = MibScalar
sleSlotReleasedSIUNosSize = _SleSlotReleasedSIUNosSize_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 11, 4, 9),
    _SleSlotReleasedSIUNosSize_Type()
)
sleSlotReleasedSIUNosSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleSlotReleasedSIUNosSize.setStatus("current")
_SleSlotReleasedIU10GE8NosVersion_Type = OctetString
_SleSlotReleasedIU10GE8NosVersion_Object = MibScalar
sleSlotReleasedIU10GE8NosVersion = _SleSlotReleasedIU10GE8NosVersion_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 11, 4, 10),
    _SleSlotReleasedIU10GE8NosVersion_Type()
)
sleSlotReleasedIU10GE8NosVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleSlotReleasedIU10GE8NosVersion.setStatus("current")
_SleSlotReleasedIU10GE8NosRevision_Type = OctetString
_SleSlotReleasedIU10GE8NosRevision_Object = MibScalar
sleSlotReleasedIU10GE8NosRevision = _SleSlotReleasedIU10GE8NosRevision_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 11, 4, 11),
    _SleSlotReleasedIU10GE8NosRevision_Type()
)
sleSlotReleasedIU10GE8NosRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleSlotReleasedIU10GE8NosRevision.setStatus("current")
_SleSlotReleasedIU10GE8NosSize_Type = Integer32
_SleSlotReleasedIU10GE8NosSize_Object = MibScalar
sleSlotReleasedIU10GE8NosSize = _SleSlotReleasedIU10GE8NosSize_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 11, 4, 12),
    _SleSlotReleasedIU10GE8NosSize_Type()
)
sleSlotReleasedIU10GE8NosSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleSlotReleasedIU10GE8NosSize.setStatus("current")
_SleSlotReleasedIU10GEPON8NosVersion_Type = OctetString
_SleSlotReleasedIU10GEPON8NosVersion_Object = MibScalar
sleSlotReleasedIU10GEPON8NosVersion = _SleSlotReleasedIU10GEPON8NosVersion_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 11, 4, 13),
    _SleSlotReleasedIU10GEPON8NosVersion_Type()
)
sleSlotReleasedIU10GEPON8NosVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleSlotReleasedIU10GEPON8NosVersion.setStatus("current")
_SleSlotReleasedIU10GEPON8NosRevision_Type = OctetString
_SleSlotReleasedIU10GEPON8NosRevision_Object = MibScalar
sleSlotReleasedIU10GEPON8NosRevision = _SleSlotReleasedIU10GEPON8NosRevision_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 11, 4, 14),
    _SleSlotReleasedIU10GEPON8NosRevision_Type()
)
sleSlotReleasedIU10GEPON8NosRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleSlotReleasedIU10GEPON8NosRevision.setStatus("current")
_SleSlotReleasedIU10GEPON8NosSize_Type = Integer32
_SleSlotReleasedIU10GEPON8NosSize_Object = MibScalar
sleSlotReleasedIU10GEPON8NosSize = _SleSlotReleasedIU10GEPON8NosSize_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 11, 4, 15),
    _SleSlotReleasedIU10GEPON8NosSize_Type()
)
sleSlotReleasedIU10GEPON8NosSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleSlotReleasedIU10GEPON8NosSize.setStatus("current")
_SleSlotReleasedIUGEPON8NosVersion_Type = OctetString
_SleSlotReleasedIUGEPON8NosVersion_Object = MibScalar
sleSlotReleasedIUGEPON8NosVersion = _SleSlotReleasedIUGEPON8NosVersion_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 11, 4, 16),
    _SleSlotReleasedIUGEPON8NosVersion_Type()
)
sleSlotReleasedIUGEPON8NosVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleSlotReleasedIUGEPON8NosVersion.setStatus("current")
_SleSlotReleasedIUGEPON8NosRevision_Type = OctetString
_SleSlotReleasedIUGEPON8NosRevision_Object = MibScalar
sleSlotReleasedIUGEPON8NosRevision = _SleSlotReleasedIUGEPON8NosRevision_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 11, 4, 17),
    _SleSlotReleasedIUGEPON8NosRevision_Type()
)
sleSlotReleasedIUGEPON8NosRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleSlotReleasedIUGEPON8NosRevision.setStatus("current")
_SleSlotReleasedIUGEPON8NosSize_Type = Integer32
_SleSlotReleasedIUGEPON8NosSize_Object = MibScalar
sleSlotReleasedIUGEPON8NosSize = _SleSlotReleasedIUGEPON8NosSize_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 11, 4, 18),
    _SleSlotReleasedIUGEPON8NosSize_Type()
)
sleSlotReleasedIUGEPON8NosSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleSlotReleasedIUGEPON8NosSize.setStatus("current")
_SleSlotPowerMon_ObjectIdentity = ObjectIdentity
sleSlotPowerMon = _SleSlotPowerMon_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 11, 5)
)
_SleSlotPowerMonTable_Object = MibTable
sleSlotPowerMonTable = _SleSlotPowerMonTable_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 11, 5, 1)
)
if mibBuilder.loadTexts:
    sleSlotPowerMonTable.setStatus("current")
_SleSlotPowerMonEntry_Object = MibTableRow
sleSlotPowerMonEntry = _SleSlotPowerMonEntry_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 11, 5, 1, 1)
)
sleSlotPowerMonEntry.setIndexNames(
    (0, "SLE-DEVICE-MIB", "sleSlotSystemIndex"),
    (0, "SLE-DEVICE-MIB", "sleSlotPowerMonIndex"),
)
if mibBuilder.loadTexts:
    sleSlotPowerMonEntry.setStatus("current")


class _SleSlotPowerMonIndex_Type(Integer32):
    """Custom type sleSlotPowerMonIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_SleSlotPowerMonIndex_Type.__name__ = "Integer32"
_SleSlotPowerMonIndex_Object = MibTableColumn
sleSlotPowerMonIndex = _SleSlotPowerMonIndex_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 11, 5, 1, 1, 1),
    _SleSlotPowerMonIndex_Type()
)
sleSlotPowerMonIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleSlotPowerMonIndex.setStatus("current")


class _SleSlotPowerMonStatus_Type(Integer32):
    """Custom type sleSlotPowerMonStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 1),
          ("good", 2),
          ("bad", 3),
          ("over", 4),
          ("under", 5),
          ("overUnder", 6))
    )


_SleSlotPowerMonStatus_Type.__name__ = "Integer32"
_SleSlotPowerMonStatus_Object = MibTableColumn
sleSlotPowerMonStatus = _SleSlotPowerMonStatus_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 11, 5, 1, 1, 2),
    _SleSlotPowerMonStatus_Type()
)
sleSlotPowerMonStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleSlotPowerMonStatus.setStatus("current")
_SleSlotPowerMonVoltage_Type = Gauge32
_SleSlotPowerMonVoltage_Object = MibTableColumn
sleSlotPowerMonVoltage = _SleSlotPowerMonVoltage_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 11, 5, 1, 1, 3),
    _SleSlotPowerMonVoltage_Type()
)
sleSlotPowerMonVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleSlotPowerMonVoltage.setStatus("current")
if mibBuilder.loadTexts:
    sleSlotPowerMonVoltage.setUnits("0.1v")
_SleSlotAiu_ObjectIdentity = ObjectIdentity
sleSlotAiu = _SleSlotAiu_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 11, 6)
)


class _SleSlotAiuRunStatus_Type(Integer32):
    """Custom type sleSlotAiuRunStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_SleSlotAiuRunStatus_Type.__name__ = "Integer32"
_SleSlotAiuRunStatus_Object = MibScalar
sleSlotAiuRunStatus = _SleSlotAiuRunStatus_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 11, 6, 1),
    _SleSlotAiuRunStatus_Type()
)
sleSlotAiuRunStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleSlotAiuRunStatus.setStatus("current")


class _SleSlotAiuAlarmStatus_Type(Integer32):
    """Custom type sleSlotAiuAlarmStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_SleSlotAiuAlarmStatus_Type.__name__ = "Integer32"
_SleSlotAiuAlarmStatus_Object = MibScalar
sleSlotAiuAlarmStatus = _SleSlotAiuAlarmStatus_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 11, 6, 2),
    _SleSlotAiuAlarmStatus_Type()
)
sleSlotAiuAlarmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleSlotAiuAlarmStatus.setStatus("current")
_SleSlotProtection_ObjectIdentity = ObjectIdentity
sleSlotProtection = _SleSlotProtection_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 11, 7)
)
_SleSlotProtectionBase_ObjectIdentity = ObjectIdentity
sleSlotProtectionBase = _SleSlotProtectionBase_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 11, 7, 1)
)
_SleSlotProtectionInfo_ObjectIdentity = ObjectIdentity
sleSlotProtectionInfo = _SleSlotProtectionInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 11, 7, 1, 1)
)


class _SleSlotProtectionSystemStatus_Type(Integer32):
    """Custom type sleSlotProtectionSystemStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_SleSlotProtectionSystemStatus_Type.__name__ = "Integer32"
_SleSlotProtectionSystemStatus_Object = MibScalar
sleSlotProtectionSystemStatus = _SleSlotProtectionSystemStatus_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 11, 7, 1, 1, 1),
    _SleSlotProtectionSystemStatus_Type()
)
sleSlotProtectionSystemStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleSlotProtectionSystemStatus.setStatus("current")
_SleSlotProtectionSystemThreshold_Type = Integer32
_SleSlotProtectionSystemThreshold_Object = MibScalar
sleSlotProtectionSystemThreshold = _SleSlotProtectionSystemThreshold_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 11, 7, 1, 1, 2),
    _SleSlotProtectionSystemThreshold_Type()
)
sleSlotProtectionSystemThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleSlotProtectionSystemThreshold.setStatus("current")


class _SleSlotProtectionIUPowerStatus_Type(Integer32):
    """Custom type sleSlotProtectionIUPowerStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_SleSlotProtectionIUPowerStatus_Type.__name__ = "Integer32"
_SleSlotProtectionIUPowerStatus_Object = MibScalar
sleSlotProtectionIUPowerStatus = _SleSlotProtectionIUPowerStatus_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 11, 7, 1, 1, 3),
    _SleSlotProtectionIUPowerStatus_Type()
)
sleSlotProtectionIUPowerStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleSlotProtectionIUPowerStatus.setStatus("current")
_SleSlotProtectionControl_ObjectIdentity = ObjectIdentity
sleSlotProtectionControl = _SleSlotProtectionControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 11, 7, 1, 2)
)


class _SleSlotProtectionControlRequest_Type(Integer32):
    """Custom type sleSlotProtectionControlRequest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("setSlotProtectionSystemStatus", 1),
          ("setSlotProtectionSystemThresh", 2),
          ("setslotProtectionIUPowerStatus", 3))
    )


_SleSlotProtectionControlRequest_Type.__name__ = "Integer32"
_SleSlotProtectionControlRequest_Object = MibScalar
sleSlotProtectionControlRequest = _SleSlotProtectionControlRequest_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 11, 7, 1, 2, 1),
    _SleSlotProtectionControlRequest_Type()
)
sleSlotProtectionControlRequest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleSlotProtectionControlRequest.setStatus("current")
_SleSlotProtectionControlStatus_Type = SleControlStatusType
_SleSlotProtectionControlStatus_Object = MibScalar
sleSlotProtectionControlStatus = _SleSlotProtectionControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 11, 7, 1, 2, 2),
    _SleSlotProtectionControlStatus_Type()
)
sleSlotProtectionControlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleSlotProtectionControlStatus.setStatus("current")
_SleSlotProtectionControlTimer_Type = Gauge32
_SleSlotProtectionControlTimer_Object = MibScalar
sleSlotProtectionControlTimer = _SleSlotProtectionControlTimer_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 11, 7, 1, 2, 3),
    _SleSlotProtectionControlTimer_Type()
)
sleSlotProtectionControlTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleSlotProtectionControlTimer.setStatus("current")
_SleSlotProtectionControlTimeStamp_Type = TimeTicks
_SleSlotProtectionControlTimeStamp_Object = MibScalar
sleSlotProtectionControlTimeStamp = _SleSlotProtectionControlTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 11, 7, 1, 2, 4),
    _SleSlotProtectionControlTimeStamp_Type()
)
sleSlotProtectionControlTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleSlotProtectionControlTimeStamp.setStatus("current")
_SleSlotProtectionControlReqResult_Type = SleControlRequestResultType
_SleSlotProtectionControlReqResult_Object = MibScalar
sleSlotProtectionControlReqResult = _SleSlotProtectionControlReqResult_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 11, 7, 1, 2, 5),
    _SleSlotProtectionControlReqResult_Type()
)
sleSlotProtectionControlReqResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleSlotProtectionControlReqResult.setStatus("current")


class _SleSlotProtectionControlSystemStatus_Type(Integer32):
    """Custom type sleSlotProtectionControlSystemStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_SleSlotProtectionControlSystemStatus_Type.__name__ = "Integer32"
_SleSlotProtectionControlSystemStatus_Object = MibScalar
sleSlotProtectionControlSystemStatus = _SleSlotProtectionControlSystemStatus_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 11, 7, 1, 2, 6),
    _SleSlotProtectionControlSystemStatus_Type()
)
sleSlotProtectionControlSystemStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleSlotProtectionControlSystemStatus.setStatus("current")
_SleSlotProtectionControlSystemThreshold_Type = Integer32
_SleSlotProtectionControlSystemThreshold_Object = MibScalar
sleSlotProtectionControlSystemThreshold = _SleSlotProtectionControlSystemThreshold_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 11, 7, 1, 2, 7),
    _SleSlotProtectionControlSystemThreshold_Type()
)
sleSlotProtectionControlSystemThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleSlotProtectionControlSystemThreshold.setStatus("current")


class _SleSlotProtectionControlIUPowerStatus_Type(Integer32):
    """Custom type sleSlotProtectionControlIUPowerStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_SleSlotProtectionControlIUPowerStatus_Type.__name__ = "Integer32"
_SleSlotProtectionControlIUPowerStatus_Object = MibScalar
sleSlotProtectionControlIUPowerStatus = _SleSlotProtectionControlIUPowerStatus_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 11, 7, 1, 2, 8),
    _SleSlotProtectionControlIUPowerStatus_Type()
)
sleSlotProtectionControlIUPowerStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleSlotProtectionControlIUPowerStatus.setStatus("current")
_SleSlotProtectionNotification_ObjectIdentity = ObjectIdentity
sleSlotProtectionNotification = _SleSlotProtectionNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 11, 7, 1, 3)
)
_SleSlotProtectionIU_ObjectIdentity = ObjectIdentity
sleSlotProtectionIU = _SleSlotProtectionIU_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 11, 7, 2)
)
_SleSlotProtectionIUTable_Object = MibTable
sleSlotProtectionIUTable = _SleSlotProtectionIUTable_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 11, 7, 2, 1)
)
if mibBuilder.loadTexts:
    sleSlotProtectionIUTable.setStatus("current")
_SleSlotProtectionIUEntry_Object = MibTableRow
sleSlotProtectionIUEntry = _SleSlotProtectionIUEntry_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 11, 7, 2, 1, 1)
)
if mibBuilder.loadTexts:
    sleSlotProtectionIUEntry.setStatus("current")


class _SleSlotProtectionIUTemperHighThresh_Type(Integer32):
    """Custom type sleSlotProtectionIUTemperHighThresh based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_SleSlotProtectionIUTemperHighThresh_Type.__name__ = "Integer32"
_SleSlotProtectionIUTemperHighThresh_Object = MibTableColumn
sleSlotProtectionIUTemperHighThresh = _SleSlotProtectionIUTemperHighThresh_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 11, 7, 2, 1, 1, 1),
    _SleSlotProtectionIUTemperHighThresh_Type()
)
sleSlotProtectionIUTemperHighThresh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleSlotProtectionIUTemperHighThresh.setStatus("current")


class _SleSlotProtectionIUTemperLowThresh_Type(Integer32):
    """Custom type sleSlotProtectionIUTemperLowThresh based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_SleSlotProtectionIUTemperLowThresh_Type.__name__ = "Integer32"
_SleSlotProtectionIUTemperLowThresh_Object = MibTableColumn
sleSlotProtectionIUTemperLowThresh = _SleSlotProtectionIUTemperLowThresh_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 11, 7, 2, 1, 1, 2),
    _SleSlotProtectionIUTemperLowThresh_Type()
)
sleSlotProtectionIUTemperLowThresh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleSlotProtectionIUTemperLowThresh.setStatus("current")


class _SleSlotProtectionIUPowerThresh_Type(Integer32):
    """Custom type sleSlotProtectionIUPowerThresh based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_SleSlotProtectionIUPowerThresh_Type.__name__ = "Integer32"
_SleSlotProtectionIUPowerThresh_Object = MibTableColumn
sleSlotProtectionIUPowerThresh = _SleSlotProtectionIUPowerThresh_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 11, 7, 2, 1, 1, 3),
    _SleSlotProtectionIUPowerThresh_Type()
)
sleSlotProtectionIUPowerThresh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleSlotProtectionIUPowerThresh.setStatus("current")


class _SleSlotProtectionIUTemper_Type(Integer32):
    """Custom type sleSlotProtectionIUTemper based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_SleSlotProtectionIUTemper_Type.__name__ = "Integer32"
_SleSlotProtectionIUTemper_Object = MibTableColumn
sleSlotProtectionIUTemper = _SleSlotProtectionIUTemper_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 11, 7, 2, 1, 1, 4),
    _SleSlotProtectionIUTemper_Type()
)
sleSlotProtectionIUTemper.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleSlotProtectionIUTemper.setStatus("current")


class _SleSlotProtectionIUTemper2_Type(Integer32):
    """Custom type sleSlotProtectionIUTemper2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_SleSlotProtectionIUTemper2_Type.__name__ = "Integer32"
_SleSlotProtectionIUTemper2_Object = MibTableColumn
sleSlotProtectionIUTemper2 = _SleSlotProtectionIUTemper2_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 11, 7, 2, 1, 1, 5),
    _SleSlotProtectionIUTemper2_Type()
)
sleSlotProtectionIUTemper2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleSlotProtectionIUTemper2.setStatus("current")
_SleSlotProtectionIUControl_ObjectIdentity = ObjectIdentity
sleSlotProtectionIUControl = _SleSlotProtectionIUControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 11, 7, 2, 2)
)


class _SleSlotProtectionIUControlRequest_Type(Integer32):
    """Custom type sleSlotProtectionIUControlRequest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("setSlotTempThreshold", 1),
          ("setSlotPowerThresh", 2))
    )


_SleSlotProtectionIUControlRequest_Type.__name__ = "Integer32"
_SleSlotProtectionIUControlRequest_Object = MibScalar
sleSlotProtectionIUControlRequest = _SleSlotProtectionIUControlRequest_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 11, 7, 2, 2, 1),
    _SleSlotProtectionIUControlRequest_Type()
)
sleSlotProtectionIUControlRequest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleSlotProtectionIUControlRequest.setStatus("current")
_SleSlotProtectionIUControlStatus_Type = SleControlStatusType
_SleSlotProtectionIUControlStatus_Object = MibScalar
sleSlotProtectionIUControlStatus = _SleSlotProtectionIUControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 11, 7, 2, 2, 2),
    _SleSlotProtectionIUControlStatus_Type()
)
sleSlotProtectionIUControlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleSlotProtectionIUControlStatus.setStatus("current")
_SleSlotProtectionIUControlTimer_Type = Gauge32
_SleSlotProtectionIUControlTimer_Object = MibScalar
sleSlotProtectionIUControlTimer = _SleSlotProtectionIUControlTimer_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 11, 7, 2, 2, 3),
    _SleSlotProtectionIUControlTimer_Type()
)
sleSlotProtectionIUControlTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleSlotProtectionIUControlTimer.setStatus("current")
_SleSlotProtectionIUControlTimeStamp_Type = TimeTicks
_SleSlotProtectionIUControlTimeStamp_Object = MibScalar
sleSlotProtectionIUControlTimeStamp = _SleSlotProtectionIUControlTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 11, 7, 2, 2, 4),
    _SleSlotProtectionIUControlTimeStamp_Type()
)
sleSlotProtectionIUControlTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleSlotProtectionIUControlTimeStamp.setStatus("current")
_SleSlotProtectionIUControlReqResult_Type = SleControlRequestResultType
_SleSlotProtectionIUControlReqResult_Object = MibScalar
sleSlotProtectionIUControlReqResult = _SleSlotProtectionIUControlReqResult_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 11, 7, 2, 2, 5),
    _SleSlotProtectionIUControlReqResult_Type()
)
sleSlotProtectionIUControlReqResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleSlotProtectionIUControlReqResult.setStatus("current")
_SleSlotProtectionIUControlindex_Type = Integer32
_SleSlotProtectionIUControlindex_Object = MibScalar
sleSlotProtectionIUControlindex = _SleSlotProtectionIUControlindex_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 11, 7, 2, 2, 6),
    _SleSlotProtectionIUControlindex_Type()
)
sleSlotProtectionIUControlindex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleSlotProtectionIUControlindex.setStatus("current")
_SleSlotProtectionIUControlTemperHighThresh_Type = Integer32
_SleSlotProtectionIUControlTemperHighThresh_Object = MibScalar
sleSlotProtectionIUControlTemperHighThresh = _SleSlotProtectionIUControlTemperHighThresh_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 11, 7, 2, 2, 7),
    _SleSlotProtectionIUControlTemperHighThresh_Type()
)
sleSlotProtectionIUControlTemperHighThresh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleSlotProtectionIUControlTemperHighThresh.setStatus("current")
_SleSlotProtectionIUControlTemperLowThresh_Type = Integer32
_SleSlotProtectionIUControlTemperLowThresh_Object = MibScalar
sleSlotProtectionIUControlTemperLowThresh = _SleSlotProtectionIUControlTemperLowThresh_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 11, 7, 2, 2, 8),
    _SleSlotProtectionIUControlTemperLowThresh_Type()
)
sleSlotProtectionIUControlTemperLowThresh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleSlotProtectionIUControlTemperLowThresh.setStatus("current")
_SleSlotProtectionIUControlPowerThresh_Type = Integer32
_SleSlotProtectionIUControlPowerThresh_Object = MibScalar
sleSlotProtectionIUControlPowerThresh = _SleSlotProtectionIUControlPowerThresh_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 11, 7, 2, 2, 9),
    _SleSlotProtectionIUControlPowerThresh_Type()
)
sleSlotProtectionIUControlPowerThresh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleSlotProtectionIUControlPowerThresh.setStatus("current")
_SleSlotProtectionIUNotification_ObjectIdentity = ObjectIdentity
sleSlotProtectionIUNotification = _SleSlotProtectionIUNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 11, 7, 2, 3)
)
_SleRF_ObjectIdentity = ObjectIdentity
sleRF = _SleRF_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 12)
)
_SleRfBaseInfo_ObjectIdentity = ObjectIdentity
sleRfBaseInfo = _SleRfBaseInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 12, 1)
)


class _SleRfConnectStatus_Type(Integer32):
    """Custom type sleRfConnectStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("connect", 1),
          ("disconnect", 2))
    )


_SleRfConnectStatus_Type.__name__ = "Integer32"
_SleRfConnectStatus_Object = MibScalar
sleRfConnectStatus = _SleRfConnectStatus_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 12, 1, 1),
    _SleRfConnectStatus_Type()
)
sleRfConnectStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleRfConnectStatus.setStatus("current")


class _SleRfPowerStatus_Type(Integer32):
    """Custom type sleRfPowerStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("poweroff", 0),
          ("poweron", 1))
    )


_SleRfPowerStatus_Type.__name__ = "Integer32"
_SleRfPowerStatus_Object = MibScalar
sleRfPowerStatus = _SleRfPowerStatus_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 12, 1, 2),
    _SleRfPowerStatus_Type()
)
sleRfPowerStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleRfPowerStatus.setStatus("current")
_SleRfEthertype_Type = OctetString
_SleRfEthertype_Object = MibScalar
sleRfEthertype = _SleRfEthertype_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 12, 1, 3),
    _SleRfEthertype_Type()
)
sleRfEthertype.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleRfEthertype.setStatus("current")
_SleRfSrcAddress_Type = OctetString
_SleRfSrcAddress_Object = MibScalar
sleRfSrcAddress = _SleRfSrcAddress_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 12, 1, 4),
    _SleRfSrcAddress_Type()
)
sleRfSrcAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleRfSrcAddress.setStatus("current")
_SleRfDesAddress_Type = OctetString
_SleRfDesAddress_Object = MibScalar
sleRfDesAddress = _SleRfDesAddress_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 12, 1, 5),
    _SleRfDesAddress_Type()
)
sleRfDesAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleRfDesAddress.setStatus("current")
_SleRfBaseControl_ObjectIdentity = ObjectIdentity
sleRfBaseControl = _SleRfBaseControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 12, 2)
)


class _SleRfBaseControlRequest_Type(Integer32):
    """Custom type sleRfBaseControlRequest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("setRfEthertype", 1),
          ("resetRfEthertype", 2))
    )


_SleRfBaseControlRequest_Type.__name__ = "Integer32"
_SleRfBaseControlRequest_Object = MibScalar
sleRfBaseControlRequest = _SleRfBaseControlRequest_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 12, 2, 1),
    _SleRfBaseControlRequest_Type()
)
sleRfBaseControlRequest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleRfBaseControlRequest.setStatus("current")
_SleRfBaseControlStatus_Type = SleControlStatusType
_SleRfBaseControlStatus_Object = MibScalar
sleRfBaseControlStatus = _SleRfBaseControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 12, 2, 2),
    _SleRfBaseControlStatus_Type()
)
sleRfBaseControlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleRfBaseControlStatus.setStatus("current")
_SleRfBaseControlTimer_Type = Integer32
_SleRfBaseControlTimer_Object = MibScalar
sleRfBaseControlTimer = _SleRfBaseControlTimer_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 12, 2, 3),
    _SleRfBaseControlTimer_Type()
)
sleRfBaseControlTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleRfBaseControlTimer.setStatus("current")
_SleRfBaseControlTimeStamp_Type = TimeTicks
_SleRfBaseControlTimeStamp_Object = MibScalar
sleRfBaseControlTimeStamp = _SleRfBaseControlTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 12, 2, 4),
    _SleRfBaseControlTimeStamp_Type()
)
sleRfBaseControlTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleRfBaseControlTimeStamp.setStatus("current")
_SleRfBaseControlReqResult_Type = SleControlRequestResultType
_SleRfBaseControlReqResult_Object = MibScalar
sleRfBaseControlReqResult = _SleRfBaseControlReqResult_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 12, 2, 5),
    _SleRfBaseControlReqResult_Type()
)
sleRfBaseControlReqResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleRfBaseControlReqResult.setStatus("current")
_SleRfBaseControlRfEthertype_Type = OctetString
_SleRfBaseControlRfEthertype_Object = MibScalar
sleRfBaseControlRfEthertype = _SleRfBaseControlRfEthertype_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 12, 2, 6),
    _SleRfBaseControlRfEthertype_Type()
)
sleRfBaseControlRfEthertype.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleRfBaseControlRfEthertype.setStatus("current")
_SleRfBaseNotification_ObjectIdentity = ObjectIdentity
sleRfBaseNotification = _SleRfBaseNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 12, 3)
)
_SleRfPortTable_Object = MibTable
sleRfPortTable = _SleRfPortTable_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 12, 4)
)
if mibBuilder.loadTexts:
    sleRfPortTable.setStatus("current")
_SleRfPortEntry_Object = MibTableRow
sleRfPortEntry = _SleRfPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 12, 4, 1)
)
sleRfPortEntry.setIndexNames(
    (0, "SLE-DEVICE-MIB", "sleRfPortIndex"),
)
if mibBuilder.loadTexts:
    sleRfPortEntry.setStatus("current")


class _SleRfPortIndex_Type(Integer32):
    """Custom type sleRfPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 256),
    )


_SleRfPortIndex_Type.__name__ = "Integer32"
_SleRfPortIndex_Object = MibTableColumn
sleRfPortIndex = _SleRfPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 12, 4, 1, 1),
    _SleRfPortIndex_Type()
)
sleRfPortIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleRfPortIndex.setStatus("current")


class _SleRfPortAdminStatus_Type(Integer32):
    """Custom type sleRfPortAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2),
          ("na", 255))
    )


_SleRfPortAdminStatus_Type.__name__ = "Integer32"
_SleRfPortAdminStatus_Object = MibTableColumn
sleRfPortAdminStatus = _SleRfPortAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 12, 4, 1, 2),
    _SleRfPortAdminStatus_Type()
)
sleRfPortAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleRfPortAdminStatus.setStatus("current")


class _SleRfPortOperStatus_Type(Integer32):
    """Custom type sleRfPortOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2),
          ("na", 255))
    )


_SleRfPortOperStatus_Type.__name__ = "Integer32"
_SleRfPortOperStatus_Object = MibTableColumn
sleRfPortOperStatus = _SleRfPortOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 12, 4, 1, 3),
    _SleRfPortOperStatus_Type()
)
sleRfPortOperStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleRfPortOperStatus.setStatus("current")
_SleRFPortControl_ObjectIdentity = ObjectIdentity
sleRFPortControl = _SleRFPortControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 12, 5)
)


class _SleRfPortControlRequest_Type(Integer32):
    """Custom type sleRfPortControlRequest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("setRfPortStatus", 1)
    )


_SleRfPortControlRequest_Type.__name__ = "Integer32"
_SleRfPortControlRequest_Object = MibScalar
sleRfPortControlRequest = _SleRfPortControlRequest_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 12, 5, 1),
    _SleRfPortControlRequest_Type()
)
sleRfPortControlRequest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleRfPortControlRequest.setStatus("current")
_SleRfPortControlStatus_Type = SleControlStatusType
_SleRfPortControlStatus_Object = MibScalar
sleRfPortControlStatus = _SleRfPortControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 12, 5, 2),
    _SleRfPortControlStatus_Type()
)
sleRfPortControlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleRfPortControlStatus.setStatus("current")
_SleRfPortControlTimer_Type = Integer32
_SleRfPortControlTimer_Object = MibScalar
sleRfPortControlTimer = _SleRfPortControlTimer_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 12, 5, 3),
    _SleRfPortControlTimer_Type()
)
sleRfPortControlTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleRfPortControlTimer.setStatus("current")
_SleRfPortControlTimeStamp_Type = TimeTicks
_SleRfPortControlTimeStamp_Object = MibScalar
sleRfPortControlTimeStamp = _SleRfPortControlTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 12, 5, 4),
    _SleRfPortControlTimeStamp_Type()
)
sleRfPortControlTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleRfPortControlTimeStamp.setStatus("current")
_SleRfPortControlReqResult_Type = SleControlRequestResultType
_SleRfPortControlReqResult_Object = MibScalar
sleRfPortControlReqResult = _SleRfPortControlReqResult_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 12, 5, 5),
    _SleRfPortControlReqResult_Type()
)
sleRfPortControlReqResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleRfPortControlReqResult.setStatus("current")


class _SleRfPortControlIndex_Type(Integer32):
    """Custom type sleRfPortControlIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_SleRfPortControlIndex_Type.__name__ = "Integer32"
_SleRfPortControlIndex_Object = MibScalar
sleRfPortControlIndex = _SleRfPortControlIndex_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 12, 5, 6),
    _SleRfPortControlIndex_Type()
)
sleRfPortControlIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleRfPortControlIndex.setStatus("current")


class _SleRfPortControlAdminStatus_Type(Integer32):
    """Custom type sleRfPortControlAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_SleRfPortControlAdminStatus_Type.__name__ = "Integer32"
_SleRfPortControlAdminStatus_Object = MibScalar
sleRfPortControlAdminStatus = _SleRfPortControlAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 12, 5, 7),
    _SleRfPortControlAdminStatus_Type()
)
sleRfPortControlAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleRfPortControlAdminStatus.setStatus("current")
_SleRFPortNotification_ObjectIdentity = ObjectIdentity
sleRFPortNotification = _SleRFPortNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 12, 6)
)
_SleEnvironmentMonitor_ObjectIdentity = ObjectIdentity
sleEnvironmentMonitor = _SleEnvironmentMonitor_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 13)
)
_SleEMTable_Object = MibTable
sleEMTable = _SleEMTable_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 13, 1)
)
if mibBuilder.loadTexts:
    sleEMTable.setStatus("current")
_SleEMEntry_Object = MibTableRow
sleEMEntry = _SleEMEntry_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 13, 1, 1)
)
sleEMEntry.setIndexNames(
    (0, "SLE-DEVICE-MIB", "sleEMInputIndex"),
)
if mibBuilder.loadTexts:
    sleEMEntry.setStatus("current")


class _SleEMInputIndex_Type(Integer32):
    """Custom type sleEMInputIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_SleEMInputIndex_Type.__name__ = "Integer32"
_SleEMInputIndex_Object = MibTableColumn
sleEMInputIndex = _SleEMInputIndex_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 13, 1, 1, 1),
    _SleEMInputIndex_Type()
)
sleEMInputIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleEMInputIndex.setStatus("current")
_SleEMAlarmString_Type = OctetString
_SleEMAlarmString_Object = MibTableColumn
sleEMAlarmString = _SleEMAlarmString_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 13, 1, 1, 2),
    _SleEMAlarmString_Type()
)
sleEMAlarmString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleEMAlarmString.setStatus("current")


class _SleEMAlarmSeverity_Type(Integer32):
    """Custom type sleEMAlarmSeverity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("critical", 1),
          ("major", 2),
          ("minor", 3),
          ("warning", 4),
          ("intermediate", 5))
    )


_SleEMAlarmSeverity_Type.__name__ = "Integer32"
_SleEMAlarmSeverity_Object = MibTableColumn
sleEMAlarmSeverity = _SleEMAlarmSeverity_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 13, 1, 1, 3),
    _SleEMAlarmSeverity_Type()
)
sleEMAlarmSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleEMAlarmSeverity.setStatus("current")


class _SleEMmode_Type(Integer32):
    """Custom type sleEMmode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("normalClose", 0),
          ("normalOpen", 1))
    )


_SleEMmode_Type.__name__ = "Integer32"
_SleEMmode_Object = MibTableColumn
sleEMmode = _SleEMmode_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 13, 1, 1, 4),
    _SleEMmode_Type()
)
sleEMmode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleEMmode.setStatus("current")
_SleEMControl_ObjectIdentity = ObjectIdentity
sleEMControl = _SleEMControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 13, 2)
)


class _SleEMControlRequest_Type(Integer32):
    """Custom type sleEMControlRequest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("setEM", 1),
          ("delEM", 2))
    )


_SleEMControlRequest_Type.__name__ = "Integer32"
_SleEMControlRequest_Object = MibScalar
sleEMControlRequest = _SleEMControlRequest_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 13, 2, 1),
    _SleEMControlRequest_Type()
)
sleEMControlRequest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleEMControlRequest.setStatus("current")
_SleEMControlStatus_Type = SleControlStatusType
_SleEMControlStatus_Object = MibScalar
sleEMControlStatus = _SleEMControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 13, 2, 2),
    _SleEMControlStatus_Type()
)
sleEMControlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleEMControlStatus.setStatus("current")
_SleEMControlTimer_Type = Gauge32
_SleEMControlTimer_Object = MibScalar
sleEMControlTimer = _SleEMControlTimer_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 13, 2, 3),
    _SleEMControlTimer_Type()
)
sleEMControlTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleEMControlTimer.setStatus("current")
_SleEMControlTimeStamp_Type = TimeTicks
_SleEMControlTimeStamp_Object = MibScalar
sleEMControlTimeStamp = _SleEMControlTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 13, 2, 4),
    _SleEMControlTimeStamp_Type()
)
sleEMControlTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleEMControlTimeStamp.setStatus("current")
_SleEMControlReqResult_Type = SleControlRequestResultType
_SleEMControlReqResult_Object = MibScalar
sleEMControlReqResult = _SleEMControlReqResult_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 13, 2, 5),
    _SleEMControlReqResult_Type()
)
sleEMControlReqResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleEMControlReqResult.setStatus("current")


class _SleEMControlInputIndex_Type(Integer32):
    """Custom type sleEMControlInputIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_SleEMControlInputIndex_Type.__name__ = "Integer32"
_SleEMControlInputIndex_Object = MibScalar
sleEMControlInputIndex = _SleEMControlInputIndex_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 13, 2, 6),
    _SleEMControlInputIndex_Type()
)
sleEMControlInputIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleEMControlInputIndex.setStatus("current")
_SleEMControlAlarmString_Type = OctetString
_SleEMControlAlarmString_Object = MibScalar
sleEMControlAlarmString = _SleEMControlAlarmString_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 13, 2, 7),
    _SleEMControlAlarmString_Type()
)
sleEMControlAlarmString.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleEMControlAlarmString.setStatus("current")


class _SleEMControlAlarmSeverity_Type(Integer32):
    """Custom type sleEMControlAlarmSeverity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("critical", 1),
          ("major", 2),
          ("minor", 3),
          ("warning", 4),
          ("intermediate", 5))
    )


_SleEMControlAlarmSeverity_Type.__name__ = "Integer32"
_SleEMControlAlarmSeverity_Object = MibScalar
sleEMControlAlarmSeverity = _SleEMControlAlarmSeverity_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 13, 2, 8),
    _SleEMControlAlarmSeverity_Type()
)
sleEMControlAlarmSeverity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleEMControlAlarmSeverity.setStatus("current")


class _SleEMControlmode_Type(Integer32):
    """Custom type sleEMControlmode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("normalClose", 0),
          ("normalOpen", 1))
    )


_SleEMControlmode_Type.__name__ = "Integer32"
_SleEMControlmode_Object = MibScalar
sleEMControlmode = _SleEMControlmode_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 13, 2, 9),
    _SleEMControlmode_Type()
)
sleEMControlmode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleEMControlmode.setStatus("current")
_SleEMNotification_ObjectIdentity = ObjectIdentity
sleEMNotification = _SleEMNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 13, 3)
)
_SleBypass_ObjectIdentity = ObjectIdentity
sleBypass = _SleBypass_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 14)
)
_SleBypassBase_ObjectIdentity = ObjectIdentity
sleBypassBase = _SleBypassBase_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 14, 1)
)
_SleBypassBaseInfo_ObjectIdentity = ObjectIdentity
sleBypassBaseInfo = _SleBypassBaseInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 14, 1, 1)
)


class _SleBypassMode_Type(Integer32):
    """Custom type sleBypassMode based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("on", 1),
          ("off", 2),
          ("auto", 3))
    )


_SleBypassMode_Type.__name__ = "Integer32"
_SleBypassMode_Object = MibScalar
sleBypassMode = _SleBypassMode_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 14, 1, 1, 1),
    _SleBypassMode_Type()
)
sleBypassMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleBypassMode.setStatus("current")


class _SleBypassStatus_Type(Integer32):
    """Custom type sleBypassStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_SleBypassStatus_Type.__name__ = "Integer32"
_SleBypassStatus_Object = MibScalar
sleBypassStatus = _SleBypassStatus_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 14, 1, 1, 2),
    _SleBypassStatus_Type()
)
sleBypassStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleBypassStatus.setStatus("current")
_SleBypassBaseControl_ObjectIdentity = ObjectIdentity
sleBypassBaseControl = _SleBypassBaseControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 14, 1, 2)
)


class _SleBypassBaseControlRequest_Type(Integer32):
    """Custom type sleBypassBaseControlRequest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("setBypassMode", 1)
    )


_SleBypassBaseControlRequest_Type.__name__ = "Integer32"
_SleBypassBaseControlRequest_Object = MibScalar
sleBypassBaseControlRequest = _SleBypassBaseControlRequest_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 14, 1, 2, 1),
    _SleBypassBaseControlRequest_Type()
)
sleBypassBaseControlRequest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleBypassBaseControlRequest.setStatus("current")
_SleBypassBaseControlStatus_Type = SleControlStatusType
_SleBypassBaseControlStatus_Object = MibScalar
sleBypassBaseControlStatus = _SleBypassBaseControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 14, 1, 2, 2),
    _SleBypassBaseControlStatus_Type()
)
sleBypassBaseControlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleBypassBaseControlStatus.setStatus("current")
_SleBypassBaseControlTimer_Type = Integer32
_SleBypassBaseControlTimer_Object = MibScalar
sleBypassBaseControlTimer = _SleBypassBaseControlTimer_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 14, 1, 2, 3),
    _SleBypassBaseControlTimer_Type()
)
sleBypassBaseControlTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleBypassBaseControlTimer.setStatus("current")
_SleBypassBaseControlTimeStamp_Type = TimeTicks
_SleBypassBaseControlTimeStamp_Object = MibScalar
sleBypassBaseControlTimeStamp = _SleBypassBaseControlTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 14, 1, 2, 4),
    _SleBypassBaseControlTimeStamp_Type()
)
sleBypassBaseControlTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleBypassBaseControlTimeStamp.setStatus("current")
_SleBypassBaseControlReqResult_Type = SleControlRequestResultType
_SleBypassBaseControlReqResult_Object = MibScalar
sleBypassBaseControlReqResult = _SleBypassBaseControlReqResult_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 14, 1, 2, 5),
    _SleBypassBaseControlReqResult_Type()
)
sleBypassBaseControlReqResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleBypassBaseControlReqResult.setStatus("current")


class _SleBypassBaseControlMode_Type(Integer32):
    """Custom type sleBypassBaseControlMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("on", 1),
          ("off", 2),
          ("auto", 3))
    )


_SleBypassBaseControlMode_Type.__name__ = "Integer32"
_SleBypassBaseControlMode_Object = MibScalar
sleBypassBaseControlMode = _SleBypassBaseControlMode_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 14, 1, 2, 6),
    _SleBypassBaseControlMode_Type()
)
sleBypassBaseControlMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleBypassBaseControlMode.setStatus("current")
_SleBypassBaseNotification_ObjectIdentity = ObjectIdentity
sleBypassBaseNotification = _SleBypassBaseNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 14, 1, 3)
)
_SleBypassOption_ObjectIdentity = ObjectIdentity
sleBypassOption = _SleBypassOption_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 14, 2)
)
_SleBypassOptionConnectivityTable_Object = MibTable
sleBypassOptionConnectivityTable = _SleBypassOptionConnectivityTable_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 14, 2, 1)
)
if mibBuilder.loadTexts:
    sleBypassOptionConnectivityTable.setStatus("current")
_SleBypassOptionConnectivityEntry_Object = MibTableRow
sleBypassOptionConnectivityEntry = _SleBypassOptionConnectivityEntry_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 14, 2, 1, 1)
)
sleBypassOptionConnectivityEntry.setIndexNames(
    (0, "SLE-DEVICE-MIB", "sleBypassOptionConnectivityAddress"),
    (0, "SLE-DEVICE-MIB", "sleBypassOptionConnectivityPort"),
)
if mibBuilder.loadTexts:
    sleBypassOptionConnectivityEntry.setStatus("current")
_SleBypassOptionConnectivityAddress_Type = IpAddress
_SleBypassOptionConnectivityAddress_Object = MibTableColumn
sleBypassOptionConnectivityAddress = _SleBypassOptionConnectivityAddress_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 14, 2, 1, 1, 1),
    _SleBypassOptionConnectivityAddress_Type()
)
sleBypassOptionConnectivityAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleBypassOptionConnectivityAddress.setStatus("current")


class _SleBypassOptionConnectivityPort_Type(Integer32):
    """Custom type sleBypassOptionConnectivityPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_SleBypassOptionConnectivityPort_Type.__name__ = "Integer32"
_SleBypassOptionConnectivityPort_Object = MibTableColumn
sleBypassOptionConnectivityPort = _SleBypassOptionConnectivityPort_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 14, 2, 1, 1, 2),
    _SleBypassOptionConnectivityPort_Type()
)
sleBypassOptionConnectivityPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleBypassOptionConnectivityPort.setStatus("current")
_SleBypassOptionConnectivityControl_ObjectIdentity = ObjectIdentity
sleBypassOptionConnectivityControl = _SleBypassOptionConnectivityControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 14, 2, 2)
)


class _SleBypassOptionConnectivityControlRequest_Type(Integer32):
    """Custom type sleBypassOptionConnectivityControlRequest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("setBypassConnectivity", 1),
          ("unsetBypassConnectivity", 2))
    )


_SleBypassOptionConnectivityControlRequest_Type.__name__ = "Integer32"
_SleBypassOptionConnectivityControlRequest_Object = MibScalar
sleBypassOptionConnectivityControlRequest = _SleBypassOptionConnectivityControlRequest_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 14, 2, 2, 1),
    _SleBypassOptionConnectivityControlRequest_Type()
)
sleBypassOptionConnectivityControlRequest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleBypassOptionConnectivityControlRequest.setStatus("current")
_SleBypassOptionConnectivityControlStatus_Type = SleControlStatusType
_SleBypassOptionConnectivityControlStatus_Object = MibScalar
sleBypassOptionConnectivityControlStatus = _SleBypassOptionConnectivityControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 14, 2, 2, 2),
    _SleBypassOptionConnectivityControlStatus_Type()
)
sleBypassOptionConnectivityControlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleBypassOptionConnectivityControlStatus.setStatus("current")
_SleBypassOptionConnectivityControlTimer_Type = Integer32
_SleBypassOptionConnectivityControlTimer_Object = MibScalar
sleBypassOptionConnectivityControlTimer = _SleBypassOptionConnectivityControlTimer_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 14, 2, 2, 3),
    _SleBypassOptionConnectivityControlTimer_Type()
)
sleBypassOptionConnectivityControlTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleBypassOptionConnectivityControlTimer.setStatus("current")
_SleBypassOptionConnectivityControlTimeStamp_Type = TimeTicks
_SleBypassOptionConnectivityControlTimeStamp_Object = MibScalar
sleBypassOptionConnectivityControlTimeStamp = _SleBypassOptionConnectivityControlTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 14, 2, 2, 4),
    _SleBypassOptionConnectivityControlTimeStamp_Type()
)
sleBypassOptionConnectivityControlTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleBypassOptionConnectivityControlTimeStamp.setStatus("current")
_SleBypassOptionConnectivityControlReqResult_Type = SleControlRequestResultType
_SleBypassOptionConnectivityControlReqResult_Object = MibScalar
sleBypassOptionConnectivityControlReqResult = _SleBypassOptionConnectivityControlReqResult_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 14, 2, 2, 5),
    _SleBypassOptionConnectivityControlReqResult_Type()
)
sleBypassOptionConnectivityControlReqResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleBypassOptionConnectivityControlReqResult.setStatus("current")
_SleBypassOptionConnectivityControlAddress_Type = IpAddress
_SleBypassOptionConnectivityControlAddress_Object = MibScalar
sleBypassOptionConnectivityControlAddress = _SleBypassOptionConnectivityControlAddress_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 14, 2, 2, 6),
    _SleBypassOptionConnectivityControlAddress_Type()
)
sleBypassOptionConnectivityControlAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleBypassOptionConnectivityControlAddress.setStatus("current")
_SleBypassOptionConnectivityControlPort_Type = Integer32
_SleBypassOptionConnectivityControlPort_Object = MibScalar
sleBypassOptionConnectivityControlPort = _SleBypassOptionConnectivityControlPort_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 14, 2, 2, 7),
    _SleBypassOptionConnectivityControlPort_Type()
)
sleBypassOptionConnectivityControlPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleBypassOptionConnectivityControlPort.setStatus("current")
_SleBypassOptionConnectivityNotification_ObjectIdentity = ObjectIdentity
sleBypassOptionConnectivityNotification = _SleBypassOptionConnectivityNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 14, 2, 3)
)
_SleBypassOptionPingTable_Object = MibTable
sleBypassOptionPingTable = _SleBypassOptionPingTable_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 14, 2, 4)
)
if mibBuilder.loadTexts:
    sleBypassOptionPingTable.setStatus("current")
_SleBypassOptionPingEntry_Object = MibTableRow
sleBypassOptionPingEntry = _SleBypassOptionPingEntry_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 14, 2, 4, 1)
)
sleBypassOptionPingEntry.setIndexNames(
    (0, "SLE-DEVICE-MIB", "sleBypassOptionPingAddress"),
)
if mibBuilder.loadTexts:
    sleBypassOptionPingEntry.setStatus("current")
_SleBypassOptionPingAddress_Type = IpAddress
_SleBypassOptionPingAddress_Object = MibTableColumn
sleBypassOptionPingAddress = _SleBypassOptionPingAddress_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 14, 2, 4, 1, 1),
    _SleBypassOptionPingAddress_Type()
)
sleBypassOptionPingAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleBypassOptionPingAddress.setStatus("current")
_SleBypassOptionPingTransInterval_Type = Integer32
_SleBypassOptionPingTransInterval_Object = MibTableColumn
sleBypassOptionPingTransInterval = _SleBypassOptionPingTransInterval_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 14, 2, 4, 1, 2),
    _SleBypassOptionPingTransInterval_Type()
)
sleBypassOptionPingTransInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleBypassOptionPingTransInterval.setStatus("current")
_SleBypassOptionPingTranNumber_Type = Integer32
_SleBypassOptionPingTranNumber_Object = MibTableColumn
sleBypassOptionPingTranNumber = _SleBypassOptionPingTranNumber_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 14, 2, 4, 1, 3),
    _SleBypassOptionPingTranNumber_Type()
)
sleBypassOptionPingTranNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleBypassOptionPingTranNumber.setStatus("current")
_SleBypassOptionPingReqInterval_Type = Integer32
_SleBypassOptionPingReqInterval_Object = MibTableColumn
sleBypassOptionPingReqInterval = _SleBypassOptionPingReqInterval_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 14, 2, 4, 1, 4),
    _SleBypassOptionPingReqInterval_Type()
)
sleBypassOptionPingReqInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleBypassOptionPingReqInterval.setStatus("current")
_SleBypassOptionPingReqTimeout_Type = Integer32
_SleBypassOptionPingReqTimeout_Object = MibTableColumn
sleBypassOptionPingReqTimeout = _SleBypassOptionPingReqTimeout_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 14, 2, 4, 1, 5),
    _SleBypassOptionPingReqTimeout_Type()
)
sleBypassOptionPingReqTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleBypassOptionPingReqTimeout.setStatus("current")
_SleBypassOptionPingLossThresh_Type = Integer32
_SleBypassOptionPingLossThresh_Object = MibTableColumn
sleBypassOptionPingLossThresh = _SleBypassOptionPingLossThresh_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 14, 2, 4, 1, 6),
    _SleBypassOptionPingLossThresh_Type()
)
sleBypassOptionPingLossThresh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleBypassOptionPingLossThresh.setStatus("current")
_SleBypassOptionPingControl_ObjectIdentity = ObjectIdentity
sleBypassOptionPingControl = _SleBypassOptionPingControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 14, 2, 5)
)


class _SleBypassOptionPingControlRequest_Type(Integer32):
    """Custom type sleBypassOptionPingControlRequest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("setBypassPing", 1),
          ("unsetBypassPing", 2))
    )


_SleBypassOptionPingControlRequest_Type.__name__ = "Integer32"
_SleBypassOptionPingControlRequest_Object = MibScalar
sleBypassOptionPingControlRequest = _SleBypassOptionPingControlRequest_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 14, 2, 5, 1),
    _SleBypassOptionPingControlRequest_Type()
)
sleBypassOptionPingControlRequest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleBypassOptionPingControlRequest.setStatus("current")
_SleBypassOptionPingControlStatus_Type = SleControlStatusType
_SleBypassOptionPingControlStatus_Object = MibScalar
sleBypassOptionPingControlStatus = _SleBypassOptionPingControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 14, 2, 5, 2),
    _SleBypassOptionPingControlStatus_Type()
)
sleBypassOptionPingControlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleBypassOptionPingControlStatus.setStatus("current")
_SleBypassOptionPingControlTimer_Type = Integer32
_SleBypassOptionPingControlTimer_Object = MibScalar
sleBypassOptionPingControlTimer = _SleBypassOptionPingControlTimer_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 14, 2, 5, 3),
    _SleBypassOptionPingControlTimer_Type()
)
sleBypassOptionPingControlTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleBypassOptionPingControlTimer.setStatus("current")
_SleBypassOptionPingControlTimeStamp_Type = TimeTicks
_SleBypassOptionPingControlTimeStamp_Object = MibScalar
sleBypassOptionPingControlTimeStamp = _SleBypassOptionPingControlTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 14, 2, 5, 4),
    _SleBypassOptionPingControlTimeStamp_Type()
)
sleBypassOptionPingControlTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleBypassOptionPingControlTimeStamp.setStatus("current")
_SleBypassOptionPingControlReqResult_Type = SleControlRequestResultType
_SleBypassOptionPingControlReqResult_Object = MibScalar
sleBypassOptionPingControlReqResult = _SleBypassOptionPingControlReqResult_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 14, 2, 5, 5),
    _SleBypassOptionPingControlReqResult_Type()
)
sleBypassOptionPingControlReqResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleBypassOptionPingControlReqResult.setStatus("current")
_SleBypassOptionPingControlAddress_Type = IpAddress
_SleBypassOptionPingControlAddress_Object = MibScalar
sleBypassOptionPingControlAddress = _SleBypassOptionPingControlAddress_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 14, 2, 5, 6),
    _SleBypassOptionPingControlAddress_Type()
)
sleBypassOptionPingControlAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleBypassOptionPingControlAddress.setStatus("current")
_SleBypassOptionPingControlTransInterval_Type = Integer32
_SleBypassOptionPingControlTransInterval_Object = MibScalar
sleBypassOptionPingControlTransInterval = _SleBypassOptionPingControlTransInterval_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 14, 2, 5, 7),
    _SleBypassOptionPingControlTransInterval_Type()
)
sleBypassOptionPingControlTransInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleBypassOptionPingControlTransInterval.setStatus("current")
_SleBypassOptionPingControlTranNumber_Type = Integer32
_SleBypassOptionPingControlTranNumber_Object = MibScalar
sleBypassOptionPingControlTranNumber = _SleBypassOptionPingControlTranNumber_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 14, 2, 5, 8),
    _SleBypassOptionPingControlTranNumber_Type()
)
sleBypassOptionPingControlTranNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleBypassOptionPingControlTranNumber.setStatus("current")
_SleBypassOptionPingControlReqInterval_Type = Integer32
_SleBypassOptionPingControlReqInterval_Object = MibScalar
sleBypassOptionPingControlReqInterval = _SleBypassOptionPingControlReqInterval_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 14, 2, 5, 9),
    _SleBypassOptionPingControlReqInterval_Type()
)
sleBypassOptionPingControlReqInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleBypassOptionPingControlReqInterval.setStatus("current")
_SleBypassOptionPingControlReqTimeout_Type = Integer32
_SleBypassOptionPingControlReqTimeout_Object = MibScalar
sleBypassOptionPingControlReqTimeout = _SleBypassOptionPingControlReqTimeout_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 14, 2, 5, 10),
    _SleBypassOptionPingControlReqTimeout_Type()
)
sleBypassOptionPingControlReqTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleBypassOptionPingControlReqTimeout.setStatus("current")
_SleBypassOptionPingControlLossThresh_Type = Integer32
_SleBypassOptionPingControlLossThresh_Object = MibScalar
sleBypassOptionPingControlLossThresh = _SleBypassOptionPingControlLossThresh_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 14, 2, 5, 11),
    _SleBypassOptionPingControlLossThresh_Type()
)
sleBypassOptionPingControlLossThresh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleBypassOptionPingControlLossThresh.setStatus("current")
_SleBypassOptionPingNotification_ObjectIdentity = ObjectIdentity
sleBypassOptionPingNotification = _SleBypassOptionPingNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 14, 2, 6)
)
_SleBypassOptionLinkMonitorTable_Object = MibTable
sleBypassOptionLinkMonitorTable = _SleBypassOptionLinkMonitorTable_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 14, 2, 7)
)
if mibBuilder.loadTexts:
    sleBypassOptionLinkMonitorTable.setStatus("current")
_SleBypassOptionLinkMonitorEntry_Object = MibTableRow
sleBypassOptionLinkMonitorEntry = _SleBypassOptionLinkMonitorEntry_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 14, 2, 7, 1)
)
sleBypassOptionLinkMonitorEntry.setIndexNames(
    (0, "SLE-DEVICE-MIB", "sleBypassOptionLinkMonitorPort"),
)
if mibBuilder.loadTexts:
    sleBypassOptionLinkMonitorEntry.setStatus("current")


class _SleBypassOptionLinkMonitorPort_Type(Integer32):
    """Custom type sleBypassOptionLinkMonitorPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_SleBypassOptionLinkMonitorPort_Type.__name__ = "Integer32"
_SleBypassOptionLinkMonitorPort_Object = MibTableColumn
sleBypassOptionLinkMonitorPort = _SleBypassOptionLinkMonitorPort_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 14, 2, 7, 1, 1),
    _SleBypassOptionLinkMonitorPort_Type()
)
sleBypassOptionLinkMonitorPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleBypassOptionLinkMonitorPort.setStatus("current")


class _SleBypassOptionLinkMonitorPortStatus_Type(Integer32):
    """Custom type sleBypassOptionLinkMonitorPortStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("enable", 1)
    )


_SleBypassOptionLinkMonitorPortStatus_Type.__name__ = "Integer32"
_SleBypassOptionLinkMonitorPortStatus_Object = MibTableColumn
sleBypassOptionLinkMonitorPortStatus = _SleBypassOptionLinkMonitorPortStatus_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 14, 2, 7, 1, 2),
    _SleBypassOptionLinkMonitorPortStatus_Type()
)
sleBypassOptionLinkMonitorPortStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleBypassOptionLinkMonitorPortStatus.setStatus("current")
_SleBypassOptionLinkMonitorControl_ObjectIdentity = ObjectIdentity
sleBypassOptionLinkMonitorControl = _SleBypassOptionLinkMonitorControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 14, 2, 8)
)


class _SleBypassOptionLinkMonitorControlRequest_Type(Integer32):
    """Custom type sleBypassOptionLinkMonitorControlRequest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("setBypassLinkMonitor", 1)
    )


_SleBypassOptionLinkMonitorControlRequest_Type.__name__ = "Integer32"
_SleBypassOptionLinkMonitorControlRequest_Object = MibScalar
sleBypassOptionLinkMonitorControlRequest = _SleBypassOptionLinkMonitorControlRequest_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 14, 2, 8, 1),
    _SleBypassOptionLinkMonitorControlRequest_Type()
)
sleBypassOptionLinkMonitorControlRequest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleBypassOptionLinkMonitorControlRequest.setStatus("current")
_SleBypassOptionLinkMonitorControlStatus_Type = SleControlStatusType
_SleBypassOptionLinkMonitorControlStatus_Object = MibScalar
sleBypassOptionLinkMonitorControlStatus = _SleBypassOptionLinkMonitorControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 14, 2, 8, 2),
    _SleBypassOptionLinkMonitorControlStatus_Type()
)
sleBypassOptionLinkMonitorControlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleBypassOptionLinkMonitorControlStatus.setStatus("current")
_SleBypassOptionLinkMonitorControlTimer_Type = Integer32
_SleBypassOptionLinkMonitorControlTimer_Object = MibScalar
sleBypassOptionLinkMonitorControlTimer = _SleBypassOptionLinkMonitorControlTimer_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 14, 2, 8, 3),
    _SleBypassOptionLinkMonitorControlTimer_Type()
)
sleBypassOptionLinkMonitorControlTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleBypassOptionLinkMonitorControlTimer.setStatus("current")
_SleBypassOptionLinkMonitorControlTimeStamp_Type = TimeTicks
_SleBypassOptionLinkMonitorControlTimeStamp_Object = MibScalar
sleBypassOptionLinkMonitorControlTimeStamp = _SleBypassOptionLinkMonitorControlTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 14, 2, 8, 4),
    _SleBypassOptionLinkMonitorControlTimeStamp_Type()
)
sleBypassOptionLinkMonitorControlTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleBypassOptionLinkMonitorControlTimeStamp.setStatus("current")
_SleBypassOptionLinkMonitorControlReqResult_Type = SleControlRequestResultType
_SleBypassOptionLinkMonitorControlReqResult_Object = MibScalar
sleBypassOptionLinkMonitorControlReqResult = _SleBypassOptionLinkMonitorControlReqResult_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 14, 2, 8, 5),
    _SleBypassOptionLinkMonitorControlReqResult_Type()
)
sleBypassOptionLinkMonitorControlReqResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleBypassOptionLinkMonitorControlReqResult.setStatus("current")
_SleBypassOptionLinkMonitorControlPort_Type = Integer32
_SleBypassOptionLinkMonitorControlPort_Object = MibScalar
sleBypassOptionLinkMonitorControlPort = _SleBypassOptionLinkMonitorControlPort_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 14, 2, 8, 6),
    _SleBypassOptionLinkMonitorControlPort_Type()
)
sleBypassOptionLinkMonitorControlPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleBypassOptionLinkMonitorControlPort.setStatus("current")


class _SleBypassOptionLinkMonitorControlPortStatus_Type(Integer32):
    """Custom type sleBypassOptionLinkMonitorControlPortStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_SleBypassOptionLinkMonitorControlPortStatus_Type.__name__ = "Integer32"
_SleBypassOptionLinkMonitorControlPortStatus_Object = MibScalar
sleBypassOptionLinkMonitorControlPortStatus = _SleBypassOptionLinkMonitorControlPortStatus_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 14, 2, 8, 7),
    _SleBypassOptionLinkMonitorControlPortStatus_Type()
)
sleBypassOptionLinkMonitorControlPortStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleBypassOptionLinkMonitorControlPortStatus.setStatus("current")
_SleBypassOptioLinkMonitorNotification_ObjectIdentity = ObjectIdentity
sleBypassOptioLinkMonitorNotification = _SleBypassOptioLinkMonitorNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 14, 2, 9)
)
_SleHFC_ObjectIdentity = ObjectIdentity
sleHFC = _SleHFC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 15)
)
_SleHFCTable_Object = MibTable
sleHFCTable = _SleHFCTable_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 15, 1)
)
if mibBuilder.loadTexts:
    sleHFCTable.setStatus("current")
_SleHFCEntry_Object = MibTableRow
sleHFCEntry = _SleHFCEntry_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 15, 1, 1)
)
sleHFCEntry.setIndexNames(
    (0, "SLE-DEVICE-MIB", "sleHFCOptic1550OTX"),
)
if mibBuilder.loadTexts:
    sleHFCEntry.setStatus("current")
_SleHFCOptic1550OTX_Type = OctetString
_SleHFCOptic1550OTX_Object = MibTableColumn
sleHFCOptic1550OTX = _SleHFCOptic1550OTX_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 15, 1, 1, 1),
    _SleHFCOptic1550OTX_Type()
)
sleHFCOptic1550OTX.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleHFCOptic1550OTX.setStatus("current")


class _SleHFCOptic1550OTXAlarm_Type(Integer32):
    """Custom type sleHFCOptic1550OTXAlarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_SleHFCOptic1550OTXAlarm_Type.__name__ = "Integer32"
_SleHFCOptic1550OTXAlarm_Object = MibTableColumn
sleHFCOptic1550OTXAlarm = _SleHFCOptic1550OTXAlarm_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 15, 1, 1, 2),
    _SleHFCOptic1550OTXAlarm_Type()
)
sleHFCOptic1550OTXAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleHFCOptic1550OTXAlarm.setStatus("current")
_SleHFCOpticUpstreamOTX_Type = OctetString
_SleHFCOpticUpstreamOTX_Object = MibTableColumn
sleHFCOpticUpstreamOTX = _SleHFCOpticUpstreamOTX_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 15, 1, 1, 3),
    _SleHFCOpticUpstreamOTX_Type()
)
sleHFCOpticUpstreamOTX.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleHFCOpticUpstreamOTX.setStatus("current")


class _SleHFCOpticUpstreamOTXAlarm_Type(Integer32):
    """Custom type sleHFCOpticUpstreamOTXAlarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_SleHFCOpticUpstreamOTXAlarm_Type.__name__ = "Integer32"
_SleHFCOpticUpstreamOTXAlarm_Object = MibTableColumn
sleHFCOpticUpstreamOTXAlarm = _SleHFCOpticUpstreamOTXAlarm_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 15, 1, 1, 4),
    _SleHFCOpticUpstreamOTXAlarm_Type()
)
sleHFCOpticUpstreamOTXAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleHFCOpticUpstreamOTXAlarm.setStatus("current")
_SleHFCOpticDownstreamORX_Type = OctetString
_SleHFCOpticDownstreamORX_Object = MibTableColumn
sleHFCOpticDownstreamORX = _SleHFCOpticDownstreamORX_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 15, 1, 1, 5),
    _SleHFCOpticDownstreamORX_Type()
)
sleHFCOpticDownstreamORX.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleHFCOpticDownstreamORX.setStatus("current")


class _SleHFCOpticDownstreamORXAlarm_Type(Integer32):
    """Custom type sleHFCOpticDownstreamORXAlarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_SleHFCOpticDownstreamORXAlarm_Type.__name__ = "Integer32"
_SleHFCOpticDownstreamORXAlarm_Object = MibTableColumn
sleHFCOpticDownstreamORXAlarm = _SleHFCOpticDownstreamORXAlarm_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 15, 1, 1, 6),
    _SleHFCOpticDownstreamORXAlarm_Type()
)
sleHFCOpticDownstreamORXAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleHFCOpticDownstreamORXAlarm.setStatus("current")
_SleHFCEDFA1OTX_Type = OctetString
_SleHFCEDFA1OTX_Object = MibTableColumn
sleHFCEDFA1OTX = _SleHFCEDFA1OTX_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 15, 1, 1, 7),
    _SleHFCEDFA1OTX_Type()
)
sleHFCEDFA1OTX.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleHFCEDFA1OTX.setStatus("current")


class _SleHFCEDFA1OTXAlarm_Type(Integer32):
    """Custom type sleHFCEDFA1OTXAlarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_SleHFCEDFA1OTXAlarm_Type.__name__ = "Integer32"
_SleHFCEDFA1OTXAlarm_Object = MibTableColumn
sleHFCEDFA1OTXAlarm = _SleHFCEDFA1OTXAlarm_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 15, 1, 1, 8),
    _SleHFCEDFA1OTXAlarm_Type()
)
sleHFCEDFA1OTXAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleHFCEDFA1OTXAlarm.setStatus("current")
_SleHFCEDFA1ORX_Type = OctetString
_SleHFCEDFA1ORX_Object = MibTableColumn
sleHFCEDFA1ORX = _SleHFCEDFA1ORX_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 15, 1, 1, 9),
    _SleHFCEDFA1ORX_Type()
)
sleHFCEDFA1ORX.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleHFCEDFA1ORX.setStatus("current")


class _SleHFCEDFA1ORXAlarm_Type(Integer32):
    """Custom type sleHFCEDFA1ORXAlarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_SleHFCEDFA1ORXAlarm_Type.__name__ = "Integer32"
_SleHFCEDFA1ORXAlarm_Object = MibTableColumn
sleHFCEDFA1ORXAlarm = _SleHFCEDFA1ORXAlarm_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 15, 1, 1, 10),
    _SleHFCEDFA1ORXAlarm_Type()
)
sleHFCEDFA1ORXAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleHFCEDFA1ORXAlarm.setStatus("current")
_SleHFCEDFA1LD1Current_Type = OctetString
_SleHFCEDFA1LD1Current_Object = MibTableColumn
sleHFCEDFA1LD1Current = _SleHFCEDFA1LD1Current_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 15, 1, 1, 11),
    _SleHFCEDFA1LD1Current_Type()
)
sleHFCEDFA1LD1Current.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleHFCEDFA1LD1Current.setStatus("current")


class _SleHFCEDFA1LD1CurrentAlarm_Type(Integer32):
    """Custom type sleHFCEDFA1LD1CurrentAlarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_SleHFCEDFA1LD1CurrentAlarm_Type.__name__ = "Integer32"
_SleHFCEDFA1LD1CurrentAlarm_Object = MibTableColumn
sleHFCEDFA1LD1CurrentAlarm = _SleHFCEDFA1LD1CurrentAlarm_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 15, 1, 1, 12),
    _SleHFCEDFA1LD1CurrentAlarm_Type()
)
sleHFCEDFA1LD1CurrentAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleHFCEDFA1LD1CurrentAlarm.setStatus("current")
_SleHFCEDFA1LD2Current_Type = OctetString
_SleHFCEDFA1LD2Current_Object = MibTableColumn
sleHFCEDFA1LD2Current = _SleHFCEDFA1LD2Current_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 15, 1, 1, 13),
    _SleHFCEDFA1LD2Current_Type()
)
sleHFCEDFA1LD2Current.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleHFCEDFA1LD2Current.setStatus("current")


class _SleHFCEDFA1LD2CurrentAlarm_Type(Integer32):
    """Custom type sleHFCEDFA1LD2CurrentAlarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_SleHFCEDFA1LD2CurrentAlarm_Type.__name__ = "Integer32"
_SleHFCEDFA1LD2CurrentAlarm_Object = MibTableColumn
sleHFCEDFA1LD2CurrentAlarm = _SleHFCEDFA1LD2CurrentAlarm_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 15, 1, 1, 14),
    _SleHFCEDFA1LD2CurrentAlarm_Type()
)
sleHFCEDFA1LD2CurrentAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleHFCEDFA1LD2CurrentAlarm.setStatus("current")
_SleHFCEDFA1LD1Temp_Type = OctetString
_SleHFCEDFA1LD1Temp_Object = MibTableColumn
sleHFCEDFA1LD1Temp = _SleHFCEDFA1LD1Temp_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 15, 1, 1, 15),
    _SleHFCEDFA1LD1Temp_Type()
)
sleHFCEDFA1LD1Temp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleHFCEDFA1LD1Temp.setStatus("current")


class _SleHFCEDFA1LD1TempAlarm_Type(Integer32):
    """Custom type sleHFCEDFA1LD1TempAlarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_SleHFCEDFA1LD1TempAlarm_Type.__name__ = "Integer32"
_SleHFCEDFA1LD1TempAlarm_Object = MibTableColumn
sleHFCEDFA1LD1TempAlarm = _SleHFCEDFA1LD1TempAlarm_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 15, 1, 1, 16),
    _SleHFCEDFA1LD1TempAlarm_Type()
)
sleHFCEDFA1LD1TempAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleHFCEDFA1LD1TempAlarm.setStatus("current")
_SleHFCEDFA1LD2Temp_Type = OctetString
_SleHFCEDFA1LD2Temp_Object = MibTableColumn
sleHFCEDFA1LD2Temp = _SleHFCEDFA1LD2Temp_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 15, 1, 1, 17),
    _SleHFCEDFA1LD2Temp_Type()
)
sleHFCEDFA1LD2Temp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleHFCEDFA1LD2Temp.setStatus("current")


class _SleHFCEDFA1LD2TempAlarm_Type(Integer32):
    """Custom type sleHFCEDFA1LD2TempAlarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_SleHFCEDFA1LD2TempAlarm_Type.__name__ = "Integer32"
_SleHFCEDFA1LD2TempAlarm_Object = MibTableColumn
sleHFCEDFA1LD2TempAlarm = _SleHFCEDFA1LD2TempAlarm_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 15, 1, 1, 18),
    _SleHFCEDFA1LD2TempAlarm_Type()
)
sleHFCEDFA1LD2TempAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleHFCEDFA1LD2TempAlarm.setStatus("current")
_SleHFCEDFA1CaseTemp_Type = OctetString
_SleHFCEDFA1CaseTemp_Object = MibTableColumn
sleHFCEDFA1CaseTemp = _SleHFCEDFA1CaseTemp_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 15, 1, 1, 19),
    _SleHFCEDFA1CaseTemp_Type()
)
sleHFCEDFA1CaseTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleHFCEDFA1CaseTemp.setStatus("current")


class _SleHFCEDFA1CaseTempAlarm_Type(Integer32):
    """Custom type sleHFCEDFA1CaseTempAlarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_SleHFCEDFA1CaseTempAlarm_Type.__name__ = "Integer32"
_SleHFCEDFA1CaseTempAlarm_Object = MibTableColumn
sleHFCEDFA1CaseTempAlarm = _SleHFCEDFA1CaseTempAlarm_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 15, 1, 1, 20),
    _SleHFCEDFA1CaseTempAlarm_Type()
)
sleHFCEDFA1CaseTempAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleHFCEDFA1CaseTempAlarm.setStatus("current")
_SleHFCEDFA2OTX_Type = OctetString
_SleHFCEDFA2OTX_Object = MibTableColumn
sleHFCEDFA2OTX = _SleHFCEDFA2OTX_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 15, 1, 1, 21),
    _SleHFCEDFA2OTX_Type()
)
sleHFCEDFA2OTX.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleHFCEDFA2OTX.setStatus("current")


class _SleHFCEDFA2OTXAarm_Type(Integer32):
    """Custom type sleHFCEDFA2OTXAarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_SleHFCEDFA2OTXAarm_Type.__name__ = "Integer32"
_SleHFCEDFA2OTXAarm_Object = MibTableColumn
sleHFCEDFA2OTXAarm = _SleHFCEDFA2OTXAarm_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 15, 1, 1, 22),
    _SleHFCEDFA2OTXAarm_Type()
)
sleHFCEDFA2OTXAarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleHFCEDFA2OTXAarm.setStatus("current")
_SleHFCEDFA2ORX_Type = OctetString
_SleHFCEDFA2ORX_Object = MibTableColumn
sleHFCEDFA2ORX = _SleHFCEDFA2ORX_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 15, 1, 1, 23),
    _SleHFCEDFA2ORX_Type()
)
sleHFCEDFA2ORX.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleHFCEDFA2ORX.setStatus("current")


class _SleHFCEDFA2ORXAlarm_Type(Integer32):
    """Custom type sleHFCEDFA2ORXAlarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_SleHFCEDFA2ORXAlarm_Type.__name__ = "Integer32"
_SleHFCEDFA2ORXAlarm_Object = MibTableColumn
sleHFCEDFA2ORXAlarm = _SleHFCEDFA2ORXAlarm_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 15, 1, 1, 24),
    _SleHFCEDFA2ORXAlarm_Type()
)
sleHFCEDFA2ORXAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleHFCEDFA2ORXAlarm.setStatus("current")
_SleHFCEDFA2LD1Current_Type = OctetString
_SleHFCEDFA2LD1Current_Object = MibTableColumn
sleHFCEDFA2LD1Current = _SleHFCEDFA2LD1Current_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 15, 1, 1, 25),
    _SleHFCEDFA2LD1Current_Type()
)
sleHFCEDFA2LD1Current.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleHFCEDFA2LD1Current.setStatus("current")


class _SleHFCEDFA2LD1CurrentAlarm_Type(Integer32):
    """Custom type sleHFCEDFA2LD1CurrentAlarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_SleHFCEDFA2LD1CurrentAlarm_Type.__name__ = "Integer32"
_SleHFCEDFA2LD1CurrentAlarm_Object = MibTableColumn
sleHFCEDFA2LD1CurrentAlarm = _SleHFCEDFA2LD1CurrentAlarm_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 15, 1, 1, 26),
    _SleHFCEDFA2LD1CurrentAlarm_Type()
)
sleHFCEDFA2LD1CurrentAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleHFCEDFA2LD1CurrentAlarm.setStatus("current")
_SleHFCEDFA2LD2Current_Type = OctetString
_SleHFCEDFA2LD2Current_Object = MibTableColumn
sleHFCEDFA2LD2Current = _SleHFCEDFA2LD2Current_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 15, 1, 1, 27),
    _SleHFCEDFA2LD2Current_Type()
)
sleHFCEDFA2LD2Current.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleHFCEDFA2LD2Current.setStatus("current")


class _SleHFCEDFA2LD2CurrentAlarm_Type(Integer32):
    """Custom type sleHFCEDFA2LD2CurrentAlarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_SleHFCEDFA2LD2CurrentAlarm_Type.__name__ = "Integer32"
_SleHFCEDFA2LD2CurrentAlarm_Object = MibTableColumn
sleHFCEDFA2LD2CurrentAlarm = _SleHFCEDFA2LD2CurrentAlarm_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 15, 1, 1, 28),
    _SleHFCEDFA2LD2CurrentAlarm_Type()
)
sleHFCEDFA2LD2CurrentAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleHFCEDFA2LD2CurrentAlarm.setStatus("current")
_SleHFCEDFA2LD1Temp_Type = OctetString
_SleHFCEDFA2LD1Temp_Object = MibTableColumn
sleHFCEDFA2LD1Temp = _SleHFCEDFA2LD1Temp_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 15, 1, 1, 29),
    _SleHFCEDFA2LD1Temp_Type()
)
sleHFCEDFA2LD1Temp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleHFCEDFA2LD1Temp.setStatus("current")


class _SleHFCEDFA2LD1TempAlarm_Type(Integer32):
    """Custom type sleHFCEDFA2LD1TempAlarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_SleHFCEDFA2LD1TempAlarm_Type.__name__ = "Integer32"
_SleHFCEDFA2LD1TempAlarm_Object = MibTableColumn
sleHFCEDFA2LD1TempAlarm = _SleHFCEDFA2LD1TempAlarm_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 15, 1, 1, 30),
    _SleHFCEDFA2LD1TempAlarm_Type()
)
sleHFCEDFA2LD1TempAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleHFCEDFA2LD1TempAlarm.setStatus("current")
_SleHFCEDFA2LD2Temp_Type = OctetString
_SleHFCEDFA2LD2Temp_Object = MibTableColumn
sleHFCEDFA2LD2Temp = _SleHFCEDFA2LD2Temp_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 15, 1, 1, 31),
    _SleHFCEDFA2LD2Temp_Type()
)
sleHFCEDFA2LD2Temp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleHFCEDFA2LD2Temp.setStatus("current")


class _SleHFCEDFA2LD2TempAlarm_Type(Integer32):
    """Custom type sleHFCEDFA2LD2TempAlarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_SleHFCEDFA2LD2TempAlarm_Type.__name__ = "Integer32"
_SleHFCEDFA2LD2TempAlarm_Object = MibTableColumn
sleHFCEDFA2LD2TempAlarm = _SleHFCEDFA2LD2TempAlarm_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 15, 1, 1, 32),
    _SleHFCEDFA2LD2TempAlarm_Type()
)
sleHFCEDFA2LD2TempAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleHFCEDFA2LD2TempAlarm.setStatus("current")
_SleHFCEDFA2CaseTemp_Type = OctetString
_SleHFCEDFA2CaseTemp_Object = MibTableColumn
sleHFCEDFA2CaseTemp = _SleHFCEDFA2CaseTemp_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 15, 1, 1, 33),
    _SleHFCEDFA2CaseTemp_Type()
)
sleHFCEDFA2CaseTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleHFCEDFA2CaseTemp.setStatus("current")


class _SleHFCEDFA2CaseTempAlarm_Type(Integer32):
    """Custom type sleHFCEDFA2CaseTempAlarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_SleHFCEDFA2CaseTempAlarm_Type.__name__ = "Integer32"
_SleHFCEDFA2CaseTempAlarm_Object = MibTableColumn
sleHFCEDFA2CaseTempAlarm = _SleHFCEDFA2CaseTempAlarm_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 15, 1, 1, 34),
    _SleHFCEDFA2CaseTempAlarm_Type()
)
sleHFCEDFA2CaseTempAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleHFCEDFA2CaseTempAlarm.setStatus("current")
_SleHFCControl_ObjectIdentity = ObjectIdentity
sleHFCControl = _SleHFCControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 15, 2)
)


class _SleHFCControlRequest_Type(Integer32):
    """Custom type sleHFCControlRequest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("setHFCAlarmStatus", 1)
    )


_SleHFCControlRequest_Type.__name__ = "Integer32"
_SleHFCControlRequest_Object = MibScalar
sleHFCControlRequest = _SleHFCControlRequest_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 15, 2, 1),
    _SleHFCControlRequest_Type()
)
sleHFCControlRequest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleHFCControlRequest.setStatus("current")
_SleHFCControlStatus_Type = SleControlStatusType
_SleHFCControlStatus_Object = MibScalar
sleHFCControlStatus = _SleHFCControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 15, 2, 2),
    _SleHFCControlStatus_Type()
)
sleHFCControlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleHFCControlStatus.setStatus("current")
_SleHFCControlTimer_Type = Gauge32
_SleHFCControlTimer_Object = MibScalar
sleHFCControlTimer = _SleHFCControlTimer_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 15, 2, 3),
    _SleHFCControlTimer_Type()
)
sleHFCControlTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleHFCControlTimer.setStatus("current")
_SleHFCControlTimeStamp_Type = TimeTicks
_SleHFCControlTimeStamp_Object = MibScalar
sleHFCControlTimeStamp = _SleHFCControlTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 15, 2, 4),
    _SleHFCControlTimeStamp_Type()
)
sleHFCControlTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleHFCControlTimeStamp.setStatus("current")
_SleHFCControlReqResult_Type = SleControlRequestResultType
_SleHFCControlReqResult_Object = MibScalar
sleHFCControlReqResult = _SleHFCControlReqResult_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 15, 2, 5),
    _SleHFCControlReqResult_Type()
)
sleHFCControlReqResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleHFCControlReqResult.setStatus("current")


class _SleHFCControlAlarmIndex_Type(Integer32):
    """Custom type sleHFCControlAlarmIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("hfcefda1", 0),
          ("hfcefda2", 1),
          ("hfcoptic", 2))
    )


_SleHFCControlAlarmIndex_Type.__name__ = "Integer32"
_SleHFCControlAlarmIndex_Object = MibScalar
sleHFCControlAlarmIndex = _SleHFCControlAlarmIndex_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 15, 2, 6),
    _SleHFCControlAlarmIndex_Type()
)
sleHFCControlAlarmIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleHFCControlAlarmIndex.setStatus("current")


class _SleHFCControlAlarmStatus_Type(Integer32):
    """Custom type sleHFCControlAlarmStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_SleHFCControlAlarmStatus_Type.__name__ = "Integer32"
_SleHFCControlAlarmStatus_Object = MibScalar
sleHFCControlAlarmStatus = _SleHFCControlAlarmStatus_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 15, 2, 7),
    _SleHFCControlAlarmStatus_Type()
)
sleHFCControlAlarmStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleHFCControlAlarmStatus.setStatus("current")
_SleHFCNotification_ObjectIdentity = ObjectIdentity
sleHFCNotification = _SleHFCNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 15, 3)
)
sleSlotSystemInfoEntry.registerAugmentions(
    ("SLE-DEVICE-MIB",
     "sleSlotProtectionIUEntry")
)
sleSlotProtectionIUEntry.setIndexNames(*sleSlotSystemInfoEntry.getIndexNames())

# Managed Objects groups

sleDeviceGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 16)
)
sleDeviceGroup.setObjects(
      *(("SLE-DEVICE-MIB", "sleRfConnectStatus"),
        ("SLE-DEVICE-MIB", "sleRfPortIndex"),
        ("SLE-DEVICE-MIB", "sleRfPortAdminStatus"),
        ("SLE-DEVICE-MIB", "sleRfPortOperStatus"),
        ("SLE-DEVICE-MIB", "sleDeviceEthernetPortNum"),
        ("SLE-DEVICE-MIB", "sleDevicePowerNum"),
        ("SLE-DEVICE-MIB", "sleDeviceFanModuleNum"),
        ("SLE-DEVICE-MIB", "sleDeviceTemperatureNum"),
        ("SLE-DEVICE-MIB", "sleDeviceFanStartTemperature"),
        ("SLE-DEVICE-MIB", "sleDeviceFanStopTemperature"),
        ("SLE-DEVICE-MIB", "sleDeviceControlRequest"),
        ("SLE-DEVICE-MIB", "sleDeviceControlStatus"),
        ("SLE-DEVICE-MIB", "sleDeviceControlTimer"),
        ("SLE-DEVICE-MIB", "sleDeviceControlTimeStamp"),
        ("SLE-DEVICE-MIB", "sleDeviceControlReqResult"),
        ("SLE-DEVICE-MIB", "sleDeviceControlFanStartTemperature"),
        ("SLE-DEVICE-MIB", "sleDeviceControlFanStopTemperature"),
        ("SLE-DEVICE-MIB", "sleEthernetPortIndex"),
        ("SLE-DEVICE-MIB", "sleEthernetPortPhyIndex"),
        ("SLE-DEVICE-MIB", "sleEthernetPortType"),
        ("SLE-DEVICE-MIB", "sleEthernetPortAdminStatus"),
        ("SLE-DEVICE-MIB", "sleEthernetPortOperStatus"),
        ("SLE-DEVICE-MIB", "sleEthernetPortTransmissionRate"),
        ("SLE-DEVICE-MIB", "sleEthernetPortDuplexMode"),
        ("SLE-DEVICE-MIB", "sleEthernetPortFlowControl"),
        ("SLE-DEVICE-MIB", "sleEthernetPortNegotiationMode"),
        ("SLE-DEVICE-MIB", "sleEthernetPortJumboFrameSize"),
        ("SLE-DEVICE-MIB", "sleEthernetPortSfpTransceiver"),
        ("SLE-DEVICE-MIB", "sleEthernetPortSfpVendorName"),
        ("SLE-DEVICE-MIB", "sleEthernetPortSfpVendorPartNumber"),
        ("SLE-DEVICE-MIB", "sleEthernetPortSfpVendorRevision"),
        ("SLE-DEVICE-MIB", "sleEthernetPortSfpVendorSerialNumber"),
        ("SLE-DEVICE-MIB", "sleEthernetPortSfpDateCode"),
        ("SLE-DEVICE-MIB", "sleEthernetPortPhysicalRemoteChassis"),
        ("SLE-DEVICE-MIB", "sleEthernetPortPhysicalRemoteSlot"),
        ("SLE-DEVICE-MIB", "sleEthernetPortPhysicalRemotePort"),
        ("SLE-DEVICE-MIB", "sleEthernetPortPhysicalLinkDiscoveryMode"),
        ("SLE-DEVICE-MIB", "sleEthernetPortControlRequest"),
        ("SLE-DEVICE-MIB", "sleEthernetPortControlStatus"),
        ("SLE-DEVICE-MIB", "sleEthernetPortControlTimer"),
        ("SLE-DEVICE-MIB", "sleEthernetPortControlTimeStamp"),
        ("SLE-DEVICE-MIB", "sleEthernetPortControlReqResult"),
        ("SLE-DEVICE-MIB", "sleEthernetPortControlIndex"),
        ("SLE-DEVICE-MIB", "sleEthernetPortControlType"),
        ("SLE-DEVICE-MIB", "sleEthernetPortControlAdminStatus"),
        ("SLE-DEVICE-MIB", "sleEthernetPortControlTransmissionRate"),
        ("SLE-DEVICE-MIB", "sleEthernetPortControlDuplexMode"),
        ("SLE-DEVICE-MIB", "sleEthernetPortControlFlowControl"),
        ("SLE-DEVICE-MIB", "sleEthernetPortControlJumboFrameSize"),
        ("SLE-DEVICE-MIB", "sleEthernetPortControlPhysicalRemoteChassis"),
        ("SLE-DEVICE-MIB", "sleEthernetPortControlPhysicalRemoteSlot"),
        ("SLE-DEVICE-MIB", "sleEthernetPortControlPhysicalRemotePort"),
        ("SLE-DEVICE-MIB", "sleEthernetPortControlPhysicalLinkDiscoveryMode"),
        ("SLE-DEVICE-MIB", "slePowerIndex"),
        ("SLE-DEVICE-MIB", "slePowerPhyIndex"),
        ("SLE-DEVICE-MIB", "slePowerState"),
        ("SLE-DEVICE-MIB", "sleFanModuleIndex"),
        ("SLE-DEVICE-MIB", "sleFanModulePhyIndex"),
        ("SLE-DEVICE-MIB", "sleFanModuleUnitNum"),
        ("SLE-DEVICE-MIB", "sleFanModuleAdminState"),
        ("SLE-DEVICE-MIB", "sleFanModuleControlRequest"),
        ("SLE-DEVICE-MIB", "sleFanModuleControlStatus"),
        ("SLE-DEVICE-MIB", "sleFanModuleControlTimer"),
        ("SLE-DEVICE-MIB", "sleFanModuleControlTimeStamp"),
        ("SLE-DEVICE-MIB", "sleFanModuleControlReqResult"),
        ("SLE-DEVICE-MIB", "sleFanModuleControlIndex"),
        ("SLE-DEVICE-MIB", "sleFanModuleControlAdminState"),
        ("SLE-DEVICE-MIB", "sleFanUnitIndex"),
        ("SLE-DEVICE-MIB", "sleFanUnitOperState"),
        ("SLE-DEVICE-MIB", "sleTemperatureIndex"),
        ("SLE-DEVICE-MIB", "sleTemperatureState"),
        ("SLE-DEVICE-MIB", "sleTemperatureValue"),
        ("SLE-DEVICE-MIB", "sleBatteryIndex"),
        ("SLE-DEVICE-MIB", "sleDoorStatus"),
        ("SLE-DEVICE-MIB", "sleOperationPowerType"),
        ("SLE-DEVICE-MIB", "sleOperationPowerInfo"),
        ("SLE-DEVICE-MIB", "slePSUACPowerState"),
        ("SLE-DEVICE-MIB", "slePSUTemperture"),
        ("SLE-DEVICE-MIB", "slePSUOutVoltage"),
        ("SLE-DEVICE-MIB", "slePSUOverTemp"),
        ("SLE-DEVICE-MIB", "slePSUFirmwareVer"),
        ("SLE-DEVICE-MIB", "sleRBUEquipState"),
        ("SLE-DEVICE-MIB", "sleRBUModeStaus"),
        ("SLE-DEVICE-MIB", "sleBatteryBackupFile"),
        ("SLE-DEVICE-MIB", "sleBatteryBackupControlRequest"),
        ("SLE-DEVICE-MIB", "sleBatteryBackupControlStatus"),
        ("SLE-DEVICE-MIB", "sleBatteryBackupControlTimer"),
        ("SLE-DEVICE-MIB", "sleBatteryBackupControlTimeStamp"),
        ("SLE-DEVICE-MIB", "sleBatteryBackupControlReqResult"),
        ("SLE-DEVICE-MIB", "sleBatteryBackupControlServerIP"),
        ("SLE-DEVICE-MIB", "sleBatteryBackupControlUserID"),
        ("SLE-DEVICE-MIB", "sleBatteryBackupControlPassword"),
        ("SLE-DEVICE-MIB", "sleBatteryBackupControlFlag"),
        ("SLE-DEVICE-MIB", "sleBatteryBackupControlLocalFile"),
        ("SLE-DEVICE-MIB", "sleBatteryBackupControlRemoteFile"),
        ("SLE-DEVICE-MIB", "sleCpuProcessor"),
        ("SLE-DEVICE-MIB", "sleCpuModel"),
        ("SLE-DEVICE-MIB", "sleCpuRevision"),
        ("SLE-DEVICE-MIB", "sleCpuBogomips"),
        ("SLE-DEVICE-MIB", "sleCpuManufacturer"),
        ("SLE-DEVICE-MIB", "sleCpuClock"),
        ("SLE-DEVICE-MIB", "sleCpuBusClock"),
        ("SLE-DEVICE-MIB", "sleRBUTemperature1"),
        ("SLE-DEVICE-MIB", "slePSUTempThreshold"),
        ("SLE-DEVICE-MIB", "sleRBUTemperature2"),
        ("SLE-DEVICE-MIB", "sleRBUOutVoltage"),
        ("SLE-DEVICE-MIB", "sleRBUChargeCurrent"),
        ("SLE-DEVICE-MIB", "sleRBURemainCapacity"),
        ("SLE-DEVICE-MIB", "sleRBUOverTemp"),
        ("SLE-DEVICE-MIB", "sleBatteryLow"),
        ("SLE-DEVICE-MIB", "sleRBUBTStatus"),
        ("SLE-DEVICE-MIB", "sleRBUBTThreshold"),
        ("SLE-DEVICE-MIB", "sleRBURechargeVoltage"),
        ("SLE-DEVICE-MIB", "sleBatteryCellStatus"),
        ("SLE-DEVICE-MIB", "sleBPSUACHardwareVer"),
        ("SLE-DEVICE-MIB", "sleBatteryControlRequest"),
        ("SLE-DEVICE-MIB", "sleBatteryControlStatus"),
        ("SLE-DEVICE-MIB", "sleBatteryControlTimer"),
        ("SLE-DEVICE-MIB", "sleBatteryControlTimeStamp"),
        ("SLE-DEVICE-MIB", "sleBatteryControlReqResult"),
        ("SLE-DEVICE-MIB", "sleBatteryControlRBUBTStatus"),
        ("SLE-DEVICE-MIB", "sleBatteryControlRBUBTThreshold"),
        ("SLE-DEVICE-MIB", "sleBatteryControlRBURechargeVoltage"),
        ("SLE-DEVICE-MIB", "sleBatteryControlTemperThresh1"),
        ("SLE-DEVICE-MIB", "sleBatteryControlTemperThresh2"),
        ("SLE-DEVICE-MIB", "sleRBUTempHighThreshold"),
        ("SLE-DEVICE-MIB", "slePowerType"),
        ("SLE-DEVICE-MIB", "sleClockModuleIndex"),
        ("SLE-DEVICE-MIB", "sleClockModuleBoardId"),
        ("SLE-DEVICE-MIB", "sleClockModuleInstallStatus"),
        ("SLE-DEVICE-MIB", "sleClockModuleInitStatus"),
        ("SLE-DEVICE-MIB", "sleSlotSystemIndex"),
        ("SLE-DEVICE-MIB", "sleSlotSystemUptime"),
        ("SLE-DEVICE-MIB", "sleSlotSystemModelName"),
        ("SLE-DEVICE-MIB", "sleSlotSystemSerialNumber"),
        ("SLE-DEVICE-MIB", "sleSlotSystemHWVersion"),
        ("SLE-DEVICE-MIB", "sleSlotSystemBLVersion"),
        ("SLE-DEVICE-MIB", "sleSlotSystemSWCompatibility"),
        ("SLE-DEVICE-MIB", "sleSlotSystemOSVersion"),
        ("SLE-DEVICE-MIB", "sleSlotSystemMacAddress"),
        ("SLE-DEVICE-MIB", "sleSlotSystemCPULoadAll"),
        ("SLE-DEVICE-MIB", "sleSlotSystemCPULoadInterrupt"),
        ("SLE-DEVICE-MIB", "sleSlotSystemMemoryTotal"),
        ("SLE-DEVICE-MIB", "sleSlotSystemMemoryFree"),
        ("SLE-DEVICE-MIB", "sleSlotSystemMemoryShared"),
        ("SLE-DEVICE-MIB", "sleSlotSystemMemoryBuffers"),
        ("SLE-DEVICE-MIB", "sleSlotSystemMemoryCached"),
        ("SLE-DEVICE-MIB", "sleSlotSystemMemorySwapTotal"),
        ("SLE-DEVICE-MIB", "sleSlotSystemMemorySwapFree"),
        ("SLE-DEVICE-MIB", "sleSlotSystemBootReason"),
        ("SLE-DEVICE-MIB", "sleSlotSystemBootTime"),
        ("SLE-DEVICE-MIB", "sleSlotSystemVoltage"),
        ("SLE-DEVICE-MIB", "sleSlotSystemControlRequest"),
        ("SLE-DEVICE-MIB", "sleSlotSystemControlStatus"),
        ("SLE-DEVICE-MIB", "sleSlotSystemControlTimer"),
        ("SLE-DEVICE-MIB", "sleSlotSystemControlTimeStamp"),
        ("SLE-DEVICE-MIB", "sleSlotSystemControlReqResult"),
        ("SLE-DEVICE-MIB", "sleSlotSystemControlSlotIndex"),
        ("SLE-DEVICE-MIB", "sleSlotStatusPlan"),
        ("SLE-DEVICE-MIB", "sleSlotStatusPlanCardType"),
        ("SLE-DEVICE-MIB", "sleSlotStatusCurrentInstall"),
        ("SLE-DEVICE-MIB", "sleSlotStatusCurrentInstallCardType"),
        ("SLE-DEVICE-MIB", "sleSlotStatusCardOperation"),
        ("SLE-DEVICE-MIB", "sleSlotStatusLock"),
        ("SLE-DEVICE-MIB", "sleSlotStatusUpgradeMode"),
        ("SLE-DEVICE-MIB", "sleSlotStatusActionEvent"),
        ("SLE-DEVICE-MIB", "sleSlotStatusState"),
        ("SLE-DEVICE-MIB", "sleSlotStatusControlRequest"),
        ("SLE-DEVICE-MIB", "sleSlotStatusControlStatus"),
        ("SLE-DEVICE-MIB", "sleSlotStatusControlTimer"),
        ("SLE-DEVICE-MIB", "sleSlotStatusControlTimeStamp"),
        ("SLE-DEVICE-MIB", "sleSlotStatusControlReqResult"),
        ("SLE-DEVICE-MIB", "sleSlotStatusControlSlotIndex"),
        ("SLE-DEVICE-MIB", "sleSlotStatusControlPlanCardType"),
        ("SLE-DEVICE-MIB", "sleSlotStatusControlUpgradeMode"),
        ("SLE-DEVICE-MIB", "sleSlotNosVersion"),
        ("SLE-DEVICE-MIB", "sleSlotNosRevision"),
        ("SLE-DEVICE-MIB", "sleSlotNosSize"),
        ("SLE-DEVICE-MIB", "sleSlotNosUpgradeStatus"),
        ("SLE-DEVICE-MIB", "sleSlotNosControlRequest"),
        ("SLE-DEVICE-MIB", "sleSlotNosControlStatus"),
        ("SLE-DEVICE-MIB", "sleSlotNosControlTimer"),
        ("SLE-DEVICE-MIB", "sleSlotNosControlTimeStamp"),
        ("SLE-DEVICE-MIB", "sleSlotNosControlReqResult"),
        ("SLE-DEVICE-MIB", "sleSlotNosControlSlotIndex"),
        ("SLE-DEVICE-MIB", "sleSlotReleasedNIUNosVersion"),
        ("SLE-DEVICE-MIB", "sleSlotReleasedNIUNosRevision"),
        ("SLE-DEVICE-MIB", "sleSlotReleasedNIUNosSize"),
        ("SLE-DEVICE-MIB", "sleSlotReleasedGPIUNosVersion"),
        ("SLE-DEVICE-MIB", "sleSlotReleasedGPIUNosRevision"),
        ("SLE-DEVICE-MIB", "sleSlotReleasedGPIUNosSize"),
        ("SLE-DEVICE-MIB", "sleSlotSystemPowerLevelStatus"),
        ("SLE-DEVICE-MIB", "sleSlotPowerMonStatus"),
        ("SLE-DEVICE-MIB", "sleSlotPowerMonVoltage"),
        ("SLE-DEVICE-MIB", "sleEthernetPortDMIIndex"),
        ("SLE-DEVICE-MIB", "sleEthernetPortDMITemper"),
        ("SLE-DEVICE-MIB", "sleEthernetPortDMIVoltage"),
        ("SLE-DEVICE-MIB", "sleEthernetPortDMITxBias"),
        ("SLE-DEVICE-MIB", "sleEthernetPortDMITxPower"),
        ("SLE-DEVICE-MIB", "sleEthernetPortDMIRxPower"),
        ("SLE-DEVICE-MIB", "sleEthernetPortSfpTransceiverType"),
        ("SLE-DEVICE-MIB", "sleSlotNosControlUpDownMethod"),
        ("SLE-DEVICE-MIB", "sleSlotNosControlUpDownFlag"),
        ("SLE-DEVICE-MIB", "sleSlotNosControlServerAddress"),
        ("SLE-DEVICE-MIB", "sleSlotNosControlUserID"),
        ("SLE-DEVICE-MIB", "sleSlotNosControlPassword"),
        ("SLE-DEVICE-MIB", "sleSlotNosControlFileName"),
        ("SLE-DEVICE-MIB", "sleFanUnitSpeed"),
        ("SLE-DEVICE-MIB", "sleSlotSystemInfoLEDStatus"),
        ("SLE-DEVICE-MIB", "sleFanModuleSpeedThreshold"),
        ("SLE-DEVICE-MIB", "sleFanModuleControlSpeedThreshold"),
        ("SLE-DEVICE-MIB", "sleEthernetPortSfpTransceiverDetailType"),
        ("SLE-DEVICE-MIB", "sleClockModuleOPMode"),
        ("SLE-DEVICE-MIB", "sleClockInfoInSrcType"),
        ("SLE-DEVICE-MIB", "sleClockInfoInSrcAISStatus"),
        ("SLE-DEVICE-MIB", "sleClockInfoInSrcLoSStatus"),
        ("SLE-DEVICE-MIB", "sleClockInfoInSrcLDSCStatus"),
        ("SLE-DEVICE-MIB", "sleClockInfoInSrcNtrClockType"),
        ("SLE-DEVICE-MIB", "sleDeviceJumboFrameStatus"),
        ("SLE-DEVICE-MIB", "sleDeviceControlJumboFrameStatus"),
        ("SLE-DEVICE-MIB", "slePowerPSUType"),
        ("SLE-DEVICE-MIB", "sleSlotSystemInfoPackageVersion"),
        ("SLE-DEVICE-MIB", "sleEthernetSfpIndex"),
        ("SLE-DEVICE-MIB", "sleEthernetSfpTransceiver"),
        ("SLE-DEVICE-MIB", "sleEthernetSfpVendorName"),
        ("SLE-DEVICE-MIB", "sleEthernetSfpVendorPartNumber"),
        ("SLE-DEVICE-MIB", "sleEthernetSfpDateCode"),
        ("SLE-DEVICE-MIB", "sleEthernetSfpTransceiverType"),
        ("SLE-DEVICE-MIB", "sleEthernetSfpTransceiverDetailType"),
        ("SLE-DEVICE-MIB", "sleTemperatureHighThreshold"),
        ("SLE-DEVICE-MIB", "sleTemperatureLowThreshold"),
        ("SLE-DEVICE-MIB", "sleTemperatureControlRequest"),
        ("SLE-DEVICE-MIB", "sleTemperatureControlStatus"),
        ("SLE-DEVICE-MIB", "sleTemperatureControlTimer"),
        ("SLE-DEVICE-MIB", "sleTemperatureControlTimeStamp"),
        ("SLE-DEVICE-MIB", "sleTemperatureControlReqResult"),
        ("SLE-DEVICE-MIB", "sleTemperatureControlIndex"),
        ("SLE-DEVICE-MIB", "sleTemperatureControlHighThreshold"),
        ("SLE-DEVICE-MIB", "sleTemperatureControlLowThreshold"),
        ("SLE-DEVICE-MIB", "sleEthernetSFPControlRequest"),
        ("SLE-DEVICE-MIB", "sleEthernetSFPControlStatus"),
        ("SLE-DEVICE-MIB", "sleEthernetSFPControlTimer"),
        ("SLE-DEVICE-MIB", "sleEthernetSFPControlTimeStamp"),
        ("SLE-DEVICE-MIB", "sleEthernetSFPControlReqResult"),
        ("SLE-DEVICE-MIB", "sleEthernetSFPControlIndex"),
        ("SLE-DEVICE-MIB", "sleTemperatureWarnHighThreshold"),
        ("SLE-DEVICE-MIB", "sleTemperatureWarnLowThreshold"),
        ("SLE-DEVICE-MIB", "sleTemperatureWarnDuration"),
        ("SLE-DEVICE-MIB", "sleTemperatureAlarmHighThreshold"),
        ("SLE-DEVICE-MIB", "sleTemperatureAlarmLowThreshold"),
        ("SLE-DEVICE-MIB", "sleTemperatureAlarmDuration"),
        ("SLE-DEVICE-MIB", "sleTemperatureControlDuration"),
        ("SLE-DEVICE-MIB", "sleSlotPowerMonIndex"),
        ("SLE-DEVICE-MIB", "sleEthernetPortSlotIndex"),
        ("SLE-DEVICE-MIB", "sleEthernetPortSlotPortIndex"),
        ("SLE-DEVICE-MIB", "sleEthernetSfpVendorRevision"),
        ("SLE-DEVICE-MIB", "sleEthernetSfpVendorSerialNumber"),
        ("SLE-DEVICE-MIB", "sleEthernetSfpTransceiverCodes"),
        ("SLE-DEVICE-MIB", "sleSlotNosStbVersion"),
        ("SLE-DEVICE-MIB", "sleSlotNosStbRevision"),
        ("SLE-DEVICE-MIB", "sleSlotNosStbSize"),
        ("SLE-DEVICE-MIB", "sleDeviceEnvironmentMonitoringStatus"),
        ("SLE-DEVICE-MIB", "sleDeviceControlEnvironmentMonitoringStatus"),
        ("SLE-DEVICE-MIB", "sleRfPowerStatus"),
        ("SLE-DEVICE-MIB", "sleSlotAiuRunStatus"),
        ("SLE-DEVICE-MIB", "sleSlotAiuAlarmStatus"),
        ("SLE-DEVICE-MIB", "sleEthernetPortAdminTransmissionRate"),
        ("SLE-DEVICE-MIB", "sleEthernetPortAdminDuplexMode"),
        ("SLE-DEVICE-MIB", "sleEthernetPortAdminFlowControl"),
        ("SLE-DEVICE-MIB", "sleEthernetPortAdminNegotiationMode"),
        ("SLE-DEVICE-MIB", "sleSlotReleasedSIUNosVersion"),
        ("SLE-DEVICE-MIB", "sleSlotReleasedSIUNosRevision"),
        ("SLE-DEVICE-MIB", "sleSlotReleasedSIUNosSize"),
        ("SLE-DEVICE-MIB", "sleEMInputIndex"),
        ("SLE-DEVICE-MIB", "sleEMAlarmString"),
        ("SLE-DEVICE-MIB", "sleEMAlarmSeverity"),
        ("SLE-DEVICE-MIB", "sleEMmode"),
        ("SLE-DEVICE-MIB", "sleEMControlRequest"),
        ("SLE-DEVICE-MIB", "sleEMControlStatus"),
        ("SLE-DEVICE-MIB", "sleEMControlInputIndex"),
        ("SLE-DEVICE-MIB", "sleEMControlAlarmString"),
        ("SLE-DEVICE-MIB", "sleEMControlAlarmSeverity"),
        ("SLE-DEVICE-MIB", "sleEMControlmode"),
        ("SLE-DEVICE-MIB", "sleEthernetSfpSpeed"),
        ("SLE-DEVICE-MIB", "sleEthernetSfpLength"),
        ("SLE-DEVICE-MIB", "sleEthernetSfpWaveLength"),
        ("SLE-DEVICE-MIB", "sleRfEthertype"),
        ("SLE-DEVICE-MIB", "sleRfSrcAddress"),
        ("SLE-DEVICE-MIB", "sleRfDesAddress"),
        ("SLE-DEVICE-MIB", "sleRBUTempLowThreshold"),
        ("SLE-DEVICE-MIB", "sleEthernetPortControlNegotiationMode"),
        ("SLE-DEVICE-MIB", "sleSlotStatusPower"),
        ("SLE-DEVICE-MIB", "sleSlotStatusSerialNumber"),
        ("SLE-DEVICE-MIB", "sleEMControlTimer"),
        ("SLE-DEVICE-MIB", "sleEMControlTimeStamp"),
        ("SLE-DEVICE-MIB", "sleEthernetPortAdminReason"),
        ("SLE-DEVICE-MIB", "sleEMControlReqResult"),
        ("SLE-DEVICE-MIB", "sleRfBaseControlRequest"),
        ("SLE-DEVICE-MIB", "sleRfBaseControlStatus"),
        ("SLE-DEVICE-MIB", "sleRfBaseControlTimer"),
        ("SLE-DEVICE-MIB", "sleRfBaseControlTimeStamp"),
        ("SLE-DEVICE-MIB", "sleRfBaseControlReqResult"),
        ("SLE-DEVICE-MIB", "sleRfBaseControlRfEthertype"),
        ("SLE-DEVICE-MIB", "sleRfPortControlRequest"),
        ("SLE-DEVICE-MIB", "sleRfPortControlStatus"),
        ("SLE-DEVICE-MIB", "sleRfPortControlTimer"),
        ("SLE-DEVICE-MIB", "sleRfPortControlTimeStamp"),
        ("SLE-DEVICE-MIB", "sleRfPortControlReqResult"),
        ("SLE-DEVICE-MIB", "sleRfPortControlIndex"),
        ("SLE-DEVICE-MIB", "sleBypassMode"),
        ("SLE-DEVICE-MIB", "sleBypassStatus"),
        ("SLE-DEVICE-MIB", "sleBypassBaseControlRequest"),
        ("SLE-DEVICE-MIB", "sleBypassBaseControlStatus"),
        ("SLE-DEVICE-MIB", "sleBypassBaseControlTimer"),
        ("SLE-DEVICE-MIB", "sleBypassBaseControlTimeStamp"),
        ("SLE-DEVICE-MIB", "sleBypassBaseControlReqResult"),
        ("SLE-DEVICE-MIB", "sleBypassBaseControlMode"),
        ("SLE-DEVICE-MIB", "sleBypassOptionConnectivityAddress"),
        ("SLE-DEVICE-MIB", "sleBypassOptionConnectivityPort"),
        ("SLE-DEVICE-MIB", "sleBypassOptionConnectivityControlRequest"),
        ("SLE-DEVICE-MIB", "sleBypassOptionConnectivityControlStatus"),
        ("SLE-DEVICE-MIB", "sleBypassOptionConnectivityControlTimer"),
        ("SLE-DEVICE-MIB", "sleBypassOptionConnectivityControlTimeStamp"),
        ("SLE-DEVICE-MIB", "sleBypassOptionConnectivityControlReqResult"),
        ("SLE-DEVICE-MIB", "sleBypassOptionConnectivityControlAddress"),
        ("SLE-DEVICE-MIB", "sleBypassOptionConnectivityControlPort"),
        ("SLE-DEVICE-MIB", "sleBypassOptionPingAddress"),
        ("SLE-DEVICE-MIB", "sleBypassOptionPingTransInterval"),
        ("SLE-DEVICE-MIB", "sleBypassOptionPingTranNumber"),
        ("SLE-DEVICE-MIB", "sleBypassOptionPingReqInterval"),
        ("SLE-DEVICE-MIB", "sleBypassOptionPingReqTimeout"),
        ("SLE-DEVICE-MIB", "sleBypassOptionPingLossThresh"),
        ("SLE-DEVICE-MIB", "sleBypassOptionPingControlRequest"),
        ("SLE-DEVICE-MIB", "sleBypassOptionPingControlStatus"),
        ("SLE-DEVICE-MIB", "sleBypassOptionPingControlTimer"),
        ("SLE-DEVICE-MIB", "sleBypassOptionPingControlTimeStamp"),
        ("SLE-DEVICE-MIB", "sleBypassOptionPingControlReqResult"),
        ("SLE-DEVICE-MIB", "sleBypassOptionPingControlAddress"),
        ("SLE-DEVICE-MIB", "sleBypassOptionPingControlTransInterval"),
        ("SLE-DEVICE-MIB", "sleBypassOptionPingControlTranNumber"),
        ("SLE-DEVICE-MIB", "sleBypassOptionPingControlReqInterval"),
        ("SLE-DEVICE-MIB", "sleBypassOptionPingControlReqTimeout"),
        ("SLE-DEVICE-MIB", "sleBypassOptionPingControlLossThresh"),
        ("SLE-DEVICE-MIB", "sleBypassOptionLinkMonitorPort"),
        ("SLE-DEVICE-MIB", "sleBypassOptionLinkMonitorPortStatus"),
        ("SLE-DEVICE-MIB", "sleBypassOptionLinkMonitorControlRequest"),
        ("SLE-DEVICE-MIB", "sleBypassOptionLinkMonitorControlStatus"),
        ("SLE-DEVICE-MIB", "sleBypassOptionLinkMonitorControlTimer"),
        ("SLE-DEVICE-MIB", "sleBypassOptionLinkMonitorControlTimeStamp"),
        ("SLE-DEVICE-MIB", "sleBypassOptionLinkMonitorControlReqResult"),
        ("SLE-DEVICE-MIB", "sleBypassOptionLinkMonitorControlPort"),
        ("SLE-DEVICE-MIB", "sleBypassOptionLinkMonitorControlPortStatus"),
        ("SLE-DEVICE-MIB", "sleSlotSystemInfoManufacturer"),
        ("SLE-DEVICE-MIB", "sleSlotSystemInfoManufactureDate"),
        ("SLE-DEVICE-MIB", "sleSlotStatusHealthState"),
        ("SLE-DEVICE-MIB", "sleRfPortControlAdminStatus"),
        ("SLE-DEVICE-MIB", "sleClockInfoInSrcStatus"),
        ("SLE-DEVICE-MIB", "sleEthernetSfpMultimodeLengthOm1"),
        ("SLE-DEVICE-MIB", "sleEthernetSfpMultimodeLengthOm2"),
        ("SLE-DEVICE-MIB", "sleEthernetSfpTransceiverDetailTypeStr"),
        ("SLE-DEVICE-MIB", "sleEthernetSfpTransceiverLengthStr"),
        ("SLE-DEVICE-MIB", "sleEthernetSfpWaveLengthStr"),
        ("SLE-DEVICE-MIB", "sleEthernetSfpConnectorType"),
        ("SLE-DEVICE-MIB", "sleSlotReleasedIU10GE8NosVersion"),
        ("SLE-DEVICE-MIB", "sleSlotReleasedIU10GE8NosRevision"),
        ("SLE-DEVICE-MIB", "sleSlotReleasedIU10GE8NosSize"),
        ("SLE-DEVICE-MIB", "sleSlotReleasedIU10GEPON8NosVersion"),
        ("SLE-DEVICE-MIB", "sleSlotReleasedIU10GEPON8NosRevision"),
        ("SLE-DEVICE-MIB", "sleSlotReleasedIU10GEPON8NosSize"),
        ("SLE-DEVICE-MIB", "sleSlotReleasedIUGEPON8NosVersion"),
        ("SLE-DEVICE-MIB", "sleSlotReleasedIUGEPON8NosRevision"),
        ("SLE-DEVICE-MIB", "sleSlotReleasedIUGEPON8NosSize"),
        ("SLE-DEVICE-MIB", "sleEthernetSfpMultimodeLengthOm3"),
        ("SLE-DEVICE-MIB", "sleSlotProtectionSystemStatus"),
        ("SLE-DEVICE-MIB", "sleSlotProtectionSystemThreshold"),
        ("SLE-DEVICE-MIB", "sleSlotProtectionControlRequest"),
        ("SLE-DEVICE-MIB", "sleSlotProtectionControlStatus"),
        ("SLE-DEVICE-MIB", "sleSlotProtectionControlTimer"),
        ("SLE-DEVICE-MIB", "sleSlotProtectionControlTimeStamp"),
        ("SLE-DEVICE-MIB", "sleSlotProtectionControlReqResult"),
        ("SLE-DEVICE-MIB", "sleSlotProtectionControlSystemStatus"),
        ("SLE-DEVICE-MIB", "sleSlotProtectionControlSystemThreshold"),
        ("SLE-DEVICE-MIB", "sleSlotProtectionIUControlRequest"),
        ("SLE-DEVICE-MIB", "sleSlotProtectionIUControlStatus"),
        ("SLE-DEVICE-MIB", "sleSlotProtectionIUControlTimer"),
        ("SLE-DEVICE-MIB", "sleSlotProtectionIUControlTimeStamp"),
        ("SLE-DEVICE-MIB", "sleSlotProtectionIUControlReqResult"),
        ("SLE-DEVICE-MIB", "sleSlotProtectionIUControlTemperHighThresh"),
        ("SLE-DEVICE-MIB", "sleSlotProtectionIUControlTemperLowThresh"),
        ("SLE-DEVICE-MIB", "sleSlotProtectionIUControlPowerThresh"),
        ("SLE-DEVICE-MIB", "sleSlotProtectionIUTemperHighThresh"),
        ("SLE-DEVICE-MIB", "sleSlotProtectionIUTemperLowThresh"),
        ("SLE-DEVICE-MIB", "sleSlotProtectionIUPowerStatus"),
        ("SLE-DEVICE-MIB", "sleSlotProtectionIUPowerThresh"),
        ("SLE-DEVICE-MIB", "sleSlotProtectionIUTemper"),
        ("SLE-DEVICE-MIB", "sleHFCOptic1550OTX"),
        ("SLE-DEVICE-MIB", "sleHFCOptic1550OTXAlarm"),
        ("SLE-DEVICE-MIB", "sleHFCOpticUpstreamOTX"),
        ("SLE-DEVICE-MIB", "sleHFCOpticUpstreamOTXAlarm"),
        ("SLE-DEVICE-MIB", "sleHFCOpticDownstreamORX"),
        ("SLE-DEVICE-MIB", "sleHFCOpticDownstreamORXAlarm"),
        ("SLE-DEVICE-MIB", "sleHFCEDFA1OTX"),
        ("SLE-DEVICE-MIB", "sleHFCEDFA1OTXAlarm"),
        ("SLE-DEVICE-MIB", "sleHFCEDFA1ORX"),
        ("SLE-DEVICE-MIB", "sleHFCEDFA1ORXAlarm"),
        ("SLE-DEVICE-MIB", "sleHFCEDFA1LD1Current"),
        ("SLE-DEVICE-MIB", "sleHFCEDFA1LD1CurrentAlarm"),
        ("SLE-DEVICE-MIB", "sleHFCEDFA1LD2Current"),
        ("SLE-DEVICE-MIB", "sleHFCEDFA1LD2CurrentAlarm"),
        ("SLE-DEVICE-MIB", "sleHFCEDFA1LD1Temp"),
        ("SLE-DEVICE-MIB", "sleHFCEDFA1LD1TempAlarm"),
        ("SLE-DEVICE-MIB", "sleHFCEDFA1LD2Temp"),
        ("SLE-DEVICE-MIB", "sleHFCEDFA1LD2TempAlarm"),
        ("SLE-DEVICE-MIB", "sleHFCEDFA1CaseTemp"),
        ("SLE-DEVICE-MIB", "sleHFCEDFA1CaseTempAlarm"),
        ("SLE-DEVICE-MIB", "sleHFCEDFA2OTX"),
        ("SLE-DEVICE-MIB", "sleHFCEDFA2OTXAarm"),
        ("SLE-DEVICE-MIB", "sleHFCEDFA2ORX"),
        ("SLE-DEVICE-MIB", "sleHFCEDFA2ORXAlarm"),
        ("SLE-DEVICE-MIB", "sleHFCEDFA2LD1Current"),
        ("SLE-DEVICE-MIB", "sleHFCEDFA2LD1CurrentAlarm"),
        ("SLE-DEVICE-MIB", "sleHFCEDFA2LD2Current"),
        ("SLE-DEVICE-MIB", "sleHFCEDFA2LD2CurrentAlarm"),
        ("SLE-DEVICE-MIB", "sleHFCEDFA2LD1Temp"),
        ("SLE-DEVICE-MIB", "sleHFCEDFA2LD1TempAlarm"),
        ("SLE-DEVICE-MIB", "sleHFCEDFA2LD2Temp"),
        ("SLE-DEVICE-MIB", "sleHFCEDFA2LD2TempAlarm"),
        ("SLE-DEVICE-MIB", "sleHFCEDFA2CaseTemp"),
        ("SLE-DEVICE-MIB", "sleHFCEDFA2CaseTempAlarm"),
        ("SLE-DEVICE-MIB", "sleHFCControlRequest"),
        ("SLE-DEVICE-MIB", "sleHFCControlStatus"),
        ("SLE-DEVICE-MIB", "sleHFCControlTimer"),
        ("SLE-DEVICE-MIB", "sleHFCControlTimeStamp"),
        ("SLE-DEVICE-MIB", "sleHFCControlReqResult"),
        ("SLE-DEVICE-MIB", "sleHFCControlAlarmIndex"),
        ("SLE-DEVICE-MIB", "sleHFCControlAlarmStatus"),
        ("SLE-DEVICE-MIB", "sleSlotSystemCPULoadHighThreshold"),
        ("SLE-DEVICE-MIB", "sleSlotSystemCPULoadHighThresholdTimer"),
        ("SLE-DEVICE-MIB", "sleSlotSystemCPULoadLowThreshold"),
        ("SLE-DEVICE-MIB", "sleSlotSystemCPULoadLowThresholdTimer"),
        ("SLE-DEVICE-MIB", "sleSlotProtectionIUControlindex"),
        ("SLE-DEVICE-MIB", "sleSlotSystemCPULoadCurrent"),
        ("SLE-DEVICE-MIB", "sleEthernetPortLinkCheckTimer"),
        ("SLE-DEVICE-MIB", "sleEthernetPortLinkDebounceTime"),
        ("SLE-DEVICE-MIB", "sleEthernetPortCpuStatisticsLimitUnicast"),
        ("SLE-DEVICE-MIB", "sleEthernetPortCpuStatisticsLimitMulticast"),
        ("SLE-DEVICE-MIB", "sleEthernetPortCpuStatisticsLimitBroadcast"),
        ("SLE-DEVICE-MIB", "sleEthernetPortFloodBlockBroadcastState"),
        ("SLE-DEVICE-MIB", "sleEthernetPortFloodBlockDlfState"),
        ("SLE-DEVICE-MIB", "sleEthernetPortControlLinkCheckTimer"),
        ("SLE-DEVICE-MIB", "sleEthernetPortControlLinkDebounceTime"),
        ("SLE-DEVICE-MIB", "sleEthernetPortControlCpuStatisticsLimitUnicast"),
        ("SLE-DEVICE-MIB", "sleEthernetPortControlCpuStatisticsLimitMulticast"),
        ("SLE-DEVICE-MIB", "sleEthernetPortControlCpuStatisticsLimitBroadcast"),
        ("SLE-DEVICE-MIB", "sleEthernetPortControlFloodBlockBroadcastState"),
        ("SLE-DEVICE-MIB", "sleEthernetPortControlFloodBlockDlfState"),
        ("SLE-DEVICE-MIB", "sleEthernetSfpDdmState"),
        ("SLE-DEVICE-MIB", "sleEthernetSfpNegoState"),
        ("SLE-DEVICE-MIB", "sleEthernetSfpControlDdmState"),
        ("SLE-DEVICE-MIB", "sleEthernetSFPThresholdIfIndex"),
        ("SLE-DEVICE-MIB", "sleEthernetSFPThresholdType"),
        ("SLE-DEVICE-MIB", "sleEthernetSFPThresholdSfpLow"),
        ("SLE-DEVICE-MIB", "sleEthernetSFPThresholdSfpHigh"),
        ("SLE-DEVICE-MIB", "sleEthernetSFPThresholdSystemLow"),
        ("SLE-DEVICE-MIB", "sleEthernetSFPThresholdSystemHigh"),
        ("SLE-DEVICE-MIB", "sleEthernetSFPThresholdControlRequest"),
        ("SLE-DEVICE-MIB", "sleEthernetSFPThresholdControlStatus"),
        ("SLE-DEVICE-MIB", "sleEthernetSFPThresholdControlTimer"),
        ("SLE-DEVICE-MIB", "sleEthernetSFPThresholdControlTimeStamp"),
        ("SLE-DEVICE-MIB", "sleEthernetSFPThresholdControlReqResult"),
        ("SLE-DEVICE-MIB", "sleEthernetSFPThresholdControlIfIndex"),
        ("SLE-DEVICE-MIB", "sleEthernetSFPThresholdControlType"),
        ("SLE-DEVICE-MIB", "sleEthernetSFPThresholdControlSfpLow"),
        ("SLE-DEVICE-MIB", "sleEthernetSFPThresholdControlSfpHigh"),
        ("SLE-DEVICE-MIB", "sleEthernetSFPThresholdControlSystemLow"),
        ("SLE-DEVICE-MIB", "sleEthernetSFPThresholdControlSystemHigh"),
        ("SLE-DEVICE-MIB", "sleSlotSystemCPUOverallStatus"),
        ("SLE-DEVICE-MIB", "sleSlotSystemTemperOverallStatus"),
        ("SLE-DEVICE-MIB", "sleslotStatusOverallState"),
        ("SLE-DEVICE-MIB", "sleslotStatusSyncState"),
        ("SLE-DEVICE-MIB", "sleSlotProtectionIUTemper2"),
        ("SLE-DEVICE-MIB", "sleSlotProtectionControlIUPowerStatus"),
        ("SLE-DEVICE-MIB", "sleSlotSystemControlCPULoadHighThreshold"),
        ("SLE-DEVICE-MIB", "sleSlotSystemControlCPULoadHighThresholdTimer"),
        ("SLE-DEVICE-MIB", "sleSlotSystemControlCPULoadLowThreshold"),
        ("SLE-DEVICE-MIB", "sleSlotSystemControlCPULoadLowThresholdTimer"))
)
if mibBuilder.loadTexts:
    sleDeviceGroup.setStatus("current")


# Notification objects

sleDeviceTemperatureThresholdChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 1, 3, 1)
)
sleDeviceTemperatureThresholdChanged.setObjects(
      *(("SLE-DEVICE-MIB", "sleDeviceFanStartTemperature"),
        ("SLE-DEVICE-MIB", "sleDeviceFanStopTemperature"),
        ("SLE-DEVICE-MIB", "sleDeviceControlRequest"),
        ("SLE-DEVICE-MIB", "sleDeviceControlTimeStamp"),
        ("SLE-DEVICE-MIB", "sleDeviceControlReqResult"))
)
if mibBuilder.loadTexts:
    sleDeviceTemperatureThresholdChanged.setStatus(
        "current"
    )

sleDeviceJumboFrameChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 1, 3, 2)
)
sleDeviceJumboFrameChanged.setObjects(
      *(("SLE-DEVICE-MIB", "sleDeviceControlRequest"),
        ("SLE-DEVICE-MIB", "sleDeviceControlTimeStamp"),
        ("SLE-DEVICE-MIB", "sleDeviceControlReqResult"),
        ("SLE-DEVICE-MIB", "sleDeviceControlJumboFrameStatus"))
)
if mibBuilder.loadTexts:
    sleDeviceJumboFrameChanged.setStatus(
        "current"
    )

sleDeviceLEDTestChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 1, 3, 3)
)
sleDeviceLEDTestChanged.setObjects(
      *(("SLE-DEVICE-MIB", "sleDeviceControlRequest"),
        ("SLE-DEVICE-MIB", "sleDeviceControlTimeStamp"),
        ("SLE-DEVICE-MIB", "sleDeviceControlReqResult"))
)
if mibBuilder.loadTexts:
    sleDeviceLEDTestChanged.setStatus(
        "current"
    )

sleDeviceEnvironmentMonitoringStatusChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 1, 3, 4)
)
sleDeviceEnvironmentMonitoringStatusChanged.setObjects(
      *(("SLE-DEVICE-MIB", "sleDeviceControlRequest"),
        ("SLE-DEVICE-MIB", "sleDeviceControlTimeStamp"),
        ("SLE-DEVICE-MIB", "sleDeviceControlReqResult"),
        ("SLE-DEVICE-MIB", "sleDeviceEnvironmentMonitoringStatus"))
)
if mibBuilder.loadTexts:
    sleDeviceEnvironmentMonitoringStatusChanged.setStatus(
        "current"
    )

sleEthernetPortChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 2, 3, 1)
)
sleEthernetPortChanged.setObjects(
      *(("SLE-DEVICE-MIB", "sleEthernetPortType"),
        ("SLE-DEVICE-MIB", "sleEthernetPortAdminStatus"),
        ("SLE-DEVICE-MIB", "sleEthernetPortTransmissionRate"),
        ("SLE-DEVICE-MIB", "sleEthernetPortDuplexMode"),
        ("SLE-DEVICE-MIB", "sleEthernetPortFlowControl"),
        ("SLE-DEVICE-MIB", "sleEthernetPortNegotiationMode"),
        ("SLE-DEVICE-MIB", "sleEthernetPortJumboFrameSize"),
        ("SLE-DEVICE-MIB", "sleEthernetPortSfpVendorName"),
        ("SLE-DEVICE-MIB", "sleEthernetPortSfpVendorPartNumber"),
        ("SLE-DEVICE-MIB", "sleEthernetPortSfpVendorRevision"),
        ("SLE-DEVICE-MIB", "sleEthernetPortSfpVendorSerialNumber"),
        ("SLE-DEVICE-MIB", "sleEthernetPortSfpDateCode"),
        ("SLE-DEVICE-MIB", "sleEthernetPortPhysicalRemoteChassis"),
        ("SLE-DEVICE-MIB", "sleEthernetPortPhysicalRemoteSlot"),
        ("SLE-DEVICE-MIB", "sleEthernetPortPhysicalRemotePort"),
        ("SLE-DEVICE-MIB", "sleEthernetPortPhysicalLinkDiscoveryMode"),
        ("SLE-DEVICE-MIB", "sleEthernetPortControlRequest"),
        ("SLE-DEVICE-MIB", "sleEthernetPortControlTimeStamp"),
        ("SLE-DEVICE-MIB", "sleEthernetPortControlReqResult"))
)
if mibBuilder.loadTexts:
    sleEthernetPortChanged.setStatus(
        "current"
    )

sleEthernetPortLinkChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 2, 3, 2)
)
sleEthernetPortLinkChanged.setObjects(
      *(("SLE-DEVICE-MIB", "sleEthernetPortControlRequest"),
        ("SLE-DEVICE-MIB", "sleEthernetPortControlTimeStamp"),
        ("SLE-DEVICE-MIB", "sleEthernetPortControlReqResult"),
        ("SLE-DEVICE-MIB", "sleEthernetPortControlIndex"),
        ("SLE-DEVICE-MIB", "sleEthernetPortControlLinkCheckTimer"),
        ("SLE-DEVICE-MIB", "sleEthernetPortControlLinkDebounceTime"))
)
if mibBuilder.loadTexts:
    sleEthernetPortLinkChanged.setStatus(
        "current"
    )

sleEthernetPortCpuStatisticsLimitChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 2, 3, 3)
)
sleEthernetPortCpuStatisticsLimitChanged.setObjects(
      *(("SLE-DEVICE-MIB", "sleEthernetPortControlRequest"),
        ("SLE-DEVICE-MIB", "sleEthernetPortControlTimeStamp"),
        ("SLE-DEVICE-MIB", "sleEthernetPortControlReqResult"),
        ("SLE-DEVICE-MIB", "sleEthernetPortControlIndex"),
        ("SLE-DEVICE-MIB", "sleEthernetPortControlCpuStatisticsLimitUnicast"),
        ("SLE-DEVICE-MIB", "sleEthernetPortControlCpuStatisticsLimitMulticast"),
        ("SLE-DEVICE-MIB", "sleEthernetPortControlCpuStatisticsLimitBroadcast"))
)
if mibBuilder.loadTexts:
    sleEthernetPortCpuStatisticsLimitChanged.setStatus(
        "current"
    )

sleEthernetPortFloodBlockStateChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 2, 3, 4)
)
sleEthernetPortFloodBlockStateChanged.setObjects(
      *(("SLE-DEVICE-MIB", "sleEthernetPortControlRequest"),
        ("SLE-DEVICE-MIB", "sleEthernetPortControlTimeStamp"),
        ("SLE-DEVICE-MIB", "sleEthernetPortControlReqResult"),
        ("SLE-DEVICE-MIB", "sleEthernetPortControlIndex"),
        ("SLE-DEVICE-MIB", "sleEthernetPortControlFloodBlockBroadcastState"),
        ("SLE-DEVICE-MIB", "sleEthernetPortControlFloodBlockDlfState"))
)
if mibBuilder.loadTexts:
    sleEthernetPortFloodBlockStateChanged.setStatus(
        "current"
    )

sleEthernetSFPRemoteReset = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 2, 7, 1)
)
sleEthernetSFPRemoteReset.setObjects(
      *(("SLE-DEVICE-MIB", "sleEthernetSFPControlRequest"),
        ("SLE-DEVICE-MIB", "sleEthernetSFPControlTimeStamp"),
        ("SLE-DEVICE-MIB", "sleEthernetSFPControlReqResult"),
        ("SLE-DEVICE-MIB", "sleEthernetSFPControlIndex"))
)
if mibBuilder.loadTexts:
    sleEthernetSFPRemoteReset.setStatus(
        "current"
    )

sleEthernetSFPDdmState = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 2, 7, 2)
)
sleEthernetSFPDdmState.setObjects(
      *(("SLE-DEVICE-MIB", "sleEthernetSFPControlRequest"),
        ("SLE-DEVICE-MIB", "sleEthernetSFPControlTimeStamp"),
        ("SLE-DEVICE-MIB", "sleEthernetSFPControlReqResult"),
        ("SLE-DEVICE-MIB", "sleEthernetSFPControlIndex"),
        ("SLE-DEVICE-MIB", "sleEthernetSfpControlDdmState"))
)
if mibBuilder.loadTexts:
    sleEthernetSFPDdmState.setStatus(
        "current"
    )

sleEthernetSFPThresholdSfpChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 2, 10, 1)
)
sleEthernetSFPThresholdSfpChanged.setObjects(
      *(("SLE-DEVICE-MIB", "sleEthernetSFPThresholdControlRequest"),
        ("SLE-DEVICE-MIB", "sleEthernetSFPThresholdControlTimeStamp"),
        ("SLE-DEVICE-MIB", "sleEthernetSFPThresholdControlReqResult"),
        ("SLE-DEVICE-MIB", "sleEthernetSFPThresholdControlIfIndex"),
        ("SLE-DEVICE-MIB", "sleEthernetSFPThresholdControlType"),
        ("SLE-DEVICE-MIB", "sleEthernetSFPThresholdControlSfpLow"),
        ("SLE-DEVICE-MIB", "sleEthernetSFPThresholdControlSfpHigh"))
)
if mibBuilder.loadTexts:
    sleEthernetSFPThresholdSfpChanged.setStatus(
        "current"
    )

sleEthernetSFPThresholdSystemChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 2, 10, 2)
)
sleEthernetSFPThresholdSystemChanged.setObjects(
      *(("SLE-DEVICE-MIB", "sleEthernetSFPThresholdControlRequest"),
        ("SLE-DEVICE-MIB", "sleEthernetSFPThresholdControlTimeStamp"),
        ("SLE-DEVICE-MIB", "sleEthernetSFPThresholdControlReqResult"),
        ("SLE-DEVICE-MIB", "sleEthernetSFPThresholdControlIfIndex"),
        ("SLE-DEVICE-MIB", "sleEthernetSFPThresholdControlType"),
        ("SLE-DEVICE-MIB", "sleEthernetSFPThresholdControlSystemLow"),
        ("SLE-DEVICE-MIB", "sleEthernetSFPThresholdControlSystemHigh"))
)
if mibBuilder.loadTexts:
    sleEthernetSFPThresholdSystemChanged.setStatus(
        "current"
    )

sleEthernetSFPThresholdDestroyed = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 2, 10, 3)
)
sleEthernetSFPThresholdDestroyed.setObjects(
      *(("SLE-DEVICE-MIB", "sleEthernetSFPThresholdControlRequest"),
        ("SLE-DEVICE-MIB", "sleEthernetSFPThresholdControlTimeStamp"),
        ("SLE-DEVICE-MIB", "sleEthernetSFPThresholdControlReqResult"),
        ("SLE-DEVICE-MIB", "sleEthernetSFPThresholdControlIfIndex"),
        ("SLE-DEVICE-MIB", "sleEthernetSFPThresholdControlType"))
)
if mibBuilder.loadTexts:
    sleEthernetSFPThresholdDestroyed.setStatus(
        "current"
    )

sleFanAdminStateChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 4, 3, 1)
)
sleFanAdminStateChanged.setObjects(
      *(("SLE-DEVICE-MIB", "sleFanModuleAdminState"),
        ("SLE-DEVICE-MIB", "sleFanModuleControlRequest"),
        ("SLE-DEVICE-MIB", "sleFanModuleControlTimeStamp"),
        ("SLE-DEVICE-MIB", "sleFanModuleControlReqResult"))
)
if mibBuilder.loadTexts:
    sleFanAdminStateChanged.setStatus(
        "current"
    )

sleFanSpeedThresholdChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 4, 3, 2)
)
sleFanSpeedThresholdChanged.setObjects(
      *(("SLE-DEVICE-MIB", "sleFanModuleControlRequest"),
        ("SLE-DEVICE-MIB", "sleFanModuleControlTimeStamp"),
        ("SLE-DEVICE-MIB", "sleFanModuleControlReqResult"),
        ("SLE-DEVICE-MIB", "sleFanModuleControlIndex"),
        ("SLE-DEVICE-MIB", "sleFanModuleControlSpeedThreshold"))
)
if mibBuilder.loadTexts:
    sleFanSpeedThresholdChanged.setStatus(
        "current"
    )

sleTemperatureThresholdChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 6, 3, 1)
)
sleTemperatureThresholdChanged.setObjects(
      *(("SLE-DEVICE-MIB", "sleTemperatureControlRequest"),
        ("SLE-DEVICE-MIB", "sleTemperatureControlTimeStamp"),
        ("SLE-DEVICE-MIB", "sleTemperatureControlReqResult"),
        ("SLE-DEVICE-MIB", "sleTemperatureIndex"),
        ("SLE-DEVICE-MIB", "sleTemperatureWarnHighThreshold"),
        ("SLE-DEVICE-MIB", "sleTemperatureWarnLowThreshold"),
        ("SLE-DEVICE-MIB", "sleTemperatureWarnDuration"),
        ("SLE-DEVICE-MIB", "sleTemperatureAlarmHighThreshold"),
        ("SLE-DEVICE-MIB", "sleTemperatureAlarmLowThreshold"),
        ("SLE-DEVICE-MIB", "sleTemperatureLowThreshold"),
        ("SLE-DEVICE-MIB", "sleTemperatureAlarmDuration"),
        ("SLE-DEVICE-MIB", "sleTemperatureHighThreshold"))
)
if mibBuilder.loadTexts:
    sleTemperatureThresholdChanged.setStatus(
        "current"
    )

sleBatteryForceChargeChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 7, 3, 1)
)
sleBatteryForceChargeChanged.setObjects(
      *(("SLE-DEVICE-MIB", "sleBatteryControlRequest"),
        ("SLE-DEVICE-MIB", "sleBatteryControlTimeStamp"),
        ("SLE-DEVICE-MIB", "sleBatteryControlReqResult"))
)
if mibBuilder.loadTexts:
    sleBatteryForceChargeChanged.setStatus(
        "current"
    )

sleBatteryChargingStartChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 7, 3, 2)
)
sleBatteryChargingStartChanged.setObjects(
      *(("SLE-DEVICE-MIB", "sleBatteryControlRequest"),
        ("SLE-DEVICE-MIB", "sleBatteryControlTimeStamp"),
        ("SLE-DEVICE-MIB", "sleBatteryControlReqResult"))
)
if mibBuilder.loadTexts:
    sleBatteryChargingStartChanged.setStatus(
        "current"
    )

sleBatteryForceChargeNonStopChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 7, 3, 3)
)
sleBatteryForceChargeNonStopChanged.setObjects(
      *(("SLE-DEVICE-MIB", "sleBatteryControlRequest"),
        ("SLE-DEVICE-MIB", "sleBatteryControlTimeStamp"),
        ("SLE-DEVICE-MIB", "sleBatteryControlReqResult"))
)
if mibBuilder.loadTexts:
    sleBatteryForceChargeNonStopChanged.setStatus(
        "current"
    )

sleBatteryRBUBTStatusChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 7, 3, 4)
)
sleBatteryRBUBTStatusChanged.setObjects(
      *(("SLE-DEVICE-MIB", "sleBatteryControlRequest"),
        ("SLE-DEVICE-MIB", "sleBatteryControlTimeStamp"),
        ("SLE-DEVICE-MIB", "sleBatteryControlReqResult"),
        ("SLE-DEVICE-MIB", "sleRBUBTStatus"))
)
if mibBuilder.loadTexts:
    sleBatteryRBUBTStatusChanged.setStatus(
        "current"
    )

sleBatteryRBUBTThresholdChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 7, 3, 5)
)
sleBatteryRBUBTThresholdChanged.setObjects(
      *(("SLE-DEVICE-MIB", "sleBatteryControlRequest"),
        ("SLE-DEVICE-MIB", "sleBatteryControlTimeStamp"),
        ("SLE-DEVICE-MIB", "sleBatteryControlReqResult"),
        ("SLE-DEVICE-MIB", "sleRBUBTThreshold"))
)
if mibBuilder.loadTexts:
    sleBatteryRBUBTThresholdChanged.setStatus(
        "current"
    )

sleBatteryRBURechargeVoltageChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 7, 3, 6)
)
sleBatteryRBURechargeVoltageChanged.setObjects(
      *(("SLE-DEVICE-MIB", "sleBatteryControlRequest"),
        ("SLE-DEVICE-MIB", "sleBatteryControlTimeStamp"),
        ("SLE-DEVICE-MIB", "sleBatteryControlReqResult"),
        ("SLE-DEVICE-MIB", "sleRBURechargeVoltage"))
)
if mibBuilder.loadTexts:
    sleBatteryRBURechargeVoltageChanged.setStatus(
        "current"
    )

sleBatteryPsuAcTemperThreshChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 7, 3, 7)
)
sleBatteryPsuAcTemperThreshChanged.setObjects(
      *(("SLE-DEVICE-MIB", "sleBatteryControlRequest"),
        ("SLE-DEVICE-MIB", "sleBatteryControlTimeStamp"),
        ("SLE-DEVICE-MIB", "sleBatteryControlReqResult"),
        ("SLE-DEVICE-MIB", "slePSUTempThreshold"))
)
if mibBuilder.loadTexts:
    sleBatteryPsuAcTemperThreshChanged.setStatus(
        "current"
    )

sleBatteryRBUTemperThreshChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 7, 3, 8)
)
sleBatteryRBUTemperThreshChanged.setObjects(
      *(("SLE-DEVICE-MIB", "sleBatteryControlRequest"),
        ("SLE-DEVICE-MIB", "sleBatteryControlTimeStamp"),
        ("SLE-DEVICE-MIB", "sleBatteryControlReqResult"),
        ("SLE-DEVICE-MIB", "sleRBUTempLowThreshold"),
        ("SLE-DEVICE-MIB", "sleRBUTempHighThreshold"))
)
if mibBuilder.loadTexts:
    sleBatteryRBUTemperThreshChanged.setStatus(
        "current"
    )

sleBatteryBackupProfileChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 7, 6, 1)
)
sleBatteryBackupProfileChanged.setObjects(
      *(("SLE-DEVICE-MIB", "sleBatteryBackupControlRequest"),
        ("SLE-DEVICE-MIB", "sleBatteryBackupControlTimeStamp"),
        ("SLE-DEVICE-MIB", "sleBatteryBackupControlReqResult"),
        ("SLE-DEVICE-MIB", "sleBatteryBackupControlServerIP"),
        ("SLE-DEVICE-MIB", "sleBatteryBackupControlUserID"),
        ("SLE-DEVICE-MIB", "sleBatteryBackupControlPassword"),
        ("SLE-DEVICE-MIB", "sleBatteryBackupControlFlag"),
        ("SLE-DEVICE-MIB", "sleBatteryBackupControlLocalFile"),
        ("SLE-DEVICE-MIB", "sleBatteryBackupControlRemoteFile"))
)
if mibBuilder.loadTexts:
    sleBatteryBackupProfileChanged.setStatus(
        "current"
    )

sleBatteryBackupUpgraded = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 7, 6, 2)
)
sleBatteryBackupUpgraded.setObjects(
      *(("SLE-DEVICE-MIB", "sleBatteryBackupControlRequest"),
        ("SLE-DEVICE-MIB", "sleBatteryBackupControlTimeStamp"),
        ("SLE-DEVICE-MIB", "sleBatteryBackupControlReqResult"),
        ("SLE-DEVICE-MIB", "sleBatteryBackupControlLocalFile"))
)
if mibBuilder.loadTexts:
    sleBatteryBackupUpgraded.setStatus(
        "current"
    )

sleBatteryBackupTableCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 7, 6, 3)
)
sleBatteryBackupTableCleared.setObjects(
      *(("SLE-DEVICE-MIB", "sleBatteryBackupControlRequest"),
        ("SLE-DEVICE-MIB", "sleBatteryBackupControlTimeStamp"),
        ("SLE-DEVICE-MIB", "sleBatteryBackupControlReqResult"),
        ("SLE-DEVICE-MIB", "sleBatteryBackupControlLocalFile"))
)
if mibBuilder.loadTexts:
    sleBatteryBackupTableCleared.setStatus(
        "current"
    )

sleSlotSystemRestart = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 11, 1, 3, 1)
)
sleSlotSystemRestart.setObjects(
      *(("SLE-DEVICE-MIB", "sleSlotSystemControlRequest"),
        ("SLE-DEVICE-MIB", "sleSlotSystemControlTimeStamp"),
        ("SLE-DEVICE-MIB", "sleSlotSystemControlReqResult"),
        ("SLE-DEVICE-MIB", "sleSlotSystemControlSlotIndex"))
)
if mibBuilder.loadTexts:
    sleSlotSystemRestart.setStatus(
        "current"
    )

sleSlotSystemCPULoadChagned = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 11, 1, 3, 2)
)
sleSlotSystemCPULoadChagned.setObjects(
      *(("SLE-DEVICE-MIB", "sleSlotSystemControlRequest"),
        ("SLE-DEVICE-MIB", "sleSlotSystemControlTimeStamp"),
        ("SLE-DEVICE-MIB", "sleSlotSystemControlReqResult"),
        ("SLE-DEVICE-MIB", "sleSlotSystemControlSlotIndex"),
        ("SLE-DEVICE-MIB", "sleSlotSystemControlCPULoadHighThreshold"),
        ("SLE-DEVICE-MIB", "sleSlotSystemControlCPULoadHighThresholdTimer"),
        ("SLE-DEVICE-MIB", "sleSlotSystemControlCPULoadLowThreshold"),
        ("SLE-DEVICE-MIB", "sleSlotSystemControlCPULoadLowThresholdTimer"))
)
if mibBuilder.loadTexts:
    sleSlotSystemCPULoadChagned.setStatus(
        "current"
    )

sleSlotSystemCPULoadDeleted = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 11, 1, 3, 3)
)
sleSlotSystemCPULoadDeleted.setObjects(
      *(("SLE-DEVICE-MIB", "sleSlotSystemControlRequest"),
        ("SLE-DEVICE-MIB", "sleSlotSystemControlTimeStamp"),
        ("SLE-DEVICE-MIB", "sleSlotSystemControlReqResult"),
        ("SLE-DEVICE-MIB", "sleSlotSystemControlSlotIndex"))
)
if mibBuilder.loadTexts:
    sleSlotSystemCPULoadDeleted.setStatus(
        "current"
    )

sleSlotStatusLocked = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 11, 2, 3, 1)
)
sleSlotStatusLocked.setObjects(
      *(("SLE-DEVICE-MIB", "sleSlotStatusControlRequest"),
        ("SLE-DEVICE-MIB", "sleSlotStatusControlTimeStamp"),
        ("SLE-DEVICE-MIB", "sleSlotStatusControlReqResult"),
        ("SLE-DEVICE-MIB", "sleSlotStatusControlSlotIndex"))
)
if mibBuilder.loadTexts:
    sleSlotStatusLocked.setStatus(
        "current"
    )

sleSlotStatusUnlocked = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 11, 2, 3, 2)
)
sleSlotStatusUnlocked.setObjects(
      *(("SLE-DEVICE-MIB", "sleSlotStatusControlRequest"),
        ("SLE-DEVICE-MIB", "sleSlotStatusControlTimeStamp"),
        ("SLE-DEVICE-MIB", "sleSlotStatusControlReqResult"),
        ("SLE-DEVICE-MIB", "sleSlotStatusControlSlotIndex"))
)
if mibBuilder.loadTexts:
    sleSlotStatusUnlocked.setStatus(
        "current"
    )

sleSlotStatusPlanning = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 11, 2, 3, 3)
)
sleSlotStatusPlanning.setObjects(
      *(("SLE-DEVICE-MIB", "sleSlotStatusControlRequest"),
        ("SLE-DEVICE-MIB", "sleSlotStatusControlTimeStamp"),
        ("SLE-DEVICE-MIB", "sleSlotStatusControlReqResult"),
        ("SLE-DEVICE-MIB", "sleSlotStatusControlSlotIndex"),
        ("SLE-DEVICE-MIB", "sleSlotStatusControlPlanCardType"))
)
if mibBuilder.loadTexts:
    sleSlotStatusPlanning.setStatus(
        "current"
    )

sleSlotStatusNoPlanning = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 11, 2, 3, 4)
)
sleSlotStatusNoPlanning.setObjects(
      *(("SLE-DEVICE-MIB", "sleSlotStatusControlRequest"),
        ("SLE-DEVICE-MIB", "sleSlotStatusControlTimeStamp"),
        ("SLE-DEVICE-MIB", "sleSlotStatusControlReqResult"),
        ("SLE-DEVICE-MIB", "sleSlotStatusControlSlotIndex"))
)
if mibBuilder.loadTexts:
    sleSlotStatusNoPlanning.setStatus(
        "current"
    )

sleSlotStatusUpgradeModeChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 11, 2, 3, 5)
)
sleSlotStatusUpgradeModeChanged.setObjects(
      *(("SLE-DEVICE-MIB", "sleSlotStatusControlRequest"),
        ("SLE-DEVICE-MIB", "sleSlotStatusControlTimeStamp"),
        ("SLE-DEVICE-MIB", "sleSlotStatusControlReqResult"),
        ("SLE-DEVICE-MIB", "sleSlotStatusControlSlotIndex"),
        ("SLE-DEVICE-MIB", "sleSlotStatusControlUpgradeMode"))
)
if mibBuilder.loadTexts:
    sleSlotStatusUpgradeModeChanged.setStatus(
        "current"
    )

sleSlotStatusPowerUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 11, 2, 3, 6)
)
sleSlotStatusPowerUp.setObjects(
      *(("SLE-DEVICE-MIB", "sleSlotStatusControlRequest"),
        ("SLE-DEVICE-MIB", "sleSlotStatusControlTimeStamp"),
        ("SLE-DEVICE-MIB", "sleSlotStatusControlReqResult"),
        ("SLE-DEVICE-MIB", "sleSlotStatusControlSlotIndex"))
)
if mibBuilder.loadTexts:
    sleSlotStatusPowerUp.setStatus(
        "current"
    )

sleSlotStatusPowerDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 11, 2, 3, 7)
)
sleSlotStatusPowerDown.setObjects(
      *(("SLE-DEVICE-MIB", "sleSlotStatusControlRequest"),
        ("SLE-DEVICE-MIB", "sleSlotStatusControlTimeStamp"),
        ("SLE-DEVICE-MIB", "sleSlotStatusControlReqResult"),
        ("SLE-DEVICE-MIB", "sleSlotStatusControlSlotIndex"))
)
if mibBuilder.loadTexts:
    sleSlotStatusPowerDown.setStatus(
        "current"
    )

sleSlotStatusPowerReset = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 11, 2, 3, 8)
)
sleSlotStatusPowerReset.setObjects(
      *(("SLE-DEVICE-MIB", "sleSlotStatusControlRequest"),
        ("SLE-DEVICE-MIB", "sleSlotStatusControlTimeStamp"),
        ("SLE-DEVICE-MIB", "sleSlotStatusControlReqResult"),
        ("SLE-DEVICE-MIB", "sleSlotStatusControlSlotIndex"))
)
if mibBuilder.loadTexts:
    sleSlotStatusPowerReset.setStatus(
        "current"
    )

sleSlotNosUpgrade = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 11, 3, 3, 1)
)
sleSlotNosUpgrade.setObjects(
      *(("SLE-DEVICE-MIB", "sleSlotNosControlRequest"),
        ("SLE-DEVICE-MIB", "sleSlotNosControlTimeStamp"),
        ("SLE-DEVICE-MIB", "sleSlotNosControlReqResult"),
        ("SLE-DEVICE-MIB", "sleSlotNosControlSlotIndex"))
)
if mibBuilder.loadTexts:
    sleSlotNosUpgrade.setStatus(
        "current"
    )

sleSlotNosDownload = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 11, 3, 3, 2)
)
sleSlotNosDownload.setObjects(
      *(("SLE-DEVICE-MIB", "sleSlotNosControlRequest"),
        ("SLE-DEVICE-MIB", "sleSlotNosControlTimeStamp"),
        ("SLE-DEVICE-MIB", "sleSlotNosControlReqResult"),
        ("SLE-DEVICE-MIB", "sleSlotNosControlUpDownMethod"),
        ("SLE-DEVICE-MIB", "sleSlotNosControlUpDownFlag"),
        ("SLE-DEVICE-MIB", "sleSlotNosControlServerAddress"),
        ("SLE-DEVICE-MIB", "sleSlotNosControlUserID"),
        ("SLE-DEVICE-MIB", "sleSlotNosControlPassword"),
        ("SLE-DEVICE-MIB", "sleSlotNosControlFileName"))
)
if mibBuilder.loadTexts:
    sleSlotNosDownload.setStatus(
        "current"
    )

sleSlotNosBootloaderUpgrade = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 11, 3, 3, 3)
)
sleSlotNosBootloaderUpgrade.setObjects(
      *(("SLE-DEVICE-MIB", "sleSlotNosControlRequest"),
        ("SLE-DEVICE-MIB", "sleSlotNosControlTimeStamp"),
        ("SLE-DEVICE-MIB", "sleSlotNosControlReqResult"),
        ("SLE-DEVICE-MIB", "sleSlotNosControlSlotIndex"),
        ("SLE-DEVICE-MIB", "sleSlotNosControlServerAddress"),
        ("SLE-DEVICE-MIB", "sleSlotNosControlUserID"),
        ("SLE-DEVICE-MIB", "sleSlotNosControlPassword"),
        ("SLE-DEVICE-MIB", "sleSlotNosControlFileName"))
)
if mibBuilder.loadTexts:
    sleSlotNosBootloaderUpgrade.setStatus(
        "current"
    )

sleSlotProtectionSystemStatusChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 11, 7, 1, 3, 1)
)
sleSlotProtectionSystemStatusChanged.setObjects(
      *(("SLE-DEVICE-MIB", "sleSlotProtectionControlRequest"),
        ("SLE-DEVICE-MIB", "sleSlotProtectionControlTimeStamp"),
        ("SLE-DEVICE-MIB", "sleSlotProtectionControlReqResult"),
        ("SLE-DEVICE-MIB", "sleSlotProtectionControlSystemStatus"))
)
if mibBuilder.loadTexts:
    sleSlotProtectionSystemStatusChanged.setStatus(
        "current"
    )

sleSlotProtectionSystemThreshChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 11, 7, 1, 3, 2)
)
sleSlotProtectionSystemThreshChanged.setObjects(
      *(("SLE-DEVICE-MIB", "sleSlotProtectionControlRequest"),
        ("SLE-DEVICE-MIB", "sleSlotProtectionControlTimeStamp"),
        ("SLE-DEVICE-MIB", "sleSlotProtectionControlReqResult"),
        ("SLE-DEVICE-MIB", "sleSlotProtectionControlSystemThreshold"))
)
if mibBuilder.loadTexts:
    sleSlotProtectionSystemThreshChanged.setStatus(
        "current"
    )

sleSlotProtectionIUPowerStatusChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 11, 7, 1, 3, 3)
)
sleSlotProtectionIUPowerStatusChanged.setObjects(
      *(("SLE-DEVICE-MIB", "sleSlotProtectionControlRequest"),
        ("SLE-DEVICE-MIB", "sleSlotProtectionControlTimeStamp"),
        ("SLE-DEVICE-MIB", "sleSlotProtectionControlReqResult"),
        ("SLE-DEVICE-MIB", "sleSlotProtectionControlIUPowerStatus"))
)
if mibBuilder.loadTexts:
    sleSlotProtectionIUPowerStatusChanged.setStatus(
        "current"
    )

sleSlotProtectionIUTemperThreshChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 11, 7, 2, 3, 1)
)
sleSlotProtectionIUTemperThreshChanged.setObjects(
      *(("SLE-DEVICE-MIB", "sleSlotProtectionIUControlRequest"),
        ("SLE-DEVICE-MIB", "sleSlotProtectionIUControlTimeStamp"),
        ("SLE-DEVICE-MIB", "sleSlotProtectionIUControlReqResult"),
        ("SLE-DEVICE-MIB", "sleSlotProtectionIUControlTemperHighThresh"),
        ("SLE-DEVICE-MIB", "sleSlotProtectionIUControlTemperLowThresh"),
        ("SLE-DEVICE-MIB", "sleSlotProtectionIUControlindex"))
)
if mibBuilder.loadTexts:
    sleSlotProtectionIUTemperThreshChanged.setStatus(
        "current"
    )

sleSlotProtectionIUPowerThreshChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 11, 7, 2, 3, 2)
)
sleSlotProtectionIUPowerThreshChanged.setObjects(
      *(("SLE-DEVICE-MIB", "sleSlotProtectionIUControlRequest"),
        ("SLE-DEVICE-MIB", "sleSlotProtectionIUControlTimeStamp"),
        ("SLE-DEVICE-MIB", "sleSlotProtectionIUControlReqResult"),
        ("SLE-DEVICE-MIB", "sleSlotProtectionIUControlindex"),
        ("SLE-DEVICE-MIB", "sleSlotProtectionIUControlPowerThresh"))
)
if mibBuilder.loadTexts:
    sleSlotProtectionIUPowerThreshChanged.setStatus(
        "current"
    )

sleRFBaseEthertypeChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 12, 3, 1)
)
sleRFBaseEthertypeChanged.setObjects(
      *(("SLE-DEVICE-MIB", "sleRfBaseControlRequest"),
        ("SLE-DEVICE-MIB", "sleRfBaseControlTimeStamp"),
        ("SLE-DEVICE-MIB", "sleRfBaseControlReqResult"),
        ("SLE-DEVICE-MIB", "sleRfBaseControlRfEthertype"))
)
if mibBuilder.loadTexts:
    sleRFBaseEthertypeChanged.setStatus(
        "current"
    )

sleRFBaseEthertypeResetChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 12, 3, 2)
)
sleRFBaseEthertypeResetChanged.setObjects(
      *(("SLE-DEVICE-MIB", "sleRfBaseControlRequest"),
        ("SLE-DEVICE-MIB", "sleRfBaseControlTimeStamp"),
        ("SLE-DEVICE-MIB", "sleRfBaseControlReqResult"),
        ("SLE-DEVICE-MIB", "sleRfBaseControlRfEthertype"))
)
if mibBuilder.loadTexts:
    sleRFBaseEthertypeResetChanged.setStatus(
        "current"
    )

sleRfPortStatusChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 12, 6, 1)
)
sleRfPortStatusChanged.setObjects(
      *(("SLE-DEVICE-MIB", "sleRfPortControlRequest"),
        ("SLE-DEVICE-MIB", "sleRfPortControlTimeStamp"),
        ("SLE-DEVICE-MIB", "sleRfPortControlReqResult"),
        ("SLE-DEVICE-MIB", "sleRfPortControlIndex"),
        ("SLE-DEVICE-MIB", "sleRfPortControlAdminStatus"))
)
if mibBuilder.loadTexts:
    sleRfPortStatusChanged.setStatus(
        "current"
    )

sleEMChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 13, 3, 1)
)
sleEMChanged.setObjects(
      *(("SLE-DEVICE-MIB", "sleEMControlRequest"),
        ("SLE-DEVICE-MIB", "sleEMControlTimeStamp"),
        ("SLE-DEVICE-MIB", "sleEMControlReqResult"),
        ("SLE-DEVICE-MIB", "sleEMControlInputIndex"),
        ("SLE-DEVICE-MIB", "sleEMControlAlarmString"),
        ("SLE-DEVICE-MIB", "sleEMControlAlarmSeverity"),
        ("SLE-DEVICE-MIB", "sleEMControlmode"))
)
if mibBuilder.loadTexts:
    sleEMChanged.setStatus(
        "current"
    )

sleEMDeleted = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 13, 3, 2)
)
sleEMDeleted.setObjects(
      *(("SLE-DEVICE-MIB", "sleEMControlRequest"),
        ("SLE-DEVICE-MIB", "sleEMControlTimeStamp"),
        ("SLE-DEVICE-MIB", "sleEMControlReqResult"),
        ("SLE-DEVICE-MIB", "sleEMControlInputIndex"))
)
if mibBuilder.loadTexts:
    sleEMDeleted.setStatus(
        "current"
    )

sleBypassModeChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 14, 1, 3, 1)
)
sleBypassModeChanged.setObjects(
      *(("SLE-DEVICE-MIB", "sleBypassBaseControlRequest"),
        ("SLE-DEVICE-MIB", "sleBypassBaseControlTimeStamp"),
        ("SLE-DEVICE-MIB", "sleBypassBaseControlReqResult"),
        ("SLE-DEVICE-MIB", "sleBypassBaseControlMode"))
)
if mibBuilder.loadTexts:
    sleBypassModeChanged.setStatus(
        "current"
    )

sleBypassOptionConnectivitySet = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 14, 2, 3, 1)
)
sleBypassOptionConnectivitySet.setObjects(
      *(("SLE-DEVICE-MIB", "sleBypassOptionConnectivityControlRequest"),
        ("SLE-DEVICE-MIB", "sleBypassOptionConnectivityControlTimeStamp"),
        ("SLE-DEVICE-MIB", "sleBypassOptionConnectivityControlReqResult"),
        ("SLE-DEVICE-MIB", "sleBypassOptionConnectivityControlAddress"),
        ("SLE-DEVICE-MIB", "sleBypassOptionConnectivityControlPort"))
)
if mibBuilder.loadTexts:
    sleBypassOptionConnectivitySet.setStatus(
        "current"
    )

sleBypassOptionConnectivityUnset = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 14, 2, 3, 2)
)
sleBypassOptionConnectivityUnset.setObjects(
      *(("SLE-DEVICE-MIB", "sleBypassOptionConnectivityControlRequest"),
        ("SLE-DEVICE-MIB", "sleBypassOptionConnectivityControlTimeStamp"),
        ("SLE-DEVICE-MIB", "sleBypassOptionConnectivityControlReqResult"),
        ("SLE-DEVICE-MIB", "sleBypassOptionConnectivityControlAddress"),
        ("SLE-DEVICE-MIB", "sleBypassOptionConnectivityControlPort"))
)
if mibBuilder.loadTexts:
    sleBypassOptionConnectivityUnset.setStatus(
        "current"
    )

sleBypassOptionPingSet = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 14, 2, 6, 1)
)
sleBypassOptionPingSet.setObjects(
      *(("SLE-DEVICE-MIB", "sleBypassOptionPingControlRequest"),
        ("SLE-DEVICE-MIB", "sleBypassOptionPingControlTimeStamp"),
        ("SLE-DEVICE-MIB", "sleBypassOptionPingControlReqResult"),
        ("SLE-DEVICE-MIB", "sleBypassOptionPingControlTranNumber"),
        ("SLE-DEVICE-MIB", "sleBypassOptionPingControlReqInterval"),
        ("SLE-DEVICE-MIB", "sleBypassOptionPingControlReqTimeout"),
        ("SLE-DEVICE-MIB", "sleBypassOptionPingControlLossThresh"),
        ("SLE-DEVICE-MIB", "sleBypassOptionPingControlAddress"),
        ("SLE-DEVICE-MIB", "sleBypassOptionPingControlTransInterval"))
)
if mibBuilder.loadTexts:
    sleBypassOptionPingSet.setStatus(
        "current"
    )

sleBypassOptionPingUnset = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 14, 2, 6, 2)
)
sleBypassOptionPingUnset.setObjects(
      *(("SLE-DEVICE-MIB", "sleBypassOptionPingControlRequest"),
        ("SLE-DEVICE-MIB", "sleBypassOptionPingControlTimeStamp"),
        ("SLE-DEVICE-MIB", "sleBypassOptionPingControlReqResult"),
        ("SLE-DEVICE-MIB", "sleBypassOptionPingControlAddress"))
)
if mibBuilder.loadTexts:
    sleBypassOptionPingUnset.setStatus(
        "current"
    )

sleBypassOptionLinkMonitorChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 14, 2, 9, 1)
)
sleBypassOptionLinkMonitorChanged.setObjects(
      *(("SLE-DEVICE-MIB", "sleBypassOptionLinkMonitorControlRequest"),
        ("SLE-DEVICE-MIB", "sleBypassOptionLinkMonitorControlStatus"),
        ("SLE-DEVICE-MIB", "sleBypassOptionLinkMonitorControlTimeStamp"),
        ("SLE-DEVICE-MIB", "sleBypassOptionLinkMonitorControlReqResult"),
        ("SLE-DEVICE-MIB", "sleBypassOptionLinkMonitorControlPort"),
        ("SLE-DEVICE-MIB", "sleBypassOptionLinkMonitorControlPortStatus"))
)
if mibBuilder.loadTexts:
    sleBypassOptionLinkMonitorChanged.setStatus(
        "current"
    )

sleHFCOpticAlarmStatusChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 15, 3, 1)
)
sleHFCOpticAlarmStatusChanged.setObjects(
      *(("SLE-DEVICE-MIB", "sleHFCControlRequest"),
        ("SLE-DEVICE-MIB", "sleHFCControlTimeStamp"),
        ("SLE-DEVICE-MIB", "sleHFCControlReqResult"),
        ("SLE-DEVICE-MIB", "sleHFCControlAlarmIndex"),
        ("SLE-DEVICE-MIB", "sleHFCControlAlarmStatus"))
)
if mibBuilder.loadTexts:
    sleHFCOpticAlarmStatusChanged.setStatus(
        "current"
    )


# Notifications groups

sleDeviceNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6296, 101, 2, 17)
)
sleDeviceNotificationGroup.setObjects(
      *(("SLE-DEVICE-MIB", "sleDeviceTemperatureThresholdChanged"),
        ("SLE-DEVICE-MIB", "sleEthernetPortChanged"),
        ("SLE-DEVICE-MIB", "sleFanAdminStateChanged"),
        ("SLE-DEVICE-MIB", "sleBatteryBackupProfileChanged"),
        ("SLE-DEVICE-MIB", "sleBatteryBackupUpgraded"),
        ("SLE-DEVICE-MIB", "sleSlotSystemRestart"),
        ("SLE-DEVICE-MIB", "sleSlotStatusLocked"),
        ("SLE-DEVICE-MIB", "sleSlotStatusUnlocked"),
        ("SLE-DEVICE-MIB", "sleSlotStatusPlanning"),
        ("SLE-DEVICE-MIB", "sleSlotStatusNoPlanning"),
        ("SLE-DEVICE-MIB", "sleSlotStatusUpgradeModeChanged"),
        ("SLE-DEVICE-MIB", "sleSlotNosUpgrade"),
        ("SLE-DEVICE-MIB", "sleSlotStatusPowerUp"),
        ("SLE-DEVICE-MIB", "sleSlotStatusPowerDown"),
        ("SLE-DEVICE-MIB", "sleSlotStatusPowerReset"),
        ("SLE-DEVICE-MIB", "sleSlotNosDownload"),
        ("SLE-DEVICE-MIB", "sleSlotNosBootloaderUpgrade"),
        ("SLE-DEVICE-MIB", "sleFanSpeedThresholdChanged"),
        ("SLE-DEVICE-MIB", "sleDeviceJumboFrameChanged"),
        ("SLE-DEVICE-MIB", "sleTemperatureThresholdChanged"),
        ("SLE-DEVICE-MIB", "sleDeviceLEDTestChanged"),
        ("SLE-DEVICE-MIB", "sleEthernetSFPRemoteReset"),
        ("SLE-DEVICE-MIB", "sleRfPortStatusChanged"),
        ("SLE-DEVICE-MIB", "sleDeviceEnvironmentMonitoringStatusChanged"),
        ("SLE-DEVICE-MIB", "sleEMChanged"),
        ("SLE-DEVICE-MIB", "sleEMDeleted"),
        ("SLE-DEVICE-MIB", "sleRFBaseEthertypeChanged"),
        ("SLE-DEVICE-MIB", "sleRFBaseEthertypeResetChanged"),
        ("SLE-DEVICE-MIB", "sleBypassModeChanged"),
        ("SLE-DEVICE-MIB", "sleBypassOptionConnectivitySet"),
        ("SLE-DEVICE-MIB", "sleBypassOptionConnectivityUnset"),
        ("SLE-DEVICE-MIB", "sleBypassOptionPingSet"),
        ("SLE-DEVICE-MIB", "sleBypassOptionPingUnset"),
        ("SLE-DEVICE-MIB", "sleBypassOptionLinkMonitorChanged"),
        ("SLE-DEVICE-MIB", "sleSlotProtectionSystemStatusChanged"),
        ("SLE-DEVICE-MIB", "sleSlotProtectionSystemThreshChanged"),
        ("SLE-DEVICE-MIB", "sleSlotProtectionIUTemperThreshChanged"),
        ("SLE-DEVICE-MIB", "sleSlotProtectionIUPowerThreshChanged"),
        ("SLE-DEVICE-MIB", "sleSlotProtectionIUPowerStatusChanged"),
        ("SLE-DEVICE-MIB", "sleHFCOpticAlarmStatusChanged"),
        ("SLE-DEVICE-MIB", "sleSlotSystemCPULoadChagned"),
        ("SLE-DEVICE-MIB", "sleSlotSystemCPULoadDeleted"),
        ("SLE-DEVICE-MIB", "sleEthernetPortLinkChanged"),
        ("SLE-DEVICE-MIB", "sleEthernetPortCpuStatisticsLimitChanged"),
        ("SLE-DEVICE-MIB", "sleEthernetPortFloodBlockStateChanged"),
        ("SLE-DEVICE-MIB", "sleEthernetSFPDdmState"),
        ("SLE-DEVICE-MIB", "sleEthernetSFPThresholdSfpChanged"),
        ("SLE-DEVICE-MIB", "sleEthernetSFPThresholdSystemChanged"),
        ("SLE-DEVICE-MIB", "sleEthernetSFPThresholdDestroyed"),
        ("SLE-DEVICE-MIB", "sleBatteryBackupTableCleared"),
        ("SLE-DEVICE-MIB", "sleBatteryForceChargeChanged"),
        ("SLE-DEVICE-MIB", "sleBatteryChargingStartChanged"),
        ("SLE-DEVICE-MIB", "sleBatteryForceChargeNonStopChanged"),
        ("SLE-DEVICE-MIB", "sleBatteryRBUBTStatusChanged"),
        ("SLE-DEVICE-MIB", "sleBatteryRBUBTThresholdChanged"),
        ("SLE-DEVICE-MIB", "sleBatteryRBURechargeVoltageChanged"),
        ("SLE-DEVICE-MIB", "sleBatteryPsuAcTemperThreshChanged"),
        ("SLE-DEVICE-MIB", "sleBatteryRBUTemperThreshChanged"))
)
if mibBuilder.loadTexts:
    sleDeviceNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SLE-DEVICE-MIB",
    **{"sleDevice": sleDevice,
       "sleDeviceBase": sleDeviceBase,
       "sleDeviceBaseInfo": sleDeviceBaseInfo,
       "sleDeviceEthernetPortNum": sleDeviceEthernetPortNum,
       "sleDevicePowerNum": sleDevicePowerNum,
       "sleDeviceFanModuleNum": sleDeviceFanModuleNum,
       "sleDeviceTemperatureNum": sleDeviceTemperatureNum,
       "sleDeviceFanStartTemperature": sleDeviceFanStartTemperature,
       "sleDeviceFanStopTemperature": sleDeviceFanStopTemperature,
       "sleDeviceJumboFrameStatus": sleDeviceJumboFrameStatus,
       "sleDeviceEnvironmentMonitoringStatus": sleDeviceEnvironmentMonitoringStatus,
       "sleDeviceBaseControl": sleDeviceBaseControl,
       "sleDeviceControlRequest": sleDeviceControlRequest,
       "sleDeviceControlStatus": sleDeviceControlStatus,
       "sleDeviceControlTimer": sleDeviceControlTimer,
       "sleDeviceControlTimeStamp": sleDeviceControlTimeStamp,
       "sleDeviceControlReqResult": sleDeviceControlReqResult,
       "sleDeviceControlFanStartTemperature": sleDeviceControlFanStartTemperature,
       "sleDeviceControlFanStopTemperature": sleDeviceControlFanStopTemperature,
       "sleDeviceControlJumboFrameStatus": sleDeviceControlJumboFrameStatus,
       "sleDeviceControlEnvironmentMonitoringStatus": sleDeviceControlEnvironmentMonitoringStatus,
       "sleDeviceBaseNotification": sleDeviceBaseNotification,
       "sleDeviceTemperatureThresholdChanged": sleDeviceTemperatureThresholdChanged,
       "sleDeviceJumboFrameChanged": sleDeviceJumboFrameChanged,
       "sleDeviceLEDTestChanged": sleDeviceLEDTestChanged,
       "sleDeviceEnvironmentMonitoringStatusChanged": sleDeviceEnvironmentMonitoringStatusChanged,
       "sleEthernetPort": sleEthernetPort,
       "sleEthernetPortTable": sleEthernetPortTable,
       "sleEthernetPortEntry": sleEthernetPortEntry,
       "sleEthernetPortIndex": sleEthernetPortIndex,
       "sleEthernetPortPhyIndex": sleEthernetPortPhyIndex,
       "sleEthernetPortType": sleEthernetPortType,
       "sleEthernetPortAdminStatus": sleEthernetPortAdminStatus,
       "sleEthernetPortOperStatus": sleEthernetPortOperStatus,
       "sleEthernetPortTransmissionRate": sleEthernetPortTransmissionRate,
       "sleEthernetPortDuplexMode": sleEthernetPortDuplexMode,
       "sleEthernetPortFlowControl": sleEthernetPortFlowControl,
       "sleEthernetPortNegotiationMode": sleEthernetPortNegotiationMode,
       "sleEthernetPortJumboFrameSize": sleEthernetPortJumboFrameSize,
       "sleEthernetPortSfpTransceiver": sleEthernetPortSfpTransceiver,
       "sleEthernetPortSfpVendorName": sleEthernetPortSfpVendorName,
       "sleEthernetPortSfpVendorPartNumber": sleEthernetPortSfpVendorPartNumber,
       "sleEthernetPortSfpVendorRevision": sleEthernetPortSfpVendorRevision,
       "sleEthernetPortSfpVendorSerialNumber": sleEthernetPortSfpVendorSerialNumber,
       "sleEthernetPortSfpDateCode": sleEthernetPortSfpDateCode,
       "sleEthernetPortPhysicalRemoteChassis": sleEthernetPortPhysicalRemoteChassis,
       "sleEthernetPortPhysicalRemoteSlot": sleEthernetPortPhysicalRemoteSlot,
       "sleEthernetPortPhysicalRemotePort": sleEthernetPortPhysicalRemotePort,
       "sleEthernetPortPhysicalLinkDiscoveryMode": sleEthernetPortPhysicalLinkDiscoveryMode,
       "sleEthernetPortSfpTransceiverType": sleEthernetPortSfpTransceiverType,
       "sleEthernetPortSfpTransceiverDetailType": sleEthernetPortSfpTransceiverDetailType,
       "sleEthernetPortSlotIndex": sleEthernetPortSlotIndex,
       "sleEthernetPortSlotPortIndex": sleEthernetPortSlotPortIndex,
       "sleEthernetPortAdminTransmissionRate": sleEthernetPortAdminTransmissionRate,
       "sleEthernetPortAdminDuplexMode": sleEthernetPortAdminDuplexMode,
       "sleEthernetPortAdminFlowControl": sleEthernetPortAdminFlowControl,
       "sleEthernetPortAdminNegotiationMode": sleEthernetPortAdminNegotiationMode,
       "sleEthernetPortAdminReason": sleEthernetPortAdminReason,
       "sleEthernetPortLinkCheckTimer": sleEthernetPortLinkCheckTimer,
       "sleEthernetPortLinkDebounceTime": sleEthernetPortLinkDebounceTime,
       "sleEthernetPortCpuStatisticsLimitUnicast": sleEthernetPortCpuStatisticsLimitUnicast,
       "sleEthernetPortCpuStatisticsLimitMulticast": sleEthernetPortCpuStatisticsLimitMulticast,
       "sleEthernetPortCpuStatisticsLimitBroadcast": sleEthernetPortCpuStatisticsLimitBroadcast,
       "sleEthernetPortFloodBlockBroadcastState": sleEthernetPortFloodBlockBroadcastState,
       "sleEthernetPortFloodBlockDlfState": sleEthernetPortFloodBlockDlfState,
       "sleEthernetPortControl": sleEthernetPortControl,
       "sleEthernetPortControlRequest": sleEthernetPortControlRequest,
       "sleEthernetPortControlStatus": sleEthernetPortControlStatus,
       "sleEthernetPortControlTimer": sleEthernetPortControlTimer,
       "sleEthernetPortControlTimeStamp": sleEthernetPortControlTimeStamp,
       "sleEthernetPortControlReqResult": sleEthernetPortControlReqResult,
       "sleEthernetPortControlIndex": sleEthernetPortControlIndex,
       "sleEthernetPortControlType": sleEthernetPortControlType,
       "sleEthernetPortControlAdminStatus": sleEthernetPortControlAdminStatus,
       "sleEthernetPortControlTransmissionRate": sleEthernetPortControlTransmissionRate,
       "sleEthernetPortControlDuplexMode": sleEthernetPortControlDuplexMode,
       "sleEthernetPortControlFlowControl": sleEthernetPortControlFlowControl,
       "sleEthernetPortControlNegotiationMode": sleEthernetPortControlNegotiationMode,
       "sleEthernetPortControlJumboFrameSize": sleEthernetPortControlJumboFrameSize,
       "sleEthernetPortControlPhysicalRemoteChassis": sleEthernetPortControlPhysicalRemoteChassis,
       "sleEthernetPortControlPhysicalRemoteSlot": sleEthernetPortControlPhysicalRemoteSlot,
       "sleEthernetPortControlPhysicalRemotePort": sleEthernetPortControlPhysicalRemotePort,
       "sleEthernetPortControlPhysicalLinkDiscoveryMode": sleEthernetPortControlPhysicalLinkDiscoveryMode,
       "sleEthernetPortControlLinkCheckTimer": sleEthernetPortControlLinkCheckTimer,
       "sleEthernetPortControlLinkDebounceTime": sleEthernetPortControlLinkDebounceTime,
       "sleEthernetPortControlCpuStatisticsLimitUnicast": sleEthernetPortControlCpuStatisticsLimitUnicast,
       "sleEthernetPortControlCpuStatisticsLimitMulticast": sleEthernetPortControlCpuStatisticsLimitMulticast,
       "sleEthernetPortControlCpuStatisticsLimitBroadcast": sleEthernetPortControlCpuStatisticsLimitBroadcast,
       "sleEthernetPortControlFloodBlockBroadcastState": sleEthernetPortControlFloodBlockBroadcastState,
       "sleEthernetPortControlFloodBlockDlfState": sleEthernetPortControlFloodBlockDlfState,
       "sleEthernetPortNotification": sleEthernetPortNotification,
       "sleEthernetPortChanged": sleEthernetPortChanged,
       "sleEthernetPortLinkChanged": sleEthernetPortLinkChanged,
       "sleEthernetPortCpuStatisticsLimitChanged": sleEthernetPortCpuStatisticsLimitChanged,
       "sleEthernetPortFloodBlockStateChanged": sleEthernetPortFloodBlockStateChanged,
       "sleEthernetPortDMITable": sleEthernetPortDMITable,
       "sleEthernetPortDMIEntry": sleEthernetPortDMIEntry,
       "sleEthernetPortDMIIndex": sleEthernetPortDMIIndex,
       "sleEthernetPortDMITemper": sleEthernetPortDMITemper,
       "sleEthernetPortDMIVoltage": sleEthernetPortDMIVoltage,
       "sleEthernetPortDMITxBias": sleEthernetPortDMITxBias,
       "sleEthernetPortDMITxPower": sleEthernetPortDMITxPower,
       "sleEthernetPortDMIRxPower": sleEthernetPortDMIRxPower,
       "sleEthernetSFPTable": sleEthernetSFPTable,
       "sleEthernetSFPEntry": sleEthernetSFPEntry,
       "sleEthernetSfpIndex": sleEthernetSfpIndex,
       "sleEthernetSfpTransceiver": sleEthernetSfpTransceiver,
       "sleEthernetSfpVendorName": sleEthernetSfpVendorName,
       "sleEthernetSfpVendorPartNumber": sleEthernetSfpVendorPartNumber,
       "sleEthernetSfpVendorRevision": sleEthernetSfpVendorRevision,
       "sleEthernetSfpVendorSerialNumber": sleEthernetSfpVendorSerialNumber,
       "sleEthernetSfpDateCode": sleEthernetSfpDateCode,
       "sleEthernetSfpTransceiverType": sleEthernetSfpTransceiverType,
       "sleEthernetSfpTransceiverDetailType": sleEthernetSfpTransceiverDetailType,
       "sleEthernetSfpTransceiverCodes": sleEthernetSfpTransceiverCodes,
       "sleEthernetSfpSpeed": sleEthernetSfpSpeed,
       "sleEthernetSfpLength": sleEthernetSfpLength,
       "sleEthernetSfpWaveLength": sleEthernetSfpWaveLength,
       "sleEthernetSfpMultimodeLengthOm1": sleEthernetSfpMultimodeLengthOm1,
       "sleEthernetSfpMultimodeLengthOm2": sleEthernetSfpMultimodeLengthOm2,
       "sleEthernetSfpMultimodeLengthOm3": sleEthernetSfpMultimodeLengthOm3,
       "sleEthernetSfpTransceiverDetailTypeStr": sleEthernetSfpTransceiverDetailTypeStr,
       "sleEthernetSfpTransceiverLengthStr": sleEthernetSfpTransceiverLengthStr,
       "sleEthernetSfpWaveLengthStr": sleEthernetSfpWaveLengthStr,
       "sleEthernetSfpConnectorType": sleEthernetSfpConnectorType,
       "sleEthernetSfpDdmState": sleEthernetSfpDdmState,
       "sleEthernetSfpNegoState": sleEthernetSfpNegoState,
       "sleEthernetSFPControl": sleEthernetSFPControl,
       "sleEthernetSFPControlRequest": sleEthernetSFPControlRequest,
       "sleEthernetSFPControlStatus": sleEthernetSFPControlStatus,
       "sleEthernetSFPControlTimer": sleEthernetSFPControlTimer,
       "sleEthernetSFPControlTimeStamp": sleEthernetSFPControlTimeStamp,
       "sleEthernetSFPControlReqResult": sleEthernetSFPControlReqResult,
       "sleEthernetSFPControlIndex": sleEthernetSFPControlIndex,
       "sleEthernetSfpControlDdmState": sleEthernetSfpControlDdmState,
       "sleEthernetSFPNotification": sleEthernetSFPNotification,
       "sleEthernetSFPRemoteReset": sleEthernetSFPRemoteReset,
       "sleEthernetSFPDdmState": sleEthernetSFPDdmState,
       "sleEthernetSFPThresholdTable": sleEthernetSFPThresholdTable,
       "sleEthernetSFPThresholdEntry": sleEthernetSFPThresholdEntry,
       "sleEthernetSFPThresholdIfIndex": sleEthernetSFPThresholdIfIndex,
       "sleEthernetSFPThresholdType": sleEthernetSFPThresholdType,
       "sleEthernetSFPThresholdSfpLow": sleEthernetSFPThresholdSfpLow,
       "sleEthernetSFPThresholdSfpHigh": sleEthernetSFPThresholdSfpHigh,
       "sleEthernetSFPThresholdSystemLow": sleEthernetSFPThresholdSystemLow,
       "sleEthernetSFPThresholdSystemHigh": sleEthernetSFPThresholdSystemHigh,
       "sleEthernetSFPThresholdControl": sleEthernetSFPThresholdControl,
       "sleEthernetSFPThresholdControlRequest": sleEthernetSFPThresholdControlRequest,
       "sleEthernetSFPThresholdControlStatus": sleEthernetSFPThresholdControlStatus,
       "sleEthernetSFPThresholdControlTimer": sleEthernetSFPThresholdControlTimer,
       "sleEthernetSFPThresholdControlTimeStamp": sleEthernetSFPThresholdControlTimeStamp,
       "sleEthernetSFPThresholdControlReqResult": sleEthernetSFPThresholdControlReqResult,
       "sleEthernetSFPThresholdControlIfIndex": sleEthernetSFPThresholdControlIfIndex,
       "sleEthernetSFPThresholdControlType": sleEthernetSFPThresholdControlType,
       "sleEthernetSFPThresholdControlSfpLow": sleEthernetSFPThresholdControlSfpLow,
       "sleEthernetSFPThresholdControlSfpHigh": sleEthernetSFPThresholdControlSfpHigh,
       "sleEthernetSFPThresholdControlSystemLow": sleEthernetSFPThresholdControlSystemLow,
       "sleEthernetSFPThresholdControlSystemHigh": sleEthernetSFPThresholdControlSystemHigh,
       "sleEthernetSFPThresholdNotification": sleEthernetSFPThresholdNotification,
       "sleEthernetSFPThresholdSfpChanged": sleEthernetSFPThresholdSfpChanged,
       "sleEthernetSFPThresholdSystemChanged": sleEthernetSFPThresholdSystemChanged,
       "sleEthernetSFPThresholdDestroyed": sleEthernetSFPThresholdDestroyed,
       "slePower": slePower,
       "slePowerTable": slePowerTable,
       "slePowerEntry": slePowerEntry,
       "slePowerIndex": slePowerIndex,
       "slePowerPhyIndex": slePowerPhyIndex,
       "slePowerState": slePowerState,
       "slePowerType": slePowerType,
       "slePowerPSUType": slePowerPSUType,
       "sleFanModule": sleFanModule,
       "sleFanModuleTable": sleFanModuleTable,
       "sleFanModuleEntry": sleFanModuleEntry,
       "sleFanModuleIndex": sleFanModuleIndex,
       "sleFanModulePhyIndex": sleFanModulePhyIndex,
       "sleFanModuleUnitNum": sleFanModuleUnitNum,
       "sleFanModuleAdminState": sleFanModuleAdminState,
       "sleFanModuleSpeedThreshold": sleFanModuleSpeedThreshold,
       "sleFanModuleControl": sleFanModuleControl,
       "sleFanModuleControlRequest": sleFanModuleControlRequest,
       "sleFanModuleControlStatus": sleFanModuleControlStatus,
       "sleFanModuleControlTimer": sleFanModuleControlTimer,
       "sleFanModuleControlTimeStamp": sleFanModuleControlTimeStamp,
       "sleFanModuleControlReqResult": sleFanModuleControlReqResult,
       "sleFanModuleControlIndex": sleFanModuleControlIndex,
       "sleFanModuleControlAdminState": sleFanModuleControlAdminState,
       "sleFanModuleControlSpeedThreshold": sleFanModuleControlSpeedThreshold,
       "sleFanModuleNotification": sleFanModuleNotification,
       "sleFanAdminStateChanged": sleFanAdminStateChanged,
       "sleFanSpeedThresholdChanged": sleFanSpeedThresholdChanged,
       "sleFanUnit": sleFanUnit,
       "sleFanUnitTable": sleFanUnitTable,
       "sleFanUnitEntry": sleFanUnitEntry,
       "sleFanUnitIndex": sleFanUnitIndex,
       "sleFanUnitOperState": sleFanUnitOperState,
       "sleFanUnitSpeed": sleFanUnitSpeed,
       "sleTemperature": sleTemperature,
       "sleTemperatureTable": sleTemperatureTable,
       "sleTemperatureEntry": sleTemperatureEntry,
       "sleTemperatureIndex": sleTemperatureIndex,
       "sleTemperatureState": sleTemperatureState,
       "sleTemperatureValue": sleTemperatureValue,
       "sleTemperatureHighThreshold": sleTemperatureHighThreshold,
       "sleTemperatureLowThreshold": sleTemperatureLowThreshold,
       "sleTemperatureWarnHighThreshold": sleTemperatureWarnHighThreshold,
       "sleTemperatureWarnLowThreshold": sleTemperatureWarnLowThreshold,
       "sleTemperatureWarnDuration": sleTemperatureWarnDuration,
       "sleTemperatureAlarmHighThreshold": sleTemperatureAlarmHighThreshold,
       "sleTemperatureAlarmLowThreshold": sleTemperatureAlarmLowThreshold,
       "sleTemperatureAlarmDuration": sleTemperatureAlarmDuration,
       "sleTemperatureControl": sleTemperatureControl,
       "sleTemperatureControlRequest": sleTemperatureControlRequest,
       "sleTemperatureControlStatus": sleTemperatureControlStatus,
       "sleTemperatureControlTimer": sleTemperatureControlTimer,
       "sleTemperatureControlTimeStamp": sleTemperatureControlTimeStamp,
       "sleTemperatureControlReqResult": sleTemperatureControlReqResult,
       "sleTemperatureControlIndex": sleTemperatureControlIndex,
       "sleTemperatureControlHighThreshold": sleTemperatureControlHighThreshold,
       "sleTemperatureControlLowThreshold": sleTemperatureControlLowThreshold,
       "sleTemperatureControlDuration": sleTemperatureControlDuration,
       "sleTemperatureNotification": sleTemperatureNotification,
       "sleTemperatureThresholdChanged": sleTemperatureThresholdChanged,
       "sleBattery": sleBattery,
       "sleBatteryTable": sleBatteryTable,
       "sleBatteryEntry": sleBatteryEntry,
       "sleBatteryIndex": sleBatteryIndex,
       "sleOperationPowerType": sleOperationPowerType,
       "sleOperationPowerInfo": sleOperationPowerInfo,
       "slePSUACPowerState": slePSUACPowerState,
       "slePSUTemperture": slePSUTemperture,
       "slePSUTempThreshold": slePSUTempThreshold,
       "slePSUOutVoltage": slePSUOutVoltage,
       "slePSUOverTemp": slePSUOverTemp,
       "slePSUFirmwareVer": slePSUFirmwareVer,
       "sleRBUEquipState": sleRBUEquipState,
       "sleRBUModeStaus": sleRBUModeStaus,
       "sleRBUTemperature1": sleRBUTemperature1,
       "sleRBUTemperature2": sleRBUTemperature2,
       "sleRBUTempLowThreshold": sleRBUTempLowThreshold,
       "sleRBUOutVoltage": sleRBUOutVoltage,
       "sleRBUChargeCurrent": sleRBUChargeCurrent,
       "sleRBURemainCapacity": sleRBURemainCapacity,
       "sleRBUOverTemp": sleRBUOverTemp,
       "sleBatteryLow": sleBatteryLow,
       "sleRBUTempHighThreshold": sleRBUTempHighThreshold,
       "sleRBUBTStatus": sleRBUBTStatus,
       "sleRBUBTThreshold": sleRBUBTThreshold,
       "sleRBURechargeVoltage": sleRBURechargeVoltage,
       "sleBatteryCellStatus": sleBatteryCellStatus,
       "sleBPSUACHardwareVer": sleBPSUACHardwareVer,
       "sleBatteryControl": sleBatteryControl,
       "sleBatteryControlRequest": sleBatteryControlRequest,
       "sleBatteryControlStatus": sleBatteryControlStatus,
       "sleBatteryControlTimer": sleBatteryControlTimer,
       "sleBatteryControlTimeStamp": sleBatteryControlTimeStamp,
       "sleBatteryControlReqResult": sleBatteryControlReqResult,
       "sleBatteryControlRBUBTStatus": sleBatteryControlRBUBTStatus,
       "sleBatteryControlRBUBTThreshold": sleBatteryControlRBUBTThreshold,
       "sleBatteryControlRBURechargeVoltage": sleBatteryControlRBURechargeVoltage,
       "sleBatteryControlTemperThresh1": sleBatteryControlTemperThresh1,
       "sleBatteryControlTemperThresh2": sleBatteryControlTemperThresh2,
       "sleBatteryNotification": sleBatteryNotification,
       "sleBatteryForceChargeChanged": sleBatteryForceChargeChanged,
       "sleBatteryChargingStartChanged": sleBatteryChargingStartChanged,
       "sleBatteryForceChargeNonStopChanged": sleBatteryForceChargeNonStopChanged,
       "sleBatteryRBUBTStatusChanged": sleBatteryRBUBTStatusChanged,
       "sleBatteryRBUBTThresholdChanged": sleBatteryRBUBTThresholdChanged,
       "sleBatteryRBURechargeVoltageChanged": sleBatteryRBURechargeVoltageChanged,
       "sleBatteryPsuAcTemperThreshChanged": sleBatteryPsuAcTemperThreshChanged,
       "sleBatteryRBUTemperThreshChanged": sleBatteryRBUTemperThreshChanged,
       "sleBatteryBackupTable": sleBatteryBackupTable,
       "sleBatteryBackupEntry": sleBatteryBackupEntry,
       "sleBatteryBackupFile": sleBatteryBackupFile,
       "sleBatteryBackupControl": sleBatteryBackupControl,
       "sleBatteryBackupControlRequest": sleBatteryBackupControlRequest,
       "sleBatteryBackupControlStatus": sleBatteryBackupControlStatus,
       "sleBatteryBackupControlTimer": sleBatteryBackupControlTimer,
       "sleBatteryBackupControlTimeStamp": sleBatteryBackupControlTimeStamp,
       "sleBatteryBackupControlReqResult": sleBatteryBackupControlReqResult,
       "sleBatteryBackupControlServerIP": sleBatteryBackupControlServerIP,
       "sleBatteryBackupControlUserID": sleBatteryBackupControlUserID,
       "sleBatteryBackupControlPassword": sleBatteryBackupControlPassword,
       "sleBatteryBackupControlFlag": sleBatteryBackupControlFlag,
       "sleBatteryBackupControlLocalFile": sleBatteryBackupControlLocalFile,
       "sleBatteryBackupControlRemoteFile": sleBatteryBackupControlRemoteFile,
       "sleBatterBackupNotification": sleBatterBackupNotification,
       "sleBatteryBackupProfileChanged": sleBatteryBackupProfileChanged,
       "sleBatteryBackupUpgraded": sleBatteryBackupUpgraded,
       "sleBatteryBackupTableCleared": sleBatteryBackupTableCleared,
       "sleDoor": sleDoor,
       "sleDoorInfo": sleDoorInfo,
       "sleDoorStatus": sleDoorStatus,
       "sleCpu": sleCpu,
       "sleCpuInfo": sleCpuInfo,
       "sleCpuProcessor": sleCpuProcessor,
       "sleCpuModel": sleCpuModel,
       "sleCpuRevision": sleCpuRevision,
       "sleCpuBogomips": sleCpuBogomips,
       "sleCpuManufacturer": sleCpuManufacturer,
       "sleCpuClock": sleCpuClock,
       "sleCpuBusClock": sleCpuBusClock,
       "sleClockModule": sleClockModule,
       "sleClockModuleTable": sleClockModuleTable,
       "sleClockModuleEntry": sleClockModuleEntry,
       "sleClockModuleIndex": sleClockModuleIndex,
       "sleClockModuleBoardId": sleClockModuleBoardId,
       "sleClockModuleInstallStatus": sleClockModuleInstallStatus,
       "sleClockModuleInitStatus": sleClockModuleInitStatus,
       "sleClockModuleOPMode": sleClockModuleOPMode,
       "sleClockInfo": sleClockInfo,
       "sleClockInfoInSrcType": sleClockInfoInSrcType,
       "sleClockInfoInSrcStatus": sleClockInfoInSrcStatus,
       "sleClockInfoInSrcAISStatus": sleClockInfoInSrcAISStatus,
       "sleClockInfoInSrcLoSStatus": sleClockInfoInSrcLoSStatus,
       "sleClockInfoInSrcLDSCStatus": sleClockInfoInSrcLDSCStatus,
       "sleClockInfoInSrcNtrClockType": sleClockInfoInSrcNtrClockType,
       "sleSlot": sleSlot,
       "sleSlotSystemInfo": sleSlotSystemInfo,
       "sleSlotSystemInfoTable": sleSlotSystemInfoTable,
       "sleSlotSystemInfoEntry": sleSlotSystemInfoEntry,
       "sleSlotSystemIndex": sleSlotSystemIndex,
       "sleSlotSystemUptime": sleSlotSystemUptime,
       "sleSlotSystemModelName": sleSlotSystemModelName,
       "sleSlotSystemSerialNumber": sleSlotSystemSerialNumber,
       "sleSlotSystemHWVersion": sleSlotSystemHWVersion,
       "sleSlotSystemBLVersion": sleSlotSystemBLVersion,
       "sleSlotSystemSWCompatibility": sleSlotSystemSWCompatibility,
       "sleSlotSystemOSVersion": sleSlotSystemOSVersion,
       "sleSlotSystemMacAddress": sleSlotSystemMacAddress,
       "sleSlotSystemCPULoadAll": sleSlotSystemCPULoadAll,
       "sleSlotSystemCPULoadInterrupt": sleSlotSystemCPULoadInterrupt,
       "sleSlotSystemMemoryTotal": sleSlotSystemMemoryTotal,
       "sleSlotSystemMemoryFree": sleSlotSystemMemoryFree,
       "sleSlotSystemMemoryShared": sleSlotSystemMemoryShared,
       "sleSlotSystemMemoryBuffers": sleSlotSystemMemoryBuffers,
       "sleSlotSystemMemoryCached": sleSlotSystemMemoryCached,
       "sleSlotSystemMemorySwapTotal": sleSlotSystemMemorySwapTotal,
       "sleSlotSystemMemorySwapFree": sleSlotSystemMemorySwapFree,
       "sleSlotSystemBootReason": sleSlotSystemBootReason,
       "sleSlotSystemBootTime": sleSlotSystemBootTime,
       "sleSlotSystemVoltage": sleSlotSystemVoltage,
       "sleSlotSystemPowerLevelStatus": sleSlotSystemPowerLevelStatus,
       "sleSlotSystemInfoLEDStatus": sleSlotSystemInfoLEDStatus,
       "sleSlotSystemInfoPackageVersion": sleSlotSystemInfoPackageVersion,
       "sleSlotSystemInfoManufacturer": sleSlotSystemInfoManufacturer,
       "sleSlotSystemInfoManufactureDate": sleSlotSystemInfoManufactureDate,
       "sleSlotSystemCPULoadHighThreshold": sleSlotSystemCPULoadHighThreshold,
       "sleSlotSystemCPULoadHighThresholdTimer": sleSlotSystemCPULoadHighThresholdTimer,
       "sleSlotSystemCPULoadLowThreshold": sleSlotSystemCPULoadLowThreshold,
       "sleSlotSystemCPULoadLowThresholdTimer": sleSlotSystemCPULoadLowThresholdTimer,
       "sleSlotSystemCPULoadCurrent": sleSlotSystemCPULoadCurrent,
       "sleSlotSystemCPUOverallStatus": sleSlotSystemCPUOverallStatus,
       "sleSlotSystemTemperOverallStatus": sleSlotSystemTemperOverallStatus,
       "sleSlotSystemControl": sleSlotSystemControl,
       "sleSlotSystemControlRequest": sleSlotSystemControlRequest,
       "sleSlotSystemControlStatus": sleSlotSystemControlStatus,
       "sleSlotSystemControlTimer": sleSlotSystemControlTimer,
       "sleSlotSystemControlTimeStamp": sleSlotSystemControlTimeStamp,
       "sleSlotSystemControlReqResult": sleSlotSystemControlReqResult,
       "sleSlotSystemControlSlotIndex": sleSlotSystemControlSlotIndex,
       "sleSlotSystemControlCPULoadHighThreshold": sleSlotSystemControlCPULoadHighThreshold,
       "sleSlotSystemControlCPULoadHighThresholdTimer": sleSlotSystemControlCPULoadHighThresholdTimer,
       "sleSlotSystemControlCPULoadLowThreshold": sleSlotSystemControlCPULoadLowThreshold,
       "sleSlotSystemControlCPULoadLowThresholdTimer": sleSlotSystemControlCPULoadLowThresholdTimer,
       "sleSlotSystemNotification": sleSlotSystemNotification,
       "sleSlotSystemRestart": sleSlotSystemRestart,
       "sleSlotSystemCPULoadChagned": sleSlotSystemCPULoadChagned,
       "sleSlotSystemCPULoadDeleted": sleSlotSystemCPULoadDeleted,
       "sleSlotStatusInfo": sleSlotStatusInfo,
       "sleSlotStatusInfoTable": sleSlotStatusInfoTable,
       "sleSlotStatusInfoEntry": sleSlotStatusInfoEntry,
       "sleSlotStatusPlan": sleSlotStatusPlan,
       "sleSlotStatusPlanCardType": sleSlotStatusPlanCardType,
       "sleSlotStatusCurrentInstall": sleSlotStatusCurrentInstall,
       "sleSlotStatusCurrentInstallCardType": sleSlotStatusCurrentInstallCardType,
       "sleSlotStatusCardOperation": sleSlotStatusCardOperation,
       "sleSlotStatusLock": sleSlotStatusLock,
       "sleSlotStatusUpgradeMode": sleSlotStatusUpgradeMode,
       "sleSlotStatusActionEvent": sleSlotStatusActionEvent,
       "sleSlotStatusState": sleSlotStatusState,
       "sleSlotStatusPower": sleSlotStatusPower,
       "sleSlotStatusSerialNumber": sleSlotStatusSerialNumber,
       "sleSlotStatusHealthState": sleSlotStatusHealthState,
       "sleslotStatusOverallState": sleslotStatusOverallState,
       "sleslotStatusSyncState": sleslotStatusSyncState,
       "sleSlotStatusControl": sleSlotStatusControl,
       "sleSlotStatusControlRequest": sleSlotStatusControlRequest,
       "sleSlotStatusControlStatus": sleSlotStatusControlStatus,
       "sleSlotStatusControlTimer": sleSlotStatusControlTimer,
       "sleSlotStatusControlTimeStamp": sleSlotStatusControlTimeStamp,
       "sleSlotStatusControlReqResult": sleSlotStatusControlReqResult,
       "sleSlotStatusControlSlotIndex": sleSlotStatusControlSlotIndex,
       "sleSlotStatusControlPlanCardType": sleSlotStatusControlPlanCardType,
       "sleSlotStatusControlUpgradeMode": sleSlotStatusControlUpgradeMode,
       "sleSlotStatusNotification": sleSlotStatusNotification,
       "sleSlotStatusLocked": sleSlotStatusLocked,
       "sleSlotStatusUnlocked": sleSlotStatusUnlocked,
       "sleSlotStatusPlanning": sleSlotStatusPlanning,
       "sleSlotStatusNoPlanning": sleSlotStatusNoPlanning,
       "sleSlotStatusUpgradeModeChanged": sleSlotStatusUpgradeModeChanged,
       "sleSlotStatusPowerUp": sleSlotStatusPowerUp,
       "sleSlotStatusPowerDown": sleSlotStatusPowerDown,
       "sleSlotStatusPowerReset": sleSlotStatusPowerReset,
       "sleSlotNosInfo": sleSlotNosInfo,
       "sleSlotNosInfoTable": sleSlotNosInfoTable,
       "sleSlotNosInfoEntry": sleSlotNosInfoEntry,
       "sleSlotNosVersion": sleSlotNosVersion,
       "sleSlotNosRevision": sleSlotNosRevision,
       "sleSlotNosSize": sleSlotNosSize,
       "sleSlotNosUpgradeStatus": sleSlotNosUpgradeStatus,
       "sleSlotNosStbVersion": sleSlotNosStbVersion,
       "sleSlotNosStbRevision": sleSlotNosStbRevision,
       "sleSlotNosStbSize": sleSlotNosStbSize,
       "sleSlotNosControl": sleSlotNosControl,
       "sleSlotNosControlRequest": sleSlotNosControlRequest,
       "sleSlotNosControlStatus": sleSlotNosControlStatus,
       "sleSlotNosControlTimer": sleSlotNosControlTimer,
       "sleSlotNosControlTimeStamp": sleSlotNosControlTimeStamp,
       "sleSlotNosControlReqResult": sleSlotNosControlReqResult,
       "sleSlotNosControlSlotIndex": sleSlotNosControlSlotIndex,
       "sleSlotNosControlUpDownMethod": sleSlotNosControlUpDownMethod,
       "sleSlotNosControlUpDownFlag": sleSlotNosControlUpDownFlag,
       "sleSlotNosControlServerAddress": sleSlotNosControlServerAddress,
       "sleSlotNosControlUserID": sleSlotNosControlUserID,
       "sleSlotNosControlPassword": sleSlotNosControlPassword,
       "sleSlotNosControlFileName": sleSlotNosControlFileName,
       "sleSlotNosNotification": sleSlotNosNotification,
       "sleSlotNosUpgrade": sleSlotNosUpgrade,
       "sleSlotNosDownload": sleSlotNosDownload,
       "sleSlotNosBootloaderUpgrade": sleSlotNosBootloaderUpgrade,
       "sleSlotReleasedIUNosInfo": sleSlotReleasedIUNosInfo,
       "sleSlotReleasedNIUNosVersion": sleSlotReleasedNIUNosVersion,
       "sleSlotReleasedNIUNosRevision": sleSlotReleasedNIUNosRevision,
       "sleSlotReleasedNIUNosSize": sleSlotReleasedNIUNosSize,
       "sleSlotReleasedGPIUNosVersion": sleSlotReleasedGPIUNosVersion,
       "sleSlotReleasedGPIUNosRevision": sleSlotReleasedGPIUNosRevision,
       "sleSlotReleasedGPIUNosSize": sleSlotReleasedGPIUNosSize,
       "sleSlotReleasedSIUNosVersion": sleSlotReleasedSIUNosVersion,
       "sleSlotReleasedSIUNosRevision": sleSlotReleasedSIUNosRevision,
       "sleSlotReleasedSIUNosSize": sleSlotReleasedSIUNosSize,
       "sleSlotReleasedIU10GE8NosVersion": sleSlotReleasedIU10GE8NosVersion,
       "sleSlotReleasedIU10GE8NosRevision": sleSlotReleasedIU10GE8NosRevision,
       "sleSlotReleasedIU10GE8NosSize": sleSlotReleasedIU10GE8NosSize,
       "sleSlotReleasedIU10GEPON8NosVersion": sleSlotReleasedIU10GEPON8NosVersion,
       "sleSlotReleasedIU10GEPON8NosRevision": sleSlotReleasedIU10GEPON8NosRevision,
       "sleSlotReleasedIU10GEPON8NosSize": sleSlotReleasedIU10GEPON8NosSize,
       "sleSlotReleasedIUGEPON8NosVersion": sleSlotReleasedIUGEPON8NosVersion,
       "sleSlotReleasedIUGEPON8NosRevision": sleSlotReleasedIUGEPON8NosRevision,
       "sleSlotReleasedIUGEPON8NosSize": sleSlotReleasedIUGEPON8NosSize,
       "sleSlotPowerMon": sleSlotPowerMon,
       "sleSlotPowerMonTable": sleSlotPowerMonTable,
       "sleSlotPowerMonEntry": sleSlotPowerMonEntry,
       "sleSlotPowerMonIndex": sleSlotPowerMonIndex,
       "sleSlotPowerMonStatus": sleSlotPowerMonStatus,
       "sleSlotPowerMonVoltage": sleSlotPowerMonVoltage,
       "sleSlotAiu": sleSlotAiu,
       "sleSlotAiuRunStatus": sleSlotAiuRunStatus,
       "sleSlotAiuAlarmStatus": sleSlotAiuAlarmStatus,
       "sleSlotProtection": sleSlotProtection,
       "sleSlotProtectionBase": sleSlotProtectionBase,
       "sleSlotProtectionInfo": sleSlotProtectionInfo,
       "sleSlotProtectionSystemStatus": sleSlotProtectionSystemStatus,
       "sleSlotProtectionSystemThreshold": sleSlotProtectionSystemThreshold,
       "sleSlotProtectionIUPowerStatus": sleSlotProtectionIUPowerStatus,
       "sleSlotProtectionControl": sleSlotProtectionControl,
       "sleSlotProtectionControlRequest": sleSlotProtectionControlRequest,
       "sleSlotProtectionControlStatus": sleSlotProtectionControlStatus,
       "sleSlotProtectionControlTimer": sleSlotProtectionControlTimer,
       "sleSlotProtectionControlTimeStamp": sleSlotProtectionControlTimeStamp,
       "sleSlotProtectionControlReqResult": sleSlotProtectionControlReqResult,
       "sleSlotProtectionControlSystemStatus": sleSlotProtectionControlSystemStatus,
       "sleSlotProtectionControlSystemThreshold": sleSlotProtectionControlSystemThreshold,
       "sleSlotProtectionControlIUPowerStatus": sleSlotProtectionControlIUPowerStatus,
       "sleSlotProtectionNotification": sleSlotProtectionNotification,
       "sleSlotProtectionSystemStatusChanged": sleSlotProtectionSystemStatusChanged,
       "sleSlotProtectionSystemThreshChanged": sleSlotProtectionSystemThreshChanged,
       "sleSlotProtectionIUPowerStatusChanged": sleSlotProtectionIUPowerStatusChanged,
       "sleSlotProtectionIU": sleSlotProtectionIU,
       "sleSlotProtectionIUTable": sleSlotProtectionIUTable,
       "sleSlotProtectionIUEntry": sleSlotProtectionIUEntry,
       "sleSlotProtectionIUTemperHighThresh": sleSlotProtectionIUTemperHighThresh,
       "sleSlotProtectionIUTemperLowThresh": sleSlotProtectionIUTemperLowThresh,
       "sleSlotProtectionIUPowerThresh": sleSlotProtectionIUPowerThresh,
       "sleSlotProtectionIUTemper": sleSlotProtectionIUTemper,
       "sleSlotProtectionIUTemper2": sleSlotProtectionIUTemper2,
       "sleSlotProtectionIUControl": sleSlotProtectionIUControl,
       "sleSlotProtectionIUControlRequest": sleSlotProtectionIUControlRequest,
       "sleSlotProtectionIUControlStatus": sleSlotProtectionIUControlStatus,
       "sleSlotProtectionIUControlTimer": sleSlotProtectionIUControlTimer,
       "sleSlotProtectionIUControlTimeStamp": sleSlotProtectionIUControlTimeStamp,
       "sleSlotProtectionIUControlReqResult": sleSlotProtectionIUControlReqResult,
       "sleSlotProtectionIUControlindex": sleSlotProtectionIUControlindex,
       "sleSlotProtectionIUControlTemperHighThresh": sleSlotProtectionIUControlTemperHighThresh,
       "sleSlotProtectionIUControlTemperLowThresh": sleSlotProtectionIUControlTemperLowThresh,
       "sleSlotProtectionIUControlPowerThresh": sleSlotProtectionIUControlPowerThresh,
       "sleSlotProtectionIUNotification": sleSlotProtectionIUNotification,
       "sleSlotProtectionIUTemperThreshChanged": sleSlotProtectionIUTemperThreshChanged,
       "sleSlotProtectionIUPowerThreshChanged": sleSlotProtectionIUPowerThreshChanged,
       "sleRF": sleRF,
       "sleRfBaseInfo": sleRfBaseInfo,
       "sleRfConnectStatus": sleRfConnectStatus,
       "sleRfPowerStatus": sleRfPowerStatus,
       "sleRfEthertype": sleRfEthertype,
       "sleRfSrcAddress": sleRfSrcAddress,
       "sleRfDesAddress": sleRfDesAddress,
       "sleRfBaseControl": sleRfBaseControl,
       "sleRfBaseControlRequest": sleRfBaseControlRequest,
       "sleRfBaseControlStatus": sleRfBaseControlStatus,
       "sleRfBaseControlTimer": sleRfBaseControlTimer,
       "sleRfBaseControlTimeStamp": sleRfBaseControlTimeStamp,
       "sleRfBaseControlReqResult": sleRfBaseControlReqResult,
       "sleRfBaseControlRfEthertype": sleRfBaseControlRfEthertype,
       "sleRfBaseNotification": sleRfBaseNotification,
       "sleRFBaseEthertypeChanged": sleRFBaseEthertypeChanged,
       "sleRFBaseEthertypeResetChanged": sleRFBaseEthertypeResetChanged,
       "sleRfPortTable": sleRfPortTable,
       "sleRfPortEntry": sleRfPortEntry,
       "sleRfPortIndex": sleRfPortIndex,
       "sleRfPortAdminStatus": sleRfPortAdminStatus,
       "sleRfPortOperStatus": sleRfPortOperStatus,
       "sleRFPortControl": sleRFPortControl,
       "sleRfPortControlRequest": sleRfPortControlRequest,
       "sleRfPortControlStatus": sleRfPortControlStatus,
       "sleRfPortControlTimer": sleRfPortControlTimer,
       "sleRfPortControlTimeStamp": sleRfPortControlTimeStamp,
       "sleRfPortControlReqResult": sleRfPortControlReqResult,
       "sleRfPortControlIndex": sleRfPortControlIndex,
       "sleRfPortControlAdminStatus": sleRfPortControlAdminStatus,
       "sleRFPortNotification": sleRFPortNotification,
       "sleRfPortStatusChanged": sleRfPortStatusChanged,
       "sleEnvironmentMonitor": sleEnvironmentMonitor,
       "sleEMTable": sleEMTable,
       "sleEMEntry": sleEMEntry,
       "sleEMInputIndex": sleEMInputIndex,
       "sleEMAlarmString": sleEMAlarmString,
       "sleEMAlarmSeverity": sleEMAlarmSeverity,
       "sleEMmode": sleEMmode,
       "sleEMControl": sleEMControl,
       "sleEMControlRequest": sleEMControlRequest,
       "sleEMControlStatus": sleEMControlStatus,
       "sleEMControlTimer": sleEMControlTimer,
       "sleEMControlTimeStamp": sleEMControlTimeStamp,
       "sleEMControlReqResult": sleEMControlReqResult,
       "sleEMControlInputIndex": sleEMControlInputIndex,
       "sleEMControlAlarmString": sleEMControlAlarmString,
       "sleEMControlAlarmSeverity": sleEMControlAlarmSeverity,
       "sleEMControlmode": sleEMControlmode,
       "sleEMNotification": sleEMNotification,
       "sleEMChanged": sleEMChanged,
       "sleEMDeleted": sleEMDeleted,
       "sleBypass": sleBypass,
       "sleBypassBase": sleBypassBase,
       "sleBypassBaseInfo": sleBypassBaseInfo,
       "sleBypassMode": sleBypassMode,
       "sleBypassStatus": sleBypassStatus,
       "sleBypassBaseControl": sleBypassBaseControl,
       "sleBypassBaseControlRequest": sleBypassBaseControlRequest,
       "sleBypassBaseControlStatus": sleBypassBaseControlStatus,
       "sleBypassBaseControlTimer": sleBypassBaseControlTimer,
       "sleBypassBaseControlTimeStamp": sleBypassBaseControlTimeStamp,
       "sleBypassBaseControlReqResult": sleBypassBaseControlReqResult,
       "sleBypassBaseControlMode": sleBypassBaseControlMode,
       "sleBypassBaseNotification": sleBypassBaseNotification,
       "sleBypassModeChanged": sleBypassModeChanged,
       "sleBypassOption": sleBypassOption,
       "sleBypassOptionConnectivityTable": sleBypassOptionConnectivityTable,
       "sleBypassOptionConnectivityEntry": sleBypassOptionConnectivityEntry,
       "sleBypassOptionConnectivityAddress": sleBypassOptionConnectivityAddress,
       "sleBypassOptionConnectivityPort": sleBypassOptionConnectivityPort,
       "sleBypassOptionConnectivityControl": sleBypassOptionConnectivityControl,
       "sleBypassOptionConnectivityControlRequest": sleBypassOptionConnectivityControlRequest,
       "sleBypassOptionConnectivityControlStatus": sleBypassOptionConnectivityControlStatus,
       "sleBypassOptionConnectivityControlTimer": sleBypassOptionConnectivityControlTimer,
       "sleBypassOptionConnectivityControlTimeStamp": sleBypassOptionConnectivityControlTimeStamp,
       "sleBypassOptionConnectivityControlReqResult": sleBypassOptionConnectivityControlReqResult,
       "sleBypassOptionConnectivityControlAddress": sleBypassOptionConnectivityControlAddress,
       "sleBypassOptionConnectivityControlPort": sleBypassOptionConnectivityControlPort,
       "sleBypassOptionConnectivityNotification": sleBypassOptionConnectivityNotification,
       "sleBypassOptionConnectivitySet": sleBypassOptionConnectivitySet,
       "sleBypassOptionConnectivityUnset": sleBypassOptionConnectivityUnset,
       "sleBypassOptionPingTable": sleBypassOptionPingTable,
       "sleBypassOptionPingEntry": sleBypassOptionPingEntry,
       "sleBypassOptionPingAddress": sleBypassOptionPingAddress,
       "sleBypassOptionPingTransInterval": sleBypassOptionPingTransInterval,
       "sleBypassOptionPingTranNumber": sleBypassOptionPingTranNumber,
       "sleBypassOptionPingReqInterval": sleBypassOptionPingReqInterval,
       "sleBypassOptionPingReqTimeout": sleBypassOptionPingReqTimeout,
       "sleBypassOptionPingLossThresh": sleBypassOptionPingLossThresh,
       "sleBypassOptionPingControl": sleBypassOptionPingControl,
       "sleBypassOptionPingControlRequest": sleBypassOptionPingControlRequest,
       "sleBypassOptionPingControlStatus": sleBypassOptionPingControlStatus,
       "sleBypassOptionPingControlTimer": sleBypassOptionPingControlTimer,
       "sleBypassOptionPingControlTimeStamp": sleBypassOptionPingControlTimeStamp,
       "sleBypassOptionPingControlReqResult": sleBypassOptionPingControlReqResult,
       "sleBypassOptionPingControlAddress": sleBypassOptionPingControlAddress,
       "sleBypassOptionPingControlTransInterval": sleBypassOptionPingControlTransInterval,
       "sleBypassOptionPingControlTranNumber": sleBypassOptionPingControlTranNumber,
       "sleBypassOptionPingControlReqInterval": sleBypassOptionPingControlReqInterval,
       "sleBypassOptionPingControlReqTimeout": sleBypassOptionPingControlReqTimeout,
       "sleBypassOptionPingControlLossThresh": sleBypassOptionPingControlLossThresh,
       "sleBypassOptionPingNotification": sleBypassOptionPingNotification,
       "sleBypassOptionPingSet": sleBypassOptionPingSet,
       "sleBypassOptionPingUnset": sleBypassOptionPingUnset,
       "sleBypassOptionLinkMonitorTable": sleBypassOptionLinkMonitorTable,
       "sleBypassOptionLinkMonitorEntry": sleBypassOptionLinkMonitorEntry,
       "sleBypassOptionLinkMonitorPort": sleBypassOptionLinkMonitorPort,
       "sleBypassOptionLinkMonitorPortStatus": sleBypassOptionLinkMonitorPortStatus,
       "sleBypassOptionLinkMonitorControl": sleBypassOptionLinkMonitorControl,
       "sleBypassOptionLinkMonitorControlRequest": sleBypassOptionLinkMonitorControlRequest,
       "sleBypassOptionLinkMonitorControlStatus": sleBypassOptionLinkMonitorControlStatus,
       "sleBypassOptionLinkMonitorControlTimer": sleBypassOptionLinkMonitorControlTimer,
       "sleBypassOptionLinkMonitorControlTimeStamp": sleBypassOptionLinkMonitorControlTimeStamp,
       "sleBypassOptionLinkMonitorControlReqResult": sleBypassOptionLinkMonitorControlReqResult,
       "sleBypassOptionLinkMonitorControlPort": sleBypassOptionLinkMonitorControlPort,
       "sleBypassOptionLinkMonitorControlPortStatus": sleBypassOptionLinkMonitorControlPortStatus,
       "sleBypassOptioLinkMonitorNotification": sleBypassOptioLinkMonitorNotification,
       "sleBypassOptionLinkMonitorChanged": sleBypassOptionLinkMonitorChanged,
       "sleHFC": sleHFC,
       "sleHFCTable": sleHFCTable,
       "sleHFCEntry": sleHFCEntry,
       "sleHFCOptic1550OTX": sleHFCOptic1550OTX,
       "sleHFCOptic1550OTXAlarm": sleHFCOptic1550OTXAlarm,
       "sleHFCOpticUpstreamOTX": sleHFCOpticUpstreamOTX,
       "sleHFCOpticUpstreamOTXAlarm": sleHFCOpticUpstreamOTXAlarm,
       "sleHFCOpticDownstreamORX": sleHFCOpticDownstreamORX,
       "sleHFCOpticDownstreamORXAlarm": sleHFCOpticDownstreamORXAlarm,
       "sleHFCEDFA1OTX": sleHFCEDFA1OTX,
       "sleHFCEDFA1OTXAlarm": sleHFCEDFA1OTXAlarm,
       "sleHFCEDFA1ORX": sleHFCEDFA1ORX,
       "sleHFCEDFA1ORXAlarm": sleHFCEDFA1ORXAlarm,
       "sleHFCEDFA1LD1Current": sleHFCEDFA1LD1Current,
       "sleHFCEDFA1LD1CurrentAlarm": sleHFCEDFA1LD1CurrentAlarm,
       "sleHFCEDFA1LD2Current": sleHFCEDFA1LD2Current,
       "sleHFCEDFA1LD2CurrentAlarm": sleHFCEDFA1LD2CurrentAlarm,
       "sleHFCEDFA1LD1Temp": sleHFCEDFA1LD1Temp,
       "sleHFCEDFA1LD1TempAlarm": sleHFCEDFA1LD1TempAlarm,
       "sleHFCEDFA1LD2Temp": sleHFCEDFA1LD2Temp,
       "sleHFCEDFA1LD2TempAlarm": sleHFCEDFA1LD2TempAlarm,
       "sleHFCEDFA1CaseTemp": sleHFCEDFA1CaseTemp,
       "sleHFCEDFA1CaseTempAlarm": sleHFCEDFA1CaseTempAlarm,
       "sleHFCEDFA2OTX": sleHFCEDFA2OTX,
       "sleHFCEDFA2OTXAarm": sleHFCEDFA2OTXAarm,
       "sleHFCEDFA2ORX": sleHFCEDFA2ORX,
       "sleHFCEDFA2ORXAlarm": sleHFCEDFA2ORXAlarm,
       "sleHFCEDFA2LD1Current": sleHFCEDFA2LD1Current,
       "sleHFCEDFA2LD1CurrentAlarm": sleHFCEDFA2LD1CurrentAlarm,
       "sleHFCEDFA2LD2Current": sleHFCEDFA2LD2Current,
       "sleHFCEDFA2LD2CurrentAlarm": sleHFCEDFA2LD2CurrentAlarm,
       "sleHFCEDFA2LD1Temp": sleHFCEDFA2LD1Temp,
       "sleHFCEDFA2LD1TempAlarm": sleHFCEDFA2LD1TempAlarm,
       "sleHFCEDFA2LD2Temp": sleHFCEDFA2LD2Temp,
       "sleHFCEDFA2LD2TempAlarm": sleHFCEDFA2LD2TempAlarm,
       "sleHFCEDFA2CaseTemp": sleHFCEDFA2CaseTemp,
       "sleHFCEDFA2CaseTempAlarm": sleHFCEDFA2CaseTempAlarm,
       "sleHFCControl": sleHFCControl,
       "sleHFCControlRequest": sleHFCControlRequest,
       "sleHFCControlStatus": sleHFCControlStatus,
       "sleHFCControlTimer": sleHFCControlTimer,
       "sleHFCControlTimeStamp": sleHFCControlTimeStamp,
       "sleHFCControlReqResult": sleHFCControlReqResult,
       "sleHFCControlAlarmIndex": sleHFCControlAlarmIndex,
       "sleHFCControlAlarmStatus": sleHFCControlAlarmStatus,
       "sleHFCNotification": sleHFCNotification,
       "sleHFCOpticAlarmStatusChanged": sleHFCOpticAlarmStatusChanged,
       "sleDeviceGroup": sleDeviceGroup,
       "sleDeviceNotificationGroup": sleDeviceNotificationGroup}
)
