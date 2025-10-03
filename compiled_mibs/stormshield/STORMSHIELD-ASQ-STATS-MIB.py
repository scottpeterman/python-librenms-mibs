# SNMP MIB module (STORMSHIELD-ASQ-STATS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\stormshield\STORMSHIELD-ASQ-STATS-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 12:28:59 2025
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

(stormshieldMIB,) = mibBuilder.importSymbols(
    "STORMSHIELD-SMI-MIB",
    "stormshieldMIB")


# MODULE-IDENTITY

snsASQStats = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 11256, 1, 12)
)
if mibBuilder.loadTexts:
    snsASQStats.setRevisions(
        ("2017-02-20 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_SnsASQStatsStateful_ObjectIdentity = ObjectIdentity
snsASQStatsStateful = _SnsASQStatsStateful_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11256, 1, 12, 1)
)
_SnsASQStatsStatefulPktBlocked_Type = Counter64
_SnsASQStatsStatefulPktBlocked_Object = MibScalar
snsASQStatsStatefulPktBlocked = _SnsASQStatsStatefulPktBlocked_Object(
    (1, 3, 6, 1, 4, 1, 11256, 1, 12, 1, 1),
    _SnsASQStatsStatefulPktBlocked_Type()
)
snsASQStatsStatefulPktBlocked.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snsASQStatsStatefulPktBlocked.setStatus("current")
_SnsASQStatsStatefulPktBlockedAsync_Type = Counter64
_SnsASQStatsStatefulPktBlockedAsync_Object = MibScalar
snsASQStatsStatefulPktBlockedAsync = _SnsASQStatsStatefulPktBlockedAsync_Object(
    (1, 3, 6, 1, 4, 1, 11256, 1, 12, 1, 2),
    _SnsASQStatsStatefulPktBlockedAsync_Type()
)
snsASQStatsStatefulPktBlockedAsync.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snsASQStatsStatefulPktBlockedAsync.setStatus("current")
_SnsASQStatsStatefulPktBlockedSynProxy_Type = Counter64
_SnsASQStatsStatefulPktBlockedSynProxy_Object = MibScalar
snsASQStatsStatefulPktBlockedSynProxy = _SnsASQStatsStatefulPktBlockedSynProxy_Object(
    (1, 3, 6, 1, 4, 1, 11256, 1, 12, 1, 3),
    _SnsASQStatsStatefulPktBlockedSynProxy_Type()
)
snsASQStatsStatefulPktBlockedSynProxy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snsASQStatsStatefulPktBlockedSynProxy.setStatus("current")
_SnsASQStatsStatefulPktAccepted_Type = Counter64
_SnsASQStatsStatefulPktAccepted_Object = MibScalar
snsASQStatsStatefulPktAccepted = _SnsASQStatsStatefulPktAccepted_Object(
    (1, 3, 6, 1, 4, 1, 11256, 1, 12, 1, 4),
    _SnsASQStatsStatefulPktAccepted_Type()
)
snsASQStatsStatefulPktAccepted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snsASQStatsStatefulPktAccepted.setStatus("current")
_SnsASQStatsStatefulLogged_Type = Counter64
_SnsASQStatsStatefulLogged_Object = MibScalar
snsASQStatsStatefulLogged = _SnsASQStatsStatefulLogged_Object(
    (1, 3, 6, 1, 4, 1, 11256, 1, 12, 1, 5),
    _SnsASQStatsStatefulLogged_Type()
)
snsASQStatsStatefulLogged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snsASQStatsStatefulLogged.setStatus("current")
_SnsASQStatsStatefulLogOverflow_Type = Counter64
_SnsASQStatsStatefulLogOverflow_Object = MibScalar
snsASQStatsStatefulLogOverflow = _SnsASQStatsStatefulLogOverflow_Object(
    (1, 3, 6, 1, 4, 1, 11256, 1, 12, 1, 6),
    _SnsASQStatsStatefulLogOverflow_Type()
)
snsASQStatsStatefulLogOverflow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snsASQStatsStatefulLogOverflow.setStatus("current")
_SnsASQStatsStatefulFilterOverflow_Type = Counter64
_SnsASQStatsStatefulFilterOverflow_Object = MibScalar
snsASQStatsStatefulFilterOverflow = _SnsASQStatsStatefulFilterOverflow_Object(
    (1, 3, 6, 1, 4, 1, 11256, 1, 12, 1, 7),
    _SnsASQStatsStatefulFilterOverflow_Type()
)
snsASQStatsStatefulFilterOverflow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snsASQStatsStatefulFilterOverflow.setStatus("current")
_SnsASQStatsStatefulAlarmOverflow_Type = Counter64
_SnsASQStatsStatefulAlarmOverflow_Object = MibScalar
snsASQStatsStatefulAlarmOverflow = _SnsASQStatsStatefulAlarmOverflow_Object(
    (1, 3, 6, 1, 4, 1, 11256, 1, 12, 1, 8),
    _SnsASQStatsStatefulAlarmOverflow_Type()
)
snsASQStatsStatefulAlarmOverflow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snsASQStatsStatefulAlarmOverflow.setStatus("current")
_SnsASQStatsStatefulSeismoFacts_Type = Counter64
_SnsASQStatsStatefulSeismoFacts_Object = MibScalar
snsASQStatsStatefulSeismoFacts = _SnsASQStatsStatefulSeismoFacts_Object(
    (1, 3, 6, 1, 4, 1, 11256, 1, 12, 1, 9),
    _SnsASQStatsStatefulSeismoFacts_Type()
)
snsASQStatsStatefulSeismoFacts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snsASQStatsStatefulSeismoFacts.setStatus("current")
_SnsASQStatsStatefulSeismoOverflow_Type = Counter64
_SnsASQStatsStatefulSeismoOverflow_Object = MibScalar
snsASQStatsStatefulSeismoOverflow = _SnsASQStatsStatefulSeismoOverflow_Object(
    (1, 3, 6, 1, 4, 1, 11256, 1, 12, 1, 10),
    _SnsASQStatsStatefulSeismoOverflow_Type()
)
snsASQStatsStatefulSeismoOverflow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snsASQStatsStatefulSeismoOverflow.setStatus("current")
_SnsASQStatsStatefulMinorAlarm_Type = Counter64
_SnsASQStatsStatefulMinorAlarm_Object = MibScalar
snsASQStatsStatefulMinorAlarm = _SnsASQStatsStatefulMinorAlarm_Object(
    (1, 3, 6, 1, 4, 1, 11256, 1, 12, 1, 11),
    _SnsASQStatsStatefulMinorAlarm_Type()
)
snsASQStatsStatefulMinorAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snsASQStatsStatefulMinorAlarm.setStatus("current")
_SnsASQStatsStatefulMajorAlarm_Type = Counter64
_SnsASQStatsStatefulMajorAlarm_Object = MibScalar
snsASQStatsStatefulMajorAlarm = _SnsASQStatsStatefulMajorAlarm_Object(
    (1, 3, 6, 1, 4, 1, 11256, 1, 12, 1, 12),
    _SnsASQStatsStatefulMajorAlarm_Type()
)
snsASQStatsStatefulMajorAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snsASQStatsStatefulMajorAlarm.setStatus("current")
_SnsASQStatsStatefulPktFragmented_Type = Counter64
_SnsASQStatsStatefulPktFragmented_Object = MibScalar
snsASQStatsStatefulPktFragmented = _SnsASQStatsStatefulPktFragmented_Object(
    (1, 3, 6, 1, 4, 1, 11256, 1, 12, 1, 13),
    _SnsASQStatsStatefulPktFragmented_Type()
)
snsASQStatsStatefulPktFragmented.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snsASQStatsStatefulPktFragmented.setStatus("current")
_SnsASQStatsStatefulInBytes_Type = DisplayString
_SnsASQStatsStatefulInBytes_Object = MibScalar
snsASQStatsStatefulInBytes = _SnsASQStatsStatefulInBytes_Object(
    (1, 3, 6, 1, 4, 1, 11256, 1, 12, 1, 14),
    _SnsASQStatsStatefulInBytes_Type()
)
snsASQStatsStatefulInBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snsASQStatsStatefulInBytes.setStatus("current")
_SnsASQStatsStatefulOutBytes_Type = DisplayString
_SnsASQStatsStatefulOutBytes_Object = MibScalar
snsASQStatsStatefulOutBytes = _SnsASQStatsStatefulOutBytes_Object(
    (1, 3, 6, 1, 4, 1, 11256, 1, 12, 1, 15),
    _SnsASQStatsStatefulOutBytes_Type()
)
snsASQStatsStatefulOutBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snsASQStatsStatefulOutBytes.setStatus("current")
_SnsASQStatsStatefulNatFailures_Type = Counter64
_SnsASQStatsStatefulNatFailures_Object = MibScalar
snsASQStatsStatefulNatFailures = _SnsASQStatsStatefulNatFailures_Object(
    (1, 3, 6, 1, 4, 1, 11256, 1, 12, 1, 16),
    _SnsASQStatsStatefulNatFailures_Type()
)
snsASQStatsStatefulNatFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snsASQStatsStatefulNatFailures.setStatus("current")
_SnsASQStatsStatefulFlowConflicts_Type = Counter64
_SnsASQStatsStatefulFlowConflicts_Object = MibScalar
snsASQStatsStatefulFlowConflicts = _SnsASQStatsStatefulFlowConflicts_Object(
    (1, 3, 6, 1, 4, 1, 11256, 1, 12, 1, 17),
    _SnsASQStatsStatefulFlowConflicts_Type()
)
snsASQStatsStatefulFlowConflicts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snsASQStatsStatefulFlowConflicts.setStatus("current")
_SnsASQStatsStatefulFlowFailures_Type = Counter64
_SnsASQStatsStatefulFlowFailures_Object = MibScalar
snsASQStatsStatefulFlowFailures = _SnsASQStatsStatefulFlowFailures_Object(
    (1, 3, 6, 1, 4, 1, 11256, 1, 12, 1, 18),
    _SnsASQStatsStatefulFlowFailures_Type()
)
snsASQStatsStatefulFlowFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snsASQStatsStatefulFlowFailures.setStatus("current")
_SnsASQStatsStatefulInterfaceMute_Type = Counter64
_SnsASQStatsStatefulInterfaceMute_Object = MibScalar
snsASQStatsStatefulInterfaceMute = _SnsASQStatsStatefulInterfaceMute_Object(
    (1, 3, 6, 1, 4, 1, 11256, 1, 12, 1, 19),
    _SnsASQStatsStatefulInterfaceMute_Type()
)
snsASQStatsStatefulInterfaceMute.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snsASQStatsStatefulInterfaceMute.setStatus("current")
_SnsASQStatsStatefulTcpPkt_Type = Counter64
_SnsASQStatsStatefulTcpPkt_Object = MibScalar
snsASQStatsStatefulTcpPkt = _SnsASQStatsStatefulTcpPkt_Object(
    (1, 3, 6, 1, 4, 1, 11256, 1, 12, 1, 20),
    _SnsASQStatsStatefulTcpPkt_Type()
)
snsASQStatsStatefulTcpPkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snsASQStatsStatefulTcpPkt.setStatus("current")
_SnsASQStatsStatefulTcpInBytes_Type = DisplayString
_SnsASQStatsStatefulTcpInBytes_Object = MibScalar
snsASQStatsStatefulTcpInBytes = _SnsASQStatsStatefulTcpInBytes_Object(
    (1, 3, 6, 1, 4, 1, 11256, 1, 12, 1, 21),
    _SnsASQStatsStatefulTcpInBytes_Type()
)
snsASQStatsStatefulTcpInBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snsASQStatsStatefulTcpInBytes.setStatus("current")
_SnsASQStatsStatefulTcpOutBytes_Type = DisplayString
_SnsASQStatsStatefulTcpOutBytes_Object = MibScalar
snsASQStatsStatefulTcpOutBytes = _SnsASQStatsStatefulTcpOutBytes_Object(
    (1, 3, 6, 1, 4, 1, 11256, 1, 12, 1, 22),
    _SnsASQStatsStatefulTcpOutBytes_Type()
)
snsASQStatsStatefulTcpOutBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snsASQStatsStatefulTcpOutBytes.setStatus("current")
_SnsASQStatsStatefulTcpConn_Type = Counter64
_SnsASQStatsStatefulTcpConn_Object = MibScalar
snsASQStatsStatefulTcpConn = _SnsASQStatsStatefulTcpConn_Object(
    (1, 3, 6, 1, 4, 1, 11256, 1, 12, 1, 23),
    _SnsASQStatsStatefulTcpConn_Type()
)
snsASQStatsStatefulTcpConn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snsASQStatsStatefulTcpConn.setStatus("current")
_SnsASQStatsStatefulTcpNatConnSrc_Type = Counter64
_SnsASQStatsStatefulTcpNatConnSrc_Object = MibScalar
snsASQStatsStatefulTcpNatConnSrc = _SnsASQStatsStatefulTcpNatConnSrc_Object(
    (1, 3, 6, 1, 4, 1, 11256, 1, 12, 1, 24),
    _SnsASQStatsStatefulTcpNatConnSrc_Type()
)
snsASQStatsStatefulTcpNatConnSrc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snsASQStatsStatefulTcpNatConnSrc.setStatus("current")
_SnsASQStatsStatefulTcpNatConnDst_Type = Counter64
_SnsASQStatsStatefulTcpNatConnDst_Object = MibScalar
snsASQStatsStatefulTcpNatConnDst = _SnsASQStatsStatefulTcpNatConnDst_Object(
    (1, 3, 6, 1, 4, 1, 11256, 1, 12, 1, 25),
    _SnsASQStatsStatefulTcpNatConnDst_Type()
)
snsASQStatsStatefulTcpNatConnDst.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snsASQStatsStatefulTcpNatConnDst.setStatus("current")
_SnsASQStatsStatefulTcpNoNatConnSrc_Type = Counter64
_SnsASQStatsStatefulTcpNoNatConnSrc_Object = MibScalar
snsASQStatsStatefulTcpNoNatConnSrc = _SnsASQStatsStatefulTcpNoNatConnSrc_Object(
    (1, 3, 6, 1, 4, 1, 11256, 1, 12, 1, 26),
    _SnsASQStatsStatefulTcpNoNatConnSrc_Type()
)
snsASQStatsStatefulTcpNoNatConnSrc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snsASQStatsStatefulTcpNoNatConnSrc.setStatus("current")
_SnsASQStatsStatefulTcpNoNatConnDst_Type = Counter64
_SnsASQStatsStatefulTcpNoNatConnDst_Object = MibScalar
snsASQStatsStatefulTcpNoNatConnDst = _SnsASQStatsStatefulTcpNoNatConnDst_Object(
    (1, 3, 6, 1, 4, 1, 11256, 1, 12, 1, 27),
    _SnsASQStatsStatefulTcpNoNatConnDst_Type()
)
snsASQStatsStatefulTcpNoNatConnDst.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snsASQStatsStatefulTcpNoNatConnDst.setStatus("current")
_SnsASQStatsStatefulTcpSmallWindowRst_Type = Counter64
_SnsASQStatsStatefulTcpSmallWindowRst_Object = MibScalar
snsASQStatsStatefulTcpSmallWindowRst = _SnsASQStatsStatefulTcpSmallWindowRst_Object(
    (1, 3, 6, 1, 4, 1, 11256, 1, 12, 1, 28),
    _SnsASQStatsStatefulTcpSmallWindowRst_Type()
)
snsASQStatsStatefulTcpSmallWindowRst.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snsASQStatsStatefulTcpSmallWindowRst.setStatus("current")
_SnsASQStatsStatefulTcpEmptyDupAckBlk_Type = Counter64
_SnsASQStatsStatefulTcpEmptyDupAckBlk_Object = MibScalar
snsASQStatsStatefulTcpEmptyDupAckBlk = _SnsASQStatsStatefulTcpEmptyDupAckBlk_Object(
    (1, 3, 6, 1, 4, 1, 11256, 1, 12, 1, 29),
    _SnsASQStatsStatefulTcpEmptyDupAckBlk_Type()
)
snsASQStatsStatefulTcpEmptyDupAckBlk.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snsASQStatsStatefulTcpEmptyDupAckBlk.setStatus("current")
_SnsASQStatsStatefulUdpPkt_Type = Counter64
_SnsASQStatsStatefulUdpPkt_Object = MibScalar
snsASQStatsStatefulUdpPkt = _SnsASQStatsStatefulUdpPkt_Object(
    (1, 3, 6, 1, 4, 1, 11256, 1, 12, 1, 30),
    _SnsASQStatsStatefulUdpPkt_Type()
)
snsASQStatsStatefulUdpPkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snsASQStatsStatefulUdpPkt.setStatus("current")
_SnsASQStatsStatefulUdpInBytes_Type = DisplayString
_SnsASQStatsStatefulUdpInBytes_Object = MibScalar
snsASQStatsStatefulUdpInBytes = _SnsASQStatsStatefulUdpInBytes_Object(
    (1, 3, 6, 1, 4, 1, 11256, 1, 12, 1, 31),
    _SnsASQStatsStatefulUdpInBytes_Type()
)
snsASQStatsStatefulUdpInBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snsASQStatsStatefulUdpInBytes.setStatus("current")
_SnsASQStatsStatefulUdpOutBytes_Type = DisplayString
_SnsASQStatsStatefulUdpOutBytes_Object = MibScalar
snsASQStatsStatefulUdpOutBytes = _SnsASQStatsStatefulUdpOutBytes_Object(
    (1, 3, 6, 1, 4, 1, 11256, 1, 12, 1, 32),
    _SnsASQStatsStatefulUdpOutBytes_Type()
)
snsASQStatsStatefulUdpOutBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snsASQStatsStatefulUdpOutBytes.setStatus("current")
_SnsASQStatsStatefulUdpConn_Type = Counter64
_SnsASQStatsStatefulUdpConn_Object = MibScalar
snsASQStatsStatefulUdpConn = _SnsASQStatsStatefulUdpConn_Object(
    (1, 3, 6, 1, 4, 1, 11256, 1, 12, 1, 33),
    _SnsASQStatsStatefulUdpConn_Type()
)
snsASQStatsStatefulUdpConn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snsASQStatsStatefulUdpConn.setStatus("current")
_SnsASQStatsStatefulUdpNatConnSrc_Type = Counter64
_SnsASQStatsStatefulUdpNatConnSrc_Object = MibScalar
snsASQStatsStatefulUdpNatConnSrc = _SnsASQStatsStatefulUdpNatConnSrc_Object(
    (1, 3, 6, 1, 4, 1, 11256, 1, 12, 1, 34),
    _SnsASQStatsStatefulUdpNatConnSrc_Type()
)
snsASQStatsStatefulUdpNatConnSrc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snsASQStatsStatefulUdpNatConnSrc.setStatus("current")
_SnsASQStatsStatefulUdpNatConnDst_Type = Counter64
_SnsASQStatsStatefulUdpNatConnDst_Object = MibScalar
snsASQStatsStatefulUdpNatConnDst = _SnsASQStatsStatefulUdpNatConnDst_Object(
    (1, 3, 6, 1, 4, 1, 11256, 1, 12, 1, 35),
    _SnsASQStatsStatefulUdpNatConnDst_Type()
)
snsASQStatsStatefulUdpNatConnDst.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snsASQStatsStatefulUdpNatConnDst.setStatus("current")
_SnsASQStatsStatefulUdpNoNatConnSrc_Type = Counter64
_SnsASQStatsStatefulUdpNoNatConnSrc_Object = MibScalar
snsASQStatsStatefulUdpNoNatConnSrc = _SnsASQStatsStatefulUdpNoNatConnSrc_Object(
    (1, 3, 6, 1, 4, 1, 11256, 1, 12, 1, 36),
    _SnsASQStatsStatefulUdpNoNatConnSrc_Type()
)
snsASQStatsStatefulUdpNoNatConnSrc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snsASQStatsStatefulUdpNoNatConnSrc.setStatus("current")
_SnsASQStatsStatefulUdpNoNatConnDst_Type = Counter64
_SnsASQStatsStatefulUdpNoNatConnDst_Object = MibScalar
snsASQStatsStatefulUdpNoNatConnDst = _SnsASQStatsStatefulUdpNoNatConnDst_Object(
    (1, 3, 6, 1, 4, 1, 11256, 1, 12, 1, 37),
    _SnsASQStatsStatefulUdpNoNatConnDst_Type()
)
snsASQStatsStatefulUdpNoNatConnDst.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snsASQStatsStatefulUdpNoNatConnDst.setStatus("current")
_SnsASQStatsStatefulIcmpPkt_Type = Counter64
_SnsASQStatsStatefulIcmpPkt_Object = MibScalar
snsASQStatsStatefulIcmpPkt = _SnsASQStatsStatefulIcmpPkt_Object(
    (1, 3, 6, 1, 4, 1, 11256, 1, 12, 1, 38),
    _SnsASQStatsStatefulIcmpPkt_Type()
)
snsASQStatsStatefulIcmpPkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snsASQStatsStatefulIcmpPkt.setStatus("current")
_SnsASQStatsStatefulIcmpInBytes_Type = DisplayString
_SnsASQStatsStatefulIcmpInBytes_Object = MibScalar
snsASQStatsStatefulIcmpInBytes = _SnsASQStatsStatefulIcmpInBytes_Object(
    (1, 3, 6, 1, 4, 1, 11256, 1, 12, 1, 39),
    _SnsASQStatsStatefulIcmpInBytes_Type()
)
snsASQStatsStatefulIcmpInBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snsASQStatsStatefulIcmpInBytes.setStatus("current")
_SnsASQStatsStatefulIcmpOutBytes_Type = DisplayString
_SnsASQStatsStatefulIcmpOutBytes_Object = MibScalar
snsASQStatsStatefulIcmpOutBytes = _SnsASQStatsStatefulIcmpOutBytes_Object(
    (1, 3, 6, 1, 4, 1, 11256, 1, 12, 1, 40),
    _SnsASQStatsStatefulIcmpOutBytes_Type()
)
snsASQStatsStatefulIcmpOutBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snsASQStatsStatefulIcmpOutBytes.setStatus("current")
_SnsASQStatsStatefulHttpTimeoutRst_Type = Counter64
_SnsASQStatsStatefulHttpTimeoutRst_Object = MibScalar
snsASQStatsStatefulHttpTimeoutRst = _SnsASQStatsStatefulHttpTimeoutRst_Object(
    (1, 3, 6, 1, 4, 1, 11256, 1, 12, 1, 41),
    _SnsASQStatsStatefulHttpTimeoutRst_Type()
)
snsASQStatsStatefulHttpTimeoutRst.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snsASQStatsStatefulHttpTimeoutRst.setStatus("current")
_SnsASQStatsStatefulNatUnusable_Type = Counter64
_SnsASQStatsStatefulNatUnusable_Object = MibScalar
snsASQStatsStatefulNatUnusable = _SnsASQStatsStatefulNatUnusable_Object(
    (1, 3, 6, 1, 4, 1, 11256, 1, 12, 1, 42),
    _SnsASQStatsStatefulNatUnusable_Type()
)
snsASQStatsStatefulNatUnusable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snsASQStatsStatefulNatUnusable.setStatus("current")
_SnsASQStatsGlobal_ObjectIdentity = ObjectIdentity
snsASQStatsGlobal = _SnsASQStatsGlobal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11256, 1, 12, 2)
)
_SnsASQStatsGlobalTimeSinceReset_Type = Counter32
_SnsASQStatsGlobalTimeSinceReset_Object = MibScalar
snsASQStatsGlobalTimeSinceReset = _SnsASQStatsGlobalTimeSinceReset_Object(
    (1, 3, 6, 1, 4, 1, 11256, 1, 12, 2, 1),
    _SnsASQStatsGlobalTimeSinceReset_Type()
)
snsASQStatsGlobalTimeSinceReset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snsASQStatsGlobalTimeSinceReset.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "STORMSHIELD-ASQ-STATS-MIB",
    **{"snsASQStats": snsASQStats,
       "snsASQStatsStateful": snsASQStatsStateful,
       "snsASQStatsStatefulPktBlocked": snsASQStatsStatefulPktBlocked,
       "snsASQStatsStatefulPktBlockedAsync": snsASQStatsStatefulPktBlockedAsync,
       "snsASQStatsStatefulPktBlockedSynProxy": snsASQStatsStatefulPktBlockedSynProxy,
       "snsASQStatsStatefulPktAccepted": snsASQStatsStatefulPktAccepted,
       "snsASQStatsStatefulLogged": snsASQStatsStatefulLogged,
       "snsASQStatsStatefulLogOverflow": snsASQStatsStatefulLogOverflow,
       "snsASQStatsStatefulFilterOverflow": snsASQStatsStatefulFilterOverflow,
       "snsASQStatsStatefulAlarmOverflow": snsASQStatsStatefulAlarmOverflow,
       "snsASQStatsStatefulSeismoFacts": snsASQStatsStatefulSeismoFacts,
       "snsASQStatsStatefulSeismoOverflow": snsASQStatsStatefulSeismoOverflow,
       "snsASQStatsStatefulMinorAlarm": snsASQStatsStatefulMinorAlarm,
       "snsASQStatsStatefulMajorAlarm": snsASQStatsStatefulMajorAlarm,
       "snsASQStatsStatefulPktFragmented": snsASQStatsStatefulPktFragmented,
       "snsASQStatsStatefulInBytes": snsASQStatsStatefulInBytes,
       "snsASQStatsStatefulOutBytes": snsASQStatsStatefulOutBytes,
       "snsASQStatsStatefulNatFailures": snsASQStatsStatefulNatFailures,
       "snsASQStatsStatefulFlowConflicts": snsASQStatsStatefulFlowConflicts,
       "snsASQStatsStatefulFlowFailures": snsASQStatsStatefulFlowFailures,
       "snsASQStatsStatefulInterfaceMute": snsASQStatsStatefulInterfaceMute,
       "snsASQStatsStatefulTcpPkt": snsASQStatsStatefulTcpPkt,
       "snsASQStatsStatefulTcpInBytes": snsASQStatsStatefulTcpInBytes,
       "snsASQStatsStatefulTcpOutBytes": snsASQStatsStatefulTcpOutBytes,
       "snsASQStatsStatefulTcpConn": snsASQStatsStatefulTcpConn,
       "snsASQStatsStatefulTcpNatConnSrc": snsASQStatsStatefulTcpNatConnSrc,
       "snsASQStatsStatefulTcpNatConnDst": snsASQStatsStatefulTcpNatConnDst,
       "snsASQStatsStatefulTcpNoNatConnSrc": snsASQStatsStatefulTcpNoNatConnSrc,
       "snsASQStatsStatefulTcpNoNatConnDst": snsASQStatsStatefulTcpNoNatConnDst,
       "snsASQStatsStatefulTcpSmallWindowRst": snsASQStatsStatefulTcpSmallWindowRst,
       "snsASQStatsStatefulTcpEmptyDupAckBlk": snsASQStatsStatefulTcpEmptyDupAckBlk,
       "snsASQStatsStatefulUdpPkt": snsASQStatsStatefulUdpPkt,
       "snsASQStatsStatefulUdpInBytes": snsASQStatsStatefulUdpInBytes,
       "snsASQStatsStatefulUdpOutBytes": snsASQStatsStatefulUdpOutBytes,
       "snsASQStatsStatefulUdpConn": snsASQStatsStatefulUdpConn,
       "snsASQStatsStatefulUdpNatConnSrc": snsASQStatsStatefulUdpNatConnSrc,
       "snsASQStatsStatefulUdpNatConnDst": snsASQStatsStatefulUdpNatConnDst,
       "snsASQStatsStatefulUdpNoNatConnSrc": snsASQStatsStatefulUdpNoNatConnSrc,
       "snsASQStatsStatefulUdpNoNatConnDst": snsASQStatsStatefulUdpNoNatConnDst,
       "snsASQStatsStatefulIcmpPkt": snsASQStatsStatefulIcmpPkt,
       "snsASQStatsStatefulIcmpInBytes": snsASQStatsStatefulIcmpInBytes,
       "snsASQStatsStatefulIcmpOutBytes": snsASQStatsStatefulIcmpOutBytes,
       "snsASQStatsStatefulHttpTimeoutRst": snsASQStatsStatefulHttpTimeoutRst,
       "snsASQStatsStatefulNatUnusable": snsASQStatsStatefulNatUnusable,
       "snsASQStatsGlobal": snsASQStatsGlobal,
       "snsASQStatsGlobalTimeSinceReset": snsASQStatsGlobalTimeSinceReset}
)
