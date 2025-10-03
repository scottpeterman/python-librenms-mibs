# SNMP MIB module (NSCRTV-HFCEMS-ALARMS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\cdata\NSCRTV-HFCEMS-ALARMS-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:47:47 2025
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

(commonNELogicalID,
 commonPhysAddress) = mibBuilder.importSymbols(
    "NSCRTV-HFCEMS-COMMON-MIB",
    "commonNELogicalID",
    "commonPhysAddress")

(alarmsIdent,
 nscrtvHFCemsTree) = mibBuilder.importSymbols(
    "NSCRTV-ROOT",
    "alarmsIdent",
    "nscrtvHFCemsTree")

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
 NotificationType,
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
    "NotificationType",
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


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AlarmLogNumberOfEntries_Type = Integer32
_AlarmLogNumberOfEntries_Object = MibScalar
alarmLogNumberOfEntries = _AlarmLogNumberOfEntries_Object(
    (1, 3, 6, 1, 4, 1, 17409, 1, 2, 1),
    _AlarmLogNumberOfEntries_Type()
)
alarmLogNumberOfEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmLogNumberOfEntries.setStatus("mandatory")
_AlarmLogLastIndex_Type = Integer32
_AlarmLogLastIndex_Object = MibScalar
alarmLogLastIndex = _AlarmLogLastIndex_Object(
    (1, 3, 6, 1, 4, 1, 17409, 1, 2, 2),
    _AlarmLogLastIndex_Type()
)
alarmLogLastIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmLogLastIndex.setStatus("mandatory")
_AlarmLogTable_Object = MibTable
alarmLogTable = _AlarmLogTable_Object(
    (1, 3, 6, 1, 4, 1, 17409, 1, 2, 3)
)
if mibBuilder.loadTexts:
    alarmLogTable.setStatus("mandatory")
_AlarmLogEntry_Object = MibTableRow
alarmLogEntry = _AlarmLogEntry_Object(
    (1, 3, 6, 1, 4, 1, 17409, 1, 2, 3, 1)
)
alarmLogEntry.setIndexNames(
    (0, "NSCRTV-HFCEMS-ALARMS-MIB", "alarmLogIndex"),
)
if mibBuilder.loadTexts:
    alarmLogEntry.setStatus("mandatory")


class _AlarmLogIndex_Type(Integer32):
    """Custom type alarmLogIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32767),
    )


_AlarmLogIndex_Type.__name__ = "Integer32"
_AlarmLogIndex_Object = MibTableColumn
alarmLogIndex = _AlarmLogIndex_Object(
    (1, 3, 6, 1, 4, 1, 17409, 1, 2, 3, 1, 1),
    _AlarmLogIndex_Type()
)
alarmLogIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmLogIndex.setStatus("mandatory")


class _AlarmLogInformation_Type(OctetString):
    """Custom type alarmLogInformation based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(17, 255),
    )


_AlarmLogInformation_Type.__name__ = "OctetString"
_AlarmLogInformation_Object = MibTableColumn
alarmLogInformation = _AlarmLogInformation_Object(
    (1, 3, 6, 1, 4, 1, 17409, 1, 2, 3, 1, 2),
    _AlarmLogInformation_Type()
)
alarmLogInformation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmLogInformation.setStatus("mandatory")
_AlarmText_Type = DisplayString
_AlarmText_Object = MibScalar
alarmText = _AlarmText_Object(
    (1, 3, 6, 1, 4, 1, 17409, 1, 2, 4),
    _AlarmText_Type()
)
alarmText.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmText.setStatus("optional")

# Managed Objects groups


# Notification objects

hfcAlarmEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 17409, 1, 0, 1)
)
hfcAlarmEvent.setObjects(
      *(("NSCRTV-HFCEMS-COMMON-MIB", "commonPhysAddress"),
        ("NSCRTV-HFCEMS-COMMON-MIB", "commonNELogicalID"),
        ("NSCRTV-HFCEMS-ALARMS-MIB", "alarmLogInformation"),
        ("NSCRTV-HFCEMS-ALARMS-MIB", "alarmText"))
)
if mibBuilder.loadTexts:
    hfcAlarmEvent.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "NSCRTV-HFCEMS-ALARMS-MIB",
    **{"hfcAlarmEvent": hfcAlarmEvent,
       "alarmLogNumberOfEntries": alarmLogNumberOfEntries,
       "alarmLogLastIndex": alarmLogLastIndex,
       "alarmLogTable": alarmLogTable,
       "alarmLogEntry": alarmLogEntry,
       "alarmLogIndex": alarmLogIndex,
       "alarmLogInformation": alarmLogInformation,
       "alarmText": alarmText}
)
