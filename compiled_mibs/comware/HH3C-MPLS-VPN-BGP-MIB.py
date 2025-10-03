# SNMP MIB module (HH3C-MPLS-VPN-BGP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\comware\HH3C-MPLS-VPN-BGP-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:32:15 2025
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

(InetAddressType,) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
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

hh3cMplsVpnBgp = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 160)
)
if mibBuilder.loadTexts:
    hh3cMplsVpnBgp.setRevisions(
        ("2016-10-26 20:00",
         "2015-11-14 20:00",
         "2014-12-03 20:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class Hh3cMplsVpnId(TextualConvention, OctetString):
    status = "current"
    displayHint = "31a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )



class Hh3cMplsVpnRtDistinguisher(TextualConvention, OctetString):
    status = "current"
    displayHint = "256a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )



# MIB Managed Objects in the order of their OIDs

_Hh3cMplsVpnObjects_ObjectIdentity = ObjectIdentity
hh3cMplsVpnObjects = _Hh3cMplsVpnObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 160, 1)
)
_Hh3cMplsVpnConf_ObjectIdentity = ObjectIdentity
hh3cMplsVpnConf = _Hh3cMplsVpnConf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 160, 1, 1)
)
_Hh3cMplsVpnVrfConfTable_Object = MibTable
hh3cMplsVpnVrfConfTable = _Hh3cMplsVpnVrfConfTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 160, 1, 1, 1)
)
if mibBuilder.loadTexts:
    hh3cMplsVpnVrfConfTable.setStatus("current")
_Hh3cMplsVpnVrfConfEntry_Object = MibTableRow
hh3cMplsVpnVrfConfEntry = _Hh3cMplsVpnVrfConfEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 160, 1, 1, 1, 1)
)
hh3cMplsVpnVrfConfEntry.setIndexNames(
    (0, "HH3C-MPLS-VPN-BGP-MIB", "hh3cMplsVpnVrfName"),
)
if mibBuilder.loadTexts:
    hh3cMplsVpnVrfConfEntry.setStatus("current")
_Hh3cMplsVpnVrfName_Type = Hh3cMplsVpnId
_Hh3cMplsVpnVrfName_Object = MibTableColumn
hh3cMplsVpnVrfName = _Hh3cMplsVpnVrfName_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 160, 1, 1, 1, 1, 1),
    _Hh3cMplsVpnVrfName_Type()
)
hh3cMplsVpnVrfName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cMplsVpnVrfName.setStatus("current")
_Hh3cMplsVpnVrfRtDistinguisher_Type = Hh3cMplsVpnRtDistinguisher
_Hh3cMplsVpnVrfRtDistinguisher_Object = MibTableColumn
hh3cMplsVpnVrfRtDistinguisher = _Hh3cMplsVpnVrfRtDistinguisher_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 160, 1, 1, 1, 1, 2),
    _Hh3cMplsVpnVrfRtDistinguisher_Type()
)
hh3cMplsVpnVrfRtDistinguisher.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cMplsVpnVrfRtDistinguisher.setStatus("current")


class _Hh3cMplsVpnVrfNetPrefixType_Type(Integer32):
    """Custom type hh3cMplsVpnVrfNetPrefixType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("rip", 2),
          ("ospf", 3),
          ("isis", 4),
          ("bgp", 5),
          ("static", 6))
    )


_Hh3cMplsVpnVrfNetPrefixType_Type.__name__ = "Integer32"
_Hh3cMplsVpnVrfNetPrefixType_Object = MibTableColumn
hh3cMplsVpnVrfNetPrefixType = _Hh3cMplsVpnVrfNetPrefixType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 160, 1, 1, 1, 1, 3),
    _Hh3cMplsVpnVrfNetPrefixType_Type()
)
hh3cMplsVpnVrfNetPrefixType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cMplsVpnVrfNetPrefixType.setStatus("current")
_Hh3cMplsVpnVrfNetPrefix_Type = IpAddress
_Hh3cMplsVpnVrfNetPrefix_Object = MibTableColumn
hh3cMplsVpnVrfNetPrefix = _Hh3cMplsVpnVrfNetPrefix_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 160, 1, 1, 1, 1, 4),
    _Hh3cMplsVpnVrfNetPrefix_Type()
)
hh3cMplsVpnVrfNetPrefix.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cMplsVpnVrfNetPrefix.setStatus("current")
_Hh3cMplsVpnVrfIpRtRedistributeConn_Type = TruthValue
_Hh3cMplsVpnVrfIpRtRedistributeConn_Object = MibTableColumn
hh3cMplsVpnVrfIpRtRedistributeConn = _Hh3cMplsVpnVrfIpRtRedistributeConn_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 160, 1, 1, 1, 1, 5),
    _Hh3cMplsVpnVrfIpRtRedistributeConn_Type()
)
hh3cMplsVpnVrfIpRtRedistributeConn.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cMplsVpnVrfIpRtRedistributeConn.setStatus("current")
_Hh3cMplsVpnVrfIpRtRedistributeStatic_Type = TruthValue
_Hh3cMplsVpnVrfIpRtRedistributeStatic_Object = MibTableColumn
hh3cMplsVpnVrfIpRtRedistributeStatic = _Hh3cMplsVpnVrfIpRtRedistributeStatic_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 160, 1, 1, 1, 1, 6),
    _Hh3cMplsVpnVrfIpRtRedistributeStatic_Type()
)
hh3cMplsVpnVrfIpRtRedistributeStatic.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cMplsVpnVrfIpRtRedistributeStatic.setStatus("current")
_Hh3cMplsVpnVrfIpRtRedistributeRip_Type = TruthValue
_Hh3cMplsVpnVrfIpRtRedistributeRip_Object = MibTableColumn
hh3cMplsVpnVrfIpRtRedistributeRip = _Hh3cMplsVpnVrfIpRtRedistributeRip_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 160, 1, 1, 1, 1, 7),
    _Hh3cMplsVpnVrfIpRtRedistributeRip_Type()
)
hh3cMplsVpnVrfIpRtRedistributeRip.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cMplsVpnVrfIpRtRedistributeRip.setStatus("current")
_Hh3cMplsVpnVrfConfHighRtThreshold_Type = Unsigned32
_Hh3cMplsVpnVrfConfHighRtThreshold_Object = MibTableColumn
hh3cMplsVpnVrfConfHighRtThreshold = _Hh3cMplsVpnVrfConfHighRtThreshold_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 160, 1, 1, 1, 1, 8),
    _Hh3cMplsVpnVrfConfHighRtThreshold_Type()
)
hh3cMplsVpnVrfConfHighRtThreshold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cMplsVpnVrfConfHighRtThreshold.setStatus("current")
_Hh3cMplsVpnVrfConfIsWarnOnly_Type = TruthValue
_Hh3cMplsVpnVrfConfIsWarnOnly_Object = MibTableColumn
hh3cMplsVpnVrfConfIsWarnOnly = _Hh3cMplsVpnVrfConfIsWarnOnly_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 160, 1, 1, 1, 1, 9),
    _Hh3cMplsVpnVrfConfIsWarnOnly_Type()
)
hh3cMplsVpnVrfConfIsWarnOnly.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cMplsVpnVrfConfIsWarnOnly.setStatus("current")
_Hh3cMplsVpnVrfConfMaxRts_Type = Unsigned32
_Hh3cMplsVpnVrfConfMaxRts_Object = MibTableColumn
hh3cMplsVpnVrfConfMaxRts = _Hh3cMplsVpnVrfConfMaxRts_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 160, 1, 1, 1, 1, 10),
    _Hh3cMplsVpnVrfConfMaxRts_Type()
)
hh3cMplsVpnVrfConfMaxRts.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cMplsVpnVrfConfMaxRts.setStatus("current")
_Hh3cMplsVpnVrfConfRowStatus_Type = RowStatus
_Hh3cMplsVpnVrfConfRowStatus_Object = MibTableColumn
hh3cMplsVpnVrfConfRowStatus = _Hh3cMplsVpnVrfConfRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 160, 1, 1, 1, 1, 11),
    _Hh3cMplsVpnVrfConfRowStatus_Type()
)
hh3cMplsVpnVrfConfRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cMplsVpnVrfConfRowStatus.setStatus("current")
_Hh3cMplsVpnVrfBgpNbrAddrTable_Object = MibTable
hh3cMplsVpnVrfBgpNbrAddrTable = _Hh3cMplsVpnVrfBgpNbrAddrTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 160, 1, 1, 2)
)
if mibBuilder.loadTexts:
    hh3cMplsVpnVrfBgpNbrAddrTable.setStatus("current")
_Hh3cMplsVpnVrfBgpNbrAddrEntry_Object = MibTableRow
hh3cMplsVpnVrfBgpNbrAddrEntry = _Hh3cMplsVpnVrfBgpNbrAddrEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 160, 1, 1, 2, 1)
)
hh3cMplsVpnVrfBgpNbrAddrEntry.setIndexNames(
    (0, "HH3C-MPLS-VPN-BGP-MIB", "hh3cMplsVpnVrfName"),
    (0, "HH3C-MPLS-VPN-BGP-MIB", "hh3cMplsVpnVrfBgpNbrAddr"),
)
if mibBuilder.loadTexts:
    hh3cMplsVpnVrfBgpNbrAddrEntry.setStatus("current")
_Hh3cMplsVpnVrfBgpNbrAddr_Type = IpAddress
_Hh3cMplsVpnVrfBgpNbrAddr_Object = MibTableColumn
hh3cMplsVpnVrfBgpNbrAddr = _Hh3cMplsVpnVrfBgpNbrAddr_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 160, 1, 1, 2, 1, 1),
    _Hh3cMplsVpnVrfBgpNbrAddr_Type()
)
hh3cMplsVpnVrfBgpNbrAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cMplsVpnVrfBgpNbrAddr.setStatus("current")


class _Hh3cMplsVpnVrfBgpNbrRole_Type(Integer32):
    """Custom type hh3cMplsVpnVrfBgpNbrRole based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ce", 1),
          ("pe", 2))
    )


_Hh3cMplsVpnVrfBgpNbrRole_Type.__name__ = "Integer32"
_Hh3cMplsVpnVrfBgpNbrRole_Object = MibTableColumn
hh3cMplsVpnVrfBgpNbrRole = _Hh3cMplsVpnVrfBgpNbrRole_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 160, 1, 1, 2, 1, 2),
    _Hh3cMplsVpnVrfBgpNbrRole_Type()
)
hh3cMplsVpnVrfBgpNbrRole.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cMplsVpnVrfBgpNbrRole.setStatus("current")
_Hh3cMplsVpnVrfBgpNbrAsNumber_Type = Unsigned32
_Hh3cMplsVpnVrfBgpNbrAsNumber_Object = MibTableColumn
hh3cMplsVpnVrfBgpNbrAsNumber = _Hh3cMplsVpnVrfBgpNbrAsNumber_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 160, 1, 1, 2, 1, 3),
    _Hh3cMplsVpnVrfBgpNbrAsNumber_Type()
)
hh3cMplsVpnVrfBgpNbrAsNumber.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cMplsVpnVrfBgpNbrAsNumber.setStatus("current")


class _Hh3cMplsVpnVrfBgpNbrAdminStatus_Type(Integer32):
    """Custom type hh3cMplsVpnVrfBgpNbrAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("mplsVpnVrfBgpNbrSetUp", 1),
          ("mplsVpnVrfBgpNbrSetDown", 2))
    )


_Hh3cMplsVpnVrfBgpNbrAdminStatus_Type.__name__ = "Integer32"
_Hh3cMplsVpnVrfBgpNbrAdminStatus_Object = MibTableColumn
hh3cMplsVpnVrfBgpNbrAdminStatus = _Hh3cMplsVpnVrfBgpNbrAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 160, 1, 1, 2, 1, 4),
    _Hh3cMplsVpnVrfBgpNbrAdminStatus_Type()
)
hh3cMplsVpnVrfBgpNbrAdminStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cMplsVpnVrfBgpNbrAdminStatus.setStatus("current")
_Hh3cMplsVpnVrfBgpNbrRowStatus_Type = RowStatus
_Hh3cMplsVpnVrfBgpNbrRowStatus_Object = MibTableColumn
hh3cMplsVpnVrfBgpNbrRowStatus = _Hh3cMplsVpnVrfBgpNbrRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 160, 1, 1, 2, 1, 5),
    _Hh3cMplsVpnVrfBgpNbrRowStatus_Type()
)
hh3cMplsVpnVrfBgpNbrRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cMplsVpnVrfBgpNbrRowStatus.setStatus("current")


class _Hh3cMplsVpnVrfBgpNbrState_Type(Integer32):
    """Custom type hh3cMplsVpnVrfBgpNbrState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("idle", 1),
          ("connect", 2),
          ("active", 3),
          ("opensent", 4),
          ("openconfirm", 5),
          ("established", 6))
    )


_Hh3cMplsVpnVrfBgpNbrState_Type.__name__ = "Integer32"
_Hh3cMplsVpnVrfBgpNbrState_Object = MibTableColumn
hh3cMplsVpnVrfBgpNbrState = _Hh3cMplsVpnVrfBgpNbrState_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 160, 1, 1, 2, 1, 6),
    _Hh3cMplsVpnVrfBgpNbrState_Type()
)
hh3cMplsVpnVrfBgpNbrState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cMplsVpnVrfBgpNbrState.setStatus("current")
_Hh3cMplsVpnVrfBgpNbrPrefixTable_Object = MibTable
hh3cMplsVpnVrfBgpNbrPrefixTable = _Hh3cMplsVpnVrfBgpNbrPrefixTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 160, 1, 1, 3)
)
if mibBuilder.loadTexts:
    hh3cMplsVpnVrfBgpNbrPrefixTable.setStatus("current")
_Hh3cMplsVpnVrfBgpNbrPrefixEntry_Object = MibTableRow
hh3cMplsVpnVrfBgpNbrPrefixEntry = _Hh3cMplsVpnVrfBgpNbrPrefixEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 160, 1, 1, 3, 1)
)
hh3cMplsVpnVrfBgpNbrPrefixEntry.setIndexNames(
    (0, "HH3C-MPLS-VPN-BGP-MIB", "hh3cMplsVpnVrfName"),
    (0, "HH3C-MPLS-VPN-BGP-MIB", "hh3cMplsVpnVrfBgpPAtrPeer"),
    (0, "HH3C-MPLS-VPN-BGP-MIB", "hh3cMplsVpnVrfBgpPAtrIpAddrPrefixLen"),
    (0, "HH3C-MPLS-VPN-BGP-MIB", "hh3cMplsVpnVrfBgpPAtrIpAddrPrefix"),
)
if mibBuilder.loadTexts:
    hh3cMplsVpnVrfBgpNbrPrefixEntry.setStatus("current")
_Hh3cMplsVpnVrfBgpPAtrPeer_Type = IpAddress
_Hh3cMplsVpnVrfBgpPAtrPeer_Object = MibTableColumn
hh3cMplsVpnVrfBgpPAtrPeer = _Hh3cMplsVpnVrfBgpPAtrPeer_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 160, 1, 1, 3, 1, 1),
    _Hh3cMplsVpnVrfBgpPAtrPeer_Type()
)
hh3cMplsVpnVrfBgpPAtrPeer.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cMplsVpnVrfBgpPAtrPeer.setStatus("current")


class _Hh3cMplsVpnVrfBgpPAtrIpAddrPrefixLen_Type(Integer32):
    """Custom type hh3cMplsVpnVrfBgpPAtrIpAddrPrefixLen based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32),
    )


_Hh3cMplsVpnVrfBgpPAtrIpAddrPrefixLen_Type.__name__ = "Integer32"
_Hh3cMplsVpnVrfBgpPAtrIpAddrPrefixLen_Object = MibTableColumn
hh3cMplsVpnVrfBgpPAtrIpAddrPrefixLen = _Hh3cMplsVpnVrfBgpPAtrIpAddrPrefixLen_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 160, 1, 1, 3, 1, 2),
    _Hh3cMplsVpnVrfBgpPAtrIpAddrPrefixLen_Type()
)
hh3cMplsVpnVrfBgpPAtrIpAddrPrefixLen.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cMplsVpnVrfBgpPAtrIpAddrPrefixLen.setStatus("current")
_Hh3cMplsVpnVrfBgpPAtrIpAddrPrefix_Type = IpAddress
_Hh3cMplsVpnVrfBgpPAtrIpAddrPrefix_Object = MibTableColumn
hh3cMplsVpnVrfBgpPAtrIpAddrPrefix = _Hh3cMplsVpnVrfBgpPAtrIpAddrPrefix_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 160, 1, 1, 3, 1, 3),
    _Hh3cMplsVpnVrfBgpPAtrIpAddrPrefix_Type()
)
hh3cMplsVpnVrfBgpPAtrIpAddrPrefix.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cMplsVpnVrfBgpPAtrIpAddrPrefix.setStatus("current")
_Hh3cMplsVpnVrfBgpPAtrPeerType_Type = InetAddressType
_Hh3cMplsVpnVrfBgpPAtrPeerType_Object = MibTableColumn
hh3cMplsVpnVrfBgpPAtrPeerType = _Hh3cMplsVpnVrfBgpPAtrPeerType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 160, 1, 1, 3, 1, 4),
    _Hh3cMplsVpnVrfBgpPAtrPeerType_Type()
)
hh3cMplsVpnVrfBgpPAtrPeerType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cMplsVpnVrfBgpPAtrPeerType.setStatus("current")


class _Hh3cMplsVpnVrfBgpPAtrOrigin_Type(Integer32):
    """Custom type hh3cMplsVpnVrfBgpPAtrOrigin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("igp", 1),
          ("egp", 2),
          ("incomplete", 3))
    )


_Hh3cMplsVpnVrfBgpPAtrOrigin_Type.__name__ = "Integer32"
_Hh3cMplsVpnVrfBgpPAtrOrigin_Object = MibTableColumn
hh3cMplsVpnVrfBgpPAtrOrigin = _Hh3cMplsVpnVrfBgpPAtrOrigin_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 160, 1, 1, 3, 1, 5),
    _Hh3cMplsVpnVrfBgpPAtrOrigin_Type()
)
hh3cMplsVpnVrfBgpPAtrOrigin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cMplsVpnVrfBgpPAtrOrigin.setStatus("current")


class _Hh3cMplsVpnVrfBgpPAtrASPathSegment_Type(OctetString):
    """Custom type hh3cMplsVpnVrfBgpPAtrASPathSegment based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 255),
    )


_Hh3cMplsVpnVrfBgpPAtrASPathSegment_Type.__name__ = "OctetString"
_Hh3cMplsVpnVrfBgpPAtrASPathSegment_Object = MibTableColumn
hh3cMplsVpnVrfBgpPAtrASPathSegment = _Hh3cMplsVpnVrfBgpPAtrASPathSegment_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 160, 1, 1, 3, 1, 6),
    _Hh3cMplsVpnVrfBgpPAtrASPathSegment_Type()
)
hh3cMplsVpnVrfBgpPAtrASPathSegment.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cMplsVpnVrfBgpPAtrASPathSegment.setStatus("current")
_Hh3cMplsVpnVrfBgpPAtrNextHop_Type = IpAddress
_Hh3cMplsVpnVrfBgpPAtrNextHop_Object = MibTableColumn
hh3cMplsVpnVrfBgpPAtrNextHop = _Hh3cMplsVpnVrfBgpPAtrNextHop_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 160, 1, 1, 3, 1, 7),
    _Hh3cMplsVpnVrfBgpPAtrNextHop_Type()
)
hh3cMplsVpnVrfBgpPAtrNextHop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cMplsVpnVrfBgpPAtrNextHop.setStatus("current")


class _Hh3cMplsVpnVrfBgpPAtrMultiExitDisc_Type(Integer32):
    """Custom type hh3cMplsVpnVrfBgpPAtrMultiExitDisc based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_Hh3cMplsVpnVrfBgpPAtrMultiExitDisc_Type.__name__ = "Integer32"
_Hh3cMplsVpnVrfBgpPAtrMultiExitDisc_Object = MibTableColumn
hh3cMplsVpnVrfBgpPAtrMultiExitDisc = _Hh3cMplsVpnVrfBgpPAtrMultiExitDisc_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 160, 1, 1, 3, 1, 8),
    _Hh3cMplsVpnVrfBgpPAtrMultiExitDisc_Type()
)
hh3cMplsVpnVrfBgpPAtrMultiExitDisc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cMplsVpnVrfBgpPAtrMultiExitDisc.setStatus("current")


class _Hh3cMplsVpnVrfBgpPAtrLocalPref_Type(Integer32):
    """Custom type hh3cMplsVpnVrfBgpPAtrLocalPref based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_Hh3cMplsVpnVrfBgpPAtrLocalPref_Type.__name__ = "Integer32"
_Hh3cMplsVpnVrfBgpPAtrLocalPref_Object = MibTableColumn
hh3cMplsVpnVrfBgpPAtrLocalPref = _Hh3cMplsVpnVrfBgpPAtrLocalPref_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 160, 1, 1, 3, 1, 9),
    _Hh3cMplsVpnVrfBgpPAtrLocalPref_Type()
)
hh3cMplsVpnVrfBgpPAtrLocalPref.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cMplsVpnVrfBgpPAtrLocalPref.setStatus("current")


class _Hh3cMplsVpnVrfBgpPAtrAtomicAggregate_Type(Integer32):
    """Custom type hh3cMplsVpnVrfBgpPAtrAtomicAggregate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("lessSpecificRtNotSelected", 1),
          ("lessSpecificRtSelected", 2))
    )


_Hh3cMplsVpnVrfBgpPAtrAtomicAggregate_Type.__name__ = "Integer32"
_Hh3cMplsVpnVrfBgpPAtrAtomicAggregate_Object = MibTableColumn
hh3cMplsVpnVrfBgpPAtrAtomicAggregate = _Hh3cMplsVpnVrfBgpPAtrAtomicAggregate_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 160, 1, 1, 3, 1, 10),
    _Hh3cMplsVpnVrfBgpPAtrAtomicAggregate_Type()
)
hh3cMplsVpnVrfBgpPAtrAtomicAggregate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cMplsVpnVrfBgpPAtrAtomicAggregate.setStatus("current")


class _Hh3cMplsVpnVrfBgpPAtrAggregatorAS_Type(Integer32):
    """Custom type hh3cMplsVpnVrfBgpPAtrAggregatorAS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Hh3cMplsVpnVrfBgpPAtrAggregatorAS_Type.__name__ = "Integer32"
_Hh3cMplsVpnVrfBgpPAtrAggregatorAS_Object = MibTableColumn
hh3cMplsVpnVrfBgpPAtrAggregatorAS = _Hh3cMplsVpnVrfBgpPAtrAggregatorAS_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 160, 1, 1, 3, 1, 11),
    _Hh3cMplsVpnVrfBgpPAtrAggregatorAS_Type()
)
hh3cMplsVpnVrfBgpPAtrAggregatorAS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cMplsVpnVrfBgpPAtrAggregatorAS.setStatus("current")
_Hh3cMplsVpnVrfBgpPAtrAggregatorAddr_Type = IpAddress
_Hh3cMplsVpnVrfBgpPAtrAggregatorAddr_Object = MibTableColumn
hh3cMplsVpnVrfBgpPAtrAggregatorAddr = _Hh3cMplsVpnVrfBgpPAtrAggregatorAddr_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 160, 1, 1, 3, 1, 12),
    _Hh3cMplsVpnVrfBgpPAtrAggregatorAddr_Type()
)
hh3cMplsVpnVrfBgpPAtrAggregatorAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cMplsVpnVrfBgpPAtrAggregatorAddr.setStatus("current")


class _Hh3cMplsVpnVrfBgpPAtrCalcLocalPref_Type(Integer32):
    """Custom type hh3cMplsVpnVrfBgpPAtrCalcLocalPref based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_Hh3cMplsVpnVrfBgpPAtrCalcLocalPref_Type.__name__ = "Integer32"
_Hh3cMplsVpnVrfBgpPAtrCalcLocalPref_Object = MibTableColumn
hh3cMplsVpnVrfBgpPAtrCalcLocalPref = _Hh3cMplsVpnVrfBgpPAtrCalcLocalPref_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 160, 1, 1, 3, 1, 13),
    _Hh3cMplsVpnVrfBgpPAtrCalcLocalPref_Type()
)
hh3cMplsVpnVrfBgpPAtrCalcLocalPref.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cMplsVpnVrfBgpPAtrCalcLocalPref.setStatus("current")
_Hh3cMplsVpnVrfBgpPAtrBest_Type = TruthValue
_Hh3cMplsVpnVrfBgpPAtrBest_Object = MibTableColumn
hh3cMplsVpnVrfBgpPAtrBest = _Hh3cMplsVpnVrfBgpPAtrBest_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 160, 1, 1, 3, 1, 14),
    _Hh3cMplsVpnVrfBgpPAtrBest_Type()
)
hh3cMplsVpnVrfBgpPAtrBest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cMplsVpnVrfBgpPAtrBest.setStatus("current")


class _Hh3cMplsVpnVrfBgpPAtrUnknown_Type(OctetString):
    """Custom type hh3cMplsVpnVrfBgpPAtrUnknown based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_Hh3cMplsVpnVrfBgpPAtrUnknown_Type.__name__ = "OctetString"
_Hh3cMplsVpnVrfBgpPAtrUnknown_Object = MibTableColumn
hh3cMplsVpnVrfBgpPAtrUnknown = _Hh3cMplsVpnVrfBgpPAtrUnknown_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 160, 1, 1, 3, 1, 15),
    _Hh3cMplsVpnVrfBgpPAtrUnknown_Type()
)
hh3cMplsVpnVrfBgpPAtrUnknown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cMplsVpnVrfBgpPAtrUnknown.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HH3C-MPLS-VPN-BGP-MIB",
    **{"Hh3cMplsVpnId": Hh3cMplsVpnId,
       "Hh3cMplsVpnRtDistinguisher": Hh3cMplsVpnRtDistinguisher,
       "hh3cMplsVpnBgp": hh3cMplsVpnBgp,
       "hh3cMplsVpnObjects": hh3cMplsVpnObjects,
       "hh3cMplsVpnConf": hh3cMplsVpnConf,
       "hh3cMplsVpnVrfConfTable": hh3cMplsVpnVrfConfTable,
       "hh3cMplsVpnVrfConfEntry": hh3cMplsVpnVrfConfEntry,
       "hh3cMplsVpnVrfName": hh3cMplsVpnVrfName,
       "hh3cMplsVpnVrfRtDistinguisher": hh3cMplsVpnVrfRtDistinguisher,
       "hh3cMplsVpnVrfNetPrefixType": hh3cMplsVpnVrfNetPrefixType,
       "hh3cMplsVpnVrfNetPrefix": hh3cMplsVpnVrfNetPrefix,
       "hh3cMplsVpnVrfIpRtRedistributeConn": hh3cMplsVpnVrfIpRtRedistributeConn,
       "hh3cMplsVpnVrfIpRtRedistributeStatic": hh3cMplsVpnVrfIpRtRedistributeStatic,
       "hh3cMplsVpnVrfIpRtRedistributeRip": hh3cMplsVpnVrfIpRtRedistributeRip,
       "hh3cMplsVpnVrfConfHighRtThreshold": hh3cMplsVpnVrfConfHighRtThreshold,
       "hh3cMplsVpnVrfConfIsWarnOnly": hh3cMplsVpnVrfConfIsWarnOnly,
       "hh3cMplsVpnVrfConfMaxRts": hh3cMplsVpnVrfConfMaxRts,
       "hh3cMplsVpnVrfConfRowStatus": hh3cMplsVpnVrfConfRowStatus,
       "hh3cMplsVpnVrfBgpNbrAddrTable": hh3cMplsVpnVrfBgpNbrAddrTable,
       "hh3cMplsVpnVrfBgpNbrAddrEntry": hh3cMplsVpnVrfBgpNbrAddrEntry,
       "hh3cMplsVpnVrfBgpNbrAddr": hh3cMplsVpnVrfBgpNbrAddr,
       "hh3cMplsVpnVrfBgpNbrRole": hh3cMplsVpnVrfBgpNbrRole,
       "hh3cMplsVpnVrfBgpNbrAsNumber": hh3cMplsVpnVrfBgpNbrAsNumber,
       "hh3cMplsVpnVrfBgpNbrAdminStatus": hh3cMplsVpnVrfBgpNbrAdminStatus,
       "hh3cMplsVpnVrfBgpNbrRowStatus": hh3cMplsVpnVrfBgpNbrRowStatus,
       "hh3cMplsVpnVrfBgpNbrState": hh3cMplsVpnVrfBgpNbrState,
       "hh3cMplsVpnVrfBgpNbrPrefixTable": hh3cMplsVpnVrfBgpNbrPrefixTable,
       "hh3cMplsVpnVrfBgpNbrPrefixEntry": hh3cMplsVpnVrfBgpNbrPrefixEntry,
       "hh3cMplsVpnVrfBgpPAtrPeer": hh3cMplsVpnVrfBgpPAtrPeer,
       "hh3cMplsVpnVrfBgpPAtrIpAddrPrefixLen": hh3cMplsVpnVrfBgpPAtrIpAddrPrefixLen,
       "hh3cMplsVpnVrfBgpPAtrIpAddrPrefix": hh3cMplsVpnVrfBgpPAtrIpAddrPrefix,
       "hh3cMplsVpnVrfBgpPAtrPeerType": hh3cMplsVpnVrfBgpPAtrPeerType,
       "hh3cMplsVpnVrfBgpPAtrOrigin": hh3cMplsVpnVrfBgpPAtrOrigin,
       "hh3cMplsVpnVrfBgpPAtrASPathSegment": hh3cMplsVpnVrfBgpPAtrASPathSegment,
       "hh3cMplsVpnVrfBgpPAtrNextHop": hh3cMplsVpnVrfBgpPAtrNextHop,
       "hh3cMplsVpnVrfBgpPAtrMultiExitDisc": hh3cMplsVpnVrfBgpPAtrMultiExitDisc,
       "hh3cMplsVpnVrfBgpPAtrLocalPref": hh3cMplsVpnVrfBgpPAtrLocalPref,
       "hh3cMplsVpnVrfBgpPAtrAtomicAggregate": hh3cMplsVpnVrfBgpPAtrAtomicAggregate,
       "hh3cMplsVpnVrfBgpPAtrAggregatorAS": hh3cMplsVpnVrfBgpPAtrAggregatorAS,
       "hh3cMplsVpnVrfBgpPAtrAggregatorAddr": hh3cMplsVpnVrfBgpPAtrAggregatorAddr,
       "hh3cMplsVpnVrfBgpPAtrCalcLocalPref": hh3cMplsVpnVrfBgpPAtrCalcLocalPref,
       "hh3cMplsVpnVrfBgpPAtrBest": hh3cMplsVpnVrfBgpPAtrBest,
       "hh3cMplsVpnVrfBgpPAtrUnknown": hh3cMplsVpnVrfBgpPAtrUnknown}
)
