# SNMP MIB module (DELL-RAC-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\dell\DELL-RAC-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:35:52 2025
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
 NotificationType,
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
    "NotificationType",
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



class DellString(DisplayString):
    """Custom type DellString based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 1023),
    )





class DellRacType(Integer32):
    """Custom type DellRacType based on Integer32"""
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
              16,
              17,
              18,
              19,
              32,
              33)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("unknown", 2),
          ("dracIII", 3),
          ("era", 4),
          ("drac4", 5),
          ("drac5", 6),
          ("drac5MC", 7),
          ("cmc", 8),
          ("idrac", 9),
          ("idrac7monolithic", 16),
          ("idrac7modular", 17),
          ("vrtxCMC", 18),
          ("fx2CMC", 19),
          ("idrac8monolithic", 32),
          ("idrac8modular", 33))
    )





class DellStatus(Integer32):
    """Custom type DellStatus based on Integer32"""
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





class DellPowerReading(DisplayString):
    """Custom type DellPowerReading based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )





class DellCMCPowerIndexRange(Integer32):
    """Custom type DellCMCPowerIndexRange based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )





class DellCMCPSUIndexRange(Integer32):
    """Custom type DellCMCPSUIndexRange based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 6),
    )





class DellCMCPSUCapable(Integer32):
    """Custom type DellCMCPSUCapable based on Integer32"""
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





class DellTemperatureReading(Integer32):
    """Custom type DellTemperatureReading based on Integer32"""




class DellTimestamp(DisplayString):
    """Custom type DellTimestamp based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(26, 26),
    )
    fixed_length = 26





class DellCMCServerIndexRange(Integer32):
    """Custom type DellCMCServerIndexRange based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )





class DellCMCServerCapable(Integer32):
    """Custom type DellCMCServerCapable based on Integer32"""
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
        *(("absent", 1),
          ("none", 2),
          ("basic", 3),
          ("off", 4))
    )





class DellCMCServerStorageMode(Integer32):
    """Custom type DellCMCServerStorageMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              99)
        )
    )
    namedValues = NamedValues(
        *(("notApplicable", 1),
          ("joined", 2),
          ("splitDualHost", 3),
          ("splitSingleHost", 4),
          ("unknown", 99))
    )





class DellCMCServerIntrusionState(Integer32):
    """Custom type DellCMCServerIntrusionState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              99)
        )
    )
    namedValues = NamedValues(
        *(("notApplicable", 1),
          ("closed", 2),
          ("open", 3),
          ("unknown", 99))
    )





class FQDDString(DisplayString):
    """Custom type FQDDString based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 512),
    )





class ObjectStatusEnum(Integer32):
    """Custom type ObjectStatusEnum based on Integer32"""
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





class BooleanType(Integer32):
    """Custom type BooleanType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )




# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Dell_ObjectIdentity = ObjectIdentity
dell = _Dell_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674)
)
_Server3_ObjectIdentity = ObjectIdentity
server3 = _Server3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10892)
)
_DrsOutofBandGroup_ObjectIdentity = ObjectIdentity
drsOutofBandGroup = _DrsOutofBandGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2)
)
_DrsInformationGroup_ObjectIdentity = ObjectIdentity
drsInformationGroup = _DrsInformationGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 1)
)
_DrsProductInfoGroup_ObjectIdentity = ObjectIdentity
drsProductInfoGroup = _DrsProductInfoGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 1, 1)
)
_DrsProductName_Type = DellString
_DrsProductName_Object = MibScalar
drsProductName = _DrsProductName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 1, 1, 1),
    _DrsProductName_Type()
)
drsProductName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drsProductName.setStatus("mandatory")
_DrsProductShortName_Type = DellString
_DrsProductShortName_Object = MibScalar
drsProductShortName = _DrsProductShortName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 1, 1, 2),
    _DrsProductShortName_Type()
)
drsProductShortName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drsProductShortName.setStatus("mandatory")
_DrsProductDescription_Type = DellString
_DrsProductDescription_Object = MibScalar
drsProductDescription = _DrsProductDescription_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 1, 1, 3),
    _DrsProductDescription_Type()
)
drsProductDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drsProductDescription.setStatus("mandatory")
_DrsProductManufacturer_Type = DellString
_DrsProductManufacturer_Object = MibScalar
drsProductManufacturer = _DrsProductManufacturer_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 1, 1, 4),
    _DrsProductManufacturer_Type()
)
drsProductManufacturer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drsProductManufacturer.setStatus("mandatory")
_DrsProductVersion_Type = DellString
_DrsProductVersion_Object = MibScalar
drsProductVersion = _DrsProductVersion_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 1, 1, 5),
    _DrsProductVersion_Type()
)
drsProductVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drsProductVersion.setStatus("mandatory")
_DrsChassisServiceTag_Type = DellString
_DrsChassisServiceTag_Object = MibScalar
drsChassisServiceTag = _DrsChassisServiceTag_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 1, 1, 6),
    _DrsChassisServiceTag_Type()
)
drsChassisServiceTag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drsChassisServiceTag.setStatus("mandatory")
_DrsProductURL_Type = DellString
_DrsProductURL_Object = MibScalar
drsProductURL = _DrsProductURL_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 1, 1, 7),
    _DrsProductURL_Type()
)
drsProductURL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drsProductURL.setStatus("mandatory")
_DrsProductChassisAssetTag_Type = DellString
_DrsProductChassisAssetTag_Object = MibScalar
drsProductChassisAssetTag = _DrsProductChassisAssetTag_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 1, 1, 8),
    _DrsProductChassisAssetTag_Type()
)
drsProductChassisAssetTag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drsProductChassisAssetTag.setStatus("mandatory")
_DrsProductChassisLocation_Type = DellString
_DrsProductChassisLocation_Object = MibScalar
drsProductChassisLocation = _DrsProductChassisLocation_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 1, 1, 9),
    _DrsProductChassisLocation_Type()
)
drsProductChassisLocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drsProductChassisLocation.setStatus("mandatory")
_DrsProductChassisName_Type = DellString
_DrsProductChassisName_Object = MibScalar
drsProductChassisName = _DrsProductChassisName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 1, 1, 10),
    _DrsProductChassisName_Type()
)
drsProductChassisName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drsProductChassisName.setStatus("mandatory")
_DrsSystemServiceTag_Type = DellString
_DrsSystemServiceTag_Object = MibScalar
drsSystemServiceTag = _DrsSystemServiceTag_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 1, 1, 11),
    _DrsSystemServiceTag_Type()
)
drsSystemServiceTag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drsSystemServiceTag.setStatus("mandatory")
_DrsProductSystemAssetTag_Type = DellString
_DrsProductSystemAssetTag_Object = MibScalar
drsProductSystemAssetTag = _DrsProductSystemAssetTag_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 1, 1, 12),
    _DrsProductSystemAssetTag_Type()
)
drsProductSystemAssetTag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drsProductSystemAssetTag.setStatus("mandatory")
_DrsProductSystemSlot_Type = DellString
_DrsProductSystemSlot_Object = MibScalar
drsProductSystemSlot = _DrsProductSystemSlot_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 1, 1, 13),
    _DrsProductSystemSlot_Type()
)
drsProductSystemSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drsProductSystemSlot.setStatus("mandatory")
_DrsProductType_Type = DellRacType
_DrsProductType_Object = MibScalar
drsProductType = _DrsProductType_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 1, 1, 14),
    _DrsProductType_Type()
)
drsProductType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drsProductType.setStatus("mandatory")
_DrsProductChassisDataCenter_Type = DellString
_DrsProductChassisDataCenter_Object = MibScalar
drsProductChassisDataCenter = _DrsProductChassisDataCenter_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 1, 1, 15),
    _DrsProductChassisDataCenter_Type()
)
drsProductChassisDataCenter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drsProductChassisDataCenter.setStatus("mandatory")
_DrsProductChassisAisle_Type = DellString
_DrsProductChassisAisle_Object = MibScalar
drsProductChassisAisle = _DrsProductChassisAisle_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 1, 1, 16),
    _DrsProductChassisAisle_Type()
)
drsProductChassisAisle.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drsProductChassisAisle.setStatus("mandatory")
_DrsProductChassisRack_Type = DellString
_DrsProductChassisRack_Object = MibScalar
drsProductChassisRack = _DrsProductChassisRack_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 1, 1, 17),
    _DrsProductChassisRack_Type()
)
drsProductChassisRack.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drsProductChassisRack.setStatus("mandatory")
_DrsProductChassisRackSlot_Type = DellString
_DrsProductChassisRackSlot_Object = MibScalar
drsProductChassisRackSlot = _DrsProductChassisRackSlot_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 1, 1, 18),
    _DrsProductChassisRackSlot_Type()
)
drsProductChassisRackSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drsProductChassisRackSlot.setStatus("mandatory")
_DrsProductChassisModel_Type = DellString
_DrsProductChassisModel_Object = MibScalar
drsProductChassisModel = _DrsProductChassisModel_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 1, 1, 19),
    _DrsProductChassisModel_Type()
)
drsProductChassisModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drsProductChassisModel.setStatus("mandatory")
_DrsProductChassisExpressServiceCode_Type = DellString
_DrsProductChassisExpressServiceCode_Object = MibScalar
drsProductChassisExpressServiceCode = _DrsProductChassisExpressServiceCode_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 1, 1, 20),
    _DrsProductChassisExpressServiceCode_Type()
)
drsProductChassisExpressServiceCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drsProductChassisExpressServiceCode.setStatus("mandatory")
_DrsProductChassisSystemID_Type = Integer32
_DrsProductChassisSystemID_Object = MibScalar
drsProductChassisSystemID = _DrsProductChassisSystemID_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 1, 1, 21),
    _DrsProductChassisSystemID_Type()
)
drsProductChassisSystemID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drsProductChassisSystemID.setStatus("mandatory")
_DrsProductChassisSize_Type = Integer32
_DrsProductChassisSize_Object = MibScalar
drsProductChassisSize = _DrsProductChassisSize_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 1, 1, 22),
    _DrsProductChassisSize_Type()
)
drsProductChassisSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drsProductChassisSize.setStatus("mandatory")
_DrsFirmwareGroup_ObjectIdentity = ObjectIdentity
drsFirmwareGroup = _DrsFirmwareGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 1, 2)
)
_DrsFirmwareVersion_Type = DellString
_DrsFirmwareVersion_Object = MibScalar
drsFirmwareVersion = _DrsFirmwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 1, 2, 1),
    _DrsFirmwareVersion_Type()
)
drsFirmwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drsFirmwareVersion.setStatus("mandatory")
_DrsiKVMFirmwareVersion_Type = DellString
_DrsiKVMFirmwareVersion_Object = MibScalar
drsiKVMFirmwareVersion = _DrsiKVMFirmwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 1, 2, 2),
    _DrsiKVMFirmwareVersion_Type()
)
drsiKVMFirmwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drsiKVMFirmwareVersion.setStatus("mandatory")
_DrsFirmwareVersion2_Type = DellString
_DrsFirmwareVersion2_Object = MibScalar
drsFirmwareVersion2 = _DrsFirmwareVersion2_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 1, 2, 3),
    _DrsFirmwareVersion2_Type()
)
drsFirmwareVersion2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drsFirmwareVersion2.setStatus("mandatory")
_DrsStatusGroup_ObjectIdentity = ObjectIdentity
drsStatusGroup = _DrsStatusGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 2)
)
_DrsGlobalSystemStatus_Type = DellStatus
_DrsGlobalSystemStatus_Object = MibScalar
drsGlobalSystemStatus = _DrsGlobalSystemStatus_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 2, 1),
    _DrsGlobalSystemStatus_Type()
)
drsGlobalSystemStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drsGlobalSystemStatus.setStatus("mandatory")
_DrsChassisStatusGroup_ObjectIdentity = ObjectIdentity
drsChassisStatusGroup = _DrsChassisStatusGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 3)
)
_DrsStatusNowGroup_ObjectIdentity = ObjectIdentity
drsStatusNowGroup = _DrsStatusNowGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 3, 1)
)
_DrsGlobalCurrStatus_Type = DellStatus
_DrsGlobalCurrStatus_Object = MibScalar
drsGlobalCurrStatus = _DrsGlobalCurrStatus_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 3, 1, 1),
    _DrsGlobalCurrStatus_Type()
)
drsGlobalCurrStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drsGlobalCurrStatus.setStatus("mandatory")
_DrsIOMCurrStatus_Type = DellStatus
_DrsIOMCurrStatus_Object = MibScalar
drsIOMCurrStatus = _DrsIOMCurrStatus_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 3, 1, 2),
    _DrsIOMCurrStatus_Type()
)
drsIOMCurrStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drsIOMCurrStatus.setStatus("mandatory")
_DrsKVMCurrStatus_Type = DellStatus
_DrsKVMCurrStatus_Object = MibScalar
drsKVMCurrStatus = _DrsKVMCurrStatus_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 3, 1, 3),
    _DrsKVMCurrStatus_Type()
)
drsKVMCurrStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drsKVMCurrStatus.setStatus("mandatory")
_DrsRedCurrStatus_Type = DellStatus
_DrsRedCurrStatus_Object = MibScalar
drsRedCurrStatus = _DrsRedCurrStatus_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 3, 1, 4),
    _DrsRedCurrStatus_Type()
)
drsRedCurrStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drsRedCurrStatus.setStatus("mandatory")
_DrsPowerCurrStatus_Type = DellStatus
_DrsPowerCurrStatus_Object = MibScalar
drsPowerCurrStatus = _DrsPowerCurrStatus_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 3, 1, 5),
    _DrsPowerCurrStatus_Type()
)
drsPowerCurrStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drsPowerCurrStatus.setStatus("mandatory")
_DrsFanCurrStatus_Type = DellStatus
_DrsFanCurrStatus_Object = MibScalar
drsFanCurrStatus = _DrsFanCurrStatus_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 3, 1, 6),
    _DrsFanCurrStatus_Type()
)
drsFanCurrStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drsFanCurrStatus.setStatus("mandatory")
_DrsBladeCurrStatus_Type = DellStatus
_DrsBladeCurrStatus_Object = MibScalar
drsBladeCurrStatus = _DrsBladeCurrStatus_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 3, 1, 7),
    _DrsBladeCurrStatus_Type()
)
drsBladeCurrStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drsBladeCurrStatus.setStatus("mandatory")
_DrsTempCurrStatus_Type = DellStatus
_DrsTempCurrStatus_Object = MibScalar
drsTempCurrStatus = _DrsTempCurrStatus_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 3, 1, 8),
    _DrsTempCurrStatus_Type()
)
drsTempCurrStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drsTempCurrStatus.setStatus("mandatory")
_DrsCMCCurrStatus_Type = DellStatus
_DrsCMCCurrStatus_Object = MibScalar
drsCMCCurrStatus = _DrsCMCCurrStatus_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 3, 1, 9),
    _DrsCMCCurrStatus_Type()
)
drsCMCCurrStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drsCMCCurrStatus.setStatus("mandatory")
_DrsChassisFrontPanelAmbientTemperature_Type = DellTemperatureReading
_DrsChassisFrontPanelAmbientTemperature_Object = MibScalar
drsChassisFrontPanelAmbientTemperature = _DrsChassisFrontPanelAmbientTemperature_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 3, 1, 10),
    _DrsChassisFrontPanelAmbientTemperature_Type()
)
drsChassisFrontPanelAmbientTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drsChassisFrontPanelAmbientTemperature.setStatus("mandatory")
_DrsCMCAmbientTemperature_Type = DellTemperatureReading
_DrsCMCAmbientTemperature_Object = MibScalar
drsCMCAmbientTemperature = _DrsCMCAmbientTemperature_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 3, 1, 11),
    _DrsCMCAmbientTemperature_Type()
)
drsCMCAmbientTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drsCMCAmbientTemperature.setStatus("mandatory")
_DrsCMCProcessorTemperature_Type = DellTemperatureReading
_DrsCMCProcessorTemperature_Object = MibScalar
drsCMCProcessorTemperature = _DrsCMCProcessorTemperature_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 3, 1, 12),
    _DrsCMCProcessorTemperature_Type()
)
drsCMCProcessorTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drsCMCProcessorTemperature.setStatus("mandatory")
_DrsStatusPrevGroup_ObjectIdentity = ObjectIdentity
drsStatusPrevGroup = _DrsStatusPrevGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 3, 2)
)
_DrsGlobalPrevStatus_Type = DellStatus
_DrsGlobalPrevStatus_Object = MibScalar
drsGlobalPrevStatus = _DrsGlobalPrevStatus_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 3, 2, 1),
    _DrsGlobalPrevStatus_Type()
)
drsGlobalPrevStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drsGlobalPrevStatus.setStatus("mandatory")
_DrsIOMPrevStatus_Type = DellStatus
_DrsIOMPrevStatus_Object = MibScalar
drsIOMPrevStatus = _DrsIOMPrevStatus_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 3, 2, 2),
    _DrsIOMPrevStatus_Type()
)
drsIOMPrevStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drsIOMPrevStatus.setStatus("mandatory")
_DrsKVMPrevStatus_Type = DellStatus
_DrsKVMPrevStatus_Object = MibScalar
drsKVMPrevStatus = _DrsKVMPrevStatus_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 3, 2, 3),
    _DrsKVMPrevStatus_Type()
)
drsKVMPrevStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drsKVMPrevStatus.setStatus("mandatory")
_DrsRedPrevStatus_Type = DellStatus
_DrsRedPrevStatus_Object = MibScalar
drsRedPrevStatus = _DrsRedPrevStatus_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 3, 2, 4),
    _DrsRedPrevStatus_Type()
)
drsRedPrevStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drsRedPrevStatus.setStatus("mandatory")
_DrsPowerPrevStatus_Type = DellStatus
_DrsPowerPrevStatus_Object = MibScalar
drsPowerPrevStatus = _DrsPowerPrevStatus_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 3, 2, 5),
    _DrsPowerPrevStatus_Type()
)
drsPowerPrevStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drsPowerPrevStatus.setStatus("mandatory")
_DrsFanPrevStatus_Type = DellStatus
_DrsFanPrevStatus_Object = MibScalar
drsFanPrevStatus = _DrsFanPrevStatus_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 3, 2, 6),
    _DrsFanPrevStatus_Type()
)
drsFanPrevStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drsFanPrevStatus.setStatus("mandatory")
_DrsBladePrevStatus_Type = DellStatus
_DrsBladePrevStatus_Object = MibScalar
drsBladePrevStatus = _DrsBladePrevStatus_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 3, 2, 7),
    _DrsBladePrevStatus_Type()
)
drsBladePrevStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drsBladePrevStatus.setStatus("mandatory")
_DrsTempPrevStatus_Type = DellStatus
_DrsTempPrevStatus_Object = MibScalar
drsTempPrevStatus = _DrsTempPrevStatus_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 3, 2, 8),
    _DrsTempPrevStatus_Type()
)
drsTempPrevStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drsTempPrevStatus.setStatus("mandatory")
_DrsCMCPrevStatus_Type = DellStatus
_DrsCMCPrevStatus_Object = MibScalar
drsCMCPrevStatus = _DrsCMCPrevStatus_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 3, 2, 9),
    _DrsCMCPrevStatus_Type()
)
drsCMCPrevStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drsCMCPrevStatus.setStatus("mandatory")
_DrsStatusChangeGroup_ObjectIdentity = ObjectIdentity
drsStatusChangeGroup = _DrsStatusChangeGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 3, 3)
)
_DrsGlobalChangeTime_Type = TimeTicks
_DrsGlobalChangeTime_Object = MibScalar
drsGlobalChangeTime = _DrsGlobalChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 3, 3, 1),
    _DrsGlobalChangeTime_Type()
)
drsGlobalChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drsGlobalChangeTime.setStatus("mandatory")
_DrsIOMChangeTime_Type = TimeTicks
_DrsIOMChangeTime_Object = MibScalar
drsIOMChangeTime = _DrsIOMChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 3, 3, 2),
    _DrsIOMChangeTime_Type()
)
drsIOMChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drsIOMChangeTime.setStatus("mandatory")
_DrsKVMChangeTime_Type = TimeTicks
_DrsKVMChangeTime_Object = MibScalar
drsKVMChangeTime = _DrsKVMChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 3, 3, 3),
    _DrsKVMChangeTime_Type()
)
drsKVMChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drsKVMChangeTime.setStatus("mandatory")
_DrsRedChangeTime_Type = TimeTicks
_DrsRedChangeTime_Object = MibScalar
drsRedChangeTime = _DrsRedChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 3, 3, 4),
    _DrsRedChangeTime_Type()
)
drsRedChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drsRedChangeTime.setStatus("mandatory")
_DrsPowerChangeTime_Type = TimeTicks
_DrsPowerChangeTime_Object = MibScalar
drsPowerChangeTime = _DrsPowerChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 3, 3, 5),
    _DrsPowerChangeTime_Type()
)
drsPowerChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drsPowerChangeTime.setStatus("mandatory")
_DrsFanChangeTime_Type = TimeTicks
_DrsFanChangeTime_Object = MibScalar
drsFanChangeTime = _DrsFanChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 3, 3, 6),
    _DrsFanChangeTime_Type()
)
drsFanChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drsFanChangeTime.setStatus("mandatory")
_DrsBladeChangeTime_Type = TimeTicks
_DrsBladeChangeTime_Object = MibScalar
drsBladeChangeTime = _DrsBladeChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 3, 3, 7),
    _DrsBladeChangeTime_Type()
)
drsBladeChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drsBladeChangeTime.setStatus("mandatory")
_DrsTempChangeTime_Type = TimeTicks
_DrsTempChangeTime_Object = MibScalar
drsTempChangeTime = _DrsTempChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 3, 3, 8),
    _DrsTempChangeTime_Type()
)
drsTempChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drsTempChangeTime.setStatus("mandatory")
_DrsCMCChangeTime_Type = TimeTicks
_DrsCMCChangeTime_Object = MibScalar
drsCMCChangeTime = _DrsCMCChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 3, 3, 9),
    _DrsCMCChangeTime_Type()
)
drsCMCChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drsCMCChangeTime.setStatus("mandatory")
_DrsChassisPowerGroup_ObjectIdentity = ObjectIdentity
drsChassisPowerGroup = _DrsChassisPowerGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 4)
)
_DrsCMCPowerTable_Object = MibTable
drsCMCPowerTable = _DrsCMCPowerTable_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 4, 1)
)
if mibBuilder.loadTexts:
    drsCMCPowerTable.setStatus("mandatory")
_DrsCMCPowerTableEntry_Object = MibTableRow
drsCMCPowerTableEntry = _DrsCMCPowerTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 4, 1, 1)
)
drsCMCPowerTableEntry.setIndexNames(
    (0, "DELL-RAC-MIB", "drsChassisIndex"),
)
if mibBuilder.loadTexts:
    drsCMCPowerTableEntry.setStatus("mandatory")
_DrsChassisIndex_Type = DellCMCPowerIndexRange
_DrsChassisIndex_Object = MibTableColumn
drsChassisIndex = _DrsChassisIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 4, 1, 1, 1),
    _DrsChassisIndex_Type()
)
drsChassisIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drsChassisIndex.setStatus("mandatory")
_DrsPotentialPower_Type = DellPowerReading
_DrsPotentialPower_Object = MibTableColumn
drsPotentialPower = _DrsPotentialPower_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 4, 1, 1, 2),
    _DrsPotentialPower_Type()
)
drsPotentialPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drsPotentialPower.setStatus("mandatory")
_DrsIdlePower_Type = DellPowerReading
_DrsIdlePower_Object = MibTableColumn
drsIdlePower = _DrsIdlePower_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 4, 1, 1, 3),
    _DrsIdlePower_Type()
)
drsIdlePower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drsIdlePower.setStatus("mandatory")
_DrsMaxPowerSpecification_Type = DellPowerReading
_DrsMaxPowerSpecification_Object = MibTableColumn
drsMaxPowerSpecification = _DrsMaxPowerSpecification_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 4, 1, 1, 4),
    _DrsMaxPowerSpecification_Type()
)
drsMaxPowerSpecification.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drsMaxPowerSpecification.setStatus("mandatory")
_DrsPowerSurplus_Type = DellPowerReading
_DrsPowerSurplus_Object = MibTableColumn
drsPowerSurplus = _DrsPowerSurplus_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 4, 1, 1, 5),
    _DrsPowerSurplus_Type()
)
drsPowerSurplus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drsPowerSurplus.setStatus("mandatory")
_DrsKWhCumulative_Type = DellPowerReading
_DrsKWhCumulative_Object = MibTableColumn
drsKWhCumulative = _DrsKWhCumulative_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 4, 1, 1, 6),
    _DrsKWhCumulative_Type()
)
drsKWhCumulative.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drsKWhCumulative.setStatus("mandatory")
_DrsKWhCumulativeTime_Type = DellTimestamp
_DrsKWhCumulativeTime_Object = MibTableColumn
drsKWhCumulativeTime = _DrsKWhCumulativeTime_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 4, 1, 1, 7),
    _DrsKWhCumulativeTime_Type()
)
drsKWhCumulativeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drsKWhCumulativeTime.setStatus("mandatory")
_DrsWattsPeakUsage_Type = DellPowerReading
_DrsWattsPeakUsage_Object = MibTableColumn
drsWattsPeakUsage = _DrsWattsPeakUsage_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 4, 1, 1, 8),
    _DrsWattsPeakUsage_Type()
)
drsWattsPeakUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drsWattsPeakUsage.setStatus("mandatory")
_DrsWattsPeakTime_Type = DellTimestamp
_DrsWattsPeakTime_Object = MibTableColumn
drsWattsPeakTime = _DrsWattsPeakTime_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 4, 1, 1, 9),
    _DrsWattsPeakTime_Type()
)
drsWattsPeakTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drsWattsPeakTime.setStatus("mandatory")
_DrsWattsMinUsage_Type = DellPowerReading
_DrsWattsMinUsage_Object = MibTableColumn
drsWattsMinUsage = _DrsWattsMinUsage_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 4, 1, 1, 10),
    _DrsWattsMinUsage_Type()
)
drsWattsMinUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drsWattsMinUsage.setStatus("mandatory")
_DrsWattsMinTime_Type = DellTimestamp
_DrsWattsMinTime_Object = MibTableColumn
drsWattsMinTime = _DrsWattsMinTime_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 4, 1, 1, 11),
    _DrsWattsMinTime_Type()
)
drsWattsMinTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drsWattsMinTime.setStatus("mandatory")
_DrsWattsResetTime_Type = DellTimestamp
_DrsWattsResetTime_Object = MibTableColumn
drsWattsResetTime = _DrsWattsResetTime_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 4, 1, 1, 12),
    _DrsWattsResetTime_Type()
)
drsWattsResetTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drsWattsResetTime.setStatus("mandatory")
_DrsWattsReading_Type = DellPowerReading
_DrsWattsReading_Object = MibTableColumn
drsWattsReading = _DrsWattsReading_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 4, 1, 1, 13),
    _DrsWattsReading_Type()
)
drsWattsReading.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drsWattsReading.setStatus("mandatory")
_DrsAmpsReading_Type = DellPowerReading
_DrsAmpsReading_Object = MibTableColumn
drsAmpsReading = _DrsAmpsReading_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 4, 1, 1, 14),
    _DrsAmpsReading_Type()
)
drsAmpsReading.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drsAmpsReading.setStatus("mandatory")
_DrsCMCPSUTable_Object = MibTable
drsCMCPSUTable = _DrsCMCPSUTable_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 4, 2)
)
if mibBuilder.loadTexts:
    drsCMCPSUTable.setStatus("mandatory")
_DrsCMCPSUTableEntry_Object = MibTableRow
drsCMCPSUTableEntry = _DrsCMCPSUTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 4, 2, 1)
)
drsCMCPSUTableEntry.setIndexNames(
    (0, "DELL-RAC-MIB", "drsPSUChassisIndex"),
    (0, "DELL-RAC-MIB", "drsPSUIndex"),
)
if mibBuilder.loadTexts:
    drsCMCPSUTableEntry.setStatus("mandatory")
_DrsPSUChassisIndex_Type = DellCMCPowerIndexRange
_DrsPSUChassisIndex_Object = MibTableColumn
drsPSUChassisIndex = _DrsPSUChassisIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 4, 2, 1, 1),
    _DrsPSUChassisIndex_Type()
)
drsPSUChassisIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drsPSUChassisIndex.setStatus("mandatory")
_DrsPSUIndex_Type = DellCMCPSUIndexRange
_DrsPSUIndex_Object = MibTableColumn
drsPSUIndex = _DrsPSUIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 4, 2, 1, 2),
    _DrsPSUIndex_Type()
)
drsPSUIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drsPSUIndex.setStatus("mandatory")
_DrsPSULocation_Type = DellString
_DrsPSULocation_Object = MibTableColumn
drsPSULocation = _DrsPSULocation_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 4, 2, 1, 3),
    _DrsPSULocation_Type()
)
drsPSULocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drsPSULocation.setStatus("mandatory")
_DrsPSUMonitoringCapable_Type = DellCMCPSUCapable
_DrsPSUMonitoringCapable_Object = MibTableColumn
drsPSUMonitoringCapable = _DrsPSUMonitoringCapable_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 4, 2, 1, 4),
    _DrsPSUMonitoringCapable_Type()
)
drsPSUMonitoringCapable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drsPSUMonitoringCapable.setStatus("mandatory")
_DrsPSUVoltsReading_Type = DellPowerReading
_DrsPSUVoltsReading_Object = MibTableColumn
drsPSUVoltsReading = _DrsPSUVoltsReading_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 4, 2, 1, 5),
    _DrsPSUVoltsReading_Type()
)
drsPSUVoltsReading.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drsPSUVoltsReading.setStatus("mandatory")
_DrsPSUAmpsReading_Type = DellPowerReading
_DrsPSUAmpsReading_Object = MibTableColumn
drsPSUAmpsReading = _DrsPSUAmpsReading_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 4, 2, 1, 6),
    _DrsPSUAmpsReading_Type()
)
drsPSUAmpsReading.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drsPSUAmpsReading.setStatus("mandatory")
_DrsPSUWattsReading_Type = DellPowerReading
_DrsPSUWattsReading_Object = MibTableColumn
drsPSUWattsReading = _DrsPSUWattsReading_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 4, 2, 1, 7),
    _DrsPSUWattsReading_Type()
)
drsPSUWattsReading.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drsPSUWattsReading.setStatus("mandatory")
_DrsChassisServerGroup_ObjectIdentity = ObjectIdentity
drsChassisServerGroup = _DrsChassisServerGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 5)
)
_DrsCMCServerTable_Object = MibTable
drsCMCServerTable = _DrsCMCServerTable_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 5, 1)
)
if mibBuilder.loadTexts:
    drsCMCServerTable.setStatus("mandatory")
_DrsCMCServerTableEntry_Object = MibTableRow
drsCMCServerTableEntry = _DrsCMCServerTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 5, 1, 1)
)
drsCMCServerTableEntry.setIndexNames(
    (0, "DELL-RAC-MIB", "drsServerIndex"),
)
if mibBuilder.loadTexts:
    drsCMCServerTableEntry.setStatus("mandatory")
_DrsServerIndex_Type = DellCMCServerIndexRange
_DrsServerIndex_Object = MibTableColumn
drsServerIndex = _DrsServerIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 5, 1, 1, 1),
    _DrsServerIndex_Type()
)
drsServerIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drsServerIndex.setStatus("mandatory")
_DrsServerMonitoringCapable_Type = DellCMCServerCapable
_DrsServerMonitoringCapable_Object = MibTableColumn
drsServerMonitoringCapable = _DrsServerMonitoringCapable_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 5, 1, 1, 2),
    _DrsServerMonitoringCapable_Type()
)
drsServerMonitoringCapable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drsServerMonitoringCapable.setStatus("mandatory")
_DrsServerServiceTag_Type = DellString
_DrsServerServiceTag_Object = MibTableColumn
drsServerServiceTag = _DrsServerServiceTag_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 5, 1, 1, 3),
    _DrsServerServiceTag_Type()
)
drsServerServiceTag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drsServerServiceTag.setStatus("mandatory")
_DrsServerSlotName_Type = DellString
_DrsServerSlotName_Object = MibTableColumn
drsServerSlotName = _DrsServerSlotName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 5, 1, 1, 4),
    _DrsServerSlotName_Type()
)
drsServerSlotName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drsServerSlotName.setStatus("mandatory")
_DrsServerSlotNumber_Type = DellString
_DrsServerSlotNumber_Object = MibTableColumn
drsServerSlotNumber = _DrsServerSlotNumber_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 5, 1, 1, 5),
    _DrsServerSlotNumber_Type()
)
drsServerSlotNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drsServerSlotNumber.setStatus("mandatory")
_DrsServerNodeID_Type = DellString
_DrsServerNodeID_Object = MibTableColumn
drsServerNodeID = _DrsServerNodeID_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 5, 1, 1, 6),
    _DrsServerNodeID_Type()
)
drsServerNodeID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drsServerNodeID.setStatus("mandatory")
_DrsServerModel_Type = DellString
_DrsServerModel_Object = MibTableColumn
drsServerModel = _DrsServerModel_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 5, 1, 1, 7),
    _DrsServerModel_Type()
)
drsServerModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drsServerModel.setStatus("mandatory")
_DrsServerAssetTag_Type = DellString
_DrsServerAssetTag_Object = MibTableColumn
drsServerAssetTag = _DrsServerAssetTag_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 5, 1, 1, 8),
    _DrsServerAssetTag_Type()
)
drsServerAssetTag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drsServerAssetTag.setStatus("mandatory")
_DrsServerNumStorageControllers_Type = Integer32
_DrsServerNumStorageControllers_Object = MibTableColumn
drsServerNumStorageControllers = _DrsServerNumStorageControllers_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 5, 1, 1, 9),
    _DrsServerNumStorageControllers_Type()
)
drsServerNumStorageControllers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drsServerNumStorageControllers.setStatus("mandatory")
_DrsServerStorageMode_Type = DellCMCServerStorageMode
_DrsServerStorageMode_Object = MibTableColumn
drsServerStorageMode = _DrsServerStorageMode_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 5, 1, 1, 10),
    _DrsServerStorageMode_Type()
)
drsServerStorageMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drsServerStorageMode.setStatus("mandatory")
_DrsServerIntrusionState_Type = DellCMCServerIntrusionState
_DrsServerIntrusionState_Object = MibTableColumn
drsServerIntrusionState = _DrsServerIntrusionState_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 5, 1, 1, 11),
    _DrsServerIntrusionState_Type()
)
drsServerIntrusionState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drsServerIntrusionState.setStatus("mandatory")
_DrsServerAssignedServerSlots_Type = DellString
_DrsServerAssignedServerSlots_Object = MibTableColumn
drsServerAssignedServerSlots = _DrsServerAssignedServerSlots_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 5, 1, 1, 12),
    _DrsServerAssignedServerSlots_Type()
)
drsServerAssignedServerSlots.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drsServerAssignedServerSlots.setStatus("mandatory")
_StorageDetailsGroup_ObjectIdentity = ObjectIdentity
storageDetailsGroup = _StorageDetailsGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 6)
)
_Software_ObjectIdentity = ObjectIdentity
software = _Software_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 6, 1)
)
_StorageManagement_ObjectIdentity = ObjectIdentity
storageManagement = _StorageManagement_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 6, 1, 20)
)
_PhysicalDevices_ObjectIdentity = ObjectIdentity
physicalDevices = _PhysicalDevices_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 6, 1, 20, 130)
)
_ControllerTable_Object = MibTable
controllerTable = _ControllerTable_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 6, 1, 20, 130, 1)
)
if mibBuilder.loadTexts:
    controllerTable.setStatus("mandatory")
_ControllerTableEntry_Object = MibTableRow
controllerTableEntry = _ControllerTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 6, 1, 20, 130, 1, 1)
)
controllerTableEntry.setIndexNames(
    (0, "DELL-RAC-MIB", "controllerNumber"),
)
if mibBuilder.loadTexts:
    controllerTableEntry.setStatus("mandatory")


class _ControllerNumber_Type(Integer32):
    """Custom type controllerNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_ControllerNumber_Type.__name__ = "Integer32"
_ControllerNumber_Object = MibTableColumn
controllerNumber = _ControllerNumber_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 6, 1, 20, 130, 1, 1, 1),
    _ControllerNumber_Type()
)
controllerNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controllerNumber.setStatus("mandatory")
_ControllerName_Type = DisplayString
_ControllerName_Object = MibTableColumn
controllerName = _ControllerName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 6, 1, 20, 130, 1, 1, 2),
    _ControllerName_Type()
)
controllerName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controllerName.setStatus("mandatory")


class _ControllerRebuildRate_Type(Integer32):
    """Custom type controllerRebuildRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_ControllerRebuildRate_Type.__name__ = "Integer32"
_ControllerRebuildRate_Object = MibTableColumn
controllerRebuildRate = _ControllerRebuildRate_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 6, 1, 20, 130, 1, 1, 7),
    _ControllerRebuildRate_Type()
)
controllerRebuildRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controllerRebuildRate.setStatus("mandatory")
_ControllerFWVersion_Type = DisplayString
_ControllerFWVersion_Object = MibTableColumn
controllerFWVersion = _ControllerFWVersion_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 6, 1, 20, 130, 1, 1, 8),
    _ControllerFWVersion_Type()
)
controllerFWVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controllerFWVersion.setStatus("mandatory")
_ControllerCacheSizeInMB_Type = Integer32
_ControllerCacheSizeInMB_Object = MibTableColumn
controllerCacheSizeInMB = _ControllerCacheSizeInMB_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 6, 1, 20, 130, 1, 1, 9),
    _ControllerCacheSizeInMB_Type()
)
controllerCacheSizeInMB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controllerCacheSizeInMB.setStatus("mandatory")
_ControllerRollUpStatus_Type = ObjectStatusEnum
_ControllerRollUpStatus_Object = MibTableColumn
controllerRollUpStatus = _ControllerRollUpStatus_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 6, 1, 20, 130, 1, 1, 37),
    _ControllerRollUpStatus_Type()
)
controllerRollUpStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controllerRollUpStatus.setStatus("mandatory")
_ControllerComponentStatus_Type = ObjectStatusEnum
_ControllerComponentStatus_Object = MibTableColumn
controllerComponentStatus = _ControllerComponentStatus_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 6, 1, 20, 130, 1, 1, 38),
    _ControllerComponentStatus_Type()
)
controllerComponentStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controllerComponentStatus.setStatus("mandatory")
_ControllerDriverVersion_Type = DisplayString
_ControllerDriverVersion_Object = MibTableColumn
controllerDriverVersion = _ControllerDriverVersion_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 6, 1, 20, 130, 1, 1, 41),
    _ControllerDriverVersion_Type()
)
controllerDriverVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controllerDriverVersion.setStatus("mandatory")
_ControllerPCISlot_Type = DisplayString
_ControllerPCISlot_Object = MibTableColumn
controllerPCISlot = _ControllerPCISlot_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 6, 1, 20, 130, 1, 1, 42),
    _ControllerPCISlot_Type()
)
controllerPCISlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controllerPCISlot.setStatus("mandatory")


class _ControllerReconstructRate_Type(Integer32):
    """Custom type controllerReconstructRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_ControllerReconstructRate_Type.__name__ = "Integer32"
_ControllerReconstructRate_Object = MibTableColumn
controllerReconstructRate = _ControllerReconstructRate_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 6, 1, 20, 130, 1, 1, 48),
    _ControllerReconstructRate_Type()
)
controllerReconstructRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controllerReconstructRate.setStatus("mandatory")


class _ControllerPatrolReadRate_Type(Integer32):
    """Custom type controllerPatrolReadRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_ControllerPatrolReadRate_Type.__name__ = "Integer32"
_ControllerPatrolReadRate_Object = MibTableColumn
controllerPatrolReadRate = _ControllerPatrolReadRate_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 6, 1, 20, 130, 1, 1, 49),
    _ControllerPatrolReadRate_Type()
)
controllerPatrolReadRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controllerPatrolReadRate.setStatus("mandatory")


class _ControllerBGIRate_Type(Integer32):
    """Custom type controllerBGIRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_ControllerBGIRate_Type.__name__ = "Integer32"
_ControllerBGIRate_Object = MibTableColumn
controllerBGIRate = _ControllerBGIRate_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 6, 1, 20, 130, 1, 1, 50),
    _ControllerBGIRate_Type()
)
controllerBGIRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controllerBGIRate.setStatus("mandatory")


class _ControllerCheckConsistencyRate_Type(Integer32):
    """Custom type controllerCheckConsistencyRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_ControllerCheckConsistencyRate_Type.__name__ = "Integer32"
_ControllerCheckConsistencyRate_Object = MibTableColumn
controllerCheckConsistencyRate = _ControllerCheckConsistencyRate_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 6, 1, 20, 130, 1, 1, 51),
    _ControllerCheckConsistencyRate_Type()
)
controllerCheckConsistencyRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controllerCheckConsistencyRate.setStatus("mandatory")


class _ControllerPatrolReadMode_Type(Integer32):
    """Custom type controllerPatrolReadMode based on Integer32"""
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
        *(("other", 1),
          ("notSupported", 2),
          ("disabled", 3),
          ("auto", 4),
          ("manual", 5))
    )


_ControllerPatrolReadMode_Type.__name__ = "Integer32"
_ControllerPatrolReadMode_Object = MibTableColumn
controllerPatrolReadMode = _ControllerPatrolReadMode_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 6, 1, 20, 130, 1, 1, 52),
    _ControllerPatrolReadMode_Type()
)
controllerPatrolReadMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controllerPatrolReadMode.setStatus("mandatory")


class _ControllerPatrolReadState_Type(Integer32):
    """Custom type controllerPatrolReadState based on Integer32"""
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
          ("stopped", 2),
          ("active", 3))
    )


_ControllerPatrolReadState_Type.__name__ = "Integer32"
_ControllerPatrolReadState_Object = MibTableColumn
controllerPatrolReadState = _ControllerPatrolReadState_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 6, 1, 20, 130, 1, 1, 53),
    _ControllerPatrolReadState_Type()
)
controllerPatrolReadState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controllerPatrolReadState.setStatus("mandatory")
_ControllerPersistentHotSpare_Type = BooleanType
_ControllerPersistentHotSpare_Object = MibTableColumn
controllerPersistentHotSpare = _ControllerPersistentHotSpare_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 6, 1, 20, 130, 1, 1, 59),
    _ControllerPersistentHotSpare_Type()
)
controllerPersistentHotSpare.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controllerPersistentHotSpare.setStatus("mandatory")
_ControllerSpinDownUnconfiguredDrives_Type = BooleanType
_ControllerSpinDownUnconfiguredDrives_Object = MibTableColumn
controllerSpinDownUnconfiguredDrives = _ControllerSpinDownUnconfiguredDrives_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 6, 1, 20, 130, 1, 1, 60),
    _ControllerSpinDownUnconfiguredDrives_Type()
)
controllerSpinDownUnconfiguredDrives.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controllerSpinDownUnconfiguredDrives.setStatus("mandatory")
_ControllerSpinDownHotSpareDrives_Type = BooleanType
_ControllerSpinDownHotSpareDrives_Object = MibTableColumn
controllerSpinDownHotSpareDrives = _ControllerSpinDownHotSpareDrives_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 6, 1, 20, 130, 1, 1, 61),
    _ControllerSpinDownHotSpareDrives_Type()
)
controllerSpinDownHotSpareDrives.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controllerSpinDownHotSpareDrives.setStatus("mandatory")


class _ControllerSpinDownTimeInterval_Type(Integer32):
    """Custom type controllerSpinDownTimeInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(30, 1440),
    )


_ControllerSpinDownTimeInterval_Type.__name__ = "Integer32"
_ControllerSpinDownTimeInterval_Object = MibTableColumn
controllerSpinDownTimeInterval = _ControllerSpinDownTimeInterval_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 6, 1, 20, 130, 1, 1, 62),
    _ControllerSpinDownTimeInterval_Type()
)
controllerSpinDownTimeInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controllerSpinDownTimeInterval.setStatus("mandatory")
_ControllerPreservedCache_Type = BooleanType
_ControllerPreservedCache_Object = MibTableColumn
controllerPreservedCache = _ControllerPreservedCache_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 6, 1, 20, 130, 1, 1, 69),
    _ControllerPreservedCache_Type()
)
controllerPreservedCache.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controllerPreservedCache.setStatus("mandatory")


class _ControllerCheckConsistencyMode_Type(Integer32):
    """Custom type controllerCheckConsistencyMode based on Integer32"""
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
        *(("other", 1),
          ("unsupported", 2),
          ("normal", 3),
          ("stopOnError", 4))
    )


_ControllerCheckConsistencyMode_Type.__name__ = "Integer32"
_ControllerCheckConsistencyMode_Object = MibTableColumn
controllerCheckConsistencyMode = _ControllerCheckConsistencyMode_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 6, 1, 20, 130, 1, 1, 70),
    _ControllerCheckConsistencyMode_Type()
)
controllerCheckConsistencyMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controllerCheckConsistencyMode.setStatus("mandatory")


class _ControllerCopyBackMode_Type(Integer32):
    """Custom type controllerCopyBackMode based on Integer32"""
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
        *(("other", 1),
          ("unsupported", 2),
          ("on", 3),
          ("onWithSmart", 4),
          ("off", 5))
    )


_ControllerCopyBackMode_Type.__name__ = "Integer32"
_ControllerCopyBackMode_Object = MibTableColumn
controllerCopyBackMode = _ControllerCopyBackMode_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 6, 1, 20, 130, 1, 1, 71),
    _ControllerCopyBackMode_Type()
)
controllerCopyBackMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controllerCopyBackMode.setStatus("mandatory")


class _ControllerSecurityStatus_Type(Integer32):
    """Custom type controllerSecurityStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 1),
          ("none", 2),
          ("lkm", 3))
    )


_ControllerSecurityStatus_Type.__name__ = "Integer32"
_ControllerSecurityStatus_Object = MibTableColumn
controllerSecurityStatus = _ControllerSecurityStatus_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 6, 1, 20, 130, 1, 1, 72),
    _ControllerSecurityStatus_Type()
)
controllerSecurityStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controllerSecurityStatus.setStatus("mandatory")
_ControllerEncryptionKeyPresent_Type = BooleanType
_ControllerEncryptionKeyPresent_Object = MibTableColumn
controllerEncryptionKeyPresent = _ControllerEncryptionKeyPresent_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 6, 1, 20, 130, 1, 1, 73),
    _ControllerEncryptionKeyPresent_Type()
)
controllerEncryptionKeyPresent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controllerEncryptionKeyPresent.setStatus("mandatory")


class _ControllerEncryptionCapability_Type(Integer32):
    """Custom type controllerEncryptionCapability based on Integer32"""
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
          ("none", 2),
          ("lkm", 3))
    )


_ControllerEncryptionCapability_Type.__name__ = "Integer32"
_ControllerEncryptionCapability_Object = MibTableColumn
controllerEncryptionCapability = _ControllerEncryptionCapability_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 6, 1, 20, 130, 1, 1, 74),
    _ControllerEncryptionCapability_Type()
)
controllerEncryptionCapability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controllerEncryptionCapability.setStatus("mandatory")


class _ControllerLoadBalanceSetting_Type(Integer32):
    """Custom type controllerLoadBalanceSetting based on Integer32"""
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
        *(("other", 1),
          ("unsupported", 2),
          ("auto", 3),
          ("none", 4))
    )


_ControllerLoadBalanceSetting_Type.__name__ = "Integer32"
_ControllerLoadBalanceSetting_Object = MibTableColumn
controllerLoadBalanceSetting = _ControllerLoadBalanceSetting_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 6, 1, 20, 130, 1, 1, 75),
    _ControllerLoadBalanceSetting_Type()
)
controllerLoadBalanceSetting.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controllerLoadBalanceSetting.setStatus("mandatory")


class _ControllerMaxCapSpeed_Type(Integer32):
    """Custom type controllerMaxCapSpeed based on Integer32"""
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
        *(("unknown", 1),
          ("oneDotFiveGbps", 2),
          ("threeGbps", 3),
          ("sixGbps", 4),
          ("twelveGbps", 5))
    )


_ControllerMaxCapSpeed_Type.__name__ = "Integer32"
_ControllerMaxCapSpeed_Object = MibTableColumn
controllerMaxCapSpeed = _ControllerMaxCapSpeed_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 6, 1, 20, 130, 1, 1, 76),
    _ControllerMaxCapSpeed_Type()
)
controllerMaxCapSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controllerMaxCapSpeed.setStatus("mandatory")
_ControllerSASAddress_Type = DisplayString
_ControllerSASAddress_Object = MibTableColumn
controllerSASAddress = _ControllerSASAddress_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 6, 1, 20, 130, 1, 1, 77),
    _ControllerSASAddress_Type()
)
controllerSASAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controllerSASAddress.setStatus("mandatory")
_ControllerFQDD_Type = FQDDString
_ControllerFQDD_Object = MibTableColumn
controllerFQDD = _ControllerFQDD_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 6, 1, 20, 130, 1, 1, 78),
    _ControllerFQDD_Type()
)
controllerFQDD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controllerFQDD.setStatus("mandatory")
_ControllerDisplayName_Type = DisplayString
_ControllerDisplayName_Object = MibTableColumn
controllerDisplayName = _ControllerDisplayName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 6, 1, 20, 130, 1, 1, 79),
    _ControllerDisplayName_Type()
)
controllerDisplayName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controllerDisplayName.setStatus("mandatory")


class _ControllerT10PICapability_Type(Integer32):
    """Custom type controllerT10PICapability based on Integer32"""
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
          ("capable", 2),
          ("notCapable", 3))
    )


_ControllerT10PICapability_Type.__name__ = "Integer32"
_ControllerT10PICapability_Object = MibTableColumn
controllerT10PICapability = _ControllerT10PICapability_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 6, 1, 20, 130, 1, 1, 80),
    _ControllerT10PICapability_Type()
)
controllerT10PICapability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controllerT10PICapability.setStatus("mandatory")
_ControllerRAID10UnevenSpansSupported_Type = BooleanType
_ControllerRAID10UnevenSpansSupported_Object = MibTableColumn
controllerRAID10UnevenSpansSupported = _ControllerRAID10UnevenSpansSupported_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 6, 1, 20, 130, 1, 1, 81),
    _ControllerRAID10UnevenSpansSupported_Type()
)
controllerRAID10UnevenSpansSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controllerRAID10UnevenSpansSupported.setStatus("mandatory")


class _ControllerEnhancedAutoImportForeignConfigMode_Type(Integer32):
    """Custom type controllerEnhancedAutoImportForeignConfigMode based on Integer32"""
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
        *(("other", 1),
          ("notSupported", 2),
          ("disabled", 3),
          ("enabled", 4))
    )


_ControllerEnhancedAutoImportForeignConfigMode_Type.__name__ = "Integer32"
_ControllerEnhancedAutoImportForeignConfigMode_Object = MibTableColumn
controllerEnhancedAutoImportForeignConfigMode = _ControllerEnhancedAutoImportForeignConfigMode_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 6, 1, 20, 130, 1, 1, 82),
    _ControllerEnhancedAutoImportForeignConfigMode_Type()
)
controllerEnhancedAutoImportForeignConfigMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controllerEnhancedAutoImportForeignConfigMode.setStatus("mandatory")
_ControllerBootModeSupported_Type = BooleanType
_ControllerBootModeSupported_Object = MibTableColumn
controllerBootModeSupported = _ControllerBootModeSupported_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 6, 1, 20, 130, 1, 1, 83),
    _ControllerBootModeSupported_Type()
)
controllerBootModeSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controllerBootModeSupported.setStatus("mandatory")


class _ControllerBootMode_Type(Integer32):
    """Custom type controllerBootMode based on Integer32"""
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
        *(("notApplicable", 1),
          ("user", 2),
          ("contOnError", 3),
          ("headlessContOnError", 4),
          ("headlessSafe", 5))
    )


_ControllerBootMode_Type.__name__ = "Integer32"
_ControllerBootMode_Object = MibTableColumn
controllerBootMode = _ControllerBootMode_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 6, 1, 20, 130, 1, 1, 84),
    _ControllerBootMode_Type()
)
controllerBootMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controllerBootMode.setStatus("mandatory")


class _ControllerHighAvailabilityMode_Type(Integer32):
    """Custom type controllerHighAvailabilityMode based on Integer32"""
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
        *(("none", 1),
          ("faultTolerantActivePassive", 2),
          ("faultTolerantActiveActive", 3),
          ("degraded", 4))
    )


_ControllerHighAvailabilityMode_Type.__name__ = "Integer32"
_ControllerHighAvailabilityMode_Object = MibTableColumn
controllerHighAvailabilityMode = _ControllerHighAvailabilityMode_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 6, 1, 20, 130, 1, 1, 85),
    _ControllerHighAvailabilityMode_Type()
)
controllerHighAvailabilityMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controllerHighAvailabilityMode.setStatus("mandatory")
_ControllerPeerController_Type = FQDDString
_ControllerPeerController_Object = MibTableColumn
controllerPeerController = _ControllerPeerController_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 6, 1, 20, 130, 1, 1, 86),
    _ControllerPeerController_Type()
)
controllerPeerController.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controllerPeerController.setStatus("mandatory")
_ControllerEncryptionKeyIdentifier_Type = DisplayString
_ControllerEncryptionKeyIdentifier_Object = MibTableColumn
controllerEncryptionKeyIdentifier = _ControllerEncryptionKeyIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 6, 1, 20, 130, 1, 1, 87),
    _ControllerEncryptionKeyIdentifier_Type()
)
controllerEncryptionKeyIdentifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controllerEncryptionKeyIdentifier.setStatus("mandatory")
_EnclosureTable_Object = MibTable
enclosureTable = _EnclosureTable_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 6, 1, 20, 130, 3)
)
if mibBuilder.loadTexts:
    enclosureTable.setStatus("mandatory")
_EnclosureTableEntry_Object = MibTableRow
enclosureTableEntry = _EnclosureTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 6, 1, 20, 130, 3, 1)
)
enclosureTableEntry.setIndexNames(
    (0, "DELL-RAC-MIB", "enclosureNumber"),
)
if mibBuilder.loadTexts:
    enclosureTableEntry.setStatus("mandatory")


class _EnclosureNumber_Type(Integer32):
    """Custom type enclosureNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_EnclosureNumber_Type.__name__ = "Integer32"
_EnclosureNumber_Object = MibTableColumn
enclosureNumber = _EnclosureNumber_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 6, 1, 20, 130, 3, 1, 1),
    _EnclosureNumber_Type()
)
enclosureNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enclosureNumber.setStatus("mandatory")
_EnclosureName_Type = DisplayString
_EnclosureName_Object = MibTableColumn
enclosureName = _EnclosureName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 6, 1, 20, 130, 3, 1, 2),
    _EnclosureName_Type()
)
enclosureName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enclosureName.setStatus("mandatory")


class _EnclosureState_Type(Integer32):
    """Custom type enclosureState based on Integer32"""
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
        *(("unknown", 1),
          ("ready", 2),
          ("failed", 3),
          ("missing", 4),
          ("degraded", 5),
          ("foreign", 6),
          ("offline", 7),
          ("online", 8),
          ("blocked", 9))
    )


_EnclosureState_Type.__name__ = "Integer32"
_EnclosureState_Object = MibTableColumn
enclosureState = _EnclosureState_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 6, 1, 20, 130, 3, 1, 4),
    _EnclosureState_Type()
)
enclosureState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enclosureState.setStatus("mandatory")
_EnclosureServiceTag_Type = DisplayString
_EnclosureServiceTag_Object = MibTableColumn
enclosureServiceTag = _EnclosureServiceTag_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 6, 1, 20, 130, 3, 1, 8),
    _EnclosureServiceTag_Type()
)
enclosureServiceTag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enclosureServiceTag.setStatus("mandatory")
_EnclosureAssetTag_Type = DisplayString
_EnclosureAssetTag_Object = MibTableColumn
enclosureAssetTag = _EnclosureAssetTag_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 6, 1, 20, 130, 3, 1, 9),
    _EnclosureAssetTag_Type()
)
enclosureAssetTag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enclosureAssetTag.setStatus("mandatory")
_EnclosureConnectedPort_Type = DisplayString
_EnclosureConnectedPort_Object = MibTableColumn
enclosureConnectedPort = _EnclosureConnectedPort_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 6, 1, 20, 130, 3, 1, 19),
    _EnclosureConnectedPort_Type()
)
enclosureConnectedPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enclosureConnectedPort.setStatus("mandatory")
_EnclosureRollUpStatus_Type = ObjectStatusEnum
_EnclosureRollUpStatus_Object = MibTableColumn
enclosureRollUpStatus = _EnclosureRollUpStatus_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 6, 1, 20, 130, 3, 1, 23),
    _EnclosureRollUpStatus_Type()
)
enclosureRollUpStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enclosureRollUpStatus.setStatus("mandatory")
_EnclosureComponentStatus_Type = ObjectStatusEnum
_EnclosureComponentStatus_Object = MibTableColumn
enclosureComponentStatus = _EnclosureComponentStatus_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 6, 1, 20, 130, 3, 1, 24),
    _EnclosureComponentStatus_Type()
)
enclosureComponentStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enclosureComponentStatus.setStatus("mandatory")
_EnclosureFirmwareVersion_Type = DisplayString
_EnclosureFirmwareVersion_Object = MibTableColumn
enclosureFirmwareVersion = _EnclosureFirmwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 6, 1, 20, 130, 3, 1, 26),
    _EnclosureFirmwareVersion_Type()
)
enclosureFirmwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enclosureFirmwareVersion.setStatus("mandatory")
_EnclosureSASAddress_Type = DisplayString
_EnclosureSASAddress_Object = MibTableColumn
enclosureSASAddress = _EnclosureSASAddress_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 6, 1, 20, 130, 3, 1, 30),
    _EnclosureSASAddress_Type()
)
enclosureSASAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enclosureSASAddress.setStatus("mandatory")
_EnclosureDriveCount_Type = Integer32
_EnclosureDriveCount_Object = MibTableColumn
enclosureDriveCount = _EnclosureDriveCount_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 6, 1, 20, 130, 3, 1, 31),
    _EnclosureDriveCount_Type()
)
enclosureDriveCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enclosureDriveCount.setStatus("mandatory")
_EnclosureTotalSlots_Type = Integer32
_EnclosureTotalSlots_Object = MibTableColumn
enclosureTotalSlots = _EnclosureTotalSlots_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 6, 1, 20, 130, 3, 1, 32),
    _EnclosureTotalSlots_Type()
)
enclosureTotalSlots.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enclosureTotalSlots.setStatus("mandatory")
_EnclosureFanCount_Type = DisplayString
_EnclosureFanCount_Object = MibTableColumn
enclosureFanCount = _EnclosureFanCount_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 6, 1, 20, 130, 3, 1, 40),
    _EnclosureFanCount_Type()
)
enclosureFanCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enclosureFanCount.setStatus("mandatory")
_EnclosurePSUCount_Type = DisplayString
_EnclosurePSUCount_Object = MibTableColumn
enclosurePSUCount = _EnclosurePSUCount_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 6, 1, 20, 130, 3, 1, 41),
    _EnclosurePSUCount_Type()
)
enclosurePSUCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enclosurePSUCount.setStatus("mandatory")
_EnclosureEMMCount_Type = DisplayString
_EnclosureEMMCount_Object = MibTableColumn
enclosureEMMCount = _EnclosureEMMCount_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 6, 1, 20, 130, 3, 1, 42),
    _EnclosureEMMCount_Type()
)
enclosureEMMCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enclosureEMMCount.setStatus("mandatory")
_EnclosureTempProbeCount_Type = DisplayString
_EnclosureTempProbeCount_Object = MibTableColumn
enclosureTempProbeCount = _EnclosureTempProbeCount_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 6, 1, 20, 130, 3, 1, 43),
    _EnclosureTempProbeCount_Type()
)
enclosureTempProbeCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enclosureTempProbeCount.setStatus("mandatory")
_EnclosureRedundantPath_Type = DisplayString
_EnclosureRedundantPath_Object = MibTableColumn
enclosureRedundantPath = _EnclosureRedundantPath_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 6, 1, 20, 130, 3, 1, 44),
    _EnclosureRedundantPath_Type()
)
enclosureRedundantPath.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enclosureRedundantPath.setStatus("mandatory")
_EnclosurePosition_Type = DisplayString
_EnclosurePosition_Object = MibTableColumn
enclosurePosition = _EnclosurePosition_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 6, 1, 20, 130, 3, 1, 45),
    _EnclosurePosition_Type()
)
enclosurePosition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enclosurePosition.setStatus("mandatory")
_EnclosureBackplaneBayID_Type = DisplayString
_EnclosureBackplaneBayID_Object = MibTableColumn
enclosureBackplaneBayID = _EnclosureBackplaneBayID_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 6, 1, 20, 130, 3, 1, 46),
    _EnclosureBackplaneBayID_Type()
)
enclosureBackplaneBayID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enclosureBackplaneBayID.setStatus("mandatory")
_EnclosureFQDD_Type = FQDDString
_EnclosureFQDD_Object = MibTableColumn
enclosureFQDD = _EnclosureFQDD_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 6, 1, 20, 130, 3, 1, 47),
    _EnclosureFQDD_Type()
)
enclosureFQDD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enclosureFQDD.setStatus("mandatory")
_EnclosureDisplayName_Type = DisplayString
_EnclosureDisplayName_Object = MibTableColumn
enclosureDisplayName = _EnclosureDisplayName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 6, 1, 20, 130, 3, 1, 48),
    _EnclosureDisplayName_Type()
)
enclosureDisplayName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enclosureDisplayName.setStatus("mandatory")


class _EnclosureType_Type(Integer32):
    """Custom type enclosureType based on Integer32"""
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
        *(("other", 1),
          ("notApplicable", 2),
          ("sassata", 3),
          ("pcie", 4),
          ("universal", 5))
    )


_EnclosureType_Type.__name__ = "Integer32"
_EnclosureType_Object = MibTableColumn
enclosureType = _EnclosureType_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 6, 1, 20, 130, 3, 1, 49),
    _EnclosureType_Type()
)
enclosureType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enclosureType.setStatus("mandatory")
_PhysicalDiskTable_Object = MibTable
physicalDiskTable = _PhysicalDiskTable_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 6, 1, 20, 130, 4)
)
if mibBuilder.loadTexts:
    physicalDiskTable.setStatus("mandatory")
_PhysicalDiskTableEntry_Object = MibTableRow
physicalDiskTableEntry = _PhysicalDiskTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 6, 1, 20, 130, 4, 1)
)
physicalDiskTableEntry.setIndexNames(
    (0, "DELL-RAC-MIB", "physicalDiskNumber"),
)
if mibBuilder.loadTexts:
    physicalDiskTableEntry.setStatus("mandatory")


class _PhysicalDiskNumber_Type(Integer32):
    """Custom type physicalDiskNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000000000),
    )


_PhysicalDiskNumber_Type.__name__ = "Integer32"
_PhysicalDiskNumber_Object = MibTableColumn
physicalDiskNumber = _PhysicalDiskNumber_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 6, 1, 20, 130, 4, 1, 1),
    _PhysicalDiskNumber_Type()
)
physicalDiskNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    physicalDiskNumber.setStatus("mandatory")
_PhysicalDiskName_Type = DisplayString
_PhysicalDiskName_Object = MibTableColumn
physicalDiskName = _PhysicalDiskName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 6, 1, 20, 130, 4, 1, 2),
    _PhysicalDiskName_Type()
)
physicalDiskName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    physicalDiskName.setStatus("mandatory")
_PhysicalDiskManufacturer_Type = DisplayString
_PhysicalDiskManufacturer_Object = MibTableColumn
physicalDiskManufacturer = _PhysicalDiskManufacturer_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 6, 1, 20, 130, 4, 1, 3),
    _PhysicalDiskManufacturer_Type()
)
physicalDiskManufacturer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    physicalDiskManufacturer.setStatus("mandatory")


class _PhysicalDiskState_Type(Integer32):
    """Custom type physicalDiskState based on Integer32"""
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
              10)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 1),
          ("ready", 2),
          ("online", 3),
          ("foreign", 4),
          ("offline", 5),
          ("blocked", 6),
          ("failed", 7),
          ("nonraid", 8),
          ("removed", 9),
          ("readonly", 10))
    )


_PhysicalDiskState_Type.__name__ = "Integer32"
_PhysicalDiskState_Object = MibTableColumn
physicalDiskState = _PhysicalDiskState_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 6, 1, 20, 130, 4, 1, 4),
    _PhysicalDiskState_Type()
)
physicalDiskState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    physicalDiskState.setStatus("mandatory")
_PhysicalDiskProductID_Type = DisplayString
_PhysicalDiskProductID_Object = MibTableColumn
physicalDiskProductID = _PhysicalDiskProductID_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 6, 1, 20, 130, 4, 1, 6),
    _PhysicalDiskProductID_Type()
)
physicalDiskProductID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    physicalDiskProductID.setStatus("mandatory")
_PhysicalDiskSerialNo_Type = DisplayString
_PhysicalDiskSerialNo_Object = MibTableColumn
physicalDiskSerialNo = _PhysicalDiskSerialNo_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 6, 1, 20, 130, 4, 1, 7),
    _PhysicalDiskSerialNo_Type()
)
physicalDiskSerialNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    physicalDiskSerialNo.setStatus("mandatory")
_PhysicalDiskRevision_Type = DisplayString
_PhysicalDiskRevision_Object = MibTableColumn
physicalDiskRevision = _PhysicalDiskRevision_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 6, 1, 20, 130, 4, 1, 8),
    _PhysicalDiskRevision_Type()
)
physicalDiskRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    physicalDiskRevision.setStatus("mandatory")
_PhysicalDiskCapacityInMB_Type = Integer32
_PhysicalDiskCapacityInMB_Object = MibTableColumn
physicalDiskCapacityInMB = _PhysicalDiskCapacityInMB_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 6, 1, 20, 130, 4, 1, 11),
    _PhysicalDiskCapacityInMB_Type()
)
physicalDiskCapacityInMB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    physicalDiskCapacityInMB.setStatus("mandatory")
_PhysicalDiskUsedSpaceInMB_Type = Integer32
_PhysicalDiskUsedSpaceInMB_Object = MibTableColumn
physicalDiskUsedSpaceInMB = _PhysicalDiskUsedSpaceInMB_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 6, 1, 20, 130, 4, 1, 17),
    _PhysicalDiskUsedSpaceInMB_Type()
)
physicalDiskUsedSpaceInMB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    physicalDiskUsedSpaceInMB.setStatus("mandatory")
_PhysicalDiskFreeSpaceInMB_Type = Integer32
_PhysicalDiskFreeSpaceInMB_Object = MibTableColumn
physicalDiskFreeSpaceInMB = _PhysicalDiskFreeSpaceInMB_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 6, 1, 20, 130, 4, 1, 19),
    _PhysicalDiskFreeSpaceInMB_Type()
)
physicalDiskFreeSpaceInMB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    physicalDiskFreeSpaceInMB.setStatus("mandatory")


class _PhysicalDiskBusType_Type(Integer32):
    """Custom type physicalDiskBusType based on Integer32"""
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
        *(("unknown", 1),
          ("scsi", 2),
          ("sas", 3),
          ("sata", 4),
          ("fibre", 5),
          ("pcie", 6))
    )


_PhysicalDiskBusType_Type.__name__ = "Integer32"
_PhysicalDiskBusType_Object = MibTableColumn
physicalDiskBusType = _PhysicalDiskBusType_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 6, 1, 20, 130, 4, 1, 21),
    _PhysicalDiskBusType_Type()
)
physicalDiskBusType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    physicalDiskBusType.setStatus("mandatory")


class _PhysicalDiskSpareState_Type(Integer32):
    """Custom type physicalDiskSpareState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("notASpare", 1),
          ("dedicatedHotSpare", 2),
          ("globalHotSpare", 3))
    )


_PhysicalDiskSpareState_Type.__name__ = "Integer32"
_PhysicalDiskSpareState_Object = MibTableColumn
physicalDiskSpareState = _PhysicalDiskSpareState_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 6, 1, 20, 130, 4, 1, 22),
    _PhysicalDiskSpareState_Type()
)
physicalDiskSpareState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    physicalDiskSpareState.setStatus("mandatory")
_PhysicalDiskComponentStatus_Type = ObjectStatusEnum
_PhysicalDiskComponentStatus_Object = MibTableColumn
physicalDiskComponentStatus = _PhysicalDiskComponentStatus_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 6, 1, 20, 130, 4, 1, 24),
    _PhysicalDiskComponentStatus_Type()
)
physicalDiskComponentStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    physicalDiskComponentStatus.setStatus("mandatory")
_PhysicalDiskPartNumber_Type = DisplayString
_PhysicalDiskPartNumber_Object = MibTableColumn
physicalDiskPartNumber = _PhysicalDiskPartNumber_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 6, 1, 20, 130, 4, 1, 27),
    _PhysicalDiskPartNumber_Type()
)
physicalDiskPartNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    physicalDiskPartNumber.setStatus("mandatory")
_PhysicalDiskSASAddress_Type = DisplayString
_PhysicalDiskSASAddress_Object = MibTableColumn
physicalDiskSASAddress = _PhysicalDiskSASAddress_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 6, 1, 20, 130, 4, 1, 28),
    _PhysicalDiskSASAddress_Type()
)
physicalDiskSASAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    physicalDiskSASAddress.setStatus("mandatory")


class _PhysicalDiskNegotiatedSpeed_Type(Integer32):
    """Custom type physicalDiskNegotiatedSpeed based on Integer32"""
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
        *(("unknown", 1),
          ("oneDotFiveGbps", 2),
          ("threeGbps", 3),
          ("sixGbps", 4),
          ("twelveGbps", 5),
          ("fiveGTps", 6),
          ("eightGTps", 7))
    )


_PhysicalDiskNegotiatedSpeed_Type.__name__ = "Integer32"
_PhysicalDiskNegotiatedSpeed_Object = MibTableColumn
physicalDiskNegotiatedSpeed = _PhysicalDiskNegotiatedSpeed_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 6, 1, 20, 130, 4, 1, 29),
    _PhysicalDiskNegotiatedSpeed_Type()
)
physicalDiskNegotiatedSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    physicalDiskNegotiatedSpeed.setStatus("mandatory")


class _PhysicalDiskCapableSpeed_Type(Integer32):
    """Custom type physicalDiskCapableSpeed based on Integer32"""
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
        *(("unknown", 1),
          ("oneDotFiveGbps", 2),
          ("threeGbps", 3),
          ("sixGbps", 4),
          ("twelveGbps", 5),
          ("fiveGTps", 6),
          ("eightGTps", 7))
    )


_PhysicalDiskCapableSpeed_Type.__name__ = "Integer32"
_PhysicalDiskCapableSpeed_Object = MibTableColumn
physicalDiskCapableSpeed = _PhysicalDiskCapableSpeed_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 6, 1, 20, 130, 4, 1, 30),
    _PhysicalDiskCapableSpeed_Type()
)
physicalDiskCapableSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    physicalDiskCapableSpeed.setStatus("mandatory")
_PhysicalDiskSmartAlertIndication_Type = BooleanType
_PhysicalDiskSmartAlertIndication_Object = MibTableColumn
physicalDiskSmartAlertIndication = _PhysicalDiskSmartAlertIndication_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 6, 1, 20, 130, 4, 1, 31),
    _PhysicalDiskSmartAlertIndication_Type()
)
physicalDiskSmartAlertIndication.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    physicalDiskSmartAlertIndication.setStatus("mandatory")
_PhysicalDiskManufactureDay_Type = DisplayString
_PhysicalDiskManufactureDay_Object = MibTableColumn
physicalDiskManufactureDay = _PhysicalDiskManufactureDay_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 6, 1, 20, 130, 4, 1, 32),
    _PhysicalDiskManufactureDay_Type()
)
physicalDiskManufactureDay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    physicalDiskManufactureDay.setStatus("mandatory")
_PhysicalDiskManufactureWeek_Type = DisplayString
_PhysicalDiskManufactureWeek_Object = MibTableColumn
physicalDiskManufactureWeek = _PhysicalDiskManufactureWeek_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 6, 1, 20, 130, 4, 1, 33),
    _PhysicalDiskManufactureWeek_Type()
)
physicalDiskManufactureWeek.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    physicalDiskManufactureWeek.setStatus("mandatory")
_PhysicalDiskManufactureYear_Type = DisplayString
_PhysicalDiskManufactureYear_Object = MibTableColumn
physicalDiskManufactureYear = _PhysicalDiskManufactureYear_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 6, 1, 20, 130, 4, 1, 34),
    _PhysicalDiskManufactureYear_Type()
)
physicalDiskManufactureYear.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    physicalDiskManufactureYear.setStatus("mandatory")


class _PhysicalDiskMediaType_Type(Integer32):
    """Custom type physicalDiskMediaType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 1),
          ("hdd", 2),
          ("ssd", 3))
    )


_PhysicalDiskMediaType_Type.__name__ = "Integer32"
_PhysicalDiskMediaType_Object = MibTableColumn
physicalDiskMediaType = _PhysicalDiskMediaType_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 6, 1, 20, 130, 4, 1, 35),
    _PhysicalDiskMediaType_Type()
)
physicalDiskMediaType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    physicalDiskMediaType.setStatus("mandatory")


class _PhysicalDiskPowerState_Type(Integer32):
    """Custom type physicalDiskPowerState based on Integer32"""
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
        *(("other", 1),
          ("spunUp", 2),
          ("spunDown", 3),
          ("transition", 4),
          ("on", 5))
    )


_PhysicalDiskPowerState_Type.__name__ = "Integer32"
_PhysicalDiskPowerState_Object = MibTableColumn
physicalDiskPowerState = _PhysicalDiskPowerState_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 6, 1, 20, 130, 4, 1, 42),
    _PhysicalDiskPowerState_Type()
)
physicalDiskPowerState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    physicalDiskPowerState.setStatus("mandatory")


class _PhysicalDiskRemainingRatedWriteEndurance_Type(Integer32):
    """Custom type physicalDiskRemainingRatedWriteEndurance based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_PhysicalDiskRemainingRatedWriteEndurance_Type.__name__ = "Integer32"
_PhysicalDiskRemainingRatedWriteEndurance_Object = MibTableColumn
physicalDiskRemainingRatedWriteEndurance = _PhysicalDiskRemainingRatedWriteEndurance_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 6, 1, 20, 130, 4, 1, 49),
    _PhysicalDiskRemainingRatedWriteEndurance_Type()
)
physicalDiskRemainingRatedWriteEndurance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    physicalDiskRemainingRatedWriteEndurance.setStatus("mandatory")


class _PhysicalDiskOperationalState_Type(Integer32):
    """Custom type physicalDiskOperationalState based on Integer32"""
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
        *(("notApplicable", 1),
          ("rebuild", 2),
          ("clear", 3),
          ("copyback", 4))
    )


_PhysicalDiskOperationalState_Type.__name__ = "Integer32"
_PhysicalDiskOperationalState_Object = MibTableColumn
physicalDiskOperationalState = _PhysicalDiskOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 6, 1, 20, 130, 4, 1, 50),
    _PhysicalDiskOperationalState_Type()
)
physicalDiskOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    physicalDiskOperationalState.setStatus("mandatory")


class _PhysicalDiskProgress_Type(Integer32):
    """Custom type physicalDiskProgress based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_PhysicalDiskProgress_Type.__name__ = "Integer32"
_PhysicalDiskProgress_Object = MibTableColumn
physicalDiskProgress = _PhysicalDiskProgress_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 6, 1, 20, 130, 4, 1, 51),
    _PhysicalDiskProgress_Type()
)
physicalDiskProgress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    physicalDiskProgress.setStatus("mandatory")


class _PhysicalDiskSecurityStatus_Type(Integer32):
    """Custom type physicalDiskSecurityStatus based on Integer32"""
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
        *(("supported", 1),
          ("notSupported", 2),
          ("secured", 3),
          ("locked", 4),
          ("foreign", 5))
    )


_PhysicalDiskSecurityStatus_Type.__name__ = "Integer32"
_PhysicalDiskSecurityStatus_Object = MibTableColumn
physicalDiskSecurityStatus = _PhysicalDiskSecurityStatus_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 6, 1, 20, 130, 4, 1, 52),
    _PhysicalDiskSecurityStatus_Type()
)
physicalDiskSecurityStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    physicalDiskSecurityStatus.setStatus("mandatory")


class _PhysicalDiskFormFactor_Type(Integer32):
    """Custom type physicalDiskFormFactor based on Integer32"""
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
          ("oneDotEight", 2),
          ("twoDotFive", 3),
          ("threeDotFive", 4))
    )


_PhysicalDiskFormFactor_Type.__name__ = "Integer32"
_PhysicalDiskFormFactor_Object = MibTableColumn
physicalDiskFormFactor = _PhysicalDiskFormFactor_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 6, 1, 20, 130, 4, 1, 53),
    _PhysicalDiskFormFactor_Type()
)
physicalDiskFormFactor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    physicalDiskFormFactor.setStatus("mandatory")
_PhysicalDiskFQDD_Type = FQDDString
_PhysicalDiskFQDD_Object = MibTableColumn
physicalDiskFQDD = _PhysicalDiskFQDD_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 6, 1, 20, 130, 4, 1, 54),
    _PhysicalDiskFQDD_Type()
)
physicalDiskFQDD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    physicalDiskFQDD.setStatus("mandatory")
_PhysicalDiskDisplayName_Type = DisplayString
_PhysicalDiskDisplayName_Object = MibTableColumn
physicalDiskDisplayName = _PhysicalDiskDisplayName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 6, 1, 20, 130, 4, 1, 55),
    _PhysicalDiskDisplayName_Type()
)
physicalDiskDisplayName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    physicalDiskDisplayName.setStatus("mandatory")


class _PhysicalDiskT10PICapability_Type(Integer32):
    """Custom type physicalDiskT10PICapability based on Integer32"""
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
          ("capable", 2),
          ("notCapable", 3))
    )


_PhysicalDiskT10PICapability_Type.__name__ = "Integer32"
_PhysicalDiskT10PICapability_Object = MibTableColumn
physicalDiskT10PICapability = _PhysicalDiskT10PICapability_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 6, 1, 20, 130, 4, 1, 57),
    _PhysicalDiskT10PICapability_Type()
)
physicalDiskT10PICapability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    physicalDiskT10PICapability.setStatus("mandatory")
_PhysicalDiskBlockSizeInBytes_Type = Integer32
_PhysicalDiskBlockSizeInBytes_Object = MibTableColumn
physicalDiskBlockSizeInBytes = _PhysicalDiskBlockSizeInBytes_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 6, 1, 20, 130, 4, 1, 58),
    _PhysicalDiskBlockSizeInBytes_Type()
)
physicalDiskBlockSizeInBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    physicalDiskBlockSizeInBytes.setStatus("mandatory")
_PhysicalDiskProtocolVersion_Type = DisplayString
_PhysicalDiskProtocolVersion_Object = MibTableColumn
physicalDiskProtocolVersion = _PhysicalDiskProtocolVersion_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 6, 1, 20, 130, 4, 1, 59),
    _PhysicalDiskProtocolVersion_Type()
)
physicalDiskProtocolVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    physicalDiskProtocolVersion.setStatus("mandatory")


class _PhysicalDiskPCIeNegotiatedLinkWidth_Type(Integer32):
    """Custom type physicalDiskPCIeNegotiatedLinkWidth based on Integer32"""
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
        *(("other", 1),
          ("notApplicable", 2),
          ("byOne", 3),
          ("byTwp", 4),
          ("byFour", 5),
          ("byEight", 6),
          ("bySixteen", 7),
          ("byThirtyTwp", 8))
    )


_PhysicalDiskPCIeNegotiatedLinkWidth_Type.__name__ = "Integer32"
_PhysicalDiskPCIeNegotiatedLinkWidth_Object = MibTableColumn
physicalDiskPCIeNegotiatedLinkWidth = _PhysicalDiskPCIeNegotiatedLinkWidth_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 6, 1, 20, 130, 4, 1, 60),
    _PhysicalDiskPCIeNegotiatedLinkWidth_Type()
)
physicalDiskPCIeNegotiatedLinkWidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    physicalDiskPCIeNegotiatedLinkWidth.setStatus("mandatory")


class _PhysicalDiskPCIeCapableLinkWidth_Type(Integer32):
    """Custom type physicalDiskPCIeCapableLinkWidth based on Integer32"""
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
        *(("other", 1),
          ("notApplicable", 2),
          ("byOne", 3),
          ("byTwp", 4),
          ("byFour", 5),
          ("byEight", 6),
          ("bySixteen", 7),
          ("byThirtyTwp", 8))
    )


_PhysicalDiskPCIeCapableLinkWidth_Type.__name__ = "Integer32"
_PhysicalDiskPCIeCapableLinkWidth_Object = MibTableColumn
physicalDiskPCIeCapableLinkWidth = _PhysicalDiskPCIeCapableLinkWidth_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 6, 1, 20, 130, 4, 1, 61),
    _PhysicalDiskPCIeCapableLinkWidth_Type()
)
physicalDiskPCIeCapableLinkWidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    physicalDiskPCIeCapableLinkWidth.setStatus("mandatory")
_PhysicalDiskCurrentActiveController_Type = FQDDString
_PhysicalDiskCurrentActiveController_Object = MibTableColumn
physicalDiskCurrentActiveController = _PhysicalDiskCurrentActiveController_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 6, 1, 20, 130, 4, 1, 62),
    _PhysicalDiskCurrentActiveController_Type()
)
physicalDiskCurrentActiveController.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    physicalDiskCurrentActiveController.setStatus("mandatory")
_PhysicalDiskFailoverController_Type = FQDDString
_PhysicalDiskFailoverController_Object = MibTableColumn
physicalDiskFailoverController = _PhysicalDiskFailoverController_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 6, 1, 20, 130, 4, 1, 63),
    _PhysicalDiskFailoverController_Type()
)
physicalDiskFailoverController.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    physicalDiskFailoverController.setStatus("mandatory")
_PhysicalDiskForeignKeyIdentifier_Type = DisplayString
_PhysicalDiskForeignKeyIdentifier_Object = MibTableColumn
physicalDiskForeignKeyIdentifier = _PhysicalDiskForeignKeyIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 6, 1, 20, 130, 4, 1, 64),
    _PhysicalDiskForeignKeyIdentifier_Type()
)
physicalDiskForeignKeyIdentifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    physicalDiskForeignKeyIdentifier.setStatus("mandatory")
_EnclosureFanTable_Object = MibTable
enclosureFanTable = _EnclosureFanTable_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 6, 1, 20, 130, 7)
)
if mibBuilder.loadTexts:
    enclosureFanTable.setStatus("mandatory")
_EnclosureFanTableEntry_Object = MibTableRow
enclosureFanTableEntry = _EnclosureFanTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 6, 1, 20, 130, 7, 1)
)
enclosureFanTableEntry.setIndexNames(
    (0, "DELL-RAC-MIB", "enclosureFanNumber"),
)
if mibBuilder.loadTexts:
    enclosureFanTableEntry.setStatus("mandatory")


class _EnclosureFanNumber_Type(Integer32):
    """Custom type enclosureFanNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_EnclosureFanNumber_Type.__name__ = "Integer32"
_EnclosureFanNumber_Object = MibTableColumn
enclosureFanNumber = _EnclosureFanNumber_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 6, 1, 20, 130, 7, 1, 1),
    _EnclosureFanNumber_Type()
)
enclosureFanNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enclosureFanNumber.setStatus("mandatory")
_EnclosureFanName_Type = DisplayString
_EnclosureFanName_Object = MibTableColumn
enclosureFanName = _EnclosureFanName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 6, 1, 20, 130, 7, 1, 2),
    _EnclosureFanName_Type()
)
enclosureFanName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enclosureFanName.setStatus("mandatory")


class _EnclosureFanState_Type(Integer32):
    """Custom type enclosureFanState based on Integer32"""
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
        *(("unknown", 1),
          ("ready", 2),
          ("failed", 3),
          ("missing", 4),
          ("degraded", 5))
    )


_EnclosureFanState_Type.__name__ = "Integer32"
_EnclosureFanState_Object = MibTableColumn
enclosureFanState = _EnclosureFanState_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 6, 1, 20, 130, 7, 1, 4),
    _EnclosureFanState_Type()
)
enclosureFanState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enclosureFanState.setStatus("mandatory")
_EnclosureFanSpeed_Type = Integer32
_EnclosureFanSpeed_Object = MibTableColumn
enclosureFanSpeed = _EnclosureFanSpeed_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 6, 1, 20, 130, 7, 1, 11),
    _EnclosureFanSpeed_Type()
)
enclosureFanSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enclosureFanSpeed.setStatus("mandatory")
_EnclosureFanComponentStatus_Type = ObjectStatusEnum
_EnclosureFanComponentStatus_Object = MibTableColumn
enclosureFanComponentStatus = _EnclosureFanComponentStatus_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 6, 1, 20, 130, 7, 1, 15),
    _EnclosureFanComponentStatus_Type()
)
enclosureFanComponentStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enclosureFanComponentStatus.setStatus("mandatory")
_EnclosureFanFQDD_Type = FQDDString
_EnclosureFanFQDD_Object = MibTableColumn
enclosureFanFQDD = _EnclosureFanFQDD_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 6, 1, 20, 130, 7, 1, 20),
    _EnclosureFanFQDD_Type()
)
enclosureFanFQDD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enclosureFanFQDD.setStatus("mandatory")
_EnclosureFanDisplayName_Type = DisplayString
_EnclosureFanDisplayName_Object = MibTableColumn
enclosureFanDisplayName = _EnclosureFanDisplayName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 6, 1, 20, 130, 7, 1, 21),
    _EnclosureFanDisplayName_Type()
)
enclosureFanDisplayName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enclosureFanDisplayName.setStatus("mandatory")
_EnclosurePowerSupplyTable_Object = MibTable
enclosurePowerSupplyTable = _EnclosurePowerSupplyTable_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 6, 1, 20, 130, 9)
)
if mibBuilder.loadTexts:
    enclosurePowerSupplyTable.setStatus("mandatory")
_EnclosurePowerSupplyTableEntry_Object = MibTableRow
enclosurePowerSupplyTableEntry = _EnclosurePowerSupplyTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 6, 1, 20, 130, 9, 1)
)
enclosurePowerSupplyTableEntry.setIndexNames(
    (0, "DELL-RAC-MIB", "enclosurePowerSupplyNumber"),
)
if mibBuilder.loadTexts:
    enclosurePowerSupplyTableEntry.setStatus("mandatory")


class _EnclosurePowerSupplyNumber_Type(Integer32):
    """Custom type enclosurePowerSupplyNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_EnclosurePowerSupplyNumber_Type.__name__ = "Integer32"
_EnclosurePowerSupplyNumber_Object = MibTableColumn
enclosurePowerSupplyNumber = _EnclosurePowerSupplyNumber_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 6, 1, 20, 130, 9, 1, 1),
    _EnclosurePowerSupplyNumber_Type()
)
enclosurePowerSupplyNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enclosurePowerSupplyNumber.setStatus("mandatory")
_EnclosurePowerSupplyName_Type = DisplayString
_EnclosurePowerSupplyName_Object = MibTableColumn
enclosurePowerSupplyName = _EnclosurePowerSupplyName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 6, 1, 20, 130, 9, 1, 2),
    _EnclosurePowerSupplyName_Type()
)
enclosurePowerSupplyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enclosurePowerSupplyName.setStatus("mandatory")


class _EnclosurePowerSupplyState_Type(Integer32):
    """Custom type enclosurePowerSupplyState based on Integer32"""
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
        *(("unknown", 1),
          ("ready", 2),
          ("failed", 3),
          ("missing", 4),
          ("degraded", 5))
    )


_EnclosurePowerSupplyState_Type.__name__ = "Integer32"
_EnclosurePowerSupplyState_Object = MibTableColumn
enclosurePowerSupplyState = _EnclosurePowerSupplyState_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 6, 1, 20, 130, 9, 1, 4),
    _EnclosurePowerSupplyState_Type()
)
enclosurePowerSupplyState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enclosurePowerSupplyState.setStatus("mandatory")
_EnclosurePowerSupplyPartNumber_Type = DisplayString
_EnclosurePowerSupplyPartNumber_Object = MibTableColumn
enclosurePowerSupplyPartNumber = _EnclosurePowerSupplyPartNumber_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 6, 1, 20, 130, 9, 1, 7),
    _EnclosurePowerSupplyPartNumber_Type()
)
enclosurePowerSupplyPartNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enclosurePowerSupplyPartNumber.setStatus("mandatory")
_EnclosurePowerSupplyComponentStatus_Type = ObjectStatusEnum
_EnclosurePowerSupplyComponentStatus_Object = MibTableColumn
enclosurePowerSupplyComponentStatus = _EnclosurePowerSupplyComponentStatus_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 6, 1, 20, 130, 9, 1, 9),
    _EnclosurePowerSupplyComponentStatus_Type()
)
enclosurePowerSupplyComponentStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enclosurePowerSupplyComponentStatus.setStatus("mandatory")
_EnclosurePowerSupplyFQDD_Type = FQDDString
_EnclosurePowerSupplyFQDD_Object = MibTableColumn
enclosurePowerSupplyFQDD = _EnclosurePowerSupplyFQDD_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 6, 1, 20, 130, 9, 1, 15),
    _EnclosurePowerSupplyFQDD_Type()
)
enclosurePowerSupplyFQDD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enclosurePowerSupplyFQDD.setStatus("mandatory")
_EnclosurePowerSupplyDisplayName_Type = DisplayString
_EnclosurePowerSupplyDisplayName_Object = MibTableColumn
enclosurePowerSupplyDisplayName = _EnclosurePowerSupplyDisplayName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 6, 1, 20, 130, 9, 1, 16),
    _EnclosurePowerSupplyDisplayName_Type()
)
enclosurePowerSupplyDisplayName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enclosurePowerSupplyDisplayName.setStatus("mandatory")
_EnclosureTemperatureProbeTable_Object = MibTable
enclosureTemperatureProbeTable = _EnclosureTemperatureProbeTable_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 6, 1, 20, 130, 11)
)
if mibBuilder.loadTexts:
    enclosureTemperatureProbeTable.setStatus("mandatory")
_EnclosureTemperatureProbeTableEntry_Object = MibTableRow
enclosureTemperatureProbeTableEntry = _EnclosureTemperatureProbeTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 6, 1, 20, 130, 11, 1)
)
enclosureTemperatureProbeTableEntry.setIndexNames(
    (0, "DELL-RAC-MIB", "enclosureTemperatureProbeNumber"),
)
if mibBuilder.loadTexts:
    enclosureTemperatureProbeTableEntry.setStatus("mandatory")


class _EnclosureTemperatureProbeNumber_Type(Integer32):
    """Custom type enclosureTemperatureProbeNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_EnclosureTemperatureProbeNumber_Type.__name__ = "Integer32"
_EnclosureTemperatureProbeNumber_Object = MibTableColumn
enclosureTemperatureProbeNumber = _EnclosureTemperatureProbeNumber_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 6, 1, 20, 130, 11, 1, 1),
    _EnclosureTemperatureProbeNumber_Type()
)
enclosureTemperatureProbeNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enclosureTemperatureProbeNumber.setStatus("mandatory")
_EnclosureTemperatureProbeName_Type = DisplayString
_EnclosureTemperatureProbeName_Object = MibTableColumn
enclosureTemperatureProbeName = _EnclosureTemperatureProbeName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 6, 1, 20, 130, 11, 1, 2),
    _EnclosureTemperatureProbeName_Type()
)
enclosureTemperatureProbeName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enclosureTemperatureProbeName.setStatus("mandatory")


class _EnclosureTemperatureProbeState_Type(Integer32):
    """Custom type enclosureTemperatureProbeState based on Integer32"""
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
        *(("unknown", 1),
          ("ready", 2),
          ("failed", 3),
          ("missing", 4),
          ("degraded", 5),
          ("overWarning", 6),
          ("underWarning", 7))
    )


_EnclosureTemperatureProbeState_Type.__name__ = "Integer32"
_EnclosureTemperatureProbeState_Object = MibTableColumn
enclosureTemperatureProbeState = _EnclosureTemperatureProbeState_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 6, 1, 20, 130, 11, 1, 4),
    _EnclosureTemperatureProbeState_Type()
)
enclosureTemperatureProbeState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enclosureTemperatureProbeState.setStatus("mandatory")
_EnclosureTemperatureProbeMinWarningValue_Type = Integer32
_EnclosureTemperatureProbeMinWarningValue_Object = MibTableColumn
enclosureTemperatureProbeMinWarningValue = _EnclosureTemperatureProbeMinWarningValue_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 6, 1, 20, 130, 11, 1, 7),
    _EnclosureTemperatureProbeMinWarningValue_Type()
)
enclosureTemperatureProbeMinWarningValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enclosureTemperatureProbeMinWarningValue.setStatus("mandatory")
_EnclosureTemperatureProbeMinCriticalValue_Type = Integer32
_EnclosureTemperatureProbeMinCriticalValue_Object = MibTableColumn
enclosureTemperatureProbeMinCriticalValue = _EnclosureTemperatureProbeMinCriticalValue_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 6, 1, 20, 130, 11, 1, 8),
    _EnclosureTemperatureProbeMinCriticalValue_Type()
)
enclosureTemperatureProbeMinCriticalValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enclosureTemperatureProbeMinCriticalValue.setStatus("mandatory")
_EnclosureTemperatureProbeMaxWarningValue_Type = Integer32
_EnclosureTemperatureProbeMaxWarningValue_Object = MibTableColumn
enclosureTemperatureProbeMaxWarningValue = _EnclosureTemperatureProbeMaxWarningValue_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 6, 1, 20, 130, 11, 1, 9),
    _EnclosureTemperatureProbeMaxWarningValue_Type()
)
enclosureTemperatureProbeMaxWarningValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enclosureTemperatureProbeMaxWarningValue.setStatus("mandatory")
_EnclosureTemperatureProbeMaxCriticalValue_Type = Integer32
_EnclosureTemperatureProbeMaxCriticalValue_Object = MibTableColumn
enclosureTemperatureProbeMaxCriticalValue = _EnclosureTemperatureProbeMaxCriticalValue_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 6, 1, 20, 130, 11, 1, 10),
    _EnclosureTemperatureProbeMaxCriticalValue_Type()
)
enclosureTemperatureProbeMaxCriticalValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enclosureTemperatureProbeMaxCriticalValue.setStatus("mandatory")
_EnclosureTemperatureProbeCurValue_Type = Integer32
_EnclosureTemperatureProbeCurValue_Object = MibTableColumn
enclosureTemperatureProbeCurValue = _EnclosureTemperatureProbeCurValue_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 6, 1, 20, 130, 11, 1, 11),
    _EnclosureTemperatureProbeCurValue_Type()
)
enclosureTemperatureProbeCurValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enclosureTemperatureProbeCurValue.setStatus("mandatory")
_EnclosureTemperatureProbeComponentStatus_Type = ObjectStatusEnum
_EnclosureTemperatureProbeComponentStatus_Object = MibTableColumn
enclosureTemperatureProbeComponentStatus = _EnclosureTemperatureProbeComponentStatus_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 6, 1, 20, 130, 11, 1, 13),
    _EnclosureTemperatureProbeComponentStatus_Type()
)
enclosureTemperatureProbeComponentStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enclosureTemperatureProbeComponentStatus.setStatus("mandatory")
_EnclosureTemperatureProbeFQDD_Type = FQDDString
_EnclosureTemperatureProbeFQDD_Object = MibTableColumn
enclosureTemperatureProbeFQDD = _EnclosureTemperatureProbeFQDD_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 6, 1, 20, 130, 11, 1, 15),
    _EnclosureTemperatureProbeFQDD_Type()
)
enclosureTemperatureProbeFQDD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enclosureTemperatureProbeFQDD.setStatus("mandatory")
_EnclosureTemperatureProbeDisplayName_Type = DisplayString
_EnclosureTemperatureProbeDisplayName_Object = MibTableColumn
enclosureTemperatureProbeDisplayName = _EnclosureTemperatureProbeDisplayName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 6, 1, 20, 130, 11, 1, 16),
    _EnclosureTemperatureProbeDisplayName_Type()
)
enclosureTemperatureProbeDisplayName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enclosureTemperatureProbeDisplayName.setStatus("mandatory")
_EnclosureManagementModuleTable_Object = MibTable
enclosureManagementModuleTable = _EnclosureManagementModuleTable_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 6, 1, 20, 130, 13)
)
if mibBuilder.loadTexts:
    enclosureManagementModuleTable.setStatus("mandatory")
_EnclosureManagementModuleTableEntry_Object = MibTableRow
enclosureManagementModuleTableEntry = _EnclosureManagementModuleTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 6, 1, 20, 130, 13, 1)
)
enclosureManagementModuleTableEntry.setIndexNames(
    (0, "DELL-RAC-MIB", "enclosureManagementModuleNumber"),
)
if mibBuilder.loadTexts:
    enclosureManagementModuleTableEntry.setStatus("mandatory")


class _EnclosureManagementModuleNumber_Type(Integer32):
    """Custom type enclosureManagementModuleNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_EnclosureManagementModuleNumber_Type.__name__ = "Integer32"
_EnclosureManagementModuleNumber_Object = MibTableColumn
enclosureManagementModuleNumber = _EnclosureManagementModuleNumber_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 6, 1, 20, 130, 13, 1, 1),
    _EnclosureManagementModuleNumber_Type()
)
enclosureManagementModuleNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enclosureManagementModuleNumber.setStatus("mandatory")
_EnclosureManagementModuleName_Type = DisplayString
_EnclosureManagementModuleName_Object = MibTableColumn
enclosureManagementModuleName = _EnclosureManagementModuleName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 6, 1, 20, 130, 13, 1, 2),
    _EnclosureManagementModuleName_Type()
)
enclosureManagementModuleName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enclosureManagementModuleName.setStatus("mandatory")


class _EnclosureManagementModuleState_Type(Integer32):
    """Custom type enclosureManagementModuleState based on Integer32"""
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
        *(("unknown", 1),
          ("ready", 2),
          ("failed", 3),
          ("missing", 4),
          ("degraded", 5))
    )


_EnclosureManagementModuleState_Type.__name__ = "Integer32"
_EnclosureManagementModuleState_Object = MibTableColumn
enclosureManagementModuleState = _EnclosureManagementModuleState_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 6, 1, 20, 130, 13, 1, 4),
    _EnclosureManagementModuleState_Type()
)
enclosureManagementModuleState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enclosureManagementModuleState.setStatus("mandatory")
_EnclosureManagementModulePartNumber_Type = DisplayString
_EnclosureManagementModulePartNumber_Object = MibTableColumn
enclosureManagementModulePartNumber = _EnclosureManagementModulePartNumber_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 6, 1, 20, 130, 13, 1, 6),
    _EnclosureManagementModulePartNumber_Type()
)
enclosureManagementModulePartNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enclosureManagementModulePartNumber.setStatus("mandatory")
_EnclosureManagementModuleFWVersion_Type = DisplayString
_EnclosureManagementModuleFWVersion_Object = MibTableColumn
enclosureManagementModuleFWVersion = _EnclosureManagementModuleFWVersion_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 6, 1, 20, 130, 13, 1, 8),
    _EnclosureManagementModuleFWVersion_Type()
)
enclosureManagementModuleFWVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enclosureManagementModuleFWVersion.setStatus("mandatory")
_EnclosureManagementModuleComponentStatus_Type = ObjectStatusEnum
_EnclosureManagementModuleComponentStatus_Object = MibTableColumn
enclosureManagementModuleComponentStatus = _EnclosureManagementModuleComponentStatus_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 6, 1, 20, 130, 13, 1, 11),
    _EnclosureManagementModuleComponentStatus_Type()
)
enclosureManagementModuleComponentStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enclosureManagementModuleComponentStatus.setStatus("mandatory")
_EnclosureManagementModuleFQDD_Type = FQDDString
_EnclosureManagementModuleFQDD_Object = MibTableColumn
enclosureManagementModuleFQDD = _EnclosureManagementModuleFQDD_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 6, 1, 20, 130, 13, 1, 15),
    _EnclosureManagementModuleFQDD_Type()
)
enclosureManagementModuleFQDD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enclosureManagementModuleFQDD.setStatus("mandatory")
_EnclosureManagementModuleDisplayName_Type = DisplayString
_EnclosureManagementModuleDisplayName_Object = MibTableColumn
enclosureManagementModuleDisplayName = _EnclosureManagementModuleDisplayName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 6, 1, 20, 130, 13, 1, 16),
    _EnclosureManagementModuleDisplayName_Type()
)
enclosureManagementModuleDisplayName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enclosureManagementModuleDisplayName.setStatus("mandatory")
_BatteryTable_Object = MibTable
batteryTable = _BatteryTable_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 6, 1, 20, 130, 15)
)
if mibBuilder.loadTexts:
    batteryTable.setStatus("mandatory")
_BatteryTableEntry_Object = MibTableRow
batteryTableEntry = _BatteryTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 6, 1, 20, 130, 15, 1)
)
batteryTableEntry.setIndexNames(
    (0, "DELL-RAC-MIB", "batteryNumber"),
)
if mibBuilder.loadTexts:
    batteryTableEntry.setStatus("mandatory")


class _BatteryNumber_Type(Integer32):
    """Custom type batteryNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_BatteryNumber_Type.__name__ = "Integer32"
_BatteryNumber_Object = MibTableColumn
batteryNumber = _BatteryNumber_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 6, 1, 20, 130, 15, 1, 1),
    _BatteryNumber_Type()
)
batteryNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    batteryNumber.setStatus("mandatory")


class _BatteryState_Type(Integer32):
    """Custom type batteryState based on Integer32"""
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
        *(("unknown", 1),
          ("ready", 2),
          ("failed", 3),
          ("degraded", 4),
          ("missing", 5),
          ("charging", 6),
          ("belowThreshold", 7))
    )


_BatteryState_Type.__name__ = "Integer32"
_BatteryState_Object = MibTableColumn
batteryState = _BatteryState_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 6, 1, 20, 130, 15, 1, 4),
    _BatteryState_Type()
)
batteryState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    batteryState.setStatus("mandatory")
_BatteryComponentStatus_Type = ObjectStatusEnum
_BatteryComponentStatus_Object = MibTableColumn
batteryComponentStatus = _BatteryComponentStatus_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 6, 1, 20, 130, 15, 1, 6),
    _BatteryComponentStatus_Type()
)
batteryComponentStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    batteryComponentStatus.setStatus("mandatory")


class _BatteryPredictedCapacity_Type(Integer32):
    """Custom type batteryPredictedCapacity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 1),
          ("failed", 2),
          ("ready", 3))
    )


_BatteryPredictedCapacity_Type.__name__ = "Integer32"
_BatteryPredictedCapacity_Object = MibTableColumn
batteryPredictedCapacity = _BatteryPredictedCapacity_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 6, 1, 20, 130, 15, 1, 10),
    _BatteryPredictedCapacity_Type()
)
batteryPredictedCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    batteryPredictedCapacity.setStatus("obsolete")
_BatteryFQDD_Type = DisplayString
_BatteryFQDD_Object = MibTableColumn
batteryFQDD = _BatteryFQDD_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 6, 1, 20, 130, 15, 1, 20),
    _BatteryFQDD_Type()
)
batteryFQDD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    batteryFQDD.setStatus("mandatory")
_BatteryDisplayName_Type = DisplayString
_BatteryDisplayName_Object = MibTableColumn
batteryDisplayName = _BatteryDisplayName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 6, 1, 20, 130, 15, 1, 21),
    _BatteryDisplayName_Type()
)
batteryDisplayName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    batteryDisplayName.setStatus("mandatory")
_LogicalDevices_ObjectIdentity = ObjectIdentity
logicalDevices = _LogicalDevices_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 6, 1, 20, 140)
)
_VirtualDiskTable_Object = MibTable
virtualDiskTable = _VirtualDiskTable_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 6, 1, 20, 140, 1)
)
if mibBuilder.loadTexts:
    virtualDiskTable.setStatus("mandatory")
_VirtualDiskTableEntry_Object = MibTableRow
virtualDiskTableEntry = _VirtualDiskTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 6, 1, 20, 140, 1, 1)
)
virtualDiskTableEntry.setIndexNames(
    (0, "DELL-RAC-MIB", "virtualDiskNumber"),
)
if mibBuilder.loadTexts:
    virtualDiskTableEntry.setStatus("mandatory")


class _VirtualDiskNumber_Type(Integer32):
    """Custom type virtualDiskNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100000000),
    )


_VirtualDiskNumber_Type.__name__ = "Integer32"
_VirtualDiskNumber_Object = MibTableColumn
virtualDiskNumber = _VirtualDiskNumber_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 6, 1, 20, 140, 1, 1, 1),
    _VirtualDiskNumber_Type()
)
virtualDiskNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualDiskNumber.setStatus("mandatory")
_VirtualDiskName_Type = DisplayString
_VirtualDiskName_Object = MibTableColumn
virtualDiskName = _VirtualDiskName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 6, 1, 20, 140, 1, 1, 2),
    _VirtualDiskName_Type()
)
virtualDiskName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualDiskName.setStatus("mandatory")


class _VirtualDiskState_Type(Integer32):
    """Custom type virtualDiskState based on Integer32"""
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
          ("online", 2),
          ("failed", 3),
          ("degraded", 4))
    )


_VirtualDiskState_Type.__name__ = "Integer32"
_VirtualDiskState_Object = MibTableColumn
virtualDiskState = _VirtualDiskState_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 6, 1, 20, 140, 1, 1, 4),
    _VirtualDiskState_Type()
)
virtualDiskState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualDiskState.setStatus("mandatory")
_VirtualDiskSizeInMB_Type = Integer32
_VirtualDiskSizeInMB_Object = MibTableColumn
virtualDiskSizeInMB = _VirtualDiskSizeInMB_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 6, 1, 20, 140, 1, 1, 6),
    _VirtualDiskSizeInMB_Type()
)
virtualDiskSizeInMB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualDiskSizeInMB.setStatus("mandatory")


class _VirtualDiskWritePolicy_Type(Integer32):
    """Custom type virtualDiskWritePolicy based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("writeThrough", 1),
          ("writeBack", 2),
          ("writeBackForce", 3))
    )


_VirtualDiskWritePolicy_Type.__name__ = "Integer32"
_VirtualDiskWritePolicy_Object = MibTableColumn
virtualDiskWritePolicy = _VirtualDiskWritePolicy_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 6, 1, 20, 140, 1, 1, 10),
    _VirtualDiskWritePolicy_Type()
)
virtualDiskWritePolicy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualDiskWritePolicy.setStatus("mandatory")


class _VirtualDiskReadPolicy_Type(Integer32):
    """Custom type virtualDiskReadPolicy based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("noReadAhead", 1),
          ("readAhead", 2),
          ("adaptiveReadAhead", 3))
    )


_VirtualDiskReadPolicy_Type.__name__ = "Integer32"
_VirtualDiskReadPolicy_Object = MibTableColumn
virtualDiskReadPolicy = _VirtualDiskReadPolicy_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 6, 1, 20, 140, 1, 1, 11),
    _VirtualDiskReadPolicy_Type()
)
virtualDiskReadPolicy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualDiskReadPolicy.setStatus("mandatory")


class _VirtualDiskLayout_Type(Integer32):
    """Custom type virtualDiskLayout based on Integer32"""
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
              10)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("r0", 2),
          ("r1", 3),
          ("r5", 4),
          ("r6", 5),
          ("r10", 6),
          ("r50", 7),
          ("r60", 8),
          ("concatRaid1", 9),
          ("concatRaid5", 10))
    )


_VirtualDiskLayout_Type.__name__ = "Integer32"
_VirtualDiskLayout_Object = MibTableColumn
virtualDiskLayout = _VirtualDiskLayout_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 6, 1, 20, 140, 1, 1, 13),
    _VirtualDiskLayout_Type()
)
virtualDiskLayout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualDiskLayout.setStatus("mandatory")


class _VirtualDiskStripeSize_Type(Integer32):
    """Custom type virtualDiskStripeSize based on Integer32"""
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
              18)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("default", 2),
          ("fiveHundredAndTwelvebytes", 3),
          ("oneKilobytes", 4),
          ("twoKilobytes", 5),
          ("fourKilobytes", 6),
          ("eightKilobytes", 7),
          ("sixteenKilobytes", 8),
          ("thirtyTwoKilobytes", 9),
          ("sixtyFourKilobytes", 10),
          ("oneTwentyEightKilobytes", 11),
          ("twoFiftySixKilobytes", 12),
          ("fiveOneTwoKilobytes", 13),
          ("oneMegabye", 14),
          ("twoMegabytes", 15),
          ("fourMegabytes", 16),
          ("eightMegabytes", 17),
          ("sixteenMegabytes", 18))
    )


_VirtualDiskStripeSize_Type.__name__ = "Integer32"
_VirtualDiskStripeSize_Object = MibTableColumn
virtualDiskStripeSize = _VirtualDiskStripeSize_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 6, 1, 20, 140, 1, 1, 14),
    _VirtualDiskStripeSize_Type()
)
virtualDiskStripeSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualDiskStripeSize.setStatus("mandatory")
_VirtualDiskComponentStatus_Type = ObjectStatusEnum
_VirtualDiskComponentStatus_Object = MibTableColumn
virtualDiskComponentStatus = _VirtualDiskComponentStatus_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 6, 1, 20, 140, 1, 1, 20),
    _VirtualDiskComponentStatus_Type()
)
virtualDiskComponentStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualDiskComponentStatus.setStatus("mandatory")
_VirtualDiskBadBlocksDetected_Type = BooleanType
_VirtualDiskBadBlocksDetected_Object = MibTableColumn
virtualDiskBadBlocksDetected = _VirtualDiskBadBlocksDetected_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 6, 1, 20, 140, 1, 1, 23),
    _VirtualDiskBadBlocksDetected_Type()
)
virtualDiskBadBlocksDetected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualDiskBadBlocksDetected.setStatus("mandatory")
_VirtualDiskSecured_Type = BooleanType
_VirtualDiskSecured_Object = MibTableColumn
virtualDiskSecured = _VirtualDiskSecured_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 6, 1, 20, 140, 1, 1, 24),
    _VirtualDiskSecured_Type()
)
virtualDiskSecured.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualDiskSecured.setStatus("mandatory")
_VirtualDiskIsCacheCade_Type = BooleanType
_VirtualDiskIsCacheCade_Object = MibTableColumn
virtualDiskIsCacheCade = _VirtualDiskIsCacheCade_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 6, 1, 20, 140, 1, 1, 25),
    _VirtualDiskIsCacheCade_Type()
)
virtualDiskIsCacheCade.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualDiskIsCacheCade.setStatus("mandatory")


class _VirtualDiskDiskCachePolicy_Type(Integer32):
    """Custom type virtualDiskDiskCachePolicy based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 1),
          ("disabled", 2),
          ("defullt", 3))
    )


_VirtualDiskDiskCachePolicy_Type.__name__ = "Integer32"
_VirtualDiskDiskCachePolicy_Object = MibTableColumn
virtualDiskDiskCachePolicy = _VirtualDiskDiskCachePolicy_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 6, 1, 20, 140, 1, 1, 26),
    _VirtualDiskDiskCachePolicy_Type()
)
virtualDiskDiskCachePolicy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualDiskDiskCachePolicy.setStatus("mandatory")


class _VirtualDiskOperationalState_Type(Integer32):
    """Custom type virtualDiskOperationalState based on Integer32"""
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
        *(("notApplicable", 1),
          ("reconstructing", 2),
          ("resynching", 3),
          ("initializing", 4),
          ("backgroundInit", 5))
    )


_VirtualDiskOperationalState_Type.__name__ = "Integer32"
_VirtualDiskOperationalState_Object = MibTableColumn
virtualDiskOperationalState = _VirtualDiskOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 6, 1, 20, 140, 1, 1, 30),
    _VirtualDiskOperationalState_Type()
)
virtualDiskOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualDiskOperationalState.setStatus("mandatory")


class _VirtualDiskProgress_Type(Integer32):
    """Custom type virtualDiskProgress based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_VirtualDiskProgress_Type.__name__ = "Integer32"
_VirtualDiskProgress_Object = MibTableColumn
virtualDiskProgress = _VirtualDiskProgress_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 6, 1, 20, 140, 1, 1, 31),
    _VirtualDiskProgress_Type()
)
virtualDiskProgress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualDiskProgress.setStatus("mandatory")
_VirtualDiskAvailableProtocols_Type = DisplayString
_VirtualDiskAvailableProtocols_Object = MibTableColumn
virtualDiskAvailableProtocols = _VirtualDiskAvailableProtocols_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 6, 1, 20, 140, 1, 1, 32),
    _VirtualDiskAvailableProtocols_Type()
)
virtualDiskAvailableProtocols.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualDiskAvailableProtocols.setStatus("mandatory")
_VirtualDiskMediaType_Type = DisplayString
_VirtualDiskMediaType_Object = MibTableColumn
virtualDiskMediaType = _VirtualDiskMediaType_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 6, 1, 20, 140, 1, 1, 33),
    _VirtualDiskMediaType_Type()
)
virtualDiskMediaType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualDiskMediaType.setStatus("mandatory")


class _VirtualDiskRemainingRedundancy_Type(Integer32):
    """Custom type virtualDiskRemainingRedundancy based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_VirtualDiskRemainingRedundancy_Type.__name__ = "Integer32"
_VirtualDiskRemainingRedundancy_Object = MibTableColumn
virtualDiskRemainingRedundancy = _VirtualDiskRemainingRedundancy_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 6, 1, 20, 140, 1, 1, 34),
    _VirtualDiskRemainingRedundancy_Type()
)
virtualDiskRemainingRedundancy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualDiskRemainingRedundancy.setStatus("mandatory")
_VirtualDiskFQDD_Type = FQDDString
_VirtualDiskFQDD_Object = MibTableColumn
virtualDiskFQDD = _VirtualDiskFQDD_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 6, 1, 20, 140, 1, 1, 35),
    _VirtualDiskFQDD_Type()
)
virtualDiskFQDD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualDiskFQDD.setStatus("mandatory")
_VirtualDiskDisplayName_Type = DisplayString
_VirtualDiskDisplayName_Object = MibTableColumn
virtualDiskDisplayName = _VirtualDiskDisplayName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 6, 1, 20, 140, 1, 1, 36),
    _VirtualDiskDisplayName_Type()
)
virtualDiskDisplayName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualDiskDisplayName.setStatus("mandatory")


class _VirtualDiskT10PIStatus_Type(Integer32):
    """Custom type virtualDiskT10PIStatus based on Integer32"""
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
          ("enabled", 2),
          ("disabled", 3))
    )


_VirtualDiskT10PIStatus_Type.__name__ = "Integer32"
_VirtualDiskT10PIStatus_Object = MibTableColumn
virtualDiskT10PIStatus = _VirtualDiskT10PIStatus_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 6, 1, 20, 140, 1, 1, 37),
    _VirtualDiskT10PIStatus_Type()
)
virtualDiskT10PIStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualDiskT10PIStatus.setStatus("mandatory")
_VirtualDiskBlockSizeInBytes_Type = Integer32
_VirtualDiskBlockSizeInBytes_Object = MibTableColumn
virtualDiskBlockSizeInBytes = _VirtualDiskBlockSizeInBytes_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 6, 1, 20, 140, 1, 1, 38),
    _VirtualDiskBlockSizeInBytes_Type()
)
virtualDiskBlockSizeInBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualDiskBlockSizeInBytes.setStatus("mandatory")


class _VirtualDiskAdapter1AccessPolicy_Type(Integer32):
    """Custom type virtualDiskAdapter1AccessPolicy based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noAccess", 1),
          ("fullAccess", 2))
    )


_VirtualDiskAdapter1AccessPolicy_Type.__name__ = "Integer32"
_VirtualDiskAdapter1AccessPolicy_Object = MibTableColumn
virtualDiskAdapter1AccessPolicy = _VirtualDiskAdapter1AccessPolicy_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 6, 1, 20, 140, 1, 1, 39),
    _VirtualDiskAdapter1AccessPolicy_Type()
)
virtualDiskAdapter1AccessPolicy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualDiskAdapter1AccessPolicy.setStatus("mandatory")


class _VirtualDiskAdapter2AccessPolicy_Type(Integer32):
    """Custom type virtualDiskAdapter2AccessPolicy based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noAccess", 1),
          ("fullAccess", 2))
    )


_VirtualDiskAdapter2AccessPolicy_Type.__name__ = "Integer32"
_VirtualDiskAdapter2AccessPolicy_Object = MibTableColumn
virtualDiskAdapter2AccessPolicy = _VirtualDiskAdapter2AccessPolicy_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 6, 1, 20, 140, 1, 1, 40),
    _VirtualDiskAdapter2AccessPolicy_Type()
)
virtualDiskAdapter2AccessPolicy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualDiskAdapter2AccessPolicy.setStatus("mandatory")


class _VirtualDiskAdapter3AccessPolicy_Type(Integer32):
    """Custom type virtualDiskAdapter3AccessPolicy based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noAccess", 1),
          ("fullAccess", 2))
    )


_VirtualDiskAdapter3AccessPolicy_Type.__name__ = "Integer32"
_VirtualDiskAdapter3AccessPolicy_Object = MibTableColumn
virtualDiskAdapter3AccessPolicy = _VirtualDiskAdapter3AccessPolicy_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 6, 1, 20, 140, 1, 1, 41),
    _VirtualDiskAdapter3AccessPolicy_Type()
)
virtualDiskAdapter3AccessPolicy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualDiskAdapter3AccessPolicy.setStatus("mandatory")


class _VirtualDiskAdapter4AccessPolicy_Type(Integer32):
    """Custom type virtualDiskAdapter4AccessPolicy based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noAccess", 1),
          ("fullAccess", 2))
    )


_VirtualDiskAdapter4AccessPolicy_Type.__name__ = "Integer32"
_VirtualDiskAdapter4AccessPolicy_Object = MibTableColumn
virtualDiskAdapter4AccessPolicy = _VirtualDiskAdapter4AccessPolicy_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 6, 1, 20, 140, 1, 1, 42),
    _VirtualDiskAdapter4AccessPolicy_Type()
)
virtualDiskAdapter4AccessPolicy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualDiskAdapter4AccessPolicy.setStatus("mandatory")
_VirtualDiskCurrentActiveController_Type = FQDDString
_VirtualDiskCurrentActiveController_Object = MibTableColumn
virtualDiskCurrentActiveController = _VirtualDiskCurrentActiveController_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 6, 1, 20, 140, 1, 1, 43),
    _VirtualDiskCurrentActiveController_Type()
)
virtualDiskCurrentActiveController.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualDiskCurrentActiveController.setStatus("mandatory")
_VirtualDiskFailoverController_Type = FQDDString
_VirtualDiskFailoverController_Object = MibTableColumn
virtualDiskFailoverController = _VirtualDiskFailoverController_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 6, 1, 20, 140, 1, 1, 44),
    _VirtualDiskFailoverController_Type()
)
virtualDiskFailoverController.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualDiskFailoverController.setStatus("mandatory")
_DrsCMCAlertGroup_ObjectIdentity = ObjectIdentity
drsCMCAlertGroup = _DrsCMCAlertGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 20)
)
_DrsChassisAlertVariables_ObjectIdentity = ObjectIdentity
drsChassisAlertVariables = _DrsChassisAlertVariables_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 20, 10)
)
_DrsCASubSystem_Type = DellString
_DrsCASubSystem_Object = MibScalar
drsCASubSystem = _DrsCASubSystem_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 20, 10, 1),
    _DrsCASubSystem_Type()
)
drsCASubSystem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drsCASubSystem.setStatus("mandatory")
_DrsCASSCurrStatus_Type = DellStatus
_DrsCASSCurrStatus_Object = MibScalar
drsCASSCurrStatus = _DrsCASSCurrStatus_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 20, 10, 2),
    _DrsCASSCurrStatus_Type()
)
drsCASSCurrStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drsCASSCurrStatus.setStatus("mandatory")
_DrsCASSPrevStatus_Type = DellStatus
_DrsCASSPrevStatus_Object = MibScalar
drsCASSPrevStatus = _DrsCASSPrevStatus_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 20, 10, 3),
    _DrsCASSPrevStatus_Type()
)
drsCASSPrevStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drsCASSPrevStatus.setStatus("mandatory")
_DrsCASSChangeTime_Type = TimeTicks
_DrsCASSChangeTime_Object = MibScalar
drsCASSChangeTime = _DrsCASSChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 20, 10, 4),
    _DrsCASSChangeTime_Type()
)
drsCASSChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drsCASSChangeTime.setStatus("mandatory")
_DrsCAMessage_Type = DellString
_DrsCAMessage_Object = MibScalar
drsCAMessage = _DrsCAMessage_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 20, 10, 5),
    _DrsCAMessage_Type()
)
drsCAMessage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drsCAMessage.setStatus("mandatory")
_DrsCMCAlert2Group_ObjectIdentity = ObjectIdentity
drsCMCAlert2Group = _DrsCMCAlert2Group_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 21)
)
_DrsChassisAlert2Variables_ObjectIdentity = ObjectIdentity
drsChassisAlert2Variables = _DrsChassisAlert2Variables_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 21, 10)
)


class _DrsCA2MessageID_Type(DisplayString):
    """Custom type drsCA2MessageID based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_DrsCA2MessageID_Type.__name__ = "DisplayString"
_DrsCA2MessageID_Object = MibScalar
drsCA2MessageID = _DrsCA2MessageID_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 21, 10, 1),
    _DrsCA2MessageID_Type()
)
drsCA2MessageID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drsCA2MessageID.setStatus("mandatory")
_DrsCA2Message_Type = DellString
_DrsCA2Message_Object = MibScalar
drsCA2Message = _DrsCA2Message_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 21, 10, 2),
    _DrsCA2Message_Type()
)
drsCA2Message.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drsCA2Message.setStatus("mandatory")
_DrsCA2MessageArgs_Type = DellString
_DrsCA2MessageArgs_Object = MibScalar
drsCA2MessageArgs = _DrsCA2MessageArgs_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 21, 10, 3),
    _DrsCA2MessageArgs_Type()
)
drsCA2MessageArgs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drsCA2MessageArgs.setStatus("mandatory")
_DrsCA2AlertStatus_Type = DellStatus
_DrsCA2AlertStatus_Object = MibScalar
drsCA2AlertStatus = _DrsCA2AlertStatus_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 21, 10, 4),
    _DrsCA2AlertStatus_Type()
)
drsCA2AlertStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drsCA2AlertStatus.setStatus("mandatory")


class _DrsCA2FQDD_Type(DisplayString):
    """Custom type drsCA2FQDD based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 512),
    )


_DrsCA2FQDD_Type.__name__ = "DisplayString"
_DrsCA2FQDD_Object = MibScalar
drsCA2FQDD = _DrsCA2FQDD_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 21, 10, 5),
    _DrsCA2FQDD_Type()
)
drsCA2FQDD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drsCA2FQDD.setStatus("mandatory")
_DrsAlertGroup_ObjectIdentity = ObjectIdentity
drsAlertGroup = _DrsAlertGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 5000)
)
_DrsAlertVariables_ObjectIdentity = ObjectIdentity
drsAlertVariables = _DrsAlertVariables_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 5000, 10)
)


class _DrsAlertSystem_Type(OctetString):
    """Custom type drsAlertSystem based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_DrsAlertSystem_Type.__name__ = "OctetString"
_DrsAlertSystem_Object = MibScalar
drsAlertSystem = _DrsAlertSystem_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 5000, 10, 1),
    _DrsAlertSystem_Type()
)
drsAlertSystem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drsAlertSystem.setStatus("mandatory")
_DrsAlertTableIndexOID_Type = ObjectIdentifier
_DrsAlertTableIndexOID_Object = MibScalar
drsAlertTableIndexOID = _DrsAlertTableIndexOID_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 5000, 10, 2),
    _DrsAlertTableIndexOID_Type()
)
drsAlertTableIndexOID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drsAlertTableIndexOID.setStatus("mandatory")


class _DrsAlertMessage_Type(OctetString):
    """Custom type drsAlertMessage based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 1024),
    )


_DrsAlertMessage_Type.__name__ = "OctetString"
_DrsAlertMessage_Object = MibScalar
drsAlertMessage = _DrsAlertMessage_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 5000, 10, 3),
    _DrsAlertMessage_Type()
)
drsAlertMessage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drsAlertMessage.setStatus("mandatory")
_DrsAlertCurrentStatus_Type = DellStatus
_DrsAlertCurrentStatus_Object = MibScalar
drsAlertCurrentStatus = _DrsAlertCurrentStatus_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 5000, 10, 4),
    _DrsAlertCurrentStatus_Type()
)
drsAlertCurrentStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drsAlertCurrentStatus.setStatus("mandatory")
_DrsAlertPreviousStatus_Type = DellStatus
_DrsAlertPreviousStatus_Object = MibScalar
drsAlertPreviousStatus = _DrsAlertPreviousStatus_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 5000, 10, 5),
    _DrsAlertPreviousStatus_Type()
)
drsAlertPreviousStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drsAlertPreviousStatus.setStatus("mandatory")


class _DrsAlertData_Type(OctetString):
    """Custom type drsAlertData based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 1024),
    )


_DrsAlertData_Type.__name__ = "OctetString"
_DrsAlertData_Object = MibScalar
drsAlertData = _DrsAlertData_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 5000, 10, 6),
    _DrsAlertData_Type()
)
drsAlertData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drsAlertData.setStatus("mandatory")

# Managed Objects groups


# Notification objects

alertDrscTestTrapEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 0, 1001)
)
alertDrscTestTrapEvent.setObjects(
      *(("DELL-RAC-MIB", "drsAlertSystem"),
        ("DELL-RAC-MIB", "drsAlertTableIndexOID"),
        ("DELL-RAC-MIB", "drsAlertMessage"),
        ("DELL-RAC-MIB", "drsAlertCurrentStatus"),
        ("DELL-RAC-MIB", "drsAlertPreviousStatus"),
        ("DELL-RAC-MIB", "drsAlertData"))
)
if mibBuilder.loadTexts:
    alertDrscTestTrapEvent.setStatus(
        ""
    )

alertDrscAuthError = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 0, 1002)
)
alertDrscAuthError.setObjects(
      *(("DELL-RAC-MIB", "drsAlertSystem"),
        ("DELL-RAC-MIB", "drsAlertTableIndexOID"),
        ("DELL-RAC-MIB", "drsAlertMessage"),
        ("DELL-RAC-MIB", "drsAlertCurrentStatus"),
        ("DELL-RAC-MIB", "drsAlertPreviousStatus"),
        ("DELL-RAC-MIB", "drsAlertData"))
)
if mibBuilder.loadTexts:
    alertDrscAuthError.setStatus(
        ""
    )

alertDrscLostESM = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 0, 1003)
)
alertDrscLostESM.setObjects(
      *(("DELL-RAC-MIB", "drsAlertSystem"),
        ("DELL-RAC-MIB", "drsAlertTableIndexOID"),
        ("DELL-RAC-MIB", "drsAlertMessage"),
        ("DELL-RAC-MIB", "drsAlertCurrentStatus"),
        ("DELL-RAC-MIB", "drsAlertPreviousStatus"),
        ("DELL-RAC-MIB", "drsAlertData"))
)
if mibBuilder.loadTexts:
    alertDrscLostESM.setStatus(
        ""
    )

alertDrscFoundESM = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 0, 1004)
)
alertDrscFoundESM.setObjects(
      *(("DELL-RAC-MIB", "drsAlertSystem"),
        ("DELL-RAC-MIB", "drsAlertTableIndexOID"),
        ("DELL-RAC-MIB", "drsAlertMessage"),
        ("DELL-RAC-MIB", "drsAlertCurrentStatus"),
        ("DELL-RAC-MIB", "drsAlertPreviousStatus"),
        ("DELL-RAC-MIB", "drsAlertData"))
)
if mibBuilder.loadTexts:
    alertDrscFoundESM.setStatus(
        ""
    )

alertDrscPowerOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 0, 1005)
)
alertDrscPowerOff.setObjects(
      *(("DELL-RAC-MIB", "drsAlertSystem"),
        ("DELL-RAC-MIB", "drsAlertTableIndexOID"),
        ("DELL-RAC-MIB", "drsAlertMessage"),
        ("DELL-RAC-MIB", "drsAlertCurrentStatus"),
        ("DELL-RAC-MIB", "drsAlertPreviousStatus"),
        ("DELL-RAC-MIB", "drsAlertData"))
)
if mibBuilder.loadTexts:
    alertDrscPowerOff.setStatus(
        ""
    )

alertDrscPowerOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 0, 1006)
)
alertDrscPowerOn.setObjects(
      *(("DELL-RAC-MIB", "drsAlertSystem"),
        ("DELL-RAC-MIB", "drsAlertTableIndexOID"),
        ("DELL-RAC-MIB", "drsAlertMessage"),
        ("DELL-RAC-MIB", "drsAlertCurrentStatus"),
        ("DELL-RAC-MIB", "drsAlertPreviousStatus"),
        ("DELL-RAC-MIB", "drsAlertData"))
)
if mibBuilder.loadTexts:
    alertDrscPowerOn.setStatus(
        ""
    )

alertDrscWatchdogExpired = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 0, 1007)
)
alertDrscWatchdogExpired.setObjects(
      *(("DELL-RAC-MIB", "drsAlertSystem"),
        ("DELL-RAC-MIB", "drsAlertTableIndexOID"),
        ("DELL-RAC-MIB", "drsAlertMessage"),
        ("DELL-RAC-MIB", "drsAlertCurrentStatus"),
        ("DELL-RAC-MIB", "drsAlertPreviousStatus"),
        ("DELL-RAC-MIB", "drsAlertData"))
)
if mibBuilder.loadTexts:
    alertDrscWatchdogExpired.setStatus(
        ""
    )

alertDrscBattLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 0, 1008)
)
alertDrscBattLow.setObjects(
      *(("DELL-RAC-MIB", "drsAlertSystem"),
        ("DELL-RAC-MIB", "drsAlertTableIndexOID"),
        ("DELL-RAC-MIB", "drsAlertMessage"),
        ("DELL-RAC-MIB", "drsAlertCurrentStatus"),
        ("DELL-RAC-MIB", "drsAlertPreviousStatus"),
        ("DELL-RAC-MIB", "drsAlertData"))
)
if mibBuilder.loadTexts:
    alertDrscBattLow.setStatus(
        ""
    )

alertDrscTempNormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 0, 1009)
)
alertDrscTempNormal.setObjects(
      *(("DELL-RAC-MIB", "drsAlertSystem"),
        ("DELL-RAC-MIB", "drsAlertTableIndexOID"),
        ("DELL-RAC-MIB", "drsAlertMessage"),
        ("DELL-RAC-MIB", "drsAlertCurrentStatus"),
        ("DELL-RAC-MIB", "drsAlertPreviousStatus"),
        ("DELL-RAC-MIB", "drsAlertData"))
)
if mibBuilder.loadTexts:
    alertDrscTempNormal.setStatus(
        ""
    )

alertDrscTempWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 0, 1010)
)
alertDrscTempWarning.setObjects(
      *(("DELL-RAC-MIB", "drsAlertSystem"),
        ("DELL-RAC-MIB", "drsAlertTableIndexOID"),
        ("DELL-RAC-MIB", "drsAlertMessage"),
        ("DELL-RAC-MIB", "drsAlertCurrentStatus"),
        ("DELL-RAC-MIB", "drsAlertPreviousStatus"),
        ("DELL-RAC-MIB", "drsAlertData"))
)
if mibBuilder.loadTexts:
    alertDrscTempWarning.setStatus(
        ""
    )

alertDrscTempCritical = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 0, 1011)
)
alertDrscTempCritical.setObjects(
      *(("DELL-RAC-MIB", "drsAlertSystem"),
        ("DELL-RAC-MIB", "drsAlertTableIndexOID"),
        ("DELL-RAC-MIB", "drsAlertMessage"),
        ("DELL-RAC-MIB", "drsAlertCurrentStatus"),
        ("DELL-RAC-MIB", "drsAlertPreviousStatus"),
        ("DELL-RAC-MIB", "drsAlertData"))
)
if mibBuilder.loadTexts:
    alertDrscTempCritical.setStatus(
        ""
    )

alertDrscVoltNormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 0, 1012)
)
alertDrscVoltNormal.setObjects(
      *(("DELL-RAC-MIB", "drsAlertSystem"),
        ("DELL-RAC-MIB", "drsAlertTableIndexOID"),
        ("DELL-RAC-MIB", "drsAlertMessage"),
        ("DELL-RAC-MIB", "drsAlertCurrentStatus"),
        ("DELL-RAC-MIB", "drsAlertPreviousStatus"),
        ("DELL-RAC-MIB", "drsAlertData"))
)
if mibBuilder.loadTexts:
    alertDrscVoltNormal.setStatus(
        ""
    )

alertDrscVoltWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 0, 1013)
)
alertDrscVoltWarning.setObjects(
      *(("DELL-RAC-MIB", "drsAlertSystem"),
        ("DELL-RAC-MIB", "drsAlertTableIndexOID"),
        ("DELL-RAC-MIB", "drsAlertMessage"),
        ("DELL-RAC-MIB", "drsAlertCurrentStatus"),
        ("DELL-RAC-MIB", "drsAlertPreviousStatus"),
        ("DELL-RAC-MIB", "drsAlertData"))
)
if mibBuilder.loadTexts:
    alertDrscVoltWarning.setStatus(
        ""
    )

alertDrscVoltCritical = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 0, 1014)
)
alertDrscVoltCritical.setObjects(
      *(("DELL-RAC-MIB", "drsAlertSystem"),
        ("DELL-RAC-MIB", "drsAlertTableIndexOID"),
        ("DELL-RAC-MIB", "drsAlertMessage"),
        ("DELL-RAC-MIB", "drsAlertCurrentStatus"),
        ("DELL-RAC-MIB", "drsAlertPreviousStatus"),
        ("DELL-RAC-MIB", "drsAlertData"))
)
if mibBuilder.loadTexts:
    alertDrscVoltCritical.setStatus(
        ""
    )

alertDrscSELWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 0, 1015)
)
alertDrscSELWarning.setObjects(
      *(("DELL-RAC-MIB", "drsAlertSystem"),
        ("DELL-RAC-MIB", "drsAlertTableIndexOID"),
        ("DELL-RAC-MIB", "drsAlertMessage"),
        ("DELL-RAC-MIB", "drsAlertCurrentStatus"),
        ("DELL-RAC-MIB", "drsAlertPreviousStatus"),
        ("DELL-RAC-MIB", "drsAlertData"))
)
if mibBuilder.loadTexts:
    alertDrscSELWarning.setStatus(
        ""
    )

alertDrscSELCritical = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 0, 1016)
)
alertDrscSELCritical.setObjects(
      *(("DELL-RAC-MIB", "drsAlertSystem"),
        ("DELL-RAC-MIB", "drsAlertTableIndexOID"),
        ("DELL-RAC-MIB", "drsAlertMessage"),
        ("DELL-RAC-MIB", "drsAlertCurrentStatus"),
        ("DELL-RAC-MIB", "drsAlertPreviousStatus"),
        ("DELL-RAC-MIB", "drsAlertData"))
)
if mibBuilder.loadTexts:
    alertDrscSELCritical.setStatus(
        ""
    )

alertDrscSEL80percentFull = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 0, 1017)
)
alertDrscSEL80percentFull.setObjects(
      *(("DELL-RAC-MIB", "drsAlertSystem"),
        ("DELL-RAC-MIB", "drsAlertTableIndexOID"),
        ("DELL-RAC-MIB", "drsAlertMessage"),
        ("DELL-RAC-MIB", "drsAlertCurrentStatus"),
        ("DELL-RAC-MIB", "drsAlertPreviousStatus"),
        ("DELL-RAC-MIB", "drsAlertData"))
)
if mibBuilder.loadTexts:
    alertDrscSEL80percentFull.setStatus(
        ""
    )

alertDrscSEL90percentFull = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 0, 1018)
)
alertDrscSEL90percentFull.setObjects(
      *(("DELL-RAC-MIB", "drsAlertSystem"),
        ("DELL-RAC-MIB", "drsAlertTableIndexOID"),
        ("DELL-RAC-MIB", "drsAlertMessage"),
        ("DELL-RAC-MIB", "drsAlertCurrentStatus"),
        ("DELL-RAC-MIB", "drsAlertPreviousStatus"),
        ("DELL-RAC-MIB", "drsAlertData"))
)
if mibBuilder.loadTexts:
    alertDrscSEL90percentFull.setStatus(
        ""
    )

alertDrscSEL100percentFull = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 0, 1019)
)
alertDrscSEL100percentFull.setObjects(
      *(("DELL-RAC-MIB", "drsAlertSystem"),
        ("DELL-RAC-MIB", "drsAlertTableIndexOID"),
        ("DELL-RAC-MIB", "drsAlertMessage"),
        ("DELL-RAC-MIB", "drsAlertCurrentStatus"),
        ("DELL-RAC-MIB", "drsAlertPreviousStatus"),
        ("DELL-RAC-MIB", "drsAlertData"))
)
if mibBuilder.loadTexts:
    alertDrscSEL100percentFull.setStatus(
        ""
    )

alertDrscSELNormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 0, 1020)
)
alertDrscSELNormal.setObjects(
      *(("DELL-RAC-MIB", "drsAlertSystem"),
        ("DELL-RAC-MIB", "drsAlertTableIndexOID"),
        ("DELL-RAC-MIB", "drsAlertMessage"),
        ("DELL-RAC-MIB", "drsAlertCurrentStatus"),
        ("DELL-RAC-MIB", "drsAlertPreviousStatus"),
        ("DELL-RAC-MIB", "drsAlertData"))
)
if mibBuilder.loadTexts:
    alertDrscSELNormal.setStatus(
        ""
    )

alertCMCTestTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 0, 2000)
)
if mibBuilder.loadTexts:
    alertCMCTestTrap.setStatus(
        ""
    )

alertCMCNormalTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 0, 2002)
)
alertCMCNormalTrap.setObjects(
      *(("DELL-RAC-MIB", "drsProductChassisName"),
        ("DELL-RAC-MIB", "drsProductChassisLocation"),
        ("DELL-RAC-MIB", "drsGlobalCurrStatus"),
        ("DELL-RAC-MIB", "drsCASubSystem"),
        ("DELL-RAC-MIB", "drsCASSCurrStatus"),
        ("DELL-RAC-MIB", "drsCASSPrevStatus"),
        ("DELL-RAC-MIB", "drsCASSChangeTime"),
        ("DELL-RAC-MIB", "drsCAMessage"))
)
if mibBuilder.loadTexts:
    alertCMCNormalTrap.setStatus(
        ""
    )

alertCMCWarningTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 0, 2003)
)
alertCMCWarningTrap.setObjects(
      *(("DELL-RAC-MIB", "drsProductChassisName"),
        ("DELL-RAC-MIB", "drsProductChassisLocation"),
        ("DELL-RAC-MIB", "drsGlobalCurrStatus"),
        ("DELL-RAC-MIB", "drsCASubSystem"),
        ("DELL-RAC-MIB", "drsCASSCurrStatus"),
        ("DELL-RAC-MIB", "drsCASSPrevStatus"),
        ("DELL-RAC-MIB", "drsCASSChangeTime"),
        ("DELL-RAC-MIB", "drsCAMessage"))
)
if mibBuilder.loadTexts:
    alertCMCWarningTrap.setStatus(
        ""
    )

alertCMCCriticalTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 0, 2004)
)
alertCMCCriticalTrap.setObjects(
      *(("DELL-RAC-MIB", "drsProductChassisName"),
        ("DELL-RAC-MIB", "drsProductChassisLocation"),
        ("DELL-RAC-MIB", "drsGlobalCurrStatus"),
        ("DELL-RAC-MIB", "drsCASubSystem"),
        ("DELL-RAC-MIB", "drsCASSCurrStatus"),
        ("DELL-RAC-MIB", "drsCASSPrevStatus"),
        ("DELL-RAC-MIB", "drsCASSChangeTime"),
        ("DELL-RAC-MIB", "drsCAMessage"))
)
if mibBuilder.loadTexts:
    alertCMCCriticalTrap.setStatus(
        ""
    )

alertCMCNonRecoverableTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 0, 2005)
)
alertCMCNonRecoverableTrap.setObjects(
      *(("DELL-RAC-MIB", "drsProductChassisName"),
        ("DELL-RAC-MIB", "drsProductChassisLocation"),
        ("DELL-RAC-MIB", "drsGlobalCurrStatus"),
        ("DELL-RAC-MIB", "drsCASubSystem"),
        ("DELL-RAC-MIB", "drsCASSCurrStatus"),
        ("DELL-RAC-MIB", "drsCASSPrevStatus"),
        ("DELL-RAC-MIB", "drsCASSChangeTime"),
        ("DELL-RAC-MIB", "drsCAMessage"))
)
if mibBuilder.loadTexts:
    alertCMCNonRecoverableTrap.setStatus(
        ""
    )

alert2FanFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 21, 0, 2153)
)
alert2FanFailure.setObjects(
      *(("DELL-RAC-MIB", "drsCA2MessageID"),
        ("DELL-RAC-MIB", "drsCA2Message"),
        ("DELL-RAC-MIB", "drsCA2MessageArgs"),
        ("DELL-RAC-MIB", "drsCA2AlertStatus"),
        ("DELL-RAC-MIB", "drsCA2FQDD"),
        ("DELL-RAC-MIB", "drsProductChassisName"),
        ("DELL-RAC-MIB", "drsProductChassisLocation"),
        ("DELL-RAC-MIB", "drsChassisServiceTag"),
        ("DELL-RAC-MIB", "drsGlobalCurrStatus"))
)
if mibBuilder.loadTexts:
    alert2FanFailure.setStatus(
        ""
    )

alert2FanWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 21, 0, 2154)
)
alert2FanWarning.setObjects(
      *(("DELL-RAC-MIB", "drsCA2MessageID"),
        ("DELL-RAC-MIB", "drsCA2Message"),
        ("DELL-RAC-MIB", "drsCA2MessageArgs"),
        ("DELL-RAC-MIB", "drsCA2AlertStatus"),
        ("DELL-RAC-MIB", "drsCA2FQDD"),
        ("DELL-RAC-MIB", "drsProductChassisName"),
        ("DELL-RAC-MIB", "drsProductChassisLocation"),
        ("DELL-RAC-MIB", "drsChassisServiceTag"),
        ("DELL-RAC-MIB", "drsGlobalCurrStatus"))
)
if mibBuilder.loadTexts:
    alert2FanWarning.setStatus(
        ""
    )

alert2FanInformation = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 21, 0, 2155)
)
alert2FanInformation.setObjects(
      *(("DELL-RAC-MIB", "drsCA2MessageID"),
        ("DELL-RAC-MIB", "drsCA2Message"),
        ("DELL-RAC-MIB", "drsCA2MessageArgs"),
        ("DELL-RAC-MIB", "drsCA2AlertStatus"),
        ("DELL-RAC-MIB", "drsCA2FQDD"),
        ("DELL-RAC-MIB", "drsProductChassisName"),
        ("DELL-RAC-MIB", "drsProductChassisLocation"),
        ("DELL-RAC-MIB", "drsChassisServiceTag"),
        ("DELL-RAC-MIB", "drsGlobalCurrStatus"))
)
if mibBuilder.loadTexts:
    alert2FanInformation.setStatus(
        ""
    )

alert2TemperatureProbeFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 21, 0, 2161)
)
alert2TemperatureProbeFailure.setObjects(
      *(("DELL-RAC-MIB", "drsCA2MessageID"),
        ("DELL-RAC-MIB", "drsCA2Message"),
        ("DELL-RAC-MIB", "drsCA2MessageArgs"),
        ("DELL-RAC-MIB", "drsCA2AlertStatus"),
        ("DELL-RAC-MIB", "drsCA2FQDD"),
        ("DELL-RAC-MIB", "drsProductChassisName"),
        ("DELL-RAC-MIB", "drsProductChassisLocation"),
        ("DELL-RAC-MIB", "drsChassisServiceTag"),
        ("DELL-RAC-MIB", "drsGlobalCurrStatus"))
)
if mibBuilder.loadTexts:
    alert2TemperatureProbeFailure.setStatus(
        ""
    )

alert2TemperatureProbeWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 21, 0, 2162)
)
alert2TemperatureProbeWarning.setObjects(
      *(("DELL-RAC-MIB", "drsCA2MessageID"),
        ("DELL-RAC-MIB", "drsCA2Message"),
        ("DELL-RAC-MIB", "drsCA2MessageArgs"),
        ("DELL-RAC-MIB", "drsCA2AlertStatus"),
        ("DELL-RAC-MIB", "drsCA2FQDD"),
        ("DELL-RAC-MIB", "drsProductChassisName"),
        ("DELL-RAC-MIB", "drsProductChassisLocation"),
        ("DELL-RAC-MIB", "drsChassisServiceTag"),
        ("DELL-RAC-MIB", "drsGlobalCurrStatus"))
)
if mibBuilder.loadTexts:
    alert2TemperatureProbeWarning.setStatus(
        ""
    )

alert2TemperatureProbeNormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 21, 0, 2163)
)
alert2TemperatureProbeNormal.setObjects(
      *(("DELL-RAC-MIB", "drsCA2MessageID"),
        ("DELL-RAC-MIB", "drsCA2Message"),
        ("DELL-RAC-MIB", "drsCA2MessageArgs"),
        ("DELL-RAC-MIB", "drsCA2AlertStatus"),
        ("DELL-RAC-MIB", "drsCA2FQDD"),
        ("DELL-RAC-MIB", "drsProductChassisName"),
        ("DELL-RAC-MIB", "drsProductChassisLocation"),
        ("DELL-RAC-MIB", "drsChassisServiceTag"),
        ("DELL-RAC-MIB", "drsGlobalCurrStatus"))
)
if mibBuilder.loadTexts:
    alert2TemperatureProbeNormal.setStatus(
        ""
    )

alert2VoltageProbeFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 21, 0, 2169)
)
alert2VoltageProbeFailure.setObjects(
      *(("DELL-RAC-MIB", "drsCA2MessageID"),
        ("DELL-RAC-MIB", "drsCA2Message"),
        ("DELL-RAC-MIB", "drsCA2MessageArgs"),
        ("DELL-RAC-MIB", "drsCA2AlertStatus"),
        ("DELL-RAC-MIB", "drsCA2FQDD"),
        ("DELL-RAC-MIB", "drsProductChassisName"),
        ("DELL-RAC-MIB", "drsProductChassisLocation"),
        ("DELL-RAC-MIB", "drsChassisServiceTag"),
        ("DELL-RAC-MIB", "drsGlobalCurrStatus"))
)
if mibBuilder.loadTexts:
    alert2VoltageProbeFailure.setStatus(
        ""
    )

alert2VoltageProbeWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 21, 0, 2170)
)
alert2VoltageProbeWarning.setObjects(
      *(("DELL-RAC-MIB", "drsCA2MessageID"),
        ("DELL-RAC-MIB", "drsCA2Message"),
        ("DELL-RAC-MIB", "drsCA2MessageArgs"),
        ("DELL-RAC-MIB", "drsCA2AlertStatus"),
        ("DELL-RAC-MIB", "drsCA2FQDD"),
        ("DELL-RAC-MIB", "drsProductChassisName"),
        ("DELL-RAC-MIB", "drsProductChassisLocation"),
        ("DELL-RAC-MIB", "drsChassisServiceTag"),
        ("DELL-RAC-MIB", "drsGlobalCurrStatus"))
)
if mibBuilder.loadTexts:
    alert2VoltageProbeWarning.setStatus(
        ""
    )

alert2VoltageProbeNormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 21, 0, 2171)
)
alert2VoltageProbeNormal.setObjects(
      *(("DELL-RAC-MIB", "drsCA2MessageID"),
        ("DELL-RAC-MIB", "drsCA2Message"),
        ("DELL-RAC-MIB", "drsCA2MessageArgs"),
        ("DELL-RAC-MIB", "drsCA2AlertStatus"),
        ("DELL-RAC-MIB", "drsCA2FQDD"),
        ("DELL-RAC-MIB", "drsProductChassisName"),
        ("DELL-RAC-MIB", "drsProductChassisLocation"),
        ("DELL-RAC-MIB", "drsChassisServiceTag"),
        ("DELL-RAC-MIB", "drsGlobalCurrStatus"))
)
if mibBuilder.loadTexts:
    alert2VoltageProbeNormal.setStatus(
        ""
    )

alert2AmperageProbeFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 21, 0, 2177)
)
alert2AmperageProbeFailure.setObjects(
      *(("DELL-RAC-MIB", "drsCA2MessageID"),
        ("DELL-RAC-MIB", "drsCA2Message"),
        ("DELL-RAC-MIB", "drsCA2MessageArgs"),
        ("DELL-RAC-MIB", "drsCA2AlertStatus"),
        ("DELL-RAC-MIB", "drsCA2FQDD"),
        ("DELL-RAC-MIB", "drsProductChassisName"),
        ("DELL-RAC-MIB", "drsProductChassisLocation"),
        ("DELL-RAC-MIB", "drsChassisServiceTag"),
        ("DELL-RAC-MIB", "drsGlobalCurrStatus"))
)
if mibBuilder.loadTexts:
    alert2AmperageProbeFailure.setStatus(
        ""
    )

alert2AmperageProbeWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 21, 0, 2178)
)
alert2AmperageProbeWarning.setObjects(
      *(("DELL-RAC-MIB", "drsCA2MessageID"),
        ("DELL-RAC-MIB", "drsCA2Message"),
        ("DELL-RAC-MIB", "drsCA2MessageArgs"),
        ("DELL-RAC-MIB", "drsCA2AlertStatus"),
        ("DELL-RAC-MIB", "drsCA2FQDD"),
        ("DELL-RAC-MIB", "drsProductChassisName"),
        ("DELL-RAC-MIB", "drsProductChassisLocation"),
        ("DELL-RAC-MIB", "drsChassisServiceTag"),
        ("DELL-RAC-MIB", "drsGlobalCurrStatus"))
)
if mibBuilder.loadTexts:
    alert2AmperageProbeWarning.setStatus(
        ""
    )

alert2AmperageProbeNormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 21, 0, 2179)
)
alert2AmperageProbeNormal.setObjects(
      *(("DELL-RAC-MIB", "drsCA2MessageID"),
        ("DELL-RAC-MIB", "drsCA2Message"),
        ("DELL-RAC-MIB", "drsCA2MessageArgs"),
        ("DELL-RAC-MIB", "drsCA2AlertStatus"),
        ("DELL-RAC-MIB", "drsCA2FQDD"),
        ("DELL-RAC-MIB", "drsProductChassisName"),
        ("DELL-RAC-MIB", "drsProductChassisLocation"),
        ("DELL-RAC-MIB", "drsChassisServiceTag"),
        ("DELL-RAC-MIB", "drsGlobalCurrStatus"))
)
if mibBuilder.loadTexts:
    alert2AmperageProbeNormal.setStatus(
        ""
    )

alert2PowerSupplyFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 21, 0, 2185)
)
alert2PowerSupplyFailure.setObjects(
      *(("DELL-RAC-MIB", "drsCA2MessageID"),
        ("DELL-RAC-MIB", "drsCA2Message"),
        ("DELL-RAC-MIB", "drsCA2MessageArgs"),
        ("DELL-RAC-MIB", "drsCA2AlertStatus"),
        ("DELL-RAC-MIB", "drsCA2FQDD"),
        ("DELL-RAC-MIB", "drsProductChassisName"),
        ("DELL-RAC-MIB", "drsProductChassisLocation"),
        ("DELL-RAC-MIB", "drsChassisServiceTag"),
        ("DELL-RAC-MIB", "drsGlobalCurrStatus"))
)
if mibBuilder.loadTexts:
    alert2PowerSupplyFailure.setStatus(
        ""
    )

alert2PowerSupplyWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 21, 0, 2186)
)
alert2PowerSupplyWarning.setObjects(
      *(("DELL-RAC-MIB", "drsCA2MessageID"),
        ("DELL-RAC-MIB", "drsCA2Message"),
        ("DELL-RAC-MIB", "drsCA2MessageArgs"),
        ("DELL-RAC-MIB", "drsCA2AlertStatus"),
        ("DELL-RAC-MIB", "drsCA2FQDD"),
        ("DELL-RAC-MIB", "drsProductChassisName"),
        ("DELL-RAC-MIB", "drsProductChassisLocation"),
        ("DELL-RAC-MIB", "drsChassisServiceTag"),
        ("DELL-RAC-MIB", "drsGlobalCurrStatus"))
)
if mibBuilder.loadTexts:
    alert2PowerSupplyWarning.setStatus(
        ""
    )

alert2PowerSupplyNormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 21, 0, 2187)
)
alert2PowerSupplyNormal.setObjects(
      *(("DELL-RAC-MIB", "drsCA2MessageID"),
        ("DELL-RAC-MIB", "drsCA2Message"),
        ("DELL-RAC-MIB", "drsCA2MessageArgs"),
        ("DELL-RAC-MIB", "drsCA2AlertStatus"),
        ("DELL-RAC-MIB", "drsCA2FQDD"),
        ("DELL-RAC-MIB", "drsProductChassisName"),
        ("DELL-RAC-MIB", "drsProductChassisLocation"),
        ("DELL-RAC-MIB", "drsChassisServiceTag"),
        ("DELL-RAC-MIB", "drsGlobalCurrStatus"))
)
if mibBuilder.loadTexts:
    alert2PowerSupplyNormal.setStatus(
        ""
    )

alert2BatteryFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 21, 0, 2225)
)
alert2BatteryFailure.setObjects(
      *(("DELL-RAC-MIB", "drsCA2MessageID"),
        ("DELL-RAC-MIB", "drsCA2Message"),
        ("DELL-RAC-MIB", "drsCA2MessageArgs"),
        ("DELL-RAC-MIB", "drsCA2AlertStatus"),
        ("DELL-RAC-MIB", "drsCA2FQDD"),
        ("DELL-RAC-MIB", "drsProductChassisName"),
        ("DELL-RAC-MIB", "drsProductChassisLocation"),
        ("DELL-RAC-MIB", "drsChassisServiceTag"),
        ("DELL-RAC-MIB", "drsGlobalCurrStatus"))
)
if mibBuilder.loadTexts:
    alert2BatteryFailure.setStatus(
        ""
    )

alert2BatteryWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 21, 0, 2226)
)
alert2BatteryWarning.setObjects(
      *(("DELL-RAC-MIB", "drsCA2MessageID"),
        ("DELL-RAC-MIB", "drsCA2Message"),
        ("DELL-RAC-MIB", "drsCA2MessageArgs"),
        ("DELL-RAC-MIB", "drsCA2AlertStatus"),
        ("DELL-RAC-MIB", "drsCA2FQDD"),
        ("DELL-RAC-MIB", "drsProductChassisName"),
        ("DELL-RAC-MIB", "drsProductChassisLocation"),
        ("DELL-RAC-MIB", "drsChassisServiceTag"),
        ("DELL-RAC-MIB", "drsGlobalCurrStatus"))
)
if mibBuilder.loadTexts:
    alert2BatteryWarning.setStatus(
        ""
    )

alert2BatteryNormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 21, 0, 2227)
)
alert2BatteryNormal.setObjects(
      *(("DELL-RAC-MIB", "drsCA2MessageID"),
        ("DELL-RAC-MIB", "drsCA2Message"),
        ("DELL-RAC-MIB", "drsCA2MessageArgs"),
        ("DELL-RAC-MIB", "drsCA2AlertStatus"),
        ("DELL-RAC-MIB", "drsCA2FQDD"),
        ("DELL-RAC-MIB", "drsProductChassisName"),
        ("DELL-RAC-MIB", "drsProductChassisLocation"),
        ("DELL-RAC-MIB", "drsChassisServiceTag"),
        ("DELL-RAC-MIB", "drsGlobalCurrStatus"))
)
if mibBuilder.loadTexts:
    alert2BatteryNormal.setStatus(
        ""
    )

alert2LinkStatusFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 21, 0, 2249)
)
alert2LinkStatusFailure.setObjects(
      *(("DELL-RAC-MIB", "drsCA2MessageID"),
        ("DELL-RAC-MIB", "drsCA2Message"),
        ("DELL-RAC-MIB", "drsCA2MessageArgs"),
        ("DELL-RAC-MIB", "drsCA2AlertStatus"),
        ("DELL-RAC-MIB", "drsCA2FQDD"),
        ("DELL-RAC-MIB", "drsProductChassisName"),
        ("DELL-RAC-MIB", "drsProductChassisLocation"),
        ("DELL-RAC-MIB", "drsChassisServiceTag"),
        ("DELL-RAC-MIB", "drsGlobalCurrStatus"))
)
if mibBuilder.loadTexts:
    alert2LinkStatusFailure.setStatus(
        ""
    )

alert2LinkStatusWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 21, 0, 2250)
)
alert2LinkStatusWarning.setObjects(
      *(("DELL-RAC-MIB", "drsCA2MessageID"),
        ("DELL-RAC-MIB", "drsCA2Message"),
        ("DELL-RAC-MIB", "drsCA2MessageArgs"),
        ("DELL-RAC-MIB", "drsCA2AlertStatus"),
        ("DELL-RAC-MIB", "drsCA2FQDD"),
        ("DELL-RAC-MIB", "drsProductChassisName"),
        ("DELL-RAC-MIB", "drsProductChassisLocation"),
        ("DELL-RAC-MIB", "drsChassisServiceTag"),
        ("DELL-RAC-MIB", "drsGlobalCurrStatus"))
)
if mibBuilder.loadTexts:
    alert2LinkStatusWarning.setStatus(
        ""
    )

alert2LinkStatusInformation = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 21, 0, 2251)
)
alert2LinkStatusInformation.setObjects(
      *(("DELL-RAC-MIB", "drsCA2MessageID"),
        ("DELL-RAC-MIB", "drsCA2Message"),
        ("DELL-RAC-MIB", "drsCA2MessageArgs"),
        ("DELL-RAC-MIB", "drsCA2AlertStatus"),
        ("DELL-RAC-MIB", "drsCA2FQDD"),
        ("DELL-RAC-MIB", "drsProductChassisName"),
        ("DELL-RAC-MIB", "drsProductChassisLocation"),
        ("DELL-RAC-MIB", "drsChassisServiceTag"),
        ("DELL-RAC-MIB", "drsGlobalCurrStatus"))
)
if mibBuilder.loadTexts:
    alert2LinkStatusInformation.setStatus(
        ""
    )

alert2PowerUsageFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 21, 0, 2273)
)
alert2PowerUsageFailure.setObjects(
      *(("DELL-RAC-MIB", "drsCA2MessageID"),
        ("DELL-RAC-MIB", "drsCA2Message"),
        ("DELL-RAC-MIB", "drsCA2MessageArgs"),
        ("DELL-RAC-MIB", "drsCA2AlertStatus"),
        ("DELL-RAC-MIB", "drsCA2FQDD"),
        ("DELL-RAC-MIB", "drsProductChassisName"),
        ("DELL-RAC-MIB", "drsProductChassisLocation"),
        ("DELL-RAC-MIB", "drsChassisServiceTag"),
        ("DELL-RAC-MIB", "drsGlobalCurrStatus"))
)
if mibBuilder.loadTexts:
    alert2PowerUsageFailure.setStatus(
        ""
    )

alert2PowerUsageWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 21, 0, 2274)
)
alert2PowerUsageWarning.setObjects(
      *(("DELL-RAC-MIB", "drsCA2MessageID"),
        ("DELL-RAC-MIB", "drsCA2Message"),
        ("DELL-RAC-MIB", "drsCA2MessageArgs"),
        ("DELL-RAC-MIB", "drsCA2AlertStatus"),
        ("DELL-RAC-MIB", "drsCA2FQDD"),
        ("DELL-RAC-MIB", "drsProductChassisName"),
        ("DELL-RAC-MIB", "drsProductChassisLocation"),
        ("DELL-RAC-MIB", "drsChassisServiceTag"),
        ("DELL-RAC-MIB", "drsGlobalCurrStatus"))
)
if mibBuilder.loadTexts:
    alert2PowerUsageWarning.setStatus(
        ""
    )

alert2PowerUsageInformation = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 21, 0, 2275)
)
alert2PowerUsageInformation.setObjects(
      *(("DELL-RAC-MIB", "drsCA2MessageID"),
        ("DELL-RAC-MIB", "drsCA2Message"),
        ("DELL-RAC-MIB", "drsCA2MessageArgs"),
        ("DELL-RAC-MIB", "drsCA2AlertStatus"),
        ("DELL-RAC-MIB", "drsCA2FQDD"),
        ("DELL-RAC-MIB", "drsProductChassisName"),
        ("DELL-RAC-MIB", "drsProductChassisLocation"),
        ("DELL-RAC-MIB", "drsChassisServiceTag"),
        ("DELL-RAC-MIB", "drsGlobalCurrStatus"))
)
if mibBuilder.loadTexts:
    alert2PowerUsageInformation.setStatus(
        ""
    )

alert2HardwareConfigurationFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 21, 0, 2329)
)
alert2HardwareConfigurationFailure.setObjects(
      *(("DELL-RAC-MIB", "drsCA2MessageID"),
        ("DELL-RAC-MIB", "drsCA2Message"),
        ("DELL-RAC-MIB", "drsCA2MessageArgs"),
        ("DELL-RAC-MIB", "drsCA2AlertStatus"),
        ("DELL-RAC-MIB", "drsCA2FQDD"),
        ("DELL-RAC-MIB", "drsProductChassisName"),
        ("DELL-RAC-MIB", "drsProductChassisLocation"),
        ("DELL-RAC-MIB", "drsChassisServiceTag"),
        ("DELL-RAC-MIB", "drsGlobalCurrStatus"))
)
if mibBuilder.loadTexts:
    alert2HardwareConfigurationFailure.setStatus(
        ""
    )

alert2HardwareConfigurationWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 21, 0, 2330)
)
alert2HardwareConfigurationWarning.setObjects(
      *(("DELL-RAC-MIB", "drsCA2MessageID"),
        ("DELL-RAC-MIB", "drsCA2Message"),
        ("DELL-RAC-MIB", "drsCA2MessageArgs"),
        ("DELL-RAC-MIB", "drsCA2AlertStatus"),
        ("DELL-RAC-MIB", "drsCA2FQDD"),
        ("DELL-RAC-MIB", "drsProductChassisName"),
        ("DELL-RAC-MIB", "drsProductChassisLocation"),
        ("DELL-RAC-MIB", "drsChassisServiceTag"),
        ("DELL-RAC-MIB", "drsGlobalCurrStatus"))
)
if mibBuilder.loadTexts:
    alert2HardwareConfigurationWarning.setStatus(
        ""
    )

alert2HardwareConfigurationInformation = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 21, 0, 2331)
)
alert2HardwareConfigurationInformation.setObjects(
      *(("DELL-RAC-MIB", "drsCA2MessageID"),
        ("DELL-RAC-MIB", "drsCA2Message"),
        ("DELL-RAC-MIB", "drsCA2MessageArgs"),
        ("DELL-RAC-MIB", "drsCA2AlertStatus"),
        ("DELL-RAC-MIB", "drsCA2FQDD"),
        ("DELL-RAC-MIB", "drsProductChassisName"),
        ("DELL-RAC-MIB", "drsProductChassisLocation"),
        ("DELL-RAC-MIB", "drsChassisServiceTag"),
        ("DELL-RAC-MIB", "drsGlobalCurrStatus"))
)
if mibBuilder.loadTexts:
    alert2HardwareConfigurationInformation.setStatus(
        ""
    )

alert2SoftwareConfigurationFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 21, 0, 2337)
)
alert2SoftwareConfigurationFailure.setObjects(
      *(("DELL-RAC-MIB", "drsCA2MessageID"),
        ("DELL-RAC-MIB", "drsCA2Message"),
        ("DELL-RAC-MIB", "drsCA2MessageArgs"),
        ("DELL-RAC-MIB", "drsCA2AlertStatus"),
        ("DELL-RAC-MIB", "drsCA2FQDD"),
        ("DELL-RAC-MIB", "drsProductChassisName"),
        ("DELL-RAC-MIB", "drsProductChassisLocation"),
        ("DELL-RAC-MIB", "drsChassisServiceTag"),
        ("DELL-RAC-MIB", "drsGlobalCurrStatus"))
)
if mibBuilder.loadTexts:
    alert2SoftwareConfigurationFailure.setStatus(
        ""
    )

alert2SoftwareConfigurationWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 21, 0, 2338)
)
alert2SoftwareConfigurationWarning.setObjects(
      *(("DELL-RAC-MIB", "drsCA2MessageID"),
        ("DELL-RAC-MIB", "drsCA2Message"),
        ("DELL-RAC-MIB", "drsCA2MessageArgs"),
        ("DELL-RAC-MIB", "drsCA2AlertStatus"),
        ("DELL-RAC-MIB", "drsCA2FQDD"),
        ("DELL-RAC-MIB", "drsProductChassisName"),
        ("DELL-RAC-MIB", "drsProductChassisLocation"),
        ("DELL-RAC-MIB", "drsChassisServiceTag"),
        ("DELL-RAC-MIB", "drsGlobalCurrStatus"))
)
if mibBuilder.loadTexts:
    alert2SoftwareConfigurationWarning.setStatus(
        ""
    )

alert2SoftwareConfigurationInformation = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 21, 0, 2339)
)
alert2SoftwareConfigurationInformation.setObjects(
      *(("DELL-RAC-MIB", "drsCA2MessageID"),
        ("DELL-RAC-MIB", "drsCA2Message"),
        ("DELL-RAC-MIB", "drsCA2MessageArgs"),
        ("DELL-RAC-MIB", "drsCA2AlertStatus"),
        ("DELL-RAC-MIB", "drsCA2FQDD"),
        ("DELL-RAC-MIB", "drsProductChassisName"),
        ("DELL-RAC-MIB", "drsProductChassisLocation"),
        ("DELL-RAC-MIB", "drsChassisServiceTag"),
        ("DELL-RAC-MIB", "drsGlobalCurrStatus"))
)
if mibBuilder.loadTexts:
    alert2SoftwareConfigurationInformation.setStatus(
        ""
    )

alert2SystemEventLogFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 21, 0, 2377)
)
alert2SystemEventLogFailure.setObjects(
      *(("DELL-RAC-MIB", "drsCA2MessageID"),
        ("DELL-RAC-MIB", "drsCA2Message"),
        ("DELL-RAC-MIB", "drsCA2MessageArgs"),
        ("DELL-RAC-MIB", "drsCA2AlertStatus"),
        ("DELL-RAC-MIB", "drsCA2FQDD"),
        ("DELL-RAC-MIB", "drsProductChassisName"),
        ("DELL-RAC-MIB", "drsProductChassisLocation"),
        ("DELL-RAC-MIB", "drsChassisServiceTag"),
        ("DELL-RAC-MIB", "drsGlobalCurrStatus"))
)
if mibBuilder.loadTexts:
    alert2SystemEventLogFailure.setStatus(
        ""
    )

alert2SystemEventLogWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 21, 0, 2378)
)
alert2SystemEventLogWarning.setObjects(
      *(("DELL-RAC-MIB", "drsCA2MessageID"),
        ("DELL-RAC-MIB", "drsCA2Message"),
        ("DELL-RAC-MIB", "drsCA2MessageArgs"),
        ("DELL-RAC-MIB", "drsCA2AlertStatus"),
        ("DELL-RAC-MIB", "drsCA2FQDD"),
        ("DELL-RAC-MIB", "drsProductChassisName"),
        ("DELL-RAC-MIB", "drsProductChassisLocation"),
        ("DELL-RAC-MIB", "drsChassisServiceTag"),
        ("DELL-RAC-MIB", "drsGlobalCurrStatus"))
)
if mibBuilder.loadTexts:
    alert2SystemEventLogWarning.setStatus(
        ""
    )

alert2SystemEventLogInformation = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 21, 0, 2379)
)
alert2SystemEventLogInformation.setObjects(
      *(("DELL-RAC-MIB", "drsCA2MessageID"),
        ("DELL-RAC-MIB", "drsCA2Message"),
        ("DELL-RAC-MIB", "drsCA2MessageArgs"),
        ("DELL-RAC-MIB", "drsCA2AlertStatus"),
        ("DELL-RAC-MIB", "drsCA2FQDD"),
        ("DELL-RAC-MIB", "drsProductChassisName"),
        ("DELL-RAC-MIB", "drsProductChassisLocation"),
        ("DELL-RAC-MIB", "drsChassisServiceTag"),
        ("DELL-RAC-MIB", "drsGlobalCurrStatus"))
)
if mibBuilder.loadTexts:
    alert2SystemEventLogInformation.setStatus(
        ""
    )

alert2SecurityFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 21, 0, 2385)
)
alert2SecurityFailure.setObjects(
      *(("DELL-RAC-MIB", "drsCA2MessageID"),
        ("DELL-RAC-MIB", "drsCA2Message"),
        ("DELL-RAC-MIB", "drsCA2MessageArgs"),
        ("DELL-RAC-MIB", "drsCA2AlertStatus"),
        ("DELL-RAC-MIB", "drsCA2FQDD"),
        ("DELL-RAC-MIB", "drsProductChassisName"),
        ("DELL-RAC-MIB", "drsProductChassisLocation"),
        ("DELL-RAC-MIB", "drsChassisServiceTag"),
        ("DELL-RAC-MIB", "drsGlobalCurrStatus"))
)
if mibBuilder.loadTexts:
    alert2SecurityFailure.setStatus(
        ""
    )

alert2SecurityWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 21, 0, 2386)
)
alert2SecurityWarning.setObjects(
      *(("DELL-RAC-MIB", "drsCA2MessageID"),
        ("DELL-RAC-MIB", "drsCA2Message"),
        ("DELL-RAC-MIB", "drsCA2MessageArgs"),
        ("DELL-RAC-MIB", "drsCA2AlertStatus"),
        ("DELL-RAC-MIB", "drsCA2FQDD"),
        ("DELL-RAC-MIB", "drsProductChassisName"),
        ("DELL-RAC-MIB", "drsProductChassisLocation"),
        ("DELL-RAC-MIB", "drsChassisServiceTag"),
        ("DELL-RAC-MIB", "drsGlobalCurrStatus"))
)
if mibBuilder.loadTexts:
    alert2SecurityWarning.setStatus(
        ""
    )

alert2SecurityInformation = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 21, 0, 2387)
)
alert2SecurityInformation.setObjects(
      *(("DELL-RAC-MIB", "drsCA2MessageID"),
        ("DELL-RAC-MIB", "drsCA2Message"),
        ("DELL-RAC-MIB", "drsCA2MessageArgs"),
        ("DELL-RAC-MIB", "drsCA2AlertStatus"),
        ("DELL-RAC-MIB", "drsCA2FQDD"),
        ("DELL-RAC-MIB", "drsProductChassisName"),
        ("DELL-RAC-MIB", "drsProductChassisLocation"),
        ("DELL-RAC-MIB", "drsChassisServiceTag"),
        ("DELL-RAC-MIB", "drsGlobalCurrStatus"))
)
if mibBuilder.loadTexts:
    alert2SecurityInformation.setStatus(
        ""
    )

alert2CableFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 21, 0, 2393)
)
alert2CableFailure.setObjects(
      *(("DELL-RAC-MIB", "drsCA2MessageID"),
        ("DELL-RAC-MIB", "drsCA2Message"),
        ("DELL-RAC-MIB", "drsCA2MessageArgs"),
        ("DELL-RAC-MIB", "drsCA2AlertStatus"),
        ("DELL-RAC-MIB", "drsCA2FQDD"),
        ("DELL-RAC-MIB", "drsProductChassisName"),
        ("DELL-RAC-MIB", "drsProductChassisLocation"),
        ("DELL-RAC-MIB", "drsChassisServiceTag"),
        ("DELL-RAC-MIB", "drsGlobalCurrStatus"))
)
if mibBuilder.loadTexts:
    alert2CableFailure.setStatus(
        ""
    )

alert2PCIDeviceFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 21, 0, 2417)
)
alert2PCIDeviceFailure.setObjects(
      *(("DELL-RAC-MIB", "drsCA2MessageID"),
        ("DELL-RAC-MIB", "drsCA2Message"),
        ("DELL-RAC-MIB", "drsCA2MessageArgs"),
        ("DELL-RAC-MIB", "drsCA2AlertStatus"),
        ("DELL-RAC-MIB", "drsCA2FQDD"),
        ("DELL-RAC-MIB", "drsProductChassisName"),
        ("DELL-RAC-MIB", "drsProductChassisLocation"),
        ("DELL-RAC-MIB", "drsChassisServiceTag"),
        ("DELL-RAC-MIB", "drsGlobalCurrStatus"))
)
if mibBuilder.loadTexts:
    alert2PCIDeviceFailure.setStatus(
        ""
    )

alert2PCIDeviceWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 21, 0, 2418)
)
alert2PCIDeviceWarning.setObjects(
      *(("DELL-RAC-MIB", "drsCA2MessageID"),
        ("DELL-RAC-MIB", "drsCA2Message"),
        ("DELL-RAC-MIB", "drsCA2MessageArgs"),
        ("DELL-RAC-MIB", "drsCA2AlertStatus"),
        ("DELL-RAC-MIB", "drsCA2FQDD"),
        ("DELL-RAC-MIB", "drsProductChassisName"),
        ("DELL-RAC-MIB", "drsProductChassisLocation"),
        ("DELL-RAC-MIB", "drsChassisServiceTag"),
        ("DELL-RAC-MIB", "drsGlobalCurrStatus"))
)
if mibBuilder.loadTexts:
    alert2PCIDeviceWarning.setStatus(
        ""
    )

alert2PCIDeviceInformation = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 21, 0, 2419)
)
alert2PCIDeviceInformation.setObjects(
      *(("DELL-RAC-MIB", "drsCA2MessageID"),
        ("DELL-RAC-MIB", "drsCA2Message"),
        ("DELL-RAC-MIB", "drsCA2MessageArgs"),
        ("DELL-RAC-MIB", "drsCA2AlertStatus"),
        ("DELL-RAC-MIB", "drsCA2FQDD"),
        ("DELL-RAC-MIB", "drsProductChassisName"),
        ("DELL-RAC-MIB", "drsProductChassisLocation"),
        ("DELL-RAC-MIB", "drsChassisServiceTag"),
        ("DELL-RAC-MIB", "drsGlobalCurrStatus"))
)
if mibBuilder.loadTexts:
    alert2PCIDeviceInformation.setStatus(
        ""
    )

alert2PowerSupplyAbsent = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 21, 0, 2465)
)
alert2PowerSupplyAbsent.setObjects(
      *(("DELL-RAC-MIB", "drsCA2MessageID"),
        ("DELL-RAC-MIB", "drsCA2Message"),
        ("DELL-RAC-MIB", "drsCA2MessageArgs"),
        ("DELL-RAC-MIB", "drsCA2AlertStatus"),
        ("DELL-RAC-MIB", "drsCA2FQDD"),
        ("DELL-RAC-MIB", "drsProductChassisName"),
        ("DELL-RAC-MIB", "drsProductChassisLocation"),
        ("DELL-RAC-MIB", "drsChassisServiceTag"),
        ("DELL-RAC-MIB", "drsGlobalCurrStatus"))
)
if mibBuilder.loadTexts:
    alert2PowerSupplyAbsent.setStatus(
        ""
    )

alert2RedundancyLost = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 21, 0, 2473)
)
alert2RedundancyLost.setObjects(
      *(("DELL-RAC-MIB", "drsCA2MessageID"),
        ("DELL-RAC-MIB", "drsCA2Message"),
        ("DELL-RAC-MIB", "drsCA2MessageArgs"),
        ("DELL-RAC-MIB", "drsCA2AlertStatus"),
        ("DELL-RAC-MIB", "drsCA2FQDD"),
        ("DELL-RAC-MIB", "drsProductChassisName"),
        ("DELL-RAC-MIB", "drsProductChassisLocation"),
        ("DELL-RAC-MIB", "drsChassisServiceTag"),
        ("DELL-RAC-MIB", "drsGlobalCurrStatus"))
)
if mibBuilder.loadTexts:
    alert2RedundancyLost.setStatus(
        ""
    )

alert2RedundancyDegraded = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 21, 0, 2474)
)
alert2RedundancyDegraded.setObjects(
      *(("DELL-RAC-MIB", "drsCA2MessageID"),
        ("DELL-RAC-MIB", "drsCA2Message"),
        ("DELL-RAC-MIB", "drsCA2MessageArgs"),
        ("DELL-RAC-MIB", "drsCA2AlertStatus"),
        ("DELL-RAC-MIB", "drsCA2FQDD"),
        ("DELL-RAC-MIB", "drsProductChassisName"),
        ("DELL-RAC-MIB", "drsProductChassisLocation"),
        ("DELL-RAC-MIB", "drsChassisServiceTag"),
        ("DELL-RAC-MIB", "drsGlobalCurrStatus"))
)
if mibBuilder.loadTexts:
    alert2RedundancyDegraded.setStatus(
        ""
    )

alert2RedundancyInformation = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 21, 0, 2475)
)
alert2RedundancyInformation.setObjects(
      *(("DELL-RAC-MIB", "drsCA2MessageID"),
        ("DELL-RAC-MIB", "drsCA2Message"),
        ("DELL-RAC-MIB", "drsCA2MessageArgs"),
        ("DELL-RAC-MIB", "drsCA2AlertStatus"),
        ("DELL-RAC-MIB", "drsCA2FQDD"),
        ("DELL-RAC-MIB", "drsProductChassisName"),
        ("DELL-RAC-MIB", "drsProductChassisLocation"),
        ("DELL-RAC-MIB", "drsChassisServiceTag"),
        ("DELL-RAC-MIB", "drsGlobalCurrStatus"))
)
if mibBuilder.loadTexts:
    alert2RedundancyInformation.setStatus(
        ""
    )

alert2CMCFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 21, 0, 2545)
)
alert2CMCFailure.setObjects(
      *(("DELL-RAC-MIB", "drsCA2MessageID"),
        ("DELL-RAC-MIB", "drsCA2Message"),
        ("DELL-RAC-MIB", "drsCA2MessageArgs"),
        ("DELL-RAC-MIB", "drsCA2AlertStatus"),
        ("DELL-RAC-MIB", "drsCA2FQDD"),
        ("DELL-RAC-MIB", "drsProductChassisName"),
        ("DELL-RAC-MIB", "drsProductChassisLocation"),
        ("DELL-RAC-MIB", "drsChassisServiceTag"),
        ("DELL-RAC-MIB", "drsGlobalCurrStatus"))
)
if mibBuilder.loadTexts:
    alert2CMCFailure.setStatus(
        ""
    )

alert2CMCWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 21, 0, 2546)
)
alert2CMCWarning.setObjects(
      *(("DELL-RAC-MIB", "drsCA2MessageID"),
        ("DELL-RAC-MIB", "drsCA2Message"),
        ("DELL-RAC-MIB", "drsCA2MessageArgs"),
        ("DELL-RAC-MIB", "drsCA2AlertStatus"),
        ("DELL-RAC-MIB", "drsCA2FQDD"),
        ("DELL-RAC-MIB", "drsProductChassisName"),
        ("DELL-RAC-MIB", "drsProductChassisLocation"),
        ("DELL-RAC-MIB", "drsChassisServiceTag"),
        ("DELL-RAC-MIB", "drsGlobalCurrStatus"))
)
if mibBuilder.loadTexts:
    alert2CMCWarning.setStatus(
        ""
    )

alert2IOVirtualizationFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 21, 0, 2553)
)
alert2IOVirtualizationFailure.setObjects(
      *(("DELL-RAC-MIB", "drsCA2MessageID"),
        ("DELL-RAC-MIB", "drsCA2Message"),
        ("DELL-RAC-MIB", "drsCA2MessageArgs"),
        ("DELL-RAC-MIB", "drsCA2AlertStatus"),
        ("DELL-RAC-MIB", "drsCA2FQDD"),
        ("DELL-RAC-MIB", "drsProductChassisName"),
        ("DELL-RAC-MIB", "drsProductChassisLocation"),
        ("DELL-RAC-MIB", "drsChassisServiceTag"),
        ("DELL-RAC-MIB", "drsGlobalCurrStatus"))
)
if mibBuilder.loadTexts:
    alert2IOVirtualizationFailure.setStatus(
        ""
    )

alert2IOVirtualizationWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 21, 0, 2554)
)
alert2IOVirtualizationWarning.setObjects(
      *(("DELL-RAC-MIB", "drsCA2MessageID"),
        ("DELL-RAC-MIB", "drsCA2Message"),
        ("DELL-RAC-MIB", "drsCA2MessageArgs"),
        ("DELL-RAC-MIB", "drsCA2AlertStatus"),
        ("DELL-RAC-MIB", "drsCA2FQDD"),
        ("DELL-RAC-MIB", "drsProductChassisName"),
        ("DELL-RAC-MIB", "drsProductChassisLocation"),
        ("DELL-RAC-MIB", "drsChassisServiceTag"),
        ("DELL-RAC-MIB", "drsGlobalCurrStatus"))
)
if mibBuilder.loadTexts:
    alert2IOVirtualizationWarning.setStatus(
        ""
    )

alert2IOVirtualizationInformation = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 21, 0, 2555)
)
alert2IOVirtualizationInformation.setObjects(
      *(("DELL-RAC-MIB", "drsCA2MessageID"),
        ("DELL-RAC-MIB", "drsCA2Message"),
        ("DELL-RAC-MIB", "drsCA2MessageArgs"),
        ("DELL-RAC-MIB", "drsCA2AlertStatus"),
        ("DELL-RAC-MIB", "drsCA2FQDD"),
        ("DELL-RAC-MIB", "drsProductChassisName"),
        ("DELL-RAC-MIB", "drsProductChassisLocation"),
        ("DELL-RAC-MIB", "drsChassisServiceTag"),
        ("DELL-RAC-MIB", "drsGlobalCurrStatus"))
)
if mibBuilder.loadTexts:
    alert2IOVirtualizationInformation.setStatus(
        ""
    )

alert2StorageManagementFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 21, 0, 4177)
)
alert2StorageManagementFailure.setObjects(
      *(("DELL-RAC-MIB", "drsCA2MessageID"),
        ("DELL-RAC-MIB", "drsCA2Message"),
        ("DELL-RAC-MIB", "drsCA2MessageArgs"),
        ("DELL-RAC-MIB", "drsCA2AlertStatus"),
        ("DELL-RAC-MIB", "drsCA2FQDD"),
        ("DELL-RAC-MIB", "drsProductChassisName"),
        ("DELL-RAC-MIB", "drsProductChassisLocation"),
        ("DELL-RAC-MIB", "drsChassisServiceTag"),
        ("DELL-RAC-MIB", "drsGlobalCurrStatus"))
)
if mibBuilder.loadTexts:
    alert2StorageManagementFailure.setStatus(
        ""
    )

alert2StorageManagementWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 21, 0, 4178)
)
alert2StorageManagementWarning.setObjects(
      *(("DELL-RAC-MIB", "drsCA2MessageID"),
        ("DELL-RAC-MIB", "drsCA2Message"),
        ("DELL-RAC-MIB", "drsCA2MessageArgs"),
        ("DELL-RAC-MIB", "drsCA2AlertStatus"),
        ("DELL-RAC-MIB", "drsCA2FQDD"),
        ("DELL-RAC-MIB", "drsProductChassisName"),
        ("DELL-RAC-MIB", "drsProductChassisLocation"),
        ("DELL-RAC-MIB", "drsChassisServiceTag"),
        ("DELL-RAC-MIB", "drsGlobalCurrStatus"))
)
if mibBuilder.loadTexts:
    alert2StorageManagementWarning.setStatus(
        ""
    )

alert2StorageManagementInformation = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 21, 0, 4179)
)
alert2StorageManagementInformation.setObjects(
      *(("DELL-RAC-MIB", "drsCA2MessageID"),
        ("DELL-RAC-MIB", "drsCA2Message"),
        ("DELL-RAC-MIB", "drsCA2MessageArgs"),
        ("DELL-RAC-MIB", "drsCA2AlertStatus"),
        ("DELL-RAC-MIB", "drsCA2FQDD"),
        ("DELL-RAC-MIB", "drsProductChassisName"),
        ("DELL-RAC-MIB", "drsProductChassisLocation"),
        ("DELL-RAC-MIB", "drsChassisServiceTag"),
        ("DELL-RAC-MIB", "drsGlobalCurrStatus"))
)
if mibBuilder.loadTexts:
    alert2StorageManagementInformation.setStatus(
        ""
    )

alert2StorageFanFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 21, 0, 4201)
)
alert2StorageFanFailure.setObjects(
      *(("DELL-RAC-MIB", "drsCA2MessageID"),
        ("DELL-RAC-MIB", "drsCA2Message"),
        ("DELL-RAC-MIB", "drsCA2MessageArgs"),
        ("DELL-RAC-MIB", "drsCA2AlertStatus"),
        ("DELL-RAC-MIB", "drsCA2FQDD"),
        ("DELL-RAC-MIB", "drsProductChassisName"),
        ("DELL-RAC-MIB", "drsProductChassisLocation"),
        ("DELL-RAC-MIB", "drsChassisServiceTag"),
        ("DELL-RAC-MIB", "drsGlobalCurrStatus"))
)
if mibBuilder.loadTexts:
    alert2StorageFanFailure.setStatus(
        ""
    )

alert2StorageFanWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 21, 0, 4202)
)
alert2StorageFanWarning.setObjects(
      *(("DELL-RAC-MIB", "drsCA2MessageID"),
        ("DELL-RAC-MIB", "drsCA2Message"),
        ("DELL-RAC-MIB", "drsCA2MessageArgs"),
        ("DELL-RAC-MIB", "drsCA2AlertStatus"),
        ("DELL-RAC-MIB", "drsCA2FQDD"),
        ("DELL-RAC-MIB", "drsProductChassisName"),
        ("DELL-RAC-MIB", "drsProductChassisLocation"),
        ("DELL-RAC-MIB", "drsChassisServiceTag"),
        ("DELL-RAC-MIB", "drsGlobalCurrStatus"))
)
if mibBuilder.loadTexts:
    alert2StorageFanWarning.setStatus(
        ""
    )

alert2StorageFanInformation = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 21, 0, 4203)
)
alert2StorageFanInformation.setObjects(
      *(("DELL-RAC-MIB", "drsCA2MessageID"),
        ("DELL-RAC-MIB", "drsCA2Message"),
        ("DELL-RAC-MIB", "drsCA2MessageArgs"),
        ("DELL-RAC-MIB", "drsCA2AlertStatus"),
        ("DELL-RAC-MIB", "drsCA2FQDD"),
        ("DELL-RAC-MIB", "drsProductChassisName"),
        ("DELL-RAC-MIB", "drsProductChassisLocation"),
        ("DELL-RAC-MIB", "drsChassisServiceTag"),
        ("DELL-RAC-MIB", "drsGlobalCurrStatus"))
)
if mibBuilder.loadTexts:
    alert2StorageFanInformation.setStatus(
        ""
    )

alert2StorageTemperatureProbeFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 21, 0, 4209)
)
alert2StorageTemperatureProbeFailure.setObjects(
      *(("DELL-RAC-MIB", "drsCA2MessageID"),
        ("DELL-RAC-MIB", "drsCA2Message"),
        ("DELL-RAC-MIB", "drsCA2MessageArgs"),
        ("DELL-RAC-MIB", "drsCA2AlertStatus"),
        ("DELL-RAC-MIB", "drsCA2FQDD"),
        ("DELL-RAC-MIB", "drsProductChassisName"),
        ("DELL-RAC-MIB", "drsProductChassisLocation"),
        ("DELL-RAC-MIB", "drsChassisServiceTag"),
        ("DELL-RAC-MIB", "drsGlobalCurrStatus"))
)
if mibBuilder.loadTexts:
    alert2StorageTemperatureProbeFailure.setStatus(
        ""
    )

alert2StorageTemperatureProbeWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 21, 0, 4210)
)
alert2StorageTemperatureProbeWarning.setObjects(
      *(("DELL-RAC-MIB", "drsCA2MessageID"),
        ("DELL-RAC-MIB", "drsCA2Message"),
        ("DELL-RAC-MIB", "drsCA2MessageArgs"),
        ("DELL-RAC-MIB", "drsCA2AlertStatus"),
        ("DELL-RAC-MIB", "drsCA2FQDD"),
        ("DELL-RAC-MIB", "drsProductChassisName"),
        ("DELL-RAC-MIB", "drsProductChassisLocation"),
        ("DELL-RAC-MIB", "drsChassisServiceTag"),
        ("DELL-RAC-MIB", "drsGlobalCurrStatus"))
)
if mibBuilder.loadTexts:
    alert2StorageTemperatureProbeWarning.setStatus(
        ""
    )

alert2StorageTemperatureProbeInformation = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 21, 0, 4211)
)
alert2StorageTemperatureProbeInformation.setObjects(
      *(("DELL-RAC-MIB", "drsCA2MessageID"),
        ("DELL-RAC-MIB", "drsCA2Message"),
        ("DELL-RAC-MIB", "drsCA2MessageArgs"),
        ("DELL-RAC-MIB", "drsCA2AlertStatus"),
        ("DELL-RAC-MIB", "drsCA2FQDD"),
        ("DELL-RAC-MIB", "drsProductChassisName"),
        ("DELL-RAC-MIB", "drsProductChassisLocation"),
        ("DELL-RAC-MIB", "drsChassisServiceTag"),
        ("DELL-RAC-MIB", "drsGlobalCurrStatus"))
)
if mibBuilder.loadTexts:
    alert2StorageTemperatureProbeInformation.setStatus(
        ""
    )

alert2StoragePowerSupplyFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 21, 0, 4233)
)
alert2StoragePowerSupplyFailure.setObjects(
      *(("DELL-RAC-MIB", "drsCA2MessageID"),
        ("DELL-RAC-MIB", "drsCA2Message"),
        ("DELL-RAC-MIB", "drsCA2MessageArgs"),
        ("DELL-RAC-MIB", "drsCA2AlertStatus"),
        ("DELL-RAC-MIB", "drsCA2FQDD"),
        ("DELL-RAC-MIB", "drsProductChassisName"),
        ("DELL-RAC-MIB", "drsProductChassisLocation"),
        ("DELL-RAC-MIB", "drsChassisServiceTag"),
        ("DELL-RAC-MIB", "drsGlobalCurrStatus"))
)
if mibBuilder.loadTexts:
    alert2StoragePowerSupplyFailure.setStatus(
        ""
    )

alert2StoragePowerSupplyWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 21, 0, 4234)
)
alert2StoragePowerSupplyWarning.setObjects(
      *(("DELL-RAC-MIB", "drsCA2MessageID"),
        ("DELL-RAC-MIB", "drsCA2Message"),
        ("DELL-RAC-MIB", "drsCA2MessageArgs"),
        ("DELL-RAC-MIB", "drsCA2AlertStatus"),
        ("DELL-RAC-MIB", "drsCA2FQDD"),
        ("DELL-RAC-MIB", "drsProductChassisName"),
        ("DELL-RAC-MIB", "drsProductChassisLocation"),
        ("DELL-RAC-MIB", "drsChassisServiceTag"),
        ("DELL-RAC-MIB", "drsGlobalCurrStatus"))
)
if mibBuilder.loadTexts:
    alert2StoragePowerSupplyWarning.setStatus(
        ""
    )

alert2StoragePowerSupplyInformation = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 21, 0, 4235)
)
alert2StoragePowerSupplyInformation.setObjects(
      *(("DELL-RAC-MIB", "drsCA2MessageID"),
        ("DELL-RAC-MIB", "drsCA2Message"),
        ("DELL-RAC-MIB", "drsCA2MessageArgs"),
        ("DELL-RAC-MIB", "drsCA2AlertStatus"),
        ("DELL-RAC-MIB", "drsCA2FQDD"),
        ("DELL-RAC-MIB", "drsProductChassisName"),
        ("DELL-RAC-MIB", "drsProductChassisLocation"),
        ("DELL-RAC-MIB", "drsChassisServiceTag"),
        ("DELL-RAC-MIB", "drsGlobalCurrStatus"))
)
if mibBuilder.loadTexts:
    alert2StoragePowerSupplyInformation.setStatus(
        ""
    )

alert2StorageBatteryFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 21, 0, 4273)
)
alert2StorageBatteryFailure.setObjects(
      *(("DELL-RAC-MIB", "drsCA2MessageID"),
        ("DELL-RAC-MIB", "drsCA2Message"),
        ("DELL-RAC-MIB", "drsCA2MessageArgs"),
        ("DELL-RAC-MIB", "drsCA2AlertStatus"),
        ("DELL-RAC-MIB", "drsCA2FQDD"),
        ("DELL-RAC-MIB", "drsProductChassisName"),
        ("DELL-RAC-MIB", "drsProductChassisLocation"),
        ("DELL-RAC-MIB", "drsChassisServiceTag"),
        ("DELL-RAC-MIB", "drsGlobalCurrStatus"))
)
if mibBuilder.loadTexts:
    alert2StorageBatteryFailure.setStatus(
        ""
    )

alert2StorageBatteryWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 21, 0, 4274)
)
alert2StorageBatteryWarning.setObjects(
      *(("DELL-RAC-MIB", "drsCA2MessageID"),
        ("DELL-RAC-MIB", "drsCA2Message"),
        ("DELL-RAC-MIB", "drsCA2MessageArgs"),
        ("DELL-RAC-MIB", "drsCA2AlertStatus"),
        ("DELL-RAC-MIB", "drsCA2FQDD"),
        ("DELL-RAC-MIB", "drsProductChassisName"),
        ("DELL-RAC-MIB", "drsProductChassisLocation"),
        ("DELL-RAC-MIB", "drsChassisServiceTag"),
        ("DELL-RAC-MIB", "drsGlobalCurrStatus"))
)
if mibBuilder.loadTexts:
    alert2StorageBatteryWarning.setStatus(
        ""
    )

alert2StorageBatteryInformation = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 21, 0, 4275)
)
alert2StorageBatteryInformation.setObjects(
      *(("DELL-RAC-MIB", "drsCA2MessageID"),
        ("DELL-RAC-MIB", "drsCA2Message"),
        ("DELL-RAC-MIB", "drsCA2MessageArgs"),
        ("DELL-RAC-MIB", "drsCA2AlertStatus"),
        ("DELL-RAC-MIB", "drsCA2FQDD"),
        ("DELL-RAC-MIB", "drsProductChassisName"),
        ("DELL-RAC-MIB", "drsProductChassisLocation"),
        ("DELL-RAC-MIB", "drsChassisServiceTag"),
        ("DELL-RAC-MIB", "drsGlobalCurrStatus"))
)
if mibBuilder.loadTexts:
    alert2StorageBatteryInformation.setStatus(
        ""
    )

alert2StorageControllerFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 21, 0, 4329)
)
alert2StorageControllerFailure.setObjects(
      *(("DELL-RAC-MIB", "drsCA2MessageID"),
        ("DELL-RAC-MIB", "drsCA2Message"),
        ("DELL-RAC-MIB", "drsCA2MessageArgs"),
        ("DELL-RAC-MIB", "drsCA2AlertStatus"),
        ("DELL-RAC-MIB", "drsCA2FQDD"),
        ("DELL-RAC-MIB", "drsProductChassisName"),
        ("DELL-RAC-MIB", "drsProductChassisLocation"),
        ("DELL-RAC-MIB", "drsChassisServiceTag"),
        ("DELL-RAC-MIB", "drsGlobalCurrStatus"))
)
if mibBuilder.loadTexts:
    alert2StorageControllerFailure.setStatus(
        ""
    )

alert2StorageControllerWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 21, 0, 4330)
)
alert2StorageControllerWarning.setObjects(
      *(("DELL-RAC-MIB", "drsCA2MessageID"),
        ("DELL-RAC-MIB", "drsCA2Message"),
        ("DELL-RAC-MIB", "drsCA2MessageArgs"),
        ("DELL-RAC-MIB", "drsCA2AlertStatus"),
        ("DELL-RAC-MIB", "drsCA2FQDD"),
        ("DELL-RAC-MIB", "drsProductChassisName"),
        ("DELL-RAC-MIB", "drsProductChassisLocation"),
        ("DELL-RAC-MIB", "drsChassisServiceTag"),
        ("DELL-RAC-MIB", "drsGlobalCurrStatus"))
)
if mibBuilder.loadTexts:
    alert2StorageControllerWarning.setStatus(
        ""
    )

alert2StorageControllerInformation = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 21, 0, 4331)
)
alert2StorageControllerInformation.setObjects(
      *(("DELL-RAC-MIB", "drsCA2MessageID"),
        ("DELL-RAC-MIB", "drsCA2Message"),
        ("DELL-RAC-MIB", "drsCA2MessageArgs"),
        ("DELL-RAC-MIB", "drsCA2AlertStatus"),
        ("DELL-RAC-MIB", "drsCA2FQDD"),
        ("DELL-RAC-MIB", "drsProductChassisName"),
        ("DELL-RAC-MIB", "drsProductChassisLocation"),
        ("DELL-RAC-MIB", "drsChassisServiceTag"),
        ("DELL-RAC-MIB", "drsGlobalCurrStatus"))
)
if mibBuilder.loadTexts:
    alert2StorageControllerInformation.setStatus(
        ""
    )

alert2StorageEnclosureFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 21, 0, 4337)
)
alert2StorageEnclosureFailure.setObjects(
      *(("DELL-RAC-MIB", "drsCA2MessageID"),
        ("DELL-RAC-MIB", "drsCA2Message"),
        ("DELL-RAC-MIB", "drsCA2MessageArgs"),
        ("DELL-RAC-MIB", "drsCA2AlertStatus"),
        ("DELL-RAC-MIB", "drsCA2FQDD"),
        ("DELL-RAC-MIB", "drsProductChassisName"),
        ("DELL-RAC-MIB", "drsProductChassisLocation"),
        ("DELL-RAC-MIB", "drsChassisServiceTag"),
        ("DELL-RAC-MIB", "drsGlobalCurrStatus"))
)
if mibBuilder.loadTexts:
    alert2StorageEnclosureFailure.setStatus(
        ""
    )

alert2StorageEnclosureWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 21, 0, 4338)
)
alert2StorageEnclosureWarning.setObjects(
      *(("DELL-RAC-MIB", "drsCA2MessageID"),
        ("DELL-RAC-MIB", "drsCA2Message"),
        ("DELL-RAC-MIB", "drsCA2MessageArgs"),
        ("DELL-RAC-MIB", "drsCA2AlertStatus"),
        ("DELL-RAC-MIB", "drsCA2FQDD"),
        ("DELL-RAC-MIB", "drsProductChassisName"),
        ("DELL-RAC-MIB", "drsProductChassisLocation"),
        ("DELL-RAC-MIB", "drsChassisServiceTag"),
        ("DELL-RAC-MIB", "drsGlobalCurrStatus"))
)
if mibBuilder.loadTexts:
    alert2StorageEnclosureWarning.setStatus(
        ""
    )

alert2StorageEnclosureInformation = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 21, 0, 4339)
)
alert2StorageEnclosureInformation.setObjects(
      *(("DELL-RAC-MIB", "drsCA2MessageID"),
        ("DELL-RAC-MIB", "drsCA2Message"),
        ("DELL-RAC-MIB", "drsCA2MessageArgs"),
        ("DELL-RAC-MIB", "drsCA2AlertStatus"),
        ("DELL-RAC-MIB", "drsCA2FQDD"),
        ("DELL-RAC-MIB", "drsProductChassisName"),
        ("DELL-RAC-MIB", "drsProductChassisLocation"),
        ("DELL-RAC-MIB", "drsChassisServiceTag"),
        ("DELL-RAC-MIB", "drsGlobalCurrStatus"))
)
if mibBuilder.loadTexts:
    alert2StorageEnclosureInformation.setStatus(
        ""
    )

alert2StoragePhysicalDiskFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 21, 0, 4345)
)
alert2StoragePhysicalDiskFailure.setObjects(
      *(("DELL-RAC-MIB", "drsCA2MessageID"),
        ("DELL-RAC-MIB", "drsCA2Message"),
        ("DELL-RAC-MIB", "drsCA2MessageArgs"),
        ("DELL-RAC-MIB", "drsCA2AlertStatus"),
        ("DELL-RAC-MIB", "drsCA2FQDD"),
        ("DELL-RAC-MIB", "drsProductChassisName"),
        ("DELL-RAC-MIB", "drsProductChassisLocation"),
        ("DELL-RAC-MIB", "drsChassisServiceTag"),
        ("DELL-RAC-MIB", "drsGlobalCurrStatus"))
)
if mibBuilder.loadTexts:
    alert2StoragePhysicalDiskFailure.setStatus(
        ""
    )

alert2StoragePhysicalDiskWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 21, 0, 4346)
)
alert2StoragePhysicalDiskWarning.setObjects(
      *(("DELL-RAC-MIB", "drsCA2MessageID"),
        ("DELL-RAC-MIB", "drsCA2Message"),
        ("DELL-RAC-MIB", "drsCA2MessageArgs"),
        ("DELL-RAC-MIB", "drsCA2AlertStatus"),
        ("DELL-RAC-MIB", "drsCA2FQDD"),
        ("DELL-RAC-MIB", "drsProductChassisName"),
        ("DELL-RAC-MIB", "drsProductChassisLocation"),
        ("DELL-RAC-MIB", "drsChassisServiceTag"),
        ("DELL-RAC-MIB", "drsGlobalCurrStatus"))
)
if mibBuilder.loadTexts:
    alert2StoragePhysicalDiskWarning.setStatus(
        ""
    )

alert2StoragePhysicalDiskInformation = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 21, 0, 4347)
)
alert2StoragePhysicalDiskInformation.setObjects(
      *(("DELL-RAC-MIB", "drsCA2MessageID"),
        ("DELL-RAC-MIB", "drsCA2Message"),
        ("DELL-RAC-MIB", "drsCA2MessageArgs"),
        ("DELL-RAC-MIB", "drsCA2AlertStatus"),
        ("DELL-RAC-MIB", "drsCA2FQDD"),
        ("DELL-RAC-MIB", "drsProductChassisName"),
        ("DELL-RAC-MIB", "drsProductChassisLocation"),
        ("DELL-RAC-MIB", "drsChassisServiceTag"),
        ("DELL-RAC-MIB", "drsGlobalCurrStatus"))
)
if mibBuilder.loadTexts:
    alert2StoragePhysicalDiskInformation.setStatus(
        ""
    )

alert2StorageVirtualDiskFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 21, 0, 4353)
)
alert2StorageVirtualDiskFailure.setObjects(
      *(("DELL-RAC-MIB", "drsCA2MessageID"),
        ("DELL-RAC-MIB", "drsCA2Message"),
        ("DELL-RAC-MIB", "drsCA2MessageArgs"),
        ("DELL-RAC-MIB", "drsCA2AlertStatus"),
        ("DELL-RAC-MIB", "drsCA2FQDD"),
        ("DELL-RAC-MIB", "drsProductChassisName"),
        ("DELL-RAC-MIB", "drsProductChassisLocation"),
        ("DELL-RAC-MIB", "drsChassisServiceTag"),
        ("DELL-RAC-MIB", "drsGlobalCurrStatus"))
)
if mibBuilder.loadTexts:
    alert2StorageVirtualDiskFailure.setStatus(
        ""
    )

alert2StorageVirtualDiskWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 21, 0, 4354)
)
alert2StorageVirtualDiskWarning.setObjects(
      *(("DELL-RAC-MIB", "drsCA2MessageID"),
        ("DELL-RAC-MIB", "drsCA2Message"),
        ("DELL-RAC-MIB", "drsCA2MessageArgs"),
        ("DELL-RAC-MIB", "drsCA2AlertStatus"),
        ("DELL-RAC-MIB", "drsCA2FQDD"),
        ("DELL-RAC-MIB", "drsProductChassisName"),
        ("DELL-RAC-MIB", "drsProductChassisLocation"),
        ("DELL-RAC-MIB", "drsChassisServiceTag"),
        ("DELL-RAC-MIB", "drsGlobalCurrStatus"))
)
if mibBuilder.loadTexts:
    alert2StorageVirtualDiskWarning.setStatus(
        ""
    )

alert2StorageVirtualDiskInformation = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 21, 0, 4355)
)
alert2StorageVirtualDiskInformation.setObjects(
      *(("DELL-RAC-MIB", "drsCA2MessageID"),
        ("DELL-RAC-MIB", "drsCA2Message"),
        ("DELL-RAC-MIB", "drsCA2MessageArgs"),
        ("DELL-RAC-MIB", "drsCA2AlertStatus"),
        ("DELL-RAC-MIB", "drsCA2FQDD"),
        ("DELL-RAC-MIB", "drsProductChassisName"),
        ("DELL-RAC-MIB", "drsProductChassisLocation"),
        ("DELL-RAC-MIB", "drsChassisServiceTag"),
        ("DELL-RAC-MIB", "drsGlobalCurrStatus"))
)
if mibBuilder.loadTexts:
    alert2StorageVirtualDiskInformation.setStatus(
        ""
    )

alert2StorageSecurityFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 21, 0, 4433)
)
alert2StorageSecurityFailure.setObjects(
      *(("DELL-RAC-MIB", "drsCA2MessageID"),
        ("DELL-RAC-MIB", "drsCA2Message"),
        ("DELL-RAC-MIB", "drsCA2MessageArgs"),
        ("DELL-RAC-MIB", "drsCA2AlertStatus"),
        ("DELL-RAC-MIB", "drsCA2FQDD"),
        ("DELL-RAC-MIB", "drsProductChassisName"),
        ("DELL-RAC-MIB", "drsProductChassisLocation"),
        ("DELL-RAC-MIB", "drsChassisServiceTag"),
        ("DELL-RAC-MIB", "drsGlobalCurrStatus"))
)
if mibBuilder.loadTexts:
    alert2StorageSecurityFailure.setStatus(
        ""
    )

alert2StorageSecurityWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 21, 0, 4434)
)
alert2StorageSecurityWarning.setObjects(
      *(("DELL-RAC-MIB", "drsCA2MessageID"),
        ("DELL-RAC-MIB", "drsCA2Message"),
        ("DELL-RAC-MIB", "drsCA2MessageArgs"),
        ("DELL-RAC-MIB", "drsCA2AlertStatus"),
        ("DELL-RAC-MIB", "drsCA2FQDD"),
        ("DELL-RAC-MIB", "drsProductChassisName"),
        ("DELL-RAC-MIB", "drsProductChassisLocation"),
        ("DELL-RAC-MIB", "drsChassisServiceTag"),
        ("DELL-RAC-MIB", "drsGlobalCurrStatus"))
)
if mibBuilder.loadTexts:
    alert2StorageSecurityWarning.setStatus(
        ""
    )

alert2StorageSecurityInformation = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 21, 0, 4435)
)
alert2StorageSecurityInformation.setObjects(
      *(("DELL-RAC-MIB", "drsCA2MessageID"),
        ("DELL-RAC-MIB", "drsCA2Message"),
        ("DELL-RAC-MIB", "drsCA2MessageArgs"),
        ("DELL-RAC-MIB", "drsCA2AlertStatus"),
        ("DELL-RAC-MIB", "drsCA2FQDD"),
        ("DELL-RAC-MIB", "drsProductChassisName"),
        ("DELL-RAC-MIB", "drsProductChassisLocation"),
        ("DELL-RAC-MIB", "drsChassisServiceTag"),
        ("DELL-RAC-MIB", "drsGlobalCurrStatus"))
)
if mibBuilder.loadTexts:
    alert2StorageSecurityInformation.setStatus(
        ""
    )

alert2SoftwareChangeUpdateWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 21, 0, 6314)
)
alert2SoftwareChangeUpdateWarning.setObjects(
      *(("DELL-RAC-MIB", "drsCA2MessageID"),
        ("DELL-RAC-MIB", "drsCA2Message"),
        ("DELL-RAC-MIB", "drsCA2MessageArgs"),
        ("DELL-RAC-MIB", "drsCA2AlertStatus"),
        ("DELL-RAC-MIB", "drsCA2FQDD"),
        ("DELL-RAC-MIB", "drsProductChassisName"),
        ("DELL-RAC-MIB", "drsProductChassisLocation"),
        ("DELL-RAC-MIB", "drsChassisServiceTag"),
        ("DELL-RAC-MIB", "drsGlobalCurrStatus"))
)
if mibBuilder.loadTexts:
    alert2SoftwareChangeUpdateWarning.setStatus(
        ""
    )

alert2IOMTemperatureExceeded = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 21, 0, 8305)
)
alert2IOMTemperatureExceeded.setObjects(
      *(("DELL-RAC-MIB", "drsCA2MessageID"),
        ("DELL-RAC-MIB", "drsCA2Message"),
        ("DELL-RAC-MIB", "drsCA2MessageArgs"),
        ("DELL-RAC-MIB", "drsCA2AlertStatus"),
        ("DELL-RAC-MIB", "drsCA2FQDD"),
        ("DELL-RAC-MIB", "drsProductChassisName"),
        ("DELL-RAC-MIB", "drsProductChassisLocation"),
        ("DELL-RAC-MIB", "drsChassisServiceTag"),
        ("DELL-RAC-MIB", "drsGlobalCurrStatus"))
)
if mibBuilder.loadTexts:
    alert2IOMTemperatureExceeded.setStatus(
        ""
    )

alert2Unable2ReadTemperatureSensors = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 21, 0, 8306)
)
alert2Unable2ReadTemperatureSensors.setObjects(
      *(("DELL-RAC-MIB", "drsCA2MessageID"),
        ("DELL-RAC-MIB", "drsCA2Message"),
        ("DELL-RAC-MIB", "drsCA2MessageArgs"),
        ("DELL-RAC-MIB", "drsCA2AlertStatus"),
        ("DELL-RAC-MIB", "drsCA2FQDD"),
        ("DELL-RAC-MIB", "drsProductChassisName"),
        ("DELL-RAC-MIB", "drsProductChassisLocation"),
        ("DELL-RAC-MIB", "drsChassisServiceTag"),
        ("DELL-RAC-MIB", "drsGlobalCurrStatus"))
)
if mibBuilder.loadTexts:
    alert2Unable2ReadTemperatureSensors.setStatus(
        ""
    )

alert2PowerSupplyAuditFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 21, 0, 8329)
)
alert2PowerSupplyAuditFailure.setObjects(
      *(("DELL-RAC-MIB", "drsCA2MessageID"),
        ("DELL-RAC-MIB", "drsCA2Message"),
        ("DELL-RAC-MIB", "drsCA2MessageArgs"),
        ("DELL-RAC-MIB", "drsCA2AlertStatus"),
        ("DELL-RAC-MIB", "drsCA2FQDD"),
        ("DELL-RAC-MIB", "drsProductChassisName"),
        ("DELL-RAC-MIB", "drsProductChassisLocation"),
        ("DELL-RAC-MIB", "drsChassisServiceTag"),
        ("DELL-RAC-MIB", "drsGlobalCurrStatus"))
)
if mibBuilder.loadTexts:
    alert2PowerSupplyAuditFailure.setStatus(
        ""
    )

alert2PowerSupplyAuditWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 21, 0, 8330)
)
alert2PowerSupplyAuditWarning.setObjects(
      *(("DELL-RAC-MIB", "drsCA2MessageID"),
        ("DELL-RAC-MIB", "drsCA2Message"),
        ("DELL-RAC-MIB", "drsCA2MessageArgs"),
        ("DELL-RAC-MIB", "drsCA2AlertStatus"),
        ("DELL-RAC-MIB", "drsCA2FQDD"),
        ("DELL-RAC-MIB", "drsProductChassisName"),
        ("DELL-RAC-MIB", "drsProductChassisLocation"),
        ("DELL-RAC-MIB", "drsChassisServiceTag"),
        ("DELL-RAC-MIB", "drsGlobalCurrStatus"))
)
if mibBuilder.loadTexts:
    alert2PowerSupplyAuditWarning.setStatus(
        ""
    )

alert2PowerSupplyRedundancyPolicyChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 21, 0, 8331)
)
alert2PowerSupplyRedundancyPolicyChanged.setObjects(
      *(("DELL-RAC-MIB", "drsCA2MessageID"),
        ("DELL-RAC-MIB", "drsCA2Message"),
        ("DELL-RAC-MIB", "drsCA2MessageArgs"),
        ("DELL-RAC-MIB", "drsCA2AlertStatus"),
        ("DELL-RAC-MIB", "drsCA2FQDD"),
        ("DELL-RAC-MIB", "drsProductChassisName"),
        ("DELL-RAC-MIB", "drsProductChassisLocation"),
        ("DELL-RAC-MIB", "drsChassisServiceTag"),
        ("DELL-RAC-MIB", "drsGlobalCurrStatus"))
)
if mibBuilder.loadTexts:
    alert2PowerSupplyRedundancyPolicyChanged.setStatus(
        ""
    )

alert2SoftwareChangeAuditFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 21, 0, 8361)
)
alert2SoftwareChangeAuditFailure.setObjects(
      *(("DELL-RAC-MIB", "drsCA2MessageID"),
        ("DELL-RAC-MIB", "drsCA2Message"),
        ("DELL-RAC-MIB", "drsCA2MessageArgs"),
        ("DELL-RAC-MIB", "drsCA2AlertStatus"),
        ("DELL-RAC-MIB", "drsCA2FQDD"),
        ("DELL-RAC-MIB", "drsProductChassisName"),
        ("DELL-RAC-MIB", "drsProductChassisLocation"),
        ("DELL-RAC-MIB", "drsChassisServiceTag"),
        ("DELL-RAC-MIB", "drsGlobalCurrStatus"))
)
if mibBuilder.loadTexts:
    alert2SoftwareChangeAuditFailure.setStatus(
        ""
    )

alert2PowerUsageAuditFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 21, 0, 8417)
)
alert2PowerUsageAuditFailure.setObjects(
      *(("DELL-RAC-MIB", "drsCA2MessageID"),
        ("DELL-RAC-MIB", "drsCA2Message"),
        ("DELL-RAC-MIB", "drsCA2MessageArgs"),
        ("DELL-RAC-MIB", "drsCA2AlertStatus"),
        ("DELL-RAC-MIB", "drsCA2FQDD"),
        ("DELL-RAC-MIB", "drsProductChassisName"),
        ("DELL-RAC-MIB", "drsProductChassisLocation"),
        ("DELL-RAC-MIB", "drsChassisServiceTag"),
        ("DELL-RAC-MIB", "drsGlobalCurrStatus"))
)
if mibBuilder.loadTexts:
    alert2PowerUsageAuditFailure.setStatus(
        ""
    )

alert2PowerUsageAuditWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 21, 0, 8418)
)
alert2PowerUsageAuditWarning.setObjects(
      *(("DELL-RAC-MIB", "drsCA2MessageID"),
        ("DELL-RAC-MIB", "drsCA2Message"),
        ("DELL-RAC-MIB", "drsCA2MessageArgs"),
        ("DELL-RAC-MIB", "drsCA2AlertStatus"),
        ("DELL-RAC-MIB", "drsCA2FQDD"),
        ("DELL-RAC-MIB", "drsProductChassisName"),
        ("DELL-RAC-MIB", "drsProductChassisLocation"),
        ("DELL-RAC-MIB", "drsChassisServiceTag"),
        ("DELL-RAC-MIB", "drsGlobalCurrStatus"))
)
if mibBuilder.loadTexts:
    alert2PowerUsageAuditWarning.setStatus(
        ""
    )

alert2PowerUsageAuditInformation = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 21, 0, 8419)
)
alert2PowerUsageAuditInformation.setObjects(
      *(("DELL-RAC-MIB", "drsCA2MessageID"),
        ("DELL-RAC-MIB", "drsCA2Message"),
        ("DELL-RAC-MIB", "drsCA2MessageArgs"),
        ("DELL-RAC-MIB", "drsCA2AlertStatus"),
        ("DELL-RAC-MIB", "drsCA2FQDD"),
        ("DELL-RAC-MIB", "drsProductChassisName"),
        ("DELL-RAC-MIB", "drsProductChassisLocation"),
        ("DELL-RAC-MIB", "drsChassisServiceTag"),
        ("DELL-RAC-MIB", "drsGlobalCurrStatus"))
)
if mibBuilder.loadTexts:
    alert2PowerUsageAuditInformation.setStatus(
        ""
    )

alert2LicenseFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 21, 0, 8513)
)
alert2LicenseFailure.setObjects(
      *(("DELL-RAC-MIB", "drsCA2MessageID"),
        ("DELL-RAC-MIB", "drsCA2Message"),
        ("DELL-RAC-MIB", "drsCA2MessageArgs"),
        ("DELL-RAC-MIB", "drsCA2AlertStatus"),
        ("DELL-RAC-MIB", "drsCA2FQDD"),
        ("DELL-RAC-MIB", "drsProductChassisName"),
        ("DELL-RAC-MIB", "drsProductChassisLocation"),
        ("DELL-RAC-MIB", "drsChassisServiceTag"),
        ("DELL-RAC-MIB", "drsGlobalCurrStatus"))
)
if mibBuilder.loadTexts:
    alert2LicenseFailure.setStatus(
        ""
    )

alert2LicenseWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 21, 0, 8514)
)
alert2LicenseWarning.setObjects(
      *(("DELL-RAC-MIB", "drsCA2MessageID"),
        ("DELL-RAC-MIB", "drsCA2Message"),
        ("DELL-RAC-MIB", "drsCA2MessageArgs"),
        ("DELL-RAC-MIB", "drsCA2AlertStatus"),
        ("DELL-RAC-MIB", "drsCA2FQDD"),
        ("DELL-RAC-MIB", "drsProductChassisName"),
        ("DELL-RAC-MIB", "drsProductChassisLocation"),
        ("DELL-RAC-MIB", "drsChassisServiceTag"),
        ("DELL-RAC-MIB", "drsGlobalCurrStatus"))
)
if mibBuilder.loadTexts:
    alert2LicenseWarning.setStatus(
        ""
    )

alert2LicenseInformation = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 21, 0, 8515)
)
alert2LicenseInformation.setObjects(
      *(("DELL-RAC-MIB", "drsCA2MessageID"),
        ("DELL-RAC-MIB", "drsCA2Message"),
        ("DELL-RAC-MIB", "drsCA2MessageArgs"),
        ("DELL-RAC-MIB", "drsCA2AlertStatus"),
        ("DELL-RAC-MIB", "drsCA2FQDD"),
        ("DELL-RAC-MIB", "drsProductChassisName"),
        ("DELL-RAC-MIB", "drsProductChassisLocation"),
        ("DELL-RAC-MIB", "drsChassisServiceTag"),
        ("DELL-RAC-MIB", "drsGlobalCurrStatus"))
)
if mibBuilder.loadTexts:
    alert2LicenseInformation.setStatus(
        ""
    )

alert2PCIDeviceAuditWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 21, 0, 8562)
)
alert2PCIDeviceAuditWarning.setObjects(
      *(("DELL-RAC-MIB", "drsCA2MessageID"),
        ("DELL-RAC-MIB", "drsCA2Message"),
        ("DELL-RAC-MIB", "drsCA2MessageArgs"),
        ("DELL-RAC-MIB", "drsCA2AlertStatus"),
        ("DELL-RAC-MIB", "drsCA2FQDD"),
        ("DELL-RAC-MIB", "drsProductChassisName"),
        ("DELL-RAC-MIB", "drsProductChassisLocation"),
        ("DELL-RAC-MIB", "drsChassisServiceTag"),
        ("DELL-RAC-MIB", "drsGlobalCurrStatus"))
)
if mibBuilder.loadTexts:
    alert2PCIDeviceAuditWarning.setStatus(
        ""
    )

alert2CMCAuditFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 21, 0, 8689)
)
alert2CMCAuditFailure.setObjects(
      *(("DELL-RAC-MIB", "drsCA2MessageID"),
        ("DELL-RAC-MIB", "drsCA2Message"),
        ("DELL-RAC-MIB", "drsCA2MessageArgs"),
        ("DELL-RAC-MIB", "drsCA2AlertStatus"),
        ("DELL-RAC-MIB", "drsCA2FQDD"),
        ("DELL-RAC-MIB", "drsProductChassisName"),
        ("DELL-RAC-MIB", "drsProductChassisLocation"),
        ("DELL-RAC-MIB", "drsChassisServiceTag"),
        ("DELL-RAC-MIB", "drsGlobalCurrStatus"))
)
if mibBuilder.loadTexts:
    alert2CMCAuditFailure.setStatus(
        ""
    )

alert2CMCAuditWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 21, 0, 8690)
)
alert2CMCAuditWarning.setObjects(
      *(("DELL-RAC-MIB", "drsCA2MessageID"),
        ("DELL-RAC-MIB", "drsCA2Message"),
        ("DELL-RAC-MIB", "drsCA2MessageArgs"),
        ("DELL-RAC-MIB", "drsCA2AlertStatus"),
        ("DELL-RAC-MIB", "drsCA2FQDD"),
        ("DELL-RAC-MIB", "drsProductChassisName"),
        ("DELL-RAC-MIB", "drsProductChassisLocation"),
        ("DELL-RAC-MIB", "drsChassisServiceTag"),
        ("DELL-RAC-MIB", "drsGlobalCurrStatus"))
)
if mibBuilder.loadTexts:
    alert2CMCAuditWarning.setStatus(
        ""
    )

alert2CMCAuditInformation = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 21, 0, 8691)
)
alert2CMCAuditInformation.setObjects(
      *(("DELL-RAC-MIB", "drsCA2MessageID"),
        ("DELL-RAC-MIB", "drsCA2Message"),
        ("DELL-RAC-MIB", "drsCA2MessageArgs"),
        ("DELL-RAC-MIB", "drsCA2AlertStatus"),
        ("DELL-RAC-MIB", "drsCA2FQDD"),
        ("DELL-RAC-MIB", "drsProductChassisName"),
        ("DELL-RAC-MIB", "drsProductChassisLocation"),
        ("DELL-RAC-MIB", "drsChassisServiceTag"),
        ("DELL-RAC-MIB", "drsGlobalCurrStatus"))
)
if mibBuilder.loadTexts:
    alert2CMCAuditInformation.setStatus(
        ""
    )

alert2IOVirtualizationAuditWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 21, 0, 8698)
)
alert2IOVirtualizationAuditWarning.setObjects(
      *(("DELL-RAC-MIB", "drsCA2MessageID"),
        ("DELL-RAC-MIB", "drsCA2Message"),
        ("DELL-RAC-MIB", "drsCA2MessageArgs"),
        ("DELL-RAC-MIB", "drsCA2AlertStatus"),
        ("DELL-RAC-MIB", "drsCA2FQDD"),
        ("DELL-RAC-MIB", "drsProductChassisName"),
        ("DELL-RAC-MIB", "drsProductChassisLocation"),
        ("DELL-RAC-MIB", "drsChassisServiceTag"),
        ("DELL-RAC-MIB", "drsGlobalCurrStatus"))
)
if mibBuilder.loadTexts:
    alert2IOVirtualizationAuditWarning.setStatus(
        ""
    )

alert2CMCTestTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 21, 0, 10395)
)
alert2CMCTestTrap.setObjects(
      *(("DELL-RAC-MIB", "drsCA2MessageID"),
        ("DELL-RAC-MIB", "drsCA2Message"),
        ("DELL-RAC-MIB", "drsCA2MessageArgs"),
        ("DELL-RAC-MIB", "drsCA2AlertStatus"),
        ("DELL-RAC-MIB", "drsCA2FQDD"),
        ("DELL-RAC-MIB", "drsProductChassisName"),
        ("DELL-RAC-MIB", "drsProductChassisLocation"),
        ("DELL-RAC-MIB", "drsChassisServiceTag"),
        ("DELL-RAC-MIB", "drsGlobalCurrStatus"))
)
if mibBuilder.loadTexts:
    alert2CMCTestTrap.setStatus(
        ""
    )

alert2SWCConfigurationFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 21, 0, 10529)
)
alert2SWCConfigurationFailure.setObjects(
      *(("DELL-RAC-MIB", "drsCA2MessageID"),
        ("DELL-RAC-MIB", "drsCA2Message"),
        ("DELL-RAC-MIB", "drsCA2MessageArgs"),
        ("DELL-RAC-MIB", "drsCA2AlertStatus"),
        ("DELL-RAC-MIB", "drsCA2FQDD"),
        ("DELL-RAC-MIB", "drsProductChassisName"),
        ("DELL-RAC-MIB", "drsProductChassisLocation"),
        ("DELL-RAC-MIB", "drsChassisServiceTag"),
        ("DELL-RAC-MIB", "drsGlobalCurrStatus"))
)
if mibBuilder.loadTexts:
    alert2SWCConfigurationFailure.setStatus(
        ""
    )

alert2SWCConfigurationWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 21, 0, 10530)
)
alert2SWCConfigurationWarning.setObjects(
      *(("DELL-RAC-MIB", "drsCA2MessageID"),
        ("DELL-RAC-MIB", "drsCA2Message"),
        ("DELL-RAC-MIB", "drsCA2MessageArgs"),
        ("DELL-RAC-MIB", "drsCA2AlertStatus"),
        ("DELL-RAC-MIB", "drsCA2FQDD"),
        ("DELL-RAC-MIB", "drsProductChassisName"),
        ("DELL-RAC-MIB", "drsProductChassisLocation"),
        ("DELL-RAC-MIB", "drsChassisServiceTag"),
        ("DELL-RAC-MIB", "drsGlobalCurrStatus"))
)
if mibBuilder.loadTexts:
    alert2SWCConfigurationWarning.setStatus(
        ""
    )

alert2PCIDeviceConfigurationInformation = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 21, 0, 10611)
)
alert2PCIDeviceConfigurationInformation.setObjects(
      *(("DELL-RAC-MIB", "drsCA2MessageID"),
        ("DELL-RAC-MIB", "drsCA2Message"),
        ("DELL-RAC-MIB", "drsCA2MessageArgs"),
        ("DELL-RAC-MIB", "drsCA2AlertStatus"),
        ("DELL-RAC-MIB", "drsCA2FQDD"),
        ("DELL-RAC-MIB", "drsProductChassisName"),
        ("DELL-RAC-MIB", "drsProductChassisLocation"),
        ("DELL-RAC-MIB", "drsChassisServiceTag"),
        ("DELL-RAC-MIB", "drsGlobalCurrStatus"))
)
if mibBuilder.loadTexts:
    alert2PCIDeviceConfigurationInformation.setStatus(
        ""
    )

alert2IOVConfigurationWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 21, 0, 10746)
)
alert2IOVConfigurationWarning.setObjects(
      *(("DELL-RAC-MIB", "drsCA2MessageID"),
        ("DELL-RAC-MIB", "drsCA2Message"),
        ("DELL-RAC-MIB", "drsCA2MessageArgs"),
        ("DELL-RAC-MIB", "drsCA2AlertStatus"),
        ("DELL-RAC-MIB", "drsCA2FQDD"),
        ("DELL-RAC-MIB", "drsProductChassisName"),
        ("DELL-RAC-MIB", "drsProductChassisLocation"),
        ("DELL-RAC-MIB", "drsChassisServiceTag"),
        ("DELL-RAC-MIB", "drsGlobalCurrStatus"))
)
if mibBuilder.loadTexts:
    alert2IOVConfigurationWarning.setStatus(
        ""
    )

alert2IOVConfigurationInformation = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 21, 0, 10747)
)
alert2IOVConfigurationInformation.setObjects(
      *(("DELL-RAC-MIB", "drsCA2MessageID"),
        ("DELL-RAC-MIB", "drsCA2Message"),
        ("DELL-RAC-MIB", "drsCA2MessageArgs"),
        ("DELL-RAC-MIB", "drsCA2AlertStatus"),
        ("DELL-RAC-MIB", "drsCA2FQDD"),
        ("DELL-RAC-MIB", "drsProductChassisName"),
        ("DELL-RAC-MIB", "drsProductChassisLocation"),
        ("DELL-RAC-MIB", "drsChassisServiceTag"),
        ("DELL-RAC-MIB", "drsGlobalCurrStatus"))
)
if mibBuilder.loadTexts:
    alert2IOVConfigurationInformation.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "DELL-RAC-MIB",
    **{"DellString": DellString,
       "DellRacType": DellRacType,
       "DellStatus": DellStatus,
       "DellPowerReading": DellPowerReading,
       "DellCMCPowerIndexRange": DellCMCPowerIndexRange,
       "DellCMCPSUIndexRange": DellCMCPSUIndexRange,
       "DellCMCPSUCapable": DellCMCPSUCapable,
       "DellTemperatureReading": DellTemperatureReading,
       "DellTimestamp": DellTimestamp,
       "DellCMCServerIndexRange": DellCMCServerIndexRange,
       "DellCMCServerCapable": DellCMCServerCapable,
       "DellCMCServerStorageMode": DellCMCServerStorageMode,
       "DellCMCServerIntrusionState": DellCMCServerIntrusionState,
       "FQDDString": FQDDString,
       "ObjectStatusEnum": ObjectStatusEnum,
       "BooleanType": BooleanType,
       "dell": dell,
       "server3": server3,
       "drsOutofBandGroup": drsOutofBandGroup,
       "alertDrscTestTrapEvent": alertDrscTestTrapEvent,
       "alertDrscAuthError": alertDrscAuthError,
       "alertDrscLostESM": alertDrscLostESM,
       "alertDrscFoundESM": alertDrscFoundESM,
       "alertDrscPowerOff": alertDrscPowerOff,
       "alertDrscPowerOn": alertDrscPowerOn,
       "alertDrscWatchdogExpired": alertDrscWatchdogExpired,
       "alertDrscBattLow": alertDrscBattLow,
       "alertDrscTempNormal": alertDrscTempNormal,
       "alertDrscTempWarning": alertDrscTempWarning,
       "alertDrscTempCritical": alertDrscTempCritical,
       "alertDrscVoltNormal": alertDrscVoltNormal,
       "alertDrscVoltWarning": alertDrscVoltWarning,
       "alertDrscVoltCritical": alertDrscVoltCritical,
       "alertDrscSELWarning": alertDrscSELWarning,
       "alertDrscSELCritical": alertDrscSELCritical,
       "alertDrscSEL80percentFull": alertDrscSEL80percentFull,
       "alertDrscSEL90percentFull": alertDrscSEL90percentFull,
       "alertDrscSEL100percentFull": alertDrscSEL100percentFull,
       "alertDrscSELNormal": alertDrscSELNormal,
       "alertCMCTestTrap": alertCMCTestTrap,
       "alertCMCNormalTrap": alertCMCNormalTrap,
       "alertCMCWarningTrap": alertCMCWarningTrap,
       "alertCMCCriticalTrap": alertCMCCriticalTrap,
       "alertCMCNonRecoverableTrap": alertCMCNonRecoverableTrap,
       "drsInformationGroup": drsInformationGroup,
       "drsProductInfoGroup": drsProductInfoGroup,
       "drsProductName": drsProductName,
       "drsProductShortName": drsProductShortName,
       "drsProductDescription": drsProductDescription,
       "drsProductManufacturer": drsProductManufacturer,
       "drsProductVersion": drsProductVersion,
       "drsChassisServiceTag": drsChassisServiceTag,
       "drsProductURL": drsProductURL,
       "drsProductChassisAssetTag": drsProductChassisAssetTag,
       "drsProductChassisLocation": drsProductChassisLocation,
       "drsProductChassisName": drsProductChassisName,
       "drsSystemServiceTag": drsSystemServiceTag,
       "drsProductSystemAssetTag": drsProductSystemAssetTag,
       "drsProductSystemSlot": drsProductSystemSlot,
       "drsProductType": drsProductType,
       "drsProductChassisDataCenter": drsProductChassisDataCenter,
       "drsProductChassisAisle": drsProductChassisAisle,
       "drsProductChassisRack": drsProductChassisRack,
       "drsProductChassisRackSlot": drsProductChassisRackSlot,
       "drsProductChassisModel": drsProductChassisModel,
       "drsProductChassisExpressServiceCode": drsProductChassisExpressServiceCode,
       "drsProductChassisSystemID": drsProductChassisSystemID,
       "drsProductChassisSize": drsProductChassisSize,
       "drsFirmwareGroup": drsFirmwareGroup,
       "drsFirmwareVersion": drsFirmwareVersion,
       "drsiKVMFirmwareVersion": drsiKVMFirmwareVersion,
       "drsFirmwareVersion2": drsFirmwareVersion2,
       "drsStatusGroup": drsStatusGroup,
       "drsGlobalSystemStatus": drsGlobalSystemStatus,
       "drsChassisStatusGroup": drsChassisStatusGroup,
       "drsStatusNowGroup": drsStatusNowGroup,
       "drsGlobalCurrStatus": drsGlobalCurrStatus,
       "drsIOMCurrStatus": drsIOMCurrStatus,
       "drsKVMCurrStatus": drsKVMCurrStatus,
       "drsRedCurrStatus": drsRedCurrStatus,
       "drsPowerCurrStatus": drsPowerCurrStatus,
       "drsFanCurrStatus": drsFanCurrStatus,
       "drsBladeCurrStatus": drsBladeCurrStatus,
       "drsTempCurrStatus": drsTempCurrStatus,
       "drsCMCCurrStatus": drsCMCCurrStatus,
       "drsChassisFrontPanelAmbientTemperature": drsChassisFrontPanelAmbientTemperature,
       "drsCMCAmbientTemperature": drsCMCAmbientTemperature,
       "drsCMCProcessorTemperature": drsCMCProcessorTemperature,
       "drsStatusPrevGroup": drsStatusPrevGroup,
       "drsGlobalPrevStatus": drsGlobalPrevStatus,
       "drsIOMPrevStatus": drsIOMPrevStatus,
       "drsKVMPrevStatus": drsKVMPrevStatus,
       "drsRedPrevStatus": drsRedPrevStatus,
       "drsPowerPrevStatus": drsPowerPrevStatus,
       "drsFanPrevStatus": drsFanPrevStatus,
       "drsBladePrevStatus": drsBladePrevStatus,
       "drsTempPrevStatus": drsTempPrevStatus,
       "drsCMCPrevStatus": drsCMCPrevStatus,
       "drsStatusChangeGroup": drsStatusChangeGroup,
       "drsGlobalChangeTime": drsGlobalChangeTime,
       "drsIOMChangeTime": drsIOMChangeTime,
       "drsKVMChangeTime": drsKVMChangeTime,
       "drsRedChangeTime": drsRedChangeTime,
       "drsPowerChangeTime": drsPowerChangeTime,
       "drsFanChangeTime": drsFanChangeTime,
       "drsBladeChangeTime": drsBladeChangeTime,
       "drsTempChangeTime": drsTempChangeTime,
       "drsCMCChangeTime": drsCMCChangeTime,
       "drsChassisPowerGroup": drsChassisPowerGroup,
       "drsCMCPowerTable": drsCMCPowerTable,
       "drsCMCPowerTableEntry": drsCMCPowerTableEntry,
       "drsChassisIndex": drsChassisIndex,
       "drsPotentialPower": drsPotentialPower,
       "drsIdlePower": drsIdlePower,
       "drsMaxPowerSpecification": drsMaxPowerSpecification,
       "drsPowerSurplus": drsPowerSurplus,
       "drsKWhCumulative": drsKWhCumulative,
       "drsKWhCumulativeTime": drsKWhCumulativeTime,
       "drsWattsPeakUsage": drsWattsPeakUsage,
       "drsWattsPeakTime": drsWattsPeakTime,
       "drsWattsMinUsage": drsWattsMinUsage,
       "drsWattsMinTime": drsWattsMinTime,
       "drsWattsResetTime": drsWattsResetTime,
       "drsWattsReading": drsWattsReading,
       "drsAmpsReading": drsAmpsReading,
       "drsCMCPSUTable": drsCMCPSUTable,
       "drsCMCPSUTableEntry": drsCMCPSUTableEntry,
       "drsPSUChassisIndex": drsPSUChassisIndex,
       "drsPSUIndex": drsPSUIndex,
       "drsPSULocation": drsPSULocation,
       "drsPSUMonitoringCapable": drsPSUMonitoringCapable,
       "drsPSUVoltsReading": drsPSUVoltsReading,
       "drsPSUAmpsReading": drsPSUAmpsReading,
       "drsPSUWattsReading": drsPSUWattsReading,
       "drsChassisServerGroup": drsChassisServerGroup,
       "drsCMCServerTable": drsCMCServerTable,
       "drsCMCServerTableEntry": drsCMCServerTableEntry,
       "drsServerIndex": drsServerIndex,
       "drsServerMonitoringCapable": drsServerMonitoringCapable,
       "drsServerServiceTag": drsServerServiceTag,
       "drsServerSlotName": drsServerSlotName,
       "drsServerSlotNumber": drsServerSlotNumber,
       "drsServerNodeID": drsServerNodeID,
       "drsServerModel": drsServerModel,
       "drsServerAssetTag": drsServerAssetTag,
       "drsServerNumStorageControllers": drsServerNumStorageControllers,
       "drsServerStorageMode": drsServerStorageMode,
       "drsServerIntrusionState": drsServerIntrusionState,
       "drsServerAssignedServerSlots": drsServerAssignedServerSlots,
       "storageDetailsGroup": storageDetailsGroup,
       "software": software,
       "storageManagement": storageManagement,
       "physicalDevices": physicalDevices,
       "controllerTable": controllerTable,
       "controllerTableEntry": controllerTableEntry,
       "controllerNumber": controllerNumber,
       "controllerName": controllerName,
       "controllerRebuildRate": controllerRebuildRate,
       "controllerFWVersion": controllerFWVersion,
       "controllerCacheSizeInMB": controllerCacheSizeInMB,
       "controllerRollUpStatus": controllerRollUpStatus,
       "controllerComponentStatus": controllerComponentStatus,
       "controllerDriverVersion": controllerDriverVersion,
       "controllerPCISlot": controllerPCISlot,
       "controllerReconstructRate": controllerReconstructRate,
       "controllerPatrolReadRate": controllerPatrolReadRate,
       "controllerBGIRate": controllerBGIRate,
       "controllerCheckConsistencyRate": controllerCheckConsistencyRate,
       "controllerPatrolReadMode": controllerPatrolReadMode,
       "controllerPatrolReadState": controllerPatrolReadState,
       "controllerPersistentHotSpare": controllerPersistentHotSpare,
       "controllerSpinDownUnconfiguredDrives": controllerSpinDownUnconfiguredDrives,
       "controllerSpinDownHotSpareDrives": controllerSpinDownHotSpareDrives,
       "controllerSpinDownTimeInterval": controllerSpinDownTimeInterval,
       "controllerPreservedCache": controllerPreservedCache,
       "controllerCheckConsistencyMode": controllerCheckConsistencyMode,
       "controllerCopyBackMode": controllerCopyBackMode,
       "controllerSecurityStatus": controllerSecurityStatus,
       "controllerEncryptionKeyPresent": controllerEncryptionKeyPresent,
       "controllerEncryptionCapability": controllerEncryptionCapability,
       "controllerLoadBalanceSetting": controllerLoadBalanceSetting,
       "controllerMaxCapSpeed": controllerMaxCapSpeed,
       "controllerSASAddress": controllerSASAddress,
       "controllerFQDD": controllerFQDD,
       "controllerDisplayName": controllerDisplayName,
       "controllerT10PICapability": controllerT10PICapability,
       "controllerRAID10UnevenSpansSupported": controllerRAID10UnevenSpansSupported,
       "controllerEnhancedAutoImportForeignConfigMode": controllerEnhancedAutoImportForeignConfigMode,
       "controllerBootModeSupported": controllerBootModeSupported,
       "controllerBootMode": controllerBootMode,
       "controllerHighAvailabilityMode": controllerHighAvailabilityMode,
       "controllerPeerController": controllerPeerController,
       "controllerEncryptionKeyIdentifier": controllerEncryptionKeyIdentifier,
       "enclosureTable": enclosureTable,
       "enclosureTableEntry": enclosureTableEntry,
       "enclosureNumber": enclosureNumber,
       "enclosureName": enclosureName,
       "enclosureState": enclosureState,
       "enclosureServiceTag": enclosureServiceTag,
       "enclosureAssetTag": enclosureAssetTag,
       "enclosureConnectedPort": enclosureConnectedPort,
       "enclosureRollUpStatus": enclosureRollUpStatus,
       "enclosureComponentStatus": enclosureComponentStatus,
       "enclosureFirmwareVersion": enclosureFirmwareVersion,
       "enclosureSASAddress": enclosureSASAddress,
       "enclosureDriveCount": enclosureDriveCount,
       "enclosureTotalSlots": enclosureTotalSlots,
       "enclosureFanCount": enclosureFanCount,
       "enclosurePSUCount": enclosurePSUCount,
       "enclosureEMMCount": enclosureEMMCount,
       "enclosureTempProbeCount": enclosureTempProbeCount,
       "enclosureRedundantPath": enclosureRedundantPath,
       "enclosurePosition": enclosurePosition,
       "enclosureBackplaneBayID": enclosureBackplaneBayID,
       "enclosureFQDD": enclosureFQDD,
       "enclosureDisplayName": enclosureDisplayName,
       "enclosureType": enclosureType,
       "physicalDiskTable": physicalDiskTable,
       "physicalDiskTableEntry": physicalDiskTableEntry,
       "physicalDiskNumber": physicalDiskNumber,
       "physicalDiskName": physicalDiskName,
       "physicalDiskManufacturer": physicalDiskManufacturer,
       "physicalDiskState": physicalDiskState,
       "physicalDiskProductID": physicalDiskProductID,
       "physicalDiskSerialNo": physicalDiskSerialNo,
       "physicalDiskRevision": physicalDiskRevision,
       "physicalDiskCapacityInMB": physicalDiskCapacityInMB,
       "physicalDiskUsedSpaceInMB": physicalDiskUsedSpaceInMB,
       "physicalDiskFreeSpaceInMB": physicalDiskFreeSpaceInMB,
       "physicalDiskBusType": physicalDiskBusType,
       "physicalDiskSpareState": physicalDiskSpareState,
       "physicalDiskComponentStatus": physicalDiskComponentStatus,
       "physicalDiskPartNumber": physicalDiskPartNumber,
       "physicalDiskSASAddress": physicalDiskSASAddress,
       "physicalDiskNegotiatedSpeed": physicalDiskNegotiatedSpeed,
       "physicalDiskCapableSpeed": physicalDiskCapableSpeed,
       "physicalDiskSmartAlertIndication": physicalDiskSmartAlertIndication,
       "physicalDiskManufactureDay": physicalDiskManufactureDay,
       "physicalDiskManufactureWeek": physicalDiskManufactureWeek,
       "physicalDiskManufactureYear": physicalDiskManufactureYear,
       "physicalDiskMediaType": physicalDiskMediaType,
       "physicalDiskPowerState": physicalDiskPowerState,
       "physicalDiskRemainingRatedWriteEndurance": physicalDiskRemainingRatedWriteEndurance,
       "physicalDiskOperationalState": physicalDiskOperationalState,
       "physicalDiskProgress": physicalDiskProgress,
       "physicalDiskSecurityStatus": physicalDiskSecurityStatus,
       "physicalDiskFormFactor": physicalDiskFormFactor,
       "physicalDiskFQDD": physicalDiskFQDD,
       "physicalDiskDisplayName": physicalDiskDisplayName,
       "physicalDiskT10PICapability": physicalDiskT10PICapability,
       "physicalDiskBlockSizeInBytes": physicalDiskBlockSizeInBytes,
       "physicalDiskProtocolVersion": physicalDiskProtocolVersion,
       "physicalDiskPCIeNegotiatedLinkWidth": physicalDiskPCIeNegotiatedLinkWidth,
       "physicalDiskPCIeCapableLinkWidth": physicalDiskPCIeCapableLinkWidth,
       "physicalDiskCurrentActiveController": physicalDiskCurrentActiveController,
       "physicalDiskFailoverController": physicalDiskFailoverController,
       "physicalDiskForeignKeyIdentifier": physicalDiskForeignKeyIdentifier,
       "enclosureFanTable": enclosureFanTable,
       "enclosureFanTableEntry": enclosureFanTableEntry,
       "enclosureFanNumber": enclosureFanNumber,
       "enclosureFanName": enclosureFanName,
       "enclosureFanState": enclosureFanState,
       "enclosureFanSpeed": enclosureFanSpeed,
       "enclosureFanComponentStatus": enclosureFanComponentStatus,
       "enclosureFanFQDD": enclosureFanFQDD,
       "enclosureFanDisplayName": enclosureFanDisplayName,
       "enclosurePowerSupplyTable": enclosurePowerSupplyTable,
       "enclosurePowerSupplyTableEntry": enclosurePowerSupplyTableEntry,
       "enclosurePowerSupplyNumber": enclosurePowerSupplyNumber,
       "enclosurePowerSupplyName": enclosurePowerSupplyName,
       "enclosurePowerSupplyState": enclosurePowerSupplyState,
       "enclosurePowerSupplyPartNumber": enclosurePowerSupplyPartNumber,
       "enclosurePowerSupplyComponentStatus": enclosurePowerSupplyComponentStatus,
       "enclosurePowerSupplyFQDD": enclosurePowerSupplyFQDD,
       "enclosurePowerSupplyDisplayName": enclosurePowerSupplyDisplayName,
       "enclosureTemperatureProbeTable": enclosureTemperatureProbeTable,
       "enclosureTemperatureProbeTableEntry": enclosureTemperatureProbeTableEntry,
       "enclosureTemperatureProbeNumber": enclosureTemperatureProbeNumber,
       "enclosureTemperatureProbeName": enclosureTemperatureProbeName,
       "enclosureTemperatureProbeState": enclosureTemperatureProbeState,
       "enclosureTemperatureProbeMinWarningValue": enclosureTemperatureProbeMinWarningValue,
       "enclosureTemperatureProbeMinCriticalValue": enclosureTemperatureProbeMinCriticalValue,
       "enclosureTemperatureProbeMaxWarningValue": enclosureTemperatureProbeMaxWarningValue,
       "enclosureTemperatureProbeMaxCriticalValue": enclosureTemperatureProbeMaxCriticalValue,
       "enclosureTemperatureProbeCurValue": enclosureTemperatureProbeCurValue,
       "enclosureTemperatureProbeComponentStatus": enclosureTemperatureProbeComponentStatus,
       "enclosureTemperatureProbeFQDD": enclosureTemperatureProbeFQDD,
       "enclosureTemperatureProbeDisplayName": enclosureTemperatureProbeDisplayName,
       "enclosureManagementModuleTable": enclosureManagementModuleTable,
       "enclosureManagementModuleTableEntry": enclosureManagementModuleTableEntry,
       "enclosureManagementModuleNumber": enclosureManagementModuleNumber,
       "enclosureManagementModuleName": enclosureManagementModuleName,
       "enclosureManagementModuleState": enclosureManagementModuleState,
       "enclosureManagementModulePartNumber": enclosureManagementModulePartNumber,
       "enclosureManagementModuleFWVersion": enclosureManagementModuleFWVersion,
       "enclosureManagementModuleComponentStatus": enclosureManagementModuleComponentStatus,
       "enclosureManagementModuleFQDD": enclosureManagementModuleFQDD,
       "enclosureManagementModuleDisplayName": enclosureManagementModuleDisplayName,
       "batteryTable": batteryTable,
       "batteryTableEntry": batteryTableEntry,
       "batteryNumber": batteryNumber,
       "batteryState": batteryState,
       "batteryComponentStatus": batteryComponentStatus,
       "batteryPredictedCapacity": batteryPredictedCapacity,
       "batteryFQDD": batteryFQDD,
       "batteryDisplayName": batteryDisplayName,
       "logicalDevices": logicalDevices,
       "virtualDiskTable": virtualDiskTable,
       "virtualDiskTableEntry": virtualDiskTableEntry,
       "virtualDiskNumber": virtualDiskNumber,
       "virtualDiskName": virtualDiskName,
       "virtualDiskState": virtualDiskState,
       "virtualDiskSizeInMB": virtualDiskSizeInMB,
       "virtualDiskWritePolicy": virtualDiskWritePolicy,
       "virtualDiskReadPolicy": virtualDiskReadPolicy,
       "virtualDiskLayout": virtualDiskLayout,
       "virtualDiskStripeSize": virtualDiskStripeSize,
       "virtualDiskComponentStatus": virtualDiskComponentStatus,
       "virtualDiskBadBlocksDetected": virtualDiskBadBlocksDetected,
       "virtualDiskSecured": virtualDiskSecured,
       "virtualDiskIsCacheCade": virtualDiskIsCacheCade,
       "virtualDiskDiskCachePolicy": virtualDiskDiskCachePolicy,
       "virtualDiskOperationalState": virtualDiskOperationalState,
       "virtualDiskProgress": virtualDiskProgress,
       "virtualDiskAvailableProtocols": virtualDiskAvailableProtocols,
       "virtualDiskMediaType": virtualDiskMediaType,
       "virtualDiskRemainingRedundancy": virtualDiskRemainingRedundancy,
       "virtualDiskFQDD": virtualDiskFQDD,
       "virtualDiskDisplayName": virtualDiskDisplayName,
       "virtualDiskT10PIStatus": virtualDiskT10PIStatus,
       "virtualDiskBlockSizeInBytes": virtualDiskBlockSizeInBytes,
       "virtualDiskAdapter1AccessPolicy": virtualDiskAdapter1AccessPolicy,
       "virtualDiskAdapter2AccessPolicy": virtualDiskAdapter2AccessPolicy,
       "virtualDiskAdapter3AccessPolicy": virtualDiskAdapter3AccessPolicy,
       "virtualDiskAdapter4AccessPolicy": virtualDiskAdapter4AccessPolicy,
       "virtualDiskCurrentActiveController": virtualDiskCurrentActiveController,
       "virtualDiskFailoverController": virtualDiskFailoverController,
       "drsCMCAlertGroup": drsCMCAlertGroup,
       "drsChassisAlertVariables": drsChassisAlertVariables,
       "drsCASubSystem": drsCASubSystem,
       "drsCASSCurrStatus": drsCASSCurrStatus,
       "drsCASSPrevStatus": drsCASSPrevStatus,
       "drsCASSChangeTime": drsCASSChangeTime,
       "drsCAMessage": drsCAMessage,
       "drsCMCAlert2Group": drsCMCAlert2Group,
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
       "alert2PCIDeviceFailure": alert2PCIDeviceFailure,
       "alert2PCIDeviceWarning": alert2PCIDeviceWarning,
       "alert2PCIDeviceInformation": alert2PCIDeviceInformation,
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
       "alert2IOMTemperatureExceeded": alert2IOMTemperatureExceeded,
       "alert2Unable2ReadTemperatureSensors": alert2Unable2ReadTemperatureSensors,
       "alert2PowerSupplyAuditFailure": alert2PowerSupplyAuditFailure,
       "alert2PowerSupplyAuditWarning": alert2PowerSupplyAuditWarning,
       "alert2PowerSupplyRedundancyPolicyChanged": alert2PowerSupplyRedundancyPolicyChanged,
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
       "drsChassisAlert2Variables": drsChassisAlert2Variables,
       "drsCA2MessageID": drsCA2MessageID,
       "drsCA2Message": drsCA2Message,
       "drsCA2MessageArgs": drsCA2MessageArgs,
       "drsCA2AlertStatus": drsCA2AlertStatus,
       "drsCA2FQDD": drsCA2FQDD,
       "drsAlertGroup": drsAlertGroup,
       "drsAlertVariables": drsAlertVariables,
       "drsAlertSystem": drsAlertSystem,
       "drsAlertTableIndexOID": drsAlertTableIndexOID,
       "drsAlertMessage": drsAlertMessage,
       "drsAlertCurrentStatus": drsAlertCurrentStatus,
       "drsAlertPreviousStatus": drsAlertPreviousStatus,
       "drsAlertData": drsAlertData}
)
