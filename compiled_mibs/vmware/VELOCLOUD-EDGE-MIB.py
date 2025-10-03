# SNMP MIB module (VELOCLOUD-EDGE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\vmware\VELOCLOUD-EDGE-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 12:34:13 2025
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

(InterfaceIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex")

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention",
    "TruthValue")

(UUID,) = mibBuilder.importSymbols(
    "UUID-TC-MIB",
    "UUID")

(modules,) = mibBuilder.importSymbols(
    "VELOCLOUD-MIB",
    "modules")


# MODULE-IDENTITY

edge = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 45346, 1, 1)
)
if mibBuilder.loadTexts:
    edge.setRevisions(
        ("2019-08-02 00:00",
         "2017-01-18 00:00",
         "2017-01-13 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class VceHaAdminStateType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("theVelocloudActiveStandbyPair", 2),
          ("theVeloCloudCluster", 3),
          ("nonVeloCloudVrrpPair", 4),
          ("unknown", 5))
    )



class VceHaPeerStateType(TextualConvention, Integer32):
    status = "current"
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
        *(("initializing", 1),
          ("active", 2),
          ("standby", 3),
          ("unknown", 4))
    )



class VceLinkStateType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8)
        )
    )
    namedValues = NamedValues(
        *(("initial", 1),
          ("dead", 2),
          ("unusable", 3),
          ("quiet", 4),
          ("standby", 5),
          ("unstable", 6),
          ("stable", 7),
          ("unknown", 8))
    )



class VcePathStateType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15)
        )
    )
    namedValues = NamedValues(
        *(("initial", 1),
          ("dead", 2),
          ("unusable", 3),
          ("quiet", 4),
          ("unstable", 5),
          ("bwUnmeasurable", 6),
          ("waitingForLinkbw", 7),
          ("measuringTxBw", 8),
          ("measuringRxBw", 9),
          ("stable", 10),
          ("active", 11),
          ("upHsby", 12),
          ("idleHsby", 13),
          ("backup", 14),
          ("unknown", 15))
    )



class VcePathTunlModeType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("default", 1),
          ("trusted", 2),
          ("untrustedTransport", 3),
          ("untrustedTunnel", 4),
          ("unknown", 5))
    )



class VceArpStateType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("reachable", 1),
          ("stale", 2),
          ("invalid", 5),
          ("unknown", 6),
          ("incomplete", 7))
    )



# MIB Managed Objects in the order of their OIDs

_VceEdgeObject_ObjectIdentity = ObjectIdentity
vceEdgeObject = _VceEdgeObject_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45346, 1, 1, 2)
)
_VceHA_ObjectIdentity = ObjectIdentity
vceHA = _VceHA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45346, 1, 1, 2, 1)
)
_VceHAObject_ObjectIdentity = ObjectIdentity
vceHAObject = _VceHAObject_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45346, 1, 1, 2, 1, 2)
)
_VceHaAdminState_Type = VceHaAdminStateType
_VceHaAdminState_Object = MibScalar
vceHaAdminState = _VceHaAdminState_Object(
    (1, 3, 6, 1, 4, 1, 45346, 1, 1, 2, 1, 2, 1),
    _VceHaAdminState_Type()
)
vceHaAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vceHaAdminState.setStatus("current")
_VceHaPeerState_Type = VceHaPeerStateType
_VceHaPeerState_Object = MibScalar
vceHaPeerState = _VceHaPeerState_Object(
    (1, 3, 6, 1, 4, 1, 45346, 1, 1, 2, 1, 2, 2),
    _VceHaPeerState_Type()
)
vceHaPeerState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vceHaPeerState.setStatus("current")
_VceHaActiveWanItfNum_Type = Integer32
_VceHaActiveWanItfNum_Object = MibScalar
vceHaActiveWanItfNum = _VceHaActiveWanItfNum_Object(
    (1, 3, 6, 1, 4, 1, 45346, 1, 1, 2, 1, 2, 3),
    _VceHaActiveWanItfNum_Type()
)
vceHaActiveWanItfNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vceHaActiveWanItfNum.setStatus("current")
_VceHaActiveLanItfNum_Type = Integer32
_VceHaActiveLanItfNum_Object = MibScalar
vceHaActiveLanItfNum = _VceHaActiveLanItfNum_Object(
    (1, 3, 6, 1, 4, 1, 45346, 1, 1, 2, 1, 2, 4),
    _VceHaActiveLanItfNum_Type()
)
vceHaActiveLanItfNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vceHaActiveLanItfNum.setStatus("current")
_VceHaStanbyWanItfNum_Type = Integer32
_VceHaStanbyWanItfNum_Object = MibScalar
vceHaStanbyWanItfNum = _VceHaStanbyWanItfNum_Object(
    (1, 3, 6, 1, 4, 1, 45346, 1, 1, 2, 1, 2, 5),
    _VceHaStanbyWanItfNum_Type()
)
vceHaStanbyWanItfNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vceHaStanbyWanItfNum.setStatus("current")
_VceHaStanbyLanItfNum_Type = Integer32
_VceHaStanbyLanItfNum_Object = MibScalar
vceHaStanbyLanItfNum = _VceHaStanbyLanItfNum_Object(
    (1, 3, 6, 1, 4, 1, 45346, 1, 1, 2, 1, 2, 6),
    _VceHaStanbyLanItfNum_Type()
)
vceHaStanbyLanItfNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vceHaStanbyLanItfNum.setStatus("current")
_VceHealth_ObjectIdentity = ObjectIdentity
vceHealth = _VceHealth_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45346, 1, 1, 2, 2)
)
_VceHealthObject_ObjectIdentity = ObjectIdentity
vceHealthObject = _VceHealthObject_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45346, 1, 1, 2, 2, 2)
)
_VceCpuUtilPct5min_Type = Integer32
_VceCpuUtilPct5min_Object = MibScalar
vceCpuUtilPct5min = _VceCpuUtilPct5min_Object(
    (1, 3, 6, 1, 4, 1, 45346, 1, 1, 2, 2, 2, 1),
    _VceCpuUtilPct5min_Type()
)
vceCpuUtilPct5min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vceCpuUtilPct5min.setStatus("current")
_VceCpuUtilPct30sec_Type = Integer32
_VceCpuUtilPct30sec_Object = MibScalar
vceCpuUtilPct30sec = _VceCpuUtilPct30sec_Object(
    (1, 3, 6, 1, 4, 1, 45346, 1, 1, 2, 2, 2, 2),
    _VceCpuUtilPct30sec_Type()
)
vceCpuUtilPct30sec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vceCpuUtilPct30sec.setStatus("current")
_VceMemUsedPct_Type = Integer32
_VceMemUsedPct_Object = MibScalar
vceMemUsedPct = _VceMemUsedPct_Object(
    (1, 3, 6, 1, 4, 1, 45346, 1, 1, 2, 2, 2, 3),
    _VceMemUsedPct_Type()
)
vceMemUsedPct.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vceMemUsedPct.setStatus("current")
_VceLink_ObjectIdentity = ObjectIdentity
vceLink = _VceLink_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45346, 1, 1, 2, 3)
)
_VceLinkObject_ObjectIdentity = ObjectIdentity
vceLinkObject = _VceLinkObject_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45346, 1, 1, 2, 3, 2)
)
_VceLinkNum_Type = Integer32
_VceLinkNum_Object = MibScalar
vceLinkNum = _VceLinkNum_Object(
    (1, 3, 6, 1, 4, 1, 45346, 1, 1, 2, 3, 2, 1),
    _VceLinkNum_Type()
)
vceLinkNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vceLinkNum.setStatus("current")
_VceLinkTable_Object = MibTable
vceLinkTable = _VceLinkTable_Object(
    (1, 3, 6, 1, 4, 1, 45346, 1, 1, 2, 3, 2, 2)
)
if mibBuilder.loadTexts:
    vceLinkTable.setStatus("current")
_VceLinkEntry_Object = MibTableRow
vceLinkEntry = _VceLinkEntry_Object(
    (1, 3, 6, 1, 4, 1, 45346, 1, 1, 2, 3, 2, 2, 1)
)
vceLinkEntry.setIndexNames(
    (0, "VELOCLOUD-EDGE-MIB", "vceLinkIntId"),
)
if mibBuilder.loadTexts:
    vceLinkEntry.setStatus("current")
_VceLinkIntId_Type = UUID
_VceLinkIntId_Object = MibTableColumn
vceLinkIntId = _VceLinkIntId_Object(
    (1, 3, 6, 1, 4, 1, 45346, 1, 1, 2, 3, 2, 2, 1, 2),
    _VceLinkIntId_Type()
)
vceLinkIntId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vceLinkIntId.setStatus("current")
_VceLinkName_Type = DisplayString
_VceLinkName_Object = MibTableColumn
vceLinkName = _VceLinkName_Object(
    (1, 3, 6, 1, 4, 1, 45346, 1, 1, 2, 3, 2, 2, 1, 3),
    _VceLinkName_Type()
)
vceLinkName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vceLinkName.setStatus("current")
_VceLinkTxP1Pkt_Type = Counter64
_VceLinkTxP1Pkt_Object = MibTableColumn
vceLinkTxP1Pkt = _VceLinkTxP1Pkt_Object(
    (1, 3, 6, 1, 4, 1, 45346, 1, 1, 2, 3, 2, 2, 1, 4),
    _VceLinkTxP1Pkt_Type()
)
vceLinkTxP1Pkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vceLinkTxP1Pkt.setStatus("current")
_VceLinkRxP1Pkt_Type = Counter64
_VceLinkRxP1Pkt_Object = MibTableColumn
vceLinkRxP1Pkt = _VceLinkRxP1Pkt_Object(
    (1, 3, 6, 1, 4, 1, 45346, 1, 1, 2, 3, 2, 2, 1, 5),
    _VceLinkRxP1Pkt_Type()
)
vceLinkRxP1Pkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vceLinkRxP1Pkt.setStatus("current")
_VceLinkTxP1Bytes_Type = Counter64
_VceLinkTxP1Bytes_Object = MibTableColumn
vceLinkTxP1Bytes = _VceLinkTxP1Bytes_Object(
    (1, 3, 6, 1, 4, 1, 45346, 1, 1, 2, 3, 2, 2, 1, 6),
    _VceLinkTxP1Bytes_Type()
)
vceLinkTxP1Bytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vceLinkTxP1Bytes.setStatus("current")
_VceLinkRxP1Bytes_Type = Counter64
_VceLinkRxP1Bytes_Object = MibTableColumn
vceLinkRxP1Bytes = _VceLinkRxP1Bytes_Object(
    (1, 3, 6, 1, 4, 1, 45346, 1, 1, 2, 3, 2, 2, 1, 7),
    _VceLinkRxP1Bytes_Type()
)
vceLinkRxP1Bytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vceLinkRxP1Bytes.setStatus("current")
_VceLinkTxP2Pkt_Type = Counter64
_VceLinkTxP2Pkt_Object = MibTableColumn
vceLinkTxP2Pkt = _VceLinkTxP2Pkt_Object(
    (1, 3, 6, 1, 4, 1, 45346, 1, 1, 2, 3, 2, 2, 1, 8),
    _VceLinkTxP2Pkt_Type()
)
vceLinkTxP2Pkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vceLinkTxP2Pkt.setStatus("current")
_VceLinkRxP2Pkt_Type = Counter64
_VceLinkRxP2Pkt_Object = MibTableColumn
vceLinkRxP2Pkt = _VceLinkRxP2Pkt_Object(
    (1, 3, 6, 1, 4, 1, 45346, 1, 1, 2, 3, 2, 2, 1, 9),
    _VceLinkRxP2Pkt_Type()
)
vceLinkRxP2Pkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vceLinkRxP2Pkt.setStatus("current")
_VceLinkTxP2Bytes_Type = Counter64
_VceLinkTxP2Bytes_Object = MibTableColumn
vceLinkTxP2Bytes = _VceLinkTxP2Bytes_Object(
    (1, 3, 6, 1, 4, 1, 45346, 1, 1, 2, 3, 2, 2, 1, 10),
    _VceLinkTxP2Bytes_Type()
)
vceLinkTxP2Bytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vceLinkTxP2Bytes.setStatus("current")
_VceLinkRxP2Bytes_Type = Counter64
_VceLinkRxP2Bytes_Object = MibTableColumn
vceLinkRxP2Bytes = _VceLinkRxP2Bytes_Object(
    (1, 3, 6, 1, 4, 1, 45346, 1, 1, 2, 3, 2, 2, 1, 11),
    _VceLinkRxP2Bytes_Type()
)
vceLinkRxP2Bytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vceLinkRxP2Bytes.setStatus("current")
_VceLinkTxP3Pkt_Type = Counter64
_VceLinkTxP3Pkt_Object = MibTableColumn
vceLinkTxP3Pkt = _VceLinkTxP3Pkt_Object(
    (1, 3, 6, 1, 4, 1, 45346, 1, 1, 2, 3, 2, 2, 1, 12),
    _VceLinkTxP3Pkt_Type()
)
vceLinkTxP3Pkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vceLinkTxP3Pkt.setStatus("current")
_VceLinkRxP3Pkt_Type = Counter64
_VceLinkRxP3Pkt_Object = MibTableColumn
vceLinkRxP3Pkt = _VceLinkRxP3Pkt_Object(
    (1, 3, 6, 1, 4, 1, 45346, 1, 1, 2, 3, 2, 2, 1, 13),
    _VceLinkRxP3Pkt_Type()
)
vceLinkRxP3Pkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vceLinkRxP3Pkt.setStatus("current")
_VceLinkTxP3Bytes_Type = Counter64
_VceLinkTxP3Bytes_Object = MibTableColumn
vceLinkTxP3Bytes = _VceLinkTxP3Bytes_Object(
    (1, 3, 6, 1, 4, 1, 45346, 1, 1, 2, 3, 2, 2, 1, 14),
    _VceLinkTxP3Bytes_Type()
)
vceLinkTxP3Bytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vceLinkTxP3Bytes.setStatus("current")
_VceLinkRxP3Bytes_Type = Counter64
_VceLinkRxP3Bytes_Object = MibTableColumn
vceLinkRxP3Bytes = _VceLinkRxP3Bytes_Object(
    (1, 3, 6, 1, 4, 1, 45346, 1, 1, 2, 3, 2, 2, 1, 15),
    _VceLinkRxP3Bytes_Type()
)
vceLinkRxP3Bytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vceLinkRxP3Bytes.setStatus("current")
_VceLinkTxCtlPkt_Type = Counter64
_VceLinkTxCtlPkt_Object = MibTableColumn
vceLinkTxCtlPkt = _VceLinkTxCtlPkt_Object(
    (1, 3, 6, 1, 4, 1, 45346, 1, 1, 2, 3, 2, 2, 1, 16),
    _VceLinkTxCtlPkt_Type()
)
vceLinkTxCtlPkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vceLinkTxCtlPkt.setStatus("current")
_VceLinkRxCtlPkt_Type = Counter64
_VceLinkRxCtlPkt_Object = MibTableColumn
vceLinkRxCtlPkt = _VceLinkRxCtlPkt_Object(
    (1, 3, 6, 1, 4, 1, 45346, 1, 1, 2, 3, 2, 2, 1, 17),
    _VceLinkRxCtlPkt_Type()
)
vceLinkRxCtlPkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vceLinkRxCtlPkt.setStatus("current")
_VceLinkTxCtlBytes_Type = Counter64
_VceLinkTxCtlBytes_Object = MibTableColumn
vceLinkTxCtlBytes = _VceLinkTxCtlBytes_Object(
    (1, 3, 6, 1, 4, 1, 45346, 1, 1, 2, 3, 2, 2, 1, 18),
    _VceLinkTxCtlBytes_Type()
)
vceLinkTxCtlBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vceLinkTxCtlBytes.setStatus("current")
_VceLinkRxCtlBytes_Type = Counter64
_VceLinkRxCtlBytes_Object = MibTableColumn
vceLinkRxCtlBytes = _VceLinkRxCtlBytes_Object(
    (1, 3, 6, 1, 4, 1, 45346, 1, 1, 2, 3, 2, 2, 1, 19),
    _VceLinkRxCtlBytes_Type()
)
vceLinkRxCtlBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vceLinkRxCtlBytes.setStatus("current")
_VceLinkTxJitter_Type = Counter64
_VceLinkTxJitter_Object = MibTableColumn
vceLinkTxJitter = _VceLinkTxJitter_Object(
    (1, 3, 6, 1, 4, 1, 45346, 1, 1, 2, 3, 2, 2, 1, 20),
    _VceLinkTxJitter_Type()
)
vceLinkTxJitter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vceLinkTxJitter.setStatus("current")
_VceLinkRxJitter_Type = Counter64
_VceLinkRxJitter_Object = MibTableColumn
vceLinkRxJitter = _VceLinkRxJitter_Object(
    (1, 3, 6, 1, 4, 1, 45346, 1, 1, 2, 3, 2, 2, 1, 21),
    _VceLinkRxJitter_Type()
)
vceLinkRxJitter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vceLinkRxJitter.setStatus("current")
_VceLinkTxLatency_Type = Counter64
_VceLinkTxLatency_Object = MibTableColumn
vceLinkTxLatency = _VceLinkTxLatency_Object(
    (1, 3, 6, 1, 4, 1, 45346, 1, 1, 2, 3, 2, 2, 1, 22),
    _VceLinkTxLatency_Type()
)
vceLinkTxLatency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vceLinkTxLatency.setStatus("current")
_VceLinkRxLatency_Type = Counter64
_VceLinkRxLatency_Object = MibTableColumn
vceLinkRxLatency = _VceLinkRxLatency_Object(
    (1, 3, 6, 1, 4, 1, 45346, 1, 1, 2, 3, 2, 2, 1, 23),
    _VceLinkRxLatency_Type()
)
vceLinkRxLatency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vceLinkRxLatency.setStatus("current")
_VceLinkTxLostPkt_Type = Counter64
_VceLinkTxLostPkt_Object = MibTableColumn
vceLinkTxLostPkt = _VceLinkTxLostPkt_Object(
    (1, 3, 6, 1, 4, 1, 45346, 1, 1, 2, 3, 2, 2, 1, 24),
    _VceLinkTxLostPkt_Type()
)
vceLinkTxLostPkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vceLinkTxLostPkt.setStatus("current")
_VceLinkRxLostPkt_Type = Counter64
_VceLinkRxLostPkt_Object = MibTableColumn
vceLinkRxLostPkt = _VceLinkRxLostPkt_Object(
    (1, 3, 6, 1, 4, 1, 45346, 1, 1, 2, 3, 2, 2, 1, 25),
    _VceLinkRxLostPkt_Type()
)
vceLinkRxLostPkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vceLinkRxLostPkt.setStatus("current")
_VceLinkVpnState_Type = VceLinkStateType
_VceLinkVpnState_Object = MibTableColumn
vceLinkVpnState = _VceLinkVpnState_Object(
    (1, 3, 6, 1, 4, 1, 45346, 1, 1, 2, 3, 2, 2, 1, 26),
    _VceLinkVpnState_Type()
)
vceLinkVpnState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vceLinkVpnState.setStatus("current")
_VceLinkPublicIpType_Type = InetAddressType
_VceLinkPublicIpType_Object = MibTableColumn
vceLinkPublicIpType = _VceLinkPublicIpType_Object(
    (1, 3, 6, 1, 4, 1, 45346, 1, 1, 2, 3, 2, 2, 1, 27),
    _VceLinkPublicIpType_Type()
)
vceLinkPublicIpType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vceLinkPublicIpType.setStatus("current")
_VceLinkPublicIp_Type = InetAddress
_VceLinkPublicIp_Object = MibTableColumn
vceLinkPublicIp = _VceLinkPublicIp_Object(
    (1, 3, 6, 1, 4, 1, 45346, 1, 1, 2, 3, 2, 2, 1, 28),
    _VceLinkPublicIp_Type()
)
vceLinkPublicIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vceLinkPublicIp.setStatus("current")
_VceLinkLocalIpType_Type = InetAddressType
_VceLinkLocalIpType_Object = MibTableColumn
vceLinkLocalIpType = _VceLinkLocalIpType_Object(
    (1, 3, 6, 1, 4, 1, 45346, 1, 1, 2, 3, 2, 2, 1, 29),
    _VceLinkLocalIpType_Type()
)
vceLinkLocalIpType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vceLinkLocalIpType.setStatus("current")
_VceLinkLocalIp_Type = InetAddress
_VceLinkLocalIp_Object = MibTableColumn
vceLinkLocalIp = _VceLinkLocalIp_Object(
    (1, 3, 6, 1, 4, 1, 45346, 1, 1, 2, 3, 2, 2, 1, 30),
    _VceLinkLocalIp_Type()
)
vceLinkLocalIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vceLinkLocalIp.setStatus("current")
_VceLinkVlanId_Type = Integer32
_VceLinkVlanId_Object = MibTableColumn
vceLinkVlanId = _VceLinkVlanId_Object(
    (1, 3, 6, 1, 4, 1, 45346, 1, 1, 2, 3, 2, 2, 1, 31),
    _VceLinkVlanId_Type()
)
vceLinkVlanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vceLinkVlanId.setStatus("current")
_VceLinkMtu_Type = Integer32
_VceLinkMtu_Object = MibTableColumn
vceLinkMtu = _VceLinkMtu_Object(
    (1, 3, 6, 1, 4, 1, 45346, 1, 1, 2, 3, 2, 2, 1, 32),
    _VceLinkMtu_Type()
)
vceLinkMtu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vceLinkMtu.setStatus("current")
_VceLinkItf_Type = DisplayString
_VceLinkItf_Object = MibTableColumn
vceLinkItf = _VceLinkItf_Object(
    (1, 3, 6, 1, 4, 1, 45346, 1, 1, 2, 3, 2, 2, 1, 33),
    _VceLinkItf_Type()
)
vceLinkItf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vceLinkItf.setStatus("current")
_VceLinkState_Type = VceLinkStateType
_VceLinkState_Object = MibTableColumn
vceLinkState = _VceLinkState_Object(
    (1, 3, 6, 1, 4, 1, 45346, 1, 1, 2, 3, 2, 2, 1, 34),
    _VceLinkState_Type()
)
vceLinkState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vceLinkState.setStatus("current")
_VceLinkVeloSvcReachable_Type = TruthValue
_VceLinkVeloSvcReachable_Object = MibTableColumn
vceLinkVeloSvcReachable = _VceLinkVeloSvcReachable_Object(
    (1, 3, 6, 1, 4, 1, 45346, 1, 1, 2, 3, 2, 2, 1, 35),
    _VceLinkVeloSvcReachable_Type()
)
vceLinkVeloSvcReachable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vceLinkVeloSvcReachable.setStatus("current")
_VceLinkTotTxPkts_Type = Counter64
_VceLinkTotTxPkts_Object = MibTableColumn
vceLinkTotTxPkts = _VceLinkTotTxPkts_Object(
    (1, 3, 6, 1, 4, 1, 45346, 1, 1, 2, 3, 2, 2, 1, 36),
    _VceLinkTotTxPkts_Type()
)
vceLinkTotTxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vceLinkTotTxPkts.setStatus("current")
_VceLinkTotRxPkts_Type = Counter64
_VceLinkTotRxPkts_Object = MibTableColumn
vceLinkTotRxPkts = _VceLinkTotRxPkts_Object(
    (1, 3, 6, 1, 4, 1, 45346, 1, 1, 2, 3, 2, 2, 1, 37),
    _VceLinkTotRxPkts_Type()
)
vceLinkTotRxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vceLinkTotRxPkts.setStatus("current")
_VceLinkTotTxbytes_Type = Counter64
_VceLinkTotTxbytes_Object = MibTableColumn
vceLinkTotTxbytes = _VceLinkTotTxbytes_Object(
    (1, 3, 6, 1, 4, 1, 45346, 1, 1, 2, 3, 2, 2, 1, 38),
    _VceLinkTotTxbytes_Type()
)
vceLinkTotTxbytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vceLinkTotTxbytes.setStatus("current")
_VceLinkTotRxBytes_Type = Counter64
_VceLinkTotRxBytes_Object = MibTableColumn
vceLinkTotRxBytes = _VceLinkTotRxBytes_Object(
    (1, 3, 6, 1, 4, 1, 45346, 1, 1, 2, 3, 2, 2, 1, 39),
    _VceLinkTotRxBytes_Type()
)
vceLinkTotRxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vceLinkTotRxBytes.setStatus("current")
_VceLinkIf_Type = InterfaceIndex
_VceLinkIf_Object = MibTableColumn
vceLinkIf = _VceLinkIf_Object(
    (1, 3, 6, 1, 4, 1, 45346, 1, 1, 2, 3, 2, 2, 1, 40),
    _VceLinkIf_Type()
)
vceLinkIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vceLinkIf.setStatus("current")
_VceLinkNextHopType_Type = InetAddressType
_VceLinkNextHopType_Object = MibTableColumn
vceLinkNextHopType = _VceLinkNextHopType_Object(
    (1, 3, 6, 1, 4, 1, 45346, 1, 1, 2, 3, 2, 2, 1, 41),
    _VceLinkNextHopType_Type()
)
vceLinkNextHopType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vceLinkNextHopType.setStatus("current")
_VceLinkNextHop_Type = InetAddress
_VceLinkNextHop_Object = MibTableColumn
vceLinkNextHop = _VceLinkNextHop_Object(
    (1, 3, 6, 1, 4, 1, 45346, 1, 1, 2, 3, 2, 2, 1, 42),
    _VceLinkNextHop_Type()
)
vceLinkNextHop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vceLinkNextHop.setStatus("current")
_VcePath_ObjectIdentity = ObjectIdentity
vcePath = _VcePath_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45346, 1, 1, 2, 4)
)
_VcePathObject_ObjectIdentity = ObjectIdentity
vcePathObject = _VcePathObject_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45346, 1, 1, 2, 4, 2)
)
_VcePathNum_Type = Integer32
_VcePathNum_Object = MibScalar
vcePathNum = _VcePathNum_Object(
    (1, 3, 6, 1, 4, 1, 45346, 1, 1, 2, 4, 2, 1),
    _VcePathNum_Type()
)
vcePathNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vcePathNum.setStatus("current")
_VcePathTable_Object = MibTable
vcePathTable = _VcePathTable_Object(
    (1, 3, 6, 1, 4, 1, 45346, 1, 1, 2, 4, 2, 2)
)
if mibBuilder.loadTexts:
    vcePathTable.setStatus("current")
_VcePathEntry_Object = MibTableRow
vcePathEntry = _VcePathEntry_Object(
    (1, 3, 6, 1, 4, 1, 45346, 1, 1, 2, 4, 2, 2, 1)
)
vcePathEntry.setIndexNames(
    (0, "VELOCLOUD-EDGE-MIB", "vcePathIfIntId"),
    (0, "VELOCLOUD-EDGE-MIB", "vcePathGwAddrType"),
    (0, "VELOCLOUD-EDGE-MIB", "vcePathGwAddr"),
)
if mibBuilder.loadTexts:
    vcePathEntry.setStatus("current")
_VcePathIfIntId_Type = UUID
_VcePathIfIntId_Object = MibTableColumn
vcePathIfIntId = _VcePathIfIntId_Object(
    (1, 3, 6, 1, 4, 1, 45346, 1, 1, 2, 4, 2, 2, 1, 1),
    _VcePathIfIntId_Type()
)
vcePathIfIntId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vcePathIfIntId.setStatus("current")
_VcePathIpType_Type = InetAddressType
_VcePathIpType_Object = MibTableColumn
vcePathIpType = _VcePathIpType_Object(
    (1, 3, 6, 1, 4, 1, 45346, 1, 1, 2, 4, 2, 2, 1, 2),
    _VcePathIpType_Type()
)
vcePathIpType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vcePathIpType.setStatus("current")
_VcePathIp_Type = InetAddress
_VcePathIp_Object = MibTableColumn
vcePathIp = _VcePathIp_Object(
    (1, 3, 6, 1, 4, 1, 45346, 1, 1, 2, 4, 2, 2, 1, 3),
    _VcePathIp_Type()
)
vcePathIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vcePathIp.setStatus("current")
_VcePathGwAddrType_Type = InetAddressType
_VcePathGwAddrType_Object = MibTableColumn
vcePathGwAddrType = _VcePathGwAddrType_Object(
    (1, 3, 6, 1, 4, 1, 45346, 1, 1, 2, 4, 2, 2, 1, 4),
    _VcePathGwAddrType_Type()
)
vcePathGwAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vcePathGwAddrType.setStatus("current")
_VcePathGwAddr_Type = InetAddress
_VcePathGwAddr_Object = MibTableColumn
vcePathGwAddr = _VcePathGwAddr_Object(
    (1, 3, 6, 1, 4, 1, 45346, 1, 1, 2, 4, 2, 2, 1, 5),
    _VcePathGwAddr_Type()
)
vcePathGwAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vcePathGwAddr.setStatus("current")
_VcePathPeerName_Type = DisplayString
_VcePathPeerName_Object = MibTableColumn
vcePathPeerName = _VcePathPeerName_Object(
    (1, 3, 6, 1, 4, 1, 45346, 1, 1, 2, 4, 2, 2, 1, 6),
    _VcePathPeerName_Type()
)
vcePathPeerName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vcePathPeerName.setStatus("current")
_VcePathState_Type = VcePathStateType
_VcePathState_Object = MibTableColumn
vcePathState = _VcePathState_Object(
    (1, 3, 6, 1, 4, 1, 45346, 1, 1, 2, 4, 2, 2, 1, 7),
    _VcePathState_Type()
)
vcePathState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vcePathState.setStatus("current")
_VcePathUpTime_Type = TimeTicks
_VcePathUpTime_Object = MibTableColumn
vcePathUpTime = _VcePathUpTime_Object(
    (1, 3, 6, 1, 4, 1, 45346, 1, 1, 2, 4, 2, 2, 1, 8),
    _VcePathUpTime_Type()
)
vcePathUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vcePathUpTime.setStatus("current")
_VcePathRxState_Type = VcePathStateType
_VcePathRxState_Object = MibTableColumn
vcePathRxState = _VcePathRxState_Object(
    (1, 3, 6, 1, 4, 1, 45346, 1, 1, 2, 4, 2, 2, 1, 10),
    _VcePathRxState_Type()
)
vcePathRxState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vcePathRxState.setStatus("current")
_VcePathTxState_Type = VcePathStateType
_VcePathTxState_Object = MibTableColumn
vcePathTxState = _VcePathTxState_Object(
    (1, 3, 6, 1, 4, 1, 45346, 1, 1, 2, 4, 2, 2, 1, 11),
    _VcePathTxState_Type()
)
vcePathTxState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vcePathTxState.setStatus("current")
_VcePathTunlMode_Type = VcePathTunlModeType
_VcePathTunlMode_Object = MibTableColumn
vcePathTunlMode = _VcePathTunlMode_Object(
    (1, 3, 6, 1, 4, 1, 45346, 1, 1, 2, 4, 2, 2, 1, 12),
    _VcePathTunlMode_Type()
)
vcePathTunlMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vcePathTunlMode.setStatus("current")
_VcePathTxAveLatency_Type = Integer32
_VcePathTxAveLatency_Object = MibTableColumn
vcePathTxAveLatency = _VcePathTxAveLatency_Object(
    (1, 3, 6, 1, 4, 1, 45346, 1, 1, 2, 4, 2, 2, 1, 13),
    _VcePathTxAveLatency_Type()
)
vcePathTxAveLatency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vcePathTxAveLatency.setStatus("current")
_VcePathRxAveLatency_Type = Integer32
_VcePathRxAveLatency_Object = MibTableColumn
vcePathRxAveLatency = _VcePathRxAveLatency_Object(
    (1, 3, 6, 1, 4, 1, 45346, 1, 1, 2, 4, 2, 2, 1, 14),
    _VcePathRxAveLatency_Type()
)
vcePathRxAveLatency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vcePathRxAveLatency.setStatus("current")
_VcePathRxBytes_Type = Counter64
_VcePathRxBytes_Object = MibTableColumn
vcePathRxBytes = _VcePathRxBytes_Object(
    (1, 3, 6, 1, 4, 1, 45346, 1, 1, 2, 4, 2, 2, 1, 15),
    _VcePathRxBytes_Type()
)
vcePathRxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vcePathRxBytes.setStatus("current")
_VcePathTxBytes_Type = Counter64
_VcePathTxBytes_Object = MibTableColumn
vcePathTxBytes = _VcePathTxBytes_Object(
    (1, 3, 6, 1, 4, 1, 45346, 1, 1, 2, 4, 2, 2, 1, 16),
    _VcePathTxBytes_Type()
)
vcePathTxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vcePathTxBytes.setStatus("current")
_VcePathRxLostPkt_Type = Counter64
_VcePathRxLostPkt_Object = MibTableColumn
vcePathRxLostPkt = _VcePathRxLostPkt_Object(
    (1, 3, 6, 1, 4, 1, 45346, 1, 1, 2, 4, 2, 2, 1, 17),
    _VcePathRxLostPkt_Type()
)
vcePathRxLostPkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vcePathRxLostPkt.setStatus("current")
_VcePathTxLostPkt_Type = Counter64
_VcePathTxLostPkt_Object = MibTableColumn
vcePathTxLostPkt = _VcePathTxLostPkt_Object(
    (1, 3, 6, 1, 4, 1, 45346, 1, 1, 2, 4, 2, 2, 1, 18),
    _VcePathTxLostPkt_Type()
)
vcePathTxLostPkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vcePathTxLostPkt.setStatus("current")
_VcePathRxPkt_Type = Counter64
_VcePathRxPkt_Object = MibTableColumn
vcePathRxPkt = _VcePathRxPkt_Object(
    (1, 3, 6, 1, 4, 1, 45346, 1, 1, 2, 4, 2, 2, 1, 19),
    _VcePathRxPkt_Type()
)
vcePathRxPkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vcePathRxPkt.setStatus("current")
_VcePathTxPkt_Type = Counter64
_VcePathTxPkt_Object = MibTableColumn
vcePathTxPkt = _VcePathTxPkt_Object(
    (1, 3, 6, 1, 4, 1, 45346, 1, 1, 2, 4, 2, 2, 1, 20),
    _VcePathTxPkt_Type()
)
vcePathTxPkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vcePathTxPkt.setStatus("current")
_VcePathRxJitter_Type = Counter64
_VcePathRxJitter_Object = MibTableColumn
vcePathRxJitter = _VcePathRxJitter_Object(
    (1, 3, 6, 1, 4, 1, 45346, 1, 1, 2, 4, 2, 2, 1, 21),
    _VcePathRxJitter_Type()
)
vcePathRxJitter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vcePathRxJitter.setStatus("current")
_VcePathTxJitter_Type = Counter64
_VcePathTxJitter_Object = MibTableColumn
vcePathTxJitter = _VcePathTxJitter_Object(
    (1, 3, 6, 1, 4, 1, 45346, 1, 1, 2, 4, 2, 2, 1, 22),
    _VcePathTxJitter_Type()
)
vcePathTxJitter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vcePathTxJitter.setStatus("current")
_VceARP_ObjectIdentity = ObjectIdentity
vceARP = _VceARP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45346, 1, 1, 2, 5)
)
_VceArpObject_ObjectIdentity = ObjectIdentity
vceArpObject = _VceArpObject_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45346, 1, 1, 2, 5, 2)
)
_VceArpNum_Type = Integer32
_VceArpNum_Object = MibScalar
vceArpNum = _VceArpNum_Object(
    (1, 3, 6, 1, 4, 1, 45346, 1, 1, 2, 5, 2, 1),
    _VceArpNum_Type()
)
vceArpNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vceArpNum.setStatus("current")
_VceArpTable_Object = MibTable
vceArpTable = _VceArpTable_Object(
    (1, 3, 6, 1, 4, 1, 45346, 1, 1, 2, 5, 2, 2)
)
if mibBuilder.loadTexts:
    vceArpTable.setStatus("current")
_VceArpEntry_Object = MibTableRow
vceArpEntry = _VceArpEntry_Object(
    (1, 3, 6, 1, 4, 1, 45346, 1, 1, 2, 5, 2, 2, 1)
)
vceArpEntry.setIndexNames(
    (0, "VELOCLOUD-EDGE-MIB", "vceArpItf"),
    (0, "VELOCLOUD-EDGE-MIB", "vceArpIpAddrType"),
    (0, "VELOCLOUD-EDGE-MIB", "vceArpIpAddr"),
)
if mibBuilder.loadTexts:
    vceArpEntry.setStatus("current")
_VceArpItf_Type = InterfaceIndex
_VceArpItf_Object = MibTableColumn
vceArpItf = _VceArpItf_Object(
    (1, 3, 6, 1, 4, 1, 45346, 1, 1, 2, 5, 2, 2, 1, 1),
    _VceArpItf_Type()
)
vceArpItf.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vceArpItf.setStatus("current")
_VceArpIpAddrType_Type = InetAddressType
_VceArpIpAddrType_Object = MibTableColumn
vceArpIpAddrType = _VceArpIpAddrType_Object(
    (1, 3, 6, 1, 4, 1, 45346, 1, 1, 2, 5, 2, 2, 1, 2),
    _VceArpIpAddrType_Type()
)
vceArpIpAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vceArpIpAddrType.setStatus("current")
_VceArpIpAddr_Type = InetAddress
_VceArpIpAddr_Object = MibTableColumn
vceArpIpAddr = _VceArpIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 45346, 1, 1, 2, 5, 2, 2, 1, 3),
    _VceArpIpAddr_Type()
)
vceArpIpAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vceArpIpAddr.setStatus("current")


class _VceArpMac_Type(PhysAddress):
    """Custom type vceArpMac based on PhysAddress"""
    subtypeSpec = PhysAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 65535),
    )


_VceArpMac_Type.__name__ = "PhysAddress"
_VceArpMac_Object = MibTableColumn
vceArpMac = _VceArpMac_Object(
    (1, 3, 6, 1, 4, 1, 45346, 1, 1, 2, 5, 2, 2, 1, 4),
    _VceArpMac_Type()
)
vceArpMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vceArpMac.setStatus("current")
_VceArpStag_Type = Integer32
_VceArpStag_Object = MibTableColumn
vceArpStag = _VceArpStag_Object(
    (1, 3, 6, 1, 4, 1, 45346, 1, 1, 2, 5, 2, 2, 1, 5),
    _VceArpStag_Type()
)
vceArpStag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vceArpStag.setStatus("current")
_VceArpCtag_Type = Integer32
_VceArpCtag_Object = MibTableColumn
vceArpCtag = _VceArpCtag_Object(
    (1, 3, 6, 1, 4, 1, 45346, 1, 1, 2, 5, 2, 2, 1, 6),
    _VceArpCtag_Type()
)
vceArpCtag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vceArpCtag.setStatus("current")
_VceArpState_Type = VceArpStateType
_VceArpState_Object = MibTableColumn
vceArpState = _VceArpState_Object(
    (1, 3, 6, 1, 4, 1, 45346, 1, 1, 2, 5, 2, 2, 1, 7),
    _VceArpState_Type()
)
vceArpState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vceArpState.setStatus("current")

# Managed Objects groups

vceHaGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 45346, 1, 1, 2, 1, 1)
)
vceHaGroup.setObjects(
      *(("VELOCLOUD-EDGE-MIB", "vceHaAdminState"),
        ("VELOCLOUD-EDGE-MIB", "vceHaPeerState"),
        ("VELOCLOUD-EDGE-MIB", "vceHaActiveWanItfNum"),
        ("VELOCLOUD-EDGE-MIB", "vceHaActiveLanItfNum"),
        ("VELOCLOUD-EDGE-MIB", "vceHaStanbyWanItfNum"),
        ("VELOCLOUD-EDGE-MIB", "vceHaStanbyLanItfNum"))
)
if mibBuilder.loadTexts:
    vceHaGroup.setStatus("current")

vceHealthGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 45346, 1, 1, 2, 2, 1)
)
vceHealthGroup.setObjects(
      *(("VELOCLOUD-EDGE-MIB", "vceCpuUtilPct5min"),
        ("VELOCLOUD-EDGE-MIB", "vceCpuUtilPct30sec"),
        ("VELOCLOUD-EDGE-MIB", "vceMemUsedPct"))
)
if mibBuilder.loadTexts:
    vceHealthGroup.setStatus("current")

vceLinkGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 45346, 1, 1, 2, 3, 1)
)
vceLinkGroup.setObjects(
      *(("VELOCLOUD-EDGE-MIB", "vceLinkNum"),
        ("VELOCLOUD-EDGE-MIB", "vceLinkName"),
        ("VELOCLOUD-EDGE-MIB", "vceLinkTxP1Pkt"),
        ("VELOCLOUD-EDGE-MIB", "vceLinkRxP1Pkt"),
        ("VELOCLOUD-EDGE-MIB", "vceLinkTxP1Bytes"),
        ("VELOCLOUD-EDGE-MIB", "vceLinkRxP1Bytes"),
        ("VELOCLOUD-EDGE-MIB", "vceLinkTxP2Pkt"),
        ("VELOCLOUD-EDGE-MIB", "vceLinkRxP2Pkt"),
        ("VELOCLOUD-EDGE-MIB", "vceLinkTxP2Bytes"),
        ("VELOCLOUD-EDGE-MIB", "vceLinkRxP2Bytes"),
        ("VELOCLOUD-EDGE-MIB", "vceLinkTxP3Pkt"),
        ("VELOCLOUD-EDGE-MIB", "vceLinkRxP3Pkt"),
        ("VELOCLOUD-EDGE-MIB", "vceLinkTxP3Bytes"),
        ("VELOCLOUD-EDGE-MIB", "vceLinkRxP3Bytes"),
        ("VELOCLOUD-EDGE-MIB", "vceLinkTxCtlPkt"),
        ("VELOCLOUD-EDGE-MIB", "vceLinkRxCtlPkt"),
        ("VELOCLOUD-EDGE-MIB", "vceLinkTxCtlBytes"),
        ("VELOCLOUD-EDGE-MIB", "vceLinkRxCtlBytes"),
        ("VELOCLOUD-EDGE-MIB", "vceLinkTxJitter"),
        ("VELOCLOUD-EDGE-MIB", "vceLinkRxJitter"),
        ("VELOCLOUD-EDGE-MIB", "vceLinkTxLatency"),
        ("VELOCLOUD-EDGE-MIB", "vceLinkRxLatency"),
        ("VELOCLOUD-EDGE-MIB", "vceLinkTxLostPkt"),
        ("VELOCLOUD-EDGE-MIB", "vceLinkRxLostPkt"),
        ("VELOCLOUD-EDGE-MIB", "vceLinkVpnState"),
        ("VELOCLOUD-EDGE-MIB", "vceLinkPublicIpType"),
        ("VELOCLOUD-EDGE-MIB", "vceLinkPublicIp"),
        ("VELOCLOUD-EDGE-MIB", "vceLinkLocalIpType"),
        ("VELOCLOUD-EDGE-MIB", "vceLinkLocalIp"),
        ("VELOCLOUD-EDGE-MIB", "vceLinkVlanId"),
        ("VELOCLOUD-EDGE-MIB", "vceLinkMtu"),
        ("VELOCLOUD-EDGE-MIB", "vceLinkItf"),
        ("VELOCLOUD-EDGE-MIB", "vceLinkState"),
        ("VELOCLOUD-EDGE-MIB", "vceLinkVeloSvcReachable"),
        ("VELOCLOUD-EDGE-MIB", "vceLinkTotTxPkts"),
        ("VELOCLOUD-EDGE-MIB", "vceLinkTotRxPkts"),
        ("VELOCLOUD-EDGE-MIB", "vceLinkTotTxbytes"),
        ("VELOCLOUD-EDGE-MIB", "vceLinkTotRxBytes"),
        ("VELOCLOUD-EDGE-MIB", "vceLinkIf"),
        ("VELOCLOUD-EDGE-MIB", "vceLinkNextHopType"),
        ("VELOCLOUD-EDGE-MIB", "vceLinkNextHop"))
)
if mibBuilder.loadTexts:
    vceLinkGroup.setStatus("current")

vcePathGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 45346, 1, 1, 2, 4, 1)
)
vcePathGroup.setObjects(
      *(("VELOCLOUD-EDGE-MIB", "vcePathNum"),
        ("VELOCLOUD-EDGE-MIB", "vcePathIpType"),
        ("VELOCLOUD-EDGE-MIB", "vcePathIp"),
        ("VELOCLOUD-EDGE-MIB", "vcePathPeerName"),
        ("VELOCLOUD-EDGE-MIB", "vcePathState"),
        ("VELOCLOUD-EDGE-MIB", "vcePathUpTime"),
        ("VELOCLOUD-EDGE-MIB", "vcePathRxState"),
        ("VELOCLOUD-EDGE-MIB", "vcePathTxState"),
        ("VELOCLOUD-EDGE-MIB", "vcePathTunlMode"),
        ("VELOCLOUD-EDGE-MIB", "vcePathTxAveLatency"),
        ("VELOCLOUD-EDGE-MIB", "vcePathRxAveLatency"),
        ("VELOCLOUD-EDGE-MIB", "vcePathRxBytes"),
        ("VELOCLOUD-EDGE-MIB", "vcePathTxBytes"),
        ("VELOCLOUD-EDGE-MIB", "vcePathRxLostPkt"),
        ("VELOCLOUD-EDGE-MIB", "vcePathTxLostPkt"),
        ("VELOCLOUD-EDGE-MIB", "vcePathRxPkt"),
        ("VELOCLOUD-EDGE-MIB", "vcePathTxPkt"),
        ("VELOCLOUD-EDGE-MIB", "vcePathRxJitter"),
        ("VELOCLOUD-EDGE-MIB", "vcePathTxJitter"))
)
if mibBuilder.loadTexts:
    vcePathGroup.setStatus("current")

vceArpGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 45346, 1, 1, 2, 5, 1)
)
vceArpGroup.setObjects(
      *(("VELOCLOUD-EDGE-MIB", "vceArpNum"),
        ("VELOCLOUD-EDGE-MIB", "vceArpMac"),
        ("VELOCLOUD-EDGE-MIB", "vceArpStag"),
        ("VELOCLOUD-EDGE-MIB", "vceArpCtag"),
        ("VELOCLOUD-EDGE-MIB", "vceArpState"))
)
if mibBuilder.loadTexts:
    vceArpGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

vceCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 45346, 1, 1, 1)
)
vceCompliance.setObjects(
      *(("VELOCLOUD-EDGE-MIB", "vceHaGroup"),
        ("VELOCLOUD-EDGE-MIB", "vceHealthGroup"),
        ("VELOCLOUD-EDGE-MIB", "vceLinkGroup"),
        ("VELOCLOUD-EDGE-MIB", "vcePathGroup"),
        ("VELOCLOUD-EDGE-MIB", "vceArpGroup"))
)
if mibBuilder.loadTexts:
    vceCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "VELOCLOUD-EDGE-MIB",
    **{"VceHaAdminStateType": VceHaAdminStateType,
       "VceHaPeerStateType": VceHaPeerStateType,
       "VceLinkStateType": VceLinkStateType,
       "VcePathStateType": VcePathStateType,
       "VcePathTunlModeType": VcePathTunlModeType,
       "VceArpStateType": VceArpStateType,
       "edge": edge,
       "vceCompliance": vceCompliance,
       "vceEdgeObject": vceEdgeObject,
       "vceHA": vceHA,
       "vceHaGroup": vceHaGroup,
       "vceHAObject": vceHAObject,
       "vceHaAdminState": vceHaAdminState,
       "vceHaPeerState": vceHaPeerState,
       "vceHaActiveWanItfNum": vceHaActiveWanItfNum,
       "vceHaActiveLanItfNum": vceHaActiveLanItfNum,
       "vceHaStanbyWanItfNum": vceHaStanbyWanItfNum,
       "vceHaStanbyLanItfNum": vceHaStanbyLanItfNum,
       "vceHealth": vceHealth,
       "vceHealthGroup": vceHealthGroup,
       "vceHealthObject": vceHealthObject,
       "vceCpuUtilPct5min": vceCpuUtilPct5min,
       "vceCpuUtilPct30sec": vceCpuUtilPct30sec,
       "vceMemUsedPct": vceMemUsedPct,
       "vceLink": vceLink,
       "vceLinkGroup": vceLinkGroup,
       "vceLinkObject": vceLinkObject,
       "vceLinkNum": vceLinkNum,
       "vceLinkTable": vceLinkTable,
       "vceLinkEntry": vceLinkEntry,
       "vceLinkIntId": vceLinkIntId,
       "vceLinkName": vceLinkName,
       "vceLinkTxP1Pkt": vceLinkTxP1Pkt,
       "vceLinkRxP1Pkt": vceLinkRxP1Pkt,
       "vceLinkTxP1Bytes": vceLinkTxP1Bytes,
       "vceLinkRxP1Bytes": vceLinkRxP1Bytes,
       "vceLinkTxP2Pkt": vceLinkTxP2Pkt,
       "vceLinkRxP2Pkt": vceLinkRxP2Pkt,
       "vceLinkTxP2Bytes": vceLinkTxP2Bytes,
       "vceLinkRxP2Bytes": vceLinkRxP2Bytes,
       "vceLinkTxP3Pkt": vceLinkTxP3Pkt,
       "vceLinkRxP3Pkt": vceLinkRxP3Pkt,
       "vceLinkTxP3Bytes": vceLinkTxP3Bytes,
       "vceLinkRxP3Bytes": vceLinkRxP3Bytes,
       "vceLinkTxCtlPkt": vceLinkTxCtlPkt,
       "vceLinkRxCtlPkt": vceLinkRxCtlPkt,
       "vceLinkTxCtlBytes": vceLinkTxCtlBytes,
       "vceLinkRxCtlBytes": vceLinkRxCtlBytes,
       "vceLinkTxJitter": vceLinkTxJitter,
       "vceLinkRxJitter": vceLinkRxJitter,
       "vceLinkTxLatency": vceLinkTxLatency,
       "vceLinkRxLatency": vceLinkRxLatency,
       "vceLinkTxLostPkt": vceLinkTxLostPkt,
       "vceLinkRxLostPkt": vceLinkRxLostPkt,
       "vceLinkVpnState": vceLinkVpnState,
       "vceLinkPublicIpType": vceLinkPublicIpType,
       "vceLinkPublicIp": vceLinkPublicIp,
       "vceLinkLocalIpType": vceLinkLocalIpType,
       "vceLinkLocalIp": vceLinkLocalIp,
       "vceLinkVlanId": vceLinkVlanId,
       "vceLinkMtu": vceLinkMtu,
       "vceLinkItf": vceLinkItf,
       "vceLinkState": vceLinkState,
       "vceLinkVeloSvcReachable": vceLinkVeloSvcReachable,
       "vceLinkTotTxPkts": vceLinkTotTxPkts,
       "vceLinkTotRxPkts": vceLinkTotRxPkts,
       "vceLinkTotTxbytes": vceLinkTotTxbytes,
       "vceLinkTotRxBytes": vceLinkTotRxBytes,
       "vceLinkIf": vceLinkIf,
       "vceLinkNextHopType": vceLinkNextHopType,
       "vceLinkNextHop": vceLinkNextHop,
       "vcePath": vcePath,
       "vcePathGroup": vcePathGroup,
       "vcePathObject": vcePathObject,
       "vcePathNum": vcePathNum,
       "vcePathTable": vcePathTable,
       "vcePathEntry": vcePathEntry,
       "vcePathIfIntId": vcePathIfIntId,
       "vcePathIpType": vcePathIpType,
       "vcePathIp": vcePathIp,
       "vcePathGwAddrType": vcePathGwAddrType,
       "vcePathGwAddr": vcePathGwAddr,
       "vcePathPeerName": vcePathPeerName,
       "vcePathState": vcePathState,
       "vcePathUpTime": vcePathUpTime,
       "vcePathRxState": vcePathRxState,
       "vcePathTxState": vcePathTxState,
       "vcePathTunlMode": vcePathTunlMode,
       "vcePathTxAveLatency": vcePathTxAveLatency,
       "vcePathRxAveLatency": vcePathRxAveLatency,
       "vcePathRxBytes": vcePathRxBytes,
       "vcePathTxBytes": vcePathTxBytes,
       "vcePathRxLostPkt": vcePathRxLostPkt,
       "vcePathTxLostPkt": vcePathTxLostPkt,
       "vcePathRxPkt": vcePathRxPkt,
       "vcePathTxPkt": vcePathTxPkt,
       "vcePathRxJitter": vcePathRxJitter,
       "vcePathTxJitter": vcePathTxJitter,
       "vceARP": vceARP,
       "vceArpGroup": vceArpGroup,
       "vceArpObject": vceArpObject,
       "vceArpNum": vceArpNum,
       "vceArpTable": vceArpTable,
       "vceArpEntry": vceArpEntry,
       "vceArpItf": vceArpItf,
       "vceArpIpAddrType": vceArpIpAddrType,
       "vceArpIpAddr": vceArpIpAddr,
       "vceArpMac": vceArpMac,
       "vceArpStag": vceArpStag,
       "vceArpCtag": vceArpCtag,
       "vceArpState": vceArpState}
)
