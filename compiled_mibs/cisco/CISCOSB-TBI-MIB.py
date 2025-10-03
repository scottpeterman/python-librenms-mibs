# SNMP MIB module (CISCOSB-TBI-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\cisco\CISCOSB-TBI-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:29:58 2025
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

(switch001,) = mibBuilder.importSymbols(
    "CISCOSB-MIB",
    "switch001")

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

rlTBIMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 145)
)
if mibBuilder.loadTexts:
    rlTBIMib.setRevisions(
        ("2006-02-12 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class RlTBIWeekDayList(TextualConvention, Bits):
    status = "current"
    namedValues = NamedValues(
        *(("monday", 0),
          ("tuesday", 1),
          ("wednesday", 2),
          ("thursday", 3),
          ("friday", 4),
          ("saturday", 5),
          ("sunday", 6))
    )


# MIB Managed Objects in the order of their OIDs

_RlTBITimeRangeTable_Object = MibTable
rlTBITimeRangeTable = _RlTBITimeRangeTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 145, 1)
)
if mibBuilder.loadTexts:
    rlTBITimeRangeTable.setStatus("current")
_RlTBITimeRangeEntry_Object = MibTableRow
rlTBITimeRangeEntry = _RlTBITimeRangeEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 145, 1, 1)
)
rlTBITimeRangeEntry.setIndexNames(
    (1, "CISCOSB-TBI-MIB", "rlTBITimeRangeName"),
)
if mibBuilder.loadTexts:
    rlTBITimeRangeEntry.setStatus("current")


class _RlTBITimeRangeName_Type(DisplayString):
    """Custom type rlTBITimeRangeName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_RlTBITimeRangeName_Type.__name__ = "DisplayString"
_RlTBITimeRangeName_Object = MibTableColumn
rlTBITimeRangeName = _RlTBITimeRangeName_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 145, 1, 1, 1),
    _RlTBITimeRangeName_Type()
)
rlTBITimeRangeName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlTBITimeRangeName.setStatus("current")


class _RlTBITimeRangeAbsoluteStart_Type(DisplayString):
    """Custom type rlTBITimeRangeAbsoluteStart based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 14),
    )


_RlTBITimeRangeAbsoluteStart_Type.__name__ = "DisplayString"
_RlTBITimeRangeAbsoluteStart_Object = MibTableColumn
rlTBITimeRangeAbsoluteStart = _RlTBITimeRangeAbsoluteStart_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 145, 1, 1, 2),
    _RlTBITimeRangeAbsoluteStart_Type()
)
rlTBITimeRangeAbsoluteStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlTBITimeRangeAbsoluteStart.setStatus("current")


class _RlTBITimeRangeAbsoluteEnd_Type(DisplayString):
    """Custom type rlTBITimeRangeAbsoluteEnd based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 14),
    )


_RlTBITimeRangeAbsoluteEnd_Type.__name__ = "DisplayString"
_RlTBITimeRangeAbsoluteEnd_Object = MibTableColumn
rlTBITimeRangeAbsoluteEnd = _RlTBITimeRangeAbsoluteEnd_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 145, 1, 1, 3),
    _RlTBITimeRangeAbsoluteEnd_Type()
)
rlTBITimeRangeAbsoluteEnd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlTBITimeRangeAbsoluteEnd.setStatus("current")
_RlTBITimeRangeActiveStatus_Type = TruthValue
_RlTBITimeRangeActiveStatus_Object = MibTableColumn
rlTBITimeRangeActiveStatus = _RlTBITimeRangeActiveStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 145, 1, 1, 4),
    _RlTBITimeRangeActiveStatus_Type()
)
rlTBITimeRangeActiveStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlTBITimeRangeActiveStatus.setStatus("current")
_RlTBITimeRangeRowStatus_Type = RowStatus
_RlTBITimeRangeRowStatus_Object = MibTableColumn
rlTBITimeRangeRowStatus = _RlTBITimeRangeRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 145, 1, 1, 5),
    _RlTBITimeRangeRowStatus_Type()
)
rlTBITimeRangeRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rlTBITimeRangeRowStatus.setStatus("current")
_RlTBIPeriodicTable_Object = MibTable
rlTBIPeriodicTable = _RlTBIPeriodicTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 145, 2)
)
if mibBuilder.loadTexts:
    rlTBIPeriodicTable.setStatus("current")
_RlTBIPeriodicEntry_Object = MibTableRow
rlTBIPeriodicEntry = _RlTBIPeriodicEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 145, 2, 1)
)
rlTBIPeriodicEntry.setIndexNames(
    (0, "CISCOSB-TBI-MIB", "rlTBIPeriodicTimeRangeName"),
    (0, "CISCOSB-TBI-MIB", "rlTBIPeriodicWeekDayList"),
    (0, "CISCOSB-TBI-MIB", "rlTBIPeriodicStart"),
    (0, "CISCOSB-TBI-MIB", "rlTBIPeriodicEnd"),
)
if mibBuilder.loadTexts:
    rlTBIPeriodicEntry.setStatus("current")


class _RlTBIPeriodicTimeRangeName_Type(DisplayString):
    """Custom type rlTBIPeriodicTimeRangeName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_RlTBIPeriodicTimeRangeName_Type.__name__ = "DisplayString"
_RlTBIPeriodicTimeRangeName_Object = MibTableColumn
rlTBIPeriodicTimeRangeName = _RlTBIPeriodicTimeRangeName_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 145, 2, 1, 1),
    _RlTBIPeriodicTimeRangeName_Type()
)
rlTBIPeriodicTimeRangeName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlTBIPeriodicTimeRangeName.setStatus("current")
_RlTBIPeriodicWeekDayList_Type = RlTBIWeekDayList
_RlTBIPeriodicWeekDayList_Object = MibTableColumn
rlTBIPeriodicWeekDayList = _RlTBIPeriodicWeekDayList_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 145, 2, 1, 2),
    _RlTBIPeriodicWeekDayList_Type()
)
rlTBIPeriodicWeekDayList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlTBIPeriodicWeekDayList.setStatus("current")


class _RlTBIPeriodicStart_Type(DisplayString):
    """Custom type rlTBIPeriodicStart based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 7),
    )


_RlTBIPeriodicStart_Type.__name__ = "DisplayString"
_RlTBIPeriodicStart_Object = MibTableColumn
rlTBIPeriodicStart = _RlTBIPeriodicStart_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 145, 2, 1, 3),
    _RlTBIPeriodicStart_Type()
)
rlTBIPeriodicStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlTBIPeriodicStart.setStatus("current")


class _RlTBIPeriodicEnd_Type(DisplayString):
    """Custom type rlTBIPeriodicEnd based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 7),
    )


_RlTBIPeriodicEnd_Type.__name__ = "DisplayString"
_RlTBIPeriodicEnd_Object = MibTableColumn
rlTBIPeriodicEnd = _RlTBIPeriodicEnd_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 145, 2, 1, 4),
    _RlTBIPeriodicEnd_Type()
)
rlTBIPeriodicEnd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlTBIPeriodicEnd.setStatus("current")
_RlTBIPeriodicRowStatus_Type = RowStatus
_RlTBIPeriodicRowStatus_Object = MibTableColumn
rlTBIPeriodicRowStatus = _RlTBIPeriodicRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 145, 2, 1, 5),
    _RlTBIPeriodicRowStatus_Type()
)
rlTBIPeriodicRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rlTBIPeriodicRowStatus.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCOSB-TBI-MIB",
    **{"RlTBIWeekDayList": RlTBIWeekDayList,
       "rlTBIMib": rlTBIMib,
       "rlTBITimeRangeTable": rlTBITimeRangeTable,
       "rlTBITimeRangeEntry": rlTBITimeRangeEntry,
       "rlTBITimeRangeName": rlTBITimeRangeName,
       "rlTBITimeRangeAbsoluteStart": rlTBITimeRangeAbsoluteStart,
       "rlTBITimeRangeAbsoluteEnd": rlTBITimeRangeAbsoluteEnd,
       "rlTBITimeRangeActiveStatus": rlTBITimeRangeActiveStatus,
       "rlTBITimeRangeRowStatus": rlTBITimeRangeRowStatus,
       "rlTBIPeriodicTable": rlTBIPeriodicTable,
       "rlTBIPeriodicEntry": rlTBIPeriodicEntry,
       "rlTBIPeriodicTimeRangeName": rlTBIPeriodicTimeRangeName,
       "rlTBIPeriodicWeekDayList": rlTBIPeriodicWeekDayList,
       "rlTBIPeriodicStart": rlTBIPeriodicStart,
       "rlTBIPeriodicEnd": rlTBIPeriodicEnd,
       "rlTBIPeriodicRowStatus": rlTBIPeriodicRowStatus}
)
