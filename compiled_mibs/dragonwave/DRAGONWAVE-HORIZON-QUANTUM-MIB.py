# SNMP MIB module (DRAGONWAVE-HORIZON-QUANTUM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\dragonwave\DRAGONWAVE-HORIZON-QUANTUM-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:38:29 2025
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

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

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

hzQtmModIdentity = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 1000)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_HorizonQuantum_ObjectIdentity = ObjectIdentity
horizonQuantum = _HorizonQuantum_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4)
)
_HzQtmSystem_ObjectIdentity = ObjectIdentity
hzQtmSystem = _HzQtmSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 1)
)
_HzQtmSysGeneral_ObjectIdentity = ObjectIdentity
hzQtmSysGeneral = _HzQtmSysGeneral_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 1, 1)
)


class _HzQtmResetSystem_Type(Integer32):
    """Custom type hzQtmResetSystem based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("reset", 1)
    )


_HzQtmResetSystem_Type.__name__ = "Integer32"
_HzQtmResetSystem_Object = MibScalar
hzQtmResetSystem = _HzQtmResetSystem_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 1, 1, 1),
    _HzQtmResetSystem_Type()
)
hzQtmResetSystem.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzQtmResetSystem.setStatus("current")


class _HzQtmSaveMIB_Type(Integer32):
    """Custom type hzQtmSaveMIB based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("save", 1)
    )


_HzQtmSaveMIB_Type.__name__ = "Integer32"
_HzQtmSaveMIB_Object = MibScalar
hzQtmSaveMIB = _HzQtmSaveMIB_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 1, 1, 2),
    _HzQtmSaveMIB_Type()
)
hzQtmSaveMIB.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzQtmSaveMIB.setStatus("current")


class _HzQtmOperStatus_Type(Integer32):
    """Custom type hzQtmOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("up", 1),
          ("down", 2),
          ("testing", 3))
    )


_HzQtmOperStatus_Type.__name__ = "Integer32"
_HzQtmOperStatus_Object = MibScalar
hzQtmOperStatus = _HzQtmOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 1, 1, 3),
    _HzQtmOperStatus_Type()
)
hzQtmOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzQtmOperStatus.setStatus("current")


class _HzQtmAirInterfaceEncryption_Type(Integer32):
    """Custom type hzQtmAirInterfaceEncryption based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_HzQtmAirInterfaceEncryption_Type.__name__ = "Integer32"
_HzQtmAirInterfaceEncryption_Object = MibScalar
hzQtmAirInterfaceEncryption = _HzQtmAirInterfaceEncryption_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 1, 1, 4),
    _HzQtmAirInterfaceEncryption_Type()
)
hzQtmAirInterfaceEncryption.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzQtmAirInterfaceEncryption.setStatus("current")


class _HzQtmSystemCapacityOption_Type(Integer32):
    """Custom type hzQtmSystemCapacityOption based on Integer32"""
    defaultValue = 1

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
        *(("singleModem-singleRadio", 1),
          ("multiModem-singleRadio", 2),
          ("multiModem-multiRadio", 3),
          ("singleModem-redundancy", 4),
          ("multiCarrierXpic", 5))
    )


_HzQtmSystemCapacityOption_Type.__name__ = "Integer32"
_HzQtmSystemCapacityOption_Object = MibScalar
hzQtmSystemCapacityOption = _HzQtmSystemCapacityOption_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 1, 1, 5),
    _HzQtmSystemCapacityOption_Type()
)
hzQtmSystemCapacityOption.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzQtmSystemCapacityOption.setStatus("current")
_HzQtmSystemLedStatus_Type = DisplayString
_HzQtmSystemLedStatus_Object = MibScalar
hzQtmSystemLedStatus = _HzQtmSystemLedStatus_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 1, 1, 6),
    _HzQtmSystemLedStatus_Type()
)
hzQtmSystemLedStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzQtmSystemLedStatus.setStatus("current")


class _HzQtmSaveL2SwConfig_Type(Integer32):
    """Custom type hzQtmSaveL2SwConfig based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("save", 1)
    )


_HzQtmSaveL2SwConfig_Type.__name__ = "Integer32"
_HzQtmSaveL2SwConfig_Object = MibScalar
hzQtmSaveL2SwConfig = _HzQtmSaveL2SwConfig_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 1, 1, 7),
    _HzQtmSaveL2SwConfig_Type()
)
hzQtmSaveL2SwConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzQtmSaveL2SwConfig.setStatus("current")
_HzQtmIduTemperature_Type = Integer32
_HzQtmIduTemperature_Object = MibScalar
hzQtmIduTemperature = _HzQtmIduTemperature_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 1, 1, 8),
    _HzQtmIduTemperature_Type()
)
hzQtmIduTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzQtmIduTemperature.setStatus("current")
_HzQtmSysUpgradeSpeed_ObjectIdentity = ObjectIdentity
hzQtmSysUpgradeSpeed = _HzQtmSysUpgradeSpeed_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 1, 2)
)
_HzQtmLicensedSpeedUpgradeSpeedAndKey_Type = DisplayString
_HzQtmLicensedSpeedUpgradeSpeedAndKey_Object = MibScalar
hzQtmLicensedSpeedUpgradeSpeedAndKey = _HzQtmLicensedSpeedUpgradeSpeedAndKey_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 1, 2, 1),
    _HzQtmLicensedSpeedUpgradeSpeedAndKey_Type()
)
hzQtmLicensedSpeedUpgradeSpeedAndKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzQtmLicensedSpeedUpgradeSpeedAndKey.setStatus("current")
_HzQtmLicensedSpeedCount_Type = Integer32
_HzQtmLicensedSpeedCount_Object = MibScalar
hzQtmLicensedSpeedCount = _HzQtmLicensedSpeedCount_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 1, 2, 2),
    _HzQtmLicensedSpeedCount_Type()
)
hzQtmLicensedSpeedCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzQtmLicensedSpeedCount.setStatus("current")
_HzQtmSysDowngradeSpeed_ObjectIdentity = ObjectIdentity
hzQtmSysDowngradeSpeed = _HzQtmSysDowngradeSpeed_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 1, 3)
)
_HzQtmLicensedSpeedDowngradeSpeed_Type = Integer32
_HzQtmLicensedSpeedDowngradeSpeed_Object = MibScalar
hzQtmLicensedSpeedDowngradeSpeed = _HzQtmLicensedSpeedDowngradeSpeed_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 1, 3, 1),
    _HzQtmLicensedSpeedDowngradeSpeed_Type()
)
hzQtmLicensedSpeedDowngradeSpeed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzQtmLicensedSpeedDowngradeSpeed.setStatus("current")
_HzQtmLicensedSpeedCountUsedForKey_Type = Integer32
_HzQtmLicensedSpeedCountUsedForKey_Object = MibScalar
hzQtmLicensedSpeedCountUsedForKey = _HzQtmLicensedSpeedCountUsedForKey_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 1, 3, 2),
    _HzQtmLicensedSpeedCountUsedForKey_Type()
)
hzQtmLicensedSpeedCountUsedForKey.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzQtmLicensedSpeedCountUsedForKey.setStatus("current")
_HzQtmLicensedSpeedConfirmationKey_Type = DisplayString
_HzQtmLicensedSpeedConfirmationKey_Object = MibScalar
hzQtmLicensedSpeedConfirmationKey = _HzQtmLicensedSpeedConfirmationKey_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 1, 3, 3),
    _HzQtmLicensedSpeedConfirmationKey_Type()
)
hzQtmLicensedSpeedConfirmationKey.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzQtmLicensedSpeedConfirmationKey.setStatus("current")
_HzQtmSysDowngradeSpeedDecrement_Type = Integer32
_HzQtmSysDowngradeSpeedDecrement_Object = MibScalar
hzQtmSysDowngradeSpeedDecrement = _HzQtmSysDowngradeSpeedDecrement_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 1, 3, 4),
    _HzQtmSysDowngradeSpeedDecrement_Type()
)
hzQtmSysDowngradeSpeedDecrement.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzQtmSysDowngradeSpeedDecrement.setStatus("current")
_HzQtmSysSpeed_ObjectIdentity = ObjectIdentity
hzQtmSysSpeed = _HzQtmSysSpeed_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 1, 4)
)


class _HzQtmSystemCurrentSpeed_Type(Integer32):
    """Custom type hzQtmSystemCurrentSpeed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2000),
    )


_HzQtmSystemCurrentSpeed_Type.__name__ = "Integer32"
_HzQtmSystemCurrentSpeed_Object = MibScalar
hzQtmSystemCurrentSpeed = _HzQtmSystemCurrentSpeed_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 1, 4, 1),
    _HzQtmSystemCurrentSpeed_Type()
)
hzQtmSystemCurrentSpeed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzQtmSystemCurrentSpeed.setStatus("current")


class _HzQtmSystemLicensedSpeed_Type(Integer32):
    """Custom type hzQtmSystemLicensedSpeed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2000),
    )


_HzQtmSystemLicensedSpeed_Type.__name__ = "Integer32"
_HzQtmSystemLicensedSpeed_Object = MibScalar
hzQtmSystemLicensedSpeed = _HzQtmSystemLicensedSpeed_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 1, 4, 2),
    _HzQtmSystemLicensedSpeed_Type()
)
hzQtmSystemLicensedSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzQtmSystemLicensedSpeed.setStatus("current")
_HzQtmSystemModeTable_Object = MibTable
hzQtmSystemModeTable = _HzQtmSystemModeTable_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 1, 4, 3)
)
if mibBuilder.loadTexts:
    hzQtmSystemModeTable.setStatus("current")
_HzQtmSystemModeEntry_Object = MibTableRow
hzQtmSystemModeEntry = _HzQtmSystemModeEntry_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 1, 4, 3, 1)
)
hzQtmSystemModeEntry.setIndexNames(
    (0, "DRAGONWAVE-HORIZON-QUANTUM-MIB", "hzQtmSystemModeIndex"),
)
if mibBuilder.loadTexts:
    hzQtmSystemModeEntry.setStatus("current")
_HzQtmSystemModeIndex_Type = Integer32
_HzQtmSystemModeIndex_Object = MibTableColumn
hzQtmSystemModeIndex = _HzQtmSystemModeIndex_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 1, 4, 3, 1, 1),
    _HzQtmSystemModeIndex_Type()
)
hzQtmSystemModeIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzQtmSystemModeIndex.setStatus("current")
_HzQtmSystemModeId_Type = Integer32
_HzQtmSystemModeId_Object = MibTableColumn
hzQtmSystemModeId = _HzQtmSystemModeId_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 1, 4, 3, 1, 2),
    _HzQtmSystemModeId_Type()
)
hzQtmSystemModeId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzQtmSystemModeId.setStatus("current")
_HzQtmSystemModeName_Type = DisplayString
_HzQtmSystemModeName_Object = MibTableColumn
hzQtmSystemModeName = _HzQtmSystemModeName_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 1, 4, 3, 1, 3),
    _HzQtmSystemModeName_Type()
)
hzQtmSystemModeName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzQtmSystemModeName.setStatus("current")


class _HzQtmSystemModeProgrammed_Type(Integer32):
    """Custom type hzQtmSystemModeProgrammed based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("notActive", 2))
    )


_HzQtmSystemModeProgrammed_Type.__name__ = "Integer32"
_HzQtmSystemModeProgrammed_Object = MibTableColumn
hzQtmSystemModeProgrammed = _HzQtmSystemModeProgrammed_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 1, 4, 3, 1, 4),
    _HzQtmSystemModeProgrammed_Type()
)
hzQtmSystemModeProgrammed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzQtmSystemModeProgrammed.setStatus("current")
_HzQtmInventory_ObjectIdentity = ObjectIdentity
hzQtmInventory = _HzQtmInventory_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 1, 5)
)
_HzQtmHwInventory_ObjectIdentity = ObjectIdentity
hzQtmHwInventory = _HzQtmHwInventory_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 1, 5, 1)
)
_HzQtmFrequencyFilePartNumber_Type = DisplayString
_HzQtmFrequencyFilePartNumber_Object = MibScalar
hzQtmFrequencyFilePartNumber = _HzQtmFrequencyFilePartNumber_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 1, 5, 1, 1),
    _HzQtmFrequencyFilePartNumber_Type()
)
hzQtmFrequencyFilePartNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzQtmFrequencyFilePartNumber.setStatus("current")
_HzQtmUnitSerialNo_Type = DisplayString
_HzQtmUnitSerialNo_Object = MibScalar
hzQtmUnitSerialNo = _HzQtmUnitSerialNo_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 1, 5, 1, 2),
    _HzQtmUnitSerialNo_Type()
)
hzQtmUnitSerialNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzQtmUnitSerialNo.setStatus("current")
_HzQtmUnitAssemblylNo_Type = DisplayString
_HzQtmUnitAssemblylNo_Object = MibScalar
hzQtmUnitAssemblylNo = _HzQtmUnitAssemblylNo_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 1, 5, 1, 3),
    _HzQtmUnitAssemblylNo_Type()
)
hzQtmUnitAssemblylNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzQtmUnitAssemblylNo.setStatus("current")
_HzQtmCcaSerialNo_Type = DisplayString
_HzQtmCcaSerialNo_Object = MibScalar
hzQtmCcaSerialNo = _HzQtmCcaSerialNo_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 1, 5, 1, 4),
    _HzQtmCcaSerialNo_Type()
)
hzQtmCcaSerialNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzQtmCcaSerialNo.setStatus("current")
_HzQtmCcaPartNo_Type = DisplayString
_HzQtmCcaPartNo_Object = MibScalar
hzQtmCcaPartNo = _HzQtmCcaPartNo_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 1, 5, 1, 5),
    _HzQtmCcaPartNo_Type()
)
hzQtmCcaPartNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzQtmCcaPartNo.setStatus("current")
_HzQtmRadio1SerialNo_Type = DisplayString
_HzQtmRadio1SerialNo_Object = MibScalar
hzQtmRadio1SerialNo = _HzQtmRadio1SerialNo_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 1, 5, 1, 6),
    _HzQtmRadio1SerialNo_Type()
)
hzQtmRadio1SerialNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzQtmRadio1SerialNo.setStatus("current")
_HzQtmRadio2SerialNo_Type = DisplayString
_HzQtmRadio2SerialNo_Object = MibScalar
hzQtmRadio2SerialNo = _HzQtmRadio2SerialNo_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 1, 5, 1, 7),
    _HzQtmRadio2SerialNo_Type()
)
hzQtmRadio2SerialNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzQtmRadio2SerialNo.setStatus("current")
_HzQtmRadio1HardwareId_Type = DisplayString
_HzQtmRadio1HardwareId_Object = MibScalar
hzQtmRadio1HardwareId = _HzQtmRadio1HardwareId_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 1, 5, 1, 8),
    _HzQtmRadio1HardwareId_Type()
)
hzQtmRadio1HardwareId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzQtmRadio1HardwareId.setStatus("current")
_HzQtmRadio2HardwareId_Type = DisplayString
_HzQtmRadio2HardwareId_Object = MibScalar
hzQtmRadio2HardwareId = _HzQtmRadio2HardwareId_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 1, 5, 1, 9),
    _HzQtmRadio2HardwareId_Type()
)
hzQtmRadio2HardwareId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzQtmRadio2HardwareId.setStatus("current")
_HzQtmRadio1HardwareType_Type = DisplayString
_HzQtmRadio1HardwareType_Object = MibScalar
hzQtmRadio1HardwareType = _HzQtmRadio1HardwareType_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 1, 5, 1, 10),
    _HzQtmRadio1HardwareType_Type()
)
hzQtmRadio1HardwareType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzQtmRadio1HardwareType.setStatus("current")
_HzQtmRadio2HardwareType_Type = DisplayString
_HzQtmRadio2HardwareType_Object = MibScalar
hzQtmRadio2HardwareType = _HzQtmRadio2HardwareType_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 1, 5, 1, 11),
    _HzQtmRadio2HardwareType_Type()
)
hzQtmRadio2HardwareType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzQtmRadio2HardwareType.setStatus("current")
_HzQtmSwInventory_ObjectIdentity = ObjectIdentity
hzQtmSwInventory = _HzQtmSwInventory_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 1, 5, 2)
)
_HzQtmSwInvAppOmniVersionNo_Type = DisplayString
_HzQtmSwInvAppOmniVersionNo_Object = MibScalar
hzQtmSwInvAppOmniVersionNo = _HzQtmSwInvAppOmniVersionNo_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 1, 5, 2, 1),
    _HzQtmSwInvAppOmniVersionNo_Type()
)
hzQtmSwInvAppOmniVersionNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzQtmSwInvAppOmniVersionNo.setStatus("current")
_HzQtmSwInvAppFirmwareVersionNo_Type = DisplayString
_HzQtmSwInvAppFirmwareVersionNo_Object = MibScalar
hzQtmSwInvAppFirmwareVersionNo = _HzQtmSwInvAppFirmwareVersionNo_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 1, 5, 2, 2),
    _HzQtmSwInvAppFirmwareVersionNo_Type()
)
hzQtmSwInvAppFirmwareVersionNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzQtmSwInvAppFirmwareVersionNo.setStatus("current")
_HzQtmSwInvFrequencyFileVersionNo_Type = DisplayString
_HzQtmSwInvFrequencyFileVersionNo_Object = MibScalar
hzQtmSwInvFrequencyFileVersionNo = _HzQtmSwInvFrequencyFileVersionNo_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 1, 5, 2, 3),
    _HzQtmSwInvFrequencyFileVersionNo_Type()
)
hzQtmSwInvFrequencyFileVersionNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzQtmSwInvFrequencyFileVersionNo.setStatus("current")
_HzQtmSwInvMibVersionNo_Type = DisplayString
_HzQtmSwInvMibVersionNo_Object = MibScalar
hzQtmSwInvMibVersionNo = _HzQtmSwInvMibVersionNo_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 1, 5, 2, 4),
    _HzQtmSwInvMibVersionNo_Type()
)
hzQtmSwInvMibVersionNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzQtmSwInvMibVersionNo.setStatus("current")
_HzQtmSwInvRadioFirmware1VersionNo_Type = DisplayString
_HzQtmSwInvRadioFirmware1VersionNo_Object = MibScalar
hzQtmSwInvRadioFirmware1VersionNo = _HzQtmSwInvRadioFirmware1VersionNo_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 1, 5, 2, 5),
    _HzQtmSwInvRadioFirmware1VersionNo_Type()
)
hzQtmSwInvRadioFirmware1VersionNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzQtmSwInvRadioFirmware1VersionNo.setStatus("current")
_HzQtmSwInvRadioFirmware2VersionNo_Type = DisplayString
_HzQtmSwInvRadioFirmware2VersionNo_Object = MibScalar
hzQtmSwInvRadioFirmware2VersionNo = _HzQtmSwInvRadioFirmware2VersionNo_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 1, 5, 2, 6),
    _HzQtmSwInvRadioFirmware2VersionNo_Type()
)
hzQtmSwInvRadioFirmware2VersionNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzQtmSwInvRadioFirmware2VersionNo.setStatus("current")
_HzQtmSwInvAppSoftwareVersionNo_Type = DisplayString
_HzQtmSwInvAppSoftwareVersionNo_Object = MibScalar
hzQtmSwInvAppSoftwareVersionNo = _HzQtmSwInvAppSoftwareVersionNo_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 1, 5, 2, 7),
    _HzQtmSwInvAppSoftwareVersionNo_Type()
)
hzQtmSwInvAppSoftwareVersionNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzQtmSwInvAppSoftwareVersionNo.setStatus("current")
_HzQtmSwInvBootloaderVersionNo_Type = DisplayString
_HzQtmSwInvBootloaderVersionNo_Object = MibScalar
hzQtmSwInvBootloaderVersionNo = _HzQtmSwInvBootloaderVersionNo_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 1, 5, 2, 8),
    _HzQtmSwInvBootloaderVersionNo_Type()
)
hzQtmSwInvBootloaderVersionNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzQtmSwInvBootloaderVersionNo.setStatus("current")
_HzQtmSwInvSupportingAppVersionNo_Type = DisplayString
_HzQtmSwInvSupportingAppVersionNo_Object = MibScalar
hzQtmSwInvSupportingAppVersionNo = _HzQtmSwInvSupportingAppVersionNo_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 1, 5, 2, 9),
    _HzQtmSwInvSupportingAppVersionNo_Type()
)
hzQtmSwInvSupportingAppVersionNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzQtmSwInvSupportingAppVersionNo.setStatus("current")
_HzQtmSwInvOperatingSystemVersionNo_Type = DisplayString
_HzQtmSwInvOperatingSystemVersionNo_Object = MibScalar
hzQtmSwInvOperatingSystemVersionNo = _HzQtmSwInvOperatingSystemVersionNo_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 1, 5, 2, 10),
    _HzQtmSwInvOperatingSystemVersionNo_Type()
)
hzQtmSwInvOperatingSystemVersionNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzQtmSwInvOperatingSystemVersionNo.setStatus("current")
_HzQtmSwInvRadio1CurrentFirmwareVersionNo_Type = DisplayString
_HzQtmSwInvRadio1CurrentFirmwareVersionNo_Object = MibScalar
hzQtmSwInvRadio1CurrentFirmwareVersionNo = _HzQtmSwInvRadio1CurrentFirmwareVersionNo_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 1, 5, 2, 11),
    _HzQtmSwInvRadio1CurrentFirmwareVersionNo_Type()
)
hzQtmSwInvRadio1CurrentFirmwareVersionNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzQtmSwInvRadio1CurrentFirmwareVersionNo.setStatus("current")
_HzQtmSwInvRadio2CurrentFirmwareVersionNo_Type = DisplayString
_HzQtmSwInvRadio2CurrentFirmwareVersionNo_Object = MibScalar
hzQtmSwInvRadio2CurrentFirmwareVersionNo = _HzQtmSwInvRadio2CurrentFirmwareVersionNo_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 1, 5, 2, 12),
    _HzQtmSwInvRadio2CurrentFirmwareVersionNo_Type()
)
hzQtmSwInvRadio2CurrentFirmwareVersionNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzQtmSwInvRadio2CurrentFirmwareVersionNo.setStatus("current")
_HzQtmAtpc_ObjectIdentity = ObjectIdentity
hzQtmAtpc = _HzQtmAtpc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 1, 6)
)


class _HzQtmAtpcEnable_Type(Integer32):
    """Custom type hzQtmAtpcEnable based on Integer32"""
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


_HzQtmAtpcEnable_Type.__name__ = "Integer32"
_HzQtmAtpcEnable_Object = MibScalar
hzQtmAtpcEnable = _HzQtmAtpcEnable_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 1, 6, 1),
    _HzQtmAtpcEnable_Type()
)
hzQtmAtpcEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzQtmAtpcEnable.setStatus("current")
_HzQtmAtpcStatus_Type = DisplayString
_HzQtmAtpcStatus_Object = MibScalar
hzQtmAtpcStatus = _HzQtmAtpcStatus_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 1, 6, 2),
    _HzQtmAtpcStatus_Type()
)
hzQtmAtpcStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzQtmAtpcStatus.setStatus("current")
_HzQtmAtpcCoordinatedPower_Type = DisplayString
_HzQtmAtpcCoordinatedPower_Object = MibScalar
hzQtmAtpcCoordinatedPower = _HzQtmAtpcCoordinatedPower_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 1, 6, 3),
    _HzQtmAtpcCoordinatedPower_Type()
)
hzQtmAtpcCoordinatedPower.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzQtmAtpcCoordinatedPower.setStatus("current")
_HzQtmHitlessAam_ObjectIdentity = ObjectIdentity
hzQtmHitlessAam = _HzQtmHitlessAam_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 1, 7)
)


class _HzQtmHitlessAamStatus_Type(Integer32):
    """Custom type hzQtmHitlessAamStatus based on Integer32"""
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


_HzQtmHitlessAamStatus_Type.__name__ = "Integer32"
_HzQtmHitlessAamStatus_Object = MibScalar
hzQtmHitlessAamStatus = _HzQtmHitlessAamStatus_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 1, 7, 1),
    _HzQtmHitlessAamStatus_Type()
)
hzQtmHitlessAamStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzQtmHitlessAamStatus.setStatus("current")


class _HzQtmHitlessAamManualMode_Type(Integer32):
    """Custom type hzQtmHitlessAamManualMode based on Integer32"""
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


_HzQtmHitlessAamManualMode_Type.__name__ = "Integer32"
_HzQtmHitlessAamManualMode_Object = MibScalar
hzQtmHitlessAamManualMode = _HzQtmHitlessAamManualMode_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 1, 7, 2),
    _HzQtmHitlessAamManualMode_Type()
)
hzQtmHitlessAamManualMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzQtmHitlessAamManualMode.setStatus("current")
_HzQtmHitlessAamTable_Object = MibTable
hzQtmHitlessAamTable = _HzQtmHitlessAamTable_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 1, 7, 3)
)
if mibBuilder.loadTexts:
    hzQtmHitlessAamTable.setStatus("current")
_HzQtmHitlessAamEntry_Object = MibTableRow
hzQtmHitlessAamEntry = _HzQtmHitlessAamEntry_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 1, 7, 3, 1)
)
hzQtmHitlessAamEntry.setIndexNames(
    (0, "DRAGONWAVE-HORIZON-QUANTUM-MIB", "hzQtmHitlessAamIndex"),
)
if mibBuilder.loadTexts:
    hzQtmHitlessAamEntry.setStatus("current")


class _HzQtmHitlessAamIndex_Type(Integer32):
    """Custom type hzQtmHitlessAamIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("wireless-port-1", 1),
          ("wireless-port-2", 2))
    )


_HzQtmHitlessAamIndex_Type.__name__ = "Integer32"
_HzQtmHitlessAamIndex_Object = MibTableColumn
hzQtmHitlessAamIndex = _HzQtmHitlessAamIndex_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 1, 7, 3, 1, 1),
    _HzQtmHitlessAamIndex_Type()
)
hzQtmHitlessAamIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzQtmHitlessAamIndex.setStatus("current")


class _HzQtmHitlessAamCurrentMode_Type(DisplayString):
    """Custom type hzQtmHitlessAamCurrentMode based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 24),
    )


_HzQtmHitlessAamCurrentMode_Type.__name__ = "DisplayString"
_HzQtmHitlessAamCurrentMode_Object = MibTableColumn
hzQtmHitlessAamCurrentMode = _HzQtmHitlessAamCurrentMode_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 1, 7, 3, 1, 2),
    _HzQtmHitlessAamCurrentMode_Type()
)
hzQtmHitlessAamCurrentMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzQtmHitlessAamCurrentMode.setStatus("current")
_HzQtmHitlessAamDiagnostics_ObjectIdentity = ObjectIdentity
hzQtmHitlessAamDiagnostics = _HzQtmHitlessAamDiagnostics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 1, 7, 4)
)


class _HzQtmHitlessAamModem1Diagnose_Type(Integer32):
    """Custom type hzQtmHitlessAamModem1Diagnose based on Integer32"""
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


_HzQtmHitlessAamModem1Diagnose_Type.__name__ = "Integer32"
_HzQtmHitlessAamModem1Diagnose_Object = MibScalar
hzQtmHitlessAamModem1Diagnose = _HzQtmHitlessAamModem1Diagnose_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 1, 7, 4, 1),
    _HzQtmHitlessAamModem1Diagnose_Type()
)
hzQtmHitlessAamModem1Diagnose.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzQtmHitlessAamModem1Diagnose.setStatus("current")
_HzQtmHitlessAamModem1DiagnosticResult_Type = DisplayString
_HzQtmHitlessAamModem1DiagnosticResult_Object = MibScalar
hzQtmHitlessAamModem1DiagnosticResult = _HzQtmHitlessAamModem1DiagnosticResult_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 1, 7, 4, 2),
    _HzQtmHitlessAamModem1DiagnosticResult_Type()
)
hzQtmHitlessAamModem1DiagnosticResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzQtmHitlessAamModem1DiagnosticResult.setStatus("current")


class _HzQtmHitlessAamModem2Diagnose_Type(Integer32):
    """Custom type hzQtmHitlessAamModem2Diagnose based on Integer32"""
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


_HzQtmHitlessAamModem2Diagnose_Type.__name__ = "Integer32"
_HzQtmHitlessAamModem2Diagnose_Object = MibScalar
hzQtmHitlessAamModem2Diagnose = _HzQtmHitlessAamModem2Diagnose_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 1, 7, 4, 3),
    _HzQtmHitlessAamModem2Diagnose_Type()
)
hzQtmHitlessAamModem2Diagnose.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzQtmHitlessAamModem2Diagnose.setStatus("current")
_HzQtmHitlessAamModem2DiagnosticResult_Type = DisplayString
_HzQtmHitlessAamModem2DiagnosticResult_Object = MibScalar
hzQtmHitlessAamModem2DiagnosticResult = _HzQtmHitlessAamModem2DiagnosticResult_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 1, 7, 4, 4),
    _HzQtmHitlessAamModem2DiagnosticResult_Type()
)
hzQtmHitlessAamModem2DiagnosticResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzQtmHitlessAamModem2DiagnosticResult.setStatus("current")
_HzQtmHitlessAamMaxMode_Type = DisplayString
_HzQtmHitlessAamMaxMode_Object = MibScalar
hzQtmHitlessAamMaxMode = _HzQtmHitlessAamMaxMode_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 1, 7, 5),
    _HzQtmHitlessAamMaxMode_Type()
)
hzQtmHitlessAamMaxMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzQtmHitlessAamMaxMode.setStatus("current")
_HzQtmHitlessAamMinMode_Type = DisplayString
_HzQtmHitlessAamMinMode_Object = MibScalar
hzQtmHitlessAamMinMode = _HzQtmHitlessAamMinMode_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 1, 7, 6),
    _HzQtmHitlessAamMinMode_Type()
)
hzQtmHitlessAamMinMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzQtmHitlessAamMinMode.setStatus("current")
_HzQtmPeerSysInfo_ObjectIdentity = ObjectIdentity
hzQtmPeerSysInfo = _HzQtmPeerSysInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 1, 8)
)
_HzQtmPeerMacAddress_Type = DisplayString
_HzQtmPeerMacAddress_Object = MibScalar
hzQtmPeerMacAddress = _HzQtmPeerMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 1, 8, 1),
    _HzQtmPeerMacAddress_Type()
)
hzQtmPeerMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzQtmPeerMacAddress.setStatus("current")
_HzQtmPeerIpAddress_Type = IpAddress
_HzQtmPeerIpAddress_Object = MibScalar
hzQtmPeerIpAddress = _HzQtmPeerIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 1, 8, 2),
    _HzQtmPeerIpAddress_Type()
)
hzQtmPeerIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzQtmPeerIpAddress.setStatus("current")
_HzQtmPeerSubnetMask_Type = IpAddress
_HzQtmPeerSubnetMask_Object = MibScalar
hzQtmPeerSubnetMask = _HzQtmPeerSubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 1, 8, 3),
    _HzQtmPeerSubnetMask_Type()
)
hzQtmPeerSubnetMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzQtmPeerSubnetMask.setStatus("current")
_HzQtmBac_ObjectIdentity = ObjectIdentity
hzQtmBac = _HzQtmBac_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 1, 9)
)
_HzQtmBacTable_Object = MibTable
hzQtmBacTable = _HzQtmBacTable_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 1, 9, 1)
)
if mibBuilder.loadTexts:
    hzQtmBacTable.setStatus("current")
_HzQtmBacEntry_Object = MibTableRow
hzQtmBacEntry = _HzQtmBacEntry_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 1, 9, 1, 1)
)
hzQtmBacEntry.setIndexNames(
    (0, "DRAGONWAVE-HORIZON-QUANTUM-MIB", "hzQtmBacQIndex"),
)
if mibBuilder.loadTexts:
    hzQtmBacEntry.setStatus("current")


class _HzQtmBacQIndex_Type(Integer32):
    """Custom type hzQtmBacQIndex based on Integer32"""
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
        *(("queue1", 1),
          ("queue2", 2),
          ("queue3", 3),
          ("queue4", 4))
    )


_HzQtmBacQIndex_Type.__name__ = "Integer32"
_HzQtmBacQIndex_Object = MibTableColumn
hzQtmBacQIndex = _HzQtmBacQIndex_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 1, 9, 1, 1, 1),
    _HzQtmBacQIndex_Type()
)
hzQtmBacQIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzQtmBacQIndex.setStatus("current")


class _HzQtmBacQEnable_Type(Integer32):
    """Custom type hzQtmBacQEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_HzQtmBacQEnable_Type.__name__ = "Integer32"
_HzQtmBacQEnable_Object = MibTableColumn
hzQtmBacQEnable = _HzQtmBacQEnable_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 1, 9, 1, 1, 2),
    _HzQtmBacQEnable_Type()
)
hzQtmBacQEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzQtmBacQEnable.setStatus("current")


class _HzQtmBacQBlockSize_Type(Integer32):
    """Custom type hzQtmBacQBlockSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(128, 8000),
    )


_HzQtmBacQBlockSize_Type.__name__ = "Integer32"
_HzQtmBacQBlockSize_Object = MibTableColumn
hzQtmBacQBlockSize = _HzQtmBacQBlockSize_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 1, 9, 1, 1, 3),
    _HzQtmBacQBlockSize_Type()
)
hzQtmBacQBlockSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzQtmBacQBlockSize.setStatus("current")
_HzQtmSysDiagnostics_ObjectIdentity = ObjectIdentity
hzQtmSysDiagnostics = _HzQtmSysDiagnostics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 1, 10)
)
_HzQtmIFPath1LoopbackAndTimeout_Type = DisplayString
_HzQtmIFPath1LoopbackAndTimeout_Object = MibScalar
hzQtmIFPath1LoopbackAndTimeout = _HzQtmIFPath1LoopbackAndTimeout_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 1, 10, 1),
    _HzQtmIFPath1LoopbackAndTimeout_Type()
)
hzQtmIFPath1LoopbackAndTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzQtmIFPath1LoopbackAndTimeout.setStatus("current")
_HzQtmIFPath2LoopbackAndTimeout_Type = DisplayString
_HzQtmIFPath2LoopbackAndTimeout_Object = MibScalar
hzQtmIFPath2LoopbackAndTimeout = _HzQtmIFPath2LoopbackAndTimeout_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 1, 10, 2),
    _HzQtmIFPath2LoopbackAndTimeout_Type()
)
hzQtmIFPath2LoopbackAndTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzQtmIFPath2LoopbackAndTimeout.setStatus("current")
_HzQtmRadio1LoopbackAndTimeout_Type = DisplayString
_HzQtmRadio1LoopbackAndTimeout_Object = MibScalar
hzQtmRadio1LoopbackAndTimeout = _HzQtmRadio1LoopbackAndTimeout_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 1, 10, 3),
    _HzQtmRadio1LoopbackAndTimeout_Type()
)
hzQtmRadio1LoopbackAndTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzQtmRadio1LoopbackAndTimeout.setStatus("current")
_HzQtmRadio2LoopbackAndTimeout_Type = DisplayString
_HzQtmRadio2LoopbackAndTimeout_Object = MibScalar
hzQtmRadio2LoopbackAndTimeout = _HzQtmRadio2LoopbackAndTimeout_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 1, 10, 4),
    _HzQtmRadio2LoopbackAndTimeout_Type()
)
hzQtmRadio2LoopbackAndTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzQtmRadio2LoopbackAndTimeout.setStatus("current")
_HzQtmSysLicensedFeatureGroups_ObjectIdentity = ObjectIdentity
hzQtmSysLicensedFeatureGroups = _HzQtmSysLicensedFeatureGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 1, 11)
)
_HzQtmSysUpgradeFeatureGroupsTable_Object = MibTable
hzQtmSysUpgradeFeatureGroupsTable = _HzQtmSysUpgradeFeatureGroupsTable_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 1, 11, 1)
)
if mibBuilder.loadTexts:
    hzQtmSysUpgradeFeatureGroupsTable.setStatus("current")
_HzQtmSysUpgradeFeatureGroupsEntry_Object = MibTableRow
hzQtmSysUpgradeFeatureGroupsEntry = _HzQtmSysUpgradeFeatureGroupsEntry_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 1, 11, 1, 1)
)
hzQtmSysUpgradeFeatureGroupsEntry.setIndexNames(
    (0, "DRAGONWAVE-HORIZON-QUANTUM-MIB", "hzQtmUpgradeLicensedFeatureIndex"),
)
if mibBuilder.loadTexts:
    hzQtmSysUpgradeFeatureGroupsEntry.setStatus("current")


class _HzQtmUpgradeLicensedFeatureIndex_Type(Integer32):
    """Custom type hzQtmUpgradeLicensedFeatureIndex based on Integer32"""
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
        *(("xpic", 1),
          ("bac", 2),
          ("rlsEcfm", 3),
          ("hitlessAam", 4),
          ("dualWirelessPorts", 5),
          ("l2switch", 6))
    )


_HzQtmUpgradeLicensedFeatureIndex_Type.__name__ = "Integer32"
_HzQtmUpgradeLicensedFeatureIndex_Object = MibTableColumn
hzQtmUpgradeLicensedFeatureIndex = _HzQtmUpgradeLicensedFeatureIndex_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 1, 11, 1, 1, 1),
    _HzQtmUpgradeLicensedFeatureIndex_Type()
)
hzQtmUpgradeLicensedFeatureIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzQtmUpgradeLicensedFeatureIndex.setStatus("current")
_HzQtmUpgradeLicensedFeatureKey_Type = DisplayString
_HzQtmUpgradeLicensedFeatureKey_Object = MibTableColumn
hzQtmUpgradeLicensedFeatureKey = _HzQtmUpgradeLicensedFeatureKey_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 1, 11, 1, 1, 2),
    _HzQtmUpgradeLicensedFeatureKey_Type()
)
hzQtmUpgradeLicensedFeatureKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzQtmUpgradeLicensedFeatureKey.setStatus("current")
_HzQtmUpgradeLicensedFeatureCount_Type = Integer32
_HzQtmUpgradeLicensedFeatureCount_Object = MibTableColumn
hzQtmUpgradeLicensedFeatureCount = _HzQtmUpgradeLicensedFeatureCount_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 1, 11, 1, 1, 3),
    _HzQtmUpgradeLicensedFeatureCount_Type()
)
hzQtmUpgradeLicensedFeatureCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzQtmUpgradeLicensedFeatureCount.setStatus("current")
_HzQtmSysDowngradeFeatureGroupsTable_Object = MibTable
hzQtmSysDowngradeFeatureGroupsTable = _HzQtmSysDowngradeFeatureGroupsTable_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 1, 11, 2)
)
if mibBuilder.loadTexts:
    hzQtmSysDowngradeFeatureGroupsTable.setStatus("current")
_HzQtmSysDowngradeFeatureGroupsEntry_Object = MibTableRow
hzQtmSysDowngradeFeatureGroupsEntry = _HzQtmSysDowngradeFeatureGroupsEntry_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 1, 11, 2, 1)
)
hzQtmSysDowngradeFeatureGroupsEntry.setIndexNames(
    (0, "DRAGONWAVE-HORIZON-QUANTUM-MIB", "hzQtmDowngradeLicensedFeatureIndex"),
)
if mibBuilder.loadTexts:
    hzQtmSysDowngradeFeatureGroupsEntry.setStatus("current")


class _HzQtmDowngradeLicensedFeatureIndex_Type(Integer32):
    """Custom type hzQtmDowngradeLicensedFeatureIndex based on Integer32"""
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
        *(("xpic", 1),
          ("bac", 2),
          ("rlsEcfm", 3),
          ("hitlessAam", 4),
          ("dualWirelessPorts", 5),
          ("l2switch", 6))
    )


_HzQtmDowngradeLicensedFeatureIndex_Type.__name__ = "Integer32"
_HzQtmDowngradeLicensedFeatureIndex_Object = MibTableColumn
hzQtmDowngradeLicensedFeatureIndex = _HzQtmDowngradeLicensedFeatureIndex_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 1, 11, 2, 1, 1),
    _HzQtmDowngradeLicensedFeatureIndex_Type()
)
hzQtmDowngradeLicensedFeatureIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzQtmDowngradeLicensedFeatureIndex.setStatus("current")


class _HzQtmDowngradeLicensedFeature_Type(Integer32):
    """Custom type hzQtmDowngradeLicensedFeature based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("downgrade", 1)
    )


_HzQtmDowngradeLicensedFeature_Type.__name__ = "Integer32"
_HzQtmDowngradeLicensedFeature_Object = MibTableColumn
hzQtmDowngradeLicensedFeature = _HzQtmDowngradeLicensedFeature_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 1, 11, 2, 1, 2),
    _HzQtmDowngradeLicensedFeature_Type()
)
hzQtmDowngradeLicensedFeature.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzQtmDowngradeLicensedFeature.setStatus("current")
_HzQtmDowngradeLicensedFeatureCount_Type = Integer32
_HzQtmDowngradeLicensedFeatureCount_Object = MibTableColumn
hzQtmDowngradeLicensedFeatureCount = _HzQtmDowngradeLicensedFeatureCount_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 1, 11, 2, 1, 3),
    _HzQtmDowngradeLicensedFeatureCount_Type()
)
hzQtmDowngradeLicensedFeatureCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzQtmDowngradeLicensedFeatureCount.setStatus("current")
_HzQtmDowngradeLicensedFeatureKey_Type = DisplayString
_HzQtmDowngradeLicensedFeatureKey_Object = MibTableColumn
hzQtmDowngradeLicensedFeatureKey = _HzQtmDowngradeLicensedFeatureKey_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 1, 11, 2, 1, 4),
    _HzQtmDowngradeLicensedFeatureKey_Type()
)
hzQtmDowngradeLicensedFeatureKey.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzQtmDowngradeLicensedFeatureKey.setStatus("current")
_HzQtmSysLicensedFeatureGroupsTable_Object = MibTable
hzQtmSysLicensedFeatureGroupsTable = _HzQtmSysLicensedFeatureGroupsTable_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 1, 11, 3)
)
if mibBuilder.loadTexts:
    hzQtmSysLicensedFeatureGroupsTable.setStatus("current")
_HzQtmSysLicensedFeatureGroupsEntry_Object = MibTableRow
hzQtmSysLicensedFeatureGroupsEntry = _HzQtmSysLicensedFeatureGroupsEntry_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 1, 11, 3, 1)
)
hzQtmSysLicensedFeatureGroupsEntry.setIndexNames(
    (0, "DRAGONWAVE-HORIZON-QUANTUM-MIB", "hzQtmSysLicensedFeatureGroupIndex"),
)
if mibBuilder.loadTexts:
    hzQtmSysLicensedFeatureGroupsEntry.setStatus("current")


class _HzQtmSysLicensedFeatureGroupIndex_Type(Integer32):
    """Custom type hzQtmSysLicensedFeatureGroupIndex based on Integer32"""
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
        *(("xpic", 1),
          ("bac", 2),
          ("rlsEcfm", 3),
          ("hitlessAam", 4),
          ("dualWirelessPorts", 5),
          ("l2switch", 6))
    )


_HzQtmSysLicensedFeatureGroupIndex_Type.__name__ = "Integer32"
_HzQtmSysLicensedFeatureGroupIndex_Object = MibTableColumn
hzQtmSysLicensedFeatureGroupIndex = _HzQtmSysLicensedFeatureGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 1, 11, 3, 1, 1),
    _HzQtmSysLicensedFeatureGroupIndex_Type()
)
hzQtmSysLicensedFeatureGroupIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzQtmSysLicensedFeatureGroupIndex.setStatus("current")
_HzQtmSysLicensedFeatureGroup_Type = DisplayString
_HzQtmSysLicensedFeatureGroup_Object = MibTableColumn
hzQtmSysLicensedFeatureGroup = _HzQtmSysLicensedFeatureGroup_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 1, 11, 3, 1, 2),
    _HzQtmSysLicensedFeatureGroup_Type()
)
hzQtmSysLicensedFeatureGroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzQtmSysLicensedFeatureGroup.setStatus("current")


class _HzQtmSysLicensedFeatureGroupStatus_Type(Integer32):
    """Custom type hzQtmSysLicensedFeatureGroupStatus based on Integer32"""
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


_HzQtmSysLicensedFeatureGroupStatus_Type.__name__ = "Integer32"
_HzQtmSysLicensedFeatureGroupStatus_Object = MibTableColumn
hzQtmSysLicensedFeatureGroupStatus = _HzQtmSysLicensedFeatureGroupStatus_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 1, 11, 3, 1, 3),
    _HzQtmSysLicensedFeatureGroupStatus_Type()
)
hzQtmSysLicensedFeatureGroupStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzQtmSysLicensedFeatureGroupStatus.setStatus("current")
_HzQtmXpic_ObjectIdentity = ObjectIdentity
hzQtmXpic = _HzQtmXpic_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 1, 12)
)


class _HzQtmXpicStatus_Type(Integer32):
    """Custom type hzQtmXpicStatus based on Integer32"""
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


_HzQtmXpicStatus_Type.__name__ = "Integer32"
_HzQtmXpicStatus_Object = MibScalar
hzQtmXpicStatus = _HzQtmXpicStatus_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 1, 12, 1),
    _HzQtmXpicStatus_Type()
)
hzQtmXpicStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzQtmXpicStatus.setStatus("current")


class _HzQtmXpicActualStatus_Type(Integer32):
    """Custom type hzQtmXpicActualStatus based on Integer32"""
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


_HzQtmXpicActualStatus_Type.__name__ = "Integer32"
_HzQtmXpicActualStatus_Object = MibScalar
hzQtmXpicActualStatus = _HzQtmXpicActualStatus_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 1, 12, 2),
    _HzQtmXpicActualStatus_Type()
)
hzQtmXpicActualStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzQtmXpicActualStatus.setStatus("current")


class _HzQtmXpicMode_Type(Integer32):
    """Custom type hzQtmXpicMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("master", 1),
          ("slave", 2))
    )


_HzQtmXpicMode_Type.__name__ = "Integer32"
_HzQtmXpicMode_Object = MibScalar
hzQtmXpicMode = _HzQtmXpicMode_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 1, 12, 3),
    _HzQtmXpicMode_Type()
)
hzQtmXpicMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzQtmXpicMode.setStatus("current")
_HzQtmPlcm_ObjectIdentity = ObjectIdentity
hzQtmPlcm = _HzQtmPlcm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 1, 13)
)


class _HzQtmPlcmMode_Type(Integer32):
    """Custom type hzQtmPlcmMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("qtm", 1),
          ("duo", 2))
    )


_HzQtmPlcmMode_Type.__name__ = "Integer32"
_HzQtmPlcmMode_Object = MibScalar
hzQtmPlcmMode = _HzQtmPlcmMode_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 1, 13, 1),
    _HzQtmPlcmMode_Type()
)
hzQtmPlcmMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzQtmPlcmMode.setStatus("current")


class _HzQtmPlcmConfigQtmAsDuo_Type(Integer32):
    """Custom type hzQtmPlcmConfigQtmAsDuo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_HzQtmPlcmConfigQtmAsDuo_Type.__name__ = "Integer32"
_HzQtmPlcmConfigQtmAsDuo_Object = MibScalar
hzQtmPlcmConfigQtmAsDuo = _HzQtmPlcmConfigQtmAsDuo_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 1, 13, 2),
    _HzQtmPlcmConfigQtmAsDuo_Type()
)
hzQtmPlcmConfigQtmAsDuo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzQtmPlcmConfigQtmAsDuo.setStatus("current")
_HzQtmPlcmPeerOmniVersionTable_Object = MibTable
hzQtmPlcmPeerOmniVersionTable = _HzQtmPlcmPeerOmniVersionTable_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 1, 13, 3)
)
if mibBuilder.loadTexts:
    hzQtmPlcmPeerOmniVersionTable.setStatus("current")
_HzQtmPlcmPeerOmniVersionEntry_Object = MibTableRow
hzQtmPlcmPeerOmniVersionEntry = _HzQtmPlcmPeerOmniVersionEntry_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 1, 13, 3, 1)
)
hzQtmPlcmPeerOmniVersionEntry.setIndexNames(
    (0, "DRAGONWAVE-HORIZON-QUANTUM-MIB", "hzQtmPlcmPeerOmniVersionIndex"),
)
if mibBuilder.loadTexts:
    hzQtmPlcmPeerOmniVersionEntry.setStatus("current")
_HzQtmPlcmPeerOmniVersionIndex_Type = Integer32
_HzQtmPlcmPeerOmniVersionIndex_Object = MibTableColumn
hzQtmPlcmPeerOmniVersionIndex = _HzQtmPlcmPeerOmniVersionIndex_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 1, 13, 3, 1, 1),
    _HzQtmPlcmPeerOmniVersionIndex_Type()
)
hzQtmPlcmPeerOmniVersionIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzQtmPlcmPeerOmniVersionIndex.setStatus("current")
_HzQtmPlcmPeerOmniVersionName_Type = DisplayString
_HzQtmPlcmPeerOmniVersionName_Object = MibTableColumn
hzQtmPlcmPeerOmniVersionName = _HzQtmPlcmPeerOmniVersionName_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 1, 13, 3, 1, 2),
    _HzQtmPlcmPeerOmniVersionName_Type()
)
hzQtmPlcmPeerOmniVersionName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzQtmPlcmPeerOmniVersionName.setStatus("current")


class _HzQtmPlcmPeerOmniVersionProgrammed_Type(Integer32):
    """Custom type hzQtmPlcmPeerOmniVersionProgrammed based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("notActive", 2))
    )


_HzQtmPlcmPeerOmniVersionProgrammed_Type.__name__ = "Integer32"
_HzQtmPlcmPeerOmniVersionProgrammed_Object = MibTableColumn
hzQtmPlcmPeerOmniVersionProgrammed = _HzQtmPlcmPeerOmniVersionProgrammed_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 1, 13, 3, 1, 3),
    _HzQtmPlcmPeerOmniVersionProgrammed_Type()
)
hzQtmPlcmPeerOmniVersionProgrammed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzQtmPlcmPeerOmniVersionProgrammed.setStatus("current")


class _HzQtmPlcmMgtInterface_Type(Integer32):
    """Custom type hzQtmPlcmMgtInterface based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("inBand", 1),
          ("outOfBand", 2),
          ("port2extened", 3))
    )


_HzQtmPlcmMgtInterface_Type.__name__ = "Integer32"
_HzQtmPlcmMgtInterface_Object = MibScalar
hzQtmPlcmMgtInterface = _HzQtmPlcmMgtInterface_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 1, 13, 4),
    _HzQtmPlcmMgtInterface_Type()
)
hzQtmPlcmMgtInterface.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzQtmPlcmMgtInterface.setStatus("current")


class _HzQtmPlcmDataPort_Type(Integer32):
    """Custom type hzQtmPlcmDataPort based on Integer32"""
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
        *(("p1", 1),
          ("p2", 2),
          ("p3", 3),
          ("p4", 4),
          ("p5", 5),
          ("p6", 6),
          ("p7", 7),
          ("p8", 8))
    )


_HzQtmPlcmDataPort_Type.__name__ = "Integer32"
_HzQtmPlcmDataPort_Object = MibScalar
hzQtmPlcmDataPort = _HzQtmPlcmDataPort_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 1, 13, 5),
    _HzQtmPlcmDataPort_Type()
)
hzQtmPlcmDataPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzQtmPlcmDataPort.setStatus("current")


class _HzQtmPlcmDataVlanTag_Type(Integer32):
    """Custom type hzQtmPlcmDataVlanTag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_HzQtmPlcmDataVlanTag_Type.__name__ = "Integer32"
_HzQtmPlcmDataVlanTag_Object = MibScalar
hzQtmPlcmDataVlanTag = _HzQtmPlcmDataVlanTag_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 1, 13, 6),
    _HzQtmPlcmDataVlanTag_Type()
)
hzQtmPlcmDataVlanTag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzQtmPlcmDataVlanTag.setStatus("current")


class _HzQtmPlcmMgmtPort_Type(Integer32):
    """Custom type hzQtmPlcmMgmtPort based on Integer32"""
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
        *(("p1", 1),
          ("p2", 2),
          ("p3", 3),
          ("p4", 4),
          ("p5", 5),
          ("p6", 6),
          ("p7", 7),
          ("p8", 8))
    )


_HzQtmPlcmMgmtPort_Type.__name__ = "Integer32"
_HzQtmPlcmMgmtPort_Object = MibScalar
hzQtmPlcmMgmtPort = _HzQtmPlcmMgmtPort_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 1, 13, 7),
    _HzQtmPlcmMgmtPort_Type()
)
hzQtmPlcmMgmtPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzQtmPlcmMgmtPort.setStatus("current")


class _HzQtmPlcmMgmtVlanTagging_Type(Integer32):
    """Custom type hzQtmPlcmMgmtVlanTagging based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_HzQtmPlcmMgmtVlanTagging_Type.__name__ = "Integer32"
_HzQtmPlcmMgmtVlanTagging_Object = MibScalar
hzQtmPlcmMgmtVlanTagging = _HzQtmPlcmMgmtVlanTagging_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 1, 13, 8),
    _HzQtmPlcmMgmtVlanTagging_Type()
)
hzQtmPlcmMgmtVlanTagging.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzQtmPlcmMgmtVlanTagging.setStatus("current")


class _HzQtmPlcmMgmtVlanTag_Type(Integer32):
    """Custom type hzQtmPlcmMgmtVlanTag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_HzQtmPlcmMgmtVlanTag_Type.__name__ = "Integer32"
_HzQtmPlcmMgmtVlanTag_Object = MibScalar
hzQtmPlcmMgmtVlanTag = _HzQtmPlcmMgmtVlanTag_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 1, 13, 9),
    _HzQtmPlcmMgmtVlanTag_Type()
)
hzQtmPlcmMgmtVlanTag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzQtmPlcmMgmtVlanTag.setStatus("current")


class _HzQtmPlcmMgmtTagPriority_Type(Integer32):
    """Custom type hzQtmPlcmMgmtTagPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_HzQtmPlcmMgmtTagPriority_Type.__name__ = "Integer32"
_HzQtmPlcmMgmtTagPriority_Object = MibScalar
hzQtmPlcmMgmtTagPriority = _HzQtmPlcmMgmtTagPriority_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 1, 13, 10),
    _HzQtmPlcmMgmtTagPriority_Type()
)
hzQtmPlcmMgmtTagPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzQtmPlcmMgmtTagPriority.setStatus("current")


class _HzQtmPlcmApplySaveResetSystem_Type(Integer32):
    """Custom type hzQtmPlcmApplySaveResetSystem based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("applySaveReset", 1)
    )


_HzQtmPlcmApplySaveResetSystem_Type.__name__ = "Integer32"
_HzQtmPlcmApplySaveResetSystem_Object = MibScalar
hzQtmPlcmApplySaveResetSystem = _HzQtmPlcmApplySaveResetSystem_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 1, 13, 20),
    _HzQtmPlcmApplySaveResetSystem_Type()
)
hzQtmPlcmApplySaveResetSystem.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzQtmPlcmApplySaveResetSystem.setStatus("current")
_HzQtmBandwidthDoubling_ObjectIdentity = ObjectIdentity
hzQtmBandwidthDoubling = _HzQtmBandwidthDoubling_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 1, 14)
)


class _HzQtmBandwidthDoublingMode_Type(Integer32):
    """Custom type hzQtmBandwidthDoublingMode based on Integer32"""
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
        *(("off", 1),
          ("primary", 2),
          ("secondary", 3))
    )


_HzQtmBandwidthDoublingMode_Type.__name__ = "Integer32"
_HzQtmBandwidthDoublingMode_Object = MibScalar
hzQtmBandwidthDoublingMode = _HzQtmBandwidthDoublingMode_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 1, 14, 1),
    _HzQtmBandwidthDoublingMode_Type()
)
hzQtmBandwidthDoublingMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzQtmBandwidthDoublingMode.setStatus("current")


class _HzQtmBandwidthDoublingActualMode_Type(Integer32):
    """Custom type hzQtmBandwidthDoublingActualMode based on Integer32"""
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
          ("primary", 2),
          ("secondary", 3))
    )


_HzQtmBandwidthDoublingActualMode_Type.__name__ = "Integer32"
_HzQtmBandwidthDoublingActualMode_Object = MibScalar
hzQtmBandwidthDoublingActualMode = _HzQtmBandwidthDoublingActualMode_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 1, 14, 2),
    _HzQtmBandwidthDoublingActualMode_Type()
)
hzQtmBandwidthDoublingActualMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzQtmBandwidthDoublingActualMode.setStatus("current")


class _HzQtmBandwidthDoublingPort_Type(Integer32):
    """Custom type hzQtmBandwidthDoublingPort based on Integer32"""
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
        *(("enet-port-none", 1),
          ("enet-port-1", 2),
          ("enet-port-2", 3),
          ("enet-port-3", 4),
          ("enet-port-4", 5),
          ("enet-port-5", 6),
          ("enet-port-6", 7),
          ("enet-port-7", 8),
          ("enet-port-8", 9))
    )


_HzQtmBandwidthDoublingPort_Type.__name__ = "Integer32"
_HzQtmBandwidthDoublingPort_Object = MibScalar
hzQtmBandwidthDoublingPort = _HzQtmBandwidthDoublingPort_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 1, 14, 3),
    _HzQtmBandwidthDoublingPort_Type()
)
hzQtmBandwidthDoublingPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzQtmBandwidthDoublingPort.setStatus("current")


class _HzQtmBandwidthDoublingActualPort_Type(Integer32):
    """Custom type hzQtmBandwidthDoublingActualPort based on Integer32"""
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
        *(("enet-port-none", 1),
          ("enet-port-1", 2),
          ("enet-port-2", 3),
          ("enet-port-3", 4),
          ("enet-port-4", 5),
          ("enet-port-5", 6),
          ("enet-port-6", 7),
          ("enet-port-7", 8),
          ("enet-port-8", 9))
    )


_HzQtmBandwidthDoublingActualPort_Type.__name__ = "Integer32"
_HzQtmBandwidthDoublingActualPort_Object = MibScalar
hzQtmBandwidthDoublingActualPort = _HzQtmBandwidthDoublingActualPort_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 1, 14, 4),
    _HzQtmBandwidthDoublingActualPort_Type()
)
hzQtmBandwidthDoublingActualPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzQtmBandwidthDoublingActualPort.setStatus("current")
_HzQtmSyncE_ObjectIdentity = ObjectIdentity
hzQtmSyncE = _HzQtmSyncE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 1, 15)
)


class _HzQtmSyncEMode_Type(Integer32):
    """Custom type hzQtmSyncEMode based on Integer32"""
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
        *(("off", 1),
          ("manual", 2),
          ("auto", 3),
          ("esmc", 4))
    )


_HzQtmSyncEMode_Type.__name__ = "Integer32"
_HzQtmSyncEMode_Object = MibScalar
hzQtmSyncEMode = _HzQtmSyncEMode_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 1, 15, 1),
    _HzQtmSyncEMode_Type()
)
hzQtmSyncEMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzQtmSyncEMode.setStatus("current")


class _HzQtmSyncEPrimarySource_Type(Integer32):
    """Custom type hzQtmSyncEPrimarySource based on Integer32"""
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
        *(("p3", 1),
          ("p4", 2),
          ("p5", 3),
          ("p6", 4),
          ("p7", 5),
          ("p8", 6),
          ("wp1", 7),
          ("wp2", 8),
          ("free-run", 9))
    )


_HzQtmSyncEPrimarySource_Type.__name__ = "Integer32"
_HzQtmSyncEPrimarySource_Object = MibScalar
hzQtmSyncEPrimarySource = _HzQtmSyncEPrimarySource_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 1, 15, 2),
    _HzQtmSyncEPrimarySource_Type()
)
hzQtmSyncEPrimarySource.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzQtmSyncEPrimarySource.setStatus("current")


class _HzQtmSyncESecondarySource_Type(Integer32):
    """Custom type hzQtmSyncESecondarySource based on Integer32"""
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
        *(("p3", 1),
          ("p4", 2),
          ("p5", 3),
          ("p6", 4),
          ("p7", 5),
          ("p8", 6),
          ("wp1", 7),
          ("wp2", 8),
          ("free-run", 9))
    )


_HzQtmSyncESecondarySource_Type.__name__ = "Integer32"
_HzQtmSyncESecondarySource_Object = MibScalar
hzQtmSyncESecondarySource = _HzQtmSyncESecondarySource_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 1, 15, 3),
    _HzQtmSyncESecondarySource_Type()
)
hzQtmSyncESecondarySource.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzQtmSyncESecondarySource.setStatus("current")
_HzQtmSyncEMemberPorts_Type = DisplayString
_HzQtmSyncEMemberPorts_Object = MibScalar
hzQtmSyncEMemberPorts = _HzQtmSyncEMemberPorts_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 1, 15, 4),
    _HzQtmSyncEMemberPorts_Type()
)
hzQtmSyncEMemberPorts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzQtmSyncEMemberPorts.setStatus("current")
_HzQtmSyncEForcedHoldover_Type = DisplayString
_HzQtmSyncEForcedHoldover_Object = MibScalar
hzQtmSyncEForcedHoldover = _HzQtmSyncEForcedHoldover_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 1, 15, 5),
    _HzQtmSyncEForcedHoldover_Type()
)
hzQtmSyncEForcedHoldover.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzQtmSyncEForcedHoldover.setStatus("current")
_HzQtmSyncERevertive_Type = DisplayString
_HzQtmSyncERevertive_Object = MibScalar
hzQtmSyncERevertive = _HzQtmSyncERevertive_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 1, 15, 6),
    _HzQtmSyncERevertive_Type()
)
hzQtmSyncERevertive.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzQtmSyncERevertive.setStatus("current")


class _HzQtmSyncEClockSource_Type(Integer32):
    """Custom type hzQtmSyncEClockSource based on Integer32"""
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
        *(("p3", 1),
          ("p4", 2),
          ("p5", 3),
          ("p6", 4),
          ("p7", 5),
          ("p8", 6),
          ("wp1", 7),
          ("wp2", 8),
          ("free-run", 9))
    )


_HzQtmSyncEClockSource_Type.__name__ = "Integer32"
_HzQtmSyncEClockSource_Object = MibScalar
hzQtmSyncEClockSource = _HzQtmSyncEClockSource_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 1, 15, 7),
    _HzQtmSyncEClockSource_Type()
)
hzQtmSyncEClockSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzQtmSyncEClockSource.setStatus("current")
_HzQtmSyncEAcquisitionStatus_Type = DisplayString
_HzQtmSyncEAcquisitionStatus_Object = MibScalar
hzQtmSyncEAcquisitionStatus = _HzQtmSyncEAcquisitionStatus_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 1, 15, 8),
    _HzQtmSyncEAcquisitionStatus_Type()
)
hzQtmSyncEAcquisitionStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzQtmSyncEAcquisitionStatus.setStatus("current")


class _HzQtmSyncEWanderFilter_Type(Integer32):
    """Custom type hzQtmSyncEWanderFilter based on Integer32"""
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


_HzQtmSyncEWanderFilter_Type.__name__ = "Integer32"
_HzQtmSyncEWanderFilter_Object = MibScalar
hzQtmSyncEWanderFilter = _HzQtmSyncEWanderFilter_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 1, 15, 9),
    _HzQtmSyncEWanderFilter_Type()
)
hzQtmSyncEWanderFilter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzQtmSyncEWanderFilter.setStatus("current")
_HzQtmAuthentication_ObjectIdentity = ObjectIdentity
hzQtmAuthentication = _HzQtmAuthentication_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 2)
)


class _HzQtmUniquePeerAuthenticationKey_Type(DisplayString):
    """Custom type hzQtmUniquePeerAuthenticationKey based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 34),
    )


_HzQtmUniquePeerAuthenticationKey_Type.__name__ = "DisplayString"
_HzQtmUniquePeerAuthenticationKey_Object = MibScalar
hzQtmUniquePeerAuthenticationKey = _HzQtmUniquePeerAuthenticationKey_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 2, 1),
    _HzQtmUniquePeerAuthenticationKey_Type()
)
hzQtmUniquePeerAuthenticationKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzQtmUniquePeerAuthenticationKey.setStatus("current")
_HzQtmPeerDetectedSerialNumber_Type = DisplayString
_HzQtmPeerDetectedSerialNumber_Object = MibScalar
hzQtmPeerDetectedSerialNumber = _HzQtmPeerDetectedSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 2, 2),
    _HzQtmPeerDetectedSerialNumber_Type()
)
hzQtmPeerDetectedSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzQtmPeerDetectedSerialNumber.setStatus("current")


class _HzQtmAuthenticationMode_Type(Integer32):
    """Custom type hzQtmAuthenticationMode based on Integer32"""
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
        *(("none", 1),
          ("unique", 2),
          ("group", 3))
    )


_HzQtmAuthenticationMode_Type.__name__ = "Integer32"
_HzQtmAuthenticationMode_Object = MibScalar
hzQtmAuthenticationMode = _HzQtmAuthenticationMode_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 2, 3),
    _HzQtmAuthenticationMode_Type()
)
hzQtmAuthenticationMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzQtmAuthenticationMode.setStatus("current")


class _HzQtmAuthenticationFailureAction_Type(Integer32):
    """Custom type hzQtmAuthenticationFailureAction based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("blockTraffic", 1),
          ("passTraffic", 2))
    )


_HzQtmAuthenticationFailureAction_Type.__name__ = "Integer32"
_HzQtmAuthenticationFailureAction_Object = MibScalar
hzQtmAuthenticationFailureAction = _HzQtmAuthenticationFailureAction_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 2, 4),
    _HzQtmAuthenticationFailureAction_Type()
)
hzQtmAuthenticationFailureAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzQtmAuthenticationFailureAction.setStatus("current")


class _HzQtmPeerAuthenticationStatus_Type(Integer32):
    """Custom type hzQtmPeerAuthenticationStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("notAuthenticated", 1),
          ("authenticated", 2),
          ("explicitAuthenticationFailure", 3))
    )


_HzQtmPeerAuthenticationStatus_Type.__name__ = "Integer32"
_HzQtmPeerAuthenticationStatus_Object = MibScalar
hzQtmPeerAuthenticationStatus = _HzQtmPeerAuthenticationStatus_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 2, 5),
    _HzQtmPeerAuthenticationStatus_Type()
)
hzQtmPeerAuthenticationStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzQtmPeerAuthenticationStatus.setStatus("current")


class _HzQtmGroupAuthenticationKey_Type(DisplayString):
    """Custom type hzQtmGroupAuthenticationKey based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 34),
    )


_HzQtmGroupAuthenticationKey_Type.__name__ = "DisplayString"
_HzQtmGroupAuthenticationKey_Object = MibScalar
hzQtmGroupAuthenticationKey = _HzQtmGroupAuthenticationKey_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 2, 6),
    _HzQtmGroupAuthenticationKey_Type()
)
hzQtmGroupAuthenticationKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzQtmGroupAuthenticationKey.setStatus("current")
_HzQtmNetworkManagement_ObjectIdentity = ObjectIdentity
hzQtmNetworkManagement = _HzQtmNetworkManagement_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 3)
)
_HzQtmMacAddress_Type = DisplayString
_HzQtmMacAddress_Object = MibScalar
hzQtmMacAddress = _HzQtmMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 3, 1),
    _HzQtmMacAddress_Type()
)
hzQtmMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzQtmMacAddress.setStatus("current")
_HzQtmIpAddress_Type = IpAddress
_HzQtmIpAddress_Object = MibScalar
hzQtmIpAddress = _HzQtmIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 3, 2),
    _HzQtmIpAddress_Type()
)
hzQtmIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzQtmIpAddress.setStatus("current")
_HzQtmSubnetMask_Type = IpAddress
_HzQtmSubnetMask_Object = MibScalar
hzQtmSubnetMask = _HzQtmSubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 3, 3),
    _HzQtmSubnetMask_Type()
)
hzQtmSubnetMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzQtmSubnetMask.setStatus("current")
_HzQtmDefaultGateway_Type = IpAddress
_HzQtmDefaultGateway_Object = MibScalar
hzQtmDefaultGateway = _HzQtmDefaultGateway_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 3, 4),
    _HzQtmDefaultGateway_Type()
)
hzQtmDefaultGateway.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzQtmDefaultGateway.setStatus("current")


class _HzQtmTelnetAccessMode_Type(Integer32):
    """Custom type hzQtmTelnetAccessMode based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_HzQtmTelnetAccessMode_Type.__name__ = "Integer32"
_HzQtmTelnetAccessMode_Object = MibScalar
hzQtmTelnetAccessMode = _HzQtmTelnetAccessMode_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 3, 5),
    _HzQtmTelnetAccessMode_Type()
)
hzQtmTelnetAccessMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzQtmTelnetAccessMode.setStatus("current")


class _HzQtmSshAccessMode_Type(Integer32):
    """Custom type hzQtmSshAccessMode based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_HzQtmSshAccessMode_Type.__name__ = "Integer32"
_HzQtmSshAccessMode_Object = MibScalar
hzQtmSshAccessMode = _HzQtmSshAccessMode_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 3, 6),
    _HzQtmSshAccessMode_Type()
)
hzQtmSshAccessMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzQtmSshAccessMode.setStatus("current")
_HzQtmNetworkManagementInterface_ObjectIdentity = ObjectIdentity
hzQtmNetworkManagementInterface = _HzQtmNetworkManagementInterface_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 3, 8)
)
_HzQtmNetMgmtPortList_Type = DisplayString
_HzQtmNetMgmtPortList_Object = MibScalar
hzQtmNetMgmtPortList = _HzQtmNetMgmtPortList_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 3, 8, 1),
    _HzQtmNetMgmtPortList_Type()
)
hzQtmNetMgmtPortList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzQtmNetMgmtPortList.setStatus("current")


class _HzQtmNetMgmtVlanTagId_Type(Integer32):
    """Custom type hzQtmNetMgmtVlanTagId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_HzQtmNetMgmtVlanTagId_Type.__name__ = "Integer32"
_HzQtmNetMgmtVlanTagId_Object = MibScalar
hzQtmNetMgmtVlanTagId = _HzQtmNetMgmtVlanTagId_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 3, 8, 2),
    _HzQtmNetMgmtVlanTagId_Type()
)
hzQtmNetMgmtVlanTagId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzQtmNetMgmtVlanTagId.setStatus("current")


class _HzQtmNetMgmtVlanTagPriority_Type(Integer32):
    """Custom type hzQtmNetMgmtVlanTagPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_HzQtmNetMgmtVlanTagPriority_Type.__name__ = "Integer32"
_HzQtmNetMgmtVlanTagPriority_Object = MibScalar
hzQtmNetMgmtVlanTagPriority = _HzQtmNetMgmtVlanTagPriority_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 3, 8, 3),
    _HzQtmNetMgmtVlanTagPriority_Type()
)
hzQtmNetMgmtVlanTagPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzQtmNetMgmtVlanTagPriority.setStatus("current")
_HzQtmNetworkInterface_ObjectIdentity = ObjectIdentity
hzQtmNetworkInterface = _HzQtmNetworkInterface_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 4)
)
_HzQtmEnetPort_ObjectIdentity = ObjectIdentity
hzQtmEnetPort = _HzQtmEnetPort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 4, 1)
)
_HzQtmEnetPortConfigTable_Object = MibTable
hzQtmEnetPortConfigTable = _HzQtmEnetPortConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 4, 1, 1)
)
if mibBuilder.loadTexts:
    hzQtmEnetPortConfigTable.setStatus("current")
_HzQtmEnetPortConfigEntry_Object = MibTableRow
hzQtmEnetPortConfigEntry = _HzQtmEnetPortConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 4, 1, 1, 1)
)
hzQtmEnetPortConfigEntry.setIndexNames(
    (0, "DRAGONWAVE-HORIZON-QUANTUM-MIB", "hzQtmEnetPortIndex"),
)
if mibBuilder.loadTexts:
    hzQtmEnetPortConfigEntry.setStatus("current")


class _HzQtmEnetPortIndex_Type(Integer32):
    """Custom type hzQtmEnetPortIndex based on Integer32"""
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
        *(("enet-port-1", 1),
          ("enet-port-2", 2),
          ("enet-port-3", 3),
          ("enet-port-4", 4),
          ("enet-port-5", 5),
          ("enet-port-6", 6),
          ("enet-port-7", 7),
          ("enet-port-8", 8))
    )


_HzQtmEnetPortIndex_Type.__name__ = "Integer32"
_HzQtmEnetPortIndex_Object = MibTableColumn
hzQtmEnetPortIndex = _HzQtmEnetPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 4, 1, 1, 1, 1),
    _HzQtmEnetPortIndex_Type()
)
hzQtmEnetPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzQtmEnetPortIndex.setStatus("current")
_HzQtmEnetPortName_Type = DisplayString
_HzQtmEnetPortName_Object = MibTableColumn
hzQtmEnetPortName = _HzQtmEnetPortName_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 4, 1, 1, 1, 2),
    _HzQtmEnetPortName_Type()
)
hzQtmEnetPortName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzQtmEnetPortName.setStatus("current")


class _HzQtmEnetPortAutoNegotiation_Type(Integer32):
    """Custom type hzQtmEnetPortAutoNegotiation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("on", 1),
          ("off", 2))
    )


_HzQtmEnetPortAutoNegotiation_Type.__name__ = "Integer32"
_HzQtmEnetPortAutoNegotiation_Object = MibTableColumn
hzQtmEnetPortAutoNegotiation = _HzQtmEnetPortAutoNegotiation_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 4, 1, 1, 1, 3),
    _HzQtmEnetPortAutoNegotiation_Type()
)
hzQtmEnetPortAutoNegotiation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzQtmEnetPortAutoNegotiation.setStatus("current")


class _HzQtmEnetPortSpeed_Type(Integer32):
    """Custom type hzQtmEnetPortSpeed based on Integer32"""
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
        *(("x10M", 1),
          ("x100M", 2),
          ("x1000M", 3),
          ("auto", 4))
    )


_HzQtmEnetPortSpeed_Type.__name__ = "Integer32"
_HzQtmEnetPortSpeed_Object = MibTableColumn
hzQtmEnetPortSpeed = _HzQtmEnetPortSpeed_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 4, 1, 1, 1, 4),
    _HzQtmEnetPortSpeed_Type()
)
hzQtmEnetPortSpeed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzQtmEnetPortSpeed.setStatus("current")


class _HzQtmEnetPortDuplex_Type(Integer32):
    """Custom type hzQtmEnetPortDuplex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("full", 1),
          ("half", 2),
          ("auto", 3))
    )


_HzQtmEnetPortDuplex_Type.__name__ = "Integer32"
_HzQtmEnetPortDuplex_Object = MibTableColumn
hzQtmEnetPortDuplex = _HzQtmEnetPortDuplex_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 4, 1, 1, 1, 5),
    _HzQtmEnetPortDuplex_Type()
)
hzQtmEnetPortDuplex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzQtmEnetPortDuplex.setStatus("current")


class _HzQtmEnetPortMedia_Type(Integer32):
    """Custom type hzQtmEnetPortMedia based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("copper", 1),
          ("sfp", 2),
          ("auto", 3))
    )


_HzQtmEnetPortMedia_Type.__name__ = "Integer32"
_HzQtmEnetPortMedia_Object = MibTableColumn
hzQtmEnetPortMedia = _HzQtmEnetPortMedia_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 4, 1, 1, 1, 6),
    _HzQtmEnetPortMedia_Type()
)
hzQtmEnetPortMedia.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzQtmEnetPortMedia.setStatus("current")


class _HzQtmEnetPortAdminState_Type(Integer32):
    """Custom type hzQtmEnetPortAdminState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("on", 1),
          ("off", 2))
    )


_HzQtmEnetPortAdminState_Type.__name__ = "Integer32"
_HzQtmEnetPortAdminState_Object = MibTableColumn
hzQtmEnetPortAdminState = _HzQtmEnetPortAdminState_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 4, 1, 1, 1, 7),
    _HzQtmEnetPortAdminState_Type()
)
hzQtmEnetPortAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzQtmEnetPortAdminState.setStatus("current")


class _HzQtmEnetPortPauseFrame_Type(Integer32):
    """Custom type hzQtmEnetPortPauseFrame based on Integer32"""
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
        *(("disabled", 1),
          ("enableRx", 2),
          ("enableTx", 3),
          ("enableBoth", 4))
    )


_HzQtmEnetPortPauseFrame_Type.__name__ = "Integer32"
_HzQtmEnetPortPauseFrame_Object = MibTableColumn
hzQtmEnetPortPauseFrame = _HzQtmEnetPortPauseFrame_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 4, 1, 1, 1, 8),
    _HzQtmEnetPortPauseFrame_Type()
)
hzQtmEnetPortPauseFrame.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzQtmEnetPortPauseFrame.setStatus("current")


class _HzQtmEnetPortMaxFrameSize_Type(Integer32):
    """Custom type hzQtmEnetPortMaxFrameSize based on Integer32"""
    defaultValue = 1600

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1600, 9600),
    )


_HzQtmEnetPortMaxFrameSize_Type.__name__ = "Integer32"
_HzQtmEnetPortMaxFrameSize_Object = MibTableColumn
hzQtmEnetPortMaxFrameSize = _HzQtmEnetPortMaxFrameSize_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 4, 1, 1, 1, 9),
    _HzQtmEnetPortMaxFrameSize_Type()
)
hzQtmEnetPortMaxFrameSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzQtmEnetPortMaxFrameSize.setStatus("current")
_HzQtmEnetPortStatusTable_Object = MibTable
hzQtmEnetPortStatusTable = _HzQtmEnetPortStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 4, 1, 2)
)
if mibBuilder.loadTexts:
    hzQtmEnetPortStatusTable.setStatus("current")
_HzQtmEnetPortStatusEntry_Object = MibTableRow
hzQtmEnetPortStatusEntry = _HzQtmEnetPortStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 4, 1, 2, 1)
)
hzQtmEnetPortStatusEntry.setIndexNames(
    (0, "DRAGONWAVE-HORIZON-QUANTUM-MIB", "hzQtmEnetPortStatusIndex"),
)
if mibBuilder.loadTexts:
    hzQtmEnetPortStatusEntry.setStatus("current")


class _HzQtmEnetPortStatusIndex_Type(Integer32):
    """Custom type hzQtmEnetPortStatusIndex based on Integer32"""
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
        *(("enet-port-1", 1),
          ("enet-port-2", 2),
          ("enet-port-3", 3),
          ("enet-port-4", 4),
          ("enet-port-5", 5),
          ("enet-port-6", 6),
          ("enet-port-7", 7),
          ("enet-port-8", 8))
    )


_HzQtmEnetPortStatusIndex_Type.__name__ = "Integer32"
_HzQtmEnetPortStatusIndex_Object = MibTableColumn
hzQtmEnetPortStatusIndex = _HzQtmEnetPortStatusIndex_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 4, 1, 2, 1, 1),
    _HzQtmEnetPortStatusIndex_Type()
)
hzQtmEnetPortStatusIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzQtmEnetPortStatusIndex.setStatus("current")


class _HzQtmEnetPortLinkStatus_Type(Integer32):
    """Custom type hzQtmEnetPortLinkStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("down", 1),
          ("up", 2),
          ("invalid", 3))
    )


_HzQtmEnetPortLinkStatus_Type.__name__ = "Integer32"
_HzQtmEnetPortLinkStatus_Object = MibTableColumn
hzQtmEnetPortLinkStatus = _HzQtmEnetPortLinkStatus_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 4, 1, 2, 1, 2),
    _HzQtmEnetPortLinkStatus_Type()
)
hzQtmEnetPortLinkStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzQtmEnetPortLinkStatus.setStatus("current")


class _HzQtmEnetPortAutoNegotiationStatus_Type(Integer32):
    """Custom type hzQtmEnetPortAutoNegotiationStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("on", 1),
          ("off", 2),
          ("invalid", 3))
    )


_HzQtmEnetPortAutoNegotiationStatus_Type.__name__ = "Integer32"
_HzQtmEnetPortAutoNegotiationStatus_Object = MibTableColumn
hzQtmEnetPortAutoNegotiationStatus = _HzQtmEnetPortAutoNegotiationStatus_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 4, 1, 2, 1, 3),
    _HzQtmEnetPortAutoNegotiationStatus_Type()
)
hzQtmEnetPortAutoNegotiationStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzQtmEnetPortAutoNegotiationStatus.setStatus("current")


class _HzQtmEnetPortSpeedStatus_Type(Integer32):
    """Custom type hzQtmEnetPortSpeedStatus based on Integer32"""
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
        *(("x10M", 1),
          ("x100M", 2),
          ("x1000M", 3),
          ("auto", 4),
          ("invalid", 5))
    )


_HzQtmEnetPortSpeedStatus_Type.__name__ = "Integer32"
_HzQtmEnetPortSpeedStatus_Object = MibTableColumn
hzQtmEnetPortSpeedStatus = _HzQtmEnetPortSpeedStatus_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 4, 1, 2, 1, 4),
    _HzQtmEnetPortSpeedStatus_Type()
)
hzQtmEnetPortSpeedStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzQtmEnetPortSpeedStatus.setStatus("current")


class _HzQtmEnetPortDuplexStatus_Type(Integer32):
    """Custom type hzQtmEnetPortDuplexStatus based on Integer32"""
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
        *(("full", 1),
          ("half", 2),
          ("auto", 3),
          ("invalid", 4))
    )


_HzQtmEnetPortDuplexStatus_Type.__name__ = "Integer32"
_HzQtmEnetPortDuplexStatus_Object = MibTableColumn
hzQtmEnetPortDuplexStatus = _HzQtmEnetPortDuplexStatus_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 4, 1, 2, 1, 5),
    _HzQtmEnetPortDuplexStatus_Type()
)
hzQtmEnetPortDuplexStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzQtmEnetPortDuplexStatus.setStatus("current")


class _HzQtmEnetPortMediaStatus_Type(Integer32):
    """Custom type hzQtmEnetPortMediaStatus based on Integer32"""
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
        *(("copper", 1),
          ("fiber", 2),
          ("auto", 3),
          ("invalid", 4))
    )


_HzQtmEnetPortMediaStatus_Type.__name__ = "Integer32"
_HzQtmEnetPortMediaStatus_Object = MibTableColumn
hzQtmEnetPortMediaStatus = _HzQtmEnetPortMediaStatus_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 4, 1, 2, 1, 6),
    _HzQtmEnetPortMediaStatus_Type()
)
hzQtmEnetPortMediaStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzQtmEnetPortMediaStatus.setStatus("current")
_HzQtmEnetPortStatsTable_Object = MibTable
hzQtmEnetPortStatsTable = _HzQtmEnetPortStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 4, 1, 3)
)
if mibBuilder.loadTexts:
    hzQtmEnetPortStatsTable.setStatus("current")
_HzQtmEnetPortStatsEntry_Object = MibTableRow
hzQtmEnetPortStatsEntry = _HzQtmEnetPortStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 4, 1, 3, 1)
)
hzQtmEnetPortStatsEntry.setIndexNames(
    (0, "DRAGONWAVE-HORIZON-QUANTUM-MIB", "hzQtmEnetPortStatsIndex"),
)
if mibBuilder.loadTexts:
    hzQtmEnetPortStatsEntry.setStatus("current")


class _HzQtmEnetPortStatsIndex_Type(Integer32):
    """Custom type hzQtmEnetPortStatsIndex based on Integer32"""
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
        *(("enet-port-1", 1),
          ("enet-port-2", 2),
          ("enet-port-3", 3),
          ("enet-port-4", 4),
          ("enet-port-5", 5),
          ("enet-port-6", 6),
          ("enet-port-7", 7),
          ("enet-port-8", 8))
    )


_HzQtmEnetPortStatsIndex_Type.__name__ = "Integer32"
_HzQtmEnetPortStatsIndex_Object = MibTableColumn
hzQtmEnetPortStatsIndex = _HzQtmEnetPortStatsIndex_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 4, 1, 3, 1, 1),
    _HzQtmEnetPortStatsIndex_Type()
)
hzQtmEnetPortStatsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzQtmEnetPortStatsIndex.setStatus("current")
_HzQtmEnetPortRxBytes_Type = Counter64
_HzQtmEnetPortRxBytes_Object = MibTableColumn
hzQtmEnetPortRxBytes = _HzQtmEnetPortRxBytes_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 4, 1, 3, 1, 2),
    _HzQtmEnetPortRxBytes_Type()
)
hzQtmEnetPortRxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzQtmEnetPortRxBytes.setStatus("current")
_HzQtmEnetPortRxUcastPkts_Type = Counter64
_HzQtmEnetPortRxUcastPkts_Object = MibTableColumn
hzQtmEnetPortRxUcastPkts = _HzQtmEnetPortRxUcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 4, 1, 3, 1, 3),
    _HzQtmEnetPortRxUcastPkts_Type()
)
hzQtmEnetPortRxUcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzQtmEnetPortRxUcastPkts.setStatus("current")
_HzQtmEnetPortRxNUcastPkts_Type = Counter64
_HzQtmEnetPortRxNUcastPkts_Object = MibTableColumn
hzQtmEnetPortRxNUcastPkts = _HzQtmEnetPortRxNUcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 4, 1, 3, 1, 4),
    _HzQtmEnetPortRxNUcastPkts_Type()
)
hzQtmEnetPortRxNUcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzQtmEnetPortRxNUcastPkts.setStatus("current")
_HzQtmEnetPortRxDiscards_Type = Counter64
_HzQtmEnetPortRxDiscards_Object = MibTableColumn
hzQtmEnetPortRxDiscards = _HzQtmEnetPortRxDiscards_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 4, 1, 3, 1, 5),
    _HzQtmEnetPortRxDiscards_Type()
)
hzQtmEnetPortRxDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzQtmEnetPortRxDiscards.setStatus("current")
_HzQtmEnetPortRxErrors_Type = Counter64
_HzQtmEnetPortRxErrors_Object = MibTableColumn
hzQtmEnetPortRxErrors = _HzQtmEnetPortRxErrors_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 4, 1, 3, 1, 6),
    _HzQtmEnetPortRxErrors_Type()
)
hzQtmEnetPortRxErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzQtmEnetPortRxErrors.setStatus("current")
_HzQtmEnetPortRxUnknownProtos_Type = Counter64
_HzQtmEnetPortRxUnknownProtos_Object = MibTableColumn
hzQtmEnetPortRxUnknownProtos = _HzQtmEnetPortRxUnknownProtos_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 4, 1, 3, 1, 7),
    _HzQtmEnetPortRxUnknownProtos_Type()
)
hzQtmEnetPortRxUnknownProtos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzQtmEnetPortRxUnknownProtos.setStatus("current")
_HzQtmEnetPortTxBytes_Type = Counter64
_HzQtmEnetPortTxBytes_Object = MibTableColumn
hzQtmEnetPortTxBytes = _HzQtmEnetPortTxBytes_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 4, 1, 3, 1, 8),
    _HzQtmEnetPortTxBytes_Type()
)
hzQtmEnetPortTxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzQtmEnetPortTxBytes.setStatus("current")
_HzQtmEnetPortTxUcastPkts_Type = Counter64
_HzQtmEnetPortTxUcastPkts_Object = MibTableColumn
hzQtmEnetPortTxUcastPkts = _HzQtmEnetPortTxUcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 4, 1, 3, 1, 9),
    _HzQtmEnetPortTxUcastPkts_Type()
)
hzQtmEnetPortTxUcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzQtmEnetPortTxUcastPkts.setStatus("current")
_HzQtmEnetPortTxNUcastPkts_Type = Counter64
_HzQtmEnetPortTxNUcastPkts_Object = MibTableColumn
hzQtmEnetPortTxNUcastPkts = _HzQtmEnetPortTxNUcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 4, 1, 3, 1, 10),
    _HzQtmEnetPortTxNUcastPkts_Type()
)
hzQtmEnetPortTxNUcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzQtmEnetPortTxNUcastPkts.setStatus("current")
_HzQtmEnetPortTxDiscards_Type = Counter64
_HzQtmEnetPortTxDiscards_Object = MibTableColumn
hzQtmEnetPortTxDiscards = _HzQtmEnetPortTxDiscards_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 4, 1, 3, 1, 11),
    _HzQtmEnetPortTxDiscards_Type()
)
hzQtmEnetPortTxDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzQtmEnetPortTxDiscards.setStatus("current")
_HzQtmEnetPortTxErrors_Type = Counter64
_HzQtmEnetPortTxErrors_Object = MibTableColumn
hzQtmEnetPortTxErrors = _HzQtmEnetPortTxErrors_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 4, 1, 3, 1, 12),
    _HzQtmEnetPortTxErrors_Type()
)
hzQtmEnetPortTxErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzQtmEnetPortTxErrors.setStatus("current")
_HzQtmAggregatedEnetPort_ObjectIdentity = ObjectIdentity
hzQtmAggregatedEnetPort = _HzQtmAggregatedEnetPort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 4, 2)
)
_HzQtmAggregatedEnetPortConfig_ObjectIdentity = ObjectIdentity
hzQtmAggregatedEnetPortConfig = _HzQtmAggregatedEnetPortConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 4, 2, 1)
)


class _HzQtmEnetPortDroppedEnetFramesThresholdParameters_Type(DisplayString):
    """Custom type hzQtmEnetPortDroppedEnetFramesThresholdParameters based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 24),
    )


_HzQtmEnetPortDroppedEnetFramesThresholdParameters_Type.__name__ = "DisplayString"
_HzQtmEnetPortDroppedEnetFramesThresholdParameters_Object = MibScalar
hzQtmEnetPortDroppedEnetFramesThresholdParameters = _HzQtmEnetPortDroppedEnetFramesThresholdParameters_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 4, 2, 1, 1),
    _HzQtmEnetPortDroppedEnetFramesThresholdParameters_Type()
)
hzQtmEnetPortDroppedEnetFramesThresholdParameters.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzQtmEnetPortDroppedEnetFramesThresholdParameters.setStatus("current")


class _HzQtmEnetPortBWUtilizationThresholdParameters_Type(DisplayString):
    """Custom type hzQtmEnetPortBWUtilizationThresholdParameters based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 24),
    )


_HzQtmEnetPortBWUtilizationThresholdParameters_Type.__name__ = "DisplayString"
_HzQtmEnetPortBWUtilizationThresholdParameters_Object = MibScalar
hzQtmEnetPortBWUtilizationThresholdParameters = _HzQtmEnetPortBWUtilizationThresholdParameters_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 4, 2, 1, 2),
    _HzQtmEnetPortBWUtilizationThresholdParameters_Type()
)
hzQtmEnetPortBWUtilizationThresholdParameters.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzQtmEnetPortBWUtilizationThresholdParameters.setStatus("current")
_HzQtmAggregatedEnetPortStats_ObjectIdentity = ObjectIdentity
hzQtmAggregatedEnetPortStats = _HzQtmAggregatedEnetPortStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 4, 2, 2)
)
_HzQtmAggPortTxFrames_Type = Counter64
_HzQtmAggPortTxFrames_Object = MibScalar
hzQtmAggPortTxFrames = _HzQtmAggPortTxFrames_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 4, 2, 2, 1),
    _HzQtmAggPortTxFrames_Type()
)
hzQtmAggPortTxFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzQtmAggPortTxFrames.setStatus("current")
_HzQtmAggPortTxBytes_Type = Counter64
_HzQtmAggPortTxBytes_Object = MibScalar
hzQtmAggPortTxBytes = _HzQtmAggPortTxBytes_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 4, 2, 2, 2),
    _HzQtmAggPortTxBytes_Type()
)
hzQtmAggPortTxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzQtmAggPortTxBytes.setStatus("current")
_HzQtmAggPortRxFramesOK_Type = Counter64
_HzQtmAggPortRxFramesOK_Object = MibScalar
hzQtmAggPortRxFramesOK = _HzQtmAggPortRxFramesOK_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 4, 2, 2, 3),
    _HzQtmAggPortRxFramesOK_Type()
)
hzQtmAggPortRxFramesOK.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzQtmAggPortRxFramesOK.setStatus("current")
_HzQtmAggPortRxBytesOK_Type = Counter64
_HzQtmAggPortRxBytesOK_Object = MibScalar
hzQtmAggPortRxBytesOK = _HzQtmAggPortRxBytesOK_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 4, 2, 2, 4),
    _HzQtmAggPortRxBytesOK_Type()
)
hzQtmAggPortRxBytesOK.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzQtmAggPortRxBytesOK.setStatus("current")
_HzQtmAggPortRxFramesError_Type = Counter64
_HzQtmAggPortRxFramesError_Object = MibScalar
hzQtmAggPortRxFramesError = _HzQtmAggPortRxFramesError_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 4, 2, 2, 5),
    _HzQtmAggPortRxFramesError_Type()
)
hzQtmAggPortRxFramesError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzQtmAggPortRxFramesError.setStatus("current")
_HzQtmAggPortBWUtilization_Type = Integer32
_HzQtmAggPortBWUtilization_Object = MibScalar
hzQtmAggPortBWUtilization = _HzQtmAggPortBWUtilization_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 4, 2, 2, 6),
    _HzQtmAggPortBWUtilization_Type()
)
hzQtmAggPortBWUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzQtmAggPortBWUtilization.setStatus("current")
_HzQtmAggPortIngressDataRate_Type = Integer32
_HzQtmAggPortIngressDataRate_Object = MibScalar
hzQtmAggPortIngressDataRate = _HzQtmAggPortIngressDataRate_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 4, 2, 2, 7),
    _HzQtmAggPortIngressDataRate_Type()
)
hzQtmAggPortIngressDataRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzQtmAggPortIngressDataRate.setStatus("current")
_HzQtmAggPortEgressDataRate_Type = Integer32
_HzQtmAggPortEgressDataRate_Object = MibScalar
hzQtmAggPortEgressDataRate = _HzQtmAggPortEgressDataRate_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 4, 2, 2, 8),
    _HzQtmAggPortEgressDataRate_Type()
)
hzQtmAggPortEgressDataRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzQtmAggPortEgressDataRate.setStatus("current")
_HzQtmAggPortFramesInQueue1_Type = Counter64
_HzQtmAggPortFramesInQueue1_Object = MibScalar
hzQtmAggPortFramesInQueue1 = _HzQtmAggPortFramesInQueue1_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 4, 2, 2, 9),
    _HzQtmAggPortFramesInQueue1_Type()
)
hzQtmAggPortFramesInQueue1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzQtmAggPortFramesInQueue1.setStatus("current")
_HzQtmAggPortFramesInQueue2_Type = Counter64
_HzQtmAggPortFramesInQueue2_Object = MibScalar
hzQtmAggPortFramesInQueue2 = _HzQtmAggPortFramesInQueue2_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 4, 2, 2, 10),
    _HzQtmAggPortFramesInQueue2_Type()
)
hzQtmAggPortFramesInQueue2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzQtmAggPortFramesInQueue2.setStatus("current")
_HzQtmAggPortFramesInQueue3_Type = Counter64
_HzQtmAggPortFramesInQueue3_Object = MibScalar
hzQtmAggPortFramesInQueue3 = _HzQtmAggPortFramesInQueue3_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 4, 2, 2, 11),
    _HzQtmAggPortFramesInQueue3_Type()
)
hzQtmAggPortFramesInQueue3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzQtmAggPortFramesInQueue3.setStatus("current")
_HzQtmAggPortFramesInQueue4_Type = Counter64
_HzQtmAggPortFramesInQueue4_Object = MibScalar
hzQtmAggPortFramesInQueue4 = _HzQtmAggPortFramesInQueue4_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 4, 2, 2, 12),
    _HzQtmAggPortFramesInQueue4_Type()
)
hzQtmAggPortFramesInQueue4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzQtmAggPortFramesInQueue4.setStatus("current")
_HzQtmAggPortFramesInQueue1Discarded_Type = Counter64
_HzQtmAggPortFramesInQueue1Discarded_Object = MibScalar
hzQtmAggPortFramesInQueue1Discarded = _HzQtmAggPortFramesInQueue1Discarded_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 4, 2, 2, 13),
    _HzQtmAggPortFramesInQueue1Discarded_Type()
)
hzQtmAggPortFramesInQueue1Discarded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzQtmAggPortFramesInQueue1Discarded.setStatus("current")
_HzQtmAggPortFramesInQueue2Discarded_Type = Counter64
_HzQtmAggPortFramesInQueue2Discarded_Object = MibScalar
hzQtmAggPortFramesInQueue2Discarded = _HzQtmAggPortFramesInQueue2Discarded_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 4, 2, 2, 14),
    _HzQtmAggPortFramesInQueue2Discarded_Type()
)
hzQtmAggPortFramesInQueue2Discarded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzQtmAggPortFramesInQueue2Discarded.setStatus("current")
_HzQtmAggPortFramesInQueue3Discarded_Type = Counter64
_HzQtmAggPortFramesInQueue3Discarded_Object = MibScalar
hzQtmAggPortFramesInQueue3Discarded = _HzQtmAggPortFramesInQueue3Discarded_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 4, 2, 2, 15),
    _HzQtmAggPortFramesInQueue3Discarded_Type()
)
hzQtmAggPortFramesInQueue3Discarded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzQtmAggPortFramesInQueue3Discarded.setStatus("current")
_HzQtmAggPortFramesInQueue4Discarded_Type = Counter64
_HzQtmAggPortFramesInQueue4Discarded_Object = MibScalar
hzQtmAggPortFramesInQueue4Discarded = _HzQtmAggPortFramesInQueue4Discarded_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 4, 2, 2, 16),
    _HzQtmAggPortFramesInQueue4Discarded_Type()
)
hzQtmAggPortFramesInQueue4Discarded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzQtmAggPortFramesInQueue4Discarded.setStatus("current")
_HzQtmAggPortFramesInQueueC_Type = Counter64
_HzQtmAggPortFramesInQueueC_Object = MibScalar
hzQtmAggPortFramesInQueueC = _HzQtmAggPortFramesInQueueC_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 4, 2, 2, 17),
    _HzQtmAggPortFramesInQueueC_Type()
)
hzQtmAggPortFramesInQueueC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzQtmAggPortFramesInQueueC.setStatus("current")
_HzQtmAggPortFramesInQueueCDiscarded_Type = Counter64
_HzQtmAggPortFramesInQueueCDiscarded_Object = MibScalar
hzQtmAggPortFramesInQueueCDiscarded = _HzQtmAggPortFramesInQueueCDiscarded_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 4, 2, 2, 18),
    _HzQtmAggPortFramesInQueueCDiscarded_Type()
)
hzQtmAggPortFramesInQueueCDiscarded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzQtmAggPortFramesInQueueCDiscarded.setStatus("current")
_HzQtmWirelessInterface_ObjectIdentity = ObjectIdentity
hzQtmWirelessInterface = _HzQtmWirelessInterface_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 5)
)
_HzQtmWirelessInterfaceNames_ObjectIdentity = ObjectIdentity
hzQtmWirelessInterfaceNames = _HzQtmWirelessInterfaceNames_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 5, 1)
)
_HzQtmWirelessInterfaceNameTable_Object = MibTable
hzQtmWirelessInterfaceNameTable = _HzQtmWirelessInterfaceNameTable_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 5, 1, 1)
)
if mibBuilder.loadTexts:
    hzQtmWirelessInterfaceNameTable.setStatus("current")
_HzQtmWirelessInterfaceNameEntry_Object = MibTableRow
hzQtmWirelessInterfaceNameEntry = _HzQtmWirelessInterfaceNameEntry_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 5, 1, 1, 1)
)
hzQtmWirelessInterfaceNameEntry.setIndexNames(
    (0, "DRAGONWAVE-HORIZON-QUANTUM-MIB", "hzQtmWirelessInterfaceNameIndex"),
)
if mibBuilder.loadTexts:
    hzQtmWirelessInterfaceNameEntry.setStatus("current")


class _HzQtmWirelessInterfaceNameIndex_Type(Integer32):
    """Custom type hzQtmWirelessInterfaceNameIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("wireless-port-1", 1),
          ("wireless-port-2", 2))
    )


_HzQtmWirelessInterfaceNameIndex_Type.__name__ = "Integer32"
_HzQtmWirelessInterfaceNameIndex_Object = MibTableColumn
hzQtmWirelessInterfaceNameIndex = _HzQtmWirelessInterfaceNameIndex_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 5, 1, 1, 1, 1),
    _HzQtmWirelessInterfaceNameIndex_Type()
)
hzQtmWirelessInterfaceNameIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzQtmWirelessInterfaceNameIndex.setStatus("current")
_HzQtmWirelessInterfaceName_Type = DisplayString
_HzQtmWirelessInterfaceName_Object = MibTableColumn
hzQtmWirelessInterfaceName = _HzQtmWirelessInterfaceName_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 5, 1, 1, 1, 2),
    _HzQtmWirelessInterfaceName_Type()
)
hzQtmWirelessInterfaceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzQtmWirelessInterfaceName.setStatus("current")
_HzQtmWirelessInterfaceModems_ObjectIdentity = ObjectIdentity
hzQtmWirelessInterfaceModems = _HzQtmWirelessInterfaceModems_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 5, 2)
)
_HzQtmModemTable_Object = MibTable
hzQtmModemTable = _HzQtmModemTable_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 5, 2, 1)
)
if mibBuilder.loadTexts:
    hzQtmModemTable.setStatus("current")
_HzQtmModemEntry_Object = MibTableRow
hzQtmModemEntry = _HzQtmModemEntry_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 5, 2, 1, 1)
)
hzQtmModemEntry.setIndexNames(
    (0, "DRAGONWAVE-HORIZON-QUANTUM-MIB", "hzQtmModemIndex"),
)
if mibBuilder.loadTexts:
    hzQtmModemEntry.setStatus("current")


class _HzQtmModemIndex_Type(Integer32):
    """Custom type hzQtmModemIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("wireless-port-1", 1),
          ("wireless-port-2", 2))
    )


_HzQtmModemIndex_Type.__name__ = "Integer32"
_HzQtmModemIndex_Object = MibTableColumn
hzQtmModemIndex = _HzQtmModemIndex_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 5, 2, 1, 1, 1),
    _HzQtmModemIndex_Type()
)
hzQtmModemIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzQtmModemIndex.setStatus("current")


class _HzQtmModemOperStatus_Type(Integer32):
    """Custom type hzQtmModemOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("up", 1),
          ("down", 2),
          ("testing", 3))
    )


_HzQtmModemOperStatus_Type.__name__ = "Integer32"
_HzQtmModemOperStatus_Object = MibTableColumn
hzQtmModemOperStatus = _HzQtmModemOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 5, 2, 1, 1, 2),
    _HzQtmModemOperStatus_Type()
)
hzQtmModemOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzQtmModemOperStatus.setStatus("current")
_HzQtmModemChannelizedRSL_Type = Integer32
_HzQtmModemChannelizedRSL_Object = MibTableColumn
hzQtmModemChannelizedRSL = _HzQtmModemChannelizedRSL_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 5, 2, 1, 1, 3),
    _HzQtmModemChannelizedRSL_Type()
)
hzQtmModemChannelizedRSL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzQtmModemChannelizedRSL.setStatus("current")
_HzQtmModemChannelizedRSLUnsignedInt_Type = Integer32
_HzQtmModemChannelizedRSLUnsignedInt_Object = MibTableColumn
hzQtmModemChannelizedRSLUnsignedInt = _HzQtmModemChannelizedRSLUnsignedInt_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 5, 2, 1, 1, 4),
    _HzQtmModemChannelizedRSLUnsignedInt_Type()
)
hzQtmModemChannelizedRSLUnsignedInt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzQtmModemChannelizedRSLUnsignedInt.setStatus("current")


class _HzQtmModemModulationType_Type(Integer32):
    """Custom type hzQtmModemModulationType based on Integer32"""
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
        *(("qpsk", 1),
          ("qam", 2),
          ("qam16", 3),
          ("qam32", 4),
          ("qam64", 5),
          ("qam128", 6),
          ("qam256", 7),
          ("x8psk", 8))
    )


_HzQtmModemModulationType_Type.__name__ = "Integer32"
_HzQtmModemModulationType_Object = MibTableColumn
hzQtmModemModulationType = _HzQtmModemModulationType_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 5, 2, 1, 1, 5),
    _HzQtmModemModulationType_Type()
)
hzQtmModemModulationType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzQtmModemModulationType.setStatus("current")
_HzQtmModemRxSpeed_Type = Integer32
_HzQtmModemRxSpeed_Object = MibTableColumn
hzQtmModemRxSpeed = _HzQtmModemRxSpeed_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 5, 2, 1, 1, 6),
    _HzQtmModemRxSpeed_Type()
)
hzQtmModemRxSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzQtmModemRxSpeed.setStatus("current")
_HzQtmModemTxSpeed_Type = Integer32
_HzQtmModemTxSpeed_Object = MibTableColumn
hzQtmModemTxSpeed = _HzQtmModemTxSpeed_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 5, 2, 1, 1, 7),
    _HzQtmModemTxSpeed_Type()
)
hzQtmModemTxSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzQtmModemTxSpeed.setStatus("current")
_HzQtmModemSNR_Type = Integer32
_HzQtmModemSNR_Object = MibTableColumn
hzQtmModemSNR = _HzQtmModemSNR_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 5, 2, 1, 1, 8),
    _HzQtmModemSNR_Type()
)
hzQtmModemSNR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzQtmModemSNR.setStatus("current")
_HzQtmModemEbToNoiseRatio_Type = Integer32
_HzQtmModemEbToNoiseRatio_Object = MibTableColumn
hzQtmModemEbToNoiseRatio = _HzQtmModemEbToNoiseRatio_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 5, 2, 1, 1, 9),
    _HzQtmModemEbToNoiseRatio_Type()
)
hzQtmModemEbToNoiseRatio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzQtmModemEbToNoiseRatio.setStatus("current")
_HzQtmModemEqualizerStress_Type = Integer32
_HzQtmModemEqualizerStress_Object = MibTableColumn
hzQtmModemEqualizerStress = _HzQtmModemEqualizerStress_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 5, 2, 1, 1, 10),
    _HzQtmModemEqualizerStress_Type()
)
hzQtmModemEqualizerStress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzQtmModemEqualizerStress.setStatus("current")


class _HzQtmModemSNRThresholdParameters_Type(DisplayString):
    """Custom type hzQtmModemSNRThresholdParameters based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 24),
    )


_HzQtmModemSNRThresholdParameters_Type.__name__ = "DisplayString"
_HzQtmModemSNRThresholdParameters_Object = MibTableColumn
hzQtmModemSNRThresholdParameters = _HzQtmModemSNRThresholdParameters_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 5, 2, 1, 1, 11),
    _HzQtmModemSNRThresholdParameters_Type()
)
hzQtmModemSNRThresholdParameters.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzQtmModemSNRThresholdParameters.setStatus("current")


class _HzQtmModemChannelizedRslBelowThresholdParameters_Type(DisplayString):
    """Custom type hzQtmModemChannelizedRslBelowThresholdParameters based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 24),
    )


_HzQtmModemChannelizedRslBelowThresholdParameters_Type.__name__ = "DisplayString"
_HzQtmModemChannelizedRslBelowThresholdParameters_Object = MibTableColumn
hzQtmModemChannelizedRslBelowThresholdParameters = _HzQtmModemChannelizedRslBelowThresholdParameters_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 5, 2, 1, 1, 12),
    _HzQtmModemChannelizedRslBelowThresholdParameters_Type()
)
hzQtmModemChannelizedRslBelowThresholdParameters.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzQtmModemChannelizedRslBelowThresholdParameters.setStatus("current")
_HzQtmModemXpicEqualizerStress_Type = Integer32
_HzQtmModemXpicEqualizerStress_Object = MibTableColumn
hzQtmModemXpicEqualizerStress = _HzQtmModemXpicEqualizerStress_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 5, 2, 1, 1, 13),
    _HzQtmModemXpicEqualizerStress_Type()
)
hzQtmModemXpicEqualizerStress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzQtmModemXpicEqualizerStress.setStatus("current")
_HzQtmModemXPI_Type = Integer32
_HzQtmModemXPI_Object = MibTableColumn
hzQtmModemXPI = _HzQtmModemXPI_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 5, 2, 1, 1, 14),
    _HzQtmModemXPI_Type()
)
hzQtmModemXPI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzQtmModemXPI.setStatus("current")
_HzQtmModemStatsTable_Object = MibTable
hzQtmModemStatsTable = _HzQtmModemStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 5, 2, 2)
)
if mibBuilder.loadTexts:
    hzQtmModemStatsTable.setStatus("current")
_HzQtmModemStatsEntry_Object = MibTableRow
hzQtmModemStatsEntry = _HzQtmModemStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 5, 2, 2, 1)
)
hzQtmModemStatsEntry.setIndexNames(
    (0, "DRAGONWAVE-HORIZON-QUANTUM-MIB", "hzQtmModemStatsIndex"),
)
if mibBuilder.loadTexts:
    hzQtmModemStatsEntry.setStatus("current")


class _HzQtmModemStatsIndex_Type(Integer32):
    """Custom type hzQtmModemStatsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("wireless-port-1", 1),
          ("wireless-port-2", 2),
          ("secondary-wireless-ports", 3))
    )


_HzQtmModemStatsIndex_Type.__name__ = "Integer32"
_HzQtmModemStatsIndex_Object = MibTableColumn
hzQtmModemStatsIndex = _HzQtmModemStatsIndex_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 5, 2, 2, 1, 1),
    _HzQtmModemStatsIndex_Type()
)
hzQtmModemStatsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzQtmModemStatsIndex.setStatus("current")
_HzQtmModemTxBlocks_Type = Counter64
_HzQtmModemTxBlocks_Object = MibTableColumn
hzQtmModemTxBlocks = _HzQtmModemTxBlocks_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 5, 2, 2, 1, 2),
    _HzQtmModemTxBlocks_Type()
)
hzQtmModemTxBlocks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzQtmModemTxBlocks.setStatus("current")
_HzQtmModemRxBlocksOKs_Type = Counter64
_HzQtmModemRxBlocksOKs_Object = MibTableColumn
hzQtmModemRxBlocksOKs = _HzQtmModemRxBlocksOKs_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 5, 2, 2, 1, 3),
    _HzQtmModemRxBlocksOKs_Type()
)
hzQtmModemRxBlocksOKs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzQtmModemRxBlocksOKs.setStatus("current")
_HzQtmModemRxBlocksErrors_Type = Counter64
_HzQtmModemRxBlocksErrors_Object = MibTableColumn
hzQtmModemRxBlocksErrors = _HzQtmModemRxBlocksErrors_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 5, 2, 2, 1, 4),
    _HzQtmModemRxBlocksErrors_Type()
)
hzQtmModemRxBlocksErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzQtmModemRxBlocksErrors.setStatus("current")
_HzQtmWirelessEnetPortStatsTable_Object = MibTable
hzQtmWirelessEnetPortStatsTable = _HzQtmWirelessEnetPortStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 5, 2, 3)
)
if mibBuilder.loadTexts:
    hzQtmWirelessEnetPortStatsTable.setStatus("current")
_HzQtmWirelessEnetPortStatsEntry_Object = MibTableRow
hzQtmWirelessEnetPortStatsEntry = _HzQtmWirelessEnetPortStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 5, 2, 3, 1)
)
hzQtmWirelessEnetPortStatsEntry.setIndexNames(
    (0, "DRAGONWAVE-HORIZON-QUANTUM-MIB", "hzQtmWirelessEnetPortIndex"),
)
if mibBuilder.loadTexts:
    hzQtmWirelessEnetPortStatsEntry.setStatus("current")


class _HzQtmWirelessEnetPortIndex_Type(Integer32):
    """Custom type hzQtmWirelessEnetPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("wireless-enetport-1", 1),
          ("wireless-enetport-2", 2))
    )


_HzQtmWirelessEnetPortIndex_Type.__name__ = "Integer32"
_HzQtmWirelessEnetPortIndex_Object = MibTableColumn
hzQtmWirelessEnetPortIndex = _HzQtmWirelessEnetPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 5, 2, 3, 1, 1),
    _HzQtmWirelessEnetPortIndex_Type()
)
hzQtmWirelessEnetPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzQtmWirelessEnetPortIndex.setStatus("current")
_HzQtmWirelessEnetPortTxFrames_Type = Counter64
_HzQtmWirelessEnetPortTxFrames_Object = MibTableColumn
hzQtmWirelessEnetPortTxFrames = _HzQtmWirelessEnetPortTxFrames_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 5, 2, 3, 1, 2),
    _HzQtmWirelessEnetPortTxFrames_Type()
)
hzQtmWirelessEnetPortTxFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzQtmWirelessEnetPortTxFrames.setStatus("current")
_HzQtmWirelessEnetPortRxFramesOK_Type = Counter64
_HzQtmWirelessEnetPortRxFramesOK_Object = MibTableColumn
hzQtmWirelessEnetPortRxFramesOK = _HzQtmWirelessEnetPortRxFramesOK_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 5, 2, 3, 1, 3),
    _HzQtmWirelessEnetPortRxFramesOK_Type()
)
hzQtmWirelessEnetPortRxFramesOK.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzQtmWirelessEnetPortRxFramesOK.setStatus("current")
_HzQtmWirelessEnetPortRxFramesErrors_Type = Counter64
_HzQtmWirelessEnetPortRxFramesErrors_Object = MibTableColumn
hzQtmWirelessEnetPortRxFramesErrors = _HzQtmWirelessEnetPortRxFramesErrors_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 5, 2, 3, 1, 4),
    _HzQtmWirelessEnetPortRxFramesErrors_Type()
)
hzQtmWirelessEnetPortRxFramesErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzQtmWirelessEnetPortRxFramesErrors.setStatus("current")
_HzQtmWirelessEnetPortRxFramesQueueDiscards_Type = Counter64
_HzQtmWirelessEnetPortRxFramesQueueDiscards_Object = MibTableColumn
hzQtmWirelessEnetPortRxFramesQueueDiscards = _HzQtmWirelessEnetPortRxFramesQueueDiscards_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 5, 2, 3, 1, 5),
    _HzQtmWirelessEnetPortRxFramesQueueDiscards_Type()
)
hzQtmWirelessEnetPortRxFramesQueueDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzQtmWirelessEnetPortRxFramesQueueDiscards.setStatus("current")
_HzQtmWirelessInterfaceIF_ObjectIdentity = ObjectIdentity
hzQtmWirelessInterfaceIF = _HzQtmWirelessInterfaceIF_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 5, 3)
)
_HzQtmIntermediateFrequencyTable_Object = MibTable
hzQtmIntermediateFrequencyTable = _HzQtmIntermediateFrequencyTable_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 5, 3, 1)
)
if mibBuilder.loadTexts:
    hzQtmIntermediateFrequencyTable.setStatus("current")
_HzQtmIntermediateFrequencyEntry_Object = MibTableRow
hzQtmIntermediateFrequencyEntry = _HzQtmIntermediateFrequencyEntry_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 5, 3, 1, 1)
)
hzQtmIntermediateFrequencyEntry.setIndexNames(
    (0, "DRAGONWAVE-HORIZON-QUANTUM-MIB", "hzQtmIFPathIndex"),
)
if mibBuilder.loadTexts:
    hzQtmIntermediateFrequencyEntry.setStatus("current")


class _HzQtmIFPathIndex_Type(Integer32):
    """Custom type hzQtmIFPathIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("wireless-port-1", 1),
          ("wireless-port-2", 2))
    )


_HzQtmIFPathIndex_Type.__name__ = "Integer32"
_HzQtmIFPathIndex_Object = MibTableColumn
hzQtmIFPathIndex = _HzQtmIFPathIndex_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 5, 3, 1, 1, 1),
    _HzQtmIFPathIndex_Type()
)
hzQtmIFPathIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzQtmIFPathIndex.setStatus("current")


class _HzQtmIFPathTxLockStatus_Type(Integer32):
    """Custom type hzQtmIFPathTxLockStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("unlocked", 1),
          ("locked", 2))
    )


_HzQtmIFPathTxLockStatus_Type.__name__ = "Integer32"
_HzQtmIFPathTxLockStatus_Object = MibTableColumn
hzQtmIFPathTxLockStatus = _HzQtmIFPathTxLockStatus_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 5, 3, 1, 1, 2),
    _HzQtmIFPathTxLockStatus_Type()
)
hzQtmIFPathTxLockStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzQtmIFPathTxLockStatus.setStatus("current")


class _HzQtmIFPathRxLockStatus_Type(Integer32):
    """Custom type hzQtmIFPathRxLockStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("unlocked", 1),
          ("locked", 2))
    )


_HzQtmIFPathRxLockStatus_Type.__name__ = "Integer32"
_HzQtmIFPathRxLockStatus_Object = MibTableColumn
hzQtmIFPathRxLockStatus = _HzQtmIFPathRxLockStatus_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 5, 3, 1, 1, 3),
    _HzQtmIFPathRxLockStatus_Type()
)
hzQtmIFPathRxLockStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzQtmIFPathRxLockStatus.setStatus("current")


class _HzQtmIFPathLoopbackLockStatus_Type(Integer32):
    """Custom type hzQtmIFPathLoopbackLockStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("unlocked", 1),
          ("locked", 2))
    )


_HzQtmIFPathLoopbackLockStatus_Type.__name__ = "Integer32"
_HzQtmIFPathLoopbackLockStatus_Object = MibTableColumn
hzQtmIFPathLoopbackLockStatus = _HzQtmIFPathLoopbackLockStatus_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 5, 3, 1, 1, 4),
    _HzQtmIFPathLoopbackLockStatus_Type()
)
hzQtmIFPathLoopbackLockStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzQtmIFPathLoopbackLockStatus.setStatus("current")
_HzQtmWirelessInterfaceRadios_ObjectIdentity = ObjectIdentity
hzQtmWirelessInterfaceRadios = _HzQtmWirelessInterfaceRadios_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 5, 4)
)
_HzQtmRadioTable_Object = MibTable
hzQtmRadioTable = _HzQtmRadioTable_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 5, 4, 1)
)
if mibBuilder.loadTexts:
    hzQtmRadioTable.setStatus("current")
_HzQtmRadioEntry_Object = MibTableRow
hzQtmRadioEntry = _HzQtmRadioEntry_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 5, 4, 1, 1)
)
hzQtmRadioEntry.setIndexNames(
    (0, "DRAGONWAVE-HORIZON-QUANTUM-MIB", "hzQtmRadioIndex"),
)
if mibBuilder.loadTexts:
    hzQtmRadioEntry.setStatus("current")


class _HzQtmRadioIndex_Type(Integer32):
    """Custom type hzQtmRadioIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("wireless-port-1", 1),
          ("wireless-port-2", 2))
    )


_HzQtmRadioIndex_Type.__name__ = "Integer32"
_HzQtmRadioIndex_Object = MibTableColumn
hzQtmRadioIndex = _HzQtmRadioIndex_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 5, 4, 1, 1, 1),
    _HzQtmRadioIndex_Type()
)
hzQtmRadioIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzQtmRadioIndex.setStatus("current")
_HzQtmRadioDescription_Type = DisplayString
_HzQtmRadioDescription_Object = MibTableColumn
hzQtmRadioDescription = _HzQtmRadioDescription_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 5, 4, 1, 1, 2),
    _HzQtmRadioDescription_Type()
)
hzQtmRadioDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzQtmRadioDescription.setStatus("current")


class _HzQtmRadioOperStatus_Type(Integer32):
    """Custom type hzQtmRadioOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("up", 1),
          ("down", 2),
          ("testing", 3))
    )


_HzQtmRadioOperStatus_Type.__name__ = "Integer32"
_HzQtmRadioOperStatus_Object = MibTableColumn
hzQtmRadioOperStatus = _HzQtmRadioOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 5, 4, 1, 1, 3),
    _HzQtmRadioOperStatus_Type()
)
hzQtmRadioOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzQtmRadioOperStatus.setStatus("current")
_HzQtmRadioLastChanged_Type = TimeTicks
_HzQtmRadioLastChanged_Object = MibTableColumn
hzQtmRadioLastChanged = _HzQtmRadioLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 5, 4, 1, 1, 4),
    _HzQtmRadioLastChanged_Type()
)
hzQtmRadioLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzQtmRadioLastChanged.setStatus("current")
_HzQtmRadioReceiveSignalLevel_Type = Integer32
_HzQtmRadioReceiveSignalLevel_Object = MibTableColumn
hzQtmRadioReceiveSignalLevel = _HzQtmRadioReceiveSignalLevel_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 5, 4, 1, 1, 5),
    _HzQtmRadioReceiveSignalLevel_Type()
)
hzQtmRadioReceiveSignalLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzQtmRadioReceiveSignalLevel.setStatus("current")
_HzQtmRadioReceiveSignalLevelUnsigned_Type = Integer32
_HzQtmRadioReceiveSignalLevelUnsigned_Object = MibTableColumn
hzQtmRadioReceiveSignalLevelUnsigned = _HzQtmRadioReceiveSignalLevelUnsigned_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 5, 4, 1, 1, 6),
    _HzQtmRadioReceiveSignalLevelUnsigned_Type()
)
hzQtmRadioReceiveSignalLevelUnsigned.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzQtmRadioReceiveSignalLevelUnsigned.setStatus("current")
_HzQtmRadioTxGain_Type = Integer32
_HzQtmRadioTxGain_Object = MibTableColumn
hzQtmRadioTxGain = _HzQtmRadioTxGain_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 5, 4, 1, 1, 7),
    _HzQtmRadioTxGain_Type()
)
hzQtmRadioTxGain.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzQtmRadioTxGain.setStatus("current")
_HzQtmRadioRxGain_Type = Integer32
_HzQtmRadioRxGain_Object = MibTableColumn
hzQtmRadioRxGain = _HzQtmRadioRxGain_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 5, 4, 1, 1, 8),
    _HzQtmRadioRxGain_Type()
)
hzQtmRadioRxGain.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzQtmRadioRxGain.setStatus("current")
_HzQtmRadioReset_Type = Integer32
_HzQtmRadioReset_Object = MibTableColumn
hzQtmRadioReset = _HzQtmRadioReset_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 5, 4, 1, 1, 9),
    _HzQtmRadioReset_Type()
)
hzQtmRadioReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzQtmRadioReset.setStatus("current")


class _HzQtmRadioTransmitPowerdBm_Type(Integer32):
    """Custom type hzQtmRadioTransmitPowerdBm based on Integer32"""
    defaultValue = 0


_HzQtmRadioTransmitPowerdBm_Type.__name__ = "Integer32"
_HzQtmRadioTransmitPowerdBm_Object = MibTableColumn
hzQtmRadioTransmitPowerdBm = _HzQtmRadioTransmitPowerdBm_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 5, 4, 1, 1, 10),
    _HzQtmRadioTransmitPowerdBm_Type()
)
hzQtmRadioTransmitPowerdBm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzQtmRadioTransmitPowerdBm.setStatus("current")


class _HzQtmRadioPowerOption_Type(Integer32):
    """Custom type hzQtmRadioPowerOption based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("normal", 1),
          ("highPower", 2))
    )


_HzQtmRadioPowerOption_Type.__name__ = "Integer32"
_HzQtmRadioPowerOption_Object = MibTableColumn
hzQtmRadioPowerOption = _HzQtmRadioPowerOption_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 5, 4, 1, 1, 11),
    _HzQtmRadioPowerOption_Type()
)
hzQtmRadioPowerOption.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzQtmRadioPowerOption.setStatus("current")


class _HzQtmRadioTxState_Type(Integer32):
    """Custom type hzQtmRadioTxState based on Integer32"""
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


_HzQtmRadioTxState_Type.__name__ = "Integer32"
_HzQtmRadioTxState_Object = MibTableColumn
hzQtmRadioTxState = _HzQtmRadioTxState_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 5, 4, 1, 1, 12),
    _HzQtmRadioTxState_Type()
)
hzQtmRadioTxState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzQtmRadioTxState.setStatus("current")


class _HzQtmRadioActualTxState_Type(Integer32):
    """Custom type hzQtmRadioActualTxState based on Integer32"""
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


_HzQtmRadioActualTxState_Type.__name__ = "Integer32"
_HzQtmRadioActualTxState_Object = MibTableColumn
hzQtmRadioActualTxState = _HzQtmRadioActualTxState_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 5, 4, 1, 1, 13),
    _HzQtmRadioActualTxState_Type()
)
hzQtmRadioActualTxState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzQtmRadioActualTxState.setStatus("current")
_HzQtmRadioTemperature_Type = Integer32
_HzQtmRadioTemperature_Object = MibTableColumn
hzQtmRadioTemperature = _HzQtmRadioTemperature_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 5, 4, 1, 1, 14),
    _HzQtmRadioTemperature_Type()
)
hzQtmRadioTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzQtmRadioTemperature.setStatus("current")
_HzQtmRadioRxCableLoss_Type = DisplayString
_HzQtmRadioRxCableLoss_Object = MibTableColumn
hzQtmRadioRxCableLoss = _HzQtmRadioRxCableLoss_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 5, 4, 1, 1, 15),
    _HzQtmRadioRxCableLoss_Type()
)
hzQtmRadioRxCableLoss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzQtmRadioRxCableLoss.setStatus("current")
_HzQtmRadioTxCableLoss_Type = DisplayString
_HzQtmRadioTxCableLoss_Object = MibTableColumn
hzQtmRadioTxCableLoss = _HzQtmRadioTxCableLoss_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 5, 4, 1, 1, 16),
    _HzQtmRadioTxCableLoss_Type()
)
hzQtmRadioTxCableLoss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzQtmRadioTxCableLoss.setStatus("current")
_HzQtmRadioTxCableLossChange_Type = DisplayString
_HzQtmRadioTxCableLossChange_Object = MibTableColumn
hzQtmRadioTxCableLossChange = _HzQtmRadioTxCableLossChange_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 5, 4, 1, 1, 17),
    _HzQtmRadioTxCableLossChange_Type()
)
hzQtmRadioTxCableLossChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzQtmRadioTxCableLossChange.setStatus("current")
_HzQtmRadioMaxTransmitPowerdBm_Type = Integer32
_HzQtmRadioMaxTransmitPowerdBm_Object = MibTableColumn
hzQtmRadioMaxTransmitPowerdBm = _HzQtmRadioMaxTransmitPowerdBm_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 5, 4, 1, 1, 18),
    _HzQtmRadioMaxTransmitPowerdBm_Type()
)
hzQtmRadioMaxTransmitPowerdBm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzQtmRadioMaxTransmitPowerdBm.setStatus("current")
_HzQtmRadioActualTransmitPowerdBm_Type = Integer32
_HzQtmRadioActualTransmitPowerdBm_Object = MibTableColumn
hzQtmRadioActualTransmitPowerdBm = _HzQtmRadioActualTransmitPowerdBm_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 5, 4, 1, 1, 19),
    _HzQtmRadioActualTransmitPowerdBm_Type()
)
hzQtmRadioActualTransmitPowerdBm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzQtmRadioActualTransmitPowerdBm.setStatus("current")
_HzQtmWirelessInterfaceRadioFrequencies_ObjectIdentity = ObjectIdentity
hzQtmWirelessInterfaceRadioFrequencies = _HzQtmWirelessInterfaceRadioFrequencies_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 5, 5)
)
_HzQtmWirelessInterfaceRadio1Frequencies_ObjectIdentity = ObjectIdentity
hzQtmWirelessInterfaceRadio1Frequencies = _HzQtmWirelessInterfaceRadio1Frequencies_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 5, 5, 1)
)


class _HzQtmRadio1FreqGroupSelected_Type(Integer32):
    """Custom type hzQtmRadio1FreqGroupSelected based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("txLow", 1),
          ("txHigh", 2),
          ("none", 3))
    )


_HzQtmRadio1FreqGroupSelected_Type.__name__ = "Integer32"
_HzQtmRadio1FreqGroupSelected_Object = MibScalar
hzQtmRadio1FreqGroupSelected = _HzQtmRadio1FreqGroupSelected_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 5, 5, 1, 1),
    _HzQtmRadio1FreqGroupSelected_Type()
)
hzQtmRadio1FreqGroupSelected.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzQtmRadio1FreqGroupSelected.setStatus("current")
_HzQtmRadio1BandTable_Object = MibTable
hzQtmRadio1BandTable = _HzQtmRadio1BandTable_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 5, 5, 1, 2)
)
if mibBuilder.loadTexts:
    hzQtmRadio1BandTable.setStatus("current")
_HzQtmRadio1BandEntry_Object = MibTableRow
hzQtmRadio1BandEntry = _HzQtmRadio1BandEntry_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 5, 5, 1, 2, 1)
)
hzQtmRadio1BandEntry.setIndexNames(
    (0, "DRAGONWAVE-HORIZON-QUANTUM-MIB", "hzQtmRadio1BandIndex"),
)
if mibBuilder.loadTexts:
    hzQtmRadio1BandEntry.setStatus("current")
_HzQtmRadio1BandIndex_Type = Integer32
_HzQtmRadio1BandIndex_Object = MibTableColumn
hzQtmRadio1BandIndex = _HzQtmRadio1BandIndex_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 5, 5, 1, 2, 1, 1),
    _HzQtmRadio1BandIndex_Type()
)
hzQtmRadio1BandIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzQtmRadio1BandIndex.setStatus("current")
_HzQtmRadio1BandId_Type = Integer32
_HzQtmRadio1BandId_Object = MibTableColumn
hzQtmRadio1BandId = _HzQtmRadio1BandId_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 5, 5, 1, 2, 1, 2),
    _HzQtmRadio1BandId_Type()
)
hzQtmRadio1BandId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzQtmRadio1BandId.setStatus("current")
_HzQtmRadio1BandName_Type = DisplayString
_HzQtmRadio1BandName_Object = MibTableColumn
hzQtmRadio1BandName = _HzQtmRadio1BandName_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 5, 5, 1, 2, 1, 3),
    _HzQtmRadio1BandName_Type()
)
hzQtmRadio1BandName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzQtmRadio1BandName.setStatus("current")


class _HzQtmRadio1BandProgrammed_Type(Integer32):
    """Custom type hzQtmRadio1BandProgrammed based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("notActive", 2))
    )


_HzQtmRadio1BandProgrammed_Type.__name__ = "Integer32"
_HzQtmRadio1BandProgrammed_Object = MibTableColumn
hzQtmRadio1BandProgrammed = _HzQtmRadio1BandProgrammed_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 5, 5, 1, 2, 1, 4),
    _HzQtmRadio1BandProgrammed_Type()
)
hzQtmRadio1BandProgrammed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzQtmRadio1BandProgrammed.setStatus("current")
_HzQtmRadio1TxHighFreqTable_Object = MibTable
hzQtmRadio1TxHighFreqTable = _HzQtmRadio1TxHighFreqTable_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 5, 5, 1, 3)
)
if mibBuilder.loadTexts:
    hzQtmRadio1TxHighFreqTable.setStatus("current")
_HzQtmRadio1TxHighFreqEntry_Object = MibTableRow
hzQtmRadio1TxHighFreqEntry = _HzQtmRadio1TxHighFreqEntry_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 5, 5, 1, 3, 1)
)
hzQtmRadio1TxHighFreqEntry.setIndexNames(
    (0, "DRAGONWAVE-HORIZON-QUANTUM-MIB", "hzQtmRadio1TxHighFreqIndex"),
)
if mibBuilder.loadTexts:
    hzQtmRadio1TxHighFreqEntry.setStatus("current")
_HzQtmRadio1TxHighFreqIndex_Type = Integer32
_HzQtmRadio1TxHighFreqIndex_Object = MibTableColumn
hzQtmRadio1TxHighFreqIndex = _HzQtmRadio1TxHighFreqIndex_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 5, 5, 1, 3, 1, 1),
    _HzQtmRadio1TxHighFreqIndex_Type()
)
hzQtmRadio1TxHighFreqIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzQtmRadio1TxHighFreqIndex.setStatus("current")
_HzQtmRadio1TxHighFreqChannelIndex_Type = DisplayString
_HzQtmRadio1TxHighFreqChannelIndex_Object = MibTableColumn
hzQtmRadio1TxHighFreqChannelIndex = _HzQtmRadio1TxHighFreqChannelIndex_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 5, 5, 1, 3, 1, 2),
    _HzQtmRadio1TxHighFreqChannelIndex_Type()
)
hzQtmRadio1TxHighFreqChannelIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzQtmRadio1TxHighFreqChannelIndex.setStatus("current")
_HzQtmRadio1TxHighFreqTransmitRfFrequency_Type = Integer32
_HzQtmRadio1TxHighFreqTransmitRfFrequency_Object = MibTableColumn
hzQtmRadio1TxHighFreqTransmitRfFrequency = _HzQtmRadio1TxHighFreqTransmitRfFrequency_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 5, 5, 1, 3, 1, 3),
    _HzQtmRadio1TxHighFreqTransmitRfFrequency_Type()
)
hzQtmRadio1TxHighFreqTransmitRfFrequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzQtmRadio1TxHighFreqTransmitRfFrequency.setStatus("current")
_HzQtmRadio1TxHighFreqReceiveRfFrequency_Type = Integer32
_HzQtmRadio1TxHighFreqReceiveRfFrequency_Object = MibTableColumn
hzQtmRadio1TxHighFreqReceiveRfFrequency = _HzQtmRadio1TxHighFreqReceiveRfFrequency_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 5, 5, 1, 3, 1, 4),
    _HzQtmRadio1TxHighFreqReceiveRfFrequency_Type()
)
hzQtmRadio1TxHighFreqReceiveRfFrequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzQtmRadio1TxHighFreqReceiveRfFrequency.setStatus("current")


class _HzQtmRadio1TxHighFreqProgrammed_Type(Integer32):
    """Custom type hzQtmRadio1TxHighFreqProgrammed based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("notActive", 2))
    )


_HzQtmRadio1TxHighFreqProgrammed_Type.__name__ = "Integer32"
_HzQtmRadio1TxHighFreqProgrammed_Object = MibTableColumn
hzQtmRadio1TxHighFreqProgrammed = _HzQtmRadio1TxHighFreqProgrammed_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 5, 5, 1, 3, 1, 5),
    _HzQtmRadio1TxHighFreqProgrammed_Type()
)
hzQtmRadio1TxHighFreqProgrammed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzQtmRadio1TxHighFreqProgrammed.setStatus("current")
_HzQtmRadio1TxLowFreqTable_Object = MibTable
hzQtmRadio1TxLowFreqTable = _HzQtmRadio1TxLowFreqTable_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 5, 5, 1, 4)
)
if mibBuilder.loadTexts:
    hzQtmRadio1TxLowFreqTable.setStatus("current")
_HzQtmRadio1TxLowFreqEntry_Object = MibTableRow
hzQtmRadio1TxLowFreqEntry = _HzQtmRadio1TxLowFreqEntry_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 5, 5, 1, 4, 1)
)
hzQtmRadio1TxLowFreqEntry.setIndexNames(
    (0, "DRAGONWAVE-HORIZON-QUANTUM-MIB", "hzQtmRadio1TxLowFreqIndex"),
)
if mibBuilder.loadTexts:
    hzQtmRadio1TxLowFreqEntry.setStatus("current")
_HzQtmRadio1TxLowFreqIndex_Type = Integer32
_HzQtmRadio1TxLowFreqIndex_Object = MibTableColumn
hzQtmRadio1TxLowFreqIndex = _HzQtmRadio1TxLowFreqIndex_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 5, 5, 1, 4, 1, 1),
    _HzQtmRadio1TxLowFreqIndex_Type()
)
hzQtmRadio1TxLowFreqIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzQtmRadio1TxLowFreqIndex.setStatus("current")
_HzQtmRadio1TxLowFreqChannelIndex_Type = DisplayString
_HzQtmRadio1TxLowFreqChannelIndex_Object = MibTableColumn
hzQtmRadio1TxLowFreqChannelIndex = _HzQtmRadio1TxLowFreqChannelIndex_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 5, 5, 1, 4, 1, 2),
    _HzQtmRadio1TxLowFreqChannelIndex_Type()
)
hzQtmRadio1TxLowFreqChannelIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzQtmRadio1TxLowFreqChannelIndex.setStatus("current")
_HzQtmRadio1TxLowFreqTransmitRfFrequency_Type = Integer32
_HzQtmRadio1TxLowFreqTransmitRfFrequency_Object = MibTableColumn
hzQtmRadio1TxLowFreqTransmitRfFrequency = _HzQtmRadio1TxLowFreqTransmitRfFrequency_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 5, 5, 1, 4, 1, 3),
    _HzQtmRadio1TxLowFreqTransmitRfFrequency_Type()
)
hzQtmRadio1TxLowFreqTransmitRfFrequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzQtmRadio1TxLowFreqTransmitRfFrequency.setStatus("current")
_HzQtmRadio1TxLowFreqReceiveRfFrequency_Type = Integer32
_HzQtmRadio1TxLowFreqReceiveRfFrequency_Object = MibTableColumn
hzQtmRadio1TxLowFreqReceiveRfFrequency = _HzQtmRadio1TxLowFreqReceiveRfFrequency_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 5, 5, 1, 4, 1, 4),
    _HzQtmRadio1TxLowFreqReceiveRfFrequency_Type()
)
hzQtmRadio1TxLowFreqReceiveRfFrequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzQtmRadio1TxLowFreqReceiveRfFrequency.setStatus("current")


class _HzQtmRadio1TxLowFreqProgrammed_Type(Integer32):
    """Custom type hzQtmRadio1TxLowFreqProgrammed based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("notActive", 2))
    )


_HzQtmRadio1TxLowFreqProgrammed_Type.__name__ = "Integer32"
_HzQtmRadio1TxLowFreqProgrammed_Object = MibTableColumn
hzQtmRadio1TxLowFreqProgrammed = _HzQtmRadio1TxLowFreqProgrammed_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 5, 5, 1, 4, 1, 5),
    _HzQtmRadio1TxLowFreqProgrammed_Type()
)
hzQtmRadio1TxLowFreqProgrammed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzQtmRadio1TxLowFreqProgrammed.setStatus("current")
_HzQtmRadio1ProgrammedFrequency_ObjectIdentity = ObjectIdentity
hzQtmRadio1ProgrammedFrequency = _HzQtmRadio1ProgrammedFrequency_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 5, 5, 1, 5)
)
_HzQtmRadio1ProgrammedFrequencyChannel_Type = DisplayString
_HzQtmRadio1ProgrammedFrequencyChannel_Object = MibScalar
hzQtmRadio1ProgrammedFrequencyChannel = _HzQtmRadio1ProgrammedFrequencyChannel_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 5, 5, 1, 5, 1),
    _HzQtmRadio1ProgrammedFrequencyChannel_Type()
)
hzQtmRadio1ProgrammedFrequencyChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzQtmRadio1ProgrammedFrequencyChannel.setStatus("current")
_HzQtmRadio1ProgrammedFrequencyTxRf_Type = Integer32
_HzQtmRadio1ProgrammedFrequencyTxRf_Object = MibScalar
hzQtmRadio1ProgrammedFrequencyTxRf = _HzQtmRadio1ProgrammedFrequencyTxRf_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 5, 5, 1, 5, 2),
    _HzQtmRadio1ProgrammedFrequencyTxRf_Type()
)
hzQtmRadio1ProgrammedFrequencyTxRf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzQtmRadio1ProgrammedFrequencyTxRf.setStatus("current")
_HzQtmRadio1ProgrammedFrequencyRxRf_Type = Integer32
_HzQtmRadio1ProgrammedFrequencyRxRf_Object = MibScalar
hzQtmRadio1ProgrammedFrequencyRxRf = _HzQtmRadio1ProgrammedFrequencyRxRf_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 5, 5, 1, 5, 3),
    _HzQtmRadio1ProgrammedFrequencyRxRf_Type()
)
hzQtmRadio1ProgrammedFrequencyRxRf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzQtmRadio1ProgrammedFrequencyRxRf.setStatus("current")
_HzQtmWirelessInterfaceRadio2Frequencies_ObjectIdentity = ObjectIdentity
hzQtmWirelessInterfaceRadio2Frequencies = _HzQtmWirelessInterfaceRadio2Frequencies_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 5, 5, 2)
)


class _HzQtmRadio2FreqGroupSelected_Type(Integer32):
    """Custom type hzQtmRadio2FreqGroupSelected based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("txLow", 1),
          ("txHigh", 2),
          ("none", 3))
    )


_HzQtmRadio2FreqGroupSelected_Type.__name__ = "Integer32"
_HzQtmRadio2FreqGroupSelected_Object = MibScalar
hzQtmRadio2FreqGroupSelected = _HzQtmRadio2FreqGroupSelected_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 5, 5, 2, 1),
    _HzQtmRadio2FreqGroupSelected_Type()
)
hzQtmRadio2FreqGroupSelected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzQtmRadio2FreqGroupSelected.setStatus("current")
_HzQtmRadio2BandTable_Object = MibTable
hzQtmRadio2BandTable = _HzQtmRadio2BandTable_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 5, 5, 2, 2)
)
if mibBuilder.loadTexts:
    hzQtmRadio2BandTable.setStatus("current")
_HzQtmRadio2BandEntry_Object = MibTableRow
hzQtmRadio2BandEntry = _HzQtmRadio2BandEntry_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 5, 5, 2, 2, 1)
)
hzQtmRadio2BandEntry.setIndexNames(
    (0, "DRAGONWAVE-HORIZON-QUANTUM-MIB", "hzQtmRadio2BandIndex"),
)
if mibBuilder.loadTexts:
    hzQtmRadio2BandEntry.setStatus("current")
_HzQtmRadio2BandIndex_Type = Integer32
_HzQtmRadio2BandIndex_Object = MibTableColumn
hzQtmRadio2BandIndex = _HzQtmRadio2BandIndex_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 5, 5, 2, 2, 1, 1),
    _HzQtmRadio2BandIndex_Type()
)
hzQtmRadio2BandIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzQtmRadio2BandIndex.setStatus("current")
_HzQtmRadio2BandId_Type = Integer32
_HzQtmRadio2BandId_Object = MibTableColumn
hzQtmRadio2BandId = _HzQtmRadio2BandId_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 5, 5, 2, 2, 1, 2),
    _HzQtmRadio2BandId_Type()
)
hzQtmRadio2BandId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzQtmRadio2BandId.setStatus("current")
_HzQtmRadio2BandName_Type = DisplayString
_HzQtmRadio2BandName_Object = MibTableColumn
hzQtmRadio2BandName = _HzQtmRadio2BandName_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 5, 5, 2, 2, 1, 3),
    _HzQtmRadio2BandName_Type()
)
hzQtmRadio2BandName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzQtmRadio2BandName.setStatus("current")


class _HzQtmRadio2BandProgrammed_Type(Integer32):
    """Custom type hzQtmRadio2BandProgrammed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("notActive", 2))
    )


_HzQtmRadio2BandProgrammed_Type.__name__ = "Integer32"
_HzQtmRadio2BandProgrammed_Object = MibTableColumn
hzQtmRadio2BandProgrammed = _HzQtmRadio2BandProgrammed_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 5, 5, 2, 2, 1, 4),
    _HzQtmRadio2BandProgrammed_Type()
)
hzQtmRadio2BandProgrammed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzQtmRadio2BandProgrammed.setStatus("current")
_HzQtmRadio2TxHighFreqTable_Object = MibTable
hzQtmRadio2TxHighFreqTable = _HzQtmRadio2TxHighFreqTable_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 5, 5, 2, 3)
)
if mibBuilder.loadTexts:
    hzQtmRadio2TxHighFreqTable.setStatus("current")
_HzQtmRadio2TxHighFreqEntry_Object = MibTableRow
hzQtmRadio2TxHighFreqEntry = _HzQtmRadio2TxHighFreqEntry_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 5, 5, 2, 3, 1)
)
hzQtmRadio2TxHighFreqEntry.setIndexNames(
    (0, "DRAGONWAVE-HORIZON-QUANTUM-MIB", "hzQtmRadio2TxHighFreqIndex"),
)
if mibBuilder.loadTexts:
    hzQtmRadio2TxHighFreqEntry.setStatus("current")
_HzQtmRadio2TxHighFreqIndex_Type = Integer32
_HzQtmRadio2TxHighFreqIndex_Object = MibTableColumn
hzQtmRadio2TxHighFreqIndex = _HzQtmRadio2TxHighFreqIndex_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 5, 5, 2, 3, 1, 1),
    _HzQtmRadio2TxHighFreqIndex_Type()
)
hzQtmRadio2TxHighFreqIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzQtmRadio2TxHighFreqIndex.setStatus("current")
_HzQtmRadio2TxHighFreqChannelIndex_Type = DisplayString
_HzQtmRadio2TxHighFreqChannelIndex_Object = MibTableColumn
hzQtmRadio2TxHighFreqChannelIndex = _HzQtmRadio2TxHighFreqChannelIndex_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 5, 5, 2, 3, 1, 2),
    _HzQtmRadio2TxHighFreqChannelIndex_Type()
)
hzQtmRadio2TxHighFreqChannelIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzQtmRadio2TxHighFreqChannelIndex.setStatus("current")
_HzQtmRadio2TxHighFreqTransmitRfFrequency_Type = Integer32
_HzQtmRadio2TxHighFreqTransmitRfFrequency_Object = MibTableColumn
hzQtmRadio2TxHighFreqTransmitRfFrequency = _HzQtmRadio2TxHighFreqTransmitRfFrequency_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 5, 5, 2, 3, 1, 3),
    _HzQtmRadio2TxHighFreqTransmitRfFrequency_Type()
)
hzQtmRadio2TxHighFreqTransmitRfFrequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzQtmRadio2TxHighFreqTransmitRfFrequency.setStatus("current")
_HzQtmRadio2TxHighFreqReceiveRfFrequency_Type = Integer32
_HzQtmRadio2TxHighFreqReceiveRfFrequency_Object = MibTableColumn
hzQtmRadio2TxHighFreqReceiveRfFrequency = _HzQtmRadio2TxHighFreqReceiveRfFrequency_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 5, 5, 2, 3, 1, 4),
    _HzQtmRadio2TxHighFreqReceiveRfFrequency_Type()
)
hzQtmRadio2TxHighFreqReceiveRfFrequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzQtmRadio2TxHighFreqReceiveRfFrequency.setStatus("current")


class _HzQtmRadio2TxHighFreqProgrammed_Type(Integer32):
    """Custom type hzQtmRadio2TxHighFreqProgrammed based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("notActive", 2))
    )


_HzQtmRadio2TxHighFreqProgrammed_Type.__name__ = "Integer32"
_HzQtmRadio2TxHighFreqProgrammed_Object = MibTableColumn
hzQtmRadio2TxHighFreqProgrammed = _HzQtmRadio2TxHighFreqProgrammed_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 5, 5, 2, 3, 1, 5),
    _HzQtmRadio2TxHighFreqProgrammed_Type()
)
hzQtmRadio2TxHighFreqProgrammed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzQtmRadio2TxHighFreqProgrammed.setStatus("current")
_HzQtmRadio2TxLowFreqTable_Object = MibTable
hzQtmRadio2TxLowFreqTable = _HzQtmRadio2TxLowFreqTable_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 5, 5, 2, 4)
)
if mibBuilder.loadTexts:
    hzQtmRadio2TxLowFreqTable.setStatus("current")
_HzQtmRadio2TxLowFreqEntry_Object = MibTableRow
hzQtmRadio2TxLowFreqEntry = _HzQtmRadio2TxLowFreqEntry_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 5, 5, 2, 4, 1)
)
hzQtmRadio2TxLowFreqEntry.setIndexNames(
    (0, "DRAGONWAVE-HORIZON-QUANTUM-MIB", "hzQtmRadio2TxLowFreqIndex"),
)
if mibBuilder.loadTexts:
    hzQtmRadio2TxLowFreqEntry.setStatus("current")
_HzQtmRadio2TxLowFreqIndex_Type = Integer32
_HzQtmRadio2TxLowFreqIndex_Object = MibTableColumn
hzQtmRadio2TxLowFreqIndex = _HzQtmRadio2TxLowFreqIndex_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 5, 5, 2, 4, 1, 1),
    _HzQtmRadio2TxLowFreqIndex_Type()
)
hzQtmRadio2TxLowFreqIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzQtmRadio2TxLowFreqIndex.setStatus("current")
_HzQtmRadio2TxLowFreqChannelIndex_Type = DisplayString
_HzQtmRadio2TxLowFreqChannelIndex_Object = MibTableColumn
hzQtmRadio2TxLowFreqChannelIndex = _HzQtmRadio2TxLowFreqChannelIndex_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 5, 5, 2, 4, 1, 2),
    _HzQtmRadio2TxLowFreqChannelIndex_Type()
)
hzQtmRadio2TxLowFreqChannelIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzQtmRadio2TxLowFreqChannelIndex.setStatus("current")
_HzQtmRadio2TxLowFreqTransmitRfFrequency_Type = Integer32
_HzQtmRadio2TxLowFreqTransmitRfFrequency_Object = MibTableColumn
hzQtmRadio2TxLowFreqTransmitRfFrequency = _HzQtmRadio2TxLowFreqTransmitRfFrequency_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 5, 5, 2, 4, 1, 3),
    _HzQtmRadio2TxLowFreqTransmitRfFrequency_Type()
)
hzQtmRadio2TxLowFreqTransmitRfFrequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzQtmRadio2TxLowFreqTransmitRfFrequency.setStatus("current")
_HzQtmRadio2TxLowFreqReceiveRfFrequency_Type = Integer32
_HzQtmRadio2TxLowFreqReceiveRfFrequency_Object = MibTableColumn
hzQtmRadio2TxLowFreqReceiveRfFrequency = _HzQtmRadio2TxLowFreqReceiveRfFrequency_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 5, 5, 2, 4, 1, 4),
    _HzQtmRadio2TxLowFreqReceiveRfFrequency_Type()
)
hzQtmRadio2TxLowFreqReceiveRfFrequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzQtmRadio2TxLowFreqReceiveRfFrequency.setStatus("current")


class _HzQtmRadio2TxLowFreqProgrammed_Type(Integer32):
    """Custom type hzQtmRadio2TxLowFreqProgrammed based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("notActive", 2))
    )


_HzQtmRadio2TxLowFreqProgrammed_Type.__name__ = "Integer32"
_HzQtmRadio2TxLowFreqProgrammed_Object = MibTableColumn
hzQtmRadio2TxLowFreqProgrammed = _HzQtmRadio2TxLowFreqProgrammed_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 5, 5, 2, 4, 1, 5),
    _HzQtmRadio2TxLowFreqProgrammed_Type()
)
hzQtmRadio2TxLowFreqProgrammed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzQtmRadio2TxLowFreqProgrammed.setStatus("current")
_HzQtmRadio2ProgrammedFrequency_ObjectIdentity = ObjectIdentity
hzQtmRadio2ProgrammedFrequency = _HzQtmRadio2ProgrammedFrequency_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 5, 5, 2, 5)
)
_HzQtmRadio2ProgrammedFrequencyChannel_Type = DisplayString
_HzQtmRadio2ProgrammedFrequencyChannel_Object = MibScalar
hzQtmRadio2ProgrammedFrequencyChannel = _HzQtmRadio2ProgrammedFrequencyChannel_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 5, 5, 2, 5, 1),
    _HzQtmRadio2ProgrammedFrequencyChannel_Type()
)
hzQtmRadio2ProgrammedFrequencyChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzQtmRadio2ProgrammedFrequencyChannel.setStatus("current")
_HzQtmRadio2ProgrammedFrequencyTxRf_Type = Integer32
_HzQtmRadio2ProgrammedFrequencyTxRf_Object = MibScalar
hzQtmRadio2ProgrammedFrequencyTxRf = _HzQtmRadio2ProgrammedFrequencyTxRf_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 5, 5, 2, 5, 2),
    _HzQtmRadio2ProgrammedFrequencyTxRf_Type()
)
hzQtmRadio2ProgrammedFrequencyTxRf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzQtmRadio2ProgrammedFrequencyTxRf.setStatus("current")
_HzQtmRadio2ProgrammedFrequencyRxRf_Type = Integer32
_HzQtmRadio2ProgrammedFrequencyRxRf_Object = MibScalar
hzQtmRadio2ProgrammedFrequencyRxRf = _HzQtmRadio2ProgrammedFrequencyRxRf_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 5, 5, 2, 5, 3),
    _HzQtmRadio2ProgrammedFrequencyRxRf_Type()
)
hzQtmRadio2ProgrammedFrequencyRxRf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzQtmRadio2ProgrammedFrequencyRxRf.setStatus("current")
_HzQtmWirelessInterfaceAntenna_ObjectIdentity = ObjectIdentity
hzQtmWirelessInterfaceAntenna = _HzQtmWirelessInterfaceAntenna_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 5, 6)
)


class _HzQtmAntennaDiameter_Type(Integer32):
    """Custom type hzQtmAntennaDiameter based on Integer32"""
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
        *(("antenna12", 1),
          ("antenna24", 2),
          ("antenna36", 3),
          ("antenna48", 4),
          ("antenna72", 5))
    )


_HzQtmAntennaDiameter_Type.__name__ = "Integer32"
_HzQtmAntennaDiameter_Object = MibScalar
hzQtmAntennaDiameter = _HzQtmAntennaDiameter_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 5, 6, 1),
    _HzQtmAntennaDiameter_Type()
)
hzQtmAntennaDiameter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzQtmAntennaDiameter.setStatus("current")


class _HzQtmAntenna1Tilt_Type(Integer32):
    """Custom type hzQtmAntenna1Tilt based on Integer32"""
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
        *(("unknown", 1),
          ("vertical", 2),
          ("horizontal", 3),
          ("flat", 4))
    )


_HzQtmAntenna1Tilt_Type.__name__ = "Integer32"
_HzQtmAntenna1Tilt_Object = MibScalar
hzQtmAntenna1Tilt = _HzQtmAntenna1Tilt_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 5, 6, 2),
    _HzQtmAntenna1Tilt_Type()
)
hzQtmAntenna1Tilt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzQtmAntenna1Tilt.setStatus("current")


class _HzQtmAntenna2Tilt_Type(Integer32):
    """Custom type hzQtmAntenna2Tilt based on Integer32"""
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
        *(("unknown", 1),
          ("vertical", 2),
          ("horizontal", 3),
          ("flat", 4))
    )


_HzQtmAntenna2Tilt_Type.__name__ = "Integer32"
_HzQtmAntenna2Tilt_Object = MibScalar
hzQtmAntenna2Tilt = _HzQtmAntenna2Tilt_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 5, 6, 3),
    _HzQtmAntenna2Tilt_Type()
)
hzQtmAntenna2Tilt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzQtmAntenna2Tilt.setStatus("current")
_HzQtmWirelessInterfaceRedundancy_ObjectIdentity = ObjectIdentity
hzQtmWirelessInterfaceRedundancy = _HzQtmWirelessInterfaceRedundancy_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 5, 7)
)


class _HzQtmWirelessInterfaceRedundancyActiveWirelessPort_Type(Integer32):
    """Custom type hzQtmWirelessInterfaceRedundancyActiveWirelessPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("wireless-port-1", 1),
          ("wireless-port-2", 2),
          ("none", 3))
    )


_HzQtmWirelessInterfaceRedundancyActiveWirelessPort_Type.__name__ = "Integer32"
_HzQtmWirelessInterfaceRedundancyActiveWirelessPort_Object = MibScalar
hzQtmWirelessInterfaceRedundancyActiveWirelessPort = _HzQtmWirelessInterfaceRedundancyActiveWirelessPort_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 5, 7, 1),
    _HzQtmWirelessInterfaceRedundancyActiveWirelessPort_Type()
)
hzQtmWirelessInterfaceRedundancyActiveWirelessPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzQtmWirelessInterfaceRedundancyActiveWirelessPort.setStatus("current")


class _HzQtmWirelessInterfaceRedundancyPrimaryWirelessPort_Type(Integer32):
    """Custom type hzQtmWirelessInterfaceRedundancyPrimaryWirelessPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("wireless-port-1", 1),
          ("wireless-port-2", 2),
          ("none", 3))
    )


_HzQtmWirelessInterfaceRedundancyPrimaryWirelessPort_Type.__name__ = "Integer32"
_HzQtmWirelessInterfaceRedundancyPrimaryWirelessPort_Object = MibScalar
hzQtmWirelessInterfaceRedundancyPrimaryWirelessPort = _HzQtmWirelessInterfaceRedundancyPrimaryWirelessPort_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 5, 7, 2),
    _HzQtmWirelessInterfaceRedundancyPrimaryWirelessPort_Type()
)
hzQtmWirelessInterfaceRedundancyPrimaryWirelessPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzQtmWirelessInterfaceRedundancyPrimaryWirelessPort.setStatus("current")


class _HzQtmWirelessInterfaceRedundancySwitchingAlgorithm_Type(Integer32):
    """Custom type hzQtmWirelessInterfaceRedundancySwitchingAlgorithm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("manual", 1),
          ("algorithm-based", 2))
    )


_HzQtmWirelessInterfaceRedundancySwitchingAlgorithm_Type.__name__ = "Integer32"
_HzQtmWirelessInterfaceRedundancySwitchingAlgorithm_Object = MibScalar
hzQtmWirelessInterfaceRedundancySwitchingAlgorithm = _HzQtmWirelessInterfaceRedundancySwitchingAlgorithm_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 5, 7, 3),
    _HzQtmWirelessInterfaceRedundancySwitchingAlgorithm_Type()
)
hzQtmWirelessInterfaceRedundancySwitchingAlgorithm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzQtmWirelessInterfaceRedundancySwitchingAlgorithm.setStatus("current")
_HzQtmWirelessInterfaceRedundancySwitchCause_Type = DisplayString
_HzQtmWirelessInterfaceRedundancySwitchCause_Object = MibScalar
hzQtmWirelessInterfaceRedundancySwitchCause = _HzQtmWirelessInterfaceRedundancySwitchCause_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 5, 7, 4),
    _HzQtmWirelessInterfaceRedundancySwitchCause_Type()
)
hzQtmWirelessInterfaceRedundancySwitchCause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzQtmWirelessInterfaceRedundancySwitchCause.setStatus("current")


class _HzQtmWirelessInterfaceRedundancyRemoveFaulty_Type(Integer32):
    """Custom type hzQtmWirelessInterfaceRedundancyRemoveFaulty based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("wireless-port-1", 1),
          ("wireless-port-2", 2))
    )


_HzQtmWirelessInterfaceRedundancyRemoveFaulty_Type.__name__ = "Integer32"
_HzQtmWirelessInterfaceRedundancyRemoveFaulty_Object = MibScalar
hzQtmWirelessInterfaceRedundancyRemoveFaulty = _HzQtmWirelessInterfaceRedundancyRemoveFaulty_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 5, 7, 5),
    _HzQtmWirelessInterfaceRedundancyRemoveFaulty_Type()
)
hzQtmWirelessInterfaceRedundancyRemoveFaulty.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzQtmWirelessInterfaceRedundancyRemoveFaulty.setStatus("current")
_HzQtmWirelessInterfaceRedundancyDiagnostics_ObjectIdentity = ObjectIdentity
hzQtmWirelessInterfaceRedundancyDiagnostics = _HzQtmWirelessInterfaceRedundancyDiagnostics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 5, 7, 6)
)


class _HzQtmWirelessInterfaceRedundancyDiagnose_Type(Integer32):
    """Custom type hzQtmWirelessInterfaceRedundancyDiagnose based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("diagnose", 1)
    )


_HzQtmWirelessInterfaceRedundancyDiagnose_Type.__name__ = "Integer32"
_HzQtmWirelessInterfaceRedundancyDiagnose_Object = MibScalar
hzQtmWirelessInterfaceRedundancyDiagnose = _HzQtmWirelessInterfaceRedundancyDiagnose_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 5, 7, 6, 1),
    _HzQtmWirelessInterfaceRedundancyDiagnose_Type()
)
hzQtmWirelessInterfaceRedundancyDiagnose.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzQtmWirelessInterfaceRedundancyDiagnose.setStatus("current")
_HzQtmWirelessInterfaceRedundancyDiagnosticResult_Type = DisplayString
_HzQtmWirelessInterfaceRedundancyDiagnosticResult_Object = MibScalar
hzQtmWirelessInterfaceRedundancyDiagnosticResult = _HzQtmWirelessInterfaceRedundancyDiagnosticResult_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 5, 7, 6, 2),
    _HzQtmWirelessInterfaceRedundancyDiagnosticResult_Type()
)
hzQtmWirelessInterfaceRedundancyDiagnosticResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzQtmWirelessInterfaceRedundancyDiagnosticResult.setStatus("current")
_HzQtmWirelessInterfaceRedundancyRadioSwitch_ObjectIdentity = ObjectIdentity
hzQtmWirelessInterfaceRedundancyRadioSwitch = _HzQtmWirelessInterfaceRedundancyRadioSwitch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 5, 7, 7)
)


class _HzQtmWirelessInterfaceRedundancySwitchRadio_Type(Integer32):
    """Custom type hzQtmWirelessInterfaceRedundancySwitchRadio based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("switch", 1)
    )


_HzQtmWirelessInterfaceRedundancySwitchRadio_Type.__name__ = "Integer32"
_HzQtmWirelessInterfaceRedundancySwitchRadio_Object = MibScalar
hzQtmWirelessInterfaceRedundancySwitchRadio = _HzQtmWirelessInterfaceRedundancySwitchRadio_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 5, 7, 7, 1),
    _HzQtmWirelessInterfaceRedundancySwitchRadio_Type()
)
hzQtmWirelessInterfaceRedundancySwitchRadio.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzQtmWirelessInterfaceRedundancySwitchRadio.setStatus("current")
_HzQtmWirelessInterfaceRedundancySwitchRadioResult_Type = DisplayString
_HzQtmWirelessInterfaceRedundancySwitchRadioResult_Object = MibScalar
hzQtmWirelessInterfaceRedundancySwitchRadioResult = _HzQtmWirelessInterfaceRedundancySwitchRadioResult_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 5, 7, 7, 2),
    _HzQtmWirelessInterfaceRedundancySwitchRadioResult_Type()
)
hzQtmWirelessInterfaceRedundancySwitchRadioResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzQtmWirelessInterfaceRedundancySwitchRadioResult.setStatus("current")
_HzQtmCalendar_ObjectIdentity = ObjectIdentity
hzQtmCalendar = _HzQtmCalendar_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 6)
)
_HzQtmDate_Type = DisplayString
_HzQtmDate_Object = MibScalar
hzQtmDate = _HzQtmDate_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 6, 1),
    _HzQtmDate_Type()
)
hzQtmDate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzQtmDate.setStatus("current")
_HzQtmTime_Type = DisplayString
_HzQtmTime_Object = MibScalar
hzQtmTime = _HzQtmTime_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 6, 2),
    _HzQtmTime_Type()
)
hzQtmTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzQtmTime.setStatus("current")
_HzQtmAlarms_ObjectIdentity = ObjectIdentity
hzQtmAlarms = _HzQtmAlarms_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 7)
)


class _HzQtmClearAlarmCounters_Type(Integer32):
    """Custom type hzQtmClearAlarmCounters based on Integer32"""
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
        *(("nicCounters", 1),
          ("modemCounters", 2),
          ("radioCounters", 3),
          ("allCounters", 4),
          ("otherCounters", 5))
    )


_HzQtmClearAlarmCounters_Type.__name__ = "Integer32"
_HzQtmClearAlarmCounters_Object = MibScalar
hzQtmClearAlarmCounters = _HzQtmClearAlarmCounters_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 7, 1),
    _HzQtmClearAlarmCounters_Type()
)
hzQtmClearAlarmCounters.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzQtmClearAlarmCounters.setStatus("current")
_HzQtmSystemAlarms_ObjectIdentity = ObjectIdentity
hzQtmSystemAlarms = _HzQtmSystemAlarms_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 7, 2)
)


class _HzQtmExplicitAuthenticationFailureAlarm_Type(Integer32):
    """Custom type hzQtmExplicitAuthenticationFailureAlarm based on Integer32"""
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


_HzQtmExplicitAuthenticationFailureAlarm_Type.__name__ = "Integer32"
_HzQtmExplicitAuthenticationFailureAlarm_Object = MibScalar
hzQtmExplicitAuthenticationFailureAlarm = _HzQtmExplicitAuthenticationFailureAlarm_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 7, 2, 1),
    _HzQtmExplicitAuthenticationFailureAlarm_Type()
)
hzQtmExplicitAuthenticationFailureAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzQtmExplicitAuthenticationFailureAlarm.setStatus("current")
_HzQtmExplicitAuthenticationFailureCounts_Type = Counter32
_HzQtmExplicitAuthenticationFailureCounts_Object = MibScalar
hzQtmExplicitAuthenticationFailureCounts = _HzQtmExplicitAuthenticationFailureCounts_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 7, 2, 2),
    _HzQtmExplicitAuthenticationFailureCounts_Type()
)
hzQtmExplicitAuthenticationFailureCounts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzQtmExplicitAuthenticationFailureCounts.setStatus("current")


class _HzQtmHitlessAamConfigMismatchAlarm_Type(Integer32):
    """Custom type hzQtmHitlessAamConfigMismatchAlarm based on Integer32"""
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


_HzQtmHitlessAamConfigMismatchAlarm_Type.__name__ = "Integer32"
_HzQtmHitlessAamConfigMismatchAlarm_Object = MibScalar
hzQtmHitlessAamConfigMismatchAlarm = _HzQtmHitlessAamConfigMismatchAlarm_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 7, 2, 3),
    _HzQtmHitlessAamConfigMismatchAlarm_Type()
)
hzQtmHitlessAamConfigMismatchAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzQtmHitlessAamConfigMismatchAlarm.setStatus("current")
_HzQtmHitlessAamConfigMismatchCounts_Type = Counter32
_HzQtmHitlessAamConfigMismatchCounts_Object = MibScalar
hzQtmHitlessAamConfigMismatchCounts = _HzQtmHitlessAamConfigMismatchCounts_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 7, 2, 4),
    _HzQtmHitlessAamConfigMismatchCounts_Type()
)
hzQtmHitlessAamConfigMismatchCounts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzQtmHitlessAamConfigMismatchCounts.setStatus("current")


class _HzQtmHitlessAamActiveAlarm_Type(Integer32):
    """Custom type hzQtmHitlessAamActiveAlarm based on Integer32"""
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


_HzQtmHitlessAamActiveAlarm_Type.__name__ = "Integer32"
_HzQtmHitlessAamActiveAlarm_Object = MibScalar
hzQtmHitlessAamActiveAlarm = _HzQtmHitlessAamActiveAlarm_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 7, 2, 5),
    _HzQtmHitlessAamActiveAlarm_Type()
)
hzQtmHitlessAamActiveAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzQtmHitlessAamActiveAlarm.setStatus("current")
_HzQtmHitlessAamActiveCounts_Type = Counter32
_HzQtmHitlessAamActiveCounts_Object = MibScalar
hzQtmHitlessAamActiveCounts = _HzQtmHitlessAamActiveCounts_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 7, 2, 6),
    _HzQtmHitlessAamActiveCounts_Type()
)
hzQtmHitlessAamActiveCounts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzQtmHitlessAamActiveCounts.setStatus("current")


class _HzQtmSntpServerUnreachableAlarm_Type(Integer32):
    """Custom type hzQtmSntpServerUnreachableAlarm based on Integer32"""
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


_HzQtmSntpServerUnreachableAlarm_Type.__name__ = "Integer32"
_HzQtmSntpServerUnreachableAlarm_Object = MibScalar
hzQtmSntpServerUnreachableAlarm = _HzQtmSntpServerUnreachableAlarm_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 7, 2, 7),
    _HzQtmSntpServerUnreachableAlarm_Type()
)
hzQtmSntpServerUnreachableAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzQtmSntpServerUnreachableAlarm.setStatus("current")
_HzQtmSntpServerUnreachableCounts_Type = Counter32
_HzQtmSntpServerUnreachableCounts_Object = MibScalar
hzQtmSntpServerUnreachableCounts = _HzQtmSntpServerUnreachableCounts_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 7, 2, 8),
    _HzQtmSntpServerUnreachableCounts_Type()
)
hzQtmSntpServerUnreachableCounts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzQtmSntpServerUnreachableCounts.setStatus("current")


class _HzQtmFrequencyFileInvalidAlarm_Type(Integer32):
    """Custom type hzQtmFrequencyFileInvalidAlarm based on Integer32"""
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


_HzQtmFrequencyFileInvalidAlarm_Type.__name__ = "Integer32"
_HzQtmFrequencyFileInvalidAlarm_Object = MibScalar
hzQtmFrequencyFileInvalidAlarm = _HzQtmFrequencyFileInvalidAlarm_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 7, 2, 9),
    _HzQtmFrequencyFileInvalidAlarm_Type()
)
hzQtmFrequencyFileInvalidAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzQtmFrequencyFileInvalidAlarm.setStatus("current")
_HzQtmFrequencyFileInvalidCounts_Type = Counter32
_HzQtmFrequencyFileInvalidCounts_Object = MibScalar
hzQtmFrequencyFileInvalidCounts = _HzQtmFrequencyFileInvalidCounts_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 7, 2, 10),
    _HzQtmFrequencyFileInvalidCounts_Type()
)
hzQtmFrequencyFileInvalidCounts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzQtmFrequencyFileInvalidCounts.setStatus("current")


class _HzQtmFanFailureAlarm_Type(Integer32):
    """Custom type hzQtmFanFailureAlarm based on Integer32"""
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


_HzQtmFanFailureAlarm_Type.__name__ = "Integer32"
_HzQtmFanFailureAlarm_Object = MibScalar
hzQtmFanFailureAlarm = _HzQtmFanFailureAlarm_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 7, 2, 11),
    _HzQtmFanFailureAlarm_Type()
)
hzQtmFanFailureAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzQtmFanFailureAlarm.setStatus("current")
_HzQtmFanFailureCounts_Type = Counter32
_HzQtmFanFailureCounts_Object = MibScalar
hzQtmFanFailureCounts = _HzQtmFanFailureCounts_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 7, 2, 12),
    _HzQtmFanFailureCounts_Type()
)
hzQtmFanFailureCounts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzQtmFanFailureCounts.setStatus("current")


class _HzQtmRedundancyPrimaryPortNotSetAlarm_Type(Integer32):
    """Custom type hzQtmRedundancyPrimaryPortNotSetAlarm based on Integer32"""
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


_HzQtmRedundancyPrimaryPortNotSetAlarm_Type.__name__ = "Integer32"
_HzQtmRedundancyPrimaryPortNotSetAlarm_Object = MibScalar
hzQtmRedundancyPrimaryPortNotSetAlarm = _HzQtmRedundancyPrimaryPortNotSetAlarm_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 7, 2, 13),
    _HzQtmRedundancyPrimaryPortNotSetAlarm_Type()
)
hzQtmRedundancyPrimaryPortNotSetAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzQtmRedundancyPrimaryPortNotSetAlarm.setStatus("current")
_HzQtmRedundancyPrimaryPortNotSetCounts_Type = Counter32
_HzQtmRedundancyPrimaryPortNotSetCounts_Object = MibScalar
hzQtmRedundancyPrimaryPortNotSetCounts = _HzQtmRedundancyPrimaryPortNotSetCounts_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 7, 2, 14),
    _HzQtmRedundancyPrimaryPortNotSetCounts_Type()
)
hzQtmRedundancyPrimaryPortNotSetCounts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzQtmRedundancyPrimaryPortNotSetCounts.setStatus("current")


class _HzQtmRedundancySecondaryPortActiveAlarm_Type(Integer32):
    """Custom type hzQtmRedundancySecondaryPortActiveAlarm based on Integer32"""
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


_HzQtmRedundancySecondaryPortActiveAlarm_Type.__name__ = "Integer32"
_HzQtmRedundancySecondaryPortActiveAlarm_Object = MibScalar
hzQtmRedundancySecondaryPortActiveAlarm = _HzQtmRedundancySecondaryPortActiveAlarm_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 7, 2, 15),
    _HzQtmRedundancySecondaryPortActiveAlarm_Type()
)
hzQtmRedundancySecondaryPortActiveAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzQtmRedundancySecondaryPortActiveAlarm.setStatus("current")
_HzQtmRedundancySecondaryPortActiveCounts_Type = Counter32
_HzQtmRedundancySecondaryPortActiveCounts_Object = MibScalar
hzQtmRedundancySecondaryPortActiveCounts = _HzQtmRedundancySecondaryPortActiveCounts_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 7, 2, 16),
    _HzQtmRedundancySecondaryPortActiveCounts_Type()
)
hzQtmRedundancySecondaryPortActiveCounts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzQtmRedundancySecondaryPortActiveCounts.setStatus("current")


class _HzQtmRedundancyPrimaryPortFaultyAlarm_Type(Integer32):
    """Custom type hzQtmRedundancyPrimaryPortFaultyAlarm based on Integer32"""
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


_HzQtmRedundancyPrimaryPortFaultyAlarm_Type.__name__ = "Integer32"
_HzQtmRedundancyPrimaryPortFaultyAlarm_Object = MibScalar
hzQtmRedundancyPrimaryPortFaultyAlarm = _HzQtmRedundancyPrimaryPortFaultyAlarm_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 7, 2, 17),
    _HzQtmRedundancyPrimaryPortFaultyAlarm_Type()
)
hzQtmRedundancyPrimaryPortFaultyAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzQtmRedundancyPrimaryPortFaultyAlarm.setStatus("current")
_HzQtmRedundancyPrimaryPortFaultyCounts_Type = Counter32
_HzQtmRedundancyPrimaryPortFaultyCounts_Object = MibScalar
hzQtmRedundancyPrimaryPortFaultyCounts = _HzQtmRedundancyPrimaryPortFaultyCounts_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 7, 2, 18),
    _HzQtmRedundancyPrimaryPortFaultyCounts_Type()
)
hzQtmRedundancyPrimaryPortFaultyCounts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzQtmRedundancyPrimaryPortFaultyCounts.setStatus("current")


class _HzQtmRedundancySecondaryPortFaultyAlarm_Type(Integer32):
    """Custom type hzQtmRedundancySecondaryPortFaultyAlarm based on Integer32"""
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


_HzQtmRedundancySecondaryPortFaultyAlarm_Type.__name__ = "Integer32"
_HzQtmRedundancySecondaryPortFaultyAlarm_Object = MibScalar
hzQtmRedundancySecondaryPortFaultyAlarm = _HzQtmRedundancySecondaryPortFaultyAlarm_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 7, 2, 19),
    _HzQtmRedundancySecondaryPortFaultyAlarm_Type()
)
hzQtmRedundancySecondaryPortFaultyAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzQtmRedundancySecondaryPortFaultyAlarm.setStatus("current")
_HzQtmRedundancySecondaryPortFaultyCounts_Type = Counter32
_HzQtmRedundancySecondaryPortFaultyCounts_Object = MibScalar
hzQtmRedundancySecondaryPortFaultyCounts = _HzQtmRedundancySecondaryPortFaultyCounts_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 7, 2, 20),
    _HzQtmRedundancySecondaryPortFaultyCounts_Type()
)
hzQtmRedundancySecondaryPortFaultyCounts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzQtmRedundancySecondaryPortFaultyCounts.setStatus("current")


class _HzQtmAtpcConfigMismatchAlarm_Type(Integer32):
    """Custom type hzQtmAtpcConfigMismatchAlarm based on Integer32"""
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


_HzQtmAtpcConfigMismatchAlarm_Type.__name__ = "Integer32"
_HzQtmAtpcConfigMismatchAlarm_Object = MibScalar
hzQtmAtpcConfigMismatchAlarm = _HzQtmAtpcConfigMismatchAlarm_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 7, 2, 21),
    _HzQtmAtpcConfigMismatchAlarm_Type()
)
hzQtmAtpcConfigMismatchAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzQtmAtpcConfigMismatchAlarm.setStatus("current")
_HzQtmAtpcConfigMismatchCounts_Type = Counter32
_HzQtmAtpcConfigMismatchCounts_Object = MibScalar
hzQtmAtpcConfigMismatchCounts = _HzQtmAtpcConfigMismatchCounts_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 7, 2, 22),
    _HzQtmAtpcConfigMismatchCounts_Type()
)
hzQtmAtpcConfigMismatchCounts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzQtmAtpcConfigMismatchCounts.setStatus("current")


class _HzQtmDroppedEnetFramesThresholdAlarm_Type(Integer32):
    """Custom type hzQtmDroppedEnetFramesThresholdAlarm based on Integer32"""
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


_HzQtmDroppedEnetFramesThresholdAlarm_Type.__name__ = "Integer32"
_HzQtmDroppedEnetFramesThresholdAlarm_Object = MibScalar
hzQtmDroppedEnetFramesThresholdAlarm = _HzQtmDroppedEnetFramesThresholdAlarm_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 7, 2, 23),
    _HzQtmDroppedEnetFramesThresholdAlarm_Type()
)
hzQtmDroppedEnetFramesThresholdAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzQtmDroppedEnetFramesThresholdAlarm.setStatus("current")
_HzQtmDroppedEnetFramesThresholdCounts_Type = Counter32
_HzQtmDroppedEnetFramesThresholdCounts_Object = MibScalar
hzQtmDroppedEnetFramesThresholdCounts = _HzQtmDroppedEnetFramesThresholdCounts_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 7, 2, 24),
    _HzQtmDroppedEnetFramesThresholdCounts_Type()
)
hzQtmDroppedEnetFramesThresholdCounts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzQtmDroppedEnetFramesThresholdCounts.setStatus("current")


class _HzQtmBandwidthUtilizationThresholdAlarm_Type(Integer32):
    """Custom type hzQtmBandwidthUtilizationThresholdAlarm based on Integer32"""
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


_HzQtmBandwidthUtilizationThresholdAlarm_Type.__name__ = "Integer32"
_HzQtmBandwidthUtilizationThresholdAlarm_Object = MibScalar
hzQtmBandwidthUtilizationThresholdAlarm = _HzQtmBandwidthUtilizationThresholdAlarm_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 7, 2, 25),
    _HzQtmBandwidthUtilizationThresholdAlarm_Type()
)
hzQtmBandwidthUtilizationThresholdAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzQtmBandwidthUtilizationThresholdAlarm.setStatus("current")
_HzQtmBandwidthUtilizationThresholdCounts_Type = Counter32
_HzQtmBandwidthUtilizationThresholdCounts_Object = MibScalar
hzQtmBandwidthUtilizationThresholdCounts = _HzQtmBandwidthUtilizationThresholdCounts_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 7, 2, 26),
    _HzQtmBandwidthUtilizationThresholdCounts_Type()
)
hzQtmBandwidthUtilizationThresholdCounts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzQtmBandwidthUtilizationThresholdCounts.setStatus("current")


class _HzQtmRlsMismatchAlarm_Type(Integer32):
    """Custom type hzQtmRlsMismatchAlarm based on Integer32"""
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


_HzQtmRlsMismatchAlarm_Type.__name__ = "Integer32"
_HzQtmRlsMismatchAlarm_Object = MibScalar
hzQtmRlsMismatchAlarm = _HzQtmRlsMismatchAlarm_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 7, 2, 27),
    _HzQtmRlsMismatchAlarm_Type()
)
hzQtmRlsMismatchAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzQtmRlsMismatchAlarm.setStatus("current")
_HzQtmRlsMismatchCounts_Type = Counter32
_HzQtmRlsMismatchCounts_Object = MibScalar
hzQtmRlsMismatchCounts = _HzQtmRlsMismatchCounts_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 7, 2, 28),
    _HzQtmRlsMismatchCounts_Type()
)
hzQtmRlsMismatchCounts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzQtmRlsMismatchCounts.setStatus("current")


class _HzQtmRLSQueueBasedShutdownActivatedAlarm_Type(Integer32):
    """Custom type hzQtmRLSQueueBasedShutdownActivatedAlarm based on Integer32"""
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


_HzQtmRLSQueueBasedShutdownActivatedAlarm_Type.__name__ = "Integer32"
_HzQtmRLSQueueBasedShutdownActivatedAlarm_Object = MibScalar
hzQtmRLSQueueBasedShutdownActivatedAlarm = _HzQtmRLSQueueBasedShutdownActivatedAlarm_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 7, 2, 29),
    _HzQtmRLSQueueBasedShutdownActivatedAlarm_Type()
)
hzQtmRLSQueueBasedShutdownActivatedAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzQtmRLSQueueBasedShutdownActivatedAlarm.setStatus("current")
_HzQtmRLSQueueBasedShutdownActivatedCounts_Type = Counter32
_HzQtmRLSQueueBasedShutdownActivatedCounts_Object = MibScalar
hzQtmRLSQueueBasedShutdownActivatedCounts = _HzQtmRLSQueueBasedShutdownActivatedCounts_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 7, 2, 30),
    _HzQtmRLSQueueBasedShutdownActivatedCounts_Type()
)
hzQtmRLSQueueBasedShutdownActivatedCounts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzQtmRLSQueueBasedShutdownActivatedCounts.setStatus("current")


class _HzQtmFpgaProgrammingErrorAlarm_Type(Integer32):
    """Custom type hzQtmFpgaProgrammingErrorAlarm based on Integer32"""
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


_HzQtmFpgaProgrammingErrorAlarm_Type.__name__ = "Integer32"
_HzQtmFpgaProgrammingErrorAlarm_Object = MibScalar
hzQtmFpgaProgrammingErrorAlarm = _HzQtmFpgaProgrammingErrorAlarm_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 7, 2, 31),
    _HzQtmFpgaProgrammingErrorAlarm_Type()
)
hzQtmFpgaProgrammingErrorAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzQtmFpgaProgrammingErrorAlarm.setStatus("current")
_HzQtmFpgaProgrammingErrorCounts_Type = Counter32
_HzQtmFpgaProgrammingErrorCounts_Object = MibScalar
hzQtmFpgaProgrammingErrorCounts = _HzQtmFpgaProgrammingErrorCounts_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 7, 2, 32),
    _HzQtmFpgaProgrammingErrorCounts_Type()
)
hzQtmFpgaProgrammingErrorCounts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzQtmFpgaProgrammingErrorCounts.setStatus("current")


class _HzQtmMibChangeNotSavedAlarm_Type(Integer32):
    """Custom type hzQtmMibChangeNotSavedAlarm based on Integer32"""
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


_HzQtmMibChangeNotSavedAlarm_Type.__name__ = "Integer32"
_HzQtmMibChangeNotSavedAlarm_Object = MibScalar
hzQtmMibChangeNotSavedAlarm = _HzQtmMibChangeNotSavedAlarm_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 7, 2, 33),
    _HzQtmMibChangeNotSavedAlarm_Type()
)
hzQtmMibChangeNotSavedAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzQtmMibChangeNotSavedAlarm.setStatus("current")
_HzQtmMibChangeNotSavedCounts_Type = Counter32
_HzQtmMibChangeNotSavedCounts_Object = MibScalar
hzQtmMibChangeNotSavedCounts = _HzQtmMibChangeNotSavedCounts_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 7, 2, 34),
    _HzQtmMibChangeNotSavedCounts_Type()
)
hzQtmMibChangeNotSavedCounts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzQtmMibChangeNotSavedCounts.setStatus("current")


class _HzQtmBadSystemConfigurationAlarm_Type(Integer32):
    """Custom type hzQtmBadSystemConfigurationAlarm based on Integer32"""
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


_HzQtmBadSystemConfigurationAlarm_Type.__name__ = "Integer32"
_HzQtmBadSystemConfigurationAlarm_Object = MibScalar
hzQtmBadSystemConfigurationAlarm = _HzQtmBadSystemConfigurationAlarm_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 7, 2, 35),
    _HzQtmBadSystemConfigurationAlarm_Type()
)
hzQtmBadSystemConfigurationAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzQtmBadSystemConfigurationAlarm.setStatus("current")
_HzQtmBadSystemConfigurationCounts_Type = Counter32
_HzQtmBadSystemConfigurationCounts_Object = MibScalar
hzQtmBadSystemConfigurationCounts = _HzQtmBadSystemConfigurationCounts_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 7, 2, 36),
    _HzQtmBadSystemConfigurationCounts_Type()
)
hzQtmBadSystemConfigurationCounts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzQtmBadSystemConfigurationCounts.setStatus("current")


class _HzQtmPartnerNodeAlarm_Type(Integer32):
    """Custom type hzQtmPartnerNodeAlarm based on Integer32"""
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


_HzQtmPartnerNodeAlarm_Type.__name__ = "Integer32"
_HzQtmPartnerNodeAlarm_Object = MibScalar
hzQtmPartnerNodeAlarm = _HzQtmPartnerNodeAlarm_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 7, 2, 37),
    _HzQtmPartnerNodeAlarm_Type()
)
hzQtmPartnerNodeAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzQtmPartnerNodeAlarm.setStatus("current")
_HzQtmPartnerNodeAlarmCounts_Type = Counter32
_HzQtmPartnerNodeAlarmCounts_Object = MibScalar
hzQtmPartnerNodeAlarmCounts = _HzQtmPartnerNodeAlarmCounts_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 7, 2, 38),
    _HzQtmPartnerNodeAlarmCounts_Type()
)
hzQtmPartnerNodeAlarmCounts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzQtmPartnerNodeAlarmCounts.setStatus("current")


class _HzQtmBandwidthDoublingInvalidLinkConfigAlarm_Type(Integer32):
    """Custom type hzQtmBandwidthDoublingInvalidLinkConfigAlarm based on Integer32"""
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


_HzQtmBandwidthDoublingInvalidLinkConfigAlarm_Type.__name__ = "Integer32"
_HzQtmBandwidthDoublingInvalidLinkConfigAlarm_Object = MibScalar
hzQtmBandwidthDoublingInvalidLinkConfigAlarm = _HzQtmBandwidthDoublingInvalidLinkConfigAlarm_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 7, 2, 39),
    _HzQtmBandwidthDoublingInvalidLinkConfigAlarm_Type()
)
hzQtmBandwidthDoublingInvalidLinkConfigAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzQtmBandwidthDoublingInvalidLinkConfigAlarm.setStatus("current")
_HzQtmBandwidthDoublingInvalidLinkConfigCounts_Type = Counter32
_HzQtmBandwidthDoublingInvalidLinkConfigCounts_Object = MibScalar
hzQtmBandwidthDoublingInvalidLinkConfigCounts = _HzQtmBandwidthDoublingInvalidLinkConfigCounts_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 7, 2, 40),
    _HzQtmBandwidthDoublingInvalidLinkConfigCounts_Type()
)
hzQtmBandwidthDoublingInvalidLinkConfigCounts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzQtmBandwidthDoublingInvalidLinkConfigCounts.setStatus("current")


class _HzQtmBandwidthDoublingWrongPortConnectedAlarm_Type(Integer32):
    """Custom type hzQtmBandwidthDoublingWrongPortConnectedAlarm based on Integer32"""
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


_HzQtmBandwidthDoublingWrongPortConnectedAlarm_Type.__name__ = "Integer32"
_HzQtmBandwidthDoublingWrongPortConnectedAlarm_Object = MibScalar
hzQtmBandwidthDoublingWrongPortConnectedAlarm = _HzQtmBandwidthDoublingWrongPortConnectedAlarm_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 7, 2, 41),
    _HzQtmBandwidthDoublingWrongPortConnectedAlarm_Type()
)
hzQtmBandwidthDoublingWrongPortConnectedAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzQtmBandwidthDoublingWrongPortConnectedAlarm.setStatus("current")
_HzQtmBandwidthDoublingWrongPortConnectedCount_Type = Counter32
_HzQtmBandwidthDoublingWrongPortConnectedCount_Object = MibScalar
hzQtmBandwidthDoublingWrongPortConnectedCount = _HzQtmBandwidthDoublingWrongPortConnectedCount_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 7, 2, 42),
    _HzQtmBandwidthDoublingWrongPortConnectedCount_Type()
)
hzQtmBandwidthDoublingWrongPortConnectedCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzQtmBandwidthDoublingWrongPortConnectedCount.setStatus("current")


class _HzQtmSynceLostLockAlarm_Type(Integer32):
    """Custom type hzQtmSynceLostLockAlarm based on Integer32"""
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


_HzQtmSynceLostLockAlarm_Type.__name__ = "Integer32"
_HzQtmSynceLostLockAlarm_Object = MibScalar
hzQtmSynceLostLockAlarm = _HzQtmSynceLostLockAlarm_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 7, 2, 43),
    _HzQtmSynceLostLockAlarm_Type()
)
hzQtmSynceLostLockAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzQtmSynceLostLockAlarm.setStatus("current")
_HzQtmSynceLostLockCount_Type = Counter32
_HzQtmSynceLostLockCount_Object = MibScalar
hzQtmSynceLostLockCount = _HzQtmSynceLostLockCount_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 7, 2, 44),
    _HzQtmSynceLostLockCount_Type()
)
hzQtmSynceLostLockCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzQtmSynceLostLockCount.setStatus("current")


class _HzQtmSynceSecondarySourceInUseAlarm_Type(Integer32):
    """Custom type hzQtmSynceSecondarySourceInUseAlarm based on Integer32"""
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


_HzQtmSynceSecondarySourceInUseAlarm_Type.__name__ = "Integer32"
_HzQtmSynceSecondarySourceInUseAlarm_Object = MibScalar
hzQtmSynceSecondarySourceInUseAlarm = _HzQtmSynceSecondarySourceInUseAlarm_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 7, 2, 45),
    _HzQtmSynceSecondarySourceInUseAlarm_Type()
)
hzQtmSynceSecondarySourceInUseAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzQtmSynceSecondarySourceInUseAlarm.setStatus("current")
_HzQtmSynceSecondarySourceInUseCount_Type = Counter32
_HzQtmSynceSecondarySourceInUseCount_Object = MibScalar
hzQtmSynceSecondarySourceInUseCount = _HzQtmSynceSecondarySourceInUseCount_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 7, 2, 46),
    _HzQtmSynceSecondarySourceInUseCount_Type()
)
hzQtmSynceSecondarySourceInUseCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzQtmSynceSecondarySourceInUseCount.setStatus("current")
_HzQtmNetworkInterfaceAlarms_ObjectIdentity = ObjectIdentity
hzQtmNetworkInterfaceAlarms = _HzQtmNetworkInterfaceAlarms_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 7, 3)
)
_HzQtmEnetPortAlarmsTable_Object = MibTable
hzQtmEnetPortAlarmsTable = _HzQtmEnetPortAlarmsTable_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 7, 3, 1)
)
if mibBuilder.loadTexts:
    hzQtmEnetPortAlarmsTable.setStatus("current")
_HzQtmEnetPortAlarmsEntry_Object = MibTableRow
hzQtmEnetPortAlarmsEntry = _HzQtmEnetPortAlarmsEntry_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 7, 3, 1, 1)
)
hzQtmEnetPortAlarmsEntry.setIndexNames(
    (0, "DRAGONWAVE-HORIZON-QUANTUM-MIB", "hzQtmEnetPortAlarmsIndex"),
)
if mibBuilder.loadTexts:
    hzQtmEnetPortAlarmsEntry.setStatus("current")


class _HzQtmEnetPortAlarmsIndex_Type(Integer32):
    """Custom type hzQtmEnetPortAlarmsIndex based on Integer32"""
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
        *(("enet-port-1", 1),
          ("enet-port-2", 2),
          ("enet-port-3", 3),
          ("enet-port-4", 4),
          ("enet-port-5", 5),
          ("enet-port-6", 6),
          ("enet-port-7", 7),
          ("enet-port-8", 8))
    )


_HzQtmEnetPortAlarmsIndex_Type.__name__ = "Integer32"
_HzQtmEnetPortAlarmsIndex_Object = MibTableColumn
hzQtmEnetPortAlarmsIndex = _HzQtmEnetPortAlarmsIndex_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 7, 3, 1, 1, 1),
    _HzQtmEnetPortAlarmsIndex_Type()
)
hzQtmEnetPortAlarmsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzQtmEnetPortAlarmsIndex.setStatus("current")


class _HzQtmEnetPortEthernetLinkDownAlarm_Type(Integer32):
    """Custom type hzQtmEnetPortEthernetLinkDownAlarm based on Integer32"""
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


_HzQtmEnetPortEthernetLinkDownAlarm_Type.__name__ = "Integer32"
_HzQtmEnetPortEthernetLinkDownAlarm_Object = MibTableColumn
hzQtmEnetPortEthernetLinkDownAlarm = _HzQtmEnetPortEthernetLinkDownAlarm_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 7, 3, 1, 1, 2),
    _HzQtmEnetPortEthernetLinkDownAlarm_Type()
)
hzQtmEnetPortEthernetLinkDownAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzQtmEnetPortEthernetLinkDownAlarm.setStatus("current")
_HzQtmEnetPortEthernetLinkDownCounts_Type = Counter32
_HzQtmEnetPortEthernetLinkDownCounts_Object = MibTableColumn
hzQtmEnetPortEthernetLinkDownCounts = _HzQtmEnetPortEthernetLinkDownCounts_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 7, 3, 1, 1, 3),
    _HzQtmEnetPortEthernetLinkDownCounts_Type()
)
hzQtmEnetPortEthernetLinkDownCounts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzQtmEnetPortEthernetLinkDownCounts.setStatus("current")
_HzQtmWirelessInterfaceAlarms_ObjectIdentity = ObjectIdentity
hzQtmWirelessInterfaceAlarms = _HzQtmWirelessInterfaceAlarms_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 7, 4)
)
_HzQtmModemAlarms_ObjectIdentity = ObjectIdentity
hzQtmModemAlarms = _HzQtmModemAlarms_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 7, 4, 1)
)
_HzQtmModemAlarmsTable_Object = MibTable
hzQtmModemAlarmsTable = _HzQtmModemAlarmsTable_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 7, 4, 1, 1)
)
if mibBuilder.loadTexts:
    hzQtmModemAlarmsTable.setStatus("current")
_HzQtmModemAlarmsEntry_Object = MibTableRow
hzQtmModemAlarmsEntry = _HzQtmModemAlarmsEntry_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 7, 4, 1, 1, 1)
)
hzQtmModemAlarmsEntry.setIndexNames(
    (0, "DRAGONWAVE-HORIZON-QUANTUM-MIB", "hzQtmModemAlarmsIndex"),
)
if mibBuilder.loadTexts:
    hzQtmModemAlarmsEntry.setStatus("current")


class _HzQtmModemAlarmsIndex_Type(Integer32):
    """Custom type hzQtmModemAlarmsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("wireless-port-1", 1),
          ("wireless-port-2", 2))
    )


_HzQtmModemAlarmsIndex_Type.__name__ = "Integer32"
_HzQtmModemAlarmsIndex_Object = MibTableColumn
hzQtmModemAlarmsIndex = _HzQtmModemAlarmsIndex_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 7, 4, 1, 1, 1, 1),
    _HzQtmModemAlarmsIndex_Type()
)
hzQtmModemAlarmsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzQtmModemAlarmsIndex.setStatus("current")


class _HzQtmModemRxLossOfSignalAlarm_Type(Integer32):
    """Custom type hzQtmModemRxLossOfSignalAlarm based on Integer32"""
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


_HzQtmModemRxLossOfSignalAlarm_Type.__name__ = "Integer32"
_HzQtmModemRxLossOfSignalAlarm_Object = MibTableColumn
hzQtmModemRxLossOfSignalAlarm = _HzQtmModemRxLossOfSignalAlarm_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 7, 4, 1, 1, 1, 2),
    _HzQtmModemRxLossOfSignalAlarm_Type()
)
hzQtmModemRxLossOfSignalAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzQtmModemRxLossOfSignalAlarm.setStatus("current")
_HzQtmModemRxLossOfSignalCounts_Type = Counter32
_HzQtmModemRxLossOfSignalCounts_Object = MibTableColumn
hzQtmModemRxLossOfSignalCounts = _HzQtmModemRxLossOfSignalCounts_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 7, 4, 1, 1, 1, 3),
    _HzQtmModemRxLossOfSignalCounts_Type()
)
hzQtmModemRxLossOfSignalCounts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzQtmModemRxLossOfSignalCounts.setStatus("current")


class _HzQtmModemTxLossOfSyncAlarm_Type(Integer32):
    """Custom type hzQtmModemTxLossOfSyncAlarm based on Integer32"""
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


_HzQtmModemTxLossOfSyncAlarm_Type.__name__ = "Integer32"
_HzQtmModemTxLossOfSyncAlarm_Object = MibTableColumn
hzQtmModemTxLossOfSyncAlarm = _HzQtmModemTxLossOfSyncAlarm_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 7, 4, 1, 1, 1, 4),
    _HzQtmModemTxLossOfSyncAlarm_Type()
)
hzQtmModemTxLossOfSyncAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzQtmModemTxLossOfSyncAlarm.setStatus("current")
_HzQtmModemTxLossOfSyncCounts_Type = Counter32
_HzQtmModemTxLossOfSyncCounts_Object = MibTableColumn
hzQtmModemTxLossOfSyncCounts = _HzQtmModemTxLossOfSyncCounts_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 7, 4, 1, 1, 1, 5),
    _HzQtmModemTxLossOfSyncCounts_Type()
)
hzQtmModemTxLossOfSyncCounts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzQtmModemTxLossOfSyncCounts.setStatus("current")


class _HzQtmModemSnrBelowThresholdAlarm_Type(Integer32):
    """Custom type hzQtmModemSnrBelowThresholdAlarm based on Integer32"""
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


_HzQtmModemSnrBelowThresholdAlarm_Type.__name__ = "Integer32"
_HzQtmModemSnrBelowThresholdAlarm_Object = MibTableColumn
hzQtmModemSnrBelowThresholdAlarm = _HzQtmModemSnrBelowThresholdAlarm_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 7, 4, 1, 1, 1, 6),
    _HzQtmModemSnrBelowThresholdAlarm_Type()
)
hzQtmModemSnrBelowThresholdAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzQtmModemSnrBelowThresholdAlarm.setStatus("current")
_HzQtmModemSnrBelowThresholdCounts_Type = Counter32
_HzQtmModemSnrBelowThresholdCounts_Object = MibTableColumn
hzQtmModemSnrBelowThresholdCounts = _HzQtmModemSnrBelowThresholdCounts_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 7, 4, 1, 1, 1, 7),
    _HzQtmModemSnrBelowThresholdCounts_Type()
)
hzQtmModemSnrBelowThresholdCounts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzQtmModemSnrBelowThresholdCounts.setStatus("current")


class _HzQtmModemEqualizerStressExceedThresholdAlarm_Type(Integer32):
    """Custom type hzQtmModemEqualizerStressExceedThresholdAlarm based on Integer32"""
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


_HzQtmModemEqualizerStressExceedThresholdAlarm_Type.__name__ = "Integer32"
_HzQtmModemEqualizerStressExceedThresholdAlarm_Object = MibTableColumn
hzQtmModemEqualizerStressExceedThresholdAlarm = _HzQtmModemEqualizerStressExceedThresholdAlarm_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 7, 4, 1, 1, 1, 8),
    _HzQtmModemEqualizerStressExceedThresholdAlarm_Type()
)
hzQtmModemEqualizerStressExceedThresholdAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzQtmModemEqualizerStressExceedThresholdAlarm.setStatus("current")
_HzQtmModemEquilizerStressExceedThresholdCounts_Type = Counter32
_HzQtmModemEquilizerStressExceedThresholdCounts_Object = MibTableColumn
hzQtmModemEquilizerStressExceedThresholdCounts = _HzQtmModemEquilizerStressExceedThresholdCounts_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 7, 4, 1, 1, 1, 9),
    _HzQtmModemEquilizerStressExceedThresholdCounts_Type()
)
hzQtmModemEquilizerStressExceedThresholdCounts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzQtmModemEquilizerStressExceedThresholdCounts.setStatus("current")


class _HzQtmModemRLSShutdownActivatedAlarm_Type(Integer32):
    """Custom type hzQtmModemRLSShutdownActivatedAlarm based on Integer32"""
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


_HzQtmModemRLSShutdownActivatedAlarm_Type.__name__ = "Integer32"
_HzQtmModemRLSShutdownActivatedAlarm_Object = MibTableColumn
hzQtmModemRLSShutdownActivatedAlarm = _HzQtmModemRLSShutdownActivatedAlarm_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 7, 4, 1, 1, 1, 10),
    _HzQtmModemRLSShutdownActivatedAlarm_Type()
)
hzQtmModemRLSShutdownActivatedAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzQtmModemRLSShutdownActivatedAlarm.setStatus("current")
_HzQtmModemRLSShutdownActivatedCounts_Type = Counter32
_HzQtmModemRLSShutdownActivatedCounts_Object = MibTableColumn
hzQtmModemRLSShutdownActivatedCounts = _HzQtmModemRLSShutdownActivatedCounts_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 7, 4, 1, 1, 1, 11),
    _HzQtmModemRLSShutdownActivatedCounts_Type()
)
hzQtmModemRLSShutdownActivatedCounts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzQtmModemRLSShutdownActivatedCounts.setStatus("current")


class _HzQtmModemXPICEquStressExceedThresholdAlarm_Type(Integer32):
    """Custom type hzQtmModemXPICEquStressExceedThresholdAlarm based on Integer32"""
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


_HzQtmModemXPICEquStressExceedThresholdAlarm_Type.__name__ = "Integer32"
_HzQtmModemXPICEquStressExceedThresholdAlarm_Object = MibTableColumn
hzQtmModemXPICEquStressExceedThresholdAlarm = _HzQtmModemXPICEquStressExceedThresholdAlarm_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 7, 4, 1, 1, 1, 12),
    _HzQtmModemXPICEquStressExceedThresholdAlarm_Type()
)
hzQtmModemXPICEquStressExceedThresholdAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzQtmModemXPICEquStressExceedThresholdAlarm.setStatus("current")
_HzQtmModemXPICEquStressExceedThresholdCounts_Type = Counter32
_HzQtmModemXPICEquStressExceedThresholdCounts_Object = MibTableColumn
hzQtmModemXPICEquStressExceedThresholdCounts = _HzQtmModemXPICEquStressExceedThresholdCounts_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 7, 4, 1, 1, 1, 13),
    _HzQtmModemXPICEquStressExceedThresholdCounts_Type()
)
hzQtmModemXPICEquStressExceedThresholdCounts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzQtmModemXPICEquStressExceedThresholdCounts.setStatus("current")
_HzQtmRadioAlarms_ObjectIdentity = ObjectIdentity
hzQtmRadioAlarms = _HzQtmRadioAlarms_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 7, 4, 2)
)
_HzQtmRadioAlarmsTable_Object = MibTable
hzQtmRadioAlarmsTable = _HzQtmRadioAlarmsTable_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 7, 4, 2, 1)
)
if mibBuilder.loadTexts:
    hzQtmRadioAlarmsTable.setStatus("current")
_HzQtmRadioAlarmsEntry_Object = MibTableRow
hzQtmRadioAlarmsEntry = _HzQtmRadioAlarmsEntry_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 7, 4, 2, 1, 1)
)
hzQtmRadioAlarmsEntry.setIndexNames(
    (0, "DRAGONWAVE-HORIZON-QUANTUM-MIB", "hzQtmRadioAlarmsIndex"),
)
if mibBuilder.loadTexts:
    hzQtmRadioAlarmsEntry.setStatus("current")


class _HzQtmRadioAlarmsIndex_Type(Integer32):
    """Custom type hzQtmRadioAlarmsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("wireless-port-1", 1),
          ("wireless-port-2", 2))
    )


_HzQtmRadioAlarmsIndex_Type.__name__ = "Integer32"
_HzQtmRadioAlarmsIndex_Object = MibTableColumn
hzQtmRadioAlarmsIndex = _HzQtmRadioAlarmsIndex_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 7, 4, 2, 1, 1, 1),
    _HzQtmRadioAlarmsIndex_Type()
)
hzQtmRadioAlarmsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzQtmRadioAlarmsIndex.setStatus("current")


class _HzQtmRadioSynthLostLockAlarm_Type(Integer32):
    """Custom type hzQtmRadioSynthLostLockAlarm based on Integer32"""
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


_HzQtmRadioSynthLostLockAlarm_Type.__name__ = "Integer32"
_HzQtmRadioSynthLostLockAlarm_Object = MibTableColumn
hzQtmRadioSynthLostLockAlarm = _HzQtmRadioSynthLostLockAlarm_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 7, 4, 2, 1, 1, 2),
    _HzQtmRadioSynthLostLockAlarm_Type()
)
hzQtmRadioSynthLostLockAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzQtmRadioSynthLostLockAlarm.setStatus("current")
_HzQtmRadioSynthLostLockCounts_Type = Counter32
_HzQtmRadioSynthLostLockCounts_Object = MibTableColumn
hzQtmRadioSynthLostLockCounts = _HzQtmRadioSynthLostLockCounts_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 7, 4, 2, 1, 1, 3),
    _HzQtmRadioSynthLostLockCounts_Type()
)
hzQtmRadioSynthLostLockCounts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzQtmRadioSynthLostLockCounts.setStatus("current")


class _HzQtmRadioLostCommunicationAlarm_Type(Integer32):
    """Custom type hzQtmRadioLostCommunicationAlarm based on Integer32"""
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


_HzQtmRadioLostCommunicationAlarm_Type.__name__ = "Integer32"
_HzQtmRadioLostCommunicationAlarm_Object = MibTableColumn
hzQtmRadioLostCommunicationAlarm = _HzQtmRadioLostCommunicationAlarm_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 7, 4, 2, 1, 1, 4),
    _HzQtmRadioLostCommunicationAlarm_Type()
)
hzQtmRadioLostCommunicationAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzQtmRadioLostCommunicationAlarm.setStatus("current")
_HzQtmRadioLostCommunicationCounts_Type = Counter32
_HzQtmRadioLostCommunicationCounts_Object = MibTableColumn
hzQtmRadioLostCommunicationCounts = _HzQtmRadioLostCommunicationCounts_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 7, 4, 2, 1, 1, 5),
    _HzQtmRadioLostCommunicationCounts_Type()
)
hzQtmRadioLostCommunicationCounts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzQtmRadioLostCommunicationCounts.setStatus("current")


class _HzQtmRadioMismatchAlarm_Type(Integer32):
    """Custom type hzQtmRadioMismatchAlarm based on Integer32"""
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


_HzQtmRadioMismatchAlarm_Type.__name__ = "Integer32"
_HzQtmRadioMismatchAlarm_Object = MibTableColumn
hzQtmRadioMismatchAlarm = _HzQtmRadioMismatchAlarm_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 7, 4, 2, 1, 1, 6),
    _HzQtmRadioMismatchAlarm_Type()
)
hzQtmRadioMismatchAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzQtmRadioMismatchAlarm.setStatus("current")
_HzQtmRadioMismatchCounts_Type = Counter32
_HzQtmRadioMismatchCounts_Object = MibTableColumn
hzQtmRadioMismatchCounts = _HzQtmRadioMismatchCounts_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 7, 4, 2, 1, 1, 7),
    _HzQtmRadioMismatchCounts_Type()
)
hzQtmRadioMismatchCounts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzQtmRadioMismatchCounts.setStatus("current")


class _HzQtmRadioPowerAmpAlarm_Type(Integer32):
    """Custom type hzQtmRadioPowerAmpAlarm based on Integer32"""
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


_HzQtmRadioPowerAmpAlarm_Type.__name__ = "Integer32"
_HzQtmRadioPowerAmpAlarm_Object = MibTableColumn
hzQtmRadioPowerAmpAlarm = _HzQtmRadioPowerAmpAlarm_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 7, 4, 2, 1, 1, 8),
    _HzQtmRadioPowerAmpAlarm_Type()
)
hzQtmRadioPowerAmpAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzQtmRadioPowerAmpAlarm.setStatus("current")
_HzQtmRadioPowerAmpCounts_Type = Counter32
_HzQtmRadioPowerAmpCounts_Object = MibTableColumn
hzQtmRadioPowerAmpCounts = _HzQtmRadioPowerAmpCounts_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 7, 4, 2, 1, 1, 9),
    _HzQtmRadioPowerAmpCounts_Type()
)
hzQtmRadioPowerAmpCounts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzQtmRadioPowerAmpCounts.setStatus("current")


class _HzQtmRadioExcessiveTxCableLossAlarm_Type(Integer32):
    """Custom type hzQtmRadioExcessiveTxCableLossAlarm based on Integer32"""
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


_HzQtmRadioExcessiveTxCableLossAlarm_Type.__name__ = "Integer32"
_HzQtmRadioExcessiveTxCableLossAlarm_Object = MibTableColumn
hzQtmRadioExcessiveTxCableLossAlarm = _HzQtmRadioExcessiveTxCableLossAlarm_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 7, 4, 2, 1, 1, 10),
    _HzQtmRadioExcessiveTxCableLossAlarm_Type()
)
hzQtmRadioExcessiveTxCableLossAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzQtmRadioExcessiveTxCableLossAlarm.setStatus("current")
_HzQtmRadioExcessiveTxCableLossCounts_Type = Counter32
_HzQtmRadioExcessiveTxCableLossCounts_Object = MibTableColumn
hzQtmRadioExcessiveTxCableLossCounts = _HzQtmRadioExcessiveTxCableLossCounts_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 7, 4, 2, 1, 1, 11),
    _HzQtmRadioExcessiveTxCableLossCounts_Type()
)
hzQtmRadioExcessiveTxCableLossCounts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzQtmRadioExcessiveTxCableLossCounts.setStatus("current")


class _HzQtmRadioRslBelowThresholdAlarm_Type(Integer32):
    """Custom type hzQtmRadioRslBelowThresholdAlarm based on Integer32"""
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


_HzQtmRadioRslBelowThresholdAlarm_Type.__name__ = "Integer32"
_HzQtmRadioRslBelowThresholdAlarm_Object = MibTableColumn
hzQtmRadioRslBelowThresholdAlarm = _HzQtmRadioRslBelowThresholdAlarm_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 7, 4, 2, 1, 1, 12),
    _HzQtmRadioRslBelowThresholdAlarm_Type()
)
hzQtmRadioRslBelowThresholdAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzQtmRadioRslBelowThresholdAlarm.setStatus("current")
_HzQtmRadioRslBelowThresholdCounts_Type = Counter32
_HzQtmRadioRslBelowThresholdCounts_Object = MibTableColumn
hzQtmRadioRslBelowThresholdCounts = _HzQtmRadioRslBelowThresholdCounts_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 7, 4, 2, 1, 1, 13),
    _HzQtmRadioRslBelowThresholdCounts_Type()
)
hzQtmRadioRslBelowThresholdCounts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzQtmRadioRslBelowThresholdCounts.setStatus("current")


class _HzQtmRadioHighPowerTxDetectorAlarm_Type(Integer32):
    """Custom type hzQtmRadioHighPowerTxDetectorAlarm based on Integer32"""
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


_HzQtmRadioHighPowerTxDetectorAlarm_Type.__name__ = "Integer32"
_HzQtmRadioHighPowerTxDetectorAlarm_Object = MibTableColumn
hzQtmRadioHighPowerTxDetectorAlarm = _HzQtmRadioHighPowerTxDetectorAlarm_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 7, 4, 2, 1, 1, 14),
    _HzQtmRadioHighPowerTxDetectorAlarm_Type()
)
hzQtmRadioHighPowerTxDetectorAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzQtmRadioHighPowerTxDetectorAlarm.setStatus("current")
_HzQtmRadioHighPowerTxDetectorCounts_Type = Counter32
_HzQtmRadioHighPowerTxDetectorCounts_Object = MibTableColumn
hzQtmRadioHighPowerTxDetectorCounts = _HzQtmRadioHighPowerTxDetectorCounts_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 7, 4, 2, 1, 1, 15),
    _HzQtmRadioHighPowerTxDetectorCounts_Type()
)
hzQtmRadioHighPowerTxDetectorCounts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzQtmRadioHighPowerTxDetectorCounts.setStatus("current")


class _HzQtmRadioRedundancySerialNumMismatchAlarm_Type(Integer32):
    """Custom type hzQtmRadioRedundancySerialNumMismatchAlarm based on Integer32"""
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


_HzQtmRadioRedundancySerialNumMismatchAlarm_Type.__name__ = "Integer32"
_HzQtmRadioRedundancySerialNumMismatchAlarm_Object = MibTableColumn
hzQtmRadioRedundancySerialNumMismatchAlarm = _HzQtmRadioRedundancySerialNumMismatchAlarm_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 7, 4, 2, 1, 1, 16),
    _HzQtmRadioRedundancySerialNumMismatchAlarm_Type()
)
hzQtmRadioRedundancySerialNumMismatchAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzQtmRadioRedundancySerialNumMismatchAlarm.setStatus("current")
_HzQtmRadioRedundancySerialNumMismatchCounts_Type = Counter32
_HzQtmRadioRedundancySerialNumMismatchCounts_Object = MibTableColumn
hzQtmRadioRedundancySerialNumMismatchCounts = _HzQtmRadioRedundancySerialNumMismatchCounts_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 7, 4, 2, 1, 1, 17),
    _HzQtmRadioRedundancySerialNumMismatchCounts_Type()
)
hzQtmRadioRedundancySerialNumMismatchCounts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzQtmRadioRedundancySerialNumMismatchCounts.setStatus("current")


class _HzQtmRadioExcessiveTxCableLossChangeAlarm_Type(Integer32):
    """Custom type hzQtmRadioExcessiveTxCableLossChangeAlarm based on Integer32"""
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


_HzQtmRadioExcessiveTxCableLossChangeAlarm_Type.__name__ = "Integer32"
_HzQtmRadioExcessiveTxCableLossChangeAlarm_Object = MibTableColumn
hzQtmRadioExcessiveTxCableLossChangeAlarm = _HzQtmRadioExcessiveTxCableLossChangeAlarm_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 7, 4, 2, 1, 1, 18),
    _HzQtmRadioExcessiveTxCableLossChangeAlarm_Type()
)
hzQtmRadioExcessiveTxCableLossChangeAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzQtmRadioExcessiveTxCableLossChangeAlarm.setStatus("current")
_HzQtmRadioExcessiveTxCableLossChangeCounts_Type = Counter32
_HzQtmRadioExcessiveTxCableLossChangeCounts_Object = MibTableColumn
hzQtmRadioExcessiveTxCableLossChangeCounts = _HzQtmRadioExcessiveTxCableLossChangeCounts_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 7, 4, 2, 1, 1, 19),
    _HzQtmRadioExcessiveTxCableLossChangeCounts_Type()
)
hzQtmRadioExcessiveTxCableLossChangeCounts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzQtmRadioExcessiveTxCableLossChangeCounts.setStatus("current")


class _HzQtmRadioExcessiveRxCableLossAlarm_Type(Integer32):
    """Custom type hzQtmRadioExcessiveRxCableLossAlarm based on Integer32"""
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


_HzQtmRadioExcessiveRxCableLossAlarm_Type.__name__ = "Integer32"
_HzQtmRadioExcessiveRxCableLossAlarm_Object = MibTableColumn
hzQtmRadioExcessiveRxCableLossAlarm = _HzQtmRadioExcessiveRxCableLossAlarm_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 7, 4, 2, 1, 1, 20),
    _HzQtmRadioExcessiveRxCableLossAlarm_Type()
)
hzQtmRadioExcessiveRxCableLossAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzQtmRadioExcessiveRxCableLossAlarm.setStatus("current")
_HzQtmRadioExcessiveRxCableLossCounts_Type = Counter32
_HzQtmRadioExcessiveRxCableLossCounts_Object = MibTableColumn
hzQtmRadioExcessiveRxCableLossCounts = _HzQtmRadioExcessiveRxCableLossCounts_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 7, 4, 2, 1, 1, 21),
    _HzQtmRadioExcessiveRxCableLossCounts_Type()
)
hzQtmRadioExcessiveRxCableLossCounts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzQtmRadioExcessiveRxCableLossCounts.setStatus("current")


class _HzQtmRadioAtpcTxAtMaxPowerAlarm_Type(Integer32):
    """Custom type hzQtmRadioAtpcTxAtMaxPowerAlarm based on Integer32"""
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


_HzQtmRadioAtpcTxAtMaxPowerAlarm_Type.__name__ = "Integer32"
_HzQtmRadioAtpcTxAtMaxPowerAlarm_Object = MibTableColumn
hzQtmRadioAtpcTxAtMaxPowerAlarm = _HzQtmRadioAtpcTxAtMaxPowerAlarm_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 7, 4, 2, 1, 1, 22),
    _HzQtmRadioAtpcTxAtMaxPowerAlarm_Type()
)
hzQtmRadioAtpcTxAtMaxPowerAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzQtmRadioAtpcTxAtMaxPowerAlarm.setStatus("current")
_HzQtmRadioAtpcTxAtMaxPowerCounts_Type = Counter32
_HzQtmRadioAtpcTxAtMaxPowerCounts_Object = MibTableColumn
hzQtmRadioAtpcTxAtMaxPowerCounts = _HzQtmRadioAtpcTxAtMaxPowerCounts_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 7, 4, 2, 1, 1, 23),
    _HzQtmRadioAtpcTxAtMaxPowerCounts_Type()
)
hzQtmRadioAtpcTxAtMaxPowerCounts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzQtmRadioAtpcTxAtMaxPowerCounts.setStatus("current")


class _HzQtmRadioSwDownloadFailedAlarm_Type(Integer32):
    """Custom type hzQtmRadioSwDownloadFailedAlarm based on Integer32"""
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


_HzQtmRadioSwDownloadFailedAlarm_Type.__name__ = "Integer32"
_HzQtmRadioSwDownloadFailedAlarm_Object = MibTableColumn
hzQtmRadioSwDownloadFailedAlarm = _HzQtmRadioSwDownloadFailedAlarm_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 7, 4, 2, 1, 1, 24),
    _HzQtmRadioSwDownloadFailedAlarm_Type()
)
hzQtmRadioSwDownloadFailedAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzQtmRadioSwDownloadFailedAlarm.setStatus("current")
_HzQtmRadioSwDownloadFailedCounts_Type = Counter32
_HzQtmRadioSwDownloadFailedCounts_Object = MibTableColumn
hzQtmRadioSwDownloadFailedCounts = _HzQtmRadioSwDownloadFailedCounts_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 7, 4, 2, 1, 1, 25),
    _HzQtmRadioSwDownloadFailedCounts_Type()
)
hzQtmRadioSwDownloadFailedCounts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzQtmRadioSwDownloadFailedCounts.setStatus("current")


class _HzQtmRadioDrainCurrentAlarm_Type(Integer32):
    """Custom type hzQtmRadioDrainCurrentAlarm based on Integer32"""
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


_HzQtmRadioDrainCurrentAlarm_Type.__name__ = "Integer32"
_HzQtmRadioDrainCurrentAlarm_Object = MibTableColumn
hzQtmRadioDrainCurrentAlarm = _HzQtmRadioDrainCurrentAlarm_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 7, 4, 2, 1, 1, 26),
    _HzQtmRadioDrainCurrentAlarm_Type()
)
hzQtmRadioDrainCurrentAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzQtmRadioDrainCurrentAlarm.setStatus("current")
_HzQtmRadioDrainCurrentCounts_Type = Counter32
_HzQtmRadioDrainCurrentCounts_Object = MibTableColumn
hzQtmRadioDrainCurrentCounts = _HzQtmRadioDrainCurrentCounts_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 7, 4, 2, 1, 1, 27),
    _HzQtmRadioDrainCurrentCounts_Type()
)
hzQtmRadioDrainCurrentCounts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzQtmRadioDrainCurrentCounts.setStatus("current")


class _HzQtmRadioPowerOffAlarm_Type(Integer32):
    """Custom type hzQtmRadioPowerOffAlarm based on Integer32"""
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


_HzQtmRadioPowerOffAlarm_Type.__name__ = "Integer32"
_HzQtmRadioPowerOffAlarm_Object = MibTableColumn
hzQtmRadioPowerOffAlarm = _HzQtmRadioPowerOffAlarm_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 7, 4, 2, 1, 1, 28),
    _HzQtmRadioPowerOffAlarm_Type()
)
hzQtmRadioPowerOffAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzQtmRadioPowerOffAlarm.setStatus("current")
_HzQtmRadioPowerOffCounts_Type = Counter32
_HzQtmRadioPowerOffCounts_Object = MibTableColumn
hzQtmRadioPowerOffCounts = _HzQtmRadioPowerOffCounts_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 7, 4, 2, 1, 1, 29),
    _HzQtmRadioPowerOffCounts_Type()
)
hzQtmRadioPowerOffCounts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzQtmRadioPowerOffCounts.setStatus("current")
_HzQtmIFAlarms_ObjectIdentity = ObjectIdentity
hzQtmIFAlarms = _HzQtmIFAlarms_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 7, 4, 3)
)
_HzQtmIFAlarmsTable_Object = MibTable
hzQtmIFAlarmsTable = _HzQtmIFAlarmsTable_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 7, 4, 3, 1)
)
if mibBuilder.loadTexts:
    hzQtmIFAlarmsTable.setStatus("current")
_HzQtmIFAlarmsEntry_Object = MibTableRow
hzQtmIFAlarmsEntry = _HzQtmIFAlarmsEntry_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 7, 4, 3, 1, 1)
)
hzQtmIFAlarmsEntry.setIndexNames(
    (0, "DRAGONWAVE-HORIZON-QUANTUM-MIB", "hzQtmIFAlarmsIndex"),
)
if mibBuilder.loadTexts:
    hzQtmIFAlarmsEntry.setStatus("current")


class _HzQtmIFAlarmsIndex_Type(Integer32):
    """Custom type hzQtmIFAlarmsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("wireless-path-1", 1),
          ("wireless-path-2", 2))
    )


_HzQtmIFAlarmsIndex_Type.__name__ = "Integer32"
_HzQtmIFAlarmsIndex_Object = MibTableColumn
hzQtmIFAlarmsIndex = _HzQtmIFAlarmsIndex_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 7, 4, 3, 1, 1, 1),
    _HzQtmIFAlarmsIndex_Type()
)
hzQtmIFAlarmsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzQtmIFAlarmsIndex.setStatus("current")


class _HzQtmIFLostLockAlarm_Type(Integer32):
    """Custom type hzQtmIFLostLockAlarm based on Integer32"""
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


_HzQtmIFLostLockAlarm_Type.__name__ = "Integer32"
_HzQtmIFLostLockAlarm_Object = MibTableColumn
hzQtmIFLostLockAlarm = _HzQtmIFLostLockAlarm_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 7, 4, 3, 1, 1, 2),
    _HzQtmIFLostLockAlarm_Type()
)
hzQtmIFLostLockAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzQtmIFLostLockAlarm.setStatus("current")
_HzQtmIFLostLockCounts_Type = Counter32
_HzQtmIFLostLockCounts_Object = MibTableColumn
hzQtmIFLostLockCounts = _HzQtmIFLostLockCounts_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 7, 4, 3, 1, 1, 3),
    _HzQtmIFLostLockCounts_Type()
)
hzQtmIFLostLockCounts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzQtmIFLostLockCounts.setStatus("current")
_HzQtmTrapConfig_ObjectIdentity = ObjectIdentity
hzQtmTrapConfig = _HzQtmTrapConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 8)
)
_HzQtmSnmpTrapHostTable_Object = MibTable
hzQtmSnmpTrapHostTable = _HzQtmSnmpTrapHostTable_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 8, 1)
)
if mibBuilder.loadTexts:
    hzQtmSnmpTrapHostTable.setStatus("current")
_HzQtmSnmpTrapHostEntry_Object = MibTableRow
hzQtmSnmpTrapHostEntry = _HzQtmSnmpTrapHostEntry_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 8, 1, 1)
)
hzQtmSnmpTrapHostEntry.setIndexNames(
    (0, "DRAGONWAVE-HORIZON-QUANTUM-MIB", "hzQtmSnmpTrapHostIndex"),
)
if mibBuilder.loadTexts:
    hzQtmSnmpTrapHostEntry.setStatus("current")
_HzQtmSnmpTrapHostIndex_Type = Integer32
_HzQtmSnmpTrapHostIndex_Object = MibTableColumn
hzQtmSnmpTrapHostIndex = _HzQtmSnmpTrapHostIndex_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 8, 1, 1, 1),
    _HzQtmSnmpTrapHostIndex_Type()
)
hzQtmSnmpTrapHostIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzQtmSnmpTrapHostIndex.setStatus("current")


class _HzQtmSnmpTrapHostMode_Type(Integer32):
    """Custom type hzQtmSnmpTrapHostMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("static", 1),
          ("dns", 2))
    )


_HzQtmSnmpTrapHostMode_Type.__name__ = "Integer32"
_HzQtmSnmpTrapHostMode_Object = MibTableColumn
hzQtmSnmpTrapHostMode = _HzQtmSnmpTrapHostMode_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 8, 1, 1, 2),
    _HzQtmSnmpTrapHostMode_Type()
)
hzQtmSnmpTrapHostMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzQtmSnmpTrapHostMode.setStatus("current")
_HzQtmSnmpTrapHostIpAddress_Type = IpAddress
_HzQtmSnmpTrapHostIpAddress_Object = MibTableColumn
hzQtmSnmpTrapHostIpAddress = _HzQtmSnmpTrapHostIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 8, 1, 1, 3),
    _HzQtmSnmpTrapHostIpAddress_Type()
)
hzQtmSnmpTrapHostIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzQtmSnmpTrapHostIpAddress.setStatus("current")


class _HzQtmSnmpTrapHostCommunityName_Type(DisplayString):
    """Custom type hzQtmSnmpTrapHostCommunityName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 24),
    )


_HzQtmSnmpTrapHostCommunityName_Type.__name__ = "DisplayString"
_HzQtmSnmpTrapHostCommunityName_Object = MibTableColumn
hzQtmSnmpTrapHostCommunityName = _HzQtmSnmpTrapHostCommunityName_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 8, 1, 1, 4),
    _HzQtmSnmpTrapHostCommunityName_Type()
)
hzQtmSnmpTrapHostCommunityName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzQtmSnmpTrapHostCommunityName.setStatus("current")


class _HzQtmSnmpTrapHostActivated_Type(Integer32):
    """Custom type hzQtmSnmpTrapHostActivated based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notActive", 1),
          ("active", 2))
    )


_HzQtmSnmpTrapHostActivated_Type.__name__ = "Integer32"
_HzQtmSnmpTrapHostActivated_Object = MibTableColumn
hzQtmSnmpTrapHostActivated = _HzQtmSnmpTrapHostActivated_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 8, 1, 1, 5),
    _HzQtmSnmpTrapHostActivated_Type()
)
hzQtmSnmpTrapHostActivated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzQtmSnmpTrapHostActivated.setStatus("current")
_HzQtmSnmpV3TrapHostsTable_Object = MibTable
hzQtmSnmpV3TrapHostsTable = _HzQtmSnmpV3TrapHostsTable_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 8, 2)
)
if mibBuilder.loadTexts:
    hzQtmSnmpV3TrapHostsTable.setStatus("current")
_HzQtmSnmpV3TrapHostsEntry_Object = MibTableRow
hzQtmSnmpV3TrapHostsEntry = _HzQtmSnmpV3TrapHostsEntry_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 8, 2, 1)
)
hzQtmSnmpV3TrapHostsEntry.setIndexNames(
    (0, "DRAGONWAVE-HORIZON-QUANTUM-MIB", "hzQtmSnmpV3TrapHostsIndex"),
)
if mibBuilder.loadTexts:
    hzQtmSnmpV3TrapHostsEntry.setStatus("current")


class _HzQtmSnmpV3TrapHostsIndex_Type(Integer32):
    """Custom type hzQtmSnmpV3TrapHostsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4),
    )


_HzQtmSnmpV3TrapHostsIndex_Type.__name__ = "Integer32"
_HzQtmSnmpV3TrapHostsIndex_Object = MibTableColumn
hzQtmSnmpV3TrapHostsIndex = _HzQtmSnmpV3TrapHostsIndex_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 8, 2, 1, 1),
    _HzQtmSnmpV3TrapHostsIndex_Type()
)
hzQtmSnmpV3TrapHostsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzQtmSnmpV3TrapHostsIndex.setStatus("current")
_SnmpV3TrapHostIpAddress_Type = IpAddress
_SnmpV3TrapHostIpAddress_Object = MibTableColumn
snmpV3TrapHostIpAddress = _SnmpV3TrapHostIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 8, 2, 1, 2),
    _SnmpV3TrapHostIpAddress_Type()
)
snmpV3TrapHostIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmpV3TrapHostIpAddress.setStatus("current")


class _SnmpV3TrapHostUserName_Type(DisplayString):
    """Custom type snmpV3TrapHostUserName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 24),
    )


_SnmpV3TrapHostUserName_Type.__name__ = "DisplayString"
_SnmpV3TrapHostUserName_Object = MibTableColumn
snmpV3TrapHostUserName = _SnmpV3TrapHostUserName_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 8, 2, 1, 3),
    _SnmpV3TrapHostUserName_Type()
)
snmpV3TrapHostUserName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmpV3TrapHostUserName.setStatus("current")


class _SnmpV3TrapHostAuthProtocol_Type(Integer32):
    """Custom type snmpV3TrapHostAuthProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("noAuth", 1),
          ("md5", 2),
          ("sha", 3))
    )


_SnmpV3TrapHostAuthProtocol_Type.__name__ = "Integer32"
_SnmpV3TrapHostAuthProtocol_Object = MibTableColumn
snmpV3TrapHostAuthProtocol = _SnmpV3TrapHostAuthProtocol_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 8, 2, 1, 4),
    _SnmpV3TrapHostAuthProtocol_Type()
)
snmpV3TrapHostAuthProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmpV3TrapHostAuthProtocol.setStatus("current")


class _SnmpV3TrapHostAuthPassword_Type(DisplayString):
    """Custom type snmpV3TrapHostAuthPassword based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 24),
    )


_SnmpV3TrapHostAuthPassword_Type.__name__ = "DisplayString"
_SnmpV3TrapHostAuthPassword_Object = MibTableColumn
snmpV3TrapHostAuthPassword = _SnmpV3TrapHostAuthPassword_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 8, 2, 1, 5),
    _SnmpV3TrapHostAuthPassword_Type()
)
snmpV3TrapHostAuthPassword.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmpV3TrapHostAuthPassword.setStatus("current")


class _SnmpV3TrapHostPrivProtocol_Type(Integer32):
    """Custom type snmpV3TrapHostPrivProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noPriv", 1),
          ("des", 2))
    )


_SnmpV3TrapHostPrivProtocol_Type.__name__ = "Integer32"
_SnmpV3TrapHostPrivProtocol_Object = MibTableColumn
snmpV3TrapHostPrivProtocol = _SnmpV3TrapHostPrivProtocol_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 8, 2, 1, 6),
    _SnmpV3TrapHostPrivProtocol_Type()
)
snmpV3TrapHostPrivProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmpV3TrapHostPrivProtocol.setStatus("current")


class _SnmpV3TrapHostPrivPassword_Type(DisplayString):
    """Custom type snmpV3TrapHostPrivPassword based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 24),
    )


_SnmpV3TrapHostPrivPassword_Type.__name__ = "DisplayString"
_SnmpV3TrapHostPrivPassword_Object = MibTableColumn
snmpV3TrapHostPrivPassword = _SnmpV3TrapHostPrivPassword_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 8, 2, 1, 7),
    _SnmpV3TrapHostPrivPassword_Type()
)
snmpV3TrapHostPrivPassword.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmpV3TrapHostPrivPassword.setStatus("current")


class _SnmpV3TrapHostActivated_Type(Integer32):
    """Custom type snmpV3TrapHostActivated based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notActive", 1),
          ("active", 2))
    )


_SnmpV3TrapHostActivated_Type.__name__ = "Integer32"
_SnmpV3TrapHostActivated_Object = MibTableColumn
snmpV3TrapHostActivated = _SnmpV3TrapHostActivated_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 8, 2, 1, 8),
    _SnmpV3TrapHostActivated_Type()
)
snmpV3TrapHostActivated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmpV3TrapHostActivated.setStatus("current")
_HzQtmTrapEnable_ObjectIdentity = ObjectIdentity
hzQtmTrapEnable = _HzQtmTrapEnable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 8, 3)
)


class _HzQtmColdStartTrap_Type(Integer32):
    """Custom type hzQtmColdStartTrap based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_HzQtmColdStartTrap_Type.__name__ = "Integer32"
_HzQtmColdStartTrap_Object = MibScalar
hzQtmColdStartTrap = _HzQtmColdStartTrap_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 8, 3, 1),
    _HzQtmColdStartTrap_Type()
)
hzQtmColdStartTrap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzQtmColdStartTrap.setStatus("current")


class _HzQtmLinkDownTrap_Type(Integer32):
    """Custom type hzQtmLinkDownTrap based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_HzQtmLinkDownTrap_Type.__name__ = "Integer32"
_HzQtmLinkDownTrap_Object = MibScalar
hzQtmLinkDownTrap = _HzQtmLinkDownTrap_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 8, 3, 2),
    _HzQtmLinkDownTrap_Type()
)
hzQtmLinkDownTrap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzQtmLinkDownTrap.setStatus("current")


class _HzQtmLinkUpTrap_Type(Integer32):
    """Custom type hzQtmLinkUpTrap based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_HzQtmLinkUpTrap_Type.__name__ = "Integer32"
_HzQtmLinkUpTrap_Object = MibScalar
hzQtmLinkUpTrap = _HzQtmLinkUpTrap_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 8, 3, 3),
    _HzQtmLinkUpTrap_Type()
)
hzQtmLinkUpTrap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzQtmLinkUpTrap.setStatus("current")


class _HzQtmExplicitAuthenticationFailureTrap_Type(Integer32):
    """Custom type hzQtmExplicitAuthenticationFailureTrap based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_HzQtmExplicitAuthenticationFailureTrap_Type.__name__ = "Integer32"
_HzQtmExplicitAuthenticationFailureTrap_Object = MibScalar
hzQtmExplicitAuthenticationFailureTrap = _HzQtmExplicitAuthenticationFailureTrap_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 8, 3, 4),
    _HzQtmExplicitAuthenticationFailureTrap_Type()
)
hzQtmExplicitAuthenticationFailureTrap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzQtmExplicitAuthenticationFailureTrap.setStatus("current")


class _HzQtmHitlessAamConfigMismatchTrap_Type(Integer32):
    """Custom type hzQtmHitlessAamConfigMismatchTrap based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_HzQtmHitlessAamConfigMismatchTrap_Type.__name__ = "Integer32"
_HzQtmHitlessAamConfigMismatchTrap_Object = MibScalar
hzQtmHitlessAamConfigMismatchTrap = _HzQtmHitlessAamConfigMismatchTrap_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 8, 3, 5),
    _HzQtmHitlessAamConfigMismatchTrap_Type()
)
hzQtmHitlessAamConfigMismatchTrap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzQtmHitlessAamConfigMismatchTrap.setStatus("current")


class _HzQtmHitlessAamActiveTrap_Type(Integer32):
    """Custom type hzQtmHitlessAamActiveTrap based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_HzQtmHitlessAamActiveTrap_Type.__name__ = "Integer32"
_HzQtmHitlessAamActiveTrap_Object = MibScalar
hzQtmHitlessAamActiveTrap = _HzQtmHitlessAamActiveTrap_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 8, 3, 6),
    _HzQtmHitlessAamActiveTrap_Type()
)
hzQtmHitlessAamActiveTrap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzQtmHitlessAamActiveTrap.setStatus("current")


class _HzQtmAtpcConfigMismatchTrap_Type(Integer32):
    """Custom type hzQtmAtpcConfigMismatchTrap based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_HzQtmAtpcConfigMismatchTrap_Type.__name__ = "Integer32"
_HzQtmAtpcConfigMismatchTrap_Object = MibScalar
hzQtmAtpcConfigMismatchTrap = _HzQtmAtpcConfigMismatchTrap_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 8, 3, 7),
    _HzQtmAtpcConfigMismatchTrap_Type()
)
hzQtmAtpcConfigMismatchTrap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzQtmAtpcConfigMismatchTrap.setStatus("current")


class _HzQtmSntpServersUnreachableTrap_Type(Integer32):
    """Custom type hzQtmSntpServersUnreachableTrap based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_HzQtmSntpServersUnreachableTrap_Type.__name__ = "Integer32"
_HzQtmSntpServersUnreachableTrap_Object = MibScalar
hzQtmSntpServersUnreachableTrap = _HzQtmSntpServersUnreachableTrap_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 8, 3, 8),
    _HzQtmSntpServersUnreachableTrap_Type()
)
hzQtmSntpServersUnreachableTrap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzQtmSntpServersUnreachableTrap.setStatus("current")


class _HzQtmFrequencyFileInvalidTrap_Type(Integer32):
    """Custom type hzQtmFrequencyFileInvalidTrap based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_HzQtmFrequencyFileInvalidTrap_Type.__name__ = "Integer32"
_HzQtmFrequencyFileInvalidTrap_Object = MibScalar
hzQtmFrequencyFileInvalidTrap = _HzQtmFrequencyFileInvalidTrap_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 8, 3, 9),
    _HzQtmFrequencyFileInvalidTrap_Type()
)
hzQtmFrequencyFileInvalidTrap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzQtmFrequencyFileInvalidTrap.setStatus("current")


class _HzQtmEnetPortDroppedFramesThresholdExceedTrap_Type(Integer32):
    """Custom type hzQtmEnetPortDroppedFramesThresholdExceedTrap based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_HzQtmEnetPortDroppedFramesThresholdExceedTrap_Type.__name__ = "Integer32"
_HzQtmEnetPortDroppedFramesThresholdExceedTrap_Object = MibScalar
hzQtmEnetPortDroppedFramesThresholdExceedTrap = _HzQtmEnetPortDroppedFramesThresholdExceedTrap_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 8, 3, 10),
    _HzQtmEnetPortDroppedFramesThresholdExceedTrap_Type()
)
hzQtmEnetPortDroppedFramesThresholdExceedTrap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzQtmEnetPortDroppedFramesThresholdExceedTrap.setStatus("current")


class _HzQtmEnetPortBandwidthUtilizationThresholdExceedTrap_Type(Integer32):
    """Custom type hzQtmEnetPortBandwidthUtilizationThresholdExceedTrap based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_HzQtmEnetPortBandwidthUtilizationThresholdExceedTrap_Type.__name__ = "Integer32"
_HzQtmEnetPortBandwidthUtilizationThresholdExceedTrap_Object = MibScalar
hzQtmEnetPortBandwidthUtilizationThresholdExceedTrap = _HzQtmEnetPortBandwidthUtilizationThresholdExceedTrap_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 8, 3, 11),
    _HzQtmEnetPortBandwidthUtilizationThresholdExceedTrap_Type()
)
hzQtmEnetPortBandwidthUtilizationThresholdExceedTrap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzQtmEnetPortBandwidthUtilizationThresholdExceedTrap.setStatus("current")


class _HzQtmEnetPortRlsMismatchTrap_Type(Integer32):
    """Custom type hzQtmEnetPortRlsMismatchTrap based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_HzQtmEnetPortRlsMismatchTrap_Type.__name__ = "Integer32"
_HzQtmEnetPortRlsMismatchTrap_Object = MibScalar
hzQtmEnetPortRlsMismatchTrap = _HzQtmEnetPortRlsMismatchTrap_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 8, 3, 12),
    _HzQtmEnetPortRlsMismatchTrap_Type()
)
hzQtmEnetPortRlsMismatchTrap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzQtmEnetPortRlsMismatchTrap.setStatus("current")


class _HzQtmRLSQueueBasedShutdownActivatedTrap_Type(Integer32):
    """Custom type hzQtmRLSQueueBasedShutdownActivatedTrap based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_HzQtmRLSQueueBasedShutdownActivatedTrap_Type.__name__ = "Integer32"
_HzQtmRLSQueueBasedShutdownActivatedTrap_Object = MibScalar
hzQtmRLSQueueBasedShutdownActivatedTrap = _HzQtmRLSQueueBasedShutdownActivatedTrap_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 8, 3, 13),
    _HzQtmRLSQueueBasedShutdownActivatedTrap_Type()
)
hzQtmRLSQueueBasedShutdownActivatedTrap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzQtmRLSQueueBasedShutdownActivatedTrap.setStatus("current")


class _HzQtmModemRxLossOfSignalLockTrap_Type(Integer32):
    """Custom type hzQtmModemRxLossOfSignalLockTrap based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_HzQtmModemRxLossOfSignalLockTrap_Type.__name__ = "Integer32"
_HzQtmModemRxLossOfSignalLockTrap_Object = MibScalar
hzQtmModemRxLossOfSignalLockTrap = _HzQtmModemRxLossOfSignalLockTrap_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 8, 3, 14),
    _HzQtmModemRxLossOfSignalLockTrap_Type()
)
hzQtmModemRxLossOfSignalLockTrap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzQtmModemRxLossOfSignalLockTrap.setStatus("current")


class _HzQtmModemTxLossOfSyncTrap_Type(Integer32):
    """Custom type hzQtmModemTxLossOfSyncTrap based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_HzQtmModemTxLossOfSyncTrap_Type.__name__ = "Integer32"
_HzQtmModemTxLossOfSyncTrap_Object = MibScalar
hzQtmModemTxLossOfSyncTrap = _HzQtmModemTxLossOfSyncTrap_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 8, 3, 15),
    _HzQtmModemTxLossOfSyncTrap_Type()
)
hzQtmModemTxLossOfSyncTrap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzQtmModemTxLossOfSyncTrap.setStatus("current")


class _HzQtmModemSnrBelowThresholdTrap_Type(Integer32):
    """Custom type hzQtmModemSnrBelowThresholdTrap based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_HzQtmModemSnrBelowThresholdTrap_Type.__name__ = "Integer32"
_HzQtmModemSnrBelowThresholdTrap_Object = MibScalar
hzQtmModemSnrBelowThresholdTrap = _HzQtmModemSnrBelowThresholdTrap_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 8, 3, 16),
    _HzQtmModemSnrBelowThresholdTrap_Type()
)
hzQtmModemSnrBelowThresholdTrap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzQtmModemSnrBelowThresholdTrap.setStatus("current")


class _HzQtmModemEqualizerStressExceedThresholdTrap_Type(Integer32):
    """Custom type hzQtmModemEqualizerStressExceedThresholdTrap based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_HzQtmModemEqualizerStressExceedThresholdTrap_Type.__name__ = "Integer32"
_HzQtmModemEqualizerStressExceedThresholdTrap_Object = MibScalar
hzQtmModemEqualizerStressExceedThresholdTrap = _HzQtmModemEqualizerStressExceedThresholdTrap_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 8, 3, 17),
    _HzQtmModemEqualizerStressExceedThresholdTrap_Type()
)
hzQtmModemEqualizerStressExceedThresholdTrap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzQtmModemEqualizerStressExceedThresholdTrap.setStatus("current")


class _HzQtmModemChannelizedRslBelowThresholdTrap_Type(Integer32):
    """Custom type hzQtmModemChannelizedRslBelowThresholdTrap based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_HzQtmModemChannelizedRslBelowThresholdTrap_Type.__name__ = "Integer32"
_HzQtmModemChannelizedRslBelowThresholdTrap_Object = MibScalar
hzQtmModemChannelizedRslBelowThresholdTrap = _HzQtmModemChannelizedRslBelowThresholdTrap_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 8, 3, 18),
    _HzQtmModemChannelizedRslBelowThresholdTrap_Type()
)
hzQtmModemChannelizedRslBelowThresholdTrap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzQtmModemChannelizedRslBelowThresholdTrap.setStatus("current")


class _HzQtmFpgaProgrammingErrorTrap_Type(Integer32):
    """Custom type hzQtmFpgaProgrammingErrorTrap based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_HzQtmFpgaProgrammingErrorTrap_Type.__name__ = "Integer32"
_HzQtmFpgaProgrammingErrorTrap_Object = MibScalar
hzQtmFpgaProgrammingErrorTrap = _HzQtmFpgaProgrammingErrorTrap_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 8, 3, 19),
    _HzQtmFpgaProgrammingErrorTrap_Type()
)
hzQtmFpgaProgrammingErrorTrap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzQtmFpgaProgrammingErrorTrap.setStatus("current")


class _HzQtmUserManagementSessionCommencedTrap_Type(Integer32):
    """Custom type hzQtmUserManagementSessionCommencedTrap based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_HzQtmUserManagementSessionCommencedTrap_Type.__name__ = "Integer32"
_HzQtmUserManagementSessionCommencedTrap_Object = MibScalar
hzQtmUserManagementSessionCommencedTrap = _HzQtmUserManagementSessionCommencedTrap_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 8, 3, 20),
    _HzQtmUserManagementSessionCommencedTrap_Type()
)
hzQtmUserManagementSessionCommencedTrap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzQtmUserManagementSessionCommencedTrap.setStatus("current")


class _HzQtmUserManagementSessionTerminatedTrap_Type(Integer32):
    """Custom type hzQtmUserManagementSessionTerminatedTrap based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_HzQtmUserManagementSessionTerminatedTrap_Type.__name__ = "Integer32"
_HzQtmUserManagementSessionTerminatedTrap_Object = MibScalar
hzQtmUserManagementSessionTerminatedTrap = _HzQtmUserManagementSessionTerminatedTrap_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 8, 3, 21),
    _HzQtmUserManagementSessionTerminatedTrap_Type()
)
hzQtmUserManagementSessionTerminatedTrap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzQtmUserManagementSessionTerminatedTrap.setStatus("current")


class _HzQtmAtpcTxAtMaxPwrTrap_Type(Integer32):
    """Custom type hzQtmAtpcTxAtMaxPwrTrap based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_HzQtmAtpcTxAtMaxPwrTrap_Type.__name__ = "Integer32"
_HzQtmAtpcTxAtMaxPwrTrap_Object = MibScalar
hzQtmAtpcTxAtMaxPwrTrap = _HzQtmAtpcTxAtMaxPwrTrap_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 8, 3, 22),
    _HzQtmAtpcTxAtMaxPwrTrap_Type()
)
hzQtmAtpcTxAtMaxPwrTrap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzQtmAtpcTxAtMaxPwrTrap.setStatus("current")


class _HzQtmRadioSynthLostLockTrap_Type(Integer32):
    """Custom type hzQtmRadioSynthLostLockTrap based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_HzQtmRadioSynthLostLockTrap_Type.__name__ = "Integer32"
_HzQtmRadioSynthLostLockTrap_Object = MibScalar
hzQtmRadioSynthLostLockTrap = _HzQtmRadioSynthLostLockTrap_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 8, 3, 23),
    _HzQtmRadioSynthLostLockTrap_Type()
)
hzQtmRadioSynthLostLockTrap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzQtmRadioSynthLostLockTrap.setStatus("current")


class _HzQtmRadioLostCommunicationTrap_Type(Integer32):
    """Custom type hzQtmRadioLostCommunicationTrap based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_HzQtmRadioLostCommunicationTrap_Type.__name__ = "Integer32"
_HzQtmRadioLostCommunicationTrap_Object = MibScalar
hzQtmRadioLostCommunicationTrap = _HzQtmRadioLostCommunicationTrap_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 8, 3, 24),
    _HzQtmRadioLostCommunicationTrap_Type()
)
hzQtmRadioLostCommunicationTrap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzQtmRadioLostCommunicationTrap.setStatus("current")


class _HzQtmRadioMismatchTrap_Type(Integer32):
    """Custom type hzQtmRadioMismatchTrap based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_HzQtmRadioMismatchTrap_Type.__name__ = "Integer32"
_HzQtmRadioMismatchTrap_Object = MibScalar
hzQtmRadioMismatchTrap = _HzQtmRadioMismatchTrap_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 8, 3, 25),
    _HzQtmRadioMismatchTrap_Type()
)
hzQtmRadioMismatchTrap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzQtmRadioMismatchTrap.setStatus("current")


class _HzQtmRadioPowerAmpTrap_Type(Integer32):
    """Custom type hzQtmRadioPowerAmpTrap based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_HzQtmRadioPowerAmpTrap_Type.__name__ = "Integer32"
_HzQtmRadioPowerAmpTrap_Object = MibScalar
hzQtmRadioPowerAmpTrap = _HzQtmRadioPowerAmpTrap_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 8, 3, 26),
    _HzQtmRadioPowerAmpTrap_Type()
)
hzQtmRadioPowerAmpTrap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzQtmRadioPowerAmpTrap.setStatus("current")


class _HzQtmRadioExcessiveTxCableLossTrap_Type(Integer32):
    """Custom type hzQtmRadioExcessiveTxCableLossTrap based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_HzQtmRadioExcessiveTxCableLossTrap_Type.__name__ = "Integer32"
_HzQtmRadioExcessiveTxCableLossTrap_Object = MibScalar
hzQtmRadioExcessiveTxCableLossTrap = _HzQtmRadioExcessiveTxCableLossTrap_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 8, 3, 27),
    _HzQtmRadioExcessiveTxCableLossTrap_Type()
)
hzQtmRadioExcessiveTxCableLossTrap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzQtmRadioExcessiveTxCableLossTrap.setStatus("current")


class _HzQtmHiPowerRadioTxDetectorTrap_Type(Integer32):
    """Custom type hzQtmHiPowerRadioTxDetectorTrap based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_HzQtmHiPowerRadioTxDetectorTrap_Type.__name__ = "Integer32"
_HzQtmHiPowerRadioTxDetectorTrap_Object = MibScalar
hzQtmHiPowerRadioTxDetectorTrap = _HzQtmHiPowerRadioTxDetectorTrap_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 8, 3, 28),
    _HzQtmHiPowerRadioTxDetectorTrap_Type()
)
hzQtmHiPowerRadioTxDetectorTrap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzQtmHiPowerRadioTxDetectorTrap.setStatus("current")


class _HzQtmSecondaryRadioIsActiveTrap_Type(Integer32):
    """Custom type hzQtmSecondaryRadioIsActiveTrap based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_HzQtmSecondaryRadioIsActiveTrap_Type.__name__ = "Integer32"
_HzQtmSecondaryRadioIsActiveTrap_Object = MibScalar
hzQtmSecondaryRadioIsActiveTrap = _HzQtmSecondaryRadioIsActiveTrap_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 8, 3, 29),
    _HzQtmSecondaryRadioIsActiveTrap_Type()
)
hzQtmSecondaryRadioIsActiveTrap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzQtmSecondaryRadioIsActiveTrap.setStatus("current")


class _HzQtmRedundancySerialNumberMisMatchTrap_Type(Integer32):
    """Custom type hzQtmRedundancySerialNumberMisMatchTrap based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_HzQtmRedundancySerialNumberMisMatchTrap_Type.__name__ = "Integer32"
_HzQtmRedundancySerialNumberMisMatchTrap_Object = MibScalar
hzQtmRedundancySerialNumberMisMatchTrap = _HzQtmRedundancySerialNumberMisMatchTrap_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 8, 3, 30),
    _HzQtmRedundancySerialNumberMisMatchTrap_Type()
)
hzQtmRedundancySerialNumberMisMatchTrap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzQtmRedundancySerialNumberMisMatchTrap.setStatus("current")


class _HzQtmRadioFirmwareMismatchTrap_Type(Integer32):
    """Custom type hzQtmRadioFirmwareMismatchTrap based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_HzQtmRadioFirmwareMismatchTrap_Type.__name__ = "Integer32"
_HzQtmRadioFirmwareMismatchTrap_Object = MibScalar
hzQtmRadioFirmwareMismatchTrap = _HzQtmRadioFirmwareMismatchTrap_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 8, 3, 31),
    _HzQtmRadioFirmwareMismatchTrap_Type()
)
hzQtmRadioFirmwareMismatchTrap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzQtmRadioFirmwareMismatchTrap.setStatus("current")


class _HzQtmSecondaryRadioNotdetectedTrap_Type(Integer32):
    """Custom type hzQtmSecondaryRadioNotdetectedTrap based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_HzQtmSecondaryRadioNotdetectedTrap_Type.__name__ = "Integer32"
_HzQtmSecondaryRadioNotdetectedTrap_Object = MibScalar
hzQtmSecondaryRadioNotdetectedTrap = _HzQtmSecondaryRadioNotdetectedTrap_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 8, 3, 32),
    _HzQtmSecondaryRadioNotdetectedTrap_Type()
)
hzQtmSecondaryRadioNotdetectedTrap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzQtmSecondaryRadioNotdetectedTrap.setStatus("current")


class _HzQtmPrimaryRadioNotdetectedTrap_Type(Integer32):
    """Custom type hzQtmPrimaryRadioNotdetectedTrap based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_HzQtmPrimaryRadioNotdetectedTrap_Type.__name__ = "Integer32"
_HzQtmPrimaryRadioNotdetectedTrap_Object = MibScalar
hzQtmPrimaryRadioNotdetectedTrap = _HzQtmPrimaryRadioNotdetectedTrap_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 8, 3, 33),
    _HzQtmPrimaryRadioNotdetectedTrap_Type()
)
hzQtmPrimaryRadioNotdetectedTrap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzQtmPrimaryRadioNotdetectedTrap.setStatus("current")


class _HzQtmFaultyPrimaryRadioTrap_Type(Integer32):
    """Custom type hzQtmFaultyPrimaryRadioTrap based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_HzQtmFaultyPrimaryRadioTrap_Type.__name__ = "Integer32"
_HzQtmFaultyPrimaryRadioTrap_Object = MibScalar
hzQtmFaultyPrimaryRadioTrap = _HzQtmFaultyPrimaryRadioTrap_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 8, 3, 34),
    _HzQtmFaultyPrimaryRadioTrap_Type()
)
hzQtmFaultyPrimaryRadioTrap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzQtmFaultyPrimaryRadioTrap.setStatus("current")


class _HzQtmRadioExcessiveTxCableLossChangeTrap_Type(Integer32):
    """Custom type hzQtmRadioExcessiveTxCableLossChangeTrap based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_HzQtmRadioExcessiveTxCableLossChangeTrap_Type.__name__ = "Integer32"
_HzQtmRadioExcessiveTxCableLossChangeTrap_Object = MibScalar
hzQtmRadioExcessiveTxCableLossChangeTrap = _HzQtmRadioExcessiveTxCableLossChangeTrap_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 8, 3, 35),
    _HzQtmRadioExcessiveTxCableLossChangeTrap_Type()
)
hzQtmRadioExcessiveTxCableLossChangeTrap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzQtmRadioExcessiveTxCableLossChangeTrap.setStatus("current")


class _HzQtmRadioExcessiveRxCableLossTrap_Type(Integer32):
    """Custom type hzQtmRadioExcessiveRxCableLossTrap based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_HzQtmRadioExcessiveRxCableLossTrap_Type.__name__ = "Integer32"
_HzQtmRadioExcessiveRxCableLossTrap_Object = MibScalar
hzQtmRadioExcessiveRxCableLossTrap = _HzQtmRadioExcessiveRxCableLossTrap_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 8, 3, 36),
    _HzQtmRadioExcessiveRxCableLossTrap_Type()
)
hzQtmRadioExcessiveRxCableLossTrap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzQtmRadioExcessiveRxCableLossTrap.setStatus("current")


class _HzQtmRedundancyPrimaryPortNotSetTrap_Type(Integer32):
    """Custom type hzQtmRedundancyPrimaryPortNotSetTrap based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_HzQtmRedundancyPrimaryPortNotSetTrap_Type.__name__ = "Integer32"
_HzQtmRedundancyPrimaryPortNotSetTrap_Object = MibScalar
hzQtmRedundancyPrimaryPortNotSetTrap = _HzQtmRedundancyPrimaryPortNotSetTrap_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 8, 3, 37),
    _HzQtmRedundancyPrimaryPortNotSetTrap_Type()
)
hzQtmRedundancyPrimaryPortNotSetTrap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzQtmRedundancyPrimaryPortNotSetTrap.setStatus("current")


class _HzQtmRedundancySecondaryPortIsActiveTrap_Type(Integer32):
    """Custom type hzQtmRedundancySecondaryPortIsActiveTrap based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_HzQtmRedundancySecondaryPortIsActiveTrap_Type.__name__ = "Integer32"
_HzQtmRedundancySecondaryPortIsActiveTrap_Object = MibScalar
hzQtmRedundancySecondaryPortIsActiveTrap = _HzQtmRedundancySecondaryPortIsActiveTrap_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 8, 3, 38),
    _HzQtmRedundancySecondaryPortIsActiveTrap_Type()
)
hzQtmRedundancySecondaryPortIsActiveTrap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzQtmRedundancySecondaryPortIsActiveTrap.setStatus("current")


class _HzQtmRedundancyPrimaryPortFaultyTrap_Type(Integer32):
    """Custom type hzQtmRedundancyPrimaryPortFaultyTrap based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_HzQtmRedundancyPrimaryPortFaultyTrap_Type.__name__ = "Integer32"
_HzQtmRedundancyPrimaryPortFaultyTrap_Object = MibScalar
hzQtmRedundancyPrimaryPortFaultyTrap = _HzQtmRedundancyPrimaryPortFaultyTrap_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 8, 3, 39),
    _HzQtmRedundancyPrimaryPortFaultyTrap_Type()
)
hzQtmRedundancyPrimaryPortFaultyTrap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzQtmRedundancyPrimaryPortFaultyTrap.setStatus("current")


class _HzQtmRedundancySecondaryPortFaultyTrap_Type(Integer32):
    """Custom type hzQtmRedundancySecondaryPortFaultyTrap based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_HzQtmRedundancySecondaryPortFaultyTrap_Type.__name__ = "Integer32"
_HzQtmRedundancySecondaryPortFaultyTrap_Object = MibScalar
hzQtmRedundancySecondaryPortFaultyTrap = _HzQtmRedundancySecondaryPortFaultyTrap_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 8, 3, 40),
    _HzQtmRedundancySecondaryPortFaultyTrap_Type()
)
hzQtmRedundancySecondaryPortFaultyTrap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzQtmRedundancySecondaryPortFaultyTrap.setStatus("current")


class _HzQtmFanFailedTrap_Type(Integer32):
    """Custom type hzQtmFanFailedTrap based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_HzQtmFanFailedTrap_Type.__name__ = "Integer32"
_HzQtmFanFailedTrap_Object = MibScalar
hzQtmFanFailedTrap = _HzQtmFanFailedTrap_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 8, 3, 41),
    _HzQtmFanFailedTrap_Type()
)
hzQtmFanFailedTrap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzQtmFanFailedTrap.setStatus("current")


class _HzQtmModemRlsShutdownActivatedTrap_Type(Integer32):
    """Custom type hzQtmModemRlsShutdownActivatedTrap based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_HzQtmModemRlsShutdownActivatedTrap_Type.__name__ = "Integer32"
_HzQtmModemRlsShutdownActivatedTrap_Object = MibScalar
hzQtmModemRlsShutdownActivatedTrap = _HzQtmModemRlsShutdownActivatedTrap_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 8, 3, 42),
    _HzQtmModemRlsShutdownActivatedTrap_Type()
)
hzQtmModemRlsShutdownActivatedTrap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzQtmModemRlsShutdownActivatedTrap.setStatus("current")


class _HzQtmRadioUnitHwChangedTrap_Type(Integer32):
    """Custom type hzQtmRadioUnitHwChangedTrap based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_HzQtmRadioUnitHwChangedTrap_Type.__name__ = "Integer32"
_HzQtmRadioUnitHwChangedTrap_Object = MibScalar
hzQtmRadioUnitHwChangedTrap = _HzQtmRadioUnitHwChangedTrap_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 8, 3, 43),
    _HzQtmRadioUnitHwChangedTrap_Type()
)
hzQtmRadioUnitHwChangedTrap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzQtmRadioUnitHwChangedTrap.setStatus("current")


class _HzQtmRadioSwDownloadFailedTrap_Type(Integer32):
    """Custom type hzQtmRadioSwDownloadFailedTrap based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_HzQtmRadioSwDownloadFailedTrap_Type.__name__ = "Integer32"
_HzQtmRadioSwDownloadFailedTrap_Object = MibScalar
hzQtmRadioSwDownloadFailedTrap = _HzQtmRadioSwDownloadFailedTrap_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 8, 3, 44),
    _HzQtmRadioSwDownloadFailedTrap_Type()
)
hzQtmRadioSwDownloadFailedTrap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzQtmRadioSwDownloadFailedTrap.setStatus("current")


class _HzQtmRadioRestartedOKTrap_Type(Integer32):
    """Custom type hzQtmRadioRestartedOKTrap based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_HzQtmRadioRestartedOKTrap_Type.__name__ = "Integer32"
_HzQtmRadioRestartedOKTrap_Object = MibScalar
hzQtmRadioRestartedOKTrap = _HzQtmRadioRestartedOKTrap_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 8, 3, 45),
    _HzQtmRadioRestartedOKTrap_Type()
)
hzQtmRadioRestartedOKTrap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzQtmRadioRestartedOKTrap.setStatus("current")


class _HzQtmMibChangeNotSavedTrap_Type(Integer32):
    """Custom type hzQtmMibChangeNotSavedTrap based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_HzQtmMibChangeNotSavedTrap_Type.__name__ = "Integer32"
_HzQtmMibChangeNotSavedTrap_Object = MibScalar
hzQtmMibChangeNotSavedTrap = _HzQtmMibChangeNotSavedTrap_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 8, 3, 46),
    _HzQtmMibChangeNotSavedTrap_Type()
)
hzQtmMibChangeNotSavedTrap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzQtmMibChangeNotSavedTrap.setStatus("current")


class _HzQtmRadioDrainCurrentTrap_Type(Integer32):
    """Custom type hzQtmRadioDrainCurrentTrap based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_HzQtmRadioDrainCurrentTrap_Type.__name__ = "Integer32"
_HzQtmRadioDrainCurrentTrap_Object = MibScalar
hzQtmRadioDrainCurrentTrap = _HzQtmRadioDrainCurrentTrap_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 8, 3, 47),
    _HzQtmRadioDrainCurrentTrap_Type()
)
hzQtmRadioDrainCurrentTrap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzQtmRadioDrainCurrentTrap.setStatus("current")


class _HzQtmIFLostLockTrap_Type(Integer32):
    """Custom type hzQtmIFLostLockTrap based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_HzQtmIFLostLockTrap_Type.__name__ = "Integer32"
_HzQtmIFLostLockTrap_Object = MibScalar
hzQtmIFLostLockTrap = _HzQtmIFLostLockTrap_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 8, 3, 48),
    _HzQtmIFLostLockTrap_Type()
)
hzQtmIFLostLockTrap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzQtmIFLostLockTrap.setStatus("current")


class _HzQtmInvalidSystemConfigurationTrap_Type(Integer32):
    """Custom type hzQtmInvalidSystemConfigurationTrap based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_HzQtmInvalidSystemConfigurationTrap_Type.__name__ = "Integer32"
_HzQtmInvalidSystemConfigurationTrap_Object = MibScalar
hzQtmInvalidSystemConfigurationTrap = _HzQtmInvalidSystemConfigurationTrap_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 8, 3, 49),
    _HzQtmInvalidSystemConfigurationTrap_Type()
)
hzQtmInvalidSystemConfigurationTrap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzQtmInvalidSystemConfigurationTrap.setStatus("current")


class _HzQtmHitlessAamEventTrap_Type(Integer32):
    """Custom type hzQtmHitlessAamEventTrap based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_HzQtmHitlessAamEventTrap_Type.__name__ = "Integer32"
_HzQtmHitlessAamEventTrap_Object = MibScalar
hzQtmHitlessAamEventTrap = _HzQtmHitlessAamEventTrap_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 8, 3, 50),
    _HzQtmHitlessAamEventTrap_Type()
)
hzQtmHitlessAamEventTrap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzQtmHitlessAamEventTrap.setStatus("current")


class _HzQtmModemXPICEqualizerStressExceedThresholdTrap_Type(Integer32):
    """Custom type hzQtmModemXPICEqualizerStressExceedThresholdTrap based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_HzQtmModemXPICEqualizerStressExceedThresholdTrap_Type.__name__ = "Integer32"
_HzQtmModemXPICEqualizerStressExceedThresholdTrap_Object = MibScalar
hzQtmModemXPICEqualizerStressExceedThresholdTrap = _HzQtmModemXPICEqualizerStressExceedThresholdTrap_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 8, 3, 51),
    _HzQtmModemXPICEqualizerStressExceedThresholdTrap_Type()
)
hzQtmModemXPICEqualizerStressExceedThresholdTrap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzQtmModemXPICEqualizerStressExceedThresholdTrap.setStatus("current")


class _HzQtmPartnerNodeAlarmTrap_Type(Integer32):
    """Custom type hzQtmPartnerNodeAlarmTrap based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_HzQtmPartnerNodeAlarmTrap_Type.__name__ = "Integer32"
_HzQtmPartnerNodeAlarmTrap_Object = MibScalar
hzQtmPartnerNodeAlarmTrap = _HzQtmPartnerNodeAlarmTrap_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 8, 3, 52),
    _HzQtmPartnerNodeAlarmTrap_Type()
)
hzQtmPartnerNodeAlarmTrap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzQtmPartnerNodeAlarmTrap.setStatus("current")


class _HzQtmBandwidthDoublingInvalidLinkConfigTrap_Type(Integer32):
    """Custom type hzQtmBandwidthDoublingInvalidLinkConfigTrap based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_HzQtmBandwidthDoublingInvalidLinkConfigTrap_Type.__name__ = "Integer32"
_HzQtmBandwidthDoublingInvalidLinkConfigTrap_Object = MibScalar
hzQtmBandwidthDoublingInvalidLinkConfigTrap = _HzQtmBandwidthDoublingInvalidLinkConfigTrap_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 8, 3, 53),
    _HzQtmBandwidthDoublingInvalidLinkConfigTrap_Type()
)
hzQtmBandwidthDoublingInvalidLinkConfigTrap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzQtmBandwidthDoublingInvalidLinkConfigTrap.setStatus("current")


class _HzQtmBandwidthDoublingWrongPortConnectedTrap_Type(Integer32):
    """Custom type hzQtmBandwidthDoublingWrongPortConnectedTrap based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_HzQtmBandwidthDoublingWrongPortConnectedTrap_Type.__name__ = "Integer32"
_HzQtmBandwidthDoublingWrongPortConnectedTrap_Object = MibScalar
hzQtmBandwidthDoublingWrongPortConnectedTrap = _HzQtmBandwidthDoublingWrongPortConnectedTrap_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 8, 3, 54),
    _HzQtmBandwidthDoublingWrongPortConnectedTrap_Type()
)
hzQtmBandwidthDoublingWrongPortConnectedTrap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzQtmBandwidthDoublingWrongPortConnectedTrap.setStatus("current")


class _HzQtmRadioPowerOffTrap_Type(Integer32):
    """Custom type hzQtmRadioPowerOffTrap based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_HzQtmRadioPowerOffTrap_Type.__name__ = "Integer32"
_HzQtmRadioPowerOffTrap_Object = MibScalar
hzQtmRadioPowerOffTrap = _HzQtmRadioPowerOffTrap_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 8, 3, 55),
    _HzQtmRadioPowerOffTrap_Type()
)
hzQtmRadioPowerOffTrap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzQtmRadioPowerOffTrap.setStatus("current")


class _HzQtmSynceLostLockTrap_Type(Integer32):
    """Custom type hzQtmSynceLostLockTrap based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_HzQtmSynceLostLockTrap_Type.__name__ = "Integer32"
_HzQtmSynceLostLockTrap_Object = MibScalar
hzQtmSynceLostLockTrap = _HzQtmSynceLostLockTrap_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 8, 3, 56),
    _HzQtmSynceLostLockTrap_Type()
)
hzQtmSynceLostLockTrap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzQtmSynceLostLockTrap.setStatus("current")


class _HzQtmSynceSecondarySourceInUseTrap_Type(Integer32):
    """Custom type hzQtmSynceSecondarySourceInUseTrap based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_HzQtmSynceSecondarySourceInUseTrap_Type.__name__ = "Integer32"
_HzQtmSynceSecondarySourceInUseTrap_Object = MibScalar
hzQtmSynceSecondarySourceInUseTrap = _HzQtmSynceSecondarySourceInUseTrap_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 8, 3, 57),
    _HzQtmSynceSecondarySourceInUseTrap_Type()
)
hzQtmSynceSecondarySourceInUseTrap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzQtmSynceSecondarySourceInUseTrap.setStatus("current")
_HzQtmSnmp_ObjectIdentity = ObjectIdentity
hzQtmSnmp = _HzQtmSnmp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 9)
)


class _HzQtmSnmpUserAccess_Type(Integer32):
    """Custom type hzQtmSnmpUserAccess based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("explicitManagers", 1),
          ("any", 2))
    )


_HzQtmSnmpUserAccess_Type.__name__ = "Integer32"
_HzQtmSnmpUserAccess_Object = MibScalar
hzQtmSnmpUserAccess = _HzQtmSnmpUserAccess_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 9, 1),
    _HzQtmSnmpUserAccess_Type()
)
hzQtmSnmpUserAccess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzQtmSnmpUserAccess.setStatus("current")


class _HzQtmSnmpManagerAnyCommunityName_Type(DisplayString):
    """Custom type hzQtmSnmpManagerAnyCommunityName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 24),
    )


_HzQtmSnmpManagerAnyCommunityName_Type.__name__ = "DisplayString"
_HzQtmSnmpManagerAnyCommunityName_Object = MibScalar
hzQtmSnmpManagerAnyCommunityName = _HzQtmSnmpManagerAnyCommunityName_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 9, 2),
    _HzQtmSnmpManagerAnyCommunityName_Type()
)
hzQtmSnmpManagerAnyCommunityName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzQtmSnmpManagerAnyCommunityName.setStatus("current")


class _HzQtmSnmpSetRequests_Type(Integer32):
    """Custom type hzQtmSnmpSetRequests based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_HzQtmSnmpSetRequests_Type.__name__ = "Integer32"
_HzQtmSnmpSetRequests_Object = MibScalar
hzQtmSnmpSetRequests = _HzQtmSnmpSetRequests_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 9, 3),
    _HzQtmSnmpSetRequests_Type()
)
hzQtmSnmpSetRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzQtmSnmpSetRequests.setStatus("current")
_HzQtmSnmpManagersTable_Object = MibTable
hzQtmSnmpManagersTable = _HzQtmSnmpManagersTable_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 9, 4)
)
if mibBuilder.loadTexts:
    hzQtmSnmpManagersTable.setStatus("current")
_HzQtmSnmpManagersEntry_Object = MibTableRow
hzQtmSnmpManagersEntry = _HzQtmSnmpManagersEntry_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 9, 4, 1)
)
hzQtmSnmpManagersEntry.setIndexNames(
    (0, "DRAGONWAVE-HORIZON-QUANTUM-MIB", "hzQtmSnmpManagersIndex"),
)
if mibBuilder.loadTexts:
    hzQtmSnmpManagersEntry.setStatus("current")
_HzQtmSnmpManagersIndex_Type = Integer32
_HzQtmSnmpManagersIndex_Object = MibTableColumn
hzQtmSnmpManagersIndex = _HzQtmSnmpManagersIndex_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 9, 4, 1, 1),
    _HzQtmSnmpManagersIndex_Type()
)
hzQtmSnmpManagersIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzQtmSnmpManagersIndex.setStatus("current")
_HzQtmSnmpManagerIpAddress_Type = IpAddress
_HzQtmSnmpManagerIpAddress_Object = MibTableColumn
hzQtmSnmpManagerIpAddress = _HzQtmSnmpManagerIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 9, 4, 1, 2),
    _HzQtmSnmpManagerIpAddress_Type()
)
hzQtmSnmpManagerIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzQtmSnmpManagerIpAddress.setStatus("current")


class _HzQtmSnmpManagerCommunityName_Type(DisplayString):
    """Custom type hzQtmSnmpManagerCommunityName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 24),
    )


_HzQtmSnmpManagerCommunityName_Type.__name__ = "DisplayString"
_HzQtmSnmpManagerCommunityName_Object = MibTableColumn
hzQtmSnmpManagerCommunityName = _HzQtmSnmpManagerCommunityName_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 9, 4, 1, 3),
    _HzQtmSnmpManagerCommunityName_Type()
)
hzQtmSnmpManagerCommunityName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzQtmSnmpManagerCommunityName.setStatus("current")


class _HzQtmSnmpManagerActivated_Type(Integer32):
    """Custom type hzQtmSnmpManagerActivated based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notActive", 1),
          ("active", 2))
    )


_HzQtmSnmpManagerActivated_Type.__name__ = "Integer32"
_HzQtmSnmpManagerActivated_Object = MibTableColumn
hzQtmSnmpManagerActivated = _HzQtmSnmpManagerActivated_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 9, 4, 1, 4),
    _HzQtmSnmpManagerActivated_Type()
)
hzQtmSnmpManagerActivated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzQtmSnmpManagerActivated.setStatus("current")
_HzQtmSnmpV3ManagersTable_Object = MibTable
hzQtmSnmpV3ManagersTable = _HzQtmSnmpV3ManagersTable_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 9, 5)
)
if mibBuilder.loadTexts:
    hzQtmSnmpV3ManagersTable.setStatus("current")
_HzQtmSnmpV3ManagersEntry_Object = MibTableRow
hzQtmSnmpV3ManagersEntry = _HzQtmSnmpV3ManagersEntry_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 9, 5, 1)
)
hzQtmSnmpV3ManagersEntry.setIndexNames(
    (0, "DRAGONWAVE-HORIZON-QUANTUM-MIB", "hzQtmSnmpV3ManagersIndex"),
)
if mibBuilder.loadTexts:
    hzQtmSnmpV3ManagersEntry.setStatus("current")
_HzQtmSnmpV3ManagersIndex_Type = Integer32
_HzQtmSnmpV3ManagersIndex_Object = MibTableColumn
hzQtmSnmpV3ManagersIndex = _HzQtmSnmpV3ManagersIndex_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 9, 5, 1, 1),
    _HzQtmSnmpV3ManagersIndex_Type()
)
hzQtmSnmpV3ManagersIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzQtmSnmpV3ManagersIndex.setStatus("current")


class _HzQtmSnmpV3ManagerUserName_Type(DisplayString):
    """Custom type hzQtmSnmpV3ManagerUserName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 24),
    )


_HzQtmSnmpV3ManagerUserName_Type.__name__ = "DisplayString"
_HzQtmSnmpV3ManagerUserName_Object = MibTableColumn
hzQtmSnmpV3ManagerUserName = _HzQtmSnmpV3ManagerUserName_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 9, 5, 1, 2),
    _HzQtmSnmpV3ManagerUserName_Type()
)
hzQtmSnmpV3ManagerUserName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzQtmSnmpV3ManagerUserName.setStatus("current")


class _HzQtmSnmpV3ManagerAuthProtocol_Type(Integer32):
    """Custom type hzQtmSnmpV3ManagerAuthProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("noAuth", 1),
          ("md5", 2),
          ("sha", 3))
    )


_HzQtmSnmpV3ManagerAuthProtocol_Type.__name__ = "Integer32"
_HzQtmSnmpV3ManagerAuthProtocol_Object = MibTableColumn
hzQtmSnmpV3ManagerAuthProtocol = _HzQtmSnmpV3ManagerAuthProtocol_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 9, 5, 1, 3),
    _HzQtmSnmpV3ManagerAuthProtocol_Type()
)
hzQtmSnmpV3ManagerAuthProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzQtmSnmpV3ManagerAuthProtocol.setStatus("current")


class _HzQtmSnmpV3ManagerAuthPassword_Type(DisplayString):
    """Custom type hzQtmSnmpV3ManagerAuthPassword based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 24),
    )


_HzQtmSnmpV3ManagerAuthPassword_Type.__name__ = "DisplayString"
_HzQtmSnmpV3ManagerAuthPassword_Object = MibTableColumn
hzQtmSnmpV3ManagerAuthPassword = _HzQtmSnmpV3ManagerAuthPassword_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 9, 5, 1, 4),
    _HzQtmSnmpV3ManagerAuthPassword_Type()
)
hzQtmSnmpV3ManagerAuthPassword.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzQtmSnmpV3ManagerAuthPassword.setStatus("current")


class _HzQtmSnmpV3ManagerPrivProtocol_Type(Integer32):
    """Custom type hzQtmSnmpV3ManagerPrivProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noPriv", 1),
          ("des", 2))
    )


_HzQtmSnmpV3ManagerPrivProtocol_Type.__name__ = "Integer32"
_HzQtmSnmpV3ManagerPrivProtocol_Object = MibTableColumn
hzQtmSnmpV3ManagerPrivProtocol = _HzQtmSnmpV3ManagerPrivProtocol_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 9, 5, 1, 5),
    _HzQtmSnmpV3ManagerPrivProtocol_Type()
)
hzQtmSnmpV3ManagerPrivProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzQtmSnmpV3ManagerPrivProtocol.setStatus("current")


class _HzQtmSnmpV3ManagerPrivPassword_Type(DisplayString):
    """Custom type hzQtmSnmpV3ManagerPrivPassword based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 24),
    )


_HzQtmSnmpV3ManagerPrivPassword_Type.__name__ = "DisplayString"
_HzQtmSnmpV3ManagerPrivPassword_Object = MibTableColumn
hzQtmSnmpV3ManagerPrivPassword = _HzQtmSnmpV3ManagerPrivPassword_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 9, 5, 1, 6),
    _HzQtmSnmpV3ManagerPrivPassword_Type()
)
hzQtmSnmpV3ManagerPrivPassword.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzQtmSnmpV3ManagerPrivPassword.setStatus("current")


class _HzQtmSnmpV3ManagerActivated_Type(Integer32):
    """Custom type hzQtmSnmpV3ManagerActivated based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notActive", 1),
          ("active", 2))
    )


_HzQtmSnmpV3ManagerActivated_Type.__name__ = "Integer32"
_HzQtmSnmpV3ManagerActivated_Object = MibTableColumn
hzQtmSnmpV3ManagerActivated = _HzQtmSnmpV3ManagerActivated_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 9, 5, 1, 7),
    _HzQtmSnmpV3ManagerActivated_Type()
)
hzQtmSnmpV3ManagerActivated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzQtmSnmpV3ManagerActivated.setStatus("current")
_HzQtmManagementSessions_ObjectIdentity = ObjectIdentity
hzQtmManagementSessions = _HzQtmManagementSessions_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 10)
)
_HzQtmUserSessionUserTable_Object = MibTable
hzQtmUserSessionUserTable = _HzQtmUserSessionUserTable_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 10, 1)
)
if mibBuilder.loadTexts:
    hzQtmUserSessionUserTable.setStatus("current")
_HzQtmUserSessionUserEntry_Object = MibTableRow
hzQtmUserSessionUserEntry = _HzQtmUserSessionUserEntry_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 10, 1, 1)
)
hzQtmUserSessionUserEntry.setIndexNames(
    (0, "DRAGONWAVE-HORIZON-QUANTUM-MIB", "hzQtmUserSessionUserIndex"),
)
if mibBuilder.loadTexts:
    hzQtmUserSessionUserEntry.setStatus("current")


class _HzQtmUserSessionUserIndex_Type(Integer32):
    """Custom type hzQtmUserSessionUserIndex based on Integer32"""
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


_HzQtmUserSessionUserIndex_Type.__name__ = "Integer32"
_HzQtmUserSessionUserIndex_Object = MibTableColumn
hzQtmUserSessionUserIndex = _HzQtmUserSessionUserIndex_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 10, 1, 1, 1),
    _HzQtmUserSessionUserIndex_Type()
)
hzQtmUserSessionUserIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzQtmUserSessionUserIndex.setStatus("current")


class _HzQtmUserSessionUserName_Type(DisplayString):
    """Custom type hzQtmUserSessionUserName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_HzQtmUserSessionUserName_Type.__name__ = "DisplayString"
_HzQtmUserSessionUserName_Object = MibTableColumn
hzQtmUserSessionUserName = _HzQtmUserSessionUserName_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 10, 1, 1, 2),
    _HzQtmUserSessionUserName_Type()
)
hzQtmUserSessionUserName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzQtmUserSessionUserName.setStatus("current")
_HzQtmUserSessionUserConnectionType_Type = DisplayString
_HzQtmUserSessionUserConnectionType_Object = MibTableColumn
hzQtmUserSessionUserConnectionType = _HzQtmUserSessionUserConnectionType_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 10, 1, 1, 3),
    _HzQtmUserSessionUserConnectionType_Type()
)
hzQtmUserSessionUserConnectionType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzQtmUserSessionUserConnectionType.setStatus("current")


class _HzQtmUserSessionUserState_Type(Integer32):
    """Custom type hzQtmUserSessionUserState based on Integer32"""
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


_HzQtmUserSessionUserState_Type.__name__ = "Integer32"
_HzQtmUserSessionUserState_Object = MibTableColumn
hzQtmUserSessionUserState = _HzQtmUserSessionUserState_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 10, 1, 1, 4),
    _HzQtmUserSessionUserState_Type()
)
hzQtmUserSessionUserState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzQtmUserSessionUserState.setStatus("current")
_HzQtmHttp_ObjectIdentity = ObjectIdentity
hzQtmHttp = _HzQtmHttp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 11)
)


class _HzQtmHttpEnable_Type(Integer32):
    """Custom type hzQtmHttpEnable based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_HzQtmHttpEnable_Type.__name__ = "Integer32"
_HzQtmHttpEnable_Object = MibScalar
hzQtmHttpEnable = _HzQtmHttpEnable_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 11, 1),
    _HzQtmHttpEnable_Type()
)
hzQtmHttpEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzQtmHttpEnable.setStatus("current")
_HzQtmHttpSecure_ObjectIdentity = ObjectIdentity
hzQtmHttpSecure = _HzQtmHttpSecure_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 11, 2)
)


class _HzQtmHttpSecureCertificateStatus_Type(DisplayString):
    """Custom type hzQtmHttpSecureCertificateStatus based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 100),
    )


_HzQtmHttpSecureCertificateStatus_Type.__name__ = "DisplayString"
_HzQtmHttpSecureCertificateStatus_Object = MibScalar
hzQtmHttpSecureCertificateStatus = _HzQtmHttpSecureCertificateStatus_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 11, 2, 1),
    _HzQtmHttpSecureCertificateStatus_Type()
)
hzQtmHttpSecureCertificateStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzQtmHttpSecureCertificateStatus.setStatus("current")


class _HzQtmHttpSecureAccessForAdminUsers_Type(Integer32):
    """Custom type hzQtmHttpSecureAccessForAdminUsers based on Integer32"""
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


_HzQtmHttpSecureAccessForAdminUsers_Type.__name__ = "Integer32"
_HzQtmHttpSecureAccessForAdminUsers_Object = MibScalar
hzQtmHttpSecureAccessForAdminUsers = _HzQtmHttpSecureAccessForAdminUsers_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 11, 2, 2),
    _HzQtmHttpSecureAccessForAdminUsers_Type()
)
hzQtmHttpSecureAccessForAdminUsers.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzQtmHttpSecureAccessForAdminUsers.setStatus("current")


class _HzQtmHttpSecureAccessForNocUsers_Type(Integer32):
    """Custom type hzQtmHttpSecureAccessForNocUsers based on Integer32"""
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


_HzQtmHttpSecureAccessForNocUsers_Type.__name__ = "Integer32"
_HzQtmHttpSecureAccessForNocUsers_Object = MibScalar
hzQtmHttpSecureAccessForNocUsers = _HzQtmHttpSecureAccessForNocUsers_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 11, 2, 3),
    _HzQtmHttpSecureAccessForNocUsers_Type()
)
hzQtmHttpSecureAccessForNocUsers.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzQtmHttpSecureAccessForNocUsers.setStatus("current")


class _HzQtmHttpSecureAccessForSuperUsers_Type(Integer32):
    """Custom type hzQtmHttpSecureAccessForSuperUsers based on Integer32"""
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


_HzQtmHttpSecureAccessForSuperUsers_Type.__name__ = "Integer32"
_HzQtmHttpSecureAccessForSuperUsers_Object = MibScalar
hzQtmHttpSecureAccessForSuperUsers = _HzQtmHttpSecureAccessForSuperUsers_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 11, 2, 4),
    _HzQtmHttpSecureAccessForSuperUsers_Type()
)
hzQtmHttpSecureAccessForSuperUsers.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzQtmHttpSecureAccessForSuperUsers.setStatus("current")
_HzQtmQos_ObjectIdentity = ObjectIdentity
hzQtmQos = _HzQtmQos_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 12)
)


class _HzQtmQosEnable_Type(Integer32):
    """Custom type hzQtmQosEnable based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_HzQtmQosEnable_Type.__name__ = "Integer32"
_HzQtmQosEnable_Object = MibScalar
hzQtmQosEnable = _HzQtmQosEnable_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 12, 1),
    _HzQtmQosEnable_Type()
)
hzQtmQosEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzQtmQosEnable.setStatus("current")


class _HzQtmCosType_Type(Integer32):
    """Custom type hzQtmCosType based on Integer32"""
    defaultValue = 1

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
        *(("cosVlan", 1),
          ("cosQinQiTag", 2),
          ("cosQinQoTag", 3),
          ("cosDscp", 4),
          ("cosMplsExp", 5))
    )


_HzQtmCosType_Type.__name__ = "Integer32"
_HzQtmCosType_Object = MibScalar
hzQtmCosType = _HzQtmCosType_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 12, 2),
    _HzQtmCosType_Type()
)
hzQtmCosType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzQtmCosType.setStatus("current")
_HzQtmCosQinQiTag_Type = DisplayString
_HzQtmCosQinQiTag_Object = MibScalar
hzQtmCosQinQiTag = _HzQtmCosQinQiTag_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 12, 3),
    _HzQtmCosQinQiTag_Type()
)
hzQtmCosQinQiTag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzQtmCosQinQiTag.setStatus("current")
_HzQtmCosQinQoTag_Type = DisplayString
_HzQtmCosQinQoTag_Object = MibScalar
hzQtmCosQinQoTag = _HzQtmCosQinQoTag_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 12, 4),
    _HzQtmCosQinQoTag_Type()
)
hzQtmCosQinQoTag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzQtmCosQinQoTag.setStatus("current")


class _HzQtmCosQueueMapping_Type(DisplayString):
    """Custom type hzQtmCosQueueMapping based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(15, 32),
    )


_HzQtmCosQueueMapping_Type.__name__ = "DisplayString"
_HzQtmCosQueueMapping_Object = MibScalar
hzQtmCosQueueMapping = _HzQtmCosQueueMapping_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 12, 5),
    _HzQtmCosQueueMapping_Type()
)
hzQtmCosQueueMapping.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzQtmCosQueueMapping.setStatus("current")


class _HzQtmCosExpediteQueue_Type(Integer32):
    """Custom type hzQtmCosExpediteQueue based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_HzQtmCosExpediteQueue_Type.__name__ = "Integer32"
_HzQtmCosExpediteQueue_Object = MibScalar
hzQtmCosExpediteQueue = _HzQtmCosExpediteQueue_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 12, 6),
    _HzQtmCosExpediteQueue_Type()
)
hzQtmCosExpediteQueue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzQtmCosExpediteQueue.setStatus("current")


class _HzQtmCosQueueCIR_Type(DisplayString):
    """Custom type hzQtmCosQueueCIR based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_HzQtmCosQueueCIR_Type.__name__ = "DisplayString"
_HzQtmCosQueueCIR_Object = MibScalar
hzQtmCosQueueCIR = _HzQtmCosQueueCIR_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 12, 7),
    _HzQtmCosQueueCIR_Type()
)
hzQtmCosQueueCIR.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzQtmCosQueueCIR.setStatus("current")


class _HzQtmCosQueueCBS_Type(DisplayString):
    """Custom type hzQtmCosQueueCBS based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_HzQtmCosQueueCBS_Type.__name__ = "DisplayString"
_HzQtmCosQueueCBS_Object = MibScalar
hzQtmCosQueueCBS = _HzQtmCosQueueCBS_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 12, 8),
    _HzQtmCosQueueCBS_Type()
)
hzQtmCosQueueCBS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzQtmCosQueueCBS.setStatus("current")


class _HzQtmCosDefaultValue_Type(Integer32):
    """Custom type hzQtmCosDefaultValue based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_HzQtmCosDefaultValue_Type.__name__ = "Integer32"
_HzQtmCosDefaultValue_Object = MibScalar
hzQtmCosDefaultValue = _HzQtmCosDefaultValue_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 12, 9),
    _HzQtmCosDefaultValue_Type()
)
hzQtmCosDefaultValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzQtmCosDefaultValue.setStatus("current")


class _HzQtmQosPolicy_Type(Integer32):
    """Custom type hzQtmQosPolicy based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("strict-priority", 1),
          ("wfq", 2))
    )


_HzQtmQosPolicy_Type.__name__ = "Integer32"
_HzQtmQosPolicy_Object = MibScalar
hzQtmQosPolicy = _HzQtmQosPolicy_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 12, 10),
    _HzQtmQosPolicy_Type()
)
hzQtmQosPolicy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzQtmQosPolicy.setStatus("current")


class _HzQtmCosWfqWeight_Type(DisplayString):
    """Custom type hzQtmCosWfqWeight based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_HzQtmCosWfqWeight_Type.__name__ = "DisplayString"
_HzQtmCosWfqWeight_Object = MibScalar
hzQtmCosWfqWeight = _HzQtmCosWfqWeight_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 12, 11),
    _HzQtmCosWfqWeight_Type()
)
hzQtmCosWfqWeight.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzQtmCosWfqWeight.setStatus("current")


class _HzQtmCutThroughProcessing_Type(Integer32):
    """Custom type hzQtmCutThroughProcessing based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_HzQtmCutThroughProcessing_Type.__name__ = "Integer32"
_HzQtmCutThroughProcessing_Object = MibScalar
hzQtmCutThroughProcessing = _HzQtmCutThroughProcessing_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 12, 12),
    _HzQtmCutThroughProcessing_Type()
)
hzQtmCutThroughProcessing.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzQtmCutThroughProcessing.setStatus("current")


class _HzQtmCosEcfmFlowMapping_Type(Integer32):
    """Custom type hzQtmCosEcfmFlowMapping based on Integer32"""
    defaultValue = 1

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
        *(("disabled", 1),
          ("q1", 2),
          ("q2", 3),
          ("q3", 4),
          ("q4", 5),
          ("qC", 6))
    )


_HzQtmCosEcfmFlowMapping_Type.__name__ = "Integer32"
_HzQtmCosEcfmFlowMapping_Object = MibScalar
hzQtmCosEcfmFlowMapping = _HzQtmCosEcfmFlowMapping_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 12, 13),
    _HzQtmCosEcfmFlowMapping_Type()
)
hzQtmCosEcfmFlowMapping.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzQtmCosEcfmFlowMapping.setStatus("current")


class _HzQtmCosControlFlowMapping_Type(Integer32):
    """Custom type hzQtmCosControlFlowMapping based on Integer32"""
    defaultValue = 1

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
        *(("disabled", 1),
          ("q1", 2),
          ("q2", 3),
          ("q3", 4),
          ("q4", 5),
          ("qC", 6))
    )


_HzQtmCosControlFlowMapping_Type.__name__ = "Integer32"
_HzQtmCosControlFlowMapping_Object = MibScalar
hzQtmCosControlFlowMapping = _HzQtmCosControlFlowMapping_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 12, 14),
    _HzQtmCosControlFlowMapping_Type()
)
hzQtmCosControlFlowMapping.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzQtmCosControlFlowMapping.setStatus("current")
_HzQtmRapidLinkShutdown_ObjectIdentity = ObjectIdentity
hzQtmRapidLinkShutdown = _HzQtmRapidLinkShutdown_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 13)
)


class _HzQtmRlsEnable_Type(Integer32):
    """Custom type hzQtmRlsEnable based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_HzQtmRlsEnable_Type.__name__ = "Integer32"
_HzQtmRlsEnable_Object = MibScalar
hzQtmRlsEnable = _HzQtmRlsEnable_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 13, 1),
    _HzQtmRlsEnable_Type()
)
hzQtmRlsEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzQtmRlsEnable.setStatus("current")


class _HzQtmRlsHardFaultMonitor_Type(Integer32):
    """Custom type hzQtmRlsHardFaultMonitor based on Integer32"""
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


_HzQtmRlsHardFaultMonitor_Type.__name__ = "Integer32"
_HzQtmRlsHardFaultMonitor_Object = MibScalar
hzQtmRlsHardFaultMonitor = _HzQtmRlsHardFaultMonitor_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 13, 2),
    _HzQtmRlsHardFaultMonitor_Type()
)
hzQtmRlsHardFaultMonitor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzQtmRlsHardFaultMonitor.setStatus("current")


class _HzQtmRlsWirelessPortOption_Type(Integer32):
    """Custom type hzQtmRlsWirelessPortOption based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("anyport", 1),
          ("bothports", 2))
    )


_HzQtmRlsWirelessPortOption_Type.__name__ = "Integer32"
_HzQtmRlsWirelessPortOption_Object = MibScalar
hzQtmRlsWirelessPortOption = _HzQtmRlsWirelessPortOption_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 13, 3),
    _HzQtmRlsWirelessPortOption_Type()
)
hzQtmRlsWirelessPortOption.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzQtmRlsWirelessPortOption.setStatus("current")


class _HzQtmRlsAutomaticLinkReestablish_Type(Integer32):
    """Custom type hzQtmRlsAutomaticLinkReestablish based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_HzQtmRlsAutomaticLinkReestablish_Type.__name__ = "Integer32"
_HzQtmRlsAutomaticLinkReestablish_Object = MibScalar
hzQtmRlsAutomaticLinkReestablish = _HzQtmRlsAutomaticLinkReestablish_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 13, 4),
    _HzQtmRlsAutomaticLinkReestablish_Type()
)
hzQtmRlsAutomaticLinkReestablish.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzQtmRlsAutomaticLinkReestablish.setStatus("current")


class _HzQtmRlsManualLinkReestablish_Type(Integer32):
    """Custom type hzQtmRlsManualLinkReestablish based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_HzQtmRlsManualLinkReestablish_Type.__name__ = "Integer32"
_HzQtmRlsManualLinkReestablish_Object = MibScalar
hzQtmRlsManualLinkReestablish = _HzQtmRlsManualLinkReestablish_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 13, 5),
    _HzQtmRlsManualLinkReestablish_Type()
)
hzQtmRlsManualLinkReestablish.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzQtmRlsManualLinkReestablish.setStatus("current")


class _HzQtmWriteRlsMonitorParametersToSystem_Type(Integer32):
    """Custom type hzQtmWriteRlsMonitorParametersToSystem based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("enabled", 1)
    )


_HzQtmWriteRlsMonitorParametersToSystem_Type.__name__ = "Integer32"
_HzQtmWriteRlsMonitorParametersToSystem_Object = MibScalar
hzQtmWriteRlsMonitorParametersToSystem = _HzQtmWriteRlsMonitorParametersToSystem_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 13, 6),
    _HzQtmWriteRlsMonitorParametersToSystem_Type()
)
hzQtmWriteRlsMonitorParametersToSystem.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzQtmWriteRlsMonitorParametersToSystem.setStatus("current")


class _HzQtmRlsDroppedFramesThresholdOverride_Type(Integer32):
    """Custom type hzQtmRlsDroppedFramesThresholdOverride based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("enabled", 1)
    )


_HzQtmRlsDroppedFramesThresholdOverride_Type.__name__ = "Integer32"
_HzQtmRlsDroppedFramesThresholdOverride_Object = MibScalar
hzQtmRlsDroppedFramesThresholdOverride = _HzQtmRlsDroppedFramesThresholdOverride_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 13, 7),
    _HzQtmRlsDroppedFramesThresholdOverride_Type()
)
hzQtmRlsDroppedFramesThresholdOverride.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzQtmRlsDroppedFramesThresholdOverride.setStatus("current")
_HzQtmRlsDroppedFramesThresholdTable_Object = MibTable
hzQtmRlsDroppedFramesThresholdTable = _HzQtmRlsDroppedFramesThresholdTable_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 13, 8)
)
if mibBuilder.loadTexts:
    hzQtmRlsDroppedFramesThresholdTable.setStatus("current")
_HzQtmRlsDroppedFramesThresholdEntry_Object = MibTableRow
hzQtmRlsDroppedFramesThresholdEntry = _HzQtmRlsDroppedFramesThresholdEntry_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 13, 8, 1)
)
hzQtmRlsDroppedFramesThresholdEntry.setIndexNames(
    (0, "DRAGONWAVE-HORIZON-QUANTUM-MIB", "hzQtmRlsDroppedFramesThresholdIndex"),
)
if mibBuilder.loadTexts:
    hzQtmRlsDroppedFramesThresholdEntry.setStatus("current")


class _HzQtmRlsDroppedFramesThresholdIndex_Type(Integer32):
    """Custom type hzQtmRlsDroppedFramesThresholdIndex based on Integer32"""
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
        *(("queue-1", 1),
          ("queue-2", 2),
          ("queue-3", 3),
          ("queue-4", 4))
    )


_HzQtmRlsDroppedFramesThresholdIndex_Type.__name__ = "Integer32"
_HzQtmRlsDroppedFramesThresholdIndex_Object = MibTableColumn
hzQtmRlsDroppedFramesThresholdIndex = _HzQtmRlsDroppedFramesThresholdIndex_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 13, 8, 1, 1),
    _HzQtmRlsDroppedFramesThresholdIndex_Type()
)
hzQtmRlsDroppedFramesThresholdIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzQtmRlsDroppedFramesThresholdIndex.setStatus("current")
_HzQtmRlsAllowedDroppedFrameRateValue_Type = DisplayString
_HzQtmRlsAllowedDroppedFrameRateValue_Object = MibTableColumn
hzQtmRlsAllowedDroppedFrameRateValue = _HzQtmRlsAllowedDroppedFrameRateValue_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 13, 8, 1, 2),
    _HzQtmRlsAllowedDroppedFrameRateValue_Type()
)
hzQtmRlsAllowedDroppedFrameRateValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzQtmRlsAllowedDroppedFrameRateValue.setStatus("current")
_HzQtmRlsDroppedFrameMonitorPeriod_Type = Integer32
_HzQtmRlsDroppedFrameMonitorPeriod_Object = MibTableColumn
hzQtmRlsDroppedFrameMonitorPeriod = _HzQtmRlsDroppedFrameMonitorPeriod_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 13, 8, 1, 3),
    _HzQtmRlsDroppedFrameMonitorPeriod_Type()
)
hzQtmRlsDroppedFrameMonitorPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzQtmRlsDroppedFrameMonitorPeriod.setStatus("current")
_HzQtmRlsSoftFaultMonitorTable_Object = MibTable
hzQtmRlsSoftFaultMonitorTable = _HzQtmRlsSoftFaultMonitorTable_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 13, 9)
)
if mibBuilder.loadTexts:
    hzQtmRlsSoftFaultMonitorTable.setStatus("current")
_HzQtmRlsSoftFaultMonitorEntry_Object = MibTableRow
hzQtmRlsSoftFaultMonitorEntry = _HzQtmRlsSoftFaultMonitorEntry_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 13, 9, 1)
)
hzQtmRlsSoftFaultMonitorEntry.setIndexNames(
    (0, "DRAGONWAVE-HORIZON-QUANTUM-MIB", "hzQtmRlsSoftFaultMonitorIndex"),
)
if mibBuilder.loadTexts:
    hzQtmRlsSoftFaultMonitorEntry.setStatus("current")


class _HzQtmRlsSoftFaultMonitorIndex_Type(Integer32):
    """Custom type hzQtmRlsSoftFaultMonitorIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("wireless-port-1", 1),
          ("wireless-port-2", 2))
    )


_HzQtmRlsSoftFaultMonitorIndex_Type.__name__ = "Integer32"
_HzQtmRlsSoftFaultMonitorIndex_Object = MibTableColumn
hzQtmRlsSoftFaultMonitorIndex = _HzQtmRlsSoftFaultMonitorIndex_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 13, 9, 1, 1),
    _HzQtmRlsSoftFaultMonitorIndex_Type()
)
hzQtmRlsSoftFaultMonitorIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzQtmRlsSoftFaultMonitorIndex.setStatus("current")
_HzQtmRlsEstablishErredFrameThreshold_Type = Integer32
_HzQtmRlsEstablishErredFrameThreshold_Object = MibTableColumn
hzQtmRlsEstablishErredFrameThreshold = _HzQtmRlsEstablishErredFrameThreshold_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 13, 9, 1, 2),
    _HzQtmRlsEstablishErredFrameThreshold_Type()
)
hzQtmRlsEstablishErredFrameThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzQtmRlsEstablishErredFrameThreshold.setStatus("current")
_HzQtmRlsShutdownErredFrameThreshold_Type = Integer32
_HzQtmRlsShutdownErredFrameThreshold_Object = MibTableColumn
hzQtmRlsShutdownErredFrameThreshold = _HzQtmRlsShutdownErredFrameThreshold_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 13, 9, 1, 3),
    _HzQtmRlsShutdownErredFrameThreshold_Type()
)
hzQtmRlsShutdownErredFrameThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzQtmRlsShutdownErredFrameThreshold.setStatus("current")
_HzQtmRlsEstablishNumberOfSamples_Type = Integer32
_HzQtmRlsEstablishNumberOfSamples_Object = MibTableColumn
hzQtmRlsEstablishNumberOfSamples = _HzQtmRlsEstablishNumberOfSamples_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 13, 9, 1, 4),
    _HzQtmRlsEstablishNumberOfSamples_Type()
)
hzQtmRlsEstablishNumberOfSamples.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzQtmRlsEstablishNumberOfSamples.setStatus("current")
_HzQtmRlsShutdownNumberOfSamples_Type = Integer32
_HzQtmRlsShutdownNumberOfSamples_Object = MibTableColumn
hzQtmRlsShutdownNumberOfSamples = _HzQtmRlsShutdownNumberOfSamples_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 13, 9, 1, 5),
    _HzQtmRlsShutdownNumberOfSamples_Type()
)
hzQtmRlsShutdownNumberOfSamples.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzQtmRlsShutdownNumberOfSamples.setStatus("current")
_HzQtmRlsEstablishSamplePeriod_Type = Integer32
_HzQtmRlsEstablishSamplePeriod_Object = MibTableColumn
hzQtmRlsEstablishSamplePeriod = _HzQtmRlsEstablishSamplePeriod_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 13, 9, 1, 6),
    _HzQtmRlsEstablishSamplePeriod_Type()
)
hzQtmRlsEstablishSamplePeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzQtmRlsEstablishSamplePeriod.setStatus("current")
_HzQtmRlsShutdownSamplePeriod_Type = Integer32
_HzQtmRlsShutdownSamplePeriod_Object = MibTableColumn
hzQtmRlsShutdownSamplePeriod = _HzQtmRlsShutdownSamplePeriod_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 13, 9, 1, 7),
    _HzQtmRlsShutdownSamplePeriod_Type()
)
hzQtmRlsShutdownSamplePeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzQtmRlsShutdownSamplePeriod.setStatus("current")
_HzQtmRlsQuickShutdownSamplePeriod_Type = Integer32
_HzQtmRlsQuickShutdownSamplePeriod_Object = MibTableColumn
hzQtmRlsQuickShutdownSamplePeriod = _HzQtmRlsQuickShutdownSamplePeriod_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 13, 9, 1, 8),
    _HzQtmRlsQuickShutdownSamplePeriod_Type()
)
hzQtmRlsQuickShutdownSamplePeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzQtmRlsQuickShutdownSamplePeriod.setStatus("current")
_HzQtmHardFaultMonitorTable_Object = MibTable
hzQtmHardFaultMonitorTable = _HzQtmHardFaultMonitorTable_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 13, 10)
)
if mibBuilder.loadTexts:
    hzQtmHardFaultMonitorTable.setStatus("current")
_HzQtmHardFaultMonitorEntry_Object = MibTableRow
hzQtmHardFaultMonitorEntry = _HzQtmHardFaultMonitorEntry_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 13, 10, 1)
)
hzQtmHardFaultMonitorEntry.setIndexNames(
    (0, "DRAGONWAVE-HORIZON-QUANTUM-MIB", "hzQtmHardFaultMonitorIndex"),
)
if mibBuilder.loadTexts:
    hzQtmHardFaultMonitorEntry.setStatus("current")


class _HzQtmHardFaultMonitorIndex_Type(Integer32):
    """Custom type hzQtmHardFaultMonitorIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("wireless-port-1", 1),
          ("wireless-port-2", 2))
    )


_HzQtmHardFaultMonitorIndex_Type.__name__ = "Integer32"
_HzQtmHardFaultMonitorIndex_Object = MibTableColumn
hzQtmHardFaultMonitorIndex = _HzQtmHardFaultMonitorIndex_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 13, 10, 1, 1),
    _HzQtmHardFaultMonitorIndex_Type()
)
hzQtmHardFaultMonitorIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzQtmHardFaultMonitorIndex.setStatus("current")
_HzQtmRlsHardFaultSamplePeriod_Type = Integer32
_HzQtmRlsHardFaultSamplePeriod_Object = MibTableColumn
hzQtmRlsHardFaultSamplePeriod = _HzQtmRlsHardFaultSamplePeriod_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 13, 10, 1, 2),
    _HzQtmRlsHardFaultSamplePeriod_Type()
)
hzQtmRlsHardFaultSamplePeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzQtmRlsHardFaultSamplePeriod.setStatus("current")
_HzQtmRlsHardFaultThreshold_Type = Integer32
_HzQtmRlsHardFaultThreshold_Object = MibTableColumn
hzQtmRlsHardFaultThreshold = _HzQtmRlsHardFaultThreshold_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 13, 10, 1, 3),
    _HzQtmRlsHardFaultThreshold_Type()
)
hzQtmRlsHardFaultThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzQtmRlsHardFaultThreshold.setStatus("current")
_HzQtmRlsReceiveSignalLevelMonitorTable_Object = MibTable
hzQtmRlsReceiveSignalLevelMonitorTable = _HzQtmRlsReceiveSignalLevelMonitorTable_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 13, 11)
)
if mibBuilder.loadTexts:
    hzQtmRlsReceiveSignalLevelMonitorTable.setStatus("current")
_HzQtmRlsReceiveSignalLevelMonitorEntry_Object = MibTableRow
hzQtmRlsReceiveSignalLevelMonitorEntry = _HzQtmRlsReceiveSignalLevelMonitorEntry_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 13, 11, 1)
)
hzQtmRlsReceiveSignalLevelMonitorEntry.setIndexNames(
    (0, "DRAGONWAVE-HORIZON-QUANTUM-MIB", "hzQtmRlsReceiveSignalLevelMonitorIndex"),
)
if mibBuilder.loadTexts:
    hzQtmRlsReceiveSignalLevelMonitorEntry.setStatus("current")


class _HzQtmRlsReceiveSignalLevelMonitorIndex_Type(Integer32):
    """Custom type hzQtmRlsReceiveSignalLevelMonitorIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("wireless-port-1", 1),
          ("wireless-port-2", 2))
    )


_HzQtmRlsReceiveSignalLevelMonitorIndex_Type.__name__ = "Integer32"
_HzQtmRlsReceiveSignalLevelMonitorIndex_Object = MibTableColumn
hzQtmRlsReceiveSignalLevelMonitorIndex = _HzQtmRlsReceiveSignalLevelMonitorIndex_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 13, 11, 1, 1),
    _HzQtmRlsReceiveSignalLevelMonitorIndex_Type()
)
hzQtmRlsReceiveSignalLevelMonitorIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzQtmRlsReceiveSignalLevelMonitorIndex.setStatus("current")


class _HzQtmRlsMakeRslMonitorRslValue_Type(DisplayString):
    """Custom type hzQtmRlsMakeRslMonitorRslValue based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 24),
    )


_HzQtmRlsMakeRslMonitorRslValue_Type.__name__ = "DisplayString"
_HzQtmRlsMakeRslMonitorRslValue_Object = MibTableColumn
hzQtmRlsMakeRslMonitorRslValue = _HzQtmRlsMakeRslMonitorRslValue_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 13, 11, 1, 2),
    _HzQtmRlsMakeRslMonitorRslValue_Type()
)
hzQtmRlsMakeRslMonitorRslValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzQtmRlsMakeRslMonitorRslValue.setStatus("current")
_HzQtmRlsMakeRslMonitorPeriod_Type = Integer32
_HzQtmRlsMakeRslMonitorPeriod_Object = MibTableColumn
hzQtmRlsMakeRslMonitorPeriod = _HzQtmRlsMakeRslMonitorPeriod_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 13, 11, 1, 3),
    _HzQtmRlsMakeRslMonitorPeriod_Type()
)
hzQtmRlsMakeRslMonitorPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzQtmRlsMakeRslMonitorPeriod.setStatus("current")
_HzQtmRlsStatus_ObjectIdentity = ObjectIdentity
hzQtmRlsStatus = _HzQtmRlsStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 13, 12)
)
_HzQtmRlsCurrentDroppedFramesTable_Object = MibTable
hzQtmRlsCurrentDroppedFramesTable = _HzQtmRlsCurrentDroppedFramesTable_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 13, 12, 1)
)
if mibBuilder.loadTexts:
    hzQtmRlsCurrentDroppedFramesTable.setStatus("current")
_HzQtmRlsCurrentDroppedFramesEntry_Object = MibTableRow
hzQtmRlsCurrentDroppedFramesEntry = _HzQtmRlsCurrentDroppedFramesEntry_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 13, 12, 1, 1)
)
hzQtmRlsCurrentDroppedFramesEntry.setIndexNames(
    (0, "DRAGONWAVE-HORIZON-QUANTUM-MIB", "hzQtmRlsCurrentDroppedFramesIndex"),
)
if mibBuilder.loadTexts:
    hzQtmRlsCurrentDroppedFramesEntry.setStatus("current")


class _HzQtmRlsCurrentDroppedFramesIndex_Type(Integer32):
    """Custom type hzQtmRlsCurrentDroppedFramesIndex based on Integer32"""
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
        *(("queue-1", 1),
          ("queue-2", 2),
          ("queue-3", 3),
          ("queue-4", 4))
    )


_HzQtmRlsCurrentDroppedFramesIndex_Type.__name__ = "Integer32"
_HzQtmRlsCurrentDroppedFramesIndex_Object = MibTableColumn
hzQtmRlsCurrentDroppedFramesIndex = _HzQtmRlsCurrentDroppedFramesIndex_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 13, 12, 1, 1, 1),
    _HzQtmRlsCurrentDroppedFramesIndex_Type()
)
hzQtmRlsCurrentDroppedFramesIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzQtmRlsCurrentDroppedFramesIndex.setStatus("current")
_HzQtmRlsCurrentDroppedFramesRateValue_Type = DisplayString
_HzQtmRlsCurrentDroppedFramesRateValue_Object = MibTableColumn
hzQtmRlsCurrentDroppedFramesRateValue = _HzQtmRlsCurrentDroppedFramesRateValue_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 13, 12, 1, 1, 2),
    _HzQtmRlsCurrentDroppedFramesRateValue_Type()
)
hzQtmRlsCurrentDroppedFramesRateValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzQtmRlsCurrentDroppedFramesRateValue.setStatus("current")
_HzQtmRlsCurrentDroppedFrameMonitorPeriod_Type = Integer32
_HzQtmRlsCurrentDroppedFrameMonitorPeriod_Object = MibTableColumn
hzQtmRlsCurrentDroppedFrameMonitorPeriod = _HzQtmRlsCurrentDroppedFrameMonitorPeriod_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 13, 12, 1, 1, 3),
    _HzQtmRlsCurrentDroppedFrameMonitorPeriod_Type()
)
hzQtmRlsCurrentDroppedFrameMonitorPeriod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzQtmRlsCurrentDroppedFrameMonitorPeriod.setStatus("current")
_HzQtmRlsCurrentQueueStatus_Type = DisplayString
_HzQtmRlsCurrentQueueStatus_Object = MibTableColumn
hzQtmRlsCurrentQueueStatus = _HzQtmRlsCurrentQueueStatus_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 13, 12, 1, 1, 4),
    _HzQtmRlsCurrentQueueStatus_Type()
)
hzQtmRlsCurrentQueueStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzQtmRlsCurrentQueueStatus.setStatus("current")
_HzQtmRlsStatusTable_Object = MibTable
hzQtmRlsStatusTable = _HzQtmRlsStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 13, 12, 2)
)
if mibBuilder.loadTexts:
    hzQtmRlsStatusTable.setStatus("current")
_HzQtmRlsStatusEntry_Object = MibTableRow
hzQtmRlsStatusEntry = _HzQtmRlsStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 13, 12, 2, 1)
)
hzQtmRlsStatusEntry.setIndexNames(
    (0, "DRAGONWAVE-HORIZON-QUANTUM-MIB", "hzQtmRlsStatusIndex"),
)
if mibBuilder.loadTexts:
    hzQtmRlsStatusEntry.setStatus("current")


class _HzQtmRlsStatusIndex_Type(Integer32):
    """Custom type hzQtmRlsStatusIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("wireless-port-1", 1),
          ("wireless-port-2", 2))
    )


_HzQtmRlsStatusIndex_Type.__name__ = "Integer32"
_HzQtmRlsStatusIndex_Object = MibTableColumn
hzQtmRlsStatusIndex = _HzQtmRlsStatusIndex_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 13, 12, 2, 1, 1),
    _HzQtmRlsStatusIndex_Type()
)
hzQtmRlsStatusIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzQtmRlsStatusIndex.setStatus("current")
_HzQtmRlsOption_Type = DisplayString
_HzQtmRlsOption_Object = MibTableColumn
hzQtmRlsOption = _HzQtmRlsOption_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 13, 12, 2, 1, 2),
    _HzQtmRlsOption_Type()
)
hzQtmRlsOption.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzQtmRlsOption.setStatus("current")
_HzQtmRlsState_Type = DisplayString
_HzQtmRlsState_Object = MibTableColumn
hzQtmRlsState = _HzQtmRlsState_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 13, 12, 2, 1, 3),
    _HzQtmRlsState_Type()
)
hzQtmRlsState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzQtmRlsState.setStatus("current")
_HzQtmRlsMismatchState_Type = DisplayString
_HzQtmRlsMismatchState_Object = MibTableColumn
hzQtmRlsMismatchState = _HzQtmRlsMismatchState_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 13, 12, 2, 1, 4),
    _HzQtmRlsMismatchState_Type()
)
hzQtmRlsMismatchState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzQtmRlsMismatchState.setStatus("current")
_HzQtmDegradeMonitorState_Type = DisplayString
_HzQtmDegradeMonitorState_Object = MibTableColumn
hzQtmDegradeMonitorState = _HzQtmDegradeMonitorState_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 13, 12, 2, 1, 5),
    _HzQtmDegradeMonitorState_Type()
)
hzQtmDegradeMonitorState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzQtmDegradeMonitorState.setStatus("current")
_HzQtmHardFaultMonitorState_Type = DisplayString
_HzQtmHardFaultMonitorState_Object = MibTableColumn
hzQtmHardFaultMonitorState = _HzQtmHardFaultMonitorState_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 13, 12, 2, 1, 6),
    _HzQtmHardFaultMonitorState_Type()
)
hzQtmHardFaultMonitorState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzQtmHardFaultMonitorState.setStatus("current")
_HzQtmMakeRslThresholdState_Type = DisplayString
_HzQtmMakeRslThresholdState_Object = MibTableColumn
hzQtmMakeRslThresholdState = _HzQtmMakeRslThresholdState_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 13, 12, 2, 1, 7),
    _HzQtmMakeRslThresholdState_Type()
)
hzQtmMakeRslThresholdState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzQtmMakeRslThresholdState.setStatus("current")
_HzQtmPeerRlsState_Type = DisplayString
_HzQtmPeerRlsState_Object = MibTableColumn
hzQtmPeerRlsState = _HzQtmPeerRlsState_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 13, 12, 2, 1, 8),
    _HzQtmPeerRlsState_Type()
)
hzQtmPeerRlsState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzQtmPeerRlsState.setStatus("current")
_HzQtmRadioInterfaceState_Type = DisplayString
_HzQtmRadioInterfaceState_Object = MibTableColumn
hzQtmRadioInterfaceState = _HzQtmRadioInterfaceState_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 13, 12, 2, 1, 9),
    _HzQtmRadioInterfaceState_Type()
)
hzQtmRadioInterfaceState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzQtmRadioInterfaceState.setStatus("current")
_HzQtmNetworkInterfaceState_Type = DisplayString
_HzQtmNetworkInterfaceState_Object = MibTableColumn
hzQtmNetworkInterfaceState = _HzQtmNetworkInterfaceState_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 13, 12, 2, 1, 10),
    _HzQtmNetworkInterfaceState_Type()
)
hzQtmNetworkInterfaceState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzQtmNetworkInterfaceState.setStatus("current")
_HzQtmUserConfiguredEstablishFer_Type = DisplayString
_HzQtmUserConfiguredEstablishFer_Object = MibTableColumn
hzQtmUserConfiguredEstablishFer = _HzQtmUserConfiguredEstablishFer_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 13, 12, 2, 1, 11),
    _HzQtmUserConfiguredEstablishFer_Type()
)
hzQtmUserConfiguredEstablishFer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzQtmUserConfiguredEstablishFer.setStatus("current")
_HzQtmMinimumAchievableEstablishFer_Type = DisplayString
_HzQtmMinimumAchievableEstablishFer_Object = MibTableColumn
hzQtmMinimumAchievableEstablishFer = _HzQtmMinimumAchievableEstablishFer_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 13, 12, 2, 1, 12),
    _HzQtmMinimumAchievableEstablishFer_Type()
)
hzQtmMinimumAchievableEstablishFer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzQtmMinimumAchievableEstablishFer.setStatus("current")
_HzQtmUserConfiguredShutdownFer_Type = DisplayString
_HzQtmUserConfiguredShutdownFer_Object = MibTableColumn
hzQtmUserConfiguredShutdownFer = _HzQtmUserConfiguredShutdownFer_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 13, 12, 2, 1, 13),
    _HzQtmUserConfiguredShutdownFer_Type()
)
hzQtmUserConfiguredShutdownFer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzQtmUserConfiguredShutdownFer.setStatus("current")
_HzQtmMinimumAchievableShutdownFer_Type = DisplayString
_HzQtmMinimumAchievableShutdownFer_Object = MibTableColumn
hzQtmMinimumAchievableShutdownFer = _HzQtmMinimumAchievableShutdownFer_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 13, 12, 2, 1, 14),
    _HzQtmMinimumAchievableShutdownFer_Type()
)
hzQtmMinimumAchievableShutdownFer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzQtmMinimumAchievableShutdownFer.setStatus("current")
_HzQtmUserConfiguredEstablishMonitorTime_Type = Integer32
_HzQtmUserConfiguredEstablishMonitorTime_Object = MibTableColumn
hzQtmUserConfiguredEstablishMonitorTime = _HzQtmUserConfiguredEstablishMonitorTime_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 13, 12, 2, 1, 15),
    _HzQtmUserConfiguredEstablishMonitorTime_Type()
)
hzQtmUserConfiguredEstablishMonitorTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzQtmUserConfiguredEstablishMonitorTime.setStatus("current")
_HzQtmActualEstablishMonitorTime_Type = Integer32
_HzQtmActualEstablishMonitorTime_Object = MibTableColumn
hzQtmActualEstablishMonitorTime = _HzQtmActualEstablishMonitorTime_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 13, 12, 2, 1, 16),
    _HzQtmActualEstablishMonitorTime_Type()
)
hzQtmActualEstablishMonitorTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzQtmActualEstablishMonitorTime.setStatus("current")
_HzQtmUserConfiguredShutdownMonitorTime_Type = Integer32
_HzQtmUserConfiguredShutdownMonitorTime_Object = MibTableColumn
hzQtmUserConfiguredShutdownMonitorTime = _HzQtmUserConfiguredShutdownMonitorTime_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 13, 12, 2, 1, 17),
    _HzQtmUserConfiguredShutdownMonitorTime_Type()
)
hzQtmUserConfiguredShutdownMonitorTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzQtmUserConfiguredShutdownMonitorTime.setStatus("current")
_HzQtmActualShutdownMonitorTime_Type = Integer32
_HzQtmActualShutdownMonitorTime_Object = MibTableColumn
hzQtmActualShutdownMonitorTime = _HzQtmActualShutdownMonitorTime_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 13, 12, 2, 1, 18),
    _HzQtmActualShutdownMonitorTime_Type()
)
hzQtmActualShutdownMonitorTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzQtmActualShutdownMonitorTime.setStatus("current")
_HzQtmRlsPortGroup_ObjectIdentity = ObjectIdentity
hzQtmRlsPortGroup = _HzQtmRlsPortGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 13, 13)
)


class _HzQtmRlsPort1_Type(Integer32):
    """Custom type hzQtmRlsPort1 based on Integer32"""
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
        *(("exclude", 0),
          ("gr-A", 1),
          ("gr-B", 2),
          ("gr-C", 3))
    )


_HzQtmRlsPort1_Type.__name__ = "Integer32"
_HzQtmRlsPort1_Object = MibScalar
hzQtmRlsPort1 = _HzQtmRlsPort1_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 13, 13, 1),
    _HzQtmRlsPort1_Type()
)
hzQtmRlsPort1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzQtmRlsPort1.setStatus("current")


class _HzQtmRlsPort2_Type(Integer32):
    """Custom type hzQtmRlsPort2 based on Integer32"""
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
        *(("exlcude", 0),
          ("gr-A", 1),
          ("gr-B", 2),
          ("gr-C", 3))
    )


_HzQtmRlsPort2_Type.__name__ = "Integer32"
_HzQtmRlsPort2_Object = MibScalar
hzQtmRlsPort2 = _HzQtmRlsPort2_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 13, 13, 2),
    _HzQtmRlsPort2_Type()
)
hzQtmRlsPort2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzQtmRlsPort2.setStatus("current")


class _HzQtmRlsPort3_Type(Integer32):
    """Custom type hzQtmRlsPort3 based on Integer32"""
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
        *(("exclude", 0),
          ("gr-A", 1),
          ("gr-B", 2),
          ("gr-C", 3))
    )


_HzQtmRlsPort3_Type.__name__ = "Integer32"
_HzQtmRlsPort3_Object = MibScalar
hzQtmRlsPort3 = _HzQtmRlsPort3_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 13, 13, 3),
    _HzQtmRlsPort3_Type()
)
hzQtmRlsPort3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzQtmRlsPort3.setStatus("current")


class _HzQtmRlsPort4_Type(Integer32):
    """Custom type hzQtmRlsPort4 based on Integer32"""
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
        *(("exlcude", 0),
          ("gr-A", 1),
          ("gr-B", 2),
          ("gr-C", 3))
    )


_HzQtmRlsPort4_Type.__name__ = "Integer32"
_HzQtmRlsPort4_Object = MibScalar
hzQtmRlsPort4 = _HzQtmRlsPort4_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 13, 13, 4),
    _HzQtmRlsPort4_Type()
)
hzQtmRlsPort4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzQtmRlsPort4.setStatus("current")


class _HzQtmRlsPort5_Type(Integer32):
    """Custom type hzQtmRlsPort5 based on Integer32"""
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
        *(("exclude", 0),
          ("gr-A", 1),
          ("gr-B", 2),
          ("gr-C", 3))
    )


_HzQtmRlsPort5_Type.__name__ = "Integer32"
_HzQtmRlsPort5_Object = MibScalar
hzQtmRlsPort5 = _HzQtmRlsPort5_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 13, 13, 5),
    _HzQtmRlsPort5_Type()
)
hzQtmRlsPort5.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzQtmRlsPort5.setStatus("current")


class _HzQtmRlsPort6_Type(Integer32):
    """Custom type hzQtmRlsPort6 based on Integer32"""
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
        *(("exclude", 0),
          ("gr-A", 1),
          ("gr-B", 2),
          ("gr-C", 3))
    )


_HzQtmRlsPort6_Type.__name__ = "Integer32"
_HzQtmRlsPort6_Object = MibScalar
hzQtmRlsPort6 = _HzQtmRlsPort6_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 13, 13, 6),
    _HzQtmRlsPort6_Type()
)
hzQtmRlsPort6.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzQtmRlsPort6.setStatus("current")


class _HzQtmRlsPort7_Type(Integer32):
    """Custom type hzQtmRlsPort7 based on Integer32"""
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
        *(("exclude", 0),
          ("gr-A", 1),
          ("gr-B", 2),
          ("gr-C", 3))
    )


_HzQtmRlsPort7_Type.__name__ = "Integer32"
_HzQtmRlsPort7_Object = MibScalar
hzQtmRlsPort7 = _HzQtmRlsPort7_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 13, 13, 7),
    _HzQtmRlsPort7_Type()
)
hzQtmRlsPort7.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzQtmRlsPort7.setStatus("current")


class _HzQtmRlsPort8_Type(Integer32):
    """Custom type hzQtmRlsPort8 based on Integer32"""
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
        *(("exclude", 0),
          ("gr-A", 1),
          ("gr-B", 2),
          ("gr-C", 3))
    )


_HzQtmRlsPort8_Type.__name__ = "Integer32"
_HzQtmRlsPort8_Object = MibScalar
hzQtmRlsPort8 = _HzQtmRlsPort8_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 13, 13, 8),
    _HzQtmRlsPort8_Type()
)
hzQtmRlsPort8.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzQtmRlsPort8.setStatus("current")


class _HzQtmRlsPauseEnable_Type(Integer32):
    """Custom type hzQtmRlsPauseEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_HzQtmRlsPauseEnable_Type.__name__ = "Integer32"
_HzQtmRlsPauseEnable_Object = MibScalar
hzQtmRlsPauseEnable = _HzQtmRlsPauseEnable_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 13, 14),
    _HzQtmRlsPauseEnable_Type()
)
hzQtmRlsPauseEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzQtmRlsPauseEnable.setStatus("current")
_HzQtmSntp_ObjectIdentity = ObjectIdentity
hzQtmSntp = _HzQtmSntp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 14)
)


class _HzQtmSntpEnable_Type(Integer32):
    """Custom type hzQtmSntpEnable based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_HzQtmSntpEnable_Type.__name__ = "Integer32"
_HzQtmSntpEnable_Object = MibScalar
hzQtmSntpEnable = _HzQtmSntpEnable_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 14, 1),
    _HzQtmSntpEnable_Type()
)
hzQtmSntpEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzQtmSntpEnable.setStatus("current")


class _HzQtmSntpOffset_Type(Integer32):
    """Custom type hzQtmSntpOffset based on Integer32"""
    defaultValue = -40

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-140, 140),
    )


_HzQtmSntpOffset_Type.__name__ = "Integer32"
_HzQtmSntpOffset_Object = MibScalar
hzQtmSntpOffset = _HzQtmSntpOffset_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 14, 2),
    _HzQtmSntpOffset_Type()
)
hzQtmSntpOffset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzQtmSntpOffset.setStatus("current")
_HzQtmSntpServerTable_Object = MibTable
hzQtmSntpServerTable = _HzQtmSntpServerTable_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 14, 3)
)
if mibBuilder.loadTexts:
    hzQtmSntpServerTable.setStatus("current")
_HzQtmSntpServerEntry_Object = MibTableRow
hzQtmSntpServerEntry = _HzQtmSntpServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 14, 3, 1)
)
hzQtmSntpServerEntry.setIndexNames(
    (0, "DRAGONWAVE-HORIZON-QUANTUM-MIB", "hzQtmSntpServerIndex"),
)
if mibBuilder.loadTexts:
    hzQtmSntpServerEntry.setStatus("current")
_HzQtmSntpServerIndex_Type = Integer32
_HzQtmSntpServerIndex_Object = MibTableColumn
hzQtmSntpServerIndex = _HzQtmSntpServerIndex_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 14, 3, 1, 1),
    _HzQtmSntpServerIndex_Type()
)
hzQtmSntpServerIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzQtmSntpServerIndex.setStatus("current")
_HzQtmSntpServerIpAddress_Type = IpAddress
_HzQtmSntpServerIpAddress_Object = MibTableColumn
hzQtmSntpServerIpAddress = _HzQtmSntpServerIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 14, 3, 1, 2),
    _HzQtmSntpServerIpAddress_Type()
)
hzQtmSntpServerIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzQtmSntpServerIpAddress.setStatus("current")


class _HzQtmSntpServerStatus_Type(Integer32):
    """Custom type hzQtmSntpServerStatus based on Integer32"""
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


_HzQtmSntpServerStatus_Type.__name__ = "Integer32"
_HzQtmSntpServerStatus_Object = MibTableColumn
hzQtmSntpServerStatus = _HzQtmSntpServerStatus_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 14, 3, 1, 3),
    _HzQtmSntpServerStatus_Type()
)
hzQtmSntpServerStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzQtmSntpServerStatus.setStatus("current")
_HzQtmSntpServerStratum_Type = Integer32
_HzQtmSntpServerStratum_Object = MibTableColumn
hzQtmSntpServerStratum = _HzQtmSntpServerStratum_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 14, 3, 1, 4),
    _HzQtmSntpServerStratum_Type()
)
hzQtmSntpServerStratum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzQtmSntpServerStratum.setStatus("current")


class _HzQtmSntpRestoreDefault_Type(Integer32):
    """Custom type hzQtmSntpRestoreDefault based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("restore", 1)
    )


_HzQtmSntpRestoreDefault_Type.__name__ = "Integer32"
_HzQtmSntpRestoreDefault_Object = MibScalar
hzQtmSntpRestoreDefault = _HzQtmSntpRestoreDefault_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 14, 4),
    _HzQtmSntpRestoreDefault_Type()
)
hzQtmSntpRestoreDefault.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzQtmSntpRestoreDefault.setStatus("current")
_HzQtmLogs_ObjectIdentity = ObjectIdentity
hzQtmLogs = _HzQtmLogs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 15)
)


class _HzQtmEventLogEnable_Type(Integer32):
    """Custom type hzQtmEventLogEnable based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_HzQtmEventLogEnable_Type.__name__ = "Integer32"
_HzQtmEventLogEnable_Object = MibScalar
hzQtmEventLogEnable = _HzQtmEventLogEnable_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 15, 1),
    _HzQtmEventLogEnable_Type()
)
hzQtmEventLogEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzQtmEventLogEnable.setStatus("current")


class _HzQtmPerfmLogEnable_Type(Integer32):
    """Custom type hzQtmPerfmLogEnable based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_HzQtmPerfmLogEnable_Type.__name__ = "Integer32"
_HzQtmPerfmLogEnable_Object = MibScalar
hzQtmPerfmLogEnable = _HzQtmPerfmLogEnable_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 15, 2),
    _HzQtmPerfmLogEnable_Type()
)
hzQtmPerfmLogEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzQtmPerfmLogEnable.setStatus("current")


class _HzQtmPerfmLogInterval_Type(DisplayString):
    """Custom type hzQtmPerfmLogInterval based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_HzQtmPerfmLogInterval_Type.__name__ = "DisplayString"
_HzQtmPerfmLogInterval_Object = MibScalar
hzQtmPerfmLogInterval = _HzQtmPerfmLogInterval_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 15, 3),
    _HzQtmPerfmLogInterval_Type()
)
hzQtmPerfmLogInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzQtmPerfmLogInterval.setStatus("current")
_HzQtmSysLog_ObjectIdentity = ObjectIdentity
hzQtmSysLog = _HzQtmSysLog_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 15, 4)
)


class _HzQtmSysLogEnable_Type(Integer32):
    """Custom type hzQtmSysLogEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_HzQtmSysLogEnable_Type.__name__ = "Integer32"
_HzQtmSysLogEnable_Object = MibScalar
hzQtmSysLogEnable = _HzQtmSysLogEnable_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 15, 4, 1),
    _HzQtmSysLogEnable_Type()
)
hzQtmSysLogEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzQtmSysLogEnable.setStatus("current")
_HzQtmSysLogIpAddress_Type = IpAddress
_HzQtmSysLogIpAddress_Object = MibScalar
hzQtmSysLogIpAddress = _HzQtmSysLogIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 15, 4, 2),
    _HzQtmSysLogIpAddress_Type()
)
hzQtmSysLogIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzQtmSysLogIpAddress.setStatus("current")
_HzQtmRadius_ObjectIdentity = ObjectIdentity
hzQtmRadius = _HzQtmRadius_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 16)
)


class _HzQtmRadiusSuperUserAuthentication_Type(Integer32):
    """Custom type hzQtmRadiusSuperUserAuthentication based on Integer32"""
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


_HzQtmRadiusSuperUserAuthentication_Type.__name__ = "Integer32"
_HzQtmRadiusSuperUserAuthentication_Object = MibScalar
hzQtmRadiusSuperUserAuthentication = _HzQtmRadiusSuperUserAuthentication_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 16, 1),
    _HzQtmRadiusSuperUserAuthentication_Type()
)
hzQtmRadiusSuperUserAuthentication.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzQtmRadiusSuperUserAuthentication.setStatus("current")
_HzQtmRadiusServerTimeOut_Type = Integer32
_HzQtmRadiusServerTimeOut_Object = MibScalar
hzQtmRadiusServerTimeOut = _HzQtmRadiusServerTimeOut_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 16, 2),
    _HzQtmRadiusServerTimeOut_Type()
)
hzQtmRadiusServerTimeOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzQtmRadiusServerTimeOut.setStatus("current")
_HzQtmRadiusServerDeadTime_Type = Integer32
_HzQtmRadiusServerDeadTime_Object = MibScalar
hzQtmRadiusServerDeadTime = _HzQtmRadiusServerDeadTime_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 16, 3),
    _HzQtmRadiusServerDeadTime_Type()
)
hzQtmRadiusServerDeadTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzQtmRadiusServerDeadTime.setStatus("current")
_HzQtmRadiusServerReTransmit_Type = Integer32
_HzQtmRadiusServerReTransmit_Object = MibScalar
hzQtmRadiusServerReTransmit = _HzQtmRadiusServerReTransmit_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 16, 4),
    _HzQtmRadiusServerReTransmit_Type()
)
hzQtmRadiusServerReTransmit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzQtmRadiusServerReTransmit.setStatus("current")
_HzQtmRadiusServerTable_Object = MibTable
hzQtmRadiusServerTable = _HzQtmRadiusServerTable_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 16, 5)
)
if mibBuilder.loadTexts:
    hzQtmRadiusServerTable.setStatus("current")
_HzQtmRadiusServerEntry_Object = MibTableRow
hzQtmRadiusServerEntry = _HzQtmRadiusServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 16, 5, 1)
)
hzQtmRadiusServerEntry.setIndexNames(
    (0, "DRAGONWAVE-HORIZON-QUANTUM-MIB", "hzQtmRadiusServerIndex"),
)
if mibBuilder.loadTexts:
    hzQtmRadiusServerEntry.setStatus("current")
_HzQtmRadiusServerIndex_Type = Integer32
_HzQtmRadiusServerIndex_Object = MibTableColumn
hzQtmRadiusServerIndex = _HzQtmRadiusServerIndex_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 16, 5, 1, 1),
    _HzQtmRadiusServerIndex_Type()
)
hzQtmRadiusServerIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzQtmRadiusServerIndex.setStatus("current")
_HzQtmRadiusCfgdHostIpAddress_Type = IpAddress
_HzQtmRadiusCfgdHostIpAddress_Object = MibTableColumn
hzQtmRadiusCfgdHostIpAddress = _HzQtmRadiusCfgdHostIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 16, 5, 1, 2),
    _HzQtmRadiusCfgdHostIpAddress_Type()
)
hzQtmRadiusCfgdHostIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzQtmRadiusCfgdHostIpAddress.setStatus("current")
_HzQtmRadiusActiveHostIpAddress_Type = IpAddress
_HzQtmRadiusActiveHostIpAddress_Object = MibTableColumn
hzQtmRadiusActiveHostIpAddress = _HzQtmRadiusActiveHostIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 16, 5, 1, 3),
    _HzQtmRadiusActiveHostIpAddress_Type()
)
hzQtmRadiusActiveHostIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzQtmRadiusActiveHostIpAddress.setStatus("current")
_HzQtmSnmpNotifications_ObjectIdentity = ObjectIdentity
hzQtmSnmpNotifications = _HzQtmSnmpNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 21)
)
_HzQtmReserved_ObjectIdentity = ObjectIdentity
hzQtmReserved = _HzQtmReserved_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 999)
)

# Managed Objects groups


# Notification objects

hzQtmLinkDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 21, 1)
)
hzQtmLinkDown.setObjects(
    ("IF-MIB", "ifIndex")
)
if mibBuilder.loadTexts:
    hzQtmLinkDown.setStatus(
        "current"
    )

hzQtmLinkUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 21, 2)
)
hzQtmLinkUp.setObjects(
    ("IF-MIB", "ifIndex")
)
if mibBuilder.loadTexts:
    hzQtmLinkUp.setStatus(
        "current"
    )

hzQtmExplicitAuthenticationFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 21, 3)
)
if mibBuilder.loadTexts:
    hzQtmExplicitAuthenticationFailure.setStatus(
        "current"
    )

hzQtmExplicitAuthenticationFailureCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 21, 4)
)
if mibBuilder.loadTexts:
    hzQtmExplicitAuthenticationFailureCleared.setStatus(
        "current"
    )

hzQtmHitlessAamConfigMisMatch = NotificationType(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 21, 5)
)
hzQtmHitlessAamConfigMisMatch.setObjects(
    ("DRAGONWAVE-HORIZON-QUANTUM-MIB", "hzQtmModemAlarmsIndex")
)
if mibBuilder.loadTexts:
    hzQtmHitlessAamConfigMisMatch.setStatus(
        "current"
    )

hzQtmHitlessAamConfigMisMatchCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 21, 6)
)
hzQtmHitlessAamConfigMisMatchCleared.setObjects(
    ("DRAGONWAVE-HORIZON-QUANTUM-MIB", "hzQtmModemAlarmsIndex")
)
if mibBuilder.loadTexts:
    hzQtmHitlessAamConfigMisMatchCleared.setStatus(
        "current"
    )

hzQtmHitlessAamActive = NotificationType(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 21, 7)
)
hzQtmHitlessAamActive.setObjects(
    ("DRAGONWAVE-HORIZON-QUANTUM-MIB", "hzQtmModemAlarmsIndex")
)
if mibBuilder.loadTexts:
    hzQtmHitlessAamActive.setStatus(
        "current"
    )

hzQtmHitlessAamActiveCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 21, 8)
)
hzQtmHitlessAamActiveCleared.setObjects(
    ("DRAGONWAVE-HORIZON-QUANTUM-MIB", "hzQtmModemAlarmsIndex")
)
if mibBuilder.loadTexts:
    hzQtmHitlessAamActiveCleared.setStatus(
        "current"
    )

hzQtmAtpcConfigMismatch = NotificationType(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 21, 9)
)
if mibBuilder.loadTexts:
    hzQtmAtpcConfigMismatch.setStatus(
        "current"
    )

hzQtmAtpcConfigMismatchCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 21, 10)
)
if mibBuilder.loadTexts:
    hzQtmAtpcConfigMismatchCleared.setStatus(
        "current"
    )

hzQtmSntpServersUnreachable = NotificationType(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 21, 11)
)
if mibBuilder.loadTexts:
    hzQtmSntpServersUnreachable.setStatus(
        "current"
    )

hzQtmSntpServersUnreachableCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 21, 12)
)
if mibBuilder.loadTexts:
    hzQtmSntpServersUnreachableCleared.setStatus(
        "current"
    )

hzQtmFrequencyFileInvalid = NotificationType(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 21, 13)
)
if mibBuilder.loadTexts:
    hzQtmFrequencyFileInvalid.setStatus(
        "current"
    )

hzQtmDroppedFramesThresholdExceeded = NotificationType(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 21, 14)
)
if mibBuilder.loadTexts:
    hzQtmDroppedFramesThresholdExceeded.setStatus(
        "current"
    )

hzQtmDroppedFramesThresholdExceededCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 21, 15)
)
if mibBuilder.loadTexts:
    hzQtmDroppedFramesThresholdExceededCleared.setStatus(
        "current"
    )

hzQtmBwUtilizationThresholdExceeded = NotificationType(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 21, 16)
)
if mibBuilder.loadTexts:
    hzQtmBwUtilizationThresholdExceeded.setStatus(
        "current"
    )

hzQtmBwUtilizationThresholdExceededCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 21, 17)
)
if mibBuilder.loadTexts:
    hzQtmBwUtilizationThresholdExceededCleared.setStatus(
        "current"
    )

hzQtmRlsMismatch = NotificationType(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 21, 18)
)
if mibBuilder.loadTexts:
    hzQtmRlsMismatch.setStatus(
        "current"
    )

hzQtmRlsMismatchCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 21, 19)
)
if mibBuilder.loadTexts:
    hzQtmRlsMismatchCleared.setStatus(
        "current"
    )

hzQtmRlsQueueBasedShutdownActivated = NotificationType(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 21, 20)
)
if mibBuilder.loadTexts:
    hzQtmRlsQueueBasedShutdownActivated.setStatus(
        "current"
    )

hzQtmRlsQueueBasedShutdownActivatedCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 21, 21)
)
if mibBuilder.loadTexts:
    hzQtmRlsQueueBasedShutdownActivatedCleared.setStatus(
        "current"
    )

hzQtmModemRxLossOfSignalLock = NotificationType(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 21, 22)
)
hzQtmModemRxLossOfSignalLock.setObjects(
    ("DRAGONWAVE-HORIZON-QUANTUM-MIB", "hzQtmModemAlarmsIndex")
)
if mibBuilder.loadTexts:
    hzQtmModemRxLossOfSignalLock.setStatus(
        "current"
    )

hzQtmModemRxLossOfSignalLockCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 21, 23)
)
hzQtmModemRxLossOfSignalLockCleared.setObjects(
    ("DRAGONWAVE-HORIZON-QUANTUM-MIB", "hzQtmModemAlarmsIndex")
)
if mibBuilder.loadTexts:
    hzQtmModemRxLossOfSignalLockCleared.setStatus(
        "current"
    )

hzQtmModemTxLossOfSync = NotificationType(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 21, 24)
)
hzQtmModemTxLossOfSync.setObjects(
    ("DRAGONWAVE-HORIZON-QUANTUM-MIB", "hzQtmModemAlarmsIndex")
)
if mibBuilder.loadTexts:
    hzQtmModemTxLossOfSync.setStatus(
        "current"
    )

hzQtmModemTxLossOfSyncCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 21, 25)
)
hzQtmModemTxLossOfSyncCleared.setObjects(
    ("DRAGONWAVE-HORIZON-QUANTUM-MIB", "hzQtmModemAlarmsIndex")
)
if mibBuilder.loadTexts:
    hzQtmModemTxLossOfSyncCleared.setStatus(
        "current"
    )

hzQtmModemSnrBelowThreshold = NotificationType(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 21, 26)
)
hzQtmModemSnrBelowThreshold.setObjects(
    ("DRAGONWAVE-HORIZON-QUANTUM-MIB", "hzQtmModemAlarmsIndex")
)
if mibBuilder.loadTexts:
    hzQtmModemSnrBelowThreshold.setStatus(
        "current"
    )

hzQtmModemSnrBelowThresholdCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 21, 27)
)
hzQtmModemSnrBelowThresholdCleared.setObjects(
    ("DRAGONWAVE-HORIZON-QUANTUM-MIB", "hzQtmModemAlarmsIndex")
)
if mibBuilder.loadTexts:
    hzQtmModemSnrBelowThresholdCleared.setStatus(
        "current"
    )

hzQtmModemEqualizerStressExceedThreshold = NotificationType(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 21, 28)
)
hzQtmModemEqualizerStressExceedThreshold.setObjects(
    ("DRAGONWAVE-HORIZON-QUANTUM-MIB", "hzQtmModemAlarmsIndex")
)
if mibBuilder.loadTexts:
    hzQtmModemEqualizerStressExceedThreshold.setStatus(
        "current"
    )

hzQtmModemEqualizerStressExceedThresholdCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 21, 29)
)
hzQtmModemEqualizerStressExceedThresholdCleared.setObjects(
    ("DRAGONWAVE-HORIZON-QUANTUM-MIB", "hzQtmModemAlarmsIndex")
)
if mibBuilder.loadTexts:
    hzQtmModemEqualizerStressExceedThresholdCleared.setStatus(
        "current"
    )

hzQtmModemChannelizedRslBelowThreshold = NotificationType(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 21, 30)
)
hzQtmModemChannelizedRslBelowThreshold.setObjects(
    ("DRAGONWAVE-HORIZON-QUANTUM-MIB", "hzQtmModemAlarmsIndex")
)
if mibBuilder.loadTexts:
    hzQtmModemChannelizedRslBelowThreshold.setStatus(
        "current"
    )

hzQtmModemChannelizedRslBelowThresholdCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 21, 31)
)
hzQtmModemChannelizedRslBelowThresholdCleared.setObjects(
    ("DRAGONWAVE-HORIZON-QUANTUM-MIB", "hzQtmModemAlarmsIndex")
)
if mibBuilder.loadTexts:
    hzQtmModemChannelizedRslBelowThresholdCleared.setStatus(
        "current"
    )

hzQtmFpgaProgrammingError = NotificationType(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 21, 32)
)
if mibBuilder.loadTexts:
    hzQtmFpgaProgrammingError.setStatus(
        "current"
    )

hzQtmFpgaProgrammingErrorCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 21, 33)
)
if mibBuilder.loadTexts:
    hzQtmFpgaProgrammingErrorCleared.setStatus(
        "current"
    )

hzQtmUserSessionCommenced = NotificationType(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 21, 34)
)
hzQtmUserSessionCommenced.setObjects(
      *(("DRAGONWAVE-HORIZON-QUANTUM-MIB", "hzQtmUserSessionUserName"),
        ("DRAGONWAVE-HORIZON-QUANTUM-MIB", "hzQtmUserSessionUserConnectionType"))
)
if mibBuilder.loadTexts:
    hzQtmUserSessionCommenced.setStatus(
        "current"
    )

hzQtmUserSessionTerminated = NotificationType(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 21, 35)
)
hzQtmUserSessionTerminated.setObjects(
      *(("DRAGONWAVE-HORIZON-QUANTUM-MIB", "hzQtmUserSessionUserName"),
        ("DRAGONWAVE-HORIZON-QUANTUM-MIB", "hzQtmUserSessionUserConnectionType"))
)
if mibBuilder.loadTexts:
    hzQtmUserSessionTerminated.setStatus(
        "current"
    )

hzQtmAtpcTxAtMaxPwr = NotificationType(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 21, 36)
)
hzQtmAtpcTxAtMaxPwr.setObjects(
    ("DRAGONWAVE-HORIZON-QUANTUM-MIB", "hzQtmRadioAlarmsIndex")
)
if mibBuilder.loadTexts:
    hzQtmAtpcTxAtMaxPwr.setStatus(
        "current"
    )

hzQtmAtpcTxAtMaxPwrCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 21, 37)
)
hzQtmAtpcTxAtMaxPwrCleared.setObjects(
    ("DRAGONWAVE-HORIZON-QUANTUM-MIB", "hzQtmRadioAlarmsIndex")
)
if mibBuilder.loadTexts:
    hzQtmAtpcTxAtMaxPwrCleared.setStatus(
        "current"
    )

hzQtmRadioSynthLostLock = NotificationType(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 21, 38)
)
hzQtmRadioSynthLostLock.setObjects(
    ("DRAGONWAVE-HORIZON-QUANTUM-MIB", "hzQtmRadioAlarmsIndex")
)
if mibBuilder.loadTexts:
    hzQtmRadioSynthLostLock.setStatus(
        "current"
    )

hzQtmRadioSynthLostLockCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 21, 39)
)
hzQtmRadioSynthLostLockCleared.setObjects(
    ("DRAGONWAVE-HORIZON-QUANTUM-MIB", "hzQtmRadioAlarmsIndex")
)
if mibBuilder.loadTexts:
    hzQtmRadioSynthLostLockCleared.setStatus(
        "current"
    )

hzQtmRadioLostCommunication = NotificationType(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 21, 40)
)
hzQtmRadioLostCommunication.setObjects(
    ("DRAGONWAVE-HORIZON-QUANTUM-MIB", "hzQtmRadioAlarmsIndex")
)
if mibBuilder.loadTexts:
    hzQtmRadioLostCommunication.setStatus(
        "current"
    )

hzQtmRadioLostCommunicationCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 21, 41)
)
hzQtmRadioLostCommunicationCleared.setObjects(
    ("DRAGONWAVE-HORIZON-QUANTUM-MIB", "hzQtmRadioAlarmsIndex")
)
if mibBuilder.loadTexts:
    hzQtmRadioLostCommunicationCleared.setStatus(
        "current"
    )

hzQtmRadioMismatch = NotificationType(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 21, 42)
)
hzQtmRadioMismatch.setObjects(
    ("DRAGONWAVE-HORIZON-QUANTUM-MIB", "hzQtmRadioAlarmsIndex")
)
if mibBuilder.loadTexts:
    hzQtmRadioMismatch.setStatus(
        "current"
    )

hzQtmRadioMismatchCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 21, 43)
)
hzQtmRadioMismatchCleared.setObjects(
    ("DRAGONWAVE-HORIZON-QUANTUM-MIB", "hzQtmRadioAlarmsIndex")
)
if mibBuilder.loadTexts:
    hzQtmRadioMismatchCleared.setStatus(
        "current"
    )

hzQtmRadioPowerAmp = NotificationType(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 21, 44)
)
hzQtmRadioPowerAmp.setObjects(
    ("DRAGONWAVE-HORIZON-QUANTUM-MIB", "hzQtmRadioAlarmsIndex")
)
if mibBuilder.loadTexts:
    hzQtmRadioPowerAmp.setStatus(
        "current"
    )

hzQtmRadioPowerAmpCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 21, 45)
)
hzQtmRadioPowerAmpCleared.setObjects(
    ("DRAGONWAVE-HORIZON-QUANTUM-MIB", "hzQtmRadioAlarmsIndex")
)
if mibBuilder.loadTexts:
    hzQtmRadioPowerAmpCleared.setStatus(
        "current"
    )

hzQtmRadioExcessiveTxCableLoss = NotificationType(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 21, 46)
)
hzQtmRadioExcessiveTxCableLoss.setObjects(
    ("DRAGONWAVE-HORIZON-QUANTUM-MIB", "hzQtmRadioAlarmsIndex")
)
if mibBuilder.loadTexts:
    hzQtmRadioExcessiveTxCableLoss.setStatus(
        "current"
    )

hzQtmRadioExcessiveTxCableLossCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 21, 47)
)
hzQtmRadioExcessiveTxCableLossCleared.setObjects(
    ("DRAGONWAVE-HORIZON-QUANTUM-MIB", "hzQtmRadioAlarmsIndex")
)
if mibBuilder.loadTexts:
    hzQtmRadioExcessiveTxCableLossCleared.setStatus(
        "current"
    )

hzQtmHiPowerRadioTxDetector = NotificationType(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 21, 48)
)
hzQtmHiPowerRadioTxDetector.setObjects(
    ("DRAGONWAVE-HORIZON-QUANTUM-MIB", "hzQtmRadioAlarmsIndex")
)
if mibBuilder.loadTexts:
    hzQtmHiPowerRadioTxDetector.setStatus(
        "current"
    )

hzQtmHiPowerRadioTxDetectorCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 21, 49)
)
hzQtmHiPowerRadioTxDetectorCleared.setObjects(
    ("DRAGONWAVE-HORIZON-QUANTUM-MIB", "hzQtmRadioAlarmsIndex")
)
if mibBuilder.loadTexts:
    hzQtmHiPowerRadioTxDetectorCleared.setStatus(
        "current"
    )

hzQtmSecondaryRadioIsActive = NotificationType(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 21, 50)
)
hzQtmSecondaryRadioIsActive.setObjects(
    ("DRAGONWAVE-HORIZON-QUANTUM-MIB", "hzQtmRadioAlarmsIndex")
)
if mibBuilder.loadTexts:
    hzQtmSecondaryRadioIsActive.setStatus(
        "current"
    )

hzQtmSecondaryRadioIsActiveCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 21, 51)
)
hzQtmSecondaryRadioIsActiveCleared.setObjects(
    ("DRAGONWAVE-HORIZON-QUANTUM-MIB", "hzQtmRadioAlarmsIndex")
)
if mibBuilder.loadTexts:
    hzQtmSecondaryRadioIsActiveCleared.setStatus(
        "current"
    )

hzQtmRedundancySerialNumberMisMatch = NotificationType(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 21, 52)
)
hzQtmRedundancySerialNumberMisMatch.setObjects(
    ("DRAGONWAVE-HORIZON-QUANTUM-MIB", "hzQtmRadioAlarmsIndex")
)
if mibBuilder.loadTexts:
    hzQtmRedundancySerialNumberMisMatch.setStatus(
        "current"
    )

hzQtmRedundancySerialNumberMisMatchCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 21, 53)
)
hzQtmRedundancySerialNumberMisMatchCleared.setObjects(
    ("DRAGONWAVE-HORIZON-QUANTUM-MIB", "hzQtmRadioAlarmsIndex")
)
if mibBuilder.loadTexts:
    hzQtmRedundancySerialNumberMisMatchCleared.setStatus(
        "current"
    )

hzQtmRadioFirmwareMismatch = NotificationType(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 21, 54)
)
hzQtmRadioFirmwareMismatch.setObjects(
    ("DRAGONWAVE-HORIZON-QUANTUM-MIB", "hzQtmRadioAlarmsIndex")
)
if mibBuilder.loadTexts:
    hzQtmRadioFirmwareMismatch.setStatus(
        "current"
    )

hzQtmRadioFirmwareMismatchCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 21, 55)
)
hzQtmRadioFirmwareMismatchCleared.setObjects(
    ("DRAGONWAVE-HORIZON-QUANTUM-MIB", "hzQtmRadioAlarmsIndex")
)
if mibBuilder.loadTexts:
    hzQtmRadioFirmwareMismatchCleared.setStatus(
        "current"
    )

hzQtmSecondaryRadioNotdetected = NotificationType(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 21, 56)
)
hzQtmSecondaryRadioNotdetected.setObjects(
    ("DRAGONWAVE-HORIZON-QUANTUM-MIB", "hzQtmRadioAlarmsIndex")
)
if mibBuilder.loadTexts:
    hzQtmSecondaryRadioNotdetected.setStatus(
        "current"
    )

hzQtmSecondaryRadioNotdetectedCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 21, 57)
)
hzQtmSecondaryRadioNotdetectedCleared.setObjects(
    ("DRAGONWAVE-HORIZON-QUANTUM-MIB", "hzQtmRadioAlarmsIndex")
)
if mibBuilder.loadTexts:
    hzQtmSecondaryRadioNotdetectedCleared.setStatus(
        "current"
    )

hzQtmPrimaryRadioNotdetected = NotificationType(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 21, 58)
)
hzQtmPrimaryRadioNotdetected.setObjects(
    ("DRAGONWAVE-HORIZON-QUANTUM-MIB", "hzQtmRadioAlarmsIndex")
)
if mibBuilder.loadTexts:
    hzQtmPrimaryRadioNotdetected.setStatus(
        "current"
    )

hzQtmPrimaryRadioNotdetectedCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 21, 59)
)
hzQtmPrimaryRadioNotdetectedCleared.setObjects(
    ("DRAGONWAVE-HORIZON-QUANTUM-MIB", "hzQtmRadioAlarmsIndex")
)
if mibBuilder.loadTexts:
    hzQtmPrimaryRadioNotdetectedCleared.setStatus(
        "current"
    )

hzQtmFaultyPrimaryRadio = NotificationType(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 21, 60)
)
hzQtmFaultyPrimaryRadio.setObjects(
    ("DRAGONWAVE-HORIZON-QUANTUM-MIB", "hzQtmRadioAlarmsIndex")
)
if mibBuilder.loadTexts:
    hzQtmFaultyPrimaryRadio.setStatus(
        "current"
    )

hzQtmFaultyPrimaryRadioCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 21, 61)
)
hzQtmFaultyPrimaryRadioCleared.setObjects(
    ("DRAGONWAVE-HORIZON-QUANTUM-MIB", "hzQtmRadioAlarmsIndex")
)
if mibBuilder.loadTexts:
    hzQtmFaultyPrimaryRadioCleared.setStatus(
        "current"
    )

hzQtmRadioExcessiveTxCableLossChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 21, 62)
)
hzQtmRadioExcessiveTxCableLossChange.setObjects(
    ("DRAGONWAVE-HORIZON-QUANTUM-MIB", "hzQtmRadioAlarmsIndex")
)
if mibBuilder.loadTexts:
    hzQtmRadioExcessiveTxCableLossChange.setStatus(
        "current"
    )

hzQtmRadioExcessiveTxCableLossChangeCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 21, 63)
)
hzQtmRadioExcessiveTxCableLossChangeCleared.setObjects(
    ("DRAGONWAVE-HORIZON-QUANTUM-MIB", "hzQtmRadioAlarmsIndex")
)
if mibBuilder.loadTexts:
    hzQtmRadioExcessiveTxCableLossChangeCleared.setStatus(
        "current"
    )

hzQtmExcessiveRxCableLoss = NotificationType(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 21, 64)
)
hzQtmExcessiveRxCableLoss.setObjects(
    ("DRAGONWAVE-HORIZON-QUANTUM-MIB", "hzQtmRadioAlarmsIndex")
)
if mibBuilder.loadTexts:
    hzQtmExcessiveRxCableLoss.setStatus(
        "current"
    )

hzQtmExcessiveRxCableLossCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 21, 65)
)
hzQtmExcessiveRxCableLossCleared.setObjects(
    ("DRAGONWAVE-HORIZON-QUANTUM-MIB", "hzQtmRadioAlarmsIndex")
)
if mibBuilder.loadTexts:
    hzQtmExcessiveRxCableLossCleared.setStatus(
        "current"
    )

hzQtmRedundancyPrimaryPortNotSet = NotificationType(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 21, 66)
)
if mibBuilder.loadTexts:
    hzQtmRedundancyPrimaryPortNotSet.setStatus(
        "current"
    )

hzQtmRedundancyPrimaryPortNotSetCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 21, 67)
)
if mibBuilder.loadTexts:
    hzQtmRedundancyPrimaryPortNotSetCleared.setStatus(
        "current"
    )

hzQtmRedundancySecondaryPortIsActive = NotificationType(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 21, 68)
)
if mibBuilder.loadTexts:
    hzQtmRedundancySecondaryPortIsActive.setStatus(
        "current"
    )

hzQtmRedundancySecondaryPortIsActiveCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 21, 69)
)
if mibBuilder.loadTexts:
    hzQtmRedundancySecondaryPortIsActiveCleared.setStatus(
        "current"
    )

hzQtmRedundancyPrimaryPortFaulty = NotificationType(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 21, 70)
)
if mibBuilder.loadTexts:
    hzQtmRedundancyPrimaryPortFaulty.setStatus(
        "current"
    )

hzQtmRedundancyPrimaryPortFaultyCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 21, 71)
)
if mibBuilder.loadTexts:
    hzQtmRedundancyPrimaryPortFaultyCleared.setStatus(
        "current"
    )

hzQtmRedundancySecondaryPortFaulty = NotificationType(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 21, 72)
)
if mibBuilder.loadTexts:
    hzQtmRedundancySecondaryPortFaulty.setStatus(
        "current"
    )

hzQtmRedundancySecondaryPortFaultyCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 21, 73)
)
if mibBuilder.loadTexts:
    hzQtmRedundancySecondaryPortFaultyCleared.setStatus(
        "current"
    )

hzQtmFanFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 21, 74)
)
if mibBuilder.loadTexts:
    hzQtmFanFailed.setStatus(
        "current"
    )

hzQtmFanFailureCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 21, 75)
)
if mibBuilder.loadTexts:
    hzQtmFanFailureCleared.setStatus(
        "current"
    )

hzQtmModemRlsShutdownActivated = NotificationType(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 21, 76)
)
hzQtmModemRlsShutdownActivated.setObjects(
    ("DRAGONWAVE-HORIZON-QUANTUM-MIB", "hzQtmModemAlarmsIndex")
)
if mibBuilder.loadTexts:
    hzQtmModemRlsShutdownActivated.setStatus(
        "current"
    )

hzQtmModemRlsShutdownActivatedCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 21, 77)
)
hzQtmModemRlsShutdownActivatedCleared.setObjects(
    ("DRAGONWAVE-HORIZON-QUANTUM-MIB", "hzQtmModemAlarmsIndex")
)
if mibBuilder.loadTexts:
    hzQtmModemRlsShutdownActivatedCleared.setStatus(
        "current"
    )

hzQtmRadioUnitHwChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 21, 78)
)
hzQtmRadioUnitHwChanged.setObjects(
    ("DRAGONWAVE-HORIZON-QUANTUM-MIB", "hzQtmRadioAlarmsIndex")
)
if mibBuilder.loadTexts:
    hzQtmRadioUnitHwChanged.setStatus(
        "current"
    )

hzQtmRadioSwDownloadFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 21, 79)
)
hzQtmRadioSwDownloadFailed.setObjects(
    ("DRAGONWAVE-HORIZON-QUANTUM-MIB", "hzQtmRadioAlarmsIndex")
)
if mibBuilder.loadTexts:
    hzQtmRadioSwDownloadFailed.setStatus(
        "current"
    )

hzQtmRadioSwDownloadFailedCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 21, 80)
)
hzQtmRadioSwDownloadFailedCleared.setObjects(
    ("DRAGONWAVE-HORIZON-QUANTUM-MIB", "hzQtmRadioAlarmsIndex")
)
if mibBuilder.loadTexts:
    hzQtmRadioSwDownloadFailedCleared.setStatus(
        "current"
    )

hzQtmRadioRestartedOK = NotificationType(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 21, 81)
)
hzQtmRadioRestartedOK.setObjects(
    ("DRAGONWAVE-HORIZON-QUANTUM-MIB", "hzQtmRadioAlarmsIndex")
)
if mibBuilder.loadTexts:
    hzQtmRadioRestartedOK.setStatus(
        "current"
    )

hzQtmMibChangeNotSaved = NotificationType(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 21, 82)
)
if mibBuilder.loadTexts:
    hzQtmMibChangeNotSaved.setStatus(
        "current"
    )

hzQtmMibChangeNotSavedCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 21, 83)
)
if mibBuilder.loadTexts:
    hzQtmMibChangeNotSavedCleared.setStatus(
        "current"
    )

hzQtmRadioDrainCurrent = NotificationType(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 21, 84)
)
hzQtmRadioDrainCurrent.setObjects(
    ("DRAGONWAVE-HORIZON-QUANTUM-MIB", "hzQtmRadioAlarmsIndex")
)
if mibBuilder.loadTexts:
    hzQtmRadioDrainCurrent.setStatus(
        "current"
    )

hzQtmRadioDrainCurrentCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 21, 85)
)
hzQtmRadioDrainCurrentCleared.setObjects(
    ("DRAGONWAVE-HORIZON-QUANTUM-MIB", "hzQtmRadioAlarmsIndex")
)
if mibBuilder.loadTexts:
    hzQtmRadioDrainCurrentCleared.setStatus(
        "current"
    )

hzQtmIFSynthLostLock = NotificationType(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 21, 86)
)
hzQtmIFSynthLostLock.setObjects(
    ("DRAGONWAVE-HORIZON-QUANTUM-MIB", "hzQtmIFPathIndex")
)
if mibBuilder.loadTexts:
    hzQtmIFSynthLostLock.setStatus(
        "current"
    )

hzQtmIFSynthLostLockCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 21, 87)
)
hzQtmIFSynthLostLockCleared.setObjects(
    ("DRAGONWAVE-HORIZON-QUANTUM-MIB", "hzQtmIFPathIndex")
)
if mibBuilder.loadTexts:
    hzQtmIFSynthLostLockCleared.setStatus(
        "current"
    )

hzQtmInvalidSystemConfig = NotificationType(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 21, 88)
)
if mibBuilder.loadTexts:
    hzQtmInvalidSystemConfig.setStatus(
        "current"
    )

hzQtmInvalidSystemConfigCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 21, 89)
)
if mibBuilder.loadTexts:
    hzQtmInvalidSystemConfigCleared.setStatus(
        "current"
    )

hzQtmHitlessAamEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 21, 90)
)
hzQtmHitlessAamEvent.setObjects(
    ("DRAGONWAVE-HORIZON-QUANTUM-MIB", "hzQtmModemAlarmsIndex")
)
if mibBuilder.loadTexts:
    hzQtmHitlessAamEvent.setStatus(
        "current"
    )

hzQtmModemXPICEquStressExceedThreshold = NotificationType(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 21, 91)
)
hzQtmModemXPICEquStressExceedThreshold.setObjects(
    ("DRAGONWAVE-HORIZON-QUANTUM-MIB", "hzQtmModemAlarmsIndex")
)
if mibBuilder.loadTexts:
    hzQtmModemXPICEquStressExceedThreshold.setStatus(
        "current"
    )

hzQtmModemXPICEquStressExceedThresholdCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 21, 92)
)
hzQtmModemXPICEquStressExceedThresholdCleared.setObjects(
    ("DRAGONWAVE-HORIZON-QUANTUM-MIB", "hzQtmModemAlarmsIndex")
)
if mibBuilder.loadTexts:
    hzQtmModemXPICEquStressExceedThresholdCleared.setStatus(
        "current"
    )

hzQtmPartnerNodeAlarmIndication = NotificationType(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 21, 93)
)
if mibBuilder.loadTexts:
    hzQtmPartnerNodeAlarmIndication.setStatus(
        "current"
    )

hzQtmPartnerNodeAlarmIndicationCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 21, 94)
)
if mibBuilder.loadTexts:
    hzQtmPartnerNodeAlarmIndicationCleared.setStatus(
        "current"
    )

hzQtmBandwidthDoublingInvalidLinkConfig = NotificationType(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 21, 95)
)
if mibBuilder.loadTexts:
    hzQtmBandwidthDoublingInvalidLinkConfig.setStatus(
        "current"
    )

hzQtmBandwidthDoublingInvalidLinkConfigCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 21, 96)
)
if mibBuilder.loadTexts:
    hzQtmBandwidthDoublingInvalidLinkConfigCleared.setStatus(
        "current"
    )

hzQtmBandwidthDoublingWrongPortConnected = NotificationType(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 21, 97)
)
if mibBuilder.loadTexts:
    hzQtmBandwidthDoublingWrongPortConnected.setStatus(
        "current"
    )

hzQtmBandwidthDoublingWrongPortConnectedCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 21, 98)
)
if mibBuilder.loadTexts:
    hzQtmBandwidthDoublingWrongPortConnectedCleared.setStatus(
        "current"
    )

hzQtmRadioPowerOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 21, 99)
)
if mibBuilder.loadTexts:
    hzQtmRadioPowerOff.setStatus(
        "current"
    )

hzQtmRadioPowerOffCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 21, 100)
)
hzQtmRadioPowerOffCleared.setObjects(
    ("DRAGONWAVE-HORIZON-QUANTUM-MIB", "hzQtmRadioAlarmsIndex")
)
if mibBuilder.loadTexts:
    hzQtmRadioPowerOffCleared.setStatus(
        "current"
    )

hzQtmSynceLostLock = NotificationType(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 21, 101)
)
if mibBuilder.loadTexts:
    hzQtmSynceLostLock.setStatus(
        "current"
    )

hzQtmSynceLostLockCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 21, 102)
)
if mibBuilder.loadTexts:
    hzQtmSynceLostLockCleared.setStatus(
        "current"
    )

hzQtmSynceSecondarySourceInUse = NotificationType(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 21, 103)
)
if mibBuilder.loadTexts:
    hzQtmSynceSecondarySourceInUse.setStatus(
        "current"
    )

hzQtmSynceSecondarySourceInUseCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 7262, 2, 4, 21, 104)
)
if mibBuilder.loadTexts:
    hzQtmSynceSecondarySourceInUseCleared.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "DRAGONWAVE-HORIZON-QUANTUM-MIB",
    **{"horizonQuantum": horizonQuantum,
       "hzQtmSystem": hzQtmSystem,
       "hzQtmSysGeneral": hzQtmSysGeneral,
       "hzQtmResetSystem": hzQtmResetSystem,
       "hzQtmSaveMIB": hzQtmSaveMIB,
       "hzQtmOperStatus": hzQtmOperStatus,
       "hzQtmAirInterfaceEncryption": hzQtmAirInterfaceEncryption,
       "hzQtmSystemCapacityOption": hzQtmSystemCapacityOption,
       "hzQtmSystemLedStatus": hzQtmSystemLedStatus,
       "hzQtmSaveL2SwConfig": hzQtmSaveL2SwConfig,
       "hzQtmIduTemperature": hzQtmIduTemperature,
       "hzQtmSysUpgradeSpeed": hzQtmSysUpgradeSpeed,
       "hzQtmLicensedSpeedUpgradeSpeedAndKey": hzQtmLicensedSpeedUpgradeSpeedAndKey,
       "hzQtmLicensedSpeedCount": hzQtmLicensedSpeedCount,
       "hzQtmSysDowngradeSpeed": hzQtmSysDowngradeSpeed,
       "hzQtmLicensedSpeedDowngradeSpeed": hzQtmLicensedSpeedDowngradeSpeed,
       "hzQtmLicensedSpeedCountUsedForKey": hzQtmLicensedSpeedCountUsedForKey,
       "hzQtmLicensedSpeedConfirmationKey": hzQtmLicensedSpeedConfirmationKey,
       "hzQtmSysDowngradeSpeedDecrement": hzQtmSysDowngradeSpeedDecrement,
       "hzQtmSysSpeed": hzQtmSysSpeed,
       "hzQtmSystemCurrentSpeed": hzQtmSystemCurrentSpeed,
       "hzQtmSystemLicensedSpeed": hzQtmSystemLicensedSpeed,
       "hzQtmSystemModeTable": hzQtmSystemModeTable,
       "hzQtmSystemModeEntry": hzQtmSystemModeEntry,
       "hzQtmSystemModeIndex": hzQtmSystemModeIndex,
       "hzQtmSystemModeId": hzQtmSystemModeId,
       "hzQtmSystemModeName": hzQtmSystemModeName,
       "hzQtmSystemModeProgrammed": hzQtmSystemModeProgrammed,
       "hzQtmInventory": hzQtmInventory,
       "hzQtmHwInventory": hzQtmHwInventory,
       "hzQtmFrequencyFilePartNumber": hzQtmFrequencyFilePartNumber,
       "hzQtmUnitSerialNo": hzQtmUnitSerialNo,
       "hzQtmUnitAssemblylNo": hzQtmUnitAssemblylNo,
       "hzQtmCcaSerialNo": hzQtmCcaSerialNo,
       "hzQtmCcaPartNo": hzQtmCcaPartNo,
       "hzQtmRadio1SerialNo": hzQtmRadio1SerialNo,
       "hzQtmRadio2SerialNo": hzQtmRadio2SerialNo,
       "hzQtmRadio1HardwareId": hzQtmRadio1HardwareId,
       "hzQtmRadio2HardwareId": hzQtmRadio2HardwareId,
       "hzQtmRadio1HardwareType": hzQtmRadio1HardwareType,
       "hzQtmRadio2HardwareType": hzQtmRadio2HardwareType,
       "hzQtmSwInventory": hzQtmSwInventory,
       "hzQtmSwInvAppOmniVersionNo": hzQtmSwInvAppOmniVersionNo,
       "hzQtmSwInvAppFirmwareVersionNo": hzQtmSwInvAppFirmwareVersionNo,
       "hzQtmSwInvFrequencyFileVersionNo": hzQtmSwInvFrequencyFileVersionNo,
       "hzQtmSwInvMibVersionNo": hzQtmSwInvMibVersionNo,
       "hzQtmSwInvRadioFirmware1VersionNo": hzQtmSwInvRadioFirmware1VersionNo,
       "hzQtmSwInvRadioFirmware2VersionNo": hzQtmSwInvRadioFirmware2VersionNo,
       "hzQtmSwInvAppSoftwareVersionNo": hzQtmSwInvAppSoftwareVersionNo,
       "hzQtmSwInvBootloaderVersionNo": hzQtmSwInvBootloaderVersionNo,
       "hzQtmSwInvSupportingAppVersionNo": hzQtmSwInvSupportingAppVersionNo,
       "hzQtmSwInvOperatingSystemVersionNo": hzQtmSwInvOperatingSystemVersionNo,
       "hzQtmSwInvRadio1CurrentFirmwareVersionNo": hzQtmSwInvRadio1CurrentFirmwareVersionNo,
       "hzQtmSwInvRadio2CurrentFirmwareVersionNo": hzQtmSwInvRadio2CurrentFirmwareVersionNo,
       "hzQtmAtpc": hzQtmAtpc,
       "hzQtmAtpcEnable": hzQtmAtpcEnable,
       "hzQtmAtpcStatus": hzQtmAtpcStatus,
       "hzQtmAtpcCoordinatedPower": hzQtmAtpcCoordinatedPower,
       "hzQtmHitlessAam": hzQtmHitlessAam,
       "hzQtmHitlessAamStatus": hzQtmHitlessAamStatus,
       "hzQtmHitlessAamManualMode": hzQtmHitlessAamManualMode,
       "hzQtmHitlessAamTable": hzQtmHitlessAamTable,
       "hzQtmHitlessAamEntry": hzQtmHitlessAamEntry,
       "hzQtmHitlessAamIndex": hzQtmHitlessAamIndex,
       "hzQtmHitlessAamCurrentMode": hzQtmHitlessAamCurrentMode,
       "hzQtmHitlessAamDiagnostics": hzQtmHitlessAamDiagnostics,
       "hzQtmHitlessAamModem1Diagnose": hzQtmHitlessAamModem1Diagnose,
       "hzQtmHitlessAamModem1DiagnosticResult": hzQtmHitlessAamModem1DiagnosticResult,
       "hzQtmHitlessAamModem2Diagnose": hzQtmHitlessAamModem2Diagnose,
       "hzQtmHitlessAamModem2DiagnosticResult": hzQtmHitlessAamModem2DiagnosticResult,
       "hzQtmHitlessAamMaxMode": hzQtmHitlessAamMaxMode,
       "hzQtmHitlessAamMinMode": hzQtmHitlessAamMinMode,
       "hzQtmPeerSysInfo": hzQtmPeerSysInfo,
       "hzQtmPeerMacAddress": hzQtmPeerMacAddress,
       "hzQtmPeerIpAddress": hzQtmPeerIpAddress,
       "hzQtmPeerSubnetMask": hzQtmPeerSubnetMask,
       "hzQtmBac": hzQtmBac,
       "hzQtmBacTable": hzQtmBacTable,
       "hzQtmBacEntry": hzQtmBacEntry,
       "hzQtmBacQIndex": hzQtmBacQIndex,
       "hzQtmBacQEnable": hzQtmBacQEnable,
       "hzQtmBacQBlockSize": hzQtmBacQBlockSize,
       "hzQtmSysDiagnostics": hzQtmSysDiagnostics,
       "hzQtmIFPath1LoopbackAndTimeout": hzQtmIFPath1LoopbackAndTimeout,
       "hzQtmIFPath2LoopbackAndTimeout": hzQtmIFPath2LoopbackAndTimeout,
       "hzQtmRadio1LoopbackAndTimeout": hzQtmRadio1LoopbackAndTimeout,
       "hzQtmRadio2LoopbackAndTimeout": hzQtmRadio2LoopbackAndTimeout,
       "hzQtmSysLicensedFeatureGroups": hzQtmSysLicensedFeatureGroups,
       "hzQtmSysUpgradeFeatureGroupsTable": hzQtmSysUpgradeFeatureGroupsTable,
       "hzQtmSysUpgradeFeatureGroupsEntry": hzQtmSysUpgradeFeatureGroupsEntry,
       "hzQtmUpgradeLicensedFeatureIndex": hzQtmUpgradeLicensedFeatureIndex,
       "hzQtmUpgradeLicensedFeatureKey": hzQtmUpgradeLicensedFeatureKey,
       "hzQtmUpgradeLicensedFeatureCount": hzQtmUpgradeLicensedFeatureCount,
       "hzQtmSysDowngradeFeatureGroupsTable": hzQtmSysDowngradeFeatureGroupsTable,
       "hzQtmSysDowngradeFeatureGroupsEntry": hzQtmSysDowngradeFeatureGroupsEntry,
       "hzQtmDowngradeLicensedFeatureIndex": hzQtmDowngradeLicensedFeatureIndex,
       "hzQtmDowngradeLicensedFeature": hzQtmDowngradeLicensedFeature,
       "hzQtmDowngradeLicensedFeatureCount": hzQtmDowngradeLicensedFeatureCount,
       "hzQtmDowngradeLicensedFeatureKey": hzQtmDowngradeLicensedFeatureKey,
       "hzQtmSysLicensedFeatureGroupsTable": hzQtmSysLicensedFeatureGroupsTable,
       "hzQtmSysLicensedFeatureGroupsEntry": hzQtmSysLicensedFeatureGroupsEntry,
       "hzQtmSysLicensedFeatureGroupIndex": hzQtmSysLicensedFeatureGroupIndex,
       "hzQtmSysLicensedFeatureGroup": hzQtmSysLicensedFeatureGroup,
       "hzQtmSysLicensedFeatureGroupStatus": hzQtmSysLicensedFeatureGroupStatus,
       "hzQtmXpic": hzQtmXpic,
       "hzQtmXpicStatus": hzQtmXpicStatus,
       "hzQtmXpicActualStatus": hzQtmXpicActualStatus,
       "hzQtmXpicMode": hzQtmXpicMode,
       "hzQtmPlcm": hzQtmPlcm,
       "hzQtmPlcmMode": hzQtmPlcmMode,
       "hzQtmPlcmConfigQtmAsDuo": hzQtmPlcmConfigQtmAsDuo,
       "hzQtmPlcmPeerOmniVersionTable": hzQtmPlcmPeerOmniVersionTable,
       "hzQtmPlcmPeerOmniVersionEntry": hzQtmPlcmPeerOmniVersionEntry,
       "hzQtmPlcmPeerOmniVersionIndex": hzQtmPlcmPeerOmniVersionIndex,
       "hzQtmPlcmPeerOmniVersionName": hzQtmPlcmPeerOmniVersionName,
       "hzQtmPlcmPeerOmniVersionProgrammed": hzQtmPlcmPeerOmniVersionProgrammed,
       "hzQtmPlcmMgtInterface": hzQtmPlcmMgtInterface,
       "hzQtmPlcmDataPort": hzQtmPlcmDataPort,
       "hzQtmPlcmDataVlanTag": hzQtmPlcmDataVlanTag,
       "hzQtmPlcmMgmtPort": hzQtmPlcmMgmtPort,
       "hzQtmPlcmMgmtVlanTagging": hzQtmPlcmMgmtVlanTagging,
       "hzQtmPlcmMgmtVlanTag": hzQtmPlcmMgmtVlanTag,
       "hzQtmPlcmMgmtTagPriority": hzQtmPlcmMgmtTagPriority,
       "hzQtmPlcmApplySaveResetSystem": hzQtmPlcmApplySaveResetSystem,
       "hzQtmBandwidthDoubling": hzQtmBandwidthDoubling,
       "hzQtmBandwidthDoublingMode": hzQtmBandwidthDoublingMode,
       "hzQtmBandwidthDoublingActualMode": hzQtmBandwidthDoublingActualMode,
       "hzQtmBandwidthDoublingPort": hzQtmBandwidthDoublingPort,
       "hzQtmBandwidthDoublingActualPort": hzQtmBandwidthDoublingActualPort,
       "hzQtmSyncE": hzQtmSyncE,
       "hzQtmSyncEMode": hzQtmSyncEMode,
       "hzQtmSyncEPrimarySource": hzQtmSyncEPrimarySource,
       "hzQtmSyncESecondarySource": hzQtmSyncESecondarySource,
       "hzQtmSyncEMemberPorts": hzQtmSyncEMemberPorts,
       "hzQtmSyncEForcedHoldover": hzQtmSyncEForcedHoldover,
       "hzQtmSyncERevertive": hzQtmSyncERevertive,
       "hzQtmSyncEClockSource": hzQtmSyncEClockSource,
       "hzQtmSyncEAcquisitionStatus": hzQtmSyncEAcquisitionStatus,
       "hzQtmSyncEWanderFilter": hzQtmSyncEWanderFilter,
       "hzQtmAuthentication": hzQtmAuthentication,
       "hzQtmUniquePeerAuthenticationKey": hzQtmUniquePeerAuthenticationKey,
       "hzQtmPeerDetectedSerialNumber": hzQtmPeerDetectedSerialNumber,
       "hzQtmAuthenticationMode": hzQtmAuthenticationMode,
       "hzQtmAuthenticationFailureAction": hzQtmAuthenticationFailureAction,
       "hzQtmPeerAuthenticationStatus": hzQtmPeerAuthenticationStatus,
       "hzQtmGroupAuthenticationKey": hzQtmGroupAuthenticationKey,
       "hzQtmNetworkManagement": hzQtmNetworkManagement,
       "hzQtmMacAddress": hzQtmMacAddress,
       "hzQtmIpAddress": hzQtmIpAddress,
       "hzQtmSubnetMask": hzQtmSubnetMask,
       "hzQtmDefaultGateway": hzQtmDefaultGateway,
       "hzQtmTelnetAccessMode": hzQtmTelnetAccessMode,
       "hzQtmSshAccessMode": hzQtmSshAccessMode,
       "hzQtmNetworkManagementInterface": hzQtmNetworkManagementInterface,
       "hzQtmNetMgmtPortList": hzQtmNetMgmtPortList,
       "hzQtmNetMgmtVlanTagId": hzQtmNetMgmtVlanTagId,
       "hzQtmNetMgmtVlanTagPriority": hzQtmNetMgmtVlanTagPriority,
       "hzQtmNetworkInterface": hzQtmNetworkInterface,
       "hzQtmEnetPort": hzQtmEnetPort,
       "hzQtmEnetPortConfigTable": hzQtmEnetPortConfigTable,
       "hzQtmEnetPortConfigEntry": hzQtmEnetPortConfigEntry,
       "hzQtmEnetPortIndex": hzQtmEnetPortIndex,
       "hzQtmEnetPortName": hzQtmEnetPortName,
       "hzQtmEnetPortAutoNegotiation": hzQtmEnetPortAutoNegotiation,
       "hzQtmEnetPortSpeed": hzQtmEnetPortSpeed,
       "hzQtmEnetPortDuplex": hzQtmEnetPortDuplex,
       "hzQtmEnetPortMedia": hzQtmEnetPortMedia,
       "hzQtmEnetPortAdminState": hzQtmEnetPortAdminState,
       "hzQtmEnetPortPauseFrame": hzQtmEnetPortPauseFrame,
       "hzQtmEnetPortMaxFrameSize": hzQtmEnetPortMaxFrameSize,
       "hzQtmEnetPortStatusTable": hzQtmEnetPortStatusTable,
       "hzQtmEnetPortStatusEntry": hzQtmEnetPortStatusEntry,
       "hzQtmEnetPortStatusIndex": hzQtmEnetPortStatusIndex,
       "hzQtmEnetPortLinkStatus": hzQtmEnetPortLinkStatus,
       "hzQtmEnetPortAutoNegotiationStatus": hzQtmEnetPortAutoNegotiationStatus,
       "hzQtmEnetPortSpeedStatus": hzQtmEnetPortSpeedStatus,
       "hzQtmEnetPortDuplexStatus": hzQtmEnetPortDuplexStatus,
       "hzQtmEnetPortMediaStatus": hzQtmEnetPortMediaStatus,
       "hzQtmEnetPortStatsTable": hzQtmEnetPortStatsTable,
       "hzQtmEnetPortStatsEntry": hzQtmEnetPortStatsEntry,
       "hzQtmEnetPortStatsIndex": hzQtmEnetPortStatsIndex,
       "hzQtmEnetPortRxBytes": hzQtmEnetPortRxBytes,
       "hzQtmEnetPortRxUcastPkts": hzQtmEnetPortRxUcastPkts,
       "hzQtmEnetPortRxNUcastPkts": hzQtmEnetPortRxNUcastPkts,
       "hzQtmEnetPortRxDiscards": hzQtmEnetPortRxDiscards,
       "hzQtmEnetPortRxErrors": hzQtmEnetPortRxErrors,
       "hzQtmEnetPortRxUnknownProtos": hzQtmEnetPortRxUnknownProtos,
       "hzQtmEnetPortTxBytes": hzQtmEnetPortTxBytes,
       "hzQtmEnetPortTxUcastPkts": hzQtmEnetPortTxUcastPkts,
       "hzQtmEnetPortTxNUcastPkts": hzQtmEnetPortTxNUcastPkts,
       "hzQtmEnetPortTxDiscards": hzQtmEnetPortTxDiscards,
       "hzQtmEnetPortTxErrors": hzQtmEnetPortTxErrors,
       "hzQtmAggregatedEnetPort": hzQtmAggregatedEnetPort,
       "hzQtmAggregatedEnetPortConfig": hzQtmAggregatedEnetPortConfig,
       "hzQtmEnetPortDroppedEnetFramesThresholdParameters": hzQtmEnetPortDroppedEnetFramesThresholdParameters,
       "hzQtmEnetPortBWUtilizationThresholdParameters": hzQtmEnetPortBWUtilizationThresholdParameters,
       "hzQtmAggregatedEnetPortStats": hzQtmAggregatedEnetPortStats,
       "hzQtmAggPortTxFrames": hzQtmAggPortTxFrames,
       "hzQtmAggPortTxBytes": hzQtmAggPortTxBytes,
       "hzQtmAggPortRxFramesOK": hzQtmAggPortRxFramesOK,
       "hzQtmAggPortRxBytesOK": hzQtmAggPortRxBytesOK,
       "hzQtmAggPortRxFramesError": hzQtmAggPortRxFramesError,
       "hzQtmAggPortBWUtilization": hzQtmAggPortBWUtilization,
       "hzQtmAggPortIngressDataRate": hzQtmAggPortIngressDataRate,
       "hzQtmAggPortEgressDataRate": hzQtmAggPortEgressDataRate,
       "hzQtmAggPortFramesInQueue1": hzQtmAggPortFramesInQueue1,
       "hzQtmAggPortFramesInQueue2": hzQtmAggPortFramesInQueue2,
       "hzQtmAggPortFramesInQueue3": hzQtmAggPortFramesInQueue3,
       "hzQtmAggPortFramesInQueue4": hzQtmAggPortFramesInQueue4,
       "hzQtmAggPortFramesInQueue1Discarded": hzQtmAggPortFramesInQueue1Discarded,
       "hzQtmAggPortFramesInQueue2Discarded": hzQtmAggPortFramesInQueue2Discarded,
       "hzQtmAggPortFramesInQueue3Discarded": hzQtmAggPortFramesInQueue3Discarded,
       "hzQtmAggPortFramesInQueue4Discarded": hzQtmAggPortFramesInQueue4Discarded,
       "hzQtmAggPortFramesInQueueC": hzQtmAggPortFramesInQueueC,
       "hzQtmAggPortFramesInQueueCDiscarded": hzQtmAggPortFramesInQueueCDiscarded,
       "hzQtmWirelessInterface": hzQtmWirelessInterface,
       "hzQtmWirelessInterfaceNames": hzQtmWirelessInterfaceNames,
       "hzQtmWirelessInterfaceNameTable": hzQtmWirelessInterfaceNameTable,
       "hzQtmWirelessInterfaceNameEntry": hzQtmWirelessInterfaceNameEntry,
       "hzQtmWirelessInterfaceNameIndex": hzQtmWirelessInterfaceNameIndex,
       "hzQtmWirelessInterfaceName": hzQtmWirelessInterfaceName,
       "hzQtmWirelessInterfaceModems": hzQtmWirelessInterfaceModems,
       "hzQtmModemTable": hzQtmModemTable,
       "hzQtmModemEntry": hzQtmModemEntry,
       "hzQtmModemIndex": hzQtmModemIndex,
       "hzQtmModemOperStatus": hzQtmModemOperStatus,
       "hzQtmModemChannelizedRSL": hzQtmModemChannelizedRSL,
       "hzQtmModemChannelizedRSLUnsignedInt": hzQtmModemChannelizedRSLUnsignedInt,
       "hzQtmModemModulationType": hzQtmModemModulationType,
       "hzQtmModemRxSpeed": hzQtmModemRxSpeed,
       "hzQtmModemTxSpeed": hzQtmModemTxSpeed,
       "hzQtmModemSNR": hzQtmModemSNR,
       "hzQtmModemEbToNoiseRatio": hzQtmModemEbToNoiseRatio,
       "hzQtmModemEqualizerStress": hzQtmModemEqualizerStress,
       "hzQtmModemSNRThresholdParameters": hzQtmModemSNRThresholdParameters,
       "hzQtmModemChannelizedRslBelowThresholdParameters": hzQtmModemChannelizedRslBelowThresholdParameters,
       "hzQtmModemXpicEqualizerStress": hzQtmModemXpicEqualizerStress,
       "hzQtmModemXPI": hzQtmModemXPI,
       "hzQtmModemStatsTable": hzQtmModemStatsTable,
       "hzQtmModemStatsEntry": hzQtmModemStatsEntry,
       "hzQtmModemStatsIndex": hzQtmModemStatsIndex,
       "hzQtmModemTxBlocks": hzQtmModemTxBlocks,
       "hzQtmModemRxBlocksOKs": hzQtmModemRxBlocksOKs,
       "hzQtmModemRxBlocksErrors": hzQtmModemRxBlocksErrors,
       "hzQtmWirelessEnetPortStatsTable": hzQtmWirelessEnetPortStatsTable,
       "hzQtmWirelessEnetPortStatsEntry": hzQtmWirelessEnetPortStatsEntry,
       "hzQtmWirelessEnetPortIndex": hzQtmWirelessEnetPortIndex,
       "hzQtmWirelessEnetPortTxFrames": hzQtmWirelessEnetPortTxFrames,
       "hzQtmWirelessEnetPortRxFramesOK": hzQtmWirelessEnetPortRxFramesOK,
       "hzQtmWirelessEnetPortRxFramesErrors": hzQtmWirelessEnetPortRxFramesErrors,
       "hzQtmWirelessEnetPortRxFramesQueueDiscards": hzQtmWirelessEnetPortRxFramesQueueDiscards,
       "hzQtmWirelessInterfaceIF": hzQtmWirelessInterfaceIF,
       "hzQtmIntermediateFrequencyTable": hzQtmIntermediateFrequencyTable,
       "hzQtmIntermediateFrequencyEntry": hzQtmIntermediateFrequencyEntry,
       "hzQtmIFPathIndex": hzQtmIFPathIndex,
       "hzQtmIFPathTxLockStatus": hzQtmIFPathTxLockStatus,
       "hzQtmIFPathRxLockStatus": hzQtmIFPathRxLockStatus,
       "hzQtmIFPathLoopbackLockStatus": hzQtmIFPathLoopbackLockStatus,
       "hzQtmWirelessInterfaceRadios": hzQtmWirelessInterfaceRadios,
       "hzQtmRadioTable": hzQtmRadioTable,
       "hzQtmRadioEntry": hzQtmRadioEntry,
       "hzQtmRadioIndex": hzQtmRadioIndex,
       "hzQtmRadioDescription": hzQtmRadioDescription,
       "hzQtmRadioOperStatus": hzQtmRadioOperStatus,
       "hzQtmRadioLastChanged": hzQtmRadioLastChanged,
       "hzQtmRadioReceiveSignalLevel": hzQtmRadioReceiveSignalLevel,
       "hzQtmRadioReceiveSignalLevelUnsigned": hzQtmRadioReceiveSignalLevelUnsigned,
       "hzQtmRadioTxGain": hzQtmRadioTxGain,
       "hzQtmRadioRxGain": hzQtmRadioRxGain,
       "hzQtmRadioReset": hzQtmRadioReset,
       "hzQtmRadioTransmitPowerdBm": hzQtmRadioTransmitPowerdBm,
       "hzQtmRadioPowerOption": hzQtmRadioPowerOption,
       "hzQtmRadioTxState": hzQtmRadioTxState,
       "hzQtmRadioActualTxState": hzQtmRadioActualTxState,
       "hzQtmRadioTemperature": hzQtmRadioTemperature,
       "hzQtmRadioRxCableLoss": hzQtmRadioRxCableLoss,
       "hzQtmRadioTxCableLoss": hzQtmRadioTxCableLoss,
       "hzQtmRadioTxCableLossChange": hzQtmRadioTxCableLossChange,
       "hzQtmRadioMaxTransmitPowerdBm": hzQtmRadioMaxTransmitPowerdBm,
       "hzQtmRadioActualTransmitPowerdBm": hzQtmRadioActualTransmitPowerdBm,
       "hzQtmWirelessInterfaceRadioFrequencies": hzQtmWirelessInterfaceRadioFrequencies,
       "hzQtmWirelessInterfaceRadio1Frequencies": hzQtmWirelessInterfaceRadio1Frequencies,
       "hzQtmRadio1FreqGroupSelected": hzQtmRadio1FreqGroupSelected,
       "hzQtmRadio1BandTable": hzQtmRadio1BandTable,
       "hzQtmRadio1BandEntry": hzQtmRadio1BandEntry,
       "hzQtmRadio1BandIndex": hzQtmRadio1BandIndex,
       "hzQtmRadio1BandId": hzQtmRadio1BandId,
       "hzQtmRadio1BandName": hzQtmRadio1BandName,
       "hzQtmRadio1BandProgrammed": hzQtmRadio1BandProgrammed,
       "hzQtmRadio1TxHighFreqTable": hzQtmRadio1TxHighFreqTable,
       "hzQtmRadio1TxHighFreqEntry": hzQtmRadio1TxHighFreqEntry,
       "hzQtmRadio1TxHighFreqIndex": hzQtmRadio1TxHighFreqIndex,
       "hzQtmRadio1TxHighFreqChannelIndex": hzQtmRadio1TxHighFreqChannelIndex,
       "hzQtmRadio1TxHighFreqTransmitRfFrequency": hzQtmRadio1TxHighFreqTransmitRfFrequency,
       "hzQtmRadio1TxHighFreqReceiveRfFrequency": hzQtmRadio1TxHighFreqReceiveRfFrequency,
       "hzQtmRadio1TxHighFreqProgrammed": hzQtmRadio1TxHighFreqProgrammed,
       "hzQtmRadio1TxLowFreqTable": hzQtmRadio1TxLowFreqTable,
       "hzQtmRadio1TxLowFreqEntry": hzQtmRadio1TxLowFreqEntry,
       "hzQtmRadio1TxLowFreqIndex": hzQtmRadio1TxLowFreqIndex,
       "hzQtmRadio1TxLowFreqChannelIndex": hzQtmRadio1TxLowFreqChannelIndex,
       "hzQtmRadio1TxLowFreqTransmitRfFrequency": hzQtmRadio1TxLowFreqTransmitRfFrequency,
       "hzQtmRadio1TxLowFreqReceiveRfFrequency": hzQtmRadio1TxLowFreqReceiveRfFrequency,
       "hzQtmRadio1TxLowFreqProgrammed": hzQtmRadio1TxLowFreqProgrammed,
       "hzQtmRadio1ProgrammedFrequency": hzQtmRadio1ProgrammedFrequency,
       "hzQtmRadio1ProgrammedFrequencyChannel": hzQtmRadio1ProgrammedFrequencyChannel,
       "hzQtmRadio1ProgrammedFrequencyTxRf": hzQtmRadio1ProgrammedFrequencyTxRf,
       "hzQtmRadio1ProgrammedFrequencyRxRf": hzQtmRadio1ProgrammedFrequencyRxRf,
       "hzQtmWirelessInterfaceRadio2Frequencies": hzQtmWirelessInterfaceRadio2Frequencies,
       "hzQtmRadio2FreqGroupSelected": hzQtmRadio2FreqGroupSelected,
       "hzQtmRadio2BandTable": hzQtmRadio2BandTable,
       "hzQtmRadio2BandEntry": hzQtmRadio2BandEntry,
       "hzQtmRadio2BandIndex": hzQtmRadio2BandIndex,
       "hzQtmRadio2BandId": hzQtmRadio2BandId,
       "hzQtmRadio2BandName": hzQtmRadio2BandName,
       "hzQtmRadio2BandProgrammed": hzQtmRadio2BandProgrammed,
       "hzQtmRadio2TxHighFreqTable": hzQtmRadio2TxHighFreqTable,
       "hzQtmRadio2TxHighFreqEntry": hzQtmRadio2TxHighFreqEntry,
       "hzQtmRadio2TxHighFreqIndex": hzQtmRadio2TxHighFreqIndex,
       "hzQtmRadio2TxHighFreqChannelIndex": hzQtmRadio2TxHighFreqChannelIndex,
       "hzQtmRadio2TxHighFreqTransmitRfFrequency": hzQtmRadio2TxHighFreqTransmitRfFrequency,
       "hzQtmRadio2TxHighFreqReceiveRfFrequency": hzQtmRadio2TxHighFreqReceiveRfFrequency,
       "hzQtmRadio2TxHighFreqProgrammed": hzQtmRadio2TxHighFreqProgrammed,
       "hzQtmRadio2TxLowFreqTable": hzQtmRadio2TxLowFreqTable,
       "hzQtmRadio2TxLowFreqEntry": hzQtmRadio2TxLowFreqEntry,
       "hzQtmRadio2TxLowFreqIndex": hzQtmRadio2TxLowFreqIndex,
       "hzQtmRadio2TxLowFreqChannelIndex": hzQtmRadio2TxLowFreqChannelIndex,
       "hzQtmRadio2TxLowFreqTransmitRfFrequency": hzQtmRadio2TxLowFreqTransmitRfFrequency,
       "hzQtmRadio2TxLowFreqReceiveRfFrequency": hzQtmRadio2TxLowFreqReceiveRfFrequency,
       "hzQtmRadio2TxLowFreqProgrammed": hzQtmRadio2TxLowFreqProgrammed,
       "hzQtmRadio2ProgrammedFrequency": hzQtmRadio2ProgrammedFrequency,
       "hzQtmRadio2ProgrammedFrequencyChannel": hzQtmRadio2ProgrammedFrequencyChannel,
       "hzQtmRadio2ProgrammedFrequencyTxRf": hzQtmRadio2ProgrammedFrequencyTxRf,
       "hzQtmRadio2ProgrammedFrequencyRxRf": hzQtmRadio2ProgrammedFrequencyRxRf,
       "hzQtmWirelessInterfaceAntenna": hzQtmWirelessInterfaceAntenna,
       "hzQtmAntennaDiameter": hzQtmAntennaDiameter,
       "hzQtmAntenna1Tilt": hzQtmAntenna1Tilt,
       "hzQtmAntenna2Tilt": hzQtmAntenna2Tilt,
       "hzQtmWirelessInterfaceRedundancy": hzQtmWirelessInterfaceRedundancy,
       "hzQtmWirelessInterfaceRedundancyActiveWirelessPort": hzQtmWirelessInterfaceRedundancyActiveWirelessPort,
       "hzQtmWirelessInterfaceRedundancyPrimaryWirelessPort": hzQtmWirelessInterfaceRedundancyPrimaryWirelessPort,
       "hzQtmWirelessInterfaceRedundancySwitchingAlgorithm": hzQtmWirelessInterfaceRedundancySwitchingAlgorithm,
       "hzQtmWirelessInterfaceRedundancySwitchCause": hzQtmWirelessInterfaceRedundancySwitchCause,
       "hzQtmWirelessInterfaceRedundancyRemoveFaulty": hzQtmWirelessInterfaceRedundancyRemoveFaulty,
       "hzQtmWirelessInterfaceRedundancyDiagnostics": hzQtmWirelessInterfaceRedundancyDiagnostics,
       "hzQtmWirelessInterfaceRedundancyDiagnose": hzQtmWirelessInterfaceRedundancyDiagnose,
       "hzQtmWirelessInterfaceRedundancyDiagnosticResult": hzQtmWirelessInterfaceRedundancyDiagnosticResult,
       "hzQtmWirelessInterfaceRedundancyRadioSwitch": hzQtmWirelessInterfaceRedundancyRadioSwitch,
       "hzQtmWirelessInterfaceRedundancySwitchRadio": hzQtmWirelessInterfaceRedundancySwitchRadio,
       "hzQtmWirelessInterfaceRedundancySwitchRadioResult": hzQtmWirelessInterfaceRedundancySwitchRadioResult,
       "hzQtmCalendar": hzQtmCalendar,
       "hzQtmDate": hzQtmDate,
       "hzQtmTime": hzQtmTime,
       "hzQtmAlarms": hzQtmAlarms,
       "hzQtmClearAlarmCounters": hzQtmClearAlarmCounters,
       "hzQtmSystemAlarms": hzQtmSystemAlarms,
       "hzQtmExplicitAuthenticationFailureAlarm": hzQtmExplicitAuthenticationFailureAlarm,
       "hzQtmExplicitAuthenticationFailureCounts": hzQtmExplicitAuthenticationFailureCounts,
       "hzQtmHitlessAamConfigMismatchAlarm": hzQtmHitlessAamConfigMismatchAlarm,
       "hzQtmHitlessAamConfigMismatchCounts": hzQtmHitlessAamConfigMismatchCounts,
       "hzQtmHitlessAamActiveAlarm": hzQtmHitlessAamActiveAlarm,
       "hzQtmHitlessAamActiveCounts": hzQtmHitlessAamActiveCounts,
       "hzQtmSntpServerUnreachableAlarm": hzQtmSntpServerUnreachableAlarm,
       "hzQtmSntpServerUnreachableCounts": hzQtmSntpServerUnreachableCounts,
       "hzQtmFrequencyFileInvalidAlarm": hzQtmFrequencyFileInvalidAlarm,
       "hzQtmFrequencyFileInvalidCounts": hzQtmFrequencyFileInvalidCounts,
       "hzQtmFanFailureAlarm": hzQtmFanFailureAlarm,
       "hzQtmFanFailureCounts": hzQtmFanFailureCounts,
       "hzQtmRedundancyPrimaryPortNotSetAlarm": hzQtmRedundancyPrimaryPortNotSetAlarm,
       "hzQtmRedundancyPrimaryPortNotSetCounts": hzQtmRedundancyPrimaryPortNotSetCounts,
       "hzQtmRedundancySecondaryPortActiveAlarm": hzQtmRedundancySecondaryPortActiveAlarm,
       "hzQtmRedundancySecondaryPortActiveCounts": hzQtmRedundancySecondaryPortActiveCounts,
       "hzQtmRedundancyPrimaryPortFaultyAlarm": hzQtmRedundancyPrimaryPortFaultyAlarm,
       "hzQtmRedundancyPrimaryPortFaultyCounts": hzQtmRedundancyPrimaryPortFaultyCounts,
       "hzQtmRedundancySecondaryPortFaultyAlarm": hzQtmRedundancySecondaryPortFaultyAlarm,
       "hzQtmRedundancySecondaryPortFaultyCounts": hzQtmRedundancySecondaryPortFaultyCounts,
       "hzQtmAtpcConfigMismatchAlarm": hzQtmAtpcConfigMismatchAlarm,
       "hzQtmAtpcConfigMismatchCounts": hzQtmAtpcConfigMismatchCounts,
       "hzQtmDroppedEnetFramesThresholdAlarm": hzQtmDroppedEnetFramesThresholdAlarm,
       "hzQtmDroppedEnetFramesThresholdCounts": hzQtmDroppedEnetFramesThresholdCounts,
       "hzQtmBandwidthUtilizationThresholdAlarm": hzQtmBandwidthUtilizationThresholdAlarm,
       "hzQtmBandwidthUtilizationThresholdCounts": hzQtmBandwidthUtilizationThresholdCounts,
       "hzQtmRlsMismatchAlarm": hzQtmRlsMismatchAlarm,
       "hzQtmRlsMismatchCounts": hzQtmRlsMismatchCounts,
       "hzQtmRLSQueueBasedShutdownActivatedAlarm": hzQtmRLSQueueBasedShutdownActivatedAlarm,
       "hzQtmRLSQueueBasedShutdownActivatedCounts": hzQtmRLSQueueBasedShutdownActivatedCounts,
       "hzQtmFpgaProgrammingErrorAlarm": hzQtmFpgaProgrammingErrorAlarm,
       "hzQtmFpgaProgrammingErrorCounts": hzQtmFpgaProgrammingErrorCounts,
       "hzQtmMibChangeNotSavedAlarm": hzQtmMibChangeNotSavedAlarm,
       "hzQtmMibChangeNotSavedCounts": hzQtmMibChangeNotSavedCounts,
       "hzQtmBadSystemConfigurationAlarm": hzQtmBadSystemConfigurationAlarm,
       "hzQtmBadSystemConfigurationCounts": hzQtmBadSystemConfigurationCounts,
       "hzQtmPartnerNodeAlarm": hzQtmPartnerNodeAlarm,
       "hzQtmPartnerNodeAlarmCounts": hzQtmPartnerNodeAlarmCounts,
       "hzQtmBandwidthDoublingInvalidLinkConfigAlarm": hzQtmBandwidthDoublingInvalidLinkConfigAlarm,
       "hzQtmBandwidthDoublingInvalidLinkConfigCounts": hzQtmBandwidthDoublingInvalidLinkConfigCounts,
       "hzQtmBandwidthDoublingWrongPortConnectedAlarm": hzQtmBandwidthDoublingWrongPortConnectedAlarm,
       "hzQtmBandwidthDoublingWrongPortConnectedCount": hzQtmBandwidthDoublingWrongPortConnectedCount,
       "hzQtmSynceLostLockAlarm": hzQtmSynceLostLockAlarm,
       "hzQtmSynceLostLockCount": hzQtmSynceLostLockCount,
       "hzQtmSynceSecondarySourceInUseAlarm": hzQtmSynceSecondarySourceInUseAlarm,
       "hzQtmSynceSecondarySourceInUseCount": hzQtmSynceSecondarySourceInUseCount,
       "hzQtmNetworkInterfaceAlarms": hzQtmNetworkInterfaceAlarms,
       "hzQtmEnetPortAlarmsTable": hzQtmEnetPortAlarmsTable,
       "hzQtmEnetPortAlarmsEntry": hzQtmEnetPortAlarmsEntry,
       "hzQtmEnetPortAlarmsIndex": hzQtmEnetPortAlarmsIndex,
       "hzQtmEnetPortEthernetLinkDownAlarm": hzQtmEnetPortEthernetLinkDownAlarm,
       "hzQtmEnetPortEthernetLinkDownCounts": hzQtmEnetPortEthernetLinkDownCounts,
       "hzQtmWirelessInterfaceAlarms": hzQtmWirelessInterfaceAlarms,
       "hzQtmModemAlarms": hzQtmModemAlarms,
       "hzQtmModemAlarmsTable": hzQtmModemAlarmsTable,
       "hzQtmModemAlarmsEntry": hzQtmModemAlarmsEntry,
       "hzQtmModemAlarmsIndex": hzQtmModemAlarmsIndex,
       "hzQtmModemRxLossOfSignalAlarm": hzQtmModemRxLossOfSignalAlarm,
       "hzQtmModemRxLossOfSignalCounts": hzQtmModemRxLossOfSignalCounts,
       "hzQtmModemTxLossOfSyncAlarm": hzQtmModemTxLossOfSyncAlarm,
       "hzQtmModemTxLossOfSyncCounts": hzQtmModemTxLossOfSyncCounts,
       "hzQtmModemSnrBelowThresholdAlarm": hzQtmModemSnrBelowThresholdAlarm,
       "hzQtmModemSnrBelowThresholdCounts": hzQtmModemSnrBelowThresholdCounts,
       "hzQtmModemEqualizerStressExceedThresholdAlarm": hzQtmModemEqualizerStressExceedThresholdAlarm,
       "hzQtmModemEquilizerStressExceedThresholdCounts": hzQtmModemEquilizerStressExceedThresholdCounts,
       "hzQtmModemRLSShutdownActivatedAlarm": hzQtmModemRLSShutdownActivatedAlarm,
       "hzQtmModemRLSShutdownActivatedCounts": hzQtmModemRLSShutdownActivatedCounts,
       "hzQtmModemXPICEquStressExceedThresholdAlarm": hzQtmModemXPICEquStressExceedThresholdAlarm,
       "hzQtmModemXPICEquStressExceedThresholdCounts": hzQtmModemXPICEquStressExceedThresholdCounts,
       "hzQtmRadioAlarms": hzQtmRadioAlarms,
       "hzQtmRadioAlarmsTable": hzQtmRadioAlarmsTable,
       "hzQtmRadioAlarmsEntry": hzQtmRadioAlarmsEntry,
       "hzQtmRadioAlarmsIndex": hzQtmRadioAlarmsIndex,
       "hzQtmRadioSynthLostLockAlarm": hzQtmRadioSynthLostLockAlarm,
       "hzQtmRadioSynthLostLockCounts": hzQtmRadioSynthLostLockCounts,
       "hzQtmRadioLostCommunicationAlarm": hzQtmRadioLostCommunicationAlarm,
       "hzQtmRadioLostCommunicationCounts": hzQtmRadioLostCommunicationCounts,
       "hzQtmRadioMismatchAlarm": hzQtmRadioMismatchAlarm,
       "hzQtmRadioMismatchCounts": hzQtmRadioMismatchCounts,
       "hzQtmRadioPowerAmpAlarm": hzQtmRadioPowerAmpAlarm,
       "hzQtmRadioPowerAmpCounts": hzQtmRadioPowerAmpCounts,
       "hzQtmRadioExcessiveTxCableLossAlarm": hzQtmRadioExcessiveTxCableLossAlarm,
       "hzQtmRadioExcessiveTxCableLossCounts": hzQtmRadioExcessiveTxCableLossCounts,
       "hzQtmRadioRslBelowThresholdAlarm": hzQtmRadioRslBelowThresholdAlarm,
       "hzQtmRadioRslBelowThresholdCounts": hzQtmRadioRslBelowThresholdCounts,
       "hzQtmRadioHighPowerTxDetectorAlarm": hzQtmRadioHighPowerTxDetectorAlarm,
       "hzQtmRadioHighPowerTxDetectorCounts": hzQtmRadioHighPowerTxDetectorCounts,
       "hzQtmRadioRedundancySerialNumMismatchAlarm": hzQtmRadioRedundancySerialNumMismatchAlarm,
       "hzQtmRadioRedundancySerialNumMismatchCounts": hzQtmRadioRedundancySerialNumMismatchCounts,
       "hzQtmRadioExcessiveTxCableLossChangeAlarm": hzQtmRadioExcessiveTxCableLossChangeAlarm,
       "hzQtmRadioExcessiveTxCableLossChangeCounts": hzQtmRadioExcessiveTxCableLossChangeCounts,
       "hzQtmRadioExcessiveRxCableLossAlarm": hzQtmRadioExcessiveRxCableLossAlarm,
       "hzQtmRadioExcessiveRxCableLossCounts": hzQtmRadioExcessiveRxCableLossCounts,
       "hzQtmRadioAtpcTxAtMaxPowerAlarm": hzQtmRadioAtpcTxAtMaxPowerAlarm,
       "hzQtmRadioAtpcTxAtMaxPowerCounts": hzQtmRadioAtpcTxAtMaxPowerCounts,
       "hzQtmRadioSwDownloadFailedAlarm": hzQtmRadioSwDownloadFailedAlarm,
       "hzQtmRadioSwDownloadFailedCounts": hzQtmRadioSwDownloadFailedCounts,
       "hzQtmRadioDrainCurrentAlarm": hzQtmRadioDrainCurrentAlarm,
       "hzQtmRadioDrainCurrentCounts": hzQtmRadioDrainCurrentCounts,
       "hzQtmRadioPowerOffAlarm": hzQtmRadioPowerOffAlarm,
       "hzQtmRadioPowerOffCounts": hzQtmRadioPowerOffCounts,
       "hzQtmIFAlarms": hzQtmIFAlarms,
       "hzQtmIFAlarmsTable": hzQtmIFAlarmsTable,
       "hzQtmIFAlarmsEntry": hzQtmIFAlarmsEntry,
       "hzQtmIFAlarmsIndex": hzQtmIFAlarmsIndex,
       "hzQtmIFLostLockAlarm": hzQtmIFLostLockAlarm,
       "hzQtmIFLostLockCounts": hzQtmIFLostLockCounts,
       "hzQtmTrapConfig": hzQtmTrapConfig,
       "hzQtmSnmpTrapHostTable": hzQtmSnmpTrapHostTable,
       "hzQtmSnmpTrapHostEntry": hzQtmSnmpTrapHostEntry,
       "hzQtmSnmpTrapHostIndex": hzQtmSnmpTrapHostIndex,
       "hzQtmSnmpTrapHostMode": hzQtmSnmpTrapHostMode,
       "hzQtmSnmpTrapHostIpAddress": hzQtmSnmpTrapHostIpAddress,
       "hzQtmSnmpTrapHostCommunityName": hzQtmSnmpTrapHostCommunityName,
       "hzQtmSnmpTrapHostActivated": hzQtmSnmpTrapHostActivated,
       "hzQtmSnmpV3TrapHostsTable": hzQtmSnmpV3TrapHostsTable,
       "hzQtmSnmpV3TrapHostsEntry": hzQtmSnmpV3TrapHostsEntry,
       "hzQtmSnmpV3TrapHostsIndex": hzQtmSnmpV3TrapHostsIndex,
       "snmpV3TrapHostIpAddress": snmpV3TrapHostIpAddress,
       "snmpV3TrapHostUserName": snmpV3TrapHostUserName,
       "snmpV3TrapHostAuthProtocol": snmpV3TrapHostAuthProtocol,
       "snmpV3TrapHostAuthPassword": snmpV3TrapHostAuthPassword,
       "snmpV3TrapHostPrivProtocol": snmpV3TrapHostPrivProtocol,
       "snmpV3TrapHostPrivPassword": snmpV3TrapHostPrivPassword,
       "snmpV3TrapHostActivated": snmpV3TrapHostActivated,
       "hzQtmTrapEnable": hzQtmTrapEnable,
       "hzQtmColdStartTrap": hzQtmColdStartTrap,
       "hzQtmLinkDownTrap": hzQtmLinkDownTrap,
       "hzQtmLinkUpTrap": hzQtmLinkUpTrap,
       "hzQtmExplicitAuthenticationFailureTrap": hzQtmExplicitAuthenticationFailureTrap,
       "hzQtmHitlessAamConfigMismatchTrap": hzQtmHitlessAamConfigMismatchTrap,
       "hzQtmHitlessAamActiveTrap": hzQtmHitlessAamActiveTrap,
       "hzQtmAtpcConfigMismatchTrap": hzQtmAtpcConfigMismatchTrap,
       "hzQtmSntpServersUnreachableTrap": hzQtmSntpServersUnreachableTrap,
       "hzQtmFrequencyFileInvalidTrap": hzQtmFrequencyFileInvalidTrap,
       "hzQtmEnetPortDroppedFramesThresholdExceedTrap": hzQtmEnetPortDroppedFramesThresholdExceedTrap,
       "hzQtmEnetPortBandwidthUtilizationThresholdExceedTrap": hzQtmEnetPortBandwidthUtilizationThresholdExceedTrap,
       "hzQtmEnetPortRlsMismatchTrap": hzQtmEnetPortRlsMismatchTrap,
       "hzQtmRLSQueueBasedShutdownActivatedTrap": hzQtmRLSQueueBasedShutdownActivatedTrap,
       "hzQtmModemRxLossOfSignalLockTrap": hzQtmModemRxLossOfSignalLockTrap,
       "hzQtmModemTxLossOfSyncTrap": hzQtmModemTxLossOfSyncTrap,
       "hzQtmModemSnrBelowThresholdTrap": hzQtmModemSnrBelowThresholdTrap,
       "hzQtmModemEqualizerStressExceedThresholdTrap": hzQtmModemEqualizerStressExceedThresholdTrap,
       "hzQtmModemChannelizedRslBelowThresholdTrap": hzQtmModemChannelizedRslBelowThresholdTrap,
       "hzQtmFpgaProgrammingErrorTrap": hzQtmFpgaProgrammingErrorTrap,
       "hzQtmUserManagementSessionCommencedTrap": hzQtmUserManagementSessionCommencedTrap,
       "hzQtmUserManagementSessionTerminatedTrap": hzQtmUserManagementSessionTerminatedTrap,
       "hzQtmAtpcTxAtMaxPwrTrap": hzQtmAtpcTxAtMaxPwrTrap,
       "hzQtmRadioSynthLostLockTrap": hzQtmRadioSynthLostLockTrap,
       "hzQtmRadioLostCommunicationTrap": hzQtmRadioLostCommunicationTrap,
       "hzQtmRadioMismatchTrap": hzQtmRadioMismatchTrap,
       "hzQtmRadioPowerAmpTrap": hzQtmRadioPowerAmpTrap,
       "hzQtmRadioExcessiveTxCableLossTrap": hzQtmRadioExcessiveTxCableLossTrap,
       "hzQtmHiPowerRadioTxDetectorTrap": hzQtmHiPowerRadioTxDetectorTrap,
       "hzQtmSecondaryRadioIsActiveTrap": hzQtmSecondaryRadioIsActiveTrap,
       "hzQtmRedundancySerialNumberMisMatchTrap": hzQtmRedundancySerialNumberMisMatchTrap,
       "hzQtmRadioFirmwareMismatchTrap": hzQtmRadioFirmwareMismatchTrap,
       "hzQtmSecondaryRadioNotdetectedTrap": hzQtmSecondaryRadioNotdetectedTrap,
       "hzQtmPrimaryRadioNotdetectedTrap": hzQtmPrimaryRadioNotdetectedTrap,
       "hzQtmFaultyPrimaryRadioTrap": hzQtmFaultyPrimaryRadioTrap,
       "hzQtmRadioExcessiveTxCableLossChangeTrap": hzQtmRadioExcessiveTxCableLossChangeTrap,
       "hzQtmRadioExcessiveRxCableLossTrap": hzQtmRadioExcessiveRxCableLossTrap,
       "hzQtmRedundancyPrimaryPortNotSetTrap": hzQtmRedundancyPrimaryPortNotSetTrap,
       "hzQtmRedundancySecondaryPortIsActiveTrap": hzQtmRedundancySecondaryPortIsActiveTrap,
       "hzQtmRedundancyPrimaryPortFaultyTrap": hzQtmRedundancyPrimaryPortFaultyTrap,
       "hzQtmRedundancySecondaryPortFaultyTrap": hzQtmRedundancySecondaryPortFaultyTrap,
       "hzQtmFanFailedTrap": hzQtmFanFailedTrap,
       "hzQtmModemRlsShutdownActivatedTrap": hzQtmModemRlsShutdownActivatedTrap,
       "hzQtmRadioUnitHwChangedTrap": hzQtmRadioUnitHwChangedTrap,
       "hzQtmRadioSwDownloadFailedTrap": hzQtmRadioSwDownloadFailedTrap,
       "hzQtmRadioRestartedOKTrap": hzQtmRadioRestartedOKTrap,
       "hzQtmMibChangeNotSavedTrap": hzQtmMibChangeNotSavedTrap,
       "hzQtmRadioDrainCurrentTrap": hzQtmRadioDrainCurrentTrap,
       "hzQtmIFLostLockTrap": hzQtmIFLostLockTrap,
       "hzQtmInvalidSystemConfigurationTrap": hzQtmInvalidSystemConfigurationTrap,
       "hzQtmHitlessAamEventTrap": hzQtmHitlessAamEventTrap,
       "hzQtmModemXPICEqualizerStressExceedThresholdTrap": hzQtmModemXPICEqualizerStressExceedThresholdTrap,
       "hzQtmPartnerNodeAlarmTrap": hzQtmPartnerNodeAlarmTrap,
       "hzQtmBandwidthDoublingInvalidLinkConfigTrap": hzQtmBandwidthDoublingInvalidLinkConfigTrap,
       "hzQtmBandwidthDoublingWrongPortConnectedTrap": hzQtmBandwidthDoublingWrongPortConnectedTrap,
       "hzQtmRadioPowerOffTrap": hzQtmRadioPowerOffTrap,
       "hzQtmSynceLostLockTrap": hzQtmSynceLostLockTrap,
       "hzQtmSynceSecondarySourceInUseTrap": hzQtmSynceSecondarySourceInUseTrap,
       "hzQtmSnmp": hzQtmSnmp,
       "hzQtmSnmpUserAccess": hzQtmSnmpUserAccess,
       "hzQtmSnmpManagerAnyCommunityName": hzQtmSnmpManagerAnyCommunityName,
       "hzQtmSnmpSetRequests": hzQtmSnmpSetRequests,
       "hzQtmSnmpManagersTable": hzQtmSnmpManagersTable,
       "hzQtmSnmpManagersEntry": hzQtmSnmpManagersEntry,
       "hzQtmSnmpManagersIndex": hzQtmSnmpManagersIndex,
       "hzQtmSnmpManagerIpAddress": hzQtmSnmpManagerIpAddress,
       "hzQtmSnmpManagerCommunityName": hzQtmSnmpManagerCommunityName,
       "hzQtmSnmpManagerActivated": hzQtmSnmpManagerActivated,
       "hzQtmSnmpV3ManagersTable": hzQtmSnmpV3ManagersTable,
       "hzQtmSnmpV3ManagersEntry": hzQtmSnmpV3ManagersEntry,
       "hzQtmSnmpV3ManagersIndex": hzQtmSnmpV3ManagersIndex,
       "hzQtmSnmpV3ManagerUserName": hzQtmSnmpV3ManagerUserName,
       "hzQtmSnmpV3ManagerAuthProtocol": hzQtmSnmpV3ManagerAuthProtocol,
       "hzQtmSnmpV3ManagerAuthPassword": hzQtmSnmpV3ManagerAuthPassword,
       "hzQtmSnmpV3ManagerPrivProtocol": hzQtmSnmpV3ManagerPrivProtocol,
       "hzQtmSnmpV3ManagerPrivPassword": hzQtmSnmpV3ManagerPrivPassword,
       "hzQtmSnmpV3ManagerActivated": hzQtmSnmpV3ManagerActivated,
       "hzQtmManagementSessions": hzQtmManagementSessions,
       "hzQtmUserSessionUserTable": hzQtmUserSessionUserTable,
       "hzQtmUserSessionUserEntry": hzQtmUserSessionUserEntry,
       "hzQtmUserSessionUserIndex": hzQtmUserSessionUserIndex,
       "hzQtmUserSessionUserName": hzQtmUserSessionUserName,
       "hzQtmUserSessionUserConnectionType": hzQtmUserSessionUserConnectionType,
       "hzQtmUserSessionUserState": hzQtmUserSessionUserState,
       "hzQtmHttp": hzQtmHttp,
       "hzQtmHttpEnable": hzQtmHttpEnable,
       "hzQtmHttpSecure": hzQtmHttpSecure,
       "hzQtmHttpSecureCertificateStatus": hzQtmHttpSecureCertificateStatus,
       "hzQtmHttpSecureAccessForAdminUsers": hzQtmHttpSecureAccessForAdminUsers,
       "hzQtmHttpSecureAccessForNocUsers": hzQtmHttpSecureAccessForNocUsers,
       "hzQtmHttpSecureAccessForSuperUsers": hzQtmHttpSecureAccessForSuperUsers,
       "hzQtmQos": hzQtmQos,
       "hzQtmQosEnable": hzQtmQosEnable,
       "hzQtmCosType": hzQtmCosType,
       "hzQtmCosQinQiTag": hzQtmCosQinQiTag,
       "hzQtmCosQinQoTag": hzQtmCosQinQoTag,
       "hzQtmCosQueueMapping": hzQtmCosQueueMapping,
       "hzQtmCosExpediteQueue": hzQtmCosExpediteQueue,
       "hzQtmCosQueueCIR": hzQtmCosQueueCIR,
       "hzQtmCosQueueCBS": hzQtmCosQueueCBS,
       "hzQtmCosDefaultValue": hzQtmCosDefaultValue,
       "hzQtmQosPolicy": hzQtmQosPolicy,
       "hzQtmCosWfqWeight": hzQtmCosWfqWeight,
       "hzQtmCutThroughProcessing": hzQtmCutThroughProcessing,
       "hzQtmCosEcfmFlowMapping": hzQtmCosEcfmFlowMapping,
       "hzQtmCosControlFlowMapping": hzQtmCosControlFlowMapping,
       "hzQtmRapidLinkShutdown": hzQtmRapidLinkShutdown,
       "hzQtmRlsEnable": hzQtmRlsEnable,
       "hzQtmRlsHardFaultMonitor": hzQtmRlsHardFaultMonitor,
       "hzQtmRlsWirelessPortOption": hzQtmRlsWirelessPortOption,
       "hzQtmRlsAutomaticLinkReestablish": hzQtmRlsAutomaticLinkReestablish,
       "hzQtmRlsManualLinkReestablish": hzQtmRlsManualLinkReestablish,
       "hzQtmWriteRlsMonitorParametersToSystem": hzQtmWriteRlsMonitorParametersToSystem,
       "hzQtmRlsDroppedFramesThresholdOverride": hzQtmRlsDroppedFramesThresholdOverride,
       "hzQtmRlsDroppedFramesThresholdTable": hzQtmRlsDroppedFramesThresholdTable,
       "hzQtmRlsDroppedFramesThresholdEntry": hzQtmRlsDroppedFramesThresholdEntry,
       "hzQtmRlsDroppedFramesThresholdIndex": hzQtmRlsDroppedFramesThresholdIndex,
       "hzQtmRlsAllowedDroppedFrameRateValue": hzQtmRlsAllowedDroppedFrameRateValue,
       "hzQtmRlsDroppedFrameMonitorPeriod": hzQtmRlsDroppedFrameMonitorPeriod,
       "hzQtmRlsSoftFaultMonitorTable": hzQtmRlsSoftFaultMonitorTable,
       "hzQtmRlsSoftFaultMonitorEntry": hzQtmRlsSoftFaultMonitorEntry,
       "hzQtmRlsSoftFaultMonitorIndex": hzQtmRlsSoftFaultMonitorIndex,
       "hzQtmRlsEstablishErredFrameThreshold": hzQtmRlsEstablishErredFrameThreshold,
       "hzQtmRlsShutdownErredFrameThreshold": hzQtmRlsShutdownErredFrameThreshold,
       "hzQtmRlsEstablishNumberOfSamples": hzQtmRlsEstablishNumberOfSamples,
       "hzQtmRlsShutdownNumberOfSamples": hzQtmRlsShutdownNumberOfSamples,
       "hzQtmRlsEstablishSamplePeriod": hzQtmRlsEstablishSamplePeriod,
       "hzQtmRlsShutdownSamplePeriod": hzQtmRlsShutdownSamplePeriod,
       "hzQtmRlsQuickShutdownSamplePeriod": hzQtmRlsQuickShutdownSamplePeriod,
       "hzQtmHardFaultMonitorTable": hzQtmHardFaultMonitorTable,
       "hzQtmHardFaultMonitorEntry": hzQtmHardFaultMonitorEntry,
       "hzQtmHardFaultMonitorIndex": hzQtmHardFaultMonitorIndex,
       "hzQtmRlsHardFaultSamplePeriod": hzQtmRlsHardFaultSamplePeriod,
       "hzQtmRlsHardFaultThreshold": hzQtmRlsHardFaultThreshold,
       "hzQtmRlsReceiveSignalLevelMonitorTable": hzQtmRlsReceiveSignalLevelMonitorTable,
       "hzQtmRlsReceiveSignalLevelMonitorEntry": hzQtmRlsReceiveSignalLevelMonitorEntry,
       "hzQtmRlsReceiveSignalLevelMonitorIndex": hzQtmRlsReceiveSignalLevelMonitorIndex,
       "hzQtmRlsMakeRslMonitorRslValue": hzQtmRlsMakeRslMonitorRslValue,
       "hzQtmRlsMakeRslMonitorPeriod": hzQtmRlsMakeRslMonitorPeriod,
       "hzQtmRlsStatus": hzQtmRlsStatus,
       "hzQtmRlsCurrentDroppedFramesTable": hzQtmRlsCurrentDroppedFramesTable,
       "hzQtmRlsCurrentDroppedFramesEntry": hzQtmRlsCurrentDroppedFramesEntry,
       "hzQtmRlsCurrentDroppedFramesIndex": hzQtmRlsCurrentDroppedFramesIndex,
       "hzQtmRlsCurrentDroppedFramesRateValue": hzQtmRlsCurrentDroppedFramesRateValue,
       "hzQtmRlsCurrentDroppedFrameMonitorPeriod": hzQtmRlsCurrentDroppedFrameMonitorPeriod,
       "hzQtmRlsCurrentQueueStatus": hzQtmRlsCurrentQueueStatus,
       "hzQtmRlsStatusTable": hzQtmRlsStatusTable,
       "hzQtmRlsStatusEntry": hzQtmRlsStatusEntry,
       "hzQtmRlsStatusIndex": hzQtmRlsStatusIndex,
       "hzQtmRlsOption": hzQtmRlsOption,
       "hzQtmRlsState": hzQtmRlsState,
       "hzQtmRlsMismatchState": hzQtmRlsMismatchState,
       "hzQtmDegradeMonitorState": hzQtmDegradeMonitorState,
       "hzQtmHardFaultMonitorState": hzQtmHardFaultMonitorState,
       "hzQtmMakeRslThresholdState": hzQtmMakeRslThresholdState,
       "hzQtmPeerRlsState": hzQtmPeerRlsState,
       "hzQtmRadioInterfaceState": hzQtmRadioInterfaceState,
       "hzQtmNetworkInterfaceState": hzQtmNetworkInterfaceState,
       "hzQtmUserConfiguredEstablishFer": hzQtmUserConfiguredEstablishFer,
       "hzQtmMinimumAchievableEstablishFer": hzQtmMinimumAchievableEstablishFer,
       "hzQtmUserConfiguredShutdownFer": hzQtmUserConfiguredShutdownFer,
       "hzQtmMinimumAchievableShutdownFer": hzQtmMinimumAchievableShutdownFer,
       "hzQtmUserConfiguredEstablishMonitorTime": hzQtmUserConfiguredEstablishMonitorTime,
       "hzQtmActualEstablishMonitorTime": hzQtmActualEstablishMonitorTime,
       "hzQtmUserConfiguredShutdownMonitorTime": hzQtmUserConfiguredShutdownMonitorTime,
       "hzQtmActualShutdownMonitorTime": hzQtmActualShutdownMonitorTime,
       "hzQtmRlsPortGroup": hzQtmRlsPortGroup,
       "hzQtmRlsPort1": hzQtmRlsPort1,
       "hzQtmRlsPort2": hzQtmRlsPort2,
       "hzQtmRlsPort3": hzQtmRlsPort3,
       "hzQtmRlsPort4": hzQtmRlsPort4,
       "hzQtmRlsPort5": hzQtmRlsPort5,
       "hzQtmRlsPort6": hzQtmRlsPort6,
       "hzQtmRlsPort7": hzQtmRlsPort7,
       "hzQtmRlsPort8": hzQtmRlsPort8,
       "hzQtmRlsPauseEnable": hzQtmRlsPauseEnable,
       "hzQtmSntp": hzQtmSntp,
       "hzQtmSntpEnable": hzQtmSntpEnable,
       "hzQtmSntpOffset": hzQtmSntpOffset,
       "hzQtmSntpServerTable": hzQtmSntpServerTable,
       "hzQtmSntpServerEntry": hzQtmSntpServerEntry,
       "hzQtmSntpServerIndex": hzQtmSntpServerIndex,
       "hzQtmSntpServerIpAddress": hzQtmSntpServerIpAddress,
       "hzQtmSntpServerStatus": hzQtmSntpServerStatus,
       "hzQtmSntpServerStratum": hzQtmSntpServerStratum,
       "hzQtmSntpRestoreDefault": hzQtmSntpRestoreDefault,
       "hzQtmLogs": hzQtmLogs,
       "hzQtmEventLogEnable": hzQtmEventLogEnable,
       "hzQtmPerfmLogEnable": hzQtmPerfmLogEnable,
       "hzQtmPerfmLogInterval": hzQtmPerfmLogInterval,
       "hzQtmSysLog": hzQtmSysLog,
       "hzQtmSysLogEnable": hzQtmSysLogEnable,
       "hzQtmSysLogIpAddress": hzQtmSysLogIpAddress,
       "hzQtmRadius": hzQtmRadius,
       "hzQtmRadiusSuperUserAuthentication": hzQtmRadiusSuperUserAuthentication,
       "hzQtmRadiusServerTimeOut": hzQtmRadiusServerTimeOut,
       "hzQtmRadiusServerDeadTime": hzQtmRadiusServerDeadTime,
       "hzQtmRadiusServerReTransmit": hzQtmRadiusServerReTransmit,
       "hzQtmRadiusServerTable": hzQtmRadiusServerTable,
       "hzQtmRadiusServerEntry": hzQtmRadiusServerEntry,
       "hzQtmRadiusServerIndex": hzQtmRadiusServerIndex,
       "hzQtmRadiusCfgdHostIpAddress": hzQtmRadiusCfgdHostIpAddress,
       "hzQtmRadiusActiveHostIpAddress": hzQtmRadiusActiveHostIpAddress,
       "hzQtmSnmpNotifications": hzQtmSnmpNotifications,
       "hzQtmLinkDown": hzQtmLinkDown,
       "hzQtmLinkUp": hzQtmLinkUp,
       "hzQtmExplicitAuthenticationFailure": hzQtmExplicitAuthenticationFailure,
       "hzQtmExplicitAuthenticationFailureCleared": hzQtmExplicitAuthenticationFailureCleared,
       "hzQtmHitlessAamConfigMisMatch": hzQtmHitlessAamConfigMisMatch,
       "hzQtmHitlessAamConfigMisMatchCleared": hzQtmHitlessAamConfigMisMatchCleared,
       "hzQtmHitlessAamActive": hzQtmHitlessAamActive,
       "hzQtmHitlessAamActiveCleared": hzQtmHitlessAamActiveCleared,
       "hzQtmAtpcConfigMismatch": hzQtmAtpcConfigMismatch,
       "hzQtmAtpcConfigMismatchCleared": hzQtmAtpcConfigMismatchCleared,
       "hzQtmSntpServersUnreachable": hzQtmSntpServersUnreachable,
       "hzQtmSntpServersUnreachableCleared": hzQtmSntpServersUnreachableCleared,
       "hzQtmFrequencyFileInvalid": hzQtmFrequencyFileInvalid,
       "hzQtmDroppedFramesThresholdExceeded": hzQtmDroppedFramesThresholdExceeded,
       "hzQtmDroppedFramesThresholdExceededCleared": hzQtmDroppedFramesThresholdExceededCleared,
       "hzQtmBwUtilizationThresholdExceeded": hzQtmBwUtilizationThresholdExceeded,
       "hzQtmBwUtilizationThresholdExceededCleared": hzQtmBwUtilizationThresholdExceededCleared,
       "hzQtmRlsMismatch": hzQtmRlsMismatch,
       "hzQtmRlsMismatchCleared": hzQtmRlsMismatchCleared,
       "hzQtmRlsQueueBasedShutdownActivated": hzQtmRlsQueueBasedShutdownActivated,
       "hzQtmRlsQueueBasedShutdownActivatedCleared": hzQtmRlsQueueBasedShutdownActivatedCleared,
       "hzQtmModemRxLossOfSignalLock": hzQtmModemRxLossOfSignalLock,
       "hzQtmModemRxLossOfSignalLockCleared": hzQtmModemRxLossOfSignalLockCleared,
       "hzQtmModemTxLossOfSync": hzQtmModemTxLossOfSync,
       "hzQtmModemTxLossOfSyncCleared": hzQtmModemTxLossOfSyncCleared,
       "hzQtmModemSnrBelowThreshold": hzQtmModemSnrBelowThreshold,
       "hzQtmModemSnrBelowThresholdCleared": hzQtmModemSnrBelowThresholdCleared,
       "hzQtmModemEqualizerStressExceedThreshold": hzQtmModemEqualizerStressExceedThreshold,
       "hzQtmModemEqualizerStressExceedThresholdCleared": hzQtmModemEqualizerStressExceedThresholdCleared,
       "hzQtmModemChannelizedRslBelowThreshold": hzQtmModemChannelizedRslBelowThreshold,
       "hzQtmModemChannelizedRslBelowThresholdCleared": hzQtmModemChannelizedRslBelowThresholdCleared,
       "hzQtmFpgaProgrammingError": hzQtmFpgaProgrammingError,
       "hzQtmFpgaProgrammingErrorCleared": hzQtmFpgaProgrammingErrorCleared,
       "hzQtmUserSessionCommenced": hzQtmUserSessionCommenced,
       "hzQtmUserSessionTerminated": hzQtmUserSessionTerminated,
       "hzQtmAtpcTxAtMaxPwr": hzQtmAtpcTxAtMaxPwr,
       "hzQtmAtpcTxAtMaxPwrCleared": hzQtmAtpcTxAtMaxPwrCleared,
       "hzQtmRadioSynthLostLock": hzQtmRadioSynthLostLock,
       "hzQtmRadioSynthLostLockCleared": hzQtmRadioSynthLostLockCleared,
       "hzQtmRadioLostCommunication": hzQtmRadioLostCommunication,
       "hzQtmRadioLostCommunicationCleared": hzQtmRadioLostCommunicationCleared,
       "hzQtmRadioMismatch": hzQtmRadioMismatch,
       "hzQtmRadioMismatchCleared": hzQtmRadioMismatchCleared,
       "hzQtmRadioPowerAmp": hzQtmRadioPowerAmp,
       "hzQtmRadioPowerAmpCleared": hzQtmRadioPowerAmpCleared,
       "hzQtmRadioExcessiveTxCableLoss": hzQtmRadioExcessiveTxCableLoss,
       "hzQtmRadioExcessiveTxCableLossCleared": hzQtmRadioExcessiveTxCableLossCleared,
       "hzQtmHiPowerRadioTxDetector": hzQtmHiPowerRadioTxDetector,
       "hzQtmHiPowerRadioTxDetectorCleared": hzQtmHiPowerRadioTxDetectorCleared,
       "hzQtmSecondaryRadioIsActive": hzQtmSecondaryRadioIsActive,
       "hzQtmSecondaryRadioIsActiveCleared": hzQtmSecondaryRadioIsActiveCleared,
       "hzQtmRedundancySerialNumberMisMatch": hzQtmRedundancySerialNumberMisMatch,
       "hzQtmRedundancySerialNumberMisMatchCleared": hzQtmRedundancySerialNumberMisMatchCleared,
       "hzQtmRadioFirmwareMismatch": hzQtmRadioFirmwareMismatch,
       "hzQtmRadioFirmwareMismatchCleared": hzQtmRadioFirmwareMismatchCleared,
       "hzQtmSecondaryRadioNotdetected": hzQtmSecondaryRadioNotdetected,
       "hzQtmSecondaryRadioNotdetectedCleared": hzQtmSecondaryRadioNotdetectedCleared,
       "hzQtmPrimaryRadioNotdetected": hzQtmPrimaryRadioNotdetected,
       "hzQtmPrimaryRadioNotdetectedCleared": hzQtmPrimaryRadioNotdetectedCleared,
       "hzQtmFaultyPrimaryRadio": hzQtmFaultyPrimaryRadio,
       "hzQtmFaultyPrimaryRadioCleared": hzQtmFaultyPrimaryRadioCleared,
       "hzQtmRadioExcessiveTxCableLossChange": hzQtmRadioExcessiveTxCableLossChange,
       "hzQtmRadioExcessiveTxCableLossChangeCleared": hzQtmRadioExcessiveTxCableLossChangeCleared,
       "hzQtmExcessiveRxCableLoss": hzQtmExcessiveRxCableLoss,
       "hzQtmExcessiveRxCableLossCleared": hzQtmExcessiveRxCableLossCleared,
       "hzQtmRedundancyPrimaryPortNotSet": hzQtmRedundancyPrimaryPortNotSet,
       "hzQtmRedundancyPrimaryPortNotSetCleared": hzQtmRedundancyPrimaryPortNotSetCleared,
       "hzQtmRedundancySecondaryPortIsActive": hzQtmRedundancySecondaryPortIsActive,
       "hzQtmRedundancySecondaryPortIsActiveCleared": hzQtmRedundancySecondaryPortIsActiveCleared,
       "hzQtmRedundancyPrimaryPortFaulty": hzQtmRedundancyPrimaryPortFaulty,
       "hzQtmRedundancyPrimaryPortFaultyCleared": hzQtmRedundancyPrimaryPortFaultyCleared,
       "hzQtmRedundancySecondaryPortFaulty": hzQtmRedundancySecondaryPortFaulty,
       "hzQtmRedundancySecondaryPortFaultyCleared": hzQtmRedundancySecondaryPortFaultyCleared,
       "hzQtmFanFailed": hzQtmFanFailed,
       "hzQtmFanFailureCleared": hzQtmFanFailureCleared,
       "hzQtmModemRlsShutdownActivated": hzQtmModemRlsShutdownActivated,
       "hzQtmModemRlsShutdownActivatedCleared": hzQtmModemRlsShutdownActivatedCleared,
       "hzQtmRadioUnitHwChanged": hzQtmRadioUnitHwChanged,
       "hzQtmRadioSwDownloadFailed": hzQtmRadioSwDownloadFailed,
       "hzQtmRadioSwDownloadFailedCleared": hzQtmRadioSwDownloadFailedCleared,
       "hzQtmRadioRestartedOK": hzQtmRadioRestartedOK,
       "hzQtmMibChangeNotSaved": hzQtmMibChangeNotSaved,
       "hzQtmMibChangeNotSavedCleared": hzQtmMibChangeNotSavedCleared,
       "hzQtmRadioDrainCurrent": hzQtmRadioDrainCurrent,
       "hzQtmRadioDrainCurrentCleared": hzQtmRadioDrainCurrentCleared,
       "hzQtmIFSynthLostLock": hzQtmIFSynthLostLock,
       "hzQtmIFSynthLostLockCleared": hzQtmIFSynthLostLockCleared,
       "hzQtmInvalidSystemConfig": hzQtmInvalidSystemConfig,
       "hzQtmInvalidSystemConfigCleared": hzQtmInvalidSystemConfigCleared,
       "hzQtmHitlessAamEvent": hzQtmHitlessAamEvent,
       "hzQtmModemXPICEquStressExceedThreshold": hzQtmModemXPICEquStressExceedThreshold,
       "hzQtmModemXPICEquStressExceedThresholdCleared": hzQtmModemXPICEquStressExceedThresholdCleared,
       "hzQtmPartnerNodeAlarmIndication": hzQtmPartnerNodeAlarmIndication,
       "hzQtmPartnerNodeAlarmIndicationCleared": hzQtmPartnerNodeAlarmIndicationCleared,
       "hzQtmBandwidthDoublingInvalidLinkConfig": hzQtmBandwidthDoublingInvalidLinkConfig,
       "hzQtmBandwidthDoublingInvalidLinkConfigCleared": hzQtmBandwidthDoublingInvalidLinkConfigCleared,
       "hzQtmBandwidthDoublingWrongPortConnected": hzQtmBandwidthDoublingWrongPortConnected,
       "hzQtmBandwidthDoublingWrongPortConnectedCleared": hzQtmBandwidthDoublingWrongPortConnectedCleared,
       "hzQtmRadioPowerOff": hzQtmRadioPowerOff,
       "hzQtmRadioPowerOffCleared": hzQtmRadioPowerOffCleared,
       "hzQtmSynceLostLock": hzQtmSynceLostLock,
       "hzQtmSynceLostLockCleared": hzQtmSynceLostLockCleared,
       "hzQtmSynceSecondarySourceInUse": hzQtmSynceSecondarySourceInUse,
       "hzQtmSynceSecondarySourceInUseCleared": hzQtmSynceSecondarySourceInUseCleared,
       "hzQtmReserved": hzQtmReserved,
       "hzQtmModIdentity": hzQtmModIdentity}
)
