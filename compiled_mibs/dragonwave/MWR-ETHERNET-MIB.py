# SNMP MIB module (MWR-ETHERNET-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\dragonwave\MWR-ETHERNET-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:38:33 2025
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

(mwr,) = mibBuilder.importSymbols(
    "DWI-HARMONY-PRIVATE-MIB",
    "mwr")

(EnableType,
 equipmentAlarmActiveConditionId,
 equipmentOutTrapsCounter,
 equipmentTrapInfo) = mibBuilder.importSymbols(
    "EQUIPMENT-COMMON-MIB",
    "EnableType",
    "equipmentAlarmActiveConditionId",
    "equipmentOutTrapsCounter",
    "equipmentTrapInfo")

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

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
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

mwrModIdentity = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 1000)
)
if mibBuilder.loadTexts:
    mwrModIdentity.setRevisions(
        ("2014-10-06 14:06",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class ClassType(TextualConvention, Integer32):
    status = "current"
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
              8,
              9,
              10,
              11,
              12,
              13)
        )
    )
    namedValues = NamedValues(
        *(("c1", 1),
          ("c2", 2),
          ("c3", 3),
          ("c4", 4),
          ("c5", 5),
          ("c6", 6),
          ("c7", 7),
          ("c8", 8),
          ("c9", 9),
          ("c10", 10),
          ("c11", 11),
          ("c12", 12),
          ("c13", 13))
    )



class FlowType(TextualConvention, Integer32):
    status = "current"
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
              8,
              9,
              10,
              11,
              12,
              13)
        )
    )
    namedValues = NamedValues(
        *(("flow1", 1),
          ("flow2", 2),
          ("flow3", 3),
          ("flow4", 4),
          ("flow5", 5),
          ("flow6", 6),
          ("flow7", 7),
          ("flow8", 8),
          ("flow9", 9),
          ("flow10", 10),
          ("flow11", 11),
          ("flow12", 12),
          ("flow13", 13))
    )



class PMIntervalType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("quarter", 1),
          ("day", 2))
    )



class PortType(TextualConvention, Integer32):
    status = "current"
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
        *(("gi01", 1),
          ("gi02", 2),
          ("gi03", 3),
          ("gi04", 4))
    )



class QueueType(TextualConvention, Integer32):
    status = "current"
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
        *(("q1", 1),
          ("q2", 2),
          ("q3", 3),
          ("q4", 4),
          ("q5", 5),
          ("q6", 6),
          ("q7", 7),
          ("q8", 8))
    )



class RadioInstanceType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("radio1", 1)
    )



# MIB Managed Objects in the order of their OIDs

_MwrPlatformObjId_ObjectIdentity = ObjectIdentity
mwrPlatformObjId = _MwrPlatformObjId_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 1)
)
_MwrEbandObjId_ObjectIdentity = ObjectIdentity
mwrEbandObjId = _MwrEbandObjId_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 1, 1)
)
_MwrEnhancedObjId_ObjectIdentity = ObjectIdentity
mwrEnhancedObjId = _MwrEnhancedObjId_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 1, 2)
)
_MwrSystem_ObjectIdentity = ObjectIdentity
mwrSystem = _MwrSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 2)
)
_MwrSystemConfigurations_ObjectIdentity = ObjectIdentity
mwrSystemConfigurations = _MwrSystemConfigurations_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 2, 1)
)


class _MwrSystemType_Type(Integer32):
    """Custom type mwrSystemType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("onePlusZero1cr", 1),
          ("onePlusZero2cr", 2),
          ("onePlusZero2crXpic", 3))
    )


_MwrSystemType_Type.__name__ = "Integer32"
_MwrSystemType_Object = MibScalar
mwrSystemType = _MwrSystemType_Object(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 2, 1, 1),
    _MwrSystemType_Type()
)
mwrSystemType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mwrSystemType.setStatus("current")


class _MwrPacketSwitchMode_Type(Integer32):
    """Custom type mwrPacketSwitchMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("bridge", 1),
          ("port-isolation", 2))
    )


_MwrPacketSwitchMode_Type.__name__ = "Integer32"
_MwrPacketSwitchMode_Object = MibScalar
mwrPacketSwitchMode = _MwrPacketSwitchMode_Object(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 2, 1, 2),
    _MwrPacketSwitchMode_Type()
)
mwrPacketSwitchMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mwrPacketSwitchMode.setStatus("current")
_MwrSysSpeed_ObjectIdentity = ObjectIdentity
mwrSysSpeed = _MwrSysSpeed_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 2, 1, 3)
)


class _MwrSystemCurrentSpeed_Type(Integer32):
    """Custom type mwrSystemCurrentSpeed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_MwrSystemCurrentSpeed_Type.__name__ = "Integer32"
_MwrSystemCurrentSpeed_Object = MibScalar
mwrSystemCurrentSpeed = _MwrSystemCurrentSpeed_Object(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 2, 1, 3, 1),
    _MwrSystemCurrentSpeed_Type()
)
mwrSystemCurrentSpeed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mwrSystemCurrentSpeed.setStatus("current")
_MwrSystemStatus_ObjectIdentity = ObjectIdentity
mwrSystemStatus = _MwrSystemStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 2, 2)
)


class _MwrSystemOperStatus_Type(Integer32):
    """Custom type mwrSystemOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("up", 1),
          ("down", 2))
    )


_MwrSystemOperStatus_Type.__name__ = "Integer32"
_MwrSystemOperStatus_Object = MibScalar
mwrSystemOperStatus = _MwrSystemOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 2, 2, 1),
    _MwrSystemOperStatus_Type()
)
mwrSystemOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwrSystemOperStatus.setStatus("current")


class _MwrSystemFaultSeverity_Type(Integer32):
    """Custom type mwrSystemFaultSeverity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("noAlarm", 1),
          ("test", 2),
          ("warning", 3),
          ("minor", 4),
          ("major", 5),
          ("critical", 6))
    )


_MwrSystemFaultSeverity_Type.__name__ = "Integer32"
_MwrSystemFaultSeverity_Object = MibScalar
mwrSystemFaultSeverity = _MwrSystemFaultSeverity_Object(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 2, 2, 2),
    _MwrSystemFaultSeverity_Type()
)
mwrSystemFaultSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwrSystemFaultSeverity.setStatus("current")
_MwrSystemTemperature_Type = Integer32
_MwrSystemTemperature_Object = MibScalar
mwrSystemTemperature = _MwrSystemTemperature_Object(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 2, 2, 3),
    _MwrSystemTemperature_Type()
)
mwrSystemTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwrSystemTemperature.setStatus("current")


class _MwrPlatformType_Type(Integer32):
    """Custom type mwrPlatformType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("eband", 1),
          ("enhanced", 2),
          ("enhanced-mc", 3))
    )


_MwrPlatformType_Type.__name__ = "Integer32"
_MwrPlatformType_Object = MibScalar
mwrPlatformType = _MwrPlatformType_Object(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 2, 2, 4),
    _MwrPlatformType_Type()
)
mwrPlatformType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwrPlatformType.setStatus("current")


class _MwrPacketSwitchModeStatus_Type(Integer32):
    """Custom type mwrPacketSwitchModeStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("bridge", 1),
          ("port-isolation", 2))
    )


_MwrPacketSwitchModeStatus_Type.__name__ = "Integer32"
_MwrPacketSwitchModeStatus_Object = MibScalar
mwrPacketSwitchModeStatus = _MwrPacketSwitchModeStatus_Object(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 2, 2, 5),
    _MwrPacketSwitchModeStatus_Type()
)
mwrPacketSwitchModeStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwrPacketSwitchModeStatus.setStatus("current")


class _MwrSystemTypeStatus_Type(Integer32):
    """Custom type mwrSystemTypeStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("onePlusZero1cr", 1),
          ("onePlusZero2cr", 2),
          ("onePlusZero2crXpic", 3))
    )


_MwrSystemTypeStatus_Type.__name__ = "Integer32"
_MwrSystemTypeStatus_Object = MibScalar
mwrSystemTypeStatus = _MwrSystemTypeStatus_Object(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 2, 2, 6),
    _MwrSystemTypeStatus_Type()
)
mwrSystemTypeStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwrSystemTypeStatus.setStatus("current")
_MwrSystemCommands_ObjectIdentity = ObjectIdentity
mwrSystemCommands = _MwrSystemCommands_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 2, 3)
)


class _MwrResetSystem_Type(Integer32):
    """Custom type mwrResetSystem based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("reset", 1)
    )


_MwrResetSystem_Type.__name__ = "Integer32"
_MwrResetSystem_Object = MibScalar
mwrResetSystem = _MwrResetSystem_Object(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 2, 3, 1),
    _MwrResetSystem_Type()
)
mwrResetSystem.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mwrResetSystem.setStatus("current")


class _MwrSaveConfig_Type(Integer32):
    """Custom type mwrSaveConfig based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("save", 1)
    )


_MwrSaveConfig_Type.__name__ = "Integer32"
_MwrSaveConfig_Object = MibScalar
mwrSaveConfig = _MwrSaveConfig_Object(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 2, 3, 2),
    _MwrSaveConfig_Type()
)
mwrSaveConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mwrSaveConfig.setStatus("current")


class _MwrDeleteConfig_Type(Integer32):
    """Custom type mwrDeleteConfig based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("startup", 1),
          ("switch", 2))
    )


_MwrDeleteConfig_Type.__name__ = "Integer32"
_MwrDeleteConfig_Object = MibScalar
mwrDeleteConfig = _MwrDeleteConfig_Object(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 2, 3, 3),
    _MwrDeleteConfig_Type()
)
mwrDeleteConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mwrDeleteConfig.setStatus("current")
_MwrSystemInventory_ObjectIdentity = ObjectIdentity
mwrSystemInventory = _MwrSystemInventory_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 2, 4)
)
_MwrHwInventory_ObjectIdentity = ObjectIdentity
mwrHwInventory = _MwrHwInventory_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 2, 4, 1)
)
_MwrMacAddress_Type = DisplayString
_MwrMacAddress_Object = MibScalar
mwrMacAddress = _MwrMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 2, 4, 1, 1),
    _MwrMacAddress_Type()
)
mwrMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwrMacAddress.setStatus("current")
_MwrTargetCfgFilePartNumber_Type = DisplayString
_MwrTargetCfgFilePartNumber_Object = MibScalar
mwrTargetCfgFilePartNumber = _MwrTargetCfgFilePartNumber_Object(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 2, 4, 1, 2),
    _MwrTargetCfgFilePartNumber_Type()
)
mwrTargetCfgFilePartNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwrTargetCfgFilePartNumber.setStatus("current")
_MwrUnitSerialNo_Type = DisplayString
_MwrUnitSerialNo_Object = MibScalar
mwrUnitSerialNo = _MwrUnitSerialNo_Object(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 2, 4, 1, 3),
    _MwrUnitSerialNo_Type()
)
mwrUnitSerialNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwrUnitSerialNo.setStatus("current")
_MwrUnitAssemblyNo_Type = DisplayString
_MwrUnitAssemblyNo_Object = MibScalar
mwrUnitAssemblyNo = _MwrUnitAssemblyNo_Object(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 2, 4, 1, 4),
    _MwrUnitAssemblyNo_Type()
)
mwrUnitAssemblyNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwrUnitAssemblyNo.setStatus("current")
_MwrBasebandSerialNo_Type = DisplayString
_MwrBasebandSerialNo_Object = MibScalar
mwrBasebandSerialNo = _MwrBasebandSerialNo_Object(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 2, 4, 1, 5),
    _MwrBasebandSerialNo_Type()
)
mwrBasebandSerialNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwrBasebandSerialNo.setStatus("current")
_MwrBasebandAssemblyNo_Type = DisplayString
_MwrBasebandAssemblyNo_Object = MibScalar
mwrBasebandAssemblyNo = _MwrBasebandAssemblyNo_Object(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 2, 4, 1, 6),
    _MwrBasebandAssemblyNo_Type()
)
mwrBasebandAssemblyNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwrBasebandAssemblyNo.setStatus("current")
_MwrPsuSerialNo_Type = DisplayString
_MwrPsuSerialNo_Object = MibScalar
mwrPsuSerialNo = _MwrPsuSerialNo_Object(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 2, 4, 1, 7),
    _MwrPsuSerialNo_Type()
)
mwrPsuSerialNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwrPsuSerialNo.setStatus("current")
_MwrPsuAssemblyNo_Type = DisplayString
_MwrPsuAssemblyNo_Object = MibScalar
mwrPsuAssemblyNo = _MwrPsuAssemblyNo_Object(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 2, 4, 1, 8),
    _MwrPsuAssemblyNo_Type()
)
mwrPsuAssemblyNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwrPsuAssemblyNo.setStatus("current")
_MwrRfSerialNo_Type = DisplayString
_MwrRfSerialNo_Object = MibScalar
mwrRfSerialNo = _MwrRfSerialNo_Object(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 2, 4, 1, 9),
    _MwrRfSerialNo_Type()
)
mwrRfSerialNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwrRfSerialNo.setStatus("current")
_MwrRfAssemblyNo_Type = DisplayString
_MwrRfAssemblyNo_Object = MibScalar
mwrRfAssemblyNo = _MwrRfAssemblyNo_Object(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 2, 4, 1, 10),
    _MwrRfAssemblyNo_Type()
)
mwrRfAssemblyNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwrRfAssemblyNo.setStatus("current")
_MwrRfRevisionNo_Type = DisplayString
_MwrRfRevisionNo_Object = MibScalar
mwrRfRevisionNo = _MwrRfRevisionNo_Object(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 2, 4, 1, 11),
    _MwrRfRevisionNo_Type()
)
mwrRfRevisionNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwrRfRevisionNo.setStatus("current")
_MwrDiplexerSerialNo_Type = DisplayString
_MwrDiplexerSerialNo_Object = MibScalar
mwrDiplexerSerialNo = _MwrDiplexerSerialNo_Object(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 2, 4, 1, 12),
    _MwrDiplexerSerialNo_Type()
)
mwrDiplexerSerialNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwrDiplexerSerialNo.setStatus("current")
_MwrDiplexerAssemblyNo_Type = DisplayString
_MwrDiplexerAssemblyNo_Object = MibScalar
mwrDiplexerAssemblyNo = _MwrDiplexerAssemblyNo_Object(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 2, 4, 1, 13),
    _MwrDiplexerAssemblyNo_Type()
)
mwrDiplexerAssemblyNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwrDiplexerAssemblyNo.setStatus("current")
_MwrSystemCleiNo_Type = DisplayString
_MwrSystemCleiNo_Object = MibScalar
mwrSystemCleiNo = _MwrSystemCleiNo_Object(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 2, 4, 1, 14),
    _MwrSystemCleiNo_Type()
)
mwrSystemCleiNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwrSystemCleiNo.setStatus("current")
_MwrSwInventory_ObjectIdentity = ObjectIdentity
mwrSwInventory = _MwrSwInventory_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 2, 4, 2)
)
_MwrSwInventoryTable_Object = MibTable
mwrSwInventoryTable = _MwrSwInventoryTable_Object(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 2, 4, 2, 1)
)
if mibBuilder.loadTexts:
    mwrSwInventoryTable.setStatus("current")
_MwrSwInventoryEntry_Object = MibTableRow
mwrSwInventoryEntry = _MwrSwInventoryEntry_Object(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 2, 4, 2, 1, 1)
)
mwrSwInventoryEntry.setIndexNames(
    (0, "MWR-ETHERNET-MIB", "mwrSwInvBank"),
)
if mibBuilder.loadTexts:
    mwrSwInventoryEntry.setStatus("current")


class _MwrSwInvBank_Type(Integer32):
    """Custom type mwrSwInvBank based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("bankA", 1),
          ("bankB", 2))
    )


_MwrSwInvBank_Type.__name__ = "Integer32"
_MwrSwInvBank_Object = MibTableColumn
mwrSwInvBank = _MwrSwInvBank_Object(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 2, 4, 2, 1, 1, 1),
    _MwrSwInvBank_Type()
)
mwrSwInvBank.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mwrSwInvBank.setStatus("current")


class _MwrSwInvStatus_Type(Integer32):
    """Custom type mwrSwInvStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("backup", 2))
    )


_MwrSwInvStatus_Type.__name__ = "Integer32"
_MwrSwInvStatus_Object = MibTableColumn
mwrSwInvStatus = _MwrSwInvStatus_Object(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 2, 4, 2, 1, 1, 2),
    _MwrSwInvStatus_Type()
)
mwrSwInvStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwrSwInvStatus.setStatus("current")
_MwrSwInvOmniRelease_Type = DisplayString
_MwrSwInvOmniRelease_Object = MibTableColumn
mwrSwInvOmniRelease = _MwrSwInvOmniRelease_Object(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 2, 4, 2, 1, 1, 3),
    _MwrSwInvOmniRelease_Type()
)
mwrSwInvOmniRelease.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwrSwInvOmniRelease.setStatus("current")
_MwrSwInvTargetConfFileVersion_Type = DisplayString
_MwrSwInvTargetConfFileVersion_Object = MibTableColumn
mwrSwInvTargetConfFileVersion = _MwrSwInvTargetConfFileVersion_Object(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 2, 4, 2, 1, 1, 4),
    _MwrSwInvTargetConfFileVersion_Type()
)
mwrSwInvTargetConfFileVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwrSwInvTargetConfFileVersion.setStatus("current")
_MwrSwInvMibVersion_Type = DisplayString
_MwrSwInvMibVersion_Object = MibTableColumn
mwrSwInvMibVersion = _MwrSwInvMibVersion_Object(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 2, 4, 2, 1, 1, 5),
    _MwrSwInvMibVersion_Type()
)
mwrSwInvMibVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwrSwInvMibVersion.setStatus("current")
_MwrSwInvSecurityVersion_Type = DisplayString
_MwrSwInvSecurityVersion_Object = MibTableColumn
mwrSwInvSecurityVersion = _MwrSwInvSecurityVersion_Object(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 2, 4, 2, 1, 1, 6),
    _MwrSwInvSecurityVersion_Type()
)
mwrSwInvSecurityVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwrSwInvSecurityVersion.setStatus("current")
_MwrSystemNotifications_ObjectIdentity = ObjectIdentity
mwrSystemNotifications = _MwrSystemNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 2, 5)
)
_MwrSoftware_ObjectIdentity = ObjectIdentity
mwrSoftware = _MwrSoftware_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 3)
)
_MwrSoftwareConfigurations_ObjectIdentity = ObjectIdentity
mwrSoftwareConfigurations = _MwrSoftwareConfigurations_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 3, 1)
)
_MwrSoftwareStatus_ObjectIdentity = ObjectIdentity
mwrSoftwareStatus = _MwrSoftwareStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 3, 2)
)


class _MwrSwBackupBankStatus_Type(Integer32):
    """Custom type mwrSwBackupBankStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("notValid", 1),
          ("valid", 2),
          ("upgrading", 3))
    )


_MwrSwBackupBankStatus_Type.__name__ = "Integer32"
_MwrSwBackupBankStatus_Object = MibScalar
mwrSwBackupBankStatus = _MwrSwBackupBankStatus_Object(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 3, 2, 1),
    _MwrSwBackupBankStatus_Type()
)
mwrSwBackupBankStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwrSwBackupBankStatus.setStatus("current")
_MwrSoftwareCommands_ObjectIdentity = ObjectIdentity
mwrSoftwareCommands = _MwrSoftwareCommands_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 3, 3)
)


class _MwrSwCommit_Type(Integer32):
    """Custom type mwrSwCommit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("commit", 1)
    )


_MwrSwCommit_Type.__name__ = "Integer32"
_MwrSwCommit_Object = MibScalar
mwrSwCommit = _MwrSwCommit_Object(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 3, 3, 1),
    _MwrSwCommit_Type()
)
mwrSwCommit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mwrSwCommit.setStatus("current")


class _MwrSwSwitchBanks_Type(Integer32):
    """Custom type mwrSwSwitchBanks based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("bankA", 1),
          ("bankB", 2))
    )


_MwrSwSwitchBanks_Type.__name__ = "Integer32"
_MwrSwSwitchBanks_Object = MibScalar
mwrSwSwitchBanks = _MwrSwSwitchBanks_Object(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 3, 3, 2),
    _MwrSwSwitchBanks_Type()
)
mwrSwSwitchBanks.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mwrSwSwitchBanks.setStatus("current")
_MwrSoftwareNotifications_ObjectIdentity = ObjectIdentity
mwrSoftwareNotifications = _MwrSoftwareNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 3, 4)
)
_MwrLicensing_ObjectIdentity = ObjectIdentity
mwrLicensing = _MwrLicensing_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 4)
)
_MwrLicensingConfigurations_ObjectIdentity = ObjectIdentity
mwrLicensingConfigurations = _MwrLicensingConfigurations_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 4, 1)
)


class _MwrLicenseUpgradeKey_Type(OctetString):
    """Custom type mwrLicenseUpgradeKey based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(33, 33),
    )
    fixed_length = 33


_MwrLicenseUpgradeKey_Type.__name__ = "OctetString"
_MwrLicenseUpgradeKey_Object = MibScalar
mwrLicenseUpgradeKey = _MwrLicenseUpgradeKey_Object(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 4, 1, 1),
    _MwrLicenseUpgradeKey_Type()
)
mwrLicenseUpgradeKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mwrLicenseUpgradeKey.setStatus("current")
_MwrLicensingStatus_ObjectIdentity = ObjectIdentity
mwrLicensingStatus = _MwrLicensingStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 4, 2)
)
_MwrLicenseCount_Type = Integer32
_MwrLicenseCount_Object = MibScalar
mwrLicenseCount = _MwrLicenseCount_Object(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 4, 2, 1),
    _MwrLicenseCount_Type()
)
mwrLicenseCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwrLicenseCount.setStatus("current")
_MwrLicensedSpeed_Type = Integer32
_MwrLicensedSpeed_Object = MibScalar
mwrLicensedSpeed = _MwrLicensedSpeed_Object(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 4, 2, 2),
    _MwrLicensedSpeed_Type()
)
mwrLicensedSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwrLicensedSpeed.setStatus("current")
_MwrLicenseFeaturesTable_Object = MibTable
mwrLicenseFeaturesTable = _MwrLicenseFeaturesTable_Object(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 4, 2, 3)
)
if mibBuilder.loadTexts:
    mwrLicenseFeaturesTable.setStatus("current")
_MwrLicenseFeaturesEntry_Object = MibTableRow
mwrLicenseFeaturesEntry = _MwrLicenseFeaturesEntry_Object(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 4, 2, 3, 1)
)
mwrLicenseFeaturesEntry.setIndexNames(
    (0, "MWR-ETHERNET-MIB", "mwrLicenseFeatureIndex"),
)
if mibBuilder.loadTexts:
    mwrLicenseFeaturesEntry.setStatus("current")
_MwrLicenseFeatureIndex_Type = Integer32
_MwrLicenseFeatureIndex_Object = MibTableColumn
mwrLicenseFeatureIndex = _MwrLicenseFeatureIndex_Object(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 4, 2, 3, 1, 1),
    _MwrLicenseFeatureIndex_Type()
)
mwrLicenseFeatureIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mwrLicenseFeatureIndex.setStatus("current")
_MwrLicenseFeatureId_Type = Integer32
_MwrLicenseFeatureId_Object = MibTableColumn
mwrLicenseFeatureId = _MwrLicenseFeatureId_Object(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 4, 2, 3, 1, 2),
    _MwrLicenseFeatureId_Type()
)
mwrLicenseFeatureId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwrLicenseFeatureId.setStatus("current")
_MwrLicenseFeature_Type = DisplayString
_MwrLicenseFeature_Object = MibTableColumn
mwrLicenseFeature = _MwrLicenseFeature_Object(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 4, 2, 3, 1, 3),
    _MwrLicenseFeature_Type()
)
mwrLicenseFeature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwrLicenseFeature.setStatus("current")


class _MwrLicenseFeatureStatus_Type(Integer32):
    """Custom type mwrLicenseFeatureStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("unlicensed", 1),
          ("licensed", 2))
    )


_MwrLicenseFeatureStatus_Type.__name__ = "Integer32"
_MwrLicenseFeatureStatus_Object = MibTableColumn
mwrLicenseFeatureStatus = _MwrLicenseFeatureStatus_Object(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 4, 2, 3, 1, 4),
    _MwrLicenseFeatureStatus_Type()
)
mwrLicenseFeatureStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwrLicenseFeatureStatus.setStatus("current")
_MwrSyncE_ObjectIdentity = ObjectIdentity
mwrSyncE = _MwrSyncE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 5)
)
_MwrSyncEConfigurations_ObjectIdentity = ObjectIdentity
mwrSyncEConfigurations = _MwrSyncEConfigurations_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 5, 1)
)


class _MwrSyncEState_Type(Integer32):
    """Custom type mwrSyncEState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("manual", 2),
          ("auto", 3))
    )


_MwrSyncEState_Type.__name__ = "Integer32"
_MwrSyncEState_Object = MibScalar
mwrSyncEState = _MwrSyncEState_Object(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 5, 1, 1),
    _MwrSyncEState_Type()
)
mwrSyncEState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mwrSyncEState.setStatus("current")


class _MwrSyncEPrimarySource_Type(Integer32):
    """Custom type mwrSyncEPrimarySource based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("gi01", 1),
          ("gi02", 2),
          ("gi03", 3),
          ("gi04", 4),
          ("radio", 5),
          ("free-run", 6))
    )


_MwrSyncEPrimarySource_Type.__name__ = "Integer32"
_MwrSyncEPrimarySource_Object = MibScalar
mwrSyncEPrimarySource = _MwrSyncEPrimarySource_Object(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 5, 1, 2),
    _MwrSyncEPrimarySource_Type()
)
mwrSyncEPrimarySource.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mwrSyncEPrimarySource.setStatus("current")


class _MwrSyncESecondarySource_Type(Integer32):
    """Custom type mwrSyncESecondarySource based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("gi01", 1),
          ("gi02", 2),
          ("gi03", 3),
          ("gi04", 4),
          ("radio", 5),
          ("free-run", 6))
    )


_MwrSyncESecondarySource_Type.__name__ = "Integer32"
_MwrSyncESecondarySource_Object = MibScalar
mwrSyncESecondarySource = _MwrSyncESecondarySource_Object(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 5, 1, 3),
    _MwrSyncESecondarySource_Type()
)
mwrSyncESecondarySource.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mwrSyncESecondarySource.setStatus("current")
_MwrSyncEMemberPorts_Type = DisplayString
_MwrSyncEMemberPorts_Object = MibScalar
mwrSyncEMemberPorts = _MwrSyncEMemberPorts_Object(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 5, 1, 4),
    _MwrSyncEMemberPorts_Type()
)
mwrSyncEMemberPorts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mwrSyncEMemberPorts.setStatus("current")
_MwrSyncEForcedHoldover_Type = DisplayString
_MwrSyncEForcedHoldover_Object = MibScalar
mwrSyncEForcedHoldover = _MwrSyncEForcedHoldover_Object(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 5, 1, 5),
    _MwrSyncEForcedHoldover_Type()
)
mwrSyncEForcedHoldover.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mwrSyncEForcedHoldover.setStatus("current")
_MwrSyncERevertive_Type = DisplayString
_MwrSyncERevertive_Object = MibScalar
mwrSyncERevertive = _MwrSyncERevertive_Object(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 5, 1, 6),
    _MwrSyncERevertive_Type()
)
mwrSyncERevertive.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mwrSyncERevertive.setStatus("current")


class _MwrSyncEWanderFilter_Type(Integer32):
    """Custom type mwrSyncEWanderFilter based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("option1", 1),
          ("option2", 2))
    )


_MwrSyncEWanderFilter_Type.__name__ = "Integer32"
_MwrSyncEWanderFilter_Object = MibScalar
mwrSyncEWanderFilter = _MwrSyncEWanderFilter_Object(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 5, 1, 7),
    _MwrSyncEWanderFilter_Type()
)
mwrSyncEWanderFilter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mwrSyncEWanderFilter.setStatus("current")
_MwrSyncEStatus_ObjectIdentity = ObjectIdentity
mwrSyncEStatus = _MwrSyncEStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 5, 2)
)


class _MwrSyncEClockSource_Type(Integer32):
    """Custom type mwrSyncEClockSource based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("gi01", 1),
          ("gi02", 2),
          ("gi03", 3),
          ("gi04", 4),
          ("radio", 5),
          ("free-run", 6))
    )


_MwrSyncEClockSource_Type.__name__ = "Integer32"
_MwrSyncEClockSource_Object = MibScalar
mwrSyncEClockSource = _MwrSyncEClockSource_Object(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 5, 2, 1),
    _MwrSyncEClockSource_Type()
)
mwrSyncEClockSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwrSyncEClockSource.setStatus("current")
_MwrSyncEAcquisitionStatus_Type = DisplayString
_MwrSyncEAcquisitionStatus_Object = MibScalar
mwrSyncEAcquisitionStatus = _MwrSyncEAcquisitionStatus_Object(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 5, 2, 2),
    _MwrSyncEAcquisitionStatus_Type()
)
mwrSyncEAcquisitionStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwrSyncEAcquisitionStatus.setStatus("current")
_MwrSyncENotifications_ObjectIdentity = ObjectIdentity
mwrSyncENotifications = _MwrSyncENotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 5, 3)
)
_MwrTiming_ObjectIdentity = ObjectIdentity
mwrTiming = _MwrTiming_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 6)
)
_MwrTimingConfigurations_ObjectIdentity = ObjectIdentity
mwrTimingConfigurations = _MwrTimingConfigurations_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 6, 1)
)
_MwrDateTime_Type = DateAndTime
_MwrDateTime_Object = MibScalar
mwrDateTime = _MwrDateTime_Object(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 6, 1, 1),
    _MwrDateTime_Type()
)
mwrDateTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mwrDateTime.setStatus("current")


class _MwrSntpEnable_Type(EnableType):
    """Custom type mwrSntpEnable based on EnableType"""
    defaultValue = 1


_MwrSntpEnable_Type.__name__ = "EnableType"
_MwrSntpEnable_Object = MibScalar
mwrSntpEnable = _MwrSntpEnable_Object(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 6, 1, 2),
    _MwrSntpEnable_Type()
)
mwrSntpEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mwrSntpEnable.setStatus("current")


class _MwrSntpOffset_Type(Integer32):
    """Custom type mwrSntpOffset based on Integer32"""
    defaultValue = -40

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-140, 140),
    )


_MwrSntpOffset_Type.__name__ = "Integer32"
_MwrSntpOffset_Object = MibScalar
mwrSntpOffset = _MwrSntpOffset_Object(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 6, 1, 3),
    _MwrSntpOffset_Type()
)
mwrSntpOffset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mwrSntpOffset.setStatus("current")
_MwrSntpServerTable_Object = MibTable
mwrSntpServerTable = _MwrSntpServerTable_Object(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 6, 1, 4)
)
if mibBuilder.loadTexts:
    mwrSntpServerTable.setStatus("current")
_MwrSntpServerEntry_Object = MibTableRow
mwrSntpServerEntry = _MwrSntpServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 6, 1, 4, 1)
)
mwrSntpServerEntry.setIndexNames(
    (0, "MWR-ETHERNET-MIB", "mwrSntpServerIndex"),
)
if mibBuilder.loadTexts:
    mwrSntpServerEntry.setStatus("current")


class _MwrSntpServerIndex_Type(Integer32):
    """Custom type mwrSntpServerIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_MwrSntpServerIndex_Type.__name__ = "Integer32"
_MwrSntpServerIndex_Object = MibTableColumn
mwrSntpServerIndex = _MwrSntpServerIndex_Object(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 6, 1, 4, 1, 1),
    _MwrSntpServerIndex_Type()
)
mwrSntpServerIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mwrSntpServerIndex.setStatus("current")
_MwrSntpServerDomain_Type = InetAddressType
_MwrSntpServerDomain_Object = MibTableColumn
mwrSntpServerDomain = _MwrSntpServerDomain_Object(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 6, 1, 4, 1, 2),
    _MwrSntpServerDomain_Type()
)
mwrSntpServerDomain.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mwrSntpServerDomain.setStatus("current")
_MwrSntpServerAddress_Type = InetAddress
_MwrSntpServerAddress_Object = MibTableColumn
mwrSntpServerAddress = _MwrSntpServerAddress_Object(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 6, 1, 4, 1, 3),
    _MwrSntpServerAddress_Type()
)
mwrSntpServerAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mwrSntpServerAddress.setStatus("current")


class _MwrSntpServerStatus_Type(Integer32):
    """Custom type mwrSntpServerStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("good", 1),
          ("failed", 2))
    )


_MwrSntpServerStatus_Type.__name__ = "Integer32"
_MwrSntpServerStatus_Object = MibTableColumn
mwrSntpServerStatus = _MwrSntpServerStatus_Object(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 6, 1, 4, 1, 4),
    _MwrSntpServerStatus_Type()
)
mwrSntpServerStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwrSntpServerStatus.setStatus("current")
_MwrSntpServerStratum_Type = Integer32
_MwrSntpServerStratum_Object = MibTableColumn
mwrSntpServerStratum = _MwrSntpServerStratum_Object(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 6, 1, 4, 1, 5),
    _MwrSntpServerStratum_Type()
)
mwrSntpServerStratum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwrSntpServerStratum.setStatus("current")
_MwrTimingStatus_ObjectIdentity = ObjectIdentity
mwrTimingStatus = _MwrTimingStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 6, 2)
)
_MwrTimingLastDateTimeChanged_Type = DateAndTime
_MwrTimingLastDateTimeChanged_Object = MibScalar
mwrTimingLastDateTimeChanged = _MwrTimingLastDateTimeChanged_Object(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 6, 2, 1),
    _MwrTimingLastDateTimeChanged_Type()
)
mwrTimingLastDateTimeChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwrTimingLastDateTimeChanged.setStatus("current")
_MwrTimingLastTimeAdjustment_Type = Integer32
_MwrTimingLastTimeAdjustment_Object = MibScalar
mwrTimingLastTimeAdjustment = _MwrTimingLastTimeAdjustment_Object(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 6, 2, 2),
    _MwrTimingLastTimeAdjustment_Type()
)
mwrTimingLastTimeAdjustment.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwrTimingLastTimeAdjustment.setStatus("current")
_MwrTimingCummulativeTimeChange_Type = Integer32
_MwrTimingCummulativeTimeChange_Object = MibScalar
mwrTimingCummulativeTimeChange = _MwrTimingCummulativeTimeChange_Object(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 6, 2, 3),
    _MwrTimingCummulativeTimeChange_Type()
)
mwrTimingCummulativeTimeChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwrTimingCummulativeTimeChange.setStatus("current")
_MwrTimingCommands_ObjectIdentity = ObjectIdentity
mwrTimingCommands = _MwrTimingCommands_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 6, 3)
)


class _MwrSntpRestoreDefault_Type(Integer32):
    """Custom type mwrSntpRestoreDefault based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("restore", 1)
    )


_MwrSntpRestoreDefault_Type.__name__ = "Integer32"
_MwrSntpRestoreDefault_Object = MibScalar
mwrSntpRestoreDefault = _MwrSntpRestoreDefault_Object(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 6, 3, 1),
    _MwrSntpRestoreDefault_Type()
)
mwrSntpRestoreDefault.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mwrSntpRestoreDefault.setStatus("current")
_MwrTimingNotifications_ObjectIdentity = ObjectIdentity
mwrTimingNotifications = _MwrTimingNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 6, 4)
)
_MwrAAA_ObjectIdentity = ObjectIdentity
mwrAAA = _MwrAAA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 7)
)
_MwrAAAConfigurations_ObjectIdentity = ObjectIdentity
mwrAAAConfigurations = _MwrAAAConfigurations_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 7, 1)
)


class _MwrAAAUserAuthentication_Type(Integer32):
    """Custom type mwrAAAUserAuthentication based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("internal", 1),
          ("radius", 2))
    )


_MwrAAAUserAuthentication_Type.__name__ = "Integer32"
_MwrAAAUserAuthentication_Object = MibScalar
mwrAAAUserAuthentication = _MwrAAAUserAuthentication_Object(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 7, 1, 1),
    _MwrAAAUserAuthentication_Type()
)
mwrAAAUserAuthentication.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mwrAAAUserAuthentication.setStatus("current")
_MwrRadiusConfigurations_ObjectIdentity = ObjectIdentity
mwrRadiusConfigurations = _MwrRadiusConfigurations_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 7, 1, 2)
)


class _MwrRadiusAdminUserStrict_Type(Integer32):
    """Custom type mwrRadiusAdminUserStrict based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_MwrRadiusAdminUserStrict_Type.__name__ = "Integer32"
_MwrRadiusAdminUserStrict_Object = MibScalar
mwrRadiusAdminUserStrict = _MwrRadiusAdminUserStrict_Object(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 7, 1, 2, 1),
    _MwrRadiusAdminUserStrict_Type()
)
mwrRadiusAdminUserStrict.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mwrRadiusAdminUserStrict.setStatus("current")
_MwrRadiusServerTimeOut_Type = Integer32
_MwrRadiusServerTimeOut_Object = MibScalar
mwrRadiusServerTimeOut = _MwrRadiusServerTimeOut_Object(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 7, 1, 2, 2),
    _MwrRadiusServerTimeOut_Type()
)
mwrRadiusServerTimeOut.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mwrRadiusServerTimeOut.setStatus("current")
_MwrRadiusServerDeadTime_Type = Integer32
_MwrRadiusServerDeadTime_Object = MibScalar
mwrRadiusServerDeadTime = _MwrRadiusServerDeadTime_Object(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 7, 1, 2, 3),
    _MwrRadiusServerDeadTime_Type()
)
mwrRadiusServerDeadTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mwrRadiusServerDeadTime.setStatus("current")
_MwrRadiusServerReTransmit_Type = Integer32
_MwrRadiusServerReTransmit_Object = MibScalar
mwrRadiusServerReTransmit = _MwrRadiusServerReTransmit_Object(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 7, 1, 2, 4),
    _MwrRadiusServerReTransmit_Type()
)
mwrRadiusServerReTransmit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mwrRadiusServerReTransmit.setStatus("current")
_MwrRadiusServerTable_Object = MibTable
mwrRadiusServerTable = _MwrRadiusServerTable_Object(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 7, 1, 2, 5)
)
if mibBuilder.loadTexts:
    mwrRadiusServerTable.setStatus("current")
_MwrRadiusServerEntry_Object = MibTableRow
mwrRadiusServerEntry = _MwrRadiusServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 7, 1, 2, 5, 1)
)
mwrRadiusServerEntry.setIndexNames(
    (0, "MWR-ETHERNET-MIB", "mwrRadiusServerIndex"),
)
if mibBuilder.loadTexts:
    mwrRadiusServerEntry.setStatus("current")


class _MwrRadiusServerIndex_Type(Integer32):
    """Custom type mwrRadiusServerIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_MwrRadiusServerIndex_Type.__name__ = "Integer32"
_MwrRadiusServerIndex_Object = MibTableColumn
mwrRadiusServerIndex = _MwrRadiusServerIndex_Object(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 7, 1, 2, 5, 1, 1),
    _MwrRadiusServerIndex_Type()
)
mwrRadiusServerIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mwrRadiusServerIndex.setStatus("current")
_MwrRadiusCfgdHostDomain_Type = InetAddressType
_MwrRadiusCfgdHostDomain_Object = MibTableColumn
mwrRadiusCfgdHostDomain = _MwrRadiusCfgdHostDomain_Object(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 7, 1, 2, 5, 1, 2),
    _MwrRadiusCfgdHostDomain_Type()
)
mwrRadiusCfgdHostDomain.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mwrRadiusCfgdHostDomain.setStatus("current")
_MwrRadiusCfgdHostAddress_Type = InetAddress
_MwrRadiusCfgdHostAddress_Object = MibTableColumn
mwrRadiusCfgdHostAddress = _MwrRadiusCfgdHostAddress_Object(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 7, 1, 2, 5, 1, 3),
    _MwrRadiusCfgdHostAddress_Type()
)
mwrRadiusCfgdHostAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mwrRadiusCfgdHostAddress.setStatus("current")


class _MwrRadiusCfgdHostKey_Type(DisplayString):
    """Custom type mwrRadiusCfgdHostKey based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_MwrRadiusCfgdHostKey_Type.__name__ = "DisplayString"
_MwrRadiusCfgdHostKey_Object = MibTableColumn
mwrRadiusCfgdHostKey = _MwrRadiusCfgdHostKey_Object(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 7, 1, 2, 5, 1, 4),
    _MwrRadiusCfgdHostKey_Type()
)
mwrRadiusCfgdHostKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mwrRadiusCfgdHostKey.setStatus("current")
_MwrNetworking_ObjectIdentity = ObjectIdentity
mwrNetworking = _MwrNetworking_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 8)
)
_MwrNetworkingConfigurations_ObjectIdentity = ObjectIdentity
mwrNetworkingConfigurations = _MwrNetworkingConfigurations_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 8, 1)
)
_MwrNetMgmtPriority_ObjectIdentity = ObjectIdentity
mwrNetMgmtPriority = _MwrNetMgmtPriority_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 8, 1, 1)
)


class _MwrNetMgmtVlanPriority_Type(Integer32):
    """Custom type mwrNetMgmtVlanPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_MwrNetMgmtVlanPriority_Type.__name__ = "Integer32"
_MwrNetMgmtVlanPriority_Object = MibScalar
mwrNetMgmtVlanPriority = _MwrNetMgmtVlanPriority_Object(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 8, 1, 1, 1),
    _MwrNetMgmtVlanPriority_Type()
)
mwrNetMgmtVlanPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mwrNetMgmtVlanPriority.setStatus("current")
_MwrNetMgmtDscp_Type = Integer32
_MwrNetMgmtDscp_Object = MibScalar
mwrNetMgmtDscp = _MwrNetMgmtDscp_Object(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 8, 1, 1, 2),
    _MwrNetMgmtDscp_Type()
)
mwrNetMgmtDscp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mwrNetMgmtDscp.setStatus("current")
_MwrNetMgmtIpv4_ObjectIdentity = ObjectIdentity
mwrNetMgmtIpv4 = _MwrNetMgmtIpv4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 8, 1, 2)
)
_MwrIpv4Table_Object = MibTable
mwrIpv4Table = _MwrIpv4Table_Object(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 8, 1, 2, 1)
)
if mibBuilder.loadTexts:
    mwrIpv4Table.setStatus("current")
_MwrIpv4Entry_Object = MibTableRow
mwrIpv4Entry = _MwrIpv4Entry_Object(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 8, 1, 2, 1, 1)
)
mwrIpv4Entry.setIndexNames(
    (0, "MWR-ETHERNET-MIB", "mwrIpv4Index"),
)
if mibBuilder.loadTexts:
    mwrIpv4Entry.setStatus("current")


class _MwrIpv4Index_Type(Integer32):
    """Custom type mwrIpv4Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_MwrIpv4Index_Type.__name__ = "Integer32"
_MwrIpv4Index_Object = MibTableColumn
mwrIpv4Index = _MwrIpv4Index_Object(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 8, 1, 2, 1, 1, 1),
    _MwrIpv4Index_Type()
)
mwrIpv4Index.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mwrIpv4Index.setStatus("current")
_MwrIpv4Address_Type = IpAddress
_MwrIpv4Address_Object = MibTableColumn
mwrIpv4Address = _MwrIpv4Address_Object(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 8, 1, 2, 1, 1, 2),
    _MwrIpv4Address_Type()
)
mwrIpv4Address.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mwrIpv4Address.setStatus("current")
_MwrIpv4SubnetMask_Type = IpAddress
_MwrIpv4SubnetMask_Object = MibTableColumn
mwrIpv4SubnetMask = _MwrIpv4SubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 8, 1, 2, 1, 1, 3),
    _MwrIpv4SubnetMask_Type()
)
mwrIpv4SubnetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mwrIpv4SubnetMask.setStatus("current")
_MwrIpv4DefaultGateway_Type = IpAddress
_MwrIpv4DefaultGateway_Object = MibTableColumn
mwrIpv4DefaultGateway = _MwrIpv4DefaultGateway_Object(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 8, 1, 2, 1, 1, 4),
    _MwrIpv4DefaultGateway_Type()
)
mwrIpv4DefaultGateway.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mwrIpv4DefaultGateway.setStatus("current")
_MwrIpv4RowStatus_Type = RowStatus
_MwrIpv4RowStatus_Object = MibTableColumn
mwrIpv4RowStatus = _MwrIpv4RowStatus_Object(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 8, 1, 2, 1, 1, 5),
    _MwrIpv4RowStatus_Type()
)
mwrIpv4RowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mwrIpv4RowStatus.setStatus("current")
_MwrSecondaryGateway_Type = IpAddress
_MwrSecondaryGateway_Object = MibScalar
mwrSecondaryGateway = _MwrSecondaryGateway_Object(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 8, 1, 2, 2),
    _MwrSecondaryGateway_Type()
)
mwrSecondaryGateway.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mwrSecondaryGateway.setStatus("current")
_MwrNetMgmttIpv6_ObjectIdentity = ObjectIdentity
mwrNetMgmttIpv6 = _MwrNetMgmttIpv6_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 8, 1, 3)
)
_MwrIpv6Table_Object = MibTable
mwrIpv6Table = _MwrIpv6Table_Object(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 8, 1, 3, 1)
)
if mibBuilder.loadTexts:
    mwrIpv6Table.setStatus("current")
_MwrIpv6Entry_Object = MibTableRow
mwrIpv6Entry = _MwrIpv6Entry_Object(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 8, 1, 3, 1, 1)
)
mwrIpv6Entry.setIndexNames(
    (0, "MWR-ETHERNET-MIB", "mwrIpv6Index"),
)
if mibBuilder.loadTexts:
    mwrIpv6Entry.setStatus("current")


class _MwrIpv6Index_Type(Integer32):
    """Custom type mwrIpv6Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_MwrIpv6Index_Type.__name__ = "Integer32"
_MwrIpv6Index_Object = MibTableColumn
mwrIpv6Index = _MwrIpv6Index_Object(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 8, 1, 3, 1, 1, 1),
    _MwrIpv6Index_Type()
)
mwrIpv6Index.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mwrIpv6Index.setStatus("current")
_MwrIpv6Domain_Type = InetAddressType
_MwrIpv6Domain_Object = MibTableColumn
mwrIpv6Domain = _MwrIpv6Domain_Object(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 8, 1, 3, 1, 1, 2),
    _MwrIpv6Domain_Type()
)
mwrIpv6Domain.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwrIpv6Domain.setStatus("current")
_MwrIpv6Address_Type = InetAddress
_MwrIpv6Address_Object = MibTableColumn
mwrIpv6Address = _MwrIpv6Address_Object(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 8, 1, 3, 1, 1, 3),
    _MwrIpv6Address_Type()
)
mwrIpv6Address.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mwrIpv6Address.setStatus("current")
_MwrIpv6Prefix_Type = Integer32
_MwrIpv6Prefix_Object = MibTableColumn
mwrIpv6Prefix = _MwrIpv6Prefix_Object(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 8, 1, 3, 1, 1, 4),
    _MwrIpv6Prefix_Type()
)
mwrIpv6Prefix.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mwrIpv6Prefix.setStatus("current")
_MwrIpv6GatewayDomain_Type = InetAddressType
_MwrIpv6GatewayDomain_Object = MibTableColumn
mwrIpv6GatewayDomain = _MwrIpv6GatewayDomain_Object(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 8, 1, 3, 1, 1, 5),
    _MwrIpv6GatewayDomain_Type()
)
mwrIpv6GatewayDomain.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwrIpv6GatewayDomain.setStatus("current")
_MwrIpv6GatewayAddress_Type = InetAddress
_MwrIpv6GatewayAddress_Object = MibTableColumn
mwrIpv6GatewayAddress = _MwrIpv6GatewayAddress_Object(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 8, 1, 3, 1, 1, 6),
    _MwrIpv6GatewayAddress_Type()
)
mwrIpv6GatewayAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mwrIpv6GatewayAddress.setStatus("current")
_MwrIpv6RowStatus_Type = RowStatus
_MwrIpv6RowStatus_Object = MibTableColumn
mwrIpv6RowStatus = _MwrIpv6RowStatus_Object(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 8, 1, 3, 1, 1, 7),
    _MwrIpv6RowStatus_Type()
)
mwrIpv6RowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mwrIpv6RowStatus.setStatus("current")
_MwrSecondaryIpv6GatewayDomain_Type = InetAddressType
_MwrSecondaryIpv6GatewayDomain_Object = MibScalar
mwrSecondaryIpv6GatewayDomain = _MwrSecondaryIpv6GatewayDomain_Object(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 8, 1, 3, 2),
    _MwrSecondaryIpv6GatewayDomain_Type()
)
mwrSecondaryIpv6GatewayDomain.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwrSecondaryIpv6GatewayDomain.setStatus("current")
_MwrSecondaryIpv6GatewayAddress_Type = InetAddress
_MwrSecondaryIpv6GatewayAddress_Object = MibScalar
mwrSecondaryIpv6GatewayAddress = _MwrSecondaryIpv6GatewayAddress_Object(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 8, 1, 3, 3),
    _MwrSecondaryIpv6GatewayAddress_Type()
)
mwrSecondaryIpv6GatewayAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mwrSecondaryIpv6GatewayAddress.setStatus("current")
_MwrUserInterfaceMgmt_ObjectIdentity = ObjectIdentity
mwrUserInterfaceMgmt = _MwrUserInterfaceMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 8, 1, 4)
)


class _MwrTelnetEnable_Type(EnableType):
    """Custom type mwrTelnetEnable based on EnableType"""
    defaultValue = 1


_MwrTelnetEnable_Type.__name__ = "EnableType"
_MwrTelnetEnable_Object = MibScalar
mwrTelnetEnable = _MwrTelnetEnable_Object(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 8, 1, 4, 1),
    _MwrTelnetEnable_Type()
)
mwrTelnetEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mwrTelnetEnable.setStatus("current")
_MwrSshEnable_Type = EnableType
_MwrSshEnable_Object = MibScalar
mwrSshEnable = _MwrSshEnable_Object(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 8, 1, 4, 2),
    _MwrSshEnable_Type()
)
mwrSshEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mwrSshEnable.setStatus("current")


class _MwrHttpEnable_Type(EnableType):
    """Custom type mwrHttpEnable based on EnableType"""
    defaultValue = 1


_MwrHttpEnable_Type.__name__ = "EnableType"
_MwrHttpEnable_Object = MibScalar
mwrHttpEnable = _MwrHttpEnable_Object(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 8, 1, 4, 3),
    _MwrHttpEnable_Type()
)
mwrHttpEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mwrHttpEnable.setStatus("current")
_MwrHttpsEnable_Type = EnableType
_MwrHttpsEnable_Object = MibScalar
mwrHttpsEnable = _MwrHttpsEnable_Object(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 8, 1, 4, 4),
    _MwrHttpsEnable_Type()
)
mwrHttpsEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mwrHttpsEnable.setStatus("current")
_MwrSnmpv1v2cEnable_Type = EnableType
_MwrSnmpv1v2cEnable_Object = MibScalar
mwrSnmpv1v2cEnable = _MwrSnmpv1v2cEnable_Object(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 8, 1, 4, 5),
    _MwrSnmpv1v2cEnable_Type()
)
mwrSnmpv1v2cEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mwrSnmpv1v2cEnable.setStatus("current")
_MwrFtpEnable_Type = EnableType
_MwrFtpEnable_Object = MibScalar
mwrFtpEnable = _MwrFtpEnable_Object(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 8, 1, 4, 6),
    _MwrFtpEnable_Type()
)
mwrFtpEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mwrFtpEnable.setStatus("current")
_MwrFileTransfer_ObjectIdentity = ObjectIdentity
mwrFileTransfer = _MwrFileTransfer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 8, 1, 5)
)


class _MwrFileXfrDirection_Type(Integer32):
    """Custom type mwrFileXfrDirection based on Integer32"""
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
        *(("serverMode", 1),
          ("clientMode", 2),
          ("both", 3))
    )


_MwrFileXfrDirection_Type.__name__ = "Integer32"
_MwrFileXfrDirection_Object = MibScalar
mwrFileXfrDirection = _MwrFileXfrDirection_Object(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 8, 1, 5, 1),
    _MwrFileXfrDirection_Type()
)
mwrFileXfrDirection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mwrFileXfrDirection.setStatus("current")
_MwrFileXfrTable_Object = MibTable
mwrFileXfrTable = _MwrFileXfrTable_Object(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 8, 1, 5, 2)
)
if mibBuilder.loadTexts:
    mwrFileXfrTable.setStatus("current")
_MwrFileXfrEntry_Object = MibTableRow
mwrFileXfrEntry = _MwrFileXfrEntry_Object(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 8, 1, 5, 2, 1)
)
mwrFileXfrEntry.setIndexNames(
    (0, "MWR-ETHERNET-MIB", "mwrFileXfrSeqID"),
)
if mibBuilder.loadTexts:
    mwrFileXfrEntry.setStatus("current")


class _MwrFileXfrSeqID_Type(Integer32):
    """Custom type mwrFileXfrSeqID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 20),
    )


_MwrFileXfrSeqID_Type.__name__ = "Integer32"
_MwrFileXfrSeqID_Object = MibTableColumn
mwrFileXfrSeqID = _MwrFileXfrSeqID_Object(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 8, 1, 5, 2, 1, 1),
    _MwrFileXfrSeqID_Type()
)
mwrFileXfrSeqID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mwrFileXfrSeqID.setStatus("current")


class _MwrFileXfrIdentifier_Type(Integer32):
    """Custom type mwrFileXfrIdentifier based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("omni", 1),
          ("tcfFile", 2),
          ("configFile", 3),
          ("eventLog", 4),
          ("pmFile", 5),
          ("security", 6),
          ("perfLog", 7))
    )


_MwrFileXfrIdentifier_Type.__name__ = "Integer32"
_MwrFileXfrIdentifier_Object = MibTableColumn
mwrFileXfrIdentifier = _MwrFileXfrIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 8, 1, 5, 2, 1, 2),
    _MwrFileXfrIdentifier_Type()
)
mwrFileXfrIdentifier.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mwrFileXfrIdentifier.setStatus("current")


class _MwrFileXfrName_Type(DisplayString):
    """Custom type mwrFileXfrName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_MwrFileXfrName_Type.__name__ = "DisplayString"
_MwrFileXfrName_Object = MibTableColumn
mwrFileXfrName = _MwrFileXfrName_Object(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 8, 1, 5, 2, 1, 3),
    _MwrFileXfrName_Type()
)
mwrFileXfrName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mwrFileXfrName.setStatus("current")


class _MwrFileXfrMode_Type(Integer32):
    """Custom type mwrFileXfrMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ftp", 1),
          ("sftp", 2))
    )


_MwrFileXfrMode_Type.__name__ = "Integer32"
_MwrFileXfrMode_Object = MibTableColumn
mwrFileXfrMode = _MwrFileXfrMode_Object(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 8, 1, 5, 2, 1, 4),
    _MwrFileXfrMode_Type()
)
mwrFileXfrMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mwrFileXfrMode.setStatus("current")
_MwrFileXfrServerDomain_Type = InetAddressType
_MwrFileXfrServerDomain_Object = MibTableColumn
mwrFileXfrServerDomain = _MwrFileXfrServerDomain_Object(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 8, 1, 5, 2, 1, 5),
    _MwrFileXfrServerDomain_Type()
)
mwrFileXfrServerDomain.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mwrFileXfrServerDomain.setStatus("current")
_MwrFileXfrServerAddress_Type = InetAddress
_MwrFileXfrServerAddress_Object = MibTableColumn
mwrFileXfrServerAddress = _MwrFileXfrServerAddress_Object(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 8, 1, 5, 2, 1, 6),
    _MwrFileXfrServerAddress_Type()
)
mwrFileXfrServerAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mwrFileXfrServerAddress.setStatus("current")


class _MwrFileXfrClientDirection_Type(Integer32):
    """Custom type mwrFileXfrClientDirection based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("import", 1),
          ("export", 2))
    )


_MwrFileXfrClientDirection_Type.__name__ = "Integer32"
_MwrFileXfrClientDirection_Object = MibTableColumn
mwrFileXfrClientDirection = _MwrFileXfrClientDirection_Object(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 8, 1, 5, 2, 1, 7),
    _MwrFileXfrClientDirection_Type()
)
mwrFileXfrClientDirection.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mwrFileXfrClientDirection.setStatus("current")


class _MwrFileXfrUserName_Type(DisplayString):
    """Custom type mwrFileXfrUserName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_MwrFileXfrUserName_Type.__name__ = "DisplayString"
_MwrFileXfrUserName_Object = MibTableColumn
mwrFileXfrUserName = _MwrFileXfrUserName_Object(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 8, 1, 5, 2, 1, 8),
    _MwrFileXfrUserName_Type()
)
mwrFileXfrUserName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mwrFileXfrUserName.setStatus("current")


class _MwrFileXfrPassword_Type(DisplayString):
    """Custom type mwrFileXfrPassword based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_MwrFileXfrPassword_Type.__name__ = "DisplayString"
_MwrFileXfrPassword_Object = MibTableColumn
mwrFileXfrPassword = _MwrFileXfrPassword_Object(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 8, 1, 5, 2, 1, 9),
    _MwrFileXfrPassword_Type()
)
mwrFileXfrPassword.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mwrFileXfrPassword.setStatus("current")
_MwrFileXfrNumEntries_Type = Integer32
_MwrFileXfrNumEntries_Object = MibTableColumn
mwrFileXfrNumEntries = _MwrFileXfrNumEntries_Object(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 8, 1, 5, 2, 1, 10),
    _MwrFileXfrNumEntries_Type()
)
mwrFileXfrNumEntries.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mwrFileXfrNumEntries.setStatus("current")


class _MwrFileXfrStatus_Type(Integer32):
    """Custom type mwrFileXfrStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("success", 1),
          ("inProgress", 2),
          ("failed", 3))
    )


_MwrFileXfrStatus_Type.__name__ = "Integer32"
_MwrFileXfrStatus_Object = MibTableColumn
mwrFileXfrStatus = _MwrFileXfrStatus_Object(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 8, 1, 5, 2, 1, 11),
    _MwrFileXfrStatus_Type()
)
mwrFileXfrStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwrFileXfrStatus.setStatus("current")
_MwrFileXfrRowStatus_Type = RowStatus
_MwrFileXfrRowStatus_Object = MibTableColumn
mwrFileXfrRowStatus = _MwrFileXfrRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 8, 1, 5, 2, 1, 12),
    _MwrFileXfrRowStatus_Type()
)
mwrFileXfrRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mwrFileXfrRowStatus.setStatus("current")
_MwrNetMgmtInterfaceTable_Object = MibTable
mwrNetMgmtInterfaceTable = _MwrNetMgmtInterfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 8, 1, 6)
)
if mibBuilder.loadTexts:
    mwrNetMgmtInterfaceTable.setStatus("current")
_MwrNetMgmtInterfaceEntry_Object = MibTableRow
mwrNetMgmtInterfaceEntry = _MwrNetMgmtInterfaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 8, 1, 6, 1)
)
mwrNetMgmtInterfaceEntry.setIndexNames(
    (0, "MWR-ETHERNET-MIB", "mwrNetMgmtInterfaceIndex"),
)
if mibBuilder.loadTexts:
    mwrNetMgmtInterfaceEntry.setStatus("current")
_MwrNetMgmtInterfaceIndex_Type = Integer32
_MwrNetMgmtInterfaceIndex_Object = MibTableColumn
mwrNetMgmtInterfaceIndex = _MwrNetMgmtInterfaceIndex_Object(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 8, 1, 6, 1, 1),
    _MwrNetMgmtInterfaceIndex_Type()
)
mwrNetMgmtInterfaceIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mwrNetMgmtInterfaceIndex.setStatus("current")


class _MwrNetMgmtVlanId_Type(Integer32):
    """Custom type mwrNetMgmtVlanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4090),
    )


_MwrNetMgmtVlanId_Type.__name__ = "Integer32"
_MwrNetMgmtVlanId_Object = MibTableColumn
mwrNetMgmtVlanId = _MwrNetMgmtVlanId_Object(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 8, 1, 6, 1, 2),
    _MwrNetMgmtVlanId_Type()
)
mwrNetMgmtVlanId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mwrNetMgmtVlanId.setStatus("current")
_MwrNetMgmtInterface1_Type = EnableType
_MwrNetMgmtInterface1_Object = MibTableColumn
mwrNetMgmtInterface1 = _MwrNetMgmtInterface1_Object(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 8, 1, 6, 1, 3),
    _MwrNetMgmtInterface1_Type()
)
mwrNetMgmtInterface1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mwrNetMgmtInterface1.setStatus("current")


class _MwrNetMgmtInterface1Mode_Type(Integer32):
    """Custom type mwrNetMgmtInterface1Mode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("inband", 1),
          ("outOfBand", 2),
          ("none", 3))
    )


_MwrNetMgmtInterface1Mode_Type.__name__ = "Integer32"
_MwrNetMgmtInterface1Mode_Object = MibTableColumn
mwrNetMgmtInterface1Mode = _MwrNetMgmtInterface1Mode_Object(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 8, 1, 6, 1, 4),
    _MwrNetMgmtInterface1Mode_Type()
)
mwrNetMgmtInterface1Mode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mwrNetMgmtInterface1Mode.setStatus("current")


class _MwrNetMgmtInterface1Tagged_Type(Integer32):
    """Custom type mwrNetMgmtInterface1Tagged based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no-vlan-tag", 1),
          ("vlan-tag", 2))
    )


_MwrNetMgmtInterface1Tagged_Type.__name__ = "Integer32"
_MwrNetMgmtInterface1Tagged_Object = MibTableColumn
mwrNetMgmtInterface1Tagged = _MwrNetMgmtInterface1Tagged_Object(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 8, 1, 6, 1, 5),
    _MwrNetMgmtInterface1Tagged_Type()
)
mwrNetMgmtInterface1Tagged.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mwrNetMgmtInterface1Tagged.setStatus("current")
_MwrNetMgmtInterface2_Type = EnableType
_MwrNetMgmtInterface2_Object = MibTableColumn
mwrNetMgmtInterface2 = _MwrNetMgmtInterface2_Object(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 8, 1, 6, 1, 6),
    _MwrNetMgmtInterface2_Type()
)
mwrNetMgmtInterface2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mwrNetMgmtInterface2.setStatus("current")


class _MwrNetMgmtInterface2Mode_Type(Integer32):
    """Custom type mwrNetMgmtInterface2Mode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("inband", 1),
          ("outOfBand", 2),
          ("none", 3))
    )


_MwrNetMgmtInterface2Mode_Type.__name__ = "Integer32"
_MwrNetMgmtInterface2Mode_Object = MibTableColumn
mwrNetMgmtInterface2Mode = _MwrNetMgmtInterface2Mode_Object(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 8, 1, 6, 1, 7),
    _MwrNetMgmtInterface2Mode_Type()
)
mwrNetMgmtInterface2Mode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mwrNetMgmtInterface2Mode.setStatus("current")


class _MwrNetMgmtInterface2Tagged_Type(Integer32):
    """Custom type mwrNetMgmtInterface2Tagged based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no-vlan-tag", 1),
          ("vlan-tag", 2))
    )


_MwrNetMgmtInterface2Tagged_Type.__name__ = "Integer32"
_MwrNetMgmtInterface2Tagged_Object = MibTableColumn
mwrNetMgmtInterface2Tagged = _MwrNetMgmtInterface2Tagged_Object(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 8, 1, 6, 1, 8),
    _MwrNetMgmtInterface2Tagged_Type()
)
mwrNetMgmtInterface2Tagged.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mwrNetMgmtInterface2Tagged.setStatus("current")
_MwrNetMgmtInterface3_Type = EnableType
_MwrNetMgmtInterface3_Object = MibTableColumn
mwrNetMgmtInterface3 = _MwrNetMgmtInterface3_Object(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 8, 1, 6, 1, 9),
    _MwrNetMgmtInterface3_Type()
)
mwrNetMgmtInterface3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mwrNetMgmtInterface3.setStatus("current")


class _MwrNetMgmtInterface3Mode_Type(Integer32):
    """Custom type mwrNetMgmtInterface3Mode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("inband", 1),
          ("outOfBand", 2),
          ("none", 3))
    )


_MwrNetMgmtInterface3Mode_Type.__name__ = "Integer32"
_MwrNetMgmtInterface3Mode_Object = MibTableColumn
mwrNetMgmtInterface3Mode = _MwrNetMgmtInterface3Mode_Object(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 8, 1, 6, 1, 10),
    _MwrNetMgmtInterface3Mode_Type()
)
mwrNetMgmtInterface3Mode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mwrNetMgmtInterface3Mode.setStatus("current")


class _MwrNetMgmtInterface3Tagged_Type(Integer32):
    """Custom type mwrNetMgmtInterface3Tagged based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no-vlan-tag", 1),
          ("vlan-tag", 2))
    )


_MwrNetMgmtInterface3Tagged_Type.__name__ = "Integer32"
_MwrNetMgmtInterface3Tagged_Object = MibTableColumn
mwrNetMgmtInterface3Tagged = _MwrNetMgmtInterface3Tagged_Object(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 8, 1, 6, 1, 11),
    _MwrNetMgmtInterface3Tagged_Type()
)
mwrNetMgmtInterface3Tagged.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mwrNetMgmtInterface3Tagged.setStatus("current")
_MwrNetMgmtInterface4_Type = EnableType
_MwrNetMgmtInterface4_Object = MibTableColumn
mwrNetMgmtInterface4 = _MwrNetMgmtInterface4_Object(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 8, 1, 6, 1, 12),
    _MwrNetMgmtInterface4_Type()
)
mwrNetMgmtInterface4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mwrNetMgmtInterface4.setStatus("current")


class _MwrNetMgmtInterface4Mode_Type(Integer32):
    """Custom type mwrNetMgmtInterface4Mode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("inband", 1),
          ("outOfBand", 2),
          ("none", 3))
    )


_MwrNetMgmtInterface4Mode_Type.__name__ = "Integer32"
_MwrNetMgmtInterface4Mode_Object = MibTableColumn
mwrNetMgmtInterface4Mode = _MwrNetMgmtInterface4Mode_Object(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 8, 1, 6, 1, 13),
    _MwrNetMgmtInterface4Mode_Type()
)
mwrNetMgmtInterface4Mode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mwrNetMgmtInterface4Mode.setStatus("current")


class _MwrNetMgmtInterface4Tagged_Type(Integer32):
    """Custom type mwrNetMgmtInterface4Tagged based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no-vlan-tag", 1),
          ("vlan-tag", 2))
    )


_MwrNetMgmtInterface4Tagged_Type.__name__ = "Integer32"
_MwrNetMgmtInterface4Tagged_Object = MibTableColumn
mwrNetMgmtInterface4Tagged = _MwrNetMgmtInterface4Tagged_Object(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 8, 1, 6, 1, 14),
    _MwrNetMgmtInterface4Tagged_Type()
)
mwrNetMgmtInterface4Tagged.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mwrNetMgmtInterface4Tagged.setStatus("current")
_MwrNetMgmtInterfaceRowStatus_Type = RowStatus
_MwrNetMgmtInterfaceRowStatus_Object = MibTableColumn
mwrNetMgmtInterfaceRowStatus = _MwrNetMgmtInterfaceRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 8, 1, 6, 1, 15),
    _MwrNetMgmtInterfaceRowStatus_Type()
)
mwrNetMgmtInterfaceRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mwrNetMgmtInterfaceRowStatus.setStatus("current")
_MwrNetworkingStatus_ObjectIdentity = ObjectIdentity
mwrNetworkingStatus = _MwrNetworkingStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 8, 2)
)
_MwrMaintenanceIpv4_ObjectIdentity = ObjectIdentity
mwrMaintenanceIpv4 = _MwrMaintenanceIpv4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 8, 2, 1)
)
_MwrMaintenanceIpv4Address_Type = IpAddress
_MwrMaintenanceIpv4Address_Object = MibScalar
mwrMaintenanceIpv4Address = _MwrMaintenanceIpv4Address_Object(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 8, 2, 1, 1),
    _MwrMaintenanceIpv4Address_Type()
)
mwrMaintenanceIpv4Address.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwrMaintenanceIpv4Address.setStatus("current")
_MwrMaintenanceSubnetMask_Type = IpAddress
_MwrMaintenanceSubnetMask_Object = MibScalar
mwrMaintenanceSubnetMask = _MwrMaintenanceSubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 8, 2, 1, 2),
    _MwrMaintenanceSubnetMask_Type()
)
mwrMaintenanceSubnetMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwrMaintenanceSubnetMask.setStatus("current")
_MwrActiveIpv4Gateway_Type = IpAddress
_MwrActiveIpv4Gateway_Object = MibScalar
mwrActiveIpv4Gateway = _MwrActiveIpv4Gateway_Object(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 8, 2, 1, 3),
    _MwrActiveIpv4Gateway_Type()
)
mwrActiveIpv4Gateway.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwrActiveIpv4Gateway.setStatus("current")
_MwrMaintenanceIpv6_ObjectIdentity = ObjectIdentity
mwrMaintenanceIpv6 = _MwrMaintenanceIpv6_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 8, 2, 2)
)
_MwrIpv6LinkLocalIPrefix_Type = Integer32
_MwrIpv6LinkLocalIPrefix_Object = MibScalar
mwrIpv6LinkLocalIPrefix = _MwrIpv6LinkLocalIPrefix_Object(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 8, 2, 2, 1),
    _MwrIpv6LinkLocalIPrefix_Type()
)
mwrIpv6LinkLocalIPrefix.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwrIpv6LinkLocalIPrefix.setStatus("current")
_MwrIpv6LinkLocalAddress_Type = InetAddress
_MwrIpv6LinkLocalAddress_Object = MibScalar
mwrIpv6LinkLocalAddress = _MwrIpv6LinkLocalAddress_Object(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 8, 2, 2, 2),
    _MwrIpv6LinkLocalAddress_Type()
)
mwrIpv6LinkLocalAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwrIpv6LinkLocalAddress.setStatus("current")
_MwrActiveIpv6Gateway_Type = InetAddress
_MwrActiveIpv6Gateway_Object = MibScalar
mwrActiveIpv6Gateway = _MwrActiveIpv6Gateway_Object(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 8, 2, 2, 3),
    _MwrActiveIpv6Gateway_Type()
)
mwrActiveIpv6Gateway.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwrActiveIpv6Gateway.setStatus("current")
_MwrPeerNetworkingStatus_ObjectIdentity = ObjectIdentity
mwrPeerNetworkingStatus = _MwrPeerNetworkingStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 8, 3)
)
_MwrPeerMacAddress_Type = DisplayString
_MwrPeerMacAddress_Object = MibScalar
mwrPeerMacAddress = _MwrPeerMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 8, 3, 1),
    _MwrPeerMacAddress_Type()
)
mwrPeerMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwrPeerMacAddress.setStatus("current")
_MwrPeerIpv4Address_Type = IpAddress
_MwrPeerIpv4Address_Object = MibScalar
mwrPeerIpv4Address = _MwrPeerIpv4Address_Object(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 8, 3, 2),
    _MwrPeerIpv4Address_Type()
)
mwrPeerIpv4Address.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwrPeerIpv4Address.setStatus("current")
_MwrPeerIpv4SubnetMask_Type = IpAddress
_MwrPeerIpv4SubnetMask_Object = MibScalar
mwrPeerIpv4SubnetMask = _MwrPeerIpv4SubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 8, 3, 3),
    _MwrPeerIpv4SubnetMask_Type()
)
mwrPeerIpv4SubnetMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwrPeerIpv4SubnetMask.setStatus("current")
_MwrPeerIpv4DefaultGateway_Type = IpAddress
_MwrPeerIpv4DefaultGateway_Object = MibScalar
mwrPeerIpv4DefaultGateway = _MwrPeerIpv4DefaultGateway_Object(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 8, 3, 4),
    _MwrPeerIpv4DefaultGateway_Type()
)
mwrPeerIpv4DefaultGateway.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwrPeerIpv4DefaultGateway.setStatus("current")
_MwrPeerIpv6Prefix_Type = Integer32
_MwrPeerIpv6Prefix_Object = MibScalar
mwrPeerIpv6Prefix = _MwrPeerIpv6Prefix_Object(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 8, 3, 5),
    _MwrPeerIpv6Prefix_Type()
)
mwrPeerIpv6Prefix.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwrPeerIpv6Prefix.setStatus("current")
_MwrPeerIpv6Domain_Type = InetAddressType
_MwrPeerIpv6Domain_Object = MibScalar
mwrPeerIpv6Domain = _MwrPeerIpv6Domain_Object(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 8, 3, 6),
    _MwrPeerIpv6Domain_Type()
)
mwrPeerIpv6Domain.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwrPeerIpv6Domain.setStatus("current")
_MwrPeerIpv6Address_Type = InetAddress
_MwrPeerIpv6Address_Object = MibScalar
mwrPeerIpv6Address = _MwrPeerIpv6Address_Object(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 8, 3, 7),
    _MwrPeerIpv6Address_Type()
)
mwrPeerIpv6Address.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwrPeerIpv6Address.setStatus("current")
_MwrPeerIpv6GatewayDomain_Type = InetAddressType
_MwrPeerIpv6GatewayDomain_Object = MibScalar
mwrPeerIpv6GatewayDomain = _MwrPeerIpv6GatewayDomain_Object(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 8, 3, 8),
    _MwrPeerIpv6GatewayDomain_Type()
)
mwrPeerIpv6GatewayDomain.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwrPeerIpv6GatewayDomain.setStatus("current")
_MwrPeerIpv6GatewayAddress_Type = InetAddress
_MwrPeerIpv6GatewayAddress_Object = MibScalar
mwrPeerIpv6GatewayAddress = _MwrPeerIpv6GatewayAddress_Object(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 8, 3, 9),
    _MwrPeerIpv6GatewayAddress_Type()
)
mwrPeerIpv6GatewayAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwrPeerIpv6GatewayAddress.setStatus("current")
_MwrPeerVlanId_Type = Integer32
_MwrPeerVlanId_Object = MibScalar
mwrPeerVlanId = _MwrPeerVlanId_Object(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 8, 3, 10),
    _MwrPeerVlanId_Type()
)
mwrPeerVlanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwrPeerVlanId.setStatus("current")
_MwrPeerVlanPriority_Type = Integer32
_MwrPeerVlanPriority_Object = MibScalar
mwrPeerVlanPriority = _MwrPeerVlanPriority_Object(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 8, 3, 11),
    _MwrPeerVlanPriority_Type()
)
mwrPeerVlanPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwrPeerVlanPriority.setStatus("current")
_MwrPeerDscp_Type = Integer32
_MwrPeerDscp_Object = MibScalar
mwrPeerDscp = _MwrPeerDscp_Object(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 8, 3, 12),
    _MwrPeerDscp_Type()
)
mwrPeerDscp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwrPeerDscp.setStatus("current")
_MwrNetworkingNotifications_ObjectIdentity = ObjectIdentity
mwrNetworkingNotifications = _MwrNetworkingNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 8, 4)
)
_MwrEthernet_ObjectIdentity = ObjectIdentity
mwrEthernet = _MwrEthernet_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 9)
)
_MwrEthernetConfigurations_ObjectIdentity = ObjectIdentity
mwrEthernetConfigurations = _MwrEthernetConfigurations_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 9, 1)
)
_MwrQos_ObjectIdentity = ObjectIdentity
mwrQos = _MwrQos_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 9, 1, 1)
)


class _MwrQosState_Type(EnableType):
    """Custom type mwrQosState based on EnableType"""
    defaultValue = 0


_MwrQosState_Type.__name__ = "EnableType"
_MwrQosState_Object = MibScalar
mwrQosState = _MwrQosState_Object(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 9, 1, 1, 1),
    _MwrQosState_Type()
)
mwrQosState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mwrQosState.setStatus("current")


class _MwrCosSource_Type(Integer32):
    """Custom type mwrCosSource based on Integer32"""
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
        *(("oTag", 1),
          ("iTag", 2),
          ("dscp", 3),
          ("mplsExp", 4))
    )


_MwrCosSource_Type.__name__ = "Integer32"
_MwrCosSource_Object = MibScalar
mwrCosSource = _MwrCosSource_Object(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 9, 1, 1, 2),
    _MwrCosSource_Type()
)
mwrCosSource.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mwrCosSource.setStatus("current")
_MwrOuterTpid_Type = DisplayString
_MwrOuterTpid_Object = MibScalar
mwrOuterTpid = _MwrOuterTpid_Object(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 9, 1, 1, 3),
    _MwrOuterTpid_Type()
)
mwrOuterTpid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mwrOuterTpid.setStatus("current")
_MwrInnerTpid_Type = DisplayString
_MwrInnerTpid_Object = MibScalar
mwrInnerTpid = _MwrInnerTpid_Object(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 9, 1, 1, 4),
    _MwrInnerTpid_Type()
)
mwrInnerTpid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mwrInnerTpid.setStatus("current")
_MwrCosTable_Object = MibTable
mwrCosTable = _MwrCosTable_Object(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 9, 1, 1, 5)
)
if mibBuilder.loadTexts:
    mwrCosTable.setStatus("current")
_MwrCosEntry_Object = MibTableRow
mwrCosEntry = _MwrCosEntry_Object(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 9, 1, 1, 5, 1)
)
mwrCosEntry.setIndexNames(
    (0, "MWR-ETHERNET-MIB", "mwrCosIndex"),
)
if mibBuilder.loadTexts:
    mwrCosEntry.setStatus("current")


class _MwrCosIndex_Type(Integer32):
    """Custom type mwrCosIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("gi01", 1),
          ("gi02", 2),
          ("gi03", 3),
          ("gi04", 4),
          ("bridgeMode", 5))
    )


_MwrCosIndex_Type.__name__ = "Integer32"
_MwrCosIndex_Object = MibTableColumn
mwrCosIndex = _MwrCosIndex_Object(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 9, 1, 1, 5, 1, 1),
    _MwrCosIndex_Type()
)
mwrCosIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mwrCosIndex.setStatus("current")
_MwrCos0_Type = QueueType
_MwrCos0_Object = MibTableColumn
mwrCos0 = _MwrCos0_Object(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 9, 1, 1, 5, 1, 2),
    _MwrCos0_Type()
)
mwrCos0.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mwrCos0.setStatus("current")
_MwrCos1_Type = QueueType
_MwrCos1_Object = MibTableColumn
mwrCos1 = _MwrCos1_Object(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 9, 1, 1, 5, 1, 3),
    _MwrCos1_Type()
)
mwrCos1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mwrCos1.setStatus("current")
_MwrCos2_Type = QueueType
_MwrCos2_Object = MibTableColumn
mwrCos2 = _MwrCos2_Object(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 9, 1, 1, 5, 1, 4),
    _MwrCos2_Type()
)
mwrCos2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mwrCos2.setStatus("current")
_MwrCos3_Type = QueueType
_MwrCos3_Object = MibTableColumn
mwrCos3 = _MwrCos3_Object(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 9, 1, 1, 5, 1, 5),
    _MwrCos3_Type()
)
mwrCos3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mwrCos3.setStatus("current")
_MwrCos4_Type = QueueType
_MwrCos4_Object = MibTableColumn
mwrCos4 = _MwrCos4_Object(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 9, 1, 1, 5, 1, 6),
    _MwrCos4_Type()
)
mwrCos4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mwrCos4.setStatus("current")
_MwrCos5_Type = QueueType
_MwrCos5_Object = MibTableColumn
mwrCos5 = _MwrCos5_Object(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 9, 1, 1, 5, 1, 7),
    _MwrCos5_Type()
)
mwrCos5.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mwrCos5.setStatus("current")
_MwrCos6_Type = QueueType
_MwrCos6_Object = MibTableColumn
mwrCos6 = _MwrCos6_Object(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 9, 1, 1, 5, 1, 8),
    _MwrCos6_Type()
)
mwrCos6.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mwrCos6.setStatus("current")
_MwrCos7_Type = QueueType
_MwrCos7_Object = MibTableColumn
mwrCos7 = _MwrCos7_Object(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 9, 1, 1, 5, 1, 9),
    _MwrCos7_Type()
)
mwrCos7.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mwrCos7.setStatus("current")
_MwrCosRowStatus_Type = RowStatus
_MwrCosRowStatus_Object = MibTableColumn
mwrCosRowStatus = _MwrCosRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 9, 1, 1, 5, 1, 10),
    _MwrCosRowStatus_Type()
)
mwrCosRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mwrCosRowStatus.setStatus("current")
_MwrCosDefValueTable_Object = MibTable
mwrCosDefValueTable = _MwrCosDefValueTable_Object(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 9, 1, 1, 6)
)
if mibBuilder.loadTexts:
    mwrCosDefValueTable.setStatus("current")
_MwrCosDefValueEntry_Object = MibTableRow
mwrCosDefValueEntry = _MwrCosDefValueEntry_Object(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 9, 1, 1, 6, 1)
)
mwrCosDefValueEntry.setIndexNames(
    (0, "MWR-ETHERNET-MIB", "mwrCosDefValueIndex"),
)
if mibBuilder.loadTexts:
    mwrCosDefValueEntry.setStatus("current")


class _MwrCosDefValueIndex_Type(Integer32):
    """Custom type mwrCosDefValueIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("gi01", 1),
          ("gi02", 2),
          ("gi03", 3),
          ("gi04", 4),
          ("bridgeMode", 5))
    )


_MwrCosDefValueIndex_Type.__name__ = "Integer32"
_MwrCosDefValueIndex_Object = MibTableColumn
mwrCosDefValueIndex = _MwrCosDefValueIndex_Object(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 9, 1, 1, 6, 1, 1),
    _MwrCosDefValueIndex_Type()
)
mwrCosDefValueIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mwrCosDefValueIndex.setStatus("current")
_MwrCosDefValue_Type = Integer32
_MwrCosDefValue_Object = MibTableColumn
mwrCosDefValue = _MwrCosDefValue_Object(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 9, 1, 1, 6, 1, 2),
    _MwrCosDefValue_Type()
)
mwrCosDefValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mwrCosDefValue.setStatus("current")
_MwrCirQTable_Object = MibTable
mwrCirQTable = _MwrCirQTable_Object(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 9, 1, 1, 7)
)
if mibBuilder.loadTexts:
    mwrCirQTable.setStatus("current")
_MwrCirQEntry_Object = MibTableRow
mwrCirQEntry = _MwrCirQEntry_Object(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 9, 1, 1, 7, 1)
)
mwrCirQEntry.setIndexNames(
    (0, "MWR-ETHERNET-MIB", "mwrCirQIndex"),
)
if mibBuilder.loadTexts:
    mwrCirQEntry.setStatus("current")
_MwrCirQIndex_Type = QueueType
_MwrCirQIndex_Object = MibTableColumn
mwrCirQIndex = _MwrCirQIndex_Object(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 9, 1, 1, 7, 1, 1),
    _MwrCirQIndex_Type()
)
mwrCirQIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mwrCirQIndex.setStatus("current")
_MwrCirQ1_Type = Integer32
_MwrCirQ1_Object = MibTableColumn
mwrCirQ1 = _MwrCirQ1_Object(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 9, 1, 1, 7, 1, 2),
    _MwrCirQ1_Type()
)
mwrCirQ1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mwrCirQ1.setStatus("current")
_MwrCirQ2_Type = Integer32
_MwrCirQ2_Object = MibTableColumn
mwrCirQ2 = _MwrCirQ2_Object(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 9, 1, 1, 7, 1, 3),
    _MwrCirQ2_Type()
)
mwrCirQ2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mwrCirQ2.setStatus("current")
_MwrCirQ3_Type = Integer32
_MwrCirQ3_Object = MibTableColumn
mwrCirQ3 = _MwrCirQ3_Object(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 9, 1, 1, 7, 1, 4),
    _MwrCirQ3_Type()
)
mwrCirQ3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mwrCirQ3.setStatus("current")
_MwrCirQ4_Type = Integer32
_MwrCirQ4_Object = MibTableColumn
mwrCirQ4 = _MwrCirQ4_Object(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 9, 1, 1, 7, 1, 5),
    _MwrCirQ4_Type()
)
mwrCirQ4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mwrCirQ4.setStatus("current")
_MwrCirQ5_Type = Integer32
_MwrCirQ5_Object = MibTableColumn
mwrCirQ5 = _MwrCirQ5_Object(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 9, 1, 1, 7, 1, 6),
    _MwrCirQ5_Type()
)
mwrCirQ5.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mwrCirQ5.setStatus("current")
_MwrCirQ6_Type = Integer32
_MwrCirQ6_Object = MibTableColumn
mwrCirQ6 = _MwrCirQ6_Object(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 9, 1, 1, 7, 1, 7),
    _MwrCirQ6_Type()
)
mwrCirQ6.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mwrCirQ6.setStatus("current")
_MwrCirQ7_Type = Integer32
_MwrCirQ7_Object = MibTableColumn
mwrCirQ7 = _MwrCirQ7_Object(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 9, 1, 1, 7, 1, 8),
    _MwrCirQ7_Type()
)
mwrCirQ7.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mwrCirQ7.setStatus("current")
_MwrCirQ8_Type = Integer32
_MwrCirQ8_Object = MibTableColumn
mwrCirQ8 = _MwrCirQ8_Object(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 9, 1, 1, 7, 1, 9),
    _MwrCirQ8_Type()
)
mwrCirQ8.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mwrCirQ8.setStatus("current")
_MwrCirQRowStatus_Type = RowStatus
_MwrCirQRowStatus_Object = MibTableColumn
mwrCirQRowStatus = _MwrCirQRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 9, 1, 1, 7, 1, 10),
    _MwrCirQRowStatus_Type()
)
mwrCirQRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mwrCirQRowStatus.setStatus("current")
_MwrCbsQTable_Object = MibTable
mwrCbsQTable = _MwrCbsQTable_Object(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 9, 1, 1, 8)
)
if mibBuilder.loadTexts:
    mwrCbsQTable.setStatus("current")
_MwrCbsQEntry_Object = MibTableRow
mwrCbsQEntry = _MwrCbsQEntry_Object(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 9, 1, 1, 8, 1)
)
mwrCbsQEntry.setIndexNames(
    (0, "MWR-ETHERNET-MIB", "mwrCbsQIndex"),
)
if mibBuilder.loadTexts:
    mwrCbsQEntry.setStatus("current")
_MwrCbsQIndex_Type = QueueType
_MwrCbsQIndex_Object = MibTableColumn
mwrCbsQIndex = _MwrCbsQIndex_Object(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 9, 1, 1, 8, 1, 1),
    _MwrCbsQIndex_Type()
)
mwrCbsQIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mwrCbsQIndex.setStatus("current")
_MwrCbsQ1_Type = Integer32
_MwrCbsQ1_Object = MibTableColumn
mwrCbsQ1 = _MwrCbsQ1_Object(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 9, 1, 1, 8, 1, 2),
    _MwrCbsQ1_Type()
)
mwrCbsQ1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mwrCbsQ1.setStatus("current")
_MwrCbsQ2_Type = Integer32
_MwrCbsQ2_Object = MibTableColumn
mwrCbsQ2 = _MwrCbsQ2_Object(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 9, 1, 1, 8, 1, 3),
    _MwrCbsQ2_Type()
)
mwrCbsQ2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mwrCbsQ2.setStatus("current")
_MwrCbsQ3_Type = Integer32
_MwrCbsQ3_Object = MibTableColumn
mwrCbsQ3 = _MwrCbsQ3_Object(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 9, 1, 1, 8, 1, 4),
    _MwrCbsQ3_Type()
)
mwrCbsQ3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mwrCbsQ3.setStatus("current")
_MwrCbsQ4_Type = Integer32
_MwrCbsQ4_Object = MibTableColumn
mwrCbsQ4 = _MwrCbsQ4_Object(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 9, 1, 1, 8, 1, 5),
    _MwrCbsQ4_Type()
)
mwrCbsQ4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mwrCbsQ4.setStatus("current")
_MwrCbsQ5_Type = Integer32
_MwrCbsQ5_Object = MibTableColumn
mwrCbsQ5 = _MwrCbsQ5_Object(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 9, 1, 1, 8, 1, 6),
    _MwrCbsQ5_Type()
)
mwrCbsQ5.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mwrCbsQ5.setStatus("current")
_MwrCbsQ6_Type = Integer32
_MwrCbsQ6_Object = MibTableColumn
mwrCbsQ6 = _MwrCbsQ6_Object(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 9, 1, 1, 8, 1, 7),
    _MwrCbsQ6_Type()
)
mwrCbsQ6.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mwrCbsQ6.setStatus("current")
_MwrCbsQ7_Type = Integer32
_MwrCbsQ7_Object = MibTableColumn
mwrCbsQ7 = _MwrCbsQ7_Object(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 9, 1, 1, 8, 1, 8),
    _MwrCbsQ7_Type()
)
mwrCbsQ7.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mwrCbsQ7.setStatus("current")
_MwrCbsQ8_Type = Integer32
_MwrCbsQ8_Object = MibTableColumn
mwrCbsQ8 = _MwrCbsQ8_Object(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 9, 1, 1, 8, 1, 9),
    _MwrCbsQ8_Type()
)
mwrCbsQ8.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mwrCbsQ8.setStatus("current")
_MwrCbsQRowStatus_Type = RowStatus
_MwrCbsQRowStatus_Object = MibTableColumn
mwrCbsQRowStatus = _MwrCbsQRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 9, 1, 1, 8, 1, 10),
    _MwrCbsQRowStatus_Type()
)
mwrCbsQRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mwrCbsQRowStatus.setStatus("current")
_MwrWeightQTable_Object = MibTable
mwrWeightQTable = _MwrWeightQTable_Object(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 9, 1, 1, 9)
)
if mibBuilder.loadTexts:
    mwrWeightQTable.setStatus("current")
_MwrWeightQEntry_Object = MibTableRow
mwrWeightQEntry = _MwrWeightQEntry_Object(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 9, 1, 1, 9, 1)
)
mwrWeightQEntry.setIndexNames(
    (0, "MWR-ETHERNET-MIB", "mwrWeightQIndex"),
)
if mibBuilder.loadTexts:
    mwrWeightQEntry.setStatus("current")
_MwrWeightQIndex_Type = QueueType
_MwrWeightQIndex_Object = MibTableColumn
mwrWeightQIndex = _MwrWeightQIndex_Object(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 9, 1, 1, 9, 1, 1),
    _MwrWeightQIndex_Type()
)
mwrWeightQIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mwrWeightQIndex.setStatus("current")
_MwrWeightQ1_Type = Integer32
_MwrWeightQ1_Object = MibTableColumn
mwrWeightQ1 = _MwrWeightQ1_Object(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 9, 1, 1, 9, 1, 2),
    _MwrWeightQ1_Type()
)
mwrWeightQ1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mwrWeightQ1.setStatus("current")
_MwrWeightQ2_Type = Integer32
_MwrWeightQ2_Object = MibTableColumn
mwrWeightQ2 = _MwrWeightQ2_Object(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 9, 1, 1, 9, 1, 3),
    _MwrWeightQ2_Type()
)
mwrWeightQ2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mwrWeightQ2.setStatus("current")
_MwrWeightQ3_Type = Integer32
_MwrWeightQ3_Object = MibTableColumn
mwrWeightQ3 = _MwrWeightQ3_Object(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 9, 1, 1, 9, 1, 4),
    _MwrWeightQ3_Type()
)
mwrWeightQ3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mwrWeightQ3.setStatus("current")
_MwrWeightQ4_Type = Integer32
_MwrWeightQ4_Object = MibTableColumn
mwrWeightQ4 = _MwrWeightQ4_Object(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 9, 1, 1, 9, 1, 5),
    _MwrWeightQ4_Type()
)
mwrWeightQ4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mwrWeightQ4.setStatus("current")
_MwrWeightQ5_Type = Integer32
_MwrWeightQ5_Object = MibTableColumn
mwrWeightQ5 = _MwrWeightQ5_Object(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 9, 1, 1, 9, 1, 6),
    _MwrWeightQ5_Type()
)
mwrWeightQ5.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mwrWeightQ5.setStatus("current")
_MwrWeightQ6_Type = Integer32
_MwrWeightQ6_Object = MibTableColumn
mwrWeightQ6 = _MwrWeightQ6_Object(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 9, 1, 1, 9, 1, 7),
    _MwrWeightQ6_Type()
)
mwrWeightQ6.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mwrWeightQ6.setStatus("current")
_MwrWeightQ7_Type = Integer32
_MwrWeightQ7_Object = MibTableColumn
mwrWeightQ7 = _MwrWeightQ7_Object(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 9, 1, 1, 9, 1, 8),
    _MwrWeightQ7_Type()
)
mwrWeightQ7.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mwrWeightQ7.setStatus("current")
_MwrWeightQ8_Type = Integer32
_MwrWeightQ8_Object = MibTableColumn
mwrWeightQ8 = _MwrWeightQ8_Object(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 9, 1, 1, 9, 1, 9),
    _MwrWeightQ8_Type()
)
mwrWeightQ8.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mwrWeightQ8.setStatus("current")
_MwrWeightQRowStatus_Type = RowStatus
_MwrWeightQRowStatus_Object = MibTableColumn
mwrWeightQRowStatus = _MwrWeightQRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 9, 1, 1, 9, 1, 10),
    _MwrWeightQRowStatus_Type()
)
mwrWeightQRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mwrWeightQRowStatus.setStatus("current")
_MwrQbsQTable_Object = MibTable
mwrQbsQTable = _MwrQbsQTable_Object(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 9, 1, 1, 10)
)
if mibBuilder.loadTexts:
    mwrQbsQTable.setStatus("current")
_MwrQbsQEntry_Object = MibTableRow
mwrQbsQEntry = _MwrQbsQEntry_Object(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 9, 1, 1, 10, 1)
)
mwrQbsQEntry.setIndexNames(
    (0, "MWR-ETHERNET-MIB", "mwrQbsQIndex"),
)
if mibBuilder.loadTexts:
    mwrQbsQEntry.setStatus("current")
_MwrQbsQIndex_Type = QueueType
_MwrQbsQIndex_Object = MibTableColumn
mwrQbsQIndex = _MwrQbsQIndex_Object(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 9, 1, 1, 10, 1, 1),
    _MwrQbsQIndex_Type()
)
mwrQbsQIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mwrQbsQIndex.setStatus("current")
_MwrQbsQ1_Type = Integer32
_MwrQbsQ1_Object = MibTableColumn
mwrQbsQ1 = _MwrQbsQ1_Object(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 9, 1, 1, 10, 1, 2),
    _MwrQbsQ1_Type()
)
mwrQbsQ1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mwrQbsQ1.setStatus("current")
_MwrQbsQ2_Type = Integer32
_MwrQbsQ2_Object = MibTableColumn
mwrQbsQ2 = _MwrQbsQ2_Object(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 9, 1, 1, 10, 1, 3),
    _MwrQbsQ2_Type()
)
mwrQbsQ2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mwrQbsQ2.setStatus("current")
_MwrQbsQ3_Type = Integer32
_MwrQbsQ3_Object = MibTableColumn
mwrQbsQ3 = _MwrQbsQ3_Object(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 9, 1, 1, 10, 1, 4),
    _MwrQbsQ3_Type()
)
mwrQbsQ3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mwrQbsQ3.setStatus("current")
_MwrQbsQ4_Type = Integer32
_MwrQbsQ4_Object = MibTableColumn
mwrQbsQ4 = _MwrQbsQ4_Object(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 9, 1, 1, 10, 1, 5),
    _MwrQbsQ4_Type()
)
mwrQbsQ4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mwrQbsQ4.setStatus("current")
_MwrQbsQ5_Type = Integer32
_MwrQbsQ5_Object = MibTableColumn
mwrQbsQ5 = _MwrQbsQ5_Object(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 9, 1, 1, 10, 1, 6),
    _MwrQbsQ5_Type()
)
mwrQbsQ5.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mwrQbsQ5.setStatus("current")
_MwrQbsQ6_Type = Integer32
_MwrQbsQ6_Object = MibTableColumn
mwrQbsQ6 = _MwrQbsQ6_Object(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 9, 1, 1, 10, 1, 7),
    _MwrQbsQ6_Type()
)
mwrQbsQ6.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mwrQbsQ6.setStatus("current")
_MwrQbsQ7_Type = Integer32
_MwrQbsQ7_Object = MibTableColumn
mwrQbsQ7 = _MwrQbsQ7_Object(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 9, 1, 1, 10, 1, 8),
    _MwrQbsQ7_Type()
)
mwrQbsQ7.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mwrQbsQ7.setStatus("current")
_MwrQbsQ8_Type = Integer32
_MwrQbsQ8_Object = MibTableColumn
mwrQbsQ8 = _MwrQbsQ8_Object(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 9, 1, 1, 10, 1, 9),
    _MwrQbsQ8_Type()
)
mwrQbsQ8.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mwrQbsQ8.setStatus("current")
_MwrQbsQRowStatus_Type = RowStatus
_MwrQbsQRowStatus_Object = MibTableColumn
mwrQbsQRowStatus = _MwrQbsQRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 9, 1, 1, 10, 1, 10),
    _MwrQbsQRowStatus_Type()
)
mwrQbsQRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mwrQbsQRowStatus.setStatus("current")
_MwrPolicyQTable_Object = MibTable
mwrPolicyQTable = _MwrPolicyQTable_Object(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 9, 1, 1, 11)
)
if mibBuilder.loadTexts:
    mwrPolicyQTable.setStatus("current")
_MwrPolicyQEntry_Object = MibTableRow
mwrPolicyQEntry = _MwrPolicyQEntry_Object(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 9, 1, 1, 11, 1)
)
mwrPolicyQEntry.setIndexNames(
    (0, "MWR-ETHERNET-MIB", "mwrPolicyQIndex"),
)
if mibBuilder.loadTexts:
    mwrPolicyQEntry.setStatus("current")
_MwrPolicyQIndex_Type = QueueType
_MwrPolicyQIndex_Object = MibTableColumn
mwrPolicyQIndex = _MwrPolicyQIndex_Object(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 9, 1, 1, 11, 1, 1),
    _MwrPolicyQIndex_Type()
)
mwrPolicyQIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mwrPolicyQIndex.setStatus("current")


class _MwrPolicyQ1_Type(Integer32):
    """Custom type mwrPolicyQ1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("wfq", 1),
          ("priority", 2),
          ("pf", 3))
    )


_MwrPolicyQ1_Type.__name__ = "Integer32"
_MwrPolicyQ1_Object = MibTableColumn
mwrPolicyQ1 = _MwrPolicyQ1_Object(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 9, 1, 1, 11, 1, 2),
    _MwrPolicyQ1_Type()
)
mwrPolicyQ1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mwrPolicyQ1.setStatus("current")


class _MwrPolicyQ2_Type(Integer32):
    """Custom type mwrPolicyQ2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("wfq", 1),
          ("priority", 2),
          ("pf", 3))
    )


_MwrPolicyQ2_Type.__name__ = "Integer32"
_MwrPolicyQ2_Object = MibTableColumn
mwrPolicyQ2 = _MwrPolicyQ2_Object(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 9, 1, 1, 11, 1, 3),
    _MwrPolicyQ2_Type()
)
mwrPolicyQ2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mwrPolicyQ2.setStatus("current")


class _MwrPolicyQ3_Type(Integer32):
    """Custom type mwrPolicyQ3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("wfq", 1),
          ("priority", 2),
          ("pf", 3))
    )


_MwrPolicyQ3_Type.__name__ = "Integer32"
_MwrPolicyQ3_Object = MibTableColumn
mwrPolicyQ3 = _MwrPolicyQ3_Object(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 9, 1, 1, 11, 1, 4),
    _MwrPolicyQ3_Type()
)
mwrPolicyQ3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mwrPolicyQ3.setStatus("current")


class _MwrPolicyQ4_Type(Integer32):
    """Custom type mwrPolicyQ4 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("wfq", 1),
          ("priority", 2),
          ("pf", 3))
    )


_MwrPolicyQ4_Type.__name__ = "Integer32"
_MwrPolicyQ4_Object = MibTableColumn
mwrPolicyQ4 = _MwrPolicyQ4_Object(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 9, 1, 1, 11, 1, 5),
    _MwrPolicyQ4_Type()
)
mwrPolicyQ4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mwrPolicyQ4.setStatus("current")


class _MwrPolicyQ5_Type(Integer32):
    """Custom type mwrPolicyQ5 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("wfq", 1),
          ("priority", 2),
          ("pf", 3))
    )


_MwrPolicyQ5_Type.__name__ = "Integer32"
_MwrPolicyQ5_Object = MibTableColumn
mwrPolicyQ5 = _MwrPolicyQ5_Object(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 9, 1, 1, 11, 1, 6),
    _MwrPolicyQ5_Type()
)
mwrPolicyQ5.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mwrPolicyQ5.setStatus("current")


class _MwrPolicyQ6_Type(Integer32):
    """Custom type mwrPolicyQ6 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("wfq", 1),
          ("priority", 2),
          ("pf", 3))
    )


_MwrPolicyQ6_Type.__name__ = "Integer32"
_MwrPolicyQ6_Object = MibTableColumn
mwrPolicyQ6 = _MwrPolicyQ6_Object(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 9, 1, 1, 11, 1, 7),
    _MwrPolicyQ6_Type()
)
mwrPolicyQ6.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mwrPolicyQ6.setStatus("current")


class _MwrPolicyQ7_Type(Integer32):
    """Custom type mwrPolicyQ7 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("wfq", 1),
          ("priority", 2),
          ("pf", 3))
    )


_MwrPolicyQ7_Type.__name__ = "Integer32"
_MwrPolicyQ7_Object = MibTableColumn
mwrPolicyQ7 = _MwrPolicyQ7_Object(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 9, 1, 1, 11, 1, 8),
    _MwrPolicyQ7_Type()
)
mwrPolicyQ7.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mwrPolicyQ7.setStatus("current")


class _MwrPolicyQ8_Type(Integer32):
    """Custom type mwrPolicyQ8 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("wfq", 1),
          ("priority", 2),
          ("pf", 3))
    )


_MwrPolicyQ8_Type.__name__ = "Integer32"
_MwrPolicyQ8_Object = MibTableColumn
mwrPolicyQ8 = _MwrPolicyQ8_Object(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 9, 1, 1, 11, 1, 9),
    _MwrPolicyQ8_Type()
)
mwrPolicyQ8.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mwrPolicyQ8.setStatus("current")
_MwrPolicyQRowStatus_Type = RowStatus
_MwrPolicyQRowStatus_Object = MibTableColumn
mwrPolicyQRowStatus = _MwrPolicyQRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 9, 1, 1, 11, 1, 10),
    _MwrPolicyQRowStatus_Type()
)
mwrPolicyQRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mwrPolicyQRowStatus.setStatus("current")
_MwrUserClassTable_Object = MibTable
mwrUserClassTable = _MwrUserClassTable_Object(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 9, 1, 1, 12)
)
if mibBuilder.loadTexts:
    mwrUserClassTable.setStatus("current")
_MwrUserClassEntry_Object = MibTableRow
mwrUserClassEntry = _MwrUserClassEntry_Object(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 9, 1, 1, 12, 1)
)
mwrUserClassEntry.setIndexNames(
    (0, "MWR-ETHERNET-MIB", "mwrUserClassIndex"),
)
if mibBuilder.loadTexts:
    mwrUserClassEntry.setStatus("current")
_MwrUserClassIndex_Type = ClassType
_MwrUserClassIndex_Object = MibTableColumn
mwrUserClassIndex = _MwrUserClassIndex_Object(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 9, 1, 1, 12, 1, 1),
    _MwrUserClassIndex_Type()
)
mwrUserClassIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mwrUserClassIndex.setStatus("current")
_MwrUserClassOffset_Type = Integer32
_MwrUserClassOffset_Object = MibTableColumn
mwrUserClassOffset = _MwrUserClassOffset_Object(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 9, 1, 1, 12, 1, 2),
    _MwrUserClassOffset_Type()
)
mwrUserClassOffset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mwrUserClassOffset.setStatus("current")
_MwrUserClassValue_Type = DisplayString
_MwrUserClassValue_Object = MibTableColumn
mwrUserClassValue = _MwrUserClassValue_Object(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 9, 1, 1, 12, 1, 3),
    _MwrUserClassValue_Type()
)
mwrUserClassValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mwrUserClassValue.setStatus("current")
_MwrUserClassMask_Type = DisplayString
_MwrUserClassMask_Object = MibTableColumn
mwrUserClassMask = _MwrUserClassMask_Object(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 9, 1, 1, 12, 1, 4),
    _MwrUserClassMask_Type()
)
mwrUserClassMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mwrUserClassMask.setStatus("current")
_MwrUserFlowTable_Object = MibTable
mwrUserFlowTable = _MwrUserFlowTable_Object(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 9, 1, 1, 13)
)
if mibBuilder.loadTexts:
    mwrUserFlowTable.setStatus("current")
_MwrUserFlowEntry_Object = MibTableRow
mwrUserFlowEntry = _MwrUserFlowEntry_Object(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 9, 1, 1, 13, 1)
)
mwrUserFlowEntry.setIndexNames(
    (0, "MWR-ETHERNET-MIB", "mwrUserFlowIndex"),
)
if mibBuilder.loadTexts:
    mwrUserFlowEntry.setStatus("current")
_MwrUserFlowIndex_Type = FlowType
_MwrUserFlowIndex_Object = MibTableColumn
mwrUserFlowIndex = _MwrUserFlowIndex_Object(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 9, 1, 1, 13, 1, 1),
    _MwrUserFlowIndex_Type()
)
mwrUserFlowIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mwrUserFlowIndex.setStatus("current")
_MwrUserFlowFilter_Type = DisplayString
_MwrUserFlowFilter_Object = MibTableColumn
mwrUserFlowFilter = _MwrUserFlowFilter_Object(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 9, 1, 1, 13, 1, 2),
    _MwrUserFlowFilter_Type()
)
mwrUserFlowFilter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mwrUserFlowFilter.setStatus("current")
_MwrUserFlowMappingTable_Object = MibTable
mwrUserFlowMappingTable = _MwrUserFlowMappingTable_Object(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 9, 1, 1, 14)
)
if mibBuilder.loadTexts:
    mwrUserFlowMappingTable.setStatus("current")
_MwrUserFlowMappingEntry_Object = MibTableRow
mwrUserFlowMappingEntry = _MwrUserFlowMappingEntry_Object(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 9, 1, 1, 14, 1)
)
mwrUserFlowMappingEntry.setIndexNames(
    (0, "MWR-ETHERNET-MIB", "mwrUserFlowMappingIndex"),
)
if mibBuilder.loadTexts:
    mwrUserFlowMappingEntry.setStatus("current")
_MwrUserFlowMappingIndex_Type = FlowType
_MwrUserFlowMappingIndex_Object = MibTableColumn
mwrUserFlowMappingIndex = _MwrUserFlowMappingIndex_Object(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 9, 1, 1, 14, 1, 1),
    _MwrUserFlowMappingIndex_Type()
)
mwrUserFlowMappingIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mwrUserFlowMappingIndex.setStatus("current")
_MwrUserFlowMappingState_Type = EnableType
_MwrUserFlowMappingState_Object = MibTableColumn
mwrUserFlowMappingState = _MwrUserFlowMappingState_Object(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 9, 1, 1, 14, 1, 2),
    _MwrUserFlowMappingState_Type()
)
mwrUserFlowMappingState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mwrUserFlowMappingState.setStatus("current")
_MwrUserFlowMapping1Q_Type = QueueType
_MwrUserFlowMapping1Q_Object = MibTableColumn
mwrUserFlowMapping1Q = _MwrUserFlowMapping1Q_Object(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 9, 1, 1, 14, 1, 3),
    _MwrUserFlowMapping1Q_Type()
)
mwrUserFlowMapping1Q.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mwrUserFlowMapping1Q.setStatus("current")
_MwrUserFlowMapping2Q_Type = QueueType
_MwrUserFlowMapping2Q_Object = MibTableColumn
mwrUserFlowMapping2Q = _MwrUserFlowMapping2Q_Object(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 9, 1, 1, 14, 1, 4),
    _MwrUserFlowMapping2Q_Type()
)
mwrUserFlowMapping2Q.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mwrUserFlowMapping2Q.setStatus("current")
_MwrUserFlowMapping3Q_Type = QueueType
_MwrUserFlowMapping3Q_Object = MibTableColumn
mwrUserFlowMapping3Q = _MwrUserFlowMapping3Q_Object(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 9, 1, 1, 14, 1, 5),
    _MwrUserFlowMapping3Q_Type()
)
mwrUserFlowMapping3Q.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mwrUserFlowMapping3Q.setStatus("current")
_MwrUserFlowMapping4Q_Type = QueueType
_MwrUserFlowMapping4Q_Object = MibTableColumn
mwrUserFlowMapping4Q = _MwrUserFlowMapping4Q_Object(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 9, 1, 1, 14, 1, 6),
    _MwrUserFlowMapping4Q_Type()
)
mwrUserFlowMapping4Q.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mwrUserFlowMapping4Q.setStatus("current")
_MwrUserFlowMappingRowStatus_Type = RowStatus
_MwrUserFlowMappingRowStatus_Object = MibTableColumn
mwrUserFlowMappingRowStatus = _MwrUserFlowMappingRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 9, 1, 1, 14, 1, 7),
    _MwrUserFlowMappingRowStatus_Type()
)
mwrUserFlowMappingRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mwrUserFlowMappingRowStatus.setStatus("current")
_MwrUserFlowMappingBridgeModeTable_Object = MibTable
mwrUserFlowMappingBridgeModeTable = _MwrUserFlowMappingBridgeModeTable_Object(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 9, 1, 1, 15)
)
if mibBuilder.loadTexts:
    mwrUserFlowMappingBridgeModeTable.setStatus("current")
_MwrUserFlowMappingBridgeModeEntry_Object = MibTableRow
mwrUserFlowMappingBridgeModeEntry = _MwrUserFlowMappingBridgeModeEntry_Object(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 9, 1, 1, 15, 1)
)
mwrUserFlowMappingBridgeModeEntry.setIndexNames(
    (0, "MWR-ETHERNET-MIB", "mwrUserFlowMappingBridgeModeIndex"),
)
if mibBuilder.loadTexts:
    mwrUserFlowMappingBridgeModeEntry.setStatus("current")
_MwrUserFlowMappingBridgeModeIndex_Type = FlowType
_MwrUserFlowMappingBridgeModeIndex_Object = MibTableColumn
mwrUserFlowMappingBridgeModeIndex = _MwrUserFlowMappingBridgeModeIndex_Object(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 9, 1, 1, 15, 1, 1),
    _MwrUserFlowMappingBridgeModeIndex_Type()
)
mwrUserFlowMappingBridgeModeIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mwrUserFlowMappingBridgeModeIndex.setStatus("current")
_MwrUserFlowMappingBridgeModeState_Type = EnableType
_MwrUserFlowMappingBridgeModeState_Object = MibTableColumn
mwrUserFlowMappingBridgeModeState = _MwrUserFlowMappingBridgeModeState_Object(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 9, 1, 1, 15, 1, 2),
    _MwrUserFlowMappingBridgeModeState_Type()
)
mwrUserFlowMappingBridgeModeState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mwrUserFlowMappingBridgeModeState.setStatus("current")
_MwrUserFlowMappingBridgeModeQ_Type = QueueType
_MwrUserFlowMappingBridgeModeQ_Object = MibTableColumn
mwrUserFlowMappingBridgeModeQ = _MwrUserFlowMappingBridgeModeQ_Object(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 9, 1, 1, 15, 1, 3),
    _MwrUserFlowMappingBridgeModeQ_Type()
)
mwrUserFlowMappingBridgeModeQ.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mwrUserFlowMappingBridgeModeQ.setStatus("current")
_MwrUserFlowMappingBridgeModeRowStatus_Type = RowStatus
_MwrUserFlowMappingBridgeModeRowStatus_Object = MibTableColumn
mwrUserFlowMappingBridgeModeRowStatus = _MwrUserFlowMappingBridgeModeRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 9, 1, 1, 15, 1, 4),
    _MwrUserFlowMappingBridgeModeRowStatus_Type()
)
mwrUserFlowMappingBridgeModeRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mwrUserFlowMappingBridgeModeRowStatus.setStatus("current")
_MwrEthThresholdAlarm_ObjectIdentity = ObjectIdentity
mwrEthThresholdAlarm = _MwrEthThresholdAlarm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 9, 1, 2)
)
_MwrPortThresholdAlarmTable_Object = MibTable
mwrPortThresholdAlarmTable = _MwrPortThresholdAlarmTable_Object(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 9, 1, 2, 1)
)
if mibBuilder.loadTexts:
    mwrPortThresholdAlarmTable.setStatus("current")
_MwrPortThresholdAlarmEntry_Object = MibTableRow
mwrPortThresholdAlarmEntry = _MwrPortThresholdAlarmEntry_Object(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 9, 1, 2, 1, 1)
)
mwrPortThresholdAlarmEntry.setIndexNames(
    (0, "MWR-ETHERNET-MIB", "mwrPortThresholdAlarmIndex"),
)
if mibBuilder.loadTexts:
    mwrPortThresholdAlarmEntry.setStatus("current")
_MwrPortThresholdAlarmIndex_Type = Integer32
_MwrPortThresholdAlarmIndex_Object = MibTableColumn
mwrPortThresholdAlarmIndex = _MwrPortThresholdAlarmIndex_Object(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 9, 1, 2, 1, 1, 1),
    _MwrPortThresholdAlarmIndex_Type()
)
mwrPortThresholdAlarmIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mwrPortThresholdAlarmIndex.setStatus("current")


class _MwrDroppedPktsThresholdParams_Type(DisplayString):
    """Custom type mwrDroppedPktsThresholdParams based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 24),
    )


_MwrDroppedPktsThresholdParams_Type.__name__ = "DisplayString"
_MwrDroppedPktsThresholdParams_Object = MibTableColumn
mwrDroppedPktsThresholdParams = _MwrDroppedPktsThresholdParams_Object(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 9, 1, 2, 1, 1, 2),
    _MwrDroppedPktsThresholdParams_Type()
)
mwrDroppedPktsThresholdParams.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mwrDroppedPktsThresholdParams.setStatus("current")
_MwrOutBWUtilizationThresholdParams_Type = DisplayString
_MwrOutBWUtilizationThresholdParams_Object = MibTableColumn
mwrOutBWUtilizationThresholdParams = _MwrOutBWUtilizationThresholdParams_Object(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 9, 1, 2, 1, 1, 3),
    _MwrOutBWUtilizationThresholdParams_Type()
)
mwrOutBWUtilizationThresholdParams.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mwrOutBWUtilizationThresholdParams.setStatus("current")
_MwrThroughputThresholdParams_Type = DisplayString
_MwrThroughputThresholdParams_Object = MibTableColumn
mwrThroughputThresholdParams = _MwrThroughputThresholdParams_Object(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 9, 1, 2, 1, 1, 4),
    _MwrThroughputThresholdParams_Type()
)
mwrThroughputThresholdParams.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mwrThroughputThresholdParams.setStatus("current")
_MwrRadioQThresholdAlarmTable_Object = MibTable
mwrRadioQThresholdAlarmTable = _MwrRadioQThresholdAlarmTable_Object(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 9, 1, 2, 2)
)
if mibBuilder.loadTexts:
    mwrRadioQThresholdAlarmTable.setStatus("current")
_MwrRadioQThresholdAlarmEntry_Object = MibTableRow
mwrRadioQThresholdAlarmEntry = _MwrRadioQThresholdAlarmEntry_Object(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 9, 1, 2, 2, 1)
)
mwrRadioQThresholdAlarmEntry.setIndexNames(
    (0, "MWR-ETHERNET-MIB", "mwrRadioQThresholdAlarmIndex"),
)
if mibBuilder.loadTexts:
    mwrRadioQThresholdAlarmEntry.setStatus("current")
_MwrRadioQThresholdAlarmIndex_Type = QueueType
_MwrRadioQThresholdAlarmIndex_Object = MibTableColumn
mwrRadioQThresholdAlarmIndex = _MwrRadioQThresholdAlarmIndex_Object(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 9, 1, 2, 2, 1, 1),
    _MwrRadioQThresholdAlarmIndex_Type()
)
mwrRadioQThresholdAlarmIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwrRadioQThresholdAlarmIndex.setStatus("current")
_MwrRadioQDepthThresholdParams_Type = DisplayString
_MwrRadioQDepthThresholdParams_Object = MibTableColumn
mwrRadioQDepthThresholdParams = _MwrRadioQDepthThresholdParams_Object(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 9, 1, 2, 2, 1, 2),
    _MwrRadioQDepthThresholdParams_Type()
)
mwrRadioQDepthThresholdParams.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mwrRadioQDepthThresholdParams.setStatus("current")
_MwrRadioQDroppedPktsThresholdParams_Type = DisplayString
_MwrRadioQDroppedPktsThresholdParams_Object = MibTableColumn
mwrRadioQDroppedPktsThresholdParams = _MwrRadioQDroppedPktsThresholdParams_Object(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 9, 1, 2, 2, 1, 3),
    _MwrRadioQDroppedPktsThresholdParams_Type()
)
mwrRadioQDroppedPktsThresholdParams.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mwrRadioQDroppedPktsThresholdParams.setStatus("current")
_MwrEthernetStatus_ObjectIdentity = ObjectIdentity
mwrEthernetStatus = _MwrEthernetStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 9, 2)
)
_MwrEthernetPerformance_ObjectIdentity = ObjectIdentity
mwrEthernetPerformance = _MwrEthernetPerformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 9, 3)
)
_MwrEnetPerfPortStatsTable_Object = MibTable
mwrEnetPerfPortStatsTable = _MwrEnetPerfPortStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 9, 3, 1)
)
if mibBuilder.loadTexts:
    mwrEnetPerfPortStatsTable.setStatus("current")
_MwrEnetPerfPortStatsEntry_Object = MibTableRow
mwrEnetPerfPortStatsEntry = _MwrEnetPerfPortStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 9, 3, 1, 1)
)
mwrEnetPerfPortStatsEntry.setIndexNames(
    (0, "MWR-ETHERNET-MIB", "mwrEnetPortStatsIndex"),
)
if mibBuilder.loadTexts:
    mwrEnetPerfPortStatsEntry.setStatus("current")


class _MwrEnetPortStatsIndex_Type(Integer32):
    """Custom type mwrEnetPortStatsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("gi01", 1),
          ("gi02", 2),
          ("gi03", 3),
          ("gi04", 4),
          ("radio", 5))
    )


_MwrEnetPortStatsIndex_Type.__name__ = "Integer32"
_MwrEnetPortStatsIndex_Object = MibTableColumn
mwrEnetPortStatsIndex = _MwrEnetPortStatsIndex_Object(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 9, 3, 1, 1, 1),
    _MwrEnetPortStatsIndex_Type()
)
mwrEnetPortStatsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwrEnetPortStatsIndex.setStatus("current")
_MwrPortStatsInOctet_Type = Counter64
_MwrPortStatsInOctet_Object = MibTableColumn
mwrPortStatsInOctet = _MwrPortStatsInOctet_Object(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 9, 3, 1, 1, 2),
    _MwrPortStatsInOctet_Type()
)
mwrPortStatsInOctet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwrPortStatsInOctet.setStatus("current")
_MwrPortStatsInGoodPkts_Type = Counter64
_MwrPortStatsInGoodPkts_Object = MibTableColumn
mwrPortStatsInGoodPkts = _MwrPortStatsInGoodPkts_Object(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 9, 3, 1, 1, 3),
    _MwrPortStatsInGoodPkts_Type()
)
mwrPortStatsInGoodPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwrPortStatsInGoodPkts.setStatus("current")
_MwrPortStatsInErrPkts_Type = Counter64
_MwrPortStatsInErrPkts_Object = MibTableColumn
mwrPortStatsInErrPkts = _MwrPortStatsInErrPkts_Object(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 9, 3, 1, 1, 4),
    _MwrPortStatsInErrPkts_Type()
)
mwrPortStatsInErrPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwrPortStatsInErrPkts.setStatus("current")
_MwrPortStatsInDiscardPkts_Type = Counter64
_MwrPortStatsInDiscardPkts_Object = MibTableColumn
mwrPortStatsInDiscardPkts = _MwrPortStatsInDiscardPkts_Object(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 9, 3, 1, 1, 5),
    _MwrPortStatsInDiscardPkts_Type()
)
mwrPortStatsInDiscardPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwrPortStatsInDiscardPkts.setStatus("current")
_MwrPortStatsOutOctets_Type = Counter64
_MwrPortStatsOutOctets_Object = MibTableColumn
mwrPortStatsOutOctets = _MwrPortStatsOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 9, 3, 1, 1, 6),
    _MwrPortStatsOutOctets_Type()
)
mwrPortStatsOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwrPortStatsOutOctets.setStatus("current")
_MwrPortStatsOutGoodPkts_Type = Counter64
_MwrPortStatsOutGoodPkts_Object = MibTableColumn
mwrPortStatsOutGoodPkts = _MwrPortStatsOutGoodPkts_Object(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 9, 3, 1, 1, 7),
    _MwrPortStatsOutGoodPkts_Type()
)
mwrPortStatsOutGoodPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwrPortStatsOutGoodPkts.setStatus("current")
_MwrPortStatsOutErrPkts_Type = Counter64
_MwrPortStatsOutErrPkts_Object = MibTableColumn
mwrPortStatsOutErrPkts = _MwrPortStatsOutErrPkts_Object(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 9, 3, 1, 1, 8),
    _MwrPortStatsOutErrPkts_Type()
)
mwrPortStatsOutErrPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwrPortStatsOutErrPkts.setStatus("current")
_MwrPortStatsOutDiscardPkts_Type = Counter64
_MwrPortStatsOutDiscardPkts_Object = MibTableColumn
mwrPortStatsOutDiscardPkts = _MwrPortStatsOutDiscardPkts_Object(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 9, 3, 1, 1, 9),
    _MwrPortStatsOutDiscardPkts_Type()
)
mwrPortStatsOutDiscardPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwrPortStatsOutDiscardPkts.setStatus("current")
_MwrPortStatsOutBwUtilization_Type = Integer32
_MwrPortStatsOutBwUtilization_Object = MibTableColumn
mwrPortStatsOutBwUtilization = _MwrPortStatsOutBwUtilization_Object(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 9, 3, 1, 1, 10),
    _MwrPortStatsOutBwUtilization_Type()
)
mwrPortStatsOutBwUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwrPortStatsOutBwUtilization.setStatus("current")
if mibBuilder.loadTexts:
    mwrPortStatsOutBwUtilization.setUnits("%")
_MwrPortStatsInBwUtilization_Type = Integer32
_MwrPortStatsInBwUtilization_Object = MibTableColumn
mwrPortStatsInBwUtilization = _MwrPortStatsInBwUtilization_Object(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 9, 3, 1, 1, 11),
    _MwrPortStatsInBwUtilization_Type()
)
mwrPortStatsInBwUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwrPortStatsInBwUtilization.setStatus("current")
if mibBuilder.loadTexts:
    mwrPortStatsInBwUtilization.setUnits("%")
_MwrPortStatsInDataRate_Type = Integer32
_MwrPortStatsInDataRate_Object = MibTableColumn
mwrPortStatsInDataRate = _MwrPortStatsInDataRate_Object(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 9, 3, 1, 1, 12),
    _MwrPortStatsInDataRate_Type()
)
mwrPortStatsInDataRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwrPortStatsInDataRate.setStatus("current")
if mibBuilder.loadTexts:
    mwrPortStatsInDataRate.setUnits("Mbps")
_MwrPortStatsThroughput_Type = Integer32
_MwrPortStatsThroughput_Object = MibTableColumn
mwrPortStatsThroughput = _MwrPortStatsThroughput_Object(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 9, 3, 1, 1, 13),
    _MwrPortStatsThroughput_Type()
)
mwrPortStatsThroughput.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwrPortStatsThroughput.setStatus("current")
if mibBuilder.loadTexts:
    mwrPortStatsThroughput.setUnits("Mbps")
_MwrEnetPerfPortStats32BitTable_Object = MibTable
mwrEnetPerfPortStats32BitTable = _MwrEnetPerfPortStats32BitTable_Object(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 9, 3, 2)
)
if mibBuilder.loadTexts:
    mwrEnetPerfPortStats32BitTable.setStatus("current")
_MwrEnetPerfPortStats32BitEntry_Object = MibTableRow
mwrEnetPerfPortStats32BitEntry = _MwrEnetPerfPortStats32BitEntry_Object(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 9, 3, 2, 1)
)
mwrEnetPerfPortStats32BitEntry.setIndexNames(
    (0, "MWR-ETHERNET-MIB", "mwrPortStats32BitIndex"),
)
if mibBuilder.loadTexts:
    mwrEnetPerfPortStats32BitEntry.setStatus("current")


class _MwrPortStats32BitIndex_Type(Integer32):
    """Custom type mwrPortStats32BitIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("gi01", 1),
          ("gi02", 2),
          ("gi03", 3),
          ("gi04", 4),
          ("radio", 5))
    )


_MwrPortStats32BitIndex_Type.__name__ = "Integer32"
_MwrPortStats32BitIndex_Object = MibTableColumn
mwrPortStats32BitIndex = _MwrPortStats32BitIndex_Object(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 9, 3, 2, 1, 1),
    _MwrPortStats32BitIndex_Type()
)
mwrPortStats32BitIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mwrPortStats32BitIndex.setStatus("current")
_MwrPortStatsInOctet32Bit_Type = Counter32
_MwrPortStatsInOctet32Bit_Object = MibTableColumn
mwrPortStatsInOctet32Bit = _MwrPortStatsInOctet32Bit_Object(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 9, 3, 2, 1, 2),
    _MwrPortStatsInOctet32Bit_Type()
)
mwrPortStatsInOctet32Bit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwrPortStatsInOctet32Bit.setStatus("current")
_MwrPortStatsInGoodPkts32Bit_Type = Counter32
_MwrPortStatsInGoodPkts32Bit_Object = MibTableColumn
mwrPortStatsInGoodPkts32Bit = _MwrPortStatsInGoodPkts32Bit_Object(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 9, 3, 2, 1, 3),
    _MwrPortStatsInGoodPkts32Bit_Type()
)
mwrPortStatsInGoodPkts32Bit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwrPortStatsInGoodPkts32Bit.setStatus("current")
_MwrPortStatsInErrPkts32Bit_Type = Counter32
_MwrPortStatsInErrPkts32Bit_Object = MibTableColumn
mwrPortStatsInErrPkts32Bit = _MwrPortStatsInErrPkts32Bit_Object(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 9, 3, 2, 1, 4),
    _MwrPortStatsInErrPkts32Bit_Type()
)
mwrPortStatsInErrPkts32Bit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwrPortStatsInErrPkts32Bit.setStatus("current")
_MwrPortStatsInDiscardPkts32Bit_Type = Counter32
_MwrPortStatsInDiscardPkts32Bit_Object = MibTableColumn
mwrPortStatsInDiscardPkts32Bit = _MwrPortStatsInDiscardPkts32Bit_Object(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 9, 3, 2, 1, 5),
    _MwrPortStatsInDiscardPkts32Bit_Type()
)
mwrPortStatsInDiscardPkts32Bit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwrPortStatsInDiscardPkts32Bit.setStatus("current")
_MwrPortStatsOutOctets32Bit_Type = Counter32
_MwrPortStatsOutOctets32Bit_Object = MibTableColumn
mwrPortStatsOutOctets32Bit = _MwrPortStatsOutOctets32Bit_Object(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 9, 3, 2, 1, 6),
    _MwrPortStatsOutOctets32Bit_Type()
)
mwrPortStatsOutOctets32Bit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwrPortStatsOutOctets32Bit.setStatus("current")
_MwrPortStatsOutGoodPkts32Bit_Type = Counter32
_MwrPortStatsOutGoodPkts32Bit_Object = MibTableColumn
mwrPortStatsOutGoodPkts32Bit = _MwrPortStatsOutGoodPkts32Bit_Object(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 9, 3, 2, 1, 7),
    _MwrPortStatsOutGoodPkts32Bit_Type()
)
mwrPortStatsOutGoodPkts32Bit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwrPortStatsOutGoodPkts32Bit.setStatus("current")
_MwrPortStatsOutErrPkts32Bit_Type = Counter32
_MwrPortStatsOutErrPkts32Bit_Object = MibTableColumn
mwrPortStatsOutErrPkts32Bit = _MwrPortStatsOutErrPkts32Bit_Object(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 9, 3, 2, 1, 8),
    _MwrPortStatsOutErrPkts32Bit_Type()
)
mwrPortStatsOutErrPkts32Bit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwrPortStatsOutErrPkts32Bit.setStatus("current")
_MwrPortStatsOutDiscardPkts32Bit_Type = Counter32
_MwrPortStatsOutDiscardPkts32Bit_Object = MibTableColumn
mwrPortStatsOutDiscardPkts32Bit = _MwrPortStatsOutDiscardPkts32Bit_Object(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 9, 3, 2, 1, 9),
    _MwrPortStatsOutDiscardPkts32Bit_Type()
)
mwrPortStatsOutDiscardPkts32Bit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwrPortStatsOutDiscardPkts32Bit.setStatus("current")
_MwrEnetPerfRadioQStatsTable_Object = MibTable
mwrEnetPerfRadioQStatsTable = _MwrEnetPerfRadioQStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 9, 3, 3)
)
if mibBuilder.loadTexts:
    mwrEnetPerfRadioQStatsTable.setStatus("current")
_MwrEnetPerfRadioQStatsEntry_Object = MibTableRow
mwrEnetPerfRadioQStatsEntry = _MwrEnetPerfRadioQStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 9, 3, 3, 1)
)
mwrEnetPerfRadioQStatsEntry.setIndexNames(
    (0, "MWR-ETHERNET-MIB", "mwrRadioQStatsIndex"),
)
if mibBuilder.loadTexts:
    mwrEnetPerfRadioQStatsEntry.setStatus("current")
_MwrRadioQStatsIndex_Type = QueueType
_MwrRadioQStatsIndex_Object = MibTableColumn
mwrRadioQStatsIndex = _MwrRadioQStatsIndex_Object(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 9, 3, 3, 1, 1),
    _MwrRadioQStatsIndex_Type()
)
mwrRadioQStatsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mwrRadioQStatsIndex.setStatus("current")
_MwrRadioQStatsInGoodPkts_Type = Counter64
_MwrRadioQStatsInGoodPkts_Object = MibTableColumn
mwrRadioQStatsInGoodPkts = _MwrRadioQStatsInGoodPkts_Object(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 9, 3, 3, 1, 2),
    _MwrRadioQStatsInGoodPkts_Type()
)
mwrRadioQStatsInGoodPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwrRadioQStatsInGoodPkts.setStatus("current")
_MwrRadioQStatsInDiscardPkts_Type = Counter64
_MwrRadioQStatsInDiscardPkts_Object = MibTableColumn
mwrRadioQStatsInDiscardPkts = _MwrRadioQStatsInDiscardPkts_Object(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 9, 3, 3, 1, 3),
    _MwrRadioQStatsInDiscardPkts_Type()
)
mwrRadioQStatsInDiscardPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwrRadioQStatsInDiscardPkts.setStatus("current")
_MwrRadioQStatsOutBwUtilization_Type = Integer32
_MwrRadioQStatsOutBwUtilization_Object = MibTableColumn
mwrRadioQStatsOutBwUtilization = _MwrRadioQStatsOutBwUtilization_Object(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 9, 3, 3, 1, 4),
    _MwrRadioQStatsOutBwUtilization_Type()
)
mwrRadioQStatsOutBwUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwrRadioQStatsOutBwUtilization.setStatus("current")
if mibBuilder.loadTexts:
    mwrRadioQStatsOutBwUtilization.setUnits("%")
_MwrRadioQStatsInDataRate_Type = Integer32
_MwrRadioQStatsInDataRate_Object = MibTableColumn
mwrRadioQStatsInDataRate = _MwrRadioQStatsInDataRate_Object(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 9, 3, 3, 1, 5),
    _MwrRadioQStatsInDataRate_Type()
)
mwrRadioQStatsInDataRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwrRadioQStatsInDataRate.setStatus("current")
if mibBuilder.loadTexts:
    mwrRadioQStatsInDataRate.setUnits("Mbps")
_MwrRadioQStatsThroughput_Type = Integer32
_MwrRadioQStatsThroughput_Object = MibTableColumn
mwrRadioQStatsThroughput = _MwrRadioQStatsThroughput_Object(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 9, 3, 3, 1, 6),
    _MwrRadioQStatsThroughput_Type()
)
mwrRadioQStatsThroughput.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwrRadioQStatsThroughput.setStatus("current")
if mibBuilder.loadTexts:
    mwrRadioQStatsThroughput.setUnits("Mbps")
_MwrEnetPerfRadioQStats32BitTable_Object = MibTable
mwrEnetPerfRadioQStats32BitTable = _MwrEnetPerfRadioQStats32BitTable_Object(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 9, 3, 4)
)
if mibBuilder.loadTexts:
    mwrEnetPerfRadioQStats32BitTable.setStatus("current")
_MwrEnetPerfRadioQStats32BitEntry_Object = MibTableRow
mwrEnetPerfRadioQStats32BitEntry = _MwrEnetPerfRadioQStats32BitEntry_Object(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 9, 3, 4, 1)
)
mwrEnetPerfRadioQStats32BitEntry.setIndexNames(
    (0, "MWR-ETHERNET-MIB", "mwrRadioQStats32BitIndex"),
)
if mibBuilder.loadTexts:
    mwrEnetPerfRadioQStats32BitEntry.setStatus("current")
_MwrRadioQStats32BitIndex_Type = QueueType
_MwrRadioQStats32BitIndex_Object = MibTableColumn
mwrRadioQStats32BitIndex = _MwrRadioQStats32BitIndex_Object(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 9, 3, 4, 1, 1),
    _MwrRadioQStats32BitIndex_Type()
)
mwrRadioQStats32BitIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mwrRadioQStats32BitIndex.setStatus("current")
_MwrRadioQStatsInGoodPkts32Bit_Type = Counter32
_MwrRadioQStatsInGoodPkts32Bit_Object = MibTableColumn
mwrRadioQStatsInGoodPkts32Bit = _MwrRadioQStatsInGoodPkts32Bit_Object(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 9, 3, 4, 1, 2),
    _MwrRadioQStatsInGoodPkts32Bit_Type()
)
mwrRadioQStatsInGoodPkts32Bit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwrRadioQStatsInGoodPkts32Bit.setStatus("current")
_MwrRadioQStatsDiscardPkts32Bit_Type = Counter32
_MwrRadioQStatsDiscardPkts32Bit_Object = MibTableColumn
mwrRadioQStatsDiscardPkts32Bit = _MwrRadioQStatsDiscardPkts32Bit_Object(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 9, 3, 4, 1, 3),
    _MwrRadioQStatsDiscardPkts32Bit_Type()
)
mwrRadioQStatsDiscardPkts32Bit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwrRadioQStatsDiscardPkts32Bit.setStatus("current")
_MwrEthernetNotifications_ObjectIdentity = ObjectIdentity
mwrEthernetNotifications = _MwrEthernetNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 9, 4)
)
_MwrAcm_ObjectIdentity = ObjectIdentity
mwrAcm = _MwrAcm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 10)
)
_MwrAcmConfigurations_ObjectIdentity = ObjectIdentity
mwrAcmConfigurations = _MwrAcmConfigurations_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 10, 1)
)
_MwrAcmManualMode_Type = EnableType
_MwrAcmManualMode_Object = MibScalar
mwrAcmManualMode = _MwrAcmManualMode_Object(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 10, 1, 1),
    _MwrAcmManualMode_Type()
)
mwrAcmManualMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mwrAcmManualMode.setStatus("current")


class _MwrAcmState_Type(EnableType):
    """Custom type mwrAcmState based on EnableType"""
    defaultValue = 0


_MwrAcmState_Type.__name__ = "EnableType"
_MwrAcmState_Object = MibScalar
mwrAcmState = _MwrAcmState_Object(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 10, 1, 2),
    _MwrAcmState_Type()
)
mwrAcmState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mwrAcmState.setStatus("current")
_MwrAcmWaitToRestore_Type = Integer32
_MwrAcmWaitToRestore_Object = MibScalar
mwrAcmWaitToRestore = _MwrAcmWaitToRestore_Object(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 10, 1, 3),
    _MwrAcmWaitToRestore_Type()
)
mwrAcmWaitToRestore.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mwrAcmWaitToRestore.setStatus("current")
_MwrAcmModeTable_Object = MibTable
mwrAcmModeTable = _MwrAcmModeTable_Object(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 10, 1, 4)
)
if mibBuilder.loadTexts:
    mwrAcmModeTable.setStatus("current")
_MwrAcmModeEntry_Object = MibTableRow
mwrAcmModeEntry = _MwrAcmModeEntry_Object(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 10, 1, 4, 1)
)
mwrAcmModeEntry.setIndexNames(
    (0, "MWR-ETHERNET-MIB", "mwrAcmModeIndex"),
)
if mibBuilder.loadTexts:
    mwrAcmModeEntry.setStatus("current")
_MwrAcmModeIndex_Type = Integer32
_MwrAcmModeIndex_Object = MibTableColumn
mwrAcmModeIndex = _MwrAcmModeIndex_Object(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 10, 1, 4, 1, 1),
    _MwrAcmModeIndex_Type()
)
mwrAcmModeIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mwrAcmModeIndex.setStatus("current")
_MwrAcmTxProfileName_Type = DisplayString
_MwrAcmTxProfileName_Object = MibTableColumn
mwrAcmTxProfileName = _MwrAcmTxProfileName_Object(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 10, 1, 4, 1, 2),
    _MwrAcmTxProfileName_Type()
)
mwrAcmTxProfileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwrAcmTxProfileName.setStatus("current")


class _MwrAcmTxProfileRange_Type(Integer32):
    """Custom type mwrAcmTxProfileRange based on Integer32"""
    defaultValue = 1

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
        *(("notAllowed", 1),
          ("allowed", 2),
          ("max", 3),
          ("min", 4))
    )


_MwrAcmTxProfileRange_Type.__name__ = "Integer32"
_MwrAcmTxProfileRange_Object = MibTableColumn
mwrAcmTxProfileRange = _MwrAcmTxProfileRange_Object(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 10, 1, 4, 1, 3),
    _MwrAcmTxProfileRange_Type()
)
mwrAcmTxProfileRange.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mwrAcmTxProfileRange.setStatus("current")
_MwrAcmStatus_ObjectIdentity = ObjectIdentity
mwrAcmStatus = _MwrAcmStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 10, 2)
)
_MwrAcmStatusTable_Object = MibTable
mwrAcmStatusTable = _MwrAcmStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 10, 2, 1)
)
if mibBuilder.loadTexts:
    mwrAcmStatusTable.setStatus("current")
_MwrAcmStatusEntry_Object = MibTableRow
mwrAcmStatusEntry = _MwrAcmStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 10, 2, 1, 1)
)
mwrAcmStatusEntry.setIndexNames(
    (0, "MWR-ETHERNET-MIB", "mwrAcmStatusIndex"),
)
if mibBuilder.loadTexts:
    mwrAcmStatusEntry.setStatus("current")
_MwrAcmStatusIndex_Type = RadioInstanceType
_MwrAcmStatusIndex_Object = MibTableColumn
mwrAcmStatusIndex = _MwrAcmStatusIndex_Object(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 10, 2, 1, 1, 1),
    _MwrAcmStatusIndex_Type()
)
mwrAcmStatusIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mwrAcmStatusIndex.setStatus("current")


class _MwrAcmActualTxProfile_Type(DisplayString):
    """Custom type mwrAcmActualTxProfile based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 24),
    )


_MwrAcmActualTxProfile_Type.__name__ = "DisplayString"
_MwrAcmActualTxProfile_Object = MibTableColumn
mwrAcmActualTxProfile = _MwrAcmActualTxProfile_Object(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 10, 2, 1, 1, 2),
    _MwrAcmActualTxProfile_Type()
)
mwrAcmActualTxProfile.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwrAcmActualTxProfile.setStatus("current")
_MwrAcmDiagnostics_ObjectIdentity = ObjectIdentity
mwrAcmDiagnostics = _MwrAcmDiagnostics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 10, 3)
)
_MwrAcmDiagTable_Object = MibTable
mwrAcmDiagTable = _MwrAcmDiagTable_Object(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 10, 3, 1)
)
if mibBuilder.loadTexts:
    mwrAcmDiagTable.setStatus("current")
_MwrAcmDiagEntry_Object = MibTableRow
mwrAcmDiagEntry = _MwrAcmDiagEntry_Object(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 10, 3, 1, 1)
)
mwrAcmDiagEntry.setIndexNames(
    (0, "MWR-ETHERNET-MIB", "mwrAcmDiagIndex"),
)
if mibBuilder.loadTexts:
    mwrAcmDiagEntry.setStatus("current")
_MwrAcmDiagIndex_Type = RadioInstanceType
_MwrAcmDiagIndex_Object = MibTableColumn
mwrAcmDiagIndex = _MwrAcmDiagIndex_Object(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 10, 3, 1, 1, 1),
    _MwrAcmDiagIndex_Type()
)
mwrAcmDiagIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mwrAcmDiagIndex.setStatus("current")


class _MwrAcmDiagnose_Type(Integer32):
    """Custom type mwrAcmDiagnose based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("up", 1),
          ("down", 2))
    )


_MwrAcmDiagnose_Type.__name__ = "Integer32"
_MwrAcmDiagnose_Object = MibTableColumn
mwrAcmDiagnose = _MwrAcmDiagnose_Object(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 10, 3, 1, 1, 2),
    _MwrAcmDiagnose_Type()
)
mwrAcmDiagnose.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mwrAcmDiagnose.setStatus("current")
_MwrAcmDiagnosticResult_Type = DisplayString
_MwrAcmDiagnosticResult_Object = MibTableColumn
mwrAcmDiagnosticResult = _MwrAcmDiagnosticResult_Object(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 10, 3, 1, 1, 3),
    _MwrAcmDiagnosticResult_Type()
)
mwrAcmDiagnosticResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwrAcmDiagnosticResult.setStatus("current")
_MwrAcmNotifications_ObjectIdentity = ObjectIdentity
mwrAcmNotifications = _MwrAcmNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 10, 4)
)
_MwrAtpc_ObjectIdentity = ObjectIdentity
mwrAtpc = _MwrAtpc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 11)
)
_MwrAtpcConfigurations_ObjectIdentity = ObjectIdentity
mwrAtpcConfigurations = _MwrAtpcConfigurations_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 11, 1)
)
_MwrAtpcConfigurationsTable_Object = MibTable
mwrAtpcConfigurationsTable = _MwrAtpcConfigurationsTable_Object(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 11, 1, 1)
)
if mibBuilder.loadTexts:
    mwrAtpcConfigurationsTable.setStatus("current")
_MwrAtpcConfigurationsEntry_Object = MibTableRow
mwrAtpcConfigurationsEntry = _MwrAtpcConfigurationsEntry_Object(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 11, 1, 1, 1)
)
mwrAtpcConfigurationsEntry.setIndexNames(
    (0, "MWR-ETHERNET-MIB", "mwrAtpcConfigIndex"),
)
if mibBuilder.loadTexts:
    mwrAtpcConfigurationsEntry.setStatus("current")
_MwrAtpcConfigIndex_Type = RadioInstanceType
_MwrAtpcConfigIndex_Object = MibTableColumn
mwrAtpcConfigIndex = _MwrAtpcConfigIndex_Object(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 11, 1, 1, 1, 1),
    _MwrAtpcConfigIndex_Type()
)
mwrAtpcConfigIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mwrAtpcConfigIndex.setStatus("current")


class _MwrAtpcState_Type(EnableType):
    """Custom type mwrAtpcState based on EnableType"""
    defaultValue = 0


_MwrAtpcState_Type.__name__ = "EnableType"
_MwrAtpcState_Object = MibTableColumn
mwrAtpcState = _MwrAtpcState_Object(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 11, 1, 1, 1, 2),
    _MwrAtpcState_Type()
)
mwrAtpcState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mwrAtpcState.setStatus("current")


class _MwrAtpcCoordinatedPower_Type(Integer32):
    """Custom type mwrAtpcCoordinatedPower based on Integer32"""
    defaultValue = 0


_MwrAtpcCoordinatedPower_Type.__name__ = "Integer32"
_MwrAtpcCoordinatedPower_Object = MibTableColumn
mwrAtpcCoordinatedPower = _MwrAtpcCoordinatedPower_Object(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 11, 1, 1, 1, 3),
    _MwrAtpcCoordinatedPower_Type()
)
mwrAtpcCoordinatedPower.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mwrAtpcCoordinatedPower.setStatus("current")
if mibBuilder.loadTexts:
    mwrAtpcCoordinatedPower.setUnits("dB")


class _MwrAtpcCoordinatedPowerEnable_Type(EnableType):
    """Custom type mwrAtpcCoordinatedPowerEnable based on EnableType"""
    defaultValue = 0


_MwrAtpcCoordinatedPowerEnable_Type.__name__ = "EnableType"
_MwrAtpcCoordinatedPowerEnable_Object = MibTableColumn
mwrAtpcCoordinatedPowerEnable = _MwrAtpcCoordinatedPowerEnable_Object(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 11, 1, 1, 1, 4),
    _MwrAtpcCoordinatedPowerEnable_Type()
)
mwrAtpcCoordinatedPowerEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mwrAtpcCoordinatedPowerEnable.setStatus("current")
_MwrAtpcMinTxPower_Type = Integer32
_MwrAtpcMinTxPower_Object = MibTableColumn
mwrAtpcMinTxPower = _MwrAtpcMinTxPower_Object(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 11, 1, 1, 1, 5),
    _MwrAtpcMinTxPower_Type()
)
mwrAtpcMinTxPower.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mwrAtpcMinTxPower.setStatus("current")
if mibBuilder.loadTexts:
    mwrAtpcMinTxPower.setUnits("dB")
_MwrAtpcMaxTxPower_Type = Integer32
_MwrAtpcMaxTxPower_Object = MibTableColumn
mwrAtpcMaxTxPower = _MwrAtpcMaxTxPower_Object(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 11, 1, 1, 1, 6),
    _MwrAtpcMaxTxPower_Type()
)
mwrAtpcMaxTxPower.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mwrAtpcMaxTxPower.setStatus("current")
if mibBuilder.loadTexts:
    mwrAtpcMaxTxPower.setUnits("dB")
_MwrAtpcRslTarget_Type = Integer32
_MwrAtpcRslTarget_Object = MibTableColumn
mwrAtpcRslTarget = _MwrAtpcRslTarget_Object(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 11, 1, 1, 1, 7),
    _MwrAtpcRslTarget_Type()
)
mwrAtpcRslTarget.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mwrAtpcRslTarget.setStatus("current")
_MwrAtpcRslTargetUseDefault_Type = EnableType
_MwrAtpcRslTargetUseDefault_Object = MibTableColumn
mwrAtpcRslTargetUseDefault = _MwrAtpcRslTargetUseDefault_Object(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 11, 1, 1, 1, 8),
    _MwrAtpcRslTargetUseDefault_Type()
)
mwrAtpcRslTargetUseDefault.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mwrAtpcRslTargetUseDefault.setStatus("current")
_MwrAtpcStatus_ObjectIdentity = ObjectIdentity
mwrAtpcStatus = _MwrAtpcStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 11, 2)
)
_MwrAtpcStatusTable_Object = MibTable
mwrAtpcStatusTable = _MwrAtpcStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 11, 2, 1)
)
if mibBuilder.loadTexts:
    mwrAtpcStatusTable.setStatus("current")
_MwrAtpcStatusEntry_Object = MibTableRow
mwrAtpcStatusEntry = _MwrAtpcStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 11, 2, 1, 1)
)
mwrAtpcStatusEntry.setIndexNames(
    (0, "MWR-ETHERNET-MIB", "mwrAtpcStatusIndex"),
)
if mibBuilder.loadTexts:
    mwrAtpcStatusEntry.setStatus("current")
_MwrAtpcStatusIndex_Type = RadioInstanceType
_MwrAtpcStatusIndex_Object = MibTableColumn
mwrAtpcStatusIndex = _MwrAtpcStatusIndex_Object(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 11, 2, 1, 1, 1),
    _MwrAtpcStatusIndex_Type()
)
mwrAtpcStatusIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mwrAtpcStatusIndex.setStatus("current")


class _MwrAtpcRunningStatus_Type(Integer32):
    """Custom type mwrAtpcRunningStatus based on Integer32"""
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
              8,
              9)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("disabledAuto", 2),
          ("running", 3),
          ("runningToggling", 4),
          ("suspended", 5),
          ("suspendedLostComm", 6),
          ("suspendedRadioDown", 7),
          ("suspendedRadioMuted", 8),
          ("suspendedRadioLoopback", 9))
    )


_MwrAtpcRunningStatus_Type.__name__ = "Integer32"
_MwrAtpcRunningStatus_Object = MibTableColumn
mwrAtpcRunningStatus = _MwrAtpcRunningStatus_Object(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 11, 2, 1, 1, 2),
    _MwrAtpcRunningStatus_Type()
)
mwrAtpcRunningStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwrAtpcRunningStatus.setStatus("current")
_MwrAtpcDefaultRslTarget_Type = Integer32
_MwrAtpcDefaultRslTarget_Object = MibTableColumn
mwrAtpcDefaultRslTarget = _MwrAtpcDefaultRslTarget_Object(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 11, 2, 1, 1, 3),
    _MwrAtpcDefaultRslTarget_Type()
)
mwrAtpcDefaultRslTarget.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwrAtpcDefaultRslTarget.setStatus("current")
_MwrAtpcActualMinTxPower_Type = Integer32
_MwrAtpcActualMinTxPower_Object = MibTableColumn
mwrAtpcActualMinTxPower = _MwrAtpcActualMinTxPower_Object(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 11, 2, 1, 1, 4),
    _MwrAtpcActualMinTxPower_Type()
)
mwrAtpcActualMinTxPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwrAtpcActualMinTxPower.setStatus("current")
_MwrAtpcActualMaxTxPower_Type = Integer32
_MwrAtpcActualMaxTxPower_Object = MibTableColumn
mwrAtpcActualMaxTxPower = _MwrAtpcActualMaxTxPower_Object(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 11, 2, 1, 1, 5),
    _MwrAtpcActualMaxTxPower_Type()
)
mwrAtpcActualMaxTxPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwrAtpcActualMaxTxPower.setStatus("current")
_MwrAtpcActualCoordinatedPower_Type = Integer32
_MwrAtpcActualCoordinatedPower_Object = MibTableColumn
mwrAtpcActualCoordinatedPower = _MwrAtpcActualCoordinatedPower_Object(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 11, 2, 1, 1, 6),
    _MwrAtpcActualCoordinatedPower_Type()
)
mwrAtpcActualCoordinatedPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwrAtpcActualCoordinatedPower.setStatus("current")
_MwrAtpcPeerRslTarget_Type = Integer32
_MwrAtpcPeerRslTarget_Object = MibTableColumn
mwrAtpcPeerRslTarget = _MwrAtpcPeerRslTarget_Object(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 11, 2, 1, 1, 7),
    _MwrAtpcPeerRslTarget_Type()
)
mwrAtpcPeerRslTarget.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwrAtpcPeerRslTarget.setStatus("current")
_MwrAtpcMinRslTarget_Type = Integer32
_MwrAtpcMinRslTarget_Object = MibTableColumn
mwrAtpcMinRslTarget = _MwrAtpcMinRslTarget_Object(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 11, 2, 1, 1, 8),
    _MwrAtpcMinRslTarget_Type()
)
mwrAtpcMinRslTarget.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwrAtpcMinRslTarget.setStatus("current")
_MwrAtpcMaxRslTarget_Type = Integer32
_MwrAtpcMaxRslTarget_Object = MibTableColumn
mwrAtpcMaxRslTarget = _MwrAtpcMaxRslTarget_Object(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 11, 2, 1, 1, 9),
    _MwrAtpcMaxRslTarget_Type()
)
mwrAtpcMaxRslTarget.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwrAtpcMaxRslTarget.setStatus("current")
_MwrAtpcPeerRsl_Type = Integer32
_MwrAtpcPeerRsl_Object = MibTableColumn
mwrAtpcPeerRsl = _MwrAtpcPeerRsl_Object(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 11, 2, 1, 1, 10),
    _MwrAtpcPeerRsl_Type()
)
mwrAtpcPeerRsl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwrAtpcPeerRsl.setStatus("current")
_MwrAtpcNotifications_ObjectIdentity = ObjectIdentity
mwrAtpcNotifications = _MwrAtpcNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 11, 3)
)
_MwrRadio_ObjectIdentity = ObjectIdentity
mwrRadio = _MwrRadio_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 12)
)
_MwrCompression_ObjectIdentity = ObjectIdentity
mwrCompression = _MwrCompression_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 13)
)
_MwrCompressionConfigurations_ObjectIdentity = ObjectIdentity
mwrCompressionConfigurations = _MwrCompressionConfigurations_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 13, 1)
)
_MwrBacRecordAvgPeriod_Type = Integer32
_MwrBacRecordAvgPeriod_Object = MibScalar
mwrBacRecordAvgPeriod = _MwrBacRecordAvgPeriod_Object(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 13, 1, 1),
    _MwrBacRecordAvgPeriod_Type()
)
mwrBacRecordAvgPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mwrBacRecordAvgPeriod.setStatus("current")
_MwrBacTable_Object = MibTable
mwrBacTable = _MwrBacTable_Object(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 13, 1, 2)
)
if mibBuilder.loadTexts:
    mwrBacTable.setStatus("current")
_MwrBacEntry_Object = MibTableRow
mwrBacEntry = _MwrBacEntry_Object(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 13, 1, 2, 1)
)
mwrBacEntry.setIndexNames(
    (0, "MWR-ETHERNET-MIB", "mwrBacQIndex"),
)
if mibBuilder.loadTexts:
    mwrBacEntry.setStatus("current")
_MwrBacQIndex_Type = QueueType
_MwrBacQIndex_Object = MibTableColumn
mwrBacQIndex = _MwrBacQIndex_Object(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 13, 1, 2, 1, 1),
    _MwrBacQIndex_Type()
)
mwrBacQIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mwrBacQIndex.setStatus("current")
_MwrBacQEnable_Type = EnableType
_MwrBacQEnable_Object = MibTableColumn
mwrBacQEnable = _MwrBacQEnable_Object(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 13, 1, 2, 1, 2),
    _MwrBacQEnable_Type()
)
mwrBacQEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mwrBacQEnable.setStatus("current")
_MwrBacQBlockSize_Type = Integer32
_MwrBacQBlockSize_Object = MibTableColumn
mwrBacQBlockSize = _MwrBacQBlockSize_Object(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 13, 1, 2, 1, 3),
    _MwrBacQBlockSize_Type()
)
mwrBacQBlockSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mwrBacQBlockSize.setStatus("current")
_MwrBacRecordLogging_Type = EnableType
_MwrBacRecordLogging_Object = MibTableColumn
mwrBacRecordLogging = _MwrBacRecordLogging_Object(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 13, 1, 2, 1, 4),
    _MwrBacRecordLogging_Type()
)
mwrBacRecordLogging.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mwrBacRecordLogging.setStatus("current")
_MwrHcQTable_Object = MibTable
mwrHcQTable = _MwrHcQTable_Object(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 13, 1, 3)
)
if mibBuilder.loadTexts:
    mwrHcQTable.setStatus("current")
_MwrHcQEntry_Object = MibTableRow
mwrHcQEntry = _MwrHcQEntry_Object(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 13, 1, 3, 1)
)
mwrHcQEntry.setIndexNames(
    (0, "MWR-ETHERNET-MIB", "mwrHcQIndex"),
)
if mibBuilder.loadTexts:
    mwrHcQEntry.setStatus("current")
_MwrHcQIndex_Type = QueueType
_MwrHcQIndex_Object = MibTableColumn
mwrHcQIndex = _MwrHcQIndex_Object(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 13, 1, 3, 1, 1),
    _MwrHcQIndex_Type()
)
mwrHcQIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mwrHcQIndex.setStatus("current")
_MwrHcQ1_Type = EnableType
_MwrHcQ1_Object = MibTableColumn
mwrHcQ1 = _MwrHcQ1_Object(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 13, 1, 3, 1, 2),
    _MwrHcQ1_Type()
)
mwrHcQ1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mwrHcQ1.setStatus("current")
_MwrHcQ2_Type = EnableType
_MwrHcQ2_Object = MibTableColumn
mwrHcQ2 = _MwrHcQ2_Object(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 13, 1, 3, 1, 3),
    _MwrHcQ2_Type()
)
mwrHcQ2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mwrHcQ2.setStatus("current")
_MwrHcQ3_Type = EnableType
_MwrHcQ3_Object = MibTableColumn
mwrHcQ3 = _MwrHcQ3_Object(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 13, 1, 3, 1, 4),
    _MwrHcQ3_Type()
)
mwrHcQ3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mwrHcQ3.setStatus("current")
_MwrHcQ4_Type = EnableType
_MwrHcQ4_Object = MibTableColumn
mwrHcQ4 = _MwrHcQ4_Object(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 13, 1, 3, 1, 5),
    _MwrHcQ4_Type()
)
mwrHcQ4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mwrHcQ4.setStatus("current")
_MwrHcQ5_Type = EnableType
_MwrHcQ5_Object = MibTableColumn
mwrHcQ5 = _MwrHcQ5_Object(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 13, 1, 3, 1, 6),
    _MwrHcQ5_Type()
)
mwrHcQ5.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mwrHcQ5.setStatus("current")
_MwrHcQ6_Type = EnableType
_MwrHcQ6_Object = MibTableColumn
mwrHcQ6 = _MwrHcQ6_Object(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 13, 1, 3, 1, 7),
    _MwrHcQ6_Type()
)
mwrHcQ6.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mwrHcQ6.setStatus("current")
_MwrHcQ7_Type = EnableType
_MwrHcQ7_Object = MibTableColumn
mwrHcQ7 = _MwrHcQ7_Object(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 13, 1, 3, 1, 8),
    _MwrHcQ7_Type()
)
mwrHcQ7.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mwrHcQ7.setStatus("current")
_MwrHcQ8_Type = EnableType
_MwrHcQ8_Object = MibTableColumn
mwrHcQ8 = _MwrHcQ8_Object(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 13, 1, 3, 1, 9),
    _MwrHcQ8_Type()
)
mwrHcQ8.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mwrHcQ8.setStatus("current")
_MwrHcQRowStatus_Type = RowStatus
_MwrHcQRowStatus_Object = MibTableColumn
mwrHcQRowStatus = _MwrHcQRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 13, 1, 3, 1, 10),
    _MwrHcQRowStatus_Type()
)
mwrHcQRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mwrHcQRowStatus.setStatus("current")
_MwrCompressionStatus_ObjectIdentity = ObjectIdentity
mwrCompressionStatus = _MwrCompressionStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 13, 2)
)
_MwrBacStatusTable_Object = MibTable
mwrBacStatusTable = _MwrBacStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 13, 2, 1)
)
if mibBuilder.loadTexts:
    mwrBacStatusTable.setStatus("current")
_MwrBacStatusEntry_Object = MibTableRow
mwrBacStatusEntry = _MwrBacStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 13, 2, 1, 1)
)
mwrBacStatusEntry.setIndexNames(
    (0, "MWR-ETHERNET-MIB", "mwrBacStatusQIndex"),
)
if mibBuilder.loadTexts:
    mwrBacStatusEntry.setStatus("current")
_MwrBacStatusQIndex_Type = QueueType
_MwrBacStatusQIndex_Object = MibTableColumn
mwrBacStatusQIndex = _MwrBacStatusQIndex_Object(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 13, 2, 1, 1, 1),
    _MwrBacStatusQIndex_Type()
)
mwrBacStatusQIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mwrBacStatusQIndex.setStatus("current")
_MwrBacUncompressedRatio_Type = DisplayString
_MwrBacUncompressedRatio_Object = MibTableColumn
mwrBacUncompressedRatio = _MwrBacUncompressedRatio_Object(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 13, 2, 1, 1, 2),
    _MwrBacUncompressedRatio_Type()
)
mwrBacUncompressedRatio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwrBacUncompressedRatio.setStatus("current")
_MwrBacGain_Type = DisplayString
_MwrBacGain_Object = MibTableColumn
mwrBacGain = _MwrBacGain_Object(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 13, 2, 1, 1, 3),
    _MwrBacGain_Type()
)
mwrBacGain.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwrBacGain.setStatus("current")
_MwrCompressionNotifications_ObjectIdentity = ObjectIdentity
mwrCompressionNotifications = _MwrCompressionNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 13, 3)
)
_MwrEvents_ObjectIdentity = ObjectIdentity
mwrEvents = _MwrEvents_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 14)
)
_MwrEventsConfigurations_ObjectIdentity = ObjectIdentity
mwrEventsConfigurations = _MwrEventsConfigurations_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 14, 1)
)
_MwrEventConfigTable_Object = MibTable
mwrEventConfigTable = _MwrEventConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 14, 1, 1)
)
if mibBuilder.loadTexts:
    mwrEventConfigTable.setStatus("current")
_MwrEventConfigEntry_Object = MibTableRow
mwrEventConfigEntry = _MwrEventConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 14, 1, 1, 1)
)
mwrEventConfigEntry.setIndexNames(
    (0, "MWR-ETHERNET-MIB", "mwrEventConfigIndex"),
    (0, "MWR-ETHERNET-MIB", "mwrEventInstanceIndex"),
)
if mibBuilder.loadTexts:
    mwrEventConfigEntry.setStatus("current")
_MwrEventConfigIndex_Type = Unsigned32
_MwrEventConfigIndex_Object = MibTableColumn
mwrEventConfigIndex = _MwrEventConfigIndex_Object(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 14, 1, 1, 1, 1),
    _MwrEventConfigIndex_Type()
)
mwrEventConfigIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mwrEventConfigIndex.setStatus("current")
_MwrEventInstanceIndex_Type = Unsigned32
_MwrEventInstanceIndex_Object = MibTableColumn
mwrEventInstanceIndex = _MwrEventInstanceIndex_Object(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 14, 1, 1, 1, 2),
    _MwrEventInstanceIndex_Type()
)
mwrEventInstanceIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwrEventInstanceIndex.setStatus("current")


class _MwrEventConfigSeverity_Type(Integer32):
    """Custom type mwrEventConfigSeverity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("clear", 0),
          ("warning", 1),
          ("minor", 2),
          ("major", 3),
          ("critical", 4))
    )


_MwrEventConfigSeverity_Type.__name__ = "Integer32"
_MwrEventConfigSeverity_Object = MibTableColumn
mwrEventConfigSeverity = _MwrEventConfigSeverity_Object(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 14, 1, 1, 1, 3),
    _MwrEventConfigSeverity_Type()
)
mwrEventConfigSeverity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mwrEventConfigSeverity.setStatus("current")
_MwrEventName_Type = DisplayString
_MwrEventName_Object = MibTableColumn
mwrEventName = _MwrEventName_Object(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 14, 1, 1, 1, 4),
    _MwrEventName_Type()
)
mwrEventName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwrEventName.setStatus("current")
_MwrAlarmConfigState_Type = EnableType
_MwrAlarmConfigState_Object = MibTableColumn
mwrAlarmConfigState = _MwrAlarmConfigState_Object(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 14, 1, 1, 1, 5),
    _MwrAlarmConfigState_Type()
)
mwrAlarmConfigState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mwrAlarmConfigState.setStatus("current")
_MwrTrapConfigState_Type = EnableType
_MwrTrapConfigState_Object = MibTableColumn
mwrTrapConfigState = _MwrTrapConfigState_Object(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 14, 1, 1, 1, 6),
    _MwrTrapConfigState_Type()
)
mwrTrapConfigState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mwrTrapConfigState.setStatus("current")
_MwrLogEventState_Type = EnableType
_MwrLogEventState_Object = MibTableColumn
mwrLogEventState = _MwrLogEventState_Object(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 14, 1, 1, 1, 7),
    _MwrLogEventState_Type()
)
mwrLogEventState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mwrLogEventState.setStatus("current")
_MwrLogs_ObjectIdentity = ObjectIdentity
mwrLogs = _MwrLogs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 15)
)
_MwrLogsConfigurations_ObjectIdentity = ObjectIdentity
mwrLogsConfigurations = _MwrLogsConfigurations_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 15, 1)
)


class _MwrEventLogEnable_Type(EnableType):
    """Custom type mwrEventLogEnable based on EnableType"""
    defaultValue = 1


_MwrEventLogEnable_Type.__name__ = "EnableType"
_MwrEventLogEnable_Object = MibScalar
mwrEventLogEnable = _MwrEventLogEnable_Object(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 15, 1, 1),
    _MwrEventLogEnable_Type()
)
mwrEventLogEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mwrEventLogEnable.setStatus("current")


class _MwrPerfmLogEnable_Type(EnableType):
    """Custom type mwrPerfmLogEnable based on EnableType"""
    defaultValue = 1


_MwrPerfmLogEnable_Type.__name__ = "EnableType"
_MwrPerfmLogEnable_Object = MibScalar
mwrPerfmLogEnable = _MwrPerfmLogEnable_Object(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 15, 1, 2),
    _MwrPerfmLogEnable_Type()
)
mwrPerfmLogEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mwrPerfmLogEnable.setStatus("current")


class _MwrPerfmLogInterval_Type(DisplayString):
    """Custom type mwrPerfmLogInterval based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_MwrPerfmLogInterval_Type.__name__ = "DisplayString"
_MwrPerfmLogInterval_Object = MibScalar
mwrPerfmLogInterval = _MwrPerfmLogInterval_Object(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 15, 1, 3),
    _MwrPerfmLogInterval_Type()
)
mwrPerfmLogInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mwrPerfmLogInterval.setStatus("current")
_MwrSysLogServerTable_Object = MibTable
mwrSysLogServerTable = _MwrSysLogServerTable_Object(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 15, 1, 4)
)
if mibBuilder.loadTexts:
    mwrSysLogServerTable.setStatus("current")
_MwrSysLogServerEntry_Object = MibTableRow
mwrSysLogServerEntry = _MwrSysLogServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 15, 1, 4, 1)
)
mwrSysLogServerEntry.setIndexNames(
    (0, "MWR-ETHERNET-MIB", "mwrSysLogServerIndex"),
)
if mibBuilder.loadTexts:
    mwrSysLogServerEntry.setStatus("current")


class _MwrSysLogServerIndex_Type(Integer32):
    """Custom type mwrSysLogServerIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_MwrSysLogServerIndex_Type.__name__ = "Integer32"
_MwrSysLogServerIndex_Object = MibTableColumn
mwrSysLogServerIndex = _MwrSysLogServerIndex_Object(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 15, 1, 4, 1, 1),
    _MwrSysLogServerIndex_Type()
)
mwrSysLogServerIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mwrSysLogServerIndex.setStatus("current")
_MwrSysLogEnable_Type = EnableType
_MwrSysLogEnable_Object = MibTableColumn
mwrSysLogEnable = _MwrSysLogEnable_Object(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 15, 1, 4, 1, 2),
    _MwrSysLogEnable_Type()
)
mwrSysLogEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mwrSysLogEnable.setStatus("current")
_MwrSysLogHostDomain_Type = InetAddressType
_MwrSysLogHostDomain_Object = MibTableColumn
mwrSysLogHostDomain = _MwrSysLogHostDomain_Object(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 15, 1, 4, 1, 3),
    _MwrSysLogHostDomain_Type()
)
mwrSysLogHostDomain.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mwrSysLogHostDomain.setStatus("current")
_MwrSysLogHostAddress_Type = InetAddress
_MwrSysLogHostAddress_Object = MibTableColumn
mwrSysLogHostAddress = _MwrSysLogHostAddress_Object(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 15, 1, 4, 1, 4),
    _MwrSysLogHostAddress_Type()
)
mwrSysLogHostAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mwrSysLogHostAddress.setStatus("current")
_MwrPM_ObjectIdentity = ObjectIdentity
mwrPM = _MwrPM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 16)
)
_MwrPMConfigurations_ObjectIdentity = ObjectIdentity
mwrPMConfigurations = _MwrPMConfigurations_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 16, 1)
)
_MwrPmRspiThresholdTable_Object = MibTable
mwrPmRspiThresholdTable = _MwrPmRspiThresholdTable_Object(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 16, 1, 1)
)
if mibBuilder.loadTexts:
    mwrPmRspiThresholdTable.setStatus("current")
_MwrPmRspiThresholdEntry_Object = MibTableRow
mwrPmRspiThresholdEntry = _MwrPmRspiThresholdEntry_Object(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 16, 1, 1, 1)
)
mwrPmRspiThresholdEntry.setIndexNames(
    (0, "MWR-ETHERNET-MIB", "mwrPmRspiThrIndex"),
)
if mibBuilder.loadTexts:
    mwrPmRspiThresholdEntry.setStatus("current")
_MwrPmRspiThrIndex_Type = RadioInstanceType
_MwrPmRspiThrIndex_Object = MibTableColumn
mwrPmRspiThrIndex = _MwrPmRspiThrIndex_Object(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 16, 1, 1, 1, 1),
    _MwrPmRspiThrIndex_Type()
)
mwrPmRspiThrIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mwrPmRspiThrIndex.setStatus("current")
_MwrPmRLT1_Type = Integer32
_MwrPmRLT1_Object = MibTableColumn
mwrPmRLT1 = _MwrPmRLT1_Object(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 16, 1, 1, 1, 2),
    _MwrPmRLT1_Type()
)
mwrPmRLT1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mwrPmRLT1.setStatus("current")
_MwrPmRLT2_Type = Integer32
_MwrPmRLT2_Object = MibTableColumn
mwrPmRLT2 = _MwrPmRLT2_Object(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 16, 1, 1, 1, 3),
    _MwrPmRLT2_Type()
)
mwrPmRLT2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mwrPmRLT2.setStatus("current")
_MwrPmRLT3_Type = Integer32
_MwrPmRLT3_Object = MibTableColumn
mwrPmRLT3 = _MwrPmRLT3_Object(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 16, 1, 1, 1, 4),
    _MwrPmRLT3_Type()
)
mwrPmRLT3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mwrPmRLT3.setStatus("current")
_MwrPmRLT4_Type = Integer32
_MwrPmRLT4_Object = MibTableColumn
mwrPmRLT4 = _MwrPmRLT4_Object(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 16, 1, 1, 1, 5),
    _MwrPmRLT4_Type()
)
mwrPmRLT4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mwrPmRLT4.setStatus("current")
_MwrPmTLT1_Type = Integer32
_MwrPmTLT1_Object = MibTableColumn
mwrPmTLT1 = _MwrPmTLT1_Object(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 16, 1, 1, 1, 6),
    _MwrPmTLT1_Type()
)
mwrPmTLT1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mwrPmTLT1.setStatus("current")
_MwrPmTLT2_Type = Integer32
_MwrPmTLT2_Object = MibTableColumn
mwrPmTLT2 = _MwrPmTLT2_Object(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 16, 1, 1, 1, 7),
    _MwrPmTLT2_Type()
)
mwrPmTLT2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mwrPmTLT2.setStatus("current")
_MwrPmRspiThrRowStatus_Type = RowStatus
_MwrPmRspiThrRowStatus_Object = MibTableColumn
mwrPmRspiThrRowStatus = _MwrPmRspiThrRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 16, 1, 1, 1, 8),
    _MwrPmRspiThrRowStatus_Type()
)
mwrPmRspiThrRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mwrPmRspiThrRowStatus.setStatus("current")
_MwrPmBwThresholdTable_Object = MibTable
mwrPmBwThresholdTable = _MwrPmBwThresholdTable_Object(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 16, 1, 2)
)
if mibBuilder.loadTexts:
    mwrPmBwThresholdTable.setStatus("current")
_MwrPmBwThresholdEntry_Object = MibTableRow
mwrPmBwThresholdEntry = _MwrPmBwThresholdEntry_Object(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 16, 1, 2, 1)
)
mwrPmBwThresholdEntry.setIndexNames(
    (0, "MWR-ETHERNET-MIB", "mwrPmBWThrIndex"),
)
if mibBuilder.loadTexts:
    mwrPmBwThresholdEntry.setStatus("current")
_MwrPmBWThrIndex_Type = Integer32
_MwrPmBWThrIndex_Object = MibTableColumn
mwrPmBWThrIndex = _MwrPmBWThrIndex_Object(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 16, 1, 2, 1, 1),
    _MwrPmBWThrIndex_Type()
)
mwrPmBWThrIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mwrPmBWThrIndex.setStatus("current")
_MwrPmBWT1_Type = Integer32
_MwrPmBWT1_Object = MibTableColumn
mwrPmBWT1 = _MwrPmBWT1_Object(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 16, 1, 2, 1, 2),
    _MwrPmBWT1_Type()
)
mwrPmBWT1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mwrPmBWT1.setStatus("current")
_MwrPmBWT2_Type = Integer32
_MwrPmBWT2_Object = MibTableColumn
mwrPmBWT2 = _MwrPmBWT2_Object(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 16, 1, 2, 1, 3),
    _MwrPmBWT2_Type()
)
mwrPmBWT2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mwrPmBWT2.setStatus("current")
_MwrPmBWT3_Type = Integer32
_MwrPmBWT3_Object = MibTableColumn
mwrPmBWT3 = _MwrPmBWT3_Object(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 16, 1, 2, 1, 4),
    _MwrPmBWT3_Type()
)
mwrPmBWT3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mwrPmBWT3.setStatus("current")
_MwrPmBWT4_Type = Integer32
_MwrPmBWT4_Object = MibTableColumn
mwrPmBWT4 = _MwrPmBWT4_Object(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 16, 1, 2, 1, 5),
    _MwrPmBWT4_Type()
)
mwrPmBWT4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mwrPmBWT4.setStatus("current")
_MwrPmBWT5_Type = Integer32
_MwrPmBWT5_Object = MibTableColumn
mwrPmBWT5 = _MwrPmBWT5_Object(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 16, 1, 2, 1, 6),
    _MwrPmBWT5_Type()
)
mwrPmBWT5.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mwrPmBWT5.setStatus("current")
_MwrPmBWT6_Type = Integer32
_MwrPmBWT6_Object = MibTableColumn
mwrPmBWT6 = _MwrPmBWT6_Object(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 16, 1, 2, 1, 7),
    _MwrPmBWT6_Type()
)
mwrPmBWT6.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mwrPmBWT6.setStatus("current")
_MwrPmBWT7_Type = Integer32
_MwrPmBWT7_Object = MibTableColumn
mwrPmBWT7 = _MwrPmBWT7_Object(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 16, 1, 2, 1, 8),
    _MwrPmBWT7_Type()
)
mwrPmBWT7.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mwrPmBWT7.setStatus("current")
_MwrPmBWT8_Type = Integer32
_MwrPmBWT8_Object = MibTableColumn
mwrPmBWT8 = _MwrPmBWT8_Object(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 16, 1, 2, 1, 9),
    _MwrPmBWT8_Type()
)
mwrPmBWT8.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mwrPmBWT8.setStatus("current")
_MwrPmBWT9_Type = Integer32
_MwrPmBWT9_Object = MibTableColumn
mwrPmBWT9 = _MwrPmBWT9_Object(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 16, 1, 2, 1, 10),
    _MwrPmBWT9_Type()
)
mwrPmBWT9.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mwrPmBWT9.setStatus("current")
_MwrPmBWT10_Type = Integer32
_MwrPmBWT10_Object = MibTableColumn
mwrPmBWT10 = _MwrPmBWT10_Object(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 16, 1, 2, 1, 11),
    _MwrPmBWT10_Type()
)
mwrPmBWT10.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mwrPmBWT10.setStatus("current")
_MwrPmBWTRowStatus_Type = RowStatus
_MwrPmBWTRowStatus_Object = MibTableColumn
mwrPmBWTRowStatus = _MwrPmBWTRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 16, 1, 2, 1, 12),
    _MwrPmBWTRowStatus_Type()
)
mwrPmBWTRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mwrPmBWTRowStatus.setStatus("current")
_MwrPmTpThresholdTable_Object = MibTable
mwrPmTpThresholdTable = _MwrPmTpThresholdTable_Object(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 16, 1, 3)
)
if mibBuilder.loadTexts:
    mwrPmTpThresholdTable.setStatus("current")
_MwrPmTpThresholdEntry_Object = MibTableRow
mwrPmTpThresholdEntry = _MwrPmTpThresholdEntry_Object(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 16, 1, 3, 1)
)
mwrPmTpThresholdEntry.setIndexNames(
    (0, "MWR-ETHERNET-MIB", "mwrPmTPThrIndex"),
)
if mibBuilder.loadTexts:
    mwrPmTpThresholdEntry.setStatus("current")
_MwrPmTPThrIndex_Type = Integer32
_MwrPmTPThrIndex_Object = MibTableColumn
mwrPmTPThrIndex = _MwrPmTPThrIndex_Object(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 16, 1, 3, 1, 1),
    _MwrPmTPThrIndex_Type()
)
mwrPmTPThrIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mwrPmTPThrIndex.setStatus("current")
_MwrPmTPT1_Type = Integer32
_MwrPmTPT1_Object = MibTableColumn
mwrPmTPT1 = _MwrPmTPT1_Object(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 16, 1, 3, 1, 2),
    _MwrPmTPT1_Type()
)
mwrPmTPT1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mwrPmTPT1.setStatus("current")
_MwrPmTPT2_Type = Integer32
_MwrPmTPT2_Object = MibTableColumn
mwrPmTPT2 = _MwrPmTPT2_Object(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 16, 1, 3, 1, 3),
    _MwrPmTPT2_Type()
)
mwrPmTPT2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mwrPmTPT2.setStatus("current")
_MwrPmTPT3_Type = Integer32
_MwrPmTPT3_Object = MibTableColumn
mwrPmTPT3 = _MwrPmTPT3_Object(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 16, 1, 3, 1, 4),
    _MwrPmTPT3_Type()
)
mwrPmTPT3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mwrPmTPT3.setStatus("current")
_MwrPmTPT4_Type = Integer32
_MwrPmTPT4_Object = MibTableColumn
mwrPmTPT4 = _MwrPmTPT4_Object(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 16, 1, 3, 1, 5),
    _MwrPmTPT4_Type()
)
mwrPmTPT4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mwrPmTPT4.setStatus("current")
_MwrPmTPT5_Type = Integer32
_MwrPmTPT5_Object = MibTableColumn
mwrPmTPT5 = _MwrPmTPT5_Object(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 16, 1, 3, 1, 6),
    _MwrPmTPT5_Type()
)
mwrPmTPT5.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mwrPmTPT5.setStatus("current")
_MwrPmTPT6_Type = Integer32
_MwrPmTPT6_Object = MibTableColumn
mwrPmTPT6 = _MwrPmTPT6_Object(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 16, 1, 3, 1, 7),
    _MwrPmTPT6_Type()
)
mwrPmTPT6.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mwrPmTPT6.setStatus("current")
_MwrPmTPT7_Type = Integer32
_MwrPmTPT7_Object = MibTableColumn
mwrPmTPT7 = _MwrPmTPT7_Object(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 16, 1, 3, 1, 8),
    _MwrPmTPT7_Type()
)
mwrPmTPT7.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mwrPmTPT7.setStatus("current")
_MwrPmTPT8_Type = Integer32
_MwrPmTPT8_Object = MibTableColumn
mwrPmTPT8 = _MwrPmTPT8_Object(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 16, 1, 3, 1, 9),
    _MwrPmTPT8_Type()
)
mwrPmTPT8.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mwrPmTPT8.setStatus("current")
_MwrPmTPT9_Type = Integer32
_MwrPmTPT9_Object = MibTableColumn
mwrPmTPT9 = _MwrPmTPT9_Object(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 16, 1, 3, 1, 10),
    _MwrPmTPT9_Type()
)
mwrPmTPT9.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mwrPmTPT9.setStatus("current")
_MwrPmTPT10_Type = Integer32
_MwrPmTPT10_Object = MibTableColumn
mwrPmTPT10 = _MwrPmTPT10_Object(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 16, 1, 3, 1, 11),
    _MwrPmTPT10_Type()
)
mwrPmTPT10.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mwrPmTPT10.setStatus("current")
_MwrPmTPTRowStatus_Type = RowStatus
_MwrPmTPTRowStatus_Object = MibTableColumn
mwrPmTPTRowStatus = _MwrPmTPTRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 16, 1, 3, 1, 12),
    _MwrPmTPTRowStatus_Type()
)
mwrPmTPTRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mwrPmTPTRowStatus.setStatus("current")
_MwrPmAdvThresholdTable_Object = MibTable
mwrPmAdvThresholdTable = _MwrPmAdvThresholdTable_Object(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 16, 1, 4)
)
if mibBuilder.loadTexts:
    mwrPmAdvThresholdTable.setStatus("current")
_MwrPmAdvThresholdEntry_Object = MibTableRow
mwrPmAdvThresholdEntry = _MwrPmAdvThresholdEntry_Object(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 16, 1, 4, 1)
)
mwrPmAdvThresholdEntry.setIndexNames(
    (0, "MWR-ETHERNET-MIB", "mwrPmAdvThrIndex"),
)
if mibBuilder.loadTexts:
    mwrPmAdvThresholdEntry.setStatus("current")
_MwrPmAdvThrIndex_Type = Integer32
_MwrPmAdvThrIndex_Object = MibTableColumn
mwrPmAdvThrIndex = _MwrPmAdvThrIndex_Object(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 16, 1, 4, 1, 1),
    _MwrPmAdvThrIndex_Type()
)
mwrPmAdvThrIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mwrPmAdvThrIndex.setStatus("current")
_MwrPmAdvTxHitsT1_Type = Integer32
_MwrPmAdvTxHitsT1_Object = MibTableColumn
mwrPmAdvTxHitsT1 = _MwrPmAdvTxHitsT1_Object(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 16, 1, 4, 1, 2),
    _MwrPmAdvTxHitsT1_Type()
)
mwrPmAdvTxHitsT1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mwrPmAdvTxHitsT1.setStatus("current")
_MwrPmAdvRxHitsT1_Type = Integer32
_MwrPmAdvRxHitsT1_Object = MibTableColumn
mwrPmAdvRxHitsT1 = _MwrPmAdvRxHitsT1_Object(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 16, 1, 4, 1, 3),
    _MwrPmAdvRxHitsT1_Type()
)
mwrPmAdvRxHitsT1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mwrPmAdvRxHitsT1.setStatus("current")
_MwrPmAdvRowStatus_Type = RowStatus
_MwrPmAdvRowStatus_Object = MibTableColumn
mwrPmAdvRowStatus = _MwrPmAdvRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 16, 1, 4, 1, 4),
    _MwrPmAdvRowStatus_Type()
)
mwrPmAdvRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mwrPmAdvRowStatus.setStatus("current")
_MwrPMStatus_ObjectIdentity = ObjectIdentity
mwrPMStatus = _MwrPMStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 16, 2)
)
_MwrPmRspiTable_Object = MibTable
mwrPmRspiTable = _MwrPmRspiTable_Object(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 16, 2, 1)
)
if mibBuilder.loadTexts:
    mwrPmRspiTable.setStatus("current")
_MwrPmRspiEntry_Object = MibTableRow
mwrPmRspiEntry = _MwrPmRspiEntry_Object(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 16, 2, 1, 1)
)
mwrPmRspiEntry.setIndexNames(
    (0, "MWR-ETHERNET-MIB", "mwrPmRspiStatusIndex"),
    (0, "MWR-ETHERNET-MIB", "mwrPmRspiInterval"),
    (0, "MWR-ETHERNET-MIB", "mwrPmRspiIntervalID"),
)
if mibBuilder.loadTexts:
    mwrPmRspiEntry.setStatus("current")
_MwrPmRspiStatusIndex_Type = RadioInstanceType
_MwrPmRspiStatusIndex_Object = MibTableColumn
mwrPmRspiStatusIndex = _MwrPmRspiStatusIndex_Object(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 16, 2, 1, 1, 1),
    _MwrPmRspiStatusIndex_Type()
)
mwrPmRspiStatusIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mwrPmRspiStatusIndex.setStatus("current")
_MwrPmRspiInterval_Type = PMIntervalType
_MwrPmRspiInterval_Object = MibTableColumn
mwrPmRspiInterval = _MwrPmRspiInterval_Object(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 16, 2, 1, 1, 2),
    _MwrPmRspiInterval_Type()
)
mwrPmRspiInterval.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mwrPmRspiInterval.setStatus("current")


class _MwrPmRspiIntervalID_Type(Integer32):
    """Custom type mwrPmRspiIntervalID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_MwrPmRspiIntervalID_Type.__name__ = "Integer32"
_MwrPmRspiIntervalID_Object = MibTableColumn
mwrPmRspiIntervalID = _MwrPmRspiIntervalID_Object(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 16, 2, 1, 1, 3),
    _MwrPmRspiIntervalID_Type()
)
mwrPmRspiIntervalID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mwrPmRspiIntervalID.setStatus("current")
_MwrPmRspiMeasSuspect_Type = TruthValue
_MwrPmRspiMeasSuspect_Object = MibTableColumn
mwrPmRspiMeasSuspect = _MwrPmRspiMeasSuspect_Object(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 16, 2, 1, 1, 4),
    _MwrPmRspiMeasSuspect_Type()
)
mwrPmRspiMeasSuspect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwrPmRspiMeasSuspect.setStatus("current")


class _MwrPmRspiMeasIntervalStatus_Type(Integer32):
    """Custom type mwrPmRspiMeasIntervalStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 1),
          ("valid", 2))
    )


_MwrPmRspiMeasIntervalStatus_Type.__name__ = "Integer32"
_MwrPmRspiMeasIntervalStatus_Object = MibTableColumn
mwrPmRspiMeasIntervalStatus = _MwrPmRspiMeasIntervalStatus_Object(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 16, 2, 1, 1, 5),
    _MwrPmRspiMeasIntervalStatus_Type()
)
mwrPmRspiMeasIntervalStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwrPmRspiMeasIntervalStatus.setStatus("current")
_MwrPmRspiMeasTimeLength_Type = Integer32
_MwrPmRspiMeasTimeLength_Object = MibTableColumn
mwrPmRspiMeasTimeLength = _MwrPmRspiMeasTimeLength_Object(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 16, 2, 1, 1, 6),
    _MwrPmRspiMeasTimeLength_Type()
)
mwrPmRspiMeasTimeLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwrPmRspiMeasTimeLength.setStatus("current")
if mibBuilder.loadTexts:
    mwrPmRspiMeasTimeLength.setUnits("seconds")
_MwrPmRspiMeasTLTMMin_Type = Integer32
_MwrPmRspiMeasTLTMMin_Object = MibTableColumn
mwrPmRspiMeasTLTMMin = _MwrPmRspiMeasTLTMMin_Object(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 16, 2, 1, 1, 7),
    _MwrPmRspiMeasTLTMMin_Type()
)
mwrPmRspiMeasTLTMMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwrPmRspiMeasTLTMMin.setStatus("current")
_MwrPmRspiMeasTLTMMax_Type = Integer32
_MwrPmRspiMeasTLTMMax_Object = MibTableColumn
mwrPmRspiMeasTLTMMax = _MwrPmRspiMeasTLTMMax_Object(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 16, 2, 1, 1, 8),
    _MwrPmRspiMeasTLTMMax_Type()
)
mwrPmRspiMeasTLTMMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwrPmRspiMeasTLTMMax.setStatus("current")
_MwrPmRspiMeasTLTS1_Type = Integer32
_MwrPmRspiMeasTLTS1_Object = MibTableColumn
mwrPmRspiMeasTLTS1 = _MwrPmRspiMeasTLTS1_Object(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 16, 2, 1, 1, 9),
    _MwrPmRspiMeasTLTS1_Type()
)
mwrPmRspiMeasTLTS1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwrPmRspiMeasTLTS1.setStatus("current")
if mibBuilder.loadTexts:
    mwrPmRspiMeasTLTS1.setUnits("seconds")
_MwrPmRspiMeasTLTS2_Type = Integer32
_MwrPmRspiMeasTLTS2_Object = MibTableColumn
mwrPmRspiMeasTLTS2 = _MwrPmRspiMeasTLTS2_Object(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 16, 2, 1, 1, 10),
    _MwrPmRspiMeasTLTS2_Type()
)
mwrPmRspiMeasTLTS2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwrPmRspiMeasTLTS2.setStatus("current")
if mibBuilder.loadTexts:
    mwrPmRspiMeasTLTS2.setUnits("seconds")
_MwrPmRspiMeasRLTMMin_Type = Integer32
_MwrPmRspiMeasRLTMMin_Object = MibTableColumn
mwrPmRspiMeasRLTMMin = _MwrPmRspiMeasRLTMMin_Object(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 16, 2, 1, 1, 11),
    _MwrPmRspiMeasRLTMMin_Type()
)
mwrPmRspiMeasRLTMMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwrPmRspiMeasRLTMMin.setStatus("current")
_MwrPmRspiMeasRLTMMax_Type = Integer32
_MwrPmRspiMeasRLTMMax_Object = MibTableColumn
mwrPmRspiMeasRLTMMax = _MwrPmRspiMeasRLTMMax_Object(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 16, 2, 1, 1, 12),
    _MwrPmRspiMeasRLTMMax_Type()
)
mwrPmRspiMeasRLTMMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwrPmRspiMeasRLTMMax.setStatus("current")
_MwrPmRspiMeasRLTS1_Type = Integer32
_MwrPmRspiMeasRLTS1_Object = MibTableColumn
mwrPmRspiMeasRLTS1 = _MwrPmRspiMeasRLTS1_Object(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 16, 2, 1, 1, 13),
    _MwrPmRspiMeasRLTS1_Type()
)
mwrPmRspiMeasRLTS1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwrPmRspiMeasRLTS1.setStatus("current")
if mibBuilder.loadTexts:
    mwrPmRspiMeasRLTS1.setUnits("seconds")
_MwrPmRspiMeasRLTS2_Type = Integer32
_MwrPmRspiMeasRLTS2_Object = MibTableColumn
mwrPmRspiMeasRLTS2 = _MwrPmRspiMeasRLTS2_Object(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 16, 2, 1, 1, 14),
    _MwrPmRspiMeasRLTS2_Type()
)
mwrPmRspiMeasRLTS2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwrPmRspiMeasRLTS2.setStatus("current")
if mibBuilder.loadTexts:
    mwrPmRspiMeasRLTS2.setUnits("seconds")
_MwrPmRspiMeasRLTS3_Type = Integer32
_MwrPmRspiMeasRLTS3_Object = MibTableColumn
mwrPmRspiMeasRLTS3 = _MwrPmRspiMeasRLTS3_Object(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 16, 2, 1, 1, 15),
    _MwrPmRspiMeasRLTS3_Type()
)
mwrPmRspiMeasRLTS3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwrPmRspiMeasRLTS3.setStatus("current")
if mibBuilder.loadTexts:
    mwrPmRspiMeasRLTS3.setUnits("seconds")
_MwrPmRspiMeasRLTS4_Type = Integer32
_MwrPmRspiMeasRLTS4_Object = MibTableColumn
mwrPmRspiMeasRLTS4 = _MwrPmRspiMeasRLTS4_Object(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 16, 2, 1, 1, 16),
    _MwrPmRspiMeasRLTS4_Type()
)
mwrPmRspiMeasRLTS4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwrPmRspiMeasRLTS4.setStatus("current")
if mibBuilder.loadTexts:
    mwrPmRspiMeasRLTS4.setUnits("seconds")
_MwrPmBWTable_Object = MibTable
mwrPmBWTable = _MwrPmBWTable_Object(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 16, 2, 2)
)
if mibBuilder.loadTexts:
    mwrPmBWTable.setStatus("current")
_MwrPmBWEntry_Object = MibTableRow
mwrPmBWEntry = _MwrPmBWEntry_Object(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 16, 2, 2, 1)
)
mwrPmBWEntry.setIndexNames(
    (0, "MWR-ETHERNET-MIB", "mwrPmBWStatusIndex"),
    (0, "MWR-ETHERNET-MIB", "mwrPmBWInterval"),
    (0, "MWR-ETHERNET-MIB", "mwrPmBWIntervalID"),
)
if mibBuilder.loadTexts:
    mwrPmBWEntry.setStatus("current")
_MwrPmBWStatusIndex_Type = Integer32
_MwrPmBWStatusIndex_Object = MibTableColumn
mwrPmBWStatusIndex = _MwrPmBWStatusIndex_Object(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 16, 2, 2, 1, 1),
    _MwrPmBWStatusIndex_Type()
)
mwrPmBWStatusIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mwrPmBWStatusIndex.setStatus("current")
_MwrPmBWInterval_Type = PMIntervalType
_MwrPmBWInterval_Object = MibTableColumn
mwrPmBWInterval = _MwrPmBWInterval_Object(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 16, 2, 2, 1, 2),
    _MwrPmBWInterval_Type()
)
mwrPmBWInterval.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mwrPmBWInterval.setStatus("current")


class _MwrPmBWIntervalID_Type(Integer32):
    """Custom type mwrPmBWIntervalID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_MwrPmBWIntervalID_Type.__name__ = "Integer32"
_MwrPmBWIntervalID_Object = MibTableColumn
mwrPmBWIntervalID = _MwrPmBWIntervalID_Object(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 16, 2, 2, 1, 3),
    _MwrPmBWIntervalID_Type()
)
mwrPmBWIntervalID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mwrPmBWIntervalID.setStatus("current")
_MwrPmBWMeasSuspect_Type = TruthValue
_MwrPmBWMeasSuspect_Object = MibTableColumn
mwrPmBWMeasSuspect = _MwrPmBWMeasSuspect_Object(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 16, 2, 2, 1, 4),
    _MwrPmBWMeasSuspect_Type()
)
mwrPmBWMeasSuspect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwrPmBWMeasSuspect.setStatus("current")


class _MwrPmBWMeasIntervalStatus_Type(Integer32):
    """Custom type mwrPmBWMeasIntervalStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 1),
          ("valid", 2))
    )


_MwrPmBWMeasIntervalStatus_Type.__name__ = "Integer32"
_MwrPmBWMeasIntervalStatus_Object = MibTableColumn
mwrPmBWMeasIntervalStatus = _MwrPmBWMeasIntervalStatus_Object(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 16, 2, 2, 1, 5),
    _MwrPmBWMeasIntervalStatus_Type()
)
mwrPmBWMeasIntervalStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwrPmBWMeasIntervalStatus.setStatus("current")
_MwrPmBWMeasTimeLength_Type = Integer32
_MwrPmBWMeasTimeLength_Object = MibTableColumn
mwrPmBWMeasTimeLength = _MwrPmBWMeasTimeLength_Object(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 16, 2, 2, 1, 6),
    _MwrPmBWMeasTimeLength_Type()
)
mwrPmBWMeasTimeLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwrPmBWMeasTimeLength.setStatus("current")
_MwrPmMeasBWTS1_Type = Integer32
_MwrPmMeasBWTS1_Object = MibTableColumn
mwrPmMeasBWTS1 = _MwrPmMeasBWTS1_Object(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 16, 2, 2, 1, 7),
    _MwrPmMeasBWTS1_Type()
)
mwrPmMeasBWTS1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwrPmMeasBWTS1.setStatus("current")
_MwrPmMeasBWTS2_Type = Integer32
_MwrPmMeasBWTS2_Object = MibTableColumn
mwrPmMeasBWTS2 = _MwrPmMeasBWTS2_Object(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 16, 2, 2, 1, 8),
    _MwrPmMeasBWTS2_Type()
)
mwrPmMeasBWTS2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwrPmMeasBWTS2.setStatus("current")
_MwrPmMeasBWTS3_Type = Integer32
_MwrPmMeasBWTS3_Object = MibTableColumn
mwrPmMeasBWTS3 = _MwrPmMeasBWTS3_Object(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 16, 2, 2, 1, 9),
    _MwrPmMeasBWTS3_Type()
)
mwrPmMeasBWTS3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwrPmMeasBWTS3.setStatus("current")
_MwrPmMeasBWTS4_Type = Integer32
_MwrPmMeasBWTS4_Object = MibTableColumn
mwrPmMeasBWTS4 = _MwrPmMeasBWTS4_Object(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 16, 2, 2, 1, 10),
    _MwrPmMeasBWTS4_Type()
)
mwrPmMeasBWTS4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwrPmMeasBWTS4.setStatus("current")
_MwrPmMeasBWTS5_Type = Integer32
_MwrPmMeasBWTS5_Object = MibTableColumn
mwrPmMeasBWTS5 = _MwrPmMeasBWTS5_Object(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 16, 2, 2, 1, 11),
    _MwrPmMeasBWTS5_Type()
)
mwrPmMeasBWTS5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwrPmMeasBWTS5.setStatus("current")
_MwrPmMeasBWTS6_Type = Integer32
_MwrPmMeasBWTS6_Object = MibTableColumn
mwrPmMeasBWTS6 = _MwrPmMeasBWTS6_Object(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 16, 2, 2, 1, 12),
    _MwrPmMeasBWTS6_Type()
)
mwrPmMeasBWTS6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwrPmMeasBWTS6.setStatus("current")
_MwrPmMeasBWTS7_Type = Integer32
_MwrPmMeasBWTS7_Object = MibTableColumn
mwrPmMeasBWTS7 = _MwrPmMeasBWTS7_Object(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 16, 2, 2, 1, 13),
    _MwrPmMeasBWTS7_Type()
)
mwrPmMeasBWTS7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwrPmMeasBWTS7.setStatus("current")
_MwrPmMeasBWTS8_Type = Integer32
_MwrPmMeasBWTS8_Object = MibTableColumn
mwrPmMeasBWTS8 = _MwrPmMeasBWTS8_Object(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 16, 2, 2, 1, 14),
    _MwrPmMeasBWTS8_Type()
)
mwrPmMeasBWTS8.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwrPmMeasBWTS8.setStatus("current")
_MwrPmMeasBWTS9_Type = Integer32
_MwrPmMeasBWTS9_Object = MibTableColumn
mwrPmMeasBWTS9 = _MwrPmMeasBWTS9_Object(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 16, 2, 2, 1, 15),
    _MwrPmMeasBWTS9_Type()
)
mwrPmMeasBWTS9.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwrPmMeasBWTS9.setStatus("current")
_MwrPmMeasBWTS10_Type = Integer32
_MwrPmMeasBWTS10_Object = MibTableColumn
mwrPmMeasBWTS10 = _MwrPmMeasBWTS10_Object(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 16, 2, 2, 1, 16),
    _MwrPmMeasBWTS10_Type()
)
mwrPmMeasBWTS10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwrPmMeasBWTS10.setStatus("current")
_MwrPmTPTable_Object = MibTable
mwrPmTPTable = _MwrPmTPTable_Object(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 16, 2, 3)
)
if mibBuilder.loadTexts:
    mwrPmTPTable.setStatus("current")
_MwrPmTPEntry_Object = MibTableRow
mwrPmTPEntry = _MwrPmTPEntry_Object(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 16, 2, 3, 1)
)
mwrPmTPEntry.setIndexNames(
    (0, "MWR-ETHERNET-MIB", "mwrPmTPStatusIndex"),
    (0, "MWR-ETHERNET-MIB", "mwrPmTPInterval"),
    (0, "MWR-ETHERNET-MIB", "mwrPmTPIntervalID"),
)
if mibBuilder.loadTexts:
    mwrPmTPEntry.setStatus("current")
_MwrPmTPStatusIndex_Type = Integer32
_MwrPmTPStatusIndex_Object = MibTableColumn
mwrPmTPStatusIndex = _MwrPmTPStatusIndex_Object(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 16, 2, 3, 1, 1),
    _MwrPmTPStatusIndex_Type()
)
mwrPmTPStatusIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mwrPmTPStatusIndex.setStatus("current")
_MwrPmTPInterval_Type = PMIntervalType
_MwrPmTPInterval_Object = MibTableColumn
mwrPmTPInterval = _MwrPmTPInterval_Object(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 16, 2, 3, 1, 2),
    _MwrPmTPInterval_Type()
)
mwrPmTPInterval.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mwrPmTPInterval.setStatus("current")


class _MwrPmTPIntervalID_Type(Integer32):
    """Custom type mwrPmTPIntervalID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_MwrPmTPIntervalID_Type.__name__ = "Integer32"
_MwrPmTPIntervalID_Object = MibTableColumn
mwrPmTPIntervalID = _MwrPmTPIntervalID_Object(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 16, 2, 3, 1, 3),
    _MwrPmTPIntervalID_Type()
)
mwrPmTPIntervalID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mwrPmTPIntervalID.setStatus("current")
_MwrPmTPMeasSuspect_Type = TruthValue
_MwrPmTPMeasSuspect_Object = MibTableColumn
mwrPmTPMeasSuspect = _MwrPmTPMeasSuspect_Object(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 16, 2, 3, 1, 4),
    _MwrPmTPMeasSuspect_Type()
)
mwrPmTPMeasSuspect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwrPmTPMeasSuspect.setStatus("current")


class _MwrPmTPMeasIntervalStatus_Type(Integer32):
    """Custom type mwrPmTPMeasIntervalStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 1),
          ("valid", 2))
    )


_MwrPmTPMeasIntervalStatus_Type.__name__ = "Integer32"
_MwrPmTPMeasIntervalStatus_Object = MibTableColumn
mwrPmTPMeasIntervalStatus = _MwrPmTPMeasIntervalStatus_Object(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 16, 2, 3, 1, 5),
    _MwrPmTPMeasIntervalStatus_Type()
)
mwrPmTPMeasIntervalStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwrPmTPMeasIntervalStatus.setStatus("current")
_MwrPmTPMeasTimeLength_Type = Integer32
_MwrPmTPMeasTimeLength_Object = MibTableColumn
mwrPmTPMeasTimeLength = _MwrPmTPMeasTimeLength_Object(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 16, 2, 3, 1, 6),
    _MwrPmTPMeasTimeLength_Type()
)
mwrPmTPMeasTimeLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwrPmTPMeasTimeLength.setStatus("current")
_MwrPmMeasTPTS1_Type = Integer32
_MwrPmMeasTPTS1_Object = MibTableColumn
mwrPmMeasTPTS1 = _MwrPmMeasTPTS1_Object(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 16, 2, 3, 1, 7),
    _MwrPmMeasTPTS1_Type()
)
mwrPmMeasTPTS1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwrPmMeasTPTS1.setStatus("current")
_MwrPmMeasTPTS2_Type = Integer32
_MwrPmMeasTPTS2_Object = MibTableColumn
mwrPmMeasTPTS2 = _MwrPmMeasTPTS2_Object(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 16, 2, 3, 1, 8),
    _MwrPmMeasTPTS2_Type()
)
mwrPmMeasTPTS2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwrPmMeasTPTS2.setStatus("current")
_MwrPmMeasTPTS3_Type = Integer32
_MwrPmMeasTPTS3_Object = MibTableColumn
mwrPmMeasTPTS3 = _MwrPmMeasTPTS3_Object(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 16, 2, 3, 1, 9),
    _MwrPmMeasTPTS3_Type()
)
mwrPmMeasTPTS3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwrPmMeasTPTS3.setStatus("current")
_MwrPmMeasTPTS4_Type = Integer32
_MwrPmMeasTPTS4_Object = MibTableColumn
mwrPmMeasTPTS4 = _MwrPmMeasTPTS4_Object(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 16, 2, 3, 1, 10),
    _MwrPmMeasTPTS4_Type()
)
mwrPmMeasTPTS4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwrPmMeasTPTS4.setStatus("current")
_MwrPmMeasTPTS5_Type = Integer32
_MwrPmMeasTPTS5_Object = MibTableColumn
mwrPmMeasTPTS5 = _MwrPmMeasTPTS5_Object(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 16, 2, 3, 1, 11),
    _MwrPmMeasTPTS5_Type()
)
mwrPmMeasTPTS5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwrPmMeasTPTS5.setStatus("current")
_MwrPmMeasTPTS6_Type = Integer32
_MwrPmMeasTPTS6_Object = MibTableColumn
mwrPmMeasTPTS6 = _MwrPmMeasTPTS6_Object(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 16, 2, 3, 1, 12),
    _MwrPmMeasTPTS6_Type()
)
mwrPmMeasTPTS6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwrPmMeasTPTS6.setStatus("current")
_MwrPmMeasTPTS7_Type = Integer32
_MwrPmMeasTPTS7_Object = MibTableColumn
mwrPmMeasTPTS7 = _MwrPmMeasTPTS7_Object(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 16, 2, 3, 1, 13),
    _MwrPmMeasTPTS7_Type()
)
mwrPmMeasTPTS7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwrPmMeasTPTS7.setStatus("current")
_MwrPmMeasTPTS8_Type = Integer32
_MwrPmMeasTPTS8_Object = MibTableColumn
mwrPmMeasTPTS8 = _MwrPmMeasTPTS8_Object(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 16, 2, 3, 1, 14),
    _MwrPmMeasTPTS8_Type()
)
mwrPmMeasTPTS8.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwrPmMeasTPTS8.setStatus("current")
_MwrPmMeasTPTS9_Type = Integer32
_MwrPmMeasTPTS9_Object = MibTableColumn
mwrPmMeasTPTS9 = _MwrPmMeasTPTS9_Object(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 16, 2, 3, 1, 15),
    _MwrPmMeasTPTS9_Type()
)
mwrPmMeasTPTS9.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwrPmMeasTPTS9.setStatus("current")
_MwrPmMeasTPTS10_Type = Integer32
_MwrPmMeasTPTS10_Object = MibTableColumn
mwrPmMeasTPTS10 = _MwrPmMeasTPTS10_Object(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 16, 2, 3, 1, 16),
    _MwrPmMeasTPTS10_Type()
)
mwrPmMeasTPTS10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwrPmMeasTPTS10.setStatus("current")
_MwrPmAdvTable_Object = MibTable
mwrPmAdvTable = _MwrPmAdvTable_Object(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 16, 2, 4)
)
if mibBuilder.loadTexts:
    mwrPmAdvTable.setStatus("current")
_MwrPmAdvEntry_Object = MibTableRow
mwrPmAdvEntry = _MwrPmAdvEntry_Object(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 16, 2, 4, 1)
)
mwrPmAdvEntry.setIndexNames(
    (0, "MWR-ETHERNET-MIB", "mwrPmAdvStatusIndex"),
    (0, "MWR-ETHERNET-MIB", "mwrPmAdvInterval"),
    (0, "MWR-ETHERNET-MIB", "mwrPmAdvIntervalID"),
)
if mibBuilder.loadTexts:
    mwrPmAdvEntry.setStatus("current")
_MwrPmAdvStatusIndex_Type = Integer32
_MwrPmAdvStatusIndex_Object = MibTableColumn
mwrPmAdvStatusIndex = _MwrPmAdvStatusIndex_Object(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 16, 2, 4, 1, 1),
    _MwrPmAdvStatusIndex_Type()
)
mwrPmAdvStatusIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mwrPmAdvStatusIndex.setStatus("current")
_MwrPmAdvInterval_Type = PMIntervalType
_MwrPmAdvInterval_Object = MibTableColumn
mwrPmAdvInterval = _MwrPmAdvInterval_Object(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 16, 2, 4, 1, 2),
    _MwrPmAdvInterval_Type()
)
mwrPmAdvInterval.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mwrPmAdvInterval.setStatus("current")


class _MwrPmAdvIntervalID_Type(Integer32):
    """Custom type mwrPmAdvIntervalID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_MwrPmAdvIntervalID_Type.__name__ = "Integer32"
_MwrPmAdvIntervalID_Object = MibTableColumn
mwrPmAdvIntervalID = _MwrPmAdvIntervalID_Object(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 16, 2, 4, 1, 3),
    _MwrPmAdvIntervalID_Type()
)
mwrPmAdvIntervalID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mwrPmAdvIntervalID.setStatus("current")
_MwrPmAdvMeasSuspect_Type = TruthValue
_MwrPmAdvMeasSuspect_Object = MibTableColumn
mwrPmAdvMeasSuspect = _MwrPmAdvMeasSuspect_Object(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 16, 2, 4, 1, 4),
    _MwrPmAdvMeasSuspect_Type()
)
mwrPmAdvMeasSuspect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwrPmAdvMeasSuspect.setStatus("current")


class _MwrPmAdvMeasIntervalStatus_Type(Integer32):
    """Custom type mwrPmAdvMeasIntervalStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 1),
          ("valid", 2))
    )


_MwrPmAdvMeasIntervalStatus_Type.__name__ = "Integer32"
_MwrPmAdvMeasIntervalStatus_Object = MibTableColumn
mwrPmAdvMeasIntervalStatus = _MwrPmAdvMeasIntervalStatus_Object(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 16, 2, 4, 1, 5),
    _MwrPmAdvMeasIntervalStatus_Type()
)
mwrPmAdvMeasIntervalStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwrPmAdvMeasIntervalStatus.setStatus("current")
_MwrPmAdvMeasTimeLength_Type = Integer32
_MwrPmAdvMeasTimeLength_Object = MibTableColumn
mwrPmAdvMeasTimeLength = _MwrPmAdvMeasTimeLength_Object(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 16, 2, 4, 1, 6),
    _MwrPmAdvMeasTimeLength_Type()
)
mwrPmAdvMeasTimeLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwrPmAdvMeasTimeLength.setStatus("current")
_MwrPmAdvTxCapPeak_Type = Integer32
_MwrPmAdvTxCapPeak_Object = MibTableColumn
mwrPmAdvTxCapPeak = _MwrPmAdvTxCapPeak_Object(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 16, 2, 4, 1, 7),
    _MwrPmAdvTxCapPeak_Type()
)
mwrPmAdvTxCapPeak.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwrPmAdvTxCapPeak.setStatus("current")
_MwrPmAdvTxCapRatio_Type = Integer32
_MwrPmAdvTxCapRatio_Object = MibTableColumn
mwrPmAdvTxCapRatio = _MwrPmAdvTxCapRatio_Object(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 16, 2, 4, 1, 8),
    _MwrPmAdvTxCapRatio_Type()
)
mwrPmAdvTxCapRatio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwrPmAdvTxCapRatio.setStatus("current")
_MwrPmAdvTxCapAvg_Type = Integer32
_MwrPmAdvTxCapAvg_Object = MibTableColumn
mwrPmAdvTxCapAvg = _MwrPmAdvTxCapAvg_Object(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 16, 2, 4, 1, 9),
    _MwrPmAdvTxCapAvg_Type()
)
mwrPmAdvTxCapAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwrPmAdvTxCapAvg.setStatus("current")
_MwrPmAdvTxCapAvgRatio_Type = Integer32
_MwrPmAdvTxCapAvgRatio_Object = MibTableColumn
mwrPmAdvTxCapAvgRatio = _MwrPmAdvTxCapAvgRatio_Object(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 16, 2, 4, 1, 10),
    _MwrPmAdvTxCapAvgRatio_Type()
)
mwrPmAdvTxCapAvgRatio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwrPmAdvTxCapAvgRatio.setStatus("current")
_MwrPmAdvTxCapHits_Type = Integer32
_MwrPmAdvTxCapHits_Object = MibTableColumn
mwrPmAdvTxCapHits = _MwrPmAdvTxCapHits_Object(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 16, 2, 4, 1, 11),
    _MwrPmAdvTxCapHits_Type()
)
mwrPmAdvTxCapHits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwrPmAdvTxCapHits.setStatus("current")
_MwrPmAdvRxCapPeak_Type = Integer32
_MwrPmAdvRxCapPeak_Object = MibTableColumn
mwrPmAdvRxCapPeak = _MwrPmAdvRxCapPeak_Object(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 16, 2, 4, 1, 12),
    _MwrPmAdvRxCapPeak_Type()
)
mwrPmAdvRxCapPeak.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwrPmAdvRxCapPeak.setStatus("current")
_MwrPmAdvRxCapRatio_Type = Integer32
_MwrPmAdvRxCapRatio_Object = MibTableColumn
mwrPmAdvRxCapRatio = _MwrPmAdvRxCapRatio_Object(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 16, 2, 4, 1, 13),
    _MwrPmAdvRxCapRatio_Type()
)
mwrPmAdvRxCapRatio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwrPmAdvRxCapRatio.setStatus("current")
_MwrPmAdvRxCapAvg_Type = Integer32
_MwrPmAdvRxCapAvg_Object = MibTableColumn
mwrPmAdvRxCapAvg = _MwrPmAdvRxCapAvg_Object(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 16, 2, 4, 1, 14),
    _MwrPmAdvRxCapAvg_Type()
)
mwrPmAdvRxCapAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwrPmAdvRxCapAvg.setStatus("current")
_MwrPmAdvRxCapHits_Type = Integer32
_MwrPmAdvRxCapHits_Object = MibTableColumn
mwrPmAdvRxCapHits = _MwrPmAdvRxCapHits_Object(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 16, 2, 4, 1, 15),
    _MwrPmAdvRxCapHits_Type()
)
mwrPmAdvRxCapHits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwrPmAdvRxCapHits.setStatus("current")
_MwrPMNotifications_ObjectIdentity = ObjectIdentity
mwrPMNotifications = _MwrPMNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 16, 3)
)
_MwrUserMgmt_ObjectIdentity = ObjectIdentity
mwrUserMgmt = _MwrUserMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 17)
)
_MwrUserConfiguration_ObjectIdentity = ObjectIdentity
mwrUserConfiguration = _MwrUserConfiguration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 17, 1)
)
_MwrUserStatus_ObjectIdentity = ObjectIdentity
mwrUserStatus = _MwrUserStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 17, 2)
)
_MwrUserSessionTable_Object = MibTable
mwrUserSessionTable = _MwrUserSessionTable_Object(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 17, 2, 1)
)
if mibBuilder.loadTexts:
    mwrUserSessionTable.setStatus("current")
_MwrUserSessionEntry_Object = MibTableRow
mwrUserSessionEntry = _MwrUserSessionEntry_Object(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 17, 2, 1, 1)
)
mwrUserSessionEntry.setIndexNames(
    (0, "MWR-ETHERNET-MIB", "mwrUserIndex"),
)
if mibBuilder.loadTexts:
    mwrUserSessionEntry.setStatus("current")


class _MwrUserIndex_Type(Integer32):
    """Custom type mwrUserIndex based on Integer32"""
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
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19,
              20)
        )
    )
    namedValues = NamedValues(
        *(("user1", 1),
          ("user2", 2),
          ("user3", 3),
          ("user4", 4),
          ("user5", 5),
          ("user6", 6),
          ("user7", 7),
          ("user8", 8),
          ("user9", 9),
          ("user10", 10),
          ("user11", 11),
          ("user12", 12),
          ("user13", 13),
          ("user14", 14),
          ("user15", 15),
          ("user16", 16),
          ("user17", 17),
          ("user18", 18),
          ("user19", 19),
          ("user20", 20))
    )


_MwrUserIndex_Type.__name__ = "Integer32"
_MwrUserIndex_Object = MibTableColumn
mwrUserIndex = _MwrUserIndex_Object(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 17, 2, 1, 1, 1),
    _MwrUserIndex_Type()
)
mwrUserIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mwrUserIndex.setStatus("current")


class _MwrUserName_Type(DisplayString):
    """Custom type mwrUserName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_MwrUserName_Type.__name__ = "DisplayString"
_MwrUserName_Object = MibTableColumn
mwrUserName = _MwrUserName_Object(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 17, 2, 1, 1, 2),
    _MwrUserName_Type()
)
mwrUserName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwrUserName.setStatus("current")
_MwrUserConnectionType_Type = DisplayString
_MwrUserConnectionType_Object = MibTableColumn
mwrUserConnectionType = _MwrUserConnectionType_Object(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 17, 2, 1, 1, 3),
    _MwrUserConnectionType_Type()
)
mwrUserConnectionType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwrUserConnectionType.setStatus("current")


class _MwrUserConnectionState_Type(Integer32):
    """Custom type mwrUserConnectionState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("informationNotAvailable", 1),
          ("sessionTerminated", 2),
          ("sessionInProgress", 3))
    )


_MwrUserConnectionState_Type.__name__ = "Integer32"
_MwrUserConnectionState_Object = MibTableColumn
mwrUserConnectionState = _MwrUserConnectionState_Object(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 17, 2, 1, 1, 4),
    _MwrUserConnectionState_Type()
)
mwrUserConnectionState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwrUserConnectionState.setStatus("current")
_MwrUserNotifications_ObjectIdentity = ObjectIdentity
mwrUserNotifications = _MwrUserNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 17, 3)
)

# Managed Objects groups


# Notification objects

mwrSysTcfInvalid = NotificationType(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 2, 5, 1)
)
mwrSysTcfInvalid.setObjects(
      *(("MWR-ETHERNET-MIB", "mwrEventConfigSeverity"),
        ("EQUIPMENT-COMMON-MIB", "equipmentAlarmActiveConditionId"),
        ("EQUIPMENT-COMMON-MIB", "equipmentTrapInfo"),
        ("EQUIPMENT-COMMON-MIB", "equipmentOutTrapsCounter"))
)
if mibBuilder.loadTexts:
    mwrSysTcfInvalid.setStatus(
        "current"
    )

mwrSysTempOutOfLimit = NotificationType(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 2, 5, 2)
)
mwrSysTempOutOfLimit.setObjects(
      *(("MWR-ETHERNET-MIB", "mwrEventConfigSeverity"),
        ("EQUIPMENT-COMMON-MIB", "equipmentAlarmActiveConditionId"),
        ("EQUIPMENT-COMMON-MIB", "equipmentTrapInfo"),
        ("EQUIPMENT-COMMON-MIB", "equipmentOutTrapsCounter"))
)
if mibBuilder.loadTexts:
    mwrSysTempOutOfLimit.setStatus(
        "current"
    )

mwrSynceLostLock = NotificationType(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 5, 3, 1)
)
mwrSynceLostLock.setObjects(
      *(("MWR-ETHERNET-MIB", "mwrEventConfigSeverity"),
        ("EQUIPMENT-COMMON-MIB", "equipmentAlarmActiveConditionId"),
        ("EQUIPMENT-COMMON-MIB", "equipmentTrapInfo"),
        ("EQUIPMENT-COMMON-MIB", "equipmentOutTrapsCounter"))
)
if mibBuilder.loadTexts:
    mwrSynceLostLock.setStatus(
        "current"
    )

mwrSynceSecondarySourceInUse = NotificationType(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 5, 3, 2)
)
mwrSynceSecondarySourceInUse.setObjects(
      *(("MWR-ETHERNET-MIB", "mwrEventConfigSeverity"),
        ("EQUIPMENT-COMMON-MIB", "equipmentAlarmActiveConditionId"),
        ("EQUIPMENT-COMMON-MIB", "equipmentTrapInfo"),
        ("EQUIPMENT-COMMON-MIB", "equipmentOutTrapsCounter"))
)
if mibBuilder.loadTexts:
    mwrSynceSecondarySourceInUse.setStatus(
        "current"
    )

mwrSynceConfigMismatch = NotificationType(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 5, 3, 3)
)
mwrSynceConfigMismatch.setObjects(
      *(("MWR-ETHERNET-MIB", "mwrEventConfigSeverity"),
        ("MWR-ETHERNET-MIB", "mwrEventInstanceIndex"),
        ("EQUIPMENT-COMMON-MIB", "equipmentAlarmActiveConditionId"),
        ("EQUIPMENT-COMMON-MIB", "equipmentTrapInfo"),
        ("EQUIPMENT-COMMON-MIB", "equipmentOutTrapsCounter"))
)
if mibBuilder.loadTexts:
    mwrSynceConfigMismatch.setStatus(
        "current"
    )

mwrSntpServerUnreachable = NotificationType(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 6, 4, 1)
)
mwrSntpServerUnreachable.setObjects(
      *(("MWR-ETHERNET-MIB", "mwrEventConfigSeverity"),
        ("EQUIPMENT-COMMON-MIB", "equipmentAlarmActiveConditionId"),
        ("EQUIPMENT-COMMON-MIB", "equipmentTrapInfo"),
        ("EQUIPMENT-COMMON-MIB", "equipmentOutTrapsCounter"))
)
if mibBuilder.loadTexts:
    mwrSntpServerUnreachable.setStatus(
        "current"
    )

mwrSystemTimeCorrected = NotificationType(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 6, 4, 2)
)
mwrSystemTimeCorrected.setObjects(
      *(("MWR-ETHERNET-MIB", "mwrEventConfigSeverity"),
        ("MWR-ETHERNET-MIB", "mwrTimingLastDateTimeChanged"),
        ("MWR-ETHERNET-MIB", "mwrTimingLastTimeAdjustment"),
        ("EQUIPMENT-COMMON-MIB", "equipmentAlarmActiveConditionId"),
        ("EQUIPMENT-COMMON-MIB", "equipmentTrapInfo"),
        ("EQUIPMENT-COMMON-MIB", "equipmentOutTrapsCounter"))
)
if mibBuilder.loadTexts:
    mwrSystemTimeCorrected.setStatus(
        "current"
    )

mwrDroppedPktsThreshold = NotificationType(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 9, 4, 1)
)
mwrDroppedPktsThreshold.setObjects(
      *(("MWR-ETHERNET-MIB", "mwrEventConfigSeverity"),
        ("MWR-ETHERNET-MIB", "mwrPortThresholdAlarmIndex"),
        ("EQUIPMENT-COMMON-MIB", "equipmentAlarmActiveConditionId"),
        ("EQUIPMENT-COMMON-MIB", "equipmentTrapInfo"),
        ("EQUIPMENT-COMMON-MIB", "equipmentOutTrapsCounter"))
)
if mibBuilder.loadTexts:
    mwrDroppedPktsThreshold.setStatus(
        "current"
    )

mwrRadioQDroppedPktsThreshold = NotificationType(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 9, 4, 2)
)
mwrRadioQDroppedPktsThreshold.setObjects(
      *(("MWR-ETHERNET-MIB", "mwrEventConfigSeverity"),
        ("MWR-ETHERNET-MIB", "mwrRadioQThresholdAlarmIndex"),
        ("EQUIPMENT-COMMON-MIB", "equipmentAlarmActiveConditionId"),
        ("EQUIPMENT-COMMON-MIB", "equipmentTrapInfo"),
        ("EQUIPMENT-COMMON-MIB", "equipmentOutTrapsCounter"))
)
if mibBuilder.loadTexts:
    mwrRadioQDroppedPktsThreshold.setStatus(
        "current"
    )

mwrRadioQDepthThreshold = NotificationType(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 9, 4, 3)
)
mwrRadioQDepthThreshold.setObjects(
      *(("MWR-ETHERNET-MIB", "mwrEventConfigSeverity"),
        ("MWR-ETHERNET-MIB", "mwrRadioQThresholdAlarmIndex"),
        ("EQUIPMENT-COMMON-MIB", "equipmentAlarmActiveConditionId"),
        ("EQUIPMENT-COMMON-MIB", "equipmentTrapInfo"),
        ("EQUIPMENT-COMMON-MIB", "equipmentOutTrapsCounter"))
)
if mibBuilder.loadTexts:
    mwrRadioQDepthThreshold.setStatus(
        "current"
    )

mwrOutBWUtilizationThreshold = NotificationType(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 9, 4, 4)
)
mwrOutBWUtilizationThreshold.setObjects(
      *(("MWR-ETHERNET-MIB", "mwrEventConfigSeverity"),
        ("MWR-ETHERNET-MIB", "mwrPortThresholdAlarmIndex"),
        ("EQUIPMENT-COMMON-MIB", "equipmentAlarmActiveConditionId"),
        ("EQUIPMENT-COMMON-MIB", "equipmentTrapInfo"),
        ("EQUIPMENT-COMMON-MIB", "equipmentOutTrapsCounter"))
)
if mibBuilder.loadTexts:
    mwrOutBWUtilizationThreshold.setStatus(
        "current"
    )

mwrThroughputThreshold = NotificationType(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 9, 4, 5)
)
mwrThroughputThreshold.setObjects(
      *(("MWR-ETHERNET-MIB", "mwrEventConfigSeverity"),
        ("MWR-ETHERNET-MIB", "mwrPortThresholdAlarmIndex"),
        ("EQUIPMENT-COMMON-MIB", "equipmentAlarmActiveConditionId"),
        ("EQUIPMENT-COMMON-MIB", "equipmentTrapInfo"),
        ("EQUIPMENT-COMMON-MIB", "equipmentOutTrapsCounter"))
)
if mibBuilder.loadTexts:
    mwrThroughputThreshold.setStatus(
        "current"
    )

mwrAcmConfigMismatch = NotificationType(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 10, 4, 1)
)
mwrAcmConfigMismatch.setObjects(
      *(("MWR-ETHERNET-MIB", "mwrEventConfigSeverity"),
        ("MWR-ETHERNET-MIB", "mwrEventInstanceIndex"),
        ("EQUIPMENT-COMMON-MIB", "equipmentAlarmActiveConditionId"),
        ("EQUIPMENT-COMMON-MIB", "equipmentTrapInfo"),
        ("EQUIPMENT-COMMON-MIB", "equipmentOutTrapsCounter"))
)
if mibBuilder.loadTexts:
    mwrAcmConfigMismatch.setStatus(
        "current"
    )

mwrAcmProfileLowered = NotificationType(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 10, 4, 2)
)
mwrAcmProfileLowered.setObjects(
      *(("MWR-ETHERNET-MIB", "mwrEventConfigSeverity"),
        ("MWR-ETHERNET-MIB", "mwrAcmStatusIndex"),
        ("EQUIPMENT-COMMON-MIB", "equipmentAlarmActiveConditionId"),
        ("EQUIPMENT-COMMON-MIB", "equipmentTrapInfo"),
        ("EQUIPMENT-COMMON-MIB", "equipmentOutTrapsCounter"))
)
if mibBuilder.loadTexts:
    mwrAcmProfileLowered.setStatus(
        "current"
    )

mwrAcmProfileChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 10, 4, 3)
)
mwrAcmProfileChanged.setObjects(
      *(("MWR-ETHERNET-MIB", "mwrEventConfigSeverity"),
        ("MWR-ETHERNET-MIB", "mwrAcmStatusIndex"),
        ("EQUIPMENT-COMMON-MIB", "equipmentAlarmActiveConditionId"),
        ("EQUIPMENT-COMMON-MIB", "equipmentTrapInfo"),
        ("EQUIPMENT-COMMON-MIB", "equipmentOutTrapsCounter"))
)
if mibBuilder.loadTexts:
    mwrAcmProfileChanged.setStatus(
        "current"
    )

mwrAtpcConfigMismatch = NotificationType(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 11, 3, 1)
)
mwrAtpcConfigMismatch.setObjects(
      *(("MWR-ETHERNET-MIB", "mwrEventConfigSeverity"),
        ("MWR-ETHERNET-MIB", "mwrEventInstanceIndex"),
        ("EQUIPMENT-COMMON-MIB", "equipmentAlarmActiveConditionId"),
        ("EQUIPMENT-COMMON-MIB", "equipmentTrapInfo"),
        ("EQUIPMENT-COMMON-MIB", "equipmentOutTrapsCounter"))
)
if mibBuilder.loadTexts:
    mwrAtpcConfigMismatch.setStatus(
        "current"
    )

mwrAtpcAutoDisabled = NotificationType(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 11, 3, 2)
)
mwrAtpcAutoDisabled.setObjects(
      *(("MWR-ETHERNET-MIB", "mwrEventConfigSeverity"),
        ("MWR-ETHERNET-MIB", "mwrAtpcStatusIndex"),
        ("EQUIPMENT-COMMON-MIB", "equipmentAlarmActiveConditionId"),
        ("EQUIPMENT-COMMON-MIB", "equipmentTrapInfo"),
        ("EQUIPMENT-COMMON-MIB", "equipmentOutTrapsCounter"))
)
if mibBuilder.loadTexts:
    mwrAtpcAutoDisabled.setStatus(
        "current"
    )

mwrUserSession = NotificationType(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 17, 3, 1)
)
mwrUserSession.setObjects(
      *(("MWR-ETHERNET-MIB", "mwrEventConfigSeverity"),
        ("MWR-ETHERNET-MIB", "mwrUserName"),
        ("MWR-ETHERNET-MIB", "mwrUserConnectionType"),
        ("EQUIPMENT-COMMON-MIB", "equipmentAlarmActiveConditionId"),
        ("EQUIPMENT-COMMON-MIB", "equipmentTrapInfo"),
        ("EQUIPMENT-COMMON-MIB", "equipmentOutTrapsCounter"))
)
if mibBuilder.loadTexts:
    mwrUserSession.setStatus(
        "current"
    )

mwrUserLoginFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 17, 3, 2)
)
mwrUserLoginFailed.setObjects(
      *(("MWR-ETHERNET-MIB", "mwrEventConfigSeverity"),
        ("MWR-ETHERNET-MIB", "mwrUserName"),
        ("MWR-ETHERNET-MIB", "mwrUserConnectionType"),
        ("EQUIPMENT-COMMON-MIB", "equipmentAlarmActiveConditionId"),
        ("EQUIPMENT-COMMON-MIB", "equipmentTrapInfo"),
        ("EQUIPMENT-COMMON-MIB", "equipmentOutTrapsCounter"))
)
if mibBuilder.loadTexts:
    mwrUserLoginFailed.setStatus(
        "current"
    )

mwrUserAccountChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 17, 3, 3)
)
mwrUserAccountChanged.setObjects(
      *(("MWR-ETHERNET-MIB", "mwrEventConfigSeverity"),
        ("MWR-ETHERNET-MIB", "mwrUserName"),
        ("EQUIPMENT-COMMON-MIB", "equipmentAlarmActiveConditionId"),
        ("EQUIPMENT-COMMON-MIB", "equipmentTrapInfo"),
        ("EQUIPMENT-COMMON-MIB", "equipmentOutTrapsCounter"))
)
if mibBuilder.loadTexts:
    mwrUserAccountChanged.setStatus(
        "current"
    )

mwrUserPasswordChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 17, 3, 4)
)
mwrUserPasswordChanged.setObjects(
      *(("MWR-ETHERNET-MIB", "mwrEventConfigSeverity"),
        ("MWR-ETHERNET-MIB", "mwrUserName"),
        ("EQUIPMENT-COMMON-MIB", "equipmentAlarmActiveConditionId"),
        ("EQUIPMENT-COMMON-MIB", "equipmentTrapInfo"),
        ("EQUIPMENT-COMMON-MIB", "equipmentOutTrapsCounter"))
)
if mibBuilder.loadTexts:
    mwrUserPasswordChanged.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "MWR-ETHERNET-MIB",
    **{"ClassType": ClassType,
       "FlowType": FlowType,
       "PMIntervalType": PMIntervalType,
       "PortType": PortType,
       "QueueType": QueueType,
       "RadioInstanceType": RadioInstanceType,
       "mwrPlatformObjId": mwrPlatformObjId,
       "mwrEbandObjId": mwrEbandObjId,
       "mwrEnhancedObjId": mwrEnhancedObjId,
       "mwrSystem": mwrSystem,
       "mwrSystemConfigurations": mwrSystemConfigurations,
       "mwrSystemType": mwrSystemType,
       "mwrPacketSwitchMode": mwrPacketSwitchMode,
       "mwrSysSpeed": mwrSysSpeed,
       "mwrSystemCurrentSpeed": mwrSystemCurrentSpeed,
       "mwrSystemStatus": mwrSystemStatus,
       "mwrSystemOperStatus": mwrSystemOperStatus,
       "mwrSystemFaultSeverity": mwrSystemFaultSeverity,
       "mwrSystemTemperature": mwrSystemTemperature,
       "mwrPlatformType": mwrPlatformType,
       "mwrPacketSwitchModeStatus": mwrPacketSwitchModeStatus,
       "mwrSystemTypeStatus": mwrSystemTypeStatus,
       "mwrSystemCommands": mwrSystemCommands,
       "mwrResetSystem": mwrResetSystem,
       "mwrSaveConfig": mwrSaveConfig,
       "mwrDeleteConfig": mwrDeleteConfig,
       "mwrSystemInventory": mwrSystemInventory,
       "mwrHwInventory": mwrHwInventory,
       "mwrMacAddress": mwrMacAddress,
       "mwrTargetCfgFilePartNumber": mwrTargetCfgFilePartNumber,
       "mwrUnitSerialNo": mwrUnitSerialNo,
       "mwrUnitAssemblyNo": mwrUnitAssemblyNo,
       "mwrBasebandSerialNo": mwrBasebandSerialNo,
       "mwrBasebandAssemblyNo": mwrBasebandAssemblyNo,
       "mwrPsuSerialNo": mwrPsuSerialNo,
       "mwrPsuAssemblyNo": mwrPsuAssemblyNo,
       "mwrRfSerialNo": mwrRfSerialNo,
       "mwrRfAssemblyNo": mwrRfAssemblyNo,
       "mwrRfRevisionNo": mwrRfRevisionNo,
       "mwrDiplexerSerialNo": mwrDiplexerSerialNo,
       "mwrDiplexerAssemblyNo": mwrDiplexerAssemblyNo,
       "mwrSystemCleiNo": mwrSystemCleiNo,
       "mwrSwInventory": mwrSwInventory,
       "mwrSwInventoryTable": mwrSwInventoryTable,
       "mwrSwInventoryEntry": mwrSwInventoryEntry,
       "mwrSwInvBank": mwrSwInvBank,
       "mwrSwInvStatus": mwrSwInvStatus,
       "mwrSwInvOmniRelease": mwrSwInvOmniRelease,
       "mwrSwInvTargetConfFileVersion": mwrSwInvTargetConfFileVersion,
       "mwrSwInvMibVersion": mwrSwInvMibVersion,
       "mwrSwInvSecurityVersion": mwrSwInvSecurityVersion,
       "mwrSystemNotifications": mwrSystemNotifications,
       "mwrSysTcfInvalid": mwrSysTcfInvalid,
       "mwrSysTempOutOfLimit": mwrSysTempOutOfLimit,
       "mwrSoftware": mwrSoftware,
       "mwrSoftwareConfigurations": mwrSoftwareConfigurations,
       "mwrSoftwareStatus": mwrSoftwareStatus,
       "mwrSwBackupBankStatus": mwrSwBackupBankStatus,
       "mwrSoftwareCommands": mwrSoftwareCommands,
       "mwrSwCommit": mwrSwCommit,
       "mwrSwSwitchBanks": mwrSwSwitchBanks,
       "mwrSoftwareNotifications": mwrSoftwareNotifications,
       "mwrLicensing": mwrLicensing,
       "mwrLicensingConfigurations": mwrLicensingConfigurations,
       "mwrLicenseUpgradeKey": mwrLicenseUpgradeKey,
       "mwrLicensingStatus": mwrLicensingStatus,
       "mwrLicenseCount": mwrLicenseCount,
       "mwrLicensedSpeed": mwrLicensedSpeed,
       "mwrLicenseFeaturesTable": mwrLicenseFeaturesTable,
       "mwrLicenseFeaturesEntry": mwrLicenseFeaturesEntry,
       "mwrLicenseFeatureIndex": mwrLicenseFeatureIndex,
       "mwrLicenseFeatureId": mwrLicenseFeatureId,
       "mwrLicenseFeature": mwrLicenseFeature,
       "mwrLicenseFeatureStatus": mwrLicenseFeatureStatus,
       "mwrSyncE": mwrSyncE,
       "mwrSyncEConfigurations": mwrSyncEConfigurations,
       "mwrSyncEState": mwrSyncEState,
       "mwrSyncEPrimarySource": mwrSyncEPrimarySource,
       "mwrSyncESecondarySource": mwrSyncESecondarySource,
       "mwrSyncEMemberPorts": mwrSyncEMemberPorts,
       "mwrSyncEForcedHoldover": mwrSyncEForcedHoldover,
       "mwrSyncERevertive": mwrSyncERevertive,
       "mwrSyncEWanderFilter": mwrSyncEWanderFilter,
       "mwrSyncEStatus": mwrSyncEStatus,
       "mwrSyncEClockSource": mwrSyncEClockSource,
       "mwrSyncEAcquisitionStatus": mwrSyncEAcquisitionStatus,
       "mwrSyncENotifications": mwrSyncENotifications,
       "mwrSynceLostLock": mwrSynceLostLock,
       "mwrSynceSecondarySourceInUse": mwrSynceSecondarySourceInUse,
       "mwrSynceConfigMismatch": mwrSynceConfigMismatch,
       "mwrTiming": mwrTiming,
       "mwrTimingConfigurations": mwrTimingConfigurations,
       "mwrDateTime": mwrDateTime,
       "mwrSntpEnable": mwrSntpEnable,
       "mwrSntpOffset": mwrSntpOffset,
       "mwrSntpServerTable": mwrSntpServerTable,
       "mwrSntpServerEntry": mwrSntpServerEntry,
       "mwrSntpServerIndex": mwrSntpServerIndex,
       "mwrSntpServerDomain": mwrSntpServerDomain,
       "mwrSntpServerAddress": mwrSntpServerAddress,
       "mwrSntpServerStatus": mwrSntpServerStatus,
       "mwrSntpServerStratum": mwrSntpServerStratum,
       "mwrTimingStatus": mwrTimingStatus,
       "mwrTimingLastDateTimeChanged": mwrTimingLastDateTimeChanged,
       "mwrTimingLastTimeAdjustment": mwrTimingLastTimeAdjustment,
       "mwrTimingCummulativeTimeChange": mwrTimingCummulativeTimeChange,
       "mwrTimingCommands": mwrTimingCommands,
       "mwrSntpRestoreDefault": mwrSntpRestoreDefault,
       "mwrTimingNotifications": mwrTimingNotifications,
       "mwrSntpServerUnreachable": mwrSntpServerUnreachable,
       "mwrSystemTimeCorrected": mwrSystemTimeCorrected,
       "mwrAAA": mwrAAA,
       "mwrAAAConfigurations": mwrAAAConfigurations,
       "mwrAAAUserAuthentication": mwrAAAUserAuthentication,
       "mwrRadiusConfigurations": mwrRadiusConfigurations,
       "mwrRadiusAdminUserStrict": mwrRadiusAdminUserStrict,
       "mwrRadiusServerTimeOut": mwrRadiusServerTimeOut,
       "mwrRadiusServerDeadTime": mwrRadiusServerDeadTime,
       "mwrRadiusServerReTransmit": mwrRadiusServerReTransmit,
       "mwrRadiusServerTable": mwrRadiusServerTable,
       "mwrRadiusServerEntry": mwrRadiusServerEntry,
       "mwrRadiusServerIndex": mwrRadiusServerIndex,
       "mwrRadiusCfgdHostDomain": mwrRadiusCfgdHostDomain,
       "mwrRadiusCfgdHostAddress": mwrRadiusCfgdHostAddress,
       "mwrRadiusCfgdHostKey": mwrRadiusCfgdHostKey,
       "mwrNetworking": mwrNetworking,
       "mwrNetworkingConfigurations": mwrNetworkingConfigurations,
       "mwrNetMgmtPriority": mwrNetMgmtPriority,
       "mwrNetMgmtVlanPriority": mwrNetMgmtVlanPriority,
       "mwrNetMgmtDscp": mwrNetMgmtDscp,
       "mwrNetMgmtIpv4": mwrNetMgmtIpv4,
       "mwrIpv4Table": mwrIpv4Table,
       "mwrIpv4Entry": mwrIpv4Entry,
       "mwrIpv4Index": mwrIpv4Index,
       "mwrIpv4Address": mwrIpv4Address,
       "mwrIpv4SubnetMask": mwrIpv4SubnetMask,
       "mwrIpv4DefaultGateway": mwrIpv4DefaultGateway,
       "mwrIpv4RowStatus": mwrIpv4RowStatus,
       "mwrSecondaryGateway": mwrSecondaryGateway,
       "mwrNetMgmttIpv6": mwrNetMgmttIpv6,
       "mwrIpv6Table": mwrIpv6Table,
       "mwrIpv6Entry": mwrIpv6Entry,
       "mwrIpv6Index": mwrIpv6Index,
       "mwrIpv6Domain": mwrIpv6Domain,
       "mwrIpv6Address": mwrIpv6Address,
       "mwrIpv6Prefix": mwrIpv6Prefix,
       "mwrIpv6GatewayDomain": mwrIpv6GatewayDomain,
       "mwrIpv6GatewayAddress": mwrIpv6GatewayAddress,
       "mwrIpv6RowStatus": mwrIpv6RowStatus,
       "mwrSecondaryIpv6GatewayDomain": mwrSecondaryIpv6GatewayDomain,
       "mwrSecondaryIpv6GatewayAddress": mwrSecondaryIpv6GatewayAddress,
       "mwrUserInterfaceMgmt": mwrUserInterfaceMgmt,
       "mwrTelnetEnable": mwrTelnetEnable,
       "mwrSshEnable": mwrSshEnable,
       "mwrHttpEnable": mwrHttpEnable,
       "mwrHttpsEnable": mwrHttpsEnable,
       "mwrSnmpv1v2cEnable": mwrSnmpv1v2cEnable,
       "mwrFtpEnable": mwrFtpEnable,
       "mwrFileTransfer": mwrFileTransfer,
       "mwrFileXfrDirection": mwrFileXfrDirection,
       "mwrFileXfrTable": mwrFileXfrTable,
       "mwrFileXfrEntry": mwrFileXfrEntry,
       "mwrFileXfrSeqID": mwrFileXfrSeqID,
       "mwrFileXfrIdentifier": mwrFileXfrIdentifier,
       "mwrFileXfrName": mwrFileXfrName,
       "mwrFileXfrMode": mwrFileXfrMode,
       "mwrFileXfrServerDomain": mwrFileXfrServerDomain,
       "mwrFileXfrServerAddress": mwrFileXfrServerAddress,
       "mwrFileXfrClientDirection": mwrFileXfrClientDirection,
       "mwrFileXfrUserName": mwrFileXfrUserName,
       "mwrFileXfrPassword": mwrFileXfrPassword,
       "mwrFileXfrNumEntries": mwrFileXfrNumEntries,
       "mwrFileXfrStatus": mwrFileXfrStatus,
       "mwrFileXfrRowStatus": mwrFileXfrRowStatus,
       "mwrNetMgmtInterfaceTable": mwrNetMgmtInterfaceTable,
       "mwrNetMgmtInterfaceEntry": mwrNetMgmtInterfaceEntry,
       "mwrNetMgmtInterfaceIndex": mwrNetMgmtInterfaceIndex,
       "mwrNetMgmtVlanId": mwrNetMgmtVlanId,
       "mwrNetMgmtInterface1": mwrNetMgmtInterface1,
       "mwrNetMgmtInterface1Mode": mwrNetMgmtInterface1Mode,
       "mwrNetMgmtInterface1Tagged": mwrNetMgmtInterface1Tagged,
       "mwrNetMgmtInterface2": mwrNetMgmtInterface2,
       "mwrNetMgmtInterface2Mode": mwrNetMgmtInterface2Mode,
       "mwrNetMgmtInterface2Tagged": mwrNetMgmtInterface2Tagged,
       "mwrNetMgmtInterface3": mwrNetMgmtInterface3,
       "mwrNetMgmtInterface3Mode": mwrNetMgmtInterface3Mode,
       "mwrNetMgmtInterface3Tagged": mwrNetMgmtInterface3Tagged,
       "mwrNetMgmtInterface4": mwrNetMgmtInterface4,
       "mwrNetMgmtInterface4Mode": mwrNetMgmtInterface4Mode,
       "mwrNetMgmtInterface4Tagged": mwrNetMgmtInterface4Tagged,
       "mwrNetMgmtInterfaceRowStatus": mwrNetMgmtInterfaceRowStatus,
       "mwrNetworkingStatus": mwrNetworkingStatus,
       "mwrMaintenanceIpv4": mwrMaintenanceIpv4,
       "mwrMaintenanceIpv4Address": mwrMaintenanceIpv4Address,
       "mwrMaintenanceSubnetMask": mwrMaintenanceSubnetMask,
       "mwrActiveIpv4Gateway": mwrActiveIpv4Gateway,
       "mwrMaintenanceIpv6": mwrMaintenanceIpv6,
       "mwrIpv6LinkLocalIPrefix": mwrIpv6LinkLocalIPrefix,
       "mwrIpv6LinkLocalAddress": mwrIpv6LinkLocalAddress,
       "mwrActiveIpv6Gateway": mwrActiveIpv6Gateway,
       "mwrPeerNetworkingStatus": mwrPeerNetworkingStatus,
       "mwrPeerMacAddress": mwrPeerMacAddress,
       "mwrPeerIpv4Address": mwrPeerIpv4Address,
       "mwrPeerIpv4SubnetMask": mwrPeerIpv4SubnetMask,
       "mwrPeerIpv4DefaultGateway": mwrPeerIpv4DefaultGateway,
       "mwrPeerIpv6Prefix": mwrPeerIpv6Prefix,
       "mwrPeerIpv6Domain": mwrPeerIpv6Domain,
       "mwrPeerIpv6Address": mwrPeerIpv6Address,
       "mwrPeerIpv6GatewayDomain": mwrPeerIpv6GatewayDomain,
       "mwrPeerIpv6GatewayAddress": mwrPeerIpv6GatewayAddress,
       "mwrPeerVlanId": mwrPeerVlanId,
       "mwrPeerVlanPriority": mwrPeerVlanPriority,
       "mwrPeerDscp": mwrPeerDscp,
       "mwrNetworkingNotifications": mwrNetworkingNotifications,
       "mwrEthernet": mwrEthernet,
       "mwrEthernetConfigurations": mwrEthernetConfigurations,
       "mwrQos": mwrQos,
       "mwrQosState": mwrQosState,
       "mwrCosSource": mwrCosSource,
       "mwrOuterTpid": mwrOuterTpid,
       "mwrInnerTpid": mwrInnerTpid,
       "mwrCosTable": mwrCosTable,
       "mwrCosEntry": mwrCosEntry,
       "mwrCosIndex": mwrCosIndex,
       "mwrCos0": mwrCos0,
       "mwrCos1": mwrCos1,
       "mwrCos2": mwrCos2,
       "mwrCos3": mwrCos3,
       "mwrCos4": mwrCos4,
       "mwrCos5": mwrCos5,
       "mwrCos6": mwrCos6,
       "mwrCos7": mwrCos7,
       "mwrCosRowStatus": mwrCosRowStatus,
       "mwrCosDefValueTable": mwrCosDefValueTable,
       "mwrCosDefValueEntry": mwrCosDefValueEntry,
       "mwrCosDefValueIndex": mwrCosDefValueIndex,
       "mwrCosDefValue": mwrCosDefValue,
       "mwrCirQTable": mwrCirQTable,
       "mwrCirQEntry": mwrCirQEntry,
       "mwrCirQIndex": mwrCirQIndex,
       "mwrCirQ1": mwrCirQ1,
       "mwrCirQ2": mwrCirQ2,
       "mwrCirQ3": mwrCirQ3,
       "mwrCirQ4": mwrCirQ4,
       "mwrCirQ5": mwrCirQ5,
       "mwrCirQ6": mwrCirQ6,
       "mwrCirQ7": mwrCirQ7,
       "mwrCirQ8": mwrCirQ8,
       "mwrCirQRowStatus": mwrCirQRowStatus,
       "mwrCbsQTable": mwrCbsQTable,
       "mwrCbsQEntry": mwrCbsQEntry,
       "mwrCbsQIndex": mwrCbsQIndex,
       "mwrCbsQ1": mwrCbsQ1,
       "mwrCbsQ2": mwrCbsQ2,
       "mwrCbsQ3": mwrCbsQ3,
       "mwrCbsQ4": mwrCbsQ4,
       "mwrCbsQ5": mwrCbsQ5,
       "mwrCbsQ6": mwrCbsQ6,
       "mwrCbsQ7": mwrCbsQ7,
       "mwrCbsQ8": mwrCbsQ8,
       "mwrCbsQRowStatus": mwrCbsQRowStatus,
       "mwrWeightQTable": mwrWeightQTable,
       "mwrWeightQEntry": mwrWeightQEntry,
       "mwrWeightQIndex": mwrWeightQIndex,
       "mwrWeightQ1": mwrWeightQ1,
       "mwrWeightQ2": mwrWeightQ2,
       "mwrWeightQ3": mwrWeightQ3,
       "mwrWeightQ4": mwrWeightQ4,
       "mwrWeightQ5": mwrWeightQ5,
       "mwrWeightQ6": mwrWeightQ6,
       "mwrWeightQ7": mwrWeightQ7,
       "mwrWeightQ8": mwrWeightQ8,
       "mwrWeightQRowStatus": mwrWeightQRowStatus,
       "mwrQbsQTable": mwrQbsQTable,
       "mwrQbsQEntry": mwrQbsQEntry,
       "mwrQbsQIndex": mwrQbsQIndex,
       "mwrQbsQ1": mwrQbsQ1,
       "mwrQbsQ2": mwrQbsQ2,
       "mwrQbsQ3": mwrQbsQ3,
       "mwrQbsQ4": mwrQbsQ4,
       "mwrQbsQ5": mwrQbsQ5,
       "mwrQbsQ6": mwrQbsQ6,
       "mwrQbsQ7": mwrQbsQ7,
       "mwrQbsQ8": mwrQbsQ8,
       "mwrQbsQRowStatus": mwrQbsQRowStatus,
       "mwrPolicyQTable": mwrPolicyQTable,
       "mwrPolicyQEntry": mwrPolicyQEntry,
       "mwrPolicyQIndex": mwrPolicyQIndex,
       "mwrPolicyQ1": mwrPolicyQ1,
       "mwrPolicyQ2": mwrPolicyQ2,
       "mwrPolicyQ3": mwrPolicyQ3,
       "mwrPolicyQ4": mwrPolicyQ4,
       "mwrPolicyQ5": mwrPolicyQ5,
       "mwrPolicyQ6": mwrPolicyQ6,
       "mwrPolicyQ7": mwrPolicyQ7,
       "mwrPolicyQ8": mwrPolicyQ8,
       "mwrPolicyQRowStatus": mwrPolicyQRowStatus,
       "mwrUserClassTable": mwrUserClassTable,
       "mwrUserClassEntry": mwrUserClassEntry,
       "mwrUserClassIndex": mwrUserClassIndex,
       "mwrUserClassOffset": mwrUserClassOffset,
       "mwrUserClassValue": mwrUserClassValue,
       "mwrUserClassMask": mwrUserClassMask,
       "mwrUserFlowTable": mwrUserFlowTable,
       "mwrUserFlowEntry": mwrUserFlowEntry,
       "mwrUserFlowIndex": mwrUserFlowIndex,
       "mwrUserFlowFilter": mwrUserFlowFilter,
       "mwrUserFlowMappingTable": mwrUserFlowMappingTable,
       "mwrUserFlowMappingEntry": mwrUserFlowMappingEntry,
       "mwrUserFlowMappingIndex": mwrUserFlowMappingIndex,
       "mwrUserFlowMappingState": mwrUserFlowMappingState,
       "mwrUserFlowMapping1Q": mwrUserFlowMapping1Q,
       "mwrUserFlowMapping2Q": mwrUserFlowMapping2Q,
       "mwrUserFlowMapping3Q": mwrUserFlowMapping3Q,
       "mwrUserFlowMapping4Q": mwrUserFlowMapping4Q,
       "mwrUserFlowMappingRowStatus": mwrUserFlowMappingRowStatus,
       "mwrUserFlowMappingBridgeModeTable": mwrUserFlowMappingBridgeModeTable,
       "mwrUserFlowMappingBridgeModeEntry": mwrUserFlowMappingBridgeModeEntry,
       "mwrUserFlowMappingBridgeModeIndex": mwrUserFlowMappingBridgeModeIndex,
       "mwrUserFlowMappingBridgeModeState": mwrUserFlowMappingBridgeModeState,
       "mwrUserFlowMappingBridgeModeQ": mwrUserFlowMappingBridgeModeQ,
       "mwrUserFlowMappingBridgeModeRowStatus": mwrUserFlowMappingBridgeModeRowStatus,
       "mwrEthThresholdAlarm": mwrEthThresholdAlarm,
       "mwrPortThresholdAlarmTable": mwrPortThresholdAlarmTable,
       "mwrPortThresholdAlarmEntry": mwrPortThresholdAlarmEntry,
       "mwrPortThresholdAlarmIndex": mwrPortThresholdAlarmIndex,
       "mwrDroppedPktsThresholdParams": mwrDroppedPktsThresholdParams,
       "mwrOutBWUtilizationThresholdParams": mwrOutBWUtilizationThresholdParams,
       "mwrThroughputThresholdParams": mwrThroughputThresholdParams,
       "mwrRadioQThresholdAlarmTable": mwrRadioQThresholdAlarmTable,
       "mwrRadioQThresholdAlarmEntry": mwrRadioQThresholdAlarmEntry,
       "mwrRadioQThresholdAlarmIndex": mwrRadioQThresholdAlarmIndex,
       "mwrRadioQDepthThresholdParams": mwrRadioQDepthThresholdParams,
       "mwrRadioQDroppedPktsThresholdParams": mwrRadioQDroppedPktsThresholdParams,
       "mwrEthernetStatus": mwrEthernetStatus,
       "mwrEthernetPerformance": mwrEthernetPerformance,
       "mwrEnetPerfPortStatsTable": mwrEnetPerfPortStatsTable,
       "mwrEnetPerfPortStatsEntry": mwrEnetPerfPortStatsEntry,
       "mwrEnetPortStatsIndex": mwrEnetPortStatsIndex,
       "mwrPortStatsInOctet": mwrPortStatsInOctet,
       "mwrPortStatsInGoodPkts": mwrPortStatsInGoodPkts,
       "mwrPortStatsInErrPkts": mwrPortStatsInErrPkts,
       "mwrPortStatsInDiscardPkts": mwrPortStatsInDiscardPkts,
       "mwrPortStatsOutOctets": mwrPortStatsOutOctets,
       "mwrPortStatsOutGoodPkts": mwrPortStatsOutGoodPkts,
       "mwrPortStatsOutErrPkts": mwrPortStatsOutErrPkts,
       "mwrPortStatsOutDiscardPkts": mwrPortStatsOutDiscardPkts,
       "mwrPortStatsOutBwUtilization": mwrPortStatsOutBwUtilization,
       "mwrPortStatsInBwUtilization": mwrPortStatsInBwUtilization,
       "mwrPortStatsInDataRate": mwrPortStatsInDataRate,
       "mwrPortStatsThroughput": mwrPortStatsThroughput,
       "mwrEnetPerfPortStats32BitTable": mwrEnetPerfPortStats32BitTable,
       "mwrEnetPerfPortStats32BitEntry": mwrEnetPerfPortStats32BitEntry,
       "mwrPortStats32BitIndex": mwrPortStats32BitIndex,
       "mwrPortStatsInOctet32Bit": mwrPortStatsInOctet32Bit,
       "mwrPortStatsInGoodPkts32Bit": mwrPortStatsInGoodPkts32Bit,
       "mwrPortStatsInErrPkts32Bit": mwrPortStatsInErrPkts32Bit,
       "mwrPortStatsInDiscardPkts32Bit": mwrPortStatsInDiscardPkts32Bit,
       "mwrPortStatsOutOctets32Bit": mwrPortStatsOutOctets32Bit,
       "mwrPortStatsOutGoodPkts32Bit": mwrPortStatsOutGoodPkts32Bit,
       "mwrPortStatsOutErrPkts32Bit": mwrPortStatsOutErrPkts32Bit,
       "mwrPortStatsOutDiscardPkts32Bit": mwrPortStatsOutDiscardPkts32Bit,
       "mwrEnetPerfRadioQStatsTable": mwrEnetPerfRadioQStatsTable,
       "mwrEnetPerfRadioQStatsEntry": mwrEnetPerfRadioQStatsEntry,
       "mwrRadioQStatsIndex": mwrRadioQStatsIndex,
       "mwrRadioQStatsInGoodPkts": mwrRadioQStatsInGoodPkts,
       "mwrRadioQStatsInDiscardPkts": mwrRadioQStatsInDiscardPkts,
       "mwrRadioQStatsOutBwUtilization": mwrRadioQStatsOutBwUtilization,
       "mwrRadioQStatsInDataRate": mwrRadioQStatsInDataRate,
       "mwrRadioQStatsThroughput": mwrRadioQStatsThroughput,
       "mwrEnetPerfRadioQStats32BitTable": mwrEnetPerfRadioQStats32BitTable,
       "mwrEnetPerfRadioQStats32BitEntry": mwrEnetPerfRadioQStats32BitEntry,
       "mwrRadioQStats32BitIndex": mwrRadioQStats32BitIndex,
       "mwrRadioQStatsInGoodPkts32Bit": mwrRadioQStatsInGoodPkts32Bit,
       "mwrRadioQStatsDiscardPkts32Bit": mwrRadioQStatsDiscardPkts32Bit,
       "mwrEthernetNotifications": mwrEthernetNotifications,
       "mwrDroppedPktsThreshold": mwrDroppedPktsThreshold,
       "mwrRadioQDroppedPktsThreshold": mwrRadioQDroppedPktsThreshold,
       "mwrRadioQDepthThreshold": mwrRadioQDepthThreshold,
       "mwrOutBWUtilizationThreshold": mwrOutBWUtilizationThreshold,
       "mwrThroughputThreshold": mwrThroughputThreshold,
       "mwrAcm": mwrAcm,
       "mwrAcmConfigurations": mwrAcmConfigurations,
       "mwrAcmManualMode": mwrAcmManualMode,
       "mwrAcmState": mwrAcmState,
       "mwrAcmWaitToRestore": mwrAcmWaitToRestore,
       "mwrAcmModeTable": mwrAcmModeTable,
       "mwrAcmModeEntry": mwrAcmModeEntry,
       "mwrAcmModeIndex": mwrAcmModeIndex,
       "mwrAcmTxProfileName": mwrAcmTxProfileName,
       "mwrAcmTxProfileRange": mwrAcmTxProfileRange,
       "mwrAcmStatus": mwrAcmStatus,
       "mwrAcmStatusTable": mwrAcmStatusTable,
       "mwrAcmStatusEntry": mwrAcmStatusEntry,
       "mwrAcmStatusIndex": mwrAcmStatusIndex,
       "mwrAcmActualTxProfile": mwrAcmActualTxProfile,
       "mwrAcmDiagnostics": mwrAcmDiagnostics,
       "mwrAcmDiagTable": mwrAcmDiagTable,
       "mwrAcmDiagEntry": mwrAcmDiagEntry,
       "mwrAcmDiagIndex": mwrAcmDiagIndex,
       "mwrAcmDiagnose": mwrAcmDiagnose,
       "mwrAcmDiagnosticResult": mwrAcmDiagnosticResult,
       "mwrAcmNotifications": mwrAcmNotifications,
       "mwrAcmConfigMismatch": mwrAcmConfigMismatch,
       "mwrAcmProfileLowered": mwrAcmProfileLowered,
       "mwrAcmProfileChanged": mwrAcmProfileChanged,
       "mwrAtpc": mwrAtpc,
       "mwrAtpcConfigurations": mwrAtpcConfigurations,
       "mwrAtpcConfigurationsTable": mwrAtpcConfigurationsTable,
       "mwrAtpcConfigurationsEntry": mwrAtpcConfigurationsEntry,
       "mwrAtpcConfigIndex": mwrAtpcConfigIndex,
       "mwrAtpcState": mwrAtpcState,
       "mwrAtpcCoordinatedPower": mwrAtpcCoordinatedPower,
       "mwrAtpcCoordinatedPowerEnable": mwrAtpcCoordinatedPowerEnable,
       "mwrAtpcMinTxPower": mwrAtpcMinTxPower,
       "mwrAtpcMaxTxPower": mwrAtpcMaxTxPower,
       "mwrAtpcRslTarget": mwrAtpcRslTarget,
       "mwrAtpcRslTargetUseDefault": mwrAtpcRslTargetUseDefault,
       "mwrAtpcStatus": mwrAtpcStatus,
       "mwrAtpcStatusTable": mwrAtpcStatusTable,
       "mwrAtpcStatusEntry": mwrAtpcStatusEntry,
       "mwrAtpcStatusIndex": mwrAtpcStatusIndex,
       "mwrAtpcRunningStatus": mwrAtpcRunningStatus,
       "mwrAtpcDefaultRslTarget": mwrAtpcDefaultRslTarget,
       "mwrAtpcActualMinTxPower": mwrAtpcActualMinTxPower,
       "mwrAtpcActualMaxTxPower": mwrAtpcActualMaxTxPower,
       "mwrAtpcActualCoordinatedPower": mwrAtpcActualCoordinatedPower,
       "mwrAtpcPeerRslTarget": mwrAtpcPeerRslTarget,
       "mwrAtpcMinRslTarget": mwrAtpcMinRslTarget,
       "mwrAtpcMaxRslTarget": mwrAtpcMaxRslTarget,
       "mwrAtpcPeerRsl": mwrAtpcPeerRsl,
       "mwrAtpcNotifications": mwrAtpcNotifications,
       "mwrAtpcConfigMismatch": mwrAtpcConfigMismatch,
       "mwrAtpcAutoDisabled": mwrAtpcAutoDisabled,
       "mwrRadio": mwrRadio,
       "mwrCompression": mwrCompression,
       "mwrCompressionConfigurations": mwrCompressionConfigurations,
       "mwrBacRecordAvgPeriod": mwrBacRecordAvgPeriod,
       "mwrBacTable": mwrBacTable,
       "mwrBacEntry": mwrBacEntry,
       "mwrBacQIndex": mwrBacQIndex,
       "mwrBacQEnable": mwrBacQEnable,
       "mwrBacQBlockSize": mwrBacQBlockSize,
       "mwrBacRecordLogging": mwrBacRecordLogging,
       "mwrHcQTable": mwrHcQTable,
       "mwrHcQEntry": mwrHcQEntry,
       "mwrHcQIndex": mwrHcQIndex,
       "mwrHcQ1": mwrHcQ1,
       "mwrHcQ2": mwrHcQ2,
       "mwrHcQ3": mwrHcQ3,
       "mwrHcQ4": mwrHcQ4,
       "mwrHcQ5": mwrHcQ5,
       "mwrHcQ6": mwrHcQ6,
       "mwrHcQ7": mwrHcQ7,
       "mwrHcQ8": mwrHcQ8,
       "mwrHcQRowStatus": mwrHcQRowStatus,
       "mwrCompressionStatus": mwrCompressionStatus,
       "mwrBacStatusTable": mwrBacStatusTable,
       "mwrBacStatusEntry": mwrBacStatusEntry,
       "mwrBacStatusQIndex": mwrBacStatusQIndex,
       "mwrBacUncompressedRatio": mwrBacUncompressedRatio,
       "mwrBacGain": mwrBacGain,
       "mwrCompressionNotifications": mwrCompressionNotifications,
       "mwrEvents": mwrEvents,
       "mwrEventsConfigurations": mwrEventsConfigurations,
       "mwrEventConfigTable": mwrEventConfigTable,
       "mwrEventConfigEntry": mwrEventConfigEntry,
       "mwrEventConfigIndex": mwrEventConfigIndex,
       "mwrEventInstanceIndex": mwrEventInstanceIndex,
       "mwrEventConfigSeverity": mwrEventConfigSeverity,
       "mwrEventName": mwrEventName,
       "mwrAlarmConfigState": mwrAlarmConfigState,
       "mwrTrapConfigState": mwrTrapConfigState,
       "mwrLogEventState": mwrLogEventState,
       "mwrLogs": mwrLogs,
       "mwrLogsConfigurations": mwrLogsConfigurations,
       "mwrEventLogEnable": mwrEventLogEnable,
       "mwrPerfmLogEnable": mwrPerfmLogEnable,
       "mwrPerfmLogInterval": mwrPerfmLogInterval,
       "mwrSysLogServerTable": mwrSysLogServerTable,
       "mwrSysLogServerEntry": mwrSysLogServerEntry,
       "mwrSysLogServerIndex": mwrSysLogServerIndex,
       "mwrSysLogEnable": mwrSysLogEnable,
       "mwrSysLogHostDomain": mwrSysLogHostDomain,
       "mwrSysLogHostAddress": mwrSysLogHostAddress,
       "mwrPM": mwrPM,
       "mwrPMConfigurations": mwrPMConfigurations,
       "mwrPmRspiThresholdTable": mwrPmRspiThresholdTable,
       "mwrPmRspiThresholdEntry": mwrPmRspiThresholdEntry,
       "mwrPmRspiThrIndex": mwrPmRspiThrIndex,
       "mwrPmRLT1": mwrPmRLT1,
       "mwrPmRLT2": mwrPmRLT2,
       "mwrPmRLT3": mwrPmRLT3,
       "mwrPmRLT4": mwrPmRLT4,
       "mwrPmTLT1": mwrPmTLT1,
       "mwrPmTLT2": mwrPmTLT2,
       "mwrPmRspiThrRowStatus": mwrPmRspiThrRowStatus,
       "mwrPmBwThresholdTable": mwrPmBwThresholdTable,
       "mwrPmBwThresholdEntry": mwrPmBwThresholdEntry,
       "mwrPmBWThrIndex": mwrPmBWThrIndex,
       "mwrPmBWT1": mwrPmBWT1,
       "mwrPmBWT2": mwrPmBWT2,
       "mwrPmBWT3": mwrPmBWT3,
       "mwrPmBWT4": mwrPmBWT4,
       "mwrPmBWT5": mwrPmBWT5,
       "mwrPmBWT6": mwrPmBWT6,
       "mwrPmBWT7": mwrPmBWT7,
       "mwrPmBWT8": mwrPmBWT8,
       "mwrPmBWT9": mwrPmBWT9,
       "mwrPmBWT10": mwrPmBWT10,
       "mwrPmBWTRowStatus": mwrPmBWTRowStatus,
       "mwrPmTpThresholdTable": mwrPmTpThresholdTable,
       "mwrPmTpThresholdEntry": mwrPmTpThresholdEntry,
       "mwrPmTPThrIndex": mwrPmTPThrIndex,
       "mwrPmTPT1": mwrPmTPT1,
       "mwrPmTPT2": mwrPmTPT2,
       "mwrPmTPT3": mwrPmTPT3,
       "mwrPmTPT4": mwrPmTPT4,
       "mwrPmTPT5": mwrPmTPT5,
       "mwrPmTPT6": mwrPmTPT6,
       "mwrPmTPT7": mwrPmTPT7,
       "mwrPmTPT8": mwrPmTPT8,
       "mwrPmTPT9": mwrPmTPT9,
       "mwrPmTPT10": mwrPmTPT10,
       "mwrPmTPTRowStatus": mwrPmTPTRowStatus,
       "mwrPmAdvThresholdTable": mwrPmAdvThresholdTable,
       "mwrPmAdvThresholdEntry": mwrPmAdvThresholdEntry,
       "mwrPmAdvThrIndex": mwrPmAdvThrIndex,
       "mwrPmAdvTxHitsT1": mwrPmAdvTxHitsT1,
       "mwrPmAdvRxHitsT1": mwrPmAdvRxHitsT1,
       "mwrPmAdvRowStatus": mwrPmAdvRowStatus,
       "mwrPMStatus": mwrPMStatus,
       "mwrPmRspiTable": mwrPmRspiTable,
       "mwrPmRspiEntry": mwrPmRspiEntry,
       "mwrPmRspiStatusIndex": mwrPmRspiStatusIndex,
       "mwrPmRspiInterval": mwrPmRspiInterval,
       "mwrPmRspiIntervalID": mwrPmRspiIntervalID,
       "mwrPmRspiMeasSuspect": mwrPmRspiMeasSuspect,
       "mwrPmRspiMeasIntervalStatus": mwrPmRspiMeasIntervalStatus,
       "mwrPmRspiMeasTimeLength": mwrPmRspiMeasTimeLength,
       "mwrPmRspiMeasTLTMMin": mwrPmRspiMeasTLTMMin,
       "mwrPmRspiMeasTLTMMax": mwrPmRspiMeasTLTMMax,
       "mwrPmRspiMeasTLTS1": mwrPmRspiMeasTLTS1,
       "mwrPmRspiMeasTLTS2": mwrPmRspiMeasTLTS2,
       "mwrPmRspiMeasRLTMMin": mwrPmRspiMeasRLTMMin,
       "mwrPmRspiMeasRLTMMax": mwrPmRspiMeasRLTMMax,
       "mwrPmRspiMeasRLTS1": mwrPmRspiMeasRLTS1,
       "mwrPmRspiMeasRLTS2": mwrPmRspiMeasRLTS2,
       "mwrPmRspiMeasRLTS3": mwrPmRspiMeasRLTS3,
       "mwrPmRspiMeasRLTS4": mwrPmRspiMeasRLTS4,
       "mwrPmBWTable": mwrPmBWTable,
       "mwrPmBWEntry": mwrPmBWEntry,
       "mwrPmBWStatusIndex": mwrPmBWStatusIndex,
       "mwrPmBWInterval": mwrPmBWInterval,
       "mwrPmBWIntervalID": mwrPmBWIntervalID,
       "mwrPmBWMeasSuspect": mwrPmBWMeasSuspect,
       "mwrPmBWMeasIntervalStatus": mwrPmBWMeasIntervalStatus,
       "mwrPmBWMeasTimeLength": mwrPmBWMeasTimeLength,
       "mwrPmMeasBWTS1": mwrPmMeasBWTS1,
       "mwrPmMeasBWTS2": mwrPmMeasBWTS2,
       "mwrPmMeasBWTS3": mwrPmMeasBWTS3,
       "mwrPmMeasBWTS4": mwrPmMeasBWTS4,
       "mwrPmMeasBWTS5": mwrPmMeasBWTS5,
       "mwrPmMeasBWTS6": mwrPmMeasBWTS6,
       "mwrPmMeasBWTS7": mwrPmMeasBWTS7,
       "mwrPmMeasBWTS8": mwrPmMeasBWTS8,
       "mwrPmMeasBWTS9": mwrPmMeasBWTS9,
       "mwrPmMeasBWTS10": mwrPmMeasBWTS10,
       "mwrPmTPTable": mwrPmTPTable,
       "mwrPmTPEntry": mwrPmTPEntry,
       "mwrPmTPStatusIndex": mwrPmTPStatusIndex,
       "mwrPmTPInterval": mwrPmTPInterval,
       "mwrPmTPIntervalID": mwrPmTPIntervalID,
       "mwrPmTPMeasSuspect": mwrPmTPMeasSuspect,
       "mwrPmTPMeasIntervalStatus": mwrPmTPMeasIntervalStatus,
       "mwrPmTPMeasTimeLength": mwrPmTPMeasTimeLength,
       "mwrPmMeasTPTS1": mwrPmMeasTPTS1,
       "mwrPmMeasTPTS2": mwrPmMeasTPTS2,
       "mwrPmMeasTPTS3": mwrPmMeasTPTS3,
       "mwrPmMeasTPTS4": mwrPmMeasTPTS4,
       "mwrPmMeasTPTS5": mwrPmMeasTPTS5,
       "mwrPmMeasTPTS6": mwrPmMeasTPTS6,
       "mwrPmMeasTPTS7": mwrPmMeasTPTS7,
       "mwrPmMeasTPTS8": mwrPmMeasTPTS8,
       "mwrPmMeasTPTS9": mwrPmMeasTPTS9,
       "mwrPmMeasTPTS10": mwrPmMeasTPTS10,
       "mwrPmAdvTable": mwrPmAdvTable,
       "mwrPmAdvEntry": mwrPmAdvEntry,
       "mwrPmAdvStatusIndex": mwrPmAdvStatusIndex,
       "mwrPmAdvInterval": mwrPmAdvInterval,
       "mwrPmAdvIntervalID": mwrPmAdvIntervalID,
       "mwrPmAdvMeasSuspect": mwrPmAdvMeasSuspect,
       "mwrPmAdvMeasIntervalStatus": mwrPmAdvMeasIntervalStatus,
       "mwrPmAdvMeasTimeLength": mwrPmAdvMeasTimeLength,
       "mwrPmAdvTxCapPeak": mwrPmAdvTxCapPeak,
       "mwrPmAdvTxCapRatio": mwrPmAdvTxCapRatio,
       "mwrPmAdvTxCapAvg": mwrPmAdvTxCapAvg,
       "mwrPmAdvTxCapAvgRatio": mwrPmAdvTxCapAvgRatio,
       "mwrPmAdvTxCapHits": mwrPmAdvTxCapHits,
       "mwrPmAdvRxCapPeak": mwrPmAdvRxCapPeak,
       "mwrPmAdvRxCapRatio": mwrPmAdvRxCapRatio,
       "mwrPmAdvRxCapAvg": mwrPmAdvRxCapAvg,
       "mwrPmAdvRxCapHits": mwrPmAdvRxCapHits,
       "mwrPMNotifications": mwrPMNotifications,
       "mwrUserMgmt": mwrUserMgmt,
       "mwrUserConfiguration": mwrUserConfiguration,
       "mwrUserStatus": mwrUserStatus,
       "mwrUserSessionTable": mwrUserSessionTable,
       "mwrUserSessionEntry": mwrUserSessionEntry,
       "mwrUserIndex": mwrUserIndex,
       "mwrUserName": mwrUserName,
       "mwrUserConnectionType": mwrUserConnectionType,
       "mwrUserConnectionState": mwrUserConnectionState,
       "mwrUserNotifications": mwrUserNotifications,
       "mwrUserSession": mwrUserSession,
       "mwrUserLoginFailed": mwrUserLoginFailed,
       "mwrUserAccountChanged": mwrUserAccountChanged,
       "mwrUserPasswordChanged": mwrUserPasswordChanged,
       "mwrModIdentity": mwrModIdentity}
)
