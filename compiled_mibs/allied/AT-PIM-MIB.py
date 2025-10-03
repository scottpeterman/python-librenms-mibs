# SNMP MIB module (AT-PIM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\allied\AT-PIM-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:17:30 2025
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

(pimInterfaceStatus,
 pimNeighborIfIndex) = mibBuilder.importSymbols(
    "PIM-MIB",
    "pimInterfaceStatus",
    "pimNeighborIfIndex")

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

pim4 = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 97)
)
if mibBuilder.loadTexts:
    pim4.setRevisions(
        ("2005-01-20 15:25",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Pim4Events_ObjectIdentity = ObjectIdentity
pim4Events = _Pim4Events_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 97, 0)
)


class _Pim4ErrorTrapType_Type(Integer32):
    """Custom type pim4ErrorTrapType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10)
        )
    )
    namedValues = NamedValues(
        *(("pim4InvalidPacket", 1),
          ("pim4InvalidDestinationError", 2),
          ("pim4FragmentError", 3),
          ("pim4LengthError", 4),
          ("pim4GroupaddressError", 5),
          ("pim4SourceaddressError", 6),
          ("pim4MissingOptionError", 7),
          ("pim4GeneralError", 8),
          ("pim4InternalError", 9),
          ("pim4RpaddressError", 10))
    )


_Pim4ErrorTrapType_Type.__name__ = "Integer32"
_Pim4ErrorTrapType_Object = MibScalar
pim4ErrorTrapType = _Pim4ErrorTrapType_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 97, 1),
    _Pim4ErrorTrapType_Type()
)
pim4ErrorTrapType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    pim4ErrorTrapType.setStatus("current")

# Managed Objects groups


# Notification objects

pim4NeighbourAddedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 97, 0, 1)
)
pim4NeighbourAddedTrap.setObjects(
    ("PIM-MIB", "pimNeighborIfIndex")
)
if mibBuilder.loadTexts:
    pim4NeighbourAddedTrap.setStatus(
        "current"
    )

pim4NeighbourDeletedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 97, 0, 2)
)
pim4NeighbourDeletedTrap.setObjects(
    ("PIM-MIB", "pimNeighborIfIndex")
)
if mibBuilder.loadTexts:
    pim4NeighbourDeletedTrap.setStatus(
        "current"
    )

pim4InterfaceUpTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 97, 0, 3)
)
pim4InterfaceUpTrap.setObjects(
    ("PIM-MIB", "pimInterfaceStatus")
)
if mibBuilder.loadTexts:
    pim4InterfaceUpTrap.setStatus(
        "current"
    )

pim4InterfaceDownTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 97, 0, 4)
)
pim4InterfaceDownTrap.setObjects(
    ("PIM-MIB", "pimInterfaceStatus")
)
if mibBuilder.loadTexts:
    pim4InterfaceDownTrap.setStatus(
        "current"
    )

pim4ErrorTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 97, 0, 5)
)
pim4ErrorTrap.setObjects(
    ("AT-PIM-MIB", "pim4ErrorTrapType")
)
if mibBuilder.loadTexts:
    pim4ErrorTrap.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "AT-PIM-MIB",
    **{"pim4": pim4,
       "pim4Events": pim4Events,
       "pim4NeighbourAddedTrap": pim4NeighbourAddedTrap,
       "pim4NeighbourDeletedTrap": pim4NeighbourDeletedTrap,
       "pim4InterfaceUpTrap": pim4InterfaceUpTrap,
       "pim4InterfaceDownTrap": pim4InterfaceDownTrap,
       "pim4ErrorTrap": pim4ErrorTrap,
       "pim4ErrorTrapType": pim4ErrorTrapType}
)
