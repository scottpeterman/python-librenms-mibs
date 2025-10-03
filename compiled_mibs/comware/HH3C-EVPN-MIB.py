# SNMP MIB module (HH3C-EVPN-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\comware\HH3C-EVPN-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:31:27 2025
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

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

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

hh3cEvpn = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 173)
)
if mibBuilder.loadTexts:
    hh3cEvpn.setRevisions(
        ("2017-10-21 09:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Hh3cEvpnObjects_ObjectIdentity = ObjectIdentity
hh3cEvpnObjects = _Hh3cEvpnObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 173, 1)
)
_Hh3cEvpnESTable_Object = MibTable
hh3cEvpnESTable = _Hh3cEvpnESTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 173, 1, 1)
)
if mibBuilder.loadTexts:
    hh3cEvpnESTable.setStatus("current")
_Hh3cEvpnESEntry_Object = MibTableRow
hh3cEvpnESEntry = _Hh3cEvpnESEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 173, 1, 1, 1)
)
hh3cEvpnESEntry.setIndexNames(
    (0, "HH3C-EVPN-MIB", "hh3cEvpnESESI"),
)
if mibBuilder.loadTexts:
    hh3cEvpnESEntry.setStatus("current")


class _Hh3cEvpnESESI_Type(OctetString):
    """Custom type hh3cEvpnESESI based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 10),
    )


_Hh3cEvpnESESI_Type.__name__ = "OctetString"
_Hh3cEvpnESESI_Object = MibTableColumn
hh3cEvpnESESI = _Hh3cEvpnESESI_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 173, 1, 1, 1, 1),
    _Hh3cEvpnESESI_Type()
)
hh3cEvpnESESI.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cEvpnESESI.setStatus("current")
_Hh3cEvpnESIfIndex_Type = InterfaceIndex
_Hh3cEvpnESIfIndex_Object = MibTableColumn
hh3cEvpnESIfIndex = _Hh3cEvpnESIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 173, 1, 1, 1, 2),
    _Hh3cEvpnESIfIndex_Type()
)
hh3cEvpnESIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cEvpnESIfIndex.setStatus("current")


class _Hh3cEvpnESIfName_Type(DisplayString):
    """Custom type hh3cEvpnESIfName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_Hh3cEvpnESIfName_Type.__name__ = "DisplayString"
_Hh3cEvpnESIfName_Object = MibTableColumn
hh3cEvpnESIfName = _Hh3cEvpnESIfName_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 173, 1, 1, 1, 3),
    _Hh3cEvpnESIfName_Type()
)
hh3cEvpnESIfName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cEvpnESIfName.setStatus("current")
_Hh3cEvpnESMode_Type = Unsigned32
_Hh3cEvpnESMode_Object = MibTableColumn
hh3cEvpnESMode = _Hh3cEvpnESMode_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 173, 1, 1, 1, 4),
    _Hh3cEvpnESMode_Type()
)
hh3cEvpnESMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cEvpnESMode.setStatus("current")
_Hh3cEvpnESMemberTable_Object = MibTable
hh3cEvpnESMemberTable = _Hh3cEvpnESMemberTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 173, 1, 2)
)
if mibBuilder.loadTexts:
    hh3cEvpnESMemberTable.setStatus("current")
_Hh3cEvpnESMemberEntry_Object = MibTableRow
hh3cEvpnESMemberEntry = _Hh3cEvpnESMemberEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 173, 1, 2, 1)
)
hh3cEvpnESMemberEntry.setIndexNames(
    (0, "HH3C-EVPN-MIB", "hh3cEvpnESESI"),
    (0, "HH3C-EVPN-MIB", "hh3cEvpnESMemberIPType"),
    (0, "HH3C-EVPN-MIB", "hh3cEvpnESMemberIP"),
)
if mibBuilder.loadTexts:
    hh3cEvpnESMemberEntry.setStatus("current")
_Hh3cEvpnESMemberIPType_Type = InetAddressType
_Hh3cEvpnESMemberIPType_Object = MibTableColumn
hh3cEvpnESMemberIPType = _Hh3cEvpnESMemberIPType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 173, 1, 2, 1, 1),
    _Hh3cEvpnESMemberIPType_Type()
)
hh3cEvpnESMemberIPType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cEvpnESMemberIPType.setStatus("current")
_Hh3cEvpnESMemberIP_Type = InetAddress
_Hh3cEvpnESMemberIP_Object = MibTableColumn
hh3cEvpnESMemberIP = _Hh3cEvpnESMemberIP_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 173, 1, 2, 1, 2),
    _Hh3cEvpnESMemberIP_Type()
)
hh3cEvpnESMemberIP.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cEvpnESMemberIP.setStatus("current")
_Hh3cEvpnESMemberIsSelf_Type = TruthValue
_Hh3cEvpnESMemberIsSelf_Object = MibTableColumn
hh3cEvpnESMemberIsSelf = _Hh3cEvpnESMemberIsSelf_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 173, 1, 2, 1, 3),
    _Hh3cEvpnESMemberIsSelf_Type()
)
hh3cEvpnESMemberIsSelf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cEvpnESMemberIsSelf.setStatus("current")
_Hh3cEvpnESDFTable_Object = MibTable
hh3cEvpnESDFTable = _Hh3cEvpnESDFTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 173, 1, 3)
)
if mibBuilder.loadTexts:
    hh3cEvpnESDFTable.setStatus("current")
_Hh3cEvpnESDFEntry_Object = MibTableRow
hh3cEvpnESDFEntry = _Hh3cEvpnESDFEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 173, 1, 3, 1)
)
hh3cEvpnESDFEntry.setIndexNames(
    (0, "HH3C-EVPN-MIB", "hh3cEvpnESESI"),
    (0, "HH3C-EVPN-MIB", "hh3cEvpnESDFVLANID"),
)
if mibBuilder.loadTexts:
    hh3cEvpnESDFEntry.setStatus("current")
_Hh3cEvpnESDFVLANID_Type = Unsigned32
_Hh3cEvpnESDFVLANID_Object = MibTableColumn
hh3cEvpnESDFVLANID = _Hh3cEvpnESDFVLANID_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 173, 1, 3, 1, 1),
    _Hh3cEvpnESDFVLANID_Type()
)
hh3cEvpnESDFVLANID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cEvpnESDFVLANID.setStatus("current")
_Hh3cEvpnESDFAcIfIndex_Type = InterfaceIndex
_Hh3cEvpnESDFAcIfIndex_Object = MibTableColumn
hh3cEvpnESDFAcIfIndex = _Hh3cEvpnESDFAcIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 173, 1, 3, 1, 2),
    _Hh3cEvpnESDFAcIfIndex_Type()
)
hh3cEvpnESDFAcIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cEvpnESDFAcIfIndex.setStatus("current")
_Hh3cEvpnESDFACEvcSrvInstId_Type = Unsigned32
_Hh3cEvpnESDFACEvcSrvInstId_Object = MibTableColumn
hh3cEvpnESDFACEvcSrvInstId = _Hh3cEvpnESDFACEvcSrvInstId_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 173, 1, 3, 1, 3),
    _Hh3cEvpnESDFACEvcSrvInstId_Type()
)
hh3cEvpnESDFACEvcSrvInstId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cEvpnESDFACEvcSrvInstId.setStatus("current")
_Hh3cEvpnESDFMode_Type = Unsigned32
_Hh3cEvpnESDFMode_Object = MibTableColumn
hh3cEvpnESDFMode = _Hh3cEvpnESDFMode_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 173, 1, 3, 1, 4),
    _Hh3cEvpnESDFMode_Type()
)
hh3cEvpnESDFMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cEvpnESDFMode.setStatus("current")
_Hh3cEvpnESDFRouterIPType_Type = InetAddressType
_Hh3cEvpnESDFRouterIPType_Object = MibTableColumn
hh3cEvpnESDFRouterIPType = _Hh3cEvpnESDFRouterIPType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 173, 1, 3, 1, 5),
    _Hh3cEvpnESDFRouterIPType_Type()
)
hh3cEvpnESDFRouterIPType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cEvpnESDFRouterIPType.setStatus("current")
_Hh3cEvpnESDFRouterIP_Type = InetAddress
_Hh3cEvpnESDFRouterIP_Object = MibTableColumn
hh3cEvpnESDFRouterIP = _Hh3cEvpnESDFRouterIP_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 173, 1, 3, 1, 6),
    _Hh3cEvpnESDFRouterIP_Type()
)
hh3cEvpnESDFRouterIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cEvpnESDFRouterIP.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HH3C-EVPN-MIB",
    **{"hh3cEvpn": hh3cEvpn,
       "hh3cEvpnObjects": hh3cEvpnObjects,
       "hh3cEvpnESTable": hh3cEvpnESTable,
       "hh3cEvpnESEntry": hh3cEvpnESEntry,
       "hh3cEvpnESESI": hh3cEvpnESESI,
       "hh3cEvpnESIfIndex": hh3cEvpnESIfIndex,
       "hh3cEvpnESIfName": hh3cEvpnESIfName,
       "hh3cEvpnESMode": hh3cEvpnESMode,
       "hh3cEvpnESMemberTable": hh3cEvpnESMemberTable,
       "hh3cEvpnESMemberEntry": hh3cEvpnESMemberEntry,
       "hh3cEvpnESMemberIPType": hh3cEvpnESMemberIPType,
       "hh3cEvpnESMemberIP": hh3cEvpnESMemberIP,
       "hh3cEvpnESMemberIsSelf": hh3cEvpnESMemberIsSelf,
       "hh3cEvpnESDFTable": hh3cEvpnESDFTable,
       "hh3cEvpnESDFEntry": hh3cEvpnESDFEntry,
       "hh3cEvpnESDFVLANID": hh3cEvpnESDFVLANID,
       "hh3cEvpnESDFAcIfIndex": hh3cEvpnESDFAcIfIndex,
       "hh3cEvpnESDFACEvcSrvInstId": hh3cEvpnESDFACEvcSrvInstId,
       "hh3cEvpnESDFMode": hh3cEvpnESDFMode,
       "hh3cEvpnESDFRouterIPType": hh3cEvpnESDFRouterIPType,
       "hh3cEvpnESDFRouterIP": hh3cEvpnESDFRouterIP}
)
