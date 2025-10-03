# SNMP MIB module (PDU-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\eaton\PDU-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:38:39 2025
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

(ModuleCompliance,
 NotificationGroup,
 ObjectGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup",
    "ObjectGroup")

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
 Opaque,
 TimeTicks,
 Unsigned32,
 enterprises,
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
    "Opaque",
    "TimeTicks",
    "Unsigned32",
    "enterprises",
    "iso")

(DisplayString,
 MacAddress,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

eaton = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 534)
)
if mibBuilder.loadTexts:
    eaton.setRevisions(
        ("2008-03-14 00:00",
         "2007-02-14 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class MilliAmps(TextualConvention, Unsigned32):
    status = "current"


class MilliVolts(TextualConvention, Unsigned32):
    status = "current"


class Watts(TextualConvention, Unsigned32):
    status = "current"


class VoltAmps(TextualConvention, Unsigned32):
    status = "current"


class DegreesCelsius(TextualConvention, Unsigned32):
    status = "current"


class Hertz(TextualConvention, Unsigned32):
    status = "current"


class RelativeHumidity(TextualConvention, Unsigned32):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )



class PowerFactorPercentage(TextualConvention, Unsigned32):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )



class SensorTypeEnumeration(TextualConvention, Integer32):
    status = "current"
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
              200,
              201,
              202,
              203,
              300,
              301,
              302,
              303,
              304,
              305,
              306,
              307,
              400,
              401,
              402,
              403,
              404,
              405,
              406,
              407,
              500,
              501,
              502,
              503,
              504,
              505,
              550,
              551,
              552,
              600,
              601,
              602)
        )
    )
    namedValues = NamedValues(
        *(("outletCurrent", 0),
          ("outletMaxCurrent", 1),
          ("outletVoltage", 2),
          ("outletActivePower", 3),
          ("outletApparentPower", 4),
          ("outletMaxActivePower", 5),
          ("outletAverageActivePower", 6),
          ("outletPowerFactor", 7),
          ("powerBranchVoltage", 200),
          ("powerBranchFrequency", 201),
          ("powerBranchTemperature", 202),
          ("powerBranchCurrent", 203),
          ("environmentalTemp1", 300),
          ("environmentalTemp2", 301),
          ("environmentalTemp3", 302),
          ("environmentalTemp4", 303),
          ("environmentalTemp5", 304),
          ("environmentalTemp6", 305),
          ("environmentalTemp7", 306),
          ("environmentalTemp8", 307),
          ("environmentalHumidity1", 400),
          ("environmentalHumidity2", 401),
          ("environmentalHumidity3", 402),
          ("environmentalHumidity4", 403),
          ("environmentalHumidity5", 404),
          ("environmentalHumidity6", 405),
          ("environmentalHumidity7", 406),
          ("environmentalHumidity8", 407),
          ("unitRmsCurrent", 500),
          ("unitMaxRmsCurrent", 501),
          ("unitVoltage", 502),
          ("unitCpuTemp", 503),
          ("unitActivePower", 504),
          ("unitApparentPower", 505),
          ("unitCircuitBreak0State", 550),
          ("unitCircuitBreak1State", 551),
          ("unitCircuitBreak2State", 552),
          ("unitCircuitBreak0Current", 600),
          ("unitCircuitBreak1Current", 601),
          ("unitCircuitBreak2Current", 602))
    )



class SensorStateEnumeration(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("unavailable", -1),
          ("ok", 0),
          ("belowLowerWarning", 1),
          ("aboveUpperWarning", 2),
          ("belowLowerCritical", 3),
          ("aboveUpperCritical", 4))
    )



# MIB Managed Objects in the order of their OIDs

_Product_ObjectIdentity = ObjectIdentity
product = _Product_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 534, 6)
)
_Pduagent_ObjectIdentity = ObjectIdentity
pduagent = _Pduagent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 534, 6, 6)
)
_Pdu_ObjectIdentity = ObjectIdentity
pdu = _Pdu_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 534, 6, 6, 6)
)
_Traps_ObjectIdentity = ObjectIdentity
traps = _Traps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 534, 6, 6, 6, 0)
)
_Board_ObjectIdentity = ObjectIdentity
board = _Board_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 534, 6, 6, 6, 1)
)
_Info_ObjectIdentity = ObjectIdentity
info = _Info_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 534, 6, 6, 6, 1, 1)
)
_FirmwareVersion_Type = DisplayString
_FirmwareVersion_Object = MibScalar
firmwareVersion = _FirmwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 6, 6, 1, 1, 1),
    _FirmwareVersion_Type()
)
firmwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    firmwareVersion.setStatus("current")
_SerialNumber_Type = DisplayString
_SerialNumber_Object = MibScalar
serialNumber = _SerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 6, 6, 1, 1, 2),
    _SerialNumber_Type()
)
serialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serialNumber.setStatus("current")
_IpAddress_Type = IpAddress
_IpAddress_Object = MibScalar
ipAddress = _IpAddress_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 6, 6, 1, 1, 3),
    _IpAddress_Type()
)
ipAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipAddress.setStatus("current")
_Netmask_Type = IpAddress
_Netmask_Object = MibScalar
netmask = _Netmask_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 6, 6, 1, 1, 4),
    _Netmask_Type()
)
netmask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netmask.setStatus("current")
_Gateway_Type = IpAddress
_Gateway_Object = MibScalar
gateway = _Gateway_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 6, 6, 1, 1, 5),
    _Gateway_Type()
)
gateway.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gateway.setStatus("current")
_Mac_Type = MacAddress
_Mac_Object = MibScalar
mac = _Mac_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 6, 6, 1, 1, 6),
    _Mac_Type()
)
mac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mac.setStatus("current")


class _HardwareRev_Type(Integer32):
    """Custom type hardwareRev based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_HardwareRev_Type.__name__ = "Integer32"
_HardwareRev_Object = MibScalar
hardwareRev = _HardwareRev_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 6, 6, 1, 1, 7),
    _HardwareRev_Type()
)
hardwareRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hardwareRev.setStatus("current")
_UserName_Type = DisplayString
_UserName_Object = MibScalar
userName = _UserName_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 6, 6, 1, 1, 10),
    _UserName_Type()
)
userName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    userName.setStatus("current")
_ObjectName_Type = DisplayString
_ObjectName_Object = MibScalar
objectName = _ObjectName_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 6, 6, 1, 1, 12),
    _ObjectName_Type()
)
objectName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    objectName.setStatus("current")
_ObjectInstance_Type = DisplayString
_ObjectInstance_Object = MibScalar
objectInstance = _ObjectInstance_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 6, 6, 1, 1, 13),
    _ObjectInstance_Type()
)
objectInstance.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    objectInstance.setStatus("current")
_TargetUser_Type = DisplayString
_TargetUser_Object = MibScalar
targetUser = _TargetUser_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 6, 6, 1, 1, 14),
    _TargetUser_Type()
)
targetUser.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    targetUser.setStatus("current")
_GroupName_Type = DisplayString
_GroupName_Object = MibScalar
groupName = _GroupName_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 6, 6, 1, 1, 15),
    _GroupName_Type()
)
groupName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    groupName.setStatus("current")
_ImageVersion_Type = DisplayString
_ImageVersion_Object = MibScalar
imageVersion = _ImageVersion_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 6, 6, 1, 1, 18),
    _ImageVersion_Type()
)
imageVersion.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    imageVersion.setStatus("current")
_SensorDescr_Type = DisplayString
_SensorDescr_Object = MibScalar
sensorDescr = _SensorDescr_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 6, 6, 1, 1, 19),
    _SensorDescr_Type()
)
sensorDescr.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    sensorDescr.setStatus("current")
_ThresholdDescr_Type = DisplayString
_ThresholdDescr_Object = MibScalar
thresholdDescr = _ThresholdDescr_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 6, 6, 1, 1, 20),
    _ThresholdDescr_Type()
)
thresholdDescr.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    thresholdDescr.setStatus("current")
_ThresholdSeverity_Type = DisplayString
_ThresholdSeverity_Object = MibScalar
thresholdSeverity = _ThresholdSeverity_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 6, 6, 1, 1, 21),
    _ThresholdSeverity_Type()
)
thresholdSeverity.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    thresholdSeverity.setStatus("current")
_ThresholdEventType_Type = DisplayString
_ThresholdEventType_Object = MibScalar
thresholdEventType = _ThresholdEventType_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 6, 6, 1, 1, 22),
    _ThresholdEventType_Type()
)
thresholdEventType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    thresholdEventType.setStatus("current")
_Status_Type = DisplayString
_Status_Object = MibScalar
status = _Status_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 6, 6, 1, 1, 23),
    _Status_Type()
)
status.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    status.setStatus("current")
_SlaveIpAddress_Type = IpAddress
_SlaveIpAddress_Object = MibScalar
slaveIpAddress = _SlaveIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 6, 6, 1, 1, 24),
    _SlaveIpAddress_Type()
)
slaveIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slaveIpAddress.setStatus("current")
_Outlets_ObjectIdentity = ObjectIdentity
outlets = _Outlets_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 534, 6, 6, 6, 1, 2)
)
_OutletCount_Type = Integer32
_OutletCount_Object = MibScalar
outletCount = _OutletCount_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 6, 6, 1, 2, 1),
    _OutletCount_Type()
)
outletCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outletCount.setStatus("current")
_OutletTable_Object = MibTable
outletTable = _OutletTable_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 6, 6, 1, 2, 2)
)
if mibBuilder.loadTexts:
    outletTable.setStatus("current")
_OutletEntry_Object = MibTableRow
outletEntry = _OutletEntry_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 6, 6, 1, 2, 2, 1)
)
outletEntry.setIndexNames(
    (0, "PDU-MIB", "outletIndex"),
)
if mibBuilder.loadTexts:
    outletEntry.setStatus("current")


class _OutletIndex_Type(Integer32):
    """Custom type outletIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_OutletIndex_Type.__name__ = "Integer32"
_OutletIndex_Object = MibTableColumn
outletIndex = _OutletIndex_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 6, 6, 1, 2, 2, 1, 1),
    _OutletIndex_Type()
)
outletIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outletIndex.setStatus("current")
_OutletLabel_Type = DisplayString
_OutletLabel_Object = MibTableColumn
outletLabel = _OutletLabel_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 6, 6, 1, 2, 2, 1, 2),
    _OutletLabel_Type()
)
outletLabel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outletLabel.setStatus("current")


class _OutletOperationalState_Type(Integer32):
    """Custom type outletOperationalState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("error", -1),
          ("off", 0),
          ("on", 1),
          ("cycling", 2))
    )


_OutletOperationalState_Type.__name__ = "Integer32"
_OutletOperationalState_Object = MibTableColumn
outletOperationalState = _OutletOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 6, 6, 1, 2, 2, 1, 3),
    _OutletOperationalState_Type()
)
outletOperationalState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outletOperationalState.setStatus("current")
_OutletCurrent_Type = MilliAmps
_OutletCurrent_Object = MibTableColumn
outletCurrent = _OutletCurrent_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 6, 6, 1, 2, 2, 1, 4),
    _OutletCurrent_Type()
)
outletCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outletCurrent.setStatus("current")
_OutletMaxCurrent_Type = MilliAmps
_OutletMaxCurrent_Object = MibTableColumn
outletMaxCurrent = _OutletMaxCurrent_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 6, 6, 1, 2, 2, 1, 5),
    _OutletMaxCurrent_Type()
)
outletMaxCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outletMaxCurrent.setStatus("current")
_OutletVoltage_Type = MilliVolts
_OutletVoltage_Object = MibTableColumn
outletVoltage = _OutletVoltage_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 6, 6, 1, 2, 2, 1, 6),
    _OutletVoltage_Type()
)
outletVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outletVoltage.setStatus("current")
_OutletActivePower_Type = Watts
_OutletActivePower_Object = MibTableColumn
outletActivePower = _OutletActivePower_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 6, 6, 1, 2, 2, 1, 7),
    _OutletActivePower_Type()
)
outletActivePower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outletActivePower.setStatus("current")
_OutletApparentPower_Type = VoltAmps
_OutletApparentPower_Object = MibTableColumn
outletApparentPower = _OutletApparentPower_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 6, 6, 1, 2, 2, 1, 8),
    _OutletApparentPower_Type()
)
outletApparentPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outletApparentPower.setStatus("current")
_OutletPowerFactor_Type = PowerFactorPercentage
_OutletPowerFactor_Object = MibTableColumn
outletPowerFactor = _OutletPowerFactor_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 6, 6, 1, 2, 2, 1, 9),
    _OutletPowerFactor_Type()
)
outletPowerFactor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outletPowerFactor.setStatus("current")
_OutletCurrentUpperWarning_Type = MilliAmps
_OutletCurrentUpperWarning_Object = MibTableColumn
outletCurrentUpperWarning = _OutletCurrentUpperWarning_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 6, 6, 1, 2, 2, 1, 21),
    _OutletCurrentUpperWarning_Type()
)
outletCurrentUpperWarning.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outletCurrentUpperWarning.setStatus("current")
_OutletCurrentUpperCritical_Type = MilliAmps
_OutletCurrentUpperCritical_Object = MibTableColumn
outletCurrentUpperCritical = _OutletCurrentUpperCritical_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 6, 6, 1, 2, 2, 1, 23),
    _OutletCurrentUpperCritical_Type()
)
outletCurrentUpperCritical.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outletCurrentUpperCritical.setStatus("current")
_Unit_ObjectIdentity = ObjectIdentity
unit = _Unit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 534, 6, 6, 6, 1, 3)
)
_UnitReadings_ObjectIdentity = ObjectIdentity
unitReadings = _UnitReadings_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 534, 6, 6, 6, 1, 3, 1)
)
_UnitCurrent_Type = MilliAmps
_UnitCurrent_Object = MibScalar
unitCurrent = _UnitCurrent_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 6, 6, 1, 3, 1, 1),
    _UnitCurrent_Type()
)
unitCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    unitCurrent.setStatus("current")
_UnitVoltage_Type = MilliVolts
_UnitVoltage_Object = MibScalar
unitVoltage = _UnitVoltage_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 6, 6, 1, 3, 1, 2),
    _UnitVoltage_Type()
)
unitVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    unitVoltage.setStatus("current")
_UnitActivePower_Type = Watts
_UnitActivePower_Object = MibScalar
unitActivePower = _UnitActivePower_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 6, 6, 1, 3, 1, 3),
    _UnitActivePower_Type()
)
unitActivePower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    unitActivePower.setStatus("current")
_UnitApparentPower_Type = Watts
_UnitApparentPower_Object = MibScalar
unitApparentPower = _UnitApparentPower_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 6, 6, 1, 3, 1, 4),
    _UnitApparentPower_Type()
)
unitApparentPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    unitApparentPower.setStatus("current")
_UnitCpuTemp_Type = DegreesCelsius
_UnitCpuTemp_Object = MibScalar
unitCpuTemp = _UnitCpuTemp_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 6, 6, 1, 3, 1, 5),
    _UnitCpuTemp_Type()
)
unitCpuTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    unitCpuTemp.setStatus("current")


class _UnitCircuitBreak0State_Type(Integer32):
    """Custom type unitCircuitBreak0State based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("unavailable", -1),
          ("ok", 0),
          ("tripped", 1))
    )


_UnitCircuitBreak0State_Type.__name__ = "Integer32"
_UnitCircuitBreak0State_Object = MibScalar
unitCircuitBreak0State = _UnitCircuitBreak0State_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 6, 6, 1, 3, 1, 20),
    _UnitCircuitBreak0State_Type()
)
unitCircuitBreak0State.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    unitCircuitBreak0State.setStatus("current")


class _UnitCircuitBreak1State_Type(Integer32):
    """Custom type unitCircuitBreak1State based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("unavailable", -1),
          ("ok", 0),
          ("tripped", 1))
    )


_UnitCircuitBreak1State_Type.__name__ = "Integer32"
_UnitCircuitBreak1State_Object = MibScalar
unitCircuitBreak1State = _UnitCircuitBreak1State_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 6, 6, 1, 3, 1, 21),
    _UnitCircuitBreak1State_Type()
)
unitCircuitBreak1State.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    unitCircuitBreak1State.setStatus("current")


class _UnitCircuitBreak2State_Type(Integer32):
    """Custom type unitCircuitBreak2State based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("unavailable", -1),
          ("ok", 0),
          ("tripped", 1))
    )


_UnitCircuitBreak2State_Type.__name__ = "Integer32"
_UnitCircuitBreak2State_Object = MibScalar
unitCircuitBreak2State = _UnitCircuitBreak2State_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 6, 6, 1, 3, 1, 22),
    _UnitCircuitBreak2State_Type()
)
unitCircuitBreak2State.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    unitCircuitBreak2State.setStatus("current")
_UnitCircuitBreak0Current_Type = MilliAmps
_UnitCircuitBreak0Current_Object = MibScalar
unitCircuitBreak0Current = _UnitCircuitBreak0Current_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 6, 6, 1, 3, 1, 40),
    _UnitCircuitBreak0Current_Type()
)
unitCircuitBreak0Current.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    unitCircuitBreak0Current.setStatus("current")
_UnitCircuitBreak1Current_Type = MilliAmps
_UnitCircuitBreak1Current_Object = MibScalar
unitCircuitBreak1Current = _UnitCircuitBreak1Current_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 6, 6, 1, 3, 1, 41),
    _UnitCircuitBreak1Current_Type()
)
unitCircuitBreak1Current.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    unitCircuitBreak1Current.setStatus("current")
_UnitCircuitBreak2Current_Type = MilliAmps
_UnitCircuitBreak2Current_Object = MibScalar
unitCircuitBreak2Current = _UnitCircuitBreak2Current_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 6, 6, 1, 3, 1, 42),
    _UnitCircuitBreak2Current_Type()
)
unitCircuitBreak2Current.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    unitCircuitBreak2Current.setStatus("current")
_UnitVoltageLowerWarning_Type = MilliVolts
_UnitVoltageLowerWarning_Object = MibScalar
unitVoltageLowerWarning = _UnitVoltageLowerWarning_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 6, 6, 1, 3, 1, 60),
    _UnitVoltageLowerWarning_Type()
)
unitVoltageLowerWarning.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    unitVoltageLowerWarning.setStatus("current")
_UnitVoltageLowerCritical_Type = MilliVolts
_UnitVoltageLowerCritical_Object = MibScalar
unitVoltageLowerCritical = _UnitVoltageLowerCritical_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 6, 6, 1, 3, 1, 61),
    _UnitVoltageLowerCritical_Type()
)
unitVoltageLowerCritical.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    unitVoltageLowerCritical.setStatus("current")
_UnitVoltageUpperWarning_Type = MilliVolts
_UnitVoltageUpperWarning_Object = MibScalar
unitVoltageUpperWarning = _UnitVoltageUpperWarning_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 6, 6, 1, 3, 1, 62),
    _UnitVoltageUpperWarning_Type()
)
unitVoltageUpperWarning.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    unitVoltageUpperWarning.setStatus("current")
_UnitVoltageUpperCritical_Type = MilliVolts
_UnitVoltageUpperCritical_Object = MibScalar
unitVoltageUpperCritical = _UnitVoltageUpperCritical_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 6, 6, 1, 3, 1, 63),
    _UnitVoltageUpperCritical_Type()
)
unitVoltageUpperCritical.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    unitVoltageUpperCritical.setStatus("current")
_UnitCurrentUpperWarning_Type = MilliAmps
_UnitCurrentUpperWarning_Object = MibScalar
unitCurrentUpperWarning = _UnitCurrentUpperWarning_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 6, 6, 1, 3, 1, 70),
    _UnitCurrentUpperWarning_Type()
)
unitCurrentUpperWarning.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    unitCurrentUpperWarning.setStatus("current")
_UnitCurrentUpperCritical_Type = MilliAmps
_UnitCurrentUpperCritical_Object = MibScalar
unitCurrentUpperCritical = _UnitCurrentUpperCritical_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 6, 6, 1, 3, 1, 71),
    _UnitCurrentUpperCritical_Type()
)
unitCurrentUpperCritical.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    unitCurrentUpperCritical.setStatus("current")
_UnitTempLowerWarning_Type = DegreesCelsius
_UnitTempLowerWarning_Object = MibScalar
unitTempLowerWarning = _UnitTempLowerWarning_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 6, 6, 1, 3, 1, 80),
    _UnitTempLowerWarning_Type()
)
unitTempLowerWarning.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    unitTempLowerWarning.setStatus("current")
_UnitTempLowerCritical_Type = DegreesCelsius
_UnitTempLowerCritical_Object = MibScalar
unitTempLowerCritical = _UnitTempLowerCritical_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 6, 6, 1, 3, 1, 81),
    _UnitTempLowerCritical_Type()
)
unitTempLowerCritical.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    unitTempLowerCritical.setStatus("current")
_UnitTempUpperWarning_Type = DegreesCelsius
_UnitTempUpperWarning_Object = MibScalar
unitTempUpperWarning = _UnitTempUpperWarning_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 6, 6, 1, 3, 1, 82),
    _UnitTempUpperWarning_Type()
)
unitTempUpperWarning.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    unitTempUpperWarning.setStatus("current")
_UnitTempUpperCritical_Type = DegreesCelsius
_UnitTempUpperCritical_Object = MibScalar
unitTempUpperCritical = _UnitTempUpperCritical_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 6, 6, 1, 3, 1, 83),
    _UnitTempUpperCritical_Type()
)
unitTempUpperCritical.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    unitTempUpperCritical.setStatus("current")
_Environmental_ObjectIdentity = ObjectIdentity
environmental = _Environmental_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 534, 6, 6, 6, 2)
)
_TempSensorCount_Type = Integer32
_TempSensorCount_Object = MibScalar
tempSensorCount = _TempSensorCount_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 6, 6, 2, 1),
    _TempSensorCount_Type()
)
tempSensorCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tempSensorCount.setStatus("current")
_TempSensorTable_Object = MibTable
tempSensorTable = _TempSensorTable_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 6, 6, 2, 2)
)
if mibBuilder.loadTexts:
    tempSensorTable.setStatus("current")
_TempSensorEntry_Object = MibTableRow
tempSensorEntry = _TempSensorEntry_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 6, 6, 2, 2, 1)
)
tempSensorEntry.setIndexNames(
    (0, "PDU-MIB", "tempSensorIndex"),
)
if mibBuilder.loadTexts:
    tempSensorEntry.setStatus("current")


class _TempSensorIndex_Type(Integer32):
    """Custom type tempSensorIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_TempSensorIndex_Type.__name__ = "Integer32"
_TempSensorIndex_Object = MibTableColumn
tempSensorIndex = _TempSensorIndex_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 6, 6, 2, 2, 1, 1),
    _TempSensorIndex_Type()
)
tempSensorIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tempSensorIndex.setStatus("current")
_TempSensorLabel_Type = DisplayString
_TempSensorLabel_Object = MibTableColumn
tempSensorLabel = _TempSensorLabel_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 6, 6, 2, 2, 1, 2),
    _TempSensorLabel_Type()
)
tempSensorLabel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tempSensorLabel.setStatus("current")
_Temperature_Type = DegreesCelsius
_Temperature_Object = MibTableColumn
temperature = _Temperature_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 6, 6, 2, 2, 1, 3),
    _Temperature_Type()
)
temperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    temperature.setStatus("current")
_TempLowerWarning_Type = DegreesCelsius
_TempLowerWarning_Object = MibTableColumn
tempLowerWarning = _TempLowerWarning_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 6, 6, 2, 2, 1, 4),
    _TempLowerWarning_Type()
)
tempLowerWarning.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tempLowerWarning.setStatus("current")
_TempUpperWarning_Type = DegreesCelsius
_TempUpperWarning_Object = MibTableColumn
tempUpperWarning = _TempUpperWarning_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 6, 6, 2, 2, 1, 5),
    _TempUpperWarning_Type()
)
tempUpperWarning.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tempUpperWarning.setStatus("current")
_TempLowerCritical_Type = DegreesCelsius
_TempLowerCritical_Object = MibTableColumn
tempLowerCritical = _TempLowerCritical_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 6, 6, 2, 2, 1, 6),
    _TempLowerCritical_Type()
)
tempLowerCritical.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tempLowerCritical.setStatus("current")
_TempUpperCritical_Type = DegreesCelsius
_TempUpperCritical_Object = MibTableColumn
tempUpperCritical = _TempUpperCritical_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 6, 6, 2, 2, 1, 7),
    _TempUpperCritical_Type()
)
tempUpperCritical.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tempUpperCritical.setStatus("current")
_TempLowerWarningReset_Type = DegreesCelsius
_TempLowerWarningReset_Object = MibTableColumn
tempLowerWarningReset = _TempLowerWarningReset_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 6, 6, 2, 2, 1, 8),
    _TempLowerWarningReset_Type()
)
tempLowerWarningReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tempLowerWarningReset.setStatus("current")
_TempUpperWarningReset_Type = DegreesCelsius
_TempUpperWarningReset_Object = MibTableColumn
tempUpperWarningReset = _TempUpperWarningReset_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 6, 6, 2, 2, 1, 9),
    _TempUpperWarningReset_Type()
)
tempUpperWarningReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tempUpperWarningReset.setStatus("current")
_TempLowerCriticalReset_Type = DegreesCelsius
_TempLowerCriticalReset_Object = MibTableColumn
tempLowerCriticalReset = _TempLowerCriticalReset_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 6, 6, 2, 2, 1, 10),
    _TempLowerCriticalReset_Type()
)
tempLowerCriticalReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tempLowerCriticalReset.setStatus("current")
_TempUpperCriticalReset_Type = DegreesCelsius
_TempUpperCriticalReset_Object = MibTableColumn
tempUpperCriticalReset = _TempUpperCriticalReset_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 6, 6, 2, 2, 1, 11),
    _TempUpperCriticalReset_Type()
)
tempUpperCriticalReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tempUpperCriticalReset.setStatus("current")
_HumiditySensorCount_Type = Integer32
_HumiditySensorCount_Object = MibScalar
humiditySensorCount = _HumiditySensorCount_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 6, 6, 2, 3),
    _HumiditySensorCount_Type()
)
humiditySensorCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    humiditySensorCount.setStatus("current")
_HumiditySensorTable_Object = MibTable
humiditySensorTable = _HumiditySensorTable_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 6, 6, 2, 4)
)
if mibBuilder.loadTexts:
    humiditySensorTable.setStatus("current")
_HumiditySensorEntry_Object = MibTableRow
humiditySensorEntry = _HumiditySensorEntry_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 6, 6, 2, 4, 1)
)
humiditySensorEntry.setIndexNames(
    (0, "PDU-MIB", "humiditySensorIndex"),
)
if mibBuilder.loadTexts:
    humiditySensorEntry.setStatus("current")


class _HumiditySensorIndex_Type(Integer32):
    """Custom type humiditySensorIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_HumiditySensorIndex_Type.__name__ = "Integer32"
_HumiditySensorIndex_Object = MibTableColumn
humiditySensorIndex = _HumiditySensorIndex_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 6, 6, 2, 4, 1, 1),
    _HumiditySensorIndex_Type()
)
humiditySensorIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    humiditySensorIndex.setStatus("current")
_HumiditySensorLabel_Type = DisplayString
_HumiditySensorLabel_Object = MibTableColumn
humiditySensorLabel = _HumiditySensorLabel_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 6, 6, 2, 4, 1, 2),
    _HumiditySensorLabel_Type()
)
humiditySensorLabel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    humiditySensorLabel.setStatus("current")
_Humidity_Type = RelativeHumidity
_Humidity_Object = MibTableColumn
humidity = _Humidity_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 6, 6, 2, 4, 1, 3),
    _Humidity_Type()
)
humidity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    humidity.setStatus("current")
_HumidityLowerWarning_Type = RelativeHumidity
_HumidityLowerWarning_Object = MibTableColumn
humidityLowerWarning = _HumidityLowerWarning_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 6, 6, 2, 4, 1, 4),
    _HumidityLowerWarning_Type()
)
humidityLowerWarning.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    humidityLowerWarning.setStatus("current")
_HumidityUpperWarning_Type = RelativeHumidity
_HumidityUpperWarning_Object = MibTableColumn
humidityUpperWarning = _HumidityUpperWarning_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 6, 6, 2, 4, 1, 5),
    _HumidityUpperWarning_Type()
)
humidityUpperWarning.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    humidityUpperWarning.setStatus("current")
_HumidityLowerCritical_Type = RelativeHumidity
_HumidityLowerCritical_Object = MibTableColumn
humidityLowerCritical = _HumidityLowerCritical_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 6, 6, 2, 4, 1, 6),
    _HumidityLowerCritical_Type()
)
humidityLowerCritical.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    humidityLowerCritical.setStatus("current")
_HumidityUpperCritical_Type = RelativeHumidity
_HumidityUpperCritical_Object = MibTableColumn
humidityUpperCritical = _HumidityUpperCritical_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 6, 6, 2, 4, 1, 7),
    _HumidityUpperCritical_Type()
)
humidityUpperCritical.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    humidityUpperCritical.setStatus("current")
_HumidityLowerWarningReset_Type = RelativeHumidity
_HumidityLowerWarningReset_Object = MibTableColumn
humidityLowerWarningReset = _HumidityLowerWarningReset_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 6, 6, 2, 4, 1, 8),
    _HumidityLowerWarningReset_Type()
)
humidityLowerWarningReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    humidityLowerWarningReset.setStatus("current")
_HumidityUpperWarningReset_Type = RelativeHumidity
_HumidityUpperWarningReset_Object = MibTableColumn
humidityUpperWarningReset = _HumidityUpperWarningReset_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 6, 6, 2, 4, 1, 9),
    _HumidityUpperWarningReset_Type()
)
humidityUpperWarningReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    humidityUpperWarningReset.setStatus("current")
_HumidityLowerCriticalReset_Type = RelativeHumidity
_HumidityLowerCriticalReset_Object = MibTableColumn
humidityLowerCriticalReset = _HumidityLowerCriticalReset_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 6, 6, 2, 4, 1, 10),
    _HumidityLowerCriticalReset_Type()
)
humidityLowerCriticalReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    humidityLowerCriticalReset.setStatus("current")
_HumidityUpperCriticalReset_Type = RelativeHumidity
_HumidityUpperCriticalReset_Object = MibTableColumn
humidityUpperCriticalReset = _HumidityUpperCriticalReset_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 6, 6, 2, 4, 1, 11),
    _HumidityUpperCriticalReset_Type()
)
humidityUpperCriticalReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    humidityUpperCriticalReset.setStatus("current")
_Conformance_ObjectIdentity = ObjectIdentity
conformance = _Conformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 534, 6, 6, 6, 9)
)
_Compliances_ObjectIdentity = ObjectIdentity
compliances = _Compliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 534, 6, 6, 6, 9, 1)
)
_Groups_ObjectIdentity = ObjectIdentity
groups = _Groups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 534, 6, 6, 6, 9, 2)
)

# Managed Objects groups

infoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 534, 6, 6, 6, 9, 2, 1)
)
infoGroup.setObjects(
      *(("PDU-MIB", "firmwareVersion"),
        ("PDU-MIB", "serialNumber"),
        ("PDU-MIB", "ipAddress"),
        ("PDU-MIB", "netmask"),
        ("PDU-MIB", "gateway"),
        ("PDU-MIB", "mac"),
        ("PDU-MIB", "hardwareRev"),
        ("PDU-MIB", "userName"),
        ("PDU-MIB", "objectName"),
        ("PDU-MIB", "objectInstance"),
        ("PDU-MIB", "targetUser"),
        ("PDU-MIB", "groupName"),
        ("PDU-MIB", "imageVersion"),
        ("PDU-MIB", "sensorDescr"),
        ("PDU-MIB", "thresholdDescr"),
        ("PDU-MIB", "thresholdSeverity"),
        ("PDU-MIB", "thresholdEventType"),
        ("PDU-MIB", "status"),
        ("PDU-MIB", "slaveIpAddress"))
)
if mibBuilder.loadTexts:
    infoGroup.setStatus("current")

outletsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 534, 6, 6, 6, 9, 2, 2)
)
outletsGroup.setObjects(
      *(("PDU-MIB", "outletCount"),
        ("PDU-MIB", "outletLabel"),
        ("PDU-MIB", "outletOperationalState"),
        ("PDU-MIB", "outletCurrent"),
        ("PDU-MIB", "outletMaxCurrent"),
        ("PDU-MIB", "outletVoltage"),
        ("PDU-MIB", "outletActivePower"),
        ("PDU-MIB", "outletApparentPower"),
        ("PDU-MIB", "outletPowerFactor"),
        ("PDU-MIB", "outletCurrentUpperWarning"),
        ("PDU-MIB", "outletCurrentUpperCritical"))
)
if mibBuilder.loadTexts:
    outletsGroup.setStatus("current")

unitSensorsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 534, 6, 6, 6, 9, 2, 4)
)
unitSensorsGroup.setObjects(
      *(("PDU-MIB", "unitCurrent"),
        ("PDU-MIB", "unitVoltage"),
        ("PDU-MIB", "unitActivePower"),
        ("PDU-MIB", "unitApparentPower"),
        ("PDU-MIB", "unitCpuTemp"),
        ("PDU-MIB", "unitCircuitBreak0State"),
        ("PDU-MIB", "unitCircuitBreak1State"),
        ("PDU-MIB", "unitCircuitBreak2State"),
        ("PDU-MIB", "unitCircuitBreak0Current"),
        ("PDU-MIB", "unitCircuitBreak1Current"),
        ("PDU-MIB", "unitCircuitBreak2Current"),
        ("PDU-MIB", "unitVoltageLowerWarning"),
        ("PDU-MIB", "unitVoltageUpperWarning"),
        ("PDU-MIB", "unitVoltageLowerCritical"),
        ("PDU-MIB", "unitVoltageUpperCritical"),
        ("PDU-MIB", "unitCurrentUpperWarning"),
        ("PDU-MIB", "unitCurrentUpperCritical"),
        ("PDU-MIB", "unitTempLowerWarning"),
        ("PDU-MIB", "unitTempUpperWarning"),
        ("PDU-MIB", "unitTempLowerCritical"),
        ("PDU-MIB", "unitTempUpperCritical"))
)
if mibBuilder.loadTexts:
    unitSensorsGroup.setStatus("current")

externalTemperatureGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 534, 6, 6, 6, 9, 2, 6)
)
externalTemperatureGroup.setObjects(
      *(("PDU-MIB", "tempSensorCount"),
        ("PDU-MIB", "tempSensorLabel"),
        ("PDU-MIB", "temperature"),
        ("PDU-MIB", "tempLowerWarning"),
        ("PDU-MIB", "tempUpperWarning"),
        ("PDU-MIB", "tempLowerCritical"),
        ("PDU-MIB", "tempUpperCritical"),
        ("PDU-MIB", "tempLowerWarningReset"),
        ("PDU-MIB", "tempUpperWarningReset"),
        ("PDU-MIB", "tempLowerCriticalReset"),
        ("PDU-MIB", "tempUpperCriticalReset"))
)
if mibBuilder.loadTexts:
    externalTemperatureGroup.setStatus("current")

externalHumidityGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 534, 6, 6, 6, 9, 2, 7)
)
externalHumidityGroup.setObjects(
      *(("PDU-MIB", "humiditySensorCount"),
        ("PDU-MIB", "humiditySensorLabel"),
        ("PDU-MIB", "humidity"),
        ("PDU-MIB", "humidityLowerWarning"),
        ("PDU-MIB", "humidityUpperWarning"),
        ("PDU-MIB", "humidityLowerCritical"),
        ("PDU-MIB", "humidityUpperCritical"),
        ("PDU-MIB", "humidityLowerWarningReset"),
        ("PDU-MIB", "humidityUpperWarningReset"),
        ("PDU-MIB", "humidityLowerCriticalReset"),
        ("PDU-MIB", "humidityUpperCriticalReset"))
)
if mibBuilder.loadTexts:
    externalHumidityGroup.setStatus("current")


# Notification objects

rebootStarted = NotificationType(
    (1, 3, 6, 1, 4, 1, 534, 6, 6, 6, 0, 1)
)
rebootStarted.setObjects(
      *(("PDU-MIB", "objectName"),
        ("PDU-MIB", "objectInstance"),
        ("PDU-MIB", "userName"))
)
if mibBuilder.loadTexts:
    rebootStarted.setStatus(
        "current"
    )

rebootCompleted = NotificationType(
    (1, 3, 6, 1, 4, 1, 534, 6, 6, 6, 0, 2)
)
rebootCompleted.setObjects(
      *(("PDU-MIB", "objectName"),
        ("PDU-MIB", "objectInstance"))
)
if mibBuilder.loadTexts:
    rebootCompleted.setStatus(
        "current"
    )

userLogin = NotificationType(
    (1, 3, 6, 1, 4, 1, 534, 6, 6, 6, 0, 3)
)
userLogin.setObjects(
      *(("PDU-MIB", "objectName"),
        ("PDU-MIB", "objectInstance"),
        ("PDU-MIB", "userName"),
        ("PDU-MIB", "ipAddress"))
)
if mibBuilder.loadTexts:
    userLogin.setStatus(
        "current"
    )

userLogout = NotificationType(
    (1, 3, 6, 1, 4, 1, 534, 6, 6, 6, 0, 4)
)
userLogout.setObjects(
      *(("PDU-MIB", "objectName"),
        ("PDU-MIB", "objectInstance"),
        ("PDU-MIB", "userName"),
        ("PDU-MIB", "ipAddress"))
)
if mibBuilder.loadTexts:
    userLogout.setStatus(
        "current"
    )

userAuthenticationFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 534, 6, 6, 6, 0, 5)
)
userAuthenticationFailure.setObjects(
      *(("PDU-MIB", "objectName"),
        ("PDU-MIB", "objectInstance"),
        ("PDU-MIB", "userName"),
        ("PDU-MIB", "ipAddress"))
)
if mibBuilder.loadTexts:
    userAuthenticationFailure.setStatus(
        "current"
    )

userSessionTimeout = NotificationType(
    (1, 3, 6, 1, 4, 1, 534, 6, 6, 6, 0, 8)
)
userSessionTimeout.setObjects(
      *(("PDU-MIB", "objectName"),
        ("PDU-MIB", "objectInstance"),
        ("PDU-MIB", "userName"),
        ("PDU-MIB", "ipAddress"))
)
if mibBuilder.loadTexts:
    userSessionTimeout.setStatus(
        "current"
    )

userAdded = NotificationType(
    (1, 3, 6, 1, 4, 1, 534, 6, 6, 6, 0, 11)
)
userAdded.setObjects(
      *(("PDU-MIB", "objectName"),
        ("PDU-MIB", "objectInstance"),
        ("PDU-MIB", "userName"),
        ("PDU-MIB", "targetUser"))
)
if mibBuilder.loadTexts:
    userAdded.setStatus(
        "current"
    )

userModified = NotificationType(
    (1, 3, 6, 1, 4, 1, 534, 6, 6, 6, 0, 12)
)
userModified.setObjects(
      *(("PDU-MIB", "objectName"),
        ("PDU-MIB", "objectInstance"),
        ("PDU-MIB", "userName"),
        ("PDU-MIB", "targetUser"))
)
if mibBuilder.loadTexts:
    userModified.setStatus(
        "current"
    )

userDeleted = NotificationType(
    (1, 3, 6, 1, 4, 1, 534, 6, 6, 6, 0, 13)
)
userDeleted.setObjects(
      *(("PDU-MIB", "objectName"),
        ("PDU-MIB", "objectInstance"),
        ("PDU-MIB", "userName"),
        ("PDU-MIB", "targetUser"))
)
if mibBuilder.loadTexts:
    userDeleted.setStatus(
        "current"
    )

groupAdded = NotificationType(
    (1, 3, 6, 1, 4, 1, 534, 6, 6, 6, 0, 14)
)
groupAdded.setObjects(
      *(("PDU-MIB", "objectName"),
        ("PDU-MIB", "objectInstance"),
        ("PDU-MIB", "userName"),
        ("PDU-MIB", "groupName"))
)
if mibBuilder.loadTexts:
    groupAdded.setStatus(
        "current"
    )

groupModified = NotificationType(
    (1, 3, 6, 1, 4, 1, 534, 6, 6, 6, 0, 15)
)
groupModified.setObjects(
      *(("PDU-MIB", "objectName"),
        ("PDU-MIB", "objectInstance"),
        ("PDU-MIB", "userName"),
        ("PDU-MIB", "groupName"))
)
if mibBuilder.loadTexts:
    groupModified.setStatus(
        "current"
    )

groupDeleted = NotificationType(
    (1, 3, 6, 1, 4, 1, 534, 6, 6, 6, 0, 16)
)
groupDeleted.setObjects(
      *(("PDU-MIB", "objectName"),
        ("PDU-MIB", "objectInstance"),
        ("PDU-MIB", "userName"),
        ("PDU-MIB", "groupName"))
)
if mibBuilder.loadTexts:
    groupDeleted.setStatus(
        "current"
    )

deviceUpdateStarted = NotificationType(
    (1, 3, 6, 1, 4, 1, 534, 6, 6, 6, 0, 20)
)
deviceUpdateStarted.setObjects(
      *(("PDU-MIB", "objectName"),
        ("PDU-MIB", "objectInstance"),
        ("PDU-MIB", "userName"),
        ("PDU-MIB", "ipAddress"),
        ("PDU-MIB", "imageVersion"))
)
if mibBuilder.loadTexts:
    deviceUpdateStarted.setStatus(
        "current"
    )

userBlocked = NotificationType(
    (1, 3, 6, 1, 4, 1, 534, 6, 6, 6, 0, 22)
)
userBlocked.setObjects(
      *(("PDU-MIB", "objectName"),
        ("PDU-MIB", "objectInstance"),
        ("PDU-MIB", "userName"),
        ("PDU-MIB", "ipAddress"))
)
if mibBuilder.loadTexts:
    userBlocked.setStatus(
        "current"
    )

powerControl = NotificationType(
    (1, 3, 6, 1, 4, 1, 534, 6, 6, 6, 0, 23)
)
powerControl.setObjects(
      *(("PDU-MIB", "objectName"),
        ("PDU-MIB", "objectInstance"),
        ("PDU-MIB", "userName"),
        ("PDU-MIB", "ipAddress"),
        ("PDU-MIB", "outletLabel"),
        ("PDU-MIB", "outletOperationalState"))
)
if mibBuilder.loadTexts:
    powerControl.setStatus(
        "current"
    )

userPasswordChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 534, 6, 6, 6, 0, 24)
)
userPasswordChanged.setObjects(
      *(("PDU-MIB", "objectName"),
        ("PDU-MIB", "objectInstance"),
        ("PDU-MIB", "userName"),
        ("PDU-MIB", "targetUser"),
        ("PDU-MIB", "ipAddress"))
)
if mibBuilder.loadTexts:
    userPasswordChanged.setStatus(
        "current"
    )

passwordSettingsChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 534, 6, 6, 6, 0, 28)
)
passwordSettingsChanged.setObjects(
      *(("PDU-MIB", "objectName"),
        ("PDU-MIB", "objectInstance"),
        ("PDU-MIB", "userName"),
        ("PDU-MIB", "status"))
)
if mibBuilder.loadTexts:
    passwordSettingsChanged.setStatus(
        "current"
    )

firmwareFileDiscarded = NotificationType(
    (1, 3, 6, 1, 4, 1, 534, 6, 6, 6, 0, 36)
)
firmwareFileDiscarded.setObjects(
      *(("PDU-MIB", "objectName"),
        ("PDU-MIB", "objectInstance"),
        ("PDU-MIB", "userName"))
)
if mibBuilder.loadTexts:
    firmwareFileDiscarded.setStatus(
        "current"
    )

firmwareValidationFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 534, 6, 6, 6, 0, 38)
)
firmwareValidationFailed.setObjects(
      *(("PDU-MIB", "objectName"),
        ("PDU-MIB", "objectInstance"),
        ("PDU-MIB", "userName"))
)
if mibBuilder.loadTexts:
    firmwareValidationFailed.setStatus(
        "current"
    )

securityViolation = NotificationType(
    (1, 3, 6, 1, 4, 1, 534, 6, 6, 6, 0, 39)
)
securityViolation.setObjects(
      *(("PDU-MIB", "objectName"),
        ("PDU-MIB", "objectInstance"),
        ("PDU-MIB", "userName"),
        ("PDU-MIB", "ipAddress"))
)
if mibBuilder.loadTexts:
    securityViolation.setStatus(
        "current"
    )

logFileCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 534, 6, 6, 6, 0, 41)
)
logFileCleared.setObjects(
      *(("PDU-MIB", "objectName"),
        ("PDU-MIB", "objectInstance"),
        ("PDU-MIB", "userName"))
)
if mibBuilder.loadTexts:
    logFileCleared.setStatus(
        "current"
    )

thresholdAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 534, 6, 6, 6, 0, 45)
)
thresholdAlarm.setObjects(
      *(("PDU-MIB", "objectName"),
        ("PDU-MIB", "objectInstance"),
        ("PDU-MIB", "ipAddress"),
        ("PDU-MIB", "sensorDescr"),
        ("PDU-MIB", "thresholdDescr"),
        ("PDU-MIB", "thresholdSeverity"),
        ("PDU-MIB", "thresholdEventType"))
)
if mibBuilder.loadTexts:
    thresholdAlarm.setStatus(
        "current"
    )

outletGroupingConnectivityLost = NotificationType(
    (1, 3, 6, 1, 4, 1, 534, 6, 6, 6, 0, 50)
)
outletGroupingConnectivityLost.setObjects(
      *(("PDU-MIB", "objectName"),
        ("PDU-MIB", "objectInstance"),
        ("PDU-MIB", "ipAddress"),
        ("PDU-MIB", "slaveIpAddress"))
)
if mibBuilder.loadTexts:
    outletGroupingConnectivityLost.setStatus(
        "current"
    )


# Notifications groups

trapsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 534, 6, 6, 6, 9, 2, 9)
)
trapsGroup.setObjects(
      *(("PDU-MIB", "rebootStarted"),
        ("PDU-MIB", "rebootCompleted"),
        ("PDU-MIB", "userLogin"),
        ("PDU-MIB", "userLogout"),
        ("PDU-MIB", "userAuthenticationFailure"),
        ("PDU-MIB", "userSessionTimeout"),
        ("PDU-MIB", "userAdded"),
        ("PDU-MIB", "userModified"),
        ("PDU-MIB", "userDeleted"),
        ("PDU-MIB", "groupAdded"),
        ("PDU-MIB", "groupModified"),
        ("PDU-MIB", "groupDeleted"),
        ("PDU-MIB", "deviceUpdateStarted"),
        ("PDU-MIB", "userBlocked"),
        ("PDU-MIB", "powerControl"),
        ("PDU-MIB", "userPasswordChanged"),
        ("PDU-MIB", "passwordSettingsChanged"),
        ("PDU-MIB", "firmwareFileDiscarded"),
        ("PDU-MIB", "firmwareValidationFailed"),
        ("PDU-MIB", "securityViolation"),
        ("PDU-MIB", "logFileCleared"),
        ("PDU-MIB", "thresholdAlarm"),
        ("PDU-MIB", "outletGroupingConnectivityLost"))
)
if mibBuilder.loadTexts:
    trapsGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 534, 6, 6, 6, 9, 1, 1)
)
compliance.setObjects(
      *(("PDU-MIB", "infoGroup"),
        ("PDU-MIB", "outletsGroup"),
        ("PDU-MIB", "unitSensorsGroup"),
        ("PDU-MIB", "externalTemperatureGroup"),
        ("PDU-MIB", "externalHumidityGroup"),
        ("PDU-MIB", "trapsGroup"))
)
if mibBuilder.loadTexts:
    compliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "PDU-MIB",
    **{"MilliAmps": MilliAmps,
       "MilliVolts": MilliVolts,
       "Watts": Watts,
       "VoltAmps": VoltAmps,
       "DegreesCelsius": DegreesCelsius,
       "Hertz": Hertz,
       "RelativeHumidity": RelativeHumidity,
       "PowerFactorPercentage": PowerFactorPercentage,
       "SensorTypeEnumeration": SensorTypeEnumeration,
       "SensorStateEnumeration": SensorStateEnumeration,
       "eaton": eaton,
       "product": product,
       "pduagent": pduagent,
       "pdu": pdu,
       "traps": traps,
       "rebootStarted": rebootStarted,
       "rebootCompleted": rebootCompleted,
       "userLogin": userLogin,
       "userLogout": userLogout,
       "userAuthenticationFailure": userAuthenticationFailure,
       "userSessionTimeout": userSessionTimeout,
       "userAdded": userAdded,
       "userModified": userModified,
       "userDeleted": userDeleted,
       "groupAdded": groupAdded,
       "groupModified": groupModified,
       "groupDeleted": groupDeleted,
       "deviceUpdateStarted": deviceUpdateStarted,
       "userBlocked": userBlocked,
       "powerControl": powerControl,
       "userPasswordChanged": userPasswordChanged,
       "passwordSettingsChanged": passwordSettingsChanged,
       "firmwareFileDiscarded": firmwareFileDiscarded,
       "firmwareValidationFailed": firmwareValidationFailed,
       "securityViolation": securityViolation,
       "logFileCleared": logFileCleared,
       "thresholdAlarm": thresholdAlarm,
       "outletGroupingConnectivityLost": outletGroupingConnectivityLost,
       "board": board,
       "info": info,
       "firmwareVersion": firmwareVersion,
       "serialNumber": serialNumber,
       "ipAddress": ipAddress,
       "netmask": netmask,
       "gateway": gateway,
       "mac": mac,
       "hardwareRev": hardwareRev,
       "userName": userName,
       "objectName": objectName,
       "objectInstance": objectInstance,
       "targetUser": targetUser,
       "groupName": groupName,
       "imageVersion": imageVersion,
       "sensorDescr": sensorDescr,
       "thresholdDescr": thresholdDescr,
       "thresholdSeverity": thresholdSeverity,
       "thresholdEventType": thresholdEventType,
       "status": status,
       "slaveIpAddress": slaveIpAddress,
       "outlets": outlets,
       "outletCount": outletCount,
       "outletTable": outletTable,
       "outletEntry": outletEntry,
       "outletIndex": outletIndex,
       "outletLabel": outletLabel,
       "outletOperationalState": outletOperationalState,
       "outletCurrent": outletCurrent,
       "outletMaxCurrent": outletMaxCurrent,
       "outletVoltage": outletVoltage,
       "outletActivePower": outletActivePower,
       "outletApparentPower": outletApparentPower,
       "outletPowerFactor": outletPowerFactor,
       "outletCurrentUpperWarning": outletCurrentUpperWarning,
       "outletCurrentUpperCritical": outletCurrentUpperCritical,
       "unit": unit,
       "unitReadings": unitReadings,
       "unitCurrent": unitCurrent,
       "unitVoltage": unitVoltage,
       "unitActivePower": unitActivePower,
       "unitApparentPower": unitApparentPower,
       "unitCpuTemp": unitCpuTemp,
       "unitCircuitBreak0State": unitCircuitBreak0State,
       "unitCircuitBreak1State": unitCircuitBreak1State,
       "unitCircuitBreak2State": unitCircuitBreak2State,
       "unitCircuitBreak0Current": unitCircuitBreak0Current,
       "unitCircuitBreak1Current": unitCircuitBreak1Current,
       "unitCircuitBreak2Current": unitCircuitBreak2Current,
       "unitVoltageLowerWarning": unitVoltageLowerWarning,
       "unitVoltageLowerCritical": unitVoltageLowerCritical,
       "unitVoltageUpperWarning": unitVoltageUpperWarning,
       "unitVoltageUpperCritical": unitVoltageUpperCritical,
       "unitCurrentUpperWarning": unitCurrentUpperWarning,
       "unitCurrentUpperCritical": unitCurrentUpperCritical,
       "unitTempLowerWarning": unitTempLowerWarning,
       "unitTempLowerCritical": unitTempLowerCritical,
       "unitTempUpperWarning": unitTempUpperWarning,
       "unitTempUpperCritical": unitTempUpperCritical,
       "environmental": environmental,
       "tempSensorCount": tempSensorCount,
       "tempSensorTable": tempSensorTable,
       "tempSensorEntry": tempSensorEntry,
       "tempSensorIndex": tempSensorIndex,
       "tempSensorLabel": tempSensorLabel,
       "temperature": temperature,
       "tempLowerWarning": tempLowerWarning,
       "tempUpperWarning": tempUpperWarning,
       "tempLowerCritical": tempLowerCritical,
       "tempUpperCritical": tempUpperCritical,
       "tempLowerWarningReset": tempLowerWarningReset,
       "tempUpperWarningReset": tempUpperWarningReset,
       "tempLowerCriticalReset": tempLowerCriticalReset,
       "tempUpperCriticalReset": tempUpperCriticalReset,
       "humiditySensorCount": humiditySensorCount,
       "humiditySensorTable": humiditySensorTable,
       "humiditySensorEntry": humiditySensorEntry,
       "humiditySensorIndex": humiditySensorIndex,
       "humiditySensorLabel": humiditySensorLabel,
       "humidity": humidity,
       "humidityLowerWarning": humidityLowerWarning,
       "humidityUpperWarning": humidityUpperWarning,
       "humidityLowerCritical": humidityLowerCritical,
       "humidityUpperCritical": humidityUpperCritical,
       "humidityLowerWarningReset": humidityLowerWarningReset,
       "humidityUpperWarningReset": humidityUpperWarningReset,
       "humidityLowerCriticalReset": humidityLowerCriticalReset,
       "humidityUpperCriticalReset": humidityUpperCriticalReset,
       "conformance": conformance,
       "compliances": compliances,
       "compliance": compliance,
       "groups": groups,
       "infoGroup": infoGroup,
       "outletsGroup": outletsGroup,
       "unitSensorsGroup": unitSensorsGroup,
       "externalTemperatureGroup": externalTemperatureGroup,
       "externalHumidityGroup": externalHumidityGroup,
       "trapsGroup": trapsGroup}
)
