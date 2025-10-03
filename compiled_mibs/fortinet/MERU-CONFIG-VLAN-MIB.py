# SNMP MIB module (MERU-CONFIG-VLAN-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\fortinet\MERU-CONFIG-VLAN-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:45:13 2025
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

(Ipv6Address,) = mibBuilder.importSymbols(
    "IPV6-TC",
    "Ipv6Address")

(mwConfiguration,) = mibBuilder.importSymbols(
    "MERU-SMI",
    "mwConfiguration")

(MwlAddressIfAssignmentType,
 MwlArrayDataTypeAction,
 MwlNmsInterfaceType,
 MwlOnOffSwitch,
 MwlProfileOwner) = mibBuilder.importSymbols(
    "MERU-TC",
    "MwlAddressIfAssignmentType",
    "MwlArrayDataTypeAction",
    "MwlNmsInterfaceType",
    "MwlOnOffSwitch",
    "MwlProfileOwner")

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

(DateAndTime,
 DisplayString,
 MacAddress,
 PhysAddress,
 RowStatus,
 TextualConvention,
 TimeInterval,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TimeInterval",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY

mwConfigVlan = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 5)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_MwVlanTable_Object = MibTable
mwVlanTable = _MwVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 5, 1)
)
if mibBuilder.loadTexts:
    mwVlanTable.setStatus("current")
_MwVlanEntry_Object = MibTableRow
mwVlanEntry = _MwVlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 5, 1, 1)
)
mwVlanEntry.setIndexNames(
    (0, "MERU-CONFIG-VLAN-MIB", "mwVlanTableIndex"),
)
if mibBuilder.loadTexts:
    mwVlanEntry.setStatus("current")
_MwVlanTableIndex_Type = Integer32
_MwVlanTableIndex_Object = MibTableColumn
mwVlanTableIndex = _MwVlanTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 5, 1, 1, 1),
    _MwVlanTableIndex_Type()
)
mwVlanTableIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mwVlanTableIndex.setStatus("current")
_MwVlanTag_Type = Unsigned32
_MwVlanTag_Object = MibTableColumn
mwVlanTag = _MwVlanTag_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 5, 1, 1, 2),
    _MwVlanTag_Type()
)
mwVlanTag.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mwVlanTag.setStatus("current")


class _MwVlanName_Type(DisplayString):
    """Custom type mwVlanName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_MwVlanName_Type.__name__ = "DisplayString"
_MwVlanName_Object = MibTableColumn
mwVlanName = _MwVlanName_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 5, 1, 1, 3),
    _MwVlanName_Type()
)
mwVlanName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mwVlanName.setStatus("current")
_MwVlanNetMask_Type = IpAddress
_MwVlanNetMask_Object = MibTableColumn
mwVlanNetMask = _MwVlanNetMask_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 5, 1, 1, 4),
    _MwVlanNetMask_Type()
)
mwVlanNetMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mwVlanNetMask.setStatus("current")
_MwVlanIpAddress_Type = IpAddress
_MwVlanIpAddress_Object = MibTableColumn
mwVlanIpAddress = _MwVlanIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 5, 1, 1, 5),
    _MwVlanIpAddress_Type()
)
mwVlanIpAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mwVlanIpAddress.setStatus("current")
_MwVlanInterfaceIndex_Type = Unsigned32
_MwVlanInterfaceIndex_Object = MibTableColumn
mwVlanInterfaceIndex = _MwVlanInterfaceIndex_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 5, 1, 1, 6),
    _MwVlanInterfaceIndex_Type()
)
mwVlanInterfaceIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mwVlanInterfaceIndex.setStatus("current")
_MwVlanDefaultGateway_Type = IpAddress
_MwVlanDefaultGateway_Object = MibTableColumn
mwVlanDefaultGateway = _MwVlanDefaultGateway_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 5, 1, 1, 7),
    _MwVlanDefaultGateway_Type()
)
mwVlanDefaultGateway.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mwVlanDefaultGateway.setStatus("current")
_MwVlanDHCPServerIpAddress_Type = IpAddress
_MwVlanDHCPServerIpAddress_Object = MibTableColumn
mwVlanDHCPServerIpAddress = _MwVlanDHCPServerIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 5, 1, 1, 8),
    _MwVlanDHCPServerIpAddress_Type()
)
mwVlanDHCPServerIpAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mwVlanDHCPServerIpAddress.setStatus("current")
_MwVlanDhcpRelayPassThroughFlag_Type = MwlOnOffSwitch
_MwVlanDhcpRelayPassThroughFlag_Object = MibTableColumn
mwVlanDhcpRelayPassThroughFlag = _MwVlanDhcpRelayPassThroughFlag_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 5, 1, 1, 9),
    _MwVlanDhcpRelayPassThroughFlag_Type()
)
mwVlanDhcpRelayPassThroughFlag.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mwVlanDhcpRelayPassThroughFlag.setStatus("current")
_MwVlanOverrideDefaultDHCPServer_Type = MwlOnOffSwitch
_MwVlanOverrideDefaultDHCPServer_Object = MibTableColumn
mwVlanOverrideDefaultDHCPServer = _MwVlanOverrideDefaultDHCPServer_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 5, 1, 1, 10),
    _MwVlanOverrideDefaultDHCPServer_Type()
)
mwVlanOverrideDefaultDHCPServer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mwVlanOverrideDefaultDHCPServer.setStatus("current")
_MwVlanOwner_Type = MwlProfileOwner
_MwVlanOwner_Object = MibTableColumn
mwVlanOwner = _MwVlanOwner_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 5, 1, 1, 11),
    _MwVlanOwner_Type()
)
mwVlanOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwVlanOwner.setStatus("current")
_MwVlanMaxNumberOfClients_Type = Unsigned32
_MwVlanMaxNumberOfClients_Object = MibTableColumn
mwVlanMaxNumberOfClients = _MwVlanMaxNumberOfClients_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 5, 1, 1, 13),
    _MwVlanMaxNumberOfClients_Type()
)
mwVlanMaxNumberOfClients.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mwVlanMaxNumberOfClients.setStatus("current")
_MwVlanRowStatus_Type = RowStatus
_MwVlanRowStatus_Object = MibTableColumn
mwVlanRowStatus = _MwVlanRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 5, 1, 1, 15),
    _MwVlanRowStatus_Type()
)
mwVlanRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mwVlanRowStatus.setStatus("current")
_MwVlanMgmtTable_Object = MibTable
mwVlanMgmtTable = _MwVlanMgmtTable_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 5, 2)
)
if mibBuilder.loadTexts:
    mwVlanMgmtTable.setStatus("current")
_MwVlanMgmtEntry_Object = MibTableRow
mwVlanMgmtEntry = _MwVlanMgmtEntry_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 5, 2, 1)
)
mwVlanMgmtEntry.setIndexNames(
    (0, "MERU-CONFIG-VLAN-MIB", "mwVlanMgmtTableIndex"),
)
if mibBuilder.loadTexts:
    mwVlanMgmtEntry.setStatus("current")
_MwVlanMgmtTableIndex_Type = Integer32
_MwVlanMgmtTableIndex_Object = MibTableColumn
mwVlanMgmtTableIndex = _MwVlanMgmtTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 5, 2, 1, 1),
    _MwVlanMgmtTableIndex_Type()
)
mwVlanMgmtTableIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mwVlanMgmtTableIndex.setStatus("current")
_MwVlanMgmtTag_Type = Unsigned32
_MwVlanMgmtTag_Object = MibTableColumn
mwVlanMgmtTag = _MwVlanMgmtTag_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 5, 2, 1, 2),
    _MwVlanMgmtTag_Type()
)
mwVlanMgmtTag.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mwVlanMgmtTag.setStatus("current")


class _MwVlanMgmtName_Type(DisplayString):
    """Custom type mwVlanMgmtName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_MwVlanMgmtName_Type.__name__ = "DisplayString"
_MwVlanMgmtName_Object = MibTableColumn
mwVlanMgmtName = _MwVlanMgmtName_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 5, 2, 1, 3),
    _MwVlanMgmtName_Type()
)
mwVlanMgmtName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mwVlanMgmtName.setStatus("current")
_MwVlanMgmtInterfaceIndex_Type = Unsigned32
_MwVlanMgmtInterfaceIndex_Object = MibTableColumn
mwVlanMgmtInterfaceIndex = _MwVlanMgmtInterfaceIndex_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 5, 2, 1, 4),
    _MwVlanMgmtInterfaceIndex_Type()
)
mwVlanMgmtInterfaceIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mwVlanMgmtInterfaceIndex.setStatus("current")
_MwVlanMgmtIpAddress_Type = IpAddress
_MwVlanMgmtIpAddress_Object = MibTableColumn
mwVlanMgmtIpAddress = _MwVlanMgmtIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 5, 2, 1, 5),
    _MwVlanMgmtIpAddress_Type()
)
mwVlanMgmtIpAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mwVlanMgmtIpAddress.setStatus("current")
_MwVlanMgmtNetMask_Type = IpAddress
_MwVlanMgmtNetMask_Object = MibTableColumn
mwVlanMgmtNetMask = _MwVlanMgmtNetMask_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 5, 2, 1, 6),
    _MwVlanMgmtNetMask_Type()
)
mwVlanMgmtNetMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mwVlanMgmtNetMask.setStatus("current")
_MwVlanMgmtDefaultGateway_Type = IpAddress
_MwVlanMgmtDefaultGateway_Object = MibTableColumn
mwVlanMgmtDefaultGateway = _MwVlanMgmtDefaultGateway_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 5, 2, 1, 7),
    _MwVlanMgmtDefaultGateway_Type()
)
mwVlanMgmtDefaultGateway.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mwVlanMgmtDefaultGateway.setStatus("current")
_MwVlanMgmtAssignedType_Type = MwlAddressIfAssignmentType
_MwVlanMgmtAssignedType_Object = MibTableColumn
mwVlanMgmtAssignedType = _MwVlanMgmtAssignedType_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 5, 2, 1, 8),
    _MwVlanMgmtAssignedType_Type()
)
mwVlanMgmtAssignedType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwVlanMgmtAssignedType.setStatus("current")
_MwVlanMgmtInterfaceType_Type = MwlNmsInterfaceType
_MwVlanMgmtInterfaceType_Object = MibTableColumn
mwVlanMgmtInterfaceType = _MwVlanMgmtInterfaceType_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 5, 2, 1, 9),
    _MwVlanMgmtInterfaceType_Type()
)
mwVlanMgmtInterfaceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwVlanMgmtInterfaceType.setStatus("current")
_MwVlanMgmtRowStatus_Type = RowStatus
_MwVlanMgmtRowStatus_Object = MibTableColumn
mwVlanMgmtRowStatus = _MwVlanMgmtRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 5, 2, 1, 11),
    _MwVlanMgmtRowStatus_Type()
)
mwVlanMgmtRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mwVlanMgmtRowStatus.setStatus("current")
_MwVlanPoolTable_Object = MibTable
mwVlanPoolTable = _MwVlanPoolTable_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 5, 3)
)
if mibBuilder.loadTexts:
    mwVlanPoolTable.setStatus("current")
_MwVlanPoolEntry_Object = MibTableRow
mwVlanPoolEntry = _MwVlanPoolEntry_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 5, 3, 1)
)
mwVlanPoolEntry.setIndexNames(
    (0, "MERU-CONFIG-VLAN-MIB", "mwVlanPoolTableIndex"),
)
if mibBuilder.loadTexts:
    mwVlanPoolEntry.setStatus("current")
_MwVlanPoolTableIndex_Type = Integer32
_MwVlanPoolTableIndex_Object = MibTableColumn
mwVlanPoolTableIndex = _MwVlanPoolTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 5, 3, 1, 1),
    _MwVlanPoolTableIndex_Type()
)
mwVlanPoolTableIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mwVlanPoolTableIndex.setStatus("current")


class _MwVlanPoolName_Type(DisplayString):
    """Custom type mwVlanPoolName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_MwVlanPoolName_Type.__name__ = "DisplayString"
_MwVlanPoolName_Object = MibTableColumn
mwVlanPoolName = _MwVlanPoolName_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 5, 3, 1, 3),
    _MwVlanPoolName_Type()
)
mwVlanPoolName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mwVlanPoolName.setStatus("current")
_MwVlanPoolTagList_Type = DisplayString
_MwVlanPoolTagList_Object = MibTableColumn
mwVlanPoolTagList = _MwVlanPoolTagList_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 5, 3, 1, 4),
    _MwVlanPoolTagList_Type()
)
mwVlanPoolTagList.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mwVlanPoolTagList.setStatus("current")
_MwVlanPoolOwner_Type = MwlProfileOwner
_MwVlanPoolOwner_Object = MibTableColumn
mwVlanPoolOwner = _MwVlanPoolOwner_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 5, 3, 1, 5),
    _MwVlanPoolOwner_Type()
)
mwVlanPoolOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwVlanPoolOwner.setStatus("current")
_MwVlanPoolRowStatus_Type = RowStatus
_MwVlanPoolRowStatus_Object = MibTableColumn
mwVlanPoolRowStatus = _MwVlanPoolRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 5, 3, 1, 6),
    _MwVlanPoolRowStatus_Type()
)
mwVlanPoolRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mwVlanPoolRowStatus.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "MERU-CONFIG-VLAN-MIB",
    **{"mwConfigVlan": mwConfigVlan,
       "mwVlanTable": mwVlanTable,
       "mwVlanEntry": mwVlanEntry,
       "mwVlanTableIndex": mwVlanTableIndex,
       "mwVlanTag": mwVlanTag,
       "mwVlanName": mwVlanName,
       "mwVlanNetMask": mwVlanNetMask,
       "mwVlanIpAddress": mwVlanIpAddress,
       "mwVlanInterfaceIndex": mwVlanInterfaceIndex,
       "mwVlanDefaultGateway": mwVlanDefaultGateway,
       "mwVlanDHCPServerIpAddress": mwVlanDHCPServerIpAddress,
       "mwVlanDhcpRelayPassThroughFlag": mwVlanDhcpRelayPassThroughFlag,
       "mwVlanOverrideDefaultDHCPServer": mwVlanOverrideDefaultDHCPServer,
       "mwVlanOwner": mwVlanOwner,
       "mwVlanMaxNumberOfClients": mwVlanMaxNumberOfClients,
       "mwVlanRowStatus": mwVlanRowStatus,
       "mwVlanMgmtTable": mwVlanMgmtTable,
       "mwVlanMgmtEntry": mwVlanMgmtEntry,
       "mwVlanMgmtTableIndex": mwVlanMgmtTableIndex,
       "mwVlanMgmtTag": mwVlanMgmtTag,
       "mwVlanMgmtName": mwVlanMgmtName,
       "mwVlanMgmtInterfaceIndex": mwVlanMgmtInterfaceIndex,
       "mwVlanMgmtIpAddress": mwVlanMgmtIpAddress,
       "mwVlanMgmtNetMask": mwVlanMgmtNetMask,
       "mwVlanMgmtDefaultGateway": mwVlanMgmtDefaultGateway,
       "mwVlanMgmtAssignedType": mwVlanMgmtAssignedType,
       "mwVlanMgmtInterfaceType": mwVlanMgmtInterfaceType,
       "mwVlanMgmtRowStatus": mwVlanMgmtRowStatus,
       "mwVlanPoolTable": mwVlanPoolTable,
       "mwVlanPoolEntry": mwVlanPoolEntry,
       "mwVlanPoolTableIndex": mwVlanPoolTableIndex,
       "mwVlanPoolName": mwVlanPoolName,
       "mwVlanPoolTagList": mwVlanPoolTagList,
       "mwVlanPoolOwner": mwVlanPoolOwner,
       "mwVlanPoolRowStatus": mwVlanPoolRowStatus}
)
