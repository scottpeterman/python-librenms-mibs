# SNMP MIB module (TN-DHCP-SNOOPING-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\transition\TN-DHCP-SNOOPING-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 12:31:18 2025
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
 MacAddress,
 PhysAddress,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "TextualConvention",
    "TruthValue")

(TNInterfaceIndex,) = mibBuilder.importSymbols(
    "TN-TC",
    "TNInterfaceIndex")

(tnProducts,) = mibBuilder.importSymbols(
    "TRANSITION-SMI",
    "tnProducts")


# MODULE-IDENTITY

tnDhcpSnoopingMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 147)
)
if mibBuilder.loadTexts:
    tnDhcpSnoopingMib.setRevisions(
        ("2015-04-20 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_TnDhcpSnoopingMibObjects_ObjectIdentity = ObjectIdentity
tnDhcpSnoopingMibObjects = _TnDhcpSnoopingMibObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 147, 1)
)
_TnDhcpSnoopingConfig_ObjectIdentity = ObjectIdentity
tnDhcpSnoopingConfig = _TnDhcpSnoopingConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 147, 1, 2)
)
_TnDhcpSnoopingConfigGlobals_ObjectIdentity = ObjectIdentity
tnDhcpSnoopingConfigGlobals = _TnDhcpSnoopingConfigGlobals_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 147, 1, 2, 1)
)
_TnDhcpSnoopingConfigGlobalsMode_Type = TruthValue
_TnDhcpSnoopingConfigGlobalsMode_Object = MibScalar
tnDhcpSnoopingConfigGlobalsMode = _TnDhcpSnoopingConfigGlobalsMode_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 147, 1, 2, 1, 1),
    _TnDhcpSnoopingConfigGlobalsMode_Type()
)
tnDhcpSnoopingConfigGlobalsMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnDhcpSnoopingConfigGlobalsMode.setStatus("current")
_TnDhcpSnoopingConfigInterfaceTable_Object = MibTable
tnDhcpSnoopingConfigInterfaceTable = _TnDhcpSnoopingConfigInterfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 147, 1, 2, 2)
)
if mibBuilder.loadTexts:
    tnDhcpSnoopingConfigInterfaceTable.setStatus("current")
_TnDhcpSnoopingConfigInterfaceEntry_Object = MibTableRow
tnDhcpSnoopingConfigInterfaceEntry = _TnDhcpSnoopingConfigInterfaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 147, 1, 2, 2, 1)
)
tnDhcpSnoopingConfigInterfaceEntry.setIndexNames(
    (0, "TN-DHCP-SNOOPING-MIB", "tnDhcpSnoopingConfigInterfaceIfIndex"),
)
if mibBuilder.loadTexts:
    tnDhcpSnoopingConfigInterfaceEntry.setStatus("current")
_TnDhcpSnoopingConfigInterfaceIfIndex_Type = TNInterfaceIndex
_TnDhcpSnoopingConfigInterfaceIfIndex_Object = MibTableColumn
tnDhcpSnoopingConfigInterfaceIfIndex = _TnDhcpSnoopingConfigInterfaceIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 147, 1, 2, 2, 1, 1),
    _TnDhcpSnoopingConfigInterfaceIfIndex_Type()
)
tnDhcpSnoopingConfigInterfaceIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnDhcpSnoopingConfigInterfaceIfIndex.setStatus("current")
_TnDhcpSnoopingConfigInterfaceTrustMode_Type = TruthValue
_TnDhcpSnoopingConfigInterfaceTrustMode_Object = MibTableColumn
tnDhcpSnoopingConfigInterfaceTrustMode = _TnDhcpSnoopingConfigInterfaceTrustMode_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 147, 1, 2, 2, 1, 2),
    _TnDhcpSnoopingConfigInterfaceTrustMode_Type()
)
tnDhcpSnoopingConfigInterfaceTrustMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnDhcpSnoopingConfigInterfaceTrustMode.setStatus("current")
_TnDhcpSnoopingStatus_ObjectIdentity = ObjectIdentity
tnDhcpSnoopingStatus = _TnDhcpSnoopingStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 147, 1, 3)
)
_TnDhcpSnoopingStatusAssignedIpTable_Object = MibTable
tnDhcpSnoopingStatusAssignedIpTable = _TnDhcpSnoopingStatusAssignedIpTable_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 147, 1, 3, 1)
)
if mibBuilder.loadTexts:
    tnDhcpSnoopingStatusAssignedIpTable.setStatus("current")
_TnDhcpSnoopingStatusAssignedIpEntry_Object = MibTableRow
tnDhcpSnoopingStatusAssignedIpEntry = _TnDhcpSnoopingStatusAssignedIpEntry_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 147, 1, 3, 1, 1)
)
tnDhcpSnoopingStatusAssignedIpEntry.setIndexNames(
    (0, "TN-DHCP-SNOOPING-MIB", "tnDhcpSnoopingStatusAssignedIpMacAddress"),
    (0, "TN-DHCP-SNOOPING-MIB", "tnDhcpSnoopingStatusAssignedIpVlanId"),
)
if mibBuilder.loadTexts:
    tnDhcpSnoopingStatusAssignedIpEntry.setStatus("current")
_TnDhcpSnoopingStatusAssignedIpMacAddress_Type = MacAddress
_TnDhcpSnoopingStatusAssignedIpMacAddress_Object = MibTableColumn
tnDhcpSnoopingStatusAssignedIpMacAddress = _TnDhcpSnoopingStatusAssignedIpMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 147, 1, 3, 1, 1, 1),
    _TnDhcpSnoopingStatusAssignedIpMacAddress_Type()
)
tnDhcpSnoopingStatusAssignedIpMacAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnDhcpSnoopingStatusAssignedIpMacAddress.setStatus("current")


class _TnDhcpSnoopingStatusAssignedIpVlanId_Type(Integer32):
    """Custom type tnDhcpSnoopingStatusAssignedIpVlanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_TnDhcpSnoopingStatusAssignedIpVlanId_Type.__name__ = "Integer32"
_TnDhcpSnoopingStatusAssignedIpVlanId_Object = MibTableColumn
tnDhcpSnoopingStatusAssignedIpVlanId = _TnDhcpSnoopingStatusAssignedIpVlanId_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 147, 1, 3, 1, 1, 2),
    _TnDhcpSnoopingStatusAssignedIpVlanId_Type()
)
tnDhcpSnoopingStatusAssignedIpVlanId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnDhcpSnoopingStatusAssignedIpVlanId.setStatus("current")
_TnDhcpSnoopingStatusAssignedIpIfIndex_Type = TNInterfaceIndex
_TnDhcpSnoopingStatusAssignedIpIfIndex_Object = MibTableColumn
tnDhcpSnoopingStatusAssignedIpIfIndex = _TnDhcpSnoopingStatusAssignedIpIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 147, 1, 3, 1, 1, 3),
    _TnDhcpSnoopingStatusAssignedIpIfIndex_Type()
)
tnDhcpSnoopingStatusAssignedIpIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnDhcpSnoopingStatusAssignedIpIfIndex.setStatus("current")
_TnDhcpSnoopingStatusAssignedIpIpAddress_Type = IpAddress
_TnDhcpSnoopingStatusAssignedIpIpAddress_Object = MibTableColumn
tnDhcpSnoopingStatusAssignedIpIpAddress = _TnDhcpSnoopingStatusAssignedIpIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 147, 1, 3, 1, 1, 4),
    _TnDhcpSnoopingStatusAssignedIpIpAddress_Type()
)
tnDhcpSnoopingStatusAssignedIpIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnDhcpSnoopingStatusAssignedIpIpAddress.setStatus("current")
_TnDhcpSnoopingStatusAssignedIpNetmask_Type = IpAddress
_TnDhcpSnoopingStatusAssignedIpNetmask_Object = MibTableColumn
tnDhcpSnoopingStatusAssignedIpNetmask = _TnDhcpSnoopingStatusAssignedIpNetmask_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 147, 1, 3, 1, 1, 5),
    _TnDhcpSnoopingStatusAssignedIpNetmask_Type()
)
tnDhcpSnoopingStatusAssignedIpNetmask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnDhcpSnoopingStatusAssignedIpNetmask.setStatus("current")
_TnDhcpSnoopingStatusAssignedIpDhcpServerIp_Type = IpAddress
_TnDhcpSnoopingStatusAssignedIpDhcpServerIp_Object = MibTableColumn
tnDhcpSnoopingStatusAssignedIpDhcpServerIp = _TnDhcpSnoopingStatusAssignedIpDhcpServerIp_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 147, 1, 3, 1, 1, 6),
    _TnDhcpSnoopingStatusAssignedIpDhcpServerIp_Type()
)
tnDhcpSnoopingStatusAssignedIpDhcpServerIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnDhcpSnoopingStatusAssignedIpDhcpServerIp.setStatus("current")
_TnDhcpSnoopingControl_ObjectIdentity = ObjectIdentity
tnDhcpSnoopingControl = _TnDhcpSnoopingControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 147, 1, 4)
)
_TnDhcpSnoopingControlInterfaceClearStatisticsTable_Object = MibTable
tnDhcpSnoopingControlInterfaceClearStatisticsTable = _TnDhcpSnoopingControlInterfaceClearStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 147, 1, 4, 1)
)
if mibBuilder.loadTexts:
    tnDhcpSnoopingControlInterfaceClearStatisticsTable.setStatus("current")
_TnDhcpSnoopingControlInterfaceClearStatisticsEntry_Object = MibTableRow
tnDhcpSnoopingControlInterfaceClearStatisticsEntry = _TnDhcpSnoopingControlInterfaceClearStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 147, 1, 4, 1, 1)
)
tnDhcpSnoopingControlInterfaceClearStatisticsEntry.setIndexNames(
    (0, "TN-DHCP-SNOOPING-MIB", "tnDhcpSnoopingControlInterfaceClearStatisticsIfIndex"),
)
if mibBuilder.loadTexts:
    tnDhcpSnoopingControlInterfaceClearStatisticsEntry.setStatus("current")
_TnDhcpSnoopingControlInterfaceClearStatisticsIfIndex_Type = TNInterfaceIndex
_TnDhcpSnoopingControlInterfaceClearStatisticsIfIndex_Object = MibTableColumn
tnDhcpSnoopingControlInterfaceClearStatisticsIfIndex = _TnDhcpSnoopingControlInterfaceClearStatisticsIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 147, 1, 4, 1, 1, 1),
    _TnDhcpSnoopingControlInterfaceClearStatisticsIfIndex_Type()
)
tnDhcpSnoopingControlInterfaceClearStatisticsIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnDhcpSnoopingControlInterfaceClearStatisticsIfIndex.setStatus("current")
_TnDhcpSnoopingControlInterfaceClearStatisticsClear_Type = TruthValue
_TnDhcpSnoopingControlInterfaceClearStatisticsClear_Object = MibTableColumn
tnDhcpSnoopingControlInterfaceClearStatisticsClear = _TnDhcpSnoopingControlInterfaceClearStatisticsClear_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 147, 1, 4, 1, 1, 2),
    _TnDhcpSnoopingControlInterfaceClearStatisticsClear_Type()
)
tnDhcpSnoopingControlInterfaceClearStatisticsClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnDhcpSnoopingControlInterfaceClearStatisticsClear.setStatus("current")
_TnDhcpSnoopingStatistics_ObjectIdentity = ObjectIdentity
tnDhcpSnoopingStatistics = _TnDhcpSnoopingStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 147, 1, 5)
)
_TnDhcpSnoopingStatisticsInterfaceTable_Object = MibTable
tnDhcpSnoopingStatisticsInterfaceTable = _TnDhcpSnoopingStatisticsInterfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 147, 1, 5, 2)
)
if mibBuilder.loadTexts:
    tnDhcpSnoopingStatisticsInterfaceTable.setStatus("current")
_TnDhcpSnoopingStatisticsInterfaceEntry_Object = MibTableRow
tnDhcpSnoopingStatisticsInterfaceEntry = _TnDhcpSnoopingStatisticsInterfaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 147, 1, 5, 2, 1)
)
tnDhcpSnoopingStatisticsInterfaceEntry.setIndexNames(
    (0, "TN-DHCP-SNOOPING-MIB", "tnDhcpSnoopingStatisticsInterfaceIfIndex"),
)
if mibBuilder.loadTexts:
    tnDhcpSnoopingStatisticsInterfaceEntry.setStatus("current")
_TnDhcpSnoopingStatisticsInterfaceIfIndex_Type = TNInterfaceIndex
_TnDhcpSnoopingStatisticsInterfaceIfIndex_Object = MibTableColumn
tnDhcpSnoopingStatisticsInterfaceIfIndex = _TnDhcpSnoopingStatisticsInterfaceIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 147, 1, 5, 2, 1, 1),
    _TnDhcpSnoopingStatisticsInterfaceIfIndex_Type()
)
tnDhcpSnoopingStatisticsInterfaceIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnDhcpSnoopingStatisticsInterfaceIfIndex.setStatus("current")
_TnDhcpSnoopingStatisticsInterfaceRxDiscover_Type = Unsigned32
_TnDhcpSnoopingStatisticsInterfaceRxDiscover_Object = MibTableColumn
tnDhcpSnoopingStatisticsInterfaceRxDiscover = _TnDhcpSnoopingStatisticsInterfaceRxDiscover_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 147, 1, 5, 2, 1, 2),
    _TnDhcpSnoopingStatisticsInterfaceRxDiscover_Type()
)
tnDhcpSnoopingStatisticsInterfaceRxDiscover.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnDhcpSnoopingStatisticsInterfaceRxDiscover.setStatus("current")
_TnDhcpSnoopingStatisticsInterfaceRxOffer_Type = Unsigned32
_TnDhcpSnoopingStatisticsInterfaceRxOffer_Object = MibTableColumn
tnDhcpSnoopingStatisticsInterfaceRxOffer = _TnDhcpSnoopingStatisticsInterfaceRxOffer_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 147, 1, 5, 2, 1, 3),
    _TnDhcpSnoopingStatisticsInterfaceRxOffer_Type()
)
tnDhcpSnoopingStatisticsInterfaceRxOffer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnDhcpSnoopingStatisticsInterfaceRxOffer.setStatus("current")
_TnDhcpSnoopingStatisticsInterfaceRxRequest_Type = Unsigned32
_TnDhcpSnoopingStatisticsInterfaceRxRequest_Object = MibTableColumn
tnDhcpSnoopingStatisticsInterfaceRxRequest = _TnDhcpSnoopingStatisticsInterfaceRxRequest_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 147, 1, 5, 2, 1, 4),
    _TnDhcpSnoopingStatisticsInterfaceRxRequest_Type()
)
tnDhcpSnoopingStatisticsInterfaceRxRequest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnDhcpSnoopingStatisticsInterfaceRxRequest.setStatus("current")
_TnDhcpSnoopingStatisticsInterfaceRxDecline_Type = Unsigned32
_TnDhcpSnoopingStatisticsInterfaceRxDecline_Object = MibTableColumn
tnDhcpSnoopingStatisticsInterfaceRxDecline = _TnDhcpSnoopingStatisticsInterfaceRxDecline_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 147, 1, 5, 2, 1, 5),
    _TnDhcpSnoopingStatisticsInterfaceRxDecline_Type()
)
tnDhcpSnoopingStatisticsInterfaceRxDecline.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnDhcpSnoopingStatisticsInterfaceRxDecline.setStatus("current")
_TnDhcpSnoopingStatisticsInterfaceRxAck_Type = Unsigned32
_TnDhcpSnoopingStatisticsInterfaceRxAck_Object = MibTableColumn
tnDhcpSnoopingStatisticsInterfaceRxAck = _TnDhcpSnoopingStatisticsInterfaceRxAck_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 147, 1, 5, 2, 1, 6),
    _TnDhcpSnoopingStatisticsInterfaceRxAck_Type()
)
tnDhcpSnoopingStatisticsInterfaceRxAck.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnDhcpSnoopingStatisticsInterfaceRxAck.setStatus("current")
_TnDhcpSnoopingStatisticsInterfaceRxNak_Type = Unsigned32
_TnDhcpSnoopingStatisticsInterfaceRxNak_Object = MibTableColumn
tnDhcpSnoopingStatisticsInterfaceRxNak = _TnDhcpSnoopingStatisticsInterfaceRxNak_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 147, 1, 5, 2, 1, 7),
    _TnDhcpSnoopingStatisticsInterfaceRxNak_Type()
)
tnDhcpSnoopingStatisticsInterfaceRxNak.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnDhcpSnoopingStatisticsInterfaceRxNak.setStatus("current")
_TnDhcpSnoopingStatisticsInterfaceRxRelease_Type = Unsigned32
_TnDhcpSnoopingStatisticsInterfaceRxRelease_Object = MibTableColumn
tnDhcpSnoopingStatisticsInterfaceRxRelease = _TnDhcpSnoopingStatisticsInterfaceRxRelease_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 147, 1, 5, 2, 1, 8),
    _TnDhcpSnoopingStatisticsInterfaceRxRelease_Type()
)
tnDhcpSnoopingStatisticsInterfaceRxRelease.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnDhcpSnoopingStatisticsInterfaceRxRelease.setStatus("current")
_TnDhcpSnoopingStatisticsInterfaceRxInform_Type = Unsigned32
_TnDhcpSnoopingStatisticsInterfaceRxInform_Object = MibTableColumn
tnDhcpSnoopingStatisticsInterfaceRxInform = _TnDhcpSnoopingStatisticsInterfaceRxInform_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 147, 1, 5, 2, 1, 9),
    _TnDhcpSnoopingStatisticsInterfaceRxInform_Type()
)
tnDhcpSnoopingStatisticsInterfaceRxInform.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnDhcpSnoopingStatisticsInterfaceRxInform.setStatus("current")
_TnDhcpSnoopingStatisticsInterfaceRxLeaseQuery_Type = Unsigned32
_TnDhcpSnoopingStatisticsInterfaceRxLeaseQuery_Object = MibTableColumn
tnDhcpSnoopingStatisticsInterfaceRxLeaseQuery = _TnDhcpSnoopingStatisticsInterfaceRxLeaseQuery_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 147, 1, 5, 2, 1, 10),
    _TnDhcpSnoopingStatisticsInterfaceRxLeaseQuery_Type()
)
tnDhcpSnoopingStatisticsInterfaceRxLeaseQuery.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnDhcpSnoopingStatisticsInterfaceRxLeaseQuery.setStatus("current")
_TnDhcpSnoopingStatisticsInterfaceRxLeaseUnassigned_Type = Unsigned32
_TnDhcpSnoopingStatisticsInterfaceRxLeaseUnassigned_Object = MibTableColumn
tnDhcpSnoopingStatisticsInterfaceRxLeaseUnassigned = _TnDhcpSnoopingStatisticsInterfaceRxLeaseUnassigned_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 147, 1, 5, 2, 1, 11),
    _TnDhcpSnoopingStatisticsInterfaceRxLeaseUnassigned_Type()
)
tnDhcpSnoopingStatisticsInterfaceRxLeaseUnassigned.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnDhcpSnoopingStatisticsInterfaceRxLeaseUnassigned.setStatus("current")
_TnDhcpSnoopingStatisticsInterfaceRxLeaseUnknown_Type = Unsigned32
_TnDhcpSnoopingStatisticsInterfaceRxLeaseUnknown_Object = MibTableColumn
tnDhcpSnoopingStatisticsInterfaceRxLeaseUnknown = _TnDhcpSnoopingStatisticsInterfaceRxLeaseUnknown_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 147, 1, 5, 2, 1, 12),
    _TnDhcpSnoopingStatisticsInterfaceRxLeaseUnknown_Type()
)
tnDhcpSnoopingStatisticsInterfaceRxLeaseUnknown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnDhcpSnoopingStatisticsInterfaceRxLeaseUnknown.setStatus("current")
_TnDhcpSnoopingStatisticsInterfaceRxLeaseActive_Type = Unsigned32
_TnDhcpSnoopingStatisticsInterfaceRxLeaseActive_Object = MibTableColumn
tnDhcpSnoopingStatisticsInterfaceRxLeaseActive = _TnDhcpSnoopingStatisticsInterfaceRxLeaseActive_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 147, 1, 5, 2, 1, 13),
    _TnDhcpSnoopingStatisticsInterfaceRxLeaseActive_Type()
)
tnDhcpSnoopingStatisticsInterfaceRxLeaseActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnDhcpSnoopingStatisticsInterfaceRxLeaseActive.setStatus("current")
_TnDhcpSnoopingStatisticsInterfaceRxDiscardChksumErr_Type = Unsigned32
_TnDhcpSnoopingStatisticsInterfaceRxDiscardChksumErr_Object = MibTableColumn
tnDhcpSnoopingStatisticsInterfaceRxDiscardChksumErr = _TnDhcpSnoopingStatisticsInterfaceRxDiscardChksumErr_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 147, 1, 5, 2, 1, 14),
    _TnDhcpSnoopingStatisticsInterfaceRxDiscardChksumErr_Type()
)
tnDhcpSnoopingStatisticsInterfaceRxDiscardChksumErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnDhcpSnoopingStatisticsInterfaceRxDiscardChksumErr.setStatus("current")
_TnDhcpSnoopingStatisticsInterfaceRxDiscardUntrust_Type = Unsigned32
_TnDhcpSnoopingStatisticsInterfaceRxDiscardUntrust_Object = MibTableColumn
tnDhcpSnoopingStatisticsInterfaceRxDiscardUntrust = _TnDhcpSnoopingStatisticsInterfaceRxDiscardUntrust_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 147, 1, 5, 2, 1, 15),
    _TnDhcpSnoopingStatisticsInterfaceRxDiscardUntrust_Type()
)
tnDhcpSnoopingStatisticsInterfaceRxDiscardUntrust.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnDhcpSnoopingStatisticsInterfaceRxDiscardUntrust.setStatus("current")
_TnDhcpSnoopingStatisticsInterfaceTxDiscover_Type = Unsigned32
_TnDhcpSnoopingStatisticsInterfaceTxDiscover_Object = MibTableColumn
tnDhcpSnoopingStatisticsInterfaceTxDiscover = _TnDhcpSnoopingStatisticsInterfaceTxDiscover_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 147, 1, 5, 2, 1, 16),
    _TnDhcpSnoopingStatisticsInterfaceTxDiscover_Type()
)
tnDhcpSnoopingStatisticsInterfaceTxDiscover.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnDhcpSnoopingStatisticsInterfaceTxDiscover.setStatus("current")
_TnDhcpSnoopingStatisticsInterfaceTxOffer_Type = Unsigned32
_TnDhcpSnoopingStatisticsInterfaceTxOffer_Object = MibTableColumn
tnDhcpSnoopingStatisticsInterfaceTxOffer = _TnDhcpSnoopingStatisticsInterfaceTxOffer_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 147, 1, 5, 2, 1, 17),
    _TnDhcpSnoopingStatisticsInterfaceTxOffer_Type()
)
tnDhcpSnoopingStatisticsInterfaceTxOffer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnDhcpSnoopingStatisticsInterfaceTxOffer.setStatus("current")
_TnDhcpSnoopingStatisticsInterfaceTxRequest_Type = Unsigned32
_TnDhcpSnoopingStatisticsInterfaceTxRequest_Object = MibTableColumn
tnDhcpSnoopingStatisticsInterfaceTxRequest = _TnDhcpSnoopingStatisticsInterfaceTxRequest_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 147, 1, 5, 2, 1, 18),
    _TnDhcpSnoopingStatisticsInterfaceTxRequest_Type()
)
tnDhcpSnoopingStatisticsInterfaceTxRequest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnDhcpSnoopingStatisticsInterfaceTxRequest.setStatus("current")
_TnDhcpSnoopingStatisticsInterfaceTxDecline_Type = Unsigned32
_TnDhcpSnoopingStatisticsInterfaceTxDecline_Object = MibTableColumn
tnDhcpSnoopingStatisticsInterfaceTxDecline = _TnDhcpSnoopingStatisticsInterfaceTxDecline_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 147, 1, 5, 2, 1, 19),
    _TnDhcpSnoopingStatisticsInterfaceTxDecline_Type()
)
tnDhcpSnoopingStatisticsInterfaceTxDecline.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnDhcpSnoopingStatisticsInterfaceTxDecline.setStatus("current")
_TnDhcpSnoopingStatisticsInterfaceTxAck_Type = Unsigned32
_TnDhcpSnoopingStatisticsInterfaceTxAck_Object = MibTableColumn
tnDhcpSnoopingStatisticsInterfaceTxAck = _TnDhcpSnoopingStatisticsInterfaceTxAck_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 147, 1, 5, 2, 1, 20),
    _TnDhcpSnoopingStatisticsInterfaceTxAck_Type()
)
tnDhcpSnoopingStatisticsInterfaceTxAck.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnDhcpSnoopingStatisticsInterfaceTxAck.setStatus("current")
_TnDhcpSnoopingStatisticsInterfaceTxNak_Type = Unsigned32
_TnDhcpSnoopingStatisticsInterfaceTxNak_Object = MibTableColumn
tnDhcpSnoopingStatisticsInterfaceTxNak = _TnDhcpSnoopingStatisticsInterfaceTxNak_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 147, 1, 5, 2, 1, 21),
    _TnDhcpSnoopingStatisticsInterfaceTxNak_Type()
)
tnDhcpSnoopingStatisticsInterfaceTxNak.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnDhcpSnoopingStatisticsInterfaceTxNak.setStatus("current")
_TnDhcpSnoopingStatisticsInterfaceTxRelease_Type = Unsigned32
_TnDhcpSnoopingStatisticsInterfaceTxRelease_Object = MibTableColumn
tnDhcpSnoopingStatisticsInterfaceTxRelease = _TnDhcpSnoopingStatisticsInterfaceTxRelease_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 147, 1, 5, 2, 1, 22),
    _TnDhcpSnoopingStatisticsInterfaceTxRelease_Type()
)
tnDhcpSnoopingStatisticsInterfaceTxRelease.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnDhcpSnoopingStatisticsInterfaceTxRelease.setStatus("current")
_TnDhcpSnoopingStatisticsInterfaceTxInform_Type = Unsigned32
_TnDhcpSnoopingStatisticsInterfaceTxInform_Object = MibTableColumn
tnDhcpSnoopingStatisticsInterfaceTxInform = _TnDhcpSnoopingStatisticsInterfaceTxInform_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 147, 1, 5, 2, 1, 23),
    _TnDhcpSnoopingStatisticsInterfaceTxInform_Type()
)
tnDhcpSnoopingStatisticsInterfaceTxInform.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnDhcpSnoopingStatisticsInterfaceTxInform.setStatus("current")
_TnDhcpSnoopingStatisticsInterfaceTxLeaseQuery_Type = Unsigned32
_TnDhcpSnoopingStatisticsInterfaceTxLeaseQuery_Object = MibTableColumn
tnDhcpSnoopingStatisticsInterfaceTxLeaseQuery = _TnDhcpSnoopingStatisticsInterfaceTxLeaseQuery_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 147, 1, 5, 2, 1, 24),
    _TnDhcpSnoopingStatisticsInterfaceTxLeaseQuery_Type()
)
tnDhcpSnoopingStatisticsInterfaceTxLeaseQuery.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnDhcpSnoopingStatisticsInterfaceTxLeaseQuery.setStatus("current")
_TnDhcpSnoopingStatisticsInterfaceTxLeaseUnassigned_Type = Unsigned32
_TnDhcpSnoopingStatisticsInterfaceTxLeaseUnassigned_Object = MibTableColumn
tnDhcpSnoopingStatisticsInterfaceTxLeaseUnassigned = _TnDhcpSnoopingStatisticsInterfaceTxLeaseUnassigned_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 147, 1, 5, 2, 1, 25),
    _TnDhcpSnoopingStatisticsInterfaceTxLeaseUnassigned_Type()
)
tnDhcpSnoopingStatisticsInterfaceTxLeaseUnassigned.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnDhcpSnoopingStatisticsInterfaceTxLeaseUnassigned.setStatus("current")
_TnDhcpSnoopingStatisticsInterfaceTxLeaseUnknown_Type = Unsigned32
_TnDhcpSnoopingStatisticsInterfaceTxLeaseUnknown_Object = MibTableColumn
tnDhcpSnoopingStatisticsInterfaceTxLeaseUnknown = _TnDhcpSnoopingStatisticsInterfaceTxLeaseUnknown_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 147, 1, 5, 2, 1, 26),
    _TnDhcpSnoopingStatisticsInterfaceTxLeaseUnknown_Type()
)
tnDhcpSnoopingStatisticsInterfaceTxLeaseUnknown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnDhcpSnoopingStatisticsInterfaceTxLeaseUnknown.setStatus("current")
_TnDhcpSnoopingStatisticsInterfaceTxLeaseActive_Type = Unsigned32
_TnDhcpSnoopingStatisticsInterfaceTxLeaseActive_Object = MibTableColumn
tnDhcpSnoopingStatisticsInterfaceTxLeaseActive = _TnDhcpSnoopingStatisticsInterfaceTxLeaseActive_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 147, 1, 5, 2, 1, 27),
    _TnDhcpSnoopingStatisticsInterfaceTxLeaseActive_Type()
)
tnDhcpSnoopingStatisticsInterfaceTxLeaseActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnDhcpSnoopingStatisticsInterfaceTxLeaseActive.setStatus("current")
_TnDhcpSnoopingMibConformance_ObjectIdentity = ObjectIdentity
tnDhcpSnoopingMibConformance = _TnDhcpSnoopingMibConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 147, 2)
)
_TnDhcpSnoopingMibCompliances_ObjectIdentity = ObjectIdentity
tnDhcpSnoopingMibCompliances = _TnDhcpSnoopingMibCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 147, 2, 1)
)
_TnDhcpSnoopingMibGroups_ObjectIdentity = ObjectIdentity
tnDhcpSnoopingMibGroups = _TnDhcpSnoopingMibGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 147, 2, 2)
)

# Managed Objects groups

tnDhcpSnoopingConfigGlobalsInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 147, 2, 2, 1)
)
tnDhcpSnoopingConfigGlobalsInfoGroup.setObjects(
    ("TN-DHCP-SNOOPING-MIB", "tnDhcpSnoopingConfigGlobalsMode")
)
if mibBuilder.loadTexts:
    tnDhcpSnoopingConfigGlobalsInfoGroup.setStatus("current")

tnDhcpSnoopingConfigInterfaceInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 147, 2, 2, 2)
)
tnDhcpSnoopingConfigInterfaceInfoGroup.setObjects(
    ("TN-DHCP-SNOOPING-MIB", "tnDhcpSnoopingConfigInterfaceTrustMode")
)
if mibBuilder.loadTexts:
    tnDhcpSnoopingConfigInterfaceInfoGroup.setStatus("current")

tnDhcpSnoopingStatusAssignedIpTableInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 147, 2, 2, 3)
)
tnDhcpSnoopingStatusAssignedIpTableInfoGroup.setObjects(
      *(("TN-DHCP-SNOOPING-MIB", "tnDhcpSnoopingStatusAssignedIpIfIndex"),
        ("TN-DHCP-SNOOPING-MIB", "tnDhcpSnoopingStatusAssignedIpIpAddress"),
        ("TN-DHCP-SNOOPING-MIB", "tnDhcpSnoopingStatusAssignedIpNetmask"),
        ("TN-DHCP-SNOOPING-MIB", "tnDhcpSnoopingStatusAssignedIpDhcpServerIp"))
)
if mibBuilder.loadTexts:
    tnDhcpSnoopingStatusAssignedIpTableInfoGroup.setStatus("current")

tnDhcpSnoopingControlInterfaceClearStatisticsTableInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 147, 2, 2, 4)
)
tnDhcpSnoopingControlInterfaceClearStatisticsTableInfoGroup.setObjects(
    ("TN-DHCP-SNOOPING-MIB", "tnDhcpSnoopingControlInterfaceClearStatisticsClear")
)
if mibBuilder.loadTexts:
    tnDhcpSnoopingControlInterfaceClearStatisticsTableInfoGroup.setStatus("current")

tnDhcpSnoopingStatisticsInterfaceTableInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 147, 2, 2, 5)
)
tnDhcpSnoopingStatisticsInterfaceTableInfoGroup.setObjects(
      *(("TN-DHCP-SNOOPING-MIB", "tnDhcpSnoopingStatisticsInterfaceRxDiscover"),
        ("TN-DHCP-SNOOPING-MIB", "tnDhcpSnoopingStatisticsInterfaceRxOffer"),
        ("TN-DHCP-SNOOPING-MIB", "tnDhcpSnoopingStatisticsInterfaceRxRequest"),
        ("TN-DHCP-SNOOPING-MIB", "tnDhcpSnoopingStatisticsInterfaceRxDecline"),
        ("TN-DHCP-SNOOPING-MIB", "tnDhcpSnoopingStatisticsInterfaceRxAck"),
        ("TN-DHCP-SNOOPING-MIB", "tnDhcpSnoopingStatisticsInterfaceRxNak"),
        ("TN-DHCP-SNOOPING-MIB", "tnDhcpSnoopingStatisticsInterfaceRxRelease"),
        ("TN-DHCP-SNOOPING-MIB", "tnDhcpSnoopingStatisticsInterfaceRxInform"),
        ("TN-DHCP-SNOOPING-MIB", "tnDhcpSnoopingStatisticsInterfaceRxLeaseQuery"),
        ("TN-DHCP-SNOOPING-MIB", "tnDhcpSnoopingStatisticsInterfaceRxLeaseUnassigned"),
        ("TN-DHCP-SNOOPING-MIB", "tnDhcpSnoopingStatisticsInterfaceRxLeaseUnknown"),
        ("TN-DHCP-SNOOPING-MIB", "tnDhcpSnoopingStatisticsInterfaceRxLeaseActive"),
        ("TN-DHCP-SNOOPING-MIB", "tnDhcpSnoopingStatisticsInterfaceRxDiscardChksumErr"),
        ("TN-DHCP-SNOOPING-MIB", "tnDhcpSnoopingStatisticsInterfaceRxDiscardUntrust"),
        ("TN-DHCP-SNOOPING-MIB", "tnDhcpSnoopingStatisticsInterfaceTxDiscover"),
        ("TN-DHCP-SNOOPING-MIB", "tnDhcpSnoopingStatisticsInterfaceTxOffer"),
        ("TN-DHCP-SNOOPING-MIB", "tnDhcpSnoopingStatisticsInterfaceTxRequest"),
        ("TN-DHCP-SNOOPING-MIB", "tnDhcpSnoopingStatisticsInterfaceTxDecline"),
        ("TN-DHCP-SNOOPING-MIB", "tnDhcpSnoopingStatisticsInterfaceTxAck"),
        ("TN-DHCP-SNOOPING-MIB", "tnDhcpSnoopingStatisticsInterfaceTxNak"),
        ("TN-DHCP-SNOOPING-MIB", "tnDhcpSnoopingStatisticsInterfaceTxRelease"),
        ("TN-DHCP-SNOOPING-MIB", "tnDhcpSnoopingStatisticsInterfaceTxInform"),
        ("TN-DHCP-SNOOPING-MIB", "tnDhcpSnoopingStatisticsInterfaceTxLeaseQuery"),
        ("TN-DHCP-SNOOPING-MIB", "tnDhcpSnoopingStatisticsInterfaceTxLeaseUnassigned"),
        ("TN-DHCP-SNOOPING-MIB", "tnDhcpSnoopingStatisticsInterfaceTxLeaseUnknown"),
        ("TN-DHCP-SNOOPING-MIB", "tnDhcpSnoopingStatisticsInterfaceTxLeaseActive"))
)
if mibBuilder.loadTexts:
    tnDhcpSnoopingStatisticsInterfaceTableInfoGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

tnDhcpSnoopingMibCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 147, 2, 1, 1)
)
tnDhcpSnoopingMibCompliance.setObjects(
      *(("TN-DHCP-SNOOPING-MIB", "tnDhcpSnoopingConfigGlobalsInfoGroup"),
        ("TN-DHCP-SNOOPING-MIB", "tnDhcpSnoopingConfigInterfaceInfoGroup"),
        ("TN-DHCP-SNOOPING-MIB", "tnDhcpSnoopingStatusAssignedIpTableInfoGroup"),
        ("TN-DHCP-SNOOPING-MIB", "tnDhcpSnoopingControlInterfaceClearStatisticsTableInfoGroup"),
        ("TN-DHCP-SNOOPING-MIB", "tnDhcpSnoopingStatisticsInterfaceTableInfoGroup"))
)
if mibBuilder.loadTexts:
    tnDhcpSnoopingMibCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TN-DHCP-SNOOPING-MIB",
    **{"tnDhcpSnoopingMib": tnDhcpSnoopingMib,
       "tnDhcpSnoopingMibObjects": tnDhcpSnoopingMibObjects,
       "tnDhcpSnoopingConfig": tnDhcpSnoopingConfig,
       "tnDhcpSnoopingConfigGlobals": tnDhcpSnoopingConfigGlobals,
       "tnDhcpSnoopingConfigGlobalsMode": tnDhcpSnoopingConfigGlobalsMode,
       "tnDhcpSnoopingConfigInterfaceTable": tnDhcpSnoopingConfigInterfaceTable,
       "tnDhcpSnoopingConfigInterfaceEntry": tnDhcpSnoopingConfigInterfaceEntry,
       "tnDhcpSnoopingConfigInterfaceIfIndex": tnDhcpSnoopingConfigInterfaceIfIndex,
       "tnDhcpSnoopingConfigInterfaceTrustMode": tnDhcpSnoopingConfigInterfaceTrustMode,
       "tnDhcpSnoopingStatus": tnDhcpSnoopingStatus,
       "tnDhcpSnoopingStatusAssignedIpTable": tnDhcpSnoopingStatusAssignedIpTable,
       "tnDhcpSnoopingStatusAssignedIpEntry": tnDhcpSnoopingStatusAssignedIpEntry,
       "tnDhcpSnoopingStatusAssignedIpMacAddress": tnDhcpSnoopingStatusAssignedIpMacAddress,
       "tnDhcpSnoopingStatusAssignedIpVlanId": tnDhcpSnoopingStatusAssignedIpVlanId,
       "tnDhcpSnoopingStatusAssignedIpIfIndex": tnDhcpSnoopingStatusAssignedIpIfIndex,
       "tnDhcpSnoopingStatusAssignedIpIpAddress": tnDhcpSnoopingStatusAssignedIpIpAddress,
       "tnDhcpSnoopingStatusAssignedIpNetmask": tnDhcpSnoopingStatusAssignedIpNetmask,
       "tnDhcpSnoopingStatusAssignedIpDhcpServerIp": tnDhcpSnoopingStatusAssignedIpDhcpServerIp,
       "tnDhcpSnoopingControl": tnDhcpSnoopingControl,
       "tnDhcpSnoopingControlInterfaceClearStatisticsTable": tnDhcpSnoopingControlInterfaceClearStatisticsTable,
       "tnDhcpSnoopingControlInterfaceClearStatisticsEntry": tnDhcpSnoopingControlInterfaceClearStatisticsEntry,
       "tnDhcpSnoopingControlInterfaceClearStatisticsIfIndex": tnDhcpSnoopingControlInterfaceClearStatisticsIfIndex,
       "tnDhcpSnoopingControlInterfaceClearStatisticsClear": tnDhcpSnoopingControlInterfaceClearStatisticsClear,
       "tnDhcpSnoopingStatistics": tnDhcpSnoopingStatistics,
       "tnDhcpSnoopingStatisticsInterfaceTable": tnDhcpSnoopingStatisticsInterfaceTable,
       "tnDhcpSnoopingStatisticsInterfaceEntry": tnDhcpSnoopingStatisticsInterfaceEntry,
       "tnDhcpSnoopingStatisticsInterfaceIfIndex": tnDhcpSnoopingStatisticsInterfaceIfIndex,
       "tnDhcpSnoopingStatisticsInterfaceRxDiscover": tnDhcpSnoopingStatisticsInterfaceRxDiscover,
       "tnDhcpSnoopingStatisticsInterfaceRxOffer": tnDhcpSnoopingStatisticsInterfaceRxOffer,
       "tnDhcpSnoopingStatisticsInterfaceRxRequest": tnDhcpSnoopingStatisticsInterfaceRxRequest,
       "tnDhcpSnoopingStatisticsInterfaceRxDecline": tnDhcpSnoopingStatisticsInterfaceRxDecline,
       "tnDhcpSnoopingStatisticsInterfaceRxAck": tnDhcpSnoopingStatisticsInterfaceRxAck,
       "tnDhcpSnoopingStatisticsInterfaceRxNak": tnDhcpSnoopingStatisticsInterfaceRxNak,
       "tnDhcpSnoopingStatisticsInterfaceRxRelease": tnDhcpSnoopingStatisticsInterfaceRxRelease,
       "tnDhcpSnoopingStatisticsInterfaceRxInform": tnDhcpSnoopingStatisticsInterfaceRxInform,
       "tnDhcpSnoopingStatisticsInterfaceRxLeaseQuery": tnDhcpSnoopingStatisticsInterfaceRxLeaseQuery,
       "tnDhcpSnoopingStatisticsInterfaceRxLeaseUnassigned": tnDhcpSnoopingStatisticsInterfaceRxLeaseUnassigned,
       "tnDhcpSnoopingStatisticsInterfaceRxLeaseUnknown": tnDhcpSnoopingStatisticsInterfaceRxLeaseUnknown,
       "tnDhcpSnoopingStatisticsInterfaceRxLeaseActive": tnDhcpSnoopingStatisticsInterfaceRxLeaseActive,
       "tnDhcpSnoopingStatisticsInterfaceRxDiscardChksumErr": tnDhcpSnoopingStatisticsInterfaceRxDiscardChksumErr,
       "tnDhcpSnoopingStatisticsInterfaceRxDiscardUntrust": tnDhcpSnoopingStatisticsInterfaceRxDiscardUntrust,
       "tnDhcpSnoopingStatisticsInterfaceTxDiscover": tnDhcpSnoopingStatisticsInterfaceTxDiscover,
       "tnDhcpSnoopingStatisticsInterfaceTxOffer": tnDhcpSnoopingStatisticsInterfaceTxOffer,
       "tnDhcpSnoopingStatisticsInterfaceTxRequest": tnDhcpSnoopingStatisticsInterfaceTxRequest,
       "tnDhcpSnoopingStatisticsInterfaceTxDecline": tnDhcpSnoopingStatisticsInterfaceTxDecline,
       "tnDhcpSnoopingStatisticsInterfaceTxAck": tnDhcpSnoopingStatisticsInterfaceTxAck,
       "tnDhcpSnoopingStatisticsInterfaceTxNak": tnDhcpSnoopingStatisticsInterfaceTxNak,
       "tnDhcpSnoopingStatisticsInterfaceTxRelease": tnDhcpSnoopingStatisticsInterfaceTxRelease,
       "tnDhcpSnoopingStatisticsInterfaceTxInform": tnDhcpSnoopingStatisticsInterfaceTxInform,
       "tnDhcpSnoopingStatisticsInterfaceTxLeaseQuery": tnDhcpSnoopingStatisticsInterfaceTxLeaseQuery,
       "tnDhcpSnoopingStatisticsInterfaceTxLeaseUnassigned": tnDhcpSnoopingStatisticsInterfaceTxLeaseUnassigned,
       "tnDhcpSnoopingStatisticsInterfaceTxLeaseUnknown": tnDhcpSnoopingStatisticsInterfaceTxLeaseUnknown,
       "tnDhcpSnoopingStatisticsInterfaceTxLeaseActive": tnDhcpSnoopingStatisticsInterfaceTxLeaseActive,
       "tnDhcpSnoopingMibConformance": tnDhcpSnoopingMibConformance,
       "tnDhcpSnoopingMibCompliances": tnDhcpSnoopingMibCompliances,
       "tnDhcpSnoopingMibCompliance": tnDhcpSnoopingMibCompliance,
       "tnDhcpSnoopingMibGroups": tnDhcpSnoopingMibGroups,
       "tnDhcpSnoopingConfigGlobalsInfoGroup": tnDhcpSnoopingConfigGlobalsInfoGroup,
       "tnDhcpSnoopingConfigInterfaceInfoGroup": tnDhcpSnoopingConfigInterfaceInfoGroup,
       "tnDhcpSnoopingStatusAssignedIpTableInfoGroup": tnDhcpSnoopingStatusAssignedIpTableInfoGroup,
       "tnDhcpSnoopingControlInterfaceClearStatisticsTableInfoGroup": tnDhcpSnoopingControlInterfaceClearStatisticsTableInfoGroup,
       "tnDhcpSnoopingStatisticsInterfaceTableInfoGroup": tnDhcpSnoopingStatisticsInterfaceTableInfoGroup}
)
