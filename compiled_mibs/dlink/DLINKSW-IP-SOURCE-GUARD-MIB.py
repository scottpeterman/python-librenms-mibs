# SNMP MIB module (DLINKSW-IP-SOURCE-GUARD-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\dlink\DLINKSW-IP-SOURCE-GUARD-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:37:16 2025
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

(Dlink2kVlanList,) = mibBuilder.importSymbols(
    "DLINKSW-TC-MIB",
    "Dlink2kVlanList")

(InterfaceIndex,
 ifIndex) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
    "ifIndex")

(InetAddressIPv4,) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddressIPv4")

(VlanId,) = mibBuilder.importSymbols(
    "Q-BRIDGE-MIB",
    "VlanId")

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
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

dlinkSwIpSourceGuardMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 132)
)
if mibBuilder.loadTexts:
    dlinkSwIpSourceGuardMIB.setRevisions(
        ("2013-07-18 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_DIpSourceGuardMIBNotifs_ObjectIdentity = ObjectIdentity
dIpSourceGuardMIBNotifs = _DIpSourceGuardMIBNotifs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 132, 0)
)
_DIpSourceGuardMIBObjects_ObjectIdentity = ObjectIdentity
dIpSourceGuardMIBObjects = _DIpSourceGuardMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 132, 1)
)
_DIpsgBindings_ObjectIdentity = ObjectIdentity
dIpsgBindings = _DIpsgBindings_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 132, 1, 1)
)
_DIpsgStaticBindingsTable_Object = MibTable
dIpsgStaticBindingsTable = _DIpsgStaticBindingsTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 132, 1, 1, 1)
)
if mibBuilder.loadTexts:
    dIpsgStaticBindingsTable.setStatus("current")
_DIpsgStaticBindingsEntry_Object = MibTableRow
dIpsgStaticBindingsEntry = _DIpsgStaticBindingsEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 132, 1, 1, 1, 1)
)
dIpsgStaticBindingsEntry.setIndexNames(
    (0, "DLINKSW-IP-SOURCE-GUARD-MIB", "dIpsgStaticBindingsVlan"),
    (0, "DLINKSW-IP-SOURCE-GUARD-MIB", "dIpsgStaticBindingsMacAddress"),
    (0, "DLINKSW-IP-SOURCE-GUARD-MIB", "dIpsgStaticBindingsIpAddress"),
    (0, "DLINKSW-IP-SOURCE-GUARD-MIB", "dIpsgStaticBindingsInterface"),
)
if mibBuilder.loadTexts:
    dIpsgStaticBindingsEntry.setStatus("current")
_DIpsgStaticBindingsVlan_Type = VlanId
_DIpsgStaticBindingsVlan_Object = MibTableColumn
dIpsgStaticBindingsVlan = _DIpsgStaticBindingsVlan_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 132, 1, 1, 1, 1, 1),
    _DIpsgStaticBindingsVlan_Type()
)
dIpsgStaticBindingsVlan.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dIpsgStaticBindingsVlan.setStatus("current")
_DIpsgStaticBindingsMacAddress_Type = MacAddress
_DIpsgStaticBindingsMacAddress_Object = MibTableColumn
dIpsgStaticBindingsMacAddress = _DIpsgStaticBindingsMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 132, 1, 1, 1, 1, 2),
    _DIpsgStaticBindingsMacAddress_Type()
)
dIpsgStaticBindingsMacAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dIpsgStaticBindingsMacAddress.setStatus("current")
_DIpsgStaticBindingsIpAddress_Type = InetAddressIPv4
_DIpsgStaticBindingsIpAddress_Object = MibTableColumn
dIpsgStaticBindingsIpAddress = _DIpsgStaticBindingsIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 132, 1, 1, 1, 1, 3),
    _DIpsgStaticBindingsIpAddress_Type()
)
dIpsgStaticBindingsIpAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dIpsgStaticBindingsIpAddress.setStatus("current")
_DIpsgStaticBindingsInterface_Type = InterfaceIndex
_DIpsgStaticBindingsInterface_Object = MibTableColumn
dIpsgStaticBindingsInterface = _DIpsgStaticBindingsInterface_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 132, 1, 1, 1, 1, 4),
    _DIpsgStaticBindingsInterface_Type()
)
dIpsgStaticBindingsInterface.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dIpsgStaticBindingsInterface.setStatus("current")
_DIpsgStaticBindingsRowStatus_Type = RowStatus
_DIpsgStaticBindingsRowStatus_Object = MibTableColumn
dIpsgStaticBindingsRowStatus = _DIpsgStaticBindingsRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 132, 1, 1, 1, 1, 99),
    _DIpsgStaticBindingsRowStatus_Type()
)
dIpsgStaticBindingsRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dIpsgStaticBindingsRowStatus.setStatus("current")
_DIpsgSrcGuard_ObjectIdentity = ObjectIdentity
dIpsgSrcGuard = _DIpsgSrcGuard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 132, 1, 2)
)
_DIpsgIfSrcGuardConfigTable_Object = MibTable
dIpsgIfSrcGuardConfigTable = _DIpsgIfSrcGuardConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 132, 1, 2, 1)
)
if mibBuilder.loadTexts:
    dIpsgIfSrcGuardConfigTable.setStatus("current")
_DIpsgIfSrcGuardConfigEntry_Object = MibTableRow
dIpsgIfSrcGuardConfigEntry = _DIpsgIfSrcGuardConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 132, 1, 2, 1, 1)
)
dIpsgIfSrcGuardConfigEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    dIpsgIfSrcGuardConfigEntry.setStatus("current")


class _DIpsgIfSrcGuardFilterType_Type(Integer32):
    """Custom type dIpsgIfSrcGuardFilterType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("ip", 2),
          ("ipMac", 3))
    )


_DIpsgIfSrcGuardFilterType_Type.__name__ = "Integer32"
_DIpsgIfSrcGuardFilterType_Object = MibTableColumn
dIpsgIfSrcGuardFilterType = _DIpsgIfSrcGuardFilterType_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 132, 1, 2, 1, 1, 1),
    _DIpsgIfSrcGuardFilterType_Type()
)
dIpsgIfSrcGuardFilterType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dIpsgIfSrcGuardFilterType.setStatus("current")
_DIpsgIfSrcGuardAddrTable_Object = MibTable
dIpsgIfSrcGuardAddrTable = _DIpsgIfSrcGuardAddrTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 132, 1, 2, 2)
)
if mibBuilder.loadTexts:
    dIpsgIfSrcGuardAddrTable.setStatus("current")
_DIpsgIfSrcGuardAddrEntry_Object = MibTableRow
dIpsgIfSrcGuardAddrEntry = _DIpsgIfSrcGuardAddrEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 132, 1, 2, 2, 1)
)
dIpsgIfSrcGuardAddrEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "DLINKSW-IP-SOURCE-GUARD-MIB", "dIpsgIfSrcGuardIndex"),
)
if mibBuilder.loadTexts:
    dIpsgIfSrcGuardAddrEntry.setStatus("current")


class _DIpsgIfSrcGuardIndex_Type(Unsigned32):
    """Custom type dIpsgIfSrcGuardIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_DIpsgIfSrcGuardIndex_Type.__name__ = "Unsigned32"
_DIpsgIfSrcGuardIndex_Object = MibTableColumn
dIpsgIfSrcGuardIndex = _DIpsgIfSrcGuardIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 132, 1, 2, 2, 1, 1),
    _DIpsgIfSrcGuardIndex_Type()
)
dIpsgIfSrcGuardIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dIpsgIfSrcGuardIndex.setStatus("current")


class _DIpsgIfSrcGuardFilterMode_Type(Integer32):
    """Custom type dIpsgIfSrcGuardFilterMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("inactiveTrustPort", 2),
          ("inactiveNoSnoopingVlan", 3))
    )


_DIpsgIfSrcGuardFilterMode_Type.__name__ = "Integer32"
_DIpsgIfSrcGuardFilterMode_Object = MibTableColumn
dIpsgIfSrcGuardFilterMode = _DIpsgIfSrcGuardFilterMode_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 132, 1, 2, 2, 1, 2),
    _DIpsgIfSrcGuardFilterMode_Type()
)
dIpsgIfSrcGuardFilterMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dIpsgIfSrcGuardFilterMode.setStatus("current")
_DIpsgIfSrcGuardIpAddress_Type = InetAddressIPv4
_DIpsgIfSrcGuardIpAddress_Object = MibTableColumn
dIpsgIfSrcGuardIpAddress = _DIpsgIfSrcGuardIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 132, 1, 2, 2, 1, 3),
    _DIpsgIfSrcGuardIpAddress_Type()
)
dIpsgIfSrcGuardIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dIpsgIfSrcGuardIpAddress.setStatus("current")


class _DIpsgIfSrcGuardIpFilterAction_Type(Integer32):
    """Custom type dIpsgIfSrcGuardIpFilterAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("permitIpAddress", 1),
          ("permitAllIpAdress", 2),
          ("denyAllIpAddress", 3))
    )


_DIpsgIfSrcGuardIpFilterAction_Type.__name__ = "Integer32"
_DIpsgIfSrcGuardIpFilterAction_Object = MibTableColumn
dIpsgIfSrcGuardIpFilterAction = _DIpsgIfSrcGuardIpFilterAction_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 132, 1, 2, 2, 1, 4),
    _DIpsgIfSrcGuardIpFilterAction_Type()
)
dIpsgIfSrcGuardIpFilterAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dIpsgIfSrcGuardIpFilterAction.setStatus("current")
_DIpsgIfSrcGuardMacAddress_Type = MacAddress
_DIpsgIfSrcGuardMacAddress_Object = MibTableColumn
dIpsgIfSrcGuardMacAddress = _DIpsgIfSrcGuardMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 132, 1, 2, 2, 1, 5),
    _DIpsgIfSrcGuardMacAddress_Type()
)
dIpsgIfSrcGuardMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dIpsgIfSrcGuardMacAddress.setStatus("current")


class _DIpsgIfSrcGuardMacFilterAction_Type(Integer32):
    """Custom type dIpsgIfSrcGuardMacFilterAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("allowMacAddress", 1),
          ("permitAllMacAddresses", 2))
    )


_DIpsgIfSrcGuardMacFilterAction_Type.__name__ = "Integer32"
_DIpsgIfSrcGuardMacFilterAction_Object = MibTableColumn
dIpsgIfSrcGuardMacFilterAction = _DIpsgIfSrcGuardMacFilterAction_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 132, 1, 2, 2, 1, 6),
    _DIpsgIfSrcGuardMacFilterAction_Type()
)
dIpsgIfSrcGuardMacFilterAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dIpsgIfSrcGuardMacFilterAction.setStatus("current")
_DIpsgIfSrcGuardVlansFirst2K_Type = Dlink2kVlanList
_DIpsgIfSrcGuardVlansFirst2K_Object = MibTableColumn
dIpsgIfSrcGuardVlansFirst2K = _DIpsgIfSrcGuardVlansFirst2K_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 132, 1, 2, 2, 1, 7),
    _DIpsgIfSrcGuardVlansFirst2K_Type()
)
dIpsgIfSrcGuardVlansFirst2K.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dIpsgIfSrcGuardVlansFirst2K.setStatus("current")
_DIpsgIfSrcGuardVlansSecond2K_Type = Dlink2kVlanList
_DIpsgIfSrcGuardVlansSecond2K_Object = MibTableColumn
dIpsgIfSrcGuardVlansSecond2K = _DIpsgIfSrcGuardVlansSecond2K_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 132, 1, 2, 2, 1, 8),
    _DIpsgIfSrcGuardVlansSecond2K_Type()
)
dIpsgIfSrcGuardVlansSecond2K.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dIpsgIfSrcGuardVlansSecond2K.setStatus("current")
_DIpSourceGuardMIBConformance_ObjectIdentity = ObjectIdentity
dIpSourceGuardMIBConformance = _DIpSourceGuardMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 132, 2)
)
_DIpsgMIBCompliances_ObjectIdentity = ObjectIdentity
dIpsgMIBCompliances = _DIpsgMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 132, 2, 1)
)
_DIpsgMIBGroups_ObjectIdentity = ObjectIdentity
dIpsgMIBGroups = _DIpsgMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 132, 2, 2)
)

# Managed Objects groups

dIpsgStaticBindingsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 171, 14, 132, 2, 2, 1)
)
dIpsgStaticBindingsGroup.setObjects(
    ("DLINKSW-IP-SOURCE-GUARD-MIB", "dIpsgStaticBindingsRowStatus")
)
if mibBuilder.loadTexts:
    dIpsgStaticBindingsGroup.setStatus("current")

dIpsgVerifySrcInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 171, 14, 132, 2, 2, 2)
)
dIpsgVerifySrcInfoGroup.setObjects(
      *(("DLINKSW-IP-SOURCE-GUARD-MIB", "dIpsgIfSrcGuardIpAddress"),
        ("DLINKSW-IP-SOURCE-GUARD-MIB", "dIpsgIfSrcGuardIpFilterAction"),
        ("DLINKSW-IP-SOURCE-GUARD-MIB", "dIpsgIfSrcGuardFilterMode"))
)
if mibBuilder.loadTexts:
    dIpsgVerifySrcInfoGroup.setStatus("current")

dIpsgVerifySrcInfoExtGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 171, 14, 132, 2, 2, 3)
)
dIpsgVerifySrcInfoExtGroup.setObjects(
      *(("DLINKSW-IP-SOURCE-GUARD-MIB", "dIpsgIfSrcGuardMacAddress"),
        ("DLINKSW-IP-SOURCE-GUARD-MIB", "dIpsgIfSrcGuardMacFilterAction"),
        ("DLINKSW-IP-SOURCE-GUARD-MIB", "dIpsgIfSrcGuardVlansFirst2K"),
        ("DLINKSW-IP-SOURCE-GUARD-MIB", "dIpsgIfSrcGuardVlansSecond2K"))
)
if mibBuilder.loadTexts:
    dIpsgVerifySrcInfoExtGroup.setStatus("current")

dIpsgIfSrcGuardTrafficFilterGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 171, 14, 132, 2, 2, 4)
)
dIpsgIfSrcGuardTrafficFilterGroup.setObjects(
    ("DLINKSW-IP-SOURCE-GUARD-MIB", "dIpsgIfSrcGuardFilterType")
)
if mibBuilder.loadTexts:
    dIpsgIfSrcGuardTrafficFilterGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

dIpsgMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 171, 14, 132, 2, 1, 1)
)
dIpsgMIBCompliance.setObjects(
      *(("DLINKSW-IP-SOURCE-GUARD-MIB", "dIpsgIfSrcGuardTrafficFilterGroup"),
        ("DLINKSW-IP-SOURCE-GUARD-MIB", "dIpsgVerifySrcInfoGroup"),
        ("DLINKSW-IP-SOURCE-GUARD-MIB", "dIpsgStaticBindingsGroup"),
        ("DLINKSW-IP-SOURCE-GUARD-MIB", "dIpsgVerifySrcInfoExtGroup"))
)
if mibBuilder.loadTexts:
    dIpsgMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "DLINKSW-IP-SOURCE-GUARD-MIB",
    **{"dlinkSwIpSourceGuardMIB": dlinkSwIpSourceGuardMIB,
       "dIpSourceGuardMIBNotifs": dIpSourceGuardMIBNotifs,
       "dIpSourceGuardMIBObjects": dIpSourceGuardMIBObjects,
       "dIpsgBindings": dIpsgBindings,
       "dIpsgStaticBindingsTable": dIpsgStaticBindingsTable,
       "dIpsgStaticBindingsEntry": dIpsgStaticBindingsEntry,
       "dIpsgStaticBindingsVlan": dIpsgStaticBindingsVlan,
       "dIpsgStaticBindingsMacAddress": dIpsgStaticBindingsMacAddress,
       "dIpsgStaticBindingsIpAddress": dIpsgStaticBindingsIpAddress,
       "dIpsgStaticBindingsInterface": dIpsgStaticBindingsInterface,
       "dIpsgStaticBindingsRowStatus": dIpsgStaticBindingsRowStatus,
       "dIpsgSrcGuard": dIpsgSrcGuard,
       "dIpsgIfSrcGuardConfigTable": dIpsgIfSrcGuardConfigTable,
       "dIpsgIfSrcGuardConfigEntry": dIpsgIfSrcGuardConfigEntry,
       "dIpsgIfSrcGuardFilterType": dIpsgIfSrcGuardFilterType,
       "dIpsgIfSrcGuardAddrTable": dIpsgIfSrcGuardAddrTable,
       "dIpsgIfSrcGuardAddrEntry": dIpsgIfSrcGuardAddrEntry,
       "dIpsgIfSrcGuardIndex": dIpsgIfSrcGuardIndex,
       "dIpsgIfSrcGuardFilterMode": dIpsgIfSrcGuardFilterMode,
       "dIpsgIfSrcGuardIpAddress": dIpsgIfSrcGuardIpAddress,
       "dIpsgIfSrcGuardIpFilterAction": dIpsgIfSrcGuardIpFilterAction,
       "dIpsgIfSrcGuardMacAddress": dIpsgIfSrcGuardMacAddress,
       "dIpsgIfSrcGuardMacFilterAction": dIpsgIfSrcGuardMacFilterAction,
       "dIpsgIfSrcGuardVlansFirst2K": dIpsgIfSrcGuardVlansFirst2K,
       "dIpsgIfSrcGuardVlansSecond2K": dIpsgIfSrcGuardVlansSecond2K,
       "dIpSourceGuardMIBConformance": dIpSourceGuardMIBConformance,
       "dIpsgMIBCompliances": dIpsgMIBCompliances,
       "dIpsgMIBCompliance": dIpsgMIBCompliance,
       "dIpsgMIBGroups": dIpsgMIBGroups,
       "dIpsgStaticBindingsGroup": dIpsgStaticBindingsGroup,
       "dIpsgVerifySrcInfoGroup": dIpsgVerifySrcInfoGroup,
       "dIpsgVerifySrcInfoExtGroup": dIpsgVerifySrcInfoExtGroup,
       "dIpsgIfSrcGuardTrafficFilterGroup": dIpsgIfSrcGuardTrafficFilterGroup}
)
