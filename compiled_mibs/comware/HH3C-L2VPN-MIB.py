# SNMP MIB module (HH3C-L2VPN-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\comware\HH3C-L2VPN-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:31:58 2025
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

(InterfaceIndex,
 InterfaceIndexOrZero) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
    "InterfaceIndexOrZero")

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
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

hh3cL2vpn = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 162)
)
if mibBuilder.loadTexts:
    hh3cL2vpn.setRevisions(
        ("2018-04-27 18:00",
         "2018-01-17 15:00",
         "2017-11-21 15:00",
         "2016-09-30 18:00",
         "2015-01-16 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Hh3cL2vpnPwNotifications_ObjectIdentity = ObjectIdentity
hh3cL2vpnPwNotifications = _Hh3cL2vpnPwNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 162, 0)
)
_Hh3cL2vpnGlobalTable_ObjectIdentity = ObjectIdentity
hh3cL2vpnGlobalTable = _Hh3cL2vpnGlobalTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 162, 2)
)
_Hh3cL2vpnPwcTable_Object = MibTable
hh3cL2vpnPwcTable = _Hh3cL2vpnPwcTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 162, 2, 1)
)
if mibBuilder.loadTexts:
    hh3cL2vpnPwcTable.setStatus("current")
_Hh3cL2vpnPwcEntry_Object = MibTableRow
hh3cL2vpnPwcEntry = _Hh3cL2vpnPwcEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 162, 2, 1, 1)
)
hh3cL2vpnPwcEntry.setIndexNames(
    (0, "HH3C-L2VPN-MIB", "hh3cL2vpnPwcName"),
)
if mibBuilder.loadTexts:
    hh3cL2vpnPwcEntry.setStatus("current")


class _Hh3cL2vpnPwcName_Type(OctetString):
    """Custom type hh3cL2vpnPwcName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 19),
    )


_Hh3cL2vpnPwcName_Type.__name__ = "OctetString"
_Hh3cL2vpnPwcName_Object = MibTableColumn
hh3cL2vpnPwcName = _Hh3cL2vpnPwcName_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 162, 2, 1, 1, 1),
    _Hh3cL2vpnPwcName_Type()
)
hh3cL2vpnPwcName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cL2vpnPwcName.setStatus("current")


class _Hh3cL2vpnPwcCvType_Type(Integer32):
    """Custom type hh3cL2vpnPwcCvType based on Integer32"""
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
          ("bfd", 2),
          ("rawBFD", 3))
    )


_Hh3cL2vpnPwcCvType_Type.__name__ = "Integer32"
_Hh3cL2vpnPwcCvType_Object = MibTableColumn
hh3cL2vpnPwcCvType = _Hh3cL2vpnPwcCvType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 162, 2, 1, 1, 2),
    _Hh3cL2vpnPwcCvType_Type()
)
hh3cL2vpnPwcCvType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cL2vpnPwcCvType.setStatus("current")


class _Hh3cL2vpnPwcCcType_Type(Integer32):
    """Custom type hh3cL2vpnPwcCcType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 1),
          ("controlWord", 2),
          ("routerAlert", 3),
          ("ttl", 4))
    )


_Hh3cL2vpnPwcCcType_Type.__name__ = "Integer32"
_Hh3cL2vpnPwcCcType_Object = MibTableColumn
hh3cL2vpnPwcCcType = _Hh3cL2vpnPwcCcType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 162, 2, 1, 1, 3),
    _Hh3cL2vpnPwcCcType_Type()
)
hh3cL2vpnPwcCcType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cL2vpnPwcCcType.setStatus("current")


class _Hh3cL2vpnPwcControlWord_Type(TruthValue):
    """Custom type hh3cL2vpnPwcControlWord based on TruthValue"""
    defaultValue = 2


_Hh3cL2vpnPwcControlWord_Type.__name__ = "TruthValue"
_Hh3cL2vpnPwcControlWord_Object = MibTableColumn
hh3cL2vpnPwcControlWord = _Hh3cL2vpnPwcControlWord_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 162, 2, 1, 1, 4),
    _Hh3cL2vpnPwcControlWord_Type()
)
hh3cL2vpnPwcControlWord.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cL2vpnPwcControlWord.setStatus("current")


class _Hh3cL2vpnPwcPwType_Type(Integer32):
    """Custom type hh3cL2vpnPwcPwType based on Integer32"""
    defaultValue = 4

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("vlan", 4),
          ("ethernet", 5))
    )


_Hh3cL2vpnPwcPwType_Type.__name__ = "Integer32"
_Hh3cL2vpnPwcPwType_Object = MibTableColumn
hh3cL2vpnPwcPwType = _Hh3cL2vpnPwcPwType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 162, 2, 1, 1, 5),
    _Hh3cL2vpnPwcPwType_Type()
)
hh3cL2vpnPwcPwType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cL2vpnPwcPwType.setStatus("current")
_Hh3cL2vpnPwcRowStatus_Type = RowStatus
_Hh3cL2vpnPwcRowStatus_Object = MibTableColumn
hh3cL2vpnPwcRowStatus = _Hh3cL2vpnPwcRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 162, 2, 1, 1, 6),
    _Hh3cL2vpnPwcRowStatus_Type()
)
hh3cL2vpnPwcRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cL2vpnPwcRowStatus.setStatus("current")


class _Hh3cL2vpnPwcFlowLabel_Type(Integer32):
    """Custom type hh3cL2vpnPwcFlowLabel based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 1),
          ("send", 2),
          ("receive", 3),
          ("both", 4))
    )


_Hh3cL2vpnPwcFlowLabel_Type.__name__ = "Integer32"
_Hh3cL2vpnPwcFlowLabel_Object = MibTableColumn
hh3cL2vpnPwcFlowLabel = _Hh3cL2vpnPwcFlowLabel_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 162, 2, 1, 1, 7),
    _Hh3cL2vpnPwcFlowLabel_Type()
)
hh3cL2vpnPwcFlowLabel.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cL2vpnPwcFlowLabel.setStatus("current")
_Hh3cL2vpnLinkTable_Object = MibTable
hh3cL2vpnLinkTable = _Hh3cL2vpnLinkTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 162, 2, 2)
)
if mibBuilder.loadTexts:
    hh3cL2vpnLinkTable.setStatus("current")
_Hh3cL2vpnLinkEntry_Object = MibTableRow
hh3cL2vpnLinkEntry = _Hh3cL2vpnLinkEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 162, 2, 2, 1)
)
hh3cL2vpnLinkEntry.setIndexNames(
    (0, "HH3C-L2VPN-MIB", "hh3cL2vpnLinkVsiIndex"),
    (0, "HH3C-L2VPN-MIB", "hh3cL2vpnLinkLinkID"),
)
if mibBuilder.loadTexts:
    hh3cL2vpnLinkEntry.setStatus("current")
_Hh3cL2vpnLinkVsiIndex_Type = Unsigned32
_Hh3cL2vpnLinkVsiIndex_Object = MibTableColumn
hh3cL2vpnLinkVsiIndex = _Hh3cL2vpnLinkVsiIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 162, 2, 2, 1, 1),
    _Hh3cL2vpnLinkVsiIndex_Type()
)
hh3cL2vpnLinkVsiIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cL2vpnLinkVsiIndex.setStatus("current")
_Hh3cL2vpnLinkLinkID_Type = Unsigned32
_Hh3cL2vpnLinkLinkID_Object = MibTableColumn
hh3cL2vpnLinkLinkID = _Hh3cL2vpnLinkLinkID_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 162, 2, 2, 1, 2),
    _Hh3cL2vpnLinkLinkID_Type()
)
hh3cL2vpnLinkLinkID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cL2vpnLinkLinkID.setStatus("current")


class _Hh3cL2vpnLinkType_Type(Integer32):
    """Custom type hh3cL2vpnLinkType based on Integer32"""
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
          ("ac", 2),
          ("tunnel", 3))
    )


_Hh3cL2vpnLinkType_Type.__name__ = "Integer32"
_Hh3cL2vpnLinkType_Object = MibTableColumn
hh3cL2vpnLinkType = _Hh3cL2vpnLinkType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 162, 2, 2, 1, 3),
    _Hh3cL2vpnLinkType_Type()
)
hh3cL2vpnLinkType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cL2vpnLinkType.setStatus("current")
_Hh3cL2vpnLinkIfIndex_Type = InterfaceIndexOrZero
_Hh3cL2vpnLinkIfIndex_Object = MibTableColumn
hh3cL2vpnLinkIfIndex = _Hh3cL2vpnLinkIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 162, 2, 2, 1, 4),
    _Hh3cL2vpnLinkIfIndex_Type()
)
hh3cL2vpnLinkIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cL2vpnLinkIfIndex.setStatus("current")
_Hh3cL2vpnLinkSrvID_Type = Unsigned32
_Hh3cL2vpnLinkSrvID_Object = MibTableColumn
hh3cL2vpnLinkSrvID = _Hh3cL2vpnLinkSrvID_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 162, 2, 2, 1, 5),
    _Hh3cL2vpnLinkSrvID_Type()
)
hh3cL2vpnLinkSrvID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cL2vpnLinkSrvID.setStatus("current")
_Hh3cL2vpnLinkTunnelID_Type = Unsigned32
_Hh3cL2vpnLinkTunnelID_Object = MibTableColumn
hh3cL2vpnLinkTunnelID = _Hh3cL2vpnLinkTunnelID_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 162, 2, 2, 1, 6),
    _Hh3cL2vpnLinkTunnelID_Type()
)
hh3cL2vpnLinkTunnelID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cL2vpnLinkTunnelID.setStatus("current")
_Hh3cL2vpnVpwsTable_ObjectIdentity = ObjectIdentity
hh3cL2vpnVpwsTable = _Hh3cL2vpnVpwsTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 162, 3)
)
_Hh3cL2vpnXcgTable_Object = MibTable
hh3cL2vpnXcgTable = _Hh3cL2vpnXcgTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 162, 3, 1)
)
if mibBuilder.loadTexts:
    hh3cL2vpnXcgTable.setStatus("current")
_Hh3cL2vpnXcgEntry_Object = MibTableRow
hh3cL2vpnXcgEntry = _Hh3cL2vpnXcgEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 162, 3, 1, 1)
)
hh3cL2vpnXcgEntry.setIndexNames(
    (0, "HH3C-L2VPN-MIB", "hh3cL2vpnXcgName"),
)
if mibBuilder.loadTexts:
    hh3cL2vpnXcgEntry.setStatus("current")


class _Hh3cL2vpnXcgName_Type(OctetString):
    """Custom type hh3cL2vpnXcgName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_Hh3cL2vpnXcgName_Type.__name__ = "OctetString"
_Hh3cL2vpnXcgName_Object = MibTableColumn
hh3cL2vpnXcgName = _Hh3cL2vpnXcgName_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 162, 3, 1, 1, 1),
    _Hh3cL2vpnXcgName_Type()
)
hh3cL2vpnXcgName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cL2vpnXcgName.setStatus("current")


class _Hh3cL2vpnXcgAdminState_Type(Integer32):
    """Custom type hh3cL2vpnXcgAdminState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("adminUp", 1),
          ("adminDown", 2))
    )


_Hh3cL2vpnXcgAdminState_Type.__name__ = "Integer32"
_Hh3cL2vpnXcgAdminState_Object = MibTableColumn
hh3cL2vpnXcgAdminState = _Hh3cL2vpnXcgAdminState_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 162, 3, 1, 1, 2),
    _Hh3cL2vpnXcgAdminState_Type()
)
hh3cL2vpnXcgAdminState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cL2vpnXcgAdminState.setStatus("current")
_Hh3cL2vpnXcgRowStatus_Type = RowStatus
_Hh3cL2vpnXcgRowStatus_Object = MibTableColumn
hh3cL2vpnXcgRowStatus = _Hh3cL2vpnXcgRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 162, 3, 1, 1, 3),
    _Hh3cL2vpnXcgRowStatus_Type()
)
hh3cL2vpnXcgRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cL2vpnXcgRowStatus.setStatus("current")
_Hh3cL2vpnXcgConnTable_Object = MibTable
hh3cL2vpnXcgConnTable = _Hh3cL2vpnXcgConnTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 162, 3, 2)
)
if mibBuilder.loadTexts:
    hh3cL2vpnXcgConnTable.setStatus("current")
_Hh3cL2vpnXcgConnEntry_Object = MibTableRow
hh3cL2vpnXcgConnEntry = _Hh3cL2vpnXcgConnEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 162, 3, 2, 1)
)
hh3cL2vpnXcgConnEntry.setIndexNames(
    (0, "HH3C-L2VPN-MIB", "hh3cL2vpnXcgName"),
    (0, "HH3C-L2VPN-MIB", "hh3cL2vpnXcgConnName"),
)
if mibBuilder.loadTexts:
    hh3cL2vpnXcgConnEntry.setStatus("current")


class _Hh3cL2vpnXcgConnName_Type(OctetString):
    """Custom type hh3cL2vpnXcgConnName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 20),
    )


_Hh3cL2vpnXcgConnName_Type.__name__ = "OctetString"
_Hh3cL2vpnXcgConnName_Object = MibTableColumn
hh3cL2vpnXcgConnName = _Hh3cL2vpnXcgConnName_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 162, 3, 2, 1, 1),
    _Hh3cL2vpnXcgConnName_Type()
)
hh3cL2vpnXcgConnName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cL2vpnXcgConnName.setStatus("current")
_Hh3cL2vpnXcgConnRowStatus_Type = RowStatus
_Hh3cL2vpnXcgConnRowStatus_Object = MibTableColumn
hh3cL2vpnXcgConnRowStatus = _Hh3cL2vpnXcgConnRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 162, 3, 2, 1, 2),
    _Hh3cL2vpnXcgConnRowStatus_Type()
)
hh3cL2vpnXcgConnRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cL2vpnXcgConnRowStatus.setStatus("current")


class _Hh3cL2vpnXcgConnRedundancy_Type(Integer32):
    """Custom type hh3cL2vpnXcgConnRedundancy based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("slave", 1),
          ("master", 2),
          ("independent", 3))
    )


_Hh3cL2vpnXcgConnRedundancy_Type.__name__ = "Integer32"
_Hh3cL2vpnXcgConnRedundancy_Object = MibTableColumn
hh3cL2vpnXcgConnRedundancy = _Hh3cL2vpnXcgConnRedundancy_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 162, 3, 2, 1, 3),
    _Hh3cL2vpnXcgConnRedundancy_Type()
)
hh3cL2vpnXcgConnRedundancy.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cL2vpnXcgConnRedundancy.setStatus("current")
_Hh3cL2vpnXcgAcTable_Object = MibTable
hh3cL2vpnXcgAcTable = _Hh3cL2vpnXcgAcTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 162, 3, 3)
)
if mibBuilder.loadTexts:
    hh3cL2vpnXcgAcTable.setStatus("current")
_Hh3cL2vpnXcgAcEntry_Object = MibTableRow
hh3cL2vpnXcgAcEntry = _Hh3cL2vpnXcgAcEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 162, 3, 3, 1)
)
hh3cL2vpnXcgAcEntry.setIndexNames(
    (0, "HH3C-L2VPN-MIB", "hh3cL2vpnXcgName"),
    (0, "HH3C-L2VPN-MIB", "hh3cL2vpnXcgConnName"),
    (0, "HH3C-L2VPN-MIB", "hh3cL2vpnXcgAcIfIndex"),
    (0, "HH3C-L2VPN-MIB", "hh3cL2vpnXcgAcEvcSrvInstId"),
)
if mibBuilder.loadTexts:
    hh3cL2vpnXcgAcEntry.setStatus("current")
_Hh3cL2vpnXcgAcIfIndex_Type = InterfaceIndex
_Hh3cL2vpnXcgAcIfIndex_Object = MibTableColumn
hh3cL2vpnXcgAcIfIndex = _Hh3cL2vpnXcgAcIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 162, 3, 3, 1, 1),
    _Hh3cL2vpnXcgAcIfIndex_Type()
)
hh3cL2vpnXcgAcIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cL2vpnXcgAcIfIndex.setStatus("current")
_Hh3cL2vpnXcgAcEvcSrvInstId_Type = Unsigned32
_Hh3cL2vpnXcgAcEvcSrvInstId_Object = MibTableColumn
hh3cL2vpnXcgAcEvcSrvInstId = _Hh3cL2vpnXcgAcEvcSrvInstId_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 162, 3, 3, 1, 2),
    _Hh3cL2vpnXcgAcEvcSrvInstId_Type()
)
hh3cL2vpnXcgAcEvcSrvInstId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cL2vpnXcgAcEvcSrvInstId.setStatus("current")


class _Hh3cL2vpnXcgAcAccessMode_Type(Integer32):
    """Custom type hh3cL2vpnXcgAcAccessMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("vlan", 1),
          ("ethernet", 2))
    )


_Hh3cL2vpnXcgAcAccessMode_Type.__name__ = "Integer32"
_Hh3cL2vpnXcgAcAccessMode_Object = MibTableColumn
hh3cL2vpnXcgAcAccessMode = _Hh3cL2vpnXcgAcAccessMode_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 162, 3, 3, 1, 3),
    _Hh3cL2vpnXcgAcAccessMode_Type()
)
hh3cL2vpnXcgAcAccessMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cL2vpnXcgAcAccessMode.setStatus("current")
_Hh3cL2vpnXcgAcRowStatus_Type = RowStatus
_Hh3cL2vpnXcgAcRowStatus_Object = MibTableColumn
hh3cL2vpnXcgAcRowStatus = _Hh3cL2vpnXcgAcRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 162, 3, 3, 1, 4),
    _Hh3cL2vpnXcgAcRowStatus_Type()
)
hh3cL2vpnXcgAcRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cL2vpnXcgAcRowStatus.setStatus("current")
_Hh3cL2vpnXcgPwTable_Object = MibTable
hh3cL2vpnXcgPwTable = _Hh3cL2vpnXcgPwTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 162, 3, 4)
)
if mibBuilder.loadTexts:
    hh3cL2vpnXcgPwTable.setStatus("current")
_Hh3cL2vpnXcgPwEntry_Object = MibTableRow
hh3cL2vpnXcgPwEntry = _Hh3cL2vpnXcgPwEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 162, 3, 4, 1)
)
hh3cL2vpnXcgPwEntry.setIndexNames(
    (0, "HH3C-L2VPN-MIB", "hh3cL2vpnXcgName"),
    (0, "HH3C-L2VPN-MIB", "hh3cL2vpnXcgConnName"),
    (0, "HH3C-L2VPN-MIB", "hh3cL2vpnXcgPwIndex"),
)
if mibBuilder.loadTexts:
    hh3cL2vpnXcgPwEntry.setStatus("current")
_Hh3cL2vpnXcgPwIndex_Type = Unsigned32
_Hh3cL2vpnXcgPwIndex_Object = MibTableColumn
hh3cL2vpnXcgPwIndex = _Hh3cL2vpnXcgPwIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 162, 3, 4, 1, 1),
    _Hh3cL2vpnXcgPwIndex_Type()
)
hh3cL2vpnXcgPwIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cL2vpnXcgPwIndex.setStatus("current")


class _Hh3cL2vpnXcgPwCfgType_Type(Integer32):
    """Custom type hh3cL2vpnXcgPwCfgType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("primary", 1),
          ("backup", 2))
    )


_Hh3cL2vpnXcgPwCfgType_Type.__name__ = "Integer32"
_Hh3cL2vpnXcgPwCfgType_Object = MibTableColumn
hh3cL2vpnXcgPwCfgType = _Hh3cL2vpnXcgPwCfgType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 162, 3, 4, 1, 2),
    _Hh3cL2vpnXcgPwCfgType_Type()
)
hh3cL2vpnXcgPwCfgType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cL2vpnXcgPwCfgType.setStatus("current")


class _Hh3cL2vpnXcgPwClassName_Type(OctetString):
    """Custom type hh3cL2vpnXcgPwClassName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 19),
    )


_Hh3cL2vpnXcgPwClassName_Type.__name__ = "OctetString"
_Hh3cL2vpnXcgPwClassName_Object = MibTableColumn
hh3cL2vpnXcgPwClassName = _Hh3cL2vpnXcgPwClassName_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 162, 3, 4, 1, 3),
    _Hh3cL2vpnXcgPwClassName_Type()
)
hh3cL2vpnXcgPwClassName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cL2vpnXcgPwClassName.setStatus("current")


class _Hh3cL2vpnXcgPwTunnelPolicy_Type(OctetString):
    """Custom type hh3cL2vpnXcgPwTunnelPolicy based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 19),
    )


_Hh3cL2vpnXcgPwTunnelPolicy_Type.__name__ = "OctetString"
_Hh3cL2vpnXcgPwTunnelPolicy_Object = MibTableColumn
hh3cL2vpnXcgPwTunnelPolicy = _Hh3cL2vpnXcgPwTunnelPolicy_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 162, 3, 4, 1, 4),
    _Hh3cL2vpnXcgPwTunnelPolicy_Type()
)
hh3cL2vpnXcgPwTunnelPolicy.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cL2vpnXcgPwTunnelPolicy.setStatus("current")
_Hh3cL2vpnXcgPwPeerIp_Type = IpAddress
_Hh3cL2vpnXcgPwPeerIp_Object = MibTableColumn
hh3cL2vpnXcgPwPeerIp = _Hh3cL2vpnXcgPwPeerIp_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 162, 3, 4, 1, 5),
    _Hh3cL2vpnXcgPwPeerIp_Type()
)
hh3cL2vpnXcgPwPeerIp.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cL2vpnXcgPwPeerIp.setStatus("current")
_Hh3cL2vpnXcgPwPwID_Type = Unsigned32
_Hh3cL2vpnXcgPwPwID_Object = MibTableColumn
hh3cL2vpnXcgPwPwID = _Hh3cL2vpnXcgPwPwID_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 162, 3, 4, 1, 6),
    _Hh3cL2vpnXcgPwPwID_Type()
)
hh3cL2vpnXcgPwPwID.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cL2vpnXcgPwPwID.setStatus("current")
_Hh3cL2vpnXcgPwRowStatus_Type = RowStatus
_Hh3cL2vpnXcgPwRowStatus_Object = MibTableColumn
hh3cL2vpnXcgPwRowStatus = _Hh3cL2vpnXcgPwRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 162, 3, 4, 1, 7),
    _Hh3cL2vpnXcgPwRowStatus_Type()
)
hh3cL2vpnXcgPwRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cL2vpnXcgPwRowStatus.setStatus("current")


class _Hh3cL2vpnXcgPwIgnoreStandby_Type(TruthValue):
    """Custom type hh3cL2vpnXcgPwIgnoreStandby based on TruthValue"""
    defaultValue = 2


_Hh3cL2vpnXcgPwIgnoreStandby_Type.__name__ = "TruthValue"
_Hh3cL2vpnXcgPwIgnoreStandby_Object = MibTableColumn
hh3cL2vpnXcgPwIgnoreStandby = _Hh3cL2vpnXcgPwIgnoreStandby_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 162, 3, 4, 1, 8),
    _Hh3cL2vpnXcgPwIgnoreStandby_Type()
)
hh3cL2vpnXcgPwIgnoreStandby.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cL2vpnXcgPwIgnoreStandby.setStatus("current")
_Hh3cL2vpnAcTable_ObjectIdentity = ObjectIdentity
hh3cL2vpnAcTable = _Hh3cL2vpnAcTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 162, 4)
)
_Hh3cL2vpnAcCfgTable_Object = MibTable
hh3cL2vpnAcCfgTable = _Hh3cL2vpnAcCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 162, 4, 1)
)
if mibBuilder.loadTexts:
    hh3cL2vpnAcCfgTable.setStatus("current")
_Hh3cL2vpnAcCfgEntry_Object = MibTableRow
hh3cL2vpnAcCfgEntry = _Hh3cL2vpnAcCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 162, 4, 1, 1)
)
hh3cL2vpnAcCfgEntry.setIndexNames(
    (0, "HH3C-L2VPN-MIB", "hh3cL2vpnAcIfIndex"),
    (0, "HH3C-L2VPN-MIB", "hh3cL2vpnAcSrvId"),
)
if mibBuilder.loadTexts:
    hh3cL2vpnAcCfgEntry.setStatus("current")
_Hh3cL2vpnAcIfIndex_Type = InterfaceIndex
_Hh3cL2vpnAcIfIndex_Object = MibTableColumn
hh3cL2vpnAcIfIndex = _Hh3cL2vpnAcIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 162, 4, 1, 1, 1),
    _Hh3cL2vpnAcIfIndex_Type()
)
hh3cL2vpnAcIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cL2vpnAcIfIndex.setStatus("current")
_Hh3cL2vpnAcSrvId_Type = Unsigned32
_Hh3cL2vpnAcSrvId_Object = MibTableColumn
hh3cL2vpnAcSrvId = _Hh3cL2vpnAcSrvId_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 162, 4, 1, 1, 2),
    _Hh3cL2vpnAcSrvId_Type()
)
hh3cL2vpnAcSrvId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cL2vpnAcSrvId.setStatus("current")


class _Hh3cL2vpnAcIfName_Type(DisplayString):
    """Custom type hh3cL2vpnAcIfName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_Hh3cL2vpnAcIfName_Type.__name__ = "DisplayString"
_Hh3cL2vpnAcIfName_Object = MibTableColumn
hh3cL2vpnAcIfName = _Hh3cL2vpnAcIfName_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 162, 4, 1, 1, 3),
    _Hh3cL2vpnAcIfName_Type()
)
hh3cL2vpnAcIfName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cL2vpnAcIfName.setStatus("current")


class _Hh3cL2vpnAcVsiName_Type(DisplayString):
    """Custom type hh3cL2vpnAcVsiName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_Hh3cL2vpnAcVsiName_Type.__name__ = "DisplayString"
_Hh3cL2vpnAcVsiName_Object = MibTableColumn
hh3cL2vpnAcVsiName = _Hh3cL2vpnAcVsiName_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 162, 4, 1, 1, 4),
    _Hh3cL2vpnAcVsiName_Type()
)
hh3cL2vpnAcVsiName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cL2vpnAcVsiName.setStatus("current")


class _Hh3cL2vpnAcXcgName_Type(DisplayString):
    """Custom type hh3cL2vpnAcXcgName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_Hh3cL2vpnAcXcgName_Type.__name__ = "DisplayString"
_Hh3cL2vpnAcXcgName_Object = MibTableColumn
hh3cL2vpnAcXcgName = _Hh3cL2vpnAcXcgName_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 162, 4, 1, 1, 5),
    _Hh3cL2vpnAcXcgName_Type()
)
hh3cL2vpnAcXcgName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cL2vpnAcXcgName.setStatus("current")


class _Hh3cL2vpnAcXcgConnName_Type(DisplayString):
    """Custom type hh3cL2vpnAcXcgConnName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_Hh3cL2vpnAcXcgConnName_Type.__name__ = "DisplayString"
_Hh3cL2vpnAcXcgConnName_Object = MibTableColumn
hh3cL2vpnAcXcgConnName = _Hh3cL2vpnAcXcgConnName_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 162, 4, 1, 1, 6),
    _Hh3cL2vpnAcXcgConnName_Type()
)
hh3cL2vpnAcXcgConnName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cL2vpnAcXcgConnName.setStatus("current")


class _Hh3cL2vpnAcDot1qType_Type(Integer32):
    """Custom type hh3cL2vpnAcDot1qType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("default", 2),
          ("singletag", 3))
    )


_Hh3cL2vpnAcDot1qType_Type.__name__ = "Integer32"
_Hh3cL2vpnAcDot1qType_Object = MibTableColumn
hh3cL2vpnAcDot1qType = _Hh3cL2vpnAcDot1qType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 162, 4, 1, 1, 7),
    _Hh3cL2vpnAcDot1qType_Type()
)
hh3cL2vpnAcDot1qType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cL2vpnAcDot1qType.setStatus("current")
_Hh3cL2vpnAcVLANID_Type = Unsigned32
_Hh3cL2vpnAcVLANID_Object = MibTableColumn
hh3cL2vpnAcVLANID = _Hh3cL2vpnAcVLANID_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 162, 4, 1, 1, 8),
    _Hh3cL2vpnAcVLANID_Type()
)
hh3cL2vpnAcVLANID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cL2vpnAcVLANID.setStatus("current")
_Hh3cL2vpnPwTable_ObjectIdentity = ObjectIdentity
hh3cL2vpnPwTable = _Hh3cL2vpnPwTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 162, 5)
)
_Hh3cL2vpnPwCfgTable_Object = MibTable
hh3cL2vpnPwCfgTable = _Hh3cL2vpnPwCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 162, 5, 1)
)
if mibBuilder.loadTexts:
    hh3cL2vpnPwCfgTable.setStatus("current")
_Hh3cL2vpnPwCfgEntry_Object = MibTableRow
hh3cL2vpnPwCfgEntry = _Hh3cL2vpnPwCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 162, 5, 1, 1)
)
hh3cL2vpnPwCfgEntry.setIndexNames(
    (0, "HH3C-L2VPN-MIB", "hh3cL2vpnPwPeerIp"),
    (0, "HH3C-L2VPN-MIB", "hh3cL2vpnPwId"),
)
if mibBuilder.loadTexts:
    hh3cL2vpnPwCfgEntry.setStatus("current")
_Hh3cL2vpnPwPeerIp_Type = IpAddress
_Hh3cL2vpnPwPeerIp_Object = MibTableColumn
hh3cL2vpnPwPeerIp = _Hh3cL2vpnPwPeerIp_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 162, 5, 1, 1, 1),
    _Hh3cL2vpnPwPeerIp_Type()
)
hh3cL2vpnPwPeerIp.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cL2vpnPwPeerIp.setStatus("current")
_Hh3cL2vpnPwId_Type = Unsigned32
_Hh3cL2vpnPwId_Object = MibTableColumn
hh3cL2vpnPwId = _Hh3cL2vpnPwId_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 162, 5, 1, 1, 2),
    _Hh3cL2vpnPwId_Type()
)
hh3cL2vpnPwId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cL2vpnPwId.setStatus("current")
_Hh3cL2vpnPwAcIfIndex_Type = InterfaceIndexOrZero
_Hh3cL2vpnPwAcIfIndex_Object = MibTableColumn
hh3cL2vpnPwAcIfIndex = _Hh3cL2vpnPwAcIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 162, 5, 1, 1, 3),
    _Hh3cL2vpnPwAcIfIndex_Type()
)
hh3cL2vpnPwAcIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cL2vpnPwAcIfIndex.setStatus("current")


class _Hh3cL2vpnPwAcIfName_Type(DisplayString):
    """Custom type hh3cL2vpnPwAcIfName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_Hh3cL2vpnPwAcIfName_Type.__name__ = "DisplayString"
_Hh3cL2vpnPwAcIfName_Object = MibTableColumn
hh3cL2vpnPwAcIfName = _Hh3cL2vpnPwAcIfName_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 162, 5, 1, 1, 4),
    _Hh3cL2vpnPwAcIfName_Type()
)
hh3cL2vpnPwAcIfName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cL2vpnPwAcIfName.setStatus("current")
_Hh3cL2vpnPwAcSrvId_Type = Unsigned32
_Hh3cL2vpnPwAcSrvId_Object = MibTableColumn
hh3cL2vpnPwAcSrvId = _Hh3cL2vpnPwAcSrvId_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 162, 5, 1, 1, 5),
    _Hh3cL2vpnPwAcSrvId_Type()
)
hh3cL2vpnPwAcSrvId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cL2vpnPwAcSrvId.setStatus("current")


class _Hh3cL2vpnPwVsiName_Type(DisplayString):
    """Custom type hh3cL2vpnPwVsiName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_Hh3cL2vpnPwVsiName_Type.__name__ = "DisplayString"
_Hh3cL2vpnPwVsiName_Object = MibTableColumn
hh3cL2vpnPwVsiName = _Hh3cL2vpnPwVsiName_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 162, 5, 1, 1, 6),
    _Hh3cL2vpnPwVsiName_Type()
)
hh3cL2vpnPwVsiName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cL2vpnPwVsiName.setStatus("current")


class _Hh3cL2vpnPwXcgName_Type(DisplayString):
    """Custom type hh3cL2vpnPwXcgName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_Hh3cL2vpnPwXcgName_Type.__name__ = "DisplayString"
_Hh3cL2vpnPwXcgName_Object = MibTableColumn
hh3cL2vpnPwXcgName = _Hh3cL2vpnPwXcgName_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 162, 5, 1, 1, 7),
    _Hh3cL2vpnPwXcgName_Type()
)
hh3cL2vpnPwXcgName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cL2vpnPwXcgName.setStatus("current")


class _Hh3cL2vpnPwXcgConnName_Type(DisplayString):
    """Custom type hh3cL2vpnPwXcgConnName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_Hh3cL2vpnPwXcgConnName_Type.__name__ = "DisplayString"
_Hh3cL2vpnPwXcgConnName_Object = MibTableColumn
hh3cL2vpnPwXcgConnName = _Hh3cL2vpnPwXcgConnName_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 162, 5, 1, 1, 8),
    _Hh3cL2vpnPwXcgConnName_Type()
)
hh3cL2vpnPwXcgConnName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cL2vpnPwXcgConnName.setStatus("current")


class _Hh3cL2vpnPwQosDirection_Type(Integer32):
    """Custom type hh3cL2vpnPwQosDirection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("inbound", 2),
          ("outbound", 3),
          ("both", 4))
    )


_Hh3cL2vpnPwQosDirection_Type.__name__ = "Integer32"
_Hh3cL2vpnPwQosDirection_Object = MibTableColumn
hh3cL2vpnPwQosDirection = _Hh3cL2vpnPwQosDirection_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 162, 5, 1, 1, 9),
    _Hh3cL2vpnPwQosDirection_Type()
)
hh3cL2vpnPwQosDirection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cL2vpnPwQosDirection.setStatus("current")
_Hh3cL2vpnPwInboundQosCir_Type = Unsigned32
_Hh3cL2vpnPwInboundQosCir_Object = MibTableColumn
hh3cL2vpnPwInboundQosCir = _Hh3cL2vpnPwInboundQosCir_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 162, 5, 1, 1, 10),
    _Hh3cL2vpnPwInboundQosCir_Type()
)
hh3cL2vpnPwInboundQosCir.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cL2vpnPwInboundQosCir.setStatus("current")
_Hh3cL2vpnPwInboundQosCbs_Type = Unsigned32
_Hh3cL2vpnPwInboundQosCbs_Object = MibTableColumn
hh3cL2vpnPwInboundQosCbs = _Hh3cL2vpnPwInboundQosCbs_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 162, 5, 1, 1, 11),
    _Hh3cL2vpnPwInboundQosCbs_Type()
)
hh3cL2vpnPwInboundQosCbs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cL2vpnPwInboundQosCbs.setStatus("current")
_Hh3cL2vpnPwInboundQosEbs_Type = Unsigned32
_Hh3cL2vpnPwInboundQosEbs_Object = MibTableColumn
hh3cL2vpnPwInboundQosEbs = _Hh3cL2vpnPwInboundQosEbs_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 162, 5, 1, 1, 12),
    _Hh3cL2vpnPwInboundQosEbs_Type()
)
hh3cL2vpnPwInboundQosEbs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cL2vpnPwInboundQosEbs.setStatus("current")
_Hh3cL2vpnPwOutboundQosCir_Type = Unsigned32
_Hh3cL2vpnPwOutboundQosCir_Object = MibTableColumn
hh3cL2vpnPwOutboundQosCir = _Hh3cL2vpnPwOutboundQosCir_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 162, 5, 1, 1, 13),
    _Hh3cL2vpnPwOutboundQosCir_Type()
)
hh3cL2vpnPwOutboundQosCir.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cL2vpnPwOutboundQosCir.setStatus("current")
_Hh3cL2vpnPwOutboundQosCbs_Type = Unsigned32
_Hh3cL2vpnPwOutboundQosCbs_Object = MibTableColumn
hh3cL2vpnPwOutboundQosCbs = _Hh3cL2vpnPwOutboundQosCbs_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 162, 5, 1, 1, 14),
    _Hh3cL2vpnPwOutboundQosCbs_Type()
)
hh3cL2vpnPwOutboundQosCbs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cL2vpnPwOutboundQosCbs.setStatus("current")
_Hh3cL2vpnPwOutboundQosEbs_Type = Unsigned32
_Hh3cL2vpnPwOutboundQosEbs_Object = MibTableColumn
hh3cL2vpnPwOutboundQosEbs = _Hh3cL2vpnPwOutboundQosEbs_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 162, 5, 1, 1, 15),
    _Hh3cL2vpnPwOutboundQosEbs_Type()
)
hh3cL2vpnPwOutboundQosEbs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cL2vpnPwOutboundQosEbs.setStatus("current")

# Managed Objects groups


# Notification objects

hh3cL2vpnPwSwitchPtoB = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 162, 0, 1)
)
hh3cL2vpnPwSwitchPtoB.setObjects(
      *(("HH3C-L2VPN-MIB", "hh3cL2vpnXcgPwIndex"),
        ("HH3C-L2VPN-MIB", "hh3cL2vpnXcgPwPeerIp"),
        ("HH3C-L2VPN-MIB", "hh3cL2vpnXcgPwPwID"),
        ("HH3C-L2VPN-MIB", "hh3cL2vpnXcgPwIndex"),
        ("HH3C-L2VPN-MIB", "hh3cL2vpnXcgPwPeerIp"),
        ("HH3C-L2VPN-MIB", "hh3cL2vpnXcgPwPwID"))
)
if mibBuilder.loadTexts:
    hh3cL2vpnPwSwitchPtoB.setStatus(
        "current"
    )

hh3cL2vpnPwSwitchBtoP = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 162, 0, 2)
)
hh3cL2vpnPwSwitchBtoP.setObjects(
      *(("HH3C-L2VPN-MIB", "hh3cL2vpnXcgPwIndex"),
        ("HH3C-L2VPN-MIB", "hh3cL2vpnXcgPwPeerIp"),
        ("HH3C-L2VPN-MIB", "hh3cL2vpnXcgPwPwID"),
        ("HH3C-L2VPN-MIB", "hh3cL2vpnXcgPwIndex"),
        ("HH3C-L2VPN-MIB", "hh3cL2vpnXcgPwPeerIp"),
        ("HH3C-L2VPN-MIB", "hh3cL2vpnXcgPwPwID"))
)
if mibBuilder.loadTexts:
    hh3cL2vpnPwSwitchBtoP.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HH3C-L2VPN-MIB",
    **{"hh3cL2vpn": hh3cL2vpn,
       "hh3cL2vpnPwNotifications": hh3cL2vpnPwNotifications,
       "hh3cL2vpnPwSwitchPtoB": hh3cL2vpnPwSwitchPtoB,
       "hh3cL2vpnPwSwitchBtoP": hh3cL2vpnPwSwitchBtoP,
       "hh3cL2vpnGlobalTable": hh3cL2vpnGlobalTable,
       "hh3cL2vpnPwcTable": hh3cL2vpnPwcTable,
       "hh3cL2vpnPwcEntry": hh3cL2vpnPwcEntry,
       "hh3cL2vpnPwcName": hh3cL2vpnPwcName,
       "hh3cL2vpnPwcCvType": hh3cL2vpnPwcCvType,
       "hh3cL2vpnPwcCcType": hh3cL2vpnPwcCcType,
       "hh3cL2vpnPwcControlWord": hh3cL2vpnPwcControlWord,
       "hh3cL2vpnPwcPwType": hh3cL2vpnPwcPwType,
       "hh3cL2vpnPwcRowStatus": hh3cL2vpnPwcRowStatus,
       "hh3cL2vpnPwcFlowLabel": hh3cL2vpnPwcFlowLabel,
       "hh3cL2vpnLinkTable": hh3cL2vpnLinkTable,
       "hh3cL2vpnLinkEntry": hh3cL2vpnLinkEntry,
       "hh3cL2vpnLinkVsiIndex": hh3cL2vpnLinkVsiIndex,
       "hh3cL2vpnLinkLinkID": hh3cL2vpnLinkLinkID,
       "hh3cL2vpnLinkType": hh3cL2vpnLinkType,
       "hh3cL2vpnLinkIfIndex": hh3cL2vpnLinkIfIndex,
       "hh3cL2vpnLinkSrvID": hh3cL2vpnLinkSrvID,
       "hh3cL2vpnLinkTunnelID": hh3cL2vpnLinkTunnelID,
       "hh3cL2vpnVpwsTable": hh3cL2vpnVpwsTable,
       "hh3cL2vpnXcgTable": hh3cL2vpnXcgTable,
       "hh3cL2vpnXcgEntry": hh3cL2vpnXcgEntry,
       "hh3cL2vpnXcgName": hh3cL2vpnXcgName,
       "hh3cL2vpnXcgAdminState": hh3cL2vpnXcgAdminState,
       "hh3cL2vpnXcgRowStatus": hh3cL2vpnXcgRowStatus,
       "hh3cL2vpnXcgConnTable": hh3cL2vpnXcgConnTable,
       "hh3cL2vpnXcgConnEntry": hh3cL2vpnXcgConnEntry,
       "hh3cL2vpnXcgConnName": hh3cL2vpnXcgConnName,
       "hh3cL2vpnXcgConnRowStatus": hh3cL2vpnXcgConnRowStatus,
       "hh3cL2vpnXcgConnRedundancy": hh3cL2vpnXcgConnRedundancy,
       "hh3cL2vpnXcgAcTable": hh3cL2vpnXcgAcTable,
       "hh3cL2vpnXcgAcEntry": hh3cL2vpnXcgAcEntry,
       "hh3cL2vpnXcgAcIfIndex": hh3cL2vpnXcgAcIfIndex,
       "hh3cL2vpnXcgAcEvcSrvInstId": hh3cL2vpnXcgAcEvcSrvInstId,
       "hh3cL2vpnXcgAcAccessMode": hh3cL2vpnXcgAcAccessMode,
       "hh3cL2vpnXcgAcRowStatus": hh3cL2vpnXcgAcRowStatus,
       "hh3cL2vpnXcgPwTable": hh3cL2vpnXcgPwTable,
       "hh3cL2vpnXcgPwEntry": hh3cL2vpnXcgPwEntry,
       "hh3cL2vpnXcgPwIndex": hh3cL2vpnXcgPwIndex,
       "hh3cL2vpnXcgPwCfgType": hh3cL2vpnXcgPwCfgType,
       "hh3cL2vpnXcgPwClassName": hh3cL2vpnXcgPwClassName,
       "hh3cL2vpnXcgPwTunnelPolicy": hh3cL2vpnXcgPwTunnelPolicy,
       "hh3cL2vpnXcgPwPeerIp": hh3cL2vpnXcgPwPeerIp,
       "hh3cL2vpnXcgPwPwID": hh3cL2vpnXcgPwPwID,
       "hh3cL2vpnXcgPwRowStatus": hh3cL2vpnXcgPwRowStatus,
       "hh3cL2vpnXcgPwIgnoreStandby": hh3cL2vpnXcgPwIgnoreStandby,
       "hh3cL2vpnAcTable": hh3cL2vpnAcTable,
       "hh3cL2vpnAcCfgTable": hh3cL2vpnAcCfgTable,
       "hh3cL2vpnAcCfgEntry": hh3cL2vpnAcCfgEntry,
       "hh3cL2vpnAcIfIndex": hh3cL2vpnAcIfIndex,
       "hh3cL2vpnAcSrvId": hh3cL2vpnAcSrvId,
       "hh3cL2vpnAcIfName": hh3cL2vpnAcIfName,
       "hh3cL2vpnAcVsiName": hh3cL2vpnAcVsiName,
       "hh3cL2vpnAcXcgName": hh3cL2vpnAcXcgName,
       "hh3cL2vpnAcXcgConnName": hh3cL2vpnAcXcgConnName,
       "hh3cL2vpnAcDot1qType": hh3cL2vpnAcDot1qType,
       "hh3cL2vpnAcVLANID": hh3cL2vpnAcVLANID,
       "hh3cL2vpnPwTable": hh3cL2vpnPwTable,
       "hh3cL2vpnPwCfgTable": hh3cL2vpnPwCfgTable,
       "hh3cL2vpnPwCfgEntry": hh3cL2vpnPwCfgEntry,
       "hh3cL2vpnPwPeerIp": hh3cL2vpnPwPeerIp,
       "hh3cL2vpnPwId": hh3cL2vpnPwId,
       "hh3cL2vpnPwAcIfIndex": hh3cL2vpnPwAcIfIndex,
       "hh3cL2vpnPwAcIfName": hh3cL2vpnPwAcIfName,
       "hh3cL2vpnPwAcSrvId": hh3cL2vpnPwAcSrvId,
       "hh3cL2vpnPwVsiName": hh3cL2vpnPwVsiName,
       "hh3cL2vpnPwXcgName": hh3cL2vpnPwXcgName,
       "hh3cL2vpnPwXcgConnName": hh3cL2vpnPwXcgConnName,
       "hh3cL2vpnPwQosDirection": hh3cL2vpnPwQosDirection,
       "hh3cL2vpnPwInboundQosCir": hh3cL2vpnPwInboundQosCir,
       "hh3cL2vpnPwInboundQosCbs": hh3cL2vpnPwInboundQosCbs,
       "hh3cL2vpnPwInboundQosEbs": hh3cL2vpnPwInboundQosEbs,
       "hh3cL2vpnPwOutboundQosCir": hh3cL2vpnPwOutboundQosCir,
       "hh3cL2vpnPwOutboundQosCbs": hh3cL2vpnPwOutboundQosCbs,
       "hh3cL2vpnPwOutboundQosEbs": hh3cL2vpnPwOutboundQosEbs}
)
