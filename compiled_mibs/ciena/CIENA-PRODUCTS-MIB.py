# SNMP MIB module (CIENA-PRODUCTS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\ciena\CIENA-PRODUCTS-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:25:00 2025
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

(cienaCommon,
 cienaProducts) = mibBuilder.importSymbols(
    "CIENA-SMI",
    "cienaCommon",
    "cienaProducts")

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

cienaProductsMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 1, 1)
)
if mibBuilder.loadTexts:
    cienaProductsMIB.setRevisions(
        ("2017-06-07 00:00",
         "2014-01-21 00:00",
         "2013-03-05 00:00",
         "2010-03-28 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Cn5410_ObjectIdentity = ObjectIdentity
cn5410 = _Cn5410_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 1, 2, 1)
)
_Cn5430_ObjectIdentity = ObjectIdentity
cn5430 = _Cn5430_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 1, 2, 2)
)
_Ome6500_ObjectIdentity = ObjectIdentity
ome6500 = _Ome6500_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 1, 2, 3)
)
_Pn8500_10_ObjectIdentity = ObjectIdentity
pn8500_10 = _Pn8500_10_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 1, 2, 4)
)
_Pn8500_30_ObjectIdentity = ObjectIdentity
pn8500_30 = _Pn8500_30_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 1, 2, 5)
)
_Pn8700_2_ObjectIdentity = ObjectIdentity
pn8700_2 = _Pn8700_2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 1, 2, 6)
)
_Pn8700_4_ObjectIdentity = ObjectIdentity
pn8700_4 = _Pn8700_4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 1, 2, 7)
)
_Pn8700_10_ObjectIdentity = ObjectIdentity
pn8700_10 = _Pn8700_10_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 1, 2, 8)
)
_Pn8700_20_ObjectIdentity = ObjectIdentity
pn8700_20 = _Pn8700_20_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 1, 2, 9)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CIENA-PRODUCTS-MIB",
    **{"cienaProductsMIB": cienaProductsMIB,
       "cn5410": cn5410,
       "cn5430": cn5430,
       "ome6500": ome6500,
       "pn8500-10": pn8500_10,
       "pn8500-30": pn8500_30,
       "pn8700-2": pn8700_2,
       "pn8700-4": pn8700_4,
       "pn8700-10": pn8700_10,
       "pn8700-20": pn8700_20}
)
