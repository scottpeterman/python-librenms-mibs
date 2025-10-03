# SNMP MIB module (ULAF2-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\siemens\ULAF2-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 12:27:59 2025
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

(ModuleCompliance,
 NotificationGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup")

(Bits,
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
 enterprises,
 iso) = mibBuilder.importSymbols(
    "SNMPv2-SMI",
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
    "enterprises",
    "iso")

(DisplayString,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_SiemensCH_ObjectIdentity = ObjectIdentity
siemensCH = _SiemensCH_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1887)
)
_Lineintegrator_ObjectIdentity = ObjectIdentity
lineintegrator = _Lineintegrator_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1887, 1)
)
_Ulaf2_ObjectIdentity = ObjectIdentity
ulaf2 = _Ulaf2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1887, 1, 1)
)
_ProxyAgent_ObjectIdentity = ObjectIdentity
proxyAgent = _ProxyAgent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1887, 1, 1, 1)
)
_ProxyAgtVers2_ObjectIdentity = ObjectIdentity
proxyAgtVers2 = _ProxyAgtVers2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1887, 1, 1, 1, 2)
)
_AgtSystem_ObjectIdentity = ObjectIdentity
agtSystem = _AgtSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1887, 1, 1, 1, 2, 1)
)


class _AgtSWVersion_Type(DisplayString):
    """Custom type agtSWVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_AgtSWVersion_Type.__name__ = "DisplayString"
_AgtSWVersion_Object = MibScalar
agtSWVersion = _AgtSWVersion_Object(
    (1, 3, 6, 1, 4, 1, 1887, 1, 1, 1, 2, 1, 1),
    _AgtSWVersion_Type()
)
agtSWVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agtSWVersion.setStatus("mandatory")
_AgtDateLastPortChange_Type = Integer32
_AgtDateLastPortChange_Object = MibScalar
agtDateLastPortChange = _AgtDateLastPortChange_Object(
    (1, 3, 6, 1, 4, 1, 1887, 1, 1, 1, 2, 1, 2),
    _AgtDateLastPortChange_Type()
)
agtDateLastPortChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agtDateLastPortChange.setStatus("mandatory")


class _AgtProxyFeatureFlag_Type(OctetString):
    """Custom type agtProxyFeatureFlag based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(33, 33),
    )
    fixed_length = 33


_AgtProxyFeatureFlag_Type.__name__ = "OctetString"
_AgtProxyFeatureFlag_Object = MibScalar
agtProxyFeatureFlag = _AgtProxyFeatureFlag_Object(
    (1, 3, 6, 1, 4, 1, 1887, 1, 1, 1, 2, 1, 3),
    _AgtProxyFeatureFlag_Type()
)
agtProxyFeatureFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agtProxyFeatureFlag.setStatus("mandatory")
_AgtProxyAciSupported_Type = DisplayString
_AgtProxyAciSupported_Object = MibScalar
agtProxyAciSupported = _AgtProxyAciSupported_Object(
    (1, 3, 6, 1, 4, 1, 1887, 1, 1, 1, 2, 1, 4),
    _AgtProxyAciSupported_Type()
)
agtProxyAciSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agtProxyAciSupported.setStatus("mandatory")
_AgtSerialPort_ObjectIdentity = ObjectIdentity
agtSerialPort = _AgtSerialPort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1887, 1, 1, 1, 2, 2)
)
_AgtPortNumber_Type = Integer32
_AgtPortNumber_Object = MibScalar
agtPortNumber = _AgtPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 1887, 1, 1, 1, 2, 2, 1),
    _AgtPortNumber_Type()
)
agtPortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agtPortNumber.setStatus("mandatory")
_AgtPortTable_Object = MibTable
agtPortTable = _AgtPortTable_Object(
    (1, 3, 6, 1, 4, 1, 1887, 1, 1, 1, 2, 2, 2)
)
if mibBuilder.loadTexts:
    agtPortTable.setStatus("mandatory")
_AgtPortEntry_Object = MibTableRow
agtPortEntry = _AgtPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 1887, 1, 1, 1, 2, 2, 2, 1)
)
agtPortEntry.setIndexNames(
    (0, "ULAF2-MIB", "agtPortIndex"),
)
if mibBuilder.loadTexts:
    agtPortEntry.setStatus("mandatory")
_AgtPortIndex_Type = Integer32
_AgtPortIndex_Object = MibTableColumn
agtPortIndex = _AgtPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 1887, 1, 1, 1, 2, 2, 2, 1, 1),
    _AgtPortIndex_Type()
)
agtPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agtPortIndex.setStatus("mandatory")


class _AgtPortName_Type(DisplayString):
    """Custom type agtPortName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_AgtPortName_Type.__name__ = "DisplayString"
_AgtPortName_Object = MibTableColumn
agtPortName = _AgtPortName_Object(
    (1, 3, 6, 1, 4, 1, 1887, 1, 1, 1, 2, 2, 2, 1, 2),
    _AgtPortName_Type()
)
agtPortName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agtPortName.setStatus("mandatory")


class _AgtPortConnected_Type(Integer32):
    """Custom type agtPortConnected based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_AgtPortConnected_Type.__name__ = "Integer32"
_AgtPortConnected_Object = MibTableColumn
agtPortConnected = _AgtPortConnected_Object(
    (1, 3, 6, 1, 4, 1, 1887, 1, 1, 1, 2, 2, 2, 1, 3),
    _AgtPortConnected_Type()
)
agtPortConnected.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agtPortConnected.setStatus("mandatory")


class _AgtConnectedDevice_Type(DisplayString):
    """Custom type agtConnectedDevice based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_AgtConnectedDevice_Type.__name__ = "DisplayString"
_AgtConnectedDevice_Object = MibTableColumn
agtConnectedDevice = _AgtConnectedDevice_Object(
    (1, 3, 6, 1, 4, 1, 1887, 1, 1, 1, 2, 2, 2, 1, 4),
    _AgtConnectedDevice_Type()
)
agtConnectedDevice.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agtConnectedDevice.setStatus("mandatory")


class _AgtPortType_Type(Integer32):
    """Custom type agtPortType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("local", 1),
          ("portType", 2),
          ("portServer", 3))
    )


_AgtPortType_Type.__name__ = "Integer32"
_AgtPortType_Object = MibTableColumn
agtPortType = _AgtPortType_Object(
    (1, 3, 6, 1, 4, 1, 1887, 1, 1, 1, 2, 2, 2, 1, 5),
    _AgtPortType_Type()
)
agtPortType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agtPortType.setStatus("mandatory")
_AgtPortTypeNumber_Type = Integer32
_AgtPortTypeNumber_Object = MibTableColumn
agtPortTypeNumber = _AgtPortTypeNumber_Object(
    (1, 3, 6, 1, 4, 1, 1887, 1, 1, 1, 2, 2, 2, 1, 6),
    _AgtPortTypeNumber_Type()
)
agtPortTypeNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agtPortTypeNumber.setStatus("mandatory")


class _AgtPortServerName_Type(DisplayString):
    """Custom type agtPortServerName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_AgtPortServerName_Type.__name__ = "DisplayString"
_AgtPortServerName_Object = MibTableColumn
agtPortServerName = _AgtPortServerName_Object(
    (1, 3, 6, 1, 4, 1, 1887, 1, 1, 1, 2, 2, 2, 1, 7),
    _AgtPortServerName_Type()
)
agtPortServerName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agtPortServerName.setStatus("mandatory")


class _AgtPortState_Type(Integer32):
    """Custom type agtPortState based on Integer32"""
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
              254)
        )
    )
    namedValues = NamedValues(
        *(("unopenedSerial", 1),
          ("openedSerial", 2),
          ("connectingRemote", 3),
          ("openedRemote", 4),
          ("failedRemote", 5),
          ("disabled", 6),
          ("invalid", 7),
          ("unknown", 254))
    )


_AgtPortState_Type.__name__ = "Integer32"
_AgtPortState_Object = MibTableColumn
agtPortState = _AgtPortState_Object(
    (1, 3, 6, 1, 4, 1, 1887, 1, 1, 1, 2, 2, 2, 1, 8),
    _AgtPortState_Type()
)
agtPortState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agtPortState.setStatus("mandatory")


class _AgtPortDeviceFamily_Type(Integer32):
    """Custom type agtPortDeviceFamily based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              254)
        )
    )
    namedValues = NamedValues(
        *(("ulaf2", 1),
          ("ulafPlus", 2),
          ("ulaf2AndPlus", 3),
          ("unknown", 254))
    )


_AgtPortDeviceFamily_Type.__name__ = "Integer32"
_AgtPortDeviceFamily_Object = MibTableColumn
agtPortDeviceFamily = _AgtPortDeviceFamily_Object(
    (1, 3, 6, 1, 4, 1, 1887, 1, 1, 1, 2, 2, 2, 1, 9),
    _AgtPortDeviceFamily_Type()
)
agtPortDeviceFamily.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agtPortDeviceFamily.setStatus("mandatory")


class _AgtPortTryingDevice_Type(Integer32):
    """Custom type agtPortTryingDevice based on Integer32"""
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
              254)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("invalid", 2),
          ("none", 3),
          ("omi", 4),
          ("nag", 5),
          ("omiPlus", 6),
          ("desktopPlus", 7),
          ("unknown", 254))
    )


_AgtPortTryingDevice_Type.__name__ = "Integer32"
_AgtPortTryingDevice_Object = MibTableColumn
agtPortTryingDevice = _AgtPortTryingDevice_Object(
    (1, 3, 6, 1, 4, 1, 1887, 1, 1, 1, 2, 2, 2, 1, 10),
    _AgtPortTryingDevice_Type()
)
agtPortTryingDevice.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agtPortTryingDevice.setStatus("mandatory")
_AgtAlarmCountGroup_ObjectIdentity = ObjectIdentity
agtAlarmCountGroup = _AgtAlarmCountGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1887, 1, 1, 1, 2, 3)
)
_AgtAlarmCount_Type = Integer32
_AgtAlarmCount_Object = MibScalar
agtAlarmCount = _AgtAlarmCount_Object(
    (1, 3, 6, 1, 4, 1, 1887, 1, 1, 1, 2, 3, 1),
    _AgtAlarmCount_Type()
)
agtAlarmCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agtAlarmCount.setStatus("mandatory")


class _AgtPortServerReset_Type(Integer32):
    """Custom type agtPortServerReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              254)
        )
    )
    namedValues = NamedValues(
        *(("reset", 1),
          ("unknown", 254))
    )


_AgtPortServerReset_Type.__name__ = "Integer32"
_AgtPortServerReset_Object = MibScalar
agtPortServerReset = _AgtPortServerReset_Object(
    (1, 3, 6, 1, 4, 1, 1887, 1, 1, 1, 2, 4),
    _AgtPortServerReset_Type()
)
agtPortServerReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agtPortServerReset.setStatus("mandatory")
_Device_ObjectIdentity = ObjectIdentity
device = _Device_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1887, 1, 1, 3)
)
_DeviceVers2_ObjectIdentity = ObjectIdentity
deviceVers2 = _DeviceVers2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1887, 1, 1, 3, 2)
)
_DeviceSystem_ObjectIdentity = ObjectIdentity
deviceSystem = _DeviceSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1887, 1, 1, 3, 2, 1)
)
_DeviceSystemTable_Object = MibTable
deviceSystemTable = _DeviceSystemTable_Object(
    (1, 3, 6, 1, 4, 1, 1887, 1, 1, 3, 2, 1, 1)
)
if mibBuilder.loadTexts:
    deviceSystemTable.setStatus("mandatory")
_DeviceSystemEntry_Object = MibTableRow
deviceSystemEntry = _DeviceSystemEntry_Object(
    (1, 3, 6, 1, 4, 1, 1887, 1, 1, 3, 2, 1, 1, 1)
)
deviceSystemEntry.setIndexNames(
    (0, "ULAF2-MIB", "deviceSystemPortIndex"),
)
if mibBuilder.loadTexts:
    deviceSystemEntry.setStatus("mandatory")
_DeviceSystemPortIndex_Type = Integer32
_DeviceSystemPortIndex_Object = MibTableColumn
deviceSystemPortIndex = _DeviceSystemPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 1887, 1, 1, 3, 2, 1, 1, 1, 1),
    _DeviceSystemPortIndex_Type()
)
deviceSystemPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deviceSystemPortIndex.setStatus("mandatory")
_DeviceLinkNumber_Type = Integer32
_DeviceLinkNumber_Object = MibTableColumn
deviceLinkNumber = _DeviceLinkNumber_Object(
    (1, 3, 6, 1, 4, 1, 1887, 1, 1, 3, 2, 1, 1, 1, 2),
    _DeviceLinkNumber_Type()
)
deviceLinkNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deviceLinkNumber.setStatus("mandatory")


class _DeviceSWVersion_Type(DisplayString):
    """Custom type deviceSWVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_DeviceSWVersion_Type.__name__ = "DisplayString"
_DeviceSWVersion_Object = MibTableColumn
deviceSWVersion = _DeviceSWVersion_Object(
    (1, 3, 6, 1, 4, 1, 1887, 1, 1, 3, 2, 1, 1, 1, 3),
    _DeviceSWVersion_Type()
)
deviceSWVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deviceSWVersion.setStatus("mandatory")


class _DeviceExtAlarm_Type(Integer32):
    """Custom type deviceExtAlarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("noAlarm", 1),
          ("urgent", 2),
          ("notUrgent", 3))
    )


_DeviceExtAlarm_Type.__name__ = "Integer32"
_DeviceExtAlarm_Object = MibTableColumn
deviceExtAlarm = _DeviceExtAlarm_Object(
    (1, 3, 6, 1, 4, 1, 1887, 1, 1, 3, 2, 1, 1, 1, 4),
    _DeviceExtAlarm_Type()
)
deviceExtAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deviceExtAlarm.setStatus("mandatory")
_DeviceDateLastLinkChange_Type = Integer32
_DeviceDateLastLinkChange_Object = MibTableColumn
deviceDateLastLinkChange = _DeviceDateLastLinkChange_Object(
    (1, 3, 6, 1, 4, 1, 1887, 1, 1, 3, 2, 1, 1, 1, 5),
    _DeviceDateLastLinkChange_Type()
)
deviceDateLastLinkChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deviceDateLastLinkChange.setStatus("mandatory")


class _DeviceOmiFeatureFlag_Type(OctetString):
    """Custom type deviceOmiFeatureFlag based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(33, 33),
    )
    fixed_length = 33


_DeviceOmiFeatureFlag_Type.__name__ = "OctetString"
_DeviceOmiFeatureFlag_Object = MibTableColumn
deviceOmiFeatureFlag = _DeviceOmiFeatureFlag_Object(
    (1, 3, 6, 1, 4, 1, 1887, 1, 1, 3, 2, 1, 1, 1, 6),
    _DeviceOmiFeatureFlag_Type()
)
deviceOmiFeatureFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deviceOmiFeatureFlag.setStatus("mandatory")
_DeviceLinks_ObjectIdentity = ObjectIdentity
deviceLinks = _DeviceLinks_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1887, 1, 1, 3, 2, 2)
)
_DeviceLinkTable_Object = MibTable
deviceLinkTable = _DeviceLinkTable_Object(
    (1, 3, 6, 1, 4, 1, 1887, 1, 1, 3, 2, 2, 1)
)
if mibBuilder.loadTexts:
    deviceLinkTable.setStatus("mandatory")
_DeviceLinkEntry_Object = MibTableRow
deviceLinkEntry = _DeviceLinkEntry_Object(
    (1, 3, 6, 1, 4, 1, 1887, 1, 1, 3, 2, 2, 1, 1)
)
deviceLinkEntry.setIndexNames(
    (0, "ULAF2-MIB", "devicePortIndex"),
    (0, "ULAF2-MIB", "deviceLinkIndex"),
)
if mibBuilder.loadTexts:
    deviceLinkEntry.setStatus("mandatory")
_DevicePortIndex_Type = Integer32
_DevicePortIndex_Object = MibTableColumn
devicePortIndex = _DevicePortIndex_Object(
    (1, 3, 6, 1, 4, 1, 1887, 1, 1, 3, 2, 2, 1, 1, 1),
    _DevicePortIndex_Type()
)
devicePortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    devicePortIndex.setStatus("mandatory")
_DeviceLinkIndex_Type = Integer32
_DeviceLinkIndex_Object = MibTableColumn
deviceLinkIndex = _DeviceLinkIndex_Object(
    (1, 3, 6, 1, 4, 1, 1887, 1, 1, 3, 2, 2, 1, 1, 2),
    _DeviceLinkIndex_Type()
)
deviceLinkIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deviceLinkIndex.setStatus("mandatory")


class _DeviceLinkName_Type(DisplayString):
    """Custom type deviceLinkName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_DeviceLinkName_Type.__name__ = "DisplayString"
_DeviceLinkName_Object = MibTableColumn
deviceLinkName = _DeviceLinkName_Object(
    (1, 3, 6, 1, 4, 1, 1887, 1, 1, 3, 2, 2, 1, 1, 3),
    _DeviceLinkName_Type()
)
deviceLinkName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deviceLinkName.setStatus("mandatory")
_DeviceLinkAlarm_Type = Integer32
_DeviceLinkAlarm_Object = MibTableColumn
deviceLinkAlarm = _DeviceLinkAlarm_Object(
    (1, 3, 6, 1, 4, 1, 1887, 1, 1, 3, 2, 2, 1, 1, 4),
    _DeviceLinkAlarm_Type()
)
deviceLinkAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deviceLinkAlarm.setStatus("mandatory")


class _DeviceLinkLocalLtNt_Type(Integer32):
    """Custom type deviceLinkLocalLtNt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              254,
              255)
        )
    )
    namedValues = NamedValues(
        *(("lt", 1),
          ("nt", 2),
          ("unknown", 254),
          ("unsupported", 255))
    )


_DeviceLinkLocalLtNt_Type.__name__ = "Integer32"
_DeviceLinkLocalLtNt_Object = MibTableColumn
deviceLinkLocalLtNt = _DeviceLinkLocalLtNt_Object(
    (1, 3, 6, 1, 4, 1, 1887, 1, 1, 3, 2, 2, 1, 1, 5),
    _DeviceLinkLocalLtNt_Type()
)
deviceLinkLocalLtNt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deviceLinkLocalLtNt.setStatus("mandatory")
_DeviceLinkLocalId_Type = DisplayString
_DeviceLinkLocalId_Object = MibTableColumn
deviceLinkLocalId = _DeviceLinkLocalId_Object(
    (1, 3, 6, 1, 4, 1, 1887, 1, 1, 3, 2, 2, 1, 1, 6),
    _DeviceLinkLocalId_Type()
)
deviceLinkLocalId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deviceLinkLocalId.setStatus("mandatory")
_DeviceLinkFarId_Type = DisplayString
_DeviceLinkFarId_Object = MibTableColumn
deviceLinkFarId = _DeviceLinkFarId_Object(
    (1, 3, 6, 1, 4, 1, 1887, 1, 1, 3, 2, 2, 1, 1, 7),
    _DeviceLinkFarId_Type()
)
deviceLinkFarId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deviceLinkFarId.setStatus("mandatory")


class _DeviceLinkNumReg1_Type(Integer32):
    """Custom type deviceLinkNumReg1 based on Integer32"""
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
              254,
              255)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("one", 2),
          ("two", 3),
          ("three", 4),
          ("four", 5),
          ("five", 6),
          ("six", 7),
          ("seven", 8),
          ("eight", 9),
          ("unknown", 254),
          ("unsupported", 255))
    )


_DeviceLinkNumReg1_Type.__name__ = "Integer32"
_DeviceLinkNumReg1_Object = MibTableColumn
deviceLinkNumReg1 = _DeviceLinkNumReg1_Object(
    (1, 3, 6, 1, 4, 1, 1887, 1, 1, 3, 2, 2, 1, 1, 8),
    _DeviceLinkNumReg1_Type()
)
deviceLinkNumReg1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deviceLinkNumReg1.setStatus("mandatory")


class _DeviceLinkNumReg2_Type(Integer32):
    """Custom type deviceLinkNumReg2 based on Integer32"""
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
              254,
              255)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("one", 2),
          ("two", 3),
          ("three", 4),
          ("four", 5),
          ("five", 6),
          ("six", 7),
          ("seven", 8),
          ("eight", 9),
          ("unknown", 254),
          ("unsupported", 255))
    )


_DeviceLinkNumReg2_Type.__name__ = "Integer32"
_DeviceLinkNumReg2_Object = MibTableColumn
deviceLinkNumReg2 = _DeviceLinkNumReg2_Object(
    (1, 3, 6, 1, 4, 1, 1887, 1, 1, 3, 2, 2, 1, 1, 9),
    _DeviceLinkNumReg2_Type()
)
deviceLinkNumReg2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deviceLinkNumReg2.setStatus("mandatory")
_DeviceLinkLocalModules_Type = Integer32
_DeviceLinkLocalModules_Object = MibTableColumn
deviceLinkLocalModules = _DeviceLinkLocalModules_Object(
    (1, 3, 6, 1, 4, 1, 1887, 1, 1, 3, 2, 2, 1, 1, 10),
    _DeviceLinkLocalModules_Type()
)
deviceLinkLocalModules.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deviceLinkLocalModules.setStatus("mandatory")
_DeviceLinkFarModules_Type = Integer32
_DeviceLinkFarModules_Object = MibTableColumn
deviceLinkFarModules = _DeviceLinkFarModules_Object(
    (1, 3, 6, 1, 4, 1, 1887, 1, 1, 3, 2, 2, 1, 1, 11),
    _DeviceLinkFarModules_Type()
)
deviceLinkFarModules.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deviceLinkFarModules.setStatus("mandatory")
_DeviceLinkLocalHwFabData_Type = DisplayString
_DeviceLinkLocalHwFabData_Object = MibTableColumn
deviceLinkLocalHwFabData = _DeviceLinkLocalHwFabData_Object(
    (1, 3, 6, 1, 4, 1, 1887, 1, 1, 3, 2, 2, 1, 1, 12),
    _DeviceLinkLocalHwFabData_Type()
)
deviceLinkLocalHwFabData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deviceLinkLocalHwFabData.setStatus("mandatory")
_DeviceLinkFarHwFabData_Type = DisplayString
_DeviceLinkFarHwFabData_Object = MibTableColumn
deviceLinkFarHwFabData = _DeviceLinkFarHwFabData_Object(
    (1, 3, 6, 1, 4, 1, 1887, 1, 1, 3, 2, 2, 1, 1, 13),
    _DeviceLinkFarHwFabData_Type()
)
deviceLinkFarHwFabData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deviceLinkFarHwFabData.setStatus("mandatory")
_DeviceLinkLocalG703FabData_Type = DisplayString
_DeviceLinkLocalG703FabData_Object = MibTableColumn
deviceLinkLocalG703FabData = _DeviceLinkLocalG703FabData_Object(
    (1, 3, 6, 1, 4, 1, 1887, 1, 1, 3, 2, 2, 1, 1, 14),
    _DeviceLinkLocalG703FabData_Type()
)
deviceLinkLocalG703FabData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deviceLinkLocalG703FabData.setStatus("mandatory")
_DeviceLinkLocalDataFabData_Type = DisplayString
_DeviceLinkLocalDataFabData_Object = MibTableColumn
deviceLinkLocalDataFabData = _DeviceLinkLocalDataFabData_Object(
    (1, 3, 6, 1, 4, 1, 1887, 1, 1, 3, 2, 2, 1, 1, 15),
    _DeviceLinkLocalDataFabData_Type()
)
deviceLinkLocalDataFabData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deviceLinkLocalDataFabData.setStatus("mandatory")


class _DeviceLinkLocalFeatureFlag_Type(OctetString):
    """Custom type deviceLinkLocalFeatureFlag based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(33, 33),
    )
    fixed_length = 33


_DeviceLinkLocalFeatureFlag_Type.__name__ = "OctetString"
_DeviceLinkLocalFeatureFlag_Object = MibTableColumn
deviceLinkLocalFeatureFlag = _DeviceLinkLocalFeatureFlag_Object(
    (1, 3, 6, 1, 4, 1, 1887, 1, 1, 3, 2, 2, 1, 1, 16),
    _DeviceLinkLocalFeatureFlag_Type()
)
deviceLinkLocalFeatureFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deviceLinkLocalFeatureFlag.setStatus("mandatory")


class _DeviceLinkFarFeatureFlag_Type(OctetString):
    """Custom type deviceLinkFarFeatureFlag based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(33, 33),
    )
    fixed_length = 33


_DeviceLinkFarFeatureFlag_Type.__name__ = "OctetString"
_DeviceLinkFarFeatureFlag_Object = MibTableColumn
deviceLinkFarFeatureFlag = _DeviceLinkFarFeatureFlag_Object(
    (1, 3, 6, 1, 4, 1, 1887, 1, 1, 3, 2, 2, 1, 1, 17),
    _DeviceLinkFarFeatureFlag_Type()
)
deviceLinkFarFeatureFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deviceLinkFarFeatureFlag.setStatus("mandatory")


class _DeviceLinkFarFeatureFlagState_Type(Integer32):
    """Custom type deviceLinkFarFeatureFlagState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              254,
              255)
        )
    )
    namedValues = NamedValues(
        *(("ok", 1),
          ("tooEarly", 2),
          ("legacy", 3),
          ("unknown", 254),
          ("unsupported", 255))
    )


_DeviceLinkFarFeatureFlagState_Type.__name__ = "Integer32"
_DeviceLinkFarFeatureFlagState_Object = MibTableColumn
deviceLinkFarFeatureFlagState = _DeviceLinkFarFeatureFlagState_Object(
    (1, 3, 6, 1, 4, 1, 1887, 1, 1, 3, 2, 2, 1, 1, 18),
    _DeviceLinkFarFeatureFlagState_Type()
)
deviceLinkFarFeatureFlagState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deviceLinkFarFeatureFlagState.setStatus("mandatory")


class _DeviceLinkSruFeatureFlag_Type(OctetString):
    """Custom type deviceLinkSruFeatureFlag based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(33, 33),
    )
    fixed_length = 33


_DeviceLinkSruFeatureFlag_Type.__name__ = "OctetString"
_DeviceLinkSruFeatureFlag_Object = MibTableColumn
deviceLinkSruFeatureFlag = _DeviceLinkSruFeatureFlag_Object(
    (1, 3, 6, 1, 4, 1, 1887, 1, 1, 3, 2, 2, 1, 1, 19),
    _DeviceLinkSruFeatureFlag_Type()
)
deviceLinkSruFeatureFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deviceLinkSruFeatureFlag.setStatus("mandatory")


class _DeviceLinkNumReg3_Type(Integer32):
    """Custom type deviceLinkNumReg3 based on Integer32"""
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
              254,
              255)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("one", 2),
          ("two", 3),
          ("three", 4),
          ("four", 5),
          ("five", 6),
          ("six", 7),
          ("seven", 8),
          ("eight", 9),
          ("unknown", 254),
          ("unsupported", 255))
    )


_DeviceLinkNumReg3_Type.__name__ = "Integer32"
_DeviceLinkNumReg3_Object = MibTableColumn
deviceLinkNumReg3 = _DeviceLinkNumReg3_Object(
    (1, 3, 6, 1, 4, 1, 1887, 1, 1, 3, 2, 2, 1, 1, 20),
    _DeviceLinkNumReg3_Type()
)
deviceLinkNumReg3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deviceLinkNumReg3.setStatus("mandatory")


class _DeviceLinkNumReg4_Type(Integer32):
    """Custom type deviceLinkNumReg4 based on Integer32"""
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
              254,
              255)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("one", 2),
          ("two", 3),
          ("three", 4),
          ("four", 5),
          ("five", 6),
          ("six", 7),
          ("seven", 8),
          ("eight", 9),
          ("unknown", 254),
          ("unsupported", 255))
    )


_DeviceLinkNumReg4_Type.__name__ = "Integer32"
_DeviceLinkNumReg4_Object = MibTableColumn
deviceLinkNumReg4 = _DeviceLinkNumReg4_Object(
    (1, 3, 6, 1, 4, 1, 1887, 1, 1, 3, 2, 2, 1, 1, 21),
    _DeviceLinkNumReg4_Type()
)
deviceLinkNumReg4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deviceLinkNumReg4.setStatus("mandatory")
_Links_ObjectIdentity = ObjectIdentity
links = _Links_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1887, 1, 1, 4)
)
_LinksVers2_ObjectIdentity = ObjectIdentity
linksVers2 = _LinksVers2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1887, 1, 1, 4, 2)
)
_Link_ObjectIdentity = ObjectIdentity
link = _Link_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1887, 1, 1, 4, 2, 1)
)
_LinkConfigTable_Object = MibTable
linkConfigTable = _LinkConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 1887, 1, 1, 4, 2, 1, 1)
)
if mibBuilder.loadTexts:
    linkConfigTable.setStatus("mandatory")
_LinkConfigEntry_Object = MibTableRow
linkConfigEntry = _LinkConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 1887, 1, 1, 4, 2, 1, 1, 1)
)
linkConfigEntry.setIndexNames(
    (0, "ULAF2-MIB", "linkConfigPortIndex"),
    (0, "ULAF2-MIB", "linkConfigIndex"),
)
if mibBuilder.loadTexts:
    linkConfigEntry.setStatus("mandatory")
_LinkConfigPortIndex_Type = Integer32
_LinkConfigPortIndex_Object = MibTableColumn
linkConfigPortIndex = _LinkConfigPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 1887, 1, 1, 4, 2, 1, 1, 1, 1),
    _LinkConfigPortIndex_Type()
)
linkConfigPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkConfigPortIndex.setStatus("mandatory")
_LinkConfigIndex_Type = Integer32
_LinkConfigIndex_Object = MibTableColumn
linkConfigIndex = _LinkConfigIndex_Object(
    (1, 3, 6, 1, 4, 1, 1887, 1, 1, 4, 2, 1, 1, 1, 2),
    _LinkConfigIndex_Type()
)
linkConfigIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkConfigIndex.setStatus("mandatory")


class _Performance_Type(Integer32):
    """Custom type performance based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("on", 1),
          ("off", 2))
    )


_Performance_Type.__name__ = "Integer32"
_Performance_Object = MibTableColumn
performance = _Performance_Object(
    (1, 3, 6, 1, 4, 1, 1887, 1, 1, 4, 2, 1, 1, 1, 4),
    _Performance_Type()
)
performance.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    performance.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ULAF2-MIB",
    **{"siemensCH": siemensCH,
       "lineintegrator": lineintegrator,
       "ulaf2": ulaf2,
       "proxyAgent": proxyAgent,
       "proxyAgtVers2": proxyAgtVers2,
       "agtSystem": agtSystem,
       "agtSWVersion": agtSWVersion,
       "agtDateLastPortChange": agtDateLastPortChange,
       "agtProxyFeatureFlag": agtProxyFeatureFlag,
       "agtProxyAciSupported": agtProxyAciSupported,
       "agtSerialPort": agtSerialPort,
       "agtPortNumber": agtPortNumber,
       "agtPortTable": agtPortTable,
       "agtPortEntry": agtPortEntry,
       "agtPortIndex": agtPortIndex,
       "agtPortName": agtPortName,
       "agtPortConnected": agtPortConnected,
       "agtConnectedDevice": agtConnectedDevice,
       "agtPortType": agtPortType,
       "agtPortTypeNumber": agtPortTypeNumber,
       "agtPortServerName": agtPortServerName,
       "agtPortState": agtPortState,
       "agtPortDeviceFamily": agtPortDeviceFamily,
       "agtPortTryingDevice": agtPortTryingDevice,
       "agtAlarmCountGroup": agtAlarmCountGroup,
       "agtAlarmCount": agtAlarmCount,
       "agtPortServerReset": agtPortServerReset,
       "device": device,
       "deviceVers2": deviceVers2,
       "deviceSystem": deviceSystem,
       "deviceSystemTable": deviceSystemTable,
       "deviceSystemEntry": deviceSystemEntry,
       "deviceSystemPortIndex": deviceSystemPortIndex,
       "deviceLinkNumber": deviceLinkNumber,
       "deviceSWVersion": deviceSWVersion,
       "deviceExtAlarm": deviceExtAlarm,
       "deviceDateLastLinkChange": deviceDateLastLinkChange,
       "deviceOmiFeatureFlag": deviceOmiFeatureFlag,
       "deviceLinks": deviceLinks,
       "deviceLinkTable": deviceLinkTable,
       "deviceLinkEntry": deviceLinkEntry,
       "devicePortIndex": devicePortIndex,
       "deviceLinkIndex": deviceLinkIndex,
       "deviceLinkName": deviceLinkName,
       "deviceLinkAlarm": deviceLinkAlarm,
       "deviceLinkLocalLtNt": deviceLinkLocalLtNt,
       "deviceLinkLocalId": deviceLinkLocalId,
       "deviceLinkFarId": deviceLinkFarId,
       "deviceLinkNumReg1": deviceLinkNumReg1,
       "deviceLinkNumReg2": deviceLinkNumReg2,
       "deviceLinkLocalModules": deviceLinkLocalModules,
       "deviceLinkFarModules": deviceLinkFarModules,
       "deviceLinkLocalHwFabData": deviceLinkLocalHwFabData,
       "deviceLinkFarHwFabData": deviceLinkFarHwFabData,
       "deviceLinkLocalG703FabData": deviceLinkLocalG703FabData,
       "deviceLinkLocalDataFabData": deviceLinkLocalDataFabData,
       "deviceLinkLocalFeatureFlag": deviceLinkLocalFeatureFlag,
       "deviceLinkFarFeatureFlag": deviceLinkFarFeatureFlag,
       "deviceLinkFarFeatureFlagState": deviceLinkFarFeatureFlagState,
       "deviceLinkSruFeatureFlag": deviceLinkSruFeatureFlag,
       "deviceLinkNumReg3": deviceLinkNumReg3,
       "deviceLinkNumReg4": deviceLinkNumReg4,
       "links": links,
       "linksVers2": linksVers2,
       "link": link,
       "linkConfigTable": linkConfigTable,
       "linkConfigEntry": linkConfigEntry,
       "linkConfigPortIndex": linkConfigPortIndex,
       "linkConfigIndex": linkConfigIndex,
       "performance": performance}
)
