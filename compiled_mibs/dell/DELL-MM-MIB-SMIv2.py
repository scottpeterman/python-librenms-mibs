# SNMP MIB module (DELL-MM-MIB-SMIv2) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\dell\DELL-MM-MIB-SMIv2
# Produced by pysmi-1.6.2 at Thu Oct  2 11:35:32 2025
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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



class DellString(TextualConvention, OctetString):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 1023),
    )



class DellMmType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("unknown", 2),
          ("mxMM", 3))
    )



class DellStatus(TextualConvention, Integer32):
    status = "current"
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
        *(("other", 1),
          ("unknown", 2),
          ("ok", 3),
          ("nonCritical", 4),
          ("critical", 5),
          ("nonRecoverable", 6))
    )



class DellPowerReading(TextualConvention, OctetString):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )



class DellPowerIndexRange(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )



class DellPSUIndexRange(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 6),
    )



class DellPSUCapable(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("absent", 1),
          ("none", 2),
          ("basic", 3))
    )



class DellTemperatureReading(TextualConvention, Integer32):
    status = "current"


class DellTimestamp(TextualConvention, OctetString):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(26, 26),
    )
    fixed_length = 26



# MIB Managed Objects in the order of their OIDs

_Dell_ObjectIdentity = ObjectIdentity
dell = _Dell_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674)
)
_Server3_ObjectIdentity = ObjectIdentity
server3 = _Server3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10892)
)
_DmmOutOfBandGroup_ObjectIdentity = ObjectIdentity
dmmOutOfBandGroup = _DmmOutOfBandGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6)
)
_DmmInformationGroup_ObjectIdentity = ObjectIdentity
dmmInformationGroup = _DmmInformationGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 1)
)
_DmmProductInfoGroup_ObjectIdentity = ObjectIdentity
dmmProductInfoGroup = _DmmProductInfoGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 1, 1)
)
_DmmProductName_Type = DellString
_DmmProductName_Object = MibScalar
dmmProductName = _DmmProductName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 1, 1, 1),
    _DmmProductName_Type()
)
dmmProductName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dmmProductName.setStatus("current")
_DmmProductShortName_Type = DellString
_DmmProductShortName_Object = MibScalar
dmmProductShortName = _DmmProductShortName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 1, 1, 2),
    _DmmProductShortName_Type()
)
dmmProductShortName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dmmProductShortName.setStatus("current")
_DmmProductDescription_Type = DellString
_DmmProductDescription_Object = MibScalar
dmmProductDescription = _DmmProductDescription_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 1, 1, 3),
    _DmmProductDescription_Type()
)
dmmProductDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dmmProductDescription.setStatus("current")
_DmmProductManufacturer_Type = DellString
_DmmProductManufacturer_Object = MibScalar
dmmProductManufacturer = _DmmProductManufacturer_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 1, 1, 4),
    _DmmProductManufacturer_Type()
)
dmmProductManufacturer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dmmProductManufacturer.setStatus("current")
_DmmProductVersion_Type = DellString
_DmmProductVersion_Object = MibScalar
dmmProductVersion = _DmmProductVersion_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 1, 1, 5),
    _DmmProductVersion_Type()
)
dmmProductVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dmmProductVersion.setStatus("current")
_DmmChassisServiceTag_Type = DellString
_DmmChassisServiceTag_Object = MibScalar
dmmChassisServiceTag = _DmmChassisServiceTag_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 1, 1, 6),
    _DmmChassisServiceTag_Type()
)
dmmChassisServiceTag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dmmChassisServiceTag.setStatus("current")
_DmmProductURL_Type = DellString
_DmmProductURL_Object = MibScalar
dmmProductURL = _DmmProductURL_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 1, 1, 7),
    _DmmProductURL_Type()
)
dmmProductURL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dmmProductURL.setStatus("current")
_DmmProductChassisAssetTag_Type = DellString
_DmmProductChassisAssetTag_Object = MibScalar
dmmProductChassisAssetTag = _DmmProductChassisAssetTag_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 1, 1, 8),
    _DmmProductChassisAssetTag_Type()
)
dmmProductChassisAssetTag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dmmProductChassisAssetTag.setStatus("current")
_DmmProductChassisName_Type = DellString
_DmmProductChassisName_Object = MibScalar
dmmProductChassisName = _DmmProductChassisName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 1, 1, 9),
    _DmmProductChassisName_Type()
)
dmmProductChassisName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dmmProductChassisName.setStatus("current")
_DmmProductType_Type = DellMmType
_DmmProductType_Object = MibScalar
dmmProductType = _DmmProductType_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 1, 1, 10),
    _DmmProductType_Type()
)
dmmProductType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dmmProductType.setStatus("current")
_DmmProductChassisDataCenter_Type = DellString
_DmmProductChassisDataCenter_Object = MibScalar
dmmProductChassisDataCenter = _DmmProductChassisDataCenter_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 1, 1, 11),
    _DmmProductChassisDataCenter_Type()
)
dmmProductChassisDataCenter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dmmProductChassisDataCenter.setStatus("current")
_DmmProductChassisAisle_Type = DellString
_DmmProductChassisAisle_Object = MibScalar
dmmProductChassisAisle = _DmmProductChassisAisle_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 1, 1, 12),
    _DmmProductChassisAisle_Type()
)
dmmProductChassisAisle.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dmmProductChassisAisle.setStatus("current")
_DmmProductChassisRack_Type = DellString
_DmmProductChassisRack_Object = MibScalar
dmmProductChassisRack = _DmmProductChassisRack_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 1, 1, 13),
    _DmmProductChassisRack_Type()
)
dmmProductChassisRack.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dmmProductChassisRack.setStatus("current")
_DmmProductChassisRackSlot_Type = DellString
_DmmProductChassisRackSlot_Object = MibScalar
dmmProductChassisRackSlot = _DmmProductChassisRackSlot_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 1, 1, 14),
    _DmmProductChassisRackSlot_Type()
)
dmmProductChassisRackSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dmmProductChassisRackSlot.setStatus("current")
_DmmProductChassisModel_Type = DellString
_DmmProductChassisModel_Object = MibScalar
dmmProductChassisModel = _DmmProductChassisModel_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 1, 1, 15),
    _DmmProductChassisModel_Type()
)
dmmProductChassisModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dmmProductChassisModel.setStatus("current")
_DmmProductChassisExpressServiceCode_Type = DellString
_DmmProductChassisExpressServiceCode_Object = MibScalar
dmmProductChassisExpressServiceCode = _DmmProductChassisExpressServiceCode_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 1, 1, 16),
    _DmmProductChassisExpressServiceCode_Type()
)
dmmProductChassisExpressServiceCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dmmProductChassisExpressServiceCode.setStatus("current")
_DmmProductChassisSystemID_Type = Integer32
_DmmProductChassisSystemID_Object = MibScalar
dmmProductChassisSystemID = _DmmProductChassisSystemID_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 1, 1, 17),
    _DmmProductChassisSystemID_Type()
)
dmmProductChassisSystemID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dmmProductChassisSystemID.setStatus("current")
_DmmFirmwareGroup_ObjectIdentity = ObjectIdentity
dmmFirmwareGroup = _DmmFirmwareGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 1, 2)
)
_DmmFirmwareVersion_Type = DellString
_DmmFirmwareVersion_Object = MibScalar
dmmFirmwareVersion = _DmmFirmwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 1, 2, 1),
    _DmmFirmwareVersion_Type()
)
dmmFirmwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dmmFirmwareVersion.setStatus("current")
_DmmFirmwareVersion2_Type = DellString
_DmmFirmwareVersion2_Object = MibScalar
dmmFirmwareVersion2 = _DmmFirmwareVersion2_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 1, 2, 2),
    _DmmFirmwareVersion2_Type()
)
dmmFirmwareVersion2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dmmFirmwareVersion2.setStatus("current")
_DmmStatusGroup_ObjectIdentity = ObjectIdentity
dmmStatusGroup = _DmmStatusGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 2)
)
_DmmGlobalSystemStatus_Type = DellStatus
_DmmGlobalSystemStatus_Object = MibScalar
dmmGlobalSystemStatus = _DmmGlobalSystemStatus_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 2, 1),
    _DmmGlobalSystemStatus_Type()
)
dmmGlobalSystemStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dmmGlobalSystemStatus.setStatus("current")
_DmmChassisStatusGroup_ObjectIdentity = ObjectIdentity
dmmChassisStatusGroup = _DmmChassisStatusGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 3)
)
_DmmStatusNowGroup_ObjectIdentity = ObjectIdentity
dmmStatusNowGroup = _DmmStatusNowGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 3, 1)
)
_DmmIOMCurrStatus_Type = DellStatus
_DmmIOMCurrStatus_Object = MibScalar
dmmIOMCurrStatus = _DmmIOMCurrStatus_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 3, 1, 1),
    _DmmIOMCurrStatus_Type()
)
dmmIOMCurrStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dmmIOMCurrStatus.setStatus("current")
_DmmRedCurrStatus_Type = DellStatus
_DmmRedCurrStatus_Object = MibScalar
dmmRedCurrStatus = _DmmRedCurrStatus_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 3, 1, 2),
    _DmmRedCurrStatus_Type()
)
dmmRedCurrStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dmmRedCurrStatus.setStatus("current")
_DmmPowerCurrStatus_Type = DellStatus
_DmmPowerCurrStatus_Object = MibScalar
dmmPowerCurrStatus = _DmmPowerCurrStatus_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 3, 1, 3),
    _DmmPowerCurrStatus_Type()
)
dmmPowerCurrStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dmmPowerCurrStatus.setStatus("current")
_DmmFanCurrStatus_Type = DellStatus
_DmmFanCurrStatus_Object = MibScalar
dmmFanCurrStatus = _DmmFanCurrStatus_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 3, 1, 4),
    _DmmFanCurrStatus_Type()
)
dmmFanCurrStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dmmFanCurrStatus.setStatus("current")
_DmmBladeCurrStatus_Type = DellStatus
_DmmBladeCurrStatus_Object = MibScalar
dmmBladeCurrStatus = _DmmBladeCurrStatus_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 3, 1, 5),
    _DmmBladeCurrStatus_Type()
)
dmmBladeCurrStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dmmBladeCurrStatus.setStatus("current")
_DmmTempCurrStatus_Type = DellStatus
_DmmTempCurrStatus_Object = MibScalar
dmmTempCurrStatus = _DmmTempCurrStatus_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 3, 1, 6),
    _DmmTempCurrStatus_Type()
)
dmmTempCurrStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dmmTempCurrStatus.setStatus("current")
_DmmMMCurrStatus_Type = DellStatus
_DmmMMCurrStatus_Object = MibScalar
dmmMMCurrStatus = _DmmMMCurrStatus_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 3, 1, 7),
    _DmmMMCurrStatus_Type()
)
dmmMMCurrStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dmmMMCurrStatus.setStatus("current")
_DmmChassisFrontPanelAmbientTemperature_Type = DellTemperatureReading
_DmmChassisFrontPanelAmbientTemperature_Object = MibScalar
dmmChassisFrontPanelAmbientTemperature = _DmmChassisFrontPanelAmbientTemperature_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 3, 1, 8),
    _DmmChassisFrontPanelAmbientTemperature_Type()
)
dmmChassisFrontPanelAmbientTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dmmChassisFrontPanelAmbientTemperature.setStatus("current")
_DmmChassisPowerGroup_ObjectIdentity = ObjectIdentity
dmmChassisPowerGroup = _DmmChassisPowerGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 4)
)
_DmmPowerTable_Object = MibTable
dmmPowerTable = _DmmPowerTable_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 4, 1)
)
if mibBuilder.loadTexts:
    dmmPowerTable.setStatus("current")
_DmmPowerTableEntry_Object = MibTableRow
dmmPowerTableEntry = _DmmPowerTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 4, 1, 1)
)
dmmPowerTableEntry.setIndexNames(
    (0, "DELL-MM-MIB-SMIv2", "dmmPowerChassisIndex"),
)
if mibBuilder.loadTexts:
    dmmPowerTableEntry.setStatus("current")
_DmmPowerChassisIndex_Type = DellPowerIndexRange
_DmmPowerChassisIndex_Object = MibTableColumn
dmmPowerChassisIndex = _DmmPowerChassisIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 4, 1, 1, 1),
    _DmmPowerChassisIndex_Type()
)
dmmPowerChassisIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dmmPowerChassisIndex.setStatus("current")
_DmmPowerIdlePower_Type = DellPowerReading
_DmmPowerIdlePower_Object = MibTableColumn
dmmPowerIdlePower = _DmmPowerIdlePower_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 4, 1, 1, 2),
    _DmmPowerIdlePower_Type()
)
dmmPowerIdlePower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dmmPowerIdlePower.setStatus("current")
_DmmPowerKWhCumulative_Type = DellPowerReading
_DmmPowerKWhCumulative_Object = MibTableColumn
dmmPowerKWhCumulative = _DmmPowerKWhCumulative_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 4, 1, 1, 3),
    _DmmPowerKWhCumulative_Type()
)
dmmPowerKWhCumulative.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dmmPowerKWhCumulative.setStatus("current")
_DmmPowerKWhCumulativeTime_Type = DellTimestamp
_DmmPowerKWhCumulativeTime_Object = MibTableColumn
dmmPowerKWhCumulativeTime = _DmmPowerKWhCumulativeTime_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 4, 1, 1, 4),
    _DmmPowerKWhCumulativeTime_Type()
)
dmmPowerKWhCumulativeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dmmPowerKWhCumulativeTime.setStatus("current")
_DmmPowerWattsPeakUsage_Type = DellPowerReading
_DmmPowerWattsPeakUsage_Object = MibTableColumn
dmmPowerWattsPeakUsage = _DmmPowerWattsPeakUsage_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 4, 1, 1, 5),
    _DmmPowerWattsPeakUsage_Type()
)
dmmPowerWattsPeakUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dmmPowerWattsPeakUsage.setStatus("current")
_DmmPowerWattsPeakTime_Type = DellTimestamp
_DmmPowerWattsPeakTime_Object = MibTableColumn
dmmPowerWattsPeakTime = _DmmPowerWattsPeakTime_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 4, 1, 1, 6),
    _DmmPowerWattsPeakTime_Type()
)
dmmPowerWattsPeakTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dmmPowerWattsPeakTime.setStatus("current")
_DmmPowerWattsMinUsage_Type = DellPowerReading
_DmmPowerWattsMinUsage_Object = MibTableColumn
dmmPowerWattsMinUsage = _DmmPowerWattsMinUsage_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 4, 1, 1, 7),
    _DmmPowerWattsMinUsage_Type()
)
dmmPowerWattsMinUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dmmPowerWattsMinUsage.setStatus("current")
_DmmPowerWattsMinTime_Type = DellTimestamp
_DmmPowerWattsMinTime_Object = MibTableColumn
dmmPowerWattsMinTime = _DmmPowerWattsMinTime_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 4, 1, 1, 8),
    _DmmPowerWattsMinTime_Type()
)
dmmPowerWattsMinTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dmmPowerWattsMinTime.setStatus("current")
_DmmPowerWattsReading_Type = DellPowerReading
_DmmPowerWattsReading_Object = MibTableColumn
dmmPowerWattsReading = _DmmPowerWattsReading_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 4, 1, 1, 9),
    _DmmPowerWattsReading_Type()
)
dmmPowerWattsReading.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dmmPowerWattsReading.setStatus("current")
_DmmPSUTable_Object = MibTable
dmmPSUTable = _DmmPSUTable_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 4, 2)
)
if mibBuilder.loadTexts:
    dmmPSUTable.setStatus("current")
_DmmPSUTableEntry_Object = MibTableRow
dmmPSUTableEntry = _DmmPSUTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 4, 2, 1)
)
dmmPSUTableEntry.setIndexNames(
    (0, "DELL-MM-MIB-SMIv2", "dmmPSUChassisIndex"),
    (0, "DELL-MM-MIB-SMIv2", "dmmPSUIndex"),
)
if mibBuilder.loadTexts:
    dmmPSUTableEntry.setStatus("current")
_DmmPSUChassisIndex_Type = DellPowerIndexRange
_DmmPSUChassisIndex_Object = MibTableColumn
dmmPSUChassisIndex = _DmmPSUChassisIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 4, 2, 1, 1),
    _DmmPSUChassisIndex_Type()
)
dmmPSUChassisIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dmmPSUChassisIndex.setStatus("current")
_DmmPSUIndex_Type = DellPSUIndexRange
_DmmPSUIndex_Object = MibTableColumn
dmmPSUIndex = _DmmPSUIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 4, 2, 1, 2),
    _DmmPSUIndex_Type()
)
dmmPSUIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dmmPSUIndex.setStatus("current")
_DmmPSULocation_Type = DellString
_DmmPSULocation_Object = MibTableColumn
dmmPSULocation = _DmmPSULocation_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 4, 2, 1, 3),
    _DmmPSULocation_Type()
)
dmmPSULocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dmmPSULocation.setStatus("current")
_DmmPSUState_Type = DellString
_DmmPSUState_Object = MibTableColumn
dmmPSUState = _DmmPSUState_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 4, 2, 1, 4),
    _DmmPSUState_Type()
)
dmmPSUState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dmmPSUState.setStatus("current")
_DmmPSUType_Type = DellString
_DmmPSUType_Object = MibTableColumn
dmmPSUType = _DmmPSUType_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 4, 2, 1, 5),
    _DmmPSUType_Type()
)
dmmPSUType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dmmPSUType.setStatus("current")
_DmmPSUCapacity_Type = DellPowerReading
_DmmPSUCapacity_Object = MibTableColumn
dmmPSUCapacity = _DmmPSUCapacity_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 4, 2, 1, 6),
    _DmmPSUCapacity_Type()
)
dmmPSUCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dmmPSUCapacity.setStatus("current")
_DmmPSUVoltage_Type = DellPowerReading
_DmmPSUVoltage_Object = MibTableColumn
dmmPSUVoltage = _DmmPSUVoltage_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 4, 2, 1, 7),
    _DmmPSUVoltage_Type()
)
dmmPSUVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dmmPSUVoltage.setStatus("current")
_DmmPSUCurrStatus_Type = DellStatus
_DmmPSUCurrStatus_Object = MibTableColumn
dmmPSUCurrStatus = _DmmPSUCurrStatus_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 4, 2, 1, 8),
    _DmmPSUCurrStatus_Type()
)
dmmPSUCurrStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dmmPSUCurrStatus.setStatus("current")
_DmmChassisAlert2Group_ObjectIdentity = ObjectIdentity
dmmChassisAlert2Group = _DmmChassisAlert2Group_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 5)
)
_DmmChassisAlert2Variables_ObjectIdentity = ObjectIdentity
dmmChassisAlert2Variables = _DmmChassisAlert2Variables_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 5, 1)
)


class _DmmCA2MessageID_Type(DisplayString):
    """Custom type dmmCA2MessageID based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_DmmCA2MessageID_Type.__name__ = "DisplayString"
_DmmCA2MessageID_Object = MibScalar
dmmCA2MessageID = _DmmCA2MessageID_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 5, 1, 1),
    _DmmCA2MessageID_Type()
)
dmmCA2MessageID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dmmCA2MessageID.setStatus("current")
_DmmCA2Message_Type = DellString
_DmmCA2Message_Object = MibScalar
dmmCA2Message = _DmmCA2Message_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 5, 1, 2),
    _DmmCA2Message_Type()
)
dmmCA2Message.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dmmCA2Message.setStatus("mandatory")
_DmmCA2MessageArgs_Type = DellString
_DmmCA2MessageArgs_Object = MibScalar
dmmCA2MessageArgs = _DmmCA2MessageArgs_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 5, 1, 3),
    _DmmCA2MessageArgs_Type()
)
dmmCA2MessageArgs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dmmCA2MessageArgs.setStatus("current")
_DmmCA2AlertStatus_Type = DellStatus
_DmmCA2AlertStatus_Object = MibScalar
dmmCA2AlertStatus = _DmmCA2AlertStatus_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 5, 1, 4),
    _DmmCA2AlertStatus_Type()
)
dmmCA2AlertStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dmmCA2AlertStatus.setStatus("current")


class _DmmCA2FQDD_Type(DisplayString):
    """Custom type dmmCA2FQDD based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 512),
    )


_DmmCA2FQDD_Type.__name__ = "DisplayString"
_DmmCA2FQDD_Object = MibScalar
dmmCA2FQDD = _DmmCA2FQDD_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 5, 1, 5),
    _DmmCA2FQDD_Type()
)
dmmCA2FQDD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dmmCA2FQDD.setStatus("current")
_DmmGenericAlertGroup_ObjectIdentity = ObjectIdentity
dmmGenericAlertGroup = _DmmGenericAlertGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 6)
)
_DmmGenericAlertVariables_ObjectIdentity = ObjectIdentity
dmmGenericAlertVariables = _DmmGenericAlertVariables_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 6, 1)
)
_DmmDeviceServiceTag_Type = DellString
_DmmDeviceServiceTag_Object = MibScalar
dmmDeviceServiceTag = _DmmDeviceServiceTag_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 6, 1, 1),
    _DmmDeviceServiceTag_Type()
)
dmmDeviceServiceTag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dmmDeviceServiceTag.setStatus("current")


class _DmmCategoryName_Type(DisplayString):
    """Custom type dmmCategoryName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 512),
    )


_DmmCategoryName_Type.__name__ = "DisplayString"
_DmmCategoryName_Object = MibScalar
dmmCategoryName = _DmmCategoryName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 6, 1, 2),
    _DmmCategoryName_Type()
)
dmmCategoryName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dmmCategoryName.setStatus("mandatory")


class _DmmSubCategoryName_Type(DisplayString):
    """Custom type dmmSubCategoryName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 512),
    )


_DmmSubCategoryName_Type.__name__ = "DisplayString"
_DmmSubCategoryName_Object = MibScalar
dmmSubCategoryName = _DmmSubCategoryName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 6, 1, 3),
    _DmmSubCategoryName_Type()
)
dmmSubCategoryName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dmmSubCategoryName.setStatus("mandatory")


class _DmmSeverity_Type(DisplayString):
    """Custom type dmmSeverity based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 512),
    )


_DmmSeverity_Type.__name__ = "DisplayString"
_DmmSeverity_Object = MibScalar
dmmSeverity = _DmmSeverity_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 6, 1, 4),
    _DmmSeverity_Type()
)
dmmSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dmmSeverity.setStatus("mandatory")
_DmmiDRACAlertGroup_ObjectIdentity = ObjectIdentity
dmmiDRACAlertGroup = _DmmiDRACAlertGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 7)
)
_DmmNWIOMAlertGroup_ObjectIdentity = ObjectIdentity
dmmNWIOMAlertGroup = _DmmNWIOMAlertGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 8)
)
_DmmSASIOMAlertGroup_ObjectIdentity = ObjectIdentity
dmmSASIOMAlertGroup = _DmmSASIOMAlertGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 9)
)
_ConformanceGroup_ObjectIdentity = ObjectIdentity
conformanceGroup = _ConformanceGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 10)
)
_ConformanceMIBGroups_ObjectIdentity = ObjectIdentity
conformanceMIBGroups = _ConformanceMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 10, 1)
)
_ConformanceMIBnotificationGroup_ObjectIdentity = ObjectIdentity
conformanceMIBnotificationGroup = _ConformanceMIBnotificationGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 10, 2)
)

# Managed Objects groups

dmmProductInfoObjGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 10, 1, 1)
)
dmmProductInfoObjGroup.setObjects(
      *(("DELL-MM-MIB-SMIv2", "dmmProductName"),
        ("DELL-MM-MIB-SMIv2", "dmmProductShortName"),
        ("DELL-MM-MIB-SMIv2", "dmmProductDescription"),
        ("DELL-MM-MIB-SMIv2", "dmmProductManufacturer"),
        ("DELL-MM-MIB-SMIv2", "dmmProductVersion"),
        ("DELL-MM-MIB-SMIv2", "dmmChassisServiceTag"),
        ("DELL-MM-MIB-SMIv2", "dmmProductURL"),
        ("DELL-MM-MIB-SMIv2", "dmmProductChassisAssetTag"),
        ("DELL-MM-MIB-SMIv2", "dmmProductChassisName"),
        ("DELL-MM-MIB-SMIv2", "dmmProductType"),
        ("DELL-MM-MIB-SMIv2", "dmmProductChassisDataCenter"),
        ("DELL-MM-MIB-SMIv2", "dmmProductChassisAisle"),
        ("DELL-MM-MIB-SMIv2", "dmmProductChassisRack"),
        ("DELL-MM-MIB-SMIv2", "dmmProductChassisRackSlot"),
        ("DELL-MM-MIB-SMIv2", "dmmProductChassisModel"),
        ("DELL-MM-MIB-SMIv2", "dmmProductChassisExpressServiceCode"),
        ("DELL-MM-MIB-SMIv2", "dmmProductChassisSystemID"))
)
if mibBuilder.loadTexts:
    dmmProductInfoObjGroup.setStatus("current")

dmmFirmwareObjGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 10, 1, 2)
)
dmmFirmwareObjGroup.setObjects(
      *(("DELL-MM-MIB-SMIv2", "dmmFirmwareVersion"),
        ("DELL-MM-MIB-SMIv2", "dmmFirmwareVersion2"))
)
if mibBuilder.loadTexts:
    dmmFirmwareObjGroup.setStatus("current")

dmmStatusObjGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 10, 1, 3)
)
dmmStatusObjGroup.setObjects(
    ("DELL-MM-MIB-SMIv2", "dmmGlobalSystemStatus")
)
if mibBuilder.loadTexts:
    dmmStatusObjGroup.setStatus("current")

dmmStatusNowObjGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 10, 1, 4)
)
dmmStatusNowObjGroup.setObjects(
      *(("DELL-MM-MIB-SMIv2", "dmmIOMCurrStatus"),
        ("DELL-MM-MIB-SMIv2", "dmmRedCurrStatus"),
        ("DELL-MM-MIB-SMIv2", "dmmPowerCurrStatus"),
        ("DELL-MM-MIB-SMIv2", "dmmFanCurrStatus"),
        ("DELL-MM-MIB-SMIv2", "dmmBladeCurrStatus"),
        ("DELL-MM-MIB-SMIv2", "dmmTempCurrStatus"),
        ("DELL-MM-MIB-SMIv2", "dmmMMCurrStatus"),
        ("DELL-MM-MIB-SMIv2", "dmmChassisFrontPanelAmbientTemperature"))
)
if mibBuilder.loadTexts:
    dmmStatusNowObjGroup.setStatus("current")

dmmChassisPowerObjGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 10, 1, 5)
)
dmmChassisPowerObjGroup.setObjects(
      *(("DELL-MM-MIB-SMIv2", "dmmPowerTable"),
        ("DELL-MM-MIB-SMIv2", "dmmPSUTable"))
)
if mibBuilder.loadTexts:
    dmmChassisPowerObjGroup.setStatus("current")

dmmPowerTableObjEntry = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 10, 1, 6)
)
dmmPowerTableObjEntry.setObjects(
      *(("DELL-MM-MIB-SMIv2", "dmmPowerChassisIndex"),
        ("DELL-MM-MIB-SMIv2", "dmmPowerIdlePower"),
        ("DELL-MM-MIB-SMIv2", "dmmPowerKWhCumulative"),
        ("DELL-MM-MIB-SMIv2", "dmmPowerKWhCumulativeTime"),
        ("DELL-MM-MIB-SMIv2", "dmmPowerWattsPeakUsage"),
        ("DELL-MM-MIB-SMIv2", "dmmPowerWattsPeakTime"),
        ("DELL-MM-MIB-SMIv2", "dmmPowerWattsMinUsage"),
        ("DELL-MM-MIB-SMIv2", "dmmPowerWattsMinTime"),
        ("DELL-MM-MIB-SMIv2", "dmmPowerWattsReading"))
)
if mibBuilder.loadTexts:
    dmmPowerTableObjEntry.setStatus("current")

dmmPSUTableObjEntry = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 10, 1, 7)
)
dmmPSUTableObjEntry.setObjects(
      *(("DELL-MM-MIB-SMIv2", "dmmPSUChassisIndex"),
        ("DELL-MM-MIB-SMIv2", "dmmPSUIndex"),
        ("DELL-MM-MIB-SMIv2", "dmmPSULocation"),
        ("DELL-MM-MIB-SMIv2", "dmmPSUState"),
        ("DELL-MM-MIB-SMIv2", "dmmPSUType"),
        ("DELL-MM-MIB-SMIv2", "dmmPSUCapacity"),
        ("DELL-MM-MIB-SMIv2", "dmmPSUVoltage"),
        ("DELL-MM-MIB-SMIv2", "dmmPSUCurrStatus"))
)
if mibBuilder.loadTexts:
    dmmPSUTableObjEntry.setStatus("current")

dmmChassisAlert2VariablesObj = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 10, 1, 8)
)
dmmChassisAlert2VariablesObj.setObjects(
      *(("DELL-MM-MIB-SMIv2", "dmmCA2MessageID"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2Message"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2MessageArgs"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2AlertStatus"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2FQDD"))
)
if mibBuilder.loadTexts:
    dmmChassisAlert2VariablesObj.setStatus("current")

dmmGenericAlertVariablesObj = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 10, 1, 9)
)
dmmGenericAlertVariablesObj.setObjects(
      *(("DELL-MM-MIB-SMIv2", "dmmDeviceServiceTag"),
        ("DELL-MM-MIB-SMIv2", "dmmCategoryName"),
        ("DELL-MM-MIB-SMIv2", "dmmSubCategoryName"),
        ("DELL-MM-MIB-SMIv2", "dmmSeverity"))
)
if mibBuilder.loadTexts:
    dmmGenericAlertVariablesObj.setStatus("current")


# Notification objects

alert2FanFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 5, 0, 2153)
)
alert2FanFailure.setObjects(
      *(("DELL-MM-MIB-SMIv2", "dmmCA2MessageID"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2Message"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2MessageArgs"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2AlertStatus"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2FQDD"),
        ("DELL-MM-MIB-SMIv2", "dmmProductChassisName"),
        ("DELL-MM-MIB-SMIv2", "dmmChassisServiceTag"))
)
if mibBuilder.loadTexts:
    alert2FanFailure.setStatus(
        "current"
    )

alert2FanWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 5, 0, 2154)
)
alert2FanWarning.setObjects(
      *(("DELL-MM-MIB-SMIv2", "dmmCA2MessageID"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2Message"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2MessageArgs"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2AlertStatus"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2FQDD"),
        ("DELL-MM-MIB-SMIv2", "dmmProductChassisName"),
        ("DELL-MM-MIB-SMIv2", "dmmChassisServiceTag"))
)
if mibBuilder.loadTexts:
    alert2FanWarning.setStatus(
        "current"
    )

alert2FanInformation = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 5, 0, 2155)
)
alert2FanInformation.setObjects(
      *(("DELL-MM-MIB-SMIv2", "dmmCA2MessageID"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2Message"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2MessageArgs"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2AlertStatus"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2FQDD"),
        ("DELL-MM-MIB-SMIv2", "dmmProductChassisName"),
        ("DELL-MM-MIB-SMIv2", "dmmChassisServiceTag"))
)
if mibBuilder.loadTexts:
    alert2FanInformation.setStatus(
        "current"
    )

alert2TemperatureProbeFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 5, 0, 2161)
)
alert2TemperatureProbeFailure.setObjects(
      *(("DELL-MM-MIB-SMIv2", "dmmCA2MessageID"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2Message"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2MessageArgs"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2AlertStatus"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2FQDD"),
        ("DELL-MM-MIB-SMIv2", "dmmProductChassisName"),
        ("DELL-MM-MIB-SMIv2", "dmmChassisServiceTag"))
)
if mibBuilder.loadTexts:
    alert2TemperatureProbeFailure.setStatus(
        "current"
    )

alert2TemperatureProbeWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 5, 0, 2162)
)
alert2TemperatureProbeWarning.setObjects(
      *(("DELL-MM-MIB-SMIv2", "dmmCA2MessageID"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2Message"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2MessageArgs"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2AlertStatus"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2FQDD"),
        ("DELL-MM-MIB-SMIv2", "dmmProductChassisName"),
        ("DELL-MM-MIB-SMIv2", "dmmChassisServiceTag"))
)
if mibBuilder.loadTexts:
    alert2TemperatureProbeWarning.setStatus(
        "current"
    )

alert2TemperatureProbeNormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 5, 0, 2163)
)
alert2TemperatureProbeNormal.setObjects(
      *(("DELL-MM-MIB-SMIv2", "dmmCA2MessageID"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2Message"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2MessageArgs"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2AlertStatus"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2FQDD"),
        ("DELL-MM-MIB-SMIv2", "dmmProductChassisName"),
        ("DELL-MM-MIB-SMIv2", "dmmChassisServiceTag"))
)
if mibBuilder.loadTexts:
    alert2TemperatureProbeNormal.setStatus(
        "current"
    )

alert2VoltageProbeFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 5, 0, 2169)
)
alert2VoltageProbeFailure.setObjects(
      *(("DELL-MM-MIB-SMIv2", "dmmCA2MessageID"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2Message"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2MessageArgs"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2AlertStatus"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2FQDD"),
        ("DELL-MM-MIB-SMIv2", "dmmProductChassisName"),
        ("DELL-MM-MIB-SMIv2", "dmmChassisServiceTag"))
)
if mibBuilder.loadTexts:
    alert2VoltageProbeFailure.setStatus(
        "current"
    )

alert2VoltageProbeWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 5, 0, 2170)
)
alert2VoltageProbeWarning.setObjects(
      *(("DELL-MM-MIB-SMIv2", "dmmCA2MessageID"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2Message"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2MessageArgs"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2AlertStatus"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2FQDD"),
        ("DELL-MM-MIB-SMIv2", "dmmProductChassisName"),
        ("DELL-MM-MIB-SMIv2", "dmmChassisServiceTag"))
)
if mibBuilder.loadTexts:
    alert2VoltageProbeWarning.setStatus(
        "current"
    )

alert2VoltageProbeNormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 5, 0, 2171)
)
alert2VoltageProbeNormal.setObjects(
      *(("DELL-MM-MIB-SMIv2", "dmmCA2MessageID"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2Message"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2MessageArgs"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2AlertStatus"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2FQDD"),
        ("DELL-MM-MIB-SMIv2", "dmmProductChassisName"),
        ("DELL-MM-MIB-SMIv2", "dmmChassisServiceTag"))
)
if mibBuilder.loadTexts:
    alert2VoltageProbeNormal.setStatus(
        "current"
    )

alert2AmperageProbeFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 5, 0, 2177)
)
alert2AmperageProbeFailure.setObjects(
      *(("DELL-MM-MIB-SMIv2", "dmmCA2MessageID"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2Message"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2MessageArgs"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2AlertStatus"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2FQDD"),
        ("DELL-MM-MIB-SMIv2", "dmmProductChassisName"),
        ("DELL-MM-MIB-SMIv2", "dmmChassisServiceTag"))
)
if mibBuilder.loadTexts:
    alert2AmperageProbeFailure.setStatus(
        "current"
    )

alert2AmperageProbeWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 5, 0, 2178)
)
alert2AmperageProbeWarning.setObjects(
      *(("DELL-MM-MIB-SMIv2", "dmmCA2MessageID"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2Message"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2MessageArgs"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2AlertStatus"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2FQDD"),
        ("DELL-MM-MIB-SMIv2", "dmmProductChassisName"),
        ("DELL-MM-MIB-SMIv2", "dmmChassisServiceTag"))
)
if mibBuilder.loadTexts:
    alert2AmperageProbeWarning.setStatus(
        "current"
    )

alert2AmperageProbeNormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 5, 0, 2179)
)
alert2AmperageProbeNormal.setObjects(
      *(("DELL-MM-MIB-SMIv2", "dmmCA2MessageID"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2Message"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2MessageArgs"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2AlertStatus"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2FQDD"),
        ("DELL-MM-MIB-SMIv2", "dmmProductChassisName"),
        ("DELL-MM-MIB-SMIv2", "dmmChassisServiceTag"))
)
if mibBuilder.loadTexts:
    alert2AmperageProbeNormal.setStatus(
        "current"
    )

alert2PowerSupplyFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 5, 0, 2185)
)
alert2PowerSupplyFailure.setObjects(
      *(("DELL-MM-MIB-SMIv2", "dmmCA2MessageID"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2Message"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2MessageArgs"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2AlertStatus"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2FQDD"),
        ("DELL-MM-MIB-SMIv2", "dmmProductChassisName"),
        ("DELL-MM-MIB-SMIv2", "dmmChassisServiceTag"))
)
if mibBuilder.loadTexts:
    alert2PowerSupplyFailure.setStatus(
        "current"
    )

alert2PowerSupplyWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 5, 0, 2186)
)
alert2PowerSupplyWarning.setObjects(
      *(("DELL-MM-MIB-SMIv2", "dmmCA2MessageID"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2Message"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2MessageArgs"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2AlertStatus"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2FQDD"),
        ("DELL-MM-MIB-SMIv2", "dmmProductChassisName"),
        ("DELL-MM-MIB-SMIv2", "dmmChassisServiceTag"))
)
if mibBuilder.loadTexts:
    alert2PowerSupplyWarning.setStatus(
        "current"
    )

alert2PowerSupplyNormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 5, 0, 2187)
)
alert2PowerSupplyNormal.setObjects(
      *(("DELL-MM-MIB-SMIv2", "dmmCA2MessageID"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2Message"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2MessageArgs"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2AlertStatus"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2FQDD"),
        ("DELL-MM-MIB-SMIv2", "dmmProductChassisName"),
        ("DELL-MM-MIB-SMIv2", "dmmChassisServiceTag"))
)
if mibBuilder.loadTexts:
    alert2PowerSupplyNormal.setStatus(
        "current"
    )

alert2BatteryFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 5, 0, 2225)
)
alert2BatteryFailure.setObjects(
      *(("DELL-MM-MIB-SMIv2", "dmmCA2MessageID"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2Message"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2MessageArgs"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2AlertStatus"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2FQDD"),
        ("DELL-MM-MIB-SMIv2", "dmmProductChassisName"),
        ("DELL-MM-MIB-SMIv2", "dmmChassisServiceTag"))
)
if mibBuilder.loadTexts:
    alert2BatteryFailure.setStatus(
        "current"
    )

alert2BatteryWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 5, 0, 2226)
)
alert2BatteryWarning.setObjects(
      *(("DELL-MM-MIB-SMIv2", "dmmCA2MessageID"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2Message"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2MessageArgs"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2AlertStatus"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2FQDD"),
        ("DELL-MM-MIB-SMIv2", "dmmProductChassisName"),
        ("DELL-MM-MIB-SMIv2", "dmmChassisServiceTag"))
)
if mibBuilder.loadTexts:
    alert2BatteryWarning.setStatus(
        "current"
    )

alert2BatteryNormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 5, 0, 2227)
)
alert2BatteryNormal.setObjects(
      *(("DELL-MM-MIB-SMIv2", "dmmCA2MessageID"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2Message"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2MessageArgs"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2AlertStatus"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2FQDD"),
        ("DELL-MM-MIB-SMIv2", "dmmProductChassisName"),
        ("DELL-MM-MIB-SMIv2", "dmmChassisServiceTag"))
)
if mibBuilder.loadTexts:
    alert2BatteryNormal.setStatus(
        "current"
    )

alert2LinkStatusFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 5, 0, 2249)
)
alert2LinkStatusFailure.setObjects(
      *(("DELL-MM-MIB-SMIv2", "dmmCA2MessageID"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2Message"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2MessageArgs"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2AlertStatus"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2FQDD"),
        ("DELL-MM-MIB-SMIv2", "dmmProductChassisName"),
        ("DELL-MM-MIB-SMIv2", "dmmChassisServiceTag"))
)
if mibBuilder.loadTexts:
    alert2LinkStatusFailure.setStatus(
        "current"
    )

alert2LinkStatusWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 5, 0, 2250)
)
alert2LinkStatusWarning.setObjects(
      *(("DELL-MM-MIB-SMIv2", "dmmCA2MessageID"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2Message"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2MessageArgs"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2AlertStatus"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2FQDD"),
        ("DELL-MM-MIB-SMIv2", "dmmProductChassisName"),
        ("DELL-MM-MIB-SMIv2", "dmmChassisServiceTag"))
)
if mibBuilder.loadTexts:
    alert2LinkStatusWarning.setStatus(
        "current"
    )

alert2LinkStatusInformation = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 5, 0, 2251)
)
alert2LinkStatusInformation.setObjects(
      *(("DELL-MM-MIB-SMIv2", "dmmCA2MessageID"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2Message"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2MessageArgs"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2AlertStatus"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2FQDD"),
        ("DELL-MM-MIB-SMIv2", "dmmProductChassisName"),
        ("DELL-MM-MIB-SMIv2", "dmmChassisServiceTag"))
)
if mibBuilder.loadTexts:
    alert2LinkStatusInformation.setStatus(
        "current"
    )

alert2PowerUsageFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 5, 0, 2273)
)
alert2PowerUsageFailure.setObjects(
      *(("DELL-MM-MIB-SMIv2", "dmmCA2MessageID"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2Message"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2MessageArgs"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2AlertStatus"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2FQDD"),
        ("DELL-MM-MIB-SMIv2", "dmmProductChassisName"),
        ("DELL-MM-MIB-SMIv2", "dmmChassisServiceTag"))
)
if mibBuilder.loadTexts:
    alert2PowerUsageFailure.setStatus(
        "current"
    )

alert2PowerUsageWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 5, 0, 2274)
)
alert2PowerUsageWarning.setObjects(
      *(("DELL-MM-MIB-SMIv2", "dmmCA2MessageID"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2Message"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2MessageArgs"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2AlertStatus"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2FQDD"),
        ("DELL-MM-MIB-SMIv2", "dmmProductChassisName"),
        ("DELL-MM-MIB-SMIv2", "dmmChassisServiceTag"))
)
if mibBuilder.loadTexts:
    alert2PowerUsageWarning.setStatus(
        "current"
    )

alert2PowerUsageInformation = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 5, 0, 2275)
)
alert2PowerUsageInformation.setObjects(
      *(("DELL-MM-MIB-SMIv2", "dmmCA2MessageID"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2Message"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2MessageArgs"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2AlertStatus"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2FQDD"),
        ("DELL-MM-MIB-SMIv2", "dmmProductChassisName"),
        ("DELL-MM-MIB-SMIv2", "dmmChassisServiceTag"))
)
if mibBuilder.loadTexts:
    alert2PowerUsageInformation.setStatus(
        "current"
    )

alert2HardwareConfigurationFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 5, 0, 2329)
)
alert2HardwareConfigurationFailure.setObjects(
      *(("DELL-MM-MIB-SMIv2", "dmmCA2MessageID"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2Message"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2MessageArgs"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2AlertStatus"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2FQDD"),
        ("DELL-MM-MIB-SMIv2", "dmmProductChassisName"),
        ("DELL-MM-MIB-SMIv2", "dmmChassisServiceTag"))
)
if mibBuilder.loadTexts:
    alert2HardwareConfigurationFailure.setStatus(
        "current"
    )

alert2HardwareConfigurationWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 5, 0, 2330)
)
alert2HardwareConfigurationWarning.setObjects(
      *(("DELL-MM-MIB-SMIv2", "dmmCA2MessageID"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2Message"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2MessageArgs"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2AlertStatus"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2FQDD"),
        ("DELL-MM-MIB-SMIv2", "dmmProductChassisName"),
        ("DELL-MM-MIB-SMIv2", "dmmChassisServiceTag"))
)
if mibBuilder.loadTexts:
    alert2HardwareConfigurationWarning.setStatus(
        "current"
    )

alert2HardwareConfigurationInformation = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 5, 0, 2331)
)
alert2HardwareConfigurationInformation.setObjects(
      *(("DELL-MM-MIB-SMIv2", "dmmCA2MessageID"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2Message"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2MessageArgs"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2AlertStatus"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2FQDD"),
        ("DELL-MM-MIB-SMIv2", "dmmProductChassisName"),
        ("DELL-MM-MIB-SMIv2", "dmmChassisServiceTag"))
)
if mibBuilder.loadTexts:
    alert2HardwareConfigurationInformation.setStatus(
        "current"
    )

alert2SoftwareConfigurationFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 5, 0, 2337)
)
alert2SoftwareConfigurationFailure.setObjects(
      *(("DELL-MM-MIB-SMIv2", "dmmCA2MessageID"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2Message"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2MessageArgs"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2AlertStatus"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2FQDD"),
        ("DELL-MM-MIB-SMIv2", "dmmProductChassisName"),
        ("DELL-MM-MIB-SMIv2", "dmmChassisServiceTag"))
)
if mibBuilder.loadTexts:
    alert2SoftwareConfigurationFailure.setStatus(
        "current"
    )

alert2SoftwareConfigurationWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 5, 0, 2338)
)
alert2SoftwareConfigurationWarning.setObjects(
      *(("DELL-MM-MIB-SMIv2", "dmmCA2MessageID"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2Message"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2MessageArgs"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2AlertStatus"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2FQDD"),
        ("DELL-MM-MIB-SMIv2", "dmmProductChassisName"),
        ("DELL-MM-MIB-SMIv2", "dmmChassisServiceTag"))
)
if mibBuilder.loadTexts:
    alert2SoftwareConfigurationWarning.setStatus(
        "current"
    )

alert2SoftwareConfigurationInformation = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 5, 0, 2339)
)
alert2SoftwareConfigurationInformation.setObjects(
      *(("DELL-MM-MIB-SMIv2", "dmmCA2MessageID"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2Message"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2MessageArgs"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2AlertStatus"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2FQDD"),
        ("DELL-MM-MIB-SMIv2", "dmmProductChassisName"),
        ("DELL-MM-MIB-SMIv2", "dmmChassisServiceTag"))
)
if mibBuilder.loadTexts:
    alert2SoftwareConfigurationInformation.setStatus(
        "current"
    )

alert2SystemEventLogFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 5, 0, 2377)
)
alert2SystemEventLogFailure.setObjects(
      *(("DELL-MM-MIB-SMIv2", "dmmCA2MessageID"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2Message"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2MessageArgs"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2AlertStatus"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2FQDD"),
        ("DELL-MM-MIB-SMIv2", "dmmProductChassisName"),
        ("DELL-MM-MIB-SMIv2", "dmmChassisServiceTag"))
)
if mibBuilder.loadTexts:
    alert2SystemEventLogFailure.setStatus(
        "current"
    )

alert2SystemEventLogWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 5, 0, 2378)
)
alert2SystemEventLogWarning.setObjects(
      *(("DELL-MM-MIB-SMIv2", "dmmCA2MessageID"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2Message"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2MessageArgs"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2AlertStatus"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2FQDD"),
        ("DELL-MM-MIB-SMIv2", "dmmProductChassisName"),
        ("DELL-MM-MIB-SMIv2", "dmmChassisServiceTag"))
)
if mibBuilder.loadTexts:
    alert2SystemEventLogWarning.setStatus(
        "current"
    )

alert2SystemEventLogInformation = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 5, 0, 2379)
)
alert2SystemEventLogInformation.setObjects(
      *(("DELL-MM-MIB-SMIv2", "dmmCA2MessageID"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2Message"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2MessageArgs"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2AlertStatus"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2FQDD"),
        ("DELL-MM-MIB-SMIv2", "dmmProductChassisName"),
        ("DELL-MM-MIB-SMIv2", "dmmChassisServiceTag"))
)
if mibBuilder.loadTexts:
    alert2SystemEventLogInformation.setStatus(
        "current"
    )

alert2SecurityFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 5, 0, 2385)
)
alert2SecurityFailure.setObjects(
      *(("DELL-MM-MIB-SMIv2", "dmmCA2MessageID"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2Message"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2MessageArgs"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2AlertStatus"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2FQDD"),
        ("DELL-MM-MIB-SMIv2", "dmmProductChassisName"),
        ("DELL-MM-MIB-SMIv2", "dmmChassisServiceTag"))
)
if mibBuilder.loadTexts:
    alert2SecurityFailure.setStatus(
        "current"
    )

alert2SecurityWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 5, 0, 2386)
)
alert2SecurityWarning.setObjects(
      *(("DELL-MM-MIB-SMIv2", "dmmCA2MessageID"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2Message"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2MessageArgs"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2AlertStatus"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2FQDD"),
        ("DELL-MM-MIB-SMIv2", "dmmProductChassisName"),
        ("DELL-MM-MIB-SMIv2", "dmmChassisServiceTag"))
)
if mibBuilder.loadTexts:
    alert2SecurityWarning.setStatus(
        "current"
    )

alert2SecurityInformation = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 5, 0, 2387)
)
alert2SecurityInformation.setObjects(
      *(("DELL-MM-MIB-SMIv2", "dmmCA2MessageID"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2Message"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2MessageArgs"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2AlertStatus"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2FQDD"),
        ("DELL-MM-MIB-SMIv2", "dmmProductChassisName"),
        ("DELL-MM-MIB-SMIv2", "dmmChassisServiceTag"))
)
if mibBuilder.loadTexts:
    alert2SecurityInformation.setStatus(
        "current"
    )

alert2CableFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 5, 0, 2393)
)
alert2CableFailure.setObjects(
      *(("DELL-MM-MIB-SMIv2", "dmmCA2MessageID"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2Message"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2MessageArgs"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2AlertStatus"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2FQDD"),
        ("DELL-MM-MIB-SMIv2", "dmmProductChassisName"),
        ("DELL-MM-MIB-SMIv2", "dmmChassisServiceTag"))
)
if mibBuilder.loadTexts:
    alert2CableFailure.setStatus(
        "current"
    )

alert2PowerSupplyAbsent = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 5, 0, 2465)
)
alert2PowerSupplyAbsent.setObjects(
      *(("DELL-MM-MIB-SMIv2", "dmmCA2MessageID"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2Message"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2MessageArgs"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2AlertStatus"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2FQDD"),
        ("DELL-MM-MIB-SMIv2", "dmmProductChassisName"),
        ("DELL-MM-MIB-SMIv2", "dmmChassisServiceTag"))
)
if mibBuilder.loadTexts:
    alert2PowerSupplyAbsent.setStatus(
        "current"
    )

alert2RedundancyLost = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 5, 0, 2473)
)
alert2RedundancyLost.setObjects(
      *(("DELL-MM-MIB-SMIv2", "dmmCA2MessageID"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2Message"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2MessageArgs"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2AlertStatus"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2FQDD"),
        ("DELL-MM-MIB-SMIv2", "dmmProductChassisName"),
        ("DELL-MM-MIB-SMIv2", "dmmChassisServiceTag"))
)
if mibBuilder.loadTexts:
    alert2RedundancyLost.setStatus(
        "current"
    )

alert2RedundancyDegraded = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 5, 0, 2474)
)
alert2RedundancyDegraded.setObjects(
      *(("DELL-MM-MIB-SMIv2", "dmmCA2MessageID"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2Message"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2MessageArgs"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2AlertStatus"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2FQDD"),
        ("DELL-MM-MIB-SMIv2", "dmmProductChassisName"),
        ("DELL-MM-MIB-SMIv2", "dmmChassisServiceTag"))
)
if mibBuilder.loadTexts:
    alert2RedundancyDegraded.setStatus(
        "current"
    )

alert2RedundancyInformation = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 5, 0, 2475)
)
alert2RedundancyInformation.setObjects(
      *(("DELL-MM-MIB-SMIv2", "dmmCA2MessageID"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2Message"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2MessageArgs"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2AlertStatus"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2FQDD"),
        ("DELL-MM-MIB-SMIv2", "dmmProductChassisName"),
        ("DELL-MM-MIB-SMIv2", "dmmChassisServiceTag"))
)
if mibBuilder.loadTexts:
    alert2RedundancyInformation.setStatus(
        "current"
    )

alert2CMCFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 5, 0, 2545)
)
alert2CMCFailure.setObjects(
      *(("DELL-MM-MIB-SMIv2", "dmmCA2MessageID"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2Message"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2MessageArgs"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2AlertStatus"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2FQDD"),
        ("DELL-MM-MIB-SMIv2", "dmmProductChassisName"),
        ("DELL-MM-MIB-SMIv2", "dmmChassisServiceTag"))
)
if mibBuilder.loadTexts:
    alert2CMCFailure.setStatus(
        "current"
    )

alert2CMCWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 5, 0, 2546)
)
alert2CMCWarning.setObjects(
      *(("DELL-MM-MIB-SMIv2", "dmmCA2MessageID"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2Message"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2MessageArgs"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2AlertStatus"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2FQDD"),
        ("DELL-MM-MIB-SMIv2", "dmmProductChassisName"),
        ("DELL-MM-MIB-SMIv2", "dmmChassisServiceTag"))
)
if mibBuilder.loadTexts:
    alert2CMCWarning.setStatus(
        "current"
    )

alert2IOVirtualizationFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 5, 0, 2553)
)
alert2IOVirtualizationFailure.setObjects(
      *(("DELL-MM-MIB-SMIv2", "dmmCA2MessageID"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2Message"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2MessageArgs"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2AlertStatus"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2FQDD"),
        ("DELL-MM-MIB-SMIv2", "dmmProductChassisName"),
        ("DELL-MM-MIB-SMIv2", "dmmChassisServiceTag"))
)
if mibBuilder.loadTexts:
    alert2IOVirtualizationFailure.setStatus(
        "current"
    )

alert2IOVirtualizationWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 5, 0, 2554)
)
alert2IOVirtualizationWarning.setObjects(
      *(("DELL-MM-MIB-SMIv2", "dmmCA2MessageID"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2Message"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2MessageArgs"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2AlertStatus"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2FQDD"),
        ("DELL-MM-MIB-SMIv2", "dmmProductChassisName"),
        ("DELL-MM-MIB-SMIv2", "dmmChassisServiceTag"))
)
if mibBuilder.loadTexts:
    alert2IOVirtualizationWarning.setStatus(
        "current"
    )

alert2IOVirtualizationInformation = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 5, 0, 2555)
)
alert2IOVirtualizationInformation.setObjects(
      *(("DELL-MM-MIB-SMIv2", "dmmCA2MessageID"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2Message"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2MessageArgs"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2AlertStatus"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2FQDD"),
        ("DELL-MM-MIB-SMIv2", "dmmProductChassisName"),
        ("DELL-MM-MIB-SMIv2", "dmmChassisServiceTag"))
)
if mibBuilder.loadTexts:
    alert2IOVirtualizationInformation.setStatus(
        "current"
    )

alert2StorageManagementFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 5, 0, 4177)
)
alert2StorageManagementFailure.setObjects(
      *(("DELL-MM-MIB-SMIv2", "dmmCA2MessageID"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2Message"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2MessageArgs"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2AlertStatus"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2FQDD"),
        ("DELL-MM-MIB-SMIv2", "dmmProductChassisName"),
        ("DELL-MM-MIB-SMIv2", "dmmChassisServiceTag"))
)
if mibBuilder.loadTexts:
    alert2StorageManagementFailure.setStatus(
        "current"
    )

alert2StorageManagementWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 5, 0, 4178)
)
alert2StorageManagementWarning.setObjects(
      *(("DELL-MM-MIB-SMIv2", "dmmCA2MessageID"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2Message"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2MessageArgs"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2AlertStatus"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2FQDD"),
        ("DELL-MM-MIB-SMIv2", "dmmProductChassisName"),
        ("DELL-MM-MIB-SMIv2", "dmmChassisServiceTag"))
)
if mibBuilder.loadTexts:
    alert2StorageManagementWarning.setStatus(
        "current"
    )

alert2StorageManagementInformation = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 5, 0, 4179)
)
alert2StorageManagementInformation.setObjects(
      *(("DELL-MM-MIB-SMIv2", "dmmCA2MessageID"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2Message"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2MessageArgs"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2AlertStatus"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2FQDD"),
        ("DELL-MM-MIB-SMIv2", "dmmProductChassisName"),
        ("DELL-MM-MIB-SMIv2", "dmmChassisServiceTag"))
)
if mibBuilder.loadTexts:
    alert2StorageManagementInformation.setStatus(
        "current"
    )

alert2StorageFanFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 5, 0, 4201)
)
alert2StorageFanFailure.setObjects(
      *(("DELL-MM-MIB-SMIv2", "dmmCA2MessageID"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2Message"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2MessageArgs"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2AlertStatus"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2FQDD"),
        ("DELL-MM-MIB-SMIv2", "dmmProductChassisName"),
        ("DELL-MM-MIB-SMIv2", "dmmChassisServiceTag"))
)
if mibBuilder.loadTexts:
    alert2StorageFanFailure.setStatus(
        "current"
    )

alert2StorageFanWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 5, 0, 4202)
)
alert2StorageFanWarning.setObjects(
      *(("DELL-MM-MIB-SMIv2", "dmmCA2MessageID"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2Message"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2MessageArgs"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2AlertStatus"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2FQDD"),
        ("DELL-MM-MIB-SMIv2", "dmmProductChassisName"),
        ("DELL-MM-MIB-SMIv2", "dmmChassisServiceTag"))
)
if mibBuilder.loadTexts:
    alert2StorageFanWarning.setStatus(
        "current"
    )

alert2StorageFanInformation = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 5, 0, 4203)
)
alert2StorageFanInformation.setObjects(
      *(("DELL-MM-MIB-SMIv2", "dmmCA2MessageID"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2Message"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2MessageArgs"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2AlertStatus"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2FQDD"),
        ("DELL-MM-MIB-SMIv2", "dmmProductChassisName"),
        ("DELL-MM-MIB-SMIv2", "dmmChassisServiceTag"))
)
if mibBuilder.loadTexts:
    alert2StorageFanInformation.setStatus(
        "current"
    )

alert2StorageTemperatureProbeFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 5, 0, 4209)
)
alert2StorageTemperatureProbeFailure.setObjects(
      *(("DELL-MM-MIB-SMIv2", "dmmCA2MessageID"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2Message"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2MessageArgs"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2AlertStatus"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2FQDD"),
        ("DELL-MM-MIB-SMIv2", "dmmProductChassisName"),
        ("DELL-MM-MIB-SMIv2", "dmmChassisServiceTag"))
)
if mibBuilder.loadTexts:
    alert2StorageTemperatureProbeFailure.setStatus(
        "current"
    )

alert2StorageTemperatureProbeWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 5, 0, 4210)
)
alert2StorageTemperatureProbeWarning.setObjects(
      *(("DELL-MM-MIB-SMIv2", "dmmCA2MessageID"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2Message"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2MessageArgs"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2AlertStatus"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2FQDD"),
        ("DELL-MM-MIB-SMIv2", "dmmProductChassisName"),
        ("DELL-MM-MIB-SMIv2", "dmmChassisServiceTag"))
)
if mibBuilder.loadTexts:
    alert2StorageTemperatureProbeWarning.setStatus(
        "current"
    )

alert2StorageTemperatureProbeInformation = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 5, 0, 4211)
)
alert2StorageTemperatureProbeInformation.setObjects(
      *(("DELL-MM-MIB-SMIv2", "dmmCA2MessageID"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2Message"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2MessageArgs"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2AlertStatus"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2FQDD"),
        ("DELL-MM-MIB-SMIv2", "dmmProductChassisName"),
        ("DELL-MM-MIB-SMIv2", "dmmChassisServiceTag"))
)
if mibBuilder.loadTexts:
    alert2StorageTemperatureProbeInformation.setStatus(
        "current"
    )

alert2StoragePowerSupplyFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 5, 0, 4233)
)
alert2StoragePowerSupplyFailure.setObjects(
      *(("DELL-MM-MIB-SMIv2", "dmmCA2MessageID"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2Message"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2MessageArgs"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2AlertStatus"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2FQDD"),
        ("DELL-MM-MIB-SMIv2", "dmmProductChassisName"),
        ("DELL-MM-MIB-SMIv2", "dmmChassisServiceTag"))
)
if mibBuilder.loadTexts:
    alert2StoragePowerSupplyFailure.setStatus(
        "current"
    )

alert2StoragePowerSupplyWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 5, 0, 4234)
)
alert2StoragePowerSupplyWarning.setObjects(
      *(("DELL-MM-MIB-SMIv2", "dmmCA2MessageID"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2Message"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2MessageArgs"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2AlertStatus"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2FQDD"),
        ("DELL-MM-MIB-SMIv2", "dmmProductChassisName"),
        ("DELL-MM-MIB-SMIv2", "dmmChassisServiceTag"))
)
if mibBuilder.loadTexts:
    alert2StoragePowerSupplyWarning.setStatus(
        "current"
    )

alert2StoragePowerSupplyInformation = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 5, 0, 4235)
)
alert2StoragePowerSupplyInformation.setObjects(
      *(("DELL-MM-MIB-SMIv2", "dmmCA2MessageID"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2Message"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2MessageArgs"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2AlertStatus"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2FQDD"),
        ("DELL-MM-MIB-SMIv2", "dmmProductChassisName"),
        ("DELL-MM-MIB-SMIv2", "dmmChassisServiceTag"))
)
if mibBuilder.loadTexts:
    alert2StoragePowerSupplyInformation.setStatus(
        "current"
    )

alert2StorageBatteryFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 5, 0, 4273)
)
alert2StorageBatteryFailure.setObjects(
      *(("DELL-MM-MIB-SMIv2", "dmmCA2MessageID"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2Message"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2MessageArgs"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2AlertStatus"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2FQDD"),
        ("DELL-MM-MIB-SMIv2", "dmmProductChassisName"),
        ("DELL-MM-MIB-SMIv2", "dmmChassisServiceTag"))
)
if mibBuilder.loadTexts:
    alert2StorageBatteryFailure.setStatus(
        "current"
    )

alert2StorageBatteryWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 5, 0, 4274)
)
alert2StorageBatteryWarning.setObjects(
      *(("DELL-MM-MIB-SMIv2", "dmmCA2MessageID"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2Message"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2MessageArgs"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2AlertStatus"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2FQDD"),
        ("DELL-MM-MIB-SMIv2", "dmmProductChassisName"),
        ("DELL-MM-MIB-SMIv2", "dmmChassisServiceTag"))
)
if mibBuilder.loadTexts:
    alert2StorageBatteryWarning.setStatus(
        "current"
    )

alert2StorageBatteryInformation = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 5, 0, 4275)
)
alert2StorageBatteryInformation.setObjects(
      *(("DELL-MM-MIB-SMIv2", "dmmCA2MessageID"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2Message"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2MessageArgs"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2AlertStatus"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2FQDD"),
        ("DELL-MM-MIB-SMIv2", "dmmProductChassisName"),
        ("DELL-MM-MIB-SMIv2", "dmmChassisServiceTag"))
)
if mibBuilder.loadTexts:
    alert2StorageBatteryInformation.setStatus(
        "current"
    )

alert2StorageControllerFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 5, 0, 4329)
)
alert2StorageControllerFailure.setObjects(
      *(("DELL-MM-MIB-SMIv2", "dmmCA2MessageID"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2Message"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2MessageArgs"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2AlertStatus"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2FQDD"),
        ("DELL-MM-MIB-SMIv2", "dmmProductChassisName"),
        ("DELL-MM-MIB-SMIv2", "dmmChassisServiceTag"))
)
if mibBuilder.loadTexts:
    alert2StorageControllerFailure.setStatus(
        "current"
    )

alert2StorageControllerWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 5, 0, 4330)
)
alert2StorageControllerWarning.setObjects(
      *(("DELL-MM-MIB-SMIv2", "dmmCA2MessageID"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2Message"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2MessageArgs"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2AlertStatus"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2FQDD"),
        ("DELL-MM-MIB-SMIv2", "dmmProductChassisName"),
        ("DELL-MM-MIB-SMIv2", "dmmChassisServiceTag"))
)
if mibBuilder.loadTexts:
    alert2StorageControllerWarning.setStatus(
        "current"
    )

alert2StorageControllerInformation = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 5, 0, 4331)
)
alert2StorageControllerInformation.setObjects(
      *(("DELL-MM-MIB-SMIv2", "dmmCA2MessageID"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2Message"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2MessageArgs"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2AlertStatus"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2FQDD"),
        ("DELL-MM-MIB-SMIv2", "dmmProductChassisName"),
        ("DELL-MM-MIB-SMIv2", "dmmChassisServiceTag"))
)
if mibBuilder.loadTexts:
    alert2StorageControllerInformation.setStatus(
        "current"
    )

alert2StorageEnclosureFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 5, 0, 4337)
)
alert2StorageEnclosureFailure.setObjects(
      *(("DELL-MM-MIB-SMIv2", "dmmCA2MessageID"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2Message"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2MessageArgs"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2AlertStatus"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2FQDD"),
        ("DELL-MM-MIB-SMIv2", "dmmProductChassisName"),
        ("DELL-MM-MIB-SMIv2", "dmmChassisServiceTag"))
)
if mibBuilder.loadTexts:
    alert2StorageEnclosureFailure.setStatus(
        "current"
    )

alert2StorageEnclosureWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 5, 0, 4338)
)
alert2StorageEnclosureWarning.setObjects(
      *(("DELL-MM-MIB-SMIv2", "dmmCA2MessageID"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2Message"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2MessageArgs"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2AlertStatus"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2FQDD"),
        ("DELL-MM-MIB-SMIv2", "dmmProductChassisName"),
        ("DELL-MM-MIB-SMIv2", "dmmChassisServiceTag"))
)
if mibBuilder.loadTexts:
    alert2StorageEnclosureWarning.setStatus(
        "current"
    )

alert2StorageEnclosureInformation = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 5, 0, 4339)
)
alert2StorageEnclosureInformation.setObjects(
      *(("DELL-MM-MIB-SMIv2", "dmmCA2MessageID"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2Message"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2MessageArgs"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2AlertStatus"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2FQDD"),
        ("DELL-MM-MIB-SMIv2", "dmmProductChassisName"),
        ("DELL-MM-MIB-SMIv2", "dmmChassisServiceTag"))
)
if mibBuilder.loadTexts:
    alert2StorageEnclosureInformation.setStatus(
        "current"
    )

alert2StoragePhysicalDiskFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 5, 0, 4345)
)
alert2StoragePhysicalDiskFailure.setObjects(
      *(("DELL-MM-MIB-SMIv2", "dmmCA2MessageID"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2Message"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2MessageArgs"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2AlertStatus"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2FQDD"),
        ("DELL-MM-MIB-SMIv2", "dmmProductChassisName"),
        ("DELL-MM-MIB-SMIv2", "dmmChassisServiceTag"))
)
if mibBuilder.loadTexts:
    alert2StoragePhysicalDiskFailure.setStatus(
        "current"
    )

alert2StoragePhysicalDiskWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 5, 0, 4346)
)
alert2StoragePhysicalDiskWarning.setObjects(
      *(("DELL-MM-MIB-SMIv2", "dmmCA2MessageID"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2Message"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2MessageArgs"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2AlertStatus"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2FQDD"),
        ("DELL-MM-MIB-SMIv2", "dmmProductChassisName"),
        ("DELL-MM-MIB-SMIv2", "dmmChassisServiceTag"))
)
if mibBuilder.loadTexts:
    alert2StoragePhysicalDiskWarning.setStatus(
        "current"
    )

alert2StoragePhysicalDiskInformation = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 5, 0, 4347)
)
alert2StoragePhysicalDiskInformation.setObjects(
      *(("DELL-MM-MIB-SMIv2", "dmmCA2MessageID"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2Message"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2MessageArgs"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2AlertStatus"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2FQDD"),
        ("DELL-MM-MIB-SMIv2", "dmmProductChassisName"),
        ("DELL-MM-MIB-SMIv2", "dmmChassisServiceTag"))
)
if mibBuilder.loadTexts:
    alert2StoragePhysicalDiskInformation.setStatus(
        "current"
    )

alert2StorageVirtualDiskFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 5, 0, 4353)
)
alert2StorageVirtualDiskFailure.setObjects(
      *(("DELL-MM-MIB-SMIv2", "dmmCA2MessageID"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2Message"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2MessageArgs"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2AlertStatus"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2FQDD"),
        ("DELL-MM-MIB-SMIv2", "dmmProductChassisName"),
        ("DELL-MM-MIB-SMIv2", "dmmChassisServiceTag"))
)
if mibBuilder.loadTexts:
    alert2StorageVirtualDiskFailure.setStatus(
        "current"
    )

alert2StorageVirtualDiskWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 5, 0, 4354)
)
alert2StorageVirtualDiskWarning.setObjects(
      *(("DELL-MM-MIB-SMIv2", "dmmCA2MessageID"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2Message"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2MessageArgs"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2AlertStatus"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2FQDD"),
        ("DELL-MM-MIB-SMIv2", "dmmProductChassisName"),
        ("DELL-MM-MIB-SMIv2", "dmmChassisServiceTag"))
)
if mibBuilder.loadTexts:
    alert2StorageVirtualDiskWarning.setStatus(
        "current"
    )

alert2StorageVirtualDiskInformation = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 5, 0, 4355)
)
alert2StorageVirtualDiskInformation.setObjects(
      *(("DELL-MM-MIB-SMIv2", "dmmCA2MessageID"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2Message"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2MessageArgs"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2AlertStatus"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2FQDD"),
        ("DELL-MM-MIB-SMIv2", "dmmProductChassisName"),
        ("DELL-MM-MIB-SMIv2", "dmmChassisServiceTag"))
)
if mibBuilder.loadTexts:
    alert2StorageVirtualDiskInformation.setStatus(
        "current"
    )

alert2StorageSecurityFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 5, 0, 4433)
)
alert2StorageSecurityFailure.setObjects(
      *(("DELL-MM-MIB-SMIv2", "dmmCA2MessageID"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2Message"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2MessageArgs"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2AlertStatus"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2FQDD"),
        ("DELL-MM-MIB-SMIv2", "dmmProductChassisName"),
        ("DELL-MM-MIB-SMIv2", "dmmChassisServiceTag"))
)
if mibBuilder.loadTexts:
    alert2StorageSecurityFailure.setStatus(
        "current"
    )

alert2StorageSecurityWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 5, 0, 4434)
)
alert2StorageSecurityWarning.setObjects(
      *(("DELL-MM-MIB-SMIv2", "dmmCA2MessageID"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2Message"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2MessageArgs"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2AlertStatus"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2FQDD"),
        ("DELL-MM-MIB-SMIv2", "dmmProductChassisName"),
        ("DELL-MM-MIB-SMIv2", "dmmChassisServiceTag"))
)
if mibBuilder.loadTexts:
    alert2StorageSecurityWarning.setStatus(
        "current"
    )

alert2StorageSecurityInformation = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 5, 0, 4435)
)
alert2StorageSecurityInformation.setObjects(
      *(("DELL-MM-MIB-SMIv2", "dmmCA2MessageID"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2Message"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2MessageArgs"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2AlertStatus"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2FQDD"),
        ("DELL-MM-MIB-SMIv2", "dmmProductChassisName"),
        ("DELL-MM-MIB-SMIv2", "dmmChassisServiceTag"))
)
if mibBuilder.loadTexts:
    alert2StorageSecurityInformation.setStatus(
        "current"
    )

alert2SoftwareChangeUpdateWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 5, 0, 6314)
)
alert2SoftwareChangeUpdateWarning.setObjects(
      *(("DELL-MM-MIB-SMIv2", "dmmCA2MessageID"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2Message"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2MessageArgs"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2AlertStatus"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2FQDD"),
        ("DELL-MM-MIB-SMIv2", "dmmProductChassisName"),
        ("DELL-MM-MIB-SMIv2", "dmmChassisServiceTag"))
)
if mibBuilder.loadTexts:
    alert2SoftwareChangeUpdateWarning.setStatus(
        "current"
    )

alert2PowerSupplyAuditFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 5, 0, 8329)
)
alert2PowerSupplyAuditFailure.setObjects(
      *(("DELL-MM-MIB-SMIv2", "dmmCA2MessageID"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2Message"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2MessageArgs"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2AlertStatus"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2FQDD"),
        ("DELL-MM-MIB-SMIv2", "dmmProductChassisName"),
        ("DELL-MM-MIB-SMIv2", "dmmChassisServiceTag"))
)
if mibBuilder.loadTexts:
    alert2PowerSupplyAuditFailure.setStatus(
        "current"
    )

alert2PowerSupplyAuditWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 5, 0, 8330)
)
alert2PowerSupplyAuditWarning.setObjects(
      *(("DELL-MM-MIB-SMIv2", "dmmCA2MessageID"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2Message"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2MessageArgs"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2AlertStatus"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2FQDD"),
        ("DELL-MM-MIB-SMIv2", "dmmProductChassisName"),
        ("DELL-MM-MIB-SMIv2", "dmmChassisServiceTag"))
)
if mibBuilder.loadTexts:
    alert2PowerSupplyAuditWarning.setStatus(
        "current"
    )

alert2SoftwareChangeAuditFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 5, 0, 8361)
)
alert2SoftwareChangeAuditFailure.setObjects(
      *(("DELL-MM-MIB-SMIv2", "dmmCA2MessageID"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2Message"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2MessageArgs"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2AlertStatus"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2FQDD"),
        ("DELL-MM-MIB-SMIv2", "dmmProductChassisName"),
        ("DELL-MM-MIB-SMIv2", "dmmChassisServiceTag"))
)
if mibBuilder.loadTexts:
    alert2SoftwareChangeAuditFailure.setStatus(
        "current"
    )

alert2PowerUsageAuditFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 5, 0, 8417)
)
alert2PowerUsageAuditFailure.setObjects(
      *(("DELL-MM-MIB-SMIv2", "dmmCA2MessageID"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2Message"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2MessageArgs"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2AlertStatus"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2FQDD"),
        ("DELL-MM-MIB-SMIv2", "dmmProductChassisName"),
        ("DELL-MM-MIB-SMIv2", "dmmChassisServiceTag"))
)
if mibBuilder.loadTexts:
    alert2PowerUsageAuditFailure.setStatus(
        "current"
    )

alert2PowerUsageAuditWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 5, 0, 8418)
)
alert2PowerUsageAuditWarning.setObjects(
      *(("DELL-MM-MIB-SMIv2", "dmmCA2MessageID"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2Message"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2MessageArgs"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2AlertStatus"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2FQDD"),
        ("DELL-MM-MIB-SMIv2", "dmmProductChassisName"),
        ("DELL-MM-MIB-SMIv2", "dmmChassisServiceTag"))
)
if mibBuilder.loadTexts:
    alert2PowerUsageAuditWarning.setStatus(
        "current"
    )

alert2PowerUsageAuditInformation = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 5, 0, 8419)
)
alert2PowerUsageAuditInformation.setObjects(
      *(("DELL-MM-MIB-SMIv2", "dmmCA2MessageID"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2Message"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2MessageArgs"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2AlertStatus"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2FQDD"),
        ("DELL-MM-MIB-SMIv2", "dmmProductChassisName"),
        ("DELL-MM-MIB-SMIv2", "dmmChassisServiceTag"))
)
if mibBuilder.loadTexts:
    alert2PowerUsageAuditInformation.setStatus(
        "current"
    )

alert2LicenseFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 5, 0, 8513)
)
alert2LicenseFailure.setObjects(
      *(("DELL-MM-MIB-SMIv2", "dmmCA2MessageID"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2Message"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2MessageArgs"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2AlertStatus"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2FQDD"),
        ("DELL-MM-MIB-SMIv2", "dmmProductChassisName"),
        ("DELL-MM-MIB-SMIv2", "dmmChassisServiceTag"))
)
if mibBuilder.loadTexts:
    alert2LicenseFailure.setStatus(
        "current"
    )

alert2LicenseWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 5, 0, 8514)
)
alert2LicenseWarning.setObjects(
      *(("DELL-MM-MIB-SMIv2", "dmmCA2MessageID"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2Message"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2MessageArgs"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2AlertStatus"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2FQDD"),
        ("DELL-MM-MIB-SMIv2", "dmmProductChassisName"),
        ("DELL-MM-MIB-SMIv2", "dmmChassisServiceTag"))
)
if mibBuilder.loadTexts:
    alert2LicenseWarning.setStatus(
        "current"
    )

alert2LicenseInformation = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 5, 0, 8515)
)
alert2LicenseInformation.setObjects(
      *(("DELL-MM-MIB-SMIv2", "dmmCA2MessageID"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2Message"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2MessageArgs"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2AlertStatus"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2FQDD"),
        ("DELL-MM-MIB-SMIv2", "dmmProductChassisName"),
        ("DELL-MM-MIB-SMIv2", "dmmChassisServiceTag"))
)
if mibBuilder.loadTexts:
    alert2LicenseInformation.setStatus(
        "current"
    )

alert2PCIDeviceAuditWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 5, 0, 8562)
)
alert2PCIDeviceAuditWarning.setObjects(
      *(("DELL-MM-MIB-SMIv2", "dmmCA2MessageID"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2Message"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2MessageArgs"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2AlertStatus"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2FQDD"),
        ("DELL-MM-MIB-SMIv2", "dmmProductChassisName"),
        ("DELL-MM-MIB-SMIv2", "dmmChassisServiceTag"))
)
if mibBuilder.loadTexts:
    alert2PCIDeviceAuditWarning.setStatus(
        "current"
    )

alert2CMCAuditFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 5, 0, 8689)
)
alert2CMCAuditFailure.setObjects(
      *(("DELL-MM-MIB-SMIv2", "dmmCA2MessageID"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2Message"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2MessageArgs"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2AlertStatus"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2FQDD"),
        ("DELL-MM-MIB-SMIv2", "dmmProductChassisName"),
        ("DELL-MM-MIB-SMIv2", "dmmChassisServiceTag"))
)
if mibBuilder.loadTexts:
    alert2CMCAuditFailure.setStatus(
        "current"
    )

alert2CMCAuditWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 5, 0, 8690)
)
alert2CMCAuditWarning.setObjects(
      *(("DELL-MM-MIB-SMIv2", "dmmCA2MessageID"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2Message"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2MessageArgs"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2AlertStatus"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2FQDD"),
        ("DELL-MM-MIB-SMIv2", "dmmProductChassisName"),
        ("DELL-MM-MIB-SMIv2", "dmmChassisServiceTag"))
)
if mibBuilder.loadTexts:
    alert2CMCAuditWarning.setStatus(
        "current"
    )

alert2CMCAuditInformation = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 5, 0, 8691)
)
alert2CMCAuditInformation.setObjects(
      *(("DELL-MM-MIB-SMIv2", "dmmCA2MessageID"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2Message"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2MessageArgs"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2AlertStatus"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2FQDD"),
        ("DELL-MM-MIB-SMIv2", "dmmProductChassisName"),
        ("DELL-MM-MIB-SMIv2", "dmmChassisServiceTag"))
)
if mibBuilder.loadTexts:
    alert2CMCAuditInformation.setStatus(
        "current"
    )

alert2IOVirtualizationAuditWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 5, 0, 8698)
)
alert2IOVirtualizationAuditWarning.setObjects(
      *(("DELL-MM-MIB-SMIv2", "dmmCA2MessageID"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2Message"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2MessageArgs"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2AlertStatus"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2FQDD"),
        ("DELL-MM-MIB-SMIv2", "dmmProductChassisName"),
        ("DELL-MM-MIB-SMIv2", "dmmChassisServiceTag"))
)
if mibBuilder.loadTexts:
    alert2IOVirtualizationAuditWarning.setStatus(
        "current"
    )

alert2CMCTestTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 5, 0, 10395)
)
alert2CMCTestTrap.setObjects(
      *(("DELL-MM-MIB-SMIv2", "dmmCA2MessageID"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2Message"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2MessageArgs"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2AlertStatus"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2FQDD"),
        ("DELL-MM-MIB-SMIv2", "dmmProductChassisName"),
        ("DELL-MM-MIB-SMIv2", "dmmChassisServiceTag"))
)
if mibBuilder.loadTexts:
    alert2CMCTestTrap.setStatus(
        "current"
    )

alert2SWCConfigurationFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 5, 0, 10529)
)
alert2SWCConfigurationFailure.setObjects(
      *(("DELL-MM-MIB-SMIv2", "dmmCA2MessageID"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2Message"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2MessageArgs"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2AlertStatus"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2FQDD"),
        ("DELL-MM-MIB-SMIv2", "dmmProductChassisName"),
        ("DELL-MM-MIB-SMIv2", "dmmChassisServiceTag"))
)
if mibBuilder.loadTexts:
    alert2SWCConfigurationFailure.setStatus(
        "current"
    )

alert2SWCConfigurationWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 5, 0, 10530)
)
alert2SWCConfigurationWarning.setObjects(
      *(("DELL-MM-MIB-SMIv2", "dmmCA2MessageID"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2Message"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2MessageArgs"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2AlertStatus"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2FQDD"),
        ("DELL-MM-MIB-SMIv2", "dmmProductChassisName"),
        ("DELL-MM-MIB-SMIv2", "dmmChassisServiceTag"))
)
if mibBuilder.loadTexts:
    alert2SWCConfigurationWarning.setStatus(
        "current"
    )

alert2PCIDeviceConfigurationInformation = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 5, 0, 10611)
)
alert2PCIDeviceConfigurationInformation.setObjects(
      *(("DELL-MM-MIB-SMIv2", "dmmCA2MessageID"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2Message"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2MessageArgs"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2AlertStatus"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2FQDD"),
        ("DELL-MM-MIB-SMIv2", "dmmProductChassisName"),
        ("DELL-MM-MIB-SMIv2", "dmmChassisServiceTag"))
)
if mibBuilder.loadTexts:
    alert2PCIDeviceConfigurationInformation.setStatus(
        "current"
    )

alert2IOVConfigurationWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 5, 0, 10746)
)
alert2IOVConfigurationWarning.setObjects(
      *(("DELL-MM-MIB-SMIv2", "dmmCA2MessageID"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2Message"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2MessageArgs"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2AlertStatus"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2FQDD"),
        ("DELL-MM-MIB-SMIv2", "dmmProductChassisName"),
        ("DELL-MM-MIB-SMIv2", "dmmChassisServiceTag"))
)
if mibBuilder.loadTexts:
    alert2IOVConfigurationWarning.setStatus(
        "current"
    )

alert2IOVConfigurationInformation = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 5, 0, 10747)
)
alert2IOVConfigurationInformation.setObjects(
      *(("DELL-MM-MIB-SMIv2", "dmmCA2MessageID"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2Message"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2MessageArgs"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2AlertStatus"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2FQDD"),
        ("DELL-MM-MIB-SMIv2", "dmmProductChassisName"),
        ("DELL-MM-MIB-SMIv2", "dmmChassisServiceTag"))
)
if mibBuilder.loadTexts:
    alert2IOVConfigurationInformation.setStatus(
        "current"
    )

alert851138RCPRestoreInformational = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 5, 0, 851138)
)
alert851138RCPRestoreInformational.setObjects(
      *(("DELL-MM-MIB-SMIv2", "dmmCA2MessageID"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2Message"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2MessageArgs"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2AlertStatus"),
        ("DELL-MM-MIB-SMIv2", "dmmDeviceServiceTag"),
        ("DELL-MM-MIB-SMIv2", "dmmCategoryName"),
        ("DELL-MM-MIB-SMIv2", "dmmSubCategoryName"),
        ("DELL-MM-MIB-SMIv2", "dmmSeverity"))
)
if mibBuilder.loadTexts:
    alert851138RCPRestoreInformational.setStatus(
        "current"
    )

alert851139RCPRestoreCritical = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 5, 0, 851139)
)
alert851139RCPRestoreCritical.setObjects(
      *(("DELL-MM-MIB-SMIv2", "dmmCA2MessageID"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2Message"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2MessageArgs"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2AlertStatus"),
        ("DELL-MM-MIB-SMIv2", "dmmDeviceServiceTag"),
        ("DELL-MM-MIB-SMIv2", "dmmCategoryName"),
        ("DELL-MM-MIB-SMIv2", "dmmSubCategoryName"),
        ("DELL-MM-MIB-SMIv2", "dmmSeverity"))
)
if mibBuilder.loadTexts:
    alert851139RCPRestoreCritical.setStatus(
        "current"
    )

alert856129DeviceStateInformational = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 5, 0, 856129)
)
alert856129DeviceStateInformational.setObjects(
      *(("DELL-MM-MIB-SMIv2", "dmmCA2MessageID"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2Message"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2MessageArgs"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2AlertStatus"),
        ("DELL-MM-MIB-SMIv2", "dmmDeviceServiceTag"),
        ("DELL-MM-MIB-SMIv2", "dmmCategoryName"),
        ("DELL-MM-MIB-SMIv2", "dmmSubCategoryName"),
        ("DELL-MM-MIB-SMIv2", "dmmSeverity"))
)
if mibBuilder.loadTexts:
    alert856129DeviceStateInformational.setStatus(
        "current"
    )

alert856130DeviceStateCritical = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 5, 0, 856130)
)
alert856130DeviceStateCritical.setObjects(
      *(("DELL-MM-MIB-SMIv2", "dmmCA2MessageID"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2Message"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2MessageArgs"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2AlertStatus"),
        ("DELL-MM-MIB-SMIv2", "dmmDeviceServiceTag"),
        ("DELL-MM-MIB-SMIv2", "dmmCategoryName"),
        ("DELL-MM-MIB-SMIv2", "dmmSubCategoryName"),
        ("DELL-MM-MIB-SMIv2", "dmmSeverity"))
)
if mibBuilder.loadTexts:
    alert856130DeviceStateCritical.setStatus(
        "current"
    )

alert856131DeviceStateCritical = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 5, 0, 856131)
)
alert856131DeviceStateCritical.setObjects(
      *(("DELL-MM-MIB-SMIv2", "dmmCA2MessageID"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2Message"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2MessageArgs"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2AlertStatus"),
        ("DELL-MM-MIB-SMIv2", "dmmDeviceServiceTag"),
        ("DELL-MM-MIB-SMIv2", "dmmCategoryName"),
        ("DELL-MM-MIB-SMIv2", "dmmSubCategoryName"),
        ("DELL-MM-MIB-SMIv2", "dmmSeverity"))
)
if mibBuilder.loadTexts:
    alert856131DeviceStateCritical.setStatus(
        "current"
    )

alert856132DeviceStateInformational = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 5, 0, 856132)
)
alert856132DeviceStateInformational.setObjects(
      *(("DELL-MM-MIB-SMIv2", "dmmCA2MessageID"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2Message"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2MessageArgs"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2AlertStatus"),
        ("DELL-MM-MIB-SMIv2", "dmmDeviceServiceTag"),
        ("DELL-MM-MIB-SMIv2", "dmmCategoryName"),
        ("DELL-MM-MIB-SMIv2", "dmmSubCategoryName"),
        ("DELL-MM-MIB-SMIv2", "dmmSeverity"))
)
if mibBuilder.loadTexts:
    alert856132DeviceStateInformational.setStatus(
        "current"
    )

alert856133DeviceStateInformational = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 5, 0, 856133)
)
alert856133DeviceStateInformational.setObjects(
      *(("DELL-MM-MIB-SMIv2", "dmmCA2MessageID"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2Message"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2MessageArgs"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2AlertStatus"),
        ("DELL-MM-MIB-SMIv2", "dmmDeviceServiceTag"),
        ("DELL-MM-MIB-SMIv2", "dmmCategoryName"),
        ("DELL-MM-MIB-SMIv2", "dmmSubCategoryName"),
        ("DELL-MM-MIB-SMIv2", "dmmSeverity"))
)
if mibBuilder.loadTexts:
    alert856133DeviceStateInformational.setStatus(
        "current"
    )

alert856134DeviceStateInformational = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 5, 0, 856134)
)
alert856134DeviceStateInformational.setObjects(
      *(("DELL-MM-MIB-SMIv2", "dmmCA2MessageID"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2Message"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2MessageArgs"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2AlertStatus"),
        ("DELL-MM-MIB-SMIv2", "dmmDeviceServiceTag"),
        ("DELL-MM-MIB-SMIv2", "dmmCategoryName"),
        ("DELL-MM-MIB-SMIv2", "dmmSubCategoryName"),
        ("DELL-MM-MIB-SMIv2", "dmmSeverity"))
)
if mibBuilder.loadTexts:
    alert856134DeviceStateInformational.setStatus(
        "current"
    )

alert856172DeviceStateInformational = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 5, 0, 856172)
)
alert856172DeviceStateInformational.setObjects(
      *(("DELL-MM-MIB-SMIv2", "dmmCA2MessageID"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2Message"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2MessageArgs"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2AlertStatus"),
        ("DELL-MM-MIB-SMIv2", "dmmDeviceServiceTag"),
        ("DELL-MM-MIB-SMIv2", "dmmCategoryName"),
        ("DELL-MM-MIB-SMIv2", "dmmSubCategoryName"),
        ("DELL-MM-MIB-SMIv2", "dmmSeverity"))
)
if mibBuilder.loadTexts:
    alert856172DeviceStateInformational.setStatus(
        "current"
    )

alert856173DeviceStateCritical = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 5, 0, 856173)
)
alert856173DeviceStateCritical.setObjects(
      *(("DELL-MM-MIB-SMIv2", "dmmCA2MessageID"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2Message"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2MessageArgs"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2AlertStatus"),
        ("DELL-MM-MIB-SMIv2", "dmmDeviceServiceTag"),
        ("DELL-MM-MIB-SMIv2", "dmmCategoryName"),
        ("DELL-MM-MIB-SMIv2", "dmmSubCategoryName"),
        ("DELL-MM-MIB-SMIv2", "dmmSeverity"))
)
if mibBuilder.loadTexts:
    alert856173DeviceStateCritical.setStatus(
        "current"
    )

alert856174DeviceStateCritical = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 5, 0, 856174)
)
alert856174DeviceStateCritical.setObjects(
      *(("DELL-MM-MIB-SMIv2", "dmmCA2MessageID"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2Message"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2MessageArgs"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2AlertStatus"),
        ("DELL-MM-MIB-SMIv2", "dmmDeviceServiceTag"),
        ("DELL-MM-MIB-SMIv2", "dmmCategoryName"),
        ("DELL-MM-MIB-SMIv2", "dmmSubCategoryName"),
        ("DELL-MM-MIB-SMIv2", "dmmSeverity"))
)
if mibBuilder.loadTexts:
    alert856174DeviceStateCritical.setStatus(
        "current"
    )

alert856175DeviceStateWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 5, 0, 856175)
)
alert856175DeviceStateWarning.setObjects(
      *(("DELL-MM-MIB-SMIv2", "dmmCA2MessageID"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2Message"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2MessageArgs"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2AlertStatus"),
        ("DELL-MM-MIB-SMIv2", "dmmDeviceServiceTag"),
        ("DELL-MM-MIB-SMIv2", "dmmCategoryName"),
        ("DELL-MM-MIB-SMIv2", "dmmSubCategoryName"),
        ("DELL-MM-MIB-SMIv2", "dmmSeverity"))
)
if mibBuilder.loadTexts:
    alert856175DeviceStateWarning.setStatus(
        "current"
    )

alertGenericCritical = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 6, 0, 100)
)
alertGenericCritical.setObjects(
      *(("DELL-MM-MIB-SMIv2", "dmmCA2MessageID"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2Message"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2MessageArgs"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2AlertStatus"),
        ("DELL-MM-MIB-SMIv2", "dmmDeviceServiceTag"),
        ("DELL-MM-MIB-SMIv2", "dmmCategoryName"),
        ("DELL-MM-MIB-SMIv2", "dmmSubCategoryName"),
        ("DELL-MM-MIB-SMIv2", "dmmSeverity"))
)
if mibBuilder.loadTexts:
    alertGenericCritical.setStatus(
        "current"
    )

alertGenericWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 6, 0, 200)
)
alertGenericWarning.setObjects(
      *(("DELL-MM-MIB-SMIv2", "dmmCA2MessageID"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2Message"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2MessageArgs"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2AlertStatus"),
        ("DELL-MM-MIB-SMIv2", "dmmDeviceServiceTag"),
        ("DELL-MM-MIB-SMIv2", "dmmCategoryName"),
        ("DELL-MM-MIB-SMIv2", "dmmSubCategoryName"),
        ("DELL-MM-MIB-SMIv2", "dmmSeverity"))
)
if mibBuilder.loadTexts:
    alertGenericWarning.setStatus(
        "current"
    )

alertGenericNormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 6, 0, 300)
)
alertGenericNormal.setObjects(
      *(("DELL-MM-MIB-SMIv2", "dmmCA2MessageID"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2Message"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2MessageArgs"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2AlertStatus"),
        ("DELL-MM-MIB-SMIv2", "dmmDeviceServiceTag"),
        ("DELL-MM-MIB-SMIv2", "dmmCategoryName"),
        ("DELL-MM-MIB-SMIv2", "dmmSubCategoryName"),
        ("DELL-MM-MIB-SMIv2", "dmmSeverity"))
)
if mibBuilder.loadTexts:
    alertGenericNormal.setStatus(
        "current"
    )

alertGenericInformational = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 6, 0, 400)
)
alertGenericInformational.setObjects(
      *(("DELL-MM-MIB-SMIv2", "dmmCA2MessageID"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2Message"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2MessageArgs"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2AlertStatus"),
        ("DELL-MM-MIB-SMIv2", "dmmDeviceServiceTag"),
        ("DELL-MM-MIB-SMIv2", "dmmCategoryName"),
        ("DELL-MM-MIB-SMIv2", "dmmSubCategoryName"),
        ("DELL-MM-MIB-SMIv2", "dmmSeverity"))
)
if mibBuilder.loadTexts:
    alertGenericInformational.setStatus(
        "current"
    )

alertGenericTestTrapEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 6, 0, 500)
)
alertGenericTestTrapEvent.setObjects(
    ("DELL-MM-MIB-SMIv2", "dmmCA2Message")
)
if mibBuilder.loadTexts:
    alertGenericTestTrapEvent.setStatus(
        "current"
    )

alertAuditCritical = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 6, 0, 600)
)
alertAuditCritical.setObjects(
      *(("DELL-MM-MIB-SMIv2", "dmmCA2MessageID"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2Message"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2MessageArgs"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2AlertStatus"),
        ("DELL-MM-MIB-SMIv2", "dmmDeviceServiceTag"),
        ("DELL-MM-MIB-SMIv2", "dmmCategoryName"),
        ("DELL-MM-MIB-SMIv2", "dmmSubCategoryName"),
        ("DELL-MM-MIB-SMIv2", "dmmSeverity"))
)
if mibBuilder.loadTexts:
    alertAuditCritical.setStatus(
        "current"
    )

alertAuditWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 6, 0, 700)
)
alertAuditWarning.setObjects(
      *(("DELL-MM-MIB-SMIv2", "dmmCA2MessageID"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2Message"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2MessageArgs"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2AlertStatus"),
        ("DELL-MM-MIB-SMIv2", "dmmDeviceServiceTag"),
        ("DELL-MM-MIB-SMIv2", "dmmCategoryName"),
        ("DELL-MM-MIB-SMIv2", "dmmSubCategoryName"),
        ("DELL-MM-MIB-SMIv2", "dmmSeverity"))
)
if mibBuilder.loadTexts:
    alertAuditWarning.setStatus(
        "current"
    )

alertAuditNormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 6, 0, 800)
)
alertAuditNormal.setObjects(
      *(("DELL-MM-MIB-SMIv2", "dmmCA2MessageID"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2Message"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2MessageArgs"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2AlertStatus"),
        ("DELL-MM-MIB-SMIv2", "dmmDeviceServiceTag"),
        ("DELL-MM-MIB-SMIv2", "dmmCategoryName"),
        ("DELL-MM-MIB-SMIv2", "dmmSubCategoryName"),
        ("DELL-MM-MIB-SMIv2", "dmmSeverity"))
)
if mibBuilder.loadTexts:
    alertAuditNormal.setStatus(
        "current"
    )

alertAuditInformational = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 6, 0, 900)
)
alertAuditInformational.setObjects(
      *(("DELL-MM-MIB-SMIv2", "dmmCA2MessageID"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2Message"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2MessageArgs"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2AlertStatus"),
        ("DELL-MM-MIB-SMIv2", "dmmDeviceServiceTag"),
        ("DELL-MM-MIB-SMIv2", "dmmCategoryName"),
        ("DELL-MM-MIB-SMIv2", "dmmSubCategoryName"),
        ("DELL-MM-MIB-SMIv2", "dmmSeverity"))
)
if mibBuilder.loadTexts:
    alertAuditInformational.setStatus(
        "current"
    )

iDRAC2089alertNetworkFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 7, 0, 2089)
)
iDRAC2089alertNetworkFailure.setObjects(
      *(("DELL-MM-MIB-SMIv2", "dmmCA2MessageID"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2Message"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2MessageArgs"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2AlertStatus"),
        ("DELL-MM-MIB-SMIv2", "dmmDeviceServiceTag"),
        ("DELL-MM-MIB-SMIv2", "dmmCategoryName"),
        ("DELL-MM-MIB-SMIv2", "dmmSubCategoryName"),
        ("DELL-MM-MIB-SMIv2", "dmmSeverity"))
)
if mibBuilder.loadTexts:
    iDRAC2089alertNetworkFailure.setStatus(
        "current"
    )

iDRAC2090alertNetworkWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 7, 0, 2090)
)
iDRAC2090alertNetworkWarning.setObjects(
      *(("DELL-MM-MIB-SMIv2", "dmmCA2MessageID"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2Message"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2MessageArgs"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2AlertStatus"),
        ("DELL-MM-MIB-SMIv2", "dmmDeviceServiceTag"),
        ("DELL-MM-MIB-SMIv2", "dmmCategoryName"),
        ("DELL-MM-MIB-SMIv2", "dmmSubCategoryName"),
        ("DELL-MM-MIB-SMIv2", "dmmSeverity"))
)
if mibBuilder.loadTexts:
    iDRAC2090alertNetworkWarning.setStatus(
        "current"
    )

iDRAC2091alertNetworkInformation = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 7, 0, 2091)
)
iDRAC2091alertNetworkInformation.setObjects(
      *(("DELL-MM-MIB-SMIv2", "dmmCA2MessageID"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2Message"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2MessageArgs"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2AlertStatus"),
        ("DELL-MM-MIB-SMIv2", "dmmDeviceServiceTag"),
        ("DELL-MM-MIB-SMIv2", "dmmCategoryName"),
        ("DELL-MM-MIB-SMIv2", "dmmSubCategoryName"),
        ("DELL-MM-MIB-SMIv2", "dmmSeverity"))
)
if mibBuilder.loadTexts:
    iDRAC2091alertNetworkInformation.setStatus(
        "current"
    )

iDRAC2153alertFanFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 7, 0, 2153)
)
iDRAC2153alertFanFailure.setObjects(
      *(("DELL-MM-MIB-SMIv2", "dmmCA2MessageID"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2Message"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2MessageArgs"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2AlertStatus"),
        ("DELL-MM-MIB-SMIv2", "dmmDeviceServiceTag"),
        ("DELL-MM-MIB-SMIv2", "dmmCategoryName"),
        ("DELL-MM-MIB-SMIv2", "dmmSubCategoryName"),
        ("DELL-MM-MIB-SMIv2", "dmmSeverity"))
)
if mibBuilder.loadTexts:
    iDRAC2153alertFanFailure.setStatus(
        "current"
    )

iDRAC2154alertFanWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 7, 0, 2154)
)
iDRAC2154alertFanWarning.setObjects(
      *(("DELL-MM-MIB-SMIv2", "dmmCA2MessageID"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2Message"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2MessageArgs"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2AlertStatus"),
        ("DELL-MM-MIB-SMIv2", "dmmDeviceServiceTag"),
        ("DELL-MM-MIB-SMIv2", "dmmCategoryName"),
        ("DELL-MM-MIB-SMIv2", "dmmSubCategoryName"),
        ("DELL-MM-MIB-SMIv2", "dmmSeverity"))
)
if mibBuilder.loadTexts:
    iDRAC2154alertFanWarning.setStatus(
        "current"
    )

iDRAC2155alertFanInformation = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 7, 0, 2155)
)
iDRAC2155alertFanInformation.setObjects(
      *(("DELL-MM-MIB-SMIv2", "dmmCA2MessageID"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2Message"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2MessageArgs"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2AlertStatus"),
        ("DELL-MM-MIB-SMIv2", "dmmDeviceServiceTag"),
        ("DELL-MM-MIB-SMIv2", "dmmCategoryName"),
        ("DELL-MM-MIB-SMIv2", "dmmSubCategoryName"),
        ("DELL-MM-MIB-SMIv2", "dmmSeverity"))
)
if mibBuilder.loadTexts:
    iDRAC2155alertFanInformation.setStatus(
        "current"
    )

iDRAC2161alertTemperatureProbeFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 7, 0, 2161)
)
iDRAC2161alertTemperatureProbeFailure.setObjects(
      *(("DELL-MM-MIB-SMIv2", "dmmCA2MessageID"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2Message"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2MessageArgs"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2AlertStatus"),
        ("DELL-MM-MIB-SMIv2", "dmmDeviceServiceTag"),
        ("DELL-MM-MIB-SMIv2", "dmmCategoryName"),
        ("DELL-MM-MIB-SMIv2", "dmmSubCategoryName"),
        ("DELL-MM-MIB-SMIv2", "dmmSeverity"))
)
if mibBuilder.loadTexts:
    iDRAC2161alertTemperatureProbeFailure.setStatus(
        "current"
    )

iDRAC2162alertTemperatureProbeWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 7, 0, 2162)
)
iDRAC2162alertTemperatureProbeWarning.setObjects(
      *(("DELL-MM-MIB-SMIv2", "dmmCA2MessageID"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2Message"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2MessageArgs"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2AlertStatus"),
        ("DELL-MM-MIB-SMIv2", "dmmDeviceServiceTag"),
        ("DELL-MM-MIB-SMIv2", "dmmCategoryName"),
        ("DELL-MM-MIB-SMIv2", "dmmSubCategoryName"),
        ("DELL-MM-MIB-SMIv2", "dmmSeverity"))
)
if mibBuilder.loadTexts:
    iDRAC2162alertTemperatureProbeWarning.setStatus(
        "current"
    )

iDRAC2163alertTemperatureProbeNormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 7, 0, 2163)
)
iDRAC2163alertTemperatureProbeNormal.setObjects(
      *(("DELL-MM-MIB-SMIv2", "dmmCA2MessageID"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2Message"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2MessageArgs"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2AlertStatus"),
        ("DELL-MM-MIB-SMIv2", "dmmDeviceServiceTag"),
        ("DELL-MM-MIB-SMIv2", "dmmCategoryName"),
        ("DELL-MM-MIB-SMIv2", "dmmSubCategoryName"),
        ("DELL-MM-MIB-SMIv2", "dmmSeverity"))
)
if mibBuilder.loadTexts:
    iDRAC2163alertTemperatureProbeNormal.setStatus(
        "current"
    )

iDRAC2169alertVoltageProbeFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 7, 0, 2169)
)
iDRAC2169alertVoltageProbeFailure.setObjects(
      *(("DELL-MM-MIB-SMIv2", "dmmCA2MessageID"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2Message"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2MessageArgs"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2AlertStatus"),
        ("DELL-MM-MIB-SMIv2", "dmmDeviceServiceTag"),
        ("DELL-MM-MIB-SMIv2", "dmmCategoryName"),
        ("DELL-MM-MIB-SMIv2", "dmmSubCategoryName"),
        ("DELL-MM-MIB-SMIv2", "dmmSeverity"))
)
if mibBuilder.loadTexts:
    iDRAC2169alertVoltageProbeFailure.setStatus(
        "current"
    )

iDRAC2170alertVoltageProbeWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 7, 0, 2170)
)
iDRAC2170alertVoltageProbeWarning.setObjects(
      *(("DELL-MM-MIB-SMIv2", "dmmCA2MessageID"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2Message"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2MessageArgs"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2AlertStatus"),
        ("DELL-MM-MIB-SMIv2", "dmmDeviceServiceTag"),
        ("DELL-MM-MIB-SMIv2", "dmmCategoryName"),
        ("DELL-MM-MIB-SMIv2", "dmmSubCategoryName"),
        ("DELL-MM-MIB-SMIv2", "dmmSeverity"))
)
if mibBuilder.loadTexts:
    iDRAC2170alertVoltageProbeWarning.setStatus(
        "current"
    )

iDRAC2171alertVoltageProbeNormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 7, 0, 2171)
)
iDRAC2171alertVoltageProbeNormal.setObjects(
      *(("DELL-MM-MIB-SMIv2", "dmmCA2MessageID"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2Message"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2MessageArgs"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2AlertStatus"),
        ("DELL-MM-MIB-SMIv2", "dmmDeviceServiceTag"),
        ("DELL-MM-MIB-SMIv2", "dmmCategoryName"),
        ("DELL-MM-MIB-SMIv2", "dmmSubCategoryName"),
        ("DELL-MM-MIB-SMIv2", "dmmSeverity"))
)
if mibBuilder.loadTexts:
    iDRAC2171alertVoltageProbeNormal.setStatus(
        "current"
    )

iDRAC2177alertAmperageProbeFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 7, 0, 2177)
)
iDRAC2177alertAmperageProbeFailure.setObjects(
      *(("DELL-MM-MIB-SMIv2", "dmmCA2MessageID"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2Message"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2MessageArgs"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2AlertStatus"),
        ("DELL-MM-MIB-SMIv2", "dmmDeviceServiceTag"),
        ("DELL-MM-MIB-SMIv2", "dmmCategoryName"),
        ("DELL-MM-MIB-SMIv2", "dmmSubCategoryName"),
        ("DELL-MM-MIB-SMIv2", "dmmSeverity"))
)
if mibBuilder.loadTexts:
    iDRAC2177alertAmperageProbeFailure.setStatus(
        "current"
    )

iDRAC2178alertAmperageProbeWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 7, 0, 2178)
)
iDRAC2178alertAmperageProbeWarning.setObjects(
      *(("DELL-MM-MIB-SMIv2", "dmmCA2MessageID"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2Message"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2MessageArgs"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2AlertStatus"),
        ("DELL-MM-MIB-SMIv2", "dmmDeviceServiceTag"),
        ("DELL-MM-MIB-SMIv2", "dmmCategoryName"),
        ("DELL-MM-MIB-SMIv2", "dmmSubCategoryName"),
        ("DELL-MM-MIB-SMIv2", "dmmSeverity"))
)
if mibBuilder.loadTexts:
    iDRAC2178alertAmperageProbeWarning.setStatus(
        "current"
    )

iDRAC2179alertAmperageProbeNormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 7, 0, 2179)
)
iDRAC2179alertAmperageProbeNormal.setObjects(
      *(("DELL-MM-MIB-SMIv2", "dmmCA2MessageID"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2Message"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2MessageArgs"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2AlertStatus"),
        ("DELL-MM-MIB-SMIv2", "dmmDeviceServiceTag"),
        ("DELL-MM-MIB-SMIv2", "dmmCategoryName"),
        ("DELL-MM-MIB-SMIv2", "dmmSubCategoryName"),
        ("DELL-MM-MIB-SMIv2", "dmmSeverity"))
)
if mibBuilder.loadTexts:
    iDRAC2179alertAmperageProbeNormal.setStatus(
        "current"
    )

iDRAC2185alertPowerSupplyFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 7, 0, 2185)
)
iDRAC2185alertPowerSupplyFailure.setObjects(
      *(("DELL-MM-MIB-SMIv2", "dmmCA2MessageID"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2Message"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2MessageArgs"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2AlertStatus"),
        ("DELL-MM-MIB-SMIv2", "dmmDeviceServiceTag"),
        ("DELL-MM-MIB-SMIv2", "dmmCategoryName"),
        ("DELL-MM-MIB-SMIv2", "dmmSubCategoryName"),
        ("DELL-MM-MIB-SMIv2", "dmmSeverity"))
)
if mibBuilder.loadTexts:
    iDRAC2185alertPowerSupplyFailure.setStatus(
        "current"
    )

iDRAC2186alertPowerSupplyWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 7, 0, 2186)
)
iDRAC2186alertPowerSupplyWarning.setObjects(
      *(("DELL-MM-MIB-SMIv2", "dmmCA2MessageID"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2Message"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2MessageArgs"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2AlertStatus"),
        ("DELL-MM-MIB-SMIv2", "dmmDeviceServiceTag"),
        ("DELL-MM-MIB-SMIv2", "dmmCategoryName"),
        ("DELL-MM-MIB-SMIv2", "dmmSubCategoryName"),
        ("DELL-MM-MIB-SMIv2", "dmmSeverity"))
)
if mibBuilder.loadTexts:
    iDRAC2186alertPowerSupplyWarning.setStatus(
        "current"
    )

iDRAC2187alertPowerSupplyNormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 7, 0, 2187)
)
iDRAC2187alertPowerSupplyNormal.setObjects(
      *(("DELL-MM-MIB-SMIv2", "dmmCA2MessageID"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2Message"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2MessageArgs"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2AlertStatus"),
        ("DELL-MM-MIB-SMIv2", "dmmDeviceServiceTag"),
        ("DELL-MM-MIB-SMIv2", "dmmCategoryName"),
        ("DELL-MM-MIB-SMIv2", "dmmSubCategoryName"),
        ("DELL-MM-MIB-SMIv2", "dmmSeverity"))
)
if mibBuilder.loadTexts:
    iDRAC2187alertPowerSupplyNormal.setStatus(
        "current"
    )

iDRAC2209alertIntegratedDualSDModuleFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 7, 0, 2209)
)
iDRAC2209alertIntegratedDualSDModuleFailure.setObjects(
      *(("DELL-MM-MIB-SMIv2", "dmmCA2MessageID"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2Message"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2MessageArgs"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2AlertStatus"),
        ("DELL-MM-MIB-SMIv2", "dmmDeviceServiceTag"),
        ("DELL-MM-MIB-SMIv2", "dmmCategoryName"),
        ("DELL-MM-MIB-SMIv2", "dmmSubCategoryName"),
        ("DELL-MM-MIB-SMIv2", "dmmSeverity"))
)
if mibBuilder.loadTexts:
    iDRAC2209alertIntegratedDualSDModuleFailure.setStatus(
        "current"
    )

iDRAC2210alertIntegratedDualSDModuleWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 7, 0, 2210)
)
iDRAC2210alertIntegratedDualSDModuleWarning.setObjects(
      *(("DELL-MM-MIB-SMIv2", "dmmCA2MessageID"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2Message"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2MessageArgs"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2AlertStatus"),
        ("DELL-MM-MIB-SMIv2", "dmmDeviceServiceTag"),
        ("DELL-MM-MIB-SMIv2", "dmmCategoryName"),
        ("DELL-MM-MIB-SMIv2", "dmmSubCategoryName"),
        ("DELL-MM-MIB-SMIv2", "dmmSeverity"))
)
if mibBuilder.loadTexts:
    iDRAC2210alertIntegratedDualSDModuleWarning.setStatus(
        "current"
    )

iDRAC2211alertIntegratedDualSDModuleInformation = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 7, 0, 2211)
)
iDRAC2211alertIntegratedDualSDModuleInformation.setObjects(
      *(("DELL-MM-MIB-SMIv2", "dmmCA2MessageID"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2Message"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2MessageArgs"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2AlertStatus"),
        ("DELL-MM-MIB-SMIv2", "dmmDeviceServiceTag"),
        ("DELL-MM-MIB-SMIv2", "dmmCategoryName"),
        ("DELL-MM-MIB-SMIv2", "dmmSubCategoryName"),
        ("DELL-MM-MIB-SMIv2", "dmmSeverity"))
)
if mibBuilder.loadTexts:
    iDRAC2211alertIntegratedDualSDModuleInformation.setStatus(
        "current"
    )

iDRAC2225alertBatteryFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 7, 0, 2225)
)
iDRAC2225alertBatteryFailure.setObjects(
      *(("DELL-MM-MIB-SMIv2", "dmmCA2MessageID"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2Message"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2MessageArgs"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2AlertStatus"),
        ("DELL-MM-MIB-SMIv2", "dmmDeviceServiceTag"),
        ("DELL-MM-MIB-SMIv2", "dmmCategoryName"),
        ("DELL-MM-MIB-SMIv2", "dmmSubCategoryName"),
        ("DELL-MM-MIB-SMIv2", "dmmSeverity"))
)
if mibBuilder.loadTexts:
    iDRAC2225alertBatteryFailure.setStatus(
        "current"
    )

iDRAC2226alertBatteryWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 7, 0, 2226)
)
iDRAC2226alertBatteryWarning.setObjects(
      *(("DELL-MM-MIB-SMIv2", "dmmCA2MessageID"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2Message"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2MessageArgs"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2AlertStatus"),
        ("DELL-MM-MIB-SMIv2", "dmmDeviceServiceTag"),
        ("DELL-MM-MIB-SMIv2", "dmmCategoryName"),
        ("DELL-MM-MIB-SMIv2", "dmmSubCategoryName"),
        ("DELL-MM-MIB-SMIv2", "dmmSeverity"))
)
if mibBuilder.loadTexts:
    iDRAC2226alertBatteryWarning.setStatus(
        "current"
    )

iDRAC2227alertBatteryNormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 7, 0, 2227)
)
iDRAC2227alertBatteryNormal.setObjects(
      *(("DELL-MM-MIB-SMIv2", "dmmCA2MessageID"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2Message"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2MessageArgs"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2AlertStatus"),
        ("DELL-MM-MIB-SMIv2", "dmmDeviceServiceTag"),
        ("DELL-MM-MIB-SMIv2", "dmmCategoryName"),
        ("DELL-MM-MIB-SMIv2", "dmmSubCategoryName"),
        ("DELL-MM-MIB-SMIv2", "dmmSeverity"))
)
if mibBuilder.loadTexts:
    iDRAC2227alertBatteryNormal.setStatus(
        "current"
    )

iDRAC2233alertAutomaticSystemRecovery = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 7, 0, 2233)
)
iDRAC2233alertAutomaticSystemRecovery.setObjects(
      *(("DELL-MM-MIB-SMIv2", "dmmCA2MessageID"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2Message"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2MessageArgs"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2AlertStatus"),
        ("DELL-MM-MIB-SMIv2", "dmmDeviceServiceTag"),
        ("DELL-MM-MIB-SMIv2", "dmmCategoryName"),
        ("DELL-MM-MIB-SMIv2", "dmmSubCategoryName"),
        ("DELL-MM-MIB-SMIv2", "dmmSeverity"))
)
if mibBuilder.loadTexts:
    iDRAC2233alertAutomaticSystemRecovery.setStatus(
        "current"
    )

iDRAC2241alertProcessorDeviceStatusFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 7, 0, 2241)
)
iDRAC2241alertProcessorDeviceStatusFailure.setObjects(
      *(("DELL-MM-MIB-SMIv2", "dmmCA2MessageID"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2Message"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2MessageArgs"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2AlertStatus"),
        ("DELL-MM-MIB-SMIv2", "dmmDeviceServiceTag"),
        ("DELL-MM-MIB-SMIv2", "dmmCategoryName"),
        ("DELL-MM-MIB-SMIv2", "dmmSubCategoryName"),
        ("DELL-MM-MIB-SMIv2", "dmmSeverity"))
)
if mibBuilder.loadTexts:
    iDRAC2241alertProcessorDeviceStatusFailure.setStatus(
        "current"
    )

iDRAC2242alertProcessorDeviceStatusWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 7, 0, 2242)
)
iDRAC2242alertProcessorDeviceStatusWarning.setObjects(
      *(("DELL-MM-MIB-SMIv2", "dmmCA2MessageID"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2Message"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2MessageArgs"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2AlertStatus"),
        ("DELL-MM-MIB-SMIv2", "dmmDeviceServiceTag"),
        ("DELL-MM-MIB-SMIv2", "dmmCategoryName"),
        ("DELL-MM-MIB-SMIv2", "dmmSubCategoryName"),
        ("DELL-MM-MIB-SMIv2", "dmmSeverity"))
)
if mibBuilder.loadTexts:
    iDRAC2242alertProcessorDeviceStatusWarning.setStatus(
        "current"
    )

iDRAC2243alertProcessorDeviceStatusNormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 7, 0, 2243)
)
iDRAC2243alertProcessorDeviceStatusNormal.setObjects(
      *(("DELL-MM-MIB-SMIv2", "dmmCA2MessageID"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2Message"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2MessageArgs"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2AlertStatus"),
        ("DELL-MM-MIB-SMIv2", "dmmDeviceServiceTag"),
        ("DELL-MM-MIB-SMIv2", "dmmCategoryName"),
        ("DELL-MM-MIB-SMIv2", "dmmSubCategoryName"),
        ("DELL-MM-MIB-SMIv2", "dmmSeverity"))
)
if mibBuilder.loadTexts:
    iDRAC2243alertProcessorDeviceStatusNormal.setStatus(
        "current"
    )

iDRAC2249alertLinkStatusFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 7, 0, 2249)
)
iDRAC2249alertLinkStatusFailure.setObjects(
      *(("DELL-MM-MIB-SMIv2", "dmmCA2MessageID"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2Message"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2MessageArgs"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2AlertStatus"),
        ("DELL-MM-MIB-SMIv2", "dmmDeviceServiceTag"),
        ("DELL-MM-MIB-SMIv2", "dmmCategoryName"),
        ("DELL-MM-MIB-SMIv2", "dmmSubCategoryName"),
        ("DELL-MM-MIB-SMIv2", "dmmSeverity"))
)
if mibBuilder.loadTexts:
    iDRAC2249alertLinkStatusFailure.setStatus(
        "current"
    )

iDRAC2250alertLinkStatusWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 7, 0, 2250)
)
iDRAC2250alertLinkStatusWarning.setObjects(
      *(("DELL-MM-MIB-SMIv2", "dmmCA2MessageID"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2Message"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2MessageArgs"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2AlertStatus"),
        ("DELL-MM-MIB-SMIv2", "dmmDeviceServiceTag"),
        ("DELL-MM-MIB-SMIv2", "dmmCategoryName"),
        ("DELL-MM-MIB-SMIv2", "dmmSubCategoryName"),
        ("DELL-MM-MIB-SMIv2", "dmmSeverity"))
)
if mibBuilder.loadTexts:
    iDRAC2250alertLinkStatusWarning.setStatus(
        "current"
    )

iDRAC2251alertLinkStatusInformation = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 7, 0, 2251)
)
iDRAC2251alertLinkStatusInformation.setObjects(
      *(("DELL-MM-MIB-SMIv2", "dmmCA2MessageID"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2Message"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2MessageArgs"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2AlertStatus"),
        ("DELL-MM-MIB-SMIv2", "dmmDeviceServiceTag"),
        ("DELL-MM-MIB-SMIv2", "dmmCategoryName"),
        ("DELL-MM-MIB-SMIv2", "dmmSubCategoryName"),
        ("DELL-MM-MIB-SMIv2", "dmmSeverity"))
)
if mibBuilder.loadTexts:
    iDRAC2251alertLinkStatusInformation.setStatus(
        "current"
    )

iDRAC2265alertMemoryDeviceFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 7, 0, 2265)
)
iDRAC2265alertMemoryDeviceFailure.setObjects(
      *(("DELL-MM-MIB-SMIv2", "dmmCA2MessageID"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2Message"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2MessageArgs"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2AlertStatus"),
        ("DELL-MM-MIB-SMIv2", "dmmDeviceServiceTag"),
        ("DELL-MM-MIB-SMIv2", "dmmCategoryName"),
        ("DELL-MM-MIB-SMIv2", "dmmSubCategoryName"),
        ("DELL-MM-MIB-SMIv2", "dmmSeverity"))
)
if mibBuilder.loadTexts:
    iDRAC2265alertMemoryDeviceFailure.setStatus(
        "current"
    )

iDRAC2266alertMemoryDeviceWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 7, 0, 2266)
)
iDRAC2266alertMemoryDeviceWarning.setObjects(
      *(("DELL-MM-MIB-SMIv2", "dmmCA2MessageID"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2Message"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2MessageArgs"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2AlertStatus"),
        ("DELL-MM-MIB-SMIv2", "dmmDeviceServiceTag"),
        ("DELL-MM-MIB-SMIv2", "dmmCategoryName"),
        ("DELL-MM-MIB-SMIv2", "dmmSubCategoryName"),
        ("DELL-MM-MIB-SMIv2", "dmmSeverity"))
)
if mibBuilder.loadTexts:
    iDRAC2266alertMemoryDeviceWarning.setStatus(
        "current"
    )

iDRAC2267alertMemoryDeviceInformation = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 7, 0, 2267)
)
iDRAC2267alertMemoryDeviceInformation.setObjects(
      *(("DELL-MM-MIB-SMIv2", "dmmCA2MessageID"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2Message"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2MessageArgs"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2AlertStatus"),
        ("DELL-MM-MIB-SMIv2", "dmmDeviceServiceTag"),
        ("DELL-MM-MIB-SMIv2", "dmmCategoryName"),
        ("DELL-MM-MIB-SMIv2", "dmmSubCategoryName"),
        ("DELL-MM-MIB-SMIv2", "dmmSeverity"))
)
if mibBuilder.loadTexts:
    iDRAC2267alertMemoryDeviceInformation.setStatus(
        "current"
    )

iDRAC2273alertPowerUsageFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 7, 0, 2273)
)
iDRAC2273alertPowerUsageFailure.setObjects(
      *(("DELL-MM-MIB-SMIv2", "dmmCA2MessageID"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2Message"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2MessageArgs"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2AlertStatus"),
        ("DELL-MM-MIB-SMIv2", "dmmDeviceServiceTag"),
        ("DELL-MM-MIB-SMIv2", "dmmCategoryName"),
        ("DELL-MM-MIB-SMIv2", "dmmSubCategoryName"),
        ("DELL-MM-MIB-SMIv2", "dmmSeverity"))
)
if mibBuilder.loadTexts:
    iDRAC2273alertPowerUsageFailure.setStatus(
        "current"
    )

iDRAC2274alertPowerUsageWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 7, 0, 2274)
)
iDRAC2274alertPowerUsageWarning.setObjects(
      *(("DELL-MM-MIB-SMIv2", "dmmCA2MessageID"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2Message"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2MessageArgs"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2AlertStatus"),
        ("DELL-MM-MIB-SMIv2", "dmmDeviceServiceTag"),
        ("DELL-MM-MIB-SMIv2", "dmmCategoryName"),
        ("DELL-MM-MIB-SMIv2", "dmmSubCategoryName"),
        ("DELL-MM-MIB-SMIv2", "dmmSeverity"))
)
if mibBuilder.loadTexts:
    iDRAC2274alertPowerUsageWarning.setStatus(
        "current"
    )

iDRAC2275alertPowerUsageInformation = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 7, 0, 2275)
)
iDRAC2275alertPowerUsageInformation.setObjects(
      *(("DELL-MM-MIB-SMIv2", "dmmCA2MessageID"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2Message"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2MessageArgs"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2AlertStatus"),
        ("DELL-MM-MIB-SMIv2", "dmmDeviceServiceTag"),
        ("DELL-MM-MIB-SMIv2", "dmmCategoryName"),
        ("DELL-MM-MIB-SMIv2", "dmmSubCategoryName"),
        ("DELL-MM-MIB-SMIv2", "dmmSeverity"))
)
if mibBuilder.loadTexts:
    iDRAC2275alertPowerUsageInformation.setStatus(
        "current"
    )

iDRAC2297alertPhysicalDiskFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 7, 0, 2297)
)
iDRAC2297alertPhysicalDiskFailure.setObjects(
      *(("DELL-MM-MIB-SMIv2", "dmmCA2MessageID"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2Message"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2MessageArgs"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2AlertStatus"),
        ("DELL-MM-MIB-SMIv2", "dmmDeviceServiceTag"),
        ("DELL-MM-MIB-SMIv2", "dmmCategoryName"),
        ("DELL-MM-MIB-SMIv2", "dmmSubCategoryName"),
        ("DELL-MM-MIB-SMIv2", "dmmSeverity"))
)
if mibBuilder.loadTexts:
    iDRAC2297alertPhysicalDiskFailure.setStatus(
        "current"
    )

iDRAC2298alertPhysicalDiskWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 7, 0, 2298)
)
iDRAC2298alertPhysicalDiskWarning.setObjects(
      *(("DELL-MM-MIB-SMIv2", "dmmCA2MessageID"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2Message"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2MessageArgs"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2AlertStatus"),
        ("DELL-MM-MIB-SMIv2", "dmmDeviceServiceTag"),
        ("DELL-MM-MIB-SMIv2", "dmmCategoryName"),
        ("DELL-MM-MIB-SMIv2", "dmmSubCategoryName"),
        ("DELL-MM-MIB-SMIv2", "dmmSeverity"))
)
if mibBuilder.loadTexts:
    iDRAC2298alertPhysicalDiskWarning.setStatus(
        "current"
    )

iDRAC2299alertPhysicalDiskInformation = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 7, 0, 2299)
)
iDRAC2299alertPhysicalDiskInformation.setObjects(
      *(("DELL-MM-MIB-SMIv2", "dmmCA2MessageID"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2Message"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2MessageArgs"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2AlertStatus"),
        ("DELL-MM-MIB-SMIv2", "dmmDeviceServiceTag"),
        ("DELL-MM-MIB-SMIv2", "dmmCategoryName"),
        ("DELL-MM-MIB-SMIv2", "dmmSubCategoryName"),
        ("DELL-MM-MIB-SMIv2", "dmmSeverity"))
)
if mibBuilder.loadTexts:
    iDRAC2299alertPhysicalDiskInformation.setStatus(
        "current"
    )

iDRAC2329alertHardwareConfigurationFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 7, 0, 2329)
)
iDRAC2329alertHardwareConfigurationFailure.setObjects(
      *(("DELL-MM-MIB-SMIv2", "dmmCA2MessageID"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2Message"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2MessageArgs"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2AlertStatus"),
        ("DELL-MM-MIB-SMIv2", "dmmDeviceServiceTag"),
        ("DELL-MM-MIB-SMIv2", "dmmCategoryName"),
        ("DELL-MM-MIB-SMIv2", "dmmSubCategoryName"),
        ("DELL-MM-MIB-SMIv2", "dmmSeverity"))
)
if mibBuilder.loadTexts:
    iDRAC2329alertHardwareConfigurationFailure.setStatus(
        "current"
    )

iDRAC2330alertHardwareConfigurationWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 7, 0, 2330)
)
iDRAC2330alertHardwareConfigurationWarning.setObjects(
      *(("DELL-MM-MIB-SMIv2", "dmmCA2MessageID"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2Message"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2MessageArgs"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2AlertStatus"),
        ("DELL-MM-MIB-SMIv2", "dmmDeviceServiceTag"),
        ("DELL-MM-MIB-SMIv2", "dmmCategoryName"),
        ("DELL-MM-MIB-SMIv2", "dmmSubCategoryName"),
        ("DELL-MM-MIB-SMIv2", "dmmSeverity"))
)
if mibBuilder.loadTexts:
    iDRAC2330alertHardwareConfigurationWarning.setStatus(
        "current"
    )

iDRAC2331alertHardwareConfigurationInformation = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 7, 0, 2331)
)
iDRAC2331alertHardwareConfigurationInformation.setObjects(
      *(("DELL-MM-MIB-SMIv2", "dmmCA2MessageID"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2Message"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2MessageArgs"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2AlertStatus"),
        ("DELL-MM-MIB-SMIv2", "dmmDeviceServiceTag"),
        ("DELL-MM-MIB-SMIv2", "dmmCategoryName"),
        ("DELL-MM-MIB-SMIv2", "dmmSubCategoryName"),
        ("DELL-MM-MIB-SMIv2", "dmmSeverity"))
)
if mibBuilder.loadTexts:
    iDRAC2331alertHardwareConfigurationInformation.setStatus(
        "current"
    )

iDRAC2337alertSoftwareConfigurationFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 7, 0, 2337)
)
iDRAC2337alertSoftwareConfigurationFailure.setObjects(
      *(("DELL-MM-MIB-SMIv2", "dmmCA2MessageID"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2Message"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2MessageArgs"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2AlertStatus"),
        ("DELL-MM-MIB-SMIv2", "dmmDeviceServiceTag"),
        ("DELL-MM-MIB-SMIv2", "dmmCategoryName"),
        ("DELL-MM-MIB-SMIv2", "dmmSubCategoryName"),
        ("DELL-MM-MIB-SMIv2", "dmmSeverity"))
)
if mibBuilder.loadTexts:
    iDRAC2337alertSoftwareConfigurationFailure.setStatus(
        "current"
    )

iDRAC2338alertSoftwareConfigurationWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 7, 0, 2338)
)
iDRAC2338alertSoftwareConfigurationWarning.setObjects(
      *(("DELL-MM-MIB-SMIv2", "dmmCA2MessageID"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2Message"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2MessageArgs"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2AlertStatus"),
        ("DELL-MM-MIB-SMIv2", "dmmDeviceServiceTag"),
        ("DELL-MM-MIB-SMIv2", "dmmCategoryName"),
        ("DELL-MM-MIB-SMIv2", "dmmSubCategoryName"),
        ("DELL-MM-MIB-SMIv2", "dmmSeverity"))
)
if mibBuilder.loadTexts:
    iDRAC2338alertSoftwareConfigurationWarning.setStatus(
        "current"
    )

iDRAC2339alertSoftwareConfigurationInformation = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 7, 0, 2339)
)
iDRAC2339alertSoftwareConfigurationInformation.setObjects(
      *(("DELL-MM-MIB-SMIv2", "dmmCA2MessageID"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2Message"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2MessageArgs"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2AlertStatus"),
        ("DELL-MM-MIB-SMIv2", "dmmDeviceServiceTag"),
        ("DELL-MM-MIB-SMIv2", "dmmCategoryName"),
        ("DELL-MM-MIB-SMIv2", "dmmSubCategoryName"),
        ("DELL-MM-MIB-SMIv2", "dmmSeverity"))
)
if mibBuilder.loadTexts:
    iDRAC2339alertSoftwareConfigurationInformation.setStatus(
        "current"
    )

iDRAC2377alertSystemEventLogFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 7, 0, 2377)
)
iDRAC2377alertSystemEventLogFailure.setObjects(
      *(("DELL-MM-MIB-SMIv2", "dmmCA2MessageID"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2Message"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2MessageArgs"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2AlertStatus"),
        ("DELL-MM-MIB-SMIv2", "dmmDeviceServiceTag"),
        ("DELL-MM-MIB-SMIv2", "dmmCategoryName"),
        ("DELL-MM-MIB-SMIv2", "dmmSubCategoryName"),
        ("DELL-MM-MIB-SMIv2", "dmmSeverity"))
)
if mibBuilder.loadTexts:
    iDRAC2377alertSystemEventLogFailure.setStatus(
        "current"
    )

iDRAC2378alertSystemEventLogWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 7, 0, 2378)
)
iDRAC2378alertSystemEventLogWarning.setObjects(
      *(("DELL-MM-MIB-SMIv2", "dmmCA2MessageID"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2Message"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2MessageArgs"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2AlertStatus"),
        ("DELL-MM-MIB-SMIv2", "dmmDeviceServiceTag"),
        ("DELL-MM-MIB-SMIv2", "dmmCategoryName"),
        ("DELL-MM-MIB-SMIv2", "dmmSubCategoryName"),
        ("DELL-MM-MIB-SMIv2", "dmmSeverity"))
)
if mibBuilder.loadTexts:
    iDRAC2378alertSystemEventLogWarning.setStatus(
        "current"
    )

iDRAC2379alertSystemEventLogInformation = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 7, 0, 2379)
)
iDRAC2379alertSystemEventLogInformation.setObjects(
      *(("DELL-MM-MIB-SMIv2", "dmmCA2MessageID"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2Message"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2MessageArgs"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2AlertStatus"),
        ("DELL-MM-MIB-SMIv2", "dmmDeviceServiceTag"),
        ("DELL-MM-MIB-SMIv2", "dmmCategoryName"),
        ("DELL-MM-MIB-SMIv2", "dmmSubCategoryName"),
        ("DELL-MM-MIB-SMIv2", "dmmSeverity"))
)
if mibBuilder.loadTexts:
    iDRAC2379alertSystemEventLogInformation.setStatus(
        "current"
    )

iDRAC2385alertSecurityFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 7, 0, 2385)
)
iDRAC2385alertSecurityFailure.setObjects(
      *(("DELL-MM-MIB-SMIv2", "dmmCA2MessageID"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2Message"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2MessageArgs"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2AlertStatus"),
        ("DELL-MM-MIB-SMIv2", "dmmDeviceServiceTag"),
        ("DELL-MM-MIB-SMIv2", "dmmCategoryName"),
        ("DELL-MM-MIB-SMIv2", "dmmSubCategoryName"),
        ("DELL-MM-MIB-SMIv2", "dmmSeverity"))
)
if mibBuilder.loadTexts:
    iDRAC2385alertSecurityFailure.setStatus(
        "current"
    )

iDRAC2386alertSecurityWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 7, 0, 2386)
)
iDRAC2386alertSecurityWarning.setObjects(
      *(("DELL-MM-MIB-SMIv2", "dmmCA2MessageID"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2Message"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2MessageArgs"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2AlertStatus"),
        ("DELL-MM-MIB-SMIv2", "dmmDeviceServiceTag"),
        ("DELL-MM-MIB-SMIv2", "dmmCategoryName"),
        ("DELL-MM-MIB-SMIv2", "dmmSubCategoryName"),
        ("DELL-MM-MIB-SMIv2", "dmmSeverity"))
)
if mibBuilder.loadTexts:
    iDRAC2386alertSecurityWarning.setStatus(
        "current"
    )

iDRAC2387alertSecurityInformation = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 7, 0, 2387)
)
iDRAC2387alertSecurityInformation.setObjects(
      *(("DELL-MM-MIB-SMIv2", "dmmCA2MessageID"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2Message"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2MessageArgs"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2AlertStatus"),
        ("DELL-MM-MIB-SMIv2", "dmmDeviceServiceTag"),
        ("DELL-MM-MIB-SMIv2", "dmmCategoryName"),
        ("DELL-MM-MIB-SMIv2", "dmmSubCategoryName"),
        ("DELL-MM-MIB-SMIv2", "dmmSeverity"))
)
if mibBuilder.loadTexts:
    iDRAC2387alertSecurityInformation.setStatus(
        "current"
    )

iDRAC2393alertCableFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 7, 0, 2393)
)
iDRAC2393alertCableFailure.setObjects(
      *(("DELL-MM-MIB-SMIv2", "dmmCA2MessageID"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2Message"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2MessageArgs"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2AlertStatus"),
        ("DELL-MM-MIB-SMIv2", "dmmDeviceServiceTag"),
        ("DELL-MM-MIB-SMIv2", "dmmCategoryName"),
        ("DELL-MM-MIB-SMIv2", "dmmSubCategoryName"),
        ("DELL-MM-MIB-SMIv2", "dmmSeverity"))
)
if mibBuilder.loadTexts:
    iDRAC2393alertCableFailure.setStatus(
        "current"
    )

iDRAC2409alertOSFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 7, 0, 2409)
)
iDRAC2409alertOSFailure.setObjects(
      *(("DELL-MM-MIB-SMIv2", "dmmCA2MessageID"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2Message"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2MessageArgs"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2AlertStatus"),
        ("DELL-MM-MIB-SMIv2", "dmmDeviceServiceTag"),
        ("DELL-MM-MIB-SMIv2", "dmmCategoryName"),
        ("DELL-MM-MIB-SMIv2", "dmmSubCategoryName"),
        ("DELL-MM-MIB-SMIv2", "dmmSeverity"))
)
if mibBuilder.loadTexts:
    iDRAC2409alertOSFailure.setStatus(
        "current"
    )

iDRAC2411alertOSInformation = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 7, 0, 2411)
)
iDRAC2411alertOSInformation.setObjects(
      *(("DELL-MM-MIB-SMIv2", "dmmCA2MessageID"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2Message"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2MessageArgs"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2AlertStatus"),
        ("DELL-MM-MIB-SMIv2", "dmmDeviceServiceTag"),
        ("DELL-MM-MIB-SMIv2", "dmmCategoryName"),
        ("DELL-MM-MIB-SMIv2", "dmmSubCategoryName"),
        ("DELL-MM-MIB-SMIv2", "dmmSeverity"))
)
if mibBuilder.loadTexts:
    iDRAC2411alertOSInformation.setStatus(
        "current"
    )

iDRAC2417alertPCIDeviceFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 7, 0, 2417)
)
iDRAC2417alertPCIDeviceFailure.setObjects(
      *(("DELL-MM-MIB-SMIv2", "dmmCA2MessageID"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2Message"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2MessageArgs"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2AlertStatus"),
        ("DELL-MM-MIB-SMIv2", "dmmDeviceServiceTag"),
        ("DELL-MM-MIB-SMIv2", "dmmCategoryName"),
        ("DELL-MM-MIB-SMIv2", "dmmSubCategoryName"),
        ("DELL-MM-MIB-SMIv2", "dmmSeverity"))
)
if mibBuilder.loadTexts:
    iDRAC2417alertPCIDeviceFailure.setStatus(
        "current"
    )

iDRAC2418alertPCIDeviceWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 7, 0, 2418)
)
iDRAC2418alertPCIDeviceWarning.setObjects(
      *(("DELL-MM-MIB-SMIv2", "dmmCA2MessageID"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2Message"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2MessageArgs"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2AlertStatus"),
        ("DELL-MM-MIB-SMIv2", "dmmDeviceServiceTag"),
        ("DELL-MM-MIB-SMIv2", "dmmCategoryName"),
        ("DELL-MM-MIB-SMIv2", "dmmSubCategoryName"),
        ("DELL-MM-MIB-SMIv2", "dmmSeverity"))
)
if mibBuilder.loadTexts:
    iDRAC2418alertPCIDeviceWarning.setStatus(
        "current"
    )

iDRAC2419alertPCIDeviceInformation = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 7, 0, 2419)
)
iDRAC2419alertPCIDeviceInformation.setObjects(
      *(("DELL-MM-MIB-SMIv2", "dmmCA2MessageID"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2Message"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2MessageArgs"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2AlertStatus"),
        ("DELL-MM-MIB-SMIv2", "dmmDeviceServiceTag"),
        ("DELL-MM-MIB-SMIv2", "dmmCategoryName"),
        ("DELL-MM-MIB-SMIv2", "dmmSubCategoryName"),
        ("DELL-MM-MIB-SMIv2", "dmmSeverity"))
)
if mibBuilder.loadTexts:
    iDRAC2419alertPCIDeviceInformation.setStatus(
        "current"
    )

iDRAC2425alertBiosPostFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 7, 0, 2425)
)
iDRAC2425alertBiosPostFailure.setObjects(
      *(("DELL-MM-MIB-SMIv2", "dmmCA2MessageID"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2Message"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2MessageArgs"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2AlertStatus"),
        ("DELL-MM-MIB-SMIv2", "dmmDeviceServiceTag"),
        ("DELL-MM-MIB-SMIv2", "dmmCategoryName"),
        ("DELL-MM-MIB-SMIv2", "dmmSubCategoryName"),
        ("DELL-MM-MIB-SMIv2", "dmmSeverity"))
)
if mibBuilder.loadTexts:
    iDRAC2425alertBiosPostFailure.setStatus(
        "current"
    )

iDRAC2433alertInternaliDRACMemoryUnresponsive = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 7, 0, 2433)
)
iDRAC2433alertInternaliDRACMemoryUnresponsive.setObjects(
      *(("DELL-MM-MIB-SMIv2", "dmmCA2MessageID"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2Message"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2MessageArgs"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2AlertStatus"),
        ("DELL-MM-MIB-SMIv2", "dmmDeviceServiceTag"),
        ("DELL-MM-MIB-SMIv2", "dmmCategoryName"),
        ("DELL-MM-MIB-SMIv2", "dmmSubCategoryName"),
        ("DELL-MM-MIB-SMIv2", "dmmSeverity"))
)
if mibBuilder.loadTexts:
    iDRAC2433alertInternaliDRACMemoryUnresponsive.setStatus(
        "current"
    )

iDRAC2435alertServerIdleTime = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 7, 0, 2435)
)
iDRAC2435alertServerIdleTime.setObjects(
      *(("DELL-MM-MIB-SMIv2", "dmmCA2MessageID"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2Message"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2MessageArgs"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2AlertStatus"),
        ("DELL-MM-MIB-SMIv2", "dmmDeviceServiceTag"),
        ("DELL-MM-MIB-SMIv2", "dmmCategoryName"),
        ("DELL-MM-MIB-SMIv2", "dmmSubCategoryName"),
        ("DELL-MM-MIB-SMIv2", "dmmSeverity"))
)
if mibBuilder.loadTexts:
    iDRAC2435alertServerIdleTime.setStatus(
        "current"
    )

iDRAC2457alertProcessorDeviceAbsent = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 7, 0, 2457)
)
iDRAC2457alertProcessorDeviceAbsent.setObjects(
      *(("DELL-MM-MIB-SMIv2", "dmmCA2MessageID"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2Message"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2MessageArgs"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2AlertStatus"),
        ("DELL-MM-MIB-SMIv2", "dmmDeviceServiceTag"),
        ("DELL-MM-MIB-SMIv2", "dmmCategoryName"),
        ("DELL-MM-MIB-SMIv2", "dmmSubCategoryName"),
        ("DELL-MM-MIB-SMIv2", "dmmSeverity"))
)
if mibBuilder.loadTexts:
    iDRAC2457alertProcessorDeviceAbsent.setStatus(
        "current"
    )

iDRAC2465alertPowerSupplyAbsent = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 7, 0, 2465)
)
iDRAC2465alertPowerSupplyAbsent.setObjects(
      *(("DELL-MM-MIB-SMIv2", "dmmCA2MessageID"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2Message"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2MessageArgs"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2AlertStatus"),
        ("DELL-MM-MIB-SMIv2", "dmmDeviceServiceTag"),
        ("DELL-MM-MIB-SMIv2", "dmmCategoryName"),
        ("DELL-MM-MIB-SMIv2", "dmmSubCategoryName"),
        ("DELL-MM-MIB-SMIv2", "dmmSeverity"))
)
if mibBuilder.loadTexts:
    iDRAC2465alertPowerSupplyAbsent.setStatus(
        "current"
    )

iDRAC2473alertRedundancyLost = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 7, 0, 2473)
)
iDRAC2473alertRedundancyLost.setObjects(
      *(("DELL-MM-MIB-SMIv2", "dmmCA2MessageID"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2Message"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2MessageArgs"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2AlertStatus"),
        ("DELL-MM-MIB-SMIv2", "dmmDeviceServiceTag"),
        ("DELL-MM-MIB-SMIv2", "dmmCategoryName"),
        ("DELL-MM-MIB-SMIv2", "dmmSubCategoryName"),
        ("DELL-MM-MIB-SMIv2", "dmmSeverity"))
)
if mibBuilder.loadTexts:
    iDRAC2473alertRedundancyLost.setStatus(
        "current"
    )

iDRAC2474alertRedundancyDegraded = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 7, 0, 2474)
)
iDRAC2474alertRedundancyDegraded.setObjects(
      *(("DELL-MM-MIB-SMIv2", "dmmCA2MessageID"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2Message"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2MessageArgs"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2AlertStatus"),
        ("DELL-MM-MIB-SMIv2", "dmmDeviceServiceTag"),
        ("DELL-MM-MIB-SMIv2", "dmmCategoryName"),
        ("DELL-MM-MIB-SMIv2", "dmmSubCategoryName"),
        ("DELL-MM-MIB-SMIv2", "dmmSeverity"))
)
if mibBuilder.loadTexts:
    iDRAC2474alertRedundancyDegraded.setStatus(
        "current"
    )

iDRAC2475alertRedundancyInformation = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 7, 0, 2475)
)
iDRAC2475alertRedundancyInformation.setObjects(
      *(("DELL-MM-MIB-SMIv2", "dmmCA2MessageID"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2Message"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2MessageArgs"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2AlertStatus"),
        ("DELL-MM-MIB-SMIv2", "dmmDeviceServiceTag"),
        ("DELL-MM-MIB-SMIv2", "dmmCategoryName"),
        ("DELL-MM-MIB-SMIv2", "dmmSubCategoryName"),
        ("DELL-MM-MIB-SMIv2", "dmmSeverity"))
)
if mibBuilder.loadTexts:
    iDRAC2475alertRedundancyInformation.setStatus(
        "current"
    )

iDRAC2481alertIntegratedDualSDModuleAbsent = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 7, 0, 2481)
)
iDRAC2481alertIntegratedDualSDModuleAbsent.setObjects(
      *(("DELL-MM-MIB-SMIv2", "dmmCA2MessageID"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2Message"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2MessageArgs"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2AlertStatus"),
        ("DELL-MM-MIB-SMIv2", "dmmDeviceServiceTag"),
        ("DELL-MM-MIB-SMIv2", "dmmCategoryName"),
        ("DELL-MM-MIB-SMIv2", "dmmSubCategoryName"),
        ("DELL-MM-MIB-SMIv2", "dmmSeverity"))
)
if mibBuilder.loadTexts:
    iDRAC2481alertIntegratedDualSDModuleAbsent.setStatus(
        "current"
    )

iDRAC2489alertIntegratedDualSDModuleRedundancyLost = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 7, 0, 2489)
)
iDRAC2489alertIntegratedDualSDModuleRedundancyLost.setObjects(
      *(("DELL-MM-MIB-SMIv2", "dmmCA2MessageID"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2Message"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2MessageArgs"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2AlertStatus"),
        ("DELL-MM-MIB-SMIv2", "dmmDeviceServiceTag"),
        ("DELL-MM-MIB-SMIv2", "dmmCategoryName"),
        ("DELL-MM-MIB-SMIv2", "dmmSubCategoryName"),
        ("DELL-MM-MIB-SMIv2", "dmmSeverity"))
)
if mibBuilder.loadTexts:
    iDRAC2489alertIntegratedDualSDModuleRedundancyLost.setStatus(
        "current"
    )

iDRAC2490alertIntegratedDualSDModuleRedundancyDegraded = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 7, 0, 2490)
)
iDRAC2490alertIntegratedDualSDModuleRedundancyDegraded.setObjects(
      *(("DELL-MM-MIB-SMIv2", "dmmCA2MessageID"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2Message"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2MessageArgs"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2AlertStatus"),
        ("DELL-MM-MIB-SMIv2", "dmmDeviceServiceTag"),
        ("DELL-MM-MIB-SMIv2", "dmmCategoryName"),
        ("DELL-MM-MIB-SMIv2", "dmmSubCategoryName"),
        ("DELL-MM-MIB-SMIv2", "dmmSeverity"))
)
if mibBuilder.loadTexts:
    iDRAC2490alertIntegratedDualSDModuleRedundancyDegraded.setStatus(
        "current"
    )

iDRAC2491alertIntegratedDualSDModuleRedundancyInformation = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 7, 0, 2491)
)
iDRAC2491alertIntegratedDualSDModuleRedundancyInformation.setObjects(
      *(("DELL-MM-MIB-SMIv2", "dmmCA2MessageID"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2Message"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2MessageArgs"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2AlertStatus"),
        ("DELL-MM-MIB-SMIv2", "dmmDeviceServiceTag"),
        ("DELL-MM-MIB-SMIv2", "dmmCategoryName"),
        ("DELL-MM-MIB-SMIv2", "dmmSubCategoryName"),
        ("DELL-MM-MIB-SMIv2", "dmmSeverity"))
)
if mibBuilder.loadTexts:
    iDRAC2491alertIntegratedDualSDModuleRedundancyInformation.setStatus(
        "current"
    )

iDRAC2505alertvFlashMediaDeviceFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 7, 0, 2505)
)
iDRAC2505alertvFlashMediaDeviceFailure.setObjects(
      *(("DELL-MM-MIB-SMIv2", "dmmCA2MessageID"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2Message"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2MessageArgs"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2AlertStatus"),
        ("DELL-MM-MIB-SMIv2", "dmmDeviceServiceTag"),
        ("DELL-MM-MIB-SMIv2", "dmmCategoryName"),
        ("DELL-MM-MIB-SMIv2", "dmmSubCategoryName"),
        ("DELL-MM-MIB-SMIv2", "dmmSeverity"))
)
if mibBuilder.loadTexts:
    iDRAC2505alertvFlashMediaDeviceFailure.setStatus(
        "current"
    )

iDRAC2506alertvFlashMediaDeviceWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 7, 0, 2506)
)
iDRAC2506alertvFlashMediaDeviceWarning.setObjects(
      *(("DELL-MM-MIB-SMIv2", "dmmCA2MessageID"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2Message"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2MessageArgs"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2AlertStatus"),
        ("DELL-MM-MIB-SMIv2", "dmmDeviceServiceTag"),
        ("DELL-MM-MIB-SMIv2", "dmmCategoryName"),
        ("DELL-MM-MIB-SMIv2", "dmmSubCategoryName"),
        ("DELL-MM-MIB-SMIv2", "dmmSeverity"))
)
if mibBuilder.loadTexts:
    iDRAC2506alertvFlashMediaDeviceWarning.setStatus(
        "current"
    )

iDRAC2507alertvFlashMediaDeviceInformation = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 7, 0, 2507)
)
iDRAC2507alertvFlashMediaDeviceInformation.setObjects(
      *(("DELL-MM-MIB-SMIv2", "dmmCA2MessageID"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2Message"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2MessageArgs"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2AlertStatus"),
        ("DELL-MM-MIB-SMIv2", "dmmDeviceServiceTag"),
        ("DELL-MM-MIB-SMIv2", "dmmCategoryName"),
        ("DELL-MM-MIB-SMIv2", "dmmSubCategoryName"),
        ("DELL-MM-MIB-SMIv2", "dmmSeverity"))
)
if mibBuilder.loadTexts:
    iDRAC2507alertvFlashMediaDeviceInformation.setStatus(
        "current"
    )

iDRAC2515alertvFlashMediaDeviceAbsent = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 7, 0, 2515)
)
iDRAC2515alertvFlashMediaDeviceAbsent.setObjects(
      *(("DELL-MM-MIB-SMIv2", "dmmCA2MessageID"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2Message"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2MessageArgs"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2AlertStatus"),
        ("DELL-MM-MIB-SMIv2", "dmmDeviceServiceTag"),
        ("DELL-MM-MIB-SMIv2", "dmmCategoryName"),
        ("DELL-MM-MIB-SMIv2", "dmmSubCategoryName"),
        ("DELL-MM-MIB-SMIv2", "dmmSeverity"))
)
if mibBuilder.loadTexts:
    iDRAC2515alertvFlashMediaDeviceAbsent.setStatus(
        "current"
    )

iDRAC2521alertTemperatureStatisticsFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 7, 0, 2521)
)
iDRAC2521alertTemperatureStatisticsFailure.setObjects(
      *(("DELL-MM-MIB-SMIv2", "dmmCA2MessageID"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2Message"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2MessageArgs"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2AlertStatus"),
        ("DELL-MM-MIB-SMIv2", "dmmDeviceServiceTag"),
        ("DELL-MM-MIB-SMIv2", "dmmCategoryName"),
        ("DELL-MM-MIB-SMIv2", "dmmSubCategoryName"),
        ("DELL-MM-MIB-SMIv2", "dmmSeverity"))
)
if mibBuilder.loadTexts:
    iDRAC2521alertTemperatureStatisticsFailure.setStatus(
        "current"
    )

iDRAC2522alertTemperatureStatisticsWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 7, 0, 2522)
)
iDRAC2522alertTemperatureStatisticsWarning.setObjects(
      *(("DELL-MM-MIB-SMIv2", "dmmCA2MessageID"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2Message"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2MessageArgs"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2AlertStatus"),
        ("DELL-MM-MIB-SMIv2", "dmmDeviceServiceTag"),
        ("DELL-MM-MIB-SMIv2", "dmmCategoryName"),
        ("DELL-MM-MIB-SMIv2", "dmmSubCategoryName"),
        ("DELL-MM-MIB-SMIv2", "dmmSeverity"))
)
if mibBuilder.loadTexts:
    iDRAC2522alertTemperatureStatisticsWarning.setStatus(
        "current"
    )

iDRAC2531alertRACInformation = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 7, 0, 2531)
)
iDRAC2531alertRACInformation.setObjects(
      *(("DELL-MM-MIB-SMIv2", "dmmCA2MessageID"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2Message"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2MessageArgs"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2AlertStatus"),
        ("DELL-MM-MIB-SMIv2", "dmmDeviceServiceTag"),
        ("DELL-MM-MIB-SMIv2", "dmmCategoryName"),
        ("DELL-MM-MIB-SMIv2", "dmmSubCategoryName"),
        ("DELL-MM-MIB-SMIv2", "dmmSeverity"))
)
if mibBuilder.loadTexts:
    iDRAC2531alertRACInformation.setStatus(
        "current"
    )

iDRAC2537alertFiberChannelFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 7, 0, 2537)
)
iDRAC2537alertFiberChannelFailure.setObjects(
      *(("DELL-MM-MIB-SMIv2", "dmmCA2MessageID"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2Message"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2MessageArgs"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2AlertStatus"),
        ("DELL-MM-MIB-SMIv2", "dmmDeviceServiceTag"),
        ("DELL-MM-MIB-SMIv2", "dmmCategoryName"),
        ("DELL-MM-MIB-SMIv2", "dmmSubCategoryName"),
        ("DELL-MM-MIB-SMIv2", "dmmSeverity"))
)
if mibBuilder.loadTexts:
    iDRAC2537alertFiberChannelFailure.setStatus(
        "current"
    )

iDRAC2538alertFiberChannelWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 7, 0, 2538)
)
iDRAC2538alertFiberChannelWarning.setObjects(
      *(("DELL-MM-MIB-SMIv2", "dmmCA2MessageID"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2Message"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2MessageArgs"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2AlertStatus"),
        ("DELL-MM-MIB-SMIv2", "dmmDeviceServiceTag"),
        ("DELL-MM-MIB-SMIv2", "dmmCategoryName"),
        ("DELL-MM-MIB-SMIv2", "dmmSubCategoryName"),
        ("DELL-MM-MIB-SMIv2", "dmmSeverity"))
)
if mibBuilder.loadTexts:
    iDRAC2538alertFiberChannelWarning.setStatus(
        "current"
    )

iDRAC2539alertFiberChannelInformation = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 7, 0, 2539)
)
iDRAC2539alertFiberChannelInformation.setObjects(
      *(("DELL-MM-MIB-SMIv2", "dmmCA2MessageID"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2Message"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2MessageArgs"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2AlertStatus"),
        ("DELL-MM-MIB-SMIv2", "dmmDeviceServiceTag"),
        ("DELL-MM-MIB-SMIv2", "dmmCategoryName"),
        ("DELL-MM-MIB-SMIv2", "dmmSubCategoryName"),
        ("DELL-MM-MIB-SMIv2", "dmmSeverity"))
)
if mibBuilder.loadTexts:
    iDRAC2539alertFiberChannelInformation.setStatus(
        "current"
    )

iDRAC2545alertCMCFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 7, 0, 2545)
)
iDRAC2545alertCMCFailure.setObjects(
      *(("DELL-MM-MIB-SMIv2", "dmmCA2MessageID"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2Message"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2MessageArgs"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2AlertStatus"),
        ("DELL-MM-MIB-SMIv2", "dmmDeviceServiceTag"),
        ("DELL-MM-MIB-SMIv2", "dmmCategoryName"),
        ("DELL-MM-MIB-SMIv2", "dmmSubCategoryName"),
        ("DELL-MM-MIB-SMIv2", "dmmSeverity"))
)
if mibBuilder.loadTexts:
    iDRAC2545alertCMCFailure.setStatus(
        "current"
    )

iDRAC2546alertCMCWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 7, 0, 2546)
)
iDRAC2546alertCMCWarning.setObjects(
      *(("DELL-MM-MIB-SMIv2", "dmmCA2MessageID"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2Message"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2MessageArgs"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2AlertStatus"),
        ("DELL-MM-MIB-SMIv2", "dmmDeviceServiceTag"),
        ("DELL-MM-MIB-SMIv2", "dmmCategoryName"),
        ("DELL-MM-MIB-SMIv2", "dmmSubCategoryName"),
        ("DELL-MM-MIB-SMIv2", "dmmSeverity"))
)
if mibBuilder.loadTexts:
    iDRAC2546alertCMCWarning.setStatus(
        "current"
    )

iDRAC2553alertIOVirtualizationFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 7, 0, 2553)
)
iDRAC2553alertIOVirtualizationFailure.setObjects(
      *(("DELL-MM-MIB-SMIv2", "dmmCA2MessageID"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2Message"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2MessageArgs"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2AlertStatus"),
        ("DELL-MM-MIB-SMIv2", "dmmDeviceServiceTag"),
        ("DELL-MM-MIB-SMIv2", "dmmCategoryName"),
        ("DELL-MM-MIB-SMIv2", "dmmSubCategoryName"),
        ("DELL-MM-MIB-SMIv2", "dmmSeverity"))
)
if mibBuilder.loadTexts:
    iDRAC2553alertIOVirtualizationFailure.setStatus(
        "current"
    )

iDRAC2650alertSystemPerformanceWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 7, 0, 2650)
)
iDRAC2650alertSystemPerformanceWarning.setObjects(
      *(("DELL-MM-MIB-SMIv2", "dmmCA2MessageID"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2Message"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2MessageArgs"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2AlertStatus"),
        ("DELL-MM-MIB-SMIv2", "dmmDeviceServiceTag"),
        ("DELL-MM-MIB-SMIv2", "dmmCategoryName"),
        ("DELL-MM-MIB-SMIv2", "dmmSubCategoryName"),
        ("DELL-MM-MIB-SMIv2", "dmmSeverity"))
)
if mibBuilder.loadTexts:
    iDRAC2650alertSystemPerformanceWarning.setStatus(
        "current"
    )

iDRAC3049alertLiquidCoolingLeakFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 7, 0, 3049)
)
iDRAC3049alertLiquidCoolingLeakFailure.setObjects(
      *(("DELL-MM-MIB-SMIv2", "dmmCA2MessageID"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2Message"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2MessageArgs"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2AlertStatus"),
        ("DELL-MM-MIB-SMIv2", "dmmDeviceServiceTag"),
        ("DELL-MM-MIB-SMIv2", "dmmCategoryName"),
        ("DELL-MM-MIB-SMIv2", "dmmSubCategoryName"),
        ("DELL-MM-MIB-SMIv2", "dmmSeverity"))
)
if mibBuilder.loadTexts:
    iDRAC3049alertLiquidCoolingLeakFailure.setStatus(
        "current"
    )

iDRAC3050alertLiquidCoolingLeakWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 7, 0, 3050)
)
iDRAC3050alertLiquidCoolingLeakWarning.setObjects(
      *(("DELL-MM-MIB-SMIv2", "dmmCA2MessageID"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2Message"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2MessageArgs"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2AlertStatus"),
        ("DELL-MM-MIB-SMIv2", "dmmDeviceServiceTag"),
        ("DELL-MM-MIB-SMIv2", "dmmCategoryName"),
        ("DELL-MM-MIB-SMIv2", "dmmSubCategoryName"),
        ("DELL-MM-MIB-SMIv2", "dmmSeverity"))
)
if mibBuilder.loadTexts:
    iDRAC3050alertLiquidCoolingLeakWarning.setStatus(
        "current"
    )

iDRAC3051alertLiquidCoolingLeakInformational = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 7, 0, 3051)
)
iDRAC3051alertLiquidCoolingLeakInformational.setObjects(
      *(("DELL-MM-MIB-SMIv2", "dmmCA2MessageID"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2Message"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2MessageArgs"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2AlertStatus"),
        ("DELL-MM-MIB-SMIv2", "dmmDeviceServiceTag"),
        ("DELL-MM-MIB-SMIv2", "dmmCategoryName"),
        ("DELL-MM-MIB-SMIv2", "dmmSubCategoryName"),
        ("DELL-MM-MIB-SMIv2", "dmmSeverity"))
)
if mibBuilder.loadTexts:
    iDRAC3051alertLiquidCoolingLeakInformational.setStatus(
        "current"
    )

iDRAC3082alertSDKSystemWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 7, 0, 3082)
)
iDRAC3082alertSDKSystemWarning.setObjects(
      *(("DELL-MM-MIB-SMIv2", "dmmCA2MessageID"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2Message"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2MessageArgs"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2AlertStatus"),
        ("DELL-MM-MIB-SMIv2", "dmmDeviceServiceTag"),
        ("DELL-MM-MIB-SMIv2", "dmmCategoryName"),
        ("DELL-MM-MIB-SMIv2", "dmmSubCategoryName"),
        ("DELL-MM-MIB-SMIv2", "dmmSeverity"))
)
if mibBuilder.loadTexts:
    iDRAC3082alertSDKSystemWarning.setStatus(
        "current"
    )

iDRAC3083alertSDKSystemInformational = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 7, 0, 3083)
)
iDRAC3083alertSDKSystemInformational.setObjects(
      *(("DELL-MM-MIB-SMIv2", "dmmCA2MessageID"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2Message"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2MessageArgs"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2AlertStatus"),
        ("DELL-MM-MIB-SMIv2", "dmmDeviceServiceTag"),
        ("DELL-MM-MIB-SMIv2", "dmmCategoryName"),
        ("DELL-MM-MIB-SMIv2", "dmmSubCategoryName"),
        ("DELL-MM-MIB-SMIv2", "dmmSeverity"))
)
if mibBuilder.loadTexts:
    iDRAC3083alertSDKSystemInformational.setStatus(
        "current"
    )

iDRAC4177alertStorageManagementFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 7, 0, 4177)
)
iDRAC4177alertStorageManagementFailure.setObjects(
      *(("DELL-MM-MIB-SMIv2", "dmmCA2MessageID"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2Message"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2MessageArgs"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2AlertStatus"),
        ("DELL-MM-MIB-SMIv2", "dmmDeviceServiceTag"),
        ("DELL-MM-MIB-SMIv2", "dmmCategoryName"),
        ("DELL-MM-MIB-SMIv2", "dmmSubCategoryName"),
        ("DELL-MM-MIB-SMIv2", "dmmSeverity"))
)
if mibBuilder.loadTexts:
    iDRAC4177alertStorageManagementFailure.setStatus(
        "current"
    )

iDRAC4178alertStorageManagementWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 7, 0, 4178)
)
iDRAC4178alertStorageManagementWarning.setObjects(
      *(("DELL-MM-MIB-SMIv2", "dmmCA2MessageID"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2Message"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2MessageArgs"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2AlertStatus"),
        ("DELL-MM-MIB-SMIv2", "dmmDeviceServiceTag"),
        ("DELL-MM-MIB-SMIv2", "dmmCategoryName"),
        ("DELL-MM-MIB-SMIv2", "dmmSubCategoryName"),
        ("DELL-MM-MIB-SMIv2", "dmmSeverity"))
)
if mibBuilder.loadTexts:
    iDRAC4178alertStorageManagementWarning.setStatus(
        "current"
    )

iDRAC4179alertStorageManagementInformation = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 7, 0, 4179)
)
iDRAC4179alertStorageManagementInformation.setObjects(
      *(("DELL-MM-MIB-SMIv2", "dmmCA2MessageID"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2Message"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2MessageArgs"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2AlertStatus"),
        ("DELL-MM-MIB-SMIv2", "dmmDeviceServiceTag"),
        ("DELL-MM-MIB-SMIv2", "dmmCategoryName"),
        ("DELL-MM-MIB-SMIv2", "dmmSubCategoryName"),
        ("DELL-MM-MIB-SMIv2", "dmmSeverity"))
)
if mibBuilder.loadTexts:
    iDRAC4179alertStorageManagementInformation.setStatus(
        "current"
    )

iDRAC4201alertStorageFanFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 7, 0, 4201)
)
iDRAC4201alertStorageFanFailure.setObjects(
      *(("DELL-MM-MIB-SMIv2", "dmmCA2MessageID"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2Message"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2MessageArgs"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2AlertStatus"),
        ("DELL-MM-MIB-SMIv2", "dmmDeviceServiceTag"),
        ("DELL-MM-MIB-SMIv2", "dmmCategoryName"),
        ("DELL-MM-MIB-SMIv2", "dmmSubCategoryName"),
        ("DELL-MM-MIB-SMIv2", "dmmSeverity"))
)
if mibBuilder.loadTexts:
    iDRAC4201alertStorageFanFailure.setStatus(
        "current"
    )

iDRAC4202alertStorageFanWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 7, 0, 4202)
)
iDRAC4202alertStorageFanWarning.setObjects(
      *(("DELL-MM-MIB-SMIv2", "dmmCA2MessageID"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2Message"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2MessageArgs"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2AlertStatus"),
        ("DELL-MM-MIB-SMIv2", "dmmDeviceServiceTag"),
        ("DELL-MM-MIB-SMIv2", "dmmCategoryName"),
        ("DELL-MM-MIB-SMIv2", "dmmSubCategoryName"),
        ("DELL-MM-MIB-SMIv2", "dmmSeverity"))
)
if mibBuilder.loadTexts:
    iDRAC4202alertStorageFanWarning.setStatus(
        "current"
    )

iDRAC4203alertStorageFanInformation = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 7, 0, 4203)
)
iDRAC4203alertStorageFanInformation.setObjects(
      *(("DELL-MM-MIB-SMIv2", "dmmCA2MessageID"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2Message"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2MessageArgs"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2AlertStatus"),
        ("DELL-MM-MIB-SMIv2", "dmmDeviceServiceTag"),
        ("DELL-MM-MIB-SMIv2", "dmmCategoryName"),
        ("DELL-MM-MIB-SMIv2", "dmmSubCategoryName"),
        ("DELL-MM-MIB-SMIv2", "dmmSeverity"))
)
if mibBuilder.loadTexts:
    iDRAC4203alertStorageFanInformation.setStatus(
        "current"
    )

iDRAC4209alertStorageTemperatureProbeFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 7, 0, 4209)
)
iDRAC4209alertStorageTemperatureProbeFailure.setObjects(
      *(("DELL-MM-MIB-SMIv2", "dmmCA2MessageID"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2Message"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2MessageArgs"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2AlertStatus"),
        ("DELL-MM-MIB-SMIv2", "dmmDeviceServiceTag"),
        ("DELL-MM-MIB-SMIv2", "dmmCategoryName"),
        ("DELL-MM-MIB-SMIv2", "dmmSubCategoryName"),
        ("DELL-MM-MIB-SMIv2", "dmmSeverity"))
)
if mibBuilder.loadTexts:
    iDRAC4209alertStorageTemperatureProbeFailure.setStatus(
        "current"
    )

iDRAC4210alertStorageTemperatureProbeWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 7, 0, 4210)
)
iDRAC4210alertStorageTemperatureProbeWarning.setObjects(
      *(("DELL-MM-MIB-SMIv2", "dmmCA2MessageID"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2Message"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2MessageArgs"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2AlertStatus"),
        ("DELL-MM-MIB-SMIv2", "dmmDeviceServiceTag"),
        ("DELL-MM-MIB-SMIv2", "dmmCategoryName"),
        ("DELL-MM-MIB-SMIv2", "dmmSubCategoryName"),
        ("DELL-MM-MIB-SMIv2", "dmmSeverity"))
)
if mibBuilder.loadTexts:
    iDRAC4210alertStorageTemperatureProbeWarning.setStatus(
        "current"
    )

iDRAC4211alertStorageTemperatureProbeInformation = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 7, 0, 4211)
)
iDRAC4211alertStorageTemperatureProbeInformation.setObjects(
      *(("DELL-MM-MIB-SMIv2", "dmmCA2MessageID"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2Message"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2MessageArgs"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2AlertStatus"),
        ("DELL-MM-MIB-SMIv2", "dmmDeviceServiceTag"),
        ("DELL-MM-MIB-SMIv2", "dmmCategoryName"),
        ("DELL-MM-MIB-SMIv2", "dmmSubCategoryName"),
        ("DELL-MM-MIB-SMIv2", "dmmSeverity"))
)
if mibBuilder.loadTexts:
    iDRAC4211alertStorageTemperatureProbeInformation.setStatus(
        "current"
    )

iDRAC4233alertStoragePowerSupplyFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 7, 0, 4233)
)
iDRAC4233alertStoragePowerSupplyFailure.setObjects(
      *(("DELL-MM-MIB-SMIv2", "dmmCA2MessageID"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2Message"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2MessageArgs"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2AlertStatus"),
        ("DELL-MM-MIB-SMIv2", "dmmDeviceServiceTag"),
        ("DELL-MM-MIB-SMIv2", "dmmCategoryName"),
        ("DELL-MM-MIB-SMIv2", "dmmSubCategoryName"),
        ("DELL-MM-MIB-SMIv2", "dmmSeverity"))
)
if mibBuilder.loadTexts:
    iDRAC4233alertStoragePowerSupplyFailure.setStatus(
        "current"
    )

iDRAC4234alertStoragePowerSupplyWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 7, 0, 4234)
)
iDRAC4234alertStoragePowerSupplyWarning.setObjects(
      *(("DELL-MM-MIB-SMIv2", "dmmCA2MessageID"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2Message"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2MessageArgs"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2AlertStatus"),
        ("DELL-MM-MIB-SMIv2", "dmmDeviceServiceTag"),
        ("DELL-MM-MIB-SMIv2", "dmmCategoryName"),
        ("DELL-MM-MIB-SMIv2", "dmmSubCategoryName"),
        ("DELL-MM-MIB-SMIv2", "dmmSeverity"))
)
if mibBuilder.loadTexts:
    iDRAC4234alertStoragePowerSupplyWarning.setStatus(
        "current"
    )

iDRAC4235alertStoragePowerSupplyInformation = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 7, 0, 4235)
)
iDRAC4235alertStoragePowerSupplyInformation.setObjects(
      *(("DELL-MM-MIB-SMIv2", "dmmCA2MessageID"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2Message"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2MessageArgs"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2AlertStatus"),
        ("DELL-MM-MIB-SMIv2", "dmmDeviceServiceTag"),
        ("DELL-MM-MIB-SMIv2", "dmmCategoryName"),
        ("DELL-MM-MIB-SMIv2", "dmmSubCategoryName"),
        ("DELL-MM-MIB-SMIv2", "dmmSeverity"))
)
if mibBuilder.loadTexts:
    iDRAC4235alertStoragePowerSupplyInformation.setStatus(
        "current"
    )

iDRAC4273alertStorageBatteryFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 7, 0, 4273)
)
iDRAC4273alertStorageBatteryFailure.setObjects(
      *(("DELL-MM-MIB-SMIv2", "dmmCA2MessageID"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2Message"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2MessageArgs"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2AlertStatus"),
        ("DELL-MM-MIB-SMIv2", "dmmDeviceServiceTag"),
        ("DELL-MM-MIB-SMIv2", "dmmCategoryName"),
        ("DELL-MM-MIB-SMIv2", "dmmSubCategoryName"),
        ("DELL-MM-MIB-SMIv2", "dmmSeverity"))
)
if mibBuilder.loadTexts:
    iDRAC4273alertStorageBatteryFailure.setStatus(
        "current"
    )

iDRAC4274alertStorageBatteryWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 7, 0, 4274)
)
iDRAC4274alertStorageBatteryWarning.setObjects(
      *(("DELL-MM-MIB-SMIv2", "dmmCA2MessageID"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2Message"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2MessageArgs"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2AlertStatus"),
        ("DELL-MM-MIB-SMIv2", "dmmDeviceServiceTag"),
        ("DELL-MM-MIB-SMIv2", "dmmCategoryName"),
        ("DELL-MM-MIB-SMIv2", "dmmSubCategoryName"),
        ("DELL-MM-MIB-SMIv2", "dmmSeverity"))
)
if mibBuilder.loadTexts:
    iDRAC4274alertStorageBatteryWarning.setStatus(
        "current"
    )

iDRAC4275alertStorageBatteryInformation = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 7, 0, 4275)
)
iDRAC4275alertStorageBatteryInformation.setObjects(
      *(("DELL-MM-MIB-SMIv2", "dmmCA2MessageID"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2Message"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2MessageArgs"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2AlertStatus"),
        ("DELL-MM-MIB-SMIv2", "dmmDeviceServiceTag"),
        ("DELL-MM-MIB-SMIv2", "dmmCategoryName"),
        ("DELL-MM-MIB-SMIv2", "dmmSubCategoryName"),
        ("DELL-MM-MIB-SMIv2", "dmmSeverity"))
)
if mibBuilder.loadTexts:
    iDRAC4275alertStorageBatteryInformation.setStatus(
        "current"
    )

iDRAC4329alertStorageControllerFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 7, 0, 4329)
)
iDRAC4329alertStorageControllerFailure.setObjects(
      *(("DELL-MM-MIB-SMIv2", "dmmCA2MessageID"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2Message"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2MessageArgs"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2AlertStatus"),
        ("DELL-MM-MIB-SMIv2", "dmmDeviceServiceTag"),
        ("DELL-MM-MIB-SMIv2", "dmmCategoryName"),
        ("DELL-MM-MIB-SMIv2", "dmmSubCategoryName"),
        ("DELL-MM-MIB-SMIv2", "dmmSeverity"))
)
if mibBuilder.loadTexts:
    iDRAC4329alertStorageControllerFailure.setStatus(
        "current"
    )

iDRAC4330alertStorageControllerWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 7, 0, 4330)
)
iDRAC4330alertStorageControllerWarning.setObjects(
      *(("DELL-MM-MIB-SMIv2", "dmmCA2MessageID"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2Message"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2MessageArgs"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2AlertStatus"),
        ("DELL-MM-MIB-SMIv2", "dmmDeviceServiceTag"),
        ("DELL-MM-MIB-SMIv2", "dmmCategoryName"),
        ("DELL-MM-MIB-SMIv2", "dmmSubCategoryName"),
        ("DELL-MM-MIB-SMIv2", "dmmSeverity"))
)
if mibBuilder.loadTexts:
    iDRAC4330alertStorageControllerWarning.setStatus(
        "current"
    )

iDRAC4331alertStorageControllerInformation = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 7, 0, 4331)
)
iDRAC4331alertStorageControllerInformation.setObjects(
      *(("DELL-MM-MIB-SMIv2", "dmmCA2MessageID"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2Message"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2MessageArgs"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2AlertStatus"),
        ("DELL-MM-MIB-SMIv2", "dmmDeviceServiceTag"),
        ("DELL-MM-MIB-SMIv2", "dmmCategoryName"),
        ("DELL-MM-MIB-SMIv2", "dmmSubCategoryName"),
        ("DELL-MM-MIB-SMIv2", "dmmSeverity"))
)
if mibBuilder.loadTexts:
    iDRAC4331alertStorageControllerInformation.setStatus(
        "current"
    )

iDRAC4337alertStorageEnclosureFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 7, 0, 4337)
)
iDRAC4337alertStorageEnclosureFailure.setObjects(
      *(("DELL-MM-MIB-SMIv2", "dmmCA2MessageID"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2Message"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2MessageArgs"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2AlertStatus"),
        ("DELL-MM-MIB-SMIv2", "dmmDeviceServiceTag"),
        ("DELL-MM-MIB-SMIv2", "dmmCategoryName"),
        ("DELL-MM-MIB-SMIv2", "dmmSubCategoryName"),
        ("DELL-MM-MIB-SMIv2", "dmmSeverity"))
)
if mibBuilder.loadTexts:
    iDRAC4337alertStorageEnclosureFailure.setStatus(
        "current"
    )

iDRAC4338alertStorageEnclosureWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 7, 0, 4338)
)
iDRAC4338alertStorageEnclosureWarning.setObjects(
      *(("DELL-MM-MIB-SMIv2", "dmmCA2MessageID"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2Message"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2MessageArgs"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2AlertStatus"),
        ("DELL-MM-MIB-SMIv2", "dmmDeviceServiceTag"),
        ("DELL-MM-MIB-SMIv2", "dmmCategoryName"),
        ("DELL-MM-MIB-SMIv2", "dmmSubCategoryName"),
        ("DELL-MM-MIB-SMIv2", "dmmSeverity"))
)
if mibBuilder.loadTexts:
    iDRAC4338alertStorageEnclosureWarning.setStatus(
        "current"
    )

iDRAC4339alertStorageEnclosureInformation = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 7, 0, 4339)
)
iDRAC4339alertStorageEnclosureInformation.setObjects(
      *(("DELL-MM-MIB-SMIv2", "dmmCA2MessageID"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2Message"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2MessageArgs"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2AlertStatus"),
        ("DELL-MM-MIB-SMIv2", "dmmDeviceServiceTag"),
        ("DELL-MM-MIB-SMIv2", "dmmCategoryName"),
        ("DELL-MM-MIB-SMIv2", "dmmSubCategoryName"),
        ("DELL-MM-MIB-SMIv2", "dmmSeverity"))
)
if mibBuilder.loadTexts:
    iDRAC4339alertStorageEnclosureInformation.setStatus(
        "current"
    )

iDRAC4345alertStoragePhysicalDiskFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 7, 0, 4345)
)
iDRAC4345alertStoragePhysicalDiskFailure.setObjects(
      *(("DELL-MM-MIB-SMIv2", "dmmCA2MessageID"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2Message"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2MessageArgs"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2AlertStatus"),
        ("DELL-MM-MIB-SMIv2", "dmmDeviceServiceTag"),
        ("DELL-MM-MIB-SMIv2", "dmmCategoryName"),
        ("DELL-MM-MIB-SMIv2", "dmmSubCategoryName"),
        ("DELL-MM-MIB-SMIv2", "dmmSeverity"))
)
if mibBuilder.loadTexts:
    iDRAC4345alertStoragePhysicalDiskFailure.setStatus(
        "current"
    )

iDRAC4346alertStoragePhysicalDiskWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 7, 0, 4346)
)
iDRAC4346alertStoragePhysicalDiskWarning.setObjects(
      *(("DELL-MM-MIB-SMIv2", "dmmCA2MessageID"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2Message"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2MessageArgs"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2AlertStatus"),
        ("DELL-MM-MIB-SMIv2", "dmmDeviceServiceTag"),
        ("DELL-MM-MIB-SMIv2", "dmmCategoryName"),
        ("DELL-MM-MIB-SMIv2", "dmmSubCategoryName"),
        ("DELL-MM-MIB-SMIv2", "dmmSeverity"))
)
if mibBuilder.loadTexts:
    iDRAC4346alertStoragePhysicalDiskWarning.setStatus(
        "current"
    )

iDRAC4347alertStoragePhysicalDiskInformation = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 7, 0, 4347)
)
iDRAC4347alertStoragePhysicalDiskInformation.setObjects(
      *(("DELL-MM-MIB-SMIv2", "dmmCA2MessageID"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2Message"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2MessageArgs"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2AlertStatus"),
        ("DELL-MM-MIB-SMIv2", "dmmDeviceServiceTag"),
        ("DELL-MM-MIB-SMIv2", "dmmCategoryName"),
        ("DELL-MM-MIB-SMIv2", "dmmSubCategoryName"),
        ("DELL-MM-MIB-SMIv2", "dmmSeverity"))
)
if mibBuilder.loadTexts:
    iDRAC4347alertStoragePhysicalDiskInformation.setStatus(
        "current"
    )

iDRAC4353alertStorageVirtualDiskFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 7, 0, 4353)
)
iDRAC4353alertStorageVirtualDiskFailure.setObjects(
      *(("DELL-MM-MIB-SMIv2", "dmmCA2MessageID"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2Message"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2MessageArgs"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2AlertStatus"),
        ("DELL-MM-MIB-SMIv2", "dmmDeviceServiceTag"),
        ("DELL-MM-MIB-SMIv2", "dmmCategoryName"),
        ("DELL-MM-MIB-SMIv2", "dmmSubCategoryName"),
        ("DELL-MM-MIB-SMIv2", "dmmSeverity"))
)
if mibBuilder.loadTexts:
    iDRAC4353alertStorageVirtualDiskFailure.setStatus(
        "current"
    )

iDRAC4354alertStorageVirtualDiskWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 7, 0, 4354)
)
iDRAC4354alertStorageVirtualDiskWarning.setObjects(
      *(("DELL-MM-MIB-SMIv2", "dmmCA2MessageID"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2Message"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2MessageArgs"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2AlertStatus"),
        ("DELL-MM-MIB-SMIv2", "dmmDeviceServiceTag"),
        ("DELL-MM-MIB-SMIv2", "dmmCategoryName"),
        ("DELL-MM-MIB-SMIv2", "dmmSubCategoryName"),
        ("DELL-MM-MIB-SMIv2", "dmmSeverity"))
)
if mibBuilder.loadTexts:
    iDRAC4354alertStorageVirtualDiskWarning.setStatus(
        "current"
    )

iDRAC4355alertStorageVirtualDiskInformation = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 7, 0, 4355)
)
iDRAC4355alertStorageVirtualDiskInformation.setObjects(
      *(("DELL-MM-MIB-SMIv2", "dmmCA2MessageID"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2Message"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2MessageArgs"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2AlertStatus"),
        ("DELL-MM-MIB-SMIv2", "dmmDeviceServiceTag"),
        ("DELL-MM-MIB-SMIv2", "dmmCategoryName"),
        ("DELL-MM-MIB-SMIv2", "dmmSubCategoryName"),
        ("DELL-MM-MIB-SMIv2", "dmmSeverity"))
)
if mibBuilder.loadTexts:
    iDRAC4355alertStorageVirtualDiskInformation.setStatus(
        "current"
    )

iDRAC4370alertStorageSolidstateDrive = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 7, 0, 4370)
)
iDRAC4370alertStorageSolidstateDrive.setObjects(
      *(("DELL-MM-MIB-SMIv2", "dmmCA2MessageID"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2Message"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2MessageArgs"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2AlertStatus"),
        ("DELL-MM-MIB-SMIv2", "dmmDeviceServiceTag"),
        ("DELL-MM-MIB-SMIv2", "dmmCategoryName"),
        ("DELL-MM-MIB-SMIv2", "dmmSubCategoryName"),
        ("DELL-MM-MIB-SMIv2", "dmmSeverity"))
)
if mibBuilder.loadTexts:
    iDRAC4370alertStorageSolidstateDrive.setStatus(
        "current"
    )

iDRAC4433alertStorageSecurityFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 7, 0, 4433)
)
iDRAC4433alertStorageSecurityFailure.setObjects(
      *(("DELL-MM-MIB-SMIv2", "dmmCA2MessageID"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2Message"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2MessageArgs"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2AlertStatus"),
        ("DELL-MM-MIB-SMIv2", "dmmDeviceServiceTag"),
        ("DELL-MM-MIB-SMIv2", "dmmCategoryName"),
        ("DELL-MM-MIB-SMIv2", "dmmSubCategoryName"),
        ("DELL-MM-MIB-SMIv2", "dmmSeverity"))
)
if mibBuilder.loadTexts:
    iDRAC4433alertStorageSecurityFailure.setStatus(
        "current"
    )

iDRAC4434alertStorageSecurityWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 7, 0, 4434)
)
iDRAC4434alertStorageSecurityWarning.setObjects(
      *(("DELL-MM-MIB-SMIv2", "dmmCA2MessageID"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2Message"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2MessageArgs"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2AlertStatus"),
        ("DELL-MM-MIB-SMIv2", "dmmDeviceServiceTag"),
        ("DELL-MM-MIB-SMIv2", "dmmCategoryName"),
        ("DELL-MM-MIB-SMIv2", "dmmSubCategoryName"),
        ("DELL-MM-MIB-SMIv2", "dmmSeverity"))
)
if mibBuilder.loadTexts:
    iDRAC4434alertStorageSecurityWarning.setStatus(
        "current"
    )

iDRAC4435alertStorageSecurityInformation = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 7, 0, 4435)
)
iDRAC4435alertStorageSecurityInformation.setObjects(
      *(("DELL-MM-MIB-SMIv2", "dmmCA2MessageID"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2Message"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2MessageArgs"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2AlertStatus"),
        ("DELL-MM-MIB-SMIv2", "dmmDeviceServiceTag"),
        ("DELL-MM-MIB-SMIv2", "dmmCategoryName"),
        ("DELL-MM-MIB-SMIv2", "dmmSubCategoryName"),
        ("DELL-MM-MIB-SMIv2", "dmmSeverity"))
)
if mibBuilder.loadTexts:
    iDRAC4435alertStorageSecurityInformation.setStatus(
        "current"
    )

iDRAC4761alertStorageSoftwareDefinedSubSystemFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 7, 0, 4761)
)
iDRAC4761alertStorageSoftwareDefinedSubSystemFailure.setObjects(
      *(("DELL-MM-MIB-SMIv2", "dmmCA2MessageID"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2Message"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2MessageArgs"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2AlertStatus"),
        ("DELL-MM-MIB-SMIv2", "dmmDeviceServiceTag"),
        ("DELL-MM-MIB-SMIv2", "dmmCategoryName"),
        ("DELL-MM-MIB-SMIv2", "dmmSubCategoryName"),
        ("DELL-MM-MIB-SMIv2", "dmmSeverity"))
)
if mibBuilder.loadTexts:
    iDRAC4761alertStorageSoftwareDefinedSubSystemFailure.setStatus(
        "current"
    )

iDRAC4762alertStorageSoftwareDefinedSubSystemWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 7, 0, 4762)
)
iDRAC4762alertStorageSoftwareDefinedSubSystemWarning.setObjects(
      *(("DELL-MM-MIB-SMIv2", "dmmCA2MessageID"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2Message"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2MessageArgs"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2AlertStatus"),
        ("DELL-MM-MIB-SMIv2", "dmmDeviceServiceTag"),
        ("DELL-MM-MIB-SMIv2", "dmmCategoryName"),
        ("DELL-MM-MIB-SMIv2", "dmmSubCategoryName"),
        ("DELL-MM-MIB-SMIv2", "dmmSeverity"))
)
if mibBuilder.loadTexts:
    iDRAC4762alertStorageSoftwareDefinedSubSystemWarning.setStatus(
        "current"
    )

iDRAC6211alertUpdateJobInformation = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 7, 0, 6211)
)
iDRAC6211alertUpdateJobInformation.setObjects(
      *(("DELL-MM-MIB-SMIv2", "dmmCA2MessageID"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2Message"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2MessageArgs"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2AlertStatus"),
        ("DELL-MM-MIB-SMIv2", "dmmDeviceServiceTag"),
        ("DELL-MM-MIB-SMIv2", "dmmCategoryName"),
        ("DELL-MM-MIB-SMIv2", "dmmSubCategoryName"),
        ("DELL-MM-MIB-SMIv2", "dmmSeverity"))
)
if mibBuilder.loadTexts:
    iDRAC6211alertUpdateJobInformation.setStatus(
        "current"
    )

iDRAC6314alertSoftwareChangeUpdateWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 7, 0, 6314)
)
iDRAC6314alertSoftwareChangeUpdateWarning.setObjects(
      *(("DELL-MM-MIB-SMIv2", "dmmCA2MessageID"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2Message"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2MessageArgs"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2AlertStatus"),
        ("DELL-MM-MIB-SMIv2", "dmmDeviceServiceTag"),
        ("DELL-MM-MIB-SMIv2", "dmmCategoryName"),
        ("DELL-MM-MIB-SMIv2", "dmmSubCategoryName"),
        ("DELL-MM-MIB-SMIv2", "dmmSeverity"))
)
if mibBuilder.loadTexts:
    iDRAC6314alertSoftwareChangeUpdateWarning.setStatus(
        "current"
    )

iDRAC8305alertTemperatureProbeChangeFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 7, 0, 8305)
)
iDRAC8305alertTemperatureProbeChangeFailure.setObjects(
      *(("DELL-MM-MIB-SMIv2", "dmmCA2MessageID"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2Message"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2MessageArgs"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2AlertStatus"),
        ("DELL-MM-MIB-SMIv2", "dmmDeviceServiceTag"),
        ("DELL-MM-MIB-SMIv2", "dmmCategoryName"),
        ("DELL-MM-MIB-SMIv2", "dmmSubCategoryName"),
        ("DELL-MM-MIB-SMIv2", "dmmSeverity"))
)
if mibBuilder.loadTexts:
    iDRAC8305alertTemperatureProbeChangeFailure.setStatus(
        "current"
    )

iDRAC8306alertTemperatureProbeReadWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 7, 0, 8306)
)
iDRAC8306alertTemperatureProbeReadWarning.setObjects(
      *(("DELL-MM-MIB-SMIv2", "dmmCA2MessageID"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2Message"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2MessageArgs"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2AlertStatus"),
        ("DELL-MM-MIB-SMIv2", "dmmDeviceServiceTag"),
        ("DELL-MM-MIB-SMIv2", "dmmCategoryName"),
        ("DELL-MM-MIB-SMIv2", "dmmSubCategoryName"),
        ("DELL-MM-MIB-SMIv2", "dmmSeverity"))
)
if mibBuilder.loadTexts:
    iDRAC8306alertTemperatureProbeReadWarning.setStatus(
        "current"
    )

iDRAC8329alertPowerSupplyAuditFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 7, 0, 8329)
)
iDRAC8329alertPowerSupplyAuditFailure.setObjects(
      *(("DELL-MM-MIB-SMIv2", "dmmCA2MessageID"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2Message"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2MessageArgs"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2AlertStatus"),
        ("DELL-MM-MIB-SMIv2", "dmmDeviceServiceTag"),
        ("DELL-MM-MIB-SMIv2", "dmmCategoryName"),
        ("DELL-MM-MIB-SMIv2", "dmmSubCategoryName"),
        ("DELL-MM-MIB-SMIv2", "dmmSeverity"))
)
if mibBuilder.loadTexts:
    iDRAC8329alertPowerSupplyAuditFailure.setStatus(
        "current"
    )

iDRAC8330alertPowerSupplyAuditWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 7, 0, 8330)
)
iDRAC8330alertPowerSupplyAuditWarning.setObjects(
      *(("DELL-MM-MIB-SMIv2", "dmmCA2MessageID"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2Message"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2MessageArgs"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2AlertStatus"),
        ("DELL-MM-MIB-SMIv2", "dmmDeviceServiceTag"),
        ("DELL-MM-MIB-SMIv2", "dmmCategoryName"),
        ("DELL-MM-MIB-SMIv2", "dmmSubCategoryName"),
        ("DELL-MM-MIB-SMIv2", "dmmSeverity"))
)
if mibBuilder.loadTexts:
    iDRAC8330alertPowerSupplyAuditWarning.setStatus(
        "current"
    )

iDRAC8417alertPowerUsageAuditFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 7, 0, 8417)
)
iDRAC8417alertPowerUsageAuditFailure.setObjects(
      *(("DELL-MM-MIB-SMIv2", "dmmCA2MessageID"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2Message"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2MessageArgs"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2AlertStatus"),
        ("DELL-MM-MIB-SMIv2", "dmmDeviceServiceTag"),
        ("DELL-MM-MIB-SMIv2", "dmmCategoryName"),
        ("DELL-MM-MIB-SMIv2", "dmmSubCategoryName"),
        ("DELL-MM-MIB-SMIv2", "dmmSeverity"))
)
if mibBuilder.loadTexts:
    iDRAC8417alertPowerUsageAuditFailure.setStatus(
        "current"
    )

iDRAC8418alertPowerUsageAuditWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 7, 0, 8418)
)
iDRAC8418alertPowerUsageAuditWarning.setObjects(
      *(("DELL-MM-MIB-SMIv2", "dmmCA2MessageID"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2Message"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2MessageArgs"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2AlertStatus"),
        ("DELL-MM-MIB-SMIv2", "dmmDeviceServiceTag"),
        ("DELL-MM-MIB-SMIv2", "dmmCategoryName"),
        ("DELL-MM-MIB-SMIv2", "dmmSubCategoryName"),
        ("DELL-MM-MIB-SMIv2", "dmmSeverity"))
)
if mibBuilder.loadTexts:
    iDRAC8418alertPowerUsageAuditWarning.setStatus(
        "current"
    )

iDRAC8419alertPowerUsageAuditInformation = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 7, 0, 8419)
)
iDRAC8419alertPowerUsageAuditInformation.setObjects(
      *(("DELL-MM-MIB-SMIv2", "dmmCA2MessageID"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2Message"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2MessageArgs"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2AlertStatus"),
        ("DELL-MM-MIB-SMIv2", "dmmDeviceServiceTag"),
        ("DELL-MM-MIB-SMIv2", "dmmCategoryName"),
        ("DELL-MM-MIB-SMIv2", "dmmSubCategoryName"),
        ("DELL-MM-MIB-SMIv2", "dmmSeverity"))
)
if mibBuilder.loadTexts:
    iDRAC8419alertPowerUsageAuditInformation.setStatus(
        "current"
    )

iDRAC8474alertHWCAuditWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 7, 0, 8474)
)
iDRAC8474alertHWCAuditWarning.setObjects(
      *(("DELL-MM-MIB-SMIv2", "dmmCA2MessageID"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2Message"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2MessageArgs"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2AlertStatus"),
        ("DELL-MM-MIB-SMIv2", "dmmDeviceServiceTag"),
        ("DELL-MM-MIB-SMIv2", "dmmCategoryName"),
        ("DELL-MM-MIB-SMIv2", "dmmSubCategoryName"),
        ("DELL-MM-MIB-SMIv2", "dmmSeverity"))
)
if mibBuilder.loadTexts:
    iDRAC8474alertHWCAuditWarning.setStatus(
        "current"
    )

iDRAC8475alertHWCAuditInformation = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 7, 0, 8475)
)
iDRAC8475alertHWCAuditInformation.setObjects(
      *(("DELL-MM-MIB-SMIv2", "dmmCA2MessageID"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2Message"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2MessageArgs"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2AlertStatus"),
        ("DELL-MM-MIB-SMIv2", "dmmDeviceServiceTag"),
        ("DELL-MM-MIB-SMIv2", "dmmCategoryName"),
        ("DELL-MM-MIB-SMIv2", "dmmSubCategoryName"),
        ("DELL-MM-MIB-SMIv2", "dmmSeverity"))
)
if mibBuilder.loadTexts:
    iDRAC8475alertHWCAuditInformation.setStatus(
        "current"
    )

iDRAC8490alertUserTrackingWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 7, 0, 8490)
)
iDRAC8490alertUserTrackingWarning.setObjects(
      *(("DELL-MM-MIB-SMIv2", "dmmCA2MessageID"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2Message"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2MessageArgs"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2AlertStatus"),
        ("DELL-MM-MIB-SMIv2", "dmmDeviceServiceTag"),
        ("DELL-MM-MIB-SMIv2", "dmmCategoryName"),
        ("DELL-MM-MIB-SMIv2", "dmmSubCategoryName"),
        ("DELL-MM-MIB-SMIv2", "dmmSeverity"))
)
if mibBuilder.loadTexts:
    iDRAC8490alertUserTrackingWarning.setStatus(
        "current"
    )

iDRAC8499alertiDRACIPAddressChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 7, 0, 8499)
)
iDRAC8499alertiDRACIPAddressChange.setObjects(
      *(("DELL-MM-MIB-SMIv2", "dmmCA2MessageID"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2Message"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2MessageArgs"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2AlertStatus"),
        ("DELL-MM-MIB-SMIv2", "dmmDeviceServiceTag"),
        ("DELL-MM-MIB-SMIv2", "dmmCategoryName"),
        ("DELL-MM-MIB-SMIv2", "dmmSubCategoryName"),
        ("DELL-MM-MIB-SMIv2", "dmmSeverity"))
)
if mibBuilder.loadTexts:
    iDRAC8499alertiDRACIPAddressChange.setStatus(
        "current"
    )

iDRAC8513alertLicenseFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 7, 0, 8513)
)
iDRAC8513alertLicenseFailure.setObjects(
      *(("DELL-MM-MIB-SMIv2", "dmmCA2MessageID"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2Message"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2MessageArgs"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2AlertStatus"),
        ("DELL-MM-MIB-SMIv2", "dmmDeviceServiceTag"),
        ("DELL-MM-MIB-SMIv2", "dmmCategoryName"),
        ("DELL-MM-MIB-SMIv2", "dmmSubCategoryName"),
        ("DELL-MM-MIB-SMIv2", "dmmSeverity"))
)
if mibBuilder.loadTexts:
    iDRAC8513alertLicenseFailure.setStatus(
        "current"
    )

iDRAC8514alertLicenseWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 7, 0, 8514)
)
iDRAC8514alertLicenseWarning.setObjects(
      *(("DELL-MM-MIB-SMIv2", "dmmCA2MessageID"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2Message"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2MessageArgs"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2AlertStatus"),
        ("DELL-MM-MIB-SMIv2", "dmmDeviceServiceTag"),
        ("DELL-MM-MIB-SMIv2", "dmmCategoryName"),
        ("DELL-MM-MIB-SMIv2", "dmmSubCategoryName"),
        ("DELL-MM-MIB-SMIv2", "dmmSeverity"))
)
if mibBuilder.loadTexts:
    iDRAC8514alertLicenseWarning.setStatus(
        "current"
    )

iDRAC8515alertLicenseInformation = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 7, 0, 8515)
)
iDRAC8515alertLicenseInformation.setObjects(
      *(("DELL-MM-MIB-SMIv2", "dmmCA2MessageID"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2Message"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2MessageArgs"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2AlertStatus"),
        ("DELL-MM-MIB-SMIv2", "dmmDeviceServiceTag"),
        ("DELL-MM-MIB-SMIv2", "dmmCategoryName"),
        ("DELL-MM-MIB-SMIv2", "dmmSubCategoryName"),
        ("DELL-MM-MIB-SMIv2", "dmmSeverity"))
)
if mibBuilder.loadTexts:
    iDRAC8515alertLicenseInformation.setStatus(
        "current"
    )

iDRAC8562alertPCIDeviceAuditWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 7, 0, 8562)
)
iDRAC8562alertPCIDeviceAuditWarning.setObjects(
      *(("DELL-MM-MIB-SMIv2", "dmmCA2MessageID"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2Message"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2MessageArgs"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2AlertStatus"),
        ("DELL-MM-MIB-SMIv2", "dmmDeviceServiceTag"),
        ("DELL-MM-MIB-SMIv2", "dmmCategoryName"),
        ("DELL-MM-MIB-SMIv2", "dmmSubCategoryName"),
        ("DELL-MM-MIB-SMIv2", "dmmSeverity"))
)
if mibBuilder.loadTexts:
    iDRAC8562alertPCIDeviceAuditWarning.setStatus(
        "current"
    )

iDRAC8579alertSystemPowerStateChangeInformation = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 7, 0, 8579)
)
iDRAC8579alertSystemPowerStateChangeInformation.setObjects(
      *(("DELL-MM-MIB-SMIv2", "dmmCA2MessageID"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2Message"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2MessageArgs"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2AlertStatus"),
        ("DELL-MM-MIB-SMIv2", "dmmDeviceServiceTag"),
        ("DELL-MM-MIB-SMIv2", "dmmCategoryName"),
        ("DELL-MM-MIB-SMIv2", "dmmSubCategoryName"),
        ("DELL-MM-MIB-SMIv2", "dmmSeverity"))
)
if mibBuilder.loadTexts:
    iDRAC8579alertSystemPowerStateChangeInformation.setStatus(
        "current"
    )

iDRAC8594alertDebugWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 7, 0, 8594)
)
iDRAC8594alertDebugWarning.setObjects(
      *(("DELL-MM-MIB-SMIv2", "dmmCA2MessageID"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2Message"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2MessageArgs"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2AlertStatus"),
        ("DELL-MM-MIB-SMIv2", "dmmDeviceServiceTag"),
        ("DELL-MM-MIB-SMIv2", "dmmCategoryName"),
        ("DELL-MM-MIB-SMIv2", "dmmSubCategoryName"),
        ("DELL-MM-MIB-SMIv2", "dmmSeverity"))
)
if mibBuilder.loadTexts:
    iDRAC8594alertDebugWarning.setStatus(
        "current"
    )

iDRAC8595alertDebugInformation = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 7, 0, 8595)
)
iDRAC8595alertDebugInformation.setObjects(
      *(("DELL-MM-MIB-SMIv2", "dmmCA2MessageID"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2Message"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2MessageArgs"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2AlertStatus"),
        ("DELL-MM-MIB-SMIv2", "dmmDeviceServiceTag"),
        ("DELL-MM-MIB-SMIv2", "dmmCategoryName"),
        ("DELL-MM-MIB-SMIv2", "dmmSubCategoryName"),
        ("DELL-MM-MIB-SMIv2", "dmmSeverity"))
)
if mibBuilder.loadTexts:
    iDRAC8595alertDebugInformation.setStatus(
        "current"
    )

iDRAC8674alertRacConfigurationChangewarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 7, 0, 8674)
)
iDRAC8674alertRacConfigurationChangewarning.setObjects(
      *(("DELL-MM-MIB-SMIv2", "dmmCA2MessageID"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2Message"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2MessageArgs"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2AlertStatus"),
        ("DELL-MM-MIB-SMIv2", "dmmDeviceServiceTag"),
        ("DELL-MM-MIB-SMIv2", "dmmCategoryName"),
        ("DELL-MM-MIB-SMIv2", "dmmSubCategoryName"),
        ("DELL-MM-MIB-SMIv2", "dmmSeverity"))
)
if mibBuilder.loadTexts:
    iDRAC8674alertRacConfigurationChangewarning.setStatus(
        "current"
    )

iDRAC8675alertRacConfigurationChangeInformation = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 7, 0, 8675)
)
iDRAC8675alertRacConfigurationChangeInformation.setObjects(
      *(("DELL-MM-MIB-SMIv2", "dmmCA2MessageID"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2Message"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2MessageArgs"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2AlertStatus"),
        ("DELL-MM-MIB-SMIv2", "dmmDeviceServiceTag"),
        ("DELL-MM-MIB-SMIv2", "dmmCategoryName"),
        ("DELL-MM-MIB-SMIv2", "dmmSubCategoryName"),
        ("DELL-MM-MIB-SMIv2", "dmmSeverity"))
)
if mibBuilder.loadTexts:
    iDRAC8675alertRacConfigurationChangeInformation.setStatus(
        "current"
    )

iDRAC8689alertCMCAuditFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 7, 0, 8689)
)
iDRAC8689alertCMCAuditFailure.setObjects(
      *(("DELL-MM-MIB-SMIv2", "dmmCA2MessageID"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2Message"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2MessageArgs"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2AlertStatus"),
        ("DELL-MM-MIB-SMIv2", "dmmDeviceServiceTag"),
        ("DELL-MM-MIB-SMIv2", "dmmCategoryName"),
        ("DELL-MM-MIB-SMIv2", "dmmSubCategoryName"),
        ("DELL-MM-MIB-SMIv2", "dmmSeverity"))
)
if mibBuilder.loadTexts:
    iDRAC8689alertCMCAuditFailure.setStatus(
        "current"
    )

iDRAC8690alertCMCAuditWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 7, 0, 8690)
)
iDRAC8690alertCMCAuditWarning.setObjects(
      *(("DELL-MM-MIB-SMIv2", "dmmCA2MessageID"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2Message"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2MessageArgs"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2AlertStatus"),
        ("DELL-MM-MIB-SMIv2", "dmmDeviceServiceTag"),
        ("DELL-MM-MIB-SMIv2", "dmmCategoryName"),
        ("DELL-MM-MIB-SMIv2", "dmmSubCategoryName"),
        ("DELL-MM-MIB-SMIv2", "dmmSeverity"))
)
if mibBuilder.loadTexts:
    iDRAC8690alertCMCAuditWarning.setStatus(
        "current"
    )

iDRAC8691alertCMCAuditInformation = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 7, 0, 8691)
)
iDRAC8691alertCMCAuditInformation.setObjects(
      *(("DELL-MM-MIB-SMIv2", "dmmCA2MessageID"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2Message"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2MessageArgs"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2AlertStatus"),
        ("DELL-MM-MIB-SMIv2", "dmmDeviceServiceTag"),
        ("DELL-MM-MIB-SMIv2", "dmmCategoryName"),
        ("DELL-MM-MIB-SMIv2", "dmmSubCategoryName"),
        ("DELL-MM-MIB-SMIv2", "dmmSeverity"))
)
if mibBuilder.loadTexts:
    iDRAC8691alertCMCAuditInformation.setStatus(
        "current"
    )

iDRAC10267alertJobControlConfigurationInformation = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 7, 0, 10267)
)
iDRAC10267alertJobControlConfigurationInformation.setObjects(
      *(("DELL-MM-MIB-SMIv2", "dmmCA2MessageID"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2Message"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2MessageArgs"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2AlertStatus"),
        ("DELL-MM-MIB-SMIv2", "dmmDeviceServiceTag"),
        ("DELL-MM-MIB-SMIv2", "dmmCategoryName"),
        ("DELL-MM-MIB-SMIv2", "dmmSubCategoryName"),
        ("DELL-MM-MIB-SMIv2", "dmmSeverity"))
)
if mibBuilder.loadTexts:
    iDRAC10267alertJobControlConfigurationInformation.setStatus(
        "current"
    )

iDRAC10298alertPRDeviceDetectionWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 7, 0, 10298)
)
iDRAC10298alertPRDeviceDetectionWarning.setObjects(
      *(("DELL-MM-MIB-SMIv2", "dmmCA2MessageID"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2Message"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2MessageArgs"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2AlertStatus"),
        ("DELL-MM-MIB-SMIv2", "dmmDeviceServiceTag"),
        ("DELL-MM-MIB-SMIv2", "dmmCategoryName"),
        ("DELL-MM-MIB-SMIv2", "dmmSubCategoryName"),
        ("DELL-MM-MIB-SMIv2", "dmmSeverity"))
)
if mibBuilder.loadTexts:
    iDRAC10298alertPRDeviceDetectionWarning.setStatus(
        "current"
    )

iDRAC10395alertTestTrapEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 7, 0, 10395)
)
iDRAC10395alertTestTrapEvent.setObjects(
      *(("DELL-MM-MIB-SMIv2", "dmmCA2MessageID"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2Message"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2MessageArgs"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2AlertStatus"),
        ("DELL-MM-MIB-SMIv2", "dmmDeviceServiceTag"),
        ("DELL-MM-MIB-SMIv2", "dmmCategoryName"),
        ("DELL-MM-MIB-SMIv2", "dmmSubCategoryName"),
        ("DELL-MM-MIB-SMIv2", "dmmSeverity"))
)
if mibBuilder.loadTexts:
    iDRAC10395alertTestTrapEvent.setStatus(
        "current"
    )

iDRAC10529alertSWCConfigurationFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 7, 0, 10529)
)
iDRAC10529alertSWCConfigurationFailure.setObjects(
      *(("DELL-MM-MIB-SMIv2", "dmmCA2MessageID"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2Message"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2MessageArgs"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2AlertStatus"),
        ("DELL-MM-MIB-SMIv2", "dmmDeviceServiceTag"),
        ("DELL-MM-MIB-SMIv2", "dmmCategoryName"),
        ("DELL-MM-MIB-SMIv2", "dmmSubCategoryName"),
        ("DELL-MM-MIB-SMIv2", "dmmSeverity"))
)
if mibBuilder.loadTexts:
    iDRAC10529alertSWCConfigurationFailure.setStatus(
        "current"
    )

iDRAC10530alertSWCConfigurationWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 7, 0, 10530)
)
iDRAC10530alertSWCConfigurationWarning.setObjects(
      *(("DELL-MM-MIB-SMIv2", "dmmCA2MessageID"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2Message"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2MessageArgs"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2AlertStatus"),
        ("DELL-MM-MIB-SMIv2", "dmmDeviceServiceTag"),
        ("DELL-MM-MIB-SMIv2", "dmmCategoryName"),
        ("DELL-MM-MIB-SMIv2", "dmmSubCategoryName"),
        ("DELL-MM-MIB-SMIv2", "dmmSeverity"))
)
if mibBuilder.loadTexts:
    iDRAC10530alertSWCConfigurationWarning.setStatus(
        "current"
    )

iDRAC10531alertSWCConfigurationInformation = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 7, 0, 10531)
)
iDRAC10531alertSWCConfigurationInformation.setObjects(
      *(("DELL-MM-MIB-SMIv2", "dmmCA2MessageID"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2Message"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2MessageArgs"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2AlertStatus"),
        ("DELL-MM-MIB-SMIv2", "dmmDeviceServiceTag"),
        ("DELL-MM-MIB-SMIv2", "dmmCategoryName"),
        ("DELL-MM-MIB-SMIv2", "dmmSubCategoryName"),
        ("DELL-MM-MIB-SMIv2", "dmmSeverity"))
)
if mibBuilder.loadTexts:
    iDRAC10531alertSWCConfigurationInformation.setStatus(
        "current"
    )

iDRAC10547alertIPAddressConfigurationInformation = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 7, 0, 10547)
)
iDRAC10547alertIPAddressConfigurationInformation.setObjects(
      *(("DELL-MM-MIB-SMIv2", "dmmCA2MessageID"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2Message"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2MessageArgs"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2AlertStatus"),
        ("DELL-MM-MIB-SMIv2", "dmmDeviceServiceTag"),
        ("DELL-MM-MIB-SMIv2", "dmmCategoryName"),
        ("DELL-MM-MIB-SMIv2", "dmmSubCategoryName"),
        ("DELL-MM-MIB-SMIv2", "dmmSeverity"))
)
if mibBuilder.loadTexts:
    iDRAC10547alertIPAddressConfigurationInformation.setStatus(
        "current"
    )

iDRAC10578alertSecurityConfigurationWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 7, 0, 10578)
)
iDRAC10578alertSecurityConfigurationWarning.setObjects(
      *(("DELL-MM-MIB-SMIv2", "dmmCA2MessageID"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2Message"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2MessageArgs"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2AlertStatus"),
        ("DELL-MM-MIB-SMIv2", "dmmDeviceServiceTag"),
        ("DELL-MM-MIB-SMIv2", "dmmCategoryName"),
        ("DELL-MM-MIB-SMIv2", "dmmSubCategoryName"),
        ("DELL-MM-MIB-SMIv2", "dmmSeverity"))
)
if mibBuilder.loadTexts:
    iDRAC10578alertSecurityConfigurationWarning.setStatus(
        "current"
    )

iDRAC10611alertPCIDeviceConfigurationInformation = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 7, 0, 10611)
)
iDRAC10611alertPCIDeviceConfigurationInformation.setObjects(
      *(("DELL-MM-MIB-SMIv2", "dmmCA2MessageID"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2Message"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2MessageArgs"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2AlertStatus"),
        ("DELL-MM-MIB-SMIv2", "dmmDeviceServiceTag"),
        ("DELL-MM-MIB-SMIv2", "dmmCategoryName"),
        ("DELL-MM-MIB-SMIv2", "dmmSubCategoryName"),
        ("DELL-MM-MIB-SMIv2", "dmmSeverity"))
)
if mibBuilder.loadTexts:
    iDRAC10611alertPCIDeviceConfigurationInformation.setStatus(
        "current"
    )

iDRAC10627alertSystemConfigurationChangeInformation = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 7, 0, 10627)
)
iDRAC10627alertSystemConfigurationChangeInformation.setObjects(
      *(("DELL-MM-MIB-SMIv2", "dmmCA2MessageID"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2Message"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2MessageArgs"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2AlertStatus"),
        ("DELL-MM-MIB-SMIv2", "dmmDeviceServiceTag"),
        ("DELL-MM-MIB-SMIv2", "dmmCategoryName"),
        ("DELL-MM-MIB-SMIv2", "dmmSubCategoryName"),
        ("DELL-MM-MIB-SMIv2", "dmmSeverity"))
)
if mibBuilder.loadTexts:
    iDRAC10627alertSystemConfigurationChangeInformation.setStatus(
        "current"
    )

iDRAC10635alertAutoDiscoveryInformation = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 7, 0, 10635)
)
iDRAC10635alertAutoDiscoveryInformation.setObjects(
      *(("DELL-MM-MIB-SMIv2", "dmmCA2MessageID"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2Message"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2MessageArgs"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2AlertStatus"),
        ("DELL-MM-MIB-SMIv2", "dmmDeviceServiceTag"),
        ("DELL-MM-MIB-SMIv2", "dmmCategoryName"),
        ("DELL-MM-MIB-SMIv2", "dmmSubCategoryName"),
        ("DELL-MM-MIB-SMIv2", "dmmSeverity"))
)
if mibBuilder.loadTexts:
    iDRAC10635alertAutoDiscoveryInformation.setStatus(
        "current"
    )

iDRAC10770alertNetworkConfigurationWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 7, 0, 10770)
)
iDRAC10770alertNetworkConfigurationWarning.setObjects(
      *(("DELL-MM-MIB-SMIv2", "dmmCA2MessageID"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2Message"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2MessageArgs"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2AlertStatus"),
        ("DELL-MM-MIB-SMIv2", "dmmDeviceServiceTag"),
        ("DELL-MM-MIB-SMIv2", "dmmCategoryName"),
        ("DELL-MM-MIB-SMIv2", "dmmSubCategoryName"),
        ("DELL-MM-MIB-SMIv2", "dmmSeverity"))
)
if mibBuilder.loadTexts:
    iDRAC10770alertNetworkConfigurationWarning.setStatus(
        "current"
    )

iDRAC10771alertNetworkConfigurationInformation = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 7, 0, 10771)
)
iDRAC10771alertNetworkConfigurationInformation.setObjects(
      *(("DELL-MM-MIB-SMIv2", "dmmCA2MessageID"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2Message"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2MessageArgs"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2AlertStatus"),
        ("DELL-MM-MIB-SMIv2", "dmmDeviceServiceTag"),
        ("DELL-MM-MIB-SMIv2", "dmmCategoryName"),
        ("DELL-MM-MIB-SMIv2", "dmmSubCategoryName"),
        ("DELL-MM-MIB-SMIv2", "dmmSeverity"))
)
if mibBuilder.loadTexts:
    iDRAC10771alertNetworkConfigurationInformation.setStatus(
        "current"
    )

iDRAC11274alertSDKConfigurationWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 7, 0, 11274)
)
iDRAC11274alertSDKConfigurationWarning.setObjects(
      *(("DELL-MM-MIB-SMIv2", "dmmCA2MessageID"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2Message"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2MessageArgs"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2AlertStatus"),
        ("DELL-MM-MIB-SMIv2", "dmmDeviceServiceTag"),
        ("DELL-MM-MIB-SMIv2", "dmmCategoryName"),
        ("DELL-MM-MIB-SMIv2", "dmmSubCategoryName"),
        ("DELL-MM-MIB-SMIv2", "dmmSeverity"))
)
if mibBuilder.loadTexts:
    iDRAC11274alertSDKConfigurationWarning.setStatus(
        "current"
    )

iDRAC11275alertSDKConfigurationInformation = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 7, 0, 11275)
)
iDRAC11275alertSDKConfigurationInformation.setObjects(
      *(("DELL-MM-MIB-SMIv2", "dmmCA2MessageID"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2Message"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2MessageArgs"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2AlertStatus"),
        ("DELL-MM-MIB-SMIv2", "dmmDeviceServiceTag"),
        ("DELL-MM-MIB-SMIv2", "dmmCategoryName"),
        ("DELL-MM-MIB-SMIv2", "dmmSubCategoryName"),
        ("DELL-MM-MIB-SMIv2", "dmmSeverity"))
)
if mibBuilder.loadTexts:
    iDRAC11275alertSDKConfigurationInformation.setStatus(
        "current"
    )

nwIOM980021AlertFabricInformational = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 8, 0, 980021)
)
nwIOM980021AlertFabricInformational.setObjects(
      *(("DELL-MM-MIB-SMIv2", "dmmCA2MessageID"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2Message"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2MessageArgs"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2AlertStatus"),
        ("DELL-MM-MIB-SMIv2", "dmmDeviceServiceTag"),
        ("DELL-MM-MIB-SMIv2", "dmmCategoryName"),
        ("DELL-MM-MIB-SMIv2", "dmmSubCategoryName"),
        ("DELL-MM-MIB-SMIv2", "dmmSeverity"))
)
if mibBuilder.loadTexts:
    nwIOM980021AlertFabricInformational.setStatus(
        "current"
    )

nwIOM980022AlertFabricWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 8, 0, 980022)
)
nwIOM980022AlertFabricWarning.setObjects(
      *(("DELL-MM-MIB-SMIv2", "dmmCA2MessageID"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2Message"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2MessageArgs"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2AlertStatus"),
        ("DELL-MM-MIB-SMIv2", "dmmDeviceServiceTag"),
        ("DELL-MM-MIB-SMIv2", "dmmCategoryName"),
        ("DELL-MM-MIB-SMIv2", "dmmSubCategoryName"),
        ("DELL-MM-MIB-SMIv2", "dmmSeverity"))
)
if mibBuilder.loadTexts:
    nwIOM980022AlertFabricWarning.setStatus(
        "current"
    )

nwIOM980023AlertFabricCritical = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 8, 0, 980023)
)
nwIOM980023AlertFabricCritical.setObjects(
      *(("DELL-MM-MIB-SMIv2", "dmmCA2MessageID"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2Message"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2MessageArgs"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2AlertStatus"),
        ("DELL-MM-MIB-SMIv2", "dmmDeviceServiceTag"),
        ("DELL-MM-MIB-SMIv2", "dmmCategoryName"),
        ("DELL-MM-MIB-SMIv2", "dmmSubCategoryName"),
        ("DELL-MM-MIB-SMIv2", "dmmSeverity"))
)
if mibBuilder.loadTexts:
    nwIOM980023AlertFabricCritical.setStatus(
        "current"
    )

nwIOM980024AlertFabricInformational = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 8, 0, 980024)
)
nwIOM980024AlertFabricInformational.setObjects(
      *(("DELL-MM-MIB-SMIv2", "dmmCA2MessageID"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2Message"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2MessageArgs"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2AlertStatus"),
        ("DELL-MM-MIB-SMIv2", "dmmDeviceServiceTag"),
        ("DELL-MM-MIB-SMIv2", "dmmCategoryName"),
        ("DELL-MM-MIB-SMIv2", "dmmSubCategoryName"),
        ("DELL-MM-MIB-SMIv2", "dmmSeverity"))
)
if mibBuilder.loadTexts:
    nwIOM980024AlertFabricInformational.setStatus(
        "current"
    )

nwIOM980025AlertFabricWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 8, 0, 980025)
)
nwIOM980025AlertFabricWarning.setObjects(
      *(("DELL-MM-MIB-SMIv2", "dmmCA2MessageID"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2Message"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2MessageArgs"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2AlertStatus"),
        ("DELL-MM-MIB-SMIv2", "dmmDeviceServiceTag"),
        ("DELL-MM-MIB-SMIv2", "dmmCategoryName"),
        ("DELL-MM-MIB-SMIv2", "dmmSubCategoryName"),
        ("DELL-MM-MIB-SMIv2", "dmmSeverity"))
)
if mibBuilder.loadTexts:
    nwIOM980025AlertFabricWarning.setStatus(
        "current"
    )

nwIOM980026AlertFabricInformational = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 8, 0, 980026)
)
nwIOM980026AlertFabricInformational.setObjects(
      *(("DELL-MM-MIB-SMIv2", "dmmCA2MessageID"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2Message"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2MessageArgs"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2AlertStatus"),
        ("DELL-MM-MIB-SMIv2", "dmmDeviceServiceTag"),
        ("DELL-MM-MIB-SMIv2", "dmmCategoryName"),
        ("DELL-MM-MIB-SMIv2", "dmmSubCategoryName"),
        ("DELL-MM-MIB-SMIv2", "dmmSeverity"))
)
if mibBuilder.loadTexts:
    nwIOM980026AlertFabricInformational.setStatus(
        "current"
    )

nwIOM980027AlertFabricInformational = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 8, 0, 980027)
)
nwIOM980027AlertFabricInformational.setObjects(
      *(("DELL-MM-MIB-SMIv2", "dmmCA2MessageID"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2Message"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2MessageArgs"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2AlertStatus"),
        ("DELL-MM-MIB-SMIv2", "dmmDeviceServiceTag"),
        ("DELL-MM-MIB-SMIv2", "dmmCategoryName"),
        ("DELL-MM-MIB-SMIv2", "dmmSubCategoryName"),
        ("DELL-MM-MIB-SMIv2", "dmmSeverity"))
)
if mibBuilder.loadTexts:
    nwIOM980027AlertFabricInformational.setStatus(
        "current"
    )

nwIOM980028AlertFabricInformational = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 8, 0, 980028)
)
nwIOM980028AlertFabricInformational.setObjects(
      *(("DELL-MM-MIB-SMIv2", "dmmCA2MessageID"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2Message"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2MessageArgs"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2AlertStatus"),
        ("DELL-MM-MIB-SMIv2", "dmmDeviceServiceTag"),
        ("DELL-MM-MIB-SMIv2", "dmmCategoryName"),
        ("DELL-MM-MIB-SMIv2", "dmmSubCategoryName"),
        ("DELL-MM-MIB-SMIv2", "dmmSeverity"))
)
if mibBuilder.loadTexts:
    nwIOM980028AlertFabricInformational.setStatus(
        "current"
    )

nwIOM980029AlertFabricCritical = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 8, 0, 980029)
)
nwIOM980029AlertFabricCritical.setObjects(
      *(("DELL-MM-MIB-SMIv2", "dmmCA2MessageID"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2Message"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2MessageArgs"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2AlertStatus"),
        ("DELL-MM-MIB-SMIv2", "dmmDeviceServiceTag"),
        ("DELL-MM-MIB-SMIv2", "dmmCategoryName"),
        ("DELL-MM-MIB-SMIv2", "dmmSubCategoryName"),
        ("DELL-MM-MIB-SMIv2", "dmmSeverity"))
)
if mibBuilder.loadTexts:
    nwIOM980029AlertFabricCritical.setStatus(
        "current"
    )

nwIOM980030AlertFabricInformational = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 8, 0, 980030)
)
nwIOM980030AlertFabricInformational.setObjects(
      *(("DELL-MM-MIB-SMIv2", "dmmCA2MessageID"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2Message"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2MessageArgs"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2AlertStatus"),
        ("DELL-MM-MIB-SMIv2", "dmmDeviceServiceTag"),
        ("DELL-MM-MIB-SMIv2", "dmmCategoryName"),
        ("DELL-MM-MIB-SMIv2", "dmmSubCategoryName"),
        ("DELL-MM-MIB-SMIv2", "dmmSeverity"))
)
if mibBuilder.loadTexts:
    nwIOM980030AlertFabricInformational.setStatus(
        "current"
    )

nwIOM980031AlertFabricInformational = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 8, 0, 980031)
)
nwIOM980031AlertFabricInformational.setObjects(
      *(("DELL-MM-MIB-SMIv2", "dmmCA2MessageID"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2Message"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2MessageArgs"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2AlertStatus"),
        ("DELL-MM-MIB-SMIv2", "dmmDeviceServiceTag"),
        ("DELL-MM-MIB-SMIv2", "dmmCategoryName"),
        ("DELL-MM-MIB-SMIv2", "dmmSubCategoryName"),
        ("DELL-MM-MIB-SMIv2", "dmmSeverity"))
)
if mibBuilder.loadTexts:
    nwIOM980031AlertFabricInformational.setStatus(
        "current"
    )

nwIOM980032AlertFabricInformational = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 8, 0, 980032)
)
nwIOM980032AlertFabricInformational.setObjects(
      *(("DELL-MM-MIB-SMIv2", "dmmCA2MessageID"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2Message"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2MessageArgs"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2AlertStatus"),
        ("DELL-MM-MIB-SMIv2", "dmmDeviceServiceTag"),
        ("DELL-MM-MIB-SMIv2", "dmmCategoryName"),
        ("DELL-MM-MIB-SMIv2", "dmmSubCategoryName"),
        ("DELL-MM-MIB-SMIv2", "dmmSeverity"))
)
if mibBuilder.loadTexts:
    nwIOM980032AlertFabricInformational.setStatus(
        "current"
    )

nwIOM990001AlertInterfaceInformational = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 8, 0, 990001)
)
nwIOM990001AlertInterfaceInformational.setObjects(
      *(("DELL-MM-MIB-SMIv2", "dmmCA2MessageID"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2Message"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2MessageArgs"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2AlertStatus"),
        ("DELL-MM-MIB-SMIv2", "dmmDeviceServiceTag"),
        ("DELL-MM-MIB-SMIv2", "dmmCategoryName"),
        ("DELL-MM-MIB-SMIv2", "dmmSubCategoryName"),
        ("DELL-MM-MIB-SMIv2", "dmmSeverity"))
)
if mibBuilder.loadTexts:
    nwIOM990001AlertInterfaceInformational.setStatus(
        "current"
    )

nwIOM990002AlertInterfaceWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 8, 0, 990002)
)
nwIOM990002AlertInterfaceWarning.setObjects(
      *(("DELL-MM-MIB-SMIv2", "dmmCA2MessageID"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2Message"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2MessageArgs"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2AlertStatus"),
        ("DELL-MM-MIB-SMIv2", "dmmDeviceServiceTag"),
        ("DELL-MM-MIB-SMIv2", "dmmCategoryName"),
        ("DELL-MM-MIB-SMIv2", "dmmSubCategoryName"),
        ("DELL-MM-MIB-SMIv2", "dmmSeverity"))
)
if mibBuilder.loadTexts:
    nwIOM990002AlertInterfaceWarning.setStatus(
        "current"
    )

nwIOM1000001AlertLinkInformational = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 8, 0, 1000001)
)
nwIOM1000001AlertLinkInformational.setObjects(
      *(("DELL-MM-MIB-SMIv2", "dmmCA2MessageID"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2Message"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2MessageArgs"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2AlertStatus"),
        ("DELL-MM-MIB-SMIv2", "dmmDeviceServiceTag"),
        ("DELL-MM-MIB-SMIv2", "dmmCategoryName"),
        ("DELL-MM-MIB-SMIv2", "dmmSubCategoryName"),
        ("DELL-MM-MIB-SMIv2", "dmmSeverity"))
)
if mibBuilder.loadTexts:
    nwIOM1000001AlertLinkInformational.setStatus(
        "current"
    )

nwIOM1000002AlertLinkWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 8, 0, 1000002)
)
nwIOM1000002AlertLinkWarning.setObjects(
      *(("DELL-MM-MIB-SMIv2", "dmmCA2MessageID"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2Message"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2MessageArgs"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2AlertStatus"),
        ("DELL-MM-MIB-SMIv2", "dmmDeviceServiceTag"),
        ("DELL-MM-MIB-SMIv2", "dmmCategoryName"),
        ("DELL-MM-MIB-SMIv2", "dmmSubCategoryName"),
        ("DELL-MM-MIB-SMIv2", "dmmSeverity"))
)
if mibBuilder.loadTexts:
    nwIOM1000002AlertLinkWarning.setStatus(
        "current"
    )

nwIOM1010001AlertNodeInformational = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 8, 0, 1010001)
)
nwIOM1010001AlertNodeInformational.setObjects(
      *(("DELL-MM-MIB-SMIv2", "dmmCA2MessageID"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2Message"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2MessageArgs"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2AlertStatus"),
        ("DELL-MM-MIB-SMIv2", "dmmDeviceServiceTag"),
        ("DELL-MM-MIB-SMIv2", "dmmCategoryName"),
        ("DELL-MM-MIB-SMIv2", "dmmSubCategoryName"),
        ("DELL-MM-MIB-SMIv2", "dmmSeverity"))
)
if mibBuilder.loadTexts:
    nwIOM1010001AlertNodeInformational.setStatus(
        "current"
    )

nwIOM1010002AlertNodeWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 8, 0, 1010002)
)
nwIOM1010002AlertNodeWarning.setObjects(
      *(("DELL-MM-MIB-SMIv2", "dmmCA2MessageID"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2Message"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2MessageArgs"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2AlertStatus"),
        ("DELL-MM-MIB-SMIv2", "dmmDeviceServiceTag"),
        ("DELL-MM-MIB-SMIv2", "dmmCategoryName"),
        ("DELL-MM-MIB-SMIv2", "dmmSubCategoryName"),
        ("DELL-MM-MIB-SMIv2", "dmmSeverity"))
)
if mibBuilder.loadTexts:
    nwIOM1010002AlertNodeWarning.setStatus(
        "current"
    )

nwIOM1010003AlertNodeInformational = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 8, 0, 1010003)
)
nwIOM1010003AlertNodeInformational.setObjects(
      *(("DELL-MM-MIB-SMIv2", "dmmCA2MessageID"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2Message"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2MessageArgs"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2AlertStatus"),
        ("DELL-MM-MIB-SMIv2", "dmmDeviceServiceTag"),
        ("DELL-MM-MIB-SMIv2", "dmmCategoryName"),
        ("DELL-MM-MIB-SMIv2", "dmmSubCategoryName"),
        ("DELL-MM-MIB-SMIv2", "dmmSeverity"))
)
if mibBuilder.loadTexts:
    nwIOM1010003AlertNodeInformational.setStatus(
        "current"
    )

nwIOM1010004AlertNodeWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 8, 0, 1010004)
)
nwIOM1010004AlertNodeWarning.setObjects(
      *(("DELL-MM-MIB-SMIv2", "dmmCA2MessageID"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2Message"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2MessageArgs"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2AlertStatus"),
        ("DELL-MM-MIB-SMIv2", "dmmDeviceServiceTag"),
        ("DELL-MM-MIB-SMIv2", "dmmCategoryName"),
        ("DELL-MM-MIB-SMIv2", "dmmSubCategoryName"),
        ("DELL-MM-MIB-SMIv2", "dmmSeverity"))
)
if mibBuilder.loadTexts:
    nwIOM1010004AlertNodeWarning.setStatus(
        "current"
    )

nwIOM1010005AlertNodeInformational = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 8, 0, 1010005)
)
nwIOM1010005AlertNodeInformational.setObjects(
      *(("DELL-MM-MIB-SMIv2", "dmmCA2MessageID"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2Message"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2MessageArgs"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2AlertStatus"),
        ("DELL-MM-MIB-SMIv2", "dmmDeviceServiceTag"),
        ("DELL-MM-MIB-SMIv2", "dmmCategoryName"),
        ("DELL-MM-MIB-SMIv2", "dmmSubCategoryName"),
        ("DELL-MM-MIB-SMIv2", "dmmSeverity"))
)
if mibBuilder.loadTexts:
    nwIOM1010005AlertNodeInformational.setStatus(
        "current"
    )

nwIOM1010006AlertNodeWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 8, 0, 1010006)
)
nwIOM1010006AlertNodeWarning.setObjects(
      *(("DELL-MM-MIB-SMIv2", "dmmCA2MessageID"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2Message"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2MessageArgs"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2AlertStatus"),
        ("DELL-MM-MIB-SMIv2", "dmmDeviceServiceTag"),
        ("DELL-MM-MIB-SMIv2", "dmmCategoryName"),
        ("DELL-MM-MIB-SMIv2", "dmmSubCategoryName"),
        ("DELL-MM-MIB-SMIv2", "dmmSeverity"))
)
if mibBuilder.loadTexts:
    nwIOM1010006AlertNodeWarning.setStatus(
        "current"
    )

nwIOM1010007AlertNodeWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 8, 0, 1010007)
)
nwIOM1010007AlertNodeWarning.setObjects(
      *(("DELL-MM-MIB-SMIv2", "dmmCA2MessageID"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2Message"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2MessageArgs"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2AlertStatus"),
        ("DELL-MM-MIB-SMIv2", "dmmDeviceServiceTag"),
        ("DELL-MM-MIB-SMIv2", "dmmCategoryName"),
        ("DELL-MM-MIB-SMIv2", "dmmSubCategoryName"),
        ("DELL-MM-MIB-SMIv2", "dmmSeverity"))
)
if mibBuilder.loadTexts:
    nwIOM1010007AlertNodeWarning.setStatus(
        "current"
    )

nwIOM1020001AlertServerInformational = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 8, 0, 1020001)
)
nwIOM1020001AlertServerInformational.setObjects(
      *(("DELL-MM-MIB-SMIv2", "dmmCA2MessageID"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2Message"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2MessageArgs"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2AlertStatus"),
        ("DELL-MM-MIB-SMIv2", "dmmDeviceServiceTag"),
        ("DELL-MM-MIB-SMIv2", "dmmCategoryName"),
        ("DELL-MM-MIB-SMIv2", "dmmSubCategoryName"),
        ("DELL-MM-MIB-SMIv2", "dmmSeverity"))
)
if mibBuilder.loadTexts:
    nwIOM1020001AlertServerInformational.setStatus(
        "current"
    )

nwIOM1020002AlertServerWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 8, 0, 1020002)
)
nwIOM1020002AlertServerWarning.setObjects(
      *(("DELL-MM-MIB-SMIv2", "dmmCA2MessageID"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2Message"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2MessageArgs"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2AlertStatus"),
        ("DELL-MM-MIB-SMIv2", "dmmDeviceServiceTag"),
        ("DELL-MM-MIB-SMIv2", "dmmCategoryName"),
        ("DELL-MM-MIB-SMIv2", "dmmSubCategoryName"),
        ("DELL-MM-MIB-SMIv2", "dmmSeverity"))
)
if mibBuilder.loadTexts:
    nwIOM1020002AlertServerWarning.setStatus(
        "current"
    )

nwIOM1020003AlertServerInformational = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 8, 0, 1020003)
)
nwIOM1020003AlertServerInformational.setObjects(
      *(("DELL-MM-MIB-SMIv2", "dmmCA2MessageID"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2Message"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2MessageArgs"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2AlertStatus"),
        ("DELL-MM-MIB-SMIv2", "dmmDeviceServiceTag"),
        ("DELL-MM-MIB-SMIv2", "dmmCategoryName"),
        ("DELL-MM-MIB-SMIv2", "dmmSubCategoryName"),
        ("DELL-MM-MIB-SMIv2", "dmmSeverity"))
)
if mibBuilder.loadTexts:
    nwIOM1020003AlertServerInformational.setStatus(
        "current"
    )

nwIOM1020004AlertServerWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 8, 0, 1020004)
)
nwIOM1020004AlertServerWarning.setObjects(
      *(("DELL-MM-MIB-SMIv2", "dmmCA2MessageID"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2Message"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2MessageArgs"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2AlertStatus"),
        ("DELL-MM-MIB-SMIv2", "dmmDeviceServiceTag"),
        ("DELL-MM-MIB-SMIv2", "dmmCategoryName"),
        ("DELL-MM-MIB-SMIv2", "dmmSubCategoryName"),
        ("DELL-MM-MIB-SMIv2", "dmmSeverity"))
)
if mibBuilder.loadTexts:
    nwIOM1020004AlertServerWarning.setStatus(
        "current"
    )

nwIOM1020005AlertServerInformational = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 8, 0, 1020005)
)
nwIOM1020005AlertServerInformational.setObjects(
      *(("DELL-MM-MIB-SMIv2", "dmmCA2MessageID"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2Message"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2MessageArgs"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2AlertStatus"),
        ("DELL-MM-MIB-SMIv2", "dmmDeviceServiceTag"),
        ("DELL-MM-MIB-SMIv2", "dmmCategoryName"),
        ("DELL-MM-MIB-SMIv2", "dmmSubCategoryName"),
        ("DELL-MM-MIB-SMIv2", "dmmSeverity"))
)
if mibBuilder.loadTexts:
    nwIOM1020005AlertServerInformational.setStatus(
        "current"
    )

nwIOM1020006AlertServerWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 8, 0, 1020006)
)
nwIOM1020006AlertServerWarning.setObjects(
      *(("DELL-MM-MIB-SMIv2", "dmmCA2MessageID"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2Message"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2MessageArgs"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2AlertStatus"),
        ("DELL-MM-MIB-SMIv2", "dmmDeviceServiceTag"),
        ("DELL-MM-MIB-SMIv2", "dmmCategoryName"),
        ("DELL-MM-MIB-SMIv2", "dmmSubCategoryName"),
        ("DELL-MM-MIB-SMIv2", "dmmSeverity"))
)
if mibBuilder.loadTexts:
    nwIOM1020006AlertServerWarning.setStatus(
        "current"
    )

nwIOM1020007AlertServerInformational = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 8, 0, 1020007)
)
nwIOM1020007AlertServerInformational.setObjects(
      *(("DELL-MM-MIB-SMIv2", "dmmCA2MessageID"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2Message"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2MessageArgs"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2AlertStatus"),
        ("DELL-MM-MIB-SMIv2", "dmmDeviceServiceTag"),
        ("DELL-MM-MIB-SMIv2", "dmmCategoryName"),
        ("DELL-MM-MIB-SMIv2", "dmmSubCategoryName"),
        ("DELL-MM-MIB-SMIv2", "dmmSeverity"))
)
if mibBuilder.loadTexts:
    nwIOM1020007AlertServerInformational.setStatus(
        "current"
    )

nwIOM1020008AlertServerWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 8, 0, 1020008)
)
nwIOM1020008AlertServerWarning.setObjects(
      *(("DELL-MM-MIB-SMIv2", "dmmCA2MessageID"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2Message"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2MessageArgs"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2AlertStatus"),
        ("DELL-MM-MIB-SMIv2", "dmmDeviceServiceTag"),
        ("DELL-MM-MIB-SMIv2", "dmmCategoryName"),
        ("DELL-MM-MIB-SMIv2", "dmmSubCategoryName"),
        ("DELL-MM-MIB-SMIv2", "dmmSeverity"))
)
if mibBuilder.loadTexts:
    nwIOM1020008AlertServerWarning.setStatus(
        "current"
    )

nwIOM1052505AlertRESTInformational = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 8, 0, 1052505)
)
nwIOM1052505AlertRESTInformational.setObjects(
      *(("DELL-MM-MIB-SMIv2", "dmmCA2MessageID"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2Message"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2MessageArgs"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2AlertStatus"),
        ("DELL-MM-MIB-SMIv2", "dmmDeviceServiceTag"),
        ("DELL-MM-MIB-SMIv2", "dmmCategoryName"),
        ("DELL-MM-MIB-SMIv2", "dmmSubCategoryName"),
        ("DELL-MM-MIB-SMIv2", "dmmSeverity"))
)
if mibBuilder.loadTexts:
    nwIOM1052505AlertRESTInformational.setStatus(
        "current"
    )

nwIOM1052506AlertRESTInformational = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 8, 0, 1052506)
)
nwIOM1052506AlertRESTInformational.setObjects(
      *(("DELL-MM-MIB-SMIv2", "dmmCA2MessageID"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2Message"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2MessageArgs"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2AlertStatus"),
        ("DELL-MM-MIB-SMIv2", "dmmDeviceServiceTag"),
        ("DELL-MM-MIB-SMIv2", "dmmCategoryName"),
        ("DELL-MM-MIB-SMIv2", "dmmSubCategoryName"),
        ("DELL-MM-MIB-SMIv2", "dmmSeverity"))
)
if mibBuilder.loadTexts:
    nwIOM1052506AlertRESTInformational.setStatus(
        "current"
    )

sasIOM1120001AlertHealthCritical = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 9, 0, 1120001)
)
sasIOM1120001AlertHealthCritical.setObjects(
      *(("DELL-MM-MIB-SMIv2", "dmmCA2MessageID"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2Message"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2MessageArgs"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2AlertStatus"),
        ("DELL-MM-MIB-SMIv2", "dmmDeviceServiceTag"),
        ("DELL-MM-MIB-SMIv2", "dmmCategoryName"),
        ("DELL-MM-MIB-SMIv2", "dmmSubCategoryName"),
        ("DELL-MM-MIB-SMIv2", "dmmSeverity"))
)
if mibBuilder.loadTexts:
    sasIOM1120001AlertHealthCritical.setStatus(
        "current"
    )

sasIOM1120002AlertHealthInformational = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 9, 0, 1120002)
)
sasIOM1120002AlertHealthInformational.setObjects(
      *(("DELL-MM-MIB-SMIv2", "dmmCA2MessageID"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2Message"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2MessageArgs"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2AlertStatus"),
        ("DELL-MM-MIB-SMIv2", "dmmDeviceServiceTag"),
        ("DELL-MM-MIB-SMIv2", "dmmCategoryName"),
        ("DELL-MM-MIB-SMIv2", "dmmSubCategoryName"),
        ("DELL-MM-MIB-SMIv2", "dmmSeverity"))
)
if mibBuilder.loadTexts:
    sasIOM1120002AlertHealthInformational.setStatus(
        "current"
    )

sasIOM1120003AlertHealthCritical = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 9, 0, 1120003)
)
sasIOM1120003AlertHealthCritical.setObjects(
      *(("DELL-MM-MIB-SMIv2", "dmmCA2MessageID"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2Message"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2MessageArgs"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2AlertStatus"),
        ("DELL-MM-MIB-SMIv2", "dmmDeviceServiceTag"),
        ("DELL-MM-MIB-SMIv2", "dmmCategoryName"),
        ("DELL-MM-MIB-SMIv2", "dmmSubCategoryName"),
        ("DELL-MM-MIB-SMIv2", "dmmSeverity"))
)
if mibBuilder.loadTexts:
    sasIOM1120003AlertHealthCritical.setStatus(
        "current"
    )

sasIOM1120004AlertHealthInformational = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 9, 0, 1120004)
)
sasIOM1120004AlertHealthInformational.setObjects(
      *(("DELL-MM-MIB-SMIv2", "dmmCA2MessageID"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2Message"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2MessageArgs"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2AlertStatus"),
        ("DELL-MM-MIB-SMIv2", "dmmDeviceServiceTag"),
        ("DELL-MM-MIB-SMIv2", "dmmCategoryName"),
        ("DELL-MM-MIB-SMIv2", "dmmSubCategoryName"),
        ("DELL-MM-MIB-SMIv2", "dmmSeverity"))
)
if mibBuilder.loadTexts:
    sasIOM1120004AlertHealthInformational.setStatus(
        "current"
    )

sasIOM1120005AlertHealthWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 9, 0, 1120005)
)
sasIOM1120005AlertHealthWarning.setObjects(
      *(("DELL-MM-MIB-SMIv2", "dmmCA2MessageID"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2Message"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2MessageArgs"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2AlertStatus"),
        ("DELL-MM-MIB-SMIv2", "dmmDeviceServiceTag"),
        ("DELL-MM-MIB-SMIv2", "dmmCategoryName"),
        ("DELL-MM-MIB-SMIv2", "dmmSubCategoryName"),
        ("DELL-MM-MIB-SMIv2", "dmmSeverity"))
)
if mibBuilder.loadTexts:
    sasIOM1120005AlertHealthWarning.setStatus(
        "current"
    )

sasIOM1120006AlertHealthInformational = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 9, 0, 1120006)
)
sasIOM1120006AlertHealthInformational.setObjects(
      *(("DELL-MM-MIB-SMIv2", "dmmCA2MessageID"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2Message"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2MessageArgs"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2AlertStatus"),
        ("DELL-MM-MIB-SMIv2", "dmmDeviceServiceTag"),
        ("DELL-MM-MIB-SMIv2", "dmmCategoryName"),
        ("DELL-MM-MIB-SMIv2", "dmmSubCategoryName"),
        ("DELL-MM-MIB-SMIv2", "dmmSeverity"))
)
if mibBuilder.loadTexts:
    sasIOM1120006AlertHealthInformational.setStatus(
        "current"
    )

sasIOM1120007AlertHealthWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 9, 0, 1120007)
)
sasIOM1120007AlertHealthWarning.setObjects(
      *(("DELL-MM-MIB-SMIv2", "dmmCA2MessageID"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2Message"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2MessageArgs"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2AlertStatus"),
        ("DELL-MM-MIB-SMIv2", "dmmDeviceServiceTag"),
        ("DELL-MM-MIB-SMIv2", "dmmCategoryName"),
        ("DELL-MM-MIB-SMIv2", "dmmSubCategoryName"),
        ("DELL-MM-MIB-SMIv2", "dmmSeverity"))
)
if mibBuilder.loadTexts:
    sasIOM1120007AlertHealthWarning.setStatus(
        "current"
    )

sasIOM1120008AlertHealthWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 9, 0, 1120008)
)
sasIOM1120008AlertHealthWarning.setObjects(
      *(("DELL-MM-MIB-SMIv2", "dmmCA2MessageID"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2Message"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2MessageArgs"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2AlertStatus"),
        ("DELL-MM-MIB-SMIv2", "dmmDeviceServiceTag"),
        ("DELL-MM-MIB-SMIv2", "dmmCategoryName"),
        ("DELL-MM-MIB-SMIv2", "dmmSubCategoryName"),
        ("DELL-MM-MIB-SMIv2", "dmmSeverity"))
)
if mibBuilder.loadTexts:
    sasIOM1120008AlertHealthWarning.setStatus(
        "current"
    )

sasIOM1120009AlertHealthInformational = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 9, 0, 1120009)
)
sasIOM1120009AlertHealthInformational.setObjects(
      *(("DELL-MM-MIB-SMIv2", "dmmCA2MessageID"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2Message"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2MessageArgs"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2AlertStatus"),
        ("DELL-MM-MIB-SMIv2", "dmmDeviceServiceTag"),
        ("DELL-MM-MIB-SMIv2", "dmmCategoryName"),
        ("DELL-MM-MIB-SMIv2", "dmmSubCategoryName"),
        ("DELL-MM-MIB-SMIv2", "dmmSeverity"))
)
if mibBuilder.loadTexts:
    sasIOM1120009AlertHealthInformational.setStatus(
        "current"
    )

sasIOM1120010AlertHealthWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 9, 0, 1120010)
)
sasIOM1120010AlertHealthWarning.setObjects(
      *(("DELL-MM-MIB-SMIv2", "dmmCA2MessageID"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2Message"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2MessageArgs"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2AlertStatus"),
        ("DELL-MM-MIB-SMIv2", "dmmDeviceServiceTag"),
        ("DELL-MM-MIB-SMIv2", "dmmCategoryName"),
        ("DELL-MM-MIB-SMIv2", "dmmSubCategoryName"),
        ("DELL-MM-MIB-SMIv2", "dmmSeverity"))
)
if mibBuilder.loadTexts:
    sasIOM1120010AlertHealthWarning.setStatus(
        "current"
    )

sasIOM1120011AlertHealthInformational = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 9, 0, 1120011)
)
sasIOM1120011AlertHealthInformational.setObjects(
      *(("DELL-MM-MIB-SMIv2", "dmmCA2MessageID"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2Message"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2MessageArgs"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2AlertStatus"),
        ("DELL-MM-MIB-SMIv2", "dmmDeviceServiceTag"),
        ("DELL-MM-MIB-SMIv2", "dmmCategoryName"),
        ("DELL-MM-MIB-SMIv2", "dmmSubCategoryName"),
        ("DELL-MM-MIB-SMIv2", "dmmSeverity"))
)
if mibBuilder.loadTexts:
    sasIOM1120011AlertHealthInformational.setStatus(
        "current"
    )

sasIOM1120012AlertHealthWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 9, 0, 1120012)
)
sasIOM1120012AlertHealthWarning.setObjects(
      *(("DELL-MM-MIB-SMIv2", "dmmCA2MessageID"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2Message"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2MessageArgs"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2AlertStatus"),
        ("DELL-MM-MIB-SMIv2", "dmmDeviceServiceTag"),
        ("DELL-MM-MIB-SMIv2", "dmmCategoryName"),
        ("DELL-MM-MIB-SMIv2", "dmmSubCategoryName"),
        ("DELL-MM-MIB-SMIv2", "dmmSeverity"))
)
if mibBuilder.loadTexts:
    sasIOM1120012AlertHealthWarning.setStatus(
        "current"
    )

sasIOM1120013AlertHealthInformational = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 9, 0, 1120013)
)
sasIOM1120013AlertHealthInformational.setObjects(
      *(("DELL-MM-MIB-SMIv2", "dmmCA2MessageID"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2Message"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2MessageArgs"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2AlertStatus"),
        ("DELL-MM-MIB-SMIv2", "dmmDeviceServiceTag"),
        ("DELL-MM-MIB-SMIv2", "dmmCategoryName"),
        ("DELL-MM-MIB-SMIv2", "dmmSubCategoryName"),
        ("DELL-MM-MIB-SMIv2", "dmmSeverity"))
)
if mibBuilder.loadTexts:
    sasIOM1120013AlertHealthInformational.setStatus(
        "current"
    )

sasIOM1120016AlertHealthWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 9, 0, 1120016)
)
sasIOM1120016AlertHealthWarning.setObjects(
      *(("DELL-MM-MIB-SMIv2", "dmmCA2MessageID"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2Message"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2MessageArgs"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2AlertStatus"),
        ("DELL-MM-MIB-SMIv2", "dmmDeviceServiceTag"),
        ("DELL-MM-MIB-SMIv2", "dmmCategoryName"),
        ("DELL-MM-MIB-SMIv2", "dmmSubCategoryName"),
        ("DELL-MM-MIB-SMIv2", "dmmSeverity"))
)
if mibBuilder.loadTexts:
    sasIOM1120016AlertHealthWarning.setStatus(
        "current"
    )

sasIOM1120017AlertHealthInformational = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 9, 0, 1120017)
)
sasIOM1120017AlertHealthInformational.setObjects(
      *(("DELL-MM-MIB-SMIv2", "dmmCA2MessageID"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2Message"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2MessageArgs"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2AlertStatus"),
        ("DELL-MM-MIB-SMIv2", "dmmDeviceServiceTag"),
        ("DELL-MM-MIB-SMIv2", "dmmCategoryName"),
        ("DELL-MM-MIB-SMIv2", "dmmSubCategoryName"),
        ("DELL-MM-MIB-SMIv2", "dmmSeverity"))
)
if mibBuilder.loadTexts:
    sasIOM1120017AlertHealthInformational.setStatus(
        "current"
    )

sasIOM1120018AlertHealthWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 9, 0, 1120018)
)
sasIOM1120018AlertHealthWarning.setObjects(
      *(("DELL-MM-MIB-SMIv2", "dmmCA2MessageID"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2Message"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2MessageArgs"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2AlertStatus"),
        ("DELL-MM-MIB-SMIv2", "dmmDeviceServiceTag"),
        ("DELL-MM-MIB-SMIv2", "dmmCategoryName"),
        ("DELL-MM-MIB-SMIv2", "dmmSubCategoryName"),
        ("DELL-MM-MIB-SMIv2", "dmmSeverity"))
)
if mibBuilder.loadTexts:
    sasIOM1120018AlertHealthWarning.setStatus(
        "current"
    )

sasIOM1120019AlertHealthInformational = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 9, 0, 1120019)
)
sasIOM1120019AlertHealthInformational.setObjects(
      *(("DELL-MM-MIB-SMIv2", "dmmCA2MessageID"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2Message"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2MessageArgs"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2AlertStatus"),
        ("DELL-MM-MIB-SMIv2", "dmmDeviceServiceTag"),
        ("DELL-MM-MIB-SMIv2", "dmmCategoryName"),
        ("DELL-MM-MIB-SMIv2", "dmmSubCategoryName"),
        ("DELL-MM-MIB-SMIv2", "dmmSeverity"))
)
if mibBuilder.loadTexts:
    sasIOM1120019AlertHealthInformational.setStatus(
        "current"
    )

sasIOM1120020AlertHealthInformational = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 9, 0, 1120020)
)
sasIOM1120020AlertHealthInformational.setObjects(
      *(("DELL-MM-MIB-SMIv2", "dmmCA2MessageID"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2Message"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2MessageArgs"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2AlertStatus"),
        ("DELL-MM-MIB-SMIv2", "dmmDeviceServiceTag"),
        ("DELL-MM-MIB-SMIv2", "dmmCategoryName"),
        ("DELL-MM-MIB-SMIv2", "dmmSubCategoryName"),
        ("DELL-MM-MIB-SMIv2", "dmmSeverity"))
)
if mibBuilder.loadTexts:
    sasIOM1120020AlertHealthInformational.setStatus(
        "current"
    )

sasIOM1120021AlertHealthInformational = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 9, 0, 1120021)
)
sasIOM1120021AlertHealthInformational.setObjects(
      *(("DELL-MM-MIB-SMIv2", "dmmCA2MessageID"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2Message"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2MessageArgs"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2AlertStatus"),
        ("DELL-MM-MIB-SMIv2", "dmmDeviceServiceTag"),
        ("DELL-MM-MIB-SMIv2", "dmmCategoryName"),
        ("DELL-MM-MIB-SMIv2", "dmmSubCategoryName"),
        ("DELL-MM-MIB-SMIv2", "dmmSeverity"))
)
if mibBuilder.loadTexts:
    sasIOM1120021AlertHealthInformational.setStatus(
        "current"
    )

sasIOM1120022AlertHealthInformational = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 9, 0, 1120022)
)
sasIOM1120022AlertHealthInformational.setObjects(
      *(("DELL-MM-MIB-SMIv2", "dmmCA2MessageID"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2Message"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2MessageArgs"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2AlertStatus"),
        ("DELL-MM-MIB-SMIv2", "dmmDeviceServiceTag"),
        ("DELL-MM-MIB-SMIv2", "dmmCategoryName"),
        ("DELL-MM-MIB-SMIv2", "dmmSubCategoryName"),
        ("DELL-MM-MIB-SMIv2", "dmmSeverity"))
)
if mibBuilder.loadTexts:
    sasIOM1120022AlertHealthInformational.setStatus(
        "current"
    )

sasIOM1120023AlertHealthInformational = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 9, 0, 1120023)
)
sasIOM1120023AlertHealthInformational.setObjects(
      *(("DELL-MM-MIB-SMIv2", "dmmCA2MessageID"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2Message"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2MessageArgs"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2AlertStatus"),
        ("DELL-MM-MIB-SMIv2", "dmmDeviceServiceTag"),
        ("DELL-MM-MIB-SMIv2", "dmmCategoryName"),
        ("DELL-MM-MIB-SMIv2", "dmmSubCategoryName"),
        ("DELL-MM-MIB-SMIv2", "dmmSeverity"))
)
if mibBuilder.loadTexts:
    sasIOM1120023AlertHealthInformational.setStatus(
        "current"
    )

sasIOM1120024AlertHealthInformational = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 9, 0, 1120024)
)
sasIOM1120024AlertHealthInformational.setObjects(
      *(("DELL-MM-MIB-SMIv2", "dmmCA2MessageID"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2Message"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2MessageArgs"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2AlertStatus"),
        ("DELL-MM-MIB-SMIv2", "dmmDeviceServiceTag"),
        ("DELL-MM-MIB-SMIv2", "dmmCategoryName"),
        ("DELL-MM-MIB-SMIv2", "dmmSubCategoryName"),
        ("DELL-MM-MIB-SMIv2", "dmmSeverity"))
)
if mibBuilder.loadTexts:
    sasIOM1120024AlertHealthInformational.setStatus(
        "current"
    )

sasIOM1120025AlertHealthCritical = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 9, 0, 1120025)
)
sasIOM1120025AlertHealthCritical.setObjects(
      *(("DELL-MM-MIB-SMIv2", "dmmCA2MessageID"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2Message"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2MessageArgs"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2AlertStatus"),
        ("DELL-MM-MIB-SMIv2", "dmmDeviceServiceTag"),
        ("DELL-MM-MIB-SMIv2", "dmmCategoryName"),
        ("DELL-MM-MIB-SMIv2", "dmmSubCategoryName"),
        ("DELL-MM-MIB-SMIv2", "dmmSeverity"))
)
if mibBuilder.loadTexts:
    sasIOM1120025AlertHealthCritical.setStatus(
        "current"
    )

sasIOM1120026AlertHealthInformational = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 9, 0, 1120026)
)
sasIOM1120026AlertHealthInformational.setObjects(
      *(("DELL-MM-MIB-SMIv2", "dmmCA2MessageID"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2Message"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2MessageArgs"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2AlertStatus"),
        ("DELL-MM-MIB-SMIv2", "dmmDeviceServiceTag"),
        ("DELL-MM-MIB-SMIv2", "dmmCategoryName"),
        ("DELL-MM-MIB-SMIv2", "dmmSubCategoryName"),
        ("DELL-MM-MIB-SMIv2", "dmmSeverity"))
)
if mibBuilder.loadTexts:
    sasIOM1120026AlertHealthInformational.setStatus(
        "current"
    )

sasIOM1120027AlertHealthCritical = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 9, 0, 1120027)
)
sasIOM1120027AlertHealthCritical.setObjects(
      *(("DELL-MM-MIB-SMIv2", "dmmCA2MessageID"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2Message"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2MessageArgs"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2AlertStatus"),
        ("DELL-MM-MIB-SMIv2", "dmmDeviceServiceTag"),
        ("DELL-MM-MIB-SMIv2", "dmmCategoryName"),
        ("DELL-MM-MIB-SMIv2", "dmmSubCategoryName"),
        ("DELL-MM-MIB-SMIv2", "dmmSeverity"))
)
if mibBuilder.loadTexts:
    sasIOM1120027AlertHealthCritical.setStatus(
        "current"
    )

sasIOM1120028AlertHealthInformational = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 9, 0, 1120028)
)
sasIOM1120028AlertHealthInformational.setObjects(
      *(("DELL-MM-MIB-SMIv2", "dmmCA2MessageID"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2Message"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2MessageArgs"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2AlertStatus"),
        ("DELL-MM-MIB-SMIv2", "dmmDeviceServiceTag"),
        ("DELL-MM-MIB-SMIv2", "dmmCategoryName"),
        ("DELL-MM-MIB-SMIv2", "dmmSubCategoryName"),
        ("DELL-MM-MIB-SMIv2", "dmmSeverity"))
)
if mibBuilder.loadTexts:
    sasIOM1120028AlertHealthInformational.setStatus(
        "current"
    )

sasIOM1120029AlertHealthWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 9, 0, 1120029)
)
sasIOM1120029AlertHealthWarning.setObjects(
      *(("DELL-MM-MIB-SMIv2", "dmmCA2MessageID"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2Message"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2MessageArgs"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2AlertStatus"),
        ("DELL-MM-MIB-SMIv2", "dmmDeviceServiceTag"),
        ("DELL-MM-MIB-SMIv2", "dmmCategoryName"),
        ("DELL-MM-MIB-SMIv2", "dmmSubCategoryName"),
        ("DELL-MM-MIB-SMIv2", "dmmSeverity"))
)
if mibBuilder.loadTexts:
    sasIOM1120029AlertHealthWarning.setStatus(
        "current"
    )

sasIOM1120030AlertHealthWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 9, 0, 1120030)
)
sasIOM1120030AlertHealthWarning.setObjects(
      *(("DELL-MM-MIB-SMIv2", "dmmCA2MessageID"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2Message"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2MessageArgs"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2AlertStatus"),
        ("DELL-MM-MIB-SMIv2", "dmmDeviceServiceTag"),
        ("DELL-MM-MIB-SMIv2", "dmmCategoryName"),
        ("DELL-MM-MIB-SMIv2", "dmmSubCategoryName"),
        ("DELL-MM-MIB-SMIv2", "dmmSeverity"))
)
if mibBuilder.loadTexts:
    sasIOM1120030AlertHealthWarning.setStatus(
        "current"
    )

sasIOM1120031AlertHealthCritical = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 9, 0, 1120031)
)
sasIOM1120031AlertHealthCritical.setObjects(
      *(("DELL-MM-MIB-SMIv2", "dmmCA2MessageID"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2Message"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2MessageArgs"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2AlertStatus"),
        ("DELL-MM-MIB-SMIv2", "dmmDeviceServiceTag"),
        ("DELL-MM-MIB-SMIv2", "dmmCategoryName"),
        ("DELL-MM-MIB-SMIv2", "dmmSubCategoryName"),
        ("DELL-MM-MIB-SMIv2", "dmmSeverity"))
)
if mibBuilder.loadTexts:
    sasIOM1120031AlertHealthCritical.setStatus(
        "current"
    )

sasIOM1120032AlertHealthInformational = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 9, 0, 1120032)
)
sasIOM1120032AlertHealthInformational.setObjects(
      *(("DELL-MM-MIB-SMIv2", "dmmCA2MessageID"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2Message"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2MessageArgs"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2AlertStatus"),
        ("DELL-MM-MIB-SMIv2", "dmmDeviceServiceTag"),
        ("DELL-MM-MIB-SMIv2", "dmmCategoryName"),
        ("DELL-MM-MIB-SMIv2", "dmmSubCategoryName"),
        ("DELL-MM-MIB-SMIv2", "dmmSeverity"))
)
if mibBuilder.loadTexts:
    sasIOM1120032AlertHealthInformational.setStatus(
        "current"
    )

sasIOM1120033AlertHealthCritical = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 9, 0, 1120033)
)
sasIOM1120033AlertHealthCritical.setObjects(
      *(("DELL-MM-MIB-SMIv2", "dmmCA2MessageID"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2Message"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2MessageArgs"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2AlertStatus"),
        ("DELL-MM-MIB-SMIv2", "dmmDeviceServiceTag"),
        ("DELL-MM-MIB-SMIv2", "dmmCategoryName"),
        ("DELL-MM-MIB-SMIv2", "dmmSubCategoryName"),
        ("DELL-MM-MIB-SMIv2", "dmmSeverity"))
)
if mibBuilder.loadTexts:
    sasIOM1120033AlertHealthCritical.setStatus(
        "current"
    )

sasIOM1120034AlertHealthInformational = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 9, 0, 1120034)
)
sasIOM1120034AlertHealthInformational.setObjects(
      *(("DELL-MM-MIB-SMIv2", "dmmCA2MessageID"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2Message"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2MessageArgs"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2AlertStatus"),
        ("DELL-MM-MIB-SMIv2", "dmmDeviceServiceTag"),
        ("DELL-MM-MIB-SMIv2", "dmmCategoryName"),
        ("DELL-MM-MIB-SMIv2", "dmmSubCategoryName"),
        ("DELL-MM-MIB-SMIv2", "dmmSeverity"))
)
if mibBuilder.loadTexts:
    sasIOM1120034AlertHealthInformational.setStatus(
        "current"
    )

sasIOM1120035AlertHealthInformational = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 9, 0, 1120035)
)
sasIOM1120035AlertHealthInformational.setObjects(
      *(("DELL-MM-MIB-SMIv2", "dmmCA2MessageID"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2Message"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2MessageArgs"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2AlertStatus"),
        ("DELL-MM-MIB-SMIv2", "dmmDeviceServiceTag"),
        ("DELL-MM-MIB-SMIv2", "dmmCategoryName"),
        ("DELL-MM-MIB-SMIv2", "dmmSubCategoryName"),
        ("DELL-MM-MIB-SMIv2", "dmmSeverity"))
)
if mibBuilder.loadTexts:
    sasIOM1120035AlertHealthInformational.setStatus(
        "current"
    )

sasIOM1120036AlertHealthInformational = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 9, 0, 1120036)
)
sasIOM1120036AlertHealthInformational.setObjects(
      *(("DELL-MM-MIB-SMIv2", "dmmCA2MessageID"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2Message"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2MessageArgs"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2AlertStatus"),
        ("DELL-MM-MIB-SMIv2", "dmmDeviceServiceTag"),
        ("DELL-MM-MIB-SMIv2", "dmmCategoryName"),
        ("DELL-MM-MIB-SMIv2", "dmmSubCategoryName"),
        ("DELL-MM-MIB-SMIv2", "dmmSeverity"))
)
if mibBuilder.loadTexts:
    sasIOM1120036AlertHealthInformational.setStatus(
        "current"
    )

sasIOM1120039AlertHealthWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 9, 0, 1120039)
)
sasIOM1120039AlertHealthWarning.setObjects(
      *(("DELL-MM-MIB-SMIv2", "dmmCA2MessageID"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2Message"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2MessageArgs"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2AlertStatus"),
        ("DELL-MM-MIB-SMIv2", "dmmDeviceServiceTag"),
        ("DELL-MM-MIB-SMIv2", "dmmCategoryName"),
        ("DELL-MM-MIB-SMIv2", "dmmSubCategoryName"),
        ("DELL-MM-MIB-SMIv2", "dmmSeverity"))
)
if mibBuilder.loadTexts:
    sasIOM1120039AlertHealthWarning.setStatus(
        "current"
    )

sasIOM1120040AlertHealthCritical = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 9, 0, 1120040)
)
sasIOM1120040AlertHealthCritical.setObjects(
      *(("DELL-MM-MIB-SMIv2", "dmmCA2MessageID"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2Message"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2MessageArgs"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2AlertStatus"),
        ("DELL-MM-MIB-SMIv2", "dmmDeviceServiceTag"),
        ("DELL-MM-MIB-SMIv2", "dmmCategoryName"),
        ("DELL-MM-MIB-SMIv2", "dmmSubCategoryName"),
        ("DELL-MM-MIB-SMIv2", "dmmSeverity"))
)
if mibBuilder.loadTexts:
    sasIOM1120040AlertHealthCritical.setStatus(
        "current"
    )

sasIOM1120041AlertHealthCritical = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 9, 0, 1120041)
)
sasIOM1120041AlertHealthCritical.setObjects(
      *(("DELL-MM-MIB-SMIv2", "dmmCA2MessageID"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2Message"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2MessageArgs"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2AlertStatus"),
        ("DELL-MM-MIB-SMIv2", "dmmDeviceServiceTag"),
        ("DELL-MM-MIB-SMIv2", "dmmCategoryName"),
        ("DELL-MM-MIB-SMIv2", "dmmSubCategoryName"),
        ("DELL-MM-MIB-SMIv2", "dmmSeverity"))
)
if mibBuilder.loadTexts:
    sasIOM1120041AlertHealthCritical.setStatus(
        "current"
    )

sasIOM1120042AlertConfigurationCritical = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 9, 0, 1120042)
)
sasIOM1120042AlertConfigurationCritical.setObjects(
      *(("DELL-MM-MIB-SMIv2", "dmmCA2MessageID"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2Message"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2MessageArgs"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2AlertStatus"),
        ("DELL-MM-MIB-SMIv2", "dmmDeviceServiceTag"),
        ("DELL-MM-MIB-SMIv2", "dmmCategoryName"),
        ("DELL-MM-MIB-SMIv2", "dmmSubCategoryName"),
        ("DELL-MM-MIB-SMIv2", "dmmSeverity"))
)
if mibBuilder.loadTexts:
    sasIOM1120042AlertConfigurationCritical.setStatus(
        "current"
    )

sasIOM1120069AlertHealthInformational = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 9, 0, 1120069)
)
sasIOM1120069AlertHealthInformational.setObjects(
      *(("DELL-MM-MIB-SMIv2", "dmmCA2MessageID"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2Message"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2MessageArgs"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2AlertStatus"),
        ("DELL-MM-MIB-SMIv2", "dmmDeviceServiceTag"),
        ("DELL-MM-MIB-SMIv2", "dmmCategoryName"),
        ("DELL-MM-MIB-SMIv2", "dmmSubCategoryName"),
        ("DELL-MM-MIB-SMIv2", "dmmSeverity"))
)
if mibBuilder.loadTexts:
    sasIOM1120069AlertHealthInformational.setStatus(
        "current"
    )

sasIOM1120072AlertHealthWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 9, 0, 1120072)
)
sasIOM1120072AlertHealthWarning.setObjects(
      *(("DELL-MM-MIB-SMIv2", "dmmCA2MessageID"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2Message"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2MessageArgs"),
        ("DELL-MM-MIB-SMIv2", "dmmCA2AlertStatus"),
        ("DELL-MM-MIB-SMIv2", "dmmDeviceServiceTag"),
        ("DELL-MM-MIB-SMIv2", "dmmCategoryName"),
        ("DELL-MM-MIB-SMIv2", "dmmSubCategoryName"),
        ("DELL-MM-MIB-SMIv2", "dmmSeverity"))
)
if mibBuilder.loadTexts:
    sasIOM1120072AlertHealthWarning.setStatus(
        "current"
    )


# Notifications groups

dmmChassisAlert2NotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 10, 2, 1)
)
dmmChassisAlert2NotificationGroup.setObjects(
      *(("DELL-MM-MIB-SMIv2", "alert2AmperageProbeNormal"),
        ("DELL-MM-MIB-SMIv2", "alert2AmperageProbeWarning"),
        ("DELL-MM-MIB-SMIv2", "alert2AmperageProbeFailure"),
        ("DELL-MM-MIB-SMIv2", "alert2BatteryNormal"),
        ("DELL-MM-MIB-SMIv2", "alert2BatteryWarning"),
        ("DELL-MM-MIB-SMIv2", "alert2BatteryFailure"),
        ("DELL-MM-MIB-SMIv2", "alert2CableFailure"),
        ("DELL-MM-MIB-SMIv2", "alert2CMCWarning"),
        ("DELL-MM-MIB-SMIv2", "alert2CMCFailure"),
        ("DELL-MM-MIB-SMIv2", "alert2FanInformation"),
        ("DELL-MM-MIB-SMIv2", "alert2FanWarning"),
        ("DELL-MM-MIB-SMIv2", "alert2FanFailure"),
        ("DELL-MM-MIB-SMIv2", "alert2HardwareConfigurationInformation"),
        ("DELL-MM-MIB-SMIv2", "alert2HardwareConfigurationWarning"),
        ("DELL-MM-MIB-SMIv2", "alert2HardwareConfigurationFailure"),
        ("DELL-MM-MIB-SMIv2", "alert2IOVirtualizationInformation"),
        ("DELL-MM-MIB-SMIv2", "alert2IOVirtualizationWarning"),
        ("DELL-MM-MIB-SMIv2", "alert2IOVirtualizationFailure"),
        ("DELL-MM-MIB-SMIv2", "alert2LinkStatusInformation"),
        ("DELL-MM-MIB-SMIv2", "alert2LinkStatusWarning"),
        ("DELL-MM-MIB-SMIv2", "alert2LinkStatusFailure"),
        ("DELL-MM-MIB-SMIv2", "alert2PowerSupplyNormal"),
        ("DELL-MM-MIB-SMIv2", "alert2PowerSupplyWarning"),
        ("DELL-MM-MIB-SMIv2", "alert2PowerSupplyFailure"),
        ("DELL-MM-MIB-SMIv2", "alert2PowerSupplyAbsent"),
        ("DELL-MM-MIB-SMIv2", "alert2PowerUsageInformation"),
        ("DELL-MM-MIB-SMIv2", "alert2PowerUsageWarning"),
        ("DELL-MM-MIB-SMIv2", "alert2PowerUsageFailure"),
        ("DELL-MM-MIB-SMIv2", "alert2RedundancyInformation"),
        ("DELL-MM-MIB-SMIv2", "alert2RedundancyDegraded"),
        ("DELL-MM-MIB-SMIv2", "alert2RedundancyLost"),
        ("DELL-MM-MIB-SMIv2", "alert2SecurityInformation"),
        ("DELL-MM-MIB-SMIv2", "alert2SecurityWarning"),
        ("DELL-MM-MIB-SMIv2", "alert2SecurityFailure"),
        ("DELL-MM-MIB-SMIv2", "alert2SystemEventLogInformation"),
        ("DELL-MM-MIB-SMIv2", "alert2SystemEventLogWarning"),
        ("DELL-MM-MIB-SMIv2", "alert2SystemEventLogFailure"),
        ("DELL-MM-MIB-SMIv2", "alert2SoftwareConfigurationInformation"),
        ("DELL-MM-MIB-SMIv2", "alert2SoftwareConfigurationWarning"),
        ("DELL-MM-MIB-SMIv2", "alert2SoftwareConfigurationFailure"),
        ("DELL-MM-MIB-SMIv2", "alert2TemperatureProbeNormal"),
        ("DELL-MM-MIB-SMIv2", "alert2TemperatureProbeWarning"),
        ("DELL-MM-MIB-SMIv2", "alert2TemperatureProbeFailure"),
        ("DELL-MM-MIB-SMIv2", "alert2VoltageProbeNormal"),
        ("DELL-MM-MIB-SMIv2", "alert2VoltageProbeWarning"),
        ("DELL-MM-MIB-SMIv2", "alert2VoltageProbeFailure"),
        ("DELL-MM-MIB-SMIv2", "alert2StorageBatteryInformation"),
        ("DELL-MM-MIB-SMIv2", "alert2StorageBatteryWarning"),
        ("DELL-MM-MIB-SMIv2", "alert2StorageBatteryFailure"),
        ("DELL-MM-MIB-SMIv2", "alert2StorageControllerInformation"),
        ("DELL-MM-MIB-SMIv2", "alert2StorageControllerWarning"),
        ("DELL-MM-MIB-SMIv2", "alert2StorageControllerFailure"),
        ("DELL-MM-MIB-SMIv2", "alert2StorageEnclosureInformation"),
        ("DELL-MM-MIB-SMIv2", "alert2StorageEnclosureWarning"),
        ("DELL-MM-MIB-SMIv2", "alert2StorageEnclosureFailure"),
        ("DELL-MM-MIB-SMIv2", "alert2StorageFanInformation"),
        ("DELL-MM-MIB-SMIv2", "alert2StorageFanWarning"),
        ("DELL-MM-MIB-SMIv2", "alert2StorageFanFailure"),
        ("DELL-MM-MIB-SMIv2", "alert2StoragePhysicalDiskInformation"),
        ("DELL-MM-MIB-SMIv2", "alert2StoragePhysicalDiskWarning"),
        ("DELL-MM-MIB-SMIv2", "alert2StoragePhysicalDiskFailure"),
        ("DELL-MM-MIB-SMIv2", "alert2StoragePowerSupplyInformation"),
        ("DELL-MM-MIB-SMIv2", "alert2StoragePowerSupplyWarning"),
        ("DELL-MM-MIB-SMIv2", "alert2StoragePowerSupplyFailure"),
        ("DELL-MM-MIB-SMIv2", "alert2StorageSecurityInformation"),
        ("DELL-MM-MIB-SMIv2", "alert2StorageSecurityWarning"),
        ("DELL-MM-MIB-SMIv2", "alert2StorageSecurityFailure"),
        ("DELL-MM-MIB-SMIv2", "alert2StorageManagementInformation"),
        ("DELL-MM-MIB-SMIv2", "alert2StorageManagementWarning"),
        ("DELL-MM-MIB-SMIv2", "alert2StorageManagementFailure"),
        ("DELL-MM-MIB-SMIv2", "alert2StorageTemperatureProbeInformation"),
        ("DELL-MM-MIB-SMIv2", "alert2StorageTemperatureProbeWarning"),
        ("DELL-MM-MIB-SMIv2", "alert2StorageTemperatureProbeFailure"),
        ("DELL-MM-MIB-SMIv2", "alert2StorageVirtualDiskInformation"),
        ("DELL-MM-MIB-SMIv2", "alert2StorageVirtualDiskWarning"),
        ("DELL-MM-MIB-SMIv2", "alert2StorageVirtualDiskFailure"),
        ("DELL-MM-MIB-SMIv2", "alert2SoftwareChangeUpdateWarning"),
        ("DELL-MM-MIB-SMIv2", "alert2CMCAuditInformation"),
        ("DELL-MM-MIB-SMIv2", "alert2CMCAuditWarning"),
        ("DELL-MM-MIB-SMIv2", "alert2CMCAuditFailure"),
        ("DELL-MM-MIB-SMIv2", "alert2IOVirtualizationAuditWarning"),
        ("DELL-MM-MIB-SMIv2", "alert2LicenseInformation"),
        ("DELL-MM-MIB-SMIv2", "alert2LicenseWarning"),
        ("DELL-MM-MIB-SMIv2", "alert2LicenseFailure"),
        ("DELL-MM-MIB-SMIv2", "alert2PCIDeviceAuditWarning"),
        ("DELL-MM-MIB-SMIv2", "alert2PowerSupplyAuditWarning"),
        ("DELL-MM-MIB-SMIv2", "alert2PowerSupplyAuditFailure"),
        ("DELL-MM-MIB-SMIv2", "alert2PowerUsageAuditInformation"),
        ("DELL-MM-MIB-SMIv2", "alert2PowerUsageAuditWarning"),
        ("DELL-MM-MIB-SMIv2", "alert2PowerUsageAuditFailure"),
        ("DELL-MM-MIB-SMIv2", "alert2SoftwareChangeAuditFailure"),
        ("DELL-MM-MIB-SMIv2", "alert2IOVConfigurationInformation"),
        ("DELL-MM-MIB-SMIv2", "alert2IOVConfigurationWarning"),
        ("DELL-MM-MIB-SMIv2", "alert2PCIDeviceConfigurationInformation"),
        ("DELL-MM-MIB-SMIv2", "alert2SWCConfigurationWarning"),
        ("DELL-MM-MIB-SMIv2", "alert2SWCConfigurationFailure"),
        ("DELL-MM-MIB-SMIv2", "alert2CMCTestTrap"),
        ("DELL-MM-MIB-SMIv2", "alert851138RCPRestoreInformational"),
        ("DELL-MM-MIB-SMIv2", "alert851139RCPRestoreCritical"),
        ("DELL-MM-MIB-SMIv2", "alert856129DeviceStateInformational"),
        ("DELL-MM-MIB-SMIv2", "alert856130DeviceStateCritical"),
        ("DELL-MM-MIB-SMIv2", "alert856131DeviceStateCritical"),
        ("DELL-MM-MIB-SMIv2", "alert856132DeviceStateInformational"),
        ("DELL-MM-MIB-SMIv2", "alert856133DeviceStateInformational"),
        ("DELL-MM-MIB-SMIv2", "alert856134DeviceStateInformational"),
        ("DELL-MM-MIB-SMIv2", "alert856172DeviceStateInformational"),
        ("DELL-MM-MIB-SMIv2", "alert856173DeviceStateCritical"),
        ("DELL-MM-MIB-SMIv2", "alert856174DeviceStateCritical"),
        ("DELL-MM-MIB-SMIv2", "alert856175DeviceStateWarning"))
)
if mibBuilder.loadTexts:
    dmmChassisAlert2NotificationGroup.setStatus(
        "current"
    )

dmmGenericAlertNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 10, 2, 2)
)
dmmGenericAlertNotificationGroup.setObjects(
      *(("DELL-MM-MIB-SMIv2", "alertGenericCritical"),
        ("DELL-MM-MIB-SMIv2", "alertGenericWarning"),
        ("DELL-MM-MIB-SMIv2", "alertGenericNormal"),
        ("DELL-MM-MIB-SMIv2", "alertGenericInformational"),
        ("DELL-MM-MIB-SMIv2", "alertGenericTestTrapEvent"),
        ("DELL-MM-MIB-SMIv2", "alertAuditCritical"),
        ("DELL-MM-MIB-SMIv2", "alertAuditWarning"),
        ("DELL-MM-MIB-SMIv2", "alertAuditNormal"),
        ("DELL-MM-MIB-SMIv2", "alertAuditInformational"))
)
if mibBuilder.loadTexts:
    dmmGenericAlertNotificationGroup.setStatus(
        "current"
    )

dmmiDRACAlertNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 10, 2, 3)
)
dmmiDRACAlertNotificationGroup.setObjects(
      *(("DELL-MM-MIB-SMIv2", "iDRAC10267alertJobControlConfigurationInformation"),
        ("DELL-MM-MIB-SMIv2", "iDRAC10298alertPRDeviceDetectionWarning"),
        ("DELL-MM-MIB-SMIv2", "iDRAC10395alertTestTrapEvent"),
        ("DELL-MM-MIB-SMIv2", "iDRAC10529alertSWCConfigurationFailure"),
        ("DELL-MM-MIB-SMIv2", "iDRAC10530alertSWCConfigurationWarning"),
        ("DELL-MM-MIB-SMIv2", "iDRAC10531alertSWCConfigurationInformation"),
        ("DELL-MM-MIB-SMIv2", "iDRAC10547alertIPAddressConfigurationInformation"),
        ("DELL-MM-MIB-SMIv2", "iDRAC10578alertSecurityConfigurationWarning"),
        ("DELL-MM-MIB-SMIv2", "iDRAC10611alertPCIDeviceConfigurationInformation"),
        ("DELL-MM-MIB-SMIv2", "iDRAC10627alertSystemConfigurationChangeInformation"),
        ("DELL-MM-MIB-SMIv2", "iDRAC10635alertAutoDiscoveryInformation"),
        ("DELL-MM-MIB-SMIv2", "iDRAC10770alertNetworkConfigurationWarning"),
        ("DELL-MM-MIB-SMIv2", "iDRAC10771alertNetworkConfigurationInformation"),
        ("DELL-MM-MIB-SMIv2", "iDRAC11274alertSDKConfigurationWarning"),
        ("DELL-MM-MIB-SMIv2", "iDRAC11275alertSDKConfigurationInformation"),
        ("DELL-MM-MIB-SMIv2", "iDRAC2089alertNetworkFailure"),
        ("DELL-MM-MIB-SMIv2", "iDRAC2090alertNetworkWarning"),
        ("DELL-MM-MIB-SMIv2", "iDRAC2091alertNetworkInformation"),
        ("DELL-MM-MIB-SMIv2", "iDRAC2153alertFanFailure"),
        ("DELL-MM-MIB-SMIv2", "iDRAC2154alertFanWarning"),
        ("DELL-MM-MIB-SMIv2", "iDRAC2155alertFanInformation"),
        ("DELL-MM-MIB-SMIv2", "iDRAC2161alertTemperatureProbeFailure"),
        ("DELL-MM-MIB-SMIv2", "iDRAC2162alertTemperatureProbeWarning"),
        ("DELL-MM-MIB-SMIv2", "iDRAC2163alertTemperatureProbeNormal"),
        ("DELL-MM-MIB-SMIv2", "iDRAC2169alertVoltageProbeFailure"),
        ("DELL-MM-MIB-SMIv2", "iDRAC2170alertVoltageProbeWarning"),
        ("DELL-MM-MIB-SMIv2", "iDRAC2171alertVoltageProbeNormal"),
        ("DELL-MM-MIB-SMIv2", "iDRAC2177alertAmperageProbeFailure"),
        ("DELL-MM-MIB-SMIv2", "iDRAC2178alertAmperageProbeWarning"),
        ("DELL-MM-MIB-SMIv2", "iDRAC2179alertAmperageProbeNormal"),
        ("DELL-MM-MIB-SMIv2", "iDRAC2185alertPowerSupplyFailure"),
        ("DELL-MM-MIB-SMIv2", "iDRAC2186alertPowerSupplyWarning"),
        ("DELL-MM-MIB-SMIv2", "iDRAC2187alertPowerSupplyNormal"),
        ("DELL-MM-MIB-SMIv2", "iDRAC2209alertIntegratedDualSDModuleFailure"),
        ("DELL-MM-MIB-SMIv2", "iDRAC2210alertIntegratedDualSDModuleWarning"),
        ("DELL-MM-MIB-SMIv2", "iDRAC2211alertIntegratedDualSDModuleInformation"),
        ("DELL-MM-MIB-SMIv2", "iDRAC2225alertBatteryFailure"),
        ("DELL-MM-MIB-SMIv2", "iDRAC2226alertBatteryWarning"),
        ("DELL-MM-MIB-SMIv2", "iDRAC2227alertBatteryNormal"),
        ("DELL-MM-MIB-SMIv2", "iDRAC2233alertAutomaticSystemRecovery"),
        ("DELL-MM-MIB-SMIv2", "iDRAC2241alertProcessorDeviceStatusFailure"),
        ("DELL-MM-MIB-SMIv2", "iDRAC2242alertProcessorDeviceStatusWarning"),
        ("DELL-MM-MIB-SMIv2", "iDRAC2243alertProcessorDeviceStatusNormal"),
        ("DELL-MM-MIB-SMIv2", "iDRAC2249alertLinkStatusFailure"),
        ("DELL-MM-MIB-SMIv2", "iDRAC2250alertLinkStatusWarning"),
        ("DELL-MM-MIB-SMIv2", "iDRAC2251alertLinkStatusInformation"),
        ("DELL-MM-MIB-SMIv2", "iDRAC2265alertMemoryDeviceFailure"),
        ("DELL-MM-MIB-SMIv2", "iDRAC2266alertMemoryDeviceWarning"),
        ("DELL-MM-MIB-SMIv2", "iDRAC2267alertMemoryDeviceInformation"),
        ("DELL-MM-MIB-SMIv2", "iDRAC2273alertPowerUsageFailure"),
        ("DELL-MM-MIB-SMIv2", "iDRAC2274alertPowerUsageWarning"),
        ("DELL-MM-MIB-SMIv2", "iDRAC2275alertPowerUsageInformation"),
        ("DELL-MM-MIB-SMIv2", "iDRAC2297alertPhysicalDiskFailure"),
        ("DELL-MM-MIB-SMIv2", "iDRAC2298alertPhysicalDiskWarning"),
        ("DELL-MM-MIB-SMIv2", "iDRAC2299alertPhysicalDiskInformation"),
        ("DELL-MM-MIB-SMIv2", "iDRAC2329alertHardwareConfigurationFailure"),
        ("DELL-MM-MIB-SMIv2", "iDRAC2330alertHardwareConfigurationWarning"),
        ("DELL-MM-MIB-SMIv2", "iDRAC2331alertHardwareConfigurationInformation"),
        ("DELL-MM-MIB-SMIv2", "iDRAC2337alertSoftwareConfigurationFailure"),
        ("DELL-MM-MIB-SMIv2", "iDRAC2338alertSoftwareConfigurationWarning"),
        ("DELL-MM-MIB-SMIv2", "iDRAC2339alertSoftwareConfigurationInformation"),
        ("DELL-MM-MIB-SMIv2", "iDRAC2377alertSystemEventLogFailure"),
        ("DELL-MM-MIB-SMIv2", "iDRAC2378alertSystemEventLogWarning"),
        ("DELL-MM-MIB-SMIv2", "iDRAC2379alertSystemEventLogInformation"),
        ("DELL-MM-MIB-SMIv2", "iDRAC2385alertSecurityFailure"),
        ("DELL-MM-MIB-SMIv2", "iDRAC2386alertSecurityWarning"),
        ("DELL-MM-MIB-SMIv2", "iDRAC2387alertSecurityInformation"),
        ("DELL-MM-MIB-SMIv2", "iDRAC2393alertCableFailure"),
        ("DELL-MM-MIB-SMIv2", "iDRAC2409alertOSFailure"),
        ("DELL-MM-MIB-SMIv2", "iDRAC2411alertOSInformation"),
        ("DELL-MM-MIB-SMIv2", "iDRAC2417alertPCIDeviceFailure"),
        ("DELL-MM-MIB-SMIv2", "iDRAC2418alertPCIDeviceWarning"),
        ("DELL-MM-MIB-SMIv2", "iDRAC2419alertPCIDeviceInformation"),
        ("DELL-MM-MIB-SMIv2", "iDRAC2425alertBiosPostFailure"),
        ("DELL-MM-MIB-SMIv2", "iDRAC2433alertInternaliDRACMemoryUnresponsive"),
        ("DELL-MM-MIB-SMIv2", "iDRAC2435alertServerIdleTime"),
        ("DELL-MM-MIB-SMIv2", "iDRAC2457alertProcessorDeviceAbsent"),
        ("DELL-MM-MIB-SMIv2", "iDRAC2465alertPowerSupplyAbsent"),
        ("DELL-MM-MIB-SMIv2", "iDRAC2473alertRedundancyLost"),
        ("DELL-MM-MIB-SMIv2", "iDRAC2474alertRedundancyDegraded"),
        ("DELL-MM-MIB-SMIv2", "iDRAC2475alertRedundancyInformation"),
        ("DELL-MM-MIB-SMIv2", "iDRAC2481alertIntegratedDualSDModuleAbsent"),
        ("DELL-MM-MIB-SMIv2", "iDRAC2489alertIntegratedDualSDModuleRedundancyLost"),
        ("DELL-MM-MIB-SMIv2", "iDRAC2490alertIntegratedDualSDModuleRedundancyDegraded"),
        ("DELL-MM-MIB-SMIv2", "iDRAC2491alertIntegratedDualSDModuleRedundancyInformation"),
        ("DELL-MM-MIB-SMIv2", "iDRAC2505alertvFlashMediaDeviceFailure"),
        ("DELL-MM-MIB-SMIv2", "iDRAC2506alertvFlashMediaDeviceWarning"),
        ("DELL-MM-MIB-SMIv2", "iDRAC2507alertvFlashMediaDeviceInformation"),
        ("DELL-MM-MIB-SMIv2", "iDRAC2515alertvFlashMediaDeviceAbsent"),
        ("DELL-MM-MIB-SMIv2", "iDRAC2521alertTemperatureStatisticsFailure"),
        ("DELL-MM-MIB-SMIv2", "iDRAC2522alertTemperatureStatisticsWarning"),
        ("DELL-MM-MIB-SMIv2", "iDRAC2531alertRACInformation"),
        ("DELL-MM-MIB-SMIv2", "iDRAC2537alertFiberChannelFailure"),
        ("DELL-MM-MIB-SMIv2", "iDRAC2538alertFiberChannelWarning"),
        ("DELL-MM-MIB-SMIv2", "iDRAC2539alertFiberChannelInformation"),
        ("DELL-MM-MIB-SMIv2", "iDRAC2545alertCMCFailure"),
        ("DELL-MM-MIB-SMIv2", "iDRAC2546alertCMCWarning"),
        ("DELL-MM-MIB-SMIv2", "iDRAC2553alertIOVirtualizationFailure"),
        ("DELL-MM-MIB-SMIv2", "iDRAC2650alertSystemPerformanceWarning"),
        ("DELL-MM-MIB-SMIv2", "iDRAC3049alertLiquidCoolingLeakFailure"),
        ("DELL-MM-MIB-SMIv2", "iDRAC3050alertLiquidCoolingLeakWarning"),
        ("DELL-MM-MIB-SMIv2", "iDRAC3051alertLiquidCoolingLeakInformational"),
        ("DELL-MM-MIB-SMIv2", "iDRAC3082alertSDKSystemWarning"),
        ("DELL-MM-MIB-SMIv2", "iDRAC3083alertSDKSystemInformational"),
        ("DELL-MM-MIB-SMIv2", "iDRAC4177alertStorageManagementFailure"),
        ("DELL-MM-MIB-SMIv2", "iDRAC4178alertStorageManagementWarning"),
        ("DELL-MM-MIB-SMIv2", "iDRAC4179alertStorageManagementInformation"),
        ("DELL-MM-MIB-SMIv2", "iDRAC4201alertStorageFanFailure"),
        ("DELL-MM-MIB-SMIv2", "iDRAC4202alertStorageFanWarning"),
        ("DELL-MM-MIB-SMIv2", "iDRAC4203alertStorageFanInformation"),
        ("DELL-MM-MIB-SMIv2", "iDRAC4209alertStorageTemperatureProbeFailure"),
        ("DELL-MM-MIB-SMIv2", "iDRAC4210alertStorageTemperatureProbeWarning"),
        ("DELL-MM-MIB-SMIv2", "iDRAC4211alertStorageTemperatureProbeInformation"),
        ("DELL-MM-MIB-SMIv2", "iDRAC4233alertStoragePowerSupplyFailure"),
        ("DELL-MM-MIB-SMIv2", "iDRAC4234alertStoragePowerSupplyWarning"),
        ("DELL-MM-MIB-SMIv2", "iDRAC4235alertStoragePowerSupplyInformation"),
        ("DELL-MM-MIB-SMIv2", "iDRAC4273alertStorageBatteryFailure"),
        ("DELL-MM-MIB-SMIv2", "iDRAC4274alertStorageBatteryWarning"),
        ("DELL-MM-MIB-SMIv2", "iDRAC4275alertStorageBatteryInformation"),
        ("DELL-MM-MIB-SMIv2", "iDRAC4329alertStorageControllerFailure"),
        ("DELL-MM-MIB-SMIv2", "iDRAC4330alertStorageControllerWarning"),
        ("DELL-MM-MIB-SMIv2", "iDRAC4331alertStorageControllerInformation"),
        ("DELL-MM-MIB-SMIv2", "iDRAC4337alertStorageEnclosureFailure"),
        ("DELL-MM-MIB-SMIv2", "iDRAC4338alertStorageEnclosureWarning"),
        ("DELL-MM-MIB-SMIv2", "iDRAC4339alertStorageEnclosureInformation"),
        ("DELL-MM-MIB-SMIv2", "iDRAC4345alertStoragePhysicalDiskFailure"),
        ("DELL-MM-MIB-SMIv2", "iDRAC4346alertStoragePhysicalDiskWarning"),
        ("DELL-MM-MIB-SMIv2", "iDRAC4347alertStoragePhysicalDiskInformation"),
        ("DELL-MM-MIB-SMIv2", "iDRAC4353alertStorageVirtualDiskFailure"),
        ("DELL-MM-MIB-SMIv2", "iDRAC4354alertStorageVirtualDiskWarning"),
        ("DELL-MM-MIB-SMIv2", "iDRAC4355alertStorageVirtualDiskInformation"),
        ("DELL-MM-MIB-SMIv2", "iDRAC4370alertStorageSolidstateDrive"),
        ("DELL-MM-MIB-SMIv2", "iDRAC4433alertStorageSecurityFailure"),
        ("DELL-MM-MIB-SMIv2", "iDRAC4434alertStorageSecurityWarning"),
        ("DELL-MM-MIB-SMIv2", "iDRAC4435alertStorageSecurityInformation"),
        ("DELL-MM-MIB-SMIv2", "iDRAC4761alertStorageSoftwareDefinedSubSystemFailure"),
        ("DELL-MM-MIB-SMIv2", "iDRAC4762alertStorageSoftwareDefinedSubSystemWarning"),
        ("DELL-MM-MIB-SMIv2", "iDRAC6211alertUpdateJobInformation"),
        ("DELL-MM-MIB-SMIv2", "iDRAC6314alertSoftwareChangeUpdateWarning"),
        ("DELL-MM-MIB-SMIv2", "iDRAC8305alertTemperatureProbeChangeFailure"),
        ("DELL-MM-MIB-SMIv2", "iDRAC8306alertTemperatureProbeReadWarning"),
        ("DELL-MM-MIB-SMIv2", "iDRAC8329alertPowerSupplyAuditFailure"),
        ("DELL-MM-MIB-SMIv2", "iDRAC8330alertPowerSupplyAuditWarning"),
        ("DELL-MM-MIB-SMIv2", "iDRAC8417alertPowerUsageAuditFailure"),
        ("DELL-MM-MIB-SMIv2", "iDRAC8418alertPowerUsageAuditWarning"),
        ("DELL-MM-MIB-SMIv2", "iDRAC8419alertPowerUsageAuditInformation"),
        ("DELL-MM-MIB-SMIv2", "iDRAC8474alertHWCAuditWarning"),
        ("DELL-MM-MIB-SMIv2", "iDRAC8475alertHWCAuditInformation"),
        ("DELL-MM-MIB-SMIv2", "iDRAC8490alertUserTrackingWarning"),
        ("DELL-MM-MIB-SMIv2", "iDRAC8499alertiDRACIPAddressChange"),
        ("DELL-MM-MIB-SMIv2", "iDRAC8513alertLicenseFailure"),
        ("DELL-MM-MIB-SMIv2", "iDRAC8514alertLicenseWarning"),
        ("DELL-MM-MIB-SMIv2", "iDRAC8515alertLicenseInformation"),
        ("DELL-MM-MIB-SMIv2", "iDRAC8562alertPCIDeviceAuditWarning"),
        ("DELL-MM-MIB-SMIv2", "iDRAC8579alertSystemPowerStateChangeInformation"),
        ("DELL-MM-MIB-SMIv2", "iDRAC8594alertDebugWarning"),
        ("DELL-MM-MIB-SMIv2", "iDRAC8595alertDebugInformation"),
        ("DELL-MM-MIB-SMIv2", "iDRAC8674alertRacConfigurationChangewarning"),
        ("DELL-MM-MIB-SMIv2", "iDRAC8675alertRacConfigurationChangeInformation"),
        ("DELL-MM-MIB-SMIv2", "iDRAC8689alertCMCAuditFailure"),
        ("DELL-MM-MIB-SMIv2", "iDRAC8690alertCMCAuditWarning"),
        ("DELL-MM-MIB-SMIv2", "iDRAC8691alertCMCAuditInformation"))
)
if mibBuilder.loadTexts:
    dmmiDRACAlertNotificationGroup.setStatus(
        "current"
    )

dmmNWIOMAlertNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 10, 2, 4)
)
dmmNWIOMAlertNotificationGroup.setObjects(
      *(("DELL-MM-MIB-SMIv2", "nwIOM980021AlertFabricInformational"),
        ("DELL-MM-MIB-SMIv2", "nwIOM980022AlertFabricWarning"),
        ("DELL-MM-MIB-SMIv2", "nwIOM980023AlertFabricCritical"),
        ("DELL-MM-MIB-SMIv2", "nwIOM980024AlertFabricInformational"),
        ("DELL-MM-MIB-SMIv2", "nwIOM980025AlertFabricWarning"),
        ("DELL-MM-MIB-SMIv2", "nwIOM980026AlertFabricInformational"),
        ("DELL-MM-MIB-SMIv2", "nwIOM980027AlertFabricInformational"),
        ("DELL-MM-MIB-SMIv2", "nwIOM980028AlertFabricInformational"),
        ("DELL-MM-MIB-SMIv2", "nwIOM980029AlertFabricCritical"),
        ("DELL-MM-MIB-SMIv2", "nwIOM980030AlertFabricInformational"),
        ("DELL-MM-MIB-SMIv2", "nwIOM980031AlertFabricInformational"),
        ("DELL-MM-MIB-SMIv2", "nwIOM980032AlertFabricInformational"),
        ("DELL-MM-MIB-SMIv2", "nwIOM990001AlertInterfaceInformational"),
        ("DELL-MM-MIB-SMIv2", "nwIOM990002AlertInterfaceWarning"),
        ("DELL-MM-MIB-SMIv2", "nwIOM1000001AlertLinkInformational"),
        ("DELL-MM-MIB-SMIv2", "nwIOM1000002AlertLinkWarning"),
        ("DELL-MM-MIB-SMIv2", "nwIOM1010001AlertNodeInformational"),
        ("DELL-MM-MIB-SMIv2", "nwIOM1010002AlertNodeWarning"),
        ("DELL-MM-MIB-SMIv2", "nwIOM1010003AlertNodeInformational"),
        ("DELL-MM-MIB-SMIv2", "nwIOM1010004AlertNodeWarning"),
        ("DELL-MM-MIB-SMIv2", "nwIOM1010005AlertNodeInformational"),
        ("DELL-MM-MIB-SMIv2", "nwIOM1010006AlertNodeWarning"),
        ("DELL-MM-MIB-SMIv2", "nwIOM1010007AlertNodeWarning"),
        ("DELL-MM-MIB-SMIv2", "nwIOM1020001AlertServerInformational"),
        ("DELL-MM-MIB-SMIv2", "nwIOM1020002AlertServerWarning"),
        ("DELL-MM-MIB-SMIv2", "nwIOM1020003AlertServerInformational"),
        ("DELL-MM-MIB-SMIv2", "nwIOM1020004AlertServerWarning"),
        ("DELL-MM-MIB-SMIv2", "nwIOM1020005AlertServerInformational"),
        ("DELL-MM-MIB-SMIv2", "nwIOM1020006AlertServerWarning"),
        ("DELL-MM-MIB-SMIv2", "nwIOM1020007AlertServerInformational"),
        ("DELL-MM-MIB-SMIv2", "nwIOM1020008AlertServerWarning"),
        ("DELL-MM-MIB-SMIv2", "nwIOM1052505AlertRESTInformational"),
        ("DELL-MM-MIB-SMIv2", "nwIOM1052506AlertRESTInformational"))
)
if mibBuilder.loadTexts:
    dmmNWIOMAlertNotificationGroup.setStatus(
        "current"
    )

dmmSASIOMAlertNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 10, 2, 5)
)
dmmSASIOMAlertNotificationGroup.setObjects(
      *(("DELL-MM-MIB-SMIv2", "sasIOM1120001AlertHealthCritical"),
        ("DELL-MM-MIB-SMIv2", "sasIOM1120002AlertHealthInformational"),
        ("DELL-MM-MIB-SMIv2", "sasIOM1120003AlertHealthCritical"),
        ("DELL-MM-MIB-SMIv2", "sasIOM1120004AlertHealthInformational"),
        ("DELL-MM-MIB-SMIv2", "sasIOM1120005AlertHealthWarning"),
        ("DELL-MM-MIB-SMIv2", "sasIOM1120006AlertHealthInformational"),
        ("DELL-MM-MIB-SMIv2", "sasIOM1120007AlertHealthWarning"),
        ("DELL-MM-MIB-SMIv2", "sasIOM1120008AlertHealthWarning"),
        ("DELL-MM-MIB-SMIv2", "sasIOM1120009AlertHealthInformational"),
        ("DELL-MM-MIB-SMIv2", "sasIOM1120010AlertHealthWarning"),
        ("DELL-MM-MIB-SMIv2", "sasIOM1120011AlertHealthInformational"),
        ("DELL-MM-MIB-SMIv2", "sasIOM1120012AlertHealthWarning"),
        ("DELL-MM-MIB-SMIv2", "sasIOM1120013AlertHealthInformational"),
        ("DELL-MM-MIB-SMIv2", "sasIOM1120016AlertHealthWarning"),
        ("DELL-MM-MIB-SMIv2", "sasIOM1120017AlertHealthInformational"),
        ("DELL-MM-MIB-SMIv2", "sasIOM1120018AlertHealthWarning"),
        ("DELL-MM-MIB-SMIv2", "sasIOM1120019AlertHealthInformational"),
        ("DELL-MM-MIB-SMIv2", "sasIOM1120020AlertHealthInformational"),
        ("DELL-MM-MIB-SMIv2", "sasIOM1120021AlertHealthInformational"),
        ("DELL-MM-MIB-SMIv2", "sasIOM1120022AlertHealthInformational"),
        ("DELL-MM-MIB-SMIv2", "sasIOM1120023AlertHealthInformational"),
        ("DELL-MM-MIB-SMIv2", "sasIOM1120024AlertHealthInformational"),
        ("DELL-MM-MIB-SMIv2", "sasIOM1120025AlertHealthCritical"),
        ("DELL-MM-MIB-SMIv2", "sasIOM1120026AlertHealthInformational"),
        ("DELL-MM-MIB-SMIv2", "sasIOM1120027AlertHealthCritical"),
        ("DELL-MM-MIB-SMIv2", "sasIOM1120028AlertHealthInformational"),
        ("DELL-MM-MIB-SMIv2", "sasIOM1120029AlertHealthWarning"),
        ("DELL-MM-MIB-SMIv2", "sasIOM1120030AlertHealthWarning"),
        ("DELL-MM-MIB-SMIv2", "sasIOM1120031AlertHealthCritical"),
        ("DELL-MM-MIB-SMIv2", "sasIOM1120032AlertHealthInformational"),
        ("DELL-MM-MIB-SMIv2", "sasIOM1120033AlertHealthCritical"),
        ("DELL-MM-MIB-SMIv2", "sasIOM1120034AlertHealthInformational"),
        ("DELL-MM-MIB-SMIv2", "sasIOM1120035AlertHealthInformational"),
        ("DELL-MM-MIB-SMIv2", "sasIOM1120036AlertHealthInformational"),
        ("DELL-MM-MIB-SMIv2", "sasIOM1120039AlertHealthWarning"),
        ("DELL-MM-MIB-SMIv2", "sasIOM1120040AlertHealthCritical"),
        ("DELL-MM-MIB-SMIv2", "sasIOM1120041AlertHealthCritical"),
        ("DELL-MM-MIB-SMIv2", "sasIOM1120042AlertConfigurationCritical"),
        ("DELL-MM-MIB-SMIv2", "sasIOM1120069AlertHealthInformational"),
        ("DELL-MM-MIB-SMIv2", "sasIOM1120072AlertHealthWarning"))
)
if mibBuilder.loadTexts:
    dmmSASIOMAlertNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "DELL-MM-MIB-SMIv2",
    **{"DellString": DellString,
       "DellMmType": DellMmType,
       "DellStatus": DellStatus,
       "DellPowerReading": DellPowerReading,
       "DellPowerIndexRange": DellPowerIndexRange,
       "DellPSUIndexRange": DellPSUIndexRange,
       "DellPSUCapable": DellPSUCapable,
       "DellTemperatureReading": DellTemperatureReading,
       "DellTimestamp": DellTimestamp,
       "dell": dell,
       "server3": server3,
       "dmmOutOfBandGroup": dmmOutOfBandGroup,
       "dmmInformationGroup": dmmInformationGroup,
       "dmmProductInfoGroup": dmmProductInfoGroup,
       "dmmProductName": dmmProductName,
       "dmmProductShortName": dmmProductShortName,
       "dmmProductDescription": dmmProductDescription,
       "dmmProductManufacturer": dmmProductManufacturer,
       "dmmProductVersion": dmmProductVersion,
       "dmmChassisServiceTag": dmmChassisServiceTag,
       "dmmProductURL": dmmProductURL,
       "dmmProductChassisAssetTag": dmmProductChassisAssetTag,
       "dmmProductChassisName": dmmProductChassisName,
       "dmmProductType": dmmProductType,
       "dmmProductChassisDataCenter": dmmProductChassisDataCenter,
       "dmmProductChassisAisle": dmmProductChassisAisle,
       "dmmProductChassisRack": dmmProductChassisRack,
       "dmmProductChassisRackSlot": dmmProductChassisRackSlot,
       "dmmProductChassisModel": dmmProductChassisModel,
       "dmmProductChassisExpressServiceCode": dmmProductChassisExpressServiceCode,
       "dmmProductChassisSystemID": dmmProductChassisSystemID,
       "dmmFirmwareGroup": dmmFirmwareGroup,
       "dmmFirmwareVersion": dmmFirmwareVersion,
       "dmmFirmwareVersion2": dmmFirmwareVersion2,
       "dmmStatusGroup": dmmStatusGroup,
       "dmmGlobalSystemStatus": dmmGlobalSystemStatus,
       "dmmChassisStatusGroup": dmmChassisStatusGroup,
       "dmmStatusNowGroup": dmmStatusNowGroup,
       "dmmIOMCurrStatus": dmmIOMCurrStatus,
       "dmmRedCurrStatus": dmmRedCurrStatus,
       "dmmPowerCurrStatus": dmmPowerCurrStatus,
       "dmmFanCurrStatus": dmmFanCurrStatus,
       "dmmBladeCurrStatus": dmmBladeCurrStatus,
       "dmmTempCurrStatus": dmmTempCurrStatus,
       "dmmMMCurrStatus": dmmMMCurrStatus,
       "dmmChassisFrontPanelAmbientTemperature": dmmChassisFrontPanelAmbientTemperature,
       "dmmChassisPowerGroup": dmmChassisPowerGroup,
       "dmmPowerTable": dmmPowerTable,
       "dmmPowerTableEntry": dmmPowerTableEntry,
       "dmmPowerChassisIndex": dmmPowerChassisIndex,
       "dmmPowerIdlePower": dmmPowerIdlePower,
       "dmmPowerKWhCumulative": dmmPowerKWhCumulative,
       "dmmPowerKWhCumulativeTime": dmmPowerKWhCumulativeTime,
       "dmmPowerWattsPeakUsage": dmmPowerWattsPeakUsage,
       "dmmPowerWattsPeakTime": dmmPowerWattsPeakTime,
       "dmmPowerWattsMinUsage": dmmPowerWattsMinUsage,
       "dmmPowerWattsMinTime": dmmPowerWattsMinTime,
       "dmmPowerWattsReading": dmmPowerWattsReading,
       "dmmPSUTable": dmmPSUTable,
       "dmmPSUTableEntry": dmmPSUTableEntry,
       "dmmPSUChassisIndex": dmmPSUChassisIndex,
       "dmmPSUIndex": dmmPSUIndex,
       "dmmPSULocation": dmmPSULocation,
       "dmmPSUState": dmmPSUState,
       "dmmPSUType": dmmPSUType,
       "dmmPSUCapacity": dmmPSUCapacity,
       "dmmPSUVoltage": dmmPSUVoltage,
       "dmmPSUCurrStatus": dmmPSUCurrStatus,
       "dmmChassisAlert2Group": dmmChassisAlert2Group,
       "alert2FanFailure": alert2FanFailure,
       "alert2FanWarning": alert2FanWarning,
       "alert2FanInformation": alert2FanInformation,
       "alert2TemperatureProbeFailure": alert2TemperatureProbeFailure,
       "alert2TemperatureProbeWarning": alert2TemperatureProbeWarning,
       "alert2TemperatureProbeNormal": alert2TemperatureProbeNormal,
       "alert2VoltageProbeFailure": alert2VoltageProbeFailure,
       "alert2VoltageProbeWarning": alert2VoltageProbeWarning,
       "alert2VoltageProbeNormal": alert2VoltageProbeNormal,
       "alert2AmperageProbeFailure": alert2AmperageProbeFailure,
       "alert2AmperageProbeWarning": alert2AmperageProbeWarning,
       "alert2AmperageProbeNormal": alert2AmperageProbeNormal,
       "alert2PowerSupplyFailure": alert2PowerSupplyFailure,
       "alert2PowerSupplyWarning": alert2PowerSupplyWarning,
       "alert2PowerSupplyNormal": alert2PowerSupplyNormal,
       "alert2BatteryFailure": alert2BatteryFailure,
       "alert2BatteryWarning": alert2BatteryWarning,
       "alert2BatteryNormal": alert2BatteryNormal,
       "alert2LinkStatusFailure": alert2LinkStatusFailure,
       "alert2LinkStatusWarning": alert2LinkStatusWarning,
       "alert2LinkStatusInformation": alert2LinkStatusInformation,
       "alert2PowerUsageFailure": alert2PowerUsageFailure,
       "alert2PowerUsageWarning": alert2PowerUsageWarning,
       "alert2PowerUsageInformation": alert2PowerUsageInformation,
       "alert2HardwareConfigurationFailure": alert2HardwareConfigurationFailure,
       "alert2HardwareConfigurationWarning": alert2HardwareConfigurationWarning,
       "alert2HardwareConfigurationInformation": alert2HardwareConfigurationInformation,
       "alert2SoftwareConfigurationFailure": alert2SoftwareConfigurationFailure,
       "alert2SoftwareConfigurationWarning": alert2SoftwareConfigurationWarning,
       "alert2SoftwareConfigurationInformation": alert2SoftwareConfigurationInformation,
       "alert2SystemEventLogFailure": alert2SystemEventLogFailure,
       "alert2SystemEventLogWarning": alert2SystemEventLogWarning,
       "alert2SystemEventLogInformation": alert2SystemEventLogInformation,
       "alert2SecurityFailure": alert2SecurityFailure,
       "alert2SecurityWarning": alert2SecurityWarning,
       "alert2SecurityInformation": alert2SecurityInformation,
       "alert2CableFailure": alert2CableFailure,
       "alert2PowerSupplyAbsent": alert2PowerSupplyAbsent,
       "alert2RedundancyLost": alert2RedundancyLost,
       "alert2RedundancyDegraded": alert2RedundancyDegraded,
       "alert2RedundancyInformation": alert2RedundancyInformation,
       "alert2CMCFailure": alert2CMCFailure,
       "alert2CMCWarning": alert2CMCWarning,
       "alert2IOVirtualizationFailure": alert2IOVirtualizationFailure,
       "alert2IOVirtualizationWarning": alert2IOVirtualizationWarning,
       "alert2IOVirtualizationInformation": alert2IOVirtualizationInformation,
       "alert2StorageManagementFailure": alert2StorageManagementFailure,
       "alert2StorageManagementWarning": alert2StorageManagementWarning,
       "alert2StorageManagementInformation": alert2StorageManagementInformation,
       "alert2StorageFanFailure": alert2StorageFanFailure,
       "alert2StorageFanWarning": alert2StorageFanWarning,
       "alert2StorageFanInformation": alert2StorageFanInformation,
       "alert2StorageTemperatureProbeFailure": alert2StorageTemperatureProbeFailure,
       "alert2StorageTemperatureProbeWarning": alert2StorageTemperatureProbeWarning,
       "alert2StorageTemperatureProbeInformation": alert2StorageTemperatureProbeInformation,
       "alert2StoragePowerSupplyFailure": alert2StoragePowerSupplyFailure,
       "alert2StoragePowerSupplyWarning": alert2StoragePowerSupplyWarning,
       "alert2StoragePowerSupplyInformation": alert2StoragePowerSupplyInformation,
       "alert2StorageBatteryFailure": alert2StorageBatteryFailure,
       "alert2StorageBatteryWarning": alert2StorageBatteryWarning,
       "alert2StorageBatteryInformation": alert2StorageBatteryInformation,
       "alert2StorageControllerFailure": alert2StorageControllerFailure,
       "alert2StorageControllerWarning": alert2StorageControllerWarning,
       "alert2StorageControllerInformation": alert2StorageControllerInformation,
       "alert2StorageEnclosureFailure": alert2StorageEnclosureFailure,
       "alert2StorageEnclosureWarning": alert2StorageEnclosureWarning,
       "alert2StorageEnclosureInformation": alert2StorageEnclosureInformation,
       "alert2StoragePhysicalDiskFailure": alert2StoragePhysicalDiskFailure,
       "alert2StoragePhysicalDiskWarning": alert2StoragePhysicalDiskWarning,
       "alert2StoragePhysicalDiskInformation": alert2StoragePhysicalDiskInformation,
       "alert2StorageVirtualDiskFailure": alert2StorageVirtualDiskFailure,
       "alert2StorageVirtualDiskWarning": alert2StorageVirtualDiskWarning,
       "alert2StorageVirtualDiskInformation": alert2StorageVirtualDiskInformation,
       "alert2StorageSecurityFailure": alert2StorageSecurityFailure,
       "alert2StorageSecurityWarning": alert2StorageSecurityWarning,
       "alert2StorageSecurityInformation": alert2StorageSecurityInformation,
       "alert2SoftwareChangeUpdateWarning": alert2SoftwareChangeUpdateWarning,
       "alert2PowerSupplyAuditFailure": alert2PowerSupplyAuditFailure,
       "alert2PowerSupplyAuditWarning": alert2PowerSupplyAuditWarning,
       "alert2SoftwareChangeAuditFailure": alert2SoftwareChangeAuditFailure,
       "alert2PowerUsageAuditFailure": alert2PowerUsageAuditFailure,
       "alert2PowerUsageAuditWarning": alert2PowerUsageAuditWarning,
       "alert2PowerUsageAuditInformation": alert2PowerUsageAuditInformation,
       "alert2LicenseFailure": alert2LicenseFailure,
       "alert2LicenseWarning": alert2LicenseWarning,
       "alert2LicenseInformation": alert2LicenseInformation,
       "alert2PCIDeviceAuditWarning": alert2PCIDeviceAuditWarning,
       "alert2CMCAuditFailure": alert2CMCAuditFailure,
       "alert2CMCAuditWarning": alert2CMCAuditWarning,
       "alert2CMCAuditInformation": alert2CMCAuditInformation,
       "alert2IOVirtualizationAuditWarning": alert2IOVirtualizationAuditWarning,
       "alert2CMCTestTrap": alert2CMCTestTrap,
       "alert2SWCConfigurationFailure": alert2SWCConfigurationFailure,
       "alert2SWCConfigurationWarning": alert2SWCConfigurationWarning,
       "alert2PCIDeviceConfigurationInformation": alert2PCIDeviceConfigurationInformation,
       "alert2IOVConfigurationWarning": alert2IOVConfigurationWarning,
       "alert2IOVConfigurationInformation": alert2IOVConfigurationInformation,
       "alert851138RCPRestoreInformational": alert851138RCPRestoreInformational,
       "alert851139RCPRestoreCritical": alert851139RCPRestoreCritical,
       "alert856129DeviceStateInformational": alert856129DeviceStateInformational,
       "alert856130DeviceStateCritical": alert856130DeviceStateCritical,
       "alert856131DeviceStateCritical": alert856131DeviceStateCritical,
       "alert856132DeviceStateInformational": alert856132DeviceStateInformational,
       "alert856133DeviceStateInformational": alert856133DeviceStateInformational,
       "alert856134DeviceStateInformational": alert856134DeviceStateInformational,
       "alert856172DeviceStateInformational": alert856172DeviceStateInformational,
       "alert856173DeviceStateCritical": alert856173DeviceStateCritical,
       "alert856174DeviceStateCritical": alert856174DeviceStateCritical,
       "alert856175DeviceStateWarning": alert856175DeviceStateWarning,
       "dmmChassisAlert2Variables": dmmChassisAlert2Variables,
       "dmmCA2MessageID": dmmCA2MessageID,
       "dmmCA2Message": dmmCA2Message,
       "dmmCA2MessageArgs": dmmCA2MessageArgs,
       "dmmCA2AlertStatus": dmmCA2AlertStatus,
       "dmmCA2FQDD": dmmCA2FQDD,
       "dmmGenericAlertGroup": dmmGenericAlertGroup,
       "alertGenericCritical": alertGenericCritical,
       "alertGenericWarning": alertGenericWarning,
       "alertGenericNormal": alertGenericNormal,
       "alertGenericInformational": alertGenericInformational,
       "alertGenericTestTrapEvent": alertGenericTestTrapEvent,
       "alertAuditCritical": alertAuditCritical,
       "alertAuditWarning": alertAuditWarning,
       "alertAuditNormal": alertAuditNormal,
       "alertAuditInformational": alertAuditInformational,
       "dmmGenericAlertVariables": dmmGenericAlertVariables,
       "dmmDeviceServiceTag": dmmDeviceServiceTag,
       "dmmCategoryName": dmmCategoryName,
       "dmmSubCategoryName": dmmSubCategoryName,
       "dmmSeverity": dmmSeverity,
       "dmmiDRACAlertGroup": dmmiDRACAlertGroup,
       "iDRAC2089alertNetworkFailure": iDRAC2089alertNetworkFailure,
       "iDRAC2090alertNetworkWarning": iDRAC2090alertNetworkWarning,
       "iDRAC2091alertNetworkInformation": iDRAC2091alertNetworkInformation,
       "iDRAC2153alertFanFailure": iDRAC2153alertFanFailure,
       "iDRAC2154alertFanWarning": iDRAC2154alertFanWarning,
       "iDRAC2155alertFanInformation": iDRAC2155alertFanInformation,
       "iDRAC2161alertTemperatureProbeFailure": iDRAC2161alertTemperatureProbeFailure,
       "iDRAC2162alertTemperatureProbeWarning": iDRAC2162alertTemperatureProbeWarning,
       "iDRAC2163alertTemperatureProbeNormal": iDRAC2163alertTemperatureProbeNormal,
       "iDRAC2169alertVoltageProbeFailure": iDRAC2169alertVoltageProbeFailure,
       "iDRAC2170alertVoltageProbeWarning": iDRAC2170alertVoltageProbeWarning,
       "iDRAC2171alertVoltageProbeNormal": iDRAC2171alertVoltageProbeNormal,
       "iDRAC2177alertAmperageProbeFailure": iDRAC2177alertAmperageProbeFailure,
       "iDRAC2178alertAmperageProbeWarning": iDRAC2178alertAmperageProbeWarning,
       "iDRAC2179alertAmperageProbeNormal": iDRAC2179alertAmperageProbeNormal,
       "iDRAC2185alertPowerSupplyFailure": iDRAC2185alertPowerSupplyFailure,
       "iDRAC2186alertPowerSupplyWarning": iDRAC2186alertPowerSupplyWarning,
       "iDRAC2187alertPowerSupplyNormal": iDRAC2187alertPowerSupplyNormal,
       "iDRAC2209alertIntegratedDualSDModuleFailure": iDRAC2209alertIntegratedDualSDModuleFailure,
       "iDRAC2210alertIntegratedDualSDModuleWarning": iDRAC2210alertIntegratedDualSDModuleWarning,
       "iDRAC2211alertIntegratedDualSDModuleInformation": iDRAC2211alertIntegratedDualSDModuleInformation,
       "iDRAC2225alertBatteryFailure": iDRAC2225alertBatteryFailure,
       "iDRAC2226alertBatteryWarning": iDRAC2226alertBatteryWarning,
       "iDRAC2227alertBatteryNormal": iDRAC2227alertBatteryNormal,
       "iDRAC2233alertAutomaticSystemRecovery": iDRAC2233alertAutomaticSystemRecovery,
       "iDRAC2241alertProcessorDeviceStatusFailure": iDRAC2241alertProcessorDeviceStatusFailure,
       "iDRAC2242alertProcessorDeviceStatusWarning": iDRAC2242alertProcessorDeviceStatusWarning,
       "iDRAC2243alertProcessorDeviceStatusNormal": iDRAC2243alertProcessorDeviceStatusNormal,
       "iDRAC2249alertLinkStatusFailure": iDRAC2249alertLinkStatusFailure,
       "iDRAC2250alertLinkStatusWarning": iDRAC2250alertLinkStatusWarning,
       "iDRAC2251alertLinkStatusInformation": iDRAC2251alertLinkStatusInformation,
       "iDRAC2265alertMemoryDeviceFailure": iDRAC2265alertMemoryDeviceFailure,
       "iDRAC2266alertMemoryDeviceWarning": iDRAC2266alertMemoryDeviceWarning,
       "iDRAC2267alertMemoryDeviceInformation": iDRAC2267alertMemoryDeviceInformation,
       "iDRAC2273alertPowerUsageFailure": iDRAC2273alertPowerUsageFailure,
       "iDRAC2274alertPowerUsageWarning": iDRAC2274alertPowerUsageWarning,
       "iDRAC2275alertPowerUsageInformation": iDRAC2275alertPowerUsageInformation,
       "iDRAC2297alertPhysicalDiskFailure": iDRAC2297alertPhysicalDiskFailure,
       "iDRAC2298alertPhysicalDiskWarning": iDRAC2298alertPhysicalDiskWarning,
       "iDRAC2299alertPhysicalDiskInformation": iDRAC2299alertPhysicalDiskInformation,
       "iDRAC2329alertHardwareConfigurationFailure": iDRAC2329alertHardwareConfigurationFailure,
       "iDRAC2330alertHardwareConfigurationWarning": iDRAC2330alertHardwareConfigurationWarning,
       "iDRAC2331alertHardwareConfigurationInformation": iDRAC2331alertHardwareConfigurationInformation,
       "iDRAC2337alertSoftwareConfigurationFailure": iDRAC2337alertSoftwareConfigurationFailure,
       "iDRAC2338alertSoftwareConfigurationWarning": iDRAC2338alertSoftwareConfigurationWarning,
       "iDRAC2339alertSoftwareConfigurationInformation": iDRAC2339alertSoftwareConfigurationInformation,
       "iDRAC2377alertSystemEventLogFailure": iDRAC2377alertSystemEventLogFailure,
       "iDRAC2378alertSystemEventLogWarning": iDRAC2378alertSystemEventLogWarning,
       "iDRAC2379alertSystemEventLogInformation": iDRAC2379alertSystemEventLogInformation,
       "iDRAC2385alertSecurityFailure": iDRAC2385alertSecurityFailure,
       "iDRAC2386alertSecurityWarning": iDRAC2386alertSecurityWarning,
       "iDRAC2387alertSecurityInformation": iDRAC2387alertSecurityInformation,
       "iDRAC2393alertCableFailure": iDRAC2393alertCableFailure,
       "iDRAC2409alertOSFailure": iDRAC2409alertOSFailure,
       "iDRAC2411alertOSInformation": iDRAC2411alertOSInformation,
       "iDRAC2417alertPCIDeviceFailure": iDRAC2417alertPCIDeviceFailure,
       "iDRAC2418alertPCIDeviceWarning": iDRAC2418alertPCIDeviceWarning,
       "iDRAC2419alertPCIDeviceInformation": iDRAC2419alertPCIDeviceInformation,
       "iDRAC2425alertBiosPostFailure": iDRAC2425alertBiosPostFailure,
       "iDRAC2433alertInternaliDRACMemoryUnresponsive": iDRAC2433alertInternaliDRACMemoryUnresponsive,
       "iDRAC2435alertServerIdleTime": iDRAC2435alertServerIdleTime,
       "iDRAC2457alertProcessorDeviceAbsent": iDRAC2457alertProcessorDeviceAbsent,
       "iDRAC2465alertPowerSupplyAbsent": iDRAC2465alertPowerSupplyAbsent,
       "iDRAC2473alertRedundancyLost": iDRAC2473alertRedundancyLost,
       "iDRAC2474alertRedundancyDegraded": iDRAC2474alertRedundancyDegraded,
       "iDRAC2475alertRedundancyInformation": iDRAC2475alertRedundancyInformation,
       "iDRAC2481alertIntegratedDualSDModuleAbsent": iDRAC2481alertIntegratedDualSDModuleAbsent,
       "iDRAC2489alertIntegratedDualSDModuleRedundancyLost": iDRAC2489alertIntegratedDualSDModuleRedundancyLost,
       "iDRAC2490alertIntegratedDualSDModuleRedundancyDegraded": iDRAC2490alertIntegratedDualSDModuleRedundancyDegraded,
       "iDRAC2491alertIntegratedDualSDModuleRedundancyInformation": iDRAC2491alertIntegratedDualSDModuleRedundancyInformation,
       "iDRAC2505alertvFlashMediaDeviceFailure": iDRAC2505alertvFlashMediaDeviceFailure,
       "iDRAC2506alertvFlashMediaDeviceWarning": iDRAC2506alertvFlashMediaDeviceWarning,
       "iDRAC2507alertvFlashMediaDeviceInformation": iDRAC2507alertvFlashMediaDeviceInformation,
       "iDRAC2515alertvFlashMediaDeviceAbsent": iDRAC2515alertvFlashMediaDeviceAbsent,
       "iDRAC2521alertTemperatureStatisticsFailure": iDRAC2521alertTemperatureStatisticsFailure,
       "iDRAC2522alertTemperatureStatisticsWarning": iDRAC2522alertTemperatureStatisticsWarning,
       "iDRAC2531alertRACInformation": iDRAC2531alertRACInformation,
       "iDRAC2537alertFiberChannelFailure": iDRAC2537alertFiberChannelFailure,
       "iDRAC2538alertFiberChannelWarning": iDRAC2538alertFiberChannelWarning,
       "iDRAC2539alertFiberChannelInformation": iDRAC2539alertFiberChannelInformation,
       "iDRAC2545alertCMCFailure": iDRAC2545alertCMCFailure,
       "iDRAC2546alertCMCWarning": iDRAC2546alertCMCWarning,
       "iDRAC2553alertIOVirtualizationFailure": iDRAC2553alertIOVirtualizationFailure,
       "iDRAC2650alertSystemPerformanceWarning": iDRAC2650alertSystemPerformanceWarning,
       "iDRAC3049alertLiquidCoolingLeakFailure": iDRAC3049alertLiquidCoolingLeakFailure,
       "iDRAC3050alertLiquidCoolingLeakWarning": iDRAC3050alertLiquidCoolingLeakWarning,
       "iDRAC3051alertLiquidCoolingLeakInformational": iDRAC3051alertLiquidCoolingLeakInformational,
       "iDRAC3082alertSDKSystemWarning": iDRAC3082alertSDKSystemWarning,
       "iDRAC3083alertSDKSystemInformational": iDRAC3083alertSDKSystemInformational,
       "iDRAC4177alertStorageManagementFailure": iDRAC4177alertStorageManagementFailure,
       "iDRAC4178alertStorageManagementWarning": iDRAC4178alertStorageManagementWarning,
       "iDRAC4179alertStorageManagementInformation": iDRAC4179alertStorageManagementInformation,
       "iDRAC4201alertStorageFanFailure": iDRAC4201alertStorageFanFailure,
       "iDRAC4202alertStorageFanWarning": iDRAC4202alertStorageFanWarning,
       "iDRAC4203alertStorageFanInformation": iDRAC4203alertStorageFanInformation,
       "iDRAC4209alertStorageTemperatureProbeFailure": iDRAC4209alertStorageTemperatureProbeFailure,
       "iDRAC4210alertStorageTemperatureProbeWarning": iDRAC4210alertStorageTemperatureProbeWarning,
       "iDRAC4211alertStorageTemperatureProbeInformation": iDRAC4211alertStorageTemperatureProbeInformation,
       "iDRAC4233alertStoragePowerSupplyFailure": iDRAC4233alertStoragePowerSupplyFailure,
       "iDRAC4234alertStoragePowerSupplyWarning": iDRAC4234alertStoragePowerSupplyWarning,
       "iDRAC4235alertStoragePowerSupplyInformation": iDRAC4235alertStoragePowerSupplyInformation,
       "iDRAC4273alertStorageBatteryFailure": iDRAC4273alertStorageBatteryFailure,
       "iDRAC4274alertStorageBatteryWarning": iDRAC4274alertStorageBatteryWarning,
       "iDRAC4275alertStorageBatteryInformation": iDRAC4275alertStorageBatteryInformation,
       "iDRAC4329alertStorageControllerFailure": iDRAC4329alertStorageControllerFailure,
       "iDRAC4330alertStorageControllerWarning": iDRAC4330alertStorageControllerWarning,
       "iDRAC4331alertStorageControllerInformation": iDRAC4331alertStorageControllerInformation,
       "iDRAC4337alertStorageEnclosureFailure": iDRAC4337alertStorageEnclosureFailure,
       "iDRAC4338alertStorageEnclosureWarning": iDRAC4338alertStorageEnclosureWarning,
       "iDRAC4339alertStorageEnclosureInformation": iDRAC4339alertStorageEnclosureInformation,
       "iDRAC4345alertStoragePhysicalDiskFailure": iDRAC4345alertStoragePhysicalDiskFailure,
       "iDRAC4346alertStoragePhysicalDiskWarning": iDRAC4346alertStoragePhysicalDiskWarning,
       "iDRAC4347alertStoragePhysicalDiskInformation": iDRAC4347alertStoragePhysicalDiskInformation,
       "iDRAC4353alertStorageVirtualDiskFailure": iDRAC4353alertStorageVirtualDiskFailure,
       "iDRAC4354alertStorageVirtualDiskWarning": iDRAC4354alertStorageVirtualDiskWarning,
       "iDRAC4355alertStorageVirtualDiskInformation": iDRAC4355alertStorageVirtualDiskInformation,
       "iDRAC4370alertStorageSolidstateDrive": iDRAC4370alertStorageSolidstateDrive,
       "iDRAC4433alertStorageSecurityFailure": iDRAC4433alertStorageSecurityFailure,
       "iDRAC4434alertStorageSecurityWarning": iDRAC4434alertStorageSecurityWarning,
       "iDRAC4435alertStorageSecurityInformation": iDRAC4435alertStorageSecurityInformation,
       "iDRAC4761alertStorageSoftwareDefinedSubSystemFailure": iDRAC4761alertStorageSoftwareDefinedSubSystemFailure,
       "iDRAC4762alertStorageSoftwareDefinedSubSystemWarning": iDRAC4762alertStorageSoftwareDefinedSubSystemWarning,
       "iDRAC6211alertUpdateJobInformation": iDRAC6211alertUpdateJobInformation,
       "iDRAC6314alertSoftwareChangeUpdateWarning": iDRAC6314alertSoftwareChangeUpdateWarning,
       "iDRAC8305alertTemperatureProbeChangeFailure": iDRAC8305alertTemperatureProbeChangeFailure,
       "iDRAC8306alertTemperatureProbeReadWarning": iDRAC8306alertTemperatureProbeReadWarning,
       "iDRAC8329alertPowerSupplyAuditFailure": iDRAC8329alertPowerSupplyAuditFailure,
       "iDRAC8330alertPowerSupplyAuditWarning": iDRAC8330alertPowerSupplyAuditWarning,
       "iDRAC8417alertPowerUsageAuditFailure": iDRAC8417alertPowerUsageAuditFailure,
       "iDRAC8418alertPowerUsageAuditWarning": iDRAC8418alertPowerUsageAuditWarning,
       "iDRAC8419alertPowerUsageAuditInformation": iDRAC8419alertPowerUsageAuditInformation,
       "iDRAC8474alertHWCAuditWarning": iDRAC8474alertHWCAuditWarning,
       "iDRAC8475alertHWCAuditInformation": iDRAC8475alertHWCAuditInformation,
       "iDRAC8490alertUserTrackingWarning": iDRAC8490alertUserTrackingWarning,
       "iDRAC8499alertiDRACIPAddressChange": iDRAC8499alertiDRACIPAddressChange,
       "iDRAC8513alertLicenseFailure": iDRAC8513alertLicenseFailure,
       "iDRAC8514alertLicenseWarning": iDRAC8514alertLicenseWarning,
       "iDRAC8515alertLicenseInformation": iDRAC8515alertLicenseInformation,
       "iDRAC8562alertPCIDeviceAuditWarning": iDRAC8562alertPCIDeviceAuditWarning,
       "iDRAC8579alertSystemPowerStateChangeInformation": iDRAC8579alertSystemPowerStateChangeInformation,
       "iDRAC8594alertDebugWarning": iDRAC8594alertDebugWarning,
       "iDRAC8595alertDebugInformation": iDRAC8595alertDebugInformation,
       "iDRAC8674alertRacConfigurationChangewarning": iDRAC8674alertRacConfigurationChangewarning,
       "iDRAC8675alertRacConfigurationChangeInformation": iDRAC8675alertRacConfigurationChangeInformation,
       "iDRAC8689alertCMCAuditFailure": iDRAC8689alertCMCAuditFailure,
       "iDRAC8690alertCMCAuditWarning": iDRAC8690alertCMCAuditWarning,
       "iDRAC8691alertCMCAuditInformation": iDRAC8691alertCMCAuditInformation,
       "iDRAC10267alertJobControlConfigurationInformation": iDRAC10267alertJobControlConfigurationInformation,
       "iDRAC10298alertPRDeviceDetectionWarning": iDRAC10298alertPRDeviceDetectionWarning,
       "iDRAC10395alertTestTrapEvent": iDRAC10395alertTestTrapEvent,
       "iDRAC10529alertSWCConfigurationFailure": iDRAC10529alertSWCConfigurationFailure,
       "iDRAC10530alertSWCConfigurationWarning": iDRAC10530alertSWCConfigurationWarning,
       "iDRAC10531alertSWCConfigurationInformation": iDRAC10531alertSWCConfigurationInformation,
       "iDRAC10547alertIPAddressConfigurationInformation": iDRAC10547alertIPAddressConfigurationInformation,
       "iDRAC10578alertSecurityConfigurationWarning": iDRAC10578alertSecurityConfigurationWarning,
       "iDRAC10611alertPCIDeviceConfigurationInformation": iDRAC10611alertPCIDeviceConfigurationInformation,
       "iDRAC10627alertSystemConfigurationChangeInformation": iDRAC10627alertSystemConfigurationChangeInformation,
       "iDRAC10635alertAutoDiscoveryInformation": iDRAC10635alertAutoDiscoveryInformation,
       "iDRAC10770alertNetworkConfigurationWarning": iDRAC10770alertNetworkConfigurationWarning,
       "iDRAC10771alertNetworkConfigurationInformation": iDRAC10771alertNetworkConfigurationInformation,
       "iDRAC11274alertSDKConfigurationWarning": iDRAC11274alertSDKConfigurationWarning,
       "iDRAC11275alertSDKConfigurationInformation": iDRAC11275alertSDKConfigurationInformation,
       "dmmNWIOMAlertGroup": dmmNWIOMAlertGroup,
       "nwIOM980021AlertFabricInformational": nwIOM980021AlertFabricInformational,
       "nwIOM980022AlertFabricWarning": nwIOM980022AlertFabricWarning,
       "nwIOM980023AlertFabricCritical": nwIOM980023AlertFabricCritical,
       "nwIOM980024AlertFabricInformational": nwIOM980024AlertFabricInformational,
       "nwIOM980025AlertFabricWarning": nwIOM980025AlertFabricWarning,
       "nwIOM980026AlertFabricInformational": nwIOM980026AlertFabricInformational,
       "nwIOM980027AlertFabricInformational": nwIOM980027AlertFabricInformational,
       "nwIOM980028AlertFabricInformational": nwIOM980028AlertFabricInformational,
       "nwIOM980029AlertFabricCritical": nwIOM980029AlertFabricCritical,
       "nwIOM980030AlertFabricInformational": nwIOM980030AlertFabricInformational,
       "nwIOM980031AlertFabricInformational": nwIOM980031AlertFabricInformational,
       "nwIOM980032AlertFabricInformational": nwIOM980032AlertFabricInformational,
       "nwIOM990001AlertInterfaceInformational": nwIOM990001AlertInterfaceInformational,
       "nwIOM990002AlertInterfaceWarning": nwIOM990002AlertInterfaceWarning,
       "nwIOM1000001AlertLinkInformational": nwIOM1000001AlertLinkInformational,
       "nwIOM1000002AlertLinkWarning": nwIOM1000002AlertLinkWarning,
       "nwIOM1010001AlertNodeInformational": nwIOM1010001AlertNodeInformational,
       "nwIOM1010002AlertNodeWarning": nwIOM1010002AlertNodeWarning,
       "nwIOM1010003AlertNodeInformational": nwIOM1010003AlertNodeInformational,
       "nwIOM1010004AlertNodeWarning": nwIOM1010004AlertNodeWarning,
       "nwIOM1010005AlertNodeInformational": nwIOM1010005AlertNodeInformational,
       "nwIOM1010006AlertNodeWarning": nwIOM1010006AlertNodeWarning,
       "nwIOM1010007AlertNodeWarning": nwIOM1010007AlertNodeWarning,
       "nwIOM1020001AlertServerInformational": nwIOM1020001AlertServerInformational,
       "nwIOM1020002AlertServerWarning": nwIOM1020002AlertServerWarning,
       "nwIOM1020003AlertServerInformational": nwIOM1020003AlertServerInformational,
       "nwIOM1020004AlertServerWarning": nwIOM1020004AlertServerWarning,
       "nwIOM1020005AlertServerInformational": nwIOM1020005AlertServerInformational,
       "nwIOM1020006AlertServerWarning": nwIOM1020006AlertServerWarning,
       "nwIOM1020007AlertServerInformational": nwIOM1020007AlertServerInformational,
       "nwIOM1020008AlertServerWarning": nwIOM1020008AlertServerWarning,
       "nwIOM1052505AlertRESTInformational": nwIOM1052505AlertRESTInformational,
       "nwIOM1052506AlertRESTInformational": nwIOM1052506AlertRESTInformational,
       "dmmSASIOMAlertGroup": dmmSASIOMAlertGroup,
       "sasIOM1120001AlertHealthCritical": sasIOM1120001AlertHealthCritical,
       "sasIOM1120002AlertHealthInformational": sasIOM1120002AlertHealthInformational,
       "sasIOM1120003AlertHealthCritical": sasIOM1120003AlertHealthCritical,
       "sasIOM1120004AlertHealthInformational": sasIOM1120004AlertHealthInformational,
       "sasIOM1120005AlertHealthWarning": sasIOM1120005AlertHealthWarning,
       "sasIOM1120006AlertHealthInformational": sasIOM1120006AlertHealthInformational,
       "sasIOM1120007AlertHealthWarning": sasIOM1120007AlertHealthWarning,
       "sasIOM1120008AlertHealthWarning": sasIOM1120008AlertHealthWarning,
       "sasIOM1120009AlertHealthInformational": sasIOM1120009AlertHealthInformational,
       "sasIOM1120010AlertHealthWarning": sasIOM1120010AlertHealthWarning,
       "sasIOM1120011AlertHealthInformational": sasIOM1120011AlertHealthInformational,
       "sasIOM1120012AlertHealthWarning": sasIOM1120012AlertHealthWarning,
       "sasIOM1120013AlertHealthInformational": sasIOM1120013AlertHealthInformational,
       "sasIOM1120016AlertHealthWarning": sasIOM1120016AlertHealthWarning,
       "sasIOM1120017AlertHealthInformational": sasIOM1120017AlertHealthInformational,
       "sasIOM1120018AlertHealthWarning": sasIOM1120018AlertHealthWarning,
       "sasIOM1120019AlertHealthInformational": sasIOM1120019AlertHealthInformational,
       "sasIOM1120020AlertHealthInformational": sasIOM1120020AlertHealthInformational,
       "sasIOM1120021AlertHealthInformational": sasIOM1120021AlertHealthInformational,
       "sasIOM1120022AlertHealthInformational": sasIOM1120022AlertHealthInformational,
       "sasIOM1120023AlertHealthInformational": sasIOM1120023AlertHealthInformational,
       "sasIOM1120024AlertHealthInformational": sasIOM1120024AlertHealthInformational,
       "sasIOM1120025AlertHealthCritical": sasIOM1120025AlertHealthCritical,
       "sasIOM1120026AlertHealthInformational": sasIOM1120026AlertHealthInformational,
       "sasIOM1120027AlertHealthCritical": sasIOM1120027AlertHealthCritical,
       "sasIOM1120028AlertHealthInformational": sasIOM1120028AlertHealthInformational,
       "sasIOM1120029AlertHealthWarning": sasIOM1120029AlertHealthWarning,
       "sasIOM1120030AlertHealthWarning": sasIOM1120030AlertHealthWarning,
       "sasIOM1120031AlertHealthCritical": sasIOM1120031AlertHealthCritical,
       "sasIOM1120032AlertHealthInformational": sasIOM1120032AlertHealthInformational,
       "sasIOM1120033AlertHealthCritical": sasIOM1120033AlertHealthCritical,
       "sasIOM1120034AlertHealthInformational": sasIOM1120034AlertHealthInformational,
       "sasIOM1120035AlertHealthInformational": sasIOM1120035AlertHealthInformational,
       "sasIOM1120036AlertHealthInformational": sasIOM1120036AlertHealthInformational,
       "sasIOM1120039AlertHealthWarning": sasIOM1120039AlertHealthWarning,
       "sasIOM1120040AlertHealthCritical": sasIOM1120040AlertHealthCritical,
       "sasIOM1120041AlertHealthCritical": sasIOM1120041AlertHealthCritical,
       "sasIOM1120042AlertConfigurationCritical": sasIOM1120042AlertConfigurationCritical,
       "sasIOM1120069AlertHealthInformational": sasIOM1120069AlertHealthInformational,
       "sasIOM1120072AlertHealthWarning": sasIOM1120072AlertHealthWarning,
       "conformanceGroup": conformanceGroup,
       "conformanceMIBGroups": conformanceMIBGroups,
       "dmmProductInfoObjGroup": dmmProductInfoObjGroup,
       "dmmFirmwareObjGroup": dmmFirmwareObjGroup,
       "dmmStatusObjGroup": dmmStatusObjGroup,
       "dmmStatusNowObjGroup": dmmStatusNowObjGroup,
       "dmmChassisPowerObjGroup": dmmChassisPowerObjGroup,
       "dmmPowerTableObjEntry": dmmPowerTableObjEntry,
       "dmmPSUTableObjEntry": dmmPSUTableObjEntry,
       "dmmChassisAlert2VariablesObj": dmmChassisAlert2VariablesObj,
       "dmmGenericAlertVariablesObj": dmmGenericAlertVariablesObj,
       "conformanceMIBnotificationGroup": conformanceMIBnotificationGroup,
       "dmmChassisAlert2NotificationGroup": dmmChassisAlert2NotificationGroup,
       "dmmGenericAlertNotificationGroup": dmmGenericAlertNotificationGroup,
       "dmmiDRACAlertNotificationGroup": dmmiDRACAlertNotificationGroup,
       "dmmNWIOMAlertNotificationGroup": dmmNWIOMAlertNotificationGroup,
       "dmmSASIOMAlertNotificationGroup": dmmSASIOMAlertNotificationGroup}
)
