# SNMP MIB module (CISCOSBLAN1-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\cisco\CISCOSBLAN1-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:30:22 2025
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

(switch001,) = mibBuilder.importSymbols(
    "CISCOSB-MIB",
    "switch001")

(VlanId,) = mibBuilder.importSymbols(
    "Q-BRIDGE-MIB",
    "VlanId")

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


# MODULE-IDENTITY

rlLan1 = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 224)
)
if mibBuilder.loadTexts:
    rlLan1.setRevisions(
        ("2015-06-30 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class GroupId(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1279),
    )



class GroupIdList(TextualConvention, OctetString):
    status = "current"


class VlanIdOrNone(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )



# MIB Managed Objects in the order of their OIDs



class _RlLan1STagEtherType_Type(OctetString):
    """Custom type rlLan1STagEtherType based on OctetString"""
    defaultHexValue = "0000"

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )
    fixed_length = 2


_RlLan1STagEtherType_Type.__name__ = "OctetString"
_RlLan1STagEtherType_Object = MibScalar
rlLan1STagEtherType = _RlLan1STagEtherType_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 224, 1),
    _RlLan1STagEtherType_Type()
)
rlLan1STagEtherType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlLan1STagEtherType.setStatus("current")


class _RlLan1CPVlanId_Type(VlanIdOrNone):
    """Custom type rlLan1CPVlanId based on VlanIdOrNone"""
    defaultValue = 0


_RlLan1CPVlanId_Type.__name__ = "VlanIdOrNone"
_RlLan1CPVlanId_Object = MibScalar
rlLan1CPVlanId = _RlLan1CPVlanId_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 224, 2),
    _RlLan1CPVlanId_Type()
)
rlLan1CPVlanId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlLan1CPVlanId.setStatus("current")


class _RlLan1CPVlanCos_Type(Integer32):
    """Custom type rlLan1CPVlanCos based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_RlLan1CPVlanCos_Type.__name__ = "Integer32"
_RlLan1CPVlanCos_Object = MibScalar
rlLan1CPVlanCos = _RlLan1CPVlanCos_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 224, 3),
    _RlLan1CPVlanCos_Type()
)
rlLan1CPVlanCos.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlLan1CPVlanCos.setStatus("current")


class _RlLan1x86Port_Type(Integer32):
    """Custom type rlLan1x86Port based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_RlLan1x86Port_Type.__name__ = "Integer32"
_RlLan1x86Port_Object = MibScalar
rlLan1x86Port = _RlLan1x86Port_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 224, 4),
    _RlLan1x86Port_Type()
)
rlLan1x86Port.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlLan1x86Port.setStatus("current")
_RlLan1x86VlanMappingTable_Object = MibTable
rlLan1x86VlanMappingTable = _RlLan1x86VlanMappingTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 224, 5)
)
if mibBuilder.loadTexts:
    rlLan1x86VlanMappingTable.setStatus("current")
_RlLan1x86VlanMappingEntry_Object = MibTableRow
rlLan1x86VlanMappingEntry = _RlLan1x86VlanMappingEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 224, 5, 1)
)
rlLan1x86VlanMappingEntry.setIndexNames(
    (0, "CISCOSBLAN1-MIB", "rlLan1x86VlanMappingVlanId"),
)
if mibBuilder.loadTexts:
    rlLan1x86VlanMappingEntry.setStatus("current")
_RlLan1x86VlanMappingVlanId_Type = VlanId
_RlLan1x86VlanMappingVlanId_Object = MibTableColumn
rlLan1x86VlanMappingVlanId = _RlLan1x86VlanMappingVlanId_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 224, 5, 1, 1),
    _RlLan1x86VlanMappingVlanId_Type()
)
rlLan1x86VlanMappingVlanId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlLan1x86VlanMappingVlanId.setStatus("current")
_RlLan1x86VlanMappingGroupId_Type = GroupId
_RlLan1x86VlanMappingGroupId_Object = MibTableColumn
rlLan1x86VlanMappingGroupId = _RlLan1x86VlanMappingGroupId_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 224, 5, 1, 2),
    _RlLan1x86VlanMappingGroupId_Type()
)
rlLan1x86VlanMappingGroupId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlLan1x86VlanMappingGroupId.setStatus("current")
_RlLan1x86VlanMappingRowStatus_Type = RowStatus
_RlLan1x86VlanMappingRowStatus_Object = MibTableColumn
rlLan1x86VlanMappingRowStatus = _RlLan1x86VlanMappingRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 224, 5, 1, 3),
    _RlLan1x86VlanMappingRowStatus_Type()
)
rlLan1x86VlanMappingRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rlLan1x86VlanMappingRowStatus.setStatus("current")
_RlLan1VfMacMappingTable_Object = MibTable
rlLan1VfMacMappingTable = _RlLan1VfMacMappingTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 224, 6)
)
if mibBuilder.loadTexts:
    rlLan1VfMacMappingTable.setStatus("current")
_RlLan1VfMacMappingEntry_Object = MibTableRow
rlLan1VfMacMappingEntry = _RlLan1VfMacMappingEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 224, 6, 1)
)
rlLan1VfMacMappingEntry.setIndexNames(
    (0, "CISCOSBLAN1-MIB", "rlLan1VfMacMappingDstMacAddress"),
)
if mibBuilder.loadTexts:
    rlLan1VfMacMappingEntry.setStatus("current")
_RlLan1VfMacMappingDstMacAddress_Type = MacAddress
_RlLan1VfMacMappingDstMacAddress_Object = MibTableColumn
rlLan1VfMacMappingDstMacAddress = _RlLan1VfMacMappingDstMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 224, 6, 1, 1),
    _RlLan1VfMacMappingDstMacAddress_Type()
)
rlLan1VfMacMappingDstMacAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlLan1VfMacMappingDstMacAddress.setStatus("current")
_RlLan1VfMacMappingVlanId_Type = VlanId
_RlLan1VfMacMappingVlanId_Object = MibTableColumn
rlLan1VfMacMappingVlanId = _RlLan1VfMacMappingVlanId_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 224, 6, 1, 2),
    _RlLan1VfMacMappingVlanId_Type()
)
rlLan1VfMacMappingVlanId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlLan1VfMacMappingVlanId.setStatus("current")


class _RlLan1VfMacMappingMulticast_Type(Integer32):
    """Custom type rlLan1VfMacMappingMulticast based on Integer32"""
    defaultValue = 1

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
          ("cp", 2),
          ("noncp", 3))
    )


_RlLan1VfMacMappingMulticast_Type.__name__ = "Integer32"
_RlLan1VfMacMappingMulticast_Object = MibTableColumn
rlLan1VfMacMappingMulticast = _RlLan1VfMacMappingMulticast_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 224, 6, 1, 3),
    _RlLan1VfMacMappingMulticast_Type()
)
rlLan1VfMacMappingMulticast.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlLan1VfMacMappingMulticast.setStatus("current")
_RlLan1VfMacMappingRowStatus_Type = RowStatus
_RlLan1VfMacMappingRowStatus_Object = MibTableColumn
rlLan1VfMacMappingRowStatus = _RlLan1VfMacMappingRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 224, 6, 1, 4),
    _RlLan1VfMacMappingRowStatus_Type()
)
rlLan1VfMacMappingRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rlLan1VfMacMappingRowStatus.setStatus("current")
_RlLan1ModulePortTable_Object = MibTable
rlLan1ModulePortTable = _RlLan1ModulePortTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 224, 7)
)
if mibBuilder.loadTexts:
    rlLan1ModulePortTable.setStatus("current")
_RlLan1ModulePortEntry_Object = MibTableRow
rlLan1ModulePortEntry = _RlLan1ModulePortEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 224, 7, 1)
)
rlLan1ModulePortEntry.setIndexNames(
    (0, "CISCOSBLAN1-MIB", "rlLan1ModulePortIfIndex"),
)
if mibBuilder.loadTexts:
    rlLan1ModulePortEntry.setStatus("current")


class _RlLan1ModulePortIfIndex_Type(Integer32):
    """Custom type rlLan1ModulePortIfIndex based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_RlLan1ModulePortIfIndex_Type.__name__ = "Integer32"
_RlLan1ModulePortIfIndex_Object = MibTableColumn
rlLan1ModulePortIfIndex = _RlLan1ModulePortIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 224, 7, 1, 1),
    _RlLan1ModulePortIfIndex_Type()
)
rlLan1ModulePortIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlLan1ModulePortIfIndex.setStatus("current")


class _RlLan1ModulePortCPAllowed_Type(TruthValue):
    """Custom type rlLan1ModulePortCPAllowed based on TruthValue"""
    defaultValue = 2


_RlLan1ModulePortCPAllowed_Type.__name__ = "TruthValue"
_RlLan1ModulePortCPAllowed_Object = MibTableColumn
rlLan1ModulePortCPAllowed = _RlLan1ModulePortCPAllowed_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 224, 7, 1, 2),
    _RlLan1ModulePortCPAllowed_Type()
)
rlLan1ModulePortCPAllowed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlLan1ModulePortCPAllowed.setStatus("current")


class _RlLan1ModulePortMulticastBroadcastAllowedVlan_Type(Integer32):
    """Custom type rlLan1ModulePortMulticastBroadcastAllowedVlan based on Integer32"""
    defaultValue = 1

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
          ("cp", 2),
          ("noncp", 3))
    )


_RlLan1ModulePortMulticastBroadcastAllowedVlan_Type.__name__ = "Integer32"
_RlLan1ModulePortMulticastBroadcastAllowedVlan_Object = MibTableColumn
rlLan1ModulePortMulticastBroadcastAllowedVlan = _RlLan1ModulePortMulticastBroadcastAllowedVlan_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 224, 7, 1, 3),
    _RlLan1ModulePortMulticastBroadcastAllowedVlan_Type()
)
rlLan1ModulePortMulticastBroadcastAllowedVlan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlLan1ModulePortMulticastBroadcastAllowedVlan.setStatus("current")


class _RlLan1ModulePortIngressGroupId_Type(GroupId):
    """Custom type rlLan1ModulePortIngressGroupId based on GroupId"""
    defaultValue = 0


_RlLan1ModulePortIngressGroupId_Type.__name__ = "GroupId"
_RlLan1ModulePortIngressGroupId_Object = MibTableColumn
rlLan1ModulePortIngressGroupId = _RlLan1ModulePortIngressGroupId_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 224, 7, 1, 4),
    _RlLan1ModulePortIngressGroupId_Type()
)
rlLan1ModulePortIngressGroupId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlLan1ModulePortIngressGroupId.setStatus("current")


class _RlLan1ModulePortEgressGroupIdList_Type(GroupIdList):
    """Custom type rlLan1ModulePortEgressGroupIdList based on GroupIdList"""
    defaultHexValue = ""


_RlLan1ModulePortEgressGroupIdList_Type.__name__ = "GroupIdList"
_RlLan1ModulePortEgressGroupIdList_Object = MibTableColumn
rlLan1ModulePortEgressGroupIdList = _RlLan1ModulePortEgressGroupIdList_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 224, 7, 1, 5),
    _RlLan1ModulePortEgressGroupIdList_Type()
)
rlLan1ModulePortEgressGroupIdList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlLan1ModulePortEgressGroupIdList.setStatus("current")
_RlLan1ModulePortRowStatus_Type = RowStatus
_RlLan1ModulePortRowStatus_Object = MibTableColumn
rlLan1ModulePortRowStatus = _RlLan1ModulePortRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 224, 7, 1, 6),
    _RlLan1ModulePortRowStatus_Type()
)
rlLan1ModulePortRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rlLan1ModulePortRowStatus.setStatus("current")
_RlLan1x86PfcTable_Object = MibTable
rlLan1x86PfcTable = _RlLan1x86PfcTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 224, 8)
)
if mibBuilder.loadTexts:
    rlLan1x86PfcTable.setStatus("current")
_RlLan1x86PfcEntry_Object = MibTableRow
rlLan1x86PfcEntry = _RlLan1x86PfcEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 224, 8, 1)
)
rlLan1x86PfcEntry.setIndexNames(
    (0, "CISCOSBLAN1-MIB", "rlLan1x86PriorityIndex"),
)
if mibBuilder.loadTexts:
    rlLan1x86PfcEntry.setStatus("current")


class _RlLan1x86PriorityIndex_Type(Integer32):
    """Custom type rlLan1x86PriorityIndex based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_RlLan1x86PriorityIndex_Type.__name__ = "Integer32"
_RlLan1x86PriorityIndex_Object = MibTableColumn
rlLan1x86PriorityIndex = _RlLan1x86PriorityIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 224, 8, 1, 1),
    _RlLan1x86PriorityIndex_Type()
)
rlLan1x86PriorityIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlLan1x86PriorityIndex.setStatus("current")


class _RlLan1x86PriorityIsLossy_Type(TruthValue):
    """Custom type rlLan1x86PriorityIsLossy based on TruthValue"""
    defaultValue = 1


_RlLan1x86PriorityIsLossy_Type.__name__ = "TruthValue"
_RlLan1x86PriorityIsLossy_Object = MibTableColumn
rlLan1x86PriorityIsLossy = _RlLan1x86PriorityIsLossy_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 224, 8, 1, 2),
    _RlLan1x86PriorityIsLossy_Type()
)
rlLan1x86PriorityIsLossy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlLan1x86PriorityIsLossy.setStatus("current")
_RlLan1x86PriorityXoffThreshold_Type = Integer32
_RlLan1x86PriorityXoffThreshold_Object = MibTableColumn
rlLan1x86PriorityXoffThreshold = _RlLan1x86PriorityXoffThreshold_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 224, 8, 1, 3),
    _RlLan1x86PriorityXoffThreshold_Type()
)
rlLan1x86PriorityXoffThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlLan1x86PriorityXoffThreshold.setStatus("current")
_RlLan1x86PriorityXonThreshold_Type = Integer32
_RlLan1x86PriorityXonThreshold_Object = MibTableColumn
rlLan1x86PriorityXonThreshold = _RlLan1x86PriorityXonThreshold_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 224, 8, 1, 4),
    _RlLan1x86PriorityXonThreshold_Type()
)
rlLan1x86PriorityXonThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlLan1x86PriorityXonThreshold.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCOSBLAN1-MIB",
    **{"GroupId": GroupId,
       "GroupIdList": GroupIdList,
       "VlanIdOrNone": VlanIdOrNone,
       "rlLan1": rlLan1,
       "rlLan1STagEtherType": rlLan1STagEtherType,
       "rlLan1CPVlanId": rlLan1CPVlanId,
       "rlLan1CPVlanCos": rlLan1CPVlanCos,
       "rlLan1x86Port": rlLan1x86Port,
       "rlLan1x86VlanMappingTable": rlLan1x86VlanMappingTable,
       "rlLan1x86VlanMappingEntry": rlLan1x86VlanMappingEntry,
       "rlLan1x86VlanMappingVlanId": rlLan1x86VlanMappingVlanId,
       "rlLan1x86VlanMappingGroupId": rlLan1x86VlanMappingGroupId,
       "rlLan1x86VlanMappingRowStatus": rlLan1x86VlanMappingRowStatus,
       "rlLan1VfMacMappingTable": rlLan1VfMacMappingTable,
       "rlLan1VfMacMappingEntry": rlLan1VfMacMappingEntry,
       "rlLan1VfMacMappingDstMacAddress": rlLan1VfMacMappingDstMacAddress,
       "rlLan1VfMacMappingVlanId": rlLan1VfMacMappingVlanId,
       "rlLan1VfMacMappingMulticast": rlLan1VfMacMappingMulticast,
       "rlLan1VfMacMappingRowStatus": rlLan1VfMacMappingRowStatus,
       "rlLan1ModulePortTable": rlLan1ModulePortTable,
       "rlLan1ModulePortEntry": rlLan1ModulePortEntry,
       "rlLan1ModulePortIfIndex": rlLan1ModulePortIfIndex,
       "rlLan1ModulePortCPAllowed": rlLan1ModulePortCPAllowed,
       "rlLan1ModulePortMulticastBroadcastAllowedVlan": rlLan1ModulePortMulticastBroadcastAllowedVlan,
       "rlLan1ModulePortIngressGroupId": rlLan1ModulePortIngressGroupId,
       "rlLan1ModulePortEgressGroupIdList": rlLan1ModulePortEgressGroupIdList,
       "rlLan1ModulePortRowStatus": rlLan1ModulePortRowStatus,
       "rlLan1x86PfcTable": rlLan1x86PfcTable,
       "rlLan1x86PfcEntry": rlLan1x86PfcEntry,
       "rlLan1x86PriorityIndex": rlLan1x86PriorityIndex,
       "rlLan1x86PriorityIsLossy": rlLan1x86PriorityIsLossy,
       "rlLan1x86PriorityXoffThreshold": rlLan1x86PriorityXoffThreshold,
       "rlLan1x86PriorityXonThreshold": rlLan1x86PriorityXonThreshold}
)
