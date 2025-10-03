# SNMP MIB module (AT-UDLD-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\awplus\AT-UDLD-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:20:40 2025
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

(modules,) = mibBuilder.importSymbols(
    "AT-SMI-MIB",
    "modules")

(InterfaceIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex")

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

atUdld = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 550)
)
if mibBuilder.loadTexts:
    atUdld.setRevisions(
        ("2011-11-22 00:00",
         "2011-05-15 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AtUdldTrap_ObjectIdentity = ObjectIdentity
atUdldTrap = _AtUdldTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 550, 0)
)
_AtUdldIfIndex_Type = InterfaceIndex
_AtUdldIfIndex_Object = MibScalar
atUdldIfIndex = _AtUdldIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 550, 1),
    _AtUdldIfIndex_Type()
)
atUdldIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atUdldIfIndex.setStatus("current")

# Managed Objects groups


# Notification objects

atUdldPortDisabledTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 550, 0, 1)
)
atUdldPortDisabledTrap.setObjects(
    ("AT-UDLD-MIB", "atUdldIfIndex")
)
if mibBuilder.loadTexts:
    atUdldPortDisabledTrap.setStatus(
        "current"
    )

atUdldPortRecoveredTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 550, 0, 2)
)
atUdldPortRecoveredTrap.setObjects(
    ("AT-UDLD-MIB", "atUdldIfIndex")
)
if mibBuilder.loadTexts:
    atUdldPortRecoveredTrap.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "AT-UDLD-MIB",
    **{"atUdld": atUdld,
       "atUdldTrap": atUdldTrap,
       "atUdldPortDisabledTrap": atUdldPortDisabledTrap,
       "atUdldPortRecoveredTrap": atUdldPortRecoveredTrap,
       "atUdldIfIndex": atUdldIfIndex}
)
