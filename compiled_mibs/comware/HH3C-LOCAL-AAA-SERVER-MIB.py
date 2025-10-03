# SNMP MIB module (HH3C-LOCAL-AAA-SERVER-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\comware\HH3C-LOCAL-AAA-SERVER-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:32:01 2025
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

(hh3cCommon,) = mibBuilder.importSymbols(
    "HH3C-OID-MIB",
    "hh3cCommon")

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

hh3cLocAAASvr = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 141)
)
if mibBuilder.loadTexts:
    hh3cLocAAASvr.setRevisions(
        ("2013-07-06 09:45",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Hh3cLocAAASvrControl_ObjectIdentity = ObjectIdentity
hh3cLocAAASvrControl = _Hh3cLocAAASvrControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 141, 1)
)
_Hh3cLocAAASvrTables_ObjectIdentity = ObjectIdentity
hh3cLocAAASvrTables = _Hh3cLocAAASvrTables_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 141, 2)
)
_Hh3cLocAAASvrTrap_ObjectIdentity = ObjectIdentity
hh3cLocAAASvrTrap = _Hh3cLocAAASvrTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 141, 3)
)
_Hh3cLocAAASvrTrapPrex_ObjectIdentity = ObjectIdentity
hh3cLocAAASvrTrapPrex = _Hh3cLocAAASvrTrapPrex_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 141, 3, 0)
)

# Managed Objects groups


# Notification objects

hh3cLocAAASvrBillExportFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 141, 3, 0, 1)
)
if mibBuilder.loadTexts:
    hh3cLocAAASvrBillExportFailed.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HH3C-LOCAL-AAA-SERVER-MIB",
    **{"hh3cLocAAASvr": hh3cLocAAASvr,
       "hh3cLocAAASvrControl": hh3cLocAAASvrControl,
       "hh3cLocAAASvrTables": hh3cLocAAASvrTables,
       "hh3cLocAAASvrTrap": hh3cLocAAASvrTrap,
       "hh3cLocAAASvrTrapPrex": hh3cLocAAASvrTrapPrex,
       "hh3cLocAAASvrBillExportFailed": hh3cLocAAASvrBillExportFailed}
)
