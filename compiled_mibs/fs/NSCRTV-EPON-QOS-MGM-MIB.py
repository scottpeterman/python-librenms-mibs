# SNMP MIB module (NSCRTV-EPON-QOS-MGM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\fs\NSCRTV-EPON-QOS-MGM-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:46:54 2025
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

(AutoNegotiationTechAbility,
 EponAlarmCode,
 EponAlarmInstance,
 EponCardIndex,
 EponDeviceIndex,
 EponPortIndex,
 EponSeverityType,
 EponStats15MinRecordType,
 EponStats24HourRecordType,
 EponStatsThresholdType,
 TAddress,
 qosManagementObjects) = mibBuilder.importSymbols(
    "NSCRTV-EPONEOC-EPON-MIB",
    "AutoNegotiationTechAbility",
    "EponAlarmCode",
    "EponAlarmInstance",
    "EponCardIndex",
    "EponDeviceIndex",
    "EponPortIndex",
    "EponSeverityType",
    "EponStats15MinRecordType",
    "EponStats24HourRecordType",
    "EponStatsThresholdType",
    "TAddress",
    "qosManagementObjects")

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
    "iso")

(DateAndTime,
 DisplayString,
 MacAddress,
 PhysAddress,
 RowStatus,
 TextualConvention,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_QosGlobalSetTable_Object = MibTable
qosGlobalSetTable = _QosGlobalSetTable_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 8, 1)
)
if mibBuilder.loadTexts:
    qosGlobalSetTable.setStatus("current")
_QosGlobalSetEntry_Object = MibTableRow
qosGlobalSetEntry = _QosGlobalSetEntry_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 8, 1, 1)
)
qosGlobalSetEntry.setIndexNames(
    (0, "NSCRTV-EPON-QOS-MGM-MIB", "qosGlobalSetDeviceIndex"),
)
if mibBuilder.loadTexts:
    qosGlobalSetEntry.setStatus("current")
_QosGlobalSetDeviceIndex_Type = EponDeviceIndex
_QosGlobalSetDeviceIndex_Object = MibTableColumn
qosGlobalSetDeviceIndex = _QosGlobalSetDeviceIndex_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 8, 1, 1, 1),
    _QosGlobalSetDeviceIndex_Type()
)
qosGlobalSetDeviceIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    qosGlobalSetDeviceIndex.setStatus("current")


class _QosGlobalSetMaxQueueCount_Type(Integer32):
    """Custom type qosGlobalSetMaxQueueCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 256),
    )


_QosGlobalSetMaxQueueCount_Type.__name__ = "Integer32"
_QosGlobalSetMaxQueueCount_Object = MibTableColumn
qosGlobalSetMaxQueueCount = _QosGlobalSetMaxQueueCount_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 8, 1, 1, 2),
    _QosGlobalSetMaxQueueCount_Type()
)
qosGlobalSetMaxQueueCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qosGlobalSetMaxQueueCount.setStatus("current")


class _QosGlobalSetMode_Type(Integer32):
    """Custom type qosGlobalSetMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("deviceBased", 1),
          ("portBased", 2))
    )


_QosGlobalSetMode_Type.__name__ = "Integer32"
_QosGlobalSetMode_Object = MibTableColumn
qosGlobalSetMode = _QosGlobalSetMode_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 8, 1, 1, 3),
    _QosGlobalSetMode_Type()
)
qosGlobalSetMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosGlobalSetMode.setStatus("current")
_DeviceBaseQosMapTable_Object = MibTable
deviceBaseQosMapTable = _DeviceBaseQosMapTable_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 8, 2)
)
if mibBuilder.loadTexts:
    deviceBaseQosMapTable.setStatus("current")
_DeviceBaseQosMapEntry_Object = MibTableRow
deviceBaseQosMapEntry = _DeviceBaseQosMapEntry_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 8, 2, 1)
)
deviceBaseQosMapEntry.setIndexNames(
    (0, "NSCRTV-EPON-QOS-MGM-MIB", "deviceBaseQosMapDeviceIndex"),
    (0, "NSCRTV-EPON-QOS-MGM-MIB", "deviceBaseQosMapRuleIndex"),
)
if mibBuilder.loadTexts:
    deviceBaseQosMapEntry.setStatus("current")
_DeviceBaseQosMapDeviceIndex_Type = EponDeviceIndex
_DeviceBaseQosMapDeviceIndex_Object = MibTableColumn
deviceBaseQosMapDeviceIndex = _DeviceBaseQosMapDeviceIndex_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 8, 2, 1, 1),
    _DeviceBaseQosMapDeviceIndex_Type()
)
deviceBaseQosMapDeviceIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    deviceBaseQosMapDeviceIndex.setStatus("current")


class _DeviceBaseQosMapRuleIndex_Type(Integer32):
    """Custom type deviceBaseQosMapRuleIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("cos", 1),
          ("tos", 2),
          ("diffserv", 3))
    )


_DeviceBaseQosMapRuleIndex_Type.__name__ = "Integer32"
_DeviceBaseQosMapRuleIndex_Object = MibTableColumn
deviceBaseQosMapRuleIndex = _DeviceBaseQosMapRuleIndex_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 8, 2, 1, 2),
    _DeviceBaseQosMapRuleIndex_Type()
)
deviceBaseQosMapRuleIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    deviceBaseQosMapRuleIndex.setStatus("current")


class _DeviceBaseQosMapOctet_Type(OctetString):
    """Custom type deviceBaseQosMapOctet based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
        ValueSizeConstraint(64, 64),
    )


_DeviceBaseQosMapOctet_Type.__name__ = "OctetString"
_DeviceBaseQosMapOctet_Object = MibTableColumn
deviceBaseQosMapOctet = _DeviceBaseQosMapOctet_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 8, 2, 1, 3),
    _DeviceBaseQosMapOctet_Type()
)
deviceBaseQosMapOctet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    deviceBaseQosMapOctet.setStatus("current")
_DeviceBaseQosPolicyTable_Object = MibTable
deviceBaseQosPolicyTable = _DeviceBaseQosPolicyTable_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 8, 3)
)
if mibBuilder.loadTexts:
    deviceBaseQosPolicyTable.setStatus("current")
_DeviceBaseQosPolicyEntry_Object = MibTableRow
deviceBaseQosPolicyEntry = _DeviceBaseQosPolicyEntry_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 8, 3, 1)
)
deviceBaseQosPolicyEntry.setIndexNames(
    (0, "NSCRTV-EPON-QOS-MGM-MIB", "deviceBaseQosPolicyDeviceIndex"),
)
if mibBuilder.loadTexts:
    deviceBaseQosPolicyEntry.setStatus("current")
_DeviceBaseQosPolicyDeviceIndex_Type = EponDeviceIndex
_DeviceBaseQosPolicyDeviceIndex_Object = MibTableColumn
deviceBaseQosPolicyDeviceIndex = _DeviceBaseQosPolicyDeviceIndex_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 8, 3, 1, 1),
    _DeviceBaseQosPolicyDeviceIndex_Type()
)
deviceBaseQosPolicyDeviceIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    deviceBaseQosPolicyDeviceIndex.setStatus("current")


class _DeviceBaseQosPolicyMode_Type(Integer32):
    """Custom type deviceBaseQosPolicyMode based on Integer32"""
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
        *(("sp", 1),
          ("wrr", 2),
          ("spWrr", 3),
          ("wfp", 4))
    )


_DeviceBaseQosPolicyMode_Type.__name__ = "Integer32"
_DeviceBaseQosPolicyMode_Object = MibTableColumn
deviceBaseQosPolicyMode = _DeviceBaseQosPolicyMode_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 8, 3, 1, 2),
    _DeviceBaseQosPolicyMode_Type()
)
deviceBaseQosPolicyMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    deviceBaseQosPolicyMode.setStatus("current")
_DeviceBaseQosPolicyWeightOctet_Type = OctetString
_DeviceBaseQosPolicyWeightOctet_Object = MibTableColumn
deviceBaseQosPolicyWeightOctet = _DeviceBaseQosPolicyWeightOctet_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 8, 3, 1, 3),
    _DeviceBaseQosPolicyWeightOctet_Type()
)
deviceBaseQosPolicyWeightOctet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    deviceBaseQosPolicyWeightOctet.setStatus("current")
_DeviceBaseQosPolicySpBandwidthRange_Type = OctetString
_DeviceBaseQosPolicySpBandwidthRange_Object = MibTableColumn
deviceBaseQosPolicySpBandwidthRange = _DeviceBaseQosPolicySpBandwidthRange_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 8, 3, 1, 4),
    _DeviceBaseQosPolicySpBandwidthRange_Type()
)
deviceBaseQosPolicySpBandwidthRange.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    deviceBaseQosPolicySpBandwidthRange.setStatus("current")
_PortBaseQosMapTable_Object = MibTable
portBaseQosMapTable = _PortBaseQosMapTable_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 8, 4)
)
if mibBuilder.loadTexts:
    portBaseQosMapTable.setStatus("current")
_PortBaseQosMapEntry_Object = MibTableRow
portBaseQosMapEntry = _PortBaseQosMapEntry_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 8, 4, 1)
)
portBaseQosMapEntry.setIndexNames(
    (0, "NSCRTV-EPON-QOS-MGM-MIB", "deviceBaseQosMapDeviceIndex"),
    (0, "NSCRTV-EPON-QOS-MGM-MIB", "portBaseQosMapCardIndex"),
    (0, "NSCRTV-EPON-QOS-MGM-MIB", "portBaseQosMapPortIndex"),
    (0, "NSCRTV-EPON-QOS-MGM-MIB", "deviceBaseQosMapRuleIndex"),
)
if mibBuilder.loadTexts:
    portBaseQosMapEntry.setStatus("current")
_PortBaseQosMapDeviceIndex_Type = EponDeviceIndex
_PortBaseQosMapDeviceIndex_Object = MibTableColumn
portBaseQosMapDeviceIndex = _PortBaseQosMapDeviceIndex_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 8, 4, 1, 1),
    _PortBaseQosMapDeviceIndex_Type()
)
portBaseQosMapDeviceIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    portBaseQosMapDeviceIndex.setStatus("current")
_PortBaseQosMapCardIndex_Type = EponPortIndex
_PortBaseQosMapCardIndex_Object = MibTableColumn
portBaseQosMapCardIndex = _PortBaseQosMapCardIndex_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 8, 4, 1, 2),
    _PortBaseQosMapCardIndex_Type()
)
portBaseQosMapCardIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    portBaseQosMapCardIndex.setStatus("current")
_PortBaseQosMapPortIndex_Type = EponPortIndex
_PortBaseQosMapPortIndex_Object = MibTableColumn
portBaseQosMapPortIndex = _PortBaseQosMapPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 8, 4, 1, 3),
    _PortBaseQosMapPortIndex_Type()
)
portBaseQosMapPortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    portBaseQosMapPortIndex.setStatus("current")


class _PortBaseQosMapRuleIndex_Type(Integer32):
    """Custom type portBaseQosMapRuleIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("cos", 1),
          ("tos", 2),
          ("diffserv", 3))
    )


_PortBaseQosMapRuleIndex_Type.__name__ = "Integer32"
_PortBaseQosMapRuleIndex_Object = MibTableColumn
portBaseQosMapRuleIndex = _PortBaseQosMapRuleIndex_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 8, 4, 1, 4),
    _PortBaseQosMapRuleIndex_Type()
)
portBaseQosMapRuleIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    portBaseQosMapRuleIndex.setStatus("current")


class _PortBaseQosMapOctet_Type(OctetString):
    """Custom type portBaseQosMapOctet based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 64),
    )


_PortBaseQosMapOctet_Type.__name__ = "OctetString"
_PortBaseQosMapOctet_Object = MibTableColumn
portBaseQosMapOctet = _PortBaseQosMapOctet_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 8, 4, 1, 5),
    _PortBaseQosMapOctet_Type()
)
portBaseQosMapOctet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portBaseQosMapOctet.setStatus("current")
_PortBaseQosPolicyTable_Object = MibTable
portBaseQosPolicyTable = _PortBaseQosPolicyTable_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 8, 5)
)
if mibBuilder.loadTexts:
    portBaseQosPolicyTable.setStatus("current")
_PortBaseQosPolicyEntry_Object = MibTableRow
portBaseQosPolicyEntry = _PortBaseQosPolicyEntry_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 8, 5, 1)
)
portBaseQosPolicyEntry.setIndexNames(
    (0, "NSCRTV-EPON-QOS-MGM-MIB", "deviceBaseQosPolicyDeviceIndex"),
    (0, "NSCRTV-EPON-QOS-MGM-MIB", "portBaseQosPolicyCardIndex"),
    (0, "NSCRTV-EPON-QOS-MGM-MIB", "portBaseQosPolicyPortIndex"),
)
if mibBuilder.loadTexts:
    portBaseQosPolicyEntry.setStatus("current")
_PortBaseQosPolicyDeviceIndex_Type = EponDeviceIndex
_PortBaseQosPolicyDeviceIndex_Object = MibTableColumn
portBaseQosPolicyDeviceIndex = _PortBaseQosPolicyDeviceIndex_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 8, 5, 1, 1),
    _PortBaseQosPolicyDeviceIndex_Type()
)
portBaseQosPolicyDeviceIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    portBaseQosPolicyDeviceIndex.setStatus("current")
_PortBaseQosPolicyCardIndex_Type = EponPortIndex
_PortBaseQosPolicyCardIndex_Object = MibTableColumn
portBaseQosPolicyCardIndex = _PortBaseQosPolicyCardIndex_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 8, 5, 1, 2),
    _PortBaseQosPolicyCardIndex_Type()
)
portBaseQosPolicyCardIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    portBaseQosPolicyCardIndex.setStatus("current")
_PortBaseQosPolicyPortIndex_Type = EponPortIndex
_PortBaseQosPolicyPortIndex_Object = MibTableColumn
portBaseQosPolicyPortIndex = _PortBaseQosPolicyPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 8, 5, 1, 3),
    _PortBaseQosPolicyPortIndex_Type()
)
portBaseQosPolicyPortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    portBaseQosPolicyPortIndex.setStatus("current")


class _PortBaseQosPolicyMode_Type(Integer32):
    """Custom type portBaseQosPolicyMode based on Integer32"""
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
        *(("sp", 1),
          ("wrr", 2),
          ("spWrr", 3),
          ("wfp", 4))
    )


_PortBaseQosPolicyMode_Type.__name__ = "Integer32"
_PortBaseQosPolicyMode_Object = MibTableColumn
portBaseQosPolicyMode = _PortBaseQosPolicyMode_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 8, 5, 1, 4),
    _PortBaseQosPolicyMode_Type()
)
portBaseQosPolicyMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portBaseQosPolicyMode.setStatus("current")


class _PortBaseQosPolicyWeightOctet_Type(OctetString):
    """Custom type portBaseQosPolicyWeightOctet based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 256),
    )


_PortBaseQosPolicyWeightOctet_Type.__name__ = "OctetString"
_PortBaseQosPolicyWeightOctet_Object = MibTableColumn
portBaseQosPolicyWeightOctet = _PortBaseQosPolicyWeightOctet_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 8, 5, 1, 5),
    _PortBaseQosPolicyWeightOctet_Type()
)
portBaseQosPolicyWeightOctet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portBaseQosPolicyWeightOctet.setStatus("current")
_PortBaseQosPolicySpBandwidthRange_Type = OctetString
_PortBaseQosPolicySpBandwidthRange_Object = MibTableColumn
portBaseQosPolicySpBandwidthRange = _PortBaseQosPolicySpBandwidthRange_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 8, 5, 1, 6),
    _PortBaseQosPolicySpBandwidthRange_Type()
)
portBaseQosPolicySpBandwidthRange.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portBaseQosPolicySpBandwidthRange.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "NSCRTV-EPON-QOS-MGM-MIB",
    **{"qosGlobalSetTable": qosGlobalSetTable,
       "qosGlobalSetEntry": qosGlobalSetEntry,
       "qosGlobalSetDeviceIndex": qosGlobalSetDeviceIndex,
       "qosGlobalSetMaxQueueCount": qosGlobalSetMaxQueueCount,
       "qosGlobalSetMode": qosGlobalSetMode,
       "deviceBaseQosMapTable": deviceBaseQosMapTable,
       "deviceBaseQosMapEntry": deviceBaseQosMapEntry,
       "deviceBaseQosMapDeviceIndex": deviceBaseQosMapDeviceIndex,
       "deviceBaseQosMapRuleIndex": deviceBaseQosMapRuleIndex,
       "deviceBaseQosMapOctet": deviceBaseQosMapOctet,
       "deviceBaseQosPolicyTable": deviceBaseQosPolicyTable,
       "deviceBaseQosPolicyEntry": deviceBaseQosPolicyEntry,
       "deviceBaseQosPolicyDeviceIndex": deviceBaseQosPolicyDeviceIndex,
       "deviceBaseQosPolicyMode": deviceBaseQosPolicyMode,
       "deviceBaseQosPolicyWeightOctet": deviceBaseQosPolicyWeightOctet,
       "deviceBaseQosPolicySpBandwidthRange": deviceBaseQosPolicySpBandwidthRange,
       "portBaseQosMapTable": portBaseQosMapTable,
       "portBaseQosMapEntry": portBaseQosMapEntry,
       "portBaseQosMapDeviceIndex": portBaseQosMapDeviceIndex,
       "portBaseQosMapCardIndex": portBaseQosMapCardIndex,
       "portBaseQosMapPortIndex": portBaseQosMapPortIndex,
       "portBaseQosMapRuleIndex": portBaseQosMapRuleIndex,
       "portBaseQosMapOctet": portBaseQosMapOctet,
       "portBaseQosPolicyTable": portBaseQosPolicyTable,
       "portBaseQosPolicyEntry": portBaseQosPolicyEntry,
       "portBaseQosPolicyDeviceIndex": portBaseQosPolicyDeviceIndex,
       "portBaseQosPolicyCardIndex": portBaseQosPolicyCardIndex,
       "portBaseQosPolicyPortIndex": portBaseQosPolicyPortIndex,
       "portBaseQosPolicyMode": portBaseQosPolicyMode,
       "portBaseQosPolicyWeightOctet": portBaseQosPolicyWeightOctet,
       "portBaseQosPolicySpBandwidthRange": portBaseQosPolicySpBandwidthRange}
)
