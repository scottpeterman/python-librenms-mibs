# SNMP MIB module (F3-PTP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\adva\F3-PTP-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:16:44 2025
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

(fsp150cm,) = mibBuilder.importSymbols(
    "ADVA-MIB",
    "fsp150cm")

(AdminState,
 CmPmBinAction,
 CmPmIntervalType,
 F3DisplayString,
 FlowSecState,
 IpPriorityMapMode,
 IpVersion,
 OperationalState,
 PerfCounter64,
 SecondaryState) = mibBuilder.importSymbols(
    "CM-COMMON-MIB",
    "AdminState",
    "CmPmBinAction",
    "CmPmIntervalType",
    "F3DisplayString",
    "FlowSecState",
    "IpPriorityMapMode",
    "IpVersion",
    "OperationalState",
    "PerfCounter64",
    "SecondaryState")

(neIndex,
 shelfIndex,
 slotIndex) = mibBuilder.importSymbols(
    "CM-ENTITY-MIB",
    "neIndex",
    "shelfIndex",
    "slotIndex")

(cmEthernetAccPortEntry,
 cmEthernetAccPortIndex,
 cmEthernetNetPortEntry,
 cmEthernetNetPortIndex,
 cmEthernetTrafficPortEntry,
 cmEthernetTrafficPortIndex) = mibBuilder.importSymbols(
    "CM-FACILITY-MIB",
    "cmEthernetAccPortEntry",
    "cmEthernetAccPortIndex",
    "cmEthernetNetPortEntry",
    "cmEthernetNetPortIndex",
    "cmEthernetTrafficPortEntry",
    "cmEthernetTrafficPortIndex")

(CmGenPgSwitchoverReason,) = mibBuilder.importSymbols(
    "CM-REDUNDANCY-MIB",
    "CmGenPgSwitchoverReason")

(HoldoverAccuracy,
 SSMQualityLevel,
 TimeSource) = mibBuilder.importSymbols(
    "F3-SYNC-MIB",
    "HoldoverAccuracy",
    "SSMQualityLevel",
    "TimeSource")

(Ipv6Address,) = mibBuilder.importSymbols(
    "IPV6-TC",
    "Ipv6Address")

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

(DateAndTime,
 DisplayString,
 MacAddress,
 PhysAddress,
 RowStatus,
 StorageType,
 TextualConvention,
 TruthValue,
 VariablePointer) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "RowStatus",
    "StorageType",
    "TextualConvention",
    "TruthValue",
    "VariablePointer")


# MODULE-IDENTITY

f3PtpMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18)
)
if mibBuilder.loadTexts:
    f3PtpMIB.setRevisions(
        ("2020-02-10 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class SlaveMode(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("not-applicable", 0),
          ("unicast", 1),
          ("multicast", 2),
          ("hybrid", 3))
    )



class PtpFlowPointType(TextualConvention, Integer32):
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
        *(("transparent", 1),
          ("oc-slave", 2),
          ("monitoring", 3),
          ("oc-master", 4),
          ("eth-multicast", 5))
    )



class PtpPortState(TextualConvention, Integer32):
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
              10)
        )
    )
    namedValues = NamedValues(
        *(("initializing", 1),
          ("faulty", 2),
          ("disabled", 3),
          ("listening", 4),
          ("uncalibrated", 5),
          ("slave", 6),
          ("premaster", 7),
          ("master", 8),
          ("passive", 9),
          ("na", 10))
    )



class MasterClockType(TextualConvention, Integer32):
    status = "current"
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
          ("one-step", 2),
          ("two-step", 3))
    )



class PTPPortType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("master", 1),
          ("slave", 2))
    )



class DelayMechanism(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("end-to-end", 1)
    )



class ClockIdentity(TextualConvention, OctetString):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )
    fixed_length = 8



class PortIdentity(TextualConvention, OctetString):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(10, 10),
    )
    fixed_length = 10



class ClockRecoveryMode(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("one-way", 1),
          ("two-way", 2))
    )



class ClockRecoveryState(TextualConvention, Integer32):
    status = "current"
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
              9)
        )
    )
    namedValues = NamedValues(
        *(("not-applicable", 0),
          ("start", 1),
          ("normal", 2),
          ("freerun", 3),
          ("holdover", 4),
          ("acquisition", 5),
          ("transient", 6),
          ("none", 7),
          ("holdoverOutOfSpec", 8),
          ("holdoverInSpec", 9))
    )



class AnnounceMsgRate(TextualConvention, Integer32):
    status = "current"
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
              9)
        )
    )
    namedValues = NamedValues(
        *(("not-applicable", 0),
          ("pkt1per16secs", 1),
          ("pkt1per8secs", 2),
          ("pkt1per4secs", 3),
          ("pkt1per2secs", 4),
          ("pkt1per1sec", 5),
          ("pkts2per1sec", 6),
          ("pkts4per1sec", 7),
          ("pkts8per1sec", 8),
          ("none", 9))
    )



class SyncMsgRate(TextualConvention, Integer32):
    status = "current"
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
              9)
        )
    )
    namedValues = NamedValues(
        *(("not-applicable", 0),
          ("pkt1persec", 1),
          ("pkts2persec", 2),
          ("pkts4persec", 3),
          ("pkts8persec", 4),
          ("pkts16persec", 5),
          ("pkts32persec", 6),
          ("pkts64persec", 7),
          ("pkts128persec", 8),
          ("none", 9))
    )



class DelayRespMsgRate(TextualConvention, Integer32):
    status = "current"
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
              10,
              11)
        )
    )
    namedValues = NamedValues(
        *(("not-applicable", 0),
          ("pkt1persec", 1),
          ("pkts2persec", 2),
          ("pkts4persec", 3),
          ("pkts8persec", 4),
          ("pkts16persec", 5),
          ("pkts32persec", 6),
          ("pkts64persec", 7),
          ("pkts128persec", 8),
          ("none", 9),
          ("na", 10),
          ("pkts0persec", 11))
    )



class DelayReqMsgRate(TextualConvention, Integer32):
    status = "current"
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("not-applicable", 0),
          ("pkt1persec", 1),
          ("pkts2persec", 2),
          ("pkts4persec", 3),
          ("pkts8persec", 4),
          ("pkts16persec", 5),
          ("pkts32persec", 6),
          ("pkts64persec", 7),
          ("pkts128persec", 8))
    )



class FreqRecoveryTarget(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("not-applicable", 0),
          ("traffic-mask", 1),
          ("sync-mask", 2),
          ("traffic-sync-mask", 3))
    )



class ScaledNanoseconds(TextualConvention, Counter64):
    status = "current"


class RemoteSlaveType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dynamic", 1),
          ("static", 2))
    )



class TimeScale(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ptp", 1),
          ("arb", 2))
    )



class PhaseRecoveryState(TextualConvention, Integer32):
    status = "current"
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
              9)
        )
    )
    namedValues = NamedValues(
        *(("not-applicable", 0),
          ("freerun", 1),
          ("holdover", 2),
          ("normal", 3),
          ("start", 4),
          ("acquisition", 5),
          ("transient", 6),
          ("none", 7),
          ("holdoverOutOfSpec", 8),
          ("holdoverInSpec", 9))
    )



class PTPProtectionState(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("standby", 2))
    )



class CompensationMode(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("automatic", 2),
          ("manual", 3))
    )



class CompensationStatus(TextualConvention, Integer32):
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
        *(("operational", 1),
          ("failed", 2),
          ("not-available", 3),
          ("manual", 4),
          ("initializing", 5))
    )



class PTPClockProfile(TextualConvention, Integer32):
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
        *(("g8275-1", 1),
          ("ieee-1588-2008-annex-f", 2),
          ("ieee-1588-2008", 3),
          ("power-c37-238-2011", 4),
          ("power-c37-238-2017", 5),
          ("utility-iec-61850-9-3", 6),
          ("g8275-2", 7),
          ("gptp-802-1as-2011", 8))
    )



class PTPClockType(TextualConvention, Integer32):
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
        *(("master-only", 1),
          ("slave-only", 2),
          ("dynamic", 3),
          ("boundaryclock", 4),
          ("static-bc", 5))
    )



class PTPClockOperMode(TextualConvention, Integer32):
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
        *(("t-gm", 1),
          ("t-tsc", 2),
          ("idle", 3),
          ("t-bc", 4),
          ("gm", 5))
    )



class DestMacAddrType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("forwardable", 1),
          ("non-forwardable", 2))
    )



class AnnounceMessageRate(TextualConvention, Integer32):
    status = "current"
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
              9)
        )
    )
    namedValues = NamedValues(
        *(("not-applicable", 0),
          ("pkt1per16secs", 1),
          ("pkt1per8secs", 2),
          ("pkt1per4secs", 3),
          ("pkt1per2secs", 4),
          ("pkt1per1sec", 5),
          ("pkts2per1sec", 6),
          ("pkts4per1sec", 7),
          ("pkts8per1sec", 8),
          ("none", 9))
    )



class DelayReqMessageRate(TextualConvention, Integer32):
    status = "current"
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
        *(("not-applicable", 0),
          ("pkt1persec", 1),
          ("pkts2persec", 2),
          ("pkts4persec", 3),
          ("pkts8persec", 4),
          ("pkts16persec", 5),
          ("pkts32persec", 6),
          ("pkts64persec", 7),
          ("pkts128persec", 8),
          ("none", 9),
          ("na", 10))
    )



class SyncMessageRate(TextualConvention, Integer32):
    status = "current"
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
              9)
        )
    )
    namedValues = NamedValues(
        *(("not-applicable", 0),
          ("pkt1persec", 1),
          ("pkts2persec", 2),
          ("pkts4persec", 3),
          ("pkts8persec", 4),
          ("pkts16persec", 5),
          ("pkts32persec", 6),
          ("pkts64persec", 7),
          ("pkts128persec", 8),
          ("none", 9))
    )



class BMCARole(TextualConvention, Integer32):
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
              7)
        )
    )
    namedValues = NamedValues(
        *(("m1", 1),
          ("m2", 2),
          ("m3", 3),
          ("s1", 4),
          ("p1", 5),
          ("p2", 6),
          ("na", 7))
    )



class ClockClassProfile(TextualConvention, Integer32):
    status = "current"
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
        *(("g82651", 1),
          ("ieee-1588-2008", 2),
          ("ptp-enterprise", 3),
          ("na", 4),
          ("g82752", 5),
          ("ptp-enterprise-and-ieee-1588-2008", 6))
    )



class PTPProfile(TextualConvention, Integer32):
    status = "current"
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
        *(("g82651", 1),
          ("ptp-enterprise", 2),
          ("ieee-1588-2008", 3),
          ("g82752", 4),
          ("aes67-media", 5),
          ("smpte-st-2059-2", 6))
    )



class PTPTransport(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ethernet", 1),
          ("udp-over-ipv4", 2),
          ("udp-over-ipv6", 3))
    )



class PTPTransportMode(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("unicast", 1),
          ("multicast", 2))
    )



class ToggleValue(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 1),
          ("disabled", 2),
          ("not-available", 3))
    )



# MIB Managed Objects in the order of their OIDs

_F3PtpConfigObjects_ObjectIdentity = ObjectIdentity
f3PtpConfigObjects = _F3PtpConfigObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 1)
)
_F3PtpTCTable_Object = MibTable
f3PtpTCTable = _F3PtpTCTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 1, 1)
)
if mibBuilder.loadTexts:
    f3PtpTCTable.setStatus("current")
_F3PtpTCEntry_Object = MibTableRow
f3PtpTCEntry = _F3PtpTCEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 1, 1, 1)
)
f3PtpTCEntry.setIndexNames(
    (0, "CM-ENTITY-MIB", "neIndex"),
    (0, "F3-PTP-MIB", "f3PtpTCIndex"),
)
if mibBuilder.loadTexts:
    f3PtpTCEntry.setStatus("current")
_F3PtpTCIndex_Type = Integer32
_F3PtpTCIndex_Object = MibTableColumn
f3PtpTCIndex = _F3PtpTCIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 1, 1, 1, 1),
    _F3PtpTCIndex_Type()
)
f3PtpTCIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    f3PtpTCIndex.setStatus("current")


class _F3PtpTCAlias_Type(DisplayString):
    """Custom type f3PtpTCAlias based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_F3PtpTCAlias_Type.__name__ = "DisplayString"
_F3PtpTCAlias_Object = MibTableColumn
f3PtpTCAlias = _F3PtpTCAlias_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 1, 1, 1, 2),
    _F3PtpTCAlias_Type()
)
f3PtpTCAlias.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3PtpTCAlias.setStatus("current")
_F3PtpTCAdminState_Type = AdminState
_F3PtpTCAdminState_Object = MibTableColumn
f3PtpTCAdminState = _F3PtpTCAdminState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 1, 1, 1, 3),
    _F3PtpTCAdminState_Type()
)
f3PtpTCAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3PtpTCAdminState.setStatus("current")
_F3PtpTCOperationalState_Type = OperationalState
_F3PtpTCOperationalState_Object = MibTableColumn
f3PtpTCOperationalState = _F3PtpTCOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 1, 1, 1, 4),
    _F3PtpTCOperationalState_Type()
)
f3PtpTCOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpTCOperationalState.setStatus("current")
_F3PtpTCSecondaryState_Type = SecondaryState
_F3PtpTCSecondaryState_Object = MibTableColumn
f3PtpTCSecondaryState = _F3PtpTCSecondaryState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 1, 1, 1, 5),
    _F3PtpTCSecondaryState_Type()
)
f3PtpTCSecondaryState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpTCSecondaryState.setStatus("current")
_F3PtpTCServiceFlow_Type = VariablePointer
_F3PtpTCServiceFlow_Object = MibTableColumn
f3PtpTCServiceFlow = _F3PtpTCServiceFlow_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 1, 1, 1, 6),
    _F3PtpTCServiceFlow_Type()
)
f3PtpTCServiceFlow.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3PtpTCServiceFlow.setStatus("current")
_F3PtpTCDelayMechanism_Type = DelayMechanism
_F3PtpTCDelayMechanism_Object = MibTableColumn
f3PtpTCDelayMechanism = _F3PtpTCDelayMechanism_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 1, 1, 1, 7),
    _F3PtpTCDelayMechanism_Type()
)
f3PtpTCDelayMechanism.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3PtpTCDelayMechanism.setStatus("current")
_F3PtpTCSync_Type = VariablePointer
_F3PtpTCSync_Object = MibTableColumn
f3PtpTCSync = _F3PtpTCSync_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 1, 1, 1, 8),
    _F3PtpTCSync_Type()
)
f3PtpTCSync.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3PtpTCSync.setStatus("current")
_F3PtpTCClockIdentity_Type = ClockIdentity
_F3PtpTCClockIdentity_Object = MibTableColumn
f3PtpTCClockIdentity = _F3PtpTCClockIdentity_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 1, 1, 1, 9),
    _F3PtpTCClockIdentity_Type()
)
f3PtpTCClockIdentity.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3PtpTCClockIdentity.setStatus("current")
_F3PtpTCStorageType_Type = StorageType
_F3PtpTCStorageType_Object = MibTableColumn
f3PtpTCStorageType = _F3PtpTCStorageType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 1, 1, 1, 10),
    _F3PtpTCStorageType_Type()
)
f3PtpTCStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3PtpTCStorageType.setStatus("current")
_F3PtpTCRowStatus_Type = RowStatus
_F3PtpTCRowStatus_Object = MibTableColumn
f3PtpTCRowStatus = _F3PtpTCRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 1, 1, 1, 11),
    _F3PtpTCRowStatus_Type()
)
f3PtpTCRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3PtpTCRowStatus.setStatus("current")
_F3PtpTCPtpProfile_Type = PTPClockProfile
_F3PtpTCPtpProfile_Object = MibTableColumn
f3PtpTCPtpProfile = _F3PtpTCPtpProfile_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 1, 1, 1, 12),
    _F3PtpTCPtpProfile_Type()
)
f3PtpTCPtpProfile.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3PtpTCPtpProfile.setStatus("current")
_F3PtpTCVirtualPortTable_Object = MibTable
f3PtpTCVirtualPortTable = _F3PtpTCVirtualPortTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 1, 2)
)
if mibBuilder.loadTexts:
    f3PtpTCVirtualPortTable.setStatus("current")
_F3PtpTCVirtualPortEntry_Object = MibTableRow
f3PtpTCVirtualPortEntry = _F3PtpTCVirtualPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 1, 2, 1)
)
f3PtpTCVirtualPortEntry.setIndexNames(
    (0, "CM-ENTITY-MIB", "neIndex"),
    (0, "F3-PTP-MIB", "f3PtpTCIndex"),
    (0, "F3-PTP-MIB", "f3PtpTCVirtualPortIndex"),
)
if mibBuilder.loadTexts:
    f3PtpTCVirtualPortEntry.setStatus("current")
_F3PtpTCVirtualPortIndex_Type = Integer32
_F3PtpTCVirtualPortIndex_Object = MibTableColumn
f3PtpTCVirtualPortIndex = _F3PtpTCVirtualPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 1, 2, 1, 1),
    _F3PtpTCVirtualPortIndex_Type()
)
f3PtpTCVirtualPortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    f3PtpTCVirtualPortIndex.setStatus("current")


class _F3PtpTCVirtualPortAlias_Type(DisplayString):
    """Custom type f3PtpTCVirtualPortAlias based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_F3PtpTCVirtualPortAlias_Type.__name__ = "DisplayString"
_F3PtpTCVirtualPortAlias_Object = MibTableColumn
f3PtpTCVirtualPortAlias = _F3PtpTCVirtualPortAlias_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 1, 2, 1, 2),
    _F3PtpTCVirtualPortAlias_Type()
)
f3PtpTCVirtualPortAlias.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3PtpTCVirtualPortAlias.setStatus("current")
_F3PtpTCVirtualPortAdminState_Type = AdminState
_F3PtpTCVirtualPortAdminState_Object = MibTableColumn
f3PtpTCVirtualPortAdminState = _F3PtpTCVirtualPortAdminState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 1, 2, 1, 3),
    _F3PtpTCVirtualPortAdminState_Type()
)
f3PtpTCVirtualPortAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3PtpTCVirtualPortAdminState.setStatus("current")
_F3PtpTCVirtualPortOperationalState_Type = OperationalState
_F3PtpTCVirtualPortOperationalState_Object = MibTableColumn
f3PtpTCVirtualPortOperationalState = _F3PtpTCVirtualPortOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 1, 2, 1, 4),
    _F3PtpTCVirtualPortOperationalState_Type()
)
f3PtpTCVirtualPortOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpTCVirtualPortOperationalState.setStatus("current")
_F3PtpTCVirtualPortSecondaryState_Type = SecondaryState
_F3PtpTCVirtualPortSecondaryState_Object = MibTableColumn
f3PtpTCVirtualPortSecondaryState = _F3PtpTCVirtualPortSecondaryState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 1, 2, 1, 5),
    _F3PtpTCVirtualPortSecondaryState_Type()
)
f3PtpTCVirtualPortSecondaryState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpTCVirtualPortSecondaryState.setStatus("current")
_F3PtpTCVirtualPortIdentity_Type = PortIdentity
_F3PtpTCVirtualPortIdentity_Object = MibTableColumn
f3PtpTCVirtualPortIdentity = _F3PtpTCVirtualPortIdentity_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 1, 2, 1, 6),
    _F3PtpTCVirtualPortIdentity_Type()
)
f3PtpTCVirtualPortIdentity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3PtpTCVirtualPortIdentity.setStatus("current")
_F3PtpTCVirtualPortFlowPoint_Type = VariablePointer
_F3PtpTCVirtualPortFlowPoint_Object = MibTableColumn
f3PtpTCVirtualPortFlowPoint = _F3PtpTCVirtualPortFlowPoint_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 1, 2, 1, 7),
    _F3PtpTCVirtualPortFlowPoint_Type()
)
f3PtpTCVirtualPortFlowPoint.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3PtpTCVirtualPortFlowPoint.setStatus("current")
_F3PtpTCVirtualPortStorageType_Type = StorageType
_F3PtpTCVirtualPortStorageType_Object = MibTableColumn
f3PtpTCVirtualPortStorageType = _F3PtpTCVirtualPortStorageType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 1, 2, 1, 8),
    _F3PtpTCVirtualPortStorageType_Type()
)
f3PtpTCVirtualPortStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3PtpTCVirtualPortStorageType.setStatus("current")
_F3PtpTCVirtualPortRowStatus_Type = RowStatus
_F3PtpTCVirtualPortRowStatus_Object = MibTableColumn
f3PtpTCVirtualPortRowStatus = _F3PtpTCVirtualPortRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 1, 2, 1, 9),
    _F3PtpTCVirtualPortRowStatus_Type()
)
f3PtpTCVirtualPortRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3PtpTCVirtualPortRowStatus.setStatus("current")
_F3PtpTSTable_Object = MibTable
f3PtpTSTable = _F3PtpTSTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 1, 3)
)
if mibBuilder.loadTexts:
    f3PtpTSTable.setStatus("current")
_F3PtpTSEntry_Object = MibTableRow
f3PtpTSEntry = _F3PtpTSEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 1, 3, 1)
)
f3PtpTSEntry.setIndexNames(
    (0, "CM-ENTITY-MIB", "neIndex"),
    (0, "F3-PTP-MIB", "f3PtpTSIndex"),
)
if mibBuilder.loadTexts:
    f3PtpTSEntry.setStatus("current")
_F3PtpTSIndex_Type = Integer32
_F3PtpTSIndex_Object = MibTableColumn
f3PtpTSIndex = _F3PtpTSIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 1, 3, 1, 1),
    _F3PtpTSIndex_Type()
)
f3PtpTSIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    f3PtpTSIndex.setStatus("current")


class _F3PtpTSAlias_Type(DisplayString):
    """Custom type f3PtpTSAlias based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_F3PtpTSAlias_Type.__name__ = "DisplayString"
_F3PtpTSAlias_Object = MibTableColumn
f3PtpTSAlias = _F3PtpTSAlias_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 1, 3, 1, 2),
    _F3PtpTSAlias_Type()
)
f3PtpTSAlias.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3PtpTSAlias.setStatus("current")
_F3PtpTSAdminState_Type = AdminState
_F3PtpTSAdminState_Object = MibTableColumn
f3PtpTSAdminState = _F3PtpTSAdminState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 1, 3, 1, 3),
    _F3PtpTSAdminState_Type()
)
f3PtpTSAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3PtpTSAdminState.setStatus("current")
_F3PtpTSOperationalState_Type = OperationalState
_F3PtpTSOperationalState_Object = MibTableColumn
f3PtpTSOperationalState = _F3PtpTSOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 1, 3, 1, 4),
    _F3PtpTSOperationalState_Type()
)
f3PtpTSOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpTSOperationalState.setStatus("current")
_F3PtpTSSecondaryState_Type = SecondaryState
_F3PtpTSSecondaryState_Object = MibTableColumn
f3PtpTSSecondaryState = _F3PtpTSSecondaryState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 1, 3, 1, 5),
    _F3PtpTSSecondaryState_Type()
)
f3PtpTSSecondaryState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpTSSecondaryState.setStatus("current")
_F3PtpTSClockIdentity_Type = ClockIdentity
_F3PtpTSClockIdentity_Object = MibTableColumn
f3PtpTSClockIdentity = _F3PtpTSClockIdentity_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 1, 3, 1, 6),
    _F3PtpTSClockIdentity_Type()
)
f3PtpTSClockIdentity.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3PtpTSClockIdentity.setStatus("current")
_F3PtpTSDomainNumber_Type = Integer32
_F3PtpTSDomainNumber_Object = MibTableColumn
f3PtpTSDomainNumber = _F3PtpTSDomainNumber_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 1, 3, 1, 7),
    _F3PtpTSDomainNumber_Type()
)
f3PtpTSDomainNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3PtpTSDomainNumber.setStatus("current")
_F3PtpTSSync_Type = VariablePointer
_F3PtpTSSync_Object = MibTableColumn
f3PtpTSSync = _F3PtpTSSync_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 1, 3, 1, 8),
    _F3PtpTSSync_Type()
)
f3PtpTSSync.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3PtpTSSync.setStatus("current")
_F3PtpTSCurrentTOD_Type = DateAndTime
_F3PtpTSCurrentTOD_Object = MibTableColumn
f3PtpTSCurrentTOD = _F3PtpTSCurrentTOD_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 1, 3, 1, 9),
    _F3PtpTSCurrentTOD_Type()
)
f3PtpTSCurrentTOD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpTSCurrentTOD.setStatus("current")
_F3PtpTSSelectedPacketClock_Type = VariablePointer
_F3PtpTSSelectedPacketClock_Object = MibTableColumn
f3PtpTSSelectedPacketClock = _F3PtpTSSelectedPacketClock_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 1, 3, 1, 10),
    _F3PtpTSSelectedPacketClock_Type()
)
f3PtpTSSelectedPacketClock.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpTSSelectedPacketClock.setStatus("current")
_F3PtpTSClockRecoveryMode_Type = ClockRecoveryMode
_F3PtpTSClockRecoveryMode_Object = MibTableColumn
f3PtpTSClockRecoveryMode = _F3PtpTSClockRecoveryMode_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 1, 3, 1, 11),
    _F3PtpTSClockRecoveryMode_Type()
)
f3PtpTSClockRecoveryMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3PtpTSClockRecoveryMode.setStatus("current")
_F3PtpTSClockRecoveryState_Type = ClockRecoveryState
_F3PtpTSClockRecoveryState_Object = MibTableColumn
f3PtpTSClockRecoveryState = _F3PtpTSClockRecoveryState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 1, 3, 1, 12),
    _F3PtpTSClockRecoveryState_Type()
)
f3PtpTSClockRecoveryState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpTSClockRecoveryState.setStatus("current")
_F3PtpTSClockSyncEEnabled_Type = TruthValue
_F3PtpTSClockSyncEEnabled_Object = MibTableColumn
f3PtpTSClockSyncEEnabled = _F3PtpTSClockSyncEEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 1, 3, 1, 13),
    _F3PtpTSClockSyncEEnabled_Type()
)
f3PtpTSClockSyncEEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3PtpTSClockSyncEEnabled.setStatus("current")
_F3PtpTSClockQLModeEnabled_Type = TruthValue
_F3PtpTSClockQLModeEnabled_Object = MibTableColumn
f3PtpTSClockQLModeEnabled = _F3PtpTSClockQLModeEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 1, 3, 1, 14),
    _F3PtpTSClockQLModeEnabled_Type()
)
f3PtpTSClockQLModeEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3PtpTSClockQLModeEnabled.setStatus("current")
_F3PtpTSClockExpectedQL_Type = SSMQualityLevel
_F3PtpTSClockExpectedQL_Object = MibTableColumn
f3PtpTSClockExpectedQL = _F3PtpTSClockExpectedQL_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 1, 3, 1, 15),
    _F3PtpTSClockExpectedQL_Type()
)
f3PtpTSClockExpectedQL.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3PtpTSClockExpectedQL.setStatus("current")
_F3PtpTSClockAssumedQL_Type = SSMQualityLevel
_F3PtpTSClockAssumedQL_Object = MibTableColumn
f3PtpTSClockAssumedQL = _F3PtpTSClockAssumedQL_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 1, 3, 1, 16),
    _F3PtpTSClockAssumedQL_Type()
)
f3PtpTSClockAssumedQL.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3PtpTSClockAssumedQL.setStatus("current")
_F3PtpTSClockReceivedQL_Type = SSMQualityLevel
_F3PtpTSClockReceivedQL_Object = MibTableColumn
f3PtpTSClockReceivedQL = _F3PtpTSClockReceivedQL_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 1, 3, 1, 17),
    _F3PtpTSClockReceivedQL_Type()
)
f3PtpTSClockReceivedQL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpTSClockReceivedQL.setStatus("current")
_F3PtpTSStorageType_Type = StorageType
_F3PtpTSStorageType_Object = MibTableColumn
f3PtpTSStorageType = _F3PtpTSStorageType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 1, 3, 1, 18),
    _F3PtpTSStorageType_Type()
)
f3PtpTSStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3PtpTSStorageType.setStatus("current")
_F3PtpTSRowStatus_Type = RowStatus
_F3PtpTSRowStatus_Object = MibTableColumn
f3PtpTSRowStatus = _F3PtpTSRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 1, 3, 1, 19),
    _F3PtpTSRowStatus_Type()
)
f3PtpTSRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3PtpTSRowStatus.setStatus("current")
_F3PtpTSTimeTraceabilityStatus_Type = TruthValue
_F3PtpTSTimeTraceabilityStatus_Object = MibTableColumn
f3PtpTSTimeTraceabilityStatus = _F3PtpTSTimeTraceabilityStatus_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 1, 3, 1, 20),
    _F3PtpTSTimeTraceabilityStatus_Type()
)
f3PtpTSTimeTraceabilityStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpTSTimeTraceabilityStatus.setStatus("current")
_F3PtpTSTimeSinceTimeTraceabilityChanged_Type = Unsigned32
_F3PtpTSTimeSinceTimeTraceabilityChanged_Object = MibTableColumn
f3PtpTSTimeSinceTimeTraceabilityChanged = _F3PtpTSTimeSinceTimeTraceabilityChanged_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 1, 3, 1, 21),
    _F3PtpTSTimeSinceTimeTraceabilityChanged_Type()
)
f3PtpTSTimeSinceTimeTraceabilityChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpTSTimeSinceTimeTraceabilityChanged.setStatus("current")
_F3PtpTSFreqTraceabilityStatus_Type = TruthValue
_F3PtpTSFreqTraceabilityStatus_Object = MibTableColumn
f3PtpTSFreqTraceabilityStatus = _F3PtpTSFreqTraceabilityStatus_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 1, 3, 1, 22),
    _F3PtpTSFreqTraceabilityStatus_Type()
)
f3PtpTSFreqTraceabilityStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpTSFreqTraceabilityStatus.setStatus("current")
_F3PtpTSTimeSinceFreqTraceabilityChanged_Type = Unsigned32
_F3PtpTSTimeSinceFreqTraceabilityChanged_Object = MibTableColumn
f3PtpTSTimeSinceFreqTraceabilityChanged = _F3PtpTSTimeSinceFreqTraceabilityChanged_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 1, 3, 1, 23),
    _F3PtpTSTimeSinceFreqTraceabilityChanged_Type()
)
f3PtpTSTimeSinceFreqTraceabilityChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpTSTimeSinceFreqTraceabilityChanged.setStatus("current")
_F3PtpTSFreqRecoveryTarget_Type = FreqRecoveryTarget
_F3PtpTSFreqRecoveryTarget_Object = MibTableColumn
f3PtpTSFreqRecoveryTarget = _F3PtpTSFreqRecoveryTarget_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 1, 3, 1, 24),
    _F3PtpTSFreqRecoveryTarget_Type()
)
f3PtpTSFreqRecoveryTarget.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3PtpTSFreqRecoveryTarget.setStatus("current")
_F3PtpTSCurrentCRScore_Type = Unsigned32
_F3PtpTSCurrentCRScore_Object = MibTableColumn
f3PtpTSCurrentCRScore = _F3PtpTSCurrentCRScore_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 1, 3, 1, 25),
    _F3PtpTSCurrentCRScore_Type()
)
f3PtpTSCurrentCRScore.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpTSCurrentCRScore.setStatus("current")
_F3PtpTSTimeLastCRScore_Type = DateAndTime
_F3PtpTSTimeLastCRScore_Object = MibTableColumn
f3PtpTSTimeLastCRScore = _F3PtpTSTimeLastCRScore_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 1, 3, 1, 26),
    _F3PtpTSTimeLastCRScore_Type()
)
f3PtpTSTimeLastCRScore.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpTSTimeLastCRScore.setStatus("current")
_F3PtpTSTargetPhaseRecoveryAccuracy_Type = Unsigned32
_F3PtpTSTargetPhaseRecoveryAccuracy_Object = MibTableColumn
f3PtpTSTargetPhaseRecoveryAccuracy = _F3PtpTSTargetPhaseRecoveryAccuracy_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 1, 3, 1, 27),
    _F3PtpTSTargetPhaseRecoveryAccuracy_Type()
)
f3PtpTSTargetPhaseRecoveryAccuracy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3PtpTSTargetPhaseRecoveryAccuracy.setStatus("current")
_F3PtpTSCurrentPRScore_Type = Unsigned32
_F3PtpTSCurrentPRScore_Object = MibTableColumn
f3PtpTSCurrentPRScore = _F3PtpTSCurrentPRScore_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 1, 3, 1, 28),
    _F3PtpTSCurrentPRScore_Type()
)
f3PtpTSCurrentPRScore.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpTSCurrentPRScore.setStatus("current")
_F3PtpTSTimeLastPRScore_Type = DateAndTime
_F3PtpTSTimeLastPRScore_Object = MibTableColumn
f3PtpTSTimeLastPRScore = _F3PtpTSTimeLastPRScore_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 1, 3, 1, 29),
    _F3PtpTSTimeLastPRScore_Type()
)
f3PtpTSTimeLastPRScore.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpTSTimeLastPRScore.setStatus("current")
_F3PtpTSClockClass_Type = Unsigned32
_F3PtpTSClockClass_Object = MibTableColumn
f3PtpTSClockClass = _F3PtpTSClockClass_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 1, 3, 1, 30),
    _F3PtpTSClockClass_Type()
)
f3PtpTSClockClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpTSClockClass.setStatus("deprecated")
_F3PtpTSClockAccuracy_Type = Unsigned32
_F3PtpTSClockAccuracy_Object = MibTableColumn
f3PtpTSClockAccuracy = _F3PtpTSClockAccuracy_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 1, 3, 1, 31),
    _F3PtpTSClockAccuracy_Type()
)
f3PtpTSClockAccuracy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpTSClockAccuracy.setStatus("current")
_F3PtpTSTimeSource_Type = TimeSource
_F3PtpTSTimeSource_Object = MibTableColumn
f3PtpTSTimeSource = _F3PtpTSTimeSource_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 1, 3, 1, 32),
    _F3PtpTSTimeSource_Type()
)
f3PtpTSTimeSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpTSTimeSource.setStatus("current")
_F3PtpTSPhaseRecoveryState_Type = PhaseRecoveryState
_F3PtpTSPhaseRecoveryState_Object = MibTableColumn
f3PtpTSPhaseRecoveryState = _F3PtpTSPhaseRecoveryState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 1, 3, 1, 33),
    _F3PtpTSPhaseRecoveryState_Type()
)
f3PtpTSPhaseRecoveryState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpTSPhaseRecoveryState.setStatus("current")
_F3PtpTSTimeHoldoverAccuracy_Type = HoldoverAccuracy
_F3PtpTSTimeHoldoverAccuracy_Object = MibTableColumn
f3PtpTSTimeHoldoverAccuracy = _F3PtpTSTimeHoldoverAccuracy_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 1, 3, 1, 34),
    _F3PtpTSTimeHoldoverAccuracy_Type()
)
f3PtpTSTimeHoldoverAccuracy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3PtpTSTimeHoldoverAccuracy.setStatus("current")


class _F3PtpTSWtrTime_Type(Integer32):
    """Custom type f3PtpTSWtrTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 12),
    )


_F3PtpTSWtrTime_Type.__name__ = "Integer32"
_F3PtpTSWtrTime_Object = MibTableColumn
f3PtpTSWtrTime = _F3PtpTSWtrTime_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 1, 3, 1, 35),
    _F3PtpTSWtrTime_Type()
)
f3PtpTSWtrTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3PtpTSWtrTime.setStatus("current")
_F3PtpSOOCTable_Object = MibTable
f3PtpSOOCTable = _F3PtpSOOCTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 1, 4)
)
if mibBuilder.loadTexts:
    f3PtpSOOCTable.setStatus("current")
_F3PtpSOOCEntry_Object = MibTableRow
f3PtpSOOCEntry = _F3PtpSOOCEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 1, 4, 1)
)
f3PtpSOOCEntry.setIndexNames(
    (0, "CM-ENTITY-MIB", "neIndex"),
    (0, "F3-PTP-MIB", "f3PtpTSIndex"),
    (0, "F3-PTP-MIB", "f3PtpSOOCIndex"),
)
if mibBuilder.loadTexts:
    f3PtpSOOCEntry.setStatus("current")
_F3PtpSOOCIndex_Type = Integer32
_F3PtpSOOCIndex_Object = MibTableColumn
f3PtpSOOCIndex = _F3PtpSOOCIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 1, 4, 1, 1),
    _F3PtpSOOCIndex_Type()
)
f3PtpSOOCIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    f3PtpSOOCIndex.setStatus("current")


class _F3PtpSOOCName_Type(DisplayString):
    """Custom type f3PtpSOOCName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 15),
    )


_F3PtpSOOCName_Type.__name__ = "DisplayString"
_F3PtpSOOCName_Object = MibTableColumn
f3PtpSOOCName = _F3PtpSOOCName_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 1, 4, 1, 2),
    _F3PtpSOOCName_Type()
)
f3PtpSOOCName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3PtpSOOCName.setStatus("current")


class _F3PtpSOOCAlias_Type(DisplayString):
    """Custom type f3PtpSOOCAlias based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_F3PtpSOOCAlias_Type.__name__ = "DisplayString"
_F3PtpSOOCAlias_Object = MibTableColumn
f3PtpSOOCAlias = _F3PtpSOOCAlias_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 1, 4, 1, 3),
    _F3PtpSOOCAlias_Type()
)
f3PtpSOOCAlias.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3PtpSOOCAlias.setStatus("current")
_F3PtpSOOCAdminState_Type = AdminState
_F3PtpSOOCAdminState_Object = MibTableColumn
f3PtpSOOCAdminState = _F3PtpSOOCAdminState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 1, 4, 1, 4),
    _F3PtpSOOCAdminState_Type()
)
f3PtpSOOCAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3PtpSOOCAdminState.setStatus("current")
_F3PtpSOOCOperationalState_Type = OperationalState
_F3PtpSOOCOperationalState_Object = MibTableColumn
f3PtpSOOCOperationalState = _F3PtpSOOCOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 1, 4, 1, 5),
    _F3PtpSOOCOperationalState_Type()
)
f3PtpSOOCOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpSOOCOperationalState.setStatus("current")
_F3PtpSOOCSecondaryState_Type = SecondaryState
_F3PtpSOOCSecondaryState_Object = MibTableColumn
f3PtpSOOCSecondaryState = _F3PtpSOOCSecondaryState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 1, 4, 1, 6),
    _F3PtpSOOCSecondaryState_Type()
)
f3PtpSOOCSecondaryState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpSOOCSecondaryState.setStatus("current")
_F3PtpSOOCServiceFlow_Type = VariablePointer
_F3PtpSOOCServiceFlow_Object = MibTableColumn
f3PtpSOOCServiceFlow = _F3PtpSOOCServiceFlow_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 1, 4, 1, 7),
    _F3PtpSOOCServiceFlow_Type()
)
f3PtpSOOCServiceFlow.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3PtpSOOCServiceFlow.setStatus("current")
_F3PtpSOOCMasterClockType_Type = MasterClockType
_F3PtpSOOCMasterClockType_Object = MibTableColumn
f3PtpSOOCMasterClockType = _F3PtpSOOCMasterClockType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 1, 4, 1, 8),
    _F3PtpSOOCMasterClockType_Type()
)
f3PtpSOOCMasterClockType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpSOOCMasterClockType.setStatus("current")
_F3PtpSOOCUnicastMessageNegEnabled_Type = TruthValue
_F3PtpSOOCUnicastMessageNegEnabled_Object = MibTableColumn
f3PtpSOOCUnicastMessageNegEnabled = _F3PtpSOOCUnicastMessageNegEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 1, 4, 1, 9),
    _F3PtpSOOCUnicastMessageNegEnabled_Type()
)
f3PtpSOOCUnicastMessageNegEnabled.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3PtpSOOCUnicastMessageNegEnabled.setStatus("current")
_F3PtpSOOCMasterDelayMechanism_Type = DelayMechanism
_F3PtpSOOCMasterDelayMechanism_Object = MibTableColumn
f3PtpSOOCMasterDelayMechanism = _F3PtpSOOCMasterDelayMechanism_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 1, 4, 1, 10),
    _F3PtpSOOCMasterDelayMechanism_Type()
)
f3PtpSOOCMasterDelayMechanism.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3PtpSOOCMasterDelayMechanism.setStatus("current")
_F3PtpSOOCMasterPriority_Type = Integer32
_F3PtpSOOCMasterPriority_Object = MibTableColumn
f3PtpSOOCMasterPriority = _F3PtpSOOCMasterPriority_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 1, 4, 1, 11),
    _F3PtpSOOCMasterPriority_Type()
)
f3PtpSOOCMasterPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3PtpSOOCMasterPriority.setStatus("current")
_F3PtpSOOCMasterIpProtocol_Type = IpVersion
_F3PtpSOOCMasterIpProtocol_Object = MibTableColumn
f3PtpSOOCMasterIpProtocol = _F3PtpSOOCMasterIpProtocol_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 1, 4, 1, 12),
    _F3PtpSOOCMasterIpProtocol_Type()
)
f3PtpSOOCMasterIpProtocol.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3PtpSOOCMasterIpProtocol.setStatus("current")
_F3PtpSOOCSlaveIpV4Address_Type = IpAddress
_F3PtpSOOCSlaveIpV4Address_Object = MibTableColumn
f3PtpSOOCSlaveIpV4Address = _F3PtpSOOCSlaveIpV4Address_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 1, 4, 1, 13),
    _F3PtpSOOCSlaveIpV4Address_Type()
)
f3PtpSOOCSlaveIpV4Address.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3PtpSOOCSlaveIpV4Address.setStatus("current")
_F3PtpSOOCSlaveIpV4SubnetMask_Type = IpAddress
_F3PtpSOOCSlaveIpV4SubnetMask_Object = MibTableColumn
f3PtpSOOCSlaveIpV4SubnetMask = _F3PtpSOOCSlaveIpV4SubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 1, 4, 1, 14),
    _F3PtpSOOCSlaveIpV4SubnetMask_Type()
)
f3PtpSOOCSlaveIpV4SubnetMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3PtpSOOCSlaveIpV4SubnetMask.setStatus("current")
_F3PtpSOOCMasterIpV4Address_Type = IpAddress
_F3PtpSOOCMasterIpV4Address_Object = MibTableColumn
f3PtpSOOCMasterIpV4Address = _F3PtpSOOCMasterIpV4Address_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 1, 4, 1, 15),
    _F3PtpSOOCMasterIpV4Address_Type()
)
f3PtpSOOCMasterIpV4Address.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3PtpSOOCMasterIpV4Address.setStatus("current")
_F3PtpSOOCIpPriorityMapMode_Type = IpPriorityMapMode
_F3PtpSOOCIpPriorityMapMode_Object = MibTableColumn
f3PtpSOOCIpPriorityMapMode = _F3PtpSOOCIpPriorityMapMode_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 1, 4, 1, 16),
    _F3PtpSOOCIpPriorityMapMode_Type()
)
f3PtpSOOCIpPriorityMapMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3PtpSOOCIpPriorityMapMode.setStatus("current")


class _F3PtpSOOCIpPriority_Type(Integer32):
    """Custom type f3PtpSOOCIpPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_F3PtpSOOCIpPriority_Type.__name__ = "Integer32"
_F3PtpSOOCIpPriority_Object = MibTableColumn
f3PtpSOOCIpPriority = _F3PtpSOOCIpPriority_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 1, 4, 1, 17),
    _F3PtpSOOCIpPriority_Type()
)
f3PtpSOOCIpPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3PtpSOOCIpPriority.setStatus("current")
_F3PtpSOOCMasterLeaseDuration_Type = Integer32
_F3PtpSOOCMasterLeaseDuration_Object = MibTableColumn
f3PtpSOOCMasterLeaseDuration = _F3PtpSOOCMasterLeaseDuration_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 1, 4, 1, 18),
    _F3PtpSOOCMasterLeaseDuration_Type()
)
f3PtpSOOCMasterLeaseDuration.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3PtpSOOCMasterLeaseDuration.setStatus("current")
_F3PtpSOOCMasterAnnounceMsgRate_Type = AnnounceMsgRate
_F3PtpSOOCMasterAnnounceMsgRate_Object = MibTableColumn
f3PtpSOOCMasterAnnounceMsgRate = _F3PtpSOOCMasterAnnounceMsgRate_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 1, 4, 1, 19),
    _F3PtpSOOCMasterAnnounceMsgRate_Type()
)
f3PtpSOOCMasterAnnounceMsgRate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3PtpSOOCMasterAnnounceMsgRate.setStatus("current")
_F3PtpSOOCMasterAnnounceMsgReceiptTimeout_Type = Integer32
_F3PtpSOOCMasterAnnounceMsgReceiptTimeout_Object = MibTableColumn
f3PtpSOOCMasterAnnounceMsgReceiptTimeout = _F3PtpSOOCMasterAnnounceMsgReceiptTimeout_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 1, 4, 1, 20),
    _F3PtpSOOCMasterAnnounceMsgReceiptTimeout_Type()
)
f3PtpSOOCMasterAnnounceMsgReceiptTimeout.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3PtpSOOCMasterAnnounceMsgReceiptTimeout.setStatus("current")
_F3PtpSOOCMasterSyncMsgRate_Type = SyncMsgRate
_F3PtpSOOCMasterSyncMsgRate_Object = MibTableColumn
f3PtpSOOCMasterSyncMsgRate = _F3PtpSOOCMasterSyncMsgRate_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 1, 4, 1, 21),
    _F3PtpSOOCMasterSyncMsgRate_Type()
)
f3PtpSOOCMasterSyncMsgRate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3PtpSOOCMasterSyncMsgRate.setStatus("current")
_F3PtpSOOCMasterSyncReceiptTimeout_Type = Integer32
_F3PtpSOOCMasterSyncReceiptTimeout_Object = MibTableColumn
f3PtpSOOCMasterSyncReceiptTimeout = _F3PtpSOOCMasterSyncReceiptTimeout_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 1, 4, 1, 22),
    _F3PtpSOOCMasterSyncReceiptTimeout_Type()
)
f3PtpSOOCMasterSyncReceiptTimeout.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3PtpSOOCMasterSyncReceiptTimeout.setStatus("current")
_F3PtpSOOCMasterDelayRspMsgRate_Type = DelayRespMsgRate
_F3PtpSOOCMasterDelayRspMsgRate_Object = MibTableColumn
f3PtpSOOCMasterDelayRspMsgRate = _F3PtpSOOCMasterDelayRspMsgRate_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 1, 4, 1, 23),
    _F3PtpSOOCMasterDelayRspMsgRate_Type()
)
f3PtpSOOCMasterDelayRspMsgRate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3PtpSOOCMasterDelayRspMsgRate.setStatus("current")
_F3PtpSOOCMasterDelayRspReceiptTimeout_Type = Integer32
_F3PtpSOOCMasterDelayRspReceiptTimeout_Object = MibTableColumn
f3PtpSOOCMasterDelayRspReceiptTimeout = _F3PtpSOOCMasterDelayRspReceiptTimeout_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 1, 4, 1, 24),
    _F3PtpSOOCMasterDelayRspReceiptTimeout_Type()
)
f3PtpSOOCMasterDelayRspReceiptTimeout.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3PtpSOOCMasterDelayRspReceiptTimeout.setStatus("current")
_F3PtpSOOCMasterRequestUnicastTimeout_Type = Integer32
_F3PtpSOOCMasterRequestUnicastTimeout_Object = MibTableColumn
f3PtpSOOCMasterRequestUnicastTimeout = _F3PtpSOOCMasterRequestUnicastTimeout_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 1, 4, 1, 25),
    _F3PtpSOOCMasterRequestUnicastTimeout_Type()
)
f3PtpSOOCMasterRequestUnicastTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3PtpSOOCMasterRequestUnicastTimeout.setStatus("current")
_F3PtpSOOCMasterRequestUnicastRestartTimer_Type = Integer32
_F3PtpSOOCMasterRequestUnicastRestartTimer_Object = MibTableColumn
f3PtpSOOCMasterRequestUnicastRestartTimer = _F3PtpSOOCMasterRequestUnicastRestartTimer_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 1, 4, 1, 26),
    _F3PtpSOOCMasterRequestUnicastRestartTimer_Type()
)
f3PtpSOOCMasterRequestUnicastRestartTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3PtpSOOCMasterRequestUnicastRestartTimer.setStatus("current")
_F3PtpSOOCCurrentOffsetFromMaster_Type = ScaledNanoseconds
_F3PtpSOOCCurrentOffsetFromMaster_Object = MibTableColumn
f3PtpSOOCCurrentOffsetFromMaster = _F3PtpSOOCCurrentOffsetFromMaster_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 1, 4, 1, 27),
    _F3PtpSOOCCurrentOffsetFromMaster_Type()
)
f3PtpSOOCCurrentOffsetFromMaster.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpSOOCCurrentOffsetFromMaster.setStatus("current")
_F3PtpSOOCAnnounceMsgClockClass_Type = Integer32
_F3PtpSOOCAnnounceMsgClockClass_Object = MibTableColumn
f3PtpSOOCAnnounceMsgClockClass = _F3PtpSOOCAnnounceMsgClockClass_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 1, 4, 1, 28),
    _F3PtpSOOCAnnounceMsgClockClass_Type()
)
f3PtpSOOCAnnounceMsgClockClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpSOOCAnnounceMsgClockClass.setStatus("deprecated")


class _F3PtpSOOCLastReceivedAnnounceMsg_Type(OctetString):
    """Custom type f3PtpSOOCLastReceivedAnnounceMsg based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_F3PtpSOOCLastReceivedAnnounceMsg_Type.__name__ = "OctetString"
_F3PtpSOOCLastReceivedAnnounceMsg_Object = MibTableColumn
f3PtpSOOCLastReceivedAnnounceMsg = _F3PtpSOOCLastReceivedAnnounceMsg_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 1, 4, 1, 29),
    _F3PtpSOOCLastReceivedAnnounceMsg_Type()
)
f3PtpSOOCLastReceivedAnnounceMsg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpSOOCLastReceivedAnnounceMsg.setStatus("current")


class _F3PtpSOOCLastReceivedSyncMsg_Type(OctetString):
    """Custom type f3PtpSOOCLastReceivedSyncMsg based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_F3PtpSOOCLastReceivedSyncMsg_Type.__name__ = "OctetString"
_F3PtpSOOCLastReceivedSyncMsg_Object = MibTableColumn
f3PtpSOOCLastReceivedSyncMsg = _F3PtpSOOCLastReceivedSyncMsg_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 1, 4, 1, 30),
    _F3PtpSOOCLastReceivedSyncMsg_Type()
)
f3PtpSOOCLastReceivedSyncMsg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpSOOCLastReceivedSyncMsg.setStatus("current")


class _F3PtpSOOCLastReceivedDelayRspMsg_Type(OctetString):
    """Custom type f3PtpSOOCLastReceivedDelayRspMsg based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_F3PtpSOOCLastReceivedDelayRspMsg_Type.__name__ = "OctetString"
_F3PtpSOOCLastReceivedDelayRspMsg_Object = MibTableColumn
f3PtpSOOCLastReceivedDelayRspMsg = _F3PtpSOOCLastReceivedDelayRspMsg_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 1, 4, 1, 31),
    _F3PtpSOOCLastReceivedDelayRspMsg_Type()
)
f3PtpSOOCLastReceivedDelayRspMsg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpSOOCLastReceivedDelayRspMsg.setStatus("current")
_F3PtpSOOCRecentMeanPathDelay_Type = ScaledNanoseconds
_F3PtpSOOCRecentMeanPathDelay_Object = MibTableColumn
f3PtpSOOCRecentMeanPathDelay = _F3PtpSOOCRecentMeanPathDelay_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 1, 4, 1, 32),
    _F3PtpSOOCRecentMeanPathDelay_Type()
)
f3PtpSOOCRecentMeanPathDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpSOOCRecentMeanPathDelay.setStatus("current")
_F3PtpSOOCRecentSyncPDV_Type = ScaledNanoseconds
_F3PtpSOOCRecentSyncPDV_Object = MibTableColumn
f3PtpSOOCRecentSyncPDV = _F3PtpSOOCRecentSyncPDV_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 1, 4, 1, 33),
    _F3PtpSOOCRecentSyncPDV_Type()
)
f3PtpSOOCRecentSyncPDV.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpSOOCRecentSyncPDV.setStatus("current")
_F3PtpSOOCStorageType_Type = StorageType
_F3PtpSOOCStorageType_Object = MibTableColumn
f3PtpSOOCStorageType = _F3PtpSOOCStorageType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 1, 4, 1, 34),
    _F3PtpSOOCStorageType_Type()
)
f3PtpSOOCStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3PtpSOOCStorageType.setStatus("current")
_F3PtpSOOCRowStatus_Type = RowStatus
_F3PtpSOOCRowStatus_Object = MibTableColumn
f3PtpSOOCRowStatus = _F3PtpSOOCRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 1, 4, 1, 35),
    _F3PtpSOOCRowStatus_Type()
)
f3PtpSOOCRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3PtpSOOCRowStatus.setStatus("current")
_F3PtpSOOCRecentSyncPathDelay_Type = ScaledNanoseconds
_F3PtpSOOCRecentSyncPathDelay_Object = MibTableColumn
f3PtpSOOCRecentSyncPathDelay = _F3PtpSOOCRecentSyncPathDelay_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 1, 4, 1, 36),
    _F3PtpSOOCRecentSyncPathDelay_Type()
)
f3PtpSOOCRecentSyncPathDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpSOOCRecentSyncPathDelay.setStatus("current")
_F3PtpSOOCSoocProtectionState_Type = PTPProtectionState
_F3PtpSOOCSoocProtectionState_Object = MibTableColumn
f3PtpSOOCSoocProtectionState = _F3PtpSOOCSoocProtectionState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 1, 4, 1, 37),
    _F3PtpSOOCSoocProtectionState_Type()
)
f3PtpSOOCSoocProtectionState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpSOOCSoocProtectionState.setStatus("current")
_F3PtpSOOCSoocWtr_Type = TruthValue
_F3PtpSOOCSoocWtr_Object = MibTableColumn
f3PtpSOOCSoocWtr = _F3PtpSOOCSoocWtr_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 1, 4, 1, 38),
    _F3PtpSOOCSoocWtr_Type()
)
f3PtpSOOCSoocWtr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpSOOCSoocWtr.setStatus("current")
_F3PtpSOOCSoocClockClass_Type = Unsigned32
_F3PtpSOOCSoocClockClass_Object = MibTableColumn
f3PtpSOOCSoocClockClass = _F3PtpSOOCSoocClockClass_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 1, 4, 1, 39),
    _F3PtpSOOCSoocClockClass_Type()
)
f3PtpSOOCSoocClockClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpSOOCSoocClockClass.setStatus("current")
_F3PtpSOOCSoocClockRecoveryState_Type = ClockRecoveryState
_F3PtpSOOCSoocClockRecoveryState_Object = MibTableColumn
f3PtpSOOCSoocClockRecoveryState = _F3PtpSOOCSoocClockRecoveryState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 1, 4, 1, 40),
    _F3PtpSOOCSoocClockRecoveryState_Type()
)
f3PtpSOOCSoocClockRecoveryState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpSOOCSoocClockRecoveryState.setStatus("current")
_F3PtpSOOCSoocPhaseRecoveryState_Type = PhaseRecoveryState
_F3PtpSOOCSoocPhaseRecoveryState_Object = MibTableColumn
f3PtpSOOCSoocPhaseRecoveryState = _F3PtpSOOCSoocPhaseRecoveryState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 1, 4, 1, 41),
    _F3PtpSOOCSoocPhaseRecoveryState_Type()
)
f3PtpSOOCSoocPhaseRecoveryState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpSOOCSoocPhaseRecoveryState.setStatus("current")
_F3PtpSOOCE2eDelayAsymmetryComp_Type = CompensationMode
_F3PtpSOOCE2eDelayAsymmetryComp_Object = MibTableColumn
f3PtpSOOCE2eDelayAsymmetryComp = _F3PtpSOOCE2eDelayAsymmetryComp_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 1, 4, 1, 42),
    _F3PtpSOOCE2eDelayAsymmetryComp_Type()
)
f3PtpSOOCE2eDelayAsymmetryComp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3PtpSOOCE2eDelayAsymmetryComp.setStatus("current")
_F3PtpSOOCE2eAutoAsymmetryCompStatus_Type = CompensationStatus
_F3PtpSOOCE2eAutoAsymmetryCompStatus_Object = MibTableColumn
f3PtpSOOCE2eAutoAsymmetryCompStatus = _F3PtpSOOCE2eAutoAsymmetryCompStatus_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 1, 4, 1, 43),
    _F3PtpSOOCE2eAutoAsymmetryCompStatus_Type()
)
f3PtpSOOCE2eAutoAsymmetryCompStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpSOOCE2eAutoAsymmetryCompStatus.setStatus("current")
_F3PtpSOOCE2eDelayAsymmetry_Type = Integer32
_F3PtpSOOCE2eDelayAsymmetry_Object = MibTableColumn
f3PtpSOOCE2eDelayAsymmetry = _F3PtpSOOCE2eDelayAsymmetry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 1, 4, 1, 44),
    _F3PtpSOOCE2eDelayAsymmetry_Type()
)
f3PtpSOOCE2eDelayAsymmetry.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3PtpSOOCE2eDelayAsymmetry.setStatus("current")
_F3PtpSOOCSoocLockOutControl_Type = TruthValue
_F3PtpSOOCSoocLockOutControl_Object = MibTableColumn
f3PtpSOOCSoocLockOutControl = _F3PtpSOOCSoocLockOutControl_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 1, 4, 1, 45),
    _F3PtpSOOCSoocLockOutControl_Type()
)
f3PtpSOOCSoocLockOutControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3PtpSOOCSoocLockOutControl.setStatus("current")
_F3PtpSOOCSlaveIpV6Address_Type = Ipv6Address
_F3PtpSOOCSlaveIpV6Address_Object = MibTableColumn
f3PtpSOOCSlaveIpV6Address = _F3PtpSOOCSlaveIpV6Address_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 1, 4, 1, 46),
    _F3PtpSOOCSlaveIpV6Address_Type()
)
f3PtpSOOCSlaveIpV6Address.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3PtpSOOCSlaveIpV6Address.setStatus("current")


class _F3PtpSOOCSlaveIpV6AddrPrefixLength_Type(Integer32):
    """Custom type f3PtpSOOCSlaveIpV6AddrPrefixLength based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_F3PtpSOOCSlaveIpV6AddrPrefixLength_Type.__name__ = "Integer32"
_F3PtpSOOCSlaveIpV6AddrPrefixLength_Object = MibTableColumn
f3PtpSOOCSlaveIpV6AddrPrefixLength = _F3PtpSOOCSlaveIpV6AddrPrefixLength_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 1, 4, 1, 47),
    _F3PtpSOOCSlaveIpV6AddrPrefixLength_Type()
)
f3PtpSOOCSlaveIpV6AddrPrefixLength.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3PtpSOOCSlaveIpV6AddrPrefixLength.setStatus("current")
_F3PtpSOOCMasterIpV6Address_Type = Ipv6Address
_F3PtpSOOCMasterIpV6Address_Object = MibTableColumn
f3PtpSOOCMasterIpV6Address = _F3PtpSOOCMasterIpV6Address_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 1, 4, 1, 48),
    _F3PtpSOOCMasterIpV6Address_Type()
)
f3PtpSOOCMasterIpV6Address.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3PtpSOOCMasterIpV6Address.setStatus("current")


class _F3PtpSOOCMinimumExpectedClockClass_Type(Integer32):
    """Custom type f3PtpSOOCMinimumExpectedClockClass based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_F3PtpSOOCMinimumExpectedClockClass_Type.__name__ = "Integer32"
_F3PtpSOOCMinimumExpectedClockClass_Object = MibTableColumn
f3PtpSOOCMinimumExpectedClockClass = _F3PtpSOOCMinimumExpectedClockClass_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 1, 4, 1, 49),
    _F3PtpSOOCMinimumExpectedClockClass_Type()
)
f3PtpSOOCMinimumExpectedClockClass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3PtpSOOCMinimumExpectedClockClass.setStatus("current")
_F3PtpSOOCMasterMessageMode_Type = SlaveMode
_F3PtpSOOCMasterMessageMode_Object = MibTableColumn
f3PtpSOOCMasterMessageMode = _F3PtpSOOCMasterMessageMode_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 1, 4, 1, 50),
    _F3PtpSOOCMasterMessageMode_Type()
)
f3PtpSOOCMasterMessageMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3PtpSOOCMasterMessageMode.setStatus("current")
_F3PtpSOOCDefaultGatewayControl_Type = ToggleValue
_F3PtpSOOCDefaultGatewayControl_Object = MibTableColumn
f3PtpSOOCDefaultGatewayControl = _F3PtpSOOCDefaultGatewayControl_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 1, 4, 1, 51),
    _F3PtpSOOCDefaultGatewayControl_Type()
)
f3PtpSOOCDefaultGatewayControl.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3PtpSOOCDefaultGatewayControl.setStatus("current")
_F3PtpSOOCGateway_Type = IpAddress
_F3PtpSOOCGateway_Object = MibTableColumn
f3PtpSOOCGateway = _F3PtpSOOCGateway_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 1, 4, 1, 52),
    _F3PtpSOOCGateway_Type()
)
f3PtpSOOCGateway.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3PtpSOOCGateway.setStatus("current")
_F3PtpSOOCIpV6Gateway_Type = Ipv6Address
_F3PtpSOOCIpV6Gateway_Object = MibTableColumn
f3PtpSOOCIpV6Gateway = _F3PtpSOOCIpV6Gateway_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 1, 4, 1, 53),
    _F3PtpSOOCIpV6Gateway_Type()
)
f3PtpSOOCIpV6Gateway.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3PtpSOOCIpV6Gateway.setStatus("current")
_F3PtpSOOCAlgorithmPtpAware_Type = TruthValue
_F3PtpSOOCAlgorithmPtpAware_Object = MibTableColumn
f3PtpSOOCAlgorithmPtpAware = _F3PtpSOOCAlgorithmPtpAware_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 1, 4, 1, 54),
    _F3PtpSOOCAlgorithmPtpAware_Type()
)
f3PtpSOOCAlgorithmPtpAware.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3PtpSOOCAlgorithmPtpAware.setStatus("current")
_F3PtpOCSlaveVirtualPortTable_Object = MibTable
f3PtpOCSlaveVirtualPortTable = _F3PtpOCSlaveVirtualPortTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 1, 5)
)
if mibBuilder.loadTexts:
    f3PtpOCSlaveVirtualPortTable.setStatus("current")
_F3PtpOCSlaveVirtualPortEntry_Object = MibTableRow
f3PtpOCSlaveVirtualPortEntry = _F3PtpOCSlaveVirtualPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 1, 5, 1)
)
f3PtpOCSlaveVirtualPortEntry.setIndexNames(
    (0, "CM-ENTITY-MIB", "neIndex"),
    (0, "F3-PTP-MIB", "f3PtpTSIndex"),
    (0, "F3-PTP-MIB", "f3PtpSOOCIndex"),
    (0, "F3-PTP-MIB", "f3PtpOCSlaveVirtualPortIndex"),
)
if mibBuilder.loadTexts:
    f3PtpOCSlaveVirtualPortEntry.setStatus("current")
_F3PtpOCSlaveVirtualPortIndex_Type = Integer32
_F3PtpOCSlaveVirtualPortIndex_Object = MibTableColumn
f3PtpOCSlaveVirtualPortIndex = _F3PtpOCSlaveVirtualPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 1, 5, 1, 1),
    _F3PtpOCSlaveVirtualPortIndex_Type()
)
f3PtpOCSlaveVirtualPortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    f3PtpOCSlaveVirtualPortIndex.setStatus("current")


class _F3PtpOCSlaveVirtualPortAlias_Type(DisplayString):
    """Custom type f3PtpOCSlaveVirtualPortAlias based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_F3PtpOCSlaveVirtualPortAlias_Type.__name__ = "DisplayString"
_F3PtpOCSlaveVirtualPortAlias_Object = MibTableColumn
f3PtpOCSlaveVirtualPortAlias = _F3PtpOCSlaveVirtualPortAlias_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 1, 5, 1, 2),
    _F3PtpOCSlaveVirtualPortAlias_Type()
)
f3PtpOCSlaveVirtualPortAlias.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3PtpOCSlaveVirtualPortAlias.setStatus("current")
_F3PtpOCSlaveVirtualPortAdminState_Type = AdminState
_F3PtpOCSlaveVirtualPortAdminState_Object = MibTableColumn
f3PtpOCSlaveVirtualPortAdminState = _F3PtpOCSlaveVirtualPortAdminState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 1, 5, 1, 3),
    _F3PtpOCSlaveVirtualPortAdminState_Type()
)
f3PtpOCSlaveVirtualPortAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3PtpOCSlaveVirtualPortAdminState.setStatus("current")
_F3PtpOCSlaveVirtualPortOperationalState_Type = OperationalState
_F3PtpOCSlaveVirtualPortOperationalState_Object = MibTableColumn
f3PtpOCSlaveVirtualPortOperationalState = _F3PtpOCSlaveVirtualPortOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 1, 5, 1, 4),
    _F3PtpOCSlaveVirtualPortOperationalState_Type()
)
f3PtpOCSlaveVirtualPortOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpOCSlaveVirtualPortOperationalState.setStatus("current")
_F3PtpOCSlaveVirtualPortSecondaryState_Type = SecondaryState
_F3PtpOCSlaveVirtualPortSecondaryState_Object = MibTableColumn
f3PtpOCSlaveVirtualPortSecondaryState = _F3PtpOCSlaveVirtualPortSecondaryState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 1, 5, 1, 5),
    _F3PtpOCSlaveVirtualPortSecondaryState_Type()
)
f3PtpOCSlaveVirtualPortSecondaryState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpOCSlaveVirtualPortSecondaryState.setStatus("current")
_F3PtpOCSlaveVirtualPortIdentity_Type = PortIdentity
_F3PtpOCSlaveVirtualPortIdentity_Object = MibTableColumn
f3PtpOCSlaveVirtualPortIdentity = _F3PtpOCSlaveVirtualPortIdentity_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 1, 5, 1, 6),
    _F3PtpOCSlaveVirtualPortIdentity_Type()
)
f3PtpOCSlaveVirtualPortIdentity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3PtpOCSlaveVirtualPortIdentity.setStatus("current")
_F3PtpOCSlaveVirtualPortFlowPoint_Type = VariablePointer
_F3PtpOCSlaveVirtualPortFlowPoint_Object = MibTableColumn
f3PtpOCSlaveVirtualPortFlowPoint = _F3PtpOCSlaveVirtualPortFlowPoint_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 1, 5, 1, 7),
    _F3PtpOCSlaveVirtualPortFlowPoint_Type()
)
f3PtpOCSlaveVirtualPortFlowPoint.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3PtpOCSlaveVirtualPortFlowPoint.setStatus("current")
_F3PtpOCSlaveVirtualPortState_Type = PtpPortState
_F3PtpOCSlaveVirtualPortState_Object = MibTableColumn
f3PtpOCSlaveVirtualPortState = _F3PtpOCSlaveVirtualPortState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 1, 5, 1, 8),
    _F3PtpOCSlaveVirtualPortState_Type()
)
f3PtpOCSlaveVirtualPortState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpOCSlaveVirtualPortState.setStatus("current")
_F3PtpOCSlaveVirtualPortStorageType_Type = StorageType
_F3PtpOCSlaveVirtualPortStorageType_Object = MibTableColumn
f3PtpOCSlaveVirtualPortStorageType = _F3PtpOCSlaveVirtualPortStorageType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 1, 5, 1, 9),
    _F3PtpOCSlaveVirtualPortStorageType_Type()
)
f3PtpOCSlaveVirtualPortStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3PtpOCSlaveVirtualPortStorageType.setStatus("current")
_F3PtpOCSlaveVirtualPortRowStatus_Type = RowStatus
_F3PtpOCSlaveVirtualPortRowStatus_Object = MibTableColumn
f3PtpOCSlaveVirtualPortRowStatus = _F3PtpOCSlaveVirtualPortRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 1, 5, 1, 10),
    _F3PtpOCSlaveVirtualPortRowStatus_Type()
)
f3PtpOCSlaveVirtualPortRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3PtpOCSlaveVirtualPortRowStatus.setStatus("current")
_F3PtpAccPortFlowPointTable_Object = MibTable
f3PtpAccPortFlowPointTable = _F3PtpAccPortFlowPointTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 1, 6)
)
if mibBuilder.loadTexts:
    f3PtpAccPortFlowPointTable.setStatus("current")
_F3PtpAccPortFlowPointEntry_Object = MibTableRow
f3PtpAccPortFlowPointEntry = _F3PtpAccPortFlowPointEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 1, 6, 1)
)
f3PtpAccPortFlowPointEntry.setIndexNames(
    (0, "CM-ENTITY-MIB", "neIndex"),
    (0, "CM-ENTITY-MIB", "shelfIndex"),
    (0, "CM-ENTITY-MIB", "slotIndex"),
    (0, "CM-FACILITY-MIB", "cmEthernetAccPortIndex"),
    (0, "F3-PTP-MIB", "f3PtpAccPortFlowPointIndex"),
)
if mibBuilder.loadTexts:
    f3PtpAccPortFlowPointEntry.setStatus("current")
_F3PtpAccPortFlowPointIndex_Type = Integer32
_F3PtpAccPortFlowPointIndex_Object = MibTableColumn
f3PtpAccPortFlowPointIndex = _F3PtpAccPortFlowPointIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 1, 6, 1, 1),
    _F3PtpAccPortFlowPointIndex_Type()
)
f3PtpAccPortFlowPointIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    f3PtpAccPortFlowPointIndex.setStatus("current")


class _F3PtpAccPortFlowPointAlias_Type(DisplayString):
    """Custom type f3PtpAccPortFlowPointAlias based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_F3PtpAccPortFlowPointAlias_Type.__name__ = "DisplayString"
_F3PtpAccPortFlowPointAlias_Object = MibTableColumn
f3PtpAccPortFlowPointAlias = _F3PtpAccPortFlowPointAlias_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 1, 6, 1, 2),
    _F3PtpAccPortFlowPointAlias_Type()
)
f3PtpAccPortFlowPointAlias.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3PtpAccPortFlowPointAlias.setStatus("current")
_F3PtpAccPortFlowPointAdminState_Type = AdminState
_F3PtpAccPortFlowPointAdminState_Object = MibTableColumn
f3PtpAccPortFlowPointAdminState = _F3PtpAccPortFlowPointAdminState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 1, 6, 1, 3),
    _F3PtpAccPortFlowPointAdminState_Type()
)
f3PtpAccPortFlowPointAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3PtpAccPortFlowPointAdminState.setStatus("current")
_F3PtpAccPortFlowPointOperationalState_Type = OperationalState
_F3PtpAccPortFlowPointOperationalState_Object = MibTableColumn
f3PtpAccPortFlowPointOperationalState = _F3PtpAccPortFlowPointOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 1, 6, 1, 4),
    _F3PtpAccPortFlowPointOperationalState_Type()
)
f3PtpAccPortFlowPointOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpAccPortFlowPointOperationalState.setStatus("current")
_F3PtpAccPortFlowPointSecondaryState_Type = SecondaryState
_F3PtpAccPortFlowPointSecondaryState_Object = MibTableColumn
f3PtpAccPortFlowPointSecondaryState = _F3PtpAccPortFlowPointSecondaryState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 1, 6, 1, 5),
    _F3PtpAccPortFlowPointSecondaryState_Type()
)
f3PtpAccPortFlowPointSecondaryState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpAccPortFlowPointSecondaryState.setStatus("current")
_F3PtpAccPortFlowPointType_Type = PtpFlowPointType
_F3PtpAccPortFlowPointType_Object = MibTableColumn
f3PtpAccPortFlowPointType = _F3PtpAccPortFlowPointType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 1, 6, 1, 6),
    _F3PtpAccPortFlowPointType_Type()
)
f3PtpAccPortFlowPointType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3PtpAccPortFlowPointType.setStatus("current")
_F3PtpAccPortFlowPointClock_Type = VariablePointer
_F3PtpAccPortFlowPointClock_Object = MibTableColumn
f3PtpAccPortFlowPointClock = _F3PtpAccPortFlowPointClock_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 1, 6, 1, 7),
    _F3PtpAccPortFlowPointClock_Type()
)
f3PtpAccPortFlowPointClock.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpAccPortFlowPointClock.setStatus("current")
_F3PtpAccPortFlowPointService_Type = VariablePointer
_F3PtpAccPortFlowPointService_Object = MibTableColumn
f3PtpAccPortFlowPointService = _F3PtpAccPortFlowPointService_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 1, 6, 1, 8),
    _F3PtpAccPortFlowPointService_Type()
)
f3PtpAccPortFlowPointService.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3PtpAccPortFlowPointService.setStatus("current")
_F3PtpAccPortFlowPointOuterVlanEtherType_Type = Integer32
_F3PtpAccPortFlowPointOuterVlanEtherType_Object = MibTableColumn
f3PtpAccPortFlowPointOuterVlanEtherType = _F3PtpAccPortFlowPointOuterVlanEtherType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 1, 6, 1, 9),
    _F3PtpAccPortFlowPointOuterVlanEtherType_Type()
)
f3PtpAccPortFlowPointOuterVlanEtherType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3PtpAccPortFlowPointOuterVlanEtherType.setStatus("current")
_F3PtpAccPortFlowPointOuterVlanMemberList_Type = DisplayString
_F3PtpAccPortFlowPointOuterVlanMemberList_Object = MibTableColumn
f3PtpAccPortFlowPointOuterVlanMemberList = _F3PtpAccPortFlowPointOuterVlanMemberList_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 1, 6, 1, 10),
    _F3PtpAccPortFlowPointOuterVlanMemberList_Type()
)
f3PtpAccPortFlowPointOuterVlanMemberList.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3PtpAccPortFlowPointOuterVlanMemberList.setStatus("current")
_F3PtpAccPortFlowPointOuterUntaggedEnabled_Type = TruthValue
_F3PtpAccPortFlowPointOuterUntaggedEnabled_Object = MibTableColumn
f3PtpAccPortFlowPointOuterUntaggedEnabled = _F3PtpAccPortFlowPointOuterUntaggedEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 1, 6, 1, 11),
    _F3PtpAccPortFlowPointOuterUntaggedEnabled_Type()
)
f3PtpAccPortFlowPointOuterUntaggedEnabled.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3PtpAccPortFlowPointOuterUntaggedEnabled.setStatus("current")
_F3PtpAccPortFlowPointInner1VlanEtherType_Type = Integer32
_F3PtpAccPortFlowPointInner1VlanEtherType_Object = MibTableColumn
f3PtpAccPortFlowPointInner1VlanEtherType = _F3PtpAccPortFlowPointInner1VlanEtherType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 1, 6, 1, 12),
    _F3PtpAccPortFlowPointInner1VlanEtherType_Type()
)
f3PtpAccPortFlowPointInner1VlanEtherType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3PtpAccPortFlowPointInner1VlanEtherType.setStatus("current")
_F3PtpAccPortFlowPointInner1VlanMemberList_Type = DisplayString
_F3PtpAccPortFlowPointInner1VlanMemberList_Object = MibTableColumn
f3PtpAccPortFlowPointInner1VlanMemberList = _F3PtpAccPortFlowPointInner1VlanMemberList_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 1, 6, 1, 13),
    _F3PtpAccPortFlowPointInner1VlanMemberList_Type()
)
f3PtpAccPortFlowPointInner1VlanMemberList.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3PtpAccPortFlowPointInner1VlanMemberList.setStatus("current")
_F3PtpAccPortFlowPointInner1UntaggedEnabled_Type = TruthValue
_F3PtpAccPortFlowPointInner1UntaggedEnabled_Object = MibTableColumn
f3PtpAccPortFlowPointInner1UntaggedEnabled = _F3PtpAccPortFlowPointInner1UntaggedEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 1, 6, 1, 14),
    _F3PtpAccPortFlowPointInner1UntaggedEnabled_Type()
)
f3PtpAccPortFlowPointInner1UntaggedEnabled.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3PtpAccPortFlowPointInner1UntaggedEnabled.setStatus("current")
_F3PtpAccPortFlowPointInner2VlanEtherType_Type = Integer32
_F3PtpAccPortFlowPointInner2VlanEtherType_Object = MibTableColumn
f3PtpAccPortFlowPointInner2VlanEtherType = _F3PtpAccPortFlowPointInner2VlanEtherType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 1, 6, 1, 15),
    _F3PtpAccPortFlowPointInner2VlanEtherType_Type()
)
f3PtpAccPortFlowPointInner2VlanEtherType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3PtpAccPortFlowPointInner2VlanEtherType.setStatus("current")
_F3PtpAccPortFlowPointInner2VlanMemberList_Type = DisplayString
_F3PtpAccPortFlowPointInner2VlanMemberList_Object = MibTableColumn
f3PtpAccPortFlowPointInner2VlanMemberList = _F3PtpAccPortFlowPointInner2VlanMemberList_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 1, 6, 1, 16),
    _F3PtpAccPortFlowPointInner2VlanMemberList_Type()
)
f3PtpAccPortFlowPointInner2VlanMemberList.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3PtpAccPortFlowPointInner2VlanMemberList.setStatus("current")
_F3PtpAccPortFlowPointInner2UntaggedEnabled_Type = TruthValue
_F3PtpAccPortFlowPointInner2UntaggedEnabled_Object = MibTableColumn
f3PtpAccPortFlowPointInner2UntaggedEnabled = _F3PtpAccPortFlowPointInner2UntaggedEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 1, 6, 1, 17),
    _F3PtpAccPortFlowPointInner2UntaggedEnabled_Type()
)
f3PtpAccPortFlowPointInner2UntaggedEnabled.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3PtpAccPortFlowPointInner2UntaggedEnabled.setStatus("current")
_F3PtpAccPortFlowPointStorageType_Type = StorageType
_F3PtpAccPortFlowPointStorageType_Object = MibTableColumn
f3PtpAccPortFlowPointStorageType = _F3PtpAccPortFlowPointStorageType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 1, 6, 1, 18),
    _F3PtpAccPortFlowPointStorageType_Type()
)
f3PtpAccPortFlowPointStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3PtpAccPortFlowPointStorageType.setStatus("current")
_F3PtpAccPortFlowPointRowStatus_Type = RowStatus
_F3PtpAccPortFlowPointRowStatus_Object = MibTableColumn
f3PtpAccPortFlowPointRowStatus = _F3PtpAccPortFlowPointRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 1, 6, 1, 19),
    _F3PtpAccPortFlowPointRowStatus_Type()
)
f3PtpAccPortFlowPointRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3PtpAccPortFlowPointRowStatus.setStatus("current")


class _F3PtpAccPortFlowPointCOS_Type(Integer32):
    """Custom type f3PtpAccPortFlowPointCOS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_F3PtpAccPortFlowPointCOS_Type.__name__ = "Integer32"
_F3PtpAccPortFlowPointCOS_Object = MibTableColumn
f3PtpAccPortFlowPointCOS = _F3PtpAccPortFlowPointCOS_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 1, 6, 1, 20),
    _F3PtpAccPortFlowPointCOS_Type()
)
f3PtpAccPortFlowPointCOS.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3PtpAccPortFlowPointCOS.setStatus("current")
_F3PtpAccPortFlowPointCIRLo_Type = Unsigned32
_F3PtpAccPortFlowPointCIRLo_Object = MibTableColumn
f3PtpAccPortFlowPointCIRLo = _F3PtpAccPortFlowPointCIRLo_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 1, 6, 1, 21),
    _F3PtpAccPortFlowPointCIRLo_Type()
)
f3PtpAccPortFlowPointCIRLo.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3PtpAccPortFlowPointCIRLo.setStatus("current")
_F3PtpAccPortFlowPointCIRHi_Type = Unsigned32
_F3PtpAccPortFlowPointCIRHi_Object = MibTableColumn
f3PtpAccPortFlowPointCIRHi = _F3PtpAccPortFlowPointCIRHi_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 1, 6, 1, 22),
    _F3PtpAccPortFlowPointCIRHi_Type()
)
f3PtpAccPortFlowPointCIRHi.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3PtpAccPortFlowPointCIRHi.setStatus("current")
_F3PtpAccPortFlowPointEIRLo_Type = Unsigned32
_F3PtpAccPortFlowPointEIRLo_Object = MibTableColumn
f3PtpAccPortFlowPointEIRLo = _F3PtpAccPortFlowPointEIRLo_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 1, 6, 1, 23),
    _F3PtpAccPortFlowPointEIRLo_Type()
)
f3PtpAccPortFlowPointEIRLo.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3PtpAccPortFlowPointEIRLo.setStatus("current")
_F3PtpAccPortFlowPointEIRHi_Type = Unsigned32
_F3PtpAccPortFlowPointEIRHi_Object = MibTableColumn
f3PtpAccPortFlowPointEIRHi = _F3PtpAccPortFlowPointEIRHi_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 1, 6, 1, 24),
    _F3PtpAccPortFlowPointEIRHi_Type()
)
f3PtpAccPortFlowPointEIRHi.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3PtpAccPortFlowPointEIRHi.setStatus("current")
_F3PtpAccPortFlowPointBufferSize_Type = Unsigned32
_F3PtpAccPortFlowPointBufferSize_Object = MibTableColumn
f3PtpAccPortFlowPointBufferSize = _F3PtpAccPortFlowPointBufferSize_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 1, 6, 1, 25),
    _F3PtpAccPortFlowPointBufferSize_Type()
)
f3PtpAccPortFlowPointBufferSize.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3PtpAccPortFlowPointBufferSize.setStatus("current")
_F3PtpAccPortFlowPointLoopAvoidance_Type = VariablePointer
_F3PtpAccPortFlowPointLoopAvoidance_Object = MibTableColumn
f3PtpAccPortFlowPointLoopAvoidance = _F3PtpAccPortFlowPointLoopAvoidance_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 1, 6, 1, 26),
    _F3PtpAccPortFlowPointLoopAvoidance_Type()
)
f3PtpAccPortFlowPointLoopAvoidance.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3PtpAccPortFlowPointLoopAvoidance.setStatus("current")
_F3PtpAccPortFlowPointRefConnectGuardFlow_Type = VariablePointer
_F3PtpAccPortFlowPointRefConnectGuardFlow_Object = MibTableColumn
f3PtpAccPortFlowPointRefConnectGuardFlow = _F3PtpAccPortFlowPointRefConnectGuardFlow_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 1, 6, 1, 27),
    _F3PtpAccPortFlowPointRefConnectGuardFlow_Type()
)
f3PtpAccPortFlowPointRefConnectGuardFlow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3PtpAccPortFlowPointRefConnectGuardFlow.setStatus("current")
_F3PtpAccPortFlowPointSecureState_Type = FlowSecState
_F3PtpAccPortFlowPointSecureState_Object = MibTableColumn
f3PtpAccPortFlowPointSecureState = _F3PtpAccPortFlowPointSecureState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 1, 6, 1, 28),
    _F3PtpAccPortFlowPointSecureState_Type()
)
f3PtpAccPortFlowPointSecureState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpAccPortFlowPointSecureState.setStatus("current")
_F3PtpAccPortFlowPointSecureBlockingEnabled_Type = TruthValue
_F3PtpAccPortFlowPointSecureBlockingEnabled_Object = MibTableColumn
f3PtpAccPortFlowPointSecureBlockingEnabled = _F3PtpAccPortFlowPointSecureBlockingEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 1, 6, 1, 29),
    _F3PtpAccPortFlowPointSecureBlockingEnabled_Type()
)
f3PtpAccPortFlowPointSecureBlockingEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3PtpAccPortFlowPointSecureBlockingEnabled.setStatus("current")
_F3PtpNetPortFlowPointTable_Object = MibTable
f3PtpNetPortFlowPointTable = _F3PtpNetPortFlowPointTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 1, 7)
)
if mibBuilder.loadTexts:
    f3PtpNetPortFlowPointTable.setStatus("current")
_F3PtpNetPortFlowPointEntry_Object = MibTableRow
f3PtpNetPortFlowPointEntry = _F3PtpNetPortFlowPointEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 1, 7, 1)
)
f3PtpNetPortFlowPointEntry.setIndexNames(
    (0, "CM-ENTITY-MIB", "neIndex"),
    (0, "CM-ENTITY-MIB", "shelfIndex"),
    (0, "CM-ENTITY-MIB", "slotIndex"),
    (0, "CM-FACILITY-MIB", "cmEthernetNetPortIndex"),
    (0, "F3-PTP-MIB", "f3PtpNetPortFlowPointIndex"),
)
if mibBuilder.loadTexts:
    f3PtpNetPortFlowPointEntry.setStatus("current")
_F3PtpNetPortFlowPointIndex_Type = Integer32
_F3PtpNetPortFlowPointIndex_Object = MibTableColumn
f3PtpNetPortFlowPointIndex = _F3PtpNetPortFlowPointIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 1, 7, 1, 1),
    _F3PtpNetPortFlowPointIndex_Type()
)
f3PtpNetPortFlowPointIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    f3PtpNetPortFlowPointIndex.setStatus("current")


class _F3PtpNetPortFlowPointAlias_Type(DisplayString):
    """Custom type f3PtpNetPortFlowPointAlias based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_F3PtpNetPortFlowPointAlias_Type.__name__ = "DisplayString"
_F3PtpNetPortFlowPointAlias_Object = MibTableColumn
f3PtpNetPortFlowPointAlias = _F3PtpNetPortFlowPointAlias_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 1, 7, 1, 2),
    _F3PtpNetPortFlowPointAlias_Type()
)
f3PtpNetPortFlowPointAlias.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3PtpNetPortFlowPointAlias.setStatus("current")
_F3PtpNetPortFlowPointAdminState_Type = AdminState
_F3PtpNetPortFlowPointAdminState_Object = MibTableColumn
f3PtpNetPortFlowPointAdminState = _F3PtpNetPortFlowPointAdminState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 1, 7, 1, 3),
    _F3PtpNetPortFlowPointAdminState_Type()
)
f3PtpNetPortFlowPointAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3PtpNetPortFlowPointAdminState.setStatus("current")
_F3PtpNetPortFlowPointOperationalState_Type = OperationalState
_F3PtpNetPortFlowPointOperationalState_Object = MibTableColumn
f3PtpNetPortFlowPointOperationalState = _F3PtpNetPortFlowPointOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 1, 7, 1, 4),
    _F3PtpNetPortFlowPointOperationalState_Type()
)
f3PtpNetPortFlowPointOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpNetPortFlowPointOperationalState.setStatus("current")
_F3PtpNetPortFlowPointSecondaryState_Type = SecondaryState
_F3PtpNetPortFlowPointSecondaryState_Object = MibTableColumn
f3PtpNetPortFlowPointSecondaryState = _F3PtpNetPortFlowPointSecondaryState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 1, 7, 1, 5),
    _F3PtpNetPortFlowPointSecondaryState_Type()
)
f3PtpNetPortFlowPointSecondaryState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpNetPortFlowPointSecondaryState.setStatus("current")
_F3PtpNetPortFlowPointType_Type = PtpFlowPointType
_F3PtpNetPortFlowPointType_Object = MibTableColumn
f3PtpNetPortFlowPointType = _F3PtpNetPortFlowPointType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 1, 7, 1, 6),
    _F3PtpNetPortFlowPointType_Type()
)
f3PtpNetPortFlowPointType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3PtpNetPortFlowPointType.setStatus("current")
_F3PtpNetPortFlowPointClock_Type = VariablePointer
_F3PtpNetPortFlowPointClock_Object = MibTableColumn
f3PtpNetPortFlowPointClock = _F3PtpNetPortFlowPointClock_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 1, 7, 1, 7),
    _F3PtpNetPortFlowPointClock_Type()
)
f3PtpNetPortFlowPointClock.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpNetPortFlowPointClock.setStatus("current")
_F3PtpNetPortFlowPointService_Type = VariablePointer
_F3PtpNetPortFlowPointService_Object = MibTableColumn
f3PtpNetPortFlowPointService = _F3PtpNetPortFlowPointService_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 1, 7, 1, 8),
    _F3PtpNetPortFlowPointService_Type()
)
f3PtpNetPortFlowPointService.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3PtpNetPortFlowPointService.setStatus("current")
_F3PtpNetPortFlowPointOuterVlanEtherType_Type = Integer32
_F3PtpNetPortFlowPointOuterVlanEtherType_Object = MibTableColumn
f3PtpNetPortFlowPointOuterVlanEtherType = _F3PtpNetPortFlowPointOuterVlanEtherType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 1, 7, 1, 9),
    _F3PtpNetPortFlowPointOuterVlanEtherType_Type()
)
f3PtpNetPortFlowPointOuterVlanEtherType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3PtpNetPortFlowPointOuterVlanEtherType.setStatus("current")
_F3PtpNetPortFlowPointOuterVlanMemberList_Type = DisplayString
_F3PtpNetPortFlowPointOuterVlanMemberList_Object = MibTableColumn
f3PtpNetPortFlowPointOuterVlanMemberList = _F3PtpNetPortFlowPointOuterVlanMemberList_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 1, 7, 1, 10),
    _F3PtpNetPortFlowPointOuterVlanMemberList_Type()
)
f3PtpNetPortFlowPointOuterVlanMemberList.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3PtpNetPortFlowPointOuterVlanMemberList.setStatus("current")
_F3PtpNetPortFlowPointOuterUntaggedEnabled_Type = TruthValue
_F3PtpNetPortFlowPointOuterUntaggedEnabled_Object = MibTableColumn
f3PtpNetPortFlowPointOuterUntaggedEnabled = _F3PtpNetPortFlowPointOuterUntaggedEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 1, 7, 1, 11),
    _F3PtpNetPortFlowPointOuterUntaggedEnabled_Type()
)
f3PtpNetPortFlowPointOuterUntaggedEnabled.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3PtpNetPortFlowPointOuterUntaggedEnabled.setStatus("current")
_F3PtpNetPortFlowPointInner1VlanEtherType_Type = Integer32
_F3PtpNetPortFlowPointInner1VlanEtherType_Object = MibTableColumn
f3PtpNetPortFlowPointInner1VlanEtherType = _F3PtpNetPortFlowPointInner1VlanEtherType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 1, 7, 1, 12),
    _F3PtpNetPortFlowPointInner1VlanEtherType_Type()
)
f3PtpNetPortFlowPointInner1VlanEtherType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3PtpNetPortFlowPointInner1VlanEtherType.setStatus("current")
_F3PtpNetPortFlowPointInner1VlanMemberList_Type = DisplayString
_F3PtpNetPortFlowPointInner1VlanMemberList_Object = MibTableColumn
f3PtpNetPortFlowPointInner1VlanMemberList = _F3PtpNetPortFlowPointInner1VlanMemberList_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 1, 7, 1, 13),
    _F3PtpNetPortFlowPointInner1VlanMemberList_Type()
)
f3PtpNetPortFlowPointInner1VlanMemberList.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3PtpNetPortFlowPointInner1VlanMemberList.setStatus("current")
_F3PtpNetPortFlowPointInner1UntaggedEnabled_Type = TruthValue
_F3PtpNetPortFlowPointInner1UntaggedEnabled_Object = MibTableColumn
f3PtpNetPortFlowPointInner1UntaggedEnabled = _F3PtpNetPortFlowPointInner1UntaggedEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 1, 7, 1, 14),
    _F3PtpNetPortFlowPointInner1UntaggedEnabled_Type()
)
f3PtpNetPortFlowPointInner1UntaggedEnabled.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3PtpNetPortFlowPointInner1UntaggedEnabled.setStatus("current")
_F3PtpNetPortFlowPointInner2VlanEtherType_Type = Integer32
_F3PtpNetPortFlowPointInner2VlanEtherType_Object = MibTableColumn
f3PtpNetPortFlowPointInner2VlanEtherType = _F3PtpNetPortFlowPointInner2VlanEtherType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 1, 7, 1, 15),
    _F3PtpNetPortFlowPointInner2VlanEtherType_Type()
)
f3PtpNetPortFlowPointInner2VlanEtherType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3PtpNetPortFlowPointInner2VlanEtherType.setStatus("current")
_F3PtpNetPortFlowPointInner2VlanMemberList_Type = DisplayString
_F3PtpNetPortFlowPointInner2VlanMemberList_Object = MibTableColumn
f3PtpNetPortFlowPointInner2VlanMemberList = _F3PtpNetPortFlowPointInner2VlanMemberList_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 1, 7, 1, 16),
    _F3PtpNetPortFlowPointInner2VlanMemberList_Type()
)
f3PtpNetPortFlowPointInner2VlanMemberList.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3PtpNetPortFlowPointInner2VlanMemberList.setStatus("current")
_F3PtpNetPortFlowPointInner2UntaggedEnabled_Type = TruthValue
_F3PtpNetPortFlowPointInner2UntaggedEnabled_Object = MibTableColumn
f3PtpNetPortFlowPointInner2UntaggedEnabled = _F3PtpNetPortFlowPointInner2UntaggedEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 1, 7, 1, 17),
    _F3PtpNetPortFlowPointInner2UntaggedEnabled_Type()
)
f3PtpNetPortFlowPointInner2UntaggedEnabled.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3PtpNetPortFlowPointInner2UntaggedEnabled.setStatus("current")
_F3PtpNetPortFlowPointStorageType_Type = StorageType
_F3PtpNetPortFlowPointStorageType_Object = MibTableColumn
f3PtpNetPortFlowPointStorageType = _F3PtpNetPortFlowPointStorageType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 1, 7, 1, 18),
    _F3PtpNetPortFlowPointStorageType_Type()
)
f3PtpNetPortFlowPointStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3PtpNetPortFlowPointStorageType.setStatus("current")
_F3PtpNetPortFlowPointRowStatus_Type = RowStatus
_F3PtpNetPortFlowPointRowStatus_Object = MibTableColumn
f3PtpNetPortFlowPointRowStatus = _F3PtpNetPortFlowPointRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 1, 7, 1, 19),
    _F3PtpNetPortFlowPointRowStatus_Type()
)
f3PtpNetPortFlowPointRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3PtpNetPortFlowPointRowStatus.setStatus("current")


class _F3PtpNetPortFlowPointCOS_Type(Integer32):
    """Custom type f3PtpNetPortFlowPointCOS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_F3PtpNetPortFlowPointCOS_Type.__name__ = "Integer32"
_F3PtpNetPortFlowPointCOS_Object = MibTableColumn
f3PtpNetPortFlowPointCOS = _F3PtpNetPortFlowPointCOS_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 1, 7, 1, 20),
    _F3PtpNetPortFlowPointCOS_Type()
)
f3PtpNetPortFlowPointCOS.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3PtpNetPortFlowPointCOS.setStatus("current")
_F3PtpNetPortFlowPointCIRLo_Type = Unsigned32
_F3PtpNetPortFlowPointCIRLo_Object = MibTableColumn
f3PtpNetPortFlowPointCIRLo = _F3PtpNetPortFlowPointCIRLo_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 1, 7, 1, 21),
    _F3PtpNetPortFlowPointCIRLo_Type()
)
f3PtpNetPortFlowPointCIRLo.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3PtpNetPortFlowPointCIRLo.setStatus("current")
_F3PtpNetPortFlowPointCIRHi_Type = Unsigned32
_F3PtpNetPortFlowPointCIRHi_Object = MibTableColumn
f3PtpNetPortFlowPointCIRHi = _F3PtpNetPortFlowPointCIRHi_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 1, 7, 1, 22),
    _F3PtpNetPortFlowPointCIRHi_Type()
)
f3PtpNetPortFlowPointCIRHi.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3PtpNetPortFlowPointCIRHi.setStatus("current")
_F3PtpNetPortFlowPointEIRLo_Type = Unsigned32
_F3PtpNetPortFlowPointEIRLo_Object = MibTableColumn
f3PtpNetPortFlowPointEIRLo = _F3PtpNetPortFlowPointEIRLo_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 1, 7, 1, 23),
    _F3PtpNetPortFlowPointEIRLo_Type()
)
f3PtpNetPortFlowPointEIRLo.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3PtpNetPortFlowPointEIRLo.setStatus("current")
_F3PtpNetPortFlowPointEIRHi_Type = Unsigned32
_F3PtpNetPortFlowPointEIRHi_Object = MibTableColumn
f3PtpNetPortFlowPointEIRHi = _F3PtpNetPortFlowPointEIRHi_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 1, 7, 1, 24),
    _F3PtpNetPortFlowPointEIRHi_Type()
)
f3PtpNetPortFlowPointEIRHi.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3PtpNetPortFlowPointEIRHi.setStatus("current")
_F3PtpNetPortFlowPointBufferSize_Type = Unsigned32
_F3PtpNetPortFlowPointBufferSize_Object = MibTableColumn
f3PtpNetPortFlowPointBufferSize = _F3PtpNetPortFlowPointBufferSize_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 1, 7, 1, 25),
    _F3PtpNetPortFlowPointBufferSize_Type()
)
f3PtpNetPortFlowPointBufferSize.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3PtpNetPortFlowPointBufferSize.setStatus("current")
_F3PtpNetPortFlowPointLoopAvoidance_Type = VariablePointer
_F3PtpNetPortFlowPointLoopAvoidance_Object = MibTableColumn
f3PtpNetPortFlowPointLoopAvoidance = _F3PtpNetPortFlowPointLoopAvoidance_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 1, 7, 1, 26),
    _F3PtpNetPortFlowPointLoopAvoidance_Type()
)
f3PtpNetPortFlowPointLoopAvoidance.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3PtpNetPortFlowPointLoopAvoidance.setStatus("current")
_F3PtpNetPortFlowPointRefConnectGuardFlow_Type = VariablePointer
_F3PtpNetPortFlowPointRefConnectGuardFlow_Object = MibTableColumn
f3PtpNetPortFlowPointRefConnectGuardFlow = _F3PtpNetPortFlowPointRefConnectGuardFlow_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 1, 7, 1, 27),
    _F3PtpNetPortFlowPointRefConnectGuardFlow_Type()
)
f3PtpNetPortFlowPointRefConnectGuardFlow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3PtpNetPortFlowPointRefConnectGuardFlow.setStatus("current")
_F3PtpNetPortFlowPointSecureState_Type = FlowSecState
_F3PtpNetPortFlowPointSecureState_Object = MibTableColumn
f3PtpNetPortFlowPointSecureState = _F3PtpNetPortFlowPointSecureState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 1, 7, 1, 28),
    _F3PtpNetPortFlowPointSecureState_Type()
)
f3PtpNetPortFlowPointSecureState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpNetPortFlowPointSecureState.setStatus("current")
_F3PtpNetPortFlowPointSecureBlockingEnabled_Type = TruthValue
_F3PtpNetPortFlowPointSecureBlockingEnabled_Object = MibTableColumn
f3PtpNetPortFlowPointSecureBlockingEnabled = _F3PtpNetPortFlowPointSecureBlockingEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 1, 7, 1, 29),
    _F3PtpNetPortFlowPointSecureBlockingEnabled_Type()
)
f3PtpNetPortFlowPointSecureBlockingEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3PtpNetPortFlowPointSecureBlockingEnabled.setStatus("current")
_F3PtpEthernetAccPortExtTable_Object = MibTable
f3PtpEthernetAccPortExtTable = _F3PtpEthernetAccPortExtTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 1, 8)
)
if mibBuilder.loadTexts:
    f3PtpEthernetAccPortExtTable.setStatus("current")
_F3PtpEthernetAccPortExtEntry_Object = MibTableRow
f3PtpEthernetAccPortExtEntry = _F3PtpEthernetAccPortExtEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 1, 8, 1)
)
if mibBuilder.loadTexts:
    f3PtpEthernetAccPortExtEntry.setStatus("current")
_F3PtpEthernetAccPortDelayAsymmetry_Type = Integer32
_F3PtpEthernetAccPortDelayAsymmetry_Object = MibTableColumn
f3PtpEthernetAccPortDelayAsymmetry = _F3PtpEthernetAccPortDelayAsymmetry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 1, 8, 1, 1),
    _F3PtpEthernetAccPortDelayAsymmetry_Type()
)
f3PtpEthernetAccPortDelayAsymmetry.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3PtpEthernetAccPortDelayAsymmetry.setStatus("current")
_F3PtpEthernetNetPortExtTable_Object = MibTable
f3PtpEthernetNetPortExtTable = _F3PtpEthernetNetPortExtTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 1, 9)
)
if mibBuilder.loadTexts:
    f3PtpEthernetNetPortExtTable.setStatus("current")
_F3PtpEthernetNetPortExtEntry_Object = MibTableRow
f3PtpEthernetNetPortExtEntry = _F3PtpEthernetNetPortExtEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 1, 9, 1)
)
if mibBuilder.loadTexts:
    f3PtpEthernetNetPortExtEntry.setStatus("current")
_F3PtpEthernetNetPortDelayAsymmetry_Type = Integer32
_F3PtpEthernetNetPortDelayAsymmetry_Object = MibTableColumn
f3PtpEthernetNetPortDelayAsymmetry = _F3PtpEthernetNetPortDelayAsymmetry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 1, 9, 1, 1),
    _F3PtpEthernetNetPortDelayAsymmetry_Type()
)
f3PtpEthernetNetPortDelayAsymmetry.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3PtpEthernetNetPortDelayAsymmetry.setStatus("current")
_F3PtpConfigScalars_ObjectIdentity = ObjectIdentity
f3PtpConfigScalars = _F3PtpConfigScalars_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 1, 10)
)
_F3PtpSysTimeOfDayClock_Type = VariablePointer
_F3PtpSysTimeOfDayClock_Object = MibScalar
f3PtpSysTimeOfDayClock = _F3PtpSysTimeOfDayClock_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 1, 10, 1),
    _F3PtpSysTimeOfDayClock_Type()
)
f3PtpSysTimeOfDayClock.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3PtpSysTimeOfDayClock.setStatus("current")
_F3PtpBCTable_Object = MibTable
f3PtpBCTable = _F3PtpBCTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 1, 11)
)
if mibBuilder.loadTexts:
    f3PtpBCTable.setStatus("current")
_F3PtpBCEntry_Object = MibTableRow
f3PtpBCEntry = _F3PtpBCEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 1, 11, 1)
)
f3PtpBCEntry.setIndexNames(
    (0, "CM-ENTITY-MIB", "neIndex"),
    (0, "F3-PTP-MIB", "f3PtpBCIndex"),
)
if mibBuilder.loadTexts:
    f3PtpBCEntry.setStatus("current")
_F3PtpBCIndex_Type = Integer32
_F3PtpBCIndex_Object = MibTableColumn
f3PtpBCIndex = _F3PtpBCIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 1, 11, 1, 1),
    _F3PtpBCIndex_Type()
)
f3PtpBCIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    f3PtpBCIndex.setStatus("current")


class _F3PtpBCAlias_Type(DisplayString):
    """Custom type f3PtpBCAlias based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_F3PtpBCAlias_Type.__name__ = "DisplayString"
_F3PtpBCAlias_Object = MibTableColumn
f3PtpBCAlias = _F3PtpBCAlias_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 1, 11, 1, 2),
    _F3PtpBCAlias_Type()
)
f3PtpBCAlias.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3PtpBCAlias.setStatus("current")
_F3PtpBCAdminState_Type = AdminState
_F3PtpBCAdminState_Object = MibTableColumn
f3PtpBCAdminState = _F3PtpBCAdminState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 1, 11, 1, 3),
    _F3PtpBCAdminState_Type()
)
f3PtpBCAdminState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3PtpBCAdminState.setStatus("current")
_F3PtpBCOperationalState_Type = OperationalState
_F3PtpBCOperationalState_Object = MibTableColumn
f3PtpBCOperationalState = _F3PtpBCOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 1, 11, 1, 4),
    _F3PtpBCOperationalState_Type()
)
f3PtpBCOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpBCOperationalState.setStatus("current")
_F3PtpBCSecondaryState_Type = SecondaryState
_F3PtpBCSecondaryState_Object = MibTableColumn
f3PtpBCSecondaryState = _F3PtpBCSecondaryState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 1, 11, 1, 5),
    _F3PtpBCSecondaryState_Type()
)
f3PtpBCSecondaryState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpBCSecondaryState.setStatus("current")
_F3PtpBCClockIdentity_Type = ClockIdentity
_F3PtpBCClockIdentity_Object = MibTableColumn
f3PtpBCClockIdentity = _F3PtpBCClockIdentity_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 1, 11, 1, 6),
    _F3PtpBCClockIdentity_Type()
)
f3PtpBCClockIdentity.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3PtpBCClockIdentity.setStatus("current")
_F3PtpBCTimingSource_Type = VariablePointer
_F3PtpBCTimingSource_Object = MibTableColumn
f3PtpBCTimingSource = _F3PtpBCTimingSource_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 1, 11, 1, 7),
    _F3PtpBCTimingSource_Type()
)
f3PtpBCTimingSource.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3PtpBCTimingSource.setStatus("current")
_F3PtpBCClockClass_Type = Unsigned32
_F3PtpBCClockClass_Object = MibTableColumn
f3PtpBCClockClass = _F3PtpBCClockClass_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 1, 11, 1, 8),
    _F3PtpBCClockClass_Type()
)
f3PtpBCClockClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpBCClockClass.setStatus("deprecated")
_F3PtpBCDomainNumber_Type = Integer32
_F3PtpBCDomainNumber_Object = MibTableColumn
f3PtpBCDomainNumber = _F3PtpBCDomainNumber_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 1, 11, 1, 9),
    _F3PtpBCDomainNumber_Type()
)
f3PtpBCDomainNumber.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3PtpBCDomainNumber.setStatus("current")
_F3PtpBCStorageType_Type = StorageType
_F3PtpBCStorageType_Object = MibTableColumn
f3PtpBCStorageType = _F3PtpBCStorageType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 1, 11, 1, 10),
    _F3PtpBCStorageType_Type()
)
f3PtpBCStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3PtpBCStorageType.setStatus("current")
_F3PtpBCRowStatus_Type = RowStatus
_F3PtpBCRowStatus_Object = MibTableColumn
f3PtpBCRowStatus = _F3PtpBCRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 1, 11, 1, 11),
    _F3PtpBCRowStatus_Type()
)
f3PtpBCRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3PtpBCRowStatus.setStatus("current")
_F3PtpBCPhysicalEntityIndex_Type = Integer32
_F3PtpBCPhysicalEntityIndex_Object = MibTableColumn
f3PtpBCPhysicalEntityIndex = _F3PtpBCPhysicalEntityIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 1, 11, 1, 12),
    _F3PtpBCPhysicalEntityIndex_Type()
)
f3PtpBCPhysicalEntityIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3PtpBCPhysicalEntityIndex.setStatus("current")
_F3PtpBCMediationControl_Type = TruthValue
_F3PtpBCMediationControl_Object = MibTableColumn
f3PtpBCMediationControl = _F3PtpBCMediationControl_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 1, 11, 1, 13),
    _F3PtpBCMediationControl_Type()
)
f3PtpBCMediationControl.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3PtpBCMediationControl.setStatus("current")
_F3PtpMasterClockTable_Object = MibTable
f3PtpMasterClockTable = _F3PtpMasterClockTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 1, 12)
)
if mibBuilder.loadTexts:
    f3PtpMasterClockTable.setStatus("current")
_F3PtpMasterClockEntry_Object = MibTableRow
f3PtpMasterClockEntry = _F3PtpMasterClockEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 1, 12, 1)
)
f3PtpMasterClockEntry.setIndexNames(
    (0, "CM-ENTITY-MIB", "neIndex"),
    (0, "F3-PTP-MIB", "f3PtpMasterClockIndex"),
)
if mibBuilder.loadTexts:
    f3PtpMasterClockEntry.setStatus("current")
_F3PtpMasterClockIndex_Type = Integer32
_F3PtpMasterClockIndex_Object = MibTableColumn
f3PtpMasterClockIndex = _F3PtpMasterClockIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 1, 12, 1, 1),
    _F3PtpMasterClockIndex_Type()
)
f3PtpMasterClockIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    f3PtpMasterClockIndex.setStatus("current")


class _F3PtpMasterClockAlias_Type(DisplayString):
    """Custom type f3PtpMasterClockAlias based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_F3PtpMasterClockAlias_Type.__name__ = "DisplayString"
_F3PtpMasterClockAlias_Object = MibTableColumn
f3PtpMasterClockAlias = _F3PtpMasterClockAlias_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 1, 12, 1, 2),
    _F3PtpMasterClockAlias_Type()
)
f3PtpMasterClockAlias.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3PtpMasterClockAlias.setStatus("current")
_F3PtpMasterClockAdminState_Type = AdminState
_F3PtpMasterClockAdminState_Object = MibTableColumn
f3PtpMasterClockAdminState = _F3PtpMasterClockAdminState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 1, 12, 1, 3),
    _F3PtpMasterClockAdminState_Type()
)
f3PtpMasterClockAdminState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3PtpMasterClockAdminState.setStatus("current")
_F3PtpMasterClockOperationalState_Type = OperationalState
_F3PtpMasterClockOperationalState_Object = MibTableColumn
f3PtpMasterClockOperationalState = _F3PtpMasterClockOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 1, 12, 1, 4),
    _F3PtpMasterClockOperationalState_Type()
)
f3PtpMasterClockOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpMasterClockOperationalState.setStatus("current")
_F3PtpMasterClockSecondaryState_Type = SecondaryState
_F3PtpMasterClockSecondaryState_Object = MibTableColumn
f3PtpMasterClockSecondaryState = _F3PtpMasterClockSecondaryState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 1, 12, 1, 5),
    _F3PtpMasterClockSecondaryState_Type()
)
f3PtpMasterClockSecondaryState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpMasterClockSecondaryState.setStatus("current")
_F3PtpMasterClockClockIdentity_Type = ClockIdentity
_F3PtpMasterClockClockIdentity_Object = MibTableColumn
f3PtpMasterClockClockIdentity = _F3PtpMasterClockClockIdentity_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 1, 12, 1, 6),
    _F3PtpMasterClockClockIdentity_Type()
)
f3PtpMasterClockClockIdentity.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3PtpMasterClockClockIdentity.setStatus("current")
_F3PtpMasterClockTimeClock_Type = VariablePointer
_F3PtpMasterClockTimeClock_Object = MibTableColumn
f3PtpMasterClockTimeClock = _F3PtpMasterClockTimeClock_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 1, 12, 1, 7),
    _F3PtpMasterClockTimeClock_Type()
)
f3PtpMasterClockTimeClock.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3PtpMasterClockTimeClock.setStatus("current")
_F3PtpMasterClockDomainNumber_Type = Integer32
_F3PtpMasterClockDomainNumber_Object = MibTableColumn
f3PtpMasterClockDomainNumber = _F3PtpMasterClockDomainNumber_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 1, 12, 1, 8),
    _F3PtpMasterClockDomainNumber_Type()
)
f3PtpMasterClockDomainNumber.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3PtpMasterClockDomainNumber.setStatus("current")


class _F3PtpMasterClockPriority1_Type(Unsigned32):
    """Custom type f3PtpMasterClockPriority1 based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_F3PtpMasterClockPriority1_Type.__name__ = "Unsigned32"
_F3PtpMasterClockPriority1_Object = MibTableColumn
f3PtpMasterClockPriority1 = _F3PtpMasterClockPriority1_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 1, 12, 1, 9),
    _F3PtpMasterClockPriority1_Type()
)
f3PtpMasterClockPriority1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3PtpMasterClockPriority1.setStatus("current")


class _F3PtpMasterClockPriority2_Type(Unsigned32):
    """Custom type f3PtpMasterClockPriority2 based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_F3PtpMasterClockPriority2_Type.__name__ = "Unsigned32"
_F3PtpMasterClockPriority2_Object = MibTableColumn
f3PtpMasterClockPriority2 = _F3PtpMasterClockPriority2_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 1, 12, 1, 10),
    _F3PtpMasterClockPriority2_Type()
)
f3PtpMasterClockPriority2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3PtpMasterClockPriority2.setStatus("current")
_F3PtpMasterClockClockClass_Type = Unsigned32
_F3PtpMasterClockClockClass_Object = MibTableColumn
f3PtpMasterClockClockClass = _F3PtpMasterClockClockClass_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 1, 12, 1, 11),
    _F3PtpMasterClockClockClass_Type()
)
f3PtpMasterClockClockClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpMasterClockClockClass.setStatus("deprecated")
_F3PtpMasterClockClockAccuracy_Type = Unsigned32
_F3PtpMasterClockClockAccuracy_Object = MibTableColumn
f3PtpMasterClockClockAccuracy = _F3PtpMasterClockClockAccuracy_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 1, 12, 1, 12),
    _F3PtpMasterClockClockAccuracy_Type()
)
f3PtpMasterClockClockAccuracy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpMasterClockClockAccuracy.setStatus("obsolete")
_F3PtpMasterClockTimeScale_Type = TimeScale
_F3PtpMasterClockTimeScale_Object = MibTableColumn
f3PtpMasterClockTimeScale = _F3PtpMasterClockTimeScale_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 1, 12, 1, 13),
    _F3PtpMasterClockTimeScale_Type()
)
f3PtpMasterClockTimeScale.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpMasterClockTimeScale.setStatus("current")
_F3PtpMasterClockUtcOffset_Type = Integer32
_F3PtpMasterClockUtcOffset_Object = MibTableColumn
f3PtpMasterClockUtcOffset = _F3PtpMasterClockUtcOffset_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 1, 12, 1, 14),
    _F3PtpMasterClockUtcOffset_Type()
)
f3PtpMasterClockUtcOffset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpMasterClockUtcOffset.setStatus("current")
_F3PtpMasterClockStorageType_Type = StorageType
_F3PtpMasterClockStorageType_Object = MibTableColumn
f3PtpMasterClockStorageType = _F3PtpMasterClockStorageType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 1, 12, 1, 15),
    _F3PtpMasterClockStorageType_Type()
)
f3PtpMasterClockStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3PtpMasterClockStorageType.setStatus("current")
_F3PtpMasterClockRowStatus_Type = RowStatus
_F3PtpMasterClockRowStatus_Object = MibTableColumn
f3PtpMasterClockRowStatus = _F3PtpMasterClockRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 1, 12, 1, 16),
    _F3PtpMasterClockRowStatus_Type()
)
f3PtpMasterClockRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3PtpMasterClockRowStatus.setStatus("current")
_F3PtpMasterClockActiveTimeRef_Type = VariablePointer
_F3PtpMasterClockActiveTimeRef_Object = MibTableColumn
f3PtpMasterClockActiveTimeRef = _F3PtpMasterClockActiveTimeRef_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 1, 12, 1, 17),
    _F3PtpMasterClockActiveTimeRef_Type()
)
f3PtpMasterClockActiveTimeRef.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpMasterClockActiveTimeRef.setStatus("current")
_F3PtpMasterClockPTPProfile_Type = PTPProfile
_F3PtpMasterClockPTPProfile_Object = MibTableColumn
f3PtpMasterClockPTPProfile = _F3PtpMasterClockPTPProfile_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 1, 12, 1, 18),
    _F3PtpMasterClockPTPProfile_Type()
)
f3PtpMasterClockPTPProfile.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3PtpMasterClockPTPProfile.setStatus("current")
_F3PtpMasterClockPhysicalEntityIndex_Type = Integer32
_F3PtpMasterClockPhysicalEntityIndex_Object = MibTableColumn
f3PtpMasterClockPhysicalEntityIndex = _F3PtpMasterClockPhysicalEntityIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 1, 12, 1, 19),
    _F3PtpMasterClockPhysicalEntityIndex_Type()
)
f3PtpMasterClockPhysicalEntityIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3PtpMasterClockPhysicalEntityIndex.setStatus("current")
_F3PtpMasterClockActiveGrantsAnnounceService_Type = Integer32
_F3PtpMasterClockActiveGrantsAnnounceService_Object = MibTableColumn
f3PtpMasterClockActiveGrantsAnnounceService = _F3PtpMasterClockActiveGrantsAnnounceService_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 1, 12, 1, 20),
    _F3PtpMasterClockActiveGrantsAnnounceService_Type()
)
f3PtpMasterClockActiveGrantsAnnounceService.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpMasterClockActiveGrantsAnnounceService.setStatus("current")
_F3PtpMasterClockActiveGrantsSyncService_Type = Integer32
_F3PtpMasterClockActiveGrantsSyncService_Object = MibTableColumn
f3PtpMasterClockActiveGrantsSyncService = _F3PtpMasterClockActiveGrantsSyncService_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 1, 12, 1, 21),
    _F3PtpMasterClockActiveGrantsSyncService_Type()
)
f3PtpMasterClockActiveGrantsSyncService.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpMasterClockActiveGrantsSyncService.setStatus("current")
_F3PtpMasterClockActiveGrantsDelayRequestService_Type = Integer32
_F3PtpMasterClockActiveGrantsDelayRequestService_Object = MibTableColumn
f3PtpMasterClockActiveGrantsDelayRequestService = _F3PtpMasterClockActiveGrantsDelayRequestService_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 1, 12, 1, 22),
    _F3PtpMasterClockActiveGrantsDelayRequestService_Type()
)
f3PtpMasterClockActiveGrantsDelayRequestService.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpMasterClockActiveGrantsDelayRequestService.setStatus("current")
_F3PtpMasterClockServiceAvailableTime_Type = Unsigned32
_F3PtpMasterClockServiceAvailableTime_Object = MibTableColumn
f3PtpMasterClockServiceAvailableTime = _F3PtpMasterClockServiceAvailableTime_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 1, 12, 1, 23),
    _F3PtpMasterClockServiceAvailableTime_Type()
)
f3PtpMasterClockServiceAvailableTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpMasterClockServiceAvailableTime.setStatus("current")
_F3PtpMasterClockServiceUnavailableTime_Type = Unsigned32
_F3PtpMasterClockServiceUnavailableTime_Object = MibTableColumn
f3PtpMasterClockServiceUnavailableTime = _F3PtpMasterClockServiceUnavailableTime_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 1, 12, 1, 24),
    _F3PtpMasterClockServiceUnavailableTime_Type()
)
f3PtpMasterClockServiceUnavailableTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpMasterClockServiceUnavailableTime.setStatus("current")
_F3PtpMasterClockServiceAvailablePercentage_Type = DisplayString
_F3PtpMasterClockServiceAvailablePercentage_Object = MibTableColumn
f3PtpMasterClockServiceAvailablePercentage = _F3PtpMasterClockServiceAvailablePercentage_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 1, 12, 1, 25),
    _F3PtpMasterClockServiceAvailablePercentage_Type()
)
f3PtpMasterClockServiceAvailablePercentage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpMasterClockServiceAvailablePercentage.setStatus("current")
_F3PtpMasterClockSmpteSystemFrameRateNumerator_Type = Unsigned32
_F3PtpMasterClockSmpteSystemFrameRateNumerator_Object = MibTableColumn
f3PtpMasterClockSmpteSystemFrameRateNumerator = _F3PtpMasterClockSmpteSystemFrameRateNumerator_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 1, 12, 1, 26),
    _F3PtpMasterClockSmpteSystemFrameRateNumerator_Type()
)
f3PtpMasterClockSmpteSystemFrameRateNumerator.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3PtpMasterClockSmpteSystemFrameRateNumerator.setStatus("current")
_F3PtpMasterClockSmpteSystemFrameRateDenominator_Type = Unsigned32
_F3PtpMasterClockSmpteSystemFrameRateDenominator_Object = MibTableColumn
f3PtpMasterClockSmpteSystemFrameRateDenominator = _F3PtpMasterClockSmpteSystemFrameRateDenominator_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 1, 12, 1, 27),
    _F3PtpMasterClockSmpteSystemFrameRateDenominator_Type()
)
f3PtpMasterClockSmpteSystemFrameRateDenominator.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3PtpMasterClockSmpteSystemFrameRateDenominator.setStatus("current")


class _F3PtpMasterClockSmpteTimeAddressFlags_Type(Integer32):
    """Custom type f3PtpMasterClockSmpteTimeAddressFlags based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_F3PtpMasterClockSmpteTimeAddressFlags_Type.__name__ = "Integer32"
_F3PtpMasterClockSmpteTimeAddressFlags_Object = MibTableColumn
f3PtpMasterClockSmpteTimeAddressFlags = _F3PtpMasterClockSmpteTimeAddressFlags_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 1, 12, 1, 28),
    _F3PtpMasterClockSmpteTimeAddressFlags_Type()
)
f3PtpMasterClockSmpteTimeAddressFlags.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3PtpMasterClockSmpteTimeAddressFlags.setStatus("current")
_F3PtpMCITable_Object = MibTable
f3PtpMCITable = _F3PtpMCITable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 1, 13)
)
if mibBuilder.loadTexts:
    f3PtpMCITable.setStatus("current")
_F3PtpMCIEntry_Object = MibTableRow
f3PtpMCIEntry = _F3PtpMCIEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 1, 13, 1)
)
f3PtpMCIEntry.setIndexNames(
    (0, "CM-ENTITY-MIB", "neIndex"),
    (0, "F3-PTP-MIB", "f3PtpBCIndex"),
    (0, "F3-PTP-MIB", "f3PtpMCIIndex"),
)
if mibBuilder.loadTexts:
    f3PtpMCIEntry.setStatus("current")
_F3PtpMCIIndex_Type = Integer32
_F3PtpMCIIndex_Object = MibTableColumn
f3PtpMCIIndex = _F3PtpMCIIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 1, 13, 1, 1),
    _F3PtpMCIIndex_Type()
)
f3PtpMCIIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    f3PtpMCIIndex.setStatus("current")


class _F3PtpMCIAlias_Type(DisplayString):
    """Custom type f3PtpMCIAlias based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_F3PtpMCIAlias_Type.__name__ = "DisplayString"
_F3PtpMCIAlias_Object = MibTableColumn
f3PtpMCIAlias = _F3PtpMCIAlias_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 1, 13, 1, 2),
    _F3PtpMCIAlias_Type()
)
f3PtpMCIAlias.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3PtpMCIAlias.setStatus("current")
_F3PtpMCIAdminState_Type = AdminState
_F3PtpMCIAdminState_Object = MibTableColumn
f3PtpMCIAdminState = _F3PtpMCIAdminState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 1, 13, 1, 3),
    _F3PtpMCIAdminState_Type()
)
f3PtpMCIAdminState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3PtpMCIAdminState.setStatus("current")
_F3PtpMCIOperationalState_Type = OperationalState
_F3PtpMCIOperationalState_Object = MibTableColumn
f3PtpMCIOperationalState = _F3PtpMCIOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 1, 13, 1, 4),
    _F3PtpMCIOperationalState_Type()
)
f3PtpMCIOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpMCIOperationalState.setStatus("current")
_F3PtpMCISecondaryState_Type = SecondaryState
_F3PtpMCISecondaryState_Object = MibTableColumn
f3PtpMCISecondaryState = _F3PtpMCISecondaryState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 1, 13, 1, 5),
    _F3PtpMCISecondaryState_Type()
)
f3PtpMCISecondaryState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpMCISecondaryState.setStatus("current")
_F3PtpMCIPortIdentity_Type = PortIdentity
_F3PtpMCIPortIdentity_Object = MibTableColumn
f3PtpMCIPortIdentity = _F3PtpMCIPortIdentity_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 1, 13, 1, 6),
    _F3PtpMCIPortIdentity_Type()
)
f3PtpMCIPortIdentity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpMCIPortIdentity.setStatus("current")
_F3PtpMCIDomainNumber_Type = Integer32
_F3PtpMCIDomainNumber_Object = MibTableColumn
f3PtpMCIDomainNumber = _F3PtpMCIDomainNumber_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 1, 13, 1, 7),
    _F3PtpMCIDomainNumber_Type()
)
f3PtpMCIDomainNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3PtpMCIDomainNumber.setStatus("current")
_F3PtpMCIClockType_Type = MasterClockType
_F3PtpMCIClockType_Object = MibTableColumn
f3PtpMCIClockType = _F3PtpMCIClockType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 1, 13, 1, 8),
    _F3PtpMCIClockType_Type()
)
f3PtpMCIClockType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3PtpMCIClockType.setStatus("current")
_F3PtpMCIDelayMechanism_Type = DelayMechanism
_F3PtpMCIDelayMechanism_Object = MibTableColumn
f3PtpMCIDelayMechanism = _F3PtpMCIDelayMechanism_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 1, 13, 1, 9),
    _F3PtpMCIDelayMechanism_Type()
)
f3PtpMCIDelayMechanism.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3PtpMCIDelayMechanism.setStatus("current")


class _F3PtpMCIIfName_Type(DisplayString):
    """Custom type f3PtpMCIIfName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 15),
    )


_F3PtpMCIIfName_Type.__name__ = "DisplayString"
_F3PtpMCIIfName_Object = MibTableColumn
f3PtpMCIIfName = _F3PtpMCIIfName_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 1, 13, 1, 10),
    _F3PtpMCIIfName_Type()
)
f3PtpMCIIfName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3PtpMCIIfName.setStatus("current")
_F3PtpMCIIpProtocol_Type = IpVersion
_F3PtpMCIIpProtocol_Object = MibTableColumn
f3PtpMCIIpProtocol = _F3PtpMCIIpProtocol_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 1, 13, 1, 11),
    _F3PtpMCIIpProtocol_Type()
)
f3PtpMCIIpProtocol.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3PtpMCIIpProtocol.setStatus("current")
_F3PtpMCIMasterIpV4Address_Type = IpAddress
_F3PtpMCIMasterIpV4Address_Object = MibTableColumn
f3PtpMCIMasterIpV4Address = _F3PtpMCIMasterIpV4Address_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 1, 13, 1, 12),
    _F3PtpMCIMasterIpV4Address_Type()
)
f3PtpMCIMasterIpV4Address.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3PtpMCIMasterIpV4Address.setStatus("current")
_F3PtpMCIMasterIpV4SubnetMask_Type = IpAddress
_F3PtpMCIMasterIpV4SubnetMask_Object = MibTableColumn
f3PtpMCIMasterIpV4SubnetMask = _F3PtpMCIMasterIpV4SubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 1, 13, 1, 13),
    _F3PtpMCIMasterIpV4SubnetMask_Type()
)
f3PtpMCIMasterIpV4SubnetMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3PtpMCIMasterIpV4SubnetMask.setStatus("current")
_F3PtpMCIIpPriorityMapMode_Type = IpPriorityMapMode
_F3PtpMCIIpPriorityMapMode_Object = MibTableColumn
f3PtpMCIIpPriorityMapMode = _F3PtpMCIIpPriorityMapMode_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 1, 13, 1, 14),
    _F3PtpMCIIpPriorityMapMode_Type()
)
f3PtpMCIIpPriorityMapMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3PtpMCIIpPriorityMapMode.setStatus("current")


class _F3PtpMCIIpPriority_Type(Integer32):
    """Custom type f3PtpMCIIpPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_F3PtpMCIIpPriority_Type.__name__ = "Integer32"
_F3PtpMCIIpPriority_Object = MibTableColumn
f3PtpMCIIpPriority = _F3PtpMCIIpPriority_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 1, 13, 1, 15),
    _F3PtpMCIIpPriority_Type()
)
f3PtpMCIIpPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3PtpMCIIpPriority.setStatus("current")
_F3PtpMCIMaxLeaseDuration_Type = Integer32
_F3PtpMCIMaxLeaseDuration_Object = MibTableColumn
f3PtpMCIMaxLeaseDuration = _F3PtpMCIMaxLeaseDuration_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 1, 13, 1, 16),
    _F3PtpMCIMaxLeaseDuration_Type()
)
f3PtpMCIMaxLeaseDuration.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3PtpMCIMaxLeaseDuration.setStatus("current")
_F3PtpMCIMaxSlavesSupported_Type = Integer32
_F3PtpMCIMaxSlavesSupported_Object = MibTableColumn
f3PtpMCIMaxSlavesSupported = _F3PtpMCIMaxSlavesSupported_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 1, 13, 1, 17),
    _F3PtpMCIMaxSlavesSupported_Type()
)
f3PtpMCIMaxSlavesSupported.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3PtpMCIMaxSlavesSupported.setStatus("current")
_F3PtpMCIMaxStaticSlavesSupported_Type = Integer32
_F3PtpMCIMaxStaticSlavesSupported_Object = MibTableColumn
f3PtpMCIMaxStaticSlavesSupported = _F3PtpMCIMaxStaticSlavesSupported_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 1, 13, 1, 18),
    _F3PtpMCIMaxStaticSlavesSupported_Type()
)
f3PtpMCIMaxStaticSlavesSupported.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3PtpMCIMaxStaticSlavesSupported.setStatus("current")
_F3PtpMCIMaxSyncMsgRate_Type = SyncMsgRate
_F3PtpMCIMaxSyncMsgRate_Object = MibTableColumn
f3PtpMCIMaxSyncMsgRate = _F3PtpMCIMaxSyncMsgRate_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 1, 13, 1, 19),
    _F3PtpMCIMaxSyncMsgRate_Type()
)
f3PtpMCIMaxSyncMsgRate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3PtpMCIMaxSyncMsgRate.setStatus("current")
_F3PtpMCIMaxDelayRespMsgRate_Type = DelayRespMsgRate
_F3PtpMCIMaxDelayRespMsgRate_Object = MibTableColumn
f3PtpMCIMaxDelayRespMsgRate = _F3PtpMCIMaxDelayRespMsgRate_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 1, 13, 1, 20),
    _F3PtpMCIMaxDelayRespMsgRate_Type()
)
f3PtpMCIMaxDelayRespMsgRate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3PtpMCIMaxDelayRespMsgRate.setStatus("current")
_F3PtpMCIMaxAnnounceMsgRate_Type = AnnounceMsgRate
_F3PtpMCIMaxAnnounceMsgRate_Object = MibTableColumn
f3PtpMCIMaxAnnounceMsgRate = _F3PtpMCIMaxAnnounceMsgRate_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 1, 13, 1, 21),
    _F3PtpMCIMaxAnnounceMsgRate_Type()
)
f3PtpMCIMaxAnnounceMsgRate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3PtpMCIMaxAnnounceMsgRate.setStatus("current")
_F3PtpMCIStorageType_Type = StorageType
_F3PtpMCIStorageType_Object = MibTableColumn
f3PtpMCIStorageType = _F3PtpMCIStorageType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 1, 13, 1, 22),
    _F3PtpMCIStorageType_Type()
)
f3PtpMCIStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3PtpMCIStorageType.setStatus("current")
_F3PtpMCIRowStatus_Type = RowStatus
_F3PtpMCIRowStatus_Object = MibTableColumn
f3PtpMCIRowStatus = _F3PtpMCIRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 1, 13, 1, 23),
    _F3PtpMCIRowStatus_Type()
)
f3PtpMCIRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3PtpMCIRowStatus.setStatus("current")
_F3PtpMCIServiceFlow_Type = VariablePointer
_F3PtpMCIServiceFlow_Object = MibTableColumn
f3PtpMCIServiceFlow = _F3PtpMCIServiceFlow_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 1, 13, 1, 24),
    _F3PtpMCIServiceFlow_Type()
)
f3PtpMCIServiceFlow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3PtpMCIServiceFlow.setStatus("current")
_F3PtpMCIClockClassProfile_Type = ClockClassProfile
_F3PtpMCIClockClassProfile_Object = MibTableColumn
f3PtpMCIClockClassProfile = _F3PtpMCIClockClassProfile_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 1, 13, 1, 25),
    _F3PtpMCIClockClassProfile_Type()
)
f3PtpMCIClockClassProfile.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3PtpMCIClockClassProfile.setStatus("current")
_F3PtpMCIClockClass_Type = Unsigned32
_F3PtpMCIClockClass_Object = MibTableColumn
f3PtpMCIClockClass = _F3PtpMCIClockClass_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 1, 13, 1, 26),
    _F3PtpMCIClockClass_Type()
)
f3PtpMCIClockClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpMCIClockClass.setStatus("current")
_F3PtpMCIAnnounceExtTLVEnable_Type = TruthValue
_F3PtpMCIAnnounceExtTLVEnable_Object = MibTableColumn
f3PtpMCIAnnounceExtTLVEnable = _F3PtpMCIAnnounceExtTLVEnable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 1, 13, 1, 27),
    _F3PtpMCIAnnounceExtTLVEnable_Type()
)
f3PtpMCIAnnounceExtTLVEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3PtpMCIAnnounceExtTLVEnable.setStatus("current")
_F3PtpMCIPtpTransport_Type = PTPTransport
_F3PtpMCIPtpTransport_Object = MibTableColumn
f3PtpMCIPtpTransport = _F3PtpMCIPtpTransport_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 1, 13, 1, 28),
    _F3PtpMCIPtpTransport_Type()
)
f3PtpMCIPtpTransport.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3PtpMCIPtpTransport.setStatus("current")
_F3PtpMCIPtpTransportMode_Type = PTPTransportMode
_F3PtpMCIPtpTransportMode_Object = MibTableColumn
f3PtpMCIPtpTransportMode = _F3PtpMCIPtpTransportMode_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 1, 13, 1, 29),
    _F3PtpMCIPtpTransportMode_Type()
)
f3PtpMCIPtpTransportMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpMCIPtpTransportMode.setStatus("current")


class _F3PtpMCIPtpRemoteSlaveAgingTimeout_Type(Integer32):
    """Custom type f3PtpMCIPtpRemoteSlaveAgingTimeout based on Integer32"""
    defaultValue = 60

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 300),
    )


_F3PtpMCIPtpRemoteSlaveAgingTimeout_Type.__name__ = "Integer32"
_F3PtpMCIPtpRemoteSlaveAgingTimeout_Object = MibTableColumn
f3PtpMCIPtpRemoteSlaveAgingTimeout = _F3PtpMCIPtpRemoteSlaveAgingTimeout_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 1, 13, 1, 30),
    _F3PtpMCIPtpRemoteSlaveAgingTimeout_Type()
)
f3PtpMCIPtpRemoteSlaveAgingTimeout.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3PtpMCIPtpRemoteSlaveAgingTimeout.setStatus("current")
_F3PtpMCIMasterIpV6Address_Type = Ipv6Address
_F3PtpMCIMasterIpV6Address_Object = MibTableColumn
f3PtpMCIMasterIpV6Address = _F3PtpMCIMasterIpV6Address_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 1, 13, 1, 31),
    _F3PtpMCIMasterIpV6Address_Type()
)
f3PtpMCIMasterIpV6Address.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3PtpMCIMasterIpV6Address.setStatus("current")


class _F3PtpMCIMasterIpV6AddrPrefixLength_Type(Integer32):
    """Custom type f3PtpMCIMasterIpV6AddrPrefixLength based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_F3PtpMCIMasterIpV6AddrPrefixLength_Type.__name__ = "Integer32"
_F3PtpMCIMasterIpV6AddrPrefixLength_Object = MibTableColumn
f3PtpMCIMasterIpV6AddrPrefixLength = _F3PtpMCIMasterIpV6AddrPrefixLength_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 1, 13, 1, 32),
    _F3PtpMCIMasterIpV6AddrPrefixLength_Type()
)
f3PtpMCIMasterIpV6AddrPrefixLength.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3PtpMCIMasterIpV6AddrPrefixLength.setStatus("current")
_F3PtpMCIDefaultGatewayControl_Type = ToggleValue
_F3PtpMCIDefaultGatewayControl_Object = MibTableColumn
f3PtpMCIDefaultGatewayControl = _F3PtpMCIDefaultGatewayControl_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 1, 13, 1, 33),
    _F3PtpMCIDefaultGatewayControl_Type()
)
f3PtpMCIDefaultGatewayControl.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3PtpMCIDefaultGatewayControl.setStatus("current")
_F3PtpMCIGateway_Type = IpAddress
_F3PtpMCIGateway_Object = MibTableColumn
f3PtpMCIGateway = _F3PtpMCIGateway_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 1, 13, 1, 34),
    _F3PtpMCIGateway_Type()
)
f3PtpMCIGateway.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3PtpMCIGateway.setStatus("current")
_F3PtpMCIIpV6Gateway_Type = Ipv6Address
_F3PtpMCIIpV6Gateway_Object = MibTableColumn
f3PtpMCIIpV6Gateway = _F3PtpMCIIpV6Gateway_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 1, 13, 1, 35),
    _F3PtpMCIIpV6Gateway_Type()
)
f3PtpMCIIpV6Gateway.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3PtpMCIIpV6Gateway.setStatus("current")
_F3PtpMasterVirtualPortTable_Object = MibTable
f3PtpMasterVirtualPortTable = _F3PtpMasterVirtualPortTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 1, 14)
)
if mibBuilder.loadTexts:
    f3PtpMasterVirtualPortTable.setStatus("current")
_F3PtpMasterVirtualPortEntry_Object = MibTableRow
f3PtpMasterVirtualPortEntry = _F3PtpMasterVirtualPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 1, 14, 1)
)
f3PtpMasterVirtualPortEntry.setIndexNames(
    (0, "CM-ENTITY-MIB", "neIndex"),
    (0, "F3-PTP-MIB", "f3PtpBCIndex"),
    (0, "F3-PTP-MIB", "f3PtpMCIIndex"),
    (0, "F3-PTP-MIB", "f3PtpMasterVirtualPortIndex"),
)
if mibBuilder.loadTexts:
    f3PtpMasterVirtualPortEntry.setStatus("current")
_F3PtpMasterVirtualPortIndex_Type = Integer32
_F3PtpMasterVirtualPortIndex_Object = MibTableColumn
f3PtpMasterVirtualPortIndex = _F3PtpMasterVirtualPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 1, 14, 1, 1),
    _F3PtpMasterVirtualPortIndex_Type()
)
f3PtpMasterVirtualPortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    f3PtpMasterVirtualPortIndex.setStatus("current")


class _F3PtpMasterVirtualPortAlias_Type(DisplayString):
    """Custom type f3PtpMasterVirtualPortAlias based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_F3PtpMasterVirtualPortAlias_Type.__name__ = "DisplayString"
_F3PtpMasterVirtualPortAlias_Object = MibTableColumn
f3PtpMasterVirtualPortAlias = _F3PtpMasterVirtualPortAlias_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 1, 14, 1, 2),
    _F3PtpMasterVirtualPortAlias_Type()
)
f3PtpMasterVirtualPortAlias.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3PtpMasterVirtualPortAlias.setStatus("current")
_F3PtpMasterVirtualPortAdminState_Type = AdminState
_F3PtpMasterVirtualPortAdminState_Object = MibTableColumn
f3PtpMasterVirtualPortAdminState = _F3PtpMasterVirtualPortAdminState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 1, 14, 1, 3),
    _F3PtpMasterVirtualPortAdminState_Type()
)
f3PtpMasterVirtualPortAdminState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3PtpMasterVirtualPortAdminState.setStatus("current")
_F3PtpMasterVirtualPortOperationalState_Type = OperationalState
_F3PtpMasterVirtualPortOperationalState_Object = MibTableColumn
f3PtpMasterVirtualPortOperationalState = _F3PtpMasterVirtualPortOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 1, 14, 1, 4),
    _F3PtpMasterVirtualPortOperationalState_Type()
)
f3PtpMasterVirtualPortOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpMasterVirtualPortOperationalState.setStatus("current")
_F3PtpMasterVirtualPortSecondaryState_Type = SecondaryState
_F3PtpMasterVirtualPortSecondaryState_Object = MibTableColumn
f3PtpMasterVirtualPortSecondaryState = _F3PtpMasterVirtualPortSecondaryState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 1, 14, 1, 5),
    _F3PtpMasterVirtualPortSecondaryState_Type()
)
f3PtpMasterVirtualPortSecondaryState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpMasterVirtualPortSecondaryState.setStatus("current")
_F3PtpMasterVirtualPortFlowPoint_Type = VariablePointer
_F3PtpMasterVirtualPortFlowPoint_Object = MibTableColumn
f3PtpMasterVirtualPortFlowPoint = _F3PtpMasterVirtualPortFlowPoint_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 1, 14, 1, 6),
    _F3PtpMasterVirtualPortFlowPoint_Type()
)
f3PtpMasterVirtualPortFlowPoint.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3PtpMasterVirtualPortFlowPoint.setStatus("current")
_F3PtpMasterVirtualPortStorageType_Type = StorageType
_F3PtpMasterVirtualPortStorageType_Object = MibTableColumn
f3PtpMasterVirtualPortStorageType = _F3PtpMasterVirtualPortStorageType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 1, 14, 1, 7),
    _F3PtpMasterVirtualPortStorageType_Type()
)
f3PtpMasterVirtualPortStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3PtpMasterVirtualPortStorageType.setStatus("current")
_F3PtpMasterVirtualPortRowStatus_Type = RowStatus
_F3PtpMasterVirtualPortRowStatus_Object = MibTableColumn
f3PtpMasterVirtualPortRowStatus = _F3PtpMasterVirtualPortRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 1, 14, 1, 8),
    _F3PtpMasterVirtualPortRowStatus_Type()
)
f3PtpMasterVirtualPortRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3PtpMasterVirtualPortRowStatus.setStatus("current")
_F3PtpStaticRemoteSlaveTable_Object = MibTable
f3PtpStaticRemoteSlaveTable = _F3PtpStaticRemoteSlaveTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 1, 15)
)
if mibBuilder.loadTexts:
    f3PtpStaticRemoteSlaveTable.setStatus("current")
_F3PtpStaticRemoteSlaveEntry_Object = MibTableRow
f3PtpStaticRemoteSlaveEntry = _F3PtpStaticRemoteSlaveEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 1, 15, 1)
)
f3PtpStaticRemoteSlaveEntry.setIndexNames(
    (0, "CM-ENTITY-MIB", "neIndex"),
    (0, "F3-PTP-MIB", "f3PtpBCIndex"),
    (0, "F3-PTP-MIB", "f3PtpMCIIndex"),
    (0, "F3-PTP-MIB", "f3PtpStaticRemoteSlaveIndex"),
)
if mibBuilder.loadTexts:
    f3PtpStaticRemoteSlaveEntry.setStatus("current")
_F3PtpStaticRemoteSlaveIndex_Type = Integer32
_F3PtpStaticRemoteSlaveIndex_Object = MibTableColumn
f3PtpStaticRemoteSlaveIndex = _F3PtpStaticRemoteSlaveIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 1, 15, 1, 1),
    _F3PtpStaticRemoteSlaveIndex_Type()
)
f3PtpStaticRemoteSlaveIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    f3PtpStaticRemoteSlaveIndex.setStatus("current")


class _F3PtpStaticRemoteSlaveAlias_Type(DisplayString):
    """Custom type f3PtpStaticRemoteSlaveAlias based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_F3PtpStaticRemoteSlaveAlias_Type.__name__ = "DisplayString"
_F3PtpStaticRemoteSlaveAlias_Object = MibTableColumn
f3PtpStaticRemoteSlaveAlias = _F3PtpStaticRemoteSlaveAlias_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 1, 15, 1, 2),
    _F3PtpStaticRemoteSlaveAlias_Type()
)
f3PtpStaticRemoteSlaveAlias.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3PtpStaticRemoteSlaveAlias.setStatus("current")
_F3PtpStaticRemoteSlaveAdminState_Type = AdminState
_F3PtpStaticRemoteSlaveAdminState_Object = MibTableColumn
f3PtpStaticRemoteSlaveAdminState = _F3PtpStaticRemoteSlaveAdminState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 1, 15, 1, 3),
    _F3PtpStaticRemoteSlaveAdminState_Type()
)
f3PtpStaticRemoteSlaveAdminState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3PtpStaticRemoteSlaveAdminState.setStatus("current")
_F3PtpStaticRemoteSlaveOperationalState_Type = OperationalState
_F3PtpStaticRemoteSlaveOperationalState_Object = MibTableColumn
f3PtpStaticRemoteSlaveOperationalState = _F3PtpStaticRemoteSlaveOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 1, 15, 1, 4),
    _F3PtpStaticRemoteSlaveOperationalState_Type()
)
f3PtpStaticRemoteSlaveOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpStaticRemoteSlaveOperationalState.setStatus("current")
_F3PtpStaticRemoteSlaveSecondaryState_Type = SecondaryState
_F3PtpStaticRemoteSlaveSecondaryState_Object = MibTableColumn
f3PtpStaticRemoteSlaveSecondaryState = _F3PtpStaticRemoteSlaveSecondaryState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 1, 15, 1, 5),
    _F3PtpStaticRemoteSlaveSecondaryState_Type()
)
f3PtpStaticRemoteSlaveSecondaryState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpStaticRemoteSlaveSecondaryState.setStatus("current")
_F3PtpStaticRemoteSlaveClockIdentity_Type = ClockIdentity
_F3PtpStaticRemoteSlaveClockIdentity_Object = MibTableColumn
f3PtpStaticRemoteSlaveClockIdentity = _F3PtpStaticRemoteSlaveClockIdentity_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 1, 15, 1, 6),
    _F3PtpStaticRemoteSlaveClockIdentity_Type()
)
f3PtpStaticRemoteSlaveClockIdentity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpStaticRemoteSlaveClockIdentity.setStatus("current")
_F3PtpStaticRemoteSlaveIpV4Address_Type = IpAddress
_F3PtpStaticRemoteSlaveIpV4Address_Object = MibTableColumn
f3PtpStaticRemoteSlaveIpV4Address = _F3PtpStaticRemoteSlaveIpV4Address_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 1, 15, 1, 7),
    _F3PtpStaticRemoteSlaveIpV4Address_Type()
)
f3PtpStaticRemoteSlaveIpV4Address.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3PtpStaticRemoteSlaveIpV4Address.setStatus("current")
_F3PtpStaticRemoteSlaveTimeCreated_Type = DateAndTime
_F3PtpStaticRemoteSlaveTimeCreated_Object = MibTableColumn
f3PtpStaticRemoteSlaveTimeCreated = _F3PtpStaticRemoteSlaveTimeCreated_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 1, 15, 1, 8),
    _F3PtpStaticRemoteSlaveTimeCreated_Type()
)
f3PtpStaticRemoteSlaveTimeCreated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpStaticRemoteSlaveTimeCreated.setStatus("current")
_F3PtpStaticRemoteSlaveSyncMsgRate_Type = SyncMsgRate
_F3PtpStaticRemoteSlaveSyncMsgRate_Object = MibTableColumn
f3PtpStaticRemoteSlaveSyncMsgRate = _F3PtpStaticRemoteSlaveSyncMsgRate_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 1, 15, 1, 9),
    _F3PtpStaticRemoteSlaveSyncMsgRate_Type()
)
f3PtpStaticRemoteSlaveSyncMsgRate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3PtpStaticRemoteSlaveSyncMsgRate.setStatus("current")
_F3PtpStaticRemoteSlaveDelayRspMsgRate_Type = DelayRespMsgRate
_F3PtpStaticRemoteSlaveDelayRspMsgRate_Object = MibTableColumn
f3PtpStaticRemoteSlaveDelayRspMsgRate = _F3PtpStaticRemoteSlaveDelayRspMsgRate_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 1, 15, 1, 10),
    _F3PtpStaticRemoteSlaveDelayRspMsgRate_Type()
)
f3PtpStaticRemoteSlaveDelayRspMsgRate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3PtpStaticRemoteSlaveDelayRspMsgRate.setStatus("current")
_F3PtpStaticRemoteSlaveAnnounceMsgRate_Type = AnnounceMsgRate
_F3PtpStaticRemoteSlaveAnnounceMsgRate_Object = MibTableColumn
f3PtpStaticRemoteSlaveAnnounceMsgRate = _F3PtpStaticRemoteSlaveAnnounceMsgRate_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 1, 15, 1, 11),
    _F3PtpStaticRemoteSlaveAnnounceMsgRate_Type()
)
f3PtpStaticRemoteSlaveAnnounceMsgRate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3PtpStaticRemoteSlaveAnnounceMsgRate.setStatus("current")
_F3PtpStaticRemoteSlaveNegSyncLeaseDur_Type = Integer32
_F3PtpStaticRemoteSlaveNegSyncLeaseDur_Object = MibTableColumn
f3PtpStaticRemoteSlaveNegSyncLeaseDur = _F3PtpStaticRemoteSlaveNegSyncLeaseDur_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 1, 15, 1, 12),
    _F3PtpStaticRemoteSlaveNegSyncLeaseDur_Type()
)
f3PtpStaticRemoteSlaveNegSyncLeaseDur.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpStaticRemoteSlaveNegSyncLeaseDur.setStatus("current")
_F3PtpStaticRemoteSlaveNegDelayRspLeaseDur_Type = Integer32
_F3PtpStaticRemoteSlaveNegDelayRspLeaseDur_Object = MibTableColumn
f3PtpStaticRemoteSlaveNegDelayRspLeaseDur = _F3PtpStaticRemoteSlaveNegDelayRspLeaseDur_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 1, 15, 1, 13),
    _F3PtpStaticRemoteSlaveNegDelayRspLeaseDur_Type()
)
f3PtpStaticRemoteSlaveNegDelayRspLeaseDur.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpStaticRemoteSlaveNegDelayRspLeaseDur.setStatus("current")
_F3PtpStaticRemoteSlaveNegAnnounceLeaseDur_Type = Integer32
_F3PtpStaticRemoteSlaveNegAnnounceLeaseDur_Object = MibTableColumn
f3PtpStaticRemoteSlaveNegAnnounceLeaseDur = _F3PtpStaticRemoteSlaveNegAnnounceLeaseDur_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 1, 15, 1, 14),
    _F3PtpStaticRemoteSlaveNegAnnounceLeaseDur_Type()
)
f3PtpStaticRemoteSlaveNegAnnounceLeaseDur.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpStaticRemoteSlaveNegAnnounceLeaseDur.setStatus("current")
_F3PtpStaticRemoteSlaveSyncDurRemTime_Type = Unsigned32
_F3PtpStaticRemoteSlaveSyncDurRemTime_Object = MibTableColumn
f3PtpStaticRemoteSlaveSyncDurRemTime = _F3PtpStaticRemoteSlaveSyncDurRemTime_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 1, 15, 1, 15),
    _F3PtpStaticRemoteSlaveSyncDurRemTime_Type()
)
f3PtpStaticRemoteSlaveSyncDurRemTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpStaticRemoteSlaveSyncDurRemTime.setStatus("current")
_F3PtpStaticRemoteSlaveDelayRspDurRemTime_Type = Unsigned32
_F3PtpStaticRemoteSlaveDelayRspDurRemTime_Object = MibTableColumn
f3PtpStaticRemoteSlaveDelayRspDurRemTime = _F3PtpStaticRemoteSlaveDelayRspDurRemTime_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 1, 15, 1, 16),
    _F3PtpStaticRemoteSlaveDelayRspDurRemTime_Type()
)
f3PtpStaticRemoteSlaveDelayRspDurRemTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpStaticRemoteSlaveDelayRspDurRemTime.setStatus("current")
_F3PtpStaticRemoteSlaveAnnounceDurRemTime_Type = Unsigned32
_F3PtpStaticRemoteSlaveAnnounceDurRemTime_Object = MibTableColumn
f3PtpStaticRemoteSlaveAnnounceDurRemTime = _F3PtpStaticRemoteSlaveAnnounceDurRemTime_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 1, 15, 1, 17),
    _F3PtpStaticRemoteSlaveAnnounceDurRemTime_Type()
)
f3PtpStaticRemoteSlaveAnnounceDurRemTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpStaticRemoteSlaveAnnounceDurRemTime.setStatus("current")
_F3PtpStaticRemoteSlaveUmnControl_Type = TruthValue
_F3PtpStaticRemoteSlaveUmnControl_Object = MibTableColumn
f3PtpStaticRemoteSlaveUmnControl = _F3PtpStaticRemoteSlaveUmnControl_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 1, 15, 1, 18),
    _F3PtpStaticRemoteSlaveUmnControl_Type()
)
f3PtpStaticRemoteSlaveUmnControl.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3PtpStaticRemoteSlaveUmnControl.setStatus("current")
_F3PtpStaticRemoteSlaveStorageType_Type = StorageType
_F3PtpStaticRemoteSlaveStorageType_Object = MibTableColumn
f3PtpStaticRemoteSlaveStorageType = _F3PtpStaticRemoteSlaveStorageType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 1, 15, 1, 19),
    _F3PtpStaticRemoteSlaveStorageType_Type()
)
f3PtpStaticRemoteSlaveStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3PtpStaticRemoteSlaveStorageType.setStatus("current")
_F3PtpStaticRemoteSlaveRowStatus_Type = RowStatus
_F3PtpStaticRemoteSlaveRowStatus_Object = MibTableColumn
f3PtpStaticRemoteSlaveRowStatus = _F3PtpStaticRemoteSlaveRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 1, 15, 1, 20),
    _F3PtpStaticRemoteSlaveRowStatus_Type()
)
f3PtpStaticRemoteSlaveRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3PtpStaticRemoteSlaveRowStatus.setStatus("current")
_F3PtpStaticRemoteSlaveIpV6Address_Type = Ipv6Address
_F3PtpStaticRemoteSlaveIpV6Address_Object = MibTableColumn
f3PtpStaticRemoteSlaveIpV6Address = _F3PtpStaticRemoteSlaveIpV6Address_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 1, 15, 1, 21),
    _F3PtpStaticRemoteSlaveIpV6Address_Type()
)
f3PtpStaticRemoteSlaveIpV6Address.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3PtpStaticRemoteSlaveIpV6Address.setStatus("current")
_F3PtpDynamicRemoteSlaveTable_Object = MibTable
f3PtpDynamicRemoteSlaveTable = _F3PtpDynamicRemoteSlaveTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 1, 16)
)
if mibBuilder.loadTexts:
    f3PtpDynamicRemoteSlaveTable.setStatus("current")
_F3PtpDynamicRemoteSlaveEntry_Object = MibTableRow
f3PtpDynamicRemoteSlaveEntry = _F3PtpDynamicRemoteSlaveEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 1, 16, 1)
)
f3PtpDynamicRemoteSlaveEntry.setIndexNames(
    (0, "CM-ENTITY-MIB", "neIndex"),
    (0, "F3-PTP-MIB", "f3PtpBCIndex"),
    (0, "F3-PTP-MIB", "f3PtpMCIIndex"),
    (0, "F3-PTP-MIB", "f3PtpDynamicRemoteSlaveIndex"),
)
if mibBuilder.loadTexts:
    f3PtpDynamicRemoteSlaveEntry.setStatus("current")
_F3PtpDynamicRemoteSlaveIndex_Type = Integer32
_F3PtpDynamicRemoteSlaveIndex_Object = MibTableColumn
f3PtpDynamicRemoteSlaveIndex = _F3PtpDynamicRemoteSlaveIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 1, 16, 1, 1),
    _F3PtpDynamicRemoteSlaveIndex_Type()
)
f3PtpDynamicRemoteSlaveIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    f3PtpDynamicRemoteSlaveIndex.setStatus("current")


class _F3PtpDynamicRemoteSlaveAlias_Type(DisplayString):
    """Custom type f3PtpDynamicRemoteSlaveAlias based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_F3PtpDynamicRemoteSlaveAlias_Type.__name__ = "DisplayString"
_F3PtpDynamicRemoteSlaveAlias_Object = MibTableColumn
f3PtpDynamicRemoteSlaveAlias = _F3PtpDynamicRemoteSlaveAlias_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 1, 16, 1, 2),
    _F3PtpDynamicRemoteSlaveAlias_Type()
)
f3PtpDynamicRemoteSlaveAlias.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3PtpDynamicRemoteSlaveAlias.setStatus("current")
_F3PtpDynamicRemoteSlaveAdminState_Type = AdminState
_F3PtpDynamicRemoteSlaveAdminState_Object = MibTableColumn
f3PtpDynamicRemoteSlaveAdminState = _F3PtpDynamicRemoteSlaveAdminState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 1, 16, 1, 3),
    _F3PtpDynamicRemoteSlaveAdminState_Type()
)
f3PtpDynamicRemoteSlaveAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3PtpDynamicRemoteSlaveAdminState.setStatus("current")
_F3PtpDynamicRemoteSlaveOperationalState_Type = OperationalState
_F3PtpDynamicRemoteSlaveOperationalState_Object = MibTableColumn
f3PtpDynamicRemoteSlaveOperationalState = _F3PtpDynamicRemoteSlaveOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 1, 16, 1, 4),
    _F3PtpDynamicRemoteSlaveOperationalState_Type()
)
f3PtpDynamicRemoteSlaveOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpDynamicRemoteSlaveOperationalState.setStatus("current")
_F3PtpDynamicRemoteSlaveSecondaryState_Type = SecondaryState
_F3PtpDynamicRemoteSlaveSecondaryState_Object = MibTableColumn
f3PtpDynamicRemoteSlaveSecondaryState = _F3PtpDynamicRemoteSlaveSecondaryState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 1, 16, 1, 5),
    _F3PtpDynamicRemoteSlaveSecondaryState_Type()
)
f3PtpDynamicRemoteSlaveSecondaryState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpDynamicRemoteSlaveSecondaryState.setStatus("current")
_F3PtpDynamicRemoteSlaveClockIdentity_Type = ClockIdentity
_F3PtpDynamicRemoteSlaveClockIdentity_Object = MibTableColumn
f3PtpDynamicRemoteSlaveClockIdentity = _F3PtpDynamicRemoteSlaveClockIdentity_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 1, 16, 1, 6),
    _F3PtpDynamicRemoteSlaveClockIdentity_Type()
)
f3PtpDynamicRemoteSlaveClockIdentity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpDynamicRemoteSlaveClockIdentity.setStatus("current")
_F3PtpDynamicRemoteSlaveIpV4Address_Type = IpAddress
_F3PtpDynamicRemoteSlaveIpV4Address_Object = MibTableColumn
f3PtpDynamicRemoteSlaveIpV4Address = _F3PtpDynamicRemoteSlaveIpV4Address_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 1, 16, 1, 7),
    _F3PtpDynamicRemoteSlaveIpV4Address_Type()
)
f3PtpDynamicRemoteSlaveIpV4Address.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpDynamicRemoteSlaveIpV4Address.setStatus("current")
_F3PtpDynamicRemoteSlaveTimeCreated_Type = DateAndTime
_F3PtpDynamicRemoteSlaveTimeCreated_Object = MibTableColumn
f3PtpDynamicRemoteSlaveTimeCreated = _F3PtpDynamicRemoteSlaveTimeCreated_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 1, 16, 1, 8),
    _F3PtpDynamicRemoteSlaveTimeCreated_Type()
)
f3PtpDynamicRemoteSlaveTimeCreated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpDynamicRemoteSlaveTimeCreated.setStatus("current")
_F3PtpDynamicRemoteSlaveSyncMsgRate_Type = SyncMsgRate
_F3PtpDynamicRemoteSlaveSyncMsgRate_Object = MibTableColumn
f3PtpDynamicRemoteSlaveSyncMsgRate = _F3PtpDynamicRemoteSlaveSyncMsgRate_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 1, 16, 1, 9),
    _F3PtpDynamicRemoteSlaveSyncMsgRate_Type()
)
f3PtpDynamicRemoteSlaveSyncMsgRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpDynamicRemoteSlaveSyncMsgRate.setStatus("current")
_F3PtpDynamicRemoteSlaveDelayRspMsgRate_Type = DelayRespMsgRate
_F3PtpDynamicRemoteSlaveDelayRspMsgRate_Object = MibTableColumn
f3PtpDynamicRemoteSlaveDelayRspMsgRate = _F3PtpDynamicRemoteSlaveDelayRspMsgRate_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 1, 16, 1, 10),
    _F3PtpDynamicRemoteSlaveDelayRspMsgRate_Type()
)
f3PtpDynamicRemoteSlaveDelayRspMsgRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpDynamicRemoteSlaveDelayRspMsgRate.setStatus("current")
_F3PtpDynamicRemoteSlaveAnnounceMsgRate_Type = AnnounceMsgRate
_F3PtpDynamicRemoteSlaveAnnounceMsgRate_Object = MibTableColumn
f3PtpDynamicRemoteSlaveAnnounceMsgRate = _F3PtpDynamicRemoteSlaveAnnounceMsgRate_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 1, 16, 1, 11),
    _F3PtpDynamicRemoteSlaveAnnounceMsgRate_Type()
)
f3PtpDynamicRemoteSlaveAnnounceMsgRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpDynamicRemoteSlaveAnnounceMsgRate.setStatus("current")
_F3PtpDynamicRemoteSlaveNegSyncLeaseDur_Type = Integer32
_F3PtpDynamicRemoteSlaveNegSyncLeaseDur_Object = MibTableColumn
f3PtpDynamicRemoteSlaveNegSyncLeaseDur = _F3PtpDynamicRemoteSlaveNegSyncLeaseDur_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 1, 16, 1, 12),
    _F3PtpDynamicRemoteSlaveNegSyncLeaseDur_Type()
)
f3PtpDynamicRemoteSlaveNegSyncLeaseDur.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpDynamicRemoteSlaveNegSyncLeaseDur.setStatus("current")
_F3PtpDynamicRemoteSlaveNegDelayRspLeaseDur_Type = Integer32
_F3PtpDynamicRemoteSlaveNegDelayRspLeaseDur_Object = MibTableColumn
f3PtpDynamicRemoteSlaveNegDelayRspLeaseDur = _F3PtpDynamicRemoteSlaveNegDelayRspLeaseDur_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 1, 16, 1, 13),
    _F3PtpDynamicRemoteSlaveNegDelayRspLeaseDur_Type()
)
f3PtpDynamicRemoteSlaveNegDelayRspLeaseDur.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpDynamicRemoteSlaveNegDelayRspLeaseDur.setStatus("current")
_F3PtpDynamicRemoteSlaveNegAnnounceLeaseDur_Type = Integer32
_F3PtpDynamicRemoteSlaveNegAnnounceLeaseDur_Object = MibTableColumn
f3PtpDynamicRemoteSlaveNegAnnounceLeaseDur = _F3PtpDynamicRemoteSlaveNegAnnounceLeaseDur_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 1, 16, 1, 14),
    _F3PtpDynamicRemoteSlaveNegAnnounceLeaseDur_Type()
)
f3PtpDynamicRemoteSlaveNegAnnounceLeaseDur.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpDynamicRemoteSlaveNegAnnounceLeaseDur.setStatus("current")
_F3PtpDynamicRemoteSlaveSyncDurRemTime_Type = Unsigned32
_F3PtpDynamicRemoteSlaveSyncDurRemTime_Object = MibTableColumn
f3PtpDynamicRemoteSlaveSyncDurRemTime = _F3PtpDynamicRemoteSlaveSyncDurRemTime_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 1, 16, 1, 15),
    _F3PtpDynamicRemoteSlaveSyncDurRemTime_Type()
)
f3PtpDynamicRemoteSlaveSyncDurRemTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpDynamicRemoteSlaveSyncDurRemTime.setStatus("current")
_F3PtpDynamicRemoteSlaveDelayRspDurRemTime_Type = Unsigned32
_F3PtpDynamicRemoteSlaveDelayRspDurRemTime_Object = MibTableColumn
f3PtpDynamicRemoteSlaveDelayRspDurRemTime = _F3PtpDynamicRemoteSlaveDelayRspDurRemTime_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 1, 16, 1, 16),
    _F3PtpDynamicRemoteSlaveDelayRspDurRemTime_Type()
)
f3PtpDynamicRemoteSlaveDelayRspDurRemTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpDynamicRemoteSlaveDelayRspDurRemTime.setStatus("current")
_F3PtpDynamicRemoteSlaveAnnounceDurRemTime_Type = Unsigned32
_F3PtpDynamicRemoteSlaveAnnounceDurRemTime_Object = MibTableColumn
f3PtpDynamicRemoteSlaveAnnounceDurRemTime = _F3PtpDynamicRemoteSlaveAnnounceDurRemTime_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 1, 16, 1, 17),
    _F3PtpDynamicRemoteSlaveAnnounceDurRemTime_Type()
)
f3PtpDynamicRemoteSlaveAnnounceDurRemTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpDynamicRemoteSlaveAnnounceDurRemTime.setStatus("current")
_F3PtpDynamicRemoteSlaveRowStatus_Type = RowStatus
_F3PtpDynamicRemoteSlaveRowStatus_Object = MibTableColumn
f3PtpDynamicRemoteSlaveRowStatus = _F3PtpDynamicRemoteSlaveRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 1, 16, 1, 18),
    _F3PtpDynamicRemoteSlaveRowStatus_Type()
)
f3PtpDynamicRemoteSlaveRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3PtpDynamicRemoteSlaveRowStatus.setStatus("current")
_F3PtpDynamicRemoteSlaveStorageType_Type = StorageType
_F3PtpDynamicRemoteSlaveStorageType_Object = MibTableColumn
f3PtpDynamicRemoteSlaveStorageType = _F3PtpDynamicRemoteSlaveStorageType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 1, 16, 1, 19),
    _F3PtpDynamicRemoteSlaveStorageType_Type()
)
f3PtpDynamicRemoteSlaveStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3PtpDynamicRemoteSlaveStorageType.setStatus("current")
_F3PtpDynamicRemoteSlavePortIdentity_Type = PortIdentity
_F3PtpDynamicRemoteSlavePortIdentity_Object = MibTableColumn
f3PtpDynamicRemoteSlavePortIdentity = _F3PtpDynamicRemoteSlavePortIdentity_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 1, 16, 1, 20),
    _F3PtpDynamicRemoteSlavePortIdentity_Type()
)
f3PtpDynamicRemoteSlavePortIdentity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpDynamicRemoteSlavePortIdentity.setStatus("current")
_F3PtpDynamicRemoteSlavePeerMacAddress_Type = MacAddress
_F3PtpDynamicRemoteSlavePeerMacAddress_Object = MibTableColumn
f3PtpDynamicRemoteSlavePeerMacAddress = _F3PtpDynamicRemoteSlavePeerMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 1, 16, 1, 21),
    _F3PtpDynamicRemoteSlavePeerMacAddress_Type()
)
f3PtpDynamicRemoteSlavePeerMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpDynamicRemoteSlavePeerMacAddress.setStatus("current")
_F3PtpDynamicRemoteSlaveIpV6Address_Type = Ipv6Address
_F3PtpDynamicRemoteSlaveIpV6Address_Object = MibTableColumn
f3PtpDynamicRemoteSlaveIpV6Address = _F3PtpDynamicRemoteSlaveIpV6Address_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 1, 16, 1, 22),
    _F3PtpDynamicRemoteSlaveIpV6Address_Type()
)
f3PtpDynamicRemoteSlaveIpV6Address.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpDynamicRemoteSlaveIpV6Address.setStatus("current")
_F3PtpTrafficPortFlowPointTable_Object = MibTable
f3PtpTrafficPortFlowPointTable = _F3PtpTrafficPortFlowPointTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 1, 17)
)
if mibBuilder.loadTexts:
    f3PtpTrafficPortFlowPointTable.setStatus("current")
_F3PtpTrafficPortFlowPointEntry_Object = MibTableRow
f3PtpTrafficPortFlowPointEntry = _F3PtpTrafficPortFlowPointEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 1, 17, 1)
)
f3PtpTrafficPortFlowPointEntry.setIndexNames(
    (0, "CM-ENTITY-MIB", "neIndex"),
    (0, "CM-ENTITY-MIB", "shelfIndex"),
    (0, "CM-ENTITY-MIB", "slotIndex"),
    (0, "CM-FACILITY-MIB", "cmEthernetTrafficPortIndex"),
    (0, "F3-PTP-MIB", "f3PtpTrafficPortFlowPointIndex"),
)
if mibBuilder.loadTexts:
    f3PtpTrafficPortFlowPointEntry.setStatus("current")
_F3PtpTrafficPortFlowPointIndex_Type = Integer32
_F3PtpTrafficPortFlowPointIndex_Object = MibTableColumn
f3PtpTrafficPortFlowPointIndex = _F3PtpTrafficPortFlowPointIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 1, 17, 1, 1),
    _F3PtpTrafficPortFlowPointIndex_Type()
)
f3PtpTrafficPortFlowPointIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    f3PtpTrafficPortFlowPointIndex.setStatus("current")


class _F3PtpTrafficPortFlowPointAlias_Type(DisplayString):
    """Custom type f3PtpTrafficPortFlowPointAlias based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_F3PtpTrafficPortFlowPointAlias_Type.__name__ = "DisplayString"
_F3PtpTrafficPortFlowPointAlias_Object = MibTableColumn
f3PtpTrafficPortFlowPointAlias = _F3PtpTrafficPortFlowPointAlias_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 1, 17, 1, 2),
    _F3PtpTrafficPortFlowPointAlias_Type()
)
f3PtpTrafficPortFlowPointAlias.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3PtpTrafficPortFlowPointAlias.setStatus("current")
_F3PtpTrafficPortFlowPointAdminState_Type = AdminState
_F3PtpTrafficPortFlowPointAdminState_Object = MibTableColumn
f3PtpTrafficPortFlowPointAdminState = _F3PtpTrafficPortFlowPointAdminState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 1, 17, 1, 3),
    _F3PtpTrafficPortFlowPointAdminState_Type()
)
f3PtpTrafficPortFlowPointAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3PtpTrafficPortFlowPointAdminState.setStatus("current")
_F3PtpTrafficPortFlowPointOperationalState_Type = OperationalState
_F3PtpTrafficPortFlowPointOperationalState_Object = MibTableColumn
f3PtpTrafficPortFlowPointOperationalState = _F3PtpTrafficPortFlowPointOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 1, 17, 1, 4),
    _F3PtpTrafficPortFlowPointOperationalState_Type()
)
f3PtpTrafficPortFlowPointOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpTrafficPortFlowPointOperationalState.setStatus("current")
_F3PtpTrafficPortFlowPointSecondaryState_Type = SecondaryState
_F3PtpTrafficPortFlowPointSecondaryState_Object = MibTableColumn
f3PtpTrafficPortFlowPointSecondaryState = _F3PtpTrafficPortFlowPointSecondaryState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 1, 17, 1, 5),
    _F3PtpTrafficPortFlowPointSecondaryState_Type()
)
f3PtpTrafficPortFlowPointSecondaryState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpTrafficPortFlowPointSecondaryState.setStatus("current")
_F3PtpTrafficPortFlowPointType_Type = PtpFlowPointType
_F3PtpTrafficPortFlowPointType_Object = MibTableColumn
f3PtpTrafficPortFlowPointType = _F3PtpTrafficPortFlowPointType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 1, 17, 1, 6),
    _F3PtpTrafficPortFlowPointType_Type()
)
f3PtpTrafficPortFlowPointType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3PtpTrafficPortFlowPointType.setStatus("current")
_F3PtpTrafficPortFlowPointClock_Type = VariablePointer
_F3PtpTrafficPortFlowPointClock_Object = MibTableColumn
f3PtpTrafficPortFlowPointClock = _F3PtpTrafficPortFlowPointClock_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 1, 17, 1, 7),
    _F3PtpTrafficPortFlowPointClock_Type()
)
f3PtpTrafficPortFlowPointClock.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpTrafficPortFlowPointClock.setStatus("current")
_F3PtpTrafficPortFlowPointService_Type = VariablePointer
_F3PtpTrafficPortFlowPointService_Object = MibTableColumn
f3PtpTrafficPortFlowPointService = _F3PtpTrafficPortFlowPointService_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 1, 17, 1, 8),
    _F3PtpTrafficPortFlowPointService_Type()
)
f3PtpTrafficPortFlowPointService.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3PtpTrafficPortFlowPointService.setStatus("current")
_F3PtpTrafficPortFlowPointOuterVlanEtherType_Type = Integer32
_F3PtpTrafficPortFlowPointOuterVlanEtherType_Object = MibTableColumn
f3PtpTrafficPortFlowPointOuterVlanEtherType = _F3PtpTrafficPortFlowPointOuterVlanEtherType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 1, 17, 1, 9),
    _F3PtpTrafficPortFlowPointOuterVlanEtherType_Type()
)
f3PtpTrafficPortFlowPointOuterVlanEtherType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3PtpTrafficPortFlowPointOuterVlanEtherType.setStatus("current")
_F3PtpTrafficPortFlowPointOuterVlanMemberList_Type = DisplayString
_F3PtpTrafficPortFlowPointOuterVlanMemberList_Object = MibTableColumn
f3PtpTrafficPortFlowPointOuterVlanMemberList = _F3PtpTrafficPortFlowPointOuterVlanMemberList_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 1, 17, 1, 10),
    _F3PtpTrafficPortFlowPointOuterVlanMemberList_Type()
)
f3PtpTrafficPortFlowPointOuterVlanMemberList.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3PtpTrafficPortFlowPointOuterVlanMemberList.setStatus("current")
_F3PtpTrafficPortFlowPointOuterUntaggedEnabled_Type = TruthValue
_F3PtpTrafficPortFlowPointOuterUntaggedEnabled_Object = MibTableColumn
f3PtpTrafficPortFlowPointOuterUntaggedEnabled = _F3PtpTrafficPortFlowPointOuterUntaggedEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 1, 17, 1, 11),
    _F3PtpTrafficPortFlowPointOuterUntaggedEnabled_Type()
)
f3PtpTrafficPortFlowPointOuterUntaggedEnabled.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3PtpTrafficPortFlowPointOuterUntaggedEnabled.setStatus("current")
_F3PtpTrafficPortFlowPointInner1VlanEtherType_Type = Integer32
_F3PtpTrafficPortFlowPointInner1VlanEtherType_Object = MibTableColumn
f3PtpTrafficPortFlowPointInner1VlanEtherType = _F3PtpTrafficPortFlowPointInner1VlanEtherType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 1, 17, 1, 12),
    _F3PtpTrafficPortFlowPointInner1VlanEtherType_Type()
)
f3PtpTrafficPortFlowPointInner1VlanEtherType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3PtpTrafficPortFlowPointInner1VlanEtherType.setStatus("current")
_F3PtpTrafficPortFlowPointInner1VlanMemberList_Type = DisplayString
_F3PtpTrafficPortFlowPointInner1VlanMemberList_Object = MibTableColumn
f3PtpTrafficPortFlowPointInner1VlanMemberList = _F3PtpTrafficPortFlowPointInner1VlanMemberList_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 1, 17, 1, 13),
    _F3PtpTrafficPortFlowPointInner1VlanMemberList_Type()
)
f3PtpTrafficPortFlowPointInner1VlanMemberList.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3PtpTrafficPortFlowPointInner1VlanMemberList.setStatus("current")
_F3PtpTrafficPortFlowPointInner1UntaggedEnabled_Type = TruthValue
_F3PtpTrafficPortFlowPointInner1UntaggedEnabled_Object = MibTableColumn
f3PtpTrafficPortFlowPointInner1UntaggedEnabled = _F3PtpTrafficPortFlowPointInner1UntaggedEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 1, 17, 1, 14),
    _F3PtpTrafficPortFlowPointInner1UntaggedEnabled_Type()
)
f3PtpTrafficPortFlowPointInner1UntaggedEnabled.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3PtpTrafficPortFlowPointInner1UntaggedEnabled.setStatus("current")
_F3PtpTrafficPortFlowPointInner2VlanEtherType_Type = Integer32
_F3PtpTrafficPortFlowPointInner2VlanEtherType_Object = MibTableColumn
f3PtpTrafficPortFlowPointInner2VlanEtherType = _F3PtpTrafficPortFlowPointInner2VlanEtherType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 1, 17, 1, 15),
    _F3PtpTrafficPortFlowPointInner2VlanEtherType_Type()
)
f3PtpTrafficPortFlowPointInner2VlanEtherType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3PtpTrafficPortFlowPointInner2VlanEtherType.setStatus("current")
_F3PtpTrafficPortFlowPointInner2VlanMemberList_Type = DisplayString
_F3PtpTrafficPortFlowPointInner2VlanMemberList_Object = MibTableColumn
f3PtpTrafficPortFlowPointInner2VlanMemberList = _F3PtpTrafficPortFlowPointInner2VlanMemberList_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 1, 17, 1, 16),
    _F3PtpTrafficPortFlowPointInner2VlanMemberList_Type()
)
f3PtpTrafficPortFlowPointInner2VlanMemberList.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3PtpTrafficPortFlowPointInner2VlanMemberList.setStatus("current")
_F3PtpTrafficPortFlowPointInner2UntaggedEnabled_Type = TruthValue
_F3PtpTrafficPortFlowPointInner2UntaggedEnabled_Object = MibTableColumn
f3PtpTrafficPortFlowPointInner2UntaggedEnabled = _F3PtpTrafficPortFlowPointInner2UntaggedEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 1, 17, 1, 17),
    _F3PtpTrafficPortFlowPointInner2UntaggedEnabled_Type()
)
f3PtpTrafficPortFlowPointInner2UntaggedEnabled.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3PtpTrafficPortFlowPointInner2UntaggedEnabled.setStatus("current")
_F3PtpTrafficPortFlowPointStorageType_Type = StorageType
_F3PtpTrafficPortFlowPointStorageType_Object = MibTableColumn
f3PtpTrafficPortFlowPointStorageType = _F3PtpTrafficPortFlowPointStorageType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 1, 17, 1, 18),
    _F3PtpTrafficPortFlowPointStorageType_Type()
)
f3PtpTrafficPortFlowPointStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3PtpTrafficPortFlowPointStorageType.setStatus("current")
_F3PtpTrafficPortFlowPointRowStatus_Type = RowStatus
_F3PtpTrafficPortFlowPointRowStatus_Object = MibTableColumn
f3PtpTrafficPortFlowPointRowStatus = _F3PtpTrafficPortFlowPointRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 1, 17, 1, 19),
    _F3PtpTrafficPortFlowPointRowStatus_Type()
)
f3PtpTrafficPortFlowPointRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3PtpTrafficPortFlowPointRowStatus.setStatus("current")


class _F3PtpTrafficPortFlowPointCOS_Type(Integer32):
    """Custom type f3PtpTrafficPortFlowPointCOS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_F3PtpTrafficPortFlowPointCOS_Type.__name__ = "Integer32"
_F3PtpTrafficPortFlowPointCOS_Object = MibTableColumn
f3PtpTrafficPortFlowPointCOS = _F3PtpTrafficPortFlowPointCOS_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 1, 17, 1, 20),
    _F3PtpTrafficPortFlowPointCOS_Type()
)
f3PtpTrafficPortFlowPointCOS.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3PtpTrafficPortFlowPointCOS.setStatus("current")
_F3PtpTrafficPortFlowPointCIRLo_Type = Unsigned32
_F3PtpTrafficPortFlowPointCIRLo_Object = MibTableColumn
f3PtpTrafficPortFlowPointCIRLo = _F3PtpTrafficPortFlowPointCIRLo_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 1, 17, 1, 21),
    _F3PtpTrafficPortFlowPointCIRLo_Type()
)
f3PtpTrafficPortFlowPointCIRLo.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3PtpTrafficPortFlowPointCIRLo.setStatus("current")
_F3PtpTrafficPortFlowPointCIRHi_Type = Unsigned32
_F3PtpTrafficPortFlowPointCIRHi_Object = MibTableColumn
f3PtpTrafficPortFlowPointCIRHi = _F3PtpTrafficPortFlowPointCIRHi_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 1, 17, 1, 22),
    _F3PtpTrafficPortFlowPointCIRHi_Type()
)
f3PtpTrafficPortFlowPointCIRHi.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3PtpTrafficPortFlowPointCIRHi.setStatus("current")
_F3PtpTrafficPortFlowPointEIRLo_Type = Unsigned32
_F3PtpTrafficPortFlowPointEIRLo_Object = MibTableColumn
f3PtpTrafficPortFlowPointEIRLo = _F3PtpTrafficPortFlowPointEIRLo_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 1, 17, 1, 23),
    _F3PtpTrafficPortFlowPointEIRLo_Type()
)
f3PtpTrafficPortFlowPointEIRLo.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3PtpTrafficPortFlowPointEIRLo.setStatus("current")
_F3PtpTrafficPortFlowPointEIRHi_Type = Unsigned32
_F3PtpTrafficPortFlowPointEIRHi_Object = MibTableColumn
f3PtpTrafficPortFlowPointEIRHi = _F3PtpTrafficPortFlowPointEIRHi_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 1, 17, 1, 24),
    _F3PtpTrafficPortFlowPointEIRHi_Type()
)
f3PtpTrafficPortFlowPointEIRHi.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3PtpTrafficPortFlowPointEIRHi.setStatus("current")
_F3PtpTrafficPortFlowPointAssociatedQueueProfile_Type = VariablePointer
_F3PtpTrafficPortFlowPointAssociatedQueueProfile_Object = MibTableColumn
f3PtpTrafficPortFlowPointAssociatedQueueProfile = _F3PtpTrafficPortFlowPointAssociatedQueueProfile_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 1, 17, 1, 25),
    _F3PtpTrafficPortFlowPointAssociatedQueueProfile_Type()
)
f3PtpTrafficPortFlowPointAssociatedQueueProfile.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3PtpTrafficPortFlowPointAssociatedQueueProfile.setStatus("current")
_F3PtpTrafficPortFlowPointLoopAvoidance_Type = VariablePointer
_F3PtpTrafficPortFlowPointLoopAvoidance_Object = MibTableColumn
f3PtpTrafficPortFlowPointLoopAvoidance = _F3PtpTrafficPortFlowPointLoopAvoidance_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 1, 17, 1, 26),
    _F3PtpTrafficPortFlowPointLoopAvoidance_Type()
)
f3PtpTrafficPortFlowPointLoopAvoidance.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3PtpTrafficPortFlowPointLoopAvoidance.setStatus("current")
_F3PtpEthernetTrafficPortExtTable_Object = MibTable
f3PtpEthernetTrafficPortExtTable = _F3PtpEthernetTrafficPortExtTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 1, 18)
)
if mibBuilder.loadTexts:
    f3PtpEthernetTrafficPortExtTable.setStatus("current")
_F3PtpEthernetTrafficPortExtEntry_Object = MibTableRow
f3PtpEthernetTrafficPortExtEntry = _F3PtpEthernetTrafficPortExtEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 1, 18, 1)
)
if mibBuilder.loadTexts:
    f3PtpEthernetTrafficPortExtEntry.setStatus("current")
_F3PtpEthernetTrafficPortDelayAsymmetry_Type = Integer32
_F3PtpEthernetTrafficPortDelayAsymmetry_Object = MibTableColumn
f3PtpEthernetTrafficPortDelayAsymmetry = _F3PtpEthernetTrafficPortDelayAsymmetry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 1, 18, 1, 1),
    _F3PtpEthernetTrafficPortDelayAsymmetry_Type()
)
f3PtpEthernetTrafficPortDelayAsymmetry.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3PtpEthernetTrafficPortDelayAsymmetry.setStatus("current")
_F3PtpPTPClockTable_Object = MibTable
f3PtpPTPClockTable = _F3PtpPTPClockTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 1, 19)
)
if mibBuilder.loadTexts:
    f3PtpPTPClockTable.setStatus("current")
_F3PtpPTPClockEntry_Object = MibTableRow
f3PtpPTPClockEntry = _F3PtpPTPClockEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 1, 19, 1)
)
f3PtpPTPClockEntry.setIndexNames(
    (0, "CM-ENTITY-MIB", "neIndex"),
    (0, "F3-PTP-MIB", "f3PtpPTPClockIndex"),
)
if mibBuilder.loadTexts:
    f3PtpPTPClockEntry.setStatus("current")
_F3PtpPTPClockIndex_Type = Integer32
_F3PtpPTPClockIndex_Object = MibTableColumn
f3PtpPTPClockIndex = _F3PtpPTPClockIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 1, 19, 1, 1),
    _F3PtpPTPClockIndex_Type()
)
f3PtpPTPClockIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    f3PtpPTPClockIndex.setStatus("current")
_F3PtpPTPClockAdminState_Type = AdminState
_F3PtpPTPClockAdminState_Object = MibTableColumn
f3PtpPTPClockAdminState = _F3PtpPTPClockAdminState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 1, 19, 1, 2),
    _F3PtpPTPClockAdminState_Type()
)
f3PtpPTPClockAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3PtpPTPClockAdminState.setStatus("current")


class _F3PtpPTPClockAlias_Type(DisplayString):
    """Custom type f3PtpPTPClockAlias based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_F3PtpPTPClockAlias_Type.__name__ = "DisplayString"
_F3PtpPTPClockAlias_Object = MibTableColumn
f3PtpPTPClockAlias = _F3PtpPTPClockAlias_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 1, 19, 1, 3),
    _F3PtpPTPClockAlias_Type()
)
f3PtpPTPClockAlias.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3PtpPTPClockAlias.setStatus("current")
_F3PtpPTPClockOperationalState_Type = OperationalState
_F3PtpPTPClockOperationalState_Object = MibTableColumn
f3PtpPTPClockOperationalState = _F3PtpPTPClockOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 1, 19, 1, 4),
    _F3PtpPTPClockOperationalState_Type()
)
f3PtpPTPClockOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpPTPClockOperationalState.setStatus("current")
_F3PtpPTPClockSecondaryState_Type = SecondaryState
_F3PtpPTPClockSecondaryState_Object = MibTableColumn
f3PtpPTPClockSecondaryState = _F3PtpPTPClockSecondaryState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 1, 19, 1, 5),
    _F3PtpPTPClockSecondaryState_Type()
)
f3PtpPTPClockSecondaryState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpPTPClockSecondaryState.setStatus("current")
_F3PtpPTPClockProfile_Type = PTPClockProfile
_F3PtpPTPClockProfile_Object = MibTableColumn
f3PtpPTPClockProfile = _F3PtpPTPClockProfile_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 1, 19, 1, 6),
    _F3PtpPTPClockProfile_Type()
)
f3PtpPTPClockProfile.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3PtpPTPClockProfile.setStatus("current")
_F3PtpPTPClockClockType_Type = PTPClockType
_F3PtpPTPClockClockType_Object = MibTableColumn
f3PtpPTPClockClockType = _F3PtpPTPClockClockType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 1, 19, 1, 7),
    _F3PtpPTPClockClockType_Type()
)
f3PtpPTPClockClockType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3PtpPTPClockClockType.setStatus("current")
_F3PtpPTPClockOperationalMode_Type = PTPClockOperMode
_F3PtpPTPClockOperationalMode_Object = MibTableColumn
f3PtpPTPClockOperationalMode = _F3PtpPTPClockOperationalMode_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 1, 19, 1, 8),
    _F3PtpPTPClockOperationalMode_Type()
)
f3PtpPTPClockOperationalMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpPTPClockOperationalMode.setStatus("current")
_F3PtpPTPClockClockIdentity_Type = ClockIdentity
_F3PtpPTPClockClockIdentity_Object = MibTableColumn
f3PtpPTPClockClockIdentity = _F3PtpPTPClockClockIdentity_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 1, 19, 1, 9),
    _F3PtpPTPClockClockIdentity_Type()
)
f3PtpPTPClockClockIdentity.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3PtpPTPClockClockIdentity.setStatus("current")
_F3PtpPTPClockDomainNumber_Type = Integer32
_F3PtpPTPClockDomainNumber_Object = MibTableColumn
f3PtpPTPClockDomainNumber = _F3PtpPTPClockDomainNumber_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 1, 19, 1, 10),
    _F3PtpPTPClockDomainNumber_Type()
)
f3PtpPTPClockDomainNumber.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3PtpPTPClockDomainNumber.setStatus("current")
_F3PtpPTPClockTimeSource_Type = VariablePointer
_F3PtpPTPClockTimeSource_Object = MibTableColumn
f3PtpPTPClockTimeSource = _F3PtpPTPClockTimeSource_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 1, 19, 1, 11),
    _F3PtpPTPClockTimeSource_Type()
)
f3PtpPTPClockTimeSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpPTPClockTimeSource.setStatus("current")


class _F3PtpPTPClockPriority1_Type(Unsigned32):
    """Custom type f3PtpPTPClockPriority1 based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_F3PtpPTPClockPriority1_Type.__name__ = "Unsigned32"
_F3PtpPTPClockPriority1_Object = MibTableColumn
f3PtpPTPClockPriority1 = _F3PtpPTPClockPriority1_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 1, 19, 1, 12),
    _F3PtpPTPClockPriority1_Type()
)
f3PtpPTPClockPriority1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3PtpPTPClockPriority1.setStatus("current")


class _F3PtpPTPClockPriority2_Type(Unsigned32):
    """Custom type f3PtpPTPClockPriority2 based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_F3PtpPTPClockPriority2_Type.__name__ = "Unsigned32"
_F3PtpPTPClockPriority2_Object = MibTableColumn
f3PtpPTPClockPriority2 = _F3PtpPTPClockPriority2_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 1, 19, 1, 13),
    _F3PtpPTPClockPriority2_Type()
)
f3PtpPTPClockPriority2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3PtpPTPClockPriority2.setStatus("current")


class _F3PtpPTPClockLocalPriority_Type(Unsigned32):
    """Custom type f3PtpPTPClockLocalPriority based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_F3PtpPTPClockLocalPriority_Type.__name__ = "Unsigned32"
_F3PtpPTPClockLocalPriority_Object = MibTableColumn
f3PtpPTPClockLocalPriority = _F3PtpPTPClockLocalPriority_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 1, 19, 1, 14),
    _F3PtpPTPClockLocalPriority_Type()
)
f3PtpPTPClockLocalPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3PtpPTPClockLocalPriority.setStatus("current")
_F3PtpPTPClockClockAccuracy_Type = Unsigned32
_F3PtpPTPClockClockAccuracy_Object = MibTableColumn
f3PtpPTPClockClockAccuracy = _F3PtpPTPClockClockAccuracy_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 1, 19, 1, 15),
    _F3PtpPTPClockClockAccuracy_Type()
)
f3PtpPTPClockClockAccuracy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpPTPClockClockAccuracy.setStatus("obsolete")
_F3PtpPTPClockScaledLogVariance_Type = Integer32
_F3PtpPTPClockScaledLogVariance_Object = MibTableColumn
f3PtpPTPClockScaledLogVariance = _F3PtpPTPClockScaledLogVariance_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 1, 19, 1, 16),
    _F3PtpPTPClockScaledLogVariance_Type()
)
f3PtpPTPClockScaledLogVariance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpPTPClockScaledLogVariance.setStatus("current")
_F3PtpPTPClockSyncEid_Type = VariablePointer
_F3PtpPTPClockSyncEid_Object = MibTableColumn
f3PtpPTPClockSyncEid = _F3PtpPTPClockSyncEid_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 1, 19, 1, 17),
    _F3PtpPTPClockSyncEid_Type()
)
f3PtpPTPClockSyncEid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3PtpPTPClockSyncEid.setStatus("current")
_F3PtpPTPClockCurrentTimeOfDay_Type = DateAndTime
_F3PtpPTPClockCurrentTimeOfDay_Object = MibTableColumn
f3PtpPTPClockCurrentTimeOfDay = _F3PtpPTPClockCurrentTimeOfDay_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 1, 19, 1, 18),
    _F3PtpPTPClockCurrentTimeOfDay_Type()
)
f3PtpPTPClockCurrentTimeOfDay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpPTPClockCurrentTimeOfDay.setStatus("current")
_F3PtpPTPClockActiveSlavePort_Type = VariablePointer
_F3PtpPTPClockActiveSlavePort_Object = MibTableColumn
f3PtpPTPClockActiveSlavePort = _F3PtpPTPClockActiveSlavePort_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 1, 19, 1, 19),
    _F3PtpPTPClockActiveSlavePort_Type()
)
f3PtpPTPClockActiveSlavePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpPTPClockActiveSlavePort.setStatus("current")
_F3PtpPTPClockClockRecoveryState_Type = ClockRecoveryState
_F3PtpPTPClockClockRecoveryState_Object = MibTableColumn
f3PtpPTPClockClockRecoveryState = _F3PtpPTPClockClockRecoveryState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 1, 19, 1, 20),
    _F3PtpPTPClockClockRecoveryState_Type()
)
f3PtpPTPClockClockRecoveryState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpPTPClockClockRecoveryState.setStatus("current")
_F3PtpPTPClockPhaseRecoveryState_Type = PhaseRecoveryState
_F3PtpPTPClockPhaseRecoveryState_Object = MibTableColumn
f3PtpPTPClockPhaseRecoveryState = _F3PtpPTPClockPhaseRecoveryState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 1, 19, 1, 21),
    _F3PtpPTPClockPhaseRecoveryState_Type()
)
f3PtpPTPClockPhaseRecoveryState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpPTPClockPhaseRecoveryState.setStatus("current")
_F3PtpPTPClockTimeTraceabilityStatus_Type = TruthValue
_F3PtpPTPClockTimeTraceabilityStatus_Object = MibTableColumn
f3PtpPTPClockTimeTraceabilityStatus = _F3PtpPTPClockTimeTraceabilityStatus_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 1, 19, 1, 22),
    _F3PtpPTPClockTimeTraceabilityStatus_Type()
)
f3PtpPTPClockTimeTraceabilityStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpPTPClockTimeTraceabilityStatus.setStatus("current")
_F3PtpPTPClockTimeSinceTimeTraceabilityChanged_Type = Unsigned32
_F3PtpPTPClockTimeSinceTimeTraceabilityChanged_Object = MibTableColumn
f3PtpPTPClockTimeSinceTimeTraceabilityChanged = _F3PtpPTPClockTimeSinceTimeTraceabilityChanged_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 1, 19, 1, 23),
    _F3PtpPTPClockTimeSinceTimeTraceabilityChanged_Type()
)
f3PtpPTPClockTimeSinceTimeTraceabilityChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpPTPClockTimeSinceTimeTraceabilityChanged.setStatus("current")
_F3PtpPTPClockFreqTraceabilityStatus_Type = TruthValue
_F3PtpPTPClockFreqTraceabilityStatus_Object = MibTableColumn
f3PtpPTPClockFreqTraceabilityStatus = _F3PtpPTPClockFreqTraceabilityStatus_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 1, 19, 1, 24),
    _F3PtpPTPClockFreqTraceabilityStatus_Type()
)
f3PtpPTPClockFreqTraceabilityStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpPTPClockFreqTraceabilityStatus.setStatus("current")
_F3PtpPTPClockTimeSinceFreqTraceabilityChanged_Type = Unsigned32
_F3PtpPTPClockTimeSinceFreqTraceabilityChanged_Object = MibTableColumn
f3PtpPTPClockTimeSinceFreqTraceabilityChanged = _F3PtpPTPClockTimeSinceFreqTraceabilityChanged_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 1, 19, 1, 25),
    _F3PtpPTPClockTimeSinceFreqTraceabilityChanged_Type()
)
f3PtpPTPClockTimeSinceFreqTraceabilityChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpPTPClockTimeSinceFreqTraceabilityChanged.setStatus("current")
_F3PtpPTPClockClockSyncEEnabled_Type = TruthValue
_F3PtpPTPClockClockSyncEEnabled_Object = MibTableColumn
f3PtpPTPClockClockSyncEEnabled = _F3PtpPTPClockClockSyncEEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 1, 19, 1, 26),
    _F3PtpPTPClockClockSyncEEnabled_Type()
)
f3PtpPTPClockClockSyncEEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3PtpPTPClockClockSyncEEnabled.setStatus("current")
_F3PtpPTPClockClockQLModeEnabled_Type = TruthValue
_F3PtpPTPClockClockQLModeEnabled_Object = MibTableColumn
f3PtpPTPClockClockQLModeEnabled = _F3PtpPTPClockClockQLModeEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 1, 19, 1, 27),
    _F3PtpPTPClockClockQLModeEnabled_Type()
)
f3PtpPTPClockClockQLModeEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3PtpPTPClockClockQLModeEnabled.setStatus("current")
_F3PtpPTPClockClockExpectedQL_Type = SSMQualityLevel
_F3PtpPTPClockClockExpectedQL_Object = MibTableColumn
f3PtpPTPClockClockExpectedQL = _F3PtpPTPClockClockExpectedQL_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 1, 19, 1, 28),
    _F3PtpPTPClockClockExpectedQL_Type()
)
f3PtpPTPClockClockExpectedQL.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3PtpPTPClockClockExpectedQL.setStatus("current")
_F3PtpPTPClockClockAssumedQL_Type = SSMQualityLevel
_F3PtpPTPClockClockAssumedQL_Object = MibTableColumn
f3PtpPTPClockClockAssumedQL = _F3PtpPTPClockClockAssumedQL_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 1, 19, 1, 29),
    _F3PtpPTPClockClockAssumedQL_Type()
)
f3PtpPTPClockClockAssumedQL.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3PtpPTPClockClockAssumedQL.setStatus("current")
_F3PtpPTPClockClockReceivedQL_Type = SSMQualityLevel
_F3PtpPTPClockClockReceivedQL_Object = MibTableColumn
f3PtpPTPClockClockReceivedQL = _F3PtpPTPClockClockReceivedQL_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 1, 19, 1, 30),
    _F3PtpPTPClockClockReceivedQL_Type()
)
f3PtpPTPClockClockReceivedQL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpPTPClockClockReceivedQL.setStatus("current")
_F3PtpPTPClockStorageType_Type = StorageType
_F3PtpPTPClockStorageType_Object = MibTableColumn
f3PtpPTPClockStorageType = _F3PtpPTPClockStorageType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 1, 19, 1, 31),
    _F3PtpPTPClockStorageType_Type()
)
f3PtpPTPClockStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3PtpPTPClockStorageType.setStatus("current")
_F3PtpPTPClockRowStatus_Type = RowStatus
_F3PtpPTPClockRowStatus_Object = MibTableColumn
f3PtpPTPClockRowStatus = _F3PtpPTPClockRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 1, 19, 1, 32),
    _F3PtpPTPClockRowStatus_Type()
)
f3PtpPTPClockRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3PtpPTPClockRowStatus.setStatus("current")
_F3PtpPTPClockCurrentOffsetFromMaster_Type = PerfCounter64
_F3PtpPTPClockCurrentOffsetFromMaster_Object = MibTableColumn
f3PtpPTPClockCurrentOffsetFromMaster = _F3PtpPTPClockCurrentOffsetFromMaster_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 1, 19, 1, 33),
    _F3PtpPTPClockCurrentOffsetFromMaster_Type()
)
f3PtpPTPClockCurrentOffsetFromMaster.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpPTPClockCurrentOffsetFromMaster.setStatus("current")
_F3PtpPTPClockRecentMeanPathDelay_Type = PerfCounter64
_F3PtpPTPClockRecentMeanPathDelay_Object = MibTableColumn
f3PtpPTPClockRecentMeanPathDelay = _F3PtpPTPClockRecentMeanPathDelay_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 1, 19, 1, 34),
    _F3PtpPTPClockRecentMeanPathDelay_Type()
)
f3PtpPTPClockRecentMeanPathDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpPTPClockRecentMeanPathDelay.setStatus("current")
_F3PtpPTPClockRecentSyncPDV_Type = PerfCounter64
_F3PtpPTPClockRecentSyncPDV_Object = MibTableColumn
f3PtpPTPClockRecentSyncPDV = _F3PtpPTPClockRecentSyncPDV_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 1, 19, 1, 35),
    _F3PtpPTPClockRecentSyncPDV_Type()
)
f3PtpPTPClockRecentSyncPDV.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpPTPClockRecentSyncPDV.setStatus("current")
_F3PtpPTPClockClockClass_Type = Unsigned32
_F3PtpPTPClockClockClass_Object = MibTableColumn
f3PtpPTPClockClockClass = _F3PtpPTPClockClockClass_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 1, 19, 1, 36),
    _F3PtpPTPClockClockClass_Type()
)
f3PtpPTPClockClockClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpPTPClockClockClass.setStatus("current")
_F3PtpPTPClockPhysicalEntityIndex_Type = Integer32
_F3PtpPTPClockPhysicalEntityIndex_Object = MibTableColumn
f3PtpPTPClockPhysicalEntityIndex = _F3PtpPTPClockPhysicalEntityIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 1, 19, 1, 37),
    _F3PtpPTPClockPhysicalEntityIndex_Type()
)
f3PtpPTPClockPhysicalEntityIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpPTPClockPhysicalEntityIndex.setStatus("current")
_F3PtpPTPClockActiveGrantsAnnounceService_Type = Integer32
_F3PtpPTPClockActiveGrantsAnnounceService_Object = MibTableColumn
f3PtpPTPClockActiveGrantsAnnounceService = _F3PtpPTPClockActiveGrantsAnnounceService_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 1, 19, 1, 38),
    _F3PtpPTPClockActiveGrantsAnnounceService_Type()
)
f3PtpPTPClockActiveGrantsAnnounceService.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpPTPClockActiveGrantsAnnounceService.setStatus("current")
_F3PtpPTPClockActiveGrantsSyncService_Type = Integer32
_F3PtpPTPClockActiveGrantsSyncService_Object = MibTableColumn
f3PtpPTPClockActiveGrantsSyncService = _F3PtpPTPClockActiveGrantsSyncService_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 1, 19, 1, 39),
    _F3PtpPTPClockActiveGrantsSyncService_Type()
)
f3PtpPTPClockActiveGrantsSyncService.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpPTPClockActiveGrantsSyncService.setStatus("current")
_F3PtpPTPClockActiveGrantsDelayRequestService_Type = Integer32
_F3PtpPTPClockActiveGrantsDelayRequestService_Object = MibTableColumn
f3PtpPTPClockActiveGrantsDelayRequestService = _F3PtpPTPClockActiveGrantsDelayRequestService_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 1, 19, 1, 40),
    _F3PtpPTPClockActiveGrantsDelayRequestService_Type()
)
f3PtpPTPClockActiveGrantsDelayRequestService.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpPTPClockActiveGrantsDelayRequestService.setStatus("current")
_F3PtpPTPClockMaxStepRemoved_Type = Integer32
_F3PtpPTPClockMaxStepRemoved_Object = MibTableColumn
f3PtpPTPClockMaxStepRemoved = _F3PtpPTPClockMaxStepRemoved_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 1, 19, 1, 41),
    _F3PtpPTPClockMaxStepRemoved_Type()
)
f3PtpPTPClockMaxStepRemoved.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3PtpPTPClockMaxStepRemoved.setStatus("current")
_F3PtpPTPClockServiceAvailableTime_Type = Unsigned32
_F3PtpPTPClockServiceAvailableTime_Object = MibTableColumn
f3PtpPTPClockServiceAvailableTime = _F3PtpPTPClockServiceAvailableTime_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 1, 19, 1, 42),
    _F3PtpPTPClockServiceAvailableTime_Type()
)
f3PtpPTPClockServiceAvailableTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpPTPClockServiceAvailableTime.setStatus("current")
_F3PtpPTPClockServiceUnavailableTime_Type = Unsigned32
_F3PtpPTPClockServiceUnavailableTime_Object = MibTableColumn
f3PtpPTPClockServiceUnavailableTime = _F3PtpPTPClockServiceUnavailableTime_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 1, 19, 1, 43),
    _F3PtpPTPClockServiceUnavailableTime_Type()
)
f3PtpPTPClockServiceUnavailableTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpPTPClockServiceUnavailableTime.setStatus("current")
_F3PtpPTPClockServiceAvailablePercentage_Type = DisplayString
_F3PtpPTPClockServiceAvailablePercentage_Object = MibTableColumn
f3PtpPTPClockServiceAvailablePercentage = _F3PtpPTPClockServiceAvailablePercentage_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 1, 19, 1, 44),
    _F3PtpPTPClockServiceAvailablePercentage_Type()
)
f3PtpPTPClockServiceAvailablePercentage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpPTPClockServiceAvailablePercentage.setStatus("current")


class _F3PtpPTPClockGrandMasterID_Type(Integer32):
    """Custom type f3PtpPTPClockGrandMasterID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_F3PtpPTPClockGrandMasterID_Type.__name__ = "Integer32"
_F3PtpPTPClockGrandMasterID_Object = MibTableColumn
f3PtpPTPClockGrandMasterID = _F3PtpPTPClockGrandMasterID_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 1, 19, 1, 45),
    _F3PtpPTPClockGrandMasterID_Type()
)
f3PtpPTPClockGrandMasterID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3PtpPTPClockGrandMasterID.setStatus("current")
_F3PtpPTPClockTimeInaccuracy_Type = Unsigned32
_F3PtpPTPClockTimeInaccuracy_Object = MibTableColumn
f3PtpPTPClockTimeInaccuracy = _F3PtpPTPClockTimeInaccuracy_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 1, 19, 1, 46),
    _F3PtpPTPClockTimeInaccuracy_Type()
)
f3PtpPTPClockTimeInaccuracy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3PtpPTPClockTimeInaccuracy.setStatus("current")
_F3PtpPTPClockNetworkTimeInaccuracy_Type = Unsigned32
_F3PtpPTPClockNetworkTimeInaccuracy_Object = MibTableColumn
f3PtpPTPClockNetworkTimeInaccuracy = _F3PtpPTPClockNetworkTimeInaccuracy_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 1, 19, 1, 47),
    _F3PtpPTPClockNetworkTimeInaccuracy_Type()
)
f3PtpPTPClockNetworkTimeInaccuracy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3PtpPTPClockNetworkTimeInaccuracy.setStatus("current")
_F3PtpPTPPortTable_Object = MibTable
f3PtpPTPPortTable = _F3PtpPTPPortTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 1, 20)
)
if mibBuilder.loadTexts:
    f3PtpPTPPortTable.setStatus("current")
_F3PtpPTPPortEntry_Object = MibTableRow
f3PtpPTPPortEntry = _F3PtpPTPPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 1, 20, 1)
)
f3PtpPTPPortEntry.setIndexNames(
    (0, "CM-ENTITY-MIB", "neIndex"),
    (0, "F3-PTP-MIB", "f3PtpPTPClockIndex"),
    (0, "F3-PTP-MIB", "f3PtpPTPPortIndex"),
)
if mibBuilder.loadTexts:
    f3PtpPTPPortEntry.setStatus("current")
_F3PtpPTPPortIndex_Type = Integer32
_F3PtpPTPPortIndex_Object = MibTableColumn
f3PtpPTPPortIndex = _F3PtpPTPPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 1, 20, 1, 1),
    _F3PtpPTPPortIndex_Type()
)
f3PtpPTPPortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    f3PtpPTPPortIndex.setStatus("current")
_F3PtpPTPPortAdminState_Type = AdminState
_F3PtpPTPPortAdminState_Object = MibTableColumn
f3PtpPTPPortAdminState = _F3PtpPTPPortAdminState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 1, 20, 1, 2),
    _F3PtpPTPPortAdminState_Type()
)
f3PtpPTPPortAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3PtpPTPPortAdminState.setStatus("current")


class _F3PtpPTPPortAlias_Type(DisplayString):
    """Custom type f3PtpPTPPortAlias based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_F3PtpPTPPortAlias_Type.__name__ = "DisplayString"
_F3PtpPTPPortAlias_Object = MibTableColumn
f3PtpPTPPortAlias = _F3PtpPTPPortAlias_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 1, 20, 1, 3),
    _F3PtpPTPPortAlias_Type()
)
f3PtpPTPPortAlias.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3PtpPTPPortAlias.setStatus("current")
_F3PtpPTPPortOperationalState_Type = OperationalState
_F3PtpPTPPortOperationalState_Object = MibTableColumn
f3PtpPTPPortOperationalState = _F3PtpPTPPortOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 1, 20, 1, 4),
    _F3PtpPTPPortOperationalState_Type()
)
f3PtpPTPPortOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpPTPPortOperationalState.setStatus("current")
_F3PtpPTPPortSecondaryState_Type = SecondaryState
_F3PtpPTPPortSecondaryState_Object = MibTableColumn
f3PtpPTPPortSecondaryState = _F3PtpPTPPortSecondaryState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 1, 20, 1, 5),
    _F3PtpPTPPortSecondaryState_Type()
)
f3PtpPTPPortSecondaryState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpPTPPortSecondaryState.setStatus("current")
_F3PtpPTPPortPeerPortIdentity_Type = PortIdentity
_F3PtpPTPPortPeerPortIdentity_Object = MibTableColumn
f3PtpPTPPortPeerPortIdentity = _F3PtpPTPPortPeerPortIdentity_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 1, 20, 1, 6),
    _F3PtpPTPPortPeerPortIdentity_Type()
)
f3PtpPTPPortPeerPortIdentity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpPTPPortPeerPortIdentity.setStatus("current")


class _F3PtpPTPPortLocalPriority_Type(Unsigned32):
    """Custom type f3PtpPTPPortLocalPriority based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_F3PtpPTPPortLocalPriority_Type.__name__ = "Unsigned32"
_F3PtpPTPPortLocalPriority_Object = MibTableColumn
f3PtpPTPPortLocalPriority = _F3PtpPTPPortLocalPriority_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 1, 20, 1, 7),
    _F3PtpPTPPortLocalPriority_Type()
)
f3PtpPTPPortLocalPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3PtpPTPPortLocalPriority.setStatus("current")
_F3PtpPTPPortPtpFlowPointEid_Type = VariablePointer
_F3PtpPTPPortPtpFlowPointEid_Object = MibTableColumn
f3PtpPTPPortPtpFlowPointEid = _F3PtpPTPPortPtpFlowPointEid_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 1, 20, 1, 8),
    _F3PtpPTPPortPtpFlowPointEid_Type()
)
f3PtpPTPPortPtpFlowPointEid.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3PtpPTPPortPtpFlowPointEid.setStatus("current")
_F3PtpPTPPortNotSlave_Type = TruthValue
_F3PtpPTPPortNotSlave_Object = MibTableColumn
f3PtpPTPPortNotSlave = _F3PtpPTPPortNotSlave_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 1, 20, 1, 9),
    _F3PtpPTPPortNotSlave_Type()
)
f3PtpPTPPortNotSlave.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3PtpPTPPortNotSlave.setStatus("deprecated")
_F3PtpPTPPortTxDestMacAddress_Type = DestMacAddrType
_F3PtpPTPPortTxDestMacAddress_Object = MibTableColumn
f3PtpPTPPortTxDestMacAddress = _F3PtpPTPPortTxDestMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 1, 20, 1, 10),
    _F3PtpPTPPortTxDestMacAddress_Type()
)
f3PtpPTPPortTxDestMacAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3PtpPTPPortTxDestMacAddress.setStatus("current")
_F3PtpPTPPortSyncMessageRate_Type = SyncMessageRate
_F3PtpPTPPortSyncMessageRate_Object = MibTableColumn
f3PtpPTPPortSyncMessageRate = _F3PtpPTPPortSyncMessageRate_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 1, 20, 1, 11),
    _F3PtpPTPPortSyncMessageRate_Type()
)
f3PtpPTPPortSyncMessageRate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3PtpPTPPortSyncMessageRate.setStatus("current")
_F3PtpPTPPortmDelayReqRespMsgRate_Type = DelayReqMessageRate
_F3PtpPTPPortmDelayReqRespMsgRate_Object = MibTableColumn
f3PtpPTPPortmDelayReqRespMsgRate = _F3PtpPTPPortmDelayReqRespMsgRate_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 1, 20, 1, 12),
    _F3PtpPTPPortmDelayReqRespMsgRate_Type()
)
f3PtpPTPPortmDelayReqRespMsgRate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3PtpPTPPortmDelayReqRespMsgRate.setStatus("current")
_F3PtpPTPPortmAnnounceMsgRate_Type = AnnounceMessageRate
_F3PtpPTPPortmAnnounceMsgRate_Object = MibTableColumn
f3PtpPTPPortmAnnounceMsgRate = _F3PtpPTPPortmAnnounceMsgRate_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 1, 20, 1, 13),
    _F3PtpPTPPortmAnnounceMsgRate_Type()
)
f3PtpPTPPortmAnnounceMsgRate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3PtpPTPPortmAnnounceMsgRate.setStatus("current")
_F3PtpPTPPortAnnounceReceiptTimeout_Type = Integer32
_F3PtpPTPPortAnnounceReceiptTimeout_Object = MibTableColumn
f3PtpPTPPortAnnounceReceiptTimeout = _F3PtpPTPPortAnnounceReceiptTimeout_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 1, 20, 1, 14),
    _F3PtpPTPPortAnnounceReceiptTimeout_Type()
)
f3PtpPTPPortAnnounceReceiptTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3PtpPTPPortAnnounceReceiptTimeout.setStatus("current")
_F3PtpPTPPortSyncReceiptTimeout_Type = Integer32
_F3PtpPTPPortSyncReceiptTimeout_Object = MibTableColumn
f3PtpPTPPortSyncReceiptTimeout = _F3PtpPTPPortSyncReceiptTimeout_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 1, 20, 1, 15),
    _F3PtpPTPPortSyncReceiptTimeout_Type()
)
f3PtpPTPPortSyncReceiptTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3PtpPTPPortSyncReceiptTimeout.setStatus("current")
_F3PtpPTPPortDelayRespTimeout_Type = Integer32
_F3PtpPTPPortDelayRespTimeout_Object = MibTableColumn
f3PtpPTPPortDelayRespTimeout = _F3PtpPTPPortDelayRespTimeout_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 1, 20, 1, 16),
    _F3PtpPTPPortDelayRespTimeout_Type()
)
f3PtpPTPPortDelayRespTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3PtpPTPPortDelayRespTimeout.setStatus("current")
_F3PtpPTPPortPortState_Type = PtpPortState
_F3PtpPTPPortPortState_Object = MibTableColumn
f3PtpPTPPortPortState = _F3PtpPTPPortPortState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 1, 20, 1, 17),
    _F3PtpPTPPortPortState_Type()
)
f3PtpPTPPortPortState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpPTPPortPortState.setStatus("current")
_F3PtpPTPPortBmcaDecisionCode_Type = BMCARole
_F3PtpPTPPortBmcaDecisionCode_Object = MibTableColumn
f3PtpPTPPortBmcaDecisionCode = _F3PtpPTPPortBmcaDecisionCode_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 1, 20, 1, 18),
    _F3PtpPTPPortBmcaDecisionCode_Type()
)
f3PtpPTPPortBmcaDecisionCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpPTPPortBmcaDecisionCode.setStatus("current")
_F3PtpPTPPortClockClass_Type = Unsigned32
_F3PtpPTPPortClockClass_Object = MibTableColumn
f3PtpPTPPortClockClass = _F3PtpPTPPortClockClass_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 1, 20, 1, 19),
    _F3PtpPTPPortClockClass_Type()
)
f3PtpPTPPortClockClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpPTPPortClockClass.setStatus("current")
_F3PtpPTPPortPeerPortMacAddress_Type = MacAddress
_F3PtpPTPPortPeerPortMacAddress_Object = MibTableColumn
f3PtpPTPPortPeerPortMacAddress = _F3PtpPTPPortPeerPortMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 1, 20, 1, 20),
    _F3PtpPTPPortPeerPortMacAddress_Type()
)
f3PtpPTPPortPeerPortMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpPTPPortPeerPortMacAddress.setStatus("current")
_F3PtpPTPPortRowStatus_Type = RowStatus
_F3PtpPTPPortRowStatus_Object = MibTableColumn
f3PtpPTPPortRowStatus = _F3PtpPTPPortRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 1, 20, 1, 21),
    _F3PtpPTPPortRowStatus_Type()
)
f3PtpPTPPortRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3PtpPTPPortRowStatus.setStatus("current")
_F3PtpPTPPortPortIdentity_Type = PortIdentity
_F3PtpPTPPortPortIdentity_Object = MibTableColumn
f3PtpPTPPortPortIdentity = _F3PtpPTPPortPortIdentity_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 1, 20, 1, 22),
    _F3PtpPTPPortPortIdentity_Type()
)
f3PtpPTPPortPortIdentity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpPTPPortPortIdentity.setStatus("current")
_F3PtpPTPPortMaxExpectedL2Slaves_Type = Unsigned32
_F3PtpPTPPortMaxExpectedL2Slaves_Object = MibTableColumn
f3PtpPTPPortMaxExpectedL2Slaves = _F3PtpPTPPortMaxExpectedL2Slaves_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 1, 20, 1, 23),
    _F3PtpPTPPortMaxExpectedL2Slaves_Type()
)
f3PtpPTPPortMaxExpectedL2Slaves.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3PtpPTPPortMaxExpectedL2Slaves.setStatus("current")
_F3PtpPTPPortMasterClockType_Type = MasterClockType
_F3PtpPTPPortMasterClockType_Object = MibTableColumn
f3PtpPTPPortMasterClockType = _F3PtpPTPPortMasterClockType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 1, 20, 1, 24),
    _F3PtpPTPPortMasterClockType_Type()
)
f3PtpPTPPortMasterClockType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3PtpPTPPortMasterClockType.setStatus("current")
_F3PtpPTPPortLastRcvdAnnounceMsg_Type = F3DisplayString
_F3PtpPTPPortLastRcvdAnnounceMsg_Object = MibTableColumn
f3PtpPTPPortLastRcvdAnnounceMsg = _F3PtpPTPPortLastRcvdAnnounceMsg_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 1, 20, 1, 25),
    _F3PtpPTPPortLastRcvdAnnounceMsg_Type()
)
f3PtpPTPPortLastRcvdAnnounceMsg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpPTPPortLastRcvdAnnounceMsg.setStatus("current")
_F3PtpPTPPortLastRcvdSyncMsg_Type = F3DisplayString
_F3PtpPTPPortLastRcvdSyncMsg_Object = MibTableColumn
f3PtpPTPPortLastRcvdSyncMsg = _F3PtpPTPPortLastRcvdSyncMsg_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 1, 20, 1, 26),
    _F3PtpPTPPortLastRcvdSyncMsg_Type()
)
f3PtpPTPPortLastRcvdSyncMsg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpPTPPortLastRcvdSyncMsg.setStatus("current")
_F3PtpPTPPortLastRcvdDelayReqMsg_Type = F3DisplayString
_F3PtpPTPPortLastRcvdDelayReqMsg_Object = MibTableColumn
f3PtpPTPPortLastRcvdDelayReqMsg = _F3PtpPTPPortLastRcvdDelayReqMsg_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 1, 20, 1, 27),
    _F3PtpPTPPortLastRcvdDelayReqMsg_Type()
)
f3PtpPTPPortLastRcvdDelayReqMsg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpPTPPortLastRcvdDelayReqMsg.setStatus("current")
_F3PtpPTPPortLastRcvdDelayRspMsg_Type = F3DisplayString
_F3PtpPTPPortLastRcvdDelayRspMsg_Object = MibTableColumn
f3PtpPTPPortLastRcvdDelayRspMsg = _F3PtpPTPPortLastRcvdDelayRspMsg_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 1, 20, 1, 28),
    _F3PtpPTPPortLastRcvdDelayRspMsg_Type()
)
f3PtpPTPPortLastRcvdDelayRspMsg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpPTPPortLastRcvdDelayRspMsg.setStatus("current")
_F3PtpPTPPortMasterOnly_Type = TruthValue
_F3PtpPTPPortMasterOnly_Object = MibTableColumn
f3PtpPTPPortMasterOnly = _F3PtpPTPPortMasterOnly_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 1, 20, 1, 29),
    _F3PtpPTPPortMasterOnly_Type()
)
f3PtpPTPPortMasterOnly.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3PtpPTPPortMasterOnly.setStatus("current")
_F3PtpPTPPortIsProbingSlave_Type = TruthValue
_F3PtpPTPPortIsProbingSlave_Object = MibTableColumn
f3PtpPTPPortIsProbingSlave = _F3PtpPTPPortIsProbingSlave_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 1, 20, 1, 30),
    _F3PtpPTPPortIsProbingSlave_Type()
)
f3PtpPTPPortIsProbingSlave.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3PtpPTPPortIsProbingSlave.setStatus("current")
_F3PtpPTPPortPeerClockClass_Type = Unsigned32
_F3PtpPTPPortPeerClockClass_Object = MibTableColumn
f3PtpPTPPortPeerClockClass = _F3PtpPTPPortPeerClockClass_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 1, 20, 1, 31),
    _F3PtpPTPPortPeerClockClass_Type()
)
f3PtpPTPPortPeerClockClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpPTPPortPeerClockClass.setStatus("current")


class _F3PtpPTPPortMinimumExpectedClockClass_Type(Integer32):
    """Custom type f3PtpPTPPortMinimumExpectedClockClass based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_F3PtpPTPPortMinimumExpectedClockClass_Type.__name__ = "Integer32"
_F3PtpPTPPortMinimumExpectedClockClass_Object = MibTableColumn
f3PtpPTPPortMinimumExpectedClockClass = _F3PtpPTPPortMinimumExpectedClockClass_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 1, 20, 1, 32),
    _F3PtpPTPPortMinimumExpectedClockClass_Type()
)
f3PtpPTPPortMinimumExpectedClockClass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3PtpPTPPortMinimumExpectedClockClass.setStatus("current")
_F3PtpPTPPortDelayAsymmetryComp_Type = CompensationMode
_F3PtpPTPPortDelayAsymmetryComp_Object = MibTableColumn
f3PtpPTPPortDelayAsymmetryComp = _F3PtpPTPPortDelayAsymmetryComp_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 1, 20, 1, 33),
    _F3PtpPTPPortDelayAsymmetryComp_Type()
)
f3PtpPTPPortDelayAsymmetryComp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3PtpPTPPortDelayAsymmetryComp.setStatus("current")
_F3PtpPTPPortAutoAsymmetryCompStatus_Type = CompensationStatus
_F3PtpPTPPortAutoAsymmetryCompStatus_Object = MibTableColumn
f3PtpPTPPortAutoAsymmetryCompStatus = _F3PtpPTPPortAutoAsymmetryCompStatus_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 1, 20, 1, 34),
    _F3PtpPTPPortAutoAsymmetryCompStatus_Type()
)
f3PtpPTPPortAutoAsymmetryCompStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpPTPPortAutoAsymmetryCompStatus.setStatus("current")
_F3PtpPTPPortDelayAsymmetry_Type = Integer32
_F3PtpPTPPortDelayAsymmetry_Object = MibTableColumn
f3PtpPTPPortDelayAsymmetry = _F3PtpPTPPortDelayAsymmetry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 1, 20, 1, 35),
    _F3PtpPTPPortDelayAsymmetry_Type()
)
f3PtpPTPPortDelayAsymmetry.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3PtpPTPPortDelayAsymmetry.setStatus("current")
_F3PtpPTPPortVirtualPortCtrl_Type = ToggleValue
_F3PtpPTPPortVirtualPortCtrl_Object = MibTableColumn
f3PtpPTPPortVirtualPortCtrl = _F3PtpPTPPortVirtualPortCtrl_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 1, 20, 1, 36),
    _F3PtpPTPPortVirtualPortCtrl_Type()
)
f3PtpPTPPortVirtualPortCtrl.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3PtpPTPPortVirtualPortCtrl.setStatus("current")
_F3PtpPTPPortDelayResponderType_Type = MasterClockType
_F3PtpPTPPortDelayResponderType_Object = MibTableColumn
f3PtpPTPPortDelayResponderType = _F3PtpPTPPortDelayResponderType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 1, 20, 1, 37),
    _F3PtpPTPPortDelayResponderType_Type()
)
f3PtpPTPPortDelayResponderType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3PtpPTPPortDelayResponderType.setStatus("current")
_F3PtpPTPPortTimeTraceable_Type = TruthValue
_F3PtpPTPPortTimeTraceable_Object = MibTableColumn
f3PtpPTPPortTimeTraceable = _F3PtpPTPPortTimeTraceable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 1, 20, 1, 38),
    _F3PtpPTPPortTimeTraceable_Type()
)
f3PtpPTPPortTimeTraceable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpPTPPortTimeTraceable.setStatus("current")
_F3PtpPTPPortFrequencyTraceable_Type = TruthValue
_F3PtpPTPPortFrequencyTraceable_Object = MibTableColumn
f3PtpPTPPortFrequencyTraceable = _F3PtpPTPPortFrequencyTraceable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 1, 20, 1, 39),
    _F3PtpPTPPortFrequencyTraceable_Type()
)
f3PtpPTPPortFrequencyTraceable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpPTPPortFrequencyTraceable.setStatus("current")
_F3PtpL2DynamicRemoteSlaveTable_Object = MibTable
f3PtpL2DynamicRemoteSlaveTable = _F3PtpL2DynamicRemoteSlaveTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 1, 21)
)
if mibBuilder.loadTexts:
    f3PtpL2DynamicRemoteSlaveTable.setStatus("current")
_F3PtpL2DynamicRemoteSlaveEntry_Object = MibTableRow
f3PtpL2DynamicRemoteSlaveEntry = _F3PtpL2DynamicRemoteSlaveEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 1, 21, 1)
)
f3PtpL2DynamicRemoteSlaveEntry.setIndexNames(
    (0, "CM-ENTITY-MIB", "neIndex"),
    (0, "F3-PTP-MIB", "f3PtpPTPClockIndex"),
    (0, "F3-PTP-MIB", "f3PtpPTPPortIndex"),
    (0, "F3-PTP-MIB", "f3PtpL2DynamicRemoteSlaveIndex"),
)
if mibBuilder.loadTexts:
    f3PtpL2DynamicRemoteSlaveEntry.setStatus("current")
_F3PtpL2DynamicRemoteSlaveIndex_Type = Integer32
_F3PtpL2DynamicRemoteSlaveIndex_Object = MibTableColumn
f3PtpL2DynamicRemoteSlaveIndex = _F3PtpL2DynamicRemoteSlaveIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 1, 21, 1, 1),
    _F3PtpL2DynamicRemoteSlaveIndex_Type()
)
f3PtpL2DynamicRemoteSlaveIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    f3PtpL2DynamicRemoteSlaveIndex.setStatus("current")
_F3PtpL2DynamicRemoteSlavePortIdentity_Type = PortIdentity
_F3PtpL2DynamicRemoteSlavePortIdentity_Object = MibTableColumn
f3PtpL2DynamicRemoteSlavePortIdentity = _F3PtpL2DynamicRemoteSlavePortIdentity_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 1, 21, 1, 2),
    _F3PtpL2DynamicRemoteSlavePortIdentity_Type()
)
f3PtpL2DynamicRemoteSlavePortIdentity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpL2DynamicRemoteSlavePortIdentity.setStatus("current")
_F3PtpL2DynamicRemoteSlaveMacAddress_Type = MacAddress
_F3PtpL2DynamicRemoteSlaveMacAddress_Object = MibTableColumn
f3PtpL2DynamicRemoteSlaveMacAddress = _F3PtpL2DynamicRemoteSlaveMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 1, 21, 1, 3),
    _F3PtpL2DynamicRemoteSlaveMacAddress_Type()
)
f3PtpL2DynamicRemoteSlaveMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpL2DynamicRemoteSlaveMacAddress.setStatus("current")
_F3PtpL2DynamicRemoteSlaveRowStatus_Type = RowStatus
_F3PtpL2DynamicRemoteSlaveRowStatus_Object = MibTableColumn
f3PtpL2DynamicRemoteSlaveRowStatus = _F3PtpL2DynamicRemoteSlaveRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 1, 21, 1, 4),
    _F3PtpL2DynamicRemoteSlaveRowStatus_Type()
)
f3PtpL2DynamicRemoteSlaveRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3PtpL2DynamicRemoteSlaveRowStatus.setStatus("current")
_F3PtpL2DynamicRemoteSlaveStorageType_Type = StorageType
_F3PtpL2DynamicRemoteSlaveStorageType_Object = MibTableColumn
f3PtpL2DynamicRemoteSlaveStorageType = _F3PtpL2DynamicRemoteSlaveStorageType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 1, 21, 1, 5),
    _F3PtpL2DynamicRemoteSlaveStorageType_Type()
)
f3PtpL2DynamicRemoteSlaveStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3PtpL2DynamicRemoteSlaveStorageType.setStatus("current")
_F3PtpL2DynamicRemoteSlaveClockIdentity_Type = ClockIdentity
_F3PtpL2DynamicRemoteSlaveClockIdentity_Object = MibTableColumn
f3PtpL2DynamicRemoteSlaveClockIdentity = _F3PtpL2DynamicRemoteSlaveClockIdentity_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 1, 21, 1, 6),
    _F3PtpL2DynamicRemoteSlaveClockIdentity_Type()
)
f3PtpL2DynamicRemoteSlaveClockIdentity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpL2DynamicRemoteSlaveClockIdentity.setStatus("current")
_F3PtpMCIProtGroupTable_Object = MibTable
f3PtpMCIProtGroupTable = _F3PtpMCIProtGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 1, 22)
)
if mibBuilder.loadTexts:
    f3PtpMCIProtGroupTable.setStatus("current")
_F3PtpMCIProtGroupEntry_Object = MibTableRow
f3PtpMCIProtGroupEntry = _F3PtpMCIProtGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 1, 22, 1)
)
f3PtpMCIProtGroupEntry.setIndexNames(
    (0, "CM-ENTITY-MIB", "neIndex"),
    (0, "F3-PTP-MIB", "f3PtpMCIProtGroupIndex"),
)
if mibBuilder.loadTexts:
    f3PtpMCIProtGroupEntry.setStatus("current")
_F3PtpMCIProtGroupIndex_Type = Integer32
_F3PtpMCIProtGroupIndex_Object = MibTableColumn
f3PtpMCIProtGroupIndex = _F3PtpMCIProtGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 1, 22, 1, 1),
    _F3PtpMCIProtGroupIndex_Type()
)
f3PtpMCIProtGroupIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpMCIProtGroupIndex.setStatus("current")
_F3PtpMCIProtGroupAdminState_Type = AdminState
_F3PtpMCIProtGroupAdminState_Object = MibTableColumn
f3PtpMCIProtGroupAdminState = _F3PtpMCIProtGroupAdminState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 1, 22, 1, 2),
    _F3PtpMCIProtGroupAdminState_Type()
)
f3PtpMCIProtGroupAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3PtpMCIProtGroupAdminState.setStatus("current")
_F3PtpMCIProtGroupActiveMember_Type = VariablePointer
_F3PtpMCIProtGroupActiveMember_Object = MibTableColumn
f3PtpMCIProtGroupActiveMember = _F3PtpMCIProtGroupActiveMember_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 1, 22, 1, 3),
    _F3PtpMCIProtGroupActiveMember_Type()
)
f3PtpMCIProtGroupActiveMember.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpMCIProtGroupActiveMember.setStatus("current")
_F3PtpMCIProtGroupLastSwitchOverTime_Type = TimeTicks
_F3PtpMCIProtGroupLastSwitchOverTime_Object = MibTableColumn
f3PtpMCIProtGroupLastSwitchOverTime = _F3PtpMCIProtGroupLastSwitchOverTime_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 1, 22, 1, 4),
    _F3PtpMCIProtGroupLastSwitchOverTime_Type()
)
f3PtpMCIProtGroupLastSwitchOverTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpMCIProtGroupLastSwitchOverTime.setStatus("current")
_F3PtpMCIProtGroupLastSwitchOverReason_Type = CmGenPgSwitchoverReason
_F3PtpMCIProtGroupLastSwitchOverReason_Object = MibTableColumn
f3PtpMCIProtGroupLastSwitchOverReason = _F3PtpMCIProtGroupLastSwitchOverReason_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 1, 22, 1, 5),
    _F3PtpMCIProtGroupLastSwitchOverReason_Type()
)
f3PtpMCIProtGroupLastSwitchOverReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpMCIProtGroupLastSwitchOverReason.setStatus("current")
_F3PtpMCIProtGroupStorageType_Type = StorageType
_F3PtpMCIProtGroupStorageType_Object = MibTableColumn
f3PtpMCIProtGroupStorageType = _F3PtpMCIProtGroupStorageType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 1, 22, 1, 6),
    _F3PtpMCIProtGroupStorageType_Type()
)
f3PtpMCIProtGroupStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3PtpMCIProtGroupStorageType.setStatus("current")
_F3PtpMCIProtGroupRowStatus_Type = RowStatus
_F3PtpMCIProtGroupRowStatus_Object = MibTableColumn
f3PtpMCIProtGroupRowStatus = _F3PtpMCIProtGroupRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 1, 22, 1, 7),
    _F3PtpMCIProtGroupRowStatus_Type()
)
f3PtpMCIProtGroupRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3PtpMCIProtGroupRowStatus.setStatus("current")
_F3PtpMCIProtMemberTable_Object = MibTable
f3PtpMCIProtMemberTable = _F3PtpMCIProtMemberTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 1, 23)
)
if mibBuilder.loadTexts:
    f3PtpMCIProtMemberTable.setStatus("current")
_F3PtpMCIProtMemberEntry_Object = MibTableRow
f3PtpMCIProtMemberEntry = _F3PtpMCIProtMemberEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 1, 23, 1)
)
f3PtpMCIProtMemberEntry.setIndexNames(
    (0, "CM-ENTITY-MIB", "neIndex"),
    (0, "F3-PTP-MIB", "f3PtpMCIProtGroupIndex"),
    (0, "F3-PTP-MIB", "f3PtpMCIProtMemberObject"),
)
if mibBuilder.loadTexts:
    f3PtpMCIProtMemberEntry.setStatus("current")
_F3PtpMCIProtMemberObject_Type = VariablePointer
_F3PtpMCIProtMemberObject_Object = MibTableColumn
f3PtpMCIProtMemberObject = _F3PtpMCIProtMemberObject_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 1, 23, 1, 1),
    _F3PtpMCIProtMemberObject_Type()
)
f3PtpMCIProtMemberObject.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    f3PtpMCIProtMemberObject.setStatus("current")
_F3PtpMCIProtMemberStorageType_Type = StorageType
_F3PtpMCIProtMemberStorageType_Object = MibTableColumn
f3PtpMCIProtMemberStorageType = _F3PtpMCIProtMemberStorageType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 1, 23, 1, 2),
    _F3PtpMCIProtMemberStorageType_Type()
)
f3PtpMCIProtMemberStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3PtpMCIProtMemberStorageType.setStatus("current")
_F3PtpMCIProtMemberRowStatus_Type = RowStatus
_F3PtpMCIProtMemberRowStatus_Object = MibTableColumn
f3PtpMCIProtMemberRowStatus = _F3PtpMCIProtMemberRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 1, 23, 1, 3),
    _F3PtpMCIProtMemberRowStatus_Type()
)
f3PtpMCIProtMemberRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3PtpMCIProtMemberRowStatus.setStatus("current")
_F3PtpTrafficPortFlowPointExtTable_Object = MibTable
f3PtpTrafficPortFlowPointExtTable = _F3PtpTrafficPortFlowPointExtTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 1, 24)
)
if mibBuilder.loadTexts:
    f3PtpTrafficPortFlowPointExtTable.setStatus("current")
_F3PtpTrafficPortFlowPointExtEntry_Object = MibTableRow
f3PtpTrafficPortFlowPointExtEntry = _F3PtpTrafficPortFlowPointExtEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 1, 24, 1)
)
if mibBuilder.loadTexts:
    f3PtpTrafficPortFlowPointExtEntry.setStatus("current")
_F3PtpTrafficPortFlowPointBufferSize_Type = Integer32
_F3PtpTrafficPortFlowPointBufferSize_Object = MibTableColumn
f3PtpTrafficPortFlowPointBufferSize = _F3PtpTrafficPortFlowPointBufferSize_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 1, 24, 1, 1),
    _F3PtpTrafficPortFlowPointBufferSize_Type()
)
f3PtpTrafficPortFlowPointBufferSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3PtpTrafficPortFlowPointBufferSize.setStatus("current")
_F3PtpL3PTPPortTable_Object = MibTable
f3PtpL3PTPPortTable = _F3PtpL3PTPPortTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 1, 25)
)
if mibBuilder.loadTexts:
    f3PtpL3PTPPortTable.setStatus("current")
_F3PtpL3PTPPortEntry_Object = MibTableRow
f3PtpL3PTPPortEntry = _F3PtpL3PTPPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 1, 25, 1)
)
f3PtpL3PTPPortEntry.setIndexNames(
    (0, "CM-ENTITY-MIB", "neIndex"),
    (0, "F3-PTP-MIB", "f3PtpPTPClockIndex"),
    (0, "F3-PTP-MIB", "f3PtpL3PTPPortIndex"),
)
if mibBuilder.loadTexts:
    f3PtpL3PTPPortEntry.setStatus("current")
_F3PtpL3PTPPortIndex_Type = Integer32
_F3PtpL3PTPPortIndex_Object = MibTableColumn
f3PtpL3PTPPortIndex = _F3PtpL3PTPPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 1, 25, 1, 1),
    _F3PtpL3PTPPortIndex_Type()
)
f3PtpL3PTPPortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    f3PtpL3PTPPortIndex.setStatus("current")
_F3PtpL3PTPPortAdminState_Type = AdminState
_F3PtpL3PTPPortAdminState_Object = MibTableColumn
f3PtpL3PTPPortAdminState = _F3PtpL3PTPPortAdminState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 1, 25, 1, 2),
    _F3PtpL3PTPPortAdminState_Type()
)
f3PtpL3PTPPortAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3PtpL3PTPPortAdminState.setStatus("current")


class _F3PtpL3PTPPortAlias_Type(DisplayString):
    """Custom type f3PtpL3PTPPortAlias based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_F3PtpL3PTPPortAlias_Type.__name__ = "DisplayString"
_F3PtpL3PTPPortAlias_Object = MibTableColumn
f3PtpL3PTPPortAlias = _F3PtpL3PTPPortAlias_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 1, 25, 1, 3),
    _F3PtpL3PTPPortAlias_Type()
)
f3PtpL3PTPPortAlias.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3PtpL3PTPPortAlias.setStatus("current")
_F3PtpL3PTPPortOperationalState_Type = OperationalState
_F3PtpL3PTPPortOperationalState_Object = MibTableColumn
f3PtpL3PTPPortOperationalState = _F3PtpL3PTPPortOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 1, 25, 1, 4),
    _F3PtpL3PTPPortOperationalState_Type()
)
f3PtpL3PTPPortOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpL3PTPPortOperationalState.setStatus("current")
_F3PtpL3PTPPortSecondaryState_Type = SecondaryState
_F3PtpL3PTPPortSecondaryState_Object = MibTableColumn
f3PtpL3PTPPortSecondaryState = _F3PtpL3PTPPortSecondaryState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 1, 25, 1, 5),
    _F3PtpL3PTPPortSecondaryState_Type()
)
f3PtpL3PTPPortSecondaryState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpL3PTPPortSecondaryState.setStatus("current")
_F3PtpL3PTPPortPortIdentity_Type = PortIdentity
_F3PtpL3PTPPortPortIdentity_Object = MibTableColumn
f3PtpL3PTPPortPortIdentity = _F3PtpL3PTPPortPortIdentity_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 1, 25, 1, 6),
    _F3PtpL3PTPPortPortIdentity_Type()
)
f3PtpL3PTPPortPortIdentity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpL3PTPPortPortIdentity.setStatus("current")


class _F3PtpL3PTPPortLocalPriority_Type(Unsigned32):
    """Custom type f3PtpL3PTPPortLocalPriority based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_F3PtpL3PTPPortLocalPriority_Type.__name__ = "Unsigned32"
_F3PtpL3PTPPortLocalPriority_Object = MibTableColumn
f3PtpL3PTPPortLocalPriority = _F3PtpL3PTPPortLocalPriority_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 1, 25, 1, 7),
    _F3PtpL3PTPPortLocalPriority_Type()
)
f3PtpL3PTPPortLocalPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3PtpL3PTPPortLocalPriority.setStatus("current")
_F3PtpL3PTPPortPtpFlowPointEid_Type = VariablePointer
_F3PtpL3PTPPortPtpFlowPointEid_Object = MibTableColumn
f3PtpL3PTPPortPtpFlowPointEid = _F3PtpL3PTPPortPtpFlowPointEid_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 1, 25, 1, 8),
    _F3PtpL3PTPPortPtpFlowPointEid_Type()
)
f3PtpL3PTPPortPtpFlowPointEid.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3PtpL3PTPPortPtpFlowPointEid.setStatus("current")
_F3PtpL3PTPPortSyncMessageRate_Type = SyncMessageRate
_F3PtpL3PTPPortSyncMessageRate_Object = MibTableColumn
f3PtpL3PTPPortSyncMessageRate = _F3PtpL3PTPPortSyncMessageRate_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 1, 25, 1, 9),
    _F3PtpL3PTPPortSyncMessageRate_Type()
)
f3PtpL3PTPPortSyncMessageRate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3PtpL3PTPPortSyncMessageRate.setStatus("current")
_F3PtpL3PTPPortDelayReqRespMsgRate_Type = DelayReqMessageRate
_F3PtpL3PTPPortDelayReqRespMsgRate_Object = MibTableColumn
f3PtpL3PTPPortDelayReqRespMsgRate = _F3PtpL3PTPPortDelayReqRespMsgRate_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 1, 25, 1, 10),
    _F3PtpL3PTPPortDelayReqRespMsgRate_Type()
)
f3PtpL3PTPPortDelayReqRespMsgRate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3PtpL3PTPPortDelayReqRespMsgRate.setStatus("current")
_F3PtpL3PTPPortAnnounceMsgRate_Type = AnnounceMessageRate
_F3PtpL3PTPPortAnnounceMsgRate_Object = MibTableColumn
f3PtpL3PTPPortAnnounceMsgRate = _F3PtpL3PTPPortAnnounceMsgRate_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 1, 25, 1, 11),
    _F3PtpL3PTPPortAnnounceMsgRate_Type()
)
f3PtpL3PTPPortAnnounceMsgRate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3PtpL3PTPPortAnnounceMsgRate.setStatus("current")


class _F3PtpL3PTPPortAnnounceReceiptTimeout_Type(Integer32):
    """Custom type f3PtpL3PTPPortAnnounceReceiptTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 255),
    )


_F3PtpL3PTPPortAnnounceReceiptTimeout_Type.__name__ = "Integer32"
_F3PtpL3PTPPortAnnounceReceiptTimeout_Object = MibTableColumn
f3PtpL3PTPPortAnnounceReceiptTimeout = _F3PtpL3PTPPortAnnounceReceiptTimeout_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 1, 25, 1, 12),
    _F3PtpL3PTPPortAnnounceReceiptTimeout_Type()
)
f3PtpL3PTPPortAnnounceReceiptTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3PtpL3PTPPortAnnounceReceiptTimeout.setStatus("current")


class _F3PtpL3PTPPortSyncReceiptTimeout_Type(Integer32):
    """Custom type f3PtpL3PTPPortSyncReceiptTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 128),
    )


_F3PtpL3PTPPortSyncReceiptTimeout_Type.__name__ = "Integer32"
_F3PtpL3PTPPortSyncReceiptTimeout_Object = MibTableColumn
f3PtpL3PTPPortSyncReceiptTimeout = _F3PtpL3PTPPortSyncReceiptTimeout_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 1, 25, 1, 13),
    _F3PtpL3PTPPortSyncReceiptTimeout_Type()
)
f3PtpL3PTPPortSyncReceiptTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3PtpL3PTPPortSyncReceiptTimeout.setStatus("current")


class _F3PtpL3PTPPortDelayRespTimeout_Type(Integer32):
    """Custom type f3PtpL3PTPPortDelayRespTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 128),
    )


_F3PtpL3PTPPortDelayRespTimeout_Type.__name__ = "Integer32"
_F3PtpL3PTPPortDelayRespTimeout_Object = MibTableColumn
f3PtpL3PTPPortDelayRespTimeout = _F3PtpL3PTPPortDelayRespTimeout_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 1, 25, 1, 14),
    _F3PtpL3PTPPortDelayRespTimeout_Type()
)
f3PtpL3PTPPortDelayRespTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3PtpL3PTPPortDelayRespTimeout.setStatus("current")
_F3PtpL3PTPPortPortState_Type = PtpPortState
_F3PtpL3PTPPortPortState_Object = MibTableColumn
f3PtpL3PTPPortPortState = _F3PtpL3PTPPortPortState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 1, 25, 1, 15),
    _F3PtpL3PTPPortPortState_Type()
)
f3PtpL3PTPPortPortState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpL3PTPPortPortState.setStatus("current")
_F3PtpL3PTPPortBmcaDecisionCode_Type = BMCARole
_F3PtpL3PTPPortBmcaDecisionCode_Object = MibTableColumn
f3PtpL3PTPPortBmcaDecisionCode = _F3PtpL3PTPPortBmcaDecisionCode_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 1, 25, 1, 16),
    _F3PtpL3PTPPortBmcaDecisionCode_Type()
)
f3PtpL3PTPPortBmcaDecisionCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpL3PTPPortBmcaDecisionCode.setStatus("current")
_F3PtpL3PTPPortPeerClockClass_Type = Unsigned32
_F3PtpL3PTPPortPeerClockClass_Object = MibTableColumn
f3PtpL3PTPPortPeerClockClass = _F3PtpL3PTPPortPeerClockClass_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 1, 25, 1, 17),
    _F3PtpL3PTPPortPeerClockClass_Type()
)
f3PtpL3PTPPortPeerClockClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpL3PTPPortPeerClockClass.setStatus("current")


class _F3PtpL3PTPPortMinimumExpectedClockClass_Type(Integer32):
    """Custom type f3PtpL3PTPPortMinimumExpectedClockClass based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_F3PtpL3PTPPortMinimumExpectedClockClass_Type.__name__ = "Integer32"
_F3PtpL3PTPPortMinimumExpectedClockClass_Object = MibTableColumn
f3PtpL3PTPPortMinimumExpectedClockClass = _F3PtpL3PTPPortMinimumExpectedClockClass_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 1, 25, 1, 18),
    _F3PtpL3PTPPortMinimumExpectedClockClass_Type()
)
f3PtpL3PTPPortMinimumExpectedClockClass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3PtpL3PTPPortMinimumExpectedClockClass.setStatus("current")
_F3PtpL3PTPPortIpProtocol_Type = IpVersion
_F3PtpL3PTPPortIpProtocol_Object = MibTableColumn
f3PtpL3PTPPortIpProtocol = _F3PtpL3PTPPortIpProtocol_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 1, 25, 1, 19),
    _F3PtpL3PTPPortIpProtocol_Type()
)
f3PtpL3PTPPortIpProtocol.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3PtpL3PTPPortIpProtocol.setStatus("current")


class _F3PtpL3PTPPortIfName_Type(DisplayString):
    """Custom type f3PtpL3PTPPortIfName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 15),
    )


_F3PtpL3PTPPortIfName_Type.__name__ = "DisplayString"
_F3PtpL3PTPPortIfName_Object = MibTableColumn
f3PtpL3PTPPortIfName = _F3PtpL3PTPPortIfName_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 1, 25, 1, 20),
    _F3PtpL3PTPPortIfName_Type()
)
f3PtpL3PTPPortIfName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3PtpL3PTPPortIfName.setStatus("current")
_F3PtpL3PTPPortIpPriorityMapMode_Type = IpPriorityMapMode
_F3PtpL3PTPPortIpPriorityMapMode_Object = MibTableColumn
f3PtpL3PTPPortIpPriorityMapMode = _F3PtpL3PTPPortIpPriorityMapMode_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 1, 25, 1, 21),
    _F3PtpL3PTPPortIpPriorityMapMode_Type()
)
f3PtpL3PTPPortIpPriorityMapMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3PtpL3PTPPortIpPriorityMapMode.setStatus("current")


class _F3PtpL3PTPPortIpPriority_Type(Integer32):
    """Custom type f3PtpL3PTPPortIpPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_F3PtpL3PTPPortIpPriority_Type.__name__ = "Integer32"
_F3PtpL3PTPPortIpPriority_Object = MibTableColumn
f3PtpL3PTPPortIpPriority = _F3PtpL3PTPPortIpPriority_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 1, 25, 1, 22),
    _F3PtpL3PTPPortIpPriority_Type()
)
f3PtpL3PTPPortIpPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3PtpL3PTPPortIpPriority.setStatus("current")
_F3PtpL3PTPPortIpV4Address_Type = IpAddress
_F3PtpL3PTPPortIpV4Address_Object = MibTableColumn
f3PtpL3PTPPortIpV4Address = _F3PtpL3PTPPortIpV4Address_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 1, 25, 1, 23),
    _F3PtpL3PTPPortIpV4Address_Type()
)
f3PtpL3PTPPortIpV4Address.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3PtpL3PTPPortIpV4Address.setStatus("current")
_F3PtpL3PTPPortIpV4SubnetMask_Type = IpAddress
_F3PtpL3PTPPortIpV4SubnetMask_Object = MibTableColumn
f3PtpL3PTPPortIpV4SubnetMask = _F3PtpL3PTPPortIpV4SubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 1, 25, 1, 24),
    _F3PtpL3PTPPortIpV4SubnetMask_Type()
)
f3PtpL3PTPPortIpV4SubnetMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3PtpL3PTPPortIpV4SubnetMask.setStatus("current")
_F3PtpL3PTPPortIpV6Address_Type = Ipv6Address
_F3PtpL3PTPPortIpV6Address_Object = MibTableColumn
f3PtpL3PTPPortIpV6Address = _F3PtpL3PTPPortIpV6Address_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 1, 25, 1, 25),
    _F3PtpL3PTPPortIpV6Address_Type()
)
f3PtpL3PTPPortIpV6Address.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3PtpL3PTPPortIpV6Address.setStatus("current")
_F3PtpL3PTPPortIpV6AddrPrefixLength_Type = Integer32
_F3PtpL3PTPPortIpV6AddrPrefixLength_Object = MibTableColumn
f3PtpL3PTPPortIpV6AddrPrefixLength = _F3PtpL3PTPPortIpV6AddrPrefixLength_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 1, 25, 1, 26),
    _F3PtpL3PTPPortIpV6AddrPrefixLength_Type()
)
f3PtpL3PTPPortIpV6AddrPrefixLength.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3PtpL3PTPPortIpV6AddrPrefixLength.setStatus("current")
_F3PtpL3PTPPortDefaultGatewayControl_Type = ToggleValue
_F3PtpL3PTPPortDefaultGatewayControl_Object = MibTableColumn
f3PtpL3PTPPortDefaultGatewayControl = _F3PtpL3PTPPortDefaultGatewayControl_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 1, 25, 1, 27),
    _F3PtpL3PTPPortDefaultGatewayControl_Type()
)
f3PtpL3PTPPortDefaultGatewayControl.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3PtpL3PTPPortDefaultGatewayControl.setStatus("current")
_F3PtpL3PTPPortGateway_Type = IpAddress
_F3PtpL3PTPPortGateway_Object = MibTableColumn
f3PtpL3PTPPortGateway = _F3PtpL3PTPPortGateway_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 1, 25, 1, 28),
    _F3PtpL3PTPPortGateway_Type()
)
f3PtpL3PTPPortGateway.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3PtpL3PTPPortGateway.setStatus("current")
_F3PtpL3PTPPortIpV6Gateway_Type = Ipv6Address
_F3PtpL3PTPPortIpV6Gateway_Object = MibTableColumn
f3PtpL3PTPPortIpV6Gateway = _F3PtpL3PTPPortIpV6Gateway_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 1, 25, 1, 29),
    _F3PtpL3PTPPortIpV6Gateway_Type()
)
f3PtpL3PTPPortIpV6Gateway.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3PtpL3PTPPortIpV6Gateway.setStatus("current")
_F3PtpL3PTPPortUnicastMessageNegEnabled_Type = TruthValue
_F3PtpL3PTPPortUnicastMessageNegEnabled_Object = MibTableColumn
f3PtpL3PTPPortUnicastMessageNegEnabled = _F3PtpL3PTPPortUnicastMessageNegEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 1, 25, 1, 30),
    _F3PtpL3PTPPortUnicastMessageNegEnabled_Type()
)
f3PtpL3PTPPortUnicastMessageNegEnabled.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3PtpL3PTPPortUnicastMessageNegEnabled.setStatus("current")


class _F3PtpL3PTPPortTransmitDuration_Type(Integer32):
    """Custom type f3PtpL3PTPPortTransmitDuration based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(60, 1000),
    )


_F3PtpL3PTPPortTransmitDuration_Type.__name__ = "Integer32"
_F3PtpL3PTPPortTransmitDuration_Object = MibTableColumn
f3PtpL3PTPPortTransmitDuration = _F3PtpL3PTPPortTransmitDuration_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 1, 25, 1, 31),
    _F3PtpL3PTPPortTransmitDuration_Type()
)
f3PtpL3PTPPortTransmitDuration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3PtpL3PTPPortTransmitDuration.setStatus("current")


class _F3PtpL3PTPPortRequestUnicastTimeout_Type(Integer32):
    """Custom type f3PtpL3PTPPortRequestUnicastTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 600),
    )


_F3PtpL3PTPPortRequestUnicastTimeout_Type.__name__ = "Integer32"
_F3PtpL3PTPPortRequestUnicastTimeout_Object = MibTableColumn
f3PtpL3PTPPortRequestUnicastTimeout = _F3PtpL3PTPPortRequestUnicastTimeout_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 1, 25, 1, 32),
    _F3PtpL3PTPPortRequestUnicastTimeout_Type()
)
f3PtpL3PTPPortRequestUnicastTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3PtpL3PTPPortRequestUnicastTimeout.setStatus("current")


class _F3PtpL3PTPPortRequestUnicastRestartTimer_Type(Integer32):
    """Custom type f3PtpL3PTPPortRequestUnicastRestartTimer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(30, 1800),
    )


_F3PtpL3PTPPortRequestUnicastRestartTimer_Type.__name__ = "Integer32"
_F3PtpL3PTPPortRequestUnicastRestartTimer_Object = MibTableColumn
f3PtpL3PTPPortRequestUnicastRestartTimer = _F3PtpL3PTPPortRequestUnicastRestartTimer_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 1, 25, 1, 33),
    _F3PtpL3PTPPortRequestUnicastRestartTimer_Type()
)
f3PtpL3PTPPortRequestUnicastRestartTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3PtpL3PTPPortRequestUnicastRestartTimer.setStatus("current")
_F3PtpL3PTPPortMasterIpV4Address_Type = IpAddress
_F3PtpL3PTPPortMasterIpV4Address_Object = MibTableColumn
f3PtpL3PTPPortMasterIpV4Address = _F3PtpL3PTPPortMasterIpV4Address_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 1, 25, 1, 34),
    _F3PtpL3PTPPortMasterIpV4Address_Type()
)
f3PtpL3PTPPortMasterIpV4Address.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3PtpL3PTPPortMasterIpV4Address.setStatus("current")
_F3PtpL3PTPPortMasterIpV6Address_Type = Ipv6Address
_F3PtpL3PTPPortMasterIpV6Address_Object = MibTableColumn
f3PtpL3PTPPortMasterIpV6Address = _F3PtpL3PTPPortMasterIpV6Address_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 1, 25, 1, 35),
    _F3PtpL3PTPPortMasterIpV6Address_Type()
)
f3PtpL3PTPPortMasterIpV6Address.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3PtpL3PTPPortMasterIpV6Address.setStatus("current")
_F3PtpL3PTPPortDelayAsymmetryComp_Type = CompensationMode
_F3PtpL3PTPPortDelayAsymmetryComp_Object = MibTableColumn
f3PtpL3PTPPortDelayAsymmetryComp = _F3PtpL3PTPPortDelayAsymmetryComp_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 1, 25, 1, 36),
    _F3PtpL3PTPPortDelayAsymmetryComp_Type()
)
f3PtpL3PTPPortDelayAsymmetryComp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3PtpL3PTPPortDelayAsymmetryComp.setStatus("current")
_F3PtpL3PTPPortAutoAsymmetryCompStatus_Type = CompensationStatus
_F3PtpL3PTPPortAutoAsymmetryCompStatus_Object = MibTableColumn
f3PtpL3PTPPortAutoAsymmetryCompStatus = _F3PtpL3PTPPortAutoAsymmetryCompStatus_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 1, 25, 1, 37),
    _F3PtpL3PTPPortAutoAsymmetryCompStatus_Type()
)
f3PtpL3PTPPortAutoAsymmetryCompStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpL3PTPPortAutoAsymmetryCompStatus.setStatus("current")


class _F3PtpL3PTPPortDelayAsymmetry_Type(Integer32):
    """Custom type f3PtpL3PTPPortDelayAsymmetry based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-10000000, 10000000),
    )


_F3PtpL3PTPPortDelayAsymmetry_Type.__name__ = "Integer32"
_F3PtpL3PTPPortDelayAsymmetry_Object = MibTableColumn
f3PtpL3PTPPortDelayAsymmetry = _F3PtpL3PTPPortDelayAsymmetry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 1, 25, 1, 38),
    _F3PtpL3PTPPortDelayAsymmetry_Type()
)
f3PtpL3PTPPortDelayAsymmetry.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3PtpL3PTPPortDelayAsymmetry.setStatus("current")
_F3PtpL3PTPPortStorageType_Type = StorageType
_F3PtpL3PTPPortStorageType_Object = MibTableColumn
f3PtpL3PTPPortStorageType = _F3PtpL3PTPPortStorageType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 1, 25, 1, 39),
    _F3PtpL3PTPPortStorageType_Type()
)
f3PtpL3PTPPortStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3PtpL3PTPPortStorageType.setStatus("current")
_F3PtpL3PTPPortRowStatus_Type = RowStatus
_F3PtpL3PTPPortRowStatus_Object = MibTableColumn
f3PtpL3PTPPortRowStatus = _F3PtpL3PTPPortRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 1, 25, 1, 40),
    _F3PtpL3PTPPortRowStatus_Type()
)
f3PtpL3PTPPortRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3PtpL3PTPPortRowStatus.setStatus("current")
_F3PtpPerformanceObjects_ObjectIdentity = ObjectIdentity
f3PtpPerformanceObjects = _F3PtpPerformanceObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2)
)
_F3PtpAccPortFlowPointStatsTable_Object = MibTable
f3PtpAccPortFlowPointStatsTable = _F3PtpAccPortFlowPointStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 1)
)
if mibBuilder.loadTexts:
    f3PtpAccPortFlowPointStatsTable.setStatus("current")
_F3PtpAccPortFlowPointStatsEntry_Object = MibTableRow
f3PtpAccPortFlowPointStatsEntry = _F3PtpAccPortFlowPointStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 1, 1)
)
f3PtpAccPortFlowPointStatsEntry.setIndexNames(
    (0, "CM-ENTITY-MIB", "neIndex"),
    (0, "CM-ENTITY-MIB", "shelfIndex"),
    (0, "CM-ENTITY-MIB", "slotIndex"),
    (0, "CM-FACILITY-MIB", "cmEthernetAccPortIndex"),
    (0, "F3-PTP-MIB", "f3PtpAccPortFlowPointIndex"),
    (0, "F3-PTP-MIB", "f3PtpAccPortFlowPointStatsIndex"),
)
if mibBuilder.loadTexts:
    f3PtpAccPortFlowPointStatsEntry.setStatus("current")


class _F3PtpAccPortFlowPointStatsIndex_Type(Integer32):
    """Custom type f3PtpAccPortFlowPointStatsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_F3PtpAccPortFlowPointStatsIndex_Type.__name__ = "Integer32"
_F3PtpAccPortFlowPointStatsIndex_Object = MibTableColumn
f3PtpAccPortFlowPointStatsIndex = _F3PtpAccPortFlowPointStatsIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 1, 1, 1),
    _F3PtpAccPortFlowPointStatsIndex_Type()
)
f3PtpAccPortFlowPointStatsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    f3PtpAccPortFlowPointStatsIndex.setStatus("current")
_F3PtpAccPortFlowPointStatsIntervalType_Type = CmPmIntervalType
_F3PtpAccPortFlowPointStatsIntervalType_Object = MibTableColumn
f3PtpAccPortFlowPointStatsIntervalType = _F3PtpAccPortFlowPointStatsIntervalType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 1, 1, 2),
    _F3PtpAccPortFlowPointStatsIntervalType_Type()
)
f3PtpAccPortFlowPointStatsIntervalType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpAccPortFlowPointStatsIntervalType.setStatus("current")
_F3PtpAccPortFlowPointStatsValid_Type = TruthValue
_F3PtpAccPortFlowPointStatsValid_Object = MibTableColumn
f3PtpAccPortFlowPointStatsValid = _F3PtpAccPortFlowPointStatsValid_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 1, 1, 3),
    _F3PtpAccPortFlowPointStatsValid_Type()
)
f3PtpAccPortFlowPointStatsValid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpAccPortFlowPointStatsValid.setStatus("current")
_F3PtpAccPortFlowPointStatsAction_Type = CmPmBinAction
_F3PtpAccPortFlowPointStatsAction_Object = MibTableColumn
f3PtpAccPortFlowPointStatsAction = _F3PtpAccPortFlowPointStatsAction_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 1, 1, 4),
    _F3PtpAccPortFlowPointStatsAction_Type()
)
f3PtpAccPortFlowPointStatsAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3PtpAccPortFlowPointStatsAction.setStatus("current")
_F3PtpAccPortFlowPointStatsAnnouncesRx_Type = PerfCounter64
_F3PtpAccPortFlowPointStatsAnnouncesRx_Object = MibTableColumn
f3PtpAccPortFlowPointStatsAnnouncesRx = _F3PtpAccPortFlowPointStatsAnnouncesRx_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 1, 1, 5),
    _F3PtpAccPortFlowPointStatsAnnouncesRx_Type()
)
f3PtpAccPortFlowPointStatsAnnouncesRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpAccPortFlowPointStatsAnnouncesRx.setStatus("current")
_F3PtpAccPortFlowPointStatsAnnouncesTx_Type = PerfCounter64
_F3PtpAccPortFlowPointStatsAnnouncesTx_Object = MibTableColumn
f3PtpAccPortFlowPointStatsAnnouncesTx = _F3PtpAccPortFlowPointStatsAnnouncesTx_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 1, 1, 6),
    _F3PtpAccPortFlowPointStatsAnnouncesTx_Type()
)
f3PtpAccPortFlowPointStatsAnnouncesTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpAccPortFlowPointStatsAnnouncesTx.setStatus("current")
_F3PtpAccPortFlowPointStatsSyncsRx_Type = PerfCounter64
_F3PtpAccPortFlowPointStatsSyncsRx_Object = MibTableColumn
f3PtpAccPortFlowPointStatsSyncsRx = _F3PtpAccPortFlowPointStatsSyncsRx_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 1, 1, 7),
    _F3PtpAccPortFlowPointStatsSyncsRx_Type()
)
f3PtpAccPortFlowPointStatsSyncsRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpAccPortFlowPointStatsSyncsRx.setStatus("current")
_F3PtpAccPortFlowPointStatsSyncsTx_Type = PerfCounter64
_F3PtpAccPortFlowPointStatsSyncsTx_Object = MibTableColumn
f3PtpAccPortFlowPointStatsSyncsTx = _F3PtpAccPortFlowPointStatsSyncsTx_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 1, 1, 8),
    _F3PtpAccPortFlowPointStatsSyncsTx_Type()
)
f3PtpAccPortFlowPointStatsSyncsTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpAccPortFlowPointStatsSyncsTx.setStatus("current")
_F3PtpAccPortFlowPointStatsFollowupsRx_Type = PerfCounter64
_F3PtpAccPortFlowPointStatsFollowupsRx_Object = MibTableColumn
f3PtpAccPortFlowPointStatsFollowupsRx = _F3PtpAccPortFlowPointStatsFollowupsRx_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 1, 1, 9),
    _F3PtpAccPortFlowPointStatsFollowupsRx_Type()
)
f3PtpAccPortFlowPointStatsFollowupsRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpAccPortFlowPointStatsFollowupsRx.setStatus("current")
_F3PtpAccPortFlowPointStatsFollowupsTx_Type = PerfCounter64
_F3PtpAccPortFlowPointStatsFollowupsTx_Object = MibTableColumn
f3PtpAccPortFlowPointStatsFollowupsTx = _F3PtpAccPortFlowPointStatsFollowupsTx_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 1, 1, 10),
    _F3PtpAccPortFlowPointStatsFollowupsTx_Type()
)
f3PtpAccPortFlowPointStatsFollowupsTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpAccPortFlowPointStatsFollowupsTx.setStatus("current")
_F3PtpAccPortFlowPointStatsDelayReqsRx_Type = PerfCounter64
_F3PtpAccPortFlowPointStatsDelayReqsRx_Object = MibTableColumn
f3PtpAccPortFlowPointStatsDelayReqsRx = _F3PtpAccPortFlowPointStatsDelayReqsRx_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 1, 1, 11),
    _F3PtpAccPortFlowPointStatsDelayReqsRx_Type()
)
f3PtpAccPortFlowPointStatsDelayReqsRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpAccPortFlowPointStatsDelayReqsRx.setStatus("current")
_F3PtpAccPortFlowPointStatsDelayReqsTx_Type = PerfCounter64
_F3PtpAccPortFlowPointStatsDelayReqsTx_Object = MibTableColumn
f3PtpAccPortFlowPointStatsDelayReqsTx = _F3PtpAccPortFlowPointStatsDelayReqsTx_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 1, 1, 12),
    _F3PtpAccPortFlowPointStatsDelayReqsTx_Type()
)
f3PtpAccPortFlowPointStatsDelayReqsTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpAccPortFlowPointStatsDelayReqsTx.setStatus("current")
_F3PtpAccPortFlowPointStatsDelayRspsRx_Type = PerfCounter64
_F3PtpAccPortFlowPointStatsDelayRspsRx_Object = MibTableColumn
f3PtpAccPortFlowPointStatsDelayRspsRx = _F3PtpAccPortFlowPointStatsDelayRspsRx_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 1, 1, 13),
    _F3PtpAccPortFlowPointStatsDelayRspsRx_Type()
)
f3PtpAccPortFlowPointStatsDelayRspsRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpAccPortFlowPointStatsDelayRspsRx.setStatus("current")
_F3PtpAccPortFlowPointStatsDelayRspsTx_Type = PerfCounter64
_F3PtpAccPortFlowPointStatsDelayRspsTx_Object = MibTableColumn
f3PtpAccPortFlowPointStatsDelayRspsTx = _F3PtpAccPortFlowPointStatsDelayRspsTx_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 1, 1, 14),
    _F3PtpAccPortFlowPointStatsDelayRspsTx_Type()
)
f3PtpAccPortFlowPointStatsDelayRspsTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpAccPortFlowPointStatsDelayRspsTx.setStatus("current")
_F3PtpAccPortFlowPointStatsPDelayReqsRx_Type = PerfCounter64
_F3PtpAccPortFlowPointStatsPDelayReqsRx_Object = MibTableColumn
f3PtpAccPortFlowPointStatsPDelayReqsRx = _F3PtpAccPortFlowPointStatsPDelayReqsRx_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 1, 1, 15),
    _F3PtpAccPortFlowPointStatsPDelayReqsRx_Type()
)
f3PtpAccPortFlowPointStatsPDelayReqsRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpAccPortFlowPointStatsPDelayReqsRx.setStatus("current")
_F3PtpAccPortFlowPointStatsPDelayReqsTx_Type = PerfCounter64
_F3PtpAccPortFlowPointStatsPDelayReqsTx_Object = MibTableColumn
f3PtpAccPortFlowPointStatsPDelayReqsTx = _F3PtpAccPortFlowPointStatsPDelayReqsTx_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 1, 1, 16),
    _F3PtpAccPortFlowPointStatsPDelayReqsTx_Type()
)
f3PtpAccPortFlowPointStatsPDelayReqsTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpAccPortFlowPointStatsPDelayReqsTx.setStatus("current")
_F3PtpAccPortFlowPointStatsPDelayRspsRx_Type = PerfCounter64
_F3PtpAccPortFlowPointStatsPDelayRspsRx_Object = MibTableColumn
f3PtpAccPortFlowPointStatsPDelayRspsRx = _F3PtpAccPortFlowPointStatsPDelayRspsRx_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 1, 1, 17),
    _F3PtpAccPortFlowPointStatsPDelayRspsRx_Type()
)
f3PtpAccPortFlowPointStatsPDelayRspsRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpAccPortFlowPointStatsPDelayRspsRx.setStatus("current")
_F3PtpAccPortFlowPointStatsPDelayRspsTx_Type = PerfCounter64
_F3PtpAccPortFlowPointStatsPDelayRspsTx_Object = MibTableColumn
f3PtpAccPortFlowPointStatsPDelayRspsTx = _F3PtpAccPortFlowPointStatsPDelayRspsTx_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 1, 1, 18),
    _F3PtpAccPortFlowPointStatsPDelayRspsTx_Type()
)
f3PtpAccPortFlowPointStatsPDelayRspsTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpAccPortFlowPointStatsPDelayRspsTx.setStatus("current")
_F3PtpAccPortFlowPointStatsPDelayRspFollowupsRx_Type = PerfCounter64
_F3PtpAccPortFlowPointStatsPDelayRspFollowupsRx_Object = MibTableColumn
f3PtpAccPortFlowPointStatsPDelayRspFollowupsRx = _F3PtpAccPortFlowPointStatsPDelayRspFollowupsRx_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 1, 1, 19),
    _F3PtpAccPortFlowPointStatsPDelayRspFollowupsRx_Type()
)
f3PtpAccPortFlowPointStatsPDelayRspFollowupsRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpAccPortFlowPointStatsPDelayRspFollowupsRx.setStatus("current")
_F3PtpAccPortFlowPointStatsPDelayRspFollowupsTx_Type = PerfCounter64
_F3PtpAccPortFlowPointStatsPDelayRspFollowupsTx_Object = MibTableColumn
f3PtpAccPortFlowPointStatsPDelayRspFollowupsTx = _F3PtpAccPortFlowPointStatsPDelayRspFollowupsTx_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 1, 1, 20),
    _F3PtpAccPortFlowPointStatsPDelayRspFollowupsTx_Type()
)
f3PtpAccPortFlowPointStatsPDelayRspFollowupsTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpAccPortFlowPointStatsPDelayRspFollowupsTx.setStatus("current")
_F3PtpAccPortFlowPointStatsSignalingRx_Type = PerfCounter64
_F3PtpAccPortFlowPointStatsSignalingRx_Object = MibTableColumn
f3PtpAccPortFlowPointStatsSignalingRx = _F3PtpAccPortFlowPointStatsSignalingRx_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 1, 1, 21),
    _F3PtpAccPortFlowPointStatsSignalingRx_Type()
)
f3PtpAccPortFlowPointStatsSignalingRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpAccPortFlowPointStatsSignalingRx.setStatus("current")
_F3PtpAccPortFlowPointStatsSignalingTx_Type = PerfCounter64
_F3PtpAccPortFlowPointStatsSignalingTx_Object = MibTableColumn
f3PtpAccPortFlowPointStatsSignalingTx = _F3PtpAccPortFlowPointStatsSignalingTx_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 1, 1, 22),
    _F3PtpAccPortFlowPointStatsSignalingTx_Type()
)
f3PtpAccPortFlowPointStatsSignalingTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpAccPortFlowPointStatsSignalingTx.setStatus("current")
_F3PtpAccPortFlowPointStatsMgmtFramesRx_Type = PerfCounter64
_F3PtpAccPortFlowPointStatsMgmtFramesRx_Object = MibTableColumn
f3PtpAccPortFlowPointStatsMgmtFramesRx = _F3PtpAccPortFlowPointStatsMgmtFramesRx_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 1, 1, 23),
    _F3PtpAccPortFlowPointStatsMgmtFramesRx_Type()
)
f3PtpAccPortFlowPointStatsMgmtFramesRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpAccPortFlowPointStatsMgmtFramesRx.setStatus("current")
_F3PtpAccPortFlowPointStatsMgmtFramesTx_Type = PerfCounter64
_F3PtpAccPortFlowPointStatsMgmtFramesTx_Object = MibTableColumn
f3PtpAccPortFlowPointStatsMgmtFramesTx = _F3PtpAccPortFlowPointStatsMgmtFramesTx_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 1, 1, 24),
    _F3PtpAccPortFlowPointStatsMgmtFramesTx_Type()
)
f3PtpAccPortFlowPointStatsMgmtFramesTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpAccPortFlowPointStatsMgmtFramesTx.setStatus("current")
_F3PtpAccPortFlowPointStatsPtpUnknownsRx_Type = PerfCounter64
_F3PtpAccPortFlowPointStatsPtpUnknownsRx_Object = MibTableColumn
f3PtpAccPortFlowPointStatsPtpUnknownsRx = _F3PtpAccPortFlowPointStatsPtpUnknownsRx_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 1, 1, 25),
    _F3PtpAccPortFlowPointStatsPtpUnknownsRx_Type()
)
f3PtpAccPortFlowPointStatsPtpUnknownsRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpAccPortFlowPointStatsPtpUnknownsRx.setStatus("current")
_F3PtpAccPortFlowPointStatsPtpUnknownsTx_Type = PerfCounter64
_F3PtpAccPortFlowPointStatsPtpUnknownsTx_Object = MibTableColumn
f3PtpAccPortFlowPointStatsPtpUnknownsTx = _F3PtpAccPortFlowPointStatsPtpUnknownsTx_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 1, 1, 26),
    _F3PtpAccPortFlowPointStatsPtpUnknownsTx_Type()
)
f3PtpAccPortFlowPointStatsPtpUnknownsTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpAccPortFlowPointStatsPtpUnknownsTx.setStatus("current")
_F3PtpAccPortFlowPointStatsMinSyncResTime_Type = Unsigned32
_F3PtpAccPortFlowPointStatsMinSyncResTime_Object = MibTableColumn
f3PtpAccPortFlowPointStatsMinSyncResTime = _F3PtpAccPortFlowPointStatsMinSyncResTime_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 1, 1, 27),
    _F3PtpAccPortFlowPointStatsMinSyncResTime_Type()
)
f3PtpAccPortFlowPointStatsMinSyncResTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpAccPortFlowPointStatsMinSyncResTime.setStatus("deprecated")
_F3PtpAccPortFlowPointStatsMaxSyncResTime_Type = Unsigned32
_F3PtpAccPortFlowPointStatsMaxSyncResTime_Object = MibTableColumn
f3PtpAccPortFlowPointStatsMaxSyncResTime = _F3PtpAccPortFlowPointStatsMaxSyncResTime_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 1, 1, 28),
    _F3PtpAccPortFlowPointStatsMaxSyncResTime_Type()
)
f3PtpAccPortFlowPointStatsMaxSyncResTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpAccPortFlowPointStatsMaxSyncResTime.setStatus("deprecated")
_F3PtpAccPortFlowPointStatsAvgSyncResTime_Type = Unsigned32
_F3PtpAccPortFlowPointStatsAvgSyncResTime_Object = MibTableColumn
f3PtpAccPortFlowPointStatsAvgSyncResTime = _F3PtpAccPortFlowPointStatsAvgSyncResTime_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 1, 1, 29),
    _F3PtpAccPortFlowPointStatsAvgSyncResTime_Type()
)
f3PtpAccPortFlowPointStatsAvgSyncResTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpAccPortFlowPointStatsAvgSyncResTime.setStatus("deprecated")
_F3PtpAccPortFlowPointStatsMinDelayReqResTime_Type = Unsigned32
_F3PtpAccPortFlowPointStatsMinDelayReqResTime_Object = MibTableColumn
f3PtpAccPortFlowPointStatsMinDelayReqResTime = _F3PtpAccPortFlowPointStatsMinDelayReqResTime_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 1, 1, 30),
    _F3PtpAccPortFlowPointStatsMinDelayReqResTime_Type()
)
f3PtpAccPortFlowPointStatsMinDelayReqResTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpAccPortFlowPointStatsMinDelayReqResTime.setStatus("deprecated")
_F3PtpAccPortFlowPointStatsMaxDelayReqResTime_Type = Unsigned32
_F3PtpAccPortFlowPointStatsMaxDelayReqResTime_Object = MibTableColumn
f3PtpAccPortFlowPointStatsMaxDelayReqResTime = _F3PtpAccPortFlowPointStatsMaxDelayReqResTime_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 1, 1, 31),
    _F3PtpAccPortFlowPointStatsMaxDelayReqResTime_Type()
)
f3PtpAccPortFlowPointStatsMaxDelayReqResTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpAccPortFlowPointStatsMaxDelayReqResTime.setStatus("deprecated")
_F3PtpAccPortFlowPointStatsAvgDelayReqResTime_Type = Unsigned32
_F3PtpAccPortFlowPointStatsAvgDelayReqResTime_Object = MibTableColumn
f3PtpAccPortFlowPointStatsAvgDelayReqResTime = _F3PtpAccPortFlowPointStatsAvgDelayReqResTime_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 1, 1, 32),
    _F3PtpAccPortFlowPointStatsAvgDelayReqResTime_Type()
)
f3PtpAccPortFlowPointStatsAvgDelayReqResTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpAccPortFlowPointStatsAvgDelayReqResTime.setStatus("deprecated")
_F3PtpAccPortFlowPointStatsMinPDelayReqResTime_Type = Unsigned32
_F3PtpAccPortFlowPointStatsMinPDelayReqResTime_Object = MibTableColumn
f3PtpAccPortFlowPointStatsMinPDelayReqResTime = _F3PtpAccPortFlowPointStatsMinPDelayReqResTime_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 1, 1, 33),
    _F3PtpAccPortFlowPointStatsMinPDelayReqResTime_Type()
)
f3PtpAccPortFlowPointStatsMinPDelayReqResTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpAccPortFlowPointStatsMinPDelayReqResTime.setStatus("deprecated")
_F3PtpAccPortFlowPointStatsMaxPDelayReqResTime_Type = Unsigned32
_F3PtpAccPortFlowPointStatsMaxPDelayReqResTime_Object = MibTableColumn
f3PtpAccPortFlowPointStatsMaxPDelayReqResTime = _F3PtpAccPortFlowPointStatsMaxPDelayReqResTime_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 1, 1, 34),
    _F3PtpAccPortFlowPointStatsMaxPDelayReqResTime_Type()
)
f3PtpAccPortFlowPointStatsMaxPDelayReqResTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpAccPortFlowPointStatsMaxPDelayReqResTime.setStatus("deprecated")
_F3PtpAccPortFlowPointStatsAvgPDelayReqResTime_Type = Unsigned32
_F3PtpAccPortFlowPointStatsAvgPDelayReqResTime_Object = MibTableColumn
f3PtpAccPortFlowPointStatsAvgPDelayReqResTime = _F3PtpAccPortFlowPointStatsAvgPDelayReqResTime_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 1, 1, 35),
    _F3PtpAccPortFlowPointStatsAvgPDelayReqResTime_Type()
)
f3PtpAccPortFlowPointStatsAvgPDelayReqResTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpAccPortFlowPointStatsAvgPDelayReqResTime.setStatus("deprecated")
_F3PtpAccPortFlowPointStatsMinPDelayRspResTime_Type = Unsigned32
_F3PtpAccPortFlowPointStatsMinPDelayRspResTime_Object = MibTableColumn
f3PtpAccPortFlowPointStatsMinPDelayRspResTime = _F3PtpAccPortFlowPointStatsMinPDelayRspResTime_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 1, 1, 36),
    _F3PtpAccPortFlowPointStatsMinPDelayRspResTime_Type()
)
f3PtpAccPortFlowPointStatsMinPDelayRspResTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpAccPortFlowPointStatsMinPDelayRspResTime.setStatus("deprecated")
_F3PtpAccPortFlowPointStatsMaxPDelayRspResTime_Type = Unsigned32
_F3PtpAccPortFlowPointStatsMaxPDelayRspResTime_Object = MibTableColumn
f3PtpAccPortFlowPointStatsMaxPDelayRspResTime = _F3PtpAccPortFlowPointStatsMaxPDelayRspResTime_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 1, 1, 37),
    _F3PtpAccPortFlowPointStatsMaxPDelayRspResTime_Type()
)
f3PtpAccPortFlowPointStatsMaxPDelayRspResTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpAccPortFlowPointStatsMaxPDelayRspResTime.setStatus("deprecated")
_F3PtpAccPortFlowPointStatsAvgPDelayRspResTime_Type = Unsigned32
_F3PtpAccPortFlowPointStatsAvgPDelayRspResTime_Object = MibTableColumn
f3PtpAccPortFlowPointStatsAvgPDelayRspResTime = _F3PtpAccPortFlowPointStatsAvgPDelayRspResTime_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 1, 1, 38),
    _F3PtpAccPortFlowPointStatsAvgPDelayRspResTime_Type()
)
f3PtpAccPortFlowPointStatsAvgPDelayRspResTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpAccPortFlowPointStatsAvgPDelayRspResTime.setStatus("deprecated")
_F3PtpAccPortFlowPointStatsDestMciNoMatchDiscards_Type = PerfCounter64
_F3PtpAccPortFlowPointStatsDestMciNoMatchDiscards_Object = MibTableColumn
f3PtpAccPortFlowPointStatsDestMciNoMatchDiscards = _F3PtpAccPortFlowPointStatsDestMciNoMatchDiscards_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 1, 1, 39),
    _F3PtpAccPortFlowPointStatsDestMciNoMatchDiscards_Type()
)
f3PtpAccPortFlowPointStatsDestMciNoMatchDiscards.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3PtpAccPortFlowPointStatsDestMciNoMatchDiscards.setStatus("current")
_F3PtpAccPortFlowPointStatsTagNoMatchDiscards_Type = PerfCounter64
_F3PtpAccPortFlowPointStatsTagNoMatchDiscards_Object = MibTableColumn
f3PtpAccPortFlowPointStatsTagNoMatchDiscards = _F3PtpAccPortFlowPointStatsTagNoMatchDiscards_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 1, 1, 40),
    _F3PtpAccPortFlowPointStatsTagNoMatchDiscards_Type()
)
f3PtpAccPortFlowPointStatsTagNoMatchDiscards.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3PtpAccPortFlowPointStatsTagNoMatchDiscards.setStatus("current")
_F3PtpAccPortFlowPointHistoryTable_Object = MibTable
f3PtpAccPortFlowPointHistoryTable = _F3PtpAccPortFlowPointHistoryTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 2)
)
if mibBuilder.loadTexts:
    f3PtpAccPortFlowPointHistoryTable.setStatus("current")
_F3PtpAccPortFlowPointHistoryEntry_Object = MibTableRow
f3PtpAccPortFlowPointHistoryEntry = _F3PtpAccPortFlowPointHistoryEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 2, 1)
)
f3PtpAccPortFlowPointHistoryEntry.setIndexNames(
    (0, "CM-ENTITY-MIB", "neIndex"),
    (0, "CM-ENTITY-MIB", "shelfIndex"),
    (0, "CM-ENTITY-MIB", "slotIndex"),
    (0, "CM-FACILITY-MIB", "cmEthernetAccPortIndex"),
    (0, "F3-PTP-MIB", "f3PtpAccPortFlowPointIndex"),
    (0, "F3-PTP-MIB", "f3PtpAccPortFlowPointStatsIndex"),
    (0, "F3-PTP-MIB", "f3PtpAccPortFlowPointHistoryIndex"),
)
if mibBuilder.loadTexts:
    f3PtpAccPortFlowPointHistoryEntry.setStatus("current")


class _F3PtpAccPortFlowPointHistoryIndex_Type(Integer32):
    """Custom type f3PtpAccPortFlowPointHistoryIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_F3PtpAccPortFlowPointHistoryIndex_Type.__name__ = "Integer32"
_F3PtpAccPortFlowPointHistoryIndex_Object = MibTableColumn
f3PtpAccPortFlowPointHistoryIndex = _F3PtpAccPortFlowPointHistoryIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 2, 1, 1),
    _F3PtpAccPortFlowPointHistoryIndex_Type()
)
f3PtpAccPortFlowPointHistoryIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    f3PtpAccPortFlowPointHistoryIndex.setStatus("current")
_F3PtpAccPortFlowPointHistoryTime_Type = DateAndTime
_F3PtpAccPortFlowPointHistoryTime_Object = MibTableColumn
f3PtpAccPortFlowPointHistoryTime = _F3PtpAccPortFlowPointHistoryTime_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 2, 1, 2),
    _F3PtpAccPortFlowPointHistoryTime_Type()
)
f3PtpAccPortFlowPointHistoryTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpAccPortFlowPointHistoryTime.setStatus("current")
_F3PtpAccPortFlowPointHistoryValid_Type = TruthValue
_F3PtpAccPortFlowPointHistoryValid_Object = MibTableColumn
f3PtpAccPortFlowPointHistoryValid = _F3PtpAccPortFlowPointHistoryValid_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 2, 1, 3),
    _F3PtpAccPortFlowPointHistoryValid_Type()
)
f3PtpAccPortFlowPointHistoryValid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpAccPortFlowPointHistoryValid.setStatus("current")
_F3PtpAccPortFlowPointHistoryAction_Type = CmPmBinAction
_F3PtpAccPortFlowPointHistoryAction_Object = MibTableColumn
f3PtpAccPortFlowPointHistoryAction = _F3PtpAccPortFlowPointHistoryAction_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 2, 1, 4),
    _F3PtpAccPortFlowPointHistoryAction_Type()
)
f3PtpAccPortFlowPointHistoryAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3PtpAccPortFlowPointHistoryAction.setStatus("current")
_F3PtpAccPortFlowPointHistoryAnnouncesRx_Type = PerfCounter64
_F3PtpAccPortFlowPointHistoryAnnouncesRx_Object = MibTableColumn
f3PtpAccPortFlowPointHistoryAnnouncesRx = _F3PtpAccPortFlowPointHistoryAnnouncesRx_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 2, 1, 5),
    _F3PtpAccPortFlowPointHistoryAnnouncesRx_Type()
)
f3PtpAccPortFlowPointHistoryAnnouncesRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpAccPortFlowPointHistoryAnnouncesRx.setStatus("current")
_F3PtpAccPortFlowPointHistoryAnnouncesTx_Type = PerfCounter64
_F3PtpAccPortFlowPointHistoryAnnouncesTx_Object = MibTableColumn
f3PtpAccPortFlowPointHistoryAnnouncesTx = _F3PtpAccPortFlowPointHistoryAnnouncesTx_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 2, 1, 6),
    _F3PtpAccPortFlowPointHistoryAnnouncesTx_Type()
)
f3PtpAccPortFlowPointHistoryAnnouncesTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpAccPortFlowPointHistoryAnnouncesTx.setStatus("current")
_F3PtpAccPortFlowPointHistorySyncsRx_Type = PerfCounter64
_F3PtpAccPortFlowPointHistorySyncsRx_Object = MibTableColumn
f3PtpAccPortFlowPointHistorySyncsRx = _F3PtpAccPortFlowPointHistorySyncsRx_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 2, 1, 7),
    _F3PtpAccPortFlowPointHistorySyncsRx_Type()
)
f3PtpAccPortFlowPointHistorySyncsRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpAccPortFlowPointHistorySyncsRx.setStatus("current")
_F3PtpAccPortFlowPointHistorySyncsTx_Type = PerfCounter64
_F3PtpAccPortFlowPointHistorySyncsTx_Object = MibTableColumn
f3PtpAccPortFlowPointHistorySyncsTx = _F3PtpAccPortFlowPointHistorySyncsTx_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 2, 1, 8),
    _F3PtpAccPortFlowPointHistorySyncsTx_Type()
)
f3PtpAccPortFlowPointHistorySyncsTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpAccPortFlowPointHistorySyncsTx.setStatus("current")
_F3PtpAccPortFlowPointHistoryFollowupsRx_Type = PerfCounter64
_F3PtpAccPortFlowPointHistoryFollowupsRx_Object = MibTableColumn
f3PtpAccPortFlowPointHistoryFollowupsRx = _F3PtpAccPortFlowPointHistoryFollowupsRx_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 2, 1, 9),
    _F3PtpAccPortFlowPointHistoryFollowupsRx_Type()
)
f3PtpAccPortFlowPointHistoryFollowupsRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpAccPortFlowPointHistoryFollowupsRx.setStatus("current")
_F3PtpAccPortFlowPointHistoryFollowupsTx_Type = PerfCounter64
_F3PtpAccPortFlowPointHistoryFollowupsTx_Object = MibTableColumn
f3PtpAccPortFlowPointHistoryFollowupsTx = _F3PtpAccPortFlowPointHistoryFollowupsTx_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 2, 1, 10),
    _F3PtpAccPortFlowPointHistoryFollowupsTx_Type()
)
f3PtpAccPortFlowPointHistoryFollowupsTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpAccPortFlowPointHistoryFollowupsTx.setStatus("current")
_F3PtpAccPortFlowPointHistoryDelayReqsRx_Type = PerfCounter64
_F3PtpAccPortFlowPointHistoryDelayReqsRx_Object = MibTableColumn
f3PtpAccPortFlowPointHistoryDelayReqsRx = _F3PtpAccPortFlowPointHistoryDelayReqsRx_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 2, 1, 11),
    _F3PtpAccPortFlowPointHistoryDelayReqsRx_Type()
)
f3PtpAccPortFlowPointHistoryDelayReqsRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpAccPortFlowPointHistoryDelayReqsRx.setStatus("current")
_F3PtpAccPortFlowPointHistoryDelayReqsTx_Type = PerfCounter64
_F3PtpAccPortFlowPointHistoryDelayReqsTx_Object = MibTableColumn
f3PtpAccPortFlowPointHistoryDelayReqsTx = _F3PtpAccPortFlowPointHistoryDelayReqsTx_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 2, 1, 12),
    _F3PtpAccPortFlowPointHistoryDelayReqsTx_Type()
)
f3PtpAccPortFlowPointHistoryDelayReqsTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpAccPortFlowPointHistoryDelayReqsTx.setStatus("current")
_F3PtpAccPortFlowPointHistoryDelayRspsRx_Type = PerfCounter64
_F3PtpAccPortFlowPointHistoryDelayRspsRx_Object = MibTableColumn
f3PtpAccPortFlowPointHistoryDelayRspsRx = _F3PtpAccPortFlowPointHistoryDelayRspsRx_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 2, 1, 13),
    _F3PtpAccPortFlowPointHistoryDelayRspsRx_Type()
)
f3PtpAccPortFlowPointHistoryDelayRspsRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpAccPortFlowPointHistoryDelayRspsRx.setStatus("current")
_F3PtpAccPortFlowPointHistoryDelayRspsTx_Type = PerfCounter64
_F3PtpAccPortFlowPointHistoryDelayRspsTx_Object = MibTableColumn
f3PtpAccPortFlowPointHistoryDelayRspsTx = _F3PtpAccPortFlowPointHistoryDelayRspsTx_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 2, 1, 14),
    _F3PtpAccPortFlowPointHistoryDelayRspsTx_Type()
)
f3PtpAccPortFlowPointHistoryDelayRspsTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpAccPortFlowPointHistoryDelayRspsTx.setStatus("current")
_F3PtpAccPortFlowPointHistoryPDelayReqsRx_Type = PerfCounter64
_F3PtpAccPortFlowPointHistoryPDelayReqsRx_Object = MibTableColumn
f3PtpAccPortFlowPointHistoryPDelayReqsRx = _F3PtpAccPortFlowPointHistoryPDelayReqsRx_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 2, 1, 15),
    _F3PtpAccPortFlowPointHistoryPDelayReqsRx_Type()
)
f3PtpAccPortFlowPointHistoryPDelayReqsRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpAccPortFlowPointHistoryPDelayReqsRx.setStatus("current")
_F3PtpAccPortFlowPointHistoryPDelayReqsTx_Type = PerfCounter64
_F3PtpAccPortFlowPointHistoryPDelayReqsTx_Object = MibTableColumn
f3PtpAccPortFlowPointHistoryPDelayReqsTx = _F3PtpAccPortFlowPointHistoryPDelayReqsTx_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 2, 1, 16),
    _F3PtpAccPortFlowPointHistoryPDelayReqsTx_Type()
)
f3PtpAccPortFlowPointHistoryPDelayReqsTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpAccPortFlowPointHistoryPDelayReqsTx.setStatus("current")
_F3PtpAccPortFlowPointHistoryPDelayRspsRx_Type = PerfCounter64
_F3PtpAccPortFlowPointHistoryPDelayRspsRx_Object = MibTableColumn
f3PtpAccPortFlowPointHistoryPDelayRspsRx = _F3PtpAccPortFlowPointHistoryPDelayRspsRx_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 2, 1, 17),
    _F3PtpAccPortFlowPointHistoryPDelayRspsRx_Type()
)
f3PtpAccPortFlowPointHistoryPDelayRspsRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpAccPortFlowPointHistoryPDelayRspsRx.setStatus("current")
_F3PtpAccPortFlowPointHistoryPDelayRspsTx_Type = PerfCounter64
_F3PtpAccPortFlowPointHistoryPDelayRspsTx_Object = MibTableColumn
f3PtpAccPortFlowPointHistoryPDelayRspsTx = _F3PtpAccPortFlowPointHistoryPDelayRspsTx_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 2, 1, 18),
    _F3PtpAccPortFlowPointHistoryPDelayRspsTx_Type()
)
f3PtpAccPortFlowPointHistoryPDelayRspsTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpAccPortFlowPointHistoryPDelayRspsTx.setStatus("current")
_F3PtpAccPortFlowPointHistoryPDelayRspFollowupsRx_Type = PerfCounter64
_F3PtpAccPortFlowPointHistoryPDelayRspFollowupsRx_Object = MibTableColumn
f3PtpAccPortFlowPointHistoryPDelayRspFollowupsRx = _F3PtpAccPortFlowPointHistoryPDelayRspFollowupsRx_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 2, 1, 19),
    _F3PtpAccPortFlowPointHistoryPDelayRspFollowupsRx_Type()
)
f3PtpAccPortFlowPointHistoryPDelayRspFollowupsRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpAccPortFlowPointHistoryPDelayRspFollowupsRx.setStatus("current")
_F3PtpAccPortFlowPointHistoryPDelayRspFollowupsTx_Type = PerfCounter64
_F3PtpAccPortFlowPointHistoryPDelayRspFollowupsTx_Object = MibTableColumn
f3PtpAccPortFlowPointHistoryPDelayRspFollowupsTx = _F3PtpAccPortFlowPointHistoryPDelayRspFollowupsTx_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 2, 1, 20),
    _F3PtpAccPortFlowPointHistoryPDelayRspFollowupsTx_Type()
)
f3PtpAccPortFlowPointHistoryPDelayRspFollowupsTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpAccPortFlowPointHistoryPDelayRspFollowupsTx.setStatus("current")
_F3PtpAccPortFlowPointHistorySignalingRx_Type = PerfCounter64
_F3PtpAccPortFlowPointHistorySignalingRx_Object = MibTableColumn
f3PtpAccPortFlowPointHistorySignalingRx = _F3PtpAccPortFlowPointHistorySignalingRx_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 2, 1, 21),
    _F3PtpAccPortFlowPointHistorySignalingRx_Type()
)
f3PtpAccPortFlowPointHistorySignalingRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpAccPortFlowPointHistorySignalingRx.setStatus("current")
_F3PtpAccPortFlowPointHistorySignalingTx_Type = PerfCounter64
_F3PtpAccPortFlowPointHistorySignalingTx_Object = MibTableColumn
f3PtpAccPortFlowPointHistorySignalingTx = _F3PtpAccPortFlowPointHistorySignalingTx_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 2, 1, 22),
    _F3PtpAccPortFlowPointHistorySignalingTx_Type()
)
f3PtpAccPortFlowPointHistorySignalingTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpAccPortFlowPointHistorySignalingTx.setStatus("current")
_F3PtpAccPortFlowPointHistoryMgmtFramesRx_Type = PerfCounter64
_F3PtpAccPortFlowPointHistoryMgmtFramesRx_Object = MibTableColumn
f3PtpAccPortFlowPointHistoryMgmtFramesRx = _F3PtpAccPortFlowPointHistoryMgmtFramesRx_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 2, 1, 23),
    _F3PtpAccPortFlowPointHistoryMgmtFramesRx_Type()
)
f3PtpAccPortFlowPointHistoryMgmtFramesRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpAccPortFlowPointHistoryMgmtFramesRx.setStatus("current")
_F3PtpAccPortFlowPointHistoryMgmtFramesTx_Type = PerfCounter64
_F3PtpAccPortFlowPointHistoryMgmtFramesTx_Object = MibTableColumn
f3PtpAccPortFlowPointHistoryMgmtFramesTx = _F3PtpAccPortFlowPointHistoryMgmtFramesTx_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 2, 1, 24),
    _F3PtpAccPortFlowPointHistoryMgmtFramesTx_Type()
)
f3PtpAccPortFlowPointHistoryMgmtFramesTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpAccPortFlowPointHistoryMgmtFramesTx.setStatus("current")
_F3PtpAccPortFlowPointHistoryPtpUnknownsRx_Type = PerfCounter64
_F3PtpAccPortFlowPointHistoryPtpUnknownsRx_Object = MibTableColumn
f3PtpAccPortFlowPointHistoryPtpUnknownsRx = _F3PtpAccPortFlowPointHistoryPtpUnknownsRx_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 2, 1, 25),
    _F3PtpAccPortFlowPointHistoryPtpUnknownsRx_Type()
)
f3PtpAccPortFlowPointHistoryPtpUnknownsRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpAccPortFlowPointHistoryPtpUnknownsRx.setStatus("current")
_F3PtpAccPortFlowPointHistoryPtpUnknownsTx_Type = PerfCounter64
_F3PtpAccPortFlowPointHistoryPtpUnknownsTx_Object = MibTableColumn
f3PtpAccPortFlowPointHistoryPtpUnknownsTx = _F3PtpAccPortFlowPointHistoryPtpUnknownsTx_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 2, 1, 26),
    _F3PtpAccPortFlowPointHistoryPtpUnknownsTx_Type()
)
f3PtpAccPortFlowPointHistoryPtpUnknownsTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpAccPortFlowPointHistoryPtpUnknownsTx.setStatus("current")
_F3PtpAccPortFlowPointHistoryMinSyncResTime_Type = Unsigned32
_F3PtpAccPortFlowPointHistoryMinSyncResTime_Object = MibTableColumn
f3PtpAccPortFlowPointHistoryMinSyncResTime = _F3PtpAccPortFlowPointHistoryMinSyncResTime_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 2, 1, 27),
    _F3PtpAccPortFlowPointHistoryMinSyncResTime_Type()
)
f3PtpAccPortFlowPointHistoryMinSyncResTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpAccPortFlowPointHistoryMinSyncResTime.setStatus("deprecated")
_F3PtpAccPortFlowPointHistoryMaxSyncResTime_Type = Unsigned32
_F3PtpAccPortFlowPointHistoryMaxSyncResTime_Object = MibTableColumn
f3PtpAccPortFlowPointHistoryMaxSyncResTime = _F3PtpAccPortFlowPointHistoryMaxSyncResTime_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 2, 1, 28),
    _F3PtpAccPortFlowPointHistoryMaxSyncResTime_Type()
)
f3PtpAccPortFlowPointHistoryMaxSyncResTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpAccPortFlowPointHistoryMaxSyncResTime.setStatus("deprecated")
_F3PtpAccPortFlowPointHistoryAvgSyncResTime_Type = Unsigned32
_F3PtpAccPortFlowPointHistoryAvgSyncResTime_Object = MibTableColumn
f3PtpAccPortFlowPointHistoryAvgSyncResTime = _F3PtpAccPortFlowPointHistoryAvgSyncResTime_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 2, 1, 29),
    _F3PtpAccPortFlowPointHistoryAvgSyncResTime_Type()
)
f3PtpAccPortFlowPointHistoryAvgSyncResTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpAccPortFlowPointHistoryAvgSyncResTime.setStatus("deprecated")
_F3PtpAccPortFlowPointHistoryMinDelayReqResTime_Type = Unsigned32
_F3PtpAccPortFlowPointHistoryMinDelayReqResTime_Object = MibTableColumn
f3PtpAccPortFlowPointHistoryMinDelayReqResTime = _F3PtpAccPortFlowPointHistoryMinDelayReqResTime_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 2, 1, 30),
    _F3PtpAccPortFlowPointHistoryMinDelayReqResTime_Type()
)
f3PtpAccPortFlowPointHistoryMinDelayReqResTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpAccPortFlowPointHistoryMinDelayReqResTime.setStatus("deprecated")
_F3PtpAccPortFlowPointHistoryMaxDelayReqResTime_Type = Unsigned32
_F3PtpAccPortFlowPointHistoryMaxDelayReqResTime_Object = MibTableColumn
f3PtpAccPortFlowPointHistoryMaxDelayReqResTime = _F3PtpAccPortFlowPointHistoryMaxDelayReqResTime_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 2, 1, 31),
    _F3PtpAccPortFlowPointHistoryMaxDelayReqResTime_Type()
)
f3PtpAccPortFlowPointHistoryMaxDelayReqResTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpAccPortFlowPointHistoryMaxDelayReqResTime.setStatus("deprecated")
_F3PtpAccPortFlowPointHistoryAvgDelayReqResTime_Type = Unsigned32
_F3PtpAccPortFlowPointHistoryAvgDelayReqResTime_Object = MibTableColumn
f3PtpAccPortFlowPointHistoryAvgDelayReqResTime = _F3PtpAccPortFlowPointHistoryAvgDelayReqResTime_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 2, 1, 32),
    _F3PtpAccPortFlowPointHistoryAvgDelayReqResTime_Type()
)
f3PtpAccPortFlowPointHistoryAvgDelayReqResTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpAccPortFlowPointHistoryAvgDelayReqResTime.setStatus("deprecated")
_F3PtpAccPortFlowPointHistoryMinPDelayReqResTime_Type = Unsigned32
_F3PtpAccPortFlowPointHistoryMinPDelayReqResTime_Object = MibTableColumn
f3PtpAccPortFlowPointHistoryMinPDelayReqResTime = _F3PtpAccPortFlowPointHistoryMinPDelayReqResTime_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 2, 1, 33),
    _F3PtpAccPortFlowPointHistoryMinPDelayReqResTime_Type()
)
f3PtpAccPortFlowPointHistoryMinPDelayReqResTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpAccPortFlowPointHistoryMinPDelayReqResTime.setStatus("deprecated")
_F3PtpAccPortFlowPointHistoryMaxPDelayReqResTime_Type = Unsigned32
_F3PtpAccPortFlowPointHistoryMaxPDelayReqResTime_Object = MibTableColumn
f3PtpAccPortFlowPointHistoryMaxPDelayReqResTime = _F3PtpAccPortFlowPointHistoryMaxPDelayReqResTime_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 2, 1, 34),
    _F3PtpAccPortFlowPointHistoryMaxPDelayReqResTime_Type()
)
f3PtpAccPortFlowPointHistoryMaxPDelayReqResTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpAccPortFlowPointHistoryMaxPDelayReqResTime.setStatus("deprecated")
_F3PtpAccPortFlowPointHistoryAvgPDelayReqResTime_Type = Unsigned32
_F3PtpAccPortFlowPointHistoryAvgPDelayReqResTime_Object = MibTableColumn
f3PtpAccPortFlowPointHistoryAvgPDelayReqResTime = _F3PtpAccPortFlowPointHistoryAvgPDelayReqResTime_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 2, 1, 35),
    _F3PtpAccPortFlowPointHistoryAvgPDelayReqResTime_Type()
)
f3PtpAccPortFlowPointHistoryAvgPDelayReqResTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpAccPortFlowPointHistoryAvgPDelayReqResTime.setStatus("deprecated")
_F3PtpAccPortFlowPointHistoryMinPDelayRspResTime_Type = Unsigned32
_F3PtpAccPortFlowPointHistoryMinPDelayRspResTime_Object = MibTableColumn
f3PtpAccPortFlowPointHistoryMinPDelayRspResTime = _F3PtpAccPortFlowPointHistoryMinPDelayRspResTime_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 2, 1, 36),
    _F3PtpAccPortFlowPointHistoryMinPDelayRspResTime_Type()
)
f3PtpAccPortFlowPointHistoryMinPDelayRspResTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpAccPortFlowPointHistoryMinPDelayRspResTime.setStatus("deprecated")
_F3PtpAccPortFlowPointHistoryMaxPDelayRspResTime_Type = Unsigned32
_F3PtpAccPortFlowPointHistoryMaxPDelayRspResTime_Object = MibTableColumn
f3PtpAccPortFlowPointHistoryMaxPDelayRspResTime = _F3PtpAccPortFlowPointHistoryMaxPDelayRspResTime_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 2, 1, 37),
    _F3PtpAccPortFlowPointHistoryMaxPDelayRspResTime_Type()
)
f3PtpAccPortFlowPointHistoryMaxPDelayRspResTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpAccPortFlowPointHistoryMaxPDelayRspResTime.setStatus("deprecated")
_F3PtpAccPortFlowPointHistoryAvgPDelayRspResTime_Type = Unsigned32
_F3PtpAccPortFlowPointHistoryAvgPDelayRspResTime_Object = MibTableColumn
f3PtpAccPortFlowPointHistoryAvgPDelayRspResTime = _F3PtpAccPortFlowPointHistoryAvgPDelayRspResTime_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 2, 1, 38),
    _F3PtpAccPortFlowPointHistoryAvgPDelayRspResTime_Type()
)
f3PtpAccPortFlowPointHistoryAvgPDelayRspResTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpAccPortFlowPointHistoryAvgPDelayRspResTime.setStatus("deprecated")
_F3PtpAccPortFlowPointHistoryDestMciNoMatchDiscards_Type = PerfCounter64
_F3PtpAccPortFlowPointHistoryDestMciNoMatchDiscards_Object = MibTableColumn
f3PtpAccPortFlowPointHistoryDestMciNoMatchDiscards = _F3PtpAccPortFlowPointHistoryDestMciNoMatchDiscards_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 2, 1, 39),
    _F3PtpAccPortFlowPointHistoryDestMciNoMatchDiscards_Type()
)
f3PtpAccPortFlowPointHistoryDestMciNoMatchDiscards.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3PtpAccPortFlowPointHistoryDestMciNoMatchDiscards.setStatus("current")
_F3PtpAccPortFlowPointHistoryTagNoMatchDiscards_Type = PerfCounter64
_F3PtpAccPortFlowPointHistoryTagNoMatchDiscards_Object = MibTableColumn
f3PtpAccPortFlowPointHistoryTagNoMatchDiscards = _F3PtpAccPortFlowPointHistoryTagNoMatchDiscards_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 2, 1, 40),
    _F3PtpAccPortFlowPointHistoryTagNoMatchDiscards_Type()
)
f3PtpAccPortFlowPointHistoryTagNoMatchDiscards.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3PtpAccPortFlowPointHistoryTagNoMatchDiscards.setStatus("current")
_F3PtpAccPortFlowPointThresholdTable_Object = MibTable
f3PtpAccPortFlowPointThresholdTable = _F3PtpAccPortFlowPointThresholdTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 3)
)
if mibBuilder.loadTexts:
    f3PtpAccPortFlowPointThresholdTable.setStatus("current")
_F3PtpAccPortFlowPointThresholdEntry_Object = MibTableRow
f3PtpAccPortFlowPointThresholdEntry = _F3PtpAccPortFlowPointThresholdEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 3, 1)
)
f3PtpAccPortFlowPointThresholdEntry.setIndexNames(
    (0, "CM-ENTITY-MIB", "neIndex"),
    (0, "CM-ENTITY-MIB", "shelfIndex"),
    (0, "CM-ENTITY-MIB", "slotIndex"),
    (0, "CM-FACILITY-MIB", "cmEthernetAccPortIndex"),
    (0, "F3-PTP-MIB", "f3PtpAccPortFlowPointIndex"),
    (0, "F3-PTP-MIB", "f3PtpAccPortFlowPointStatsIndex"),
    (0, "F3-PTP-MIB", "f3PtpAccPortFlowPointThresholdIndex"),
)
if mibBuilder.loadTexts:
    f3PtpAccPortFlowPointThresholdEntry.setStatus("current")


class _F3PtpAccPortFlowPointThresholdIndex_Type(Integer32):
    """Custom type f3PtpAccPortFlowPointThresholdIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_F3PtpAccPortFlowPointThresholdIndex_Type.__name__ = "Integer32"
_F3PtpAccPortFlowPointThresholdIndex_Object = MibTableColumn
f3PtpAccPortFlowPointThresholdIndex = _F3PtpAccPortFlowPointThresholdIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 3, 1, 1),
    _F3PtpAccPortFlowPointThresholdIndex_Type()
)
f3PtpAccPortFlowPointThresholdIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    f3PtpAccPortFlowPointThresholdIndex.setStatus("current")
_F3PtpAccPortFlowPointThresholdInterval_Type = CmPmIntervalType
_F3PtpAccPortFlowPointThresholdInterval_Object = MibTableColumn
f3PtpAccPortFlowPointThresholdInterval = _F3PtpAccPortFlowPointThresholdInterval_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 3, 1, 2),
    _F3PtpAccPortFlowPointThresholdInterval_Type()
)
f3PtpAccPortFlowPointThresholdInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpAccPortFlowPointThresholdInterval.setStatus("current")
_F3PtpAccPortFlowPointThresholdVariable_Type = VariablePointer
_F3PtpAccPortFlowPointThresholdVariable_Object = MibTableColumn
f3PtpAccPortFlowPointThresholdVariable = _F3PtpAccPortFlowPointThresholdVariable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 3, 1, 3),
    _F3PtpAccPortFlowPointThresholdVariable_Type()
)
f3PtpAccPortFlowPointThresholdVariable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpAccPortFlowPointThresholdVariable.setStatus("current")
_F3PtpAccPortFlowPointThresholdValueLo_Type = Unsigned32
_F3PtpAccPortFlowPointThresholdValueLo_Object = MibTableColumn
f3PtpAccPortFlowPointThresholdValueLo = _F3PtpAccPortFlowPointThresholdValueLo_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 3, 1, 4),
    _F3PtpAccPortFlowPointThresholdValueLo_Type()
)
f3PtpAccPortFlowPointThresholdValueLo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3PtpAccPortFlowPointThresholdValueLo.setStatus("current")
_F3PtpAccPortFlowPointThresholdValueHi_Type = Unsigned32
_F3PtpAccPortFlowPointThresholdValueHi_Object = MibTableColumn
f3PtpAccPortFlowPointThresholdValueHi = _F3PtpAccPortFlowPointThresholdValueHi_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 3, 1, 5),
    _F3PtpAccPortFlowPointThresholdValueHi_Type()
)
f3PtpAccPortFlowPointThresholdValueHi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3PtpAccPortFlowPointThresholdValueHi.setStatus("current")
_F3PtpAccPortFlowPointThresholdMonValue_Type = PerfCounter64
_F3PtpAccPortFlowPointThresholdMonValue_Object = MibTableColumn
f3PtpAccPortFlowPointThresholdMonValue = _F3PtpAccPortFlowPointThresholdMonValue_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 3, 1, 6),
    _F3PtpAccPortFlowPointThresholdMonValue_Type()
)
f3PtpAccPortFlowPointThresholdMonValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpAccPortFlowPointThresholdMonValue.setStatus("current")
_F3PtpNetPortFlowPointStatsTable_Object = MibTable
f3PtpNetPortFlowPointStatsTable = _F3PtpNetPortFlowPointStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 4)
)
if mibBuilder.loadTexts:
    f3PtpNetPortFlowPointStatsTable.setStatus("current")
_F3PtpNetPortFlowPointStatsEntry_Object = MibTableRow
f3PtpNetPortFlowPointStatsEntry = _F3PtpNetPortFlowPointStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 4, 1)
)
f3PtpNetPortFlowPointStatsEntry.setIndexNames(
    (0, "CM-ENTITY-MIB", "neIndex"),
    (0, "CM-ENTITY-MIB", "shelfIndex"),
    (0, "CM-ENTITY-MIB", "slotIndex"),
    (0, "CM-FACILITY-MIB", "cmEthernetNetPortIndex"),
    (0, "F3-PTP-MIB", "f3PtpNetPortFlowPointIndex"),
    (0, "F3-PTP-MIB", "f3PtpNetPortFlowPointStatsIndex"),
)
if mibBuilder.loadTexts:
    f3PtpNetPortFlowPointStatsEntry.setStatus("current")


class _F3PtpNetPortFlowPointStatsIndex_Type(Integer32):
    """Custom type f3PtpNetPortFlowPointStatsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_F3PtpNetPortFlowPointStatsIndex_Type.__name__ = "Integer32"
_F3PtpNetPortFlowPointStatsIndex_Object = MibTableColumn
f3PtpNetPortFlowPointStatsIndex = _F3PtpNetPortFlowPointStatsIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 4, 1, 1),
    _F3PtpNetPortFlowPointStatsIndex_Type()
)
f3PtpNetPortFlowPointStatsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    f3PtpNetPortFlowPointStatsIndex.setStatus("current")
_F3PtpNetPortFlowPointStatsIntervalType_Type = CmPmIntervalType
_F3PtpNetPortFlowPointStatsIntervalType_Object = MibTableColumn
f3PtpNetPortFlowPointStatsIntervalType = _F3PtpNetPortFlowPointStatsIntervalType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 4, 1, 2),
    _F3PtpNetPortFlowPointStatsIntervalType_Type()
)
f3PtpNetPortFlowPointStatsIntervalType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpNetPortFlowPointStatsIntervalType.setStatus("current")
_F3PtpNetPortFlowPointStatsValid_Type = TruthValue
_F3PtpNetPortFlowPointStatsValid_Object = MibTableColumn
f3PtpNetPortFlowPointStatsValid = _F3PtpNetPortFlowPointStatsValid_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 4, 1, 3),
    _F3PtpNetPortFlowPointStatsValid_Type()
)
f3PtpNetPortFlowPointStatsValid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpNetPortFlowPointStatsValid.setStatus("current")
_F3PtpNetPortFlowPointStatsAction_Type = CmPmBinAction
_F3PtpNetPortFlowPointStatsAction_Object = MibTableColumn
f3PtpNetPortFlowPointStatsAction = _F3PtpNetPortFlowPointStatsAction_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 4, 1, 4),
    _F3PtpNetPortFlowPointStatsAction_Type()
)
f3PtpNetPortFlowPointStatsAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3PtpNetPortFlowPointStatsAction.setStatus("current")
_F3PtpNetPortFlowPointStatsAnnouncesRx_Type = PerfCounter64
_F3PtpNetPortFlowPointStatsAnnouncesRx_Object = MibTableColumn
f3PtpNetPortFlowPointStatsAnnouncesRx = _F3PtpNetPortFlowPointStatsAnnouncesRx_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 4, 1, 5),
    _F3PtpNetPortFlowPointStatsAnnouncesRx_Type()
)
f3PtpNetPortFlowPointStatsAnnouncesRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpNetPortFlowPointStatsAnnouncesRx.setStatus("current")
_F3PtpNetPortFlowPointStatsAnnouncesTx_Type = PerfCounter64
_F3PtpNetPortFlowPointStatsAnnouncesTx_Object = MibTableColumn
f3PtpNetPortFlowPointStatsAnnouncesTx = _F3PtpNetPortFlowPointStatsAnnouncesTx_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 4, 1, 6),
    _F3PtpNetPortFlowPointStatsAnnouncesTx_Type()
)
f3PtpNetPortFlowPointStatsAnnouncesTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpNetPortFlowPointStatsAnnouncesTx.setStatus("current")
_F3PtpNetPortFlowPointStatsSyncsRx_Type = PerfCounter64
_F3PtpNetPortFlowPointStatsSyncsRx_Object = MibTableColumn
f3PtpNetPortFlowPointStatsSyncsRx = _F3PtpNetPortFlowPointStatsSyncsRx_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 4, 1, 7),
    _F3PtpNetPortFlowPointStatsSyncsRx_Type()
)
f3PtpNetPortFlowPointStatsSyncsRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpNetPortFlowPointStatsSyncsRx.setStatus("current")
_F3PtpNetPortFlowPointStatsSyncsTx_Type = PerfCounter64
_F3PtpNetPortFlowPointStatsSyncsTx_Object = MibTableColumn
f3PtpNetPortFlowPointStatsSyncsTx = _F3PtpNetPortFlowPointStatsSyncsTx_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 4, 1, 8),
    _F3PtpNetPortFlowPointStatsSyncsTx_Type()
)
f3PtpNetPortFlowPointStatsSyncsTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpNetPortFlowPointStatsSyncsTx.setStatus("current")
_F3PtpNetPortFlowPointStatsFollowupsRx_Type = PerfCounter64
_F3PtpNetPortFlowPointStatsFollowupsRx_Object = MibTableColumn
f3PtpNetPortFlowPointStatsFollowupsRx = _F3PtpNetPortFlowPointStatsFollowupsRx_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 4, 1, 9),
    _F3PtpNetPortFlowPointStatsFollowupsRx_Type()
)
f3PtpNetPortFlowPointStatsFollowupsRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpNetPortFlowPointStatsFollowupsRx.setStatus("current")
_F3PtpNetPortFlowPointStatsFollowupsTx_Type = PerfCounter64
_F3PtpNetPortFlowPointStatsFollowupsTx_Object = MibTableColumn
f3PtpNetPortFlowPointStatsFollowupsTx = _F3PtpNetPortFlowPointStatsFollowupsTx_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 4, 1, 10),
    _F3PtpNetPortFlowPointStatsFollowupsTx_Type()
)
f3PtpNetPortFlowPointStatsFollowupsTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpNetPortFlowPointStatsFollowupsTx.setStatus("current")
_F3PtpNetPortFlowPointStatsDelayReqsRx_Type = PerfCounter64
_F3PtpNetPortFlowPointStatsDelayReqsRx_Object = MibTableColumn
f3PtpNetPortFlowPointStatsDelayReqsRx = _F3PtpNetPortFlowPointStatsDelayReqsRx_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 4, 1, 11),
    _F3PtpNetPortFlowPointStatsDelayReqsRx_Type()
)
f3PtpNetPortFlowPointStatsDelayReqsRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpNetPortFlowPointStatsDelayReqsRx.setStatus("current")
_F3PtpNetPortFlowPointStatsDelayReqsTx_Type = PerfCounter64
_F3PtpNetPortFlowPointStatsDelayReqsTx_Object = MibTableColumn
f3PtpNetPortFlowPointStatsDelayReqsTx = _F3PtpNetPortFlowPointStatsDelayReqsTx_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 4, 1, 12),
    _F3PtpNetPortFlowPointStatsDelayReqsTx_Type()
)
f3PtpNetPortFlowPointStatsDelayReqsTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpNetPortFlowPointStatsDelayReqsTx.setStatus("current")
_F3PtpNetPortFlowPointStatsDelayRspsRx_Type = PerfCounter64
_F3PtpNetPortFlowPointStatsDelayRspsRx_Object = MibTableColumn
f3PtpNetPortFlowPointStatsDelayRspsRx = _F3PtpNetPortFlowPointStatsDelayRspsRx_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 4, 1, 13),
    _F3PtpNetPortFlowPointStatsDelayRspsRx_Type()
)
f3PtpNetPortFlowPointStatsDelayRspsRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpNetPortFlowPointStatsDelayRspsRx.setStatus("current")
_F3PtpNetPortFlowPointStatsDelayRspsTx_Type = PerfCounter64
_F3PtpNetPortFlowPointStatsDelayRspsTx_Object = MibTableColumn
f3PtpNetPortFlowPointStatsDelayRspsTx = _F3PtpNetPortFlowPointStatsDelayRspsTx_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 4, 1, 14),
    _F3PtpNetPortFlowPointStatsDelayRspsTx_Type()
)
f3PtpNetPortFlowPointStatsDelayRspsTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpNetPortFlowPointStatsDelayRspsTx.setStatus("current")
_F3PtpNetPortFlowPointStatsPDelayReqsRx_Type = PerfCounter64
_F3PtpNetPortFlowPointStatsPDelayReqsRx_Object = MibTableColumn
f3PtpNetPortFlowPointStatsPDelayReqsRx = _F3PtpNetPortFlowPointStatsPDelayReqsRx_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 4, 1, 15),
    _F3PtpNetPortFlowPointStatsPDelayReqsRx_Type()
)
f3PtpNetPortFlowPointStatsPDelayReqsRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpNetPortFlowPointStatsPDelayReqsRx.setStatus("current")
_F3PtpNetPortFlowPointStatsPDelayReqsTx_Type = PerfCounter64
_F3PtpNetPortFlowPointStatsPDelayReqsTx_Object = MibTableColumn
f3PtpNetPortFlowPointStatsPDelayReqsTx = _F3PtpNetPortFlowPointStatsPDelayReqsTx_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 4, 1, 16),
    _F3PtpNetPortFlowPointStatsPDelayReqsTx_Type()
)
f3PtpNetPortFlowPointStatsPDelayReqsTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpNetPortFlowPointStatsPDelayReqsTx.setStatus("current")
_F3PtpNetPortFlowPointStatsPDelayRspsRx_Type = PerfCounter64
_F3PtpNetPortFlowPointStatsPDelayRspsRx_Object = MibTableColumn
f3PtpNetPortFlowPointStatsPDelayRspsRx = _F3PtpNetPortFlowPointStatsPDelayRspsRx_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 4, 1, 17),
    _F3PtpNetPortFlowPointStatsPDelayRspsRx_Type()
)
f3PtpNetPortFlowPointStatsPDelayRspsRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpNetPortFlowPointStatsPDelayRspsRx.setStatus("current")
_F3PtpNetPortFlowPointStatsPDelayRspsTx_Type = PerfCounter64
_F3PtpNetPortFlowPointStatsPDelayRspsTx_Object = MibTableColumn
f3PtpNetPortFlowPointStatsPDelayRspsTx = _F3PtpNetPortFlowPointStatsPDelayRspsTx_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 4, 1, 18),
    _F3PtpNetPortFlowPointStatsPDelayRspsTx_Type()
)
f3PtpNetPortFlowPointStatsPDelayRspsTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpNetPortFlowPointStatsPDelayRspsTx.setStatus("current")
_F3PtpNetPortFlowPointStatsPDelayRspFollowupsRx_Type = PerfCounter64
_F3PtpNetPortFlowPointStatsPDelayRspFollowupsRx_Object = MibTableColumn
f3PtpNetPortFlowPointStatsPDelayRspFollowupsRx = _F3PtpNetPortFlowPointStatsPDelayRspFollowupsRx_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 4, 1, 19),
    _F3PtpNetPortFlowPointStatsPDelayRspFollowupsRx_Type()
)
f3PtpNetPortFlowPointStatsPDelayRspFollowupsRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpNetPortFlowPointStatsPDelayRspFollowupsRx.setStatus("current")
_F3PtpNetPortFlowPointStatsPDelayRspFollowupsTx_Type = PerfCounter64
_F3PtpNetPortFlowPointStatsPDelayRspFollowupsTx_Object = MibTableColumn
f3PtpNetPortFlowPointStatsPDelayRspFollowupsTx = _F3PtpNetPortFlowPointStatsPDelayRspFollowupsTx_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 4, 1, 20),
    _F3PtpNetPortFlowPointStatsPDelayRspFollowupsTx_Type()
)
f3PtpNetPortFlowPointStatsPDelayRspFollowupsTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpNetPortFlowPointStatsPDelayRspFollowupsTx.setStatus("current")
_F3PtpNetPortFlowPointStatsSignalingRx_Type = PerfCounter64
_F3PtpNetPortFlowPointStatsSignalingRx_Object = MibTableColumn
f3PtpNetPortFlowPointStatsSignalingRx = _F3PtpNetPortFlowPointStatsSignalingRx_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 4, 1, 21),
    _F3PtpNetPortFlowPointStatsSignalingRx_Type()
)
f3PtpNetPortFlowPointStatsSignalingRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpNetPortFlowPointStatsSignalingRx.setStatus("current")
_F3PtpNetPortFlowPointStatsSignalingTx_Type = PerfCounter64
_F3PtpNetPortFlowPointStatsSignalingTx_Object = MibTableColumn
f3PtpNetPortFlowPointStatsSignalingTx = _F3PtpNetPortFlowPointStatsSignalingTx_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 4, 1, 22),
    _F3PtpNetPortFlowPointStatsSignalingTx_Type()
)
f3PtpNetPortFlowPointStatsSignalingTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpNetPortFlowPointStatsSignalingTx.setStatus("current")
_F3PtpNetPortFlowPointStatsMgmtFramesRx_Type = PerfCounter64
_F3PtpNetPortFlowPointStatsMgmtFramesRx_Object = MibTableColumn
f3PtpNetPortFlowPointStatsMgmtFramesRx = _F3PtpNetPortFlowPointStatsMgmtFramesRx_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 4, 1, 23),
    _F3PtpNetPortFlowPointStatsMgmtFramesRx_Type()
)
f3PtpNetPortFlowPointStatsMgmtFramesRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpNetPortFlowPointStatsMgmtFramesRx.setStatus("current")
_F3PtpNetPortFlowPointStatsMgmtFramesTx_Type = PerfCounter64
_F3PtpNetPortFlowPointStatsMgmtFramesTx_Object = MibTableColumn
f3PtpNetPortFlowPointStatsMgmtFramesTx = _F3PtpNetPortFlowPointStatsMgmtFramesTx_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 4, 1, 24),
    _F3PtpNetPortFlowPointStatsMgmtFramesTx_Type()
)
f3PtpNetPortFlowPointStatsMgmtFramesTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpNetPortFlowPointStatsMgmtFramesTx.setStatus("current")
_F3PtpNetPortFlowPointStatsPtpUnknownsRx_Type = PerfCounter64
_F3PtpNetPortFlowPointStatsPtpUnknownsRx_Object = MibTableColumn
f3PtpNetPortFlowPointStatsPtpUnknownsRx = _F3PtpNetPortFlowPointStatsPtpUnknownsRx_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 4, 1, 25),
    _F3PtpNetPortFlowPointStatsPtpUnknownsRx_Type()
)
f3PtpNetPortFlowPointStatsPtpUnknownsRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpNetPortFlowPointStatsPtpUnknownsRx.setStatus("current")
_F3PtpNetPortFlowPointStatsPtpUnknownsTx_Type = PerfCounter64
_F3PtpNetPortFlowPointStatsPtpUnknownsTx_Object = MibTableColumn
f3PtpNetPortFlowPointStatsPtpUnknownsTx = _F3PtpNetPortFlowPointStatsPtpUnknownsTx_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 4, 1, 26),
    _F3PtpNetPortFlowPointStatsPtpUnknownsTx_Type()
)
f3PtpNetPortFlowPointStatsPtpUnknownsTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpNetPortFlowPointStatsPtpUnknownsTx.setStatus("current")
_F3PtpNetPortFlowPointStatsAvgSyncResTime_Type = Unsigned32
_F3PtpNetPortFlowPointStatsAvgSyncResTime_Object = MibTableColumn
f3PtpNetPortFlowPointStatsAvgSyncResTime = _F3PtpNetPortFlowPointStatsAvgSyncResTime_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 4, 1, 27),
    _F3PtpNetPortFlowPointStatsAvgSyncResTime_Type()
)
f3PtpNetPortFlowPointStatsAvgSyncResTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpNetPortFlowPointStatsAvgSyncResTime.setStatus("deprecated")
_F3PtpNetPortFlowPointStatsMinSyncResTime_Type = Unsigned32
_F3PtpNetPortFlowPointStatsMinSyncResTime_Object = MibTableColumn
f3PtpNetPortFlowPointStatsMinSyncResTime = _F3PtpNetPortFlowPointStatsMinSyncResTime_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 4, 1, 28),
    _F3PtpNetPortFlowPointStatsMinSyncResTime_Type()
)
f3PtpNetPortFlowPointStatsMinSyncResTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpNetPortFlowPointStatsMinSyncResTime.setStatus("deprecated")
_F3PtpNetPortFlowPointStatsMaxSyncResTime_Type = Unsigned32
_F3PtpNetPortFlowPointStatsMaxSyncResTime_Object = MibTableColumn
f3PtpNetPortFlowPointStatsMaxSyncResTime = _F3PtpNetPortFlowPointStatsMaxSyncResTime_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 4, 1, 29),
    _F3PtpNetPortFlowPointStatsMaxSyncResTime_Type()
)
f3PtpNetPortFlowPointStatsMaxSyncResTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpNetPortFlowPointStatsMaxSyncResTime.setStatus("deprecated")
_F3PtpNetPortFlowPointStatsAvgDelayReqResTime_Type = Unsigned32
_F3PtpNetPortFlowPointStatsAvgDelayReqResTime_Object = MibTableColumn
f3PtpNetPortFlowPointStatsAvgDelayReqResTime = _F3PtpNetPortFlowPointStatsAvgDelayReqResTime_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 4, 1, 30),
    _F3PtpNetPortFlowPointStatsAvgDelayReqResTime_Type()
)
f3PtpNetPortFlowPointStatsAvgDelayReqResTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpNetPortFlowPointStatsAvgDelayReqResTime.setStatus("deprecated")
_F3PtpNetPortFlowPointStatsMinDelayReqResTime_Type = Unsigned32
_F3PtpNetPortFlowPointStatsMinDelayReqResTime_Object = MibTableColumn
f3PtpNetPortFlowPointStatsMinDelayReqResTime = _F3PtpNetPortFlowPointStatsMinDelayReqResTime_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 4, 1, 31),
    _F3PtpNetPortFlowPointStatsMinDelayReqResTime_Type()
)
f3PtpNetPortFlowPointStatsMinDelayReqResTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpNetPortFlowPointStatsMinDelayReqResTime.setStatus("deprecated")
_F3PtpNetPortFlowPointStatsMaxDelayReqResTime_Type = Unsigned32
_F3PtpNetPortFlowPointStatsMaxDelayReqResTime_Object = MibTableColumn
f3PtpNetPortFlowPointStatsMaxDelayReqResTime = _F3PtpNetPortFlowPointStatsMaxDelayReqResTime_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 4, 1, 32),
    _F3PtpNetPortFlowPointStatsMaxDelayReqResTime_Type()
)
f3PtpNetPortFlowPointStatsMaxDelayReqResTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpNetPortFlowPointStatsMaxDelayReqResTime.setStatus("deprecated")
_F3PtpNetPortFlowPointStatsMinPDelayReqResTime_Type = Unsigned32
_F3PtpNetPortFlowPointStatsMinPDelayReqResTime_Object = MibTableColumn
f3PtpNetPortFlowPointStatsMinPDelayReqResTime = _F3PtpNetPortFlowPointStatsMinPDelayReqResTime_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 4, 1, 33),
    _F3PtpNetPortFlowPointStatsMinPDelayReqResTime_Type()
)
f3PtpNetPortFlowPointStatsMinPDelayReqResTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpNetPortFlowPointStatsMinPDelayReqResTime.setStatus("deprecated")
_F3PtpNetPortFlowPointStatsMaxPDelayReqResTime_Type = Unsigned32
_F3PtpNetPortFlowPointStatsMaxPDelayReqResTime_Object = MibTableColumn
f3PtpNetPortFlowPointStatsMaxPDelayReqResTime = _F3PtpNetPortFlowPointStatsMaxPDelayReqResTime_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 4, 1, 34),
    _F3PtpNetPortFlowPointStatsMaxPDelayReqResTime_Type()
)
f3PtpNetPortFlowPointStatsMaxPDelayReqResTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpNetPortFlowPointStatsMaxPDelayReqResTime.setStatus("deprecated")
_F3PtpNetPortFlowPointStatsAvgPDelayReqResTime_Type = Unsigned32
_F3PtpNetPortFlowPointStatsAvgPDelayReqResTime_Object = MibTableColumn
f3PtpNetPortFlowPointStatsAvgPDelayReqResTime = _F3PtpNetPortFlowPointStatsAvgPDelayReqResTime_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 4, 1, 35),
    _F3PtpNetPortFlowPointStatsAvgPDelayReqResTime_Type()
)
f3PtpNetPortFlowPointStatsAvgPDelayReqResTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpNetPortFlowPointStatsAvgPDelayReqResTime.setStatus("deprecated")
_F3PtpNetPortFlowPointStatsMinPDelayRspResTime_Type = Unsigned32
_F3PtpNetPortFlowPointStatsMinPDelayRspResTime_Object = MibTableColumn
f3PtpNetPortFlowPointStatsMinPDelayRspResTime = _F3PtpNetPortFlowPointStatsMinPDelayRspResTime_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 4, 1, 36),
    _F3PtpNetPortFlowPointStatsMinPDelayRspResTime_Type()
)
f3PtpNetPortFlowPointStatsMinPDelayRspResTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpNetPortFlowPointStatsMinPDelayRspResTime.setStatus("deprecated")
_F3PtpNetPortFlowPointStatsMaxPDelayRspResTime_Type = Unsigned32
_F3PtpNetPortFlowPointStatsMaxPDelayRspResTime_Object = MibTableColumn
f3PtpNetPortFlowPointStatsMaxPDelayRspResTime = _F3PtpNetPortFlowPointStatsMaxPDelayRspResTime_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 4, 1, 37),
    _F3PtpNetPortFlowPointStatsMaxPDelayRspResTime_Type()
)
f3PtpNetPortFlowPointStatsMaxPDelayRspResTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpNetPortFlowPointStatsMaxPDelayRspResTime.setStatus("deprecated")
_F3PtpNetPortFlowPointStatsAvgPDelayRspResTime_Type = Unsigned32
_F3PtpNetPortFlowPointStatsAvgPDelayRspResTime_Object = MibTableColumn
f3PtpNetPortFlowPointStatsAvgPDelayRspResTime = _F3PtpNetPortFlowPointStatsAvgPDelayRspResTime_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 4, 1, 38),
    _F3PtpNetPortFlowPointStatsAvgPDelayRspResTime_Type()
)
f3PtpNetPortFlowPointStatsAvgPDelayRspResTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpNetPortFlowPointStatsAvgPDelayRspResTime.setStatus("deprecated")
_F3PtpNetPortFlowPointStatsDestMciNoMatchDiscards_Type = PerfCounter64
_F3PtpNetPortFlowPointStatsDestMciNoMatchDiscards_Object = MibTableColumn
f3PtpNetPortFlowPointStatsDestMciNoMatchDiscards = _F3PtpNetPortFlowPointStatsDestMciNoMatchDiscards_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 4, 1, 39),
    _F3PtpNetPortFlowPointStatsDestMciNoMatchDiscards_Type()
)
f3PtpNetPortFlowPointStatsDestMciNoMatchDiscards.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3PtpNetPortFlowPointStatsDestMciNoMatchDiscards.setStatus("current")
_F3PtpNetPortFlowPointStatsTagNoMatchDiscards_Type = PerfCounter64
_F3PtpNetPortFlowPointStatsTagNoMatchDiscards_Object = MibTableColumn
f3PtpNetPortFlowPointStatsTagNoMatchDiscards = _F3PtpNetPortFlowPointStatsTagNoMatchDiscards_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 4, 1, 40),
    _F3PtpNetPortFlowPointStatsTagNoMatchDiscards_Type()
)
f3PtpNetPortFlowPointStatsTagNoMatchDiscards.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3PtpNetPortFlowPointStatsTagNoMatchDiscards.setStatus("current")
_F3PtpNetPortFlowPointHistoryTable_Object = MibTable
f3PtpNetPortFlowPointHistoryTable = _F3PtpNetPortFlowPointHistoryTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 5)
)
if mibBuilder.loadTexts:
    f3PtpNetPortFlowPointHistoryTable.setStatus("current")
_F3PtpNetPortFlowPointHistoryEntry_Object = MibTableRow
f3PtpNetPortFlowPointHistoryEntry = _F3PtpNetPortFlowPointHistoryEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 5, 1)
)
f3PtpNetPortFlowPointHistoryEntry.setIndexNames(
    (0, "CM-ENTITY-MIB", "neIndex"),
    (0, "CM-ENTITY-MIB", "shelfIndex"),
    (0, "CM-ENTITY-MIB", "slotIndex"),
    (0, "CM-FACILITY-MIB", "cmEthernetNetPortIndex"),
    (0, "F3-PTP-MIB", "f3PtpNetPortFlowPointIndex"),
    (0, "F3-PTP-MIB", "f3PtpNetPortFlowPointStatsIndex"),
    (0, "F3-PTP-MIB", "f3PtpNetPortFlowPointHistoryIndex"),
)
if mibBuilder.loadTexts:
    f3PtpNetPortFlowPointHistoryEntry.setStatus("current")


class _F3PtpNetPortFlowPointHistoryIndex_Type(Integer32):
    """Custom type f3PtpNetPortFlowPointHistoryIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_F3PtpNetPortFlowPointHistoryIndex_Type.__name__ = "Integer32"
_F3PtpNetPortFlowPointHistoryIndex_Object = MibTableColumn
f3PtpNetPortFlowPointHistoryIndex = _F3PtpNetPortFlowPointHistoryIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 5, 1, 1),
    _F3PtpNetPortFlowPointHistoryIndex_Type()
)
f3PtpNetPortFlowPointHistoryIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    f3PtpNetPortFlowPointHistoryIndex.setStatus("current")
_F3PtpNetPortFlowPointHistoryTime_Type = DateAndTime
_F3PtpNetPortFlowPointHistoryTime_Object = MibTableColumn
f3PtpNetPortFlowPointHistoryTime = _F3PtpNetPortFlowPointHistoryTime_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 5, 1, 2),
    _F3PtpNetPortFlowPointHistoryTime_Type()
)
f3PtpNetPortFlowPointHistoryTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpNetPortFlowPointHistoryTime.setStatus("current")
_F3PtpNetPortFlowPointHistoryValid_Type = TruthValue
_F3PtpNetPortFlowPointHistoryValid_Object = MibTableColumn
f3PtpNetPortFlowPointHistoryValid = _F3PtpNetPortFlowPointHistoryValid_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 5, 1, 3),
    _F3PtpNetPortFlowPointHistoryValid_Type()
)
f3PtpNetPortFlowPointHistoryValid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpNetPortFlowPointHistoryValid.setStatus("current")
_F3PtpNetPortFlowPointHistoryAction_Type = CmPmBinAction
_F3PtpNetPortFlowPointHistoryAction_Object = MibTableColumn
f3PtpNetPortFlowPointHistoryAction = _F3PtpNetPortFlowPointHistoryAction_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 5, 1, 4),
    _F3PtpNetPortFlowPointHistoryAction_Type()
)
f3PtpNetPortFlowPointHistoryAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3PtpNetPortFlowPointHistoryAction.setStatus("current")
_F3PtpNetPortFlowPointHistoryAnnouncesRx_Type = PerfCounter64
_F3PtpNetPortFlowPointHistoryAnnouncesRx_Object = MibTableColumn
f3PtpNetPortFlowPointHistoryAnnouncesRx = _F3PtpNetPortFlowPointHistoryAnnouncesRx_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 5, 1, 5),
    _F3PtpNetPortFlowPointHistoryAnnouncesRx_Type()
)
f3PtpNetPortFlowPointHistoryAnnouncesRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpNetPortFlowPointHistoryAnnouncesRx.setStatus("current")
_F3PtpNetPortFlowPointHistoryAnnouncesTx_Type = PerfCounter64
_F3PtpNetPortFlowPointHistoryAnnouncesTx_Object = MibTableColumn
f3PtpNetPortFlowPointHistoryAnnouncesTx = _F3PtpNetPortFlowPointHistoryAnnouncesTx_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 5, 1, 6),
    _F3PtpNetPortFlowPointHistoryAnnouncesTx_Type()
)
f3PtpNetPortFlowPointHistoryAnnouncesTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpNetPortFlowPointHistoryAnnouncesTx.setStatus("current")
_F3PtpNetPortFlowPointHistorySyncsRx_Type = PerfCounter64
_F3PtpNetPortFlowPointHistorySyncsRx_Object = MibTableColumn
f3PtpNetPortFlowPointHistorySyncsRx = _F3PtpNetPortFlowPointHistorySyncsRx_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 5, 1, 7),
    _F3PtpNetPortFlowPointHistorySyncsRx_Type()
)
f3PtpNetPortFlowPointHistorySyncsRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpNetPortFlowPointHistorySyncsRx.setStatus("current")
_F3PtpNetPortFlowPointHistorySyncsTx_Type = PerfCounter64
_F3PtpNetPortFlowPointHistorySyncsTx_Object = MibTableColumn
f3PtpNetPortFlowPointHistorySyncsTx = _F3PtpNetPortFlowPointHistorySyncsTx_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 5, 1, 8),
    _F3PtpNetPortFlowPointHistorySyncsTx_Type()
)
f3PtpNetPortFlowPointHistorySyncsTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpNetPortFlowPointHistorySyncsTx.setStatus("current")
_F3PtpNetPortFlowPointHistoryFollowupsRx_Type = PerfCounter64
_F3PtpNetPortFlowPointHistoryFollowupsRx_Object = MibTableColumn
f3PtpNetPortFlowPointHistoryFollowupsRx = _F3PtpNetPortFlowPointHistoryFollowupsRx_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 5, 1, 9),
    _F3PtpNetPortFlowPointHistoryFollowupsRx_Type()
)
f3PtpNetPortFlowPointHistoryFollowupsRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpNetPortFlowPointHistoryFollowupsRx.setStatus("current")
_F3PtpNetPortFlowPointHistoryFollowupsTx_Type = PerfCounter64
_F3PtpNetPortFlowPointHistoryFollowupsTx_Object = MibTableColumn
f3PtpNetPortFlowPointHistoryFollowupsTx = _F3PtpNetPortFlowPointHistoryFollowupsTx_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 5, 1, 10),
    _F3PtpNetPortFlowPointHistoryFollowupsTx_Type()
)
f3PtpNetPortFlowPointHistoryFollowupsTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpNetPortFlowPointHistoryFollowupsTx.setStatus("current")
_F3PtpNetPortFlowPointHistoryDelayReqsRx_Type = PerfCounter64
_F3PtpNetPortFlowPointHistoryDelayReqsRx_Object = MibTableColumn
f3PtpNetPortFlowPointHistoryDelayReqsRx = _F3PtpNetPortFlowPointHistoryDelayReqsRx_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 5, 1, 11),
    _F3PtpNetPortFlowPointHistoryDelayReqsRx_Type()
)
f3PtpNetPortFlowPointHistoryDelayReqsRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpNetPortFlowPointHistoryDelayReqsRx.setStatus("current")
_F3PtpNetPortFlowPointHistoryDelayReqsTx_Type = PerfCounter64
_F3PtpNetPortFlowPointHistoryDelayReqsTx_Object = MibTableColumn
f3PtpNetPortFlowPointHistoryDelayReqsTx = _F3PtpNetPortFlowPointHistoryDelayReqsTx_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 5, 1, 12),
    _F3PtpNetPortFlowPointHistoryDelayReqsTx_Type()
)
f3PtpNetPortFlowPointHistoryDelayReqsTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpNetPortFlowPointHistoryDelayReqsTx.setStatus("current")
_F3PtpNetPortFlowPointHistoryDelayRspsRx_Type = PerfCounter64
_F3PtpNetPortFlowPointHistoryDelayRspsRx_Object = MibTableColumn
f3PtpNetPortFlowPointHistoryDelayRspsRx = _F3PtpNetPortFlowPointHistoryDelayRspsRx_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 5, 1, 13),
    _F3PtpNetPortFlowPointHistoryDelayRspsRx_Type()
)
f3PtpNetPortFlowPointHistoryDelayRspsRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpNetPortFlowPointHistoryDelayRspsRx.setStatus("current")
_F3PtpNetPortFlowPointHistoryDelayRspsTx_Type = PerfCounter64
_F3PtpNetPortFlowPointHistoryDelayRspsTx_Object = MibTableColumn
f3PtpNetPortFlowPointHistoryDelayRspsTx = _F3PtpNetPortFlowPointHistoryDelayRspsTx_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 5, 1, 14),
    _F3PtpNetPortFlowPointHistoryDelayRspsTx_Type()
)
f3PtpNetPortFlowPointHistoryDelayRspsTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpNetPortFlowPointHistoryDelayRspsTx.setStatus("current")
_F3PtpNetPortFlowPointHistoryPDelayReqsRx_Type = PerfCounter64
_F3PtpNetPortFlowPointHistoryPDelayReqsRx_Object = MibTableColumn
f3PtpNetPortFlowPointHistoryPDelayReqsRx = _F3PtpNetPortFlowPointHistoryPDelayReqsRx_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 5, 1, 15),
    _F3PtpNetPortFlowPointHistoryPDelayReqsRx_Type()
)
f3PtpNetPortFlowPointHistoryPDelayReqsRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpNetPortFlowPointHistoryPDelayReqsRx.setStatus("current")
_F3PtpNetPortFlowPointHistoryPDelayReqsTx_Type = PerfCounter64
_F3PtpNetPortFlowPointHistoryPDelayReqsTx_Object = MibTableColumn
f3PtpNetPortFlowPointHistoryPDelayReqsTx = _F3PtpNetPortFlowPointHistoryPDelayReqsTx_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 5, 1, 16),
    _F3PtpNetPortFlowPointHistoryPDelayReqsTx_Type()
)
f3PtpNetPortFlowPointHistoryPDelayReqsTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpNetPortFlowPointHistoryPDelayReqsTx.setStatus("current")
_F3PtpNetPortFlowPointHistoryPDelayRspsRx_Type = PerfCounter64
_F3PtpNetPortFlowPointHistoryPDelayRspsRx_Object = MibTableColumn
f3PtpNetPortFlowPointHistoryPDelayRspsRx = _F3PtpNetPortFlowPointHistoryPDelayRspsRx_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 5, 1, 17),
    _F3PtpNetPortFlowPointHistoryPDelayRspsRx_Type()
)
f3PtpNetPortFlowPointHistoryPDelayRspsRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpNetPortFlowPointHistoryPDelayRspsRx.setStatus("current")
_F3PtpNetPortFlowPointHistoryPDelayRspsTx_Type = PerfCounter64
_F3PtpNetPortFlowPointHistoryPDelayRspsTx_Object = MibTableColumn
f3PtpNetPortFlowPointHistoryPDelayRspsTx = _F3PtpNetPortFlowPointHistoryPDelayRspsTx_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 5, 1, 18),
    _F3PtpNetPortFlowPointHistoryPDelayRspsTx_Type()
)
f3PtpNetPortFlowPointHistoryPDelayRspsTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpNetPortFlowPointHistoryPDelayRspsTx.setStatus("current")
_F3PtpNetPortFlowPointHistoryPDelayRspFollowupsRx_Type = PerfCounter64
_F3PtpNetPortFlowPointHistoryPDelayRspFollowupsRx_Object = MibTableColumn
f3PtpNetPortFlowPointHistoryPDelayRspFollowupsRx = _F3PtpNetPortFlowPointHistoryPDelayRspFollowupsRx_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 5, 1, 19),
    _F3PtpNetPortFlowPointHistoryPDelayRspFollowupsRx_Type()
)
f3PtpNetPortFlowPointHistoryPDelayRspFollowupsRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpNetPortFlowPointHistoryPDelayRspFollowupsRx.setStatus("current")
_F3PtpNetPortFlowPointHistoryPDelayRspFollowupsTx_Type = PerfCounter64
_F3PtpNetPortFlowPointHistoryPDelayRspFollowupsTx_Object = MibTableColumn
f3PtpNetPortFlowPointHistoryPDelayRspFollowupsTx = _F3PtpNetPortFlowPointHistoryPDelayRspFollowupsTx_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 5, 1, 20),
    _F3PtpNetPortFlowPointHistoryPDelayRspFollowupsTx_Type()
)
f3PtpNetPortFlowPointHistoryPDelayRspFollowupsTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpNetPortFlowPointHistoryPDelayRspFollowupsTx.setStatus("current")
_F3PtpNetPortFlowPointHistorySignalingRx_Type = PerfCounter64
_F3PtpNetPortFlowPointHistorySignalingRx_Object = MibTableColumn
f3PtpNetPortFlowPointHistorySignalingRx = _F3PtpNetPortFlowPointHistorySignalingRx_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 5, 1, 21),
    _F3PtpNetPortFlowPointHistorySignalingRx_Type()
)
f3PtpNetPortFlowPointHistorySignalingRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpNetPortFlowPointHistorySignalingRx.setStatus("current")
_F3PtpNetPortFlowPointHistorySignalingTx_Type = PerfCounter64
_F3PtpNetPortFlowPointHistorySignalingTx_Object = MibTableColumn
f3PtpNetPortFlowPointHistorySignalingTx = _F3PtpNetPortFlowPointHistorySignalingTx_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 5, 1, 22),
    _F3PtpNetPortFlowPointHistorySignalingTx_Type()
)
f3PtpNetPortFlowPointHistorySignalingTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpNetPortFlowPointHistorySignalingTx.setStatus("current")
_F3PtpNetPortFlowPointHistoryMgmtFramesRx_Type = PerfCounter64
_F3PtpNetPortFlowPointHistoryMgmtFramesRx_Object = MibTableColumn
f3PtpNetPortFlowPointHistoryMgmtFramesRx = _F3PtpNetPortFlowPointHistoryMgmtFramesRx_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 5, 1, 23),
    _F3PtpNetPortFlowPointHistoryMgmtFramesRx_Type()
)
f3PtpNetPortFlowPointHistoryMgmtFramesRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpNetPortFlowPointHistoryMgmtFramesRx.setStatus("current")
_F3PtpNetPortFlowPointHistoryMgmtFramesTx_Type = PerfCounter64
_F3PtpNetPortFlowPointHistoryMgmtFramesTx_Object = MibTableColumn
f3PtpNetPortFlowPointHistoryMgmtFramesTx = _F3PtpNetPortFlowPointHistoryMgmtFramesTx_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 5, 1, 24),
    _F3PtpNetPortFlowPointHistoryMgmtFramesTx_Type()
)
f3PtpNetPortFlowPointHistoryMgmtFramesTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpNetPortFlowPointHistoryMgmtFramesTx.setStatus("current")
_F3PtpNetPortFlowPointHistoryPtpUnknownsRx_Type = PerfCounter64
_F3PtpNetPortFlowPointHistoryPtpUnknownsRx_Object = MibTableColumn
f3PtpNetPortFlowPointHistoryPtpUnknownsRx = _F3PtpNetPortFlowPointHistoryPtpUnknownsRx_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 5, 1, 25),
    _F3PtpNetPortFlowPointHistoryPtpUnknownsRx_Type()
)
f3PtpNetPortFlowPointHistoryPtpUnknownsRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpNetPortFlowPointHistoryPtpUnknownsRx.setStatus("current")
_F3PtpNetPortFlowPointHistoryPtpUnknownsTx_Type = PerfCounter64
_F3PtpNetPortFlowPointHistoryPtpUnknownsTx_Object = MibTableColumn
f3PtpNetPortFlowPointHistoryPtpUnknownsTx = _F3PtpNetPortFlowPointHistoryPtpUnknownsTx_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 5, 1, 26),
    _F3PtpNetPortFlowPointHistoryPtpUnknownsTx_Type()
)
f3PtpNetPortFlowPointHistoryPtpUnknownsTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpNetPortFlowPointHistoryPtpUnknownsTx.setStatus("current")
_F3PtpNetPortFlowPointHistoryAvgSyncResTime_Type = Unsigned32
_F3PtpNetPortFlowPointHistoryAvgSyncResTime_Object = MibTableColumn
f3PtpNetPortFlowPointHistoryAvgSyncResTime = _F3PtpNetPortFlowPointHistoryAvgSyncResTime_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 5, 1, 27),
    _F3PtpNetPortFlowPointHistoryAvgSyncResTime_Type()
)
f3PtpNetPortFlowPointHistoryAvgSyncResTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpNetPortFlowPointHistoryAvgSyncResTime.setStatus("deprecated")
_F3PtpNetPortFlowPointHistoryMinSyncResTime_Type = Unsigned32
_F3PtpNetPortFlowPointHistoryMinSyncResTime_Object = MibTableColumn
f3PtpNetPortFlowPointHistoryMinSyncResTime = _F3PtpNetPortFlowPointHistoryMinSyncResTime_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 5, 1, 28),
    _F3PtpNetPortFlowPointHistoryMinSyncResTime_Type()
)
f3PtpNetPortFlowPointHistoryMinSyncResTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpNetPortFlowPointHistoryMinSyncResTime.setStatus("deprecated")
_F3PtpNetPortFlowPointHistoryMaxSyncResTime_Type = Unsigned32
_F3PtpNetPortFlowPointHistoryMaxSyncResTime_Object = MibTableColumn
f3PtpNetPortFlowPointHistoryMaxSyncResTime = _F3PtpNetPortFlowPointHistoryMaxSyncResTime_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 5, 1, 29),
    _F3PtpNetPortFlowPointHistoryMaxSyncResTime_Type()
)
f3PtpNetPortFlowPointHistoryMaxSyncResTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpNetPortFlowPointHistoryMaxSyncResTime.setStatus("deprecated")
_F3PtpNetPortFlowPointHistoryAvgDelayReqResTime_Type = Unsigned32
_F3PtpNetPortFlowPointHistoryAvgDelayReqResTime_Object = MibTableColumn
f3PtpNetPortFlowPointHistoryAvgDelayReqResTime = _F3PtpNetPortFlowPointHistoryAvgDelayReqResTime_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 5, 1, 30),
    _F3PtpNetPortFlowPointHistoryAvgDelayReqResTime_Type()
)
f3PtpNetPortFlowPointHistoryAvgDelayReqResTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpNetPortFlowPointHistoryAvgDelayReqResTime.setStatus("deprecated")
_F3PtpNetPortFlowPointHistoryMinDelayReqResTime_Type = Unsigned32
_F3PtpNetPortFlowPointHistoryMinDelayReqResTime_Object = MibTableColumn
f3PtpNetPortFlowPointHistoryMinDelayReqResTime = _F3PtpNetPortFlowPointHistoryMinDelayReqResTime_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 5, 1, 31),
    _F3PtpNetPortFlowPointHistoryMinDelayReqResTime_Type()
)
f3PtpNetPortFlowPointHistoryMinDelayReqResTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpNetPortFlowPointHistoryMinDelayReqResTime.setStatus("deprecated")
_F3PtpNetPortFlowPointHistoryMaxDelayReqResTime_Type = Unsigned32
_F3PtpNetPortFlowPointHistoryMaxDelayReqResTime_Object = MibTableColumn
f3PtpNetPortFlowPointHistoryMaxDelayReqResTime = _F3PtpNetPortFlowPointHistoryMaxDelayReqResTime_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 5, 1, 32),
    _F3PtpNetPortFlowPointHistoryMaxDelayReqResTime_Type()
)
f3PtpNetPortFlowPointHistoryMaxDelayReqResTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpNetPortFlowPointHistoryMaxDelayReqResTime.setStatus("deprecated")
_F3PtpNetPortFlowPointHistoryMinPDelayReqResTime_Type = Unsigned32
_F3PtpNetPortFlowPointHistoryMinPDelayReqResTime_Object = MibTableColumn
f3PtpNetPortFlowPointHistoryMinPDelayReqResTime = _F3PtpNetPortFlowPointHistoryMinPDelayReqResTime_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 5, 1, 33),
    _F3PtpNetPortFlowPointHistoryMinPDelayReqResTime_Type()
)
f3PtpNetPortFlowPointHistoryMinPDelayReqResTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpNetPortFlowPointHistoryMinPDelayReqResTime.setStatus("deprecated")
_F3PtpNetPortFlowPointHistoryMaxPDelayReqResTime_Type = Unsigned32
_F3PtpNetPortFlowPointHistoryMaxPDelayReqResTime_Object = MibTableColumn
f3PtpNetPortFlowPointHistoryMaxPDelayReqResTime = _F3PtpNetPortFlowPointHistoryMaxPDelayReqResTime_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 5, 1, 34),
    _F3PtpNetPortFlowPointHistoryMaxPDelayReqResTime_Type()
)
f3PtpNetPortFlowPointHistoryMaxPDelayReqResTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpNetPortFlowPointHistoryMaxPDelayReqResTime.setStatus("deprecated")
_F3PtpNetPortFlowPointHistoryAvgPDelayReqResTime_Type = Unsigned32
_F3PtpNetPortFlowPointHistoryAvgPDelayReqResTime_Object = MibTableColumn
f3PtpNetPortFlowPointHistoryAvgPDelayReqResTime = _F3PtpNetPortFlowPointHistoryAvgPDelayReqResTime_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 5, 1, 35),
    _F3PtpNetPortFlowPointHistoryAvgPDelayReqResTime_Type()
)
f3PtpNetPortFlowPointHistoryAvgPDelayReqResTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpNetPortFlowPointHistoryAvgPDelayReqResTime.setStatus("deprecated")
_F3PtpNetPortFlowPointHistoryMinPDelayRspResTime_Type = Unsigned32
_F3PtpNetPortFlowPointHistoryMinPDelayRspResTime_Object = MibTableColumn
f3PtpNetPortFlowPointHistoryMinPDelayRspResTime = _F3PtpNetPortFlowPointHistoryMinPDelayRspResTime_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 5, 1, 36),
    _F3PtpNetPortFlowPointHistoryMinPDelayRspResTime_Type()
)
f3PtpNetPortFlowPointHistoryMinPDelayRspResTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpNetPortFlowPointHistoryMinPDelayRspResTime.setStatus("deprecated")
_F3PtpNetPortFlowPointHistoryMaxPDelayRspResTime_Type = Unsigned32
_F3PtpNetPortFlowPointHistoryMaxPDelayRspResTime_Object = MibTableColumn
f3PtpNetPortFlowPointHistoryMaxPDelayRspResTime = _F3PtpNetPortFlowPointHistoryMaxPDelayRspResTime_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 5, 1, 37),
    _F3PtpNetPortFlowPointHistoryMaxPDelayRspResTime_Type()
)
f3PtpNetPortFlowPointHistoryMaxPDelayRspResTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpNetPortFlowPointHistoryMaxPDelayRspResTime.setStatus("deprecated")
_F3PtpNetPortFlowPointHistoryAvgPDelayRspResTime_Type = Unsigned32
_F3PtpNetPortFlowPointHistoryAvgPDelayRspResTime_Object = MibTableColumn
f3PtpNetPortFlowPointHistoryAvgPDelayRspResTime = _F3PtpNetPortFlowPointHistoryAvgPDelayRspResTime_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 5, 1, 38),
    _F3PtpNetPortFlowPointHistoryAvgPDelayRspResTime_Type()
)
f3PtpNetPortFlowPointHistoryAvgPDelayRspResTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpNetPortFlowPointHistoryAvgPDelayRspResTime.setStatus("deprecated")
_F3PtpNetPortFlowPointHistoryDestMciNoMatchDiscards_Type = PerfCounter64
_F3PtpNetPortFlowPointHistoryDestMciNoMatchDiscards_Object = MibTableColumn
f3PtpNetPortFlowPointHistoryDestMciNoMatchDiscards = _F3PtpNetPortFlowPointHistoryDestMciNoMatchDiscards_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 5, 1, 39),
    _F3PtpNetPortFlowPointHistoryDestMciNoMatchDiscards_Type()
)
f3PtpNetPortFlowPointHistoryDestMciNoMatchDiscards.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3PtpNetPortFlowPointHistoryDestMciNoMatchDiscards.setStatus("current")
_F3PtpNetPortFlowPointHistoryTagNoMatchDiscards_Type = PerfCounter64
_F3PtpNetPortFlowPointHistoryTagNoMatchDiscards_Object = MibTableColumn
f3PtpNetPortFlowPointHistoryTagNoMatchDiscards = _F3PtpNetPortFlowPointHistoryTagNoMatchDiscards_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 5, 1, 40),
    _F3PtpNetPortFlowPointHistoryTagNoMatchDiscards_Type()
)
f3PtpNetPortFlowPointHistoryTagNoMatchDiscards.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3PtpNetPortFlowPointHistoryTagNoMatchDiscards.setStatus("current")
_F3PtpNetPortFlowPointThresholdTable_Object = MibTable
f3PtpNetPortFlowPointThresholdTable = _F3PtpNetPortFlowPointThresholdTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 6)
)
if mibBuilder.loadTexts:
    f3PtpNetPortFlowPointThresholdTable.setStatus("current")
_F3PtpNetPortFlowPointThresholdEntry_Object = MibTableRow
f3PtpNetPortFlowPointThresholdEntry = _F3PtpNetPortFlowPointThresholdEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 6, 1)
)
f3PtpNetPortFlowPointThresholdEntry.setIndexNames(
    (0, "CM-ENTITY-MIB", "neIndex"),
    (0, "CM-ENTITY-MIB", "shelfIndex"),
    (0, "CM-ENTITY-MIB", "slotIndex"),
    (0, "CM-FACILITY-MIB", "cmEthernetNetPortIndex"),
    (0, "F3-PTP-MIB", "f3PtpNetPortFlowPointIndex"),
    (0, "F3-PTP-MIB", "f3PtpNetPortFlowPointStatsIndex"),
    (0, "F3-PTP-MIB", "f3PtpNetPortFlowPointThresholdIndex"),
)
if mibBuilder.loadTexts:
    f3PtpNetPortFlowPointThresholdEntry.setStatus("current")


class _F3PtpNetPortFlowPointThresholdIndex_Type(Integer32):
    """Custom type f3PtpNetPortFlowPointThresholdIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_F3PtpNetPortFlowPointThresholdIndex_Type.__name__ = "Integer32"
_F3PtpNetPortFlowPointThresholdIndex_Object = MibTableColumn
f3PtpNetPortFlowPointThresholdIndex = _F3PtpNetPortFlowPointThresholdIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 6, 1, 1),
    _F3PtpNetPortFlowPointThresholdIndex_Type()
)
f3PtpNetPortFlowPointThresholdIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    f3PtpNetPortFlowPointThresholdIndex.setStatus("current")
_F3PtpNetPortFlowPointThresholdInterval_Type = CmPmIntervalType
_F3PtpNetPortFlowPointThresholdInterval_Object = MibTableColumn
f3PtpNetPortFlowPointThresholdInterval = _F3PtpNetPortFlowPointThresholdInterval_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 6, 1, 2),
    _F3PtpNetPortFlowPointThresholdInterval_Type()
)
f3PtpNetPortFlowPointThresholdInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpNetPortFlowPointThresholdInterval.setStatus("current")
_F3PtpNetPortFlowPointThresholdVariable_Type = VariablePointer
_F3PtpNetPortFlowPointThresholdVariable_Object = MibTableColumn
f3PtpNetPortFlowPointThresholdVariable = _F3PtpNetPortFlowPointThresholdVariable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 6, 1, 3),
    _F3PtpNetPortFlowPointThresholdVariable_Type()
)
f3PtpNetPortFlowPointThresholdVariable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpNetPortFlowPointThresholdVariable.setStatus("current")
_F3PtpNetPortFlowPointThresholdValueLo_Type = Unsigned32
_F3PtpNetPortFlowPointThresholdValueLo_Object = MibTableColumn
f3PtpNetPortFlowPointThresholdValueLo = _F3PtpNetPortFlowPointThresholdValueLo_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 6, 1, 4),
    _F3PtpNetPortFlowPointThresholdValueLo_Type()
)
f3PtpNetPortFlowPointThresholdValueLo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3PtpNetPortFlowPointThresholdValueLo.setStatus("current")
_F3PtpNetPortFlowPointThresholdValueHi_Type = Unsigned32
_F3PtpNetPortFlowPointThresholdValueHi_Object = MibTableColumn
f3PtpNetPortFlowPointThresholdValueHi = _F3PtpNetPortFlowPointThresholdValueHi_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 6, 1, 5),
    _F3PtpNetPortFlowPointThresholdValueHi_Type()
)
f3PtpNetPortFlowPointThresholdValueHi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3PtpNetPortFlowPointThresholdValueHi.setStatus("current")
_F3PtpNetPortFlowPointThresholdMonValue_Type = PerfCounter64
_F3PtpNetPortFlowPointThresholdMonValue_Object = MibTableColumn
f3PtpNetPortFlowPointThresholdMonValue = _F3PtpNetPortFlowPointThresholdMonValue_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 6, 1, 6),
    _F3PtpNetPortFlowPointThresholdMonValue_Type()
)
f3PtpNetPortFlowPointThresholdMonValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpNetPortFlowPointThresholdMonValue.setStatus("current")
_F3PtpSOOCStatsTable_Object = MibTable
f3PtpSOOCStatsTable = _F3PtpSOOCStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 7)
)
if mibBuilder.loadTexts:
    f3PtpSOOCStatsTable.setStatus("current")
_F3PtpSOOCStatsEntry_Object = MibTableRow
f3PtpSOOCStatsEntry = _F3PtpSOOCStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 7, 1)
)
f3PtpSOOCStatsEntry.setIndexNames(
    (0, "CM-ENTITY-MIB", "neIndex"),
    (0, "F3-PTP-MIB", "f3PtpTSIndex"),
    (0, "F3-PTP-MIB", "f3PtpSOOCIndex"),
    (0, "F3-PTP-MIB", "f3PtpSOOCStatsIndex"),
)
if mibBuilder.loadTexts:
    f3PtpSOOCStatsEntry.setStatus("current")


class _F3PtpSOOCStatsIndex_Type(Integer32):
    """Custom type f3PtpSOOCStatsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_F3PtpSOOCStatsIndex_Type.__name__ = "Integer32"
_F3PtpSOOCStatsIndex_Object = MibTableColumn
f3PtpSOOCStatsIndex = _F3PtpSOOCStatsIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 7, 1, 1),
    _F3PtpSOOCStatsIndex_Type()
)
f3PtpSOOCStatsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    f3PtpSOOCStatsIndex.setStatus("current")
_F3PtpSOOCStatsIntervalType_Type = CmPmIntervalType
_F3PtpSOOCStatsIntervalType_Object = MibTableColumn
f3PtpSOOCStatsIntervalType = _F3PtpSOOCStatsIntervalType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 7, 1, 2),
    _F3PtpSOOCStatsIntervalType_Type()
)
f3PtpSOOCStatsIntervalType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpSOOCStatsIntervalType.setStatus("current")
_F3PtpSOOCStatsValid_Type = TruthValue
_F3PtpSOOCStatsValid_Object = MibTableColumn
f3PtpSOOCStatsValid = _F3PtpSOOCStatsValid_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 7, 1, 3),
    _F3PtpSOOCStatsValid_Type()
)
f3PtpSOOCStatsValid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpSOOCStatsValid.setStatus("current")
_F3PtpSOOCStatsAction_Type = CmPmBinAction
_F3PtpSOOCStatsAction_Object = MibTableColumn
f3PtpSOOCStatsAction = _F3PtpSOOCStatsAction_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 7, 1, 4),
    _F3PtpSOOCStatsAction_Type()
)
f3PtpSOOCStatsAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3PtpSOOCStatsAction.setStatus("current")
_F3PtpSOOCStatsMinOffsetFromMaster_Type = ScaledNanoseconds
_F3PtpSOOCStatsMinOffsetFromMaster_Object = MibTableColumn
f3PtpSOOCStatsMinOffsetFromMaster = _F3PtpSOOCStatsMinOffsetFromMaster_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 7, 1, 5),
    _F3PtpSOOCStatsMinOffsetFromMaster_Type()
)
f3PtpSOOCStatsMinOffsetFromMaster.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpSOOCStatsMinOffsetFromMaster.setStatus("current")
_F3PtpSOOCStatsMaxOffsetFromMaster_Type = ScaledNanoseconds
_F3PtpSOOCStatsMaxOffsetFromMaster_Object = MibTableColumn
f3PtpSOOCStatsMaxOffsetFromMaster = _F3PtpSOOCStatsMaxOffsetFromMaster_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 7, 1, 6),
    _F3PtpSOOCStatsMaxOffsetFromMaster_Type()
)
f3PtpSOOCStatsMaxOffsetFromMaster.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpSOOCStatsMaxOffsetFromMaster.setStatus("current")
_F3PtpSOOCStatsAvgOffsetFromMaster_Type = ScaledNanoseconds
_F3PtpSOOCStatsAvgOffsetFromMaster_Object = MibTableColumn
f3PtpSOOCStatsAvgOffsetFromMaster = _F3PtpSOOCStatsAvgOffsetFromMaster_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 7, 1, 7),
    _F3PtpSOOCStatsAvgOffsetFromMaster_Type()
)
f3PtpSOOCStatsAvgOffsetFromMaster.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpSOOCStatsAvgOffsetFromMaster.setStatus("current")
_F3PtpSOOCStatsMinMeanPathDelay_Type = ScaledNanoseconds
_F3PtpSOOCStatsMinMeanPathDelay_Object = MibTableColumn
f3PtpSOOCStatsMinMeanPathDelay = _F3PtpSOOCStatsMinMeanPathDelay_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 7, 1, 8),
    _F3PtpSOOCStatsMinMeanPathDelay_Type()
)
f3PtpSOOCStatsMinMeanPathDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpSOOCStatsMinMeanPathDelay.setStatus("current")
_F3PtpSOOCStatsMaxMeanPathDelay_Type = ScaledNanoseconds
_F3PtpSOOCStatsMaxMeanPathDelay_Object = MibTableColumn
f3PtpSOOCStatsMaxMeanPathDelay = _F3PtpSOOCStatsMaxMeanPathDelay_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 7, 1, 9),
    _F3PtpSOOCStatsMaxMeanPathDelay_Type()
)
f3PtpSOOCStatsMaxMeanPathDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpSOOCStatsMaxMeanPathDelay.setStatus("current")
_F3PtpSOOCStatsAvgMeanPathDelay_Type = ScaledNanoseconds
_F3PtpSOOCStatsAvgMeanPathDelay_Object = MibTableColumn
f3PtpSOOCStatsAvgMeanPathDelay = _F3PtpSOOCStatsAvgMeanPathDelay_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 7, 1, 10),
    _F3PtpSOOCStatsAvgMeanPathDelay_Type()
)
f3PtpSOOCStatsAvgMeanPathDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpSOOCStatsAvgMeanPathDelay.setStatus("current")
_F3PtpSOOCStatsMinSyncPathDelay_Type = ScaledNanoseconds
_F3PtpSOOCStatsMinSyncPathDelay_Object = MibTableColumn
f3PtpSOOCStatsMinSyncPathDelay = _F3PtpSOOCStatsMinSyncPathDelay_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 7, 1, 11),
    _F3PtpSOOCStatsMinSyncPathDelay_Type()
)
f3PtpSOOCStatsMinSyncPathDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpSOOCStatsMinSyncPathDelay.setStatus("current")
_F3PtpSOOCStatsMaxSyncPathDelay_Type = ScaledNanoseconds
_F3PtpSOOCStatsMaxSyncPathDelay_Object = MibTableColumn
f3PtpSOOCStatsMaxSyncPathDelay = _F3PtpSOOCStatsMaxSyncPathDelay_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 7, 1, 12),
    _F3PtpSOOCStatsMaxSyncPathDelay_Type()
)
f3PtpSOOCStatsMaxSyncPathDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpSOOCStatsMaxSyncPathDelay.setStatus("current")
_F3PtpSOOCStatsAvgSyncPathDelay_Type = ScaledNanoseconds
_F3PtpSOOCStatsAvgSyncPathDelay_Object = MibTableColumn
f3PtpSOOCStatsAvgSyncPathDelay = _F3PtpSOOCStatsAvgSyncPathDelay_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 7, 1, 13),
    _F3PtpSOOCStatsAvgSyncPathDelay_Type()
)
f3PtpSOOCStatsAvgSyncPathDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpSOOCStatsAvgSyncPathDelay.setStatus("current")
_F3PtpSOOCStatsMinSyncPDV_Type = ScaledNanoseconds
_F3PtpSOOCStatsMinSyncPDV_Object = MibTableColumn
f3PtpSOOCStatsMinSyncPDV = _F3PtpSOOCStatsMinSyncPDV_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 7, 1, 14),
    _F3PtpSOOCStatsMinSyncPDV_Type()
)
f3PtpSOOCStatsMinSyncPDV.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpSOOCStatsMinSyncPDV.setStatus("current")
_F3PtpSOOCStatsMaxSyncPDV_Type = ScaledNanoseconds
_F3PtpSOOCStatsMaxSyncPDV_Object = MibTableColumn
f3PtpSOOCStatsMaxSyncPDV = _F3PtpSOOCStatsMaxSyncPDV_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 7, 1, 15),
    _F3PtpSOOCStatsMaxSyncPDV_Type()
)
f3PtpSOOCStatsMaxSyncPDV.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpSOOCStatsMaxSyncPDV.setStatus("current")
_F3PtpSOOCStatsAvgSyncPDV_Type = ScaledNanoseconds
_F3PtpSOOCStatsAvgSyncPDV_Object = MibTableColumn
f3PtpSOOCStatsAvgSyncPDV = _F3PtpSOOCStatsAvgSyncPDV_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 7, 1, 16),
    _F3PtpSOOCStatsAvgSyncPDV_Type()
)
f3PtpSOOCStatsAvgSyncPDV.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpSOOCStatsAvgSyncPDV.setStatus("current")
_F3PtpSOOCStatsMgmtMsgsDiscarded_Type = PerfCounter64
_F3PtpSOOCStatsMgmtMsgsDiscarded_Object = MibTableColumn
f3PtpSOOCStatsMgmtMsgsDiscarded = _F3PtpSOOCStatsMgmtMsgsDiscarded_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 7, 1, 17),
    _F3PtpSOOCStatsMgmtMsgsDiscarded_Type()
)
f3PtpSOOCStatsMgmtMsgsDiscarded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpSOOCStatsMgmtMsgsDiscarded.setStatus("current")
_F3PtpSOOCStatsInvalidMsgLenDiscards_Type = PerfCounter64
_F3PtpSOOCStatsInvalidMsgLenDiscards_Object = MibTableColumn
f3PtpSOOCStatsInvalidMsgLenDiscards = _F3PtpSOOCStatsInvalidMsgLenDiscards_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 7, 1, 18),
    _F3PtpSOOCStatsInvalidMsgLenDiscards_Type()
)
f3PtpSOOCStatsInvalidMsgLenDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpSOOCStatsInvalidMsgLenDiscards.setStatus("current")
_F3PtpSOOCStatsUnknownMasterDiscards_Type = PerfCounter64
_F3PtpSOOCStatsUnknownMasterDiscards_Object = MibTableColumn
f3PtpSOOCStatsUnknownMasterDiscards = _F3PtpSOOCStatsUnknownMasterDiscards_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 7, 1, 19),
    _F3PtpSOOCStatsUnknownMasterDiscards_Type()
)
f3PtpSOOCStatsUnknownMasterDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpSOOCStatsUnknownMasterDiscards.setStatus("current")
_F3PtpSOOCStatsUnknownDomainDiscards_Type = PerfCounter64
_F3PtpSOOCStatsUnknownDomainDiscards_Object = MibTableColumn
f3PtpSOOCStatsUnknownDomainDiscards = _F3PtpSOOCStatsUnknownDomainDiscards_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 7, 1, 20),
    _F3PtpSOOCStatsUnknownDomainDiscards_Type()
)
f3PtpSOOCStatsUnknownDomainDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpSOOCStatsUnknownDomainDiscards.setStatus("current")
_F3PtpSOOCStatsMulticastAnnounceDiscards_Type = PerfCounter64
_F3PtpSOOCStatsMulticastAnnounceDiscards_Object = MibTableColumn
f3PtpSOOCStatsMulticastAnnounceDiscards = _F3PtpSOOCStatsMulticastAnnounceDiscards_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 7, 1, 21),
    _F3PtpSOOCStatsMulticastAnnounceDiscards_Type()
)
f3PtpSOOCStatsMulticastAnnounceDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpSOOCStatsMulticastAnnounceDiscards.setStatus("current")
_F3PtpSOOCStatsOutOfSeqAnnounceMsgs_Type = PerfCounter64
_F3PtpSOOCStatsOutOfSeqAnnounceMsgs_Object = MibTableColumn
f3PtpSOOCStatsOutOfSeqAnnounceMsgs = _F3PtpSOOCStatsOutOfSeqAnnounceMsgs_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 7, 1, 22),
    _F3PtpSOOCStatsOutOfSeqAnnounceMsgs_Type()
)
f3PtpSOOCStatsOutOfSeqAnnounceMsgs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpSOOCStatsOutOfSeqAnnounceMsgs.setStatus("current")
_F3PtpSOOCStatsMulticastSyncDiscards_Type = PerfCounter64
_F3PtpSOOCStatsMulticastSyncDiscards_Object = MibTableColumn
f3PtpSOOCStatsMulticastSyncDiscards = _F3PtpSOOCStatsMulticastSyncDiscards_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 7, 1, 23),
    _F3PtpSOOCStatsMulticastSyncDiscards_Type()
)
f3PtpSOOCStatsMulticastSyncDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpSOOCStatsMulticastSyncDiscards.setStatus("current")
_F3PtpSOOCStatsTwoStepSyncDiscards_Type = PerfCounter64
_F3PtpSOOCStatsTwoStepSyncDiscards_Object = MibTableColumn
f3PtpSOOCStatsTwoStepSyncDiscards = _F3PtpSOOCStatsTwoStepSyncDiscards_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 7, 1, 24),
    _F3PtpSOOCStatsTwoStepSyncDiscards_Type()
)
f3PtpSOOCStatsTwoStepSyncDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpSOOCStatsTwoStepSyncDiscards.setStatus("current")
_F3PtpSOOCStatsFollowupDiscards_Type = PerfCounter64
_F3PtpSOOCStatsFollowupDiscards_Object = MibTableColumn
f3PtpSOOCStatsFollowupDiscards = _F3PtpSOOCStatsFollowupDiscards_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 7, 1, 25),
    _F3PtpSOOCStatsFollowupDiscards_Type()
)
f3PtpSOOCStatsFollowupDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpSOOCStatsFollowupDiscards.setStatus("current")
_F3PtpSOOCStatsDelayReqDiscards_Type = PerfCounter64
_F3PtpSOOCStatsDelayReqDiscards_Object = MibTableColumn
f3PtpSOOCStatsDelayReqDiscards = _F3PtpSOOCStatsDelayReqDiscards_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 7, 1, 26),
    _F3PtpSOOCStatsDelayReqDiscards_Type()
)
f3PtpSOOCStatsDelayReqDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpSOOCStatsDelayReqDiscards.setStatus("current")
_F3PtpSOOCStatsPDelayReqDiscards_Type = PerfCounter64
_F3PtpSOOCStatsPDelayReqDiscards_Object = MibTableColumn
f3PtpSOOCStatsPDelayReqDiscards = _F3PtpSOOCStatsPDelayReqDiscards_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 7, 1, 27),
    _F3PtpSOOCStatsPDelayReqDiscards_Type()
)
f3PtpSOOCStatsPDelayReqDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpSOOCStatsPDelayReqDiscards.setStatus("current")
_F3PtpSOOCStatsPDelayRspDiscards_Type = PerfCounter64
_F3PtpSOOCStatsPDelayRspDiscards_Object = MibTableColumn
f3PtpSOOCStatsPDelayRspDiscards = _F3PtpSOOCStatsPDelayRspDiscards_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 7, 1, 28),
    _F3PtpSOOCStatsPDelayRspDiscards_Type()
)
f3PtpSOOCStatsPDelayRspDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpSOOCStatsPDelayRspDiscards.setStatus("current")
_F3PtpSOOCStatsPDelayFollowupDiscards_Type = PerfCounter64
_F3PtpSOOCStatsPDelayFollowupDiscards_Object = MibTableColumn
f3PtpSOOCStatsPDelayFollowupDiscards = _F3PtpSOOCStatsPDelayFollowupDiscards_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 7, 1, 29),
    _F3PtpSOOCStatsPDelayFollowupDiscards_Type()
)
f3PtpSOOCStatsPDelayFollowupDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpSOOCStatsPDelayFollowupDiscards.setStatus("current")
_F3PtpSOOCStatsInvalidTLVLenDiscards_Type = PerfCounter64
_F3PtpSOOCStatsInvalidTLVLenDiscards_Object = MibTableColumn
f3PtpSOOCStatsInvalidTLVLenDiscards = _F3PtpSOOCStatsInvalidTLVLenDiscards_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 7, 1, 30),
    _F3PtpSOOCStatsInvalidTLVLenDiscards_Type()
)
f3PtpSOOCStatsInvalidTLVLenDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpSOOCStatsInvalidTLVLenDiscards.setStatus("current")
_F3PtpSOOCStatsInvalidTLVTypeDiscards_Type = PerfCounter64
_F3PtpSOOCStatsInvalidTLVTypeDiscards_Object = MibTableColumn
f3PtpSOOCStatsInvalidTLVTypeDiscards = _F3PtpSOOCStatsInvalidTLVTypeDiscards_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 7, 1, 31),
    _F3PtpSOOCStatsInvalidTLVTypeDiscards_Type()
)
f3PtpSOOCStatsInvalidTLVTypeDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpSOOCStatsInvalidTLVTypeDiscards.setStatus("current")
_F3PtpSOOCStatsMaxFwdFlowWeight_Type = Integer32
_F3PtpSOOCStatsMaxFwdFlowWeight_Object = MibTableColumn
f3PtpSOOCStatsMaxFwdFlowWeight = _F3PtpSOOCStatsMaxFwdFlowWeight_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 7, 1, 32),
    _F3PtpSOOCStatsMaxFwdFlowWeight_Type()
)
f3PtpSOOCStatsMaxFwdFlowWeight.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3PtpSOOCStatsMaxFwdFlowWeight.setStatus("current")
_F3PtpSOOCStatsAvgFwdFlowWeight_Type = Integer32
_F3PtpSOOCStatsAvgFwdFlowWeight_Object = MibTableColumn
f3PtpSOOCStatsAvgFwdFlowWeight = _F3PtpSOOCStatsAvgFwdFlowWeight_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 7, 1, 33),
    _F3PtpSOOCStatsAvgFwdFlowWeight_Type()
)
f3PtpSOOCStatsAvgFwdFlowWeight.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3PtpSOOCStatsAvgFwdFlowWeight.setStatus("current")
_F3PtpSOOCStatsMinRevFlowWeight_Type = Integer32
_F3PtpSOOCStatsMinRevFlowWeight_Object = MibTableColumn
f3PtpSOOCStatsMinRevFlowWeight = _F3PtpSOOCStatsMinRevFlowWeight_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 7, 1, 34),
    _F3PtpSOOCStatsMinRevFlowWeight_Type()
)
f3PtpSOOCStatsMinRevFlowWeight.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3PtpSOOCStatsMinRevFlowWeight.setStatus("current")
_F3PtpSOOCStatsMaxRevFlowWeight_Type = Integer32
_F3PtpSOOCStatsMaxRevFlowWeight_Object = MibTableColumn
f3PtpSOOCStatsMaxRevFlowWeight = _F3PtpSOOCStatsMaxRevFlowWeight_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 7, 1, 35),
    _F3PtpSOOCStatsMaxRevFlowWeight_Type()
)
f3PtpSOOCStatsMaxRevFlowWeight.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3PtpSOOCStatsMaxRevFlowWeight.setStatus("current")
_F3PtpSOOCStatsAvgRevFlowWeight_Type = Integer32
_F3PtpSOOCStatsAvgRevFlowWeight_Object = MibTableColumn
f3PtpSOOCStatsAvgRevFlowWeight = _F3PtpSOOCStatsAvgRevFlowWeight_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 7, 1, 36),
    _F3PtpSOOCStatsAvgRevFlowWeight_Type()
)
f3PtpSOOCStatsAvgRevFlowWeight.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3PtpSOOCStatsAvgRevFlowWeight.setStatus("current")
_F3PtpSOOCStatsNumClockRecTransients_Type = Unsigned32
_F3PtpSOOCStatsNumClockRecTransients_Object = MibTableColumn
f3PtpSOOCStatsNumClockRecTransients = _F3PtpSOOCStatsNumClockRecTransients_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 7, 1, 37),
    _F3PtpSOOCStatsNumClockRecTransients_Type()
)
f3PtpSOOCStatsNumClockRecTransients.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3PtpSOOCStatsNumClockRecTransients.setStatus("current")
_F3PtpSOOCHistoryTable_Object = MibTable
f3PtpSOOCHistoryTable = _F3PtpSOOCHistoryTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 8)
)
if mibBuilder.loadTexts:
    f3PtpSOOCHistoryTable.setStatus("current")
_F3PtpSOOCHistoryEntry_Object = MibTableRow
f3PtpSOOCHistoryEntry = _F3PtpSOOCHistoryEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 8, 1)
)
f3PtpSOOCHistoryEntry.setIndexNames(
    (0, "CM-ENTITY-MIB", "neIndex"),
    (0, "F3-PTP-MIB", "f3PtpTSIndex"),
    (0, "F3-PTP-MIB", "f3PtpSOOCIndex"),
    (0, "F3-PTP-MIB", "f3PtpSOOCStatsIndex"),
    (0, "F3-PTP-MIB", "f3PtpSOOCHistoryIndex"),
)
if mibBuilder.loadTexts:
    f3PtpSOOCHistoryEntry.setStatus("current")


class _F3PtpSOOCHistoryIndex_Type(Integer32):
    """Custom type f3PtpSOOCHistoryIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_F3PtpSOOCHistoryIndex_Type.__name__ = "Integer32"
_F3PtpSOOCHistoryIndex_Object = MibTableColumn
f3PtpSOOCHistoryIndex = _F3PtpSOOCHistoryIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 8, 1, 1),
    _F3PtpSOOCHistoryIndex_Type()
)
f3PtpSOOCHistoryIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    f3PtpSOOCHistoryIndex.setStatus("current")
_F3PtpSOOCHistoryTime_Type = DateAndTime
_F3PtpSOOCHistoryTime_Object = MibTableColumn
f3PtpSOOCHistoryTime = _F3PtpSOOCHistoryTime_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 8, 1, 2),
    _F3PtpSOOCHistoryTime_Type()
)
f3PtpSOOCHistoryTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpSOOCHistoryTime.setStatus("current")
_F3PtpSOOCHistoryValid_Type = TruthValue
_F3PtpSOOCHistoryValid_Object = MibTableColumn
f3PtpSOOCHistoryValid = _F3PtpSOOCHistoryValid_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 8, 1, 3),
    _F3PtpSOOCHistoryValid_Type()
)
f3PtpSOOCHistoryValid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpSOOCHistoryValid.setStatus("current")
_F3PtpSOOCHistoryAction_Type = CmPmBinAction
_F3PtpSOOCHistoryAction_Object = MibTableColumn
f3PtpSOOCHistoryAction = _F3PtpSOOCHistoryAction_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 8, 1, 4),
    _F3PtpSOOCHistoryAction_Type()
)
f3PtpSOOCHistoryAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3PtpSOOCHistoryAction.setStatus("current")
_F3PtpSOOCHistoryMinOffsetFromMaster_Type = ScaledNanoseconds
_F3PtpSOOCHistoryMinOffsetFromMaster_Object = MibTableColumn
f3PtpSOOCHistoryMinOffsetFromMaster = _F3PtpSOOCHistoryMinOffsetFromMaster_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 8, 1, 5),
    _F3PtpSOOCHistoryMinOffsetFromMaster_Type()
)
f3PtpSOOCHistoryMinOffsetFromMaster.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpSOOCHistoryMinOffsetFromMaster.setStatus("current")
_F3PtpSOOCHistoryMaxOffsetFromMaster_Type = ScaledNanoseconds
_F3PtpSOOCHistoryMaxOffsetFromMaster_Object = MibTableColumn
f3PtpSOOCHistoryMaxOffsetFromMaster = _F3PtpSOOCHistoryMaxOffsetFromMaster_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 8, 1, 6),
    _F3PtpSOOCHistoryMaxOffsetFromMaster_Type()
)
f3PtpSOOCHistoryMaxOffsetFromMaster.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpSOOCHistoryMaxOffsetFromMaster.setStatus("current")
_F3PtpSOOCHistoryAvgOffsetFromMaster_Type = ScaledNanoseconds
_F3PtpSOOCHistoryAvgOffsetFromMaster_Object = MibTableColumn
f3PtpSOOCHistoryAvgOffsetFromMaster = _F3PtpSOOCHistoryAvgOffsetFromMaster_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 8, 1, 7),
    _F3PtpSOOCHistoryAvgOffsetFromMaster_Type()
)
f3PtpSOOCHistoryAvgOffsetFromMaster.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpSOOCHistoryAvgOffsetFromMaster.setStatus("current")
_F3PtpSOOCHistoryMinMeanPathDelay_Type = ScaledNanoseconds
_F3PtpSOOCHistoryMinMeanPathDelay_Object = MibTableColumn
f3PtpSOOCHistoryMinMeanPathDelay = _F3PtpSOOCHistoryMinMeanPathDelay_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 8, 1, 8),
    _F3PtpSOOCHistoryMinMeanPathDelay_Type()
)
f3PtpSOOCHistoryMinMeanPathDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpSOOCHistoryMinMeanPathDelay.setStatus("current")
_F3PtpSOOCHistoryMaxMeanPathDelay_Type = ScaledNanoseconds
_F3PtpSOOCHistoryMaxMeanPathDelay_Object = MibTableColumn
f3PtpSOOCHistoryMaxMeanPathDelay = _F3PtpSOOCHistoryMaxMeanPathDelay_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 8, 1, 9),
    _F3PtpSOOCHistoryMaxMeanPathDelay_Type()
)
f3PtpSOOCHistoryMaxMeanPathDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpSOOCHistoryMaxMeanPathDelay.setStatus("current")
_F3PtpSOOCHistoryAvgMeanPathDelay_Type = ScaledNanoseconds
_F3PtpSOOCHistoryAvgMeanPathDelay_Object = MibTableColumn
f3PtpSOOCHistoryAvgMeanPathDelay = _F3PtpSOOCHistoryAvgMeanPathDelay_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 8, 1, 10),
    _F3PtpSOOCHistoryAvgMeanPathDelay_Type()
)
f3PtpSOOCHistoryAvgMeanPathDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpSOOCHistoryAvgMeanPathDelay.setStatus("current")
_F3PtpSOOCHistoryMinSyncPathDelay_Type = ScaledNanoseconds
_F3PtpSOOCHistoryMinSyncPathDelay_Object = MibTableColumn
f3PtpSOOCHistoryMinSyncPathDelay = _F3PtpSOOCHistoryMinSyncPathDelay_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 8, 1, 11),
    _F3PtpSOOCHistoryMinSyncPathDelay_Type()
)
f3PtpSOOCHistoryMinSyncPathDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpSOOCHistoryMinSyncPathDelay.setStatus("current")
_F3PtpSOOCHistoryMaxSyncPathDelay_Type = ScaledNanoseconds
_F3PtpSOOCHistoryMaxSyncPathDelay_Object = MibTableColumn
f3PtpSOOCHistoryMaxSyncPathDelay = _F3PtpSOOCHistoryMaxSyncPathDelay_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 8, 1, 12),
    _F3PtpSOOCHistoryMaxSyncPathDelay_Type()
)
f3PtpSOOCHistoryMaxSyncPathDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpSOOCHistoryMaxSyncPathDelay.setStatus("current")
_F3PtpSOOCHistoryAvgSyncPathDelay_Type = ScaledNanoseconds
_F3PtpSOOCHistoryAvgSyncPathDelay_Object = MibTableColumn
f3PtpSOOCHistoryAvgSyncPathDelay = _F3PtpSOOCHistoryAvgSyncPathDelay_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 8, 1, 13),
    _F3PtpSOOCHistoryAvgSyncPathDelay_Type()
)
f3PtpSOOCHistoryAvgSyncPathDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpSOOCHistoryAvgSyncPathDelay.setStatus("current")
_F3PtpSOOCHistoryMinSyncPDV_Type = ScaledNanoseconds
_F3PtpSOOCHistoryMinSyncPDV_Object = MibTableColumn
f3PtpSOOCHistoryMinSyncPDV = _F3PtpSOOCHistoryMinSyncPDV_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 8, 1, 14),
    _F3PtpSOOCHistoryMinSyncPDV_Type()
)
f3PtpSOOCHistoryMinSyncPDV.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpSOOCHistoryMinSyncPDV.setStatus("current")
_F3PtpSOOCHistoryMaxSyncPDV_Type = ScaledNanoseconds
_F3PtpSOOCHistoryMaxSyncPDV_Object = MibTableColumn
f3PtpSOOCHistoryMaxSyncPDV = _F3PtpSOOCHistoryMaxSyncPDV_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 8, 1, 15),
    _F3PtpSOOCHistoryMaxSyncPDV_Type()
)
f3PtpSOOCHistoryMaxSyncPDV.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpSOOCHistoryMaxSyncPDV.setStatus("current")
_F3PtpSOOCHistoryAvgSyncPDV_Type = ScaledNanoseconds
_F3PtpSOOCHistoryAvgSyncPDV_Object = MibTableColumn
f3PtpSOOCHistoryAvgSyncPDV = _F3PtpSOOCHistoryAvgSyncPDV_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 8, 1, 16),
    _F3PtpSOOCHistoryAvgSyncPDV_Type()
)
f3PtpSOOCHistoryAvgSyncPDV.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpSOOCHistoryAvgSyncPDV.setStatus("current")
_F3PtpSOOCHistoryMgmtMsgsDiscarded_Type = PerfCounter64
_F3PtpSOOCHistoryMgmtMsgsDiscarded_Object = MibTableColumn
f3PtpSOOCHistoryMgmtMsgsDiscarded = _F3PtpSOOCHistoryMgmtMsgsDiscarded_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 8, 1, 17),
    _F3PtpSOOCHistoryMgmtMsgsDiscarded_Type()
)
f3PtpSOOCHistoryMgmtMsgsDiscarded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpSOOCHistoryMgmtMsgsDiscarded.setStatus("current")
_F3PtpSOOCHistoryInvalidMsgLenDiscards_Type = PerfCounter64
_F3PtpSOOCHistoryInvalidMsgLenDiscards_Object = MibTableColumn
f3PtpSOOCHistoryInvalidMsgLenDiscards = _F3PtpSOOCHistoryInvalidMsgLenDiscards_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 8, 1, 18),
    _F3PtpSOOCHistoryInvalidMsgLenDiscards_Type()
)
f3PtpSOOCHistoryInvalidMsgLenDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpSOOCHistoryInvalidMsgLenDiscards.setStatus("current")
_F3PtpSOOCHistoryUnknownMasterDiscards_Type = PerfCounter64
_F3PtpSOOCHistoryUnknownMasterDiscards_Object = MibTableColumn
f3PtpSOOCHistoryUnknownMasterDiscards = _F3PtpSOOCHistoryUnknownMasterDiscards_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 8, 1, 19),
    _F3PtpSOOCHistoryUnknownMasterDiscards_Type()
)
f3PtpSOOCHistoryUnknownMasterDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpSOOCHistoryUnknownMasterDiscards.setStatus("current")
_F3PtpSOOCHistoryUnknownDomainDiscards_Type = PerfCounter64
_F3PtpSOOCHistoryUnknownDomainDiscards_Object = MibTableColumn
f3PtpSOOCHistoryUnknownDomainDiscards = _F3PtpSOOCHistoryUnknownDomainDiscards_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 8, 1, 20),
    _F3PtpSOOCHistoryUnknownDomainDiscards_Type()
)
f3PtpSOOCHistoryUnknownDomainDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpSOOCHistoryUnknownDomainDiscards.setStatus("current")
_F3PtpSOOCHistoryMulticastAnnounceDiscards_Type = PerfCounter64
_F3PtpSOOCHistoryMulticastAnnounceDiscards_Object = MibTableColumn
f3PtpSOOCHistoryMulticastAnnounceDiscards = _F3PtpSOOCHistoryMulticastAnnounceDiscards_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 8, 1, 21),
    _F3PtpSOOCHistoryMulticastAnnounceDiscards_Type()
)
f3PtpSOOCHistoryMulticastAnnounceDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpSOOCHistoryMulticastAnnounceDiscards.setStatus("current")
_F3PtpSOOCHistoryOutOfSeqAnnounceMsgs_Type = PerfCounter64
_F3PtpSOOCHistoryOutOfSeqAnnounceMsgs_Object = MibTableColumn
f3PtpSOOCHistoryOutOfSeqAnnounceMsgs = _F3PtpSOOCHistoryOutOfSeqAnnounceMsgs_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 8, 1, 22),
    _F3PtpSOOCHistoryOutOfSeqAnnounceMsgs_Type()
)
f3PtpSOOCHistoryOutOfSeqAnnounceMsgs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpSOOCHistoryOutOfSeqAnnounceMsgs.setStatus("current")
_F3PtpSOOCHistoryMulticastSyncDiscards_Type = PerfCounter64
_F3PtpSOOCHistoryMulticastSyncDiscards_Object = MibTableColumn
f3PtpSOOCHistoryMulticastSyncDiscards = _F3PtpSOOCHistoryMulticastSyncDiscards_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 8, 1, 23),
    _F3PtpSOOCHistoryMulticastSyncDiscards_Type()
)
f3PtpSOOCHistoryMulticastSyncDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpSOOCHistoryMulticastSyncDiscards.setStatus("current")
_F3PtpSOOCHistoryTwoStepSyncDiscards_Type = PerfCounter64
_F3PtpSOOCHistoryTwoStepSyncDiscards_Object = MibTableColumn
f3PtpSOOCHistoryTwoStepSyncDiscards = _F3PtpSOOCHistoryTwoStepSyncDiscards_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 8, 1, 24),
    _F3PtpSOOCHistoryTwoStepSyncDiscards_Type()
)
f3PtpSOOCHistoryTwoStepSyncDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpSOOCHistoryTwoStepSyncDiscards.setStatus("current")
_F3PtpSOOCHistoryFollowupDiscards_Type = PerfCounter64
_F3PtpSOOCHistoryFollowupDiscards_Object = MibTableColumn
f3PtpSOOCHistoryFollowupDiscards = _F3PtpSOOCHistoryFollowupDiscards_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 8, 1, 25),
    _F3PtpSOOCHistoryFollowupDiscards_Type()
)
f3PtpSOOCHistoryFollowupDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpSOOCHistoryFollowupDiscards.setStatus("current")
_F3PtpSOOCHistoryDelayReqDiscards_Type = PerfCounter64
_F3PtpSOOCHistoryDelayReqDiscards_Object = MibTableColumn
f3PtpSOOCHistoryDelayReqDiscards = _F3PtpSOOCHistoryDelayReqDiscards_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 8, 1, 26),
    _F3PtpSOOCHistoryDelayReqDiscards_Type()
)
f3PtpSOOCHistoryDelayReqDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpSOOCHistoryDelayReqDiscards.setStatus("current")
_F3PtpSOOCHistoryPDelayReqDiscards_Type = PerfCounter64
_F3PtpSOOCHistoryPDelayReqDiscards_Object = MibTableColumn
f3PtpSOOCHistoryPDelayReqDiscards = _F3PtpSOOCHistoryPDelayReqDiscards_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 8, 1, 27),
    _F3PtpSOOCHistoryPDelayReqDiscards_Type()
)
f3PtpSOOCHistoryPDelayReqDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpSOOCHistoryPDelayReqDiscards.setStatus("current")
_F3PtpSOOCHistoryPDelayRspDiscards_Type = PerfCounter64
_F3PtpSOOCHistoryPDelayRspDiscards_Object = MibTableColumn
f3PtpSOOCHistoryPDelayRspDiscards = _F3PtpSOOCHistoryPDelayRspDiscards_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 8, 1, 28),
    _F3PtpSOOCHistoryPDelayRspDiscards_Type()
)
f3PtpSOOCHistoryPDelayRspDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpSOOCHistoryPDelayRspDiscards.setStatus("current")
_F3PtpSOOCHistoryPDelayFollowupDiscards_Type = PerfCounter64
_F3PtpSOOCHistoryPDelayFollowupDiscards_Object = MibTableColumn
f3PtpSOOCHistoryPDelayFollowupDiscards = _F3PtpSOOCHistoryPDelayFollowupDiscards_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 8, 1, 29),
    _F3PtpSOOCHistoryPDelayFollowupDiscards_Type()
)
f3PtpSOOCHistoryPDelayFollowupDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpSOOCHistoryPDelayFollowupDiscards.setStatus("current")
_F3PtpSOOCHistoryInvalidTLVLenDiscards_Type = PerfCounter64
_F3PtpSOOCHistoryInvalidTLVLenDiscards_Object = MibTableColumn
f3PtpSOOCHistoryInvalidTLVLenDiscards = _F3PtpSOOCHistoryInvalidTLVLenDiscards_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 8, 1, 30),
    _F3PtpSOOCHistoryInvalidTLVLenDiscards_Type()
)
f3PtpSOOCHistoryInvalidTLVLenDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpSOOCHistoryInvalidTLVLenDiscards.setStatus("current")
_F3PtpSOOCHistoryInvalidTLVTypeDiscards_Type = PerfCounter64
_F3PtpSOOCHistoryInvalidTLVTypeDiscards_Object = MibTableColumn
f3PtpSOOCHistoryInvalidTLVTypeDiscards = _F3PtpSOOCHistoryInvalidTLVTypeDiscards_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 8, 1, 31),
    _F3PtpSOOCHistoryInvalidTLVTypeDiscards_Type()
)
f3PtpSOOCHistoryInvalidTLVTypeDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpSOOCHistoryInvalidTLVTypeDiscards.setStatus("current")
_F3PtpSOOCHistoryMaxFwdFlowWeight_Type = Integer32
_F3PtpSOOCHistoryMaxFwdFlowWeight_Object = MibTableColumn
f3PtpSOOCHistoryMaxFwdFlowWeight = _F3PtpSOOCHistoryMaxFwdFlowWeight_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 8, 1, 32),
    _F3PtpSOOCHistoryMaxFwdFlowWeight_Type()
)
f3PtpSOOCHistoryMaxFwdFlowWeight.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3PtpSOOCHistoryMaxFwdFlowWeight.setStatus("current")
_F3PtpSOOCHistoryAvgFwdFlowWeight_Type = Integer32
_F3PtpSOOCHistoryAvgFwdFlowWeight_Object = MibTableColumn
f3PtpSOOCHistoryAvgFwdFlowWeight = _F3PtpSOOCHistoryAvgFwdFlowWeight_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 8, 1, 33),
    _F3PtpSOOCHistoryAvgFwdFlowWeight_Type()
)
f3PtpSOOCHistoryAvgFwdFlowWeight.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3PtpSOOCHistoryAvgFwdFlowWeight.setStatus("current")
_F3PtpSOOCHistoryMinRevFlowWeight_Type = Integer32
_F3PtpSOOCHistoryMinRevFlowWeight_Object = MibTableColumn
f3PtpSOOCHistoryMinRevFlowWeight = _F3PtpSOOCHistoryMinRevFlowWeight_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 8, 1, 34),
    _F3PtpSOOCHistoryMinRevFlowWeight_Type()
)
f3PtpSOOCHistoryMinRevFlowWeight.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3PtpSOOCHistoryMinRevFlowWeight.setStatus("current")
_F3PtpSOOCHistoryMaxRevFlowWeight_Type = Integer32
_F3PtpSOOCHistoryMaxRevFlowWeight_Object = MibTableColumn
f3PtpSOOCHistoryMaxRevFlowWeight = _F3PtpSOOCHistoryMaxRevFlowWeight_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 8, 1, 35),
    _F3PtpSOOCHistoryMaxRevFlowWeight_Type()
)
f3PtpSOOCHistoryMaxRevFlowWeight.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3PtpSOOCHistoryMaxRevFlowWeight.setStatus("current")
_F3PtpSOOCHistoryAvgRevFlowWeight_Type = Integer32
_F3PtpSOOCHistoryAvgRevFlowWeight_Object = MibTableColumn
f3PtpSOOCHistoryAvgRevFlowWeight = _F3PtpSOOCHistoryAvgRevFlowWeight_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 8, 1, 36),
    _F3PtpSOOCHistoryAvgRevFlowWeight_Type()
)
f3PtpSOOCHistoryAvgRevFlowWeight.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3PtpSOOCHistoryAvgRevFlowWeight.setStatus("current")
_F3PtpSOOCHistoryNumClockRecTransients_Type = Unsigned32
_F3PtpSOOCHistoryNumClockRecTransients_Object = MibTableColumn
f3PtpSOOCHistoryNumClockRecTransients = _F3PtpSOOCHistoryNumClockRecTransients_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 8, 1, 37),
    _F3PtpSOOCHistoryNumClockRecTransients_Type()
)
f3PtpSOOCHistoryNumClockRecTransients.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3PtpSOOCHistoryNumClockRecTransients.setStatus("current")
_F3PtpSOOCThresholdTable_Object = MibTable
f3PtpSOOCThresholdTable = _F3PtpSOOCThresholdTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 9)
)
if mibBuilder.loadTexts:
    f3PtpSOOCThresholdTable.setStatus("current")
_F3PtpSOOCThresholdEntry_Object = MibTableRow
f3PtpSOOCThresholdEntry = _F3PtpSOOCThresholdEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 9, 1)
)
f3PtpSOOCThresholdEntry.setIndexNames(
    (0, "CM-ENTITY-MIB", "neIndex"),
    (0, "F3-PTP-MIB", "f3PtpTSIndex"),
    (0, "F3-PTP-MIB", "f3PtpSOOCIndex"),
    (0, "F3-PTP-MIB", "f3PtpSOOCStatsIndex"),
    (0, "F3-PTP-MIB", "f3PtpSOOCThresholdIndex"),
)
if mibBuilder.loadTexts:
    f3PtpSOOCThresholdEntry.setStatus("current")


class _F3PtpSOOCThresholdIndex_Type(Integer32):
    """Custom type f3PtpSOOCThresholdIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_F3PtpSOOCThresholdIndex_Type.__name__ = "Integer32"
_F3PtpSOOCThresholdIndex_Object = MibTableColumn
f3PtpSOOCThresholdIndex = _F3PtpSOOCThresholdIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 9, 1, 1),
    _F3PtpSOOCThresholdIndex_Type()
)
f3PtpSOOCThresholdIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    f3PtpSOOCThresholdIndex.setStatus("current")
_F3PtpSOOCThresholdInterval_Type = CmPmIntervalType
_F3PtpSOOCThresholdInterval_Object = MibTableColumn
f3PtpSOOCThresholdInterval = _F3PtpSOOCThresholdInterval_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 9, 1, 2),
    _F3PtpSOOCThresholdInterval_Type()
)
f3PtpSOOCThresholdInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpSOOCThresholdInterval.setStatus("current")
_F3PtpSOOCThresholdVariable_Type = VariablePointer
_F3PtpSOOCThresholdVariable_Object = MibTableColumn
f3PtpSOOCThresholdVariable = _F3PtpSOOCThresholdVariable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 9, 1, 3),
    _F3PtpSOOCThresholdVariable_Type()
)
f3PtpSOOCThresholdVariable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpSOOCThresholdVariable.setStatus("current")
_F3PtpSOOCThresholdValueLo_Type = Unsigned32
_F3PtpSOOCThresholdValueLo_Object = MibTableColumn
f3PtpSOOCThresholdValueLo = _F3PtpSOOCThresholdValueLo_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 9, 1, 4),
    _F3PtpSOOCThresholdValueLo_Type()
)
f3PtpSOOCThresholdValueLo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3PtpSOOCThresholdValueLo.setStatus("current")
_F3PtpSOOCThresholdValueHi_Type = Unsigned32
_F3PtpSOOCThresholdValueHi_Object = MibTableColumn
f3PtpSOOCThresholdValueHi = _F3PtpSOOCThresholdValueHi_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 9, 1, 5),
    _F3PtpSOOCThresholdValueHi_Type()
)
f3PtpSOOCThresholdValueHi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3PtpSOOCThresholdValueHi.setStatus("current")
_F3PtpSOOCThresholdMonValue_Type = PerfCounter64
_F3PtpSOOCThresholdMonValue_Object = MibTableColumn
f3PtpSOOCThresholdMonValue = _F3PtpSOOCThresholdMonValue_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 9, 1, 6),
    _F3PtpSOOCThresholdMonValue_Type()
)
f3PtpSOOCThresholdMonValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpSOOCThresholdMonValue.setStatus("current")
_F3PtpTSStatsTable_Object = MibTable
f3PtpTSStatsTable = _F3PtpTSStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 10)
)
if mibBuilder.loadTexts:
    f3PtpTSStatsTable.setStatus("current")
_F3PtpTSStatsEntry_Object = MibTableRow
f3PtpTSStatsEntry = _F3PtpTSStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 10, 1)
)
f3PtpTSStatsEntry.setIndexNames(
    (0, "CM-ENTITY-MIB", "neIndex"),
    (0, "F3-PTP-MIB", "f3PtpTSIndex"),
    (0, "F3-PTP-MIB", "f3PtpTSStatsIndex"),
)
if mibBuilder.loadTexts:
    f3PtpTSStatsEntry.setStatus("current")


class _F3PtpTSStatsIndex_Type(Integer32):
    """Custom type f3PtpTSStatsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_F3PtpTSStatsIndex_Type.__name__ = "Integer32"
_F3PtpTSStatsIndex_Object = MibTableColumn
f3PtpTSStatsIndex = _F3PtpTSStatsIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 10, 1, 1),
    _F3PtpTSStatsIndex_Type()
)
f3PtpTSStatsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    f3PtpTSStatsIndex.setStatus("current")
_F3PtpTSStatsIntervalType_Type = CmPmIntervalType
_F3PtpTSStatsIntervalType_Object = MibTableColumn
f3PtpTSStatsIntervalType = _F3PtpTSStatsIntervalType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 10, 1, 2),
    _F3PtpTSStatsIntervalType_Type()
)
f3PtpTSStatsIntervalType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpTSStatsIntervalType.setStatus("current")
_F3PtpTSStatsValid_Type = TruthValue
_F3PtpTSStatsValid_Object = MibTableColumn
f3PtpTSStatsValid = _F3PtpTSStatsValid_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 10, 1, 3),
    _F3PtpTSStatsValid_Type()
)
f3PtpTSStatsValid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpTSStatsValid.setStatus("current")
_F3PtpTSStatsAction_Type = CmPmBinAction
_F3PtpTSStatsAction_Object = MibTableColumn
f3PtpTSStatsAction = _F3PtpTSStatsAction_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 10, 1, 4),
    _F3PtpTSStatsAction_Type()
)
f3PtpTSStatsAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3PtpTSStatsAction.setStatus("current")
_F3PtpTSStatsTotalTimeCR5_Type = Unsigned32
_F3PtpTSStatsTotalTimeCR5_Object = MibTableColumn
f3PtpTSStatsTotalTimeCR5 = _F3PtpTSStatsTotalTimeCR5_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 10, 1, 5),
    _F3PtpTSStatsTotalTimeCR5_Type()
)
f3PtpTSStatsTotalTimeCR5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpTSStatsTotalTimeCR5.setStatus("current")
_F3PtpTSStatsTotalTimeCR4_Type = Unsigned32
_F3PtpTSStatsTotalTimeCR4_Object = MibTableColumn
f3PtpTSStatsTotalTimeCR4 = _F3PtpTSStatsTotalTimeCR4_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 10, 1, 6),
    _F3PtpTSStatsTotalTimeCR4_Type()
)
f3PtpTSStatsTotalTimeCR4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpTSStatsTotalTimeCR4.setStatus("current")
_F3PtpTSStatsTotalTimeCR3_Type = Unsigned32
_F3PtpTSStatsTotalTimeCR3_Object = MibTableColumn
f3PtpTSStatsTotalTimeCR3 = _F3PtpTSStatsTotalTimeCR3_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 10, 1, 7),
    _F3PtpTSStatsTotalTimeCR3_Type()
)
f3PtpTSStatsTotalTimeCR3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpTSStatsTotalTimeCR3.setStatus("current")
_F3PtpTSStatsTotalTimePR5_Type = Unsigned32
_F3PtpTSStatsTotalTimePR5_Object = MibTableColumn
f3PtpTSStatsTotalTimePR5 = _F3PtpTSStatsTotalTimePR5_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 10, 1, 8),
    _F3PtpTSStatsTotalTimePR5_Type()
)
f3PtpTSStatsTotalTimePR5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpTSStatsTotalTimePR5.setStatus("current")
_F3PtpTSStatsTotalTimePR4_Type = Unsigned32
_F3PtpTSStatsTotalTimePR4_Object = MibTableColumn
f3PtpTSStatsTotalTimePR4 = _F3PtpTSStatsTotalTimePR4_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 10, 1, 9),
    _F3PtpTSStatsTotalTimePR4_Type()
)
f3PtpTSStatsTotalTimePR4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpTSStatsTotalTimePR4.setStatus("current")
_F3PtpTSStatsTotalTimePR3_Type = Unsigned32
_F3PtpTSStatsTotalTimePR3_Object = MibTableColumn
f3PtpTSStatsTotalTimePR3 = _F3PtpTSStatsTotalTimePR3_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 10, 1, 10),
    _F3PtpTSStatsTotalTimePR3_Type()
)
f3PtpTSStatsTotalTimePR3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpTSStatsTotalTimePR3.setStatus("current")
_F3PtpTSHistoryTable_Object = MibTable
f3PtpTSHistoryTable = _F3PtpTSHistoryTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 11)
)
if mibBuilder.loadTexts:
    f3PtpTSHistoryTable.setStatus("current")
_F3PtpTSHistoryEntry_Object = MibTableRow
f3PtpTSHistoryEntry = _F3PtpTSHistoryEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 11, 1)
)
f3PtpTSHistoryEntry.setIndexNames(
    (0, "CM-ENTITY-MIB", "neIndex"),
    (0, "F3-PTP-MIB", "f3PtpTSIndex"),
    (0, "F3-PTP-MIB", "f3PtpTSStatsIndex"),
    (0, "F3-PTP-MIB", "f3PtpTSHistoryIndex"),
)
if mibBuilder.loadTexts:
    f3PtpTSHistoryEntry.setStatus("current")


class _F3PtpTSHistoryIndex_Type(Integer32):
    """Custom type f3PtpTSHistoryIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_F3PtpTSHistoryIndex_Type.__name__ = "Integer32"
_F3PtpTSHistoryIndex_Object = MibTableColumn
f3PtpTSHistoryIndex = _F3PtpTSHistoryIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 11, 1, 1),
    _F3PtpTSHistoryIndex_Type()
)
f3PtpTSHistoryIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    f3PtpTSHistoryIndex.setStatus("current")
_F3PtpTSHistoryTime_Type = DateAndTime
_F3PtpTSHistoryTime_Object = MibTableColumn
f3PtpTSHistoryTime = _F3PtpTSHistoryTime_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 11, 1, 2),
    _F3PtpTSHistoryTime_Type()
)
f3PtpTSHistoryTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpTSHistoryTime.setStatus("current")
_F3PtpTSHistoryValid_Type = TruthValue
_F3PtpTSHistoryValid_Object = MibTableColumn
f3PtpTSHistoryValid = _F3PtpTSHistoryValid_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 11, 1, 3),
    _F3PtpTSHistoryValid_Type()
)
f3PtpTSHistoryValid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpTSHistoryValid.setStatus("current")
_F3PtpTSHistoryAction_Type = CmPmBinAction
_F3PtpTSHistoryAction_Object = MibTableColumn
f3PtpTSHistoryAction = _F3PtpTSHistoryAction_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 11, 1, 4),
    _F3PtpTSHistoryAction_Type()
)
f3PtpTSHistoryAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3PtpTSHistoryAction.setStatus("current")
_F3PtpTSHistoryTotalTimeCR5_Type = Unsigned32
_F3PtpTSHistoryTotalTimeCR5_Object = MibTableColumn
f3PtpTSHistoryTotalTimeCR5 = _F3PtpTSHistoryTotalTimeCR5_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 11, 1, 5),
    _F3PtpTSHistoryTotalTimeCR5_Type()
)
f3PtpTSHistoryTotalTimeCR5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpTSHistoryTotalTimeCR5.setStatus("current")
_F3PtpTSHistoryTotalTimeCR4_Type = Unsigned32
_F3PtpTSHistoryTotalTimeCR4_Object = MibTableColumn
f3PtpTSHistoryTotalTimeCR4 = _F3PtpTSHistoryTotalTimeCR4_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 11, 1, 6),
    _F3PtpTSHistoryTotalTimeCR4_Type()
)
f3PtpTSHistoryTotalTimeCR4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpTSHistoryTotalTimeCR4.setStatus("current")
_F3PtpTSHistoryTotalTimeCR3_Type = Unsigned32
_F3PtpTSHistoryTotalTimeCR3_Object = MibTableColumn
f3PtpTSHistoryTotalTimeCR3 = _F3PtpTSHistoryTotalTimeCR3_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 11, 1, 7),
    _F3PtpTSHistoryTotalTimeCR3_Type()
)
f3PtpTSHistoryTotalTimeCR3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpTSHistoryTotalTimeCR3.setStatus("current")
_F3PtpTSHistoryTotalTimePR5_Type = Unsigned32
_F3PtpTSHistoryTotalTimePR5_Object = MibTableColumn
f3PtpTSHistoryTotalTimePR5 = _F3PtpTSHistoryTotalTimePR5_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 11, 1, 8),
    _F3PtpTSHistoryTotalTimePR5_Type()
)
f3PtpTSHistoryTotalTimePR5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpTSHistoryTotalTimePR5.setStatus("current")
_F3PtpTSHistoryTotalTimePR4_Type = Unsigned32
_F3PtpTSHistoryTotalTimePR4_Object = MibTableColumn
f3PtpTSHistoryTotalTimePR4 = _F3PtpTSHistoryTotalTimePR4_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 11, 1, 9),
    _F3PtpTSHistoryTotalTimePR4_Type()
)
f3PtpTSHistoryTotalTimePR4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpTSHistoryTotalTimePR4.setStatus("current")
_F3PtpTSHistoryTotalTimePR3_Type = Unsigned32
_F3PtpTSHistoryTotalTimePR3_Object = MibTableColumn
f3PtpTSHistoryTotalTimePR3 = _F3PtpTSHistoryTotalTimePR3_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 11, 1, 10),
    _F3PtpTSHistoryTotalTimePR3_Type()
)
f3PtpTSHistoryTotalTimePR3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpTSHistoryTotalTimePR3.setStatus("current")
_F3PtpTSThresholdTable_Object = MibTable
f3PtpTSThresholdTable = _F3PtpTSThresholdTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 12)
)
if mibBuilder.loadTexts:
    f3PtpTSThresholdTable.setStatus("current")
_F3PtpTSThresholdEntry_Object = MibTableRow
f3PtpTSThresholdEntry = _F3PtpTSThresholdEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 12, 1)
)
f3PtpTSThresholdEntry.setIndexNames(
    (0, "CM-ENTITY-MIB", "neIndex"),
    (0, "F3-PTP-MIB", "f3PtpTSIndex"),
    (0, "F3-PTP-MIB", "f3PtpTSStatsIndex"),
    (0, "F3-PTP-MIB", "f3PtpTSThresholdIndex"),
)
if mibBuilder.loadTexts:
    f3PtpTSThresholdEntry.setStatus("current")


class _F3PtpTSThresholdIndex_Type(Integer32):
    """Custom type f3PtpTSThresholdIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_F3PtpTSThresholdIndex_Type.__name__ = "Integer32"
_F3PtpTSThresholdIndex_Object = MibTableColumn
f3PtpTSThresholdIndex = _F3PtpTSThresholdIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 12, 1, 1),
    _F3PtpTSThresholdIndex_Type()
)
f3PtpTSThresholdIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    f3PtpTSThresholdIndex.setStatus("current")
_F3PtpTSThresholdInterval_Type = CmPmIntervalType
_F3PtpTSThresholdInterval_Object = MibTableColumn
f3PtpTSThresholdInterval = _F3PtpTSThresholdInterval_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 12, 1, 2),
    _F3PtpTSThresholdInterval_Type()
)
f3PtpTSThresholdInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpTSThresholdInterval.setStatus("current")
_F3PtpTSThresholdVariable_Type = VariablePointer
_F3PtpTSThresholdVariable_Object = MibTableColumn
f3PtpTSThresholdVariable = _F3PtpTSThresholdVariable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 12, 1, 3),
    _F3PtpTSThresholdVariable_Type()
)
f3PtpTSThresholdVariable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpTSThresholdVariable.setStatus("current")
_F3PtpTSThresholdValueLo_Type = Unsigned32
_F3PtpTSThresholdValueLo_Object = MibTableColumn
f3PtpTSThresholdValueLo = _F3PtpTSThresholdValueLo_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 12, 1, 4),
    _F3PtpTSThresholdValueLo_Type()
)
f3PtpTSThresholdValueLo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3PtpTSThresholdValueLo.setStatus("current")
_F3PtpTSThresholdValueHi_Type = Unsigned32
_F3PtpTSThresholdValueHi_Object = MibTableColumn
f3PtpTSThresholdValueHi = _F3PtpTSThresholdValueHi_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 12, 1, 5),
    _F3PtpTSThresholdValueHi_Type()
)
f3PtpTSThresholdValueHi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3PtpTSThresholdValueHi.setStatus("current")
_F3PtpTSThresholdMonValue_Type = PerfCounter64
_F3PtpTSThresholdMonValue_Object = MibTableColumn
f3PtpTSThresholdMonValue = _F3PtpTSThresholdMonValue_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 12, 1, 6),
    _F3PtpTSThresholdMonValue_Type()
)
f3PtpTSThresholdMonValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpTSThresholdMonValue.setStatus("current")
_F3PtpMCIStatsTable_Object = MibTable
f3PtpMCIStatsTable = _F3PtpMCIStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 13)
)
if mibBuilder.loadTexts:
    f3PtpMCIStatsTable.setStatus("current")
_F3PtpMCIStatsEntry_Object = MibTableRow
f3PtpMCIStatsEntry = _F3PtpMCIStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 13, 1)
)
f3PtpMCIStatsEntry.setIndexNames(
    (0, "CM-ENTITY-MIB", "neIndex"),
    (0, "F3-PTP-MIB", "f3PtpBCIndex"),
    (0, "F3-PTP-MIB", "f3PtpMCIIndex"),
    (0, "F3-PTP-MIB", "f3PtpMCIStatsIndex"),
)
if mibBuilder.loadTexts:
    f3PtpMCIStatsEntry.setStatus("current")


class _F3PtpMCIStatsIndex_Type(Integer32):
    """Custom type f3PtpMCIStatsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_F3PtpMCIStatsIndex_Type.__name__ = "Integer32"
_F3PtpMCIStatsIndex_Object = MibTableColumn
f3PtpMCIStatsIndex = _F3PtpMCIStatsIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 13, 1, 1),
    _F3PtpMCIStatsIndex_Type()
)
f3PtpMCIStatsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    f3PtpMCIStatsIndex.setStatus("current")
_F3PtpMCIStatsIntervalType_Type = CmPmIntervalType
_F3PtpMCIStatsIntervalType_Object = MibTableColumn
f3PtpMCIStatsIntervalType = _F3PtpMCIStatsIntervalType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 13, 1, 2),
    _F3PtpMCIStatsIntervalType_Type()
)
f3PtpMCIStatsIntervalType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpMCIStatsIntervalType.setStatus("current")
_F3PtpMCIStatsValid_Type = TruthValue
_F3PtpMCIStatsValid_Object = MibTableColumn
f3PtpMCIStatsValid = _F3PtpMCIStatsValid_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 13, 1, 3),
    _F3PtpMCIStatsValid_Type()
)
f3PtpMCIStatsValid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpMCIStatsValid.setStatus("current")
_F3PtpMCIStatsAction_Type = CmPmBinAction
_F3PtpMCIStatsAction_Object = MibTableColumn
f3PtpMCIStatsAction = _F3PtpMCIStatsAction_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 13, 1, 4),
    _F3PtpMCIStatsAction_Type()
)
f3PtpMCIStatsAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3PtpMCIStatsAction.setStatus("current")
_F3PtpMCIStatsPtpDiscards_Type = PerfCounter64
_F3PtpMCIStatsPtpDiscards_Object = MibTableColumn
f3PtpMCIStatsPtpDiscards = _F3PtpMCIStatsPtpDiscards_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 13, 1, 5),
    _F3PtpMCIStatsPtpDiscards_Type()
)
f3PtpMCIStatsPtpDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpMCIStatsPtpDiscards.setStatus("current")
_F3PtpMCIStatsSyncDeniedEvents_Type = PerfCounter64
_F3PtpMCIStatsSyncDeniedEvents_Object = MibTableColumn
f3PtpMCIStatsSyncDeniedEvents = _F3PtpMCIStatsSyncDeniedEvents_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 13, 1, 6),
    _F3PtpMCIStatsSyncDeniedEvents_Type()
)
f3PtpMCIStatsSyncDeniedEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpMCIStatsSyncDeniedEvents.setStatus("current")
_F3PtpMCIStatsDelayRspDeniedEvents_Type = PerfCounter64
_F3PtpMCIStatsDelayRspDeniedEvents_Object = MibTableColumn
f3PtpMCIStatsDelayRspDeniedEvents = _F3PtpMCIStatsDelayRspDeniedEvents_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 13, 1, 7),
    _F3PtpMCIStatsDelayRspDeniedEvents_Type()
)
f3PtpMCIStatsDelayRspDeniedEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpMCIStatsDelayRspDeniedEvents.setStatus("current")
_F3PtpMCIStatsAnnounceDeniedEvents_Type = PerfCounter64
_F3PtpMCIStatsAnnounceDeniedEvents_Object = MibTableColumn
f3PtpMCIStatsAnnounceDeniedEvents = _F3PtpMCIStatsAnnounceDeniedEvents_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 13, 1, 8),
    _F3PtpMCIStatsAnnounceDeniedEvents_Type()
)
f3PtpMCIStatsAnnounceDeniedEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpMCIStatsAnnounceDeniedEvents.setStatus("current")
_F3PtpMCIStatsSyncCancelledEvents_Type = PerfCounter64
_F3PtpMCIStatsSyncCancelledEvents_Object = MibTableColumn
f3PtpMCIStatsSyncCancelledEvents = _F3PtpMCIStatsSyncCancelledEvents_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 13, 1, 9),
    _F3PtpMCIStatsSyncCancelledEvents_Type()
)
f3PtpMCIStatsSyncCancelledEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpMCIStatsSyncCancelledEvents.setStatus("current")
_F3PtpMCIStatsDelayRspCancelledEvents_Type = PerfCounter64
_F3PtpMCIStatsDelayRspCancelledEvents_Object = MibTableColumn
f3PtpMCIStatsDelayRspCancelledEvents = _F3PtpMCIStatsDelayRspCancelledEvents_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 13, 1, 10),
    _F3PtpMCIStatsDelayRspCancelledEvents_Type()
)
f3PtpMCIStatsDelayRspCancelledEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpMCIStatsDelayRspCancelledEvents.setStatus("current")
_F3PtpMCIStatsAnnounceCancelledEvents_Type = PerfCounter64
_F3PtpMCIStatsAnnounceCancelledEvents_Object = MibTableColumn
f3PtpMCIStatsAnnounceCancelledEvents = _F3PtpMCIStatsAnnounceCancelledEvents_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 13, 1, 11),
    _F3PtpMCIStatsAnnounceCancelledEvents_Type()
)
f3PtpMCIStatsAnnounceCancelledEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpMCIStatsAnnounceCancelledEvents.setStatus("current")
_F3PtpMCIStatsDynamicSlavesLearnt_Type = PerfCounter64
_F3PtpMCIStatsDynamicSlavesLearnt_Object = MibTableColumn
f3PtpMCIStatsDynamicSlavesLearnt = _F3PtpMCIStatsDynamicSlavesLearnt_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 13, 1, 12),
    _F3PtpMCIStatsDynamicSlavesLearnt_Type()
)
f3PtpMCIStatsDynamicSlavesLearnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpMCIStatsDynamicSlavesLearnt.setStatus("current")
_F3PtpMCIStatsDynamicSlavesDropped_Type = PerfCounter64
_F3PtpMCIStatsDynamicSlavesDropped_Object = MibTableColumn
f3PtpMCIStatsDynamicSlavesDropped = _F3PtpMCIStatsDynamicSlavesDropped_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 13, 1, 13),
    _F3PtpMCIStatsDynamicSlavesDropped_Type()
)
f3PtpMCIStatsDynamicSlavesDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpMCIStatsDynamicSlavesDropped.setStatus("current")
_F3PtpMCIHistoryTable_Object = MibTable
f3PtpMCIHistoryTable = _F3PtpMCIHistoryTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 14)
)
if mibBuilder.loadTexts:
    f3PtpMCIHistoryTable.setStatus("current")
_F3PtpMCIHistoryEntry_Object = MibTableRow
f3PtpMCIHistoryEntry = _F3PtpMCIHistoryEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 14, 1)
)
f3PtpMCIHistoryEntry.setIndexNames(
    (0, "CM-ENTITY-MIB", "neIndex"),
    (0, "F3-PTP-MIB", "f3PtpBCIndex"),
    (0, "F3-PTP-MIB", "f3PtpMCIIndex"),
    (0, "F3-PTP-MIB", "f3PtpMCIStatsIndex"),
    (0, "F3-PTP-MIB", "f3PtpMCIHistoryIndex"),
)
if mibBuilder.loadTexts:
    f3PtpMCIHistoryEntry.setStatus("current")


class _F3PtpMCIHistoryIndex_Type(Integer32):
    """Custom type f3PtpMCIHistoryIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_F3PtpMCIHistoryIndex_Type.__name__ = "Integer32"
_F3PtpMCIHistoryIndex_Object = MibTableColumn
f3PtpMCIHistoryIndex = _F3PtpMCIHistoryIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 14, 1, 1),
    _F3PtpMCIHistoryIndex_Type()
)
f3PtpMCIHistoryIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    f3PtpMCIHistoryIndex.setStatus("current")
_F3PtpMCIHistoryTime_Type = DateAndTime
_F3PtpMCIHistoryTime_Object = MibTableColumn
f3PtpMCIHistoryTime = _F3PtpMCIHistoryTime_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 14, 1, 2),
    _F3PtpMCIHistoryTime_Type()
)
f3PtpMCIHistoryTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpMCIHistoryTime.setStatus("current")
_F3PtpMCIHistoryValid_Type = TruthValue
_F3PtpMCIHistoryValid_Object = MibTableColumn
f3PtpMCIHistoryValid = _F3PtpMCIHistoryValid_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 14, 1, 3),
    _F3PtpMCIHistoryValid_Type()
)
f3PtpMCIHistoryValid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpMCIHistoryValid.setStatus("current")
_F3PtpMCIHistoryAction_Type = CmPmBinAction
_F3PtpMCIHistoryAction_Object = MibTableColumn
f3PtpMCIHistoryAction = _F3PtpMCIHistoryAction_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 14, 1, 4),
    _F3PtpMCIHistoryAction_Type()
)
f3PtpMCIHistoryAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3PtpMCIHistoryAction.setStatus("current")
_F3PtpMCIHistoryPtpDiscards_Type = PerfCounter64
_F3PtpMCIHistoryPtpDiscards_Object = MibTableColumn
f3PtpMCIHistoryPtpDiscards = _F3PtpMCIHistoryPtpDiscards_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 14, 1, 5),
    _F3PtpMCIHistoryPtpDiscards_Type()
)
f3PtpMCIHistoryPtpDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpMCIHistoryPtpDiscards.setStatus("current")
_F3PtpMCIHistorySyncDeniedEvents_Type = PerfCounter64
_F3PtpMCIHistorySyncDeniedEvents_Object = MibTableColumn
f3PtpMCIHistorySyncDeniedEvents = _F3PtpMCIHistorySyncDeniedEvents_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 14, 1, 6),
    _F3PtpMCIHistorySyncDeniedEvents_Type()
)
f3PtpMCIHistorySyncDeniedEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpMCIHistorySyncDeniedEvents.setStatus("current")
_F3PtpMCIHistoryDelayRspDeniedEvents_Type = PerfCounter64
_F3PtpMCIHistoryDelayRspDeniedEvents_Object = MibTableColumn
f3PtpMCIHistoryDelayRspDeniedEvents = _F3PtpMCIHistoryDelayRspDeniedEvents_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 14, 1, 7),
    _F3PtpMCIHistoryDelayRspDeniedEvents_Type()
)
f3PtpMCIHistoryDelayRspDeniedEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpMCIHistoryDelayRspDeniedEvents.setStatus("current")
_F3PtpMCIHistoryAnnounceDeniedEvents_Type = PerfCounter64
_F3PtpMCIHistoryAnnounceDeniedEvents_Object = MibTableColumn
f3PtpMCIHistoryAnnounceDeniedEvents = _F3PtpMCIHistoryAnnounceDeniedEvents_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 14, 1, 8),
    _F3PtpMCIHistoryAnnounceDeniedEvents_Type()
)
f3PtpMCIHistoryAnnounceDeniedEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpMCIHistoryAnnounceDeniedEvents.setStatus("current")
_F3PtpMCIHistorySyncCancelledEvents_Type = PerfCounter64
_F3PtpMCIHistorySyncCancelledEvents_Object = MibTableColumn
f3PtpMCIHistorySyncCancelledEvents = _F3PtpMCIHistorySyncCancelledEvents_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 14, 1, 9),
    _F3PtpMCIHistorySyncCancelledEvents_Type()
)
f3PtpMCIHistorySyncCancelledEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpMCIHistorySyncCancelledEvents.setStatus("current")
_F3PtpMCIHistoryDelayRspCancelledEvents_Type = PerfCounter64
_F3PtpMCIHistoryDelayRspCancelledEvents_Object = MibTableColumn
f3PtpMCIHistoryDelayRspCancelledEvents = _F3PtpMCIHistoryDelayRspCancelledEvents_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 14, 1, 10),
    _F3PtpMCIHistoryDelayRspCancelledEvents_Type()
)
f3PtpMCIHistoryDelayRspCancelledEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpMCIHistoryDelayRspCancelledEvents.setStatus("current")
_F3PtpMCIHistoryAnnounceCancelledEvents_Type = PerfCounter64
_F3PtpMCIHistoryAnnounceCancelledEvents_Object = MibTableColumn
f3PtpMCIHistoryAnnounceCancelledEvents = _F3PtpMCIHistoryAnnounceCancelledEvents_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 14, 1, 11),
    _F3PtpMCIHistoryAnnounceCancelledEvents_Type()
)
f3PtpMCIHistoryAnnounceCancelledEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpMCIHistoryAnnounceCancelledEvents.setStatus("current")
_F3PtpMCIHistoryDynamicSlavesLearnt_Type = PerfCounter64
_F3PtpMCIHistoryDynamicSlavesLearnt_Object = MibTableColumn
f3PtpMCIHistoryDynamicSlavesLearnt = _F3PtpMCIHistoryDynamicSlavesLearnt_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 14, 1, 12),
    _F3PtpMCIHistoryDynamicSlavesLearnt_Type()
)
f3PtpMCIHistoryDynamicSlavesLearnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpMCIHistoryDynamicSlavesLearnt.setStatus("current")
_F3PtpMCIHistoryDynamicSlavesDropped_Type = PerfCounter64
_F3PtpMCIHistoryDynamicSlavesDropped_Object = MibTableColumn
f3PtpMCIHistoryDynamicSlavesDropped = _F3PtpMCIHistoryDynamicSlavesDropped_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 14, 1, 13),
    _F3PtpMCIHistoryDynamicSlavesDropped_Type()
)
f3PtpMCIHistoryDynamicSlavesDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpMCIHistoryDynamicSlavesDropped.setStatus("current")
_F3PtpMCIThresholdTable_Object = MibTable
f3PtpMCIThresholdTable = _F3PtpMCIThresholdTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 15)
)
if mibBuilder.loadTexts:
    f3PtpMCIThresholdTable.setStatus("current")
_F3PtpMCIThresholdEntry_Object = MibTableRow
f3PtpMCIThresholdEntry = _F3PtpMCIThresholdEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 15, 1)
)
f3PtpMCIThresholdEntry.setIndexNames(
    (0, "CM-ENTITY-MIB", "neIndex"),
    (0, "F3-PTP-MIB", "f3PtpBCIndex"),
    (0, "F3-PTP-MIB", "f3PtpMCIIndex"),
    (0, "F3-PTP-MIB", "f3PtpMCIStatsIndex"),
    (0, "F3-PTP-MIB", "f3PtpMCIThresholdIndex"),
)
if mibBuilder.loadTexts:
    f3PtpMCIThresholdEntry.setStatus("current")


class _F3PtpMCIThresholdIndex_Type(Integer32):
    """Custom type f3PtpMCIThresholdIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_F3PtpMCIThresholdIndex_Type.__name__ = "Integer32"
_F3PtpMCIThresholdIndex_Object = MibTableColumn
f3PtpMCIThresholdIndex = _F3PtpMCIThresholdIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 15, 1, 1),
    _F3PtpMCIThresholdIndex_Type()
)
f3PtpMCIThresholdIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    f3PtpMCIThresholdIndex.setStatus("current")
_F3PtpMCIThresholdInterval_Type = CmPmIntervalType
_F3PtpMCIThresholdInterval_Object = MibTableColumn
f3PtpMCIThresholdInterval = _F3PtpMCIThresholdInterval_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 15, 1, 2),
    _F3PtpMCIThresholdInterval_Type()
)
f3PtpMCIThresholdInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpMCIThresholdInterval.setStatus("current")
_F3PtpMCIThresholdVariable_Type = VariablePointer
_F3PtpMCIThresholdVariable_Object = MibTableColumn
f3PtpMCIThresholdVariable = _F3PtpMCIThresholdVariable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 15, 1, 3),
    _F3PtpMCIThresholdVariable_Type()
)
f3PtpMCIThresholdVariable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpMCIThresholdVariable.setStatus("current")
_F3PtpMCIThresholdValueLo_Type = Unsigned32
_F3PtpMCIThresholdValueLo_Object = MibTableColumn
f3PtpMCIThresholdValueLo = _F3PtpMCIThresholdValueLo_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 15, 1, 4),
    _F3PtpMCIThresholdValueLo_Type()
)
f3PtpMCIThresholdValueLo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3PtpMCIThresholdValueLo.setStatus("current")
_F3PtpMCIThresholdValueHi_Type = Unsigned32
_F3PtpMCIThresholdValueHi_Object = MibTableColumn
f3PtpMCIThresholdValueHi = _F3PtpMCIThresholdValueHi_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 15, 1, 5),
    _F3PtpMCIThresholdValueHi_Type()
)
f3PtpMCIThresholdValueHi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3PtpMCIThresholdValueHi.setStatus("current")
_F3PtpMCIThresholdMonValue_Type = PerfCounter64
_F3PtpMCIThresholdMonValue_Object = MibTableColumn
f3PtpMCIThresholdMonValue = _F3PtpMCIThresholdMonValue_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 15, 1, 6),
    _F3PtpMCIThresholdMonValue_Type()
)
f3PtpMCIThresholdMonValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpMCIThresholdMonValue.setStatus("current")
_F3PtpRemoteSlaveStatsTable_Object = MibTable
f3PtpRemoteSlaveStatsTable = _F3PtpRemoteSlaveStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 16)
)
if mibBuilder.loadTexts:
    f3PtpRemoteSlaveStatsTable.setStatus("current")
_F3PtpRemoteSlaveStatsEntry_Object = MibTableRow
f3PtpRemoteSlaveStatsEntry = _F3PtpRemoteSlaveStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 16, 1)
)
f3PtpRemoteSlaveStatsEntry.setIndexNames(
    (0, "CM-ENTITY-MIB", "neIndex"),
    (0, "F3-PTP-MIB", "f3PtpBCIndex"),
    (0, "F3-PTP-MIB", "f3PtpMCIIndex"),
    (0, "F3-PTP-MIB", "f3PtpRemoteSlaveStatsSlaveType"),
    (0, "F3-PTP-MIB", "f3PtpRemoteSlaveStatsSlaveIndex"),
    (0, "F3-PTP-MIB", "f3PtpRemoteSlaveStatsIndex"),
)
if mibBuilder.loadTexts:
    f3PtpRemoteSlaveStatsEntry.setStatus("current")
_F3PtpRemoteSlaveStatsSlaveType_Type = RemoteSlaveType
_F3PtpRemoteSlaveStatsSlaveType_Object = MibTableColumn
f3PtpRemoteSlaveStatsSlaveType = _F3PtpRemoteSlaveStatsSlaveType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 16, 1, 1),
    _F3PtpRemoteSlaveStatsSlaveType_Type()
)
f3PtpRemoteSlaveStatsSlaveType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    f3PtpRemoteSlaveStatsSlaveType.setStatus("current")
_F3PtpRemoteSlaveStatsSlaveIndex_Type = Integer32
_F3PtpRemoteSlaveStatsSlaveIndex_Object = MibTableColumn
f3PtpRemoteSlaveStatsSlaveIndex = _F3PtpRemoteSlaveStatsSlaveIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 16, 1, 2),
    _F3PtpRemoteSlaveStatsSlaveIndex_Type()
)
f3PtpRemoteSlaveStatsSlaveIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    f3PtpRemoteSlaveStatsSlaveIndex.setStatus("current")


class _F3PtpRemoteSlaveStatsIndex_Type(Integer32):
    """Custom type f3PtpRemoteSlaveStatsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_F3PtpRemoteSlaveStatsIndex_Type.__name__ = "Integer32"
_F3PtpRemoteSlaveStatsIndex_Object = MibTableColumn
f3PtpRemoteSlaveStatsIndex = _F3PtpRemoteSlaveStatsIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 16, 1, 3),
    _F3PtpRemoteSlaveStatsIndex_Type()
)
f3PtpRemoteSlaveStatsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    f3PtpRemoteSlaveStatsIndex.setStatus("current")
_F3PtpRemoteSlaveStatsIntervalType_Type = CmPmIntervalType
_F3PtpRemoteSlaveStatsIntervalType_Object = MibTableColumn
f3PtpRemoteSlaveStatsIntervalType = _F3PtpRemoteSlaveStatsIntervalType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 16, 1, 4),
    _F3PtpRemoteSlaveStatsIntervalType_Type()
)
f3PtpRemoteSlaveStatsIntervalType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpRemoteSlaveStatsIntervalType.setStatus("current")
_F3PtpRemoteSlaveStatsValid_Type = TruthValue
_F3PtpRemoteSlaveStatsValid_Object = MibTableColumn
f3PtpRemoteSlaveStatsValid = _F3PtpRemoteSlaveStatsValid_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 16, 1, 5),
    _F3PtpRemoteSlaveStatsValid_Type()
)
f3PtpRemoteSlaveStatsValid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpRemoteSlaveStatsValid.setStatus("current")
_F3PtpRemoteSlaveStatsAction_Type = CmPmBinAction
_F3PtpRemoteSlaveStatsAction_Object = MibTableColumn
f3PtpRemoteSlaveStatsAction = _F3PtpRemoteSlaveStatsAction_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 16, 1, 6),
    _F3PtpRemoteSlaveStatsAction_Type()
)
f3PtpRemoteSlaveStatsAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3PtpRemoteSlaveStatsAction.setStatus("current")
_F3PtpRemoteSlaveStatsSyncMsgsGen_Type = PerfCounter64
_F3PtpRemoteSlaveStatsSyncMsgsGen_Object = MibTableColumn
f3PtpRemoteSlaveStatsSyncMsgsGen = _F3PtpRemoteSlaveStatsSyncMsgsGen_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 16, 1, 7),
    _F3PtpRemoteSlaveStatsSyncMsgsGen_Type()
)
f3PtpRemoteSlaveStatsSyncMsgsGen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpRemoteSlaveStatsSyncMsgsGen.setStatus("current")
_F3PtpRemoteSlaveStatsDelayRspMsgsGen_Type = PerfCounter64
_F3PtpRemoteSlaveStatsDelayRspMsgsGen_Object = MibTableColumn
f3PtpRemoteSlaveStatsDelayRspMsgsGen = _F3PtpRemoteSlaveStatsDelayRspMsgsGen_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 16, 1, 8),
    _F3PtpRemoteSlaveStatsDelayRspMsgsGen_Type()
)
f3PtpRemoteSlaveStatsDelayRspMsgsGen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpRemoteSlaveStatsDelayRspMsgsGen.setStatus("current")
_F3PtpRemoteSlaveStatsAnnounceMsgsGen_Type = PerfCounter64
_F3PtpRemoteSlaveStatsAnnounceMsgsGen_Object = MibTableColumn
f3PtpRemoteSlaveStatsAnnounceMsgsGen = _F3PtpRemoteSlaveStatsAnnounceMsgsGen_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 16, 1, 9),
    _F3PtpRemoteSlaveStatsAnnounceMsgsGen_Type()
)
f3PtpRemoteSlaveStatsAnnounceMsgsGen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpRemoteSlaveStatsAnnounceMsgsGen.setStatus("current")
_F3PtpRemoteSlaveStatsSignallingMsgsGen_Type = PerfCounter64
_F3PtpRemoteSlaveStatsSignallingMsgsGen_Object = MibTableColumn
f3PtpRemoteSlaveStatsSignallingMsgsGen = _F3PtpRemoteSlaveStatsSignallingMsgsGen_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 16, 1, 10),
    _F3PtpRemoteSlaveStatsSignallingMsgsGen_Type()
)
f3PtpRemoteSlaveStatsSignallingMsgsGen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpRemoteSlaveStatsSignallingMsgsGen.setStatus("current")
_F3PtpRemoteSlaveStatsDelayReqMsgsRx_Type = PerfCounter64
_F3PtpRemoteSlaveStatsDelayReqMsgsRx_Object = MibTableColumn
f3PtpRemoteSlaveStatsDelayReqMsgsRx = _F3PtpRemoteSlaveStatsDelayReqMsgsRx_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 16, 1, 11),
    _F3PtpRemoteSlaveStatsDelayReqMsgsRx_Type()
)
f3PtpRemoteSlaveStatsDelayReqMsgsRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpRemoteSlaveStatsDelayReqMsgsRx.setStatus("current")
_F3PtpRemoteSlaveStatsSignallingMsgsRx_Type = PerfCounter64
_F3PtpRemoteSlaveStatsSignallingMsgsRx_Object = MibTableColumn
f3PtpRemoteSlaveStatsSignallingMsgsRx = _F3PtpRemoteSlaveStatsSignallingMsgsRx_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 16, 1, 12),
    _F3PtpRemoteSlaveStatsSignallingMsgsRx_Type()
)
f3PtpRemoteSlaveStatsSignallingMsgsRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpRemoteSlaveStatsSignallingMsgsRx.setStatus("current")
_F3PtpRemoteSlaveStatsDelayReqMsgsDropped_Type = PerfCounter64
_F3PtpRemoteSlaveStatsDelayReqMsgsDropped_Object = MibTableColumn
f3PtpRemoteSlaveStatsDelayReqMsgsDropped = _F3PtpRemoteSlaveStatsDelayReqMsgsDropped_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 16, 1, 13),
    _F3PtpRemoteSlaveStatsDelayReqMsgsDropped_Type()
)
f3PtpRemoteSlaveStatsDelayReqMsgsDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpRemoteSlaveStatsDelayReqMsgsDropped.setStatus("current")
_F3PtpRemoteSlaveStatsInvalidTLVLenDiscards_Type = PerfCounter64
_F3PtpRemoteSlaveStatsInvalidTLVLenDiscards_Object = MibTableColumn
f3PtpRemoteSlaveStatsInvalidTLVLenDiscards = _F3PtpRemoteSlaveStatsInvalidTLVLenDiscards_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 16, 1, 14),
    _F3PtpRemoteSlaveStatsInvalidTLVLenDiscards_Type()
)
f3PtpRemoteSlaveStatsInvalidTLVLenDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpRemoteSlaveStatsInvalidTLVLenDiscards.setStatus("current")
_F3PtpRemoteSlaveStatsInvalidTLVTypeDiscards_Type = PerfCounter64
_F3PtpRemoteSlaveStatsInvalidTLVTypeDiscards_Object = MibTableColumn
f3PtpRemoteSlaveStatsInvalidTLVTypeDiscards = _F3PtpRemoteSlaveStatsInvalidTLVTypeDiscards_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 16, 1, 15),
    _F3PtpRemoteSlaveStatsInvalidTLVTypeDiscards_Type()
)
f3PtpRemoteSlaveStatsInvalidTLVTypeDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpRemoteSlaveStatsInvalidTLVTypeDiscards.setStatus("current")
_F3PtpRemoteSlaveStatsTimesSyncLeaseExp_Type = PerfCounter64
_F3PtpRemoteSlaveStatsTimesSyncLeaseExp_Object = MibTableColumn
f3PtpRemoteSlaveStatsTimesSyncLeaseExp = _F3PtpRemoteSlaveStatsTimesSyncLeaseExp_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 16, 1, 16),
    _F3PtpRemoteSlaveStatsTimesSyncLeaseExp_Type()
)
f3PtpRemoteSlaveStatsTimesSyncLeaseExp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpRemoteSlaveStatsTimesSyncLeaseExp.setStatus("current")
_F3PtpRemoteSlaveStatsTimesDelayRspLeaseExp_Type = PerfCounter64
_F3PtpRemoteSlaveStatsTimesDelayRspLeaseExp_Object = MibTableColumn
f3PtpRemoteSlaveStatsTimesDelayRspLeaseExp = _F3PtpRemoteSlaveStatsTimesDelayRspLeaseExp_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 16, 1, 17),
    _F3PtpRemoteSlaveStatsTimesDelayRspLeaseExp_Type()
)
f3PtpRemoteSlaveStatsTimesDelayRspLeaseExp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpRemoteSlaveStatsTimesDelayRspLeaseExp.setStatus("current")
_F3PtpRemoteSlaveStatsTimesAnnounceLeaseExp_Type = PerfCounter64
_F3PtpRemoteSlaveStatsTimesAnnounceLeaseExp_Object = MibTableColumn
f3PtpRemoteSlaveStatsTimesAnnounceLeaseExp = _F3PtpRemoteSlaveStatsTimesAnnounceLeaseExp_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 16, 1, 18),
    _F3PtpRemoteSlaveStatsTimesAnnounceLeaseExp_Type()
)
f3PtpRemoteSlaveStatsTimesAnnounceLeaseExp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpRemoteSlaveStatsTimesAnnounceLeaseExp.setStatus("current")
_F3PtpRemoteSlaveHistoryTable_Object = MibTable
f3PtpRemoteSlaveHistoryTable = _F3PtpRemoteSlaveHistoryTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 17)
)
if mibBuilder.loadTexts:
    f3PtpRemoteSlaveHistoryTable.setStatus("current")
_F3PtpRemoteSlaveHistoryEntry_Object = MibTableRow
f3PtpRemoteSlaveHistoryEntry = _F3PtpRemoteSlaveHistoryEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 17, 1)
)
f3PtpRemoteSlaveHistoryEntry.setIndexNames(
    (0, "CM-ENTITY-MIB", "neIndex"),
    (0, "F3-PTP-MIB", "f3PtpBCIndex"),
    (0, "F3-PTP-MIB", "f3PtpMCIIndex"),
    (0, "F3-PTP-MIB", "f3PtpRemoteSlaveStatsSlaveType"),
    (0, "F3-PTP-MIB", "f3PtpRemoteSlaveStatsSlaveIndex"),
    (0, "F3-PTP-MIB", "f3PtpRemoteSlaveStatsIndex"),
    (0, "F3-PTP-MIB", "f3PtpRemoteSlaveHistoryIndex"),
)
if mibBuilder.loadTexts:
    f3PtpRemoteSlaveHistoryEntry.setStatus("current")


class _F3PtpRemoteSlaveHistoryIndex_Type(Integer32):
    """Custom type f3PtpRemoteSlaveHistoryIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_F3PtpRemoteSlaveHistoryIndex_Type.__name__ = "Integer32"
_F3PtpRemoteSlaveHistoryIndex_Object = MibTableColumn
f3PtpRemoteSlaveHistoryIndex = _F3PtpRemoteSlaveHistoryIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 17, 1, 1),
    _F3PtpRemoteSlaveHistoryIndex_Type()
)
f3PtpRemoteSlaveHistoryIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    f3PtpRemoteSlaveHistoryIndex.setStatus("current")
_F3PtpRemoteSlaveHistoryTime_Type = DateAndTime
_F3PtpRemoteSlaveHistoryTime_Object = MibTableColumn
f3PtpRemoteSlaveHistoryTime = _F3PtpRemoteSlaveHistoryTime_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 17, 1, 2),
    _F3PtpRemoteSlaveHistoryTime_Type()
)
f3PtpRemoteSlaveHistoryTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpRemoteSlaveHistoryTime.setStatus("current")
_F3PtpRemoteSlaveHistoryValid_Type = TruthValue
_F3PtpRemoteSlaveHistoryValid_Object = MibTableColumn
f3PtpRemoteSlaveHistoryValid = _F3PtpRemoteSlaveHistoryValid_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 17, 1, 3),
    _F3PtpRemoteSlaveHistoryValid_Type()
)
f3PtpRemoteSlaveHistoryValid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpRemoteSlaveHistoryValid.setStatus("current")
_F3PtpRemoteSlaveHistoryAction_Type = CmPmBinAction
_F3PtpRemoteSlaveHistoryAction_Object = MibTableColumn
f3PtpRemoteSlaveHistoryAction = _F3PtpRemoteSlaveHistoryAction_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 17, 1, 4),
    _F3PtpRemoteSlaveHistoryAction_Type()
)
f3PtpRemoteSlaveHistoryAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3PtpRemoteSlaveHistoryAction.setStatus("current")
_F3PtpRemoteSlaveHistorySyncMsgsGen_Type = PerfCounter64
_F3PtpRemoteSlaveHistorySyncMsgsGen_Object = MibTableColumn
f3PtpRemoteSlaveHistorySyncMsgsGen = _F3PtpRemoteSlaveHistorySyncMsgsGen_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 17, 1, 5),
    _F3PtpRemoteSlaveHistorySyncMsgsGen_Type()
)
f3PtpRemoteSlaveHistorySyncMsgsGen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpRemoteSlaveHistorySyncMsgsGen.setStatus("current")
_F3PtpRemoteSlaveHistoryDelayRspMsgsGen_Type = PerfCounter64
_F3PtpRemoteSlaveHistoryDelayRspMsgsGen_Object = MibTableColumn
f3PtpRemoteSlaveHistoryDelayRspMsgsGen = _F3PtpRemoteSlaveHistoryDelayRspMsgsGen_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 17, 1, 6),
    _F3PtpRemoteSlaveHistoryDelayRspMsgsGen_Type()
)
f3PtpRemoteSlaveHistoryDelayRspMsgsGen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpRemoteSlaveHistoryDelayRspMsgsGen.setStatus("current")
_F3PtpRemoteSlaveHistoryAnnounceMsgsGen_Type = PerfCounter64
_F3PtpRemoteSlaveHistoryAnnounceMsgsGen_Object = MibTableColumn
f3PtpRemoteSlaveHistoryAnnounceMsgsGen = _F3PtpRemoteSlaveHistoryAnnounceMsgsGen_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 17, 1, 7),
    _F3PtpRemoteSlaveHistoryAnnounceMsgsGen_Type()
)
f3PtpRemoteSlaveHistoryAnnounceMsgsGen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpRemoteSlaveHistoryAnnounceMsgsGen.setStatus("current")
_F3PtpRemoteSlaveHistorySignallingMsgsGen_Type = PerfCounter64
_F3PtpRemoteSlaveHistorySignallingMsgsGen_Object = MibTableColumn
f3PtpRemoteSlaveHistorySignallingMsgsGen = _F3PtpRemoteSlaveHistorySignallingMsgsGen_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 17, 1, 8),
    _F3PtpRemoteSlaveHistorySignallingMsgsGen_Type()
)
f3PtpRemoteSlaveHistorySignallingMsgsGen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpRemoteSlaveHistorySignallingMsgsGen.setStatus("current")
_F3PtpRemoteSlaveHistoryDelayReqMsgsRx_Type = PerfCounter64
_F3PtpRemoteSlaveHistoryDelayReqMsgsRx_Object = MibTableColumn
f3PtpRemoteSlaveHistoryDelayReqMsgsRx = _F3PtpRemoteSlaveHistoryDelayReqMsgsRx_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 17, 1, 9),
    _F3PtpRemoteSlaveHistoryDelayReqMsgsRx_Type()
)
f3PtpRemoteSlaveHistoryDelayReqMsgsRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpRemoteSlaveHistoryDelayReqMsgsRx.setStatus("current")
_F3PtpRemoteSlaveHistorySignallingMsgsRx_Type = PerfCounter64
_F3PtpRemoteSlaveHistorySignallingMsgsRx_Object = MibTableColumn
f3PtpRemoteSlaveHistorySignallingMsgsRx = _F3PtpRemoteSlaveHistorySignallingMsgsRx_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 17, 1, 10),
    _F3PtpRemoteSlaveHistorySignallingMsgsRx_Type()
)
f3PtpRemoteSlaveHistorySignallingMsgsRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpRemoteSlaveHistorySignallingMsgsRx.setStatus("current")
_F3PtpRemoteSlaveHistoryDelayReqMsgsDropped_Type = PerfCounter64
_F3PtpRemoteSlaveHistoryDelayReqMsgsDropped_Object = MibTableColumn
f3PtpRemoteSlaveHistoryDelayReqMsgsDropped = _F3PtpRemoteSlaveHistoryDelayReqMsgsDropped_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 17, 1, 11),
    _F3PtpRemoteSlaveHistoryDelayReqMsgsDropped_Type()
)
f3PtpRemoteSlaveHistoryDelayReqMsgsDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpRemoteSlaveHistoryDelayReqMsgsDropped.setStatus("current")
_F3PtpRemoteSlaveHistoryInvalidTLVLenDiscards_Type = PerfCounter64
_F3PtpRemoteSlaveHistoryInvalidTLVLenDiscards_Object = MibTableColumn
f3PtpRemoteSlaveHistoryInvalidTLVLenDiscards = _F3PtpRemoteSlaveHistoryInvalidTLVLenDiscards_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 17, 1, 12),
    _F3PtpRemoteSlaveHistoryInvalidTLVLenDiscards_Type()
)
f3PtpRemoteSlaveHistoryInvalidTLVLenDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpRemoteSlaveHistoryInvalidTLVLenDiscards.setStatus("current")
_F3PtpRemoteSlaveHistoryInvalidTLVTypeDiscards_Type = PerfCounter64
_F3PtpRemoteSlaveHistoryInvalidTLVTypeDiscards_Object = MibTableColumn
f3PtpRemoteSlaveHistoryInvalidTLVTypeDiscards = _F3PtpRemoteSlaveHistoryInvalidTLVTypeDiscards_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 17, 1, 13),
    _F3PtpRemoteSlaveHistoryInvalidTLVTypeDiscards_Type()
)
f3PtpRemoteSlaveHistoryInvalidTLVTypeDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpRemoteSlaveHistoryInvalidTLVTypeDiscards.setStatus("current")
_F3PtpRemoteSlaveHistoryTimesSyncLeaseExp_Type = PerfCounter64
_F3PtpRemoteSlaveHistoryTimesSyncLeaseExp_Object = MibTableColumn
f3PtpRemoteSlaveHistoryTimesSyncLeaseExp = _F3PtpRemoteSlaveHistoryTimesSyncLeaseExp_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 17, 1, 14),
    _F3PtpRemoteSlaveHistoryTimesSyncLeaseExp_Type()
)
f3PtpRemoteSlaveHistoryTimesSyncLeaseExp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpRemoteSlaveHistoryTimesSyncLeaseExp.setStatus("current")
_F3PtpRemoteSlaveHistoryTimesDelayRspLeaseExp_Type = PerfCounter64
_F3PtpRemoteSlaveHistoryTimesDelayRspLeaseExp_Object = MibTableColumn
f3PtpRemoteSlaveHistoryTimesDelayRspLeaseExp = _F3PtpRemoteSlaveHistoryTimesDelayRspLeaseExp_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 17, 1, 15),
    _F3PtpRemoteSlaveHistoryTimesDelayRspLeaseExp_Type()
)
f3PtpRemoteSlaveHistoryTimesDelayRspLeaseExp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpRemoteSlaveHistoryTimesDelayRspLeaseExp.setStatus("current")
_F3PtpRemoteSlaveHistoryTimesAnnounceLeaseExp_Type = PerfCounter64
_F3PtpRemoteSlaveHistoryTimesAnnounceLeaseExp_Object = MibTableColumn
f3PtpRemoteSlaveHistoryTimesAnnounceLeaseExp = _F3PtpRemoteSlaveHistoryTimesAnnounceLeaseExp_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 17, 1, 16),
    _F3PtpRemoteSlaveHistoryTimesAnnounceLeaseExp_Type()
)
f3PtpRemoteSlaveHistoryTimesAnnounceLeaseExp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpRemoteSlaveHistoryTimesAnnounceLeaseExp.setStatus("current")
_F3PtpRemoteSlaveThresholdTable_Object = MibTable
f3PtpRemoteSlaveThresholdTable = _F3PtpRemoteSlaveThresholdTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 18)
)
if mibBuilder.loadTexts:
    f3PtpRemoteSlaveThresholdTable.setStatus("current")
_F3PtpRemoteSlaveThresholdEntry_Object = MibTableRow
f3PtpRemoteSlaveThresholdEntry = _F3PtpRemoteSlaveThresholdEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 18, 1)
)
f3PtpRemoteSlaveThresholdEntry.setIndexNames(
    (0, "CM-ENTITY-MIB", "neIndex"),
    (0, "F3-PTP-MIB", "f3PtpBCIndex"),
    (0, "F3-PTP-MIB", "f3PtpMCIIndex"),
    (0, "F3-PTP-MIB", "f3PtpRemoteSlaveStatsSlaveType"),
    (0, "F3-PTP-MIB", "f3PtpRemoteSlaveStatsSlaveIndex"),
    (0, "F3-PTP-MIB", "f3PtpRemoteSlaveStatsIndex"),
    (0, "F3-PTP-MIB", "f3PtpRemoteSlaveThresholdIndex"),
)
if mibBuilder.loadTexts:
    f3PtpRemoteSlaveThresholdEntry.setStatus("current")


class _F3PtpRemoteSlaveThresholdIndex_Type(Integer32):
    """Custom type f3PtpRemoteSlaveThresholdIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_F3PtpRemoteSlaveThresholdIndex_Type.__name__ = "Integer32"
_F3PtpRemoteSlaveThresholdIndex_Object = MibTableColumn
f3PtpRemoteSlaveThresholdIndex = _F3PtpRemoteSlaveThresholdIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 18, 1, 1),
    _F3PtpRemoteSlaveThresholdIndex_Type()
)
f3PtpRemoteSlaveThresholdIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    f3PtpRemoteSlaveThresholdIndex.setStatus("current")
_F3PtpRemoteSlaveThresholdInterval_Type = CmPmIntervalType
_F3PtpRemoteSlaveThresholdInterval_Object = MibTableColumn
f3PtpRemoteSlaveThresholdInterval = _F3PtpRemoteSlaveThresholdInterval_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 18, 1, 2),
    _F3PtpRemoteSlaveThresholdInterval_Type()
)
f3PtpRemoteSlaveThresholdInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpRemoteSlaveThresholdInterval.setStatus("current")
_F3PtpRemoteSlaveThresholdVariable_Type = VariablePointer
_F3PtpRemoteSlaveThresholdVariable_Object = MibTableColumn
f3PtpRemoteSlaveThresholdVariable = _F3PtpRemoteSlaveThresholdVariable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 18, 1, 3),
    _F3PtpRemoteSlaveThresholdVariable_Type()
)
f3PtpRemoteSlaveThresholdVariable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpRemoteSlaveThresholdVariable.setStatus("current")
_F3PtpRemoteSlaveThresholdValueLo_Type = Unsigned32
_F3PtpRemoteSlaveThresholdValueLo_Object = MibTableColumn
f3PtpRemoteSlaveThresholdValueLo = _F3PtpRemoteSlaveThresholdValueLo_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 18, 1, 4),
    _F3PtpRemoteSlaveThresholdValueLo_Type()
)
f3PtpRemoteSlaveThresholdValueLo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3PtpRemoteSlaveThresholdValueLo.setStatus("current")
_F3PtpRemoteSlaveThresholdValueHi_Type = Unsigned32
_F3PtpRemoteSlaveThresholdValueHi_Object = MibTableColumn
f3PtpRemoteSlaveThresholdValueHi = _F3PtpRemoteSlaveThresholdValueHi_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 18, 1, 5),
    _F3PtpRemoteSlaveThresholdValueHi_Type()
)
f3PtpRemoteSlaveThresholdValueHi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3PtpRemoteSlaveThresholdValueHi.setStatus("current")
_F3PtpRemoteSlaveThresholdMonValue_Type = PerfCounter64
_F3PtpRemoteSlaveThresholdMonValue_Object = MibTableColumn
f3PtpRemoteSlaveThresholdMonValue = _F3PtpRemoteSlaveThresholdMonValue_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 18, 1, 6),
    _F3PtpRemoteSlaveThresholdMonValue_Type()
)
f3PtpRemoteSlaveThresholdMonValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpRemoteSlaveThresholdMonValue.setStatus("current")
_F3PtpTrafficPortFlowPointStatsTable_Object = MibTable
f3PtpTrafficPortFlowPointStatsTable = _F3PtpTrafficPortFlowPointStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 19)
)
if mibBuilder.loadTexts:
    f3PtpTrafficPortFlowPointStatsTable.setStatus("current")
_F3PtpTrafficPortFlowPointStatsEntry_Object = MibTableRow
f3PtpTrafficPortFlowPointStatsEntry = _F3PtpTrafficPortFlowPointStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 19, 1)
)
f3PtpTrafficPortFlowPointStatsEntry.setIndexNames(
    (0, "CM-ENTITY-MIB", "neIndex"),
    (0, "CM-ENTITY-MIB", "shelfIndex"),
    (0, "CM-ENTITY-MIB", "slotIndex"),
    (0, "CM-FACILITY-MIB", "cmEthernetTrafficPortIndex"),
    (0, "F3-PTP-MIB", "f3PtpTrafficPortFlowPointIndex"),
    (0, "F3-PTP-MIB", "f3PtpTrafficPortFlowPointStatsIndex"),
)
if mibBuilder.loadTexts:
    f3PtpTrafficPortFlowPointStatsEntry.setStatus("current")


class _F3PtpTrafficPortFlowPointStatsIndex_Type(Integer32):
    """Custom type f3PtpTrafficPortFlowPointStatsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_F3PtpTrafficPortFlowPointStatsIndex_Type.__name__ = "Integer32"
_F3PtpTrafficPortFlowPointStatsIndex_Object = MibTableColumn
f3PtpTrafficPortFlowPointStatsIndex = _F3PtpTrafficPortFlowPointStatsIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 19, 1, 1),
    _F3PtpTrafficPortFlowPointStatsIndex_Type()
)
f3PtpTrafficPortFlowPointStatsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    f3PtpTrafficPortFlowPointStatsIndex.setStatus("current")
_F3PtpTrafficPortFlowPointStatsIntervalType_Type = CmPmIntervalType
_F3PtpTrafficPortFlowPointStatsIntervalType_Object = MibTableColumn
f3PtpTrafficPortFlowPointStatsIntervalType = _F3PtpTrafficPortFlowPointStatsIntervalType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 19, 1, 2),
    _F3PtpTrafficPortFlowPointStatsIntervalType_Type()
)
f3PtpTrafficPortFlowPointStatsIntervalType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpTrafficPortFlowPointStatsIntervalType.setStatus("current")
_F3PtpTrafficPortFlowPointStatsValid_Type = TruthValue
_F3PtpTrafficPortFlowPointStatsValid_Object = MibTableColumn
f3PtpTrafficPortFlowPointStatsValid = _F3PtpTrafficPortFlowPointStatsValid_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 19, 1, 3),
    _F3PtpTrafficPortFlowPointStatsValid_Type()
)
f3PtpTrafficPortFlowPointStatsValid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpTrafficPortFlowPointStatsValid.setStatus("current")
_F3PtpTrafficPortFlowPointStatsAction_Type = CmPmBinAction
_F3PtpTrafficPortFlowPointStatsAction_Object = MibTableColumn
f3PtpTrafficPortFlowPointStatsAction = _F3PtpTrafficPortFlowPointStatsAction_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 19, 1, 4),
    _F3PtpTrafficPortFlowPointStatsAction_Type()
)
f3PtpTrafficPortFlowPointStatsAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3PtpTrafficPortFlowPointStatsAction.setStatus("current")
_F3PtpTrafficPortFlowPointStatsAnnouncesRx_Type = PerfCounter64
_F3PtpTrafficPortFlowPointStatsAnnouncesRx_Object = MibTableColumn
f3PtpTrafficPortFlowPointStatsAnnouncesRx = _F3PtpTrafficPortFlowPointStatsAnnouncesRx_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 19, 1, 5),
    _F3PtpTrafficPortFlowPointStatsAnnouncesRx_Type()
)
f3PtpTrafficPortFlowPointStatsAnnouncesRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpTrafficPortFlowPointStatsAnnouncesRx.setStatus("current")
_F3PtpTrafficPortFlowPointStatsAnnouncesTx_Type = PerfCounter64
_F3PtpTrafficPortFlowPointStatsAnnouncesTx_Object = MibTableColumn
f3PtpTrafficPortFlowPointStatsAnnouncesTx = _F3PtpTrafficPortFlowPointStatsAnnouncesTx_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 19, 1, 6),
    _F3PtpTrafficPortFlowPointStatsAnnouncesTx_Type()
)
f3PtpTrafficPortFlowPointStatsAnnouncesTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpTrafficPortFlowPointStatsAnnouncesTx.setStatus("current")
_F3PtpTrafficPortFlowPointStatsSyncsRx_Type = PerfCounter64
_F3PtpTrafficPortFlowPointStatsSyncsRx_Object = MibTableColumn
f3PtpTrafficPortFlowPointStatsSyncsRx = _F3PtpTrafficPortFlowPointStatsSyncsRx_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 19, 1, 7),
    _F3PtpTrafficPortFlowPointStatsSyncsRx_Type()
)
f3PtpTrafficPortFlowPointStatsSyncsRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpTrafficPortFlowPointStatsSyncsRx.setStatus("current")
_F3PtpTrafficPortFlowPointStatsSyncsTx_Type = PerfCounter64
_F3PtpTrafficPortFlowPointStatsSyncsTx_Object = MibTableColumn
f3PtpTrafficPortFlowPointStatsSyncsTx = _F3PtpTrafficPortFlowPointStatsSyncsTx_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 19, 1, 8),
    _F3PtpTrafficPortFlowPointStatsSyncsTx_Type()
)
f3PtpTrafficPortFlowPointStatsSyncsTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpTrafficPortFlowPointStatsSyncsTx.setStatus("current")
_F3PtpTrafficPortFlowPointStatsFollowupsRx_Type = PerfCounter64
_F3PtpTrafficPortFlowPointStatsFollowupsRx_Object = MibTableColumn
f3PtpTrafficPortFlowPointStatsFollowupsRx = _F3PtpTrafficPortFlowPointStatsFollowupsRx_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 19, 1, 9),
    _F3PtpTrafficPortFlowPointStatsFollowupsRx_Type()
)
f3PtpTrafficPortFlowPointStatsFollowupsRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpTrafficPortFlowPointStatsFollowupsRx.setStatus("current")
_F3PtpTrafficPortFlowPointStatsFollowupsTx_Type = PerfCounter64
_F3PtpTrafficPortFlowPointStatsFollowupsTx_Object = MibTableColumn
f3PtpTrafficPortFlowPointStatsFollowupsTx = _F3PtpTrafficPortFlowPointStatsFollowupsTx_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 19, 1, 10),
    _F3PtpTrafficPortFlowPointStatsFollowupsTx_Type()
)
f3PtpTrafficPortFlowPointStatsFollowupsTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpTrafficPortFlowPointStatsFollowupsTx.setStatus("current")
_F3PtpTrafficPortFlowPointStatsDelayReqsRx_Type = PerfCounter64
_F3PtpTrafficPortFlowPointStatsDelayReqsRx_Object = MibTableColumn
f3PtpTrafficPortFlowPointStatsDelayReqsRx = _F3PtpTrafficPortFlowPointStatsDelayReqsRx_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 19, 1, 11),
    _F3PtpTrafficPortFlowPointStatsDelayReqsRx_Type()
)
f3PtpTrafficPortFlowPointStatsDelayReqsRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpTrafficPortFlowPointStatsDelayReqsRx.setStatus("current")
_F3PtpTrafficPortFlowPointStatsDelayReqsTx_Type = PerfCounter64
_F3PtpTrafficPortFlowPointStatsDelayReqsTx_Object = MibTableColumn
f3PtpTrafficPortFlowPointStatsDelayReqsTx = _F3PtpTrafficPortFlowPointStatsDelayReqsTx_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 19, 1, 12),
    _F3PtpTrafficPortFlowPointStatsDelayReqsTx_Type()
)
f3PtpTrafficPortFlowPointStatsDelayReqsTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpTrafficPortFlowPointStatsDelayReqsTx.setStatus("current")
_F3PtpTrafficPortFlowPointStatsDelayRspsRx_Type = PerfCounter64
_F3PtpTrafficPortFlowPointStatsDelayRspsRx_Object = MibTableColumn
f3PtpTrafficPortFlowPointStatsDelayRspsRx = _F3PtpTrafficPortFlowPointStatsDelayRspsRx_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 19, 1, 13),
    _F3PtpTrafficPortFlowPointStatsDelayRspsRx_Type()
)
f3PtpTrafficPortFlowPointStatsDelayRspsRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpTrafficPortFlowPointStatsDelayRspsRx.setStatus("current")
_F3PtpTrafficPortFlowPointStatsDelayRspsTx_Type = PerfCounter64
_F3PtpTrafficPortFlowPointStatsDelayRspsTx_Object = MibTableColumn
f3PtpTrafficPortFlowPointStatsDelayRspsTx = _F3PtpTrafficPortFlowPointStatsDelayRspsTx_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 19, 1, 14),
    _F3PtpTrafficPortFlowPointStatsDelayRspsTx_Type()
)
f3PtpTrafficPortFlowPointStatsDelayRspsTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpTrafficPortFlowPointStatsDelayRspsTx.setStatus("current")
_F3PtpTrafficPortFlowPointStatsPDelayReqsRx_Type = PerfCounter64
_F3PtpTrafficPortFlowPointStatsPDelayReqsRx_Object = MibTableColumn
f3PtpTrafficPortFlowPointStatsPDelayReqsRx = _F3PtpTrafficPortFlowPointStatsPDelayReqsRx_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 19, 1, 15),
    _F3PtpTrafficPortFlowPointStatsPDelayReqsRx_Type()
)
f3PtpTrafficPortFlowPointStatsPDelayReqsRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpTrafficPortFlowPointStatsPDelayReqsRx.setStatus("current")
_F3PtpTrafficPortFlowPointStatsPDelayReqsTx_Type = PerfCounter64
_F3PtpTrafficPortFlowPointStatsPDelayReqsTx_Object = MibTableColumn
f3PtpTrafficPortFlowPointStatsPDelayReqsTx = _F3PtpTrafficPortFlowPointStatsPDelayReqsTx_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 19, 1, 16),
    _F3PtpTrafficPortFlowPointStatsPDelayReqsTx_Type()
)
f3PtpTrafficPortFlowPointStatsPDelayReqsTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpTrafficPortFlowPointStatsPDelayReqsTx.setStatus("current")
_F3PtpTrafficPortFlowPointStatsPDelayRspsRx_Type = PerfCounter64
_F3PtpTrafficPortFlowPointStatsPDelayRspsRx_Object = MibTableColumn
f3PtpTrafficPortFlowPointStatsPDelayRspsRx = _F3PtpTrafficPortFlowPointStatsPDelayRspsRx_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 19, 1, 17),
    _F3PtpTrafficPortFlowPointStatsPDelayRspsRx_Type()
)
f3PtpTrafficPortFlowPointStatsPDelayRspsRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpTrafficPortFlowPointStatsPDelayRspsRx.setStatus("current")
_F3PtpTrafficPortFlowPointStatsPDelayRspsTx_Type = PerfCounter64
_F3PtpTrafficPortFlowPointStatsPDelayRspsTx_Object = MibTableColumn
f3PtpTrafficPortFlowPointStatsPDelayRspsTx = _F3PtpTrafficPortFlowPointStatsPDelayRspsTx_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 19, 1, 18),
    _F3PtpTrafficPortFlowPointStatsPDelayRspsTx_Type()
)
f3PtpTrafficPortFlowPointStatsPDelayRspsTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpTrafficPortFlowPointStatsPDelayRspsTx.setStatus("current")
_F3PtpTrafficPortFlowPointStatsPDelayRspFollowupsRx_Type = PerfCounter64
_F3PtpTrafficPortFlowPointStatsPDelayRspFollowupsRx_Object = MibTableColumn
f3PtpTrafficPortFlowPointStatsPDelayRspFollowupsRx = _F3PtpTrafficPortFlowPointStatsPDelayRspFollowupsRx_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 19, 1, 19),
    _F3PtpTrafficPortFlowPointStatsPDelayRspFollowupsRx_Type()
)
f3PtpTrafficPortFlowPointStatsPDelayRspFollowupsRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpTrafficPortFlowPointStatsPDelayRspFollowupsRx.setStatus("current")
_F3PtpTrafficPortFlowPointStatsPDelayRspFollowupsTx_Type = PerfCounter64
_F3PtpTrafficPortFlowPointStatsPDelayRspFollowupsTx_Object = MibTableColumn
f3PtpTrafficPortFlowPointStatsPDelayRspFollowupsTx = _F3PtpTrafficPortFlowPointStatsPDelayRspFollowupsTx_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 19, 1, 20),
    _F3PtpTrafficPortFlowPointStatsPDelayRspFollowupsTx_Type()
)
f3PtpTrafficPortFlowPointStatsPDelayRspFollowupsTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpTrafficPortFlowPointStatsPDelayRspFollowupsTx.setStatus("current")
_F3PtpTrafficPortFlowPointStatsSignalingRx_Type = PerfCounter64
_F3PtpTrafficPortFlowPointStatsSignalingRx_Object = MibTableColumn
f3PtpTrafficPortFlowPointStatsSignalingRx = _F3PtpTrafficPortFlowPointStatsSignalingRx_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 19, 1, 21),
    _F3PtpTrafficPortFlowPointStatsSignalingRx_Type()
)
f3PtpTrafficPortFlowPointStatsSignalingRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpTrafficPortFlowPointStatsSignalingRx.setStatus("current")
_F3PtpTrafficPortFlowPointStatsSignalingTx_Type = PerfCounter64
_F3PtpTrafficPortFlowPointStatsSignalingTx_Object = MibTableColumn
f3PtpTrafficPortFlowPointStatsSignalingTx = _F3PtpTrafficPortFlowPointStatsSignalingTx_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 19, 1, 22),
    _F3PtpTrafficPortFlowPointStatsSignalingTx_Type()
)
f3PtpTrafficPortFlowPointStatsSignalingTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpTrafficPortFlowPointStatsSignalingTx.setStatus("current")
_F3PtpTrafficPortFlowPointStatsMgmtFramesRx_Type = PerfCounter64
_F3PtpTrafficPortFlowPointStatsMgmtFramesRx_Object = MibTableColumn
f3PtpTrafficPortFlowPointStatsMgmtFramesRx = _F3PtpTrafficPortFlowPointStatsMgmtFramesRx_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 19, 1, 23),
    _F3PtpTrafficPortFlowPointStatsMgmtFramesRx_Type()
)
f3PtpTrafficPortFlowPointStatsMgmtFramesRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpTrafficPortFlowPointStatsMgmtFramesRx.setStatus("current")
_F3PtpTrafficPortFlowPointStatsMgmtFramesTx_Type = PerfCounter64
_F3PtpTrafficPortFlowPointStatsMgmtFramesTx_Object = MibTableColumn
f3PtpTrafficPortFlowPointStatsMgmtFramesTx = _F3PtpTrafficPortFlowPointStatsMgmtFramesTx_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 19, 1, 24),
    _F3PtpTrafficPortFlowPointStatsMgmtFramesTx_Type()
)
f3PtpTrafficPortFlowPointStatsMgmtFramesTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpTrafficPortFlowPointStatsMgmtFramesTx.setStatus("current")
_F3PtpTrafficPortFlowPointStatsPtpUnknownsRx_Type = PerfCounter64
_F3PtpTrafficPortFlowPointStatsPtpUnknownsRx_Object = MibTableColumn
f3PtpTrafficPortFlowPointStatsPtpUnknownsRx = _F3PtpTrafficPortFlowPointStatsPtpUnknownsRx_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 19, 1, 25),
    _F3PtpTrafficPortFlowPointStatsPtpUnknownsRx_Type()
)
f3PtpTrafficPortFlowPointStatsPtpUnknownsRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpTrafficPortFlowPointStatsPtpUnknownsRx.setStatus("current")
_F3PtpTrafficPortFlowPointStatsPtpUnknownsTx_Type = PerfCounter64
_F3PtpTrafficPortFlowPointStatsPtpUnknownsTx_Object = MibTableColumn
f3PtpTrafficPortFlowPointStatsPtpUnknownsTx = _F3PtpTrafficPortFlowPointStatsPtpUnknownsTx_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 19, 1, 26),
    _F3PtpTrafficPortFlowPointStatsPtpUnknownsTx_Type()
)
f3PtpTrafficPortFlowPointStatsPtpUnknownsTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpTrafficPortFlowPointStatsPtpUnknownsTx.setStatus("current")
_F3PtpTrafficPortFlowPointStatsMinSyncResTime_Type = Unsigned32
_F3PtpTrafficPortFlowPointStatsMinSyncResTime_Object = MibTableColumn
f3PtpTrafficPortFlowPointStatsMinSyncResTime = _F3PtpTrafficPortFlowPointStatsMinSyncResTime_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 19, 1, 27),
    _F3PtpTrafficPortFlowPointStatsMinSyncResTime_Type()
)
f3PtpTrafficPortFlowPointStatsMinSyncResTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpTrafficPortFlowPointStatsMinSyncResTime.setStatus("current")
_F3PtpTrafficPortFlowPointStatsMaxSyncResTime_Type = Unsigned32
_F3PtpTrafficPortFlowPointStatsMaxSyncResTime_Object = MibTableColumn
f3PtpTrafficPortFlowPointStatsMaxSyncResTime = _F3PtpTrafficPortFlowPointStatsMaxSyncResTime_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 19, 1, 28),
    _F3PtpTrafficPortFlowPointStatsMaxSyncResTime_Type()
)
f3PtpTrafficPortFlowPointStatsMaxSyncResTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpTrafficPortFlowPointStatsMaxSyncResTime.setStatus("current")
_F3PtpTrafficPortFlowPointStatsAvgSyncResTime_Type = Unsigned32
_F3PtpTrafficPortFlowPointStatsAvgSyncResTime_Object = MibTableColumn
f3PtpTrafficPortFlowPointStatsAvgSyncResTime = _F3PtpTrafficPortFlowPointStatsAvgSyncResTime_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 19, 1, 29),
    _F3PtpTrafficPortFlowPointStatsAvgSyncResTime_Type()
)
f3PtpTrafficPortFlowPointStatsAvgSyncResTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpTrafficPortFlowPointStatsAvgSyncResTime.setStatus("current")
_F3PtpTrafficPortFlowPointStatsMinDelayReqResTime_Type = Unsigned32
_F3PtpTrafficPortFlowPointStatsMinDelayReqResTime_Object = MibTableColumn
f3PtpTrafficPortFlowPointStatsMinDelayReqResTime = _F3PtpTrafficPortFlowPointStatsMinDelayReqResTime_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 19, 1, 30),
    _F3PtpTrafficPortFlowPointStatsMinDelayReqResTime_Type()
)
f3PtpTrafficPortFlowPointStatsMinDelayReqResTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpTrafficPortFlowPointStatsMinDelayReqResTime.setStatus("current")
_F3PtpTrafficPortFlowPointStatsMaxDelayReqResTime_Type = Unsigned32
_F3PtpTrafficPortFlowPointStatsMaxDelayReqResTime_Object = MibTableColumn
f3PtpTrafficPortFlowPointStatsMaxDelayReqResTime = _F3PtpTrafficPortFlowPointStatsMaxDelayReqResTime_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 19, 1, 31),
    _F3PtpTrafficPortFlowPointStatsMaxDelayReqResTime_Type()
)
f3PtpTrafficPortFlowPointStatsMaxDelayReqResTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpTrafficPortFlowPointStatsMaxDelayReqResTime.setStatus("current")
_F3PtpTrafficPortFlowPointStatsAvgDelayReqResTime_Type = Unsigned32
_F3PtpTrafficPortFlowPointStatsAvgDelayReqResTime_Object = MibTableColumn
f3PtpTrafficPortFlowPointStatsAvgDelayReqResTime = _F3PtpTrafficPortFlowPointStatsAvgDelayReqResTime_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 19, 1, 32),
    _F3PtpTrafficPortFlowPointStatsAvgDelayReqResTime_Type()
)
f3PtpTrafficPortFlowPointStatsAvgDelayReqResTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpTrafficPortFlowPointStatsAvgDelayReqResTime.setStatus("current")
_F3PtpTrafficPortFlowPointStatsMinPDelayReqResTime_Type = Unsigned32
_F3PtpTrafficPortFlowPointStatsMinPDelayReqResTime_Object = MibTableColumn
f3PtpTrafficPortFlowPointStatsMinPDelayReqResTime = _F3PtpTrafficPortFlowPointStatsMinPDelayReqResTime_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 19, 1, 33),
    _F3PtpTrafficPortFlowPointStatsMinPDelayReqResTime_Type()
)
f3PtpTrafficPortFlowPointStatsMinPDelayReqResTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpTrafficPortFlowPointStatsMinPDelayReqResTime.setStatus("current")
_F3PtpTrafficPortFlowPointStatsMaxPDelayReqResTime_Type = Unsigned32
_F3PtpTrafficPortFlowPointStatsMaxPDelayReqResTime_Object = MibTableColumn
f3PtpTrafficPortFlowPointStatsMaxPDelayReqResTime = _F3PtpTrafficPortFlowPointStatsMaxPDelayReqResTime_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 19, 1, 34),
    _F3PtpTrafficPortFlowPointStatsMaxPDelayReqResTime_Type()
)
f3PtpTrafficPortFlowPointStatsMaxPDelayReqResTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpTrafficPortFlowPointStatsMaxPDelayReqResTime.setStatus("current")
_F3PtpTrafficPortFlowPointStatsAvgPDelayReqResTime_Type = Unsigned32
_F3PtpTrafficPortFlowPointStatsAvgPDelayReqResTime_Object = MibTableColumn
f3PtpTrafficPortFlowPointStatsAvgPDelayReqResTime = _F3PtpTrafficPortFlowPointStatsAvgPDelayReqResTime_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 19, 1, 35),
    _F3PtpTrafficPortFlowPointStatsAvgPDelayReqResTime_Type()
)
f3PtpTrafficPortFlowPointStatsAvgPDelayReqResTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpTrafficPortFlowPointStatsAvgPDelayReqResTime.setStatus("current")
_F3PtpTrafficPortFlowPointStatsMinPDelayRspResTime_Type = Unsigned32
_F3PtpTrafficPortFlowPointStatsMinPDelayRspResTime_Object = MibTableColumn
f3PtpTrafficPortFlowPointStatsMinPDelayRspResTime = _F3PtpTrafficPortFlowPointStatsMinPDelayRspResTime_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 19, 1, 36),
    _F3PtpTrafficPortFlowPointStatsMinPDelayRspResTime_Type()
)
f3PtpTrafficPortFlowPointStatsMinPDelayRspResTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpTrafficPortFlowPointStatsMinPDelayRspResTime.setStatus("current")
_F3PtpTrafficPortFlowPointStatsMaxPDelayRspResTime_Type = Unsigned32
_F3PtpTrafficPortFlowPointStatsMaxPDelayRspResTime_Object = MibTableColumn
f3PtpTrafficPortFlowPointStatsMaxPDelayRspResTime = _F3PtpTrafficPortFlowPointStatsMaxPDelayRspResTime_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 19, 1, 37),
    _F3PtpTrafficPortFlowPointStatsMaxPDelayRspResTime_Type()
)
f3PtpTrafficPortFlowPointStatsMaxPDelayRspResTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpTrafficPortFlowPointStatsMaxPDelayRspResTime.setStatus("current")
_F3PtpTrafficPortFlowPointStatsAvgPDelayRspResTime_Type = Unsigned32
_F3PtpTrafficPortFlowPointStatsAvgPDelayRspResTime_Object = MibTableColumn
f3PtpTrafficPortFlowPointStatsAvgPDelayRspResTime = _F3PtpTrafficPortFlowPointStatsAvgPDelayRspResTime_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 19, 1, 38),
    _F3PtpTrafficPortFlowPointStatsAvgPDelayRspResTime_Type()
)
f3PtpTrafficPortFlowPointStatsAvgPDelayRspResTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpTrafficPortFlowPointStatsAvgPDelayRspResTime.setStatus("current")
_F3PtpTrafficPortFlowPointStatsDestMciNoMatchDiscards_Type = PerfCounter64
_F3PtpTrafficPortFlowPointStatsDestMciNoMatchDiscards_Object = MibTableColumn
f3PtpTrafficPortFlowPointStatsDestMciNoMatchDiscards = _F3PtpTrafficPortFlowPointStatsDestMciNoMatchDiscards_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 19, 1, 39),
    _F3PtpTrafficPortFlowPointStatsDestMciNoMatchDiscards_Type()
)
f3PtpTrafficPortFlowPointStatsDestMciNoMatchDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpTrafficPortFlowPointStatsDestMciNoMatchDiscards.setStatus("current")
_F3PtpTrafficPortFlowPointStatsTagNoMatchDiscards_Type = PerfCounter64
_F3PtpTrafficPortFlowPointStatsTagNoMatchDiscards_Object = MibTableColumn
f3PtpTrafficPortFlowPointStatsTagNoMatchDiscards = _F3PtpTrafficPortFlowPointStatsTagNoMatchDiscards_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 19, 1, 40),
    _F3PtpTrafficPortFlowPointStatsTagNoMatchDiscards_Type()
)
f3PtpTrafficPortFlowPointStatsTagNoMatchDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpTrafficPortFlowPointStatsTagNoMatchDiscards.setStatus("current")
_F3PtpTrafficPortFlowPointHistoryTable_Object = MibTable
f3PtpTrafficPortFlowPointHistoryTable = _F3PtpTrafficPortFlowPointHistoryTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 20)
)
if mibBuilder.loadTexts:
    f3PtpTrafficPortFlowPointHistoryTable.setStatus("current")
_F3PtpTrafficPortFlowPointHistoryEntry_Object = MibTableRow
f3PtpTrafficPortFlowPointHistoryEntry = _F3PtpTrafficPortFlowPointHistoryEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 20, 1)
)
f3PtpTrafficPortFlowPointHistoryEntry.setIndexNames(
    (0, "CM-ENTITY-MIB", "neIndex"),
    (0, "CM-ENTITY-MIB", "shelfIndex"),
    (0, "CM-ENTITY-MIB", "slotIndex"),
    (0, "CM-FACILITY-MIB", "cmEthernetTrafficPortIndex"),
    (0, "F3-PTP-MIB", "f3PtpTrafficPortFlowPointIndex"),
    (0, "F3-PTP-MIB", "f3PtpTrafficPortFlowPointStatsIndex"),
    (0, "F3-PTP-MIB", "f3PtpTrafficPortFlowPointHistoryIndex"),
)
if mibBuilder.loadTexts:
    f3PtpTrafficPortFlowPointHistoryEntry.setStatus("current")


class _F3PtpTrafficPortFlowPointHistoryIndex_Type(Integer32):
    """Custom type f3PtpTrafficPortFlowPointHistoryIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_F3PtpTrafficPortFlowPointHistoryIndex_Type.__name__ = "Integer32"
_F3PtpTrafficPortFlowPointHistoryIndex_Object = MibTableColumn
f3PtpTrafficPortFlowPointHistoryIndex = _F3PtpTrafficPortFlowPointHistoryIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 20, 1, 1),
    _F3PtpTrafficPortFlowPointHistoryIndex_Type()
)
f3PtpTrafficPortFlowPointHistoryIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    f3PtpTrafficPortFlowPointHistoryIndex.setStatus("current")
_F3PtpTrafficPortFlowPointHistoryTime_Type = DateAndTime
_F3PtpTrafficPortFlowPointHistoryTime_Object = MibTableColumn
f3PtpTrafficPortFlowPointHistoryTime = _F3PtpTrafficPortFlowPointHistoryTime_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 20, 1, 2),
    _F3PtpTrafficPortFlowPointHistoryTime_Type()
)
f3PtpTrafficPortFlowPointHistoryTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpTrafficPortFlowPointHistoryTime.setStatus("current")
_F3PtpTrafficPortFlowPointHistoryValid_Type = TruthValue
_F3PtpTrafficPortFlowPointHistoryValid_Object = MibTableColumn
f3PtpTrafficPortFlowPointHistoryValid = _F3PtpTrafficPortFlowPointHistoryValid_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 20, 1, 3),
    _F3PtpTrafficPortFlowPointHistoryValid_Type()
)
f3PtpTrafficPortFlowPointHistoryValid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpTrafficPortFlowPointHistoryValid.setStatus("current")
_F3PtpTrafficPortFlowPointHistoryAction_Type = CmPmBinAction
_F3PtpTrafficPortFlowPointHistoryAction_Object = MibTableColumn
f3PtpTrafficPortFlowPointHistoryAction = _F3PtpTrafficPortFlowPointHistoryAction_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 20, 1, 4),
    _F3PtpTrafficPortFlowPointHistoryAction_Type()
)
f3PtpTrafficPortFlowPointHistoryAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3PtpTrafficPortFlowPointHistoryAction.setStatus("current")
_F3PtpTrafficPortFlowPointHistoryAnnouncesRx_Type = PerfCounter64
_F3PtpTrafficPortFlowPointHistoryAnnouncesRx_Object = MibTableColumn
f3PtpTrafficPortFlowPointHistoryAnnouncesRx = _F3PtpTrafficPortFlowPointHistoryAnnouncesRx_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 20, 1, 5),
    _F3PtpTrafficPortFlowPointHistoryAnnouncesRx_Type()
)
f3PtpTrafficPortFlowPointHistoryAnnouncesRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpTrafficPortFlowPointHistoryAnnouncesRx.setStatus("current")
_F3PtpTrafficPortFlowPointHistoryAnnouncesTx_Type = PerfCounter64
_F3PtpTrafficPortFlowPointHistoryAnnouncesTx_Object = MibTableColumn
f3PtpTrafficPortFlowPointHistoryAnnouncesTx = _F3PtpTrafficPortFlowPointHistoryAnnouncesTx_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 20, 1, 6),
    _F3PtpTrafficPortFlowPointHistoryAnnouncesTx_Type()
)
f3PtpTrafficPortFlowPointHistoryAnnouncesTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpTrafficPortFlowPointHistoryAnnouncesTx.setStatus("current")
_F3PtpTrafficPortFlowPointHistorySyncsRx_Type = PerfCounter64
_F3PtpTrafficPortFlowPointHistorySyncsRx_Object = MibTableColumn
f3PtpTrafficPortFlowPointHistorySyncsRx = _F3PtpTrafficPortFlowPointHistorySyncsRx_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 20, 1, 7),
    _F3PtpTrafficPortFlowPointHistorySyncsRx_Type()
)
f3PtpTrafficPortFlowPointHistorySyncsRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpTrafficPortFlowPointHistorySyncsRx.setStatus("current")
_F3PtpTrafficPortFlowPointHistorySyncsTx_Type = PerfCounter64
_F3PtpTrafficPortFlowPointHistorySyncsTx_Object = MibTableColumn
f3PtpTrafficPortFlowPointHistorySyncsTx = _F3PtpTrafficPortFlowPointHistorySyncsTx_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 20, 1, 8),
    _F3PtpTrafficPortFlowPointHistorySyncsTx_Type()
)
f3PtpTrafficPortFlowPointHistorySyncsTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpTrafficPortFlowPointHistorySyncsTx.setStatus("current")
_F3PtpTrafficPortFlowPointHistoryFollowupsRx_Type = PerfCounter64
_F3PtpTrafficPortFlowPointHistoryFollowupsRx_Object = MibTableColumn
f3PtpTrafficPortFlowPointHistoryFollowupsRx = _F3PtpTrafficPortFlowPointHistoryFollowupsRx_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 20, 1, 9),
    _F3PtpTrafficPortFlowPointHistoryFollowupsRx_Type()
)
f3PtpTrafficPortFlowPointHistoryFollowupsRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpTrafficPortFlowPointHistoryFollowupsRx.setStatus("current")
_F3PtpTrafficPortFlowPointHistoryFollowupsTx_Type = PerfCounter64
_F3PtpTrafficPortFlowPointHistoryFollowupsTx_Object = MibTableColumn
f3PtpTrafficPortFlowPointHistoryFollowupsTx = _F3PtpTrafficPortFlowPointHistoryFollowupsTx_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 20, 1, 10),
    _F3PtpTrafficPortFlowPointHistoryFollowupsTx_Type()
)
f3PtpTrafficPortFlowPointHistoryFollowupsTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpTrafficPortFlowPointHistoryFollowupsTx.setStatus("current")
_F3PtpTrafficPortFlowPointHistoryDelayReqsRx_Type = PerfCounter64
_F3PtpTrafficPortFlowPointHistoryDelayReqsRx_Object = MibTableColumn
f3PtpTrafficPortFlowPointHistoryDelayReqsRx = _F3PtpTrafficPortFlowPointHistoryDelayReqsRx_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 20, 1, 11),
    _F3PtpTrafficPortFlowPointHistoryDelayReqsRx_Type()
)
f3PtpTrafficPortFlowPointHistoryDelayReqsRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpTrafficPortFlowPointHistoryDelayReqsRx.setStatus("current")
_F3PtpTrafficPortFlowPointHistoryDelayReqsTx_Type = PerfCounter64
_F3PtpTrafficPortFlowPointHistoryDelayReqsTx_Object = MibTableColumn
f3PtpTrafficPortFlowPointHistoryDelayReqsTx = _F3PtpTrafficPortFlowPointHistoryDelayReqsTx_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 20, 1, 12),
    _F3PtpTrafficPortFlowPointHistoryDelayReqsTx_Type()
)
f3PtpTrafficPortFlowPointHistoryDelayReqsTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpTrafficPortFlowPointHistoryDelayReqsTx.setStatus("current")
_F3PtpTrafficPortFlowPointHistoryDelayRspsRx_Type = PerfCounter64
_F3PtpTrafficPortFlowPointHistoryDelayRspsRx_Object = MibTableColumn
f3PtpTrafficPortFlowPointHistoryDelayRspsRx = _F3PtpTrafficPortFlowPointHistoryDelayRspsRx_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 20, 1, 13),
    _F3PtpTrafficPortFlowPointHistoryDelayRspsRx_Type()
)
f3PtpTrafficPortFlowPointHistoryDelayRspsRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpTrafficPortFlowPointHistoryDelayRspsRx.setStatus("current")
_F3PtpTrafficPortFlowPointHistoryDelayRspsTx_Type = PerfCounter64
_F3PtpTrafficPortFlowPointHistoryDelayRspsTx_Object = MibTableColumn
f3PtpTrafficPortFlowPointHistoryDelayRspsTx = _F3PtpTrafficPortFlowPointHistoryDelayRspsTx_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 20, 1, 14),
    _F3PtpTrafficPortFlowPointHistoryDelayRspsTx_Type()
)
f3PtpTrafficPortFlowPointHistoryDelayRspsTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpTrafficPortFlowPointHistoryDelayRspsTx.setStatus("current")
_F3PtpTrafficPortFlowPointHistoryPDelayReqsRx_Type = PerfCounter64
_F3PtpTrafficPortFlowPointHistoryPDelayReqsRx_Object = MibTableColumn
f3PtpTrafficPortFlowPointHistoryPDelayReqsRx = _F3PtpTrafficPortFlowPointHistoryPDelayReqsRx_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 20, 1, 15),
    _F3PtpTrafficPortFlowPointHistoryPDelayReqsRx_Type()
)
f3PtpTrafficPortFlowPointHistoryPDelayReqsRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpTrafficPortFlowPointHistoryPDelayReqsRx.setStatus("current")
_F3PtpTrafficPortFlowPointHistoryPDelayReqsTx_Type = PerfCounter64
_F3PtpTrafficPortFlowPointHistoryPDelayReqsTx_Object = MibTableColumn
f3PtpTrafficPortFlowPointHistoryPDelayReqsTx = _F3PtpTrafficPortFlowPointHistoryPDelayReqsTx_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 20, 1, 16),
    _F3PtpTrafficPortFlowPointHistoryPDelayReqsTx_Type()
)
f3PtpTrafficPortFlowPointHistoryPDelayReqsTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpTrafficPortFlowPointHistoryPDelayReqsTx.setStatus("current")
_F3PtpTrafficPortFlowPointHistoryPDelayRspsRx_Type = PerfCounter64
_F3PtpTrafficPortFlowPointHistoryPDelayRspsRx_Object = MibTableColumn
f3PtpTrafficPortFlowPointHistoryPDelayRspsRx = _F3PtpTrafficPortFlowPointHistoryPDelayRspsRx_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 20, 1, 17),
    _F3PtpTrafficPortFlowPointHistoryPDelayRspsRx_Type()
)
f3PtpTrafficPortFlowPointHistoryPDelayRspsRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpTrafficPortFlowPointHistoryPDelayRspsRx.setStatus("current")
_F3PtpTrafficPortFlowPointHistoryPDelayRspsTx_Type = PerfCounter64
_F3PtpTrafficPortFlowPointHistoryPDelayRspsTx_Object = MibTableColumn
f3PtpTrafficPortFlowPointHistoryPDelayRspsTx = _F3PtpTrafficPortFlowPointHistoryPDelayRspsTx_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 20, 1, 18),
    _F3PtpTrafficPortFlowPointHistoryPDelayRspsTx_Type()
)
f3PtpTrafficPortFlowPointHistoryPDelayRspsTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpTrafficPortFlowPointHistoryPDelayRspsTx.setStatus("current")
_F3PtpTrafficPortFlowPointHistoryPDelayRspFollowupsRx_Type = PerfCounter64
_F3PtpTrafficPortFlowPointHistoryPDelayRspFollowupsRx_Object = MibTableColumn
f3PtpTrafficPortFlowPointHistoryPDelayRspFollowupsRx = _F3PtpTrafficPortFlowPointHistoryPDelayRspFollowupsRx_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 20, 1, 19),
    _F3PtpTrafficPortFlowPointHistoryPDelayRspFollowupsRx_Type()
)
f3PtpTrafficPortFlowPointHistoryPDelayRspFollowupsRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpTrafficPortFlowPointHistoryPDelayRspFollowupsRx.setStatus("current")
_F3PtpTrafficPortFlowPointHistoryPDelayRspFollowupsTx_Type = PerfCounter64
_F3PtpTrafficPortFlowPointHistoryPDelayRspFollowupsTx_Object = MibTableColumn
f3PtpTrafficPortFlowPointHistoryPDelayRspFollowupsTx = _F3PtpTrafficPortFlowPointHistoryPDelayRspFollowupsTx_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 20, 1, 20),
    _F3PtpTrafficPortFlowPointHistoryPDelayRspFollowupsTx_Type()
)
f3PtpTrafficPortFlowPointHistoryPDelayRspFollowupsTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpTrafficPortFlowPointHistoryPDelayRspFollowupsTx.setStatus("current")
_F3PtpTrafficPortFlowPointHistorySignalingRx_Type = PerfCounter64
_F3PtpTrafficPortFlowPointHistorySignalingRx_Object = MibTableColumn
f3PtpTrafficPortFlowPointHistorySignalingRx = _F3PtpTrafficPortFlowPointHistorySignalingRx_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 20, 1, 21),
    _F3PtpTrafficPortFlowPointHistorySignalingRx_Type()
)
f3PtpTrafficPortFlowPointHistorySignalingRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpTrafficPortFlowPointHistorySignalingRx.setStatus("current")
_F3PtpTrafficPortFlowPointHistorySignalingTx_Type = PerfCounter64
_F3PtpTrafficPortFlowPointHistorySignalingTx_Object = MibTableColumn
f3PtpTrafficPortFlowPointHistorySignalingTx = _F3PtpTrafficPortFlowPointHistorySignalingTx_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 20, 1, 22),
    _F3PtpTrafficPortFlowPointHistorySignalingTx_Type()
)
f3PtpTrafficPortFlowPointHistorySignalingTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpTrafficPortFlowPointHistorySignalingTx.setStatus("current")
_F3PtpTrafficPortFlowPointHistoryMgmtFramesRx_Type = PerfCounter64
_F3PtpTrafficPortFlowPointHistoryMgmtFramesRx_Object = MibTableColumn
f3PtpTrafficPortFlowPointHistoryMgmtFramesRx = _F3PtpTrafficPortFlowPointHistoryMgmtFramesRx_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 20, 1, 23),
    _F3PtpTrafficPortFlowPointHistoryMgmtFramesRx_Type()
)
f3PtpTrafficPortFlowPointHistoryMgmtFramesRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpTrafficPortFlowPointHistoryMgmtFramesRx.setStatus("current")
_F3PtpTrafficPortFlowPointHistoryMgmtFramesTx_Type = PerfCounter64
_F3PtpTrafficPortFlowPointHistoryMgmtFramesTx_Object = MibTableColumn
f3PtpTrafficPortFlowPointHistoryMgmtFramesTx = _F3PtpTrafficPortFlowPointHistoryMgmtFramesTx_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 20, 1, 24),
    _F3PtpTrafficPortFlowPointHistoryMgmtFramesTx_Type()
)
f3PtpTrafficPortFlowPointHistoryMgmtFramesTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpTrafficPortFlowPointHistoryMgmtFramesTx.setStatus("current")
_F3PtpTrafficPortFlowPointHistoryPtpUnknownsRx_Type = PerfCounter64
_F3PtpTrafficPortFlowPointHistoryPtpUnknownsRx_Object = MibTableColumn
f3PtpTrafficPortFlowPointHistoryPtpUnknownsRx = _F3PtpTrafficPortFlowPointHistoryPtpUnknownsRx_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 20, 1, 25),
    _F3PtpTrafficPortFlowPointHistoryPtpUnknownsRx_Type()
)
f3PtpTrafficPortFlowPointHistoryPtpUnknownsRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpTrafficPortFlowPointHistoryPtpUnknownsRx.setStatus("current")
_F3PtpTrafficPortFlowPointHistoryPtpUnknownsTx_Type = PerfCounter64
_F3PtpTrafficPortFlowPointHistoryPtpUnknownsTx_Object = MibTableColumn
f3PtpTrafficPortFlowPointHistoryPtpUnknownsTx = _F3PtpTrafficPortFlowPointHistoryPtpUnknownsTx_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 20, 1, 26),
    _F3PtpTrafficPortFlowPointHistoryPtpUnknownsTx_Type()
)
f3PtpTrafficPortFlowPointHistoryPtpUnknownsTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpTrafficPortFlowPointHistoryPtpUnknownsTx.setStatus("current")
_F3PtpTrafficPortFlowPointHistoryMinSyncResTime_Type = Unsigned32
_F3PtpTrafficPortFlowPointHistoryMinSyncResTime_Object = MibTableColumn
f3PtpTrafficPortFlowPointHistoryMinSyncResTime = _F3PtpTrafficPortFlowPointHistoryMinSyncResTime_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 20, 1, 27),
    _F3PtpTrafficPortFlowPointHistoryMinSyncResTime_Type()
)
f3PtpTrafficPortFlowPointHistoryMinSyncResTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpTrafficPortFlowPointHistoryMinSyncResTime.setStatus("current")
_F3PtpTrafficPortFlowPointHistoryMaxSyncResTime_Type = Unsigned32
_F3PtpTrafficPortFlowPointHistoryMaxSyncResTime_Object = MibTableColumn
f3PtpTrafficPortFlowPointHistoryMaxSyncResTime = _F3PtpTrafficPortFlowPointHistoryMaxSyncResTime_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 20, 1, 28),
    _F3PtpTrafficPortFlowPointHistoryMaxSyncResTime_Type()
)
f3PtpTrafficPortFlowPointHistoryMaxSyncResTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpTrafficPortFlowPointHistoryMaxSyncResTime.setStatus("current")
_F3PtpTrafficPortFlowPointHistoryAvgSyncResTime_Type = Unsigned32
_F3PtpTrafficPortFlowPointHistoryAvgSyncResTime_Object = MibTableColumn
f3PtpTrafficPortFlowPointHistoryAvgSyncResTime = _F3PtpTrafficPortFlowPointHistoryAvgSyncResTime_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 20, 1, 29),
    _F3PtpTrafficPortFlowPointHistoryAvgSyncResTime_Type()
)
f3PtpTrafficPortFlowPointHistoryAvgSyncResTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpTrafficPortFlowPointHistoryAvgSyncResTime.setStatus("current")
_F3PtpTrafficPortFlowPointHistoryMinDelayReqResTime_Type = Unsigned32
_F3PtpTrafficPortFlowPointHistoryMinDelayReqResTime_Object = MibTableColumn
f3PtpTrafficPortFlowPointHistoryMinDelayReqResTime = _F3PtpTrafficPortFlowPointHistoryMinDelayReqResTime_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 20, 1, 30),
    _F3PtpTrafficPortFlowPointHistoryMinDelayReqResTime_Type()
)
f3PtpTrafficPortFlowPointHistoryMinDelayReqResTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpTrafficPortFlowPointHistoryMinDelayReqResTime.setStatus("current")
_F3PtpTrafficPortFlowPointHistoryMaxDelayReqResTime_Type = Unsigned32
_F3PtpTrafficPortFlowPointHistoryMaxDelayReqResTime_Object = MibTableColumn
f3PtpTrafficPortFlowPointHistoryMaxDelayReqResTime = _F3PtpTrafficPortFlowPointHistoryMaxDelayReqResTime_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 20, 1, 31),
    _F3PtpTrafficPortFlowPointHistoryMaxDelayReqResTime_Type()
)
f3PtpTrafficPortFlowPointHistoryMaxDelayReqResTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpTrafficPortFlowPointHistoryMaxDelayReqResTime.setStatus("current")
_F3PtpTrafficPortFlowPointHistoryAvgDelayReqResTime_Type = Unsigned32
_F3PtpTrafficPortFlowPointHistoryAvgDelayReqResTime_Object = MibTableColumn
f3PtpTrafficPortFlowPointHistoryAvgDelayReqResTime = _F3PtpTrafficPortFlowPointHistoryAvgDelayReqResTime_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 20, 1, 32),
    _F3PtpTrafficPortFlowPointHistoryAvgDelayReqResTime_Type()
)
f3PtpTrafficPortFlowPointHistoryAvgDelayReqResTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpTrafficPortFlowPointHistoryAvgDelayReqResTime.setStatus("current")
_F3PtpTrafficPortFlowPointHistoryMinPDelayReqResTime_Type = Unsigned32
_F3PtpTrafficPortFlowPointHistoryMinPDelayReqResTime_Object = MibTableColumn
f3PtpTrafficPortFlowPointHistoryMinPDelayReqResTime = _F3PtpTrafficPortFlowPointHistoryMinPDelayReqResTime_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 20, 1, 33),
    _F3PtpTrafficPortFlowPointHistoryMinPDelayReqResTime_Type()
)
f3PtpTrafficPortFlowPointHistoryMinPDelayReqResTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpTrafficPortFlowPointHistoryMinPDelayReqResTime.setStatus("current")
_F3PtpTrafficPortFlowPointHistoryMaxPDelayReqResTime_Type = Unsigned32
_F3PtpTrafficPortFlowPointHistoryMaxPDelayReqResTime_Object = MibTableColumn
f3PtpTrafficPortFlowPointHistoryMaxPDelayReqResTime = _F3PtpTrafficPortFlowPointHistoryMaxPDelayReqResTime_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 20, 1, 34),
    _F3PtpTrafficPortFlowPointHistoryMaxPDelayReqResTime_Type()
)
f3PtpTrafficPortFlowPointHistoryMaxPDelayReqResTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpTrafficPortFlowPointHistoryMaxPDelayReqResTime.setStatus("current")
_F3PtpTrafficPortFlowPointHistoryAvgPDelayReqResTime_Type = Unsigned32
_F3PtpTrafficPortFlowPointHistoryAvgPDelayReqResTime_Object = MibTableColumn
f3PtpTrafficPortFlowPointHistoryAvgPDelayReqResTime = _F3PtpTrafficPortFlowPointHistoryAvgPDelayReqResTime_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 20, 1, 35),
    _F3PtpTrafficPortFlowPointHistoryAvgPDelayReqResTime_Type()
)
f3PtpTrafficPortFlowPointHistoryAvgPDelayReqResTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpTrafficPortFlowPointHistoryAvgPDelayReqResTime.setStatus("current")
_F3PtpTrafficPortFlowPointHistoryMinPDelayRspResTime_Type = Unsigned32
_F3PtpTrafficPortFlowPointHistoryMinPDelayRspResTime_Object = MibTableColumn
f3PtpTrafficPortFlowPointHistoryMinPDelayRspResTime = _F3PtpTrafficPortFlowPointHistoryMinPDelayRspResTime_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 20, 1, 36),
    _F3PtpTrafficPortFlowPointHistoryMinPDelayRspResTime_Type()
)
f3PtpTrafficPortFlowPointHistoryMinPDelayRspResTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpTrafficPortFlowPointHistoryMinPDelayRspResTime.setStatus("current")
_F3PtpTrafficPortFlowPointHistoryMaxPDelayRspResTime_Type = Unsigned32
_F3PtpTrafficPortFlowPointHistoryMaxPDelayRspResTime_Object = MibTableColumn
f3PtpTrafficPortFlowPointHistoryMaxPDelayRspResTime = _F3PtpTrafficPortFlowPointHistoryMaxPDelayRspResTime_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 20, 1, 37),
    _F3PtpTrafficPortFlowPointHistoryMaxPDelayRspResTime_Type()
)
f3PtpTrafficPortFlowPointHistoryMaxPDelayRspResTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpTrafficPortFlowPointHistoryMaxPDelayRspResTime.setStatus("current")
_F3PtpTrafficPortFlowPointHistoryAvgPDelayRspResTime_Type = Unsigned32
_F3PtpTrafficPortFlowPointHistoryAvgPDelayRspResTime_Object = MibTableColumn
f3PtpTrafficPortFlowPointHistoryAvgPDelayRspResTime = _F3PtpTrafficPortFlowPointHistoryAvgPDelayRspResTime_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 20, 1, 38),
    _F3PtpTrafficPortFlowPointHistoryAvgPDelayRspResTime_Type()
)
f3PtpTrafficPortFlowPointHistoryAvgPDelayRspResTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpTrafficPortFlowPointHistoryAvgPDelayRspResTime.setStatus("current")
_F3PtpTrafficPortFlowPointHistoryDestMciNoMatchDiscards_Type = PerfCounter64
_F3PtpTrafficPortFlowPointHistoryDestMciNoMatchDiscards_Object = MibTableColumn
f3PtpTrafficPortFlowPointHistoryDestMciNoMatchDiscards = _F3PtpTrafficPortFlowPointHistoryDestMciNoMatchDiscards_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 20, 1, 39),
    _F3PtpTrafficPortFlowPointHistoryDestMciNoMatchDiscards_Type()
)
f3PtpTrafficPortFlowPointHistoryDestMciNoMatchDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpTrafficPortFlowPointHistoryDestMciNoMatchDiscards.setStatus("current")
_F3PtpTrafficPortFlowPointHistoryTagNoMatchDiscards_Type = PerfCounter64
_F3PtpTrafficPortFlowPointHistoryTagNoMatchDiscards_Object = MibTableColumn
f3PtpTrafficPortFlowPointHistoryTagNoMatchDiscards = _F3PtpTrafficPortFlowPointHistoryTagNoMatchDiscards_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 20, 1, 40),
    _F3PtpTrafficPortFlowPointHistoryTagNoMatchDiscards_Type()
)
f3PtpTrafficPortFlowPointHistoryTagNoMatchDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpTrafficPortFlowPointHistoryTagNoMatchDiscards.setStatus("current")
_F3PtpTrafficPortFlowPointThresholdTable_Object = MibTable
f3PtpTrafficPortFlowPointThresholdTable = _F3PtpTrafficPortFlowPointThresholdTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 21)
)
if mibBuilder.loadTexts:
    f3PtpTrafficPortFlowPointThresholdTable.setStatus("current")
_F3PtpTrafficPortFlowPointThresholdEntry_Object = MibTableRow
f3PtpTrafficPortFlowPointThresholdEntry = _F3PtpTrafficPortFlowPointThresholdEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 21, 1)
)
f3PtpTrafficPortFlowPointThresholdEntry.setIndexNames(
    (0, "CM-ENTITY-MIB", "neIndex"),
    (0, "CM-ENTITY-MIB", "shelfIndex"),
    (0, "CM-ENTITY-MIB", "slotIndex"),
    (0, "CM-FACILITY-MIB", "cmEthernetTrafficPortIndex"),
    (0, "F3-PTP-MIB", "f3PtpTrafficPortFlowPointIndex"),
    (0, "F3-PTP-MIB", "f3PtpTrafficPortFlowPointStatsIndex"),
    (0, "F3-PTP-MIB", "f3PtpTrafficPortFlowPointThresholdIndex"),
)
if mibBuilder.loadTexts:
    f3PtpTrafficPortFlowPointThresholdEntry.setStatus("current")


class _F3PtpTrafficPortFlowPointThresholdIndex_Type(Integer32):
    """Custom type f3PtpTrafficPortFlowPointThresholdIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_F3PtpTrafficPortFlowPointThresholdIndex_Type.__name__ = "Integer32"
_F3PtpTrafficPortFlowPointThresholdIndex_Object = MibTableColumn
f3PtpTrafficPortFlowPointThresholdIndex = _F3PtpTrafficPortFlowPointThresholdIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 21, 1, 1),
    _F3PtpTrafficPortFlowPointThresholdIndex_Type()
)
f3PtpTrafficPortFlowPointThresholdIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    f3PtpTrafficPortFlowPointThresholdIndex.setStatus("current")
_F3PtpTrafficPortFlowPointThresholdInterval_Type = CmPmIntervalType
_F3PtpTrafficPortFlowPointThresholdInterval_Object = MibTableColumn
f3PtpTrafficPortFlowPointThresholdInterval = _F3PtpTrafficPortFlowPointThresholdInterval_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 21, 1, 2),
    _F3PtpTrafficPortFlowPointThresholdInterval_Type()
)
f3PtpTrafficPortFlowPointThresholdInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpTrafficPortFlowPointThresholdInterval.setStatus("current")
_F3PtpTrafficPortFlowPointThresholdVariable_Type = VariablePointer
_F3PtpTrafficPortFlowPointThresholdVariable_Object = MibTableColumn
f3PtpTrafficPortFlowPointThresholdVariable = _F3PtpTrafficPortFlowPointThresholdVariable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 21, 1, 3),
    _F3PtpTrafficPortFlowPointThresholdVariable_Type()
)
f3PtpTrafficPortFlowPointThresholdVariable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpTrafficPortFlowPointThresholdVariable.setStatus("current")
_F3PtpTrafficPortFlowPointThresholdValueLo_Type = Unsigned32
_F3PtpTrafficPortFlowPointThresholdValueLo_Object = MibTableColumn
f3PtpTrafficPortFlowPointThresholdValueLo = _F3PtpTrafficPortFlowPointThresholdValueLo_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 21, 1, 4),
    _F3PtpTrafficPortFlowPointThresholdValueLo_Type()
)
f3PtpTrafficPortFlowPointThresholdValueLo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3PtpTrafficPortFlowPointThresholdValueLo.setStatus("current")
_F3PtpTrafficPortFlowPointThresholdValueHi_Type = Unsigned32
_F3PtpTrafficPortFlowPointThresholdValueHi_Object = MibTableColumn
f3PtpTrafficPortFlowPointThresholdValueHi = _F3PtpTrafficPortFlowPointThresholdValueHi_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 21, 1, 5),
    _F3PtpTrafficPortFlowPointThresholdValueHi_Type()
)
f3PtpTrafficPortFlowPointThresholdValueHi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3PtpTrafficPortFlowPointThresholdValueHi.setStatus("current")
_F3PtpTrafficPortFlowPointThresholdMonValue_Type = PerfCounter64
_F3PtpTrafficPortFlowPointThresholdMonValue_Object = MibTableColumn
f3PtpTrafficPortFlowPointThresholdMonValue = _F3PtpTrafficPortFlowPointThresholdMonValue_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 21, 1, 6),
    _F3PtpTrafficPortFlowPointThresholdMonValue_Type()
)
f3PtpTrafficPortFlowPointThresholdMonValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpTrafficPortFlowPointThresholdMonValue.setStatus("current")
_F3PtpPTPPortStatsTable_Object = MibTable
f3PtpPTPPortStatsTable = _F3PtpPTPPortStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 22)
)
if mibBuilder.loadTexts:
    f3PtpPTPPortStatsTable.setStatus("current")
_F3PtpPTPPortStatsEntry_Object = MibTableRow
f3PtpPTPPortStatsEntry = _F3PtpPTPPortStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 22, 1)
)
f3PtpPTPPortStatsEntry.setIndexNames(
    (0, "CM-ENTITY-MIB", "neIndex"),
    (0, "F3-PTP-MIB", "f3PtpPTPClockIndex"),
    (0, "F3-PTP-MIB", "f3PtpPTPPortIndex"),
    (0, "F3-PTP-MIB", "f3PtpPTPPortStatsIndex"),
)
if mibBuilder.loadTexts:
    f3PtpPTPPortStatsEntry.setStatus("current")


class _F3PtpPTPPortStatsIndex_Type(Integer32):
    """Custom type f3PtpPTPPortStatsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_F3PtpPTPPortStatsIndex_Type.__name__ = "Integer32"
_F3PtpPTPPortStatsIndex_Object = MibTableColumn
f3PtpPTPPortStatsIndex = _F3PtpPTPPortStatsIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 22, 1, 1),
    _F3PtpPTPPortStatsIndex_Type()
)
f3PtpPTPPortStatsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    f3PtpPTPPortStatsIndex.setStatus("current")
_F3PtpPTPPortStatsIntervalType_Type = CmPmIntervalType
_F3PtpPTPPortStatsIntervalType_Object = MibTableColumn
f3PtpPTPPortStatsIntervalType = _F3PtpPTPPortStatsIntervalType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 22, 1, 2),
    _F3PtpPTPPortStatsIntervalType_Type()
)
f3PtpPTPPortStatsIntervalType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpPTPPortStatsIntervalType.setStatus("current")
_F3PtpPTPPortStatsValid_Type = TruthValue
_F3PtpPTPPortStatsValid_Object = MibTableColumn
f3PtpPTPPortStatsValid = _F3PtpPTPPortStatsValid_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 22, 1, 3),
    _F3PtpPTPPortStatsValid_Type()
)
f3PtpPTPPortStatsValid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpPTPPortStatsValid.setStatus("current")
_F3PtpPTPPortStatsAction_Type = CmPmBinAction
_F3PtpPTPPortStatsAction_Object = MibTableColumn
f3PtpPTPPortStatsAction = _F3PtpPTPPortStatsAction_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 22, 1, 4),
    _F3PtpPTPPortStatsAction_Type()
)
f3PtpPTPPortStatsAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3PtpPTPPortStatsAction.setStatus("current")
_F3PtpPTPPortStatsAvgAnnounceRate_Type = Unsigned32
_F3PtpPTPPortStatsAvgAnnounceRate_Object = MibTableColumn
f3PtpPTPPortStatsAvgAnnounceRate = _F3PtpPTPPortStatsAvgAnnounceRate_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 22, 1, 5),
    _F3PtpPTPPortStatsAvgAnnounceRate_Type()
)
f3PtpPTPPortStatsAvgAnnounceRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpPTPPortStatsAvgAnnounceRate.setStatus("current")
_F3PtpPTPPortStatsAvgSyncRate_Type = Unsigned32
_F3PtpPTPPortStatsAvgSyncRate_Object = MibTableColumn
f3PtpPTPPortStatsAvgSyncRate = _F3PtpPTPPortStatsAvgSyncRate_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 22, 1, 6),
    _F3PtpPTPPortStatsAvgSyncRate_Type()
)
f3PtpPTPPortStatsAvgSyncRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpPTPPortStatsAvgSyncRate.setStatus("current")
_F3PtpPTPPortStatsAvgDelayReqRate_Type = Unsigned32
_F3PtpPTPPortStatsAvgDelayReqRate_Object = MibTableColumn
f3PtpPTPPortStatsAvgDelayReqRate = _F3PtpPTPPortStatsAvgDelayReqRate_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 22, 1, 7),
    _F3PtpPTPPortStatsAvgDelayReqRate_Type()
)
f3PtpPTPPortStatsAvgDelayReqRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpPTPPortStatsAvgDelayReqRate.setStatus("current")
_F3PtpPTPPortStatsAvgDelayRespRate_Type = Unsigned32
_F3PtpPTPPortStatsAvgDelayRespRate_Object = MibTableColumn
f3PtpPTPPortStatsAvgDelayRespRate = _F3PtpPTPPortStatsAvgDelayRespRate_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 22, 1, 8),
    _F3PtpPTPPortStatsAvgDelayRespRate_Type()
)
f3PtpPTPPortStatsAvgDelayRespRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpPTPPortStatsAvgDelayRespRate.setStatus("current")
_F3PtpPTPPortStatsMismatchDomainDiscards_Type = PerfCounter64
_F3PtpPTPPortStatsMismatchDomainDiscards_Object = MibTableColumn
f3PtpPTPPortStatsMismatchDomainDiscards = _F3PtpPTPPortStatsMismatchDomainDiscards_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 22, 1, 9),
    _F3PtpPTPPortStatsMismatchDomainDiscards_Type()
)
f3PtpPTPPortStatsMismatchDomainDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpPTPPortStatsMismatchDomainDiscards.setStatus("current")
_F3PtpPTPPortStatsMessageWrongTypeDiscards_Type = PerfCounter64
_F3PtpPTPPortStatsMessageWrongTypeDiscards_Object = MibTableColumn
f3PtpPTPPortStatsMessageWrongTypeDiscards = _F3PtpPTPPortStatsMessageWrongTypeDiscards_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 22, 1, 10),
    _F3PtpPTPPortStatsMessageWrongTypeDiscards_Type()
)
f3PtpPTPPortStatsMessageWrongTypeDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpPTPPortStatsMessageWrongTypeDiscards.setStatus("current")
_F3PtpPTPPortStatsMessagesWrongLengthDiscards_Type = PerfCounter64
_F3PtpPTPPortStatsMessagesWrongLengthDiscards_Object = MibTableColumn
f3PtpPTPPortStatsMessagesWrongLengthDiscards = _F3PtpPTPPortStatsMessagesWrongLengthDiscards_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 22, 1, 11),
    _F3PtpPTPPortStatsMessagesWrongLengthDiscards_Type()
)
f3PtpPTPPortStatsMessagesWrongLengthDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpPTPPortStatsMessagesWrongLengthDiscards.setStatus("current")
_F3PtpPTPPortStatsUnknownMasterDiscards_Type = PerfCounter64
_F3PtpPTPPortStatsUnknownMasterDiscards_Object = MibTableColumn
f3PtpPTPPortStatsUnknownMasterDiscards = _F3PtpPTPPortStatsUnknownMasterDiscards_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 22, 1, 12),
    _F3PtpPTPPortStatsUnknownMasterDiscards_Type()
)
f3PtpPTPPortStatsUnknownMasterDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpPTPPortStatsUnknownMasterDiscards.setStatus("deprecated")
_F3PtpPTPPortStatsMinOffsetFromMaster_Type = PerfCounter64
_F3PtpPTPPortStatsMinOffsetFromMaster_Object = MibTableColumn
f3PtpPTPPortStatsMinOffsetFromMaster = _F3PtpPTPPortStatsMinOffsetFromMaster_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 22, 1, 13),
    _F3PtpPTPPortStatsMinOffsetFromMaster_Type()
)
f3PtpPTPPortStatsMinOffsetFromMaster.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpPTPPortStatsMinOffsetFromMaster.setStatus("current")
_F3PtpPTPPortStatsMaxOffsetFromMaster_Type = PerfCounter64
_F3PtpPTPPortStatsMaxOffsetFromMaster_Object = MibTableColumn
f3PtpPTPPortStatsMaxOffsetFromMaster = _F3PtpPTPPortStatsMaxOffsetFromMaster_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 22, 1, 14),
    _F3PtpPTPPortStatsMaxOffsetFromMaster_Type()
)
f3PtpPTPPortStatsMaxOffsetFromMaster.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpPTPPortStatsMaxOffsetFromMaster.setStatus("current")
_F3PtpPTPPortStatsAvgOffsetFromMaster_Type = PerfCounter64
_F3PtpPTPPortStatsAvgOffsetFromMaster_Object = MibTableColumn
f3PtpPTPPortStatsAvgOffsetFromMaster = _F3PtpPTPPortStatsAvgOffsetFromMaster_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 22, 1, 15),
    _F3PtpPTPPortStatsAvgOffsetFromMaster_Type()
)
f3PtpPTPPortStatsAvgOffsetFromMaster.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpPTPPortStatsAvgOffsetFromMaster.setStatus("current")
_F3PtpPTPPortStatsMinSyncPathDelay_Type = PerfCounter64
_F3PtpPTPPortStatsMinSyncPathDelay_Object = MibTableColumn
f3PtpPTPPortStatsMinSyncPathDelay = _F3PtpPTPPortStatsMinSyncPathDelay_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 22, 1, 16),
    _F3PtpPTPPortStatsMinSyncPathDelay_Type()
)
f3PtpPTPPortStatsMinSyncPathDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpPTPPortStatsMinSyncPathDelay.setStatus("current")
_F3PtpPTPPortStatsMaxSyncPathDelay_Type = PerfCounter64
_F3PtpPTPPortStatsMaxSyncPathDelay_Object = MibTableColumn
f3PtpPTPPortStatsMaxSyncPathDelay = _F3PtpPTPPortStatsMaxSyncPathDelay_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 22, 1, 17),
    _F3PtpPTPPortStatsMaxSyncPathDelay_Type()
)
f3PtpPTPPortStatsMaxSyncPathDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpPTPPortStatsMaxSyncPathDelay.setStatus("current")
_F3PtpPTPPortStatsAvgSyncPathDelay_Type = PerfCounter64
_F3PtpPTPPortStatsAvgSyncPathDelay_Object = MibTableColumn
f3PtpPTPPortStatsAvgSyncPathDelay = _F3PtpPTPPortStatsAvgSyncPathDelay_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 22, 1, 18),
    _F3PtpPTPPortStatsAvgSyncPathDelay_Type()
)
f3PtpPTPPortStatsAvgSyncPathDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpPTPPortStatsAvgSyncPathDelay.setStatus("current")
_F3PtpPTPPortStatsMinMeanPathDelay_Type = PerfCounter64
_F3PtpPTPPortStatsMinMeanPathDelay_Object = MibTableColumn
f3PtpPTPPortStatsMinMeanPathDelay = _F3PtpPTPPortStatsMinMeanPathDelay_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 22, 1, 19),
    _F3PtpPTPPortStatsMinMeanPathDelay_Type()
)
f3PtpPTPPortStatsMinMeanPathDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpPTPPortStatsMinMeanPathDelay.setStatus("current")
_F3PtpPTPPortStatsMaxMeanPathDelay_Type = PerfCounter64
_F3PtpPTPPortStatsMaxMeanPathDelay_Object = MibTableColumn
f3PtpPTPPortStatsMaxMeanPathDelay = _F3PtpPTPPortStatsMaxMeanPathDelay_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 22, 1, 20),
    _F3PtpPTPPortStatsMaxMeanPathDelay_Type()
)
f3PtpPTPPortStatsMaxMeanPathDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpPTPPortStatsMaxMeanPathDelay.setStatus("current")
_F3PtpPTPPortStatsAvgMeanPathDelay_Type = PerfCounter64
_F3PtpPTPPortStatsAvgMeanPathDelay_Object = MibTableColumn
f3PtpPTPPortStatsAvgMeanPathDelay = _F3PtpPTPPortStatsAvgMeanPathDelay_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 22, 1, 21),
    _F3PtpPTPPortStatsAvgMeanPathDelay_Type()
)
f3PtpPTPPortStatsAvgMeanPathDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpPTPPortStatsAvgMeanPathDelay.setStatus("current")
_F3PtpPTPPortStatsMsgMiscDiscards_Type = PerfCounter64
_F3PtpPTPPortStatsMsgMiscDiscards_Object = MibTableColumn
f3PtpPTPPortStatsMsgMiscDiscards = _F3PtpPTPPortStatsMsgMiscDiscards_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 22, 1, 22),
    _F3PtpPTPPortStatsMsgMiscDiscards_Type()
)
f3PtpPTPPortStatsMsgMiscDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpPTPPortStatsMsgMiscDiscards.setStatus("deprecated")
_F3PtpPTPPortHistoryTable_Object = MibTable
f3PtpPTPPortHistoryTable = _F3PtpPTPPortHistoryTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 23)
)
if mibBuilder.loadTexts:
    f3PtpPTPPortHistoryTable.setStatus("current")
_F3PtpPTPPortHistoryEntry_Object = MibTableRow
f3PtpPTPPortHistoryEntry = _F3PtpPTPPortHistoryEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 23, 1)
)
f3PtpPTPPortHistoryEntry.setIndexNames(
    (0, "CM-ENTITY-MIB", "neIndex"),
    (0, "F3-PTP-MIB", "f3PtpPTPClockIndex"),
    (0, "F3-PTP-MIB", "f3PtpPTPPortIndex"),
    (0, "F3-PTP-MIB", "f3PtpPTPPortStatsIndex"),
    (0, "F3-PTP-MIB", "f3PtpPTPPortHistoryIndex"),
)
if mibBuilder.loadTexts:
    f3PtpPTPPortHistoryEntry.setStatus("current")


class _F3PtpPTPPortHistoryIndex_Type(Integer32):
    """Custom type f3PtpPTPPortHistoryIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_F3PtpPTPPortHistoryIndex_Type.__name__ = "Integer32"
_F3PtpPTPPortHistoryIndex_Object = MibTableColumn
f3PtpPTPPortHistoryIndex = _F3PtpPTPPortHistoryIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 23, 1, 1),
    _F3PtpPTPPortHistoryIndex_Type()
)
f3PtpPTPPortHistoryIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    f3PtpPTPPortHistoryIndex.setStatus("current")
_F3PtpPTPPortHistoryTime_Type = DateAndTime
_F3PtpPTPPortHistoryTime_Object = MibTableColumn
f3PtpPTPPortHistoryTime = _F3PtpPTPPortHistoryTime_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 23, 1, 2),
    _F3PtpPTPPortHistoryTime_Type()
)
f3PtpPTPPortHistoryTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpPTPPortHistoryTime.setStatus("current")
_F3PtpPTPPortHistoryValid_Type = TruthValue
_F3PtpPTPPortHistoryValid_Object = MibTableColumn
f3PtpPTPPortHistoryValid = _F3PtpPTPPortHistoryValid_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 23, 1, 3),
    _F3PtpPTPPortHistoryValid_Type()
)
f3PtpPTPPortHistoryValid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpPTPPortHistoryValid.setStatus("current")
_F3PtpPTPPortHistoryAction_Type = CmPmBinAction
_F3PtpPTPPortHistoryAction_Object = MibTableColumn
f3PtpPTPPortHistoryAction = _F3PtpPTPPortHistoryAction_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 23, 1, 4),
    _F3PtpPTPPortHistoryAction_Type()
)
f3PtpPTPPortHistoryAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3PtpPTPPortHistoryAction.setStatus("current")
_F3PtpPTPPortHistoryAvgAnnounceRate_Type = Unsigned32
_F3PtpPTPPortHistoryAvgAnnounceRate_Object = MibTableColumn
f3PtpPTPPortHistoryAvgAnnounceRate = _F3PtpPTPPortHistoryAvgAnnounceRate_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 23, 1, 5),
    _F3PtpPTPPortHistoryAvgAnnounceRate_Type()
)
f3PtpPTPPortHistoryAvgAnnounceRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpPTPPortHistoryAvgAnnounceRate.setStatus("current")
_F3PtpPTPPortHistoryAvgSyncRate_Type = Unsigned32
_F3PtpPTPPortHistoryAvgSyncRate_Object = MibTableColumn
f3PtpPTPPortHistoryAvgSyncRate = _F3PtpPTPPortHistoryAvgSyncRate_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 23, 1, 6),
    _F3PtpPTPPortHistoryAvgSyncRate_Type()
)
f3PtpPTPPortHistoryAvgSyncRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpPTPPortHistoryAvgSyncRate.setStatus("current")
_F3PtpPTPPortHistoryAvgDelayReqRate_Type = Unsigned32
_F3PtpPTPPortHistoryAvgDelayReqRate_Object = MibTableColumn
f3PtpPTPPortHistoryAvgDelayReqRate = _F3PtpPTPPortHistoryAvgDelayReqRate_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 23, 1, 7),
    _F3PtpPTPPortHistoryAvgDelayReqRate_Type()
)
f3PtpPTPPortHistoryAvgDelayReqRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpPTPPortHistoryAvgDelayReqRate.setStatus("current")
_F3PtpPTPPortHistoryAvgDelayRespRate_Type = Unsigned32
_F3PtpPTPPortHistoryAvgDelayRespRate_Object = MibTableColumn
f3PtpPTPPortHistoryAvgDelayRespRate = _F3PtpPTPPortHistoryAvgDelayRespRate_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 23, 1, 8),
    _F3PtpPTPPortHistoryAvgDelayRespRate_Type()
)
f3PtpPTPPortHistoryAvgDelayRespRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpPTPPortHistoryAvgDelayRespRate.setStatus("current")
_F3PtpPTPPortHistoryMismatchDomainDiscards_Type = PerfCounter64
_F3PtpPTPPortHistoryMismatchDomainDiscards_Object = MibTableColumn
f3PtpPTPPortHistoryMismatchDomainDiscards = _F3PtpPTPPortHistoryMismatchDomainDiscards_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 23, 1, 9),
    _F3PtpPTPPortHistoryMismatchDomainDiscards_Type()
)
f3PtpPTPPortHistoryMismatchDomainDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpPTPPortHistoryMismatchDomainDiscards.setStatus("current")
_F3PtpPTPPortHistoryMessageWrongTypeDiscards_Type = PerfCounter64
_F3PtpPTPPortHistoryMessageWrongTypeDiscards_Object = MibTableColumn
f3PtpPTPPortHistoryMessageWrongTypeDiscards = _F3PtpPTPPortHistoryMessageWrongTypeDiscards_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 23, 1, 10),
    _F3PtpPTPPortHistoryMessageWrongTypeDiscards_Type()
)
f3PtpPTPPortHistoryMessageWrongTypeDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpPTPPortHistoryMessageWrongTypeDiscards.setStatus("current")
_F3PtpPTPPortHistoryMessagesWrongLengthDiscards_Type = PerfCounter64
_F3PtpPTPPortHistoryMessagesWrongLengthDiscards_Object = MibTableColumn
f3PtpPTPPortHistoryMessagesWrongLengthDiscards = _F3PtpPTPPortHistoryMessagesWrongLengthDiscards_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 23, 1, 11),
    _F3PtpPTPPortHistoryMessagesWrongLengthDiscards_Type()
)
f3PtpPTPPortHistoryMessagesWrongLengthDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpPTPPortHistoryMessagesWrongLengthDiscards.setStatus("current")
_F3PtpPTPPortHistoryUnknownMasterDiscards_Type = PerfCounter64
_F3PtpPTPPortHistoryUnknownMasterDiscards_Object = MibTableColumn
f3PtpPTPPortHistoryUnknownMasterDiscards = _F3PtpPTPPortHistoryUnknownMasterDiscards_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 23, 1, 12),
    _F3PtpPTPPortHistoryUnknownMasterDiscards_Type()
)
f3PtpPTPPortHistoryUnknownMasterDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpPTPPortHistoryUnknownMasterDiscards.setStatus("deprecated")
_F3PtpPTPPortHistoryMinOffsetFromMaster_Type = PerfCounter64
_F3PtpPTPPortHistoryMinOffsetFromMaster_Object = MibTableColumn
f3PtpPTPPortHistoryMinOffsetFromMaster = _F3PtpPTPPortHistoryMinOffsetFromMaster_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 23, 1, 13),
    _F3PtpPTPPortHistoryMinOffsetFromMaster_Type()
)
f3PtpPTPPortHistoryMinOffsetFromMaster.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpPTPPortHistoryMinOffsetFromMaster.setStatus("current")
_F3PtpPTPPortHistoryMaxOffsetFromMaster_Type = PerfCounter64
_F3PtpPTPPortHistoryMaxOffsetFromMaster_Object = MibTableColumn
f3PtpPTPPortHistoryMaxOffsetFromMaster = _F3PtpPTPPortHistoryMaxOffsetFromMaster_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 23, 1, 14),
    _F3PtpPTPPortHistoryMaxOffsetFromMaster_Type()
)
f3PtpPTPPortHistoryMaxOffsetFromMaster.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpPTPPortHistoryMaxOffsetFromMaster.setStatus("current")
_F3PtpPTPPortHistoryAvgOffsetFromMaster_Type = PerfCounter64
_F3PtpPTPPortHistoryAvgOffsetFromMaster_Object = MibTableColumn
f3PtpPTPPortHistoryAvgOffsetFromMaster = _F3PtpPTPPortHistoryAvgOffsetFromMaster_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 23, 1, 15),
    _F3PtpPTPPortHistoryAvgOffsetFromMaster_Type()
)
f3PtpPTPPortHistoryAvgOffsetFromMaster.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpPTPPortHistoryAvgOffsetFromMaster.setStatus("current")
_F3PtpPTPPortHistoryMinSyncPathDelay_Type = PerfCounter64
_F3PtpPTPPortHistoryMinSyncPathDelay_Object = MibTableColumn
f3PtpPTPPortHistoryMinSyncPathDelay = _F3PtpPTPPortHistoryMinSyncPathDelay_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 23, 1, 16),
    _F3PtpPTPPortHistoryMinSyncPathDelay_Type()
)
f3PtpPTPPortHistoryMinSyncPathDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpPTPPortHistoryMinSyncPathDelay.setStatus("current")
_F3PtpPTPPortHistoryMaxSyncPathDelay_Type = PerfCounter64
_F3PtpPTPPortHistoryMaxSyncPathDelay_Object = MibTableColumn
f3PtpPTPPortHistoryMaxSyncPathDelay = _F3PtpPTPPortHistoryMaxSyncPathDelay_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 23, 1, 17),
    _F3PtpPTPPortHistoryMaxSyncPathDelay_Type()
)
f3PtpPTPPortHistoryMaxSyncPathDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpPTPPortHistoryMaxSyncPathDelay.setStatus("current")
_F3PtpPTPPortHistoryAvgSyncPathDelay_Type = PerfCounter64
_F3PtpPTPPortHistoryAvgSyncPathDelay_Object = MibTableColumn
f3PtpPTPPortHistoryAvgSyncPathDelay = _F3PtpPTPPortHistoryAvgSyncPathDelay_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 23, 1, 18),
    _F3PtpPTPPortHistoryAvgSyncPathDelay_Type()
)
f3PtpPTPPortHistoryAvgSyncPathDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpPTPPortHistoryAvgSyncPathDelay.setStatus("current")
_F3PtpPTPPortHistoryMinMeanPathDelay_Type = PerfCounter64
_F3PtpPTPPortHistoryMinMeanPathDelay_Object = MibTableColumn
f3PtpPTPPortHistoryMinMeanPathDelay = _F3PtpPTPPortHistoryMinMeanPathDelay_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 23, 1, 19),
    _F3PtpPTPPortHistoryMinMeanPathDelay_Type()
)
f3PtpPTPPortHistoryMinMeanPathDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpPTPPortHistoryMinMeanPathDelay.setStatus("current")
_F3PtpPTPPortHistoryMaxMeanPathDelay_Type = PerfCounter64
_F3PtpPTPPortHistoryMaxMeanPathDelay_Object = MibTableColumn
f3PtpPTPPortHistoryMaxMeanPathDelay = _F3PtpPTPPortHistoryMaxMeanPathDelay_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 23, 1, 20),
    _F3PtpPTPPortHistoryMaxMeanPathDelay_Type()
)
f3PtpPTPPortHistoryMaxMeanPathDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpPTPPortHistoryMaxMeanPathDelay.setStatus("current")
_F3PtpPTPPortHistoryAvgMeanPathDelay_Type = PerfCounter64
_F3PtpPTPPortHistoryAvgMeanPathDelay_Object = MibTableColumn
f3PtpPTPPortHistoryAvgMeanPathDelay = _F3PtpPTPPortHistoryAvgMeanPathDelay_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 23, 1, 21),
    _F3PtpPTPPortHistoryAvgMeanPathDelay_Type()
)
f3PtpPTPPortHistoryAvgMeanPathDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpPTPPortHistoryAvgMeanPathDelay.setStatus("current")
_F3PtpPTPPortHistoryMsgMiscDiscards_Type = PerfCounter64
_F3PtpPTPPortHistoryMsgMiscDiscards_Object = MibTableColumn
f3PtpPTPPortHistoryMsgMiscDiscards = _F3PtpPTPPortHistoryMsgMiscDiscards_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 23, 1, 22),
    _F3PtpPTPPortHistoryMsgMiscDiscards_Type()
)
f3PtpPTPPortHistoryMsgMiscDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpPTPPortHistoryMsgMiscDiscards.setStatus("deprecated")
_F3PtpPTPPortThresholdTable_Object = MibTable
f3PtpPTPPortThresholdTable = _F3PtpPTPPortThresholdTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 24)
)
if mibBuilder.loadTexts:
    f3PtpPTPPortThresholdTable.setStatus("current")
_F3PtpPTPPortThresholdEntry_Object = MibTableRow
f3PtpPTPPortThresholdEntry = _F3PtpPTPPortThresholdEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 24, 1)
)
f3PtpPTPPortThresholdEntry.setIndexNames(
    (0, "CM-ENTITY-MIB", "neIndex"),
    (0, "F3-PTP-MIB", "f3PtpPTPClockIndex"),
    (0, "F3-PTP-MIB", "f3PtpPTPPortIndex"),
    (0, "F3-PTP-MIB", "f3PtpPTPPortStatsIndex"),
    (0, "F3-PTP-MIB", "f3PtpPTPPortThresholdIndex"),
)
if mibBuilder.loadTexts:
    f3PtpPTPPortThresholdEntry.setStatus("current")


class _F3PtpPTPPortThresholdIndex_Type(Integer32):
    """Custom type f3PtpPTPPortThresholdIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_F3PtpPTPPortThresholdIndex_Type.__name__ = "Integer32"
_F3PtpPTPPortThresholdIndex_Object = MibTableColumn
f3PtpPTPPortThresholdIndex = _F3PtpPTPPortThresholdIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 24, 1, 1),
    _F3PtpPTPPortThresholdIndex_Type()
)
f3PtpPTPPortThresholdIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    f3PtpPTPPortThresholdIndex.setStatus("current")
_F3PtpPTPPortThresholdInterval_Type = CmPmIntervalType
_F3PtpPTPPortThresholdInterval_Object = MibTableColumn
f3PtpPTPPortThresholdInterval = _F3PtpPTPPortThresholdInterval_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 24, 1, 2),
    _F3PtpPTPPortThresholdInterval_Type()
)
f3PtpPTPPortThresholdInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpPTPPortThresholdInterval.setStatus("current")
_F3PtpPTPPortThresholdVariable_Type = VariablePointer
_F3PtpPTPPortThresholdVariable_Object = MibTableColumn
f3PtpPTPPortThresholdVariable = _F3PtpPTPPortThresholdVariable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 24, 1, 3),
    _F3PtpPTPPortThresholdVariable_Type()
)
f3PtpPTPPortThresholdVariable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpPTPPortThresholdVariable.setStatus("current")
_F3PtpPTPPortThresholdValueLo_Type = Unsigned32
_F3PtpPTPPortThresholdValueLo_Object = MibTableColumn
f3PtpPTPPortThresholdValueLo = _F3PtpPTPPortThresholdValueLo_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 24, 1, 4),
    _F3PtpPTPPortThresholdValueLo_Type()
)
f3PtpPTPPortThresholdValueLo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3PtpPTPPortThresholdValueLo.setStatus("current")
_F3PtpPTPPortThresholdValueHi_Type = Unsigned32
_F3PtpPTPPortThresholdValueHi_Object = MibTableColumn
f3PtpPTPPortThresholdValueHi = _F3PtpPTPPortThresholdValueHi_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 24, 1, 5),
    _F3PtpPTPPortThresholdValueHi_Type()
)
f3PtpPTPPortThresholdValueHi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3PtpPTPPortThresholdValueHi.setStatus("current")
_F3PtpPTPPortThresholdMonValue_Type = PerfCounter64
_F3PtpPTPPortThresholdMonValue_Object = MibTableColumn
f3PtpPTPPortThresholdMonValue = _F3PtpPTPPortThresholdMonValue_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 24, 1, 6),
    _F3PtpPTPPortThresholdMonValue_Type()
)
f3PtpPTPPortThresholdMonValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpPTPPortThresholdMonValue.setStatus("current")
_F3PtpPTPClockStatsTable_Object = MibTable
f3PtpPTPClockStatsTable = _F3PtpPTPClockStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 25)
)
if mibBuilder.loadTexts:
    f3PtpPTPClockStatsTable.setStatus("current")
_F3PtpPTPClockStatsEntry_Object = MibTableRow
f3PtpPTPClockStatsEntry = _F3PtpPTPClockStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 25, 1)
)
f3PtpPTPClockStatsEntry.setIndexNames(
    (0, "CM-ENTITY-MIB", "neIndex"),
    (0, "F3-PTP-MIB", "f3PtpPTPClockIndex"),
    (0, "F3-PTP-MIB", "f3PtpPTPClockStatsIndex"),
)
if mibBuilder.loadTexts:
    f3PtpPTPClockStatsEntry.setStatus("current")


class _F3PtpPTPClockStatsIndex_Type(Integer32):
    """Custom type f3PtpPTPClockStatsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_F3PtpPTPClockStatsIndex_Type.__name__ = "Integer32"
_F3PtpPTPClockStatsIndex_Object = MibTableColumn
f3PtpPTPClockStatsIndex = _F3PtpPTPClockStatsIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 25, 1, 1),
    _F3PtpPTPClockStatsIndex_Type()
)
f3PtpPTPClockStatsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    f3PtpPTPClockStatsIndex.setStatus("current")
_F3PtpPTPClockStatsIntervalType_Type = CmPmIntervalType
_F3PtpPTPClockStatsIntervalType_Object = MibTableColumn
f3PtpPTPClockStatsIntervalType = _F3PtpPTPClockStatsIntervalType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 25, 1, 2),
    _F3PtpPTPClockStatsIntervalType_Type()
)
f3PtpPTPClockStatsIntervalType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpPTPClockStatsIntervalType.setStatus("current")
_F3PtpPTPClockStatsValid_Type = TruthValue
_F3PtpPTPClockStatsValid_Object = MibTableColumn
f3PtpPTPClockStatsValid = _F3PtpPTPClockStatsValid_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 25, 1, 3),
    _F3PtpPTPClockStatsValid_Type()
)
f3PtpPTPClockStatsValid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpPTPClockStatsValid.setStatus("current")
_F3PtpPTPClockStatsAction_Type = CmPmBinAction
_F3PtpPTPClockStatsAction_Object = MibTableColumn
f3PtpPTPClockStatsAction = _F3PtpPTPClockStatsAction_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 25, 1, 4),
    _F3PtpPTPClockStatsAction_Type()
)
f3PtpPTPClockStatsAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3PtpPTPClockStatsAction.setStatus("current")
_F3PtpPTPClockStatsMinOffsetFromMaster_Type = ScaledNanoseconds
_F3PtpPTPClockStatsMinOffsetFromMaster_Object = MibTableColumn
f3PtpPTPClockStatsMinOffsetFromMaster = _F3PtpPTPClockStatsMinOffsetFromMaster_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 25, 1, 5),
    _F3PtpPTPClockStatsMinOffsetFromMaster_Type()
)
f3PtpPTPClockStatsMinOffsetFromMaster.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpPTPClockStatsMinOffsetFromMaster.setStatus("current")
_F3PtpPTPClockStatsMaxOffsetFromMaster_Type = ScaledNanoseconds
_F3PtpPTPClockStatsMaxOffsetFromMaster_Object = MibTableColumn
f3PtpPTPClockStatsMaxOffsetFromMaster = _F3PtpPTPClockStatsMaxOffsetFromMaster_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 25, 1, 6),
    _F3PtpPTPClockStatsMaxOffsetFromMaster_Type()
)
f3PtpPTPClockStatsMaxOffsetFromMaster.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpPTPClockStatsMaxOffsetFromMaster.setStatus("current")
_F3PtpPTPClockStatsAvgOffsetFromMaster_Type = ScaledNanoseconds
_F3PtpPTPClockStatsAvgOffsetFromMaster_Object = MibTableColumn
f3PtpPTPClockStatsAvgOffsetFromMaster = _F3PtpPTPClockStatsAvgOffsetFromMaster_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 25, 1, 7),
    _F3PtpPTPClockStatsAvgOffsetFromMaster_Type()
)
f3PtpPTPClockStatsAvgOffsetFromMaster.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpPTPClockStatsAvgOffsetFromMaster.setStatus("current")
_F3PtpPTPClockStatsMinSyncPathDelay_Type = ScaledNanoseconds
_F3PtpPTPClockStatsMinSyncPathDelay_Object = MibTableColumn
f3PtpPTPClockStatsMinSyncPathDelay = _F3PtpPTPClockStatsMinSyncPathDelay_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 25, 1, 8),
    _F3PtpPTPClockStatsMinSyncPathDelay_Type()
)
f3PtpPTPClockStatsMinSyncPathDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpPTPClockStatsMinSyncPathDelay.setStatus("current")
_F3PtpPTPClockStatsMaxSyncPathDelay_Type = ScaledNanoseconds
_F3PtpPTPClockStatsMaxSyncPathDelay_Object = MibTableColumn
f3PtpPTPClockStatsMaxSyncPathDelay = _F3PtpPTPClockStatsMaxSyncPathDelay_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 25, 1, 9),
    _F3PtpPTPClockStatsMaxSyncPathDelay_Type()
)
f3PtpPTPClockStatsMaxSyncPathDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpPTPClockStatsMaxSyncPathDelay.setStatus("current")
_F3PtpPTPClockStatsAvgSyncPathDelay_Type = ScaledNanoseconds
_F3PtpPTPClockStatsAvgSyncPathDelay_Object = MibTableColumn
f3PtpPTPClockStatsAvgSyncPathDelay = _F3PtpPTPClockStatsAvgSyncPathDelay_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 25, 1, 10),
    _F3PtpPTPClockStatsAvgSyncPathDelay_Type()
)
f3PtpPTPClockStatsAvgSyncPathDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpPTPClockStatsAvgSyncPathDelay.setStatus("current")
_F3PtpPTPClockStatsMinMeanPathDelay_Type = ScaledNanoseconds
_F3PtpPTPClockStatsMinMeanPathDelay_Object = MibTableColumn
f3PtpPTPClockStatsMinMeanPathDelay = _F3PtpPTPClockStatsMinMeanPathDelay_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 25, 1, 11),
    _F3PtpPTPClockStatsMinMeanPathDelay_Type()
)
f3PtpPTPClockStatsMinMeanPathDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpPTPClockStatsMinMeanPathDelay.setStatus("current")
_F3PtpPTPClockStatsMaxMeanPathDelay_Type = ScaledNanoseconds
_F3PtpPTPClockStatsMaxMeanPathDelay_Object = MibTableColumn
f3PtpPTPClockStatsMaxMeanPathDelay = _F3PtpPTPClockStatsMaxMeanPathDelay_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 25, 1, 12),
    _F3PtpPTPClockStatsMaxMeanPathDelay_Type()
)
f3PtpPTPClockStatsMaxMeanPathDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpPTPClockStatsMaxMeanPathDelay.setStatus("current")
_F3PtpPTPClockStatsAvgMeanPathDelay_Type = ScaledNanoseconds
_F3PtpPTPClockStatsAvgMeanPathDelay_Object = MibTableColumn
f3PtpPTPClockStatsAvgMeanPathDelay = _F3PtpPTPClockStatsAvgMeanPathDelay_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 25, 1, 13),
    _F3PtpPTPClockStatsAvgMeanPathDelay_Type()
)
f3PtpPTPClockStatsAvgMeanPathDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpPTPClockStatsAvgMeanPathDelay.setStatus("current")
_F3PtpPTPClockHistoryTable_Object = MibTable
f3PtpPTPClockHistoryTable = _F3PtpPTPClockHistoryTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 26)
)
if mibBuilder.loadTexts:
    f3PtpPTPClockHistoryTable.setStatus("current")
_F3PtpPTPClockHistoryEntry_Object = MibTableRow
f3PtpPTPClockHistoryEntry = _F3PtpPTPClockHistoryEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 26, 1)
)
f3PtpPTPClockHistoryEntry.setIndexNames(
    (0, "CM-ENTITY-MIB", "neIndex"),
    (0, "F3-PTP-MIB", "f3PtpPTPClockIndex"),
    (0, "F3-PTP-MIB", "f3PtpPTPClockStatsIndex"),
    (0, "F3-PTP-MIB", "f3PtpPTPClockHistoryIndex"),
)
if mibBuilder.loadTexts:
    f3PtpPTPClockHistoryEntry.setStatus("current")


class _F3PtpPTPClockHistoryIndex_Type(Integer32):
    """Custom type f3PtpPTPClockHistoryIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_F3PtpPTPClockHistoryIndex_Type.__name__ = "Integer32"
_F3PtpPTPClockHistoryIndex_Object = MibTableColumn
f3PtpPTPClockHistoryIndex = _F3PtpPTPClockHistoryIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 26, 1, 1),
    _F3PtpPTPClockHistoryIndex_Type()
)
f3PtpPTPClockHistoryIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    f3PtpPTPClockHistoryIndex.setStatus("current")
_F3PtpPTPClockHistoryTime_Type = DateAndTime
_F3PtpPTPClockHistoryTime_Object = MibTableColumn
f3PtpPTPClockHistoryTime = _F3PtpPTPClockHistoryTime_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 26, 1, 2),
    _F3PtpPTPClockHistoryTime_Type()
)
f3PtpPTPClockHistoryTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpPTPClockHistoryTime.setStatus("current")
_F3PtpPTPClockHistoryValid_Type = TruthValue
_F3PtpPTPClockHistoryValid_Object = MibTableColumn
f3PtpPTPClockHistoryValid = _F3PtpPTPClockHistoryValid_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 26, 1, 3),
    _F3PtpPTPClockHistoryValid_Type()
)
f3PtpPTPClockHistoryValid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpPTPClockHistoryValid.setStatus("current")
_F3PtpPTPClockHistoryAction_Type = CmPmBinAction
_F3PtpPTPClockHistoryAction_Object = MibTableColumn
f3PtpPTPClockHistoryAction = _F3PtpPTPClockHistoryAction_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 26, 1, 4),
    _F3PtpPTPClockHistoryAction_Type()
)
f3PtpPTPClockHistoryAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3PtpPTPClockHistoryAction.setStatus("current")
_F3PtpPTPClockHistoryMinOffsetFromMaster_Type = ScaledNanoseconds
_F3PtpPTPClockHistoryMinOffsetFromMaster_Object = MibTableColumn
f3PtpPTPClockHistoryMinOffsetFromMaster = _F3PtpPTPClockHistoryMinOffsetFromMaster_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 26, 1, 5),
    _F3PtpPTPClockHistoryMinOffsetFromMaster_Type()
)
f3PtpPTPClockHistoryMinOffsetFromMaster.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpPTPClockHistoryMinOffsetFromMaster.setStatus("current")
_F3PtpPTPClockHistoryMaxOffsetFromMaster_Type = ScaledNanoseconds
_F3PtpPTPClockHistoryMaxOffsetFromMaster_Object = MibTableColumn
f3PtpPTPClockHistoryMaxOffsetFromMaster = _F3PtpPTPClockHistoryMaxOffsetFromMaster_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 26, 1, 6),
    _F3PtpPTPClockHistoryMaxOffsetFromMaster_Type()
)
f3PtpPTPClockHistoryMaxOffsetFromMaster.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpPTPClockHistoryMaxOffsetFromMaster.setStatus("current")
_F3PtpPTPClockHistoryAvgOffsetFromMaster_Type = ScaledNanoseconds
_F3PtpPTPClockHistoryAvgOffsetFromMaster_Object = MibTableColumn
f3PtpPTPClockHistoryAvgOffsetFromMaster = _F3PtpPTPClockHistoryAvgOffsetFromMaster_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 26, 1, 7),
    _F3PtpPTPClockHistoryAvgOffsetFromMaster_Type()
)
f3PtpPTPClockHistoryAvgOffsetFromMaster.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpPTPClockHistoryAvgOffsetFromMaster.setStatus("current")
_F3PtpPTPClockHistoryMinSyncPathDelay_Type = ScaledNanoseconds
_F3PtpPTPClockHistoryMinSyncPathDelay_Object = MibTableColumn
f3PtpPTPClockHistoryMinSyncPathDelay = _F3PtpPTPClockHistoryMinSyncPathDelay_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 26, 1, 8),
    _F3PtpPTPClockHistoryMinSyncPathDelay_Type()
)
f3PtpPTPClockHistoryMinSyncPathDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpPTPClockHistoryMinSyncPathDelay.setStatus("current")
_F3PtpPTPClockHistoryMaxSyncPathDelay_Type = ScaledNanoseconds
_F3PtpPTPClockHistoryMaxSyncPathDelay_Object = MibTableColumn
f3PtpPTPClockHistoryMaxSyncPathDelay = _F3PtpPTPClockHistoryMaxSyncPathDelay_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 26, 1, 9),
    _F3PtpPTPClockHistoryMaxSyncPathDelay_Type()
)
f3PtpPTPClockHistoryMaxSyncPathDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpPTPClockHistoryMaxSyncPathDelay.setStatus("current")
_F3PtpPTPClockHistoryAvgSyncPathDelay_Type = ScaledNanoseconds
_F3PtpPTPClockHistoryAvgSyncPathDelay_Object = MibTableColumn
f3PtpPTPClockHistoryAvgSyncPathDelay = _F3PtpPTPClockHistoryAvgSyncPathDelay_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 26, 1, 10),
    _F3PtpPTPClockHistoryAvgSyncPathDelay_Type()
)
f3PtpPTPClockHistoryAvgSyncPathDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpPTPClockHistoryAvgSyncPathDelay.setStatus("current")
_F3PtpPTPClockHistoryMinMeanPathDelay_Type = ScaledNanoseconds
_F3PtpPTPClockHistoryMinMeanPathDelay_Object = MibTableColumn
f3PtpPTPClockHistoryMinMeanPathDelay = _F3PtpPTPClockHistoryMinMeanPathDelay_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 26, 1, 11),
    _F3PtpPTPClockHistoryMinMeanPathDelay_Type()
)
f3PtpPTPClockHistoryMinMeanPathDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpPTPClockHistoryMinMeanPathDelay.setStatus("current")
_F3PtpPTPClockHistoryMaxMeanPathDelay_Type = ScaledNanoseconds
_F3PtpPTPClockHistoryMaxMeanPathDelay_Object = MibTableColumn
f3PtpPTPClockHistoryMaxMeanPathDelay = _F3PtpPTPClockHistoryMaxMeanPathDelay_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 26, 1, 12),
    _F3PtpPTPClockHistoryMaxMeanPathDelay_Type()
)
f3PtpPTPClockHistoryMaxMeanPathDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpPTPClockHistoryMaxMeanPathDelay.setStatus("current")
_F3PtpPTPClockHistoryAvgMeanPathDelay_Type = ScaledNanoseconds
_F3PtpPTPClockHistoryAvgMeanPathDelay_Object = MibTableColumn
f3PtpPTPClockHistoryAvgMeanPathDelay = _F3PtpPTPClockHistoryAvgMeanPathDelay_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 26, 1, 13),
    _F3PtpPTPClockHistoryAvgMeanPathDelay_Type()
)
f3PtpPTPClockHistoryAvgMeanPathDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpPTPClockHistoryAvgMeanPathDelay.setStatus("current")
_F3PtpPTPClockThresholdTable_Object = MibTable
f3PtpPTPClockThresholdTable = _F3PtpPTPClockThresholdTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 27)
)
if mibBuilder.loadTexts:
    f3PtpPTPClockThresholdTable.setStatus("current")
_F3PtpPTPClockThresholdEntry_Object = MibTableRow
f3PtpPTPClockThresholdEntry = _F3PtpPTPClockThresholdEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 27, 1)
)
f3PtpPTPClockThresholdEntry.setIndexNames(
    (0, "CM-ENTITY-MIB", "neIndex"),
    (0, "F3-PTP-MIB", "f3PtpPTPClockIndex"),
    (0, "F3-PTP-MIB", "f3PtpPTPClockStatsIndex"),
    (0, "F3-PTP-MIB", "f3PtpPTPClockThresholdIndex"),
)
if mibBuilder.loadTexts:
    f3PtpPTPClockThresholdEntry.setStatus("current")


class _F3PtpPTPClockThresholdIndex_Type(Integer32):
    """Custom type f3PtpPTPClockThresholdIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_F3PtpPTPClockThresholdIndex_Type.__name__ = "Integer32"
_F3PtpPTPClockThresholdIndex_Object = MibTableColumn
f3PtpPTPClockThresholdIndex = _F3PtpPTPClockThresholdIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 27, 1, 1),
    _F3PtpPTPClockThresholdIndex_Type()
)
f3PtpPTPClockThresholdIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    f3PtpPTPClockThresholdIndex.setStatus("current")
_F3PtpPTPClockThresholdInterval_Type = CmPmIntervalType
_F3PtpPTPClockThresholdInterval_Object = MibTableColumn
f3PtpPTPClockThresholdInterval = _F3PtpPTPClockThresholdInterval_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 27, 1, 2),
    _F3PtpPTPClockThresholdInterval_Type()
)
f3PtpPTPClockThresholdInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpPTPClockThresholdInterval.setStatus("current")
_F3PtpPTPClockThresholdVariable_Type = VariablePointer
_F3PtpPTPClockThresholdVariable_Object = MibTableColumn
f3PtpPTPClockThresholdVariable = _F3PtpPTPClockThresholdVariable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 27, 1, 3),
    _F3PtpPTPClockThresholdVariable_Type()
)
f3PtpPTPClockThresholdVariable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpPTPClockThresholdVariable.setStatus("current")
_F3PtpPTPClockThresholdValueLo_Type = Unsigned32
_F3PtpPTPClockThresholdValueLo_Object = MibTableColumn
f3PtpPTPClockThresholdValueLo = _F3PtpPTPClockThresholdValueLo_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 27, 1, 4),
    _F3PtpPTPClockThresholdValueLo_Type()
)
f3PtpPTPClockThresholdValueLo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3PtpPTPClockThresholdValueLo.setStatus("current")
_F3PtpPTPClockThresholdValueHi_Type = Unsigned32
_F3PtpPTPClockThresholdValueHi_Object = MibTableColumn
f3PtpPTPClockThresholdValueHi = _F3PtpPTPClockThresholdValueHi_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 27, 1, 5),
    _F3PtpPTPClockThresholdValueHi_Type()
)
f3PtpPTPClockThresholdValueHi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3PtpPTPClockThresholdValueHi.setStatus("current")
_F3PtpPTPClockThresholdMonValue_Type = PerfCounter64
_F3PtpPTPClockThresholdMonValue_Object = MibTableColumn
f3PtpPTPClockThresholdMonValue = _F3PtpPTPClockThresholdMonValue_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 27, 1, 6),
    _F3PtpPTPClockThresholdMonValue_Type()
)
f3PtpPTPClockThresholdMonValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpPTPClockThresholdMonValue.setStatus("current")
_F3PtpL3PTPPortStatsTable_Object = MibTable
f3PtpL3PTPPortStatsTable = _F3PtpL3PTPPortStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 28)
)
if mibBuilder.loadTexts:
    f3PtpL3PTPPortStatsTable.setStatus("current")
_F3PtpL3PTPPortStatsEntry_Object = MibTableRow
f3PtpL3PTPPortStatsEntry = _F3PtpL3PTPPortStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 28, 1)
)
f3PtpL3PTPPortStatsEntry.setIndexNames(
    (0, "CM-ENTITY-MIB", "neIndex"),
    (0, "F3-PTP-MIB", "f3PtpPTPClockIndex"),
    (0, "F3-PTP-MIB", "f3PtpL3PTPPortIndex"),
    (0, "F3-PTP-MIB", "f3PtpL3PTPPortStatsIndex"),
)
if mibBuilder.loadTexts:
    f3PtpL3PTPPortStatsEntry.setStatus("current")


class _F3PtpL3PTPPortStatsIndex_Type(Integer32):
    """Custom type f3PtpL3PTPPortStatsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_F3PtpL3PTPPortStatsIndex_Type.__name__ = "Integer32"
_F3PtpL3PTPPortStatsIndex_Object = MibTableColumn
f3PtpL3PTPPortStatsIndex = _F3PtpL3PTPPortStatsIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 28, 1, 1),
    _F3PtpL3PTPPortStatsIndex_Type()
)
f3PtpL3PTPPortStatsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    f3PtpL3PTPPortStatsIndex.setStatus("current")
_F3PtpL3PTPPortStatsIntervalType_Type = CmPmIntervalType
_F3PtpL3PTPPortStatsIntervalType_Object = MibTableColumn
f3PtpL3PTPPortStatsIntervalType = _F3PtpL3PTPPortStatsIntervalType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 28, 1, 2),
    _F3PtpL3PTPPortStatsIntervalType_Type()
)
f3PtpL3PTPPortStatsIntervalType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpL3PTPPortStatsIntervalType.setStatus("current")
_F3PtpL3PTPPortStatsValid_Type = TruthValue
_F3PtpL3PTPPortStatsValid_Object = MibTableColumn
f3PtpL3PTPPortStatsValid = _F3PtpL3PTPPortStatsValid_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 28, 1, 3),
    _F3PtpL3PTPPortStatsValid_Type()
)
f3PtpL3PTPPortStatsValid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpL3PTPPortStatsValid.setStatus("current")
_F3PtpL3PTPPortStatsAction_Type = CmPmBinAction
_F3PtpL3PTPPortStatsAction_Object = MibTableColumn
f3PtpL3PTPPortStatsAction = _F3PtpL3PTPPortStatsAction_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 28, 1, 4),
    _F3PtpL3PTPPortStatsAction_Type()
)
f3PtpL3PTPPortStatsAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3PtpL3PTPPortStatsAction.setStatus("current")
_F3PtpL3PTPPortStatsAvgAnnounceRate_Type = Unsigned32
_F3PtpL3PTPPortStatsAvgAnnounceRate_Object = MibTableColumn
f3PtpL3PTPPortStatsAvgAnnounceRate = _F3PtpL3PTPPortStatsAvgAnnounceRate_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 28, 1, 5),
    _F3PtpL3PTPPortStatsAvgAnnounceRate_Type()
)
f3PtpL3PTPPortStatsAvgAnnounceRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpL3PTPPortStatsAvgAnnounceRate.setStatus("current")
_F3PtpL3PTPPortStatsAvgSyncRate_Type = Unsigned32
_F3PtpL3PTPPortStatsAvgSyncRate_Object = MibTableColumn
f3PtpL3PTPPortStatsAvgSyncRate = _F3PtpL3PTPPortStatsAvgSyncRate_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 28, 1, 6),
    _F3PtpL3PTPPortStatsAvgSyncRate_Type()
)
f3PtpL3PTPPortStatsAvgSyncRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpL3PTPPortStatsAvgSyncRate.setStatus("current")
_F3PtpL3PTPPortStatsAvgDelayReqRate_Type = Unsigned32
_F3PtpL3PTPPortStatsAvgDelayReqRate_Object = MibTableColumn
f3PtpL3PTPPortStatsAvgDelayReqRate = _F3PtpL3PTPPortStatsAvgDelayReqRate_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 28, 1, 7),
    _F3PtpL3PTPPortStatsAvgDelayReqRate_Type()
)
f3PtpL3PTPPortStatsAvgDelayReqRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpL3PTPPortStatsAvgDelayReqRate.setStatus("current")
_F3PtpL3PTPPortStatsAvgDelayRespRate_Type = Unsigned32
_F3PtpL3PTPPortStatsAvgDelayRespRate_Object = MibTableColumn
f3PtpL3PTPPortStatsAvgDelayRespRate = _F3PtpL3PTPPortStatsAvgDelayRespRate_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 28, 1, 8),
    _F3PtpL3PTPPortStatsAvgDelayRespRate_Type()
)
f3PtpL3PTPPortStatsAvgDelayRespRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpL3PTPPortStatsAvgDelayRespRate.setStatus("current")
_F3PtpL3PTPPortStatsMismatchDomainDiscards_Type = PerfCounter64
_F3PtpL3PTPPortStatsMismatchDomainDiscards_Object = MibTableColumn
f3PtpL3PTPPortStatsMismatchDomainDiscards = _F3PtpL3PTPPortStatsMismatchDomainDiscards_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 28, 1, 9),
    _F3PtpL3PTPPortStatsMismatchDomainDiscards_Type()
)
f3PtpL3PTPPortStatsMismatchDomainDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpL3PTPPortStatsMismatchDomainDiscards.setStatus("current")
_F3PtpL3PTPPortStatsMessageWrongTypeDiscards_Type = PerfCounter64
_F3PtpL3PTPPortStatsMessageWrongTypeDiscards_Object = MibTableColumn
f3PtpL3PTPPortStatsMessageWrongTypeDiscards = _F3PtpL3PTPPortStatsMessageWrongTypeDiscards_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 28, 1, 10),
    _F3PtpL3PTPPortStatsMessageWrongTypeDiscards_Type()
)
f3PtpL3PTPPortStatsMessageWrongTypeDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpL3PTPPortStatsMessageWrongTypeDiscards.setStatus("current")
_F3PtpL3PTPPortStatsMessagesWrongLengthDiscards_Type = PerfCounter64
_F3PtpL3PTPPortStatsMessagesWrongLengthDiscards_Object = MibTableColumn
f3PtpL3PTPPortStatsMessagesWrongLengthDiscards = _F3PtpL3PTPPortStatsMessagesWrongLengthDiscards_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 28, 1, 11),
    _F3PtpL3PTPPortStatsMessagesWrongLengthDiscards_Type()
)
f3PtpL3PTPPortStatsMessagesWrongLengthDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpL3PTPPortStatsMessagesWrongLengthDiscards.setStatus("current")
_F3PtpL3PTPPortStatsUnknownMasterDiscards_Type = PerfCounter64
_F3PtpL3PTPPortStatsUnknownMasterDiscards_Object = MibTableColumn
f3PtpL3PTPPortStatsUnknownMasterDiscards = _F3PtpL3PTPPortStatsUnknownMasterDiscards_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 28, 1, 12),
    _F3PtpL3PTPPortStatsUnknownMasterDiscards_Type()
)
f3PtpL3PTPPortStatsUnknownMasterDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpL3PTPPortStatsUnknownMasterDiscards.setStatus("deprecated")
_F3PtpL3PTPPortStatsMinOffsetFromMaster_Type = PerfCounter64
_F3PtpL3PTPPortStatsMinOffsetFromMaster_Object = MibTableColumn
f3PtpL3PTPPortStatsMinOffsetFromMaster = _F3PtpL3PTPPortStatsMinOffsetFromMaster_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 28, 1, 13),
    _F3PtpL3PTPPortStatsMinOffsetFromMaster_Type()
)
f3PtpL3PTPPortStatsMinOffsetFromMaster.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpL3PTPPortStatsMinOffsetFromMaster.setStatus("current")
_F3PtpL3PTPPortStatsMaxOffsetFromMaster_Type = PerfCounter64
_F3PtpL3PTPPortStatsMaxOffsetFromMaster_Object = MibTableColumn
f3PtpL3PTPPortStatsMaxOffsetFromMaster = _F3PtpL3PTPPortStatsMaxOffsetFromMaster_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 28, 1, 14),
    _F3PtpL3PTPPortStatsMaxOffsetFromMaster_Type()
)
f3PtpL3PTPPortStatsMaxOffsetFromMaster.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpL3PTPPortStatsMaxOffsetFromMaster.setStatus("current")
_F3PtpL3PTPPortStatsAvgOffsetFromMaster_Type = PerfCounter64
_F3PtpL3PTPPortStatsAvgOffsetFromMaster_Object = MibTableColumn
f3PtpL3PTPPortStatsAvgOffsetFromMaster = _F3PtpL3PTPPortStatsAvgOffsetFromMaster_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 28, 1, 15),
    _F3PtpL3PTPPortStatsAvgOffsetFromMaster_Type()
)
f3PtpL3PTPPortStatsAvgOffsetFromMaster.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpL3PTPPortStatsAvgOffsetFromMaster.setStatus("current")
_F3PtpL3PTPPortStatsMinSyncPathDelay_Type = PerfCounter64
_F3PtpL3PTPPortStatsMinSyncPathDelay_Object = MibTableColumn
f3PtpL3PTPPortStatsMinSyncPathDelay = _F3PtpL3PTPPortStatsMinSyncPathDelay_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 28, 1, 16),
    _F3PtpL3PTPPortStatsMinSyncPathDelay_Type()
)
f3PtpL3PTPPortStatsMinSyncPathDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpL3PTPPortStatsMinSyncPathDelay.setStatus("current")
_F3PtpL3PTPPortStatsMaxSyncPathDelay_Type = PerfCounter64
_F3PtpL3PTPPortStatsMaxSyncPathDelay_Object = MibTableColumn
f3PtpL3PTPPortStatsMaxSyncPathDelay = _F3PtpL3PTPPortStatsMaxSyncPathDelay_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 28, 1, 17),
    _F3PtpL3PTPPortStatsMaxSyncPathDelay_Type()
)
f3PtpL3PTPPortStatsMaxSyncPathDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpL3PTPPortStatsMaxSyncPathDelay.setStatus("current")
_F3PtpL3PTPPortStatsAvgSyncPathDelay_Type = PerfCounter64
_F3PtpL3PTPPortStatsAvgSyncPathDelay_Object = MibTableColumn
f3PtpL3PTPPortStatsAvgSyncPathDelay = _F3PtpL3PTPPortStatsAvgSyncPathDelay_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 28, 1, 18),
    _F3PtpL3PTPPortStatsAvgSyncPathDelay_Type()
)
f3PtpL3PTPPortStatsAvgSyncPathDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpL3PTPPortStatsAvgSyncPathDelay.setStatus("current")
_F3PtpL3PTPPortStatsMinMeanPathDelay_Type = PerfCounter64
_F3PtpL3PTPPortStatsMinMeanPathDelay_Object = MibTableColumn
f3PtpL3PTPPortStatsMinMeanPathDelay = _F3PtpL3PTPPortStatsMinMeanPathDelay_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 28, 1, 19),
    _F3PtpL3PTPPortStatsMinMeanPathDelay_Type()
)
f3PtpL3PTPPortStatsMinMeanPathDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpL3PTPPortStatsMinMeanPathDelay.setStatus("current")
_F3PtpL3PTPPortStatsMaxMeanPathDelay_Type = PerfCounter64
_F3PtpL3PTPPortStatsMaxMeanPathDelay_Object = MibTableColumn
f3PtpL3PTPPortStatsMaxMeanPathDelay = _F3PtpL3PTPPortStatsMaxMeanPathDelay_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 28, 1, 20),
    _F3PtpL3PTPPortStatsMaxMeanPathDelay_Type()
)
f3PtpL3PTPPortStatsMaxMeanPathDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpL3PTPPortStatsMaxMeanPathDelay.setStatus("current")
_F3PtpL3PTPPortStatsAvgMeanPathDelay_Type = PerfCounter64
_F3PtpL3PTPPortStatsAvgMeanPathDelay_Object = MibTableColumn
f3PtpL3PTPPortStatsAvgMeanPathDelay = _F3PtpL3PTPPortStatsAvgMeanPathDelay_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 28, 1, 21),
    _F3PtpL3PTPPortStatsAvgMeanPathDelay_Type()
)
f3PtpL3PTPPortStatsAvgMeanPathDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpL3PTPPortStatsAvgMeanPathDelay.setStatus("current")
_F3PtpL3PTPPortStatsMsgMiscDiscards_Type = PerfCounter64
_F3PtpL3PTPPortStatsMsgMiscDiscards_Object = MibTableColumn
f3PtpL3PTPPortStatsMsgMiscDiscards = _F3PtpL3PTPPortStatsMsgMiscDiscards_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 28, 1, 22),
    _F3PtpL3PTPPortStatsMsgMiscDiscards_Type()
)
f3PtpL3PTPPortStatsMsgMiscDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpL3PTPPortStatsMsgMiscDiscards.setStatus("deprecated")
_F3PtpL3PTPPortHistoryTable_Object = MibTable
f3PtpL3PTPPortHistoryTable = _F3PtpL3PTPPortHistoryTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 29)
)
if mibBuilder.loadTexts:
    f3PtpL3PTPPortHistoryTable.setStatus("current")
_F3PtpL3PTPPortHistoryEntry_Object = MibTableRow
f3PtpL3PTPPortHistoryEntry = _F3PtpL3PTPPortHistoryEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 29, 1)
)
f3PtpL3PTPPortHistoryEntry.setIndexNames(
    (0, "CM-ENTITY-MIB", "neIndex"),
    (0, "F3-PTP-MIB", "f3PtpPTPClockIndex"),
    (0, "F3-PTP-MIB", "f3PtpL3PTPPortIndex"),
    (0, "F3-PTP-MIB", "f3PtpL3PTPPortStatsIndex"),
    (0, "F3-PTP-MIB", "f3PtpL3PTPPortHistoryIndex"),
)
if mibBuilder.loadTexts:
    f3PtpL3PTPPortHistoryEntry.setStatus("current")


class _F3PtpL3PTPPortHistoryIndex_Type(Integer32):
    """Custom type f3PtpL3PTPPortHistoryIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_F3PtpL3PTPPortHistoryIndex_Type.__name__ = "Integer32"
_F3PtpL3PTPPortHistoryIndex_Object = MibTableColumn
f3PtpL3PTPPortHistoryIndex = _F3PtpL3PTPPortHistoryIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 29, 1, 1),
    _F3PtpL3PTPPortHistoryIndex_Type()
)
f3PtpL3PTPPortHistoryIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    f3PtpL3PTPPortHistoryIndex.setStatus("current")
_F3PtpL3PTPPortHistoryTime_Type = DateAndTime
_F3PtpL3PTPPortHistoryTime_Object = MibTableColumn
f3PtpL3PTPPortHistoryTime = _F3PtpL3PTPPortHistoryTime_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 29, 1, 2),
    _F3PtpL3PTPPortHistoryTime_Type()
)
f3PtpL3PTPPortHistoryTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpL3PTPPortHistoryTime.setStatus("current")
_F3PtpL3PTPPortHistoryValid_Type = TruthValue
_F3PtpL3PTPPortHistoryValid_Object = MibTableColumn
f3PtpL3PTPPortHistoryValid = _F3PtpL3PTPPortHistoryValid_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 29, 1, 3),
    _F3PtpL3PTPPortHistoryValid_Type()
)
f3PtpL3PTPPortHistoryValid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpL3PTPPortHistoryValid.setStatus("current")
_F3PtpL3PTPPortHistoryAction_Type = CmPmBinAction
_F3PtpL3PTPPortHistoryAction_Object = MibTableColumn
f3PtpL3PTPPortHistoryAction = _F3PtpL3PTPPortHistoryAction_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 29, 1, 4),
    _F3PtpL3PTPPortHistoryAction_Type()
)
f3PtpL3PTPPortHistoryAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3PtpL3PTPPortHistoryAction.setStatus("current")
_F3PtpL3PTPPortHistoryAvgAnnounceRate_Type = Unsigned32
_F3PtpL3PTPPortHistoryAvgAnnounceRate_Object = MibTableColumn
f3PtpL3PTPPortHistoryAvgAnnounceRate = _F3PtpL3PTPPortHistoryAvgAnnounceRate_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 29, 1, 5),
    _F3PtpL3PTPPortHistoryAvgAnnounceRate_Type()
)
f3PtpL3PTPPortHistoryAvgAnnounceRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpL3PTPPortHistoryAvgAnnounceRate.setStatus("current")
_F3PtpL3PTPPortHistoryAvgSyncRate_Type = Unsigned32
_F3PtpL3PTPPortHistoryAvgSyncRate_Object = MibTableColumn
f3PtpL3PTPPortHistoryAvgSyncRate = _F3PtpL3PTPPortHistoryAvgSyncRate_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 29, 1, 6),
    _F3PtpL3PTPPortHistoryAvgSyncRate_Type()
)
f3PtpL3PTPPortHistoryAvgSyncRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpL3PTPPortHistoryAvgSyncRate.setStatus("current")
_F3PtpL3PTPPortHistoryAvgDelayReqRate_Type = Unsigned32
_F3PtpL3PTPPortHistoryAvgDelayReqRate_Object = MibTableColumn
f3PtpL3PTPPortHistoryAvgDelayReqRate = _F3PtpL3PTPPortHistoryAvgDelayReqRate_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 29, 1, 7),
    _F3PtpL3PTPPortHistoryAvgDelayReqRate_Type()
)
f3PtpL3PTPPortHistoryAvgDelayReqRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpL3PTPPortHistoryAvgDelayReqRate.setStatus("current")
_F3PtpL3PTPPortHistoryAvgDelayRespRate_Type = Unsigned32
_F3PtpL3PTPPortHistoryAvgDelayRespRate_Object = MibTableColumn
f3PtpL3PTPPortHistoryAvgDelayRespRate = _F3PtpL3PTPPortHistoryAvgDelayRespRate_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 29, 1, 8),
    _F3PtpL3PTPPortHistoryAvgDelayRespRate_Type()
)
f3PtpL3PTPPortHistoryAvgDelayRespRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpL3PTPPortHistoryAvgDelayRespRate.setStatus("current")
_F3PtpL3PTPPortHistoryMismatchDomainDiscards_Type = PerfCounter64
_F3PtpL3PTPPortHistoryMismatchDomainDiscards_Object = MibTableColumn
f3PtpL3PTPPortHistoryMismatchDomainDiscards = _F3PtpL3PTPPortHistoryMismatchDomainDiscards_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 29, 1, 9),
    _F3PtpL3PTPPortHistoryMismatchDomainDiscards_Type()
)
f3PtpL3PTPPortHistoryMismatchDomainDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpL3PTPPortHistoryMismatchDomainDiscards.setStatus("current")
_F3PtpL3PTPPortHistoryMessageWrongTypeDiscards_Type = PerfCounter64
_F3PtpL3PTPPortHistoryMessageWrongTypeDiscards_Object = MibTableColumn
f3PtpL3PTPPortHistoryMessageWrongTypeDiscards = _F3PtpL3PTPPortHistoryMessageWrongTypeDiscards_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 29, 1, 10),
    _F3PtpL3PTPPortHistoryMessageWrongTypeDiscards_Type()
)
f3PtpL3PTPPortHistoryMessageWrongTypeDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpL3PTPPortHistoryMessageWrongTypeDiscards.setStatus("current")
_F3PtpL3PTPPortHistoryMessagesWrongLengthDiscards_Type = PerfCounter64
_F3PtpL3PTPPortHistoryMessagesWrongLengthDiscards_Object = MibTableColumn
f3PtpL3PTPPortHistoryMessagesWrongLengthDiscards = _F3PtpL3PTPPortHistoryMessagesWrongLengthDiscards_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 29, 1, 11),
    _F3PtpL3PTPPortHistoryMessagesWrongLengthDiscards_Type()
)
f3PtpL3PTPPortHistoryMessagesWrongLengthDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpL3PTPPortHistoryMessagesWrongLengthDiscards.setStatus("current")
_F3PtpL3PTPPortHistoryUnknownMasterDiscards_Type = PerfCounter64
_F3PtpL3PTPPortHistoryUnknownMasterDiscards_Object = MibTableColumn
f3PtpL3PTPPortHistoryUnknownMasterDiscards = _F3PtpL3PTPPortHistoryUnknownMasterDiscards_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 29, 1, 12),
    _F3PtpL3PTPPortHistoryUnknownMasterDiscards_Type()
)
f3PtpL3PTPPortHistoryUnknownMasterDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpL3PTPPortHistoryUnknownMasterDiscards.setStatus("deprecated")
_F3PtpL3PTPPortHistoryMinOffsetFromMaster_Type = PerfCounter64
_F3PtpL3PTPPortHistoryMinOffsetFromMaster_Object = MibTableColumn
f3PtpL3PTPPortHistoryMinOffsetFromMaster = _F3PtpL3PTPPortHistoryMinOffsetFromMaster_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 29, 1, 13),
    _F3PtpL3PTPPortHistoryMinOffsetFromMaster_Type()
)
f3PtpL3PTPPortHistoryMinOffsetFromMaster.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpL3PTPPortHistoryMinOffsetFromMaster.setStatus("current")
_F3PtpL3PTPPortHistoryMaxOffsetFromMaster_Type = PerfCounter64
_F3PtpL3PTPPortHistoryMaxOffsetFromMaster_Object = MibTableColumn
f3PtpL3PTPPortHistoryMaxOffsetFromMaster = _F3PtpL3PTPPortHistoryMaxOffsetFromMaster_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 29, 1, 14),
    _F3PtpL3PTPPortHistoryMaxOffsetFromMaster_Type()
)
f3PtpL3PTPPortHistoryMaxOffsetFromMaster.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpL3PTPPortHistoryMaxOffsetFromMaster.setStatus("current")
_F3PtpL3PTPPortHistoryAvgOffsetFromMaster_Type = PerfCounter64
_F3PtpL3PTPPortHistoryAvgOffsetFromMaster_Object = MibTableColumn
f3PtpL3PTPPortHistoryAvgOffsetFromMaster = _F3PtpL3PTPPortHistoryAvgOffsetFromMaster_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 29, 1, 15),
    _F3PtpL3PTPPortHistoryAvgOffsetFromMaster_Type()
)
f3PtpL3PTPPortHistoryAvgOffsetFromMaster.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpL3PTPPortHistoryAvgOffsetFromMaster.setStatus("current")
_F3PtpL3PTPPortHistoryMinSyncPathDelay_Type = PerfCounter64
_F3PtpL3PTPPortHistoryMinSyncPathDelay_Object = MibTableColumn
f3PtpL3PTPPortHistoryMinSyncPathDelay = _F3PtpL3PTPPortHistoryMinSyncPathDelay_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 29, 1, 16),
    _F3PtpL3PTPPortHistoryMinSyncPathDelay_Type()
)
f3PtpL3PTPPortHistoryMinSyncPathDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpL3PTPPortHistoryMinSyncPathDelay.setStatus("current")
_F3PtpL3PTPPortHistoryMaxSyncPathDelay_Type = PerfCounter64
_F3PtpL3PTPPortHistoryMaxSyncPathDelay_Object = MibTableColumn
f3PtpL3PTPPortHistoryMaxSyncPathDelay = _F3PtpL3PTPPortHistoryMaxSyncPathDelay_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 29, 1, 17),
    _F3PtpL3PTPPortHistoryMaxSyncPathDelay_Type()
)
f3PtpL3PTPPortHistoryMaxSyncPathDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpL3PTPPortHistoryMaxSyncPathDelay.setStatus("current")
_F3PtpL3PTPPortHistoryAvgSyncPathDelay_Type = PerfCounter64
_F3PtpL3PTPPortHistoryAvgSyncPathDelay_Object = MibTableColumn
f3PtpL3PTPPortHistoryAvgSyncPathDelay = _F3PtpL3PTPPortHistoryAvgSyncPathDelay_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 29, 1, 18),
    _F3PtpL3PTPPortHistoryAvgSyncPathDelay_Type()
)
f3PtpL3PTPPortHistoryAvgSyncPathDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpL3PTPPortHistoryAvgSyncPathDelay.setStatus("current")
_F3PtpL3PTPPortHistoryMinMeanPathDelay_Type = PerfCounter64
_F3PtpL3PTPPortHistoryMinMeanPathDelay_Object = MibTableColumn
f3PtpL3PTPPortHistoryMinMeanPathDelay = _F3PtpL3PTPPortHistoryMinMeanPathDelay_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 29, 1, 19),
    _F3PtpL3PTPPortHistoryMinMeanPathDelay_Type()
)
f3PtpL3PTPPortHistoryMinMeanPathDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpL3PTPPortHistoryMinMeanPathDelay.setStatus("current")
_F3PtpL3PTPPortHistoryMaxMeanPathDelay_Type = PerfCounter64
_F3PtpL3PTPPortHistoryMaxMeanPathDelay_Object = MibTableColumn
f3PtpL3PTPPortHistoryMaxMeanPathDelay = _F3PtpL3PTPPortHistoryMaxMeanPathDelay_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 29, 1, 20),
    _F3PtpL3PTPPortHistoryMaxMeanPathDelay_Type()
)
f3PtpL3PTPPortHistoryMaxMeanPathDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpL3PTPPortHistoryMaxMeanPathDelay.setStatus("current")
_F3PtpL3PTPPortHistoryAvgMeanPathDelay_Type = PerfCounter64
_F3PtpL3PTPPortHistoryAvgMeanPathDelay_Object = MibTableColumn
f3PtpL3PTPPortHistoryAvgMeanPathDelay = _F3PtpL3PTPPortHistoryAvgMeanPathDelay_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 29, 1, 21),
    _F3PtpL3PTPPortHistoryAvgMeanPathDelay_Type()
)
f3PtpL3PTPPortHistoryAvgMeanPathDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpL3PTPPortHistoryAvgMeanPathDelay.setStatus("current")
_F3PtpL3PTPPortHistoryMsgMiscDiscards_Type = PerfCounter64
_F3PtpL3PTPPortHistoryMsgMiscDiscards_Object = MibTableColumn
f3PtpL3PTPPortHistoryMsgMiscDiscards = _F3PtpL3PTPPortHistoryMsgMiscDiscards_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 29, 1, 22),
    _F3PtpL3PTPPortHistoryMsgMiscDiscards_Type()
)
f3PtpL3PTPPortHistoryMsgMiscDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpL3PTPPortHistoryMsgMiscDiscards.setStatus("deprecated")
_F3PtpL3PTPPortThresholdTable_Object = MibTable
f3PtpL3PTPPortThresholdTable = _F3PtpL3PTPPortThresholdTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 30)
)
if mibBuilder.loadTexts:
    f3PtpL3PTPPortThresholdTable.setStatus("current")
_F3PtpL3PTPPortThresholdEntry_Object = MibTableRow
f3PtpL3PTPPortThresholdEntry = _F3PtpL3PTPPortThresholdEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 30, 1)
)
f3PtpL3PTPPortThresholdEntry.setIndexNames(
    (0, "CM-ENTITY-MIB", "neIndex"),
    (0, "F3-PTP-MIB", "f3PtpPTPClockIndex"),
    (0, "F3-PTP-MIB", "f3PtpL3PTPPortIndex"),
    (0, "F3-PTP-MIB", "f3PtpL3PTPPortStatsIndex"),
    (0, "F3-PTP-MIB", "f3PtpL3PTPPortThresholdIndex"),
)
if mibBuilder.loadTexts:
    f3PtpL3PTPPortThresholdEntry.setStatus("current")


class _F3PtpL3PTPPortThresholdIndex_Type(Integer32):
    """Custom type f3PtpL3PTPPortThresholdIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_F3PtpL3PTPPortThresholdIndex_Type.__name__ = "Integer32"
_F3PtpL3PTPPortThresholdIndex_Object = MibTableColumn
f3PtpL3PTPPortThresholdIndex = _F3PtpL3PTPPortThresholdIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 30, 1, 1),
    _F3PtpL3PTPPortThresholdIndex_Type()
)
f3PtpL3PTPPortThresholdIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    f3PtpL3PTPPortThresholdIndex.setStatus("current")
_F3PtpL3PTPPortThresholdInterval_Type = CmPmIntervalType
_F3PtpL3PTPPortThresholdInterval_Object = MibTableColumn
f3PtpL3PTPPortThresholdInterval = _F3PtpL3PTPPortThresholdInterval_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 30, 1, 2),
    _F3PtpL3PTPPortThresholdInterval_Type()
)
f3PtpL3PTPPortThresholdInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpL3PTPPortThresholdInterval.setStatus("current")
_F3PtpL3PTPPortThresholdVariable_Type = VariablePointer
_F3PtpL3PTPPortThresholdVariable_Object = MibTableColumn
f3PtpL3PTPPortThresholdVariable = _F3PtpL3PTPPortThresholdVariable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 30, 1, 3),
    _F3PtpL3PTPPortThresholdVariable_Type()
)
f3PtpL3PTPPortThresholdVariable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpL3PTPPortThresholdVariable.setStatus("current")
_F3PtpL3PTPPortThresholdValueLo_Type = Unsigned32
_F3PtpL3PTPPortThresholdValueLo_Object = MibTableColumn
f3PtpL3PTPPortThresholdValueLo = _F3PtpL3PTPPortThresholdValueLo_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 30, 1, 4),
    _F3PtpL3PTPPortThresholdValueLo_Type()
)
f3PtpL3PTPPortThresholdValueLo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3PtpL3PTPPortThresholdValueLo.setStatus("current")
_F3PtpL3PTPPortThresholdValueHi_Type = Unsigned32
_F3PtpL3PTPPortThresholdValueHi_Object = MibTableColumn
f3PtpL3PTPPortThresholdValueHi = _F3PtpL3PTPPortThresholdValueHi_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 30, 1, 5),
    _F3PtpL3PTPPortThresholdValueHi_Type()
)
f3PtpL3PTPPortThresholdValueHi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3PtpL3PTPPortThresholdValueHi.setStatus("current")
_F3PtpL3PTPPortThresholdMonValue_Type = PerfCounter64
_F3PtpL3PTPPortThresholdMonValue_Object = MibTableColumn
f3PtpL3PTPPortThresholdMonValue = _F3PtpL3PTPPortThresholdMonValue_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 2, 30, 1, 6),
    _F3PtpL3PTPPortThresholdMonValue_Type()
)
f3PtpL3PTPPortThresholdMonValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PtpL3PTPPortThresholdMonValue.setStatus("current")
_F3PtpPerformanceNotifications_ObjectIdentity = ObjectIdentity
f3PtpPerformanceNotifications = _F3PtpPerformanceNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 3)
)
_F3PtpConformance_ObjectIdentity = ObjectIdentity
f3PtpConformance = _F3PtpConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 4)
)
_F3PtpCompliances_ObjectIdentity = ObjectIdentity
f3PtpCompliances = _F3PtpCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 4, 1)
)
_F3PtpGroups_ObjectIdentity = ObjectIdentity
f3PtpGroups = _F3PtpGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 4, 2)
)
_F3PtpStatusChangeNotifications_ObjectIdentity = ObjectIdentity
f3PtpStatusChangeNotifications = _F3PtpStatusChangeNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 5)
)
cmEthernetAccPortEntry.registerAugmentions(
    ("F3-PTP-MIB",
     "f3PtpEthernetAccPortExtEntry")
)
f3PtpEthernetAccPortExtEntry.setIndexNames(*cmEthernetAccPortEntry.getIndexNames())
cmEthernetNetPortEntry.registerAugmentions(
    ("F3-PTP-MIB",
     "f3PtpEthernetNetPortExtEntry")
)
f3PtpEthernetNetPortExtEntry.setIndexNames(*cmEthernetNetPortEntry.getIndexNames())
cmEthernetTrafficPortEntry.registerAugmentions(
    ("F3-PTP-MIB",
     "f3PtpEthernetTrafficPortExtEntry")
)
f3PtpEthernetTrafficPortExtEntry.setIndexNames(*cmEthernetTrafficPortEntry.getIndexNames())
f3PtpTrafficPortFlowPointEntry.registerAugmentions(
    ("F3-PTP-MIB",
     "f3PtpTrafficPortFlowPointExtEntry")
)
f3PtpTrafficPortFlowPointExtEntry.setIndexNames(*f3PtpTrafficPortFlowPointEntry.getIndexNames())

# Managed Objects groups

f3PtpObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 4, 2, 1)
)
f3PtpObjectGroup.setObjects(
      *(("F3-PTP-MIB", "f3PtpTCIndex"),
        ("F3-PTP-MIB", "f3PtpTCAlias"),
        ("F3-PTP-MIB", "f3PtpTCAdminState"),
        ("F3-PTP-MIB", "f3PtpTCOperationalState"),
        ("F3-PTP-MIB", "f3PtpTCSecondaryState"),
        ("F3-PTP-MIB", "f3PtpTCServiceFlow"),
        ("F3-PTP-MIB", "f3PtpTCDelayMechanism"),
        ("F3-PTP-MIB", "f3PtpTCSync"),
        ("F3-PTP-MIB", "f3PtpTCClockIdentity"),
        ("F3-PTP-MIB", "f3PtpTCStorageType"),
        ("F3-PTP-MIB", "f3PtpTCRowStatus"),
        ("F3-PTP-MIB", "f3PtpTCPtpProfile"),
        ("F3-PTP-MIB", "f3PtpTCVirtualPortIndex"),
        ("F3-PTP-MIB", "f3PtpTCVirtualPortAlias"),
        ("F3-PTP-MIB", "f3PtpTCVirtualPortAdminState"),
        ("F3-PTP-MIB", "f3PtpTCVirtualPortOperationalState"),
        ("F3-PTP-MIB", "f3PtpTCVirtualPortSecondaryState"),
        ("F3-PTP-MIB", "f3PtpTCVirtualPortIdentity"),
        ("F3-PTP-MIB", "f3PtpTCVirtualPortFlowPoint"),
        ("F3-PTP-MIB", "f3PtpTCVirtualPortStorageType"),
        ("F3-PTP-MIB", "f3PtpTCVirtualPortRowStatus"),
        ("F3-PTP-MIB", "f3PtpTSIndex"),
        ("F3-PTP-MIB", "f3PtpTSAlias"),
        ("F3-PTP-MIB", "f3PtpTSAdminState"),
        ("F3-PTP-MIB", "f3PtpTSOperationalState"),
        ("F3-PTP-MIB", "f3PtpTSSecondaryState"),
        ("F3-PTP-MIB", "f3PtpTSClockIdentity"),
        ("F3-PTP-MIB", "f3PtpTSDomainNumber"),
        ("F3-PTP-MIB", "f3PtpTSSync"),
        ("F3-PTP-MIB", "f3PtpTSCurrentTOD"),
        ("F3-PTP-MIB", "f3PtpTSSelectedPacketClock"),
        ("F3-PTP-MIB", "f3PtpTSClockRecoveryMode"),
        ("F3-PTP-MIB", "f3PtpTSClockRecoveryState"),
        ("F3-PTP-MIB", "f3PtpTSClockSyncEEnabled"),
        ("F3-PTP-MIB", "f3PtpTSClockQLModeEnabled"),
        ("F3-PTP-MIB", "f3PtpTSClockExpectedQL"),
        ("F3-PTP-MIB", "f3PtpTSClockAssumedQL"),
        ("F3-PTP-MIB", "f3PtpTSClockReceivedQL"),
        ("F3-PTP-MIB", "f3PtpTSStorageType"),
        ("F3-PTP-MIB", "f3PtpTSRowStatus"),
        ("F3-PTP-MIB", "f3PtpTSTimeTraceabilityStatus"),
        ("F3-PTP-MIB", "f3PtpTSTimeSinceTimeTraceabilityChanged"),
        ("F3-PTP-MIB", "f3PtpTSFreqTraceabilityStatus"),
        ("F3-PTP-MIB", "f3PtpTSTimeSinceFreqTraceabilityChanged"),
        ("F3-PTP-MIB", "f3PtpTSFreqRecoveryTarget"),
        ("F3-PTP-MIB", "f3PtpTSCurrentCRScore"),
        ("F3-PTP-MIB", "f3PtpTSTimeLastCRScore"),
        ("F3-PTP-MIB", "f3PtpTSTargetPhaseRecoveryAccuracy"),
        ("F3-PTP-MIB", "f3PtpTSCurrentPRScore"),
        ("F3-PTP-MIB", "f3PtpTSTimeLastPRScore"),
        ("F3-PTP-MIB", "f3PtpTSClockClass"),
        ("F3-PTP-MIB", "f3PtpTSClockAccuracy"),
        ("F3-PTP-MIB", "f3PtpTSTimeSource"),
        ("F3-PTP-MIB", "f3PtpTSPhaseRecoveryState"),
        ("F3-PTP-MIB", "f3PtpTSTimeHoldoverAccuracy"),
        ("F3-PTP-MIB", "f3PtpSOOCIndex"),
        ("F3-PTP-MIB", "f3PtpSOOCName"),
        ("F3-PTP-MIB", "f3PtpSOOCAlias"),
        ("F3-PTP-MIB", "f3PtpSOOCAdminState"),
        ("F3-PTP-MIB", "f3PtpSOOCOperationalState"),
        ("F3-PTP-MIB", "f3PtpSOOCSecondaryState"),
        ("F3-PTP-MIB", "f3PtpSOOCServiceFlow"),
        ("F3-PTP-MIB", "f3PtpSOOCMasterClockType"),
        ("F3-PTP-MIB", "f3PtpSOOCUnicastMessageNegEnabled"),
        ("F3-PTP-MIB", "f3PtpSOOCMasterDelayMechanism"),
        ("F3-PTP-MIB", "f3PtpSOOCMasterPriority"),
        ("F3-PTP-MIB", "f3PtpSOOCMasterIpProtocol"),
        ("F3-PTP-MIB", "f3PtpSOOCSlaveIpV4Address"),
        ("F3-PTP-MIB", "f3PtpSOOCSlaveIpV4SubnetMask"),
        ("F3-PTP-MIB", "f3PtpSOOCMasterIpV4Address"),
        ("F3-PTP-MIB", "f3PtpSOOCIpPriorityMapMode"),
        ("F3-PTP-MIB", "f3PtpSOOCIpPriority"),
        ("F3-PTP-MIB", "f3PtpSOOCMasterLeaseDuration"),
        ("F3-PTP-MIB", "f3PtpSOOCMasterAnnounceMsgRate"),
        ("F3-PTP-MIB", "f3PtpSOOCMasterAnnounceMsgReceiptTimeout"),
        ("F3-PTP-MIB", "f3PtpSOOCMasterSyncMsgRate"),
        ("F3-PTP-MIB", "f3PtpSOOCMasterSyncReceiptTimeout"),
        ("F3-PTP-MIB", "f3PtpSOOCMasterDelayRspMsgRate"),
        ("F3-PTP-MIB", "f3PtpSOOCMasterDelayRspReceiptTimeout"),
        ("F3-PTP-MIB", "f3PtpSOOCMasterRequestUnicastTimeout"),
        ("F3-PTP-MIB", "f3PtpSOOCMasterRequestUnicastRestartTimer"),
        ("F3-PTP-MIB", "f3PtpSOOCCurrentOffsetFromMaster"),
        ("F3-PTP-MIB", "f3PtpSOOCAnnounceMsgClockClass"),
        ("F3-PTP-MIB", "f3PtpSOOCLastReceivedAnnounceMsg"),
        ("F3-PTP-MIB", "f3PtpSOOCLastReceivedSyncMsg"),
        ("F3-PTP-MIB", "f3PtpSOOCLastReceivedDelayRspMsg"),
        ("F3-PTP-MIB", "f3PtpSOOCRecentMeanPathDelay"),
        ("F3-PTP-MIB", "f3PtpSOOCRecentSyncPDV"),
        ("F3-PTP-MIB", "f3PtpSOOCStorageType"),
        ("F3-PTP-MIB", "f3PtpSOOCRowStatus"),
        ("F3-PTP-MIB", "f3PtpSOOCRecentSyncPathDelay"),
        ("F3-PTP-MIB", "f3PtpSOOCSoocProtectionState"),
        ("F3-PTP-MIB", "f3PtpSOOCSoocWtr"),
        ("F3-PTP-MIB", "f3PtpSOOCSoocClockClass"),
        ("F3-PTP-MIB", "f3PtpSOOCSoocClockRecoveryState"),
        ("F3-PTP-MIB", "f3PtpSOOCSoocPhaseRecoveryState"),
        ("F3-PTP-MIB", "f3PtpSOOCE2eDelayAsymmetryComp"),
        ("F3-PTP-MIB", "f3PtpSOOCE2eAutoAsymmetryCompStatus"),
        ("F3-PTP-MIB", "f3PtpSOOCE2eDelayAsymmetry"),
        ("F3-PTP-MIB", "f3PtpSOOCSoocLockOutControl"),
        ("F3-PTP-MIB", "f3PtpSOOCSlaveIpV6Address"),
        ("F3-PTP-MIB", "f3PtpSOOCSlaveIpV6AddrPrefixLength"),
        ("F3-PTP-MIB", "f3PtpSOOCMasterIpV6Address"),
        ("F3-PTP-MIB", "f3PtpSOOCMinimumExpectedClockClass"),
        ("F3-PTP-MIB", "f3PtpSOOCMasterMessageMode"),
        ("F3-PTP-MIB", "f3PtpSOOCDefaultGatewayControl"),
        ("F3-PTP-MIB", "f3PtpSOOCGateway"),
        ("F3-PTP-MIB", "f3PtpSOOCIpV6Gateway"),
        ("F3-PTP-MIB", "f3PtpSOOCAlgorithmPtpAware"),
        ("F3-PTP-MIB", "f3PtpOCSlaveVirtualPortIndex"),
        ("F3-PTP-MIB", "f3PtpOCSlaveVirtualPortAlias"),
        ("F3-PTP-MIB", "f3PtpOCSlaveVirtualPortAdminState"),
        ("F3-PTP-MIB", "f3PtpOCSlaveVirtualPortOperationalState"),
        ("F3-PTP-MIB", "f3PtpOCSlaveVirtualPortSecondaryState"),
        ("F3-PTP-MIB", "f3PtpOCSlaveVirtualPortIdentity"),
        ("F3-PTP-MIB", "f3PtpOCSlaveVirtualPortFlowPoint"),
        ("F3-PTP-MIB", "f3PtpOCSlaveVirtualPortState"),
        ("F3-PTP-MIB", "f3PtpOCSlaveVirtualPortStorageType"),
        ("F3-PTP-MIB", "f3PtpOCSlaveVirtualPortRowStatus"),
        ("F3-PTP-MIB", "f3PtpAccPortFlowPointIndex"),
        ("F3-PTP-MIB", "f3PtpAccPortFlowPointAlias"),
        ("F3-PTP-MIB", "f3PtpAccPortFlowPointAdminState"),
        ("F3-PTP-MIB", "f3PtpAccPortFlowPointOperationalState"),
        ("F3-PTP-MIB", "f3PtpAccPortFlowPointSecondaryState"),
        ("F3-PTP-MIB", "f3PtpAccPortFlowPointType"),
        ("F3-PTP-MIB", "f3PtpAccPortFlowPointClock"),
        ("F3-PTP-MIB", "f3PtpAccPortFlowPointService"),
        ("F3-PTP-MIB", "f3PtpAccPortFlowPointOuterVlanEtherType"),
        ("F3-PTP-MIB", "f3PtpAccPortFlowPointOuterVlanMemberList"),
        ("F3-PTP-MIB", "f3PtpAccPortFlowPointOuterUntaggedEnabled"),
        ("F3-PTP-MIB", "f3PtpAccPortFlowPointInner1VlanEtherType"),
        ("F3-PTP-MIB", "f3PtpAccPortFlowPointInner1VlanMemberList"),
        ("F3-PTP-MIB", "f3PtpAccPortFlowPointInner1UntaggedEnabled"),
        ("F3-PTP-MIB", "f3PtpAccPortFlowPointInner2VlanEtherType"),
        ("F3-PTP-MIB", "f3PtpAccPortFlowPointInner2VlanMemberList"),
        ("F3-PTP-MIB", "f3PtpAccPortFlowPointInner2UntaggedEnabled"),
        ("F3-PTP-MIB", "f3PtpAccPortFlowPointStorageType"),
        ("F3-PTP-MIB", "f3PtpAccPortFlowPointRowStatus"),
        ("F3-PTP-MIB", "f3PtpAccPortFlowPointCOS"),
        ("F3-PTP-MIB", "f3PtpAccPortFlowPointCIRLo"),
        ("F3-PTP-MIB", "f3PtpAccPortFlowPointCIRHi"),
        ("F3-PTP-MIB", "f3PtpAccPortFlowPointEIRLo"),
        ("F3-PTP-MIB", "f3PtpAccPortFlowPointEIRHi"),
        ("F3-PTP-MIB", "f3PtpAccPortFlowPointBufferSize"),
        ("F3-PTP-MIB", "f3PtpAccPortFlowPointLoopAvoidance"),
        ("F3-PTP-MIB", "f3PtpAccPortFlowPointRefConnectGuardFlow"),
        ("F3-PTP-MIB", "f3PtpAccPortFlowPointSecureState"),
        ("F3-PTP-MIB", "f3PtpAccPortFlowPointSecureBlockingEnabled"),
        ("F3-PTP-MIB", "f3PtpNetPortFlowPointIndex"),
        ("F3-PTP-MIB", "f3PtpNetPortFlowPointAlias"),
        ("F3-PTP-MIB", "f3PtpNetPortFlowPointAdminState"),
        ("F3-PTP-MIB", "f3PtpNetPortFlowPointOperationalState"),
        ("F3-PTP-MIB", "f3PtpNetPortFlowPointSecondaryState"),
        ("F3-PTP-MIB", "f3PtpNetPortFlowPointType"),
        ("F3-PTP-MIB", "f3PtpNetPortFlowPointClock"),
        ("F3-PTP-MIB", "f3PtpNetPortFlowPointService"),
        ("F3-PTP-MIB", "f3PtpNetPortFlowPointOuterVlanEtherType"),
        ("F3-PTP-MIB", "f3PtpNetPortFlowPointOuterVlanMemberList"),
        ("F3-PTP-MIB", "f3PtpNetPortFlowPointOuterUntaggedEnabled"),
        ("F3-PTP-MIB", "f3PtpNetPortFlowPointInner1VlanEtherType"),
        ("F3-PTP-MIB", "f3PtpNetPortFlowPointInner1VlanMemberList"),
        ("F3-PTP-MIB", "f3PtpNetPortFlowPointInner1UntaggedEnabled"),
        ("F3-PTP-MIB", "f3PtpNetPortFlowPointInner2VlanEtherType"),
        ("F3-PTP-MIB", "f3PtpNetPortFlowPointInner2VlanMemberList"),
        ("F3-PTP-MIB", "f3PtpNetPortFlowPointInner2UntaggedEnabled"),
        ("F3-PTP-MIB", "f3PtpNetPortFlowPointStorageType"),
        ("F3-PTP-MIB", "f3PtpNetPortFlowPointRowStatus"),
        ("F3-PTP-MIB", "f3PtpNetPortFlowPointCOS"),
        ("F3-PTP-MIB", "f3PtpNetPortFlowPointCIRLo"),
        ("F3-PTP-MIB", "f3PtpNetPortFlowPointCIRHi"),
        ("F3-PTP-MIB", "f3PtpNetPortFlowPointEIRLo"),
        ("F3-PTP-MIB", "f3PtpNetPortFlowPointEIRHi"),
        ("F3-PTP-MIB", "f3PtpNetPortFlowPointBufferSize"),
        ("F3-PTP-MIB", "f3PtpNetPortFlowPointLoopAvoidance"),
        ("F3-PTP-MIB", "f3PtpNetPortFlowPointRefConnectGuardFlow"),
        ("F3-PTP-MIB", "f3PtpNetPortFlowPointSecureState"),
        ("F3-PTP-MIB", "f3PtpNetPortFlowPointSecureBlockingEnabled"),
        ("F3-PTP-MIB", "f3PtpEthernetAccPortDelayAsymmetry"),
        ("F3-PTP-MIB", "f3PtpEthernetNetPortDelayAsymmetry"),
        ("F3-PTP-MIB", "f3PtpSysTimeOfDayClock"),
        ("F3-PTP-MIB", "f3PtpTrafficPortFlowPointIndex"),
        ("F3-PTP-MIB", "f3PtpTrafficPortFlowPointAlias"),
        ("F3-PTP-MIB", "f3PtpTrafficPortFlowPointAdminState"),
        ("F3-PTP-MIB", "f3PtpTrafficPortFlowPointOperationalState"),
        ("F3-PTP-MIB", "f3PtpTrafficPortFlowPointSecondaryState"),
        ("F3-PTP-MIB", "f3PtpTrafficPortFlowPointType"),
        ("F3-PTP-MIB", "f3PtpTrafficPortFlowPointClock"),
        ("F3-PTP-MIB", "f3PtpTrafficPortFlowPointService"),
        ("F3-PTP-MIB", "f3PtpTrafficPortFlowPointOuterVlanEtherType"),
        ("F3-PTP-MIB", "f3PtpTrafficPortFlowPointOuterVlanMemberList"),
        ("F3-PTP-MIB", "f3PtpTrafficPortFlowPointOuterUntaggedEnabled"),
        ("F3-PTP-MIB", "f3PtpTrafficPortFlowPointInner1VlanEtherType"),
        ("F3-PTP-MIB", "f3PtpTrafficPortFlowPointInner1VlanMemberList"),
        ("F3-PTP-MIB", "f3PtpTrafficPortFlowPointInner1UntaggedEnabled"),
        ("F3-PTP-MIB", "f3PtpTrafficPortFlowPointInner2VlanEtherType"),
        ("F3-PTP-MIB", "f3PtpTrafficPortFlowPointInner2VlanMemberList"),
        ("F3-PTP-MIB", "f3PtpTrafficPortFlowPointInner2UntaggedEnabled"),
        ("F3-PTP-MIB", "f3PtpTrafficPortFlowPointStorageType"),
        ("F3-PTP-MIB", "f3PtpTrafficPortFlowPointRowStatus"),
        ("F3-PTP-MIB", "f3PtpTrafficPortFlowPointCOS"),
        ("F3-PTP-MIB", "f3PtpTrafficPortFlowPointCIRLo"),
        ("F3-PTP-MIB", "f3PtpTrafficPortFlowPointCIRHi"),
        ("F3-PTP-MIB", "f3PtpTrafficPortFlowPointEIRLo"),
        ("F3-PTP-MIB", "f3PtpTrafficPortFlowPointEIRHi"),
        ("F3-PTP-MIB", "f3PtpTrafficPortFlowPointAssociatedQueueProfile"),
        ("F3-PTP-MIB", "f3PtpTrafficPortFlowPointLoopAvoidance"),
        ("F3-PTP-MIB", "f3PtpTrafficPortFlowPointBufferSize"),
        ("F3-PTP-MIB", "f3PtpEthernetTrafficPortDelayAsymmetry"),
        ("F3-PTP-MIB", "f3PtpPTPClockIndex"),
        ("F3-PTP-MIB", "f3PtpPTPClockAdminState"),
        ("F3-PTP-MIB", "f3PtpPTPClockAlias"),
        ("F3-PTP-MIB", "f3PtpPTPClockOperationalState"),
        ("F3-PTP-MIB", "f3PtpPTPClockSecondaryState"),
        ("F3-PTP-MIB", "f3PtpPTPClockProfile"),
        ("F3-PTP-MIB", "f3PtpPTPClockClockType"),
        ("F3-PTP-MIB", "f3PtpPTPClockOperationalMode"),
        ("F3-PTP-MIB", "f3PtpPTPClockClockIdentity"),
        ("F3-PTP-MIB", "f3PtpPTPClockDomainNumber"),
        ("F3-PTP-MIB", "f3PtpPTPClockTimeSource"),
        ("F3-PTP-MIB", "f3PtpPTPClockPriority1"),
        ("F3-PTP-MIB", "f3PtpPTPClockPriority2"),
        ("F3-PTP-MIB", "f3PtpPTPClockLocalPriority"),
        ("F3-PTP-MIB", "f3PtpPTPClockClockAccuracy"),
        ("F3-PTP-MIB", "f3PtpPTPClockScaledLogVariance"),
        ("F3-PTP-MIB", "f3PtpPTPClockSyncEid"),
        ("F3-PTP-MIB", "f3PtpPTPClockCurrentTimeOfDay"),
        ("F3-PTP-MIB", "f3PtpPTPClockActiveSlavePort"),
        ("F3-PTP-MIB", "f3PtpPTPClockClockRecoveryState"),
        ("F3-PTP-MIB", "f3PtpPTPClockPhaseRecoveryState"),
        ("F3-PTP-MIB", "f3PtpPTPClockTimeTraceabilityStatus"),
        ("F3-PTP-MIB", "f3PtpPTPClockTimeSinceTimeTraceabilityChanged"),
        ("F3-PTP-MIB", "f3PtpPTPClockFreqTraceabilityStatus"),
        ("F3-PTP-MIB", "f3PtpPTPClockTimeSinceFreqTraceabilityChanged"),
        ("F3-PTP-MIB", "f3PtpPTPClockClockSyncEEnabled"),
        ("F3-PTP-MIB", "f3PtpPTPClockClockQLModeEnabled"),
        ("F3-PTP-MIB", "f3PtpPTPClockClockExpectedQL"),
        ("F3-PTP-MIB", "f3PtpPTPClockClockAssumedQL"),
        ("F3-PTP-MIB", "f3PtpPTPClockClockReceivedQL"),
        ("F3-PTP-MIB", "f3PtpPTPClockCurrentOffsetFromMaster"),
        ("F3-PTP-MIB", "f3PtpPTPClockRecentMeanPathDelay"),
        ("F3-PTP-MIB", "f3PtpPTPClockRecentSyncPDV"),
        ("F3-PTP-MIB", "f3PtpPTPClockClockClass"),
        ("F3-PTP-MIB", "f3PtpPTPClockPhysicalEntityIndex"),
        ("F3-PTP-MIB", "f3PtpPTPClockActiveGrantsAnnounceService"),
        ("F3-PTP-MIB", "f3PtpPTPClockActiveGrantsSyncService"),
        ("F3-PTP-MIB", "f3PtpPTPClockActiveGrantsDelayRequestService"),
        ("F3-PTP-MIB", "f3PtpPTPClockMaxStepRemoved"),
        ("F3-PTP-MIB", "f3PtpPTPClockServiceAvailableTime"),
        ("F3-PTP-MIB", "f3PtpPTPClockServiceUnavailableTime"),
        ("F3-PTP-MIB", "f3PtpPTPClockServiceAvailablePercentage"),
        ("F3-PTP-MIB", "f3PtpPTPClockGrandMasterID"),
        ("F3-PTP-MIB", "f3PtpPTPClockTimeInaccuracy"),
        ("F3-PTP-MIB", "f3PtpPTPClockNetworkTimeInaccuracy"),
        ("F3-PTP-MIB", "f3PtpPTPClockStorageType"),
        ("F3-PTP-MIB", "f3PtpPTPClockRowStatus"),
        ("F3-PTP-MIB", "f3PtpPTPPortIndex"),
        ("F3-PTP-MIB", "f3PtpPTPPortAdminState"),
        ("F3-PTP-MIB", "f3PtpPTPPortAlias"),
        ("F3-PTP-MIB", "f3PtpPTPPortOperationalState"),
        ("F3-PTP-MIB", "f3PtpPTPPortSecondaryState"),
        ("F3-PTP-MIB", "f3PtpPTPPortPeerPortIdentity"),
        ("F3-PTP-MIB", "f3PtpPTPPortLocalPriority"),
        ("F3-PTP-MIB", "f3PtpPTPPortPtpFlowPointEid"),
        ("F3-PTP-MIB", "f3PtpPTPPortNotSlave"),
        ("F3-PTP-MIB", "f3PtpPTPPortTxDestMacAddress"),
        ("F3-PTP-MIB", "f3PtpPTPPortSyncMessageRate"),
        ("F3-PTP-MIB", "f3PtpPTPPortmDelayReqRespMsgRate"),
        ("F3-PTP-MIB", "f3PtpPTPPortmAnnounceMsgRate"),
        ("F3-PTP-MIB", "f3PtpPTPPortAnnounceReceiptTimeout"),
        ("F3-PTP-MIB", "f3PtpPTPPortSyncReceiptTimeout"),
        ("F3-PTP-MIB", "f3PtpPTPPortDelayRespTimeout"),
        ("F3-PTP-MIB", "f3PtpPTPPortPortState"),
        ("F3-PTP-MIB", "f3PtpPTPPortBmcaDecisionCode"),
        ("F3-PTP-MIB", "f3PtpPTPPortClockClass"),
        ("F3-PTP-MIB", "f3PtpPTPPortPeerPortMacAddress"),
        ("F3-PTP-MIB", "f3PtpPTPPortRowStatus"),
        ("F3-PTP-MIB", "f3PtpPTPPortPortIdentity"),
        ("F3-PTP-MIB", "f3PtpPTPPortMasterClockType"),
        ("F3-PTP-MIB", "f3PtpPTPPortLastRcvdAnnounceMsg"),
        ("F3-PTP-MIB", "f3PtpPTPPortLastRcvdSyncMsg"),
        ("F3-PTP-MIB", "f3PtpPTPPortLastRcvdDelayReqMsg"),
        ("F3-PTP-MIB", "f3PtpPTPPortLastRcvdDelayRspMsg"),
        ("F3-PTP-MIB", "f3PtpPTPPortMasterOnly"),
        ("F3-PTP-MIB", "f3PtpPTPPortPeerClockClass"),
        ("F3-PTP-MIB", "f3PtpPTPPortMinimumExpectedClockClass"),
        ("F3-PTP-MIB", "f3PtpPTPPortDelayAsymmetryComp"),
        ("F3-PTP-MIB", "f3PtpPTPPortAutoAsymmetryCompStatus"),
        ("F3-PTP-MIB", "f3PtpPTPPortDelayAsymmetry"),
        ("F3-PTP-MIB", "f3PtpPTPPortVirtualPortCtrl"),
        ("F3-PTP-MIB", "f3PtpPTPPortDelayResponderType"),
        ("F3-PTP-MIB", "f3PtpPTPPortTimeTraceable"),
        ("F3-PTP-MIB", "f3PtpPTPPortFrequencyTraceable"),
        ("F3-PTP-MIB", "f3PtpL2DynamicRemoteSlaveIndex"),
        ("F3-PTP-MIB", "f3PtpL2DynamicRemoteSlavePortIdentity"),
        ("F3-PTP-MIB", "f3PtpL2DynamicRemoteSlaveClockIdentity"),
        ("F3-PTP-MIB", "f3PtpL2DynamicRemoteSlaveMacAddress"),
        ("F3-PTP-MIB", "f3PtpL2DynamicRemoteSlaveRowStatus"),
        ("F3-PTP-MIB", "f3PtpL2DynamicRemoteSlaveStorageType"),
        ("F3-PTP-MIB", "f3PtpL3PTPPortIndex"),
        ("F3-PTP-MIB", "f3PtpL3PTPPortAdminState"),
        ("F3-PTP-MIB", "f3PtpL3PTPPortAlias"),
        ("F3-PTP-MIB", "f3PtpL3PTPPortOperationalState"),
        ("F3-PTP-MIB", "f3PtpL3PTPPortSecondaryState"),
        ("F3-PTP-MIB", "f3PtpL3PTPPortPortIdentity"),
        ("F3-PTP-MIB", "f3PtpL3PTPPortLocalPriority"),
        ("F3-PTP-MIB", "f3PtpL3PTPPortPtpFlowPointEid"),
        ("F3-PTP-MIB", "f3PtpL3PTPPortSyncMessageRate"),
        ("F3-PTP-MIB", "f3PtpL3PTPPortDelayReqRespMsgRate"),
        ("F3-PTP-MIB", "f3PtpL3PTPPortAnnounceMsgRate"),
        ("F3-PTP-MIB", "f3PtpL3PTPPortAnnounceReceiptTimeout"),
        ("F3-PTP-MIB", "f3PtpL3PTPPortSyncReceiptTimeout"),
        ("F3-PTP-MIB", "f3PtpL3PTPPortDelayRespTimeout"),
        ("F3-PTP-MIB", "f3PtpL3PTPPortPortState"),
        ("F3-PTP-MIB", "f3PtpL3PTPPortBmcaDecisionCode"),
        ("F3-PTP-MIB", "f3PtpL3PTPPortPeerClockClass"),
        ("F3-PTP-MIB", "f3PtpL3PTPPortMinimumExpectedClockClass"),
        ("F3-PTP-MIB", "f3PtpL3PTPPortIpProtocol"),
        ("F3-PTP-MIB", "f3PtpL3PTPPortIfName"),
        ("F3-PTP-MIB", "f3PtpL3PTPPortIpPriorityMapMode"),
        ("F3-PTP-MIB", "f3PtpL3PTPPortIpPriority"),
        ("F3-PTP-MIB", "f3PtpL3PTPPortIpV4Address"),
        ("F3-PTP-MIB", "f3PtpL3PTPPortIpV4SubnetMask"),
        ("F3-PTP-MIB", "f3PtpL3PTPPortIpV6Address"),
        ("F3-PTP-MIB", "f3PtpL3PTPPortIpV6AddrPrefixLength"),
        ("F3-PTP-MIB", "f3PtpL3PTPPortDefaultGatewayControl"),
        ("F3-PTP-MIB", "f3PtpL3PTPPortGateway"),
        ("F3-PTP-MIB", "f3PtpL3PTPPortIpV6Gateway"),
        ("F3-PTP-MIB", "f3PtpL3PTPPortUnicastMessageNegEnabled"),
        ("F3-PTP-MIB", "f3PtpL3PTPPortTransmitDuration"),
        ("F3-PTP-MIB", "f3PtpL3PTPPortRequestUnicastTimeout"),
        ("F3-PTP-MIB", "f3PtpL3PTPPortRequestUnicastRestartTimer"),
        ("F3-PTP-MIB", "f3PtpL3PTPPortMasterIpV4Address"),
        ("F3-PTP-MIB", "f3PtpL3PTPPortMasterIpV6Address"),
        ("F3-PTP-MIB", "f3PtpL3PTPPortDelayAsymmetryComp"),
        ("F3-PTP-MIB", "f3PtpL3PTPPortAutoAsymmetryCompStatus"),
        ("F3-PTP-MIB", "f3PtpL3PTPPortDelayAsymmetry"),
        ("F3-PTP-MIB", "f3PtpL3PTPPortStorageType"),
        ("F3-PTP-MIB", "f3PtpL3PTPPortRowStatus"))
)
if mibBuilder.loadTexts:
    f3PtpObjectGroup.setStatus("current")

f3PtpPerfObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 4, 2, 2)
)
f3PtpPerfObjectGroup.setObjects(
      *(("F3-PTP-MIB", "f3PtpAccPortFlowPointStatsIndex"),
        ("F3-PTP-MIB", "f3PtpAccPortFlowPointStatsIntervalType"),
        ("F3-PTP-MIB", "f3PtpAccPortFlowPointStatsValid"),
        ("F3-PTP-MIB", "f3PtpAccPortFlowPointStatsAction"),
        ("F3-PTP-MIB", "f3PtpAccPortFlowPointStatsAnnouncesRx"),
        ("F3-PTP-MIB", "f3PtpAccPortFlowPointStatsAnnouncesTx"),
        ("F3-PTP-MIB", "f3PtpAccPortFlowPointStatsSyncsRx"),
        ("F3-PTP-MIB", "f3PtpAccPortFlowPointStatsSyncsTx"),
        ("F3-PTP-MIB", "f3PtpAccPortFlowPointStatsFollowupsRx"),
        ("F3-PTP-MIB", "f3PtpAccPortFlowPointStatsFollowupsTx"),
        ("F3-PTP-MIB", "f3PtpAccPortFlowPointStatsDelayReqsRx"),
        ("F3-PTP-MIB", "f3PtpAccPortFlowPointStatsDelayReqsTx"),
        ("F3-PTP-MIB", "f3PtpAccPortFlowPointStatsDelayRspsRx"),
        ("F3-PTP-MIB", "f3PtpAccPortFlowPointStatsDelayRspsTx"),
        ("F3-PTP-MIB", "f3PtpAccPortFlowPointStatsPDelayReqsRx"),
        ("F3-PTP-MIB", "f3PtpAccPortFlowPointStatsPDelayReqsTx"),
        ("F3-PTP-MIB", "f3PtpAccPortFlowPointStatsPDelayRspsRx"),
        ("F3-PTP-MIB", "f3PtpAccPortFlowPointStatsPDelayRspsTx"),
        ("F3-PTP-MIB", "f3PtpAccPortFlowPointStatsPDelayRspFollowupsRx"),
        ("F3-PTP-MIB", "f3PtpAccPortFlowPointStatsPDelayRspFollowupsTx"),
        ("F3-PTP-MIB", "f3PtpAccPortFlowPointStatsSignalingRx"),
        ("F3-PTP-MIB", "f3PtpAccPortFlowPointStatsSignalingTx"),
        ("F3-PTP-MIB", "f3PtpAccPortFlowPointStatsMgmtFramesRx"),
        ("F3-PTP-MIB", "f3PtpAccPortFlowPointStatsMgmtFramesTx"),
        ("F3-PTP-MIB", "f3PtpAccPortFlowPointStatsPtpUnknownsRx"),
        ("F3-PTP-MIB", "f3PtpAccPortFlowPointStatsPtpUnknownsTx"),
        ("F3-PTP-MIB", "f3PtpAccPortFlowPointStatsAvgSyncResTime"),
        ("F3-PTP-MIB", "f3PtpAccPortFlowPointStatsMinSyncResTime"),
        ("F3-PTP-MIB", "f3PtpAccPortFlowPointStatsMaxSyncResTime"),
        ("F3-PTP-MIB", "f3PtpAccPortFlowPointStatsAvgDelayReqResTime"),
        ("F3-PTP-MIB", "f3PtpAccPortFlowPointStatsMinDelayReqResTime"),
        ("F3-PTP-MIB", "f3PtpAccPortFlowPointStatsMaxDelayReqResTime"),
        ("F3-PTP-MIB", "f3PtpAccPortFlowPointStatsMinPDelayReqResTime"),
        ("F3-PTP-MIB", "f3PtpAccPortFlowPointStatsMaxPDelayReqResTime"),
        ("F3-PTP-MIB", "f3PtpAccPortFlowPointStatsAvgPDelayReqResTime"),
        ("F3-PTP-MIB", "f3PtpAccPortFlowPointStatsMinPDelayRspResTime"),
        ("F3-PTP-MIB", "f3PtpAccPortFlowPointStatsMaxPDelayRspResTime"),
        ("F3-PTP-MIB", "f3PtpAccPortFlowPointStatsAvgPDelayRspResTime"),
        ("F3-PTP-MIB", "f3PtpAccPortFlowPointStatsDestMciNoMatchDiscards"),
        ("F3-PTP-MIB", "f3PtpAccPortFlowPointHistoryIndex"),
        ("F3-PTP-MIB", "f3PtpAccPortFlowPointHistoryTime"),
        ("F3-PTP-MIB", "f3PtpAccPortFlowPointHistoryValid"),
        ("F3-PTP-MIB", "f3PtpAccPortFlowPointHistoryAction"),
        ("F3-PTP-MIB", "f3PtpAccPortFlowPointHistoryAnnouncesRx"),
        ("F3-PTP-MIB", "f3PtpAccPortFlowPointHistoryAnnouncesTx"),
        ("F3-PTP-MIB", "f3PtpAccPortFlowPointHistorySyncsRx"),
        ("F3-PTP-MIB", "f3PtpAccPortFlowPointHistorySyncsTx"),
        ("F3-PTP-MIB", "f3PtpAccPortFlowPointHistoryFollowupsRx"),
        ("F3-PTP-MIB", "f3PtpAccPortFlowPointHistoryFollowupsTx"),
        ("F3-PTP-MIB", "f3PtpAccPortFlowPointHistoryDelayReqsRx"),
        ("F3-PTP-MIB", "f3PtpAccPortFlowPointHistoryDelayReqsTx"),
        ("F3-PTP-MIB", "f3PtpAccPortFlowPointHistoryDelayRspsRx"),
        ("F3-PTP-MIB", "f3PtpAccPortFlowPointHistoryDelayRspsTx"),
        ("F3-PTP-MIB", "f3PtpAccPortFlowPointHistoryPDelayReqsRx"),
        ("F3-PTP-MIB", "f3PtpAccPortFlowPointHistoryPDelayReqsTx"),
        ("F3-PTP-MIB", "f3PtpAccPortFlowPointHistoryPDelayRspsRx"),
        ("F3-PTP-MIB", "f3PtpAccPortFlowPointHistoryPDelayRspsTx"),
        ("F3-PTP-MIB", "f3PtpAccPortFlowPointHistoryPDelayRspFollowupsRx"),
        ("F3-PTP-MIB", "f3PtpAccPortFlowPointHistoryPDelayRspFollowupsTx"),
        ("F3-PTP-MIB", "f3PtpAccPortFlowPointHistorySignalingRx"),
        ("F3-PTP-MIB", "f3PtpAccPortFlowPointHistorySignalingTx"),
        ("F3-PTP-MIB", "f3PtpAccPortFlowPointHistoryMgmtFramesRx"),
        ("F3-PTP-MIB", "f3PtpAccPortFlowPointHistoryMgmtFramesTx"),
        ("F3-PTP-MIB", "f3PtpAccPortFlowPointHistoryPtpUnknownsRx"),
        ("F3-PTP-MIB", "f3PtpAccPortFlowPointHistoryPtpUnknownsTx"),
        ("F3-PTP-MIB", "f3PtpAccPortFlowPointHistoryAvgSyncResTime"),
        ("F3-PTP-MIB", "f3PtpAccPortFlowPointHistoryMinSyncResTime"),
        ("F3-PTP-MIB", "f3PtpAccPortFlowPointHistoryMaxSyncResTime"),
        ("F3-PTP-MIB", "f3PtpAccPortFlowPointHistoryAvgDelayReqResTime"),
        ("F3-PTP-MIB", "f3PtpAccPortFlowPointHistoryMinDelayReqResTime"),
        ("F3-PTP-MIB", "f3PtpAccPortFlowPointHistoryMaxDelayReqResTime"),
        ("F3-PTP-MIB", "f3PtpAccPortFlowPointHistoryMinPDelayReqResTime"),
        ("F3-PTP-MIB", "f3PtpAccPortFlowPointHistoryMaxPDelayReqResTime"),
        ("F3-PTP-MIB", "f3PtpAccPortFlowPointHistoryAvgPDelayReqResTime"),
        ("F3-PTP-MIB", "f3PtpAccPortFlowPointHistoryMinPDelayRspResTime"),
        ("F3-PTP-MIB", "f3PtpAccPortFlowPointHistoryMaxPDelayRspResTime"),
        ("F3-PTP-MIB", "f3PtpAccPortFlowPointHistoryAvgPDelayRspResTime"),
        ("F3-PTP-MIB", "f3PtpAccPortFlowPointHistoryDestMciNoMatchDiscards"),
        ("F3-PTP-MIB", "f3PtpAccPortFlowPointThresholdIndex"),
        ("F3-PTP-MIB", "f3PtpAccPortFlowPointThresholdInterval"),
        ("F3-PTP-MIB", "f3PtpAccPortFlowPointThresholdVariable"),
        ("F3-PTP-MIB", "f3PtpAccPortFlowPointThresholdValueLo"),
        ("F3-PTP-MIB", "f3PtpAccPortFlowPointThresholdValueHi"),
        ("F3-PTP-MIB", "f3PtpAccPortFlowPointThresholdMonValue"),
        ("F3-PTP-MIB", "f3PtpNetPortFlowPointStatsIndex"),
        ("F3-PTP-MIB", "f3PtpNetPortFlowPointStatsIntervalType"),
        ("F3-PTP-MIB", "f3PtpNetPortFlowPointStatsValid"),
        ("F3-PTP-MIB", "f3PtpNetPortFlowPointStatsAction"),
        ("F3-PTP-MIB", "f3PtpNetPortFlowPointStatsAnnouncesRx"),
        ("F3-PTP-MIB", "f3PtpNetPortFlowPointStatsAnnouncesTx"),
        ("F3-PTP-MIB", "f3PtpNetPortFlowPointStatsSyncsRx"),
        ("F3-PTP-MIB", "f3PtpNetPortFlowPointStatsSyncsTx"),
        ("F3-PTP-MIB", "f3PtpNetPortFlowPointStatsFollowupsRx"),
        ("F3-PTP-MIB", "f3PtpNetPortFlowPointStatsFollowupsTx"),
        ("F3-PTP-MIB", "f3PtpNetPortFlowPointStatsDelayReqsRx"),
        ("F3-PTP-MIB", "f3PtpNetPortFlowPointStatsDelayReqsTx"),
        ("F3-PTP-MIB", "f3PtpNetPortFlowPointStatsDelayRspsRx"),
        ("F3-PTP-MIB", "f3PtpNetPortFlowPointStatsDelayRspsTx"),
        ("F3-PTP-MIB", "f3PtpNetPortFlowPointStatsPDelayReqsRx"),
        ("F3-PTP-MIB", "f3PtpNetPortFlowPointStatsPDelayReqsTx"),
        ("F3-PTP-MIB", "f3PtpNetPortFlowPointStatsPDelayRspsRx"),
        ("F3-PTP-MIB", "f3PtpNetPortFlowPointStatsPDelayRspsTx"),
        ("F3-PTP-MIB", "f3PtpNetPortFlowPointStatsPDelayRspFollowupsRx"),
        ("F3-PTP-MIB", "f3PtpNetPortFlowPointStatsPDelayRspFollowupsTx"),
        ("F3-PTP-MIB", "f3PtpNetPortFlowPointStatsSignalingRx"),
        ("F3-PTP-MIB", "f3PtpNetPortFlowPointStatsSignalingTx"),
        ("F3-PTP-MIB", "f3PtpNetPortFlowPointStatsMgmtFramesRx"),
        ("F3-PTP-MIB", "f3PtpNetPortFlowPointStatsMgmtFramesTx"),
        ("F3-PTP-MIB", "f3PtpNetPortFlowPointStatsPtpUnknownsRx"),
        ("F3-PTP-MIB", "f3PtpNetPortFlowPointStatsPtpUnknownsTx"),
        ("F3-PTP-MIB", "f3PtpNetPortFlowPointStatsAvgSyncResTime"),
        ("F3-PTP-MIB", "f3PtpNetPortFlowPointStatsMinSyncResTime"),
        ("F3-PTP-MIB", "f3PtpNetPortFlowPointStatsMaxSyncResTime"),
        ("F3-PTP-MIB", "f3PtpNetPortFlowPointStatsAvgDelayReqResTime"),
        ("F3-PTP-MIB", "f3PtpNetPortFlowPointStatsMinDelayReqResTime"),
        ("F3-PTP-MIB", "f3PtpNetPortFlowPointStatsMaxDelayReqResTime"),
        ("F3-PTP-MIB", "f3PtpNetPortFlowPointStatsMinPDelayReqResTime"),
        ("F3-PTP-MIB", "f3PtpNetPortFlowPointStatsMaxPDelayReqResTime"),
        ("F3-PTP-MIB", "f3PtpNetPortFlowPointStatsAvgPDelayReqResTime"),
        ("F3-PTP-MIB", "f3PtpNetPortFlowPointStatsMinPDelayRspResTime"),
        ("F3-PTP-MIB", "f3PtpNetPortFlowPointStatsMaxPDelayRspResTime"),
        ("F3-PTP-MIB", "f3PtpNetPortFlowPointStatsAvgPDelayRspResTime"),
        ("F3-PTP-MIB", "f3PtpNetPortFlowPointStatsDestMciNoMatchDiscards"),
        ("F3-PTP-MIB", "f3PtpNetPortFlowPointHistoryIndex"),
        ("F3-PTP-MIB", "f3PtpNetPortFlowPointHistoryTime"),
        ("F3-PTP-MIB", "f3PtpNetPortFlowPointHistoryValid"),
        ("F3-PTP-MIB", "f3PtpNetPortFlowPointHistoryAction"),
        ("F3-PTP-MIB", "f3PtpNetPortFlowPointHistoryAnnouncesRx"),
        ("F3-PTP-MIB", "f3PtpNetPortFlowPointHistoryAnnouncesTx"),
        ("F3-PTP-MIB", "f3PtpNetPortFlowPointHistorySyncsRx"),
        ("F3-PTP-MIB", "f3PtpNetPortFlowPointHistorySyncsTx"),
        ("F3-PTP-MIB", "f3PtpNetPortFlowPointHistoryFollowupsRx"),
        ("F3-PTP-MIB", "f3PtpNetPortFlowPointHistoryFollowupsTx"),
        ("F3-PTP-MIB", "f3PtpNetPortFlowPointHistoryDelayReqsRx"),
        ("F3-PTP-MIB", "f3PtpNetPortFlowPointHistoryDelayReqsTx"),
        ("F3-PTP-MIB", "f3PtpNetPortFlowPointHistoryDelayRspsRx"),
        ("F3-PTP-MIB", "f3PtpNetPortFlowPointHistoryDelayRspsTx"),
        ("F3-PTP-MIB", "f3PtpNetPortFlowPointHistoryPDelayReqsRx"),
        ("F3-PTP-MIB", "f3PtpNetPortFlowPointHistoryPDelayReqsTx"),
        ("F3-PTP-MIB", "f3PtpNetPortFlowPointHistoryPDelayRspsRx"),
        ("F3-PTP-MIB", "f3PtpNetPortFlowPointHistoryPDelayRspsTx"),
        ("F3-PTP-MIB", "f3PtpNetPortFlowPointHistoryPDelayRspFollowupsRx"),
        ("F3-PTP-MIB", "f3PtpNetPortFlowPointHistoryPDelayRspFollowupsTx"),
        ("F3-PTP-MIB", "f3PtpNetPortFlowPointHistorySignalingRx"),
        ("F3-PTP-MIB", "f3PtpNetPortFlowPointHistorySignalingTx"),
        ("F3-PTP-MIB", "f3PtpNetPortFlowPointHistoryMgmtFramesRx"),
        ("F3-PTP-MIB", "f3PtpNetPortFlowPointHistoryMgmtFramesTx"),
        ("F3-PTP-MIB", "f3PtpNetPortFlowPointHistoryPtpUnknownsRx"),
        ("F3-PTP-MIB", "f3PtpNetPortFlowPointHistoryPtpUnknownsTx"),
        ("F3-PTP-MIB", "f3PtpNetPortFlowPointHistoryAvgSyncResTime"),
        ("F3-PTP-MIB", "f3PtpNetPortFlowPointHistoryMinSyncResTime"),
        ("F3-PTP-MIB", "f3PtpNetPortFlowPointHistoryMaxSyncResTime"),
        ("F3-PTP-MIB", "f3PtpNetPortFlowPointHistoryAvgDelayReqResTime"),
        ("F3-PTP-MIB", "f3PtpNetPortFlowPointHistoryMinDelayReqResTime"),
        ("F3-PTP-MIB", "f3PtpNetPortFlowPointHistoryMaxDelayReqResTime"),
        ("F3-PTP-MIB", "f3PtpNetPortFlowPointHistoryMinPDelayReqResTime"),
        ("F3-PTP-MIB", "f3PtpNetPortFlowPointHistoryMaxPDelayReqResTime"),
        ("F3-PTP-MIB", "f3PtpNetPortFlowPointHistoryAvgPDelayReqResTime"),
        ("F3-PTP-MIB", "f3PtpNetPortFlowPointHistoryMinPDelayRspResTime"),
        ("F3-PTP-MIB", "f3PtpNetPortFlowPointHistoryMaxPDelayRspResTime"),
        ("F3-PTP-MIB", "f3PtpNetPortFlowPointHistoryAvgPDelayRspResTime"),
        ("F3-PTP-MIB", "f3PtpNetPortFlowPointHistoryDestMciNoMatchDiscards"),
        ("F3-PTP-MIB", "f3PtpNetPortFlowPointThresholdIndex"),
        ("F3-PTP-MIB", "f3PtpNetPortFlowPointThresholdInterval"),
        ("F3-PTP-MIB", "f3PtpNetPortFlowPointThresholdVariable"),
        ("F3-PTP-MIB", "f3PtpNetPortFlowPointThresholdValueLo"),
        ("F3-PTP-MIB", "f3PtpNetPortFlowPointThresholdValueHi"),
        ("F3-PTP-MIB", "f3PtpNetPortFlowPointThresholdMonValue"),
        ("F3-PTP-MIB", "f3PtpSOOCStatsIndex"),
        ("F3-PTP-MIB", "f3PtpSOOCStatsIntervalType"),
        ("F3-PTP-MIB", "f3PtpSOOCStatsValid"),
        ("F3-PTP-MIB", "f3PtpSOOCStatsAction"),
        ("F3-PTP-MIB", "f3PtpSOOCStatsMinOffsetFromMaster"),
        ("F3-PTP-MIB", "f3PtpSOOCStatsMaxOffsetFromMaster"),
        ("F3-PTP-MIB", "f3PtpSOOCStatsAvgOffsetFromMaster"),
        ("F3-PTP-MIB", "f3PtpSOOCStatsMinMeanPathDelay"),
        ("F3-PTP-MIB", "f3PtpSOOCStatsMaxMeanPathDelay"),
        ("F3-PTP-MIB", "f3PtpSOOCStatsAvgMeanPathDelay"),
        ("F3-PTP-MIB", "f3PtpSOOCStatsMinSyncPathDelay"),
        ("F3-PTP-MIB", "f3PtpSOOCStatsMaxSyncPathDelay"),
        ("F3-PTP-MIB", "f3PtpSOOCStatsAvgSyncPathDelay"),
        ("F3-PTP-MIB", "f3PtpSOOCStatsMinSyncPDV"),
        ("F3-PTP-MIB", "f3PtpSOOCStatsMaxSyncPDV"),
        ("F3-PTP-MIB", "f3PtpSOOCStatsAvgSyncPDV"),
        ("F3-PTP-MIB", "f3PtpSOOCStatsMgmtMsgsDiscarded"),
        ("F3-PTP-MIB", "f3PtpSOOCStatsInvalidMsgLenDiscards"),
        ("F3-PTP-MIB", "f3PtpSOOCStatsUnknownMasterDiscards"),
        ("F3-PTP-MIB", "f3PtpSOOCStatsUnknownDomainDiscards"),
        ("F3-PTP-MIB", "f3PtpSOOCStatsMulticastAnnounceDiscards"),
        ("F3-PTP-MIB", "f3PtpSOOCStatsOutOfSeqAnnounceMsgs"),
        ("F3-PTP-MIB", "f3PtpSOOCStatsMulticastSyncDiscards"),
        ("F3-PTP-MIB", "f3PtpSOOCStatsTwoStepSyncDiscards"),
        ("F3-PTP-MIB", "f3PtpSOOCStatsFollowupDiscards"),
        ("F3-PTP-MIB", "f3PtpSOOCStatsDelayReqDiscards"),
        ("F3-PTP-MIB", "f3PtpSOOCStatsPDelayReqDiscards"),
        ("F3-PTP-MIB", "f3PtpSOOCStatsPDelayRspDiscards"),
        ("F3-PTP-MIB", "f3PtpSOOCStatsPDelayFollowupDiscards"),
        ("F3-PTP-MIB", "f3PtpSOOCStatsInvalidTLVLenDiscards"),
        ("F3-PTP-MIB", "f3PtpSOOCStatsInvalidTLVTypeDiscards"),
        ("F3-PTP-MIB", "f3PtpSOOCStatsMaxFwdFlowWeight"),
        ("F3-PTP-MIB", "f3PtpSOOCStatsAvgFwdFlowWeight"),
        ("F3-PTP-MIB", "f3PtpSOOCStatsMinRevFlowWeight"),
        ("F3-PTP-MIB", "f3PtpSOOCStatsMaxRevFlowWeight"),
        ("F3-PTP-MIB", "f3PtpSOOCStatsAvgRevFlowWeight"),
        ("F3-PTP-MIB", "f3PtpSOOCStatsNumClockRecTransients"),
        ("F3-PTP-MIB", "f3PtpSOOCHistoryIndex"),
        ("F3-PTP-MIB", "f3PtpSOOCHistoryTime"),
        ("F3-PTP-MIB", "f3PtpSOOCHistoryValid"),
        ("F3-PTP-MIB", "f3PtpSOOCHistoryAction"),
        ("F3-PTP-MIB", "f3PtpSOOCHistoryMinOffsetFromMaster"),
        ("F3-PTP-MIB", "f3PtpSOOCHistoryMaxOffsetFromMaster"),
        ("F3-PTP-MIB", "f3PtpSOOCHistoryAvgOffsetFromMaster"),
        ("F3-PTP-MIB", "f3PtpSOOCHistoryMinMeanPathDelay"),
        ("F3-PTP-MIB", "f3PtpSOOCHistoryMaxMeanPathDelay"),
        ("F3-PTP-MIB", "f3PtpSOOCHistoryAvgMeanPathDelay"),
        ("F3-PTP-MIB", "f3PtpSOOCHistoryMinSyncPathDelay"),
        ("F3-PTP-MIB", "f3PtpSOOCHistoryMaxSyncPathDelay"),
        ("F3-PTP-MIB", "f3PtpSOOCHistoryAvgSyncPathDelay"),
        ("F3-PTP-MIB", "f3PtpSOOCHistoryMinSyncPDV"),
        ("F3-PTP-MIB", "f3PtpSOOCHistoryMaxSyncPDV"),
        ("F3-PTP-MIB", "f3PtpSOOCHistoryAvgSyncPDV"),
        ("F3-PTP-MIB", "f3PtpSOOCHistoryMgmtMsgsDiscarded"),
        ("F3-PTP-MIB", "f3PtpSOOCHistoryInvalidMsgLenDiscards"),
        ("F3-PTP-MIB", "f3PtpSOOCHistoryUnknownMasterDiscards"),
        ("F3-PTP-MIB", "f3PtpSOOCHistoryUnknownDomainDiscards"),
        ("F3-PTP-MIB", "f3PtpSOOCHistoryMulticastAnnounceDiscards"),
        ("F3-PTP-MIB", "f3PtpSOOCHistoryOutOfSeqAnnounceMsgs"),
        ("F3-PTP-MIB", "f3PtpSOOCHistoryMulticastSyncDiscards"),
        ("F3-PTP-MIB", "f3PtpSOOCHistoryTwoStepSyncDiscards"),
        ("F3-PTP-MIB", "f3PtpSOOCHistoryFollowupDiscards"),
        ("F3-PTP-MIB", "f3PtpSOOCHistoryDelayReqDiscards"),
        ("F3-PTP-MIB", "f3PtpSOOCHistoryPDelayReqDiscards"),
        ("F3-PTP-MIB", "f3PtpSOOCHistoryPDelayRspDiscards"),
        ("F3-PTP-MIB", "f3PtpSOOCHistoryPDelayFollowupDiscards"),
        ("F3-PTP-MIB", "f3PtpSOOCHistoryInvalidTLVLenDiscards"),
        ("F3-PTP-MIB", "f3PtpSOOCHistoryInvalidTLVTypeDiscards"),
        ("F3-PTP-MIB", "f3PtpSOOCHistoryMaxFwdFlowWeight"),
        ("F3-PTP-MIB", "f3PtpSOOCHistoryAvgFwdFlowWeight"),
        ("F3-PTP-MIB", "f3PtpSOOCHistoryMinRevFlowWeight"),
        ("F3-PTP-MIB", "f3PtpSOOCHistoryMaxRevFlowWeight"),
        ("F3-PTP-MIB", "f3PtpSOOCHistoryAvgRevFlowWeight"),
        ("F3-PTP-MIB", "f3PtpSOOCHistoryNumClockRecTransients"),
        ("F3-PTP-MIB", "f3PtpSOOCThresholdIndex"),
        ("F3-PTP-MIB", "f3PtpSOOCThresholdInterval"),
        ("F3-PTP-MIB", "f3PtpSOOCThresholdVariable"),
        ("F3-PTP-MIB", "f3PtpSOOCThresholdValueLo"),
        ("F3-PTP-MIB", "f3PtpSOOCThresholdValueHi"),
        ("F3-PTP-MIB", "f3PtpSOOCThresholdMonValue"),
        ("F3-PTP-MIB", "f3PtpTSStatsIndex"),
        ("F3-PTP-MIB", "f3PtpTSStatsIntervalType"),
        ("F3-PTP-MIB", "f3PtpTSStatsValid"),
        ("F3-PTP-MIB", "f3PtpTSStatsAction"),
        ("F3-PTP-MIB", "f3PtpTSStatsTotalTimeCR5"),
        ("F3-PTP-MIB", "f3PtpTSStatsTotalTimeCR4"),
        ("F3-PTP-MIB", "f3PtpTSStatsTotalTimeCR3"),
        ("F3-PTP-MIB", "f3PtpTSStatsTotalTimePR5"),
        ("F3-PTP-MIB", "f3PtpTSStatsTotalTimePR4"),
        ("F3-PTP-MIB", "f3PtpTSStatsTotalTimePR3"),
        ("F3-PTP-MIB", "f3PtpTSHistoryIndex"),
        ("F3-PTP-MIB", "f3PtpTSHistoryTime"),
        ("F3-PTP-MIB", "f3PtpTSHistoryValid"),
        ("F3-PTP-MIB", "f3PtpTSHistoryAction"),
        ("F3-PTP-MIB", "f3PtpTSHistoryTotalTimeCR5"),
        ("F3-PTP-MIB", "f3PtpTSHistoryTotalTimeCR4"),
        ("F3-PTP-MIB", "f3PtpTSHistoryTotalTimeCR3"),
        ("F3-PTP-MIB", "f3PtpTSHistoryTotalTimePR5"),
        ("F3-PTP-MIB", "f3PtpTSHistoryTotalTimePR4"),
        ("F3-PTP-MIB", "f3PtpTSHistoryTotalTimePR3"),
        ("F3-PTP-MIB", "f3PtpTSThresholdIndex"),
        ("F3-PTP-MIB", "f3PtpTSThresholdInterval"),
        ("F3-PTP-MIB", "f3PtpTSThresholdVariable"),
        ("F3-PTP-MIB", "f3PtpTSThresholdValueLo"),
        ("F3-PTP-MIB", "f3PtpTSThresholdValueHi"),
        ("F3-PTP-MIB", "f3PtpTSThresholdMonValue"),
        ("F3-PTP-MIB", "f3PtpTrafficPortFlowPointStatsIndex"),
        ("F3-PTP-MIB", "f3PtpTrafficPortFlowPointStatsIntervalType"),
        ("F3-PTP-MIB", "f3PtpTrafficPortFlowPointStatsValid"),
        ("F3-PTP-MIB", "f3PtpTrafficPortFlowPointStatsAction"),
        ("F3-PTP-MIB", "f3PtpTrafficPortFlowPointStatsAnnouncesRx"),
        ("F3-PTP-MIB", "f3PtpTrafficPortFlowPointStatsAnnouncesTx"),
        ("F3-PTP-MIB", "f3PtpTrafficPortFlowPointStatsSyncsRx"),
        ("F3-PTP-MIB", "f3PtpTrafficPortFlowPointStatsSyncsTx"),
        ("F3-PTP-MIB", "f3PtpTrafficPortFlowPointStatsFollowupsRx"),
        ("F3-PTP-MIB", "f3PtpTrafficPortFlowPointStatsFollowupsTx"),
        ("F3-PTP-MIB", "f3PtpTrafficPortFlowPointStatsDelayReqsRx"),
        ("F3-PTP-MIB", "f3PtpTrafficPortFlowPointStatsDelayReqsTx"),
        ("F3-PTP-MIB", "f3PtpTrafficPortFlowPointStatsDelayRspsRx"),
        ("F3-PTP-MIB", "f3PtpTrafficPortFlowPointStatsDelayRspsTx"),
        ("F3-PTP-MIB", "f3PtpTrafficPortFlowPointStatsPDelayReqsRx"),
        ("F3-PTP-MIB", "f3PtpTrafficPortFlowPointStatsPDelayReqsTx"),
        ("F3-PTP-MIB", "f3PtpTrafficPortFlowPointStatsPDelayRspsRx"),
        ("F3-PTP-MIB", "f3PtpTrafficPortFlowPointStatsPDelayRspsTx"),
        ("F3-PTP-MIB", "f3PtpTrafficPortFlowPointStatsPDelayRspFollowupsRx"),
        ("F3-PTP-MIB", "f3PtpTrafficPortFlowPointStatsPDelayRspFollowupsTx"),
        ("F3-PTP-MIB", "f3PtpTrafficPortFlowPointStatsSignalingRx"),
        ("F3-PTP-MIB", "f3PtpTrafficPortFlowPointStatsSignalingTx"),
        ("F3-PTP-MIB", "f3PtpTrafficPortFlowPointStatsMgmtFramesRx"),
        ("F3-PTP-MIB", "f3PtpTrafficPortFlowPointStatsMgmtFramesTx"),
        ("F3-PTP-MIB", "f3PtpTrafficPortFlowPointStatsPtpUnknownsRx"),
        ("F3-PTP-MIB", "f3PtpTrafficPortFlowPointStatsPtpUnknownsTx"),
        ("F3-PTP-MIB", "f3PtpTrafficPortFlowPointStatsMinSyncResTime"),
        ("F3-PTP-MIB", "f3PtpTrafficPortFlowPointStatsMaxSyncResTime"),
        ("F3-PTP-MIB", "f3PtpTrafficPortFlowPointStatsAvgSyncResTime"),
        ("F3-PTP-MIB", "f3PtpTrafficPortFlowPointStatsMinDelayReqResTime"),
        ("F3-PTP-MIB", "f3PtpTrafficPortFlowPointStatsMaxDelayReqResTime"),
        ("F3-PTP-MIB", "f3PtpTrafficPortFlowPointStatsAvgDelayReqResTime"),
        ("F3-PTP-MIB", "f3PtpTrafficPortFlowPointStatsMinPDelayReqResTime"),
        ("F3-PTP-MIB", "f3PtpTrafficPortFlowPointStatsMaxPDelayReqResTime"),
        ("F3-PTP-MIB", "f3PtpTrafficPortFlowPointStatsAvgPDelayReqResTime"),
        ("F3-PTP-MIB", "f3PtpTrafficPortFlowPointStatsMinPDelayRspResTime"),
        ("F3-PTP-MIB", "f3PtpTrafficPortFlowPointStatsMaxPDelayRspResTime"),
        ("F3-PTP-MIB", "f3PtpTrafficPortFlowPointStatsAvgPDelayRspResTime"),
        ("F3-PTP-MIB", "f3PtpTrafficPortFlowPointStatsDestMciNoMatchDiscards"),
        ("F3-PTP-MIB", "f3PtpTrafficPortFlowPointStatsTagNoMatchDiscards"),
        ("F3-PTP-MIB", "f3PtpTrafficPortFlowPointHistoryIndex"),
        ("F3-PTP-MIB", "f3PtpTrafficPortFlowPointHistoryTime"),
        ("F3-PTP-MIB", "f3PtpTrafficPortFlowPointHistoryValid"),
        ("F3-PTP-MIB", "f3PtpTrafficPortFlowPointHistoryAction"),
        ("F3-PTP-MIB", "f3PtpTrafficPortFlowPointHistoryAnnouncesRx"),
        ("F3-PTP-MIB", "f3PtpTrafficPortFlowPointHistoryAnnouncesTx"),
        ("F3-PTP-MIB", "f3PtpTrafficPortFlowPointHistorySyncsRx"),
        ("F3-PTP-MIB", "f3PtpTrafficPortFlowPointHistorySyncsTx"),
        ("F3-PTP-MIB", "f3PtpTrafficPortFlowPointHistoryFollowupsRx"),
        ("F3-PTP-MIB", "f3PtpTrafficPortFlowPointHistoryFollowupsTx"),
        ("F3-PTP-MIB", "f3PtpTrafficPortFlowPointHistoryDelayReqsRx"),
        ("F3-PTP-MIB", "f3PtpTrafficPortFlowPointHistoryDelayReqsTx"),
        ("F3-PTP-MIB", "f3PtpTrafficPortFlowPointHistoryDelayRspsRx"),
        ("F3-PTP-MIB", "f3PtpTrafficPortFlowPointHistoryDelayRspsTx"),
        ("F3-PTP-MIB", "f3PtpTrafficPortFlowPointHistoryPDelayReqsRx"),
        ("F3-PTP-MIB", "f3PtpTrafficPortFlowPointHistoryPDelayReqsTx"),
        ("F3-PTP-MIB", "f3PtpTrafficPortFlowPointHistoryPDelayRspsRx"),
        ("F3-PTP-MIB", "f3PtpTrafficPortFlowPointHistoryPDelayRspsTx"),
        ("F3-PTP-MIB", "f3PtpTrafficPortFlowPointHistoryPDelayRspFollowupsRx"),
        ("F3-PTP-MIB", "f3PtpTrafficPortFlowPointHistoryPDelayRspFollowupsTx"),
        ("F3-PTP-MIB", "f3PtpTrafficPortFlowPointHistorySignalingRx"),
        ("F3-PTP-MIB", "f3PtpTrafficPortFlowPointHistorySignalingTx"),
        ("F3-PTP-MIB", "f3PtpTrafficPortFlowPointHistoryMgmtFramesRx"),
        ("F3-PTP-MIB", "f3PtpTrafficPortFlowPointHistoryMgmtFramesTx"),
        ("F3-PTP-MIB", "f3PtpTrafficPortFlowPointHistoryPtpUnknownsRx"),
        ("F3-PTP-MIB", "f3PtpTrafficPortFlowPointHistoryPtpUnknownsTx"),
        ("F3-PTP-MIB", "f3PtpTrafficPortFlowPointHistoryMinSyncResTime"),
        ("F3-PTP-MIB", "f3PtpTrafficPortFlowPointHistoryMaxSyncResTime"),
        ("F3-PTP-MIB", "f3PtpTrafficPortFlowPointHistoryAvgSyncResTime"),
        ("F3-PTP-MIB", "f3PtpTrafficPortFlowPointHistoryMinDelayReqResTime"),
        ("F3-PTP-MIB", "f3PtpTrafficPortFlowPointHistoryMaxDelayReqResTime"),
        ("F3-PTP-MIB", "f3PtpTrafficPortFlowPointHistoryAvgDelayReqResTime"),
        ("F3-PTP-MIB", "f3PtpTrafficPortFlowPointHistoryMinPDelayReqResTime"),
        ("F3-PTP-MIB", "f3PtpTrafficPortFlowPointHistoryMaxPDelayReqResTime"),
        ("F3-PTP-MIB", "f3PtpTrafficPortFlowPointHistoryAvgPDelayReqResTime"),
        ("F3-PTP-MIB", "f3PtpTrafficPortFlowPointHistoryMinPDelayRspResTime"),
        ("F3-PTP-MIB", "f3PtpTrafficPortFlowPointHistoryMaxPDelayRspResTime"),
        ("F3-PTP-MIB", "f3PtpTrafficPortFlowPointHistoryAvgPDelayRspResTime"),
        ("F3-PTP-MIB", "f3PtpTrafficPortFlowPointHistoryDestMciNoMatchDiscards"),
        ("F3-PTP-MIB", "f3PtpTrafficPortFlowPointHistoryTagNoMatchDiscards"),
        ("F3-PTP-MIB", "f3PtpTrafficPortFlowPointThresholdIndex"),
        ("F3-PTP-MIB", "f3PtpTrafficPortFlowPointThresholdInterval"),
        ("F3-PTP-MIB", "f3PtpTrafficPortFlowPointThresholdVariable"),
        ("F3-PTP-MIB", "f3PtpTrafficPortFlowPointThresholdValueLo"),
        ("F3-PTP-MIB", "f3PtpTrafficPortFlowPointThresholdValueHi"),
        ("F3-PTP-MIB", "f3PtpTrafficPortFlowPointThresholdMonValue"),
        ("F3-PTP-MIB", "f3PtpPTPPortStatsIndex"),
        ("F3-PTP-MIB", "f3PtpPTPPortStatsIntervalType"),
        ("F3-PTP-MIB", "f3PtpPTPPortStatsValid"),
        ("F3-PTP-MIB", "f3PtpPTPPortStatsAction"),
        ("F3-PTP-MIB", "f3PtpPTPPortStatsAvgAnnounceRate"),
        ("F3-PTP-MIB", "f3PtpPTPPortStatsAvgSyncRate"),
        ("F3-PTP-MIB", "f3PtpPTPPortStatsAvgDelayReqRate"),
        ("F3-PTP-MIB", "f3PtpPTPPortStatsAvgDelayRespRate"),
        ("F3-PTP-MIB", "f3PtpPTPPortStatsMismatchDomainDiscards"),
        ("F3-PTP-MIB", "f3PtpPTPPortStatsMessageWrongTypeDiscards"),
        ("F3-PTP-MIB", "f3PtpPTPPortStatsMessagesWrongLengthDiscards"),
        ("F3-PTP-MIB", "f3PtpPTPPortStatsUnknownMasterDiscards"),
        ("F3-PTP-MIB", "f3PtpPTPPortStatsMinOffsetFromMaster"),
        ("F3-PTP-MIB", "f3PtpPTPPortStatsMaxOffsetFromMaster"),
        ("F3-PTP-MIB", "f3PtpPTPPortStatsAvgOffsetFromMaster"),
        ("F3-PTP-MIB", "f3PtpPTPPortStatsMinSyncPathDelay"),
        ("F3-PTP-MIB", "f3PtpPTPPortStatsMaxSyncPathDelay"),
        ("F3-PTP-MIB", "f3PtpPTPPortStatsAvgSyncPathDelay"),
        ("F3-PTP-MIB", "f3PtpPTPPortStatsMinMeanPathDelay"),
        ("F3-PTP-MIB", "f3PtpPTPPortStatsMaxMeanPathDelay"),
        ("F3-PTP-MIB", "f3PtpPTPPortStatsAvgMeanPathDelay"),
        ("F3-PTP-MIB", "f3PtpPTPPortStatsMsgMiscDiscards"),
        ("F3-PTP-MIB", "f3PtpPTPPortHistoryIndex"),
        ("F3-PTP-MIB", "f3PtpPTPPortHistoryTime"),
        ("F3-PTP-MIB", "f3PtpPTPPortHistoryValid"),
        ("F3-PTP-MIB", "f3PtpPTPPortHistoryAction"),
        ("F3-PTP-MIB", "f3PtpPTPPortHistoryAvgAnnounceRate"),
        ("F3-PTP-MIB", "f3PtpPTPPortHistoryAvgSyncRate"),
        ("F3-PTP-MIB", "f3PtpPTPPortHistoryAvgDelayReqRate"),
        ("F3-PTP-MIB", "f3PtpPTPPortHistoryAvgDelayRespRate"),
        ("F3-PTP-MIB", "f3PtpPTPPortHistoryMismatchDomainDiscards"),
        ("F3-PTP-MIB", "f3PtpPTPPortHistoryMessageWrongTypeDiscards"),
        ("F3-PTP-MIB", "f3PtpPTPPortHistoryMessagesWrongLengthDiscards"),
        ("F3-PTP-MIB", "f3PtpPTPPortHistoryUnknownMasterDiscards"),
        ("F3-PTP-MIB", "f3PtpPTPPortHistoryMinOffsetFromMaster"),
        ("F3-PTP-MIB", "f3PtpPTPPortHistoryMaxOffsetFromMaster"),
        ("F3-PTP-MIB", "f3PtpPTPPortHistoryAvgOffsetFromMaster"),
        ("F3-PTP-MIB", "f3PtpPTPPortHistoryMinSyncPathDelay"),
        ("F3-PTP-MIB", "f3PtpPTPPortHistoryMaxSyncPathDelay"),
        ("F3-PTP-MIB", "f3PtpPTPPortHistoryAvgSyncPathDelay"),
        ("F3-PTP-MIB", "f3PtpPTPPortHistoryMinMeanPathDelay"),
        ("F3-PTP-MIB", "f3PtpPTPPortHistoryMaxMeanPathDelay"),
        ("F3-PTP-MIB", "f3PtpPTPPortHistoryAvgMeanPathDelay"),
        ("F3-PTP-MIB", "f3PtpPTPPortHistoryMsgMiscDiscards"),
        ("F3-PTP-MIB", "f3PtpPTPPortThresholdIndex"),
        ("F3-PTP-MIB", "f3PtpPTPPortThresholdInterval"),
        ("F3-PTP-MIB", "f3PtpPTPPortThresholdVariable"),
        ("F3-PTP-MIB", "f3PtpPTPPortThresholdValueLo"),
        ("F3-PTP-MIB", "f3PtpPTPPortThresholdValueHi"),
        ("F3-PTP-MIB", "f3PtpPTPPortThresholdMonValue"),
        ("F3-PTP-MIB", "f3PtpL3PTPPortStatsIndex"),
        ("F3-PTP-MIB", "f3PtpL3PTPPortStatsIntervalType"),
        ("F3-PTP-MIB", "f3PtpL3PTPPortStatsValid"),
        ("F3-PTP-MIB", "f3PtpL3PTPPortStatsAction"),
        ("F3-PTP-MIB", "f3PtpL3PTPPortStatsAvgAnnounceRate"),
        ("F3-PTP-MIB", "f3PtpL3PTPPortStatsAvgSyncRate"),
        ("F3-PTP-MIB", "f3PtpL3PTPPortStatsAvgDelayReqRate"),
        ("F3-PTP-MIB", "f3PtpL3PTPPortStatsAvgDelayRespRate"),
        ("F3-PTP-MIB", "f3PtpL3PTPPortStatsMismatchDomainDiscards"),
        ("F3-PTP-MIB", "f3PtpL3PTPPortStatsMessageWrongTypeDiscards"),
        ("F3-PTP-MIB", "f3PtpL3PTPPortStatsMessagesWrongLengthDiscards"),
        ("F3-PTP-MIB", "f3PtpL3PTPPortStatsUnknownMasterDiscards"),
        ("F3-PTP-MIB", "f3PtpL3PTPPortStatsMinOffsetFromMaster"),
        ("F3-PTP-MIB", "f3PtpL3PTPPortStatsMaxOffsetFromMaster"),
        ("F3-PTP-MIB", "f3PtpL3PTPPortStatsAvgOffsetFromMaster"),
        ("F3-PTP-MIB", "f3PtpL3PTPPortStatsMinSyncPathDelay"),
        ("F3-PTP-MIB", "f3PtpL3PTPPortStatsMaxSyncPathDelay"),
        ("F3-PTP-MIB", "f3PtpL3PTPPortStatsAvgSyncPathDelay"),
        ("F3-PTP-MIB", "f3PtpL3PTPPortStatsMinMeanPathDelay"),
        ("F3-PTP-MIB", "f3PtpL3PTPPortStatsMaxMeanPathDelay"),
        ("F3-PTP-MIB", "f3PtpL3PTPPortStatsAvgMeanPathDelay"),
        ("F3-PTP-MIB", "f3PtpL3PTPPortStatsMsgMiscDiscards"),
        ("F3-PTP-MIB", "f3PtpL3PTPPortHistoryIndex"),
        ("F3-PTP-MIB", "f3PtpL3PTPPortHistoryTime"),
        ("F3-PTP-MIB", "f3PtpL3PTPPortHistoryValid"),
        ("F3-PTP-MIB", "f3PtpL3PTPPortHistoryAction"),
        ("F3-PTP-MIB", "f3PtpL3PTPPortHistoryAvgAnnounceRate"),
        ("F3-PTP-MIB", "f3PtpL3PTPPortHistoryAvgSyncRate"),
        ("F3-PTP-MIB", "f3PtpL3PTPPortHistoryAvgDelayReqRate"),
        ("F3-PTP-MIB", "f3PtpL3PTPPortHistoryAvgDelayRespRate"),
        ("F3-PTP-MIB", "f3PtpL3PTPPortHistoryMismatchDomainDiscards"),
        ("F3-PTP-MIB", "f3PtpL3PTPPortHistoryMessageWrongTypeDiscards"),
        ("F3-PTP-MIB", "f3PtpL3PTPPortHistoryMessagesWrongLengthDiscards"),
        ("F3-PTP-MIB", "f3PtpL3PTPPortHistoryUnknownMasterDiscards"),
        ("F3-PTP-MIB", "f3PtpL3PTPPortHistoryMinOffsetFromMaster"),
        ("F3-PTP-MIB", "f3PtpL3PTPPortHistoryMaxOffsetFromMaster"),
        ("F3-PTP-MIB", "f3PtpL3PTPPortHistoryAvgOffsetFromMaster"),
        ("F3-PTP-MIB", "f3PtpL3PTPPortHistoryMinSyncPathDelay"),
        ("F3-PTP-MIB", "f3PtpL3PTPPortHistoryMaxSyncPathDelay"),
        ("F3-PTP-MIB", "f3PtpL3PTPPortHistoryAvgSyncPathDelay"),
        ("F3-PTP-MIB", "f3PtpL3PTPPortHistoryMinMeanPathDelay"),
        ("F3-PTP-MIB", "f3PtpL3PTPPortHistoryMaxMeanPathDelay"),
        ("F3-PTP-MIB", "f3PtpL3PTPPortHistoryAvgMeanPathDelay"),
        ("F3-PTP-MIB", "f3PtpL3PTPPortHistoryMsgMiscDiscards"),
        ("F3-PTP-MIB", "f3PtpL3PTPPortThresholdIndex"),
        ("F3-PTP-MIB", "f3PtpL3PTPPortThresholdInterval"),
        ("F3-PTP-MIB", "f3PtpL3PTPPortThresholdVariable"),
        ("F3-PTP-MIB", "f3PtpL3PTPPortThresholdValueLo"),
        ("F3-PTP-MIB", "f3PtpL3PTPPortThresholdValueHi"),
        ("F3-PTP-MIB", "f3PtpL3PTPPortThresholdMonValue"),
        ("F3-PTP-MIB", "f3PtpPTPClockStatsIndex"),
        ("F3-PTP-MIB", "f3PtpPTPClockStatsIntervalType"),
        ("F3-PTP-MIB", "f3PtpPTPClockStatsValid"),
        ("F3-PTP-MIB", "f3PtpPTPClockStatsAction"),
        ("F3-PTP-MIB", "f3PtpPTPClockStatsMinOffsetFromMaster"),
        ("F3-PTP-MIB", "f3PtpPTPClockStatsMaxOffsetFromMaster"),
        ("F3-PTP-MIB", "f3PtpPTPClockStatsAvgOffsetFromMaster"),
        ("F3-PTP-MIB", "f3PtpPTPClockStatsMinSyncPathDelay"),
        ("F3-PTP-MIB", "f3PtpPTPClockStatsMaxSyncPathDelay"),
        ("F3-PTP-MIB", "f3PtpPTPClockStatsAvgSyncPathDelay"),
        ("F3-PTP-MIB", "f3PtpPTPClockStatsMinMeanPathDelay"),
        ("F3-PTP-MIB", "f3PtpPTPClockStatsMaxMeanPathDelay"),
        ("F3-PTP-MIB", "f3PtpPTPClockStatsAvgMeanPathDelay"),
        ("F3-PTP-MIB", "f3PtpPTPClockHistoryIndex"),
        ("F3-PTP-MIB", "f3PtpPTPClockHistoryTime"),
        ("F3-PTP-MIB", "f3PtpPTPClockHistoryValid"),
        ("F3-PTP-MIB", "f3PtpPTPClockHistoryAction"),
        ("F3-PTP-MIB", "f3PtpPTPClockHistoryMinOffsetFromMaster"),
        ("F3-PTP-MIB", "f3PtpPTPClockHistoryMaxOffsetFromMaster"),
        ("F3-PTP-MIB", "f3PtpPTPClockHistoryAvgOffsetFromMaster"),
        ("F3-PTP-MIB", "f3PtpPTPClockHistoryMinSyncPathDelay"),
        ("F3-PTP-MIB", "f3PtpPTPClockHistoryMaxSyncPathDelay"),
        ("F3-PTP-MIB", "f3PtpPTPClockHistoryAvgSyncPathDelay"),
        ("F3-PTP-MIB", "f3PtpPTPClockHistoryMinMeanPathDelay"),
        ("F3-PTP-MIB", "f3PtpPTPClockHistoryMaxMeanPathDelay"),
        ("F3-PTP-MIB", "f3PtpPTPClockHistoryAvgMeanPathDelay"),
        ("F3-PTP-MIB", "f3PtpPTPClockThresholdIndex"),
        ("F3-PTP-MIB", "f3PtpPTPClockThresholdInterval"),
        ("F3-PTP-MIB", "f3PtpPTPClockThresholdVariable"),
        ("F3-PTP-MIB", "f3PtpPTPClockThresholdValueLo"),
        ("F3-PTP-MIB", "f3PtpPTPClockThresholdValueHi"),
        ("F3-PTP-MIB", "f3PtpPTPClockThresholdMonValue"))
)
if mibBuilder.loadTexts:
    f3PtpPerfObjectGroup.setStatus("current")

f3PtpBoundaryClockObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 4, 2, 5)
)
f3PtpBoundaryClockObjectGroup.setObjects(
      *(("F3-PTP-MIB", "f3PtpBCAlias"),
        ("F3-PTP-MIB", "f3PtpBCAdminState"),
        ("F3-PTP-MIB", "f3PtpBCOperationalState"),
        ("F3-PTP-MIB", "f3PtpBCSecondaryState"),
        ("F3-PTP-MIB", "f3PtpBCClockIdentity"),
        ("F3-PTP-MIB", "f3PtpBCTimingSource"),
        ("F3-PTP-MIB", "f3PtpBCClockClass"),
        ("F3-PTP-MIB", "f3PtpBCDomainNumber"),
        ("F3-PTP-MIB", "f3PtpBCStorageType"),
        ("F3-PTP-MIB", "f3PtpBCRowStatus"),
        ("F3-PTP-MIB", "f3PtpBCMediationControl"),
        ("F3-PTP-MIB", "f3PtpMasterClockIndex"),
        ("F3-PTP-MIB", "f3PtpMasterClockAlias"),
        ("F3-PTP-MIB", "f3PtpMasterClockAdminState"),
        ("F3-PTP-MIB", "f3PtpMasterClockOperationalState"),
        ("F3-PTP-MIB", "f3PtpMasterClockSecondaryState"),
        ("F3-PTP-MIB", "f3PtpMasterClockClockIdentity"),
        ("F3-PTP-MIB", "f3PtpMasterClockTimeClock"),
        ("F3-PTP-MIB", "f3PtpMasterClockClockClass"),
        ("F3-PTP-MIB", "f3PtpMasterClockDomainNumber"),
        ("F3-PTP-MIB", "f3PtpMasterClockPriority1"),
        ("F3-PTP-MIB", "f3PtpMasterClockPriority2"),
        ("F3-PTP-MIB", "f3PtpMasterClockClockAccuracy"),
        ("F3-PTP-MIB", "f3PtpMasterClockTimeScale"),
        ("F3-PTP-MIB", "f3PtpMasterClockUtcOffset"),
        ("F3-PTP-MIB", "f3PtpMasterClockStorageType"),
        ("F3-PTP-MIB", "f3PtpMasterClockRowStatus"),
        ("F3-PTP-MIB", "f3PtpMasterClockActiveTimeRef"),
        ("F3-PTP-MIB", "f3PtpMasterClockPTPProfile"),
        ("F3-PTP-MIB", "f3PtpMasterClockServiceAvailableTime"),
        ("F3-PTP-MIB", "f3PtpMasterClockServiceUnavailableTime"),
        ("F3-PTP-MIB", "f3PtpMasterClockServiceAvailablePercentage"),
        ("F3-PTP-MIB", "f3PtpMasterClockSmpteSystemFrameRateNumerator"),
        ("F3-PTP-MIB", "f3PtpMasterClockSmpteSystemFrameRateDenominator"),
        ("F3-PTP-MIB", "f3PtpMasterClockSmpteTimeAddressFlags"),
        ("F3-PTP-MIB", "f3PtpMCIAlias"),
        ("F3-PTP-MIB", "f3PtpMCIAdminState"),
        ("F3-PTP-MIB", "f3PtpMCIOperationalState"),
        ("F3-PTP-MIB", "f3PtpMCISecondaryState"),
        ("F3-PTP-MIB", "f3PtpMCIPortIdentity"),
        ("F3-PTP-MIB", "f3PtpMCIDomainNumber"),
        ("F3-PTP-MIB", "f3PtpMCIClockType"),
        ("F3-PTP-MIB", "f3PtpMCIDelayMechanism"),
        ("F3-PTP-MIB", "f3PtpMCIIfName"),
        ("F3-PTP-MIB", "f3PtpMCIIpProtocol"),
        ("F3-PTP-MIB", "f3PtpMCIMasterIpV4Address"),
        ("F3-PTP-MIB", "f3PtpMCIMasterIpV4SubnetMask"),
        ("F3-PTP-MIB", "f3PtpMCIIpPriorityMapMode"),
        ("F3-PTP-MIB", "f3PtpMCIIpPriority"),
        ("F3-PTP-MIB", "f3PtpMCIMaxLeaseDuration"),
        ("F3-PTP-MIB", "f3PtpMCIMaxSlavesSupported"),
        ("F3-PTP-MIB", "f3PtpMCIMaxStaticSlavesSupported"),
        ("F3-PTP-MIB", "f3PtpMCIMaxSyncMsgRate"),
        ("F3-PTP-MIB", "f3PtpMCIMaxDelayRespMsgRate"),
        ("F3-PTP-MIB", "f3PtpMCIMaxAnnounceMsgRate"),
        ("F3-PTP-MIB", "f3PtpMCIStorageType"),
        ("F3-PTP-MIB", "f3PtpMCIRowStatus"),
        ("F3-PTP-MIB", "f3PtpMCIServiceFlow"),
        ("F3-PTP-MIB", "f3PtpMCIClockClassProfile"),
        ("F3-PTP-MIB", "f3PtpMCIClockClass"),
        ("F3-PTP-MIB", "f3PtpMCIAnnounceExtTLVEnable"),
        ("F3-PTP-MIB", "f3PtpMCIPtpTransport"),
        ("F3-PTP-MIB", "f3PtpMCIPtpTransportMode"),
        ("F3-PTP-MIB", "f3PtpMCIPtpRemoteSlaveAgingTimeout"),
        ("F3-PTP-MIB", "f3PtpMCIMasterIpV6Address"),
        ("F3-PTP-MIB", "f3PtpMCIMasterIpV6AddrPrefixLength"),
        ("F3-PTP-MIB", "f3PtpMCIDefaultGatewayControl"),
        ("F3-PTP-MIB", "f3PtpMCIGateway"),
        ("F3-PTP-MIB", "f3PtpMCIIpV6Gateway"),
        ("F3-PTP-MIB", "f3PtpMasterVirtualPortAlias"),
        ("F3-PTP-MIB", "f3PtpMasterVirtualPortAdminState"),
        ("F3-PTP-MIB", "f3PtpMasterVirtualPortOperationalState"),
        ("F3-PTP-MIB", "f3PtpMasterVirtualPortSecondaryState"),
        ("F3-PTP-MIB", "f3PtpMasterVirtualPortFlowPoint"),
        ("F3-PTP-MIB", "f3PtpMasterVirtualPortStorageType"),
        ("F3-PTP-MIB", "f3PtpMasterVirtualPortRowStatus"),
        ("F3-PTP-MIB", "f3PtpStaticRemoteSlaveAlias"),
        ("F3-PTP-MIB", "f3PtpStaticRemoteSlaveAdminState"),
        ("F3-PTP-MIB", "f3PtpStaticRemoteSlaveOperationalState"),
        ("F3-PTP-MIB", "f3PtpStaticRemoteSlaveSecondaryState"),
        ("F3-PTP-MIB", "f3PtpStaticRemoteSlaveClockIdentity"),
        ("F3-PTP-MIB", "f3PtpStaticRemoteSlaveIpV4Address"),
        ("F3-PTP-MIB", "f3PtpStaticRemoteSlaveTimeCreated"),
        ("F3-PTP-MIB", "f3PtpStaticRemoteSlaveSyncMsgRate"),
        ("F3-PTP-MIB", "f3PtpStaticRemoteSlaveDelayRspMsgRate"),
        ("F3-PTP-MIB", "f3PtpStaticRemoteSlaveAnnounceMsgRate"),
        ("F3-PTP-MIB", "f3PtpStaticRemoteSlaveNegSyncLeaseDur"),
        ("F3-PTP-MIB", "f3PtpStaticRemoteSlaveNegDelayRspLeaseDur"),
        ("F3-PTP-MIB", "f3PtpStaticRemoteSlaveNegAnnounceLeaseDur"),
        ("F3-PTP-MIB", "f3PtpStaticRemoteSlaveSyncDurRemTime"),
        ("F3-PTP-MIB", "f3PtpStaticRemoteSlaveDelayRspDurRemTime"),
        ("F3-PTP-MIB", "f3PtpStaticRemoteSlaveAnnounceDurRemTime"),
        ("F3-PTP-MIB", "f3PtpStaticRemoteSlaveUmnControl"),
        ("F3-PTP-MIB", "f3PtpStaticRemoteSlaveStorageType"),
        ("F3-PTP-MIB", "f3PtpStaticRemoteSlaveRowStatus"),
        ("F3-PTP-MIB", "f3PtpStaticRemoteSlaveIpV6Address"),
        ("F3-PTP-MIB", "f3PtpDynamicRemoteSlaveAlias"),
        ("F3-PTP-MIB", "f3PtpDynamicRemoteSlaveAdminState"),
        ("F3-PTP-MIB", "f3PtpDynamicRemoteSlaveOperationalState"),
        ("F3-PTP-MIB", "f3PtpDynamicRemoteSlaveSecondaryState"),
        ("F3-PTP-MIB", "f3PtpDynamicRemoteSlaveClockIdentity"),
        ("F3-PTP-MIB", "f3PtpDynamicRemoteSlaveIpV4Address"),
        ("F3-PTP-MIB", "f3PtpDynamicRemoteSlaveTimeCreated"),
        ("F3-PTP-MIB", "f3PtpDynamicRemoteSlaveSyncMsgRate"),
        ("F3-PTP-MIB", "f3PtpDynamicRemoteSlaveDelayRspMsgRate"),
        ("F3-PTP-MIB", "f3PtpDynamicRemoteSlaveAnnounceMsgRate"),
        ("F3-PTP-MIB", "f3PtpDynamicRemoteSlaveNegSyncLeaseDur"),
        ("F3-PTP-MIB", "f3PtpDynamicRemoteSlaveNegDelayRspLeaseDur"),
        ("F3-PTP-MIB", "f3PtpDynamicRemoteSlaveNegAnnounceLeaseDur"),
        ("F3-PTP-MIB", "f3PtpDynamicRemoteSlaveSyncDurRemTime"),
        ("F3-PTP-MIB", "f3PtpDynamicRemoteSlaveDelayRspDurRemTime"),
        ("F3-PTP-MIB", "f3PtpDynamicRemoteSlaveAnnounceDurRemTime"),
        ("F3-PTP-MIB", "f3PtpDynamicRemoteSlaveRowStatus"),
        ("F3-PTP-MIB", "f3PtpDynamicRemoteSlaveStorageType"),
        ("F3-PTP-MIB", "f3PtpDynamicRemoteSlavePortIdentity"),
        ("F3-PTP-MIB", "f3PtpDynamicRemoteSlavePeerMacAddress"),
        ("F3-PTP-MIB", "f3PtpDynamicRemoteSlaveIpV6Address"),
        ("F3-PTP-MIB", "f3PtpMCIStatsIntervalType"),
        ("F3-PTP-MIB", "f3PtpMCIStatsValid"),
        ("F3-PTP-MIB", "f3PtpMCIStatsAction"),
        ("F3-PTP-MIB", "f3PtpMCIStatsPtpDiscards"),
        ("F3-PTP-MIB", "f3PtpMCIStatsSyncDeniedEvents"),
        ("F3-PTP-MIB", "f3PtpMCIStatsDelayRspDeniedEvents"),
        ("F3-PTP-MIB", "f3PtpMCIStatsAnnounceDeniedEvents"),
        ("F3-PTP-MIB", "f3PtpMCIStatsSyncCancelledEvents"),
        ("F3-PTP-MIB", "f3PtpMCIStatsDelayRspCancelledEvents"),
        ("F3-PTP-MIB", "f3PtpMCIStatsAnnounceCancelledEvents"),
        ("F3-PTP-MIB", "f3PtpMCIStatsDynamicSlavesLearnt"),
        ("F3-PTP-MIB", "f3PtpMCIStatsDynamicSlavesDropped"),
        ("F3-PTP-MIB", "f3PtpMCIHistoryIndex"),
        ("F3-PTP-MIB", "f3PtpTSHistoryTime"),
        ("F3-PTP-MIB", "f3PtpMCIHistoryValid"),
        ("F3-PTP-MIB", "f3PtpMCIHistoryAction"),
        ("F3-PTP-MIB", "f3PtpMCIHistoryPtpDiscards"),
        ("F3-PTP-MIB", "f3PtpMCIHistorySyncDeniedEvents"),
        ("F3-PTP-MIB", "f3PtpMCIHistoryDelayRspDeniedEvents"),
        ("F3-PTP-MIB", "f3PtpMCIHistoryAnnounceDeniedEvents"),
        ("F3-PTP-MIB", "f3PtpMCIHistorySyncCancelledEvents"),
        ("F3-PTP-MIB", "f3PtpMCIHistoryDelayRspCancelledEvents"),
        ("F3-PTP-MIB", "f3PtpMCIHistoryAnnounceCancelledEvents"),
        ("F3-PTP-MIB", "f3PtpMCIHistoryDynamicSlavesLearnt"),
        ("F3-PTP-MIB", "f3PtpMCIHistoryDynamicSlavesDropped"),
        ("F3-PTP-MIB", "f3PtpMCIThresholdInterval"),
        ("F3-PTP-MIB", "f3PtpMCIThresholdVariable"),
        ("F3-PTP-MIB", "f3PtpMCIThresholdValueLo"),
        ("F3-PTP-MIB", "f3PtpMCIThresholdValueHi"),
        ("F3-PTP-MIB", "f3PtpMCIThresholdMonValue"),
        ("F3-PTP-MIB", "f3PtpRemoteSlaveStatsIntervalType"),
        ("F3-PTP-MIB", "f3PtpRemoteSlaveStatsValid"),
        ("F3-PTP-MIB", "f3PtpRemoteSlaveStatsAction"),
        ("F3-PTP-MIB", "f3PtpRemoteSlaveStatsSyncMsgsGen"),
        ("F3-PTP-MIB", "f3PtpRemoteSlaveStatsDelayRspMsgsGen"),
        ("F3-PTP-MIB", "f3PtpRemoteSlaveStatsAnnounceMsgsGen"),
        ("F3-PTP-MIB", "f3PtpRemoteSlaveStatsSignallingMsgsGen"),
        ("F3-PTP-MIB", "f3PtpRemoteSlaveStatsDelayReqMsgsRx"),
        ("F3-PTP-MIB", "f3PtpRemoteSlaveStatsSignallingMsgsRx"),
        ("F3-PTP-MIB", "f3PtpRemoteSlaveStatsDelayReqMsgsDropped"),
        ("F3-PTP-MIB", "f3PtpRemoteSlaveStatsInvalidTLVLenDiscards"),
        ("F3-PTP-MIB", "f3PtpRemoteSlaveStatsInvalidTLVTypeDiscards"),
        ("F3-PTP-MIB", "f3PtpRemoteSlaveStatsTimesSyncLeaseExp"),
        ("F3-PTP-MIB", "f3PtpRemoteSlaveStatsTimesDelayRspLeaseExp"),
        ("F3-PTP-MIB", "f3PtpRemoteSlaveStatsTimesAnnounceLeaseExp"),
        ("F3-PTP-MIB", "f3PtpRemoteSlaveHistoryTime"),
        ("F3-PTP-MIB", "f3PtpRemoteSlaveHistoryValid"),
        ("F3-PTP-MIB", "f3PtpRemoteSlaveHistoryAction"),
        ("F3-PTP-MIB", "f3PtpRemoteSlaveHistorySyncMsgsGen"),
        ("F3-PTP-MIB", "f3PtpRemoteSlaveHistoryDelayRspMsgsGen"),
        ("F3-PTP-MIB", "f3PtpRemoteSlaveHistoryAnnounceMsgsGen"),
        ("F3-PTP-MIB", "f3PtpRemoteSlaveHistorySignallingMsgsGen"),
        ("F3-PTP-MIB", "f3PtpRemoteSlaveHistoryDelayReqMsgsRx"),
        ("F3-PTP-MIB", "f3PtpRemoteSlaveHistorySignallingMsgsRx"),
        ("F3-PTP-MIB", "f3PtpRemoteSlaveHistoryDelayReqMsgsDropped"),
        ("F3-PTP-MIB", "f3PtpRemoteSlaveHistoryInvalidTLVLenDiscards"),
        ("F3-PTP-MIB", "f3PtpRemoteSlaveHistoryInvalidTLVTypeDiscards"),
        ("F3-PTP-MIB", "f3PtpRemoteSlaveHistoryTimesSyncLeaseExp"),
        ("F3-PTP-MIB", "f3PtpRemoteSlaveHistoryTimesDelayRspLeaseExp"),
        ("F3-PTP-MIB", "f3PtpRemoteSlaveHistoryTimesAnnounceLeaseExp"),
        ("F3-PTP-MIB", "f3PtpRemoteSlaveThresholdInterval"),
        ("F3-PTP-MIB", "f3PtpRemoteSlaveThresholdVariable"),
        ("F3-PTP-MIB", "f3PtpRemoteSlaveThresholdValueLo"),
        ("F3-PTP-MIB", "f3PtpRemoteSlaveThresholdValueHi"),
        ("F3-PTP-MIB", "f3PtpRemoteSlaveThresholdMonValue"))
)
if mibBuilder.loadTexts:
    f3PtpBoundaryClockObjectGroup.setStatus("current")

f3PtpProtObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 4, 2, 7)
)
f3PtpProtObjectGroup.setObjects(
      *(("F3-PTP-MIB", "f3PtpMCIProtGroupIndex"),
        ("F3-PTP-MIB", "f3PtpMCIProtGroupAdminState"),
        ("F3-PTP-MIB", "f3PtpMCIProtGroupActiveMember"),
        ("F3-PTP-MIB", "f3PtpMCIProtGroupLastSwitchOverTime"),
        ("F3-PTP-MIB", "f3PtpMCIProtGroupLastSwitchOverReason"),
        ("F3-PTP-MIB", "f3PtpMCIProtGroupStorageType"),
        ("F3-PTP-MIB", "f3PtpMCIProtGroupRowStatus"),
        ("F3-PTP-MIB", "f3PtpMCIProtMemberObject"),
        ("F3-PTP-MIB", "f3PtpMCIProtMemberStorageType"),
        ("F3-PTP-MIB", "f3PtpMCIProtMemberRowStatus"))
)
if mibBuilder.loadTexts:
    f3PtpProtObjectGroup.setStatus("current")


# Notification objects

f3PtpAccPortFlowPointThresholdCrossingAlert = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 3, 1)
)
f3PtpAccPortFlowPointThresholdCrossingAlert.setObjects(
      *(("F3-PTP-MIB", "f3PtpAccPortFlowPointThresholdIndex"),
        ("F3-PTP-MIB", "f3PtpAccPortFlowPointThresholdInterval"),
        ("F3-PTP-MIB", "f3PtpAccPortFlowPointThresholdVariable"),
        ("F3-PTP-MIB", "f3PtpAccPortFlowPointThresholdValueLo"),
        ("F3-PTP-MIB", "f3PtpAccPortFlowPointThresholdValueHi"),
        ("F3-PTP-MIB", "f3PtpAccPortFlowPointThresholdMonValue"))
)
if mibBuilder.loadTexts:
    f3PtpAccPortFlowPointThresholdCrossingAlert.setStatus(
        "current"
    )

f3PtpNetPortFlowPointThresholdCrossingAlert = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 3, 2)
)
f3PtpNetPortFlowPointThresholdCrossingAlert.setObjects(
      *(("F3-PTP-MIB", "f3PtpNetPortFlowPointThresholdIndex"),
        ("F3-PTP-MIB", "f3PtpNetPortFlowPointThresholdInterval"),
        ("F3-PTP-MIB", "f3PtpNetPortFlowPointThresholdVariable"),
        ("F3-PTP-MIB", "f3PtpNetPortFlowPointThresholdValueLo"),
        ("F3-PTP-MIB", "f3PtpNetPortFlowPointThresholdValueHi"),
        ("F3-PTP-MIB", "f3PtpNetPortFlowPointThresholdMonValue"))
)
if mibBuilder.loadTexts:
    f3PtpNetPortFlowPointThresholdCrossingAlert.setStatus(
        "current"
    )

f3PtpSOOCCrossingAlert = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 3, 3)
)
f3PtpSOOCCrossingAlert.setObjects(
      *(("F3-PTP-MIB", "f3PtpSOOCThresholdIndex"),
        ("F3-PTP-MIB", "f3PtpSOOCThresholdInterval"),
        ("F3-PTP-MIB", "f3PtpSOOCThresholdVariable"),
        ("F3-PTP-MIB", "f3PtpSOOCThresholdValueLo"),
        ("F3-PTP-MIB", "f3PtpSOOCThresholdValueHi"),
        ("F3-PTP-MIB", "f3PtpSOOCThresholdMonValue"))
)
if mibBuilder.loadTexts:
    f3PtpSOOCCrossingAlert.setStatus(
        "current"
    )

f3PtpTSCrossingAlert = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 3, 4)
)
f3PtpTSCrossingAlert.setObjects(
      *(("F3-PTP-MIB", "f3PtpTSThresholdIndex"),
        ("F3-PTP-MIB", "f3PtpTSThresholdInterval"),
        ("F3-PTP-MIB", "f3PtpTSThresholdVariable"),
        ("F3-PTP-MIB", "f3PtpTSThresholdValueLo"),
        ("F3-PTP-MIB", "f3PtpTSThresholdValueHi"),
        ("F3-PTP-MIB", "f3PtpTSThresholdMonValue"))
)
if mibBuilder.loadTexts:
    f3PtpTSCrossingAlert.setStatus(
        "current"
    )

f3PtpMCICrossingAlert = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 3, 5)
)
f3PtpMCICrossingAlert.setObjects(
      *(("F3-PTP-MIB", "f3PtpMCIThresholdIndex"),
        ("F3-PTP-MIB", "f3PtpMCIThresholdInterval"),
        ("F3-PTP-MIB", "f3PtpMCIThresholdVariable"),
        ("F3-PTP-MIB", "f3PtpMCIThresholdValueLo"),
        ("F3-PTP-MIB", "f3PtpMCIThresholdValueHi"),
        ("F3-PTP-MIB", "f3PtpMCIThresholdMonValue"))
)
if mibBuilder.loadTexts:
    f3PtpMCICrossingAlert.setStatus(
        "current"
    )

f3PtpRemoteSlaveCrossingAlert = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 3, 6)
)
f3PtpRemoteSlaveCrossingAlert.setObjects(
      *(("F3-PTP-MIB", "f3PtpRemoteSlaveThresholdIndex"),
        ("F3-PTP-MIB", "f3PtpRemoteSlaveThresholdInterval"),
        ("F3-PTP-MIB", "f3PtpRemoteSlaveThresholdVariable"),
        ("F3-PTP-MIB", "f3PtpRemoteSlaveThresholdValueLo"),
        ("F3-PTP-MIB", "f3PtpRemoteSlaveThresholdValueHi"),
        ("F3-PTP-MIB", "f3PtpRemoteSlaveThresholdMonValue"))
)
if mibBuilder.loadTexts:
    f3PtpRemoteSlaveCrossingAlert.setStatus(
        "current"
    )

f3PtpTrafficPortFlowPointThresholdCrossingAlert = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 3, 7)
)
f3PtpTrafficPortFlowPointThresholdCrossingAlert.setObjects(
      *(("F3-PTP-MIB", "f3PtpTrafficPortFlowPointThresholdIndex"),
        ("F3-PTP-MIB", "f3PtpTrafficPortFlowPointThresholdInterval"),
        ("F3-PTP-MIB", "f3PtpTrafficPortFlowPointThresholdVariable"),
        ("F3-PTP-MIB", "f3PtpTrafficPortFlowPointThresholdValueLo"),
        ("F3-PTP-MIB", "f3PtpTrafficPortFlowPointThresholdValueHi"),
        ("F3-PTP-MIB", "f3PtpTrafficPortFlowPointThresholdMonValue"))
)
if mibBuilder.loadTexts:
    f3PtpTrafficPortFlowPointThresholdCrossingAlert.setStatus(
        "current"
    )

f3PtpPTPPortCrossingAlert = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 3, 8)
)
f3PtpPTPPortCrossingAlert.setObjects(
      *(("F3-PTP-MIB", "f3PtpPTPPortThresholdIndex"),
        ("F3-PTP-MIB", "f3PtpPTPPortThresholdInterval"),
        ("F3-PTP-MIB", "f3PtpPTPPortThresholdVariable"),
        ("F3-PTP-MIB", "f3PtpPTPPortThresholdValueLo"),
        ("F3-PTP-MIB", "f3PtpPTPPortThresholdValueHi"),
        ("F3-PTP-MIB", "f3PtpPTPPortThresholdMonValue"))
)
if mibBuilder.loadTexts:
    f3PtpPTPPortCrossingAlert.setStatus(
        "current"
    )

f3PtpPTPClockCrossingAlert = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 3, 9)
)
f3PtpPTPClockCrossingAlert.setObjects(
      *(("F3-PTP-MIB", "f3PtpPTPClockThresholdIndex"),
        ("F3-PTP-MIB", "f3PtpPTPClockThresholdInterval"),
        ("F3-PTP-MIB", "f3PtpPTPClockThresholdVariable"),
        ("F3-PTP-MIB", "f3PtpPTPClockThresholdValueLo"),
        ("F3-PTP-MIB", "f3PtpPTPClockThresholdValueHi"),
        ("F3-PTP-MIB", "f3PtpPTPClockThresholdMonValue"))
)
if mibBuilder.loadTexts:
    f3PtpPTPClockCrossingAlert.setStatus(
        "current"
    )

f3PtpL3PTPPortCrossingAlert = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 3, 10)
)
f3PtpL3PTPPortCrossingAlert.setObjects(
      *(("F3-PTP-MIB", "f3PtpL3PTPPortThresholdIndex"),
        ("F3-PTP-MIB", "f3PtpL3PTPPortThresholdInterval"),
        ("F3-PTP-MIB", "f3PtpL3PTPPortThresholdVariable"),
        ("F3-PTP-MIB", "f3PtpL3PTPPortThresholdValueLo"),
        ("F3-PTP-MIB", "f3PtpL3PTPPortThresholdValueHi"),
        ("F3-PTP-MIB", "f3PtpL3PTPPortThresholdMonValue"))
)
if mibBuilder.loadTexts:
    f3PtpL3PTPPortCrossingAlert.setStatus(
        "current"
    )

f3PtpTSStatusChangeTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 5, 1)
)
f3PtpTSStatusChangeTrap.setObjects(
      *(("F3-PTP-MIB", "f3PtpTSAdminState"),
        ("F3-PTP-MIB", "f3PtpTSCurrentCRScore"),
        ("F3-PTP-MIB", "f3PtpTSCurrentPRScore"),
        ("F3-PTP-MIB", "f3PtpTSClockRecoveryState"),
        ("F3-PTP-MIB", "f3PtpTSSelectedPacketClock"))
)
if mibBuilder.loadTexts:
    f3PtpTSStatusChangeTrap.setStatus(
        "current"
    )

f3PtpMasterClockStatusChangeTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 5, 2)
)
f3PtpMasterClockStatusChangeTrap.setObjects(
      *(("F3-PTP-MIB", "f3PtpMasterClockClockClass"),
        ("F3-PTP-MIB", "f3PtpMasterClockUtcOffset"),
        ("F3-PTP-MIB", "f3PtpMasterClockActiveTimeRef"),
        ("F3-PTP-MIB", "f3PtpMasterClockPTPProfile"))
)
if mibBuilder.loadTexts:
    f3PtpMasterClockStatusChangeTrap.setStatus(
        "current"
    )

f3PtpBCStatusChangeTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 5, 3)
)
f3PtpBCStatusChangeTrap.setObjects(
    ("F3-PTP-MIB", "f3PtpBCClockClass")
)
if mibBuilder.loadTexts:
    f3PtpBCStatusChangeTrap.setStatus(
        "current"
    )

f3PtpDynamicRemoteSlaveStatusChangeTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 5, 4)
)
f3PtpDynamicRemoteSlaveStatusChangeTrap.setObjects(
      *(("F3-PTP-MIB", "f3PtpDynamicRemoteSlaveClockIdentity"),
        ("F3-PTP-MIB", "f3PtpDynamicRemoteSlaveIpV4Address"),
        ("F3-PTP-MIB", "f3PtpDynamicRemoteSlaveSyncMsgRate"),
        ("F3-PTP-MIB", "f3PtpDynamicRemoteSlaveDelayRspMsgRate"),
        ("F3-PTP-MIB", "f3PtpDynamicRemoteSlaveAnnounceMsgRate"))
)
if mibBuilder.loadTexts:
    f3PtpDynamicRemoteSlaveStatusChangeTrap.setStatus(
        "current"
    )


# Notifications groups

f3PtpPerfNotifGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 4, 2, 3)
)
f3PtpPerfNotifGroup.setObjects(
      *(("F3-PTP-MIB", "f3PtpAccPortFlowPointThresholdCrossingAlert"),
        ("F3-PTP-MIB", "f3PtpNetPortFlowPointThresholdCrossingAlert"),
        ("F3-PTP-MIB", "f3PtpSOOCCrossingAlert"),
        ("F3-PTP-MIB", "f3PtpTSCrossingAlert"),
        ("F3-PTP-MIB", "f3PtpPTPClockCrossingAlert"),
        ("F3-PTP-MIB", "f3PtpPTPPortCrossingAlert"),
        ("F3-PTP-MIB", "f3PtpL3PTPPortCrossingAlert"))
)
if mibBuilder.loadTexts:
    f3PtpPerfNotifGroup.setStatus(
        "current"
    )

f3PtpStatusChangeNotifGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 4, 2, 4)
)
f3PtpStatusChangeNotifGroup.setObjects(
    ("F3-PTP-MIB", "f3PtpTSStatusChangeTrap")
)
if mibBuilder.loadTexts:
    f3PtpStatusChangeNotifGroup.setStatus(
        "current"
    )

f3PtpBoundaryClockNotifGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 4, 2, 6)
)
f3PtpBoundaryClockNotifGroup.setObjects(
      *(("F3-PTP-MIB", "f3PtpMCICrossingAlert"),
        ("F3-PTP-MIB", "f3PtpRemoteSlaveCrossingAlert"),
        ("F3-PTP-MIB", "f3PtpMasterClockStatusChangeTrap"),
        ("F3-PTP-MIB", "f3PtpBCStatusChangeTrap"),
        ("F3-PTP-MIB", "f3PtpDynamicRemoteSlaveStatusChangeTrap"))
)
if mibBuilder.loadTexts:
    f3PtpBoundaryClockNotifGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

f3PtpCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 18, 4, 1, 1)
)
f3PtpCompliance.setObjects(
      *(("F3-PTP-MIB", "f3PtpObjectGroup"),
        ("F3-PTP-MIB", "f3PtpPerfObjectGroup"),
        ("F3-PTP-MIB", "f3PtpPerfNotifGroup"),
        ("F3-PTP-MIB", "f3PtpStatusChangeNotifGroup"))
)
if mibBuilder.loadTexts:
    f3PtpCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "F3-PTP-MIB",
    **{"SlaveMode": SlaveMode,
       "PtpFlowPointType": PtpFlowPointType,
       "PtpPortState": PtpPortState,
       "MasterClockType": MasterClockType,
       "PTPPortType": PTPPortType,
       "DelayMechanism": DelayMechanism,
       "ClockIdentity": ClockIdentity,
       "PortIdentity": PortIdentity,
       "ClockRecoveryMode": ClockRecoveryMode,
       "ClockRecoveryState": ClockRecoveryState,
       "AnnounceMsgRate": AnnounceMsgRate,
       "SyncMsgRate": SyncMsgRate,
       "DelayRespMsgRate": DelayRespMsgRate,
       "DelayReqMsgRate": DelayReqMsgRate,
       "FreqRecoveryTarget": FreqRecoveryTarget,
       "ScaledNanoseconds": ScaledNanoseconds,
       "RemoteSlaveType": RemoteSlaveType,
       "TimeScale": TimeScale,
       "PhaseRecoveryState": PhaseRecoveryState,
       "PTPProtectionState": PTPProtectionState,
       "CompensationMode": CompensationMode,
       "CompensationStatus": CompensationStatus,
       "PTPClockProfile": PTPClockProfile,
       "PTPClockType": PTPClockType,
       "PTPClockOperMode": PTPClockOperMode,
       "DestMacAddrType": DestMacAddrType,
       "AnnounceMessageRate": AnnounceMessageRate,
       "DelayReqMessageRate": DelayReqMessageRate,
       "SyncMessageRate": SyncMessageRate,
       "BMCARole": BMCARole,
       "ClockClassProfile": ClockClassProfile,
       "PTPProfile": PTPProfile,
       "PTPTransport": PTPTransport,
       "PTPTransportMode": PTPTransportMode,
       "ToggleValue": ToggleValue,
       "f3PtpMIB": f3PtpMIB,
       "f3PtpConfigObjects": f3PtpConfigObjects,
       "f3PtpTCTable": f3PtpTCTable,
       "f3PtpTCEntry": f3PtpTCEntry,
       "f3PtpTCIndex": f3PtpTCIndex,
       "f3PtpTCAlias": f3PtpTCAlias,
       "f3PtpTCAdminState": f3PtpTCAdminState,
       "f3PtpTCOperationalState": f3PtpTCOperationalState,
       "f3PtpTCSecondaryState": f3PtpTCSecondaryState,
       "f3PtpTCServiceFlow": f3PtpTCServiceFlow,
       "f3PtpTCDelayMechanism": f3PtpTCDelayMechanism,
       "f3PtpTCSync": f3PtpTCSync,
       "f3PtpTCClockIdentity": f3PtpTCClockIdentity,
       "f3PtpTCStorageType": f3PtpTCStorageType,
       "f3PtpTCRowStatus": f3PtpTCRowStatus,
       "f3PtpTCPtpProfile": f3PtpTCPtpProfile,
       "f3PtpTCVirtualPortTable": f3PtpTCVirtualPortTable,
       "f3PtpTCVirtualPortEntry": f3PtpTCVirtualPortEntry,
       "f3PtpTCVirtualPortIndex": f3PtpTCVirtualPortIndex,
       "f3PtpTCVirtualPortAlias": f3PtpTCVirtualPortAlias,
       "f3PtpTCVirtualPortAdminState": f3PtpTCVirtualPortAdminState,
       "f3PtpTCVirtualPortOperationalState": f3PtpTCVirtualPortOperationalState,
       "f3PtpTCVirtualPortSecondaryState": f3PtpTCVirtualPortSecondaryState,
       "f3PtpTCVirtualPortIdentity": f3PtpTCVirtualPortIdentity,
       "f3PtpTCVirtualPortFlowPoint": f3PtpTCVirtualPortFlowPoint,
       "f3PtpTCVirtualPortStorageType": f3PtpTCVirtualPortStorageType,
       "f3PtpTCVirtualPortRowStatus": f3PtpTCVirtualPortRowStatus,
       "f3PtpTSTable": f3PtpTSTable,
       "f3PtpTSEntry": f3PtpTSEntry,
       "f3PtpTSIndex": f3PtpTSIndex,
       "f3PtpTSAlias": f3PtpTSAlias,
       "f3PtpTSAdminState": f3PtpTSAdminState,
       "f3PtpTSOperationalState": f3PtpTSOperationalState,
       "f3PtpTSSecondaryState": f3PtpTSSecondaryState,
       "f3PtpTSClockIdentity": f3PtpTSClockIdentity,
       "f3PtpTSDomainNumber": f3PtpTSDomainNumber,
       "f3PtpTSSync": f3PtpTSSync,
       "f3PtpTSCurrentTOD": f3PtpTSCurrentTOD,
       "f3PtpTSSelectedPacketClock": f3PtpTSSelectedPacketClock,
       "f3PtpTSClockRecoveryMode": f3PtpTSClockRecoveryMode,
       "f3PtpTSClockRecoveryState": f3PtpTSClockRecoveryState,
       "f3PtpTSClockSyncEEnabled": f3PtpTSClockSyncEEnabled,
       "f3PtpTSClockQLModeEnabled": f3PtpTSClockQLModeEnabled,
       "f3PtpTSClockExpectedQL": f3PtpTSClockExpectedQL,
       "f3PtpTSClockAssumedQL": f3PtpTSClockAssumedQL,
       "f3PtpTSClockReceivedQL": f3PtpTSClockReceivedQL,
       "f3PtpTSStorageType": f3PtpTSStorageType,
       "f3PtpTSRowStatus": f3PtpTSRowStatus,
       "f3PtpTSTimeTraceabilityStatus": f3PtpTSTimeTraceabilityStatus,
       "f3PtpTSTimeSinceTimeTraceabilityChanged": f3PtpTSTimeSinceTimeTraceabilityChanged,
       "f3PtpTSFreqTraceabilityStatus": f3PtpTSFreqTraceabilityStatus,
       "f3PtpTSTimeSinceFreqTraceabilityChanged": f3PtpTSTimeSinceFreqTraceabilityChanged,
       "f3PtpTSFreqRecoveryTarget": f3PtpTSFreqRecoveryTarget,
       "f3PtpTSCurrentCRScore": f3PtpTSCurrentCRScore,
       "f3PtpTSTimeLastCRScore": f3PtpTSTimeLastCRScore,
       "f3PtpTSTargetPhaseRecoveryAccuracy": f3PtpTSTargetPhaseRecoveryAccuracy,
       "f3PtpTSCurrentPRScore": f3PtpTSCurrentPRScore,
       "f3PtpTSTimeLastPRScore": f3PtpTSTimeLastPRScore,
       "f3PtpTSClockClass": f3PtpTSClockClass,
       "f3PtpTSClockAccuracy": f3PtpTSClockAccuracy,
       "f3PtpTSTimeSource": f3PtpTSTimeSource,
       "f3PtpTSPhaseRecoveryState": f3PtpTSPhaseRecoveryState,
       "f3PtpTSTimeHoldoverAccuracy": f3PtpTSTimeHoldoverAccuracy,
       "f3PtpTSWtrTime": f3PtpTSWtrTime,
       "f3PtpSOOCTable": f3PtpSOOCTable,
       "f3PtpSOOCEntry": f3PtpSOOCEntry,
       "f3PtpSOOCIndex": f3PtpSOOCIndex,
       "f3PtpSOOCName": f3PtpSOOCName,
       "f3PtpSOOCAlias": f3PtpSOOCAlias,
       "f3PtpSOOCAdminState": f3PtpSOOCAdminState,
       "f3PtpSOOCOperationalState": f3PtpSOOCOperationalState,
       "f3PtpSOOCSecondaryState": f3PtpSOOCSecondaryState,
       "f3PtpSOOCServiceFlow": f3PtpSOOCServiceFlow,
       "f3PtpSOOCMasterClockType": f3PtpSOOCMasterClockType,
       "f3PtpSOOCUnicastMessageNegEnabled": f3PtpSOOCUnicastMessageNegEnabled,
       "f3PtpSOOCMasterDelayMechanism": f3PtpSOOCMasterDelayMechanism,
       "f3PtpSOOCMasterPriority": f3PtpSOOCMasterPriority,
       "f3PtpSOOCMasterIpProtocol": f3PtpSOOCMasterIpProtocol,
       "f3PtpSOOCSlaveIpV4Address": f3PtpSOOCSlaveIpV4Address,
       "f3PtpSOOCSlaveIpV4SubnetMask": f3PtpSOOCSlaveIpV4SubnetMask,
       "f3PtpSOOCMasterIpV4Address": f3PtpSOOCMasterIpV4Address,
       "f3PtpSOOCIpPriorityMapMode": f3PtpSOOCIpPriorityMapMode,
       "f3PtpSOOCIpPriority": f3PtpSOOCIpPriority,
       "f3PtpSOOCMasterLeaseDuration": f3PtpSOOCMasterLeaseDuration,
       "f3PtpSOOCMasterAnnounceMsgRate": f3PtpSOOCMasterAnnounceMsgRate,
       "f3PtpSOOCMasterAnnounceMsgReceiptTimeout": f3PtpSOOCMasterAnnounceMsgReceiptTimeout,
       "f3PtpSOOCMasterSyncMsgRate": f3PtpSOOCMasterSyncMsgRate,
       "f3PtpSOOCMasterSyncReceiptTimeout": f3PtpSOOCMasterSyncReceiptTimeout,
       "f3PtpSOOCMasterDelayRspMsgRate": f3PtpSOOCMasterDelayRspMsgRate,
       "f3PtpSOOCMasterDelayRspReceiptTimeout": f3PtpSOOCMasterDelayRspReceiptTimeout,
       "f3PtpSOOCMasterRequestUnicastTimeout": f3PtpSOOCMasterRequestUnicastTimeout,
       "f3PtpSOOCMasterRequestUnicastRestartTimer": f3PtpSOOCMasterRequestUnicastRestartTimer,
       "f3PtpSOOCCurrentOffsetFromMaster": f3PtpSOOCCurrentOffsetFromMaster,
       "f3PtpSOOCAnnounceMsgClockClass": f3PtpSOOCAnnounceMsgClockClass,
       "f3PtpSOOCLastReceivedAnnounceMsg": f3PtpSOOCLastReceivedAnnounceMsg,
       "f3PtpSOOCLastReceivedSyncMsg": f3PtpSOOCLastReceivedSyncMsg,
       "f3PtpSOOCLastReceivedDelayRspMsg": f3PtpSOOCLastReceivedDelayRspMsg,
       "f3PtpSOOCRecentMeanPathDelay": f3PtpSOOCRecentMeanPathDelay,
       "f3PtpSOOCRecentSyncPDV": f3PtpSOOCRecentSyncPDV,
       "f3PtpSOOCStorageType": f3PtpSOOCStorageType,
       "f3PtpSOOCRowStatus": f3PtpSOOCRowStatus,
       "f3PtpSOOCRecentSyncPathDelay": f3PtpSOOCRecentSyncPathDelay,
       "f3PtpSOOCSoocProtectionState": f3PtpSOOCSoocProtectionState,
       "f3PtpSOOCSoocWtr": f3PtpSOOCSoocWtr,
       "f3PtpSOOCSoocClockClass": f3PtpSOOCSoocClockClass,
       "f3PtpSOOCSoocClockRecoveryState": f3PtpSOOCSoocClockRecoveryState,
       "f3PtpSOOCSoocPhaseRecoveryState": f3PtpSOOCSoocPhaseRecoveryState,
       "f3PtpSOOCE2eDelayAsymmetryComp": f3PtpSOOCE2eDelayAsymmetryComp,
       "f3PtpSOOCE2eAutoAsymmetryCompStatus": f3PtpSOOCE2eAutoAsymmetryCompStatus,
       "f3PtpSOOCE2eDelayAsymmetry": f3PtpSOOCE2eDelayAsymmetry,
       "f3PtpSOOCSoocLockOutControl": f3PtpSOOCSoocLockOutControl,
       "f3PtpSOOCSlaveIpV6Address": f3PtpSOOCSlaveIpV6Address,
       "f3PtpSOOCSlaveIpV6AddrPrefixLength": f3PtpSOOCSlaveIpV6AddrPrefixLength,
       "f3PtpSOOCMasterIpV6Address": f3PtpSOOCMasterIpV6Address,
       "f3PtpSOOCMinimumExpectedClockClass": f3PtpSOOCMinimumExpectedClockClass,
       "f3PtpSOOCMasterMessageMode": f3PtpSOOCMasterMessageMode,
       "f3PtpSOOCDefaultGatewayControl": f3PtpSOOCDefaultGatewayControl,
       "f3PtpSOOCGateway": f3PtpSOOCGateway,
       "f3PtpSOOCIpV6Gateway": f3PtpSOOCIpV6Gateway,
       "f3PtpSOOCAlgorithmPtpAware": f3PtpSOOCAlgorithmPtpAware,
       "f3PtpOCSlaveVirtualPortTable": f3PtpOCSlaveVirtualPortTable,
       "f3PtpOCSlaveVirtualPortEntry": f3PtpOCSlaveVirtualPortEntry,
       "f3PtpOCSlaveVirtualPortIndex": f3PtpOCSlaveVirtualPortIndex,
       "f3PtpOCSlaveVirtualPortAlias": f3PtpOCSlaveVirtualPortAlias,
       "f3PtpOCSlaveVirtualPortAdminState": f3PtpOCSlaveVirtualPortAdminState,
       "f3PtpOCSlaveVirtualPortOperationalState": f3PtpOCSlaveVirtualPortOperationalState,
       "f3PtpOCSlaveVirtualPortSecondaryState": f3PtpOCSlaveVirtualPortSecondaryState,
       "f3PtpOCSlaveVirtualPortIdentity": f3PtpOCSlaveVirtualPortIdentity,
       "f3PtpOCSlaveVirtualPortFlowPoint": f3PtpOCSlaveVirtualPortFlowPoint,
       "f3PtpOCSlaveVirtualPortState": f3PtpOCSlaveVirtualPortState,
       "f3PtpOCSlaveVirtualPortStorageType": f3PtpOCSlaveVirtualPortStorageType,
       "f3PtpOCSlaveVirtualPortRowStatus": f3PtpOCSlaveVirtualPortRowStatus,
       "f3PtpAccPortFlowPointTable": f3PtpAccPortFlowPointTable,
       "f3PtpAccPortFlowPointEntry": f3PtpAccPortFlowPointEntry,
       "f3PtpAccPortFlowPointIndex": f3PtpAccPortFlowPointIndex,
       "f3PtpAccPortFlowPointAlias": f3PtpAccPortFlowPointAlias,
       "f3PtpAccPortFlowPointAdminState": f3PtpAccPortFlowPointAdminState,
       "f3PtpAccPortFlowPointOperationalState": f3PtpAccPortFlowPointOperationalState,
       "f3PtpAccPortFlowPointSecondaryState": f3PtpAccPortFlowPointSecondaryState,
       "f3PtpAccPortFlowPointType": f3PtpAccPortFlowPointType,
       "f3PtpAccPortFlowPointClock": f3PtpAccPortFlowPointClock,
       "f3PtpAccPortFlowPointService": f3PtpAccPortFlowPointService,
       "f3PtpAccPortFlowPointOuterVlanEtherType": f3PtpAccPortFlowPointOuterVlanEtherType,
       "f3PtpAccPortFlowPointOuterVlanMemberList": f3PtpAccPortFlowPointOuterVlanMemberList,
       "f3PtpAccPortFlowPointOuterUntaggedEnabled": f3PtpAccPortFlowPointOuterUntaggedEnabled,
       "f3PtpAccPortFlowPointInner1VlanEtherType": f3PtpAccPortFlowPointInner1VlanEtherType,
       "f3PtpAccPortFlowPointInner1VlanMemberList": f3PtpAccPortFlowPointInner1VlanMemberList,
       "f3PtpAccPortFlowPointInner1UntaggedEnabled": f3PtpAccPortFlowPointInner1UntaggedEnabled,
       "f3PtpAccPortFlowPointInner2VlanEtherType": f3PtpAccPortFlowPointInner2VlanEtherType,
       "f3PtpAccPortFlowPointInner2VlanMemberList": f3PtpAccPortFlowPointInner2VlanMemberList,
       "f3PtpAccPortFlowPointInner2UntaggedEnabled": f3PtpAccPortFlowPointInner2UntaggedEnabled,
       "f3PtpAccPortFlowPointStorageType": f3PtpAccPortFlowPointStorageType,
       "f3PtpAccPortFlowPointRowStatus": f3PtpAccPortFlowPointRowStatus,
       "f3PtpAccPortFlowPointCOS": f3PtpAccPortFlowPointCOS,
       "f3PtpAccPortFlowPointCIRLo": f3PtpAccPortFlowPointCIRLo,
       "f3PtpAccPortFlowPointCIRHi": f3PtpAccPortFlowPointCIRHi,
       "f3PtpAccPortFlowPointEIRLo": f3PtpAccPortFlowPointEIRLo,
       "f3PtpAccPortFlowPointEIRHi": f3PtpAccPortFlowPointEIRHi,
       "f3PtpAccPortFlowPointBufferSize": f3PtpAccPortFlowPointBufferSize,
       "f3PtpAccPortFlowPointLoopAvoidance": f3PtpAccPortFlowPointLoopAvoidance,
       "f3PtpAccPortFlowPointRefConnectGuardFlow": f3PtpAccPortFlowPointRefConnectGuardFlow,
       "f3PtpAccPortFlowPointSecureState": f3PtpAccPortFlowPointSecureState,
       "f3PtpAccPortFlowPointSecureBlockingEnabled": f3PtpAccPortFlowPointSecureBlockingEnabled,
       "f3PtpNetPortFlowPointTable": f3PtpNetPortFlowPointTable,
       "f3PtpNetPortFlowPointEntry": f3PtpNetPortFlowPointEntry,
       "f3PtpNetPortFlowPointIndex": f3PtpNetPortFlowPointIndex,
       "f3PtpNetPortFlowPointAlias": f3PtpNetPortFlowPointAlias,
       "f3PtpNetPortFlowPointAdminState": f3PtpNetPortFlowPointAdminState,
       "f3PtpNetPortFlowPointOperationalState": f3PtpNetPortFlowPointOperationalState,
       "f3PtpNetPortFlowPointSecondaryState": f3PtpNetPortFlowPointSecondaryState,
       "f3PtpNetPortFlowPointType": f3PtpNetPortFlowPointType,
       "f3PtpNetPortFlowPointClock": f3PtpNetPortFlowPointClock,
       "f3PtpNetPortFlowPointService": f3PtpNetPortFlowPointService,
       "f3PtpNetPortFlowPointOuterVlanEtherType": f3PtpNetPortFlowPointOuterVlanEtherType,
       "f3PtpNetPortFlowPointOuterVlanMemberList": f3PtpNetPortFlowPointOuterVlanMemberList,
       "f3PtpNetPortFlowPointOuterUntaggedEnabled": f3PtpNetPortFlowPointOuterUntaggedEnabled,
       "f3PtpNetPortFlowPointInner1VlanEtherType": f3PtpNetPortFlowPointInner1VlanEtherType,
       "f3PtpNetPortFlowPointInner1VlanMemberList": f3PtpNetPortFlowPointInner1VlanMemberList,
       "f3PtpNetPortFlowPointInner1UntaggedEnabled": f3PtpNetPortFlowPointInner1UntaggedEnabled,
       "f3PtpNetPortFlowPointInner2VlanEtherType": f3PtpNetPortFlowPointInner2VlanEtherType,
       "f3PtpNetPortFlowPointInner2VlanMemberList": f3PtpNetPortFlowPointInner2VlanMemberList,
       "f3PtpNetPortFlowPointInner2UntaggedEnabled": f3PtpNetPortFlowPointInner2UntaggedEnabled,
       "f3PtpNetPortFlowPointStorageType": f3PtpNetPortFlowPointStorageType,
       "f3PtpNetPortFlowPointRowStatus": f3PtpNetPortFlowPointRowStatus,
       "f3PtpNetPortFlowPointCOS": f3PtpNetPortFlowPointCOS,
       "f3PtpNetPortFlowPointCIRLo": f3PtpNetPortFlowPointCIRLo,
       "f3PtpNetPortFlowPointCIRHi": f3PtpNetPortFlowPointCIRHi,
       "f3PtpNetPortFlowPointEIRLo": f3PtpNetPortFlowPointEIRLo,
       "f3PtpNetPortFlowPointEIRHi": f3PtpNetPortFlowPointEIRHi,
       "f3PtpNetPortFlowPointBufferSize": f3PtpNetPortFlowPointBufferSize,
       "f3PtpNetPortFlowPointLoopAvoidance": f3PtpNetPortFlowPointLoopAvoidance,
       "f3PtpNetPortFlowPointRefConnectGuardFlow": f3PtpNetPortFlowPointRefConnectGuardFlow,
       "f3PtpNetPortFlowPointSecureState": f3PtpNetPortFlowPointSecureState,
       "f3PtpNetPortFlowPointSecureBlockingEnabled": f3PtpNetPortFlowPointSecureBlockingEnabled,
       "f3PtpEthernetAccPortExtTable": f3PtpEthernetAccPortExtTable,
       "f3PtpEthernetAccPortExtEntry": f3PtpEthernetAccPortExtEntry,
       "f3PtpEthernetAccPortDelayAsymmetry": f3PtpEthernetAccPortDelayAsymmetry,
       "f3PtpEthernetNetPortExtTable": f3PtpEthernetNetPortExtTable,
       "f3PtpEthernetNetPortExtEntry": f3PtpEthernetNetPortExtEntry,
       "f3PtpEthernetNetPortDelayAsymmetry": f3PtpEthernetNetPortDelayAsymmetry,
       "f3PtpConfigScalars": f3PtpConfigScalars,
       "f3PtpSysTimeOfDayClock": f3PtpSysTimeOfDayClock,
       "f3PtpBCTable": f3PtpBCTable,
       "f3PtpBCEntry": f3PtpBCEntry,
       "f3PtpBCIndex": f3PtpBCIndex,
       "f3PtpBCAlias": f3PtpBCAlias,
       "f3PtpBCAdminState": f3PtpBCAdminState,
       "f3PtpBCOperationalState": f3PtpBCOperationalState,
       "f3PtpBCSecondaryState": f3PtpBCSecondaryState,
       "f3PtpBCClockIdentity": f3PtpBCClockIdentity,
       "f3PtpBCTimingSource": f3PtpBCTimingSource,
       "f3PtpBCClockClass": f3PtpBCClockClass,
       "f3PtpBCDomainNumber": f3PtpBCDomainNumber,
       "f3PtpBCStorageType": f3PtpBCStorageType,
       "f3PtpBCRowStatus": f3PtpBCRowStatus,
       "f3PtpBCPhysicalEntityIndex": f3PtpBCPhysicalEntityIndex,
       "f3PtpBCMediationControl": f3PtpBCMediationControl,
       "f3PtpMasterClockTable": f3PtpMasterClockTable,
       "f3PtpMasterClockEntry": f3PtpMasterClockEntry,
       "f3PtpMasterClockIndex": f3PtpMasterClockIndex,
       "f3PtpMasterClockAlias": f3PtpMasterClockAlias,
       "f3PtpMasterClockAdminState": f3PtpMasterClockAdminState,
       "f3PtpMasterClockOperationalState": f3PtpMasterClockOperationalState,
       "f3PtpMasterClockSecondaryState": f3PtpMasterClockSecondaryState,
       "f3PtpMasterClockClockIdentity": f3PtpMasterClockClockIdentity,
       "f3PtpMasterClockTimeClock": f3PtpMasterClockTimeClock,
       "f3PtpMasterClockDomainNumber": f3PtpMasterClockDomainNumber,
       "f3PtpMasterClockPriority1": f3PtpMasterClockPriority1,
       "f3PtpMasterClockPriority2": f3PtpMasterClockPriority2,
       "f3PtpMasterClockClockClass": f3PtpMasterClockClockClass,
       "f3PtpMasterClockClockAccuracy": f3PtpMasterClockClockAccuracy,
       "f3PtpMasterClockTimeScale": f3PtpMasterClockTimeScale,
       "f3PtpMasterClockUtcOffset": f3PtpMasterClockUtcOffset,
       "f3PtpMasterClockStorageType": f3PtpMasterClockStorageType,
       "f3PtpMasterClockRowStatus": f3PtpMasterClockRowStatus,
       "f3PtpMasterClockActiveTimeRef": f3PtpMasterClockActiveTimeRef,
       "f3PtpMasterClockPTPProfile": f3PtpMasterClockPTPProfile,
       "f3PtpMasterClockPhysicalEntityIndex": f3PtpMasterClockPhysicalEntityIndex,
       "f3PtpMasterClockActiveGrantsAnnounceService": f3PtpMasterClockActiveGrantsAnnounceService,
       "f3PtpMasterClockActiveGrantsSyncService": f3PtpMasterClockActiveGrantsSyncService,
       "f3PtpMasterClockActiveGrantsDelayRequestService": f3PtpMasterClockActiveGrantsDelayRequestService,
       "f3PtpMasterClockServiceAvailableTime": f3PtpMasterClockServiceAvailableTime,
       "f3PtpMasterClockServiceUnavailableTime": f3PtpMasterClockServiceUnavailableTime,
       "f3PtpMasterClockServiceAvailablePercentage": f3PtpMasterClockServiceAvailablePercentage,
       "f3PtpMasterClockSmpteSystemFrameRateNumerator": f3PtpMasterClockSmpteSystemFrameRateNumerator,
       "f3PtpMasterClockSmpteSystemFrameRateDenominator": f3PtpMasterClockSmpteSystemFrameRateDenominator,
       "f3PtpMasterClockSmpteTimeAddressFlags": f3PtpMasterClockSmpteTimeAddressFlags,
       "f3PtpMCITable": f3PtpMCITable,
       "f3PtpMCIEntry": f3PtpMCIEntry,
       "f3PtpMCIIndex": f3PtpMCIIndex,
       "f3PtpMCIAlias": f3PtpMCIAlias,
       "f3PtpMCIAdminState": f3PtpMCIAdminState,
       "f3PtpMCIOperationalState": f3PtpMCIOperationalState,
       "f3PtpMCISecondaryState": f3PtpMCISecondaryState,
       "f3PtpMCIPortIdentity": f3PtpMCIPortIdentity,
       "f3PtpMCIDomainNumber": f3PtpMCIDomainNumber,
       "f3PtpMCIClockType": f3PtpMCIClockType,
       "f3PtpMCIDelayMechanism": f3PtpMCIDelayMechanism,
       "f3PtpMCIIfName": f3PtpMCIIfName,
       "f3PtpMCIIpProtocol": f3PtpMCIIpProtocol,
       "f3PtpMCIMasterIpV4Address": f3PtpMCIMasterIpV4Address,
       "f3PtpMCIMasterIpV4SubnetMask": f3PtpMCIMasterIpV4SubnetMask,
       "f3PtpMCIIpPriorityMapMode": f3PtpMCIIpPriorityMapMode,
       "f3PtpMCIIpPriority": f3PtpMCIIpPriority,
       "f3PtpMCIMaxLeaseDuration": f3PtpMCIMaxLeaseDuration,
       "f3PtpMCIMaxSlavesSupported": f3PtpMCIMaxSlavesSupported,
       "f3PtpMCIMaxStaticSlavesSupported": f3PtpMCIMaxStaticSlavesSupported,
       "f3PtpMCIMaxSyncMsgRate": f3PtpMCIMaxSyncMsgRate,
       "f3PtpMCIMaxDelayRespMsgRate": f3PtpMCIMaxDelayRespMsgRate,
       "f3PtpMCIMaxAnnounceMsgRate": f3PtpMCIMaxAnnounceMsgRate,
       "f3PtpMCIStorageType": f3PtpMCIStorageType,
       "f3PtpMCIRowStatus": f3PtpMCIRowStatus,
       "f3PtpMCIServiceFlow": f3PtpMCIServiceFlow,
       "f3PtpMCIClockClassProfile": f3PtpMCIClockClassProfile,
       "f3PtpMCIClockClass": f3PtpMCIClockClass,
       "f3PtpMCIAnnounceExtTLVEnable": f3PtpMCIAnnounceExtTLVEnable,
       "f3PtpMCIPtpTransport": f3PtpMCIPtpTransport,
       "f3PtpMCIPtpTransportMode": f3PtpMCIPtpTransportMode,
       "f3PtpMCIPtpRemoteSlaveAgingTimeout": f3PtpMCIPtpRemoteSlaveAgingTimeout,
       "f3PtpMCIMasterIpV6Address": f3PtpMCIMasterIpV6Address,
       "f3PtpMCIMasterIpV6AddrPrefixLength": f3PtpMCIMasterIpV6AddrPrefixLength,
       "f3PtpMCIDefaultGatewayControl": f3PtpMCIDefaultGatewayControl,
       "f3PtpMCIGateway": f3PtpMCIGateway,
       "f3PtpMCIIpV6Gateway": f3PtpMCIIpV6Gateway,
       "f3PtpMasterVirtualPortTable": f3PtpMasterVirtualPortTable,
       "f3PtpMasterVirtualPortEntry": f3PtpMasterVirtualPortEntry,
       "f3PtpMasterVirtualPortIndex": f3PtpMasterVirtualPortIndex,
       "f3PtpMasterVirtualPortAlias": f3PtpMasterVirtualPortAlias,
       "f3PtpMasterVirtualPortAdminState": f3PtpMasterVirtualPortAdminState,
       "f3PtpMasterVirtualPortOperationalState": f3PtpMasterVirtualPortOperationalState,
       "f3PtpMasterVirtualPortSecondaryState": f3PtpMasterVirtualPortSecondaryState,
       "f3PtpMasterVirtualPortFlowPoint": f3PtpMasterVirtualPortFlowPoint,
       "f3PtpMasterVirtualPortStorageType": f3PtpMasterVirtualPortStorageType,
       "f3PtpMasterVirtualPortRowStatus": f3PtpMasterVirtualPortRowStatus,
       "f3PtpStaticRemoteSlaveTable": f3PtpStaticRemoteSlaveTable,
       "f3PtpStaticRemoteSlaveEntry": f3PtpStaticRemoteSlaveEntry,
       "f3PtpStaticRemoteSlaveIndex": f3PtpStaticRemoteSlaveIndex,
       "f3PtpStaticRemoteSlaveAlias": f3PtpStaticRemoteSlaveAlias,
       "f3PtpStaticRemoteSlaveAdminState": f3PtpStaticRemoteSlaveAdminState,
       "f3PtpStaticRemoteSlaveOperationalState": f3PtpStaticRemoteSlaveOperationalState,
       "f3PtpStaticRemoteSlaveSecondaryState": f3PtpStaticRemoteSlaveSecondaryState,
       "f3PtpStaticRemoteSlaveClockIdentity": f3PtpStaticRemoteSlaveClockIdentity,
       "f3PtpStaticRemoteSlaveIpV4Address": f3PtpStaticRemoteSlaveIpV4Address,
       "f3PtpStaticRemoteSlaveTimeCreated": f3PtpStaticRemoteSlaveTimeCreated,
       "f3PtpStaticRemoteSlaveSyncMsgRate": f3PtpStaticRemoteSlaveSyncMsgRate,
       "f3PtpStaticRemoteSlaveDelayRspMsgRate": f3PtpStaticRemoteSlaveDelayRspMsgRate,
       "f3PtpStaticRemoteSlaveAnnounceMsgRate": f3PtpStaticRemoteSlaveAnnounceMsgRate,
       "f3PtpStaticRemoteSlaveNegSyncLeaseDur": f3PtpStaticRemoteSlaveNegSyncLeaseDur,
       "f3PtpStaticRemoteSlaveNegDelayRspLeaseDur": f3PtpStaticRemoteSlaveNegDelayRspLeaseDur,
       "f3PtpStaticRemoteSlaveNegAnnounceLeaseDur": f3PtpStaticRemoteSlaveNegAnnounceLeaseDur,
       "f3PtpStaticRemoteSlaveSyncDurRemTime": f3PtpStaticRemoteSlaveSyncDurRemTime,
       "f3PtpStaticRemoteSlaveDelayRspDurRemTime": f3PtpStaticRemoteSlaveDelayRspDurRemTime,
       "f3PtpStaticRemoteSlaveAnnounceDurRemTime": f3PtpStaticRemoteSlaveAnnounceDurRemTime,
       "f3PtpStaticRemoteSlaveUmnControl": f3PtpStaticRemoteSlaveUmnControl,
       "f3PtpStaticRemoteSlaveStorageType": f3PtpStaticRemoteSlaveStorageType,
       "f3PtpStaticRemoteSlaveRowStatus": f3PtpStaticRemoteSlaveRowStatus,
       "f3PtpStaticRemoteSlaveIpV6Address": f3PtpStaticRemoteSlaveIpV6Address,
       "f3PtpDynamicRemoteSlaveTable": f3PtpDynamicRemoteSlaveTable,
       "f3PtpDynamicRemoteSlaveEntry": f3PtpDynamicRemoteSlaveEntry,
       "f3PtpDynamicRemoteSlaveIndex": f3PtpDynamicRemoteSlaveIndex,
       "f3PtpDynamicRemoteSlaveAlias": f3PtpDynamicRemoteSlaveAlias,
       "f3PtpDynamicRemoteSlaveAdminState": f3PtpDynamicRemoteSlaveAdminState,
       "f3PtpDynamicRemoteSlaveOperationalState": f3PtpDynamicRemoteSlaveOperationalState,
       "f3PtpDynamicRemoteSlaveSecondaryState": f3PtpDynamicRemoteSlaveSecondaryState,
       "f3PtpDynamicRemoteSlaveClockIdentity": f3PtpDynamicRemoteSlaveClockIdentity,
       "f3PtpDynamicRemoteSlaveIpV4Address": f3PtpDynamicRemoteSlaveIpV4Address,
       "f3PtpDynamicRemoteSlaveTimeCreated": f3PtpDynamicRemoteSlaveTimeCreated,
       "f3PtpDynamicRemoteSlaveSyncMsgRate": f3PtpDynamicRemoteSlaveSyncMsgRate,
       "f3PtpDynamicRemoteSlaveDelayRspMsgRate": f3PtpDynamicRemoteSlaveDelayRspMsgRate,
       "f3PtpDynamicRemoteSlaveAnnounceMsgRate": f3PtpDynamicRemoteSlaveAnnounceMsgRate,
       "f3PtpDynamicRemoteSlaveNegSyncLeaseDur": f3PtpDynamicRemoteSlaveNegSyncLeaseDur,
       "f3PtpDynamicRemoteSlaveNegDelayRspLeaseDur": f3PtpDynamicRemoteSlaveNegDelayRspLeaseDur,
       "f3PtpDynamicRemoteSlaveNegAnnounceLeaseDur": f3PtpDynamicRemoteSlaveNegAnnounceLeaseDur,
       "f3PtpDynamicRemoteSlaveSyncDurRemTime": f3PtpDynamicRemoteSlaveSyncDurRemTime,
       "f3PtpDynamicRemoteSlaveDelayRspDurRemTime": f3PtpDynamicRemoteSlaveDelayRspDurRemTime,
       "f3PtpDynamicRemoteSlaveAnnounceDurRemTime": f3PtpDynamicRemoteSlaveAnnounceDurRemTime,
       "f3PtpDynamicRemoteSlaveRowStatus": f3PtpDynamicRemoteSlaveRowStatus,
       "f3PtpDynamicRemoteSlaveStorageType": f3PtpDynamicRemoteSlaveStorageType,
       "f3PtpDynamicRemoteSlavePortIdentity": f3PtpDynamicRemoteSlavePortIdentity,
       "f3PtpDynamicRemoteSlavePeerMacAddress": f3PtpDynamicRemoteSlavePeerMacAddress,
       "f3PtpDynamicRemoteSlaveIpV6Address": f3PtpDynamicRemoteSlaveIpV6Address,
       "f3PtpTrafficPortFlowPointTable": f3PtpTrafficPortFlowPointTable,
       "f3PtpTrafficPortFlowPointEntry": f3PtpTrafficPortFlowPointEntry,
       "f3PtpTrafficPortFlowPointIndex": f3PtpTrafficPortFlowPointIndex,
       "f3PtpTrafficPortFlowPointAlias": f3PtpTrafficPortFlowPointAlias,
       "f3PtpTrafficPortFlowPointAdminState": f3PtpTrafficPortFlowPointAdminState,
       "f3PtpTrafficPortFlowPointOperationalState": f3PtpTrafficPortFlowPointOperationalState,
       "f3PtpTrafficPortFlowPointSecondaryState": f3PtpTrafficPortFlowPointSecondaryState,
       "f3PtpTrafficPortFlowPointType": f3PtpTrafficPortFlowPointType,
       "f3PtpTrafficPortFlowPointClock": f3PtpTrafficPortFlowPointClock,
       "f3PtpTrafficPortFlowPointService": f3PtpTrafficPortFlowPointService,
       "f3PtpTrafficPortFlowPointOuterVlanEtherType": f3PtpTrafficPortFlowPointOuterVlanEtherType,
       "f3PtpTrafficPortFlowPointOuterVlanMemberList": f3PtpTrafficPortFlowPointOuterVlanMemberList,
       "f3PtpTrafficPortFlowPointOuterUntaggedEnabled": f3PtpTrafficPortFlowPointOuterUntaggedEnabled,
       "f3PtpTrafficPortFlowPointInner1VlanEtherType": f3PtpTrafficPortFlowPointInner1VlanEtherType,
       "f3PtpTrafficPortFlowPointInner1VlanMemberList": f3PtpTrafficPortFlowPointInner1VlanMemberList,
       "f3PtpTrafficPortFlowPointInner1UntaggedEnabled": f3PtpTrafficPortFlowPointInner1UntaggedEnabled,
       "f3PtpTrafficPortFlowPointInner2VlanEtherType": f3PtpTrafficPortFlowPointInner2VlanEtherType,
       "f3PtpTrafficPortFlowPointInner2VlanMemberList": f3PtpTrafficPortFlowPointInner2VlanMemberList,
       "f3PtpTrafficPortFlowPointInner2UntaggedEnabled": f3PtpTrafficPortFlowPointInner2UntaggedEnabled,
       "f3PtpTrafficPortFlowPointStorageType": f3PtpTrafficPortFlowPointStorageType,
       "f3PtpTrafficPortFlowPointRowStatus": f3PtpTrafficPortFlowPointRowStatus,
       "f3PtpTrafficPortFlowPointCOS": f3PtpTrafficPortFlowPointCOS,
       "f3PtpTrafficPortFlowPointCIRLo": f3PtpTrafficPortFlowPointCIRLo,
       "f3PtpTrafficPortFlowPointCIRHi": f3PtpTrafficPortFlowPointCIRHi,
       "f3PtpTrafficPortFlowPointEIRLo": f3PtpTrafficPortFlowPointEIRLo,
       "f3PtpTrafficPortFlowPointEIRHi": f3PtpTrafficPortFlowPointEIRHi,
       "f3PtpTrafficPortFlowPointAssociatedQueueProfile": f3PtpTrafficPortFlowPointAssociatedQueueProfile,
       "f3PtpTrafficPortFlowPointLoopAvoidance": f3PtpTrafficPortFlowPointLoopAvoidance,
       "f3PtpEthernetTrafficPortExtTable": f3PtpEthernetTrafficPortExtTable,
       "f3PtpEthernetTrafficPortExtEntry": f3PtpEthernetTrafficPortExtEntry,
       "f3PtpEthernetTrafficPortDelayAsymmetry": f3PtpEthernetTrafficPortDelayAsymmetry,
       "f3PtpPTPClockTable": f3PtpPTPClockTable,
       "f3PtpPTPClockEntry": f3PtpPTPClockEntry,
       "f3PtpPTPClockIndex": f3PtpPTPClockIndex,
       "f3PtpPTPClockAdminState": f3PtpPTPClockAdminState,
       "f3PtpPTPClockAlias": f3PtpPTPClockAlias,
       "f3PtpPTPClockOperationalState": f3PtpPTPClockOperationalState,
       "f3PtpPTPClockSecondaryState": f3PtpPTPClockSecondaryState,
       "f3PtpPTPClockProfile": f3PtpPTPClockProfile,
       "f3PtpPTPClockClockType": f3PtpPTPClockClockType,
       "f3PtpPTPClockOperationalMode": f3PtpPTPClockOperationalMode,
       "f3PtpPTPClockClockIdentity": f3PtpPTPClockClockIdentity,
       "f3PtpPTPClockDomainNumber": f3PtpPTPClockDomainNumber,
       "f3PtpPTPClockTimeSource": f3PtpPTPClockTimeSource,
       "f3PtpPTPClockPriority1": f3PtpPTPClockPriority1,
       "f3PtpPTPClockPriority2": f3PtpPTPClockPriority2,
       "f3PtpPTPClockLocalPriority": f3PtpPTPClockLocalPriority,
       "f3PtpPTPClockClockAccuracy": f3PtpPTPClockClockAccuracy,
       "f3PtpPTPClockScaledLogVariance": f3PtpPTPClockScaledLogVariance,
       "f3PtpPTPClockSyncEid": f3PtpPTPClockSyncEid,
       "f3PtpPTPClockCurrentTimeOfDay": f3PtpPTPClockCurrentTimeOfDay,
       "f3PtpPTPClockActiveSlavePort": f3PtpPTPClockActiveSlavePort,
       "f3PtpPTPClockClockRecoveryState": f3PtpPTPClockClockRecoveryState,
       "f3PtpPTPClockPhaseRecoveryState": f3PtpPTPClockPhaseRecoveryState,
       "f3PtpPTPClockTimeTraceabilityStatus": f3PtpPTPClockTimeTraceabilityStatus,
       "f3PtpPTPClockTimeSinceTimeTraceabilityChanged": f3PtpPTPClockTimeSinceTimeTraceabilityChanged,
       "f3PtpPTPClockFreqTraceabilityStatus": f3PtpPTPClockFreqTraceabilityStatus,
       "f3PtpPTPClockTimeSinceFreqTraceabilityChanged": f3PtpPTPClockTimeSinceFreqTraceabilityChanged,
       "f3PtpPTPClockClockSyncEEnabled": f3PtpPTPClockClockSyncEEnabled,
       "f3PtpPTPClockClockQLModeEnabled": f3PtpPTPClockClockQLModeEnabled,
       "f3PtpPTPClockClockExpectedQL": f3PtpPTPClockClockExpectedQL,
       "f3PtpPTPClockClockAssumedQL": f3PtpPTPClockClockAssumedQL,
       "f3PtpPTPClockClockReceivedQL": f3PtpPTPClockClockReceivedQL,
       "f3PtpPTPClockStorageType": f3PtpPTPClockStorageType,
       "f3PtpPTPClockRowStatus": f3PtpPTPClockRowStatus,
       "f3PtpPTPClockCurrentOffsetFromMaster": f3PtpPTPClockCurrentOffsetFromMaster,
       "f3PtpPTPClockRecentMeanPathDelay": f3PtpPTPClockRecentMeanPathDelay,
       "f3PtpPTPClockRecentSyncPDV": f3PtpPTPClockRecentSyncPDV,
       "f3PtpPTPClockClockClass": f3PtpPTPClockClockClass,
       "f3PtpPTPClockPhysicalEntityIndex": f3PtpPTPClockPhysicalEntityIndex,
       "f3PtpPTPClockActiveGrantsAnnounceService": f3PtpPTPClockActiveGrantsAnnounceService,
       "f3PtpPTPClockActiveGrantsSyncService": f3PtpPTPClockActiveGrantsSyncService,
       "f3PtpPTPClockActiveGrantsDelayRequestService": f3PtpPTPClockActiveGrantsDelayRequestService,
       "f3PtpPTPClockMaxStepRemoved": f3PtpPTPClockMaxStepRemoved,
       "f3PtpPTPClockServiceAvailableTime": f3PtpPTPClockServiceAvailableTime,
       "f3PtpPTPClockServiceUnavailableTime": f3PtpPTPClockServiceUnavailableTime,
       "f3PtpPTPClockServiceAvailablePercentage": f3PtpPTPClockServiceAvailablePercentage,
       "f3PtpPTPClockGrandMasterID": f3PtpPTPClockGrandMasterID,
       "f3PtpPTPClockTimeInaccuracy": f3PtpPTPClockTimeInaccuracy,
       "f3PtpPTPClockNetworkTimeInaccuracy": f3PtpPTPClockNetworkTimeInaccuracy,
       "f3PtpPTPPortTable": f3PtpPTPPortTable,
       "f3PtpPTPPortEntry": f3PtpPTPPortEntry,
       "f3PtpPTPPortIndex": f3PtpPTPPortIndex,
       "f3PtpPTPPortAdminState": f3PtpPTPPortAdminState,
       "f3PtpPTPPortAlias": f3PtpPTPPortAlias,
       "f3PtpPTPPortOperationalState": f3PtpPTPPortOperationalState,
       "f3PtpPTPPortSecondaryState": f3PtpPTPPortSecondaryState,
       "f3PtpPTPPortPeerPortIdentity": f3PtpPTPPortPeerPortIdentity,
       "f3PtpPTPPortLocalPriority": f3PtpPTPPortLocalPriority,
       "f3PtpPTPPortPtpFlowPointEid": f3PtpPTPPortPtpFlowPointEid,
       "f3PtpPTPPortNotSlave": f3PtpPTPPortNotSlave,
       "f3PtpPTPPortTxDestMacAddress": f3PtpPTPPortTxDestMacAddress,
       "f3PtpPTPPortSyncMessageRate": f3PtpPTPPortSyncMessageRate,
       "f3PtpPTPPortmDelayReqRespMsgRate": f3PtpPTPPortmDelayReqRespMsgRate,
       "f3PtpPTPPortmAnnounceMsgRate": f3PtpPTPPortmAnnounceMsgRate,
       "f3PtpPTPPortAnnounceReceiptTimeout": f3PtpPTPPortAnnounceReceiptTimeout,
       "f3PtpPTPPortSyncReceiptTimeout": f3PtpPTPPortSyncReceiptTimeout,
       "f3PtpPTPPortDelayRespTimeout": f3PtpPTPPortDelayRespTimeout,
       "f3PtpPTPPortPortState": f3PtpPTPPortPortState,
       "f3PtpPTPPortBmcaDecisionCode": f3PtpPTPPortBmcaDecisionCode,
       "f3PtpPTPPortClockClass": f3PtpPTPPortClockClass,
       "f3PtpPTPPortPeerPortMacAddress": f3PtpPTPPortPeerPortMacAddress,
       "f3PtpPTPPortRowStatus": f3PtpPTPPortRowStatus,
       "f3PtpPTPPortPortIdentity": f3PtpPTPPortPortIdentity,
       "f3PtpPTPPortMaxExpectedL2Slaves": f3PtpPTPPortMaxExpectedL2Slaves,
       "f3PtpPTPPortMasterClockType": f3PtpPTPPortMasterClockType,
       "f3PtpPTPPortLastRcvdAnnounceMsg": f3PtpPTPPortLastRcvdAnnounceMsg,
       "f3PtpPTPPortLastRcvdSyncMsg": f3PtpPTPPortLastRcvdSyncMsg,
       "f3PtpPTPPortLastRcvdDelayReqMsg": f3PtpPTPPortLastRcvdDelayReqMsg,
       "f3PtpPTPPortLastRcvdDelayRspMsg": f3PtpPTPPortLastRcvdDelayRspMsg,
       "f3PtpPTPPortMasterOnly": f3PtpPTPPortMasterOnly,
       "f3PtpPTPPortIsProbingSlave": f3PtpPTPPortIsProbingSlave,
       "f3PtpPTPPortPeerClockClass": f3PtpPTPPortPeerClockClass,
       "f3PtpPTPPortMinimumExpectedClockClass": f3PtpPTPPortMinimumExpectedClockClass,
       "f3PtpPTPPortDelayAsymmetryComp": f3PtpPTPPortDelayAsymmetryComp,
       "f3PtpPTPPortAutoAsymmetryCompStatus": f3PtpPTPPortAutoAsymmetryCompStatus,
       "f3PtpPTPPortDelayAsymmetry": f3PtpPTPPortDelayAsymmetry,
       "f3PtpPTPPortVirtualPortCtrl": f3PtpPTPPortVirtualPortCtrl,
       "f3PtpPTPPortDelayResponderType": f3PtpPTPPortDelayResponderType,
       "f3PtpPTPPortTimeTraceable": f3PtpPTPPortTimeTraceable,
       "f3PtpPTPPortFrequencyTraceable": f3PtpPTPPortFrequencyTraceable,
       "f3PtpL2DynamicRemoteSlaveTable": f3PtpL2DynamicRemoteSlaveTable,
       "f3PtpL2DynamicRemoteSlaveEntry": f3PtpL2DynamicRemoteSlaveEntry,
       "f3PtpL2DynamicRemoteSlaveIndex": f3PtpL2DynamicRemoteSlaveIndex,
       "f3PtpL2DynamicRemoteSlavePortIdentity": f3PtpL2DynamicRemoteSlavePortIdentity,
       "f3PtpL2DynamicRemoteSlaveMacAddress": f3PtpL2DynamicRemoteSlaveMacAddress,
       "f3PtpL2DynamicRemoteSlaveRowStatus": f3PtpL2DynamicRemoteSlaveRowStatus,
       "f3PtpL2DynamicRemoteSlaveStorageType": f3PtpL2DynamicRemoteSlaveStorageType,
       "f3PtpL2DynamicRemoteSlaveClockIdentity": f3PtpL2DynamicRemoteSlaveClockIdentity,
       "f3PtpMCIProtGroupTable": f3PtpMCIProtGroupTable,
       "f3PtpMCIProtGroupEntry": f3PtpMCIProtGroupEntry,
       "f3PtpMCIProtGroupIndex": f3PtpMCIProtGroupIndex,
       "f3PtpMCIProtGroupAdminState": f3PtpMCIProtGroupAdminState,
       "f3PtpMCIProtGroupActiveMember": f3PtpMCIProtGroupActiveMember,
       "f3PtpMCIProtGroupLastSwitchOverTime": f3PtpMCIProtGroupLastSwitchOverTime,
       "f3PtpMCIProtGroupLastSwitchOverReason": f3PtpMCIProtGroupLastSwitchOverReason,
       "f3PtpMCIProtGroupStorageType": f3PtpMCIProtGroupStorageType,
       "f3PtpMCIProtGroupRowStatus": f3PtpMCIProtGroupRowStatus,
       "f3PtpMCIProtMemberTable": f3PtpMCIProtMemberTable,
       "f3PtpMCIProtMemberEntry": f3PtpMCIProtMemberEntry,
       "f3PtpMCIProtMemberObject": f3PtpMCIProtMemberObject,
       "f3PtpMCIProtMemberStorageType": f3PtpMCIProtMemberStorageType,
       "f3PtpMCIProtMemberRowStatus": f3PtpMCIProtMemberRowStatus,
       "f3PtpTrafficPortFlowPointExtTable": f3PtpTrafficPortFlowPointExtTable,
       "f3PtpTrafficPortFlowPointExtEntry": f3PtpTrafficPortFlowPointExtEntry,
       "f3PtpTrafficPortFlowPointBufferSize": f3PtpTrafficPortFlowPointBufferSize,
       "f3PtpL3PTPPortTable": f3PtpL3PTPPortTable,
       "f3PtpL3PTPPortEntry": f3PtpL3PTPPortEntry,
       "f3PtpL3PTPPortIndex": f3PtpL3PTPPortIndex,
       "f3PtpL3PTPPortAdminState": f3PtpL3PTPPortAdminState,
       "f3PtpL3PTPPortAlias": f3PtpL3PTPPortAlias,
       "f3PtpL3PTPPortOperationalState": f3PtpL3PTPPortOperationalState,
       "f3PtpL3PTPPortSecondaryState": f3PtpL3PTPPortSecondaryState,
       "f3PtpL3PTPPortPortIdentity": f3PtpL3PTPPortPortIdentity,
       "f3PtpL3PTPPortLocalPriority": f3PtpL3PTPPortLocalPriority,
       "f3PtpL3PTPPortPtpFlowPointEid": f3PtpL3PTPPortPtpFlowPointEid,
       "f3PtpL3PTPPortSyncMessageRate": f3PtpL3PTPPortSyncMessageRate,
       "f3PtpL3PTPPortDelayReqRespMsgRate": f3PtpL3PTPPortDelayReqRespMsgRate,
       "f3PtpL3PTPPortAnnounceMsgRate": f3PtpL3PTPPortAnnounceMsgRate,
       "f3PtpL3PTPPortAnnounceReceiptTimeout": f3PtpL3PTPPortAnnounceReceiptTimeout,
       "f3PtpL3PTPPortSyncReceiptTimeout": f3PtpL3PTPPortSyncReceiptTimeout,
       "f3PtpL3PTPPortDelayRespTimeout": f3PtpL3PTPPortDelayRespTimeout,
       "f3PtpL3PTPPortPortState": f3PtpL3PTPPortPortState,
       "f3PtpL3PTPPortBmcaDecisionCode": f3PtpL3PTPPortBmcaDecisionCode,
       "f3PtpL3PTPPortPeerClockClass": f3PtpL3PTPPortPeerClockClass,
       "f3PtpL3PTPPortMinimumExpectedClockClass": f3PtpL3PTPPortMinimumExpectedClockClass,
       "f3PtpL3PTPPortIpProtocol": f3PtpL3PTPPortIpProtocol,
       "f3PtpL3PTPPortIfName": f3PtpL3PTPPortIfName,
       "f3PtpL3PTPPortIpPriorityMapMode": f3PtpL3PTPPortIpPriorityMapMode,
       "f3PtpL3PTPPortIpPriority": f3PtpL3PTPPortIpPriority,
       "f3PtpL3PTPPortIpV4Address": f3PtpL3PTPPortIpV4Address,
       "f3PtpL3PTPPortIpV4SubnetMask": f3PtpL3PTPPortIpV4SubnetMask,
       "f3PtpL3PTPPortIpV6Address": f3PtpL3PTPPortIpV6Address,
       "f3PtpL3PTPPortIpV6AddrPrefixLength": f3PtpL3PTPPortIpV6AddrPrefixLength,
       "f3PtpL3PTPPortDefaultGatewayControl": f3PtpL3PTPPortDefaultGatewayControl,
       "f3PtpL3PTPPortGateway": f3PtpL3PTPPortGateway,
       "f3PtpL3PTPPortIpV6Gateway": f3PtpL3PTPPortIpV6Gateway,
       "f3PtpL3PTPPortUnicastMessageNegEnabled": f3PtpL3PTPPortUnicastMessageNegEnabled,
       "f3PtpL3PTPPortTransmitDuration": f3PtpL3PTPPortTransmitDuration,
       "f3PtpL3PTPPortRequestUnicastTimeout": f3PtpL3PTPPortRequestUnicastTimeout,
       "f3PtpL3PTPPortRequestUnicastRestartTimer": f3PtpL3PTPPortRequestUnicastRestartTimer,
       "f3PtpL3PTPPortMasterIpV4Address": f3PtpL3PTPPortMasterIpV4Address,
       "f3PtpL3PTPPortMasterIpV6Address": f3PtpL3PTPPortMasterIpV6Address,
       "f3PtpL3PTPPortDelayAsymmetryComp": f3PtpL3PTPPortDelayAsymmetryComp,
       "f3PtpL3PTPPortAutoAsymmetryCompStatus": f3PtpL3PTPPortAutoAsymmetryCompStatus,
       "f3PtpL3PTPPortDelayAsymmetry": f3PtpL3PTPPortDelayAsymmetry,
       "f3PtpL3PTPPortStorageType": f3PtpL3PTPPortStorageType,
       "f3PtpL3PTPPortRowStatus": f3PtpL3PTPPortRowStatus,
       "f3PtpPerformanceObjects": f3PtpPerformanceObjects,
       "f3PtpAccPortFlowPointStatsTable": f3PtpAccPortFlowPointStatsTable,
       "f3PtpAccPortFlowPointStatsEntry": f3PtpAccPortFlowPointStatsEntry,
       "f3PtpAccPortFlowPointStatsIndex": f3PtpAccPortFlowPointStatsIndex,
       "f3PtpAccPortFlowPointStatsIntervalType": f3PtpAccPortFlowPointStatsIntervalType,
       "f3PtpAccPortFlowPointStatsValid": f3PtpAccPortFlowPointStatsValid,
       "f3PtpAccPortFlowPointStatsAction": f3PtpAccPortFlowPointStatsAction,
       "f3PtpAccPortFlowPointStatsAnnouncesRx": f3PtpAccPortFlowPointStatsAnnouncesRx,
       "f3PtpAccPortFlowPointStatsAnnouncesTx": f3PtpAccPortFlowPointStatsAnnouncesTx,
       "f3PtpAccPortFlowPointStatsSyncsRx": f3PtpAccPortFlowPointStatsSyncsRx,
       "f3PtpAccPortFlowPointStatsSyncsTx": f3PtpAccPortFlowPointStatsSyncsTx,
       "f3PtpAccPortFlowPointStatsFollowupsRx": f3PtpAccPortFlowPointStatsFollowupsRx,
       "f3PtpAccPortFlowPointStatsFollowupsTx": f3PtpAccPortFlowPointStatsFollowupsTx,
       "f3PtpAccPortFlowPointStatsDelayReqsRx": f3PtpAccPortFlowPointStatsDelayReqsRx,
       "f3PtpAccPortFlowPointStatsDelayReqsTx": f3PtpAccPortFlowPointStatsDelayReqsTx,
       "f3PtpAccPortFlowPointStatsDelayRspsRx": f3PtpAccPortFlowPointStatsDelayRspsRx,
       "f3PtpAccPortFlowPointStatsDelayRspsTx": f3PtpAccPortFlowPointStatsDelayRspsTx,
       "f3PtpAccPortFlowPointStatsPDelayReqsRx": f3PtpAccPortFlowPointStatsPDelayReqsRx,
       "f3PtpAccPortFlowPointStatsPDelayReqsTx": f3PtpAccPortFlowPointStatsPDelayReqsTx,
       "f3PtpAccPortFlowPointStatsPDelayRspsRx": f3PtpAccPortFlowPointStatsPDelayRspsRx,
       "f3PtpAccPortFlowPointStatsPDelayRspsTx": f3PtpAccPortFlowPointStatsPDelayRspsTx,
       "f3PtpAccPortFlowPointStatsPDelayRspFollowupsRx": f3PtpAccPortFlowPointStatsPDelayRspFollowupsRx,
       "f3PtpAccPortFlowPointStatsPDelayRspFollowupsTx": f3PtpAccPortFlowPointStatsPDelayRspFollowupsTx,
       "f3PtpAccPortFlowPointStatsSignalingRx": f3PtpAccPortFlowPointStatsSignalingRx,
       "f3PtpAccPortFlowPointStatsSignalingTx": f3PtpAccPortFlowPointStatsSignalingTx,
       "f3PtpAccPortFlowPointStatsMgmtFramesRx": f3PtpAccPortFlowPointStatsMgmtFramesRx,
       "f3PtpAccPortFlowPointStatsMgmtFramesTx": f3PtpAccPortFlowPointStatsMgmtFramesTx,
       "f3PtpAccPortFlowPointStatsPtpUnknownsRx": f3PtpAccPortFlowPointStatsPtpUnknownsRx,
       "f3PtpAccPortFlowPointStatsPtpUnknownsTx": f3PtpAccPortFlowPointStatsPtpUnknownsTx,
       "f3PtpAccPortFlowPointStatsMinSyncResTime": f3PtpAccPortFlowPointStatsMinSyncResTime,
       "f3PtpAccPortFlowPointStatsMaxSyncResTime": f3PtpAccPortFlowPointStatsMaxSyncResTime,
       "f3PtpAccPortFlowPointStatsAvgSyncResTime": f3PtpAccPortFlowPointStatsAvgSyncResTime,
       "f3PtpAccPortFlowPointStatsMinDelayReqResTime": f3PtpAccPortFlowPointStatsMinDelayReqResTime,
       "f3PtpAccPortFlowPointStatsMaxDelayReqResTime": f3PtpAccPortFlowPointStatsMaxDelayReqResTime,
       "f3PtpAccPortFlowPointStatsAvgDelayReqResTime": f3PtpAccPortFlowPointStatsAvgDelayReqResTime,
       "f3PtpAccPortFlowPointStatsMinPDelayReqResTime": f3PtpAccPortFlowPointStatsMinPDelayReqResTime,
       "f3PtpAccPortFlowPointStatsMaxPDelayReqResTime": f3PtpAccPortFlowPointStatsMaxPDelayReqResTime,
       "f3PtpAccPortFlowPointStatsAvgPDelayReqResTime": f3PtpAccPortFlowPointStatsAvgPDelayReqResTime,
       "f3PtpAccPortFlowPointStatsMinPDelayRspResTime": f3PtpAccPortFlowPointStatsMinPDelayRspResTime,
       "f3PtpAccPortFlowPointStatsMaxPDelayRspResTime": f3PtpAccPortFlowPointStatsMaxPDelayRspResTime,
       "f3PtpAccPortFlowPointStatsAvgPDelayRspResTime": f3PtpAccPortFlowPointStatsAvgPDelayRspResTime,
       "f3PtpAccPortFlowPointStatsDestMciNoMatchDiscards": f3PtpAccPortFlowPointStatsDestMciNoMatchDiscards,
       "f3PtpAccPortFlowPointStatsTagNoMatchDiscards": f3PtpAccPortFlowPointStatsTagNoMatchDiscards,
       "f3PtpAccPortFlowPointHistoryTable": f3PtpAccPortFlowPointHistoryTable,
       "f3PtpAccPortFlowPointHistoryEntry": f3PtpAccPortFlowPointHistoryEntry,
       "f3PtpAccPortFlowPointHistoryIndex": f3PtpAccPortFlowPointHistoryIndex,
       "f3PtpAccPortFlowPointHistoryTime": f3PtpAccPortFlowPointHistoryTime,
       "f3PtpAccPortFlowPointHistoryValid": f3PtpAccPortFlowPointHistoryValid,
       "f3PtpAccPortFlowPointHistoryAction": f3PtpAccPortFlowPointHistoryAction,
       "f3PtpAccPortFlowPointHistoryAnnouncesRx": f3PtpAccPortFlowPointHistoryAnnouncesRx,
       "f3PtpAccPortFlowPointHistoryAnnouncesTx": f3PtpAccPortFlowPointHistoryAnnouncesTx,
       "f3PtpAccPortFlowPointHistorySyncsRx": f3PtpAccPortFlowPointHistorySyncsRx,
       "f3PtpAccPortFlowPointHistorySyncsTx": f3PtpAccPortFlowPointHistorySyncsTx,
       "f3PtpAccPortFlowPointHistoryFollowupsRx": f3PtpAccPortFlowPointHistoryFollowupsRx,
       "f3PtpAccPortFlowPointHistoryFollowupsTx": f3PtpAccPortFlowPointHistoryFollowupsTx,
       "f3PtpAccPortFlowPointHistoryDelayReqsRx": f3PtpAccPortFlowPointHistoryDelayReqsRx,
       "f3PtpAccPortFlowPointHistoryDelayReqsTx": f3PtpAccPortFlowPointHistoryDelayReqsTx,
       "f3PtpAccPortFlowPointHistoryDelayRspsRx": f3PtpAccPortFlowPointHistoryDelayRspsRx,
       "f3PtpAccPortFlowPointHistoryDelayRspsTx": f3PtpAccPortFlowPointHistoryDelayRspsTx,
       "f3PtpAccPortFlowPointHistoryPDelayReqsRx": f3PtpAccPortFlowPointHistoryPDelayReqsRx,
       "f3PtpAccPortFlowPointHistoryPDelayReqsTx": f3PtpAccPortFlowPointHistoryPDelayReqsTx,
       "f3PtpAccPortFlowPointHistoryPDelayRspsRx": f3PtpAccPortFlowPointHistoryPDelayRspsRx,
       "f3PtpAccPortFlowPointHistoryPDelayRspsTx": f3PtpAccPortFlowPointHistoryPDelayRspsTx,
       "f3PtpAccPortFlowPointHistoryPDelayRspFollowupsRx": f3PtpAccPortFlowPointHistoryPDelayRspFollowupsRx,
       "f3PtpAccPortFlowPointHistoryPDelayRspFollowupsTx": f3PtpAccPortFlowPointHistoryPDelayRspFollowupsTx,
       "f3PtpAccPortFlowPointHistorySignalingRx": f3PtpAccPortFlowPointHistorySignalingRx,
       "f3PtpAccPortFlowPointHistorySignalingTx": f3PtpAccPortFlowPointHistorySignalingTx,
       "f3PtpAccPortFlowPointHistoryMgmtFramesRx": f3PtpAccPortFlowPointHistoryMgmtFramesRx,
       "f3PtpAccPortFlowPointHistoryMgmtFramesTx": f3PtpAccPortFlowPointHistoryMgmtFramesTx,
       "f3PtpAccPortFlowPointHistoryPtpUnknownsRx": f3PtpAccPortFlowPointHistoryPtpUnknownsRx,
       "f3PtpAccPortFlowPointHistoryPtpUnknownsTx": f3PtpAccPortFlowPointHistoryPtpUnknownsTx,
       "f3PtpAccPortFlowPointHistoryMinSyncResTime": f3PtpAccPortFlowPointHistoryMinSyncResTime,
       "f3PtpAccPortFlowPointHistoryMaxSyncResTime": f3PtpAccPortFlowPointHistoryMaxSyncResTime,
       "f3PtpAccPortFlowPointHistoryAvgSyncResTime": f3PtpAccPortFlowPointHistoryAvgSyncResTime,
       "f3PtpAccPortFlowPointHistoryMinDelayReqResTime": f3PtpAccPortFlowPointHistoryMinDelayReqResTime,
       "f3PtpAccPortFlowPointHistoryMaxDelayReqResTime": f3PtpAccPortFlowPointHistoryMaxDelayReqResTime,
       "f3PtpAccPortFlowPointHistoryAvgDelayReqResTime": f3PtpAccPortFlowPointHistoryAvgDelayReqResTime,
       "f3PtpAccPortFlowPointHistoryMinPDelayReqResTime": f3PtpAccPortFlowPointHistoryMinPDelayReqResTime,
       "f3PtpAccPortFlowPointHistoryMaxPDelayReqResTime": f3PtpAccPortFlowPointHistoryMaxPDelayReqResTime,
       "f3PtpAccPortFlowPointHistoryAvgPDelayReqResTime": f3PtpAccPortFlowPointHistoryAvgPDelayReqResTime,
       "f3PtpAccPortFlowPointHistoryMinPDelayRspResTime": f3PtpAccPortFlowPointHistoryMinPDelayRspResTime,
       "f3PtpAccPortFlowPointHistoryMaxPDelayRspResTime": f3PtpAccPortFlowPointHistoryMaxPDelayRspResTime,
       "f3PtpAccPortFlowPointHistoryAvgPDelayRspResTime": f3PtpAccPortFlowPointHistoryAvgPDelayRspResTime,
       "f3PtpAccPortFlowPointHistoryDestMciNoMatchDiscards": f3PtpAccPortFlowPointHistoryDestMciNoMatchDiscards,
       "f3PtpAccPortFlowPointHistoryTagNoMatchDiscards": f3PtpAccPortFlowPointHistoryTagNoMatchDiscards,
       "f3PtpAccPortFlowPointThresholdTable": f3PtpAccPortFlowPointThresholdTable,
       "f3PtpAccPortFlowPointThresholdEntry": f3PtpAccPortFlowPointThresholdEntry,
       "f3PtpAccPortFlowPointThresholdIndex": f3PtpAccPortFlowPointThresholdIndex,
       "f3PtpAccPortFlowPointThresholdInterval": f3PtpAccPortFlowPointThresholdInterval,
       "f3PtpAccPortFlowPointThresholdVariable": f3PtpAccPortFlowPointThresholdVariable,
       "f3PtpAccPortFlowPointThresholdValueLo": f3PtpAccPortFlowPointThresholdValueLo,
       "f3PtpAccPortFlowPointThresholdValueHi": f3PtpAccPortFlowPointThresholdValueHi,
       "f3PtpAccPortFlowPointThresholdMonValue": f3PtpAccPortFlowPointThresholdMonValue,
       "f3PtpNetPortFlowPointStatsTable": f3PtpNetPortFlowPointStatsTable,
       "f3PtpNetPortFlowPointStatsEntry": f3PtpNetPortFlowPointStatsEntry,
       "f3PtpNetPortFlowPointStatsIndex": f3PtpNetPortFlowPointStatsIndex,
       "f3PtpNetPortFlowPointStatsIntervalType": f3PtpNetPortFlowPointStatsIntervalType,
       "f3PtpNetPortFlowPointStatsValid": f3PtpNetPortFlowPointStatsValid,
       "f3PtpNetPortFlowPointStatsAction": f3PtpNetPortFlowPointStatsAction,
       "f3PtpNetPortFlowPointStatsAnnouncesRx": f3PtpNetPortFlowPointStatsAnnouncesRx,
       "f3PtpNetPortFlowPointStatsAnnouncesTx": f3PtpNetPortFlowPointStatsAnnouncesTx,
       "f3PtpNetPortFlowPointStatsSyncsRx": f3PtpNetPortFlowPointStatsSyncsRx,
       "f3PtpNetPortFlowPointStatsSyncsTx": f3PtpNetPortFlowPointStatsSyncsTx,
       "f3PtpNetPortFlowPointStatsFollowupsRx": f3PtpNetPortFlowPointStatsFollowupsRx,
       "f3PtpNetPortFlowPointStatsFollowupsTx": f3PtpNetPortFlowPointStatsFollowupsTx,
       "f3PtpNetPortFlowPointStatsDelayReqsRx": f3PtpNetPortFlowPointStatsDelayReqsRx,
       "f3PtpNetPortFlowPointStatsDelayReqsTx": f3PtpNetPortFlowPointStatsDelayReqsTx,
       "f3PtpNetPortFlowPointStatsDelayRspsRx": f3PtpNetPortFlowPointStatsDelayRspsRx,
       "f3PtpNetPortFlowPointStatsDelayRspsTx": f3PtpNetPortFlowPointStatsDelayRspsTx,
       "f3PtpNetPortFlowPointStatsPDelayReqsRx": f3PtpNetPortFlowPointStatsPDelayReqsRx,
       "f3PtpNetPortFlowPointStatsPDelayReqsTx": f3PtpNetPortFlowPointStatsPDelayReqsTx,
       "f3PtpNetPortFlowPointStatsPDelayRspsRx": f3PtpNetPortFlowPointStatsPDelayRspsRx,
       "f3PtpNetPortFlowPointStatsPDelayRspsTx": f3PtpNetPortFlowPointStatsPDelayRspsTx,
       "f3PtpNetPortFlowPointStatsPDelayRspFollowupsRx": f3PtpNetPortFlowPointStatsPDelayRspFollowupsRx,
       "f3PtpNetPortFlowPointStatsPDelayRspFollowupsTx": f3PtpNetPortFlowPointStatsPDelayRspFollowupsTx,
       "f3PtpNetPortFlowPointStatsSignalingRx": f3PtpNetPortFlowPointStatsSignalingRx,
       "f3PtpNetPortFlowPointStatsSignalingTx": f3PtpNetPortFlowPointStatsSignalingTx,
       "f3PtpNetPortFlowPointStatsMgmtFramesRx": f3PtpNetPortFlowPointStatsMgmtFramesRx,
       "f3PtpNetPortFlowPointStatsMgmtFramesTx": f3PtpNetPortFlowPointStatsMgmtFramesTx,
       "f3PtpNetPortFlowPointStatsPtpUnknownsRx": f3PtpNetPortFlowPointStatsPtpUnknownsRx,
       "f3PtpNetPortFlowPointStatsPtpUnknownsTx": f3PtpNetPortFlowPointStatsPtpUnknownsTx,
       "f3PtpNetPortFlowPointStatsAvgSyncResTime": f3PtpNetPortFlowPointStatsAvgSyncResTime,
       "f3PtpNetPortFlowPointStatsMinSyncResTime": f3PtpNetPortFlowPointStatsMinSyncResTime,
       "f3PtpNetPortFlowPointStatsMaxSyncResTime": f3PtpNetPortFlowPointStatsMaxSyncResTime,
       "f3PtpNetPortFlowPointStatsAvgDelayReqResTime": f3PtpNetPortFlowPointStatsAvgDelayReqResTime,
       "f3PtpNetPortFlowPointStatsMinDelayReqResTime": f3PtpNetPortFlowPointStatsMinDelayReqResTime,
       "f3PtpNetPortFlowPointStatsMaxDelayReqResTime": f3PtpNetPortFlowPointStatsMaxDelayReqResTime,
       "f3PtpNetPortFlowPointStatsMinPDelayReqResTime": f3PtpNetPortFlowPointStatsMinPDelayReqResTime,
       "f3PtpNetPortFlowPointStatsMaxPDelayReqResTime": f3PtpNetPortFlowPointStatsMaxPDelayReqResTime,
       "f3PtpNetPortFlowPointStatsAvgPDelayReqResTime": f3PtpNetPortFlowPointStatsAvgPDelayReqResTime,
       "f3PtpNetPortFlowPointStatsMinPDelayRspResTime": f3PtpNetPortFlowPointStatsMinPDelayRspResTime,
       "f3PtpNetPortFlowPointStatsMaxPDelayRspResTime": f3PtpNetPortFlowPointStatsMaxPDelayRspResTime,
       "f3PtpNetPortFlowPointStatsAvgPDelayRspResTime": f3PtpNetPortFlowPointStatsAvgPDelayRspResTime,
       "f3PtpNetPortFlowPointStatsDestMciNoMatchDiscards": f3PtpNetPortFlowPointStatsDestMciNoMatchDiscards,
       "f3PtpNetPortFlowPointStatsTagNoMatchDiscards": f3PtpNetPortFlowPointStatsTagNoMatchDiscards,
       "f3PtpNetPortFlowPointHistoryTable": f3PtpNetPortFlowPointHistoryTable,
       "f3PtpNetPortFlowPointHistoryEntry": f3PtpNetPortFlowPointHistoryEntry,
       "f3PtpNetPortFlowPointHistoryIndex": f3PtpNetPortFlowPointHistoryIndex,
       "f3PtpNetPortFlowPointHistoryTime": f3PtpNetPortFlowPointHistoryTime,
       "f3PtpNetPortFlowPointHistoryValid": f3PtpNetPortFlowPointHistoryValid,
       "f3PtpNetPortFlowPointHistoryAction": f3PtpNetPortFlowPointHistoryAction,
       "f3PtpNetPortFlowPointHistoryAnnouncesRx": f3PtpNetPortFlowPointHistoryAnnouncesRx,
       "f3PtpNetPortFlowPointHistoryAnnouncesTx": f3PtpNetPortFlowPointHistoryAnnouncesTx,
       "f3PtpNetPortFlowPointHistorySyncsRx": f3PtpNetPortFlowPointHistorySyncsRx,
       "f3PtpNetPortFlowPointHistorySyncsTx": f3PtpNetPortFlowPointHistorySyncsTx,
       "f3PtpNetPortFlowPointHistoryFollowupsRx": f3PtpNetPortFlowPointHistoryFollowupsRx,
       "f3PtpNetPortFlowPointHistoryFollowupsTx": f3PtpNetPortFlowPointHistoryFollowupsTx,
       "f3PtpNetPortFlowPointHistoryDelayReqsRx": f3PtpNetPortFlowPointHistoryDelayReqsRx,
       "f3PtpNetPortFlowPointHistoryDelayReqsTx": f3PtpNetPortFlowPointHistoryDelayReqsTx,
       "f3PtpNetPortFlowPointHistoryDelayRspsRx": f3PtpNetPortFlowPointHistoryDelayRspsRx,
       "f3PtpNetPortFlowPointHistoryDelayRspsTx": f3PtpNetPortFlowPointHistoryDelayRspsTx,
       "f3PtpNetPortFlowPointHistoryPDelayReqsRx": f3PtpNetPortFlowPointHistoryPDelayReqsRx,
       "f3PtpNetPortFlowPointHistoryPDelayReqsTx": f3PtpNetPortFlowPointHistoryPDelayReqsTx,
       "f3PtpNetPortFlowPointHistoryPDelayRspsRx": f3PtpNetPortFlowPointHistoryPDelayRspsRx,
       "f3PtpNetPortFlowPointHistoryPDelayRspsTx": f3PtpNetPortFlowPointHistoryPDelayRspsTx,
       "f3PtpNetPortFlowPointHistoryPDelayRspFollowupsRx": f3PtpNetPortFlowPointHistoryPDelayRspFollowupsRx,
       "f3PtpNetPortFlowPointHistoryPDelayRspFollowupsTx": f3PtpNetPortFlowPointHistoryPDelayRspFollowupsTx,
       "f3PtpNetPortFlowPointHistorySignalingRx": f3PtpNetPortFlowPointHistorySignalingRx,
       "f3PtpNetPortFlowPointHistorySignalingTx": f3PtpNetPortFlowPointHistorySignalingTx,
       "f3PtpNetPortFlowPointHistoryMgmtFramesRx": f3PtpNetPortFlowPointHistoryMgmtFramesRx,
       "f3PtpNetPortFlowPointHistoryMgmtFramesTx": f3PtpNetPortFlowPointHistoryMgmtFramesTx,
       "f3PtpNetPortFlowPointHistoryPtpUnknownsRx": f3PtpNetPortFlowPointHistoryPtpUnknownsRx,
       "f3PtpNetPortFlowPointHistoryPtpUnknownsTx": f3PtpNetPortFlowPointHistoryPtpUnknownsTx,
       "f3PtpNetPortFlowPointHistoryAvgSyncResTime": f3PtpNetPortFlowPointHistoryAvgSyncResTime,
       "f3PtpNetPortFlowPointHistoryMinSyncResTime": f3PtpNetPortFlowPointHistoryMinSyncResTime,
       "f3PtpNetPortFlowPointHistoryMaxSyncResTime": f3PtpNetPortFlowPointHistoryMaxSyncResTime,
       "f3PtpNetPortFlowPointHistoryAvgDelayReqResTime": f3PtpNetPortFlowPointHistoryAvgDelayReqResTime,
       "f3PtpNetPortFlowPointHistoryMinDelayReqResTime": f3PtpNetPortFlowPointHistoryMinDelayReqResTime,
       "f3PtpNetPortFlowPointHistoryMaxDelayReqResTime": f3PtpNetPortFlowPointHistoryMaxDelayReqResTime,
       "f3PtpNetPortFlowPointHistoryMinPDelayReqResTime": f3PtpNetPortFlowPointHistoryMinPDelayReqResTime,
       "f3PtpNetPortFlowPointHistoryMaxPDelayReqResTime": f3PtpNetPortFlowPointHistoryMaxPDelayReqResTime,
       "f3PtpNetPortFlowPointHistoryAvgPDelayReqResTime": f3PtpNetPortFlowPointHistoryAvgPDelayReqResTime,
       "f3PtpNetPortFlowPointHistoryMinPDelayRspResTime": f3PtpNetPortFlowPointHistoryMinPDelayRspResTime,
       "f3PtpNetPortFlowPointHistoryMaxPDelayRspResTime": f3PtpNetPortFlowPointHistoryMaxPDelayRspResTime,
       "f3PtpNetPortFlowPointHistoryAvgPDelayRspResTime": f3PtpNetPortFlowPointHistoryAvgPDelayRspResTime,
       "f3PtpNetPortFlowPointHistoryDestMciNoMatchDiscards": f3PtpNetPortFlowPointHistoryDestMciNoMatchDiscards,
       "f3PtpNetPortFlowPointHistoryTagNoMatchDiscards": f3PtpNetPortFlowPointHistoryTagNoMatchDiscards,
       "f3PtpNetPortFlowPointThresholdTable": f3PtpNetPortFlowPointThresholdTable,
       "f3PtpNetPortFlowPointThresholdEntry": f3PtpNetPortFlowPointThresholdEntry,
       "f3PtpNetPortFlowPointThresholdIndex": f3PtpNetPortFlowPointThresholdIndex,
       "f3PtpNetPortFlowPointThresholdInterval": f3PtpNetPortFlowPointThresholdInterval,
       "f3PtpNetPortFlowPointThresholdVariable": f3PtpNetPortFlowPointThresholdVariable,
       "f3PtpNetPortFlowPointThresholdValueLo": f3PtpNetPortFlowPointThresholdValueLo,
       "f3PtpNetPortFlowPointThresholdValueHi": f3PtpNetPortFlowPointThresholdValueHi,
       "f3PtpNetPortFlowPointThresholdMonValue": f3PtpNetPortFlowPointThresholdMonValue,
       "f3PtpSOOCStatsTable": f3PtpSOOCStatsTable,
       "f3PtpSOOCStatsEntry": f3PtpSOOCStatsEntry,
       "f3PtpSOOCStatsIndex": f3PtpSOOCStatsIndex,
       "f3PtpSOOCStatsIntervalType": f3PtpSOOCStatsIntervalType,
       "f3PtpSOOCStatsValid": f3PtpSOOCStatsValid,
       "f3PtpSOOCStatsAction": f3PtpSOOCStatsAction,
       "f3PtpSOOCStatsMinOffsetFromMaster": f3PtpSOOCStatsMinOffsetFromMaster,
       "f3PtpSOOCStatsMaxOffsetFromMaster": f3PtpSOOCStatsMaxOffsetFromMaster,
       "f3PtpSOOCStatsAvgOffsetFromMaster": f3PtpSOOCStatsAvgOffsetFromMaster,
       "f3PtpSOOCStatsMinMeanPathDelay": f3PtpSOOCStatsMinMeanPathDelay,
       "f3PtpSOOCStatsMaxMeanPathDelay": f3PtpSOOCStatsMaxMeanPathDelay,
       "f3PtpSOOCStatsAvgMeanPathDelay": f3PtpSOOCStatsAvgMeanPathDelay,
       "f3PtpSOOCStatsMinSyncPathDelay": f3PtpSOOCStatsMinSyncPathDelay,
       "f3PtpSOOCStatsMaxSyncPathDelay": f3PtpSOOCStatsMaxSyncPathDelay,
       "f3PtpSOOCStatsAvgSyncPathDelay": f3PtpSOOCStatsAvgSyncPathDelay,
       "f3PtpSOOCStatsMinSyncPDV": f3PtpSOOCStatsMinSyncPDV,
       "f3PtpSOOCStatsMaxSyncPDV": f3PtpSOOCStatsMaxSyncPDV,
       "f3PtpSOOCStatsAvgSyncPDV": f3PtpSOOCStatsAvgSyncPDV,
       "f3PtpSOOCStatsMgmtMsgsDiscarded": f3PtpSOOCStatsMgmtMsgsDiscarded,
       "f3PtpSOOCStatsInvalidMsgLenDiscards": f3PtpSOOCStatsInvalidMsgLenDiscards,
       "f3PtpSOOCStatsUnknownMasterDiscards": f3PtpSOOCStatsUnknownMasterDiscards,
       "f3PtpSOOCStatsUnknownDomainDiscards": f3PtpSOOCStatsUnknownDomainDiscards,
       "f3PtpSOOCStatsMulticastAnnounceDiscards": f3PtpSOOCStatsMulticastAnnounceDiscards,
       "f3PtpSOOCStatsOutOfSeqAnnounceMsgs": f3PtpSOOCStatsOutOfSeqAnnounceMsgs,
       "f3PtpSOOCStatsMulticastSyncDiscards": f3PtpSOOCStatsMulticastSyncDiscards,
       "f3PtpSOOCStatsTwoStepSyncDiscards": f3PtpSOOCStatsTwoStepSyncDiscards,
       "f3PtpSOOCStatsFollowupDiscards": f3PtpSOOCStatsFollowupDiscards,
       "f3PtpSOOCStatsDelayReqDiscards": f3PtpSOOCStatsDelayReqDiscards,
       "f3PtpSOOCStatsPDelayReqDiscards": f3PtpSOOCStatsPDelayReqDiscards,
       "f3PtpSOOCStatsPDelayRspDiscards": f3PtpSOOCStatsPDelayRspDiscards,
       "f3PtpSOOCStatsPDelayFollowupDiscards": f3PtpSOOCStatsPDelayFollowupDiscards,
       "f3PtpSOOCStatsInvalidTLVLenDiscards": f3PtpSOOCStatsInvalidTLVLenDiscards,
       "f3PtpSOOCStatsInvalidTLVTypeDiscards": f3PtpSOOCStatsInvalidTLVTypeDiscards,
       "f3PtpSOOCStatsMaxFwdFlowWeight": f3PtpSOOCStatsMaxFwdFlowWeight,
       "f3PtpSOOCStatsAvgFwdFlowWeight": f3PtpSOOCStatsAvgFwdFlowWeight,
       "f3PtpSOOCStatsMinRevFlowWeight": f3PtpSOOCStatsMinRevFlowWeight,
       "f3PtpSOOCStatsMaxRevFlowWeight": f3PtpSOOCStatsMaxRevFlowWeight,
       "f3PtpSOOCStatsAvgRevFlowWeight": f3PtpSOOCStatsAvgRevFlowWeight,
       "f3PtpSOOCStatsNumClockRecTransients": f3PtpSOOCStatsNumClockRecTransients,
       "f3PtpSOOCHistoryTable": f3PtpSOOCHistoryTable,
       "f3PtpSOOCHistoryEntry": f3PtpSOOCHistoryEntry,
       "f3PtpSOOCHistoryIndex": f3PtpSOOCHistoryIndex,
       "f3PtpSOOCHistoryTime": f3PtpSOOCHistoryTime,
       "f3PtpSOOCHistoryValid": f3PtpSOOCHistoryValid,
       "f3PtpSOOCHistoryAction": f3PtpSOOCHistoryAction,
       "f3PtpSOOCHistoryMinOffsetFromMaster": f3PtpSOOCHistoryMinOffsetFromMaster,
       "f3PtpSOOCHistoryMaxOffsetFromMaster": f3PtpSOOCHistoryMaxOffsetFromMaster,
       "f3PtpSOOCHistoryAvgOffsetFromMaster": f3PtpSOOCHistoryAvgOffsetFromMaster,
       "f3PtpSOOCHistoryMinMeanPathDelay": f3PtpSOOCHistoryMinMeanPathDelay,
       "f3PtpSOOCHistoryMaxMeanPathDelay": f3PtpSOOCHistoryMaxMeanPathDelay,
       "f3PtpSOOCHistoryAvgMeanPathDelay": f3PtpSOOCHistoryAvgMeanPathDelay,
       "f3PtpSOOCHistoryMinSyncPathDelay": f3PtpSOOCHistoryMinSyncPathDelay,
       "f3PtpSOOCHistoryMaxSyncPathDelay": f3PtpSOOCHistoryMaxSyncPathDelay,
       "f3PtpSOOCHistoryAvgSyncPathDelay": f3PtpSOOCHistoryAvgSyncPathDelay,
       "f3PtpSOOCHistoryMinSyncPDV": f3PtpSOOCHistoryMinSyncPDV,
       "f3PtpSOOCHistoryMaxSyncPDV": f3PtpSOOCHistoryMaxSyncPDV,
       "f3PtpSOOCHistoryAvgSyncPDV": f3PtpSOOCHistoryAvgSyncPDV,
       "f3PtpSOOCHistoryMgmtMsgsDiscarded": f3PtpSOOCHistoryMgmtMsgsDiscarded,
       "f3PtpSOOCHistoryInvalidMsgLenDiscards": f3PtpSOOCHistoryInvalidMsgLenDiscards,
       "f3PtpSOOCHistoryUnknownMasterDiscards": f3PtpSOOCHistoryUnknownMasterDiscards,
       "f3PtpSOOCHistoryUnknownDomainDiscards": f3PtpSOOCHistoryUnknownDomainDiscards,
       "f3PtpSOOCHistoryMulticastAnnounceDiscards": f3PtpSOOCHistoryMulticastAnnounceDiscards,
       "f3PtpSOOCHistoryOutOfSeqAnnounceMsgs": f3PtpSOOCHistoryOutOfSeqAnnounceMsgs,
       "f3PtpSOOCHistoryMulticastSyncDiscards": f3PtpSOOCHistoryMulticastSyncDiscards,
       "f3PtpSOOCHistoryTwoStepSyncDiscards": f3PtpSOOCHistoryTwoStepSyncDiscards,
       "f3PtpSOOCHistoryFollowupDiscards": f3PtpSOOCHistoryFollowupDiscards,
       "f3PtpSOOCHistoryDelayReqDiscards": f3PtpSOOCHistoryDelayReqDiscards,
       "f3PtpSOOCHistoryPDelayReqDiscards": f3PtpSOOCHistoryPDelayReqDiscards,
       "f3PtpSOOCHistoryPDelayRspDiscards": f3PtpSOOCHistoryPDelayRspDiscards,
       "f3PtpSOOCHistoryPDelayFollowupDiscards": f3PtpSOOCHistoryPDelayFollowupDiscards,
       "f3PtpSOOCHistoryInvalidTLVLenDiscards": f3PtpSOOCHistoryInvalidTLVLenDiscards,
       "f3PtpSOOCHistoryInvalidTLVTypeDiscards": f3PtpSOOCHistoryInvalidTLVTypeDiscards,
       "f3PtpSOOCHistoryMaxFwdFlowWeight": f3PtpSOOCHistoryMaxFwdFlowWeight,
       "f3PtpSOOCHistoryAvgFwdFlowWeight": f3PtpSOOCHistoryAvgFwdFlowWeight,
       "f3PtpSOOCHistoryMinRevFlowWeight": f3PtpSOOCHistoryMinRevFlowWeight,
       "f3PtpSOOCHistoryMaxRevFlowWeight": f3PtpSOOCHistoryMaxRevFlowWeight,
       "f3PtpSOOCHistoryAvgRevFlowWeight": f3PtpSOOCHistoryAvgRevFlowWeight,
       "f3PtpSOOCHistoryNumClockRecTransients": f3PtpSOOCHistoryNumClockRecTransients,
       "f3PtpSOOCThresholdTable": f3PtpSOOCThresholdTable,
       "f3PtpSOOCThresholdEntry": f3PtpSOOCThresholdEntry,
       "f3PtpSOOCThresholdIndex": f3PtpSOOCThresholdIndex,
       "f3PtpSOOCThresholdInterval": f3PtpSOOCThresholdInterval,
       "f3PtpSOOCThresholdVariable": f3PtpSOOCThresholdVariable,
       "f3PtpSOOCThresholdValueLo": f3PtpSOOCThresholdValueLo,
       "f3PtpSOOCThresholdValueHi": f3PtpSOOCThresholdValueHi,
       "f3PtpSOOCThresholdMonValue": f3PtpSOOCThresholdMonValue,
       "f3PtpTSStatsTable": f3PtpTSStatsTable,
       "f3PtpTSStatsEntry": f3PtpTSStatsEntry,
       "f3PtpTSStatsIndex": f3PtpTSStatsIndex,
       "f3PtpTSStatsIntervalType": f3PtpTSStatsIntervalType,
       "f3PtpTSStatsValid": f3PtpTSStatsValid,
       "f3PtpTSStatsAction": f3PtpTSStatsAction,
       "f3PtpTSStatsTotalTimeCR5": f3PtpTSStatsTotalTimeCR5,
       "f3PtpTSStatsTotalTimeCR4": f3PtpTSStatsTotalTimeCR4,
       "f3PtpTSStatsTotalTimeCR3": f3PtpTSStatsTotalTimeCR3,
       "f3PtpTSStatsTotalTimePR5": f3PtpTSStatsTotalTimePR5,
       "f3PtpTSStatsTotalTimePR4": f3PtpTSStatsTotalTimePR4,
       "f3PtpTSStatsTotalTimePR3": f3PtpTSStatsTotalTimePR3,
       "f3PtpTSHistoryTable": f3PtpTSHistoryTable,
       "f3PtpTSHistoryEntry": f3PtpTSHistoryEntry,
       "f3PtpTSHistoryIndex": f3PtpTSHistoryIndex,
       "f3PtpTSHistoryTime": f3PtpTSHistoryTime,
       "f3PtpTSHistoryValid": f3PtpTSHistoryValid,
       "f3PtpTSHistoryAction": f3PtpTSHistoryAction,
       "f3PtpTSHistoryTotalTimeCR5": f3PtpTSHistoryTotalTimeCR5,
       "f3PtpTSHistoryTotalTimeCR4": f3PtpTSHistoryTotalTimeCR4,
       "f3PtpTSHistoryTotalTimeCR3": f3PtpTSHistoryTotalTimeCR3,
       "f3PtpTSHistoryTotalTimePR5": f3PtpTSHistoryTotalTimePR5,
       "f3PtpTSHistoryTotalTimePR4": f3PtpTSHistoryTotalTimePR4,
       "f3PtpTSHistoryTotalTimePR3": f3PtpTSHistoryTotalTimePR3,
       "f3PtpTSThresholdTable": f3PtpTSThresholdTable,
       "f3PtpTSThresholdEntry": f3PtpTSThresholdEntry,
       "f3PtpTSThresholdIndex": f3PtpTSThresholdIndex,
       "f3PtpTSThresholdInterval": f3PtpTSThresholdInterval,
       "f3PtpTSThresholdVariable": f3PtpTSThresholdVariable,
       "f3PtpTSThresholdValueLo": f3PtpTSThresholdValueLo,
       "f3PtpTSThresholdValueHi": f3PtpTSThresholdValueHi,
       "f3PtpTSThresholdMonValue": f3PtpTSThresholdMonValue,
       "f3PtpMCIStatsTable": f3PtpMCIStatsTable,
       "f3PtpMCIStatsEntry": f3PtpMCIStatsEntry,
       "f3PtpMCIStatsIndex": f3PtpMCIStatsIndex,
       "f3PtpMCIStatsIntervalType": f3PtpMCIStatsIntervalType,
       "f3PtpMCIStatsValid": f3PtpMCIStatsValid,
       "f3PtpMCIStatsAction": f3PtpMCIStatsAction,
       "f3PtpMCIStatsPtpDiscards": f3PtpMCIStatsPtpDiscards,
       "f3PtpMCIStatsSyncDeniedEvents": f3PtpMCIStatsSyncDeniedEvents,
       "f3PtpMCIStatsDelayRspDeniedEvents": f3PtpMCIStatsDelayRspDeniedEvents,
       "f3PtpMCIStatsAnnounceDeniedEvents": f3PtpMCIStatsAnnounceDeniedEvents,
       "f3PtpMCIStatsSyncCancelledEvents": f3PtpMCIStatsSyncCancelledEvents,
       "f3PtpMCIStatsDelayRspCancelledEvents": f3PtpMCIStatsDelayRspCancelledEvents,
       "f3PtpMCIStatsAnnounceCancelledEvents": f3PtpMCIStatsAnnounceCancelledEvents,
       "f3PtpMCIStatsDynamicSlavesLearnt": f3PtpMCIStatsDynamicSlavesLearnt,
       "f3PtpMCIStatsDynamicSlavesDropped": f3PtpMCIStatsDynamicSlavesDropped,
       "f3PtpMCIHistoryTable": f3PtpMCIHistoryTable,
       "f3PtpMCIHistoryEntry": f3PtpMCIHistoryEntry,
       "f3PtpMCIHistoryIndex": f3PtpMCIHistoryIndex,
       "f3PtpMCIHistoryTime": f3PtpMCIHistoryTime,
       "f3PtpMCIHistoryValid": f3PtpMCIHistoryValid,
       "f3PtpMCIHistoryAction": f3PtpMCIHistoryAction,
       "f3PtpMCIHistoryPtpDiscards": f3PtpMCIHistoryPtpDiscards,
       "f3PtpMCIHistorySyncDeniedEvents": f3PtpMCIHistorySyncDeniedEvents,
       "f3PtpMCIHistoryDelayRspDeniedEvents": f3PtpMCIHistoryDelayRspDeniedEvents,
       "f3PtpMCIHistoryAnnounceDeniedEvents": f3PtpMCIHistoryAnnounceDeniedEvents,
       "f3PtpMCIHistorySyncCancelledEvents": f3PtpMCIHistorySyncCancelledEvents,
       "f3PtpMCIHistoryDelayRspCancelledEvents": f3PtpMCIHistoryDelayRspCancelledEvents,
       "f3PtpMCIHistoryAnnounceCancelledEvents": f3PtpMCIHistoryAnnounceCancelledEvents,
       "f3PtpMCIHistoryDynamicSlavesLearnt": f3PtpMCIHistoryDynamicSlavesLearnt,
       "f3PtpMCIHistoryDynamicSlavesDropped": f3PtpMCIHistoryDynamicSlavesDropped,
       "f3PtpMCIThresholdTable": f3PtpMCIThresholdTable,
       "f3PtpMCIThresholdEntry": f3PtpMCIThresholdEntry,
       "f3PtpMCIThresholdIndex": f3PtpMCIThresholdIndex,
       "f3PtpMCIThresholdInterval": f3PtpMCIThresholdInterval,
       "f3PtpMCIThresholdVariable": f3PtpMCIThresholdVariable,
       "f3PtpMCIThresholdValueLo": f3PtpMCIThresholdValueLo,
       "f3PtpMCIThresholdValueHi": f3PtpMCIThresholdValueHi,
       "f3PtpMCIThresholdMonValue": f3PtpMCIThresholdMonValue,
       "f3PtpRemoteSlaveStatsTable": f3PtpRemoteSlaveStatsTable,
       "f3PtpRemoteSlaveStatsEntry": f3PtpRemoteSlaveStatsEntry,
       "f3PtpRemoteSlaveStatsSlaveType": f3PtpRemoteSlaveStatsSlaveType,
       "f3PtpRemoteSlaveStatsSlaveIndex": f3PtpRemoteSlaveStatsSlaveIndex,
       "f3PtpRemoteSlaveStatsIndex": f3PtpRemoteSlaveStatsIndex,
       "f3PtpRemoteSlaveStatsIntervalType": f3PtpRemoteSlaveStatsIntervalType,
       "f3PtpRemoteSlaveStatsValid": f3PtpRemoteSlaveStatsValid,
       "f3PtpRemoteSlaveStatsAction": f3PtpRemoteSlaveStatsAction,
       "f3PtpRemoteSlaveStatsSyncMsgsGen": f3PtpRemoteSlaveStatsSyncMsgsGen,
       "f3PtpRemoteSlaveStatsDelayRspMsgsGen": f3PtpRemoteSlaveStatsDelayRspMsgsGen,
       "f3PtpRemoteSlaveStatsAnnounceMsgsGen": f3PtpRemoteSlaveStatsAnnounceMsgsGen,
       "f3PtpRemoteSlaveStatsSignallingMsgsGen": f3PtpRemoteSlaveStatsSignallingMsgsGen,
       "f3PtpRemoteSlaveStatsDelayReqMsgsRx": f3PtpRemoteSlaveStatsDelayReqMsgsRx,
       "f3PtpRemoteSlaveStatsSignallingMsgsRx": f3PtpRemoteSlaveStatsSignallingMsgsRx,
       "f3PtpRemoteSlaveStatsDelayReqMsgsDropped": f3PtpRemoteSlaveStatsDelayReqMsgsDropped,
       "f3PtpRemoteSlaveStatsInvalidTLVLenDiscards": f3PtpRemoteSlaveStatsInvalidTLVLenDiscards,
       "f3PtpRemoteSlaveStatsInvalidTLVTypeDiscards": f3PtpRemoteSlaveStatsInvalidTLVTypeDiscards,
       "f3PtpRemoteSlaveStatsTimesSyncLeaseExp": f3PtpRemoteSlaveStatsTimesSyncLeaseExp,
       "f3PtpRemoteSlaveStatsTimesDelayRspLeaseExp": f3PtpRemoteSlaveStatsTimesDelayRspLeaseExp,
       "f3PtpRemoteSlaveStatsTimesAnnounceLeaseExp": f3PtpRemoteSlaveStatsTimesAnnounceLeaseExp,
       "f3PtpRemoteSlaveHistoryTable": f3PtpRemoteSlaveHistoryTable,
       "f3PtpRemoteSlaveHistoryEntry": f3PtpRemoteSlaveHistoryEntry,
       "f3PtpRemoteSlaveHistoryIndex": f3PtpRemoteSlaveHistoryIndex,
       "f3PtpRemoteSlaveHistoryTime": f3PtpRemoteSlaveHistoryTime,
       "f3PtpRemoteSlaveHistoryValid": f3PtpRemoteSlaveHistoryValid,
       "f3PtpRemoteSlaveHistoryAction": f3PtpRemoteSlaveHistoryAction,
       "f3PtpRemoteSlaveHistorySyncMsgsGen": f3PtpRemoteSlaveHistorySyncMsgsGen,
       "f3PtpRemoteSlaveHistoryDelayRspMsgsGen": f3PtpRemoteSlaveHistoryDelayRspMsgsGen,
       "f3PtpRemoteSlaveHistoryAnnounceMsgsGen": f3PtpRemoteSlaveHistoryAnnounceMsgsGen,
       "f3PtpRemoteSlaveHistorySignallingMsgsGen": f3PtpRemoteSlaveHistorySignallingMsgsGen,
       "f3PtpRemoteSlaveHistoryDelayReqMsgsRx": f3PtpRemoteSlaveHistoryDelayReqMsgsRx,
       "f3PtpRemoteSlaveHistorySignallingMsgsRx": f3PtpRemoteSlaveHistorySignallingMsgsRx,
       "f3PtpRemoteSlaveHistoryDelayReqMsgsDropped": f3PtpRemoteSlaveHistoryDelayReqMsgsDropped,
       "f3PtpRemoteSlaveHistoryInvalidTLVLenDiscards": f3PtpRemoteSlaveHistoryInvalidTLVLenDiscards,
       "f3PtpRemoteSlaveHistoryInvalidTLVTypeDiscards": f3PtpRemoteSlaveHistoryInvalidTLVTypeDiscards,
       "f3PtpRemoteSlaveHistoryTimesSyncLeaseExp": f3PtpRemoteSlaveHistoryTimesSyncLeaseExp,
       "f3PtpRemoteSlaveHistoryTimesDelayRspLeaseExp": f3PtpRemoteSlaveHistoryTimesDelayRspLeaseExp,
       "f3PtpRemoteSlaveHistoryTimesAnnounceLeaseExp": f3PtpRemoteSlaveHistoryTimesAnnounceLeaseExp,
       "f3PtpRemoteSlaveThresholdTable": f3PtpRemoteSlaveThresholdTable,
       "f3PtpRemoteSlaveThresholdEntry": f3PtpRemoteSlaveThresholdEntry,
       "f3PtpRemoteSlaveThresholdIndex": f3PtpRemoteSlaveThresholdIndex,
       "f3PtpRemoteSlaveThresholdInterval": f3PtpRemoteSlaveThresholdInterval,
       "f3PtpRemoteSlaveThresholdVariable": f3PtpRemoteSlaveThresholdVariable,
       "f3PtpRemoteSlaveThresholdValueLo": f3PtpRemoteSlaveThresholdValueLo,
       "f3PtpRemoteSlaveThresholdValueHi": f3PtpRemoteSlaveThresholdValueHi,
       "f3PtpRemoteSlaveThresholdMonValue": f3PtpRemoteSlaveThresholdMonValue,
       "f3PtpTrafficPortFlowPointStatsTable": f3PtpTrafficPortFlowPointStatsTable,
       "f3PtpTrafficPortFlowPointStatsEntry": f3PtpTrafficPortFlowPointStatsEntry,
       "f3PtpTrafficPortFlowPointStatsIndex": f3PtpTrafficPortFlowPointStatsIndex,
       "f3PtpTrafficPortFlowPointStatsIntervalType": f3PtpTrafficPortFlowPointStatsIntervalType,
       "f3PtpTrafficPortFlowPointStatsValid": f3PtpTrafficPortFlowPointStatsValid,
       "f3PtpTrafficPortFlowPointStatsAction": f3PtpTrafficPortFlowPointStatsAction,
       "f3PtpTrafficPortFlowPointStatsAnnouncesRx": f3PtpTrafficPortFlowPointStatsAnnouncesRx,
       "f3PtpTrafficPortFlowPointStatsAnnouncesTx": f3PtpTrafficPortFlowPointStatsAnnouncesTx,
       "f3PtpTrafficPortFlowPointStatsSyncsRx": f3PtpTrafficPortFlowPointStatsSyncsRx,
       "f3PtpTrafficPortFlowPointStatsSyncsTx": f3PtpTrafficPortFlowPointStatsSyncsTx,
       "f3PtpTrafficPortFlowPointStatsFollowupsRx": f3PtpTrafficPortFlowPointStatsFollowupsRx,
       "f3PtpTrafficPortFlowPointStatsFollowupsTx": f3PtpTrafficPortFlowPointStatsFollowupsTx,
       "f3PtpTrafficPortFlowPointStatsDelayReqsRx": f3PtpTrafficPortFlowPointStatsDelayReqsRx,
       "f3PtpTrafficPortFlowPointStatsDelayReqsTx": f3PtpTrafficPortFlowPointStatsDelayReqsTx,
       "f3PtpTrafficPortFlowPointStatsDelayRspsRx": f3PtpTrafficPortFlowPointStatsDelayRspsRx,
       "f3PtpTrafficPortFlowPointStatsDelayRspsTx": f3PtpTrafficPortFlowPointStatsDelayRspsTx,
       "f3PtpTrafficPortFlowPointStatsPDelayReqsRx": f3PtpTrafficPortFlowPointStatsPDelayReqsRx,
       "f3PtpTrafficPortFlowPointStatsPDelayReqsTx": f3PtpTrafficPortFlowPointStatsPDelayReqsTx,
       "f3PtpTrafficPortFlowPointStatsPDelayRspsRx": f3PtpTrafficPortFlowPointStatsPDelayRspsRx,
       "f3PtpTrafficPortFlowPointStatsPDelayRspsTx": f3PtpTrafficPortFlowPointStatsPDelayRspsTx,
       "f3PtpTrafficPortFlowPointStatsPDelayRspFollowupsRx": f3PtpTrafficPortFlowPointStatsPDelayRspFollowupsRx,
       "f3PtpTrafficPortFlowPointStatsPDelayRspFollowupsTx": f3PtpTrafficPortFlowPointStatsPDelayRspFollowupsTx,
       "f3PtpTrafficPortFlowPointStatsSignalingRx": f3PtpTrafficPortFlowPointStatsSignalingRx,
       "f3PtpTrafficPortFlowPointStatsSignalingTx": f3PtpTrafficPortFlowPointStatsSignalingTx,
       "f3PtpTrafficPortFlowPointStatsMgmtFramesRx": f3PtpTrafficPortFlowPointStatsMgmtFramesRx,
       "f3PtpTrafficPortFlowPointStatsMgmtFramesTx": f3PtpTrafficPortFlowPointStatsMgmtFramesTx,
       "f3PtpTrafficPortFlowPointStatsPtpUnknownsRx": f3PtpTrafficPortFlowPointStatsPtpUnknownsRx,
       "f3PtpTrafficPortFlowPointStatsPtpUnknownsTx": f3PtpTrafficPortFlowPointStatsPtpUnknownsTx,
       "f3PtpTrafficPortFlowPointStatsMinSyncResTime": f3PtpTrafficPortFlowPointStatsMinSyncResTime,
       "f3PtpTrafficPortFlowPointStatsMaxSyncResTime": f3PtpTrafficPortFlowPointStatsMaxSyncResTime,
       "f3PtpTrafficPortFlowPointStatsAvgSyncResTime": f3PtpTrafficPortFlowPointStatsAvgSyncResTime,
       "f3PtpTrafficPortFlowPointStatsMinDelayReqResTime": f3PtpTrafficPortFlowPointStatsMinDelayReqResTime,
       "f3PtpTrafficPortFlowPointStatsMaxDelayReqResTime": f3PtpTrafficPortFlowPointStatsMaxDelayReqResTime,
       "f3PtpTrafficPortFlowPointStatsAvgDelayReqResTime": f3PtpTrafficPortFlowPointStatsAvgDelayReqResTime,
       "f3PtpTrafficPortFlowPointStatsMinPDelayReqResTime": f3PtpTrafficPortFlowPointStatsMinPDelayReqResTime,
       "f3PtpTrafficPortFlowPointStatsMaxPDelayReqResTime": f3PtpTrafficPortFlowPointStatsMaxPDelayReqResTime,
       "f3PtpTrafficPortFlowPointStatsAvgPDelayReqResTime": f3PtpTrafficPortFlowPointStatsAvgPDelayReqResTime,
       "f3PtpTrafficPortFlowPointStatsMinPDelayRspResTime": f3PtpTrafficPortFlowPointStatsMinPDelayRspResTime,
       "f3PtpTrafficPortFlowPointStatsMaxPDelayRspResTime": f3PtpTrafficPortFlowPointStatsMaxPDelayRspResTime,
       "f3PtpTrafficPortFlowPointStatsAvgPDelayRspResTime": f3PtpTrafficPortFlowPointStatsAvgPDelayRspResTime,
       "f3PtpTrafficPortFlowPointStatsDestMciNoMatchDiscards": f3PtpTrafficPortFlowPointStatsDestMciNoMatchDiscards,
       "f3PtpTrafficPortFlowPointStatsTagNoMatchDiscards": f3PtpTrafficPortFlowPointStatsTagNoMatchDiscards,
       "f3PtpTrafficPortFlowPointHistoryTable": f3PtpTrafficPortFlowPointHistoryTable,
       "f3PtpTrafficPortFlowPointHistoryEntry": f3PtpTrafficPortFlowPointHistoryEntry,
       "f3PtpTrafficPortFlowPointHistoryIndex": f3PtpTrafficPortFlowPointHistoryIndex,
       "f3PtpTrafficPortFlowPointHistoryTime": f3PtpTrafficPortFlowPointHistoryTime,
       "f3PtpTrafficPortFlowPointHistoryValid": f3PtpTrafficPortFlowPointHistoryValid,
       "f3PtpTrafficPortFlowPointHistoryAction": f3PtpTrafficPortFlowPointHistoryAction,
       "f3PtpTrafficPortFlowPointHistoryAnnouncesRx": f3PtpTrafficPortFlowPointHistoryAnnouncesRx,
       "f3PtpTrafficPortFlowPointHistoryAnnouncesTx": f3PtpTrafficPortFlowPointHistoryAnnouncesTx,
       "f3PtpTrafficPortFlowPointHistorySyncsRx": f3PtpTrafficPortFlowPointHistorySyncsRx,
       "f3PtpTrafficPortFlowPointHistorySyncsTx": f3PtpTrafficPortFlowPointHistorySyncsTx,
       "f3PtpTrafficPortFlowPointHistoryFollowupsRx": f3PtpTrafficPortFlowPointHistoryFollowupsRx,
       "f3PtpTrafficPortFlowPointHistoryFollowupsTx": f3PtpTrafficPortFlowPointHistoryFollowupsTx,
       "f3PtpTrafficPortFlowPointHistoryDelayReqsRx": f3PtpTrafficPortFlowPointHistoryDelayReqsRx,
       "f3PtpTrafficPortFlowPointHistoryDelayReqsTx": f3PtpTrafficPortFlowPointHistoryDelayReqsTx,
       "f3PtpTrafficPortFlowPointHistoryDelayRspsRx": f3PtpTrafficPortFlowPointHistoryDelayRspsRx,
       "f3PtpTrafficPortFlowPointHistoryDelayRspsTx": f3PtpTrafficPortFlowPointHistoryDelayRspsTx,
       "f3PtpTrafficPortFlowPointHistoryPDelayReqsRx": f3PtpTrafficPortFlowPointHistoryPDelayReqsRx,
       "f3PtpTrafficPortFlowPointHistoryPDelayReqsTx": f3PtpTrafficPortFlowPointHistoryPDelayReqsTx,
       "f3PtpTrafficPortFlowPointHistoryPDelayRspsRx": f3PtpTrafficPortFlowPointHistoryPDelayRspsRx,
       "f3PtpTrafficPortFlowPointHistoryPDelayRspsTx": f3PtpTrafficPortFlowPointHistoryPDelayRspsTx,
       "f3PtpTrafficPortFlowPointHistoryPDelayRspFollowupsRx": f3PtpTrafficPortFlowPointHistoryPDelayRspFollowupsRx,
       "f3PtpTrafficPortFlowPointHistoryPDelayRspFollowupsTx": f3PtpTrafficPortFlowPointHistoryPDelayRspFollowupsTx,
       "f3PtpTrafficPortFlowPointHistorySignalingRx": f3PtpTrafficPortFlowPointHistorySignalingRx,
       "f3PtpTrafficPortFlowPointHistorySignalingTx": f3PtpTrafficPortFlowPointHistorySignalingTx,
       "f3PtpTrafficPortFlowPointHistoryMgmtFramesRx": f3PtpTrafficPortFlowPointHistoryMgmtFramesRx,
       "f3PtpTrafficPortFlowPointHistoryMgmtFramesTx": f3PtpTrafficPortFlowPointHistoryMgmtFramesTx,
       "f3PtpTrafficPortFlowPointHistoryPtpUnknownsRx": f3PtpTrafficPortFlowPointHistoryPtpUnknownsRx,
       "f3PtpTrafficPortFlowPointHistoryPtpUnknownsTx": f3PtpTrafficPortFlowPointHistoryPtpUnknownsTx,
       "f3PtpTrafficPortFlowPointHistoryMinSyncResTime": f3PtpTrafficPortFlowPointHistoryMinSyncResTime,
       "f3PtpTrafficPortFlowPointHistoryMaxSyncResTime": f3PtpTrafficPortFlowPointHistoryMaxSyncResTime,
       "f3PtpTrafficPortFlowPointHistoryAvgSyncResTime": f3PtpTrafficPortFlowPointHistoryAvgSyncResTime,
       "f3PtpTrafficPortFlowPointHistoryMinDelayReqResTime": f3PtpTrafficPortFlowPointHistoryMinDelayReqResTime,
       "f3PtpTrafficPortFlowPointHistoryMaxDelayReqResTime": f3PtpTrafficPortFlowPointHistoryMaxDelayReqResTime,
       "f3PtpTrafficPortFlowPointHistoryAvgDelayReqResTime": f3PtpTrafficPortFlowPointHistoryAvgDelayReqResTime,
       "f3PtpTrafficPortFlowPointHistoryMinPDelayReqResTime": f3PtpTrafficPortFlowPointHistoryMinPDelayReqResTime,
       "f3PtpTrafficPortFlowPointHistoryMaxPDelayReqResTime": f3PtpTrafficPortFlowPointHistoryMaxPDelayReqResTime,
       "f3PtpTrafficPortFlowPointHistoryAvgPDelayReqResTime": f3PtpTrafficPortFlowPointHistoryAvgPDelayReqResTime,
       "f3PtpTrafficPortFlowPointHistoryMinPDelayRspResTime": f3PtpTrafficPortFlowPointHistoryMinPDelayRspResTime,
       "f3PtpTrafficPortFlowPointHistoryMaxPDelayRspResTime": f3PtpTrafficPortFlowPointHistoryMaxPDelayRspResTime,
       "f3PtpTrafficPortFlowPointHistoryAvgPDelayRspResTime": f3PtpTrafficPortFlowPointHistoryAvgPDelayRspResTime,
       "f3PtpTrafficPortFlowPointHistoryDestMciNoMatchDiscards": f3PtpTrafficPortFlowPointHistoryDestMciNoMatchDiscards,
       "f3PtpTrafficPortFlowPointHistoryTagNoMatchDiscards": f3PtpTrafficPortFlowPointHistoryTagNoMatchDiscards,
       "f3PtpTrafficPortFlowPointThresholdTable": f3PtpTrafficPortFlowPointThresholdTable,
       "f3PtpTrafficPortFlowPointThresholdEntry": f3PtpTrafficPortFlowPointThresholdEntry,
       "f3PtpTrafficPortFlowPointThresholdIndex": f3PtpTrafficPortFlowPointThresholdIndex,
       "f3PtpTrafficPortFlowPointThresholdInterval": f3PtpTrafficPortFlowPointThresholdInterval,
       "f3PtpTrafficPortFlowPointThresholdVariable": f3PtpTrafficPortFlowPointThresholdVariable,
       "f3PtpTrafficPortFlowPointThresholdValueLo": f3PtpTrafficPortFlowPointThresholdValueLo,
       "f3PtpTrafficPortFlowPointThresholdValueHi": f3PtpTrafficPortFlowPointThresholdValueHi,
       "f3PtpTrafficPortFlowPointThresholdMonValue": f3PtpTrafficPortFlowPointThresholdMonValue,
       "f3PtpPTPPortStatsTable": f3PtpPTPPortStatsTable,
       "f3PtpPTPPortStatsEntry": f3PtpPTPPortStatsEntry,
       "f3PtpPTPPortStatsIndex": f3PtpPTPPortStatsIndex,
       "f3PtpPTPPortStatsIntervalType": f3PtpPTPPortStatsIntervalType,
       "f3PtpPTPPortStatsValid": f3PtpPTPPortStatsValid,
       "f3PtpPTPPortStatsAction": f3PtpPTPPortStatsAction,
       "f3PtpPTPPortStatsAvgAnnounceRate": f3PtpPTPPortStatsAvgAnnounceRate,
       "f3PtpPTPPortStatsAvgSyncRate": f3PtpPTPPortStatsAvgSyncRate,
       "f3PtpPTPPortStatsAvgDelayReqRate": f3PtpPTPPortStatsAvgDelayReqRate,
       "f3PtpPTPPortStatsAvgDelayRespRate": f3PtpPTPPortStatsAvgDelayRespRate,
       "f3PtpPTPPortStatsMismatchDomainDiscards": f3PtpPTPPortStatsMismatchDomainDiscards,
       "f3PtpPTPPortStatsMessageWrongTypeDiscards": f3PtpPTPPortStatsMessageWrongTypeDiscards,
       "f3PtpPTPPortStatsMessagesWrongLengthDiscards": f3PtpPTPPortStatsMessagesWrongLengthDiscards,
       "f3PtpPTPPortStatsUnknownMasterDiscards": f3PtpPTPPortStatsUnknownMasterDiscards,
       "f3PtpPTPPortStatsMinOffsetFromMaster": f3PtpPTPPortStatsMinOffsetFromMaster,
       "f3PtpPTPPortStatsMaxOffsetFromMaster": f3PtpPTPPortStatsMaxOffsetFromMaster,
       "f3PtpPTPPortStatsAvgOffsetFromMaster": f3PtpPTPPortStatsAvgOffsetFromMaster,
       "f3PtpPTPPortStatsMinSyncPathDelay": f3PtpPTPPortStatsMinSyncPathDelay,
       "f3PtpPTPPortStatsMaxSyncPathDelay": f3PtpPTPPortStatsMaxSyncPathDelay,
       "f3PtpPTPPortStatsAvgSyncPathDelay": f3PtpPTPPortStatsAvgSyncPathDelay,
       "f3PtpPTPPortStatsMinMeanPathDelay": f3PtpPTPPortStatsMinMeanPathDelay,
       "f3PtpPTPPortStatsMaxMeanPathDelay": f3PtpPTPPortStatsMaxMeanPathDelay,
       "f3PtpPTPPortStatsAvgMeanPathDelay": f3PtpPTPPortStatsAvgMeanPathDelay,
       "f3PtpPTPPortStatsMsgMiscDiscards": f3PtpPTPPortStatsMsgMiscDiscards,
       "f3PtpPTPPortHistoryTable": f3PtpPTPPortHistoryTable,
       "f3PtpPTPPortHistoryEntry": f3PtpPTPPortHistoryEntry,
       "f3PtpPTPPortHistoryIndex": f3PtpPTPPortHistoryIndex,
       "f3PtpPTPPortHistoryTime": f3PtpPTPPortHistoryTime,
       "f3PtpPTPPortHistoryValid": f3PtpPTPPortHistoryValid,
       "f3PtpPTPPortHistoryAction": f3PtpPTPPortHistoryAction,
       "f3PtpPTPPortHistoryAvgAnnounceRate": f3PtpPTPPortHistoryAvgAnnounceRate,
       "f3PtpPTPPortHistoryAvgSyncRate": f3PtpPTPPortHistoryAvgSyncRate,
       "f3PtpPTPPortHistoryAvgDelayReqRate": f3PtpPTPPortHistoryAvgDelayReqRate,
       "f3PtpPTPPortHistoryAvgDelayRespRate": f3PtpPTPPortHistoryAvgDelayRespRate,
       "f3PtpPTPPortHistoryMismatchDomainDiscards": f3PtpPTPPortHistoryMismatchDomainDiscards,
       "f3PtpPTPPortHistoryMessageWrongTypeDiscards": f3PtpPTPPortHistoryMessageWrongTypeDiscards,
       "f3PtpPTPPortHistoryMessagesWrongLengthDiscards": f3PtpPTPPortHistoryMessagesWrongLengthDiscards,
       "f3PtpPTPPortHistoryUnknownMasterDiscards": f3PtpPTPPortHistoryUnknownMasterDiscards,
       "f3PtpPTPPortHistoryMinOffsetFromMaster": f3PtpPTPPortHistoryMinOffsetFromMaster,
       "f3PtpPTPPortHistoryMaxOffsetFromMaster": f3PtpPTPPortHistoryMaxOffsetFromMaster,
       "f3PtpPTPPortHistoryAvgOffsetFromMaster": f3PtpPTPPortHistoryAvgOffsetFromMaster,
       "f3PtpPTPPortHistoryMinSyncPathDelay": f3PtpPTPPortHistoryMinSyncPathDelay,
       "f3PtpPTPPortHistoryMaxSyncPathDelay": f3PtpPTPPortHistoryMaxSyncPathDelay,
       "f3PtpPTPPortHistoryAvgSyncPathDelay": f3PtpPTPPortHistoryAvgSyncPathDelay,
       "f3PtpPTPPortHistoryMinMeanPathDelay": f3PtpPTPPortHistoryMinMeanPathDelay,
       "f3PtpPTPPortHistoryMaxMeanPathDelay": f3PtpPTPPortHistoryMaxMeanPathDelay,
       "f3PtpPTPPortHistoryAvgMeanPathDelay": f3PtpPTPPortHistoryAvgMeanPathDelay,
       "f3PtpPTPPortHistoryMsgMiscDiscards": f3PtpPTPPortHistoryMsgMiscDiscards,
       "f3PtpPTPPortThresholdTable": f3PtpPTPPortThresholdTable,
       "f3PtpPTPPortThresholdEntry": f3PtpPTPPortThresholdEntry,
       "f3PtpPTPPortThresholdIndex": f3PtpPTPPortThresholdIndex,
       "f3PtpPTPPortThresholdInterval": f3PtpPTPPortThresholdInterval,
       "f3PtpPTPPortThresholdVariable": f3PtpPTPPortThresholdVariable,
       "f3PtpPTPPortThresholdValueLo": f3PtpPTPPortThresholdValueLo,
       "f3PtpPTPPortThresholdValueHi": f3PtpPTPPortThresholdValueHi,
       "f3PtpPTPPortThresholdMonValue": f3PtpPTPPortThresholdMonValue,
       "f3PtpPTPClockStatsTable": f3PtpPTPClockStatsTable,
       "f3PtpPTPClockStatsEntry": f3PtpPTPClockStatsEntry,
       "f3PtpPTPClockStatsIndex": f3PtpPTPClockStatsIndex,
       "f3PtpPTPClockStatsIntervalType": f3PtpPTPClockStatsIntervalType,
       "f3PtpPTPClockStatsValid": f3PtpPTPClockStatsValid,
       "f3PtpPTPClockStatsAction": f3PtpPTPClockStatsAction,
       "f3PtpPTPClockStatsMinOffsetFromMaster": f3PtpPTPClockStatsMinOffsetFromMaster,
       "f3PtpPTPClockStatsMaxOffsetFromMaster": f3PtpPTPClockStatsMaxOffsetFromMaster,
       "f3PtpPTPClockStatsAvgOffsetFromMaster": f3PtpPTPClockStatsAvgOffsetFromMaster,
       "f3PtpPTPClockStatsMinSyncPathDelay": f3PtpPTPClockStatsMinSyncPathDelay,
       "f3PtpPTPClockStatsMaxSyncPathDelay": f3PtpPTPClockStatsMaxSyncPathDelay,
       "f3PtpPTPClockStatsAvgSyncPathDelay": f3PtpPTPClockStatsAvgSyncPathDelay,
       "f3PtpPTPClockStatsMinMeanPathDelay": f3PtpPTPClockStatsMinMeanPathDelay,
       "f3PtpPTPClockStatsMaxMeanPathDelay": f3PtpPTPClockStatsMaxMeanPathDelay,
       "f3PtpPTPClockStatsAvgMeanPathDelay": f3PtpPTPClockStatsAvgMeanPathDelay,
       "f3PtpPTPClockHistoryTable": f3PtpPTPClockHistoryTable,
       "f3PtpPTPClockHistoryEntry": f3PtpPTPClockHistoryEntry,
       "f3PtpPTPClockHistoryIndex": f3PtpPTPClockHistoryIndex,
       "f3PtpPTPClockHistoryTime": f3PtpPTPClockHistoryTime,
       "f3PtpPTPClockHistoryValid": f3PtpPTPClockHistoryValid,
       "f3PtpPTPClockHistoryAction": f3PtpPTPClockHistoryAction,
       "f3PtpPTPClockHistoryMinOffsetFromMaster": f3PtpPTPClockHistoryMinOffsetFromMaster,
       "f3PtpPTPClockHistoryMaxOffsetFromMaster": f3PtpPTPClockHistoryMaxOffsetFromMaster,
       "f3PtpPTPClockHistoryAvgOffsetFromMaster": f3PtpPTPClockHistoryAvgOffsetFromMaster,
       "f3PtpPTPClockHistoryMinSyncPathDelay": f3PtpPTPClockHistoryMinSyncPathDelay,
       "f3PtpPTPClockHistoryMaxSyncPathDelay": f3PtpPTPClockHistoryMaxSyncPathDelay,
       "f3PtpPTPClockHistoryAvgSyncPathDelay": f3PtpPTPClockHistoryAvgSyncPathDelay,
       "f3PtpPTPClockHistoryMinMeanPathDelay": f3PtpPTPClockHistoryMinMeanPathDelay,
       "f3PtpPTPClockHistoryMaxMeanPathDelay": f3PtpPTPClockHistoryMaxMeanPathDelay,
       "f3PtpPTPClockHistoryAvgMeanPathDelay": f3PtpPTPClockHistoryAvgMeanPathDelay,
       "f3PtpPTPClockThresholdTable": f3PtpPTPClockThresholdTable,
       "f3PtpPTPClockThresholdEntry": f3PtpPTPClockThresholdEntry,
       "f3PtpPTPClockThresholdIndex": f3PtpPTPClockThresholdIndex,
       "f3PtpPTPClockThresholdInterval": f3PtpPTPClockThresholdInterval,
       "f3PtpPTPClockThresholdVariable": f3PtpPTPClockThresholdVariable,
       "f3PtpPTPClockThresholdValueLo": f3PtpPTPClockThresholdValueLo,
       "f3PtpPTPClockThresholdValueHi": f3PtpPTPClockThresholdValueHi,
       "f3PtpPTPClockThresholdMonValue": f3PtpPTPClockThresholdMonValue,
       "f3PtpL3PTPPortStatsTable": f3PtpL3PTPPortStatsTable,
       "f3PtpL3PTPPortStatsEntry": f3PtpL3PTPPortStatsEntry,
       "f3PtpL3PTPPortStatsIndex": f3PtpL3PTPPortStatsIndex,
       "f3PtpL3PTPPortStatsIntervalType": f3PtpL3PTPPortStatsIntervalType,
       "f3PtpL3PTPPortStatsValid": f3PtpL3PTPPortStatsValid,
       "f3PtpL3PTPPortStatsAction": f3PtpL3PTPPortStatsAction,
       "f3PtpL3PTPPortStatsAvgAnnounceRate": f3PtpL3PTPPortStatsAvgAnnounceRate,
       "f3PtpL3PTPPortStatsAvgSyncRate": f3PtpL3PTPPortStatsAvgSyncRate,
       "f3PtpL3PTPPortStatsAvgDelayReqRate": f3PtpL3PTPPortStatsAvgDelayReqRate,
       "f3PtpL3PTPPortStatsAvgDelayRespRate": f3PtpL3PTPPortStatsAvgDelayRespRate,
       "f3PtpL3PTPPortStatsMismatchDomainDiscards": f3PtpL3PTPPortStatsMismatchDomainDiscards,
       "f3PtpL3PTPPortStatsMessageWrongTypeDiscards": f3PtpL3PTPPortStatsMessageWrongTypeDiscards,
       "f3PtpL3PTPPortStatsMessagesWrongLengthDiscards": f3PtpL3PTPPortStatsMessagesWrongLengthDiscards,
       "f3PtpL3PTPPortStatsUnknownMasterDiscards": f3PtpL3PTPPortStatsUnknownMasterDiscards,
       "f3PtpL3PTPPortStatsMinOffsetFromMaster": f3PtpL3PTPPortStatsMinOffsetFromMaster,
       "f3PtpL3PTPPortStatsMaxOffsetFromMaster": f3PtpL3PTPPortStatsMaxOffsetFromMaster,
       "f3PtpL3PTPPortStatsAvgOffsetFromMaster": f3PtpL3PTPPortStatsAvgOffsetFromMaster,
       "f3PtpL3PTPPortStatsMinSyncPathDelay": f3PtpL3PTPPortStatsMinSyncPathDelay,
       "f3PtpL3PTPPortStatsMaxSyncPathDelay": f3PtpL3PTPPortStatsMaxSyncPathDelay,
       "f3PtpL3PTPPortStatsAvgSyncPathDelay": f3PtpL3PTPPortStatsAvgSyncPathDelay,
       "f3PtpL3PTPPortStatsMinMeanPathDelay": f3PtpL3PTPPortStatsMinMeanPathDelay,
       "f3PtpL3PTPPortStatsMaxMeanPathDelay": f3PtpL3PTPPortStatsMaxMeanPathDelay,
       "f3PtpL3PTPPortStatsAvgMeanPathDelay": f3PtpL3PTPPortStatsAvgMeanPathDelay,
       "f3PtpL3PTPPortStatsMsgMiscDiscards": f3PtpL3PTPPortStatsMsgMiscDiscards,
       "f3PtpL3PTPPortHistoryTable": f3PtpL3PTPPortHistoryTable,
       "f3PtpL3PTPPortHistoryEntry": f3PtpL3PTPPortHistoryEntry,
       "f3PtpL3PTPPortHistoryIndex": f3PtpL3PTPPortHistoryIndex,
       "f3PtpL3PTPPortHistoryTime": f3PtpL3PTPPortHistoryTime,
       "f3PtpL3PTPPortHistoryValid": f3PtpL3PTPPortHistoryValid,
       "f3PtpL3PTPPortHistoryAction": f3PtpL3PTPPortHistoryAction,
       "f3PtpL3PTPPortHistoryAvgAnnounceRate": f3PtpL3PTPPortHistoryAvgAnnounceRate,
       "f3PtpL3PTPPortHistoryAvgSyncRate": f3PtpL3PTPPortHistoryAvgSyncRate,
       "f3PtpL3PTPPortHistoryAvgDelayReqRate": f3PtpL3PTPPortHistoryAvgDelayReqRate,
       "f3PtpL3PTPPortHistoryAvgDelayRespRate": f3PtpL3PTPPortHistoryAvgDelayRespRate,
       "f3PtpL3PTPPortHistoryMismatchDomainDiscards": f3PtpL3PTPPortHistoryMismatchDomainDiscards,
       "f3PtpL3PTPPortHistoryMessageWrongTypeDiscards": f3PtpL3PTPPortHistoryMessageWrongTypeDiscards,
       "f3PtpL3PTPPortHistoryMessagesWrongLengthDiscards": f3PtpL3PTPPortHistoryMessagesWrongLengthDiscards,
       "f3PtpL3PTPPortHistoryUnknownMasterDiscards": f3PtpL3PTPPortHistoryUnknownMasterDiscards,
       "f3PtpL3PTPPortHistoryMinOffsetFromMaster": f3PtpL3PTPPortHistoryMinOffsetFromMaster,
       "f3PtpL3PTPPortHistoryMaxOffsetFromMaster": f3PtpL3PTPPortHistoryMaxOffsetFromMaster,
       "f3PtpL3PTPPortHistoryAvgOffsetFromMaster": f3PtpL3PTPPortHistoryAvgOffsetFromMaster,
       "f3PtpL3PTPPortHistoryMinSyncPathDelay": f3PtpL3PTPPortHistoryMinSyncPathDelay,
       "f3PtpL3PTPPortHistoryMaxSyncPathDelay": f3PtpL3PTPPortHistoryMaxSyncPathDelay,
       "f3PtpL3PTPPortHistoryAvgSyncPathDelay": f3PtpL3PTPPortHistoryAvgSyncPathDelay,
       "f3PtpL3PTPPortHistoryMinMeanPathDelay": f3PtpL3PTPPortHistoryMinMeanPathDelay,
       "f3PtpL3PTPPortHistoryMaxMeanPathDelay": f3PtpL3PTPPortHistoryMaxMeanPathDelay,
       "f3PtpL3PTPPortHistoryAvgMeanPathDelay": f3PtpL3PTPPortHistoryAvgMeanPathDelay,
       "f3PtpL3PTPPortHistoryMsgMiscDiscards": f3PtpL3PTPPortHistoryMsgMiscDiscards,
       "f3PtpL3PTPPortThresholdTable": f3PtpL3PTPPortThresholdTable,
       "f3PtpL3PTPPortThresholdEntry": f3PtpL3PTPPortThresholdEntry,
       "f3PtpL3PTPPortThresholdIndex": f3PtpL3PTPPortThresholdIndex,
       "f3PtpL3PTPPortThresholdInterval": f3PtpL3PTPPortThresholdInterval,
       "f3PtpL3PTPPortThresholdVariable": f3PtpL3PTPPortThresholdVariable,
       "f3PtpL3PTPPortThresholdValueLo": f3PtpL3PTPPortThresholdValueLo,
       "f3PtpL3PTPPortThresholdValueHi": f3PtpL3PTPPortThresholdValueHi,
       "f3PtpL3PTPPortThresholdMonValue": f3PtpL3PTPPortThresholdMonValue,
       "f3PtpPerformanceNotifications": f3PtpPerformanceNotifications,
       "f3PtpAccPortFlowPointThresholdCrossingAlert": f3PtpAccPortFlowPointThresholdCrossingAlert,
       "f3PtpNetPortFlowPointThresholdCrossingAlert": f3PtpNetPortFlowPointThresholdCrossingAlert,
       "f3PtpSOOCCrossingAlert": f3PtpSOOCCrossingAlert,
       "f3PtpTSCrossingAlert": f3PtpTSCrossingAlert,
       "f3PtpMCICrossingAlert": f3PtpMCICrossingAlert,
       "f3PtpRemoteSlaveCrossingAlert": f3PtpRemoteSlaveCrossingAlert,
       "f3PtpTrafficPortFlowPointThresholdCrossingAlert": f3PtpTrafficPortFlowPointThresholdCrossingAlert,
       "f3PtpPTPPortCrossingAlert": f3PtpPTPPortCrossingAlert,
       "f3PtpPTPClockCrossingAlert": f3PtpPTPClockCrossingAlert,
       "f3PtpL3PTPPortCrossingAlert": f3PtpL3PTPPortCrossingAlert,
       "f3PtpConformance": f3PtpConformance,
       "f3PtpCompliances": f3PtpCompliances,
       "f3PtpCompliance": f3PtpCompliance,
       "f3PtpGroups": f3PtpGroups,
       "f3PtpObjectGroup": f3PtpObjectGroup,
       "f3PtpPerfObjectGroup": f3PtpPerfObjectGroup,
       "f3PtpPerfNotifGroup": f3PtpPerfNotifGroup,
       "f3PtpStatusChangeNotifGroup": f3PtpStatusChangeNotifGroup,
       "f3PtpBoundaryClockObjectGroup": f3PtpBoundaryClockObjectGroup,
       "f3PtpBoundaryClockNotifGroup": f3PtpBoundaryClockNotifGroup,
       "f3PtpProtObjectGroup": f3PtpProtObjectGroup,
       "f3PtpStatusChangeNotifications": f3PtpStatusChangeNotifications,
       "f3PtpTSStatusChangeTrap": f3PtpTSStatusChangeTrap,
       "f3PtpMasterClockStatusChangeTrap": f3PtpMasterClockStatusChangeTrap,
       "f3PtpBCStatusChangeTrap": f3PtpBCStatusChangeTrap,
       "f3PtpDynamicRemoteSlaveStatusChangeTrap": f3PtpDynamicRemoteSlaveStatusChangeTrap}
)
