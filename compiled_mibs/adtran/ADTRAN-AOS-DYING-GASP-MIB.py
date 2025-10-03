# SNMP MIB module (ADTRAN-AOS-DYING-GASP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\adtran\ADTRAN-AOS-DYING-GASP-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:14:17 2025
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

adGenAOSDyingGaspMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 53, 1, 11)
)
if mibBuilder.loadTexts:
    adGenAOSDyingGaspMib.setRevisions(
        ("2015-01-05 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AdGenAOSDyingGasp_ObjectIdentity = ObjectIdentity
adGenAOSDyingGasp = _AdGenAOSDyingGasp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 11)
)
_AdGenAOSDyingGaspTrap_ObjectIdentity = ObjectIdentity
adGenAOSDyingGaspTrap = _AdGenAOSDyingGaspTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 11, 0)
)
_AdGenAOSDyingGaspConformance_ObjectIdentity = ObjectIdentity
adGenAOSDyingGaspConformance = _AdGenAOSDyingGaspConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 25)
)
_AdGenAOSDyingGaspGroups_ObjectIdentity = ObjectIdentity
adGenAOSDyingGaspGroups = _AdGenAOSDyingGaspGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 25, 1)
)
_AdGenAOSDyingGaspCompliances_ObjectIdentity = ObjectIdentity
adGenAOSDyingGaspCompliances = _AdGenAOSDyingGaspCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 25, 2)
)

# Managed Objects groups


# Notification objects

adGenAOSDyingGaspEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 11, 0, 1)
)
if mibBuilder.loadTexts:
    adGenAOSDyingGaspEvent.setStatus(
        "current"
    )


# Notifications groups

adGenAOSDyingGaspGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 25, 1, 1)
)
adGenAOSDyingGaspGroup.setObjects(
    ("ADTRAN-AOS-DYING-GASP-MIB", "adGenAOSDyingGaspEvent")
)
if mibBuilder.loadTexts:
    adGenAOSDyingGaspGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

adGenAOSDyingGaspFullCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 25, 2, 1)
)
adGenAOSDyingGaspFullCompliance.setObjects(
    ("ADTRAN-AOS-DYING-GASP-MIB", "adGenAOSDyingGaspGroup")
)
if mibBuilder.loadTexts:
    adGenAOSDyingGaspFullCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ADTRAN-AOS-DYING-GASP-MIB",
    **{"adGenAOSDyingGasp": adGenAOSDyingGasp,
       "adGenAOSDyingGaspTrap": adGenAOSDyingGaspTrap,
       "adGenAOSDyingGaspEvent": adGenAOSDyingGaspEvent,
       "adGenAOSDyingGaspConformance": adGenAOSDyingGaspConformance,
       "adGenAOSDyingGaspGroups": adGenAOSDyingGaspGroups,
       "adGenAOSDyingGaspGroup": adGenAOSDyingGaspGroup,
       "adGenAOSDyingGaspCompliances": adGenAOSDyingGaspCompliances,
       "adGenAOSDyingGaspFullCompliance": adGenAOSDyingGaspFullCompliance,
       "adGenAOSDyingGaspMib": adGenAOSDyingGaspMib}
)
