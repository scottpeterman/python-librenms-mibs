# SNMP MIB module (PT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\ericsson\PT-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 12:21:31 2025
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

(miniLink,) = mibBuilder.importSymbols(
    "MINI-LINK-MIB",
    "miniLink")

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

pt = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 193, 223, 2)
)
if mibBuilder.loadTexts:
    pt.setRevisions(
        ("2017-01-21 12:00",
         "2016-03-09 12:00",
         "2016-02-10 12:30")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_PtDeviceType_Type = ObjectIdentifier
_PtDeviceType_Object = MibScalar
ptDeviceType = _PtDeviceType_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 1),
    _PtDeviceType_Type()
)
ptDeviceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ptDeviceType.setStatus("current")
_PtConformance_ObjectIdentity = ObjectIdentity
ptConformance = _PtConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 8)
)
_PtCompliances_ObjectIdentity = ObjectIdentity
ptCompliances = _PtCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 8, 1)
)
_PtGroups_ObjectIdentity = ObjectIdentity
ptGroups = _PtGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 8, 2)
)

# Managed Objects groups

ptCompleteGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 8, 2, 1)
)
ptCompleteGroup.setObjects(
    ("PT-MIB", "ptDeviceType")
)
if mibBuilder.loadTexts:
    ptCompleteGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

ptCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 8, 1, 1)
)
ptCompliance.setObjects(
    ("PT-MIB", "ptCompleteGroup")
)
if mibBuilder.loadTexts:
    ptCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "PT-MIB",
    **{"pt": pt,
       "ptDeviceType": ptDeviceType,
       "ptConformance": ptConformance,
       "ptCompliances": ptCompliances,
       "ptCompliance": ptCompliance,
       "ptGroups": ptGroups,
       "ptCompleteGroup": ptCompleteGroup}
)
