# SNMP MIB module (CERENT-IF-EXT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\cisco\CERENT-IF-EXT-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:25:36 2025
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

(cerentGeneric,
 cerentModules,
 cerentRequirements) = mibBuilder.importSymbols(
    "CERENT-GLOBAL-REGISTRY",
    "cerentGeneric",
    "cerentModules",
    "cerentRequirements")

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

cerentIfExtMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 3607, 1, 10, 140)
)
if mibBuilder.loadTexts:
    cerentIfExtMIB.setRevisions(
        ("2005-11-14 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CerentIfExtMIBObjects_ObjectIdentity = ObjectIdentity
cerentIfExtMIBObjects = _CerentIfExtMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3607, 2, 100)
)
_CerentIfExtTable_Object = MibTable
cerentIfExtTable = _CerentIfExtTable_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 100, 10)
)
if mibBuilder.loadTexts:
    cerentIfExtTable.setStatus("current")
_CerentIfExtEntry_Object = MibTableRow
cerentIfExtEntry = _CerentIfExtEntry_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 100, 10, 1)
)
cerentIfExtEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    cerentIfExtEntry.setStatus("current")


class _CerentIfExtPreServiceAlarmSuppression_Type(TruthValue):
    """Custom type cerentIfExtPreServiceAlarmSuppression based on TruthValue"""
    defaultValue = 2


_CerentIfExtPreServiceAlarmSuppression_Type.__name__ = "TruthValue"
_CerentIfExtPreServiceAlarmSuppression_Object = MibTableColumn
cerentIfExtPreServiceAlarmSuppression = _CerentIfExtPreServiceAlarmSuppression_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 100, 10, 1, 10),
    _CerentIfExtPreServiceAlarmSuppression_Type()
)
cerentIfExtPreServiceAlarmSuppression.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cerentIfExtPreServiceAlarmSuppression.setStatus("current")


class _CerentIfExtConfiguredSoakTime_Type(Integer32):
    """Custom type cerentIfExtConfiguredSoakTime based on Integer32"""
    defaultValue = 480


_CerentIfExtConfiguredSoakTime_Type.__name__ = "Integer32"
_CerentIfExtConfiguredSoakTime_Object = MibTableColumn
cerentIfExtConfiguredSoakTime = _CerentIfExtConfiguredSoakTime_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 100, 10, 1, 20),
    _CerentIfExtConfiguredSoakTime_Type()
)
cerentIfExtConfiguredSoakTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cerentIfExtConfiguredSoakTime.setStatus("current")
if mibBuilder.loadTexts:
    cerentIfExtConfiguredSoakTime.setUnits("minutes")
_CerentIfExtCurrentSoakTime_Type = Integer32
_CerentIfExtCurrentSoakTime_Object = MibTableColumn
cerentIfExtCurrentSoakTime = _CerentIfExtCurrentSoakTime_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 100, 10, 1, 30),
    _CerentIfExtCurrentSoakTime_Type()
)
cerentIfExtCurrentSoakTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cerentIfExtCurrentSoakTime.setStatus("current")
if mibBuilder.loadTexts:
    cerentIfExtCurrentSoakTime.setUnits("minutes")
_CerentIfExtMIBConformance_ObjectIdentity = ObjectIdentity
cerentIfExtMIBConformance = _CerentIfExtMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3607, 5, 90)
)
_CerentIfExtMIBCompliances_ObjectIdentity = ObjectIdentity
cerentIfExtMIBCompliances = _CerentIfExtMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3607, 5, 90, 1)
)
_CerentIfExtMIBGroups_ObjectIdentity = ObjectIdentity
cerentIfExtMIBGroups = _CerentIfExtMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3607, 5, 90, 2)
)

# Managed Objects groups

cerentIfExtGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 3607, 5, 90, 2, 10)
)
cerentIfExtGroup.setObjects(
      *(("CERENT-IF-EXT-MIB", "cerentIfExtPreServiceAlarmSuppression"),
        ("CERENT-IF-EXT-MIB", "cerentIfExtConfiguredSoakTime"),
        ("CERENT-IF-EXT-MIB", "cerentIfExtCurrentSoakTime"))
)
if mibBuilder.loadTexts:
    cerentIfExtGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

cerentIfExtMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 3607, 5, 90, 1, 1)
)
cerentIfExtMIBCompliance.setObjects(
    ("CERENT-IF-EXT-MIB", "cerentIfExtGroup")
)
if mibBuilder.loadTexts:
    cerentIfExtMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CERENT-IF-EXT-MIB",
    **{"cerentIfExtMIB": cerentIfExtMIB,
       "cerentIfExtMIBObjects": cerentIfExtMIBObjects,
       "cerentIfExtTable": cerentIfExtTable,
       "cerentIfExtEntry": cerentIfExtEntry,
       "cerentIfExtPreServiceAlarmSuppression": cerentIfExtPreServiceAlarmSuppression,
       "cerentIfExtConfiguredSoakTime": cerentIfExtConfiguredSoakTime,
       "cerentIfExtCurrentSoakTime": cerentIfExtCurrentSoakTime,
       "cerentIfExtMIBConformance": cerentIfExtMIBConformance,
       "cerentIfExtMIBCompliances": cerentIfExtMIBCompliances,
       "cerentIfExtMIBCompliance": cerentIfExtMIBCompliance,
       "cerentIfExtMIBGroups": cerentIfExtMIBGroups,
       "cerentIfExtGroup": cerentIfExtGroup}
)
