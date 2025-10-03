# SNMP MIB module (PACKETLOGIC-SNOOPER-DHCP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\procera\PACKETLOGIC-SNOOPER-DHCP-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 12:21:26 2025
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

(CounterBasedGauge64,) = mibBuilder.importSymbols(
    "HCNUM-TC",
    "CounterBasedGauge64")

(snoopers,) = mibBuilder.importSymbols(
    "PACKETLOGIC-MIB",
    "snoopers")

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
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

dhcp = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 10, 1)
)
if mibBuilder.loadTexts:
    dhcp.setRevisions(
        ("2019-09-12 15:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_DhcpTable_Object = MibTable
dhcpTable = _DhcpTable_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 10, 1, 1)
)
if mibBuilder.loadTexts:
    dhcpTable.setStatus("current")
_DhcpEntry_Object = MibTableRow
dhcpEntry = _DhcpEntry_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 10, 1, 1, 1)
)
dhcpEntry.setIndexNames(
    (0, "PACKETLOGIC-SNOOPER-DHCP-MIB", "dhcpEntryIndex"),
)
if mibBuilder.loadTexts:
    dhcpEntry.setStatus("current")
_DhcpRequestsInQueue_ObjectIdentity = ObjectIdentity
dhcpRequestsInQueue = _DhcpRequestsInQueue_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 10, 1, 1, 1, 1)
)
_DhcpRequestsInQueueVal_Type = CounterBasedGauge64
_DhcpRequestsInQueueVal_Object = MibScalar
dhcpRequestsInQueueVal = _DhcpRequestsInQueueVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 10, 1, 1, 1, 1, 1),
    _DhcpRequestsInQueueVal_Type()
)
dhcpRequestsInQueueVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpRequestsInQueueVal.setStatus("current")
_DhcpRequestsInQueueMax_Type = CounterBasedGauge64
_DhcpRequestsInQueueMax_Object = MibScalar
dhcpRequestsInQueueMax = _DhcpRequestsInQueueMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 10, 1, 1, 1, 1, 3),
    _DhcpRequestsInQueueMax_Type()
)
dhcpRequestsInQueueMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpRequestsInQueueMax.setStatus("current")
_DhcpRequestsInQueueLevelTable_Object = MibTable
dhcpRequestsInQueueLevelTable = _DhcpRequestsInQueueLevelTable_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 10, 1, 1, 1, 1, 4)
)
if mibBuilder.loadTexts:
    dhcpRequestsInQueueLevelTable.setStatus("current")
_DhcpRequestsInQueueLevelEntry_Object = MibTableRow
dhcpRequestsInQueueLevelEntry = _DhcpRequestsInQueueLevelEntry_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 10, 1, 1, 1, 1, 4, 1)
)
dhcpRequestsInQueueLevelEntry.setIndexNames(
    (0, "PACKETLOGIC-SNOOPER-DHCP-MIB", "dhcpRequestsInQueueLevelName"),
)
if mibBuilder.loadTexts:
    dhcpRequestsInQueueLevelEntry.setStatus("current")
_DhcpRequestsInQueueLevelName_Type = DisplayString
_DhcpRequestsInQueueLevelName_Object = MibTableColumn
dhcpRequestsInQueueLevelName = _DhcpRequestsInQueueLevelName_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 10, 1, 1, 1, 1, 4, 1, 1),
    _DhcpRequestsInQueueLevelName_Type()
)
dhcpRequestsInQueueLevelName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dhcpRequestsInQueueLevelName.setStatus("current")
_DhcpRequestsInQueueLevelVal_Type = CounterBasedGauge64
_DhcpRequestsInQueueLevelVal_Object = MibTableColumn
dhcpRequestsInQueueLevelVal = _DhcpRequestsInQueueLevelVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 10, 1, 1, 1, 1, 4, 1, 2),
    _DhcpRequestsInQueueLevelVal_Type()
)
dhcpRequestsInQueueLevelVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpRequestsInQueueLevelVal.setStatus("current")
_DhcpRequestsInQueueLevelMax_Type = CounterBasedGauge64
_DhcpRequestsInQueueLevelMax_Object = MibTableColumn
dhcpRequestsInQueueLevelMax = _DhcpRequestsInQueueLevelMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 10, 1, 1, 1, 1, 4, 1, 4),
    _DhcpRequestsInQueueLevelMax_Type()
)
dhcpRequestsInQueueLevelMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpRequestsInQueueLevelMax.setStatus("current")
_DhcpDynAddFailures_ObjectIdentity = ObjectIdentity
dhcpDynAddFailures = _DhcpDynAddFailures_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 10, 1, 1, 1, 2)
)
_DhcpDynAddFailuresVal_Type = Counter64
_DhcpDynAddFailuresVal_Object = MibScalar
dhcpDynAddFailuresVal = _DhcpDynAddFailuresVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 10, 1, 1, 1, 2, 1),
    _DhcpDynAddFailuresVal_Type()
)
dhcpDynAddFailuresVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpDynAddFailuresVal.setStatus("current")
_DhcpDynAddFailuresMom_Type = CounterBasedGauge64
_DhcpDynAddFailuresMom_Object = MibScalar
dhcpDynAddFailuresMom = _DhcpDynAddFailuresMom_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 10, 1, 1, 1, 2, 2),
    _DhcpDynAddFailuresMom_Type()
)
dhcpDynAddFailuresMom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpDynAddFailuresMom.setStatus("current")
_DhcpDynAddFailuresMax_Type = CounterBasedGauge64
_DhcpDynAddFailuresMax_Object = MibScalar
dhcpDynAddFailuresMax = _DhcpDynAddFailuresMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 10, 1, 1, 1, 2, 3),
    _DhcpDynAddFailuresMax_Type()
)
dhcpDynAddFailuresMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpDynAddFailuresMax.setStatus("current")
_DhcpDynAddFailuresLevelTable_Object = MibTable
dhcpDynAddFailuresLevelTable = _DhcpDynAddFailuresLevelTable_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 10, 1, 1, 1, 2, 4)
)
if mibBuilder.loadTexts:
    dhcpDynAddFailuresLevelTable.setStatus("current")
_DhcpDynAddFailuresLevelEntry_Object = MibTableRow
dhcpDynAddFailuresLevelEntry = _DhcpDynAddFailuresLevelEntry_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 10, 1, 1, 1, 2, 4, 1)
)
dhcpDynAddFailuresLevelEntry.setIndexNames(
    (0, "PACKETLOGIC-SNOOPER-DHCP-MIB", "dhcpDynAddFailuresLevelName"),
)
if mibBuilder.loadTexts:
    dhcpDynAddFailuresLevelEntry.setStatus("current")
_DhcpDynAddFailuresLevelName_Type = DisplayString
_DhcpDynAddFailuresLevelName_Object = MibTableColumn
dhcpDynAddFailuresLevelName = _DhcpDynAddFailuresLevelName_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 10, 1, 1, 1, 2, 4, 1, 1),
    _DhcpDynAddFailuresLevelName_Type()
)
dhcpDynAddFailuresLevelName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dhcpDynAddFailuresLevelName.setStatus("current")
_DhcpDynAddFailuresLevelVal_Type = Counter64
_DhcpDynAddFailuresLevelVal_Object = MibTableColumn
dhcpDynAddFailuresLevelVal = _DhcpDynAddFailuresLevelVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 10, 1, 1, 1, 2, 4, 1, 2),
    _DhcpDynAddFailuresLevelVal_Type()
)
dhcpDynAddFailuresLevelVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpDynAddFailuresLevelVal.setStatus("current")
_DhcpDynAddFailuresLevelMom_Type = CounterBasedGauge64
_DhcpDynAddFailuresLevelMom_Object = MibTableColumn
dhcpDynAddFailuresLevelMom = _DhcpDynAddFailuresLevelMom_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 10, 1, 1, 1, 2, 4, 1, 3),
    _DhcpDynAddFailuresLevelMom_Type()
)
dhcpDynAddFailuresLevelMom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpDynAddFailuresLevelMom.setStatus("current")
_DhcpDynAddFailuresLevelMax_Type = CounterBasedGauge64
_DhcpDynAddFailuresLevelMax_Object = MibTableColumn
dhcpDynAddFailuresLevelMax = _DhcpDynAddFailuresLevelMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 10, 1, 1, 1, 2, 4, 1, 4),
    _DhcpDynAddFailuresLevelMax_Type()
)
dhcpDynAddFailuresLevelMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpDynAddFailuresLevelMax.setStatus("current")
_DhcpPLDBReconnects_ObjectIdentity = ObjectIdentity
dhcpPLDBReconnects = _DhcpPLDBReconnects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 10, 1, 1, 1, 3)
)
_DhcpPLDBReconnectsVal_Type = CounterBasedGauge64
_DhcpPLDBReconnectsVal_Object = MibScalar
dhcpPLDBReconnectsVal = _DhcpPLDBReconnectsVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 10, 1, 1, 1, 3, 1),
    _DhcpPLDBReconnectsVal_Type()
)
dhcpPLDBReconnectsVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpPLDBReconnectsVal.setStatus("current")
_DhcpPLDBReconnectsMax_Type = CounterBasedGauge64
_DhcpPLDBReconnectsMax_Object = MibScalar
dhcpPLDBReconnectsMax = _DhcpPLDBReconnectsMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 10, 1, 1, 1, 3, 3),
    _DhcpPLDBReconnectsMax_Type()
)
dhcpPLDBReconnectsMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpPLDBReconnectsMax.setStatus("current")
_DhcpPLDBReconnectsLevelTable_Object = MibTable
dhcpPLDBReconnectsLevelTable = _DhcpPLDBReconnectsLevelTable_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 10, 1, 1, 1, 3, 4)
)
if mibBuilder.loadTexts:
    dhcpPLDBReconnectsLevelTable.setStatus("current")
_DhcpPLDBReconnectsLevelEntry_Object = MibTableRow
dhcpPLDBReconnectsLevelEntry = _DhcpPLDBReconnectsLevelEntry_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 10, 1, 1, 1, 3, 4, 1)
)
dhcpPLDBReconnectsLevelEntry.setIndexNames(
    (0, "PACKETLOGIC-SNOOPER-DHCP-MIB", "dhcpPLDBReconnectsLevelName"),
)
if mibBuilder.loadTexts:
    dhcpPLDBReconnectsLevelEntry.setStatus("current")
_DhcpPLDBReconnectsLevelName_Type = DisplayString
_DhcpPLDBReconnectsLevelName_Object = MibTableColumn
dhcpPLDBReconnectsLevelName = _DhcpPLDBReconnectsLevelName_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 10, 1, 1, 1, 3, 4, 1, 1),
    _DhcpPLDBReconnectsLevelName_Type()
)
dhcpPLDBReconnectsLevelName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dhcpPLDBReconnectsLevelName.setStatus("current")
_DhcpPLDBReconnectsLevelVal_Type = CounterBasedGauge64
_DhcpPLDBReconnectsLevelVal_Object = MibTableColumn
dhcpPLDBReconnectsLevelVal = _DhcpPLDBReconnectsLevelVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 10, 1, 1, 1, 3, 4, 1, 2),
    _DhcpPLDBReconnectsLevelVal_Type()
)
dhcpPLDBReconnectsLevelVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpPLDBReconnectsLevelVal.setStatus("current")
_DhcpPLDBReconnectsLevelMax_Type = CounterBasedGauge64
_DhcpPLDBReconnectsLevelMax_Object = MibTableColumn
dhcpPLDBReconnectsLevelMax = _DhcpPLDBReconnectsLevelMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 10, 1, 1, 1, 3, 4, 1, 4),
    _DhcpPLDBReconnectsLevelMax_Type()
)
dhcpPLDBReconnectsLevelMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpPLDBReconnectsLevelMax.setStatus("current")
_DhcpPLDBUptime_ObjectIdentity = ObjectIdentity
dhcpPLDBUptime = _DhcpPLDBUptime_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 10, 1, 1, 1, 4)
)
_DhcpPLDBUptimeVal_Type = TimeTicks
_DhcpPLDBUptimeVal_Object = MibScalar
dhcpPLDBUptimeVal = _DhcpPLDBUptimeVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 10, 1, 1, 1, 4, 1),
    _DhcpPLDBUptimeVal_Type()
)
dhcpPLDBUptimeVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpPLDBUptimeVal.setStatus("current")
_DhcpPLDBUptimeLevelTable_Object = MibTable
dhcpPLDBUptimeLevelTable = _DhcpPLDBUptimeLevelTable_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 10, 1, 1, 1, 4, 2)
)
if mibBuilder.loadTexts:
    dhcpPLDBUptimeLevelTable.setStatus("current")
_DhcpPLDBUptimeLevelEntry_Object = MibTableRow
dhcpPLDBUptimeLevelEntry = _DhcpPLDBUptimeLevelEntry_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 10, 1, 1, 1, 4, 2, 1)
)
dhcpPLDBUptimeLevelEntry.setIndexNames(
    (0, "PACKETLOGIC-SNOOPER-DHCP-MIB", "dhcpPLDBUptimeLevelName"),
)
if mibBuilder.loadTexts:
    dhcpPLDBUptimeLevelEntry.setStatus("current")
_DhcpPLDBUptimeLevelName_Type = DisplayString
_DhcpPLDBUptimeLevelName_Object = MibTableColumn
dhcpPLDBUptimeLevelName = _DhcpPLDBUptimeLevelName_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 10, 1, 1, 1, 4, 2, 1, 1),
    _DhcpPLDBUptimeLevelName_Type()
)
dhcpPLDBUptimeLevelName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dhcpPLDBUptimeLevelName.setStatus("current")
_DhcpPLDBUptimeLevelVal_Type = TimeTicks
_DhcpPLDBUptimeLevelVal_Object = MibTableColumn
dhcpPLDBUptimeLevelVal = _DhcpPLDBUptimeLevelVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 10, 1, 1, 1, 4, 2, 1, 2),
    _DhcpPLDBUptimeLevelVal_Type()
)
dhcpPLDBUptimeLevelVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpPLDBUptimeLevelVal.setStatus("current")
_DhcpPLDBCommits_ObjectIdentity = ObjectIdentity
dhcpPLDBCommits = _DhcpPLDBCommits_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 10, 1, 1, 1, 5)
)
_DhcpPLDBCommitsVal_Type = Counter64
_DhcpPLDBCommitsVal_Object = MibScalar
dhcpPLDBCommitsVal = _DhcpPLDBCommitsVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 10, 1, 1, 1, 5, 1),
    _DhcpPLDBCommitsVal_Type()
)
dhcpPLDBCommitsVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpPLDBCommitsVal.setStatus("current")
_DhcpPLDBCommitsMom_Type = CounterBasedGauge64
_DhcpPLDBCommitsMom_Object = MibScalar
dhcpPLDBCommitsMom = _DhcpPLDBCommitsMom_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 10, 1, 1, 1, 5, 2),
    _DhcpPLDBCommitsMom_Type()
)
dhcpPLDBCommitsMom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpPLDBCommitsMom.setStatus("current")
_DhcpPLDBCommitsMax_Type = CounterBasedGauge64
_DhcpPLDBCommitsMax_Object = MibScalar
dhcpPLDBCommitsMax = _DhcpPLDBCommitsMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 10, 1, 1, 1, 5, 3),
    _DhcpPLDBCommitsMax_Type()
)
dhcpPLDBCommitsMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpPLDBCommitsMax.setStatus("current")
_DhcpPLDBCommitsLevelTable_Object = MibTable
dhcpPLDBCommitsLevelTable = _DhcpPLDBCommitsLevelTable_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 10, 1, 1, 1, 5, 4)
)
if mibBuilder.loadTexts:
    dhcpPLDBCommitsLevelTable.setStatus("current")
_DhcpPLDBCommitsLevelEntry_Object = MibTableRow
dhcpPLDBCommitsLevelEntry = _DhcpPLDBCommitsLevelEntry_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 10, 1, 1, 1, 5, 4, 1)
)
dhcpPLDBCommitsLevelEntry.setIndexNames(
    (0, "PACKETLOGIC-SNOOPER-DHCP-MIB", "dhcpPLDBCommitsLevelName"),
)
if mibBuilder.loadTexts:
    dhcpPLDBCommitsLevelEntry.setStatus("current")
_DhcpPLDBCommitsLevelName_Type = DisplayString
_DhcpPLDBCommitsLevelName_Object = MibTableColumn
dhcpPLDBCommitsLevelName = _DhcpPLDBCommitsLevelName_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 10, 1, 1, 1, 5, 4, 1, 1),
    _DhcpPLDBCommitsLevelName_Type()
)
dhcpPLDBCommitsLevelName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dhcpPLDBCommitsLevelName.setStatus("current")
_DhcpPLDBCommitsLevelVal_Type = Counter64
_DhcpPLDBCommitsLevelVal_Object = MibTableColumn
dhcpPLDBCommitsLevelVal = _DhcpPLDBCommitsLevelVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 10, 1, 1, 1, 5, 4, 1, 2),
    _DhcpPLDBCommitsLevelVal_Type()
)
dhcpPLDBCommitsLevelVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpPLDBCommitsLevelVal.setStatus("current")
_DhcpPLDBCommitsLevelMom_Type = CounterBasedGauge64
_DhcpPLDBCommitsLevelMom_Object = MibTableColumn
dhcpPLDBCommitsLevelMom = _DhcpPLDBCommitsLevelMom_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 10, 1, 1, 1, 5, 4, 1, 3),
    _DhcpPLDBCommitsLevelMom_Type()
)
dhcpPLDBCommitsLevelMom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpPLDBCommitsLevelMom.setStatus("current")
_DhcpPLDBCommitsLevelMax_Type = CounterBasedGauge64
_DhcpPLDBCommitsLevelMax_Object = MibTableColumn
dhcpPLDBCommitsLevelMax = _DhcpPLDBCommitsLevelMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 10, 1, 1, 1, 5, 4, 1, 4),
    _DhcpPLDBCommitsLevelMax_Type()
)
dhcpPLDBCommitsLevelMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpPLDBCommitsLevelMax.setStatus("current")
_DhcpPLDReconnects_ObjectIdentity = ObjectIdentity
dhcpPLDReconnects = _DhcpPLDReconnects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 10, 1, 1, 1, 6)
)
_DhcpPLDReconnectsVal_Type = CounterBasedGauge64
_DhcpPLDReconnectsVal_Object = MibScalar
dhcpPLDReconnectsVal = _DhcpPLDReconnectsVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 10, 1, 1, 1, 6, 1),
    _DhcpPLDReconnectsVal_Type()
)
dhcpPLDReconnectsVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpPLDReconnectsVal.setStatus("current")
_DhcpPLDReconnectsMax_Type = CounterBasedGauge64
_DhcpPLDReconnectsMax_Object = MibScalar
dhcpPLDReconnectsMax = _DhcpPLDReconnectsMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 10, 1, 1, 1, 6, 3),
    _DhcpPLDReconnectsMax_Type()
)
dhcpPLDReconnectsMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpPLDReconnectsMax.setStatus("current")
_DhcpPLDReconnectsLevelTable_Object = MibTable
dhcpPLDReconnectsLevelTable = _DhcpPLDReconnectsLevelTable_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 10, 1, 1, 1, 6, 4)
)
if mibBuilder.loadTexts:
    dhcpPLDReconnectsLevelTable.setStatus("current")
_DhcpPLDReconnectsLevelEntry_Object = MibTableRow
dhcpPLDReconnectsLevelEntry = _DhcpPLDReconnectsLevelEntry_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 10, 1, 1, 1, 6, 4, 1)
)
dhcpPLDReconnectsLevelEntry.setIndexNames(
    (0, "PACKETLOGIC-SNOOPER-DHCP-MIB", "dhcpPLDReconnectsLevelName"),
)
if mibBuilder.loadTexts:
    dhcpPLDReconnectsLevelEntry.setStatus("current")
_DhcpPLDReconnectsLevelName_Type = DisplayString
_DhcpPLDReconnectsLevelName_Object = MibTableColumn
dhcpPLDReconnectsLevelName = _DhcpPLDReconnectsLevelName_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 10, 1, 1, 1, 6, 4, 1, 1),
    _DhcpPLDReconnectsLevelName_Type()
)
dhcpPLDReconnectsLevelName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dhcpPLDReconnectsLevelName.setStatus("current")
_DhcpPLDReconnectsLevelVal_Type = CounterBasedGauge64
_DhcpPLDReconnectsLevelVal_Object = MibTableColumn
dhcpPLDReconnectsLevelVal = _DhcpPLDReconnectsLevelVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 10, 1, 1, 1, 6, 4, 1, 2),
    _DhcpPLDReconnectsLevelVal_Type()
)
dhcpPLDReconnectsLevelVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpPLDReconnectsLevelVal.setStatus("current")
_DhcpPLDReconnectsLevelMax_Type = CounterBasedGauge64
_DhcpPLDReconnectsLevelMax_Object = MibTableColumn
dhcpPLDReconnectsLevelMax = _DhcpPLDReconnectsLevelMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 10, 1, 1, 1, 6, 4, 1, 4),
    _DhcpPLDReconnectsLevelMax_Type()
)
dhcpPLDReconnectsLevelMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpPLDReconnectsLevelMax.setStatus("current")
_DhcpPLDUptime_ObjectIdentity = ObjectIdentity
dhcpPLDUptime = _DhcpPLDUptime_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 10, 1, 1, 1, 7)
)
_DhcpPLDUptimeVal_Type = TimeTicks
_DhcpPLDUptimeVal_Object = MibScalar
dhcpPLDUptimeVal = _DhcpPLDUptimeVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 10, 1, 1, 1, 7, 1),
    _DhcpPLDUptimeVal_Type()
)
dhcpPLDUptimeVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpPLDUptimeVal.setStatus("current")
_DhcpPLDUptimeLevelTable_Object = MibTable
dhcpPLDUptimeLevelTable = _DhcpPLDUptimeLevelTable_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 10, 1, 1, 1, 7, 2)
)
if mibBuilder.loadTexts:
    dhcpPLDUptimeLevelTable.setStatus("current")
_DhcpPLDUptimeLevelEntry_Object = MibTableRow
dhcpPLDUptimeLevelEntry = _DhcpPLDUptimeLevelEntry_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 10, 1, 1, 1, 7, 2, 1)
)
dhcpPLDUptimeLevelEntry.setIndexNames(
    (0, "PACKETLOGIC-SNOOPER-DHCP-MIB", "dhcpPLDUptimeLevelName"),
)
if mibBuilder.loadTexts:
    dhcpPLDUptimeLevelEntry.setStatus("current")
_DhcpPLDUptimeLevelName_Type = DisplayString
_DhcpPLDUptimeLevelName_Object = MibTableColumn
dhcpPLDUptimeLevelName = _DhcpPLDUptimeLevelName_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 10, 1, 1, 1, 7, 2, 1, 1),
    _DhcpPLDUptimeLevelName_Type()
)
dhcpPLDUptimeLevelName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dhcpPLDUptimeLevelName.setStatus("current")
_DhcpPLDUptimeLevelVal_Type = TimeTicks
_DhcpPLDUptimeLevelVal_Object = MibTableColumn
dhcpPLDUptimeLevelVal = _DhcpPLDUptimeLevelVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 10, 1, 1, 1, 7, 2, 1, 2),
    _DhcpPLDUptimeLevelVal_Type()
)
dhcpPLDUptimeLevelVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpPLDUptimeLevelVal.setStatus("current")
_DhcpPLDOperations_ObjectIdentity = ObjectIdentity
dhcpPLDOperations = _DhcpPLDOperations_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 10, 1, 1, 1, 8)
)
_DhcpPLDOperationsVal_Type = Counter64
_DhcpPLDOperationsVal_Object = MibScalar
dhcpPLDOperationsVal = _DhcpPLDOperationsVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 10, 1, 1, 1, 8, 1),
    _DhcpPLDOperationsVal_Type()
)
dhcpPLDOperationsVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpPLDOperationsVal.setStatus("current")
_DhcpPLDOperationsMom_Type = CounterBasedGauge64
_DhcpPLDOperationsMom_Object = MibScalar
dhcpPLDOperationsMom = _DhcpPLDOperationsMom_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 10, 1, 1, 1, 8, 2),
    _DhcpPLDOperationsMom_Type()
)
dhcpPLDOperationsMom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpPLDOperationsMom.setStatus("current")
_DhcpPLDOperationsMax_Type = CounterBasedGauge64
_DhcpPLDOperationsMax_Object = MibScalar
dhcpPLDOperationsMax = _DhcpPLDOperationsMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 10, 1, 1, 1, 8, 3),
    _DhcpPLDOperationsMax_Type()
)
dhcpPLDOperationsMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpPLDOperationsMax.setStatus("current")
_DhcpPLDOperationsLevelTable_Object = MibTable
dhcpPLDOperationsLevelTable = _DhcpPLDOperationsLevelTable_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 10, 1, 1, 1, 8, 4)
)
if mibBuilder.loadTexts:
    dhcpPLDOperationsLevelTable.setStatus("current")
_DhcpPLDOperationsLevelEntry_Object = MibTableRow
dhcpPLDOperationsLevelEntry = _DhcpPLDOperationsLevelEntry_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 10, 1, 1, 1, 8, 4, 1)
)
dhcpPLDOperationsLevelEntry.setIndexNames(
    (0, "PACKETLOGIC-SNOOPER-DHCP-MIB", "dhcpPLDOperationsLevelName"),
)
if mibBuilder.loadTexts:
    dhcpPLDOperationsLevelEntry.setStatus("current")
_DhcpPLDOperationsLevelName_Type = DisplayString
_DhcpPLDOperationsLevelName_Object = MibTableColumn
dhcpPLDOperationsLevelName = _DhcpPLDOperationsLevelName_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 10, 1, 1, 1, 8, 4, 1, 1),
    _DhcpPLDOperationsLevelName_Type()
)
dhcpPLDOperationsLevelName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dhcpPLDOperationsLevelName.setStatus("current")
_DhcpPLDOperationsLevelVal_Type = Counter64
_DhcpPLDOperationsLevelVal_Object = MibTableColumn
dhcpPLDOperationsLevelVal = _DhcpPLDOperationsLevelVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 10, 1, 1, 1, 8, 4, 1, 2),
    _DhcpPLDOperationsLevelVal_Type()
)
dhcpPLDOperationsLevelVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpPLDOperationsLevelVal.setStatus("current")
_DhcpPLDOperationsLevelMom_Type = CounterBasedGauge64
_DhcpPLDOperationsLevelMom_Object = MibTableColumn
dhcpPLDOperationsLevelMom = _DhcpPLDOperationsLevelMom_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 10, 1, 1, 1, 8, 4, 1, 3),
    _DhcpPLDOperationsLevelMom_Type()
)
dhcpPLDOperationsLevelMom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpPLDOperationsLevelMom.setStatus("current")
_DhcpPLDOperationsLevelMax_Type = CounterBasedGauge64
_DhcpPLDOperationsLevelMax_Object = MibTableColumn
dhcpPLDOperationsLevelMax = _DhcpPLDOperationsLevelMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 10, 1, 1, 1, 8, 4, 1, 4),
    _DhcpPLDOperationsLevelMax_Type()
)
dhcpPLDOperationsLevelMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpPLDOperationsLevelMax.setStatus("current")
_DhcpPackets_ObjectIdentity = ObjectIdentity
dhcpPackets = _DhcpPackets_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 10, 1, 1, 1, 9)
)
_DhcpPacketsVal_Type = Counter64
_DhcpPacketsVal_Object = MibScalar
dhcpPacketsVal = _DhcpPacketsVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 10, 1, 1, 1, 9, 1),
    _DhcpPacketsVal_Type()
)
dhcpPacketsVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpPacketsVal.setStatus("current")
_DhcpPacketsMom_Type = CounterBasedGauge64
_DhcpPacketsMom_Object = MibScalar
dhcpPacketsMom = _DhcpPacketsMom_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 10, 1, 1, 1, 9, 2),
    _DhcpPacketsMom_Type()
)
dhcpPacketsMom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpPacketsMom.setStatus("current")
_DhcpPacketsMax_Type = CounterBasedGauge64
_DhcpPacketsMax_Object = MibScalar
dhcpPacketsMax = _DhcpPacketsMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 10, 1, 1, 1, 9, 3),
    _DhcpPacketsMax_Type()
)
dhcpPacketsMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpPacketsMax.setStatus("current")
_DhcpPacketsLevelTable_Object = MibTable
dhcpPacketsLevelTable = _DhcpPacketsLevelTable_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 10, 1, 1, 1, 9, 4)
)
if mibBuilder.loadTexts:
    dhcpPacketsLevelTable.setStatus("current")
_DhcpPacketsLevelEntry_Object = MibTableRow
dhcpPacketsLevelEntry = _DhcpPacketsLevelEntry_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 10, 1, 1, 1, 9, 4, 1)
)
dhcpPacketsLevelEntry.setIndexNames(
    (0, "PACKETLOGIC-SNOOPER-DHCP-MIB", "dhcpPacketsLevelName"),
)
if mibBuilder.loadTexts:
    dhcpPacketsLevelEntry.setStatus("current")
_DhcpPacketsLevelName_Type = DisplayString
_DhcpPacketsLevelName_Object = MibTableColumn
dhcpPacketsLevelName = _DhcpPacketsLevelName_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 10, 1, 1, 1, 9, 4, 1, 1),
    _DhcpPacketsLevelName_Type()
)
dhcpPacketsLevelName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dhcpPacketsLevelName.setStatus("current")
_DhcpPacketsLevelVal_Type = Counter64
_DhcpPacketsLevelVal_Object = MibTableColumn
dhcpPacketsLevelVal = _DhcpPacketsLevelVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 10, 1, 1, 1, 9, 4, 1, 2),
    _DhcpPacketsLevelVal_Type()
)
dhcpPacketsLevelVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpPacketsLevelVal.setStatus("current")
_DhcpPacketsLevelMom_Type = CounterBasedGauge64
_DhcpPacketsLevelMom_Object = MibTableColumn
dhcpPacketsLevelMom = _DhcpPacketsLevelMom_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 10, 1, 1, 1, 9, 4, 1, 3),
    _DhcpPacketsLevelMom_Type()
)
dhcpPacketsLevelMom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpPacketsLevelMom.setStatus("current")
_DhcpPacketsLevelMax_Type = CounterBasedGauge64
_DhcpPacketsLevelMax_Object = MibTableColumn
dhcpPacketsLevelMax = _DhcpPacketsLevelMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 10, 1, 1, 1, 9, 4, 1, 4),
    _DhcpPacketsLevelMax_Type()
)
dhcpPacketsLevelMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpPacketsLevelMax.setStatus("current")
_DhcpUnparsablePackets_ObjectIdentity = ObjectIdentity
dhcpUnparsablePackets = _DhcpUnparsablePackets_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 10, 1, 1, 1, 10)
)
_DhcpUnparsablePacketsVal_Type = Counter64
_DhcpUnparsablePacketsVal_Object = MibScalar
dhcpUnparsablePacketsVal = _DhcpUnparsablePacketsVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 10, 1, 1, 1, 10, 1),
    _DhcpUnparsablePacketsVal_Type()
)
dhcpUnparsablePacketsVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpUnparsablePacketsVal.setStatus("current")
_DhcpUnparsablePacketsMom_Type = CounterBasedGauge64
_DhcpUnparsablePacketsMom_Object = MibScalar
dhcpUnparsablePacketsMom = _DhcpUnparsablePacketsMom_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 10, 1, 1, 1, 10, 2),
    _DhcpUnparsablePacketsMom_Type()
)
dhcpUnparsablePacketsMom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpUnparsablePacketsMom.setStatus("current")
_DhcpUnparsablePacketsMax_Type = CounterBasedGauge64
_DhcpUnparsablePacketsMax_Object = MibScalar
dhcpUnparsablePacketsMax = _DhcpUnparsablePacketsMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 10, 1, 1, 1, 10, 3),
    _DhcpUnparsablePacketsMax_Type()
)
dhcpUnparsablePacketsMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpUnparsablePacketsMax.setStatus("current")
_DhcpUnparsablePacketsLevelTable_Object = MibTable
dhcpUnparsablePacketsLevelTable = _DhcpUnparsablePacketsLevelTable_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 10, 1, 1, 1, 10, 4)
)
if mibBuilder.loadTexts:
    dhcpUnparsablePacketsLevelTable.setStatus("current")
_DhcpUnparsablePacketsLevelEntry_Object = MibTableRow
dhcpUnparsablePacketsLevelEntry = _DhcpUnparsablePacketsLevelEntry_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 10, 1, 1, 1, 10, 4, 1)
)
dhcpUnparsablePacketsLevelEntry.setIndexNames(
    (0, "PACKETLOGIC-SNOOPER-DHCP-MIB", "dhcpUnparsablePacketsLevelName"),
)
if mibBuilder.loadTexts:
    dhcpUnparsablePacketsLevelEntry.setStatus("current")
_DhcpUnparsablePacketsLevelName_Type = DisplayString
_DhcpUnparsablePacketsLevelName_Object = MibTableColumn
dhcpUnparsablePacketsLevelName = _DhcpUnparsablePacketsLevelName_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 10, 1, 1, 1, 10, 4, 1, 1),
    _DhcpUnparsablePacketsLevelName_Type()
)
dhcpUnparsablePacketsLevelName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dhcpUnparsablePacketsLevelName.setStatus("current")
_DhcpUnparsablePacketsLevelVal_Type = Counter64
_DhcpUnparsablePacketsLevelVal_Object = MibTableColumn
dhcpUnparsablePacketsLevelVal = _DhcpUnparsablePacketsLevelVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 10, 1, 1, 1, 10, 4, 1, 2),
    _DhcpUnparsablePacketsLevelVal_Type()
)
dhcpUnparsablePacketsLevelVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpUnparsablePacketsLevelVal.setStatus("current")
_DhcpUnparsablePacketsLevelMom_Type = CounterBasedGauge64
_DhcpUnparsablePacketsLevelMom_Object = MibTableColumn
dhcpUnparsablePacketsLevelMom = _DhcpUnparsablePacketsLevelMom_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 10, 1, 1, 1, 10, 4, 1, 3),
    _DhcpUnparsablePacketsLevelMom_Type()
)
dhcpUnparsablePacketsLevelMom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpUnparsablePacketsLevelMom.setStatus("current")
_DhcpUnparsablePacketsLevelMax_Type = CounterBasedGauge64
_DhcpUnparsablePacketsLevelMax_Object = MibTableColumn
dhcpUnparsablePacketsLevelMax = _DhcpUnparsablePacketsLevelMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 10, 1, 1, 1, 10, 4, 1, 4),
    _DhcpUnparsablePacketsLevelMax_Type()
)
dhcpUnparsablePacketsLevelMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpUnparsablePacketsLevelMax.setStatus("current")
_DhcpPacketsReq_ObjectIdentity = ObjectIdentity
dhcpPacketsReq = _DhcpPacketsReq_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 10, 1, 1, 1, 11)
)
_DhcpPacketsReqVal_Type = Counter64
_DhcpPacketsReqVal_Object = MibScalar
dhcpPacketsReqVal = _DhcpPacketsReqVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 10, 1, 1, 1, 11, 1),
    _DhcpPacketsReqVal_Type()
)
dhcpPacketsReqVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpPacketsReqVal.setStatus("current")
_DhcpPacketsReqMom_Type = CounterBasedGauge64
_DhcpPacketsReqMom_Object = MibScalar
dhcpPacketsReqMom = _DhcpPacketsReqMom_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 10, 1, 1, 1, 11, 2),
    _DhcpPacketsReqMom_Type()
)
dhcpPacketsReqMom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpPacketsReqMom.setStatus("current")
_DhcpPacketsReqMax_Type = CounterBasedGauge64
_DhcpPacketsReqMax_Object = MibScalar
dhcpPacketsReqMax = _DhcpPacketsReqMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 10, 1, 1, 1, 11, 3),
    _DhcpPacketsReqMax_Type()
)
dhcpPacketsReqMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpPacketsReqMax.setStatus("current")
_DhcpPacketsReqLevelTable_Object = MibTable
dhcpPacketsReqLevelTable = _DhcpPacketsReqLevelTable_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 10, 1, 1, 1, 11, 4)
)
if mibBuilder.loadTexts:
    dhcpPacketsReqLevelTable.setStatus("current")
_DhcpPacketsReqLevelEntry_Object = MibTableRow
dhcpPacketsReqLevelEntry = _DhcpPacketsReqLevelEntry_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 10, 1, 1, 1, 11, 4, 1)
)
dhcpPacketsReqLevelEntry.setIndexNames(
    (0, "PACKETLOGIC-SNOOPER-DHCP-MIB", "dhcpPacketsReqLevelName"),
)
if mibBuilder.loadTexts:
    dhcpPacketsReqLevelEntry.setStatus("current")
_DhcpPacketsReqLevelName_Type = DisplayString
_DhcpPacketsReqLevelName_Object = MibTableColumn
dhcpPacketsReqLevelName = _DhcpPacketsReqLevelName_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 10, 1, 1, 1, 11, 4, 1, 1),
    _DhcpPacketsReqLevelName_Type()
)
dhcpPacketsReqLevelName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dhcpPacketsReqLevelName.setStatus("current")
_DhcpPacketsReqLevelVal_Type = Counter64
_DhcpPacketsReqLevelVal_Object = MibTableColumn
dhcpPacketsReqLevelVal = _DhcpPacketsReqLevelVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 10, 1, 1, 1, 11, 4, 1, 2),
    _DhcpPacketsReqLevelVal_Type()
)
dhcpPacketsReqLevelVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpPacketsReqLevelVal.setStatus("current")
_DhcpPacketsReqLevelMom_Type = CounterBasedGauge64
_DhcpPacketsReqLevelMom_Object = MibTableColumn
dhcpPacketsReqLevelMom = _DhcpPacketsReqLevelMom_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 10, 1, 1, 1, 11, 4, 1, 3),
    _DhcpPacketsReqLevelMom_Type()
)
dhcpPacketsReqLevelMom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpPacketsReqLevelMom.setStatus("current")
_DhcpPacketsReqLevelMax_Type = CounterBasedGauge64
_DhcpPacketsReqLevelMax_Object = MibTableColumn
dhcpPacketsReqLevelMax = _DhcpPacketsReqLevelMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 10, 1, 1, 1, 11, 4, 1, 4),
    _DhcpPacketsReqLevelMax_Type()
)
dhcpPacketsReqLevelMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpPacketsReqLevelMax.setStatus("current")
_DhcpPacketsAck_ObjectIdentity = ObjectIdentity
dhcpPacketsAck = _DhcpPacketsAck_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 10, 1, 1, 1, 12)
)
_DhcpPacketsAckVal_Type = Counter64
_DhcpPacketsAckVal_Object = MibScalar
dhcpPacketsAckVal = _DhcpPacketsAckVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 10, 1, 1, 1, 12, 1),
    _DhcpPacketsAckVal_Type()
)
dhcpPacketsAckVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpPacketsAckVal.setStatus("current")
_DhcpPacketsAckMom_Type = CounterBasedGauge64
_DhcpPacketsAckMom_Object = MibScalar
dhcpPacketsAckMom = _DhcpPacketsAckMom_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 10, 1, 1, 1, 12, 2),
    _DhcpPacketsAckMom_Type()
)
dhcpPacketsAckMom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpPacketsAckMom.setStatus("current")
_DhcpPacketsAckMax_Type = CounterBasedGauge64
_DhcpPacketsAckMax_Object = MibScalar
dhcpPacketsAckMax = _DhcpPacketsAckMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 10, 1, 1, 1, 12, 3),
    _DhcpPacketsAckMax_Type()
)
dhcpPacketsAckMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpPacketsAckMax.setStatus("current")
_DhcpPacketsAckLevelTable_Object = MibTable
dhcpPacketsAckLevelTable = _DhcpPacketsAckLevelTable_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 10, 1, 1, 1, 12, 4)
)
if mibBuilder.loadTexts:
    dhcpPacketsAckLevelTable.setStatus("current")
_DhcpPacketsAckLevelEntry_Object = MibTableRow
dhcpPacketsAckLevelEntry = _DhcpPacketsAckLevelEntry_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 10, 1, 1, 1, 12, 4, 1)
)
dhcpPacketsAckLevelEntry.setIndexNames(
    (0, "PACKETLOGIC-SNOOPER-DHCP-MIB", "dhcpPacketsAckLevelName"),
)
if mibBuilder.loadTexts:
    dhcpPacketsAckLevelEntry.setStatus("current")
_DhcpPacketsAckLevelName_Type = DisplayString
_DhcpPacketsAckLevelName_Object = MibTableColumn
dhcpPacketsAckLevelName = _DhcpPacketsAckLevelName_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 10, 1, 1, 1, 12, 4, 1, 1),
    _DhcpPacketsAckLevelName_Type()
)
dhcpPacketsAckLevelName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dhcpPacketsAckLevelName.setStatus("current")
_DhcpPacketsAckLevelVal_Type = Counter64
_DhcpPacketsAckLevelVal_Object = MibTableColumn
dhcpPacketsAckLevelVal = _DhcpPacketsAckLevelVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 10, 1, 1, 1, 12, 4, 1, 2),
    _DhcpPacketsAckLevelVal_Type()
)
dhcpPacketsAckLevelVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpPacketsAckLevelVal.setStatus("current")
_DhcpPacketsAckLevelMom_Type = CounterBasedGauge64
_DhcpPacketsAckLevelMom_Object = MibTableColumn
dhcpPacketsAckLevelMom = _DhcpPacketsAckLevelMom_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 10, 1, 1, 1, 12, 4, 1, 3),
    _DhcpPacketsAckLevelMom_Type()
)
dhcpPacketsAckLevelMom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpPacketsAckLevelMom.setStatus("current")
_DhcpPacketsAckLevelMax_Type = CounterBasedGauge64
_DhcpPacketsAckLevelMax_Object = MibTableColumn
dhcpPacketsAckLevelMax = _DhcpPacketsAckLevelMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 10, 1, 1, 1, 12, 4, 1, 4),
    _DhcpPacketsAckLevelMax_Type()
)
dhcpPacketsAckLevelMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpPacketsAckLevelMax.setStatus("current")
_DhcpPacketsIgnored_ObjectIdentity = ObjectIdentity
dhcpPacketsIgnored = _DhcpPacketsIgnored_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 10, 1, 1, 1, 13)
)
_DhcpPacketsIgnoredVal_Type = Counter64
_DhcpPacketsIgnoredVal_Object = MibScalar
dhcpPacketsIgnoredVal = _DhcpPacketsIgnoredVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 10, 1, 1, 1, 13, 1),
    _DhcpPacketsIgnoredVal_Type()
)
dhcpPacketsIgnoredVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpPacketsIgnoredVal.setStatus("current")
_DhcpPacketsIgnoredMom_Type = CounterBasedGauge64
_DhcpPacketsIgnoredMom_Object = MibScalar
dhcpPacketsIgnoredMom = _DhcpPacketsIgnoredMom_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 10, 1, 1, 1, 13, 2),
    _DhcpPacketsIgnoredMom_Type()
)
dhcpPacketsIgnoredMom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpPacketsIgnoredMom.setStatus("current")
_DhcpPacketsIgnoredMax_Type = CounterBasedGauge64
_DhcpPacketsIgnoredMax_Object = MibScalar
dhcpPacketsIgnoredMax = _DhcpPacketsIgnoredMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 10, 1, 1, 1, 13, 3),
    _DhcpPacketsIgnoredMax_Type()
)
dhcpPacketsIgnoredMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpPacketsIgnoredMax.setStatus("current")
_DhcpPacketsIgnoredLevelTable_Object = MibTable
dhcpPacketsIgnoredLevelTable = _DhcpPacketsIgnoredLevelTable_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 10, 1, 1, 1, 13, 4)
)
if mibBuilder.loadTexts:
    dhcpPacketsIgnoredLevelTable.setStatus("current")
_DhcpPacketsIgnoredLevelEntry_Object = MibTableRow
dhcpPacketsIgnoredLevelEntry = _DhcpPacketsIgnoredLevelEntry_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 10, 1, 1, 1, 13, 4, 1)
)
dhcpPacketsIgnoredLevelEntry.setIndexNames(
    (0, "PACKETLOGIC-SNOOPER-DHCP-MIB", "dhcpPacketsIgnoredLevelName"),
)
if mibBuilder.loadTexts:
    dhcpPacketsIgnoredLevelEntry.setStatus("current")
_DhcpPacketsIgnoredLevelName_Type = DisplayString
_DhcpPacketsIgnoredLevelName_Object = MibTableColumn
dhcpPacketsIgnoredLevelName = _DhcpPacketsIgnoredLevelName_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 10, 1, 1, 1, 13, 4, 1, 1),
    _DhcpPacketsIgnoredLevelName_Type()
)
dhcpPacketsIgnoredLevelName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dhcpPacketsIgnoredLevelName.setStatus("current")
_DhcpPacketsIgnoredLevelVal_Type = Counter64
_DhcpPacketsIgnoredLevelVal_Object = MibTableColumn
dhcpPacketsIgnoredLevelVal = _DhcpPacketsIgnoredLevelVal_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 10, 1, 1, 1, 13, 4, 1, 2),
    _DhcpPacketsIgnoredLevelVal_Type()
)
dhcpPacketsIgnoredLevelVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpPacketsIgnoredLevelVal.setStatus("current")
_DhcpPacketsIgnoredLevelMom_Type = CounterBasedGauge64
_DhcpPacketsIgnoredLevelMom_Object = MibTableColumn
dhcpPacketsIgnoredLevelMom = _DhcpPacketsIgnoredLevelMom_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 10, 1, 1, 1, 13, 4, 1, 3),
    _DhcpPacketsIgnoredLevelMom_Type()
)
dhcpPacketsIgnoredLevelMom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpPacketsIgnoredLevelMom.setStatus("current")
_DhcpPacketsIgnoredLevelMax_Type = CounterBasedGauge64
_DhcpPacketsIgnoredLevelMax_Object = MibTableColumn
dhcpPacketsIgnoredLevelMax = _DhcpPacketsIgnoredLevelMax_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 10, 1, 1, 1, 13, 4, 1, 4),
    _DhcpPacketsIgnoredLevelMax_Type()
)
dhcpPacketsIgnoredLevelMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpPacketsIgnoredLevelMax.setStatus("current")


class _DhcpEntryIndex_Type(Integer32):
    """Custom type dhcpEntryIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_DhcpEntryIndex_Type.__name__ = "Integer32"
_DhcpEntryIndex_Object = MibTableColumn
dhcpEntryIndex = _DhcpEntryIndex_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 10, 1, 1, 1, 999),
    _DhcpEntryIndex_Type()
)
dhcpEntryIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dhcpEntryIndex.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "PACKETLOGIC-SNOOPER-DHCP-MIB",
    **{"dhcp": dhcp,
       "dhcpTable": dhcpTable,
       "dhcpEntry": dhcpEntry,
       "dhcpRequestsInQueue": dhcpRequestsInQueue,
       "dhcpRequestsInQueueVal": dhcpRequestsInQueueVal,
       "dhcpRequestsInQueueMax": dhcpRequestsInQueueMax,
       "dhcpRequestsInQueueLevelTable": dhcpRequestsInQueueLevelTable,
       "dhcpRequestsInQueueLevelEntry": dhcpRequestsInQueueLevelEntry,
       "dhcpRequestsInQueueLevelName": dhcpRequestsInQueueLevelName,
       "dhcpRequestsInQueueLevelVal": dhcpRequestsInQueueLevelVal,
       "dhcpRequestsInQueueLevelMax": dhcpRequestsInQueueLevelMax,
       "dhcpDynAddFailures": dhcpDynAddFailures,
       "dhcpDynAddFailuresVal": dhcpDynAddFailuresVal,
       "dhcpDynAddFailuresMom": dhcpDynAddFailuresMom,
       "dhcpDynAddFailuresMax": dhcpDynAddFailuresMax,
       "dhcpDynAddFailuresLevelTable": dhcpDynAddFailuresLevelTable,
       "dhcpDynAddFailuresLevelEntry": dhcpDynAddFailuresLevelEntry,
       "dhcpDynAddFailuresLevelName": dhcpDynAddFailuresLevelName,
       "dhcpDynAddFailuresLevelVal": dhcpDynAddFailuresLevelVal,
       "dhcpDynAddFailuresLevelMom": dhcpDynAddFailuresLevelMom,
       "dhcpDynAddFailuresLevelMax": dhcpDynAddFailuresLevelMax,
       "dhcpPLDBReconnects": dhcpPLDBReconnects,
       "dhcpPLDBReconnectsVal": dhcpPLDBReconnectsVal,
       "dhcpPLDBReconnectsMax": dhcpPLDBReconnectsMax,
       "dhcpPLDBReconnectsLevelTable": dhcpPLDBReconnectsLevelTable,
       "dhcpPLDBReconnectsLevelEntry": dhcpPLDBReconnectsLevelEntry,
       "dhcpPLDBReconnectsLevelName": dhcpPLDBReconnectsLevelName,
       "dhcpPLDBReconnectsLevelVal": dhcpPLDBReconnectsLevelVal,
       "dhcpPLDBReconnectsLevelMax": dhcpPLDBReconnectsLevelMax,
       "dhcpPLDBUptime": dhcpPLDBUptime,
       "dhcpPLDBUptimeVal": dhcpPLDBUptimeVal,
       "dhcpPLDBUptimeLevelTable": dhcpPLDBUptimeLevelTable,
       "dhcpPLDBUptimeLevelEntry": dhcpPLDBUptimeLevelEntry,
       "dhcpPLDBUptimeLevelName": dhcpPLDBUptimeLevelName,
       "dhcpPLDBUptimeLevelVal": dhcpPLDBUptimeLevelVal,
       "dhcpPLDBCommits": dhcpPLDBCommits,
       "dhcpPLDBCommitsVal": dhcpPLDBCommitsVal,
       "dhcpPLDBCommitsMom": dhcpPLDBCommitsMom,
       "dhcpPLDBCommitsMax": dhcpPLDBCommitsMax,
       "dhcpPLDBCommitsLevelTable": dhcpPLDBCommitsLevelTable,
       "dhcpPLDBCommitsLevelEntry": dhcpPLDBCommitsLevelEntry,
       "dhcpPLDBCommitsLevelName": dhcpPLDBCommitsLevelName,
       "dhcpPLDBCommitsLevelVal": dhcpPLDBCommitsLevelVal,
       "dhcpPLDBCommitsLevelMom": dhcpPLDBCommitsLevelMom,
       "dhcpPLDBCommitsLevelMax": dhcpPLDBCommitsLevelMax,
       "dhcpPLDReconnects": dhcpPLDReconnects,
       "dhcpPLDReconnectsVal": dhcpPLDReconnectsVal,
       "dhcpPLDReconnectsMax": dhcpPLDReconnectsMax,
       "dhcpPLDReconnectsLevelTable": dhcpPLDReconnectsLevelTable,
       "dhcpPLDReconnectsLevelEntry": dhcpPLDReconnectsLevelEntry,
       "dhcpPLDReconnectsLevelName": dhcpPLDReconnectsLevelName,
       "dhcpPLDReconnectsLevelVal": dhcpPLDReconnectsLevelVal,
       "dhcpPLDReconnectsLevelMax": dhcpPLDReconnectsLevelMax,
       "dhcpPLDUptime": dhcpPLDUptime,
       "dhcpPLDUptimeVal": dhcpPLDUptimeVal,
       "dhcpPLDUptimeLevelTable": dhcpPLDUptimeLevelTable,
       "dhcpPLDUptimeLevelEntry": dhcpPLDUptimeLevelEntry,
       "dhcpPLDUptimeLevelName": dhcpPLDUptimeLevelName,
       "dhcpPLDUptimeLevelVal": dhcpPLDUptimeLevelVal,
       "dhcpPLDOperations": dhcpPLDOperations,
       "dhcpPLDOperationsVal": dhcpPLDOperationsVal,
       "dhcpPLDOperationsMom": dhcpPLDOperationsMom,
       "dhcpPLDOperationsMax": dhcpPLDOperationsMax,
       "dhcpPLDOperationsLevelTable": dhcpPLDOperationsLevelTable,
       "dhcpPLDOperationsLevelEntry": dhcpPLDOperationsLevelEntry,
       "dhcpPLDOperationsLevelName": dhcpPLDOperationsLevelName,
       "dhcpPLDOperationsLevelVal": dhcpPLDOperationsLevelVal,
       "dhcpPLDOperationsLevelMom": dhcpPLDOperationsLevelMom,
       "dhcpPLDOperationsLevelMax": dhcpPLDOperationsLevelMax,
       "dhcpPackets": dhcpPackets,
       "dhcpPacketsVal": dhcpPacketsVal,
       "dhcpPacketsMom": dhcpPacketsMom,
       "dhcpPacketsMax": dhcpPacketsMax,
       "dhcpPacketsLevelTable": dhcpPacketsLevelTable,
       "dhcpPacketsLevelEntry": dhcpPacketsLevelEntry,
       "dhcpPacketsLevelName": dhcpPacketsLevelName,
       "dhcpPacketsLevelVal": dhcpPacketsLevelVal,
       "dhcpPacketsLevelMom": dhcpPacketsLevelMom,
       "dhcpPacketsLevelMax": dhcpPacketsLevelMax,
       "dhcpUnparsablePackets": dhcpUnparsablePackets,
       "dhcpUnparsablePacketsVal": dhcpUnparsablePacketsVal,
       "dhcpUnparsablePacketsMom": dhcpUnparsablePacketsMom,
       "dhcpUnparsablePacketsMax": dhcpUnparsablePacketsMax,
       "dhcpUnparsablePacketsLevelTable": dhcpUnparsablePacketsLevelTable,
       "dhcpUnparsablePacketsLevelEntry": dhcpUnparsablePacketsLevelEntry,
       "dhcpUnparsablePacketsLevelName": dhcpUnparsablePacketsLevelName,
       "dhcpUnparsablePacketsLevelVal": dhcpUnparsablePacketsLevelVal,
       "dhcpUnparsablePacketsLevelMom": dhcpUnparsablePacketsLevelMom,
       "dhcpUnparsablePacketsLevelMax": dhcpUnparsablePacketsLevelMax,
       "dhcpPacketsReq": dhcpPacketsReq,
       "dhcpPacketsReqVal": dhcpPacketsReqVal,
       "dhcpPacketsReqMom": dhcpPacketsReqMom,
       "dhcpPacketsReqMax": dhcpPacketsReqMax,
       "dhcpPacketsReqLevelTable": dhcpPacketsReqLevelTable,
       "dhcpPacketsReqLevelEntry": dhcpPacketsReqLevelEntry,
       "dhcpPacketsReqLevelName": dhcpPacketsReqLevelName,
       "dhcpPacketsReqLevelVal": dhcpPacketsReqLevelVal,
       "dhcpPacketsReqLevelMom": dhcpPacketsReqLevelMom,
       "dhcpPacketsReqLevelMax": dhcpPacketsReqLevelMax,
       "dhcpPacketsAck": dhcpPacketsAck,
       "dhcpPacketsAckVal": dhcpPacketsAckVal,
       "dhcpPacketsAckMom": dhcpPacketsAckMom,
       "dhcpPacketsAckMax": dhcpPacketsAckMax,
       "dhcpPacketsAckLevelTable": dhcpPacketsAckLevelTable,
       "dhcpPacketsAckLevelEntry": dhcpPacketsAckLevelEntry,
       "dhcpPacketsAckLevelName": dhcpPacketsAckLevelName,
       "dhcpPacketsAckLevelVal": dhcpPacketsAckLevelVal,
       "dhcpPacketsAckLevelMom": dhcpPacketsAckLevelMom,
       "dhcpPacketsAckLevelMax": dhcpPacketsAckLevelMax,
       "dhcpPacketsIgnored": dhcpPacketsIgnored,
       "dhcpPacketsIgnoredVal": dhcpPacketsIgnoredVal,
       "dhcpPacketsIgnoredMom": dhcpPacketsIgnoredMom,
       "dhcpPacketsIgnoredMax": dhcpPacketsIgnoredMax,
       "dhcpPacketsIgnoredLevelTable": dhcpPacketsIgnoredLevelTable,
       "dhcpPacketsIgnoredLevelEntry": dhcpPacketsIgnoredLevelEntry,
       "dhcpPacketsIgnoredLevelName": dhcpPacketsIgnoredLevelName,
       "dhcpPacketsIgnoredLevelVal": dhcpPacketsIgnoredLevelVal,
       "dhcpPacketsIgnoredLevelMom": dhcpPacketsIgnoredLevelMom,
       "dhcpPacketsIgnoredLevelMax": dhcpPacketsIgnoredLevelMax,
       "dhcpEntryIndex": dhcpEntryIndex}
)
