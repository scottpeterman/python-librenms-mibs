# SNMP MIB module (Juniper-HTTP-Profile-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\junose\Juniper-HTTP-Profile-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 12:06:39 2025
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

(juniMibs,) = mibBuilder.importSymbols(
    "Juniper-MIBs",
    "juniMibs")

(JuniSetMap,) = mibBuilder.importSymbols(
    "Juniper-TC",
    "JuniSetMap")

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

juniHttpProfileMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 79)
)
if mibBuilder.loadTexts:
    juniHttpProfileMIB.setRevisions(
        ("2005-08-19 14:21",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_JuniHttpProfileObjects_ObjectIdentity = ObjectIdentity
juniHttpProfileObjects = _JuniHttpProfileObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 79, 1)
)
_JuniHttpProfile_ObjectIdentity = ObjectIdentity
juniHttpProfile = _JuniHttpProfile_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 79, 1, 1)
)
_JuniHttpProfileTable_Object = MibTable
juniHttpProfileTable = _JuniHttpProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 79, 1, 1, 1)
)
if mibBuilder.loadTexts:
    juniHttpProfileTable.setStatus("current")
_JuniHttpProfileEntry_Object = MibTableRow
juniHttpProfileEntry = _JuniHttpProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 79, 1, 1, 1, 1)
)
juniHttpProfileEntry.setIndexNames(
    (0, "Juniper-HTTP-Profile-MIB", "juniHttpProfileId"),
)
if mibBuilder.loadTexts:
    juniHttpProfileEntry.setStatus("current")
_JuniHttpProfileId_Type = Unsigned32
_JuniHttpProfileId_Object = MibTableColumn
juniHttpProfileId = _JuniHttpProfileId_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 79, 1, 1, 1, 1, 1),
    _JuniHttpProfileId_Type()
)
juniHttpProfileId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    juniHttpProfileId.setStatus("current")
_JuniHttpProfileSetMap_Type = JuniSetMap
_JuniHttpProfileSetMap_Object = MibTableColumn
juniHttpProfileSetMap = _JuniHttpProfileSetMap_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 79, 1, 1, 1, 1, 2),
    _JuniHttpProfileSetMap_Type()
)
juniHttpProfileSetMap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniHttpProfileSetMap.setStatus("current")


class _JuniHttpProfileRedirectUrl_Type(DisplayString):
    """Custom type juniHttpProfileRedirectUrl based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_JuniHttpProfileRedirectUrl_Type.__name__ = "DisplayString"
_JuniHttpProfileRedirectUrl_Object = MibTableColumn
juniHttpProfileRedirectUrl = _JuniHttpProfileRedirectUrl_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 79, 1, 1, 1, 1, 3),
    _JuniHttpProfileRedirectUrl_Type()
)
juniHttpProfileRedirectUrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniHttpProfileRedirectUrl.setStatus("current")
_JuniHttpProfileConformance_ObjectIdentity = ObjectIdentity
juniHttpProfileConformance = _JuniHttpProfileConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 79, 4)
)
_JuniHttpProfileCompliances_ObjectIdentity = ObjectIdentity
juniHttpProfileCompliances = _JuniHttpProfileCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 79, 4, 1)
)
_JuniHttpProfileGroups_ObjectIdentity = ObjectIdentity
juniHttpProfileGroups = _JuniHttpProfileGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 79, 4, 2)
)

# Managed Objects groups

juniHttpProfileGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 79, 4, 2, 1)
)
juniHttpProfileGroup.setObjects(
      *(("Juniper-HTTP-Profile-MIB", "juniHttpProfileSetMap"),
        ("Juniper-HTTP-Profile-MIB", "juniHttpProfileRedirectUrl"))
)
if mibBuilder.loadTexts:
    juniHttpProfileGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

juniHttpProfileCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 79, 4, 1, 1)
)
juniHttpProfileCompliance.setObjects(
    ("Juniper-HTTP-Profile-MIB", "juniHttpProfileGroup")
)
if mibBuilder.loadTexts:
    juniHttpProfileCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Juniper-HTTP-Profile-MIB",
    **{"juniHttpProfileMIB": juniHttpProfileMIB,
       "juniHttpProfileObjects": juniHttpProfileObjects,
       "juniHttpProfile": juniHttpProfile,
       "juniHttpProfileTable": juniHttpProfileTable,
       "juniHttpProfileEntry": juniHttpProfileEntry,
       "juniHttpProfileId": juniHttpProfileId,
       "juniHttpProfileSetMap": juniHttpProfileSetMap,
       "juniHttpProfileRedirectUrl": juniHttpProfileRedirectUrl,
       "juniHttpProfileConformance": juniHttpProfileConformance,
       "juniHttpProfileCompliances": juniHttpProfileCompliances,
       "juniHttpProfileCompliance": juniHttpProfileCompliance,
       "juniHttpProfileGroups": juniHttpProfileGroups,
       "juniHttpProfileGroup": juniHttpProfileGroup}
)
