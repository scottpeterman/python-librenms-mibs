# SNMP MIB module (DLINKSW-SFLOW-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\dlink\DLINKSW-SFLOW-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:37:50 2025
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

(dlinkIndustrialCommon,) = mibBuilder.importSymbols(
    "DLINK-ID-REC-MIB",
    "dlinkIndustrialCommon")

(InetAddress,
 InetAddressIPv4,
 InetAddressIPv6,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressIPv4",
    "InetAddressIPv6",
    "InetAddressType")

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

(DisplayString,
 PhysAddress,
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

dlinkSwSFlowMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 36)
)
if mibBuilder.loadTexts:
    dlinkSwSFlowMIB.setRevisions(
        ("2013-04-10 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class DSFlowDataSource(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )



class DSFlowInstance(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )



class DSFlowReceiver(TextualConvention, Integer32):
    status = "current"


# MIB Managed Objects in the order of their OIDs

_DSFlowMIBNotifications_ObjectIdentity = ObjectIdentity
dSFlowMIBNotifications = _DSFlowMIBNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 36, 0)
)
_DSFlowMIBObjects_ObjectIdentity = ObjectIdentity
dSFlowMIBObjects = _DSFlowMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 36, 1)
)


class _DSFlowVersion_Type(SnmpAdminString):
    """Custom type dSFlowVersion based on SnmpAdminString"""
    defaultValue = OctetString("1.3;;")


_DSFlowVersion_Type.__name__ = "SnmpAdminString"
_DSFlowVersion_Object = MibScalar
dSFlowVersion = _DSFlowVersion_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 36, 1, 1),
    _DSFlowVersion_Type()
)
dSFlowVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dSFlowVersion.setStatus("current")
_DSFlowAgentAddressIPv4_Type = InetAddressIPv4
_DSFlowAgentAddressIPv4_Object = MibScalar
dSFlowAgentAddressIPv4 = _DSFlowAgentAddressIPv4_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 36, 1, 2),
    _DSFlowAgentAddressIPv4_Type()
)
dSFlowAgentAddressIPv4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dSFlowAgentAddressIPv4.setStatus("current")
_DSFlowAgentAddressIPv6_Type = InetAddressIPv6
_DSFlowAgentAddressIPv6_Object = MibScalar
dSFlowAgentAddressIPv6 = _DSFlowAgentAddressIPv6_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 36, 1, 3),
    _DSFlowAgentAddressIPv6_Type()
)
dSFlowAgentAddressIPv6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dSFlowAgentAddressIPv6.setStatus("current")
_DSFlowRcvrTable_Object = MibTable
dSFlowRcvrTable = _DSFlowRcvrTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 36, 1, 4)
)
if mibBuilder.loadTexts:
    dSFlowRcvrTable.setStatus("current")
_DSFlowRcvrEntry_Object = MibTableRow
dSFlowRcvrEntry = _DSFlowRcvrEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 36, 1, 4, 1)
)
dSFlowRcvrEntry.setIndexNames(
    (0, "DLINKSW-SFLOW-MIB", "dSFlowRcvrIndex"),
)
if mibBuilder.loadTexts:
    dSFlowRcvrEntry.setStatus("current")


class _DSFlowRcvrIndex_Type(Integer32):
    """Custom type dSFlowRcvrIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_DSFlowRcvrIndex_Type.__name__ = "Integer32"
_DSFlowRcvrIndex_Object = MibTableColumn
dSFlowRcvrIndex = _DSFlowRcvrIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 36, 1, 4, 1, 1),
    _DSFlowRcvrIndex_Type()
)
dSFlowRcvrIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dSFlowRcvrIndex.setStatus("current")


class _DSFlowRcvrOwner_Type(DisplayString):
    """Custom type dSFlowRcvrOwner based on DisplayString"""
    defaultValue = OctetString("")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_DSFlowRcvrOwner_Type.__name__ = "DisplayString"
_DSFlowRcvrOwner_Object = MibTableColumn
dSFlowRcvrOwner = _DSFlowRcvrOwner_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 36, 1, 4, 1, 2),
    _DSFlowRcvrOwner_Type()
)
dSFlowRcvrOwner.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dSFlowRcvrOwner.setStatus("current")


class _DSFlowRcvrAdminTimeout_Type(Integer32):
    """Custom type dSFlowRcvrAdminTimeout based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2000000),
    )


_DSFlowRcvrAdminTimeout_Type.__name__ = "Integer32"
_DSFlowRcvrAdminTimeout_Object = MibTableColumn
dSFlowRcvrAdminTimeout = _DSFlowRcvrAdminTimeout_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 36, 1, 4, 1, 3),
    _DSFlowRcvrAdminTimeout_Type()
)
dSFlowRcvrAdminTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dSFlowRcvrAdminTimeout.setStatus("current")


class _DSFlowRcvrCurrentTimeout_Type(Integer32):
    """Custom type dSFlowRcvrCurrentTimeout based on Integer32"""
    defaultValue = 0


_DSFlowRcvrCurrentTimeout_Type.__name__ = "Integer32"
_DSFlowRcvrCurrentTimeout_Object = MibTableColumn
dSFlowRcvrCurrentTimeout = _DSFlowRcvrCurrentTimeout_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 36, 1, 4, 1, 4),
    _DSFlowRcvrCurrentTimeout_Type()
)
dSFlowRcvrCurrentTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dSFlowRcvrCurrentTimeout.setStatus("current")


class _DSFlowRcvrMaximumDatagramSize_Type(Integer32):
    """Custom type dSFlowRcvrMaximumDatagramSize based on Integer32"""
    defaultValue = 1400

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(700, 1400),
    )


_DSFlowRcvrMaximumDatagramSize_Type.__name__ = "Integer32"
_DSFlowRcvrMaximumDatagramSize_Object = MibTableColumn
dSFlowRcvrMaximumDatagramSize = _DSFlowRcvrMaximumDatagramSize_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 36, 1, 4, 1, 5),
    _DSFlowRcvrMaximumDatagramSize_Type()
)
dSFlowRcvrMaximumDatagramSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dSFlowRcvrMaximumDatagramSize.setStatus("current")


class _DSFlowRcvrAddressType_Type(InetAddressType):
    """Custom type dSFlowRcvrAddressType based on InetAddressType"""
    defaultValue = 1


_DSFlowRcvrAddressType_Type.__name__ = "InetAddressType"
_DSFlowRcvrAddressType_Object = MibTableColumn
dSFlowRcvrAddressType = _DSFlowRcvrAddressType_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 36, 1, 4, 1, 6),
    _DSFlowRcvrAddressType_Type()
)
dSFlowRcvrAddressType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dSFlowRcvrAddressType.setStatus("current")


class _DSFlowRcvrAddress_Type(InetAddress):
    """Custom type dSFlowRcvrAddress based on InetAddress"""
    defaultHexValue = "00000000"


_DSFlowRcvrAddress_Type.__name__ = "InetAddress"
_DSFlowRcvrAddress_Object = MibTableColumn
dSFlowRcvrAddress = _DSFlowRcvrAddress_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 36, 1, 4, 1, 7),
    _DSFlowRcvrAddress_Type()
)
dSFlowRcvrAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dSFlowRcvrAddress.setStatus("current")


class _DSFlowRcvrVrfName_Type(DisplayString):
    """Custom type dSFlowRcvrVrfName based on DisplayString"""
    defaultValue = OctetString("")


_DSFlowRcvrVrfName_Type.__name__ = "DisplayString"
_DSFlowRcvrVrfName_Object = MibTableColumn
dSFlowRcvrVrfName = _DSFlowRcvrVrfName_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 36, 1, 4, 1, 8),
    _DSFlowRcvrVrfName_Type()
)
dSFlowRcvrVrfName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dSFlowRcvrVrfName.setStatus("current")


class _DSFlowRcvrPort_Type(Integer32):
    """Custom type dSFlowRcvrPort based on Integer32"""
    defaultValue = 6343

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_DSFlowRcvrPort_Type.__name__ = "Integer32"
_DSFlowRcvrPort_Object = MibTableColumn
dSFlowRcvrPort = _DSFlowRcvrPort_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 36, 1, 4, 1, 9),
    _DSFlowRcvrPort_Type()
)
dSFlowRcvrPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dSFlowRcvrPort.setStatus("current")


class _DSFlowRcvrDatagramVersion_Type(Integer32):
    """Custom type dSFlowRcvrDatagramVersion based on Integer32"""
    defaultValue = 5


_DSFlowRcvrDatagramVersion_Type.__name__ = "Integer32"
_DSFlowRcvrDatagramVersion_Object = MibTableColumn
dSFlowRcvrDatagramVersion = _DSFlowRcvrDatagramVersion_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 36, 1, 4, 1, 10),
    _DSFlowRcvrDatagramVersion_Type()
)
dSFlowRcvrDatagramVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dSFlowRcvrDatagramVersion.setStatus("current")


class _DSFlowRcvrReset_Type(Integer32):
    """Custom type dSFlowRcvrReset based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("reset", 1),
          ("noOp", 2))
    )


_DSFlowRcvrReset_Type.__name__ = "Integer32"
_DSFlowRcvrReset_Object = MibTableColumn
dSFlowRcvrReset = _DSFlowRcvrReset_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 36, 1, 4, 1, 11),
    _DSFlowRcvrReset_Type()
)
dSFlowRcvrReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dSFlowRcvrReset.setStatus("current")
_DSFlowFsTable_Object = MibTable
dSFlowFsTable = _DSFlowFsTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 36, 1, 5)
)
if mibBuilder.loadTexts:
    dSFlowFsTable.setStatus("current")
_DSFlowFsEntry_Object = MibTableRow
dSFlowFsEntry = _DSFlowFsEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 36, 1, 5, 1)
)
dSFlowFsEntry.setIndexNames(
    (0, "DLINKSW-SFLOW-MIB", "dSFlowFsDataSource"),
    (0, "DLINKSW-SFLOW-MIB", "dSFlowFsInstance"),
)
if mibBuilder.loadTexts:
    dSFlowFsEntry.setStatus("current")
_DSFlowFsDataSource_Type = DSFlowDataSource
_DSFlowFsDataSource_Object = MibTableColumn
dSFlowFsDataSource = _DSFlowFsDataSource_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 36, 1, 5, 1, 1),
    _DSFlowFsDataSource_Type()
)
dSFlowFsDataSource.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dSFlowFsDataSource.setStatus("current")
_DSFlowFsInstance_Type = DSFlowInstance
_DSFlowFsInstance_Object = MibTableColumn
dSFlowFsInstance = _DSFlowFsInstance_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 36, 1, 5, 1, 2),
    _DSFlowFsInstance_Type()
)
dSFlowFsInstance.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dSFlowFsInstance.setStatus("current")


class _DSFlowFsReceiver_Type(DSFlowReceiver):
    """Custom type dSFlowFsReceiver based on DSFlowReceiver"""
    defaultValue = 0


_DSFlowFsReceiver_Type.__name__ = "DSFlowReceiver"
_DSFlowFsReceiver_Object = MibTableColumn
dSFlowFsReceiver = _DSFlowFsReceiver_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 36, 1, 5, 1, 3),
    _DSFlowFsReceiver_Type()
)
dSFlowFsReceiver.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dSFlowFsReceiver.setStatus("current")


class _DSFlowFsDirection_Type(Integer32):
    """Custom type dSFlowFsDirection based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("inbound", 1),
          ("outbound", 2))
    )


_DSFlowFsDirection_Type.__name__ = "Integer32"
_DSFlowFsDirection_Object = MibTableColumn
dSFlowFsDirection = _DSFlowFsDirection_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 36, 1, 5, 1, 4),
    _DSFlowFsDirection_Type()
)
dSFlowFsDirection.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dSFlowFsDirection.setStatus("current")


class _DSFlowFsAdminSamplingRate_Type(Integer32):
    """Custom type dSFlowFsAdminSamplingRate based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_DSFlowFsAdminSamplingRate_Type.__name__ = "Integer32"
_DSFlowFsAdminSamplingRate_Object = MibTableColumn
dSFlowFsAdminSamplingRate = _DSFlowFsAdminSamplingRate_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 36, 1, 5, 1, 5),
    _DSFlowFsAdminSamplingRate_Type()
)
dSFlowFsAdminSamplingRate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dSFlowFsAdminSamplingRate.setStatus("current")


class _DSFlowFsActiveSamplingRate_Type(Integer32):
    """Custom type dSFlowFsActiveSamplingRate based on Integer32"""
    defaultValue = 0


_DSFlowFsActiveSamplingRate_Type.__name__ = "Integer32"
_DSFlowFsActiveSamplingRate_Object = MibTableColumn
dSFlowFsActiveSamplingRate = _DSFlowFsActiveSamplingRate_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 36, 1, 5, 1, 6),
    _DSFlowFsActiveSamplingRate_Type()
)
dSFlowFsActiveSamplingRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dSFlowFsActiveSamplingRate.setStatus("current")


class _DSFlowFsMaximumHeaderSize_Type(Integer32):
    """Custom type dSFlowFsMaximumHeaderSize based on Integer32"""
    defaultValue = 128

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(18, 256),
    )


_DSFlowFsMaximumHeaderSize_Type.__name__ = "Integer32"
_DSFlowFsMaximumHeaderSize_Object = MibTableColumn
dSFlowFsMaximumHeaderSize = _DSFlowFsMaximumHeaderSize_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 36, 1, 5, 1, 7),
    _DSFlowFsMaximumHeaderSize_Type()
)
dSFlowFsMaximumHeaderSize.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dSFlowFsMaximumHeaderSize.setStatus("current")
_DSFlowFsRowStatus_Type = RowStatus
_DSFlowFsRowStatus_Object = MibTableColumn
dSFlowFsRowStatus = _DSFlowFsRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 36, 1, 5, 1, 8),
    _DSFlowFsRowStatus_Type()
)
dSFlowFsRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dSFlowFsRowStatus.setStatus("current")
_DSFlowCpTable_Object = MibTable
dSFlowCpTable = _DSFlowCpTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 36, 1, 6)
)
if mibBuilder.loadTexts:
    dSFlowCpTable.setStatus("current")
_DSFlowCpEntry_Object = MibTableRow
dSFlowCpEntry = _DSFlowCpEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 36, 1, 6, 1)
)
dSFlowCpEntry.setIndexNames(
    (0, "DLINKSW-SFLOW-MIB", "dSFlowCpDataSource"),
    (0, "DLINKSW-SFLOW-MIB", "dSFlowCpInstance"),
)
if mibBuilder.loadTexts:
    dSFlowCpEntry.setStatus("current")
_DSFlowCpDataSource_Type = DSFlowDataSource
_DSFlowCpDataSource_Object = MibTableColumn
dSFlowCpDataSource = _DSFlowCpDataSource_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 36, 1, 6, 1, 1),
    _DSFlowCpDataSource_Type()
)
dSFlowCpDataSource.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dSFlowCpDataSource.setStatus("current")
_DSFlowCpInstance_Type = DSFlowInstance
_DSFlowCpInstance_Object = MibTableColumn
dSFlowCpInstance = _DSFlowCpInstance_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 36, 1, 6, 1, 2),
    _DSFlowCpInstance_Type()
)
dSFlowCpInstance.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dSFlowCpInstance.setStatus("current")


class _DSFlowCpReceiver_Type(DSFlowReceiver):
    """Custom type dSFlowCpReceiver based on DSFlowReceiver"""
    defaultValue = 0


_DSFlowCpReceiver_Type.__name__ = "DSFlowReceiver"
_DSFlowCpReceiver_Object = MibTableColumn
dSFlowCpReceiver = _DSFlowCpReceiver_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 36, 1, 6, 1, 3),
    _DSFlowCpReceiver_Type()
)
dSFlowCpReceiver.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dSFlowCpReceiver.setStatus("current")


class _DSFlowCpInterval_Type(Integer32):
    """Custom type dSFlowCpInterval based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 120),
    )


_DSFlowCpInterval_Type.__name__ = "Integer32"
_DSFlowCpInterval_Object = MibTableColumn
dSFlowCpInterval = _DSFlowCpInterval_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 36, 1, 6, 1, 4),
    _DSFlowCpInterval_Type()
)
dSFlowCpInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dSFlowCpInterval.setStatus("current")
_DSFlowCpRowStatus_Type = RowStatus
_DSFlowCpRowStatus_Object = MibTableColumn
dSFlowCpRowStatus = _DSFlowCpRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 36, 1, 6, 1, 5),
    _DSFlowCpRowStatus_Type()
)
dSFlowCpRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dSFlowCpRowStatus.setStatus("current")
_DSFlowMIBConformance_ObjectIdentity = ObjectIdentity
dSFlowMIBConformance = _DSFlowMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 36, 2)
)
_DSFlowMIBCompliances_ObjectIdentity = ObjectIdentity
dSFlowMIBCompliances = _DSFlowMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 36, 2, 1)
)
_DSFlowMIBGroups_ObjectIdentity = ObjectIdentity
dSFlowMIBGroups = _DSFlowMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 36, 2, 2)
)

# Managed Objects groups

dSFlowAgentGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 171, 14, 36, 2, 2, 1)
)
dSFlowAgentGroup.setObjects(
      *(("DLINKSW-SFLOW-MIB", "dSFlowVersion"),
        ("DLINKSW-SFLOW-MIB", "dSFlowAgentAddressIPv4"),
        ("DLINKSW-SFLOW-MIB", "dSFlowAgentAddressIPv6"),
        ("DLINKSW-SFLOW-MIB", "dSFlowRcvrOwner"),
        ("DLINKSW-SFLOW-MIB", "dSFlowRcvrAdminTimeout"),
        ("DLINKSW-SFLOW-MIB", "dSFlowRcvrCurrentTimeout"),
        ("DLINKSW-SFLOW-MIB", "dSFlowRcvrMaximumDatagramSize"),
        ("DLINKSW-SFLOW-MIB", "dSFlowRcvrAddressType"),
        ("DLINKSW-SFLOW-MIB", "dSFlowRcvrAddress"),
        ("DLINKSW-SFLOW-MIB", "dSFlowRcvrPort"),
        ("DLINKSW-SFLOW-MIB", "dSFlowRcvrVrfName"),
        ("DLINKSW-SFLOW-MIB", "dSFlowRcvrDatagramVersion"),
        ("DLINKSW-SFLOW-MIB", "dSFlowRcvrReset"),
        ("DLINKSW-SFLOW-MIB", "dSFlowFsReceiver"),
        ("DLINKSW-SFLOW-MIB", "dSFlowFsDirection"),
        ("DLINKSW-SFLOW-MIB", "dSFlowFsAdminSamplingRate"),
        ("DLINKSW-SFLOW-MIB", "dSFlowFsActiveSamplingRate"),
        ("DLINKSW-SFLOW-MIB", "dSFlowFsMaximumHeaderSize"),
        ("DLINKSW-SFLOW-MIB", "dSFlowFsRowStatus"),
        ("DLINKSW-SFLOW-MIB", "dSFlowCpReceiver"),
        ("DLINKSW-SFLOW-MIB", "dSFlowCpInterval"),
        ("DLINKSW-SFLOW-MIB", "dSFlowCpRowStatus"))
)
if mibBuilder.loadTexts:
    dSFlowAgentGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

dSFlowCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 171, 14, 36, 2, 1, 1)
)
dSFlowCompliance.setObjects(
    ("DLINKSW-SFLOW-MIB", "dSFlowAgentGroup")
)
if mibBuilder.loadTexts:
    dSFlowCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "DLINKSW-SFLOW-MIB",
    **{"DSFlowDataSource": DSFlowDataSource,
       "DSFlowInstance": DSFlowInstance,
       "DSFlowReceiver": DSFlowReceiver,
       "dlinkSwSFlowMIB": dlinkSwSFlowMIB,
       "dSFlowMIBNotifications": dSFlowMIBNotifications,
       "dSFlowMIBObjects": dSFlowMIBObjects,
       "dSFlowVersion": dSFlowVersion,
       "dSFlowAgentAddressIPv4": dSFlowAgentAddressIPv4,
       "dSFlowAgentAddressIPv6": dSFlowAgentAddressIPv6,
       "dSFlowRcvrTable": dSFlowRcvrTable,
       "dSFlowRcvrEntry": dSFlowRcvrEntry,
       "dSFlowRcvrIndex": dSFlowRcvrIndex,
       "dSFlowRcvrOwner": dSFlowRcvrOwner,
       "dSFlowRcvrAdminTimeout": dSFlowRcvrAdminTimeout,
       "dSFlowRcvrCurrentTimeout": dSFlowRcvrCurrentTimeout,
       "dSFlowRcvrMaximumDatagramSize": dSFlowRcvrMaximumDatagramSize,
       "dSFlowRcvrAddressType": dSFlowRcvrAddressType,
       "dSFlowRcvrAddress": dSFlowRcvrAddress,
       "dSFlowRcvrVrfName": dSFlowRcvrVrfName,
       "dSFlowRcvrPort": dSFlowRcvrPort,
       "dSFlowRcvrDatagramVersion": dSFlowRcvrDatagramVersion,
       "dSFlowRcvrReset": dSFlowRcvrReset,
       "dSFlowFsTable": dSFlowFsTable,
       "dSFlowFsEntry": dSFlowFsEntry,
       "dSFlowFsDataSource": dSFlowFsDataSource,
       "dSFlowFsInstance": dSFlowFsInstance,
       "dSFlowFsReceiver": dSFlowFsReceiver,
       "dSFlowFsDirection": dSFlowFsDirection,
       "dSFlowFsAdminSamplingRate": dSFlowFsAdminSamplingRate,
       "dSFlowFsActiveSamplingRate": dSFlowFsActiveSamplingRate,
       "dSFlowFsMaximumHeaderSize": dSFlowFsMaximumHeaderSize,
       "dSFlowFsRowStatus": dSFlowFsRowStatus,
       "dSFlowCpTable": dSFlowCpTable,
       "dSFlowCpEntry": dSFlowCpEntry,
       "dSFlowCpDataSource": dSFlowCpDataSource,
       "dSFlowCpInstance": dSFlowCpInstance,
       "dSFlowCpReceiver": dSFlowCpReceiver,
       "dSFlowCpInterval": dSFlowCpInterval,
       "dSFlowCpRowStatus": dSFlowCpRowStatus,
       "dSFlowMIBConformance": dSFlowMIBConformance,
       "dSFlowMIBCompliances": dSFlowMIBCompliances,
       "dSFlowCompliance": dSFlowCompliance,
       "dSFlowMIBGroups": dSFlowMIBGroups,
       "dSFlowAgentGroup": dSFlowAgentGroup}
)
