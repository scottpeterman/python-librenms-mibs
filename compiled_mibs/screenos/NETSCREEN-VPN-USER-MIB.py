# SNMP MIB module (NETSCREEN-VPN-USER-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\screenos\NETSCREEN-VPN-USER-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 12:26:07 2025
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

(netscreenVpn,
 netscreenVpnMibModule) = mibBuilder.importSymbols(
    "NETSCREEN-SMI",
    "netscreenVpn",
    "netscreenVpnMibModule")

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

netscreenUserMibModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 3224, 4, 0, 10)
)
if mibBuilder.loadTexts:
    netscreenUserMibModule.setRevisions(
        ("2004-05-03 00:00",
         "2004-03-03 00:00",
         "2003-11-13 00:00",
         "2002-05-05 00:00",
         "2001-05-14 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_NsVpnUser_ObjectIdentity = ObjectIdentity
nsVpnUser = _NsVpnUser_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3224, 4, 10)
)
_NsVpnUsrDialupGrpTable_Object = MibTable
nsVpnUsrDialupGrpTable = _NsVpnUsrDialupGrpTable_Object(
    (1, 3, 6, 1, 4, 1, 3224, 4, 10, 1)
)
if mibBuilder.loadTexts:
    nsVpnUsrDialupGrpTable.setStatus("current")
_NsVpnUsrDialupGrpEntry_Object = MibTableRow
nsVpnUsrDialupGrpEntry = _NsVpnUsrDialupGrpEntry_Object(
    (1, 3, 6, 1, 4, 1, 3224, 4, 10, 1, 1)
)
nsVpnUsrDialupGrpEntry.setIndexNames(
    (0, "NETSCREEN-VPN-USER-MIB", "nsVpnUsrDialupGrpIndex"),
)
if mibBuilder.loadTexts:
    nsVpnUsrDialupGrpEntry.setStatus("current")


class _NsVpnUsrDialupGrpIndex_Type(Integer32):
    """Custom type nsVpnUsrDialupGrpIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_NsVpnUsrDialupGrpIndex_Type.__name__ = "Integer32"
_NsVpnUsrDialupGrpIndex_Object = MibTableColumn
nsVpnUsrDialupGrpIndex = _NsVpnUsrDialupGrpIndex_Object(
    (1, 3, 6, 1, 4, 1, 3224, 4, 10, 1, 1, 1),
    _NsVpnUsrDialupGrpIndex_Type()
)
nsVpnUsrDialupGrpIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsVpnUsrDialupGrpIndex.setStatus("current")


class _NsVpnUsrDialupGrpName_Type(DisplayString):
    """Custom type nsVpnUsrDialupGrpName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_NsVpnUsrDialupGrpName_Type.__name__ = "DisplayString"
_NsVpnUsrDialupGrpName_Object = MibTableColumn
nsVpnUsrDialupGrpName = _NsVpnUsrDialupGrpName_Object(
    (1, 3, 6, 1, 4, 1, 3224, 4, 10, 1, 1, 2),
    _NsVpnUsrDialupGrpName_Type()
)
nsVpnUsrDialupGrpName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsVpnUsrDialupGrpName.setStatus("current")


class _NsVpnUsrDialupGrpType_Type(Integer32):
    """Custom type nsVpnUsrDialupGrpType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("undefined", 0),
          ("manual", 1),
          ("ike", 2),
          ("l2tp", 3),
          ("xauth", 4),
          ("auth", 5),
          ("external", 6))
    )


_NsVpnUsrDialupGrpType_Type.__name__ = "Integer32"
_NsVpnUsrDialupGrpType_Object = MibTableColumn
nsVpnUsrDialupGrpType = _NsVpnUsrDialupGrpType_Object(
    (1, 3, 6, 1, 4, 1, 3224, 4, 10, 1, 1, 3),
    _NsVpnUsrDialupGrpType_Type()
)
nsVpnUsrDialupGrpType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsVpnUsrDialupGrpType.setStatus("current")
_NsVpnUsrDialupGrpVsys_Type = Integer32
_NsVpnUsrDialupGrpVsys_Object = MibTableColumn
nsVpnUsrDialupGrpVsys = _NsVpnUsrDialupGrpVsys_Object(
    (1, 3, 6, 1, 4, 1, 3224, 4, 10, 1, 1, 4),
    _NsVpnUsrDialupGrpVsys_Type()
)
nsVpnUsrDialupGrpVsys.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsVpnUsrDialupGrpVsys.setStatus("current")
_NsVpnManualKeyUsrTable_Object = MibTable
nsVpnManualKeyUsrTable = _NsVpnManualKeyUsrTable_Object(
    (1, 3, 6, 1, 4, 1, 3224, 4, 10, 2)
)
if mibBuilder.loadTexts:
    nsVpnManualKeyUsrTable.setStatus("current")
_NsVpnManualKeyUsrEntry_Object = MibTableRow
nsVpnManualKeyUsrEntry = _NsVpnManualKeyUsrEntry_Object(
    (1, 3, 6, 1, 4, 1, 3224, 4, 10, 2, 1)
)
nsVpnManualKeyUsrEntry.setIndexNames(
    (0, "NETSCREEN-VPN-USER-MIB", "nsVpnManualKeyUsrIndex"),
)
if mibBuilder.loadTexts:
    nsVpnManualKeyUsrEntry.setStatus("current")


class _NsVpnManualKeyUsrIndex_Type(Integer32):
    """Custom type nsVpnManualKeyUsrIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_NsVpnManualKeyUsrIndex_Type.__name__ = "Integer32"
_NsVpnManualKeyUsrIndex_Object = MibTableColumn
nsVpnManualKeyUsrIndex = _NsVpnManualKeyUsrIndex_Object(
    (1, 3, 6, 1, 4, 1, 3224, 4, 10, 2, 1, 1),
    _NsVpnManualKeyUsrIndex_Type()
)
nsVpnManualKeyUsrIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsVpnManualKeyUsrIndex.setStatus("current")


class _NsVpnManualKeyUsrName_Type(DisplayString):
    """Custom type nsVpnManualKeyUsrName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_NsVpnManualKeyUsrName_Type.__name__ = "DisplayString"
_NsVpnManualKeyUsrName_Object = MibTableColumn
nsVpnManualKeyUsrName = _NsVpnManualKeyUsrName_Object(
    (1, 3, 6, 1, 4, 1, 3224, 4, 10, 2, 1, 2),
    _NsVpnManualKeyUsrName_Type()
)
nsVpnManualKeyUsrName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsVpnManualKeyUsrName.setStatus("current")


class _NsVpnManualKeyUsrGrp_Type(DisplayString):
    """Custom type nsVpnManualKeyUsrGrp based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_NsVpnManualKeyUsrGrp_Type.__name__ = "DisplayString"
_NsVpnManualKeyUsrGrp_Object = MibTableColumn
nsVpnManualKeyUsrGrp = _NsVpnManualKeyUsrGrp_Object(
    (1, 3, 6, 1, 4, 1, 3224, 4, 10, 2, 1, 3),
    _NsVpnManualKeyUsrGrp_Type()
)
nsVpnManualKeyUsrGrp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsVpnManualKeyUsrGrp.setStatus("current")
_NsVpnManualKeyUsrSILocal_Type = Integer32
_NsVpnManualKeyUsrSILocal_Object = MibTableColumn
nsVpnManualKeyUsrSILocal = _NsVpnManualKeyUsrSILocal_Object(
    (1, 3, 6, 1, 4, 1, 3224, 4, 10, 2, 1, 4),
    _NsVpnManualKeyUsrSILocal_Type()
)
nsVpnManualKeyUsrSILocal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsVpnManualKeyUsrSILocal.setStatus("current")
_NsVpnManualKeyUsrSIRemote_Type = Integer32
_NsVpnManualKeyUsrSIRemote_Object = MibTableColumn
nsVpnManualKeyUsrSIRemote = _NsVpnManualKeyUsrSIRemote_Object(
    (1, 3, 6, 1, 4, 1, 3224, 4, 10, 2, 1, 5),
    _NsVpnManualKeyUsrSIRemote_Type()
)
nsVpnManualKeyUsrSIRemote.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsVpnManualKeyUsrSIRemote.setStatus("current")


class _NsVpnManualKeyUsrTunnelType_Type(Integer32):
    """Custom type nsVpnManualKeyUsrTunnelType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("esp", 0),
          ("ah", 1))
    )


_NsVpnManualKeyUsrTunnelType_Type.__name__ = "Integer32"
_NsVpnManualKeyUsrTunnelType_Object = MibTableColumn
nsVpnManualKeyUsrTunnelType = _NsVpnManualKeyUsrTunnelType_Object(
    (1, 3, 6, 1, 4, 1, 3224, 4, 10, 2, 1, 6),
    _NsVpnManualKeyUsrTunnelType_Type()
)
nsVpnManualKeyUsrTunnelType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsVpnManualKeyUsrTunnelType.setStatus("current")


class _NsVpnManualKeyUsrEspEncAlg_Type(Integer32):
    """Custom type nsVpnManualKeyUsrEspEncAlg based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("null", 0),
          ("des-cbc", 1),
          ("triple-des-cbc", 2),
          ("aes", 3),
          ("aes-192", 4),
          ("aes-256", 5))
    )


_NsVpnManualKeyUsrEspEncAlg_Type.__name__ = "Integer32"
_NsVpnManualKeyUsrEspEncAlg_Object = MibTableColumn
nsVpnManualKeyUsrEspEncAlg = _NsVpnManualKeyUsrEspEncAlg_Object(
    (1, 3, 6, 1, 4, 1, 3224, 4, 10, 2, 1, 7),
    _NsVpnManualKeyUsrEspEncAlg_Type()
)
nsVpnManualKeyUsrEspEncAlg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsVpnManualKeyUsrEspEncAlg.setStatus("current")


class _NsVpnManualKeyUsrEspAuthAlg_Type(Integer32):
    """Custom type nsVpnManualKeyUsrEspAuthAlg based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("null", 0),
          ("md5", 1),
          ("sha", 2))
    )


_NsVpnManualKeyUsrEspAuthAlg_Type.__name__ = "Integer32"
_NsVpnManualKeyUsrEspAuthAlg_Object = MibTableColumn
nsVpnManualKeyUsrEspAuthAlg = _NsVpnManualKeyUsrEspAuthAlg_Object(
    (1, 3, 6, 1, 4, 1, 3224, 4, 10, 2, 1, 8),
    _NsVpnManualKeyUsrEspAuthAlg_Type()
)
nsVpnManualKeyUsrEspAuthAlg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsVpnManualKeyUsrEspAuthAlg.setStatus("current")


class _NsVpnManualKeyUsrAhHash_Type(Integer32):
    """Custom type nsVpnManualKeyUsrAhHash based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("null", 0),
          ("md5", 1),
          ("sha", 2))
    )


_NsVpnManualKeyUsrAhHash_Type.__name__ = "Integer32"
_NsVpnManualKeyUsrAhHash_Object = MibTableColumn
nsVpnManualKeyUsrAhHash = _NsVpnManualKeyUsrAhHash_Object(
    (1, 3, 6, 1, 4, 1, 3224, 4, 10, 2, 1, 9),
    _NsVpnManualKeyUsrAhHash_Type()
)
nsVpnManualKeyUsrAhHash.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsVpnManualKeyUsrAhHash.setStatus("current")
_NsVpnManualKeyUsrVsys_Type = Integer32
_NsVpnManualKeyUsrVsys_Object = MibTableColumn
nsVpnManualKeyUsrVsys = _NsVpnManualKeyUsrVsys_Object(
    (1, 3, 6, 1, 4, 1, 3224, 4, 10, 2, 1, 10),
    _NsVpnManualKeyUsrVsys_Type()
)
nsVpnManualKeyUsrVsys.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsVpnManualKeyUsrVsys.setStatus("current")
_NsVpnAILUsrTable_Object = MibTable
nsVpnAILUsrTable = _NsVpnAILUsrTable_Object(
    (1, 3, 6, 1, 4, 1, 3224, 4, 10, 3)
)
if mibBuilder.loadTexts:
    nsVpnAILUsrTable.setStatus("current")
_NsVpnAILUsrEntry_Object = MibTableRow
nsVpnAILUsrEntry = _NsVpnAILUsrEntry_Object(
    (1, 3, 6, 1, 4, 1, 3224, 4, 10, 3, 1)
)
nsVpnAILUsrEntry.setIndexNames(
    (0, "NETSCREEN-VPN-USER-MIB", "nsVpnAILUsrIndex"),
)
if mibBuilder.loadTexts:
    nsVpnAILUsrEntry.setStatus("current")


class _NsVpnAILUsrIndex_Type(Integer32):
    """Custom type nsVpnAILUsrIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_NsVpnAILUsrIndex_Type.__name__ = "Integer32"
_NsVpnAILUsrIndex_Object = MibTableColumn
nsVpnAILUsrIndex = _NsVpnAILUsrIndex_Object(
    (1, 3, 6, 1, 4, 1, 3224, 4, 10, 3, 1, 1),
    _NsVpnAILUsrIndex_Type()
)
nsVpnAILUsrIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsVpnAILUsrIndex.setStatus("current")


class _NsVpnAILUsrName_Type(DisplayString):
    """Custom type nsVpnAILUsrName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_NsVpnAILUsrName_Type.__name__ = "DisplayString"
_NsVpnAILUsrName_Object = MibTableColumn
nsVpnAILUsrName = _NsVpnAILUsrName_Object(
    (1, 3, 6, 1, 4, 1, 3224, 4, 10, 3, 1, 2),
    _NsVpnAILUsrName_Type()
)
nsVpnAILUsrName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsVpnAILUsrName.setStatus("current")


class _NsVpnAILUsrGrp_Type(DisplayString):
    """Custom type nsVpnAILUsrGrp based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_NsVpnAILUsrGrp_Type.__name__ = "DisplayString"
_NsVpnAILUsrGrp_Object = MibTableColumn
nsVpnAILUsrGrp = _NsVpnAILUsrGrp_Object(
    (1, 3, 6, 1, 4, 1, 3224, 4, 10, 3, 1, 3),
    _NsVpnAILUsrGrp_Type()
)
nsVpnAILUsrGrp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsVpnAILUsrGrp.setStatus("current")


class _NsVpnAILUsrStatus_Type(Integer32):
    """Custom type nsVpnAILUsrStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enabled", 1))
    )


_NsVpnAILUsrStatus_Type.__name__ = "Integer32"
_NsVpnAILUsrStatus_Object = MibTableColumn
nsVpnAILUsrStatus = _NsVpnAILUsrStatus_Object(
    (1, 3, 6, 1, 4, 1, 3224, 4, 10, 3, 1, 4),
    _NsVpnAILUsrStatus_Type()
)
nsVpnAILUsrStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsVpnAILUsrStatus.setStatus("current")


class _NsVpnAILUsrIKE_Type(Integer32):
    """Custom type nsVpnAILUsrIKE based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1))
    )


_NsVpnAILUsrIKE_Type.__name__ = "Integer32"
_NsVpnAILUsrIKE_Object = MibTableColumn
nsVpnAILUsrIKE = _NsVpnAILUsrIKE_Object(
    (1, 3, 6, 1, 4, 1, 3224, 4, 10, 3, 1, 5),
    _NsVpnAILUsrIKE_Type()
)
nsVpnAILUsrIKE.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsVpnAILUsrIKE.setStatus("current")


class _NsVpnAILUsrIKEIdType_Type(Integer32):
    """Custom type nsVpnAILUsrIKEIdType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10)
        )
    )
    namedValues = NamedValues(
        *(("not-set", 0),
          ("ipv4-addr", 1),
          ("fqdn", 2),
          ("usr-fqdn", 3),
          ("ipv4-addr-subnet", 4),
          ("ipv6-addr", 5),
          ("ipv6-addr-subnet", 6),
          ("ipv4-addr-addr-range", 7),
          ("ipv6-addr-addr-range", 8),
          ("der-asn1-dn", 9),
          ("der-asn1-gn", 10))
    )


_NsVpnAILUsrIKEIdType_Type.__name__ = "Integer32"
_NsVpnAILUsrIKEIdType_Object = MibTableColumn
nsVpnAILUsrIKEIdType = _NsVpnAILUsrIKEIdType_Object(
    (1, 3, 6, 1, 4, 1, 3224, 4, 10, 3, 1, 6),
    _NsVpnAILUsrIKEIdType_Type()
)
nsVpnAILUsrIKEIdType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsVpnAILUsrIKEIdType.setStatus("current")
_NsVpnAILUsrIKEId_Type = DisplayString
_NsVpnAILUsrIKEId_Object = MibTableColumn
nsVpnAILUsrIKEId = _NsVpnAILUsrIKEId_Object(
    (1, 3, 6, 1, 4, 1, 3224, 4, 10, 3, 1, 7),
    _NsVpnAILUsrIKEId_Type()
)
nsVpnAILUsrIKEId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsVpnAILUsrIKEId.setStatus("current")


class _NsVpnAILUsrAuth_Type(Integer32):
    """Custom type nsVpnAILUsrAuth based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1))
    )


_NsVpnAILUsrAuth_Type.__name__ = "Integer32"
_NsVpnAILUsrAuth_Object = MibTableColumn
nsVpnAILUsrAuth = _NsVpnAILUsrAuth_Object(
    (1, 3, 6, 1, 4, 1, 3224, 4, 10, 3, 1, 8),
    _NsVpnAILUsrAuth_Type()
)
nsVpnAILUsrAuth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsVpnAILUsrAuth.setStatus("current")


class _NsVpnAILUsrL2TP_Type(Integer32):
    """Custom type nsVpnAILUsrL2TP based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1))
    )


_NsVpnAILUsrL2TP_Type.__name__ = "Integer32"
_NsVpnAILUsrL2TP_Object = MibTableColumn
nsVpnAILUsrL2TP = _NsVpnAILUsrL2TP_Object(
    (1, 3, 6, 1, 4, 1, 3224, 4, 10, 3, 1, 9),
    _NsVpnAILUsrL2TP_Type()
)
nsVpnAILUsrL2TP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsVpnAILUsrL2TP.setStatus("current")
_NsVpnAILUsrL2tpRemoteIp_Type = IpAddress
_NsVpnAILUsrL2tpRemoteIp_Object = MibTableColumn
nsVpnAILUsrL2tpRemoteIp = _NsVpnAILUsrL2tpRemoteIp_Object(
    (1, 3, 6, 1, 4, 1, 3224, 4, 10, 3, 1, 10),
    _NsVpnAILUsrL2tpRemoteIp_Type()
)
nsVpnAILUsrL2tpRemoteIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsVpnAILUsrL2tpRemoteIp.setStatus("current")
_NsVpnAILUsrL2tpIpPool_Type = DisplayString
_NsVpnAILUsrL2tpIpPool_Object = MibTableColumn
nsVpnAILUsrL2tpIpPool = _NsVpnAILUsrL2tpIpPool_Object(
    (1, 3, 6, 1, 4, 1, 3224, 4, 10, 3, 1, 11),
    _NsVpnAILUsrL2tpIpPool_Type()
)
nsVpnAILUsrL2tpIpPool.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsVpnAILUsrL2tpIpPool.setStatus("current")
_NsVpnAILUsrL2tpIp_Type = IpAddress
_NsVpnAILUsrL2tpIp_Object = MibTableColumn
nsVpnAILUsrL2tpIp = _NsVpnAILUsrL2tpIp_Object(
    (1, 3, 6, 1, 4, 1, 3224, 4, 10, 3, 1, 12),
    _NsVpnAILUsrL2tpIp_Type()
)
nsVpnAILUsrL2tpIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsVpnAILUsrL2tpIp.setStatus("current")
_NsVpnAILUsrL2tpPriDnsIp_Type = IpAddress
_NsVpnAILUsrL2tpPriDnsIp_Object = MibTableColumn
nsVpnAILUsrL2tpPriDnsIp = _NsVpnAILUsrL2tpPriDnsIp_Object(
    (1, 3, 6, 1, 4, 1, 3224, 4, 10, 3, 1, 13),
    _NsVpnAILUsrL2tpPriDnsIp_Type()
)
nsVpnAILUsrL2tpPriDnsIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsVpnAILUsrL2tpPriDnsIp.setStatus("current")
_NsVpnAILUsrL2tpSecDnsIp_Type = IpAddress
_NsVpnAILUsrL2tpSecDnsIp_Object = MibTableColumn
nsVpnAILUsrL2tpSecDnsIp = _NsVpnAILUsrL2tpSecDnsIp_Object(
    (1, 3, 6, 1, 4, 1, 3224, 4, 10, 3, 1, 14),
    _NsVpnAILUsrL2tpSecDnsIp_Type()
)
nsVpnAILUsrL2tpSecDnsIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsVpnAILUsrL2tpSecDnsIp.setStatus("current")
_NsVpnAILUsrL2tpPriWinsIp_Type = IpAddress
_NsVpnAILUsrL2tpPriWinsIp_Object = MibTableColumn
nsVpnAILUsrL2tpPriWinsIp = _NsVpnAILUsrL2tpPriWinsIp_Object(
    (1, 3, 6, 1, 4, 1, 3224, 4, 10, 3, 1, 15),
    _NsVpnAILUsrL2tpPriWinsIp_Type()
)
nsVpnAILUsrL2tpPriWinsIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsVpnAILUsrL2tpPriWinsIp.setStatus("current")
_NsVpnAILUsrL2tpSecWinsIp_Type = IpAddress
_NsVpnAILUsrL2tpSecWinsIp_Object = MibTableColumn
nsVpnAILUsrL2tpSecWinsIp = _NsVpnAILUsrL2tpSecWinsIp_Object(
    (1, 3, 6, 1, 4, 1, 3224, 4, 10, 3, 1, 16),
    _NsVpnAILUsrL2tpSecWinsIp_Type()
)
nsVpnAILUsrL2tpSecWinsIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsVpnAILUsrL2tpSecWinsIp.setStatus("current")
_NsVpnAILUsrVsys_Type = Integer32
_NsVpnAILUsrVsys_Object = MibTableColumn
nsVpnAILUsrVsys = _NsVpnAILUsrVsys_Object(
    (1, 3, 6, 1, 4, 1, 3224, 4, 10, 3, 1, 17),
    _NsVpnAILUsrVsys_Type()
)
nsVpnAILUsrVsys.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsVpnAILUsrVsys.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "NETSCREEN-VPN-USER-MIB",
    **{"netscreenUserMibModule": netscreenUserMibModule,
       "nsVpnUser": nsVpnUser,
       "nsVpnUsrDialupGrpTable": nsVpnUsrDialupGrpTable,
       "nsVpnUsrDialupGrpEntry": nsVpnUsrDialupGrpEntry,
       "nsVpnUsrDialupGrpIndex": nsVpnUsrDialupGrpIndex,
       "nsVpnUsrDialupGrpName": nsVpnUsrDialupGrpName,
       "nsVpnUsrDialupGrpType": nsVpnUsrDialupGrpType,
       "nsVpnUsrDialupGrpVsys": nsVpnUsrDialupGrpVsys,
       "nsVpnManualKeyUsrTable": nsVpnManualKeyUsrTable,
       "nsVpnManualKeyUsrEntry": nsVpnManualKeyUsrEntry,
       "nsVpnManualKeyUsrIndex": nsVpnManualKeyUsrIndex,
       "nsVpnManualKeyUsrName": nsVpnManualKeyUsrName,
       "nsVpnManualKeyUsrGrp": nsVpnManualKeyUsrGrp,
       "nsVpnManualKeyUsrSILocal": nsVpnManualKeyUsrSILocal,
       "nsVpnManualKeyUsrSIRemote": nsVpnManualKeyUsrSIRemote,
       "nsVpnManualKeyUsrTunnelType": nsVpnManualKeyUsrTunnelType,
       "nsVpnManualKeyUsrEspEncAlg": nsVpnManualKeyUsrEspEncAlg,
       "nsVpnManualKeyUsrEspAuthAlg": nsVpnManualKeyUsrEspAuthAlg,
       "nsVpnManualKeyUsrAhHash": nsVpnManualKeyUsrAhHash,
       "nsVpnManualKeyUsrVsys": nsVpnManualKeyUsrVsys,
       "nsVpnAILUsrTable": nsVpnAILUsrTable,
       "nsVpnAILUsrEntry": nsVpnAILUsrEntry,
       "nsVpnAILUsrIndex": nsVpnAILUsrIndex,
       "nsVpnAILUsrName": nsVpnAILUsrName,
       "nsVpnAILUsrGrp": nsVpnAILUsrGrp,
       "nsVpnAILUsrStatus": nsVpnAILUsrStatus,
       "nsVpnAILUsrIKE": nsVpnAILUsrIKE,
       "nsVpnAILUsrIKEIdType": nsVpnAILUsrIKEIdType,
       "nsVpnAILUsrIKEId": nsVpnAILUsrIKEId,
       "nsVpnAILUsrAuth": nsVpnAILUsrAuth,
       "nsVpnAILUsrL2TP": nsVpnAILUsrL2TP,
       "nsVpnAILUsrL2tpRemoteIp": nsVpnAILUsrL2tpRemoteIp,
       "nsVpnAILUsrL2tpIpPool": nsVpnAILUsrL2tpIpPool,
       "nsVpnAILUsrL2tpIp": nsVpnAILUsrL2tpIp,
       "nsVpnAILUsrL2tpPriDnsIp": nsVpnAILUsrL2tpPriDnsIp,
       "nsVpnAILUsrL2tpSecDnsIp": nsVpnAILUsrL2tpSecDnsIp,
       "nsVpnAILUsrL2tpPriWinsIp": nsVpnAILUsrL2tpPriWinsIp,
       "nsVpnAILUsrL2tpSecWinsIp": nsVpnAILUsrL2tpSecWinsIp,
       "nsVpnAILUsrVsys": nsVpnAILUsrVsys}
)
