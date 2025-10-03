# SNMP MIB module (Juniper-BRIDGE-ETHERNET-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\junose\Juniper-BRIDGE-ETHERNET-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 12:05:58 2025
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

(InterfaceIndex,
 InterfaceIndexOrZero) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
    "InterfaceIndexOrZero")

(juniMibs,) = mibBuilder.importSymbols(
    "Juniper-MIBs",
    "juniMibs")

(JuniNextIfIndex,) = mibBuilder.importSymbols(
    "Juniper-TC",
    "JuniNextIfIndex")

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

juniBridgeEthernetMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 31)
)
if mibBuilder.loadTexts:
    juniBridgeEthernetMIB.setRevisions(
        ("2005-12-14 17:10",
         "2002-09-16 21:44",
         "2000-09-26 14:43",
         "2000-03-27 23:45",
         "1999-12-10 18:30")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_JuniBridgedEthernetObjects_ObjectIdentity = ObjectIdentity
juniBridgedEthernetObjects = _JuniBridgedEthernetObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 31, 1)
)
_JuniBridgedEthernetIfLayer_ObjectIdentity = ObjectIdentity
juniBridgedEthernetIfLayer = _JuniBridgedEthernetIfLayer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 31, 1, 1)
)
_JuniBridgedEthernetNextIfIndex_Type = JuniNextIfIndex
_JuniBridgedEthernetNextIfIndex_Object = MibScalar
juniBridgedEthernetNextIfIndex = _JuniBridgedEthernetNextIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 31, 1, 1, 1),
    _JuniBridgedEthernetNextIfIndex_Type()
)
juniBridgedEthernetNextIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniBridgedEthernetNextIfIndex.setStatus("current")
_JuniBridgedEthernetIfTable_Object = MibTable
juniBridgedEthernetIfTable = _JuniBridgedEthernetIfTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 31, 1, 1, 2)
)
if mibBuilder.loadTexts:
    juniBridgedEthernetIfTable.setStatus("current")
_JuniBridgedEthernetIfEntry_Object = MibTableRow
juniBridgedEthernetIfEntry = _JuniBridgedEthernetIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 31, 1, 1, 2, 1)
)
juniBridgedEthernetIfEntry.setIndexNames(
    (0, "Juniper-BRIDGE-ETHERNET-MIB", "juniBridgedEthernetIfIfIndex"),
)
if mibBuilder.loadTexts:
    juniBridgedEthernetIfEntry.setStatus("current")
_JuniBridgedEthernetIfIfIndex_Type = InterfaceIndex
_JuniBridgedEthernetIfIfIndex_Object = MibTableColumn
juniBridgedEthernetIfIfIndex = _JuniBridgedEthernetIfIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 31, 1, 1, 2, 1, 1),
    _JuniBridgedEthernetIfIfIndex_Type()
)
juniBridgedEthernetIfIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniBridgedEthernetIfIfIndex.setStatus("current")


class _JuniBridgedEthernetProxyArp_Type(Integer32):
    """Custom type juniBridgedEthernetProxyArp based on Integer32"""
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
        *(("enableRestricted", 1),
          ("enableUnrestricted", 2),
          ("disable", 3))
    )


_JuniBridgedEthernetProxyArp_Type.__name__ = "Integer32"
_JuniBridgedEthernetProxyArp_Object = MibTableColumn
juniBridgedEthernetProxyArp = _JuniBridgedEthernetProxyArp_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 31, 1, 1, 2, 1, 2),
    _JuniBridgedEthernetProxyArp_Type()
)
juniBridgedEthernetProxyArp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniBridgedEthernetProxyArp.setStatus("obsolete")
_JuniBridgedEthernetIfLowerIfIndex_Type = InterfaceIndexOrZero
_JuniBridgedEthernetIfLowerIfIndex_Object = MibTableColumn
juniBridgedEthernetIfLowerIfIndex = _JuniBridgedEthernetIfLowerIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 31, 1, 1, 2, 1, 3),
    _JuniBridgedEthernetIfLowerIfIndex_Type()
)
juniBridgedEthernetIfLowerIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniBridgedEthernetIfLowerIfIndex.setStatus("current")
_JuniBridgedEthernetIfRowStatus_Type = RowStatus
_JuniBridgedEthernetIfRowStatus_Object = MibTableColumn
juniBridgedEthernetIfRowStatus = _JuniBridgedEthernetIfRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 31, 1, 1, 2, 1, 4),
    _JuniBridgedEthernetIfRowStatus_Type()
)
juniBridgedEthernetIfRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniBridgedEthernetIfRowStatus.setStatus("current")


class _JuniBridgedEthernetIfMtu_Type(Integer32):
    """Custom type juniBridgedEthernetIfMtu based on Integer32"""
    defaultValue = 1518

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(64, 9180),
    )


_JuniBridgedEthernetIfMtu_Type.__name__ = "Integer32"
_JuniBridgedEthernetIfMtu_Object = MibTableColumn
juniBridgedEthernetIfMtu = _JuniBridgedEthernetIfMtu_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 31, 1, 1, 2, 1, 5),
    _JuniBridgedEthernetIfMtu_Type()
)
juniBridgedEthernetIfMtu.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniBridgedEthernetIfMtu.setStatus("current")
_JuniBridgeEthernetConformance_ObjectIdentity = ObjectIdentity
juniBridgeEthernetConformance = _JuniBridgeEthernetConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 31, 4)
)
_JuniBridgeEthernetCompliances_ObjectIdentity = ObjectIdentity
juniBridgeEthernetCompliances = _JuniBridgeEthernetCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 31, 4, 1)
)
_JuniBridgeEthernetGroups_ObjectIdentity = ObjectIdentity
juniBridgeEthernetGroups = _JuniBridgeEthernetGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 31, 4, 2)
)

# Managed Objects groups

juniBridgedEthernetGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 31, 4, 2, 1)
)
juniBridgedEthernetGroup.setObjects(
      *(("Juniper-BRIDGE-ETHERNET-MIB", "juniBridgedEthernetNextIfIndex"),
        ("Juniper-BRIDGE-ETHERNET-MIB", "juniBridgedEthernetIfIfIndex"),
        ("Juniper-BRIDGE-ETHERNET-MIB", "juniBridgedEthernetProxyArp"),
        ("Juniper-BRIDGE-ETHERNET-MIB", "juniBridgedEthernetIfLowerIfIndex"),
        ("Juniper-BRIDGE-ETHERNET-MIB", "juniBridgedEthernetIfRowStatus"))
)
if mibBuilder.loadTexts:
    juniBridgedEthernetGroup.setStatus("obsolete")

juniBridgedEthernetGroup2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 31, 4, 2, 2)
)
juniBridgedEthernetGroup2.setObjects(
      *(("Juniper-BRIDGE-ETHERNET-MIB", "juniBridgedEthernetNextIfIndex"),
        ("Juniper-BRIDGE-ETHERNET-MIB", "juniBridgedEthernetIfIfIndex"),
        ("Juniper-BRIDGE-ETHERNET-MIB", "juniBridgedEthernetIfLowerIfIndex"),
        ("Juniper-BRIDGE-ETHERNET-MIB", "juniBridgedEthernetIfRowStatus"))
)
if mibBuilder.loadTexts:
    juniBridgedEthernetGroup2.setStatus("deprecated")

juniBridgedEthernetGroup3 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 31, 4, 2, 3)
)
juniBridgedEthernetGroup3.setObjects(
      *(("Juniper-BRIDGE-ETHERNET-MIB", "juniBridgedEthernetNextIfIndex"),
        ("Juniper-BRIDGE-ETHERNET-MIB", "juniBridgedEthernetIfIfIndex"),
        ("Juniper-BRIDGE-ETHERNET-MIB", "juniBridgedEthernetIfLowerIfIndex"),
        ("Juniper-BRIDGE-ETHERNET-MIB", "juniBridgedEthernetIfRowStatus"),
        ("Juniper-BRIDGE-ETHERNET-MIB", "juniBridgedEthernetIfMtu"))
)
if mibBuilder.loadTexts:
    juniBridgedEthernetGroup3.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

juniBridgedEthernetCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 31, 4, 1, 1)
)
juniBridgedEthernetCompliance.setObjects(
    ("Juniper-BRIDGE-ETHERNET-MIB", "juniBridgedEthernetGroup2")
)
if mibBuilder.loadTexts:
    juniBridgedEthernetCompliance.setStatus(
        "deprecated"
    )

juniBridgedEthernetCompliance2 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 31, 4, 1, 2)
)
juniBridgedEthernetCompliance2.setObjects(
    ("Juniper-BRIDGE-ETHERNET-MIB", "juniBridgedEthernetGroup3")
)
if mibBuilder.loadTexts:
    juniBridgedEthernetCompliance2.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Juniper-BRIDGE-ETHERNET-MIB",
    **{"juniBridgeEthernetMIB": juniBridgeEthernetMIB,
       "juniBridgedEthernetObjects": juniBridgedEthernetObjects,
       "juniBridgedEthernetIfLayer": juniBridgedEthernetIfLayer,
       "juniBridgedEthernetNextIfIndex": juniBridgedEthernetNextIfIndex,
       "juniBridgedEthernetIfTable": juniBridgedEthernetIfTable,
       "juniBridgedEthernetIfEntry": juniBridgedEthernetIfEntry,
       "juniBridgedEthernetIfIfIndex": juniBridgedEthernetIfIfIndex,
       "juniBridgedEthernetProxyArp": juniBridgedEthernetProxyArp,
       "juniBridgedEthernetIfLowerIfIndex": juniBridgedEthernetIfLowerIfIndex,
       "juniBridgedEthernetIfRowStatus": juniBridgedEthernetIfRowStatus,
       "juniBridgedEthernetIfMtu": juniBridgedEthernetIfMtu,
       "juniBridgeEthernetConformance": juniBridgeEthernetConformance,
       "juniBridgeEthernetCompliances": juniBridgeEthernetCompliances,
       "juniBridgedEthernetCompliance": juniBridgedEthernetCompliance,
       "juniBridgedEthernetCompliance2": juniBridgedEthernetCompliance2,
       "juniBridgeEthernetGroups": juniBridgeEthernetGroups,
       "juniBridgedEthernetGroup": juniBridgedEthernetGroup,
       "juniBridgedEthernetGroup2": juniBridgedEthernetGroup2,
       "juniBridgedEthernetGroup3": juniBridgedEthernetGroup3}
)
