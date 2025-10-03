# SNMP MIB module (ARUBAWIRED-SWITCH-IMAGE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\arubaos-cx\ARUBAWIRED-SWITCH-IMAGE-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:19:28 2025
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

(wndFeatures,) = mibBuilder.importSymbols(
    "ARUBAWIRED-NETWORKING-OID",
    "wndFeatures")

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

arubaWiredSwitchImage = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 26)
)
if mibBuilder.loadTexts:
    arubaWiredSwitchImage.setRevisions(
        ("2023-05-25 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_ArubaWiredSwitchImageObject_ObjectIdentity = ObjectIdentity
arubaWiredSwitchImageObject = _ArubaWiredSwitchImageObject_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 26, 1)
)
_ArubaWiredSwitchImageGeneral_ObjectIdentity = ObjectIdentity
arubaWiredSwitchImageGeneral = _ArubaWiredSwitchImageGeneral_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 26, 1, 0)
)
_ArubaWiredDefaultBoot_Type = DisplayString
_ArubaWiredDefaultBoot_Object = MibScalar
arubaWiredDefaultBoot = _ArubaWiredDefaultBoot_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 26, 1, 0, 1),
    _ArubaWiredDefaultBoot_Type()
)
arubaWiredDefaultBoot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arubaWiredDefaultBoot.setStatus("current")


class _ArubaWiredDefaultBootEnum_Type(Integer32):
    """Custom type arubaWiredDefaultBootEnum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("primary", 1),
          ("secondary", 2))
    )


_ArubaWiredDefaultBootEnum_Type.__name__ = "Integer32"
_ArubaWiredDefaultBootEnum_Object = MibScalar
arubaWiredDefaultBootEnum = _ArubaWiredDefaultBootEnum_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 26, 1, 0, 2),
    _ArubaWiredDefaultBootEnum_Type()
)
arubaWiredDefaultBootEnum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arubaWiredDefaultBootEnum.setStatus("current")


class _ArubaWiredBootProfileTimeout_Type(Integer32):
    """Custom type arubaWiredBootProfileTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 10),
    )


_ArubaWiredBootProfileTimeout_Type.__name__ = "Integer32"
_ArubaWiredBootProfileTimeout_Object = MibScalar
arubaWiredBootProfileTimeout = _ArubaWiredBootProfileTimeout_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 26, 1, 0, 3),
    _ArubaWiredBootProfileTimeout_Type()
)
arubaWiredBootProfileTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arubaWiredBootProfileTimeout.setStatus("current")
_ArubaWiredSwitchImageDetails_ObjectIdentity = ObjectIdentity
arubaWiredSwitchImageDetails = _ArubaWiredSwitchImageDetails_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 26, 1, 1)
)
_ArubaWiredSwitchImageTable_Object = MibTable
arubaWiredSwitchImageTable = _ArubaWiredSwitchImageTable_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 26, 1, 1, 1)
)
if mibBuilder.loadTexts:
    arubaWiredSwitchImageTable.setStatus("current")
_ArubaWiredSwitchImageEntry_Object = MibTableRow
arubaWiredSwitchImageEntry = _ArubaWiredSwitchImageEntry_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 26, 1, 1, 1, 1)
)
arubaWiredSwitchImageEntry.setIndexNames(
    (0, "ARUBAWIRED-SWITCH-IMAGE-MIB", "arubaWiredSwitchImageTypeEnum"),
)
if mibBuilder.loadTexts:
    arubaWiredSwitchImageEntry.setStatus("current")


class _ArubaWiredSwitchImageTypeEnum_Type(Integer32):
    """Custom type arubaWiredSwitchImageTypeEnum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("primary", 1),
          ("secondary", 2))
    )


_ArubaWiredSwitchImageTypeEnum_Type.__name__ = "Integer32"
_ArubaWiredSwitchImageTypeEnum_Object = MibTableColumn
arubaWiredSwitchImageTypeEnum = _ArubaWiredSwitchImageTypeEnum_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 26, 1, 1, 1, 1, 1),
    _ArubaWiredSwitchImageTypeEnum_Type()
)
arubaWiredSwitchImageTypeEnum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    arubaWiredSwitchImageTypeEnum.setStatus("current")
_ArubaWiredSwitchImageType_Type = DisplayString
_ArubaWiredSwitchImageType_Object = MibTableColumn
arubaWiredSwitchImageType = _ArubaWiredSwitchImageType_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 26, 1, 1, 1, 1, 2),
    _ArubaWiredSwitchImageType_Type()
)
arubaWiredSwitchImageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arubaWiredSwitchImageType.setStatus("current")
_ArubaWiredSwitchImageVersion_Type = DisplayString
_ArubaWiredSwitchImageVersion_Object = MibTableColumn
arubaWiredSwitchImageVersion = _ArubaWiredSwitchImageVersion_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 26, 1, 1, 1, 1, 3),
    _ArubaWiredSwitchImageVersion_Type()
)
arubaWiredSwitchImageVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arubaWiredSwitchImageVersion.setStatus("current")
_ArubaWiredSwitchImageSize_Type = DisplayString
_ArubaWiredSwitchImageSize_Object = MibTableColumn
arubaWiredSwitchImageSize = _ArubaWiredSwitchImageSize_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 26, 1, 1, 1, 1, 4),
    _ArubaWiredSwitchImageSize_Type()
)
arubaWiredSwitchImageSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arubaWiredSwitchImageSize.setStatus("current")
_ArubaWiredSwitchImageBuildDate_Type = DisplayString
_ArubaWiredSwitchImageBuildDate_Object = MibTableColumn
arubaWiredSwitchImageBuildDate = _ArubaWiredSwitchImageBuildDate_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 26, 1, 1, 1, 1, 5),
    _ArubaWiredSwitchImageBuildDate_Type()
)
arubaWiredSwitchImageBuildDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arubaWiredSwitchImageBuildDate.setStatus("current")
_ArubaWiredSwitchImageSha_Type = DisplayString
_ArubaWiredSwitchImageSha_Object = MibTableColumn
arubaWiredSwitchImageSha = _ArubaWiredSwitchImageSha_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 26, 1, 1, 1, 1, 6),
    _ArubaWiredSwitchImageSha_Type()
)
arubaWiredSwitchImageSha.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arubaWiredSwitchImageSha.setStatus("current")
_ArubaWiredSwitchImageConformance_ObjectIdentity = ObjectIdentity
arubaWiredSwitchImageConformance = _ArubaWiredSwitchImageConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 26, 2)
)
_ArubaWiredSwitchImageGroups_ObjectIdentity = ObjectIdentity
arubaWiredSwitchImageGroups = _ArubaWiredSwitchImageGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 26, 2, 1)
)
_ArubaWiredSwitchImageCompliances_ObjectIdentity = ObjectIdentity
arubaWiredSwitchImageCompliances = _ArubaWiredSwitchImageCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 26, 2, 2)
)

# Managed Objects groups

arubaWiredSwitchFlashImagesGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 26, 2, 1, 1)
)
arubaWiredSwitchFlashImagesGroup.setObjects(
      *(("ARUBAWIRED-SWITCH-IMAGE-MIB", "arubaWiredSwitchImageType"),
        ("ARUBAWIRED-SWITCH-IMAGE-MIB", "arubaWiredSwitchImageVersion"),
        ("ARUBAWIRED-SWITCH-IMAGE-MIB", "arubaWiredSwitchImageSize"),
        ("ARUBAWIRED-SWITCH-IMAGE-MIB", "arubaWiredSwitchImageBuildDate"),
        ("ARUBAWIRED-SWITCH-IMAGE-MIB", "arubaWiredSwitchImageSha"))
)
if mibBuilder.loadTexts:
    arubaWiredSwitchFlashImagesGroup.setStatus("current")

arubaWiredSwitchBootGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 26, 2, 1, 2)
)
arubaWiredSwitchBootGroup.setObjects(
      *(("ARUBAWIRED-SWITCH-IMAGE-MIB", "arubaWiredDefaultBoot"),
        ("ARUBAWIRED-SWITCH-IMAGE-MIB", "arubaWiredDefaultBootEnum"),
        ("ARUBAWIRED-SWITCH-IMAGE-MIB", "arubaWiredBootProfileTimeout"))
)
if mibBuilder.loadTexts:
    arubaWiredSwitchBootGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

arubaWiredSwitchImageCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 26, 2, 2, 1)
)
arubaWiredSwitchImageCompliance.setObjects(
      *(("ARUBAWIRED-SWITCH-IMAGE-MIB", "arubaWiredSwitchFlashImagesGroup"),
        ("ARUBAWIRED-SWITCH-IMAGE-MIB", "arubaWiredSwitchBootGroup"))
)
if mibBuilder.loadTexts:
    arubaWiredSwitchImageCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ARUBAWIRED-SWITCH-IMAGE-MIB",
    **{"arubaWiredSwitchImage": arubaWiredSwitchImage,
       "arubaWiredSwitchImageObject": arubaWiredSwitchImageObject,
       "arubaWiredSwitchImageGeneral": arubaWiredSwitchImageGeneral,
       "arubaWiredDefaultBoot": arubaWiredDefaultBoot,
       "arubaWiredDefaultBootEnum": arubaWiredDefaultBootEnum,
       "arubaWiredBootProfileTimeout": arubaWiredBootProfileTimeout,
       "arubaWiredSwitchImageDetails": arubaWiredSwitchImageDetails,
       "arubaWiredSwitchImageTable": arubaWiredSwitchImageTable,
       "arubaWiredSwitchImageEntry": arubaWiredSwitchImageEntry,
       "arubaWiredSwitchImageTypeEnum": arubaWiredSwitchImageTypeEnum,
       "arubaWiredSwitchImageType": arubaWiredSwitchImageType,
       "arubaWiredSwitchImageVersion": arubaWiredSwitchImageVersion,
       "arubaWiredSwitchImageSize": arubaWiredSwitchImageSize,
       "arubaWiredSwitchImageBuildDate": arubaWiredSwitchImageBuildDate,
       "arubaWiredSwitchImageSha": arubaWiredSwitchImageSha,
       "arubaWiredSwitchImageConformance": arubaWiredSwitchImageConformance,
       "arubaWiredSwitchImageGroups": arubaWiredSwitchImageGroups,
       "arubaWiredSwitchFlashImagesGroup": arubaWiredSwitchFlashImagesGroup,
       "arubaWiredSwitchBootGroup": arubaWiredSwitchBootGroup,
       "arubaWiredSwitchImageCompliances": arubaWiredSwitchImageCompliances,
       "arubaWiredSwitchImageCompliance": arubaWiredSwitchImageCompliance}
)
