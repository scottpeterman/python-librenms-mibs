# SNMP MIB module (MPBC-2RU-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\mpb\MPBC-2RU-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 12:11:07 2025
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
    "TimeTicks",
    "Unsigned32",
    "enterprises",
    "iso")

(DisplayString,
 PhysAddress,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

mpbc2RU = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2)
)
if mibBuilder.loadTexts:
    mpbc2RU.setRevisions(
        ("2009-07-02 11:28",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Mpbc_ObjectIdentity = ObjectIdentity
mpbc = _Mpbc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4464)
)
_MpbcRegs_ObjectIdentity = ObjectIdentity
mpbcRegs = _MpbcRegs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4464, 1)
)
_MpbcProductRegs_ObjectIdentity = ObjectIdentity
mpbcProductRegs = _MpbcProductRegs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4464, 1, 1)
)
_Mpbc2RUProductReg_ObjectIdentity = ObjectIdentity
mpbc2RUProductReg = _Mpbc2RUProductReg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4464, 1, 1, 2)
)
if mibBuilder.loadTexts:
    mpbc2RUProductReg.setStatus("current")
_MpbcProducts_ObjectIdentity = ObjectIdentity
mpbcProducts = _MpbcProducts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4464, 2)
)
_Mpbc2RUTrap_ObjectIdentity = ObjectIdentity
mpbc2RUTrap = _Mpbc2RUTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 0)
)
_Mpbc2RUAlarm_ObjectIdentity = ObjectIdentity
mpbc2RUAlarm = _Mpbc2RUAlarm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 1)
)
_Mpbc2RUAlarmTable_Object = MibTable
mpbc2RUAlarmTable = _Mpbc2RUAlarmTable_Object(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 1, 1)
)
if mibBuilder.loadTexts:
    mpbc2RUAlarmTable.setStatus("current")
_Mpbc2RUAlarmEntry_Object = MibTableRow
mpbc2RUAlarmEntry = _Mpbc2RUAlarmEntry_Object(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 1, 1, 1)
)
mpbc2RUAlarmEntry.setIndexNames(
    (0, "MPBC-2RU-MIB", "mpbc2RUAlarmIndex"),
)
if mibBuilder.loadTexts:
    mpbc2RUAlarmEntry.setStatus("current")
_Mpbc2RUAlarmIndex_Type = Integer32
_Mpbc2RUAlarmIndex_Object = MibTableColumn
mpbc2RUAlarmIndex = _Mpbc2RUAlarmIndex_Object(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 1, 1, 1, 1),
    _Mpbc2RUAlarmIndex_Type()
)
mpbc2RUAlarmIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mpbc2RUAlarmIndex.setStatus("current")
_Mpbc2RUAlarmNEID_Type = OctetString
_Mpbc2RUAlarmNEID_Object = MibTableColumn
mpbc2RUAlarmNEID = _Mpbc2RUAlarmNEID_Object(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 1, 1, 1, 2),
    _Mpbc2RUAlarmNEID_Type()
)
mpbc2RUAlarmNEID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpbc2RUAlarmNEID.setStatus("current")
_Mpbc2RUPosition_Type = Integer32
_Mpbc2RUPosition_Object = MibTableColumn
mpbc2RUPosition = _Mpbc2RUPosition_Object(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 1, 1, 1, 3),
    _Mpbc2RUPosition_Type()
)
mpbc2RUPosition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpbc2RUPosition.setStatus("current")
_Mpbc2RUAlarmModule_Type = OctetString
_Mpbc2RUAlarmModule_Object = MibTableColumn
mpbc2RUAlarmModule = _Mpbc2RUAlarmModule_Object(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 1, 1, 1, 4),
    _Mpbc2RUAlarmModule_Type()
)
mpbc2RUAlarmModule.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpbc2RUAlarmModule.setStatus("current")
_Mpbc2RUAlarmID_Type = Integer32
_Mpbc2RUAlarmID_Object = MibTableColumn
mpbc2RUAlarmID = _Mpbc2RUAlarmID_Object(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 1, 1, 1, 5),
    _Mpbc2RUAlarmID_Type()
)
mpbc2RUAlarmID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpbc2RUAlarmID.setStatus("current")
_Mpbc2RUAlarmDescription_Type = OctetString
_Mpbc2RUAlarmDescription_Object = MibTableColumn
mpbc2RUAlarmDescription = _Mpbc2RUAlarmDescription_Object(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 1, 1, 1, 6),
    _Mpbc2RUAlarmDescription_Type()
)
mpbc2RUAlarmDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpbc2RUAlarmDescription.setStatus("current")
_Mpbc2RUAlarmSeverity_Type = OctetString
_Mpbc2RUAlarmSeverity_Object = MibTableColumn
mpbc2RUAlarmSeverity = _Mpbc2RUAlarmSeverity_Object(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 1, 1, 1, 7),
    _Mpbc2RUAlarmSeverity_Type()
)
mpbc2RUAlarmSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpbc2RUAlarmSeverity.setStatus("current")
_Mpbc2RUAlarmDateAndTime_Type = OctetString
_Mpbc2RUAlarmDateAndTime_Object = MibTableColumn
mpbc2RUAlarmDateAndTime = _Mpbc2RUAlarmDateAndTime_Object(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 1, 1, 1, 8),
    _Mpbc2RUAlarmDateAndTime_Type()
)
mpbc2RUAlarmDateAndTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpbc2RUAlarmDateAndTime.setStatus("current")
_Mpbc2RUAlarmExtraData_Type = OctetString
_Mpbc2RUAlarmExtraData_Object = MibTableColumn
mpbc2RUAlarmExtraData = _Mpbc2RUAlarmExtraData_Object(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 1, 1, 1, 9),
    _Mpbc2RUAlarmExtraData_Type()
)
mpbc2RUAlarmExtraData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpbc2RUAlarmExtraData.setStatus("current")
_Mpbc2RUPxx_ObjectIdentity = ObjectIdentity
mpbc2RUPxx = _Mpbc2RUPxx_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 2)
)
_Mpbc2RUPxxControl_ObjectIdentity = ObjectIdentity
mpbc2RUPxxControl = _Mpbc2RUPxxControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 2, 1)
)


class _Mpbc2RUPxxLaserMode_Type(Integer32):
    """Custom type mpbc2RUPxxLaserMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("laserOff", 0),
          ("laserAPR", 1))
    )


_Mpbc2RUPxxLaserMode_Type.__name__ = "Integer32"
_Mpbc2RUPxxLaserMode_Object = MibScalar
mpbc2RUPxxLaserMode = _Mpbc2RUPxxLaserMode_Object(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 2, 1, 1),
    _Mpbc2RUPxxLaserMode_Type()
)
mpbc2RUPxxLaserMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mpbc2RUPxxLaserMode.setStatus("current")
_Mpbc2RUPxxControlMode_Type = Integer32
_Mpbc2RUPxxControlMode_Object = MibScalar
mpbc2RUPxxControlMode = _Mpbc2RUPxxControlMode_Object(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 2, 1, 2),
    _Mpbc2RUPxxControlMode_Type()
)
mpbc2RUPxxControlMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mpbc2RUPxxControlMode.setStatus("current")
_Mpbc2RUPxxPwrSetPtmW_Type = Integer32
_Mpbc2RUPxxPwrSetPtmW_Object = MibScalar
mpbc2RUPxxPwrSetPtmW = _Mpbc2RUPxxPwrSetPtmW_Object(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 2, 1, 3),
    _Mpbc2RUPxxPwrSetPtmW_Type()
)
mpbc2RUPxxPwrSetPtmW.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mpbc2RUPxxPwrSetPtmW.setStatus("current")
_Mpbc2RUPxxGainSetPtdBx10_Type = Integer32
_Mpbc2RUPxxGainSetPtdBx10_Object = MibScalar
mpbc2RUPxxGainSetPtdBx10 = _Mpbc2RUPxxGainSetPtdBx10_Object(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 2, 1, 4),
    _Mpbc2RUPxxGainSetPtdBx10_Type()
)
mpbc2RUPxxGainSetPtdBx10.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mpbc2RUPxxGainSetPtdBx10.setStatus("current")
_Mpbc2RUPxxVOASettingdBx10_Type = Integer32
_Mpbc2RUPxxVOASettingdBx10_Object = MibScalar
mpbc2RUPxxVOASettingdBx10 = _Mpbc2RUPxxVOASettingdBx10_Object(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 2, 1, 5),
    _Mpbc2RUPxxVOASettingdBx10_Type()
)
mpbc2RUPxxVOASettingdBx10.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mpbc2RUPxxVOASettingdBx10.setStatus("current")
_Mpbc2RUPxxReset_Type = TruthValue
_Mpbc2RUPxxReset_Object = MibScalar
mpbc2RUPxxReset = _Mpbc2RUPxxReset_Object(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 2, 1, 6),
    _Mpbc2RUPxxReset_Type()
)
mpbc2RUPxxReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mpbc2RUPxxReset.setStatus("current")
_Mpbc2RUPxxMonitor_ObjectIdentity = ObjectIdentity
mpbc2RUPxxMonitor = _Mpbc2RUPxxMonitor_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 2, 2)
)
_Mpbc2RUPxxLD1CurmA_Type = Unsigned32
_Mpbc2RUPxxLD1CurmA_Object = MibScalar
mpbc2RUPxxLD1CurmA = _Mpbc2RUPxxLD1CurmA_Object(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 2, 2, 1),
    _Mpbc2RUPxxLD1CurmA_Type()
)
mpbc2RUPxxLD1CurmA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpbc2RUPxxLD1CurmA.setStatus("current")
_Mpbc2RUPxxLD1TempDegCx10_Type = Integer32
_Mpbc2RUPxxLD1TempDegCx10_Object = MibScalar
mpbc2RUPxxLD1TempDegCx10 = _Mpbc2RUPxxLD1TempDegCx10_Object(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 2, 2, 2),
    _Mpbc2RUPxxLD1TempDegCx10_Type()
)
mpbc2RUPxxLD1TempDegCx10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpbc2RUPxxLD1TempDegCx10.setStatus("current")
_Mpbc2RUPxxLD1TECCurmA_Type = Unsigned32
_Mpbc2RUPxxLD1TECCurmA_Object = MibScalar
mpbc2RUPxxLD1TECCurmA = _Mpbc2RUPxxLD1TECCurmA_Object(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 2, 2, 3),
    _Mpbc2RUPxxLD1TECCurmA_Type()
)
mpbc2RUPxxLD1TECCurmA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpbc2RUPxxLD1TECCurmA.setStatus("current")
_Mpbc2RUPxxLD2CurmA_Type = Unsigned32
_Mpbc2RUPxxLD2CurmA_Object = MibScalar
mpbc2RUPxxLD2CurmA = _Mpbc2RUPxxLD2CurmA_Object(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 2, 2, 4),
    _Mpbc2RUPxxLD2CurmA_Type()
)
mpbc2RUPxxLD2CurmA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpbc2RUPxxLD2CurmA.setStatus("current")
_Mpbc2RUPxxLD2TempDegCx10_Type = Integer32
_Mpbc2RUPxxLD2TempDegCx10_Object = MibScalar
mpbc2RUPxxLD2TempDegCx10 = _Mpbc2RUPxxLD2TempDegCx10_Object(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 2, 2, 5),
    _Mpbc2RUPxxLD2TempDegCx10_Type()
)
mpbc2RUPxxLD2TempDegCx10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpbc2RUPxxLD2TempDegCx10.setStatus("current")
_Mpbc2RUPxxLD2TECCurmA_Type = Unsigned32
_Mpbc2RUPxxLD2TECCurmA_Object = MibScalar
mpbc2RUPxxLD2TECCurmA = _Mpbc2RUPxxLD2TECCurmA_Object(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 2, 2, 6),
    _Mpbc2RUPxxLD2TECCurmA_Type()
)
mpbc2RUPxxLD2TECCurmA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpbc2RUPxxLD2TECCurmA.setStatus("current")
_Mpbc2RUPxxCaseTempDegCx10_Type = Integer32
_Mpbc2RUPxxCaseTempDegCx10_Object = MibScalar
mpbc2RUPxxCaseTempDegCx10 = _Mpbc2RUPxxCaseTempDegCx10_Object(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 2, 2, 7),
    _Mpbc2RUPxxCaseTempDegCx10_Type()
)
mpbc2RUPxxCaseTempDegCx10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpbc2RUPxxCaseTempDegCx10.setStatus("current")
_Mpbc2RUPxxOutputPwrmW_Type = Unsigned32
_Mpbc2RUPxxOutputPwrmW_Object = MibScalar
mpbc2RUPxxOutputPwrmW = _Mpbc2RUPxxOutputPwrmW_Object(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 2, 2, 8),
    _Mpbc2RUPxxOutputPwrmW_Type()
)
mpbc2RUPxxOutputPwrmW.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpbc2RUPxxOutputPwrmW.setStatus("current")
_Mpbc2RUPxxGaindBx10_Type = Integer32
_Mpbc2RUPxxGaindBx10_Object = MibScalar
mpbc2RUPxxGaindBx10 = _Mpbc2RUPxxGaindBx10_Object(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 2, 2, 9),
    _Mpbc2RUPxxGaindBx10_Type()
)
mpbc2RUPxxGaindBx10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpbc2RUPxxGaindBx10.setStatus("current")
_Mpbc2RUPxxInputPwrmWx100_Type = Unsigned32
_Mpbc2RUPxxInputPwrmWx100_Object = MibScalar
mpbc2RUPxxInputPwrmWx100 = _Mpbc2RUPxxInputPwrmWx100_Object(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 2, 2, 10),
    _Mpbc2RUPxxInputPwrmWx100_Type()
)
mpbc2RUPxxInputPwrmWx100.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpbc2RUPxxInputPwrmWx100.setStatus("current")
_Mpbc2RUPxxBackReflPwrmWx100_Type = Unsigned32
_Mpbc2RUPxxBackReflPwrmWx100_Object = MibScalar
mpbc2RUPxxBackReflPwrmWx100 = _Mpbc2RUPxxBackReflPwrmWx100_Object(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 2, 2, 11),
    _Mpbc2RUPxxBackReflPwrmWx100_Type()
)
mpbc2RUPxxBackReflPwrmWx100.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpbc2RUPxxBackReflPwrmWx100.setStatus("current")


class _Mpbc2RUPxxMonLaserState_Type(Integer32):
    """Custom type mpbc2RUPxxMonLaserState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              10)
        )
    )
    namedValues = NamedValues(
        *(("laserOff", 0),
          ("laserNormal", 1),
          ("laserALS", 2),
          ("laserALS100", 3),
          ("laserOn", 10))
    )


_Mpbc2RUPxxMonLaserState_Type.__name__ = "Integer32"
_Mpbc2RUPxxMonLaserState_Object = MibScalar
mpbc2RUPxxMonLaserState = _Mpbc2RUPxxMonLaserState_Object(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 2, 2, 12),
    _Mpbc2RUPxxMonLaserState_Type()
)
mpbc2RUPxxMonLaserState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpbc2RUPxxMonLaserState.setStatus("current")


class _Mpbc2RUPxxMonLaserMode_Type(Integer32):
    """Custom type mpbc2RUPxxMonLaserMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              10)
        )
    )
    namedValues = NamedValues(
        *(("laserOff", 0),
          ("laserAPR", 1),
          ("laserOn", 10))
    )


_Mpbc2RUPxxMonLaserMode_Type.__name__ = "Integer32"
_Mpbc2RUPxxMonLaserMode_Object = MibScalar
mpbc2RUPxxMonLaserMode = _Mpbc2RUPxxMonLaserMode_Object(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 2, 2, 13),
    _Mpbc2RUPxxMonLaserMode_Type()
)
mpbc2RUPxxMonLaserMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpbc2RUPxxMonLaserMode.setStatus("current")
_Mpbc2RUPxxMonControlMode_Type = Integer32
_Mpbc2RUPxxMonControlMode_Object = MibScalar
mpbc2RUPxxMonControlMode = _Mpbc2RUPxxMonControlMode_Object(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 2, 2, 14),
    _Mpbc2RUPxxMonControlMode_Type()
)
mpbc2RUPxxMonControlMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpbc2RUPxxMonControlMode.setStatus("current")
_Mpbc2RUPxxDisableInputState_Type = Unsigned32
_Mpbc2RUPxxDisableInputState_Object = MibScalar
mpbc2RUPxxDisableInputState = _Mpbc2RUPxxDisableInputState_Object(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 2, 2, 15),
    _Mpbc2RUPxxDisableInputState_Type()
)
mpbc2RUPxxDisableInputState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpbc2RUPxxDisableInputState.setStatus("current")


class _Mpbc2RUPxxUnitState_Type(Integer32):
    """Custom type mpbc2RUPxxUnitState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("stateInit", 0),
          ("stateNormal", 1),
          ("stateFault", 2))
    )


_Mpbc2RUPxxUnitState_Type.__name__ = "Integer32"
_Mpbc2RUPxxUnitState_Object = MibScalar
mpbc2RUPxxUnitState = _Mpbc2RUPxxUnitState_Object(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 2, 2, 16),
    _Mpbc2RUPxxUnitState_Type()
)
mpbc2RUPxxUnitState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpbc2RUPxxUnitState.setStatus("current")


class _Mpbc2RUPxxOSCRxTone_Type(Integer32):
    """Custom type mpbc2RUPxxOSCRxTone based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("noTone", 0),
          ("tone1", 1),
          ("tone2", 2),
          ("tone1plus2", 3))
    )


_Mpbc2RUPxxOSCRxTone_Type.__name__ = "Integer32"
_Mpbc2RUPxxOSCRxTone_Object = MibScalar
mpbc2RUPxxOSCRxTone = _Mpbc2RUPxxOSCRxTone_Object(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 2, 2, 17),
    _Mpbc2RUPxxOSCRxTone_Type()
)
mpbc2RUPxxOSCRxTone.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpbc2RUPxxOSCRxTone.setStatus("current")
_Mpbc2RUPxxOSCTempdegCx10_Type = Integer32
_Mpbc2RUPxxOSCTempdegCx10_Object = MibScalar
mpbc2RUPxxOSCTempdegCx10 = _Mpbc2RUPxxOSCTempdegCx10_Object(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 2, 2, 18),
    _Mpbc2RUPxxOSCTempdegCx10_Type()
)
mpbc2RUPxxOSCTempdegCx10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpbc2RUPxxOSCTempdegCx10.setStatus("current")


class _Mpbc2RUPxxOSCTxTone_Type(Integer32):
    """Custom type mpbc2RUPxxOSCTxTone based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("tone1", 1),
          ("tone2", 2))
    )


_Mpbc2RUPxxOSCTxTone_Type.__name__ = "Integer32"
_Mpbc2RUPxxOSCTxTone_Object = MibScalar
mpbc2RUPxxOSCTxTone = _Mpbc2RUPxxOSCTxTone_Object(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 2, 2, 19),
    _Mpbc2RUPxxOSCTxTone_Type()
)
mpbc2RUPxxOSCTxTone.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpbc2RUPxxOSCTxTone.setStatus("current")
_Mpbc2RUPxxOSCTxPwrmWx100_Type = Integer32
_Mpbc2RUPxxOSCTxPwrmWx100_Object = MibScalar
mpbc2RUPxxOSCTxPwrmWx100 = _Mpbc2RUPxxOSCTxPwrmWx100_Object(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 2, 2, 20),
    _Mpbc2RUPxxOSCTxPwrmWx100_Type()
)
mpbc2RUPxxOSCTxPwrmWx100.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpbc2RUPxxOSCTxPwrmWx100.setStatus("current")


class _Mpbc2RUPxxOSCRx1610Tone_Type(Integer32):
    """Custom type mpbc2RUPxxOSCRx1610Tone based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("tone1", 1),
          ("tone2", 2))
    )


_Mpbc2RUPxxOSCRx1610Tone_Type.__name__ = "Integer32"
_Mpbc2RUPxxOSCRx1610Tone_Object = MibScalar
mpbc2RUPxxOSCRx1610Tone = _Mpbc2RUPxxOSCRx1610Tone_Object(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 2, 2, 21),
    _Mpbc2RUPxxOSCRx1610Tone_Type()
)
mpbc2RUPxxOSCRx1610Tone.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpbc2RUPxxOSCRx1610Tone.setStatus("current")
_Mpbc2RUPxxMonVOASettingdBx10_Type = Integer32
_Mpbc2RUPxxMonVOASettingdBx10_Object = MibScalar
mpbc2RUPxxMonVOASettingdBx10 = _Mpbc2RUPxxMonVOASettingdBx10_Object(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 2, 2, 22),
    _Mpbc2RUPxxMonVOASettingdBx10_Type()
)
mpbc2RUPxxMonVOASettingdBx10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpbc2RUPxxMonVOASettingdBx10.setStatus("current")
_Mpbc2RUPxxConfiguration_ObjectIdentity = ObjectIdentity
mpbc2RUPxxConfiguration = _Mpbc2RUPxxConfiguration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 2, 3)
)
_Mpbc2RUPxxLD1CurMinThrmA_Type = Unsigned32
_Mpbc2RUPxxLD1CurMinThrmA_Object = MibScalar
mpbc2RUPxxLD1CurMinThrmA = _Mpbc2RUPxxLD1CurMinThrmA_Object(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 2, 3, 1),
    _Mpbc2RUPxxLD1CurMinThrmA_Type()
)
mpbc2RUPxxLD1CurMinThrmA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpbc2RUPxxLD1CurMinThrmA.setStatus("current")
_Mpbc2RUPxxLD2CurMinThrmA_Type = Unsigned32
_Mpbc2RUPxxLD2CurMinThrmA_Object = MibScalar
mpbc2RUPxxLD2CurMinThrmA = _Mpbc2RUPxxLD2CurMinThrmA_Object(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 2, 3, 2),
    _Mpbc2RUPxxLD2CurMinThrmA_Type()
)
mpbc2RUPxxLD2CurMinThrmA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpbc2RUPxxLD2CurMinThrmA.setStatus("current")
_Mpbc2RUPxxLD1CurMaxThrmA_Type = Unsigned32
_Mpbc2RUPxxLD1CurMaxThrmA_Object = MibScalar
mpbc2RUPxxLD1CurMaxThrmA = _Mpbc2RUPxxLD1CurMaxThrmA_Object(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 2, 3, 3),
    _Mpbc2RUPxxLD1CurMaxThrmA_Type()
)
mpbc2RUPxxLD1CurMaxThrmA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpbc2RUPxxLD1CurMaxThrmA.setStatus("current")
_Mpbc2RUPxxLD2CurMaxThrmA_Type = Unsigned32
_Mpbc2RUPxxLD2CurMaxThrmA_Object = MibScalar
mpbc2RUPxxLD2CurMaxThrmA = _Mpbc2RUPxxLD2CurMaxThrmA_Object(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 2, 3, 4),
    _Mpbc2RUPxxLD2CurMaxThrmA_Type()
)
mpbc2RUPxxLD2CurMaxThrmA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpbc2RUPxxLD2CurMaxThrmA.setStatus("current")
_Mpbc2RUPxxCaseTempMinSetThrDegCx10_Type = Integer32
_Mpbc2RUPxxCaseTempMinSetThrDegCx10_Object = MibScalar
mpbc2RUPxxCaseTempMinSetThrDegCx10 = _Mpbc2RUPxxCaseTempMinSetThrDegCx10_Object(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 2, 3, 5),
    _Mpbc2RUPxxCaseTempMinSetThrDegCx10_Type()
)
mpbc2RUPxxCaseTempMinSetThrDegCx10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpbc2RUPxxCaseTempMinSetThrDegCx10.setStatus("current")
_Mpbc2RUPxxCaseTempMinClearThrDegCx10_Type = Integer32
_Mpbc2RUPxxCaseTempMinClearThrDegCx10_Object = MibScalar
mpbc2RUPxxCaseTempMinClearThrDegCx10 = _Mpbc2RUPxxCaseTempMinClearThrDegCx10_Object(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 2, 3, 6),
    _Mpbc2RUPxxCaseTempMinClearThrDegCx10_Type()
)
mpbc2RUPxxCaseTempMinClearThrDegCx10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpbc2RUPxxCaseTempMinClearThrDegCx10.setStatus("current")
_Mpbc2RUPxxCaseTempMaxSetThrDegCx10_Type = Integer32
_Mpbc2RUPxxCaseTempMaxSetThrDegCx10_Object = MibScalar
mpbc2RUPxxCaseTempMaxSetThrDegCx10 = _Mpbc2RUPxxCaseTempMaxSetThrDegCx10_Object(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 2, 3, 7),
    _Mpbc2RUPxxCaseTempMaxSetThrDegCx10_Type()
)
mpbc2RUPxxCaseTempMaxSetThrDegCx10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpbc2RUPxxCaseTempMaxSetThrDegCx10.setStatus("current")
_Mpbc2RUPxxCaseTempMaxClearThrDegCx10_Type = Integer32
_Mpbc2RUPxxCaseTempMaxClearThrDegCx10_Object = MibScalar
mpbc2RUPxxCaseTempMaxClearThrDegCx10 = _Mpbc2RUPxxCaseTempMaxClearThrDegCx10_Object(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 2, 3, 8),
    _Mpbc2RUPxxCaseTempMaxClearThrDegCx10_Type()
)
mpbc2RUPxxCaseTempMaxClearThrDegCx10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpbc2RUPxxCaseTempMaxClearThrDegCx10.setStatus("current")
_Mpbc2RUPxxCaseTempMinAlrmThrDegCx10_Type = Integer32
_Mpbc2RUPxxCaseTempMinAlrmThrDegCx10_Object = MibScalar
mpbc2RUPxxCaseTempMinAlrmThrDegCx10 = _Mpbc2RUPxxCaseTempMinAlrmThrDegCx10_Object(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 2, 3, 9),
    _Mpbc2RUPxxCaseTempMinAlrmThrDegCx10_Type()
)
mpbc2RUPxxCaseTempMinAlrmThrDegCx10.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mpbc2RUPxxCaseTempMinAlrmThrDegCx10.setStatus("current")
_Mpbc2RUPxxCaseTempMaxAlrmThrDegCx10_Type = Integer32
_Mpbc2RUPxxCaseTempMaxAlrmThrDegCx10_Object = MibScalar
mpbc2RUPxxCaseTempMaxAlrmThrDegCx10 = _Mpbc2RUPxxCaseTempMaxAlrmThrDegCx10_Object(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 2, 3, 10),
    _Mpbc2RUPxxCaseTempMaxAlrmThrDegCx10_Type()
)
mpbc2RUPxxCaseTempMaxAlrmThrDegCx10.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mpbc2RUPxxCaseTempMaxAlrmThrDegCx10.setStatus("current")
_Mpbc2RUPxxLOSSetThrdBmx100_Type = Integer32
_Mpbc2RUPxxLOSSetThrdBmx100_Object = MibScalar
mpbc2RUPxxLOSSetThrdBmx100 = _Mpbc2RUPxxLOSSetThrdBmx100_Object(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 2, 3, 11),
    _Mpbc2RUPxxLOSSetThrdBmx100_Type()
)
mpbc2RUPxxLOSSetThrdBmx100.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpbc2RUPxxLOSSetThrdBmx100.setStatus("current")
_Mpbc2RUPxxLOSClearThrdBmx100_Type = Integer32
_Mpbc2RUPxxLOSClearThrdBmx100_Object = MibScalar
mpbc2RUPxxLOSClearThrdBmx100 = _Mpbc2RUPxxLOSClearThrdBmx100_Object(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 2, 3, 12),
    _Mpbc2RUPxxLOSClearThrdBmx100_Type()
)
mpbc2RUPxxLOSClearThrdBmx100.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpbc2RUPxxLOSClearThrdBmx100.setStatus("current")
_Mpbc2RUPxxInputMinThrdBmx100_Type = Integer32
_Mpbc2RUPxxInputMinThrdBmx100_Object = MibScalar
mpbc2RUPxxInputMinThrdBmx100 = _Mpbc2RUPxxInputMinThrdBmx100_Object(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 2, 3, 13),
    _Mpbc2RUPxxInputMinThrdBmx100_Type()
)
mpbc2RUPxxInputMinThrdBmx100.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mpbc2RUPxxInputMinThrdBmx100.setStatus("current")
_Mpbc2RUPxxInputMaxThrdBmx100_Type = Integer32
_Mpbc2RUPxxInputMaxThrdBmx100_Object = MibScalar
mpbc2RUPxxInputMaxThrdBmx100 = _Mpbc2RUPxxInputMaxThrdBmx100_Object(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 2, 3, 14),
    _Mpbc2RUPxxInputMaxThrdBmx100_Type()
)
mpbc2RUPxxInputMaxThrdBmx100.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mpbc2RUPxxInputMaxThrdBmx100.setStatus("current")
_Mpbc2RUPxxOutputMinThrdBx10_Type = Integer32
_Mpbc2RUPxxOutputMinThrdBx10_Object = MibScalar
mpbc2RUPxxOutputMinThrdBx10 = _Mpbc2RUPxxOutputMinThrdBx10_Object(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 2, 3, 15),
    _Mpbc2RUPxxOutputMinThrdBx10_Type()
)
mpbc2RUPxxOutputMinThrdBx10.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mpbc2RUPxxOutputMinThrdBx10.setStatus("current")
_Mpbc2RUPxxOutputMaxThrdBx10_Type = Integer32
_Mpbc2RUPxxOutputMaxThrdBx10_Object = MibScalar
mpbc2RUPxxOutputMaxThrdBx10 = _Mpbc2RUPxxOutputMaxThrdBx10_Object(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 2, 3, 16),
    _Mpbc2RUPxxOutputMaxThrdBx10_Type()
)
mpbc2RUPxxOutputMaxThrdBx10.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mpbc2RUPxxOutputMaxThrdBx10.setStatus("current")
_Mpbc2RUPxxOSCMode_Type = Unsigned32
_Mpbc2RUPxxOSCMode_Object = MibScalar
mpbc2RUPxxOSCMode = _Mpbc2RUPxxOSCMode_Object(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 2, 3, 17),
    _Mpbc2RUPxxOSCMode_Type()
)
mpbc2RUPxxOSCMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mpbc2RUPxxOSCMode.setStatus("current")
_Mpbc2RUPxxOutputSetptminLimdBmx10_Type = Integer32
_Mpbc2RUPxxOutputSetptminLimdBmx10_Object = MibScalar
mpbc2RUPxxOutputSetptminLimdBmx10 = _Mpbc2RUPxxOutputSetptminLimdBmx10_Object(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 2, 3, 18),
    _Mpbc2RUPxxOutputSetptminLimdBmx10_Type()
)
mpbc2RUPxxOutputSetptminLimdBmx10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpbc2RUPxxOutputSetptminLimdBmx10.setStatus("current")
_Mpbc2RUPxxOutputSetptmaxLimdBmx10_Type = Integer32
_Mpbc2RUPxxOutputSetptmaxLimdBmx10_Object = MibScalar
mpbc2RUPxxOutputSetptmaxLimdBmx10 = _Mpbc2RUPxxOutputSetptmaxLimdBmx10_Object(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 2, 3, 19),
    _Mpbc2RUPxxOutputSetptmaxLimdBmx10_Type()
)
mpbc2RUPxxOutputSetptmaxLimdBmx10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpbc2RUPxxOutputSetptmaxLimdBmx10.setStatus("current")
_Mpbc2RUPxxGainSetptminLimdBx10_Type = Integer32
_Mpbc2RUPxxGainSetptminLimdBx10_Object = MibScalar
mpbc2RUPxxGainSetptminLimdBx10 = _Mpbc2RUPxxGainSetptminLimdBx10_Object(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 2, 3, 20),
    _Mpbc2RUPxxGainSetptminLimdBx10_Type()
)
mpbc2RUPxxGainSetptminLimdBx10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpbc2RUPxxGainSetptminLimdBx10.setStatus("current")
_Mpbc2RUPxxGainSetptmaxLimdBx10_Type = Integer32
_Mpbc2RUPxxGainSetptmaxLimdBx10_Object = MibScalar
mpbc2RUPxxGainSetptmaxLimdBx10 = _Mpbc2RUPxxGainSetptmaxLimdBx10_Object(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 2, 3, 21),
    _Mpbc2RUPxxGainSetptmaxLimdBx10_Type()
)
mpbc2RUPxxGainSetptmaxLimdBx10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpbc2RUPxxGainSetptmaxLimdBx10.setStatus("current")
_Mpbc2RURFL1_ObjectIdentity = ObjectIdentity
mpbc2RURFL1 = _Mpbc2RURFL1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 3)
)
_Mpbc2RURFL1Control_ObjectIdentity = ObjectIdentity
mpbc2RURFL1Control = _Mpbc2RURFL1Control_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 3, 1)
)


class _Mpbc2RURFL1LaserMode_Type(Integer32):
    """Custom type mpbc2RURFL1LaserMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("laserOff", 0),
          ("laserAPR", 1))
    )


_Mpbc2RURFL1LaserMode_Type.__name__ = "Integer32"
_Mpbc2RURFL1LaserMode_Object = MibScalar
mpbc2RURFL1LaserMode = _Mpbc2RURFL1LaserMode_Object(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 3, 1, 1),
    _Mpbc2RURFL1LaserMode_Type()
)
mpbc2RURFL1LaserMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mpbc2RURFL1LaserMode.setStatus("current")
_Mpbc2RURFL1ControlMode_Type = Integer32
_Mpbc2RURFL1ControlMode_Object = MibScalar
mpbc2RURFL1ControlMode = _Mpbc2RURFL1ControlMode_Object(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 3, 1, 2),
    _Mpbc2RURFL1ControlMode_Type()
)
mpbc2RURFL1ControlMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mpbc2RURFL1ControlMode.setStatus("current")
_Mpbc2RURFL1PwrSetPtmW_Type = Unsigned32
_Mpbc2RURFL1PwrSetPtmW_Object = MibScalar
mpbc2RURFL1PwrSetPtmW = _Mpbc2RURFL1PwrSetPtmW_Object(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 3, 1, 3),
    _Mpbc2RURFL1PwrSetPtmW_Type()
)
mpbc2RURFL1PwrSetPtmW.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mpbc2RURFL1PwrSetPtmW.setStatus("current")
_Mpbc2RURFL1Reset_Type = TruthValue
_Mpbc2RURFL1Reset_Object = MibScalar
mpbc2RURFL1Reset = _Mpbc2RURFL1Reset_Object(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 3, 1, 4),
    _Mpbc2RURFL1Reset_Type()
)
mpbc2RURFL1Reset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mpbc2RURFL1Reset.setStatus("current")
_Mpbc2RURFL1Monitor_ObjectIdentity = ObjectIdentity
mpbc2RURFL1Monitor = _Mpbc2RURFL1Monitor_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 3, 2)
)
_Mpbc2RURFL1LD1Current_Type = Unsigned32
_Mpbc2RURFL1LD1Current_Object = MibScalar
mpbc2RURFL1LD1Current = _Mpbc2RURFL1LD1Current_Object(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 3, 2, 1),
    _Mpbc2RURFL1LD1Current_Type()
)
mpbc2RURFL1LD1Current.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpbc2RURFL1LD1Current.setStatus("current")
_Mpbc2RURFL1LD2Current_Type = Unsigned32
_Mpbc2RURFL1LD2Current_Object = MibScalar
mpbc2RURFL1LD2Current = _Mpbc2RURFL1LD2Current_Object(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 3, 2, 2),
    _Mpbc2RURFL1LD2Current_Type()
)
mpbc2RURFL1LD2Current.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpbc2RURFL1LD2Current.setStatus("current")
_Mpbc2RURFL1CaseTempDegCx10_Type = Integer32
_Mpbc2RURFL1CaseTempDegCx10_Object = MibScalar
mpbc2RURFL1CaseTempDegCx10 = _Mpbc2RURFL1CaseTempDegCx10_Object(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 3, 2, 3),
    _Mpbc2RURFL1CaseTempDegCx10_Type()
)
mpbc2RURFL1CaseTempDegCx10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpbc2RURFL1CaseTempDegCx10.setStatus("current")
_Mpbc2RURFL1OutputPwrmW_Type = Unsigned32
_Mpbc2RURFL1OutputPwrmW_Object = MibScalar
mpbc2RURFL1OutputPwrmW = _Mpbc2RURFL1OutputPwrmW_Object(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 3, 2, 4),
    _Mpbc2RURFL1OutputPwrmW_Type()
)
mpbc2RURFL1OutputPwrmW.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpbc2RURFL1OutputPwrmW.setStatus("current")


class _Mpbc2RURFL1MonLaserState_Type(Integer32):
    """Custom type mpbc2RURFL1MonLaserState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              10)
        )
    )
    namedValues = NamedValues(
        *(("laserOff", 0),
          ("laserNormal", 1),
          ("laserALS", 2),
          ("laserALS100", 3),
          ("laserOn", 10))
    )


_Mpbc2RURFL1MonLaserState_Type.__name__ = "Integer32"
_Mpbc2RURFL1MonLaserState_Object = MibScalar
mpbc2RURFL1MonLaserState = _Mpbc2RURFL1MonLaserState_Object(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 3, 2, 5),
    _Mpbc2RURFL1MonLaserState_Type()
)
mpbc2RURFL1MonLaserState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpbc2RURFL1MonLaserState.setStatus("current")


class _Mpbc2RURFL1MonLaserMode_Type(Integer32):
    """Custom type mpbc2RURFL1MonLaserMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              10)
        )
    )
    namedValues = NamedValues(
        *(("laserOff", 0),
          ("laserAPR", 1),
          ("laserOn", 10))
    )


_Mpbc2RURFL1MonLaserMode_Type.__name__ = "Integer32"
_Mpbc2RURFL1MonLaserMode_Object = MibScalar
mpbc2RURFL1MonLaserMode = _Mpbc2RURFL1MonLaserMode_Object(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 3, 2, 6),
    _Mpbc2RURFL1MonLaserMode_Type()
)
mpbc2RURFL1MonLaserMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpbc2RURFL1MonLaserMode.setStatus("current")
_Mpbc2RURFL1MonControlMode_Type = Integer32
_Mpbc2RURFL1MonControlMode_Object = MibScalar
mpbc2RURFL1MonControlMode = _Mpbc2RURFL1MonControlMode_Object(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 3, 2, 7),
    _Mpbc2RURFL1MonControlMode_Type()
)
mpbc2RURFL1MonControlMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpbc2RURFL1MonControlMode.setStatus("current")
_Mpbc2RURFL1DisableInputState_Type = Integer32
_Mpbc2RURFL1DisableInputState_Object = MibScalar
mpbc2RURFL1DisableInputState = _Mpbc2RURFL1DisableInputState_Object(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 3, 2, 8),
    _Mpbc2RURFL1DisableInputState_Type()
)
mpbc2RURFL1DisableInputState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpbc2RURFL1DisableInputState.setStatus("current")


class _Mpbc2RURFL1UnitState_Type(Integer32):
    """Custom type mpbc2RURFL1UnitState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("stateInit", 0),
          ("stateNormal", 1),
          ("stateFault", 2))
    )


_Mpbc2RURFL1UnitState_Type.__name__ = "Integer32"
_Mpbc2RURFL1UnitState_Object = MibScalar
mpbc2RURFL1UnitState = _Mpbc2RURFL1UnitState_Object(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 3, 2, 9),
    _Mpbc2RURFL1UnitState_Type()
)
mpbc2RURFL1UnitState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpbc2RURFL1UnitState.setStatus("current")


class _Mpbc2RURFL1OSCRxTone_Type(Integer32):
    """Custom type mpbc2RURFL1OSCRxTone based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("noTone", 0),
          ("tone1", 1),
          ("tone2", 2),
          ("tone1plus2", 3))
    )


_Mpbc2RURFL1OSCRxTone_Type.__name__ = "Integer32"
_Mpbc2RURFL1OSCRxTone_Object = MibScalar
mpbc2RURFL1OSCRxTone = _Mpbc2RURFL1OSCRxTone_Object(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 3, 2, 10),
    _Mpbc2RURFL1OSCRxTone_Type()
)
mpbc2RURFL1OSCRxTone.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpbc2RURFL1OSCRxTone.setStatus("current")
_Mpbc2RURFL1OSCTempDegCx10_Type = Integer32
_Mpbc2RURFL1OSCTempDegCx10_Object = MibScalar
mpbc2RURFL1OSCTempDegCx10 = _Mpbc2RURFL1OSCTempDegCx10_Object(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 3, 2, 11),
    _Mpbc2RURFL1OSCTempDegCx10_Type()
)
mpbc2RURFL1OSCTempDegCx10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpbc2RURFL1OSCTempDegCx10.setStatus("current")


class _Mpbc2RURFL1OSCTxTone_Type(Integer32):
    """Custom type mpbc2RURFL1OSCTxTone based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("tone1", 1),
          ("tone2", 2))
    )


_Mpbc2RURFL1OSCTxTone_Type.__name__ = "Integer32"
_Mpbc2RURFL1OSCTxTone_Object = MibScalar
mpbc2RURFL1OSCTxTone = _Mpbc2RURFL1OSCTxTone_Object(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 3, 2, 12),
    _Mpbc2RURFL1OSCTxTone_Type()
)
mpbc2RURFL1OSCTxTone.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpbc2RURFL1OSCTxTone.setStatus("current")
_Mpbc2RURFL1OSCTxPwrmWx100_Type = Integer32
_Mpbc2RURFL1OSCTxPwrmWx100_Object = MibScalar
mpbc2RURFL1OSCTxPwrmWx100 = _Mpbc2RURFL1OSCTxPwrmWx100_Object(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 3, 2, 13),
    _Mpbc2RURFL1OSCTxPwrmWx100_Type()
)
mpbc2RURFL1OSCTxPwrmWx100.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpbc2RURFL1OSCTxPwrmWx100.setStatus("current")
_Mpbc2RURFL1Configuration_ObjectIdentity = ObjectIdentity
mpbc2RURFL1Configuration = _Mpbc2RURFL1Configuration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 3, 3)
)
_Mpbc2RURFL1PwrThrLowdBx10_Type = Integer32
_Mpbc2RURFL1PwrThrLowdBx10_Object = MibScalar
mpbc2RURFL1PwrThrLowdBx10 = _Mpbc2RURFL1PwrThrLowdBx10_Object(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 3, 3, 1),
    _Mpbc2RURFL1PwrThrLowdBx10_Type()
)
mpbc2RURFL1PwrThrLowdBx10.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mpbc2RURFL1PwrThrLowdBx10.setStatus("current")
_Mpbc2RURFL1PwrThrHidBx10_Type = Unsigned32
_Mpbc2RURFL1PwrThrHidBx10_Object = MibScalar
mpbc2RURFL1PwrThrHidBx10 = _Mpbc2RURFL1PwrThrHidBx10_Object(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 3, 3, 2),
    _Mpbc2RURFL1PwrThrHidBx10_Type()
)
mpbc2RURFL1PwrThrHidBx10.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mpbc2RURFL1PwrThrHidBx10.setStatus("current")
_Mpbc2RURFL1CaseTempMinAlrmThDegCx10_Type = Integer32
_Mpbc2RURFL1CaseTempMinAlrmThDegCx10_Object = MibScalar
mpbc2RURFL1CaseTempMinAlrmThDegCx10 = _Mpbc2RURFL1CaseTempMinAlrmThDegCx10_Object(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 3, 3, 3),
    _Mpbc2RURFL1CaseTempMinAlrmThDegCx10_Type()
)
mpbc2RURFL1CaseTempMinAlrmThDegCx10.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mpbc2RURFL1CaseTempMinAlrmThDegCx10.setStatus("current")
_Mpbc2RURFL1CaseTempMaxAlrmThDegCx10_Type = Integer32
_Mpbc2RURFL1CaseTempMaxAlrmThDegCx10_Object = MibScalar
mpbc2RURFL1CaseTempMaxAlrmThDegCx10 = _Mpbc2RURFL1CaseTempMaxAlrmThDegCx10_Object(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 3, 3, 4),
    _Mpbc2RURFL1CaseTempMaxAlrmThDegCx10_Type()
)
mpbc2RURFL1CaseTempMaxAlrmThDegCx10.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mpbc2RURFL1CaseTempMaxAlrmThDegCx10.setStatus("current")
_Mpbc2RURFL1LD1CurMinThrmA_Type = Unsigned32
_Mpbc2RURFL1LD1CurMinThrmA_Object = MibScalar
mpbc2RURFL1LD1CurMinThrmA = _Mpbc2RURFL1LD1CurMinThrmA_Object(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 3, 3, 5),
    _Mpbc2RURFL1LD1CurMinThrmA_Type()
)
mpbc2RURFL1LD1CurMinThrmA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpbc2RURFL1LD1CurMinThrmA.setStatus("current")
_Mpbc2RURFL1LD1CurMaxThrmA_Type = Unsigned32
_Mpbc2RURFL1LD1CurMaxThrmA_Object = MibScalar
mpbc2RURFL1LD1CurMaxThrmA = _Mpbc2RURFL1LD1CurMaxThrmA_Object(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 3, 3, 6),
    _Mpbc2RURFL1LD1CurMaxThrmA_Type()
)
mpbc2RURFL1LD1CurMaxThrmA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpbc2RURFL1LD1CurMaxThrmA.setStatus("current")
_Mpbc2RURFL1LD2CurMinThrmA_Type = Unsigned32
_Mpbc2RURFL1LD2CurMinThrmA_Object = MibScalar
mpbc2RURFL1LD2CurMinThrmA = _Mpbc2RURFL1LD2CurMinThrmA_Object(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 3, 3, 7),
    _Mpbc2RURFL1LD2CurMinThrmA_Type()
)
mpbc2RURFL1LD2CurMinThrmA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpbc2RURFL1LD2CurMinThrmA.setStatus("current")
_Mpbc2RURFL1LD2CurMaxThrmA_Type = Unsigned32
_Mpbc2RURFL1LD2CurMaxThrmA_Object = MibScalar
mpbc2RURFL1LD2CurMaxThrmA = _Mpbc2RURFL1LD2CurMaxThrmA_Object(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 3, 3, 8),
    _Mpbc2RURFL1LD2CurMaxThrmA_Type()
)
mpbc2RURFL1LD2CurMaxThrmA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpbc2RURFL1LD2CurMaxThrmA.setStatus("current")
_Mpbc2RURFL1CaseTempMinSetThrDegCx10_Type = Integer32
_Mpbc2RURFL1CaseTempMinSetThrDegCx10_Object = MibScalar
mpbc2RURFL1CaseTempMinSetThrDegCx10 = _Mpbc2RURFL1CaseTempMinSetThrDegCx10_Object(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 3, 3, 9),
    _Mpbc2RURFL1CaseTempMinSetThrDegCx10_Type()
)
mpbc2RURFL1CaseTempMinSetThrDegCx10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpbc2RURFL1CaseTempMinSetThrDegCx10.setStatus("current")
_Mpbc2RURFL1CaseTempMinClearThrDegCx10_Type = Integer32
_Mpbc2RURFL1CaseTempMinClearThrDegCx10_Object = MibScalar
mpbc2RURFL1CaseTempMinClearThrDegCx10 = _Mpbc2RURFL1CaseTempMinClearThrDegCx10_Object(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 3, 3, 10),
    _Mpbc2RURFL1CaseTempMinClearThrDegCx10_Type()
)
mpbc2RURFL1CaseTempMinClearThrDegCx10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpbc2RURFL1CaseTempMinClearThrDegCx10.setStatus("current")
_Mpbc2RURFL1CaseTempMaxSetThrDegCx10_Type = Integer32
_Mpbc2RURFL1CaseTempMaxSetThrDegCx10_Object = MibScalar
mpbc2RURFL1CaseTempMaxSetThrDegCx10 = _Mpbc2RURFL1CaseTempMaxSetThrDegCx10_Object(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 3, 3, 11),
    _Mpbc2RURFL1CaseTempMaxSetThrDegCx10_Type()
)
mpbc2RURFL1CaseTempMaxSetThrDegCx10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpbc2RURFL1CaseTempMaxSetThrDegCx10.setStatus("current")
_Mpbc2RURFL1CaseTempMaxClearThrDegCx10_Type = Integer32
_Mpbc2RURFL1CaseTempMaxClearThrDegCx10_Object = MibScalar
mpbc2RURFL1CaseTempMaxClearThrDegCx10 = _Mpbc2RURFL1CaseTempMaxClearThrDegCx10_Object(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 3, 3, 12),
    _Mpbc2RURFL1CaseTempMaxClearThrDegCx10_Type()
)
mpbc2RURFL1CaseTempMaxClearThrDegCx10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpbc2RURFL1CaseTempMaxClearThrDegCx10.setStatus("current")
_Mpbc2RURFL2_ObjectIdentity = ObjectIdentity
mpbc2RURFL2 = _Mpbc2RURFL2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 4)
)
_Mpbc2RURFL2Control_ObjectIdentity = ObjectIdentity
mpbc2RURFL2Control = _Mpbc2RURFL2Control_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 4, 1)
)


class _Mpbc2RURFL2LaserMode_Type(Integer32):
    """Custom type mpbc2RURFL2LaserMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("laserOff", 0),
          ("laserAPR", 1))
    )


_Mpbc2RURFL2LaserMode_Type.__name__ = "Integer32"
_Mpbc2RURFL2LaserMode_Object = MibScalar
mpbc2RURFL2LaserMode = _Mpbc2RURFL2LaserMode_Object(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 4, 1, 1),
    _Mpbc2RURFL2LaserMode_Type()
)
mpbc2RURFL2LaserMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mpbc2RURFL2LaserMode.setStatus("current")
_Mpbc2RURFL2ControlMode_Type = Integer32
_Mpbc2RURFL2ControlMode_Object = MibScalar
mpbc2RURFL2ControlMode = _Mpbc2RURFL2ControlMode_Object(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 4, 1, 2),
    _Mpbc2RURFL2ControlMode_Type()
)
mpbc2RURFL2ControlMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mpbc2RURFL2ControlMode.setStatus("current")
_Mpbc2RURFL2WL145xPwrSetPtmW_Type = Unsigned32
_Mpbc2RURFL2WL145xPwrSetPtmW_Object = MibScalar
mpbc2RURFL2WL145xPwrSetPtmW = _Mpbc2RURFL2WL145xPwrSetPtmW_Object(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 4, 1, 3),
    _Mpbc2RURFL2WL145xPwrSetPtmW_Type()
)
mpbc2RURFL2WL145xPwrSetPtmW.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mpbc2RURFL2WL145xPwrSetPtmW.setStatus("current")
_Mpbc2RURFL2WL142xPwrSetPtmW_Type = Unsigned32
_Mpbc2RURFL2WL142xPwrSetPtmW_Object = MibScalar
mpbc2RURFL2WL142xPwrSetPtmW = _Mpbc2RURFL2WL142xPwrSetPtmW_Object(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 4, 1, 4),
    _Mpbc2RURFL2WL142xPwrSetPtmW_Type()
)
mpbc2RURFL2WL142xPwrSetPtmW.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mpbc2RURFL2WL142xPwrSetPtmW.setStatus("current")
_Mpbc2RURFL2Reset_Type = TruthValue
_Mpbc2RURFL2Reset_Object = MibScalar
mpbc2RURFL2Reset = _Mpbc2RURFL2Reset_Object(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 4, 1, 5),
    _Mpbc2RURFL2Reset_Type()
)
mpbc2RURFL2Reset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mpbc2RURFL2Reset.setStatus("current")
_Mpbc2RURFL2Monitor_ObjectIdentity = ObjectIdentity
mpbc2RURFL2Monitor = _Mpbc2RURFL2Monitor_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 4, 2)
)
_Mpbc2RURFL2LD1CurmA_Type = Unsigned32
_Mpbc2RURFL2LD1CurmA_Object = MibScalar
mpbc2RURFL2LD1CurmA = _Mpbc2RURFL2LD1CurmA_Object(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 4, 2, 1),
    _Mpbc2RURFL2LD1CurmA_Type()
)
mpbc2RURFL2LD1CurmA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpbc2RURFL2LD1CurmA.setStatus("current")
_Mpbc2RURFL2LD1TempDegCx10_Type = Integer32
_Mpbc2RURFL2LD1TempDegCx10_Object = MibScalar
mpbc2RURFL2LD1TempDegCx10 = _Mpbc2RURFL2LD1TempDegCx10_Object(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 4, 2, 2),
    _Mpbc2RURFL2LD1TempDegCx10_Type()
)
mpbc2RURFL2LD1TempDegCx10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpbc2RURFL2LD1TempDegCx10.setStatus("current")
_Mpbc2RURFL2LD1TECCurmA_Type = Unsigned32
_Mpbc2RURFL2LD1TECCurmA_Object = MibScalar
mpbc2RURFL2LD1TECCurmA = _Mpbc2RURFL2LD1TECCurmA_Object(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 4, 2, 3),
    _Mpbc2RURFL2LD1TECCurmA_Type()
)
mpbc2RURFL2LD1TECCurmA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpbc2RURFL2LD1TECCurmA.setStatus("current")
_Mpbc2RURFL2LD2CurmA_Type = Unsigned32
_Mpbc2RURFL2LD2CurmA_Object = MibScalar
mpbc2RURFL2LD2CurmA = _Mpbc2RURFL2LD2CurmA_Object(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 4, 2, 4),
    _Mpbc2RURFL2LD2CurmA_Type()
)
mpbc2RURFL2LD2CurmA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpbc2RURFL2LD2CurmA.setStatus("current")
_Mpbc2RURFL2CaseTempDegCx10_Type = Integer32
_Mpbc2RURFL2CaseTempDegCx10_Object = MibScalar
mpbc2RURFL2CaseTempDegCx10 = _Mpbc2RURFL2CaseTempDegCx10_Object(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 4, 2, 5),
    _Mpbc2RURFL2CaseTempDegCx10_Type()
)
mpbc2RURFL2CaseTempDegCx10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpbc2RURFL2CaseTempDegCx10.setStatus("current")
_Mpbc2RURFL2SeedPwrmWx100_Type = Unsigned32
_Mpbc2RURFL2SeedPwrmWx100_Object = MibScalar
mpbc2RURFL2SeedPwrmWx100 = _Mpbc2RURFL2SeedPwrmWx100_Object(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 4, 2, 6),
    _Mpbc2RURFL2SeedPwrmWx100_Type()
)
mpbc2RURFL2SeedPwrmWx100.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpbc2RURFL2SeedPwrmWx100.setStatus("current")
_Mpbc2RURFL2WL142xOutPwrmWx10_Type = Unsigned32
_Mpbc2RURFL2WL142xOutPwrmWx10_Object = MibScalar
mpbc2RURFL2WL142xOutPwrmWx10 = _Mpbc2RURFL2WL142xOutPwrmWx10_Object(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 4, 2, 7),
    _Mpbc2RURFL2WL142xOutPwrmWx10_Type()
)
mpbc2RURFL2WL142xOutPwrmWx10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpbc2RURFL2WL142xOutPwrmWx10.setStatus("current")
_Mpbc2RURFL2WL145xOutPwrmWx10_Type = Unsigned32
_Mpbc2RURFL2WL145xOutPwrmWx10_Object = MibScalar
mpbc2RURFL2WL145xOutPwrmWx10 = _Mpbc2RURFL2WL145xOutPwrmWx10_Object(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 4, 2, 8),
    _Mpbc2RURFL2WL145xOutPwrmWx10_Type()
)
mpbc2RURFL2WL145xOutPwrmWx10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpbc2RURFL2WL145xOutPwrmWx10.setStatus("current")
_Mpbc2RURFL2TotalOutPwrmWx10_Type = Unsigned32
_Mpbc2RURFL2TotalOutPwrmWx10_Object = MibScalar
mpbc2RURFL2TotalOutPwrmWx10 = _Mpbc2RURFL2TotalOutPwrmWx10_Object(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 4, 2, 9),
    _Mpbc2RURFL2TotalOutPwrmWx10_Type()
)
mpbc2RURFL2TotalOutPwrmWx10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpbc2RURFL2TotalOutPwrmWx10.setStatus("current")


class _Mpbc2RURFL2MonLaserState_Type(Integer32):
    """Custom type mpbc2RURFL2MonLaserState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              10)
        )
    )
    namedValues = NamedValues(
        *(("laserOff", 0),
          ("laserNormal", 1),
          ("laserALS", 2),
          ("laserALS100", 3),
          ("laserOn", 10))
    )


_Mpbc2RURFL2MonLaserState_Type.__name__ = "Integer32"
_Mpbc2RURFL2MonLaserState_Object = MibScalar
mpbc2RURFL2MonLaserState = _Mpbc2RURFL2MonLaserState_Object(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 4, 2, 10),
    _Mpbc2RURFL2MonLaserState_Type()
)
mpbc2RURFL2MonLaserState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpbc2RURFL2MonLaserState.setStatus("current")


class _Mpbc2RURFL2MonLaserMode_Type(Integer32):
    """Custom type mpbc2RURFL2MonLaserMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              10)
        )
    )
    namedValues = NamedValues(
        *(("laserOff", 0),
          ("laserAPR", 1),
          ("laserOn", 10))
    )


_Mpbc2RURFL2MonLaserMode_Type.__name__ = "Integer32"
_Mpbc2RURFL2MonLaserMode_Object = MibScalar
mpbc2RURFL2MonLaserMode = _Mpbc2RURFL2MonLaserMode_Object(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 4, 2, 11),
    _Mpbc2RURFL2MonLaserMode_Type()
)
mpbc2RURFL2MonLaserMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpbc2RURFL2MonLaserMode.setStatus("current")
_Mpbc2RURFL2MonControlMode_Type = Integer32
_Mpbc2RURFL2MonControlMode_Object = MibScalar
mpbc2RURFL2MonControlMode = _Mpbc2RURFL2MonControlMode_Object(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 4, 2, 12),
    _Mpbc2RURFL2MonControlMode_Type()
)
mpbc2RURFL2MonControlMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpbc2RURFL2MonControlMode.setStatus("current")
_Mpbc2RURFL2DisableInputState_Type = Integer32
_Mpbc2RURFL2DisableInputState_Object = MibScalar
mpbc2RURFL2DisableInputState = _Mpbc2RURFL2DisableInputState_Object(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 4, 2, 13),
    _Mpbc2RURFL2DisableInputState_Type()
)
mpbc2RURFL2DisableInputState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpbc2RURFL2DisableInputState.setStatus("current")


class _Mpbc2RURFL2UnitState_Type(Integer32):
    """Custom type mpbc2RURFL2UnitState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("stateInit", 0),
          ("stateNormal", 1),
          ("stateFault", 2))
    )


_Mpbc2RURFL2UnitState_Type.__name__ = "Integer32"
_Mpbc2RURFL2UnitState_Object = MibScalar
mpbc2RURFL2UnitState = _Mpbc2RURFL2UnitState_Object(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 4, 2, 14),
    _Mpbc2RURFL2UnitState_Type()
)
mpbc2RURFL2UnitState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpbc2RURFL2UnitState.setStatus("current")


class _Mpbc2RURFL2OSCRxTone_Type(Integer32):
    """Custom type mpbc2RURFL2OSCRxTone based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("noTone", 0),
          ("tone1", 1),
          ("tone2", 2),
          ("tone1plus2", 3))
    )


_Mpbc2RURFL2OSCRxTone_Type.__name__ = "Integer32"
_Mpbc2RURFL2OSCRxTone_Object = MibScalar
mpbc2RURFL2OSCRxTone = _Mpbc2RURFL2OSCRxTone_Object(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 4, 2, 15),
    _Mpbc2RURFL2OSCRxTone_Type()
)
mpbc2RURFL2OSCRxTone.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpbc2RURFL2OSCRxTone.setStatus("current")
_Mpbc2RURFL2OSCTempDegCx10_Type = Integer32
_Mpbc2RURFL2OSCTempDegCx10_Object = MibScalar
mpbc2RURFL2OSCTempDegCx10 = _Mpbc2RURFL2OSCTempDegCx10_Object(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 4, 2, 16),
    _Mpbc2RURFL2OSCTempDegCx10_Type()
)
mpbc2RURFL2OSCTempDegCx10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpbc2RURFL2OSCTempDegCx10.setStatus("current")


class _Mpbc2RURFL2OSCTxTone_Type(Integer32):
    """Custom type mpbc2RURFL2OSCTxTone based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("tone1", 1),
          ("tone2", 2))
    )


_Mpbc2RURFL2OSCTxTone_Type.__name__ = "Integer32"
_Mpbc2RURFL2OSCTxTone_Object = MibScalar
mpbc2RURFL2OSCTxTone = _Mpbc2RURFL2OSCTxTone_Object(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 4, 2, 17),
    _Mpbc2RURFL2OSCTxTone_Type()
)
mpbc2RURFL2OSCTxTone.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpbc2RURFL2OSCTxTone.setStatus("current")
_Mpbc2RURFL2OSCTxPwrmWx100_Type = Integer32
_Mpbc2RURFL2OSCTxPwrmWx100_Object = MibScalar
mpbc2RURFL2OSCTxPwrmWx100 = _Mpbc2RURFL2OSCTxPwrmWx100_Object(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 4, 2, 18),
    _Mpbc2RURFL2OSCTxPwrmWx100_Type()
)
mpbc2RURFL2OSCTxPwrmWx100.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpbc2RURFL2OSCTxPwrmWx100.setStatus("current")
_Mpbc2RURFL2Configuration_ObjectIdentity = ObjectIdentity
mpbc2RURFL2Configuration = _Mpbc2RURFL2Configuration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 4, 3)
)
_Mpbc2RURFL2LD1CurMinThrmA_Type = Unsigned32
_Mpbc2RURFL2LD1CurMinThrmA_Object = MibScalar
mpbc2RURFL2LD1CurMinThrmA = _Mpbc2RURFL2LD1CurMinThrmA_Object(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 4, 3, 1),
    _Mpbc2RURFL2LD1CurMinThrmA_Type()
)
mpbc2RURFL2LD1CurMinThrmA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpbc2RURFL2LD1CurMinThrmA.setStatus("current")
_Mpbc2RURFL2LD1CurMaxThrmA_Type = Unsigned32
_Mpbc2RURFL2LD1CurMaxThrmA_Object = MibScalar
mpbc2RURFL2LD1CurMaxThrmA = _Mpbc2RURFL2LD1CurMaxThrmA_Object(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 4, 3, 2),
    _Mpbc2RURFL2LD1CurMaxThrmA_Type()
)
mpbc2RURFL2LD1CurMaxThrmA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpbc2RURFL2LD1CurMaxThrmA.setStatus("current")
_Mpbc2RURFL2LD2CurMinThrmA_Type = Unsigned32
_Mpbc2RURFL2LD2CurMinThrmA_Object = MibScalar
mpbc2RURFL2LD2CurMinThrmA = _Mpbc2RURFL2LD2CurMinThrmA_Object(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 4, 3, 3),
    _Mpbc2RURFL2LD2CurMinThrmA_Type()
)
mpbc2RURFL2LD2CurMinThrmA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpbc2RURFL2LD2CurMinThrmA.setStatus("current")
_Mpbc2RURFL2LD2CurMaxThrmA_Type = Unsigned32
_Mpbc2RURFL2LD2CurMaxThrmA_Object = MibScalar
mpbc2RURFL2LD2CurMaxThrmA = _Mpbc2RURFL2LD2CurMaxThrmA_Object(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 4, 3, 4),
    _Mpbc2RURFL2LD2CurMaxThrmA_Type()
)
mpbc2RURFL2LD2CurMaxThrmA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpbc2RURFL2LD2CurMaxThrmA.setStatus("current")
_Mpbc2RURFL2CaseTempMinSetThrDegCx10_Type = Integer32
_Mpbc2RURFL2CaseTempMinSetThrDegCx10_Object = MibScalar
mpbc2RURFL2CaseTempMinSetThrDegCx10 = _Mpbc2RURFL2CaseTempMinSetThrDegCx10_Object(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 4, 3, 5),
    _Mpbc2RURFL2CaseTempMinSetThrDegCx10_Type()
)
mpbc2RURFL2CaseTempMinSetThrDegCx10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpbc2RURFL2CaseTempMinSetThrDegCx10.setStatus("current")
_Mpbc2RURFL2CaseTempMinClearThrDegCx10_Type = Integer32
_Mpbc2RURFL2CaseTempMinClearThrDegCx10_Object = MibScalar
mpbc2RURFL2CaseTempMinClearThrDegCx10 = _Mpbc2RURFL2CaseTempMinClearThrDegCx10_Object(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 4, 3, 6),
    _Mpbc2RURFL2CaseTempMinClearThrDegCx10_Type()
)
mpbc2RURFL2CaseTempMinClearThrDegCx10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpbc2RURFL2CaseTempMinClearThrDegCx10.setStatus("current")
_Mpbc2RURFL2CaseTempMaxSetThrDegCx10_Type = Integer32
_Mpbc2RURFL2CaseTempMaxSetThrDegCx10_Object = MibScalar
mpbc2RURFL2CaseTempMaxSetThrDegCx10 = _Mpbc2RURFL2CaseTempMaxSetThrDegCx10_Object(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 4, 3, 7),
    _Mpbc2RURFL2CaseTempMaxSetThrDegCx10_Type()
)
mpbc2RURFL2CaseTempMaxSetThrDegCx10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpbc2RURFL2CaseTempMaxSetThrDegCx10.setStatus("current")
_Mpbc2RURFL2CaseTempMaxClearThrDegCx10_Type = Integer32
_Mpbc2RURFL2CaseTempMaxClearThrDegCx10_Object = MibScalar
mpbc2RURFL2CaseTempMaxClearThrDegCx10 = _Mpbc2RURFL2CaseTempMaxClearThrDegCx10_Object(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 4, 3, 8),
    _Mpbc2RURFL2CaseTempMaxClearThrDegCx10_Type()
)
mpbc2RURFL2CaseTempMaxClearThrDegCx10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpbc2RURFL2CaseTempMaxClearThrDegCx10.setStatus("current")
_Mpbc2RURFL2WL1OutputMinThrdBx10_Type = Integer32
_Mpbc2RURFL2WL1OutputMinThrdBx10_Object = MibScalar
mpbc2RURFL2WL1OutputMinThrdBx10 = _Mpbc2RURFL2WL1OutputMinThrdBx10_Object(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 4, 3, 9),
    _Mpbc2RURFL2WL1OutputMinThrdBx10_Type()
)
mpbc2RURFL2WL1OutputMinThrdBx10.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mpbc2RURFL2WL1OutputMinThrdBx10.setStatus("current")
_Mpbc2RURFL2WL1OutputMaxThrdBx10_Type = Integer32
_Mpbc2RURFL2WL1OutputMaxThrdBx10_Object = MibScalar
mpbc2RURFL2WL1OutputMaxThrdBx10 = _Mpbc2RURFL2WL1OutputMaxThrdBx10_Object(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 4, 3, 10),
    _Mpbc2RURFL2WL1OutputMaxThrdBx10_Type()
)
mpbc2RURFL2WL1OutputMaxThrdBx10.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mpbc2RURFL2WL1OutputMaxThrdBx10.setStatus("current")
_Mpbc2RURFL2WL1FaultSetpointmA_Type = Unsigned32
_Mpbc2RURFL2WL1FaultSetpointmA_Object = MibScalar
mpbc2RURFL2WL1FaultSetpointmA = _Mpbc2RURFL2WL1FaultSetpointmA_Object(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 4, 3, 11),
    _Mpbc2RURFL2WL1FaultSetpointmA_Type()
)
mpbc2RURFL2WL1FaultSetpointmA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpbc2RURFL2WL1FaultSetpointmA.setStatus("current")
_Mpbc2RURFL2WL1FaultThr_Type = Unsigned32
_Mpbc2RURFL2WL1FaultThr_Object = MibScalar
mpbc2RURFL2WL1FaultThr = _Mpbc2RURFL2WL1FaultThr_Object(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 4, 3, 12),
    _Mpbc2RURFL2WL1FaultThr_Type()
)
mpbc2RURFL2WL1FaultThr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpbc2RURFL2WL1FaultThr.setStatus("current")
_Mpbc2RURFL2WL1FaultDelayms_Type = Unsigned32
_Mpbc2RURFL2WL1FaultDelayms_Object = MibScalar
mpbc2RURFL2WL1FaultDelayms = _Mpbc2RURFL2WL1FaultDelayms_Object(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 4, 3, 13),
    _Mpbc2RURFL2WL1FaultDelayms_Type()
)
mpbc2RURFL2WL1FaultDelayms.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpbc2RURFL2WL1FaultDelayms.setStatus("current")
_Mpbc2RURFL2WL2OutputMinThrdBx10_Type = Integer32
_Mpbc2RURFL2WL2OutputMinThrdBx10_Object = MibScalar
mpbc2RURFL2WL2OutputMinThrdBx10 = _Mpbc2RURFL2WL2OutputMinThrdBx10_Object(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 4, 3, 14),
    _Mpbc2RURFL2WL2OutputMinThrdBx10_Type()
)
mpbc2RURFL2WL2OutputMinThrdBx10.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mpbc2RURFL2WL2OutputMinThrdBx10.setStatus("current")
_Mpbc2RURFL2WL2OutputMaxThrdBx10_Type = Integer32
_Mpbc2RURFL2WL2OutputMaxThrdBx10_Object = MibScalar
mpbc2RURFL2WL2OutputMaxThrdBx10 = _Mpbc2RURFL2WL2OutputMaxThrdBx10_Object(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 4, 3, 15),
    _Mpbc2RURFL2WL2OutputMaxThrdBx10_Type()
)
mpbc2RURFL2WL2OutputMaxThrdBx10.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mpbc2RURFL2WL2OutputMaxThrdBx10.setStatus("current")
_Mpbc2RURFL2CaseTempMinAlrmThrDegCx10_Type = Integer32
_Mpbc2RURFL2CaseTempMinAlrmThrDegCx10_Object = MibScalar
mpbc2RURFL2CaseTempMinAlrmThrDegCx10 = _Mpbc2RURFL2CaseTempMinAlrmThrDegCx10_Object(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 4, 3, 16),
    _Mpbc2RURFL2CaseTempMinAlrmThrDegCx10_Type()
)
mpbc2RURFL2CaseTempMinAlrmThrDegCx10.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mpbc2RURFL2CaseTempMinAlrmThrDegCx10.setStatus("current")
_Mpbc2RURFL2CaseTempMaxAlrmThrDegCx10_Type = Integer32
_Mpbc2RURFL2CaseTempMaxAlrmThrDegCx10_Object = MibScalar
mpbc2RURFL2CaseTempMaxAlrmThrDegCx10 = _Mpbc2RURFL2CaseTempMaxAlrmThrDegCx10_Object(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 4, 3, 17),
    _Mpbc2RURFL2CaseTempMaxAlrmThrDegCx10_Type()
)
mpbc2RURFL2CaseTempMaxAlrmThrDegCx10.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mpbc2RURFL2CaseTempMaxAlrmThrDegCx10.setStatus("current")
_Mpbc2RURFL2WL2OutputPwrMinLimdBmx10_Type = Integer32
_Mpbc2RURFL2WL2OutputPwrMinLimdBmx10_Object = MibScalar
mpbc2RURFL2WL2OutputPwrMinLimdBmx10 = _Mpbc2RURFL2WL2OutputPwrMinLimdBmx10_Object(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 4, 3, 18),
    _Mpbc2RURFL2WL2OutputPwrMinLimdBmx10_Type()
)
mpbc2RURFL2WL2OutputPwrMinLimdBmx10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpbc2RURFL2WL2OutputPwrMinLimdBmx10.setStatus("current")
_Mpbc2RURFL2WL2OutputPwrMaxLimdBmx10_Type = Integer32
_Mpbc2RURFL2WL2OutputPwrMaxLimdBmx10_Object = MibScalar
mpbc2RURFL2WL2OutputPwrMaxLimdBmx10 = _Mpbc2RURFL2WL2OutputPwrMaxLimdBmx10_Object(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 4, 3, 19),
    _Mpbc2RURFL2WL2OutputPwrMaxLimdBmx10_Type()
)
mpbc2RURFL2WL2OutputPwrMaxLimdBmx10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpbc2RURFL2WL2OutputPwrMaxLimdBmx10.setStatus("current")
_Mpbc2RURFL2WL1OutputPwrMinLimdBmx10_Type = Integer32
_Mpbc2RURFL2WL1OutputPwrMinLimdBmx10_Object = MibScalar
mpbc2RURFL2WL1OutputPwrMinLimdBmx10 = _Mpbc2RURFL2WL1OutputPwrMinLimdBmx10_Object(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 4, 3, 20),
    _Mpbc2RURFL2WL1OutputPwrMinLimdBmx10_Type()
)
mpbc2RURFL2WL1OutputPwrMinLimdBmx10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpbc2RURFL2WL1OutputPwrMinLimdBmx10.setStatus("current")
_Mpbc2RURFL2WL1OutputPwrMaxLimdBmx10_Type = Integer32
_Mpbc2RURFL2WL1OutputPwrMaxLimdBmx10_Object = MibScalar
mpbc2RURFL2WL1OutputPwrMaxLimdBmx10 = _Mpbc2RURFL2WL1OutputPwrMaxLimdBmx10_Object(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 4, 3, 21),
    _Mpbc2RURFL2WL1OutputPwrMaxLimdBmx10_Type()
)
mpbc2RURFL2WL1OutputPwrMaxLimdBmx10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpbc2RURFL2WL1OutputPwrMaxLimdBmx10.setStatus("current")
_Mpbc2RUSRCP_ObjectIdentity = ObjectIdentity
mpbc2RUSRCP = _Mpbc2RUSRCP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 5)
)
_Mpbc2RUSRCPControl_ObjectIdentity = ObjectIdentity
mpbc2RUSRCPControl = _Mpbc2RUSRCPControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 5, 1)
)


class _Mpbc2RUSRCPLaserMode_Type(Integer32):
    """Custom type mpbc2RUSRCPLaserMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("laserOff", 0),
          ("laserAPR", 1))
    )


_Mpbc2RUSRCPLaserMode_Type.__name__ = "Integer32"
_Mpbc2RUSRCPLaserMode_Object = MibScalar
mpbc2RUSRCPLaserMode = _Mpbc2RUSRCPLaserMode_Object(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 5, 1, 1),
    _Mpbc2RUSRCPLaserMode_Type()
)
mpbc2RUSRCPLaserMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mpbc2RUSRCPLaserMode.setStatus("current")
_Mpbc2RUSRCPControlMode_Type = Integer32
_Mpbc2RUSRCPControlMode_Object = MibScalar
mpbc2RUSRCPControlMode = _Mpbc2RUSRCPControlMode_Object(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 5, 1, 2),
    _Mpbc2RUSRCPControlMode_Type()
)
mpbc2RUSRCPControlMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mpbc2RUSRCPControlMode.setStatus("current")
_Mpbc2RUSRCPSeedOutputPwrmW_Type = Unsigned32
_Mpbc2RUSRCPSeedOutputPwrmW_Object = MibScalar
mpbc2RUSRCPSeedOutputPwrmW = _Mpbc2RUSRCPSeedOutputPwrmW_Object(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 5, 1, 3),
    _Mpbc2RUSRCPSeedOutputPwrmW_Type()
)
mpbc2RUSRCPSeedOutputPwrmW.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mpbc2RUSRCPSeedOutputPwrmW.setStatus("current")
_Mpbc2RUSRCPMainOutputPwrmW_Type = Unsigned32
_Mpbc2RUSRCPMainOutputPwrmW_Object = MibScalar
mpbc2RUSRCPMainOutputPwrmW = _Mpbc2RUSRCPMainOutputPwrmW_Object(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 5, 1, 4),
    _Mpbc2RUSRCPMainOutputPwrmW_Type()
)
mpbc2RUSRCPMainOutputPwrmW.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mpbc2RUSRCPMainOutputPwrmW.setStatus("current")
_Mpbc2RUSRCPReset_Type = TruthValue
_Mpbc2RUSRCPReset_Object = MibScalar
mpbc2RUSRCPReset = _Mpbc2RUSRCPReset_Object(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 5, 1, 5),
    _Mpbc2RUSRCPReset_Type()
)
mpbc2RUSRCPReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mpbc2RUSRCPReset.setStatus("current")
_Mpbc2RUSRCPMonitor_ObjectIdentity = ObjectIdentity
mpbc2RUSRCPMonitor = _Mpbc2RUSRCPMonitor_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 5, 2)
)
_Mpbc2RUSRCPLD1CurmA_Type = Unsigned32
_Mpbc2RUSRCPLD1CurmA_Object = MibScalar
mpbc2RUSRCPLD1CurmA = _Mpbc2RUSRCPLD1CurmA_Object(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 5, 2, 1),
    _Mpbc2RUSRCPLD1CurmA_Type()
)
mpbc2RUSRCPLD1CurmA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpbc2RUSRCPLD1CurmA.setStatus("current")
_Mpbc2RUSRCPLD1TempDegCx10_Type = Integer32
_Mpbc2RUSRCPLD1TempDegCx10_Object = MibScalar
mpbc2RUSRCPLD1TempDegCx10 = _Mpbc2RUSRCPLD1TempDegCx10_Object(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 5, 2, 2),
    _Mpbc2RUSRCPLD1TempDegCx10_Type()
)
mpbc2RUSRCPLD1TempDegCx10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpbc2RUSRCPLD1TempDegCx10.setStatus("current")
_Mpbc2RUSRCPLD1TECCurmA_Type = Unsigned32
_Mpbc2RUSRCPLD1TECCurmA_Object = MibScalar
mpbc2RUSRCPLD1TECCurmA = _Mpbc2RUSRCPLD1TECCurmA_Object(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 5, 2, 3),
    _Mpbc2RUSRCPLD1TECCurmA_Type()
)
mpbc2RUSRCPLD1TECCurmA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpbc2RUSRCPLD1TECCurmA.setStatus("current")
_Mpbc2RUSRCPLD2CurmA_Type = Unsigned32
_Mpbc2RUSRCPLD2CurmA_Object = MibScalar
mpbc2RUSRCPLD2CurmA = _Mpbc2RUSRCPLD2CurmA_Object(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 5, 2, 4),
    _Mpbc2RUSRCPLD2CurmA_Type()
)
mpbc2RUSRCPLD2CurmA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpbc2RUSRCPLD2CurmA.setStatus("current")
_Mpbc2RUSRCPCaseTempDegCx10_Type = Integer32
_Mpbc2RUSRCPCaseTempDegCx10_Object = MibScalar
mpbc2RUSRCPCaseTempDegCx10 = _Mpbc2RUSRCPCaseTempDegCx10_Object(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 5, 2, 5),
    _Mpbc2RUSRCPCaseTempDegCx10_Type()
)
mpbc2RUSRCPCaseTempDegCx10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpbc2RUSRCPCaseTempDegCx10.setStatus("current")
_Mpbc2RUSRCPMonSeedOutputPwrmWx10_Type = Unsigned32
_Mpbc2RUSRCPMonSeedOutputPwrmWx10_Object = MibScalar
mpbc2RUSRCPMonSeedOutputPwrmWx10 = _Mpbc2RUSRCPMonSeedOutputPwrmWx10_Object(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 5, 2, 6),
    _Mpbc2RUSRCPMonSeedOutputPwrmWx10_Type()
)
mpbc2RUSRCPMonSeedOutputPwrmWx10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpbc2RUSRCPMonSeedOutputPwrmWx10.setStatus("current")
_Mpbc2RUSRCPMainOutputPwrmWx10_Type = Unsigned32
_Mpbc2RUSRCPMainOutputPwrmWx10_Object = MibScalar
mpbc2RUSRCPMainOutputPwrmWx10 = _Mpbc2RUSRCPMainOutputPwrmWx10_Object(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 5, 2, 7),
    _Mpbc2RUSRCPMainOutputPwrmWx10_Type()
)
mpbc2RUSRCPMainOutputPwrmWx10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpbc2RUSRCPMainOutputPwrmWx10.setStatus("current")
_Mpbc2RUSRCPInputPwrmWx100_Type = Unsigned32
_Mpbc2RUSRCPInputPwrmWx100_Object = MibScalar
mpbc2RUSRCPInputPwrmWx100 = _Mpbc2RUSRCPInputPwrmWx100_Object(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 5, 2, 8),
    _Mpbc2RUSRCPInputPwrmWx100_Type()
)
mpbc2RUSRCPInputPwrmWx100.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpbc2RUSRCPInputPwrmWx100.setStatus("current")


class _Mpbc2RUSRCPMonLaserState_Type(Integer32):
    """Custom type mpbc2RUSRCPMonLaserState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              10)
        )
    )
    namedValues = NamedValues(
        *(("laserOff", 0),
          ("laserNormal", 1),
          ("laserALS", 2),
          ("laserALS100", 3),
          ("laserOn", 10))
    )


_Mpbc2RUSRCPMonLaserState_Type.__name__ = "Integer32"
_Mpbc2RUSRCPMonLaserState_Object = MibScalar
mpbc2RUSRCPMonLaserState = _Mpbc2RUSRCPMonLaserState_Object(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 5, 2, 9),
    _Mpbc2RUSRCPMonLaserState_Type()
)
mpbc2RUSRCPMonLaserState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpbc2RUSRCPMonLaserState.setStatus("current")


class _Mpbc2RUSRCPMonLaserMode_Type(Integer32):
    """Custom type mpbc2RUSRCPMonLaserMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              10)
        )
    )
    namedValues = NamedValues(
        *(("laserOff", 0),
          ("laserAPR", 1),
          ("laserOn", 10))
    )


_Mpbc2RUSRCPMonLaserMode_Type.__name__ = "Integer32"
_Mpbc2RUSRCPMonLaserMode_Object = MibScalar
mpbc2RUSRCPMonLaserMode = _Mpbc2RUSRCPMonLaserMode_Object(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 5, 2, 10),
    _Mpbc2RUSRCPMonLaserMode_Type()
)
mpbc2RUSRCPMonLaserMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpbc2RUSRCPMonLaserMode.setStatus("current")
_Mpbc2RUSRCPMonControlMode_Type = Unsigned32
_Mpbc2RUSRCPMonControlMode_Object = MibScalar
mpbc2RUSRCPMonControlMode = _Mpbc2RUSRCPMonControlMode_Object(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 5, 2, 11),
    _Mpbc2RUSRCPMonControlMode_Type()
)
mpbc2RUSRCPMonControlMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpbc2RUSRCPMonControlMode.setStatus("current")
_Mpbc2RUSRCPDisableInputState_Type = Unsigned32
_Mpbc2RUSRCPDisableInputState_Object = MibScalar
mpbc2RUSRCPDisableInputState = _Mpbc2RUSRCPDisableInputState_Object(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 5, 2, 12),
    _Mpbc2RUSRCPDisableInputState_Type()
)
mpbc2RUSRCPDisableInputState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpbc2RUSRCPDisableInputState.setStatus("current")


class _Mpbc2RUSRCPUnitState_Type(Integer32):
    """Custom type mpbc2RUSRCPUnitState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("stateInit", 0),
          ("stateNormal", 1),
          ("stateFault", 2))
    )


_Mpbc2RUSRCPUnitState_Type.__name__ = "Integer32"
_Mpbc2RUSRCPUnitState_Object = MibScalar
mpbc2RUSRCPUnitState = _Mpbc2RUSRCPUnitState_Object(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 5, 2, 13),
    _Mpbc2RUSRCPUnitState_Type()
)
mpbc2RUSRCPUnitState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpbc2RUSRCPUnitState.setStatus("current")


class _Mpbc2RUSRCPOSCRxTone_Type(Integer32):
    """Custom type mpbc2RUSRCPOSCRxTone based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("noTone", 0),
          ("tone1", 1),
          ("tone2", 2),
          ("tone1plus2", 3))
    )


_Mpbc2RUSRCPOSCRxTone_Type.__name__ = "Integer32"
_Mpbc2RUSRCPOSCRxTone_Object = MibScalar
mpbc2RUSRCPOSCRxTone = _Mpbc2RUSRCPOSCRxTone_Object(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 5, 2, 14),
    _Mpbc2RUSRCPOSCRxTone_Type()
)
mpbc2RUSRCPOSCRxTone.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpbc2RUSRCPOSCRxTone.setStatus("current")
_Mpbc2RUSRCPOSCTempdegCx10_Type = Integer32
_Mpbc2RUSRCPOSCTempdegCx10_Object = MibScalar
mpbc2RUSRCPOSCTempdegCx10 = _Mpbc2RUSRCPOSCTempdegCx10_Object(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 5, 2, 15),
    _Mpbc2RUSRCPOSCTempdegCx10_Type()
)
mpbc2RUSRCPOSCTempdegCx10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpbc2RUSRCPOSCTempdegCx10.setStatus("current")


class _Mpbc2RUSRCPOSCTxTone_Type(Integer32):
    """Custom type mpbc2RUSRCPOSCTxTone based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("tone1", 1),
          ("tone2", 2))
    )


_Mpbc2RUSRCPOSCTxTone_Type.__name__ = "Integer32"
_Mpbc2RUSRCPOSCTxTone_Object = MibScalar
mpbc2RUSRCPOSCTxTone = _Mpbc2RUSRCPOSCTxTone_Object(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 5, 2, 16),
    _Mpbc2RUSRCPOSCTxTone_Type()
)
mpbc2RUSRCPOSCTxTone.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpbc2RUSRCPOSCTxTone.setStatus("current")
_Mpbc2RUSRCPOSCTxPwrmWx100_Type = Integer32
_Mpbc2RUSRCPOSCTxPwrmWx100_Object = MibScalar
mpbc2RUSRCPOSCTxPwrmWx100 = _Mpbc2RUSRCPOSCTxPwrmWx100_Object(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 5, 2, 17),
    _Mpbc2RUSRCPOSCTxPwrmWx100_Type()
)
mpbc2RUSRCPOSCTxPwrmWx100.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpbc2RUSRCPOSCTxPwrmWx100.setStatus("current")


class _Mpbc2RUSRCPOSCRx1610Tone_Type(Integer32):
    """Custom type mpbc2RUSRCPOSCRx1610Tone based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("noTone", 0),
          ("tone1", 1),
          ("tone2", 2),
          ("tone1plus2", 3))
    )


_Mpbc2RUSRCPOSCRx1610Tone_Type.__name__ = "Integer32"
_Mpbc2RUSRCPOSCRx1610Tone_Object = MibScalar
mpbc2RUSRCPOSCRx1610Tone = _Mpbc2RUSRCPOSCRx1610Tone_Object(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 5, 2, 18),
    _Mpbc2RUSRCPOSCRx1610Tone_Type()
)
mpbc2RUSRCPOSCRx1610Tone.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpbc2RUSRCPOSCRx1610Tone.setStatus("current")
_Mpbc2RUSRCPConfiguration_ObjectIdentity = ObjectIdentity
mpbc2RUSRCPConfiguration = _Mpbc2RUSRCPConfiguration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 5, 3)
)
_Mpbc2RUSRCPLD1CurMinThrmA_Type = Unsigned32
_Mpbc2RUSRCPLD1CurMinThrmA_Object = MibScalar
mpbc2RUSRCPLD1CurMinThrmA = _Mpbc2RUSRCPLD1CurMinThrmA_Object(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 5, 3, 1),
    _Mpbc2RUSRCPLD1CurMinThrmA_Type()
)
mpbc2RUSRCPLD1CurMinThrmA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpbc2RUSRCPLD1CurMinThrmA.setStatus("current")
_Mpbc2RUSRCPLD1CurMaxThrmA_Type = Unsigned32
_Mpbc2RUSRCPLD1CurMaxThrmA_Object = MibScalar
mpbc2RUSRCPLD1CurMaxThrmA = _Mpbc2RUSRCPLD1CurMaxThrmA_Object(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 5, 3, 2),
    _Mpbc2RUSRCPLD1CurMaxThrmA_Type()
)
mpbc2RUSRCPLD1CurMaxThrmA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpbc2RUSRCPLD1CurMaxThrmA.setStatus("current")
_Mpbc2RUSRCPLD2CurMinThrmA_Type = Unsigned32
_Mpbc2RUSRCPLD2CurMinThrmA_Object = MibScalar
mpbc2RUSRCPLD2CurMinThrmA = _Mpbc2RUSRCPLD2CurMinThrmA_Object(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 5, 3, 3),
    _Mpbc2RUSRCPLD2CurMinThrmA_Type()
)
mpbc2RUSRCPLD2CurMinThrmA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpbc2RUSRCPLD2CurMinThrmA.setStatus("current")
_Mpbc2RUSRCPLD2CurMaxThrmA_Type = Unsigned32
_Mpbc2RUSRCPLD2CurMaxThrmA_Object = MibScalar
mpbc2RUSRCPLD2CurMaxThrmA = _Mpbc2RUSRCPLD2CurMaxThrmA_Object(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 5, 3, 4),
    _Mpbc2RUSRCPLD2CurMaxThrmA_Type()
)
mpbc2RUSRCPLD2CurMaxThrmA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpbc2RUSRCPLD2CurMaxThrmA.setStatus("current")
_Mpbc2RUSRCPCaseTempMinSetThrDegCx10_Type = Integer32
_Mpbc2RUSRCPCaseTempMinSetThrDegCx10_Object = MibScalar
mpbc2RUSRCPCaseTempMinSetThrDegCx10 = _Mpbc2RUSRCPCaseTempMinSetThrDegCx10_Object(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 5, 3, 5),
    _Mpbc2RUSRCPCaseTempMinSetThrDegCx10_Type()
)
mpbc2RUSRCPCaseTempMinSetThrDegCx10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpbc2RUSRCPCaseTempMinSetThrDegCx10.setStatus("current")
_Mpbc2RUSRCPCaseTempMinClearThrDegCx10_Type = Integer32
_Mpbc2RUSRCPCaseTempMinClearThrDegCx10_Object = MibScalar
mpbc2RUSRCPCaseTempMinClearThrDegCx10 = _Mpbc2RUSRCPCaseTempMinClearThrDegCx10_Object(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 5, 3, 6),
    _Mpbc2RUSRCPCaseTempMinClearThrDegCx10_Type()
)
mpbc2RUSRCPCaseTempMinClearThrDegCx10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpbc2RUSRCPCaseTempMinClearThrDegCx10.setStatus("current")
_Mpbc2RUSRCPCaseTempMaxSetThrDegCx10_Type = Integer32
_Mpbc2RUSRCPCaseTempMaxSetThrDegCx10_Object = MibScalar
mpbc2RUSRCPCaseTempMaxSetThrDegCx10 = _Mpbc2RUSRCPCaseTempMaxSetThrDegCx10_Object(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 5, 3, 7),
    _Mpbc2RUSRCPCaseTempMaxSetThrDegCx10_Type()
)
mpbc2RUSRCPCaseTempMaxSetThrDegCx10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpbc2RUSRCPCaseTempMaxSetThrDegCx10.setStatus("current")
_Mpbc2RUSRCPCaseTempMaxClearThrDegCx10_Type = Integer32
_Mpbc2RUSRCPCaseTempMaxClearThrDegCx10_Object = MibScalar
mpbc2RUSRCPCaseTempMaxClearThrDegCx10 = _Mpbc2RUSRCPCaseTempMaxClearThrDegCx10_Object(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 5, 3, 8),
    _Mpbc2RUSRCPCaseTempMaxClearThrDegCx10_Type()
)
mpbc2RUSRCPCaseTempMaxClearThrDegCx10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpbc2RUSRCPCaseTempMaxClearThrDegCx10.setStatus("current")
_Mpbc2RUSRCPSeedOutputMinThrdBx10_Type = Integer32
_Mpbc2RUSRCPSeedOutputMinThrdBx10_Object = MibScalar
mpbc2RUSRCPSeedOutputMinThrdBx10 = _Mpbc2RUSRCPSeedOutputMinThrdBx10_Object(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 5, 3, 9),
    _Mpbc2RUSRCPSeedOutputMinThrdBx10_Type()
)
mpbc2RUSRCPSeedOutputMinThrdBx10.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mpbc2RUSRCPSeedOutputMinThrdBx10.setStatus("current")
_Mpbc2RUSRCPSeedOutputMaxThrdBx10_Type = Integer32
_Mpbc2RUSRCPSeedOutputMaxThrdBx10_Object = MibScalar
mpbc2RUSRCPSeedOutputMaxThrdBx10 = _Mpbc2RUSRCPSeedOutputMaxThrdBx10_Object(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 5, 3, 10),
    _Mpbc2RUSRCPSeedOutputMaxThrdBx10_Type()
)
mpbc2RUSRCPSeedOutputMaxThrdBx10.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mpbc2RUSRCPSeedOutputMaxThrdBx10.setStatus("current")
_Mpbc2RUSRCPMainOutputPwrMinThrdBx10_Type = Integer32
_Mpbc2RUSRCPMainOutputPwrMinThrdBx10_Object = MibScalar
mpbc2RUSRCPMainOutputPwrMinThrdBx10 = _Mpbc2RUSRCPMainOutputPwrMinThrdBx10_Object(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 5, 3, 11),
    _Mpbc2RUSRCPMainOutputPwrMinThrdBx10_Type()
)
mpbc2RUSRCPMainOutputPwrMinThrdBx10.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mpbc2RUSRCPMainOutputPwrMinThrdBx10.setStatus("current")
_Mpbc2RUSRCPMainOutputPwrMaxThrdBx10_Type = Integer32
_Mpbc2RUSRCPMainOutputPwrMaxThrdBx10_Object = MibScalar
mpbc2RUSRCPMainOutputPwrMaxThrdBx10 = _Mpbc2RUSRCPMainOutputPwrMaxThrdBx10_Object(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 5, 3, 12),
    _Mpbc2RUSRCPMainOutputPwrMaxThrdBx10_Type()
)
mpbc2RUSRCPMainOutputPwrMaxThrdBx10.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mpbc2RUSRCPMainOutputPwrMaxThrdBx10.setStatus("current")
_Mpbc2RUSRCPSeedOutputMinFautThrmW_Type = Unsigned32
_Mpbc2RUSRCPSeedOutputMinFautThrmW_Object = MibScalar
mpbc2RUSRCPSeedOutputMinFautThrmW = _Mpbc2RUSRCPSeedOutputMinFautThrmW_Object(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 5, 3, 13),
    _Mpbc2RUSRCPSeedOutputMinFautThrmW_Type()
)
mpbc2RUSRCPSeedOutputMinFautThrmW.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpbc2RUSRCPSeedOutputMinFautThrmW.setStatus("current")
_Mpbc2RUSRCPCaseTempMinAlrmThrDegCx10_Type = Integer32
_Mpbc2RUSRCPCaseTempMinAlrmThrDegCx10_Object = MibScalar
mpbc2RUSRCPCaseTempMinAlrmThrDegCx10 = _Mpbc2RUSRCPCaseTempMinAlrmThrDegCx10_Object(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 5, 3, 14),
    _Mpbc2RUSRCPCaseTempMinAlrmThrDegCx10_Type()
)
mpbc2RUSRCPCaseTempMinAlrmThrDegCx10.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mpbc2RUSRCPCaseTempMinAlrmThrDegCx10.setStatus("current")
_Mpbc2RUSRCPCaseTempMaxAlrmThrDegCx10_Type = Integer32
_Mpbc2RUSRCPCaseTempMaxAlrmThrDegCx10_Object = MibScalar
mpbc2RUSRCPCaseTempMaxAlrmThrDegCx10 = _Mpbc2RUSRCPCaseTempMaxAlrmThrDegCx10_Object(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 5, 3, 15),
    _Mpbc2RUSRCPCaseTempMaxAlrmThrDegCx10_Type()
)
mpbc2RUSRCPCaseTempMaxAlrmThrDegCx10.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mpbc2RUSRCPCaseTempMaxAlrmThrDegCx10.setStatus("current")
_Mpbc2RUSRCPMainOutputPwrMinLimdBmx10_Type = Unsigned32
_Mpbc2RUSRCPMainOutputPwrMinLimdBmx10_Object = MibScalar
mpbc2RUSRCPMainOutputPwrMinLimdBmx10 = _Mpbc2RUSRCPMainOutputPwrMinLimdBmx10_Object(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 5, 3, 16),
    _Mpbc2RUSRCPMainOutputPwrMinLimdBmx10_Type()
)
mpbc2RUSRCPMainOutputPwrMinLimdBmx10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpbc2RUSRCPMainOutputPwrMinLimdBmx10.setStatus("current")
_Mpbc2RUSRCPMainOutputPwrMaxLimdBmx10_Type = Unsigned32
_Mpbc2RUSRCPMainOutputPwrMaxLimdBmx10_Object = MibScalar
mpbc2RUSRCPMainOutputPwrMaxLimdBmx10 = _Mpbc2RUSRCPMainOutputPwrMaxLimdBmx10_Object(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 5, 3, 17),
    _Mpbc2RUSRCPMainOutputPwrMaxLimdBmx10_Type()
)
mpbc2RUSRCPMainOutputPwrMaxLimdBmx10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpbc2RUSRCPMainOutputPwrMaxLimdBmx10.setStatus("current")
_Mpbc2RUSRCPSeedOutputPwrMinLimdBmx10_Type = Integer32
_Mpbc2RUSRCPSeedOutputPwrMinLimdBmx10_Object = MibScalar
mpbc2RUSRCPSeedOutputPwrMinLimdBmx10 = _Mpbc2RUSRCPSeedOutputPwrMinLimdBmx10_Object(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 5, 3, 18),
    _Mpbc2RUSRCPSeedOutputPwrMinLimdBmx10_Type()
)
mpbc2RUSRCPSeedOutputPwrMinLimdBmx10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpbc2RUSRCPSeedOutputPwrMinLimdBmx10.setStatus("current")
_Mpbc2RUSRCPSeedOutputPwrMaxLimdBmx10_Type = Integer32
_Mpbc2RUSRCPSeedOutputPwrMaxLimdBmx10_Object = MibScalar
mpbc2RUSRCPSeedOutputPwrMaxLimdBmx10 = _Mpbc2RUSRCPSeedOutputPwrMaxLimdBmx10_Object(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 5, 3, 19),
    _Mpbc2RUSRCPSeedOutputPwrMaxLimdBmx10_Type()
)
mpbc2RUSRCPSeedOutputPwrMaxLimdBmx10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpbc2RUSRCPSeedOutputPwrMaxLimdBmx10.setStatus("current")
_Mpbc2RUSRCPAPLSetThrdBmx10_Type = Integer32
_Mpbc2RUSRCPAPLSetThrdBmx10_Object = MibScalar
mpbc2RUSRCPAPLSetThrdBmx10 = _Mpbc2RUSRCPAPLSetThrdBmx10_Object(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 5, 3, 20),
    _Mpbc2RUSRCPAPLSetThrdBmx10_Type()
)
mpbc2RUSRCPAPLSetThrdBmx10.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mpbc2RUSRCPAPLSetThrdBmx10.setStatus("current")
_Mpbc2RUSRCPAPLClearThrdBmx10_Type = Integer32
_Mpbc2RUSRCPAPLClearThrdBmx10_Object = MibScalar
mpbc2RUSRCPAPLClearThrdBmx10 = _Mpbc2RUSRCPAPLClearThrdBmx10_Object(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 5, 3, 21),
    _Mpbc2RUSRCPAPLClearThrdBmx10_Type()
)
mpbc2RUSRCPAPLClearThrdBmx10.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mpbc2RUSRCPAPLClearThrdBmx10.setStatus("current")
_Mpbc2RUSRCPAPLMainOutputPwrdBmx10_Type = Integer32
_Mpbc2RUSRCPAPLMainOutputPwrdBmx10_Object = MibScalar
mpbc2RUSRCPAPLMainOutputPwrdBmx10 = _Mpbc2RUSRCPAPLMainOutputPwrdBmx10_Object(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 5, 3, 22),
    _Mpbc2RUSRCPAPLMainOutputPwrdBmx10_Type()
)
mpbc2RUSRCPAPLMainOutputPwrdBmx10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpbc2RUSRCPAPLMainOutputPwrdBmx10.setStatus("current")
_Mpbc2RUSRCPOSCMode_Type = Unsigned32
_Mpbc2RUSRCPOSCMode_Object = MibScalar
mpbc2RUSRCPOSCMode = _Mpbc2RUSRCPOSCMode_Object(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 5, 3, 23),
    _Mpbc2RUSRCPOSCMode_Type()
)
mpbc2RUSRCPOSCMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mpbc2RUSRCPOSCMode.setStatus("current")
_Mpbc2RUSRCPSeedFaultDelayms_Type = Unsigned32
_Mpbc2RUSRCPSeedFaultDelayms_Object = MibScalar
mpbc2RUSRCPSeedFaultDelayms = _Mpbc2RUSRCPSeedFaultDelayms_Object(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 5, 3, 24),
    _Mpbc2RUSRCPSeedFaultDelayms_Type()
)
mpbc2RUSRCPSeedFaultDelayms.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpbc2RUSRCPSeedFaultDelayms.setStatus("current")
_Mpbc2RUMLD_ObjectIdentity = ObjectIdentity
mpbc2RUMLD = _Mpbc2RUMLD_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 6)
)
_Mpbc2RUMLDControl_ObjectIdentity = ObjectIdentity
mpbc2RUMLDControl = _Mpbc2RUMLDControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 6, 1)
)


class _Mpbc2RUMLDLaserMode_Type(Integer32):
    """Custom type mpbc2RUMLDLaserMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("laserOff", 0),
          ("laserAPR", 1))
    )


_Mpbc2RUMLDLaserMode_Type.__name__ = "Integer32"
_Mpbc2RUMLDLaserMode_Object = MibScalar
mpbc2RUMLDLaserMode = _Mpbc2RUMLDLaserMode_Object(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 6, 1, 1),
    _Mpbc2RUMLDLaserMode_Type()
)
mpbc2RUMLDLaserMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mpbc2RUMLDLaserMode.setStatus("current")
_Mpbc2RUMLDControlMode_Type = Unsigned32
_Mpbc2RUMLDControlMode_Object = MibScalar
mpbc2RUMLDControlMode = _Mpbc2RUMLDControlMode_Object(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 6, 1, 2),
    _Mpbc2RUMLDControlMode_Type()
)
mpbc2RUMLDControlMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mpbc2RUMLDControlMode.setStatus("current")
_Mpbc2RUMLD1stWLPwrSetPtmW_Type = Unsigned32
_Mpbc2RUMLD1stWLPwrSetPtmW_Object = MibScalar
mpbc2RUMLD1stWLPwrSetPtmW = _Mpbc2RUMLD1stWLPwrSetPtmW_Object(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 6, 1, 3),
    _Mpbc2RUMLD1stWLPwrSetPtmW_Type()
)
mpbc2RUMLD1stWLPwrSetPtmW.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mpbc2RUMLD1stWLPwrSetPtmW.setStatus("current")
_Mpbc2RUMLD2ndWLPwrSetPtmW_Type = Unsigned32
_Mpbc2RUMLD2ndWLPwrSetPtmW_Object = MibScalar
mpbc2RUMLD2ndWLPwrSetPtmW = _Mpbc2RUMLD2ndWLPwrSetPtmW_Object(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 6, 1, 4),
    _Mpbc2RUMLD2ndWLPwrSetPtmW_Type()
)
mpbc2RUMLD2ndWLPwrSetPtmW.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mpbc2RUMLD2ndWLPwrSetPtmW.setStatus("current")
_Mpbc2RUMLDReset_Type = TruthValue
_Mpbc2RUMLDReset_Object = MibScalar
mpbc2RUMLDReset = _Mpbc2RUMLDReset_Object(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 6, 1, 5),
    _Mpbc2RUMLDReset_Type()
)
mpbc2RUMLDReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mpbc2RUMLDReset.setStatus("current")
_Mpbc2RUMLDMonitor_ObjectIdentity = ObjectIdentity
mpbc2RUMLDMonitor = _Mpbc2RUMLDMonitor_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 6, 2)
)
_Mpbc2RUMLDLD1CurmA_Type = Unsigned32
_Mpbc2RUMLDLD1CurmA_Object = MibScalar
mpbc2RUMLDLD1CurmA = _Mpbc2RUMLDLD1CurmA_Object(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 6, 2, 1),
    _Mpbc2RUMLDLD1CurmA_Type()
)
mpbc2RUMLDLD1CurmA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpbc2RUMLDLD1CurmA.setStatus("current")
_Mpbc2RUMLDLD1TempDegCx10_Type = Integer32
_Mpbc2RUMLDLD1TempDegCx10_Object = MibScalar
mpbc2RUMLDLD1TempDegCx10 = _Mpbc2RUMLDLD1TempDegCx10_Object(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 6, 2, 2),
    _Mpbc2RUMLDLD1TempDegCx10_Type()
)
mpbc2RUMLDLD1TempDegCx10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpbc2RUMLDLD1TempDegCx10.setStatus("current")
_Mpbc2RUMLDLD1TECCurmA_Type = Unsigned32
_Mpbc2RUMLDLD1TECCurmA_Object = MibScalar
mpbc2RUMLDLD1TECCurmA = _Mpbc2RUMLDLD1TECCurmA_Object(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 6, 2, 3),
    _Mpbc2RUMLDLD1TECCurmA_Type()
)
mpbc2RUMLDLD1TECCurmA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpbc2RUMLDLD1TECCurmA.setStatus("current")
_Mpbc2RUMLDLD2CurmA_Type = Unsigned32
_Mpbc2RUMLDLD2CurmA_Object = MibScalar
mpbc2RUMLDLD2CurmA = _Mpbc2RUMLDLD2CurmA_Object(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 6, 2, 4),
    _Mpbc2RUMLDLD2CurmA_Type()
)
mpbc2RUMLDLD2CurmA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpbc2RUMLDLD2CurmA.setStatus("current")
_Mpbc2RUMLDLD2TempDegCx10_Type = Integer32
_Mpbc2RUMLDLD2TempDegCx10_Object = MibScalar
mpbc2RUMLDLD2TempDegCx10 = _Mpbc2RUMLDLD2TempDegCx10_Object(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 6, 2, 5),
    _Mpbc2RUMLDLD2TempDegCx10_Type()
)
mpbc2RUMLDLD2TempDegCx10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpbc2RUMLDLD2TempDegCx10.setStatus("current")
_Mpbc2RUMLDLD2TECCurmA_Type = Unsigned32
_Mpbc2RUMLDLD2TECCurmA_Object = MibScalar
mpbc2RUMLDLD2TECCurmA = _Mpbc2RUMLDLD2TECCurmA_Object(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 6, 2, 6),
    _Mpbc2RUMLDLD2TECCurmA_Type()
)
mpbc2RUMLDLD2TECCurmA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpbc2RUMLDLD2TECCurmA.setStatus("current")
_Mpbc2RUMLDCaseTempDegCx10_Type = Integer32
_Mpbc2RUMLDCaseTempDegCx10_Object = MibScalar
mpbc2RUMLDCaseTempDegCx10 = _Mpbc2RUMLDCaseTempDegCx10_Object(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 6, 2, 7),
    _Mpbc2RUMLDCaseTempDegCx10_Type()
)
mpbc2RUMLDCaseTempDegCx10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpbc2RUMLDCaseTempDegCx10.setStatus("current")
_Mpbc2RUMLDMon1stWLOutputPwrmWx10_Type = Unsigned32
_Mpbc2RUMLDMon1stWLOutputPwrmWx10_Object = MibScalar
mpbc2RUMLDMon1stWLOutputPwrmWx10 = _Mpbc2RUMLDMon1stWLOutputPwrmWx10_Object(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 6, 2, 8),
    _Mpbc2RUMLDMon1stWLOutputPwrmWx10_Type()
)
mpbc2RUMLDMon1stWLOutputPwrmWx10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpbc2RUMLDMon1stWLOutputPwrmWx10.setStatus("current")
_Mpbc2RUMLDMon2ndWLOutputPwrmWx10_Type = Unsigned32
_Mpbc2RUMLDMon2ndWLOutputPwrmWx10_Object = MibScalar
mpbc2RUMLDMon2ndWLOutputPwrmWx10 = _Mpbc2RUMLDMon2ndWLOutputPwrmWx10_Object(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 6, 2, 9),
    _Mpbc2RUMLDMon2ndWLOutputPwrmWx10_Type()
)
mpbc2RUMLDMon2ndWLOutputPwrmWx10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpbc2RUMLDMon2ndWLOutputPwrmWx10.setStatus("current")
_Mpbc2RUMLDInputPwrmWx100_Type = Unsigned32
_Mpbc2RUMLDInputPwrmWx100_Object = MibScalar
mpbc2RUMLDInputPwrmWx100 = _Mpbc2RUMLDInputPwrmWx100_Object(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 6, 2, 10),
    _Mpbc2RUMLDInputPwrmWx100_Type()
)
mpbc2RUMLDInputPwrmWx100.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpbc2RUMLDInputPwrmWx100.setStatus("current")


class _Mpbc2RUMLDMonLaserState_Type(Integer32):
    """Custom type mpbc2RUMLDMonLaserState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              10)
        )
    )
    namedValues = NamedValues(
        *(("laserOff", 0),
          ("laserNormal", 1),
          ("laserALS", 2),
          ("laserALS100", 3),
          ("laserOn", 10))
    )


_Mpbc2RUMLDMonLaserState_Type.__name__ = "Integer32"
_Mpbc2RUMLDMonLaserState_Object = MibScalar
mpbc2RUMLDMonLaserState = _Mpbc2RUMLDMonLaserState_Object(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 6, 2, 11),
    _Mpbc2RUMLDMonLaserState_Type()
)
mpbc2RUMLDMonLaserState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpbc2RUMLDMonLaserState.setStatus("current")


class _Mpbc2RUMLDMonLaserMode_Type(Integer32):
    """Custom type mpbc2RUMLDMonLaserMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              10)
        )
    )
    namedValues = NamedValues(
        *(("laserOff", 0),
          ("laserAPR", 1),
          ("laserOn", 10))
    )


_Mpbc2RUMLDMonLaserMode_Type.__name__ = "Integer32"
_Mpbc2RUMLDMonLaserMode_Object = MibScalar
mpbc2RUMLDMonLaserMode = _Mpbc2RUMLDMonLaserMode_Object(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 6, 2, 12),
    _Mpbc2RUMLDMonLaserMode_Type()
)
mpbc2RUMLDMonLaserMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpbc2RUMLDMonLaserMode.setStatus("current")
_Mpbc2RUMLDMonControlMode_Type = Unsigned32
_Mpbc2RUMLDMonControlMode_Object = MibScalar
mpbc2RUMLDMonControlMode = _Mpbc2RUMLDMonControlMode_Object(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 6, 2, 13),
    _Mpbc2RUMLDMonControlMode_Type()
)
mpbc2RUMLDMonControlMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpbc2RUMLDMonControlMode.setStatus("current")
_Mpbc2RUMLDDisableInputState_Type = Unsigned32
_Mpbc2RUMLDDisableInputState_Object = MibScalar
mpbc2RUMLDDisableInputState = _Mpbc2RUMLDDisableInputState_Object(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 6, 2, 14),
    _Mpbc2RUMLDDisableInputState_Type()
)
mpbc2RUMLDDisableInputState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpbc2RUMLDDisableInputState.setStatus("current")


class _Mpbc2RUMLDUnitState_Type(Integer32):
    """Custom type mpbc2RUMLDUnitState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("stateInit", 0),
          ("stateNormal", 1),
          ("stateFault", 2))
    )


_Mpbc2RUMLDUnitState_Type.__name__ = "Integer32"
_Mpbc2RUMLDUnitState_Object = MibScalar
mpbc2RUMLDUnitState = _Mpbc2RUMLDUnitState_Object(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 6, 2, 15),
    _Mpbc2RUMLDUnitState_Type()
)
mpbc2RUMLDUnitState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpbc2RUMLDUnitState.setStatus("current")


class _Mpbc2RUMLDOSCRx1574Tone_Type(Integer32):
    """Custom type mpbc2RUMLDOSCRx1574Tone based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("noTone", 0),
          ("tone1", 1),
          ("tone2", 2),
          ("tone1plus2", 3))
    )


_Mpbc2RUMLDOSCRx1574Tone_Type.__name__ = "Integer32"
_Mpbc2RUMLDOSCRx1574Tone_Object = MibScalar
mpbc2RUMLDOSCRx1574Tone = _Mpbc2RUMLDOSCRx1574Tone_Object(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 6, 2, 16),
    _Mpbc2RUMLDOSCRx1574Tone_Type()
)
mpbc2RUMLDOSCRx1574Tone.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpbc2RUMLDOSCRx1574Tone.setStatus("current")
_Mpbc2RUMLDOSCTempdegCx10_Type = Integer32
_Mpbc2RUMLDOSCTempdegCx10_Object = MibScalar
mpbc2RUMLDOSCTempdegCx10 = _Mpbc2RUMLDOSCTempdegCx10_Object(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 6, 2, 17),
    _Mpbc2RUMLDOSCTempdegCx10_Type()
)
mpbc2RUMLDOSCTempdegCx10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpbc2RUMLDOSCTempdegCx10.setStatus("current")


class _Mpbc2RUMLDOSCTxTone_Type(Integer32):
    """Custom type mpbc2RUMLDOSCTxTone based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("tone1", 1),
          ("tone2", 2))
    )


_Mpbc2RUMLDOSCTxTone_Type.__name__ = "Integer32"
_Mpbc2RUMLDOSCTxTone_Object = MibScalar
mpbc2RUMLDOSCTxTone = _Mpbc2RUMLDOSCTxTone_Object(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 6, 2, 18),
    _Mpbc2RUMLDOSCTxTone_Type()
)
mpbc2RUMLDOSCTxTone.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpbc2RUMLDOSCTxTone.setStatus("current")
_Mpbc2RUMLDOSCTxPwrmWx100_Type = Integer32
_Mpbc2RUMLDOSCTxPwrmWx100_Object = MibScalar
mpbc2RUMLDOSCTxPwrmWx100 = _Mpbc2RUMLDOSCTxPwrmWx100_Object(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 6, 2, 19),
    _Mpbc2RUMLDOSCTxPwrmWx100_Type()
)
mpbc2RUMLDOSCTxPwrmWx100.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpbc2RUMLDOSCTxPwrmWx100.setStatus("current")


class _Mpbc2RUMLDOSCRx1610Tone_Type(Integer32):
    """Custom type mpbc2RUMLDOSCRx1610Tone based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("noTone", 0),
          ("tone1", 1),
          ("tone2", 2),
          ("tone1plus2", 3))
    )


_Mpbc2RUMLDOSCRx1610Tone_Type.__name__ = "Integer32"
_Mpbc2RUMLDOSCRx1610Tone_Object = MibScalar
mpbc2RUMLDOSCRx1610Tone = _Mpbc2RUMLDOSCRx1610Tone_Object(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 6, 2, 20),
    _Mpbc2RUMLDOSCRx1610Tone_Type()
)
mpbc2RUMLDOSCRx1610Tone.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpbc2RUMLDOSCRx1610Tone.setStatus("current")
_Mpbc2RUMLDConfiguration_ObjectIdentity = ObjectIdentity
mpbc2RUMLDConfiguration = _Mpbc2RUMLDConfiguration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 6, 3)
)
_Mpbc2RUMLDLD1CurMinThrmA_Type = Unsigned32
_Mpbc2RUMLDLD1CurMinThrmA_Object = MibScalar
mpbc2RUMLDLD1CurMinThrmA = _Mpbc2RUMLDLD1CurMinThrmA_Object(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 6, 3, 1),
    _Mpbc2RUMLDLD1CurMinThrmA_Type()
)
mpbc2RUMLDLD1CurMinThrmA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpbc2RUMLDLD1CurMinThrmA.setStatus("current")
_Mpbc2RUMLDLD1CurMaxThrmA_Type = Unsigned32
_Mpbc2RUMLDLD1CurMaxThrmA_Object = MibScalar
mpbc2RUMLDLD1CurMaxThrmA = _Mpbc2RUMLDLD1CurMaxThrmA_Object(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 6, 3, 2),
    _Mpbc2RUMLDLD1CurMaxThrmA_Type()
)
mpbc2RUMLDLD1CurMaxThrmA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpbc2RUMLDLD1CurMaxThrmA.setStatus("current")
_Mpbc2RUMLDLD2CurMinThrmA_Type = Unsigned32
_Mpbc2RUMLDLD2CurMinThrmA_Object = MibScalar
mpbc2RUMLDLD2CurMinThrmA = _Mpbc2RUMLDLD2CurMinThrmA_Object(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 6, 3, 3),
    _Mpbc2RUMLDLD2CurMinThrmA_Type()
)
mpbc2RUMLDLD2CurMinThrmA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpbc2RUMLDLD2CurMinThrmA.setStatus("current")
_Mpbc2RUMLDLD2CurMaxThrmA_Type = Unsigned32
_Mpbc2RUMLDLD2CurMaxThrmA_Object = MibScalar
mpbc2RUMLDLD2CurMaxThrmA = _Mpbc2RUMLDLD2CurMaxThrmA_Object(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 6, 3, 4),
    _Mpbc2RUMLDLD2CurMaxThrmA_Type()
)
mpbc2RUMLDLD2CurMaxThrmA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpbc2RUMLDLD2CurMaxThrmA.setStatus("current")
_Mpbc2RUMLDCaseTempMinSetThrDegCx10_Type = Integer32
_Mpbc2RUMLDCaseTempMinSetThrDegCx10_Object = MibScalar
mpbc2RUMLDCaseTempMinSetThrDegCx10 = _Mpbc2RUMLDCaseTempMinSetThrDegCx10_Object(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 6, 3, 5),
    _Mpbc2RUMLDCaseTempMinSetThrDegCx10_Type()
)
mpbc2RUMLDCaseTempMinSetThrDegCx10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpbc2RUMLDCaseTempMinSetThrDegCx10.setStatus("current")
_Mpbc2RUMLDCaseTempMinClearThrDegCx10_Type = Integer32
_Mpbc2RUMLDCaseTempMinClearThrDegCx10_Object = MibScalar
mpbc2RUMLDCaseTempMinClearThrDegCx10 = _Mpbc2RUMLDCaseTempMinClearThrDegCx10_Object(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 6, 3, 6),
    _Mpbc2RUMLDCaseTempMinClearThrDegCx10_Type()
)
mpbc2RUMLDCaseTempMinClearThrDegCx10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpbc2RUMLDCaseTempMinClearThrDegCx10.setStatus("current")
_Mpbc2RUMLDCaseTempMaxSetThrDegCx10_Type = Integer32
_Mpbc2RUMLDCaseTempMaxSetThrDegCx10_Object = MibScalar
mpbc2RUMLDCaseTempMaxSetThrDegCx10 = _Mpbc2RUMLDCaseTempMaxSetThrDegCx10_Object(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 6, 3, 7),
    _Mpbc2RUMLDCaseTempMaxSetThrDegCx10_Type()
)
mpbc2RUMLDCaseTempMaxSetThrDegCx10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpbc2RUMLDCaseTempMaxSetThrDegCx10.setStatus("current")
_Mpbc2RUMLDCaseTempMaxClearThrDegCx10_Type = Integer32
_Mpbc2RUMLDCaseTempMaxClearThrDegCx10_Object = MibScalar
mpbc2RUMLDCaseTempMaxClearThrDegCx10 = _Mpbc2RUMLDCaseTempMaxClearThrDegCx10_Object(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 6, 3, 8),
    _Mpbc2RUMLDCaseTempMaxClearThrDegCx10_Type()
)
mpbc2RUMLDCaseTempMaxClearThrDegCx10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpbc2RUMLDCaseTempMaxClearThrDegCx10.setStatus("current")
_Mpbc2RUMLDCaseTempMinAlrmThrDegCx10_Type = Integer32
_Mpbc2RUMLDCaseTempMinAlrmThrDegCx10_Object = MibScalar
mpbc2RUMLDCaseTempMinAlrmThrDegCx10 = _Mpbc2RUMLDCaseTempMinAlrmThrDegCx10_Object(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 6, 3, 9),
    _Mpbc2RUMLDCaseTempMinAlrmThrDegCx10_Type()
)
mpbc2RUMLDCaseTempMinAlrmThrDegCx10.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mpbc2RUMLDCaseTempMinAlrmThrDegCx10.setStatus("current")
_Mpbc2RUMLDCaseTempMaxAlrmThrDegCx10_Type = Integer32
_Mpbc2RUMLDCaseTempMaxAlrmThrDegCx10_Object = MibScalar
mpbc2RUMLDCaseTempMaxAlrmThrDegCx10 = _Mpbc2RUMLDCaseTempMaxAlrmThrDegCx10_Object(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 6, 3, 10),
    _Mpbc2RUMLDCaseTempMaxAlrmThrDegCx10_Type()
)
mpbc2RUMLDCaseTempMaxAlrmThrDegCx10.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mpbc2RUMLDCaseTempMaxAlrmThrDegCx10.setStatus("current")
_Mpbc2RUMLD1stWLOutputPwrMinThrdBx10_Type = Integer32
_Mpbc2RUMLD1stWLOutputPwrMinThrdBx10_Object = MibScalar
mpbc2RUMLD1stWLOutputPwrMinThrdBx10 = _Mpbc2RUMLD1stWLOutputPwrMinThrdBx10_Object(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 6, 3, 11),
    _Mpbc2RUMLD1stWLOutputPwrMinThrdBx10_Type()
)
mpbc2RUMLD1stWLOutputPwrMinThrdBx10.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mpbc2RUMLD1stWLOutputPwrMinThrdBx10.setStatus("current")
_Mpbc2RUMLD1stWLOutputPwrMaxThrdBx10_Type = Integer32
_Mpbc2RUMLD1stWLOutputPwrMaxThrdBx10_Object = MibScalar
mpbc2RUMLD1stWLOutputPwrMaxThrdBx10 = _Mpbc2RUMLD1stWLOutputPwrMaxThrdBx10_Object(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 6, 3, 12),
    _Mpbc2RUMLD1stWLOutputPwrMaxThrdBx10_Type()
)
mpbc2RUMLD1stWLOutputPwrMaxThrdBx10.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mpbc2RUMLD1stWLOutputPwrMaxThrdBx10.setStatus("current")
_Mpbc2RUMLD2ndWLOutputPwrMinThrdBx10_Type = Integer32
_Mpbc2RUMLD2ndWLOutputPwrMinThrdBx10_Object = MibScalar
mpbc2RUMLD2ndWLOutputPwrMinThrdBx10 = _Mpbc2RUMLD2ndWLOutputPwrMinThrdBx10_Object(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 6, 3, 13),
    _Mpbc2RUMLD2ndWLOutputPwrMinThrdBx10_Type()
)
mpbc2RUMLD2ndWLOutputPwrMinThrdBx10.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mpbc2RUMLD2ndWLOutputPwrMinThrdBx10.setStatus("current")
_Mpbc2RUMLD2ndWLOutputPwrMaxThrdBx10_Type = Integer32
_Mpbc2RUMLD2ndWLOutputPwrMaxThrdBx10_Object = MibScalar
mpbc2RUMLD2ndWLOutputPwrMaxThrdBx10 = _Mpbc2RUMLD2ndWLOutputPwrMaxThrdBx10_Object(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 6, 3, 14),
    _Mpbc2RUMLD2ndWLOutputPwrMaxThrdBx10_Type()
)
mpbc2RUMLD2ndWLOutputPwrMaxThrdBx10.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mpbc2RUMLD2ndWLOutputPwrMaxThrdBx10.setStatus("current")
_Mpbc2RUMLD1stWLOutputPwrMinLimdBmx10_Type = Integer32
_Mpbc2RUMLD1stWLOutputPwrMinLimdBmx10_Object = MibScalar
mpbc2RUMLD1stWLOutputPwrMinLimdBmx10 = _Mpbc2RUMLD1stWLOutputPwrMinLimdBmx10_Object(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 6, 3, 15),
    _Mpbc2RUMLD1stWLOutputPwrMinLimdBmx10_Type()
)
mpbc2RUMLD1stWLOutputPwrMinLimdBmx10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpbc2RUMLD1stWLOutputPwrMinLimdBmx10.setStatus("current")
_Mpbc2RUMLD1stWLOutputPwrMaxLimdBmx10_Type = Integer32
_Mpbc2RUMLD1stWLOutputPwrMaxLimdBmx10_Object = MibScalar
mpbc2RUMLD1stWLOutputPwrMaxLimdBmx10 = _Mpbc2RUMLD1stWLOutputPwrMaxLimdBmx10_Object(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 6, 3, 16),
    _Mpbc2RUMLD1stWLOutputPwrMaxLimdBmx10_Type()
)
mpbc2RUMLD1stWLOutputPwrMaxLimdBmx10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpbc2RUMLD1stWLOutputPwrMaxLimdBmx10.setStatus("current")
_Mpbc2RUMLD2ndWLOutputPwrMinLimdBmx10_Type = Integer32
_Mpbc2RUMLD2ndWLOutputPwrMinLimdBmx10_Object = MibScalar
mpbc2RUMLD2ndWLOutputPwrMinLimdBmx10 = _Mpbc2RUMLD2ndWLOutputPwrMinLimdBmx10_Object(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 6, 3, 17),
    _Mpbc2RUMLD2ndWLOutputPwrMinLimdBmx10_Type()
)
mpbc2RUMLD2ndWLOutputPwrMinLimdBmx10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpbc2RUMLD2ndWLOutputPwrMinLimdBmx10.setStatus("current")
_Mpbc2RUMLD2ndWLOutputPwrMaxLimdBmx10_Type = Integer32
_Mpbc2RUMLD2ndWLOutputPwrMaxLimdBmx10_Object = MibScalar
mpbc2RUMLD2ndWLOutputPwrMaxLimdBmx10 = _Mpbc2RUMLD2ndWLOutputPwrMaxLimdBmx10_Object(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 6, 3, 18),
    _Mpbc2RUMLD2ndWLOutputPwrMaxLimdBmx10_Type()
)
mpbc2RUMLD2ndWLOutputPwrMaxLimdBmx10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpbc2RUMLD2ndWLOutputPwrMaxLimdBmx10.setStatus("current")
_Mpbc2RUMLDOSCMode_Type = Unsigned32
_Mpbc2RUMLDOSCMode_Object = MibScalar
mpbc2RUMLDOSCMode = _Mpbc2RUMLDOSCMode_Object(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 6, 3, 19),
    _Mpbc2RUMLDOSCMode_Type()
)
mpbc2RUMLDOSCMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mpbc2RUMLDOSCMode.setStatus("current")
_Mpbc2RUPY_ObjectIdentity = ObjectIdentity
mpbc2RUPY = _Mpbc2RUPY_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 7)
)
_Mpbc2RUPYControl_ObjectIdentity = ObjectIdentity
mpbc2RUPYControl = _Mpbc2RUPYControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 7, 1)
)


class _Mpbc2RUPYLaserMode_Type(Integer32):
    """Custom type mpbc2RUPYLaserMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("laserOff", 0),
          ("laserAPR", 1))
    )


_Mpbc2RUPYLaserMode_Type.__name__ = "Integer32"
_Mpbc2RUPYLaserMode_Object = MibScalar
mpbc2RUPYLaserMode = _Mpbc2RUPYLaserMode_Object(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 7, 1, 1),
    _Mpbc2RUPYLaserMode_Type()
)
mpbc2RUPYLaserMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mpbc2RUPYLaserMode.setStatus("current")
_Mpbc2RUPYControlMode_Type = Unsigned32
_Mpbc2RUPYControlMode_Object = MibScalar
mpbc2RUPYControlMode = _Mpbc2RUPYControlMode_Object(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 7, 1, 2),
    _Mpbc2RUPYControlMode_Type()
)
mpbc2RUPYControlMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mpbc2RUPYControlMode.setStatus("current")
_Mpbc2RUPYPreAmpSetPtmW_Type = Unsigned32
_Mpbc2RUPYPreAmpSetPtmW_Object = MibScalar
mpbc2RUPYPreAmpSetPtmW = _Mpbc2RUPYPreAmpSetPtmW_Object(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 7, 1, 3),
    _Mpbc2RUPYPreAmpSetPtmW_Type()
)
mpbc2RUPYPreAmpSetPtmW.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpbc2RUPYPreAmpSetPtmW.setStatus("current")
_Mpbc2RUPYPwrSetPtmW_Type = Unsigned32
_Mpbc2RUPYPwrSetPtmW_Object = MibScalar
mpbc2RUPYPwrSetPtmW = _Mpbc2RUPYPwrSetPtmW_Object(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 7, 1, 4),
    _Mpbc2RUPYPwrSetPtmW_Type()
)
mpbc2RUPYPwrSetPtmW.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mpbc2RUPYPwrSetPtmW.setStatus("current")
_Mpbc2RUPYGainSetPtdBx10_Type = Integer32
_Mpbc2RUPYGainSetPtdBx10_Object = MibScalar
mpbc2RUPYGainSetPtdBx10 = _Mpbc2RUPYGainSetPtdBx10_Object(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 7, 1, 5),
    _Mpbc2RUPYGainSetPtdBx10_Type()
)
mpbc2RUPYGainSetPtdBx10.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mpbc2RUPYGainSetPtdBx10.setStatus("current")
_Mpbc2RUPYVoaSetPtdBx10_Type = Integer32
_Mpbc2RUPYVoaSetPtdBx10_Object = MibScalar
mpbc2RUPYVoaSetPtdBx10 = _Mpbc2RUPYVoaSetPtdBx10_Object(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 7, 1, 6),
    _Mpbc2RUPYVoaSetPtdBx10_Type()
)
mpbc2RUPYVoaSetPtdBx10.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mpbc2RUPYVoaSetPtdBx10.setStatus("current")
_Mpbc2RUPYReset_Type = TruthValue
_Mpbc2RUPYReset_Object = MibScalar
mpbc2RUPYReset = _Mpbc2RUPYReset_Object(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 7, 1, 7),
    _Mpbc2RUPYReset_Type()
)
mpbc2RUPYReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mpbc2RUPYReset.setStatus("current")
_Mpbc2RUPYMonitor_ObjectIdentity = ObjectIdentity
mpbc2RUPYMonitor = _Mpbc2RUPYMonitor_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 7, 2)
)
_Mpbc2RUPYLD1CurmA_Type = Unsigned32
_Mpbc2RUPYLD1CurmA_Object = MibScalar
mpbc2RUPYLD1CurmA = _Mpbc2RUPYLD1CurmA_Object(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 7, 2, 1),
    _Mpbc2RUPYLD1CurmA_Type()
)
mpbc2RUPYLD1CurmA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpbc2RUPYLD1CurmA.setStatus("current")
_Mpbc2RUPYLD1TempDegCx10_Type = Integer32
_Mpbc2RUPYLD1TempDegCx10_Object = MibScalar
mpbc2RUPYLD1TempDegCx10 = _Mpbc2RUPYLD1TempDegCx10_Object(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 7, 2, 2),
    _Mpbc2RUPYLD1TempDegCx10_Type()
)
mpbc2RUPYLD1TempDegCx10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpbc2RUPYLD1TempDegCx10.setStatus("current")
_Mpbc2RUPYLD1TECCurmA_Type = Unsigned32
_Mpbc2RUPYLD1TECCurmA_Object = MibScalar
mpbc2RUPYLD1TECCurmA = _Mpbc2RUPYLD1TECCurmA_Object(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 7, 2, 3),
    _Mpbc2RUPYLD1TECCurmA_Type()
)
mpbc2RUPYLD1TECCurmA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpbc2RUPYLD1TECCurmA.setStatus("current")
_Mpbc2RUPYLD2CurmA_Type = Unsigned32
_Mpbc2RUPYLD2CurmA_Object = MibScalar
mpbc2RUPYLD2CurmA = _Mpbc2RUPYLD2CurmA_Object(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 7, 2, 4),
    _Mpbc2RUPYLD2CurmA_Type()
)
mpbc2RUPYLD2CurmA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpbc2RUPYLD2CurmA.setStatus("current")
_Mpbc2RUPYCaseTempDegCx10_Type = Integer32
_Mpbc2RUPYCaseTempDegCx10_Object = MibScalar
mpbc2RUPYCaseTempDegCx10 = _Mpbc2RUPYCaseTempDegCx10_Object(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 7, 2, 5),
    _Mpbc2RUPYCaseTempDegCx10_Type()
)
mpbc2RUPYCaseTempDegCx10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpbc2RUPYCaseTempDegCx10.setStatus("current")
_Mpbc2RUPYMonPreAmpPumpPwrmWx10_Type = Unsigned32
_Mpbc2RUPYMonPreAmpPumpPwrmWx10_Object = MibScalar
mpbc2RUPYMonPreAmpPumpPwrmWx10 = _Mpbc2RUPYMonPreAmpPumpPwrmWx10_Object(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 7, 2, 6),
    _Mpbc2RUPYMonPreAmpPumpPwrmWx10_Type()
)
mpbc2RUPYMonPreAmpPumpPwrmWx10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpbc2RUPYMonPreAmpPumpPwrmWx10.setStatus("current")
_Mpbc2RUPYMainOutputPwrmWx10_Type = Unsigned32
_Mpbc2RUPYMainOutputPwrmWx10_Object = MibScalar
mpbc2RUPYMainOutputPwrmWx10 = _Mpbc2RUPYMainOutputPwrmWx10_Object(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 7, 2, 7),
    _Mpbc2RUPYMainOutputPwrmWx10_Type()
)
mpbc2RUPYMainOutputPwrmWx10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpbc2RUPYMainOutputPwrmWx10.setStatus("current")
_Mpbc2RUPYGaindBx10_Type = Integer32
_Mpbc2RUPYGaindBx10_Object = MibScalar
mpbc2RUPYGaindBx10 = _Mpbc2RUPYGaindBx10_Object(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 7, 2, 8),
    _Mpbc2RUPYGaindBx10_Type()
)
mpbc2RUPYGaindBx10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpbc2RUPYGaindBx10.setStatus("current")
_Mpbc2RUPYInputPwrmWx100_Type = Unsigned32
_Mpbc2RUPYInputPwrmWx100_Object = MibScalar
mpbc2RUPYInputPwrmWx100 = _Mpbc2RUPYInputPwrmWx100_Object(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 7, 2, 9),
    _Mpbc2RUPYInputPwrmWx100_Type()
)
mpbc2RUPYInputPwrmWx100.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpbc2RUPYInputPwrmWx100.setStatus("current")
_Mpbc2RUPYBackReflPwrmWx100_Type = Unsigned32
_Mpbc2RUPYBackReflPwrmWx100_Object = MibScalar
mpbc2RUPYBackReflPwrmWx100 = _Mpbc2RUPYBackReflPwrmWx100_Object(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 7, 2, 10),
    _Mpbc2RUPYBackReflPwrmWx100_Type()
)
mpbc2RUPYBackReflPwrmWx100.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpbc2RUPYBackReflPwrmWx100.setStatus("current")


class _Mpbc2RUPYMonLaserState_Type(Integer32):
    """Custom type mpbc2RUPYMonLaserState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              10)
        )
    )
    namedValues = NamedValues(
        *(("laserOff", 0),
          ("laserNormal", 1),
          ("laserALS", 2),
          ("laserALS100", 3),
          ("laserOn", 10))
    )


_Mpbc2RUPYMonLaserState_Type.__name__ = "Integer32"
_Mpbc2RUPYMonLaserState_Object = MibScalar
mpbc2RUPYMonLaserState = _Mpbc2RUPYMonLaserState_Object(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 7, 2, 11),
    _Mpbc2RUPYMonLaserState_Type()
)
mpbc2RUPYMonLaserState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpbc2RUPYMonLaserState.setStatus("current")


class _Mpbc2RUPYMonLaserMode_Type(Integer32):
    """Custom type mpbc2RUPYMonLaserMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              10)
        )
    )
    namedValues = NamedValues(
        *(("laserOff", 0),
          ("laserAPR", 1),
          ("laserOn", 10))
    )


_Mpbc2RUPYMonLaserMode_Type.__name__ = "Integer32"
_Mpbc2RUPYMonLaserMode_Object = MibScalar
mpbc2RUPYMonLaserMode = _Mpbc2RUPYMonLaserMode_Object(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 7, 2, 12),
    _Mpbc2RUPYMonLaserMode_Type()
)
mpbc2RUPYMonLaserMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpbc2RUPYMonLaserMode.setStatus("current")
_Mpbc2RUPYMonControlMode_Type = Unsigned32
_Mpbc2RUPYMonControlMode_Object = MibScalar
mpbc2RUPYMonControlMode = _Mpbc2RUPYMonControlMode_Object(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 7, 2, 13),
    _Mpbc2RUPYMonControlMode_Type()
)
mpbc2RUPYMonControlMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpbc2RUPYMonControlMode.setStatus("current")
_Mpbc2RUPYDisableInputState_Type = Unsigned32
_Mpbc2RUPYDisableInputState_Object = MibScalar
mpbc2RUPYDisableInputState = _Mpbc2RUPYDisableInputState_Object(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 7, 2, 14),
    _Mpbc2RUPYDisableInputState_Type()
)
mpbc2RUPYDisableInputState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpbc2RUPYDisableInputState.setStatus("current")


class _Mpbc2RUPYUnitState_Type(Integer32):
    """Custom type mpbc2RUPYUnitState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("stateInit", 0),
          ("stateNormal", 1),
          ("stateFault", 2))
    )


_Mpbc2RUPYUnitState_Type.__name__ = "Integer32"
_Mpbc2RUPYUnitState_Object = MibScalar
mpbc2RUPYUnitState = _Mpbc2RUPYUnitState_Object(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 7, 2, 15),
    _Mpbc2RUPYUnitState_Type()
)
mpbc2RUPYUnitState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpbc2RUPYUnitState.setStatus("current")


class _Mpbc2RUPYOSCRxTone_Type(Integer32):
    """Custom type mpbc2RUPYOSCRxTone based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("noTone", 0),
          ("tone1", 1),
          ("tone2", 2),
          ("tone1plus2", 3))
    )


_Mpbc2RUPYOSCRxTone_Type.__name__ = "Integer32"
_Mpbc2RUPYOSCRxTone_Object = MibScalar
mpbc2RUPYOSCRxTone = _Mpbc2RUPYOSCRxTone_Object(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 7, 2, 16),
    _Mpbc2RUPYOSCRxTone_Type()
)
mpbc2RUPYOSCRxTone.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpbc2RUPYOSCRxTone.setStatus("current")
_Mpbc2RUPYOSCTempDegCx10_Type = Integer32
_Mpbc2RUPYOSCTempDegCx10_Object = MibScalar
mpbc2RUPYOSCTempDegCx10 = _Mpbc2RUPYOSCTempDegCx10_Object(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 7, 2, 17),
    _Mpbc2RUPYOSCTempDegCx10_Type()
)
mpbc2RUPYOSCTempDegCx10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpbc2RUPYOSCTempDegCx10.setStatus("current")


class _Mpbc2RUPYOSCTxTone_Type(Integer32):
    """Custom type mpbc2RUPYOSCTxTone based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("tone1", 1),
          ("tone2", 2))
    )


_Mpbc2RUPYOSCTxTone_Type.__name__ = "Integer32"
_Mpbc2RUPYOSCTxTone_Object = MibScalar
mpbc2RUPYOSCTxTone = _Mpbc2RUPYOSCTxTone_Object(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 7, 2, 18),
    _Mpbc2RUPYOSCTxTone_Type()
)
mpbc2RUPYOSCTxTone.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpbc2RUPYOSCTxTone.setStatus("current")
_Mpbc2RUPYOSCTxPwrmWx100_Type = Integer32
_Mpbc2RUPYOSCTxPwrmWx100_Object = MibScalar
mpbc2RUPYOSCTxPwrmWx100 = _Mpbc2RUPYOSCTxPwrmWx100_Object(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 7, 2, 19),
    _Mpbc2RUPYOSCTxPwrmWx100_Type()
)
mpbc2RUPYOSCTxPwrmWx100.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpbc2RUPYOSCTxPwrmWx100.setStatus("current")


class _Mpbc2RUPYOSCRx1610Tone_Type(Integer32):
    """Custom type mpbc2RUPYOSCRx1610Tone based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("noTone", 0),
          ("tone1", 1),
          ("tone2", 2),
          ("tone1plus2", 3))
    )


_Mpbc2RUPYOSCRx1610Tone_Type.__name__ = "Integer32"
_Mpbc2RUPYOSCRx1610Tone_Object = MibScalar
mpbc2RUPYOSCRx1610Tone = _Mpbc2RUPYOSCRx1610Tone_Object(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 7, 2, 20),
    _Mpbc2RUPYOSCRx1610Tone_Type()
)
mpbc2RUPYOSCRx1610Tone.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpbc2RUPYOSCRx1610Tone.setStatus("current")
_Mpbc2RUPYVOASettingdBx10_Type = Integer32
_Mpbc2RUPYVOASettingdBx10_Object = MibScalar
mpbc2RUPYVOASettingdBx10 = _Mpbc2RUPYVOASettingdBx10_Object(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 7, 2, 21),
    _Mpbc2RUPYVOASettingdBx10_Type()
)
mpbc2RUPYVOASettingdBx10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpbc2RUPYVOASettingdBx10.setStatus("current")
_Mpbc2RUPYConfiguration_ObjectIdentity = ObjectIdentity
mpbc2RUPYConfiguration = _Mpbc2RUPYConfiguration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 7, 3)
)
_Mpbc2RUPYLD1CurMinThrmA_Type = Unsigned32
_Mpbc2RUPYLD1CurMinThrmA_Object = MibScalar
mpbc2RUPYLD1CurMinThrmA = _Mpbc2RUPYLD1CurMinThrmA_Object(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 7, 3, 1),
    _Mpbc2RUPYLD1CurMinThrmA_Type()
)
mpbc2RUPYLD1CurMinThrmA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpbc2RUPYLD1CurMinThrmA.setStatus("current")
_Mpbc2RUPYLD1CurMaxThrmA_Type = Unsigned32
_Mpbc2RUPYLD1CurMaxThrmA_Object = MibScalar
mpbc2RUPYLD1CurMaxThrmA = _Mpbc2RUPYLD1CurMaxThrmA_Object(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 7, 3, 2),
    _Mpbc2RUPYLD1CurMaxThrmA_Type()
)
mpbc2RUPYLD1CurMaxThrmA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpbc2RUPYLD1CurMaxThrmA.setStatus("current")
_Mpbc2RUPYLD2CurMinThrmA_Type = Unsigned32
_Mpbc2RUPYLD2CurMinThrmA_Object = MibScalar
mpbc2RUPYLD2CurMinThrmA = _Mpbc2RUPYLD2CurMinThrmA_Object(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 7, 3, 3),
    _Mpbc2RUPYLD2CurMinThrmA_Type()
)
mpbc2RUPYLD2CurMinThrmA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpbc2RUPYLD2CurMinThrmA.setStatus("current")
_Mpbc2RUPYLD2CurMaxThrmA_Type = Unsigned32
_Mpbc2RUPYLD2CurMaxThrmA_Object = MibScalar
mpbc2RUPYLD2CurMaxThrmA = _Mpbc2RUPYLD2CurMaxThrmA_Object(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 7, 3, 4),
    _Mpbc2RUPYLD2CurMaxThrmA_Type()
)
mpbc2RUPYLD2CurMaxThrmA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpbc2RUPYLD2CurMaxThrmA.setStatus("current")
_Mpbc2RUPYCaseTempMinSetThrDegCx10_Type = Integer32
_Mpbc2RUPYCaseTempMinSetThrDegCx10_Object = MibScalar
mpbc2RUPYCaseTempMinSetThrDegCx10 = _Mpbc2RUPYCaseTempMinSetThrDegCx10_Object(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 7, 3, 5),
    _Mpbc2RUPYCaseTempMinSetThrDegCx10_Type()
)
mpbc2RUPYCaseTempMinSetThrDegCx10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpbc2RUPYCaseTempMinSetThrDegCx10.setStatus("current")
_Mpbc2RUPYCaseTempMinClearThrDegCx10_Type = Integer32
_Mpbc2RUPYCaseTempMinClearThrDegCx10_Object = MibScalar
mpbc2RUPYCaseTempMinClearThrDegCx10 = _Mpbc2RUPYCaseTempMinClearThrDegCx10_Object(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 7, 3, 6),
    _Mpbc2RUPYCaseTempMinClearThrDegCx10_Type()
)
mpbc2RUPYCaseTempMinClearThrDegCx10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpbc2RUPYCaseTempMinClearThrDegCx10.setStatus("current")
_Mpbc2RUPYCaseTempMaxSetThrDegCx10_Type = Integer32
_Mpbc2RUPYCaseTempMaxSetThrDegCx10_Object = MibScalar
mpbc2RUPYCaseTempMaxSetThrDegCx10 = _Mpbc2RUPYCaseTempMaxSetThrDegCx10_Object(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 7, 3, 7),
    _Mpbc2RUPYCaseTempMaxSetThrDegCx10_Type()
)
mpbc2RUPYCaseTempMaxSetThrDegCx10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpbc2RUPYCaseTempMaxSetThrDegCx10.setStatus("current")
_Mpbc2RUPYCaseTempMaxClearThrDegCx10_Type = Integer32
_Mpbc2RUPYCaseTempMaxClearThrDegCx10_Object = MibScalar
mpbc2RUPYCaseTempMaxClearThrDegCx10 = _Mpbc2RUPYCaseTempMaxClearThrDegCx10_Object(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 7, 3, 8),
    _Mpbc2RUPYCaseTempMaxClearThrDegCx10_Type()
)
mpbc2RUPYCaseTempMaxClearThrDegCx10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpbc2RUPYCaseTempMaxClearThrDegCx10.setStatus("current")
_Mpbc2RUPYCaseTempMinAlrmThrDegCx10_Type = Integer32
_Mpbc2RUPYCaseTempMinAlrmThrDegCx10_Object = MibScalar
mpbc2RUPYCaseTempMinAlrmThrDegCx10 = _Mpbc2RUPYCaseTempMinAlrmThrDegCx10_Object(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 7, 3, 9),
    _Mpbc2RUPYCaseTempMinAlrmThrDegCx10_Type()
)
mpbc2RUPYCaseTempMinAlrmThrDegCx10.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mpbc2RUPYCaseTempMinAlrmThrDegCx10.setStatus("current")
_Mpbc2RUPYCaseTempMaxAlrmThrDegCx10_Type = Integer32
_Mpbc2RUPYCaseTempMaxAlrmThrDegCx10_Object = MibScalar
mpbc2RUPYCaseTempMaxAlrmThrDegCx10 = _Mpbc2RUPYCaseTempMaxAlrmThrDegCx10_Object(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 7, 3, 10),
    _Mpbc2RUPYCaseTempMaxAlrmThrDegCx10_Type()
)
mpbc2RUPYCaseTempMaxAlrmThrDegCx10.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mpbc2RUPYCaseTempMaxAlrmThrDegCx10.setStatus("current")
_Mpbc2RUPYLOSSetThrdBmx100_Type = Integer32
_Mpbc2RUPYLOSSetThrdBmx100_Object = MibScalar
mpbc2RUPYLOSSetThrdBmx100 = _Mpbc2RUPYLOSSetThrdBmx100_Object(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 7, 3, 11),
    _Mpbc2RUPYLOSSetThrdBmx100_Type()
)
mpbc2RUPYLOSSetThrdBmx100.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpbc2RUPYLOSSetThrdBmx100.setStatus("current")
_Mpbc2RUPYLOSClearThrdBmx100_Type = Integer32
_Mpbc2RUPYLOSClearThrdBmx100_Object = MibScalar
mpbc2RUPYLOSClearThrdBmx100 = _Mpbc2RUPYLOSClearThrdBmx100_Object(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 7, 3, 12),
    _Mpbc2RUPYLOSClearThrdBmx100_Type()
)
mpbc2RUPYLOSClearThrdBmx100.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpbc2RUPYLOSClearThrdBmx100.setStatus("current")
_Mpbc2RUPYInputMinThrdBmx100_Type = Integer32
_Mpbc2RUPYInputMinThrdBmx100_Object = MibScalar
mpbc2RUPYInputMinThrdBmx100 = _Mpbc2RUPYInputMinThrdBmx100_Object(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 7, 3, 13),
    _Mpbc2RUPYInputMinThrdBmx100_Type()
)
mpbc2RUPYInputMinThrdBmx100.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mpbc2RUPYInputMinThrdBmx100.setStatus("current")
_Mpbc2RUPYInputMaxThrdBmx100_Type = Integer32
_Mpbc2RUPYInputMaxThrdBmx100_Object = MibScalar
mpbc2RUPYInputMaxThrdBmx100 = _Mpbc2RUPYInputMaxThrdBmx100_Object(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 7, 3, 14),
    _Mpbc2RUPYInputMaxThrdBmx100_Type()
)
mpbc2RUPYInputMaxThrdBmx100.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mpbc2RUPYInputMaxThrdBmx100.setStatus("current")
_Mpbc2RUPYMainOutputMinThrdBx10_Type = Integer32
_Mpbc2RUPYMainOutputMinThrdBx10_Object = MibScalar
mpbc2RUPYMainOutputMinThrdBx10 = _Mpbc2RUPYMainOutputMinThrdBx10_Object(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 7, 3, 15),
    _Mpbc2RUPYMainOutputMinThrdBx10_Type()
)
mpbc2RUPYMainOutputMinThrdBx10.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mpbc2RUPYMainOutputMinThrdBx10.setStatus("current")
_Mpbc2RUPYMainOutputMaxThrdBx10_Type = Integer32
_Mpbc2RUPYMainOutputMaxThrdBx10_Object = MibScalar
mpbc2RUPYMainOutputMaxThrdBx10 = _Mpbc2RUPYMainOutputMaxThrdBx10_Object(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 7, 3, 16),
    _Mpbc2RUPYMainOutputMaxThrdBx10_Type()
)
mpbc2RUPYMainOutputMaxThrdBx10.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mpbc2RUPYMainOutputMaxThrdBx10.setStatus("current")
_Mpbc2RUPYPreampPwrMinThrdBx10_Type = Integer32
_Mpbc2RUPYPreampPwrMinThrdBx10_Object = MibScalar
mpbc2RUPYPreampPwrMinThrdBx10 = _Mpbc2RUPYPreampPwrMinThrdBx10_Object(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 7, 3, 17),
    _Mpbc2RUPYPreampPwrMinThrdBx10_Type()
)
mpbc2RUPYPreampPwrMinThrdBx10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpbc2RUPYPreampPwrMinThrdBx10.setStatus("current")
_Mpbc2RUPYPreampPwrMaxThrdBx10_Type = Integer32
_Mpbc2RUPYPreampPwrMaxThrdBx10_Object = MibScalar
mpbc2RUPYPreampPwrMaxThrdBx10 = _Mpbc2RUPYPreampPwrMaxThrdBx10_Object(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 7, 3, 18),
    _Mpbc2RUPYPreampPwrMaxThrdBx10_Type()
)
mpbc2RUPYPreampPwrMaxThrdBx10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpbc2RUPYPreampPwrMaxThrdBx10.setStatus("current")
_Mpbc2RUPYOSCMode_Type = Unsigned32
_Mpbc2RUPYOSCMode_Object = MibScalar
mpbc2RUPYOSCMode = _Mpbc2RUPYOSCMode_Object(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 7, 3, 19),
    _Mpbc2RUPYOSCMode_Type()
)
mpbc2RUPYOSCMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mpbc2RUPYOSCMode.setStatus("current")
_Mpbc2RUPYOutputPwrSetpointMindBmx10_Type = Unsigned32
_Mpbc2RUPYOutputPwrSetpointMindBmx10_Object = MibScalar
mpbc2RUPYOutputPwrSetpointMindBmx10 = _Mpbc2RUPYOutputPwrSetpointMindBmx10_Object(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 7, 3, 20),
    _Mpbc2RUPYOutputPwrSetpointMindBmx10_Type()
)
mpbc2RUPYOutputPwrSetpointMindBmx10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpbc2RUPYOutputPwrSetpointMindBmx10.setStatus("current")
_Mpbc2RUPYOutputPwrSetpointMaxdBmx10_Type = Unsigned32
_Mpbc2RUPYOutputPwrSetpointMaxdBmx10_Object = MibScalar
mpbc2RUPYOutputPwrSetpointMaxdBmx10 = _Mpbc2RUPYOutputPwrSetpointMaxdBmx10_Object(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 7, 3, 21),
    _Mpbc2RUPYOutputPwrSetpointMaxdBmx10_Type()
)
mpbc2RUPYOutputPwrSetpointMaxdBmx10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpbc2RUPYOutputPwrSetpointMaxdBmx10.setStatus("current")
_Mpbc2RUPYGainSetPointMindBx10_Type = Integer32
_Mpbc2RUPYGainSetPointMindBx10_Object = MibScalar
mpbc2RUPYGainSetPointMindBx10 = _Mpbc2RUPYGainSetPointMindBx10_Object(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 7, 3, 22),
    _Mpbc2RUPYGainSetPointMindBx10_Type()
)
mpbc2RUPYGainSetPointMindBx10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpbc2RUPYGainSetPointMindBx10.setStatus("current")
_Mpbc2RUPYGainSetPointMaxdBx10_Type = Integer32
_Mpbc2RUPYGainSetPointMaxdBx10_Object = MibScalar
mpbc2RUPYGainSetPointMaxdBx10 = _Mpbc2RUPYGainSetPointMaxdBx10_Object(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 7, 3, 23),
    _Mpbc2RUPYGainSetPointMaxdBx10_Type()
)
mpbc2RUPYGainSetPointMaxdBx10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpbc2RUPYGainSetPointMaxdBx10.setStatus("current")
_Mpbc2RUPYPreAmpFaultThrmW_Type = Unsigned32
_Mpbc2RUPYPreAmpFaultThrmW_Object = MibScalar
mpbc2RUPYPreAmpFaultThrmW = _Mpbc2RUPYPreAmpFaultThrmW_Object(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 7, 3, 24),
    _Mpbc2RUPYPreAmpFaultThrmW_Type()
)
mpbc2RUPYPreAmpFaultThrmW.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpbc2RUPYPreAmpFaultThrmW.setStatus("current")
_Mpbc2RUPYPreAmpFaultDelayms_Type = Unsigned32
_Mpbc2RUPYPreAmpFaultDelayms_Object = MibScalar
mpbc2RUPYPreAmpFaultDelayms = _Mpbc2RUPYPreAmpFaultDelayms_Object(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 7, 3, 25),
    _Mpbc2RUPYPreAmpFaultDelayms_Type()
)
mpbc2RUPYPreAmpFaultDelayms.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpbc2RUPYPreAmpFaultDelayms.setStatus("current")
_Mpbc2RUSRP_ObjectIdentity = ObjectIdentity
mpbc2RUSRP = _Mpbc2RUSRP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 8)
)
_Mpbc2RUSRPControl_ObjectIdentity = ObjectIdentity
mpbc2RUSRPControl = _Mpbc2RUSRPControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 8, 1)
)


class _Mpbc2RUSRPLaserMode_Type(Integer32):
    """Custom type mpbc2RUSRPLaserMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("laserOff", 0),
          ("laserAPR", 1))
    )


_Mpbc2RUSRPLaserMode_Type.__name__ = "Integer32"
_Mpbc2RUSRPLaserMode_Object = MibScalar
mpbc2RUSRPLaserMode = _Mpbc2RUSRPLaserMode_Object(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 8, 1, 1),
    _Mpbc2RUSRPLaserMode_Type()
)
mpbc2RUSRPLaserMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mpbc2RUSRPLaserMode.setStatus("current")
_Mpbc2RUSRPControlMode_Type = Unsigned32
_Mpbc2RUSRPControlMode_Object = MibScalar
mpbc2RUSRPControlMode = _Mpbc2RUSRPControlMode_Object(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 8, 1, 2),
    _Mpbc2RUSRPControlMode_Type()
)
mpbc2RUSRPControlMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mpbc2RUSRPControlMode.setStatus("current")
_Mpbc2RUSRPSeedOutputPwrSetPtmW_Type = Unsigned32
_Mpbc2RUSRPSeedOutputPwrSetPtmW_Object = MibScalar
mpbc2RUSRPSeedOutputPwrSetPtmW = _Mpbc2RUSRPSeedOutputPwrSetPtmW_Object(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 8, 1, 3),
    _Mpbc2RUSRPSeedOutputPwrSetPtmW_Type()
)
mpbc2RUSRPSeedOutputPwrSetPtmW.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mpbc2RUSRPSeedOutputPwrSetPtmW.setStatus("current")
_Mpbc2RUSRPMainOutputPwrSetPtmW_Type = Unsigned32
_Mpbc2RUSRPMainOutputPwrSetPtmW_Object = MibScalar
mpbc2RUSRPMainOutputPwrSetPtmW = _Mpbc2RUSRPMainOutputPwrSetPtmW_Object(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 8, 1, 4),
    _Mpbc2RUSRPMainOutputPwrSetPtmW_Type()
)
mpbc2RUSRPMainOutputPwrSetPtmW.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mpbc2RUSRPMainOutputPwrSetPtmW.setStatus("current")
_Mpbc2RUSRPReset_Type = TruthValue
_Mpbc2RUSRPReset_Object = MibScalar
mpbc2RUSRPReset = _Mpbc2RUSRPReset_Object(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 8, 1, 5),
    _Mpbc2RUSRPReset_Type()
)
mpbc2RUSRPReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mpbc2RUSRPReset.setStatus("current")
_Mpbc2RUSRPMonitor_ObjectIdentity = ObjectIdentity
mpbc2RUSRPMonitor = _Mpbc2RUSRPMonitor_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 8, 2)
)
_Mpbc2RUSRPLD1CurmA_Type = Unsigned32
_Mpbc2RUSRPLD1CurmA_Object = MibScalar
mpbc2RUSRPLD1CurmA = _Mpbc2RUSRPLD1CurmA_Object(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 8, 2, 1),
    _Mpbc2RUSRPLD1CurmA_Type()
)
mpbc2RUSRPLD1CurmA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpbc2RUSRPLD1CurmA.setStatus("current")
_Mpbc2RUSRPLD1TempDegCx10_Type = Integer32
_Mpbc2RUSRPLD1TempDegCx10_Object = MibScalar
mpbc2RUSRPLD1TempDegCx10 = _Mpbc2RUSRPLD1TempDegCx10_Object(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 8, 2, 2),
    _Mpbc2RUSRPLD1TempDegCx10_Type()
)
mpbc2RUSRPLD1TempDegCx10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpbc2RUSRPLD1TempDegCx10.setStatus("current")
_Mpbc2RUSRPLD1TECCurmA_Type = Unsigned32
_Mpbc2RUSRPLD1TECCurmA_Object = MibScalar
mpbc2RUSRPLD1TECCurmA = _Mpbc2RUSRPLD1TECCurmA_Object(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 8, 2, 3),
    _Mpbc2RUSRPLD1TECCurmA_Type()
)
mpbc2RUSRPLD1TECCurmA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpbc2RUSRPLD1TECCurmA.setStatus("current")
_Mpbc2RUSRPLD2CurmA_Type = Unsigned32
_Mpbc2RUSRPLD2CurmA_Object = MibScalar
mpbc2RUSRPLD2CurmA = _Mpbc2RUSRPLD2CurmA_Object(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 8, 2, 4),
    _Mpbc2RUSRPLD2CurmA_Type()
)
mpbc2RUSRPLD2CurmA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpbc2RUSRPLD2CurmA.setStatus("current")
_Mpbc2RUSRPCaseTempDegCx10_Type = Integer32
_Mpbc2RUSRPCaseTempDegCx10_Object = MibScalar
mpbc2RUSRPCaseTempDegCx10 = _Mpbc2RUSRPCaseTempDegCx10_Object(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 8, 2, 5),
    _Mpbc2RUSRPCaseTempDegCx10_Type()
)
mpbc2RUSRPCaseTempDegCx10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpbc2RUSRPCaseTempDegCx10.setStatus("current")
_Mpbc2RUSRPMonSeedOutputPwrmWx10_Type = Unsigned32
_Mpbc2RUSRPMonSeedOutputPwrmWx10_Object = MibScalar
mpbc2RUSRPMonSeedOutputPwrmWx10 = _Mpbc2RUSRPMonSeedOutputPwrmWx10_Object(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 8, 2, 6),
    _Mpbc2RUSRPMonSeedOutputPwrmWx10_Type()
)
mpbc2RUSRPMonSeedOutputPwrmWx10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpbc2RUSRPMonSeedOutputPwrmWx10.setStatus("current")
_Mpbc2RUSRPMainOutputPwrmWx10_Type = Unsigned32
_Mpbc2RUSRPMainOutputPwrmWx10_Object = MibScalar
mpbc2RUSRPMainOutputPwrmWx10 = _Mpbc2RUSRPMainOutputPwrmWx10_Object(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 8, 2, 7),
    _Mpbc2RUSRPMainOutputPwrmWx10_Type()
)
mpbc2RUSRPMainOutputPwrmWx10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpbc2RUSRPMainOutputPwrmWx10.setStatus("current")


class _Mpbc2RUSRPMonLaserState_Type(Integer32):
    """Custom type mpbc2RUSRPMonLaserState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              10)
        )
    )
    namedValues = NamedValues(
        *(("laserOff", 0),
          ("laserNormal", 1),
          ("laserALS", 2),
          ("laserALS100", 3),
          ("laserOn", 10))
    )


_Mpbc2RUSRPMonLaserState_Type.__name__ = "Integer32"
_Mpbc2RUSRPMonLaserState_Object = MibScalar
mpbc2RUSRPMonLaserState = _Mpbc2RUSRPMonLaserState_Object(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 8, 2, 8),
    _Mpbc2RUSRPMonLaserState_Type()
)
mpbc2RUSRPMonLaserState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpbc2RUSRPMonLaserState.setStatus("current")


class _Mpbc2RUSRPMonLaserMode_Type(Integer32):
    """Custom type mpbc2RUSRPMonLaserMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              10)
        )
    )
    namedValues = NamedValues(
        *(("laserOff", 0),
          ("laserAPR", 1),
          ("laserOn", 10))
    )


_Mpbc2RUSRPMonLaserMode_Type.__name__ = "Integer32"
_Mpbc2RUSRPMonLaserMode_Object = MibScalar
mpbc2RUSRPMonLaserMode = _Mpbc2RUSRPMonLaserMode_Object(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 8, 2, 9),
    _Mpbc2RUSRPMonLaserMode_Type()
)
mpbc2RUSRPMonLaserMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpbc2RUSRPMonLaserMode.setStatus("current")
_Mpbc2RUSRPMonControlMode_Type = Unsigned32
_Mpbc2RUSRPMonControlMode_Object = MibScalar
mpbc2RUSRPMonControlMode = _Mpbc2RUSRPMonControlMode_Object(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 8, 2, 10),
    _Mpbc2RUSRPMonControlMode_Type()
)
mpbc2RUSRPMonControlMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpbc2RUSRPMonControlMode.setStatus("current")
_Mpbc2RUSRPDisableInputState_Type = Unsigned32
_Mpbc2RUSRPDisableInputState_Object = MibScalar
mpbc2RUSRPDisableInputState = _Mpbc2RUSRPDisableInputState_Object(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 8, 2, 11),
    _Mpbc2RUSRPDisableInputState_Type()
)
mpbc2RUSRPDisableInputState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpbc2RUSRPDisableInputState.setStatus("current")


class _Mpbc2RUSRPUnitState_Type(Integer32):
    """Custom type mpbc2RUSRPUnitState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("stateInit", 0),
          ("stateNormal", 1),
          ("stateFault", 2))
    )


_Mpbc2RUSRPUnitState_Type.__name__ = "Integer32"
_Mpbc2RUSRPUnitState_Object = MibScalar
mpbc2RUSRPUnitState = _Mpbc2RUSRPUnitState_Object(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 8, 2, 12),
    _Mpbc2RUSRPUnitState_Type()
)
mpbc2RUSRPUnitState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpbc2RUSRPUnitState.setStatus("current")


class _Mpbc2RUSRPOSCRxTone_Type(Integer32):
    """Custom type mpbc2RUSRPOSCRxTone based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("noTone", 0),
          ("tone1", 1),
          ("tone2", 2),
          ("tone1plus2", 3))
    )


_Mpbc2RUSRPOSCRxTone_Type.__name__ = "Integer32"
_Mpbc2RUSRPOSCRxTone_Object = MibScalar
mpbc2RUSRPOSCRxTone = _Mpbc2RUSRPOSCRxTone_Object(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 8, 2, 13),
    _Mpbc2RUSRPOSCRxTone_Type()
)
mpbc2RUSRPOSCRxTone.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpbc2RUSRPOSCRxTone.setStatus("current")
_Mpbc2RUSRPOSCTempdegCx10_Type = Integer32
_Mpbc2RUSRPOSCTempdegCx10_Object = MibScalar
mpbc2RUSRPOSCTempdegCx10 = _Mpbc2RUSRPOSCTempdegCx10_Object(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 8, 2, 14),
    _Mpbc2RUSRPOSCTempdegCx10_Type()
)
mpbc2RUSRPOSCTempdegCx10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpbc2RUSRPOSCTempdegCx10.setStatus("current")


class _Mpbc2RUSRPOSCTxTone_Type(Integer32):
    """Custom type mpbc2RUSRPOSCTxTone based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("tone1", 1),
          ("tone2", 2))
    )


_Mpbc2RUSRPOSCTxTone_Type.__name__ = "Integer32"
_Mpbc2RUSRPOSCTxTone_Object = MibScalar
mpbc2RUSRPOSCTxTone = _Mpbc2RUSRPOSCTxTone_Object(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 8, 2, 15),
    _Mpbc2RUSRPOSCTxTone_Type()
)
mpbc2RUSRPOSCTxTone.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpbc2RUSRPOSCTxTone.setStatus("current")
_Mpbc2RUSRPOSCTxPwrmWx100_Type = Integer32
_Mpbc2RUSRPOSCTxPwrmWx100_Object = MibScalar
mpbc2RUSRPOSCTxPwrmWx100 = _Mpbc2RUSRPOSCTxPwrmWx100_Object(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 8, 2, 16),
    _Mpbc2RUSRPOSCTxPwrmWx100_Type()
)
mpbc2RUSRPOSCTxPwrmWx100.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpbc2RUSRPOSCTxPwrmWx100.setStatus("current")
_Mpbc2RUSRPConfiguration_ObjectIdentity = ObjectIdentity
mpbc2RUSRPConfiguration = _Mpbc2RUSRPConfiguration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 8, 3)
)
_Mpbc2RUSRPLD1CurMinThrmA_Type = Unsigned32
_Mpbc2RUSRPLD1CurMinThrmA_Object = MibScalar
mpbc2RUSRPLD1CurMinThrmA = _Mpbc2RUSRPLD1CurMinThrmA_Object(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 8, 3, 1),
    _Mpbc2RUSRPLD1CurMinThrmA_Type()
)
mpbc2RUSRPLD1CurMinThrmA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpbc2RUSRPLD1CurMinThrmA.setStatus("current")
_Mpbc2RUSRPLD1CurMaxThrmA_Type = Unsigned32
_Mpbc2RUSRPLD1CurMaxThrmA_Object = MibScalar
mpbc2RUSRPLD1CurMaxThrmA = _Mpbc2RUSRPLD1CurMaxThrmA_Object(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 8, 3, 2),
    _Mpbc2RUSRPLD1CurMaxThrmA_Type()
)
mpbc2RUSRPLD1CurMaxThrmA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpbc2RUSRPLD1CurMaxThrmA.setStatus("current")
_Mpbc2RUSRPLD2CurMinThrmA_Type = Unsigned32
_Mpbc2RUSRPLD2CurMinThrmA_Object = MibScalar
mpbc2RUSRPLD2CurMinThrmA = _Mpbc2RUSRPLD2CurMinThrmA_Object(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 8, 3, 3),
    _Mpbc2RUSRPLD2CurMinThrmA_Type()
)
mpbc2RUSRPLD2CurMinThrmA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpbc2RUSRPLD2CurMinThrmA.setStatus("current")
_Mpbc2RUSRPLD2CurMaxThrmA_Type = Unsigned32
_Mpbc2RUSRPLD2CurMaxThrmA_Object = MibScalar
mpbc2RUSRPLD2CurMaxThrmA = _Mpbc2RUSRPLD2CurMaxThrmA_Object(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 8, 3, 4),
    _Mpbc2RUSRPLD2CurMaxThrmA_Type()
)
mpbc2RUSRPLD2CurMaxThrmA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpbc2RUSRPLD2CurMaxThrmA.setStatus("current")
_Mpbc2RUSRPCaseTempMinSetThrDegCx10_Type = Integer32
_Mpbc2RUSRPCaseTempMinSetThrDegCx10_Object = MibScalar
mpbc2RUSRPCaseTempMinSetThrDegCx10 = _Mpbc2RUSRPCaseTempMinSetThrDegCx10_Object(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 8, 3, 5),
    _Mpbc2RUSRPCaseTempMinSetThrDegCx10_Type()
)
mpbc2RUSRPCaseTempMinSetThrDegCx10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpbc2RUSRPCaseTempMinSetThrDegCx10.setStatus("current")
_Mpbc2RUSRPCaseTempMinClearThrDegCx10_Type = Integer32
_Mpbc2RUSRPCaseTempMinClearThrDegCx10_Object = MibScalar
mpbc2RUSRPCaseTempMinClearThrDegCx10 = _Mpbc2RUSRPCaseTempMinClearThrDegCx10_Object(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 8, 3, 6),
    _Mpbc2RUSRPCaseTempMinClearThrDegCx10_Type()
)
mpbc2RUSRPCaseTempMinClearThrDegCx10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpbc2RUSRPCaseTempMinClearThrDegCx10.setStatus("current")
_Mpbc2RUSRPCaseTempMaxSetThrDegCx10_Type = Integer32
_Mpbc2RUSRPCaseTempMaxSetThrDegCx10_Object = MibScalar
mpbc2RUSRPCaseTempMaxSetThrDegCx10 = _Mpbc2RUSRPCaseTempMaxSetThrDegCx10_Object(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 8, 3, 7),
    _Mpbc2RUSRPCaseTempMaxSetThrDegCx10_Type()
)
mpbc2RUSRPCaseTempMaxSetThrDegCx10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpbc2RUSRPCaseTempMaxSetThrDegCx10.setStatus("current")
_Mpbc2RUSRPCaseTempMaxClearThrDegCx10_Type = Integer32
_Mpbc2RUSRPCaseTempMaxClearThrDegCx10_Object = MibScalar
mpbc2RUSRPCaseTempMaxClearThrDegCx10 = _Mpbc2RUSRPCaseTempMaxClearThrDegCx10_Object(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 8, 3, 8),
    _Mpbc2RUSRPCaseTempMaxClearThrDegCx10_Type()
)
mpbc2RUSRPCaseTempMaxClearThrDegCx10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpbc2RUSRPCaseTempMaxClearThrDegCx10.setStatus("current")
_Mpbc2RUSRPMainOutputMinThrdBx10_Type = Integer32
_Mpbc2RUSRPMainOutputMinThrdBx10_Object = MibScalar
mpbc2RUSRPMainOutputMinThrdBx10 = _Mpbc2RUSRPMainOutputMinThrdBx10_Object(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 8, 3, 9),
    _Mpbc2RUSRPMainOutputMinThrdBx10_Type()
)
mpbc2RUSRPMainOutputMinThrdBx10.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mpbc2RUSRPMainOutputMinThrdBx10.setStatus("current")
_Mpbc2RUSRPMainOutputMaxThrdBx10_Type = Integer32
_Mpbc2RUSRPMainOutputMaxThrdBx10_Object = MibScalar
mpbc2RUSRPMainOutputMaxThrdBx10 = _Mpbc2RUSRPMainOutputMaxThrdBx10_Object(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 8, 3, 10),
    _Mpbc2RUSRPMainOutputMaxThrdBx10_Type()
)
mpbc2RUSRPMainOutputMaxThrdBx10.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mpbc2RUSRPMainOutputMaxThrdBx10.setStatus("current")
_Mpbc2RUSRPCaseTempMinAlrmThrDegCx10_Type = Integer32
_Mpbc2RUSRPCaseTempMinAlrmThrDegCx10_Object = MibScalar
mpbc2RUSRPCaseTempMinAlrmThrDegCx10 = _Mpbc2RUSRPCaseTempMinAlrmThrDegCx10_Object(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 8, 3, 11),
    _Mpbc2RUSRPCaseTempMinAlrmThrDegCx10_Type()
)
mpbc2RUSRPCaseTempMinAlrmThrDegCx10.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mpbc2RUSRPCaseTempMinAlrmThrDegCx10.setStatus("current")
_Mpbc2RUSRPCaseTempMaxAlrmThrDegCx10_Type = Integer32
_Mpbc2RUSRPCaseTempMaxAlrmThrDegCx10_Object = MibScalar
mpbc2RUSRPCaseTempMaxAlrmThrDegCx10 = _Mpbc2RUSRPCaseTempMaxAlrmThrDegCx10_Object(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 8, 3, 12),
    _Mpbc2RUSRPCaseTempMaxAlrmThrDegCx10_Type()
)
mpbc2RUSRPCaseTempMaxAlrmThrDegCx10.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mpbc2RUSRPCaseTempMaxAlrmThrDegCx10.setStatus("current")
_Mpbc2RUSRPSeedOutputPwrMinThrdBx10_Type = Integer32
_Mpbc2RUSRPSeedOutputPwrMinThrdBx10_Object = MibScalar
mpbc2RUSRPSeedOutputPwrMinThrdBx10 = _Mpbc2RUSRPSeedOutputPwrMinThrdBx10_Object(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 8, 3, 13),
    _Mpbc2RUSRPSeedOutputPwrMinThrdBx10_Type()
)
mpbc2RUSRPSeedOutputPwrMinThrdBx10.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mpbc2RUSRPSeedOutputPwrMinThrdBx10.setStatus("current")
_Mpbc2RUSRPSeedOutputPwrMaxThrdBx10_Type = Integer32
_Mpbc2RUSRPSeedOutputPwrMaxThrdBx10_Object = MibScalar
mpbc2RUSRPSeedOutputPwrMaxThrdBx10 = _Mpbc2RUSRPSeedOutputPwrMaxThrdBx10_Object(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 8, 3, 14),
    _Mpbc2RUSRPSeedOutputPwrMaxThrdBx10_Type()
)
mpbc2RUSRPSeedOutputPwrMaxThrdBx10.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mpbc2RUSRPSeedOutputPwrMaxThrdBx10.setStatus("current")
_Mpbc2RUSRPSeedOutputMinFaultThrmW_Type = Unsigned32
_Mpbc2RUSRPSeedOutputMinFaultThrmW_Object = MibScalar
mpbc2RUSRPSeedOutputMinFaultThrmW = _Mpbc2RUSRPSeedOutputMinFaultThrmW_Object(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 8, 3, 15),
    _Mpbc2RUSRPSeedOutputMinFaultThrmW_Type()
)
mpbc2RUSRPSeedOutputMinFaultThrmW.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpbc2RUSRPSeedOutputMinFaultThrmW.setStatus("current")
_Mpbc2RUSRPMainOutputPwrMinLimdBmx10_Type = Unsigned32
_Mpbc2RUSRPMainOutputPwrMinLimdBmx10_Object = MibScalar
mpbc2RUSRPMainOutputPwrMinLimdBmx10 = _Mpbc2RUSRPMainOutputPwrMinLimdBmx10_Object(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 8, 3, 16),
    _Mpbc2RUSRPMainOutputPwrMinLimdBmx10_Type()
)
mpbc2RUSRPMainOutputPwrMinLimdBmx10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpbc2RUSRPMainOutputPwrMinLimdBmx10.setStatus("current")
_Mpbc2RUSRPMainOutputPwrMaxLimdBmx10_Type = Unsigned32
_Mpbc2RUSRPMainOutputPwrMaxLimdBmx10_Object = MibScalar
mpbc2RUSRPMainOutputPwrMaxLimdBmx10 = _Mpbc2RUSRPMainOutputPwrMaxLimdBmx10_Object(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 8, 3, 17),
    _Mpbc2RUSRPMainOutputPwrMaxLimdBmx10_Type()
)
mpbc2RUSRPMainOutputPwrMaxLimdBmx10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpbc2RUSRPMainOutputPwrMaxLimdBmx10.setStatus("current")
_Mpbc2RUSRPSeedOutputPwrMinLimdBmx10_Type = Integer32
_Mpbc2RUSRPSeedOutputPwrMinLimdBmx10_Object = MibScalar
mpbc2RUSRPSeedOutputPwrMinLimdBmx10 = _Mpbc2RUSRPSeedOutputPwrMinLimdBmx10_Object(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 8, 3, 18),
    _Mpbc2RUSRPSeedOutputPwrMinLimdBmx10_Type()
)
mpbc2RUSRPSeedOutputPwrMinLimdBmx10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpbc2RUSRPSeedOutputPwrMinLimdBmx10.setStatus("current")
_Mpbc2RUSRPSeedOutputPwrMaxLimdBmx10_Type = Integer32
_Mpbc2RUSRPSeedOutputPwrMaxLimdBmx10_Object = MibScalar
mpbc2RUSRPSeedOutputPwrMaxLimdBmx10 = _Mpbc2RUSRPSeedOutputPwrMaxLimdBmx10_Object(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 8, 3, 19),
    _Mpbc2RUSRPSeedOutputPwrMaxLimdBmx10_Type()
)
mpbc2RUSRPSeedOutputPwrMaxLimdBmx10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpbc2RUSRPSeedOutputPwrMaxLimdBmx10.setStatus("current")
_Mpbc2RUSRPSeedFaultDelayms_Type = Integer32
_Mpbc2RUSRPSeedFaultDelayms_Object = MibScalar
mpbc2RUSRPSeedFaultDelayms = _Mpbc2RUSRPSeedFaultDelayms_Object(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 8, 3, 20),
    _Mpbc2RUSRPSeedFaultDelayms_Type()
)
mpbc2RUSRPSeedFaultDelayms.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpbc2RUSRPSeedFaultDelayms.setStatus("current")
_Mpbc2RUCRP_ObjectIdentity = ObjectIdentity
mpbc2RUCRP = _Mpbc2RUCRP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 9)
)
_Mpbc2RUCRPControl_ObjectIdentity = ObjectIdentity
mpbc2RUCRPControl = _Mpbc2RUCRPControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 9, 1)
)


class _Mpbc2RUCRPLaserMode_Type(Integer32):
    """Custom type mpbc2RUCRPLaserMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("laserOff", 0),
          ("laserAPR", 1))
    )


_Mpbc2RUCRPLaserMode_Type.__name__ = "Integer32"
_Mpbc2RUCRPLaserMode_Object = MibScalar
mpbc2RUCRPLaserMode = _Mpbc2RUCRPLaserMode_Object(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 9, 1, 1),
    _Mpbc2RUCRPLaserMode_Type()
)
mpbc2RUCRPLaserMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mpbc2RUCRPLaserMode.setStatus("current")
_Mpbc2RUCRPControlMode_Type = Unsigned32
_Mpbc2RUCRPControlMode_Object = MibScalar
mpbc2RUCRPControlMode = _Mpbc2RUCRPControlMode_Object(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 9, 1, 2),
    _Mpbc2RUCRPControlMode_Type()
)
mpbc2RUCRPControlMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mpbc2RUCRPControlMode.setStatus("current")
_Mpbc2RUCRPSeedOutputPwrSetPtmW_Type = Unsigned32
_Mpbc2RUCRPSeedOutputPwrSetPtmW_Object = MibScalar
mpbc2RUCRPSeedOutputPwrSetPtmW = _Mpbc2RUCRPSeedOutputPwrSetPtmW_Object(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 9, 1, 3),
    _Mpbc2RUCRPSeedOutputPwrSetPtmW_Type()
)
mpbc2RUCRPSeedOutputPwrSetPtmW.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mpbc2RUCRPSeedOutputPwrSetPtmW.setStatus("current")
_Mpbc2RUCRPMainOutputPwrSetPtmW_Type = Unsigned32
_Mpbc2RUCRPMainOutputPwrSetPtmW_Object = MibScalar
mpbc2RUCRPMainOutputPwrSetPtmW = _Mpbc2RUCRPMainOutputPwrSetPtmW_Object(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 9, 1, 4),
    _Mpbc2RUCRPMainOutputPwrSetPtmW_Type()
)
mpbc2RUCRPMainOutputPwrSetPtmW.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mpbc2RUCRPMainOutputPwrSetPtmW.setStatus("current")
_Mpbc2RUCRPReset_Type = TruthValue
_Mpbc2RUCRPReset_Object = MibScalar
mpbc2RUCRPReset = _Mpbc2RUCRPReset_Object(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 9, 1, 5),
    _Mpbc2RUCRPReset_Type()
)
mpbc2RUCRPReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mpbc2RUCRPReset.setStatus("current")
_Mpbc2RUCRPMonitor_ObjectIdentity = ObjectIdentity
mpbc2RUCRPMonitor = _Mpbc2RUCRPMonitor_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 9, 2)
)
_Mpbc2RUCRPLD1CurmA_Type = Unsigned32
_Mpbc2RUCRPLD1CurmA_Object = MibScalar
mpbc2RUCRPLD1CurmA = _Mpbc2RUCRPLD1CurmA_Object(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 9, 2, 1),
    _Mpbc2RUCRPLD1CurmA_Type()
)
mpbc2RUCRPLD1CurmA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpbc2RUCRPLD1CurmA.setStatus("current")
_Mpbc2RUCRPLD1TempDegCx10_Type = Integer32
_Mpbc2RUCRPLD1TempDegCx10_Object = MibScalar
mpbc2RUCRPLD1TempDegCx10 = _Mpbc2RUCRPLD1TempDegCx10_Object(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 9, 2, 2),
    _Mpbc2RUCRPLD1TempDegCx10_Type()
)
mpbc2RUCRPLD1TempDegCx10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpbc2RUCRPLD1TempDegCx10.setStatus("current")
_Mpbc2RUCRPLD1TECCurmA_Type = Unsigned32
_Mpbc2RUCRPLD1TECCurmA_Object = MibScalar
mpbc2RUCRPLD1TECCurmA = _Mpbc2RUCRPLD1TECCurmA_Object(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 9, 2, 3),
    _Mpbc2RUCRPLD1TECCurmA_Type()
)
mpbc2RUCRPLD1TECCurmA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpbc2RUCRPLD1TECCurmA.setStatus("current")
_Mpbc2RUCRPLD2CurmA_Type = Unsigned32
_Mpbc2RUCRPLD2CurmA_Object = MibScalar
mpbc2RUCRPLD2CurmA = _Mpbc2RUCRPLD2CurmA_Object(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 9, 2, 4),
    _Mpbc2RUCRPLD2CurmA_Type()
)
mpbc2RUCRPLD2CurmA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpbc2RUCRPLD2CurmA.setStatus("current")
_Mpbc2RUCRPCaseTempDegCx10_Type = Integer32
_Mpbc2RUCRPCaseTempDegCx10_Object = MibScalar
mpbc2RUCRPCaseTempDegCx10 = _Mpbc2RUCRPCaseTempDegCx10_Object(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 9, 2, 5),
    _Mpbc2RUCRPCaseTempDegCx10_Type()
)
mpbc2RUCRPCaseTempDegCx10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpbc2RUCRPCaseTempDegCx10.setStatus("current")
_Mpbc2RUCRPMonSeedOutputPwrmWx10_Type = Unsigned32
_Mpbc2RUCRPMonSeedOutputPwrmWx10_Object = MibScalar
mpbc2RUCRPMonSeedOutputPwrmWx10 = _Mpbc2RUCRPMonSeedOutputPwrmWx10_Object(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 9, 2, 6),
    _Mpbc2RUCRPMonSeedOutputPwrmWx10_Type()
)
mpbc2RUCRPMonSeedOutputPwrmWx10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpbc2RUCRPMonSeedOutputPwrmWx10.setStatus("current")
_Mpbc2RUCRPMainOutputPwrmWx10_Type = Unsigned32
_Mpbc2RUCRPMainOutputPwrmWx10_Object = MibScalar
mpbc2RUCRPMainOutputPwrmWx10 = _Mpbc2RUCRPMainOutputPwrmWx10_Object(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 9, 2, 7),
    _Mpbc2RUCRPMainOutputPwrmWx10_Type()
)
mpbc2RUCRPMainOutputPwrmWx10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpbc2RUCRPMainOutputPwrmWx10.setStatus("current")


class _Mpbc2RUCRPMonLaserState_Type(Integer32):
    """Custom type mpbc2RUCRPMonLaserState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              10)
        )
    )
    namedValues = NamedValues(
        *(("laserOff", 0),
          ("laserNormal", 1),
          ("laserALS", 2),
          ("laserALS100", 3),
          ("laserOn", 10))
    )


_Mpbc2RUCRPMonLaserState_Type.__name__ = "Integer32"
_Mpbc2RUCRPMonLaserState_Object = MibScalar
mpbc2RUCRPMonLaserState = _Mpbc2RUCRPMonLaserState_Object(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 9, 2, 8),
    _Mpbc2RUCRPMonLaserState_Type()
)
mpbc2RUCRPMonLaserState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpbc2RUCRPMonLaserState.setStatus("current")


class _Mpbc2RUCRPMonLaserMode_Type(Integer32):
    """Custom type mpbc2RUCRPMonLaserMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              10)
        )
    )
    namedValues = NamedValues(
        *(("laserOff", 0),
          ("laserAPR", 1),
          ("laserOn", 10))
    )


_Mpbc2RUCRPMonLaserMode_Type.__name__ = "Integer32"
_Mpbc2RUCRPMonLaserMode_Object = MibScalar
mpbc2RUCRPMonLaserMode = _Mpbc2RUCRPMonLaserMode_Object(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 9, 2, 9),
    _Mpbc2RUCRPMonLaserMode_Type()
)
mpbc2RUCRPMonLaserMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpbc2RUCRPMonLaserMode.setStatus("current")
_Mpbc2RUCRPMonControlMode_Type = Unsigned32
_Mpbc2RUCRPMonControlMode_Object = MibScalar
mpbc2RUCRPMonControlMode = _Mpbc2RUCRPMonControlMode_Object(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 9, 2, 10),
    _Mpbc2RUCRPMonControlMode_Type()
)
mpbc2RUCRPMonControlMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpbc2RUCRPMonControlMode.setStatus("current")
_Mpbc2RUCRPDisableInputState_Type = Unsigned32
_Mpbc2RUCRPDisableInputState_Object = MibScalar
mpbc2RUCRPDisableInputState = _Mpbc2RUCRPDisableInputState_Object(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 9, 2, 11),
    _Mpbc2RUCRPDisableInputState_Type()
)
mpbc2RUCRPDisableInputState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpbc2RUCRPDisableInputState.setStatus("current")


class _Mpbc2RUCRPUnitState_Type(Integer32):
    """Custom type mpbc2RUCRPUnitState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("stateInit", 0),
          ("stateNormal", 1),
          ("stateFault", 2))
    )


_Mpbc2RUCRPUnitState_Type.__name__ = "Integer32"
_Mpbc2RUCRPUnitState_Object = MibScalar
mpbc2RUCRPUnitState = _Mpbc2RUCRPUnitState_Object(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 9, 2, 12),
    _Mpbc2RUCRPUnitState_Type()
)
mpbc2RUCRPUnitState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpbc2RUCRPUnitState.setStatus("current")


class _Mpbc2RUCRPOSCRx1574Tone_Type(Integer32):
    """Custom type mpbc2RUCRPOSCRx1574Tone based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("noTone", 0),
          ("tone1", 1),
          ("tone2", 2),
          ("tone1plus2", 3))
    )


_Mpbc2RUCRPOSCRx1574Tone_Type.__name__ = "Integer32"
_Mpbc2RUCRPOSCRx1574Tone_Object = MibScalar
mpbc2RUCRPOSCRx1574Tone = _Mpbc2RUCRPOSCRx1574Tone_Object(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 9, 2, 13),
    _Mpbc2RUCRPOSCRx1574Tone_Type()
)
mpbc2RUCRPOSCRx1574Tone.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpbc2RUCRPOSCRx1574Tone.setStatus("current")
_Mpbc2RUCRPOSCTempdegCx10_Type = Integer32
_Mpbc2RUCRPOSCTempdegCx10_Object = MibScalar
mpbc2RUCRPOSCTempdegCx10 = _Mpbc2RUCRPOSCTempdegCx10_Object(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 9, 2, 14),
    _Mpbc2RUCRPOSCTempdegCx10_Type()
)
mpbc2RUCRPOSCTempdegCx10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpbc2RUCRPOSCTempdegCx10.setStatus("current")


class _Mpbc2RUCRPOSCTx1610Tone_Type(Integer32):
    """Custom type mpbc2RUCRPOSCTx1610Tone based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("tone1", 1),
          ("tone2", 2),
          ("tone1plus2", 3))
    )


_Mpbc2RUCRPOSCTx1610Tone_Type.__name__ = "Integer32"
_Mpbc2RUCRPOSCTx1610Tone_Object = MibScalar
mpbc2RUCRPOSCTx1610Tone = _Mpbc2RUCRPOSCTx1610Tone_Object(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 9, 2, 15),
    _Mpbc2RUCRPOSCTx1610Tone_Type()
)
mpbc2RUCRPOSCTx1610Tone.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpbc2RUCRPOSCTx1610Tone.setStatus("current")
_Mpbc2RUCRPOSCTxPwrmWx100_Type = Integer32
_Mpbc2RUCRPOSCTxPwrmWx100_Object = MibScalar
mpbc2RUCRPOSCTxPwrmWx100 = _Mpbc2RUCRPOSCTxPwrmWx100_Object(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 9, 2, 16),
    _Mpbc2RUCRPOSCTxPwrmWx100_Type()
)
mpbc2RUCRPOSCTxPwrmWx100.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpbc2RUCRPOSCTxPwrmWx100.setStatus("current")


class _Mpbc2RUCRPOSCRx1610Tone_Type(Integer32):
    """Custom type mpbc2RUCRPOSCRx1610Tone based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("tone1", 1),
          ("tone2", 2),
          ("tone1plus2", 3))
    )


_Mpbc2RUCRPOSCRx1610Tone_Type.__name__ = "Integer32"
_Mpbc2RUCRPOSCRx1610Tone_Object = MibScalar
mpbc2RUCRPOSCRx1610Tone = _Mpbc2RUCRPOSCRx1610Tone_Object(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 9, 2, 17),
    _Mpbc2RUCRPOSCRx1610Tone_Type()
)
mpbc2RUCRPOSCRx1610Tone.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpbc2RUCRPOSCRx1610Tone.setStatus("current")
_Mpbc2RUCRPConfiguration_ObjectIdentity = ObjectIdentity
mpbc2RUCRPConfiguration = _Mpbc2RUCRPConfiguration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 9, 3)
)
_Mpbc2RUCRPLD1CurMinThrmA_Type = Unsigned32
_Mpbc2RUCRPLD1CurMinThrmA_Object = MibScalar
mpbc2RUCRPLD1CurMinThrmA = _Mpbc2RUCRPLD1CurMinThrmA_Object(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 9, 3, 1),
    _Mpbc2RUCRPLD1CurMinThrmA_Type()
)
mpbc2RUCRPLD1CurMinThrmA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpbc2RUCRPLD1CurMinThrmA.setStatus("current")
_Mpbc2RUCRPLD1CurMaxThrmA_Type = Unsigned32
_Mpbc2RUCRPLD1CurMaxThrmA_Object = MibScalar
mpbc2RUCRPLD1CurMaxThrmA = _Mpbc2RUCRPLD1CurMaxThrmA_Object(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 9, 3, 2),
    _Mpbc2RUCRPLD1CurMaxThrmA_Type()
)
mpbc2RUCRPLD1CurMaxThrmA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpbc2RUCRPLD1CurMaxThrmA.setStatus("current")
_Mpbc2RUCRPLD2CurMinThrmA_Type = Unsigned32
_Mpbc2RUCRPLD2CurMinThrmA_Object = MibScalar
mpbc2RUCRPLD2CurMinThrmA = _Mpbc2RUCRPLD2CurMinThrmA_Object(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 9, 3, 3),
    _Mpbc2RUCRPLD2CurMinThrmA_Type()
)
mpbc2RUCRPLD2CurMinThrmA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpbc2RUCRPLD2CurMinThrmA.setStatus("current")
_Mpbc2RUCRPLD2CurMaxThrmA_Type = Unsigned32
_Mpbc2RUCRPLD2CurMaxThrmA_Object = MibScalar
mpbc2RUCRPLD2CurMaxThrmA = _Mpbc2RUCRPLD2CurMaxThrmA_Object(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 9, 3, 4),
    _Mpbc2RUCRPLD2CurMaxThrmA_Type()
)
mpbc2RUCRPLD2CurMaxThrmA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpbc2RUCRPLD2CurMaxThrmA.setStatus("current")
_Mpbc2RUCRPCaseTempMinSetThrDegCx10_Type = Integer32
_Mpbc2RUCRPCaseTempMinSetThrDegCx10_Object = MibScalar
mpbc2RUCRPCaseTempMinSetThrDegCx10 = _Mpbc2RUCRPCaseTempMinSetThrDegCx10_Object(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 9, 3, 5),
    _Mpbc2RUCRPCaseTempMinSetThrDegCx10_Type()
)
mpbc2RUCRPCaseTempMinSetThrDegCx10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpbc2RUCRPCaseTempMinSetThrDegCx10.setStatus("current")
_Mpbc2RUCRPCaseTempMinClearThrDegCx10_Type = Integer32
_Mpbc2RUCRPCaseTempMinClearThrDegCx10_Object = MibScalar
mpbc2RUCRPCaseTempMinClearThrDegCx10 = _Mpbc2RUCRPCaseTempMinClearThrDegCx10_Object(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 9, 3, 6),
    _Mpbc2RUCRPCaseTempMinClearThrDegCx10_Type()
)
mpbc2RUCRPCaseTempMinClearThrDegCx10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpbc2RUCRPCaseTempMinClearThrDegCx10.setStatus("current")
_Mpbc2RUCRPCaseTempMaxSetThrDegCx10_Type = Integer32
_Mpbc2RUCRPCaseTempMaxSetThrDegCx10_Object = MibScalar
mpbc2RUCRPCaseTempMaxSetThrDegCx10 = _Mpbc2RUCRPCaseTempMaxSetThrDegCx10_Object(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 9, 3, 7),
    _Mpbc2RUCRPCaseTempMaxSetThrDegCx10_Type()
)
mpbc2RUCRPCaseTempMaxSetThrDegCx10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpbc2RUCRPCaseTempMaxSetThrDegCx10.setStatus("current")
_Mpbc2RUCRPCaseTempMaxClearThrDegCx10_Type = Integer32
_Mpbc2RUCRPCaseTempMaxClearThrDegCx10_Object = MibScalar
mpbc2RUCRPCaseTempMaxClearThrDegCx10 = _Mpbc2RUCRPCaseTempMaxClearThrDegCx10_Object(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 9, 3, 8),
    _Mpbc2RUCRPCaseTempMaxClearThrDegCx10_Type()
)
mpbc2RUCRPCaseTempMaxClearThrDegCx10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpbc2RUCRPCaseTempMaxClearThrDegCx10.setStatus("current")
_Mpbc2RUCRPMainOutputMinThrdBx10_Type = Integer32
_Mpbc2RUCRPMainOutputMinThrdBx10_Object = MibScalar
mpbc2RUCRPMainOutputMinThrdBx10 = _Mpbc2RUCRPMainOutputMinThrdBx10_Object(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 9, 3, 9),
    _Mpbc2RUCRPMainOutputMinThrdBx10_Type()
)
mpbc2RUCRPMainOutputMinThrdBx10.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mpbc2RUCRPMainOutputMinThrdBx10.setStatus("current")
_Mpbc2RUCRPMainOutputMaxThrdBx10_Type = Integer32
_Mpbc2RUCRPMainOutputMaxThrdBx10_Object = MibScalar
mpbc2RUCRPMainOutputMaxThrdBx10 = _Mpbc2RUCRPMainOutputMaxThrdBx10_Object(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 9, 3, 10),
    _Mpbc2RUCRPMainOutputMaxThrdBx10_Type()
)
mpbc2RUCRPMainOutputMaxThrdBx10.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mpbc2RUCRPMainOutputMaxThrdBx10.setStatus("current")
_Mpbc2RUCRPCaseTempMinAlrmThrDegCx10_Type = Integer32
_Mpbc2RUCRPCaseTempMinAlrmThrDegCx10_Object = MibScalar
mpbc2RUCRPCaseTempMinAlrmThrDegCx10 = _Mpbc2RUCRPCaseTempMinAlrmThrDegCx10_Object(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 9, 3, 11),
    _Mpbc2RUCRPCaseTempMinAlrmThrDegCx10_Type()
)
mpbc2RUCRPCaseTempMinAlrmThrDegCx10.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mpbc2RUCRPCaseTempMinAlrmThrDegCx10.setStatus("current")
_Mpbc2RUCRPCaseTempMaxAlrmThrDegCx10_Type = Integer32
_Mpbc2RUCRPCaseTempMaxAlrmThrDegCx10_Object = MibScalar
mpbc2RUCRPCaseTempMaxAlrmThrDegCx10 = _Mpbc2RUCRPCaseTempMaxAlrmThrDegCx10_Object(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 9, 3, 12),
    _Mpbc2RUCRPCaseTempMaxAlrmThrDegCx10_Type()
)
mpbc2RUCRPCaseTempMaxAlrmThrDegCx10.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mpbc2RUCRPCaseTempMaxAlrmThrDegCx10.setStatus("current")
_Mpbc2RUCRPSeedOutputPwrMinThrdBx10_Type = Integer32
_Mpbc2RUCRPSeedOutputPwrMinThrdBx10_Object = MibScalar
mpbc2RUCRPSeedOutputPwrMinThrdBx10 = _Mpbc2RUCRPSeedOutputPwrMinThrdBx10_Object(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 9, 3, 13),
    _Mpbc2RUCRPSeedOutputPwrMinThrdBx10_Type()
)
mpbc2RUCRPSeedOutputPwrMinThrdBx10.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mpbc2RUCRPSeedOutputPwrMinThrdBx10.setStatus("current")
_Mpbc2RUCRPSeedOutputPwrMaxThrdBx10_Type = Integer32
_Mpbc2RUCRPSeedOutputPwrMaxThrdBx10_Object = MibScalar
mpbc2RUCRPSeedOutputPwrMaxThrdBx10 = _Mpbc2RUCRPSeedOutputPwrMaxThrdBx10_Object(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 9, 3, 14),
    _Mpbc2RUCRPSeedOutputPwrMaxThrdBx10_Type()
)
mpbc2RUCRPSeedOutputPwrMaxThrdBx10.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mpbc2RUCRPSeedOutputPwrMaxThrdBx10.setStatus("current")
_Mpbc2RUCRPSeedOutputMinFaultThrmW_Type = Unsigned32
_Mpbc2RUCRPSeedOutputMinFaultThrmW_Object = MibScalar
mpbc2RUCRPSeedOutputMinFaultThrmW = _Mpbc2RUCRPSeedOutputMinFaultThrmW_Object(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 9, 3, 15),
    _Mpbc2RUCRPSeedOutputMinFaultThrmW_Type()
)
mpbc2RUCRPSeedOutputMinFaultThrmW.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpbc2RUCRPSeedOutputMinFaultThrmW.setStatus("current")
_Mpbc2RUCRPMainOutputPwrMinLimdBmx10_Type = Unsigned32
_Mpbc2RUCRPMainOutputPwrMinLimdBmx10_Object = MibScalar
mpbc2RUCRPMainOutputPwrMinLimdBmx10 = _Mpbc2RUCRPMainOutputPwrMinLimdBmx10_Object(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 9, 3, 16),
    _Mpbc2RUCRPMainOutputPwrMinLimdBmx10_Type()
)
mpbc2RUCRPMainOutputPwrMinLimdBmx10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpbc2RUCRPMainOutputPwrMinLimdBmx10.setStatus("current")
_Mpbc2RUCRPMainOutputPwrMaxLimdBmx10_Type = Unsigned32
_Mpbc2RUCRPMainOutputPwrMaxLimdBmx10_Object = MibScalar
mpbc2RUCRPMainOutputPwrMaxLimdBmx10 = _Mpbc2RUCRPMainOutputPwrMaxLimdBmx10_Object(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 9, 3, 17),
    _Mpbc2RUCRPMainOutputPwrMaxLimdBmx10_Type()
)
mpbc2RUCRPMainOutputPwrMaxLimdBmx10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpbc2RUCRPMainOutputPwrMaxLimdBmx10.setStatus("current")
_Mpbc2RUCRPSeedOutputPwrMinLimdBmx10_Type = Integer32
_Mpbc2RUCRPSeedOutputPwrMinLimdBmx10_Object = MibScalar
mpbc2RUCRPSeedOutputPwrMinLimdBmx10 = _Mpbc2RUCRPSeedOutputPwrMinLimdBmx10_Object(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 9, 3, 18),
    _Mpbc2RUCRPSeedOutputPwrMinLimdBmx10_Type()
)
mpbc2RUCRPSeedOutputPwrMinLimdBmx10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpbc2RUCRPSeedOutputPwrMinLimdBmx10.setStatus("current")
_Mpbc2RUCRPSeedOutputPwrMaxLimdBmx10_Type = Integer32
_Mpbc2RUCRPSeedOutputPwrMaxLimdBmx10_Object = MibScalar
mpbc2RUCRPSeedOutputPwrMaxLimdBmx10 = _Mpbc2RUCRPSeedOutputPwrMaxLimdBmx10_Object(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 9, 3, 19),
    _Mpbc2RUCRPSeedOutputPwrMaxLimdBmx10_Type()
)
mpbc2RUCRPSeedOutputPwrMaxLimdBmx10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpbc2RUCRPSeedOutputPwrMaxLimdBmx10.setStatus("current")
_Mpbc2RUCRPSeedFaultDelayms_Type = Unsigned32
_Mpbc2RUCRPSeedFaultDelayms_Object = MibScalar
mpbc2RUCRPSeedFaultDelayms = _Mpbc2RUCRPSeedFaultDelayms_Object(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 9, 3, 20),
    _Mpbc2RUCRPSeedFaultDelayms_Type()
)
mpbc2RUCRPSeedFaultDelayms.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpbc2RUCRPSeedFaultDelayms.setStatus("current")
_Mpbc2RUCRPOSCMode_Type = Unsigned32
_Mpbc2RUCRPOSCMode_Object = MibScalar
mpbc2RUCRPOSCMode = _Mpbc2RUCRPOSCMode_Object(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 9, 3, 21),
    _Mpbc2RUCRPOSCMode_Type()
)
mpbc2RUCRPOSCMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mpbc2RUCRPOSCMode.setStatus("current")
_Mpbc2RURFL148x_ObjectIdentity = ObjectIdentity
mpbc2RURFL148x = _Mpbc2RURFL148x_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 10)
)
_Mpbc2RURFL148xControl_ObjectIdentity = ObjectIdentity
mpbc2RURFL148xControl = _Mpbc2RURFL148xControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 10, 1)
)


class _Mpbc2RURFL148xLaserMode_Type(Integer32):
    """Custom type mpbc2RURFL148xLaserMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("laserOff", 0),
          ("laserAPR", 1))
    )


_Mpbc2RURFL148xLaserMode_Type.__name__ = "Integer32"
_Mpbc2RURFL148xLaserMode_Object = MibScalar
mpbc2RURFL148xLaserMode = _Mpbc2RURFL148xLaserMode_Object(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 10, 1, 1),
    _Mpbc2RURFL148xLaserMode_Type()
)
mpbc2RURFL148xLaserMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mpbc2RURFL148xLaserMode.setStatus("current")
_Mpbc2RURFL148xControlMode_Type = Integer32
_Mpbc2RURFL148xControlMode_Object = MibScalar
mpbc2RURFL148xControlMode = _Mpbc2RURFL148xControlMode_Object(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 10, 1, 2),
    _Mpbc2RURFL148xControlMode_Type()
)
mpbc2RURFL148xControlMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mpbc2RURFL148xControlMode.setStatus("current")
_Mpbc2RURFL148xPwrSetPtmW_Type = Unsigned32
_Mpbc2RURFL148xPwrSetPtmW_Object = MibScalar
mpbc2RURFL148xPwrSetPtmW = _Mpbc2RURFL148xPwrSetPtmW_Object(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 10, 1, 3),
    _Mpbc2RURFL148xPwrSetPtmW_Type()
)
mpbc2RURFL148xPwrSetPtmW.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mpbc2RURFL148xPwrSetPtmW.setStatus("current")
_Mpbc2RURFL148xReset_Type = TruthValue
_Mpbc2RURFL148xReset_Object = MibScalar
mpbc2RURFL148xReset = _Mpbc2RURFL148xReset_Object(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 10, 1, 4),
    _Mpbc2RURFL148xReset_Type()
)
mpbc2RURFL148xReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mpbc2RURFL148xReset.setStatus("current")
_Mpbc2RURFL148xMonitor_ObjectIdentity = ObjectIdentity
mpbc2RURFL148xMonitor = _Mpbc2RURFL148xMonitor_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 10, 2)
)
_Mpbc2RURFL148xLD1Current_Type = Unsigned32
_Mpbc2RURFL148xLD1Current_Object = MibScalar
mpbc2RURFL148xLD1Current = _Mpbc2RURFL148xLD1Current_Object(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 10, 2, 1),
    _Mpbc2RURFL148xLD1Current_Type()
)
mpbc2RURFL148xLD1Current.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpbc2RURFL148xLD1Current.setStatus("current")
_Mpbc2RURFL148xLD2Current_Type = Unsigned32
_Mpbc2RURFL148xLD2Current_Object = MibScalar
mpbc2RURFL148xLD2Current = _Mpbc2RURFL148xLD2Current_Object(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 10, 2, 2),
    _Mpbc2RURFL148xLD2Current_Type()
)
mpbc2RURFL148xLD2Current.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpbc2RURFL148xLD2Current.setStatus("current")
_Mpbc2RURFL148xCaseTempDegCx10_Type = Integer32
_Mpbc2RURFL148xCaseTempDegCx10_Object = MibScalar
mpbc2RURFL148xCaseTempDegCx10 = _Mpbc2RURFL148xCaseTempDegCx10_Object(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 10, 2, 3),
    _Mpbc2RURFL148xCaseTempDegCx10_Type()
)
mpbc2RURFL148xCaseTempDegCx10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpbc2RURFL148xCaseTempDegCx10.setStatus("current")
_Mpbc2RURFL148xOutputPwrmW_Type = Unsigned32
_Mpbc2RURFL148xOutputPwrmW_Object = MibScalar
mpbc2RURFL148xOutputPwrmW = _Mpbc2RURFL148xOutputPwrmW_Object(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 10, 2, 4),
    _Mpbc2RURFL148xOutputPwrmW_Type()
)
mpbc2RURFL148xOutputPwrmW.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpbc2RURFL148xOutputPwrmW.setStatus("current")


class _Mpbc2RURFL148xMonLaserState_Type(Integer32):
    """Custom type mpbc2RURFL148xMonLaserState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              10)
        )
    )
    namedValues = NamedValues(
        *(("laserOff", 0),
          ("laserNormal", 1),
          ("laserALS", 2),
          ("laserALS100", 3),
          ("laserOn", 10))
    )


_Mpbc2RURFL148xMonLaserState_Type.__name__ = "Integer32"
_Mpbc2RURFL148xMonLaserState_Object = MibScalar
mpbc2RURFL148xMonLaserState = _Mpbc2RURFL148xMonLaserState_Object(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 10, 2, 5),
    _Mpbc2RURFL148xMonLaserState_Type()
)
mpbc2RURFL148xMonLaserState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpbc2RURFL148xMonLaserState.setStatus("current")


class _Mpbc2RURFL148xMonLaserMode_Type(Integer32):
    """Custom type mpbc2RURFL148xMonLaserMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              10)
        )
    )
    namedValues = NamedValues(
        *(("laserOff", 0),
          ("laserAPR", 1),
          ("laserOn", 10))
    )


_Mpbc2RURFL148xMonLaserMode_Type.__name__ = "Integer32"
_Mpbc2RURFL148xMonLaserMode_Object = MibScalar
mpbc2RURFL148xMonLaserMode = _Mpbc2RURFL148xMonLaserMode_Object(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 10, 2, 6),
    _Mpbc2RURFL148xMonLaserMode_Type()
)
mpbc2RURFL148xMonLaserMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpbc2RURFL148xMonLaserMode.setStatus("current")
_Mpbc2RURFL148xMonControlMode_Type = Unsigned32
_Mpbc2RURFL148xMonControlMode_Object = MibScalar
mpbc2RURFL148xMonControlMode = _Mpbc2RURFL148xMonControlMode_Object(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 10, 2, 7),
    _Mpbc2RURFL148xMonControlMode_Type()
)
mpbc2RURFL148xMonControlMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpbc2RURFL148xMonControlMode.setStatus("current")
_Mpbc2RURFL148xDisableInputState_Type = Integer32
_Mpbc2RURFL148xDisableInputState_Object = MibScalar
mpbc2RURFL148xDisableInputState = _Mpbc2RURFL148xDisableInputState_Object(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 10, 2, 8),
    _Mpbc2RURFL148xDisableInputState_Type()
)
mpbc2RURFL148xDisableInputState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpbc2RURFL148xDisableInputState.setStatus("current")


class _Mpbc2RURFL148xUnitState_Type(Integer32):
    """Custom type mpbc2RURFL148xUnitState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("stateInit", 0),
          ("stateNormal", 1),
          ("stateFault", 2))
    )


_Mpbc2RURFL148xUnitState_Type.__name__ = "Integer32"
_Mpbc2RURFL148xUnitState_Object = MibScalar
mpbc2RURFL148xUnitState = _Mpbc2RURFL148xUnitState_Object(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 10, 2, 9),
    _Mpbc2RURFL148xUnitState_Type()
)
mpbc2RURFL148xUnitState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpbc2RURFL148xUnitState.setStatus("current")


class _Mpbc2RURFL148xOSCRx1574Tone_Type(Integer32):
    """Custom type mpbc2RURFL148xOSCRx1574Tone based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("noTone", 0),
          ("tone1", 1),
          ("tone2", 2),
          ("tone1plus2", 3))
    )


_Mpbc2RURFL148xOSCRx1574Tone_Type.__name__ = "Integer32"
_Mpbc2RURFL148xOSCRx1574Tone_Object = MibScalar
mpbc2RURFL148xOSCRx1574Tone = _Mpbc2RURFL148xOSCRx1574Tone_Object(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 10, 2, 10),
    _Mpbc2RURFL148xOSCRx1574Tone_Type()
)
mpbc2RURFL148xOSCRx1574Tone.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpbc2RURFL148xOSCRx1574Tone.setStatus("current")
_Mpbc2RURFL148xOSCTempDegCx10_Type = Integer32
_Mpbc2RURFL148xOSCTempDegCx10_Object = MibScalar
mpbc2RURFL148xOSCTempDegCx10 = _Mpbc2RURFL148xOSCTempDegCx10_Object(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 10, 2, 11),
    _Mpbc2RURFL148xOSCTempDegCx10_Type()
)
mpbc2RURFL148xOSCTempDegCx10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpbc2RURFL148xOSCTempDegCx10.setStatus("current")


class _Mpbc2RURFL148xOSCTxTone_Type(Integer32):
    """Custom type mpbc2RURFL148xOSCTxTone based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("tone1", 1),
          ("tone2", 2))
    )


_Mpbc2RURFL148xOSCTxTone_Type.__name__ = "Integer32"
_Mpbc2RURFL148xOSCTxTone_Object = MibScalar
mpbc2RURFL148xOSCTxTone = _Mpbc2RURFL148xOSCTxTone_Object(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 10, 2, 12),
    _Mpbc2RURFL148xOSCTxTone_Type()
)
mpbc2RURFL148xOSCTxTone.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpbc2RURFL148xOSCTxTone.setStatus("current")
_Mpbc2RURFL148xOSCTxPwrmWx100_Type = Integer32
_Mpbc2RURFL148xOSCTxPwrmWx100_Object = MibScalar
mpbc2RURFL148xOSCTxPwrmWx100 = _Mpbc2RURFL148xOSCTxPwrmWx100_Object(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 10, 2, 13),
    _Mpbc2RURFL148xOSCTxPwrmWx100_Type()
)
mpbc2RURFL148xOSCTxPwrmWx100.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpbc2RURFL148xOSCTxPwrmWx100.setStatus("current")


class _Mpbc2RURFL148xOSCRx1610Tone_Type(Integer32):
    """Custom type mpbc2RURFL148xOSCRx1610Tone based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("tone1", 1),
          ("tone2", 2))
    )


_Mpbc2RURFL148xOSCRx1610Tone_Type.__name__ = "Integer32"
_Mpbc2RURFL148xOSCRx1610Tone_Object = MibScalar
mpbc2RURFL148xOSCRx1610Tone = _Mpbc2RURFL148xOSCRx1610Tone_Object(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 10, 2, 14),
    _Mpbc2RURFL148xOSCRx1610Tone_Type()
)
mpbc2RURFL148xOSCRx1610Tone.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpbc2RURFL148xOSCRx1610Tone.setStatus("current")
_Mpbc2RURFL148xConfiguration_ObjectIdentity = ObjectIdentity
mpbc2RURFL148xConfiguration = _Mpbc2RURFL148xConfiguration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 10, 3)
)
_Mpbc2RURFL148xAlarmPwrThrLowdBx10_Type = Integer32
_Mpbc2RURFL148xAlarmPwrThrLowdBx10_Object = MibScalar
mpbc2RURFL148xAlarmPwrThrLowdBx10 = _Mpbc2RURFL148xAlarmPwrThrLowdBx10_Object(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 10, 3, 1),
    _Mpbc2RURFL148xAlarmPwrThrLowdBx10_Type()
)
mpbc2RURFL148xAlarmPwrThrLowdBx10.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mpbc2RURFL148xAlarmPwrThrLowdBx10.setStatus("current")
_Mpbc2RURFL148xAlarmPwrThrHidBx10_Type = Unsigned32
_Mpbc2RURFL148xAlarmPwrThrHidBx10_Object = MibScalar
mpbc2RURFL148xAlarmPwrThrHidBx10 = _Mpbc2RURFL148xAlarmPwrThrHidBx10_Object(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 10, 3, 2),
    _Mpbc2RURFL148xAlarmPwrThrHidBx10_Type()
)
mpbc2RURFL148xAlarmPwrThrHidBx10.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mpbc2RURFL148xAlarmPwrThrHidBx10.setStatus("current")
_Mpbc2RURFL148xAlarmCaseTempMinThDegCx10_Type = Integer32
_Mpbc2RURFL148xAlarmCaseTempMinThDegCx10_Object = MibScalar
mpbc2RURFL148xAlarmCaseTempMinThDegCx10 = _Mpbc2RURFL148xAlarmCaseTempMinThDegCx10_Object(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 10, 3, 3),
    _Mpbc2RURFL148xAlarmCaseTempMinThDegCx10_Type()
)
mpbc2RURFL148xAlarmCaseTempMinThDegCx10.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mpbc2RURFL148xAlarmCaseTempMinThDegCx10.setStatus("current")
_Mpbc2RURFL148xAlarmCaseTempMaxThDegCx10_Type = Integer32
_Mpbc2RURFL148xAlarmCaseTempMaxThDegCx10_Object = MibScalar
mpbc2RURFL148xAlarmCaseTempMaxThDegCx10 = _Mpbc2RURFL148xAlarmCaseTempMaxThDegCx10_Object(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 10, 3, 4),
    _Mpbc2RURFL148xAlarmCaseTempMaxThDegCx10_Type()
)
mpbc2RURFL148xAlarmCaseTempMaxThDegCx10.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mpbc2RURFL148xAlarmCaseTempMaxThDegCx10.setStatus("current")
_Mpbc2RURFL148xLD1CurMinThrmA_Type = Unsigned32
_Mpbc2RURFL148xLD1CurMinThrmA_Object = MibScalar
mpbc2RURFL148xLD1CurMinThrmA = _Mpbc2RURFL148xLD1CurMinThrmA_Object(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 10, 3, 5),
    _Mpbc2RURFL148xLD1CurMinThrmA_Type()
)
mpbc2RURFL148xLD1CurMinThrmA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpbc2RURFL148xLD1CurMinThrmA.setStatus("current")
_Mpbc2RURFL148xLD1CurMaxThrmA_Type = Unsigned32
_Mpbc2RURFL148xLD1CurMaxThrmA_Object = MibScalar
mpbc2RURFL148xLD1CurMaxThrmA = _Mpbc2RURFL148xLD1CurMaxThrmA_Object(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 10, 3, 6),
    _Mpbc2RURFL148xLD1CurMaxThrmA_Type()
)
mpbc2RURFL148xLD1CurMaxThrmA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpbc2RURFL148xLD1CurMaxThrmA.setStatus("current")
_Mpbc2RURFL148xLD2CurMinThrmA_Type = Unsigned32
_Mpbc2RURFL148xLD2CurMinThrmA_Object = MibScalar
mpbc2RURFL148xLD2CurMinThrmA = _Mpbc2RURFL148xLD2CurMinThrmA_Object(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 10, 3, 7),
    _Mpbc2RURFL148xLD2CurMinThrmA_Type()
)
mpbc2RURFL148xLD2CurMinThrmA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpbc2RURFL148xLD2CurMinThrmA.setStatus("current")
_Mpbc2RURFL148xLD2CurMaxThrmA_Type = Unsigned32
_Mpbc2RURFL148xLD2CurMaxThrmA_Object = MibScalar
mpbc2RURFL148xLD2CurMaxThrmA = _Mpbc2RURFL148xLD2CurMaxThrmA_Object(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 10, 3, 8),
    _Mpbc2RURFL148xLD2CurMaxThrmA_Type()
)
mpbc2RURFL148xLD2CurMaxThrmA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpbc2RURFL148xLD2CurMaxThrmA.setStatus("current")
_Mpbc2RURFL148xCaseTempMinSetThrDegCx10_Type = Integer32
_Mpbc2RURFL148xCaseTempMinSetThrDegCx10_Object = MibScalar
mpbc2RURFL148xCaseTempMinSetThrDegCx10 = _Mpbc2RURFL148xCaseTempMinSetThrDegCx10_Object(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 10, 3, 9),
    _Mpbc2RURFL148xCaseTempMinSetThrDegCx10_Type()
)
mpbc2RURFL148xCaseTempMinSetThrDegCx10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpbc2RURFL148xCaseTempMinSetThrDegCx10.setStatus("current")
_Mpbc2RURFL148xCaseTempMinClearThrDegCx10_Type = Integer32
_Mpbc2RURFL148xCaseTempMinClearThrDegCx10_Object = MibScalar
mpbc2RURFL148xCaseTempMinClearThrDegCx10 = _Mpbc2RURFL148xCaseTempMinClearThrDegCx10_Object(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 10, 3, 10),
    _Mpbc2RURFL148xCaseTempMinClearThrDegCx10_Type()
)
mpbc2RURFL148xCaseTempMinClearThrDegCx10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpbc2RURFL148xCaseTempMinClearThrDegCx10.setStatus("current")
_Mpbc2RURFL148xCaseTempMaxSetThrDegCx10_Type = Integer32
_Mpbc2RURFL148xCaseTempMaxSetThrDegCx10_Object = MibScalar
mpbc2RURFL148xCaseTempMaxSetThrDegCx10 = _Mpbc2RURFL148xCaseTempMaxSetThrDegCx10_Object(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 10, 3, 11),
    _Mpbc2RURFL148xCaseTempMaxSetThrDegCx10_Type()
)
mpbc2RURFL148xCaseTempMaxSetThrDegCx10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpbc2RURFL148xCaseTempMaxSetThrDegCx10.setStatus("current")
_Mpbc2RURFL148xCaseTempMaxClearThrDegCx10_Type = Integer32
_Mpbc2RURFL148xCaseTempMaxClearThrDegCx10_Object = MibScalar
mpbc2RURFL148xCaseTempMaxClearThrDegCx10 = _Mpbc2RURFL148xCaseTempMaxClearThrDegCx10_Object(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 10, 3, 12),
    _Mpbc2RURFL148xCaseTempMaxClearThrDegCx10_Type()
)
mpbc2RURFL148xCaseTempMaxClearThrDegCx10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpbc2RURFL148xCaseTempMaxClearThrDegCx10.setStatus("current")
_Mpbc2RURFL148xOutputPwrSetptMindBmx10_Type = Integer32
_Mpbc2RURFL148xOutputPwrSetptMindBmx10_Object = MibScalar
mpbc2RURFL148xOutputPwrSetptMindBmx10 = _Mpbc2RURFL148xOutputPwrSetptMindBmx10_Object(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 10, 3, 13),
    _Mpbc2RURFL148xOutputPwrSetptMindBmx10_Type()
)
mpbc2RURFL148xOutputPwrSetptMindBmx10.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mpbc2RURFL148xOutputPwrSetptMindBmx10.setStatus("current")
_Mpbc2RURFL148xOutputPwrSetptMaxdBmx10_Type = Integer32
_Mpbc2RURFL148xOutputPwrSetptMaxdBmx10_Object = MibScalar
mpbc2RURFL148xOutputPwrSetptMaxdBmx10 = _Mpbc2RURFL148xOutputPwrSetptMaxdBmx10_Object(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 10, 3, 14),
    _Mpbc2RURFL148xOutputPwrSetptMaxdBmx10_Type()
)
mpbc2RURFL148xOutputPwrSetptMaxdBmx10.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mpbc2RURFL148xOutputPwrSetptMaxdBmx10.setStatus("current")
_Mpbc2RURFL148xOSCMode_Type = Unsigned32
_Mpbc2RURFL148xOSCMode_Object = MibScalar
mpbc2RURFL148xOSCMode = _Mpbc2RURFL148xOSCMode_Object(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 10, 3, 15),
    _Mpbc2RURFL148xOSCMode_Type()
)
mpbc2RURFL148xOSCMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mpbc2RURFL148xOSCMode.setStatus("current")
_Mpbc2RULDP_ObjectIdentity = ObjectIdentity
mpbc2RULDP = _Mpbc2RULDP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 11)
)
_Mpbc2RULDPControl_ObjectIdentity = ObjectIdentity
mpbc2RULDPControl = _Mpbc2RULDPControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 11, 1)
)


class _Mpbc2RULDPLaserMode_Type(Integer32):
    """Custom type mpbc2RULDPLaserMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("laserOff", 0),
          ("laserAPR", 1))
    )


_Mpbc2RULDPLaserMode_Type.__name__ = "Integer32"
_Mpbc2RULDPLaserMode_Object = MibScalar
mpbc2RULDPLaserMode = _Mpbc2RULDPLaserMode_Object(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 11, 1, 1),
    _Mpbc2RULDPLaserMode_Type()
)
mpbc2RULDPLaserMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mpbc2RULDPLaserMode.setStatus("current")
_Mpbc2RULDPControlMode_Type = Unsigned32
_Mpbc2RULDPControlMode_Object = MibScalar
mpbc2RULDPControlMode = _Mpbc2RULDPControlMode_Object(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 11, 1, 2),
    _Mpbc2RULDPControlMode_Type()
)
mpbc2RULDPControlMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mpbc2RULDPControlMode.setStatus("current")
_Mpbc2RULDP1stWLPwrSetPtmW_Type = Unsigned32
_Mpbc2RULDP1stWLPwrSetPtmW_Object = MibScalar
mpbc2RULDP1stWLPwrSetPtmW = _Mpbc2RULDP1stWLPwrSetPtmW_Object(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 11, 1, 3),
    _Mpbc2RULDP1stWLPwrSetPtmW_Type()
)
mpbc2RULDP1stWLPwrSetPtmW.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mpbc2RULDP1stWLPwrSetPtmW.setStatus("current")
_Mpbc2RULDP2ndWLPwrSetPtmW_Type = Unsigned32
_Mpbc2RULDP2ndWLPwrSetPtmW_Object = MibScalar
mpbc2RULDP2ndWLPwrSetPtmW = _Mpbc2RULDP2ndWLPwrSetPtmW_Object(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 11, 1, 4),
    _Mpbc2RULDP2ndWLPwrSetPtmW_Type()
)
mpbc2RULDP2ndWLPwrSetPtmW.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mpbc2RULDP2ndWLPwrSetPtmW.setStatus("current")
_Mpbc2RULDPReset_Type = TruthValue
_Mpbc2RULDPReset_Object = MibScalar
mpbc2RULDPReset = _Mpbc2RULDPReset_Object(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 11, 1, 5),
    _Mpbc2RULDPReset_Type()
)
mpbc2RULDPReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mpbc2RULDPReset.setStatus("current")
_Mpbc2RULDPMonitor_ObjectIdentity = ObjectIdentity
mpbc2RULDPMonitor = _Mpbc2RULDPMonitor_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 11, 2)
)
_Mpbc2RULDPLD1CurmA_Type = Unsigned32
_Mpbc2RULDPLD1CurmA_Object = MibScalar
mpbc2RULDPLD1CurmA = _Mpbc2RULDPLD1CurmA_Object(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 11, 2, 1),
    _Mpbc2RULDPLD1CurmA_Type()
)
mpbc2RULDPLD1CurmA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpbc2RULDPLD1CurmA.setStatus("current")
_Mpbc2RULDPLD1TempDegCx10_Type = Integer32
_Mpbc2RULDPLD1TempDegCx10_Object = MibScalar
mpbc2RULDPLD1TempDegCx10 = _Mpbc2RULDPLD1TempDegCx10_Object(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 11, 2, 2),
    _Mpbc2RULDPLD1TempDegCx10_Type()
)
mpbc2RULDPLD1TempDegCx10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpbc2RULDPLD1TempDegCx10.setStatus("current")
_Mpbc2RULDPLD1TECCurmA_Type = Unsigned32
_Mpbc2RULDPLD1TECCurmA_Object = MibScalar
mpbc2RULDPLD1TECCurmA = _Mpbc2RULDPLD1TECCurmA_Object(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 11, 2, 3),
    _Mpbc2RULDPLD1TECCurmA_Type()
)
mpbc2RULDPLD1TECCurmA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpbc2RULDPLD1TECCurmA.setStatus("current")
_Mpbc2RULDPLD2CurmA_Type = Unsigned32
_Mpbc2RULDPLD2CurmA_Object = MibScalar
mpbc2RULDPLD2CurmA = _Mpbc2RULDPLD2CurmA_Object(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 11, 2, 4),
    _Mpbc2RULDPLD2CurmA_Type()
)
mpbc2RULDPLD2CurmA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpbc2RULDPLD2CurmA.setStatus("current")
_Mpbc2RULDPLD2TempDegCx10_Type = Integer32
_Mpbc2RULDPLD2TempDegCx10_Object = MibScalar
mpbc2RULDPLD2TempDegCx10 = _Mpbc2RULDPLD2TempDegCx10_Object(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 11, 2, 5),
    _Mpbc2RULDPLD2TempDegCx10_Type()
)
mpbc2RULDPLD2TempDegCx10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpbc2RULDPLD2TempDegCx10.setStatus("current")
_Mpbc2RULDPLD2TECCurmA_Type = Unsigned32
_Mpbc2RULDPLD2TECCurmA_Object = MibScalar
mpbc2RULDPLD2TECCurmA = _Mpbc2RULDPLD2TECCurmA_Object(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 11, 2, 6),
    _Mpbc2RULDPLD2TECCurmA_Type()
)
mpbc2RULDPLD2TECCurmA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpbc2RULDPLD2TECCurmA.setStatus("current")
_Mpbc2RULDPCaseTempDegCx10_Type = Integer32
_Mpbc2RULDPCaseTempDegCx10_Object = MibScalar
mpbc2RULDPCaseTempDegCx10 = _Mpbc2RULDPCaseTempDegCx10_Object(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 11, 2, 7),
    _Mpbc2RULDPCaseTempDegCx10_Type()
)
mpbc2RULDPCaseTempDegCx10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpbc2RULDPCaseTempDegCx10.setStatus("current")
_Mpbc2RULDPMon1stWLOutputPwrmWx10_Type = Unsigned32
_Mpbc2RULDPMon1stWLOutputPwrmWx10_Object = MibScalar
mpbc2RULDPMon1stWLOutputPwrmWx10 = _Mpbc2RULDPMon1stWLOutputPwrmWx10_Object(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 11, 2, 8),
    _Mpbc2RULDPMon1stWLOutputPwrmWx10_Type()
)
mpbc2RULDPMon1stWLOutputPwrmWx10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpbc2RULDPMon1stWLOutputPwrmWx10.setStatus("current")
_Mpbc2RULDPMon2ndWLOutputPwrmWx10_Type = Unsigned32
_Mpbc2RULDPMon2ndWLOutputPwrmWx10_Object = MibScalar
mpbc2RULDPMon2ndWLOutputPwrmWx10 = _Mpbc2RULDPMon2ndWLOutputPwrmWx10_Object(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 11, 2, 9),
    _Mpbc2RULDPMon2ndWLOutputPwrmWx10_Type()
)
mpbc2RULDPMon2ndWLOutputPwrmWx10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpbc2RULDPMon2ndWLOutputPwrmWx10.setStatus("current")


class _Mpbc2RULDPMonLaserState_Type(Integer32):
    """Custom type mpbc2RULDPMonLaserState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              10)
        )
    )
    namedValues = NamedValues(
        *(("laserOff", 0),
          ("laserNormal", 1),
          ("laserALS", 2),
          ("laserALS100", 3),
          ("laserOn", 10))
    )


_Mpbc2RULDPMonLaserState_Type.__name__ = "Integer32"
_Mpbc2RULDPMonLaserState_Object = MibScalar
mpbc2RULDPMonLaserState = _Mpbc2RULDPMonLaserState_Object(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 11, 2, 10),
    _Mpbc2RULDPMonLaserState_Type()
)
mpbc2RULDPMonLaserState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpbc2RULDPMonLaserState.setStatus("current")


class _Mpbc2RULDPMonLaserMode_Type(Integer32):
    """Custom type mpbc2RULDPMonLaserMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              10)
        )
    )
    namedValues = NamedValues(
        *(("laserOff", 0),
          ("laserAPR", 1),
          ("laserOn", 10))
    )


_Mpbc2RULDPMonLaserMode_Type.__name__ = "Integer32"
_Mpbc2RULDPMonLaserMode_Object = MibScalar
mpbc2RULDPMonLaserMode = _Mpbc2RULDPMonLaserMode_Object(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 11, 2, 11),
    _Mpbc2RULDPMonLaserMode_Type()
)
mpbc2RULDPMonLaserMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpbc2RULDPMonLaserMode.setStatus("current")
_Mpbc2RULDPMonControlMode_Type = Unsigned32
_Mpbc2RULDPMonControlMode_Object = MibScalar
mpbc2RULDPMonControlMode = _Mpbc2RULDPMonControlMode_Object(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 11, 2, 12),
    _Mpbc2RULDPMonControlMode_Type()
)
mpbc2RULDPMonControlMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpbc2RULDPMonControlMode.setStatus("current")
_Mpbc2RULDPDisableInputState_Type = Unsigned32
_Mpbc2RULDPDisableInputState_Object = MibScalar
mpbc2RULDPDisableInputState = _Mpbc2RULDPDisableInputState_Object(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 11, 2, 13),
    _Mpbc2RULDPDisableInputState_Type()
)
mpbc2RULDPDisableInputState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpbc2RULDPDisableInputState.setStatus("current")


class _Mpbc2RULDPUnitState_Type(Integer32):
    """Custom type mpbc2RULDPUnitState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("stateInit", 0),
          ("stateNormal", 1),
          ("stateFault", 2))
    )


_Mpbc2RULDPUnitState_Type.__name__ = "Integer32"
_Mpbc2RULDPUnitState_Object = MibScalar
mpbc2RULDPUnitState = _Mpbc2RULDPUnitState_Object(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 11, 2, 14),
    _Mpbc2RULDPUnitState_Type()
)
mpbc2RULDPUnitState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpbc2RULDPUnitState.setStatus("current")


class _Mpbc2RULDPOSCRxTone_Type(Integer32):
    """Custom type mpbc2RULDPOSCRxTone based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("noTone", 0),
          ("tone1", 1),
          ("tone2", 2),
          ("tone1plus2", 3))
    )


_Mpbc2RULDPOSCRxTone_Type.__name__ = "Integer32"
_Mpbc2RULDPOSCRxTone_Object = MibScalar
mpbc2RULDPOSCRxTone = _Mpbc2RULDPOSCRxTone_Object(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 11, 2, 15),
    _Mpbc2RULDPOSCRxTone_Type()
)
mpbc2RULDPOSCRxTone.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpbc2RULDPOSCRxTone.setStatus("current")
_Mpbc2RULDPOSCTempDegCx10_Type = Integer32
_Mpbc2RULDPOSCTempDegCx10_Object = MibScalar
mpbc2RULDPOSCTempDegCx10 = _Mpbc2RULDPOSCTempDegCx10_Object(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 11, 2, 16),
    _Mpbc2RULDPOSCTempDegCx10_Type()
)
mpbc2RULDPOSCTempDegCx10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpbc2RULDPOSCTempDegCx10.setStatus("current")


class _Mpbc2RULDPOSCTxTone_Type(Integer32):
    """Custom type mpbc2RULDPOSCTxTone based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("tone1", 1),
          ("tone2", 2))
    )


_Mpbc2RULDPOSCTxTone_Type.__name__ = "Integer32"
_Mpbc2RULDPOSCTxTone_Object = MibScalar
mpbc2RULDPOSCTxTone = _Mpbc2RULDPOSCTxTone_Object(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 11, 2, 17),
    _Mpbc2RULDPOSCTxTone_Type()
)
mpbc2RULDPOSCTxTone.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpbc2RULDPOSCTxTone.setStatus("current")
_Mpbc2RULDPOSCTxPwrmWx100_Type = Integer32
_Mpbc2RULDPOSCTxPwrmWx100_Object = MibScalar
mpbc2RULDPOSCTxPwrmWx100 = _Mpbc2RULDPOSCTxPwrmWx100_Object(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 11, 2, 18),
    _Mpbc2RULDPOSCTxPwrmWx100_Type()
)
mpbc2RULDPOSCTxPwrmWx100.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpbc2RULDPOSCTxPwrmWx100.setStatus("current")
_Mpbc2RULDPConfiguration_ObjectIdentity = ObjectIdentity
mpbc2RULDPConfiguration = _Mpbc2RULDPConfiguration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 11, 3)
)
_Mpbc2RULDPLD1CurMinThrmA_Type = Unsigned32
_Mpbc2RULDPLD1CurMinThrmA_Object = MibScalar
mpbc2RULDPLD1CurMinThrmA = _Mpbc2RULDPLD1CurMinThrmA_Object(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 11, 3, 1),
    _Mpbc2RULDPLD1CurMinThrmA_Type()
)
mpbc2RULDPLD1CurMinThrmA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpbc2RULDPLD1CurMinThrmA.setStatus("current")
_Mpbc2RULDPLD1CurMaxThrmA_Type = Unsigned32
_Mpbc2RULDPLD1CurMaxThrmA_Object = MibScalar
mpbc2RULDPLD1CurMaxThrmA = _Mpbc2RULDPLD1CurMaxThrmA_Object(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 11, 3, 2),
    _Mpbc2RULDPLD1CurMaxThrmA_Type()
)
mpbc2RULDPLD1CurMaxThrmA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpbc2RULDPLD1CurMaxThrmA.setStatus("current")
_Mpbc2RULDPLD2CurMinThrmA_Type = Unsigned32
_Mpbc2RULDPLD2CurMinThrmA_Object = MibScalar
mpbc2RULDPLD2CurMinThrmA = _Mpbc2RULDPLD2CurMinThrmA_Object(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 11, 3, 3),
    _Mpbc2RULDPLD2CurMinThrmA_Type()
)
mpbc2RULDPLD2CurMinThrmA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpbc2RULDPLD2CurMinThrmA.setStatus("current")
_Mpbc2RULDPLD2CurMaxThrmA_Type = Unsigned32
_Mpbc2RULDPLD2CurMaxThrmA_Object = MibScalar
mpbc2RULDPLD2CurMaxThrmA = _Mpbc2RULDPLD2CurMaxThrmA_Object(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 11, 3, 4),
    _Mpbc2RULDPLD2CurMaxThrmA_Type()
)
mpbc2RULDPLD2CurMaxThrmA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpbc2RULDPLD2CurMaxThrmA.setStatus("current")
_Mpbc2RULDPCaseTempMinSetThrDegCx10_Type = Integer32
_Mpbc2RULDPCaseTempMinSetThrDegCx10_Object = MibScalar
mpbc2RULDPCaseTempMinSetThrDegCx10 = _Mpbc2RULDPCaseTempMinSetThrDegCx10_Object(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 11, 3, 5),
    _Mpbc2RULDPCaseTempMinSetThrDegCx10_Type()
)
mpbc2RULDPCaseTempMinSetThrDegCx10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpbc2RULDPCaseTempMinSetThrDegCx10.setStatus("current")
_Mpbc2RULDPCaseTempMinClearThrDegCx10_Type = Integer32
_Mpbc2RULDPCaseTempMinClearThrDegCx10_Object = MibScalar
mpbc2RULDPCaseTempMinClearThrDegCx10 = _Mpbc2RULDPCaseTempMinClearThrDegCx10_Object(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 11, 3, 6),
    _Mpbc2RULDPCaseTempMinClearThrDegCx10_Type()
)
mpbc2RULDPCaseTempMinClearThrDegCx10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpbc2RULDPCaseTempMinClearThrDegCx10.setStatus("current")
_Mpbc2RULDPCaseTempMaxSetThrDegCx10_Type = Integer32
_Mpbc2RULDPCaseTempMaxSetThrDegCx10_Object = MibScalar
mpbc2RULDPCaseTempMaxSetThrDegCx10 = _Mpbc2RULDPCaseTempMaxSetThrDegCx10_Object(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 11, 3, 7),
    _Mpbc2RULDPCaseTempMaxSetThrDegCx10_Type()
)
mpbc2RULDPCaseTempMaxSetThrDegCx10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpbc2RULDPCaseTempMaxSetThrDegCx10.setStatus("current")
_Mpbc2RULDPCaseTempMaxClearThrDegCx10_Type = Integer32
_Mpbc2RULDPCaseTempMaxClearThrDegCx10_Object = MibScalar
mpbc2RULDPCaseTempMaxClearThrDegCx10 = _Mpbc2RULDPCaseTempMaxClearThrDegCx10_Object(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 11, 3, 8),
    _Mpbc2RULDPCaseTempMaxClearThrDegCx10_Type()
)
mpbc2RULDPCaseTempMaxClearThrDegCx10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpbc2RULDPCaseTempMaxClearThrDegCx10.setStatus("current")
_Mpbc2RULDPCaseTempMinAlrmThDegCx10_Type = Integer32
_Mpbc2RULDPCaseTempMinAlrmThDegCx10_Object = MibScalar
mpbc2RULDPCaseTempMinAlrmThDegCx10 = _Mpbc2RULDPCaseTempMinAlrmThDegCx10_Object(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 11, 3, 9),
    _Mpbc2RULDPCaseTempMinAlrmThDegCx10_Type()
)
mpbc2RULDPCaseTempMinAlrmThDegCx10.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mpbc2RULDPCaseTempMinAlrmThDegCx10.setStatus("current")
_Mpbc2RULDPCaseTempMaxAlrmThDegCx10_Type = Integer32
_Mpbc2RULDPCaseTempMaxAlrmThDegCx10_Object = MibScalar
mpbc2RULDPCaseTempMaxAlrmThDegCx10 = _Mpbc2RULDPCaseTempMaxAlrmThDegCx10_Object(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 11, 3, 10),
    _Mpbc2RULDPCaseTempMaxAlrmThDegCx10_Type()
)
mpbc2RULDPCaseTempMaxAlrmThDegCx10.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mpbc2RULDPCaseTempMaxAlrmThDegCx10.setStatus("current")
_Mpbc2RULDP1stWLOutputPwrMinThrdBx10_Type = Integer32
_Mpbc2RULDP1stWLOutputPwrMinThrdBx10_Object = MibScalar
mpbc2RULDP1stWLOutputPwrMinThrdBx10 = _Mpbc2RULDP1stWLOutputPwrMinThrdBx10_Object(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 11, 3, 11),
    _Mpbc2RULDP1stWLOutputPwrMinThrdBx10_Type()
)
mpbc2RULDP1stWLOutputPwrMinThrdBx10.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mpbc2RULDP1stWLOutputPwrMinThrdBx10.setStatus("current")
_Mpbc2RULDP1stWLOutputPwrMaxThrdBx10_Type = Integer32
_Mpbc2RULDP1stWLOutputPwrMaxThrdBx10_Object = MibScalar
mpbc2RULDP1stWLOutputPwrMaxThrdBx10 = _Mpbc2RULDP1stWLOutputPwrMaxThrdBx10_Object(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 11, 3, 12),
    _Mpbc2RULDP1stWLOutputPwrMaxThrdBx10_Type()
)
mpbc2RULDP1stWLOutputPwrMaxThrdBx10.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mpbc2RULDP1stWLOutputPwrMaxThrdBx10.setStatus("current")
_Mpbc2RULDP2ndWLOutputPwrMinThrdBx10_Type = Integer32
_Mpbc2RULDP2ndWLOutputPwrMinThrdBx10_Object = MibScalar
mpbc2RULDP2ndWLOutputPwrMinThrdBx10 = _Mpbc2RULDP2ndWLOutputPwrMinThrdBx10_Object(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 11, 3, 13),
    _Mpbc2RULDP2ndWLOutputPwrMinThrdBx10_Type()
)
mpbc2RULDP2ndWLOutputPwrMinThrdBx10.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mpbc2RULDP2ndWLOutputPwrMinThrdBx10.setStatus("current")
_Mpbc2RULDP2ndWLOutputPwrMaxThrdBx10_Type = Integer32
_Mpbc2RULDP2ndWLOutputPwrMaxThrdBx10_Object = MibScalar
mpbc2RULDP2ndWLOutputPwrMaxThrdBx10 = _Mpbc2RULDP2ndWLOutputPwrMaxThrdBx10_Object(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 11, 3, 14),
    _Mpbc2RULDP2ndWLOutputPwrMaxThrdBx10_Type()
)
mpbc2RULDP2ndWLOutputPwrMaxThrdBx10.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mpbc2RULDP2ndWLOutputPwrMaxThrdBx10.setStatus("current")
_Mpbc2RULDP1stWLOutputPwrMinLimdBmx10_Type = Integer32
_Mpbc2RULDP1stWLOutputPwrMinLimdBmx10_Object = MibScalar
mpbc2RULDP1stWLOutputPwrMinLimdBmx10 = _Mpbc2RULDP1stWLOutputPwrMinLimdBmx10_Object(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 11, 3, 15),
    _Mpbc2RULDP1stWLOutputPwrMinLimdBmx10_Type()
)
mpbc2RULDP1stWLOutputPwrMinLimdBmx10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpbc2RULDP1stWLOutputPwrMinLimdBmx10.setStatus("current")
_Mpbc2RULDP1stWLOutputPwrMaxLimdBmx10_Type = Integer32
_Mpbc2RULDP1stWLOutputPwrMaxLimdBmx10_Object = MibScalar
mpbc2RULDP1stWLOutputPwrMaxLimdBmx10 = _Mpbc2RULDP1stWLOutputPwrMaxLimdBmx10_Object(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 11, 3, 16),
    _Mpbc2RULDP1stWLOutputPwrMaxLimdBmx10_Type()
)
mpbc2RULDP1stWLOutputPwrMaxLimdBmx10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpbc2RULDP1stWLOutputPwrMaxLimdBmx10.setStatus("current")
_Mpbc2RULDP2ndWLOutputPwrMinLimdBmx10_Type = Integer32
_Mpbc2RULDP2ndWLOutputPwrMinLimdBmx10_Object = MibScalar
mpbc2RULDP2ndWLOutputPwrMinLimdBmx10 = _Mpbc2RULDP2ndWLOutputPwrMinLimdBmx10_Object(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 11, 3, 17),
    _Mpbc2RULDP2ndWLOutputPwrMinLimdBmx10_Type()
)
mpbc2RULDP2ndWLOutputPwrMinLimdBmx10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpbc2RULDP2ndWLOutputPwrMinLimdBmx10.setStatus("current")
_Mpbc2RULDP2ndWLOutputPwrMaxLimdBmx10_Type = Integer32
_Mpbc2RULDP2ndWLOutputPwrMaxLimdBmx10_Object = MibScalar
mpbc2RULDP2ndWLOutputPwrMaxLimdBmx10 = _Mpbc2RULDP2ndWLOutputPwrMaxLimdBmx10_Object(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 11, 3, 18),
    _Mpbc2RULDP2ndWLOutputPwrMaxLimdBmx10_Type()
)
mpbc2RULDP2ndWLOutputPwrMaxLimdBmx10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpbc2RULDP2ndWLOutputPwrMaxLimdBmx10.setStatus("current")
_Mpbc2RUConfiguration_ObjectIdentity = ObjectIdentity
mpbc2RUConfiguration = _Mpbc2RUConfiguration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 12)
)
_Mpbc2RUNetMgt_ObjectIdentity = ObjectIdentity
mpbc2RUNetMgt = _Mpbc2RUNetMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 12, 1)
)
_Mpbc2RUNotifiedNMSipAddressTable_Object = MibTable
mpbc2RUNotifiedNMSipAddressTable = _Mpbc2RUNotifiedNMSipAddressTable_Object(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 12, 1, 1)
)
if mibBuilder.loadTexts:
    mpbc2RUNotifiedNMSipAddressTable.setStatus("current")
_Mpbc2RUNotifiedNMSipAddressEntry_Object = MibTableRow
mpbc2RUNotifiedNMSipAddressEntry = _Mpbc2RUNotifiedNMSipAddressEntry_Object(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 12, 1, 1, 1)
)
mpbc2RUNotifiedNMSipAddressEntry.setIndexNames(
    (0, "MPBC-2RU-MIB", "mpbc2RUNotifiedNMSipAddressIndex"),
)
if mibBuilder.loadTexts:
    mpbc2RUNotifiedNMSipAddressEntry.setStatus("current")
_Mpbc2RUNotifiedNMSipAddressIndex_Type = Integer32
_Mpbc2RUNotifiedNMSipAddressIndex_Object = MibTableColumn
mpbc2RUNotifiedNMSipAddressIndex = _Mpbc2RUNotifiedNMSipAddressIndex_Object(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 12, 1, 1, 1, 1),
    _Mpbc2RUNotifiedNMSipAddressIndex_Type()
)
mpbc2RUNotifiedNMSipAddressIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mpbc2RUNotifiedNMSipAddressIndex.setStatus("current")
_Mpbc2RUNotifiedNMSipAddress_IP_Type = IpAddress
_Mpbc2RUNotifiedNMSipAddress_IP_Object = MibTableColumn
mpbc2RUNotifiedNMSipAddress_IP = _Mpbc2RUNotifiedNMSipAddress_IP_Object(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 12, 1, 1, 1, 2),
    _Mpbc2RUNotifiedNMSipAddress_IP_Type()
)
mpbc2RUNotifiedNMSipAddress_IP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mpbc2RUNotifiedNMSipAddress_IP.setStatus("current")
_Mpbc2RUNotifiedNMSipAddress_Description_Type = OctetString
_Mpbc2RUNotifiedNMSipAddress_Description_Object = MibTableColumn
mpbc2RUNotifiedNMSipAddress_Description = _Mpbc2RUNotifiedNMSipAddress_Description_Object(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 12, 1, 1, 1, 3),
    _Mpbc2RUNotifiedNMSipAddress_Description_Type()
)
mpbc2RUNotifiedNMSipAddress_Description.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mpbc2RUNotifiedNMSipAddress_Description.setStatus("current")
_Mpbc2RUNotifiedNMSipAddress_Enabled_Type = TruthValue
_Mpbc2RUNotifiedNMSipAddress_Enabled_Object = MibTableColumn
mpbc2RUNotifiedNMSipAddress_Enabled = _Mpbc2RUNotifiedNMSipAddress_Enabled_Object(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 12, 1, 1, 1, 4),
    _Mpbc2RUNotifiedNMSipAddress_Enabled_Type()
)
mpbc2RUNotifiedNMSipAddress_Enabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mpbc2RUNotifiedNMSipAddress_Enabled.setStatus("current")
_Mpbc2RUAckTrapControl_ObjectIdentity = ObjectIdentity
mpbc2RUAckTrapControl = _Mpbc2RUAckTrapControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 12, 1, 2)
)
_Mpbc2RUAckTrapCriticalEnable_Type = TruthValue
_Mpbc2RUAckTrapCriticalEnable_Object = MibScalar
mpbc2RUAckTrapCriticalEnable = _Mpbc2RUAckTrapCriticalEnable_Object(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 12, 1, 2, 1),
    _Mpbc2RUAckTrapCriticalEnable_Type()
)
mpbc2RUAckTrapCriticalEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mpbc2RUAckTrapCriticalEnable.setStatus("current")


class _Mpbc2RUAckTrapCriticalRetries_Type(Unsigned32):
    """Custom type mpbc2RUAckTrapCriticalRetries based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_Mpbc2RUAckTrapCriticalRetries_Type.__name__ = "Unsigned32"
_Mpbc2RUAckTrapCriticalRetries_Object = MibScalar
mpbc2RUAckTrapCriticalRetries = _Mpbc2RUAckTrapCriticalRetries_Object(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 12, 1, 2, 2),
    _Mpbc2RUAckTrapCriticalRetries_Type()
)
mpbc2RUAckTrapCriticalRetries.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mpbc2RUAckTrapCriticalRetries.setStatus("current")
_Mpbc2RUAckTrapCriticalTimeOutsec_Type = Unsigned32
_Mpbc2RUAckTrapCriticalTimeOutsec_Object = MibScalar
mpbc2RUAckTrapCriticalTimeOutsec = _Mpbc2RUAckTrapCriticalTimeOutsec_Object(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 12, 1, 2, 3),
    _Mpbc2RUAckTrapCriticalTimeOutsec_Type()
)
mpbc2RUAckTrapCriticalTimeOutsec.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mpbc2RUAckTrapCriticalTimeOutsec.setStatus("current")
_Mpbc2RUAckTrapMajorEnable_Type = TruthValue
_Mpbc2RUAckTrapMajorEnable_Object = MibScalar
mpbc2RUAckTrapMajorEnable = _Mpbc2RUAckTrapMajorEnable_Object(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 12, 1, 2, 4),
    _Mpbc2RUAckTrapMajorEnable_Type()
)
mpbc2RUAckTrapMajorEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mpbc2RUAckTrapMajorEnable.setStatus("current")


class _Mpbc2RUAckTrapMajorRetries_Type(Unsigned32):
    """Custom type mpbc2RUAckTrapMajorRetries based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_Mpbc2RUAckTrapMajorRetries_Type.__name__ = "Unsigned32"
_Mpbc2RUAckTrapMajorRetries_Object = MibScalar
mpbc2RUAckTrapMajorRetries = _Mpbc2RUAckTrapMajorRetries_Object(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 12, 1, 2, 5),
    _Mpbc2RUAckTrapMajorRetries_Type()
)
mpbc2RUAckTrapMajorRetries.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mpbc2RUAckTrapMajorRetries.setStatus("current")


class _Mpbc2RUAckTrapMajorTimeOutsec_Type(Unsigned32):
    """Custom type mpbc2RUAckTrapMajorTimeOutsec based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_Mpbc2RUAckTrapMajorTimeOutsec_Type.__name__ = "Unsigned32"
_Mpbc2RUAckTrapMajorTimeOutsec_Object = MibScalar
mpbc2RUAckTrapMajorTimeOutsec = _Mpbc2RUAckTrapMajorTimeOutsec_Object(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 12, 1, 2, 6),
    _Mpbc2RUAckTrapMajorTimeOutsec_Type()
)
mpbc2RUAckTrapMajorTimeOutsec.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mpbc2RUAckTrapMajorTimeOutsec.setStatus("current")
_Mpbc2RUAckTrapMinorEnable_Type = TruthValue
_Mpbc2RUAckTrapMinorEnable_Object = MibScalar
mpbc2RUAckTrapMinorEnable = _Mpbc2RUAckTrapMinorEnable_Object(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 12, 1, 2, 7),
    _Mpbc2RUAckTrapMinorEnable_Type()
)
mpbc2RUAckTrapMinorEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mpbc2RUAckTrapMinorEnable.setStatus("current")


class _Mpbc2RUAckTrapMinorRetries_Type(Unsigned32):
    """Custom type mpbc2RUAckTrapMinorRetries based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_Mpbc2RUAckTrapMinorRetries_Type.__name__ = "Unsigned32"
_Mpbc2RUAckTrapMinorRetries_Object = MibScalar
mpbc2RUAckTrapMinorRetries = _Mpbc2RUAckTrapMinorRetries_Object(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 12, 1, 2, 8),
    _Mpbc2RUAckTrapMinorRetries_Type()
)
mpbc2RUAckTrapMinorRetries.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mpbc2RUAckTrapMinorRetries.setStatus("current")


class _Mpbc2RUAckTrapMinorTimeOutsec_Type(Unsigned32):
    """Custom type mpbc2RUAckTrapMinorTimeOutsec based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_Mpbc2RUAckTrapMinorTimeOutsec_Type.__name__ = "Unsigned32"
_Mpbc2RUAckTrapMinorTimeOutsec_Object = MibScalar
mpbc2RUAckTrapMinorTimeOutsec = _Mpbc2RUAckTrapMinorTimeOutsec_Object(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 12, 1, 2, 9),
    _Mpbc2RUAckTrapMinorTimeOutsec_Type()
)
mpbc2RUAckTrapMinorTimeOutsec.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mpbc2RUAckTrapMinorTimeOutsec.setStatus("current")
_Mpbc2RUAckTrapInformationalEnable_Type = TruthValue
_Mpbc2RUAckTrapInformationalEnable_Object = MibScalar
mpbc2RUAckTrapInformationalEnable = _Mpbc2RUAckTrapInformationalEnable_Object(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 12, 1, 2, 10),
    _Mpbc2RUAckTrapInformationalEnable_Type()
)
mpbc2RUAckTrapInformationalEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mpbc2RUAckTrapInformationalEnable.setStatus("current")


class _Mpbc2RUAckTrapInformationalRetries_Type(Unsigned32):
    """Custom type mpbc2RUAckTrapInformationalRetries based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_Mpbc2RUAckTrapInformationalRetries_Type.__name__ = "Unsigned32"
_Mpbc2RUAckTrapInformationalRetries_Object = MibScalar
mpbc2RUAckTrapInformationalRetries = _Mpbc2RUAckTrapInformationalRetries_Object(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 12, 1, 2, 11),
    _Mpbc2RUAckTrapInformationalRetries_Type()
)
mpbc2RUAckTrapInformationalRetries.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mpbc2RUAckTrapInformationalRetries.setStatus("current")


class _Mpbc2RUAckTrapInformationalTimeOutsec_Type(Unsigned32):
    """Custom type mpbc2RUAckTrapInformationalTimeOutsec based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_Mpbc2RUAckTrapInformationalTimeOutsec_Type.__name__ = "Unsigned32"
_Mpbc2RUAckTrapInformationalTimeOutsec_Object = MibScalar
mpbc2RUAckTrapInformationalTimeOutsec = _Mpbc2RUAckTrapInformationalTimeOutsec_Object(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 12, 1, 2, 12),
    _Mpbc2RUAckTrapInformationalTimeOutsec_Type()
)
mpbc2RUAckTrapInformationalTimeOutsec.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mpbc2RUAckTrapInformationalTimeOutsec.setStatus("current")
_Mpbc2RUTrapControl_ObjectIdentity = ObjectIdentity
mpbc2RUTrapControl = _Mpbc2RUTrapControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 12, 1, 3)
)
_Mpbc2RUTrapCriticalEnable_Type = TruthValue
_Mpbc2RUTrapCriticalEnable_Object = MibScalar
mpbc2RUTrapCriticalEnable = _Mpbc2RUTrapCriticalEnable_Object(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 12, 1, 3, 1),
    _Mpbc2RUTrapCriticalEnable_Type()
)
mpbc2RUTrapCriticalEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mpbc2RUTrapCriticalEnable.setStatus("current")
_Mpbc2RUTrapMajorEnable_Type = TruthValue
_Mpbc2RUTrapMajorEnable_Object = MibScalar
mpbc2RUTrapMajorEnable = _Mpbc2RUTrapMajorEnable_Object(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 12, 1, 3, 2),
    _Mpbc2RUTrapMajorEnable_Type()
)
mpbc2RUTrapMajorEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mpbc2RUTrapMajorEnable.setStatus("current")
_Mpbc2RUTrapMinorEnable_Type = TruthValue
_Mpbc2RUTrapMinorEnable_Object = MibScalar
mpbc2RUTrapMinorEnable = _Mpbc2RUTrapMinorEnable_Object(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 12, 1, 3, 3),
    _Mpbc2RUTrapMinorEnable_Type()
)
mpbc2RUTrapMinorEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mpbc2RUTrapMinorEnable.setStatus("current")
_Mpbc2RUTrapInformationalEnable_Type = TruthValue
_Mpbc2RUTrapInformationalEnable_Object = MibScalar
mpbc2RUTrapInformationalEnable = _Mpbc2RUTrapInformationalEnable_Object(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 12, 1, 3, 4),
    _Mpbc2RUTrapInformationalEnable_Type()
)
mpbc2RUTrapInformationalEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mpbc2RUTrapInformationalEnable.setStatus("current")
_Mpbc2RUMacAddress_Type = OctetString
_Mpbc2RUMacAddress_Object = MibScalar
mpbc2RUMacAddress = _Mpbc2RUMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 12, 1, 4),
    _Mpbc2RUMacAddress_Type()
)
mpbc2RUMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpbc2RUMacAddress.setStatus("current")
_Mpbc2RUEthernetIPaddress_Type = IpAddress
_Mpbc2RUEthernetIPaddress_Object = MibScalar
mpbc2RUEthernetIPaddress = _Mpbc2RUEthernetIPaddress_Object(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 12, 1, 5),
    _Mpbc2RUEthernetIPaddress_Type()
)
mpbc2RUEthernetIPaddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mpbc2RUEthernetIPaddress.setStatus("current")
_Mpbc2RUEthernetIPsubNetMask_Type = IpAddress
_Mpbc2RUEthernetIPsubNetMask_Object = MibScalar
mpbc2RUEthernetIPsubNetMask = _Mpbc2RUEthernetIPsubNetMask_Object(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 12, 1, 6),
    _Mpbc2RUEthernetIPsubNetMask_Type()
)
mpbc2RUEthernetIPsubNetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mpbc2RUEthernetIPsubNetMask.setStatus("current")
_Mpbc2RUDefaultGateway_Type = IpAddress
_Mpbc2RUDefaultGateway_Object = MibScalar
mpbc2RUDefaultGateway = _Mpbc2RUDefaultGateway_Object(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 12, 1, 7),
    _Mpbc2RUDefaultGateway_Type()
)
mpbc2RUDefaultGateway.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mpbc2RUDefaultGateway.setStatus("current")


class _Mpbc2RUSnmpTrapPort_Type(Integer32):
    """Custom type mpbc2RUSnmpTrapPort based on Integer32"""
    defaultValue = 161


_Mpbc2RUSnmpTrapPort_Type.__name__ = "Integer32"
_Mpbc2RUSnmpTrapPort_Object = MibScalar
mpbc2RUSnmpTrapPort = _Mpbc2RUSnmpTrapPort_Object(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 12, 1, 8),
    _Mpbc2RUSnmpTrapPort_Type()
)
mpbc2RUSnmpTrapPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpbc2RUSnmpTrapPort.setStatus("current")
_Mpbc2RUNE_ObjectIdentity = ObjectIdentity
mpbc2RUNE = _Mpbc2RUNE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 12, 2)
)
_Mpbc2RUNEID_Type = OctetString
_Mpbc2RUNEID_Object = MibScalar
mpbc2RUNEID = _Mpbc2RUNEID_Object(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 12, 2, 1),
    _Mpbc2RUNEID_Type()
)
mpbc2RUNEID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpbc2RUNEID.setStatus("current")
_Mpbc2RUInfoTable_Object = MibTable
mpbc2RUInfoTable = _Mpbc2RUInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 12, 2, 2)
)
if mibBuilder.loadTexts:
    mpbc2RUInfoTable.setStatus("current")
_Mpbc2RUInfoEntry_Object = MibTableRow
mpbc2RUInfoEntry = _Mpbc2RUInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 12, 2, 2, 1)
)
mpbc2RUInfoEntry.setIndexNames(
    (0, "MPBC-2RU-MIB", "mpbc2RUInfoIndex"),
)
if mibBuilder.loadTexts:
    mpbc2RUInfoEntry.setStatus("current")
_Mpbc2RUInfoIndex_Type = Integer32
_Mpbc2RUInfoIndex_Object = MibTableColumn
mpbc2RUInfoIndex = _Mpbc2RUInfoIndex_Object(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 12, 2, 2, 1, 1),
    _Mpbc2RUInfoIndex_Type()
)
mpbc2RUInfoIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mpbc2RUInfoIndex.setStatus("current")
_Mpbc2RUInfoLoc_Type = OctetString
_Mpbc2RUInfoLoc_Object = MibTableColumn
mpbc2RUInfoLoc = _Mpbc2RUInfoLoc_Object(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 12, 2, 2, 1, 2),
    _Mpbc2RUInfoLoc_Type()
)
mpbc2RUInfoLoc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpbc2RUInfoLoc.setStatus("current")
_Mpbc2RUInfoModelNum_Type = OctetString
_Mpbc2RUInfoModelNum_Object = MibTableColumn
mpbc2RUInfoModelNum = _Mpbc2RUInfoModelNum_Object(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 12, 2, 2, 1, 3),
    _Mpbc2RUInfoModelNum_Type()
)
mpbc2RUInfoModelNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpbc2RUInfoModelNum.setStatus("current")
_Mpbc2RUInfoModelSN_Type = OctetString
_Mpbc2RUInfoModelSN_Object = MibTableColumn
mpbc2RUInfoModelSN = _Mpbc2RUInfoModelSN_Object(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 12, 2, 2, 1, 4),
    _Mpbc2RUInfoModelSN_Type()
)
mpbc2RUInfoModelSN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpbc2RUInfoModelSN.setStatus("current")
_Mpbc2RUInfoOEMPartNum_Type = OctetString
_Mpbc2RUInfoOEMPartNum_Object = MibTableColumn
mpbc2RUInfoOEMPartNum = _Mpbc2RUInfoOEMPartNum_Object(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 12, 2, 2, 1, 5),
    _Mpbc2RUInfoOEMPartNum_Type()
)
mpbc2RUInfoOEMPartNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpbc2RUInfoOEMPartNum.setStatus("current")
_Mpbc2RUInfoAssyNum_Type = OctetString
_Mpbc2RUInfoAssyNum_Object = MibTableColumn
mpbc2RUInfoAssyNum = _Mpbc2RUInfoAssyNum_Object(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 12, 2, 2, 1, 6),
    _Mpbc2RUInfoAssyNum_Type()
)
mpbc2RUInfoAssyNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpbc2RUInfoAssyNum.setStatus("current")
_Mpbc2RUInfoRev_Type = OctetString
_Mpbc2RUInfoRev_Object = MibTableColumn
mpbc2RUInfoRev = _Mpbc2RUInfoRev_Object(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 12, 2, 2, 1, 7),
    _Mpbc2RUInfoRev_Type()
)
mpbc2RUInfoRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpbc2RUInfoRev.setStatus("current")
_Mpbc2RUInfoECN_Type = OctetString
_Mpbc2RUInfoECN_Object = MibTableColumn
mpbc2RUInfoECN = _Mpbc2RUInfoECN_Object(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 12, 2, 2, 1, 8),
    _Mpbc2RUInfoECN_Type()
)
mpbc2RUInfoECN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpbc2RUInfoECN.setStatus("current")
_Mpbc2RUInfoSeqNum_Type = OctetString
_Mpbc2RUInfoSeqNum_Object = MibTableColumn
mpbc2RUInfoSeqNum = _Mpbc2RUInfoSeqNum_Object(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 12, 2, 2, 1, 9),
    _Mpbc2RUInfoSeqNum_Type()
)
mpbc2RUInfoSeqNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpbc2RUInfoSeqNum.setStatus("current")
_Mpbc2RUInfoMfgDate_Type = OctetString
_Mpbc2RUInfoMfgDate_Object = MibTableColumn
mpbc2RUInfoMfgDate = _Mpbc2RUInfoMfgDate_Object(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 12, 2, 2, 1, 10),
    _Mpbc2RUInfoMfgDate_Type()
)
mpbc2RUInfoMfgDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpbc2RUInfoMfgDate.setStatus("current")
_Mpbc2RUInfoSwVer_Type = OctetString
_Mpbc2RUInfoSwVer_Object = MibTableColumn
mpbc2RUInfoSwVer = _Mpbc2RUInfoSwVer_Object(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 12, 2, 2, 1, 11),
    _Mpbc2RUInfoSwVer_Type()
)
mpbc2RUInfoSwVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpbc2RUInfoSwVer.setStatus("current")
_Mpbc2RUInfoBootLoaderRev_Type = OctetString
_Mpbc2RUInfoBootLoaderRev_Object = MibTableColumn
mpbc2RUInfoBootLoaderRev = _Mpbc2RUInfoBootLoaderRev_Object(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 12, 2, 2, 1, 12),
    _Mpbc2RUInfoBootLoaderRev_Type()
)
mpbc2RUInfoBootLoaderRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpbc2RUInfoBootLoaderRev.setStatus("current")
_Mpbc2RUInfoLibRev_Type = OctetString
_Mpbc2RUInfoLibRev_Object = MibTableColumn
mpbc2RUInfoLibRev = _Mpbc2RUInfoLibRev_Object(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 12, 2, 2, 1, 13),
    _Mpbc2RUInfoLibRev_Type()
)
mpbc2RUInfoLibRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpbc2RUInfoLibRev.setStatus("current")
_Mpbc2RUInfoLddFw1_Type = OctetString
_Mpbc2RUInfoLddFw1_Object = MibTableColumn
mpbc2RUInfoLddFw1 = _Mpbc2RUInfoLddFw1_Object(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 12, 2, 2, 1, 14),
    _Mpbc2RUInfoLddFw1_Type()
)
mpbc2RUInfoLddFw1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpbc2RUInfoLddFw1.setStatus("current")
_Mpbc2RUInfoLddFw2_Type = OctetString
_Mpbc2RUInfoLddFw2_Object = MibTableColumn
mpbc2RUInfoLddFw2 = _Mpbc2RUInfoLddFw2_Object(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 12, 2, 2, 1, 15),
    _Mpbc2RUInfoLddFw2_Type()
)
mpbc2RUInfoLddFw2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpbc2RUInfoLddFw2.setStatus("current")
_Mpbc2RUInfoCLEI_Type = OctetString
_Mpbc2RUInfoCLEI_Object = MibTableColumn
mpbc2RUInfoCLEI = _Mpbc2RUInfoCLEI_Object(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 12, 2, 2, 1, 16),
    _Mpbc2RUInfoCLEI_Type()
)
mpbc2RUInfoCLEI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpbc2RUInfoCLEI.setStatus("current")
_Mpbc2RUInfoLastRmaDate_Type = OctetString
_Mpbc2RUInfoLastRmaDate_Object = MibTableColumn
mpbc2RUInfoLastRmaDate = _Mpbc2RUInfoLastRmaDate_Object(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 12, 2, 2, 1, 17),
    _Mpbc2RUInfoLastRmaDate_Type()
)
mpbc2RUInfoLastRmaDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpbc2RUInfoLastRmaDate.setStatus("current")
_Mpbc2RUDateTime_Type = OctetString
_Mpbc2RUDateTime_Object = MibScalar
mpbc2RUDateTime = _Mpbc2RUDateTime_Object(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 12, 2, 3),
    _Mpbc2RUDateTime_Type()
)
mpbc2RUDateTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mpbc2RUDateTime.setStatus("current")
_Mpbc2RUSNMPAgentVersion_Type = OctetString
_Mpbc2RUSNMPAgentVersion_Object = MibScalar
mpbc2RUSNMPAgentVersion = _Mpbc2RUSNMPAgentVersion_Object(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 12, 2, 4),
    _Mpbc2RUSNMPAgentVersion_Type()
)
mpbc2RUSNMPAgentVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpbc2RUSNMPAgentVersion.setStatus("current")


class _Mpbc2RUSNMPMIBVersion_Type(OctetString):
    """Custom type mpbc2RUSNMPMIBVersion based on OctetString"""
    defaultValue = OctetString("2RU_MIB_VERSION 1.1.2.0")


_Mpbc2RUSNMPMIBVersion_Type.__name__ = "OctetString"
_Mpbc2RUSNMPMIBVersion_Object = MibScalar
mpbc2RUSNMPMIBVersion = _Mpbc2RUSNMPMIBVersion_Object(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 12, 2, 5),
    _Mpbc2RUSNMPMIBVersion_Type()
)
mpbc2RUSNMPMIBVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpbc2RUSNMPMIBVersion.setStatus("current")
_Mpbc2RUSNMPMemoryConfig_ObjectIdentity = ObjectIdentity
mpbc2RUSNMPMemoryConfig = _Mpbc2RUSNMPMemoryConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 12, 3)
)


class _Mpbc2RUSNMPMemorySave_Type(TruthValue):
    """Custom type mpbc2RUSNMPMemorySave based on TruthValue"""
    defaultValue = 2


_Mpbc2RUSNMPMemorySave_Type.__name__ = "TruthValue"
_Mpbc2RUSNMPMemorySave_Object = MibScalar
mpbc2RUSNMPMemorySave = _Mpbc2RUSNMPMemorySave_Object(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 12, 3, 1),
    _Mpbc2RUSNMPMemorySave_Type()
)
mpbc2RUSNMPMemorySave.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mpbc2RUSNMPMemorySave.setStatus("current")


class _Mpbc2RUSNMPMemoryRestore_Type(TruthValue):
    """Custom type mpbc2RUSNMPMemoryRestore based on TruthValue"""
    defaultValue = 2


_Mpbc2RUSNMPMemoryRestore_Type.__name__ = "TruthValue"
_Mpbc2RUSNMPMemoryRestore_Object = MibScalar
mpbc2RUSNMPMemoryRestore = _Mpbc2RUSNMPMemoryRestore_Object(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 12, 3, 2),
    _Mpbc2RUSNMPMemoryRestore_Type()
)
mpbc2RUSNMPMemoryRestore.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mpbc2RUSNMPMemoryRestore.setStatus("current")
_Mpbc2RUConformance_ObjectIdentity = ObjectIdentity
mpbc2RUConformance = _Mpbc2RUConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 13)
)
_Mpbc2RUGroups_ObjectIdentity = ObjectIdentity
mpbc2RUGroups = _Mpbc2RUGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 13, 1)
)
_Mpbc2RUMLDS_ObjectIdentity = ObjectIdentity
mpbc2RUMLDS = _Mpbc2RUMLDS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 14)
)
_Mpbc2RUMLDSControl_ObjectIdentity = ObjectIdentity
mpbc2RUMLDSControl = _Mpbc2RUMLDSControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 14, 1)
)


class _Mpbc2RUMLDSLaserMode_Type(Integer32):
    """Custom type mpbc2RUMLDSLaserMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("laserOff", 0),
          ("laserAPR", 1))
    )


_Mpbc2RUMLDSLaserMode_Type.__name__ = "Integer32"
_Mpbc2RUMLDSLaserMode_Object = MibScalar
mpbc2RUMLDSLaserMode = _Mpbc2RUMLDSLaserMode_Object(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 14, 1, 1),
    _Mpbc2RUMLDSLaserMode_Type()
)
mpbc2RUMLDSLaserMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mpbc2RUMLDSLaserMode.setStatus("current")
_Mpbc2RUMLDSControlMode_Type = Unsigned32
_Mpbc2RUMLDSControlMode_Object = MibScalar
mpbc2RUMLDSControlMode = _Mpbc2RUMLDSControlMode_Object(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 14, 1, 2),
    _Mpbc2RUMLDSControlMode_Type()
)
mpbc2RUMLDSControlMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mpbc2RUMLDSControlMode.setStatus("current")
_Mpbc2RUMLDS3rdWLPwrSetPtmW_Type = Unsigned32
_Mpbc2RUMLDS3rdWLPwrSetPtmW_Object = MibScalar
mpbc2RUMLDS3rdWLPwrSetPtmW = _Mpbc2RUMLDS3rdWLPwrSetPtmW_Object(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 14, 1, 3),
    _Mpbc2RUMLDS3rdWLPwrSetPtmW_Type()
)
mpbc2RUMLDS3rdWLPwrSetPtmW.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mpbc2RUMLDS3rdWLPwrSetPtmW.setStatus("current")
_Mpbc2RUMLDS4thWLPwrSetPtmW_Type = Unsigned32
_Mpbc2RUMLDS4thWLPwrSetPtmW_Object = MibScalar
mpbc2RUMLDS4thWLPwrSetPtmW = _Mpbc2RUMLDS4thWLPwrSetPtmW_Object(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 14, 1, 4),
    _Mpbc2RUMLDS4thWLPwrSetPtmW_Type()
)
mpbc2RUMLDS4thWLPwrSetPtmW.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mpbc2RUMLDS4thWLPwrSetPtmW.setStatus("current")
_Mpbc2RUMLDSReset_Type = TruthValue
_Mpbc2RUMLDSReset_Object = MibScalar
mpbc2RUMLDSReset = _Mpbc2RUMLDSReset_Object(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 14, 1, 5),
    _Mpbc2RUMLDSReset_Type()
)
mpbc2RUMLDSReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mpbc2RUMLDSReset.setStatus("current")
_Mpbc2RUMLDSMonitor_ObjectIdentity = ObjectIdentity
mpbc2RUMLDSMonitor = _Mpbc2RUMLDSMonitor_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 14, 2)
)
_Mpbc2RUMLDSLD1CurmA_Type = Unsigned32
_Mpbc2RUMLDSLD1CurmA_Object = MibScalar
mpbc2RUMLDSLD1CurmA = _Mpbc2RUMLDSLD1CurmA_Object(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 14, 2, 1),
    _Mpbc2RUMLDSLD1CurmA_Type()
)
mpbc2RUMLDSLD1CurmA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpbc2RUMLDSLD1CurmA.setStatus("current")
_Mpbc2RUMLDSLD1TempDegCx10_Type = Integer32
_Mpbc2RUMLDSLD1TempDegCx10_Object = MibScalar
mpbc2RUMLDSLD1TempDegCx10 = _Mpbc2RUMLDSLD1TempDegCx10_Object(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 14, 2, 2),
    _Mpbc2RUMLDSLD1TempDegCx10_Type()
)
mpbc2RUMLDSLD1TempDegCx10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpbc2RUMLDSLD1TempDegCx10.setStatus("current")
_Mpbc2RUMLDSLD1TECCurmA_Type = Unsigned32
_Mpbc2RUMLDSLD1TECCurmA_Object = MibScalar
mpbc2RUMLDSLD1TECCurmA = _Mpbc2RUMLDSLD1TECCurmA_Object(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 14, 2, 3),
    _Mpbc2RUMLDSLD1TECCurmA_Type()
)
mpbc2RUMLDSLD1TECCurmA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpbc2RUMLDSLD1TECCurmA.setStatus("current")
_Mpbc2RUMLDSLD2CurmA_Type = Unsigned32
_Mpbc2RUMLDSLD2CurmA_Object = MibScalar
mpbc2RUMLDSLD2CurmA = _Mpbc2RUMLDSLD2CurmA_Object(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 14, 2, 4),
    _Mpbc2RUMLDSLD2CurmA_Type()
)
mpbc2RUMLDSLD2CurmA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpbc2RUMLDSLD2CurmA.setStatus("current")
_Mpbc2RUMLDSLD2TempDegCx10_Type = Integer32
_Mpbc2RUMLDSLD2TempDegCx10_Object = MibScalar
mpbc2RUMLDSLD2TempDegCx10 = _Mpbc2RUMLDSLD2TempDegCx10_Object(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 14, 2, 5),
    _Mpbc2RUMLDSLD2TempDegCx10_Type()
)
mpbc2RUMLDSLD2TempDegCx10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpbc2RUMLDSLD2TempDegCx10.setStatus("current")
_Mpbc2RUMLDSLD2TECCurmA_Type = Unsigned32
_Mpbc2RUMLDSLD2TECCurmA_Object = MibScalar
mpbc2RUMLDSLD2TECCurmA = _Mpbc2RUMLDSLD2TECCurmA_Object(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 14, 2, 6),
    _Mpbc2RUMLDSLD2TECCurmA_Type()
)
mpbc2RUMLDSLD2TECCurmA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpbc2RUMLDSLD2TECCurmA.setStatus("current")
_Mpbc2RUMLDSCaseTempDegCx10_Type = Integer32
_Mpbc2RUMLDSCaseTempDegCx10_Object = MibScalar
mpbc2RUMLDSCaseTempDegCx10 = _Mpbc2RUMLDSCaseTempDegCx10_Object(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 14, 2, 7),
    _Mpbc2RUMLDSCaseTempDegCx10_Type()
)
mpbc2RUMLDSCaseTempDegCx10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpbc2RUMLDSCaseTempDegCx10.setStatus("current")
_Mpbc2RUMLDSMon3rdWLOutputPwrmW_Type = Unsigned32
_Mpbc2RUMLDSMon3rdWLOutputPwrmW_Object = MibScalar
mpbc2RUMLDSMon3rdWLOutputPwrmW = _Mpbc2RUMLDSMon3rdWLOutputPwrmW_Object(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 14, 2, 8),
    _Mpbc2RUMLDSMon3rdWLOutputPwrmW_Type()
)
mpbc2RUMLDSMon3rdWLOutputPwrmW.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpbc2RUMLDSMon3rdWLOutputPwrmW.setStatus("current")
_Mpbc2RUMLDSMon4thWLOutputPwrmW_Type = Unsigned32
_Mpbc2RUMLDSMon4thWLOutputPwrmW_Object = MibScalar
mpbc2RUMLDSMon4thWLOutputPwrmW = _Mpbc2RUMLDSMon4thWLOutputPwrmW_Object(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 14, 2, 9),
    _Mpbc2RUMLDSMon4thWLOutputPwrmW_Type()
)
mpbc2RUMLDSMon4thWLOutputPwrmW.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpbc2RUMLDSMon4thWLOutputPwrmW.setStatus("current")
_Mpbc2RUMLDSMonTotalOutputPwrmW_Type = Unsigned32
_Mpbc2RUMLDSMonTotalOutputPwrmW_Object = MibScalar
mpbc2RUMLDSMonTotalOutputPwrmW = _Mpbc2RUMLDSMonTotalOutputPwrmW_Object(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 14, 2, 10),
    _Mpbc2RUMLDSMonTotalOutputPwrmW_Type()
)
mpbc2RUMLDSMonTotalOutputPwrmW.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpbc2RUMLDSMonTotalOutputPwrmW.setStatus("current")
_Mpbc2RUMLDSInputPwrmW_Type = Unsigned32
_Mpbc2RUMLDSInputPwrmW_Object = MibScalar
mpbc2RUMLDSInputPwrmW = _Mpbc2RUMLDSInputPwrmW_Object(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 14, 2, 11),
    _Mpbc2RUMLDSInputPwrmW_Type()
)
mpbc2RUMLDSInputPwrmW.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpbc2RUMLDSInputPwrmW.setStatus("current")


class _Mpbc2RUMLDSMonLaserState_Type(Integer32):
    """Custom type mpbc2RUMLDSMonLaserState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              10)
        )
    )
    namedValues = NamedValues(
        *(("laserOff", 0),
          ("laserNormal", 1),
          ("laserALS", 2),
          ("laserALS100", 3),
          ("laserOn", 10))
    )


_Mpbc2RUMLDSMonLaserState_Type.__name__ = "Integer32"
_Mpbc2RUMLDSMonLaserState_Object = MibScalar
mpbc2RUMLDSMonLaserState = _Mpbc2RUMLDSMonLaserState_Object(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 14, 2, 12),
    _Mpbc2RUMLDSMonLaserState_Type()
)
mpbc2RUMLDSMonLaserState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpbc2RUMLDSMonLaserState.setStatus("current")


class _Mpbc2RUMLDSMonLaserMode_Type(Integer32):
    """Custom type mpbc2RUMLDSMonLaserMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              10)
        )
    )
    namedValues = NamedValues(
        *(("laserOff", 0),
          ("laserAPR", 1),
          ("laserOn", 10))
    )


_Mpbc2RUMLDSMonLaserMode_Type.__name__ = "Integer32"
_Mpbc2RUMLDSMonLaserMode_Object = MibScalar
mpbc2RUMLDSMonLaserMode = _Mpbc2RUMLDSMonLaserMode_Object(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 14, 2, 13),
    _Mpbc2RUMLDSMonLaserMode_Type()
)
mpbc2RUMLDSMonLaserMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpbc2RUMLDSMonLaserMode.setStatus("current")
_Mpbc2RUMLDSMonControlMode_Type = Unsigned32
_Mpbc2RUMLDSMonControlMode_Object = MibScalar
mpbc2RUMLDSMonControlMode = _Mpbc2RUMLDSMonControlMode_Object(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 14, 2, 14),
    _Mpbc2RUMLDSMonControlMode_Type()
)
mpbc2RUMLDSMonControlMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpbc2RUMLDSMonControlMode.setStatus("current")
_Mpbc2RUMLDSDisableInputState_Type = Unsigned32
_Mpbc2RUMLDSDisableInputState_Object = MibScalar
mpbc2RUMLDSDisableInputState = _Mpbc2RUMLDSDisableInputState_Object(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 14, 2, 15),
    _Mpbc2RUMLDSDisableInputState_Type()
)
mpbc2RUMLDSDisableInputState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpbc2RUMLDSDisableInputState.setStatus("current")


class _Mpbc2RUMLDSUnitState_Type(Integer32):
    """Custom type mpbc2RUMLDSUnitState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("stateInit", 0),
          ("stateNormal", 1),
          ("stateFault", 2))
    )


_Mpbc2RUMLDSUnitState_Type.__name__ = "Integer32"
_Mpbc2RUMLDSUnitState_Object = MibScalar
mpbc2RUMLDSUnitState = _Mpbc2RUMLDSUnitState_Object(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 14, 2, 16),
    _Mpbc2RUMLDSUnitState_Type()
)
mpbc2RUMLDSUnitState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpbc2RUMLDSUnitState.setStatus("current")
_Mpbc2RUMLDSConfiguration_ObjectIdentity = ObjectIdentity
mpbc2RUMLDSConfiguration = _Mpbc2RUMLDSConfiguration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 14, 3)
)
_Mpbc2RUMLDSLD1CurMinThrmA_Type = Unsigned32
_Mpbc2RUMLDSLD1CurMinThrmA_Object = MibScalar
mpbc2RUMLDSLD1CurMinThrmA = _Mpbc2RUMLDSLD1CurMinThrmA_Object(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 14, 3, 1),
    _Mpbc2RUMLDSLD1CurMinThrmA_Type()
)
mpbc2RUMLDSLD1CurMinThrmA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpbc2RUMLDSLD1CurMinThrmA.setStatus("current")
_Mpbc2RUMLDSLD1CurMaxThrmA_Type = Unsigned32
_Mpbc2RUMLDSLD1CurMaxThrmA_Object = MibScalar
mpbc2RUMLDSLD1CurMaxThrmA = _Mpbc2RUMLDSLD1CurMaxThrmA_Object(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 14, 3, 2),
    _Mpbc2RUMLDSLD1CurMaxThrmA_Type()
)
mpbc2RUMLDSLD1CurMaxThrmA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpbc2RUMLDSLD1CurMaxThrmA.setStatus("current")
_Mpbc2RUMLDSLD2CurMinThrmA_Type = Unsigned32
_Mpbc2RUMLDSLD2CurMinThrmA_Object = MibScalar
mpbc2RUMLDSLD2CurMinThrmA = _Mpbc2RUMLDSLD2CurMinThrmA_Object(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 14, 3, 3),
    _Mpbc2RUMLDSLD2CurMinThrmA_Type()
)
mpbc2RUMLDSLD2CurMinThrmA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpbc2RUMLDSLD2CurMinThrmA.setStatus("current")
_Mpbc2RUMLDSLD2CurMaxThrmA_Type = Unsigned32
_Mpbc2RUMLDSLD2CurMaxThrmA_Object = MibScalar
mpbc2RUMLDSLD2CurMaxThrmA = _Mpbc2RUMLDSLD2CurMaxThrmA_Object(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 14, 3, 4),
    _Mpbc2RUMLDSLD2CurMaxThrmA_Type()
)
mpbc2RUMLDSLD2CurMaxThrmA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpbc2RUMLDSLD2CurMaxThrmA.setStatus("current")
_Mpbc2RUMLDSCaseTempMinSetThrDegCx10_Type = Integer32
_Mpbc2RUMLDSCaseTempMinSetThrDegCx10_Object = MibScalar
mpbc2RUMLDSCaseTempMinSetThrDegCx10 = _Mpbc2RUMLDSCaseTempMinSetThrDegCx10_Object(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 14, 3, 5),
    _Mpbc2RUMLDSCaseTempMinSetThrDegCx10_Type()
)
mpbc2RUMLDSCaseTempMinSetThrDegCx10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpbc2RUMLDSCaseTempMinSetThrDegCx10.setStatus("current")
_Mpbc2RUMLDSCaseTempMinClearThrDegCx10_Type = Integer32
_Mpbc2RUMLDSCaseTempMinClearThrDegCx10_Object = MibScalar
mpbc2RUMLDSCaseTempMinClearThrDegCx10 = _Mpbc2RUMLDSCaseTempMinClearThrDegCx10_Object(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 14, 3, 6),
    _Mpbc2RUMLDSCaseTempMinClearThrDegCx10_Type()
)
mpbc2RUMLDSCaseTempMinClearThrDegCx10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpbc2RUMLDSCaseTempMinClearThrDegCx10.setStatus("current")
_Mpbc2RUMLDSCaseTempMaxSetThrDegCx10_Type = Integer32
_Mpbc2RUMLDSCaseTempMaxSetThrDegCx10_Object = MibScalar
mpbc2RUMLDSCaseTempMaxSetThrDegCx10 = _Mpbc2RUMLDSCaseTempMaxSetThrDegCx10_Object(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 14, 3, 7),
    _Mpbc2RUMLDSCaseTempMaxSetThrDegCx10_Type()
)
mpbc2RUMLDSCaseTempMaxSetThrDegCx10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpbc2RUMLDSCaseTempMaxSetThrDegCx10.setStatus("current")
_Mpbc2RUMLDSCaseTempMaxClearThrDegCx10_Type = Integer32
_Mpbc2RUMLDSCaseTempMaxClearThrDegCx10_Object = MibScalar
mpbc2RUMLDSCaseTempMaxClearThrDegCx10 = _Mpbc2RUMLDSCaseTempMaxClearThrDegCx10_Object(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 14, 3, 8),
    _Mpbc2RUMLDSCaseTempMaxClearThrDegCx10_Type()
)
mpbc2RUMLDSCaseTempMaxClearThrDegCx10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpbc2RUMLDSCaseTempMaxClearThrDegCx10.setStatus("current")
_Mpbc2RUMLDSCaseTempMinAlrmThrDegCx10_Type = Integer32
_Mpbc2RUMLDSCaseTempMinAlrmThrDegCx10_Object = MibScalar
mpbc2RUMLDSCaseTempMinAlrmThrDegCx10 = _Mpbc2RUMLDSCaseTempMinAlrmThrDegCx10_Object(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 14, 3, 9),
    _Mpbc2RUMLDSCaseTempMinAlrmThrDegCx10_Type()
)
mpbc2RUMLDSCaseTempMinAlrmThrDegCx10.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mpbc2RUMLDSCaseTempMinAlrmThrDegCx10.setStatus("current")
_Mpbc2RUMLDSCaseTempMaxAlrmThrDegCx10_Type = Integer32
_Mpbc2RUMLDSCaseTempMaxAlrmThrDegCx10_Object = MibScalar
mpbc2RUMLDSCaseTempMaxAlrmThrDegCx10 = _Mpbc2RUMLDSCaseTempMaxAlrmThrDegCx10_Object(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 14, 3, 10),
    _Mpbc2RUMLDSCaseTempMaxAlrmThrDegCx10_Type()
)
mpbc2RUMLDSCaseTempMaxAlrmThrDegCx10.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mpbc2RUMLDSCaseTempMaxAlrmThrDegCx10.setStatus("current")
_Mpbc2RUMLDS3rdWLOutputPwrMinThrdBx10_Type = Integer32
_Mpbc2RUMLDS3rdWLOutputPwrMinThrdBx10_Object = MibScalar
mpbc2RUMLDS3rdWLOutputPwrMinThrdBx10 = _Mpbc2RUMLDS3rdWLOutputPwrMinThrdBx10_Object(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 14, 3, 11),
    _Mpbc2RUMLDS3rdWLOutputPwrMinThrdBx10_Type()
)
mpbc2RUMLDS3rdWLOutputPwrMinThrdBx10.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mpbc2RUMLDS3rdWLOutputPwrMinThrdBx10.setStatus("current")
_Mpbc2RUMLDS3rdWLOutputPwrMaxThrdBx10_Type = Integer32
_Mpbc2RUMLDS3rdWLOutputPwrMaxThrdBx10_Object = MibScalar
mpbc2RUMLDS3rdWLOutputPwrMaxThrdBx10 = _Mpbc2RUMLDS3rdWLOutputPwrMaxThrdBx10_Object(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 14, 3, 12),
    _Mpbc2RUMLDS3rdWLOutputPwrMaxThrdBx10_Type()
)
mpbc2RUMLDS3rdWLOutputPwrMaxThrdBx10.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mpbc2RUMLDS3rdWLOutputPwrMaxThrdBx10.setStatus("current")
_Mpbc2RUMLDS4thWLOutputPwrMinThrdBx10_Type = Integer32
_Mpbc2RUMLDS4thWLOutputPwrMinThrdBx10_Object = MibScalar
mpbc2RUMLDS4thWLOutputPwrMinThrdBx10 = _Mpbc2RUMLDS4thWLOutputPwrMinThrdBx10_Object(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 14, 3, 13),
    _Mpbc2RUMLDS4thWLOutputPwrMinThrdBx10_Type()
)
mpbc2RUMLDS4thWLOutputPwrMinThrdBx10.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mpbc2RUMLDS4thWLOutputPwrMinThrdBx10.setStatus("current")
_Mpbc2RUMLDS4thWLOutputPwrMaxThrdBx10_Type = Integer32
_Mpbc2RUMLDS4thWLOutputPwrMaxThrdBx10_Object = MibScalar
mpbc2RUMLDS4thWLOutputPwrMaxThrdBx10 = _Mpbc2RUMLDS4thWLOutputPwrMaxThrdBx10_Object(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 14, 3, 14),
    _Mpbc2RUMLDS4thWLOutputPwrMaxThrdBx10_Type()
)
mpbc2RUMLDS4thWLOutputPwrMaxThrdBx10.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mpbc2RUMLDS4thWLOutputPwrMaxThrdBx10.setStatus("current")
_Mpbc2RUMLDS3rdWLOutputPwrMinLimdBmx10_Type = Integer32
_Mpbc2RUMLDS3rdWLOutputPwrMinLimdBmx10_Object = MibScalar
mpbc2RUMLDS3rdWLOutputPwrMinLimdBmx10 = _Mpbc2RUMLDS3rdWLOutputPwrMinLimdBmx10_Object(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 14, 3, 15),
    _Mpbc2RUMLDS3rdWLOutputPwrMinLimdBmx10_Type()
)
mpbc2RUMLDS3rdWLOutputPwrMinLimdBmx10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpbc2RUMLDS3rdWLOutputPwrMinLimdBmx10.setStatus("current")
_Mpbc2RUMLDS3rdWLOutputPwrMaxLimdBmx10_Type = Integer32
_Mpbc2RUMLDS3rdWLOutputPwrMaxLimdBmx10_Object = MibScalar
mpbc2RUMLDS3rdWLOutputPwrMaxLimdBmx10 = _Mpbc2RUMLDS3rdWLOutputPwrMaxLimdBmx10_Object(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 14, 3, 16),
    _Mpbc2RUMLDS3rdWLOutputPwrMaxLimdBmx10_Type()
)
mpbc2RUMLDS3rdWLOutputPwrMaxLimdBmx10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpbc2RUMLDS3rdWLOutputPwrMaxLimdBmx10.setStatus("current")
_Mpbc2RUMLDS4thWLOutputPwrMinLimdBmx10_Type = Integer32
_Mpbc2RUMLDS4thWLOutputPwrMinLimdBmx10_Object = MibScalar
mpbc2RUMLDS4thWLOutputPwrMinLimdBmx10 = _Mpbc2RUMLDS4thWLOutputPwrMinLimdBmx10_Object(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 14, 3, 17),
    _Mpbc2RUMLDS4thWLOutputPwrMinLimdBmx10_Type()
)
mpbc2RUMLDS4thWLOutputPwrMinLimdBmx10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpbc2RUMLDS4thWLOutputPwrMinLimdBmx10.setStatus("current")
_Mpbc2RUMLDS4thWLOutputPwrMaxLimdBmx10_Type = Integer32
_Mpbc2RUMLDS4thWLOutputPwrMaxLimdBmx10_Object = MibScalar
mpbc2RUMLDS4thWLOutputPwrMaxLimdBmx10 = _Mpbc2RUMLDS4thWLOutputPwrMaxLimdBmx10_Object(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 14, 3, 18),
    _Mpbc2RUMLDS4thWLOutputPwrMaxLimdBmx10_Type()
)
mpbc2RUMLDS4thWLOutputPwrMaxLimdBmx10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpbc2RUMLDS4thWLOutputPwrMaxLimdBmx10.setStatus("current")
_Mpbc2RUMLDSLOSSetThrdBmx100_Type = Integer32
_Mpbc2RUMLDSLOSSetThrdBmx100_Object = MibScalar
mpbc2RUMLDSLOSSetThrdBmx100 = _Mpbc2RUMLDSLOSSetThrdBmx100_Object(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 14, 3, 19),
    _Mpbc2RUMLDSLOSSetThrdBmx100_Type()
)
mpbc2RUMLDSLOSSetThrdBmx100.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpbc2RUMLDSLOSSetThrdBmx100.setStatus("current")
_Mpbc2RUMLDSLOSClearThrdBmx100_Type = Integer32
_Mpbc2RUMLDSLOSClearThrdBmx100_Object = MibScalar
mpbc2RUMLDSLOSClearThrdBmx100 = _Mpbc2RUMLDSLOSClearThrdBmx100_Object(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 14, 3, 20),
    _Mpbc2RUMLDSLOSClearThrdBmx100_Type()
)
mpbc2RUMLDSLOSClearThrdBmx100.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpbc2RUMLDSLOSClearThrdBmx100.setStatus("current")
_Mpbc2RUPxxH_ObjectIdentity = ObjectIdentity
mpbc2RUPxxH = _Mpbc2RUPxxH_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 15)
)
_Mpbc2RUPxxHControl_ObjectIdentity = ObjectIdentity
mpbc2RUPxxHControl = _Mpbc2RUPxxHControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 15, 1)
)


class _Mpbc2RUPxxHLaserMode_Type(Integer32):
    """Custom type mpbc2RUPxxHLaserMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("laserOff", 0),
          ("laserAPR", 1))
    )


_Mpbc2RUPxxHLaserMode_Type.__name__ = "Integer32"
_Mpbc2RUPxxHLaserMode_Object = MibScalar
mpbc2RUPxxHLaserMode = _Mpbc2RUPxxHLaserMode_Object(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 15, 1, 1),
    _Mpbc2RUPxxHLaserMode_Type()
)
mpbc2RUPxxHLaserMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mpbc2RUPxxHLaserMode.setStatus("current")
_Mpbc2RUPxxHControlMode_Type = Integer32
_Mpbc2RUPxxHControlMode_Object = MibScalar
mpbc2RUPxxHControlMode = _Mpbc2RUPxxHControlMode_Object(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 15, 1, 2),
    _Mpbc2RUPxxHControlMode_Type()
)
mpbc2RUPxxHControlMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mpbc2RUPxxHControlMode.setStatus("current")
_Mpbc2RUPxxHPwrSetPtmW_Type = Integer32
_Mpbc2RUPxxHPwrSetPtmW_Object = MibScalar
mpbc2RUPxxHPwrSetPtmW = _Mpbc2RUPxxHPwrSetPtmW_Object(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 15, 1, 3),
    _Mpbc2RUPxxHPwrSetPtmW_Type()
)
mpbc2RUPxxHPwrSetPtmW.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mpbc2RUPxxHPwrSetPtmW.setStatus("current")
_Mpbc2RUPxxHGainSetPtdBx10_Type = Integer32
_Mpbc2RUPxxHGainSetPtdBx10_Object = MibScalar
mpbc2RUPxxHGainSetPtdBx10 = _Mpbc2RUPxxHGainSetPtdBx10_Object(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 15, 1, 4),
    _Mpbc2RUPxxHGainSetPtdBx10_Type()
)
mpbc2RUPxxHGainSetPtdBx10.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mpbc2RUPxxHGainSetPtdBx10.setStatus("current")
_Mpbc2RUPxxHVOASettingdBx10_Type = Integer32
_Mpbc2RUPxxHVOASettingdBx10_Object = MibScalar
mpbc2RUPxxHVOASettingdBx10 = _Mpbc2RUPxxHVOASettingdBx10_Object(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 15, 1, 5),
    _Mpbc2RUPxxHVOASettingdBx10_Type()
)
mpbc2RUPxxHVOASettingdBx10.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mpbc2RUPxxHVOASettingdBx10.setStatus("current")
_Mpbc2RUPxxHReset_Type = TruthValue
_Mpbc2RUPxxHReset_Object = MibScalar
mpbc2RUPxxHReset = _Mpbc2RUPxxHReset_Object(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 15, 1, 6),
    _Mpbc2RUPxxHReset_Type()
)
mpbc2RUPxxHReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mpbc2RUPxxHReset.setStatus("current")
_Mpbc2RUPxxHMonitor_ObjectIdentity = ObjectIdentity
mpbc2RUPxxHMonitor = _Mpbc2RUPxxHMonitor_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 15, 2)
)
_Mpbc2RUPxxHLD1CurmA_Type = Unsigned32
_Mpbc2RUPxxHLD1CurmA_Object = MibScalar
mpbc2RUPxxHLD1CurmA = _Mpbc2RUPxxHLD1CurmA_Object(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 15, 2, 1),
    _Mpbc2RUPxxHLD1CurmA_Type()
)
mpbc2RUPxxHLD1CurmA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpbc2RUPxxHLD1CurmA.setStatus("current")
_Mpbc2RUPxxHLD1TempDegCx10_Type = Integer32
_Mpbc2RUPxxHLD1TempDegCx10_Object = MibScalar
mpbc2RUPxxHLD1TempDegCx10 = _Mpbc2RUPxxHLD1TempDegCx10_Object(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 15, 2, 2),
    _Mpbc2RUPxxHLD1TempDegCx10_Type()
)
mpbc2RUPxxHLD1TempDegCx10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpbc2RUPxxHLD1TempDegCx10.setStatus("current")
_Mpbc2RUPxxHLD1TECCurmA_Type = Unsigned32
_Mpbc2RUPxxHLD1TECCurmA_Object = MibScalar
mpbc2RUPxxHLD1TECCurmA = _Mpbc2RUPxxHLD1TECCurmA_Object(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 15, 2, 3),
    _Mpbc2RUPxxHLD1TECCurmA_Type()
)
mpbc2RUPxxHLD1TECCurmA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpbc2RUPxxHLD1TECCurmA.setStatus("current")
_Mpbc2RUPxxHLD1BackFacetPwrmWx100_Type = Unsigned32
_Mpbc2RUPxxHLD1BackFacetPwrmWx100_Object = MibScalar
mpbc2RUPxxHLD1BackFacetPwrmWx100 = _Mpbc2RUPxxHLD1BackFacetPwrmWx100_Object(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 15, 2, 4),
    _Mpbc2RUPxxHLD1BackFacetPwrmWx100_Type()
)
mpbc2RUPxxHLD1BackFacetPwrmWx100.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpbc2RUPxxHLD1BackFacetPwrmWx100.setStatus("current")
_Mpbc2RUPxxHLD2CurmA_Type = Unsigned32
_Mpbc2RUPxxHLD2CurmA_Object = MibScalar
mpbc2RUPxxHLD2CurmA = _Mpbc2RUPxxHLD2CurmA_Object(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 15, 2, 5),
    _Mpbc2RUPxxHLD2CurmA_Type()
)
mpbc2RUPxxHLD2CurmA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpbc2RUPxxHLD2CurmA.setStatus("current")
_Mpbc2RUPxxHCaseTempDegCx10_Type = Integer32
_Mpbc2RUPxxHCaseTempDegCx10_Object = MibScalar
mpbc2RUPxxHCaseTempDegCx10 = _Mpbc2RUPxxHCaseTempDegCx10_Object(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 15, 2, 6),
    _Mpbc2RUPxxHCaseTempDegCx10_Type()
)
mpbc2RUPxxHCaseTempDegCx10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpbc2RUPxxHCaseTempDegCx10.setStatus("current")
_Mpbc2RUPxxH148xPumpPwrmW_Type = Unsigned32
_Mpbc2RUPxxH148xPumpPwrmW_Object = MibScalar
mpbc2RUPxxH148xPumpPwrmW = _Mpbc2RUPxxH148xPumpPwrmW_Object(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 15, 2, 7),
    _Mpbc2RUPxxH148xPumpPwrmW_Type()
)
mpbc2RUPxxH148xPumpPwrmW.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpbc2RUPxxH148xPumpPwrmW.setStatus("current")
_Mpbc2RUPxxHOutputPwrmW_Type = Unsigned32
_Mpbc2RUPxxHOutputPwrmW_Object = MibScalar
mpbc2RUPxxHOutputPwrmW = _Mpbc2RUPxxHOutputPwrmW_Object(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 15, 2, 8),
    _Mpbc2RUPxxHOutputPwrmW_Type()
)
mpbc2RUPxxHOutputPwrmW.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpbc2RUPxxHOutputPwrmW.setStatus("current")
_Mpbc2RUPxxHGaindBx10_Type = Integer32
_Mpbc2RUPxxHGaindBx10_Object = MibScalar
mpbc2RUPxxHGaindBx10 = _Mpbc2RUPxxHGaindBx10_Object(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 15, 2, 9),
    _Mpbc2RUPxxHGaindBx10_Type()
)
mpbc2RUPxxHGaindBx10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpbc2RUPxxHGaindBx10.setStatus("current")
_Mpbc2RUPxxHInputPwrmWx100_Type = Unsigned32
_Mpbc2RUPxxHInputPwrmWx100_Object = MibScalar
mpbc2RUPxxHInputPwrmWx100 = _Mpbc2RUPxxHInputPwrmWx100_Object(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 15, 2, 10),
    _Mpbc2RUPxxHInputPwrmWx100_Type()
)
mpbc2RUPxxHInputPwrmWx100.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpbc2RUPxxHInputPwrmWx100.setStatus("current")
_Mpbc2RUPxxHBackReflPwrmWx100_Type = Unsigned32
_Mpbc2RUPxxHBackReflPwrmWx100_Object = MibScalar
mpbc2RUPxxHBackReflPwrmWx100 = _Mpbc2RUPxxHBackReflPwrmWx100_Object(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 15, 2, 11),
    _Mpbc2RUPxxHBackReflPwrmWx100_Type()
)
mpbc2RUPxxHBackReflPwrmWx100.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpbc2RUPxxHBackReflPwrmWx100.setStatus("current")


class _Mpbc2RUPxxHMonLaserState_Type(Integer32):
    """Custom type mpbc2RUPxxHMonLaserState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              10)
        )
    )
    namedValues = NamedValues(
        *(("laserOff", 0),
          ("laserNormal", 1),
          ("laserALS", 2),
          ("laserALS100", 3),
          ("laserOn", 10))
    )


_Mpbc2RUPxxHMonLaserState_Type.__name__ = "Integer32"
_Mpbc2RUPxxHMonLaserState_Object = MibScalar
mpbc2RUPxxHMonLaserState = _Mpbc2RUPxxHMonLaserState_Object(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 15, 2, 12),
    _Mpbc2RUPxxHMonLaserState_Type()
)
mpbc2RUPxxHMonLaserState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpbc2RUPxxHMonLaserState.setStatus("current")


class _Mpbc2RUPxxHMonLaserMode_Type(Integer32):
    """Custom type mpbc2RUPxxHMonLaserMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              10)
        )
    )
    namedValues = NamedValues(
        *(("laserOff", 0),
          ("laserAPR", 1),
          ("laserOn", 10))
    )


_Mpbc2RUPxxHMonLaserMode_Type.__name__ = "Integer32"
_Mpbc2RUPxxHMonLaserMode_Object = MibScalar
mpbc2RUPxxHMonLaserMode = _Mpbc2RUPxxHMonLaserMode_Object(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 15, 2, 13),
    _Mpbc2RUPxxHMonLaserMode_Type()
)
mpbc2RUPxxHMonLaserMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpbc2RUPxxHMonLaserMode.setStatus("current")
_Mpbc2RUPxxHMonControlMode_Type = Integer32
_Mpbc2RUPxxHMonControlMode_Object = MibScalar
mpbc2RUPxxHMonControlMode = _Mpbc2RUPxxHMonControlMode_Object(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 15, 2, 14),
    _Mpbc2RUPxxHMonControlMode_Type()
)
mpbc2RUPxxHMonControlMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpbc2RUPxxHMonControlMode.setStatus("current")
_Mpbc2RUPxxHDisableInputState_Type = Unsigned32
_Mpbc2RUPxxHDisableInputState_Object = MibScalar
mpbc2RUPxxHDisableInputState = _Mpbc2RUPxxHDisableInputState_Object(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 15, 2, 15),
    _Mpbc2RUPxxHDisableInputState_Type()
)
mpbc2RUPxxHDisableInputState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpbc2RUPxxHDisableInputState.setStatus("current")


class _Mpbc2RUPxxHUnitState_Type(Integer32):
    """Custom type mpbc2RUPxxHUnitState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("stateInit", 0),
          ("stateNormal", 1),
          ("stateFault", 2))
    )


_Mpbc2RUPxxHUnitState_Type.__name__ = "Integer32"
_Mpbc2RUPxxHUnitState_Object = MibScalar
mpbc2RUPxxHUnitState = _Mpbc2RUPxxHUnitState_Object(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 15, 2, 16),
    _Mpbc2RUPxxHUnitState_Type()
)
mpbc2RUPxxHUnitState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpbc2RUPxxHUnitState.setStatus("current")


class _Mpbc2RUPxxHOSCRxTone_Type(Integer32):
    """Custom type mpbc2RUPxxHOSCRxTone based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("noTone", 0),
          ("tone1", 1),
          ("tone2", 2),
          ("tone1plus2", 3))
    )


_Mpbc2RUPxxHOSCRxTone_Type.__name__ = "Integer32"
_Mpbc2RUPxxHOSCRxTone_Object = MibScalar
mpbc2RUPxxHOSCRxTone = _Mpbc2RUPxxHOSCRxTone_Object(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 15, 2, 17),
    _Mpbc2RUPxxHOSCRxTone_Type()
)
mpbc2RUPxxHOSCRxTone.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpbc2RUPxxHOSCRxTone.setStatus("current")
_Mpbc2RUPxxHOSCTempdegCx10_Type = Integer32
_Mpbc2RUPxxHOSCTempdegCx10_Object = MibScalar
mpbc2RUPxxHOSCTempdegCx10 = _Mpbc2RUPxxHOSCTempdegCx10_Object(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 15, 2, 18),
    _Mpbc2RUPxxHOSCTempdegCx10_Type()
)
mpbc2RUPxxHOSCTempdegCx10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpbc2RUPxxHOSCTempdegCx10.setStatus("current")


class _Mpbc2RUPxxHOSCTxTone_Type(Integer32):
    """Custom type mpbc2RUPxxHOSCTxTone based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("tone1", 1),
          ("tone2", 2))
    )


_Mpbc2RUPxxHOSCTxTone_Type.__name__ = "Integer32"
_Mpbc2RUPxxHOSCTxTone_Object = MibScalar
mpbc2RUPxxHOSCTxTone = _Mpbc2RUPxxHOSCTxTone_Object(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 15, 2, 19),
    _Mpbc2RUPxxHOSCTxTone_Type()
)
mpbc2RUPxxHOSCTxTone.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpbc2RUPxxHOSCTxTone.setStatus("current")
_Mpbc2RUPxxHOSCTxPwrmWx100_Type = Integer32
_Mpbc2RUPxxHOSCTxPwrmWx100_Object = MibScalar
mpbc2RUPxxHOSCTxPwrmWx100 = _Mpbc2RUPxxHOSCTxPwrmWx100_Object(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 15, 2, 20),
    _Mpbc2RUPxxHOSCTxPwrmWx100_Type()
)
mpbc2RUPxxHOSCTxPwrmWx100.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpbc2RUPxxHOSCTxPwrmWx100.setStatus("current")


class _Mpbc2RUPxxHOSCRx1610Tone_Type(Integer32):
    """Custom type mpbc2RUPxxHOSCRx1610Tone based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("tone1", 1),
          ("tone2", 2))
    )


_Mpbc2RUPxxHOSCRx1610Tone_Type.__name__ = "Integer32"
_Mpbc2RUPxxHOSCRx1610Tone_Object = MibScalar
mpbc2RUPxxHOSCRx1610Tone = _Mpbc2RUPxxHOSCRx1610Tone_Object(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 15, 2, 21),
    _Mpbc2RUPxxHOSCRx1610Tone_Type()
)
mpbc2RUPxxHOSCRx1610Tone.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpbc2RUPxxHOSCRx1610Tone.setStatus("current")
_Mpbc2RUPxxHMonVOASettingdBx10_Type = Integer32
_Mpbc2RUPxxHMonVOASettingdBx10_Object = MibScalar
mpbc2RUPxxHMonVOASettingdBx10 = _Mpbc2RUPxxHMonVOASettingdBx10_Object(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 15, 2, 22),
    _Mpbc2RUPxxHMonVOASettingdBx10_Type()
)
mpbc2RUPxxHMonVOASettingdBx10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpbc2RUPxxHMonVOASettingdBx10.setStatus("current")
_Mpbc2RUPxxHConfiguration_ObjectIdentity = ObjectIdentity
mpbc2RUPxxHConfiguration = _Mpbc2RUPxxHConfiguration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 15, 3)
)
_Mpbc2RUPxxHLD1CurMinThrmA_Type = Unsigned32
_Mpbc2RUPxxHLD1CurMinThrmA_Object = MibScalar
mpbc2RUPxxHLD1CurMinThrmA = _Mpbc2RUPxxHLD1CurMinThrmA_Object(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 15, 3, 1),
    _Mpbc2RUPxxHLD1CurMinThrmA_Type()
)
mpbc2RUPxxHLD1CurMinThrmA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpbc2RUPxxHLD1CurMinThrmA.setStatus("current")
_Mpbc2RUPxxHLD2CurMinThrmA_Type = Unsigned32
_Mpbc2RUPxxHLD2CurMinThrmA_Object = MibScalar
mpbc2RUPxxHLD2CurMinThrmA = _Mpbc2RUPxxHLD2CurMinThrmA_Object(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 15, 3, 2),
    _Mpbc2RUPxxHLD2CurMinThrmA_Type()
)
mpbc2RUPxxHLD2CurMinThrmA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpbc2RUPxxHLD2CurMinThrmA.setStatus("current")
_Mpbc2RUPxxHLD1CurMaxThrmA_Type = Unsigned32
_Mpbc2RUPxxHLD1CurMaxThrmA_Object = MibScalar
mpbc2RUPxxHLD1CurMaxThrmA = _Mpbc2RUPxxHLD1CurMaxThrmA_Object(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 15, 3, 3),
    _Mpbc2RUPxxHLD1CurMaxThrmA_Type()
)
mpbc2RUPxxHLD1CurMaxThrmA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpbc2RUPxxHLD1CurMaxThrmA.setStatus("current")
_Mpbc2RUPxxHLD2CurMaxThrmA_Type = Unsigned32
_Mpbc2RUPxxHLD2CurMaxThrmA_Object = MibScalar
mpbc2RUPxxHLD2CurMaxThrmA = _Mpbc2RUPxxHLD2CurMaxThrmA_Object(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 15, 3, 4),
    _Mpbc2RUPxxHLD2CurMaxThrmA_Type()
)
mpbc2RUPxxHLD2CurMaxThrmA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpbc2RUPxxHLD2CurMaxThrmA.setStatus("current")
_Mpbc2RUPxxHCaseTempMinSetThrDegCx10_Type = Integer32
_Mpbc2RUPxxHCaseTempMinSetThrDegCx10_Object = MibScalar
mpbc2RUPxxHCaseTempMinSetThrDegCx10 = _Mpbc2RUPxxHCaseTempMinSetThrDegCx10_Object(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 15, 3, 5),
    _Mpbc2RUPxxHCaseTempMinSetThrDegCx10_Type()
)
mpbc2RUPxxHCaseTempMinSetThrDegCx10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpbc2RUPxxHCaseTempMinSetThrDegCx10.setStatus("current")
_Mpbc2RUPxxHCaseTempMinClearThrDegCx10_Type = Integer32
_Mpbc2RUPxxHCaseTempMinClearThrDegCx10_Object = MibScalar
mpbc2RUPxxHCaseTempMinClearThrDegCx10 = _Mpbc2RUPxxHCaseTempMinClearThrDegCx10_Object(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 15, 3, 6),
    _Mpbc2RUPxxHCaseTempMinClearThrDegCx10_Type()
)
mpbc2RUPxxHCaseTempMinClearThrDegCx10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpbc2RUPxxHCaseTempMinClearThrDegCx10.setStatus("current")
_Mpbc2RUPxxHCaseTempMaxSetThrDegCx10_Type = Integer32
_Mpbc2RUPxxHCaseTempMaxSetThrDegCx10_Object = MibScalar
mpbc2RUPxxHCaseTempMaxSetThrDegCx10 = _Mpbc2RUPxxHCaseTempMaxSetThrDegCx10_Object(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 15, 3, 7),
    _Mpbc2RUPxxHCaseTempMaxSetThrDegCx10_Type()
)
mpbc2RUPxxHCaseTempMaxSetThrDegCx10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpbc2RUPxxHCaseTempMaxSetThrDegCx10.setStatus("current")
_Mpbc2RUPxxHCaseTempMaxClearThrDegCx10_Type = Integer32
_Mpbc2RUPxxHCaseTempMaxClearThrDegCx10_Object = MibScalar
mpbc2RUPxxHCaseTempMaxClearThrDegCx10 = _Mpbc2RUPxxHCaseTempMaxClearThrDegCx10_Object(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 15, 3, 8),
    _Mpbc2RUPxxHCaseTempMaxClearThrDegCx10_Type()
)
mpbc2RUPxxHCaseTempMaxClearThrDegCx10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpbc2RUPxxHCaseTempMaxClearThrDegCx10.setStatus("current")
_Mpbc2RUPxxHCaseTempMinAlrmThrDegCx10_Type = Integer32
_Mpbc2RUPxxHCaseTempMinAlrmThrDegCx10_Object = MibScalar
mpbc2RUPxxHCaseTempMinAlrmThrDegCx10 = _Mpbc2RUPxxHCaseTempMinAlrmThrDegCx10_Object(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 15, 3, 9),
    _Mpbc2RUPxxHCaseTempMinAlrmThrDegCx10_Type()
)
mpbc2RUPxxHCaseTempMinAlrmThrDegCx10.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mpbc2RUPxxHCaseTempMinAlrmThrDegCx10.setStatus("current")
_Mpbc2RUPxxHCaseTempMaxAlrmThrDegCx10_Type = Integer32
_Mpbc2RUPxxHCaseTempMaxAlrmThrDegCx10_Object = MibScalar
mpbc2RUPxxHCaseTempMaxAlrmThrDegCx10 = _Mpbc2RUPxxHCaseTempMaxAlrmThrDegCx10_Object(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 15, 3, 10),
    _Mpbc2RUPxxHCaseTempMaxAlrmThrDegCx10_Type()
)
mpbc2RUPxxHCaseTempMaxAlrmThrDegCx10.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mpbc2RUPxxHCaseTempMaxAlrmThrDegCx10.setStatus("current")
_Mpbc2RUPxxHLOSSetThrdBmx100_Type = Integer32
_Mpbc2RUPxxHLOSSetThrdBmx100_Object = MibScalar
mpbc2RUPxxHLOSSetThrdBmx100 = _Mpbc2RUPxxHLOSSetThrdBmx100_Object(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 15, 3, 11),
    _Mpbc2RUPxxHLOSSetThrdBmx100_Type()
)
mpbc2RUPxxHLOSSetThrdBmx100.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpbc2RUPxxHLOSSetThrdBmx100.setStatus("current")
_Mpbc2RUPxxHLOSClearThrdBmx100_Type = Integer32
_Mpbc2RUPxxHLOSClearThrdBmx100_Object = MibScalar
mpbc2RUPxxHLOSClearThrdBmx100 = _Mpbc2RUPxxHLOSClearThrdBmx100_Object(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 15, 3, 12),
    _Mpbc2RUPxxHLOSClearThrdBmx100_Type()
)
mpbc2RUPxxHLOSClearThrdBmx100.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpbc2RUPxxHLOSClearThrdBmx100.setStatus("current")
_Mpbc2RUPxxHInputMinThrdBmx100_Type = Integer32
_Mpbc2RUPxxHInputMinThrdBmx100_Object = MibScalar
mpbc2RUPxxHInputMinThrdBmx100 = _Mpbc2RUPxxHInputMinThrdBmx100_Object(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 15, 3, 13),
    _Mpbc2RUPxxHInputMinThrdBmx100_Type()
)
mpbc2RUPxxHInputMinThrdBmx100.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mpbc2RUPxxHInputMinThrdBmx100.setStatus("current")
_Mpbc2RUPxxHInputMaxThrdBmx100_Type = Integer32
_Mpbc2RUPxxHInputMaxThrdBmx100_Object = MibScalar
mpbc2RUPxxHInputMaxThrdBmx100 = _Mpbc2RUPxxHInputMaxThrdBmx100_Object(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 15, 3, 14),
    _Mpbc2RUPxxHInputMaxThrdBmx100_Type()
)
mpbc2RUPxxHInputMaxThrdBmx100.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mpbc2RUPxxHInputMaxThrdBmx100.setStatus("current")
_Mpbc2RUPxxHOutputMinThrdBx10_Type = Integer32
_Mpbc2RUPxxHOutputMinThrdBx10_Object = MibScalar
mpbc2RUPxxHOutputMinThrdBx10 = _Mpbc2RUPxxHOutputMinThrdBx10_Object(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 15, 3, 15),
    _Mpbc2RUPxxHOutputMinThrdBx10_Type()
)
mpbc2RUPxxHOutputMinThrdBx10.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mpbc2RUPxxHOutputMinThrdBx10.setStatus("current")
_Mpbc2RUPxxHOutputMaxThrdBx10_Type = Integer32
_Mpbc2RUPxxHOutputMaxThrdBx10_Object = MibScalar
mpbc2RUPxxHOutputMaxThrdBx10 = _Mpbc2RUPxxHOutputMaxThrdBx10_Object(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 15, 3, 16),
    _Mpbc2RUPxxHOutputMaxThrdBx10_Type()
)
mpbc2RUPxxHOutputMaxThrdBx10.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mpbc2RUPxxHOutputMaxThrdBx10.setStatus("current")
_Mpbc2RUPxxHOSCMode_Type = Unsigned32
_Mpbc2RUPxxHOSCMode_Object = MibScalar
mpbc2RUPxxHOSCMode = _Mpbc2RUPxxHOSCMode_Object(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 15, 3, 17),
    _Mpbc2RUPxxHOSCMode_Type()
)
mpbc2RUPxxHOSCMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mpbc2RUPxxHOSCMode.setStatus("current")
_Mpbc2RUPxxHOutputSetptminLimdBmx10_Type = Integer32
_Mpbc2RUPxxHOutputSetptminLimdBmx10_Object = MibScalar
mpbc2RUPxxHOutputSetptminLimdBmx10 = _Mpbc2RUPxxHOutputSetptminLimdBmx10_Object(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 15, 3, 18),
    _Mpbc2RUPxxHOutputSetptminLimdBmx10_Type()
)
mpbc2RUPxxHOutputSetptminLimdBmx10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpbc2RUPxxHOutputSetptminLimdBmx10.setStatus("current")
_Mpbc2RUPxxHOutputSetptmaxLimdBmx10_Type = Integer32
_Mpbc2RUPxxHOutputSetptmaxLimdBmx10_Object = MibScalar
mpbc2RUPxxHOutputSetptmaxLimdBmx10 = _Mpbc2RUPxxHOutputSetptmaxLimdBmx10_Object(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 15, 3, 19),
    _Mpbc2RUPxxHOutputSetptmaxLimdBmx10_Type()
)
mpbc2RUPxxHOutputSetptmaxLimdBmx10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpbc2RUPxxHOutputSetptmaxLimdBmx10.setStatus("current")
_Mpbc2RUPxxHGainSetptminLimdBx10_Type = Integer32
_Mpbc2RUPxxHGainSetptminLimdBx10_Object = MibScalar
mpbc2RUPxxHGainSetptminLimdBx10 = _Mpbc2RUPxxHGainSetptminLimdBx10_Object(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 15, 3, 20),
    _Mpbc2RUPxxHGainSetptminLimdBx10_Type()
)
mpbc2RUPxxHGainSetptminLimdBx10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpbc2RUPxxHGainSetptminLimdBx10.setStatus("current")
_Mpbc2RUPxxHGainSetptmaxLimdBx10_Type = Integer32
_Mpbc2RUPxxHGainSetptmaxLimdBx10_Object = MibScalar
mpbc2RUPxxHGainSetptmaxLimdBx10 = _Mpbc2RUPxxHGainSetptmaxLimdBx10_Object(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 15, 3, 21),
    _Mpbc2RUPxxHGainSetptmaxLimdBx10_Type()
)
mpbc2RUPxxHGainSetptmaxLimdBx10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpbc2RUPxxHGainSetptmaxLimdBx10.setStatus("current")

# Managed Objects groups

mpbc2RUMibAllObjects = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 13, 1, 1)
)
mpbc2RUMibAllObjects.setObjects(
      *(("MPBC-2RU-MIB", "mpbc2RUTrapCriticalEnable"),
        ("MPBC-2RU-MIB", "mpbc2RUTrapMajorEnable"),
        ("MPBC-2RU-MIB", "mpbc2RUTrapMinorEnable"),
        ("MPBC-2RU-MIB", "mpbc2RUTrapInformationalEnable"),
        ("MPBC-2RU-MIB", "mpbc2RUMacAddress"),
        ("MPBC-2RU-MIB", "mpbc2RUEthernetIPaddress"),
        ("MPBC-2RU-MIB", "mpbc2RUEthernetIPsubNetMask"),
        ("MPBC-2RU-MIB", "mpbc2RUDefaultGateway"),
        ("MPBC-2RU-MIB", "mpbc2RUNEID"),
        ("MPBC-2RU-MIB", "mpbc2RUAlarmNEID"),
        ("MPBC-2RU-MIB", "mpbc2RUAlarmSeverity"),
        ("MPBC-2RU-MIB", "mpbc2RUAlarmDescription"),
        ("MPBC-2RU-MIB", "mpbc2RUAlarmDateAndTime"),
        ("MPBC-2RU-MIB", "mpbc2RUNotifiedNMSipAddress-IP"),
        ("MPBC-2RU-MIB", "mpbc2RUNotifiedNMSipAddress-Description"),
        ("MPBC-2RU-MIB", "mpbc2RUNotifiedNMSipAddress-Enabled"))
)
if mibBuilder.loadTexts:
    mpbc2RUMibAllObjects.setStatus("current")

mpbc2ruMibAllObjects = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 13, 1, 3)
)
mpbc2ruMibAllObjects.setObjects(
      *(("MPBC-2RU-MIB", "mpbc2RUAckTrapCriticalEnable"),
        ("MPBC-2RU-MIB", "mpbc2RUAckTrapCriticalRetries"),
        ("MPBC-2RU-MIB", "mpbc2RUAckTrapCriticalTimeOutsec"),
        ("MPBC-2RU-MIB", "mpbc2RUAckTrapMajorEnable"),
        ("MPBC-2RU-MIB", "mpbc2RUAckTrapMajorRetries"),
        ("MPBC-2RU-MIB", "mpbc2RUAckTrapMajorTimeOutsec"),
        ("MPBC-2RU-MIB", "mpbc2RUAckTrapMinorEnable"),
        ("MPBC-2RU-MIB", "mpbc2RUAckTrapMinorRetries"),
        ("MPBC-2RU-MIB", "mpbc2RUAckTrapMinorTimeOutsec"),
        ("MPBC-2RU-MIB", "mpbc2RUAckTrapInformationalEnable"),
        ("MPBC-2RU-MIB", "mpbc2RUAckTrapInformationalRetries"),
        ("MPBC-2RU-MIB", "mpbc2RUAckTrapInformationalTimeOutsec"),
        ("MPBC-2RU-MIB", "mpbc2RUSnmpTrapPort"),
        ("MPBC-2RU-MIB", "mpbc2RUDateTime"),
        ("MPBC-2RU-MIB", "mpbc2RUSNMPAgentVersion"),
        ("MPBC-2RU-MIB", "mpbc2RUSNMPMIBVersion"),
        ("MPBC-2RU-MIB", "mpbc2RUInfoLoc"),
        ("MPBC-2RU-MIB", "mpbc2RUInfoModelNum"),
        ("MPBC-2RU-MIB", "mpbc2RUInfoModelSN"),
        ("MPBC-2RU-MIB", "mpbc2RUInfoOEMPartNum"),
        ("MPBC-2RU-MIB", "mpbc2RUInfoAssyNum"),
        ("MPBC-2RU-MIB", "mpbc2RUInfoRev"),
        ("MPBC-2RU-MIB", "mpbc2RUInfoECN"),
        ("MPBC-2RU-MIB", "mpbc2RUInfoSeqNum"),
        ("MPBC-2RU-MIB", "mpbc2RUInfoMfgDate"),
        ("MPBC-2RU-MIB", "mpbc2RUInfoSwVer"),
        ("MPBC-2RU-MIB", "mpbc2RUInfoBootLoaderRev"),
        ("MPBC-2RU-MIB", "mpbc2RUInfoLibRev"),
        ("MPBC-2RU-MIB", "mpbc2RUInfoLddFw1"),
        ("MPBC-2RU-MIB", "mpbc2RUInfoLddFw2"),
        ("MPBC-2RU-MIB", "mpbc2RUInfoCLEI"),
        ("MPBC-2RU-MIB", "mpbc2RUInfoLastRmaDate"))
)
if mibBuilder.loadTexts:
    mpbc2ruMibAllObjects.setStatus("current")


# Notification objects

mpbc2RUTrapCritical = NotificationType(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 0, 1)
)
mpbc2RUTrapCritical.setObjects(
    ("MPBC-2RU-MIB", "mpbc2RUAlarmNEID")
)
if mibBuilder.loadTexts:
    mpbc2RUTrapCritical.setStatus(
        "current"
    )

mpbc2RUTrapMajor = NotificationType(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 0, 2)
)
mpbc2RUTrapMajor.setObjects(
    ("MPBC-2RU-MIB", "mpbc2RUAlarmNEID")
)
if mibBuilder.loadTexts:
    mpbc2RUTrapMajor.setStatus(
        "current"
    )

mpbc2RUTrapMinor = NotificationType(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 0, 3)
)
mpbc2RUTrapMinor.setObjects(
    ("MPBC-2RU-MIB", "mpbc2RUAlarmNEID")
)
if mibBuilder.loadTexts:
    mpbc2RUTrapMinor.setStatus(
        "current"
    )

mpbc2RUTrapInformational = NotificationType(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 0, 4)
)
mpbc2RUTrapInformational.setObjects(
    ("MPBC-2RU-MIB", "mpbc2RUAlarmNEID")
)
if mibBuilder.loadTexts:
    mpbc2RUTrapInformational.setStatus(
        "current"
    )


# Notifications groups

mpbc2RUMibAllNotifications = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 4464, 2, 2, 13, 1, 2)
)
mpbc2RUMibAllNotifications.setObjects(
      *(("MPBC-2RU-MIB", "mpbc2RUTrapCritical"),
        ("MPBC-2RU-MIB", "mpbc2RUTrapMajor"),
        ("MPBC-2RU-MIB", "mpbc2RUTrapMinor"),
        ("MPBC-2RU-MIB", "mpbc2RUTrapInformational"))
)
if mibBuilder.loadTexts:
    mpbc2RUMibAllNotifications.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "MPBC-2RU-MIB",
    **{"mpbc": mpbc,
       "mpbcRegs": mpbcRegs,
       "mpbcProductRegs": mpbcProductRegs,
       "mpbc2RUProductReg": mpbc2RUProductReg,
       "mpbcProducts": mpbcProducts,
       "mpbc2RU": mpbc2RU,
       "mpbc2RUTrap": mpbc2RUTrap,
       "mpbc2RUTrapCritical": mpbc2RUTrapCritical,
       "mpbc2RUTrapMajor": mpbc2RUTrapMajor,
       "mpbc2RUTrapMinor": mpbc2RUTrapMinor,
       "mpbc2RUTrapInformational": mpbc2RUTrapInformational,
       "mpbc2RUAlarm": mpbc2RUAlarm,
       "mpbc2RUAlarmTable": mpbc2RUAlarmTable,
       "mpbc2RUAlarmEntry": mpbc2RUAlarmEntry,
       "mpbc2RUAlarmIndex": mpbc2RUAlarmIndex,
       "mpbc2RUAlarmNEID": mpbc2RUAlarmNEID,
       "mpbc2RUPosition": mpbc2RUPosition,
       "mpbc2RUAlarmModule": mpbc2RUAlarmModule,
       "mpbc2RUAlarmID": mpbc2RUAlarmID,
       "mpbc2RUAlarmDescription": mpbc2RUAlarmDescription,
       "mpbc2RUAlarmSeverity": mpbc2RUAlarmSeverity,
       "mpbc2RUAlarmDateAndTime": mpbc2RUAlarmDateAndTime,
       "mpbc2RUAlarmExtraData": mpbc2RUAlarmExtraData,
       "mpbc2RUPxx": mpbc2RUPxx,
       "mpbc2RUPxxControl": mpbc2RUPxxControl,
       "mpbc2RUPxxLaserMode": mpbc2RUPxxLaserMode,
       "mpbc2RUPxxControlMode": mpbc2RUPxxControlMode,
       "mpbc2RUPxxPwrSetPtmW": mpbc2RUPxxPwrSetPtmW,
       "mpbc2RUPxxGainSetPtdBx10": mpbc2RUPxxGainSetPtdBx10,
       "mpbc2RUPxxVOASettingdBx10": mpbc2RUPxxVOASettingdBx10,
       "mpbc2RUPxxReset": mpbc2RUPxxReset,
       "mpbc2RUPxxMonitor": mpbc2RUPxxMonitor,
       "mpbc2RUPxxLD1CurmA": mpbc2RUPxxLD1CurmA,
       "mpbc2RUPxxLD1TempDegCx10": mpbc2RUPxxLD1TempDegCx10,
       "mpbc2RUPxxLD1TECCurmA": mpbc2RUPxxLD1TECCurmA,
       "mpbc2RUPxxLD2CurmA": mpbc2RUPxxLD2CurmA,
       "mpbc2RUPxxLD2TempDegCx10": mpbc2RUPxxLD2TempDegCx10,
       "mpbc2RUPxxLD2TECCurmA": mpbc2RUPxxLD2TECCurmA,
       "mpbc2RUPxxCaseTempDegCx10": mpbc2RUPxxCaseTempDegCx10,
       "mpbc2RUPxxOutputPwrmW": mpbc2RUPxxOutputPwrmW,
       "mpbc2RUPxxGaindBx10": mpbc2RUPxxGaindBx10,
       "mpbc2RUPxxInputPwrmWx100": mpbc2RUPxxInputPwrmWx100,
       "mpbc2RUPxxBackReflPwrmWx100": mpbc2RUPxxBackReflPwrmWx100,
       "mpbc2RUPxxMonLaserState": mpbc2RUPxxMonLaserState,
       "mpbc2RUPxxMonLaserMode": mpbc2RUPxxMonLaserMode,
       "mpbc2RUPxxMonControlMode": mpbc2RUPxxMonControlMode,
       "mpbc2RUPxxDisableInputState": mpbc2RUPxxDisableInputState,
       "mpbc2RUPxxUnitState": mpbc2RUPxxUnitState,
       "mpbc2RUPxxOSCRxTone": mpbc2RUPxxOSCRxTone,
       "mpbc2RUPxxOSCTempdegCx10": mpbc2RUPxxOSCTempdegCx10,
       "mpbc2RUPxxOSCTxTone": mpbc2RUPxxOSCTxTone,
       "mpbc2RUPxxOSCTxPwrmWx100": mpbc2RUPxxOSCTxPwrmWx100,
       "mpbc2RUPxxOSCRx1610Tone": mpbc2RUPxxOSCRx1610Tone,
       "mpbc2RUPxxMonVOASettingdBx10": mpbc2RUPxxMonVOASettingdBx10,
       "mpbc2RUPxxConfiguration": mpbc2RUPxxConfiguration,
       "mpbc2RUPxxLD1CurMinThrmA": mpbc2RUPxxLD1CurMinThrmA,
       "mpbc2RUPxxLD2CurMinThrmA": mpbc2RUPxxLD2CurMinThrmA,
       "mpbc2RUPxxLD1CurMaxThrmA": mpbc2RUPxxLD1CurMaxThrmA,
       "mpbc2RUPxxLD2CurMaxThrmA": mpbc2RUPxxLD2CurMaxThrmA,
       "mpbc2RUPxxCaseTempMinSetThrDegCx10": mpbc2RUPxxCaseTempMinSetThrDegCx10,
       "mpbc2RUPxxCaseTempMinClearThrDegCx10": mpbc2RUPxxCaseTempMinClearThrDegCx10,
       "mpbc2RUPxxCaseTempMaxSetThrDegCx10": mpbc2RUPxxCaseTempMaxSetThrDegCx10,
       "mpbc2RUPxxCaseTempMaxClearThrDegCx10": mpbc2RUPxxCaseTempMaxClearThrDegCx10,
       "mpbc2RUPxxCaseTempMinAlrmThrDegCx10": mpbc2RUPxxCaseTempMinAlrmThrDegCx10,
       "mpbc2RUPxxCaseTempMaxAlrmThrDegCx10": mpbc2RUPxxCaseTempMaxAlrmThrDegCx10,
       "mpbc2RUPxxLOSSetThrdBmx100": mpbc2RUPxxLOSSetThrdBmx100,
       "mpbc2RUPxxLOSClearThrdBmx100": mpbc2RUPxxLOSClearThrdBmx100,
       "mpbc2RUPxxInputMinThrdBmx100": mpbc2RUPxxInputMinThrdBmx100,
       "mpbc2RUPxxInputMaxThrdBmx100": mpbc2RUPxxInputMaxThrdBmx100,
       "mpbc2RUPxxOutputMinThrdBx10": mpbc2RUPxxOutputMinThrdBx10,
       "mpbc2RUPxxOutputMaxThrdBx10": mpbc2RUPxxOutputMaxThrdBx10,
       "mpbc2RUPxxOSCMode": mpbc2RUPxxOSCMode,
       "mpbc2RUPxxOutputSetptminLimdBmx10": mpbc2RUPxxOutputSetptminLimdBmx10,
       "mpbc2RUPxxOutputSetptmaxLimdBmx10": mpbc2RUPxxOutputSetptmaxLimdBmx10,
       "mpbc2RUPxxGainSetptminLimdBx10": mpbc2RUPxxGainSetptminLimdBx10,
       "mpbc2RUPxxGainSetptmaxLimdBx10": mpbc2RUPxxGainSetptmaxLimdBx10,
       "mpbc2RURFL1": mpbc2RURFL1,
       "mpbc2RURFL1Control": mpbc2RURFL1Control,
       "mpbc2RURFL1LaserMode": mpbc2RURFL1LaserMode,
       "mpbc2RURFL1ControlMode": mpbc2RURFL1ControlMode,
       "mpbc2RURFL1PwrSetPtmW": mpbc2RURFL1PwrSetPtmW,
       "mpbc2RURFL1Reset": mpbc2RURFL1Reset,
       "mpbc2RURFL1Monitor": mpbc2RURFL1Monitor,
       "mpbc2RURFL1LD1Current": mpbc2RURFL1LD1Current,
       "mpbc2RURFL1LD2Current": mpbc2RURFL1LD2Current,
       "mpbc2RURFL1CaseTempDegCx10": mpbc2RURFL1CaseTempDegCx10,
       "mpbc2RURFL1OutputPwrmW": mpbc2RURFL1OutputPwrmW,
       "mpbc2RURFL1MonLaserState": mpbc2RURFL1MonLaserState,
       "mpbc2RURFL1MonLaserMode": mpbc2RURFL1MonLaserMode,
       "mpbc2RURFL1MonControlMode": mpbc2RURFL1MonControlMode,
       "mpbc2RURFL1DisableInputState": mpbc2RURFL1DisableInputState,
       "mpbc2RURFL1UnitState": mpbc2RURFL1UnitState,
       "mpbc2RURFL1OSCRxTone": mpbc2RURFL1OSCRxTone,
       "mpbc2RURFL1OSCTempDegCx10": mpbc2RURFL1OSCTempDegCx10,
       "mpbc2RURFL1OSCTxTone": mpbc2RURFL1OSCTxTone,
       "mpbc2RURFL1OSCTxPwrmWx100": mpbc2RURFL1OSCTxPwrmWx100,
       "mpbc2RURFL1Configuration": mpbc2RURFL1Configuration,
       "mpbc2RURFL1PwrThrLowdBx10": mpbc2RURFL1PwrThrLowdBx10,
       "mpbc2RURFL1PwrThrHidBx10": mpbc2RURFL1PwrThrHidBx10,
       "mpbc2RURFL1CaseTempMinAlrmThDegCx10": mpbc2RURFL1CaseTempMinAlrmThDegCx10,
       "mpbc2RURFL1CaseTempMaxAlrmThDegCx10": mpbc2RURFL1CaseTempMaxAlrmThDegCx10,
       "mpbc2RURFL1LD1CurMinThrmA": mpbc2RURFL1LD1CurMinThrmA,
       "mpbc2RURFL1LD1CurMaxThrmA": mpbc2RURFL1LD1CurMaxThrmA,
       "mpbc2RURFL1LD2CurMinThrmA": mpbc2RURFL1LD2CurMinThrmA,
       "mpbc2RURFL1LD2CurMaxThrmA": mpbc2RURFL1LD2CurMaxThrmA,
       "mpbc2RURFL1CaseTempMinSetThrDegCx10": mpbc2RURFL1CaseTempMinSetThrDegCx10,
       "mpbc2RURFL1CaseTempMinClearThrDegCx10": mpbc2RURFL1CaseTempMinClearThrDegCx10,
       "mpbc2RURFL1CaseTempMaxSetThrDegCx10": mpbc2RURFL1CaseTempMaxSetThrDegCx10,
       "mpbc2RURFL1CaseTempMaxClearThrDegCx10": mpbc2RURFL1CaseTempMaxClearThrDegCx10,
       "mpbc2RURFL2": mpbc2RURFL2,
       "mpbc2RURFL2Control": mpbc2RURFL2Control,
       "mpbc2RURFL2LaserMode": mpbc2RURFL2LaserMode,
       "mpbc2RURFL2ControlMode": mpbc2RURFL2ControlMode,
       "mpbc2RURFL2WL145xPwrSetPtmW": mpbc2RURFL2WL145xPwrSetPtmW,
       "mpbc2RURFL2WL142xPwrSetPtmW": mpbc2RURFL2WL142xPwrSetPtmW,
       "mpbc2RURFL2Reset": mpbc2RURFL2Reset,
       "mpbc2RURFL2Monitor": mpbc2RURFL2Monitor,
       "mpbc2RURFL2LD1CurmA": mpbc2RURFL2LD1CurmA,
       "mpbc2RURFL2LD1TempDegCx10": mpbc2RURFL2LD1TempDegCx10,
       "mpbc2RURFL2LD1TECCurmA": mpbc2RURFL2LD1TECCurmA,
       "mpbc2RURFL2LD2CurmA": mpbc2RURFL2LD2CurmA,
       "mpbc2RURFL2CaseTempDegCx10": mpbc2RURFL2CaseTempDegCx10,
       "mpbc2RURFL2SeedPwrmWx100": mpbc2RURFL2SeedPwrmWx100,
       "mpbc2RURFL2WL142xOutPwrmWx10": mpbc2RURFL2WL142xOutPwrmWx10,
       "mpbc2RURFL2WL145xOutPwrmWx10": mpbc2RURFL2WL145xOutPwrmWx10,
       "mpbc2RURFL2TotalOutPwrmWx10": mpbc2RURFL2TotalOutPwrmWx10,
       "mpbc2RURFL2MonLaserState": mpbc2RURFL2MonLaserState,
       "mpbc2RURFL2MonLaserMode": mpbc2RURFL2MonLaserMode,
       "mpbc2RURFL2MonControlMode": mpbc2RURFL2MonControlMode,
       "mpbc2RURFL2DisableInputState": mpbc2RURFL2DisableInputState,
       "mpbc2RURFL2UnitState": mpbc2RURFL2UnitState,
       "mpbc2RURFL2OSCRxTone": mpbc2RURFL2OSCRxTone,
       "mpbc2RURFL2OSCTempDegCx10": mpbc2RURFL2OSCTempDegCx10,
       "mpbc2RURFL2OSCTxTone": mpbc2RURFL2OSCTxTone,
       "mpbc2RURFL2OSCTxPwrmWx100": mpbc2RURFL2OSCTxPwrmWx100,
       "mpbc2RURFL2Configuration": mpbc2RURFL2Configuration,
       "mpbc2RURFL2LD1CurMinThrmA": mpbc2RURFL2LD1CurMinThrmA,
       "mpbc2RURFL2LD1CurMaxThrmA": mpbc2RURFL2LD1CurMaxThrmA,
       "mpbc2RURFL2LD2CurMinThrmA": mpbc2RURFL2LD2CurMinThrmA,
       "mpbc2RURFL2LD2CurMaxThrmA": mpbc2RURFL2LD2CurMaxThrmA,
       "mpbc2RURFL2CaseTempMinSetThrDegCx10": mpbc2RURFL2CaseTempMinSetThrDegCx10,
       "mpbc2RURFL2CaseTempMinClearThrDegCx10": mpbc2RURFL2CaseTempMinClearThrDegCx10,
       "mpbc2RURFL2CaseTempMaxSetThrDegCx10": mpbc2RURFL2CaseTempMaxSetThrDegCx10,
       "mpbc2RURFL2CaseTempMaxClearThrDegCx10": mpbc2RURFL2CaseTempMaxClearThrDegCx10,
       "mpbc2RURFL2WL1OutputMinThrdBx10": mpbc2RURFL2WL1OutputMinThrdBx10,
       "mpbc2RURFL2WL1OutputMaxThrdBx10": mpbc2RURFL2WL1OutputMaxThrdBx10,
       "mpbc2RURFL2WL1FaultSetpointmA": mpbc2RURFL2WL1FaultSetpointmA,
       "mpbc2RURFL2WL1FaultThr": mpbc2RURFL2WL1FaultThr,
       "mpbc2RURFL2WL1FaultDelayms": mpbc2RURFL2WL1FaultDelayms,
       "mpbc2RURFL2WL2OutputMinThrdBx10": mpbc2RURFL2WL2OutputMinThrdBx10,
       "mpbc2RURFL2WL2OutputMaxThrdBx10": mpbc2RURFL2WL2OutputMaxThrdBx10,
       "mpbc2RURFL2CaseTempMinAlrmThrDegCx10": mpbc2RURFL2CaseTempMinAlrmThrDegCx10,
       "mpbc2RURFL2CaseTempMaxAlrmThrDegCx10": mpbc2RURFL2CaseTempMaxAlrmThrDegCx10,
       "mpbc2RURFL2WL2OutputPwrMinLimdBmx10": mpbc2RURFL2WL2OutputPwrMinLimdBmx10,
       "mpbc2RURFL2WL2OutputPwrMaxLimdBmx10": mpbc2RURFL2WL2OutputPwrMaxLimdBmx10,
       "mpbc2RURFL2WL1OutputPwrMinLimdBmx10": mpbc2RURFL2WL1OutputPwrMinLimdBmx10,
       "mpbc2RURFL2WL1OutputPwrMaxLimdBmx10": mpbc2RURFL2WL1OutputPwrMaxLimdBmx10,
       "mpbc2RUSRCP": mpbc2RUSRCP,
       "mpbc2RUSRCPControl": mpbc2RUSRCPControl,
       "mpbc2RUSRCPLaserMode": mpbc2RUSRCPLaserMode,
       "mpbc2RUSRCPControlMode": mpbc2RUSRCPControlMode,
       "mpbc2RUSRCPSeedOutputPwrmW": mpbc2RUSRCPSeedOutputPwrmW,
       "mpbc2RUSRCPMainOutputPwrmW": mpbc2RUSRCPMainOutputPwrmW,
       "mpbc2RUSRCPReset": mpbc2RUSRCPReset,
       "mpbc2RUSRCPMonitor": mpbc2RUSRCPMonitor,
       "mpbc2RUSRCPLD1CurmA": mpbc2RUSRCPLD1CurmA,
       "mpbc2RUSRCPLD1TempDegCx10": mpbc2RUSRCPLD1TempDegCx10,
       "mpbc2RUSRCPLD1TECCurmA": mpbc2RUSRCPLD1TECCurmA,
       "mpbc2RUSRCPLD2CurmA": mpbc2RUSRCPLD2CurmA,
       "mpbc2RUSRCPCaseTempDegCx10": mpbc2RUSRCPCaseTempDegCx10,
       "mpbc2RUSRCPMonSeedOutputPwrmWx10": mpbc2RUSRCPMonSeedOutputPwrmWx10,
       "mpbc2RUSRCPMainOutputPwrmWx10": mpbc2RUSRCPMainOutputPwrmWx10,
       "mpbc2RUSRCPInputPwrmWx100": mpbc2RUSRCPInputPwrmWx100,
       "mpbc2RUSRCPMonLaserState": mpbc2RUSRCPMonLaserState,
       "mpbc2RUSRCPMonLaserMode": mpbc2RUSRCPMonLaserMode,
       "mpbc2RUSRCPMonControlMode": mpbc2RUSRCPMonControlMode,
       "mpbc2RUSRCPDisableInputState": mpbc2RUSRCPDisableInputState,
       "mpbc2RUSRCPUnitState": mpbc2RUSRCPUnitState,
       "mpbc2RUSRCPOSCRxTone": mpbc2RUSRCPOSCRxTone,
       "mpbc2RUSRCPOSCTempdegCx10": mpbc2RUSRCPOSCTempdegCx10,
       "mpbc2RUSRCPOSCTxTone": mpbc2RUSRCPOSCTxTone,
       "mpbc2RUSRCPOSCTxPwrmWx100": mpbc2RUSRCPOSCTxPwrmWx100,
       "mpbc2RUSRCPOSCRx1610Tone": mpbc2RUSRCPOSCRx1610Tone,
       "mpbc2RUSRCPConfiguration": mpbc2RUSRCPConfiguration,
       "mpbc2RUSRCPLD1CurMinThrmA": mpbc2RUSRCPLD1CurMinThrmA,
       "mpbc2RUSRCPLD1CurMaxThrmA": mpbc2RUSRCPLD1CurMaxThrmA,
       "mpbc2RUSRCPLD2CurMinThrmA": mpbc2RUSRCPLD2CurMinThrmA,
       "mpbc2RUSRCPLD2CurMaxThrmA": mpbc2RUSRCPLD2CurMaxThrmA,
       "mpbc2RUSRCPCaseTempMinSetThrDegCx10": mpbc2RUSRCPCaseTempMinSetThrDegCx10,
       "mpbc2RUSRCPCaseTempMinClearThrDegCx10": mpbc2RUSRCPCaseTempMinClearThrDegCx10,
       "mpbc2RUSRCPCaseTempMaxSetThrDegCx10": mpbc2RUSRCPCaseTempMaxSetThrDegCx10,
       "mpbc2RUSRCPCaseTempMaxClearThrDegCx10": mpbc2RUSRCPCaseTempMaxClearThrDegCx10,
       "mpbc2RUSRCPSeedOutputMinThrdBx10": mpbc2RUSRCPSeedOutputMinThrdBx10,
       "mpbc2RUSRCPSeedOutputMaxThrdBx10": mpbc2RUSRCPSeedOutputMaxThrdBx10,
       "mpbc2RUSRCPMainOutputPwrMinThrdBx10": mpbc2RUSRCPMainOutputPwrMinThrdBx10,
       "mpbc2RUSRCPMainOutputPwrMaxThrdBx10": mpbc2RUSRCPMainOutputPwrMaxThrdBx10,
       "mpbc2RUSRCPSeedOutputMinFautThrmW": mpbc2RUSRCPSeedOutputMinFautThrmW,
       "mpbc2RUSRCPCaseTempMinAlrmThrDegCx10": mpbc2RUSRCPCaseTempMinAlrmThrDegCx10,
       "mpbc2RUSRCPCaseTempMaxAlrmThrDegCx10": mpbc2RUSRCPCaseTempMaxAlrmThrDegCx10,
       "mpbc2RUSRCPMainOutputPwrMinLimdBmx10": mpbc2RUSRCPMainOutputPwrMinLimdBmx10,
       "mpbc2RUSRCPMainOutputPwrMaxLimdBmx10": mpbc2RUSRCPMainOutputPwrMaxLimdBmx10,
       "mpbc2RUSRCPSeedOutputPwrMinLimdBmx10": mpbc2RUSRCPSeedOutputPwrMinLimdBmx10,
       "mpbc2RUSRCPSeedOutputPwrMaxLimdBmx10": mpbc2RUSRCPSeedOutputPwrMaxLimdBmx10,
       "mpbc2RUSRCPAPLSetThrdBmx10": mpbc2RUSRCPAPLSetThrdBmx10,
       "mpbc2RUSRCPAPLClearThrdBmx10": mpbc2RUSRCPAPLClearThrdBmx10,
       "mpbc2RUSRCPAPLMainOutputPwrdBmx10": mpbc2RUSRCPAPLMainOutputPwrdBmx10,
       "mpbc2RUSRCPOSCMode": mpbc2RUSRCPOSCMode,
       "mpbc2RUSRCPSeedFaultDelayms": mpbc2RUSRCPSeedFaultDelayms,
       "mpbc2RUMLD": mpbc2RUMLD,
       "mpbc2RUMLDControl": mpbc2RUMLDControl,
       "mpbc2RUMLDLaserMode": mpbc2RUMLDLaserMode,
       "mpbc2RUMLDControlMode": mpbc2RUMLDControlMode,
       "mpbc2RUMLD1stWLPwrSetPtmW": mpbc2RUMLD1stWLPwrSetPtmW,
       "mpbc2RUMLD2ndWLPwrSetPtmW": mpbc2RUMLD2ndWLPwrSetPtmW,
       "mpbc2RUMLDReset": mpbc2RUMLDReset,
       "mpbc2RUMLDMonitor": mpbc2RUMLDMonitor,
       "mpbc2RUMLDLD1CurmA": mpbc2RUMLDLD1CurmA,
       "mpbc2RUMLDLD1TempDegCx10": mpbc2RUMLDLD1TempDegCx10,
       "mpbc2RUMLDLD1TECCurmA": mpbc2RUMLDLD1TECCurmA,
       "mpbc2RUMLDLD2CurmA": mpbc2RUMLDLD2CurmA,
       "mpbc2RUMLDLD2TempDegCx10": mpbc2RUMLDLD2TempDegCx10,
       "mpbc2RUMLDLD2TECCurmA": mpbc2RUMLDLD2TECCurmA,
       "mpbc2RUMLDCaseTempDegCx10": mpbc2RUMLDCaseTempDegCx10,
       "mpbc2RUMLDMon1stWLOutputPwrmWx10": mpbc2RUMLDMon1stWLOutputPwrmWx10,
       "mpbc2RUMLDMon2ndWLOutputPwrmWx10": mpbc2RUMLDMon2ndWLOutputPwrmWx10,
       "mpbc2RUMLDInputPwrmWx100": mpbc2RUMLDInputPwrmWx100,
       "mpbc2RUMLDMonLaserState": mpbc2RUMLDMonLaserState,
       "mpbc2RUMLDMonLaserMode": mpbc2RUMLDMonLaserMode,
       "mpbc2RUMLDMonControlMode": mpbc2RUMLDMonControlMode,
       "mpbc2RUMLDDisableInputState": mpbc2RUMLDDisableInputState,
       "mpbc2RUMLDUnitState": mpbc2RUMLDUnitState,
       "mpbc2RUMLDOSCRx1574Tone": mpbc2RUMLDOSCRx1574Tone,
       "mpbc2RUMLDOSCTempdegCx10": mpbc2RUMLDOSCTempdegCx10,
       "mpbc2RUMLDOSCTxTone": mpbc2RUMLDOSCTxTone,
       "mpbc2RUMLDOSCTxPwrmWx100": mpbc2RUMLDOSCTxPwrmWx100,
       "mpbc2RUMLDOSCRx1610Tone": mpbc2RUMLDOSCRx1610Tone,
       "mpbc2RUMLDConfiguration": mpbc2RUMLDConfiguration,
       "mpbc2RUMLDLD1CurMinThrmA": mpbc2RUMLDLD1CurMinThrmA,
       "mpbc2RUMLDLD1CurMaxThrmA": mpbc2RUMLDLD1CurMaxThrmA,
       "mpbc2RUMLDLD2CurMinThrmA": mpbc2RUMLDLD2CurMinThrmA,
       "mpbc2RUMLDLD2CurMaxThrmA": mpbc2RUMLDLD2CurMaxThrmA,
       "mpbc2RUMLDCaseTempMinSetThrDegCx10": mpbc2RUMLDCaseTempMinSetThrDegCx10,
       "mpbc2RUMLDCaseTempMinClearThrDegCx10": mpbc2RUMLDCaseTempMinClearThrDegCx10,
       "mpbc2RUMLDCaseTempMaxSetThrDegCx10": mpbc2RUMLDCaseTempMaxSetThrDegCx10,
       "mpbc2RUMLDCaseTempMaxClearThrDegCx10": mpbc2RUMLDCaseTempMaxClearThrDegCx10,
       "mpbc2RUMLDCaseTempMinAlrmThrDegCx10": mpbc2RUMLDCaseTempMinAlrmThrDegCx10,
       "mpbc2RUMLDCaseTempMaxAlrmThrDegCx10": mpbc2RUMLDCaseTempMaxAlrmThrDegCx10,
       "mpbc2RUMLD1stWLOutputPwrMinThrdBx10": mpbc2RUMLD1stWLOutputPwrMinThrdBx10,
       "mpbc2RUMLD1stWLOutputPwrMaxThrdBx10": mpbc2RUMLD1stWLOutputPwrMaxThrdBx10,
       "mpbc2RUMLD2ndWLOutputPwrMinThrdBx10": mpbc2RUMLD2ndWLOutputPwrMinThrdBx10,
       "mpbc2RUMLD2ndWLOutputPwrMaxThrdBx10": mpbc2RUMLD2ndWLOutputPwrMaxThrdBx10,
       "mpbc2RUMLD1stWLOutputPwrMinLimdBmx10": mpbc2RUMLD1stWLOutputPwrMinLimdBmx10,
       "mpbc2RUMLD1stWLOutputPwrMaxLimdBmx10": mpbc2RUMLD1stWLOutputPwrMaxLimdBmx10,
       "mpbc2RUMLD2ndWLOutputPwrMinLimdBmx10": mpbc2RUMLD2ndWLOutputPwrMinLimdBmx10,
       "mpbc2RUMLD2ndWLOutputPwrMaxLimdBmx10": mpbc2RUMLD2ndWLOutputPwrMaxLimdBmx10,
       "mpbc2RUMLDOSCMode": mpbc2RUMLDOSCMode,
       "mpbc2RUPY": mpbc2RUPY,
       "mpbc2RUPYControl": mpbc2RUPYControl,
       "mpbc2RUPYLaserMode": mpbc2RUPYLaserMode,
       "mpbc2RUPYControlMode": mpbc2RUPYControlMode,
       "mpbc2RUPYPreAmpSetPtmW": mpbc2RUPYPreAmpSetPtmW,
       "mpbc2RUPYPwrSetPtmW": mpbc2RUPYPwrSetPtmW,
       "mpbc2RUPYGainSetPtdBx10": mpbc2RUPYGainSetPtdBx10,
       "mpbc2RUPYVoaSetPtdBx10": mpbc2RUPYVoaSetPtdBx10,
       "mpbc2RUPYReset": mpbc2RUPYReset,
       "mpbc2RUPYMonitor": mpbc2RUPYMonitor,
       "mpbc2RUPYLD1CurmA": mpbc2RUPYLD1CurmA,
       "mpbc2RUPYLD1TempDegCx10": mpbc2RUPYLD1TempDegCx10,
       "mpbc2RUPYLD1TECCurmA": mpbc2RUPYLD1TECCurmA,
       "mpbc2RUPYLD2CurmA": mpbc2RUPYLD2CurmA,
       "mpbc2RUPYCaseTempDegCx10": mpbc2RUPYCaseTempDegCx10,
       "mpbc2RUPYMonPreAmpPumpPwrmWx10": mpbc2RUPYMonPreAmpPumpPwrmWx10,
       "mpbc2RUPYMainOutputPwrmWx10": mpbc2RUPYMainOutputPwrmWx10,
       "mpbc2RUPYGaindBx10": mpbc2RUPYGaindBx10,
       "mpbc2RUPYInputPwrmWx100": mpbc2RUPYInputPwrmWx100,
       "mpbc2RUPYBackReflPwrmWx100": mpbc2RUPYBackReflPwrmWx100,
       "mpbc2RUPYMonLaserState": mpbc2RUPYMonLaserState,
       "mpbc2RUPYMonLaserMode": mpbc2RUPYMonLaserMode,
       "mpbc2RUPYMonControlMode": mpbc2RUPYMonControlMode,
       "mpbc2RUPYDisableInputState": mpbc2RUPYDisableInputState,
       "mpbc2RUPYUnitState": mpbc2RUPYUnitState,
       "mpbc2RUPYOSCRxTone": mpbc2RUPYOSCRxTone,
       "mpbc2RUPYOSCTempDegCx10": mpbc2RUPYOSCTempDegCx10,
       "mpbc2RUPYOSCTxTone": mpbc2RUPYOSCTxTone,
       "mpbc2RUPYOSCTxPwrmWx100": mpbc2RUPYOSCTxPwrmWx100,
       "mpbc2RUPYOSCRx1610Tone": mpbc2RUPYOSCRx1610Tone,
       "mpbc2RUPYVOASettingdBx10": mpbc2RUPYVOASettingdBx10,
       "mpbc2RUPYConfiguration": mpbc2RUPYConfiguration,
       "mpbc2RUPYLD1CurMinThrmA": mpbc2RUPYLD1CurMinThrmA,
       "mpbc2RUPYLD1CurMaxThrmA": mpbc2RUPYLD1CurMaxThrmA,
       "mpbc2RUPYLD2CurMinThrmA": mpbc2RUPYLD2CurMinThrmA,
       "mpbc2RUPYLD2CurMaxThrmA": mpbc2RUPYLD2CurMaxThrmA,
       "mpbc2RUPYCaseTempMinSetThrDegCx10": mpbc2RUPYCaseTempMinSetThrDegCx10,
       "mpbc2RUPYCaseTempMinClearThrDegCx10": mpbc2RUPYCaseTempMinClearThrDegCx10,
       "mpbc2RUPYCaseTempMaxSetThrDegCx10": mpbc2RUPYCaseTempMaxSetThrDegCx10,
       "mpbc2RUPYCaseTempMaxClearThrDegCx10": mpbc2RUPYCaseTempMaxClearThrDegCx10,
       "mpbc2RUPYCaseTempMinAlrmThrDegCx10": mpbc2RUPYCaseTempMinAlrmThrDegCx10,
       "mpbc2RUPYCaseTempMaxAlrmThrDegCx10": mpbc2RUPYCaseTempMaxAlrmThrDegCx10,
       "mpbc2RUPYLOSSetThrdBmx100": mpbc2RUPYLOSSetThrdBmx100,
       "mpbc2RUPYLOSClearThrdBmx100": mpbc2RUPYLOSClearThrdBmx100,
       "mpbc2RUPYInputMinThrdBmx100": mpbc2RUPYInputMinThrdBmx100,
       "mpbc2RUPYInputMaxThrdBmx100": mpbc2RUPYInputMaxThrdBmx100,
       "mpbc2RUPYMainOutputMinThrdBx10": mpbc2RUPYMainOutputMinThrdBx10,
       "mpbc2RUPYMainOutputMaxThrdBx10": mpbc2RUPYMainOutputMaxThrdBx10,
       "mpbc2RUPYPreampPwrMinThrdBx10": mpbc2RUPYPreampPwrMinThrdBx10,
       "mpbc2RUPYPreampPwrMaxThrdBx10": mpbc2RUPYPreampPwrMaxThrdBx10,
       "mpbc2RUPYOSCMode": mpbc2RUPYOSCMode,
       "mpbc2RUPYOutputPwrSetpointMindBmx10": mpbc2RUPYOutputPwrSetpointMindBmx10,
       "mpbc2RUPYOutputPwrSetpointMaxdBmx10": mpbc2RUPYOutputPwrSetpointMaxdBmx10,
       "mpbc2RUPYGainSetPointMindBx10": mpbc2RUPYGainSetPointMindBx10,
       "mpbc2RUPYGainSetPointMaxdBx10": mpbc2RUPYGainSetPointMaxdBx10,
       "mpbc2RUPYPreAmpFaultThrmW": mpbc2RUPYPreAmpFaultThrmW,
       "mpbc2RUPYPreAmpFaultDelayms": mpbc2RUPYPreAmpFaultDelayms,
       "mpbc2RUSRP": mpbc2RUSRP,
       "mpbc2RUSRPControl": mpbc2RUSRPControl,
       "mpbc2RUSRPLaserMode": mpbc2RUSRPLaserMode,
       "mpbc2RUSRPControlMode": mpbc2RUSRPControlMode,
       "mpbc2RUSRPSeedOutputPwrSetPtmW": mpbc2RUSRPSeedOutputPwrSetPtmW,
       "mpbc2RUSRPMainOutputPwrSetPtmW": mpbc2RUSRPMainOutputPwrSetPtmW,
       "mpbc2RUSRPReset": mpbc2RUSRPReset,
       "mpbc2RUSRPMonitor": mpbc2RUSRPMonitor,
       "mpbc2RUSRPLD1CurmA": mpbc2RUSRPLD1CurmA,
       "mpbc2RUSRPLD1TempDegCx10": mpbc2RUSRPLD1TempDegCx10,
       "mpbc2RUSRPLD1TECCurmA": mpbc2RUSRPLD1TECCurmA,
       "mpbc2RUSRPLD2CurmA": mpbc2RUSRPLD2CurmA,
       "mpbc2RUSRPCaseTempDegCx10": mpbc2RUSRPCaseTempDegCx10,
       "mpbc2RUSRPMonSeedOutputPwrmWx10": mpbc2RUSRPMonSeedOutputPwrmWx10,
       "mpbc2RUSRPMainOutputPwrmWx10": mpbc2RUSRPMainOutputPwrmWx10,
       "mpbc2RUSRPMonLaserState": mpbc2RUSRPMonLaserState,
       "mpbc2RUSRPMonLaserMode": mpbc2RUSRPMonLaserMode,
       "mpbc2RUSRPMonControlMode": mpbc2RUSRPMonControlMode,
       "mpbc2RUSRPDisableInputState": mpbc2RUSRPDisableInputState,
       "mpbc2RUSRPUnitState": mpbc2RUSRPUnitState,
       "mpbc2RUSRPOSCRxTone": mpbc2RUSRPOSCRxTone,
       "mpbc2RUSRPOSCTempdegCx10": mpbc2RUSRPOSCTempdegCx10,
       "mpbc2RUSRPOSCTxTone": mpbc2RUSRPOSCTxTone,
       "mpbc2RUSRPOSCTxPwrmWx100": mpbc2RUSRPOSCTxPwrmWx100,
       "mpbc2RUSRPConfiguration": mpbc2RUSRPConfiguration,
       "mpbc2RUSRPLD1CurMinThrmA": mpbc2RUSRPLD1CurMinThrmA,
       "mpbc2RUSRPLD1CurMaxThrmA": mpbc2RUSRPLD1CurMaxThrmA,
       "mpbc2RUSRPLD2CurMinThrmA": mpbc2RUSRPLD2CurMinThrmA,
       "mpbc2RUSRPLD2CurMaxThrmA": mpbc2RUSRPLD2CurMaxThrmA,
       "mpbc2RUSRPCaseTempMinSetThrDegCx10": mpbc2RUSRPCaseTempMinSetThrDegCx10,
       "mpbc2RUSRPCaseTempMinClearThrDegCx10": mpbc2RUSRPCaseTempMinClearThrDegCx10,
       "mpbc2RUSRPCaseTempMaxSetThrDegCx10": mpbc2RUSRPCaseTempMaxSetThrDegCx10,
       "mpbc2RUSRPCaseTempMaxClearThrDegCx10": mpbc2RUSRPCaseTempMaxClearThrDegCx10,
       "mpbc2RUSRPMainOutputMinThrdBx10": mpbc2RUSRPMainOutputMinThrdBx10,
       "mpbc2RUSRPMainOutputMaxThrdBx10": mpbc2RUSRPMainOutputMaxThrdBx10,
       "mpbc2RUSRPCaseTempMinAlrmThrDegCx10": mpbc2RUSRPCaseTempMinAlrmThrDegCx10,
       "mpbc2RUSRPCaseTempMaxAlrmThrDegCx10": mpbc2RUSRPCaseTempMaxAlrmThrDegCx10,
       "mpbc2RUSRPSeedOutputPwrMinThrdBx10": mpbc2RUSRPSeedOutputPwrMinThrdBx10,
       "mpbc2RUSRPSeedOutputPwrMaxThrdBx10": mpbc2RUSRPSeedOutputPwrMaxThrdBx10,
       "mpbc2RUSRPSeedOutputMinFaultThrmW": mpbc2RUSRPSeedOutputMinFaultThrmW,
       "mpbc2RUSRPMainOutputPwrMinLimdBmx10": mpbc2RUSRPMainOutputPwrMinLimdBmx10,
       "mpbc2RUSRPMainOutputPwrMaxLimdBmx10": mpbc2RUSRPMainOutputPwrMaxLimdBmx10,
       "mpbc2RUSRPSeedOutputPwrMinLimdBmx10": mpbc2RUSRPSeedOutputPwrMinLimdBmx10,
       "mpbc2RUSRPSeedOutputPwrMaxLimdBmx10": mpbc2RUSRPSeedOutputPwrMaxLimdBmx10,
       "mpbc2RUSRPSeedFaultDelayms": mpbc2RUSRPSeedFaultDelayms,
       "mpbc2RUCRP": mpbc2RUCRP,
       "mpbc2RUCRPControl": mpbc2RUCRPControl,
       "mpbc2RUCRPLaserMode": mpbc2RUCRPLaserMode,
       "mpbc2RUCRPControlMode": mpbc2RUCRPControlMode,
       "mpbc2RUCRPSeedOutputPwrSetPtmW": mpbc2RUCRPSeedOutputPwrSetPtmW,
       "mpbc2RUCRPMainOutputPwrSetPtmW": mpbc2RUCRPMainOutputPwrSetPtmW,
       "mpbc2RUCRPReset": mpbc2RUCRPReset,
       "mpbc2RUCRPMonitor": mpbc2RUCRPMonitor,
       "mpbc2RUCRPLD1CurmA": mpbc2RUCRPLD1CurmA,
       "mpbc2RUCRPLD1TempDegCx10": mpbc2RUCRPLD1TempDegCx10,
       "mpbc2RUCRPLD1TECCurmA": mpbc2RUCRPLD1TECCurmA,
       "mpbc2RUCRPLD2CurmA": mpbc2RUCRPLD2CurmA,
       "mpbc2RUCRPCaseTempDegCx10": mpbc2RUCRPCaseTempDegCx10,
       "mpbc2RUCRPMonSeedOutputPwrmWx10": mpbc2RUCRPMonSeedOutputPwrmWx10,
       "mpbc2RUCRPMainOutputPwrmWx10": mpbc2RUCRPMainOutputPwrmWx10,
       "mpbc2RUCRPMonLaserState": mpbc2RUCRPMonLaserState,
       "mpbc2RUCRPMonLaserMode": mpbc2RUCRPMonLaserMode,
       "mpbc2RUCRPMonControlMode": mpbc2RUCRPMonControlMode,
       "mpbc2RUCRPDisableInputState": mpbc2RUCRPDisableInputState,
       "mpbc2RUCRPUnitState": mpbc2RUCRPUnitState,
       "mpbc2RUCRPOSCRx1574Tone": mpbc2RUCRPOSCRx1574Tone,
       "mpbc2RUCRPOSCTempdegCx10": mpbc2RUCRPOSCTempdegCx10,
       "mpbc2RUCRPOSCTx1610Tone": mpbc2RUCRPOSCTx1610Tone,
       "mpbc2RUCRPOSCTxPwrmWx100": mpbc2RUCRPOSCTxPwrmWx100,
       "mpbc2RUCRPOSCRx1610Tone": mpbc2RUCRPOSCRx1610Tone,
       "mpbc2RUCRPConfiguration": mpbc2RUCRPConfiguration,
       "mpbc2RUCRPLD1CurMinThrmA": mpbc2RUCRPLD1CurMinThrmA,
       "mpbc2RUCRPLD1CurMaxThrmA": mpbc2RUCRPLD1CurMaxThrmA,
       "mpbc2RUCRPLD2CurMinThrmA": mpbc2RUCRPLD2CurMinThrmA,
       "mpbc2RUCRPLD2CurMaxThrmA": mpbc2RUCRPLD2CurMaxThrmA,
       "mpbc2RUCRPCaseTempMinSetThrDegCx10": mpbc2RUCRPCaseTempMinSetThrDegCx10,
       "mpbc2RUCRPCaseTempMinClearThrDegCx10": mpbc2RUCRPCaseTempMinClearThrDegCx10,
       "mpbc2RUCRPCaseTempMaxSetThrDegCx10": mpbc2RUCRPCaseTempMaxSetThrDegCx10,
       "mpbc2RUCRPCaseTempMaxClearThrDegCx10": mpbc2RUCRPCaseTempMaxClearThrDegCx10,
       "mpbc2RUCRPMainOutputMinThrdBx10": mpbc2RUCRPMainOutputMinThrdBx10,
       "mpbc2RUCRPMainOutputMaxThrdBx10": mpbc2RUCRPMainOutputMaxThrdBx10,
       "mpbc2RUCRPCaseTempMinAlrmThrDegCx10": mpbc2RUCRPCaseTempMinAlrmThrDegCx10,
       "mpbc2RUCRPCaseTempMaxAlrmThrDegCx10": mpbc2RUCRPCaseTempMaxAlrmThrDegCx10,
       "mpbc2RUCRPSeedOutputPwrMinThrdBx10": mpbc2RUCRPSeedOutputPwrMinThrdBx10,
       "mpbc2RUCRPSeedOutputPwrMaxThrdBx10": mpbc2RUCRPSeedOutputPwrMaxThrdBx10,
       "mpbc2RUCRPSeedOutputMinFaultThrmW": mpbc2RUCRPSeedOutputMinFaultThrmW,
       "mpbc2RUCRPMainOutputPwrMinLimdBmx10": mpbc2RUCRPMainOutputPwrMinLimdBmx10,
       "mpbc2RUCRPMainOutputPwrMaxLimdBmx10": mpbc2RUCRPMainOutputPwrMaxLimdBmx10,
       "mpbc2RUCRPSeedOutputPwrMinLimdBmx10": mpbc2RUCRPSeedOutputPwrMinLimdBmx10,
       "mpbc2RUCRPSeedOutputPwrMaxLimdBmx10": mpbc2RUCRPSeedOutputPwrMaxLimdBmx10,
       "mpbc2RUCRPSeedFaultDelayms": mpbc2RUCRPSeedFaultDelayms,
       "mpbc2RUCRPOSCMode": mpbc2RUCRPOSCMode,
       "mpbc2RURFL148x": mpbc2RURFL148x,
       "mpbc2RURFL148xControl": mpbc2RURFL148xControl,
       "mpbc2RURFL148xLaserMode": mpbc2RURFL148xLaserMode,
       "mpbc2RURFL148xControlMode": mpbc2RURFL148xControlMode,
       "mpbc2RURFL148xPwrSetPtmW": mpbc2RURFL148xPwrSetPtmW,
       "mpbc2RURFL148xReset": mpbc2RURFL148xReset,
       "mpbc2RURFL148xMonitor": mpbc2RURFL148xMonitor,
       "mpbc2RURFL148xLD1Current": mpbc2RURFL148xLD1Current,
       "mpbc2RURFL148xLD2Current": mpbc2RURFL148xLD2Current,
       "mpbc2RURFL148xCaseTempDegCx10": mpbc2RURFL148xCaseTempDegCx10,
       "mpbc2RURFL148xOutputPwrmW": mpbc2RURFL148xOutputPwrmW,
       "mpbc2RURFL148xMonLaserState": mpbc2RURFL148xMonLaserState,
       "mpbc2RURFL148xMonLaserMode": mpbc2RURFL148xMonLaserMode,
       "mpbc2RURFL148xMonControlMode": mpbc2RURFL148xMonControlMode,
       "mpbc2RURFL148xDisableInputState": mpbc2RURFL148xDisableInputState,
       "mpbc2RURFL148xUnitState": mpbc2RURFL148xUnitState,
       "mpbc2RURFL148xOSCRx1574Tone": mpbc2RURFL148xOSCRx1574Tone,
       "mpbc2RURFL148xOSCTempDegCx10": mpbc2RURFL148xOSCTempDegCx10,
       "mpbc2RURFL148xOSCTxTone": mpbc2RURFL148xOSCTxTone,
       "mpbc2RURFL148xOSCTxPwrmWx100": mpbc2RURFL148xOSCTxPwrmWx100,
       "mpbc2RURFL148xOSCRx1610Tone": mpbc2RURFL148xOSCRx1610Tone,
       "mpbc2RURFL148xConfiguration": mpbc2RURFL148xConfiguration,
       "mpbc2RURFL148xAlarmPwrThrLowdBx10": mpbc2RURFL148xAlarmPwrThrLowdBx10,
       "mpbc2RURFL148xAlarmPwrThrHidBx10": mpbc2RURFL148xAlarmPwrThrHidBx10,
       "mpbc2RURFL148xAlarmCaseTempMinThDegCx10": mpbc2RURFL148xAlarmCaseTempMinThDegCx10,
       "mpbc2RURFL148xAlarmCaseTempMaxThDegCx10": mpbc2RURFL148xAlarmCaseTempMaxThDegCx10,
       "mpbc2RURFL148xLD1CurMinThrmA": mpbc2RURFL148xLD1CurMinThrmA,
       "mpbc2RURFL148xLD1CurMaxThrmA": mpbc2RURFL148xLD1CurMaxThrmA,
       "mpbc2RURFL148xLD2CurMinThrmA": mpbc2RURFL148xLD2CurMinThrmA,
       "mpbc2RURFL148xLD2CurMaxThrmA": mpbc2RURFL148xLD2CurMaxThrmA,
       "mpbc2RURFL148xCaseTempMinSetThrDegCx10": mpbc2RURFL148xCaseTempMinSetThrDegCx10,
       "mpbc2RURFL148xCaseTempMinClearThrDegCx10": mpbc2RURFL148xCaseTempMinClearThrDegCx10,
       "mpbc2RURFL148xCaseTempMaxSetThrDegCx10": mpbc2RURFL148xCaseTempMaxSetThrDegCx10,
       "mpbc2RURFL148xCaseTempMaxClearThrDegCx10": mpbc2RURFL148xCaseTempMaxClearThrDegCx10,
       "mpbc2RURFL148xOutputPwrSetptMindBmx10": mpbc2RURFL148xOutputPwrSetptMindBmx10,
       "mpbc2RURFL148xOutputPwrSetptMaxdBmx10": mpbc2RURFL148xOutputPwrSetptMaxdBmx10,
       "mpbc2RURFL148xOSCMode": mpbc2RURFL148xOSCMode,
       "mpbc2RULDP": mpbc2RULDP,
       "mpbc2RULDPControl": mpbc2RULDPControl,
       "mpbc2RULDPLaserMode": mpbc2RULDPLaserMode,
       "mpbc2RULDPControlMode": mpbc2RULDPControlMode,
       "mpbc2RULDP1stWLPwrSetPtmW": mpbc2RULDP1stWLPwrSetPtmW,
       "mpbc2RULDP2ndWLPwrSetPtmW": mpbc2RULDP2ndWLPwrSetPtmW,
       "mpbc2RULDPReset": mpbc2RULDPReset,
       "mpbc2RULDPMonitor": mpbc2RULDPMonitor,
       "mpbc2RULDPLD1CurmA": mpbc2RULDPLD1CurmA,
       "mpbc2RULDPLD1TempDegCx10": mpbc2RULDPLD1TempDegCx10,
       "mpbc2RULDPLD1TECCurmA": mpbc2RULDPLD1TECCurmA,
       "mpbc2RULDPLD2CurmA": mpbc2RULDPLD2CurmA,
       "mpbc2RULDPLD2TempDegCx10": mpbc2RULDPLD2TempDegCx10,
       "mpbc2RULDPLD2TECCurmA": mpbc2RULDPLD2TECCurmA,
       "mpbc2RULDPCaseTempDegCx10": mpbc2RULDPCaseTempDegCx10,
       "mpbc2RULDPMon1stWLOutputPwrmWx10": mpbc2RULDPMon1stWLOutputPwrmWx10,
       "mpbc2RULDPMon2ndWLOutputPwrmWx10": mpbc2RULDPMon2ndWLOutputPwrmWx10,
       "mpbc2RULDPMonLaserState": mpbc2RULDPMonLaserState,
       "mpbc2RULDPMonLaserMode": mpbc2RULDPMonLaserMode,
       "mpbc2RULDPMonControlMode": mpbc2RULDPMonControlMode,
       "mpbc2RULDPDisableInputState": mpbc2RULDPDisableInputState,
       "mpbc2RULDPUnitState": mpbc2RULDPUnitState,
       "mpbc2RULDPOSCRxTone": mpbc2RULDPOSCRxTone,
       "mpbc2RULDPOSCTempDegCx10": mpbc2RULDPOSCTempDegCx10,
       "mpbc2RULDPOSCTxTone": mpbc2RULDPOSCTxTone,
       "mpbc2RULDPOSCTxPwrmWx100": mpbc2RULDPOSCTxPwrmWx100,
       "mpbc2RULDPConfiguration": mpbc2RULDPConfiguration,
       "mpbc2RULDPLD1CurMinThrmA": mpbc2RULDPLD1CurMinThrmA,
       "mpbc2RULDPLD1CurMaxThrmA": mpbc2RULDPLD1CurMaxThrmA,
       "mpbc2RULDPLD2CurMinThrmA": mpbc2RULDPLD2CurMinThrmA,
       "mpbc2RULDPLD2CurMaxThrmA": mpbc2RULDPLD2CurMaxThrmA,
       "mpbc2RULDPCaseTempMinSetThrDegCx10": mpbc2RULDPCaseTempMinSetThrDegCx10,
       "mpbc2RULDPCaseTempMinClearThrDegCx10": mpbc2RULDPCaseTempMinClearThrDegCx10,
       "mpbc2RULDPCaseTempMaxSetThrDegCx10": mpbc2RULDPCaseTempMaxSetThrDegCx10,
       "mpbc2RULDPCaseTempMaxClearThrDegCx10": mpbc2RULDPCaseTempMaxClearThrDegCx10,
       "mpbc2RULDPCaseTempMinAlrmThDegCx10": mpbc2RULDPCaseTempMinAlrmThDegCx10,
       "mpbc2RULDPCaseTempMaxAlrmThDegCx10": mpbc2RULDPCaseTempMaxAlrmThDegCx10,
       "mpbc2RULDP1stWLOutputPwrMinThrdBx10": mpbc2RULDP1stWLOutputPwrMinThrdBx10,
       "mpbc2RULDP1stWLOutputPwrMaxThrdBx10": mpbc2RULDP1stWLOutputPwrMaxThrdBx10,
       "mpbc2RULDP2ndWLOutputPwrMinThrdBx10": mpbc2RULDP2ndWLOutputPwrMinThrdBx10,
       "mpbc2RULDP2ndWLOutputPwrMaxThrdBx10": mpbc2RULDP2ndWLOutputPwrMaxThrdBx10,
       "mpbc2RULDP1stWLOutputPwrMinLimdBmx10": mpbc2RULDP1stWLOutputPwrMinLimdBmx10,
       "mpbc2RULDP1stWLOutputPwrMaxLimdBmx10": mpbc2RULDP1stWLOutputPwrMaxLimdBmx10,
       "mpbc2RULDP2ndWLOutputPwrMinLimdBmx10": mpbc2RULDP2ndWLOutputPwrMinLimdBmx10,
       "mpbc2RULDP2ndWLOutputPwrMaxLimdBmx10": mpbc2RULDP2ndWLOutputPwrMaxLimdBmx10,
       "mpbc2RUConfiguration": mpbc2RUConfiguration,
       "mpbc2RUNetMgt": mpbc2RUNetMgt,
       "mpbc2RUNotifiedNMSipAddressTable": mpbc2RUNotifiedNMSipAddressTable,
       "mpbc2RUNotifiedNMSipAddressEntry": mpbc2RUNotifiedNMSipAddressEntry,
       "mpbc2RUNotifiedNMSipAddressIndex": mpbc2RUNotifiedNMSipAddressIndex,
       "mpbc2RUNotifiedNMSipAddress-IP": mpbc2RUNotifiedNMSipAddress_IP,
       "mpbc2RUNotifiedNMSipAddress-Description": mpbc2RUNotifiedNMSipAddress_Description,
       "mpbc2RUNotifiedNMSipAddress-Enabled": mpbc2RUNotifiedNMSipAddress_Enabled,
       "mpbc2RUAckTrapControl": mpbc2RUAckTrapControl,
       "mpbc2RUAckTrapCriticalEnable": mpbc2RUAckTrapCriticalEnable,
       "mpbc2RUAckTrapCriticalRetries": mpbc2RUAckTrapCriticalRetries,
       "mpbc2RUAckTrapCriticalTimeOutsec": mpbc2RUAckTrapCriticalTimeOutsec,
       "mpbc2RUAckTrapMajorEnable": mpbc2RUAckTrapMajorEnable,
       "mpbc2RUAckTrapMajorRetries": mpbc2RUAckTrapMajorRetries,
       "mpbc2RUAckTrapMajorTimeOutsec": mpbc2RUAckTrapMajorTimeOutsec,
       "mpbc2RUAckTrapMinorEnable": mpbc2RUAckTrapMinorEnable,
       "mpbc2RUAckTrapMinorRetries": mpbc2RUAckTrapMinorRetries,
       "mpbc2RUAckTrapMinorTimeOutsec": mpbc2RUAckTrapMinorTimeOutsec,
       "mpbc2RUAckTrapInformationalEnable": mpbc2RUAckTrapInformationalEnable,
       "mpbc2RUAckTrapInformationalRetries": mpbc2RUAckTrapInformationalRetries,
       "mpbc2RUAckTrapInformationalTimeOutsec": mpbc2RUAckTrapInformationalTimeOutsec,
       "mpbc2RUTrapControl": mpbc2RUTrapControl,
       "mpbc2RUTrapCriticalEnable": mpbc2RUTrapCriticalEnable,
       "mpbc2RUTrapMajorEnable": mpbc2RUTrapMajorEnable,
       "mpbc2RUTrapMinorEnable": mpbc2RUTrapMinorEnable,
       "mpbc2RUTrapInformationalEnable": mpbc2RUTrapInformationalEnable,
       "mpbc2RUMacAddress": mpbc2RUMacAddress,
       "mpbc2RUEthernetIPaddress": mpbc2RUEthernetIPaddress,
       "mpbc2RUEthernetIPsubNetMask": mpbc2RUEthernetIPsubNetMask,
       "mpbc2RUDefaultGateway": mpbc2RUDefaultGateway,
       "mpbc2RUSnmpTrapPort": mpbc2RUSnmpTrapPort,
       "mpbc2RUNE": mpbc2RUNE,
       "mpbc2RUNEID": mpbc2RUNEID,
       "mpbc2RUInfoTable": mpbc2RUInfoTable,
       "mpbc2RUInfoEntry": mpbc2RUInfoEntry,
       "mpbc2RUInfoIndex": mpbc2RUInfoIndex,
       "mpbc2RUInfoLoc": mpbc2RUInfoLoc,
       "mpbc2RUInfoModelNum": mpbc2RUInfoModelNum,
       "mpbc2RUInfoModelSN": mpbc2RUInfoModelSN,
       "mpbc2RUInfoOEMPartNum": mpbc2RUInfoOEMPartNum,
       "mpbc2RUInfoAssyNum": mpbc2RUInfoAssyNum,
       "mpbc2RUInfoRev": mpbc2RUInfoRev,
       "mpbc2RUInfoECN": mpbc2RUInfoECN,
       "mpbc2RUInfoSeqNum": mpbc2RUInfoSeqNum,
       "mpbc2RUInfoMfgDate": mpbc2RUInfoMfgDate,
       "mpbc2RUInfoSwVer": mpbc2RUInfoSwVer,
       "mpbc2RUInfoBootLoaderRev": mpbc2RUInfoBootLoaderRev,
       "mpbc2RUInfoLibRev": mpbc2RUInfoLibRev,
       "mpbc2RUInfoLddFw1": mpbc2RUInfoLddFw1,
       "mpbc2RUInfoLddFw2": mpbc2RUInfoLddFw2,
       "mpbc2RUInfoCLEI": mpbc2RUInfoCLEI,
       "mpbc2RUInfoLastRmaDate": mpbc2RUInfoLastRmaDate,
       "mpbc2RUDateTime": mpbc2RUDateTime,
       "mpbc2RUSNMPAgentVersion": mpbc2RUSNMPAgentVersion,
       "mpbc2RUSNMPMIBVersion": mpbc2RUSNMPMIBVersion,
       "mpbc2RUSNMPMemoryConfig": mpbc2RUSNMPMemoryConfig,
       "mpbc2RUSNMPMemorySave": mpbc2RUSNMPMemorySave,
       "mpbc2RUSNMPMemoryRestore": mpbc2RUSNMPMemoryRestore,
       "mpbc2RUConformance": mpbc2RUConformance,
       "mpbc2RUGroups": mpbc2RUGroups,
       "mpbc2RUMibAllObjects": mpbc2RUMibAllObjects,
       "mpbc2RUMibAllNotifications": mpbc2RUMibAllNotifications,
       "mpbc2ruMibAllObjects": mpbc2ruMibAllObjects,
       "mpbc2RUMLDS": mpbc2RUMLDS,
       "mpbc2RUMLDSControl": mpbc2RUMLDSControl,
       "mpbc2RUMLDSLaserMode": mpbc2RUMLDSLaserMode,
       "mpbc2RUMLDSControlMode": mpbc2RUMLDSControlMode,
       "mpbc2RUMLDS3rdWLPwrSetPtmW": mpbc2RUMLDS3rdWLPwrSetPtmW,
       "mpbc2RUMLDS4thWLPwrSetPtmW": mpbc2RUMLDS4thWLPwrSetPtmW,
       "mpbc2RUMLDSReset": mpbc2RUMLDSReset,
       "mpbc2RUMLDSMonitor": mpbc2RUMLDSMonitor,
       "mpbc2RUMLDSLD1CurmA": mpbc2RUMLDSLD1CurmA,
       "mpbc2RUMLDSLD1TempDegCx10": mpbc2RUMLDSLD1TempDegCx10,
       "mpbc2RUMLDSLD1TECCurmA": mpbc2RUMLDSLD1TECCurmA,
       "mpbc2RUMLDSLD2CurmA": mpbc2RUMLDSLD2CurmA,
       "mpbc2RUMLDSLD2TempDegCx10": mpbc2RUMLDSLD2TempDegCx10,
       "mpbc2RUMLDSLD2TECCurmA": mpbc2RUMLDSLD2TECCurmA,
       "mpbc2RUMLDSCaseTempDegCx10": mpbc2RUMLDSCaseTempDegCx10,
       "mpbc2RUMLDSMon3rdWLOutputPwrmW": mpbc2RUMLDSMon3rdWLOutputPwrmW,
       "mpbc2RUMLDSMon4thWLOutputPwrmW": mpbc2RUMLDSMon4thWLOutputPwrmW,
       "mpbc2RUMLDSMonTotalOutputPwrmW": mpbc2RUMLDSMonTotalOutputPwrmW,
       "mpbc2RUMLDSInputPwrmW": mpbc2RUMLDSInputPwrmW,
       "mpbc2RUMLDSMonLaserState": mpbc2RUMLDSMonLaserState,
       "mpbc2RUMLDSMonLaserMode": mpbc2RUMLDSMonLaserMode,
       "mpbc2RUMLDSMonControlMode": mpbc2RUMLDSMonControlMode,
       "mpbc2RUMLDSDisableInputState": mpbc2RUMLDSDisableInputState,
       "mpbc2RUMLDSUnitState": mpbc2RUMLDSUnitState,
       "mpbc2RUMLDSConfiguration": mpbc2RUMLDSConfiguration,
       "mpbc2RUMLDSLD1CurMinThrmA": mpbc2RUMLDSLD1CurMinThrmA,
       "mpbc2RUMLDSLD1CurMaxThrmA": mpbc2RUMLDSLD1CurMaxThrmA,
       "mpbc2RUMLDSLD2CurMinThrmA": mpbc2RUMLDSLD2CurMinThrmA,
       "mpbc2RUMLDSLD2CurMaxThrmA": mpbc2RUMLDSLD2CurMaxThrmA,
       "mpbc2RUMLDSCaseTempMinSetThrDegCx10": mpbc2RUMLDSCaseTempMinSetThrDegCx10,
       "mpbc2RUMLDSCaseTempMinClearThrDegCx10": mpbc2RUMLDSCaseTempMinClearThrDegCx10,
       "mpbc2RUMLDSCaseTempMaxSetThrDegCx10": mpbc2RUMLDSCaseTempMaxSetThrDegCx10,
       "mpbc2RUMLDSCaseTempMaxClearThrDegCx10": mpbc2RUMLDSCaseTempMaxClearThrDegCx10,
       "mpbc2RUMLDSCaseTempMinAlrmThrDegCx10": mpbc2RUMLDSCaseTempMinAlrmThrDegCx10,
       "mpbc2RUMLDSCaseTempMaxAlrmThrDegCx10": mpbc2RUMLDSCaseTempMaxAlrmThrDegCx10,
       "mpbc2RUMLDS3rdWLOutputPwrMinThrdBx10": mpbc2RUMLDS3rdWLOutputPwrMinThrdBx10,
       "mpbc2RUMLDS3rdWLOutputPwrMaxThrdBx10": mpbc2RUMLDS3rdWLOutputPwrMaxThrdBx10,
       "mpbc2RUMLDS4thWLOutputPwrMinThrdBx10": mpbc2RUMLDS4thWLOutputPwrMinThrdBx10,
       "mpbc2RUMLDS4thWLOutputPwrMaxThrdBx10": mpbc2RUMLDS4thWLOutputPwrMaxThrdBx10,
       "mpbc2RUMLDS3rdWLOutputPwrMinLimdBmx10": mpbc2RUMLDS3rdWLOutputPwrMinLimdBmx10,
       "mpbc2RUMLDS3rdWLOutputPwrMaxLimdBmx10": mpbc2RUMLDS3rdWLOutputPwrMaxLimdBmx10,
       "mpbc2RUMLDS4thWLOutputPwrMinLimdBmx10": mpbc2RUMLDS4thWLOutputPwrMinLimdBmx10,
       "mpbc2RUMLDS4thWLOutputPwrMaxLimdBmx10": mpbc2RUMLDS4thWLOutputPwrMaxLimdBmx10,
       "mpbc2RUMLDSLOSSetThrdBmx100": mpbc2RUMLDSLOSSetThrdBmx100,
       "mpbc2RUMLDSLOSClearThrdBmx100": mpbc2RUMLDSLOSClearThrdBmx100,
       "mpbc2RUPxxH": mpbc2RUPxxH,
       "mpbc2RUPxxHControl": mpbc2RUPxxHControl,
       "mpbc2RUPxxHLaserMode": mpbc2RUPxxHLaserMode,
       "mpbc2RUPxxHControlMode": mpbc2RUPxxHControlMode,
       "mpbc2RUPxxHPwrSetPtmW": mpbc2RUPxxHPwrSetPtmW,
       "mpbc2RUPxxHGainSetPtdBx10": mpbc2RUPxxHGainSetPtdBx10,
       "mpbc2RUPxxHVOASettingdBx10": mpbc2RUPxxHVOASettingdBx10,
       "mpbc2RUPxxHReset": mpbc2RUPxxHReset,
       "mpbc2RUPxxHMonitor": mpbc2RUPxxHMonitor,
       "mpbc2RUPxxHLD1CurmA": mpbc2RUPxxHLD1CurmA,
       "mpbc2RUPxxHLD1TempDegCx10": mpbc2RUPxxHLD1TempDegCx10,
       "mpbc2RUPxxHLD1TECCurmA": mpbc2RUPxxHLD1TECCurmA,
       "mpbc2RUPxxHLD1BackFacetPwrmWx100": mpbc2RUPxxHLD1BackFacetPwrmWx100,
       "mpbc2RUPxxHLD2CurmA": mpbc2RUPxxHLD2CurmA,
       "mpbc2RUPxxHCaseTempDegCx10": mpbc2RUPxxHCaseTempDegCx10,
       "mpbc2RUPxxH148xPumpPwrmW": mpbc2RUPxxH148xPumpPwrmW,
       "mpbc2RUPxxHOutputPwrmW": mpbc2RUPxxHOutputPwrmW,
       "mpbc2RUPxxHGaindBx10": mpbc2RUPxxHGaindBx10,
       "mpbc2RUPxxHInputPwrmWx100": mpbc2RUPxxHInputPwrmWx100,
       "mpbc2RUPxxHBackReflPwrmWx100": mpbc2RUPxxHBackReflPwrmWx100,
       "mpbc2RUPxxHMonLaserState": mpbc2RUPxxHMonLaserState,
       "mpbc2RUPxxHMonLaserMode": mpbc2RUPxxHMonLaserMode,
       "mpbc2RUPxxHMonControlMode": mpbc2RUPxxHMonControlMode,
       "mpbc2RUPxxHDisableInputState": mpbc2RUPxxHDisableInputState,
       "mpbc2RUPxxHUnitState": mpbc2RUPxxHUnitState,
       "mpbc2RUPxxHOSCRxTone": mpbc2RUPxxHOSCRxTone,
       "mpbc2RUPxxHOSCTempdegCx10": mpbc2RUPxxHOSCTempdegCx10,
       "mpbc2RUPxxHOSCTxTone": mpbc2RUPxxHOSCTxTone,
       "mpbc2RUPxxHOSCTxPwrmWx100": mpbc2RUPxxHOSCTxPwrmWx100,
       "mpbc2RUPxxHOSCRx1610Tone": mpbc2RUPxxHOSCRx1610Tone,
       "mpbc2RUPxxHMonVOASettingdBx10": mpbc2RUPxxHMonVOASettingdBx10,
       "mpbc2RUPxxHConfiguration": mpbc2RUPxxHConfiguration,
       "mpbc2RUPxxHLD1CurMinThrmA": mpbc2RUPxxHLD1CurMinThrmA,
       "mpbc2RUPxxHLD2CurMinThrmA": mpbc2RUPxxHLD2CurMinThrmA,
       "mpbc2RUPxxHLD1CurMaxThrmA": mpbc2RUPxxHLD1CurMaxThrmA,
       "mpbc2RUPxxHLD2CurMaxThrmA": mpbc2RUPxxHLD2CurMaxThrmA,
       "mpbc2RUPxxHCaseTempMinSetThrDegCx10": mpbc2RUPxxHCaseTempMinSetThrDegCx10,
       "mpbc2RUPxxHCaseTempMinClearThrDegCx10": mpbc2RUPxxHCaseTempMinClearThrDegCx10,
       "mpbc2RUPxxHCaseTempMaxSetThrDegCx10": mpbc2RUPxxHCaseTempMaxSetThrDegCx10,
       "mpbc2RUPxxHCaseTempMaxClearThrDegCx10": mpbc2RUPxxHCaseTempMaxClearThrDegCx10,
       "mpbc2RUPxxHCaseTempMinAlrmThrDegCx10": mpbc2RUPxxHCaseTempMinAlrmThrDegCx10,
       "mpbc2RUPxxHCaseTempMaxAlrmThrDegCx10": mpbc2RUPxxHCaseTempMaxAlrmThrDegCx10,
       "mpbc2RUPxxHLOSSetThrdBmx100": mpbc2RUPxxHLOSSetThrdBmx100,
       "mpbc2RUPxxHLOSClearThrdBmx100": mpbc2RUPxxHLOSClearThrdBmx100,
       "mpbc2RUPxxHInputMinThrdBmx100": mpbc2RUPxxHInputMinThrdBmx100,
       "mpbc2RUPxxHInputMaxThrdBmx100": mpbc2RUPxxHInputMaxThrdBmx100,
       "mpbc2RUPxxHOutputMinThrdBx10": mpbc2RUPxxHOutputMinThrdBx10,
       "mpbc2RUPxxHOutputMaxThrdBx10": mpbc2RUPxxHOutputMaxThrdBx10,
       "mpbc2RUPxxHOSCMode": mpbc2RUPxxHOSCMode,
       "mpbc2RUPxxHOutputSetptminLimdBmx10": mpbc2RUPxxHOutputSetptminLimdBmx10,
       "mpbc2RUPxxHOutputSetptmaxLimdBmx10": mpbc2RUPxxHOutputSetptmaxLimdBmx10,
       "mpbc2RUPxxHGainSetptminLimdBx10": mpbc2RUPxxHGainSetptminLimdBx10,
       "mpbc2RUPxxHGainSetptmaxLimdBx10": mpbc2RUPxxHGainSetptmaxLimdBx10}
)
