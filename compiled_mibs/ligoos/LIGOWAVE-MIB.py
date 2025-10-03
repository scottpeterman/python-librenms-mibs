# SNMP MIB module (LIGOWAVE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\ligoos\LIGOWAVE-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 12:08:39 2025
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

ligowave = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 32750)
)
if mibBuilder.loadTexts:
    ligowave.setRevisions(
        ("2008-09-05 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_LigoProducts_ObjectIdentity = ObjectIdentity
ligoProducts = _LigoProducts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 32750, 1)
)
_LigoAdmin_ObjectIdentity = ObjectIdentity
ligoAdmin = _LigoAdmin_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 32750, 2)
)
_LigoMgmt_ObjectIdentity = ObjectIdentity
ligoMgmt = _LigoMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 32750, 3)
)
_LigoExperimental_ObjectIdentity = ObjectIdentity
ligoExperimental = _LigoExperimental_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 32750, 7)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "LIGOWAVE-MIB",
    **{"ligowave": ligowave,
       "ligoProducts": ligoProducts,
       "ligoAdmin": ligoAdmin,
       "ligoMgmt": ligoMgmt,
       "ligoExperimental": ligoExperimental}
)
