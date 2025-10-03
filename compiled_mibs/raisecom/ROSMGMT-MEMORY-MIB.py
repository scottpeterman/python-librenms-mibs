# SNMP MIB module (ROSMGMT-MEMORY-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\raisecom\ROSMGMT-MEMORY-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 12:23:05 2025
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

(rosMgmtSystem,) = mibBuilder.importSymbols(
    "ROSMGMT-SYSTEM-MIB",
    "rosMgmtSystem")

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

(EnableVar,) = mibBuilder.importSymbols(
    "SWITCH-TC",
    "EnableVar")


# MODULE-IDENTITY

rosMgmtMemory = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 60, 1, 3)
)
if mibBuilder.loadTexts:
    rosMgmtMemory.setRevisions(
        ("2020-04-12 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_RosMgmtMemoryNotifications_ObjectIdentity = ObjectIdentity
rosMgmtMemoryNotifications = _RosMgmtMemoryNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 60, 1, 3, 0)
)
_RosMgmtMemoryObjects_ObjectIdentity = ObjectIdentity
rosMgmtMemoryObjects = _RosMgmtMemoryObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 60, 1, 3, 1)
)
_RosMgmtMemoryScalarGroup_ObjectIdentity = ObjectIdentity
rosMgmtMemoryScalarGroup = _RosMgmtMemoryScalarGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 60, 1, 3, 1, 1)
)
_RosMgmtMemoryTotal_Type = Integer32
_RosMgmtMemoryTotal_Object = MibScalar
rosMgmtMemoryTotal = _RosMgmtMemoryTotal_Object(
    (1, 3, 6, 1, 4, 1, 8886, 60, 1, 3, 1, 1, 1),
    _RosMgmtMemoryTotal_Type()
)
rosMgmtMemoryTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rosMgmtMemoryTotal.setStatus("current")
if mibBuilder.loadTexts:
    rosMgmtMemoryTotal.setUnits("KB")
_RosMgmtMemoryAvailable_Type = Integer32
_RosMgmtMemoryAvailable_Object = MibScalar
rosMgmtMemoryAvailable = _RosMgmtMemoryAvailable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 60, 1, 3, 1, 1, 2),
    _RosMgmtMemoryAvailable_Type()
)
rosMgmtMemoryAvailable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rosMgmtMemoryAvailable.setStatus("current")
if mibBuilder.loadTexts:
    rosMgmtMemoryAvailable.setUnits("KB")


class _RosMgmtMemoryUtil_Type(OctetString):
    """Custom type rosMgmtMemoryUtil based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 8),
    )


_RosMgmtMemoryUtil_Type.__name__ = "OctetString"
_RosMgmtMemoryUtil_Object = MibScalar
rosMgmtMemoryUtil = _RosMgmtMemoryUtil_Object(
    (1, 3, 6, 1, 4, 1, 8886, 60, 1, 3, 1, 1, 3),
    _RosMgmtMemoryUtil_Type()
)
rosMgmtMemoryUtil.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rosMgmtMemoryUtil.setStatus("current")
if mibBuilder.loadTexts:
    rosMgmtMemoryUtil.setUnits("percent")
_RosMgmtMemoryTrapEnable_Type = EnableVar
_RosMgmtMemoryTrapEnable_Object = MibScalar
rosMgmtMemoryTrapEnable = _RosMgmtMemoryTrapEnable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 60, 1, 3, 1, 1, 4),
    _RosMgmtMemoryTrapEnable_Type()
)
rosMgmtMemoryTrapEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rosMgmtMemoryTrapEnable.setStatus("deprecated")
_RosMgmtMemoryThrshd_Type = Integer32
_RosMgmtMemoryThrshd_Object = MibScalar
rosMgmtMemoryThrshd = _RosMgmtMemoryThrshd_Object(
    (1, 3, 6, 1, 4, 1, 8886, 60, 1, 3, 1, 1, 5),
    _RosMgmtMemoryThrshd_Type()
)
rosMgmtMemoryThrshd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rosMgmtMemoryThrshd.setStatus("current")
if mibBuilder.loadTexts:
    rosMgmtMemoryThrshd.setUnits("percent")
_RosMgmtMemoryThrshdRecover_Type = Integer32
_RosMgmtMemoryThrshdRecover_Object = MibScalar
rosMgmtMemoryThrshdRecover = _RosMgmtMemoryThrshdRecover_Object(
    (1, 3, 6, 1, 4, 1, 8886, 60, 1, 3, 1, 1, 6),
    _RosMgmtMemoryThrshdRecover_Type()
)
rosMgmtMemoryThrshdRecover.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rosMgmtMemoryThrshdRecover.setStatus("current")
if mibBuilder.loadTexts:
    rosMgmtMemoryThrshdRecover.setUnits("percent")
_RosMgmtMemoryMonInterval_Type = Integer32
_RosMgmtMemoryMonInterval_Object = MibScalar
rosMgmtMemoryMonInterval = _RosMgmtMemoryMonInterval_Object(
    (1, 3, 6, 1, 4, 1, 8886, 60, 1, 3, 1, 1, 7),
    _RosMgmtMemoryMonInterval_Type()
)
rosMgmtMemoryMonInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rosMgmtMemoryMonInterval.setStatus("current")
if mibBuilder.loadTexts:
    rosMgmtMemoryMonInterval.setUnits("second")
_RosMgmtMemoryConformance_ObjectIdentity = ObjectIdentity
rosMgmtMemoryConformance = _RosMgmtMemoryConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 60, 1, 3, 2)
)

# Managed Objects groups


# Notification objects

rosMgmtMemoryTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 60, 1, 3, 0, 1)
)
rosMgmtMemoryTrap.setObjects(
      *(("ROSMGMT-MEMORY-MIB", "rosMgmtMemoryTotal"),
        ("ROSMGMT-MEMORY-MIB", "rosMgmtMemoryUtil"),
        ("ROSMGMT-MEMORY-MIB", "rosMgmtMemoryThrshd"))
)
if mibBuilder.loadTexts:
    rosMgmtMemoryTrap.setStatus(
        "current"
    )

rosMgmtMemoryTrapRecover = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 60, 1, 3, 0, 2)
)
rosMgmtMemoryTrapRecover.setObjects(
      *(("ROSMGMT-MEMORY-MIB", "rosMgmtMemoryTotal"),
        ("ROSMGMT-MEMORY-MIB", "rosMgmtMemoryUtil"),
        ("ROSMGMT-MEMORY-MIB", "rosMgmtMemoryThrshdRecover"))
)
if mibBuilder.loadTexts:
    rosMgmtMemoryTrapRecover.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ROSMGMT-MEMORY-MIB",
    **{"rosMgmtMemory": rosMgmtMemory,
       "rosMgmtMemoryNotifications": rosMgmtMemoryNotifications,
       "rosMgmtMemoryTrap": rosMgmtMemoryTrap,
       "rosMgmtMemoryTrapRecover": rosMgmtMemoryTrapRecover,
       "rosMgmtMemoryObjects": rosMgmtMemoryObjects,
       "rosMgmtMemoryScalarGroup": rosMgmtMemoryScalarGroup,
       "rosMgmtMemoryTotal": rosMgmtMemoryTotal,
       "rosMgmtMemoryAvailable": rosMgmtMemoryAvailable,
       "rosMgmtMemoryUtil": rosMgmtMemoryUtil,
       "rosMgmtMemoryTrapEnable": rosMgmtMemoryTrapEnable,
       "rosMgmtMemoryThrshd": rosMgmtMemoryThrshd,
       "rosMgmtMemoryThrshdRecover": rosMgmtMemoryThrshdRecover,
       "rosMgmtMemoryMonInterval": rosMgmtMemoryMonInterval,
       "rosMgmtMemoryConformance": rosMgmtMemoryConformance}
)
