# SNMP MIB module (Juniper-DISMAN-EVENT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\junose\Juniper-DISMAN-EVENT-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 12:06:10 2025
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

(mteTriggerEntry,) = mibBuilder.importSymbols(
    "DISMAN-EVENT-MIB",
    "mteTriggerEntry")

(juniMibs,) = mibBuilder.importSymbols(
    "Juniper-MIBs",
    "juniMibs")

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

juniDismanEventMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 66)
)
if mibBuilder.loadTexts:
    juniDismanEventMIB.setRevisions(
        ("2003-10-30 15:35",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_JuniDismanEventMIBObjects_ObjectIdentity = ObjectIdentity
juniDismanEventMIBObjects = _JuniDismanEventMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 66, 1)
)
_JuniMteTrigger_ObjectIdentity = ObjectIdentity
juniMteTrigger = _JuniMteTrigger_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 66, 1, 1)
)
_JuniMteTriggerTable_Object = MibTable
juniMteTriggerTable = _JuniMteTriggerTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 66, 1, 1, 1)
)
if mibBuilder.loadTexts:
    juniMteTriggerTable.setStatus("current")
_JuniMteTriggerEntry_Object = MibTableRow
juniMteTriggerEntry = _JuniMteTriggerEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 66, 1, 1, 1, 1)
)
if mibBuilder.loadTexts:
    juniMteTriggerEntry.setStatus("current")


class _JuniMteTriggerContextNameLimit_Type(Unsigned32):
    """Custom type juniMteTriggerContextNameLimit based on Unsigned32"""
    defaultValue = 0


_JuniMteTriggerContextNameLimit_Type.__name__ = "Unsigned32"
_JuniMteTriggerContextNameLimit_Object = MibTableColumn
juniMteTriggerContextNameLimit = _JuniMteTriggerContextNameLimit_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 66, 1, 1, 1, 1, 2),
    _JuniMteTriggerContextNameLimit_Type()
)
juniMteTriggerContextNameLimit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniMteTriggerContextNameLimit.setStatus("current")
_JuniDismanEventMIBNotificationPrefix_ObjectIdentity = ObjectIdentity
juniDismanEventMIBNotificationPrefix = _JuniDismanEventMIBNotificationPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 66, 2)
)
_JuniDismanEventMIBNotificationObjects_ObjectIdentity = ObjectIdentity
juniDismanEventMIBNotificationObjects = _JuniDismanEventMIBNotificationObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 66, 2, 1)
)


class _JuniMteExistenceTestResult_Type(Integer32):
    """Custom type juniMteExistenceTestResult based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("present", 0),
          ("absent", 1),
          ("changed", 2))
    )


_JuniMteExistenceTestResult_Type.__name__ = "Integer32"
_JuniMteExistenceTestResult_Object = MibScalar
juniMteExistenceTestResult = _JuniMteExistenceTestResult_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 66, 2, 1, 1),
    _JuniMteExistenceTestResult_Type()
)
juniMteExistenceTestResult.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    juniMteExistenceTestResult.setStatus("current")
_JuniDismanEventConformance_ObjectIdentity = ObjectIdentity
juniDismanEventConformance = _JuniDismanEventConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 66, 3)
)
_JuniDismanEventCompliances_ObjectIdentity = ObjectIdentity
juniDismanEventCompliances = _JuniDismanEventCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 66, 3, 1)
)
_JuniDismanEventGroups_ObjectIdentity = ObjectIdentity
juniDismanEventGroups = _JuniDismanEventGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 66, 3, 2)
)
mteTriggerEntry.registerAugmentions(
    ("Juniper-DISMAN-EVENT-MIB",
     "juniMteTriggerEntry")
)
juniMteTriggerEntry.setIndexNames(*mteTriggerEntry.getIndexNames())

# Managed Objects groups

juniMteTriggerTableGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 66, 3, 2, 1)
)
juniMteTriggerTableGroup.setObjects(
      *(("Juniper-DISMAN-EVENT-MIB", "juniMteTriggerContextNameLimit"),
        ("Juniper-DISMAN-EVENT-MIB", "juniMteExistenceTestResult"))
)
if mibBuilder.loadTexts:
    juniMteTriggerTableGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

juniDismanEventCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 66, 3, 1, 1)
)
juniDismanEventCompliance.setObjects(
    ("Juniper-DISMAN-EVENT-MIB", "juniMteTriggerTableGroup")
)
if mibBuilder.loadTexts:
    juniDismanEventCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Juniper-DISMAN-EVENT-MIB",
    **{"juniDismanEventMIB": juniDismanEventMIB,
       "juniDismanEventMIBObjects": juniDismanEventMIBObjects,
       "juniMteTrigger": juniMteTrigger,
       "juniMteTriggerTable": juniMteTriggerTable,
       "juniMteTriggerEntry": juniMteTriggerEntry,
       "juniMteTriggerContextNameLimit": juniMteTriggerContextNameLimit,
       "juniDismanEventMIBNotificationPrefix": juniDismanEventMIBNotificationPrefix,
       "juniDismanEventMIBNotificationObjects": juniDismanEventMIBNotificationObjects,
       "juniMteExistenceTestResult": juniMteExistenceTestResult,
       "juniDismanEventConformance": juniDismanEventConformance,
       "juniDismanEventCompliances": juniDismanEventCompliances,
       "juniDismanEventCompliance": juniDismanEventCompliance,
       "juniDismanEventGroups": juniDismanEventGroups,
       "juniMteTriggerTableGroup": juniMteTriggerTableGroup}
)
