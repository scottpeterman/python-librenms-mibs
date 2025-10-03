# SNMP MIB module (HH3C-MULTICAST-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\comware\HH3C-MULTICAST-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:32:21 2025
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

hh3cMulticast = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 50)
)
if mibBuilder.loadTexts:
    hh3cMulticast.setRevisions(
        ("2005-04-29 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class EnabledStatus(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 1),
          ("disabled", 2))
    )



# MIB Managed Objects in the order of their OIDs

_Hh3cMulticastObject_ObjectIdentity = ObjectIdentity
hh3cMulticastObject = _Hh3cMulticastObject_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 50, 1)
)


class _Hh3cMulticastEnable_Type(EnabledStatus):
    """Custom type hh3cMulticastEnable based on EnabledStatus"""
    defaultValue = 2


_Hh3cMulticastEnable_Type.__name__ = "EnabledStatus"
_Hh3cMulticastEnable_Object = MibScalar
hh3cMulticastEnable = _Hh3cMulticastEnable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 50, 1, 1),
    _Hh3cMulticastEnable_Type()
)
hh3cMulticastEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cMulticastEnable.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HH3C-MULTICAST-MIB",
    **{"EnabledStatus": EnabledStatus,
       "hh3cMulticast": hh3cMulticast,
       "hh3cMulticastObject": hh3cMulticastObject,
       "hh3cMulticastEnable": hh3cMulticastEnable}
)
