# SNMP MIB module (HH3C-PPP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\comware\HH3C-PPP-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:32:31 2025
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

hh3cPPP = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 175)
)
if mibBuilder.loadTexts:
    hh3cPPP.setRevisions(
        ("2018-02-01 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Hh3cPPPAuthObjects_ObjectIdentity = ObjectIdentity
hh3cPPPAuthObjects = _Hh3cPPPAuthObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 175, 1)
)
_Hh3cPPPAuthTable_Object = MibTable
hh3cPPPAuthTable = _Hh3cPPPAuthTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 175, 1, 1)
)
if mibBuilder.loadTexts:
    hh3cPPPAuthTable.setStatus("current")
_Hh3cPPPAuthEntry_Object = MibTableRow
hh3cPPPAuthEntry = _Hh3cPPPAuthEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 175, 1, 1, 1)
)
hh3cPPPAuthEntry.setIndexNames(
    (0, "HH3C-PPP-MIB", "hh3cPPPIfIndex"),
    (0, "HH3C-PPP-MIB", "hh3cPPPAuthType"),
)
if mibBuilder.loadTexts:
    hh3cPPPAuthEntry.setStatus("current")
_Hh3cPPPIfIndex_Type = InterfaceIndex
_Hh3cPPPIfIndex_Object = MibTableColumn
hh3cPPPIfIndex = _Hh3cPPPIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 175, 1, 1, 1, 1),
    _Hh3cPPPIfIndex_Type()
)
hh3cPPPIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cPPPIfIndex.setStatus("current")


class _Hh3cPPPAuthType_Type(Integer32):
    """Custom type hh3cPPPAuthType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 1),
          ("pap", 2),
          ("chap", 3))
    )


_Hh3cPPPAuthType_Type.__name__ = "Integer32"
_Hh3cPPPAuthType_Object = MibTableColumn
hh3cPPPAuthType = _Hh3cPPPAuthType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 175, 1, 1, 1, 2),
    _Hh3cPPPAuthType_Type()
)
hh3cPPPAuthType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cPPPAuthType.setStatus("current")


class _Hh3cPPPUserName_Type(DisplayString):
    """Custom type hh3cPPPUserName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 80),
    )


_Hh3cPPPUserName_Type.__name__ = "DisplayString"
_Hh3cPPPUserName_Object = MibTableColumn
hh3cPPPUserName = _Hh3cPPPUserName_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 175, 1, 1, 1, 3),
    _Hh3cPPPUserName_Type()
)
hh3cPPPUserName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cPPPUserName.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HH3C-PPP-MIB",
    **{"hh3cPPP": hh3cPPP,
       "hh3cPPPAuthObjects": hh3cPPPAuthObjects,
       "hh3cPPPAuthTable": hh3cPPPAuthTable,
       "hh3cPPPAuthEntry": hh3cPPPAuthEntry,
       "hh3cPPPIfIndex": hh3cPPPIfIndex,
       "hh3cPPPAuthType": hh3cPPPAuthType,
       "hh3cPPPUserName": hh3cPPPUserName}
)
