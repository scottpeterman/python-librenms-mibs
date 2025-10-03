# SNMP MIB module (ADTRAN-AOS-OVER-TEMP-PROTECTION-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\adtran\ADTRAN-AOS-OVER-TEMP-PROTECTION-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:14:22 2025
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

(adGenAOSCommon,
 adGenAOSConformance) = mibBuilder.importSymbols(
    "ADTRAN-AOS",
    "adGenAOSCommon",
    "adGenAOSConformance")

(adIdentity,) = mibBuilder.importSymbols(
    "ADTRAN-MIB",
    "adIdentity")

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
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

adGenAOSOverTempProtectionMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 53, 1, 10)
)
if mibBuilder.loadTexts:
    adGenAOSOverTempProtectionMib.setRevisions(
        ("2014-11-04 16:15",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AdGenAOSOverTempProtection_ObjectIdentity = ObjectIdentity
adGenAOSOverTempProtection = _AdGenAOSOverTempProtection_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 10)
)
_AdGenAOSOverTempProtectionTrap_ObjectIdentity = ObjectIdentity
adGenAOSOverTempProtectionTrap = _AdGenAOSOverTempProtectionTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 10, 0)
)
_AdGenAOSOverTempProtectionConformance_ObjectIdentity = ObjectIdentity
adGenAOSOverTempProtectionConformance = _AdGenAOSOverTempProtectionConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 19)
)
_AdGenAOSOverTempProtectionGroups_ObjectIdentity = ObjectIdentity
adGenAOSOverTempProtectionGroups = _AdGenAOSOverTempProtectionGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 19, 1)
)
_AdGenAOSOverTempProtectionCompliances_ObjectIdentity = ObjectIdentity
adGenAOSOverTempProtectionCompliances = _AdGenAOSOverTempProtectionCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 19, 2)
)

# Managed Objects groups


# Notification objects

adGenAOSOverTempProtectionWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 10, 0, 1)
)
if mibBuilder.loadTexts:
    adGenAOSOverTempProtectionWarning.setStatus(
        "current"
    )

adGenAOSOverTempProtectionShutdown = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 10, 0, 2)
)
if mibBuilder.loadTexts:
    adGenAOSOverTempProtectionShutdown.setStatus(
        "current"
    )


# Notifications groups

adGenAOSOverTempProtectionNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 19, 1, 1)
)
adGenAOSOverTempProtectionNotificationGroup.setObjects(
      *(("ADTRAN-AOS-OVER-TEMP-PROTECTION-MIB", "adGenAOSOverTempProtectionWarning"),
        ("ADTRAN-AOS-OVER-TEMP-PROTECTION-MIB", "adGenAOSOverTempProtectionShutdown"))
)
if mibBuilder.loadTexts:
    adGenAOSOverTempProtectionNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

adGenAOSOverTempProtectionFullCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 19, 2, 1)
)
adGenAOSOverTempProtectionFullCompliance.setObjects(
    ("ADTRAN-AOS-OVER-TEMP-PROTECTION-MIB", "adGenAOSOverTempProtectionNotificationGroup")
)
if mibBuilder.loadTexts:
    adGenAOSOverTempProtectionFullCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ADTRAN-AOS-OVER-TEMP-PROTECTION-MIB",
    **{"adGenAOSOverTempProtection": adGenAOSOverTempProtection,
       "adGenAOSOverTempProtectionTrap": adGenAOSOverTempProtectionTrap,
       "adGenAOSOverTempProtectionWarning": adGenAOSOverTempProtectionWarning,
       "adGenAOSOverTempProtectionShutdown": adGenAOSOverTempProtectionShutdown,
       "adGenAOSOverTempProtectionConformance": adGenAOSOverTempProtectionConformance,
       "adGenAOSOverTempProtectionGroups": adGenAOSOverTempProtectionGroups,
       "adGenAOSOverTempProtectionNotificationGroup": adGenAOSOverTempProtectionNotificationGroup,
       "adGenAOSOverTempProtectionCompliances": adGenAOSOverTempProtectionCompliances,
       "adGenAOSOverTempProtectionFullCompliance": adGenAOSOverTempProtectionFullCompliance,
       "adGenAOSOverTempProtectionMib": adGenAOSOverTempProtectionMib}
)
