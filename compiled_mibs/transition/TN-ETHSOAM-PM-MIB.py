# SNMP MIB module (TN-ETHSOAM-PM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\transition\TN-ETHSOAM-PM-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 12:31:30 2025
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

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

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
 RowStatus,
 TextualConvention,
 TimeInterval) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TimeInterval")

(tnEthSoaminstance,) = mibBuilder.importSymbols(
    "TN-ETHSOAM-MIB",
    "tnEthSoaminstance")

(tnEvcEceId,
 tnEvcIndex) = mibBuilder.importSymbols(
    "TN-EVC-MIB",
    "tnEvcEceId",
    "tnEvcIndex")

(tnProducts,) = mibBuilder.importSymbols(
    "TRANSITION-SMI",
    "tnProducts")


# MODULE-IDENTITY

tnEthSoamPmMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 143)
)
if mibBuilder.loadTexts:
    tnEthSoamPmMIB.setRevisions(
        ("2014-03-28 12:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_TnEthSoamPmNotifications_ObjectIdentity = ObjectIdentity
tnEthSoamPmNotifications = _TnEthSoamPmNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 143, 0)
)
_TnEthSoamPmCfgMIBObjects_ObjectIdentity = ObjectIdentity
tnEthSoamPmCfgMIBObjects = _TnEthSoamPmCfgMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 143, 1)
)
_TnEthSoamPmSessionCfgObjects_ObjectIdentity = ObjectIdentity
tnEthSoamPmSessionCfgObjects = _TnEthSoamPmSessionCfgObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 143, 1, 1)
)
_TnEthSoamPmSessionCfgTable_Object = MibTable
tnEthSoamPmSessionCfgTable = _TnEthSoamPmSessionCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 143, 1, 1, 1)
)
if mibBuilder.loadTexts:
    tnEthSoamPmSessionCfgTable.setStatus("current")
_TnEthSoamPmSessionCfgEntry_Object = MibTableRow
tnEthSoamPmSessionCfgEntry = _TnEthSoamPmSessionCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 143, 1, 1, 1, 1)
)
tnEthSoamPmSessionCfgEntry.setIndexNames(
    (0, "TN-ETHSOAM-PM-MIB", "tnEthSoamPmSessionCfgId"),
)
if mibBuilder.loadTexts:
    tnEthSoamPmSessionCfgEntry.setStatus("current")


class _TnEthSoamPmSessionCfgId_Type(Integer32):
    """Custom type tnEthSoamPmSessionCfgId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_TnEthSoamPmSessionCfgId_Type.__name__ = "Integer32"
_TnEthSoamPmSessionCfgId_Object = MibTableColumn
tnEthSoamPmSessionCfgId = _TnEthSoamPmSessionCfgId_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 143, 1, 1, 1, 1, 1),
    _TnEthSoamPmSessionCfgId_Type()
)
tnEthSoamPmSessionCfgId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnEthSoamPmSessionCfgId.setStatus("current")


class _TnEthSoamPmSessionCfgType_Type(Integer32):
    """Custom type tnEthSoamPmSessionCfgType based on Integer32"""
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
        *(("lossMeasurement", 1),
          ("delayMeasurement", 2),
          ("evc", 3),
          ("ece", 4),
          ("dmBinning", 5))
    )


_TnEthSoamPmSessionCfgType_Type.__name__ = "Integer32"
_TnEthSoamPmSessionCfgType_Object = MibTableColumn
tnEthSoamPmSessionCfgType = _TnEthSoamPmSessionCfgType_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 143, 1, 1, 1, 1, 2),
    _TnEthSoamPmSessionCfgType_Type()
)
tnEthSoamPmSessionCfgType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnEthSoamPmSessionCfgType.setStatus("current")


class _TnEthSoamPmSessionCfgSessionMode_Type(Integer32):
    """Custom type tnEthSoamPmSessionCfgSessionMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 1),
          ("disabled", 2))
    )


_TnEthSoamPmSessionCfgSessionMode_Type.__name__ = "Integer32"
_TnEthSoamPmSessionCfgSessionMode_Object = MibTableColumn
tnEthSoamPmSessionCfgSessionMode = _TnEthSoamPmSessionCfgSessionMode_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 143, 1, 1, 1, 1, 3),
    _TnEthSoamPmSessionCfgSessionMode_Type()
)
tnEthSoamPmSessionCfgSessionMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnEthSoamPmSessionCfgSessionMode.setStatus("current")


class _TnEthSoamPmSessionCfgStorageMode_Type(Integer32):
    """Custom type tnEthSoamPmSessionCfgStorageMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 1),
          ("disabled", 2))
    )


_TnEthSoamPmSessionCfgStorageMode_Type.__name__ = "Integer32"
_TnEthSoamPmSessionCfgStorageMode_Object = MibTableColumn
tnEthSoamPmSessionCfgStorageMode = _TnEthSoamPmSessionCfgStorageMode_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 143, 1, 1, 1, 1, 4),
    _TnEthSoamPmSessionCfgStorageMode_Type()
)
tnEthSoamPmSessionCfgStorageMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnEthSoamPmSessionCfgStorageMode.setStatus("current")
_TnEthSoamPmSessionCfgInterval_Type = Unsigned32
_TnEthSoamPmSessionCfgInterval_Object = MibTableColumn
tnEthSoamPmSessionCfgInterval = _TnEthSoamPmSessionCfgInterval_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 143, 1, 1, 1, 1, 5),
    _TnEthSoamPmSessionCfgInterval_Type()
)
tnEthSoamPmSessionCfgInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnEthSoamPmSessionCfgInterval.setStatus("current")
_TnEthSoamPmTransferCfgObjects_ObjectIdentity = ObjectIdentity
tnEthSoamPmTransferCfgObjects = _TnEthSoamPmTransferCfgObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 143, 1, 2)
)
_TnEthSoamPmTransferCfgTable_Object = MibTable
tnEthSoamPmTransferCfgTable = _TnEthSoamPmTransferCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 143, 1, 2, 1)
)
if mibBuilder.loadTexts:
    tnEthSoamPmTransferCfgTable.setStatus("current")
_TnEthSoamPmTransferCfgEntry_Object = MibTableRow
tnEthSoamPmTransferCfgEntry = _TnEthSoamPmTransferCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 143, 1, 2, 1, 1)
)
tnEthSoamPmTransferCfgEntry.setIndexNames(
    (0, "TN-ETHSOAM-PM-MIB", "tnEthSoamPmTransferCfgId"),
)
if mibBuilder.loadTexts:
    tnEthSoamPmTransferCfgEntry.setStatus("current")


class _TnEthSoamPmTransferCfgId_Type(Integer32):
    """Custom type tnEthSoamPmTransferCfgId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_TnEthSoamPmTransferCfgId_Type.__name__ = "Integer32"
_TnEthSoamPmTransferCfgId_Object = MibTableColumn
tnEthSoamPmTransferCfgId = _TnEthSoamPmTransferCfgId_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 143, 1, 2, 1, 1, 1),
    _TnEthSoamPmTransferCfgId_Type()
)
tnEthSoamPmTransferCfgId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnEthSoamPmTransferCfgId.setStatus("current")


class _TnEthSoamPmTransferCfgMode_Type(Integer32):
    """Custom type tnEthSoamPmTransferCfgMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 1),
          ("disabled", 2))
    )


_TnEthSoamPmTransferCfgMode_Type.__name__ = "Integer32"
_TnEthSoamPmTransferCfgMode_Object = MibTableColumn
tnEthSoamPmTransferCfgMode = _TnEthSoamPmTransferCfgMode_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 143, 1, 2, 1, 1, 2),
    _TnEthSoamPmTransferCfgMode_Type()
)
tnEthSoamPmTransferCfgMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnEthSoamPmTransferCfgMode.setStatus("current")


class _TnEthSoamPmTransferCfgSchedHrs_Type(Bits):
    """Custom type tnEthSoamPmTransferCfgSchedHrs based on Bits"""
    namedValues = NamedValues(
        *(("hrs00", 0),
          ("hrs01", 1),
          ("hrs02", 2),
          ("hrs03", 3),
          ("hrs04", 4),
          ("hrs05", 5),
          ("hrs06", 6),
          ("hrs07", 7),
          ("hrs08", 8),
          ("hrs09", 9),
          ("hrs10", 10),
          ("hrs11", 11),
          ("hrs12", 12),
          ("hrs13", 13),
          ("hrs14", 14),
          ("hrs15", 15),
          ("hrs16", 16),
          ("hrs17", 17),
          ("hrs18", 18),
          ("hrs19", 19),
          ("hrs20", 20),
          ("hrs21", 21),
          ("hrs22", 22),
          ("hrs23", 23))
    )

_TnEthSoamPmTransferCfgSchedHrs_Type.__name__ = "Bits"
_TnEthSoamPmTransferCfgSchedHrs_Object = MibTableColumn
tnEthSoamPmTransferCfgSchedHrs = _TnEthSoamPmTransferCfgSchedHrs_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 143, 1, 2, 1, 1, 3),
    _TnEthSoamPmTransferCfgSchedHrs_Type()
)
tnEthSoamPmTransferCfgSchedHrs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnEthSoamPmTransferCfgSchedHrs.setStatus("current")


class _TnEthSoamPmTransferCfgSchedMins_Type(Bits):
    """Custom type tnEthSoamPmTransferCfgSchedMins based on Bits"""
    namedValues = NamedValues(
        *(("mins00", 0),
          ("mins15", 1),
          ("mins30", 2),
          ("mins45", 3))
    )

_TnEthSoamPmTransferCfgSchedMins_Type.__name__ = "Bits"
_TnEthSoamPmTransferCfgSchedMins_Object = MibTableColumn
tnEthSoamPmTransferCfgSchedMins = _TnEthSoamPmTransferCfgSchedMins_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 143, 1, 2, 1, 1, 4),
    _TnEthSoamPmTransferCfgSchedMins_Type()
)
tnEthSoamPmTransferCfgSchedMins.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnEthSoamPmTransferCfgSchedMins.setStatus("current")
_TnEthSoamPmTransferCfgSchedOffset_Type = Integer32
_TnEthSoamPmTransferCfgSchedOffset_Object = MibTableColumn
tnEthSoamPmTransferCfgSchedOffset = _TnEthSoamPmTransferCfgSchedOffset_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 143, 1, 2, 1, 1, 5),
    _TnEthSoamPmTransferCfgSchedOffset_Type()
)
tnEthSoamPmTransferCfgSchedOffset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnEthSoamPmTransferCfgSchedOffset.setStatus("current")
_TnEthSoamPmTransferCfgRandomOffset_Type = Integer32
_TnEthSoamPmTransferCfgRandomOffset_Object = MibTableColumn
tnEthSoamPmTransferCfgRandomOffset = _TnEthSoamPmTransferCfgRandomOffset_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 143, 1, 2, 1, 1, 6),
    _TnEthSoamPmTransferCfgRandomOffset_Type()
)
tnEthSoamPmTransferCfgRandomOffset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnEthSoamPmTransferCfgRandomOffset.setStatus("current")


class _TnEthSoamPmTransferCfgServerAddr_Type(OctetString):
    """Custom type tnEthSoamPmTransferCfgServerAddr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_TnEthSoamPmTransferCfgServerAddr_Type.__name__ = "OctetString"
_TnEthSoamPmTransferCfgServerAddr_Object = MibTableColumn
tnEthSoamPmTransferCfgServerAddr = _TnEthSoamPmTransferCfgServerAddr_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 143, 1, 2, 1, 1, 7),
    _TnEthSoamPmTransferCfgServerAddr_Type()
)
tnEthSoamPmTransferCfgServerAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnEthSoamPmTransferCfgServerAddr.setStatus("current")


class _TnEthSoamPmTransferCfgIntervalMode_Type(Integer32):
    """Custom type tnEthSoamPmTransferCfgIntervalMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("allAvailableIntervals", 1),
          ("newIntervalsSinceLastTransfer", 2),
          ("fixedNumberOfIntervals", 3))
    )


_TnEthSoamPmTransferCfgIntervalMode_Type.__name__ = "Integer32"
_TnEthSoamPmTransferCfgIntervalMode_Object = MibTableColumn
tnEthSoamPmTransferCfgIntervalMode = _TnEthSoamPmTransferCfgIntervalMode_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 143, 1, 2, 1, 1, 8),
    _TnEthSoamPmTransferCfgIntervalMode_Type()
)
tnEthSoamPmTransferCfgIntervalMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnEthSoamPmTransferCfgIntervalMode.setStatus("current")


class _TnEthSoamPmTransferCfgIntervalNum_Type(Integer32):
    """Custom type tnEthSoamPmTransferCfgIntervalNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 96),
    )


_TnEthSoamPmTransferCfgIntervalNum_Type.__name__ = "Integer32"
_TnEthSoamPmTransferCfgIntervalNum_Object = MibTableColumn
tnEthSoamPmTransferCfgIntervalNum = _TnEthSoamPmTransferCfgIntervalNum_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 143, 1, 2, 1, 1, 9),
    _TnEthSoamPmTransferCfgIntervalNum_Type()
)
tnEthSoamPmTransferCfgIntervalNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnEthSoamPmTransferCfgIntervalNum.setStatus("current")


class _TnEthSoamPmTransferCfgIncludeIncomplete_Type(Integer32):
    """Custom type tnEthSoamPmTransferCfgIncludeIncomplete based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 1),
          ("disabled", 2))
    )


_TnEthSoamPmTransferCfgIncludeIncomplete_Type.__name__ = "Integer32"
_TnEthSoamPmTransferCfgIncludeIncomplete_Object = MibTableColumn
tnEthSoamPmTransferCfgIncludeIncomplete = _TnEthSoamPmTransferCfgIncludeIncomplete_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 143, 1, 2, 1, 1, 10),
    _TnEthSoamPmTransferCfgIncludeIncomplete_Type()
)
tnEthSoamPmTransferCfgIncludeIncomplete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnEthSoamPmTransferCfgIncludeIncomplete.setStatus("current")
_TnEthSoamPmStatsMIBObjects_ObjectIdentity = ObjectIdentity
tnEthSoamPmStatsMIBObjects = _TnEthSoamPmStatsMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 143, 2)
)
_TnEthSoamPmLmStatsObjects_ObjectIdentity = ObjectIdentity
tnEthSoamPmLmStatsObjects = _TnEthSoamPmLmStatsObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 143, 2, 1)
)
_TnEthSoamPmLmHistoryStatsTable_Object = MibTable
tnEthSoamPmLmHistoryStatsTable = _TnEthSoamPmLmHistoryStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 143, 2, 1, 1)
)
if mibBuilder.loadTexts:
    tnEthSoamPmLmHistoryStatsTable.setStatus("current")
_TnEthSoamPmLmHistoryStatsEntry_Object = MibTableRow
tnEthSoamPmLmHistoryStatsEntry = _TnEthSoamPmLmHistoryStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 143, 2, 1, 1, 1)
)
tnEthSoamPmLmHistoryStatsEntry.setIndexNames(
    (0, "TN-ETHSOAM-PM-MIB", "tnEthSoamPmLmHistoryStatsIndex"),
    (0, "TN-ETHSOAM-MIB", "tnEthSoaminstance"),
)
if mibBuilder.loadTexts:
    tnEthSoamPmLmHistoryStatsEntry.setStatus("current")


class _TnEthSoamPmLmHistoryStatsIndex_Type(Unsigned32):
    """Custom type tnEthSoamPmLmHistoryStatsIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_TnEthSoamPmLmHistoryStatsIndex_Type.__name__ = "Unsigned32"
_TnEthSoamPmLmHistoryStatsIndex_Object = MibTableColumn
tnEthSoamPmLmHistoryStatsIndex = _TnEthSoamPmLmHistoryStatsIndex_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 143, 2, 1, 1, 1, 1),
    _TnEthSoamPmLmHistoryStatsIndex_Type()
)
tnEthSoamPmLmHistoryStatsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnEthSoamPmLmHistoryStatsIndex.setStatus("current")
_TnEthSoamPmLmHistoryStatsEndTime_Type = DateAndTime
_TnEthSoamPmLmHistoryStatsEndTime_Object = MibTableColumn
tnEthSoamPmLmHistoryStatsEndTime = _TnEthSoamPmLmHistoryStatsEndTime_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 143, 2, 1, 1, 1, 2),
    _TnEthSoamPmLmHistoryStatsEndTime_Type()
)
tnEthSoamPmLmHistoryStatsEndTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnEthSoamPmLmHistoryStatsEndTime.setStatus("current")
_TnEthSoamPmLmHistoryStatsElapsedTime_Type = TimeInterval
_TnEthSoamPmLmHistoryStatsElapsedTime_Object = MibTableColumn
tnEthSoamPmLmHistoryStatsElapsedTime = _TnEthSoamPmLmHistoryStatsElapsedTime_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 143, 2, 1, 1, 1, 3),
    _TnEthSoamPmLmHistoryStatsElapsedTime_Type()
)
tnEthSoamPmLmHistoryStatsElapsedTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnEthSoamPmLmHistoryStatsElapsedTime.setStatus("current")
_TnEthSoamPmLmHistoryStatsTxCount_Type = Counter64
_TnEthSoamPmLmHistoryStatsTxCount_Object = MibTableColumn
tnEthSoamPmLmHistoryStatsTxCount = _TnEthSoamPmLmHistoryStatsTxCount_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 143, 2, 1, 1, 1, 4),
    _TnEthSoamPmLmHistoryStatsTxCount_Type()
)
tnEthSoamPmLmHistoryStatsTxCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnEthSoamPmLmHistoryStatsTxCount.setStatus("current")
_TnEthSoamPmLmHistoryStatsRxCount_Type = Counter64
_TnEthSoamPmLmHistoryStatsRxCount_Object = MibTableColumn
tnEthSoamPmLmHistoryStatsRxCount = _TnEthSoamPmLmHistoryStatsRxCount_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 143, 2, 1, 1, 1, 5),
    _TnEthSoamPmLmHistoryStatsRxCount_Type()
)
tnEthSoamPmLmHistoryStatsRxCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnEthSoamPmLmHistoryStatsRxCount.setStatus("current")
_TnEthSoamPmLmHistoryStatsNELossCount_Type = Counter64
_TnEthSoamPmLmHistoryStatsNELossCount_Object = MibTableColumn
tnEthSoamPmLmHistoryStatsNELossCount = _TnEthSoamPmLmHistoryStatsNELossCount_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 143, 2, 1, 1, 1, 6),
    _TnEthSoamPmLmHistoryStatsNELossCount_Type()
)
tnEthSoamPmLmHistoryStatsNELossCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnEthSoamPmLmHistoryStatsNELossCount.setStatus("current")
_TnEthSoamPmLmHistoryStatsFELossCount_Type = Counter64
_TnEthSoamPmLmHistoryStatsFELossCount_Object = MibTableColumn
tnEthSoamPmLmHistoryStatsFELossCount = _TnEthSoamPmLmHistoryStatsFELossCount_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 143, 2, 1, 1, 1, 7),
    _TnEthSoamPmLmHistoryStatsFELossCount_Type()
)
tnEthSoamPmLmHistoryStatsFELossCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnEthSoamPmLmHistoryStatsFELossCount.setStatus("current")


class _TnEthSoamPmLmHistoryStatsNEAvgFlr_Type(Unsigned32):
    """Custom type tnEthSoamPmLmHistoryStatsNEAvgFlr based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100000),
    )


_TnEthSoamPmLmHistoryStatsNEAvgFlr_Type.__name__ = "Unsigned32"
_TnEthSoamPmLmHistoryStatsNEAvgFlr_Object = MibTableColumn
tnEthSoamPmLmHistoryStatsNEAvgFlr = _TnEthSoamPmLmHistoryStatsNEAvgFlr_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 143, 2, 1, 1, 1, 8),
    _TnEthSoamPmLmHistoryStatsNEAvgFlr_Type()
)
tnEthSoamPmLmHistoryStatsNEAvgFlr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnEthSoamPmLmHistoryStatsNEAvgFlr.setStatus("current")
if mibBuilder.loadTexts:
    tnEthSoamPmLmHistoryStatsNEAvgFlr.setUnits("milli-percent")


class _TnEthSoamPmLmHistoryStatsFEAvgFlr_Type(Unsigned32):
    """Custom type tnEthSoamPmLmHistoryStatsFEAvgFlr based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100000),
    )


_TnEthSoamPmLmHistoryStatsFEAvgFlr_Type.__name__ = "Unsigned32"
_TnEthSoamPmLmHistoryStatsFEAvgFlr_Object = MibTableColumn
tnEthSoamPmLmHistoryStatsFEAvgFlr = _TnEthSoamPmLmHistoryStatsFEAvgFlr_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 143, 2, 1, 1, 1, 9),
    _TnEthSoamPmLmHistoryStatsFEAvgFlr_Type()
)
tnEthSoamPmLmHistoryStatsFEAvgFlr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnEthSoamPmLmHistoryStatsFEAvgFlr.setStatus("current")
if mibBuilder.loadTexts:
    tnEthSoamPmLmHistoryStatsFEAvgFlr.setUnits("milli-percent")
_TnEthSoamPmDmStatsObjects_ObjectIdentity = ObjectIdentity
tnEthSoamPmDmStatsObjects = _TnEthSoamPmDmStatsObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 143, 2, 2)
)
_TnEthSoamPmDmHistoryStatsTable_Object = MibTable
tnEthSoamPmDmHistoryStatsTable = _TnEthSoamPmDmHistoryStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 143, 2, 2, 1)
)
if mibBuilder.loadTexts:
    tnEthSoamPmDmHistoryStatsTable.setStatus("current")
_TnEthSoamPmDmHistoryStatsEntry_Object = MibTableRow
tnEthSoamPmDmHistoryStatsEntry = _TnEthSoamPmDmHistoryStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 143, 2, 2, 1, 1)
)
tnEthSoamPmDmHistoryStatsEntry.setIndexNames(
    (0, "TN-ETHSOAM-PM-MIB", "tnEthSoamPmDmHistoryStatsIndex"),
    (0, "TN-ETHSOAM-MIB", "tnEthSoaminstance"),
)
if mibBuilder.loadTexts:
    tnEthSoamPmDmHistoryStatsEntry.setStatus("current")


class _TnEthSoamPmDmHistoryStatsIndex_Type(Unsigned32):
    """Custom type tnEthSoamPmDmHistoryStatsIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_TnEthSoamPmDmHistoryStatsIndex_Type.__name__ = "Unsigned32"
_TnEthSoamPmDmHistoryStatsIndex_Object = MibTableColumn
tnEthSoamPmDmHistoryStatsIndex = _TnEthSoamPmDmHistoryStatsIndex_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 143, 2, 2, 1, 1, 1),
    _TnEthSoamPmDmHistoryStatsIndex_Type()
)
tnEthSoamPmDmHistoryStatsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnEthSoamPmDmHistoryStatsIndex.setStatus("current")
_TnEthSoamPmDmHistoryStatsEndTime_Type = DateAndTime
_TnEthSoamPmDmHistoryStatsEndTime_Object = MibTableColumn
tnEthSoamPmDmHistoryStatsEndTime = _TnEthSoamPmDmHistoryStatsEndTime_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 143, 2, 2, 1, 1, 2),
    _TnEthSoamPmDmHistoryStatsEndTime_Type()
)
tnEthSoamPmDmHistoryStatsEndTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnEthSoamPmDmHistoryStatsEndTime.setStatus("current")
_TnEthSoamPmDmHistoryStatsElapsedTime_Type = TimeInterval
_TnEthSoamPmDmHistoryStatsElapsedTime_Object = MibTableColumn
tnEthSoamPmDmHistoryStatsElapsedTime = _TnEthSoamPmDmHistoryStatsElapsedTime_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 143, 2, 2, 1, 1, 3),
    _TnEthSoamPmDmHistoryStatsElapsedTime_Type()
)
tnEthSoamPmDmHistoryStatsElapsedTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnEthSoamPmDmHistoryStatsElapsedTime.setStatus("current")
_TnEthSoamPmDmHistoryStatsTxCount_Type = Counter64
_TnEthSoamPmDmHistoryStatsTxCount_Object = MibTableColumn
tnEthSoamPmDmHistoryStatsTxCount = _TnEthSoamPmDmHistoryStatsTxCount_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 143, 2, 2, 1, 1, 4),
    _TnEthSoamPmDmHistoryStatsTxCount_Type()
)
tnEthSoamPmDmHistoryStatsTxCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnEthSoamPmDmHistoryStatsTxCount.setStatus("current")
_TnEthSoamPmDmHistoryStatsRxCount_Type = Counter64
_TnEthSoamPmDmHistoryStatsRxCount_Object = MibTableColumn
tnEthSoamPmDmHistoryStatsRxCount = _TnEthSoamPmDmHistoryStatsRxCount_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 143, 2, 2, 1, 1, 5),
    _TnEthSoamPmDmHistoryStatsRxCount_Type()
)
tnEthSoamPmDmHistoryStatsRxCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnEthSoamPmDmHistoryStatsRxCount.setStatus("current")
_TnEthSoamPmDmHistoryStatsFNAvgFrameDelay_Type = Unsigned32
_TnEthSoamPmDmHistoryStatsFNAvgFrameDelay_Object = MibTableColumn
tnEthSoamPmDmHistoryStatsFNAvgFrameDelay = _TnEthSoamPmDmHistoryStatsFNAvgFrameDelay_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 143, 2, 2, 1, 1, 6),
    _TnEthSoamPmDmHistoryStatsFNAvgFrameDelay_Type()
)
tnEthSoamPmDmHistoryStatsFNAvgFrameDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnEthSoamPmDmHistoryStatsFNAvgFrameDelay.setStatus("current")
_TnEthSoamPmDmHistoryStatsFNAvgFrameDV_Type = Unsigned32
_TnEthSoamPmDmHistoryStatsFNAvgFrameDV_Object = MibTableColumn
tnEthSoamPmDmHistoryStatsFNAvgFrameDV = _TnEthSoamPmDmHistoryStatsFNAvgFrameDV_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 143, 2, 2, 1, 1, 7),
    _TnEthSoamPmDmHistoryStatsFNAvgFrameDV_Type()
)
tnEthSoamPmDmHistoryStatsFNAvgFrameDV.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnEthSoamPmDmHistoryStatsFNAvgFrameDV.setStatus("current")
_TnEthSoamPmDmHistoryStatsFNMinFrameDelay_Type = Unsigned32
_TnEthSoamPmDmHistoryStatsFNMinFrameDelay_Object = MibTableColumn
tnEthSoamPmDmHistoryStatsFNMinFrameDelay = _TnEthSoamPmDmHistoryStatsFNMinFrameDelay_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 143, 2, 2, 1, 1, 8),
    _TnEthSoamPmDmHistoryStatsFNMinFrameDelay_Type()
)
tnEthSoamPmDmHistoryStatsFNMinFrameDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnEthSoamPmDmHistoryStatsFNMinFrameDelay.setStatus("current")
_TnEthSoamPmDmHistoryStatsFNMaxFrameDelay_Type = Unsigned32
_TnEthSoamPmDmHistoryStatsFNMaxFrameDelay_Object = MibTableColumn
tnEthSoamPmDmHistoryStatsFNMaxFrameDelay = _TnEthSoamPmDmHistoryStatsFNMaxFrameDelay_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 143, 2, 2, 1, 1, 9),
    _TnEthSoamPmDmHistoryStatsFNMaxFrameDelay_Type()
)
tnEthSoamPmDmHistoryStatsFNMaxFrameDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnEthSoamPmDmHistoryStatsFNMaxFrameDelay.setStatus("current")
_TnEthSoamPmDmHistoryStatsNFAvgFrameDelay_Type = Unsigned32
_TnEthSoamPmDmHistoryStatsNFAvgFrameDelay_Object = MibTableColumn
tnEthSoamPmDmHistoryStatsNFAvgFrameDelay = _TnEthSoamPmDmHistoryStatsNFAvgFrameDelay_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 143, 2, 2, 1, 1, 10),
    _TnEthSoamPmDmHistoryStatsNFAvgFrameDelay_Type()
)
tnEthSoamPmDmHistoryStatsNFAvgFrameDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnEthSoamPmDmHistoryStatsNFAvgFrameDelay.setStatus("current")
_TnEthSoamPmDmHistoryStatsNFAvgFrameDV_Type = Unsigned32
_TnEthSoamPmDmHistoryStatsNFAvgFrameDV_Object = MibTableColumn
tnEthSoamPmDmHistoryStatsNFAvgFrameDV = _TnEthSoamPmDmHistoryStatsNFAvgFrameDV_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 143, 2, 2, 1, 1, 11),
    _TnEthSoamPmDmHistoryStatsNFAvgFrameDV_Type()
)
tnEthSoamPmDmHistoryStatsNFAvgFrameDV.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnEthSoamPmDmHistoryStatsNFAvgFrameDV.setStatus("current")
_TnEthSoamPmDmHistoryStatsNFMinFrameDelay_Type = Unsigned32
_TnEthSoamPmDmHistoryStatsNFMinFrameDelay_Object = MibTableColumn
tnEthSoamPmDmHistoryStatsNFMinFrameDelay = _TnEthSoamPmDmHistoryStatsNFMinFrameDelay_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 143, 2, 2, 1, 1, 12),
    _TnEthSoamPmDmHistoryStatsNFMinFrameDelay_Type()
)
tnEthSoamPmDmHistoryStatsNFMinFrameDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnEthSoamPmDmHistoryStatsNFMinFrameDelay.setStatus("current")
_TnEthSoamPmDmHistoryStatsNFMaxFrameDelay_Type = Unsigned32
_TnEthSoamPmDmHistoryStatsNFMaxFrameDelay_Object = MibTableColumn
tnEthSoamPmDmHistoryStatsNFMaxFrameDelay = _TnEthSoamPmDmHistoryStatsNFMaxFrameDelay_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 143, 2, 2, 1, 1, 13),
    _TnEthSoamPmDmHistoryStatsNFMaxFrameDelay_Type()
)
tnEthSoamPmDmHistoryStatsNFMaxFrameDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnEthSoamPmDmHistoryStatsNFMaxFrameDelay.setStatus("current")
_TnEthSoamPmDmHistoryStatsTwoWayAvgFrameDelay_Type = Unsigned32
_TnEthSoamPmDmHistoryStatsTwoWayAvgFrameDelay_Object = MibTableColumn
tnEthSoamPmDmHistoryStatsTwoWayAvgFrameDelay = _TnEthSoamPmDmHistoryStatsTwoWayAvgFrameDelay_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 143, 2, 2, 1, 1, 14),
    _TnEthSoamPmDmHistoryStatsTwoWayAvgFrameDelay_Type()
)
tnEthSoamPmDmHistoryStatsTwoWayAvgFrameDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnEthSoamPmDmHistoryStatsTwoWayAvgFrameDelay.setStatus("current")
_TnEthSoamPmDmHistoryStatsTwoWayAvgFrameDV_Type = Unsigned32
_TnEthSoamPmDmHistoryStatsTwoWayAvgFrameDV_Object = MibTableColumn
tnEthSoamPmDmHistoryStatsTwoWayAvgFrameDV = _TnEthSoamPmDmHistoryStatsTwoWayAvgFrameDV_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 143, 2, 2, 1, 1, 15),
    _TnEthSoamPmDmHistoryStatsTwoWayAvgFrameDV_Type()
)
tnEthSoamPmDmHistoryStatsTwoWayAvgFrameDV.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnEthSoamPmDmHistoryStatsTwoWayAvgFrameDV.setStatus("current")
_TnEthSoamPmDmHistoryStatsTwoWayMinFrameDelay_Type = Unsigned32
_TnEthSoamPmDmHistoryStatsTwoWayMinFrameDelay_Object = MibTableColumn
tnEthSoamPmDmHistoryStatsTwoWayMinFrameDelay = _TnEthSoamPmDmHistoryStatsTwoWayMinFrameDelay_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 143, 2, 2, 1, 1, 16),
    _TnEthSoamPmDmHistoryStatsTwoWayMinFrameDelay_Type()
)
tnEthSoamPmDmHistoryStatsTwoWayMinFrameDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnEthSoamPmDmHistoryStatsTwoWayMinFrameDelay.setStatus("current")
_TnEthSoamPmDmHistoryStatsTwoWayMaxFrameDelay_Type = Unsigned32
_TnEthSoamPmDmHistoryStatsTwoWayMaxFrameDelay_Object = MibTableColumn
tnEthSoamPmDmHistoryStatsTwoWayMaxFrameDelay = _TnEthSoamPmDmHistoryStatsTwoWayMaxFrameDelay_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 143, 2, 2, 1, 1, 17),
    _TnEthSoamPmDmHistoryStatsTwoWayMaxFrameDelay_Type()
)
tnEthSoamPmDmHistoryStatsTwoWayMaxFrameDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnEthSoamPmDmHistoryStatsTwoWayMaxFrameDelay.setStatus("current")
_TnEthSoamPmEvcStatsObjects_ObjectIdentity = ObjectIdentity
tnEthSoamPmEvcStatsObjects = _TnEthSoamPmEvcStatsObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 143, 2, 3)
)
_TnEthSoamPmEvcHistoryStatsTable_Object = MibTable
tnEthSoamPmEvcHistoryStatsTable = _TnEthSoamPmEvcHistoryStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 143, 2, 3, 1)
)
if mibBuilder.loadTexts:
    tnEthSoamPmEvcHistoryStatsTable.setStatus("current")
_TnEthSoamPmEvcHistoryStatsEntry_Object = MibTableRow
tnEthSoamPmEvcHistoryStatsEntry = _TnEthSoamPmEvcHistoryStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 143, 2, 3, 1, 1)
)
tnEthSoamPmEvcHistoryStatsEntry.setIndexNames(
    (0, "TN-ETHSOAM-PM-MIB", "tnEthSoamPmEvcHistoryStatsIndex"),
    (0, "TN-EVC-MIB", "tnEvcIndex"),
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    tnEthSoamPmEvcHistoryStatsEntry.setStatus("current")


class _TnEthSoamPmEvcHistoryStatsIndex_Type(Unsigned32):
    """Custom type tnEthSoamPmEvcHistoryStatsIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_TnEthSoamPmEvcHistoryStatsIndex_Type.__name__ = "Unsigned32"
_TnEthSoamPmEvcHistoryStatsIndex_Object = MibTableColumn
tnEthSoamPmEvcHistoryStatsIndex = _TnEthSoamPmEvcHistoryStatsIndex_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 143, 2, 3, 1, 1, 1),
    _TnEthSoamPmEvcHistoryStatsIndex_Type()
)
tnEthSoamPmEvcHistoryStatsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnEthSoamPmEvcHistoryStatsIndex.setStatus("current")
_TnEthSoamPmEvcHistoryStatsEndTime_Type = DateAndTime
_TnEthSoamPmEvcHistoryStatsEndTime_Object = MibTableColumn
tnEthSoamPmEvcHistoryStatsEndTime = _TnEthSoamPmEvcHistoryStatsEndTime_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 143, 2, 3, 1, 1, 2),
    _TnEthSoamPmEvcHistoryStatsEndTime_Type()
)
tnEthSoamPmEvcHistoryStatsEndTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnEthSoamPmEvcHistoryStatsEndTime.setStatus("current")
_TnEthSoamPmEvcHistoryStatsElapsedTime_Type = TimeInterval
_TnEthSoamPmEvcHistoryStatsElapsedTime_Object = MibTableColumn
tnEthSoamPmEvcHistoryStatsElapsedTime = _TnEthSoamPmEvcHistoryStatsElapsedTime_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 143, 2, 3, 1, 1, 3),
    _TnEthSoamPmEvcHistoryStatsElapsedTime_Type()
)
tnEthSoamPmEvcHistoryStatsElapsedTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnEthSoamPmEvcHistoryStatsElapsedTime.setStatus("current")
_TnEthSoamPmEvcHistoryStatsGreenFramesTx_Type = Counter64
_TnEthSoamPmEvcHistoryStatsGreenFramesTx_Object = MibTableColumn
tnEthSoamPmEvcHistoryStatsGreenFramesTx = _TnEthSoamPmEvcHistoryStatsGreenFramesTx_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 143, 2, 3, 1, 1, 4),
    _TnEthSoamPmEvcHistoryStatsGreenFramesTx_Type()
)
tnEthSoamPmEvcHistoryStatsGreenFramesTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnEthSoamPmEvcHistoryStatsGreenFramesTx.setStatus("current")
_TnEthSoamPmEvcHistoryStatsGreenFramesRx_Type = Counter64
_TnEthSoamPmEvcHistoryStatsGreenFramesRx_Object = MibTableColumn
tnEthSoamPmEvcHistoryStatsGreenFramesRx = _TnEthSoamPmEvcHistoryStatsGreenFramesRx_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 143, 2, 3, 1, 1, 5),
    _TnEthSoamPmEvcHistoryStatsGreenFramesRx_Type()
)
tnEthSoamPmEvcHistoryStatsGreenFramesRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnEthSoamPmEvcHistoryStatsGreenFramesRx.setStatus("current")
_TnEthSoamPmEvcHistoryStatsGreenBytesTx_Type = Counter64
_TnEthSoamPmEvcHistoryStatsGreenBytesTx_Object = MibTableColumn
tnEthSoamPmEvcHistoryStatsGreenBytesTx = _TnEthSoamPmEvcHistoryStatsGreenBytesTx_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 143, 2, 3, 1, 1, 6),
    _TnEthSoamPmEvcHistoryStatsGreenBytesTx_Type()
)
tnEthSoamPmEvcHistoryStatsGreenBytesTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnEthSoamPmEvcHistoryStatsGreenBytesTx.setStatus("current")
_TnEthSoamPmEvcHistoryStatsGreenBytesRx_Type = Counter64
_TnEthSoamPmEvcHistoryStatsGreenBytesRx_Object = MibTableColumn
tnEthSoamPmEvcHistoryStatsGreenBytesRx = _TnEthSoamPmEvcHistoryStatsGreenBytesRx_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 143, 2, 3, 1, 1, 7),
    _TnEthSoamPmEvcHistoryStatsGreenBytesRx_Type()
)
tnEthSoamPmEvcHistoryStatsGreenBytesRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnEthSoamPmEvcHistoryStatsGreenBytesRx.setStatus("current")
_TnEthSoamPmEvcHistoryStatsYellowFramesTx_Type = Counter64
_TnEthSoamPmEvcHistoryStatsYellowFramesTx_Object = MibTableColumn
tnEthSoamPmEvcHistoryStatsYellowFramesTx = _TnEthSoamPmEvcHistoryStatsYellowFramesTx_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 143, 2, 3, 1, 1, 8),
    _TnEthSoamPmEvcHistoryStatsYellowFramesTx_Type()
)
tnEthSoamPmEvcHistoryStatsYellowFramesTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnEthSoamPmEvcHistoryStatsYellowFramesTx.setStatus("current")
_TnEthSoamPmEvcHistoryStatsYellowFramesRx_Type = Counter64
_TnEthSoamPmEvcHistoryStatsYellowFramesRx_Object = MibTableColumn
tnEthSoamPmEvcHistoryStatsYellowFramesRx = _TnEthSoamPmEvcHistoryStatsYellowFramesRx_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 143, 2, 3, 1, 1, 9),
    _TnEthSoamPmEvcHistoryStatsYellowFramesRx_Type()
)
tnEthSoamPmEvcHistoryStatsYellowFramesRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnEthSoamPmEvcHistoryStatsYellowFramesRx.setStatus("current")
_TnEthSoamPmEvcHistoryStatsYellowBytesTx_Type = Counter64
_TnEthSoamPmEvcHistoryStatsYellowBytesTx_Object = MibTableColumn
tnEthSoamPmEvcHistoryStatsYellowBytesTx = _TnEthSoamPmEvcHistoryStatsYellowBytesTx_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 143, 2, 3, 1, 1, 10),
    _TnEthSoamPmEvcHistoryStatsYellowBytesTx_Type()
)
tnEthSoamPmEvcHistoryStatsYellowBytesTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnEthSoamPmEvcHistoryStatsYellowBytesTx.setStatus("current")
_TnEthSoamPmEvcHistoryStatsYellowBytesRx_Type = Counter64
_TnEthSoamPmEvcHistoryStatsYellowBytesRx_Object = MibTableColumn
tnEthSoamPmEvcHistoryStatsYellowBytesRx = _TnEthSoamPmEvcHistoryStatsYellowBytesRx_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 143, 2, 3, 1, 1, 11),
    _TnEthSoamPmEvcHistoryStatsYellowBytesRx_Type()
)
tnEthSoamPmEvcHistoryStatsYellowBytesRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnEthSoamPmEvcHistoryStatsYellowBytesRx.setStatus("current")
_TnEthSoamPmEvcHistoryStatsRedFramesRx_Type = Counter64
_TnEthSoamPmEvcHistoryStatsRedFramesRx_Object = MibTableColumn
tnEthSoamPmEvcHistoryStatsRedFramesRx = _TnEthSoamPmEvcHistoryStatsRedFramesRx_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 143, 2, 3, 1, 1, 12),
    _TnEthSoamPmEvcHistoryStatsRedFramesRx_Type()
)
tnEthSoamPmEvcHistoryStatsRedFramesRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnEthSoamPmEvcHistoryStatsRedFramesRx.setStatus("current")
_TnEthSoamPmEvcHistoryStatsRedBytesRx_Type = Counter64
_TnEthSoamPmEvcHistoryStatsRedBytesRx_Object = MibTableColumn
tnEthSoamPmEvcHistoryStatsRedBytesRx = _TnEthSoamPmEvcHistoryStatsRedBytesRx_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 143, 2, 3, 1, 1, 13),
    _TnEthSoamPmEvcHistoryStatsRedBytesRx_Type()
)
tnEthSoamPmEvcHistoryStatsRedBytesRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnEthSoamPmEvcHistoryStatsRedBytesRx.setStatus("current")
_TnEthSoamPmEvcHistoryStatsDiscardFramesTx_Type = Counter64
_TnEthSoamPmEvcHistoryStatsDiscardFramesTx_Object = MibTableColumn
tnEthSoamPmEvcHistoryStatsDiscardFramesTx = _TnEthSoamPmEvcHistoryStatsDiscardFramesTx_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 143, 2, 3, 1, 1, 14),
    _TnEthSoamPmEvcHistoryStatsDiscardFramesTx_Type()
)
tnEthSoamPmEvcHistoryStatsDiscardFramesTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnEthSoamPmEvcHistoryStatsDiscardFramesTx.setStatus("current")
_TnEthSoamPmEvcHistoryStatsDiscardFramesRx_Type = Counter64
_TnEthSoamPmEvcHistoryStatsDiscardFramesRx_Object = MibTableColumn
tnEthSoamPmEvcHistoryStatsDiscardFramesRx = _TnEthSoamPmEvcHistoryStatsDiscardFramesRx_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 143, 2, 3, 1, 1, 15),
    _TnEthSoamPmEvcHistoryStatsDiscardFramesRx_Type()
)
tnEthSoamPmEvcHistoryStatsDiscardFramesRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnEthSoamPmEvcHistoryStatsDiscardFramesRx.setStatus("current")
_TnEthSoamPmEvcHistoryStatsDiscardBytesTx_Type = Counter64
_TnEthSoamPmEvcHistoryStatsDiscardBytesTx_Object = MibTableColumn
tnEthSoamPmEvcHistoryStatsDiscardBytesTx = _TnEthSoamPmEvcHistoryStatsDiscardBytesTx_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 143, 2, 3, 1, 1, 16),
    _TnEthSoamPmEvcHistoryStatsDiscardBytesTx_Type()
)
tnEthSoamPmEvcHistoryStatsDiscardBytesTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnEthSoamPmEvcHistoryStatsDiscardBytesTx.setStatus("current")
_TnEthSoamPmEvcHistoryStatsDiscardBytesRx_Type = Counter64
_TnEthSoamPmEvcHistoryStatsDiscardBytesRx_Object = MibTableColumn
tnEthSoamPmEvcHistoryStatsDiscardBytesRx = _TnEthSoamPmEvcHistoryStatsDiscardBytesRx_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 143, 2, 3, 1, 1, 17),
    _TnEthSoamPmEvcHistoryStatsDiscardBytesRx_Type()
)
tnEthSoamPmEvcHistoryStatsDiscardBytesRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnEthSoamPmEvcHistoryStatsDiscardBytesRx.setStatus("current")
_TnEthSoamPmEceStatsObjects_ObjectIdentity = ObjectIdentity
tnEthSoamPmEceStatsObjects = _TnEthSoamPmEceStatsObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 143, 2, 4)
)
_TnEthSoamPmEceHistoryStatsTable_Object = MibTable
tnEthSoamPmEceHistoryStatsTable = _TnEthSoamPmEceHistoryStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 143, 2, 4, 1)
)
if mibBuilder.loadTexts:
    tnEthSoamPmEceHistoryStatsTable.setStatus("current")
_TnEthSoamPmEceHistoryStatsEntry_Object = MibTableRow
tnEthSoamPmEceHistoryStatsEntry = _TnEthSoamPmEceHistoryStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 143, 2, 4, 1, 1)
)
tnEthSoamPmEceHistoryStatsEntry.setIndexNames(
    (0, "TN-ETHSOAM-PM-MIB", "tnEthSoamPmEceHistoryStatsIndex"),
    (0, "TN-EVC-MIB", "tnEvcEceId"),
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    tnEthSoamPmEceHistoryStatsEntry.setStatus("current")


class _TnEthSoamPmEceHistoryStatsIndex_Type(Unsigned32):
    """Custom type tnEthSoamPmEceHistoryStatsIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_TnEthSoamPmEceHistoryStatsIndex_Type.__name__ = "Unsigned32"
_TnEthSoamPmEceHistoryStatsIndex_Object = MibTableColumn
tnEthSoamPmEceHistoryStatsIndex = _TnEthSoamPmEceHistoryStatsIndex_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 143, 2, 4, 1, 1, 1),
    _TnEthSoamPmEceHistoryStatsIndex_Type()
)
tnEthSoamPmEceHistoryStatsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnEthSoamPmEceHistoryStatsIndex.setStatus("current")
_TnEthSoamPmEceHistoryStatsEndTime_Type = DateAndTime
_TnEthSoamPmEceHistoryStatsEndTime_Object = MibTableColumn
tnEthSoamPmEceHistoryStatsEndTime = _TnEthSoamPmEceHistoryStatsEndTime_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 143, 2, 4, 1, 1, 2),
    _TnEthSoamPmEceHistoryStatsEndTime_Type()
)
tnEthSoamPmEceHistoryStatsEndTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnEthSoamPmEceHistoryStatsEndTime.setStatus("current")
_TnEthSoamPmEceHistoryStatsElapsedTime_Type = TimeInterval
_TnEthSoamPmEceHistoryStatsElapsedTime_Object = MibTableColumn
tnEthSoamPmEceHistoryStatsElapsedTime = _TnEthSoamPmEceHistoryStatsElapsedTime_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 143, 2, 4, 1, 1, 3),
    _TnEthSoamPmEceHistoryStatsElapsedTime_Type()
)
tnEthSoamPmEceHistoryStatsElapsedTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnEthSoamPmEceHistoryStatsElapsedTime.setStatus("current")
_TnEthSoamPmEceHistoryStatsGreenFramesTx_Type = Counter64
_TnEthSoamPmEceHistoryStatsGreenFramesTx_Object = MibTableColumn
tnEthSoamPmEceHistoryStatsGreenFramesTx = _TnEthSoamPmEceHistoryStatsGreenFramesTx_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 143, 2, 4, 1, 1, 4),
    _TnEthSoamPmEceHistoryStatsGreenFramesTx_Type()
)
tnEthSoamPmEceHistoryStatsGreenFramesTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnEthSoamPmEceHistoryStatsGreenFramesTx.setStatus("current")
_TnEthSoamPmEceHistoryStatsGreenFramesRx_Type = Counter64
_TnEthSoamPmEceHistoryStatsGreenFramesRx_Object = MibTableColumn
tnEthSoamPmEceHistoryStatsGreenFramesRx = _TnEthSoamPmEceHistoryStatsGreenFramesRx_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 143, 2, 4, 1, 1, 5),
    _TnEthSoamPmEceHistoryStatsGreenFramesRx_Type()
)
tnEthSoamPmEceHistoryStatsGreenFramesRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnEthSoamPmEceHistoryStatsGreenFramesRx.setStatus("current")
_TnEthSoamPmEceHistoryStatsGreenBytesTx_Type = Counter64
_TnEthSoamPmEceHistoryStatsGreenBytesTx_Object = MibTableColumn
tnEthSoamPmEceHistoryStatsGreenBytesTx = _TnEthSoamPmEceHistoryStatsGreenBytesTx_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 143, 2, 4, 1, 1, 6),
    _TnEthSoamPmEceHistoryStatsGreenBytesTx_Type()
)
tnEthSoamPmEceHistoryStatsGreenBytesTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnEthSoamPmEceHistoryStatsGreenBytesTx.setStatus("current")
_TnEthSoamPmEceHistoryStatsGreenBytesRx_Type = Counter64
_TnEthSoamPmEceHistoryStatsGreenBytesRx_Object = MibTableColumn
tnEthSoamPmEceHistoryStatsGreenBytesRx = _TnEthSoamPmEceHistoryStatsGreenBytesRx_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 143, 2, 4, 1, 1, 7),
    _TnEthSoamPmEceHistoryStatsGreenBytesRx_Type()
)
tnEthSoamPmEceHistoryStatsGreenBytesRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnEthSoamPmEceHistoryStatsGreenBytesRx.setStatus("current")
_TnEthSoamPmEceHistoryStatsYellowFramesTx_Type = Counter64
_TnEthSoamPmEceHistoryStatsYellowFramesTx_Object = MibTableColumn
tnEthSoamPmEceHistoryStatsYellowFramesTx = _TnEthSoamPmEceHistoryStatsYellowFramesTx_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 143, 2, 4, 1, 1, 8),
    _TnEthSoamPmEceHistoryStatsYellowFramesTx_Type()
)
tnEthSoamPmEceHistoryStatsYellowFramesTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnEthSoamPmEceHistoryStatsYellowFramesTx.setStatus("current")
_TnEthSoamPmEceHistoryStatsYellowFramesRx_Type = Counter64
_TnEthSoamPmEceHistoryStatsYellowFramesRx_Object = MibTableColumn
tnEthSoamPmEceHistoryStatsYellowFramesRx = _TnEthSoamPmEceHistoryStatsYellowFramesRx_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 143, 2, 4, 1, 1, 9),
    _TnEthSoamPmEceHistoryStatsYellowFramesRx_Type()
)
tnEthSoamPmEceHistoryStatsYellowFramesRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnEthSoamPmEceHistoryStatsYellowFramesRx.setStatus("current")
_TnEthSoamPmEceHistoryStatsYellowBytesTx_Type = Counter64
_TnEthSoamPmEceHistoryStatsYellowBytesTx_Object = MibTableColumn
tnEthSoamPmEceHistoryStatsYellowBytesTx = _TnEthSoamPmEceHistoryStatsYellowBytesTx_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 143, 2, 4, 1, 1, 10),
    _TnEthSoamPmEceHistoryStatsYellowBytesTx_Type()
)
tnEthSoamPmEceHistoryStatsYellowBytesTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnEthSoamPmEceHistoryStatsYellowBytesTx.setStatus("current")
_TnEthSoamPmEceHistoryStatsYellowBytesRx_Type = Counter64
_TnEthSoamPmEceHistoryStatsYellowBytesRx_Object = MibTableColumn
tnEthSoamPmEceHistoryStatsYellowBytesRx = _TnEthSoamPmEceHistoryStatsYellowBytesRx_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 143, 2, 4, 1, 1, 11),
    _TnEthSoamPmEceHistoryStatsYellowBytesRx_Type()
)
tnEthSoamPmEceHistoryStatsYellowBytesRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnEthSoamPmEceHistoryStatsYellowBytesRx.setStatus("current")
_TnEthSoamPmEceHistoryStatsRedFramesRx_Type = Counter64
_TnEthSoamPmEceHistoryStatsRedFramesRx_Object = MibTableColumn
tnEthSoamPmEceHistoryStatsRedFramesRx = _TnEthSoamPmEceHistoryStatsRedFramesRx_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 143, 2, 4, 1, 1, 12),
    _TnEthSoamPmEceHistoryStatsRedFramesRx_Type()
)
tnEthSoamPmEceHistoryStatsRedFramesRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnEthSoamPmEceHistoryStatsRedFramesRx.setStatus("current")
_TnEthSoamPmEceHistoryStatsRedBytesRx_Type = Counter64
_TnEthSoamPmEceHistoryStatsRedBytesRx_Object = MibTableColumn
tnEthSoamPmEceHistoryStatsRedBytesRx = _TnEthSoamPmEceHistoryStatsRedBytesRx_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 143, 2, 4, 1, 1, 13),
    _TnEthSoamPmEceHistoryStatsRedBytesRx_Type()
)
tnEthSoamPmEceHistoryStatsRedBytesRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnEthSoamPmEceHistoryStatsRedBytesRx.setStatus("current")
_TnEthSoamPmEceHistoryStatsDiscardFramesTx_Type = Counter64
_TnEthSoamPmEceHistoryStatsDiscardFramesTx_Object = MibTableColumn
tnEthSoamPmEceHistoryStatsDiscardFramesTx = _TnEthSoamPmEceHistoryStatsDiscardFramesTx_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 143, 2, 4, 1, 1, 14),
    _TnEthSoamPmEceHistoryStatsDiscardFramesTx_Type()
)
tnEthSoamPmEceHistoryStatsDiscardFramesTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnEthSoamPmEceHistoryStatsDiscardFramesTx.setStatus("current")
_TnEthSoamPmEceHistoryStatsDiscardFramesRx_Type = Counter64
_TnEthSoamPmEceHistoryStatsDiscardFramesRx_Object = MibTableColumn
tnEthSoamPmEceHistoryStatsDiscardFramesRx = _TnEthSoamPmEceHistoryStatsDiscardFramesRx_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 143, 2, 4, 1, 1, 15),
    _TnEthSoamPmEceHistoryStatsDiscardFramesRx_Type()
)
tnEthSoamPmEceHistoryStatsDiscardFramesRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnEthSoamPmEceHistoryStatsDiscardFramesRx.setStatus("current")
_TnEthSoamPmEceHistoryStatsDiscardBytesTx_Type = Counter64
_TnEthSoamPmEceHistoryStatsDiscardBytesTx_Object = MibTableColumn
tnEthSoamPmEceHistoryStatsDiscardBytesTx = _TnEthSoamPmEceHistoryStatsDiscardBytesTx_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 143, 2, 4, 1, 1, 16),
    _TnEthSoamPmEceHistoryStatsDiscardBytesTx_Type()
)
tnEthSoamPmEceHistoryStatsDiscardBytesTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnEthSoamPmEceHistoryStatsDiscardBytesTx.setStatus("current")
_TnEthSoamPmEceHistoryStatsDiscardBytesRx_Type = Counter64
_TnEthSoamPmEceHistoryStatsDiscardBytesRx_Object = MibTableColumn
tnEthSoamPmEceHistoryStatsDiscardBytesRx = _TnEthSoamPmEceHistoryStatsDiscardBytesRx_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 143, 2, 4, 1, 1, 17),
    _TnEthSoamPmEceHistoryStatsDiscardBytesRx_Type()
)
tnEthSoamPmEceHistoryStatsDiscardBytesRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnEthSoamPmEceHistoryStatsDiscardBytesRx.setStatus("current")
_TnEthSoamPmNotificationMIBObjects_ObjectIdentity = ObjectIdentity
tnEthSoamPmNotificationMIBObjects = _TnEthSoamPmNotificationMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 143, 3)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TN-ETHSOAM-PM-MIB",
    **{"tnEthSoamPmMIB": tnEthSoamPmMIB,
       "tnEthSoamPmNotifications": tnEthSoamPmNotifications,
       "tnEthSoamPmCfgMIBObjects": tnEthSoamPmCfgMIBObjects,
       "tnEthSoamPmSessionCfgObjects": tnEthSoamPmSessionCfgObjects,
       "tnEthSoamPmSessionCfgTable": tnEthSoamPmSessionCfgTable,
       "tnEthSoamPmSessionCfgEntry": tnEthSoamPmSessionCfgEntry,
       "tnEthSoamPmSessionCfgId": tnEthSoamPmSessionCfgId,
       "tnEthSoamPmSessionCfgType": tnEthSoamPmSessionCfgType,
       "tnEthSoamPmSessionCfgSessionMode": tnEthSoamPmSessionCfgSessionMode,
       "tnEthSoamPmSessionCfgStorageMode": tnEthSoamPmSessionCfgStorageMode,
       "tnEthSoamPmSessionCfgInterval": tnEthSoamPmSessionCfgInterval,
       "tnEthSoamPmTransferCfgObjects": tnEthSoamPmTransferCfgObjects,
       "tnEthSoamPmTransferCfgTable": tnEthSoamPmTransferCfgTable,
       "tnEthSoamPmTransferCfgEntry": tnEthSoamPmTransferCfgEntry,
       "tnEthSoamPmTransferCfgId": tnEthSoamPmTransferCfgId,
       "tnEthSoamPmTransferCfgMode": tnEthSoamPmTransferCfgMode,
       "tnEthSoamPmTransferCfgSchedHrs": tnEthSoamPmTransferCfgSchedHrs,
       "tnEthSoamPmTransferCfgSchedMins": tnEthSoamPmTransferCfgSchedMins,
       "tnEthSoamPmTransferCfgSchedOffset": tnEthSoamPmTransferCfgSchedOffset,
       "tnEthSoamPmTransferCfgRandomOffset": tnEthSoamPmTransferCfgRandomOffset,
       "tnEthSoamPmTransferCfgServerAddr": tnEthSoamPmTransferCfgServerAddr,
       "tnEthSoamPmTransferCfgIntervalMode": tnEthSoamPmTransferCfgIntervalMode,
       "tnEthSoamPmTransferCfgIntervalNum": tnEthSoamPmTransferCfgIntervalNum,
       "tnEthSoamPmTransferCfgIncludeIncomplete": tnEthSoamPmTransferCfgIncludeIncomplete,
       "tnEthSoamPmStatsMIBObjects": tnEthSoamPmStatsMIBObjects,
       "tnEthSoamPmLmStatsObjects": tnEthSoamPmLmStatsObjects,
       "tnEthSoamPmLmHistoryStatsTable": tnEthSoamPmLmHistoryStatsTable,
       "tnEthSoamPmLmHistoryStatsEntry": tnEthSoamPmLmHistoryStatsEntry,
       "tnEthSoamPmLmHistoryStatsIndex": tnEthSoamPmLmHistoryStatsIndex,
       "tnEthSoamPmLmHistoryStatsEndTime": tnEthSoamPmLmHistoryStatsEndTime,
       "tnEthSoamPmLmHistoryStatsElapsedTime": tnEthSoamPmLmHistoryStatsElapsedTime,
       "tnEthSoamPmLmHistoryStatsTxCount": tnEthSoamPmLmHistoryStatsTxCount,
       "tnEthSoamPmLmHistoryStatsRxCount": tnEthSoamPmLmHistoryStatsRxCount,
       "tnEthSoamPmLmHistoryStatsNELossCount": tnEthSoamPmLmHistoryStatsNELossCount,
       "tnEthSoamPmLmHistoryStatsFELossCount": tnEthSoamPmLmHistoryStatsFELossCount,
       "tnEthSoamPmLmHistoryStatsNEAvgFlr": tnEthSoamPmLmHistoryStatsNEAvgFlr,
       "tnEthSoamPmLmHistoryStatsFEAvgFlr": tnEthSoamPmLmHistoryStatsFEAvgFlr,
       "tnEthSoamPmDmStatsObjects": tnEthSoamPmDmStatsObjects,
       "tnEthSoamPmDmHistoryStatsTable": tnEthSoamPmDmHistoryStatsTable,
       "tnEthSoamPmDmHistoryStatsEntry": tnEthSoamPmDmHistoryStatsEntry,
       "tnEthSoamPmDmHistoryStatsIndex": tnEthSoamPmDmHistoryStatsIndex,
       "tnEthSoamPmDmHistoryStatsEndTime": tnEthSoamPmDmHistoryStatsEndTime,
       "tnEthSoamPmDmHistoryStatsElapsedTime": tnEthSoamPmDmHistoryStatsElapsedTime,
       "tnEthSoamPmDmHistoryStatsTxCount": tnEthSoamPmDmHistoryStatsTxCount,
       "tnEthSoamPmDmHistoryStatsRxCount": tnEthSoamPmDmHistoryStatsRxCount,
       "tnEthSoamPmDmHistoryStatsFNAvgFrameDelay": tnEthSoamPmDmHistoryStatsFNAvgFrameDelay,
       "tnEthSoamPmDmHistoryStatsFNAvgFrameDV": tnEthSoamPmDmHistoryStatsFNAvgFrameDV,
       "tnEthSoamPmDmHistoryStatsFNMinFrameDelay": tnEthSoamPmDmHistoryStatsFNMinFrameDelay,
       "tnEthSoamPmDmHistoryStatsFNMaxFrameDelay": tnEthSoamPmDmHistoryStatsFNMaxFrameDelay,
       "tnEthSoamPmDmHistoryStatsNFAvgFrameDelay": tnEthSoamPmDmHistoryStatsNFAvgFrameDelay,
       "tnEthSoamPmDmHistoryStatsNFAvgFrameDV": tnEthSoamPmDmHistoryStatsNFAvgFrameDV,
       "tnEthSoamPmDmHistoryStatsNFMinFrameDelay": tnEthSoamPmDmHistoryStatsNFMinFrameDelay,
       "tnEthSoamPmDmHistoryStatsNFMaxFrameDelay": tnEthSoamPmDmHistoryStatsNFMaxFrameDelay,
       "tnEthSoamPmDmHistoryStatsTwoWayAvgFrameDelay": tnEthSoamPmDmHistoryStatsTwoWayAvgFrameDelay,
       "tnEthSoamPmDmHistoryStatsTwoWayAvgFrameDV": tnEthSoamPmDmHistoryStatsTwoWayAvgFrameDV,
       "tnEthSoamPmDmHistoryStatsTwoWayMinFrameDelay": tnEthSoamPmDmHistoryStatsTwoWayMinFrameDelay,
       "tnEthSoamPmDmHistoryStatsTwoWayMaxFrameDelay": tnEthSoamPmDmHistoryStatsTwoWayMaxFrameDelay,
       "tnEthSoamPmEvcStatsObjects": tnEthSoamPmEvcStatsObjects,
       "tnEthSoamPmEvcHistoryStatsTable": tnEthSoamPmEvcHistoryStatsTable,
       "tnEthSoamPmEvcHistoryStatsEntry": tnEthSoamPmEvcHistoryStatsEntry,
       "tnEthSoamPmEvcHistoryStatsIndex": tnEthSoamPmEvcHistoryStatsIndex,
       "tnEthSoamPmEvcHistoryStatsEndTime": tnEthSoamPmEvcHistoryStatsEndTime,
       "tnEthSoamPmEvcHistoryStatsElapsedTime": tnEthSoamPmEvcHistoryStatsElapsedTime,
       "tnEthSoamPmEvcHistoryStatsGreenFramesTx": tnEthSoamPmEvcHistoryStatsGreenFramesTx,
       "tnEthSoamPmEvcHistoryStatsGreenFramesRx": tnEthSoamPmEvcHistoryStatsGreenFramesRx,
       "tnEthSoamPmEvcHistoryStatsGreenBytesTx": tnEthSoamPmEvcHistoryStatsGreenBytesTx,
       "tnEthSoamPmEvcHistoryStatsGreenBytesRx": tnEthSoamPmEvcHistoryStatsGreenBytesRx,
       "tnEthSoamPmEvcHistoryStatsYellowFramesTx": tnEthSoamPmEvcHistoryStatsYellowFramesTx,
       "tnEthSoamPmEvcHistoryStatsYellowFramesRx": tnEthSoamPmEvcHistoryStatsYellowFramesRx,
       "tnEthSoamPmEvcHistoryStatsYellowBytesTx": tnEthSoamPmEvcHistoryStatsYellowBytesTx,
       "tnEthSoamPmEvcHistoryStatsYellowBytesRx": tnEthSoamPmEvcHistoryStatsYellowBytesRx,
       "tnEthSoamPmEvcHistoryStatsRedFramesRx": tnEthSoamPmEvcHistoryStatsRedFramesRx,
       "tnEthSoamPmEvcHistoryStatsRedBytesRx": tnEthSoamPmEvcHistoryStatsRedBytesRx,
       "tnEthSoamPmEvcHistoryStatsDiscardFramesTx": tnEthSoamPmEvcHistoryStatsDiscardFramesTx,
       "tnEthSoamPmEvcHistoryStatsDiscardFramesRx": tnEthSoamPmEvcHistoryStatsDiscardFramesRx,
       "tnEthSoamPmEvcHistoryStatsDiscardBytesTx": tnEthSoamPmEvcHistoryStatsDiscardBytesTx,
       "tnEthSoamPmEvcHistoryStatsDiscardBytesRx": tnEthSoamPmEvcHistoryStatsDiscardBytesRx,
       "tnEthSoamPmEceStatsObjects": tnEthSoamPmEceStatsObjects,
       "tnEthSoamPmEceHistoryStatsTable": tnEthSoamPmEceHistoryStatsTable,
       "tnEthSoamPmEceHistoryStatsEntry": tnEthSoamPmEceHistoryStatsEntry,
       "tnEthSoamPmEceHistoryStatsIndex": tnEthSoamPmEceHistoryStatsIndex,
       "tnEthSoamPmEceHistoryStatsEndTime": tnEthSoamPmEceHistoryStatsEndTime,
       "tnEthSoamPmEceHistoryStatsElapsedTime": tnEthSoamPmEceHistoryStatsElapsedTime,
       "tnEthSoamPmEceHistoryStatsGreenFramesTx": tnEthSoamPmEceHistoryStatsGreenFramesTx,
       "tnEthSoamPmEceHistoryStatsGreenFramesRx": tnEthSoamPmEceHistoryStatsGreenFramesRx,
       "tnEthSoamPmEceHistoryStatsGreenBytesTx": tnEthSoamPmEceHistoryStatsGreenBytesTx,
       "tnEthSoamPmEceHistoryStatsGreenBytesRx": tnEthSoamPmEceHistoryStatsGreenBytesRx,
       "tnEthSoamPmEceHistoryStatsYellowFramesTx": tnEthSoamPmEceHistoryStatsYellowFramesTx,
       "tnEthSoamPmEceHistoryStatsYellowFramesRx": tnEthSoamPmEceHistoryStatsYellowFramesRx,
       "tnEthSoamPmEceHistoryStatsYellowBytesTx": tnEthSoamPmEceHistoryStatsYellowBytesTx,
       "tnEthSoamPmEceHistoryStatsYellowBytesRx": tnEthSoamPmEceHistoryStatsYellowBytesRx,
       "tnEthSoamPmEceHistoryStatsRedFramesRx": tnEthSoamPmEceHistoryStatsRedFramesRx,
       "tnEthSoamPmEceHistoryStatsRedBytesRx": tnEthSoamPmEceHistoryStatsRedBytesRx,
       "tnEthSoamPmEceHistoryStatsDiscardFramesTx": tnEthSoamPmEceHistoryStatsDiscardFramesTx,
       "tnEthSoamPmEceHistoryStatsDiscardFramesRx": tnEthSoamPmEceHistoryStatsDiscardFramesRx,
       "tnEthSoamPmEceHistoryStatsDiscardBytesTx": tnEthSoamPmEceHistoryStatsDiscardBytesTx,
       "tnEthSoamPmEceHistoryStatsDiscardBytesRx": tnEthSoamPmEceHistoryStatsDiscardBytesRx,
       "tnEthSoamPmNotificationMIBObjects": tnEthSoamPmNotificationMIBObjects}
)
