# SNMP MIB module (RADLAN-vlan-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\radlan\RADLAN-vlan-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 12:22:49 2025
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

(dot1dBasePort,) = mibBuilder.importSymbols(
    "BRIDGE-MIB",
    "dot1dBasePort")

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

(PortList,
 VlanIndex,
 dot1qVlanIndex) = mibBuilder.importSymbols(
    "Q-BRIDGE-MIB",
    "PortList",
    "VlanIndex",
    "dot1qVlanIndex")

(rnd,
 rndErrorDesc,
 rndErrorSeverity) = mibBuilder.importSymbols(
    "RADLAN-MIB",
    "rnd",
    "rndErrorDesc",
    "rndErrorSeverity")

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

(DisplayString,
 MacAddress,
 PhysAddress,
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")

(DisplayString,) = mibBuilder.importSymbols(
    "SNMPv2-TC-v1",
    "DisplayString")


# MODULE-IDENTITY

vlan = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 89, 48)
)
if mibBuilder.loadTexts:
    vlan.setRevisions(
        ("2004-04-19 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_VlanMibVersion_Type = Integer32
_VlanMibVersion_Object = MibScalar
vlanMibVersion = _VlanMibVersion_Object(
    (1, 3, 6, 1, 4, 1, 89, 48, 1),
    _VlanMibVersion_Type()
)
vlanMibVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlanMibVersion.setStatus("current")
_VlanMaxTableNumber_Type = Integer32
_VlanMaxTableNumber_Object = MibScalar
vlanMaxTableNumber = _VlanMaxTableNumber_Object(
    (1, 3, 6, 1, 4, 1, 89, 48, 2),
    _VlanMaxTableNumber_Type()
)
vlanMaxTableNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlanMaxTableNumber.setStatus("current")
_VlanNameTable_Object = MibTable
vlanNameTable = _VlanNameTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 48, 21)
)
if mibBuilder.loadTexts:
    vlanNameTable.setStatus("current")
_VlanNameEntry_Object = MibTableRow
vlanNameEntry = _VlanNameEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 48, 21, 1)
)
vlanNameEntry.setIndexNames(
    (0, "RADLAN-vlan-MIB", "vlanNameName"),
)
if mibBuilder.loadTexts:
    vlanNameEntry.setStatus("current")


class _VlanNameName_Type(DisplayString):
    """Custom type vlanNameName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_VlanNameName_Type.__name__ = "DisplayString"
_VlanNameName_Object = MibTableColumn
vlanNameName = _VlanNameName_Object(
    (1, 3, 6, 1, 4, 1, 89, 48, 21, 1, 1),
    _VlanNameName_Type()
)
vlanNameName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlanNameName.setStatus("current")
_VlanNameTag_Type = Integer32
_VlanNameTag_Object = MibTableColumn
vlanNameTag = _VlanNameTag_Object(
    (1, 3, 6, 1, 4, 1, 89, 48, 21, 1, 2),
    _VlanNameTag_Type()
)
vlanNameTag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlanNameTag.setStatus("current")
_VlanNameIfIndex_Type = Integer32
_VlanNameIfIndex_Object = MibTableColumn
vlanNameIfIndex = _VlanNameIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 89, 48, 21, 1, 3),
    _VlanNameIfIndex_Type()
)
vlanNameIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlanNameIfIndex.setStatus("current")
_VlanPortModeTable_Object = MibTable
vlanPortModeTable = _VlanPortModeTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 48, 22)
)
if mibBuilder.loadTexts:
    vlanPortModeTable.setStatus("current")
_VlanPortModeEntry_Object = MibTableRow
vlanPortModeEntry = _VlanPortModeEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 48, 22, 1)
)
vlanPortModeEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    vlanPortModeEntry.setStatus("current")
_VlanPortModeState_Type = Integer32
_VlanPortModeState_Object = MibTableColumn
vlanPortModeState = _VlanPortModeState_Object(
    (1, 3, 6, 1, 4, 1, 89, 48, 22, 1, 1),
    _VlanPortModeState_Type()
)
vlanPortModeState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vlanPortModeState.setStatus("current")


class _VlanSendUnknownToAllPorts_Type(TruthValue):
    """Custom type vlanSendUnknownToAllPorts based on TruthValue"""
    defaultValue = 1


_VlanSendUnknownToAllPorts_Type.__name__ = "TruthValue"
_VlanSendUnknownToAllPorts_Object = MibScalar
vlanSendUnknownToAllPorts = _VlanSendUnknownToAllPorts_Object(
    (1, 3, 6, 1, 4, 1, 89, 48, 27),
    _VlanSendUnknownToAllPorts_Type()
)
vlanSendUnknownToAllPorts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vlanSendUnknownToAllPorts.setStatus("current")
_VlanDefaultSupported_Type = TruthValue
_VlanDefaultSupported_Object = MibScalar
vlanDefaultSupported = _VlanDefaultSupported_Object(
    (1, 3, 6, 1, 4, 1, 89, 48, 29),
    _VlanDefaultSupported_Type()
)
vlanDefaultSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlanDefaultSupported.setStatus("current")
_VlanDot1vSupported_Type = TruthValue
_VlanDot1vSupported_Object = MibScalar
vlanDot1vSupported = _VlanDot1vSupported_Object(
    (1, 3, 6, 1, 4, 1, 89, 48, 31),
    _VlanDot1vSupported_Type()
)
vlanDot1vSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlanDot1vSupported.setStatus("current")
_VlanDefaultEnabled_Type = TruthValue
_VlanDefaultEnabled_Object = MibScalar
vlanDefaultEnabled = _VlanDefaultEnabled_Object(
    (1, 3, 6, 1, 4, 1, 89, 48, 32),
    _VlanDefaultEnabled_Type()
)
vlanDefaultEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vlanDefaultEnabled.setStatus("current")
_VlanSpecialTagTable_Object = MibTable
vlanSpecialTagTable = _VlanSpecialTagTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 48, 33)
)
if mibBuilder.loadTexts:
    vlanSpecialTagTable.setStatus("current")
_VlanSpecialTagEntry_Object = MibTableRow
vlanSpecialTagEntry = _VlanSpecialTagEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 48, 33, 1)
)
vlanSpecialTagEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    vlanSpecialTagEntry.setStatus("current")
_VlanSpecialTagVID_Type = VlanIndex
_VlanSpecialTagVID_Object = MibTableColumn
vlanSpecialTagVID = _VlanSpecialTagVID_Object(
    (1, 3, 6, 1, 4, 1, 89, 48, 33, 1, 1),
    _VlanSpecialTagVID_Type()
)
vlanSpecialTagVID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vlanSpecialTagVID.setStatus("current")
_VlanSpecialTagStatus_Type = RowStatus
_VlanSpecialTagStatus_Object = MibTableColumn
vlanSpecialTagStatus = _VlanSpecialTagStatus_Object(
    (1, 3, 6, 1, 4, 1, 89, 48, 33, 1, 2),
    _VlanSpecialTagStatus_Type()
)
vlanSpecialTagStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vlanSpecialTagStatus.setStatus("current")
_VlanSpecialTagCurrentTable_Object = MibTable
vlanSpecialTagCurrentTable = _VlanSpecialTagCurrentTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 48, 34)
)
if mibBuilder.loadTexts:
    vlanSpecialTagCurrentTable.setStatus("current")
_VlanSpecialTagCurrentEntry_Object = MibTableRow
vlanSpecialTagCurrentEntry = _VlanSpecialTagCurrentEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 48, 34, 1)
)
vlanSpecialTagCurrentEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    vlanSpecialTagCurrentEntry.setStatus("current")
_VlanSpecialTagCurrentVID_Type = VlanIndex
_VlanSpecialTagCurrentVID_Object = MibTableColumn
vlanSpecialTagCurrentVID = _VlanSpecialTagCurrentVID_Object(
    (1, 3, 6, 1, 4, 1, 89, 48, 34, 1, 1),
    _VlanSpecialTagCurrentVID_Type()
)
vlanSpecialTagCurrentVID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlanSpecialTagCurrentVID.setStatus("current")
_VlanSpecialTagCurrentReserved_Type = TruthValue
_VlanSpecialTagCurrentReserved_Object = MibTableColumn
vlanSpecialTagCurrentReserved = _VlanSpecialTagCurrentReserved_Object(
    (1, 3, 6, 1, 4, 1, 89, 48, 34, 1, 2),
    _VlanSpecialTagCurrentReserved_Type()
)
vlanSpecialTagCurrentReserved.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlanSpecialTagCurrentReserved.setStatus("current")
_VlanSpecialTagCurrentActive_Type = TruthValue
_VlanSpecialTagCurrentActive_Object = MibTableColumn
vlanSpecialTagCurrentActive = _VlanSpecialTagCurrentActive_Object(
    (1, 3, 6, 1, 4, 1, 89, 48, 34, 1, 3),
    _VlanSpecialTagCurrentActive_Type()
)
vlanSpecialTagCurrentActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlanSpecialTagCurrentActive.setStatus("current")
_VlanPrivateEdgeSupported_Type = TruthValue
_VlanPrivateEdgeSupported_Object = MibScalar
vlanPrivateEdgeSupported = _VlanPrivateEdgeSupported_Object(
    (1, 3, 6, 1, 4, 1, 89, 48, 35),
    _VlanPrivateEdgeSupported_Type()
)
vlanPrivateEdgeSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlanPrivateEdgeSupported.setStatus("current")
_VlanPrivateEdgeVersion_Type = Integer32
_VlanPrivateEdgeVersion_Object = MibScalar
vlanPrivateEdgeVersion = _VlanPrivateEdgeVersion_Object(
    (1, 3, 6, 1, 4, 1, 89, 48, 36),
    _VlanPrivateEdgeVersion_Type()
)
vlanPrivateEdgeVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlanPrivateEdgeVersion.setStatus("current")
_VlanPrivateEdgeTable_Object = MibTable
vlanPrivateEdgeTable = _VlanPrivateEdgeTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 48, 37)
)
if mibBuilder.loadTexts:
    vlanPrivateEdgeTable.setStatus("current")
_VlanPrivateEdgeEntry_Object = MibTableRow
vlanPrivateEdgeEntry = _VlanPrivateEdgeEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 48, 37, 1)
)
vlanPrivateEdgeEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    vlanPrivateEdgeEntry.setStatus("current")


class _VlanPrivateEdgeUplink_Type(Integer32):
    """Custom type vlanPrivateEdgeUplink based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_VlanPrivateEdgeUplink_Type.__name__ = "Integer32"
_VlanPrivateEdgeUplink_Object = MibTableColumn
vlanPrivateEdgeUplink = _VlanPrivateEdgeUplink_Object(
    (1, 3, 6, 1, 4, 1, 89, 48, 37, 1, 1),
    _VlanPrivateEdgeUplink_Type()
)
vlanPrivateEdgeUplink.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vlanPrivateEdgeUplink.setStatus("current")
_VlanPrivateEdgeStatus_Type = RowStatus
_VlanPrivateEdgeStatus_Object = MibTableColumn
vlanPrivateEdgeStatus = _VlanPrivateEdgeStatus_Object(
    (1, 3, 6, 1, 4, 1, 89, 48, 37, 1, 2),
    _VlanPrivateEdgeStatus_Type()
)
vlanPrivateEdgeStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vlanPrivateEdgeStatus.setStatus("current")
_VlanDynamicVlanSupported_Type = TruthValue
_VlanDynamicVlanSupported_Object = MibScalar
vlanDynamicVlanSupported = _VlanDynamicVlanSupported_Object(
    (1, 3, 6, 1, 4, 1, 89, 48, 38),
    _VlanDynamicVlanSupported_Type()
)
vlanDynamicVlanSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlanDynamicVlanSupported.setStatus("current")
_VlanDynamicVlanTable_Object = MibTable
vlanDynamicVlanTable = _VlanDynamicVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 48, 39)
)
if mibBuilder.loadTexts:
    vlanDynamicVlanTable.setStatus("current")
_VlanDynamicVlanEntry_Object = MibTableRow
vlanDynamicVlanEntry = _VlanDynamicVlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 48, 39, 1)
)
vlanDynamicVlanEntry.setIndexNames(
    (0, "RADLAN-vlan-MIB", "vlanDynamicVlanMacAddress"),
)
if mibBuilder.loadTexts:
    vlanDynamicVlanEntry.setStatus("current")
_VlanDynamicVlanMacAddress_Type = MacAddress
_VlanDynamicVlanMacAddress_Object = MibTableColumn
vlanDynamicVlanMacAddress = _VlanDynamicVlanMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 89, 48, 39, 1, 1),
    _VlanDynamicVlanMacAddress_Type()
)
vlanDynamicVlanMacAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vlanDynamicVlanMacAddress.setStatus("current")
_VlanDynamicVlanTag_Type = VlanIndex
_VlanDynamicVlanTag_Object = MibTableColumn
vlanDynamicVlanTag = _VlanDynamicVlanTag_Object(
    (1, 3, 6, 1, 4, 1, 89, 48, 39, 1, 2),
    _VlanDynamicVlanTag_Type()
)
vlanDynamicVlanTag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vlanDynamicVlanTag.setStatus("current")
_VlanDynamicVlanStatus_Type = RowStatus
_VlanDynamicVlanStatus_Object = MibTableColumn
vlanDynamicVlanStatus = _VlanDynamicVlanStatus_Object(
    (1, 3, 6, 1, 4, 1, 89, 48, 39, 1, 3),
    _VlanDynamicVlanStatus_Type()
)
vlanDynamicVlanStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vlanDynamicVlanStatus.setStatus("current")
_VlanPortModeExtTable_Object = MibTable
vlanPortModeExtTable = _VlanPortModeExtTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 48, 40)
)
if mibBuilder.loadTexts:
    vlanPortModeExtTable.setStatus("current")
_VlanPortModeExtEntry_Object = MibTableRow
vlanPortModeExtEntry = _VlanPortModeExtEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 48, 40, 1)
)
vlanPortModeExtEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    vlanPortModeExtEntry.setStatus("current")
_VlanPortModeExtState_Type = Integer32
_VlanPortModeExtState_Object = MibTableColumn
vlanPortModeExtState = _VlanPortModeExtState_Object(
    (1, 3, 6, 1, 4, 1, 89, 48, 40, 1, 1),
    _VlanPortModeExtState_Type()
)
vlanPortModeExtState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vlanPortModeExtState.setStatus("current")
_VlanPortModeExtStatus_Type = RowStatus
_VlanPortModeExtStatus_Object = MibTableColumn
vlanPortModeExtStatus = _VlanPortModeExtStatus_Object(
    (1, 3, 6, 1, 4, 1, 89, 48, 40, 1, 2),
    _VlanPortModeExtStatus_Type()
)
vlanPortModeExtStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vlanPortModeExtStatus.setStatus("current")
_VlanPrivateSupported_Type = TruthValue
_VlanPrivateSupported_Object = MibScalar
vlanPrivateSupported = _VlanPrivateSupported_Object(
    (1, 3, 6, 1, 4, 1, 89, 48, 41),
    _VlanPrivateSupported_Type()
)
vlanPrivateSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlanPrivateSupported.setStatus("current")
_VlanPrivateTable_Object = MibTable
vlanPrivateTable = _VlanPrivateTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 48, 42)
)
if mibBuilder.loadTexts:
    vlanPrivateTable.setStatus("current")
_VlanPrivateEntry_Object = MibTableRow
vlanPrivateEntry = _VlanPrivateEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 48, 42, 1)
)
vlanPrivateEntry.setIndexNames(
    (0, "Q-BRIDGE-MIB", "dot1qVlanIndex"),
)
if mibBuilder.loadTexts:
    vlanPrivateEntry.setStatus("current")


class _VlanPrivateIsolatedVlanTag_Type(Integer32):
    """Custom type vlanPrivateIsolatedVlanTag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_VlanPrivateIsolatedVlanTag_Type.__name__ = "Integer32"
_VlanPrivateIsolatedVlanTag_Object = MibTableColumn
vlanPrivateIsolatedVlanTag = _VlanPrivateIsolatedVlanTag_Object(
    (1, 3, 6, 1, 4, 1, 89, 48, 42, 1, 1),
    _VlanPrivateIsolatedVlanTag_Type()
)
vlanPrivateIsolatedVlanTag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vlanPrivateIsolatedVlanTag.setStatus("current")
_VlanPrivateStatus_Type = RowStatus
_VlanPrivateStatus_Object = MibTableColumn
vlanPrivateStatus = _VlanPrivateStatus_Object(
    (1, 3, 6, 1, 4, 1, 89, 48, 42, 1, 2),
    _VlanPrivateStatus_Type()
)
vlanPrivateStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vlanPrivateStatus.setStatus("current")
_VlanPrivateCommunityTable_Object = MibTable
vlanPrivateCommunityTable = _VlanPrivateCommunityTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 48, 43)
)
if mibBuilder.loadTexts:
    vlanPrivateCommunityTable.setStatus("current")
_VlanPrivateCommunityEntry_Object = MibTableRow
vlanPrivateCommunityEntry = _VlanPrivateCommunityEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 48, 43, 1)
)
vlanPrivateCommunityEntry.setIndexNames(
    (0, "Q-BRIDGE-MIB", "dot1qVlanIndex"),
    (0, "RADLAN-vlan-MIB", "vlanPrivateCommunityVlanTag"),
)
if mibBuilder.loadTexts:
    vlanPrivateCommunityEntry.setStatus("current")
_VlanPrivateCommunityVlanTag_Type = VlanIndex
_VlanPrivateCommunityVlanTag_Object = MibTableColumn
vlanPrivateCommunityVlanTag = _VlanPrivateCommunityVlanTag_Object(
    (1, 3, 6, 1, 4, 1, 89, 48, 43, 1, 1),
    _VlanPrivateCommunityVlanTag_Type()
)
vlanPrivateCommunityVlanTag.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vlanPrivateCommunityVlanTag.setStatus("current")
_VlanPrivateCommunityStatus_Type = RowStatus
_VlanPrivateCommunityStatus_Object = MibTableColumn
vlanPrivateCommunityStatus = _VlanPrivateCommunityStatus_Object(
    (1, 3, 6, 1, 4, 1, 89, 48, 43, 1, 2),
    _VlanPrivateCommunityStatus_Type()
)
vlanPrivateCommunityStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vlanPrivateCommunityStatus.setStatus("current")
_VlanMulticastTvTable_Object = MibTable
vlanMulticastTvTable = _VlanMulticastTvTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 48, 44)
)
if mibBuilder.loadTexts:
    vlanMulticastTvTable.setStatus("current")
_VlanMulticastTvEntry_Object = MibTableRow
vlanMulticastTvEntry = _VlanMulticastTvEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 48, 44, 1)
)
vlanMulticastTvEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    vlanMulticastTvEntry.setStatus("current")
_VlanMulticastTvVID_Type = VlanIndex
_VlanMulticastTvVID_Object = MibTableColumn
vlanMulticastTvVID = _VlanMulticastTvVID_Object(
    (1, 3, 6, 1, 4, 1, 89, 48, 44, 1, 1),
    _VlanMulticastTvVID_Type()
)
vlanMulticastTvVID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vlanMulticastTvVID.setStatus("current")
_VlanMulticastTvStatus_Type = RowStatus
_VlanMulticastTvStatus_Object = MibTableColumn
vlanMulticastTvStatus = _VlanMulticastTvStatus_Object(
    (1, 3, 6, 1, 4, 1, 89, 48, 44, 1, 2),
    _VlanMulticastTvStatus_Type()
)
vlanMulticastTvStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vlanMulticastTvStatus.setStatus("current")
_VlanMacBaseVlanGroupTable_Object = MibTable
vlanMacBaseVlanGroupTable = _VlanMacBaseVlanGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 48, 45)
)
if mibBuilder.loadTexts:
    vlanMacBaseVlanGroupTable.setStatus("current")
_VlanMacBaseVlanGroupEntry_Object = MibTableRow
vlanMacBaseVlanGroupEntry = _VlanMacBaseVlanGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 48, 45, 1)
)
vlanMacBaseVlanGroupEntry.setIndexNames(
    (0, "RADLAN-vlan-MIB", "vlanMacBaseVlanMacAddress"),
    (0, "RADLAN-vlan-MIB", "vlanMacBaseVlanMacMask"),
)
if mibBuilder.loadTexts:
    vlanMacBaseVlanGroupEntry.setStatus("current")
_VlanMacBaseVlanMacAddress_Type = MacAddress
_VlanMacBaseVlanMacAddress_Object = MibTableColumn
vlanMacBaseVlanMacAddress = _VlanMacBaseVlanMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 89, 48, 45, 1, 1),
    _VlanMacBaseVlanMacAddress_Type()
)
vlanMacBaseVlanMacAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vlanMacBaseVlanMacAddress.setStatus("current")


class _VlanMacBaseVlanMacMask_Type(Integer32):
    """Custom type vlanMacBaseVlanMacMask based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(9, 48),
    )


_VlanMacBaseVlanMacMask_Type.__name__ = "Integer32"
_VlanMacBaseVlanMacMask_Object = MibTableColumn
vlanMacBaseVlanMacMask = _VlanMacBaseVlanMacMask_Object(
    (1, 3, 6, 1, 4, 1, 89, 48, 45, 1, 2),
    _VlanMacBaseVlanMacMask_Type()
)
vlanMacBaseVlanMacMask.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vlanMacBaseVlanMacMask.setStatus("current")


class _VlanMacBaseVlanGroupId_Type(Integer32):
    """Custom type vlanMacBaseVlanGroupId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_VlanMacBaseVlanGroupId_Type.__name__ = "Integer32"
_VlanMacBaseVlanGroupId_Object = MibTableColumn
vlanMacBaseVlanGroupId = _VlanMacBaseVlanGroupId_Object(
    (1, 3, 6, 1, 4, 1, 89, 48, 45, 1, 3),
    _VlanMacBaseVlanGroupId_Type()
)
vlanMacBaseVlanGroupId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vlanMacBaseVlanGroupId.setStatus("current")
_VlanMacBaseVlanGroupRowStatus_Type = RowStatus
_VlanMacBaseVlanGroupRowStatus_Object = MibTableColumn
vlanMacBaseVlanGroupRowStatus = _VlanMacBaseVlanGroupRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 89, 48, 45, 1, 4),
    _VlanMacBaseVlanGroupRowStatus_Type()
)
vlanMacBaseVlanGroupRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vlanMacBaseVlanGroupRowStatus.setStatus("current")
_VlanMacBaseVlanPortTable_Object = MibTable
vlanMacBaseVlanPortTable = _VlanMacBaseVlanPortTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 48, 46)
)
if mibBuilder.loadTexts:
    vlanMacBaseVlanPortTable.setStatus("current")
_VlanMacBaseVlanPortEntry_Object = MibTableRow
vlanMacBaseVlanPortEntry = _VlanMacBaseVlanPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 48, 46, 1)
)
vlanMacBaseVlanPortEntry.setIndexNames(
    (0, "BRIDGE-MIB", "dot1dBasePort"),
    (0, "RADLAN-vlan-MIB", "vlanMacBaseVlanPortGroupId"),
)
if mibBuilder.loadTexts:
    vlanMacBaseVlanPortEntry.setStatus("current")


class _VlanMacBaseVlanPortGroupId_Type(Integer32):
    """Custom type vlanMacBaseVlanPortGroupId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_VlanMacBaseVlanPortGroupId_Type.__name__ = "Integer32"
_VlanMacBaseVlanPortGroupId_Object = MibTableColumn
vlanMacBaseVlanPortGroupId = _VlanMacBaseVlanPortGroupId_Object(
    (1, 3, 6, 1, 4, 1, 89, 48, 46, 1, 1),
    _VlanMacBaseVlanPortGroupId_Type()
)
vlanMacBaseVlanPortGroupId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vlanMacBaseVlanPortGroupId.setStatus("current")
_VlanMacBaseVlanPortGroupVid_Type = VlanIndex
_VlanMacBaseVlanPortGroupVid_Object = MibTableColumn
vlanMacBaseVlanPortGroupVid = _VlanMacBaseVlanPortGroupVid_Object(
    (1, 3, 6, 1, 4, 1, 89, 48, 46, 1, 2),
    _VlanMacBaseVlanPortGroupVid_Type()
)
vlanMacBaseVlanPortGroupVid.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vlanMacBaseVlanPortGroupVid.setStatus("current")
_VlanMacBaseVlanPortRowStatus_Type = RowStatus
_VlanMacBaseVlanPortRowStatus_Object = MibTableColumn
vlanMacBaseVlanPortRowStatus = _VlanMacBaseVlanPortRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 89, 48, 46, 1, 3),
    _VlanMacBaseVlanPortRowStatus_Type()
)
vlanMacBaseVlanPortRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vlanMacBaseVlanPortRowStatus.setStatus("current")
_VlanPrivateEdgeGroupTable_Object = MibTable
vlanPrivateEdgeGroupTable = _VlanPrivateEdgeGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 48, 47)
)
if mibBuilder.loadTexts:
    vlanPrivateEdgeGroupTable.setStatus("current")
_VlanPrivateEdgeGroupEntry_Object = MibTableRow
vlanPrivateEdgeGroupEntry = _VlanPrivateEdgeGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 48, 47, 1)
)
vlanPrivateEdgeGroupEntry.setIndexNames(
    (0, "RADLAN-vlan-MIB", "vlanPrivateEdgeGroupSource"),
)
if mibBuilder.loadTexts:
    vlanPrivateEdgeGroupEntry.setStatus("current")


class _VlanPrivateEdgeGroupSource_Type(Integer32):
    """Custom type vlanPrivateEdgeGroupSource based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_VlanPrivateEdgeGroupSource_Type.__name__ = "Integer32"
_VlanPrivateEdgeGroupSource_Object = MibTableColumn
vlanPrivateEdgeGroupSource = _VlanPrivateEdgeGroupSource_Object(
    (1, 3, 6, 1, 4, 1, 89, 48, 47, 1, 1),
    _VlanPrivateEdgeGroupSource_Type()
)
vlanPrivateEdgeGroupSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlanPrivateEdgeGroupSource.setStatus("current")


class _VlanPrivateEdgeGroupUplink_Type(Integer32):
    """Custom type vlanPrivateEdgeGroupUplink based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_VlanPrivateEdgeGroupUplink_Type.__name__ = "Integer32"
_VlanPrivateEdgeGroupUplink_Object = MibTableColumn
vlanPrivateEdgeGroupUplink = _VlanPrivateEdgeGroupUplink_Object(
    (1, 3, 6, 1, 4, 1, 89, 48, 47, 1, 2),
    _VlanPrivateEdgeGroupUplink_Type()
)
vlanPrivateEdgeGroupUplink.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vlanPrivateEdgeGroupUplink.setStatus("current")
_VlanPrivateEdgeGroupStatus_Type = RowStatus
_VlanPrivateEdgeGroupStatus_Object = MibTableColumn
vlanPrivateEdgeGroupStatus = _VlanPrivateEdgeGroupStatus_Object(
    (1, 3, 6, 1, 4, 1, 89, 48, 47, 1, 3),
    _VlanPrivateEdgeGroupStatus_Type()
)
vlanPrivateEdgeGroupStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vlanPrivateEdgeGroupStatus.setStatus("current")
_VlanPrivateEdgeGroupIfIndexTable_Object = MibTable
vlanPrivateEdgeGroupIfIndexTable = _VlanPrivateEdgeGroupIfIndexTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 48, 48)
)
if mibBuilder.loadTexts:
    vlanPrivateEdgeGroupIfIndexTable.setStatus("current")
_VlanPrivateEdgeGroupIfIndexEntry_Object = MibTableRow
vlanPrivateEdgeGroupIfIndexEntry = _VlanPrivateEdgeGroupIfIndexEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 48, 48, 1)
)
vlanPrivateEdgeGroupIfIndexEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    vlanPrivateEdgeGroupIfIndexEntry.setStatus("current")


class _VlanPrivateEdgeGroupIfIndexID_Type(Integer32):
    """Custom type vlanPrivateEdgeGroupIfIndexID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_VlanPrivateEdgeGroupIfIndexID_Type.__name__ = "Integer32"
_VlanPrivateEdgeGroupIfIndexID_Object = MibTableColumn
vlanPrivateEdgeGroupIfIndexID = _VlanPrivateEdgeGroupIfIndexID_Object(
    (1, 3, 6, 1, 4, 1, 89, 48, 48, 1, 1),
    _VlanPrivateEdgeGroupIfIndexID_Type()
)
vlanPrivateEdgeGroupIfIndexID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlanPrivateEdgeGroupIfIndexID.setStatus("current")


class _VlanPrivateEdgeGroupIfIndexDomainID_Type(Integer32):
    """Custom type vlanPrivateEdgeGroupIfIndexDomainID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_VlanPrivateEdgeGroupIfIndexDomainID_Type.__name__ = "Integer32"
_VlanPrivateEdgeGroupIfIndexDomainID_Object = MibTableColumn
vlanPrivateEdgeGroupIfIndexDomainID = _VlanPrivateEdgeGroupIfIndexDomainID_Object(
    (1, 3, 6, 1, 4, 1, 89, 48, 48, 1, 2),
    _VlanPrivateEdgeGroupIfIndexDomainID_Type()
)
vlanPrivateEdgeGroupIfIndexDomainID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlanPrivateEdgeGroupIfIndexDomainID.setStatus("current")
_VlanSubnetRangeTable_Object = MibTable
vlanSubnetRangeTable = _VlanSubnetRangeTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 48, 49)
)
if mibBuilder.loadTexts:
    vlanSubnetRangeTable.setStatus("current")
_VlanSubnetRangeEntry_Object = MibTableRow
vlanSubnetRangeEntry = _VlanSubnetRangeEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 48, 49, 1)
)
vlanSubnetRangeEntry.setIndexNames(
    (0, "RADLAN-vlan-MIB", "vlanSubnetRangeAddr"),
    (0, "RADLAN-vlan-MIB", "vlanSubnetRangeMask"),
)
if mibBuilder.loadTexts:
    vlanSubnetRangeEntry.setStatus("current")
_VlanSubnetRangeAddr_Type = IpAddress
_VlanSubnetRangeAddr_Object = MibTableColumn
vlanSubnetRangeAddr = _VlanSubnetRangeAddr_Object(
    (1, 3, 6, 1, 4, 1, 89, 48, 49, 1, 1),
    _VlanSubnetRangeAddr_Type()
)
vlanSubnetRangeAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlanSubnetRangeAddr.setStatus("current")


class _VlanSubnetRangeMask_Type(Integer32):
    """Custom type vlanSubnetRangeMask based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_VlanSubnetRangeMask_Type.__name__ = "Integer32"
_VlanSubnetRangeMask_Object = MibTableColumn
vlanSubnetRangeMask = _VlanSubnetRangeMask_Object(
    (1, 3, 6, 1, 4, 1, 89, 48, 49, 1, 2),
    _VlanSubnetRangeMask_Type()
)
vlanSubnetRangeMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlanSubnetRangeMask.setStatus("current")


class _VlanSubnetRangeGroupId_Type(Integer32):
    """Custom type vlanSubnetRangeGroupId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_VlanSubnetRangeGroupId_Type.__name__ = "Integer32"
_VlanSubnetRangeGroupId_Object = MibTableColumn
vlanSubnetRangeGroupId = _VlanSubnetRangeGroupId_Object(
    (1, 3, 6, 1, 4, 1, 89, 48, 49, 1, 3),
    _VlanSubnetRangeGroupId_Type()
)
vlanSubnetRangeGroupId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vlanSubnetRangeGroupId.setStatus("current")
_VlanSubnetRangeRowStatus_Type = RowStatus
_VlanSubnetRangeRowStatus_Object = MibTableColumn
vlanSubnetRangeRowStatus = _VlanSubnetRangeRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 89, 48, 49, 1, 4),
    _VlanSubnetRangeRowStatus_Type()
)
vlanSubnetRangeRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vlanSubnetRangeRowStatus.setStatus("current")
_VlanSubnetPortTable_Object = MibTable
vlanSubnetPortTable = _VlanSubnetPortTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 48, 50)
)
if mibBuilder.loadTexts:
    vlanSubnetPortTable.setStatus("current")
_VlanSubnetPortEntry_Object = MibTableRow
vlanSubnetPortEntry = _VlanSubnetPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 48, 50, 1)
)
vlanSubnetPortEntry.setIndexNames(
    (0, "BRIDGE-MIB", "dot1dBasePort"),
    (0, "RADLAN-vlan-MIB", "vlanSubnetPortGroupId"),
)
if mibBuilder.loadTexts:
    vlanSubnetPortEntry.setStatus("current")


class _VlanSubnetPortGroupId_Type(Integer32):
    """Custom type vlanSubnetPortGroupId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_VlanSubnetPortGroupId_Type.__name__ = "Integer32"
_VlanSubnetPortGroupId_Object = MibTableColumn
vlanSubnetPortGroupId = _VlanSubnetPortGroupId_Object(
    (1, 3, 6, 1, 4, 1, 89, 48, 50, 1, 1),
    _VlanSubnetPortGroupId_Type()
)
vlanSubnetPortGroupId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vlanSubnetPortGroupId.setStatus("current")


class _VlanSubnetPortGroupVid_Type(Integer32):
    """Custom type vlanSubnetPortGroupVid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_VlanSubnetPortGroupVid_Type.__name__ = "Integer32"
_VlanSubnetPortGroupVid_Object = MibTableColumn
vlanSubnetPortGroupVid = _VlanSubnetPortGroupVid_Object(
    (1, 3, 6, 1, 4, 1, 89, 48, 50, 1, 2),
    _VlanSubnetPortGroupVid_Type()
)
vlanSubnetPortGroupVid.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vlanSubnetPortGroupVid.setStatus("current")
_VlanSubnetPortRowStatus_Type = RowStatus
_VlanSubnetPortRowStatus_Object = MibTableColumn
vlanSubnetPortRowStatus = _VlanSubnetPortRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 89, 48, 50, 1, 3),
    _VlanSubnetPortRowStatus_Type()
)
vlanSubnetPortRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vlanSubnetPortRowStatus.setStatus("current")
_VlanTriplePlayTable_Object = MibTable
vlanTriplePlayTable = _VlanTriplePlayTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 48, 51)
)
if mibBuilder.loadTexts:
    vlanTriplePlayTable.setStatus("current")
_VlanTriplePlayEntry_Object = MibTableRow
vlanTriplePlayEntry = _VlanTriplePlayEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 48, 51, 1)
)
vlanTriplePlayEntry.setIndexNames(
    (0, "RADLAN-vlan-MIB", "vlanTriplePlayInnerVID"),
)
if mibBuilder.loadTexts:
    vlanTriplePlayEntry.setStatus("current")
_VlanTriplePlayInnerVID_Type = VlanIndex
_VlanTriplePlayInnerVID_Object = MibTableColumn
vlanTriplePlayInnerVID = _VlanTriplePlayInnerVID_Object(
    (1, 3, 6, 1, 4, 1, 89, 48, 51, 1, 1),
    _VlanTriplePlayInnerVID_Type()
)
vlanTriplePlayInnerVID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vlanTriplePlayInnerVID.setStatus("current")
_VlanTriplePlayMulticastTvVID_Type = VlanIndex
_VlanTriplePlayMulticastTvVID_Object = MibTableColumn
vlanTriplePlayMulticastTvVID = _VlanTriplePlayMulticastTvVID_Object(
    (1, 3, 6, 1, 4, 1, 89, 48, 51, 1, 2),
    _VlanTriplePlayMulticastTvVID_Type()
)
vlanTriplePlayMulticastTvVID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vlanTriplePlayMulticastTvVID.setStatus("current")
_VlanTriplePlayRowStatus_Type = RowStatus
_VlanTriplePlayRowStatus_Object = MibTableColumn
vlanTriplePlayRowStatus = _VlanTriplePlayRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 89, 48, 51, 1, 3),
    _VlanTriplePlayRowStatus_Type()
)
vlanTriplePlayRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vlanTriplePlayRowStatus.setStatus("current")
_VlanTriplePlayMulticastTvTable_Object = MibTable
vlanTriplePlayMulticastTvTable = _VlanTriplePlayMulticastTvTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 48, 52)
)
if mibBuilder.loadTexts:
    vlanTriplePlayMulticastTvTable.setStatus("current")
_VlanTriplePlayMulticatTvEntry_Object = MibTableRow
vlanTriplePlayMulticatTvEntry = _VlanTriplePlayMulticatTvEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 48, 52, 1)
)
vlanTriplePlayMulticatTvEntry.setIndexNames(
    (0, "RADLAN-vlan-MIB", "vlanTriplePlayMulticastTvMulticastTvVID"),
)
if mibBuilder.loadTexts:
    vlanTriplePlayMulticatTvEntry.setStatus("current")
_VlanTriplePlayMulticastTvMulticastTvVID_Type = VlanIndex
_VlanTriplePlayMulticastTvMulticastTvVID_Object = MibTableColumn
vlanTriplePlayMulticastTvMulticastTvVID = _VlanTriplePlayMulticastTvMulticastTvVID_Object(
    (1, 3, 6, 1, 4, 1, 89, 48, 52, 1, 1),
    _VlanTriplePlayMulticastTvMulticastTvVID_Type()
)
vlanTriplePlayMulticastTvMulticastTvVID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlanTriplePlayMulticastTvMulticastTvVID.setStatus("current")
_VlanTriplePlayMulticastTvMulticastTvPortList_Type = PortList
_VlanTriplePlayMulticastTvMulticastTvPortList_Object = MibTableColumn
vlanTriplePlayMulticastTvMulticastTvPortList = _VlanTriplePlayMulticastTvMulticastTvPortList_Object(
    (1, 3, 6, 1, 4, 1, 89, 48, 52, 1, 2),
    _VlanTriplePlayMulticastTvMulticastTvPortList_Type()
)
vlanTriplePlayMulticastTvMulticastTvPortList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vlanTriplePlayMulticastTvMulticastTvPortList.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RADLAN-vlan-MIB",
    **{"vlan": vlan,
       "vlanMibVersion": vlanMibVersion,
       "vlanMaxTableNumber": vlanMaxTableNumber,
       "vlanNameTable": vlanNameTable,
       "vlanNameEntry": vlanNameEntry,
       "vlanNameName": vlanNameName,
       "vlanNameTag": vlanNameTag,
       "vlanNameIfIndex": vlanNameIfIndex,
       "vlanPortModeTable": vlanPortModeTable,
       "vlanPortModeEntry": vlanPortModeEntry,
       "vlanPortModeState": vlanPortModeState,
       "vlanSendUnknownToAllPorts": vlanSendUnknownToAllPorts,
       "vlanDefaultSupported": vlanDefaultSupported,
       "vlanDot1vSupported": vlanDot1vSupported,
       "vlanDefaultEnabled": vlanDefaultEnabled,
       "vlanSpecialTagTable": vlanSpecialTagTable,
       "vlanSpecialTagEntry": vlanSpecialTagEntry,
       "vlanSpecialTagVID": vlanSpecialTagVID,
       "vlanSpecialTagStatus": vlanSpecialTagStatus,
       "vlanSpecialTagCurrentTable": vlanSpecialTagCurrentTable,
       "vlanSpecialTagCurrentEntry": vlanSpecialTagCurrentEntry,
       "vlanSpecialTagCurrentVID": vlanSpecialTagCurrentVID,
       "vlanSpecialTagCurrentReserved": vlanSpecialTagCurrentReserved,
       "vlanSpecialTagCurrentActive": vlanSpecialTagCurrentActive,
       "vlanPrivateEdgeSupported": vlanPrivateEdgeSupported,
       "vlanPrivateEdgeVersion": vlanPrivateEdgeVersion,
       "vlanPrivateEdgeTable": vlanPrivateEdgeTable,
       "vlanPrivateEdgeEntry": vlanPrivateEdgeEntry,
       "vlanPrivateEdgeUplink": vlanPrivateEdgeUplink,
       "vlanPrivateEdgeStatus": vlanPrivateEdgeStatus,
       "vlanDynamicVlanSupported": vlanDynamicVlanSupported,
       "vlanDynamicVlanTable": vlanDynamicVlanTable,
       "vlanDynamicVlanEntry": vlanDynamicVlanEntry,
       "vlanDynamicVlanMacAddress": vlanDynamicVlanMacAddress,
       "vlanDynamicVlanTag": vlanDynamicVlanTag,
       "vlanDynamicVlanStatus": vlanDynamicVlanStatus,
       "vlanPortModeExtTable": vlanPortModeExtTable,
       "vlanPortModeExtEntry": vlanPortModeExtEntry,
       "vlanPortModeExtState": vlanPortModeExtState,
       "vlanPortModeExtStatus": vlanPortModeExtStatus,
       "vlanPrivateSupported": vlanPrivateSupported,
       "vlanPrivateTable": vlanPrivateTable,
       "vlanPrivateEntry": vlanPrivateEntry,
       "vlanPrivateIsolatedVlanTag": vlanPrivateIsolatedVlanTag,
       "vlanPrivateStatus": vlanPrivateStatus,
       "vlanPrivateCommunityTable": vlanPrivateCommunityTable,
       "vlanPrivateCommunityEntry": vlanPrivateCommunityEntry,
       "vlanPrivateCommunityVlanTag": vlanPrivateCommunityVlanTag,
       "vlanPrivateCommunityStatus": vlanPrivateCommunityStatus,
       "vlanMulticastTvTable": vlanMulticastTvTable,
       "vlanMulticastTvEntry": vlanMulticastTvEntry,
       "vlanMulticastTvVID": vlanMulticastTvVID,
       "vlanMulticastTvStatus": vlanMulticastTvStatus,
       "vlanMacBaseVlanGroupTable": vlanMacBaseVlanGroupTable,
       "vlanMacBaseVlanGroupEntry": vlanMacBaseVlanGroupEntry,
       "vlanMacBaseVlanMacAddress": vlanMacBaseVlanMacAddress,
       "vlanMacBaseVlanMacMask": vlanMacBaseVlanMacMask,
       "vlanMacBaseVlanGroupId": vlanMacBaseVlanGroupId,
       "vlanMacBaseVlanGroupRowStatus": vlanMacBaseVlanGroupRowStatus,
       "vlanMacBaseVlanPortTable": vlanMacBaseVlanPortTable,
       "vlanMacBaseVlanPortEntry": vlanMacBaseVlanPortEntry,
       "vlanMacBaseVlanPortGroupId": vlanMacBaseVlanPortGroupId,
       "vlanMacBaseVlanPortGroupVid": vlanMacBaseVlanPortGroupVid,
       "vlanMacBaseVlanPortRowStatus": vlanMacBaseVlanPortRowStatus,
       "vlanPrivateEdgeGroupTable": vlanPrivateEdgeGroupTable,
       "vlanPrivateEdgeGroupEntry": vlanPrivateEdgeGroupEntry,
       "vlanPrivateEdgeGroupSource": vlanPrivateEdgeGroupSource,
       "vlanPrivateEdgeGroupUplink": vlanPrivateEdgeGroupUplink,
       "vlanPrivateEdgeGroupStatus": vlanPrivateEdgeGroupStatus,
       "vlanPrivateEdgeGroupIfIndexTable": vlanPrivateEdgeGroupIfIndexTable,
       "vlanPrivateEdgeGroupIfIndexEntry": vlanPrivateEdgeGroupIfIndexEntry,
       "vlanPrivateEdgeGroupIfIndexID": vlanPrivateEdgeGroupIfIndexID,
       "vlanPrivateEdgeGroupIfIndexDomainID": vlanPrivateEdgeGroupIfIndexDomainID,
       "vlanSubnetRangeTable": vlanSubnetRangeTable,
       "vlanSubnetRangeEntry": vlanSubnetRangeEntry,
       "vlanSubnetRangeAddr": vlanSubnetRangeAddr,
       "vlanSubnetRangeMask": vlanSubnetRangeMask,
       "vlanSubnetRangeGroupId": vlanSubnetRangeGroupId,
       "vlanSubnetRangeRowStatus": vlanSubnetRangeRowStatus,
       "vlanSubnetPortTable": vlanSubnetPortTable,
       "vlanSubnetPortEntry": vlanSubnetPortEntry,
       "vlanSubnetPortGroupId": vlanSubnetPortGroupId,
       "vlanSubnetPortGroupVid": vlanSubnetPortGroupVid,
       "vlanSubnetPortRowStatus": vlanSubnetPortRowStatus,
       "vlanTriplePlayTable": vlanTriplePlayTable,
       "vlanTriplePlayEntry": vlanTriplePlayEntry,
       "vlanTriplePlayInnerVID": vlanTriplePlayInnerVID,
       "vlanTriplePlayMulticastTvVID": vlanTriplePlayMulticastTvVID,
       "vlanTriplePlayRowStatus": vlanTriplePlayRowStatus,
       "vlanTriplePlayMulticastTvTable": vlanTriplePlayMulticastTvTable,
       "vlanTriplePlayMulticatTvEntry": vlanTriplePlayMulticatTvEntry,
       "vlanTriplePlayMulticastTvMulticastTvVID": vlanTriplePlayMulticastTvMulticastTvVID,
       "vlanTriplePlayMulticastTvMulticastTvPortList": vlanTriplePlayMulticastTvMulticastTvPortList}
)
