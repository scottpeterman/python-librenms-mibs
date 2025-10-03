# SNMP MIB module (SFLOW-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\nokia\SFLOW-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 12:22:08 2025
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

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

(OwnerString,) = mibBuilder.importSymbols(
    "RMON-MIB",
    "OwnerString")

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

(ModuleCompliance,
 NotificationGroup,
 ObjectGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup",
    "ObjectGroup")

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

sFlowMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 14706, 1)
)
if mibBuilder.loadTexts:
    sFlowMIB.setRevisions(
        ("2003-10-18 00:00",
         "2003-09-24 00:00",
         "2003-04-08 00:00",
         "2002-09-17 00:00",
         "2001-07-31 00:00",
         "2001-05-01 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class SFlowDataSource(TextualConvention, ObjectIdentifier):
    status = "current"


class SFlowInstance(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )



class SFlowReceiver(TextualConvention, Integer32):
    status = "current"


# MIB Managed Objects in the order of their OIDs

_SFlowAgent_ObjectIdentity = ObjectIdentity
sFlowAgent = _SFlowAgent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14706, 1, 1)
)


class _SFlowVersion_Type(SnmpAdminString):
    """Custom type sFlowVersion based on SnmpAdminString"""
    defaultValue = OctetString("1.3;;")


_SFlowVersion_Type.__name__ = "SnmpAdminString"
_SFlowVersion_Object = MibScalar
sFlowVersion = _SFlowVersion_Object(
    (1, 3, 6, 1, 4, 1, 14706, 1, 1, 1),
    _SFlowVersion_Type()
)
sFlowVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sFlowVersion.setStatus("current")
_SFlowAgentAddressType_Type = InetAddressType
_SFlowAgentAddressType_Object = MibScalar
sFlowAgentAddressType = _SFlowAgentAddressType_Object(
    (1, 3, 6, 1, 4, 1, 14706, 1, 1, 2),
    _SFlowAgentAddressType_Type()
)
sFlowAgentAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sFlowAgentAddressType.setStatus("current")
_SFlowAgentAddress_Type = InetAddress
_SFlowAgentAddress_Object = MibScalar
sFlowAgentAddress = _SFlowAgentAddress_Object(
    (1, 3, 6, 1, 4, 1, 14706, 1, 1, 3),
    _SFlowAgentAddress_Type()
)
sFlowAgentAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sFlowAgentAddress.setStatus("current")
_SFlowRcvrTable_Object = MibTable
sFlowRcvrTable = _SFlowRcvrTable_Object(
    (1, 3, 6, 1, 4, 1, 14706, 1, 1, 4)
)
if mibBuilder.loadTexts:
    sFlowRcvrTable.setStatus("current")
_SFlowRcvrEntry_Object = MibTableRow
sFlowRcvrEntry = _SFlowRcvrEntry_Object(
    (1, 3, 6, 1, 4, 1, 14706, 1, 1, 4, 1)
)
sFlowRcvrEntry.setIndexNames(
    (0, "SFLOW-MIB", "sFlowRcvrIndex"),
)
if mibBuilder.loadTexts:
    sFlowRcvrEntry.setStatus("current")


class _SFlowRcvrIndex_Type(Integer32):
    """Custom type sFlowRcvrIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_SFlowRcvrIndex_Type.__name__ = "Integer32"
_SFlowRcvrIndex_Object = MibTableColumn
sFlowRcvrIndex = _SFlowRcvrIndex_Object(
    (1, 3, 6, 1, 4, 1, 14706, 1, 1, 4, 1, 1),
    _SFlowRcvrIndex_Type()
)
sFlowRcvrIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sFlowRcvrIndex.setStatus("current")


class _SFlowRcvrOwner_Type(OwnerString):
    """Custom type sFlowRcvrOwner based on OwnerString"""
    defaultValue = OctetString("")


_SFlowRcvrOwner_Type.__name__ = "OwnerString"
_SFlowRcvrOwner_Object = MibTableColumn
sFlowRcvrOwner = _SFlowRcvrOwner_Object(
    (1, 3, 6, 1, 4, 1, 14706, 1, 1, 4, 1, 2),
    _SFlowRcvrOwner_Type()
)
sFlowRcvrOwner.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sFlowRcvrOwner.setStatus("current")


class _SFlowRcvrTimeout_Type(Integer32):
    """Custom type sFlowRcvrTimeout based on Integer32"""
    defaultValue = 0


_SFlowRcvrTimeout_Type.__name__ = "Integer32"
_SFlowRcvrTimeout_Object = MibTableColumn
sFlowRcvrTimeout = _SFlowRcvrTimeout_Object(
    (1, 3, 6, 1, 4, 1, 14706, 1, 1, 4, 1, 3),
    _SFlowRcvrTimeout_Type()
)
sFlowRcvrTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sFlowRcvrTimeout.setStatus("current")


class _SFlowRcvrMaximumDatagramSize_Type(Integer32):
    """Custom type sFlowRcvrMaximumDatagramSize based on Integer32"""
    defaultValue = 1400


_SFlowRcvrMaximumDatagramSize_Type.__name__ = "Integer32"
_SFlowRcvrMaximumDatagramSize_Object = MibTableColumn
sFlowRcvrMaximumDatagramSize = _SFlowRcvrMaximumDatagramSize_Object(
    (1, 3, 6, 1, 4, 1, 14706, 1, 1, 4, 1, 4),
    _SFlowRcvrMaximumDatagramSize_Type()
)
sFlowRcvrMaximumDatagramSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sFlowRcvrMaximumDatagramSize.setStatus("current")


class _SFlowRcvrAddressType_Type(InetAddressType):
    """Custom type sFlowRcvrAddressType based on InetAddressType"""
    defaultValue = 1


_SFlowRcvrAddressType_Type.__name__ = "InetAddressType"
_SFlowRcvrAddressType_Object = MibTableColumn
sFlowRcvrAddressType = _SFlowRcvrAddressType_Object(
    (1, 3, 6, 1, 4, 1, 14706, 1, 1, 4, 1, 5),
    _SFlowRcvrAddressType_Type()
)
sFlowRcvrAddressType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sFlowRcvrAddressType.setStatus("current")


class _SFlowRcvrAddress_Type(InetAddress):
    """Custom type sFlowRcvrAddress based on InetAddress"""
    defaultHexValue = "00000000"


_SFlowRcvrAddress_Type.__name__ = "InetAddress"
_SFlowRcvrAddress_Object = MibTableColumn
sFlowRcvrAddress = _SFlowRcvrAddress_Object(
    (1, 3, 6, 1, 4, 1, 14706, 1, 1, 4, 1, 6),
    _SFlowRcvrAddress_Type()
)
sFlowRcvrAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sFlowRcvrAddress.setStatus("current")


class _SFlowRcvrPort_Type(Integer32):
    """Custom type sFlowRcvrPort based on Integer32"""
    defaultValue = 6343


_SFlowRcvrPort_Type.__name__ = "Integer32"
_SFlowRcvrPort_Object = MibTableColumn
sFlowRcvrPort = _SFlowRcvrPort_Object(
    (1, 3, 6, 1, 4, 1, 14706, 1, 1, 4, 1, 7),
    _SFlowRcvrPort_Type()
)
sFlowRcvrPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sFlowRcvrPort.setStatus("current")


class _SFlowRcvrDatagramVersion_Type(Integer32):
    """Custom type sFlowRcvrDatagramVersion based on Integer32"""
    defaultValue = 5


_SFlowRcvrDatagramVersion_Type.__name__ = "Integer32"
_SFlowRcvrDatagramVersion_Object = MibTableColumn
sFlowRcvrDatagramVersion = _SFlowRcvrDatagramVersion_Object(
    (1, 3, 6, 1, 4, 1, 14706, 1, 1, 4, 1, 8),
    _SFlowRcvrDatagramVersion_Type()
)
sFlowRcvrDatagramVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sFlowRcvrDatagramVersion.setStatus("current")
_SFlowFsTable_Object = MibTable
sFlowFsTable = _SFlowFsTable_Object(
    (1, 3, 6, 1, 4, 1, 14706, 1, 1, 5)
)
if mibBuilder.loadTexts:
    sFlowFsTable.setStatus("current")
_SFlowFsEntry_Object = MibTableRow
sFlowFsEntry = _SFlowFsEntry_Object(
    (1, 3, 6, 1, 4, 1, 14706, 1, 1, 5, 1)
)
sFlowFsEntry.setIndexNames(
    (0, "SFLOW-MIB", "sFlowFsDataSource"),
    (0, "SFLOW-MIB", "sFlowFsInstance"),
)
if mibBuilder.loadTexts:
    sFlowFsEntry.setStatus("current")
_SFlowFsDataSource_Type = SFlowDataSource
_SFlowFsDataSource_Object = MibTableColumn
sFlowFsDataSource = _SFlowFsDataSource_Object(
    (1, 3, 6, 1, 4, 1, 14706, 1, 1, 5, 1, 1),
    _SFlowFsDataSource_Type()
)
sFlowFsDataSource.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sFlowFsDataSource.setStatus("current")
_SFlowFsInstance_Type = SFlowInstance
_SFlowFsInstance_Object = MibTableColumn
sFlowFsInstance = _SFlowFsInstance_Object(
    (1, 3, 6, 1, 4, 1, 14706, 1, 1, 5, 1, 2),
    _SFlowFsInstance_Type()
)
sFlowFsInstance.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sFlowFsInstance.setStatus("current")


class _SFlowFsReceiver_Type(SFlowReceiver):
    """Custom type sFlowFsReceiver based on SFlowReceiver"""
    defaultValue = 0


_SFlowFsReceiver_Type.__name__ = "SFlowReceiver"
_SFlowFsReceiver_Object = MibTableColumn
sFlowFsReceiver = _SFlowFsReceiver_Object(
    (1, 3, 6, 1, 4, 1, 14706, 1, 1, 5, 1, 3),
    _SFlowFsReceiver_Type()
)
sFlowFsReceiver.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sFlowFsReceiver.setStatus("current")


class _SFlowFsPacketSamplingRate_Type(Integer32):
    """Custom type sFlowFsPacketSamplingRate based on Integer32"""
    defaultValue = 0


_SFlowFsPacketSamplingRate_Type.__name__ = "Integer32"
_SFlowFsPacketSamplingRate_Object = MibTableColumn
sFlowFsPacketSamplingRate = _SFlowFsPacketSamplingRate_Object(
    (1, 3, 6, 1, 4, 1, 14706, 1, 1, 5, 1, 4),
    _SFlowFsPacketSamplingRate_Type()
)
sFlowFsPacketSamplingRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sFlowFsPacketSamplingRate.setStatus("current")


class _SFlowFsMaximumHeaderSize_Type(Integer32):
    """Custom type sFlowFsMaximumHeaderSize based on Integer32"""
    defaultValue = 128


_SFlowFsMaximumHeaderSize_Type.__name__ = "Integer32"
_SFlowFsMaximumHeaderSize_Object = MibTableColumn
sFlowFsMaximumHeaderSize = _SFlowFsMaximumHeaderSize_Object(
    (1, 3, 6, 1, 4, 1, 14706, 1, 1, 5, 1, 5),
    _SFlowFsMaximumHeaderSize_Type()
)
sFlowFsMaximumHeaderSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sFlowFsMaximumHeaderSize.setStatus("current")
_SFlowCpTable_Object = MibTable
sFlowCpTable = _SFlowCpTable_Object(
    (1, 3, 6, 1, 4, 1, 14706, 1, 1, 6)
)
if mibBuilder.loadTexts:
    sFlowCpTable.setStatus("current")
_SFlowCpEntry_Object = MibTableRow
sFlowCpEntry = _SFlowCpEntry_Object(
    (1, 3, 6, 1, 4, 1, 14706, 1, 1, 6, 1)
)
sFlowCpEntry.setIndexNames(
    (0, "SFLOW-MIB", "sFlowCpDataSource"),
    (0, "SFLOW-MIB", "sFlowCpInstance"),
)
if mibBuilder.loadTexts:
    sFlowCpEntry.setStatus("current")
_SFlowCpDataSource_Type = SFlowDataSource
_SFlowCpDataSource_Object = MibTableColumn
sFlowCpDataSource = _SFlowCpDataSource_Object(
    (1, 3, 6, 1, 4, 1, 14706, 1, 1, 6, 1, 1),
    _SFlowCpDataSource_Type()
)
sFlowCpDataSource.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sFlowCpDataSource.setStatus("current")
_SFlowCpInstance_Type = SFlowInstance
_SFlowCpInstance_Object = MibTableColumn
sFlowCpInstance = _SFlowCpInstance_Object(
    (1, 3, 6, 1, 4, 1, 14706, 1, 1, 6, 1, 2),
    _SFlowCpInstance_Type()
)
sFlowCpInstance.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sFlowCpInstance.setStatus("current")


class _SFlowCpReceiver_Type(SFlowReceiver):
    """Custom type sFlowCpReceiver based on SFlowReceiver"""
    defaultValue = 0


_SFlowCpReceiver_Type.__name__ = "SFlowReceiver"
_SFlowCpReceiver_Object = MibTableColumn
sFlowCpReceiver = _SFlowCpReceiver_Object(
    (1, 3, 6, 1, 4, 1, 14706, 1, 1, 6, 1, 3),
    _SFlowCpReceiver_Type()
)
sFlowCpReceiver.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sFlowCpReceiver.setStatus("current")


class _SFlowCpInterval_Type(Integer32):
    """Custom type sFlowCpInterval based on Integer32"""
    defaultValue = 0


_SFlowCpInterval_Type.__name__ = "Integer32"
_SFlowCpInterval_Object = MibTableColumn
sFlowCpInterval = _SFlowCpInterval_Object(
    (1, 3, 6, 1, 4, 1, 14706, 1, 1, 6, 1, 4),
    _SFlowCpInterval_Type()
)
sFlowCpInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sFlowCpInterval.setStatus("current")
_SFlowMIBConformance_ObjectIdentity = ObjectIdentity
sFlowMIBConformance = _SFlowMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14706, 1, 2)
)
_SFlowMIBGroups_ObjectIdentity = ObjectIdentity
sFlowMIBGroups = _SFlowMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14706, 1, 2, 1)
)
_SFlowMIBCompliances_ObjectIdentity = ObjectIdentity
sFlowMIBCompliances = _SFlowMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14706, 1, 2, 2)
)

# Managed Objects groups

sFlowAgentGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 14706, 1, 2, 1, 1)
)
sFlowAgentGroup.setObjects(
      *(("SFLOW-MIB", "sFlowVersion"),
        ("SFLOW-MIB", "sFlowAgentAddressType"),
        ("SFLOW-MIB", "sFlowAgentAddress"),
        ("SFLOW-MIB", "sFlowRcvrOwner"),
        ("SFLOW-MIB", "sFlowRcvrTimeout"),
        ("SFLOW-MIB", "sFlowRcvrMaximumDatagramSize"),
        ("SFLOW-MIB", "sFlowRcvrAddressType"),
        ("SFLOW-MIB", "sFlowRcvrAddress"),
        ("SFLOW-MIB", "sFlowRcvrPort"),
        ("SFLOW-MIB", "sFlowRcvrDatagramVersion"),
        ("SFLOW-MIB", "sFlowFsReceiver"),
        ("SFLOW-MIB", "sFlowFsPacketSamplingRate"),
        ("SFLOW-MIB", "sFlowFsMaximumHeaderSize"),
        ("SFLOW-MIB", "sFlowCpReceiver"),
        ("SFLOW-MIB", "sFlowCpInterval"))
)
if mibBuilder.loadTexts:
    sFlowAgentGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

sFlowCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 14706, 1, 2, 2, 1)
)
sFlowCompliance.setObjects(
    ("SFLOW-MIB", "sFlowAgentGroup")
)
if mibBuilder.loadTexts:
    sFlowCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SFLOW-MIB",
    **{"SFlowDataSource": SFlowDataSource,
       "SFlowInstance": SFlowInstance,
       "SFlowReceiver": SFlowReceiver,
       "sFlowMIB": sFlowMIB,
       "sFlowAgent": sFlowAgent,
       "sFlowVersion": sFlowVersion,
       "sFlowAgentAddressType": sFlowAgentAddressType,
       "sFlowAgentAddress": sFlowAgentAddress,
       "sFlowRcvrTable": sFlowRcvrTable,
       "sFlowRcvrEntry": sFlowRcvrEntry,
       "sFlowRcvrIndex": sFlowRcvrIndex,
       "sFlowRcvrOwner": sFlowRcvrOwner,
       "sFlowRcvrTimeout": sFlowRcvrTimeout,
       "sFlowRcvrMaximumDatagramSize": sFlowRcvrMaximumDatagramSize,
       "sFlowRcvrAddressType": sFlowRcvrAddressType,
       "sFlowRcvrAddress": sFlowRcvrAddress,
       "sFlowRcvrPort": sFlowRcvrPort,
       "sFlowRcvrDatagramVersion": sFlowRcvrDatagramVersion,
       "sFlowFsTable": sFlowFsTable,
       "sFlowFsEntry": sFlowFsEntry,
       "sFlowFsDataSource": sFlowFsDataSource,
       "sFlowFsInstance": sFlowFsInstance,
       "sFlowFsReceiver": sFlowFsReceiver,
       "sFlowFsPacketSamplingRate": sFlowFsPacketSamplingRate,
       "sFlowFsMaximumHeaderSize": sFlowFsMaximumHeaderSize,
       "sFlowCpTable": sFlowCpTable,
       "sFlowCpEntry": sFlowCpEntry,
       "sFlowCpDataSource": sFlowCpDataSource,
       "sFlowCpInstance": sFlowCpInstance,
       "sFlowCpReceiver": sFlowCpReceiver,
       "sFlowCpInterval": sFlowCpInterval,
       "sFlowMIBConformance": sFlowMIBConformance,
       "sFlowMIBGroups": sFlowMIBGroups,
       "sFlowAgentGroup": sFlowAgentGroup,
       "sFlowMIBCompliances": sFlowMIBCompliances,
       "sFlowCompliance": sFlowCompliance}
)
