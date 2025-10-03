# SNMP MIB module (SML-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\SML-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 12:01:07 2025
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



class UShortReal(Integer32):
    """Custom type UShortReal based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )





class CimDateTime(OctetString):
    """Custom type CimDateTime based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(24, 24),
    )
    fixed_length = 24





class UINT64(OctetString):
    """Custom type UINT64 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )
    fixed_length = 8





class UINT32(Integer32):
    """Custom type UINT32 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )





class UINT16(Integer32):
    """Custom type UINT16 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )




# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Ibm_ObjectIdentity = ObjectIdentity
ibm = _Ibm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2)
)
_IbmProd_ObjectIdentity = ObjectIdentity
ibmProd = _IbmProd_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6)
)
_Ibm3584_ObjectIdentity = ObjectIdentity
ibm3584 = _Ibm3584_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 182)
)
_SmlRoot_ObjectIdentity = ObjectIdentity
smlRoot = _SmlRoot_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 182, 3)
)


class _SmlMibVersion_Type(DisplayString):
    """Custom type smlMibVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 4),
    )


_SmlMibVersion_Type.__name__ = "DisplayString"
_SmlMibVersion_Object = MibScalar
smlMibVersion = _SmlMibVersion_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 182, 3, 1),
    _SmlMibVersion_Type()
)
smlMibVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smlMibVersion.setStatus("mandatory")


class _SmlCimVersion_Type(DisplayString):
    """Custom type smlCimVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 4),
    )


_SmlCimVersion_Type.__name__ = "DisplayString"
_SmlCimVersion_Object = MibScalar
smlCimVersion = _SmlCimVersion_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 182, 3, 2),
    _SmlCimVersion_Type()
)
smlCimVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smlCimVersion.setStatus("mandatory")
_ProductGroup_ObjectIdentity = ObjectIdentity
productGroup = _ProductGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 182, 3, 3)
)


class _Product_Name_Type(DisplayString):
    """Custom type product_Name based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_Product_Name_Type.__name__ = "DisplayString"
_Product_Name_Object = MibScalar
product_Name = _Product_Name_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 182, 3, 3, 1),
    _Product_Name_Type()
)
product_Name.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    product_Name.setStatus("mandatory")


class _Product_IdentifyingNumber_Type(DisplayString):
    """Custom type product_IdentifyingNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_Product_IdentifyingNumber_Type.__name__ = "DisplayString"
_Product_IdentifyingNumber_Object = MibScalar
product_IdentifyingNumber = _Product_IdentifyingNumber_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 182, 3, 3, 2),
    _Product_IdentifyingNumber_Type()
)
product_IdentifyingNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    product_IdentifyingNumber.setStatus("mandatory")


class _Product_Vendor_Type(DisplayString):
    """Custom type product_Vendor based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_Product_Vendor_Type.__name__ = "DisplayString"
_Product_Vendor_Object = MibScalar
product_Vendor = _Product_Vendor_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 182, 3, 3, 3),
    _Product_Vendor_Type()
)
product_Vendor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    product_Vendor.setStatus("mandatory")


class _Product_Version_Type(DisplayString):
    """Custom type product_Version based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_Product_Version_Type.__name__ = "DisplayString"
_Product_Version_Object = MibScalar
product_Version = _Product_Version_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 182, 3, 3, 4),
    _Product_Version_Type()
)
product_Version.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    product_Version.setStatus("mandatory")
_ChassisGroup_ObjectIdentity = ObjectIdentity
chassisGroup = _ChassisGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 182, 3, 4)
)


class _Chassis_Manufacturer_Type(DisplayString):
    """Custom type chassis_Manufacturer based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_Chassis_Manufacturer_Type.__name__ = "DisplayString"
_Chassis_Manufacturer_Object = MibScalar
chassis_Manufacturer = _Chassis_Manufacturer_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 182, 3, 4, 1),
    _Chassis_Manufacturer_Type()
)
chassis_Manufacturer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chassis_Manufacturer.setStatus("mandatory")


class _Chassis_Model_Type(DisplayString):
    """Custom type chassis_Model based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_Chassis_Model_Type.__name__ = "DisplayString"
_Chassis_Model_Object = MibScalar
chassis_Model = _Chassis_Model_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 182, 3, 4, 2),
    _Chassis_Model_Type()
)
chassis_Model.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chassis_Model.setStatus("mandatory")


class _Chassis_SerialNumber_Type(DisplayString):
    """Custom type chassis_SerialNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_Chassis_SerialNumber_Type.__name__ = "DisplayString"
_Chassis_SerialNumber_Object = MibScalar
chassis_SerialNumber = _Chassis_SerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 182, 3, 4, 3),
    _Chassis_SerialNumber_Type()
)
chassis_SerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chassis_SerialNumber.setStatus("mandatory")


class _Chassis_LockPresent_Type(Integer32):
    """Custom type chassis_LockPresent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 0),
          ("true", 1),
          ("false", 2))
    )


_Chassis_LockPresent_Type.__name__ = "Integer32"
_Chassis_LockPresent_Object = MibScalar
chassis_LockPresent = _Chassis_LockPresent_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 182, 3, 4, 4),
    _Chassis_LockPresent_Type()
)
chassis_LockPresent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chassis_LockPresent.setStatus("mandatory")


class _Chassis_SecurityBreach_Type(Integer32):
    """Custom type chassis_SecurityBreach based on Integer32"""
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
        *(("unknown", 0),
          ("other", 1),
          ("noBreach", 2),
          ("breachAttempted", 3))
    )


_Chassis_SecurityBreach_Type.__name__ = "Integer32"
_Chassis_SecurityBreach_Object = MibScalar
chassis_SecurityBreach = _Chassis_SecurityBreach_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 182, 3, 4, 5),
    _Chassis_SecurityBreach_Type()
)
chassis_SecurityBreach.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chassis_SecurityBreach.setStatus("mandatory")


class _Chassis_IsLocked_Type(Integer32):
    """Custom type chassis_IsLocked based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 0),
          ("true", 1),
          ("false", 2))
    )


_Chassis_IsLocked_Type.__name__ = "Integer32"
_Chassis_IsLocked_Object = MibScalar
chassis_IsLocked = _Chassis_IsLocked_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 182, 3, 4, 6),
    _Chassis_IsLocked_Type()
)
chassis_IsLocked.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chassis_IsLocked.setStatus("mandatory")
_StorageLibraryGroup_ObjectIdentity = ObjectIdentity
storageLibraryGroup = _StorageLibraryGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 182, 3, 5)
)


class _StorageLibrary_Name_Type(DisplayString):
    """Custom type storageLibrary_Name based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_StorageLibrary_Name_Type.__name__ = "DisplayString"
_StorageLibrary_Name_Object = MibScalar
storageLibrary_Name = _StorageLibrary_Name_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 182, 3, 5, 1),
    _StorageLibrary_Name_Type()
)
storageLibrary_Name.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    storageLibrary_Name.setStatus("mandatory")


class _StorageLibrary_Description_Type(DisplayString):
    """Custom type storageLibrary_Description based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_StorageLibrary_Description_Type.__name__ = "DisplayString"
_StorageLibrary_Description_Object = MibScalar
storageLibrary_Description = _StorageLibrary_Description_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 182, 3, 5, 2),
    _StorageLibrary_Description_Type()
)
storageLibrary_Description.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    storageLibrary_Description.setStatus("mandatory")


class _StorageLibrary_Caption_Type(DisplayString):
    """Custom type storageLibrary_Caption based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_StorageLibrary_Caption_Type.__name__ = "DisplayString"
_StorageLibrary_Caption_Object = MibScalar
storageLibrary_Caption = _StorageLibrary_Caption_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 182, 3, 5, 3),
    _StorageLibrary_Caption_Type()
)
storageLibrary_Caption.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    storageLibrary_Caption.setStatus("mandatory")


class _StorageLibrary_Status_Type(DisplayString):
    """Custom type storageLibrary_Status based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_StorageLibrary_Status_Type.__name__ = "DisplayString"
_StorageLibrary_Status_Object = MibScalar
storageLibrary_Status = _StorageLibrary_Status_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 182, 3, 5, 4),
    _StorageLibrary_Status_Type()
)
storageLibrary_Status.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    storageLibrary_Status.setStatus("mandatory")
_StorageLibrary_InstallDate_Type = CimDateTime
_StorageLibrary_InstallDate_Object = MibScalar
storageLibrary_InstallDate = _StorageLibrary_InstallDate_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 182, 3, 5, 5),
    _StorageLibrary_InstallDate_Type()
)
storageLibrary_InstallDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    storageLibrary_InstallDate.setStatus("mandatory")
_MediaAccessDeviceGroup_ObjectIdentity = ObjectIdentity
mediaAccessDeviceGroup = _MediaAccessDeviceGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 182, 3, 6)
)
_NumberOfMediaAccessDevices_Type = Integer32
_NumberOfMediaAccessDevices_Object = MibScalar
numberOfMediaAccessDevices = _NumberOfMediaAccessDevices_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 182, 3, 6, 1),
    _NumberOfMediaAccessDevices_Type()
)
numberOfMediaAccessDevices.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    numberOfMediaAccessDevices.setStatus("mandatory")
_MediaAccessDeviceTable_Object = MibTable
mediaAccessDeviceTable = _MediaAccessDeviceTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 182, 3, 6, 2)
)
if mibBuilder.loadTexts:
    mediaAccessDeviceTable.setStatus("mandatory")
_MediaAccessDeviceEntry_Object = MibTableRow
mediaAccessDeviceEntry = _MediaAccessDeviceEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 182, 3, 6, 2, 1)
)
mediaAccessDeviceEntry.setIndexNames(
    (0, "SML-MIB", "mediaAccessDeviceIndex"),
)
if mibBuilder.loadTexts:
    mediaAccessDeviceEntry.setStatus("mandatory")
_MediaAccessDeviceIndex_Type = UINT32
_MediaAccessDeviceIndex_Object = MibTableColumn
mediaAccessDeviceIndex = _MediaAccessDeviceIndex_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 182, 3, 6, 2, 1, 1),
    _MediaAccessDeviceIndex_Type()
)
mediaAccessDeviceIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mediaAccessDeviceIndex.setStatus("mandatory")


class _MediaAccessDeviceObjectType_Type(Integer32):
    """Custom type mediaAccessDeviceObjectType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 0),
          ("wormDrive", 1),
          ("magnetoOpticalDrive", 2),
          ("tapeDrive", 3),
          ("dvdDrive", 4),
          ("cdromDrive", 5))
    )


_MediaAccessDeviceObjectType_Type.__name__ = "Integer32"
_MediaAccessDeviceObjectType_Object = MibTableColumn
mediaAccessDeviceObjectType = _MediaAccessDeviceObjectType_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 182, 3, 6, 2, 1, 2),
    _MediaAccessDeviceObjectType_Type()
)
mediaAccessDeviceObjectType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mediaAccessDeviceObjectType.setStatus("mandatory")


class _MediaAccessDevice_Name_Type(DisplayString):
    """Custom type mediaAccessDevice_Name based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_MediaAccessDevice_Name_Type.__name__ = "DisplayString"
_MediaAccessDevice_Name_Object = MibTableColumn
mediaAccessDevice_Name = _MediaAccessDevice_Name_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 182, 3, 6, 2, 1, 3),
    _MediaAccessDevice_Name_Type()
)
mediaAccessDevice_Name.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mediaAccessDevice_Name.setStatus("mandatory")


class _MediaAccessDevice_Status_Type(DisplayString):
    """Custom type mediaAccessDevice_Status based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_MediaAccessDevice_Status_Type.__name__ = "DisplayString"
_MediaAccessDevice_Status_Object = MibTableColumn
mediaAccessDevice_Status = _MediaAccessDevice_Status_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 182, 3, 6, 2, 1, 4),
    _MediaAccessDevice_Status_Type()
)
mediaAccessDevice_Status.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mediaAccessDevice_Status.setStatus("mandatory")


class _MediaAccessDevice_Availability_Type(Integer32):
    """Custom type mediaAccessDevice_Availability based on Integer32"""
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
              15,
              16,
              17,
              18)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 0),
          ("other", 1),
          ("runningFullPower", 2),
          ("warning", 3),
          ("inTest", 4),
          ("notApplicable", 5),
          ("powerOff", 6),
          ("offLine", 7),
          ("offDuty", 8),
          ("degraded", 9),
          ("notInstalled", 10),
          ("installError", 11),
          ("powerSaveUnknown", 12),
          ("powerSaveLowPowerMode", 13),
          ("powerSaveStandby", 14),
          ("powerCycle", 15),
          ("powerSaveWarning", 16),
          ("paused", 17),
          ("notReady", 18))
    )


_MediaAccessDevice_Availability_Type.__name__ = "Integer32"
_MediaAccessDevice_Availability_Object = MibTableColumn
mediaAccessDevice_Availability = _MediaAccessDevice_Availability_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 182, 3, 6, 2, 1, 5),
    _MediaAccessDevice_Availability_Type()
)
mediaAccessDevice_Availability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mediaAccessDevice_Availability.setStatus("mandatory")


class _MediaAccessDevice_NeedsCleaning_Type(Integer32):
    """Custom type mediaAccessDevice_NeedsCleaning based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 0),
          ("true", 1),
          ("false", 2))
    )


_MediaAccessDevice_NeedsCleaning_Type.__name__ = "Integer32"
_MediaAccessDevice_NeedsCleaning_Object = MibTableColumn
mediaAccessDevice_NeedsCleaning = _MediaAccessDevice_NeedsCleaning_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 182, 3, 6, 2, 1, 6),
    _MediaAccessDevice_NeedsCleaning_Type()
)
mediaAccessDevice_NeedsCleaning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mediaAccessDevice_NeedsCleaning.setStatus("mandatory")
_PhysicalMediaGroup_ObjectIdentity = ObjectIdentity
physicalMediaGroup = _PhysicalMediaGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 182, 3, 7)
)
_NumberOfPhysicalMedias_Type = Integer32
_NumberOfPhysicalMedias_Object = MibScalar
numberOfPhysicalMedias = _NumberOfPhysicalMedias_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 182, 3, 7, 1),
    _NumberOfPhysicalMedias_Type()
)
numberOfPhysicalMedias.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    numberOfPhysicalMedias.setStatus("mandatory")
_PhysicalMediaTable_Object = MibTable
physicalMediaTable = _PhysicalMediaTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 182, 3, 7, 2)
)
if mibBuilder.loadTexts:
    physicalMediaTable.setStatus("mandatory")
_PhysicalMediaEntry_Object = MibTableRow
physicalMediaEntry = _PhysicalMediaEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 182, 3, 7, 2, 1)
)
physicalMediaEntry.setIndexNames(
    (0, "SML-MIB", "physicalMediaIndex"),
)
if mibBuilder.loadTexts:
    physicalMediaEntry.setStatus("mandatory")
_PhysicalMediaIndex_Type = UINT32
_PhysicalMediaIndex_Object = MibTableColumn
physicalMediaIndex = _PhysicalMediaIndex_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 182, 3, 7, 2, 1, 1),
    _PhysicalMediaIndex_Type()
)
physicalMediaIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    physicalMediaIndex.setStatus("mandatory")


class _PhysicalMediaObjectType_Type(Integer32):
    """Custom type physicalMediaObjectType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("tape", 0),
          ("other", 1))
    )


_PhysicalMediaObjectType_Type.__name__ = "Integer32"
_PhysicalMediaObjectType_Object = MibTableColumn
physicalMediaObjectType = _PhysicalMediaObjectType_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 182, 3, 7, 2, 1, 2),
    _PhysicalMediaObjectType_Type()
)
physicalMediaObjectType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    physicalMediaObjectType.setStatus("mandatory")


class _PhysicalMedia_Removable_Type(Integer32):
    """Custom type physicalMedia_Removable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 0),
          ("true", 1),
          ("false", 2))
    )


_PhysicalMedia_Removable_Type.__name__ = "Integer32"
_PhysicalMedia_Removable_Object = MibTableColumn
physicalMedia_Removable = _PhysicalMedia_Removable_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 182, 3, 7, 2, 1, 3),
    _PhysicalMedia_Removable_Type()
)
physicalMedia_Removable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    physicalMedia_Removable.setStatus("mandatory")


class _PhysicalMedia_Replaceable_Type(Integer32):
    """Custom type physicalMedia_Replaceable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 0),
          ("true", 1),
          ("false", 2))
    )


_PhysicalMedia_Replaceable_Type.__name__ = "Integer32"
_PhysicalMedia_Replaceable_Object = MibTableColumn
physicalMedia_Replaceable = _PhysicalMedia_Replaceable_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 182, 3, 7, 2, 1, 4),
    _PhysicalMedia_Replaceable_Type()
)
physicalMedia_Replaceable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    physicalMedia_Replaceable.setStatus("mandatory")


class _PhysicalMedia_HotSwappable_Type(Integer32):
    """Custom type physicalMedia_HotSwappable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 0),
          ("true", 1),
          ("false", 2))
    )


_PhysicalMedia_HotSwappable_Type.__name__ = "Integer32"
_PhysicalMedia_HotSwappable_Object = MibTableColumn
physicalMedia_HotSwappable = _PhysicalMedia_HotSwappable_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 182, 3, 7, 2, 1, 5),
    _PhysicalMedia_HotSwappable_Type()
)
physicalMedia_HotSwappable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    physicalMedia_HotSwappable.setStatus("mandatory")
_PhysicalMedia_Capacity_Type = UINT64
_PhysicalMedia_Capacity_Object = MibTableColumn
physicalMedia_Capacity = _PhysicalMedia_Capacity_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 182, 3, 7, 2, 1, 6),
    _PhysicalMedia_Capacity_Type()
)
physicalMedia_Capacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    physicalMedia_Capacity.setStatus("mandatory")


class _PhysicalMedia_MediaType_Type(Integer32):
    """Custom type physicalMedia_MediaType based on Integer32"""
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
              15,
              16,
              17,
              18,
              19,
              20,
              21,
              22,
              23,
              24,
              25,
              26,
              27,
              28,
              29,
              30,
              31,
              32,
              33,
              34,
              35,
              36,
              37,
              38,
              39,
              40,
              41,
              42,
              43,
              44,
              45,
              46,
              47,
              48,
              49,
              50,
              51,
              52,
              53,
              54,
              55,
              56,
              57,
              58,
              59)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 0),
          ("other", 1),
          ("tape", 2),
          ("qic", 3),
          ("ait", 4),
          ("dtf", 5),
          ("dat", 6),
          ("eightmmTape", 7),
          ("nineteenmmTape", 8),
          ("dlt", 9),
          ("halfInchMO", 10),
          ("catridgeDisk", 11),
          ("jazDisk", 12),
          ("zipDisk", 13),
          ("syQuestDisk", 14),
          ("winchesterDisk", 15),
          ("cdRom", 16),
          ("cdRomXA", 17),
          ("cdI", 18),
          ("cdRecordable", 19),
          ("dvd", 20),
          ("dvdRWPlus", 21),
          ("dvdRAM", 22),
          ("dvdROM", 23),
          ("dvdVideo", 24),
          ("divx", 25),
          ("cdRW", 26),
          ("cdDA", 27),
          ("cdPlus", 28),
          ("dvdRecordable", 29),
          ("dvdRW", 30),
          ("dvdAudio", 31),
          ("dvd5", 32),
          ("dvd9", 33),
          ("dvd10", 34),
          ("dvd18", 35),
          ("moRewriteable", 36),
          ("moWriteOnce", 37),
          ("moLIMDOW", 38),
          ("phaseChangeWO", 39),
          ("phaseChangeRewriteable", 40),
          ("phaseChangeDualRewriteable", 41),
          ("ablativeWriteOnce", 42),
          ("nearField", 43),
          ("miniQic", 44),
          ("travan", 45),
          ("eightmmMetal", 46),
          ("eightmmAdvanced", 47),
          ("nctp", 48),
          ("ltoUltrium", 49),
          ("ltoAccelis", 50),
          ("tape9Track", 51),
          ("tape18Track", 52),
          ("tape36Track", 53),
          ("magstar3590", 54),
          ("magstarMP", 55),
          ("d2Tape", 56),
          ("dstSmall", 57),
          ("dstMedium", 58),
          ("dstLarge", 59))
    )


_PhysicalMedia_MediaType_Type.__name__ = "Integer32"
_PhysicalMedia_MediaType_Object = MibTableColumn
physicalMedia_MediaType = _PhysicalMedia_MediaType_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 182, 3, 7, 2, 1, 7),
    _PhysicalMedia_MediaType_Type()
)
physicalMedia_MediaType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    physicalMedia_MediaType.setStatus("mandatory")


class _PhysicalMedia_MediaDescription_Type(DisplayString):
    """Custom type physicalMedia_MediaDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_PhysicalMedia_MediaDescription_Type.__name__ = "DisplayString"
_PhysicalMedia_MediaDescription_Object = MibTableColumn
physicalMedia_MediaDescription = _PhysicalMedia_MediaDescription_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 182, 3, 7, 2, 1, 8),
    _PhysicalMedia_MediaDescription_Type()
)
physicalMedia_MediaDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    physicalMedia_MediaDescription.setStatus("mandatory")


class _PhysicalMedia_CleanerMedia_Type(Integer32):
    """Custom type physicalMedia_CleanerMedia based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 0),
          ("true", 1),
          ("false", 2))
    )


_PhysicalMedia_CleanerMedia_Type.__name__ = "Integer32"
_PhysicalMedia_CleanerMedia_Object = MibTableColumn
physicalMedia_CleanerMedia = _PhysicalMedia_CleanerMedia_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 182, 3, 7, 2, 1, 9),
    _PhysicalMedia_CleanerMedia_Type()
)
physicalMedia_CleanerMedia.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    physicalMedia_CleanerMedia.setStatus("mandatory")


class _PhysicalMedia_DualSided_Type(Integer32):
    """Custom type physicalMedia_DualSided based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 0),
          ("true", 1),
          ("false", 2))
    )


_PhysicalMedia_DualSided_Type.__name__ = "Integer32"
_PhysicalMedia_DualSided_Object = MibTableColumn
physicalMedia_DualSided = _PhysicalMedia_DualSided_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 182, 3, 7, 2, 1, 10),
    _PhysicalMedia_DualSided_Type()
)
physicalMedia_DualSided.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    physicalMedia_DualSided.setStatus("mandatory")


class _PhysicalMedia_PhysicalLabel_Type(DisplayString):
    """Custom type physicalMedia_PhysicalLabel based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_PhysicalMedia_PhysicalLabel_Type.__name__ = "DisplayString"
_PhysicalMedia_PhysicalLabel_Object = MibTableColumn
physicalMedia_PhysicalLabel = _PhysicalMedia_PhysicalLabel_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 182, 3, 7, 2, 1, 11),
    _PhysicalMedia_PhysicalLabel_Type()
)
physicalMedia_PhysicalLabel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    physicalMedia_PhysicalLabel.setStatus("mandatory")
_PhysicalPackageGroup_ObjectIdentity = ObjectIdentity
physicalPackageGroup = _PhysicalPackageGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 182, 3, 8)
)
_NumberOfPhysicalPackages_Type = Integer32
_NumberOfPhysicalPackages_Object = MibScalar
numberOfPhysicalPackages = _NumberOfPhysicalPackages_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 182, 3, 8, 1),
    _NumberOfPhysicalPackages_Type()
)
numberOfPhysicalPackages.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    numberOfPhysicalPackages.setStatus("mandatory")
_PhysicalPackageTable_Object = MibTable
physicalPackageTable = _PhysicalPackageTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 182, 3, 8, 2)
)
if mibBuilder.loadTexts:
    physicalPackageTable.setStatus("mandatory")
_PhysicalPackageEntry_Object = MibTableRow
physicalPackageEntry = _PhysicalPackageEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 182, 3, 8, 2, 1)
)
physicalPackageEntry.setIndexNames(
    (0, "SML-MIB", "physicalPackageIndex"),
)
if mibBuilder.loadTexts:
    physicalPackageEntry.setStatus("mandatory")
_PhysicalPackageIndex_Type = UINT32
_PhysicalPackageIndex_Object = MibTableColumn
physicalPackageIndex = _PhysicalPackageIndex_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 182, 3, 8, 2, 1, 1),
    _PhysicalPackageIndex_Type()
)
physicalPackageIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    physicalPackageIndex.setStatus("mandatory")


class _PhysicalPackage_Manufacturer_Type(DisplayString):
    """Custom type physicalPackage_Manufacturer based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_PhysicalPackage_Manufacturer_Type.__name__ = "DisplayString"
_PhysicalPackage_Manufacturer_Object = MibTableColumn
physicalPackage_Manufacturer = _PhysicalPackage_Manufacturer_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 182, 3, 8, 2, 1, 2),
    _PhysicalPackage_Manufacturer_Type()
)
physicalPackage_Manufacturer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    physicalPackage_Manufacturer.setStatus("mandatory")


class _PhysicalPackage_Model_Type(DisplayString):
    """Custom type physicalPackage_Model based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_PhysicalPackage_Model_Type.__name__ = "DisplayString"
_PhysicalPackage_Model_Object = MibTableColumn
physicalPackage_Model = _PhysicalPackage_Model_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 182, 3, 8, 2, 1, 3),
    _PhysicalPackage_Model_Type()
)
physicalPackage_Model.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    physicalPackage_Model.setStatus("mandatory")


class _PhysicalPackage_SerialNumber_Type(DisplayString):
    """Custom type physicalPackage_SerialNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_PhysicalPackage_SerialNumber_Type.__name__ = "DisplayString"
_PhysicalPackage_SerialNumber_Object = MibTableColumn
physicalPackage_SerialNumber = _PhysicalPackage_SerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 182, 3, 8, 2, 1, 4),
    _PhysicalPackage_SerialNumber_Type()
)
physicalPackage_SerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    physicalPackage_SerialNumber.setStatus("mandatory")
_PhysicalPackage_Realizes_MediaAccessDeviceIndex_Type = Integer32
_PhysicalPackage_Realizes_MediaAccessDeviceIndex_Object = MibTableColumn
physicalPackage_Realizes_MediaAccessDeviceIndex = _PhysicalPackage_Realizes_MediaAccessDeviceIndex_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 182, 3, 8, 2, 1, 5),
    _PhysicalPackage_Realizes_MediaAccessDeviceIndex_Type()
)
physicalPackage_Realizes_MediaAccessDeviceIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    physicalPackage_Realizes_MediaAccessDeviceIndex.setStatus("mandatory")
_SoftwareElementGroup_ObjectIdentity = ObjectIdentity
softwareElementGroup = _SoftwareElementGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 182, 3, 9)
)
_NumberOfSoftwareElements_Type = Integer32
_NumberOfSoftwareElements_Object = MibScalar
numberOfSoftwareElements = _NumberOfSoftwareElements_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 182, 3, 9, 1),
    _NumberOfSoftwareElements_Type()
)
numberOfSoftwareElements.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    numberOfSoftwareElements.setStatus("mandatory")
_SoftwareElementTable_Object = MibTable
softwareElementTable = _SoftwareElementTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 182, 3, 9, 2)
)
if mibBuilder.loadTexts:
    softwareElementTable.setStatus("mandatory")
_SoftwareElementEntry_Object = MibTableRow
softwareElementEntry = _SoftwareElementEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 182, 3, 9, 2, 1)
)
softwareElementEntry.setIndexNames(
    (0, "SML-MIB", "softwareElementIndex"),
)
if mibBuilder.loadTexts:
    softwareElementEntry.setStatus("mandatory")
_SoftwareElementIndex_Type = UINT32
_SoftwareElementIndex_Object = MibTableColumn
softwareElementIndex = _SoftwareElementIndex_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 182, 3, 9, 2, 1, 1),
    _SoftwareElementIndex_Type()
)
softwareElementIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    softwareElementIndex.setStatus("mandatory")


class _SoftwareElement_Name_Type(DisplayString):
    """Custom type softwareElement_Name based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SoftwareElement_Name_Type.__name__ = "DisplayString"
_SoftwareElement_Name_Object = MibTableColumn
softwareElement_Name = _SoftwareElement_Name_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 182, 3, 9, 2, 1, 2),
    _SoftwareElement_Name_Type()
)
softwareElement_Name.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    softwareElement_Name.setStatus("mandatory")


class _SoftwareElement_Version_Type(DisplayString):
    """Custom type softwareElement_Version based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SoftwareElement_Version_Type.__name__ = "DisplayString"
_SoftwareElement_Version_Object = MibTableColumn
softwareElement_Version = _SoftwareElement_Version_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 182, 3, 9, 2, 1, 3),
    _SoftwareElement_Version_Type()
)
softwareElement_Version.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    softwareElement_Version.setStatus("mandatory")


class _SoftwareElement_SoftwareElementID_Type(DisplayString):
    """Custom type softwareElement_SoftwareElementID based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SoftwareElement_SoftwareElementID_Type.__name__ = "DisplayString"
_SoftwareElement_SoftwareElementID_Object = MibTableColumn
softwareElement_SoftwareElementID = _SoftwareElement_SoftwareElementID_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 182, 3, 9, 2, 1, 4),
    _SoftwareElement_SoftwareElementID_Type()
)
softwareElement_SoftwareElementID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    softwareElement_SoftwareElementID.setStatus("mandatory")


class _SoftwareElement_Manufacturer_Type(DisplayString):
    """Custom type softwareElement_Manufacturer based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_SoftwareElement_Manufacturer_Type.__name__ = "DisplayString"
_SoftwareElement_Manufacturer_Object = MibTableColumn
softwareElement_Manufacturer = _SoftwareElement_Manufacturer_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 182, 3, 9, 2, 1, 5),
    _SoftwareElement_Manufacturer_Type()
)
softwareElement_Manufacturer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    softwareElement_Manufacturer.setStatus("mandatory")


class _SoftwareElement_BuildNumber_Type(DisplayString):
    """Custom type softwareElement_BuildNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_SoftwareElement_BuildNumber_Type.__name__ = "DisplayString"
_SoftwareElement_BuildNumber_Object = MibTableColumn
softwareElement_BuildNumber = _SoftwareElement_BuildNumber_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 182, 3, 9, 2, 1, 6),
    _SoftwareElement_BuildNumber_Type()
)
softwareElement_BuildNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    softwareElement_BuildNumber.setStatus("mandatory")


class _SoftwareElement_SerialNumber_Type(DisplayString):
    """Custom type softwareElement_SerialNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_SoftwareElement_SerialNumber_Type.__name__ = "DisplayString"
_SoftwareElement_SerialNumber_Object = MibTableColumn
softwareElement_SerialNumber = _SoftwareElement_SerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 182, 3, 9, 2, 1, 7),
    _SoftwareElement_SerialNumber_Type()
)
softwareElement_SerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    softwareElement_SerialNumber.setStatus("mandatory")


class _SoftwareElement_CodeSet_Type(DisplayString):
    """Custom type softwareElement_CodeSet based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_SoftwareElement_CodeSet_Type.__name__ = "DisplayString"
_SoftwareElement_CodeSet_Object = MibTableColumn
softwareElement_CodeSet = _SoftwareElement_CodeSet_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 182, 3, 9, 2, 1, 8),
    _SoftwareElement_CodeSet_Type()
)
softwareElement_CodeSet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    softwareElement_CodeSet.setStatus("mandatory")


class _SoftwareElement_IdentificationCode_Type(DisplayString):
    """Custom type softwareElement_IdentificationCode based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_SoftwareElement_IdentificationCode_Type.__name__ = "DisplayString"
_SoftwareElement_IdentificationCode_Object = MibTableColumn
softwareElement_IdentificationCode = _SoftwareElement_IdentificationCode_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 182, 3, 9, 2, 1, 9),
    _SoftwareElement_IdentificationCode_Type()
)
softwareElement_IdentificationCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    softwareElement_IdentificationCode.setStatus("mandatory")


class _SoftwareElement_LanguageEdition_Type(DisplayString):
    """Custom type softwareElement_LanguageEdition based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_SoftwareElement_LanguageEdition_Type.__name__ = "DisplayString"
_SoftwareElement_LanguageEdition_Object = MibTableColumn
softwareElement_LanguageEdition = _SoftwareElement_LanguageEdition_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 182, 3, 9, 2, 1, 10),
    _SoftwareElement_LanguageEdition_Type()
)
softwareElement_LanguageEdition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    softwareElement_LanguageEdition.setStatus("mandatory")
_SoftwareElement_Associations_Type = ObjectIdentifier
_SoftwareElement_Associations_Object = MibTableColumn
softwareElement_Associations = _SoftwareElement_Associations_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 182, 3, 9, 2, 1, 11),
    _SoftwareElement_Associations_Type()
)
softwareElement_Associations.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    softwareElement_Associations.setStatus("mandatory")


class _SoftwareElement_DeviceSoftware_LogicalDeviceAssociation_ObjectT_Type(Integer32):
    """Custom type softwareElement_DeviceSoftware_LogicalDeviceAssociation_ObjectT based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("mediaAccessDevice", 0),
          ("storageLibrary", 1),
          ("other", 2))
    )


_SoftwareElement_DeviceSoftware_LogicalDeviceAssociation_ObjectT_Type.__name__ = "Integer32"
_SoftwareElement_DeviceSoftware_LogicalDeviceAssociation_ObjectT_Object = MibTableColumn
softwareElement_DeviceSoftware_LogicalDeviceAssociation_ObjectT = _SoftwareElement_DeviceSoftware_LogicalDeviceAssociation_ObjectT_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 182, 3, 9, 2, 1, 12),
    _SoftwareElement_DeviceSoftware_LogicalDeviceAssociation_ObjectT_Type()
)
softwareElement_DeviceSoftware_LogicalDeviceAssociation_ObjectT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    softwareElement_DeviceSoftware_LogicalDeviceAssociation_ObjectT.setStatus("mandatory")
_SoftwareElement_DeviceSoftware_LogicalDeviceAssociationId_Type = Integer32
_SoftwareElement_DeviceSoftware_LogicalDeviceAssociationId_Object = MibTableColumn
softwareElement_DeviceSoftware_LogicalDeviceAssociationId = _SoftwareElement_DeviceSoftware_LogicalDeviceAssociationId_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 182, 3, 9, 2, 1, 13),
    _SoftwareElement_DeviceSoftware_LogicalDeviceAssociationId_Type()
)
softwareElement_DeviceSoftware_LogicalDeviceAssociationId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    softwareElement_DeviceSoftware_LogicalDeviceAssociationId.setStatus("mandatory")
_EndOfSmlMib_Type = ObjectIdentifier
_EndOfSmlMib_Object = MibScalar
endOfSmlMib = _EndOfSmlMib_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 182, 3, 10),
    _EndOfSmlMib_Type()
)
endOfSmlMib.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    endOfSmlMib.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SML-MIB",
    **{"UShortReal": UShortReal,
       "CimDateTime": CimDateTime,
       "UINT64": UINT64,
       "UINT32": UINT32,
       "UINT16": UINT16,
       "ibm": ibm,
       "ibmProd": ibmProd,
       "ibm3584": ibm3584,
       "smlRoot": smlRoot,
       "smlMibVersion": smlMibVersion,
       "smlCimVersion": smlCimVersion,
       "productGroup": productGroup,
       "product-Name": product_Name,
       "product-IdentifyingNumber": product_IdentifyingNumber,
       "product-Vendor": product_Vendor,
       "product-Version": product_Version,
       "chassisGroup": chassisGroup,
       "chassis-Manufacturer": chassis_Manufacturer,
       "chassis-Model": chassis_Model,
       "chassis-SerialNumber": chassis_SerialNumber,
       "chassis-LockPresent": chassis_LockPresent,
       "chassis-SecurityBreach": chassis_SecurityBreach,
       "chassis-IsLocked": chassis_IsLocked,
       "storageLibraryGroup": storageLibraryGroup,
       "storageLibrary-Name": storageLibrary_Name,
       "storageLibrary-Description": storageLibrary_Description,
       "storageLibrary-Caption": storageLibrary_Caption,
       "storageLibrary-Status": storageLibrary_Status,
       "storageLibrary-InstallDate": storageLibrary_InstallDate,
       "mediaAccessDeviceGroup": mediaAccessDeviceGroup,
       "numberOfMediaAccessDevices": numberOfMediaAccessDevices,
       "mediaAccessDeviceTable": mediaAccessDeviceTable,
       "mediaAccessDeviceEntry": mediaAccessDeviceEntry,
       "mediaAccessDeviceIndex": mediaAccessDeviceIndex,
       "mediaAccessDeviceObjectType": mediaAccessDeviceObjectType,
       "mediaAccessDevice-Name": mediaAccessDevice_Name,
       "mediaAccessDevice-Status": mediaAccessDevice_Status,
       "mediaAccessDevice-Availability": mediaAccessDevice_Availability,
       "mediaAccessDevice-NeedsCleaning": mediaAccessDevice_NeedsCleaning,
       "physicalMediaGroup": physicalMediaGroup,
       "numberOfPhysicalMedias": numberOfPhysicalMedias,
       "physicalMediaTable": physicalMediaTable,
       "physicalMediaEntry": physicalMediaEntry,
       "physicalMediaIndex": physicalMediaIndex,
       "physicalMediaObjectType": physicalMediaObjectType,
       "physicalMedia-Removable": physicalMedia_Removable,
       "physicalMedia-Replaceable": physicalMedia_Replaceable,
       "physicalMedia-HotSwappable": physicalMedia_HotSwappable,
       "physicalMedia-Capacity": physicalMedia_Capacity,
       "physicalMedia-MediaType": physicalMedia_MediaType,
       "physicalMedia-MediaDescription": physicalMedia_MediaDescription,
       "physicalMedia-CleanerMedia": physicalMedia_CleanerMedia,
       "physicalMedia-DualSided": physicalMedia_DualSided,
       "physicalMedia-PhysicalLabel": physicalMedia_PhysicalLabel,
       "physicalPackageGroup": physicalPackageGroup,
       "numberOfPhysicalPackages": numberOfPhysicalPackages,
       "physicalPackageTable": physicalPackageTable,
       "physicalPackageEntry": physicalPackageEntry,
       "physicalPackageIndex": physicalPackageIndex,
       "physicalPackage-Manufacturer": physicalPackage_Manufacturer,
       "physicalPackage-Model": physicalPackage_Model,
       "physicalPackage-SerialNumber": physicalPackage_SerialNumber,
       "physicalPackage-Realizes-MediaAccessDeviceIndex": physicalPackage_Realizes_MediaAccessDeviceIndex,
       "softwareElementGroup": softwareElementGroup,
       "numberOfSoftwareElements": numberOfSoftwareElements,
       "softwareElementTable": softwareElementTable,
       "softwareElementEntry": softwareElementEntry,
       "softwareElementIndex": softwareElementIndex,
       "softwareElement-Name": softwareElement_Name,
       "softwareElement-Version": softwareElement_Version,
       "softwareElement-SoftwareElementID": softwareElement_SoftwareElementID,
       "softwareElement-Manufacturer": softwareElement_Manufacturer,
       "softwareElement-BuildNumber": softwareElement_BuildNumber,
       "softwareElement-SerialNumber": softwareElement_SerialNumber,
       "softwareElement-CodeSet": softwareElement_CodeSet,
       "softwareElement-IdentificationCode": softwareElement_IdentificationCode,
       "softwareElement-LanguageEdition": softwareElement_LanguageEdition,
       "softwareElement-Associations": softwareElement_Associations,
       "softwareElement-DeviceSoftware-LogicalDeviceAssociation-ObjectT": softwareElement_DeviceSoftware_LogicalDeviceAssociation_ObjectT,
       "softwareElement-DeviceSoftware-LogicalDeviceAssociationId": softwareElement_DeviceSoftware_LogicalDeviceAssociationId,
       "endOfSmlMib": endOfSmlMib}
)
