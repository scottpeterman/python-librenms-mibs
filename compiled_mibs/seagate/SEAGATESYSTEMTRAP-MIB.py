# SNMP MIB module (SEAGATESYSTEMTRAP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\seagate\SEAGATESYSTEMTRAP-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 12:26:19 2025
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

(connUnitEventDescr,
 connUnitEventId,
 connUnitEventType) = mibBuilder.importSymbols(
    "FCMGMT-MIB",
    "connUnitEventDescr",
    "connUnitEventId",
    "connUnitEventType")

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
 NotificationType,
 TimeTicks,
 Unsigned32,
 enterprises,
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
    "NotificationType",
    "TimeTicks",
    "Unsigned32",
    "enterprises",
    "iso")

(DisplayString,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_SeagateSystems_ObjectIdentity = ObjectIdentity
seagateSystems = _SeagateSystems_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 347)
)

# Managed Objects groups


# Notification objects

seagateEventInfoTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 347, 0, 1)
)
seagateEventInfoTrap.setObjects(
      *(("FCMGMT-MIB", "connUnitEventId"),
        ("FCMGMT-MIB", "connUnitEventType"),
        ("FCMGMT-MIB", "connUnitEventDescr"))
)
if mibBuilder.loadTexts:
    seagateEventInfoTrap.setStatus(
        ""
    )

seagateEventWarningTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 347, 0, 2)
)
seagateEventWarningTrap.setObjects(
      *(("FCMGMT-MIB", "connUnitEventId"),
        ("FCMGMT-MIB", "connUnitEventType"),
        ("FCMGMT-MIB", "connUnitEventDescr"))
)
if mibBuilder.loadTexts:
    seagateEventWarningTrap.setStatus(
        ""
    )

seagateEventErrorTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 347, 0, 3)
)
seagateEventErrorTrap.setObjects(
      *(("FCMGMT-MIB", "connUnitEventId"),
        ("FCMGMT-MIB", "connUnitEventType"),
        ("FCMGMT-MIB", "connUnitEventDescr"))
)
if mibBuilder.loadTexts:
    seagateEventErrorTrap.setStatus(
        ""
    )

seagateEventCriticalTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 347, 0, 4)
)
seagateEventCriticalTrap.setObjects(
      *(("FCMGMT-MIB", "connUnitEventId"),
        ("FCMGMT-MIB", "connUnitEventType"),
        ("FCMGMT-MIB", "connUnitEventDescr"))
)
if mibBuilder.loadTexts:
    seagateEventCriticalTrap.setStatus(
        ""
    )

seagateEventResolvedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 347, 0, 5)
)
seagateEventResolvedTrap.setObjects(
      *(("FCMGMT-MIB", "connUnitEventId"),
        ("FCMGMT-MIB", "connUnitEventType"),
        ("FCMGMT-MIB", "connUnitEventDescr"))
)
if mibBuilder.loadTexts:
    seagateEventResolvedTrap.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SEAGATESYSTEMTRAP-MIB",
    **{"seagateSystems": seagateSystems,
       "seagateEventInfoTrap": seagateEventInfoTrap,
       "seagateEventWarningTrap": seagateEventWarningTrap,
       "seagateEventErrorTrap": seagateEventErrorTrap,
       "seagateEventCriticalTrap": seagateEventCriticalTrap,
       "seagateEventResolvedTrap": seagateEventResolvedTrap}
)
