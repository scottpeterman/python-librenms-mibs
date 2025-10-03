# SNMP MIB module (HH3C-VPN-PEER-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\comware\HH3C-VPN-PEER-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:33:23 2025
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

hh3cVpnPeer = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 165)
)
if mibBuilder.loadTexts:
    hh3cVpnPeer.setRevisions(
        ("2016-03-09 16:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Hh3cVpnPeerGroup_ObjectIdentity = ObjectIdentity
hh3cVpnPeerGroup = _Hh3cVpnPeerGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 165, 1)
)
_Hh3cVpnPeerStat_ObjectIdentity = ObjectIdentity
hh3cVpnPeerStat = _Hh3cVpnPeerStat_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 165, 1, 1)
)
_Hh3cVpnPeerStatTable_Object = MibTable
hh3cVpnPeerStatTable = _Hh3cVpnPeerStatTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 165, 1, 1, 1)
)
if mibBuilder.loadTexts:
    hh3cVpnPeerStatTable.setStatus("current")
_Hh3cVpnPeerStatEntry_Object = MibTableRow
hh3cVpnPeerStatEntry = _Hh3cVpnPeerStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 165, 1, 1, 1, 1)
)
hh3cVpnPeerStatEntry.setIndexNames(
    (0, "HH3C-VPN-PEER-MIB", "hh3cVpnPeerName"),
)
if mibBuilder.loadTexts:
    hh3cVpnPeerStatEntry.setStatus("current")


class _Hh3cVpnPeerName_Type(OctetString):
    """Custom type hh3cVpnPeerName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_Hh3cVpnPeerName_Type.__name__ = "OctetString"
_Hh3cVpnPeerName_Object = MibTableColumn
hh3cVpnPeerName = _Hh3cVpnPeerName_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 165, 1, 1, 1, 1, 1),
    _Hh3cVpnPeerName_Type()
)
hh3cVpnPeerName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cVpnPeerName.setStatus("current")
_Hh3cVpnPeerOutPassPkts_Type = Counter64
_Hh3cVpnPeerOutPassPkts_Object = MibTableColumn
hh3cVpnPeerOutPassPkts = _Hh3cVpnPeerOutPassPkts_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 165, 1, 1, 1, 1, 2),
    _Hh3cVpnPeerOutPassPkts_Type()
)
hh3cVpnPeerOutPassPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cVpnPeerOutPassPkts.setStatus("current")
_Hh3cVpnPeerOutPassBytes_Type = Counter64
_Hh3cVpnPeerOutPassBytes_Object = MibTableColumn
hh3cVpnPeerOutPassBytes = _Hh3cVpnPeerOutPassBytes_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 165, 1, 1, 1, 1, 3),
    _Hh3cVpnPeerOutPassBytes_Type()
)
hh3cVpnPeerOutPassBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cVpnPeerOutPassBytes.setStatus("current")
_Hh3cVpnPeerOutDropPkts_Type = Counter64
_Hh3cVpnPeerOutDropPkts_Object = MibTableColumn
hh3cVpnPeerOutDropPkts = _Hh3cVpnPeerOutDropPkts_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 165, 1, 1, 1, 1, 4),
    _Hh3cVpnPeerOutDropPkts_Type()
)
hh3cVpnPeerOutDropPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cVpnPeerOutDropPkts.setStatus("current")
_Hh3cVpnPeerOutDropBytes_Type = Counter64
_Hh3cVpnPeerOutDropBytes_Object = MibTableColumn
hh3cVpnPeerOutDropBytes = _Hh3cVpnPeerOutDropBytes_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 165, 1, 1, 1, 1, 5),
    _Hh3cVpnPeerOutDropBytes_Type()
)
hh3cVpnPeerOutDropBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cVpnPeerOutDropBytes.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HH3C-VPN-PEER-MIB",
    **{"hh3cVpnPeer": hh3cVpnPeer,
       "hh3cVpnPeerGroup": hh3cVpnPeerGroup,
       "hh3cVpnPeerStat": hh3cVpnPeerStat,
       "hh3cVpnPeerStatTable": hh3cVpnPeerStatTable,
       "hh3cVpnPeerStatEntry": hh3cVpnPeerStatEntry,
       "hh3cVpnPeerName": hh3cVpnPeerName,
       "hh3cVpnPeerOutPassPkts": hh3cVpnPeerOutPassPkts,
       "hh3cVpnPeerOutPassBytes": hh3cVpnPeerOutPassBytes,
       "hh3cVpnPeerOutDropPkts": hh3cVpnPeerOutDropPkts,
       "hh3cVpnPeerOutDropBytes": hh3cVpnPeerOutDropBytes}
)
