# SNMP MIB module (HH3C-RMON-EXT2-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\comware\HH3C-RMON-EXT2-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:32:44 2025
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

(EntryStatus,
 OwnerString) = mibBuilder.importSymbols(
    "RMON-MIB",
    "EntryStatus",
    "OwnerString")

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

hh3cRmonExt = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 125)
)
if mibBuilder.loadTexts:
    hh3cRmonExt.setRevisions(
        ("2012-06-19 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Hh3cRmonExtEvent_ObjectIdentity = ObjectIdentity
hh3cRmonExtEvent = _Hh3cRmonExtEvent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 125, 0)
)
if mibBuilder.loadTexts:
    hh3cRmonExtEvent.setStatus("current")
_Hh3cRmonExtAlarmTable_Object = MibTable
hh3cRmonExtAlarmTable = _Hh3cRmonExtAlarmTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 125, 1)
)
if mibBuilder.loadTexts:
    hh3cRmonExtAlarmTable.setStatus("current")
_Hh3cRmonExtAlarmEntry_Object = MibTableRow
hh3cRmonExtAlarmEntry = _Hh3cRmonExtAlarmEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 125, 1, 1)
)
hh3cRmonExtAlarmEntry.setIndexNames(
    (0, "HH3C-RMON-EXT2-MIB", "hh3cRmonExtAlarmIndex"),
)
if mibBuilder.loadTexts:
    hh3cRmonExtAlarmEntry.setStatus("current")


class _Hh3cRmonExtAlarmIndex_Type(Integer32):
    """Custom type hh3cRmonExtAlarmIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_Hh3cRmonExtAlarmIndex_Type.__name__ = "Integer32"
_Hh3cRmonExtAlarmIndex_Object = MibTableColumn
hh3cRmonExtAlarmIndex = _Hh3cRmonExtAlarmIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 125, 1, 1, 1),
    _Hh3cRmonExtAlarmIndex_Type()
)
hh3cRmonExtAlarmIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cRmonExtAlarmIndex.setStatus("current")


class _Hh3cRmonExtAlarmInterval_Type(Integer32):
    """Custom type hh3cRmonExtAlarmInterval based on Integer32"""
    defaultValue = 1800

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 65535),
    )


_Hh3cRmonExtAlarmInterval_Type.__name__ = "Integer32"
_Hh3cRmonExtAlarmInterval_Object = MibTableColumn
hh3cRmonExtAlarmInterval = _Hh3cRmonExtAlarmInterval_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 125, 1, 1, 2),
    _Hh3cRmonExtAlarmInterval_Type()
)
hh3cRmonExtAlarmInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cRmonExtAlarmInterval.setStatus("current")
_Hh3cRmonExtAlarmVariable_Type = DisplayString
_Hh3cRmonExtAlarmVariable_Object = MibTableColumn
hh3cRmonExtAlarmVariable = _Hh3cRmonExtAlarmVariable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 125, 1, 1, 3),
    _Hh3cRmonExtAlarmVariable_Type()
)
hh3cRmonExtAlarmVariable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cRmonExtAlarmVariable.setStatus("current")
_Hh3cRmonExtAlarmSympol_Type = DisplayString
_Hh3cRmonExtAlarmSympol_Object = MibTableColumn
hh3cRmonExtAlarmSympol = _Hh3cRmonExtAlarmSympol_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 125, 1, 1, 4),
    _Hh3cRmonExtAlarmSympol_Type()
)
hh3cRmonExtAlarmSympol.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cRmonExtAlarmSympol.setStatus("current")


class _Hh3cRmonExtAlarmSampleType_Type(Integer32):
    """Custom type hh3cRmonExtAlarmSampleType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("absoluteValue", 1),
          ("deltaValue", 2),
          ("speedValue", 3))
    )


_Hh3cRmonExtAlarmSampleType_Type.__name__ = "Integer32"
_Hh3cRmonExtAlarmSampleType_Object = MibTableColumn
hh3cRmonExtAlarmSampleType = _Hh3cRmonExtAlarmSampleType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 125, 1, 1, 5),
    _Hh3cRmonExtAlarmSampleType_Type()
)
hh3cRmonExtAlarmSampleType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cRmonExtAlarmSampleType.setStatus("current")
_Hh3cRmonExtAlarmValue_Type = Integer32
_Hh3cRmonExtAlarmValue_Object = MibTableColumn
hh3cRmonExtAlarmValue = _Hh3cRmonExtAlarmValue_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 125, 1, 1, 6),
    _Hh3cRmonExtAlarmValue_Type()
)
hh3cRmonExtAlarmValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cRmonExtAlarmValue.setStatus("current")


class _Hh3cRmonExtAlarmStartupAlarm_Type(Integer32):
    """Custom type hh3cRmonExtAlarmStartupAlarm based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("risingAlarm", 1),
          ("fallingAlarm", 2),
          ("risingOrFallingAlarm", 3))
    )


_Hh3cRmonExtAlarmStartupAlarm_Type.__name__ = "Integer32"
_Hh3cRmonExtAlarmStartupAlarm_Object = MibTableColumn
hh3cRmonExtAlarmStartupAlarm = _Hh3cRmonExtAlarmStartupAlarm_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 125, 1, 1, 7),
    _Hh3cRmonExtAlarmStartupAlarm_Type()
)
hh3cRmonExtAlarmStartupAlarm.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cRmonExtAlarmStartupAlarm.setStatus("current")


class _Hh3cRmonExtAlarmRisingThreshold_Type(Integer32):
    """Custom type hh3cRmonExtAlarmRisingThreshold based on Integer32"""
    defaultValue = 1


_Hh3cRmonExtAlarmRisingThreshold_Type.__name__ = "Integer32"
_Hh3cRmonExtAlarmRisingThreshold_Object = MibTableColumn
hh3cRmonExtAlarmRisingThreshold = _Hh3cRmonExtAlarmRisingThreshold_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 125, 1, 1, 8),
    _Hh3cRmonExtAlarmRisingThreshold_Type()
)
hh3cRmonExtAlarmRisingThreshold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cRmonExtAlarmRisingThreshold.setStatus("current")


class _Hh3cRmonExtAlarmFallingThreshold_Type(Integer32):
    """Custom type hh3cRmonExtAlarmFallingThreshold based on Integer32"""
    defaultValue = 0


_Hh3cRmonExtAlarmFallingThreshold_Type.__name__ = "Integer32"
_Hh3cRmonExtAlarmFallingThreshold_Object = MibTableColumn
hh3cRmonExtAlarmFallingThreshold = _Hh3cRmonExtAlarmFallingThreshold_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 125, 1, 1, 9),
    _Hh3cRmonExtAlarmFallingThreshold_Type()
)
hh3cRmonExtAlarmFallingThreshold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cRmonExtAlarmFallingThreshold.setStatus("current")


class _Hh3cRmonExtAlarmRisingEvtIndex_Type(Integer32):
    """Custom type hh3cRmonExtAlarmRisingEvtIndex based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Hh3cRmonExtAlarmRisingEvtIndex_Type.__name__ = "Integer32"
_Hh3cRmonExtAlarmRisingEvtIndex_Object = MibTableColumn
hh3cRmonExtAlarmRisingEvtIndex = _Hh3cRmonExtAlarmRisingEvtIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 125, 1, 1, 10),
    _Hh3cRmonExtAlarmRisingEvtIndex_Type()
)
hh3cRmonExtAlarmRisingEvtIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cRmonExtAlarmRisingEvtIndex.setStatus("current")


class _Hh3cRmonExtAlarmFallingEvtIndex_Type(Integer32):
    """Custom type hh3cRmonExtAlarmFallingEvtIndex based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Hh3cRmonExtAlarmFallingEvtIndex_Type.__name__ = "Integer32"
_Hh3cRmonExtAlarmFallingEvtIndex_Object = MibTableColumn
hh3cRmonExtAlarmFallingEvtIndex = _Hh3cRmonExtAlarmFallingEvtIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 125, 1, 1, 11),
    _Hh3cRmonExtAlarmFallingEvtIndex_Type()
)
hh3cRmonExtAlarmFallingEvtIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cRmonExtAlarmFallingEvtIndex.setStatus("current")


class _Hh3cRmonExtAlarmStatCycle_Type(Integer32):
    """Custom type hh3cRmonExtAlarmStatCycle based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967),
    )


_Hh3cRmonExtAlarmStatCycle_Type.__name__ = "Integer32"
_Hh3cRmonExtAlarmStatCycle_Object = MibTableColumn
hh3cRmonExtAlarmStatCycle = _Hh3cRmonExtAlarmStatCycle_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 125, 1, 1, 12),
    _Hh3cRmonExtAlarmStatCycle_Type()
)
hh3cRmonExtAlarmStatCycle.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cRmonExtAlarmStatCycle.setStatus("current")


class _Hh3cRmonExtAlarmStatType_Type(Integer32):
    """Custom type hh3cRmonExtAlarmStatType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("forever", 1),
          ("during", 2))
    )


_Hh3cRmonExtAlarmStatType_Type.__name__ = "Integer32"
_Hh3cRmonExtAlarmStatType_Object = MibTableColumn
hh3cRmonExtAlarmStatType = _Hh3cRmonExtAlarmStatType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 125, 1, 1, 13),
    _Hh3cRmonExtAlarmStatType_Type()
)
hh3cRmonExtAlarmStatType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cRmonExtAlarmStatType.setStatus("current")
_Hh3cRmonExtAlarmOwner_Type = OwnerString
_Hh3cRmonExtAlarmOwner_Object = MibTableColumn
hh3cRmonExtAlarmOwner = _Hh3cRmonExtAlarmOwner_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 125, 1, 1, 14),
    _Hh3cRmonExtAlarmOwner_Type()
)
hh3cRmonExtAlarmOwner.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cRmonExtAlarmOwner.setStatus("current")
_Hh3cRmonExtAlarmStatus_Type = EntryStatus
_Hh3cRmonExtAlarmStatus_Object = MibTableColumn
hh3cRmonExtAlarmStatus = _Hh3cRmonExtAlarmStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 125, 1, 1, 15),
    _Hh3cRmonExtAlarmStatus_Type()
)
hh3cRmonExtAlarmStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cRmonExtAlarmStatus.setStatus("current")

# Managed Objects groups


# Notification objects

hh3cRmonExtRisingAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 125, 0, 1)
)
hh3cRmonExtRisingAlarm.setObjects(
      *(("HH3C-RMON-EXT2-MIB", "hh3cRmonExtAlarmIndex"),
        ("HH3C-RMON-EXT2-MIB", "hh3cRmonExtAlarmSympol"),
        ("HH3C-RMON-EXT2-MIB", "hh3cRmonExtAlarmSampleType"),
        ("HH3C-RMON-EXT2-MIB", "hh3cRmonExtAlarmValue"),
        ("HH3C-RMON-EXT2-MIB", "hh3cRmonExtAlarmRisingThreshold"))
)
if mibBuilder.loadTexts:
    hh3cRmonExtRisingAlarm.setStatus(
        "current"
    )

hh3cRmonExtFallingAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 125, 0, 2)
)
hh3cRmonExtFallingAlarm.setObjects(
      *(("HH3C-RMON-EXT2-MIB", "hh3cRmonExtAlarmIndex"),
        ("HH3C-RMON-EXT2-MIB", "hh3cRmonExtAlarmSympol"),
        ("HH3C-RMON-EXT2-MIB", "hh3cRmonExtAlarmSampleType"),
        ("HH3C-RMON-EXT2-MIB", "hh3cRmonExtAlarmValue"),
        ("HH3C-RMON-EXT2-MIB", "hh3cRmonExtAlarmFallingThreshold"))
)
if mibBuilder.loadTexts:
    hh3cRmonExtFallingAlarm.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HH3C-RMON-EXT2-MIB",
    **{"hh3cRmonExt": hh3cRmonExt,
       "hh3cRmonExtEvent": hh3cRmonExtEvent,
       "hh3cRmonExtRisingAlarm": hh3cRmonExtRisingAlarm,
       "hh3cRmonExtFallingAlarm": hh3cRmonExtFallingAlarm,
       "hh3cRmonExtAlarmTable": hh3cRmonExtAlarmTable,
       "hh3cRmonExtAlarmEntry": hh3cRmonExtAlarmEntry,
       "hh3cRmonExtAlarmIndex": hh3cRmonExtAlarmIndex,
       "hh3cRmonExtAlarmInterval": hh3cRmonExtAlarmInterval,
       "hh3cRmonExtAlarmVariable": hh3cRmonExtAlarmVariable,
       "hh3cRmonExtAlarmSympol": hh3cRmonExtAlarmSympol,
       "hh3cRmonExtAlarmSampleType": hh3cRmonExtAlarmSampleType,
       "hh3cRmonExtAlarmValue": hh3cRmonExtAlarmValue,
       "hh3cRmonExtAlarmStartupAlarm": hh3cRmonExtAlarmStartupAlarm,
       "hh3cRmonExtAlarmRisingThreshold": hh3cRmonExtAlarmRisingThreshold,
       "hh3cRmonExtAlarmFallingThreshold": hh3cRmonExtAlarmFallingThreshold,
       "hh3cRmonExtAlarmRisingEvtIndex": hh3cRmonExtAlarmRisingEvtIndex,
       "hh3cRmonExtAlarmFallingEvtIndex": hh3cRmonExtAlarmFallingEvtIndex,
       "hh3cRmonExtAlarmStatCycle": hh3cRmonExtAlarmStatCycle,
       "hh3cRmonExtAlarmStatType": hh3cRmonExtAlarmStatType,
       "hh3cRmonExtAlarmOwner": hh3cRmonExtAlarmOwner,
       "hh3cRmonExtAlarmStatus": hh3cRmonExtAlarmStatus}
)
