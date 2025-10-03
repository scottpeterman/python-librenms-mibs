# SNMP MIB module (TN-IP-SOURCE-GUARD-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\transition\TN-IP-SOURCE-GUARD-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 12:31:39 2025
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

(entPhysicalIndex,) = mibBuilder.importSymbols(
    "ENTITY-MIB",
    "entPhysicalIndex")

(InterfaceIndex,
 ifIndex) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
    "ifIndex")

(InetAddress,
 InetAddressPrefixLength,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressPrefixLength",
    "InetAddressType")

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
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TimeStamp",
    "TruthValue")

(tnProducts,) = mibBuilder.importSymbols(
    "TRANSITION-SMI",
    "tnProducts")


# MODULE-IDENTITY

tnIPSourceGuardMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 31)
)
if mibBuilder.loadTexts:
    tnIPSourceGuardMIB.setRevisions(
        ("2012-09-26 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_TnIPSourceGuardMIBObjects_ObjectIdentity = ObjectIdentity
tnIPSourceGuardMIBObjects = _TnIPSourceGuardMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 31, 1)
)
_TnIPSourceGuardMgmt_ObjectIdentity = ObjectIdentity
tnIPSourceGuardMgmt = _TnIPSourceGuardMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 31, 1, 1)
)
_TnIPSourceGuardTable_Object = MibTable
tnIPSourceGuardTable = _TnIPSourceGuardTable_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 31, 1, 1, 1)
)
if mibBuilder.loadTexts:
    tnIPSourceGuardTable.setStatus("current")
_TnIPSourceGuardEntry_Object = MibTableRow
tnIPSourceGuardEntry = _TnIPSourceGuardEntry_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 31, 1, 1, 1, 1)
)
tnIPSourceGuardEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
)
if mibBuilder.loadTexts:
    tnIPSourceGuardEntry.setStatus("current")


class _TnIPSourceGuardGlobalMode_Type(TruthValue):
    """Custom type tnIPSourceGuardGlobalMode based on TruthValue"""
    defaultValue = 2


_TnIPSourceGuardGlobalMode_Type.__name__ = "TruthValue"
_TnIPSourceGuardGlobalMode_Object = MibTableColumn
tnIPSourceGuardGlobalMode = _TnIPSourceGuardGlobalMode_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 31, 1, 1, 1, 1, 1),
    _TnIPSourceGuardGlobalMode_Type()
)
tnIPSourceGuardGlobalMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnIPSourceGuardGlobalMode.setStatus("current")


class _TnIPSourceGuardDynamicToStatic_Type(TruthValue):
    """Custom type tnIPSourceGuardDynamicToStatic based on TruthValue"""
    defaultValue = 2


_TnIPSourceGuardDynamicToStatic_Type.__name__ = "TruthValue"
_TnIPSourceGuardDynamicToStatic_Object = MibTableColumn
tnIPSourceGuardDynamicToStatic = _TnIPSourceGuardDynamicToStatic_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 31, 1, 1, 1, 1, 2),
    _TnIPSourceGuardDynamicToStatic_Type()
)
tnIPSourceGuardDynamicToStatic.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnIPSourceGuardDynamicToStatic.setStatus("current")
_TnIPSourceGuardIfTable_Object = MibTable
tnIPSourceGuardIfTable = _TnIPSourceGuardIfTable_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 31, 1, 1, 2)
)
if mibBuilder.loadTexts:
    tnIPSourceGuardIfTable.setStatus("current")
_TnIPSourceGuardIfEntry_Object = MibTableRow
tnIPSourceGuardIfEntry = _TnIPSourceGuardIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 31, 1, 1, 2, 1)
)
tnIPSourceGuardIfEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    tnIPSourceGuardIfEntry.setStatus("current")


class _TnIPSourceGuardIfMode_Type(TruthValue):
    """Custom type tnIPSourceGuardIfMode based on TruthValue"""
    defaultValue = 2


_TnIPSourceGuardIfMode_Type.__name__ = "TruthValue"
_TnIPSourceGuardIfMode_Object = MibTableColumn
tnIPSourceGuardIfMode = _TnIPSourceGuardIfMode_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 31, 1, 1, 2, 1, 1),
    _TnIPSourceGuardIfMode_Type()
)
tnIPSourceGuardIfMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnIPSourceGuardIfMode.setStatus("current")


class _TnIPSourceGuardIfMaxDynamicClients_Type(Integer32):
    """Custom type tnIPSourceGuardIfMaxDynamicClients based on Integer32"""
    defaultValue = 65535

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              65535)
        )
    )
    namedValues = NamedValues(
        *(("zero", 0),
          ("one", 1),
          ("two", 2),
          ("unlimited", 65535))
    )


_TnIPSourceGuardIfMaxDynamicClients_Type.__name__ = "Integer32"
_TnIPSourceGuardIfMaxDynamicClients_Object = MibTableColumn
tnIPSourceGuardIfMaxDynamicClients = _TnIPSourceGuardIfMaxDynamicClients_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 31, 1, 1, 2, 1, 2),
    _TnIPSourceGuardIfMaxDynamicClients_Type()
)
tnIPSourceGuardIfMaxDynamicClients.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnIPSourceGuardIfMaxDynamicClients.setStatus("current")
_TnIPSourceGuardStaticTable_Object = MibTable
tnIPSourceGuardStaticTable = _TnIPSourceGuardStaticTable_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 31, 1, 1, 3)
)
if mibBuilder.loadTexts:
    tnIPSourceGuardStaticTable.setStatus("current")
_TnIPSourceGuardStaticEntry_Object = MibTableRow
tnIPSourceGuardStaticEntry = _TnIPSourceGuardStaticEntry_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 31, 1, 1, 3, 1)
)
tnIPSourceGuardStaticEntry.setIndexNames(
    (0, "TN-IP-SOURCE-GUARD-MIB", "tnIPSourceGuardStaticPort"),
    (0, "TN-IP-SOURCE-GUARD-MIB", "tnIPSourceGuardStaticVlanID"),
    (0, "TN-IP-SOURCE-GUARD-MIB", "tnIPSourceGuardStaticAddrType"),
    (0, "TN-IP-SOURCE-GUARD-MIB", "tnIPSourceGuardStaticAddr"),
    (0, "TN-IP-SOURCE-GUARD-MIB", "tnIPSourceGuardStaticMask"),
)
if mibBuilder.loadTexts:
    tnIPSourceGuardStaticEntry.setStatus("current")
_TnIPSourceGuardStaticPort_Type = InterfaceIndex
_TnIPSourceGuardStaticPort_Object = MibTableColumn
tnIPSourceGuardStaticPort = _TnIPSourceGuardStaticPort_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 31, 1, 1, 3, 1, 1),
    _TnIPSourceGuardStaticPort_Type()
)
tnIPSourceGuardStaticPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnIPSourceGuardStaticPort.setStatus("current")


class _TnIPSourceGuardStaticVlanID_Type(Integer32):
    """Custom type tnIPSourceGuardStaticVlanID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_TnIPSourceGuardStaticVlanID_Type.__name__ = "Integer32"
_TnIPSourceGuardStaticVlanID_Object = MibTableColumn
tnIPSourceGuardStaticVlanID = _TnIPSourceGuardStaticVlanID_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 31, 1, 1, 3, 1, 2),
    _TnIPSourceGuardStaticVlanID_Type()
)
tnIPSourceGuardStaticVlanID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnIPSourceGuardStaticVlanID.setStatus("current")
_TnIPSourceGuardStaticAddrType_Type = InetAddressType
_TnIPSourceGuardStaticAddrType_Object = MibTableColumn
tnIPSourceGuardStaticAddrType = _TnIPSourceGuardStaticAddrType_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 31, 1, 1, 3, 1, 3),
    _TnIPSourceGuardStaticAddrType_Type()
)
tnIPSourceGuardStaticAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnIPSourceGuardStaticAddrType.setStatus("current")
_TnIPSourceGuardStaticAddr_Type = InetAddress
_TnIPSourceGuardStaticAddr_Object = MibTableColumn
tnIPSourceGuardStaticAddr = _TnIPSourceGuardStaticAddr_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 31, 1, 1, 3, 1, 4),
    _TnIPSourceGuardStaticAddr_Type()
)
tnIPSourceGuardStaticAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnIPSourceGuardStaticAddr.setStatus("current")
_TnIPSourceGuardStaticMask_Type = InetAddressPrefixLength
_TnIPSourceGuardStaticMask_Object = MibTableColumn
tnIPSourceGuardStaticMask = _TnIPSourceGuardStaticMask_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 31, 1, 1, 3, 1, 5),
    _TnIPSourceGuardStaticMask_Type()
)
tnIPSourceGuardStaticMask.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnIPSourceGuardStaticMask.setStatus("current")
_TnIPSourceGuardStaticMacAddress_Type = MacAddress
_TnIPSourceGuardStaticMacAddress_Object = MibTableColumn
tnIPSourceGuardStaticMacAddress = _TnIPSourceGuardStaticMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 31, 1, 1, 3, 1, 6),
    _TnIPSourceGuardStaticMacAddress_Type()
)
tnIPSourceGuardStaticMacAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnIPSourceGuardStaticMacAddress.setStatus("current")
_TnIPSourceGuardStaticRowStatus_Type = RowStatus
_TnIPSourceGuardStaticRowStatus_Object = MibTableColumn
tnIPSourceGuardStaticRowStatus = _TnIPSourceGuardStaticRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 31, 1, 1, 3, 1, 7),
    _TnIPSourceGuardStaticRowStatus_Type()
)
tnIPSourceGuardStaticRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnIPSourceGuardStaticRowStatus.setStatus("current")
_TnIPSourceGuardDynamicTable_Object = MibTable
tnIPSourceGuardDynamicTable = _TnIPSourceGuardDynamicTable_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 31, 1, 1, 4)
)
if mibBuilder.loadTexts:
    tnIPSourceGuardDynamicTable.setStatus("current")
_TnIPSourceGuardDynamicEntry_Object = MibTableRow
tnIPSourceGuardDynamicEntry = _TnIPSourceGuardDynamicEntry_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 31, 1, 1, 4, 1)
)
tnIPSourceGuardDynamicEntry.setIndexNames(
    (0, "TN-IP-SOURCE-GUARD-MIB", "tnIPSourceGuardDynamicPort"),
    (0, "TN-IP-SOURCE-GUARD-MIB", "tnIPSourceGuardDynamicVlanID"),
    (0, "TN-IP-SOURCE-GUARD-MIB", "tnIPSourceGuardDynamicAddrType"),
    (0, "TN-IP-SOURCE-GUARD-MIB", "tnIPSourceGuardDynamicAddr"),
    (0, "TN-IP-SOURCE-GUARD-MIB", "tnIPSourceGuardDynamicMask"),
)
if mibBuilder.loadTexts:
    tnIPSourceGuardDynamicEntry.setStatus("current")
_TnIPSourceGuardDynamicPort_Type = InterfaceIndex
_TnIPSourceGuardDynamicPort_Object = MibTableColumn
tnIPSourceGuardDynamicPort = _TnIPSourceGuardDynamicPort_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 31, 1, 1, 4, 1, 1),
    _TnIPSourceGuardDynamicPort_Type()
)
tnIPSourceGuardDynamicPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnIPSourceGuardDynamicPort.setStatus("current")


class _TnIPSourceGuardDynamicVlanID_Type(Integer32):
    """Custom type tnIPSourceGuardDynamicVlanID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_TnIPSourceGuardDynamicVlanID_Type.__name__ = "Integer32"
_TnIPSourceGuardDynamicVlanID_Object = MibTableColumn
tnIPSourceGuardDynamicVlanID = _TnIPSourceGuardDynamicVlanID_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 31, 1, 1, 4, 1, 2),
    _TnIPSourceGuardDynamicVlanID_Type()
)
tnIPSourceGuardDynamicVlanID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnIPSourceGuardDynamicVlanID.setStatus("current")
_TnIPSourceGuardDynamicAddrType_Type = InetAddressType
_TnIPSourceGuardDynamicAddrType_Object = MibTableColumn
tnIPSourceGuardDynamicAddrType = _TnIPSourceGuardDynamicAddrType_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 31, 1, 1, 4, 1, 3),
    _TnIPSourceGuardDynamicAddrType_Type()
)
tnIPSourceGuardDynamicAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnIPSourceGuardDynamicAddrType.setStatus("current")
_TnIPSourceGuardDynamicAddr_Type = InetAddress
_TnIPSourceGuardDynamicAddr_Object = MibTableColumn
tnIPSourceGuardDynamicAddr = _TnIPSourceGuardDynamicAddr_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 31, 1, 1, 4, 1, 4),
    _TnIPSourceGuardDynamicAddr_Type()
)
tnIPSourceGuardDynamicAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnIPSourceGuardDynamicAddr.setStatus("current")
_TnIPSourceGuardDynamicMask_Type = InetAddressPrefixLength
_TnIPSourceGuardDynamicMask_Object = MibTableColumn
tnIPSourceGuardDynamicMask = _TnIPSourceGuardDynamicMask_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 31, 1, 1, 4, 1, 5),
    _TnIPSourceGuardDynamicMask_Type()
)
tnIPSourceGuardDynamicMask.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnIPSourceGuardDynamicMask.setStatus("current")
_TnIPSourceGuardDynamicMacAddress_Type = MacAddress
_TnIPSourceGuardDynamicMacAddress_Object = MibTableColumn
tnIPSourceGuardDynamicMacAddress = _TnIPSourceGuardDynamicMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 31, 1, 1, 4, 1, 6),
    _TnIPSourceGuardDynamicMacAddress_Type()
)
tnIPSourceGuardDynamicMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnIPSourceGuardDynamicMacAddress.setStatus("current")
_TnIPSourceGuardMIBNotifications_ObjectIdentity = ObjectIdentity
tnIPSourceGuardMIBNotifications = _TnIPSourceGuardMIBNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 31, 2)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TN-IP-SOURCE-GUARD-MIB",
    **{"tnIPSourceGuardMIB": tnIPSourceGuardMIB,
       "tnIPSourceGuardMIBObjects": tnIPSourceGuardMIBObjects,
       "tnIPSourceGuardMgmt": tnIPSourceGuardMgmt,
       "tnIPSourceGuardTable": tnIPSourceGuardTable,
       "tnIPSourceGuardEntry": tnIPSourceGuardEntry,
       "tnIPSourceGuardGlobalMode": tnIPSourceGuardGlobalMode,
       "tnIPSourceGuardDynamicToStatic": tnIPSourceGuardDynamicToStatic,
       "tnIPSourceGuardIfTable": tnIPSourceGuardIfTable,
       "tnIPSourceGuardIfEntry": tnIPSourceGuardIfEntry,
       "tnIPSourceGuardIfMode": tnIPSourceGuardIfMode,
       "tnIPSourceGuardIfMaxDynamicClients": tnIPSourceGuardIfMaxDynamicClients,
       "tnIPSourceGuardStaticTable": tnIPSourceGuardStaticTable,
       "tnIPSourceGuardStaticEntry": tnIPSourceGuardStaticEntry,
       "tnIPSourceGuardStaticPort": tnIPSourceGuardStaticPort,
       "tnIPSourceGuardStaticVlanID": tnIPSourceGuardStaticVlanID,
       "tnIPSourceGuardStaticAddrType": tnIPSourceGuardStaticAddrType,
       "tnIPSourceGuardStaticAddr": tnIPSourceGuardStaticAddr,
       "tnIPSourceGuardStaticMask": tnIPSourceGuardStaticMask,
       "tnIPSourceGuardStaticMacAddress": tnIPSourceGuardStaticMacAddress,
       "tnIPSourceGuardStaticRowStatus": tnIPSourceGuardStaticRowStatus,
       "tnIPSourceGuardDynamicTable": tnIPSourceGuardDynamicTable,
       "tnIPSourceGuardDynamicEntry": tnIPSourceGuardDynamicEntry,
       "tnIPSourceGuardDynamicPort": tnIPSourceGuardDynamicPort,
       "tnIPSourceGuardDynamicVlanID": tnIPSourceGuardDynamicVlanID,
       "tnIPSourceGuardDynamicAddrType": tnIPSourceGuardDynamicAddrType,
       "tnIPSourceGuardDynamicAddr": tnIPSourceGuardDynamicAddr,
       "tnIPSourceGuardDynamicMask": tnIPSourceGuardDynamicMask,
       "tnIPSourceGuardDynamicMacAddress": tnIPSourceGuardDynamicMacAddress,
       "tnIPSourceGuardMIBNotifications": tnIPSourceGuardMIBNotifications}
)
