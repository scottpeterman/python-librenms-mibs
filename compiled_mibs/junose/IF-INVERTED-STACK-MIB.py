# SNMP MIB module (IF-INVERTED-STACK-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\junose\IF-INVERTED-STACK-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 12:05:43 2025
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

(ifStackGroup2,
 ifStackHigherLayer,
 ifStackLowerLayer) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifStackGroup2",
    "ifStackHigherLayer",
    "ifStackLowerLayer")

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
 iso,
 mib_2) = mibBuilder.importSymbols(
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
    "iso",
    "mib-2")

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

ifInvertedStackMIB = ModuleIdentity(
    (1, 3, 6, 1, 2, 1, 77)
)
if mibBuilder.loadTexts:
    ifInvertedStackMIB.setRevisions(
        ("2000-06-14 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_IfInvMIBObjects_ObjectIdentity = ObjectIdentity
ifInvMIBObjects = _IfInvMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 77, 1)
)
_IfInvStackTable_Object = MibTable
ifInvStackTable = _IfInvStackTable_Object(
    (1, 3, 6, 1, 2, 1, 77, 1, 1)
)
if mibBuilder.loadTexts:
    ifInvStackTable.setStatus("current")
_IfInvStackEntry_Object = MibTableRow
ifInvStackEntry = _IfInvStackEntry_Object(
    (1, 3, 6, 1, 2, 1, 77, 1, 1, 1)
)
ifInvStackEntry.setIndexNames(
    (0, "IF-MIB", "ifStackLowerLayer"),
    (0, "IF-MIB", "ifStackHigherLayer"),
)
if mibBuilder.loadTexts:
    ifInvStackEntry.setStatus("current")
_IfInvStackStatus_Type = RowStatus
_IfInvStackStatus_Object = MibTableColumn
ifInvStackStatus = _IfInvStackStatus_Object(
    (1, 3, 6, 1, 2, 1, 77, 1, 1, 1, 1),
    _IfInvStackStatus_Type()
)
ifInvStackStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifInvStackStatus.setStatus("current")
_IfInvConformance_ObjectIdentity = ObjectIdentity
ifInvConformance = _IfInvConformance_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 77, 1, 2)
)
_IfInvGroups_ObjectIdentity = ObjectIdentity
ifInvGroups = _IfInvGroups_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 77, 1, 2, 1)
)
_IfInvCompliances_ObjectIdentity = ObjectIdentity
ifInvCompliances = _IfInvCompliances_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 77, 1, 2, 2)
)

# Managed Objects groups

ifInvStackGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 77, 1, 2, 1, 1)
)
ifInvStackGroup.setObjects(
    ("IF-INVERTED-STACK-MIB", "ifInvStackStatus")
)
if mibBuilder.loadTexts:
    ifInvStackGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

ifInvCompliance = ModuleCompliance(
    (1, 3, 6, 1, 2, 1, 77, 1, 2, 2, 1)
)
ifInvCompliance.setObjects(
      *(("IF-INVERTED-STACK-MIB", "ifInvStackGroup"),
        ("IF-MIB", "ifStackGroup2"))
)
if mibBuilder.loadTexts:
    ifInvCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "IF-INVERTED-STACK-MIB",
    **{"ifInvertedStackMIB": ifInvertedStackMIB,
       "ifInvMIBObjects": ifInvMIBObjects,
       "ifInvStackTable": ifInvStackTable,
       "ifInvStackEntry": ifInvStackEntry,
       "ifInvStackStatus": ifInvStackStatus,
       "ifInvConformance": ifInvConformance,
       "ifInvGroups": ifInvGroups,
       "ifInvStackGroup": ifInvStackGroup,
       "ifInvCompliances": ifInvCompliances,
       "ifInvCompliance": ifInvCompliance}
)
