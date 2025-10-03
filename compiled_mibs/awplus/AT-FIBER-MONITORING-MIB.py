# SNMP MIB module (AT-FIBER-MONITORING-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\awplus\AT-FIBER-MONITORING-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:20:26 2025
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

(sysinfo,) = mibBuilder.importSymbols(
    "AT-SYSINFO-MIB",
    "sysinfo")

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

atFiberMon = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 27)
)
if mibBuilder.loadTexts:
    atFiberMon.setRevisions(
        ("2015-09-08 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AtFiberMonNotifications_ObjectIdentity = ObjectIdentity
atFiberMonNotifications = _AtFiberMonNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 27, 0)
)
_AtFiberMonTrapVariable_ObjectIdentity = ObjectIdentity
atFiberMonTrapVariable = _AtFiberMonTrapVariable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 27, 1)
)


class _AtFiberMonReading_Type(Integer32):
    """Custom type atFiberMonReading based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AtFiberMonReading_Type.__name__ = "Integer32"
_AtFiberMonReading_Object = MibScalar
atFiberMonReading = _AtFiberMonReading_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 27, 1, 1),
    _AtFiberMonReading_Type()
)
atFiberMonReading.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    atFiberMonReading.setStatus("current")
_AtFiberMonConfigTable_Object = MibTable
atFiberMonConfigTable = _AtFiberMonConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 27, 2)
)
if mibBuilder.loadTexts:
    atFiberMonConfigTable.setStatus("current")
_AtFiberMonConfigEntry_Object = MibTableRow
atFiberMonConfigEntry = _AtFiberMonConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 27, 2, 1)
)
atFiberMonConfigEntry.setIndexNames(
    (0, "AT-FIBER-MONITORING-MIB", "atFiberMonIfname"),
)
if mibBuilder.loadTexts:
    atFiberMonConfigEntry.setStatus("current")


class _AtFiberMonIfname_Type(OctetString):
    """Custom type atFiberMonIfname based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_AtFiberMonIfname_Type.__name__ = "OctetString"
_AtFiberMonIfname_Object = MibTableColumn
atFiberMonIfname = _AtFiberMonIfname_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 27, 2, 1, 1),
    _AtFiberMonIfname_Type()
)
atFiberMonIfname.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atFiberMonIfname.setStatus("current")


class _AtFiberMonEnable_Type(Integer32):
    """Custom type atFiberMonEnable based on Integer32"""
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


_AtFiberMonEnable_Type.__name__ = "Integer32"
_AtFiberMonEnable_Object = MibTableColumn
atFiberMonEnable = _AtFiberMonEnable_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 27, 2, 1, 2),
    _AtFiberMonEnable_Type()
)
atFiberMonEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atFiberMonEnable.setStatus("current")


class _AtFiberMonInterval_Type(Integer32):
    """Custom type atFiberMonInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 60),
    )


_AtFiberMonInterval_Type.__name__ = "Integer32"
_AtFiberMonInterval_Object = MibTableColumn
atFiberMonInterval = _AtFiberMonInterval_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 27, 2, 1, 3),
    _AtFiberMonInterval_Type()
)
atFiberMonInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atFiberMonInterval.setStatus("current")
_AtFiberMonSensitivity_Type = OctetString
_AtFiberMonSensitivity_Object = MibTableColumn
atFiberMonSensitivity = _AtFiberMonSensitivity_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 27, 2, 1, 4),
    _AtFiberMonSensitivity_Type()
)
atFiberMonSensitivity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atFiberMonSensitivity.setStatus("current")
_AtFiberMonBaseline_Type = OctetString
_AtFiberMonBaseline_Object = MibTableColumn
atFiberMonBaseline = _AtFiberMonBaseline_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 27, 2, 1, 5),
    _AtFiberMonBaseline_Type()
)
atFiberMonBaseline.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atFiberMonBaseline.setStatus("current")


class _AtFiberMonAlarmAction_Type(Integer32):
    """Custom type atFiberMonAlarmAction based on Integer32"""
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
        *(("logOnly", 1),
          ("sendTrap", 2),
          ("shutdown", 3),
          ("sendtrapAndShutdown", 4))
    )


_AtFiberMonAlarmAction_Type.__name__ = "Integer32"
_AtFiberMonAlarmAction_Object = MibTableColumn
atFiberMonAlarmAction = _AtFiberMonAlarmAction_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 27, 2, 1, 6),
    _AtFiberMonAlarmAction_Type()
)
atFiberMonAlarmAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atFiberMonAlarmAction.setStatus("current")
_AtFiberMonStateTable_Object = MibTable
atFiberMonStateTable = _AtFiberMonStateTable_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 27, 3)
)
if mibBuilder.loadTexts:
    atFiberMonStateTable.setStatus("current")
_AtFiberMonStateEntry_Object = MibTableRow
atFiberMonStateEntry = _AtFiberMonStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 27, 3, 1)
)
atFiberMonStateEntry.setIndexNames(
    (0, "AT-FIBER-MONITORING-MIB", "atFiberMonIfindex"),
    (0, "AT-FIBER-MONITORING-MIB", "atFiberMonChannel"),
)
if mibBuilder.loadTexts:
    atFiberMonStateEntry.setStatus("current")


class _AtFiberMonIfindex_Type(Integer32):
    """Custom type atFiberMonIfindex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_AtFiberMonIfindex_Type.__name__ = "Integer32"
_AtFiberMonIfindex_Object = MibTableColumn
atFiberMonIfindex = _AtFiberMonIfindex_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 27, 3, 1, 1),
    _AtFiberMonIfindex_Type()
)
atFiberMonIfindex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atFiberMonIfindex.setStatus("current")


class _AtFiberMonChannel_Type(Integer32):
    """Custom type atFiberMonChannel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_AtFiberMonChannel_Type.__name__ = "Integer32"
_AtFiberMonChannel_Object = MibTableColumn
atFiberMonChannel = _AtFiberMonChannel_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 27, 3, 1, 2),
    _AtFiberMonChannel_Type()
)
atFiberMonChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atFiberMonChannel.setStatus("current")
_AtFiberMonlIfDescription_Type = DisplayString
_AtFiberMonlIfDescription_Object = MibTableColumn
atFiberMonlIfDescription = _AtFiberMonlIfDescription_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 27, 3, 1, 3),
    _AtFiberMonlIfDescription_Type()
)
atFiberMonlIfDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atFiberMonlIfDescription.setStatus("current")


class _AtFiberMonActualBaseline_Type(Integer32):
    """Custom type atFiberMonActualBaseline based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AtFiberMonActualBaseline_Type.__name__ = "Integer32"
_AtFiberMonActualBaseline_Object = MibTableColumn
atFiberMonActualBaseline = _AtFiberMonActualBaseline_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 27, 3, 1, 4),
    _AtFiberMonActualBaseline_Type()
)
atFiberMonActualBaseline.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atFiberMonActualBaseline.setStatus("current")


class _AtFiberMonThreshold_Type(Integer32):
    """Custom type atFiberMonThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AtFiberMonThreshold_Type.__name__ = "Integer32"
_AtFiberMonThreshold_Object = MibTableColumn
atFiberMonThreshold = _AtFiberMonThreshold_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 27, 3, 1, 5),
    _AtFiberMonThreshold_Type()
)
atFiberMonThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atFiberMonThreshold.setStatus("current")
_AtFiberMonReadingHistory_Type = DisplayString
_AtFiberMonReadingHistory_Object = MibTableColumn
atFiberMonReadingHistory = _AtFiberMonReadingHistory_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 27, 3, 1, 6),
    _AtFiberMonReadingHistory_Type()
)
atFiberMonReadingHistory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atFiberMonReadingHistory.setStatus("current")


class _AtFiberMonMinReading_Type(Integer32):
    """Custom type atFiberMonMinReading based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AtFiberMonMinReading_Type.__name__ = "Integer32"
_AtFiberMonMinReading_Object = MibTableColumn
atFiberMonMinReading = _AtFiberMonMinReading_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 27, 3, 1, 7),
    _AtFiberMonMinReading_Type()
)
atFiberMonMinReading.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atFiberMonMinReading.setStatus("current")


class _AtFiberMonMaxReading_Type(Integer32):
    """Custom type atFiberMonMaxReading based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AtFiberMonMaxReading_Type.__name__ = "Integer32"
_AtFiberMonMaxReading_Object = MibTableColumn
atFiberMonMaxReading = _AtFiberMonMaxReading_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 27, 3, 1, 8),
    _AtFiberMonMaxReading_Type()
)
atFiberMonMaxReading.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atFiberMonMaxReading.setStatus("current")

# Managed Objects groups


# Notification objects

atFiberMonAlarmSetNotify = NotificationType(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 27, 0, 1)
)
atFiberMonAlarmSetNotify.setObjects(
      *(("AT-FIBER-MONITORING-MIB", "atFiberMonIfindex"),
        ("AT-FIBER-MONITORING-MIB", "atFiberMonChannel"),
        ("AT-FIBER-MONITORING-MIB", "atFiberMonIfname"),
        ("AT-FIBER-MONITORING-MIB", "atFiberMonReading"),
        ("AT-FIBER-MONITORING-MIB", "atFiberMonThreshold"))
)
if mibBuilder.loadTexts:
    atFiberMonAlarmSetNotify.setStatus(
        "current"
    )

atFiberMonAlarmClearedNotify = NotificationType(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 27, 0, 2)
)
atFiberMonAlarmClearedNotify.setObjects(
      *(("AT-FIBER-MONITORING-MIB", "atFiberMonIfindex"),
        ("AT-FIBER-MONITORING-MIB", "atFiberMonChannel"),
        ("AT-FIBER-MONITORING-MIB", "atFiberMonIfname"),
        ("AT-FIBER-MONITORING-MIB", "atFiberMonReading"),
        ("AT-FIBER-MONITORING-MIB", "atFiberMonThreshold"))
)
if mibBuilder.loadTexts:
    atFiberMonAlarmClearedNotify.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "AT-FIBER-MONITORING-MIB",
    **{"atFiberMon": atFiberMon,
       "atFiberMonNotifications": atFiberMonNotifications,
       "atFiberMonAlarmSetNotify": atFiberMonAlarmSetNotify,
       "atFiberMonAlarmClearedNotify": atFiberMonAlarmClearedNotify,
       "atFiberMonTrapVariable": atFiberMonTrapVariable,
       "atFiberMonReading": atFiberMonReading,
       "atFiberMonConfigTable": atFiberMonConfigTable,
       "atFiberMonConfigEntry": atFiberMonConfigEntry,
       "atFiberMonIfname": atFiberMonIfname,
       "atFiberMonEnable": atFiberMonEnable,
       "atFiberMonInterval": atFiberMonInterval,
       "atFiberMonSensitivity": atFiberMonSensitivity,
       "atFiberMonBaseline": atFiberMonBaseline,
       "atFiberMonAlarmAction": atFiberMonAlarmAction,
       "atFiberMonStateTable": atFiberMonStateTable,
       "atFiberMonStateEntry": atFiberMonStateEntry,
       "atFiberMonIfindex": atFiberMonIfindex,
       "atFiberMonChannel": atFiberMonChannel,
       "atFiberMonlIfDescription": atFiberMonlIfDescription,
       "atFiberMonActualBaseline": atFiberMonActualBaseline,
       "atFiberMonThreshold": atFiberMonThreshold,
       "atFiberMonReadingHistory": atFiberMonReadingHistory,
       "atFiberMonMinReading": atFiberMonMinReading,
       "atFiberMonMaxReading": atFiberMonMaxReading}
)
