# SNMP MIB module (SIAE-QUEUE-DEPTH-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\siae\SIAE-QUEUE-DEPTH-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 12:27:27 2025
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

(AlarmSeverityCode,
 AlarmStatus) = mibBuilder.importSymbols(
    "SIAE-ALARM-MIB",
    "AlarmSeverityCode",
    "AlarmStatus")

(siaeMib,) = mibBuilder.importSymbols(
    "SIAE-TREE-MIB",
    "siaeMib")

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

queueDepth = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 84)
)
if mibBuilder.loadTexts:
    queueDepth.setRevisions(
        ("2014-05-20 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class DisplayString1024(TextualConvention, OctetString):
    status = "current"
    displayHint = "1024a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 1024),
    )



# MIB Managed Objects in the order of their OIDs

_QueueDepthMibVersion_Type = Integer32
_QueueDepthMibVersion_Object = MibScalar
queueDepthMibVersion = _QueueDepthMibVersion_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 84, 1),
    _QueueDepthMibVersion_Type()
)
queueDepthMibVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    queueDepthMibVersion.setStatus("current")
_QdProfileTable_Object = MibTable
qdProfileTable = _QdProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 84, 2)
)
if mibBuilder.loadTexts:
    qdProfileTable.setStatus("current")
_QdProfileEntry_Object = MibTableRow
qdProfileEntry = _QdProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 84, 2, 1)
)
qdProfileEntry.setIndexNames(
    (0, "SIAE-QUEUE-DEPTH-MIB", "qdProfileIndex"),
)
if mibBuilder.loadTexts:
    qdProfileEntry.setStatus("current")
_QdProfileIndex_Type = Integer32
_QdProfileIndex_Object = MibTableColumn
qdProfileIndex = _QdProfileIndex_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 84, 2, 1, 1),
    _QdProfileIndex_Type()
)
qdProfileIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qdProfileIndex.setStatus("current")


class _QdProfileName_Type(DisplayString):
    """Custom type qdProfileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_QdProfileName_Type.__name__ = "DisplayString"
_QdProfileName_Object = MibTableColumn
qdProfileName = _QdProfileName_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 84, 2, 1, 2),
    _QdProfileName_Type()
)
qdProfileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qdProfileName.setStatus("current")
_QdProfileDescription_Type = DisplayString1024
_QdProfileDescription_Object = MibTableColumn
qdProfileDescription = _QdProfileDescription_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 84, 2, 1, 3),
    _QdProfileDescription_Type()
)
qdProfileDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qdProfileDescription.setStatus("current")


class _QdProfileSelect_Type(Integer32):
    """Custom type qdProfileSelect based on Integer32"""
    defaultValue = 1


_QdProfileSelect_Type.__name__ = "Integer32"
_QdProfileSelect_Object = MibScalar
qdProfileSelect = _QdProfileSelect_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 84, 3),
    _QdProfileSelect_Type()
)
qdProfileSelect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qdProfileSelect.setStatus("current")
_QdActualProfile_Type = Integer32
_QdActualProfile_Object = MibScalar
qdActualProfile = _QdActualProfile_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 84, 4),
    _QdActualProfile_Type()
)
qdActualProfile.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qdActualProfile.setStatus("current")
_QdProfileMismatchAlarm_Type = AlarmStatus
_QdProfileMismatchAlarm_Object = MibScalar
qdProfileMismatchAlarm = _QdProfileMismatchAlarm_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 84, 5),
    _QdProfileMismatchAlarm_Type()
)
qdProfileMismatchAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qdProfileMismatchAlarm.setStatus("current")


class _QdProfileMismatchAlarmSeverityCode_Type(AlarmSeverityCode):
    """Custom type qdProfileMismatchAlarmSeverityCode based on AlarmSeverityCode"""
    defaultValue = 3


_QdProfileMismatchAlarmSeverityCode_Type.__name__ = "AlarmSeverityCode"
_QdProfileMismatchAlarmSeverityCode_Object = MibScalar
qdProfileMismatchAlarmSeverityCode = _QdProfileMismatchAlarmSeverityCode_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 84, 6),
    _QdProfileMismatchAlarmSeverityCode_Type()
)
qdProfileMismatchAlarmSeverityCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qdProfileMismatchAlarmSeverityCode.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SIAE-QUEUE-DEPTH-MIB",
    **{"DisplayString1024": DisplayString1024,
       "queueDepth": queueDepth,
       "queueDepthMibVersion": queueDepthMibVersion,
       "qdProfileTable": qdProfileTable,
       "qdProfileEntry": qdProfileEntry,
       "qdProfileIndex": qdProfileIndex,
       "qdProfileName": qdProfileName,
       "qdProfileDescription": qdProfileDescription,
       "qdProfileSelect": qdProfileSelect,
       "qdActualProfile": qdActualProfile,
       "qdProfileMismatchAlarm": qdProfileMismatchAlarm,
       "qdProfileMismatchAlarmSeverityCode": qdProfileMismatchAlarmSeverityCode}
)
