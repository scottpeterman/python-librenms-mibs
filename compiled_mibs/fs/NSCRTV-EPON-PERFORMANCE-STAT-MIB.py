# SNMP MIB module (NSCRTV-EPON-PERFORMANCE-STAT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\fs\NSCRTV-EPON-PERFORMANCE-STAT-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:46:52 2025
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

(AutoNegotiationTechAbility,
 EponAlarmCode,
 EponAlarmInstance,
 EponCardIndex,
 EponDeviceIndex,
 EponPortIndex,
 EponSeverityType,
 EponStats15MinRecordType,
 EponStats24HourRecordType,
 EponStatsThresholdType,
 TAddress,
 performanceStatisticObjects) = mibBuilder.importSymbols(
    "NSCRTV-EPONEOC-EPON-MIB",
    "AutoNegotiationTechAbility",
    "EponAlarmCode",
    "EponAlarmInstance",
    "EponCardIndex",
    "EponDeviceIndex",
    "EponPortIndex",
    "EponSeverityType",
    "EponStats15MinRecordType",
    "EponStats24HourRecordType",
    "EponStatsThresholdType",
    "TAddress",
    "performanceStatisticObjects")

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

(DateAndTime,
 DisplayString,
 MacAddress,
 PhysAddress,
 RowStatus,
 TextualConvention,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CurStatsTable_Object = MibTable
curStatsTable = _CurStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 10, 1)
)
if mibBuilder.loadTexts:
    curStatsTable.setStatus("current")
_CurStatsEntry_Object = MibTableRow
curStatsEntry = _CurStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 10, 1, 1)
)
curStatsEntry.setIndexNames(
    (0, "NSCRTV-EPON-PERFORMANCE-STAT-MIB", "curStatsDeviceIndex"),
    (0, "NSCRTV-EPON-PERFORMANCE-STAT-MIB", "curStatsCardIndex"),
    (0, "NSCRTV-EPON-PERFORMANCE-STAT-MIB", "curStatsPortIndex"),
)
if mibBuilder.loadTexts:
    curStatsEntry.setStatus("current")
_CurStatsDeviceIndex_Type = EponDeviceIndex
_CurStatsDeviceIndex_Object = MibTableColumn
curStatsDeviceIndex = _CurStatsDeviceIndex_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 10, 1, 1, 1),
    _CurStatsDeviceIndex_Type()
)
curStatsDeviceIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    curStatsDeviceIndex.setStatus("current")
_CurStatsCardIndex_Type = EponCardIndex
_CurStatsCardIndex_Object = MibTableColumn
curStatsCardIndex = _CurStatsCardIndex_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 10, 1, 1, 2),
    _CurStatsCardIndex_Type()
)
curStatsCardIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    curStatsCardIndex.setStatus("current")
_CurStatsPortIndex_Type = EponPortIndex
_CurStatsPortIndex_Object = MibTableColumn
curStatsPortIndex = _CurStatsPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 10, 1, 1, 3),
    _CurStatsPortIndex_Type()
)
curStatsPortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    curStatsPortIndex.setStatus("current")
_CurStatsInOctets_Type = Counter64
_CurStatsInOctets_Object = MibTableColumn
curStatsInOctets = _CurStatsInOctets_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 10, 1, 1, 4),
    _CurStatsInOctets_Type()
)
curStatsInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    curStatsInOctets.setStatus("current")
_CurStatsInPkts_Type = Counter64
_CurStatsInPkts_Object = MibTableColumn
curStatsInPkts = _CurStatsInPkts_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 10, 1, 1, 5),
    _CurStatsInPkts_Type()
)
curStatsInPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    curStatsInPkts.setStatus("current")
_CurStatsInBroadcastPkts_Type = Counter64
_CurStatsInBroadcastPkts_Object = MibTableColumn
curStatsInBroadcastPkts = _CurStatsInBroadcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 10, 1, 1, 6),
    _CurStatsInBroadcastPkts_Type()
)
curStatsInBroadcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    curStatsInBroadcastPkts.setStatus("current")
_CurStatsInMulticastPkts_Type = Counter64
_CurStatsInMulticastPkts_Object = MibTableColumn
curStatsInMulticastPkts = _CurStatsInMulticastPkts_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 10, 1, 1, 7),
    _CurStatsInMulticastPkts_Type()
)
curStatsInMulticastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    curStatsInMulticastPkts.setStatus("current")
_CurStatsInPkts64Octets_Type = Counter64
_CurStatsInPkts64Octets_Object = MibTableColumn
curStatsInPkts64Octets = _CurStatsInPkts64Octets_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 10, 1, 1, 8),
    _CurStatsInPkts64Octets_Type()
)
curStatsInPkts64Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    curStatsInPkts64Octets.setStatus("current")
_CurStatsInPkts65to127Octets_Type = Counter64
_CurStatsInPkts65to127Octets_Object = MibTableColumn
curStatsInPkts65to127Octets = _CurStatsInPkts65to127Octets_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 10, 1, 1, 9),
    _CurStatsInPkts65to127Octets_Type()
)
curStatsInPkts65to127Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    curStatsInPkts65to127Octets.setStatus("current")
_CurStatsInPkts128to255Octets_Type = Counter64
_CurStatsInPkts128to255Octets_Object = MibTableColumn
curStatsInPkts128to255Octets = _CurStatsInPkts128to255Octets_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 10, 1, 1, 10),
    _CurStatsInPkts128to255Octets_Type()
)
curStatsInPkts128to255Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    curStatsInPkts128to255Octets.setStatus("current")
_CurStatsInPkts256to511Octets_Type = Counter64
_CurStatsInPkts256to511Octets_Object = MibTableColumn
curStatsInPkts256to511Octets = _CurStatsInPkts256to511Octets_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 10, 1, 1, 11),
    _CurStatsInPkts256to511Octets_Type()
)
curStatsInPkts256to511Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    curStatsInPkts256to511Octets.setStatus("current")
_CurStatsInPkts512to1023Octets_Type = Counter64
_CurStatsInPkts512to1023Octets_Object = MibTableColumn
curStatsInPkts512to1023Octets = _CurStatsInPkts512to1023Octets_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 10, 1, 1, 12),
    _CurStatsInPkts512to1023Octets_Type()
)
curStatsInPkts512to1023Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    curStatsInPkts512to1023Octets.setStatus("current")
_CurStatsInPkts1024to1518Octets_Type = Counter64
_CurStatsInPkts1024to1518Octets_Object = MibTableColumn
curStatsInPkts1024to1518Octets = _CurStatsInPkts1024to1518Octets_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 10, 1, 1, 13),
    _CurStatsInPkts1024to1518Octets_Type()
)
curStatsInPkts1024to1518Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    curStatsInPkts1024to1518Octets.setStatus("current")
_CurStatsInPkts1519to1522Octets_Type = Counter64
_CurStatsInPkts1519to1522Octets_Object = MibTableColumn
curStatsInPkts1519to1522Octets = _CurStatsInPkts1519to1522Octets_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 10, 1, 1, 14),
    _CurStatsInPkts1519to1522Octets_Type()
)
curStatsInPkts1519to1522Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    curStatsInPkts1519to1522Octets.setStatus("current")
_CurStatsInUndersizePkts_Type = Counter64
_CurStatsInUndersizePkts_Object = MibTableColumn
curStatsInUndersizePkts = _CurStatsInUndersizePkts_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 10, 1, 1, 15),
    _CurStatsInUndersizePkts_Type()
)
curStatsInUndersizePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    curStatsInUndersizePkts.setStatus("current")
_CurStatsInOversizePkts_Type = Counter64
_CurStatsInOversizePkts_Object = MibTableColumn
curStatsInOversizePkts = _CurStatsInOversizePkts_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 10, 1, 1, 16),
    _CurStatsInOversizePkts_Type()
)
curStatsInOversizePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    curStatsInOversizePkts.setStatus("current")
_CurStatsInFragments_Type = Counter64
_CurStatsInFragments_Object = MibTableColumn
curStatsInFragments = _CurStatsInFragments_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 10, 1, 1, 17),
    _CurStatsInFragments_Type()
)
curStatsInFragments.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    curStatsInFragments.setStatus("current")
_CurStatsInMpcpFrames_Type = Counter64
_CurStatsInMpcpFrames_Object = MibTableColumn
curStatsInMpcpFrames = _CurStatsInMpcpFrames_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 10, 1, 1, 18),
    _CurStatsInMpcpFrames_Type()
)
curStatsInMpcpFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    curStatsInMpcpFrames.setStatus("current")
_CurStatsInMpcpOctets_Type = Counter64
_CurStatsInMpcpOctets_Object = MibTableColumn
curStatsInMpcpOctets = _CurStatsInMpcpOctets_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 10, 1, 1, 19),
    _CurStatsInMpcpOctets_Type()
)
curStatsInMpcpOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    curStatsInMpcpOctets.setStatus("current")
_CurStatsInOAMFrames_Type = Counter64
_CurStatsInOAMFrames_Object = MibTableColumn
curStatsInOAMFrames = _CurStatsInOAMFrames_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 10, 1, 1, 20),
    _CurStatsInOAMFrames_Type()
)
curStatsInOAMFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    curStatsInOAMFrames.setStatus("current")
_CurStatsInOAMOctets_Type = Counter64
_CurStatsInOAMOctets_Object = MibTableColumn
curStatsInOAMOctets = _CurStatsInOAMOctets_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 10, 1, 1, 21),
    _CurStatsInOAMOctets_Type()
)
curStatsInOAMOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    curStatsInOAMOctets.setStatus("current")
_CurStatsInCRCErrorPkts_Type = Counter64
_CurStatsInCRCErrorPkts_Object = MibTableColumn
curStatsInCRCErrorPkts = _CurStatsInCRCErrorPkts_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 10, 1, 1, 22),
    _CurStatsInCRCErrorPkts_Type()
)
curStatsInCRCErrorPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    curStatsInCRCErrorPkts.setStatus("current")
_CurStatsInDropEvents_Type = Counter64
_CurStatsInDropEvents_Object = MibTableColumn
curStatsInDropEvents = _CurStatsInDropEvents_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 10, 1, 1, 23),
    _CurStatsInDropEvents_Type()
)
curStatsInDropEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    curStatsInDropEvents.setStatus("current")
_CurStatsInJabbers_Type = Counter64
_CurStatsInJabbers_Object = MibTableColumn
curStatsInJabbers = _CurStatsInJabbers_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 10, 1, 1, 24),
    _CurStatsInJabbers_Type()
)
curStatsInJabbers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    curStatsInJabbers.setStatus("current")
_CurStatsInCollision_Type = Counter64
_CurStatsInCollision_Object = MibTableColumn
curStatsInCollision = _CurStatsInCollision_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 10, 1, 1, 25),
    _CurStatsInCollision_Type()
)
curStatsInCollision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    curStatsInCollision.setStatus("current")
_CurStatsOutOctets_Type = Counter64
_CurStatsOutOctets_Object = MibTableColumn
curStatsOutOctets = _CurStatsOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 10, 1, 1, 26),
    _CurStatsOutOctets_Type()
)
curStatsOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    curStatsOutOctets.setStatus("current")
_CurStatsOutPkts_Type = Counter64
_CurStatsOutPkts_Object = MibTableColumn
curStatsOutPkts = _CurStatsOutPkts_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 10, 1, 1, 27),
    _CurStatsOutPkts_Type()
)
curStatsOutPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    curStatsOutPkts.setStatus("current")
_CurStatsOutBroadcastPkts_Type = Counter64
_CurStatsOutBroadcastPkts_Object = MibTableColumn
curStatsOutBroadcastPkts = _CurStatsOutBroadcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 10, 1, 1, 28),
    _CurStatsOutBroadcastPkts_Type()
)
curStatsOutBroadcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    curStatsOutBroadcastPkts.setStatus("current")
_CurStatsOutMulticastPkts_Type = Counter64
_CurStatsOutMulticastPkts_Object = MibTableColumn
curStatsOutMulticastPkts = _CurStatsOutMulticastPkts_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 10, 1, 1, 29),
    _CurStatsOutMulticastPkts_Type()
)
curStatsOutMulticastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    curStatsOutMulticastPkts.setStatus("current")
_CurStatsOutPkts64Octets_Type = Counter64
_CurStatsOutPkts64Octets_Object = MibTableColumn
curStatsOutPkts64Octets = _CurStatsOutPkts64Octets_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 10, 1, 1, 30),
    _CurStatsOutPkts64Octets_Type()
)
curStatsOutPkts64Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    curStatsOutPkts64Octets.setStatus("current")
_CurStatsOutPkts65to127Octets_Type = Counter64
_CurStatsOutPkts65to127Octets_Object = MibTableColumn
curStatsOutPkts65to127Octets = _CurStatsOutPkts65to127Octets_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 10, 1, 1, 31),
    _CurStatsOutPkts65to127Octets_Type()
)
curStatsOutPkts65to127Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    curStatsOutPkts65to127Octets.setStatus("current")
_CurStatsOutPkts128to255Octets_Type = Counter64
_CurStatsOutPkts128to255Octets_Object = MibTableColumn
curStatsOutPkts128to255Octets = _CurStatsOutPkts128to255Octets_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 10, 1, 1, 32),
    _CurStatsOutPkts128to255Octets_Type()
)
curStatsOutPkts128to255Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    curStatsOutPkts128to255Octets.setStatus("current")
_CurStatsOutPkts256to511Octets_Type = Counter64
_CurStatsOutPkts256to511Octets_Object = MibTableColumn
curStatsOutPkts256to511Octets = _CurStatsOutPkts256to511Octets_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 10, 1, 1, 33),
    _CurStatsOutPkts256to511Octets_Type()
)
curStatsOutPkts256to511Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    curStatsOutPkts256to511Octets.setStatus("current")
_CurStatsOutPkts512to1023Octets_Type = Counter64
_CurStatsOutPkts512to1023Octets_Object = MibTableColumn
curStatsOutPkts512to1023Octets = _CurStatsOutPkts512to1023Octets_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 10, 1, 1, 34),
    _CurStatsOutPkts512to1023Octets_Type()
)
curStatsOutPkts512to1023Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    curStatsOutPkts512to1023Octets.setStatus("current")
_CurStatsOutPkts1024to1518Octets_Type = Counter64
_CurStatsOutPkts1024to1518Octets_Object = MibTableColumn
curStatsOutPkts1024to1518Octets = _CurStatsOutPkts1024to1518Octets_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 10, 1, 1, 35),
    _CurStatsOutPkts1024to1518Octets_Type()
)
curStatsOutPkts1024to1518Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    curStatsOutPkts1024to1518Octets.setStatus("current")
_CurStatsOutPkts1519o1522Octets_Type = Counter64
_CurStatsOutPkts1519o1522Octets_Object = MibTableColumn
curStatsOutPkts1519o1522Octets = _CurStatsOutPkts1519o1522Octets_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 10, 1, 1, 36),
    _CurStatsOutPkts1519o1522Octets_Type()
)
curStatsOutPkts1519o1522Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    curStatsOutPkts1519o1522Octets.setStatus("current")
_CurStatsOutUndersizePkts_Type = Counter64
_CurStatsOutUndersizePkts_Object = MibTableColumn
curStatsOutUndersizePkts = _CurStatsOutUndersizePkts_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 10, 1, 1, 37),
    _CurStatsOutUndersizePkts_Type()
)
curStatsOutUndersizePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    curStatsOutUndersizePkts.setStatus("current")
_CurStatsOutOversizePkts_Type = Counter64
_CurStatsOutOversizePkts_Object = MibTableColumn
curStatsOutOversizePkts = _CurStatsOutOversizePkts_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 10, 1, 1, 38),
    _CurStatsOutOversizePkts_Type()
)
curStatsOutOversizePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    curStatsOutOversizePkts.setStatus("current")
_CurStatsOutFragments_Type = Counter64
_CurStatsOutFragments_Object = MibTableColumn
curStatsOutFragments = _CurStatsOutFragments_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 10, 1, 1, 39),
    _CurStatsOutFragments_Type()
)
curStatsOutFragments.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    curStatsOutFragments.setStatus("current")
_CurStatsOutMpcpFrames_Type = Counter64
_CurStatsOutMpcpFrames_Object = MibTableColumn
curStatsOutMpcpFrames = _CurStatsOutMpcpFrames_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 10, 1, 1, 40),
    _CurStatsOutMpcpFrames_Type()
)
curStatsOutMpcpFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    curStatsOutMpcpFrames.setStatus("current")
_CurStatsOutMpcpOctets_Type = Counter64
_CurStatsOutMpcpOctets_Object = MibTableColumn
curStatsOutMpcpOctets = _CurStatsOutMpcpOctets_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 10, 1, 1, 41),
    _CurStatsOutMpcpOctets_Type()
)
curStatsOutMpcpOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    curStatsOutMpcpOctets.setStatus("current")
_CurStatsOutOAMFrames_Type = Counter64
_CurStatsOutOAMFrames_Object = MibTableColumn
curStatsOutOAMFrames = _CurStatsOutOAMFrames_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 10, 1, 1, 42),
    _CurStatsOutOAMFrames_Type()
)
curStatsOutOAMFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    curStatsOutOAMFrames.setStatus("current")
_CurStatsOutOAMOctets_Type = Counter64
_CurStatsOutOAMOctets_Object = MibTableColumn
curStatsOutOAMOctets = _CurStatsOutOAMOctets_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 10, 1, 1, 43),
    _CurStatsOutOAMOctets_Type()
)
curStatsOutOAMOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    curStatsOutOAMOctets.setStatus("current")
_CurStatsOutCRCErrorPkts_Type = Counter64
_CurStatsOutCRCErrorPkts_Object = MibTableColumn
curStatsOutCRCErrorPkts = _CurStatsOutCRCErrorPkts_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 10, 1, 1, 44),
    _CurStatsOutCRCErrorPkts_Type()
)
curStatsOutCRCErrorPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    curStatsOutCRCErrorPkts.setStatus("current")
_CurStatsOutDropEvents_Type = Counter64
_CurStatsOutDropEvents_Object = MibTableColumn
curStatsOutDropEvents = _CurStatsOutDropEvents_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 10, 1, 1, 45),
    _CurStatsOutDropEvents_Type()
)
curStatsOutDropEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    curStatsOutDropEvents.setStatus("current")
_CurStatsOutJabbers_Type = Counter64
_CurStatsOutJabbers_Object = MibTableColumn
curStatsOutJabbers = _CurStatsOutJabbers_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 10, 1, 1, 46),
    _CurStatsOutJabbers_Type()
)
curStatsOutJabbers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    curStatsOutJabbers.setStatus("current")
_CurStatsOutCollision_Type = Counter64
_CurStatsOutCollision_Object = MibTableColumn
curStatsOutCollision = _CurStatsOutCollision_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 10, 1, 1, 47),
    _CurStatsOutCollision_Type()
)
curStatsOutCollision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    curStatsOutCollision.setStatus("current")


class _CurStatsStatusAndAction_Type(Integer32):
    """Custom type curStatsStatusAndAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("clean", 2))
    )


_CurStatsStatusAndAction_Type.__name__ = "Integer32"
_CurStatsStatusAndAction_Object = MibTableColumn
curStatsStatusAndAction = _CurStatsStatusAndAction_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 10, 1, 1, 48),
    _CurStatsStatusAndAction_Type()
)
curStatsStatusAndAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    curStatsStatusAndAction.setStatus("current")
_Stats15Table_Object = MibTable
stats15Table = _Stats15Table_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 10, 2)
)
if mibBuilder.loadTexts:
    stats15Table.setStatus("current")
_Stats15Entry_Object = MibTableRow
stats15Entry = _Stats15Entry_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 10, 2, 1)
)
stats15Entry.setIndexNames(
    (0, "NSCRTV-EPON-PERFORMANCE-STAT-MIB", "stats15DeviceIndex"),
    (0, "NSCRTV-EPON-PERFORMANCE-STAT-MIB", "stats15CardIndex"),
    (0, "NSCRTV-EPON-PERFORMANCE-STAT-MIB", "stats15PortIndex"),
    (0, "NSCRTV-EPON-PERFORMANCE-STAT-MIB", "stats15Index"),
)
if mibBuilder.loadTexts:
    stats15Entry.setStatus("current")
_Stats15DeviceIndex_Type = EponDeviceIndex
_Stats15DeviceIndex_Object = MibTableColumn
stats15DeviceIndex = _Stats15DeviceIndex_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 10, 2, 1, 1),
    _Stats15DeviceIndex_Type()
)
stats15DeviceIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    stats15DeviceIndex.setStatus("current")
_Stats15CardIndex_Type = EponCardIndex
_Stats15CardIndex_Object = MibTableColumn
stats15CardIndex = _Stats15CardIndex_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 10, 2, 1, 2),
    _Stats15CardIndex_Type()
)
stats15CardIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    stats15CardIndex.setStatus("current")
_Stats15PortIndex_Type = EponPortIndex
_Stats15PortIndex_Object = MibTableColumn
stats15PortIndex = _Stats15PortIndex_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 10, 2, 1, 3),
    _Stats15PortIndex_Type()
)
stats15PortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    stats15PortIndex.setStatus("current")
_Stats15Index_Type = EponStats15MinRecordType
_Stats15Index_Object = MibTableColumn
stats15Index = _Stats15Index_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 10, 2, 1, 4),
    _Stats15Index_Type()
)
stats15Index.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    stats15Index.setStatus("current")
_Stats15InOctets_Type = Counter64
_Stats15InOctets_Object = MibTableColumn
stats15InOctets = _Stats15InOctets_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 10, 2, 1, 5),
    _Stats15InOctets_Type()
)
stats15InOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stats15InOctets.setStatus("current")
_Stats15InPkts_Type = Counter64
_Stats15InPkts_Object = MibTableColumn
stats15InPkts = _Stats15InPkts_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 10, 2, 1, 6),
    _Stats15InPkts_Type()
)
stats15InPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stats15InPkts.setStatus("current")
_Stats15InBroadcastPkts_Type = Counter64
_Stats15InBroadcastPkts_Object = MibTableColumn
stats15InBroadcastPkts = _Stats15InBroadcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 10, 2, 1, 7),
    _Stats15InBroadcastPkts_Type()
)
stats15InBroadcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stats15InBroadcastPkts.setStatus("current")
_Stats15InMulticastPkts_Type = Counter64
_Stats15InMulticastPkts_Object = MibTableColumn
stats15InMulticastPkts = _Stats15InMulticastPkts_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 10, 2, 1, 8),
    _Stats15InMulticastPkts_Type()
)
stats15InMulticastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stats15InMulticastPkts.setStatus("current")
_Stats15InPkts64Octets_Type = Counter64
_Stats15InPkts64Octets_Object = MibTableColumn
stats15InPkts64Octets = _Stats15InPkts64Octets_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 10, 2, 1, 9),
    _Stats15InPkts64Octets_Type()
)
stats15InPkts64Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stats15InPkts64Octets.setStatus("current")
_Stats15InPkts65to127Octets_Type = Counter64
_Stats15InPkts65to127Octets_Object = MibTableColumn
stats15InPkts65to127Octets = _Stats15InPkts65to127Octets_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 10, 2, 1, 10),
    _Stats15InPkts65to127Octets_Type()
)
stats15InPkts65to127Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stats15InPkts65to127Octets.setStatus("current")
_Stats15InPkts128to255Octets_Type = Counter64
_Stats15InPkts128to255Octets_Object = MibTableColumn
stats15InPkts128to255Octets = _Stats15InPkts128to255Octets_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 10, 2, 1, 11),
    _Stats15InPkts128to255Octets_Type()
)
stats15InPkts128to255Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stats15InPkts128to255Octets.setStatus("current")
_Stats15InPkts256to511Octets_Type = Counter64
_Stats15InPkts256to511Octets_Object = MibTableColumn
stats15InPkts256to511Octets = _Stats15InPkts256to511Octets_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 10, 2, 1, 12),
    _Stats15InPkts256to511Octets_Type()
)
stats15InPkts256to511Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stats15InPkts256to511Octets.setStatus("current")
_Stats15InPkts512to1023Octets_Type = Counter64
_Stats15InPkts512to1023Octets_Object = MibTableColumn
stats15InPkts512to1023Octets = _Stats15InPkts512to1023Octets_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 10, 2, 1, 13),
    _Stats15InPkts512to1023Octets_Type()
)
stats15InPkts512to1023Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stats15InPkts512to1023Octets.setStatus("current")
_Stats15InPkts1024to1518Octets_Type = Counter64
_Stats15InPkts1024to1518Octets_Object = MibTableColumn
stats15InPkts1024to1518Octets = _Stats15InPkts1024to1518Octets_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 10, 2, 1, 14),
    _Stats15InPkts1024to1518Octets_Type()
)
stats15InPkts1024to1518Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stats15InPkts1024to1518Octets.setStatus("current")
_Stats15InPkts1519to1522Octets_Type = Counter64
_Stats15InPkts1519to1522Octets_Object = MibTableColumn
stats15InPkts1519to1522Octets = _Stats15InPkts1519to1522Octets_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 10, 2, 1, 15),
    _Stats15InPkts1519to1522Octets_Type()
)
stats15InPkts1519to1522Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stats15InPkts1519to1522Octets.setStatus("current")
_Stats15InUndersizePkts_Type = Counter64
_Stats15InUndersizePkts_Object = MibTableColumn
stats15InUndersizePkts = _Stats15InUndersizePkts_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 10, 2, 1, 16),
    _Stats15InUndersizePkts_Type()
)
stats15InUndersizePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stats15InUndersizePkts.setStatus("current")
_Stats15InOversizePkts_Type = Counter64
_Stats15InOversizePkts_Object = MibTableColumn
stats15InOversizePkts = _Stats15InOversizePkts_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 10, 2, 1, 17),
    _Stats15InOversizePkts_Type()
)
stats15InOversizePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stats15InOversizePkts.setStatus("current")
_Stats15InFragments_Type = Counter64
_Stats15InFragments_Object = MibTableColumn
stats15InFragments = _Stats15InFragments_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 10, 2, 1, 18),
    _Stats15InFragments_Type()
)
stats15InFragments.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stats15InFragments.setStatus("current")
_Stats15InMpcpFrames_Type = Counter64
_Stats15InMpcpFrames_Object = MibTableColumn
stats15InMpcpFrames = _Stats15InMpcpFrames_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 10, 2, 1, 19),
    _Stats15InMpcpFrames_Type()
)
stats15InMpcpFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stats15InMpcpFrames.setStatus("current")
_Stats15InMpcpOctets_Type = Counter64
_Stats15InMpcpOctets_Object = MibTableColumn
stats15InMpcpOctets = _Stats15InMpcpOctets_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 10, 2, 1, 20),
    _Stats15InMpcpOctets_Type()
)
stats15InMpcpOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stats15InMpcpOctets.setStatus("current")
_Stats15InOAMFrames_Type = Counter64
_Stats15InOAMFrames_Object = MibTableColumn
stats15InOAMFrames = _Stats15InOAMFrames_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 10, 2, 1, 21),
    _Stats15InOAMFrames_Type()
)
stats15InOAMFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stats15InOAMFrames.setStatus("current")
_Stats15InOAMOctets_Type = Counter64
_Stats15InOAMOctets_Object = MibTableColumn
stats15InOAMOctets = _Stats15InOAMOctets_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 10, 2, 1, 22),
    _Stats15InOAMOctets_Type()
)
stats15InOAMOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stats15InOAMOctets.setStatus("current")
_Stats15InCRCErrorPkts_Type = Counter64
_Stats15InCRCErrorPkts_Object = MibTableColumn
stats15InCRCErrorPkts = _Stats15InCRCErrorPkts_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 10, 2, 1, 23),
    _Stats15InCRCErrorPkts_Type()
)
stats15InCRCErrorPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stats15InCRCErrorPkts.setStatus("current")
_Stats15InDropEvents_Type = Counter64
_Stats15InDropEvents_Object = MibTableColumn
stats15InDropEvents = _Stats15InDropEvents_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 10, 2, 1, 24),
    _Stats15InDropEvents_Type()
)
stats15InDropEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stats15InDropEvents.setStatus("current")
_Stats15InJabbers_Type = Counter64
_Stats15InJabbers_Object = MibTableColumn
stats15InJabbers = _Stats15InJabbers_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 10, 2, 1, 25),
    _Stats15InJabbers_Type()
)
stats15InJabbers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stats15InJabbers.setStatus("current")
_Stats15InCollision_Type = Counter64
_Stats15InCollision_Object = MibTableColumn
stats15InCollision = _Stats15InCollision_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 10, 2, 1, 26),
    _Stats15InCollision_Type()
)
stats15InCollision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stats15InCollision.setStatus("current")
_Stats15OutOctets_Type = Counter64
_Stats15OutOctets_Object = MibTableColumn
stats15OutOctets = _Stats15OutOctets_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 10, 2, 1, 27),
    _Stats15OutOctets_Type()
)
stats15OutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stats15OutOctets.setStatus("current")
_Stats15OutPkts_Type = Counter64
_Stats15OutPkts_Object = MibTableColumn
stats15OutPkts = _Stats15OutPkts_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 10, 2, 1, 28),
    _Stats15OutPkts_Type()
)
stats15OutPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stats15OutPkts.setStatus("current")
_Stats15OutBroadcastPkts_Type = Counter64
_Stats15OutBroadcastPkts_Object = MibTableColumn
stats15OutBroadcastPkts = _Stats15OutBroadcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 10, 2, 1, 29),
    _Stats15OutBroadcastPkts_Type()
)
stats15OutBroadcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stats15OutBroadcastPkts.setStatus("current")
_Stats15OutMulticastPkts_Type = Counter64
_Stats15OutMulticastPkts_Object = MibTableColumn
stats15OutMulticastPkts = _Stats15OutMulticastPkts_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 10, 2, 1, 30),
    _Stats15OutMulticastPkts_Type()
)
stats15OutMulticastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stats15OutMulticastPkts.setStatus("current")
_Stats15OutPkts64Octets_Type = Counter64
_Stats15OutPkts64Octets_Object = MibTableColumn
stats15OutPkts64Octets = _Stats15OutPkts64Octets_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 10, 2, 1, 31),
    _Stats15OutPkts64Octets_Type()
)
stats15OutPkts64Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stats15OutPkts64Octets.setStatus("current")
_Stats15OutPkts65to127Octets_Type = Counter64
_Stats15OutPkts65to127Octets_Object = MibTableColumn
stats15OutPkts65to127Octets = _Stats15OutPkts65to127Octets_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 10, 2, 1, 32),
    _Stats15OutPkts65to127Octets_Type()
)
stats15OutPkts65to127Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stats15OutPkts65to127Octets.setStatus("current")
_Stats15OutPkts128to255Octets_Type = Counter64
_Stats15OutPkts128to255Octets_Object = MibTableColumn
stats15OutPkts128to255Octets = _Stats15OutPkts128to255Octets_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 10, 2, 1, 33),
    _Stats15OutPkts128to255Octets_Type()
)
stats15OutPkts128to255Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stats15OutPkts128to255Octets.setStatus("current")
_Stats15OutPkts256to511Octets_Type = Counter64
_Stats15OutPkts256to511Octets_Object = MibTableColumn
stats15OutPkts256to511Octets = _Stats15OutPkts256to511Octets_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 10, 2, 1, 34),
    _Stats15OutPkts256to511Octets_Type()
)
stats15OutPkts256to511Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stats15OutPkts256to511Octets.setStatus("current")
_Stats15OutPkts512to1023Octets_Type = Counter64
_Stats15OutPkts512to1023Octets_Object = MibTableColumn
stats15OutPkts512to1023Octets = _Stats15OutPkts512to1023Octets_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 10, 2, 1, 35),
    _Stats15OutPkts512to1023Octets_Type()
)
stats15OutPkts512to1023Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stats15OutPkts512to1023Octets.setStatus("current")
_Stats15OutPkts1024to1518Octets_Type = Counter64
_Stats15OutPkts1024to1518Octets_Object = MibTableColumn
stats15OutPkts1024to1518Octets = _Stats15OutPkts1024to1518Octets_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 10, 2, 1, 36),
    _Stats15OutPkts1024to1518Octets_Type()
)
stats15OutPkts1024to1518Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stats15OutPkts1024to1518Octets.setStatus("current")
_Stats15OutPkts1519o1522Octets_Type = Counter64
_Stats15OutPkts1519o1522Octets_Object = MibTableColumn
stats15OutPkts1519o1522Octets = _Stats15OutPkts1519o1522Octets_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 10, 2, 1, 37),
    _Stats15OutPkts1519o1522Octets_Type()
)
stats15OutPkts1519o1522Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stats15OutPkts1519o1522Octets.setStatus("current")
_Stats15OutUndersizePkts_Type = Counter64
_Stats15OutUndersizePkts_Object = MibTableColumn
stats15OutUndersizePkts = _Stats15OutUndersizePkts_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 10, 2, 1, 38),
    _Stats15OutUndersizePkts_Type()
)
stats15OutUndersizePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stats15OutUndersizePkts.setStatus("current")
_Stats15OutOversizePkts_Type = Counter64
_Stats15OutOversizePkts_Object = MibTableColumn
stats15OutOversizePkts = _Stats15OutOversizePkts_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 10, 2, 1, 39),
    _Stats15OutOversizePkts_Type()
)
stats15OutOversizePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stats15OutOversizePkts.setStatus("current")
_Stats15OutFragments_Type = Counter64
_Stats15OutFragments_Object = MibTableColumn
stats15OutFragments = _Stats15OutFragments_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 10, 2, 1, 40),
    _Stats15OutFragments_Type()
)
stats15OutFragments.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stats15OutFragments.setStatus("current")
_Stats15OutMpcpFrames_Type = Counter64
_Stats15OutMpcpFrames_Object = MibTableColumn
stats15OutMpcpFrames = _Stats15OutMpcpFrames_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 10, 2, 1, 41),
    _Stats15OutMpcpFrames_Type()
)
stats15OutMpcpFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stats15OutMpcpFrames.setStatus("current")
_Stats15OutMpcpOctets_Type = Counter64
_Stats15OutMpcpOctets_Object = MibTableColumn
stats15OutMpcpOctets = _Stats15OutMpcpOctets_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 10, 2, 1, 42),
    _Stats15OutMpcpOctets_Type()
)
stats15OutMpcpOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stats15OutMpcpOctets.setStatus("current")
_Stats15OutOAMFrames_Type = Counter64
_Stats15OutOAMFrames_Object = MibTableColumn
stats15OutOAMFrames = _Stats15OutOAMFrames_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 10, 2, 1, 43),
    _Stats15OutOAMFrames_Type()
)
stats15OutOAMFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stats15OutOAMFrames.setStatus("current")
_Stats15OutOAMOctets_Type = Counter64
_Stats15OutOAMOctets_Object = MibTableColumn
stats15OutOAMOctets = _Stats15OutOAMOctets_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 10, 2, 1, 44),
    _Stats15OutOAMOctets_Type()
)
stats15OutOAMOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stats15OutOAMOctets.setStatus("current")
_Stats15OutCRCErrorPkts_Type = Counter64
_Stats15OutCRCErrorPkts_Object = MibTableColumn
stats15OutCRCErrorPkts = _Stats15OutCRCErrorPkts_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 10, 2, 1, 45),
    _Stats15OutCRCErrorPkts_Type()
)
stats15OutCRCErrorPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stats15OutCRCErrorPkts.setStatus("current")
_Stats15OutDropEvents_Type = Counter64
_Stats15OutDropEvents_Object = MibTableColumn
stats15OutDropEvents = _Stats15OutDropEvents_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 10, 2, 1, 46),
    _Stats15OutDropEvents_Type()
)
stats15OutDropEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stats15OutDropEvents.setStatus("current")
_Stats15OutJabbers_Type = Counter64
_Stats15OutJabbers_Object = MibTableColumn
stats15OutJabbers = _Stats15OutJabbers_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 10, 2, 1, 47),
    _Stats15OutJabbers_Type()
)
stats15OutJabbers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stats15OutJabbers.setStatus("current")
_Stats15OutCollision_Type = Counter64
_Stats15OutCollision_Object = MibTableColumn
stats15OutCollision = _Stats15OutCollision_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 10, 2, 1, 48),
    _Stats15OutCollision_Type()
)
stats15OutCollision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stats15OutCollision.setStatus("current")


class _Stats15StatusAndAction_Type(Integer32):
    """Custom type stats15StatusAndAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("clean", 2))
    )


_Stats15StatusAndAction_Type.__name__ = "Integer32"
_Stats15StatusAndAction_Object = MibTableColumn
stats15StatusAndAction = _Stats15StatusAndAction_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 10, 2, 1, 49),
    _Stats15StatusAndAction_Type()
)
stats15StatusAndAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    stats15StatusAndAction.setStatus("current")
_Stats15ValidityTag_Type = TruthValue
_Stats15ValidityTag_Object = MibTableColumn
stats15ValidityTag = _Stats15ValidityTag_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 10, 2, 1, 50),
    _Stats15ValidityTag_Type()
)
stats15ValidityTag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stats15ValidityTag.setStatus("current")
_Stats15ElapsedTime_Type = Counter32
_Stats15ElapsedTime_Object = MibTableColumn
stats15ElapsedTime = _Stats15ElapsedTime_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 10, 2, 1, 51),
    _Stats15ElapsedTime_Type()
)
stats15ElapsedTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stats15ElapsedTime.setStatus("current")
if mibBuilder.loadTexts:
    stats15ElapsedTime.setUnits("seconds")
_Stats15EndTime_Type = DateAndTime
_Stats15EndTime_Object = MibTableColumn
stats15EndTime = _Stats15EndTime_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 10, 2, 1, 52),
    _Stats15EndTime_Type()
)
stats15EndTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stats15EndTime.setStatus("current")
_Stats24Table_Object = MibTable
stats24Table = _Stats24Table_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 10, 3)
)
if mibBuilder.loadTexts:
    stats24Table.setStatus("current")
_Stats24Entry_Object = MibTableRow
stats24Entry = _Stats24Entry_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 10, 3, 1)
)
stats24Entry.setIndexNames(
    (0, "NSCRTV-EPON-PERFORMANCE-STAT-MIB", "stats24DeviceIndex"),
    (0, "NSCRTV-EPON-PERFORMANCE-STAT-MIB", "stats24CardIndex"),
    (0, "NSCRTV-EPON-PERFORMANCE-STAT-MIB", "stats24PortIndex"),
    (0, "NSCRTV-EPON-PERFORMANCE-STAT-MIB", "stats24Index"),
)
if mibBuilder.loadTexts:
    stats24Entry.setStatus("current")
_Stats24DeviceIndex_Type = EponDeviceIndex
_Stats24DeviceIndex_Object = MibTableColumn
stats24DeviceIndex = _Stats24DeviceIndex_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 10, 3, 1, 1),
    _Stats24DeviceIndex_Type()
)
stats24DeviceIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    stats24DeviceIndex.setStatus("current")
_Stats24CardIndex_Type = EponCardIndex
_Stats24CardIndex_Object = MibTableColumn
stats24CardIndex = _Stats24CardIndex_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 10, 3, 1, 2),
    _Stats24CardIndex_Type()
)
stats24CardIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    stats24CardIndex.setStatus("current")
_Stats24PortIndex_Type = EponPortIndex
_Stats24PortIndex_Object = MibTableColumn
stats24PortIndex = _Stats24PortIndex_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 10, 3, 1, 3),
    _Stats24PortIndex_Type()
)
stats24PortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    stats24PortIndex.setStatus("current")
_Stats24Index_Type = EponStats24HourRecordType
_Stats24Index_Object = MibTableColumn
stats24Index = _Stats24Index_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 10, 3, 1, 4),
    _Stats24Index_Type()
)
stats24Index.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    stats24Index.setStatus("current")
_Stats24InOctets_Type = Counter64
_Stats24InOctets_Object = MibTableColumn
stats24InOctets = _Stats24InOctets_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 10, 3, 1, 5),
    _Stats24InOctets_Type()
)
stats24InOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stats24InOctets.setStatus("current")
_Stats24InPkts_Type = Counter64
_Stats24InPkts_Object = MibTableColumn
stats24InPkts = _Stats24InPkts_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 10, 3, 1, 6),
    _Stats24InPkts_Type()
)
stats24InPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stats24InPkts.setStatus("current")
_Stats24InBroadcastPkts_Type = Counter64
_Stats24InBroadcastPkts_Object = MibTableColumn
stats24InBroadcastPkts = _Stats24InBroadcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 10, 3, 1, 7),
    _Stats24InBroadcastPkts_Type()
)
stats24InBroadcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stats24InBroadcastPkts.setStatus("current")
_Stats24InMulticastPkts_Type = Counter64
_Stats24InMulticastPkts_Object = MibTableColumn
stats24InMulticastPkts = _Stats24InMulticastPkts_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 10, 3, 1, 8),
    _Stats24InMulticastPkts_Type()
)
stats24InMulticastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stats24InMulticastPkts.setStatus("current")
_Stats24InPkts64Octets_Type = Counter64
_Stats24InPkts64Octets_Object = MibTableColumn
stats24InPkts64Octets = _Stats24InPkts64Octets_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 10, 3, 1, 9),
    _Stats24InPkts64Octets_Type()
)
stats24InPkts64Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stats24InPkts64Octets.setStatus("current")
_Stats24InPkts65to127Octets_Type = Counter64
_Stats24InPkts65to127Octets_Object = MibTableColumn
stats24InPkts65to127Octets = _Stats24InPkts65to127Octets_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 10, 3, 1, 10),
    _Stats24InPkts65to127Octets_Type()
)
stats24InPkts65to127Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stats24InPkts65to127Octets.setStatus("current")
_Stats24InPkts128to255Octets_Type = Counter64
_Stats24InPkts128to255Octets_Object = MibTableColumn
stats24InPkts128to255Octets = _Stats24InPkts128to255Octets_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 10, 3, 1, 11),
    _Stats24InPkts128to255Octets_Type()
)
stats24InPkts128to255Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stats24InPkts128to255Octets.setStatus("current")
_Stats24InPkts256to511Octets_Type = Counter64
_Stats24InPkts256to511Octets_Object = MibTableColumn
stats24InPkts256to511Octets = _Stats24InPkts256to511Octets_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 10, 3, 1, 12),
    _Stats24InPkts256to511Octets_Type()
)
stats24InPkts256to511Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stats24InPkts256to511Octets.setStatus("current")
_Stats24InPkts512to1023Octets_Type = Counter64
_Stats24InPkts512to1023Octets_Object = MibTableColumn
stats24InPkts512to1023Octets = _Stats24InPkts512to1023Octets_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 10, 3, 1, 13),
    _Stats24InPkts512to1023Octets_Type()
)
stats24InPkts512to1023Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stats24InPkts512to1023Octets.setStatus("current")
_Stats24InPkts1024to1518Octets_Type = Counter64
_Stats24InPkts1024to1518Octets_Object = MibTableColumn
stats24InPkts1024to1518Octets = _Stats24InPkts1024to1518Octets_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 10, 3, 1, 14),
    _Stats24InPkts1024to1518Octets_Type()
)
stats24InPkts1024to1518Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stats24InPkts1024to1518Octets.setStatus("current")
_Stats24InPkts1519to1522Octets_Type = Counter64
_Stats24InPkts1519to1522Octets_Object = MibTableColumn
stats24InPkts1519to1522Octets = _Stats24InPkts1519to1522Octets_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 10, 3, 1, 15),
    _Stats24InPkts1519to1522Octets_Type()
)
stats24InPkts1519to1522Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stats24InPkts1519to1522Octets.setStatus("current")
_Stats24InUndersizePkts_Type = Counter64
_Stats24InUndersizePkts_Object = MibTableColumn
stats24InUndersizePkts = _Stats24InUndersizePkts_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 10, 3, 1, 16),
    _Stats24InUndersizePkts_Type()
)
stats24InUndersizePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stats24InUndersizePkts.setStatus("current")
_Stats24InOversizePkts_Type = Counter64
_Stats24InOversizePkts_Object = MibTableColumn
stats24InOversizePkts = _Stats24InOversizePkts_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 10, 3, 1, 17),
    _Stats24InOversizePkts_Type()
)
stats24InOversizePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stats24InOversizePkts.setStatus("current")
_Stats24InFragments_Type = Counter64
_Stats24InFragments_Object = MibTableColumn
stats24InFragments = _Stats24InFragments_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 10, 3, 1, 18),
    _Stats24InFragments_Type()
)
stats24InFragments.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stats24InFragments.setStatus("current")
_Stats24InMpcpFrames_Type = Counter64
_Stats24InMpcpFrames_Object = MibTableColumn
stats24InMpcpFrames = _Stats24InMpcpFrames_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 10, 3, 1, 19),
    _Stats24InMpcpFrames_Type()
)
stats24InMpcpFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stats24InMpcpFrames.setStatus("current")
_Stats24InMpcpOctets_Type = Counter64
_Stats24InMpcpOctets_Object = MibTableColumn
stats24InMpcpOctets = _Stats24InMpcpOctets_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 10, 3, 1, 20),
    _Stats24InMpcpOctets_Type()
)
stats24InMpcpOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stats24InMpcpOctets.setStatus("current")
_Stats24InOAMFrames_Type = Counter64
_Stats24InOAMFrames_Object = MibTableColumn
stats24InOAMFrames = _Stats24InOAMFrames_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 10, 3, 1, 21),
    _Stats24InOAMFrames_Type()
)
stats24InOAMFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stats24InOAMFrames.setStatus("current")
_Stats24InOAMOctets_Type = Counter64
_Stats24InOAMOctets_Object = MibTableColumn
stats24InOAMOctets = _Stats24InOAMOctets_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 10, 3, 1, 22),
    _Stats24InOAMOctets_Type()
)
stats24InOAMOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stats24InOAMOctets.setStatus("current")
_Stats24InCRCErrorPkts_Type = Counter64
_Stats24InCRCErrorPkts_Object = MibTableColumn
stats24InCRCErrorPkts = _Stats24InCRCErrorPkts_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 10, 3, 1, 23),
    _Stats24InCRCErrorPkts_Type()
)
stats24InCRCErrorPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stats24InCRCErrorPkts.setStatus("current")
_Stats24InDropEvents_Type = Counter64
_Stats24InDropEvents_Object = MibTableColumn
stats24InDropEvents = _Stats24InDropEvents_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 10, 3, 1, 24),
    _Stats24InDropEvents_Type()
)
stats24InDropEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stats24InDropEvents.setStatus("current")
_Stats24InJabbers_Type = Counter64
_Stats24InJabbers_Object = MibTableColumn
stats24InJabbers = _Stats24InJabbers_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 10, 3, 1, 25),
    _Stats24InJabbers_Type()
)
stats24InJabbers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stats24InJabbers.setStatus("current")
_Stats24InCollision_Type = Counter64
_Stats24InCollision_Object = MibTableColumn
stats24InCollision = _Stats24InCollision_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 10, 3, 1, 26),
    _Stats24InCollision_Type()
)
stats24InCollision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stats24InCollision.setStatus("current")
_Stats24OutOctets_Type = Counter64
_Stats24OutOctets_Object = MibTableColumn
stats24OutOctets = _Stats24OutOctets_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 10, 3, 1, 27),
    _Stats24OutOctets_Type()
)
stats24OutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stats24OutOctets.setStatus("current")
_Stats24OutPkts_Type = Counter64
_Stats24OutPkts_Object = MibTableColumn
stats24OutPkts = _Stats24OutPkts_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 10, 3, 1, 28),
    _Stats24OutPkts_Type()
)
stats24OutPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stats24OutPkts.setStatus("current")
_Stats24OutBroadcastPkts_Type = Counter64
_Stats24OutBroadcastPkts_Object = MibTableColumn
stats24OutBroadcastPkts = _Stats24OutBroadcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 10, 3, 1, 29),
    _Stats24OutBroadcastPkts_Type()
)
stats24OutBroadcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stats24OutBroadcastPkts.setStatus("current")
_Stats24OutMulticastPkts_Type = Counter64
_Stats24OutMulticastPkts_Object = MibTableColumn
stats24OutMulticastPkts = _Stats24OutMulticastPkts_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 10, 3, 1, 30),
    _Stats24OutMulticastPkts_Type()
)
stats24OutMulticastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stats24OutMulticastPkts.setStatus("current")
_Stats24OutPkts64Octets_Type = Counter64
_Stats24OutPkts64Octets_Object = MibTableColumn
stats24OutPkts64Octets = _Stats24OutPkts64Octets_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 10, 3, 1, 31),
    _Stats24OutPkts64Octets_Type()
)
stats24OutPkts64Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stats24OutPkts64Octets.setStatus("current")
_Stats24OutPkts65to127Octets_Type = Counter64
_Stats24OutPkts65to127Octets_Object = MibTableColumn
stats24OutPkts65to127Octets = _Stats24OutPkts65to127Octets_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 10, 3, 1, 32),
    _Stats24OutPkts65to127Octets_Type()
)
stats24OutPkts65to127Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stats24OutPkts65to127Octets.setStatus("current")
_Stats24OutPkts128to255Octets_Type = Counter64
_Stats24OutPkts128to255Octets_Object = MibTableColumn
stats24OutPkts128to255Octets = _Stats24OutPkts128to255Octets_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 10, 3, 1, 33),
    _Stats24OutPkts128to255Octets_Type()
)
stats24OutPkts128to255Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stats24OutPkts128to255Octets.setStatus("current")
_Stats24OutPkts256to511Octets_Type = Counter64
_Stats24OutPkts256to511Octets_Object = MibTableColumn
stats24OutPkts256to511Octets = _Stats24OutPkts256to511Octets_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 10, 3, 1, 34),
    _Stats24OutPkts256to511Octets_Type()
)
stats24OutPkts256to511Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stats24OutPkts256to511Octets.setStatus("current")
_Stats24OutPkts512to1023Octets_Type = Counter64
_Stats24OutPkts512to1023Octets_Object = MibTableColumn
stats24OutPkts512to1023Octets = _Stats24OutPkts512to1023Octets_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 10, 3, 1, 35),
    _Stats24OutPkts512to1023Octets_Type()
)
stats24OutPkts512to1023Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stats24OutPkts512to1023Octets.setStatus("current")
_Stats24OutPkts1024to1518Octets_Type = Counter64
_Stats24OutPkts1024to1518Octets_Object = MibTableColumn
stats24OutPkts1024to1518Octets = _Stats24OutPkts1024to1518Octets_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 10, 3, 1, 36),
    _Stats24OutPkts1024to1518Octets_Type()
)
stats24OutPkts1024to1518Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stats24OutPkts1024to1518Octets.setStatus("current")
_Stats24OutPkts1519o1522Octets_Type = Counter64
_Stats24OutPkts1519o1522Octets_Object = MibTableColumn
stats24OutPkts1519o1522Octets = _Stats24OutPkts1519o1522Octets_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 10, 3, 1, 37),
    _Stats24OutPkts1519o1522Octets_Type()
)
stats24OutPkts1519o1522Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stats24OutPkts1519o1522Octets.setStatus("current")
_Stats24OutUndersizePkts_Type = Counter64
_Stats24OutUndersizePkts_Object = MibTableColumn
stats24OutUndersizePkts = _Stats24OutUndersizePkts_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 10, 3, 1, 38),
    _Stats24OutUndersizePkts_Type()
)
stats24OutUndersizePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stats24OutUndersizePkts.setStatus("current")
_Stats24OutOversizePkts_Type = Counter64
_Stats24OutOversizePkts_Object = MibTableColumn
stats24OutOversizePkts = _Stats24OutOversizePkts_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 10, 3, 1, 39),
    _Stats24OutOversizePkts_Type()
)
stats24OutOversizePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stats24OutOversizePkts.setStatus("current")
_Stats24OutFragments_Type = Counter64
_Stats24OutFragments_Object = MibTableColumn
stats24OutFragments = _Stats24OutFragments_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 10, 3, 1, 40),
    _Stats24OutFragments_Type()
)
stats24OutFragments.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stats24OutFragments.setStatus("current")
_Stats24OutMpcpFrames_Type = Counter64
_Stats24OutMpcpFrames_Object = MibTableColumn
stats24OutMpcpFrames = _Stats24OutMpcpFrames_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 10, 3, 1, 41),
    _Stats24OutMpcpFrames_Type()
)
stats24OutMpcpFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stats24OutMpcpFrames.setStatus("current")
_Stats24OutMpcpOctets_Type = Counter64
_Stats24OutMpcpOctets_Object = MibTableColumn
stats24OutMpcpOctets = _Stats24OutMpcpOctets_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 10, 3, 1, 42),
    _Stats24OutMpcpOctets_Type()
)
stats24OutMpcpOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stats24OutMpcpOctets.setStatus("current")
_Stats24OutOAMFrames_Type = Counter64
_Stats24OutOAMFrames_Object = MibTableColumn
stats24OutOAMFrames = _Stats24OutOAMFrames_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 10, 3, 1, 43),
    _Stats24OutOAMFrames_Type()
)
stats24OutOAMFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stats24OutOAMFrames.setStatus("current")
_Stats24OutOAMOctets_Type = Counter64
_Stats24OutOAMOctets_Object = MibTableColumn
stats24OutOAMOctets = _Stats24OutOAMOctets_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 10, 3, 1, 44),
    _Stats24OutOAMOctets_Type()
)
stats24OutOAMOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stats24OutOAMOctets.setStatus("current")
_Stats24OutCRCErrorPkts_Type = Counter64
_Stats24OutCRCErrorPkts_Object = MibTableColumn
stats24OutCRCErrorPkts = _Stats24OutCRCErrorPkts_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 10, 3, 1, 45),
    _Stats24OutCRCErrorPkts_Type()
)
stats24OutCRCErrorPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stats24OutCRCErrorPkts.setStatus("current")
_Stats24OutDropEvents_Type = Counter64
_Stats24OutDropEvents_Object = MibTableColumn
stats24OutDropEvents = _Stats24OutDropEvents_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 10, 3, 1, 46),
    _Stats24OutDropEvents_Type()
)
stats24OutDropEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stats24OutDropEvents.setStatus("current")
_Stats24OutJabbers_Type = Counter64
_Stats24OutJabbers_Object = MibTableColumn
stats24OutJabbers = _Stats24OutJabbers_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 10, 3, 1, 47),
    _Stats24OutJabbers_Type()
)
stats24OutJabbers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stats24OutJabbers.setStatus("current")
_Stats24OutCollision_Type = Counter64
_Stats24OutCollision_Object = MibTableColumn
stats24OutCollision = _Stats24OutCollision_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 10, 3, 1, 48),
    _Stats24OutCollision_Type()
)
stats24OutCollision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stats24OutCollision.setStatus("current")


class _Stats24StatusAndAction_Type(Integer32):
    """Custom type stats24StatusAndAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("clear", 2))
    )


_Stats24StatusAndAction_Type.__name__ = "Integer32"
_Stats24StatusAndAction_Object = MibTableColumn
stats24StatusAndAction = _Stats24StatusAndAction_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 10, 3, 1, 49),
    _Stats24StatusAndAction_Type()
)
stats24StatusAndAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    stats24StatusAndAction.setStatus("current")
_Stats24ValidityTag_Type = TruthValue
_Stats24ValidityTag_Object = MibTableColumn
stats24ValidityTag = _Stats24ValidityTag_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 10, 3, 1, 50),
    _Stats24ValidityTag_Type()
)
stats24ValidityTag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stats24ValidityTag.setStatus("current")
_Stats24ElapsedTime_Type = Counter32
_Stats24ElapsedTime_Object = MibTableColumn
stats24ElapsedTime = _Stats24ElapsedTime_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 10, 3, 1, 51),
    _Stats24ElapsedTime_Type()
)
stats24ElapsedTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stats24ElapsedTime.setStatus("current")
if mibBuilder.loadTexts:
    stats24ElapsedTime.setUnits("seconds")
_Stats24EndTime_Type = DateAndTime
_Stats24EndTime_Object = MibTableColumn
stats24EndTime = _Stats24EndTime_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 10, 3, 1, 52),
    _Stats24EndTime_Type()
)
stats24EndTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stats24EndTime.setStatus("current")
_PerfStatsGlobalSet_ObjectIdentity = ObjectIdentity
perfStatsGlobalSet = _PerfStatsGlobalSet_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 10, 4)
)
if mibBuilder.loadTexts:
    perfStatsGlobalSet.setStatus("current")


class _PerfStats15MinMaxRecord_Type(EponStats15MinRecordType):
    """Custom type perfStats15MinMaxRecord based on EponStats15MinRecordType"""
    defaultValue = 96


_PerfStats15MinMaxRecord_Type.__name__ = "EponStats15MinRecordType"
_PerfStats15MinMaxRecord_Object = MibScalar
perfStats15MinMaxRecord = _PerfStats15MinMaxRecord_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 10, 4, 1),
    _PerfStats15MinMaxRecord_Type()
)
perfStats15MinMaxRecord.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    perfStats15MinMaxRecord.setStatus("current")


class _PerfStats24HourMaxRecord_Type(EponStats24HourRecordType):
    """Custom type perfStats24HourMaxRecord based on EponStats24HourRecordType"""
    defaultValue = 7


_PerfStats24HourMaxRecord_Type.__name__ = "EponStats24HourRecordType"
_PerfStats24HourMaxRecord_Object = MibScalar
perfStats24HourMaxRecord = _PerfStats24HourMaxRecord_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 10, 4, 2),
    _PerfStats24HourMaxRecord_Type()
)
perfStats24HourMaxRecord.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    perfStats24HourMaxRecord.setStatus("current")
_PerfStatsThresholdTable_Object = MibTable
perfStatsThresholdTable = _PerfStatsThresholdTable_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 10, 5)
)
if mibBuilder.loadTexts:
    perfStatsThresholdTable.setStatus("current")
_PerfStatsThresholdEntry_Object = MibTableRow
perfStatsThresholdEntry = _PerfStatsThresholdEntry_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 10, 5, 1)
)
perfStatsThresholdEntry.setIndexNames(
    (0, "NSCRTV-EPON-PERFORMANCE-STAT-MIB", "perfStatsThresholdDeviceIndex"),
    (0, "NSCRTV-EPON-PERFORMANCE-STAT-MIB", "perfStatsThresholdCardIndex"),
    (0, "NSCRTV-EPON-PERFORMANCE-STAT-MIB", "perfStatsThresholdPortIndex"),
    (0, "NSCRTV-EPON-PERFORMANCE-STAT-MIB", "perfStatsThresholdTypeIndex"),
)
if mibBuilder.loadTexts:
    perfStatsThresholdEntry.setStatus("current")
_PerfStatsThresholdDeviceIndex_Type = EponDeviceIndex
_PerfStatsThresholdDeviceIndex_Object = MibTableColumn
perfStatsThresholdDeviceIndex = _PerfStatsThresholdDeviceIndex_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 10, 5, 1, 1),
    _PerfStatsThresholdDeviceIndex_Type()
)
perfStatsThresholdDeviceIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    perfStatsThresholdDeviceIndex.setStatus("current")
_PerfStatsThresholdCardIndex_Type = EponCardIndex
_PerfStatsThresholdCardIndex_Object = MibTableColumn
perfStatsThresholdCardIndex = _PerfStatsThresholdCardIndex_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 10, 5, 1, 2),
    _PerfStatsThresholdCardIndex_Type()
)
perfStatsThresholdCardIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    perfStatsThresholdCardIndex.setStatus("current")
_PerfStatsThresholdPortIndex_Type = EponPortIndex
_PerfStatsThresholdPortIndex_Object = MibTableColumn
perfStatsThresholdPortIndex = _PerfStatsThresholdPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 10, 5, 1, 3),
    _PerfStatsThresholdPortIndex_Type()
)
perfStatsThresholdPortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    perfStatsThresholdPortIndex.setStatus("current")
_PerfStatsThresholdTypeIndex_Type = EponStatsThresholdType
_PerfStatsThresholdTypeIndex_Object = MibTableColumn
perfStatsThresholdTypeIndex = _PerfStatsThresholdTypeIndex_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 10, 5, 1, 4),
    _PerfStatsThresholdTypeIndex_Type()
)
perfStatsThresholdTypeIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    perfStatsThresholdTypeIndex.setStatus("current")
_PerfStatsThresholdUpper_Type = Counter64
_PerfStatsThresholdUpper_Object = MibTableColumn
perfStatsThresholdUpper = _PerfStatsThresholdUpper_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 10, 5, 1, 5),
    _PerfStatsThresholdUpper_Type()
)
perfStatsThresholdUpper.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    perfStatsThresholdUpper.setStatus("current")
_PerfStatsThresholdLower_Type = Counter64
_PerfStatsThresholdLower_Object = MibTableColumn
perfStatsThresholdLower = _PerfStatsThresholdLower_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 10, 5, 1, 6),
    _PerfStatsThresholdLower_Type()
)
perfStatsThresholdLower.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    perfStatsThresholdLower.setStatus("current")
_PerfStatsThresholdRowStatus_Type = RowStatus
_PerfStatsThresholdRowStatus_Object = MibTableColumn
perfStatsThresholdRowStatus = _PerfStatsThresholdRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 10, 5, 1, 7),
    _PerfStatsThresholdRowStatus_Type()
)
perfStatsThresholdRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    perfStatsThresholdRowStatus.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "NSCRTV-EPON-PERFORMANCE-STAT-MIB",
    **{"curStatsTable": curStatsTable,
       "curStatsEntry": curStatsEntry,
       "curStatsDeviceIndex": curStatsDeviceIndex,
       "curStatsCardIndex": curStatsCardIndex,
       "curStatsPortIndex": curStatsPortIndex,
       "curStatsInOctets": curStatsInOctets,
       "curStatsInPkts": curStatsInPkts,
       "curStatsInBroadcastPkts": curStatsInBroadcastPkts,
       "curStatsInMulticastPkts": curStatsInMulticastPkts,
       "curStatsInPkts64Octets": curStatsInPkts64Octets,
       "curStatsInPkts65to127Octets": curStatsInPkts65to127Octets,
       "curStatsInPkts128to255Octets": curStatsInPkts128to255Octets,
       "curStatsInPkts256to511Octets": curStatsInPkts256to511Octets,
       "curStatsInPkts512to1023Octets": curStatsInPkts512to1023Octets,
       "curStatsInPkts1024to1518Octets": curStatsInPkts1024to1518Octets,
       "curStatsInPkts1519to1522Octets": curStatsInPkts1519to1522Octets,
       "curStatsInUndersizePkts": curStatsInUndersizePkts,
       "curStatsInOversizePkts": curStatsInOversizePkts,
       "curStatsInFragments": curStatsInFragments,
       "curStatsInMpcpFrames": curStatsInMpcpFrames,
       "curStatsInMpcpOctets": curStatsInMpcpOctets,
       "curStatsInOAMFrames": curStatsInOAMFrames,
       "curStatsInOAMOctets": curStatsInOAMOctets,
       "curStatsInCRCErrorPkts": curStatsInCRCErrorPkts,
       "curStatsInDropEvents": curStatsInDropEvents,
       "curStatsInJabbers": curStatsInJabbers,
       "curStatsInCollision": curStatsInCollision,
       "curStatsOutOctets": curStatsOutOctets,
       "curStatsOutPkts": curStatsOutPkts,
       "curStatsOutBroadcastPkts": curStatsOutBroadcastPkts,
       "curStatsOutMulticastPkts": curStatsOutMulticastPkts,
       "curStatsOutPkts64Octets": curStatsOutPkts64Octets,
       "curStatsOutPkts65to127Octets": curStatsOutPkts65to127Octets,
       "curStatsOutPkts128to255Octets": curStatsOutPkts128to255Octets,
       "curStatsOutPkts256to511Octets": curStatsOutPkts256to511Octets,
       "curStatsOutPkts512to1023Octets": curStatsOutPkts512to1023Octets,
       "curStatsOutPkts1024to1518Octets": curStatsOutPkts1024to1518Octets,
       "curStatsOutPkts1519o1522Octets": curStatsOutPkts1519o1522Octets,
       "curStatsOutUndersizePkts": curStatsOutUndersizePkts,
       "curStatsOutOversizePkts": curStatsOutOversizePkts,
       "curStatsOutFragments": curStatsOutFragments,
       "curStatsOutMpcpFrames": curStatsOutMpcpFrames,
       "curStatsOutMpcpOctets": curStatsOutMpcpOctets,
       "curStatsOutOAMFrames": curStatsOutOAMFrames,
       "curStatsOutOAMOctets": curStatsOutOAMOctets,
       "curStatsOutCRCErrorPkts": curStatsOutCRCErrorPkts,
       "curStatsOutDropEvents": curStatsOutDropEvents,
       "curStatsOutJabbers": curStatsOutJabbers,
       "curStatsOutCollision": curStatsOutCollision,
       "curStatsStatusAndAction": curStatsStatusAndAction,
       "stats15Table": stats15Table,
       "stats15Entry": stats15Entry,
       "stats15DeviceIndex": stats15DeviceIndex,
       "stats15CardIndex": stats15CardIndex,
       "stats15PortIndex": stats15PortIndex,
       "stats15Index": stats15Index,
       "stats15InOctets": stats15InOctets,
       "stats15InPkts": stats15InPkts,
       "stats15InBroadcastPkts": stats15InBroadcastPkts,
       "stats15InMulticastPkts": stats15InMulticastPkts,
       "stats15InPkts64Octets": stats15InPkts64Octets,
       "stats15InPkts65to127Octets": stats15InPkts65to127Octets,
       "stats15InPkts128to255Octets": stats15InPkts128to255Octets,
       "stats15InPkts256to511Octets": stats15InPkts256to511Octets,
       "stats15InPkts512to1023Octets": stats15InPkts512to1023Octets,
       "stats15InPkts1024to1518Octets": stats15InPkts1024to1518Octets,
       "stats15InPkts1519to1522Octets": stats15InPkts1519to1522Octets,
       "stats15InUndersizePkts": stats15InUndersizePkts,
       "stats15InOversizePkts": stats15InOversizePkts,
       "stats15InFragments": stats15InFragments,
       "stats15InMpcpFrames": stats15InMpcpFrames,
       "stats15InMpcpOctets": stats15InMpcpOctets,
       "stats15InOAMFrames": stats15InOAMFrames,
       "stats15InOAMOctets": stats15InOAMOctets,
       "stats15InCRCErrorPkts": stats15InCRCErrorPkts,
       "stats15InDropEvents": stats15InDropEvents,
       "stats15InJabbers": stats15InJabbers,
       "stats15InCollision": stats15InCollision,
       "stats15OutOctets": stats15OutOctets,
       "stats15OutPkts": stats15OutPkts,
       "stats15OutBroadcastPkts": stats15OutBroadcastPkts,
       "stats15OutMulticastPkts": stats15OutMulticastPkts,
       "stats15OutPkts64Octets": stats15OutPkts64Octets,
       "stats15OutPkts65to127Octets": stats15OutPkts65to127Octets,
       "stats15OutPkts128to255Octets": stats15OutPkts128to255Octets,
       "stats15OutPkts256to511Octets": stats15OutPkts256to511Octets,
       "stats15OutPkts512to1023Octets": stats15OutPkts512to1023Octets,
       "stats15OutPkts1024to1518Octets": stats15OutPkts1024to1518Octets,
       "stats15OutPkts1519o1522Octets": stats15OutPkts1519o1522Octets,
       "stats15OutUndersizePkts": stats15OutUndersizePkts,
       "stats15OutOversizePkts": stats15OutOversizePkts,
       "stats15OutFragments": stats15OutFragments,
       "stats15OutMpcpFrames": stats15OutMpcpFrames,
       "stats15OutMpcpOctets": stats15OutMpcpOctets,
       "stats15OutOAMFrames": stats15OutOAMFrames,
       "stats15OutOAMOctets": stats15OutOAMOctets,
       "stats15OutCRCErrorPkts": stats15OutCRCErrorPkts,
       "stats15OutDropEvents": stats15OutDropEvents,
       "stats15OutJabbers": stats15OutJabbers,
       "stats15OutCollision": stats15OutCollision,
       "stats15StatusAndAction": stats15StatusAndAction,
       "stats15ValidityTag": stats15ValidityTag,
       "stats15ElapsedTime": stats15ElapsedTime,
       "stats15EndTime": stats15EndTime,
       "stats24Table": stats24Table,
       "stats24Entry": stats24Entry,
       "stats24DeviceIndex": stats24DeviceIndex,
       "stats24CardIndex": stats24CardIndex,
       "stats24PortIndex": stats24PortIndex,
       "stats24Index": stats24Index,
       "stats24InOctets": stats24InOctets,
       "stats24InPkts": stats24InPkts,
       "stats24InBroadcastPkts": stats24InBroadcastPkts,
       "stats24InMulticastPkts": stats24InMulticastPkts,
       "stats24InPkts64Octets": stats24InPkts64Octets,
       "stats24InPkts65to127Octets": stats24InPkts65to127Octets,
       "stats24InPkts128to255Octets": stats24InPkts128to255Octets,
       "stats24InPkts256to511Octets": stats24InPkts256to511Octets,
       "stats24InPkts512to1023Octets": stats24InPkts512to1023Octets,
       "stats24InPkts1024to1518Octets": stats24InPkts1024to1518Octets,
       "stats24InPkts1519to1522Octets": stats24InPkts1519to1522Octets,
       "stats24InUndersizePkts": stats24InUndersizePkts,
       "stats24InOversizePkts": stats24InOversizePkts,
       "stats24InFragments": stats24InFragments,
       "stats24InMpcpFrames": stats24InMpcpFrames,
       "stats24InMpcpOctets": stats24InMpcpOctets,
       "stats24InOAMFrames": stats24InOAMFrames,
       "stats24InOAMOctets": stats24InOAMOctets,
       "stats24InCRCErrorPkts": stats24InCRCErrorPkts,
       "stats24InDropEvents": stats24InDropEvents,
       "stats24InJabbers": stats24InJabbers,
       "stats24InCollision": stats24InCollision,
       "stats24OutOctets": stats24OutOctets,
       "stats24OutPkts": stats24OutPkts,
       "stats24OutBroadcastPkts": stats24OutBroadcastPkts,
       "stats24OutMulticastPkts": stats24OutMulticastPkts,
       "stats24OutPkts64Octets": stats24OutPkts64Octets,
       "stats24OutPkts65to127Octets": stats24OutPkts65to127Octets,
       "stats24OutPkts128to255Octets": stats24OutPkts128to255Octets,
       "stats24OutPkts256to511Octets": stats24OutPkts256to511Octets,
       "stats24OutPkts512to1023Octets": stats24OutPkts512to1023Octets,
       "stats24OutPkts1024to1518Octets": stats24OutPkts1024to1518Octets,
       "stats24OutPkts1519o1522Octets": stats24OutPkts1519o1522Octets,
       "stats24OutUndersizePkts": stats24OutUndersizePkts,
       "stats24OutOversizePkts": stats24OutOversizePkts,
       "stats24OutFragments": stats24OutFragments,
       "stats24OutMpcpFrames": stats24OutMpcpFrames,
       "stats24OutMpcpOctets": stats24OutMpcpOctets,
       "stats24OutOAMFrames": stats24OutOAMFrames,
       "stats24OutOAMOctets": stats24OutOAMOctets,
       "stats24OutCRCErrorPkts": stats24OutCRCErrorPkts,
       "stats24OutDropEvents": stats24OutDropEvents,
       "stats24OutJabbers": stats24OutJabbers,
       "stats24OutCollision": stats24OutCollision,
       "stats24StatusAndAction": stats24StatusAndAction,
       "stats24ValidityTag": stats24ValidityTag,
       "stats24ElapsedTime": stats24ElapsedTime,
       "stats24EndTime": stats24EndTime,
       "perfStatsGlobalSet": perfStatsGlobalSet,
       "perfStats15MinMaxRecord": perfStats15MinMaxRecord,
       "perfStats24HourMaxRecord": perfStats24HourMaxRecord,
       "perfStatsThresholdTable": perfStatsThresholdTable,
       "perfStatsThresholdEntry": perfStatsThresholdEntry,
       "perfStatsThresholdDeviceIndex": perfStatsThresholdDeviceIndex,
       "perfStatsThresholdCardIndex": perfStatsThresholdCardIndex,
       "perfStatsThresholdPortIndex": perfStatsThresholdPortIndex,
       "perfStatsThresholdTypeIndex": perfStatsThresholdTypeIndex,
       "perfStatsThresholdUpper": perfStatsThresholdUpper,
       "perfStatsThresholdLower": perfStatsThresholdLower,
       "perfStatsThresholdRowStatus": perfStatsThresholdRowStatus}
)
