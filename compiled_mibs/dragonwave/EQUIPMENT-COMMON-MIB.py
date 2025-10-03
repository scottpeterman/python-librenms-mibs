# SNMP MIB module (EQUIPMENT-COMMON-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\dragonwave\EQUIPMENT-COMMON-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:38:30 2025
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

(equipmentCommon,) = mibBuilder.importSymbols(
    "DWI-HARMONY-PRIVATE-MIB",
    "equipmentCommon")

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
 TextualConvention,
 TimeStamp) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "PhysAddress",
    "TextualConvention",
    "TimeStamp")


# MODULE-IDENTITY

equipmentCommonMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 7262, 20, 100)
)
if mibBuilder.loadTexts:
    equipmentCommonMib.setRevisions(
        ("2009-01-21 00:00",
         "2015-01-05 16:15")
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

_EquipmentCommonObjects_ObjectIdentity = ObjectIdentity
equipmentCommonObjects = _EquipmentCommonObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7262, 20, 1)
)
_EquipmentConfigLog_ObjectIdentity = ObjectIdentity
equipmentConfigLog = _EquipmentConfigLog_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7262, 20, 1, 1)
)


class _EquipmentEventLogEntryLimit_Type(Unsigned32):
    """Custom type equipmentEventLogEntryLimit based on Unsigned32"""
    defaultValue = 4096


_EquipmentEventLogEntryLimit_Type.__name__ = "Unsigned32"
_EquipmentEventLogEntryLimit_Object = MibScalar
equipmentEventLogEntryLimit = _EquipmentEventLogEntryLimit_Object(
    (1, 3, 6, 1, 4, 1, 7262, 20, 1, 1, 1),
    _EquipmentEventLogEntryLimit_Type()
)
equipmentEventLogEntryLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    equipmentEventLogEntryLimit.setStatus("current")
_EquipmentLog_ObjectIdentity = ObjectIdentity
equipmentLog = _EquipmentLog_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7262, 20, 1, 2)
)
_EquipmentEventLogLastEntry_Type = Unsigned32
_EquipmentEventLogLastEntry_Object = MibScalar
equipmentEventLogLastEntry = _EquipmentEventLogLastEntry_Object(
    (1, 3, 6, 1, 4, 1, 7262, 20, 1, 2, 1),
    _EquipmentEventLogLastEntry_Type()
)
equipmentEventLogLastEntry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    equipmentEventLogLastEntry.setStatus("current")
_EquipmentEventLogTable_Object = MibTable
equipmentEventLogTable = _EquipmentEventLogTable_Object(
    (1, 3, 6, 1, 4, 1, 7262, 20, 1, 2, 2)
)
if mibBuilder.loadTexts:
    equipmentEventLogTable.setStatus("current")
_EquipmentEventLogEntry_Object = MibTableRow
equipmentEventLogEntry = _EquipmentEventLogEntry_Object(
    (1, 3, 6, 1, 4, 1, 7262, 20, 1, 2, 2, 1)
)
equipmentEventLogEntry.setIndexNames(
    (0, "EQUIPMENT-COMMON-MIB", "equipmentEventLogIndex"),
)
if mibBuilder.loadTexts:
    equipmentEventLogEntry.setStatus("current")


class _EquipmentEventLogIndex_Type(Unsigned32):
    """Custom type equipmentEventLogIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_EquipmentEventLogIndex_Type.__name__ = "Unsigned32"
_EquipmentEventLogIndex_Object = MibTableColumn
equipmentEventLogIndex = _EquipmentEventLogIndex_Object(
    (1, 3, 6, 1, 4, 1, 7262, 20, 1, 2, 2, 1, 1),
    _EquipmentEventLogIndex_Type()
)
equipmentEventLogIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    equipmentEventLogIndex.setStatus("current")
_EquipmentEventLogTime_Type = TimeStamp
_EquipmentEventLogTime_Object = MibTableColumn
equipmentEventLogTime = _EquipmentEventLogTime_Object(
    (1, 3, 6, 1, 4, 1, 7262, 20, 1, 2, 2, 1, 2),
    _EquipmentEventLogTime_Type()
)
equipmentEventLogTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    equipmentEventLogTime.setStatus("current")
_EquipmentEventLogDateAndTime_Type = DateAndTime
_EquipmentEventLogDateAndTime_Object = MibTableColumn
equipmentEventLogDateAndTime = _EquipmentEventLogDateAndTime_Object(
    (1, 3, 6, 1, 4, 1, 7262, 20, 1, 2, 2, 1, 3),
    _EquipmentEventLogDateAndTime_Type()
)
equipmentEventLogDateAndTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    equipmentEventLogDateAndTime.setStatus("current")
_EquipmentEventLogNotificationID_Type = ObjectIdentifier
_EquipmentEventLogNotificationID_Object = MibTableColumn
equipmentEventLogNotificationID = _EquipmentEventLogNotificationID_Object(
    (1, 3, 6, 1, 4, 1, 7262, 20, 1, 2, 2, 1, 4),
    _EquipmentEventLogNotificationID_Type()
)
equipmentEventLogNotificationID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    equipmentEventLogNotificationID.setStatus("current")
_EquipmentEventLogVariables_Type = Unsigned32
_EquipmentEventLogVariables_Object = MibTableColumn
equipmentEventLogVariables = _EquipmentEventLogVariables_Object(
    (1, 3, 6, 1, 4, 1, 7262, 20, 1, 2, 2, 1, 5),
    _EquipmentEventLogVariables_Type()
)
equipmentEventLogVariables.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    equipmentEventLogVariables.setStatus("current")
_EquipmentEventLogVariableTable_Object = MibTable
equipmentEventLogVariableTable = _EquipmentEventLogVariableTable_Object(
    (1, 3, 6, 1, 4, 1, 7262, 20, 1, 2, 3)
)
if mibBuilder.loadTexts:
    equipmentEventLogVariableTable.setStatus("current")
_EquipmentEventLogVariableEntry_Object = MibTableRow
equipmentEventLogVariableEntry = _EquipmentEventLogVariableEntry_Object(
    (1, 3, 6, 1, 4, 1, 7262, 20, 1, 2, 3, 1)
)
equipmentEventLogVariableEntry.setIndexNames(
    (0, "EQUIPMENT-COMMON-MIB", "equipmentEventLogIndex"),
    (0, "EQUIPMENT-COMMON-MIB", "equipmentEventLogVariableIndex"),
)
if mibBuilder.loadTexts:
    equipmentEventLogVariableEntry.setStatus("current")


class _EquipmentEventLogVariableIndex_Type(Unsigned32):
    """Custom type equipmentEventLogVariableIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_EquipmentEventLogVariableIndex_Type.__name__ = "Unsigned32"
_EquipmentEventLogVariableIndex_Object = MibTableColumn
equipmentEventLogVariableIndex = _EquipmentEventLogVariableIndex_Object(
    (1, 3, 6, 1, 4, 1, 7262, 20, 1, 2, 3, 1, 1),
    _EquipmentEventLogVariableIndex_Type()
)
equipmentEventLogVariableIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    equipmentEventLogVariableIndex.setStatus("current")
_EquipmentEventLogVariableID_Type = ObjectIdentifier
_EquipmentEventLogVariableID_Object = MibTableColumn
equipmentEventLogVariableID = _EquipmentEventLogVariableID_Object(
    (1, 3, 6, 1, 4, 1, 7262, 20, 1, 2, 3, 1, 2),
    _EquipmentEventLogVariableID_Type()
)
equipmentEventLogVariableID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    equipmentEventLogVariableID.setStatus("current")


class _EquipmentEventLogVariableValueType_Type(Integer32):
    """Custom type equipmentEventLogVariableValueType based on Integer32"""
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


_EquipmentEventLogVariableValueType_Type.__name__ = "Integer32"
_EquipmentEventLogVariableValueType_Object = MibTableColumn
equipmentEventLogVariableValueType = _EquipmentEventLogVariableValueType_Object(
    (1, 3, 6, 1, 4, 1, 7262, 20, 1, 2, 3, 1, 3),
    _EquipmentEventLogVariableValueType_Type()
)
equipmentEventLogVariableValueType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    equipmentEventLogVariableValueType.setStatus("current")
_EquipmentEventLogVariableCounter32Val_Type = Counter32
_EquipmentEventLogVariableCounter32Val_Object = MibTableColumn
equipmentEventLogVariableCounter32Val = _EquipmentEventLogVariableCounter32Val_Object(
    (1, 3, 6, 1, 4, 1, 7262, 20, 1, 2, 3, 1, 4),
    _EquipmentEventLogVariableCounter32Val_Type()
)
equipmentEventLogVariableCounter32Val.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    equipmentEventLogVariableCounter32Val.setStatus("current")
_EquipmentEventLogVariableUnsigned32Val_Type = Unsigned32
_EquipmentEventLogVariableUnsigned32Val_Object = MibTableColumn
equipmentEventLogVariableUnsigned32Val = _EquipmentEventLogVariableUnsigned32Val_Object(
    (1, 3, 6, 1, 4, 1, 7262, 20, 1, 2, 3, 1, 5),
    _EquipmentEventLogVariableUnsigned32Val_Type()
)
equipmentEventLogVariableUnsigned32Val.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    equipmentEventLogVariableUnsigned32Val.setStatus("current")
_EquipmentEventLogVariableTimeTicksVal_Type = TimeTicks
_EquipmentEventLogVariableTimeTicksVal_Object = MibTableColumn
equipmentEventLogVariableTimeTicksVal = _EquipmentEventLogVariableTimeTicksVal_Object(
    (1, 3, 6, 1, 4, 1, 7262, 20, 1, 2, 3, 1, 6),
    _EquipmentEventLogVariableTimeTicksVal_Type()
)
equipmentEventLogVariableTimeTicksVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    equipmentEventLogVariableTimeTicksVal.setStatus("current")
_EquipmentEventLogVariableInteger32Val_Type = Integer32
_EquipmentEventLogVariableInteger32Val_Object = MibTableColumn
equipmentEventLogVariableInteger32Val = _EquipmentEventLogVariableInteger32Val_Object(
    (1, 3, 6, 1, 4, 1, 7262, 20, 1, 2, 3, 1, 7),
    _EquipmentEventLogVariableInteger32Val_Type()
)
equipmentEventLogVariableInteger32Val.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    equipmentEventLogVariableInteger32Val.setStatus("current")
_EquipmentEventLogVariableOctetStringVal_Type = OctetString
_EquipmentEventLogVariableOctetStringVal_Object = MibTableColumn
equipmentEventLogVariableOctetStringVal = _EquipmentEventLogVariableOctetStringVal_Object(
    (1, 3, 6, 1, 4, 1, 7262, 20, 1, 2, 3, 1, 8),
    _EquipmentEventLogVariableOctetStringVal_Type()
)
equipmentEventLogVariableOctetStringVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    equipmentEventLogVariableOctetStringVal.setStatus("current")
_EquipmentEventLogVariableIpAddressVal_Type = IpAddress
_EquipmentEventLogVariableIpAddressVal_Object = MibTableColumn
equipmentEventLogVariableIpAddressVal = _EquipmentEventLogVariableIpAddressVal_Object(
    (1, 3, 6, 1, 4, 1, 7262, 20, 1, 2, 3, 1, 9),
    _EquipmentEventLogVariableIpAddressVal_Type()
)
equipmentEventLogVariableIpAddressVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    equipmentEventLogVariableIpAddressVal.setStatus("current")
_EquipmentEventLogVariableOidVal_Type = ObjectIdentifier
_EquipmentEventLogVariableOidVal_Object = MibTableColumn
equipmentEventLogVariableOidVal = _EquipmentEventLogVariableOidVal_Object(
    (1, 3, 6, 1, 4, 1, 7262, 20, 1, 2, 3, 1, 10),
    _EquipmentEventLogVariableOidVal_Type()
)
equipmentEventLogVariableOidVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    equipmentEventLogVariableOidVal.setStatus("current")
_EquipmentEventLogVariableCounter64Val_Type = Counter64
_EquipmentEventLogVariableCounter64Val_Object = MibTableColumn
equipmentEventLogVariableCounter64Val = _EquipmentEventLogVariableCounter64Val_Object(
    (1, 3, 6, 1, 4, 1, 7262, 20, 1, 2, 3, 1, 11),
    _EquipmentEventLogVariableCounter64Val_Type()
)
equipmentEventLogVariableCounter64Val.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    equipmentEventLogVariableCounter64Val.setStatus("current")
_EquipmentAlarmList_ObjectIdentity = ObjectIdentity
equipmentAlarmList = _EquipmentAlarmList_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7262, 20, 1, 3)
)
_EquipmentAlarmActiveLastChanged_Type = TimeTicks
_EquipmentAlarmActiveLastChanged_Object = MibScalar
equipmentAlarmActiveLastChanged = _EquipmentAlarmActiveLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 7262, 20, 1, 3, 1),
    _EquipmentAlarmActiveLastChanged_Type()
)
equipmentAlarmActiveLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    equipmentAlarmActiveLastChanged.setStatus("current")
_EquipmentAlarmActiveRowCounter_Type = Counter32
_EquipmentAlarmActiveRowCounter_Object = MibScalar
equipmentAlarmActiveRowCounter = _EquipmentAlarmActiveRowCounter_Object(
    (1, 3, 6, 1, 4, 1, 7262, 20, 1, 3, 2),
    _EquipmentAlarmActiveRowCounter_Type()
)
equipmentAlarmActiveRowCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    equipmentAlarmActiveRowCounter.setStatus("current")
_EquipmentAlarmActiveTable_Object = MibTable
equipmentAlarmActiveTable = _EquipmentAlarmActiveTable_Object(
    (1, 3, 6, 1, 4, 1, 7262, 20, 1, 3, 3)
)
if mibBuilder.loadTexts:
    equipmentAlarmActiveTable.setStatus("current")
_EquipmentAlarmActiveEntry_Object = MibTableRow
equipmentAlarmActiveEntry = _EquipmentAlarmActiveEntry_Object(
    (1, 3, 6, 1, 4, 1, 7262, 20, 1, 3, 3, 1)
)
equipmentAlarmActiveEntry.setIndexNames(
    (0, "EQUIPMENT-COMMON-MIB", "equipmentAlarmActiveIndex"),
    (0, "EQUIPMENT-COMMON-MIB", "equipmentAlarmActiveTime"),
)
if mibBuilder.loadTexts:
    equipmentAlarmActiveEntry.setStatus("current")


class _EquipmentAlarmActiveIndex_Type(Unsigned32):
    """Custom type equipmentAlarmActiveIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_EquipmentAlarmActiveIndex_Type.__name__ = "Unsigned32"
_EquipmentAlarmActiveIndex_Object = MibTableColumn
equipmentAlarmActiveIndex = _EquipmentAlarmActiveIndex_Object(
    (1, 3, 6, 1, 4, 1, 7262, 20, 1, 3, 3, 1, 1),
    _EquipmentAlarmActiveIndex_Type()
)
equipmentAlarmActiveIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    equipmentAlarmActiveIndex.setStatus("current")
_EquipmentAlarmActiveTime_Type = TimeStamp
_EquipmentAlarmActiveTime_Object = MibTableColumn
equipmentAlarmActiveTime = _EquipmentAlarmActiveTime_Object(
    (1, 3, 6, 1, 4, 1, 7262, 20, 1, 3, 3, 1, 2),
    _EquipmentAlarmActiveTime_Type()
)
equipmentAlarmActiveTime.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    equipmentAlarmActiveTime.setStatus("current")
_EquipmentAlarmActiveDateAndTime_Type = DateAndTime
_EquipmentAlarmActiveDateAndTime_Object = MibTableColumn
equipmentAlarmActiveDateAndTime = _EquipmentAlarmActiveDateAndTime_Object(
    (1, 3, 6, 1, 4, 1, 7262, 20, 1, 3, 3, 1, 3),
    _EquipmentAlarmActiveDateAndTime_Type()
)
equipmentAlarmActiveDateAndTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    equipmentAlarmActiveDateAndTime.setStatus("current")
_EquipmentAlarmActiveName_Type = DisplayString
_EquipmentAlarmActiveName_Object = MibTableColumn
equipmentAlarmActiveName = _EquipmentAlarmActiveName_Object(
    (1, 3, 6, 1, 4, 1, 7262, 20, 1, 3, 3, 1, 4),
    _EquipmentAlarmActiveName_Type()
)
equipmentAlarmActiveName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    equipmentAlarmActiveName.setStatus("current")
_EquipmentAlarmActiveID_Type = Integer32
_EquipmentAlarmActiveID_Object = MibTableColumn
equipmentAlarmActiveID = _EquipmentAlarmActiveID_Object(
    (1, 3, 6, 1, 4, 1, 7262, 20, 1, 3, 3, 1, 5),
    _EquipmentAlarmActiveID_Type()
)
equipmentAlarmActiveID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    equipmentAlarmActiveID.setStatus("current")
_EquipmentAlarmActiveInstance_Type = Unsigned32
_EquipmentAlarmActiveInstance_Object = MibTableColumn
equipmentAlarmActiveInstance = _EquipmentAlarmActiveInstance_Object(
    (1, 3, 6, 1, 4, 1, 7262, 20, 1, 3, 3, 1, 6),
    _EquipmentAlarmActiveInstance_Type()
)
equipmentAlarmActiveInstance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    equipmentAlarmActiveInstance.setStatus("current")
_EquipmentAlarmActiveTrapOID_Type = ObjectIdentifier
_EquipmentAlarmActiveTrapOID_Object = MibTableColumn
equipmentAlarmActiveTrapOID = _EquipmentAlarmActiveTrapOID_Object(
    (1, 3, 6, 1, 4, 1, 7262, 20, 1, 3, 3, 1, 7),
    _EquipmentAlarmActiveTrapOID_Type()
)
equipmentAlarmActiveTrapOID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    equipmentAlarmActiveTrapOID.setStatus("current")


class _EquipmentAlarmActiveSeverity_Type(Integer32):
    """Custom type equipmentAlarmActiveSeverity based on Integer32"""
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
        *(("warning", 1),
          ("minor", 2),
          ("major", 3),
          ("critical", 4))
    )


_EquipmentAlarmActiveSeverity_Type.__name__ = "Integer32"
_EquipmentAlarmActiveSeverity_Object = MibTableColumn
equipmentAlarmActiveSeverity = _EquipmentAlarmActiveSeverity_Object(
    (1, 3, 6, 1, 4, 1, 7262, 20, 1, 3, 3, 1, 8),
    _EquipmentAlarmActiveSeverity_Type()
)
equipmentAlarmActiveSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    equipmentAlarmActiveSeverity.setStatus("current")
_EquipmentAlarmActiveConditionId_Type = DisplayString
_EquipmentAlarmActiveConditionId_Object = MibTableColumn
equipmentAlarmActiveConditionId = _EquipmentAlarmActiveConditionId_Object(
    (1, 3, 6, 1, 4, 1, 7262, 20, 1, 3, 3, 1, 9),
    _EquipmentAlarmActiveConditionId_Type()
)
equipmentAlarmActiveConditionId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    equipmentAlarmActiveConditionId.setStatus("current")
_EquipmentSnmpTrap_ObjectIdentity = ObjectIdentity
equipmentSnmpTrap = _EquipmentSnmpTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7262, 20, 1, 4)
)
_EquipmentOutTrapsCounter_Type = Counter32
_EquipmentOutTrapsCounter_Object = MibScalar
equipmentOutTrapsCounter = _EquipmentOutTrapsCounter_Object(
    (1, 3, 6, 1, 4, 1, 7262, 20, 1, 4, 1),
    _EquipmentOutTrapsCounter_Type()
)
equipmentOutTrapsCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    equipmentOutTrapsCounter.setStatus("current")
_EquipmentLastOutTrapTimeStamp_Type = TimeStamp
_EquipmentLastOutTrapTimeStamp_Object = MibScalar
equipmentLastOutTrapTimeStamp = _EquipmentLastOutTrapTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 7262, 20, 1, 4, 2),
    _EquipmentLastOutTrapTimeStamp_Type()
)
equipmentLastOutTrapTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    equipmentLastOutTrapTimeStamp.setStatus("current")
_EquipmentTrapInfo_Type = DisplayString
_EquipmentTrapInfo_Object = MibScalar
equipmentTrapInfo = _EquipmentTrapInfo_Object(
    (1, 3, 6, 1, 4, 1, 7262, 20, 1, 4, 3),
    _EquipmentTrapInfo_Type()
)
equipmentTrapInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    equipmentTrapInfo.setStatus("current")
_EquipmentPseudoEventsObjects_ObjectIdentity = ObjectIdentity
equipmentPseudoEventsObjects = _EquipmentPseudoEventsObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7262, 20, 2)
)
_EquipmentConfChangeOid_Type = ObjectIdentifier
_EquipmentConfChangeOid_Object = MibScalar
equipmentConfChangeOid = _EquipmentConfChangeOid_Object(
    (1, 3, 6, 1, 4, 1, 7262, 20, 2, 1),
    _EquipmentConfChangeOid_Type()
)
equipmentConfChangeOid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    equipmentConfChangeOid.setStatus("current")


class _EquipmentConfChangeMode_Type(EnableType):
    """Custom type equipmentConfChangeMode based on EnableType"""
    defaultValue = 1


_EquipmentConfChangeMode_Type.__name__ = "EnableType"
_EquipmentConfChangeMode_Object = MibScalar
equipmentConfChangeMode = _EquipmentConfChangeMode_Object(
    (1, 3, 6, 1, 4, 1, 7262, 20, 2, 2),
    _EquipmentConfChangeMode_Type()
)
equipmentConfChangeMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    equipmentConfChangeMode.setStatus("current")
_EquipmentMirrorObjects_ObjectIdentity = ObjectIdentity
equipmentMirrorObjects = _EquipmentMirrorObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7262, 20, 3)
)


class _EquipmentMirrorFlag_Type(Integer32):
    """Custom type equipmentMirrorFlag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_EquipmentMirrorFlag_Type.__name__ = "Integer32"
_EquipmentMirrorFlag_Object = MibScalar
equipmentMirrorFlag = _EquipmentMirrorFlag_Object(
    (1, 3, 6, 1, 4, 1, 7262, 20, 3, 1),
    _EquipmentMirrorFlag_Type()
)
equipmentMirrorFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    equipmentMirrorFlag.setStatus("current")

# Managed Objects groups


# Notification objects

equipmentConfChangeNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 7262, 20, 2, 3)
)
equipmentConfChangeNotification.setObjects(
      *(("EQUIPMENT-COMMON-MIB", "equipmentConfChangeOid"),
        ("EQUIPMENT-COMMON-MIB", "equipmentOutTrapsCounter"))
)
if mibBuilder.loadTexts:
    equipmentConfChangeNotification.setStatus(
        "current"
    )

equipmentMirrorColdStart = NotificationType(
    (1, 3, 6, 1, 4, 1, 7262, 20, 3, 2)
)
equipmentMirrorColdStart.setObjects(
      *(("EQUIPMENT-COMMON-MIB", "equipmentMirrorFlag"),
        ("EQUIPMENT-COMMON-MIB", "equipmentOutTrapsCounter"))
)
if mibBuilder.loadTexts:
    equipmentMirrorColdStart.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "EQUIPMENT-COMMON-MIB",
    **{"EnableType": EnableType,
       "equipmentCommonObjects": equipmentCommonObjects,
       "equipmentConfigLog": equipmentConfigLog,
       "equipmentEventLogEntryLimit": equipmentEventLogEntryLimit,
       "equipmentLog": equipmentLog,
       "equipmentEventLogLastEntry": equipmentEventLogLastEntry,
       "equipmentEventLogTable": equipmentEventLogTable,
       "equipmentEventLogEntry": equipmentEventLogEntry,
       "equipmentEventLogIndex": equipmentEventLogIndex,
       "equipmentEventLogTime": equipmentEventLogTime,
       "equipmentEventLogDateAndTime": equipmentEventLogDateAndTime,
       "equipmentEventLogNotificationID": equipmentEventLogNotificationID,
       "equipmentEventLogVariables": equipmentEventLogVariables,
       "equipmentEventLogVariableTable": equipmentEventLogVariableTable,
       "equipmentEventLogVariableEntry": equipmentEventLogVariableEntry,
       "equipmentEventLogVariableIndex": equipmentEventLogVariableIndex,
       "equipmentEventLogVariableID": equipmentEventLogVariableID,
       "equipmentEventLogVariableValueType": equipmentEventLogVariableValueType,
       "equipmentEventLogVariableCounter32Val": equipmentEventLogVariableCounter32Val,
       "equipmentEventLogVariableUnsigned32Val": equipmentEventLogVariableUnsigned32Val,
       "equipmentEventLogVariableTimeTicksVal": equipmentEventLogVariableTimeTicksVal,
       "equipmentEventLogVariableInteger32Val": equipmentEventLogVariableInteger32Val,
       "equipmentEventLogVariableOctetStringVal": equipmentEventLogVariableOctetStringVal,
       "equipmentEventLogVariableIpAddressVal": equipmentEventLogVariableIpAddressVal,
       "equipmentEventLogVariableOidVal": equipmentEventLogVariableOidVal,
       "equipmentEventLogVariableCounter64Val": equipmentEventLogVariableCounter64Val,
       "equipmentAlarmList": equipmentAlarmList,
       "equipmentAlarmActiveLastChanged": equipmentAlarmActiveLastChanged,
       "equipmentAlarmActiveRowCounter": equipmentAlarmActiveRowCounter,
       "equipmentAlarmActiveTable": equipmentAlarmActiveTable,
       "equipmentAlarmActiveEntry": equipmentAlarmActiveEntry,
       "equipmentAlarmActiveIndex": equipmentAlarmActiveIndex,
       "equipmentAlarmActiveTime": equipmentAlarmActiveTime,
       "equipmentAlarmActiveDateAndTime": equipmentAlarmActiveDateAndTime,
       "equipmentAlarmActiveName": equipmentAlarmActiveName,
       "equipmentAlarmActiveID": equipmentAlarmActiveID,
       "equipmentAlarmActiveInstance": equipmentAlarmActiveInstance,
       "equipmentAlarmActiveTrapOID": equipmentAlarmActiveTrapOID,
       "equipmentAlarmActiveSeverity": equipmentAlarmActiveSeverity,
       "equipmentAlarmActiveConditionId": equipmentAlarmActiveConditionId,
       "equipmentSnmpTrap": equipmentSnmpTrap,
       "equipmentOutTrapsCounter": equipmentOutTrapsCounter,
       "equipmentLastOutTrapTimeStamp": equipmentLastOutTrapTimeStamp,
       "equipmentTrapInfo": equipmentTrapInfo,
       "equipmentPseudoEventsObjects": equipmentPseudoEventsObjects,
       "equipmentConfChangeOid": equipmentConfChangeOid,
       "equipmentConfChangeMode": equipmentConfChangeMode,
       "equipmentConfChangeNotification": equipmentConfChangeNotification,
       "equipmentMirrorObjects": equipmentMirrorObjects,
       "equipmentMirrorFlag": equipmentMirrorFlag,
       "equipmentMirrorColdStart": equipmentMirrorColdStart,
       "equipmentCommonMib": equipmentCommonMib}
)
