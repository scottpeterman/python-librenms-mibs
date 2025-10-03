# SNMP MIB module (SIAE-EQUIP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\siae\SIAE-EQUIP-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 12:26:44 2025
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

(InterfaceIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex")

(AlarmSeverityCode,
 AlarmStatus,
 alarmTrap) = mibBuilder.importSymbols(
    "SIAE-ALARM-MIB",
    "AlarmSeverityCode",
    "AlarmStatus",
    "alarmTrap")

(equipTypeUnknown,) = mibBuilder.importSymbols(
    "SIAE-EQUIPTYPE-MIB",
    "equipTypeUnknown")

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

(AutonomousType,
 DisplayString,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "AutonomousType",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

equipment = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 1)
)
if mibBuilder.loadTexts:
    equipment.setRevisions(
        ("2015-03-23 00:00",
         "2014-12-03 00:00",
         "2014-07-01 00:00",
         "2014-06-23 00:00",
         "2014-02-03 00:00",
         "2013-04-16 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs



class _EquipMibVersion_Type(Integer32):
    """Custom type equipMibVersion based on Integer32"""
    defaultValue = 1


_EquipMibVersion_Type.__name__ = "Integer32"
_EquipMibVersion_Object = MibScalar
equipMibVersion = _EquipMibVersion_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 1, 1),
    _EquipMibVersion_Type()
)
equipMibVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    equipMibVersion.setStatus("current")
_EquipCurrentTime_Type = TimeTicks
_EquipCurrentTime_Object = MibScalar
equipCurrentTime = _EquipCurrentTime_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 1, 2),
    _EquipCurrentTime_Type()
)
equipCurrentTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    equipCurrentTime.setStatus("current")
_EquipUpTime_Type = TimeTicks
_EquipUpTime_Object = MibScalar
equipUpTime = _EquipUpTime_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 1, 3),
    _EquipUpTime_Type()
)
equipUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    equipUpTime.setStatus("current")


class _EquipType_Type(AutonomousType):
    """Custom type equipType based on AutonomousType"""
    defaultValue = (1, 3, 6, 1, 4, 1, 3373, 1103, 1, 5, 1)


_EquipType_Type.__name__ = "AutonomousType"
_EquipType_Object = MibScalar
equipType = _EquipType_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 1, 4),
    _EquipType_Type()
)
equipType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    equipType.setStatus("current")
_EquipIpEthOsiAddress_Type = IpAddress
_EquipIpEthOsiAddress_Object = MibScalar
equipIpEthOsiAddress = _EquipIpEthOsiAddress_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 1, 6),
    _EquipIpEthOsiAddress_Type()
)
equipIpEthOsiAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    equipIpEthOsiAddress.setStatus("current")


class _EquipGosipAddress_Type(OctetString):
    """Custom type equipGosipAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_EquipGosipAddress_Type.__name__ = "OctetString"
_EquipGosipAddress_Object = MibScalar
equipGosipAddress = _EquipGosipAddress_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 1, 7),
    _EquipGosipAddress_Type()
)
equipGosipAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    equipGosipAddress.setStatus("current")
_EquipIpEthOsiNetMask_Type = IpAddress
_EquipIpEthOsiNetMask_Object = MibScalar
equipIpEthOsiNetMask = _EquipIpEthOsiNetMask_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 1, 8),
    _EquipIpEthOsiNetMask_Type()
)
equipIpEthOsiNetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    equipIpEthOsiNetMask.setStatus("current")


class _EquipL1L2IsIsRouting_Type(Integer32):
    """Custom type equipL1L2IsIsRouting based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("l1", 1),
          ("l2", 2))
    )


_EquipL1L2IsIsRouting_Type.__name__ = "Integer32"
_EquipL1L2IsIsRouting_Object = MibScalar
equipL1L2IsIsRouting = _EquipL1L2IsIsRouting_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 1, 9),
    _EquipL1L2IsIsRouting_Type()
)
equipL1L2IsIsRouting.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    equipL1L2IsIsRouting.setStatus("current")


class _EquipStationID_Type(DisplayString):
    """Custom type equipStationID based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_EquipStationID_Type.__name__ = "DisplayString"
_EquipStationID_Object = MibScalar
equipStationID = _EquipStationID_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 1, 10),
    _EquipStationID_Type()
)
equipStationID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    equipStationID.setStatus("current")


class _EquipLOMConfigEnable_Type(Integer32):
    """Custom type equipLOMConfigEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_EquipLOMConfigEnable_Type.__name__ = "Integer32"
_EquipLOMConfigEnable_Object = MibScalar
equipLOMConfigEnable = _EquipLOMConfigEnable_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 1, 11),
    _EquipLOMConfigEnable_Type()
)
equipLOMConfigEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    equipLOMConfigEnable.setStatus("current")


class _EquipLOMConnected_Type(Integer32):
    """Custom type equipLOMConnected based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("cleared", 1),
          ("connectionAsMonitor", 2),
          ("connectionAsConfig", 3))
    )


_EquipLOMConnected_Type.__name__ = "Integer32"
_EquipLOMConnected_Object = MibScalar
equipLOMConnected = _EquipLOMConnected_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 1, 12),
    _EquipLOMConnected_Type()
)
equipLOMConnected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    equipLOMConnected.setStatus("current")


class _EquipLOMConnectedTrapEnable_Type(Integer32):
    """Custom type equipLOMConnectedTrapEnable based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("trapDisable", 1),
          ("trapEnable", 2),
          ("trapEnableWithAck", 3))
    )


_EquipLOMConnectedTrapEnable_Type.__name__ = "Integer32"
_EquipLOMConnectedTrapEnable_Object = MibScalar
equipLOMConnectedTrapEnable = _EquipLOMConnectedTrapEnable_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 1, 13),
    _EquipLOMConnectedTrapEnable_Type()
)
equipLOMConnectedTrapEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    equipLOMConnectedTrapEnable.setStatus("current")


class _EquipConfigChange_Type(OctetString):
    """Custom type equipConfigChange based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )
    fixed_length = 6


_EquipConfigChange_Type.__name__ = "OctetString"
_EquipConfigChange_Object = MibScalar
equipConfigChange = _EquipConfigChange_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 1, 14),
    _EquipConfigChange_Type()
)
equipConfigChange.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    equipConfigChange.setStatus("current")


class _EquipConfigChangeTrapEnable_Type(Integer32):
    """Custom type equipConfigChangeTrapEnable based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("trapDisable", 1),
          ("trapEnable", 2),
          ("trapEnableWithACK", 3))
    )


_EquipConfigChangeTrapEnable_Type.__name__ = "Integer32"
_EquipConfigChangeTrapEnable_Object = MibScalar
equipConfigChangeTrapEnable = _EquipConfigChangeTrapEnable_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 1, 15),
    _EquipConfigChangeTrapEnable_Type()
)
equipConfigChangeTrapEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    equipConfigChangeTrapEnable.setStatus("current")


class _EquipRequest_Type(Integer32):
    """Custom type equipRequest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              11,
              20,
              21,
              50,
              100,
              125,
              126,
              127)
        )
    )
    namedValues = NamedValues(
        *(("notActive", 0),
          ("restart", 1),
          ("applyIfChange", 2),
          ("revertIfChange", 3),
          ("configClearAndRestart", 4),
          ("routeTableClear", 5),
          ("uploadBaseBand", 6),
          ("offLineRouteRetrieve", 7),
          ("offLineRouteSave", 8),
          ("hotApplyIfChange", 11),
          ("ipStackConfigure", 20),
          ("osiStackConfigure", 21),
          ("atuTableReset", 50),
          ("siaeReservedReq1", 100),
          ("siaeReservedReq26", 125),
          ("siaeReservedReq27", 126),
          ("switchFactoryDefault", 127))
    )


_EquipRequest_Type.__name__ = "Integer32"
_EquipRequest_Object = MibScalar
equipRequest = _EquipRequest_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 1, 16),
    _EquipRequest_Type()
)
equipRequest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    equipRequest.setStatus("current")
_EquipIpEthAddress_Type = IpAddress
_EquipIpEthAddress_Object = MibScalar
equipIpEthAddress = _EquipIpEthAddress_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 1, 17),
    _EquipIpEthAddress_Type()
)
equipIpEthAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    equipIpEthAddress.setStatus("current")
_EquipIpEthNetMask_Type = IpAddress
_EquipIpEthNetMask_Object = MibScalar
equipIpEthNetMask = _EquipIpEthNetMask_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 1, 18),
    _EquipIpEthNetMask_Type()
)
equipIpEthNetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    equipIpEthNetMask.setStatus("current")


class _EquipOsiamParameter_Type(OctetString):
    """Custom type equipOsiamParameter based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 41),
    )


_EquipOsiamParameter_Type.__name__ = "OctetString"
_EquipOsiamParameter_Object = MibScalar
equipOsiamParameter = _EquipOsiamParameter_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 1, 19),
    _EquipOsiamParameter_Type()
)
equipOsiamParameter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    equipOsiamParameter.setStatus("current")
_EquipIpSnmpAgentAddress_Type = IpAddress
_EquipIpSnmpAgentAddress_Object = MibScalar
equipIpSnmpAgentAddress = _EquipIpSnmpAgentAddress_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 1, 20),
    _EquipIpSnmpAgentAddress_Type()
)
equipIpSnmpAgentAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    equipIpSnmpAgentAddress.setStatus("current")


class _EquipOperationInProgress_Type(Integer32):
    """Custom type equipOperationInProgress based on Integer32"""
    defaultValue = 0


_EquipOperationInProgress_Type.__name__ = "Integer32"
_EquipOperationInProgress_Object = MibScalar
equipOperationInProgress = _EquipOperationInProgress_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 1, 21),
    _EquipOperationInProgress_Type()
)
equipOperationInProgress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    equipOperationInProgress.setStatus("current")
_EquipManagerWakeUpAlarm_Type = AlarmStatus
_EquipManagerWakeUpAlarm_Object = MibScalar
equipManagerWakeUpAlarm = _EquipManagerWakeUpAlarm_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 1, 22),
    _EquipManagerWakeUpAlarm_Type()
)
equipManagerWakeUpAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    equipManagerWakeUpAlarm.setStatus("current")


class _EquipManagerWakeUpAlarmSeverityCode_Type(AlarmSeverityCode):
    """Custom type equipManagerWakeUpAlarmSeverityCode based on AlarmSeverityCode"""
    defaultValue = 1


_EquipManagerWakeUpAlarmSeverityCode_Type.__name__ = "AlarmSeverityCode"
_EquipManagerWakeUpAlarmSeverityCode_Object = MibScalar
equipManagerWakeUpAlarmSeverityCode = _EquipManagerWakeUpAlarmSeverityCode_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 1, 23),
    _EquipManagerWakeUpAlarmSeverityCode_Type()
)
equipManagerWakeUpAlarmSeverityCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    equipManagerWakeUpAlarmSeverityCode.setStatus("current")


class _EquipManagerWakeUpTimeout_Type(Integer32):
    """Custom type equipManagerWakeUpTimeout based on Integer32"""
    defaultValue = 60

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1440),
    )


_EquipManagerWakeUpTimeout_Type.__name__ = "Integer32"
_EquipManagerWakeUpTimeout_Object = MibScalar
equipManagerWakeUpTimeout = _EquipManagerWakeUpTimeout_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 1, 24),
    _EquipManagerWakeUpTimeout_Type()
)
equipManagerWakeUpTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    equipManagerWakeUpTimeout.setStatus("current")
_EquipManagerWakeUpIpAddr_Type = IpAddress
_EquipManagerWakeUpIpAddr_Object = MibScalar
equipManagerWakeUpIpAddr = _EquipManagerWakeUpIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 1, 25),
    _EquipManagerWakeUpIpAddr_Type()
)
equipManagerWakeUpIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    equipManagerWakeUpIpAddr.setStatus("current")


class _EquipManagerWakeUpGosipAddress_Type(OctetString):
    """Custom type equipManagerWakeUpGosipAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_EquipManagerWakeUpGosipAddress_Type.__name__ = "OctetString"
_EquipManagerWakeUpGosipAddress_Object = MibScalar
equipManagerWakeUpGosipAddress = _EquipManagerWakeUpGosipAddress_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 1, 26),
    _EquipManagerWakeUpGosipAddress_Type()
)
equipManagerWakeUpGosipAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    equipManagerWakeUpGosipAddress.setStatus("current")


class _EquipManagerWakeUpTrapVersion_Type(Integer32):
    """Custom type equipManagerWakeUpTrapVersion based on Integer32"""
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
        *(("trapV1", 1),
          ("trapV2", 2),
          ("trapV3", 3))
    )


_EquipManagerWakeUpTrapVersion_Type.__name__ = "Integer32"
_EquipManagerWakeUpTrapVersion_Object = MibScalar
equipManagerWakeUpTrapVersion = _EquipManagerWakeUpTrapVersion_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 1, 27),
    _EquipManagerWakeUpTrapVersion_Type()
)
equipManagerWakeUpTrapVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    equipManagerWakeUpTrapVersion.setStatus("current")
_EquipManager1IpAddr_Type = IpAddress
_EquipManager1IpAddr_Object = MibScalar
equipManager1IpAddr = _EquipManager1IpAddr_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 1, 28),
    _EquipManager1IpAddr_Type()
)
equipManager1IpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    equipManager1IpAddr.setStatus("current")
_EquipManager2IpAddr_Type = IpAddress
_EquipManager2IpAddr_Object = MibScalar
equipManager2IpAddr = _EquipManager2IpAddr_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 1, 29),
    _EquipManager2IpAddr_Type()
)
equipManager2IpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    equipManager2IpAddr.setStatus("current")


class _EquipManager1TrapVersion_Type(Integer32):
    """Custom type equipManager1TrapVersion based on Integer32"""
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
        *(("trapV1", 1),
          ("trapV2", 2),
          ("trapV3", 3))
    )


_EquipManager1TrapVersion_Type.__name__ = "Integer32"
_EquipManager1TrapVersion_Object = MibScalar
equipManager1TrapVersion = _EquipManager1TrapVersion_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 1, 30),
    _EquipManager1TrapVersion_Type()
)
equipManager1TrapVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    equipManager1TrapVersion.setStatus("current")


class _EquipManager2TrapVersion_Type(Integer32):
    """Custom type equipManager2TrapVersion based on Integer32"""
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
        *(("trapV1", 1),
          ("trapV2", 2),
          ("trapV3", 3))
    )


_EquipManager2TrapVersion_Type.__name__ = "Integer32"
_EquipManager2TrapVersion_Object = MibScalar
equipManager2TrapVersion = _EquipManager2TrapVersion_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 1, 31),
    _EquipManager2TrapVersion_Type()
)
equipManager2TrapVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    equipManager2TrapVersion.setStatus("current")


class _EquipDailyPmTimeZone_Type(Integer32):
    """Custom type equipDailyPmTimeZone based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-12, 12),
    )


_EquipDailyPmTimeZone_Type.__name__ = "Integer32"
_EquipDailyPmTimeZone_Object = MibScalar
equipDailyPmTimeZone = _EquipDailyPmTimeZone_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 1, 32),
    _EquipDailyPmTimeZone_Type()
)
equipDailyPmTimeZone.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    equipDailyPmTimeZone.setStatus("current")


class _EquipOperationMngtControl_Type(Integer32):
    """Custom type equipOperationMngtControl based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notActive", 0),
          ("startOperation", 1),
          ("confirmOperation", 2))
    )


_EquipOperationMngtControl_Type.__name__ = "Integer32"
_EquipOperationMngtControl_Object = MibScalar
equipOperationMngtControl = _EquipOperationMngtControl_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 1, 33),
    _EquipOperationMngtControl_Type()
)
equipOperationMngtControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    equipOperationMngtControl.setStatus("current")
_EquipOperationMngtInProgress_Type = Integer32
_EquipOperationMngtInProgress_Object = MibScalar
equipOperationMngtInProgress = _EquipOperationMngtInProgress_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 1, 34),
    _EquipOperationMngtInProgress_Type()
)
equipOperationMngtInProgress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    equipOperationMngtInProgress.setStatus("current")


class _EquipLocation_Type(DisplayString):
    """Custom type equipLocation based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_EquipLocation_Type.__name__ = "DisplayString"
_EquipLocation_Object = MibScalar
equipLocation = _EquipLocation_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 1, 35),
    _EquipLocation_Type()
)
equipLocation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    equipLocation.setStatus("current")
_EquipLongitude_Type = Integer32
_EquipLongitude_Object = MibScalar
equipLongitude = _EquipLongitude_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 1, 36),
    _EquipLongitude_Type()
)
equipLongitude.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    equipLongitude.setStatus("current")
_EquipLatitude_Type = Integer32
_EquipLatitude_Object = MibScalar
equipLatitude = _EquipLatitude_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 1, 37),
    _EquipLatitude_Type()
)
equipLatitude.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    equipLatitude.setStatus("current")


class _EquipIpEthVlanId_Type(Integer32):
    """Custom type equipIpEthVlanId based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_EquipIpEthVlanId_Type.__name__ = "Integer32"
_EquipIpEthVlanId_Object = MibScalar
equipIpEthVlanId = _EquipIpEthVlanId_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 1, 38),
    _EquipIpEthVlanId_Type()
)
equipIpEthVlanId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    equipIpEthVlanId.setStatus("current")
_EquipIpEthDefGateway_Type = IpAddress
_EquipIpEthDefGateway_Object = MibScalar
equipIpEthDefGateway = _EquipIpEthDefGateway_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 1, 39),
    _EquipIpEthDefGateway_Type()
)
equipIpEthDefGateway.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    equipIpEthDefGateway.setStatus("current")


class _EquipIpEthDefGatewayIfIndex_Type(InterfaceIndex):
    """Custom type equipIpEthDefGatewayIfIndex based on InterfaceIndex"""
    subtypeSpec = InterfaceIndex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 999),
    )


_EquipIpEthDefGatewayIfIndex_Type.__name__ = "InterfaceIndex"
_EquipIpEthDefGatewayIfIndex_Object = MibScalar
equipIpEthDefGatewayIfIndex = _EquipIpEthDefGatewayIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 1, 40),
    _EquipIpEthDefGatewayIfIndex_Type()
)
equipIpEthDefGatewayIfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    equipIpEthDefGatewayIfIndex.setStatus("current")

# Managed Objects groups


# Notification objects

equipLOMConnectedMonitor = NotificationType(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 0, 109)
)
equipLOMConnectedMonitor.setObjects(
      *(("SIAE-EQUIP-MIB", "equipIpSnmpAgentAddress"),
        ("SIAE-EQUIP-MIB", "equipLOMConnected"))
)
if mibBuilder.loadTexts:
    equipLOMConnectedMonitor.setStatus(
        "current"
    )

equipLOMConnectedConfig = NotificationType(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 0, 110)
)
equipLOMConnectedConfig.setObjects(
      *(("SIAE-EQUIP-MIB", "equipIpSnmpAgentAddress"),
        ("SIAE-EQUIP-MIB", "equipLOMConnected"))
)
if mibBuilder.loadTexts:
    equipLOMConnectedConfig.setStatus(
        "current"
    )

equipLOMDisconnected = NotificationType(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 0, 111)
)
equipLOMDisconnected.setObjects(
      *(("SIAE-EQUIP-MIB", "equipIpSnmpAgentAddress"),
        ("SIAE-EQUIP-MIB", "equipLOMConnected"))
)
if mibBuilder.loadTexts:
    equipLOMDisconnected.setStatus(
        "current"
    )

equipConfigChangeStatus = NotificationType(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 0, 114)
)
equipConfigChangeStatus.setObjects(
      *(("SIAE-EQUIP-MIB", "equipIpSnmpAgentAddress"),
        ("SIAE-EQUIP-MIB", "equipConfigChange"))
)
if mibBuilder.loadTexts:
    equipConfigChangeStatus.setStatus(
        "current"
    )

equipManagerWakeUpNotify = NotificationType(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 0, 123)
)
equipManagerWakeUpNotify.setObjects(
      *(("SIAE-EQUIP-MIB", "equipIpSnmpAgentAddress"),
        ("SIAE-EQUIP-MIB", "equipStationID"),
        ("SIAE-EQUIP-MIB", "equipLocation"),
        ("SIAE-EQUIP-MIB", "equipIpSnmpAgentAddress"),
        ("SIAE-EQUIP-MIB", "equipGosipAddress"),
        ("SIAE-EQUIP-MIB", "equipManagerWakeUpIpAddr"),
        ("SIAE-EQUIP-MIB", "equipManagerWakeUpAlarm"))
)
if mibBuilder.loadTexts:
    equipManagerWakeUpNotify.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SIAE-EQUIP-MIB",
    **{"equipLOMConnectedMonitor": equipLOMConnectedMonitor,
       "equipLOMConnectedConfig": equipLOMConnectedConfig,
       "equipLOMDisconnected": equipLOMDisconnected,
       "equipConfigChangeStatus": equipConfigChangeStatus,
       "equipManagerWakeUpNotify": equipManagerWakeUpNotify,
       "equipment": equipment,
       "equipMibVersion": equipMibVersion,
       "equipCurrentTime": equipCurrentTime,
       "equipUpTime": equipUpTime,
       "equipType": equipType,
       "equipIpEthOsiAddress": equipIpEthOsiAddress,
       "equipGosipAddress": equipGosipAddress,
       "equipIpEthOsiNetMask": equipIpEthOsiNetMask,
       "equipL1L2IsIsRouting": equipL1L2IsIsRouting,
       "equipStationID": equipStationID,
       "equipLOMConfigEnable": equipLOMConfigEnable,
       "equipLOMConnected": equipLOMConnected,
       "equipLOMConnectedTrapEnable": equipLOMConnectedTrapEnable,
       "equipConfigChange": equipConfigChange,
       "equipConfigChangeTrapEnable": equipConfigChangeTrapEnable,
       "equipRequest": equipRequest,
       "equipIpEthAddress": equipIpEthAddress,
       "equipIpEthNetMask": equipIpEthNetMask,
       "equipOsiamParameter": equipOsiamParameter,
       "equipIpSnmpAgentAddress": equipIpSnmpAgentAddress,
       "equipOperationInProgress": equipOperationInProgress,
       "equipManagerWakeUpAlarm": equipManagerWakeUpAlarm,
       "equipManagerWakeUpAlarmSeverityCode": equipManagerWakeUpAlarmSeverityCode,
       "equipManagerWakeUpTimeout": equipManagerWakeUpTimeout,
       "equipManagerWakeUpIpAddr": equipManagerWakeUpIpAddr,
       "equipManagerWakeUpGosipAddress": equipManagerWakeUpGosipAddress,
       "equipManagerWakeUpTrapVersion": equipManagerWakeUpTrapVersion,
       "equipManager1IpAddr": equipManager1IpAddr,
       "equipManager2IpAddr": equipManager2IpAddr,
       "equipManager1TrapVersion": equipManager1TrapVersion,
       "equipManager2TrapVersion": equipManager2TrapVersion,
       "equipDailyPmTimeZone": equipDailyPmTimeZone,
       "equipOperationMngtControl": equipOperationMngtControl,
       "equipOperationMngtInProgress": equipOperationMngtInProgress,
       "equipLocation": equipLocation,
       "equipLongitude": equipLongitude,
       "equipLatitude": equipLatitude,
       "equipIpEthVlanId": equipIpEthVlanId,
       "equipIpEthDefGateway": equipIpEthDefGateway,
       "equipIpEthDefGatewayIfIndex": equipIpEthDefGatewayIfIndex}
)
