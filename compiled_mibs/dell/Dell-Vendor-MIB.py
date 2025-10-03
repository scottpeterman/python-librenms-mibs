# SNMP MIB module (Dell-Vendor-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\dell\Dell-Vendor-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:35:30 2025
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
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

powerConnectVendorMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10895, 3000)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class EnvMonState(TextualConvention, Integer32):
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
        *(("normal", 1),
          ("warning", 2),
          ("critical", 3),
          ("shutdown", 4),
          ("notPresent", 5),
          ("notFunctioning", 6))
    )



# MIB Managed Objects in the order of their OIDs

_Dell_ObjectIdentity = ObjectIdentity
dell = _Dell_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674)
)
_DellLan_ObjectIdentity = ObjectIdentity
dellLan = _DellLan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10895)
)
_DellVendorMIBObjects_ObjectIdentity = ObjectIdentity
dellVendorMIBObjects = _DellVendorMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10895, 3000, 1)
)
_Hardware_ObjectIdentity = ObjectIdentity
hardware = _Hardware_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10895, 3000, 1, 2)
)
_ProductIdentification_ObjectIdentity = ObjectIdentity
productIdentification = _ProductIdentification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10895, 3000, 1, 2, 100)
)
_ProductIdentificationDisplayName_Type = DisplayString
_ProductIdentificationDisplayName_Object = MibScalar
productIdentificationDisplayName = _ProductIdentificationDisplayName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 3000, 1, 2, 100, 1),
    _ProductIdentificationDisplayName_Type()
)
productIdentificationDisplayName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    productIdentificationDisplayName.setStatus("current")
_ProductIdentificationDescription_Type = DisplayString
_ProductIdentificationDescription_Object = MibScalar
productIdentificationDescription = _ProductIdentificationDescription_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 3000, 1, 2, 100, 2),
    _ProductIdentificationDescription_Type()
)
productIdentificationDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    productIdentificationDescription.setStatus("current")
_ProductIdentificationVendor_Type = DisplayString
_ProductIdentificationVendor_Object = MibScalar
productIdentificationVendor = _ProductIdentificationVendor_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 3000, 1, 2, 100, 3),
    _ProductIdentificationVendor_Type()
)
productIdentificationVendor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    productIdentificationVendor.setStatus("current")
_ProductIdentificationVersion_Type = DisplayString
_ProductIdentificationVersion_Object = MibScalar
productIdentificationVersion = _ProductIdentificationVersion_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 3000, 1, 2, 100, 4),
    _ProductIdentificationVersion_Type()
)
productIdentificationVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    productIdentificationVersion.setStatus("current")
_ProductIdentificationBuildNumber_Type = DisplayString
_ProductIdentificationBuildNumber_Object = MibScalar
productIdentificationBuildNumber = _ProductIdentificationBuildNumber_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 3000, 1, 2, 100, 5),
    _ProductIdentificationBuildNumber_Type()
)
productIdentificationBuildNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    productIdentificationBuildNumber.setStatus("current")
_ProductIdentificationURL_Type = DisplayString
_ProductIdentificationURL_Object = MibScalar
productIdentificationURL = _ProductIdentificationURL_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 3000, 1, 2, 100, 6),
    _ProductIdentificationURL_Type()
)
productIdentificationURL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    productIdentificationURL.setStatus("current")
_ProductIdentificationDeviceNetworkName_Type = DisplayString
_ProductIdentificationDeviceNetworkName_Object = MibScalar
productIdentificationDeviceNetworkName = _ProductIdentificationDeviceNetworkName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 3000, 1, 2, 100, 7),
    _ProductIdentificationDeviceNetworkName_Type()
)
productIdentificationDeviceNetworkName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    productIdentificationDeviceNetworkName.setStatus("current")
_ProductIdentificationPerUnitTable_Object = MibTable
productIdentificationPerUnitTable = _ProductIdentificationPerUnitTable_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 3000, 1, 2, 100, 8)
)
if mibBuilder.loadTexts:
    productIdentificationPerUnitTable.setStatus("current")
_ProductIdentificationPerUnitEntry_Object = MibTableRow
productIdentificationPerUnitEntry = _ProductIdentificationPerUnitEntry_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 3000, 1, 2, 100, 8, 1)
)
productIdentificationPerUnitEntry.setIndexNames(
    (0, "Dell-Vendor-MIB", "productIdentificationPerBoxIndex"),
)
if mibBuilder.loadTexts:
    productIdentificationPerUnitEntry.setStatus("current")


class _ProductIdentificationPerBoxIndex_Type(Integer32):
    """Custom type productIdentificationPerBoxIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_ProductIdentificationPerBoxIndex_Type.__name__ = "Integer32"
_ProductIdentificationPerBoxIndex_Object = MibTableColumn
productIdentificationPerBoxIndex = _ProductIdentificationPerBoxIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 3000, 1, 2, 100, 8, 1, 1),
    _ProductIdentificationPerBoxIndex_Type()
)
productIdentificationPerBoxIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    productIdentificationPerBoxIndex.setStatus("current")
_ProductIdentificationSerialNumber_Type = DisplayString
_ProductIdentificationSerialNumber_Object = MibTableColumn
productIdentificationSerialNumber = _ProductIdentificationSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 3000, 1, 2, 100, 8, 1, 2),
    _ProductIdentificationSerialNumber_Type()
)
productIdentificationSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    productIdentificationSerialNumber.setStatus("current")
_ProductIdentificationAssetTag_Type = DisplayString
_ProductIdentificationAssetTag_Object = MibTableColumn
productIdentificationAssetTag = _ProductIdentificationAssetTag_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 3000, 1, 2, 100, 8, 1, 3),
    _ProductIdentificationAssetTag_Type()
)
productIdentificationAssetTag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    productIdentificationAssetTag.setStatus("current")
_ProductIdentificationServiceTag_Type = DisplayString
_ProductIdentificationServiceTag_Object = MibTableColumn
productIdentificationServiceTag = _ProductIdentificationServiceTag_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 3000, 1, 2, 100, 8, 1, 4),
    _ProductIdentificationServiceTag_Type()
)
productIdentificationServiceTag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    productIdentificationServiceTag.setStatus("current")
_ProductIdentificationBootromVersion_Type = DisplayString
_ProductIdentificationBootromVersion_Object = MibTableColumn
productIdentificationBootromVersion = _ProductIdentificationBootromVersion_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 3000, 1, 2, 100, 8, 1, 6),
    _ProductIdentificationBootromVersion_Type()
)
productIdentificationBootromVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    productIdentificationBootromVersion.setStatus("current")


class _ProductIdentificationBannerMotd_Type(DisplayString):
    """Custom type productIdentificationBannerMotd based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 1500),
    )


_ProductIdentificationBannerMotd_Type.__name__ = "DisplayString"
_ProductIdentificationBannerMotd_Object = MibScalar
productIdentificationBannerMotd = _ProductIdentificationBannerMotd_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 3000, 1, 2, 100, 9),
    _ProductIdentificationBannerMotd_Type()
)
productIdentificationBannerMotd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    productIdentificationBannerMotd.setStatus("current")


class _ProductIdentificationBannerMotdAckMode_Type(Integer32):
    """Custom type productIdentificationBannerMotdAckMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_ProductIdentificationBannerMotdAckMode_Type.__name__ = "Integer32"
_ProductIdentificationBannerMotdAckMode_Object = MibScalar
productIdentificationBannerMotdAckMode = _ProductIdentificationBannerMotdAckMode_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 3000, 1, 2, 100, 10),
    _ProductIdentificationBannerMotdAckMode_Type()
)
productIdentificationBannerMotdAckMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    productIdentificationBannerMotdAckMode.setStatus("current")
_ProductStatus_ObjectIdentity = ObjectIdentity
productStatus = _ProductStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10895, 3000, 1, 2, 110)
)


class _ProductStatusGlobalStatus_Type(Integer32):
    """Custom type productStatusGlobalStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("ok", 3),
          ("non-critical", 4),
          ("critical", 5))
    )


_ProductStatusGlobalStatus_Type.__name__ = "Integer32"
_ProductStatusGlobalStatus_Object = MibScalar
productStatusGlobalStatus = _ProductStatusGlobalStatus_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 3000, 1, 2, 110, 1),
    _ProductStatusGlobalStatus_Type()
)
productStatusGlobalStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    productStatusGlobalStatus.setStatus("current")


class _ProductStatusLastGlobalStatus_Type(Integer32):
    """Custom type productStatusLastGlobalStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("ok", 3),
          ("non-critical", 4),
          ("critical", 5))
    )


_ProductStatusLastGlobalStatus_Type.__name__ = "Integer32"
_ProductStatusLastGlobalStatus_Object = MibScalar
productStatusLastGlobalStatus = _ProductStatusLastGlobalStatus_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 3000, 1, 2, 110, 2),
    _ProductStatusLastGlobalStatus_Type()
)
productStatusLastGlobalStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    productStatusLastGlobalStatus.setStatus("current")
_ProductStatusTimeStamp_Type = TimeTicks
_ProductStatusTimeStamp_Object = MibScalar
productStatusTimeStamp = _ProductStatusTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 3000, 1, 2, 110, 3),
    _ProductStatusTimeStamp_Type()
)
productStatusTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    productStatusTimeStamp.setStatus("current")


class _ProductStatusGetTimeOut_Type(Integer32):
    """Custom type productStatusGetTimeOut based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000),
    )


_ProductStatusGetTimeOut_Type.__name__ = "Integer32"
_ProductStatusGetTimeOut_Object = MibScalar
productStatusGetTimeOut = _ProductStatusGetTimeOut_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 3000, 1, 2, 110, 4),
    _ProductStatusGetTimeOut_Type()
)
productStatusGetTimeOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    productStatusGetTimeOut.setStatus("current")


class _ProductStatusRefreshRate_Type(Integer32):
    """Custom type productStatusRefreshRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_ProductStatusRefreshRate_Type.__name__ = "Integer32"
_ProductStatusRefreshRate_Object = MibScalar
productStatusRefreshRate = _ProductStatusRefreshRate_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 3000, 1, 2, 110, 5),
    _ProductStatusRefreshRate_Type()
)
productStatusRefreshRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    productStatusRefreshRate.setStatus("current")


class _ProductStatusGeneratingTrapsFlag_Type(Integer32):
    """Custom type productStatusGeneratingTrapsFlag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("true", 1),
          ("false", 2),
          ("disabled", 3))
    )


_ProductStatusGeneratingTrapsFlag_Type.__name__ = "Integer32"
_ProductStatusGeneratingTrapsFlag_Object = MibScalar
productStatusGeneratingTrapsFlag = _ProductStatusGeneratingTrapsFlag_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 3000, 1, 2, 110, 6),
    _ProductStatusGeneratingTrapsFlag_Type()
)
productStatusGeneratingTrapsFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    productStatusGeneratingTrapsFlag.setStatus("current")
_ProductStatusEnvironment_ObjectIdentity = ObjectIdentity
productStatusEnvironment = _ProductStatusEnvironment_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10895, 3000, 1, 2, 110, 7)
)
_EnvMonFanStatusTable_Object = MibTable
envMonFanStatusTable = _EnvMonFanStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 3000, 1, 2, 110, 7, 1)
)
if mibBuilder.loadTexts:
    envMonFanStatusTable.setStatus("current")
_EnvMonFanStatusEntry_Object = MibTableRow
envMonFanStatusEntry = _EnvMonFanStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 3000, 1, 2, 110, 7, 1, 1)
)
envMonFanStatusEntry.setIndexNames(
    (0, "Dell-Vendor-MIB", "envMonFanStatusIndex"),
)
if mibBuilder.loadTexts:
    envMonFanStatusEntry.setStatus("current")


class _EnvMonFanStatusIndex_Type(Integer32):
    """Custom type envMonFanStatusIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_EnvMonFanStatusIndex_Type.__name__ = "Integer32"
_EnvMonFanStatusIndex_Object = MibTableColumn
envMonFanStatusIndex = _EnvMonFanStatusIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 3000, 1, 2, 110, 7, 1, 1, 1),
    _EnvMonFanStatusIndex_Type()
)
envMonFanStatusIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    envMonFanStatusIndex.setStatus("current")


class _EnvMonFanStatusDescr_Type(DisplayString):
    """Custom type envMonFanStatusDescr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_EnvMonFanStatusDescr_Type.__name__ = "DisplayString"
_EnvMonFanStatusDescr_Object = MibTableColumn
envMonFanStatusDescr = _EnvMonFanStatusDescr_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 3000, 1, 2, 110, 7, 1, 1, 2),
    _EnvMonFanStatusDescr_Type()
)
envMonFanStatusDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    envMonFanStatusDescr.setStatus("current")
_EnvMonFanState_Type = EnvMonState
_EnvMonFanState_Object = MibTableColumn
envMonFanState = _EnvMonFanState_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 3000, 1, 2, 110, 7, 1, 1, 3),
    _EnvMonFanState_Type()
)
envMonFanState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    envMonFanState.setStatus("current")
_EnvMonSupplyStatusTable_Object = MibTable
envMonSupplyStatusTable = _EnvMonSupplyStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 3000, 1, 2, 110, 7, 2)
)
if mibBuilder.loadTexts:
    envMonSupplyStatusTable.setStatus("current")
_EnvMonSupplyStatusEntry_Object = MibTableRow
envMonSupplyStatusEntry = _EnvMonSupplyStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 3000, 1, 2, 110, 7, 2, 1)
)
envMonSupplyStatusEntry.setIndexNames(
    (0, "Dell-Vendor-MIB", "envMonSupplyStatusIndex"),
)
if mibBuilder.loadTexts:
    envMonSupplyStatusEntry.setStatus("current")


class _EnvMonSupplyStatusIndex_Type(Integer32):
    """Custom type envMonSupplyStatusIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_EnvMonSupplyStatusIndex_Type.__name__ = "Integer32"
_EnvMonSupplyStatusIndex_Object = MibTableColumn
envMonSupplyStatusIndex = _EnvMonSupplyStatusIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 3000, 1, 2, 110, 7, 2, 1, 1),
    _EnvMonSupplyStatusIndex_Type()
)
envMonSupplyStatusIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    envMonSupplyStatusIndex.setStatus("current")


class _EnvMonSupplyStatusDescr_Type(DisplayString):
    """Custom type envMonSupplyStatusDescr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_EnvMonSupplyStatusDescr_Type.__name__ = "DisplayString"
_EnvMonSupplyStatusDescr_Object = MibTableColumn
envMonSupplyStatusDescr = _EnvMonSupplyStatusDescr_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 3000, 1, 2, 110, 7, 2, 1, 2),
    _EnvMonSupplyStatusDescr_Type()
)
envMonSupplyStatusDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    envMonSupplyStatusDescr.setStatus("current")
_EnvMonSupplyState_Type = EnvMonState
_EnvMonSupplyState_Object = MibTableColumn
envMonSupplyState = _EnvMonSupplyState_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 3000, 1, 2, 110, 7, 2, 1, 3),
    _EnvMonSupplyState_Type()
)
envMonSupplyState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    envMonSupplyState.setStatus("current")


class _EnvMonSupplySource_Type(Integer32):
    """Custom type envMonSupplySource based on Integer32"""
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
          ("ac", 2),
          ("dc", 3),
          ("externalPowerSupply", 4),
          ("internalRedundant", 5))
    )


_EnvMonSupplySource_Type.__name__ = "Integer32"
_EnvMonSupplySource_Object = MibTableColumn
envMonSupplySource = _EnvMonSupplySource_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 3000, 1, 2, 110, 7, 2, 1, 4),
    _EnvMonSupplySource_Type()
)
envMonSupplySource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    envMonSupplySource.setStatus("current")
_DellVendorNotifications_ObjectIdentity = ObjectIdentity
dellVendorNotifications = _DellVendorNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10895, 3000, 2)
)
_DellVendorTraps_ObjectIdentity = ObjectIdentity
dellVendorTraps = _DellVendorTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10895, 3000, 2, 1)
)
_DellVendorTrapsPrefix_ObjectIdentity = ObjectIdentity
dellVendorTrapsPrefix = _DellVendorTrapsPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10895, 3000, 2, 1, 0)
)
_DellLanStandard_ObjectIdentity = ObjectIdentity
dellLanStandard = _DellLanStandard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000)
)
_DellLanCommon_ObjectIdentity = ObjectIdentity
dellLanCommon = _DellLanCommon_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 1)
)
_DellLanExtension_ObjectIdentity = ObjectIdentity
dellLanExtension = _DellLanExtension_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2)
)

# Managed Objects groups


# Notification objects

productStatusGlobalStatusChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10895, 3000, 2, 1, 0, 1)
)
productStatusGlobalStatusChange.setObjects(
      *(("Dell-Vendor-MIB", "productStatusGlobalStatus"),
        ("Dell-Vendor-MIB", "productStatusLastGlobalStatus"),
        ("Dell-Vendor-MIB", "productStatusTimeStamp"))
)
if mibBuilder.loadTexts:
    productStatusGlobalStatusChange.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Dell-Vendor-MIB",
    **{"EnvMonState": EnvMonState,
       "dell": dell,
       "dellLan": dellLan,
       "powerConnectVendorMIB": powerConnectVendorMIB,
       "dellVendorMIBObjects": dellVendorMIBObjects,
       "hardware": hardware,
       "productIdentification": productIdentification,
       "productIdentificationDisplayName": productIdentificationDisplayName,
       "productIdentificationDescription": productIdentificationDescription,
       "productIdentificationVendor": productIdentificationVendor,
       "productIdentificationVersion": productIdentificationVersion,
       "productIdentificationBuildNumber": productIdentificationBuildNumber,
       "productIdentificationURL": productIdentificationURL,
       "productIdentificationDeviceNetworkName": productIdentificationDeviceNetworkName,
       "productIdentificationPerUnitTable": productIdentificationPerUnitTable,
       "productIdentificationPerUnitEntry": productIdentificationPerUnitEntry,
       "productIdentificationPerBoxIndex": productIdentificationPerBoxIndex,
       "productIdentificationSerialNumber": productIdentificationSerialNumber,
       "productIdentificationAssetTag": productIdentificationAssetTag,
       "productIdentificationServiceTag": productIdentificationServiceTag,
       "productIdentificationBootromVersion": productIdentificationBootromVersion,
       "productIdentificationBannerMotd": productIdentificationBannerMotd,
       "productIdentificationBannerMotdAckMode": productIdentificationBannerMotdAckMode,
       "productStatus": productStatus,
       "productStatusGlobalStatus": productStatusGlobalStatus,
       "productStatusLastGlobalStatus": productStatusLastGlobalStatus,
       "productStatusTimeStamp": productStatusTimeStamp,
       "productStatusGetTimeOut": productStatusGetTimeOut,
       "productStatusRefreshRate": productStatusRefreshRate,
       "productStatusGeneratingTrapsFlag": productStatusGeneratingTrapsFlag,
       "productStatusEnvironment": productStatusEnvironment,
       "envMonFanStatusTable": envMonFanStatusTable,
       "envMonFanStatusEntry": envMonFanStatusEntry,
       "envMonFanStatusIndex": envMonFanStatusIndex,
       "envMonFanStatusDescr": envMonFanStatusDescr,
       "envMonFanState": envMonFanState,
       "envMonSupplyStatusTable": envMonSupplyStatusTable,
       "envMonSupplyStatusEntry": envMonSupplyStatusEntry,
       "envMonSupplyStatusIndex": envMonSupplyStatusIndex,
       "envMonSupplyStatusDescr": envMonSupplyStatusDescr,
       "envMonSupplyState": envMonSupplyState,
       "envMonSupplySource": envMonSupplySource,
       "dellVendorNotifications": dellVendorNotifications,
       "dellVendorTraps": dellVendorTraps,
       "dellVendorTrapsPrefix": dellVendorTrapsPrefix,
       "productStatusGlobalStatusChange": productStatusGlobalStatusChange,
       "dellLanStandard": dellLanStandard,
       "dellLanCommon": dellLanCommon,
       "dellLanExtension": dellLanExtension}
)
