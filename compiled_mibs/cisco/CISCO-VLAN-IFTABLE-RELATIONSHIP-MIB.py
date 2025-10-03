# SNMP MIB module (CISCO-VLAN-IFTABLE-RELATIONSHIP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\cisco\CISCO-VLAN-IFTABLE-RELATIONSHIP-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:27:56 2025
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

(ciscoMgmt,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoMgmt")

(InterfaceIndexOrZero,) = mibBuilder.importSymbols(
    "CISCO-TC",
    "InterfaceIndexOrZero")

(VlanIndex,) = mibBuilder.importSymbols(
    "CISCO-VTP-MIB",
    "VlanIndex")

(InterfaceIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

ciscoVlanIfTableRelationshipMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 128)
)
if mibBuilder.loadTexts:
    ciscoVlanIfTableRelationshipMIB.setRevisions(
        ("2013-07-15 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CviMIBObjects_ObjectIdentity = ObjectIdentity
cviMIBObjects = _CviMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 128, 1)
)
_CviGlobals_ObjectIdentity = ObjectIdentity
cviGlobals = _CviGlobals_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 128, 1, 1)
)
_CviVlanInterfaceIndexTable_Object = MibTable
cviVlanInterfaceIndexTable = _CviVlanInterfaceIndexTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 128, 1, 1, 1)
)
if mibBuilder.loadTexts:
    cviVlanInterfaceIndexTable.setStatus("current")
_CviVlanInterfaceIndexEntry_Object = MibTableRow
cviVlanInterfaceIndexEntry = _CviVlanInterfaceIndexEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 128, 1, 1, 1, 1)
)
cviVlanInterfaceIndexEntry.setIndexNames(
    (0, "CISCO-VLAN-IFTABLE-RELATIONSHIP-MIB", "cviVlanId"),
    (0, "CISCO-VLAN-IFTABLE-RELATIONSHIP-MIB", "cviPhysicalIfIndex"),
)
if mibBuilder.loadTexts:
    cviVlanInterfaceIndexEntry.setStatus("current")
_CviVlanId_Type = VlanIndex
_CviVlanId_Object = MibTableColumn
cviVlanId = _CviVlanId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 128, 1, 1, 1, 1, 1),
    _CviVlanId_Type()
)
cviVlanId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cviVlanId.setStatus("current")
_CviPhysicalIfIndex_Type = InterfaceIndexOrZero
_CviPhysicalIfIndex_Object = MibTableColumn
cviPhysicalIfIndex = _CviPhysicalIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 128, 1, 1, 1, 1, 2),
    _CviPhysicalIfIndex_Type()
)
cviPhysicalIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cviPhysicalIfIndex.setStatus("current")
_CviRoutedVlanIfIndex_Type = InterfaceIndex
_CviRoutedVlanIfIndex_Object = MibTableColumn
cviRoutedVlanIfIndex = _CviRoutedVlanIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 128, 1, 1, 1, 1, 3),
    _CviRoutedVlanIfIndex_Type()
)
cviRoutedVlanIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cviRoutedVlanIfIndex.setStatus("current")
_CviMIBConformance_ObjectIdentity = ObjectIdentity
cviMIBConformance = _CviMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 128, 1, 3)
)
_CviMIBCompliances_ObjectIdentity = ObjectIdentity
cviMIBCompliances = _CviMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 128, 1, 3, 1)
)
_CviMIBGroups_ObjectIdentity = ObjectIdentity
cviMIBGroups = _CviMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 128, 1, 3, 2)
)

# Managed Objects groups

cviMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 128, 1, 3, 2, 1)
)
cviMIBGroup.setObjects(
    ("CISCO-VLAN-IFTABLE-RELATIONSHIP-MIB", "cviRoutedVlanIfIndex")
)
if mibBuilder.loadTexts:
    cviMIBGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

cviMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 128, 1, 3, 1, 1)
)
cviMIBCompliance.setObjects(
    ("CISCO-VLAN-IFTABLE-RELATIONSHIP-MIB", "cviMIBGroup")
)
if mibBuilder.loadTexts:
    cviMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-VLAN-IFTABLE-RELATIONSHIP-MIB",
    **{"ciscoVlanIfTableRelationshipMIB": ciscoVlanIfTableRelationshipMIB,
       "cviMIBObjects": cviMIBObjects,
       "cviGlobals": cviGlobals,
       "cviVlanInterfaceIndexTable": cviVlanInterfaceIndexTable,
       "cviVlanInterfaceIndexEntry": cviVlanInterfaceIndexEntry,
       "cviVlanId": cviVlanId,
       "cviPhysicalIfIndex": cviPhysicalIfIndex,
       "cviRoutedVlanIfIndex": cviRoutedVlanIfIndex,
       "cviMIBConformance": cviMIBConformance,
       "cviMIBCompliances": cviMIBCompliances,
       "cviMIBCompliance": cviMIBCompliance,
       "cviMIBGroups": cviMIBGroups,
       "cviMIBGroup": cviMIBGroup}
)
