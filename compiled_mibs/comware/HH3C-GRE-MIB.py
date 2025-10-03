# SNMP MIB module (HH3C-GRE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\comware\HH3C-GRE-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:31:47 2025
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

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

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

hh3cGre = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 54)
)
if mibBuilder.loadTexts:
    hh3cGre.setRevisions(
        ("2005-06-04 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Hh3cGreObjects_ObjectIdentity = ObjectIdentity
hh3cGreObjects = _Hh3cGreObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 54, 1)
)
_Hh3cGreTable_Object = MibTable
hh3cGreTable = _Hh3cGreTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 54, 1, 1)
)
if mibBuilder.loadTexts:
    hh3cGreTable.setStatus("current")
_Hh3cGreEntry_Object = MibTableRow
hh3cGreEntry = _Hh3cGreEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 54, 1, 1, 1)
)
hh3cGreEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    hh3cGreEntry.setStatus("current")
_Hh3cGreKeyValue_Type = Unsigned32
_Hh3cGreKeyValue_Object = MibTableColumn
hh3cGreKeyValue = _Hh3cGreKeyValue_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 54, 1, 1, 1, 1),
    _Hh3cGreKeyValue_Type()
)
hh3cGreKeyValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cGreKeyValue.setStatus("current")


class _Hh3cGreKey_Type(Integer32):
    """Custom type hh3cGreKey based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_Hh3cGreKey_Type.__name__ = "Integer32"
_Hh3cGreKey_Object = MibTableColumn
hh3cGreKey = _Hh3cGreKey_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 54, 1, 1, 1, 2),
    _Hh3cGreKey_Type()
)
hh3cGreKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cGreKey.setStatus("current")


class _Hh3cGreChecksum_Type(Integer32):
    """Custom type hh3cGreChecksum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_Hh3cGreChecksum_Type.__name__ = "Integer32"
_Hh3cGreChecksum_Object = MibTableColumn
hh3cGreChecksum = _Hh3cGreChecksum_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 54, 1, 1, 1, 3),
    _Hh3cGreChecksum_Type()
)
hh3cGreChecksum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cGreChecksum.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HH3C-GRE-MIB",
    **{"hh3cGre": hh3cGre,
       "hh3cGreObjects": hh3cGreObjects,
       "hh3cGreTable": hh3cGreTable,
       "hh3cGreEntry": hh3cGreEntry,
       "hh3cGreKeyValue": hh3cGreKeyValue,
       "hh3cGreKey": hh3cGreKey,
       "hh3cGreChecksum": hh3cGreChecksum}
)
