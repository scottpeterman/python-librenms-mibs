# SNMP MIB module (HH3C-ARP-SOURCE-SUPPRESSION-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\comware\HH3C-ARP-SOURCE-SUPPRESSION-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:30:44 2025
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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

hh3cARPSourceSuppression = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 146)
)
if mibBuilder.loadTexts:
    hh3cARPSourceSuppression.setRevisions(
        ("2013-10-14 18:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Hh3cARPSourceSuppressionObjects_ObjectIdentity = ObjectIdentity
hh3cARPSourceSuppressionObjects = _Hh3cARPSourceSuppressionObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 146, 1)
)
_Hh3cARPSourceSuppressionGlobal_ObjectIdentity = ObjectIdentity
hh3cARPSourceSuppressionGlobal = _Hh3cARPSourceSuppressionGlobal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 146, 1, 1)
)
_Hh3cARPSourceSuppressionEnable_Type = TruthValue
_Hh3cARPSourceSuppressionEnable_Object = MibScalar
hh3cARPSourceSuppressionEnable = _Hh3cARPSourceSuppressionEnable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 146, 1, 1, 1),
    _Hh3cARPSourceSuppressionEnable_Type()
)
hh3cARPSourceSuppressionEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cARPSourceSuppressionEnable.setStatus("current")


class _Hh3cARPSourceSuppressionLimit_Type(Unsigned32):
    """Custom type hh3cARPSourceSuppressionLimit based on Unsigned32"""
    defaultValue = 10

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 1024),
    )


_Hh3cARPSourceSuppressionLimit_Type.__name__ = "Unsigned32"
_Hh3cARPSourceSuppressionLimit_Object = MibScalar
hh3cARPSourceSuppressionLimit = _Hh3cARPSourceSuppressionLimit_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 146, 1, 1, 2),
    _Hh3cARPSourceSuppressionLimit_Type()
)
hh3cARPSourceSuppressionLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cARPSourceSuppressionLimit.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HH3C-ARP-SOURCE-SUPPRESSION-MIB",
    **{"hh3cARPSourceSuppression": hh3cARPSourceSuppression,
       "hh3cARPSourceSuppressionObjects": hh3cARPSourceSuppressionObjects,
       "hh3cARPSourceSuppressionGlobal": hh3cARPSourceSuppressionGlobal,
       "hh3cARPSourceSuppressionEnable": hh3cARPSourceSuppressionEnable,
       "hh3cARPSourceSuppressionLimit": hh3cARPSourceSuppressionLimit}
)
