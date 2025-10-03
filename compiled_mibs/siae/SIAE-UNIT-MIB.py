# SNMP MIB module (SIAE-UNIT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\siae\SIAE-UNIT-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 12:27:50 2025
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

(unitTypeUnequipped,) = mibBuilder.importSymbols(
    "SIAE-UNITYPE-MIB",
    "unitTypeUnequipped")

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

(AutonomousType,
 DisplayString,
 PhysAddress,
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "AutonomousType",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

unit = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 6)
)
if mibBuilder.loadTexts:
    unit.setRevisions(
        ("2014-02-03 00:00",
         "2013-04-16 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs



class _UnitMibVersion_Type(Integer32):
    """Custom type unitMibVersion based on Integer32"""
    defaultValue = 1


_UnitMibVersion_Type.__name__ = "Integer32"
_UnitMibVersion_Object = MibScalar
unitMibVersion = _UnitMibVersion_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 6, 1),
    _UnitMibVersion_Type()
)
unitMibVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    unitMibVersion.setStatus("current")
_UnitTable_Object = MibTable
unitTable = _UnitTable_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 6, 2)
)
if mibBuilder.loadTexts:
    unitTable.setStatus("current")
_UnitRecord_Object = MibTableRow
unitRecord = _UnitRecord_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 6, 2, 1)
)
unitRecord.setIndexNames(
    (0, "SIAE-UNIT-MIB", "unitId"),
)
if mibBuilder.loadTexts:
    unitRecord.setStatus("current")
_UnitId_Type = Integer32
_UnitId_Object = MibTableColumn
unitId = _UnitId_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 6, 2, 1, 1),
    _UnitId_Type()
)
unitId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    unitId.setStatus("current")


class _UnitExpectedType_Type(AutonomousType):
    """Custom type unitExpectedType based on AutonomousType"""
    defaultValue = (1, 3, 6, 1, 4, 1, 3373, 1103, 6, 3, 1)


_UnitExpectedType_Type.__name__ = "AutonomousType"
_UnitExpectedType_Object = MibTableColumn
unitExpectedType = _UnitExpectedType_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 6, 2, 1, 2),
    _UnitExpectedType_Type()
)
unitExpectedType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    unitExpectedType.setStatus("current")


class _UnitActualType_Type(AutonomousType):
    """Custom type unitActualType based on AutonomousType"""
    defaultValue = (1, 3, 6, 1, 4, 1, 3373, 1103, 6, 3, 1)


_UnitActualType_Type.__name__ = "AutonomousType"
_UnitActualType_Object = MibTableColumn
unitActualType = _UnitActualType_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 6, 2, 1, 3),
    _UnitActualType_Type()
)
unitActualType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    unitActualType.setStatus("current")


class _UnitLabel_Type(DisplayString):
    """Custom type unitLabel based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 30),
    )


_UnitLabel_Type.__name__ = "DisplayString"
_UnitLabel_Object = MibTableColumn
unitLabel = _UnitLabel_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 6, 2, 1, 4),
    _UnitLabel_Type()
)
unitLabel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    unitLabel.setStatus("current")


class _UnitFailAlarm_Type(AlarmStatus):
    """Custom type unitFailAlarm based on AlarmStatus"""
    defaultValue = 5


_UnitFailAlarm_Type.__name__ = "AlarmStatus"
_UnitFailAlarm_Object = MibTableColumn
unitFailAlarm = _UnitFailAlarm_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 6, 2, 1, 5),
    _UnitFailAlarm_Type()
)
unitFailAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    unitFailAlarm.setStatus("current")


class _UnitMissingAlarm_Type(AlarmStatus):
    """Custom type unitMissingAlarm based on AlarmStatus"""
    defaultValue = 5


_UnitMissingAlarm_Type.__name__ = "AlarmStatus"
_UnitMissingAlarm_Object = MibTableColumn
unitMissingAlarm = _UnitMissingAlarm_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 6, 2, 1, 6),
    _UnitMissingAlarm_Type()
)
unitMissingAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    unitMissingAlarm.setStatus("current")


class _UnitNotRespondingAlarm_Type(AlarmStatus):
    """Custom type unitNotRespondingAlarm based on AlarmStatus"""
    defaultValue = 5


_UnitNotRespondingAlarm_Type.__name__ = "AlarmStatus"
_UnitNotRespondingAlarm_Object = MibTableColumn
unitNotRespondingAlarm = _UnitNotRespondingAlarm_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 6, 2, 1, 7),
    _UnitNotRespondingAlarm_Type()
)
unitNotRespondingAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    unitNotRespondingAlarm.setStatus("current")


class _UnitHwMismatchAlarm_Type(AlarmStatus):
    """Custom type unitHwMismatchAlarm based on AlarmStatus"""
    defaultValue = 5


_UnitHwMismatchAlarm_Type.__name__ = "AlarmStatus"
_UnitHwMismatchAlarm_Object = MibTableColumn
unitHwMismatchAlarm = _UnitHwMismatchAlarm_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 6, 2, 1, 8),
    _UnitHwMismatchAlarm_Type()
)
unitHwMismatchAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    unitHwMismatchAlarm.setStatus("current")


class _UnitSwMismatchAlarm_Type(AlarmStatus):
    """Custom type unitSwMismatchAlarm based on AlarmStatus"""
    defaultValue = 5


_UnitSwMismatchAlarm_Type.__name__ = "AlarmStatus"
_UnitSwMismatchAlarm_Object = MibTableColumn
unitSwMismatchAlarm = _UnitSwMismatchAlarm_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 6, 2, 1, 9),
    _UnitSwMismatchAlarm_Type()
)
unitSwMismatchAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    unitSwMismatchAlarm.setStatus("current")


class _UnitHwEdition_Type(DisplayString):
    """Custom type unitHwEdition based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_UnitHwEdition_Type.__name__ = "DisplayString"
_UnitHwEdition_Object = MibTableColumn
unitHwEdition = _UnitHwEdition_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 6, 2, 1, 10),
    _UnitHwEdition_Type()
)
unitHwEdition.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    unitHwEdition.setStatus("current")


class _UnitPartNumber_Type(DisplayString):
    """Custom type unitPartNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 30),
    )


_UnitPartNumber_Type.__name__ = "DisplayString"
_UnitPartNumber_Object = MibTableColumn
unitPartNumber = _UnitPartNumber_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 6, 2, 1, 11),
    _UnitPartNumber_Type()
)
unitPartNumber.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    unitPartNumber.setStatus("current")


class _UnitParentPartNumber_Type(DisplayString):
    """Custom type unitParentPartNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 30),
    )


_UnitParentPartNumber_Type.__name__ = "DisplayString"
_UnitParentPartNumber_Object = MibTableColumn
unitParentPartNumber = _UnitParentPartNumber_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 6, 2, 1, 12),
    _UnitParentPartNumber_Type()
)
unitParentPartNumber.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    unitParentPartNumber.setStatus("current")


class _UnitParentSerialNumber_Type(DisplayString):
    """Custom type unitParentSerialNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 30),
    )


_UnitParentSerialNumber_Type.__name__ = "DisplayString"
_UnitParentSerialNumber_Object = MibTableColumn
unitParentSerialNumber = _UnitParentSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 6, 2, 1, 13),
    _UnitParentSerialNumber_Type()
)
unitParentSerialNumber.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    unitParentSerialNumber.setStatus("current")
_UnitRowStatus_Type = RowStatus
_UnitRowStatus_Object = MibTableColumn
unitRowStatus = _UnitRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 6, 2, 1, 14),
    _UnitRowStatus_Type()
)
unitRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    unitRowStatus.setStatus("current")


class _UnitFailAlarmSeverityCode_Type(AlarmSeverityCode):
    """Custom type unitFailAlarmSeverityCode based on AlarmSeverityCode"""
    defaultValue = 5


_UnitFailAlarmSeverityCode_Type.__name__ = "AlarmSeverityCode"
_UnitFailAlarmSeverityCode_Object = MibScalar
unitFailAlarmSeverityCode = _UnitFailAlarmSeverityCode_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 6, 4),
    _UnitFailAlarmSeverityCode_Type()
)
unitFailAlarmSeverityCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    unitFailAlarmSeverityCode.setStatus("current")


class _UnitMissingAlarmSeverityCode_Type(AlarmSeverityCode):
    """Custom type unitMissingAlarmSeverityCode based on AlarmSeverityCode"""
    defaultValue = 5


_UnitMissingAlarmSeverityCode_Type.__name__ = "AlarmSeverityCode"
_UnitMissingAlarmSeverityCode_Object = MibScalar
unitMissingAlarmSeverityCode = _UnitMissingAlarmSeverityCode_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 6, 5),
    _UnitMissingAlarmSeverityCode_Type()
)
unitMissingAlarmSeverityCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    unitMissingAlarmSeverityCode.setStatus("current")


class _UnitNotRespondingAlarmSeverityCode_Type(AlarmSeverityCode):
    """Custom type unitNotRespondingAlarmSeverityCode based on AlarmSeverityCode"""
    defaultValue = 5


_UnitNotRespondingAlarmSeverityCode_Type.__name__ = "AlarmSeverityCode"
_UnitNotRespondingAlarmSeverityCode_Object = MibScalar
unitNotRespondingAlarmSeverityCode = _UnitNotRespondingAlarmSeverityCode_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 6, 6),
    _UnitNotRespondingAlarmSeverityCode_Type()
)
unitNotRespondingAlarmSeverityCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    unitNotRespondingAlarmSeverityCode.setStatus("current")


class _UnitHwMismatchAlarmSeverityCode_Type(AlarmSeverityCode):
    """Custom type unitHwMismatchAlarmSeverityCode based on AlarmSeverityCode"""
    defaultValue = 5


_UnitHwMismatchAlarmSeverityCode_Type.__name__ = "AlarmSeverityCode"
_UnitHwMismatchAlarmSeverityCode_Object = MibScalar
unitHwMismatchAlarmSeverityCode = _UnitHwMismatchAlarmSeverityCode_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 6, 7),
    _UnitHwMismatchAlarmSeverityCode_Type()
)
unitHwMismatchAlarmSeverityCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    unitHwMismatchAlarmSeverityCode.setStatus("current")


class _UnitSwMismatchAlarmSeverityCode_Type(AlarmSeverityCode):
    """Custom type unitSwMismatchAlarmSeverityCode based on AlarmSeverityCode"""
    defaultValue = 5


_UnitSwMismatchAlarmSeverityCode_Type.__name__ = "AlarmSeverityCode"
_UnitSwMismatchAlarmSeverityCode_Object = MibScalar
unitSwMismatchAlarmSeverityCode = _UnitSwMismatchAlarmSeverityCode_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 6, 8),
    _UnitSwMismatchAlarmSeverityCode_Type()
)
unitSwMismatchAlarmSeverityCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    unitSwMismatchAlarmSeverityCode.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SIAE-UNIT-MIB",
    **{"unit": unit,
       "unitMibVersion": unitMibVersion,
       "unitTable": unitTable,
       "unitRecord": unitRecord,
       "unitId": unitId,
       "unitExpectedType": unitExpectedType,
       "unitActualType": unitActualType,
       "unitLabel": unitLabel,
       "unitFailAlarm": unitFailAlarm,
       "unitMissingAlarm": unitMissingAlarm,
       "unitNotRespondingAlarm": unitNotRespondingAlarm,
       "unitHwMismatchAlarm": unitHwMismatchAlarm,
       "unitSwMismatchAlarm": unitSwMismatchAlarm,
       "unitHwEdition": unitHwEdition,
       "unitPartNumber": unitPartNumber,
       "unitParentPartNumber": unitParentPartNumber,
       "unitParentSerialNumber": unitParentSerialNumber,
       "unitRowStatus": unitRowStatus,
       "unitFailAlarmSeverityCode": unitFailAlarmSeverityCode,
       "unitMissingAlarmSeverityCode": unitMissingAlarmSeverityCode,
       "unitNotRespondingAlarmSeverityCode": unitNotRespondingAlarmSeverityCode,
       "unitHwMismatchAlarmSeverityCode": unitHwMismatchAlarmSeverityCode,
       "unitSwMismatchAlarmSeverityCode": unitSwMismatchAlarmSeverityCode}
)
