# SNMP MIB module (CIENA-6500R-INVENTORY-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\ciena\CIENA-6500R-INVENTORY-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:24:18 2025
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

(rlsInventory,) = mibBuilder.importSymbols(
    "CIENA-6500R-SLOTS-MIB",
    "rlsInventory")

(AdminState,
 BandOccupancy,
 MeansurementType,
 PecCode,
 PowerEnum,
 RamEnum,
 RestartType) = mibBuilder.importSymbols(
    "CIENA-6500R-TYPES-MIB",
    "AdminState",
    "BandOccupancy",
    "MeansurementType",
    "PecCode",
    "PowerEnum",
    "RamEnum",
    "RestartType")

(DisplayString16,
 DisplayString32,
 DisplayString64) = mibBuilder.importSymbols(
    "CIENA-PRO-TYPES-MIB",
    "DisplayString16",
    "DisplayString32",
    "DisplayString64")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

cienaRlsInventoryMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 4, 1, 1, 1)
)
if mibBuilder.loadTexts:
    cienaRlsInventoryMIB.setRevisions(
        ("2020-09-30 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_RlsCircuitPack_ObjectIdentity = ObjectIdentity
rlsCircuitPack = _RlsCircuitPack_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 4, 1, 1, 1, 1)
)
_RlsCircuitPackTable_Object = MibTable
rlsCircuitPackTable = _RlsCircuitPackTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 4, 1, 1, 1, 1, 1)
)
if mibBuilder.loadTexts:
    rlsCircuitPackTable.setStatus("current")
_RlsCircuitPackEntry_Object = MibTableRow
rlsCircuitPackEntry = _RlsCircuitPackEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 4, 1, 1, 1, 1, 1, 1)
)
rlsCircuitPackEntry.setIndexNames(
    (0, "CIENA-6500R-INVENTORY-MIB", "rlsCircuitPackSlotName"),
)
if mibBuilder.loadTexts:
    rlsCircuitPackEntry.setStatus("current")
_RlsCircuitPackSlotName_Type = DisplayString32
_RlsCircuitPackSlotName_Object = MibTableColumn
rlsCircuitPackSlotName = _RlsCircuitPackSlotName_Object(
    (1, 3, 6, 1, 4, 1, 1271, 4, 1, 1, 1, 1, 1, 1, 1),
    _RlsCircuitPackSlotName_Type()
)
rlsCircuitPackSlotName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlsCircuitPackSlotName.setStatus("current")
_RlsCircuitPackPec_Type = PecCode
_RlsCircuitPackPec_Object = MibTableColumn
rlsCircuitPackPec = _RlsCircuitPackPec_Object(
    (1, 3, 6, 1, 4, 1, 1271, 4, 1, 1, 1, 1, 1, 1, 2),
    _RlsCircuitPackPec_Type()
)
rlsCircuitPackPec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlsCircuitPackPec.setStatus("current")
_RlsCircuitPackCtype_Type = DisplayString64
_RlsCircuitPackCtype_Object = MibTableColumn
rlsCircuitPackCtype = _RlsCircuitPackCtype_Object(
    (1, 3, 6, 1, 4, 1, 1271, 4, 1, 1, 1, 1, 1, 1, 3),
    _RlsCircuitPackCtype_Type()
)
rlsCircuitPackCtype.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlsCircuitPackCtype.setStatus("current")
_RlsCircuitPackLabel_Type = DisplayString64
_RlsCircuitPackLabel_Object = MibTableColumn
rlsCircuitPackLabel = _RlsCircuitPackLabel_Object(
    (1, 3, 6, 1, 4, 1, 1271, 4, 1, 1, 1, 1, 1, 1, 4),
    _RlsCircuitPackLabel_Type()
)
rlsCircuitPackLabel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlsCircuitPackLabel.setStatus("current")


class _RlsCircuitPackLowPower_Type(Integer32):
    """Custom type rlsCircuitPackLowPower based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 960),
    )


_RlsCircuitPackLowPower_Type.__name__ = "Integer32"
_RlsCircuitPackLowPower_Object = MibTableColumn
rlsCircuitPackLowPower = _RlsCircuitPackLowPower_Object(
    (1, 3, 6, 1, 4, 1, 1271, 4, 1, 1, 1, 1, 1, 1, 5),
    _RlsCircuitPackLowPower_Type()
)
rlsCircuitPackLowPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlsCircuitPackLowPower.setStatus("current")


class _RlsCircuitPackMaxPower_Type(Integer32):
    """Custom type rlsCircuitPackMaxPower based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 960),
    )


_RlsCircuitPackMaxPower_Type.__name__ = "Integer32"
_RlsCircuitPackMaxPower_Object = MibTableColumn
rlsCircuitPackMaxPower = _RlsCircuitPackMaxPower_Object(
    (1, 3, 6, 1, 4, 1, 1271, 4, 1, 1, 1, 1, 1, 1, 6),
    _RlsCircuitPackMaxPower_Type()
)
rlsCircuitPackMaxPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlsCircuitPackMaxPower.setStatus("current")
_RlsCircuitPackAdminState_Type = AdminState
_RlsCircuitPackAdminState_Object = MibTableColumn
rlsCircuitPackAdminState = _RlsCircuitPackAdminState_Object(
    (1, 3, 6, 1, 4, 1, 1271, 4, 1, 1, 1, 1, 1, 1, 7),
    _RlsCircuitPackAdminState_Type()
)
rlsCircuitPackAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlsCircuitPackAdminState.setStatus("current")


class _RlsCircuitPackOperationalState_Type(Integer32):
    """Custom type rlsCircuitPackOperationalState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("active", 0),
          ("idle", 1))
    )


_RlsCircuitPackOperationalState_Type.__name__ = "Integer32"
_RlsCircuitPackOperationalState_Object = MibTableColumn
rlsCircuitPackOperationalState = _RlsCircuitPackOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 1271, 4, 1, 1, 1, 1, 1, 1, 8),
    _RlsCircuitPackOperationalState_Type()
)
rlsCircuitPackOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlsCircuitPackOperationalState.setStatus("current")


class _RlsCircuitPackSlotType_Type(Integer32):
    """Custom type rlsCircuitPackSlotType based on Integer32"""
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
        *(("single", 0),
          ("doubleWide", 1),
          ("doubleHigh", 2),
          ("quad", 3),
          ("tripleHigh", 4))
    )


_RlsCircuitPackSlotType_Type.__name__ = "Integer32"
_RlsCircuitPackSlotType_Object = MibTableColumn
rlsCircuitPackSlotType = _RlsCircuitPackSlotType_Object(
    (1, 3, 6, 1, 4, 1, 1271, 4, 1, 1, 1, 1, 1, 1, 9),
    _RlsCircuitPackSlotType_Type()
)
rlsCircuitPackSlotType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlsCircuitPackSlotType.setStatus("current")
_RlsCircuitPackType_Type = DisplayString32
_RlsCircuitPackType_Object = MibTableColumn
rlsCircuitPackType = _RlsCircuitPackType_Object(
    (1, 3, 6, 1, 4, 1, 1271, 4, 1, 1, 1, 1, 1, 1, 10),
    _RlsCircuitPackType_Type()
)
rlsCircuitPackType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlsCircuitPackType.setStatus("current")


class _RlsCircuitPackFormFactor_Type(Integer32):
    """Custom type rlsCircuitPackFormFactor based on Integer32"""
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
              9,
              10,
              11,
              12,
              13,
              14,
              15)
        )
    )
    namedValues = NamedValues(
        *(("backplane", 0),
          ("accessPanel", 1),
          ("ctm", 2),
          ("fan", 3),
          ("power", 4),
          ("i2c", 5),
          ("passive", 6),
          ("sfp", 7),
          ("sfpplus", 8),
          ("cfp", 9),
          ("cfp2", 10),
          ("xfp", 11),
          ("qsfp", 12),
          ("qsfp28", 13),
          ("ctmFrontPanel", 14),
          ("backplane300mm", 15))
    )


_RlsCircuitPackFormFactor_Type.__name__ = "Integer32"
_RlsCircuitPackFormFactor_Object = MibTableColumn
rlsCircuitPackFormFactor = _RlsCircuitPackFormFactor_Object(
    (1, 3, 6, 1, 4, 1, 1271, 4, 1, 1, 1, 1, 1, 1, 11),
    _RlsCircuitPackFormFactor_Type()
)
rlsCircuitPackFormFactor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlsCircuitPackFormFactor.setStatus("current")
_RlsCircuitPackPowerType_Type = PowerEnum
_RlsCircuitPackPowerType_Object = MibTableColumn
rlsCircuitPackPowerType = _RlsCircuitPackPowerType_Object(
    (1, 3, 6, 1, 4, 1, 1271, 4, 1, 1, 1, 1, 1, 1, 12),
    _RlsCircuitPackPowerType_Type()
)
rlsCircuitPackPowerType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlsCircuitPackPowerType.setStatus("current")
_RlsCircuitPackRamSize_Type = RamEnum
_RlsCircuitPackRamSize_Object = MibTableColumn
rlsCircuitPackRamSize = _RlsCircuitPackRamSize_Object(
    (1, 3, 6, 1, 4, 1, 1271, 4, 1, 1, 1, 1, 1, 1, 13),
    _RlsCircuitPackRamSize_Type()
)
rlsCircuitPackRamSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlsCircuitPackRamSize.setStatus("current")
_RlsCircuitPackBandInfo_Type = BandOccupancy
_RlsCircuitPackBandInfo_Object = MibTableColumn
rlsCircuitPackBandInfo = _RlsCircuitPackBandInfo_Object(
    (1, 3, 6, 1, 4, 1, 1271, 4, 1, 1, 1, 1, 1, 1, 14),
    _RlsCircuitPackBandInfo_Type()
)
rlsCircuitPackBandInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlsCircuitPackBandInfo.setStatus("current")


class _RlsCircuitPackCctEncoding_Type(Integer32):
    """Custom type rlsCircuitPackCctEncoding based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("snBin", 1),
          ("xml", 2))
    )


_RlsCircuitPackCctEncoding_Type.__name__ = "Integer32"
_RlsCircuitPackCctEncoding_Object = MibTableColumn
rlsCircuitPackCctEncoding = _RlsCircuitPackCctEncoding_Object(
    (1, 3, 6, 1, 4, 1, 1271, 4, 1, 1, 1, 1, 1, 1, 15),
    _RlsCircuitPackCctEncoding_Type()
)
rlsCircuitPackCctEncoding.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlsCircuitPackCctEncoding.setStatus("current")
_RlsCircuitPackDiagActive_Type = TruthValue
_RlsCircuitPackDiagActive_Object = MibTableColumn
rlsCircuitPackDiagActive = _RlsCircuitPackDiagActive_Object(
    (1, 3, 6, 1, 4, 1, 1271, 4, 1, 1, 1, 1, 1, 1, 16),
    _RlsCircuitPackDiagActive_Type()
)
rlsCircuitPackDiagActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlsCircuitPackDiagActive.setStatus("current")
_RlsCircuitPackDiagFailed_Type = TruthValue
_RlsCircuitPackDiagFailed_Object = MibTableColumn
rlsCircuitPackDiagFailed = _RlsCircuitPackDiagFailed_Object(
    (1, 3, 6, 1, 4, 1, 1271, 4, 1, 1, 1, 1, 1, 1, 17),
    _RlsCircuitPackDiagFailed_Type()
)
rlsCircuitPackDiagFailed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlsCircuitPackDiagFailed.setStatus("current")
_RlsCircuitPackDiagHardwareSubsystemFailed_Type = TruthValue
_RlsCircuitPackDiagHardwareSubsystemFailed_Object = MibTableColumn
rlsCircuitPackDiagHardwareSubsystemFailed = _RlsCircuitPackDiagHardwareSubsystemFailed_Object(
    (1, 3, 6, 1, 4, 1, 1271, 4, 1, 1, 1, 1, 1, 1, 18),
    _RlsCircuitPackDiagHardwareSubsystemFailed_Type()
)
rlsCircuitPackDiagHardwareSubsystemFailed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlsCircuitPackDiagHardwareSubsystemFailed.setStatus("current")
_RlsCircuitPackDiagSoftwareSubsytemFailed_Type = TruthValue
_RlsCircuitPackDiagSoftwareSubsytemFailed_Object = MibTableColumn
rlsCircuitPackDiagSoftwareSubsytemFailed = _RlsCircuitPackDiagSoftwareSubsytemFailed_Object(
    (1, 3, 6, 1, 4, 1, 1271, 4, 1, 1, 1, 1, 1, 1, 19),
    _RlsCircuitPackDiagSoftwareSubsytemFailed_Type()
)
rlsCircuitPackDiagSoftwareSubsytemFailed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlsCircuitPackDiagSoftwareSubsytemFailed.setStatus("current")
_RlsCircuitPackDiagHiTempWarning_Type = TruthValue
_RlsCircuitPackDiagHiTempWarning_Object = MibTableColumn
rlsCircuitPackDiagHiTempWarning = _RlsCircuitPackDiagHiTempWarning_Object(
    (1, 3, 6, 1, 4, 1, 1271, 4, 1, 1, 1, 1, 1, 1, 20),
    _RlsCircuitPackDiagHiTempWarning_Type()
)
rlsCircuitPackDiagHiTempWarning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlsCircuitPackDiagHiTempWarning.setStatus("current")
_RlsCircuitPackDiagHiTemp_Type = TruthValue
_RlsCircuitPackDiagHiTemp_Object = MibTableColumn
rlsCircuitPackDiagHiTemp = _RlsCircuitPackDiagHiTemp_Object(
    (1, 3, 6, 1, 4, 1, 1271, 4, 1, 1, 1, 1, 1, 1, 21),
    _RlsCircuitPackDiagHiTemp_Type()
)
rlsCircuitPackDiagHiTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlsCircuitPackDiagHiTemp.setStatus("current")
_RlsCircuitPackHardwareRelease_Type = DisplayString32
_RlsCircuitPackHardwareRelease_Object = MibTableColumn
rlsCircuitPackHardwareRelease = _RlsCircuitPackHardwareRelease_Object(
    (1, 3, 6, 1, 4, 1, 1271, 4, 1, 1, 1, 1, 1, 1, 22),
    _RlsCircuitPackHardwareRelease_Type()
)
rlsCircuitPackHardwareRelease.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlsCircuitPackHardwareRelease.setStatus("current")
_RlsCircuitPackCommonLanguageEquipmentIndentifier_Type = DisplayString32
_RlsCircuitPackCommonLanguageEquipmentIndentifier_Object = MibTableColumn
rlsCircuitPackCommonLanguageEquipmentIndentifier = _RlsCircuitPackCommonLanguageEquipmentIndentifier_Object(
    (1, 3, 6, 1, 4, 1, 1271, 4, 1, 1, 1, 1, 1, 1, 23),
    _RlsCircuitPackCommonLanguageEquipmentIndentifier_Type()
)
rlsCircuitPackCommonLanguageEquipmentIndentifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlsCircuitPackCommonLanguageEquipmentIndentifier.setStatus("current")
_RlsCircuitPackSerialNumber_Type = DisplayString32
_RlsCircuitPackSerialNumber_Object = MibTableColumn
rlsCircuitPackSerialNumber = _RlsCircuitPackSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 1271, 4, 1, 1, 1, 1, 1, 1, 24),
    _RlsCircuitPackSerialNumber_Type()
)
rlsCircuitPackSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlsCircuitPackSerialNumber.setStatus("current")
_RlsCircuitPackManufacturingDate_Type = DisplayString32
_RlsCircuitPackManufacturingDate_Object = MibTableColumn
rlsCircuitPackManufacturingDate = _RlsCircuitPackManufacturingDate_Object(
    (1, 3, 6, 1, 4, 1, 1271, 4, 1, 1, 1, 1, 1, 1, 25),
    _RlsCircuitPackManufacturingDate_Type()
)
rlsCircuitPackManufacturingDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlsCircuitPackManufacturingDate.setStatus("current")
_RlsCircuitPackAge_Type = DisplayString16
_RlsCircuitPackAge_Object = MibTableColumn
rlsCircuitPackAge = _RlsCircuitPackAge_Object(
    (1, 3, 6, 1, 4, 1, 1271, 4, 1, 1, 1, 1, 1, 1, 26),
    _RlsCircuitPackAge_Type()
)
rlsCircuitPackAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlsCircuitPackAge.setStatus("current")
_RlsCircuitPackUptime_Type = DisplayString16
_RlsCircuitPackUptime_Object = MibTableColumn
rlsCircuitPackUptime = _RlsCircuitPackUptime_Object(
    (1, 3, 6, 1, 4, 1, 1271, 4, 1, 1, 1, 1, 1, 1, 27),
    _RlsCircuitPackUptime_Type()
)
rlsCircuitPackUptime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlsCircuitPackUptime.setStatus("current")
_RlsCircuitPackLastRestartType_Type = RestartType
_RlsCircuitPackLastRestartType_Object = MibTableColumn
rlsCircuitPackLastRestartType = _RlsCircuitPackLastRestartType_Object(
    (1, 3, 6, 1, 4, 1, 1271, 4, 1, 1, 1, 1, 1, 1, 28),
    _RlsCircuitPackLastRestartType_Type()
)
rlsCircuitPackLastRestartType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlsCircuitPackLastRestartType.setStatus("current")
_RlsCircuitPackCurrTemprature_Type = Integer32
_RlsCircuitPackCurrTemprature_Object = MibTableColumn
rlsCircuitPackCurrTemprature = _RlsCircuitPackCurrTemprature_Object(
    (1, 3, 6, 1, 4, 1, 1271, 4, 1, 1, 1, 1, 1, 1, 29),
    _RlsCircuitPackCurrTemprature_Type()
)
rlsCircuitPackCurrTemprature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlsCircuitPackCurrTemprature.setStatus("current")
_RlsCircuitPackAvgTemprature_Type = Integer32
_RlsCircuitPackAvgTemprature_Object = MibTableColumn
rlsCircuitPackAvgTemprature = _RlsCircuitPackAvgTemprature_Object(
    (1, 3, 6, 1, 4, 1, 1271, 4, 1, 1, 1, 1, 1, 1, 30),
    _RlsCircuitPackAvgTemprature_Type()
)
rlsCircuitPackAvgTemprature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlsCircuitPackAvgTemprature.setStatus("current")
_RlsCircuitPackFanSpeedValue_Type = Integer32
_RlsCircuitPackFanSpeedValue_Object = MibTableColumn
rlsCircuitPackFanSpeedValue = _RlsCircuitPackFanSpeedValue_Object(
    (1, 3, 6, 1, 4, 1, 1271, 4, 1, 1, 1, 1, 1, 1, 31),
    _RlsCircuitPackFanSpeedValue_Type()
)
rlsCircuitPackFanSpeedValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlsCircuitPackFanSpeedValue.setStatus("current")
if mibBuilder.loadTexts:
    rlsCircuitPackFanSpeedValue.setUnits("rpm")
_RlsCircuitPackFanSpeedMeansurementType_Type = MeansurementType
_RlsCircuitPackFanSpeedMeansurementType_Object = MibTableColumn
rlsCircuitPackFanSpeedMeansurementType = _RlsCircuitPackFanSpeedMeansurementType_Object(
    (1, 3, 6, 1, 4, 1, 1271, 4, 1, 1, 1, 1, 1, 1, 32),
    _RlsCircuitPackFanSpeedMeansurementType_Type()
)
rlsCircuitPackFanSpeedMeansurementType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlsCircuitPackFanSpeedMeansurementType.setStatus("current")
_RlsCircuitPackCurrPowerValue_Type = Integer32
_RlsCircuitPackCurrPowerValue_Object = MibTableColumn
rlsCircuitPackCurrPowerValue = _RlsCircuitPackCurrPowerValue_Object(
    (1, 3, 6, 1, 4, 1, 1271, 4, 1, 1, 1, 1, 1, 1, 33),
    _RlsCircuitPackCurrPowerValue_Type()
)
rlsCircuitPackCurrPowerValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlsCircuitPackCurrPowerValue.setStatus("current")
if mibBuilder.loadTexts:
    rlsCircuitPackCurrPowerValue.setUnits("W")
_RlsCircuitPackCurrPowerMeansurementType_Type = MeansurementType
_RlsCircuitPackCurrPowerMeansurementType_Object = MibTableColumn
rlsCircuitPackCurrPowerMeansurementType = _RlsCircuitPackCurrPowerMeansurementType_Object(
    (1, 3, 6, 1, 4, 1, 1271, 4, 1, 1, 1, 1, 1, 1, 34),
    _RlsCircuitPackCurrPowerMeansurementType_Type()
)
rlsCircuitPackCurrPowerMeansurementType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlsCircuitPackCurrPowerMeansurementType.setStatus("current")
_RlsCircuitPackPoweredUpTime_Type = DisplayString16
_RlsCircuitPackPoweredUpTime_Object = MibTableColumn
rlsCircuitPackPoweredUpTime = _RlsCircuitPackPoweredUpTime_Object(
    (1, 3, 6, 1, 4, 1, 1271, 4, 1, 1, 1, 1, 1, 1, 35),
    _RlsCircuitPackPoweredUpTime_Type()
)
rlsCircuitPackPoweredUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlsCircuitPackPoweredUpTime.setStatus("current")
_RlsInventoryAmps_ObjectIdentity = ObjectIdentity
rlsInventoryAmps = _RlsInventoryAmps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 4, 1, 1, 1, 2)
)
_RlsInventoryProtectionGrp_ObjectIdentity = ObjectIdentity
rlsInventoryProtectionGrp = _RlsInventoryProtectionGrp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 4, 1, 1, 1, 3)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CIENA-6500R-INVENTORY-MIB",
    **{"cienaRlsInventoryMIB": cienaRlsInventoryMIB,
       "rlsCircuitPack": rlsCircuitPack,
       "rlsCircuitPackTable": rlsCircuitPackTable,
       "rlsCircuitPackEntry": rlsCircuitPackEntry,
       "rlsCircuitPackSlotName": rlsCircuitPackSlotName,
       "rlsCircuitPackPec": rlsCircuitPackPec,
       "rlsCircuitPackCtype": rlsCircuitPackCtype,
       "rlsCircuitPackLabel": rlsCircuitPackLabel,
       "rlsCircuitPackLowPower": rlsCircuitPackLowPower,
       "rlsCircuitPackMaxPower": rlsCircuitPackMaxPower,
       "rlsCircuitPackAdminState": rlsCircuitPackAdminState,
       "rlsCircuitPackOperationalState": rlsCircuitPackOperationalState,
       "rlsCircuitPackSlotType": rlsCircuitPackSlotType,
       "rlsCircuitPackType": rlsCircuitPackType,
       "rlsCircuitPackFormFactor": rlsCircuitPackFormFactor,
       "rlsCircuitPackPowerType": rlsCircuitPackPowerType,
       "rlsCircuitPackRamSize": rlsCircuitPackRamSize,
       "rlsCircuitPackBandInfo": rlsCircuitPackBandInfo,
       "rlsCircuitPackCctEncoding": rlsCircuitPackCctEncoding,
       "rlsCircuitPackDiagActive": rlsCircuitPackDiagActive,
       "rlsCircuitPackDiagFailed": rlsCircuitPackDiagFailed,
       "rlsCircuitPackDiagHardwareSubsystemFailed": rlsCircuitPackDiagHardwareSubsystemFailed,
       "rlsCircuitPackDiagSoftwareSubsytemFailed": rlsCircuitPackDiagSoftwareSubsytemFailed,
       "rlsCircuitPackDiagHiTempWarning": rlsCircuitPackDiagHiTempWarning,
       "rlsCircuitPackDiagHiTemp": rlsCircuitPackDiagHiTemp,
       "rlsCircuitPackHardwareRelease": rlsCircuitPackHardwareRelease,
       "rlsCircuitPackCommonLanguageEquipmentIndentifier": rlsCircuitPackCommonLanguageEquipmentIndentifier,
       "rlsCircuitPackSerialNumber": rlsCircuitPackSerialNumber,
       "rlsCircuitPackManufacturingDate": rlsCircuitPackManufacturingDate,
       "rlsCircuitPackAge": rlsCircuitPackAge,
       "rlsCircuitPackUptime": rlsCircuitPackUptime,
       "rlsCircuitPackLastRestartType": rlsCircuitPackLastRestartType,
       "rlsCircuitPackCurrTemprature": rlsCircuitPackCurrTemprature,
       "rlsCircuitPackAvgTemprature": rlsCircuitPackAvgTemprature,
       "rlsCircuitPackFanSpeedValue": rlsCircuitPackFanSpeedValue,
       "rlsCircuitPackFanSpeedMeansurementType": rlsCircuitPackFanSpeedMeansurementType,
       "rlsCircuitPackCurrPowerValue": rlsCircuitPackCurrPowerValue,
       "rlsCircuitPackCurrPowerMeansurementType": rlsCircuitPackCurrPowerMeansurementType,
       "rlsCircuitPackPoweredUpTime": rlsCircuitPackPoweredUpTime,
       "rlsInventoryAmps": rlsInventoryAmps,
       "rlsInventoryProtectionGrp": rlsInventoryProtectionGrp}
)
