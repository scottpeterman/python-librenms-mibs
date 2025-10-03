# SNMP MIB module (DLINKSW-AAA-SERVER-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\dlink\DLINKSW-AAA-SERVER-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:36:37 2025
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

(dAaaMIBObjects,) = mibBuilder.importSymbols(
    "DLINKSW-AAA-COMMON-MIB",
    "dAaaMIBObjects")

(InterfaceIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex")

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

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

dlinkSwAAAServerMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 150, 1, 2)
)
if mibBuilder.loadTexts:
    dlinkSwAAAServerMIB.setRevisions(
        ("2013-07-18 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class DlinkAAAProtocol(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("tacacsplus", 1),
          ("radius", 2))
    )



class DlinkAAAGroupName(TextualConvention, OctetString):
    status = "current"
    displayHint = "32a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )



class VrfName(TextualConvention, OctetString):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )



# MIB Managed Objects in the order of their OIDs

_DAaaSrvMIBNotifications_ObjectIdentity = ObjectIdentity
dAaaSrvMIBNotifications = _DAaaSrvMIBNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 150, 1, 2, 0)
)
_DAaaSrvMIBObjects_ObjectIdentity = ObjectIdentity
dAaaSrvMIBObjects = _DAaaSrvMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 150, 1, 2, 1)
)
_DasConfig_ObjectIdentity = ObjectIdentity
dasConfig = _DasConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 150, 1, 2, 1, 1)
)
_DasServerConfigTable_Object = MibTable
dasServerConfigTable = _DasServerConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 150, 1, 2, 1, 1, 1)
)
if mibBuilder.loadTexts:
    dasServerConfigTable.setStatus("current")
_DasServerConfigEntry_Object = MibTableRow
dasServerConfigEntry = _DasServerConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 150, 1, 2, 1, 1, 1, 1)
)
dasServerConfigEntry.setIndexNames(
    (0, "DLINKSW-AAA-SERVER-MIB", "dasServerProtocol"),
    (0, "DLINKSW-AAA-SERVER-MIB", "dasServerIndex"),
)
if mibBuilder.loadTexts:
    dasServerConfigEntry.setStatus("current")
_DasServerProtocol_Type = DlinkAAAProtocol
_DasServerProtocol_Object = MibTableColumn
dasServerProtocol = _DasServerProtocol_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 150, 1, 2, 1, 1, 1, 1, 1),
    _DasServerProtocol_Type()
)
dasServerProtocol.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dasServerProtocol.setStatus("current")


class _DasServerIndex_Type(Unsigned32):
    """Custom type dasServerIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_DasServerIndex_Type.__name__ = "Unsigned32"
_DasServerIndex_Object = MibTableColumn
dasServerIndex = _DasServerIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 150, 1, 2, 1, 1, 1, 1, 2),
    _DasServerIndex_Type()
)
dasServerIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dasServerIndex.setStatus("current")
_DasServerAddrType_Type = InetAddressType
_DasServerAddrType_Object = MibTableColumn
dasServerAddrType = _DasServerAddrType_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 150, 1, 2, 1, 1, 1, 1, 3),
    _DasServerAddrType_Type()
)
dasServerAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dasServerAddrType.setStatus("current")
_DasServerAddress_Type = InetAddress
_DasServerAddress_Object = MibTableColumn
dasServerAddress = _DasServerAddress_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 150, 1, 2, 1, 1, 1, 1, 4),
    _DasServerAddress_Type()
)
dasServerAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dasServerAddress.setStatus("current")


class _DasServerAuthenPort_Type(Unsigned32):
    """Custom type dasServerAuthenPort based on Unsigned32"""
    defaultValue = 1812

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_DasServerAuthenPort_Type.__name__ = "Unsigned32"
_DasServerAuthenPort_Object = MibTableColumn
dasServerAuthenPort = _DasServerAuthenPort_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 150, 1, 2, 1, 1, 1, 1, 5),
    _DasServerAuthenPort_Type()
)
dasServerAuthenPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dasServerAuthenPort.setStatus("current")


class _DasServerAcctPort_Type(Unsigned32):
    """Custom type dasServerAcctPort based on Unsigned32"""
    defaultValue = 1813

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_DasServerAcctPort_Type.__name__ = "Unsigned32"
_DasServerAcctPort_Object = MibTableColumn
dasServerAcctPort = _DasServerAcctPort_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 150, 1, 2, 1, 1, 1, 1, 6),
    _DasServerAcctPort_Type()
)
dasServerAcctPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dasServerAcctPort.setStatus("current")


class _DasServerKey_Type(DisplayString):
    """Custom type dasServerKey based on DisplayString"""
    defaultValue = OctetString("")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 254),
    )


_DasServerKey_Type.__name__ = "DisplayString"
_DasServerKey_Object = MibTableColumn
dasServerKey = _DasServerKey_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 150, 1, 2, 1, 1, 1, 1, 7),
    _DasServerKey_Type()
)
dasServerKey.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dasServerKey.setStatus("current")


class _DasServerTimeout_Type(Unsigned32):
    """Custom type dasServerTimeout based on Unsigned32"""
    defaultValue = 5

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_DasServerTimeout_Type.__name__ = "Unsigned32"
_DasServerTimeout_Object = MibTableColumn
dasServerTimeout = _DasServerTimeout_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 150, 1, 2, 1, 1, 1, 1, 8),
    _DasServerTimeout_Type()
)
dasServerTimeout.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dasServerTimeout.setStatus("current")


class _DasServerRetransmit_Type(Unsigned32):
    """Custom type dasServerRetransmit based on Unsigned32"""
    defaultValue = 2

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 20),
    )


_DasServerRetransmit_Type.__name__ = "Unsigned32"
_DasServerRetransmit_Object = MibTableColumn
dasServerRetransmit = _DasServerRetransmit_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 150, 1, 2, 1, 1, 1, 1, 9),
    _DasServerRetransmit_Type()
)
dasServerRetransmit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dasServerRetransmit.setStatus("current")


class _DasServerPriority_Type(Unsigned32):
    """Custom type dasServerPriority based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_DasServerPriority_Type.__name__ = "Unsigned32"
_DasServerPriority_Object = MibTableColumn
dasServerPriority = _DasServerPriority_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 150, 1, 2, 1, 1, 1, 1, 10),
    _DasServerPriority_Type()
)
dasServerPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dasServerPriority.setStatus("current")
_DasServerRowStatus_Type = RowStatus
_DasServerRowStatus_Object = MibTableColumn
dasServerRowStatus = _DasServerRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 150, 1, 2, 1, 1, 1, 1, 99),
    _DasServerRowStatus_Type()
)
dasServerRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dasServerRowStatus.setStatus("current")


class _DasRadiusServerDeadTime_Type(Unsigned32):
    """Custom type dasRadiusServerDeadTime based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1440),
    )


_DasRadiusServerDeadTime_Type.__name__ = "Unsigned32"
_DasRadiusServerDeadTime_Object = MibScalar
dasRadiusServerDeadTime = _DasRadiusServerDeadTime_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 150, 1, 2, 1, 1, 2),
    _DasRadiusServerDeadTime_Type()
)
dasRadiusServerDeadTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dasRadiusServerDeadTime.setStatus("current")
_DasStatistics_ObjectIdentity = ObjectIdentity
dasStatistics = _DasStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 150, 1, 2, 1, 2)
)
_DasTacplusStatisticsTable_Object = MibTable
dasTacplusStatisticsTable = _DasTacplusStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 150, 1, 2, 1, 2, 1)
)
if mibBuilder.loadTexts:
    dasTacplusStatisticsTable.setStatus("current")
_DasTacplusStatisticsEntry_Object = MibTableRow
dasTacplusStatisticsEntry = _DasTacplusStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 150, 1, 2, 1, 2, 1, 1)
)
if mibBuilder.loadTexts:
    dasTacplusStatisticsEntry.setStatus("current")
_DasTacplusSocketOpens_Type = Counter32
_DasTacplusSocketOpens_Object = MibTableColumn
dasTacplusSocketOpens = _DasTacplusSocketOpens_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 150, 1, 2, 1, 2, 1, 1, 1),
    _DasTacplusSocketOpens_Type()
)
dasTacplusSocketOpens.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dasTacplusSocketOpens.setStatus("current")
_DasTacplusSocketCloses_Type = Counter32
_DasTacplusSocketCloses_Object = MibTableColumn
dasTacplusSocketCloses = _DasTacplusSocketCloses_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 150, 1, 2, 1, 2, 1, 1, 2),
    _DasTacplusSocketCloses_Type()
)
dasTacplusSocketCloses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dasTacplusSocketCloses.setStatus("current")
_DasTacplusTotalPktSent_Type = Counter32
_DasTacplusTotalPktSent_Object = MibTableColumn
dasTacplusTotalPktSent = _DasTacplusTotalPktSent_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 150, 1, 2, 1, 2, 1, 1, 3),
    _DasTacplusTotalPktSent_Type()
)
dasTacplusTotalPktSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dasTacplusTotalPktSent.setStatus("current")
_DasTacplusTotalPktRecv_Type = Counter32
_DasTacplusTotalPktRecv_Object = MibTableColumn
dasTacplusTotalPktRecv = _DasTacplusTotalPktRecv_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 150, 1, 2, 1, 2, 1, 1, 4),
    _DasTacplusTotalPktRecv_Type()
)
dasTacplusTotalPktRecv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dasTacplusTotalPktRecv.setStatus("current")
_DasTacplusReferenceCount_Type = Counter32
_DasTacplusReferenceCount_Object = MibTableColumn
dasTacplusReferenceCount = _DasTacplusReferenceCount_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 150, 1, 2, 1, 2, 1, 1, 5),
    _DasTacplusReferenceCount_Type()
)
dasTacplusReferenceCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dasTacplusReferenceCount.setStatus("current")
_DasGroup_ObjectIdentity = ObjectIdentity
dasGroup = _DasGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 150, 1, 2, 1, 3)
)
_DasGroupTable_Object = MibTable
dasGroupTable = _DasGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 150, 1, 2, 1, 3, 1)
)
if mibBuilder.loadTexts:
    dasGroupTable.setStatus("current")
_DasGroupEntry_Object = MibTableRow
dasGroupEntry = _DasGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 150, 1, 2, 1, 3, 1, 1)
)
dasGroupEntry.setIndexNames(
    (0, "DLINKSW-AAA-SERVER-MIB", "dasGroupProtocol"),
    (0, "DLINKSW-AAA-SERVER-MIB", "dasGroupName"),
)
if mibBuilder.loadTexts:
    dasGroupEntry.setStatus("current")
_DasGroupProtocol_Type = DlinkAAAProtocol
_DasGroupProtocol_Object = MibTableColumn
dasGroupProtocol = _DasGroupProtocol_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 150, 1, 2, 1, 3, 1, 1, 1),
    _DasGroupProtocol_Type()
)
dasGroupProtocol.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dasGroupProtocol.setStatus("current")


class _DasGroupName_Type(DlinkAAAGroupName):
    """Custom type dasGroupName based on DlinkAAAGroupName"""
    defaultValue = OctetString("")


_DasGroupName_Type.__name__ = "DlinkAAAGroupName"
_DasGroupName_Object = MibTableColumn
dasGroupName = _DasGroupName_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 150, 1, 2, 1, 3, 1, 1, 2),
    _DasGroupName_Type()
)
dasGroupName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dasGroupName.setStatus("current")
_DasGroupRowStatus_Type = RowStatus
_DasGroupRowStatus_Object = MibTableColumn
dasGroupRowStatus = _DasGroupRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 150, 1, 2, 1, 3, 1, 1, 3),
    _DasGroupRowStatus_Type()
)
dasGroupRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dasGroupRowStatus.setStatus("current")
_DasGroupServerTable_Object = MibTable
dasGroupServerTable = _DasGroupServerTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 150, 1, 2, 1, 3, 2)
)
if mibBuilder.loadTexts:
    dasGroupServerTable.setStatus("current")
_DasGroupServerEntry_Object = MibTableRow
dasGroupServerEntry = _DasGroupServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 150, 1, 2, 1, 3, 2, 1)
)
dasGroupServerEntry.setIndexNames(
    (0, "DLINKSW-AAA-SERVER-MIB", "dasGroupProtocol"),
    (0, "DLINKSW-AAA-SERVER-MIB", "dasGroupName"),
    (0, "DLINKSW-AAA-SERVER-MIB", "dasGroupSrvIndex"),
)
if mibBuilder.loadTexts:
    dasGroupServerEntry.setStatus("current")


class _DasGroupSrvIndex_Type(Unsigned32):
    """Custom type dasGroupSrvIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_DasGroupSrvIndex_Type.__name__ = "Unsigned32"
_DasGroupSrvIndex_Object = MibTableColumn
dasGroupSrvIndex = _DasGroupSrvIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 150, 1, 2, 1, 3, 2, 1, 1),
    _DasGroupSrvIndex_Type()
)
dasGroupSrvIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dasGroupSrvIndex.setStatus("current")
_DasGroupSrvAddrType_Type = InetAddressType
_DasGroupSrvAddrType_Object = MibTableColumn
dasGroupSrvAddrType = _DasGroupSrvAddrType_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 150, 1, 2, 1, 3, 2, 1, 2),
    _DasGroupSrvAddrType_Type()
)
dasGroupSrvAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dasGroupSrvAddrType.setStatus("current")
_DasGroupSrvAddress_Type = InetAddress
_DasGroupSrvAddress_Object = MibTableColumn
dasGroupSrvAddress = _DasGroupSrvAddress_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 150, 1, 2, 1, 3, 2, 1, 3),
    _DasGroupSrvAddress_Type()
)
dasGroupSrvAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dasGroupSrvAddress.setStatus("current")


class _DasGroupSrvPriority_Type(Unsigned32):
    """Custom type dasGroupSrvPriority based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_DasGroupSrvPriority_Type.__name__ = "Unsigned32"
_DasGroupSrvPriority_Object = MibTableColumn
dasGroupSrvPriority = _DasGroupSrvPriority_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 150, 1, 2, 1, 3, 2, 1, 4),
    _DasGroupSrvPriority_Type()
)
dasGroupSrvPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dasGroupSrvPriority.setStatus("current")
_DasGroupServerRowStatus_Type = RowStatus
_DasGroupServerRowStatus_Object = MibTableColumn
dasGroupServerRowStatus = _DasGroupServerRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 150, 1, 2, 1, 3, 2, 1, 5),
    _DasGroupServerRowStatus_Type()
)
dasGroupServerRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dasGroupServerRowStatus.setStatus("current")
_DasVrf_ObjectIdentity = ObjectIdentity
dasVrf = _DasVrf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 150, 1, 2, 1, 4)
)
_DasGroupVrfTable_Object = MibTable
dasGroupVrfTable = _DasGroupVrfTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 150, 1, 2, 1, 4, 1)
)
if mibBuilder.loadTexts:
    dasGroupVrfTable.setStatus("current")
_DasGroupVrfEntry_Object = MibTableRow
dasGroupVrfEntry = _DasGroupVrfEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 150, 1, 2, 1, 4, 1, 1)
)
dasGroupVrfEntry.setIndexNames(
    (0, "DLINKSW-AAA-SERVER-MIB", "dasGroupProtocol"),
    (0, "DLINKSW-AAA-SERVER-MIB", "dasGroupName"),
)
if mibBuilder.loadTexts:
    dasGroupVrfEntry.setStatus("current")
_DasGroupVrfName_Type = VrfName
_DasGroupVrfName_Object = MibTableColumn
dasGroupVrfName = _DasGroupVrfName_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 150, 1, 2, 1, 4, 1, 1, 1),
    _DasGroupVrfName_Type()
)
dasGroupVrfName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dasGroupVrfName.setStatus("current")
_DasGroupVrfConfigRowStatus_Type = RowStatus
_DasGroupVrfConfigRowStatus_Object = MibTableColumn
dasGroupVrfConfigRowStatus = _DasGroupVrfConfigRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 150, 1, 2, 1, 4, 1, 1, 2),
    _DasGroupVrfConfigRowStatus_Type()
)
dasGroupVrfConfigRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dasGroupVrfConfigRowStatus.setStatus("current")
_DasSrcIf_ObjectIdentity = ObjectIdentity
dasSrcIf = _DasSrcIf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 150, 1, 2, 1, 5)
)
_DasGroupSrcIfTable_Object = MibTable
dasGroupSrcIfTable = _DasGroupSrcIfTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 150, 1, 2, 1, 5, 1)
)
if mibBuilder.loadTexts:
    dasGroupSrcIfTable.setStatus("current")
_DasGroupSrcIfEntry_Object = MibTableRow
dasGroupSrcIfEntry = _DasGroupSrcIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 150, 1, 2, 1, 5, 1, 1)
)
dasGroupSrcIfEntry.setIndexNames(
    (0, "DLINKSW-AAA-SERVER-MIB", "dasGroupProtocol"),
    (0, "DLINKSW-AAA-SERVER-MIB", "dasGroupName"),
    (0, "DLINKSW-AAA-SERVER-MIB", "dasGroupSrcAddrType"),
)
if mibBuilder.loadTexts:
    dasGroupSrcIfEntry.setStatus("current")
_DasGroupSrcAddrType_Type = InetAddressType
_DasGroupSrcAddrType_Object = MibTableColumn
dasGroupSrcAddrType = _DasGroupSrcAddrType_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 150, 1, 2, 1, 5, 1, 1, 1),
    _DasGroupSrcAddrType_Type()
)
dasGroupSrcAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dasGroupSrcAddrType.setStatus("current")
_DasGroupSrcIfIndex_Type = InterfaceIndex
_DasGroupSrcIfIndex_Object = MibTableColumn
dasGroupSrcIfIndex = _DasGroupSrcIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 150, 1, 2, 1, 5, 1, 1, 2),
    _DasGroupSrcIfIndex_Type()
)
dasGroupSrcIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dasGroupSrcIfIndex.setStatus("current")
_DasGroupSrcIfConfigRowStatus_Type = RowStatus
_DasGroupSrcIfConfigRowStatus_Object = MibTableColumn
dasGroupSrcIfConfigRowStatus = _DasGroupSrcIfConfigRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 150, 1, 2, 1, 5, 1, 1, 3),
    _DasGroupSrcIfConfigRowStatus_Type()
)
dasGroupSrcIfConfigRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dasGroupSrcIfConfigRowStatus.setStatus("current")
_DasClear_ObjectIdentity = ObjectIdentity
dasClear = _DasClear_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 150, 1, 2, 1, 6)
)
_DasClearServerStatTable_Object = MibTable
dasClearServerStatTable = _DasClearServerStatTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 150, 1, 2, 1, 6, 1)
)
if mibBuilder.loadTexts:
    dasClearServerStatTable.setStatus("current")
_DasClearServerStatEntry_Object = MibTableRow
dasClearServerStatEntry = _DasClearServerStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 150, 1, 2, 1, 6, 1, 1)
)
dasClearServerStatEntry.setIndexNames(
    (0, "DLINKSW-AAA-SERVER-MIB", "dasServerProtocol"),
    (0, "DLINKSW-AAA-SERVER-MIB", "dasServerIndex"),
)
if mibBuilder.loadTexts:
    dasClearServerStatEntry.setStatus("current")


class _DasClearServerStatAction_Type(Integer32):
    """Custom type dasClearServerStatAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("clear", 1),
          ("noOp", 2))
    )


_DasClearServerStatAction_Type.__name__ = "Integer32"
_DasClearServerStatAction_Object = MibTableColumn
dasClearServerStatAction = _DasClearServerStatAction_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 150, 1, 2, 1, 6, 1, 1, 1),
    _DasClearServerStatAction_Type()
)
dasClearServerStatAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dasClearServerStatAction.setStatus("current")
_DasClearServerStatByGroup_Type = DlinkAAAGroupName
_DasClearServerStatByGroup_Object = MibScalar
dasClearServerStatByGroup = _DasClearServerStatByGroup_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 150, 1, 2, 1, 6, 2),
    _DasClearServerStatByGroup_Type()
)
dasClearServerStatByGroup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dasClearServerStatByGroup.setStatus("current")
_DasClearServerStatByProtocol_Type = DlinkAAAProtocol
_DasClearServerStatByProtocol_Object = MibScalar
dasClearServerStatByProtocol = _DasClearServerStatByProtocol_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 150, 1, 2, 1, 6, 3),
    _DasClearServerStatByProtocol_Type()
)
dasClearServerStatByProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dasClearServerStatByProtocol.setStatus("current")


class _DasClearAllServerStat_Type(Integer32):
    """Custom type dasClearAllServerStat based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("clear", 1),
          ("noOp", 2))
    )


_DasClearAllServerStat_Type.__name__ = "Integer32"
_DasClearAllServerStat_Object = MibScalar
dasClearAllServerStat = _DasClearAllServerStat_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 150, 1, 2, 1, 6, 4),
    _DasClearAllServerStat_Type()
)
dasClearAllServerStat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dasClearAllServerStat.setStatus("current")
_DAaaSrvMIBConformance_ObjectIdentity = ObjectIdentity
dAaaSrvMIBConformance = _DAaaSrvMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 150, 1, 2, 2)
)
_DasMIBCompliances_ObjectIdentity = ObjectIdentity
dasMIBCompliances = _DasMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 150, 1, 2, 2, 1)
)
_DasMIBGroups_ObjectIdentity = ObjectIdentity
dasMIBGroups = _DasMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 150, 1, 2, 2, 2)
)
dasServerConfigEntry.registerAugmentions(
    ("DLINKSW-AAA-SERVER-MIB",
     "dasTacplusStatisticsEntry")
)
dasTacplusStatisticsEntry.setIndexNames(*dasServerConfigEntry.getIndexNames())

# Managed Objects groups

dasTacplusStatisticsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 171, 14, 150, 1, 2, 2, 2, 1)
)
dasTacplusStatisticsGroup.setObjects(
      *(("DLINKSW-AAA-SERVER-MIB", "dasTacplusSocketOpens"),
        ("DLINKSW-AAA-SERVER-MIB", "dasTacplusSocketCloses"),
        ("DLINKSW-AAA-SERVER-MIB", "dasTacplusTotalPktSent"),
        ("DLINKSW-AAA-SERVER-MIB", "dasTacplusTotalPktRecv"),
        ("DLINKSW-AAA-SERVER-MIB", "dasTacplusReferenceCount"))
)
if mibBuilder.loadTexts:
    dasTacplusStatisticsGroup.setStatus("current")

dasConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 171, 14, 150, 1, 2, 2, 2, 2)
)
dasConfigGroup.setObjects(
      *(("DLINKSW-AAA-SERVER-MIB", "dasRadiusServerDeadTime"),
        ("DLINKSW-AAA-SERVER-MIB", "dasServerAddrType"),
        ("DLINKSW-AAA-SERVER-MIB", "dasServerAddress"),
        ("DLINKSW-AAA-SERVER-MIB", "dasServerAuthenPort"),
        ("DLINKSW-AAA-SERVER-MIB", "dasServerAcctPort"),
        ("DLINKSW-AAA-SERVER-MIB", "dasServerTimeout"),
        ("DLINKSW-AAA-SERVER-MIB", "dasServerRetransmit"),
        ("DLINKSW-AAA-SERVER-MIB", "dasServerKey"),
        ("DLINKSW-AAA-SERVER-MIB", "dasServerPriority"),
        ("DLINKSW-AAA-SERVER-MIB", "dasServerRowStatus"))
)
if mibBuilder.loadTexts:
    dasConfigGroup.setStatus("current")

dasSrvGroupGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 171, 14, 150, 1, 2, 2, 2, 3)
)
dasSrvGroupGroup.setObjects(
      *(("DLINKSW-AAA-SERVER-MIB", "dasGroupRowStatus"),
        ("DLINKSW-AAA-SERVER-MIB", "dasGroupSrvAddrType"),
        ("DLINKSW-AAA-SERVER-MIB", "dasGroupSrvAddress"),
        ("DLINKSW-AAA-SERVER-MIB", "dasGroupSrvPriority"),
        ("DLINKSW-AAA-SERVER-MIB", "dasGroupServerRowStatus"))
)
if mibBuilder.loadTexts:
    dasSrvGroupGroup.setStatus("current")

dasVrfGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 171, 14, 150, 1, 2, 2, 2, 4)
)
dasVrfGroup.setObjects(
      *(("DLINKSW-AAA-SERVER-MIB", "dasGroupVrfName"),
        ("DLINKSW-AAA-SERVER-MIB", "dasGroupVrfConfigRowStatus"))
)
if mibBuilder.loadTexts:
    dasVrfGroup.setStatus("current")

dasSrcIfGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 171, 14, 150, 1, 2, 2, 2, 5)
)
dasSrcIfGroup.setObjects(
      *(("DLINKSW-AAA-SERVER-MIB", "dasGroupSrcIfIndex"),
        ("DLINKSW-AAA-SERVER-MIB", "dasGroupSrcIfConfigRowStatus"))
)
if mibBuilder.loadTexts:
    dasSrcIfGroup.setStatus("current")

dasClearStatGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 171, 14, 150, 1, 2, 2, 2, 6)
)
dasClearStatGroup.setObjects(
      *(("DLINKSW-AAA-SERVER-MIB", "dasClearServerStatAction"),
        ("DLINKSW-AAA-SERVER-MIB", "dasClearServerStatByGroup"),
        ("DLINKSW-AAA-SERVER-MIB", "dasClearServerStatByProtocol"),
        ("DLINKSW-AAA-SERVER-MIB", "dasClearAllServerStat"))
)
if mibBuilder.loadTexts:
    dasClearStatGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

dasMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 171, 14, 150, 1, 2, 2, 1, 1)
)
dasMIBCompliance.setObjects(
      *(("DLINKSW-AAA-SERVER-MIB", "dasConfigGroup"),
        ("DLINKSW-AAA-SERVER-MIB", "dasTacplusStatisticsGroup"),
        ("DLINKSW-AAA-SERVER-MIB", "dasSrvGroupGroup"),
        ("DLINKSW-AAA-SERVER-MIB", "dasVrfGroup"),
        ("DLINKSW-AAA-SERVER-MIB", "dasSrcIfGroup"),
        ("DLINKSW-AAA-SERVER-MIB", "dasClearStatGroup"))
)
if mibBuilder.loadTexts:
    dasMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "DLINKSW-AAA-SERVER-MIB",
    **{"DlinkAAAProtocol": DlinkAAAProtocol,
       "DlinkAAAGroupName": DlinkAAAGroupName,
       "VrfName": VrfName,
       "dlinkSwAAAServerMIB": dlinkSwAAAServerMIB,
       "dAaaSrvMIBNotifications": dAaaSrvMIBNotifications,
       "dAaaSrvMIBObjects": dAaaSrvMIBObjects,
       "dasConfig": dasConfig,
       "dasServerConfigTable": dasServerConfigTable,
       "dasServerConfigEntry": dasServerConfigEntry,
       "dasServerProtocol": dasServerProtocol,
       "dasServerIndex": dasServerIndex,
       "dasServerAddrType": dasServerAddrType,
       "dasServerAddress": dasServerAddress,
       "dasServerAuthenPort": dasServerAuthenPort,
       "dasServerAcctPort": dasServerAcctPort,
       "dasServerKey": dasServerKey,
       "dasServerTimeout": dasServerTimeout,
       "dasServerRetransmit": dasServerRetransmit,
       "dasServerPriority": dasServerPriority,
       "dasServerRowStatus": dasServerRowStatus,
       "dasRadiusServerDeadTime": dasRadiusServerDeadTime,
       "dasStatistics": dasStatistics,
       "dasTacplusStatisticsTable": dasTacplusStatisticsTable,
       "dasTacplusStatisticsEntry": dasTacplusStatisticsEntry,
       "dasTacplusSocketOpens": dasTacplusSocketOpens,
       "dasTacplusSocketCloses": dasTacplusSocketCloses,
       "dasTacplusTotalPktSent": dasTacplusTotalPktSent,
       "dasTacplusTotalPktRecv": dasTacplusTotalPktRecv,
       "dasTacplusReferenceCount": dasTacplusReferenceCount,
       "dasGroup": dasGroup,
       "dasGroupTable": dasGroupTable,
       "dasGroupEntry": dasGroupEntry,
       "dasGroupProtocol": dasGroupProtocol,
       "dasGroupName": dasGroupName,
       "dasGroupRowStatus": dasGroupRowStatus,
       "dasGroupServerTable": dasGroupServerTable,
       "dasGroupServerEntry": dasGroupServerEntry,
       "dasGroupSrvIndex": dasGroupSrvIndex,
       "dasGroupSrvAddrType": dasGroupSrvAddrType,
       "dasGroupSrvAddress": dasGroupSrvAddress,
       "dasGroupSrvPriority": dasGroupSrvPriority,
       "dasGroupServerRowStatus": dasGroupServerRowStatus,
       "dasVrf": dasVrf,
       "dasGroupVrfTable": dasGroupVrfTable,
       "dasGroupVrfEntry": dasGroupVrfEntry,
       "dasGroupVrfName": dasGroupVrfName,
       "dasGroupVrfConfigRowStatus": dasGroupVrfConfigRowStatus,
       "dasSrcIf": dasSrcIf,
       "dasGroupSrcIfTable": dasGroupSrcIfTable,
       "dasGroupSrcIfEntry": dasGroupSrcIfEntry,
       "dasGroupSrcAddrType": dasGroupSrcAddrType,
       "dasGroupSrcIfIndex": dasGroupSrcIfIndex,
       "dasGroupSrcIfConfigRowStatus": dasGroupSrcIfConfigRowStatus,
       "dasClear": dasClear,
       "dasClearServerStatTable": dasClearServerStatTable,
       "dasClearServerStatEntry": dasClearServerStatEntry,
       "dasClearServerStatAction": dasClearServerStatAction,
       "dasClearServerStatByGroup": dasClearServerStatByGroup,
       "dasClearServerStatByProtocol": dasClearServerStatByProtocol,
       "dasClearAllServerStat": dasClearAllServerStat,
       "dAaaSrvMIBConformance": dAaaSrvMIBConformance,
       "dasMIBCompliances": dasMIBCompliances,
       "dasMIBCompliance": dasMIBCompliance,
       "dasMIBGroups": dasMIBGroups,
       "dasTacplusStatisticsGroup": dasTacplusStatisticsGroup,
       "dasConfigGroup": dasConfigGroup,
       "dasSrvGroupGroup": dasSrvGroupGroup,
       "dasVrfGroup": dasVrfGroup,
       "dasSrcIfGroup": dasSrcIfGroup,
       "dasClearStatGroup": dasClearStatGroup}
)
