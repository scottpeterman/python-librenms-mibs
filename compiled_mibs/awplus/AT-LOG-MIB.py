# SNMP MIB module (AT-LOG-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\awplus\AT-LOG-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:20:31 2025
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

(modules,) = mibBuilder.importSymbols(
    "AT-SMI-MIB",
    "modules")

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

log = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 601)
)
if mibBuilder.loadTexts:
    log.setRevisions(
        ("2016-06-23 00:00",
         "2012-06-08 00:00",
         "2012-06-07 00:00",
         "2011-05-30 00:00",
         "2011-04-18 00:00",
         "2010-09-07 00:00",
         "2010-06-14 05:11",
         "2008-10-08 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_LogNotifications_ObjectIdentity = ObjectIdentity
logNotifications = _LogNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 601, 0)
)
_LogTable_Object = MibTable
logTable = _LogTable_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 601, 1)
)
if mibBuilder.loadTexts:
    logTable.setStatus("current")
_LogEntry_Object = MibTableRow
logEntry = _LogEntry_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 601, 1, 1)
)
logEntry.setIndexNames(
    (0, "AT-LOG-MIB", "logIndex"),
)
if mibBuilder.loadTexts:
    logEntry.setStatus("current")
_LogIndex_Type = Unsigned32
_LogIndex_Object = MibTableColumn
logIndex = _LogIndex_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 601, 1, 1, 1),
    _LogIndex_Type()
)
logIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    logIndex.setStatus("current")
_LogDate_Type = DisplayString
_LogDate_Object = MibTableColumn
logDate = _LogDate_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 601, 1, 1, 2),
    _LogDate_Type()
)
logDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    logDate.setStatus("current")
_LogTime_Type = DisplayString
_LogTime_Object = MibTableColumn
logTime = _LogTime_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 601, 1, 1, 3),
    _LogTime_Type()
)
logTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    logTime.setStatus("current")
_LogFacility_Type = DisplayString
_LogFacility_Object = MibTableColumn
logFacility = _LogFacility_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 601, 1, 1, 4),
    _LogFacility_Type()
)
logFacility.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    logFacility.setStatus("current")
_LogSeverity_Type = DisplayString
_LogSeverity_Object = MibTableColumn
logSeverity = _LogSeverity_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 601, 1, 1, 5),
    _LogSeverity_Type()
)
logSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    logSeverity.setStatus("current")
_LogProgram_Type = DisplayString
_LogProgram_Object = MibTableColumn
logProgram = _LogProgram_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 601, 1, 1, 6),
    _LogProgram_Type()
)
logProgram.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    logProgram.setStatus("current")
_LogMessage_Type = DisplayString
_LogMessage_Object = MibTableColumn
logMessage = _LogMessage_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 601, 1, 1, 7),
    _LogMessage_Type()
)
logMessage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    logMessage.setStatus("current")
_LogOptions_ObjectIdentity = ObjectIdentity
logOptions = _LogOptions_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 601, 2)
)


class _LogSource_Type(Integer32):
    """Custom type logSource based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("bufferedLog", 1),
          ("permanentLog", 2))
    )


_LogSource_Type.__name__ = "Integer32"
_LogSource_Object = MibScalar
logSource = _LogSource_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 601, 2, 1),
    _LogSource_Type()
)
logSource.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    logSource.setStatus("current")


class _LogAll_Type(Integer32):
    """Custom type logAll based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_LogAll_Type.__name__ = "Integer32"
_LogAll_Object = MibScalar
logAll = _LogAll_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 601, 2, 2),
    _LogAll_Type()
)
logAll.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    logAll.setStatus("current")


class _ClearLog_Type(Integer32):
    """Custom type clearLog based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_ClearLog_Type.__name__ = "Integer32"
_ClearLog_Object = MibScalar
clearLog = _ClearLog_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 601, 2, 3),
    _ClearLog_Type()
)
clearLog.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clearLog.setStatus("current")
_LogProcessKilled_Type = DisplayString
_LogProcessKilled_Object = MibScalar
logProcessKilled = _LogProcessKilled_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 601, 3),
    _LogProcessKilled_Type()
)
logProcessKilled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    logProcessKilled.setStatus("current")

# Managed Objects groups


# Notification objects

logProcessKilledNotify = NotificationType(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 601, 0, 1)
)
logProcessKilledNotify.setObjects(
    ("AT-LOG-MIB", "logProcessKilled")
)
if mibBuilder.loadTexts:
    logProcessKilledNotify.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "AT-LOG-MIB",
    **{"log": log,
       "logNotifications": logNotifications,
       "logProcessKilledNotify": logProcessKilledNotify,
       "logTable": logTable,
       "logEntry": logEntry,
       "logIndex": logIndex,
       "logDate": logDate,
       "logTime": logTime,
       "logFacility": logFacility,
       "logSeverity": logSeverity,
       "logProgram": logProgram,
       "logMessage": logMessage,
       "logOptions": logOptions,
       "logSource": logSource,
       "logAll": logAll,
       "clearLog": clearLog,
       "logProcessKilled": logProcessKilled}
)
