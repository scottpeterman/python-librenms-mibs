# SNMP MIB module (ARUBAWIRED-LED-LOCATOR-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\arubaos-cx\ARUBAWIRED-LED-LOCATOR-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:19:09 2025
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

(arubaWiredChassisMIB,) = mibBuilder.importSymbols(
    "ARUBAWIRED-CHASSIS-MIB",
    "arubaWiredChassisMIB")

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

arubaWiredLedLocator = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 11, 7)
)
if mibBuilder.loadTexts:
    arubaWiredLedLocator.setRevisions(
        ("2023-06-06 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_ArubaWiredLedLocatorObjects_ObjectIdentity = ObjectIdentity
arubaWiredLedLocatorObjects = _ArubaWiredLedLocatorObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 11, 7, 1)
)
_ArubaWiredLedLocatorDetails_ObjectIdentity = ObjectIdentity
arubaWiredLedLocatorDetails = _ArubaWiredLedLocatorDetails_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 11, 7, 1, 1)
)
_ArubaWiredLedLocatorTable_Object = MibTable
arubaWiredLedLocatorTable = _ArubaWiredLedLocatorTable_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 11, 7, 1, 1, 1)
)
if mibBuilder.loadTexts:
    arubaWiredLedLocatorTable.setStatus("current")
_ArubaWiredLedLocatorEntry_Object = MibTableRow
arubaWiredLedLocatorEntry = _ArubaWiredLedLocatorEntry_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 11, 7, 1, 1, 1, 1)
)
arubaWiredLedLocatorEntry.setIndexNames(
    (0, "ARUBAWIRED-LED-LOCATOR-MIB", "arubaWiredLedLocatorGroupIndex"),
)
if mibBuilder.loadTexts:
    arubaWiredLedLocatorEntry.setStatus("current")


class _ArubaWiredLedLocatorGroupIndex_Type(Integer32):
    """Custom type arubaWiredLedLocatorGroupIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_ArubaWiredLedLocatorGroupIndex_Type.__name__ = "Integer32"
_ArubaWiredLedLocatorGroupIndex_Object = MibTableColumn
arubaWiredLedLocatorGroupIndex = _ArubaWiredLedLocatorGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 11, 7, 1, 1, 1, 1, 1),
    _ArubaWiredLedLocatorGroupIndex_Type()
)
arubaWiredLedLocatorGroupIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    arubaWiredLedLocatorGroupIndex.setStatus("current")


class _ArubaWiredLedLocatorName_Type(DisplayString):
    """Custom type arubaWiredLedLocatorName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_ArubaWiredLedLocatorName_Type.__name__ = "DisplayString"
_ArubaWiredLedLocatorName_Object = MibTableColumn
arubaWiredLedLocatorName = _ArubaWiredLedLocatorName_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 11, 7, 1, 1, 1, 1, 2),
    _ArubaWiredLedLocatorName_Type()
)
arubaWiredLedLocatorName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arubaWiredLedLocatorName.setStatus("current")


class _ArubaWiredLedLocatorState_Type(DisplayString):
    """Custom type arubaWiredLedLocatorState based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_ArubaWiredLedLocatorState_Type.__name__ = "DisplayString"
_ArubaWiredLedLocatorState_Object = MibTableColumn
arubaWiredLedLocatorState = _ArubaWiredLedLocatorState_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 11, 7, 1, 1, 1, 1, 3),
    _ArubaWiredLedLocatorState_Type()
)
arubaWiredLedLocatorState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arubaWiredLedLocatorState.setStatus("current")
_ArubaWiredLedLocatorConformance_ObjectIdentity = ObjectIdentity
arubaWiredLedLocatorConformance = _ArubaWiredLedLocatorConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 11, 7, 2)
)
_ArubaWiredLedLocatorCompliances_ObjectIdentity = ObjectIdentity
arubaWiredLedLocatorCompliances = _ArubaWiredLedLocatorCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 11, 7, 2, 1)
)
_ArubaWiredLedLocatorGroups_ObjectIdentity = ObjectIdentity
arubaWiredLedLocatorGroups = _ArubaWiredLedLocatorGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 11, 7, 2, 2)
)

# Managed Objects groups

arubaWiredLedLocatorTableGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 11, 7, 2, 2, 1)
)
arubaWiredLedLocatorTableGroup.setObjects(
      *(("ARUBAWIRED-LED-LOCATOR-MIB", "arubaWiredLedLocatorName"),
        ("ARUBAWIRED-LED-LOCATOR-MIB", "arubaWiredLedLocatorState"))
)
if mibBuilder.loadTexts:
    arubaWiredLedLocatorTableGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

arubaWiredLedLocatorCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 11, 7, 2, 1, 1)
)
arubaWiredLedLocatorCompliance.setObjects(
      *(("ARUBAWIRED-LED-LOCATOR-MIB", "arubaWiredLedLocatorTable"),
        ("ARUBAWIRED-LED-LOCATOR-MIB", "arubaWiredLedLocatorTableGroup"))
)
if mibBuilder.loadTexts:
    arubaWiredLedLocatorCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ARUBAWIRED-LED-LOCATOR-MIB",
    **{"arubaWiredLedLocator": arubaWiredLedLocator,
       "arubaWiredLedLocatorObjects": arubaWiredLedLocatorObjects,
       "arubaWiredLedLocatorDetails": arubaWiredLedLocatorDetails,
       "arubaWiredLedLocatorTable": arubaWiredLedLocatorTable,
       "arubaWiredLedLocatorEntry": arubaWiredLedLocatorEntry,
       "arubaWiredLedLocatorGroupIndex": arubaWiredLedLocatorGroupIndex,
       "arubaWiredLedLocatorName": arubaWiredLedLocatorName,
       "arubaWiredLedLocatorState": arubaWiredLedLocatorState,
       "arubaWiredLedLocatorConformance": arubaWiredLedLocatorConformance,
       "arubaWiredLedLocatorCompliances": arubaWiredLedLocatorCompliances,
       "arubaWiredLedLocatorCompliance": arubaWiredLedLocatorCompliance,
       "arubaWiredLedLocatorGroups": arubaWiredLedLocatorGroups,
       "arubaWiredLedLocatorTableGroup": arubaWiredLedLocatorTableGroup}
)
