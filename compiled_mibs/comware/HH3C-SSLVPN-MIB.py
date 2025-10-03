# SNMP MIB module (HH3C-SSLVPN-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\comware\HH3C-SSLVPN-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:33:02 2025
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

hh3cSslvpn = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 170)
)
if mibBuilder.loadTexts:
    hh3cSslvpn.setRevisions(
        ("2017-07-05 19:20",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Hh3cSslvpnMibObjects_ObjectIdentity = ObjectIdentity
hh3cSslvpnMibObjects = _Hh3cSslvpnMibObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 170, 1)
)
_Hh3cSslvpnInfomation_ObjectIdentity = ObjectIdentity
hh3cSslvpnInfomation = _Hh3cSslvpnInfomation_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 170, 1, 1)
)
_Hh3cSslvpnCtxIpacStatTable_Object = MibTable
hh3cSslvpnCtxIpacStatTable = _Hh3cSslvpnCtxIpacStatTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 170, 1, 1, 1)
)
if mibBuilder.loadTexts:
    hh3cSslvpnCtxIpacStatTable.setStatus("current")
_Hh3cSslvpnCtxIpacStatEntry_Object = MibTableRow
hh3cSslvpnCtxIpacStatEntry = _Hh3cSslvpnCtxIpacStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 170, 1, 1, 1, 1)
)
hh3cSslvpnCtxIpacStatEntry.setIndexNames(
    (0, "HH3C-SSLVPN-MIB", "hh3cSslvpnCtxName"),
)
if mibBuilder.loadTexts:
    hh3cSslvpnCtxIpacStatEntry.setStatus("current")


class _Hh3cSslvpnCtxName_Type(DisplayString):
    """Custom type hh3cSslvpnCtxName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_Hh3cSslvpnCtxName_Type.__name__ = "DisplayString"
_Hh3cSslvpnCtxName_Object = MibTableColumn
hh3cSslvpnCtxName = _Hh3cSslvpnCtxName_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 170, 1, 1, 1, 1, 1),
    _Hh3cSslvpnCtxName_Type()
)
hh3cSslvpnCtxName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cSslvpnCtxName.setStatus("current")
_Hh3cSslvpnCtxIpacClientInBytes_Type = Counter64
_Hh3cSslvpnCtxIpacClientInBytes_Object = MibTableColumn
hh3cSslvpnCtxIpacClientInBytes = _Hh3cSslvpnCtxIpacClientInBytes_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 170, 1, 1, 1, 1, 2),
    _Hh3cSslvpnCtxIpacClientInBytes_Type()
)
hh3cSslvpnCtxIpacClientInBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cSslvpnCtxIpacClientInBytes.setStatus("current")
_Hh3cSslvpnCtxIpacClientOutBytes_Type = Counter64
_Hh3cSslvpnCtxIpacClientOutBytes_Object = MibTableColumn
hh3cSslvpnCtxIpacClientOutBytes = _Hh3cSslvpnCtxIpacClientOutBytes_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 170, 1, 1, 1, 1, 3),
    _Hh3cSslvpnCtxIpacClientOutBytes_Type()
)
hh3cSslvpnCtxIpacClientOutBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cSslvpnCtxIpacClientOutBytes.setStatus("current")
_Hh3cSslvpnCtxIpacServerInBytes_Type = Counter64
_Hh3cSslvpnCtxIpacServerInBytes_Object = MibTableColumn
hh3cSslvpnCtxIpacServerInBytes = _Hh3cSslvpnCtxIpacServerInBytes_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 170, 1, 1, 1, 1, 4),
    _Hh3cSslvpnCtxIpacServerInBytes_Type()
)
hh3cSslvpnCtxIpacServerInBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cSslvpnCtxIpacServerInBytes.setStatus("current")
_Hh3cSslvpnCtxIpacServerOutBytes_Type = Counter64
_Hh3cSslvpnCtxIpacServerOutBytes_Object = MibTableColumn
hh3cSslvpnCtxIpacServerOutBytes = _Hh3cSslvpnCtxIpacServerOutBytes_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 170, 1, 1, 1, 1, 5),
    _Hh3cSslvpnCtxIpacServerOutBytes_Type()
)
hh3cSslvpnCtxIpacServerOutBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cSslvpnCtxIpacServerOutBytes.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HH3C-SSLVPN-MIB",
    **{"hh3cSslvpn": hh3cSslvpn,
       "hh3cSslvpnMibObjects": hh3cSslvpnMibObjects,
       "hh3cSslvpnInfomation": hh3cSslvpnInfomation,
       "hh3cSslvpnCtxIpacStatTable": hh3cSslvpnCtxIpacStatTable,
       "hh3cSslvpnCtxIpacStatEntry": hh3cSslvpnCtxIpacStatEntry,
       "hh3cSslvpnCtxName": hh3cSslvpnCtxName,
       "hh3cSslvpnCtxIpacClientInBytes": hh3cSslvpnCtxIpacClientInBytes,
       "hh3cSslvpnCtxIpacClientOutBytes": hh3cSslvpnCtxIpacClientOutBytes,
       "hh3cSslvpnCtxIpacServerInBytes": hh3cSslvpnCtxIpacServerInBytes,
       "hh3cSslvpnCtxIpacServerOutBytes": hh3cSslvpnCtxIpacServerOutBytes}
)
