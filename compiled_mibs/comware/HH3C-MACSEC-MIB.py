# SNMP MIB module (HH3C-MACSEC-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\comware\HH3C-MACSEC-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:32:07 2025
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

hh3cMACsec = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 163)
)
if mibBuilder.loadTexts:
    hh3cMACsec.setRevisions(
        ("2015-09-01 16:15",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Hh3cMACsecCFGObjects_ObjectIdentity = ObjectIdentity
hh3cMACsecCFGObjects = _Hh3cMACsecCFGObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 163, 1)
)
_Hh3cMACsecCFGPortTable_Object = MibTable
hh3cMACsecCFGPortTable = _Hh3cMACsecCFGPortTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 163, 1, 1)
)
if mibBuilder.loadTexts:
    hh3cMACsecCFGPortTable.setStatus("current")
_Hh3cMACsecCFGPortEntry_Object = MibTableRow
hh3cMACsecCFGPortEntry = _Hh3cMACsecCFGPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 163, 1, 1, 1)
)
hh3cMACsecCFGPortEntry.setIndexNames(
    (0, "HH3C-MACSEC-MIB", "hh3cMACsecCFGPortIndex"),
)
if mibBuilder.loadTexts:
    hh3cMACsecCFGPortEntry.setStatus("current")
_Hh3cMACsecCFGPortIndex_Type = InterfaceIndex
_Hh3cMACsecCFGPortIndex_Object = MibTableColumn
hh3cMACsecCFGPortIndex = _Hh3cMACsecCFGPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 163, 1, 1, 1, 1),
    _Hh3cMACsecCFGPortIndex_Type()
)
hh3cMACsecCFGPortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cMACsecCFGPortIndex.setStatus("current")


class _Hh3cMACsecCFGPortPSKCKNName_Type(OctetString):
    """Custom type hh3cMACsecCFGPortPSKCKNName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_Hh3cMACsecCFGPortPSKCKNName_Type.__name__ = "OctetString"
_Hh3cMACsecCFGPortPSKCKNName_Object = MibTableColumn
hh3cMACsecCFGPortPSKCKNName = _Hh3cMACsecCFGPortPSKCKNName_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 163, 1, 1, 1, 2),
    _Hh3cMACsecCFGPortPSKCKNName_Type()
)
hh3cMACsecCFGPortPSKCKNName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cMACsecCFGPortPSKCKNName.setStatus("current")


class _Hh3cMACsecCFGPortPSKCAKValue_Type(OctetString):
    """Custom type hh3cMACsecCFGPortPSKCAKValue based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_Hh3cMACsecCFGPortPSKCAKValue_Type.__name__ = "OctetString"
_Hh3cMACsecCFGPortPSKCAKValue_Object = MibTableColumn
hh3cMACsecCFGPortPSKCAKValue = _Hh3cMACsecCFGPortPSKCAKValue_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 163, 1, 1, 1, 3),
    _Hh3cMACsecCFGPortPSKCAKValue_Type()
)
hh3cMACsecCFGPortPSKCAKValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cMACsecCFGPortPSKCAKValue.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HH3C-MACSEC-MIB",
    **{"hh3cMACsec": hh3cMACsec,
       "hh3cMACsecCFGObjects": hh3cMACsecCFGObjects,
       "hh3cMACsecCFGPortTable": hh3cMACsecCFGPortTable,
       "hh3cMACsecCFGPortEntry": hh3cMACsecCFGPortEntry,
       "hh3cMACsecCFGPortIndex": hh3cMACsecCFGPortIndex,
       "hh3cMACsecCFGPortPSKCKNName": hh3cMACsecCFGPortPSKCKNName,
       "hh3cMACsecCFGPortPSKCAKValue": hh3cMACsecCFGPortPSKCAKValue}
)
