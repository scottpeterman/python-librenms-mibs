# SNMP MIB module (MPLS-MLDP-STD-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\junos\MPLS-MLDP-STD-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 12:05:16 2025
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

(IndexInteger,
 IndexIntegerNextFree) = mibBuilder.importSymbols(
    "DIFFSERV-MIB",
    "IndexInteger",
    "IndexIntegerNextFree")

(InterfaceIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex")

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

(jnxMldpExperiment,) = mibBuilder.importSymbols(
    "JUNIPER-EXPERIMENT-MIB",
    "jnxMldpExperiment")

(mplsLdpEntityIndex,
 mplsLdpEntityLdpId,
 mplsLdpPeerLdpId,
 mplsLdpSessionStatsEntry,
 mplsLdpStdMIB) = mibBuilder.importSymbols(
    "MPLS-LDP-STD-MIB",
    "mplsLdpEntityIndex",
    "mplsLdpEntityLdpId",
    "mplsLdpPeerLdpId",
    "mplsLdpSessionStatsEntry",
    "mplsLdpStdMIB")

(MplsIndexType,) = mibBuilder.importSymbols(
    "MPLS-LSR-STD-MIB",
    "MplsIndexType")

(MplsLdpIdentifier,
 mplsStdMIB) = mibBuilder.importSymbols(
    "MPLS-TC-STD-MIB",
    "MplsLdpIdentifier",
    "mplsStdMIB")

(ModuleCompliance,
 NotificationGroup,
 ObjectGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup",
    "ObjectGroup")

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
 StorageType,
 TextualConvention,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "StorageType",
    "TextualConvention",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY

mplsMldpStdMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 5, 13, 1)
)
if mibBuilder.loadTexts:
    mplsMldpStdMIB.setRevisions(
        ("2016-09-26 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_MplsMldpNotifications_ObjectIdentity = ObjectIdentity
mplsMldpNotifications = _MplsMldpNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 5, 13, 1, 0)
)
_MplsMldpScalars_ObjectIdentity = ObjectIdentity
mplsMldpScalars = _MplsMldpScalars_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 5, 13, 1, 1)
)


class _MplsMldpP2mpCapable_Type(Integer32):
    """Custom type mplsMldpP2mpCapable based on Integer32"""
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


_MplsMldpP2mpCapable_Type.__name__ = "Integer32"
_MplsMldpP2mpCapable_Object = MibScalar
mplsMldpP2mpCapable = _MplsMldpP2mpCapable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 13, 1, 1, 1),
    _MplsMldpP2mpCapable_Type()
)
mplsMldpP2mpCapable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsMldpP2mpCapable.setStatus("current")


class _MplsMldpMp2mpCapable_Type(Integer32):
    """Custom type mplsMldpMp2mpCapable based on Integer32"""
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


_MplsMldpMp2mpCapable_Type.__name__ = "Integer32"
_MplsMldpMp2mpCapable_Object = MibScalar
mplsMldpMp2mpCapable = _MplsMldpMp2mpCapable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 13, 1, 1, 2),
    _MplsMldpMp2mpCapable_Type()
)
mplsMldpMp2mpCapable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsMldpMp2mpCapable.setStatus("current")


class _MplsMldpMbbCapable_Type(Integer32):
    """Custom type mplsMldpMbbCapable based on Integer32"""
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


_MplsMldpMbbCapable_Type.__name__ = "Integer32"
_MplsMldpMbbCapable_Object = MibScalar
mplsMldpMbbCapable = _MplsMldpMbbCapable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 13, 1, 1, 3),
    _MplsMldpMbbCapable_Type()
)
mplsMldpMbbCapable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsMldpMbbCapable.setStatus("current")


class _MplsMldpMbbTime_Type(Unsigned32):
    """Custom type mplsMldpMbbTime based on Unsigned32"""
    defaultValue = 30

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 300),
    )


_MplsMldpMbbTime_Type.__name__ = "Unsigned32"
_MplsMldpMbbTime_Object = MibScalar
mplsMldpMbbTime = _MplsMldpMbbTime_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 13, 1, 1, 4),
    _MplsMldpMbbTime_Type()
)
mplsMldpMbbTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsMldpMbbTime.setStatus("current")
if mibBuilder.loadTexts:
    mplsMldpMbbTime.setUnits("seconds")
_MplsMldpNumFecs_Type = Unsigned32
_MplsMldpNumFecs_Object = MibScalar
mplsMldpNumFecs = _MplsMldpNumFecs_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 13, 1, 1, 5),
    _MplsMldpNumFecs_Type()
)
mplsMldpNumFecs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsMldpNumFecs.setStatus("current")
_MplsMldpNumFecsActive_Type = Unsigned32
_MplsMldpNumFecsActive_Object = MibScalar
mplsMldpNumFecsActive = _MplsMldpNumFecsActive_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 13, 1, 1, 6),
    _MplsMldpNumFecsActive_Type()
)
mplsMldpNumFecsActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsMldpNumFecsActive.setStatus("current")


class _MplsMldpPlrCapable_Type(Integer32):
    """Custom type mplsMldpPlrCapable based on Integer32"""
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


_MplsMldpPlrCapable_Type.__name__ = "Integer32"
_MplsMldpPlrCapable_Object = MibScalar
mplsMldpPlrCapable = _MplsMldpPlrCapable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 13, 1, 1, 7),
    _MplsMldpPlrCapable_Type()
)
mplsMldpPlrCapable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsMldpPlrCapable.setStatus("current")


class _MplsMldpMptCapable_Type(Integer32):
    """Custom type mplsMldpMptCapable based on Integer32"""
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


_MplsMldpMptCapable_Type.__name__ = "Integer32"
_MplsMldpMptCapable_Object = MibScalar
mplsMldpMptCapable = _MplsMldpMptCapable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 13, 1, 1, 8),
    _MplsMldpMptCapable_Type()
)
mplsMldpMptCapable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsMldpMptCapable.setStatus("current")


class _MplsMldpProtLsrCapable_Type(Integer32):
    """Custom type mplsMldpProtLsrCapable based on Integer32"""
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


_MplsMldpProtLsrCapable_Type.__name__ = "Integer32"
_MplsMldpProtLsrCapable_Object = MibScalar
mplsMldpProtLsrCapable = _MplsMldpProtLsrCapable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 13, 1, 1, 9),
    _MplsMldpProtLsrCapable_Type()
)
mplsMldpProtLsrCapable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsMldpProtLsrCapable.setStatus("current")


class _MplsMldpNodeProtCapable_Type(Integer32):
    """Custom type mplsMldpNodeProtCapable based on Integer32"""
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


_MplsMldpNodeProtCapable_Type.__name__ = "Integer32"
_MplsMldpNodeProtCapable_Object = MibScalar
mplsMldpNodeProtCapable = _MplsMldpNodeProtCapable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 13, 1, 1, 10),
    _MplsMldpNodeProtCapable_Type()
)
mplsMldpNodeProtCapable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsMldpNodeProtCapable.setStatus("current")
_MplsMldpObjects_ObjectIdentity = ObjectIdentity
mplsMldpObjects = _MplsMldpObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 5, 13, 1, 2)
)
_MplsLdpPeerCapabilityTable_Object = MibTable
mplsLdpPeerCapabilityTable = _MplsLdpPeerCapabilityTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 13, 1, 2, 1)
)
if mibBuilder.loadTexts:
    mplsLdpPeerCapabilityTable.setStatus("current")
_MplsLdpPeerCapabilityEntry_Object = MibTableRow
mplsLdpPeerCapabilityEntry = _MplsLdpPeerCapabilityEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 13, 1, 2, 1, 1)
)
mplsLdpPeerCapabilityEntry.setIndexNames(
    (0, "MPLS-LDP-STD-MIB", "mplsLdpEntityLdpId"),
    (0, "MPLS-LDP-STD-MIB", "mplsLdpEntityIndex"),
    (0, "MPLS-MLDP-STD-MIB", "mplsMldpPeerLdpId"),
)
if mibBuilder.loadTexts:
    mplsLdpPeerCapabilityEntry.setStatus("current")
_MplsMldpPeerLdpId_Type = MplsLdpIdentifier
_MplsMldpPeerLdpId_Object = MibTableColumn
mplsMldpPeerLdpId = _MplsMldpPeerLdpId_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 13, 1, 2, 1, 1, 1),
    _MplsMldpPeerLdpId_Type()
)
mplsMldpPeerLdpId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsMldpPeerLdpId.setStatus("current")


class _MplsLdpPeerCapability_Type(Bits):
    """Custom type mplsLdpPeerCapability based on Bits"""
    namedValues = NamedValues(
        *(("none", 0),
          ("p2mp", 1),
          ("mp2mp", 2),
          ("mbb", 3),
          ("upstream-label-assignment", 4),
          ("dynamic", 5),
          ("plr", 6),
          ("mpt", 7),
          ("prot-lsr", 8),
          ("node-prot", 9))
    )

_MplsLdpPeerCapability_Type.__name__ = "Bits"
_MplsLdpPeerCapability_Object = MibTableColumn
mplsLdpPeerCapability = _MplsLdpPeerCapability_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 13, 1, 2, 1, 1, 2),
    _MplsLdpPeerCapability_Type()
)
mplsLdpPeerCapability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsLdpPeerCapability.setStatus("current")
_MplsMldpSessionStatsTable_Object = MibTable
mplsMldpSessionStatsTable = _MplsMldpSessionStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 13, 1, 2, 2)
)
if mibBuilder.loadTexts:
    mplsMldpSessionStatsTable.setStatus("current")
_MplsMldpSessionStatsEntry_Object = MibTableRow
mplsMldpSessionStatsEntry = _MplsMldpSessionStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 13, 1, 2, 2, 1)
)
mplsMldpSessionStatsEntry.setIndexNames(
    (0, "MPLS-LDP-STD-MIB", "mplsLdpEntityLdpId"),
    (0, "MPLS-LDP-STD-MIB", "mplsLdpEntityIndex"),
    (0, "MPLS-LDP-STD-MIB", "mplsLdpPeerLdpId"),
)
if mibBuilder.loadTexts:
    mplsMldpSessionStatsEntry.setStatus("current")
_MplsMldpSessionStatsNumFecsSent_Type = Counter32
_MplsMldpSessionStatsNumFecsSent_Object = MibTableColumn
mplsMldpSessionStatsNumFecsSent = _MplsMldpSessionStatsNumFecsSent_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 13, 1, 2, 2, 1, 1),
    _MplsMldpSessionStatsNumFecsSent_Type()
)
mplsMldpSessionStatsNumFecsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsMldpSessionStatsNumFecsSent.setStatus("current")
_MplsMldpSessionStatsNumMbbReqSentState_Type = Counter32
_MplsMldpSessionStatsNumMbbReqSentState_Object = MibTableColumn
mplsMldpSessionStatsNumMbbReqSentState = _MplsMldpSessionStatsNumMbbReqSentState_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 13, 1, 2, 2, 1, 2),
    _MplsMldpSessionStatsNumMbbReqSentState_Type()
)
mplsMldpSessionStatsNumMbbReqSentState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsMldpSessionStatsNumMbbReqSentState.setStatus("current")
_MplsMldpSessionStatsNumFecsRcvd_Type = Counter32
_MplsMldpSessionStatsNumFecsRcvd_Object = MibTableColumn
mplsMldpSessionStatsNumFecsRcvd = _MplsMldpSessionStatsNumFecsRcvd_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 13, 1, 2, 2, 1, 3),
    _MplsMldpSessionStatsNumFecsRcvd_Type()
)
mplsMldpSessionStatsNumFecsRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsMldpSessionStatsNumFecsRcvd.setStatus("current")
_MplsMldpSessionStatsNumMbbReqRcvdState_Type = Counter32
_MplsMldpSessionStatsNumMbbReqRcvdState_Object = MibTableColumn
mplsMldpSessionStatsNumMbbReqRcvdState = _MplsMldpSessionStatsNumMbbReqRcvdState_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 13, 1, 2, 2, 1, 4),
    _MplsMldpSessionStatsNumMbbReqRcvdState_Type()
)
mplsMldpSessionStatsNumMbbReqRcvdState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsMldpSessionStatsNumMbbReqRcvdState.setStatus("current")
_MplsMldpSessionStatsNumMbbResetAckByTimer_Type = Counter32
_MplsMldpSessionStatsNumMbbResetAckByTimer_Object = MibTableColumn
mplsMldpSessionStatsNumMbbResetAckByTimer = _MplsMldpSessionStatsNumMbbResetAckByTimer_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 13, 1, 2, 2, 1, 5),
    _MplsMldpSessionStatsNumMbbResetAckByTimer_Type()
)
mplsMldpSessionStatsNumMbbResetAckByTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsMldpSessionStatsNumMbbResetAckByTimer.setStatus("current")
_MplsMldpFecTable_Object = MibTable
mplsMldpFecTable = _MplsMldpFecTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 13, 1, 2, 3)
)
if mibBuilder.loadTexts:
    mplsMldpFecTable.setStatus("current")
_MplsMldpFecEntry_Object = MibTableRow
mplsMldpFecEntry = _MplsMldpFecEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 13, 1, 2, 3, 1)
)
mplsMldpFecEntry.setIndexNames(
    (0, "MPLS-LDP-STD-MIB", "mplsLdpEntityLdpId"),
    (0, "MPLS-LDP-STD-MIB", "mplsLdpEntityIndex"),
    (0, "MPLS-MLDP-STD-MIB", "mplsMldpFecIndex"),
)
if mibBuilder.loadTexts:
    mplsMldpFecEntry.setStatus("current")
_MplsMldpFecIndex_Type = IndexInteger
_MplsMldpFecIndex_Object = MibTableColumn
mplsMldpFecIndex = _MplsMldpFecIndex_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 13, 1, 2, 3, 1, 1),
    _MplsMldpFecIndex_Type()
)
mplsMldpFecIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mplsMldpFecIndex.setStatus("current")


class _MplsMldpFecType_Type(Integer32):
    """Custom type mplsMldpFecType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(6,
              7,
              8)
        )
    )
    namedValues = NamedValues(
        *(("p2mp", 6),
          ("mp2mpUpstream", 7),
          ("mp2mpDownstream", 8))
    )


_MplsMldpFecType_Type.__name__ = "Integer32"
_MplsMldpFecType_Object = MibTableColumn
mplsMldpFecType = _MplsMldpFecType_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 13, 1, 2, 3, 1, 2),
    _MplsMldpFecType_Type()
)
mplsMldpFecType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsMldpFecType.setStatus("current")
_MplsMldpFecRootAddrType_Type = InetAddressType
_MplsMldpFecRootAddrType_Object = MibTableColumn
mplsMldpFecRootAddrType = _MplsMldpFecRootAddrType_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 13, 1, 2, 3, 1, 3),
    _MplsMldpFecRootAddrType_Type()
)
mplsMldpFecRootAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsMldpFecRootAddrType.setStatus("current")
_MplsMldpFecRootAddr_Type = InetAddress
_MplsMldpFecRootAddr_Object = MibTableColumn
mplsMldpFecRootAddr = _MplsMldpFecRootAddr_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 13, 1, 2, 3, 1, 4),
    _MplsMldpFecRootAddr_Type()
)
mplsMldpFecRootAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsMldpFecRootAddr.setStatus("current")


class _MplsMldpFecOpaqueType_Type(Integer32):
    """Custom type mplsMldpFecOpaqueType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("genericLspId", 1),
          ("transitIpv4Source", 3),
          ("transitIpv6Source", 4),
          ("transitIpv4Bidir", 5),
          ("transitIpv6Bidir", 6))
    )


_MplsMldpFecOpaqueType_Type.__name__ = "Integer32"
_MplsMldpFecOpaqueType_Object = MibTableColumn
mplsMldpFecOpaqueType = _MplsMldpFecOpaqueType_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 13, 1, 2, 3, 1, 5),
    _MplsMldpFecOpaqueType_Type()
)
mplsMldpFecOpaqueType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsMldpFecOpaqueType.setStatus("current")
_MplsMldpFecOpaqueGenLspId_Type = Unsigned32
_MplsMldpFecOpaqueGenLspId_Object = MibTableColumn
mplsMldpFecOpaqueGenLspId = _MplsMldpFecOpaqueGenLspId_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 13, 1, 2, 3, 1, 6),
    _MplsMldpFecOpaqueGenLspId_Type()
)
mplsMldpFecOpaqueGenLspId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsMldpFecOpaqueGenLspId.setStatus("current")
_MplsMldpFecOpaqueTransitSourceOrBidirAddrType_Type = InetAddressType
_MplsMldpFecOpaqueTransitSourceOrBidirAddrType_Object = MibTableColumn
mplsMldpFecOpaqueTransitSourceOrBidirAddrType = _MplsMldpFecOpaqueTransitSourceOrBidirAddrType_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 13, 1, 2, 3, 1, 7),
    _MplsMldpFecOpaqueTransitSourceOrBidirAddrType_Type()
)
mplsMldpFecOpaqueTransitSourceOrBidirAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsMldpFecOpaqueTransitSourceOrBidirAddrType.setStatus("current")
_MplsMldpFecOpaqueTransitSourceOrBidirAddr_Type = InetAddress
_MplsMldpFecOpaqueTransitSourceOrBidirAddr_Object = MibTableColumn
mplsMldpFecOpaqueTransitSourceOrBidirAddr = _MplsMldpFecOpaqueTransitSourceOrBidirAddr_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 13, 1, 2, 3, 1, 8),
    _MplsMldpFecOpaqueTransitSourceOrBidirAddr_Type()
)
mplsMldpFecOpaqueTransitSourceOrBidirAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsMldpFecOpaqueTransitSourceOrBidirAddr.setStatus("current")
_MplsMldpFecOpaqueTransitGroupAddrType_Type = InetAddressType
_MplsMldpFecOpaqueTransitGroupAddrType_Object = MibTableColumn
mplsMldpFecOpaqueTransitGroupAddrType = _MplsMldpFecOpaqueTransitGroupAddrType_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 13, 1, 2, 3, 1, 9),
    _MplsMldpFecOpaqueTransitGroupAddrType_Type()
)
mplsMldpFecOpaqueTransitGroupAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsMldpFecOpaqueTransitGroupAddrType.setStatus("current")
_MplsMldpFecOpaqueTransitGroupAddr_Type = InetAddress
_MplsMldpFecOpaqueTransitGroupAddr_Object = MibTableColumn
mplsMldpFecOpaqueTransitGroupAddr = _MplsMldpFecOpaqueTransitGroupAddr_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 13, 1, 2, 3, 1, 10),
    _MplsMldpFecOpaqueTransitGroupAddr_Type()
)
mplsMldpFecOpaqueTransitGroupAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsMldpFecOpaqueTransitGroupAddr.setStatus("current")


class _MplsMldpFecAdminStatus_Type(Integer32):
    """Custom type mplsMldpFecAdminStatus based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("up", 1),
          ("down", 2))
    )


_MplsMldpFecAdminStatus_Type.__name__ = "Integer32"
_MplsMldpFecAdminStatus_Object = MibTableColumn
mplsMldpFecAdminStatus = _MplsMldpFecAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 13, 1, 2, 3, 1, 11),
    _MplsMldpFecAdminStatus_Type()
)
mplsMldpFecAdminStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsMldpFecAdminStatus.setStatus("current")


class _MplsMldpFecOperStatus_Type(Integer32):
    """Custom type mplsMldpFecOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("up", 1),
          ("down", 2))
    )


_MplsMldpFecOperStatus_Type.__name__ = "Integer32"
_MplsMldpFecOperStatus_Object = MibTableColumn
mplsMldpFecOperStatus = _MplsMldpFecOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 13, 1, 2, 3, 1, 12),
    _MplsMldpFecOperStatus_Type()
)
mplsMldpFecOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsMldpFecOperStatus.setStatus("current")


class _MplsMldpFecMoFrr_Type(Integer32):
    """Custom type mplsMldpFecMoFrr based on Integer32"""
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


_MplsMldpFecMoFrr_Type.__name__ = "Integer32"
_MplsMldpFecMoFrr_Object = MibTableColumn
mplsMldpFecMoFrr = _MplsMldpFecMoFrr_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 13, 1, 2, 3, 1, 13),
    _MplsMldpFecMoFrr_Type()
)
mplsMldpFecMoFrr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsMldpFecMoFrr.setStatus("current")


class _MplsMldpFecLsrState_Type(Integer32):
    """Custom type mplsMldpFecLsrState based on Integer32"""
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
        *(("egress", 1),
          ("bud", 2),
          ("transit", 3),
          ("ingress", 4))
    )


_MplsMldpFecLsrState_Type.__name__ = "Integer32"
_MplsMldpFecLsrState_Object = MibTableColumn
mplsMldpFecLsrState = _MplsMldpFecLsrState_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 13, 1, 2, 3, 1, 14),
    _MplsMldpFecLsrState_Type()
)
mplsMldpFecLsrState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsMldpFecLsrState.setStatus("current")
_MplsMldpFecUpTime_Type = TimeStamp
_MplsMldpFecUpTime_Object = MibTableColumn
mplsMldpFecUpTime = _MplsMldpFecUpTime_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 13, 1, 2, 3, 1, 15),
    _MplsMldpFecUpTime_Type()
)
mplsMldpFecUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsMldpFecUpTime.setStatus("current")
_MplsMldpFecBranchStatsTable_Object = MibTable
mplsMldpFecBranchStatsTable = _MplsMldpFecBranchStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 13, 1, 2, 4)
)
if mibBuilder.loadTexts:
    mplsMldpFecBranchStatsTable.setStatus("current")
_MplsMldpFecBranchStatsEntry_Object = MibTableRow
mplsMldpFecBranchStatsEntry = _MplsMldpFecBranchStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 13, 1, 2, 4, 1)
)
mplsMldpFecBranchStatsEntry.setIndexNames(
    (0, "MPLS-LDP-STD-MIB", "mplsLdpEntityIndex"),
    (0, "MPLS-MLDP-STD-MIB", "mplsMldpFecBranchFecIndex"),
    (0, "MPLS-MLDP-STD-MIB", "mplsMldpFecBranchOutSegIndex"),
)
if mibBuilder.loadTexts:
    mplsMldpFecBranchStatsEntry.setStatus("current")
_MplsMldpFecBranchFecIndex_Type = MplsIndexType
_MplsMldpFecBranchFecIndex_Object = MibTableColumn
mplsMldpFecBranchFecIndex = _MplsMldpFecBranchFecIndex_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 13, 1, 2, 4, 1, 1),
    _MplsMldpFecBranchFecIndex_Type()
)
mplsMldpFecBranchFecIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mplsMldpFecBranchFecIndex.setStatus("current")
_MplsMldpFecBranchOutSegIndex_Type = MplsIndexType
_MplsMldpFecBranchOutSegIndex_Object = MibTableColumn
mplsMldpFecBranchOutSegIndex = _MplsMldpFecBranchOutSegIndex_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 13, 1, 2, 4, 1, 2),
    _MplsMldpFecBranchOutSegIndex_Type()
)
mplsMldpFecBranchOutSegIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mplsMldpFecBranchOutSegIndex.setStatus("current")
_MplsMldpFecBranchPeerLdpId_Type = MplsLdpIdentifier
_MplsMldpFecBranchPeerLdpId_Object = MibTableColumn
mplsMldpFecBranchPeerLdpId = _MplsMldpFecBranchPeerLdpId_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 13, 1, 2, 4, 1, 3),
    _MplsMldpFecBranchPeerLdpId_Type()
)
mplsMldpFecBranchPeerLdpId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsMldpFecBranchPeerLdpId.setStatus("current")
_MplsMldpFecBranchStatsPackets_Type = Counter64
_MplsMldpFecBranchStatsPackets_Object = MibTableColumn
mplsMldpFecBranchStatsPackets = _MplsMldpFecBranchStatsPackets_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 13, 1, 2, 4, 1, 4),
    _MplsMldpFecBranchStatsPackets_Type()
)
mplsMldpFecBranchStatsPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsMldpFecBranchStatsPackets.setStatus("current")
_MplsMldpFecBranchStatsBytes_Type = Counter64
_MplsMldpFecBranchStatsBytes_Object = MibTableColumn
mplsMldpFecBranchStatsBytes = _MplsMldpFecBranchStatsBytes_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 13, 1, 2, 4, 1, 5),
    _MplsMldpFecBranchStatsBytes_Type()
)
mplsMldpFecBranchStatsBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsMldpFecBranchStatsBytes.setStatus("current")
_MplsMldpFecBranchStatsDiscontinuityTime_Type = TimeStamp
_MplsMldpFecBranchStatsDiscontinuityTime_Object = MibTableColumn
mplsMldpFecBranchStatsDiscontinuityTime = _MplsMldpFecBranchStatsDiscontinuityTime_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 13, 1, 2, 4, 1, 6),
    _MplsMldpFecBranchStatsDiscontinuityTime_Type()
)
mplsMldpFecBranchStatsDiscontinuityTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsMldpFecBranchStatsDiscontinuityTime.setStatus("current")
_MplsMldpFecUpstreamSessTable_Object = MibTable
mplsMldpFecUpstreamSessTable = _MplsMldpFecUpstreamSessTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 13, 1, 2, 5)
)
if mibBuilder.loadTexts:
    mplsMldpFecUpstreamSessTable.setStatus("current")
_MplsMldpFecUpstreamSessEntry_Object = MibTableRow
mplsMldpFecUpstreamSessEntry = _MplsMldpFecUpstreamSessEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 13, 1, 2, 5, 1)
)
mplsMldpFecUpstreamSessEntry.setIndexNames(
    (0, "MPLS-LDP-STD-MIB", "mplsLdpEntityLdpId"),
    (0, "MPLS-LDP-STD-MIB", "mplsLdpEntityIndex"),
    (0, "MPLS-MLDP-STD-MIB", "mplsMldpFecUpstreamSessFecIndex"),
    (0, "MPLS-MLDP-STD-MIB", "mplsMldpFecUpstreamSessInSegIndex"),
)
if mibBuilder.loadTexts:
    mplsMldpFecUpstreamSessEntry.setStatus("current")
_MplsMldpFecUpstreamSessFecIndex_Type = MplsIndexType
_MplsMldpFecUpstreamSessFecIndex_Object = MibTableColumn
mplsMldpFecUpstreamSessFecIndex = _MplsMldpFecUpstreamSessFecIndex_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 13, 1, 2, 5, 1, 1),
    _MplsMldpFecUpstreamSessFecIndex_Type()
)
mplsMldpFecUpstreamSessFecIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mplsMldpFecUpstreamSessFecIndex.setStatus("current")
_MplsMldpFecUpstreamSessInSegIndex_Type = MplsIndexType
_MplsMldpFecUpstreamSessInSegIndex_Object = MibTableColumn
mplsMldpFecUpstreamSessInSegIndex = _MplsMldpFecUpstreamSessInSegIndex_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 13, 1, 2, 5, 1, 2),
    _MplsMldpFecUpstreamSessInSegIndex_Type()
)
mplsMldpFecUpstreamSessInSegIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mplsMldpFecUpstreamSessInSegIndex.setStatus("current")
_MplsMldpFecUpstreamSessPeerLdpId_Type = MplsLdpIdentifier
_MplsMldpFecUpstreamSessPeerLdpId_Object = MibTableColumn
mplsMldpFecUpstreamSessPeerLdpId = _MplsMldpFecUpstreamSessPeerLdpId_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 13, 1, 2, 5, 1, 3),
    _MplsMldpFecUpstreamSessPeerLdpId_Type()
)
mplsMldpFecUpstreamSessPeerLdpId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsMldpFecUpstreamSessPeerLdpId.setStatus("current")


class _MplsMldpFecUpstreamSessPrimary_Type(Integer32):
    """Custom type mplsMldpFecUpstreamSessPrimary based on Integer32"""
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


_MplsMldpFecUpstreamSessPrimary_Type.__name__ = "Integer32"
_MplsMldpFecUpstreamSessPrimary_Object = MibTableColumn
mplsMldpFecUpstreamSessPrimary = _MplsMldpFecUpstreamSessPrimary_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 13, 1, 2, 5, 1, 4),
    _MplsMldpFecUpstreamSessPrimary_Type()
)
mplsMldpFecUpstreamSessPrimary.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsMldpFecUpstreamSessPrimary.setStatus("current")


class _MplsMldpFecUpstreamSessActive_Type(Integer32):
    """Custom type mplsMldpFecUpstreamSessActive based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("inactive", 2))
    )


_MplsMldpFecUpstreamSessActive_Type.__name__ = "Integer32"
_MplsMldpFecUpstreamSessActive_Object = MibTableColumn
mplsMldpFecUpstreamSessActive = _MplsMldpFecUpstreamSessActive_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 13, 1, 2, 5, 1, 5),
    _MplsMldpFecUpstreamSessActive_Type()
)
mplsMldpFecUpstreamSessActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsMldpFecUpstreamSessActive.setStatus("current")
_MplsMldpFecUpstreamSessPackets_Type = Counter64
_MplsMldpFecUpstreamSessPackets_Object = MibTableColumn
mplsMldpFecUpstreamSessPackets = _MplsMldpFecUpstreamSessPackets_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 13, 1, 2, 5, 1, 6),
    _MplsMldpFecUpstreamSessPackets_Type()
)
mplsMldpFecUpstreamSessPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsMldpFecUpstreamSessPackets.setStatus("current")
_MplsMldpFecUpstreamSessBytes_Type = Counter64
_MplsMldpFecUpstreamSessBytes_Object = MibTableColumn
mplsMldpFecUpstreamSessBytes = _MplsMldpFecUpstreamSessBytes_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 13, 1, 2, 5, 1, 7),
    _MplsMldpFecUpstreamSessBytes_Type()
)
mplsMldpFecUpstreamSessBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsMldpFecUpstreamSessBytes.setStatus("current")
_MplsMldpFecUpstreamSessDiscontinuityTime_Type = TimeStamp
_MplsMldpFecUpstreamSessDiscontinuityTime_Object = MibTableColumn
mplsMldpFecUpstreamSessDiscontinuityTime = _MplsMldpFecUpstreamSessDiscontinuityTime_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 13, 1, 2, 5, 1, 8),
    _MplsMldpFecUpstreamSessDiscontinuityTime_Type()
)
mplsMldpFecUpstreamSessDiscontinuityTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsMldpFecUpstreamSessDiscontinuityTime.setStatus("current")
_MplsMldpInterfaceStatsTable_Object = MibTable
mplsMldpInterfaceStatsTable = _MplsMldpInterfaceStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 13, 1, 2, 6)
)
if mibBuilder.loadTexts:
    mplsMldpInterfaceStatsTable.setStatus("current")
_MplsMldpInterfaceStatsEntry_Object = MibTableRow
mplsMldpInterfaceStatsEntry = _MplsMldpInterfaceStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 13, 1, 2, 6, 1)
)
mplsMldpInterfaceStatsEntry.setIndexNames(
    (0, "MPLS-MLDP-STD-MIB", "mplsMldpInterfaceIndex"),
)
if mibBuilder.loadTexts:
    mplsMldpInterfaceStatsEntry.setStatus("current")
_MplsMldpInterfaceIndex_Type = InterfaceIndex
_MplsMldpInterfaceIndex_Object = MibTableColumn
mplsMldpInterfaceIndex = _MplsMldpInterfaceIndex_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 13, 1, 2, 6, 1, 1),
    _MplsMldpInterfaceIndex_Type()
)
mplsMldpInterfaceIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mplsMldpInterfaceIndex.setStatus("current")
_MplsMldpInterfaceStatsSentPackets_Type = Counter64
_MplsMldpInterfaceStatsSentPackets_Object = MibTableColumn
mplsMldpInterfaceStatsSentPackets = _MplsMldpInterfaceStatsSentPackets_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 13, 1, 2, 6, 1, 2),
    _MplsMldpInterfaceStatsSentPackets_Type()
)
mplsMldpInterfaceStatsSentPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsMldpInterfaceStatsSentPackets.setStatus("current")
_MplsMldpInterfaceStatsSentBytes_Type = Counter64
_MplsMldpInterfaceStatsSentBytes_Object = MibTableColumn
mplsMldpInterfaceStatsSentBytes = _MplsMldpInterfaceStatsSentBytes_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 13, 1, 2, 6, 1, 3),
    _MplsMldpInterfaceStatsSentBytes_Type()
)
mplsMldpInterfaceStatsSentBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsMldpInterfaceStatsSentBytes.setStatus("current")
_MplsMldpInterfaceStatsRecvPackets_Type = Counter64
_MplsMldpInterfaceStatsRecvPackets_Object = MibTableColumn
mplsMldpInterfaceStatsRecvPackets = _MplsMldpInterfaceStatsRecvPackets_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 13, 1, 2, 6, 1, 4),
    _MplsMldpInterfaceStatsRecvPackets_Type()
)
mplsMldpInterfaceStatsRecvPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsMldpInterfaceStatsRecvPackets.setStatus("current")
_MplsMldpInterfaceStatsRecvBytes_Type = Counter64
_MplsMldpInterfaceStatsRecvBytes_Object = MibTableColumn
mplsMldpInterfaceStatsRecvBytes = _MplsMldpInterfaceStatsRecvBytes_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 13, 1, 2, 6, 1, 5),
    _MplsMldpInterfaceStatsRecvBytes_Type()
)
mplsMldpInterfaceStatsRecvBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsMldpInterfaceStatsRecvBytes.setStatus("current")

# Managed Objects groups


# Notification objects

mplsMldpFecUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 5, 13, 1, 0, 1)
)
mplsMldpFecUp.setObjects(
      *(("MPLS-MLDP-STD-MIB", "mplsMldpFecAdminStatus"),
        ("MPLS-MLDP-STD-MIB", "mplsMldpFecOperStatus"))
)
if mibBuilder.loadTexts:
    mplsMldpFecUp.setStatus(
        "current"
    )

mplsMldpFecDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 5, 13, 1, 0, 2)
)
mplsMldpFecDown.setObjects(
      *(("MPLS-MLDP-STD-MIB", "mplsMldpFecAdminStatus"),
        ("MPLS-MLDP-STD-MIB", "mplsMldpFecOperStatus"))
)
if mibBuilder.loadTexts:
    mplsMldpFecDown.setStatus(
        "current"
    )

mplsMldpMoFrrStatusChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 5, 13, 1, 0, 3)
)
mplsMldpMoFrrStatusChange.setObjects(
    ("MPLS-MLDP-STD-MIB", "mplsMldpFecUpstreamSessPrimary")
)
if mibBuilder.loadTexts:
    mplsMldpMoFrrStatusChange.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "MPLS-MLDP-STD-MIB",
    **{"mplsMldpStdMIB": mplsMldpStdMIB,
       "mplsMldpNotifications": mplsMldpNotifications,
       "mplsMldpFecUp": mplsMldpFecUp,
       "mplsMldpFecDown": mplsMldpFecDown,
       "mplsMldpMoFrrStatusChange": mplsMldpMoFrrStatusChange,
       "mplsMldpScalars": mplsMldpScalars,
       "mplsMldpP2mpCapable": mplsMldpP2mpCapable,
       "mplsMldpMp2mpCapable": mplsMldpMp2mpCapable,
       "mplsMldpMbbCapable": mplsMldpMbbCapable,
       "mplsMldpMbbTime": mplsMldpMbbTime,
       "mplsMldpNumFecs": mplsMldpNumFecs,
       "mplsMldpNumFecsActive": mplsMldpNumFecsActive,
       "mplsMldpPlrCapable": mplsMldpPlrCapable,
       "mplsMldpMptCapable": mplsMldpMptCapable,
       "mplsMldpProtLsrCapable": mplsMldpProtLsrCapable,
       "mplsMldpNodeProtCapable": mplsMldpNodeProtCapable,
       "mplsMldpObjects": mplsMldpObjects,
       "mplsLdpPeerCapabilityTable": mplsLdpPeerCapabilityTable,
       "mplsLdpPeerCapabilityEntry": mplsLdpPeerCapabilityEntry,
       "mplsMldpPeerLdpId": mplsMldpPeerLdpId,
       "mplsLdpPeerCapability": mplsLdpPeerCapability,
       "mplsMldpSessionStatsTable": mplsMldpSessionStatsTable,
       "mplsMldpSessionStatsEntry": mplsMldpSessionStatsEntry,
       "mplsMldpSessionStatsNumFecsSent": mplsMldpSessionStatsNumFecsSent,
       "mplsMldpSessionStatsNumMbbReqSentState": mplsMldpSessionStatsNumMbbReqSentState,
       "mplsMldpSessionStatsNumFecsRcvd": mplsMldpSessionStatsNumFecsRcvd,
       "mplsMldpSessionStatsNumMbbReqRcvdState": mplsMldpSessionStatsNumMbbReqRcvdState,
       "mplsMldpSessionStatsNumMbbResetAckByTimer": mplsMldpSessionStatsNumMbbResetAckByTimer,
       "mplsMldpFecTable": mplsMldpFecTable,
       "mplsMldpFecEntry": mplsMldpFecEntry,
       "mplsMldpFecIndex": mplsMldpFecIndex,
       "mplsMldpFecType": mplsMldpFecType,
       "mplsMldpFecRootAddrType": mplsMldpFecRootAddrType,
       "mplsMldpFecRootAddr": mplsMldpFecRootAddr,
       "mplsMldpFecOpaqueType": mplsMldpFecOpaqueType,
       "mplsMldpFecOpaqueGenLspId": mplsMldpFecOpaqueGenLspId,
       "mplsMldpFecOpaqueTransitSourceOrBidirAddrType": mplsMldpFecOpaqueTransitSourceOrBidirAddrType,
       "mplsMldpFecOpaqueTransitSourceOrBidirAddr": mplsMldpFecOpaqueTransitSourceOrBidirAddr,
       "mplsMldpFecOpaqueTransitGroupAddrType": mplsMldpFecOpaqueTransitGroupAddrType,
       "mplsMldpFecOpaqueTransitGroupAddr": mplsMldpFecOpaqueTransitGroupAddr,
       "mplsMldpFecAdminStatus": mplsMldpFecAdminStatus,
       "mplsMldpFecOperStatus": mplsMldpFecOperStatus,
       "mplsMldpFecMoFrr": mplsMldpFecMoFrr,
       "mplsMldpFecLsrState": mplsMldpFecLsrState,
       "mplsMldpFecUpTime": mplsMldpFecUpTime,
       "mplsMldpFecBranchStatsTable": mplsMldpFecBranchStatsTable,
       "mplsMldpFecBranchStatsEntry": mplsMldpFecBranchStatsEntry,
       "mplsMldpFecBranchFecIndex": mplsMldpFecBranchFecIndex,
       "mplsMldpFecBranchOutSegIndex": mplsMldpFecBranchOutSegIndex,
       "mplsMldpFecBranchPeerLdpId": mplsMldpFecBranchPeerLdpId,
       "mplsMldpFecBranchStatsPackets": mplsMldpFecBranchStatsPackets,
       "mplsMldpFecBranchStatsBytes": mplsMldpFecBranchStatsBytes,
       "mplsMldpFecBranchStatsDiscontinuityTime": mplsMldpFecBranchStatsDiscontinuityTime,
       "mplsMldpFecUpstreamSessTable": mplsMldpFecUpstreamSessTable,
       "mplsMldpFecUpstreamSessEntry": mplsMldpFecUpstreamSessEntry,
       "mplsMldpFecUpstreamSessFecIndex": mplsMldpFecUpstreamSessFecIndex,
       "mplsMldpFecUpstreamSessInSegIndex": mplsMldpFecUpstreamSessInSegIndex,
       "mplsMldpFecUpstreamSessPeerLdpId": mplsMldpFecUpstreamSessPeerLdpId,
       "mplsMldpFecUpstreamSessPrimary": mplsMldpFecUpstreamSessPrimary,
       "mplsMldpFecUpstreamSessActive": mplsMldpFecUpstreamSessActive,
       "mplsMldpFecUpstreamSessPackets": mplsMldpFecUpstreamSessPackets,
       "mplsMldpFecUpstreamSessBytes": mplsMldpFecUpstreamSessBytes,
       "mplsMldpFecUpstreamSessDiscontinuityTime": mplsMldpFecUpstreamSessDiscontinuityTime,
       "mplsMldpInterfaceStatsTable": mplsMldpInterfaceStatsTable,
       "mplsMldpInterfaceStatsEntry": mplsMldpInterfaceStatsEntry,
       "mplsMldpInterfaceIndex": mplsMldpInterfaceIndex,
       "mplsMldpInterfaceStatsSentPackets": mplsMldpInterfaceStatsSentPackets,
       "mplsMldpInterfaceStatsSentBytes": mplsMldpInterfaceStatsSentBytes,
       "mplsMldpInterfaceStatsRecvPackets": mplsMldpInterfaceStatsRecvPackets,
       "mplsMldpInterfaceStatsRecvBytes": mplsMldpInterfaceStatsRecvBytes}
)
