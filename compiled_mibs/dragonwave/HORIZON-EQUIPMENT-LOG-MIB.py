# SNMP MIB module (HORIZON-EQUIPMENT-LOG-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\dragonwave\HORIZON-EQUIPMENT-LOG-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:38:26 2025
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

(horizon,) = mibBuilder.importSymbols(
    "HORIZON-MIB",
    "horizon")

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
 TimeStamp) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TimeStamp")


# MODULE-IDENTITY

horizonEquipmentLogMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 7262, 2, 100)
)
if mibBuilder.loadTexts:
    horizonEquipmentLogMib.setRevisions(
        ("2009-01-21 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class EnableType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )



# MIB Managed Objects in the order of their OIDs

_HorizonEquipmentLogMibObjects_ObjectIdentity = ObjectIdentity
horizonEquipmentLogMibObjects = _HorizonEquipmentLogMibObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7262, 2, 100, 1)
)
_HorizonEquipmentConfigLog_ObjectIdentity = ObjectIdentity
horizonEquipmentConfigLog = _HorizonEquipmentConfigLog_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7262, 2, 100, 1, 1)
)


class _HorizonEquipmentEventLogEntryLimit_Type(Unsigned32):
    """Custom type horizonEquipmentEventLogEntryLimit based on Unsigned32"""
    defaultValue = 4096


_HorizonEquipmentEventLogEntryLimit_Type.__name__ = "Unsigned32"
_HorizonEquipmentEventLogEntryLimit_Object = MibScalar
horizonEquipmentEventLogEntryLimit = _HorizonEquipmentEventLogEntryLimit_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 100, 1, 1, 1),
    _HorizonEquipmentEventLogEntryLimit_Type()
)
horizonEquipmentEventLogEntryLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    horizonEquipmentEventLogEntryLimit.setStatus("current")
_HorizonEquipmentLog_ObjectIdentity = ObjectIdentity
horizonEquipmentLog = _HorizonEquipmentLog_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7262, 2, 100, 1, 2)
)
_HorizonEquipmentEventLogLastEntry_Type = Unsigned32
_HorizonEquipmentEventLogLastEntry_Object = MibScalar
horizonEquipmentEventLogLastEntry = _HorizonEquipmentEventLogLastEntry_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 100, 1, 2, 1),
    _HorizonEquipmentEventLogLastEntry_Type()
)
horizonEquipmentEventLogLastEntry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    horizonEquipmentEventLogLastEntry.setStatus("current")
_HorizonEquipmentEventLogTable_Object = MibTable
horizonEquipmentEventLogTable = _HorizonEquipmentEventLogTable_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 100, 1, 2, 2)
)
if mibBuilder.loadTexts:
    horizonEquipmentEventLogTable.setStatus("current")
_HorizonEquipmentEventLogEntry_Object = MibTableRow
horizonEquipmentEventLogEntry = _HorizonEquipmentEventLogEntry_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 100, 1, 2, 2, 1)
)
horizonEquipmentEventLogEntry.setIndexNames(
    (0, "HORIZON-EQUIPMENT-LOG-MIB", "horizonEquipmentEventLogIndex"),
)
if mibBuilder.loadTexts:
    horizonEquipmentEventLogEntry.setStatus("current")


class _HorizonEquipmentEventLogIndex_Type(Unsigned32):
    """Custom type horizonEquipmentEventLogIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_HorizonEquipmentEventLogIndex_Type.__name__ = "Unsigned32"
_HorizonEquipmentEventLogIndex_Object = MibTableColumn
horizonEquipmentEventLogIndex = _HorizonEquipmentEventLogIndex_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 100, 1, 2, 2, 1, 1),
    _HorizonEquipmentEventLogIndex_Type()
)
horizonEquipmentEventLogIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    horizonEquipmentEventLogIndex.setStatus("current")
_HorizonEquipmentEventLogTime_Type = TimeStamp
_HorizonEquipmentEventLogTime_Object = MibTableColumn
horizonEquipmentEventLogTime = _HorizonEquipmentEventLogTime_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 100, 1, 2, 2, 1, 2),
    _HorizonEquipmentEventLogTime_Type()
)
horizonEquipmentEventLogTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    horizonEquipmentEventLogTime.setStatus("current")
_HorizonEquipmentEventLogDateAndTime_Type = DateAndTime
_HorizonEquipmentEventLogDateAndTime_Object = MibTableColumn
horizonEquipmentEventLogDateAndTime = _HorizonEquipmentEventLogDateAndTime_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 100, 1, 2, 2, 1, 3),
    _HorizonEquipmentEventLogDateAndTime_Type()
)
horizonEquipmentEventLogDateAndTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    horizonEquipmentEventLogDateAndTime.setStatus("current")
_HorizonEquipmentEventLogNotificationID_Type = ObjectIdentifier
_HorizonEquipmentEventLogNotificationID_Object = MibTableColumn
horizonEquipmentEventLogNotificationID = _HorizonEquipmentEventLogNotificationID_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 100, 1, 2, 2, 1, 4),
    _HorizonEquipmentEventLogNotificationID_Type()
)
horizonEquipmentEventLogNotificationID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    horizonEquipmentEventLogNotificationID.setStatus("current")
_HorizonEquipmentEventLogVariables_Type = Unsigned32
_HorizonEquipmentEventLogVariables_Object = MibTableColumn
horizonEquipmentEventLogVariables = _HorizonEquipmentEventLogVariables_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 100, 1, 2, 2, 1, 5),
    _HorizonEquipmentEventLogVariables_Type()
)
horizonEquipmentEventLogVariables.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    horizonEquipmentEventLogVariables.setStatus("current")
_HorizonEquipmentEventLogVariableTable_Object = MibTable
horizonEquipmentEventLogVariableTable = _HorizonEquipmentEventLogVariableTable_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 100, 1, 2, 3)
)
if mibBuilder.loadTexts:
    horizonEquipmentEventLogVariableTable.setStatus("current")
_HorizonEquipmentEventLogVariableEntry_Object = MibTableRow
horizonEquipmentEventLogVariableEntry = _HorizonEquipmentEventLogVariableEntry_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 100, 1, 2, 3, 1)
)
horizonEquipmentEventLogVariableEntry.setIndexNames(
    (0, "HORIZON-EQUIPMENT-LOG-MIB", "horizonEquipmentEventLogIndex"),
    (0, "HORIZON-EQUIPMENT-LOG-MIB", "horizonEquipmentEventLogVariableIndex"),
)
if mibBuilder.loadTexts:
    horizonEquipmentEventLogVariableEntry.setStatus("current")


class _HorizonEquipmentEventLogVariableIndex_Type(Unsigned32):
    """Custom type horizonEquipmentEventLogVariableIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_HorizonEquipmentEventLogVariableIndex_Type.__name__ = "Unsigned32"
_HorizonEquipmentEventLogVariableIndex_Object = MibTableColumn
horizonEquipmentEventLogVariableIndex = _HorizonEquipmentEventLogVariableIndex_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 100, 1, 2, 3, 1, 1),
    _HorizonEquipmentEventLogVariableIndex_Type()
)
horizonEquipmentEventLogVariableIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    horizonEquipmentEventLogVariableIndex.setStatus("current")
_HorizonEquipmentEventLogVariableID_Type = ObjectIdentifier
_HorizonEquipmentEventLogVariableID_Object = MibTableColumn
horizonEquipmentEventLogVariableID = _HorizonEquipmentEventLogVariableID_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 100, 1, 2, 3, 1, 2),
    _HorizonEquipmentEventLogVariableID_Type()
)
horizonEquipmentEventLogVariableID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    horizonEquipmentEventLogVariableID.setStatus("current")


class _HorizonEquipmentEventLogVariableValueType_Type(Integer32):
    """Custom type horizonEquipmentEventLogVariableValueType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8)
        )
    )
    namedValues = NamedValues(
        *(("counter32", 1),
          ("unsigned32", 2),
          ("timeTicks", 3),
          ("integer32", 4),
          ("ipAddress", 5),
          ("octetString", 6),
          ("objectId", 7),
          ("counter64", 8))
    )


_HorizonEquipmentEventLogVariableValueType_Type.__name__ = "Integer32"
_HorizonEquipmentEventLogVariableValueType_Object = MibTableColumn
horizonEquipmentEventLogVariableValueType = _HorizonEquipmentEventLogVariableValueType_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 100, 1, 2, 3, 1, 3),
    _HorizonEquipmentEventLogVariableValueType_Type()
)
horizonEquipmentEventLogVariableValueType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    horizonEquipmentEventLogVariableValueType.setStatus("current")
_HorizonEquipmentEventLogVariableCounter32Val_Type = Counter32
_HorizonEquipmentEventLogVariableCounter32Val_Object = MibTableColumn
horizonEquipmentEventLogVariableCounter32Val = _HorizonEquipmentEventLogVariableCounter32Val_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 100, 1, 2, 3, 1, 4),
    _HorizonEquipmentEventLogVariableCounter32Val_Type()
)
horizonEquipmentEventLogVariableCounter32Val.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    horizonEquipmentEventLogVariableCounter32Val.setStatus("current")
_HorizonEquipmentEventLogVariableUnsigned32Val_Type = Unsigned32
_HorizonEquipmentEventLogVariableUnsigned32Val_Object = MibTableColumn
horizonEquipmentEventLogVariableUnsigned32Val = _HorizonEquipmentEventLogVariableUnsigned32Val_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 100, 1, 2, 3, 1, 5),
    _HorizonEquipmentEventLogVariableUnsigned32Val_Type()
)
horizonEquipmentEventLogVariableUnsigned32Val.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    horizonEquipmentEventLogVariableUnsigned32Val.setStatus("current")
_HorizonEquipmentEventLogVariableTimeTicksVal_Type = TimeTicks
_HorizonEquipmentEventLogVariableTimeTicksVal_Object = MibTableColumn
horizonEquipmentEventLogVariableTimeTicksVal = _HorizonEquipmentEventLogVariableTimeTicksVal_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 100, 1, 2, 3, 1, 6),
    _HorizonEquipmentEventLogVariableTimeTicksVal_Type()
)
horizonEquipmentEventLogVariableTimeTicksVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    horizonEquipmentEventLogVariableTimeTicksVal.setStatus("current")
_HorizonEquipmentEventLogVariableInteger32Val_Type = Integer32
_HorizonEquipmentEventLogVariableInteger32Val_Object = MibTableColumn
horizonEquipmentEventLogVariableInteger32Val = _HorizonEquipmentEventLogVariableInteger32Val_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 100, 1, 2, 3, 1, 7),
    _HorizonEquipmentEventLogVariableInteger32Val_Type()
)
horizonEquipmentEventLogVariableInteger32Val.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    horizonEquipmentEventLogVariableInteger32Val.setStatus("current")
_HorizonEquipmentEventLogVariableOctetStringVal_Type = OctetString
_HorizonEquipmentEventLogVariableOctetStringVal_Object = MibTableColumn
horizonEquipmentEventLogVariableOctetStringVal = _HorizonEquipmentEventLogVariableOctetStringVal_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 100, 1, 2, 3, 1, 8),
    _HorizonEquipmentEventLogVariableOctetStringVal_Type()
)
horizonEquipmentEventLogVariableOctetStringVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    horizonEquipmentEventLogVariableOctetStringVal.setStatus("current")
_HorizonEquipmentEventLogVariableIpAddressVal_Type = IpAddress
_HorizonEquipmentEventLogVariableIpAddressVal_Object = MibTableColumn
horizonEquipmentEventLogVariableIpAddressVal = _HorizonEquipmentEventLogVariableIpAddressVal_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 100, 1, 2, 3, 1, 9),
    _HorizonEquipmentEventLogVariableIpAddressVal_Type()
)
horizonEquipmentEventLogVariableIpAddressVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    horizonEquipmentEventLogVariableIpAddressVal.setStatus("current")
_HorizonEquipmentEventLogVariableOidVal_Type = ObjectIdentifier
_HorizonEquipmentEventLogVariableOidVal_Object = MibTableColumn
horizonEquipmentEventLogVariableOidVal = _HorizonEquipmentEventLogVariableOidVal_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 100, 1, 2, 3, 1, 10),
    _HorizonEquipmentEventLogVariableOidVal_Type()
)
horizonEquipmentEventLogVariableOidVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    horizonEquipmentEventLogVariableOidVal.setStatus("current")
_HorizonEquipmentEventLogVariableCounter64Val_Type = Counter64
_HorizonEquipmentEventLogVariableCounter64Val_Object = MibTableColumn
horizonEquipmentEventLogVariableCounter64Val = _HorizonEquipmentEventLogVariableCounter64Val_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 100, 1, 2, 3, 1, 11),
    _HorizonEquipmentEventLogVariableCounter64Val_Type()
)
horizonEquipmentEventLogVariableCounter64Val.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    horizonEquipmentEventLogVariableCounter64Val.setStatus("current")
_HorizonEquipmentAlarmList_ObjectIdentity = ObjectIdentity
horizonEquipmentAlarmList = _HorizonEquipmentAlarmList_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7262, 2, 100, 1, 3)
)
_HorizonEquipmentAlarmActiveLastChanged_Type = TimeTicks
_HorizonEquipmentAlarmActiveLastChanged_Object = MibScalar
horizonEquipmentAlarmActiveLastChanged = _HorizonEquipmentAlarmActiveLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 100, 1, 3, 1),
    _HorizonEquipmentAlarmActiveLastChanged_Type()
)
horizonEquipmentAlarmActiveLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    horizonEquipmentAlarmActiveLastChanged.setStatus("current")
_HorizonEquipmentAlarmActiveRowCounter_Type = Counter32
_HorizonEquipmentAlarmActiveRowCounter_Object = MibScalar
horizonEquipmentAlarmActiveRowCounter = _HorizonEquipmentAlarmActiveRowCounter_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 100, 1, 3, 2),
    _HorizonEquipmentAlarmActiveRowCounter_Type()
)
horizonEquipmentAlarmActiveRowCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    horizonEquipmentAlarmActiveRowCounter.setStatus("current")
_HorizonEquipmentAlarmActiveTable_Object = MibTable
horizonEquipmentAlarmActiveTable = _HorizonEquipmentAlarmActiveTable_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 100, 1, 3, 3)
)
if mibBuilder.loadTexts:
    horizonEquipmentAlarmActiveTable.setStatus("current")
_HorizonEquipmentAlarmActiveEntry_Object = MibTableRow
horizonEquipmentAlarmActiveEntry = _HorizonEquipmentAlarmActiveEntry_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 100, 1, 3, 3, 1)
)
horizonEquipmentAlarmActiveEntry.setIndexNames(
    (0, "HORIZON-EQUIPMENT-LOG-MIB", "horizonEquipmentAlarmActiveTime"),
    (0, "HORIZON-EQUIPMENT-LOG-MIB", "horizonEquipmentAlarmActiveIndex"),
)
if mibBuilder.loadTexts:
    horizonEquipmentAlarmActiveEntry.setStatus("current")


class _HorizonEquipmentAlarmActiveIndex_Type(Unsigned32):
    """Custom type horizonEquipmentAlarmActiveIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_HorizonEquipmentAlarmActiveIndex_Type.__name__ = "Unsigned32"
_HorizonEquipmentAlarmActiveIndex_Object = MibTableColumn
horizonEquipmentAlarmActiveIndex = _HorizonEquipmentAlarmActiveIndex_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 100, 1, 3, 3, 1, 1),
    _HorizonEquipmentAlarmActiveIndex_Type()
)
horizonEquipmentAlarmActiveIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    horizonEquipmentAlarmActiveIndex.setStatus("current")
_HorizonEquipmentAlarmActiveTime_Type = TimeStamp
_HorizonEquipmentAlarmActiveTime_Object = MibTableColumn
horizonEquipmentAlarmActiveTime = _HorizonEquipmentAlarmActiveTime_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 100, 1, 3, 3, 1, 2),
    _HorizonEquipmentAlarmActiveTime_Type()
)
horizonEquipmentAlarmActiveTime.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    horizonEquipmentAlarmActiveTime.setStatus("current")
_HorizonEquipmentAlarmActiveDateAndTime_Type = DateAndTime
_HorizonEquipmentAlarmActiveDateAndTime_Object = MibTableColumn
horizonEquipmentAlarmActiveDateAndTime = _HorizonEquipmentAlarmActiveDateAndTime_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 100, 1, 3, 3, 1, 3),
    _HorizonEquipmentAlarmActiveDateAndTime_Type()
)
horizonEquipmentAlarmActiveDateAndTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    horizonEquipmentAlarmActiveDateAndTime.setStatus("current")
_HorizonEquipmentAlarmActiveSourceID_Type = ObjectIdentifier
_HorizonEquipmentAlarmActiveSourceID_Object = MibTableColumn
horizonEquipmentAlarmActiveSourceID = _HorizonEquipmentAlarmActiveSourceID_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 100, 1, 3, 3, 1, 4),
    _HorizonEquipmentAlarmActiveSourceID_Type()
)
horizonEquipmentAlarmActiveSourceID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    horizonEquipmentAlarmActiveSourceID.setStatus("current")
_HorizonEquipmentSnmpTrap_ObjectIdentity = ObjectIdentity
horizonEquipmentSnmpTrap = _HorizonEquipmentSnmpTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7262, 2, 100, 1, 4)
)
_HorizonEquipmentOutTrapsCounter_Type = Counter32
_HorizonEquipmentOutTrapsCounter_Object = MibScalar
horizonEquipmentOutTrapsCounter = _HorizonEquipmentOutTrapsCounter_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 100, 1, 4, 1),
    _HorizonEquipmentOutTrapsCounter_Type()
)
horizonEquipmentOutTrapsCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    horizonEquipmentOutTrapsCounter.setStatus("current")
_HorizonEquipmentLastOutTrapTimeStamp_Type = TimeStamp
_HorizonEquipmentLastOutTrapTimeStamp_Object = MibScalar
horizonEquipmentLastOutTrapTimeStamp = _HorizonEquipmentLastOutTrapTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 100, 1, 4, 2),
    _HorizonEquipmentLastOutTrapTimeStamp_Type()
)
horizonEquipmentLastOutTrapTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    horizonEquipmentLastOutTrapTimeStamp.setStatus("current")
_HorizonEquipmentTrapDestTable_Object = MibTable
horizonEquipmentTrapDestTable = _HorizonEquipmentTrapDestTable_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 100, 1, 4, 4)
)
if mibBuilder.loadTexts:
    horizonEquipmentTrapDestTable.setStatus("current")
_HorizonEquipmentTrapDestEntry_Object = MibTableRow
horizonEquipmentTrapDestEntry = _HorizonEquipmentTrapDestEntry_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 100, 1, 4, 4, 1)
)
horizonEquipmentTrapDestEntry.setIndexNames(
    (0, "HORIZON-EQUIPMENT-LOG-MIB", "horizonEquipmentTrapDestAddress"),
)
if mibBuilder.loadTexts:
    horizonEquipmentTrapDestEntry.setStatus("current")
_HorizonEquipmentTrapDestAddress_Type = IpAddress
_HorizonEquipmentTrapDestAddress_Object = MibTableColumn
horizonEquipmentTrapDestAddress = _HorizonEquipmentTrapDestAddress_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 100, 1, 4, 4, 1, 1),
    _HorizonEquipmentTrapDestAddress_Type()
)
horizonEquipmentTrapDestAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    horizonEquipmentTrapDestAddress.setStatus("current")


class _HorizonEquipmentTrapDestCommString_Type(OctetString):
    """Custom type horizonEquipmentTrapDestCommString based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 24),
    )


_HorizonEquipmentTrapDestCommString_Type.__name__ = "OctetString"
_HorizonEquipmentTrapDestCommString_Object = MibTableColumn
horizonEquipmentTrapDestCommString = _HorizonEquipmentTrapDestCommString_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 100, 1, 4, 4, 1, 2),
    _HorizonEquipmentTrapDestCommString_Type()
)
horizonEquipmentTrapDestCommString.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    horizonEquipmentTrapDestCommString.setStatus("current")


class _HorizonEquipmentTrapDestUdpPort_Type(Integer32):
    """Custom type horizonEquipmentTrapDestUdpPort based on Integer32"""
    defaultValue = 162

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_HorizonEquipmentTrapDestUdpPort_Type.__name__ = "Integer32"
_HorizonEquipmentTrapDestUdpPort_Object = MibTableColumn
horizonEquipmentTrapDestUdpPort = _HorizonEquipmentTrapDestUdpPort_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 100, 1, 4, 4, 1, 3),
    _HorizonEquipmentTrapDestUdpPort_Type()
)
horizonEquipmentTrapDestUdpPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    horizonEquipmentTrapDestUdpPort.setStatus("current")


class _HorizonEquipmentTrapDestSnmpVer_Type(Integer32):
    """Custom type horizonEquipmentTrapDestSnmpVer based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("v1", 0),
          ("v2", 1))
    )


_HorizonEquipmentTrapDestSnmpVer_Type.__name__ = "Integer32"
_HorizonEquipmentTrapDestSnmpVer_Object = MibTableColumn
horizonEquipmentTrapDestSnmpVer = _HorizonEquipmentTrapDestSnmpVer_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 100, 1, 4, 4, 1, 4),
    _HorizonEquipmentTrapDestSnmpVer_Type()
)
horizonEquipmentTrapDestSnmpVer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    horizonEquipmentTrapDestSnmpVer.setStatus("current")


class _HorizonEquipmentTrapDestEraseTime_Type(TimeTicks):
    """Custom type horizonEquipmentTrapDestEraseTime based on TimeTicks"""
    defaultValue = 1440000


_HorizonEquipmentTrapDestEraseTime_Type.__name__ = "TimeTicks"
_HorizonEquipmentTrapDestEraseTime_Object = MibTableColumn
horizonEquipmentTrapDestEraseTime = _HorizonEquipmentTrapDestEraseTime_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 100, 1, 4, 4, 1, 5),
    _HorizonEquipmentTrapDestEraseTime_Type()
)
horizonEquipmentTrapDestEraseTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    horizonEquipmentTrapDestEraseTime.setStatus("current")
_HorizonEquipmentTrapDestRowStatus_Type = RowStatus
_HorizonEquipmentTrapDestRowStatus_Object = MibTableColumn
horizonEquipmentTrapDestRowStatus = _HorizonEquipmentTrapDestRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 100, 1, 4, 4, 1, 6),
    _HorizonEquipmentTrapDestRowStatus_Type()
)
horizonEquipmentTrapDestRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    horizonEquipmentTrapDestRowStatus.setStatus("current")
_HorizonEquipmentPseudoEventsObjects_ObjectIdentity = ObjectIdentity
horizonEquipmentPseudoEventsObjects = _HorizonEquipmentPseudoEventsObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7262, 2, 100, 2)
)
_HorizonEquipmentConfChangeOid_Type = ObjectIdentifier
_HorizonEquipmentConfChangeOid_Object = MibScalar
horizonEquipmentConfChangeOid = _HorizonEquipmentConfChangeOid_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 100, 2, 1),
    _HorizonEquipmentConfChangeOid_Type()
)
horizonEquipmentConfChangeOid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    horizonEquipmentConfChangeOid.setStatus("current")


class _HorizonEquipmentConfChangeMode_Type(EnableType):
    """Custom type horizonEquipmentConfChangeMode based on EnableType"""
    defaultValue = 1


_HorizonEquipmentConfChangeMode_Type.__name__ = "EnableType"
_HorizonEquipmentConfChangeMode_Object = MibScalar
horizonEquipmentConfChangeMode = _HorizonEquipmentConfChangeMode_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 100, 2, 3),
    _HorizonEquipmentConfChangeMode_Type()
)
horizonEquipmentConfChangeMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    horizonEquipmentConfChangeMode.setStatus("current")
_HorizonEquipmentMirrorObjects_ObjectIdentity = ObjectIdentity
horizonEquipmentMirrorObjects = _HorizonEquipmentMirrorObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7262, 2, 100, 3)
)


class _HorizonEquipmentMirrorFlag_Type(Integer32):
    """Custom type horizonEquipmentMirrorFlag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_HorizonEquipmentMirrorFlag_Type.__name__ = "Integer32"
_HorizonEquipmentMirrorFlag_Object = MibScalar
horizonEquipmentMirrorFlag = _HorizonEquipmentMirrorFlag_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 100, 3, 1),
    _HorizonEquipmentMirrorFlag_Type()
)
horizonEquipmentMirrorFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    horizonEquipmentMirrorFlag.setStatus("current")

# Managed Objects groups


# Notification objects

horizonEquipmentConfChangeNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 7262, 2, 100, 2, 4)
)
horizonEquipmentConfChangeNotification.setObjects(
      *(("HORIZON-EQUIPMENT-LOG-MIB", "horizonEquipmentConfChangeOid"),
        ("HORIZON-EQUIPMENT-LOG-MIB", "horizonEquipmentOutTrapsCounter"))
)
if mibBuilder.loadTexts:
    horizonEquipmentConfChangeNotification.setStatus(
        "current"
    )

horizonEquipmentMirrorColdStart = NotificationType(
    (1, 3, 6, 1, 4, 1, 7262, 2, 100, 3, 2)
)
horizonEquipmentMirrorColdStart.setObjects(
      *(("HORIZON-EQUIPMENT-LOG-MIB", "horizonEquipmentMirrorFlag"),
        ("HORIZON-EQUIPMENT-LOG-MIB", "horizonEquipmentOutTrapsCounter"))
)
if mibBuilder.loadTexts:
    horizonEquipmentMirrorColdStart.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HORIZON-EQUIPMENT-LOG-MIB",
    **{"EnableType": EnableType,
       "horizonEquipmentLogMib": horizonEquipmentLogMib,
       "horizonEquipmentLogMibObjects": horizonEquipmentLogMibObjects,
       "horizonEquipmentConfigLog": horizonEquipmentConfigLog,
       "horizonEquipmentEventLogEntryLimit": horizonEquipmentEventLogEntryLimit,
       "horizonEquipmentLog": horizonEquipmentLog,
       "horizonEquipmentEventLogLastEntry": horizonEquipmentEventLogLastEntry,
       "horizonEquipmentEventLogTable": horizonEquipmentEventLogTable,
       "horizonEquipmentEventLogEntry": horizonEquipmentEventLogEntry,
       "horizonEquipmentEventLogIndex": horizonEquipmentEventLogIndex,
       "horizonEquipmentEventLogTime": horizonEquipmentEventLogTime,
       "horizonEquipmentEventLogDateAndTime": horizonEquipmentEventLogDateAndTime,
       "horizonEquipmentEventLogNotificationID": horizonEquipmentEventLogNotificationID,
       "horizonEquipmentEventLogVariables": horizonEquipmentEventLogVariables,
       "horizonEquipmentEventLogVariableTable": horizonEquipmentEventLogVariableTable,
       "horizonEquipmentEventLogVariableEntry": horizonEquipmentEventLogVariableEntry,
       "horizonEquipmentEventLogVariableIndex": horizonEquipmentEventLogVariableIndex,
       "horizonEquipmentEventLogVariableID": horizonEquipmentEventLogVariableID,
       "horizonEquipmentEventLogVariableValueType": horizonEquipmentEventLogVariableValueType,
       "horizonEquipmentEventLogVariableCounter32Val": horizonEquipmentEventLogVariableCounter32Val,
       "horizonEquipmentEventLogVariableUnsigned32Val": horizonEquipmentEventLogVariableUnsigned32Val,
       "horizonEquipmentEventLogVariableTimeTicksVal": horizonEquipmentEventLogVariableTimeTicksVal,
       "horizonEquipmentEventLogVariableInteger32Val": horizonEquipmentEventLogVariableInteger32Val,
       "horizonEquipmentEventLogVariableOctetStringVal": horizonEquipmentEventLogVariableOctetStringVal,
       "horizonEquipmentEventLogVariableIpAddressVal": horizonEquipmentEventLogVariableIpAddressVal,
       "horizonEquipmentEventLogVariableOidVal": horizonEquipmentEventLogVariableOidVal,
       "horizonEquipmentEventLogVariableCounter64Val": horizonEquipmentEventLogVariableCounter64Val,
       "horizonEquipmentAlarmList": horizonEquipmentAlarmList,
       "horizonEquipmentAlarmActiveLastChanged": horizonEquipmentAlarmActiveLastChanged,
       "horizonEquipmentAlarmActiveRowCounter": horizonEquipmentAlarmActiveRowCounter,
       "horizonEquipmentAlarmActiveTable": horizonEquipmentAlarmActiveTable,
       "horizonEquipmentAlarmActiveEntry": horizonEquipmentAlarmActiveEntry,
       "horizonEquipmentAlarmActiveIndex": horizonEquipmentAlarmActiveIndex,
       "horizonEquipmentAlarmActiveTime": horizonEquipmentAlarmActiveTime,
       "horizonEquipmentAlarmActiveDateAndTime": horizonEquipmentAlarmActiveDateAndTime,
       "horizonEquipmentAlarmActiveSourceID": horizonEquipmentAlarmActiveSourceID,
       "horizonEquipmentSnmpTrap": horizonEquipmentSnmpTrap,
       "horizonEquipmentOutTrapsCounter": horizonEquipmentOutTrapsCounter,
       "horizonEquipmentLastOutTrapTimeStamp": horizonEquipmentLastOutTrapTimeStamp,
       "horizonEquipmentTrapDestTable": horizonEquipmentTrapDestTable,
       "horizonEquipmentTrapDestEntry": horizonEquipmentTrapDestEntry,
       "horizonEquipmentTrapDestAddress": horizonEquipmentTrapDestAddress,
       "horizonEquipmentTrapDestCommString": horizonEquipmentTrapDestCommString,
       "horizonEquipmentTrapDestUdpPort": horizonEquipmentTrapDestUdpPort,
       "horizonEquipmentTrapDestSnmpVer": horizonEquipmentTrapDestSnmpVer,
       "horizonEquipmentTrapDestEraseTime": horizonEquipmentTrapDestEraseTime,
       "horizonEquipmentTrapDestRowStatus": horizonEquipmentTrapDestRowStatus,
       "horizonEquipmentPseudoEventsObjects": horizonEquipmentPseudoEventsObjects,
       "horizonEquipmentConfChangeOid": horizonEquipmentConfChangeOid,
       "horizonEquipmentConfChangeMode": horizonEquipmentConfChangeMode,
       "horizonEquipmentConfChangeNotification": horizonEquipmentConfChangeNotification,
       "horizonEquipmentMirrorObjects": horizonEquipmentMirrorObjects,
       "horizonEquipmentMirrorFlag": horizonEquipmentMirrorFlag,
       "horizonEquipmentMirrorColdStart": horizonEquipmentMirrorColdStart}
)
