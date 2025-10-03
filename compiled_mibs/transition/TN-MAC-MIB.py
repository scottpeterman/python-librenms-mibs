# SNMP MIB module (TN-MAC-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\transition\TN-MAC-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 12:31:52 2025
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

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

(PortList,
 VlanId) = mibBuilder.importSymbols(
    "Q-BRIDGE-MIB",
    "PortList",
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

(tnProducts,) = mibBuilder.importSymbols(
    "TRANSITION-SMI",
    "tnProducts")


# MODULE-IDENTITY

tnMacMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 142)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_TnMacMibNotifications_ObjectIdentity = ObjectIdentity
tnMacMibNotifications = _TnMacMibNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 142, 0)
)
_TnMacMibObjects_ObjectIdentity = ObjectIdentity
tnMacMibObjects = _TnMacMibObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 142, 1)
)
_TnMacAgeAutomaticConfig_ObjectIdentity = ObjectIdentity
tnMacAgeAutomaticConfig = _TnMacAgeAutomaticConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 142, 1, 1)
)
_TnMacAgeAutomaticAgingDisable_Type = TruthValue
_TnMacAgeAutomaticAgingDisable_Object = MibScalar
tnMacAgeAutomaticAgingDisable = _TnMacAgeAutomaticAgingDisable_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 142, 1, 1, 1),
    _TnMacAgeAutomaticAgingDisable_Type()
)
tnMacAgeAutomaticAgingDisable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnMacAgeAutomaticAgingDisable.setStatus("current")


class _TnMacAgeAutomaticAgingTime_Type(Integer32):
    """Custom type tnMacAgeAutomaticAgingTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 1000000),
    )


_TnMacAgeAutomaticAgingTime_Type.__name__ = "Integer32"
_TnMacAgeAutomaticAgingTime_Object = MibScalar
tnMacAgeAutomaticAgingTime = _TnMacAgeAutomaticAgingTime_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 142, 1, 1, 2),
    _TnMacAgeAutomaticAgingTime_Type()
)
tnMacAgeAutomaticAgingTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnMacAgeAutomaticAgingTime.setStatus("current")
_TnMacLearningTable_Object = MibTable
tnMacLearningTable = _TnMacLearningTable_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 142, 1, 2)
)
if mibBuilder.loadTexts:
    tnMacLearningTable.setStatus("current")
_TnMacLearningEntry_Object = MibTableRow
tnMacLearningEntry = _TnMacLearningEntry_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 142, 1, 2, 1)
)
tnMacLearningEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    tnMacLearningEntry.setStatus("current")


class _TnMacTablePortLearning_Type(Integer32):
    """Custom type tnMacTablePortLearning based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("auto", 1),
          ("disable", 2),
          ("secure", 3))
    )


_TnMacTablePortLearning_Type.__name__ = "Integer32"
_TnMacTablePortLearning_Object = MibTableColumn
tnMacTablePortLearning = _TnMacTablePortLearning_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 142, 1, 2, 1, 1),
    _TnMacTablePortLearning_Type()
)
tnMacTablePortLearning.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnMacTablePortLearning.setStatus("current")
_TnMacStaticConfigTable_Object = MibTable
tnMacStaticConfigTable = _TnMacStaticConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 142, 1, 3)
)
if mibBuilder.loadTexts:
    tnMacStaticConfigTable.setStatus("current")
_TnMacStaticConfigEntry_Object = MibTableRow
tnMacStaticConfigEntry = _TnMacStaticConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 142, 1, 3, 1)
)
tnMacStaticConfigEntry.setIndexNames(
    (0, "TN-MAC-MIB", "tnStaticMacVlanId"),
    (0, "TN-MAC-MIB", "tnStaticMacAddress"),
)
if mibBuilder.loadTexts:
    tnMacStaticConfigEntry.setStatus("current")
_TnStaticMacVlanId_Type = VlanId
_TnStaticMacVlanId_Object = MibTableColumn
tnStaticMacVlanId = _TnStaticMacVlanId_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 142, 1, 3, 1, 1),
    _TnStaticMacVlanId_Type()
)
tnStaticMacVlanId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnStaticMacVlanId.setStatus("current")
_TnStaticMacAddress_Type = MacAddress
_TnStaticMacAddress_Object = MibTableColumn
tnStaticMacAddress = _TnStaticMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 142, 1, 3, 1, 2),
    _TnStaticMacAddress_Type()
)
tnStaticMacAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnStaticMacAddress.setStatus("current")
_TnStaticMacPortMembers_Type = PortList
_TnStaticMacPortMembers_Object = MibTableColumn
tnStaticMacPortMembers = _TnStaticMacPortMembers_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 142, 1, 3, 1, 3),
    _TnStaticMacPortMembers_Type()
)
tnStaticMacPortMembers.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnStaticMacPortMembers.setStatus("current")
_TnStaticMacStatus_Type = RowStatus
_TnStaticMacStatus_Object = MibTableColumn
tnStaticMacStatus = _TnStaticMacStatus_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 142, 1, 3, 1, 4),
    _TnStaticMacStatus_Type()
)
tnStaticMacStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnStaticMacStatus.setStatus("current")
_TnMacAddressTable_Object = MibTable
tnMacAddressTable = _TnMacAddressTable_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 142, 1, 4)
)
if mibBuilder.loadTexts:
    tnMacAddressTable.setStatus("current")
_TnMacAddressEntry_Object = MibTableRow
tnMacAddressEntry = _TnMacAddressEntry_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 142, 1, 4, 1)
)
tnMacAddressEntry.setIndexNames(
    (0, "TN-MAC-MIB", "tnMacType"),
    (0, "TN-MAC-MIB", "tnMacVlan"),
    (0, "TN-MAC-MIB", "tnMacAddress"),
)
if mibBuilder.loadTexts:
    tnMacAddressEntry.setStatus("current")


class _TnMacType_Type(Integer32):
    """Custom type tnMacType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("static", 1),
          ("dynamic", 2))
    )


_TnMacType_Type.__name__ = "Integer32"
_TnMacType_Object = MibTableColumn
tnMacType = _TnMacType_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 142, 1, 4, 1, 1),
    _TnMacType_Type()
)
tnMacType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnMacType.setStatus("current")
_TnMacVlan_Type = VlanId
_TnMacVlan_Object = MibTableColumn
tnMacVlan = _TnMacVlan_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 142, 1, 4, 1, 2),
    _TnMacVlan_Type()
)
tnMacVlan.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnMacVlan.setStatus("current")
_TnMacAddress_Type = MacAddress
_TnMacAddress_Object = MibTableColumn
tnMacAddress = _TnMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 142, 1, 4, 1, 3),
    _TnMacAddress_Type()
)
tnMacAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnMacAddress.setStatus("current")
_TnMacPortMembers_Type = PortList
_TnMacPortMembers_Object = MibTableColumn
tnMacPortMembers = _TnMacPortMembers_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 142, 1, 4, 1, 4),
    _TnMacPortMembers_Type()
)
tnMacPortMembers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnMacPortMembers.setStatus("current")
_TnMacDynamicClear_Type = TruthValue
_TnMacDynamicClear_Object = MibScalar
tnMacDynamicClear = _TnMacDynamicClear_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 142, 1, 5),
    _TnMacDynamicClear_Type()
)
tnMacDynamicClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnMacDynamicClear.setStatus("current")
_TnMacMibConformance_ObjectIdentity = ObjectIdentity
tnMacMibConformance = _TnMacMibConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 142, 2)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TN-MAC-MIB",
    **{"tnMacMib": tnMacMib,
       "tnMacMibNotifications": tnMacMibNotifications,
       "tnMacMibObjects": tnMacMibObjects,
       "tnMacAgeAutomaticConfig": tnMacAgeAutomaticConfig,
       "tnMacAgeAutomaticAgingDisable": tnMacAgeAutomaticAgingDisable,
       "tnMacAgeAutomaticAgingTime": tnMacAgeAutomaticAgingTime,
       "tnMacLearningTable": tnMacLearningTable,
       "tnMacLearningEntry": tnMacLearningEntry,
       "tnMacTablePortLearning": tnMacTablePortLearning,
       "tnMacStaticConfigTable": tnMacStaticConfigTable,
       "tnMacStaticConfigEntry": tnMacStaticConfigEntry,
       "tnStaticMacVlanId": tnStaticMacVlanId,
       "tnStaticMacAddress": tnStaticMacAddress,
       "tnStaticMacPortMembers": tnStaticMacPortMembers,
       "tnStaticMacStatus": tnStaticMacStatus,
       "tnMacAddressTable": tnMacAddressTable,
       "tnMacAddressEntry": tnMacAddressEntry,
       "tnMacType": tnMacType,
       "tnMacVlan": tnMacVlan,
       "tnMacAddress": tnMacAddress,
       "tnMacPortMembers": tnMacPortMembers,
       "tnMacDynamicClear": tnMacDynamicClear,
       "tnMacMibConformance": tnMacMibConformance}
)
