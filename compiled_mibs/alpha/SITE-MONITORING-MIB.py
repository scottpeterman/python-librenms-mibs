# SNMP MIB module (SITE-MONITORING-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\alpha\SITE-MONITORING-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:17:44 2025
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
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

siteMonitoringMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 26854, 1, 1)
)
if mibBuilder.loadTexts:
    siteMonitoringMIB.setRevisions(
        ("2017-05-16 16:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Atsa_ObjectIdentity = ObjectIdentity
atsa = _Atsa_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 26854)
)
_AtsaCorporate_ObjectIdentity = ObjectIdentity
atsaCorporate = _AtsaCorporate_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 26854, 1)
)
_AtsaUs_ObjectIdentity = ObjectIdentity
atsaUs = _AtsaUs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 26854, 2)
)
_AtsaEu_ObjectIdentity = ObjectIdentity
atsaEu = _AtsaEu_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 26854, 3)
)
_AtsaEuDevices_ObjectIdentity = ObjectIdentity
atsaEuDevices = _AtsaEuDevices_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 26854, 3, 1)
)
_SiteMonitoring_ObjectIdentity = ObjectIdentity
siteMonitoring = _SiteMonitoring_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 26854, 3, 2)
)
_SiteV1_ObjectIdentity = ObjectIdentity
siteV1 = _SiteV1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 26854, 3, 2, 1)
)


class _SiteV1GlobalStatus_Type(DisplayString):
    """Custom type siteV1GlobalStatus based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SiteV1GlobalStatus_Type.__name__ = "DisplayString"
_SiteV1GlobalStatus_Object = MibScalar
siteV1GlobalStatus = _SiteV1GlobalStatus_Object(
    (1, 3, 6, 1, 4, 1, 26854, 3, 2, 1, 1),
    _SiteV1GlobalStatus_Type()
)
siteV1GlobalStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    siteV1GlobalStatus.setStatus("current")
_SiteV1GlobalAlarmSeverityType_Type = DisplayString
_SiteV1GlobalAlarmSeverityType_Object = MibScalar
siteV1GlobalAlarmSeverityType = _SiteV1GlobalAlarmSeverityType_Object(
    (1, 3, 6, 1, 4, 1, 26854, 3, 2, 1, 2),
    _SiteV1GlobalAlarmSeverityType_Type()
)
siteV1GlobalAlarmSeverityType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    siteV1GlobalAlarmSeverityType.setStatus("current")
_SiteV1GlobalAlarmSeverityLevel_Type = Integer32
_SiteV1GlobalAlarmSeverityLevel_Object = MibScalar
siteV1GlobalAlarmSeverityLevel = _SiteV1GlobalAlarmSeverityLevel_Object(
    (1, 3, 6, 1, 4, 1, 26854, 3, 2, 1, 3),
    _SiteV1GlobalAlarmSeverityLevel_Type()
)
siteV1GlobalAlarmSeverityLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    siteV1GlobalAlarmSeverityLevel.setStatus("current")
_SiteV1GlobalAlarmSeverityTypeInt_Type = Integer32
_SiteV1GlobalAlarmSeverityTypeInt_Object = MibScalar
siteV1GlobalAlarmSeverityTypeInt = _SiteV1GlobalAlarmSeverityTypeInt_Object(
    (1, 3, 6, 1, 4, 1, 26854, 3, 2, 1, 4),
    _SiteV1GlobalAlarmSeverityTypeInt_Type()
)
siteV1GlobalAlarmSeverityTypeInt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    siteV1GlobalAlarmSeverityTypeInt.setStatus("current")
_SiteV1Description_ObjectIdentity = ObjectIdentity
siteV1Description = _SiteV1Description_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 26854, 3, 2, 1, 10)
)
_SiteV1DescriptionNumber_Type = Integer32
_SiteV1DescriptionNumber_Object = MibScalar
siteV1DescriptionNumber = _SiteV1DescriptionNumber_Object(
    (1, 3, 6, 1, 4, 1, 26854, 3, 2, 1, 10, 1),
    _SiteV1DescriptionNumber_Type()
)
siteV1DescriptionNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    siteV1DescriptionNumber.setStatus("current")
_SiteV1DescriptionTable_Object = MibTable
siteV1DescriptionTable = _SiteV1DescriptionTable_Object(
    (1, 3, 6, 1, 4, 1, 26854, 3, 2, 1, 10, 2)
)
if mibBuilder.loadTexts:
    siteV1DescriptionTable.setStatus("current")
_SiteV1DescriptionEntry_Object = MibTableRow
siteV1DescriptionEntry = _SiteV1DescriptionEntry_Object(
    (1, 3, 6, 1, 4, 1, 26854, 3, 2, 1, 10, 2, 1)
)
siteV1DescriptionEntry.setIndexNames(
    (0, "SITE-MONITORING-MIB", "siteV1DescriptionIndex"),
)
if mibBuilder.loadTexts:
    siteV1DescriptionEntry.setStatus("current")
_SiteV1DescriptionIndex_Type = Unsigned32
_SiteV1DescriptionIndex_Object = MibTableColumn
siteV1DescriptionIndex = _SiteV1DescriptionIndex_Object(
    (1, 3, 6, 1, 4, 1, 26854, 3, 2, 1, 10, 2, 1, 1),
    _SiteV1DescriptionIndex_Type()
)
siteV1DescriptionIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    siteV1DescriptionIndex.setStatus("current")
_SiteV1DescriptionName_Type = DisplayString
_SiteV1DescriptionName_Object = MibTableColumn
siteV1DescriptionName = _SiteV1DescriptionName_Object(
    (1, 3, 6, 1, 4, 1, 26854, 3, 2, 1, 10, 2, 1, 2),
    _SiteV1DescriptionName_Type()
)
siteV1DescriptionName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    siteV1DescriptionName.setStatus("current")
_SiteV1DescriptionValue_Type = DisplayString
_SiteV1DescriptionValue_Object = MibTableColumn
siteV1DescriptionValue = _SiteV1DescriptionValue_Object(
    (1, 3, 6, 1, 4, 1, 26854, 3, 2, 1, 10, 2, 1, 3),
    _SiteV1DescriptionValue_Type()
)
siteV1DescriptionValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    siteV1DescriptionValue.setStatus("current")
_SiteV1DescriptionEntryStatus_Type = RowStatus
_SiteV1DescriptionEntryStatus_Object = MibTableColumn
siteV1DescriptionEntryStatus = _SiteV1DescriptionEntryStatus_Object(
    (1, 3, 6, 1, 4, 1, 26854, 3, 2, 1, 10, 2, 1, 4),
    _SiteV1DescriptionEntryStatus_Type()
)
siteV1DescriptionEntryStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    siteV1DescriptionEntryStatus.setStatus("current")
_SiteV1DescriptionList_ObjectIdentity = ObjectIdentity
siteV1DescriptionList = _SiteV1DescriptionList_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 26854, 3, 2, 1, 10, 3)
)
_SiteV1DescDescriptionSiteNumber_Type = DisplayString
_SiteV1DescDescriptionSiteNumber_Object = MibScalar
siteV1DescDescriptionSiteNumber = _SiteV1DescDescriptionSiteNumber_Object(
    (1, 3, 6, 1, 4, 1, 26854, 3, 2, 1, 10, 3, 1),
    _SiteV1DescDescriptionSiteNumber_Type()
)
siteV1DescDescriptionSiteNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    siteV1DescDescriptionSiteNumber.setStatus("current")
_SiteV1DescDescriptionSiteName_Type = DisplayString
_SiteV1DescDescriptionSiteName_Object = MibScalar
siteV1DescDescriptionSiteName = _SiteV1DescDescriptionSiteName_Object(
    (1, 3, 6, 1, 4, 1, 26854, 3, 2, 1, 10, 3, 2),
    _SiteV1DescDescriptionSiteName_Type()
)
siteV1DescDescriptionSiteName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    siteV1DescDescriptionSiteName.setStatus("current")
_SiteV1DescDescriptionShortDescription_Type = DisplayString
_SiteV1DescDescriptionShortDescription_Object = MibScalar
siteV1DescDescriptionShortDescription = _SiteV1DescDescriptionShortDescription_Object(
    (1, 3, 6, 1, 4, 1, 26854, 3, 2, 1, 10, 3, 3),
    _SiteV1DescDescriptionShortDescription_Type()
)
siteV1DescDescriptionShortDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    siteV1DescDescriptionShortDescription.setStatus("current")
_SiteV1DescDescriptionInfo_Type = DisplayString
_SiteV1DescDescriptionInfo_Object = MibScalar
siteV1DescDescriptionInfo = _SiteV1DescDescriptionInfo_Object(
    (1, 3, 6, 1, 4, 1, 26854, 3, 2, 1, 10, 3, 4),
    _SiteV1DescDescriptionInfo_Type()
)
siteV1DescDescriptionInfo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    siteV1DescDescriptionInfo.setStatus("current")
_SiteV1DescDescriptionDescription_Type = DisplayString
_SiteV1DescDescriptionDescription_Object = MibScalar
siteV1DescDescriptionDescription = _SiteV1DescDescriptionDescription_Object(
    (1, 3, 6, 1, 4, 1, 26854, 3, 2, 1, 10, 3, 5),
    _SiteV1DescDescriptionDescription_Type()
)
siteV1DescDescriptionDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    siteV1DescDescriptionDescription.setStatus("current")
_SiteV1DescDescriptionReference_Type = DisplayString
_SiteV1DescDescriptionReference_Object = MibScalar
siteV1DescDescriptionReference = _SiteV1DescDescriptionReference_Object(
    (1, 3, 6, 1, 4, 1, 26854, 3, 2, 1, 10, 3, 6),
    _SiteV1DescDescriptionReference_Type()
)
siteV1DescDescriptionReference.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    siteV1DescDescriptionReference.setStatus("current")
_SiteV1DescDescriptionContactName_Type = DisplayString
_SiteV1DescDescriptionContactName_Object = MibScalar
siteV1DescDescriptionContactName = _SiteV1DescDescriptionContactName_Object(
    (1, 3, 6, 1, 4, 1, 26854, 3, 2, 1, 10, 3, 7),
    _SiteV1DescDescriptionContactName_Type()
)
siteV1DescDescriptionContactName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    siteV1DescDescriptionContactName.setStatus("current")
_SiteV1DescDescriptionPhoneNumber_Type = DisplayString
_SiteV1DescDescriptionPhoneNumber_Object = MibScalar
siteV1DescDescriptionPhoneNumber = _SiteV1DescDescriptionPhoneNumber_Object(
    (1, 3, 6, 1, 4, 1, 26854, 3, 2, 1, 10, 3, 8),
    _SiteV1DescDescriptionPhoneNumber_Type()
)
siteV1DescDescriptionPhoneNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    siteV1DescDescriptionPhoneNumber.setStatus("current")
_SiteV1DescDescriptionStreet_Type = DisplayString
_SiteV1DescDescriptionStreet_Object = MibScalar
siteV1DescDescriptionStreet = _SiteV1DescDescriptionStreet_Object(
    (1, 3, 6, 1, 4, 1, 26854, 3, 2, 1, 10, 3, 11),
    _SiteV1DescDescriptionStreet_Type()
)
siteV1DescDescriptionStreet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    siteV1DescDescriptionStreet.setStatus("current")
_SiteV1DescDescriptionCity_Type = DisplayString
_SiteV1DescDescriptionCity_Object = MibScalar
siteV1DescDescriptionCity = _SiteV1DescDescriptionCity_Object(
    (1, 3, 6, 1, 4, 1, 26854, 3, 2, 1, 10, 3, 12),
    _SiteV1DescDescriptionCity_Type()
)
siteV1DescDescriptionCity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    siteV1DescDescriptionCity.setStatus("current")
_SiteV1DescDescriptionProvince_Type = DisplayString
_SiteV1DescDescriptionProvince_Object = MibScalar
siteV1DescDescriptionProvince = _SiteV1DescDescriptionProvince_Object(
    (1, 3, 6, 1, 4, 1, 26854, 3, 2, 1, 10, 3, 13),
    _SiteV1DescDescriptionProvince_Type()
)
siteV1DescDescriptionProvince.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    siteV1DescDescriptionProvince.setStatus("current")
_SiteV1DescDescriptionPostalCode_Type = DisplayString
_SiteV1DescDescriptionPostalCode_Object = MibScalar
siteV1DescDescriptionPostalCode = _SiteV1DescDescriptionPostalCode_Object(
    (1, 3, 6, 1, 4, 1, 26854, 3, 2, 1, 10, 3, 14),
    _SiteV1DescDescriptionPostalCode_Type()
)
siteV1DescDescriptionPostalCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    siteV1DescDescriptionPostalCode.setStatus("current")
_SiteV1DescDescriptionRegion_Type = DisplayString
_SiteV1DescDescriptionRegion_Object = MibScalar
siteV1DescDescriptionRegion = _SiteV1DescDescriptionRegion_Object(
    (1, 3, 6, 1, 4, 1, 26854, 3, 2, 1, 10, 3, 15),
    _SiteV1DescDescriptionRegion_Type()
)
siteV1DescDescriptionRegion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    siteV1DescDescriptionRegion.setStatus("current")
_SiteV1DescDescriptionCountry_Type = DisplayString
_SiteV1DescDescriptionCountry_Object = MibScalar
siteV1DescDescriptionCountry = _SiteV1DescDescriptionCountry_Object(
    (1, 3, 6, 1, 4, 1, 26854, 3, 2, 1, 10, 3, 16),
    _SiteV1DescDescriptionCountry_Type()
)
siteV1DescDescriptionCountry.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    siteV1DescDescriptionCountry.setStatus("current")
_SiteV1DescDescriptionGroup1_Type = DisplayString
_SiteV1DescDescriptionGroup1_Object = MibScalar
siteV1DescDescriptionGroup1 = _SiteV1DescDescriptionGroup1_Object(
    (1, 3, 6, 1, 4, 1, 26854, 3, 2, 1, 10, 3, 21),
    _SiteV1DescDescriptionGroup1_Type()
)
siteV1DescDescriptionGroup1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    siteV1DescDescriptionGroup1.setStatus("current")
_SiteV1DescDescriptionGroup2_Type = DisplayString
_SiteV1DescDescriptionGroup2_Object = MibScalar
siteV1DescDescriptionGroup2 = _SiteV1DescDescriptionGroup2_Object(
    (1, 3, 6, 1, 4, 1, 26854, 3, 2, 1, 10, 3, 22),
    _SiteV1DescDescriptionGroup2_Type()
)
siteV1DescDescriptionGroup2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    siteV1DescDescriptionGroup2.setStatus("current")
_SiteV1DescDescriptionGroup3_Type = DisplayString
_SiteV1DescDescriptionGroup3_Object = MibScalar
siteV1DescDescriptionGroup3 = _SiteV1DescDescriptionGroup3_Object(
    (1, 3, 6, 1, 4, 1, 26854, 3, 2, 1, 10, 3, 23),
    _SiteV1DescDescriptionGroup3_Type()
)
siteV1DescDescriptionGroup3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    siteV1DescDescriptionGroup3.setStatus("current")
_SiteV1DescDescriptionGroup4_Type = DisplayString
_SiteV1DescDescriptionGroup4_Object = MibScalar
siteV1DescDescriptionGroup4 = _SiteV1DescDescriptionGroup4_Object(
    (1, 3, 6, 1, 4, 1, 26854, 3, 2, 1, 10, 3, 24),
    _SiteV1DescDescriptionGroup4_Type()
)
siteV1DescDescriptionGroup4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    siteV1DescDescriptionGroup4.setStatus("current")
_SiteV1DescDescriptionGroup5_Type = DisplayString
_SiteV1DescDescriptionGroup5_Object = MibScalar
siteV1DescDescriptionGroup5 = _SiteV1DescDescriptionGroup5_Object(
    (1, 3, 6, 1, 4, 1, 26854, 3, 2, 1, 10, 3, 25),
    _SiteV1DescDescriptionGroup5_Type()
)
siteV1DescDescriptionGroup5.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    siteV1DescDescriptionGroup5.setStatus("current")
_SiteV1DescDescriptionLatitude_Type = DisplayString
_SiteV1DescDescriptionLatitude_Object = MibScalar
siteV1DescDescriptionLatitude = _SiteV1DescDescriptionLatitude_Object(
    (1, 3, 6, 1, 4, 1, 26854, 3, 2, 1, 10, 3, 31),
    _SiteV1DescDescriptionLatitude_Type()
)
siteV1DescDescriptionLatitude.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    siteV1DescDescriptionLatitude.setStatus("current")
_SiteV1DescDescriptionLongitude_Type = DisplayString
_SiteV1DescDescriptionLongitude_Object = MibScalar
siteV1DescDescriptionLongitude = _SiteV1DescDescriptionLongitude_Object(
    (1, 3, 6, 1, 4, 1, 26854, 3, 2, 1, 10, 3, 32),
    _SiteV1DescDescriptionLongitude_Type()
)
siteV1DescDescriptionLongitude.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    siteV1DescDescriptionLongitude.setStatus("current")
_SiteV1DescDescriptionAltitude_Type = DisplayString
_SiteV1DescDescriptionAltitude_Object = MibScalar
siteV1DescDescriptionAltitude = _SiteV1DescDescriptionAltitude_Object(
    (1, 3, 6, 1, 4, 1, 26854, 3, 2, 1, 10, 3, 33),
    _SiteV1DescDescriptionAltitude_Type()
)
siteV1DescDescriptionAltitude.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    siteV1DescDescriptionAltitude.setStatus("current")
_SiteV1DescControllerSoftwareRevision_Type = DisplayString
_SiteV1DescControllerSoftwareRevision_Object = MibScalar
siteV1DescControllerSoftwareRevision = _SiteV1DescControllerSoftwareRevision_Object(
    (1, 3, 6, 1, 4, 1, 26854, 3, 2, 1, 10, 3, 91),
    _SiteV1DescControllerSoftwareRevision_Type()
)
siteV1DescControllerSoftwareRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    siteV1DescControllerSoftwareRevision.setStatus("current")
_SiteV1DescControllerOperatingSystemRevision_Type = DisplayString
_SiteV1DescControllerOperatingSystemRevision_Object = MibScalar
siteV1DescControllerOperatingSystemRevision = _SiteV1DescControllerOperatingSystemRevision_Object(
    (1, 3, 6, 1, 4, 1, 26854, 3, 2, 1, 10, 3, 92),
    _SiteV1DescControllerOperatingSystemRevision_Type()
)
siteV1DescControllerOperatingSystemRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    siteV1DescControllerOperatingSystemRevision.setStatus("current")
_SiteV1DescControllerCPU_Type = DisplayString
_SiteV1DescControllerCPU_Object = MibScalar
siteV1DescControllerCPU = _SiteV1DescControllerCPU_Object(
    (1, 3, 6, 1, 4, 1, 26854, 3, 2, 1, 10, 3, 93),
    _SiteV1DescControllerCPU_Type()
)
siteV1DescControllerCPU.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    siteV1DescControllerCPU.setStatus("current")
_SiteV1DescControllerCard_Type = DisplayString
_SiteV1DescControllerCard_Object = MibScalar
siteV1DescControllerCard = _SiteV1DescControllerCard_Object(
    (1, 3, 6, 1, 4, 1, 26854, 3, 2, 1, 10, 3, 94),
    _SiteV1DescControllerCard_Type()
)
siteV1DescControllerCard.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    siteV1DescControllerCard.setStatus("current")
_SiteV1DescControllerStarterVersion_Type = DisplayString
_SiteV1DescControllerStarterVersion_Object = MibScalar
siteV1DescControllerStarterVersion = _SiteV1DescControllerStarterVersion_Object(
    (1, 3, 6, 1, 4, 1, 26854, 3, 2, 1, 10, 3, 100),
    _SiteV1DescControllerStarterVersion_Type()
)
siteV1DescControllerStarterVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    siteV1DescControllerStarterVersion.setStatus("current")
_SiteV1DescControllerFactoryCompasVersion_Type = DisplayString
_SiteV1DescControllerFactoryCompasVersion_Object = MibScalar
siteV1DescControllerFactoryCompasVersion = _SiteV1DescControllerFactoryCompasVersion_Object(
    (1, 3, 6, 1, 4, 1, 26854, 3, 2, 1, 10, 3, 105),
    _SiteV1DescControllerFactoryCompasVersion_Type()
)
siteV1DescControllerFactoryCompasVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    siteV1DescControllerFactoryCompasVersion.setStatus("current")
_SiteV1DescControllerUserCompasVersion_Type = DisplayString
_SiteV1DescControllerUserCompasVersion_Object = MibScalar
siteV1DescControllerUserCompasVersion = _SiteV1DescControllerUserCompasVersion_Object(
    (1, 3, 6, 1, 4, 1, 26854, 3, 2, 1, 10, 3, 106),
    _SiteV1DescControllerUserCompasVersion_Type()
)
siteV1DescControllerUserCompasVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    siteV1DescControllerUserCompasVersion.setStatus("current")
_SiteV1DescControllerFactoryFTPServerVersion_Type = DisplayString
_SiteV1DescControllerFactoryFTPServerVersion_Object = MibScalar
siteV1DescControllerFactoryFTPServerVersion = _SiteV1DescControllerFactoryFTPServerVersion_Object(
    (1, 3, 6, 1, 4, 1, 26854, 3, 2, 1, 10, 3, 110),
    _SiteV1DescControllerFactoryFTPServerVersion_Type()
)
siteV1DescControllerFactoryFTPServerVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    siteV1DescControllerFactoryFTPServerVersion.setStatus("current")
_SiteV1DescControllerUserFTPServerVersion_Type = DisplayString
_SiteV1DescControllerUserFTPServerVersion_Object = MibScalar
siteV1DescControllerUserFTPServerVersion = _SiteV1DescControllerUserFTPServerVersion_Object(
    (1, 3, 6, 1, 4, 1, 26854, 3, 2, 1, 10, 3, 111),
    _SiteV1DescControllerUserFTPServerVersion_Type()
)
siteV1DescControllerUserFTPServerVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    siteV1DescControllerUserFTPServerVersion.setStatus("current")
_SiteV1Alarm_ObjectIdentity = ObjectIdentity
siteV1Alarm = _SiteV1Alarm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 26854, 3, 2, 1, 11)
)
_SiteV1AlarmNumber_Type = Integer32
_SiteV1AlarmNumber_Object = MibScalar
siteV1AlarmNumber = _SiteV1AlarmNumber_Object(
    (1, 3, 6, 1, 4, 1, 26854, 3, 2, 1, 11, 1),
    _SiteV1AlarmNumber_Type()
)
siteV1AlarmNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    siteV1AlarmNumber.setStatus("current")
_SiteV1AlarmTable_Object = MibTable
siteV1AlarmTable = _SiteV1AlarmTable_Object(
    (1, 3, 6, 1, 4, 1, 26854, 3, 2, 1, 11, 2)
)
if mibBuilder.loadTexts:
    siteV1AlarmTable.setStatus("current")
_SiteV1AlarmEntry_Object = MibTableRow
siteV1AlarmEntry = _SiteV1AlarmEntry_Object(
    (1, 3, 6, 1, 4, 1, 26854, 3, 2, 1, 11, 2, 1)
)
siteV1AlarmEntry.setIndexNames(
    (0, "SITE-MONITORING-MIB", "siteV1AlarmIndex"),
)
if mibBuilder.loadTexts:
    siteV1AlarmEntry.setStatus("current")
_SiteV1AlarmIndex_Type = Unsigned32
_SiteV1AlarmIndex_Object = MibTableColumn
siteV1AlarmIndex = _SiteV1AlarmIndex_Object(
    (1, 3, 6, 1, 4, 1, 26854, 3, 2, 1, 11, 2, 1, 1),
    _SiteV1AlarmIndex_Type()
)
siteV1AlarmIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    siteV1AlarmIndex.setStatus("current")
_SiteV1AlarmName_Type = DisplayString
_SiteV1AlarmName_Object = MibTableColumn
siteV1AlarmName = _SiteV1AlarmName_Object(
    (1, 3, 6, 1, 4, 1, 26854, 3, 2, 1, 11, 2, 1, 2),
    _SiteV1AlarmName_Type()
)
siteV1AlarmName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    siteV1AlarmName.setStatus("current")
_SiteV1AlarmActive_Type = DisplayString
_SiteV1AlarmActive_Object = MibTableColumn
siteV1AlarmActive = _SiteV1AlarmActive_Object(
    (1, 3, 6, 1, 4, 1, 26854, 3, 2, 1, 11, 2, 1, 3),
    _SiteV1AlarmActive_Type()
)
siteV1AlarmActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    siteV1AlarmActive.setStatus("current")
_SiteV1AlarmSeverityType_Type = DisplayString
_SiteV1AlarmSeverityType_Object = MibTableColumn
siteV1AlarmSeverityType = _SiteV1AlarmSeverityType_Object(
    (1, 3, 6, 1, 4, 1, 26854, 3, 2, 1, 11, 2, 1, 4),
    _SiteV1AlarmSeverityType_Type()
)
siteV1AlarmSeverityType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    siteV1AlarmSeverityType.setStatus("current")
_SiteV1AlarmSeverityLevel_Type = DisplayString
_SiteV1AlarmSeverityLevel_Object = MibTableColumn
siteV1AlarmSeverityLevel = _SiteV1AlarmSeverityLevel_Object(
    (1, 3, 6, 1, 4, 1, 26854, 3, 2, 1, 11, 2, 1, 5),
    _SiteV1AlarmSeverityLevel_Type()
)
siteV1AlarmSeverityLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    siteV1AlarmSeverityLevel.setStatus("current")
_SiteV1AlarmStartTime_Type = DisplayString
_SiteV1AlarmStartTime_Object = MibTableColumn
siteV1AlarmStartTime = _SiteV1AlarmStartTime_Object(
    (1, 3, 6, 1, 4, 1, 26854, 3, 2, 1, 11, 2, 1, 6),
    _SiteV1AlarmStartTime_Type()
)
siteV1AlarmStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    siteV1AlarmStartTime.setStatus("current")
_SiteV1AlarmStopTime_Type = DisplayString
_SiteV1AlarmStopTime_Object = MibTableColumn
siteV1AlarmStopTime = _SiteV1AlarmStopTime_Object(
    (1, 3, 6, 1, 4, 1, 26854, 3, 2, 1, 11, 2, 1, 7),
    _SiteV1AlarmStopTime_Type()
)
siteV1AlarmStopTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    siteV1AlarmStopTime.setStatus("current")
_SiteV1AlarmEntryStatus_Type = RowStatus
_SiteV1AlarmEntryStatus_Object = MibTableColumn
siteV1AlarmEntryStatus = _SiteV1AlarmEntryStatus_Object(
    (1, 3, 6, 1, 4, 1, 26854, 3, 2, 1, 11, 2, 1, 8),
    _SiteV1AlarmEntryStatus_Type()
)
siteV1AlarmEntryStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    siteV1AlarmEntryStatus.setStatus("current")


class _SiteV1AlarmSummary_Type(Bits):
    """Custom type siteV1AlarmSummary based on Bits"""
    namedValues = NamedValues(
        *(("inventoryCANBusFail", 0),
          ("inventoryCANBusAddressingError", 1),
          ("inventoryMissingCANBusNodeIDs", 2),
          ("inventoryRunningCANLSSDeviceDetection", 3),
          ("inventoryRunningCANFirmwareUpgrade", 4),
          ("controllerControllerRebootRequired", 10),
          ("controllerLastConfChangesUnsaved", 14),
          ("xMLXMLHeartbeatPostFail", 20))
    )

_SiteV1AlarmSummary_Type.__name__ = "Bits"
_SiteV1AlarmSummary_Object = MibScalar
siteV1AlarmSummary = _SiteV1AlarmSummary_Object(
    (1, 3, 6, 1, 4, 1, 26854, 3, 2, 1, 11, 3),
    _SiteV1AlarmSummary_Type()
)
siteV1AlarmSummary.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    siteV1AlarmSummary.setStatus("current")
_SiteV1Event_ObjectIdentity = ObjectIdentity
siteV1Event = _SiteV1Event_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 26854, 3, 2, 1, 12)
)
_SiteV1EventNumber_Type = Integer32
_SiteV1EventNumber_Object = MibScalar
siteV1EventNumber = _SiteV1EventNumber_Object(
    (1, 3, 6, 1, 4, 1, 26854, 3, 2, 1, 12, 1),
    _SiteV1EventNumber_Type()
)
siteV1EventNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    siteV1EventNumber.setStatus("current")
_SiteV1EventTable_Object = MibTable
siteV1EventTable = _SiteV1EventTable_Object(
    (1, 3, 6, 1, 4, 1, 26854, 3, 2, 1, 12, 2)
)
if mibBuilder.loadTexts:
    siteV1EventTable.setStatus("current")
_SiteV1EventEntry_Object = MibTableRow
siteV1EventEntry = _SiteV1EventEntry_Object(
    (1, 3, 6, 1, 4, 1, 26854, 3, 2, 1, 12, 2, 1)
)
siteV1EventEntry.setIndexNames(
    (0, "SITE-MONITORING-MIB", "siteV1EventIndex"),
)
if mibBuilder.loadTexts:
    siteV1EventEntry.setStatus("current")
_SiteV1EventIndex_Type = Unsigned32
_SiteV1EventIndex_Object = MibTableColumn
siteV1EventIndex = _SiteV1EventIndex_Object(
    (1, 3, 6, 1, 4, 1, 26854, 3, 2, 1, 12, 2, 1, 1),
    _SiteV1EventIndex_Type()
)
siteV1EventIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    siteV1EventIndex.setStatus("current")
_SiteV1EventId_Type = Unsigned32
_SiteV1EventId_Object = MibTableColumn
siteV1EventId = _SiteV1EventId_Object(
    (1, 3, 6, 1, 4, 1, 26854, 3, 2, 1, 12, 2, 1, 2),
    _SiteV1EventId_Type()
)
siteV1EventId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    siteV1EventId.setStatus("current")
_SiteV1EventName_Type = DisplayString
_SiteV1EventName_Object = MibTableColumn
siteV1EventName = _SiteV1EventName_Object(
    (1, 3, 6, 1, 4, 1, 26854, 3, 2, 1, 12, 2, 1, 3),
    _SiteV1EventName_Type()
)
siteV1EventName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    siteV1EventName.setStatus("current")
_SiteV1EventDateTime_Type = DisplayString
_SiteV1EventDateTime_Object = MibTableColumn
siteV1EventDateTime = _SiteV1EventDateTime_Object(
    (1, 3, 6, 1, 4, 1, 26854, 3, 2, 1, 12, 2, 1, 4),
    _SiteV1EventDateTime_Type()
)
siteV1EventDateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    siteV1EventDateTime.setStatus("current")
_SiteV1EventSeverityType_Type = DisplayString
_SiteV1EventSeverityType_Object = MibTableColumn
siteV1EventSeverityType = _SiteV1EventSeverityType_Object(
    (1, 3, 6, 1, 4, 1, 26854, 3, 2, 1, 12, 2, 1, 5),
    _SiteV1EventSeverityType_Type()
)
siteV1EventSeverityType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    siteV1EventSeverityType.setStatus("current")
_SiteV1EventSeverityLevel_Type = DisplayString
_SiteV1EventSeverityLevel_Object = MibTableColumn
siteV1EventSeverityLevel = _SiteV1EventSeverityLevel_Object(
    (1, 3, 6, 1, 4, 1, 26854, 3, 2, 1, 12, 2, 1, 6),
    _SiteV1EventSeverityLevel_Type()
)
siteV1EventSeverityLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    siteV1EventSeverityLevel.setStatus("current")
_SiteV1EventEntryStatus_Type = RowStatus
_SiteV1EventEntryStatus_Object = MibTableColumn
siteV1EventEntryStatus = _SiteV1EventEntryStatus_Object(
    (1, 3, 6, 1, 4, 1, 26854, 3, 2, 1, 12, 2, 1, 7),
    _SiteV1EventEntryStatus_Type()
)
siteV1EventEntryStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    siteV1EventEntryStatus.setStatus("current")
_SiteV1Data_ObjectIdentity = ObjectIdentity
siteV1Data = _SiteV1Data_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 26854, 3, 2, 1, 13)
)
_SiteV1DataNumber_Type = Integer32
_SiteV1DataNumber_Object = MibScalar
siteV1DataNumber = _SiteV1DataNumber_Object(
    (1, 3, 6, 1, 4, 1, 26854, 3, 2, 1, 13, 1),
    _SiteV1DataNumber_Type()
)
siteV1DataNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    siteV1DataNumber.setStatus("current")
_SiteV1DataTable_Object = MibTable
siteV1DataTable = _SiteV1DataTable_Object(
    (1, 3, 6, 1, 4, 1, 26854, 3, 2, 1, 13, 2)
)
if mibBuilder.loadTexts:
    siteV1DataTable.setStatus("current")
_SiteV1DataEntry_Object = MibTableRow
siteV1DataEntry = _SiteV1DataEntry_Object(
    (1, 3, 6, 1, 4, 1, 26854, 3, 2, 1, 13, 2, 1)
)
siteV1DataEntry.setIndexNames(
    (0, "SITE-MONITORING-MIB", "siteV1DataIndex"),
)
if mibBuilder.loadTexts:
    siteV1DataEntry.setStatus("current")
_SiteV1DataIndex_Type = Unsigned32
_SiteV1DataIndex_Object = MibTableColumn
siteV1DataIndex = _SiteV1DataIndex_Object(
    (1, 3, 6, 1, 4, 1, 26854, 3, 2, 1, 13, 2, 1, 1),
    _SiteV1DataIndex_Type()
)
siteV1DataIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    siteV1DataIndex.setStatus("current")
_SiteV1DataName_Type = DisplayString
_SiteV1DataName_Object = MibTableColumn
siteV1DataName = _SiteV1DataName_Object(
    (1, 3, 6, 1, 4, 1, 26854, 3, 2, 1, 13, 2, 1, 2),
    _SiteV1DataName_Type()
)
siteV1DataName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    siteV1DataName.setStatus("current")
_SiteV1DataValue_Type = DisplayString
_SiteV1DataValue_Object = MibTableColumn
siteV1DataValue = _SiteV1DataValue_Object(
    (1, 3, 6, 1, 4, 1, 26854, 3, 2, 1, 13, 2, 1, 3),
    _SiteV1DataValue_Type()
)
siteV1DataValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    siteV1DataValue.setStatus("current")
_SiteV1DataEntryStatus_Type = RowStatus
_SiteV1DataEntryStatus_Object = MibTableColumn
siteV1DataEntryStatus = _SiteV1DataEntryStatus_Object(
    (1, 3, 6, 1, 4, 1, 26854, 3, 2, 1, 13, 2, 1, 4),
    _SiteV1DataEntryStatus_Type()
)
siteV1DataEntryStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    siteV1DataEntryStatus.setStatus("current")
_SiteV1DataList_ObjectIdentity = ObjectIdentity
siteV1DataList = _SiteV1DataList_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 26854, 3, 2, 1, 13, 3)
)
_SiteV1DataNetworkCurrentIPAddress_Type = Integer32
_SiteV1DataNetworkCurrentIPAddress_Object = MibScalar
siteV1DataNetworkCurrentIPAddress = _SiteV1DataNetworkCurrentIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 26854, 3, 2, 1, 13, 3, 1),
    _SiteV1DataNetworkCurrentIPAddress_Type()
)
siteV1DataNetworkCurrentIPAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    siteV1DataNetworkCurrentIPAddress.setStatus("current")
_SiteV1DataNetworkCurrentIPMask_Type = Integer32
_SiteV1DataNetworkCurrentIPMask_Object = MibScalar
siteV1DataNetworkCurrentIPMask = _SiteV1DataNetworkCurrentIPMask_Object(
    (1, 3, 6, 1, 4, 1, 26854, 3, 2, 1, 13, 3, 2),
    _SiteV1DataNetworkCurrentIPMask_Type()
)
siteV1DataNetworkCurrentIPMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    siteV1DataNetworkCurrentIPMask.setStatus("current")
_SiteV1DataNetworkCurrentMACAddress_Type = Integer32
_SiteV1DataNetworkCurrentMACAddress_Object = MibScalar
siteV1DataNetworkCurrentMACAddress = _SiteV1DataNetworkCurrentMACAddress_Object(
    (1, 3, 6, 1, 4, 1, 26854, 3, 2, 1, 13, 3, 3),
    _SiteV1DataNetworkCurrentMACAddress_Type()
)
siteV1DataNetworkCurrentMACAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    siteV1DataNetworkCurrentMACAddress.setStatus("current")
_SiteV1DataControllerLicensedOptions_Type = Integer32
_SiteV1DataControllerLicensedOptions_Object = MibScalar
siteV1DataControllerLicensedOptions = _SiteV1DataControllerLicensedOptions_Object(
    (1, 3, 6, 1, 4, 1, 26854, 3, 2, 1, 13, 3, 11),
    _SiteV1DataControllerLicensedOptions_Type()
)
siteV1DataControllerLicensedOptions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    siteV1DataControllerLicensedOptions.setStatus("current")
_SiteV1DataTimeDateAndTimeLocal_Type = DisplayString
_SiteV1DataTimeDateAndTimeLocal_Object = MibScalar
siteV1DataTimeDateAndTimeLocal = _SiteV1DataTimeDateAndTimeLocal_Object(
    (1, 3, 6, 1, 4, 1, 26854, 3, 2, 1, 13, 3, 21),
    _SiteV1DataTimeDateAndTimeLocal_Type()
)
siteV1DataTimeDateAndTimeLocal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    siteV1DataTimeDateAndTimeLocal.setStatus("current")
_SiteV1DataTimeDateAndTimeUTC_Type = DisplayString
_SiteV1DataTimeDateAndTimeUTC_Object = MibScalar
siteV1DataTimeDateAndTimeUTC = _SiteV1DataTimeDateAndTimeUTC_Object(
    (1, 3, 6, 1, 4, 1, 26854, 3, 2, 1, 13, 3, 22),
    _SiteV1DataTimeDateAndTimeUTC_Type()
)
siteV1DataTimeDateAndTimeUTC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    siteV1DataTimeDateAndTimeUTC.setStatus("current")
_SiteV1DataControllerMonitoringMemoryUsed_Type = Integer32
_SiteV1DataControllerMonitoringMemoryUsed_Object = MibScalar
siteV1DataControllerMonitoringMemoryUsed = _SiteV1DataControllerMonitoringMemoryUsed_Object(
    (1, 3, 6, 1, 4, 1, 26854, 3, 2, 1, 13, 3, 31),
    _SiteV1DataControllerMonitoringMemoryUsed_Type()
)
siteV1DataControllerMonitoringMemoryUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    siteV1DataControllerMonitoringMemoryUsed.setStatus("current")
_SiteV1DataControllerCPUPercentageUsage_Type = Integer32
_SiteV1DataControllerCPUPercentageUsage_Object = MibScalar
siteV1DataControllerCPUPercentageUsage = _SiteV1DataControllerCPUPercentageUsage_Object(
    (1, 3, 6, 1, 4, 1, 26854, 3, 2, 1, 13, 3, 32),
    _SiteV1DataControllerCPUPercentageUsage_Type()
)
siteV1DataControllerCPUPercentageUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    siteV1DataControllerCPUPercentageUsage.setStatus("current")
_SiteV1DataControllerFreeFlashMemorySpace_Type = Integer32
_SiteV1DataControllerFreeFlashMemorySpace_Object = MibScalar
siteV1DataControllerFreeFlashMemorySpace = _SiteV1DataControllerFreeFlashMemorySpace_Object(
    (1, 3, 6, 1, 4, 1, 26854, 3, 2, 1, 13, 3, 33),
    _SiteV1DataControllerFreeFlashMemorySpace_Type()
)
siteV1DataControllerFreeFlashMemorySpace.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    siteV1DataControllerFreeFlashMemorySpace.setStatus("current")
_SiteV1DataControllerFTPServerStatus_Type = DisplayString
_SiteV1DataControllerFTPServerStatus_Object = MibScalar
siteV1DataControllerFTPServerStatus = _SiteV1DataControllerFTPServerStatus_Object(
    (1, 3, 6, 1, 4, 1, 26854, 3, 2, 1, 13, 3, 35),
    _SiteV1DataControllerFTPServerStatus_Type()
)
siteV1DataControllerFTPServerStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    siteV1DataControllerFTPServerStatus.setStatus("current")
_SiteV1DataDataRecordsTotalFifoSizeOfSecondRecords_Type = Integer32
_SiteV1DataDataRecordsTotalFifoSizeOfSecondRecords_Object = MibScalar
siteV1DataDataRecordsTotalFifoSizeOfSecondRecords = _SiteV1DataDataRecordsTotalFifoSizeOfSecondRecords_Object(
    (1, 3, 6, 1, 4, 1, 26854, 3, 2, 1, 13, 3, 41),
    _SiteV1DataDataRecordsTotalFifoSizeOfSecondRecords_Type()
)
siteV1DataDataRecordsTotalFifoSizeOfSecondRecords.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    siteV1DataDataRecordsTotalFifoSizeOfSecondRecords.setStatus("current")
_SiteV1DataDataRecordsTotalFifoSizeOfMinuteRecords_Type = Integer32
_SiteV1DataDataRecordsTotalFifoSizeOfMinuteRecords_Object = MibScalar
siteV1DataDataRecordsTotalFifoSizeOfMinuteRecords = _SiteV1DataDataRecordsTotalFifoSizeOfMinuteRecords_Object(
    (1, 3, 6, 1, 4, 1, 26854, 3, 2, 1, 13, 3, 42),
    _SiteV1DataDataRecordsTotalFifoSizeOfMinuteRecords_Type()
)
siteV1DataDataRecordsTotalFifoSizeOfMinuteRecords.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    siteV1DataDataRecordsTotalFifoSizeOfMinuteRecords.setStatus("current")
_SiteV1DataDataRecordsTotalFifoSizeOfHourRecords_Type = Integer32
_SiteV1DataDataRecordsTotalFifoSizeOfHourRecords_Object = MibScalar
siteV1DataDataRecordsTotalFifoSizeOfHourRecords = _SiteV1DataDataRecordsTotalFifoSizeOfHourRecords_Object(
    (1, 3, 6, 1, 4, 1, 26854, 3, 2, 1, 13, 3, 43),
    _SiteV1DataDataRecordsTotalFifoSizeOfHourRecords_Type()
)
siteV1DataDataRecordsTotalFifoSizeOfHourRecords.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    siteV1DataDataRecordsTotalFifoSizeOfHourRecords.setStatus("current")
_SiteV1DataDataRecordsTotalFifoSizeOfDayRecords_Type = Integer32
_SiteV1DataDataRecordsTotalFifoSizeOfDayRecords_Object = MibScalar
siteV1DataDataRecordsTotalFifoSizeOfDayRecords = _SiteV1DataDataRecordsTotalFifoSizeOfDayRecords_Object(
    (1, 3, 6, 1, 4, 1, 26854, 3, 2, 1, 13, 3, 44),
    _SiteV1DataDataRecordsTotalFifoSizeOfDayRecords_Type()
)
siteV1DataDataRecordsTotalFifoSizeOfDayRecords.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    siteV1DataDataRecordsTotalFifoSizeOfDayRecords.setStatus("current")
_SiteV1DataInventoryCANBusNodeIDs_Type = Integer32
_SiteV1DataInventoryCANBusNodeIDs_Object = MibScalar
siteV1DataInventoryCANBusNodeIDs = _SiteV1DataInventoryCANBusNodeIDs_Object(
    (1, 3, 6, 1, 4, 1, 26854, 3, 2, 1, 13, 3, 51),
    _SiteV1DataInventoryCANBusNodeIDs_Type()
)
siteV1DataInventoryCANBusNodeIDs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    siteV1DataInventoryCANBusNodeIDs.setStatus("current")
_SiteV1DataCloudLinkCloudLinkState_Type = DisplayString
_SiteV1DataCloudLinkCloudLinkState_Object = MibScalar
siteV1DataCloudLinkCloudLinkState = _SiteV1DataCloudLinkCloudLinkState_Object(
    (1, 3, 6, 1, 4, 1, 26854, 3, 2, 1, 13, 3, 166),
    _SiteV1DataCloudLinkCloudLinkState_Type()
)
siteV1DataCloudLinkCloudLinkState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    siteV1DataCloudLinkCloudLinkState.setStatus("current")
_SiteV1Config_ObjectIdentity = ObjectIdentity
siteV1Config = _SiteV1Config_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 26854, 3, 2, 1, 15)
)
_SiteV1ConfigNumber_Type = Integer32
_SiteV1ConfigNumber_Object = MibScalar
siteV1ConfigNumber = _SiteV1ConfigNumber_Object(
    (1, 3, 6, 1, 4, 1, 26854, 3, 2, 1, 15, 1),
    _SiteV1ConfigNumber_Type()
)
siteV1ConfigNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    siteV1ConfigNumber.setStatus("current")
_SiteV1ConfigTable_Object = MibTable
siteV1ConfigTable = _SiteV1ConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 26854, 3, 2, 1, 15, 2)
)
if mibBuilder.loadTexts:
    siteV1ConfigTable.setStatus("current")
_SiteV1ConfigEntry_Object = MibTableRow
siteV1ConfigEntry = _SiteV1ConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 26854, 3, 2, 1, 15, 2, 1)
)
siteV1ConfigEntry.setIndexNames(
    (0, "SITE-MONITORING-MIB", "siteV1ConfigIndex"),
)
if mibBuilder.loadTexts:
    siteV1ConfigEntry.setStatus("current")
_SiteV1ConfigIndex_Type = Unsigned32
_SiteV1ConfigIndex_Object = MibTableColumn
siteV1ConfigIndex = _SiteV1ConfigIndex_Object(
    (1, 3, 6, 1, 4, 1, 26854, 3, 2, 1, 15, 2, 1, 1),
    _SiteV1ConfigIndex_Type()
)
siteV1ConfigIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    siteV1ConfigIndex.setStatus("current")
_SiteV1ConfigName_Type = DisplayString
_SiteV1ConfigName_Object = MibTableColumn
siteV1ConfigName = _SiteV1ConfigName_Object(
    (1, 3, 6, 1, 4, 1, 26854, 3, 2, 1, 15, 2, 1, 2),
    _SiteV1ConfigName_Type()
)
siteV1ConfigName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    siteV1ConfigName.setStatus("current")
_SiteV1ConfigValue_Type = DisplayString
_SiteV1ConfigValue_Object = MibTableColumn
siteV1ConfigValue = _SiteV1ConfigValue_Object(
    (1, 3, 6, 1, 4, 1, 26854, 3, 2, 1, 15, 2, 1, 3),
    _SiteV1ConfigValue_Type()
)
siteV1ConfigValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    siteV1ConfigValue.setStatus("current")
_SiteV1ConfigEntryStatus_Type = RowStatus
_SiteV1ConfigEntryStatus_Object = MibTableColumn
siteV1ConfigEntryStatus = _SiteV1ConfigEntryStatus_Object(
    (1, 3, 6, 1, 4, 1, 26854, 3, 2, 1, 15, 2, 1, 4),
    _SiteV1ConfigEntryStatus_Type()
)
siteV1ConfigEntryStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    siteV1ConfigEntryStatus.setStatus("current")
_SiteV1ConfigList_ObjectIdentity = ObjectIdentity
siteV1ConfigList = _SiteV1ConfigList_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 26854, 3, 2, 1, 15, 3)
)
_SiteV1CfgNetworkDHCPEnabled_Type = DisplayString
_SiteV1CfgNetworkDHCPEnabled_Object = MibScalar
siteV1CfgNetworkDHCPEnabled = _SiteV1CfgNetworkDHCPEnabled_Object(
    (1, 3, 6, 1, 4, 1, 26854, 3, 2, 1, 15, 3, 1),
    _SiteV1CfgNetworkDHCPEnabled_Type()
)
siteV1CfgNetworkDHCPEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    siteV1CfgNetworkDHCPEnabled.setStatus("current")
_SiteV1CfgNetworkIPAddressIfStatic_Type = DisplayString
_SiteV1CfgNetworkIPAddressIfStatic_Object = MibScalar
siteV1CfgNetworkIPAddressIfStatic = _SiteV1CfgNetworkIPAddressIfStatic_Object(
    (1, 3, 6, 1, 4, 1, 26854, 3, 2, 1, 15, 3, 2),
    _SiteV1CfgNetworkIPAddressIfStatic_Type()
)
siteV1CfgNetworkIPAddressIfStatic.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    siteV1CfgNetworkIPAddressIfStatic.setStatus("current")
_SiteV1CfgNetworkSubnetMaskIfStatic_Type = DisplayString
_SiteV1CfgNetworkSubnetMaskIfStatic_Object = MibScalar
siteV1CfgNetworkSubnetMaskIfStatic = _SiteV1CfgNetworkSubnetMaskIfStatic_Object(
    (1, 3, 6, 1, 4, 1, 26854, 3, 2, 1, 15, 3, 3),
    _SiteV1CfgNetworkSubnetMaskIfStatic_Type()
)
siteV1CfgNetworkSubnetMaskIfStatic.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    siteV1CfgNetworkSubnetMaskIfStatic.setStatus("current")
_SiteV1CfgNetworkDefaultGatewayIfStatic_Type = DisplayString
_SiteV1CfgNetworkDefaultGatewayIfStatic_Object = MibScalar
siteV1CfgNetworkDefaultGatewayIfStatic = _SiteV1CfgNetworkDefaultGatewayIfStatic_Object(
    (1, 3, 6, 1, 4, 1, 26854, 3, 2, 1, 15, 3, 4),
    _SiteV1CfgNetworkDefaultGatewayIfStatic_Type()
)
siteV1CfgNetworkDefaultGatewayIfStatic.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    siteV1CfgNetworkDefaultGatewayIfStatic.setStatus("current")
_SiteV1CfgNetworkDNSIfStatic_Type = DisplayString
_SiteV1CfgNetworkDNSIfStatic_Object = MibScalar
siteV1CfgNetworkDNSIfStatic = _SiteV1CfgNetworkDNSIfStatic_Object(
    (1, 3, 6, 1, 4, 1, 26854, 3, 2, 1, 15, 3, 5),
    _SiteV1CfgNetworkDNSIfStatic_Type()
)
siteV1CfgNetworkDNSIfStatic.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    siteV1CfgNetworkDNSIfStatic.setStatus("current")
_SiteV1CfgNetworkMaxTransmissionUnit_Type = DisplayString
_SiteV1CfgNetworkMaxTransmissionUnit_Object = MibScalar
siteV1CfgNetworkMaxTransmissionUnit = _SiteV1CfgNetworkMaxTransmissionUnit_Object(
    (1, 3, 6, 1, 4, 1, 26854, 3, 2, 1, 15, 3, 8),
    _SiteV1CfgNetworkMaxTransmissionUnit_Type()
)
siteV1CfgNetworkMaxTransmissionUnit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    siteV1CfgNetworkMaxTransmissionUnit.setStatus("current")
_SiteV1CfgTimeSNTPTimeServer_Type = DisplayString
_SiteV1CfgTimeSNTPTimeServer_Object = MibScalar
siteV1CfgTimeSNTPTimeServer = _SiteV1CfgTimeSNTPTimeServer_Object(
    (1, 3, 6, 1, 4, 1, 26854, 3, 2, 1, 15, 3, 11),
    _SiteV1CfgTimeSNTPTimeServer_Type()
)
siteV1CfgTimeSNTPTimeServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    siteV1CfgTimeSNTPTimeServer.setStatus("current")
_SiteV1CfgTimeTimeZoneName_Type = DisplayString
_SiteV1CfgTimeTimeZoneName_Object = MibScalar
siteV1CfgTimeTimeZoneName = _SiteV1CfgTimeTimeZoneName_Object(
    (1, 3, 6, 1, 4, 1, 26854, 3, 2, 1, 15, 3, 14),
    _SiteV1CfgTimeTimeZoneName_Type()
)
siteV1CfgTimeTimeZoneName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    siteV1CfgTimeTimeZoneName.setStatus("current")
_SiteV1CfgTimeSNTPTimeRefresh_Type = DisplayString
_SiteV1CfgTimeSNTPTimeRefresh_Object = MibScalar
siteV1CfgTimeSNTPTimeRefresh = _SiteV1CfgTimeSNTPTimeRefresh_Object(
    (1, 3, 6, 1, 4, 1, 26854, 3, 2, 1, 15, 3, 15),
    _SiteV1CfgTimeSNTPTimeRefresh_Type()
)
siteV1CfgTimeSNTPTimeRefresh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    siteV1CfgTimeSNTPTimeRefresh.setStatus("current")
_SiteV1CfgTimeSNTPTimeRecoveryRefresh_Type = DisplayString
_SiteV1CfgTimeSNTPTimeRecoveryRefresh_Object = MibScalar
siteV1CfgTimeSNTPTimeRecoveryRefresh = _SiteV1CfgTimeSNTPTimeRecoveryRefresh_Object(
    (1, 3, 6, 1, 4, 1, 26854, 3, 2, 1, 15, 3, 16),
    _SiteV1CfgTimeSNTPTimeRecoveryRefresh_Type()
)
siteV1CfgTimeSNTPTimeRecoveryRefresh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    siteV1CfgTimeSNTPTimeRecoveryRefresh.setStatus("current")
_SiteV1CfgWebServerWebServerSecurityEnabled_Type = DisplayString
_SiteV1CfgWebServerWebServerSecurityEnabled_Object = MibScalar
siteV1CfgWebServerWebServerSecurityEnabled = _SiteV1CfgWebServerWebServerSecurityEnabled_Object(
    (1, 3, 6, 1, 4, 1, 26854, 3, 2, 1, 15, 3, 22),
    _SiteV1CfgWebServerWebServerSecurityEnabled_Type()
)
siteV1CfgWebServerWebServerSecurityEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    siteV1CfgWebServerWebServerSecurityEnabled.setStatus("current")
_SiteV1CfgWebServerWebServerPort_Type = DisplayString
_SiteV1CfgWebServerWebServerPort_Object = MibScalar
siteV1CfgWebServerWebServerPort = _SiteV1CfgWebServerWebServerPort_Object(
    (1, 3, 6, 1, 4, 1, 26854, 3, 2, 1, 15, 3, 23),
    _SiteV1CfgWebServerWebServerPort_Type()
)
siteV1CfgWebServerWebServerPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    siteV1CfgWebServerWebServerPort.setStatus("current")
_SiteV1CfgWebServerWebAuthenticationMethod_Type = DisplayString
_SiteV1CfgWebServerWebAuthenticationMethod_Object = MibScalar
siteV1CfgWebServerWebAuthenticationMethod = _SiteV1CfgWebServerWebAuthenticationMethod_Object(
    (1, 3, 6, 1, 4, 1, 26854, 3, 2, 1, 15, 3, 24),
    _SiteV1CfgWebServerWebAuthenticationMethod_Type()
)
siteV1CfgWebServerWebAuthenticationMethod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    siteV1CfgWebServerWebAuthenticationMethod.setStatus("current")
_SiteV1CfgWebServerHttpsWebServerPort_Type = DisplayString
_SiteV1CfgWebServerHttpsWebServerPort_Object = MibScalar
siteV1CfgWebServerHttpsWebServerPort = _SiteV1CfgWebServerHttpsWebServerPort_Object(
    (1, 3, 6, 1, 4, 1, 26854, 3, 2, 1, 15, 3, 26),
    _SiteV1CfgWebServerHttpsWebServerPort_Type()
)
siteV1CfgWebServerHttpsWebServerPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    siteV1CfgWebServerHttpsWebServerPort.setStatus("current")
_SiteV1CfgWebServerDefaultPage_Type = DisplayString
_SiteV1CfgWebServerDefaultPage_Object = MibScalar
siteV1CfgWebServerDefaultPage = _SiteV1CfgWebServerDefaultPage_Object(
    (1, 3, 6, 1, 4, 1, 26854, 3, 2, 1, 15, 3, 31),
    _SiteV1CfgWebServerDefaultPage_Type()
)
siteV1CfgWebServerDefaultPage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    siteV1CfgWebServerDefaultPage.setStatus("current")
_SiteV1CfgXMLXMLEventPostingActivated_Type = DisplayString
_SiteV1CfgXMLXMLEventPostingActivated_Object = MibScalar
siteV1CfgXMLXMLEventPostingActivated = _SiteV1CfgXMLXMLEventPostingActivated_Object(
    (1, 3, 6, 1, 4, 1, 26854, 3, 2, 1, 15, 3, 41),
    _SiteV1CfgXMLXMLEventPostingActivated_Type()
)
siteV1CfgXMLXMLEventPostingActivated.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    siteV1CfgXMLXMLEventPostingActivated.setStatus("current")
_SiteV1CfgXMLXMLEventPostingRefreshTime_Type = DisplayString
_SiteV1CfgXMLXMLEventPostingRefreshTime_Object = MibScalar
siteV1CfgXMLXMLEventPostingRefreshTime = _SiteV1CfgXMLXMLEventPostingRefreshTime_Object(
    (1, 3, 6, 1, 4, 1, 26854, 3, 2, 1, 15, 3, 42),
    _SiteV1CfgXMLXMLEventPostingRefreshTime_Type()
)
siteV1CfgXMLXMLEventPostingRefreshTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    siteV1CfgXMLXMLEventPostingRefreshTime.setStatus("current")
_SiteV1CfgXMLXMLEventPostingTimeout_Type = DisplayString
_SiteV1CfgXMLXMLEventPostingTimeout_Object = MibScalar
siteV1CfgXMLXMLEventPostingTimeout = _SiteV1CfgXMLXMLEventPostingTimeout_Object(
    (1, 3, 6, 1, 4, 1, 26854, 3, 2, 1, 15, 3, 43),
    _SiteV1CfgXMLXMLEventPostingTimeout_Type()
)
siteV1CfgXMLXMLEventPostingTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    siteV1CfgXMLXMLEventPostingTimeout.setStatus("current")
_SiteV1CfgXMLXMLEventPostingToSecOnlyIfPrimFail_Type = DisplayString
_SiteV1CfgXMLXMLEventPostingToSecOnlyIfPrimFail_Object = MibScalar
siteV1CfgXMLXMLEventPostingToSecOnlyIfPrimFail = _SiteV1CfgXMLXMLEventPostingToSecOnlyIfPrimFail_Object(
    (1, 3, 6, 1, 4, 1, 26854, 3, 2, 1, 15, 3, 45),
    _SiteV1CfgXMLXMLEventPostingToSecOnlyIfPrimFail_Type()
)
siteV1CfgXMLXMLEventPostingToSecOnlyIfPrimFail.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    siteV1CfgXMLXMLEventPostingToSecOnlyIfPrimFail.setStatus("current")
_SiteV1CfgXMLXMLTablesToPostOnXMLEvent_Type = DisplayString
_SiteV1CfgXMLXMLTablesToPostOnXMLEvent_Object = MibScalar
siteV1CfgXMLXMLTablesToPostOnXMLEvent = _SiteV1CfgXMLXMLTablesToPostOnXMLEvent_Object(
    (1, 3, 6, 1, 4, 1, 26854, 3, 2, 1, 15, 3, 46),
    _SiteV1CfgXMLXMLTablesToPostOnXMLEvent_Type()
)
siteV1CfgXMLXMLTablesToPostOnXMLEvent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    siteV1CfgXMLXMLTablesToPostOnXMLEvent.setStatus("current")
_SiteV1CfgXMLXMLHeartbeatTime_Type = DisplayString
_SiteV1CfgXMLXMLHeartbeatTime_Object = MibScalar
siteV1CfgXMLXMLHeartbeatTime = _SiteV1CfgXMLXMLHeartbeatTime_Object(
    (1, 3, 6, 1, 4, 1, 26854, 3, 2, 1, 15, 3, 51),
    _SiteV1CfgXMLXMLHeartbeatTime_Type()
)
siteV1CfgXMLXMLHeartbeatTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    siteV1CfgXMLXMLHeartbeatTime.setStatus("current")
_SiteV1CfgSNMPSNMPActivated_Type = DisplayString
_SiteV1CfgSNMPSNMPActivated_Object = MibScalar
siteV1CfgSNMPSNMPActivated = _SiteV1CfgSNMPSNMPActivated_Object(
    (1, 3, 6, 1, 4, 1, 26854, 3, 2, 1, 15, 3, 61),
    _SiteV1CfgSNMPSNMPActivated_Type()
)
siteV1CfgSNMPSNMPActivated.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    siteV1CfgSNMPSNMPActivated.setStatus("current")
_SiteV1CfgSNMPSNMPTrapVersion_Type = DisplayString
_SiteV1CfgSNMPSNMPTrapVersion_Object = MibScalar
siteV1CfgSNMPSNMPTrapVersion = _SiteV1CfgSNMPSNMPTrapVersion_Object(
    (1, 3, 6, 1, 4, 1, 26854, 3, 2, 1, 15, 3, 63),
    _SiteV1CfgSNMPSNMPTrapVersion_Type()
)
siteV1CfgSNMPSNMPTrapVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    siteV1CfgSNMPSNMPTrapVersion.setStatus("current")
_SiteV1CfgSNMPSNMPGETMinSecurityLevel_Type = DisplayString
_SiteV1CfgSNMPSNMPGETMinSecurityLevel_Object = MibScalar
siteV1CfgSNMPSNMPGETMinSecurityLevel = _SiteV1CfgSNMPSNMPGETMinSecurityLevel_Object(
    (1, 3, 6, 1, 4, 1, 26854, 3, 2, 1, 15, 3, 64),
    _SiteV1CfgSNMPSNMPGETMinSecurityLevel_Type()
)
siteV1CfgSNMPSNMPGETMinSecurityLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    siteV1CfgSNMPSNMPGETMinSecurityLevel.setStatus("current")
_SiteV1CfgSNMPSNMPSETMinSecurityLevel_Type = DisplayString
_SiteV1CfgSNMPSNMPSETMinSecurityLevel_Object = MibScalar
siteV1CfgSNMPSNMPSETMinSecurityLevel = _SiteV1CfgSNMPSNMPSETMinSecurityLevel_Object(
    (1, 3, 6, 1, 4, 1, 26854, 3, 2, 1, 15, 3, 65),
    _SiteV1CfgSNMPSNMPSETMinSecurityLevel_Type()
)
siteV1CfgSNMPSNMPSETMinSecurityLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    siteV1CfgSNMPSNMPSETMinSecurityLevel.setStatus("current")
_SiteV1CfgSNMPSNMPV3AuthAlgorithm_Type = DisplayString
_SiteV1CfgSNMPSNMPV3AuthAlgorithm_Object = MibScalar
siteV1CfgSNMPSNMPV3AuthAlgorithm = _SiteV1CfgSNMPSNMPV3AuthAlgorithm_Object(
    (1, 3, 6, 1, 4, 1, 26854, 3, 2, 1, 15, 3, 66),
    _SiteV1CfgSNMPSNMPV3AuthAlgorithm_Type()
)
siteV1CfgSNMPSNMPV3AuthAlgorithm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    siteV1CfgSNMPSNMPV3AuthAlgorithm.setStatus("current")
_SiteV1CfgSNMPSNMPV3PrivacyAlgorithm_Type = DisplayString
_SiteV1CfgSNMPSNMPV3PrivacyAlgorithm_Object = MibScalar
siteV1CfgSNMPSNMPV3PrivacyAlgorithm = _SiteV1CfgSNMPSNMPV3PrivacyAlgorithm_Object(
    (1, 3, 6, 1, 4, 1, 26854, 3, 2, 1, 15, 3, 67),
    _SiteV1CfgSNMPSNMPV3PrivacyAlgorithm_Type()
)
siteV1CfgSNMPSNMPV3PrivacyAlgorithm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    siteV1CfgSNMPSNMPV3PrivacyAlgorithm.setStatus("current")
_SiteV1CfgSNMPSNMPV3PrivacyPassword_Type = DisplayString
_SiteV1CfgSNMPSNMPV3PrivacyPassword_Object = MibScalar
siteV1CfgSNMPSNMPV3PrivacyPassword = _SiteV1CfgSNMPSNMPV3PrivacyPassword_Object(
    (1, 3, 6, 1, 4, 1, 26854, 3, 2, 1, 15, 3, 68),
    _SiteV1CfgSNMPSNMPV3PrivacyPassword_Type()
)
siteV1CfgSNMPSNMPV3PrivacyPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    siteV1CfgSNMPSNMPV3PrivacyPassword.setStatus("current")
_SiteV1CfgSNMPSNMPV3EngineID_Type = DisplayString
_SiteV1CfgSNMPSNMPV3EngineID_Object = MibScalar
siteV1CfgSNMPSNMPV3EngineID = _SiteV1CfgSNMPSNMPV3EngineID_Object(
    (1, 3, 6, 1, 4, 1, 26854, 3, 2, 1, 15, 3, 69),
    _SiteV1CfgSNMPSNMPV3EngineID_Type()
)
siteV1CfgSNMPSNMPV3EngineID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    siteV1CfgSNMPSNMPV3EngineID.setStatus("current")
_SiteV1CfgSNMPSNMPV3TrapAuthAlgorithm_Type = DisplayString
_SiteV1CfgSNMPSNMPV3TrapAuthAlgorithm_Object = MibScalar
siteV1CfgSNMPSNMPV3TrapAuthAlgorithm = _SiteV1CfgSNMPSNMPV3TrapAuthAlgorithm_Object(
    (1, 3, 6, 1, 4, 1, 26854, 3, 2, 1, 15, 3, 72),
    _SiteV1CfgSNMPSNMPV3TrapAuthAlgorithm_Type()
)
siteV1CfgSNMPSNMPV3TrapAuthAlgorithm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    siteV1CfgSNMPSNMPV3TrapAuthAlgorithm.setStatus("current")
_SiteV1CfgSNMPSNMPV3TrapPrivacyAlgorithm_Type = DisplayString
_SiteV1CfgSNMPSNMPV3TrapPrivacyAlgorithm_Object = MibScalar
siteV1CfgSNMPSNMPV3TrapPrivacyAlgorithm = _SiteV1CfgSNMPSNMPV3TrapPrivacyAlgorithm_Object(
    (1, 3, 6, 1, 4, 1, 26854, 3, 2, 1, 15, 3, 73),
    _SiteV1CfgSNMPSNMPV3TrapPrivacyAlgorithm_Type()
)
siteV1CfgSNMPSNMPV3TrapPrivacyAlgorithm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    siteV1CfgSNMPSNMPV3TrapPrivacyAlgorithm.setStatus("current")
_SiteV1CfgSNMPSNMPV3TrapUsername_Type = DisplayString
_SiteV1CfgSNMPSNMPV3TrapUsername_Object = MibScalar
siteV1CfgSNMPSNMPV3TrapUsername = _SiteV1CfgSNMPSNMPV3TrapUsername_Object(
    (1, 3, 6, 1, 4, 1, 26854, 3, 2, 1, 15, 3, 74),
    _SiteV1CfgSNMPSNMPV3TrapUsername_Type()
)
siteV1CfgSNMPSNMPV3TrapUsername.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    siteV1CfgSNMPSNMPV3TrapUsername.setStatus("current")
_SiteV1CfgSNMPSNMPV3TrapAuthPassword_Type = DisplayString
_SiteV1CfgSNMPSNMPV3TrapAuthPassword_Object = MibScalar
siteV1CfgSNMPSNMPV3TrapAuthPassword = _SiteV1CfgSNMPSNMPV3TrapAuthPassword_Object(
    (1, 3, 6, 1, 4, 1, 26854, 3, 2, 1, 15, 3, 75),
    _SiteV1CfgSNMPSNMPV3TrapAuthPassword_Type()
)
siteV1CfgSNMPSNMPV3TrapAuthPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    siteV1CfgSNMPSNMPV3TrapAuthPassword.setStatus("current")
_SiteV1CfgSNMPSNMPV3TrapPrivacyPassword_Type = DisplayString
_SiteV1CfgSNMPSNMPV3TrapPrivacyPassword_Object = MibScalar
siteV1CfgSNMPSNMPV3TrapPrivacyPassword = _SiteV1CfgSNMPSNMPV3TrapPrivacyPassword_Object(
    (1, 3, 6, 1, 4, 1, 26854, 3, 2, 1, 15, 3, 76),
    _SiteV1CfgSNMPSNMPV3TrapPrivacyPassword_Type()
)
siteV1CfgSNMPSNMPV3TrapPrivacyPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    siteV1CfgSNMPSNMPV3TrapPrivacyPassword.setStatus("current")
_SiteV1CfgSNMPSiteDescriptionIdsIncludedInTraps_Type = DisplayString
_SiteV1CfgSNMPSiteDescriptionIdsIncludedInTraps_Object = MibScalar
siteV1CfgSNMPSiteDescriptionIdsIncludedInTraps = _SiteV1CfgSNMPSiteDescriptionIdsIncludedInTraps_Object(
    (1, 3, 6, 1, 4, 1, 26854, 3, 2, 1, 15, 3, 77),
    _SiteV1CfgSNMPSiteDescriptionIdsIncludedInTraps_Type()
)
siteV1CfgSNMPSiteDescriptionIdsIncludedInTraps.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    siteV1CfgSNMPSiteDescriptionIdsIncludedInTraps.setStatus("current")
_SiteV1CfgGenericGenerateEventOnConfChanges_Type = DisplayString
_SiteV1CfgGenericGenerateEventOnConfChanges_Object = MibScalar
siteV1CfgGenericGenerateEventOnConfChanges = _SiteV1CfgGenericGenerateEventOnConfChanges_Object(
    (1, 3, 6, 1, 4, 1, 26854, 3, 2, 1, 15, 3, 81),
    _SiteV1CfgGenericGenerateEventOnConfChanges_Type()
)
siteV1CfgGenericGenerateEventOnConfChanges.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    siteV1CfgGenericGenerateEventOnConfChanges.setStatus("current")
_SiteV1CfgDataRecordsAutoArchivePeriodDataRecord_Type = DisplayString
_SiteV1CfgDataRecordsAutoArchivePeriodDataRecord_Object = MibScalar
siteV1CfgDataRecordsAutoArchivePeriodDataRecord = _SiteV1CfgDataRecordsAutoArchivePeriodDataRecord_Object(
    (1, 3, 6, 1, 4, 1, 26854, 3, 2, 1, 15, 3, 82),
    _SiteV1CfgDataRecordsAutoArchivePeriodDataRecord_Type()
)
siteV1CfgDataRecordsAutoArchivePeriodDataRecord.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    siteV1CfgDataRecordsAutoArchivePeriodDataRecord.setStatus("current")
_SiteV1CfgGenericGenerateEventOnControlExecution_Type = DisplayString
_SiteV1CfgGenericGenerateEventOnControlExecution_Object = MibScalar
siteV1CfgGenericGenerateEventOnControlExecution = _SiteV1CfgGenericGenerateEventOnControlExecution_Object(
    (1, 3, 6, 1, 4, 1, 26854, 3, 2, 1, 15, 3, 83),
    _SiteV1CfgGenericGenerateEventOnControlExecution_Type()
)
siteV1CfgGenericGenerateEventOnControlExecution.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    siteV1CfgGenericGenerateEventOnControlExecution.setStatus("current")
_SiteV1CfgGenericGenerateEventOnAlarmAcknowledge_Type = DisplayString
_SiteV1CfgGenericGenerateEventOnAlarmAcknowledge_Object = MibScalar
siteV1CfgGenericGenerateEventOnAlarmAcknowledge = _SiteV1CfgGenericGenerateEventOnAlarmAcknowledge_Object(
    (1, 3, 6, 1, 4, 1, 26854, 3, 2, 1, 15, 3, 84),
    _SiteV1CfgGenericGenerateEventOnAlarmAcknowledge_Type()
)
siteV1CfgGenericGenerateEventOnAlarmAcknowledge.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    siteV1CfgGenericGenerateEventOnAlarmAcknowledge.setStatus("current")
_SiteV1CfgInventoryRequiredCANBusNodeIDs_Type = DisplayString
_SiteV1CfgInventoryRequiredCANBusNodeIDs_Object = MibScalar
siteV1CfgInventoryRequiredCANBusNodeIDs = _SiteV1CfgInventoryRequiredCANBusNodeIDs_Object(
    (1, 3, 6, 1, 4, 1, 26854, 3, 2, 1, 15, 3, 91),
    _SiteV1CfgInventoryRequiredCANBusNodeIDs_Type()
)
siteV1CfgInventoryRequiredCANBusNodeIDs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    siteV1CfgInventoryRequiredCANBusNodeIDs.setStatus("current")
_SiteV1CfgInventoryLSSCANidrange_Type = DisplayString
_SiteV1CfgInventoryLSSCANidrange_Object = MibScalar
siteV1CfgInventoryLSSCANidrange = _SiteV1CfgInventoryLSSCANidrange_Object(
    (1, 3, 6, 1, 4, 1, 26854, 3, 2, 1, 15, 3, 92),
    _SiteV1CfgInventoryLSSCANidrange_Type()
)
siteV1CfgInventoryLSSCANidrange.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    siteV1CfgInventoryLSSCANidrange.setStatus("current")
_SiteV1CfgInventorySystemNodesDefinition_Type = DisplayString
_SiteV1CfgInventorySystemNodesDefinition_Object = MibScalar
siteV1CfgInventorySystemNodesDefinition = _SiteV1CfgInventorySystemNodesDefinition_Object(
    (1, 3, 6, 1, 4, 1, 26854, 3, 2, 1, 15, 3, 93),
    _SiteV1CfgInventorySystemNodesDefinition_Type()
)
siteV1CfgInventorySystemNodesDefinition.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    siteV1CfgInventorySystemNodesDefinition.setStatus("current")
_SiteV1CfgInventoryLSSCANOpenSavedConf_Type = DisplayString
_SiteV1CfgInventoryLSSCANOpenSavedConf_Object = MibScalar
siteV1CfgInventoryLSSCANOpenSavedConf = _SiteV1CfgInventoryLSSCANOpenSavedConf_Object(
    (1, 3, 6, 1, 4, 1, 26854, 3, 2, 1, 15, 3, 95),
    _SiteV1CfgInventoryLSSCANOpenSavedConf_Type()
)
siteV1CfgInventoryLSSCANOpenSavedConf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    siteV1CfgInventoryLSSCANOpenSavedConf.setStatus("current")
_SiteV1CfgUsersAdministratorLoginPassword_Type = DisplayString
_SiteV1CfgUsersAdministratorLoginPassword_Object = MibScalar
siteV1CfgUsersAdministratorLoginPassword = _SiteV1CfgUsersAdministratorLoginPassword_Object(
    (1, 3, 6, 1, 4, 1, 26854, 3, 2, 1, 15, 3, 101),
    _SiteV1CfgUsersAdministratorLoginPassword_Type()
)
siteV1CfgUsersAdministratorLoginPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    siteV1CfgUsersAdministratorLoginPassword.setStatus("current")
_SiteV1CfgUsersUser1LoginPassword_Type = DisplayString
_SiteV1CfgUsersUser1LoginPassword_Object = MibScalar
siteV1CfgUsersUser1LoginPassword = _SiteV1CfgUsersUser1LoginPassword_Object(
    (1, 3, 6, 1, 4, 1, 26854, 3, 2, 1, 15, 3, 102),
    _SiteV1CfgUsersUser1LoginPassword_Type()
)
siteV1CfgUsersUser1LoginPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    siteV1CfgUsersUser1LoginPassword.setStatus("current")
_SiteV1CfgUsersUser2LoginPassword_Type = DisplayString
_SiteV1CfgUsersUser2LoginPassword_Object = MibScalar
siteV1CfgUsersUser2LoginPassword = _SiteV1CfgUsersUser2LoginPassword_Object(
    (1, 3, 6, 1, 4, 1, 26854, 3, 2, 1, 15, 3, 103),
    _SiteV1CfgUsersUser2LoginPassword_Type()
)
siteV1CfgUsersUser2LoginPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    siteV1CfgUsersUser2LoginPassword.setStatus("current")
_SiteV1CfgUsersUser3LoginPassword_Type = DisplayString
_SiteV1CfgUsersUser3LoginPassword_Object = MibScalar
siteV1CfgUsersUser3LoginPassword = _SiteV1CfgUsersUser3LoginPassword_Object(
    (1, 3, 6, 1, 4, 1, 26854, 3, 2, 1, 15, 3, 104),
    _SiteV1CfgUsersUser3LoginPassword_Type()
)
siteV1CfgUsersUser3LoginPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    siteV1CfgUsersUser3LoginPassword.setStatus("current")
_SiteV1CfgUsersUser4LoginPassword_Type = DisplayString
_SiteV1CfgUsersUser4LoginPassword_Object = MibScalar
siteV1CfgUsersUser4LoginPassword = _SiteV1CfgUsersUser4LoginPassword_Object(
    (1, 3, 6, 1, 4, 1, 26854, 3, 2, 1, 15, 3, 105),
    _SiteV1CfgUsersUser4LoginPassword_Type()
)
siteV1CfgUsersUser4LoginPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    siteV1CfgUsersUser4LoginPassword.setStatus("current")
_SiteV1CfgUsersUser5LoginPassword_Type = DisplayString
_SiteV1CfgUsersUser5LoginPassword_Object = MibScalar
siteV1CfgUsersUser5LoginPassword = _SiteV1CfgUsersUser5LoginPassword_Object(
    (1, 3, 6, 1, 4, 1, 26854, 3, 2, 1, 15, 3, 106),
    _SiteV1CfgUsersUser5LoginPassword_Type()
)
siteV1CfgUsersUser5LoginPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    siteV1CfgUsersUser5LoginPassword.setStatus("current")
_SiteV1CfgRadiusAuthenticationRadiusServer_Type = DisplayString
_SiteV1CfgRadiusAuthenticationRadiusServer_Object = MibScalar
siteV1CfgRadiusAuthenticationRadiusServer = _SiteV1CfgRadiusAuthenticationRadiusServer_Object(
    (1, 3, 6, 1, 4, 1, 26854, 3, 2, 1, 15, 3, 111),
    _SiteV1CfgRadiusAuthenticationRadiusServer_Type()
)
siteV1CfgRadiusAuthenticationRadiusServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    siteV1CfgRadiusAuthenticationRadiusServer.setStatus("current")
_SiteV1CfgRadiusAuthenticationRadiusPort_Type = DisplayString
_SiteV1CfgRadiusAuthenticationRadiusPort_Object = MibScalar
siteV1CfgRadiusAuthenticationRadiusPort = _SiteV1CfgRadiusAuthenticationRadiusPort_Object(
    (1, 3, 6, 1, 4, 1, 26854, 3, 2, 1, 15, 3, 112),
    _SiteV1CfgRadiusAuthenticationRadiusPort_Type()
)
siteV1CfgRadiusAuthenticationRadiusPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    siteV1CfgRadiusAuthenticationRadiusPort.setStatus("current")
_SiteV1CfgRadiusAuthenticationRadiusSecret_Type = DisplayString
_SiteV1CfgRadiusAuthenticationRadiusSecret_Object = MibScalar
siteV1CfgRadiusAuthenticationRadiusSecret = _SiteV1CfgRadiusAuthenticationRadiusSecret_Object(
    (1, 3, 6, 1, 4, 1, 26854, 3, 2, 1, 15, 3, 113),
    _SiteV1CfgRadiusAuthenticationRadiusSecret_Type()
)
siteV1CfgRadiusAuthenticationRadiusSecret.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    siteV1CfgRadiusAuthenticationRadiusSecret.setStatus("current")
_SiteV1CfgEmailEnableEmailFeature_Type = DisplayString
_SiteV1CfgEmailEnableEmailFeature_Object = MibScalar
siteV1CfgEmailEnableEmailFeature = _SiteV1CfgEmailEnableEmailFeature_Object(
    (1, 3, 6, 1, 4, 1, 26854, 3, 2, 1, 15, 3, 120),
    _SiteV1CfgEmailEnableEmailFeature_Type()
)
siteV1CfgEmailEnableEmailFeature.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    siteV1CfgEmailEnableEmailFeature.setStatus("current")
_SiteV1CfgEmailSmtpServer_Type = DisplayString
_SiteV1CfgEmailSmtpServer_Object = MibScalar
siteV1CfgEmailSmtpServer = _SiteV1CfgEmailSmtpServer_Object(
    (1, 3, 6, 1, 4, 1, 26854, 3, 2, 1, 15, 3, 121),
    _SiteV1CfgEmailSmtpServer_Type()
)
siteV1CfgEmailSmtpServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    siteV1CfgEmailSmtpServer.setStatus("current")
_SiteV1CfgEmailSmtpDomain_Type = DisplayString
_SiteV1CfgEmailSmtpDomain_Object = MibScalar
siteV1CfgEmailSmtpDomain = _SiteV1CfgEmailSmtpDomain_Object(
    (1, 3, 6, 1, 4, 1, 26854, 3, 2, 1, 15, 3, 122),
    _SiteV1CfgEmailSmtpDomain_Type()
)
siteV1CfgEmailSmtpDomain.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    siteV1CfgEmailSmtpDomain.setStatus("current")
_SiteV1CfgEmailSmtpUserLoginPassword_Type = DisplayString
_SiteV1CfgEmailSmtpUserLoginPassword_Object = MibScalar
siteV1CfgEmailSmtpUserLoginPassword = _SiteV1CfgEmailSmtpUserLoginPassword_Object(
    (1, 3, 6, 1, 4, 1, 26854, 3, 2, 1, 15, 3, 123),
    _SiteV1CfgEmailSmtpUserLoginPassword_Type()
)
siteV1CfgEmailSmtpUserLoginPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    siteV1CfgEmailSmtpUserLoginPassword.setStatus("current")
_SiteV1CfgEmailMailSender_Type = DisplayString
_SiteV1CfgEmailMailSender_Object = MibScalar
siteV1CfgEmailMailSender = _SiteV1CfgEmailMailSender_Object(
    (1, 3, 6, 1, 4, 1, 26854, 3, 2, 1, 15, 3, 130),
    _SiteV1CfgEmailMailSender_Type()
)
siteV1CfgEmailMailSender.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    siteV1CfgEmailMailSender.setStatus("current")
_SiteV1CfgEmailMailRecipients_Type = DisplayString
_SiteV1CfgEmailMailRecipients_Object = MibScalar
siteV1CfgEmailMailRecipients = _SiteV1CfgEmailMailRecipients_Object(
    (1, 3, 6, 1, 4, 1, 26854, 3, 2, 1, 15, 3, 131),
    _SiteV1CfgEmailMailRecipients_Type()
)
siteV1CfgEmailMailRecipients.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    siteV1CfgEmailMailRecipients.setStatus("current")
_SiteV1CfgEmailMinimalSeverityTypeToSendMail_Type = DisplayString
_SiteV1CfgEmailMinimalSeverityTypeToSendMail_Object = MibScalar
siteV1CfgEmailMinimalSeverityTypeToSendMail = _SiteV1CfgEmailMinimalSeverityTypeToSendMail_Object(
    (1, 3, 6, 1, 4, 1, 26854, 3, 2, 1, 15, 3, 135),
    _SiteV1CfgEmailMinimalSeverityTypeToSendMail_Type()
)
siteV1CfgEmailMinimalSeverityTypeToSendMail.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    siteV1CfgEmailMinimalSeverityTypeToSendMail.setStatus("current")
_SiteV1CfgControllerAutomaticReboot_Type = DisplayString
_SiteV1CfgControllerAutomaticReboot_Object = MibScalar
siteV1CfgControllerAutomaticReboot = _SiteV1CfgControllerAutomaticReboot_Object(
    (1, 3, 6, 1, 4, 1, 26854, 3, 2, 1, 15, 3, 150),
    _SiteV1CfgControllerAutomaticReboot_Type()
)
siteV1CfgControllerAutomaticReboot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    siteV1CfgControllerAutomaticReboot.setStatus("current")
_SiteV1CfgCloudLinkCloudEnabled_Type = DisplayString
_SiteV1CfgCloudLinkCloudEnabled_Object = MibScalar
siteV1CfgCloudLinkCloudEnabled = _SiteV1CfgCloudLinkCloudEnabled_Object(
    (1, 3, 6, 1, 4, 1, 26854, 3, 2, 1, 15, 3, 161),
    _SiteV1CfgCloudLinkCloudEnabled_Type()
)
siteV1CfgCloudLinkCloudEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    siteV1CfgCloudLinkCloudEnabled.setStatus("current")
_SiteV1CfgCloudLinkCloudServer_Type = DisplayString
_SiteV1CfgCloudLinkCloudServer_Object = MibScalar
siteV1CfgCloudLinkCloudServer = _SiteV1CfgCloudLinkCloudServer_Object(
    (1, 3, 6, 1, 4, 1, 26854, 3, 2, 1, 15, 3, 162),
    _SiteV1CfgCloudLinkCloudServer_Type()
)
siteV1CfgCloudLinkCloudServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    siteV1CfgCloudLinkCloudServer.setStatus("current")
_SiteV1CfgCloudLinkCloudPort_Type = DisplayString
_SiteV1CfgCloudLinkCloudPort_Object = MibScalar
siteV1CfgCloudLinkCloudPort = _SiteV1CfgCloudLinkCloudPort_Object(
    (1, 3, 6, 1, 4, 1, 26854, 3, 2, 1, 15, 3, 163),
    _SiteV1CfgCloudLinkCloudPort_Type()
)
siteV1CfgCloudLinkCloudPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    siteV1CfgCloudLinkCloudPort.setStatus("current")
_SiteV1CfgCloudLinkCloudCredential_Type = DisplayString
_SiteV1CfgCloudLinkCloudCredential_Object = MibScalar
siteV1CfgCloudLinkCloudCredential = _SiteV1CfgCloudLinkCloudCredential_Object(
    (1, 3, 6, 1, 4, 1, 26854, 3, 2, 1, 15, 3, 164),
    _SiteV1CfgCloudLinkCloudCredential_Type()
)
siteV1CfgCloudLinkCloudCredential.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    siteV1CfgCloudLinkCloudCredential.setStatus("current")
_SiteV1CfgCloudLinkCloudCluster_Type = DisplayString
_SiteV1CfgCloudLinkCloudCluster_Object = MibScalar
siteV1CfgCloudLinkCloudCluster = _SiteV1CfgCloudLinkCloudCluster_Object(
    (1, 3, 6, 1, 4, 1, 26854, 3, 2, 1, 15, 3, 165),
    _SiteV1CfgCloudLinkCloudCluster_Type()
)
siteV1CfgCloudLinkCloudCluster.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    siteV1CfgCloudLinkCloudCluster.setStatus("current")
_SiteV1CfgInventoryRS485ExtensionsConf_Type = DisplayString
_SiteV1CfgInventoryRS485ExtensionsConf_Object = MibScalar
siteV1CfgInventoryRS485ExtensionsConf = _SiteV1CfgInventoryRS485ExtensionsConf_Object(
    (1, 3, 6, 1, 4, 1, 26854, 3, 2, 1, 15, 3, 210),
    _SiteV1CfgInventoryRS485ExtensionsConf_Type()
)
siteV1CfgInventoryRS485ExtensionsConf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    siteV1CfgInventoryRS485ExtensionsConf.setStatus("current")
_SiteV1CfgInventoryEthernetExtensionsConf_Type = DisplayString
_SiteV1CfgInventoryEthernetExtensionsConf_Object = MibScalar
siteV1CfgInventoryEthernetExtensionsConf = _SiteV1CfgInventoryEthernetExtensionsConf_Object(
    (1, 3, 6, 1, 4, 1, 26854, 3, 2, 1, 15, 3, 220),
    _SiteV1CfgInventoryEthernetExtensionsConf_Type()
)
siteV1CfgInventoryEthernetExtensionsConf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    siteV1CfgInventoryEthernetExtensionsConf.setStatus("current")
_SiteV1CfgScriptingEnabledscripts_Type = DisplayString
_SiteV1CfgScriptingEnabledscripts_Object = MibScalar
siteV1CfgScriptingEnabledscripts = _SiteV1CfgScriptingEnabledscripts_Object(
    (1, 3, 6, 1, 4, 1, 26854, 3, 2, 1, 15, 3, 250),
    _SiteV1CfgScriptingEnabledscripts_Type()
)
siteV1CfgScriptingEnabledscripts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    siteV1CfgScriptingEnabledscripts.setStatus("current")
_SiteV1CfgScriptingNumberofErrorsbeforetriggeringalarm_Type = DisplayString
_SiteV1CfgScriptingNumberofErrorsbeforetriggeringalarm_Object = MibScalar
siteV1CfgScriptingNumberofErrorsbeforetriggeringalarm = _SiteV1CfgScriptingNumberofErrorsbeforetriggeringalarm_Object(
    (1, 3, 6, 1, 4, 1, 26854, 3, 2, 1, 15, 3, 251),
    _SiteV1CfgScriptingNumberofErrorsbeforetriggeringalarm_Type()
)
siteV1CfgScriptingNumberofErrorsbeforetriggeringalarm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    siteV1CfgScriptingNumberofErrorsbeforetriggeringalarm.setStatus("current")
_SiteV1CfgGenericReadAccessUserNumbers_Type = DisplayString
_SiteV1CfgGenericReadAccessUserNumbers_Object = MibScalar
siteV1CfgGenericReadAccessUserNumbers = _SiteV1CfgGenericReadAccessUserNumbers_Object(
    (1, 3, 6, 1, 4, 1, 26854, 3, 2, 1, 15, 3, 521),
    _SiteV1CfgGenericReadAccessUserNumbers_Type()
)
siteV1CfgGenericReadAccessUserNumbers.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    siteV1CfgGenericReadAccessUserNumbers.setStatus("current")
_SiteV1CfgGenericWriteAccessUserNumbers_Type = DisplayString
_SiteV1CfgGenericWriteAccessUserNumbers_Object = MibScalar
siteV1CfgGenericWriteAccessUserNumbers = _SiteV1CfgGenericWriteAccessUserNumbers_Object(
    (1, 3, 6, 1, 4, 1, 26854, 3, 2, 1, 15, 3, 522),
    _SiteV1CfgGenericWriteAccessUserNumbers_Type()
)
siteV1CfgGenericWriteAccessUserNumbers.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    siteV1CfgGenericWriteAccessUserNumbers.setStatus("current")
_SiteV1CfgGenericEventTableLength_Type = DisplayString
_SiteV1CfgGenericEventTableLength_Object = MibScalar
siteV1CfgGenericEventTableLength = _SiteV1CfgGenericEventTableLength_Object(
    (1, 3, 6, 1, 4, 1, 26854, 3, 2, 1, 15, 3, 601),
    _SiteV1CfgGenericEventTableLength_Type()
)
siteV1CfgGenericEventTableLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    siteV1CfgGenericEventTableLength.setStatus("current")
_SiteV1CfgSNMPSNMPTrapTargetsIP_Type = DisplayString
_SiteV1CfgSNMPSNMPTrapTargetsIP_Object = MibScalar
siteV1CfgSNMPSNMPTrapTargetsIP = _SiteV1CfgSNMPSNMPTrapTargetsIP_Object(
    (1, 3, 6, 1, 4, 1, 26854, 3, 2, 1, 15, 3, 611),
    _SiteV1CfgSNMPSNMPTrapTargetsIP_Type()
)
siteV1CfgSNMPSNMPTrapTargetsIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    siteV1CfgSNMPSNMPTrapTargetsIP.setStatus("current")
_SiteV1CfgSNMPMinimalEventSeverityForTraps_Type = DisplayString
_SiteV1CfgSNMPMinimalEventSeverityForTraps_Object = MibScalar
siteV1CfgSNMPMinimalEventSeverityForTraps = _SiteV1CfgSNMPMinimalEventSeverityForTraps_Object(
    (1, 3, 6, 1, 4, 1, 26854, 3, 2, 1, 15, 3, 612),
    _SiteV1CfgSNMPMinimalEventSeverityForTraps_Type()
)
siteV1CfgSNMPMinimalEventSeverityForTraps.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    siteV1CfgSNMPMinimalEventSeverityForTraps.setStatus("current")
_SiteV1CfgXMLXMLEventsPrimPostURL_Type = DisplayString
_SiteV1CfgXMLXMLEventsPrimPostURL_Object = MibScalar
siteV1CfgXMLXMLEventsPrimPostURL = _SiteV1CfgXMLXMLEventsPrimPostURL_Object(
    (1, 3, 6, 1, 4, 1, 26854, 3, 2, 1, 15, 3, 651),
    _SiteV1CfgXMLXMLEventsPrimPostURL_Type()
)
siteV1CfgXMLXMLEventsPrimPostURL.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    siteV1CfgXMLXMLEventsPrimPostURL.setStatus("current")
_SiteV1CfgXMLXMLEventsPrimPostLogin_Type = DisplayString
_SiteV1CfgXMLXMLEventsPrimPostLogin_Object = MibScalar
siteV1CfgXMLXMLEventsPrimPostLogin = _SiteV1CfgXMLXMLEventsPrimPostLogin_Object(
    (1, 3, 6, 1, 4, 1, 26854, 3, 2, 1, 15, 3, 652),
    _SiteV1CfgXMLXMLEventsPrimPostLogin_Type()
)
siteV1CfgXMLXMLEventsPrimPostLogin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    siteV1CfgXMLXMLEventsPrimPostLogin.setStatus("current")
_SiteV1CfgXMLXMLEventsPrimPostPassword_Type = DisplayString
_SiteV1CfgXMLXMLEventsPrimPostPassword_Object = MibScalar
siteV1CfgXMLXMLEventsPrimPostPassword = _SiteV1CfgXMLXMLEventsPrimPostPassword_Object(
    (1, 3, 6, 1, 4, 1, 26854, 3, 2, 1, 15, 3, 653),
    _SiteV1CfgXMLXMLEventsPrimPostPassword_Type()
)
siteV1CfgXMLXMLEventsPrimPostPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    siteV1CfgXMLXMLEventsPrimPostPassword.setStatus("current")
_SiteV1CfgXMLXMLEventsSecPostURL_Type = DisplayString
_SiteV1CfgXMLXMLEventsSecPostURL_Object = MibScalar
siteV1CfgXMLXMLEventsSecPostURL = _SiteV1CfgXMLXMLEventsSecPostURL_Object(
    (1, 3, 6, 1, 4, 1, 26854, 3, 2, 1, 15, 3, 661),
    _SiteV1CfgXMLXMLEventsSecPostURL_Type()
)
siteV1CfgXMLXMLEventsSecPostURL.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    siteV1CfgXMLXMLEventsSecPostURL.setStatus("current")
_SiteV1CfgXMLXMLEventsSecPostLogin_Type = DisplayString
_SiteV1CfgXMLXMLEventsSecPostLogin_Object = MibScalar
siteV1CfgXMLXMLEventsSecPostLogin = _SiteV1CfgXMLXMLEventsSecPostLogin_Object(
    (1, 3, 6, 1, 4, 1, 26854, 3, 2, 1, 15, 3, 662),
    _SiteV1CfgXMLXMLEventsSecPostLogin_Type()
)
siteV1CfgXMLXMLEventsSecPostLogin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    siteV1CfgXMLXMLEventsSecPostLogin.setStatus("current")
_SiteV1CfgXMLXMLEventsSecPostPassword_Type = DisplayString
_SiteV1CfgXMLXMLEventsSecPostPassword_Object = MibScalar
siteV1CfgXMLXMLEventsSecPostPassword = _SiteV1CfgXMLXMLEventsSecPostPassword_Object(
    (1, 3, 6, 1, 4, 1, 26854, 3, 2, 1, 15, 3, 663),
    _SiteV1CfgXMLXMLEventsSecPostPassword_Type()
)
siteV1CfgXMLXMLEventsSecPostPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    siteV1CfgXMLXMLEventsSecPostPassword.setStatus("current")
_SiteV1CfgPLCNumberOfPLCData_Type = DisplayString
_SiteV1CfgPLCNumberOfPLCData_Object = MibScalar
siteV1CfgPLCNumberOfPLCData = _SiteV1CfgPLCNumberOfPLCData_Object(
    (1, 3, 6, 1, 4, 1, 26854, 3, 2, 1, 15, 3, 901),
    _SiteV1CfgPLCNumberOfPLCData_Type()
)
siteV1CfgPLCNumberOfPLCData.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    siteV1CfgPLCNumberOfPLCData.setStatus("current")
_SiteV1CfgPLCNumberOfPLCAlarm_Type = DisplayString
_SiteV1CfgPLCNumberOfPLCAlarm_Object = MibScalar
siteV1CfgPLCNumberOfPLCAlarm = _SiteV1CfgPLCNumberOfPLCAlarm_Object(
    (1, 3, 6, 1, 4, 1, 26854, 3, 2, 1, 15, 3, 902),
    _SiteV1CfgPLCNumberOfPLCAlarm_Type()
)
siteV1CfgPLCNumberOfPLCAlarm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    siteV1CfgPLCNumberOfPLCAlarm.setStatus("current")
_SiteV1Control_ObjectIdentity = ObjectIdentity
siteV1Control = _SiteV1Control_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 26854, 3, 2, 1, 16)
)
_SiteV1ControlNumber_Type = Integer32
_SiteV1ControlNumber_Object = MibScalar
siteV1ControlNumber = _SiteV1ControlNumber_Object(
    (1, 3, 6, 1, 4, 1, 26854, 3, 2, 1, 16, 1),
    _SiteV1ControlNumber_Type()
)
siteV1ControlNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    siteV1ControlNumber.setStatus("current")
_SiteV1ControlTable_Object = MibTable
siteV1ControlTable = _SiteV1ControlTable_Object(
    (1, 3, 6, 1, 4, 1, 26854, 3, 2, 1, 16, 2)
)
if mibBuilder.loadTexts:
    siteV1ControlTable.setStatus("current")
_SiteV1ControlEntry_Object = MibTableRow
siteV1ControlEntry = _SiteV1ControlEntry_Object(
    (1, 3, 6, 1, 4, 1, 26854, 3, 2, 1, 16, 2, 1)
)
siteV1ControlEntry.setIndexNames(
    (0, "SITE-MONITORING-MIB", "siteV1ControlIndex"),
)
if mibBuilder.loadTexts:
    siteV1ControlEntry.setStatus("current")
_SiteV1ControlIndex_Type = Unsigned32
_SiteV1ControlIndex_Object = MibTableColumn
siteV1ControlIndex = _SiteV1ControlIndex_Object(
    (1, 3, 6, 1, 4, 1, 26854, 3, 2, 1, 16, 2, 1, 1),
    _SiteV1ControlIndex_Type()
)
siteV1ControlIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    siteV1ControlIndex.setStatus("current")
_SiteV1ControlName_Type = DisplayString
_SiteV1ControlName_Object = MibTableColumn
siteV1ControlName = _SiteV1ControlName_Object(
    (1, 3, 6, 1, 4, 1, 26854, 3, 2, 1, 16, 2, 1, 2),
    _SiteV1ControlName_Type()
)
siteV1ControlName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    siteV1ControlName.setStatus("current")
_SiteV1ControlValue_Type = DisplayString
_SiteV1ControlValue_Object = MibTableColumn
siteV1ControlValue = _SiteV1ControlValue_Object(
    (1, 3, 6, 1, 4, 1, 26854, 3, 2, 1, 16, 2, 1, 3),
    _SiteV1ControlValue_Type()
)
siteV1ControlValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    siteV1ControlValue.setStatus("current")
_SiteV1ControlEntryStatus_Type = RowStatus
_SiteV1ControlEntryStatus_Object = MibTableColumn
siteV1ControlEntryStatus = _SiteV1ControlEntryStatus_Object(
    (1, 3, 6, 1, 4, 1, 26854, 3, 2, 1, 16, 2, 1, 4),
    _SiteV1ControlEntryStatus_Type()
)
siteV1ControlEntryStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    siteV1ControlEntryStatus.setStatus("current")
_SiteV1ControlList_ObjectIdentity = ObjectIdentity
siteV1ControlList = _SiteV1ControlList_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 26854, 3, 2, 1, 16, 3)
)
_SiteV1CtrlControllerRebootController_Type = DisplayString
_SiteV1CtrlControllerRebootController_Object = MibScalar
siteV1CtrlControllerRebootController = _SiteV1CtrlControllerRebootController_Object(
    (1, 3, 6, 1, 4, 1, 26854, 3, 2, 1, 16, 3, 1),
    _SiteV1CtrlControllerRebootController_Type()
)
siteV1CtrlControllerRebootController.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    siteV1CtrlControllerRebootController.setStatus("current")
_SiteV1CtrlControllerSaveConfAndRebootController_Type = DisplayString
_SiteV1CtrlControllerSaveConfAndRebootController_Object = MibScalar
siteV1CtrlControllerSaveConfAndRebootController = _SiteV1CtrlControllerSaveConfAndRebootController_Object(
    (1, 3, 6, 1, 4, 1, 26854, 3, 2, 1, 16, 3, 2),
    _SiteV1CtrlControllerSaveConfAndRebootController_Type()
)
siteV1CtrlControllerSaveConfAndRebootController.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    siteV1CtrlControllerSaveConfAndRebootController.setStatus("current")
_SiteV1CtrlControllerRebootControllerWithoutSavingRecords_Type = DisplayString
_SiteV1CtrlControllerRebootControllerWithoutSavingRecords_Object = MibScalar
siteV1CtrlControllerRebootControllerWithoutSavingRecords = _SiteV1CtrlControllerRebootControllerWithoutSavingRecords_Object(
    (1, 3, 6, 1, 4, 1, 26854, 3, 2, 1, 16, 3, 3),
    _SiteV1CtrlControllerRebootControllerWithoutSavingRecords_Type()
)
siteV1CtrlControllerRebootControllerWithoutSavingRecords.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    siteV1CtrlControllerRebootControllerWithoutSavingRecords.setStatus("current")
_SiteV1CtrlNetworkApplyNetworkConf_Type = DisplayString
_SiteV1CtrlNetworkApplyNetworkConf_Object = MibScalar
siteV1CtrlNetworkApplyNetworkConf = _SiteV1CtrlNetworkApplyNetworkConf_Object(
    (1, 3, 6, 1, 4, 1, 26854, 3, 2, 1, 16, 3, 6),
    _SiteV1CtrlNetworkApplyNetworkConf_Type()
)
siteV1CtrlNetworkApplyNetworkConf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    siteV1CtrlNetworkApplyNetworkConf.setStatus("current")
_SiteV1CtrlTimeForceSNTPTimeRefresh_Type = DisplayString
_SiteV1CtrlTimeForceSNTPTimeRefresh_Object = MibScalar
siteV1CtrlTimeForceSNTPTimeRefresh = _SiteV1CtrlTimeForceSNTPTimeRefresh_Object(
    (1, 3, 6, 1, 4, 1, 26854, 3, 2, 1, 16, 3, 11),
    _SiteV1CtrlTimeForceSNTPTimeRefresh_Type()
)
siteV1CtrlTimeForceSNTPTimeRefresh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    siteV1CtrlTimeForceSNTPTimeRefresh.setStatus("current")
_SiteV1CtrlTimeSetLocalTime_Type = DisplayString
_SiteV1CtrlTimeSetLocalTime_Object = MibScalar
siteV1CtrlTimeSetLocalTime = _SiteV1CtrlTimeSetLocalTime_Object(
    (1, 3, 6, 1, 4, 1, 26854, 3, 2, 1, 16, 3, 12),
    _SiteV1CtrlTimeSetLocalTime_Type()
)
siteV1CtrlTimeSetLocalTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    siteV1CtrlTimeSetLocalTime.setStatus("current")
_SiteV1CtrlTimeSetUTCTime_Type = DisplayString
_SiteV1CtrlTimeSetUTCTime_Object = MibScalar
siteV1CtrlTimeSetUTCTime = _SiteV1CtrlTimeSetUTCTime_Object(
    (1, 3, 6, 1, 4, 1, 26854, 3, 2, 1, 16, 3, 13),
    _SiteV1CtrlTimeSetUTCTime_Type()
)
siteV1CtrlTimeSetUTCTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    siteV1CtrlTimeSetUTCTime.setStatus("current")
_SiteV1CtrlTimeResetUptime_Type = DisplayString
_SiteV1CtrlTimeResetUptime_Object = MibScalar
siteV1CtrlTimeResetUptime = _SiteV1CtrlTimeResetUptime_Object(
    (1, 3, 6, 1, 4, 1, 26854, 3, 2, 1, 16, 3, 14),
    _SiteV1CtrlTimeResetUptime_Type()
)
siteV1CtrlTimeResetUptime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    siteV1CtrlTimeResetUptime.setStatus("current")
_SiteV1CtrlControllerCleanandSaveXMLUserConf_Type = DisplayString
_SiteV1CtrlControllerCleanandSaveXMLUserConf_Object = MibScalar
siteV1CtrlControllerCleanandSaveXMLUserConf = _SiteV1CtrlControllerCleanandSaveXMLUserConf_Object(
    (1, 3, 6, 1, 4, 1, 26854, 3, 2, 1, 16, 3, 20),
    _SiteV1CtrlControllerCleanandSaveXMLUserConf_Type()
)
siteV1CtrlControllerCleanandSaveXMLUserConf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    siteV1CtrlControllerCleanandSaveXMLUserConf.setStatus("current")
_SiteV1CtrlControllerSaveXMLUserConf_Type = DisplayString
_SiteV1CtrlControllerSaveXMLUserConf_Object = MibScalar
siteV1CtrlControllerSaveXMLUserConf = _SiteV1CtrlControllerSaveXMLUserConf_Object(
    (1, 3, 6, 1, 4, 1, 26854, 3, 2, 1, 16, 3, 21),
    _SiteV1CtrlControllerSaveXMLUserConf_Type()
)
siteV1CtrlControllerSaveXMLUserConf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    siteV1CtrlControllerSaveXMLUserConf.setStatus("current")
_SiteV1CtrlControllerSaveInventory_Type = DisplayString
_SiteV1CtrlControllerSaveInventory_Object = MibScalar
siteV1CtrlControllerSaveInventory = _SiteV1CtrlControllerSaveInventory_Object(
    (1, 3, 6, 1, 4, 1, 26854, 3, 2, 1, 16, 3, 22),
    _SiteV1CtrlControllerSaveInventory_Type()
)
siteV1CtrlControllerSaveInventory.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    siteV1CtrlControllerSaveInventory.setStatus("current")
_SiteV1CtrlDataRecordsSaveDataRecords_Type = DisplayString
_SiteV1CtrlDataRecordsSaveDataRecords_Object = MibScalar
siteV1CtrlDataRecordsSaveDataRecords = _SiteV1CtrlDataRecordsSaveDataRecords_Object(
    (1, 3, 6, 1, 4, 1, 26854, 3, 2, 1, 16, 3, 33),
    _SiteV1CtrlDataRecordsSaveDataRecords_Type()
)
siteV1CtrlDataRecordsSaveDataRecords.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    siteV1CtrlDataRecordsSaveDataRecords.setStatus("current")
_SiteV1CtrlDataRecordsExportDataRecordsinCSV_Type = DisplayString
_SiteV1CtrlDataRecordsExportDataRecordsinCSV_Object = MibScalar
siteV1CtrlDataRecordsExportDataRecordsinCSV = _SiteV1CtrlDataRecordsExportDataRecordsinCSV_Object(
    (1, 3, 6, 1, 4, 1, 26854, 3, 2, 1, 16, 3, 34),
    _SiteV1CtrlDataRecordsExportDataRecordsinCSV_Type()
)
siteV1CtrlDataRecordsExportDataRecordsinCSV.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    siteV1CtrlDataRecordsExportDataRecordsinCSV.setStatus("current")
_SiteV1CtrlDataRecordsArchiveDataRecords_Type = DisplayString
_SiteV1CtrlDataRecordsArchiveDataRecords_Object = MibScalar
siteV1CtrlDataRecordsArchiveDataRecords = _SiteV1CtrlDataRecordsArchiveDataRecords_Object(
    (1, 3, 6, 1, 4, 1, 26854, 3, 2, 1, 16, 3, 35),
    _SiteV1CtrlDataRecordsArchiveDataRecords_Type()
)
siteV1CtrlDataRecordsArchiveDataRecords.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    siteV1CtrlDataRecordsArchiveDataRecords.setStatus("current")
_SiteV1CtrlDataRecordsDeleteAllDataRecords_Type = DisplayString
_SiteV1CtrlDataRecordsDeleteAllDataRecords_Object = MibScalar
siteV1CtrlDataRecordsDeleteAllDataRecords = _SiteV1CtrlDataRecordsDeleteAllDataRecords_Object(
    (1, 3, 6, 1, 4, 1, 26854, 3, 2, 1, 16, 3, 36),
    _SiteV1CtrlDataRecordsDeleteAllDataRecords_Type()
)
siteV1CtrlDataRecordsDeleteAllDataRecords.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    siteV1CtrlDataRecordsDeleteAllDataRecords.setStatus("current")
_SiteV1CtrlControllerEmulateRecords_Type = DisplayString
_SiteV1CtrlControllerEmulateRecords_Object = MibScalar
siteV1CtrlControllerEmulateRecords = _SiteV1CtrlControllerEmulateRecords_Object(
    (1, 3, 6, 1, 4, 1, 26854, 3, 2, 1, 16, 3, 40),
    _SiteV1CtrlControllerEmulateRecords_Type()
)
siteV1CtrlControllerEmulateRecords.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    siteV1CtrlControllerEmulateRecords.setStatus("current")
_SiteV1CtrlControllerReloadTranslations_Type = DisplayString
_SiteV1CtrlControllerReloadTranslations_Object = MibScalar
siteV1CtrlControllerReloadTranslations = _SiteV1CtrlControllerReloadTranslations_Object(
    (1, 3, 6, 1, 4, 1, 26854, 3, 2, 1, 16, 3, 41),
    _SiteV1CtrlControllerReloadTranslations_Type()
)
siteV1CtrlControllerReloadTranslations.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    siteV1CtrlControllerReloadTranslations.setStatus("current")
_SiteV1CtrlControllerReloadLicense_Type = DisplayString
_SiteV1CtrlControllerReloadLicense_Object = MibScalar
siteV1CtrlControllerReloadLicense = _SiteV1CtrlControllerReloadLicense_Object(
    (1, 3, 6, 1, 4, 1, 26854, 3, 2, 1, 16, 3, 51),
    _SiteV1CtrlControllerReloadLicense_Type()
)
siteV1CtrlControllerReloadLicense.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    siteV1CtrlControllerReloadLicense.setStatus("current")
_SiteV1CtrlControllerManageFTPServer_Type = DisplayString
_SiteV1CtrlControllerManageFTPServer_Object = MibScalar
siteV1CtrlControllerManageFTPServer = _SiteV1CtrlControllerManageFTPServer_Object(
    (1, 3, 6, 1, 4, 1, 26854, 3, 2, 1, 16, 3, 55),
    _SiteV1CtrlControllerManageFTPServer_Type()
)
siteV1CtrlControllerManageFTPServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    siteV1CtrlControllerManageFTPServer.setStatus("current")
_SiteV1CtrlInventoryRemoveAbsentEquipments_Type = DisplayString
_SiteV1CtrlInventoryRemoveAbsentEquipments_Object = MibScalar
siteV1CtrlInventoryRemoveAbsentEquipments = _SiteV1CtrlInventoryRemoveAbsentEquipments_Object(
    (1, 3, 6, 1, 4, 1, 26854, 3, 2, 1, 16, 3, 61),
    _SiteV1CtrlInventoryRemoveAbsentEquipments_Type()
)
siteV1CtrlInventoryRemoveAbsentEquipments.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    siteV1CtrlInventoryRemoveAbsentEquipments.setStatus("current")
_SiteV1CtrlInventoryResetCANBusNode_Type = DisplayString
_SiteV1CtrlInventoryResetCANBusNode_Object = MibScalar
siteV1CtrlInventoryResetCANBusNode = _SiteV1CtrlInventoryResetCANBusNode_Object(
    (1, 3, 6, 1, 4, 1, 26854, 3, 2, 1, 16, 3, 81),
    _SiteV1CtrlInventoryResetCANBusNode_Type()
)
siteV1CtrlInventoryResetCANBusNode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    siteV1CtrlInventoryResetCANBusNode.setStatus("current")
_SiteV1CtrlInventorySaveCANOpenLSSConf_Type = DisplayString
_SiteV1CtrlInventorySaveCANOpenLSSConf_Object = MibScalar
siteV1CtrlInventorySaveCANOpenLSSConf = _SiteV1CtrlInventorySaveCANOpenLSSConf_Object(
    (1, 3, 6, 1, 4, 1, 26854, 3, 2, 1, 16, 3, 82),
    _SiteV1CtrlInventorySaveCANOpenLSSConf_Type()
)
siteV1CtrlInventorySaveCANOpenLSSConf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    siteV1CtrlInventorySaveCANOpenLSSConf.setStatus("current")
_SiteV1CtrlInventoryStartNewInventory_Type = DisplayString
_SiteV1CtrlInventoryStartNewInventory_Object = MibScalar
siteV1CtrlInventoryStartNewInventory = _SiteV1CtrlInventoryStartNewInventory_Object(
    (1, 3, 6, 1, 4, 1, 26854, 3, 2, 1, 16, 3, 83),
    _SiteV1CtrlInventoryStartNewInventory_Type()
)
siteV1CtrlInventoryStartNewInventory.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    siteV1CtrlInventoryStartNewInventory.setStatus("current")
_SiteV1CtrlInventoryUpgradeNodeFirmware_Type = DisplayString
_SiteV1CtrlInventoryUpgradeNodeFirmware_Object = MibScalar
siteV1CtrlInventoryUpgradeNodeFirmware = _SiteV1CtrlInventoryUpgradeNodeFirmware_Object(
    (1, 3, 6, 1, 4, 1, 26854, 3, 2, 1, 16, 3, 91),
    _SiteV1CtrlInventoryUpgradeNodeFirmware_Type()
)
siteV1CtrlInventoryUpgradeNodeFirmware.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    siteV1CtrlInventoryUpgradeNodeFirmware.setStatus("current")
_SiteV1CtrlInventoryCancelFirmwareUpgrade_Type = DisplayString
_SiteV1CtrlInventoryCancelFirmwareUpgrade_Object = MibScalar
siteV1CtrlInventoryCancelFirmwareUpgrade = _SiteV1CtrlInventoryCancelFirmwareUpgrade_Object(
    (1, 3, 6, 1, 4, 1, 26854, 3, 2, 1, 16, 3, 92),
    _SiteV1CtrlInventoryCancelFirmwareUpgrade_Type()
)
siteV1CtrlInventoryCancelFirmwareUpgrade.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    siteV1CtrlInventoryCancelFirmwareUpgrade.setStatus("current")
_SiteV1CtrlFilesFlashBinary_Type = DisplayString
_SiteV1CtrlFilesFlashBinary_Object = MibScalar
siteV1CtrlFilesFlashBinary = _SiteV1CtrlFilesFlashBinary_Object(
    (1, 3, 6, 1, 4, 1, 26854, 3, 2, 1, 16, 3, 103),
    _SiteV1CtrlFilesFlashBinary_Type()
)
siteV1CtrlFilesFlashBinary.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    siteV1CtrlFilesFlashBinary.setStatus("current")
_SiteV1CtrlFilesDownloadFileFromUrl_Type = DisplayString
_SiteV1CtrlFilesDownloadFileFromUrl_Object = MibScalar
siteV1CtrlFilesDownloadFileFromUrl = _SiteV1CtrlFilesDownloadFileFromUrl_Object(
    (1, 3, 6, 1, 4, 1, 26854, 3, 2, 1, 16, 3, 110),
    _SiteV1CtrlFilesDownloadFileFromUrl_Type()
)
siteV1CtrlFilesDownloadFileFromUrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    siteV1CtrlFilesDownloadFileFromUrl.setStatus("current")
_SiteV1CtrlFilesDeleteUserUploadedFile_Type = DisplayString
_SiteV1CtrlFilesDeleteUserUploadedFile_Object = MibScalar
siteV1CtrlFilesDeleteUserUploadedFile = _SiteV1CtrlFilesDeleteUserUploadedFile_Object(
    (1, 3, 6, 1, 4, 1, 26854, 3, 2, 1, 16, 3, 111),
    _SiteV1CtrlFilesDeleteUserUploadedFile_Type()
)
siteV1CtrlFilesDeleteUserUploadedFile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    siteV1CtrlFilesDeleteUserUploadedFile.setStatus("current")
_SiteV1CtrlFilesMoveUserUploadedFile_Type = DisplayString
_SiteV1CtrlFilesMoveUserUploadedFile_Object = MibScalar
siteV1CtrlFilesMoveUserUploadedFile = _SiteV1CtrlFilesMoveUserUploadedFile_Object(
    (1, 3, 6, 1, 4, 1, 26854, 3, 2, 1, 16, 3, 112),
    _SiteV1CtrlFilesMoveUserUploadedFile_Type()
)
siteV1CtrlFilesMoveUserUploadedFile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    siteV1CtrlFilesMoveUserUploadedFile.setStatus("current")
_SiteV1CtrlFilesExtractZipFileinuserupload_Type = DisplayString
_SiteV1CtrlFilesExtractZipFileinuserupload_Object = MibScalar
siteV1CtrlFilesExtractZipFileinuserupload = _SiteV1CtrlFilesExtractZipFileinuserupload_Object(
    (1, 3, 6, 1, 4, 1, 26854, 3, 2, 1, 16, 3, 113),
    _SiteV1CtrlFilesExtractZipFileinuserupload_Type()
)
siteV1CtrlFilesExtractZipFileinuserupload.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    siteV1CtrlFilesExtractZipFileinuserupload.setStatus("current")
_SiteV1CtrlEmailSendSummaryEmail_Type = DisplayString
_SiteV1CtrlEmailSendSummaryEmail_Object = MibScalar
siteV1CtrlEmailSendSummaryEmail = _SiteV1CtrlEmailSendSummaryEmail_Object(
    (1, 3, 6, 1, 4, 1, 26854, 3, 2, 1, 16, 3, 120),
    _SiteV1CtrlEmailSendSummaryEmail_Type()
)
siteV1CtrlEmailSendSummaryEmail.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    siteV1CtrlEmailSendSummaryEmail.setStatus("current")
_SiteV1CtrlScriptingControlLuaScript_Type = DisplayString
_SiteV1CtrlScriptingControlLuaScript_Object = MibScalar
siteV1CtrlScriptingControlLuaScript = _SiteV1CtrlScriptingControlLuaScript_Object(
    (1, 3, 6, 1, 4, 1, 26854, 3, 2, 1, 16, 3, 250),
    _SiteV1CtrlScriptingControlLuaScript_Type()
)
siteV1CtrlScriptingControlLuaScript.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    siteV1CtrlScriptingControlLuaScript.setStatus("current")
_SiteV1CtrlControllerAdvancedFunctionGenericCommandExecution_Type = DisplayString
_SiteV1CtrlControllerAdvancedFunctionGenericCommandExecution_Object = MibScalar
siteV1CtrlControllerAdvancedFunctionGenericCommandExecution = _SiteV1CtrlControllerAdvancedFunctionGenericCommandExecution_Object(
    (1, 3, 6, 1, 4, 1, 26854, 3, 2, 1, 16, 3, 300),
    _SiteV1CtrlControllerAdvancedFunctionGenericCommandExecution_Type()
)
siteV1CtrlControllerAdvancedFunctionGenericCommandExecution.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    siteV1CtrlControllerAdvancedFunctionGenericCommandExecution.setStatus("current")
_SiteV1CtrlGenericClearMyEvents_Type = DisplayString
_SiteV1CtrlGenericClearMyEvents_Object = MibScalar
siteV1CtrlGenericClearMyEvents = _SiteV1CtrlGenericClearMyEvents_Object(
    (1, 3, 6, 1, 4, 1, 26854, 3, 2, 1, 16, 3, 501),
    _SiteV1CtrlGenericClearMyEvents_Type()
)
siteV1CtrlGenericClearMyEvents.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    siteV1CtrlGenericClearMyEvents.setStatus("current")
_SiteV1CtrlGenericClearAllEvents_Type = DisplayString
_SiteV1CtrlGenericClearAllEvents_Object = MibScalar
siteV1CtrlGenericClearAllEvents = _SiteV1CtrlGenericClearAllEvents_Object(
    (1, 3, 6, 1, 4, 1, 26854, 3, 2, 1, 16, 3, 502),
    _SiteV1CtrlGenericClearAllEvents_Type()
)
siteV1CtrlGenericClearAllEvents.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    siteV1CtrlGenericClearAllEvents.setStatus("current")
_SiteV1CtrlGenericAddEvent_Type = DisplayString
_SiteV1CtrlGenericAddEvent_Object = MibScalar
siteV1CtrlGenericAddEvent = _SiteV1CtrlGenericAddEvent_Object(
    (1, 3, 6, 1, 4, 1, 26854, 3, 2, 1, 16, 3, 511),
    _SiteV1CtrlGenericAddEvent_Type()
)
siteV1CtrlGenericAddEvent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    siteV1CtrlGenericAddEvent.setStatus("current")
_SiteV1CtrlGenericAddMajorEvent_Type = DisplayString
_SiteV1CtrlGenericAddMajorEvent_Object = MibScalar
siteV1CtrlGenericAddMajorEvent = _SiteV1CtrlGenericAddMajorEvent_Object(
    (1, 3, 6, 1, 4, 1, 26854, 3, 2, 1, 16, 3, 512),
    _SiteV1CtrlGenericAddMajorEvent_Type()
)
siteV1CtrlGenericAddMajorEvent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    siteV1CtrlGenericAddMajorEvent.setStatus("current")
_SiteV1CtrlGenericResetDefaultNamesAndGroups_Type = DisplayString
_SiteV1CtrlGenericResetDefaultNamesAndGroups_Object = MibScalar
siteV1CtrlGenericResetDefaultNamesAndGroups = _SiteV1CtrlGenericResetDefaultNamesAndGroups_Object(
    (1, 3, 6, 1, 4, 1, 26854, 3, 2, 1, 16, 3, 521),
    _SiteV1CtrlGenericResetDefaultNamesAndGroups_Type()
)
siteV1CtrlGenericResetDefaultNamesAndGroups.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    siteV1CtrlGenericResetDefaultNamesAndGroups.setStatus("current")
_SiteV1CtrlGenericResetDefaultNamesAndGroupsRecursive_Type = DisplayString
_SiteV1CtrlGenericResetDefaultNamesAndGroupsRecursive_Object = MibScalar
siteV1CtrlGenericResetDefaultNamesAndGroupsRecursive = _SiteV1CtrlGenericResetDefaultNamesAndGroupsRecursive_Object(
    (1, 3, 6, 1, 4, 1, 26854, 3, 2, 1, 16, 3, 522),
    _SiteV1CtrlGenericResetDefaultNamesAndGroupsRecursive_Type()
)
siteV1CtrlGenericResetDefaultNamesAndGroupsRecursive.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    siteV1CtrlGenericResetDefaultNamesAndGroupsRecursive.setStatus("current")
_SiteV1Notifications_ObjectIdentity = ObjectIdentity
siteV1Notifications = _SiteV1Notifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 26854, 3, 2, 1, 18)
)
_SiteV1NotificationPrefix_ObjectIdentity = ObjectIdentity
siteV1NotificationPrefix = _SiteV1NotificationPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 26854, 3, 2, 1, 18, 0)
)
_SiteV1Compliance_ObjectIdentity = ObjectIdentity
siteV1Compliance = _SiteV1Compliance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 26854, 3, 2, 1, 19)
)
_SiteV1ComplianceGroups_ObjectIdentity = ObjectIdentity
siteV1ComplianceGroups = _SiteV1ComplianceGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 26854, 3, 2, 1, 19, 1)
)
_EnergySystems_ObjectIdentity = ObjectIdentity
energySystems = _EnergySystems_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 26854, 3, 2, 1, 20)
)
_Es1_ObjectIdentity = ObjectIdentity
es1 = _Es1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 26854, 3, 2, 1, 20, 1)
)


class _Es1GlobalStatus_Type(DisplayString):
    """Custom type es1GlobalStatus based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_Es1GlobalStatus_Type.__name__ = "DisplayString"
_Es1GlobalStatus_Object = MibScalar
es1GlobalStatus = _Es1GlobalStatus_Object(
    (1, 3, 6, 1, 4, 1, 26854, 3, 2, 1, 20, 1, 1),
    _Es1GlobalStatus_Type()
)
es1GlobalStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es1GlobalStatus.setStatus("current")
_Es1GlobalAlarmSeverityType_Type = DisplayString
_Es1GlobalAlarmSeverityType_Object = MibScalar
es1GlobalAlarmSeverityType = _Es1GlobalAlarmSeverityType_Object(
    (1, 3, 6, 1, 4, 1, 26854, 3, 2, 1, 20, 1, 2),
    _Es1GlobalAlarmSeverityType_Type()
)
es1GlobalAlarmSeverityType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es1GlobalAlarmSeverityType.setStatus("current")
_Es1GlobalAlarmSeverityLevel_Type = Integer32
_Es1GlobalAlarmSeverityLevel_Object = MibScalar
es1GlobalAlarmSeverityLevel = _Es1GlobalAlarmSeverityLevel_Object(
    (1, 3, 6, 1, 4, 1, 26854, 3, 2, 1, 20, 1, 3),
    _Es1GlobalAlarmSeverityLevel_Type()
)
es1GlobalAlarmSeverityLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es1GlobalAlarmSeverityLevel.setStatus("current")
_Es1GlobalAlarmSeverityTypeInt_Type = Integer32
_Es1GlobalAlarmSeverityTypeInt_Object = MibScalar
es1GlobalAlarmSeverityTypeInt = _Es1GlobalAlarmSeverityTypeInt_Object(
    (1, 3, 6, 1, 4, 1, 26854, 3, 2, 1, 20, 1, 4),
    _Es1GlobalAlarmSeverityTypeInt_Type()
)
es1GlobalAlarmSeverityTypeInt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es1GlobalAlarmSeverityTypeInt.setStatus("current")
_Es1Description_ObjectIdentity = ObjectIdentity
es1Description = _Es1Description_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 26854, 3, 2, 1, 20, 1, 10)
)
_Es1DescriptionNumber_Type = Integer32
_Es1DescriptionNumber_Object = MibScalar
es1DescriptionNumber = _Es1DescriptionNumber_Object(
    (1, 3, 6, 1, 4, 1, 26854, 3, 2, 1, 20, 1, 10, 1),
    _Es1DescriptionNumber_Type()
)
es1DescriptionNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es1DescriptionNumber.setStatus("current")
_Es1DescriptionTable_Object = MibTable
es1DescriptionTable = _Es1DescriptionTable_Object(
    (1, 3, 6, 1, 4, 1, 26854, 3, 2, 1, 20, 1, 10, 2)
)
if mibBuilder.loadTexts:
    es1DescriptionTable.setStatus("current")
_Es1DescriptionEntry_Object = MibTableRow
es1DescriptionEntry = _Es1DescriptionEntry_Object(
    (1, 3, 6, 1, 4, 1, 26854, 3, 2, 1, 20, 1, 10, 2, 1)
)
es1DescriptionEntry.setIndexNames(
    (0, "SITE-MONITORING-MIB", "es1DescriptionIndex"),
)
if mibBuilder.loadTexts:
    es1DescriptionEntry.setStatus("current")
_Es1DescriptionIndex_Type = Unsigned32
_Es1DescriptionIndex_Object = MibTableColumn
es1DescriptionIndex = _Es1DescriptionIndex_Object(
    (1, 3, 6, 1, 4, 1, 26854, 3, 2, 1, 20, 1, 10, 2, 1, 1),
    _Es1DescriptionIndex_Type()
)
es1DescriptionIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    es1DescriptionIndex.setStatus("current")
_Es1DescriptionName_Type = DisplayString
_Es1DescriptionName_Object = MibTableColumn
es1DescriptionName = _Es1DescriptionName_Object(
    (1, 3, 6, 1, 4, 1, 26854, 3, 2, 1, 20, 1, 10, 2, 1, 2),
    _Es1DescriptionName_Type()
)
es1DescriptionName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es1DescriptionName.setStatus("current")
_Es1DescriptionValue_Type = DisplayString
_Es1DescriptionValue_Object = MibTableColumn
es1DescriptionValue = _Es1DescriptionValue_Object(
    (1, 3, 6, 1, 4, 1, 26854, 3, 2, 1, 20, 1, 10, 2, 1, 3),
    _Es1DescriptionValue_Type()
)
es1DescriptionValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    es1DescriptionValue.setStatus("current")
_Es1DescriptionEntryStatus_Type = RowStatus
_Es1DescriptionEntryStatus_Object = MibTableColumn
es1DescriptionEntryStatus = _Es1DescriptionEntryStatus_Object(
    (1, 3, 6, 1, 4, 1, 26854, 3, 2, 1, 20, 1, 10, 2, 1, 4),
    _Es1DescriptionEntryStatus_Type()
)
es1DescriptionEntryStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    es1DescriptionEntryStatus.setStatus("current")
_Es1DescriptionList_ObjectIdentity = ObjectIdentity
es1DescriptionList = _Es1DescriptionList_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 26854, 3, 2, 1, 20, 1, 10, 3)
)
_Es1DescDescriptionDescription_Type = DisplayString
_Es1DescDescriptionDescription_Object = MibScalar
es1DescDescriptionDescription = _Es1DescDescriptionDescription_Object(
    (1, 3, 6, 1, 4, 1, 26854, 3, 2, 1, 20, 1, 10, 3, 1),
    _Es1DescDescriptionDescription_Type()
)
es1DescDescriptionDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es1DescDescriptionDescription.setStatus("current")
_Es1DescDescriptionReference_Type = DisplayString
_Es1DescDescriptionReference_Object = MibScalar
es1DescDescriptionReference = _Es1DescDescriptionReference_Object(
    (1, 3, 6, 1, 4, 1, 26854, 3, 2, 1, 20, 1, 10, 3, 2),
    _Es1DescDescriptionReference_Type()
)
es1DescDescriptionReference.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es1DescDescriptionReference.setStatus("current")
_Es1Alarm_ObjectIdentity = ObjectIdentity
es1Alarm = _Es1Alarm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 26854, 3, 2, 1, 20, 1, 11)
)
_Es1AlarmNumber_Type = Integer32
_Es1AlarmNumber_Object = MibScalar
es1AlarmNumber = _Es1AlarmNumber_Object(
    (1, 3, 6, 1, 4, 1, 26854, 3, 2, 1, 20, 1, 11, 1),
    _Es1AlarmNumber_Type()
)
es1AlarmNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es1AlarmNumber.setStatus("current")
_Es1AlarmTable_Object = MibTable
es1AlarmTable = _Es1AlarmTable_Object(
    (1, 3, 6, 1, 4, 1, 26854, 3, 2, 1, 20, 1, 11, 2)
)
if mibBuilder.loadTexts:
    es1AlarmTable.setStatus("current")
_Es1AlarmEntry_Object = MibTableRow
es1AlarmEntry = _Es1AlarmEntry_Object(
    (1, 3, 6, 1, 4, 1, 26854, 3, 2, 1, 20, 1, 11, 2, 1)
)
es1AlarmEntry.setIndexNames(
    (0, "SITE-MONITORING-MIB", "es1AlarmIndex"),
)
if mibBuilder.loadTexts:
    es1AlarmEntry.setStatus("current")
_Es1AlarmIndex_Type = Unsigned32
_Es1AlarmIndex_Object = MibTableColumn
es1AlarmIndex = _Es1AlarmIndex_Object(
    (1, 3, 6, 1, 4, 1, 26854, 3, 2, 1, 20, 1, 11, 2, 1, 1),
    _Es1AlarmIndex_Type()
)
es1AlarmIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    es1AlarmIndex.setStatus("current")
_Es1AlarmName_Type = DisplayString
_Es1AlarmName_Object = MibTableColumn
es1AlarmName = _Es1AlarmName_Object(
    (1, 3, 6, 1, 4, 1, 26854, 3, 2, 1, 20, 1, 11, 2, 1, 2),
    _Es1AlarmName_Type()
)
es1AlarmName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es1AlarmName.setStatus("current")
_Es1AlarmActive_Type = DisplayString
_Es1AlarmActive_Object = MibTableColumn
es1AlarmActive = _Es1AlarmActive_Object(
    (1, 3, 6, 1, 4, 1, 26854, 3, 2, 1, 20, 1, 11, 2, 1, 3),
    _Es1AlarmActive_Type()
)
es1AlarmActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es1AlarmActive.setStatus("current")
_Es1AlarmSeverityType_Type = DisplayString
_Es1AlarmSeverityType_Object = MibTableColumn
es1AlarmSeverityType = _Es1AlarmSeverityType_Object(
    (1, 3, 6, 1, 4, 1, 26854, 3, 2, 1, 20, 1, 11, 2, 1, 4),
    _Es1AlarmSeverityType_Type()
)
es1AlarmSeverityType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es1AlarmSeverityType.setStatus("current")
_Es1AlarmSeverityLevel_Type = DisplayString
_Es1AlarmSeverityLevel_Object = MibTableColumn
es1AlarmSeverityLevel = _Es1AlarmSeverityLevel_Object(
    (1, 3, 6, 1, 4, 1, 26854, 3, 2, 1, 20, 1, 11, 2, 1, 5),
    _Es1AlarmSeverityLevel_Type()
)
es1AlarmSeverityLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es1AlarmSeverityLevel.setStatus("current")
_Es1AlarmStartTime_Type = DisplayString
_Es1AlarmStartTime_Object = MibTableColumn
es1AlarmStartTime = _Es1AlarmStartTime_Object(
    (1, 3, 6, 1, 4, 1, 26854, 3, 2, 1, 20, 1, 11, 2, 1, 6),
    _Es1AlarmStartTime_Type()
)
es1AlarmStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es1AlarmStartTime.setStatus("current")
_Es1AlarmStopTime_Type = DisplayString
_Es1AlarmStopTime_Object = MibTableColumn
es1AlarmStopTime = _Es1AlarmStopTime_Object(
    (1, 3, 6, 1, 4, 1, 26854, 3, 2, 1, 20, 1, 11, 2, 1, 7),
    _Es1AlarmStopTime_Type()
)
es1AlarmStopTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es1AlarmStopTime.setStatus("current")
_Es1AlarmEntryStatus_Type = RowStatus
_Es1AlarmEntryStatus_Object = MibTableColumn
es1AlarmEntryStatus = _Es1AlarmEntryStatus_Object(
    (1, 3, 6, 1, 4, 1, 26854, 3, 2, 1, 20, 1, 11, 2, 1, 8),
    _Es1AlarmEntryStatus_Type()
)
es1AlarmEntryStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    es1AlarmEntryStatus.setStatus("current")


class _Es1AlarmSummary_Type(Bits):
    """Custom type es1AlarmSummary based on Bits"""
    namedValues = NamedValues(
        ("none", 0)
    )

_Es1AlarmSummary_Type.__name__ = "Bits"
_Es1AlarmSummary_Object = MibScalar
es1AlarmSummary = _Es1AlarmSummary_Object(
    (1, 3, 6, 1, 4, 1, 26854, 3, 2, 1, 20, 1, 11, 3),
    _Es1AlarmSummary_Type()
)
es1AlarmSummary.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es1AlarmSummary.setStatus("current")
_Es1Event_ObjectIdentity = ObjectIdentity
es1Event = _Es1Event_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 26854, 3, 2, 1, 20, 1, 12)
)
_Es1EventNumber_Type = Integer32
_Es1EventNumber_Object = MibScalar
es1EventNumber = _Es1EventNumber_Object(
    (1, 3, 6, 1, 4, 1, 26854, 3, 2, 1, 20, 1, 12, 1),
    _Es1EventNumber_Type()
)
es1EventNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es1EventNumber.setStatus("current")
_Es1EventTable_Object = MibTable
es1EventTable = _Es1EventTable_Object(
    (1, 3, 6, 1, 4, 1, 26854, 3, 2, 1, 20, 1, 12, 2)
)
if mibBuilder.loadTexts:
    es1EventTable.setStatus("current")
_Es1EventEntry_Object = MibTableRow
es1EventEntry = _Es1EventEntry_Object(
    (1, 3, 6, 1, 4, 1, 26854, 3, 2, 1, 20, 1, 12, 2, 1)
)
es1EventEntry.setIndexNames(
    (0, "SITE-MONITORING-MIB", "es1EventIndex"),
)
if mibBuilder.loadTexts:
    es1EventEntry.setStatus("current")
_Es1EventIndex_Type = Unsigned32
_Es1EventIndex_Object = MibTableColumn
es1EventIndex = _Es1EventIndex_Object(
    (1, 3, 6, 1, 4, 1, 26854, 3, 2, 1, 20, 1, 12, 2, 1, 1),
    _Es1EventIndex_Type()
)
es1EventIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    es1EventIndex.setStatus("current")
_Es1EventId_Type = Unsigned32
_Es1EventId_Object = MibTableColumn
es1EventId = _Es1EventId_Object(
    (1, 3, 6, 1, 4, 1, 26854, 3, 2, 1, 20, 1, 12, 2, 1, 2),
    _Es1EventId_Type()
)
es1EventId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es1EventId.setStatus("current")
_Es1EventName_Type = DisplayString
_Es1EventName_Object = MibTableColumn
es1EventName = _Es1EventName_Object(
    (1, 3, 6, 1, 4, 1, 26854, 3, 2, 1, 20, 1, 12, 2, 1, 3),
    _Es1EventName_Type()
)
es1EventName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es1EventName.setStatus("current")
_Es1EventDateTime_Type = DisplayString
_Es1EventDateTime_Object = MibTableColumn
es1EventDateTime = _Es1EventDateTime_Object(
    (1, 3, 6, 1, 4, 1, 26854, 3, 2, 1, 20, 1, 12, 2, 1, 4),
    _Es1EventDateTime_Type()
)
es1EventDateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es1EventDateTime.setStatus("current")
_Es1EventSeverityType_Type = DisplayString
_Es1EventSeverityType_Object = MibTableColumn
es1EventSeverityType = _Es1EventSeverityType_Object(
    (1, 3, 6, 1, 4, 1, 26854, 3, 2, 1, 20, 1, 12, 2, 1, 5),
    _Es1EventSeverityType_Type()
)
es1EventSeverityType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es1EventSeverityType.setStatus("current")
_Es1EventSeverityLevel_Type = DisplayString
_Es1EventSeverityLevel_Object = MibTableColumn
es1EventSeverityLevel = _Es1EventSeverityLevel_Object(
    (1, 3, 6, 1, 4, 1, 26854, 3, 2, 1, 20, 1, 12, 2, 1, 6),
    _Es1EventSeverityLevel_Type()
)
es1EventSeverityLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es1EventSeverityLevel.setStatus("current")
_Es1EventEntryStatus_Type = RowStatus
_Es1EventEntryStatus_Object = MibTableColumn
es1EventEntryStatus = _Es1EventEntryStatus_Object(
    (1, 3, 6, 1, 4, 1, 26854, 3, 2, 1, 20, 1, 12, 2, 1, 7),
    _Es1EventEntryStatus_Type()
)
es1EventEntryStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    es1EventEntryStatus.setStatus("current")
_Es1Data_ObjectIdentity = ObjectIdentity
es1Data = _Es1Data_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 26854, 3, 2, 1, 20, 1, 13)
)
_Es1DataNumber_Type = Integer32
_Es1DataNumber_Object = MibScalar
es1DataNumber = _Es1DataNumber_Object(
    (1, 3, 6, 1, 4, 1, 26854, 3, 2, 1, 20, 1, 13, 1),
    _Es1DataNumber_Type()
)
es1DataNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es1DataNumber.setStatus("current")
_Es1Config_ObjectIdentity = ObjectIdentity
es1Config = _Es1Config_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 26854, 3, 2, 1, 20, 1, 15)
)
_Es1ConfigNumber_Type = Integer32
_Es1ConfigNumber_Object = MibScalar
es1ConfigNumber = _Es1ConfigNumber_Object(
    (1, 3, 6, 1, 4, 1, 26854, 3, 2, 1, 20, 1, 15, 1),
    _Es1ConfigNumber_Type()
)
es1ConfigNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es1ConfigNumber.setStatus("current")
_Es1ConfigTable_Object = MibTable
es1ConfigTable = _Es1ConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 26854, 3, 2, 1, 20, 1, 15, 2)
)
if mibBuilder.loadTexts:
    es1ConfigTable.setStatus("current")
_Es1ConfigEntry_Object = MibTableRow
es1ConfigEntry = _Es1ConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 26854, 3, 2, 1, 20, 1, 15, 2, 1)
)
es1ConfigEntry.setIndexNames(
    (0, "SITE-MONITORING-MIB", "es1ConfigIndex"),
)
if mibBuilder.loadTexts:
    es1ConfigEntry.setStatus("current")
_Es1ConfigIndex_Type = Unsigned32
_Es1ConfigIndex_Object = MibTableColumn
es1ConfigIndex = _Es1ConfigIndex_Object(
    (1, 3, 6, 1, 4, 1, 26854, 3, 2, 1, 20, 1, 15, 2, 1, 1),
    _Es1ConfigIndex_Type()
)
es1ConfigIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    es1ConfigIndex.setStatus("current")
_Es1ConfigName_Type = DisplayString
_Es1ConfigName_Object = MibTableColumn
es1ConfigName = _Es1ConfigName_Object(
    (1, 3, 6, 1, 4, 1, 26854, 3, 2, 1, 20, 1, 15, 2, 1, 2),
    _Es1ConfigName_Type()
)
es1ConfigName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es1ConfigName.setStatus("current")
_Es1ConfigValue_Type = DisplayString
_Es1ConfigValue_Object = MibTableColumn
es1ConfigValue = _Es1ConfigValue_Object(
    (1, 3, 6, 1, 4, 1, 26854, 3, 2, 1, 20, 1, 15, 2, 1, 3),
    _Es1ConfigValue_Type()
)
es1ConfigValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es1ConfigValue.setStatus("current")
_Es1ConfigEntryStatus_Type = RowStatus
_Es1ConfigEntryStatus_Object = MibTableColumn
es1ConfigEntryStatus = _Es1ConfigEntryStatus_Object(
    (1, 3, 6, 1, 4, 1, 26854, 3, 2, 1, 20, 1, 15, 2, 1, 4),
    _Es1ConfigEntryStatus_Type()
)
es1ConfigEntryStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    es1ConfigEntryStatus.setStatus("current")
_Es1ConfigList_ObjectIdentity = ObjectIdentity
es1ConfigList = _Es1ConfigList_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 26854, 3, 2, 1, 20, 1, 15, 3)
)
_Es1CfgEnergyMeterNumberOfGenericPulseEnergyCounter_Type = DisplayString
_Es1CfgEnergyMeterNumberOfGenericPulseEnergyCounter_Object = MibScalar
es1CfgEnergyMeterNumberOfGenericPulseEnergyCounter = _Es1CfgEnergyMeterNumberOfGenericPulseEnergyCounter_Object(
    (1, 3, 6, 1, 4, 1, 26854, 3, 2, 1, 20, 1, 15, 3, 100),
    _Es1CfgEnergyMeterNumberOfGenericPulseEnergyCounter_Type()
)
es1CfgEnergyMeterNumberOfGenericPulseEnergyCounter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es1CfgEnergyMeterNumberOfGenericPulseEnergyCounter.setStatus("current")
_Es1Control_ObjectIdentity = ObjectIdentity
es1Control = _Es1Control_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 26854, 3, 2, 1, 20, 1, 16)
)
_Es1ControlNumber_Type = Integer32
_Es1ControlNumber_Object = MibScalar
es1ControlNumber = _Es1ControlNumber_Object(
    (1, 3, 6, 1, 4, 1, 26854, 3, 2, 1, 20, 1, 16, 1),
    _Es1ControlNumber_Type()
)
es1ControlNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es1ControlNumber.setStatus("current")
_Es1ControlTable_Object = MibTable
es1ControlTable = _Es1ControlTable_Object(
    (1, 3, 6, 1, 4, 1, 26854, 3, 2, 1, 20, 1, 16, 2)
)
if mibBuilder.loadTexts:
    es1ControlTable.setStatus("current")
_Es1ControlEntry_Object = MibTableRow
es1ControlEntry = _Es1ControlEntry_Object(
    (1, 3, 6, 1, 4, 1, 26854, 3, 2, 1, 20, 1, 16, 2, 1)
)
es1ControlEntry.setIndexNames(
    (0, "SITE-MONITORING-MIB", "es1ControlIndex"),
)
if mibBuilder.loadTexts:
    es1ControlEntry.setStatus("current")
_Es1ControlIndex_Type = Unsigned32
_Es1ControlIndex_Object = MibTableColumn
es1ControlIndex = _Es1ControlIndex_Object(
    (1, 3, 6, 1, 4, 1, 26854, 3, 2, 1, 20, 1, 16, 2, 1, 1),
    _Es1ControlIndex_Type()
)
es1ControlIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    es1ControlIndex.setStatus("current")
_Es1ControlName_Type = DisplayString
_Es1ControlName_Object = MibTableColumn
es1ControlName = _Es1ControlName_Object(
    (1, 3, 6, 1, 4, 1, 26854, 3, 2, 1, 20, 1, 16, 2, 1, 2),
    _Es1ControlName_Type()
)
es1ControlName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es1ControlName.setStatus("current")
_Es1ControlValue_Type = DisplayString
_Es1ControlValue_Object = MibTableColumn
es1ControlValue = _Es1ControlValue_Object(
    (1, 3, 6, 1, 4, 1, 26854, 3, 2, 1, 20, 1, 16, 2, 1, 3),
    _Es1ControlValue_Type()
)
es1ControlValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es1ControlValue.setStatus("current")
_Es1ControlEntryStatus_Type = RowStatus
_Es1ControlEntryStatus_Object = MibTableColumn
es1ControlEntryStatus = _Es1ControlEntryStatus_Object(
    (1, 3, 6, 1, 4, 1, 26854, 3, 2, 1, 20, 1, 16, 2, 1, 4),
    _Es1ControlEntryStatus_Type()
)
es1ControlEntryStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    es1ControlEntryStatus.setStatus("current")
_Es1ControlList_ObjectIdentity = ObjectIdentity
es1ControlList = _Es1ControlList_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 26854, 3, 2, 1, 20, 1, 16, 3)
)
_Es1CtrlGenericClearMyEvents_Type = DisplayString
_Es1CtrlGenericClearMyEvents_Object = MibScalar
es1CtrlGenericClearMyEvents = _Es1CtrlGenericClearMyEvents_Object(
    (1, 3, 6, 1, 4, 1, 26854, 3, 2, 1, 20, 1, 16, 3, 501),
    _Es1CtrlGenericClearMyEvents_Type()
)
es1CtrlGenericClearMyEvents.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es1CtrlGenericClearMyEvents.setStatus("current")
_Es1CtrlGenericClearAllEvents_Type = DisplayString
_Es1CtrlGenericClearAllEvents_Object = MibScalar
es1CtrlGenericClearAllEvents = _Es1CtrlGenericClearAllEvents_Object(
    (1, 3, 6, 1, 4, 1, 26854, 3, 2, 1, 20, 1, 16, 3, 502),
    _Es1CtrlGenericClearAllEvents_Type()
)
es1CtrlGenericClearAllEvents.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es1CtrlGenericClearAllEvents.setStatus("current")
_Es1CtrlGenericAddEvent_Type = DisplayString
_Es1CtrlGenericAddEvent_Object = MibScalar
es1CtrlGenericAddEvent = _Es1CtrlGenericAddEvent_Object(
    (1, 3, 6, 1, 4, 1, 26854, 3, 2, 1, 20, 1, 16, 3, 511),
    _Es1CtrlGenericAddEvent_Type()
)
es1CtrlGenericAddEvent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es1CtrlGenericAddEvent.setStatus("current")
_Es1CtrlGenericAddMajorEvent_Type = DisplayString
_Es1CtrlGenericAddMajorEvent_Object = MibScalar
es1CtrlGenericAddMajorEvent = _Es1CtrlGenericAddMajorEvent_Object(
    (1, 3, 6, 1, 4, 1, 26854, 3, 2, 1, 20, 1, 16, 3, 512),
    _Es1CtrlGenericAddMajorEvent_Type()
)
es1CtrlGenericAddMajorEvent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es1CtrlGenericAddMajorEvent.setStatus("current")
_Es1CtrlGenericResetDefaultNamesAndGroups_Type = DisplayString
_Es1CtrlGenericResetDefaultNamesAndGroups_Object = MibScalar
es1CtrlGenericResetDefaultNamesAndGroups = _Es1CtrlGenericResetDefaultNamesAndGroups_Object(
    (1, 3, 6, 1, 4, 1, 26854, 3, 2, 1, 20, 1, 16, 3, 521),
    _Es1CtrlGenericResetDefaultNamesAndGroups_Type()
)
es1CtrlGenericResetDefaultNamesAndGroups.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es1CtrlGenericResetDefaultNamesAndGroups.setStatus("current")
_Es1CtrlGenericResetDefaultNamesAndGroupsRecursive_Type = DisplayString
_Es1CtrlGenericResetDefaultNamesAndGroupsRecursive_Object = MibScalar
es1CtrlGenericResetDefaultNamesAndGroupsRecursive = _Es1CtrlGenericResetDefaultNamesAndGroupsRecursive_Object(
    (1, 3, 6, 1, 4, 1, 26854, 3, 2, 1, 20, 1, 16, 3, 522),
    _Es1CtrlGenericResetDefaultNamesAndGroupsRecursive_Type()
)
es1CtrlGenericResetDefaultNamesAndGroupsRecursive.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es1CtrlGenericResetDefaultNamesAndGroupsRecursive.setStatus("current")
_Es1Notifications_ObjectIdentity = ObjectIdentity
es1Notifications = _Es1Notifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 26854, 3, 2, 1, 20, 1, 18)
)
_Es1NotificationPrefix_ObjectIdentity = ObjectIdentity
es1NotificationPrefix = _Es1NotificationPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 26854, 3, 2, 1, 20, 1, 18, 0)
)
_Es1Compliance_ObjectIdentity = ObjectIdentity
es1Compliance = _Es1Compliance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 26854, 3, 2, 1, 20, 1, 19)
)
_Es1ComplianceGroups_ObjectIdentity = ObjectIdentity
es1ComplianceGroups = _Es1ComplianceGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 26854, 3, 2, 1, 20, 1, 19, 1)
)
_Es1DCSystems_ObjectIdentity = ObjectIdentity
es1DCSystems = _Es1DCSystems_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 26854, 3, 2, 1, 20, 1, 20)
)
_Es1dc1_ObjectIdentity = ObjectIdentity
es1dc1 = _Es1dc1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 26854, 3, 2, 1, 20, 1, 20, 1)
)


class _Es1dc1GlobalStatus_Type(DisplayString):
    """Custom type es1dc1GlobalStatus based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_Es1dc1GlobalStatus_Type.__name__ = "DisplayString"
_Es1dc1GlobalStatus_Object = MibScalar
es1dc1GlobalStatus = _Es1dc1GlobalStatus_Object(
    (1, 3, 6, 1, 4, 1, 26854, 3, 2, 1, 20, 1, 20, 1, 1),
    _Es1dc1GlobalStatus_Type()
)
es1dc1GlobalStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es1dc1GlobalStatus.setStatus("current")
_Es1dc1GlobalAlarmSeverityType_Type = DisplayString
_Es1dc1GlobalAlarmSeverityType_Object = MibScalar
es1dc1GlobalAlarmSeverityType = _Es1dc1GlobalAlarmSeverityType_Object(
    (1, 3, 6, 1, 4, 1, 26854, 3, 2, 1, 20, 1, 20, 1, 2),
    _Es1dc1GlobalAlarmSeverityType_Type()
)
es1dc1GlobalAlarmSeverityType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es1dc1GlobalAlarmSeverityType.setStatus("current")
_Es1dc1GlobalAlarmSeverityLevel_Type = Integer32
_Es1dc1GlobalAlarmSeverityLevel_Object = MibScalar
es1dc1GlobalAlarmSeverityLevel = _Es1dc1GlobalAlarmSeverityLevel_Object(
    (1, 3, 6, 1, 4, 1, 26854, 3, 2, 1, 20, 1, 20, 1, 3),
    _Es1dc1GlobalAlarmSeverityLevel_Type()
)
es1dc1GlobalAlarmSeverityLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es1dc1GlobalAlarmSeverityLevel.setStatus("current")
_Es1dc1GlobalAlarmSeverityTypeInt_Type = Integer32
_Es1dc1GlobalAlarmSeverityTypeInt_Object = MibScalar
es1dc1GlobalAlarmSeverityTypeInt = _Es1dc1GlobalAlarmSeverityTypeInt_Object(
    (1, 3, 6, 1, 4, 1, 26854, 3, 2, 1, 20, 1, 20, 1, 4),
    _Es1dc1GlobalAlarmSeverityTypeInt_Type()
)
es1dc1GlobalAlarmSeverityTypeInt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es1dc1GlobalAlarmSeverityTypeInt.setStatus("current")
_Es1dc1Description_ObjectIdentity = ObjectIdentity
es1dc1Description = _Es1dc1Description_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 26854, 3, 2, 1, 20, 1, 20, 1, 10)
)
_Es1dc1DescriptionNumber_Type = Integer32
_Es1dc1DescriptionNumber_Object = MibScalar
es1dc1DescriptionNumber = _Es1dc1DescriptionNumber_Object(
    (1, 3, 6, 1, 4, 1, 26854, 3, 2, 1, 20, 1, 20, 1, 10, 1),
    _Es1dc1DescriptionNumber_Type()
)
es1dc1DescriptionNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es1dc1DescriptionNumber.setStatus("current")
_Es1dc1DescriptionTable_Object = MibTable
es1dc1DescriptionTable = _Es1dc1DescriptionTable_Object(
    (1, 3, 6, 1, 4, 1, 26854, 3, 2, 1, 20, 1, 20, 1, 10, 2)
)
if mibBuilder.loadTexts:
    es1dc1DescriptionTable.setStatus("current")
_Es1dc1DescriptionEntry_Object = MibTableRow
es1dc1DescriptionEntry = _Es1dc1DescriptionEntry_Object(
    (1, 3, 6, 1, 4, 1, 26854, 3, 2, 1, 20, 1, 20, 1, 10, 2, 1)
)
es1dc1DescriptionEntry.setIndexNames(
    (0, "SITE-MONITORING-MIB", "es1dc1DescriptionIndex"),
)
if mibBuilder.loadTexts:
    es1dc1DescriptionEntry.setStatus("current")
_Es1dc1DescriptionIndex_Type = Unsigned32
_Es1dc1DescriptionIndex_Object = MibTableColumn
es1dc1DescriptionIndex = _Es1dc1DescriptionIndex_Object(
    (1, 3, 6, 1, 4, 1, 26854, 3, 2, 1, 20, 1, 20, 1, 10, 2, 1, 1),
    _Es1dc1DescriptionIndex_Type()
)
es1dc1DescriptionIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    es1dc1DescriptionIndex.setStatus("current")
_Es1dc1DescriptionName_Type = DisplayString
_Es1dc1DescriptionName_Object = MibTableColumn
es1dc1DescriptionName = _Es1dc1DescriptionName_Object(
    (1, 3, 6, 1, 4, 1, 26854, 3, 2, 1, 20, 1, 20, 1, 10, 2, 1, 2),
    _Es1dc1DescriptionName_Type()
)
es1dc1DescriptionName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es1dc1DescriptionName.setStatus("current")
_Es1dc1DescriptionValue_Type = DisplayString
_Es1dc1DescriptionValue_Object = MibTableColumn
es1dc1DescriptionValue = _Es1dc1DescriptionValue_Object(
    (1, 3, 6, 1, 4, 1, 26854, 3, 2, 1, 20, 1, 20, 1, 10, 2, 1, 3),
    _Es1dc1DescriptionValue_Type()
)
es1dc1DescriptionValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    es1dc1DescriptionValue.setStatus("current")
_Es1dc1DescriptionEntryStatus_Type = RowStatus
_Es1dc1DescriptionEntryStatus_Object = MibTableColumn
es1dc1DescriptionEntryStatus = _Es1dc1DescriptionEntryStatus_Object(
    (1, 3, 6, 1, 4, 1, 26854, 3, 2, 1, 20, 1, 20, 1, 10, 2, 1, 4),
    _Es1dc1DescriptionEntryStatus_Type()
)
es1dc1DescriptionEntryStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    es1dc1DescriptionEntryStatus.setStatus("current")
_Es1dc1DescriptionList_ObjectIdentity = ObjectIdentity
es1dc1DescriptionList = _Es1dc1DescriptionList_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 26854, 3, 2, 1, 20, 1, 20, 1, 10, 3)
)
_Es1dc1DescDescriptionDescription_Type = DisplayString
_Es1dc1DescDescriptionDescription_Object = MibScalar
es1dc1DescDescriptionDescription = _Es1dc1DescDescriptionDescription_Object(
    (1, 3, 6, 1, 4, 1, 26854, 3, 2, 1, 20, 1, 20, 1, 10, 3, 1),
    _Es1dc1DescDescriptionDescription_Type()
)
es1dc1DescDescriptionDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es1dc1DescDescriptionDescription.setStatus("current")
_Es1dc1DescDescriptionReference_Type = DisplayString
_Es1dc1DescDescriptionReference_Object = MibScalar
es1dc1DescDescriptionReference = _Es1dc1DescDescriptionReference_Object(
    (1, 3, 6, 1, 4, 1, 26854, 3, 2, 1, 20, 1, 20, 1, 10, 3, 2),
    _Es1dc1DescDescriptionReference_Type()
)
es1dc1DescDescriptionReference.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es1dc1DescDescriptionReference.setStatus("current")
_Es1dc1DescDescriptionProductName_Type = DisplayString
_Es1dc1DescDescriptionProductName_Object = MibScalar
es1dc1DescDescriptionProductName = _Es1dc1DescDescriptionProductName_Object(
    (1, 3, 6, 1, 4, 1, 26854, 3, 2, 1, 20, 1, 20, 1, 10, 3, 11),
    _Es1dc1DescDescriptionProductName_Type()
)
es1dc1DescDescriptionProductName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es1dc1DescDescriptionProductName.setStatus("current")
_Es1dc1DescDescriptionHardwareReference_Type = DisplayString
_Es1dc1DescDescriptionHardwareReference_Object = MibScalar
es1dc1DescDescriptionHardwareReference = _Es1dc1DescDescriptionHardwareReference_Object(
    (1, 3, 6, 1, 4, 1, 26854, 3, 2, 1, 20, 1, 20, 1, 10, 3, 12),
    _Es1dc1DescDescriptionHardwareReference_Type()
)
es1dc1DescDescriptionHardwareReference.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es1dc1DescDescriptionHardwareReference.setStatus("current")
_Es1dc1DescDescriptionSoftwareReference_Type = DisplayString
_Es1dc1DescDescriptionSoftwareReference_Object = MibScalar
es1dc1DescDescriptionSoftwareReference = _Es1dc1DescDescriptionSoftwareReference_Object(
    (1, 3, 6, 1, 4, 1, 26854, 3, 2, 1, 20, 1, 20, 1, 10, 3, 14),
    _Es1dc1DescDescriptionSoftwareReference_Type()
)
es1dc1DescDescriptionSoftwareReference.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es1dc1DescDescriptionSoftwareReference.setStatus("current")
_Es1dc1DescDescriptionSerialNumber_Type = DisplayString
_Es1dc1DescDescriptionSerialNumber_Object = MibScalar
es1dc1DescDescriptionSerialNumber = _Es1dc1DescDescriptionSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 26854, 3, 2, 1, 20, 1, 20, 1, 10, 3, 16),
    _Es1dc1DescDescriptionSerialNumber_Type()
)
es1dc1DescDescriptionSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es1dc1DescDescriptionSerialNumber.setStatus("current")
_Es1dc1DescDescriptionManufacturingDate_Type = DisplayString
_Es1dc1DescDescriptionManufacturingDate_Object = MibScalar
es1dc1DescDescriptionManufacturingDate = _Es1dc1DescDescriptionManufacturingDate_Object(
    (1, 3, 6, 1, 4, 1, 26854, 3, 2, 1, 20, 1, 20, 1, 10, 3, 18),
    _Es1dc1DescDescriptionManufacturingDate_Type()
)
es1dc1DescDescriptionManufacturingDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es1dc1DescDescriptionManufacturingDate.setStatus("current")
_Es1dc1DescDescriptionDistributionModuleProductName_Type = DisplayString
_Es1dc1DescDescriptionDistributionModuleProductName_Object = MibScalar
es1dc1DescDescriptionDistributionModuleProductName = _Es1dc1DescDescriptionDistributionModuleProductName_Object(
    (1, 3, 6, 1, 4, 1, 26854, 3, 2, 1, 20, 1, 20, 1, 10, 3, 31),
    _Es1dc1DescDescriptionDistributionModuleProductName_Type()
)
es1dc1DescDescriptionDistributionModuleProductName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es1dc1DescDescriptionDistributionModuleProductName.setStatus("current")
_Es1dc1DescDescriptionDistributionModuleHardwareReference_Type = DisplayString
_Es1dc1DescDescriptionDistributionModuleHardwareReference_Object = MibScalar
es1dc1DescDescriptionDistributionModuleHardwareReference = _Es1dc1DescDescriptionDistributionModuleHardwareReference_Object(
    (1, 3, 6, 1, 4, 1, 26854, 3, 2, 1, 20, 1, 20, 1, 10, 3, 32),
    _Es1dc1DescDescriptionDistributionModuleHardwareReference_Type()
)
es1dc1DescDescriptionDistributionModuleHardwareReference.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es1dc1DescDescriptionDistributionModuleHardwareReference.setStatus("current")
_Es1dc1DescDescriptionDistributionModuleSoftwareReference_Type = DisplayString
_Es1dc1DescDescriptionDistributionModuleSoftwareReference_Object = MibScalar
es1dc1DescDescriptionDistributionModuleSoftwareReference = _Es1dc1DescDescriptionDistributionModuleSoftwareReference_Object(
    (1, 3, 6, 1, 4, 1, 26854, 3, 2, 1, 20, 1, 20, 1, 10, 3, 34),
    _Es1dc1DescDescriptionDistributionModuleSoftwareReference_Type()
)
es1dc1DescDescriptionDistributionModuleSoftwareReference.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es1dc1DescDescriptionDistributionModuleSoftwareReference.setStatus("current")
_Es1dc1DescDescriptionDistributionModuleSerialNumber_Type = DisplayString
_Es1dc1DescDescriptionDistributionModuleSerialNumber_Object = MibScalar
es1dc1DescDescriptionDistributionModuleSerialNumber = _Es1dc1DescDescriptionDistributionModuleSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 26854, 3, 2, 1, 20, 1, 20, 1, 10, 3, 36),
    _Es1dc1DescDescriptionDistributionModuleSerialNumber_Type()
)
es1dc1DescDescriptionDistributionModuleSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es1dc1DescDescriptionDistributionModuleSerialNumber.setStatus("current")
_Es1dc1DescDescriptionDistributionModuleManufacturingDate_Type = DisplayString
_Es1dc1DescDescriptionDistributionModuleManufacturingDate_Object = MibScalar
es1dc1DescDescriptionDistributionModuleManufacturingDate = _Es1dc1DescDescriptionDistributionModuleManufacturingDate_Object(
    (1, 3, 6, 1, 4, 1, 26854, 3, 2, 1, 20, 1, 20, 1, 10, 3, 38),
    _Es1dc1DescDescriptionDistributionModuleManufacturingDate_Type()
)
es1dc1DescDescriptionDistributionModuleManufacturingDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es1dc1DescDescriptionDistributionModuleManufacturingDate.setStatus("current")
_Es1dc1Alarm_ObjectIdentity = ObjectIdentity
es1dc1Alarm = _Es1dc1Alarm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 26854, 3, 2, 1, 20, 1, 20, 1, 11)
)
_Es1dc1AlarmNumber_Type = Integer32
_Es1dc1AlarmNumber_Object = MibScalar
es1dc1AlarmNumber = _Es1dc1AlarmNumber_Object(
    (1, 3, 6, 1, 4, 1, 26854, 3, 2, 1, 20, 1, 20, 1, 11, 1),
    _Es1dc1AlarmNumber_Type()
)
es1dc1AlarmNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es1dc1AlarmNumber.setStatus("current")
_Es1dc1AlarmTable_Object = MibTable
es1dc1AlarmTable = _Es1dc1AlarmTable_Object(
    (1, 3, 6, 1, 4, 1, 26854, 3, 2, 1, 20, 1, 20, 1, 11, 2)
)
if mibBuilder.loadTexts:
    es1dc1AlarmTable.setStatus("current")
_Es1dc1AlarmEntry_Object = MibTableRow
es1dc1AlarmEntry = _Es1dc1AlarmEntry_Object(
    (1, 3, 6, 1, 4, 1, 26854, 3, 2, 1, 20, 1, 20, 1, 11, 2, 1)
)
es1dc1AlarmEntry.setIndexNames(
    (0, "SITE-MONITORING-MIB", "es1dc1AlarmIndex"),
)
if mibBuilder.loadTexts:
    es1dc1AlarmEntry.setStatus("current")
_Es1dc1AlarmIndex_Type = Unsigned32
_Es1dc1AlarmIndex_Object = MibTableColumn
es1dc1AlarmIndex = _Es1dc1AlarmIndex_Object(
    (1, 3, 6, 1, 4, 1, 26854, 3, 2, 1, 20, 1, 20, 1, 11, 2, 1, 1),
    _Es1dc1AlarmIndex_Type()
)
es1dc1AlarmIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    es1dc1AlarmIndex.setStatus("current")
_Es1dc1AlarmName_Type = DisplayString
_Es1dc1AlarmName_Object = MibTableColumn
es1dc1AlarmName = _Es1dc1AlarmName_Object(
    (1, 3, 6, 1, 4, 1, 26854, 3, 2, 1, 20, 1, 20, 1, 11, 2, 1, 2),
    _Es1dc1AlarmName_Type()
)
es1dc1AlarmName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es1dc1AlarmName.setStatus("current")
_Es1dc1AlarmActive_Type = DisplayString
_Es1dc1AlarmActive_Object = MibTableColumn
es1dc1AlarmActive = _Es1dc1AlarmActive_Object(
    (1, 3, 6, 1, 4, 1, 26854, 3, 2, 1, 20, 1, 20, 1, 11, 2, 1, 3),
    _Es1dc1AlarmActive_Type()
)
es1dc1AlarmActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es1dc1AlarmActive.setStatus("current")
_Es1dc1AlarmSeverityType_Type = DisplayString
_Es1dc1AlarmSeverityType_Object = MibTableColumn
es1dc1AlarmSeverityType = _Es1dc1AlarmSeverityType_Object(
    (1, 3, 6, 1, 4, 1, 26854, 3, 2, 1, 20, 1, 20, 1, 11, 2, 1, 4),
    _Es1dc1AlarmSeverityType_Type()
)
es1dc1AlarmSeverityType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es1dc1AlarmSeverityType.setStatus("current")
_Es1dc1AlarmSeverityLevel_Type = DisplayString
_Es1dc1AlarmSeverityLevel_Object = MibTableColumn
es1dc1AlarmSeverityLevel = _Es1dc1AlarmSeverityLevel_Object(
    (1, 3, 6, 1, 4, 1, 26854, 3, 2, 1, 20, 1, 20, 1, 11, 2, 1, 5),
    _Es1dc1AlarmSeverityLevel_Type()
)
es1dc1AlarmSeverityLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es1dc1AlarmSeverityLevel.setStatus("current")
_Es1dc1AlarmStartTime_Type = DisplayString
_Es1dc1AlarmStartTime_Object = MibTableColumn
es1dc1AlarmStartTime = _Es1dc1AlarmStartTime_Object(
    (1, 3, 6, 1, 4, 1, 26854, 3, 2, 1, 20, 1, 20, 1, 11, 2, 1, 6),
    _Es1dc1AlarmStartTime_Type()
)
es1dc1AlarmStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es1dc1AlarmStartTime.setStatus("current")
_Es1dc1AlarmStopTime_Type = DisplayString
_Es1dc1AlarmStopTime_Object = MibTableColumn
es1dc1AlarmStopTime = _Es1dc1AlarmStopTime_Object(
    (1, 3, 6, 1, 4, 1, 26854, 3, 2, 1, 20, 1, 20, 1, 11, 2, 1, 7),
    _Es1dc1AlarmStopTime_Type()
)
es1dc1AlarmStopTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es1dc1AlarmStopTime.setStatus("current")
_Es1dc1AlarmEntryStatus_Type = RowStatus
_Es1dc1AlarmEntryStatus_Object = MibTableColumn
es1dc1AlarmEntryStatus = _Es1dc1AlarmEntryStatus_Object(
    (1, 3, 6, 1, 4, 1, 26854, 3, 2, 1, 20, 1, 20, 1, 11, 2, 1, 8),
    _Es1dc1AlarmEntryStatus_Type()
)
es1dc1AlarmEntryStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    es1dc1AlarmEntryStatus.setStatus("current")


class _Es1dc1AlarmSummary_Type(Bits):
    """Custom type es1dc1AlarmSummary based on Bits"""
    namedValues = NamedValues(
        *(("dCBusDCBusExtraLow", 0),
          ("dCBusDCBusLow", 1),
          ("dCBusDCBusHigh", 2),
          ("dCBusDCBusExtraHigh", 3),
          ("dCBusDCBusVoltageSenseFail", 4),
          ("aCBusMainsFail", 5),
          ("aCBusMainsPartialFail", 6),
          ("aCBusMainsLow", 7),
          ("rectifiersOneRectifierFail", 9),
          ("rectifiersMoreThanOneRectifierFail", 10),
          ("rectifiersMissingRectifiers", 11),
          ("batBatLastTestFailed", 12),
          ("batBatOnDischarge", 13),
          ("lVDBatLVDRelOpen", 16),
          ("batBatTempTooHigh", 17),
          ("batBatTempTooLow", 18),
          ("batBatTempSensorFail", 19),
          ("sensorsAmbientTempTooHigh", 20),
          ("sensorsAmbientTempTooLow", 21),
          ("sensorsAmbientTempSensorFail", 22),
          ("digInputsDistributionBreakerOpen", 24),
          ("digInputsBatBreakerOpen", 25),
          ("digInputsDigInput1", 26),
          ("digInputsDigInput2", 27),
          ("digInputsDigInput3", 28),
          ("digInputsDigInput4", 29))
    )

_Es1dc1AlarmSummary_Type.__name__ = "Bits"
_Es1dc1AlarmSummary_Object = MibScalar
es1dc1AlarmSummary = _Es1dc1AlarmSummary_Object(
    (1, 3, 6, 1, 4, 1, 26854, 3, 2, 1, 20, 1, 20, 1, 11, 3),
    _Es1dc1AlarmSummary_Type()
)
es1dc1AlarmSummary.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es1dc1AlarmSummary.setStatus("current")
_Es1dc1Event_ObjectIdentity = ObjectIdentity
es1dc1Event = _Es1dc1Event_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 26854, 3, 2, 1, 20, 1, 20, 1, 12)
)
_Es1dc1EventNumber_Type = Integer32
_Es1dc1EventNumber_Object = MibScalar
es1dc1EventNumber = _Es1dc1EventNumber_Object(
    (1, 3, 6, 1, 4, 1, 26854, 3, 2, 1, 20, 1, 20, 1, 12, 1),
    _Es1dc1EventNumber_Type()
)
es1dc1EventNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es1dc1EventNumber.setStatus("current")
_Es1dc1EventTable_Object = MibTable
es1dc1EventTable = _Es1dc1EventTable_Object(
    (1, 3, 6, 1, 4, 1, 26854, 3, 2, 1, 20, 1, 20, 1, 12, 2)
)
if mibBuilder.loadTexts:
    es1dc1EventTable.setStatus("current")
_Es1dc1EventEntry_Object = MibTableRow
es1dc1EventEntry = _Es1dc1EventEntry_Object(
    (1, 3, 6, 1, 4, 1, 26854, 3, 2, 1, 20, 1, 20, 1, 12, 2, 1)
)
es1dc1EventEntry.setIndexNames(
    (0, "SITE-MONITORING-MIB", "es1dc1EventIndex"),
)
if mibBuilder.loadTexts:
    es1dc1EventEntry.setStatus("current")
_Es1dc1EventIndex_Type = Unsigned32
_Es1dc1EventIndex_Object = MibTableColumn
es1dc1EventIndex = _Es1dc1EventIndex_Object(
    (1, 3, 6, 1, 4, 1, 26854, 3, 2, 1, 20, 1, 20, 1, 12, 2, 1, 1),
    _Es1dc1EventIndex_Type()
)
es1dc1EventIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    es1dc1EventIndex.setStatus("current")
_Es1dc1EventId_Type = Unsigned32
_Es1dc1EventId_Object = MibTableColumn
es1dc1EventId = _Es1dc1EventId_Object(
    (1, 3, 6, 1, 4, 1, 26854, 3, 2, 1, 20, 1, 20, 1, 12, 2, 1, 2),
    _Es1dc1EventId_Type()
)
es1dc1EventId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es1dc1EventId.setStatus("current")
_Es1dc1EventName_Type = DisplayString
_Es1dc1EventName_Object = MibTableColumn
es1dc1EventName = _Es1dc1EventName_Object(
    (1, 3, 6, 1, 4, 1, 26854, 3, 2, 1, 20, 1, 20, 1, 12, 2, 1, 3),
    _Es1dc1EventName_Type()
)
es1dc1EventName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es1dc1EventName.setStatus("current")
_Es1dc1EventDateTime_Type = DisplayString
_Es1dc1EventDateTime_Object = MibTableColumn
es1dc1EventDateTime = _Es1dc1EventDateTime_Object(
    (1, 3, 6, 1, 4, 1, 26854, 3, 2, 1, 20, 1, 20, 1, 12, 2, 1, 4),
    _Es1dc1EventDateTime_Type()
)
es1dc1EventDateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es1dc1EventDateTime.setStatus("current")
_Es1dc1EventSeverityType_Type = DisplayString
_Es1dc1EventSeverityType_Object = MibTableColumn
es1dc1EventSeverityType = _Es1dc1EventSeverityType_Object(
    (1, 3, 6, 1, 4, 1, 26854, 3, 2, 1, 20, 1, 20, 1, 12, 2, 1, 5),
    _Es1dc1EventSeverityType_Type()
)
es1dc1EventSeverityType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es1dc1EventSeverityType.setStatus("current")
_Es1dc1EventSeverityLevel_Type = DisplayString
_Es1dc1EventSeverityLevel_Object = MibTableColumn
es1dc1EventSeverityLevel = _Es1dc1EventSeverityLevel_Object(
    (1, 3, 6, 1, 4, 1, 26854, 3, 2, 1, 20, 1, 20, 1, 12, 2, 1, 6),
    _Es1dc1EventSeverityLevel_Type()
)
es1dc1EventSeverityLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es1dc1EventSeverityLevel.setStatus("current")
_Es1dc1EventEntryStatus_Type = RowStatus
_Es1dc1EventEntryStatus_Object = MibTableColumn
es1dc1EventEntryStatus = _Es1dc1EventEntryStatus_Object(
    (1, 3, 6, 1, 4, 1, 26854, 3, 2, 1, 20, 1, 20, 1, 12, 2, 1, 7),
    _Es1dc1EventEntryStatus_Type()
)
es1dc1EventEntryStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    es1dc1EventEntryStatus.setStatus("current")
_Es1dc1Data_ObjectIdentity = ObjectIdentity
es1dc1Data = _Es1dc1Data_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 26854, 3, 2, 1, 20, 1, 20, 1, 13)
)
_Es1dc1DataNumber_Type = Integer32
_Es1dc1DataNumber_Object = MibScalar
es1dc1DataNumber = _Es1dc1DataNumber_Object(
    (1, 3, 6, 1, 4, 1, 26854, 3, 2, 1, 20, 1, 20, 1, 13, 1),
    _Es1dc1DataNumber_Type()
)
es1dc1DataNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es1dc1DataNumber.setStatus("current")
_Es1dc1DataTable_Object = MibTable
es1dc1DataTable = _Es1dc1DataTable_Object(
    (1, 3, 6, 1, 4, 1, 26854, 3, 2, 1, 20, 1, 20, 1, 13, 2)
)
if mibBuilder.loadTexts:
    es1dc1DataTable.setStatus("current")
_Es1dc1DataEntry_Object = MibTableRow
es1dc1DataEntry = _Es1dc1DataEntry_Object(
    (1, 3, 6, 1, 4, 1, 26854, 3, 2, 1, 20, 1, 20, 1, 13, 2, 1)
)
es1dc1DataEntry.setIndexNames(
    (0, "SITE-MONITORING-MIB", "es1dc1DataIndex"),
)
if mibBuilder.loadTexts:
    es1dc1DataEntry.setStatus("current")
_Es1dc1DataIndex_Type = Unsigned32
_Es1dc1DataIndex_Object = MibTableColumn
es1dc1DataIndex = _Es1dc1DataIndex_Object(
    (1, 3, 6, 1, 4, 1, 26854, 3, 2, 1, 20, 1, 20, 1, 13, 2, 1, 1),
    _Es1dc1DataIndex_Type()
)
es1dc1DataIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    es1dc1DataIndex.setStatus("current")
_Es1dc1DataName_Type = DisplayString
_Es1dc1DataName_Object = MibTableColumn
es1dc1DataName = _Es1dc1DataName_Object(
    (1, 3, 6, 1, 4, 1, 26854, 3, 2, 1, 20, 1, 20, 1, 13, 2, 1, 2),
    _Es1dc1DataName_Type()
)
es1dc1DataName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es1dc1DataName.setStatus("current")
_Es1dc1DataValue_Type = DisplayString
_Es1dc1DataValue_Object = MibTableColumn
es1dc1DataValue = _Es1dc1DataValue_Object(
    (1, 3, 6, 1, 4, 1, 26854, 3, 2, 1, 20, 1, 20, 1, 13, 2, 1, 3),
    _Es1dc1DataValue_Type()
)
es1dc1DataValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es1dc1DataValue.setStatus("current")
_Es1dc1DataEntryStatus_Type = RowStatus
_Es1dc1DataEntryStatus_Object = MibTableColumn
es1dc1DataEntryStatus = _Es1dc1DataEntryStatus_Object(
    (1, 3, 6, 1, 4, 1, 26854, 3, 2, 1, 20, 1, 20, 1, 13, 2, 1, 4),
    _Es1dc1DataEntryStatus_Type()
)
es1dc1DataEntryStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    es1dc1DataEntryStatus.setStatus("current")
_Es1dc1DataList_ObjectIdentity = ObjectIdentity
es1dc1DataList = _Es1dc1DataList_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 26854, 3, 2, 1, 20, 1, 20, 1, 13, 3)
)
_Es1dc1DataSystemDCMode_Type = Integer32
_Es1dc1DataSystemDCMode_Object = MibScalar
es1dc1DataSystemDCMode = _Es1dc1DataSystemDCMode_Object(
    (1, 3, 6, 1, 4, 1, 26854, 3, 2, 1, 20, 1, 20, 1, 13, 3, 1),
    _Es1dc1DataSystemDCMode_Type()
)
es1dc1DataSystemDCMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es1dc1DataSystemDCMode.setStatus("current")
_Es1dc1DataSystemPreviousDCMode_Type = Integer32
_Es1dc1DataSystemPreviousDCMode_Object = MibScalar
es1dc1DataSystemPreviousDCMode = _Es1dc1DataSystemPreviousDCMode_Object(
    (1, 3, 6, 1, 4, 1, 26854, 3, 2, 1, 20, 1, 20, 1, 13, 3, 2),
    _Es1dc1DataSystemPreviousDCMode_Type()
)
es1dc1DataSystemPreviousDCMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es1dc1DataSystemPreviousDCMode.setStatus("current")
_Es1dc1DataSystemNiMHChargeMode_Type = Integer32
_Es1dc1DataSystemNiMHChargeMode_Object = MibScalar
es1dc1DataSystemNiMHChargeMode = _Es1dc1DataSystemNiMHChargeMode_Object(
    (1, 3, 6, 1, 4, 1, 26854, 3, 2, 1, 20, 1, 20, 1, 13, 3, 5),
    _Es1dc1DataSystemNiMHChargeMode_Type()
)
es1dc1DataSystemNiMHChargeMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es1dc1DataSystemNiMHChargeMode.setStatus("current")
_Es1dc1DataDCBusBusVoltage_Type = Integer32
_Es1dc1DataDCBusBusVoltage_Object = MibScalar
es1dc1DataDCBusBusVoltage = _Es1dc1DataDCBusBusVoltage_Object(
    (1, 3, 6, 1, 4, 1, 26854, 3, 2, 1, 20, 1, 20, 1, 13, 3, 11),
    _Es1dc1DataDCBusBusVoltage_Type()
)
es1dc1DataDCBusBusVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es1dc1DataDCBusBusVoltage.setStatus("current")
_Es1dc1DataSystemRatioDeliveredOnAvailablePower_Type = Integer32
_Es1dc1DataSystemRatioDeliveredOnAvailablePower_Object = MibScalar
es1dc1DataSystemRatioDeliveredOnAvailablePower = _Es1dc1DataSystemRatioDeliveredOnAvailablePower_Object(
    (1, 3, 6, 1, 4, 1, 26854, 3, 2, 1, 20, 1, 20, 1, 13, 3, 12),
    _Es1dc1DataSystemRatioDeliveredOnAvailablePower_Type()
)
es1dc1DataSystemRatioDeliveredOnAvailablePower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es1dc1DataSystemRatioDeliveredOnAvailablePower.setStatus("current")
_Es1dc1DataACBusMinutesSinceLastACFailBegin_Type = Integer32
_Es1dc1DataACBusMinutesSinceLastACFailBegin_Object = MibScalar
es1dc1DataACBusMinutesSinceLastACFailBegin = _Es1dc1DataACBusMinutesSinceLastACFailBegin_Object(
    (1, 3, 6, 1, 4, 1, 26854, 3, 2, 1, 20, 1, 20, 1, 13, 3, 13),
    _Es1dc1DataACBusMinutesSinceLastACFailBegin_Type()
)
es1dc1DataACBusMinutesSinceLastACFailBegin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es1dc1DataACBusMinutesSinceLastACFailBegin.setStatus("current")
_Es1dc1DataACBusMinutesSinceLastACFailEnd_Type = Integer32
_Es1dc1DataACBusMinutesSinceLastACFailEnd_Object = MibScalar
es1dc1DataACBusMinutesSinceLastACFailEnd = _Es1dc1DataACBusMinutesSinceLastACFailEnd_Object(
    (1, 3, 6, 1, 4, 1, 26854, 3, 2, 1, 20, 1, 20, 1, 13, 3, 14),
    _Es1dc1DataACBusMinutesSinceLastACFailEnd_Type()
)
es1dc1DataACBusMinutesSinceLastACFailEnd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es1dc1DataACBusMinutesSinceLastACFailEnd.setStatus("current")
_Es1dc1DataRectifiersRectifiersOutPower_Type = Integer32
_Es1dc1DataRectifiersRectifiersOutPower_Object = MibScalar
es1dc1DataRectifiersRectifiersOutPower = _Es1dc1DataRectifiersRectifiersOutPower_Object(
    (1, 3, 6, 1, 4, 1, 26854, 3, 2, 1, 20, 1, 20, 1, 13, 3, 21),
    _Es1dc1DataRectifiersRectifiersOutPower_Type()
)
es1dc1DataRectifiersRectifiersOutPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es1dc1DataRectifiersRectifiersOutPower.setStatus("current")
_Es1dc1DataRectifiersRectifiersOutCurrent_Type = Integer32
_Es1dc1DataRectifiersRectifiersOutCurrent_Object = MibScalar
es1dc1DataRectifiersRectifiersOutCurrent = _Es1dc1DataRectifiersRectifiersOutCurrent_Object(
    (1, 3, 6, 1, 4, 1, 26854, 3, 2, 1, 20, 1, 20, 1, 13, 3, 22),
    _Es1dc1DataRectifiersRectifiersOutCurrent_Type()
)
es1dc1DataRectifiersRectifiersOutCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es1dc1DataRectifiersRectifiersOutCurrent.setStatus("current")
_Es1dc1DataRectifiersRectifiersOutPowerMax_Type = Integer32
_Es1dc1DataRectifiersRectifiersOutPowerMax_Object = MibScalar
es1dc1DataRectifiersRectifiersOutPowerMax = _Es1dc1DataRectifiersRectifiersOutPowerMax_Object(
    (1, 3, 6, 1, 4, 1, 26854, 3, 2, 1, 20, 1, 20, 1, 13, 3, 23),
    _Es1dc1DataRectifiersRectifiersOutPowerMax_Type()
)
es1dc1DataRectifiersRectifiersOutPowerMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es1dc1DataRectifiersRectifiersOutPowerMax.setStatus("current")
_Es1dc1DataRectifiersRectifiersOutCurrentMax_Type = Integer32
_Es1dc1DataRectifiersRectifiersOutCurrentMax_Object = MibScalar
es1dc1DataRectifiersRectifiersOutCurrentMax = _Es1dc1DataRectifiersRectifiersOutCurrentMax_Object(
    (1, 3, 6, 1, 4, 1, 26854, 3, 2, 1, 20, 1, 20, 1, 13, 3, 24),
    _Es1dc1DataRectifiersRectifiersOutCurrentMax_Type()
)
es1dc1DataRectifiersRectifiersOutCurrentMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es1dc1DataRectifiersRectifiersOutCurrentMax.setStatus("current")
_Es1dc1DataRectifiersNumberOfRectifierMax_Type = Integer32
_Es1dc1DataRectifiersNumberOfRectifierMax_Object = MibScalar
es1dc1DataRectifiersNumberOfRectifierMax = _Es1dc1DataRectifiersNumberOfRectifierMax_Object(
    (1, 3, 6, 1, 4, 1, 26854, 3, 2, 1, 20, 1, 20, 1, 13, 3, 31),
    _Es1dc1DataRectifiersNumberOfRectifierMax_Type()
)
es1dc1DataRectifiersNumberOfRectifierMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es1dc1DataRectifiersNumberOfRectifierMax.setStatus("current")
_Es1dc1DataRectifiersNumberOfPresentRectifier_Type = Integer32
_Es1dc1DataRectifiersNumberOfPresentRectifier_Object = MibScalar
es1dc1DataRectifiersNumberOfPresentRectifier = _Es1dc1DataRectifiersNumberOfPresentRectifier_Object(
    (1, 3, 6, 1, 4, 1, 26854, 3, 2, 1, 20, 1, 20, 1, 13, 3, 32),
    _Es1dc1DataRectifiersNumberOfPresentRectifier_Type()
)
es1dc1DataRectifiersNumberOfPresentRectifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es1dc1DataRectifiersNumberOfPresentRectifier.setStatus("current")
_Es1dc1DataRectifiersNumberOfAbsentRectifier_Type = Integer32
_Es1dc1DataRectifiersNumberOfAbsentRectifier_Object = MibScalar
es1dc1DataRectifiersNumberOfAbsentRectifier = _Es1dc1DataRectifiersNumberOfAbsentRectifier_Object(
    (1, 3, 6, 1, 4, 1, 26854, 3, 2, 1, 20, 1, 20, 1, 13, 3, 33),
    _Es1dc1DataRectifiersNumberOfAbsentRectifier_Type()
)
es1dc1DataRectifiersNumberOfAbsentRectifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es1dc1DataRectifiersNumberOfAbsentRectifier.setStatus("current")
_Es1dc1DataRectifiersNumberOfActiveRectifier_Type = Integer32
_Es1dc1DataRectifiersNumberOfActiveRectifier_Object = MibScalar
es1dc1DataRectifiersNumberOfActiveRectifier = _Es1dc1DataRectifiersNumberOfActiveRectifier_Object(
    (1, 3, 6, 1, 4, 1, 26854, 3, 2, 1, 20, 1, 20, 1, 13, 3, 34),
    _Es1dc1DataRectifiersNumberOfActiveRectifier_Type()
)
es1dc1DataRectifiersNumberOfActiveRectifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es1dc1DataRectifiersNumberOfActiveRectifier.setStatus("current")
_Es1dc1DataRectifiersNumberOfACFailRectifier_Type = Integer32
_Es1dc1DataRectifiersNumberOfACFailRectifier_Object = MibScalar
es1dc1DataRectifiersNumberOfACFailRectifier = _Es1dc1DataRectifiersNumberOfACFailRectifier_Object(
    (1, 3, 6, 1, 4, 1, 26854, 3, 2, 1, 20, 1, 20, 1, 13, 3, 35),
    _Es1dc1DataRectifiersNumberOfACFailRectifier_Type()
)
es1dc1DataRectifiersNumberOfACFailRectifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es1dc1DataRectifiersNumberOfACFailRectifier.setStatus("current")
_Es1dc1DataRectifiersNumberOfDCFailRectifier_Type = Integer32
_Es1dc1DataRectifiersNumberOfDCFailRectifier_Object = MibScalar
es1dc1DataRectifiersNumberOfDCFailRectifier = _Es1dc1DataRectifiersNumberOfDCFailRectifier_Object(
    (1, 3, 6, 1, 4, 1, 26854, 3, 2, 1, 20, 1, 20, 1, 13, 3, 36),
    _Es1dc1DataRectifiersNumberOfDCFailRectifier_Type()
)
es1dc1DataRectifiersNumberOfDCFailRectifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es1dc1DataRectifiersNumberOfDCFailRectifier.setStatus("current")
_Es1dc1DataRectifiersNumberOfRemoteOffRectifier_Type = Integer32
_Es1dc1DataRectifiersNumberOfRemoteOffRectifier_Object = MibScalar
es1dc1DataRectifiersNumberOfRemoteOffRectifier = _Es1dc1DataRectifiersNumberOfRemoteOffRectifier_Object(
    (1, 3, 6, 1, 4, 1, 26854, 3, 2, 1, 20, 1, 20, 1, 13, 3, 37),
    _Es1dc1DataRectifiersNumberOfRemoteOffRectifier_Type()
)
es1dc1DataRectifiersNumberOfRemoteOffRectifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es1dc1DataRectifiersNumberOfRemoteOffRectifier.setStatus("current")
_Es1dc1DataRectifiersNumberOfOverTempRectifier_Type = Integer32
_Es1dc1DataRectifiersNumberOfOverTempRectifier_Object = MibScalar
es1dc1DataRectifiersNumberOfOverTempRectifier = _Es1dc1DataRectifiersNumberOfOverTempRectifier_Object(
    (1, 3, 6, 1, 4, 1, 26854, 3, 2, 1, 20, 1, 20, 1, 13, 3, 38),
    _Es1dc1DataRectifiersNumberOfOverTempRectifier_Type()
)
es1dc1DataRectifiersNumberOfOverTempRectifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es1dc1DataRectifiersNumberOfOverTempRectifier.setStatus("current")
_Es1dc1DataLoadLoadPower_Type = Integer32
_Es1dc1DataLoadLoadPower_Object = MibScalar
es1dc1DataLoadLoadPower = _Es1dc1DataLoadLoadPower_Object(
    (1, 3, 6, 1, 4, 1, 26854, 3, 2, 1, 20, 1, 20, 1, 13, 3, 51),
    _Es1dc1DataLoadLoadPower_Type()
)
es1dc1DataLoadLoadPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es1dc1DataLoadLoadPower.setStatus("current")
_Es1dc1DataLoadLoadCurrent_Type = Integer32
_Es1dc1DataLoadLoadCurrent_Object = MibScalar
es1dc1DataLoadLoadCurrent = _Es1dc1DataLoadLoadCurrent_Object(
    (1, 3, 6, 1, 4, 1, 26854, 3, 2, 1, 20, 1, 20, 1, 13, 3, 52),
    _Es1dc1DataLoadLoadCurrent_Type()
)
es1dc1DataLoadLoadCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es1dc1DataLoadLoadCurrent.setStatus("current")
_Es1dc1DataBatBatInputCurrent_Type = Integer32
_Es1dc1DataBatBatInputCurrent_Object = MibScalar
es1dc1DataBatBatInputCurrent = _Es1dc1DataBatBatInputCurrent_Object(
    (1, 3, 6, 1, 4, 1, 26854, 3, 2, 1, 20, 1, 20, 1, 13, 3, 61),
    _Es1dc1DataBatBatInputCurrent_Type()
)
es1dc1DataBatBatInputCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es1dc1DataBatBatInputCurrent.setStatus("current")
_Es1dc1DataBatBatInputPower_Type = Integer32
_Es1dc1DataBatBatInputPower_Object = MibScalar
es1dc1DataBatBatInputPower = _Es1dc1DataBatBatInputPower_Object(
    (1, 3, 6, 1, 4, 1, 26854, 3, 2, 1, 20, 1, 20, 1, 13, 3, 62),
    _Es1dc1DataBatBatInputPower_Type()
)
es1dc1DataBatBatInputPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es1dc1DataBatBatInputPower.setStatus("current")
_Es1dc1DataBatBatTemp_Type = Integer32
_Es1dc1DataBatBatTemp_Object = MibScalar
es1dc1DataBatBatTemp = _Es1dc1DataBatBatTemp_Object(
    (1, 3, 6, 1, 4, 1, 26854, 3, 2, 1, 20, 1, 20, 1, 13, 3, 71),
    _Es1dc1DataBatBatTemp_Type()
)
es1dc1DataBatBatTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es1dc1DataBatBatTemp.setStatus("current")
_Es1dc1DataBatBatTestState_Type = Integer32
_Es1dc1DataBatBatTestState_Object = MibScalar
es1dc1DataBatBatTestState = _Es1dc1DataBatBatTestState_Object(
    (1, 3, 6, 1, 4, 1, 26854, 3, 2, 1, 20, 1, 20, 1, 13, 3, 72),
    _Es1dc1DataBatBatTestState_Type()
)
es1dc1DataBatBatTestState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es1dc1DataBatBatTestState.setStatus("current")
_Es1dc1DataBatLastBatTestDischargedCapacityRatio_Type = Integer32
_Es1dc1DataBatLastBatTestDischargedCapacityRatio_Object = MibScalar
es1dc1DataBatLastBatTestDischargedCapacityRatio = _Es1dc1DataBatLastBatTestDischargedCapacityRatio_Object(
    (1, 3, 6, 1, 4, 1, 26854, 3, 2, 1, 20, 1, 20, 1, 13, 3, 73),
    _Es1dc1DataBatLastBatTestDischargedCapacityRatio_Type()
)
es1dc1DataBatLastBatTestDischargedCapacityRatio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es1dc1DataBatLastBatTestDischargedCapacityRatio.setStatus("current")
_Es1dc1DataBatLastBatTestDischargedCapacity_Type = Integer32
_Es1dc1DataBatLastBatTestDischargedCapacity_Object = MibScalar
es1dc1DataBatLastBatTestDischargedCapacity = _Es1dc1DataBatLastBatTestDischargedCapacity_Object(
    (1, 3, 6, 1, 4, 1, 26854, 3, 2, 1, 20, 1, 20, 1, 13, 3, 74),
    _Es1dc1DataBatLastBatTestDischargedCapacity_Type()
)
es1dc1DataBatLastBatTestDischargedCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es1dc1DataBatLastBatTestDischargedCapacity.setStatus("current")
_Es1dc1DataBatLastBatTestFinalVoltage_Type = Integer32
_Es1dc1DataBatLastBatTestFinalVoltage_Object = MibScalar
es1dc1DataBatLastBatTestFinalVoltage = _Es1dc1DataBatLastBatTestFinalVoltage_Object(
    (1, 3, 6, 1, 4, 1, 26854, 3, 2, 1, 20, 1, 20, 1, 13, 3, 75),
    _Es1dc1DataBatLastBatTestFinalVoltage_Type()
)
es1dc1DataBatLastBatTestFinalVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es1dc1DataBatLastBatTestFinalVoltage.setStatus("current")
_Es1dc1DataBatBatTestDuration_Type = Integer32
_Es1dc1DataBatBatTestDuration_Object = MibScalar
es1dc1DataBatBatTestDuration = _Es1dc1DataBatBatTestDuration_Object(
    (1, 3, 6, 1, 4, 1, 26854, 3, 2, 1, 20, 1, 20, 1, 13, 3, 76),
    _Es1dc1DataBatBatTestDuration_Type()
)
es1dc1DataBatBatTestDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es1dc1DataBatBatTestDuration.setStatus("current")
_Es1dc1DataBatPreviousBatTestDischargedCapacityRatio_Type = Integer32
_Es1dc1DataBatPreviousBatTestDischargedCapacityRatio_Object = MibScalar
es1dc1DataBatPreviousBatTestDischargedCapacityRatio = _Es1dc1DataBatPreviousBatTestDischargedCapacityRatio_Object(
    (1, 3, 6, 1, 4, 1, 26854, 3, 2, 1, 20, 1, 20, 1, 13, 3, 77),
    _Es1dc1DataBatPreviousBatTestDischargedCapacityRatio_Type()
)
es1dc1DataBatPreviousBatTestDischargedCapacityRatio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es1dc1DataBatPreviousBatTestDischargedCapacityRatio.setStatus("current")
_Es1dc1DataBatPreviousBatTestDischargedCapacity_Type = Integer32
_Es1dc1DataBatPreviousBatTestDischargedCapacity_Object = MibScalar
es1dc1DataBatPreviousBatTestDischargedCapacity = _Es1dc1DataBatPreviousBatTestDischargedCapacity_Object(
    (1, 3, 6, 1, 4, 1, 26854, 3, 2, 1, 20, 1, 20, 1, 13, 3, 78),
    _Es1dc1DataBatPreviousBatTestDischargedCapacity_Type()
)
es1dc1DataBatPreviousBatTestDischargedCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es1dc1DataBatPreviousBatTestDischargedCapacity.setStatus("current")
_Es1dc1DataBatPreviousBatTestFinalVoltage_Type = Integer32
_Es1dc1DataBatPreviousBatTestFinalVoltage_Object = MibScalar
es1dc1DataBatPreviousBatTestFinalVoltage = _Es1dc1DataBatPreviousBatTestFinalVoltage_Object(
    (1, 3, 6, 1, 4, 1, 26854, 3, 2, 1, 20, 1, 20, 1, 13, 3, 79),
    _Es1dc1DataBatPreviousBatTestFinalVoltage_Type()
)
es1dc1DataBatPreviousBatTestFinalVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es1dc1DataBatPreviousBatTestFinalVoltage.setStatus("current")
_Es1dc1DataBatPreviousBatTestDuration_Type = Integer32
_Es1dc1DataBatPreviousBatTestDuration_Object = MibScalar
es1dc1DataBatPreviousBatTestDuration = _Es1dc1DataBatPreviousBatTestDuration_Object(
    (1, 3, 6, 1, 4, 1, 26854, 3, 2, 1, 20, 1, 20, 1, 13, 3, 80),
    _Es1dc1DataBatPreviousBatTestDuration_Type()
)
es1dc1DataBatPreviousBatTestDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es1dc1DataBatPreviousBatTestDuration.setStatus("current")
_Es1dc1DataBatPreviousBatTestState_Type = Integer32
_Es1dc1DataBatPreviousBatTestState_Object = MibScalar
es1dc1DataBatPreviousBatTestState = _Es1dc1DataBatPreviousBatTestState_Object(
    (1, 3, 6, 1, 4, 1, 26854, 3, 2, 1, 20, 1, 20, 1, 13, 3, 81),
    _Es1dc1DataBatPreviousBatTestState_Type()
)
es1dc1DataBatPreviousBatTestState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es1dc1DataBatPreviousBatTestState.setStatus("current")
_Es1dc1DataBatMinutesSinceLastTestBat_Type = Integer32
_Es1dc1DataBatMinutesSinceLastTestBat_Object = MibScalar
es1dc1DataBatMinutesSinceLastTestBat = _Es1dc1DataBatMinutesSinceLastTestBat_Object(
    (1, 3, 6, 1, 4, 1, 26854, 3, 2, 1, 20, 1, 20, 1, 13, 3, 82),
    _Es1dc1DataBatMinutesSinceLastTestBat_Type()
)
es1dc1DataBatMinutesSinceLastTestBat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es1dc1DataBatMinutesSinceLastTestBat.setStatus("current")
_Es1dc1DataBatNextScheduledBatTest_Type = Integer32
_Es1dc1DataBatNextScheduledBatTest_Object = MibScalar
es1dc1DataBatNextScheduledBatTest = _Es1dc1DataBatNextScheduledBatTest_Object(
    (1, 3, 6, 1, 4, 1, 26854, 3, 2, 1, 20, 1, 20, 1, 13, 3, 84),
    _Es1dc1DataBatNextScheduledBatTest_Type()
)
es1dc1DataBatNextScheduledBatTest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es1dc1DataBatNextScheduledBatTest.setStatus("current")
_Es1dc1DataBatBatChargeCapacity_Type = Integer32
_Es1dc1DataBatBatChargeCapacity_Object = MibScalar
es1dc1DataBatBatChargeCapacity = _Es1dc1DataBatBatChargeCapacity_Object(
    (1, 3, 6, 1, 4, 1, 26854, 3, 2, 1, 20, 1, 20, 1, 13, 3, 91),
    _Es1dc1DataBatBatChargeCapacity_Type()
)
es1dc1DataBatBatChargeCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es1dc1DataBatBatChargeCapacity.setStatus("current")
_Es1dc1DataBatCalculatedAutonomy_Type = Integer32
_Es1dc1DataBatCalculatedAutonomy_Object = MibScalar
es1dc1DataBatCalculatedAutonomy = _Es1dc1DataBatCalculatedAutonomy_Object(
    (1, 3, 6, 1, 4, 1, 26854, 3, 2, 1, 20, 1, 20, 1, 13, 3, 92),
    _Es1dc1DataBatCalculatedAutonomy_Type()
)
es1dc1DataBatCalculatedAutonomy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es1dc1DataBatCalculatedAutonomy.setStatus("current")
_Es1dc1DataBatBatCurrentIntegration_Type = Integer32
_Es1dc1DataBatBatCurrentIntegration_Object = MibScalar
es1dc1DataBatBatCurrentIntegration = _Es1dc1DataBatBatCurrentIntegration_Object(
    (1, 3, 6, 1, 4, 1, 26854, 3, 2, 1, 20, 1, 20, 1, 13, 3, 94),
    _Es1dc1DataBatBatCurrentIntegration_Type()
)
es1dc1DataBatBatCurrentIntegration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es1dc1DataBatBatCurrentIntegration.setStatus("current")
_Es1dc1DataLVDLVDState_Type = Integer32
_Es1dc1DataLVDLVDState_Object = MibScalar
es1dc1DataLVDLVDState = _Es1dc1DataLVDLVDState_Object(
    (1, 3, 6, 1, 4, 1, 26854, 3, 2, 1, 20, 1, 20, 1, 13, 3, 101),
    _Es1dc1DataLVDLVDState_Type()
)
es1dc1DataLVDLVDState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es1dc1DataLVDLVDState.setStatus("current")
_Es1dc1DataRelsRel1State_Type = Integer32
_Es1dc1DataRelsRel1State_Object = MibScalar
es1dc1DataRelsRel1State = _Es1dc1DataRelsRel1State_Object(
    (1, 3, 6, 1, 4, 1, 26854, 3, 2, 1, 20, 1, 20, 1, 13, 3, 111),
    _Es1dc1DataRelsRel1State_Type()
)
es1dc1DataRelsRel1State.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es1dc1DataRelsRel1State.setStatus("current")
_Es1dc1DataRelsRel2State_Type = Integer32
_Es1dc1DataRelsRel2State_Object = MibScalar
es1dc1DataRelsRel2State = _Es1dc1DataRelsRel2State_Object(
    (1, 3, 6, 1, 4, 1, 26854, 3, 2, 1, 20, 1, 20, 1, 13, 3, 112),
    _Es1dc1DataRelsRel2State_Type()
)
es1dc1DataRelsRel2State.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es1dc1DataRelsRel2State.setStatus("current")
_Es1dc1DataRelsRel3State_Type = Integer32
_Es1dc1DataRelsRel3State_Object = MibScalar
es1dc1DataRelsRel3State = _Es1dc1DataRelsRel3State_Object(
    (1, 3, 6, 1, 4, 1, 26854, 3, 2, 1, 20, 1, 20, 1, 13, 3, 113),
    _Es1dc1DataRelsRel3State_Type()
)
es1dc1DataRelsRel3State.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es1dc1DataRelsRel3State.setStatus("current")
_Es1dc1DataRelsRel4State_Type = Integer32
_Es1dc1DataRelsRel4State_Object = MibScalar
es1dc1DataRelsRel4State = _Es1dc1DataRelsRel4State_Object(
    (1, 3, 6, 1, 4, 1, 26854, 3, 2, 1, 20, 1, 20, 1, 13, 3, 114),
    _Es1dc1DataRelsRel4State_Type()
)
es1dc1DataRelsRel4State.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es1dc1DataRelsRel4State.setStatus("current")
_Es1dc1DataSmartEnergyEfficiencyOptimizedNumberOfRectifier_Type = Integer32
_Es1dc1DataSmartEnergyEfficiencyOptimizedNumberOfRectifier_Object = MibScalar
es1dc1DataSmartEnergyEfficiencyOptimizedNumberOfRectifier = _Es1dc1DataSmartEnergyEfficiencyOptimizedNumberOfRectifier_Object(
    (1, 3, 6, 1, 4, 1, 26854, 3, 2, 1, 20, 1, 20, 1, 13, 3, 121),
    _Es1dc1DataSmartEnergyEfficiencyOptimizedNumberOfRectifier_Type()
)
es1dc1DataSmartEnergyEfficiencyOptimizedNumberOfRectifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es1dc1DataSmartEnergyEfficiencyOptimizedNumberOfRectifier.setStatus("current")
_Es1dc1DataSmartEnergySystemLossWithoutOptimisation_Type = Integer32
_Es1dc1DataSmartEnergySystemLossWithoutOptimisation_Object = MibScalar
es1dc1DataSmartEnergySystemLossWithoutOptimisation = _Es1dc1DataSmartEnergySystemLossWithoutOptimisation_Object(
    (1, 3, 6, 1, 4, 1, 26854, 3, 2, 1, 20, 1, 20, 1, 13, 3, 122),
    _Es1dc1DataSmartEnergySystemLossWithoutOptimisation_Type()
)
es1dc1DataSmartEnergySystemLossWithoutOptimisation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es1dc1DataSmartEnergySystemLossWithoutOptimisation.setStatus("current")
_Es1dc1DataSmartEnergySystemLossWithOptimisation_Type = Integer32
_Es1dc1DataSmartEnergySystemLossWithOptimisation_Object = MibScalar
es1dc1DataSmartEnergySystemLossWithOptimisation = _Es1dc1DataSmartEnergySystemLossWithOptimisation_Object(
    (1, 3, 6, 1, 4, 1, 26854, 3, 2, 1, 20, 1, 20, 1, 13, 3, 123),
    _Es1dc1DataSmartEnergySystemLossWithOptimisation_Type()
)
es1dc1DataSmartEnergySystemLossWithOptimisation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es1dc1DataSmartEnergySystemLossWithOptimisation.setStatus("current")
_Es1dc1DataSmartEnergyRectifierModelUsedForCalculation_Type = Integer32
_Es1dc1DataSmartEnergyRectifierModelUsedForCalculation_Object = MibScalar
es1dc1DataSmartEnergyRectifierModelUsedForCalculation = _Es1dc1DataSmartEnergyRectifierModelUsedForCalculation_Object(
    (1, 3, 6, 1, 4, 1, 26854, 3, 2, 1, 20, 1, 20, 1, 13, 3, 124),
    _Es1dc1DataSmartEnergyRectifierModelUsedForCalculation_Type()
)
es1dc1DataSmartEnergyRectifierModelUsedForCalculation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es1dc1DataSmartEnergyRectifierModelUsedForCalculation.setStatus("current")
_Es1dc1DataSmartEnergySmartEnergySavings_Type = Integer32
_Es1dc1DataSmartEnergySmartEnergySavings_Object = MibScalar
es1dc1DataSmartEnergySmartEnergySavings = _Es1dc1DataSmartEnergySmartEnergySavings_Object(
    (1, 3, 6, 1, 4, 1, 26854, 3, 2, 1, 20, 1, 20, 1, 13, 3, 125),
    _Es1dc1DataSmartEnergySmartEnergySavings_Type()
)
es1dc1DataSmartEnergySmartEnergySavings.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es1dc1DataSmartEnergySmartEnergySavings.setStatus("current")
_Es1dc1DataSensorsAmbientTemp_Type = Integer32
_Es1dc1DataSensorsAmbientTemp_Object = MibScalar
es1dc1DataSensorsAmbientTemp = _Es1dc1DataSensorsAmbientTemp_Object(
    (1, 3, 6, 1, 4, 1, 26854, 3, 2, 1, 20, 1, 20, 1, 13, 3, 151),
    _Es1dc1DataSensorsAmbientTemp_Type()
)
es1dc1DataSensorsAmbientTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es1dc1DataSensorsAmbientTemp.setStatus("current")
_Es1dc1DataSensorsPulseCounter4_Type = Integer32
_Es1dc1DataSensorsPulseCounter4_Object = MibScalar
es1dc1DataSensorsPulseCounter4 = _Es1dc1DataSensorsPulseCounter4_Object(
    (1, 3, 6, 1, 4, 1, 26854, 3, 2, 1, 20, 1, 20, 1, 13, 3, 204),
    _Es1dc1DataSensorsPulseCounter4_Type()
)
es1dc1DataSensorsPulseCounter4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es1dc1DataSensorsPulseCounter4.setStatus("current")
_Es1dc1Config_ObjectIdentity = ObjectIdentity
es1dc1Config = _Es1dc1Config_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 26854, 3, 2, 1, 20, 1, 20, 1, 15)
)
_Es1dc1ConfigNumber_Type = Integer32
_Es1dc1ConfigNumber_Object = MibScalar
es1dc1ConfigNumber = _Es1dc1ConfigNumber_Object(
    (1, 3, 6, 1, 4, 1, 26854, 3, 2, 1, 20, 1, 20, 1, 15, 1),
    _Es1dc1ConfigNumber_Type()
)
es1dc1ConfigNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es1dc1ConfigNumber.setStatus("current")
_Es1dc1ConfigTable_Object = MibTable
es1dc1ConfigTable = _Es1dc1ConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 26854, 3, 2, 1, 20, 1, 20, 1, 15, 2)
)
if mibBuilder.loadTexts:
    es1dc1ConfigTable.setStatus("current")
_Es1dc1ConfigEntry_Object = MibTableRow
es1dc1ConfigEntry = _Es1dc1ConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 26854, 3, 2, 1, 20, 1, 20, 1, 15, 2, 1)
)
es1dc1ConfigEntry.setIndexNames(
    (0, "SITE-MONITORING-MIB", "es1dc1ConfigIndex"),
)
if mibBuilder.loadTexts:
    es1dc1ConfigEntry.setStatus("current")
_Es1dc1ConfigIndex_Type = Unsigned32
_Es1dc1ConfigIndex_Object = MibTableColumn
es1dc1ConfigIndex = _Es1dc1ConfigIndex_Object(
    (1, 3, 6, 1, 4, 1, 26854, 3, 2, 1, 20, 1, 20, 1, 15, 2, 1, 1),
    _Es1dc1ConfigIndex_Type()
)
es1dc1ConfigIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    es1dc1ConfigIndex.setStatus("current")
_Es1dc1ConfigName_Type = DisplayString
_Es1dc1ConfigName_Object = MibTableColumn
es1dc1ConfigName = _Es1dc1ConfigName_Object(
    (1, 3, 6, 1, 4, 1, 26854, 3, 2, 1, 20, 1, 20, 1, 15, 2, 1, 2),
    _Es1dc1ConfigName_Type()
)
es1dc1ConfigName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es1dc1ConfigName.setStatus("current")
_Es1dc1ConfigValue_Type = DisplayString
_Es1dc1ConfigValue_Object = MibTableColumn
es1dc1ConfigValue = _Es1dc1ConfigValue_Object(
    (1, 3, 6, 1, 4, 1, 26854, 3, 2, 1, 20, 1, 20, 1, 15, 2, 1, 3),
    _Es1dc1ConfigValue_Type()
)
es1dc1ConfigValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es1dc1ConfigValue.setStatus("current")
_Es1dc1ConfigEntryStatus_Type = RowStatus
_Es1dc1ConfigEntryStatus_Object = MibTableColumn
es1dc1ConfigEntryStatus = _Es1dc1ConfigEntryStatus_Object(
    (1, 3, 6, 1, 4, 1, 26854, 3, 2, 1, 20, 1, 20, 1, 15, 2, 1, 4),
    _Es1dc1ConfigEntryStatus_Type()
)
es1dc1ConfigEntryStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    es1dc1ConfigEntryStatus.setStatus("current")
_Es1dc1ConfigList_ObjectIdentity = ObjectIdentity
es1dc1ConfigList = _Es1dc1ConfigList_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 26854, 3, 2, 1, 20, 1, 20, 1, 15, 3)
)
_Es1dc1CfgDCBusDCBusFloatVoltageat25degC_Type = DisplayString
_Es1dc1CfgDCBusDCBusFloatVoltageat25degC_Object = MibScalar
es1dc1CfgDCBusDCBusFloatVoltageat25degC = _Es1dc1CfgDCBusDCBusFloatVoltageat25degC_Object(
    (1, 3, 6, 1, 4, 1, 26854, 3, 2, 1, 20, 1, 20, 1, 15, 3, 1),
    _Es1dc1CfgDCBusDCBusFloatVoltageat25degC_Type()
)
es1dc1CfgDCBusDCBusFloatVoltageat25degC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es1dc1CfgDCBusDCBusFloatVoltageat25degC.setStatus("current")
_Es1dc1CfgDCBusDCBusVoltageExtraLow_Type = DisplayString
_Es1dc1CfgDCBusDCBusVoltageExtraLow_Object = MibScalar
es1dc1CfgDCBusDCBusVoltageExtraLow = _Es1dc1CfgDCBusDCBusVoltageExtraLow_Object(
    (1, 3, 6, 1, 4, 1, 26854, 3, 2, 1, 20, 1, 20, 1, 15, 3, 2),
    _Es1dc1CfgDCBusDCBusVoltageExtraLow_Type()
)
es1dc1CfgDCBusDCBusVoltageExtraLow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es1dc1CfgDCBusDCBusVoltageExtraLow.setStatus("current")
_Es1dc1CfgDCBusDCBusVoltageExtraLowHysteresis_Type = DisplayString
_Es1dc1CfgDCBusDCBusVoltageExtraLowHysteresis_Object = MibScalar
es1dc1CfgDCBusDCBusVoltageExtraLowHysteresis = _Es1dc1CfgDCBusDCBusVoltageExtraLowHysteresis_Object(
    (1, 3, 6, 1, 4, 1, 26854, 3, 2, 1, 20, 1, 20, 1, 15, 3, 3),
    _Es1dc1CfgDCBusDCBusVoltageExtraLowHysteresis_Type()
)
es1dc1CfgDCBusDCBusVoltageExtraLowHysteresis.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es1dc1CfgDCBusDCBusVoltageExtraLowHysteresis.setStatus("current")
_Es1dc1CfgDCBusDCBusVoltageLow_Type = DisplayString
_Es1dc1CfgDCBusDCBusVoltageLow_Object = MibScalar
es1dc1CfgDCBusDCBusVoltageLow = _Es1dc1CfgDCBusDCBusVoltageLow_Object(
    (1, 3, 6, 1, 4, 1, 26854, 3, 2, 1, 20, 1, 20, 1, 15, 3, 4),
    _Es1dc1CfgDCBusDCBusVoltageLow_Type()
)
es1dc1CfgDCBusDCBusVoltageLow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es1dc1CfgDCBusDCBusVoltageLow.setStatus("current")
_Es1dc1CfgDCBusDCBusVoltageLowHysteresis_Type = DisplayString
_Es1dc1CfgDCBusDCBusVoltageLowHysteresis_Object = MibScalar
es1dc1CfgDCBusDCBusVoltageLowHysteresis = _Es1dc1CfgDCBusDCBusVoltageLowHysteresis_Object(
    (1, 3, 6, 1, 4, 1, 26854, 3, 2, 1, 20, 1, 20, 1, 15, 3, 5),
    _Es1dc1CfgDCBusDCBusVoltageLowHysteresis_Type()
)
es1dc1CfgDCBusDCBusVoltageLowHysteresis.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es1dc1CfgDCBusDCBusVoltageLowHysteresis.setStatus("current")
_Es1dc1CfgDCBusDCBusVoltageHigh_Type = DisplayString
_Es1dc1CfgDCBusDCBusVoltageHigh_Object = MibScalar
es1dc1CfgDCBusDCBusVoltageHigh = _Es1dc1CfgDCBusDCBusVoltageHigh_Object(
    (1, 3, 6, 1, 4, 1, 26854, 3, 2, 1, 20, 1, 20, 1, 15, 3, 6),
    _Es1dc1CfgDCBusDCBusVoltageHigh_Type()
)
es1dc1CfgDCBusDCBusVoltageHigh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es1dc1CfgDCBusDCBusVoltageHigh.setStatus("current")
_Es1dc1CfgDCBusDCBusVoltageHighHysteresis_Type = DisplayString
_Es1dc1CfgDCBusDCBusVoltageHighHysteresis_Object = MibScalar
es1dc1CfgDCBusDCBusVoltageHighHysteresis = _Es1dc1CfgDCBusDCBusVoltageHighHysteresis_Object(
    (1, 3, 6, 1, 4, 1, 26854, 3, 2, 1, 20, 1, 20, 1, 15, 3, 7),
    _Es1dc1CfgDCBusDCBusVoltageHighHysteresis_Type()
)
es1dc1CfgDCBusDCBusVoltageHighHysteresis.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es1dc1CfgDCBusDCBusVoltageHighHysteresis.setStatus("current")
_Es1dc1CfgDCBusDCBusVoltageExtraHigh_Type = DisplayString
_Es1dc1CfgDCBusDCBusVoltageExtraHigh_Object = MibScalar
es1dc1CfgDCBusDCBusVoltageExtraHigh = _Es1dc1CfgDCBusDCBusVoltageExtraHigh_Object(
    (1, 3, 6, 1, 4, 1, 26854, 3, 2, 1, 20, 1, 20, 1, 15, 3, 8),
    _Es1dc1CfgDCBusDCBusVoltageExtraHigh_Type()
)
es1dc1CfgDCBusDCBusVoltageExtraHigh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es1dc1CfgDCBusDCBusVoltageExtraHigh.setStatus("current")
_Es1dc1CfgDCBusDCBusVoltageExtraHighHysteresis_Type = DisplayString
_Es1dc1CfgDCBusDCBusVoltageExtraHighHysteresis_Object = MibScalar
es1dc1CfgDCBusDCBusVoltageExtraHighHysteresis = _Es1dc1CfgDCBusDCBusVoltageExtraHighHysteresis_Object(
    (1, 3, 6, 1, 4, 1, 26854, 3, 2, 1, 20, 1, 20, 1, 15, 3, 9),
    _Es1dc1CfgDCBusDCBusVoltageExtraHighHysteresis_Type()
)
es1dc1CfgDCBusDCBusVoltageExtraHighHysteresis.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es1dc1CfgDCBusDCBusVoltageExtraHighHysteresis.setStatus("current")
_Es1dc1CfgLVDLVDDisconnectVoltage_Type = DisplayString
_Es1dc1CfgLVDLVDDisconnectVoltage_Object = MibScalar
es1dc1CfgLVDLVDDisconnectVoltage = _Es1dc1CfgLVDLVDDisconnectVoltage_Object(
    (1, 3, 6, 1, 4, 1, 26854, 3, 2, 1, 20, 1, 20, 1, 15, 3, 10),
    _Es1dc1CfgLVDLVDDisconnectVoltage_Type()
)
es1dc1CfgLVDLVDDisconnectVoltage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es1dc1CfgLVDLVDDisconnectVoltage.setStatus("current")
_Es1dc1CfgLVDLVDDisconnectDelay_Type = DisplayString
_Es1dc1CfgLVDLVDDisconnectDelay_Object = MibScalar
es1dc1CfgLVDLVDDisconnectDelay = _Es1dc1CfgLVDLVDDisconnectDelay_Object(
    (1, 3, 6, 1, 4, 1, 26854, 3, 2, 1, 20, 1, 20, 1, 15, 3, 11),
    _Es1dc1CfgLVDLVDDisconnectDelay_Type()
)
es1dc1CfgLVDLVDDisconnectDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es1dc1CfgLVDLVDDisconnectDelay.setStatus("current")
_Es1dc1CfgBatTempCompensationSlope_Type = DisplayString
_Es1dc1CfgBatTempCompensationSlope_Object = MibScalar
es1dc1CfgBatTempCompensationSlope = _Es1dc1CfgBatTempCompensationSlope_Object(
    (1, 3, 6, 1, 4, 1, 26854, 3, 2, 1, 20, 1, 20, 1, 15, 3, 21),
    _Es1dc1CfgBatTempCompensationSlope_Type()
)
es1dc1CfgBatTempCompensationSlope.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es1dc1CfgBatTempCompensationSlope.setStatus("current")
_Es1dc1CfgBatMaxPosTempCompensation_Type = DisplayString
_Es1dc1CfgBatMaxPosTempCompensation_Object = MibScalar
es1dc1CfgBatMaxPosTempCompensation = _Es1dc1CfgBatMaxPosTempCompensation_Object(
    (1, 3, 6, 1, 4, 1, 26854, 3, 2, 1, 20, 1, 20, 1, 15, 3, 22),
    _Es1dc1CfgBatMaxPosTempCompensation_Type()
)
es1dc1CfgBatMaxPosTempCompensation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es1dc1CfgBatMaxPosTempCompensation.setStatus("current")
_Es1dc1CfgBatMaxNegTempCompensation_Type = DisplayString
_Es1dc1CfgBatMaxNegTempCompensation_Object = MibScalar
es1dc1CfgBatMaxNegTempCompensation = _Es1dc1CfgBatMaxNegTempCompensation_Object(
    (1, 3, 6, 1, 4, 1, 26854, 3, 2, 1, 20, 1, 20, 1, 15, 3, 23),
    _Es1dc1CfgBatMaxNegTempCompensation_Type()
)
es1dc1CfgBatMaxNegTempCompensation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es1dc1CfgBatMaxNegTempCompensation.setStatus("current")
_Es1dc1CfgRectifiersMinimalNumberOfPresentRectifiers_Type = DisplayString
_Es1dc1CfgRectifiersMinimalNumberOfPresentRectifiers_Object = MibScalar
es1dc1CfgRectifiersMinimalNumberOfPresentRectifiers = _Es1dc1CfgRectifiersMinimalNumberOfPresentRectifiers_Object(
    (1, 3, 6, 1, 4, 1, 26854, 3, 2, 1, 20, 1, 20, 1, 15, 3, 25),
    _Es1dc1CfgRectifiersMinimalNumberOfPresentRectifiers_Type()
)
es1dc1CfgRectifiersMinimalNumberOfPresentRectifiers.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es1dc1CfgRectifiersMinimalNumberOfPresentRectifiers.setStatus("current")
_Es1dc1CfgRectifiersRectifierModel_Type = DisplayString
_Es1dc1CfgRectifiersRectifierModel_Object = MibScalar
es1dc1CfgRectifiersRectifierModel = _Es1dc1CfgRectifiersRectifierModel_Object(
    (1, 3, 6, 1, 4, 1, 26854, 3, 2, 1, 20, 1, 20, 1, 15, 3, 26),
    _Es1dc1CfgRectifiersRectifierModel_Type()
)
es1dc1CfgRectifiersRectifierModel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es1dc1CfgRectifiersRectifierModel.setStatus("current")
_Es1dc1CfgRectifiersForcedRemoteOffRectifers_Type = DisplayString
_Es1dc1CfgRectifiersForcedRemoteOffRectifers_Object = MibScalar
es1dc1CfgRectifiersForcedRemoteOffRectifers = _Es1dc1CfgRectifiersForcedRemoteOffRectifers_Object(
    (1, 3, 6, 1, 4, 1, 26854, 3, 2, 1, 20, 1, 20, 1, 15, 3, 27),
    _Es1dc1CfgRectifiersForcedRemoteOffRectifers_Type()
)
es1dc1CfgRectifiersForcedRemoteOffRectifers.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es1dc1CfgRectifiersForcedRemoteOffRectifers.setStatus("current")
_Es1dc1CfgBatBatChargeCurrentLimit_Type = DisplayString
_Es1dc1CfgBatBatChargeCurrentLimit_Object = MibScalar
es1dc1CfgBatBatChargeCurrentLimit = _Es1dc1CfgBatBatChargeCurrentLimit_Object(
    (1, 3, 6, 1, 4, 1, 26854, 3, 2, 1, 20, 1, 20, 1, 15, 3, 31),
    _Es1dc1CfgBatBatChargeCurrentLimit_Type()
)
es1dc1CfgBatBatChargeCurrentLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es1dc1CfgBatBatChargeCurrentLimit.setStatus("current")
_Es1dc1CfgBatBatStringCapacity_Type = DisplayString
_Es1dc1CfgBatBatStringCapacity_Object = MibScalar
es1dc1CfgBatBatStringCapacity = _Es1dc1CfgBatBatStringCapacity_Object(
    (1, 3, 6, 1, 4, 1, 26854, 3, 2, 1, 20, 1, 20, 1, 15, 3, 32),
    _Es1dc1CfgBatBatStringCapacity_Type()
)
es1dc1CfgBatBatStringCapacity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es1dc1CfgBatBatStringCapacity.setStatus("current")
_Es1dc1CfgBatBatTempLow_Type = DisplayString
_Es1dc1CfgBatBatTempLow_Object = MibScalar
es1dc1CfgBatBatTempLow = _Es1dc1CfgBatBatTempLow_Object(
    (1, 3, 6, 1, 4, 1, 26854, 3, 2, 1, 20, 1, 20, 1, 15, 3, 33),
    _Es1dc1CfgBatBatTempLow_Type()
)
es1dc1CfgBatBatTempLow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es1dc1CfgBatBatTempLow.setStatus("current")
_Es1dc1CfgBatBatTempHigh_Type = DisplayString
_Es1dc1CfgBatBatTempHigh_Object = MibScalar
es1dc1CfgBatBatTempHigh = _Es1dc1CfgBatBatTempHigh_Object(
    (1, 3, 6, 1, 4, 1, 26854, 3, 2, 1, 20, 1, 20, 1, 15, 3, 34),
    _Es1dc1CfgBatBatTempHigh_Type()
)
es1dc1CfgBatBatTempHigh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es1dc1CfgBatBatTempHigh.setStatus("current")
_Es1dc1CfgBatBatTempHysteresis_Type = DisplayString
_Es1dc1CfgBatBatTempHysteresis_Object = MibScalar
es1dc1CfgBatBatTempHysteresis = _Es1dc1CfgBatBatTempHysteresis_Object(
    (1, 3, 6, 1, 4, 1, 26854, 3, 2, 1, 20, 1, 20, 1, 15, 3, 35),
    _Es1dc1CfgBatBatTempHysteresis_Type()
)
es1dc1CfgBatBatTempHysteresis.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es1dc1CfgBatBatTempHysteresis.setStatus("current")
_Es1dc1CfgBatMinimalCurrentForDischargingAlarm_Type = DisplayString
_Es1dc1CfgBatMinimalCurrentForDischargingAlarm_Object = MibScalar
es1dc1CfgBatMinimalCurrentForDischargingAlarm = _Es1dc1CfgBatMinimalCurrentForDischargingAlarm_Object(
    (1, 3, 6, 1, 4, 1, 26854, 3, 2, 1, 20, 1, 20, 1, 15, 3, 36),
    _Es1dc1CfgBatMinimalCurrentForDischargingAlarm_Type()
)
es1dc1CfgBatMinimalCurrentForDischargingAlarm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es1dc1CfgBatMinimalCurrentForDischargingAlarm.setStatus("current")
_Es1dc1CfgBatCurrentHysteresisForDischargingAlarm_Type = DisplayString
_Es1dc1CfgBatCurrentHysteresisForDischargingAlarm_Object = MibScalar
es1dc1CfgBatCurrentHysteresisForDischargingAlarm = _Es1dc1CfgBatCurrentHysteresisForDischargingAlarm_Object(
    (1, 3, 6, 1, 4, 1, 26854, 3, 2, 1, 20, 1, 20, 1, 15, 3, 37),
    _Es1dc1CfgBatCurrentHysteresisForDischargingAlarm_Type()
)
es1dc1CfgBatCurrentHysteresisForDischargingAlarm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es1dc1CfgBatCurrentHysteresisForDischargingAlarm.setStatus("current")
_Es1dc1CfgBatPeukertNumber_Type = DisplayString
_Es1dc1CfgBatPeukertNumber_Object = MibScalar
es1dc1CfgBatPeukertNumber = _Es1dc1CfgBatPeukertNumber_Object(
    (1, 3, 6, 1, 4, 1, 26854, 3, 2, 1, 20, 1, 20, 1, 15, 3, 38),
    _Es1dc1CfgBatPeukertNumber_Type()
)
es1dc1CfgBatPeukertNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es1dc1CfgBatPeukertNumber.setStatus("current")
_Es1dc1CfgBatMaxDepthOfDischargeforAutonomyEstimation_Type = DisplayString
_Es1dc1CfgBatMaxDepthOfDischargeforAutonomyEstimation_Object = MibScalar
es1dc1CfgBatMaxDepthOfDischargeforAutonomyEstimation = _Es1dc1CfgBatMaxDepthOfDischargeforAutonomyEstimation_Object(
    (1, 3, 6, 1, 4, 1, 26854, 3, 2, 1, 20, 1, 20, 1, 15, 3, 39),
    _Es1dc1CfgBatMaxDepthOfDischargeforAutonomyEstimation_Type()
)
es1dc1CfgBatMaxDepthOfDischargeforAutonomyEstimation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es1dc1CfgBatMaxDepthOfDischargeforAutonomyEstimation.setStatus("current")
_Es1dc1CfgBatBoostAutomatic_Type = DisplayString
_Es1dc1CfgBatBoostAutomatic_Object = MibScalar
es1dc1CfgBatBoostAutomatic = _Es1dc1CfgBatBoostAutomatic_Object(
    (1, 3, 6, 1, 4, 1, 26854, 3, 2, 1, 20, 1, 20, 1, 15, 3, 51),
    _Es1dc1CfgBatBoostAutomatic_Type()
)
es1dc1CfgBatBoostAutomatic.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es1dc1CfgBatBoostAutomatic.setStatus("current")
_Es1dc1CfgBatBoostActivationLowVoltage_Type = DisplayString
_Es1dc1CfgBatBoostActivationLowVoltage_Object = MibScalar
es1dc1CfgBatBoostActivationLowVoltage = _Es1dc1CfgBatBoostActivationLowVoltage_Object(
    (1, 3, 6, 1, 4, 1, 26854, 3, 2, 1, 20, 1, 20, 1, 15, 3, 52),
    _Es1dc1CfgBatBoostActivationLowVoltage_Type()
)
es1dc1CfgBatBoostActivationLowVoltage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es1dc1CfgBatBoostActivationLowVoltage.setStatus("current")
_Es1dc1CfgBatBoostTerminationVoltage_Type = DisplayString
_Es1dc1CfgBatBoostTerminationVoltage_Object = MibScalar
es1dc1CfgBatBoostTerminationVoltage = _Es1dc1CfgBatBoostTerminationVoltage_Object(
    (1, 3, 6, 1, 4, 1, 26854, 3, 2, 1, 20, 1, 20, 1, 15, 3, 53),
    _Es1dc1CfgBatBoostTerminationVoltage_Type()
)
es1dc1CfgBatBoostTerminationVoltage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es1dc1CfgBatBoostTerminationVoltage.setStatus("current")
_Es1dc1CfgBatBoostTerminationCurrent_Type = DisplayString
_Es1dc1CfgBatBoostTerminationCurrent_Object = MibScalar
es1dc1CfgBatBoostTerminationCurrent = _Es1dc1CfgBatBoostTerminationCurrent_Object(
    (1, 3, 6, 1, 4, 1, 26854, 3, 2, 1, 20, 1, 20, 1, 15, 3, 54),
    _Es1dc1CfgBatBoostTerminationCurrent_Type()
)
es1dc1CfgBatBoostTerminationCurrent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es1dc1CfgBatBoostTerminationCurrent.setStatus("current")
_Es1dc1CfgBatBoostTerminationTime_Type = DisplayString
_Es1dc1CfgBatBoostTerminationTime_Object = MibScalar
es1dc1CfgBatBoostTerminationTime = _Es1dc1CfgBatBoostTerminationTime_Object(
    (1, 3, 6, 1, 4, 1, 26854, 3, 2, 1, 20, 1, 20, 1, 15, 3, 55),
    _Es1dc1CfgBatBoostTerminationTime_Type()
)
es1dc1CfgBatBoostTerminationTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es1dc1CfgBatBoostTerminationTime.setStatus("current")
_Es1dc1CfgBatBatTestType_Type = DisplayString
_Es1dc1CfgBatBatTestType_Object = MibScalar
es1dc1CfgBatBatTestType = _Es1dc1CfgBatBatTestType_Object(
    (1, 3, 6, 1, 4, 1, 26854, 3, 2, 1, 20, 1, 20, 1, 15, 3, 69),
    _Es1dc1CfgBatBatTestType_Type()
)
es1dc1CfgBatBatTestType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es1dc1CfgBatBatTestType.setStatus("current")
_Es1dc1CfgBatBatTestEndVoltage_Type = DisplayString
_Es1dc1CfgBatBatTestEndVoltage_Object = MibScalar
es1dc1CfgBatBatTestEndVoltage = _Es1dc1CfgBatBatTestEndVoltage_Object(
    (1, 3, 6, 1, 4, 1, 26854, 3, 2, 1, 20, 1, 20, 1, 15, 3, 70),
    _Es1dc1CfgBatBatTestEndVoltage_Type()
)
es1dc1CfgBatBatTestEndVoltage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es1dc1CfgBatBatTestEndVoltage.setStatus("current")
_Es1dc1CfgBatBatTestDischargeRatio_Type = DisplayString
_Es1dc1CfgBatBatTestDischargeRatio_Object = MibScalar
es1dc1CfgBatBatTestDischargeRatio = _Es1dc1CfgBatBatTestDischargeRatio_Object(
    (1, 3, 6, 1, 4, 1, 26854, 3, 2, 1, 20, 1, 20, 1, 15, 3, 71),
    _Es1dc1CfgBatBatTestDischargeRatio_Type()
)
es1dc1CfgBatBatTestDischargeRatio.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es1dc1CfgBatBatTestDischargeRatio.setStatus("current")
_Es1dc1CfgBatBatTestInterval_Type = DisplayString
_Es1dc1CfgBatBatTestInterval_Object = MibScalar
es1dc1CfgBatBatTestInterval = _Es1dc1CfgBatBatTestInterval_Object(
    (1, 3, 6, 1, 4, 1, 26854, 3, 2, 1, 20, 1, 20, 1, 15, 3, 72),
    _Es1dc1CfgBatBatTestInterval_Type()
)
es1dc1CfgBatBatTestInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es1dc1CfgBatBatTestInterval.setStatus("current")
_Es1dc1CfgBatBatTestDischargeCurrent_Type = DisplayString
_Es1dc1CfgBatBatTestDischargeCurrent_Object = MibScalar
es1dc1CfgBatBatTestDischargeCurrent = _Es1dc1CfgBatBatTestDischargeCurrent_Object(
    (1, 3, 6, 1, 4, 1, 26854, 3, 2, 1, 20, 1, 20, 1, 15, 3, 73),
    _Es1dc1CfgBatBatTestDischargeCurrent_Type()
)
es1dc1CfgBatBatTestDischargeCurrent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es1dc1CfgBatBatTestDischargeCurrent.setStatus("current")
_Es1dc1CfgBatBatTestMinimalDischargeCurrent_Type = DisplayString
_Es1dc1CfgBatBatTestMinimalDischargeCurrent_Object = MibScalar
es1dc1CfgBatBatTestMinimalDischargeCurrent = _Es1dc1CfgBatBatTestMinimalDischargeCurrent_Object(
    (1, 3, 6, 1, 4, 1, 26854, 3, 2, 1, 20, 1, 20, 1, 15, 3, 74),
    _Es1dc1CfgBatBatTestMinimalDischargeCurrent_Type()
)
es1dc1CfgBatBatTestMinimalDischargeCurrent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es1dc1CfgBatBatTestMinimalDischargeCurrent.setStatus("current")
_Es1dc1CfgBatBatTestDuration_Type = DisplayString
_Es1dc1CfgBatBatTestDuration_Object = MibScalar
es1dc1CfgBatBatTestDuration = _Es1dc1CfgBatBatTestDuration_Object(
    (1, 3, 6, 1, 4, 1, 26854, 3, 2, 1, 20, 1, 20, 1, 15, 3, 75),
    _Es1dc1CfgBatBatTestDuration_Type()
)
es1dc1CfgBatBatTestDuration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es1dc1CfgBatBatTestDuration.setStatus("current")
_Es1dc1CfgBatBatTestRequMinutesWithoutMainsFail_Type = DisplayString
_Es1dc1CfgBatBatTestRequMinutesWithoutMainsFail_Object = MibScalar
es1dc1CfgBatBatTestRequMinutesWithoutMainsFail = _Es1dc1CfgBatBatTestRequMinutesWithoutMainsFail_Object(
    (1, 3, 6, 1, 4, 1, 26854, 3, 2, 1, 20, 1, 20, 1, 15, 3, 76),
    _Es1dc1CfgBatBatTestRequMinutesWithoutMainsFail_Type()
)
es1dc1CfgBatBatTestRequMinutesWithoutMainsFail.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es1dc1CfgBatBatTestRequMinutesWithoutMainsFail.setStatus("current")
_Es1dc1CfgBatBatTestSchedulerCronRule_Type = DisplayString
_Es1dc1CfgBatBatTestSchedulerCronRule_Object = MibScalar
es1dc1CfgBatBatTestSchedulerCronRule = _Es1dc1CfgBatBatTestSchedulerCronRule_Object(
    (1, 3, 6, 1, 4, 1, 26854, 3, 2, 1, 20, 1, 20, 1, 15, 3, 77),
    _Es1dc1CfgBatBatTestSchedulerCronRule_Type()
)
es1dc1CfgBatBatTestSchedulerCronRule.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es1dc1CfgBatBatTestSchedulerCronRule.setStatus("current")
_Es1dc1CfgSmartEnergySmartEnergyBooleanCond_Type = DisplayString
_Es1dc1CfgSmartEnergySmartEnergyBooleanCond_Object = MibScalar
es1dc1CfgSmartEnergySmartEnergyBooleanCond = _Es1dc1CfgSmartEnergySmartEnergyBooleanCond_Object(
    (1, 3, 6, 1, 4, 1, 26854, 3, 2, 1, 20, 1, 20, 1, 15, 3, 83),
    _Es1dc1CfgSmartEnergySmartEnergyBooleanCond_Type()
)
es1dc1CfgSmartEnergySmartEnergyBooleanCond.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es1dc1CfgSmartEnergySmartEnergyBooleanCond.setStatus("current")
_Es1dc1CfgLVDBatLVDNodeId_Type = DisplayString
_Es1dc1CfgLVDBatLVDNodeId_Object = MibScalar
es1dc1CfgLVDBatLVDNodeId = _Es1dc1CfgLVDBatLVDNodeId_Object(
    (1, 3, 6, 1, 4, 1, 26854, 3, 2, 1, 20, 1, 20, 1, 15, 3, 86),
    _Es1dc1CfgLVDBatLVDNodeId_Type()
)
es1dc1CfgLVDBatLVDNodeId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es1dc1CfgLVDBatLVDNodeId.setStatus("current")
_Es1dc1CfgDigInputsDigInput1Name_Type = DisplayString
_Es1dc1CfgDigInputsDigInput1Name_Object = MibScalar
es1dc1CfgDigInputsDigInput1Name = _Es1dc1CfgDigInputsDigInput1Name_Object(
    (1, 3, 6, 1, 4, 1, 26854, 3, 2, 1, 20, 1, 20, 1, 15, 3, 91),
    _Es1dc1CfgDigInputsDigInput1Name_Type()
)
es1dc1CfgDigInputsDigInput1Name.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es1dc1CfgDigInputsDigInput1Name.setStatus("current")
_Es1dc1CfgDigInputsDigInput1NormallyClosed_Type = DisplayString
_Es1dc1CfgDigInputsDigInput1NormallyClosed_Object = MibScalar
es1dc1CfgDigInputsDigInput1NormallyClosed = _Es1dc1CfgDigInputsDigInput1NormallyClosed_Object(
    (1, 3, 6, 1, 4, 1, 26854, 3, 2, 1, 20, 1, 20, 1, 15, 3, 92),
    _Es1dc1CfgDigInputsDigInput1NormallyClosed_Type()
)
es1dc1CfgDigInputsDigInput1NormallyClosed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es1dc1CfgDigInputsDigInput1NormallyClosed.setStatus("current")
_Es1dc1CfgDigInputsDigInput2Name_Type = DisplayString
_Es1dc1CfgDigInputsDigInput2Name_Object = MibScalar
es1dc1CfgDigInputsDigInput2Name = _Es1dc1CfgDigInputsDigInput2Name_Object(
    (1, 3, 6, 1, 4, 1, 26854, 3, 2, 1, 20, 1, 20, 1, 15, 3, 93),
    _Es1dc1CfgDigInputsDigInput2Name_Type()
)
es1dc1CfgDigInputsDigInput2Name.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es1dc1CfgDigInputsDigInput2Name.setStatus("current")
_Es1dc1CfgDigInputsDigInput2NormallyClosed_Type = DisplayString
_Es1dc1CfgDigInputsDigInput2NormallyClosed_Object = MibScalar
es1dc1CfgDigInputsDigInput2NormallyClosed = _Es1dc1CfgDigInputsDigInput2NormallyClosed_Object(
    (1, 3, 6, 1, 4, 1, 26854, 3, 2, 1, 20, 1, 20, 1, 15, 3, 94),
    _Es1dc1CfgDigInputsDigInput2NormallyClosed_Type()
)
es1dc1CfgDigInputsDigInput2NormallyClosed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es1dc1CfgDigInputsDigInput2NormallyClosed.setStatus("current")
_Es1dc1CfgDigInputsDigInput3Name_Type = DisplayString
_Es1dc1CfgDigInputsDigInput3Name_Object = MibScalar
es1dc1CfgDigInputsDigInput3Name = _Es1dc1CfgDigInputsDigInput3Name_Object(
    (1, 3, 6, 1, 4, 1, 26854, 3, 2, 1, 20, 1, 20, 1, 15, 3, 95),
    _Es1dc1CfgDigInputsDigInput3Name_Type()
)
es1dc1CfgDigInputsDigInput3Name.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es1dc1CfgDigInputsDigInput3Name.setStatus("current")
_Es1dc1CfgDigInputsDigInput3NormallyClosed_Type = DisplayString
_Es1dc1CfgDigInputsDigInput3NormallyClosed_Object = MibScalar
es1dc1CfgDigInputsDigInput3NormallyClosed = _Es1dc1CfgDigInputsDigInput3NormallyClosed_Object(
    (1, 3, 6, 1, 4, 1, 26854, 3, 2, 1, 20, 1, 20, 1, 15, 3, 96),
    _Es1dc1CfgDigInputsDigInput3NormallyClosed_Type()
)
es1dc1CfgDigInputsDigInput3NormallyClosed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es1dc1CfgDigInputsDigInput3NormallyClosed.setStatus("current")
_Es1dc1CfgDigInputsDigInput4Name_Type = DisplayString
_Es1dc1CfgDigInputsDigInput4Name_Object = MibScalar
es1dc1CfgDigInputsDigInput4Name = _Es1dc1CfgDigInputsDigInput4Name_Object(
    (1, 3, 6, 1, 4, 1, 26854, 3, 2, 1, 20, 1, 20, 1, 15, 3, 97),
    _Es1dc1CfgDigInputsDigInput4Name_Type()
)
es1dc1CfgDigInputsDigInput4Name.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es1dc1CfgDigInputsDigInput4Name.setStatus("current")
_Es1dc1CfgDigInputsDigInput4NormallyClosed_Type = DisplayString
_Es1dc1CfgDigInputsDigInput4NormallyClosed_Object = MibScalar
es1dc1CfgDigInputsDigInput4NormallyClosed = _Es1dc1CfgDigInputsDigInput4NormallyClosed_Object(
    (1, 3, 6, 1, 4, 1, 26854, 3, 2, 1, 20, 1, 20, 1, 15, 3, 98),
    _Es1dc1CfgDigInputsDigInput4NormallyClosed_Type()
)
es1dc1CfgDigInputsDigInput4NormallyClosed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es1dc1CfgDigInputsDigInput4NormallyClosed.setStatus("current")
_Es1dc1CfgDigInputsDigInput5Name_Type = DisplayString
_Es1dc1CfgDigInputsDigInput5Name_Object = MibScalar
es1dc1CfgDigInputsDigInput5Name = _Es1dc1CfgDigInputsDigInput5Name_Object(
    (1, 3, 6, 1, 4, 1, 26854, 3, 2, 1, 20, 1, 20, 1, 15, 3, 99),
    _Es1dc1CfgDigInputsDigInput5Name_Type()
)
es1dc1CfgDigInputsDigInput5Name.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es1dc1CfgDigInputsDigInput5Name.setStatus("current")
_Es1dc1CfgDigInputsDigInput5NormallyClosed_Type = DisplayString
_Es1dc1CfgDigInputsDigInput5NormallyClosed_Object = MibScalar
es1dc1CfgDigInputsDigInput5NormallyClosed = _Es1dc1CfgDigInputsDigInput5NormallyClosed_Object(
    (1, 3, 6, 1, 4, 1, 26854, 3, 2, 1, 20, 1, 20, 1, 15, 3, 100),
    _Es1dc1CfgDigInputsDigInput5NormallyClosed_Type()
)
es1dc1CfgDigInputsDigInput5NormallyClosed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es1dc1CfgDigInputsDigInput5NormallyClosed.setStatus("current")
_Es1dc1CfgDigInputsDigInput6Name_Type = DisplayString
_Es1dc1CfgDigInputsDigInput6Name_Object = MibScalar
es1dc1CfgDigInputsDigInput6Name = _Es1dc1CfgDigInputsDigInput6Name_Object(
    (1, 3, 6, 1, 4, 1, 26854, 3, 2, 1, 20, 1, 20, 1, 15, 3, 101),
    _Es1dc1CfgDigInputsDigInput6Name_Type()
)
es1dc1CfgDigInputsDigInput6Name.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es1dc1CfgDigInputsDigInput6Name.setStatus("current")
_Es1dc1CfgDigInputsDigInput6NormallyClosed_Type = DisplayString
_Es1dc1CfgDigInputsDigInput6NormallyClosed_Object = MibScalar
es1dc1CfgDigInputsDigInput6NormallyClosed = _Es1dc1CfgDigInputsDigInput6NormallyClosed_Object(
    (1, 3, 6, 1, 4, 1, 26854, 3, 2, 1, 20, 1, 20, 1, 15, 3, 102),
    _Es1dc1CfgDigInputsDigInput6NormallyClosed_Type()
)
es1dc1CfgDigInputsDigInput6NormallyClosed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es1dc1CfgDigInputsDigInput6NormallyClosed.setStatus("current")
_Es1dc1CfgRelsDryAlarm1AlternativeBooleanCond_Type = DisplayString
_Es1dc1CfgRelsDryAlarm1AlternativeBooleanCond_Object = MibScalar
es1dc1CfgRelsDryAlarm1AlternativeBooleanCond = _Es1dc1CfgRelsDryAlarm1AlternativeBooleanCond_Object(
    (1, 3, 6, 1, 4, 1, 26854, 3, 2, 1, 20, 1, 20, 1, 15, 3, 111),
    _Es1dc1CfgRelsDryAlarm1AlternativeBooleanCond_Type()
)
es1dc1CfgRelsDryAlarm1AlternativeBooleanCond.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es1dc1CfgRelsDryAlarm1AlternativeBooleanCond.setStatus("current")
_Es1dc1CfgRelsDryAlarm2AlternativeBooleanCond_Type = DisplayString
_Es1dc1CfgRelsDryAlarm2AlternativeBooleanCond_Object = MibScalar
es1dc1CfgRelsDryAlarm2AlternativeBooleanCond = _Es1dc1CfgRelsDryAlarm2AlternativeBooleanCond_Object(
    (1, 3, 6, 1, 4, 1, 26854, 3, 2, 1, 20, 1, 20, 1, 15, 3, 112),
    _Es1dc1CfgRelsDryAlarm2AlternativeBooleanCond_Type()
)
es1dc1CfgRelsDryAlarm2AlternativeBooleanCond.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es1dc1CfgRelsDryAlarm2AlternativeBooleanCond.setStatus("current")
_Es1dc1CfgRelsDryAlarm3AlternativeBooleanCond_Type = DisplayString
_Es1dc1CfgRelsDryAlarm3AlternativeBooleanCond_Object = MibScalar
es1dc1CfgRelsDryAlarm3AlternativeBooleanCond = _Es1dc1CfgRelsDryAlarm3AlternativeBooleanCond_Object(
    (1, 3, 6, 1, 4, 1, 26854, 3, 2, 1, 20, 1, 20, 1, 15, 3, 113),
    _Es1dc1CfgRelsDryAlarm3AlternativeBooleanCond_Type()
)
es1dc1CfgRelsDryAlarm3AlternativeBooleanCond.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es1dc1CfgRelsDryAlarm3AlternativeBooleanCond.setStatus("current")
_Es1dc1CfgRelsDryAlarm4AlternativeBooleanCond_Type = DisplayString
_Es1dc1CfgRelsDryAlarm4AlternativeBooleanCond_Object = MibScalar
es1dc1CfgRelsDryAlarm4AlternativeBooleanCond = _Es1dc1CfgRelsDryAlarm4AlternativeBooleanCond_Object(
    (1, 3, 6, 1, 4, 1, 26854, 3, 2, 1, 20, 1, 20, 1, 15, 3, 114),
    _Es1dc1CfgRelsDryAlarm4AlternativeBooleanCond_Type()
)
es1dc1CfgRelsDryAlarm4AlternativeBooleanCond.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es1dc1CfgRelsDryAlarm4AlternativeBooleanCond.setStatus("current")
_Es1dc1CfgSensorsAmbientTempLow_Type = DisplayString
_Es1dc1CfgSensorsAmbientTempLow_Object = MibScalar
es1dc1CfgSensorsAmbientTempLow = _Es1dc1CfgSensorsAmbientTempLow_Object(
    (1, 3, 6, 1, 4, 1, 26854, 3, 2, 1, 20, 1, 20, 1, 15, 3, 131),
    _Es1dc1CfgSensorsAmbientTempLow_Type()
)
es1dc1CfgSensorsAmbientTempLow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es1dc1CfgSensorsAmbientTempLow.setStatus("current")
_Es1dc1CfgSensorsAmbientTempHigh_Type = DisplayString
_Es1dc1CfgSensorsAmbientTempHigh_Object = MibScalar
es1dc1CfgSensorsAmbientTempHigh = _Es1dc1CfgSensorsAmbientTempHigh_Object(
    (1, 3, 6, 1, 4, 1, 26854, 3, 2, 1, 20, 1, 20, 1, 15, 3, 132),
    _Es1dc1CfgSensorsAmbientTempHigh_Type()
)
es1dc1CfgSensorsAmbientTempHigh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es1dc1CfgSensorsAmbientTempHigh.setStatus("current")
_Es1dc1CfgSensorsAmbientTempHysteresis_Type = DisplayString
_Es1dc1CfgSensorsAmbientTempHysteresis_Object = MibScalar
es1dc1CfgSensorsAmbientTempHysteresis = _Es1dc1CfgSensorsAmbientTempHysteresis_Object(
    (1, 3, 6, 1, 4, 1, 26854, 3, 2, 1, 20, 1, 20, 1, 15, 3, 133),
    _Es1dc1CfgSensorsAmbientTempHysteresis_Type()
)
es1dc1CfgSensorsAmbientTempHysteresis.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es1dc1CfgSensorsAmbientTempHysteresis.setStatus("current")
_Es1dc1CfgGenericReadAccessUserNumbers_Type = DisplayString
_Es1dc1CfgGenericReadAccessUserNumbers_Object = MibScalar
es1dc1CfgGenericReadAccessUserNumbers = _Es1dc1CfgGenericReadAccessUserNumbers_Object(
    (1, 3, 6, 1, 4, 1, 26854, 3, 2, 1, 20, 1, 20, 1, 15, 3, 521),
    _Es1dc1CfgGenericReadAccessUserNumbers_Type()
)
es1dc1CfgGenericReadAccessUserNumbers.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es1dc1CfgGenericReadAccessUserNumbers.setStatus("current")
_Es1dc1CfgGenericWriteAccessUserNumbers_Type = DisplayString
_Es1dc1CfgGenericWriteAccessUserNumbers_Object = MibScalar
es1dc1CfgGenericWriteAccessUserNumbers = _Es1dc1CfgGenericWriteAccessUserNumbers_Object(
    (1, 3, 6, 1, 4, 1, 26854, 3, 2, 1, 20, 1, 20, 1, 15, 3, 522),
    _Es1dc1CfgGenericWriteAccessUserNumbers_Type()
)
es1dc1CfgGenericWriteAccessUserNumbers.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es1dc1CfgGenericWriteAccessUserNumbers.setStatus("current")
_Es1dc1CfgGenericEventTableLength_Type = DisplayString
_Es1dc1CfgGenericEventTableLength_Object = MibScalar
es1dc1CfgGenericEventTableLength = _Es1dc1CfgGenericEventTableLength_Object(
    (1, 3, 6, 1, 4, 1, 26854, 3, 2, 1, 20, 1, 20, 1, 15, 3, 601),
    _Es1dc1CfgGenericEventTableLength_Type()
)
es1dc1CfgGenericEventTableLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es1dc1CfgGenericEventTableLength.setStatus("current")
_Es1dc1CfgGenericEventTableLengthByRectifier_Type = DisplayString
_Es1dc1CfgGenericEventTableLengthByRectifier_Object = MibScalar
es1dc1CfgGenericEventTableLengthByRectifier = _Es1dc1CfgGenericEventTableLengthByRectifier_Object(
    (1, 3, 6, 1, 4, 1, 26854, 3, 2, 1, 20, 1, 20, 1, 15, 3, 602),
    _Es1dc1CfgGenericEventTableLengthByRectifier_Type()
)
es1dc1CfgGenericEventTableLengthByRectifier.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es1dc1CfgGenericEventTableLengthByRectifier.setStatus("current")
_Es1dc1CfgPLCNumberOfPLCData_Type = DisplayString
_Es1dc1CfgPLCNumberOfPLCData_Object = MibScalar
es1dc1CfgPLCNumberOfPLCData = _Es1dc1CfgPLCNumberOfPLCData_Object(
    (1, 3, 6, 1, 4, 1, 26854, 3, 2, 1, 20, 1, 20, 1, 15, 3, 901),
    _Es1dc1CfgPLCNumberOfPLCData_Type()
)
es1dc1CfgPLCNumberOfPLCData.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es1dc1CfgPLCNumberOfPLCData.setStatus("current")
_Es1dc1CfgPLCNumberOfPLCAlarm_Type = DisplayString
_Es1dc1CfgPLCNumberOfPLCAlarm_Object = MibScalar
es1dc1CfgPLCNumberOfPLCAlarm = _Es1dc1CfgPLCNumberOfPLCAlarm_Object(
    (1, 3, 6, 1, 4, 1, 26854, 3, 2, 1, 20, 1, 20, 1, 15, 3, 902),
    _Es1dc1CfgPLCNumberOfPLCAlarm_Type()
)
es1dc1CfgPLCNumberOfPLCAlarm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es1dc1CfgPLCNumberOfPLCAlarm.setStatus("current")
_Es1dc1Control_ObjectIdentity = ObjectIdentity
es1dc1Control = _Es1dc1Control_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 26854, 3, 2, 1, 20, 1, 20, 1, 16)
)
_Es1dc1ControlNumber_Type = Integer32
_Es1dc1ControlNumber_Object = MibScalar
es1dc1ControlNumber = _Es1dc1ControlNumber_Object(
    (1, 3, 6, 1, 4, 1, 26854, 3, 2, 1, 20, 1, 20, 1, 16, 1),
    _Es1dc1ControlNumber_Type()
)
es1dc1ControlNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es1dc1ControlNumber.setStatus("current")
_Es1dc1ControlTable_Object = MibTable
es1dc1ControlTable = _Es1dc1ControlTable_Object(
    (1, 3, 6, 1, 4, 1, 26854, 3, 2, 1, 20, 1, 20, 1, 16, 2)
)
if mibBuilder.loadTexts:
    es1dc1ControlTable.setStatus("current")
_Es1dc1ControlEntry_Object = MibTableRow
es1dc1ControlEntry = _Es1dc1ControlEntry_Object(
    (1, 3, 6, 1, 4, 1, 26854, 3, 2, 1, 20, 1, 20, 1, 16, 2, 1)
)
es1dc1ControlEntry.setIndexNames(
    (0, "SITE-MONITORING-MIB", "es1dc1ControlIndex"),
)
if mibBuilder.loadTexts:
    es1dc1ControlEntry.setStatus("current")
_Es1dc1ControlIndex_Type = Unsigned32
_Es1dc1ControlIndex_Object = MibTableColumn
es1dc1ControlIndex = _Es1dc1ControlIndex_Object(
    (1, 3, 6, 1, 4, 1, 26854, 3, 2, 1, 20, 1, 20, 1, 16, 2, 1, 1),
    _Es1dc1ControlIndex_Type()
)
es1dc1ControlIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    es1dc1ControlIndex.setStatus("current")
_Es1dc1ControlName_Type = DisplayString
_Es1dc1ControlName_Object = MibTableColumn
es1dc1ControlName = _Es1dc1ControlName_Object(
    (1, 3, 6, 1, 4, 1, 26854, 3, 2, 1, 20, 1, 20, 1, 16, 2, 1, 2),
    _Es1dc1ControlName_Type()
)
es1dc1ControlName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es1dc1ControlName.setStatus("current")
_Es1dc1ControlValue_Type = DisplayString
_Es1dc1ControlValue_Object = MibTableColumn
es1dc1ControlValue = _Es1dc1ControlValue_Object(
    (1, 3, 6, 1, 4, 1, 26854, 3, 2, 1, 20, 1, 20, 1, 16, 2, 1, 3),
    _Es1dc1ControlValue_Type()
)
es1dc1ControlValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es1dc1ControlValue.setStatus("current")
_Es1dc1ControlEntryStatus_Type = RowStatus
_Es1dc1ControlEntryStatus_Object = MibTableColumn
es1dc1ControlEntryStatus = _Es1dc1ControlEntryStatus_Object(
    (1, 3, 6, 1, 4, 1, 26854, 3, 2, 1, 20, 1, 20, 1, 16, 2, 1, 4),
    _Es1dc1ControlEntryStatus_Type()
)
es1dc1ControlEntryStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    es1dc1ControlEntryStatus.setStatus("current")
_Es1dc1ControlList_ObjectIdentity = ObjectIdentity
es1dc1ControlList = _Es1dc1ControlList_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 26854, 3, 2, 1, 20, 1, 20, 1, 16, 3)
)
_Es1dc1CtrlSystemBackToFloat_Type = DisplayString
_Es1dc1CtrlSystemBackToFloat_Object = MibScalar
es1dc1CtrlSystemBackToFloat = _Es1dc1CtrlSystemBackToFloat_Object(
    (1, 3, 6, 1, 4, 1, 26854, 3, 2, 1, 20, 1, 20, 1, 16, 3, 1),
    _Es1dc1CtrlSystemBackToFloat_Type()
)
es1dc1CtrlSystemBackToFloat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es1dc1CtrlSystemBackToFloat.setStatus("current")
_Es1dc1CtrlSystemStartBatTest_Type = DisplayString
_Es1dc1CtrlSystemStartBatTest_Object = MibScalar
es1dc1CtrlSystemStartBatTest = _Es1dc1CtrlSystemStartBatTest_Object(
    (1, 3, 6, 1, 4, 1, 26854, 3, 2, 1, 20, 1, 20, 1, 16, 3, 2),
    _Es1dc1CtrlSystemStartBatTest_Type()
)
es1dc1CtrlSystemStartBatTest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es1dc1CtrlSystemStartBatTest.setStatus("current")
_Es1dc1CtrlSystemForceBatTest_Type = DisplayString
_Es1dc1CtrlSystemForceBatTest_Object = MibScalar
es1dc1CtrlSystemForceBatTest = _Es1dc1CtrlSystemForceBatTest_Object(
    (1, 3, 6, 1, 4, 1, 26854, 3, 2, 1, 20, 1, 20, 1, 16, 3, 3),
    _Es1dc1CtrlSystemForceBatTest_Type()
)
es1dc1CtrlSystemForceBatTest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es1dc1CtrlSystemForceBatTest.setStatus("current")
_Es1dc1CtrlSystemStartBoostMode_Type = DisplayString
_Es1dc1CtrlSystemStartBoostMode_Object = MibScalar
es1dc1CtrlSystemStartBoostMode = _Es1dc1CtrlSystemStartBoostMode_Object(
    (1, 3, 6, 1, 4, 1, 26854, 3, 2, 1, 20, 1, 20, 1, 16, 3, 4),
    _Es1dc1CtrlSystemStartBoostMode_Type()
)
es1dc1CtrlSystemStartBoostMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es1dc1CtrlSystemStartBoostMode.setStatus("current")
_Es1dc1CtrlLVDOpenTheLVD_Type = DisplayString
_Es1dc1CtrlLVDOpenTheLVD_Object = MibScalar
es1dc1CtrlLVDOpenTheLVD = _Es1dc1CtrlLVDOpenTheLVD_Object(
    (1, 3, 6, 1, 4, 1, 26854, 3, 2, 1, 20, 1, 20, 1, 16, 3, 11),
    _Es1dc1CtrlLVDOpenTheLVD_Type()
)
es1dc1CtrlLVDOpenTheLVD.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es1dc1CtrlLVDOpenTheLVD.setStatus("current")
_Es1dc1CtrlLVDCloseTheLVD_Type = DisplayString
_Es1dc1CtrlLVDCloseTheLVD_Object = MibScalar
es1dc1CtrlLVDCloseTheLVD = _Es1dc1CtrlLVDCloseTheLVD_Object(
    (1, 3, 6, 1, 4, 1, 26854, 3, 2, 1, 20, 1, 20, 1, 16, 3, 12),
    _Es1dc1CtrlLVDCloseTheLVD_Type()
)
es1dc1CtrlLVDCloseTheLVD.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es1dc1CtrlLVDCloseTheLVD.setStatus("current")
_Es1dc1CtrlBatCorrectBatCurrentOffset_Type = DisplayString
_Es1dc1CtrlBatCorrectBatCurrentOffset_Object = MibScalar
es1dc1CtrlBatCorrectBatCurrentOffset = _Es1dc1CtrlBatCorrectBatCurrentOffset_Object(
    (1, 3, 6, 1, 4, 1, 26854, 3, 2, 1, 20, 1, 20, 1, 16, 3, 21),
    _Es1dc1CtrlBatCorrectBatCurrentOffset_Type()
)
es1dc1CtrlBatCorrectBatCurrentOffset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es1dc1CtrlBatCorrectBatCurrentOffset.setStatus("current")
_Es1dc1CtrlBatResetLastBatTestState_Type = DisplayString
_Es1dc1CtrlBatResetLastBatTestState_Object = MibScalar
es1dc1CtrlBatResetLastBatTestState = _Es1dc1CtrlBatResetLastBatTestState_Object(
    (1, 3, 6, 1, 4, 1, 26854, 3, 2, 1, 20, 1, 20, 1, 16, 3, 41),
    _Es1dc1CtrlBatResetLastBatTestState_Type()
)
es1dc1CtrlBatResetLastBatTestState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es1dc1CtrlBatResetLastBatTestState.setStatus("current")
_Es1dc1CtrlSaveSaveConfInMCU_Type = DisplayString
_Es1dc1CtrlSaveSaveConfInMCU_Object = MibScalar
es1dc1CtrlSaveSaveConfInMCU = _Es1dc1CtrlSaveSaveConfInMCU_Object(
    (1, 3, 6, 1, 4, 1, 26854, 3, 2, 1, 20, 1, 20, 1, 16, 3, 51),
    _Es1dc1CtrlSaveSaveConfInMCU_Type()
)
es1dc1CtrlSaveSaveConfInMCU.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es1dc1CtrlSaveSaveConfInMCU.setStatus("current")
_Es1dc1CtrlAdvancedSetMCUSpecificConfId_Type = DisplayString
_Es1dc1CtrlAdvancedSetMCUSpecificConfId_Object = MibScalar
es1dc1CtrlAdvancedSetMCUSpecificConfId = _Es1dc1CtrlAdvancedSetMCUSpecificConfId_Object(
    (1, 3, 6, 1, 4, 1, 26854, 3, 2, 1, 20, 1, 20, 1, 16, 3, 55),
    _Es1dc1CtrlAdvancedSetMCUSpecificConfId_Type()
)
es1dc1CtrlAdvancedSetMCUSpecificConfId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es1dc1CtrlAdvancedSetMCUSpecificConfId.setStatus("current")
_Es1dc1CtrlDigInputsSetDigInput4CounterValue_Type = DisplayString
_Es1dc1CtrlDigInputsSetDigInput4CounterValue_Object = MibScalar
es1dc1CtrlDigInputsSetDigInput4CounterValue = _Es1dc1CtrlDigInputsSetDigInput4CounterValue_Object(
    (1, 3, 6, 1, 4, 1, 26854, 3, 2, 1, 20, 1, 20, 1, 16, 3, 61),
    _Es1dc1CtrlDigInputsSetDigInput4CounterValue_Type()
)
es1dc1CtrlDigInputsSetDigInput4CounterValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es1dc1CtrlDigInputsSetDigInput4CounterValue.setStatus("current")
_Es1dc1CtrlRelsInvertRel1StateForXSeconds_Type = DisplayString
_Es1dc1CtrlRelsInvertRel1StateForXSeconds_Object = MibScalar
es1dc1CtrlRelsInvertRel1StateForXSeconds = _Es1dc1CtrlRelsInvertRel1StateForXSeconds_Object(
    (1, 3, 6, 1, 4, 1, 26854, 3, 2, 1, 20, 1, 20, 1, 16, 3, 111),
    _Es1dc1CtrlRelsInvertRel1StateForXSeconds_Type()
)
es1dc1CtrlRelsInvertRel1StateForXSeconds.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es1dc1CtrlRelsInvertRel1StateForXSeconds.setStatus("current")
_Es1dc1CtrlRelsInvertRel2StateForXSeconds_Type = DisplayString
_Es1dc1CtrlRelsInvertRel2StateForXSeconds_Object = MibScalar
es1dc1CtrlRelsInvertRel2StateForXSeconds = _Es1dc1CtrlRelsInvertRel2StateForXSeconds_Object(
    (1, 3, 6, 1, 4, 1, 26854, 3, 2, 1, 20, 1, 20, 1, 16, 3, 112),
    _Es1dc1CtrlRelsInvertRel2StateForXSeconds_Type()
)
es1dc1CtrlRelsInvertRel2StateForXSeconds.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es1dc1CtrlRelsInvertRel2StateForXSeconds.setStatus("current")
_Es1dc1CtrlRelsInvertRel3StateForXSeconds_Type = DisplayString
_Es1dc1CtrlRelsInvertRel3StateForXSeconds_Object = MibScalar
es1dc1CtrlRelsInvertRel3StateForXSeconds = _Es1dc1CtrlRelsInvertRel3StateForXSeconds_Object(
    (1, 3, 6, 1, 4, 1, 26854, 3, 2, 1, 20, 1, 20, 1, 16, 3, 113),
    _Es1dc1CtrlRelsInvertRel3StateForXSeconds_Type()
)
es1dc1CtrlRelsInvertRel3StateForXSeconds.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es1dc1CtrlRelsInvertRel3StateForXSeconds.setStatus("current")
_Es1dc1CtrlRelsInvertRel4StateForXSeconds_Type = DisplayString
_Es1dc1CtrlRelsInvertRel4StateForXSeconds_Object = MibScalar
es1dc1CtrlRelsInvertRel4StateForXSeconds = _Es1dc1CtrlRelsInvertRel4StateForXSeconds_Object(
    (1, 3, 6, 1, 4, 1, 26854, 3, 2, 1, 20, 1, 20, 1, 16, 3, 114),
    _Es1dc1CtrlRelsInvertRel4StateForXSeconds_Type()
)
es1dc1CtrlRelsInvertRel4StateForXSeconds.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es1dc1CtrlRelsInvertRel4StateForXSeconds.setStatus("current")
_Es1dc1CtrlGenericClearMyEvents_Type = DisplayString
_Es1dc1CtrlGenericClearMyEvents_Object = MibScalar
es1dc1CtrlGenericClearMyEvents = _Es1dc1CtrlGenericClearMyEvents_Object(
    (1, 3, 6, 1, 4, 1, 26854, 3, 2, 1, 20, 1, 20, 1, 16, 3, 501),
    _Es1dc1CtrlGenericClearMyEvents_Type()
)
es1dc1CtrlGenericClearMyEvents.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es1dc1CtrlGenericClearMyEvents.setStatus("current")
_Es1dc1CtrlGenericClearAllEvents_Type = DisplayString
_Es1dc1CtrlGenericClearAllEvents_Object = MibScalar
es1dc1CtrlGenericClearAllEvents = _Es1dc1CtrlGenericClearAllEvents_Object(
    (1, 3, 6, 1, 4, 1, 26854, 3, 2, 1, 20, 1, 20, 1, 16, 3, 502),
    _Es1dc1CtrlGenericClearAllEvents_Type()
)
es1dc1CtrlGenericClearAllEvents.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es1dc1CtrlGenericClearAllEvents.setStatus("current")
_Es1dc1CtrlGenericAddEvent_Type = DisplayString
_Es1dc1CtrlGenericAddEvent_Object = MibScalar
es1dc1CtrlGenericAddEvent = _Es1dc1CtrlGenericAddEvent_Object(
    (1, 3, 6, 1, 4, 1, 26854, 3, 2, 1, 20, 1, 20, 1, 16, 3, 511),
    _Es1dc1CtrlGenericAddEvent_Type()
)
es1dc1CtrlGenericAddEvent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es1dc1CtrlGenericAddEvent.setStatus("current")
_Es1dc1CtrlGenericAddMajorEvent_Type = DisplayString
_Es1dc1CtrlGenericAddMajorEvent_Object = MibScalar
es1dc1CtrlGenericAddMajorEvent = _Es1dc1CtrlGenericAddMajorEvent_Object(
    (1, 3, 6, 1, 4, 1, 26854, 3, 2, 1, 20, 1, 20, 1, 16, 3, 512),
    _Es1dc1CtrlGenericAddMajorEvent_Type()
)
es1dc1CtrlGenericAddMajorEvent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es1dc1CtrlGenericAddMajorEvent.setStatus("current")
_Es1dc1CtrlGenericResetDefaultNamesAndGroups_Type = DisplayString
_Es1dc1CtrlGenericResetDefaultNamesAndGroups_Object = MibScalar
es1dc1CtrlGenericResetDefaultNamesAndGroups = _Es1dc1CtrlGenericResetDefaultNamesAndGroups_Object(
    (1, 3, 6, 1, 4, 1, 26854, 3, 2, 1, 20, 1, 20, 1, 16, 3, 521),
    _Es1dc1CtrlGenericResetDefaultNamesAndGroups_Type()
)
es1dc1CtrlGenericResetDefaultNamesAndGroups.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es1dc1CtrlGenericResetDefaultNamesAndGroups.setStatus("current")
_Es1dc1CtrlGenericResetDefaultNamesAndGroupsRecursive_Type = DisplayString
_Es1dc1CtrlGenericResetDefaultNamesAndGroupsRecursive_Object = MibScalar
es1dc1CtrlGenericResetDefaultNamesAndGroupsRecursive = _Es1dc1CtrlGenericResetDefaultNamesAndGroupsRecursive_Object(
    (1, 3, 6, 1, 4, 1, 26854, 3, 2, 1, 20, 1, 20, 1, 16, 3, 522),
    _Es1dc1CtrlGenericResetDefaultNamesAndGroupsRecursive_Type()
)
es1dc1CtrlGenericResetDefaultNamesAndGroupsRecursive.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es1dc1CtrlGenericResetDefaultNamesAndGroupsRecursive.setStatus("current")
_Es1dc1Notifications_ObjectIdentity = ObjectIdentity
es1dc1Notifications = _Es1dc1Notifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 26854, 3, 2, 1, 20, 1, 20, 1, 18)
)
_Es1dc1NotificationPrefix_ObjectIdentity = ObjectIdentity
es1dc1NotificationPrefix = _Es1dc1NotificationPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 26854, 3, 2, 1, 20, 1, 20, 1, 18, 0)
)
_Es1dc1Compliance_ObjectIdentity = ObjectIdentity
es1dc1Compliance = _Es1dc1Compliance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 26854, 3, 2, 1, 20, 1, 20, 1, 19)
)
_Es1dc1ComplianceGroups_ObjectIdentity = ObjectIdentity
es1dc1ComplianceGroups = _Es1dc1ComplianceGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 26854, 3, 2, 1, 20, 1, 20, 1, 19, 1)
)
_Es1InverterSystems_ObjectIdentity = ObjectIdentity
es1InverterSystems = _Es1InverterSystems_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 26854, 3, 2, 1, 20, 1, 25)
)
_Es1RemotePowerFeedingSystems_ObjectIdentity = ObjectIdentity
es1RemotePowerFeedingSystems = _Es1RemotePowerFeedingSystems_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 26854, 3, 2, 1, 20, 1, 28)
)
_Extensions_ObjectIdentity = ObjectIdentity
extensions = _Extensions_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 26854, 3, 2, 1, 21)
)

# Managed Objects groups

siteV1GlobalGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 26854, 3, 2, 1, 19, 1, 1)
)
siteV1GlobalGroup.setObjects(
      *(("SITE-MONITORING-MIB", "siteV1GlobalStatus"),
        ("SITE-MONITORING-MIB", "siteV1GlobalAlarmSeverityType"),
        ("SITE-MONITORING-MIB", "siteV1GlobalAlarmSeverityLevel"),
        ("SITE-MONITORING-MIB", "siteV1GlobalAlarmSeverityTypeInt"),
        ("SITE-MONITORING-MIB", "siteV1DescriptionNumber"),
        ("SITE-MONITORING-MIB", "siteV1DescriptionName"),
        ("SITE-MONITORING-MIB", "siteV1DescriptionValue"),
        ("SITE-MONITORING-MIB", "siteV1DescriptionEntryStatus"),
        ("SITE-MONITORING-MIB", "siteV1DescDescriptionSiteNumber"),
        ("SITE-MONITORING-MIB", "siteV1DescDescriptionSiteName"),
        ("SITE-MONITORING-MIB", "siteV1DescDescriptionShortDescription"),
        ("SITE-MONITORING-MIB", "siteV1DescDescriptionInfo"),
        ("SITE-MONITORING-MIB", "siteV1DescDescriptionDescription"),
        ("SITE-MONITORING-MIB", "siteV1DescDescriptionReference"),
        ("SITE-MONITORING-MIB", "siteV1DescDescriptionContactName"),
        ("SITE-MONITORING-MIB", "siteV1DescDescriptionPhoneNumber"),
        ("SITE-MONITORING-MIB", "siteV1DescDescriptionStreet"),
        ("SITE-MONITORING-MIB", "siteV1DescDescriptionCity"),
        ("SITE-MONITORING-MIB", "siteV1DescDescriptionProvince"),
        ("SITE-MONITORING-MIB", "siteV1DescDescriptionPostalCode"),
        ("SITE-MONITORING-MIB", "siteV1DescDescriptionRegion"),
        ("SITE-MONITORING-MIB", "siteV1DescDescriptionCountry"),
        ("SITE-MONITORING-MIB", "siteV1DescDescriptionGroup1"),
        ("SITE-MONITORING-MIB", "siteV1DescDescriptionGroup2"),
        ("SITE-MONITORING-MIB", "siteV1DescDescriptionGroup3"),
        ("SITE-MONITORING-MIB", "siteV1DescDescriptionGroup4"),
        ("SITE-MONITORING-MIB", "siteV1DescDescriptionGroup5"),
        ("SITE-MONITORING-MIB", "siteV1DescDescriptionLatitude"),
        ("SITE-MONITORING-MIB", "siteV1DescDescriptionLongitude"),
        ("SITE-MONITORING-MIB", "siteV1DescDescriptionAltitude"),
        ("SITE-MONITORING-MIB", "siteV1DescControllerSoftwareRevision"),
        ("SITE-MONITORING-MIB", "siteV1DescControllerOperatingSystemRevision"),
        ("SITE-MONITORING-MIB", "siteV1DescControllerCPU"),
        ("SITE-MONITORING-MIB", "siteV1DescControllerCard"),
        ("SITE-MONITORING-MIB", "siteV1DescControllerStarterVersion"),
        ("SITE-MONITORING-MIB", "siteV1DescControllerFactoryCompasVersion"),
        ("SITE-MONITORING-MIB", "siteV1DescControllerUserCompasVersion"),
        ("SITE-MONITORING-MIB", "siteV1DescControllerFactoryFTPServerVersion"),
        ("SITE-MONITORING-MIB", "siteV1DescControllerUserFTPServerVersion"),
        ("SITE-MONITORING-MIB", "siteV1AlarmNumber"),
        ("SITE-MONITORING-MIB", "siteV1AlarmName"),
        ("SITE-MONITORING-MIB", "siteV1AlarmActive"),
        ("SITE-MONITORING-MIB", "siteV1AlarmSeverityType"),
        ("SITE-MONITORING-MIB", "siteV1AlarmSeverityLevel"),
        ("SITE-MONITORING-MIB", "siteV1AlarmStartTime"),
        ("SITE-MONITORING-MIB", "siteV1AlarmStopTime"),
        ("SITE-MONITORING-MIB", "siteV1AlarmEntryStatus"),
        ("SITE-MONITORING-MIB", "siteV1AlarmSummary"),
        ("SITE-MONITORING-MIB", "siteV1EventNumber"),
        ("SITE-MONITORING-MIB", "siteV1EventId"),
        ("SITE-MONITORING-MIB", "siteV1EventName"),
        ("SITE-MONITORING-MIB", "siteV1EventDateTime"),
        ("SITE-MONITORING-MIB", "siteV1EventSeverityType"),
        ("SITE-MONITORING-MIB", "siteV1EventSeverityLevel"),
        ("SITE-MONITORING-MIB", "siteV1EventEntryStatus"),
        ("SITE-MONITORING-MIB", "siteV1DataNumber"),
        ("SITE-MONITORING-MIB", "siteV1DataName"),
        ("SITE-MONITORING-MIB", "siteV1DataValue"),
        ("SITE-MONITORING-MIB", "siteV1DataEntryStatus"),
        ("SITE-MONITORING-MIB", "siteV1DataNetworkCurrentIPAddress"),
        ("SITE-MONITORING-MIB", "siteV1DataNetworkCurrentIPMask"),
        ("SITE-MONITORING-MIB", "siteV1DataNetworkCurrentMACAddress"),
        ("SITE-MONITORING-MIB", "siteV1DataControllerLicensedOptions"),
        ("SITE-MONITORING-MIB", "siteV1DataTimeDateAndTimeLocal"),
        ("SITE-MONITORING-MIB", "siteV1DataTimeDateAndTimeUTC"),
        ("SITE-MONITORING-MIB", "siteV1DataControllerMonitoringMemoryUsed"),
        ("SITE-MONITORING-MIB", "siteV1DataControllerCPUPercentageUsage"),
        ("SITE-MONITORING-MIB", "siteV1DataControllerFreeFlashMemorySpace"),
        ("SITE-MONITORING-MIB", "siteV1DataControllerFTPServerStatus"),
        ("SITE-MONITORING-MIB", "siteV1DataDataRecordsTotalFifoSizeOfSecondRecords"),
        ("SITE-MONITORING-MIB", "siteV1DataDataRecordsTotalFifoSizeOfMinuteRecords"),
        ("SITE-MONITORING-MIB", "siteV1DataDataRecordsTotalFifoSizeOfHourRecords"),
        ("SITE-MONITORING-MIB", "siteV1DataDataRecordsTotalFifoSizeOfDayRecords"),
        ("SITE-MONITORING-MIB", "siteV1DataInventoryCANBusNodeIDs"),
        ("SITE-MONITORING-MIB", "siteV1DataCloudLinkCloudLinkState"),
        ("SITE-MONITORING-MIB", "siteV1ConfigNumber"),
        ("SITE-MONITORING-MIB", "siteV1ConfigName"),
        ("SITE-MONITORING-MIB", "siteV1ConfigValue"),
        ("SITE-MONITORING-MIB", "siteV1ConfigEntryStatus"),
        ("SITE-MONITORING-MIB", "siteV1CfgNetworkDHCPEnabled"),
        ("SITE-MONITORING-MIB", "siteV1CfgNetworkIPAddressIfStatic"),
        ("SITE-MONITORING-MIB", "siteV1CfgNetworkSubnetMaskIfStatic"),
        ("SITE-MONITORING-MIB", "siteV1CfgNetworkDefaultGatewayIfStatic"),
        ("SITE-MONITORING-MIB", "siteV1CfgNetworkDNSIfStatic"),
        ("SITE-MONITORING-MIB", "siteV1CfgNetworkMaxTransmissionUnit"),
        ("SITE-MONITORING-MIB", "siteV1CfgTimeSNTPTimeServer"),
        ("SITE-MONITORING-MIB", "siteV1CfgTimeTimeZoneName"),
        ("SITE-MONITORING-MIB", "siteV1CfgTimeSNTPTimeRefresh"),
        ("SITE-MONITORING-MIB", "siteV1CfgTimeSNTPTimeRecoveryRefresh"),
        ("SITE-MONITORING-MIB", "siteV1CfgWebServerWebServerSecurityEnabled"),
        ("SITE-MONITORING-MIB", "siteV1CfgWebServerWebServerPort"),
        ("SITE-MONITORING-MIB", "siteV1CfgWebServerWebAuthenticationMethod"),
        ("SITE-MONITORING-MIB", "siteV1CfgWebServerHttpsWebServerPort"),
        ("SITE-MONITORING-MIB", "siteV1CfgWebServerDefaultPage"),
        ("SITE-MONITORING-MIB", "siteV1CfgXMLXMLEventPostingActivated"),
        ("SITE-MONITORING-MIB", "siteV1CfgXMLXMLEventPostingRefreshTime"),
        ("SITE-MONITORING-MIB", "siteV1CfgXMLXMLEventPostingTimeout"),
        ("SITE-MONITORING-MIB", "siteV1CfgXMLXMLEventPostingToSecOnlyIfPrimFail"),
        ("SITE-MONITORING-MIB", "siteV1CfgXMLXMLTablesToPostOnXMLEvent"),
        ("SITE-MONITORING-MIB", "siteV1CfgXMLXMLHeartbeatTime"),
        ("SITE-MONITORING-MIB", "siteV1CfgSNMPSNMPActivated"),
        ("SITE-MONITORING-MIB", "siteV1CfgSNMPSNMPTrapVersion"),
        ("SITE-MONITORING-MIB", "siteV1CfgSNMPSNMPGETMinSecurityLevel"),
        ("SITE-MONITORING-MIB", "siteV1CfgSNMPSNMPSETMinSecurityLevel"),
        ("SITE-MONITORING-MIB", "siteV1CfgSNMPSNMPV3AuthAlgorithm"),
        ("SITE-MONITORING-MIB", "siteV1CfgSNMPSNMPV3PrivacyAlgorithm"),
        ("SITE-MONITORING-MIB", "siteV1CfgSNMPSNMPV3PrivacyPassword"),
        ("SITE-MONITORING-MIB", "siteV1CfgSNMPSNMPV3EngineID"),
        ("SITE-MONITORING-MIB", "siteV1CfgSNMPSNMPV3TrapAuthAlgorithm"),
        ("SITE-MONITORING-MIB", "siteV1CfgSNMPSNMPV3TrapPrivacyAlgorithm"),
        ("SITE-MONITORING-MIB", "siteV1CfgSNMPSNMPV3TrapUsername"),
        ("SITE-MONITORING-MIB", "siteV1CfgSNMPSNMPV3TrapAuthPassword"),
        ("SITE-MONITORING-MIB", "siteV1CfgSNMPSNMPV3TrapPrivacyPassword"),
        ("SITE-MONITORING-MIB", "siteV1CfgSNMPSiteDescriptionIdsIncludedInTraps"),
        ("SITE-MONITORING-MIB", "siteV1CfgGenericGenerateEventOnConfChanges"),
        ("SITE-MONITORING-MIB", "siteV1CfgDataRecordsAutoArchivePeriodDataRecord"),
        ("SITE-MONITORING-MIB", "siteV1CfgGenericGenerateEventOnControlExecution"),
        ("SITE-MONITORING-MIB", "siteV1CfgGenericGenerateEventOnAlarmAcknowledge"),
        ("SITE-MONITORING-MIB", "siteV1CfgInventoryRequiredCANBusNodeIDs"),
        ("SITE-MONITORING-MIB", "siteV1CfgInventoryLSSCANidrange"),
        ("SITE-MONITORING-MIB", "siteV1CfgInventorySystemNodesDefinition"),
        ("SITE-MONITORING-MIB", "siteV1CfgInventoryLSSCANOpenSavedConf"),
        ("SITE-MONITORING-MIB", "siteV1CfgUsersAdministratorLoginPassword"),
        ("SITE-MONITORING-MIB", "siteV1CfgUsersUser1LoginPassword"),
        ("SITE-MONITORING-MIB", "siteV1CfgUsersUser2LoginPassword"),
        ("SITE-MONITORING-MIB", "siteV1CfgUsersUser3LoginPassword"),
        ("SITE-MONITORING-MIB", "siteV1CfgUsersUser4LoginPassword"),
        ("SITE-MONITORING-MIB", "siteV1CfgUsersUser5LoginPassword"),
        ("SITE-MONITORING-MIB", "siteV1CfgRadiusAuthenticationRadiusServer"),
        ("SITE-MONITORING-MIB", "siteV1CfgRadiusAuthenticationRadiusPort"),
        ("SITE-MONITORING-MIB", "siteV1CfgRadiusAuthenticationRadiusSecret"),
        ("SITE-MONITORING-MIB", "siteV1CfgEmailEnableEmailFeature"),
        ("SITE-MONITORING-MIB", "siteV1CfgEmailSmtpServer"),
        ("SITE-MONITORING-MIB", "siteV1CfgEmailSmtpDomain"),
        ("SITE-MONITORING-MIB", "siteV1CfgEmailSmtpUserLoginPassword"),
        ("SITE-MONITORING-MIB", "siteV1CfgEmailMailSender"),
        ("SITE-MONITORING-MIB", "siteV1CfgEmailMailRecipients"),
        ("SITE-MONITORING-MIB", "siteV1CfgEmailMinimalSeverityTypeToSendMail"),
        ("SITE-MONITORING-MIB", "siteV1CfgControllerAutomaticReboot"),
        ("SITE-MONITORING-MIB", "siteV1CfgCloudLinkCloudEnabled"),
        ("SITE-MONITORING-MIB", "siteV1CfgCloudLinkCloudServer"),
        ("SITE-MONITORING-MIB", "siteV1CfgCloudLinkCloudPort"),
        ("SITE-MONITORING-MIB", "siteV1CfgCloudLinkCloudCredential"),
        ("SITE-MONITORING-MIB", "siteV1CfgCloudLinkCloudCluster"),
        ("SITE-MONITORING-MIB", "siteV1CfgInventoryRS485ExtensionsConf"),
        ("SITE-MONITORING-MIB", "siteV1CfgInventoryEthernetExtensionsConf"),
        ("SITE-MONITORING-MIB", "siteV1CfgScriptingEnabledscripts"),
        ("SITE-MONITORING-MIB", "siteV1CfgScriptingNumberofErrorsbeforetriggeringalarm"),
        ("SITE-MONITORING-MIB", "siteV1CfgGenericReadAccessUserNumbers"),
        ("SITE-MONITORING-MIB", "siteV1CfgGenericWriteAccessUserNumbers"),
        ("SITE-MONITORING-MIB", "siteV1CfgGenericEventTableLength"),
        ("SITE-MONITORING-MIB", "siteV1CfgSNMPSNMPTrapTargetsIP"),
        ("SITE-MONITORING-MIB", "siteV1CfgSNMPMinimalEventSeverityForTraps"),
        ("SITE-MONITORING-MIB", "siteV1CfgXMLXMLEventsPrimPostURL"),
        ("SITE-MONITORING-MIB", "siteV1CfgXMLXMLEventsPrimPostLogin"),
        ("SITE-MONITORING-MIB", "siteV1CfgXMLXMLEventsPrimPostPassword"),
        ("SITE-MONITORING-MIB", "siteV1CfgXMLXMLEventsSecPostURL"),
        ("SITE-MONITORING-MIB", "siteV1CfgXMLXMLEventsSecPostLogin"),
        ("SITE-MONITORING-MIB", "siteV1CfgXMLXMLEventsSecPostPassword"),
        ("SITE-MONITORING-MIB", "siteV1CfgPLCNumberOfPLCData"),
        ("SITE-MONITORING-MIB", "siteV1CfgPLCNumberOfPLCAlarm"),
        ("SITE-MONITORING-MIB", "siteV1ControlNumber"),
        ("SITE-MONITORING-MIB", "siteV1ControlName"),
        ("SITE-MONITORING-MIB", "siteV1ControlValue"),
        ("SITE-MONITORING-MIB", "siteV1ControlEntryStatus"),
        ("SITE-MONITORING-MIB", "siteV1CtrlControllerRebootController"),
        ("SITE-MONITORING-MIB", "siteV1CtrlControllerSaveConfAndRebootController"),
        ("SITE-MONITORING-MIB", "siteV1CtrlControllerRebootControllerWithoutSavingRecords"),
        ("SITE-MONITORING-MIB", "siteV1CtrlNetworkApplyNetworkConf"),
        ("SITE-MONITORING-MIB", "siteV1CtrlTimeForceSNTPTimeRefresh"),
        ("SITE-MONITORING-MIB", "siteV1CtrlTimeSetLocalTime"),
        ("SITE-MONITORING-MIB", "siteV1CtrlTimeSetUTCTime"),
        ("SITE-MONITORING-MIB", "siteV1CtrlTimeResetUptime"),
        ("SITE-MONITORING-MIB", "siteV1CtrlControllerCleanandSaveXMLUserConf"),
        ("SITE-MONITORING-MIB", "siteV1CtrlControllerSaveXMLUserConf"),
        ("SITE-MONITORING-MIB", "siteV1CtrlControllerSaveInventory"),
        ("SITE-MONITORING-MIB", "siteV1CtrlDataRecordsSaveDataRecords"),
        ("SITE-MONITORING-MIB", "siteV1CtrlDataRecordsExportDataRecordsinCSV"),
        ("SITE-MONITORING-MIB", "siteV1CtrlDataRecordsArchiveDataRecords"),
        ("SITE-MONITORING-MIB", "siteV1CtrlDataRecordsDeleteAllDataRecords"),
        ("SITE-MONITORING-MIB", "siteV1CtrlControllerEmulateRecords"),
        ("SITE-MONITORING-MIB", "siteV1CtrlControllerReloadTranslations"),
        ("SITE-MONITORING-MIB", "siteV1CtrlControllerReloadLicense"),
        ("SITE-MONITORING-MIB", "siteV1CtrlControllerManageFTPServer"),
        ("SITE-MONITORING-MIB", "siteV1CtrlInventoryRemoveAbsentEquipments"),
        ("SITE-MONITORING-MIB", "siteV1CtrlInventoryResetCANBusNode"),
        ("SITE-MONITORING-MIB", "siteV1CtrlInventorySaveCANOpenLSSConf"),
        ("SITE-MONITORING-MIB", "siteV1CtrlInventoryStartNewInventory"),
        ("SITE-MONITORING-MIB", "siteV1CtrlInventoryUpgradeNodeFirmware"),
        ("SITE-MONITORING-MIB", "siteV1CtrlInventoryCancelFirmwareUpgrade"),
        ("SITE-MONITORING-MIB", "siteV1CtrlFilesFlashBinary"),
        ("SITE-MONITORING-MIB", "siteV1CtrlFilesDownloadFileFromUrl"),
        ("SITE-MONITORING-MIB", "siteV1CtrlFilesDeleteUserUploadedFile"),
        ("SITE-MONITORING-MIB", "siteV1CtrlFilesMoveUserUploadedFile"),
        ("SITE-MONITORING-MIB", "siteV1CtrlFilesExtractZipFileinuserupload"),
        ("SITE-MONITORING-MIB", "siteV1CtrlEmailSendSummaryEmail"),
        ("SITE-MONITORING-MIB", "siteV1CtrlScriptingControlLuaScript"),
        ("SITE-MONITORING-MIB", "siteV1CtrlControllerAdvancedFunctionGenericCommandExecution"),
        ("SITE-MONITORING-MIB", "siteV1CtrlGenericClearMyEvents"),
        ("SITE-MONITORING-MIB", "siteV1CtrlGenericClearAllEvents"),
        ("SITE-MONITORING-MIB", "siteV1CtrlGenericAddEvent"),
        ("SITE-MONITORING-MIB", "siteV1CtrlGenericAddMajorEvent"),
        ("SITE-MONITORING-MIB", "siteV1CtrlGenericResetDefaultNamesAndGroups"),
        ("SITE-MONITORING-MIB", "siteV1CtrlGenericResetDefaultNamesAndGroupsRecursive"))
)
if mibBuilder.loadTexts:
    siteV1GlobalGroup.setStatus("current")

es1GlobalGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 26854, 3, 2, 1, 20, 1, 19, 1, 1)
)
es1GlobalGroup.setObjects(
      *(("SITE-MONITORING-MIB", "es1GlobalStatus"),
        ("SITE-MONITORING-MIB", "es1GlobalAlarmSeverityType"),
        ("SITE-MONITORING-MIB", "es1GlobalAlarmSeverityLevel"),
        ("SITE-MONITORING-MIB", "es1GlobalAlarmSeverityTypeInt"),
        ("SITE-MONITORING-MIB", "es1DescriptionNumber"),
        ("SITE-MONITORING-MIB", "es1DescriptionName"),
        ("SITE-MONITORING-MIB", "es1DescriptionValue"),
        ("SITE-MONITORING-MIB", "es1DescriptionEntryStatus"),
        ("SITE-MONITORING-MIB", "es1DescDescriptionDescription"),
        ("SITE-MONITORING-MIB", "es1DescDescriptionReference"),
        ("SITE-MONITORING-MIB", "es1AlarmNumber"),
        ("SITE-MONITORING-MIB", "es1AlarmName"),
        ("SITE-MONITORING-MIB", "es1AlarmActive"),
        ("SITE-MONITORING-MIB", "es1AlarmSeverityType"),
        ("SITE-MONITORING-MIB", "es1AlarmSeverityLevel"),
        ("SITE-MONITORING-MIB", "es1AlarmStartTime"),
        ("SITE-MONITORING-MIB", "es1AlarmStopTime"),
        ("SITE-MONITORING-MIB", "es1AlarmEntryStatus"),
        ("SITE-MONITORING-MIB", "es1AlarmSummary"),
        ("SITE-MONITORING-MIB", "es1EventNumber"),
        ("SITE-MONITORING-MIB", "es1EventId"),
        ("SITE-MONITORING-MIB", "es1EventName"),
        ("SITE-MONITORING-MIB", "es1EventDateTime"),
        ("SITE-MONITORING-MIB", "es1EventSeverityType"),
        ("SITE-MONITORING-MIB", "es1EventSeverityLevel"),
        ("SITE-MONITORING-MIB", "es1EventEntryStatus"),
        ("SITE-MONITORING-MIB", "es1DataNumber"),
        ("SITE-MONITORING-MIB", "es1ConfigNumber"),
        ("SITE-MONITORING-MIB", "es1ConfigName"),
        ("SITE-MONITORING-MIB", "es1ConfigValue"),
        ("SITE-MONITORING-MIB", "es1ConfigEntryStatus"),
        ("SITE-MONITORING-MIB", "es1CfgEnergyMeterNumberOfGenericPulseEnergyCounter"),
        ("SITE-MONITORING-MIB", "es1ControlNumber"),
        ("SITE-MONITORING-MIB", "es1ControlName"),
        ("SITE-MONITORING-MIB", "es1ControlValue"),
        ("SITE-MONITORING-MIB", "es1ControlEntryStatus"),
        ("SITE-MONITORING-MIB", "es1CtrlGenericClearMyEvents"),
        ("SITE-MONITORING-MIB", "es1CtrlGenericClearAllEvents"),
        ("SITE-MONITORING-MIB", "es1CtrlGenericAddEvent"),
        ("SITE-MONITORING-MIB", "es1CtrlGenericAddMajorEvent"),
        ("SITE-MONITORING-MIB", "es1CtrlGenericResetDefaultNamesAndGroups"),
        ("SITE-MONITORING-MIB", "es1CtrlGenericResetDefaultNamesAndGroupsRecursive"))
)
if mibBuilder.loadTexts:
    es1GlobalGroup.setStatus("current")

es1dc1GlobalGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 26854, 3, 2, 1, 20, 1, 20, 1, 19, 1, 1)
)
es1dc1GlobalGroup.setObjects(
      *(("SITE-MONITORING-MIB", "es1dc1GlobalStatus"),
        ("SITE-MONITORING-MIB", "es1dc1GlobalAlarmSeverityType"),
        ("SITE-MONITORING-MIB", "es1dc1GlobalAlarmSeverityLevel"),
        ("SITE-MONITORING-MIB", "es1dc1GlobalAlarmSeverityTypeInt"),
        ("SITE-MONITORING-MIB", "es1dc1DescriptionNumber"),
        ("SITE-MONITORING-MIB", "es1dc1DescriptionName"),
        ("SITE-MONITORING-MIB", "es1dc1DescriptionValue"),
        ("SITE-MONITORING-MIB", "es1dc1DescriptionEntryStatus"),
        ("SITE-MONITORING-MIB", "es1dc1DescDescriptionDescription"),
        ("SITE-MONITORING-MIB", "es1dc1DescDescriptionReference"),
        ("SITE-MONITORING-MIB", "es1dc1DescDescriptionProductName"),
        ("SITE-MONITORING-MIB", "es1dc1DescDescriptionHardwareReference"),
        ("SITE-MONITORING-MIB", "es1dc1DescDescriptionSoftwareReference"),
        ("SITE-MONITORING-MIB", "es1dc1DescDescriptionSerialNumber"),
        ("SITE-MONITORING-MIB", "es1dc1DescDescriptionManufacturingDate"),
        ("SITE-MONITORING-MIB", "es1dc1DescDescriptionDistributionModuleProductName"),
        ("SITE-MONITORING-MIB", "es1dc1DescDescriptionDistributionModuleHardwareReference"),
        ("SITE-MONITORING-MIB", "es1dc1DescDescriptionDistributionModuleSoftwareReference"),
        ("SITE-MONITORING-MIB", "es1dc1DescDescriptionDistributionModuleSerialNumber"),
        ("SITE-MONITORING-MIB", "es1dc1DescDescriptionDistributionModuleManufacturingDate"),
        ("SITE-MONITORING-MIB", "es1dc1AlarmNumber"),
        ("SITE-MONITORING-MIB", "es1dc1AlarmName"),
        ("SITE-MONITORING-MIB", "es1dc1AlarmActive"),
        ("SITE-MONITORING-MIB", "es1dc1AlarmSeverityType"),
        ("SITE-MONITORING-MIB", "es1dc1AlarmSeverityLevel"),
        ("SITE-MONITORING-MIB", "es1dc1AlarmStartTime"),
        ("SITE-MONITORING-MIB", "es1dc1AlarmStopTime"),
        ("SITE-MONITORING-MIB", "es1dc1AlarmEntryStatus"),
        ("SITE-MONITORING-MIB", "es1dc1AlarmSummary"),
        ("SITE-MONITORING-MIB", "es1dc1EventNumber"),
        ("SITE-MONITORING-MIB", "es1dc1EventId"),
        ("SITE-MONITORING-MIB", "es1dc1EventName"),
        ("SITE-MONITORING-MIB", "es1dc1EventDateTime"),
        ("SITE-MONITORING-MIB", "es1dc1EventSeverityType"),
        ("SITE-MONITORING-MIB", "es1dc1EventSeverityLevel"),
        ("SITE-MONITORING-MIB", "es1dc1EventEntryStatus"),
        ("SITE-MONITORING-MIB", "es1dc1DataNumber"),
        ("SITE-MONITORING-MIB", "es1dc1DataName"),
        ("SITE-MONITORING-MIB", "es1dc1DataValue"),
        ("SITE-MONITORING-MIB", "es1dc1DataEntryStatus"),
        ("SITE-MONITORING-MIB", "es1dc1DataSystemDCMode"),
        ("SITE-MONITORING-MIB", "es1dc1DataSystemPreviousDCMode"),
        ("SITE-MONITORING-MIB", "es1dc1DataSystemNiMHChargeMode"),
        ("SITE-MONITORING-MIB", "es1dc1DataDCBusBusVoltage"),
        ("SITE-MONITORING-MIB", "es1dc1DataSystemRatioDeliveredOnAvailablePower"),
        ("SITE-MONITORING-MIB", "es1dc1DataACBusMinutesSinceLastACFailBegin"),
        ("SITE-MONITORING-MIB", "es1dc1DataACBusMinutesSinceLastACFailEnd"),
        ("SITE-MONITORING-MIB", "es1dc1DataRectifiersRectifiersOutPower"),
        ("SITE-MONITORING-MIB", "es1dc1DataRectifiersRectifiersOutCurrent"),
        ("SITE-MONITORING-MIB", "es1dc1DataRectifiersRectifiersOutPowerMax"),
        ("SITE-MONITORING-MIB", "es1dc1DataRectifiersRectifiersOutCurrentMax"),
        ("SITE-MONITORING-MIB", "es1dc1DataRectifiersNumberOfRectifierMax"),
        ("SITE-MONITORING-MIB", "es1dc1DataRectifiersNumberOfPresentRectifier"),
        ("SITE-MONITORING-MIB", "es1dc1DataRectifiersNumberOfAbsentRectifier"),
        ("SITE-MONITORING-MIB", "es1dc1DataRectifiersNumberOfActiveRectifier"),
        ("SITE-MONITORING-MIB", "es1dc1DataRectifiersNumberOfACFailRectifier"),
        ("SITE-MONITORING-MIB", "es1dc1DataRectifiersNumberOfDCFailRectifier"),
        ("SITE-MONITORING-MIB", "es1dc1DataRectifiersNumberOfRemoteOffRectifier"),
        ("SITE-MONITORING-MIB", "es1dc1DataRectifiersNumberOfOverTempRectifier"),
        ("SITE-MONITORING-MIB", "es1dc1DataLoadLoadPower"),
        ("SITE-MONITORING-MIB", "es1dc1DataLoadLoadCurrent"),
        ("SITE-MONITORING-MIB", "es1dc1DataBatBatInputCurrent"),
        ("SITE-MONITORING-MIB", "es1dc1DataBatBatInputPower"),
        ("SITE-MONITORING-MIB", "es1dc1DataBatBatTemp"),
        ("SITE-MONITORING-MIB", "es1dc1DataBatBatTestState"),
        ("SITE-MONITORING-MIB", "es1dc1DataBatLastBatTestDischargedCapacityRatio"),
        ("SITE-MONITORING-MIB", "es1dc1DataBatLastBatTestDischargedCapacity"),
        ("SITE-MONITORING-MIB", "es1dc1DataBatLastBatTestFinalVoltage"),
        ("SITE-MONITORING-MIB", "es1dc1DataBatBatTestDuration"),
        ("SITE-MONITORING-MIB", "es1dc1DataBatPreviousBatTestDischargedCapacityRatio"),
        ("SITE-MONITORING-MIB", "es1dc1DataBatPreviousBatTestDischargedCapacity"),
        ("SITE-MONITORING-MIB", "es1dc1DataBatPreviousBatTestFinalVoltage"),
        ("SITE-MONITORING-MIB", "es1dc1DataBatPreviousBatTestDuration"),
        ("SITE-MONITORING-MIB", "es1dc1DataBatPreviousBatTestState"),
        ("SITE-MONITORING-MIB", "es1dc1DataBatMinutesSinceLastTestBat"),
        ("SITE-MONITORING-MIB", "es1dc1DataBatNextScheduledBatTest"),
        ("SITE-MONITORING-MIB", "es1dc1DataBatBatChargeCapacity"),
        ("SITE-MONITORING-MIB", "es1dc1DataBatCalculatedAutonomy"),
        ("SITE-MONITORING-MIB", "es1dc1DataBatBatCurrentIntegration"),
        ("SITE-MONITORING-MIB", "es1dc1DataLVDLVDState"),
        ("SITE-MONITORING-MIB", "es1dc1DataRelsRel1State"),
        ("SITE-MONITORING-MIB", "es1dc1DataRelsRel2State"),
        ("SITE-MONITORING-MIB", "es1dc1DataRelsRel3State"),
        ("SITE-MONITORING-MIB", "es1dc1DataRelsRel4State"),
        ("SITE-MONITORING-MIB", "es1dc1DataSmartEnergyEfficiencyOptimizedNumberOfRectifier"),
        ("SITE-MONITORING-MIB", "es1dc1DataSmartEnergySystemLossWithoutOptimisation"),
        ("SITE-MONITORING-MIB", "es1dc1DataSmartEnergySystemLossWithOptimisation"),
        ("SITE-MONITORING-MIB", "es1dc1DataSmartEnergyRectifierModelUsedForCalculation"),
        ("SITE-MONITORING-MIB", "es1dc1DataSmartEnergySmartEnergySavings"),
        ("SITE-MONITORING-MIB", "es1dc1DataSensorsAmbientTemp"),
        ("SITE-MONITORING-MIB", "es1dc1DataSensorsPulseCounter4"),
        ("SITE-MONITORING-MIB", "es1dc1ConfigNumber"),
        ("SITE-MONITORING-MIB", "es1dc1ConfigName"),
        ("SITE-MONITORING-MIB", "es1dc1ConfigValue"),
        ("SITE-MONITORING-MIB", "es1dc1ConfigEntryStatus"),
        ("SITE-MONITORING-MIB", "es1dc1CfgDCBusDCBusFloatVoltageat25degC"),
        ("SITE-MONITORING-MIB", "es1dc1CfgDCBusDCBusVoltageExtraLow"),
        ("SITE-MONITORING-MIB", "es1dc1CfgDCBusDCBusVoltageExtraLowHysteresis"),
        ("SITE-MONITORING-MIB", "es1dc1CfgDCBusDCBusVoltageLow"),
        ("SITE-MONITORING-MIB", "es1dc1CfgDCBusDCBusVoltageLowHysteresis"),
        ("SITE-MONITORING-MIB", "es1dc1CfgDCBusDCBusVoltageHigh"),
        ("SITE-MONITORING-MIB", "es1dc1CfgDCBusDCBusVoltageHighHysteresis"),
        ("SITE-MONITORING-MIB", "es1dc1CfgDCBusDCBusVoltageExtraHigh"),
        ("SITE-MONITORING-MIB", "es1dc1CfgDCBusDCBusVoltageExtraHighHysteresis"),
        ("SITE-MONITORING-MIB", "es1dc1CfgLVDLVDDisconnectVoltage"),
        ("SITE-MONITORING-MIB", "es1dc1CfgLVDLVDDisconnectDelay"),
        ("SITE-MONITORING-MIB", "es1dc1CfgBatTempCompensationSlope"),
        ("SITE-MONITORING-MIB", "es1dc1CfgBatMaxPosTempCompensation"),
        ("SITE-MONITORING-MIB", "es1dc1CfgBatMaxNegTempCompensation"),
        ("SITE-MONITORING-MIB", "es1dc1CfgRectifiersMinimalNumberOfPresentRectifiers"),
        ("SITE-MONITORING-MIB", "es1dc1CfgRectifiersRectifierModel"),
        ("SITE-MONITORING-MIB", "es1dc1CfgRectifiersForcedRemoteOffRectifers"),
        ("SITE-MONITORING-MIB", "es1dc1CfgBatBatChargeCurrentLimit"),
        ("SITE-MONITORING-MIB", "es1dc1CfgBatBatStringCapacity"),
        ("SITE-MONITORING-MIB", "es1dc1CfgBatBatTempLow"),
        ("SITE-MONITORING-MIB", "es1dc1CfgBatBatTempHigh"),
        ("SITE-MONITORING-MIB", "es1dc1CfgBatBatTempHysteresis"),
        ("SITE-MONITORING-MIB", "es1dc1CfgBatMinimalCurrentForDischargingAlarm"),
        ("SITE-MONITORING-MIB", "es1dc1CfgBatCurrentHysteresisForDischargingAlarm"),
        ("SITE-MONITORING-MIB", "es1dc1CfgBatPeukertNumber"),
        ("SITE-MONITORING-MIB", "es1dc1CfgBatMaxDepthOfDischargeforAutonomyEstimation"),
        ("SITE-MONITORING-MIB", "es1dc1CfgBatBoostAutomatic"),
        ("SITE-MONITORING-MIB", "es1dc1CfgBatBoostActivationLowVoltage"),
        ("SITE-MONITORING-MIB", "es1dc1CfgBatBoostTerminationVoltage"),
        ("SITE-MONITORING-MIB", "es1dc1CfgBatBoostTerminationCurrent"),
        ("SITE-MONITORING-MIB", "es1dc1CfgBatBoostTerminationTime"),
        ("SITE-MONITORING-MIB", "es1dc1CfgBatBatTestType"),
        ("SITE-MONITORING-MIB", "es1dc1CfgBatBatTestEndVoltage"),
        ("SITE-MONITORING-MIB", "es1dc1CfgBatBatTestDischargeRatio"),
        ("SITE-MONITORING-MIB", "es1dc1CfgBatBatTestInterval"),
        ("SITE-MONITORING-MIB", "es1dc1CfgBatBatTestDischargeCurrent"),
        ("SITE-MONITORING-MIB", "es1dc1CfgBatBatTestMinimalDischargeCurrent"),
        ("SITE-MONITORING-MIB", "es1dc1CfgBatBatTestDuration"),
        ("SITE-MONITORING-MIB", "es1dc1CfgBatBatTestRequMinutesWithoutMainsFail"),
        ("SITE-MONITORING-MIB", "es1dc1CfgBatBatTestSchedulerCronRule"),
        ("SITE-MONITORING-MIB", "es1dc1CfgSmartEnergySmartEnergyBooleanCond"),
        ("SITE-MONITORING-MIB", "es1dc1CfgLVDBatLVDNodeId"),
        ("SITE-MONITORING-MIB", "es1dc1CfgDigInputsDigInput1Name"),
        ("SITE-MONITORING-MIB", "es1dc1CfgDigInputsDigInput1NormallyClosed"),
        ("SITE-MONITORING-MIB", "es1dc1CfgDigInputsDigInput2Name"),
        ("SITE-MONITORING-MIB", "es1dc1CfgDigInputsDigInput2NormallyClosed"),
        ("SITE-MONITORING-MIB", "es1dc1CfgDigInputsDigInput3Name"),
        ("SITE-MONITORING-MIB", "es1dc1CfgDigInputsDigInput3NormallyClosed"),
        ("SITE-MONITORING-MIB", "es1dc1CfgDigInputsDigInput4Name"),
        ("SITE-MONITORING-MIB", "es1dc1CfgDigInputsDigInput4NormallyClosed"),
        ("SITE-MONITORING-MIB", "es1dc1CfgDigInputsDigInput5Name"),
        ("SITE-MONITORING-MIB", "es1dc1CfgDigInputsDigInput5NormallyClosed"),
        ("SITE-MONITORING-MIB", "es1dc1CfgDigInputsDigInput6Name"),
        ("SITE-MONITORING-MIB", "es1dc1CfgDigInputsDigInput6NormallyClosed"),
        ("SITE-MONITORING-MIB", "es1dc1CfgRelsDryAlarm1AlternativeBooleanCond"),
        ("SITE-MONITORING-MIB", "es1dc1CfgRelsDryAlarm2AlternativeBooleanCond"),
        ("SITE-MONITORING-MIB", "es1dc1CfgRelsDryAlarm3AlternativeBooleanCond"),
        ("SITE-MONITORING-MIB", "es1dc1CfgRelsDryAlarm4AlternativeBooleanCond"),
        ("SITE-MONITORING-MIB", "es1dc1CfgSensorsAmbientTempLow"),
        ("SITE-MONITORING-MIB", "es1dc1CfgSensorsAmbientTempHigh"),
        ("SITE-MONITORING-MIB", "es1dc1CfgSensorsAmbientTempHysteresis"),
        ("SITE-MONITORING-MIB", "es1dc1CfgGenericReadAccessUserNumbers"),
        ("SITE-MONITORING-MIB", "es1dc1CfgGenericWriteAccessUserNumbers"),
        ("SITE-MONITORING-MIB", "es1dc1CfgGenericEventTableLength"),
        ("SITE-MONITORING-MIB", "es1dc1CfgGenericEventTableLengthByRectifier"),
        ("SITE-MONITORING-MIB", "es1dc1CfgPLCNumberOfPLCData"),
        ("SITE-MONITORING-MIB", "es1dc1CfgPLCNumberOfPLCAlarm"),
        ("SITE-MONITORING-MIB", "es1dc1ControlNumber"),
        ("SITE-MONITORING-MIB", "es1dc1ControlName"),
        ("SITE-MONITORING-MIB", "es1dc1ControlValue"),
        ("SITE-MONITORING-MIB", "es1dc1ControlEntryStatus"),
        ("SITE-MONITORING-MIB", "es1dc1CtrlSystemBackToFloat"),
        ("SITE-MONITORING-MIB", "es1dc1CtrlSystemStartBatTest"),
        ("SITE-MONITORING-MIB", "es1dc1CtrlSystemForceBatTest"),
        ("SITE-MONITORING-MIB", "es1dc1CtrlSystemStartBoostMode"),
        ("SITE-MONITORING-MIB", "es1dc1CtrlLVDOpenTheLVD"),
        ("SITE-MONITORING-MIB", "es1dc1CtrlLVDCloseTheLVD"),
        ("SITE-MONITORING-MIB", "es1dc1CtrlBatCorrectBatCurrentOffset"),
        ("SITE-MONITORING-MIB", "es1dc1CtrlBatResetLastBatTestState"),
        ("SITE-MONITORING-MIB", "es1dc1CtrlSaveSaveConfInMCU"),
        ("SITE-MONITORING-MIB", "es1dc1CtrlAdvancedSetMCUSpecificConfId"),
        ("SITE-MONITORING-MIB", "es1dc1CtrlDigInputsSetDigInput4CounterValue"),
        ("SITE-MONITORING-MIB", "es1dc1CtrlRelsInvertRel1StateForXSeconds"),
        ("SITE-MONITORING-MIB", "es1dc1CtrlRelsInvertRel2StateForXSeconds"),
        ("SITE-MONITORING-MIB", "es1dc1CtrlRelsInvertRel3StateForXSeconds"),
        ("SITE-MONITORING-MIB", "es1dc1CtrlRelsInvertRel4StateForXSeconds"),
        ("SITE-MONITORING-MIB", "es1dc1CtrlGenericClearMyEvents"),
        ("SITE-MONITORING-MIB", "es1dc1CtrlGenericClearAllEvents"),
        ("SITE-MONITORING-MIB", "es1dc1CtrlGenericAddEvent"),
        ("SITE-MONITORING-MIB", "es1dc1CtrlGenericAddMajorEvent"),
        ("SITE-MONITORING-MIB", "es1dc1CtrlGenericResetDefaultNamesAndGroups"),
        ("SITE-MONITORING-MIB", "es1dc1CtrlGenericResetDefaultNamesAndGroupsRecursive"))
)
if mibBuilder.loadTexts:
    es1dc1GlobalGroup.setStatus("current")


# Notification objects

siteV1NotificationOfEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 26854, 3, 2, 1, 18, 0, 1)
)
siteV1NotificationOfEvent.setObjects(
      *(("SITE-MONITORING-MIB", "siteV1EventId"),
        ("SITE-MONITORING-MIB", "siteV1EventName"),
        ("SITE-MONITORING-MIB", "siteV1EventDateTime"),
        ("SITE-MONITORING-MIB", "siteV1EventSeverityType"),
        ("SITE-MONITORING-MIB", "siteV1EventSeverityLevel"),
        ("SITE-MONITORING-MIB", "siteV1AlarmSummary"))
)
if mibBuilder.loadTexts:
    siteV1NotificationOfEvent.setStatus(
        "current"
    )

es1NotificationOfEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 26854, 3, 2, 1, 20, 1, 18, 0, 1)
)
es1NotificationOfEvent.setObjects(
      *(("SITE-MONITORING-MIB", "es1EventId"),
        ("SITE-MONITORING-MIB", "es1EventName"),
        ("SITE-MONITORING-MIB", "es1EventDateTime"),
        ("SITE-MONITORING-MIB", "es1EventSeverityType"),
        ("SITE-MONITORING-MIB", "es1EventSeverityLevel"),
        ("SITE-MONITORING-MIB", "es1AlarmSummary"))
)
if mibBuilder.loadTexts:
    es1NotificationOfEvent.setStatus(
        "current"
    )

es1dc1NotificationOfEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 26854, 3, 2, 1, 20, 1, 20, 1, 18, 0, 1)
)
es1dc1NotificationOfEvent.setObjects(
      *(("SITE-MONITORING-MIB", "es1dc1EventId"),
        ("SITE-MONITORING-MIB", "es1dc1EventName"),
        ("SITE-MONITORING-MIB", "es1dc1EventDateTime"),
        ("SITE-MONITORING-MIB", "es1dc1EventSeverityType"),
        ("SITE-MONITORING-MIB", "es1dc1EventSeverityLevel"),
        ("SITE-MONITORING-MIB", "es1dc1AlarmSummary"))
)
if mibBuilder.loadTexts:
    es1dc1NotificationOfEvent.setStatus(
        "current"
    )


# Notifications groups

siteV1NotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 26854, 3, 2, 1, 19, 1, 2)
)
siteV1NotificationGroup.setObjects(
    ("SITE-MONITORING-MIB", "siteV1NotificationOfEvent")
)
if mibBuilder.loadTexts:
    siteV1NotificationGroup.setStatus(
        "current"
    )

es1NotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 26854, 3, 2, 1, 20, 1, 19, 1, 2)
)
es1NotificationGroup.setObjects(
    ("SITE-MONITORING-MIB", "es1NotificationOfEvent")
)
if mibBuilder.loadTexts:
    es1NotificationGroup.setStatus(
        "current"
    )

es1dc1NotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 26854, 3, 2, 1, 20, 1, 20, 1, 19, 1, 2)
)
es1dc1NotificationGroup.setObjects(
    ("SITE-MONITORING-MIB", "es1dc1NotificationOfEvent")
)
if mibBuilder.loadTexts:
    es1dc1NotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

siteV1FullCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 26854, 3, 2, 1, 19, 2)
)
siteV1FullCompliance.setObjects(
      *(("SITE-MONITORING-MIB", "siteV1GlobalGroup"),
        ("SITE-MONITORING-MIB", "siteV1NotificationGroup"))
)
if mibBuilder.loadTexts:
    siteV1FullCompliance.setStatus(
        "current"
    )

es1FullCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 26854, 3, 2, 1, 20, 1, 19, 2)
)
es1FullCompliance.setObjects(
      *(("SITE-MONITORING-MIB", "es1GlobalGroup"),
        ("SITE-MONITORING-MIB", "es1NotificationGroup"))
)
if mibBuilder.loadTexts:
    es1FullCompliance.setStatus(
        "current"
    )

es1dc1FullCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 26854, 3, 2, 1, 20, 1, 20, 1, 19, 2)
)
es1dc1FullCompliance.setObjects(
      *(("SITE-MONITORING-MIB", "es1dc1GlobalGroup"),
        ("SITE-MONITORING-MIB", "es1dc1NotificationGroup"))
)
if mibBuilder.loadTexts:
    es1dc1FullCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SITE-MONITORING-MIB",
    **{"atsa": atsa,
       "atsaCorporate": atsaCorporate,
       "siteMonitoringMIB": siteMonitoringMIB,
       "atsaUs": atsaUs,
       "atsaEu": atsaEu,
       "atsaEuDevices": atsaEuDevices,
       "siteMonitoring": siteMonitoring,
       "siteV1": siteV1,
       "siteV1GlobalStatus": siteV1GlobalStatus,
       "siteV1GlobalAlarmSeverityType": siteV1GlobalAlarmSeverityType,
       "siteV1GlobalAlarmSeverityLevel": siteV1GlobalAlarmSeverityLevel,
       "siteV1GlobalAlarmSeverityTypeInt": siteV1GlobalAlarmSeverityTypeInt,
       "siteV1Description": siteV1Description,
       "siteV1DescriptionNumber": siteV1DescriptionNumber,
       "siteV1DescriptionTable": siteV1DescriptionTable,
       "siteV1DescriptionEntry": siteV1DescriptionEntry,
       "siteV1DescriptionIndex": siteV1DescriptionIndex,
       "siteV1DescriptionName": siteV1DescriptionName,
       "siteV1DescriptionValue": siteV1DescriptionValue,
       "siteV1DescriptionEntryStatus": siteV1DescriptionEntryStatus,
       "siteV1DescriptionList": siteV1DescriptionList,
       "siteV1DescDescriptionSiteNumber": siteV1DescDescriptionSiteNumber,
       "siteV1DescDescriptionSiteName": siteV1DescDescriptionSiteName,
       "siteV1DescDescriptionShortDescription": siteV1DescDescriptionShortDescription,
       "siteV1DescDescriptionInfo": siteV1DescDescriptionInfo,
       "siteV1DescDescriptionDescription": siteV1DescDescriptionDescription,
       "siteV1DescDescriptionReference": siteV1DescDescriptionReference,
       "siteV1DescDescriptionContactName": siteV1DescDescriptionContactName,
       "siteV1DescDescriptionPhoneNumber": siteV1DescDescriptionPhoneNumber,
       "siteV1DescDescriptionStreet": siteV1DescDescriptionStreet,
       "siteV1DescDescriptionCity": siteV1DescDescriptionCity,
       "siteV1DescDescriptionProvince": siteV1DescDescriptionProvince,
       "siteV1DescDescriptionPostalCode": siteV1DescDescriptionPostalCode,
       "siteV1DescDescriptionRegion": siteV1DescDescriptionRegion,
       "siteV1DescDescriptionCountry": siteV1DescDescriptionCountry,
       "siteV1DescDescriptionGroup1": siteV1DescDescriptionGroup1,
       "siteV1DescDescriptionGroup2": siteV1DescDescriptionGroup2,
       "siteV1DescDescriptionGroup3": siteV1DescDescriptionGroup3,
       "siteV1DescDescriptionGroup4": siteV1DescDescriptionGroup4,
       "siteV1DescDescriptionGroup5": siteV1DescDescriptionGroup5,
       "siteV1DescDescriptionLatitude": siteV1DescDescriptionLatitude,
       "siteV1DescDescriptionLongitude": siteV1DescDescriptionLongitude,
       "siteV1DescDescriptionAltitude": siteV1DescDescriptionAltitude,
       "siteV1DescControllerSoftwareRevision": siteV1DescControllerSoftwareRevision,
       "siteV1DescControllerOperatingSystemRevision": siteV1DescControllerOperatingSystemRevision,
       "siteV1DescControllerCPU": siteV1DescControllerCPU,
       "siteV1DescControllerCard": siteV1DescControllerCard,
       "siteV1DescControllerStarterVersion": siteV1DescControllerStarterVersion,
       "siteV1DescControllerFactoryCompasVersion": siteV1DescControllerFactoryCompasVersion,
       "siteV1DescControllerUserCompasVersion": siteV1DescControllerUserCompasVersion,
       "siteV1DescControllerFactoryFTPServerVersion": siteV1DescControllerFactoryFTPServerVersion,
       "siteV1DescControllerUserFTPServerVersion": siteV1DescControllerUserFTPServerVersion,
       "siteV1Alarm": siteV1Alarm,
       "siteV1AlarmNumber": siteV1AlarmNumber,
       "siteV1AlarmTable": siteV1AlarmTable,
       "siteV1AlarmEntry": siteV1AlarmEntry,
       "siteV1AlarmIndex": siteV1AlarmIndex,
       "siteV1AlarmName": siteV1AlarmName,
       "siteV1AlarmActive": siteV1AlarmActive,
       "siteV1AlarmSeverityType": siteV1AlarmSeverityType,
       "siteV1AlarmSeverityLevel": siteV1AlarmSeverityLevel,
       "siteV1AlarmStartTime": siteV1AlarmStartTime,
       "siteV1AlarmStopTime": siteV1AlarmStopTime,
       "siteV1AlarmEntryStatus": siteV1AlarmEntryStatus,
       "siteV1AlarmSummary": siteV1AlarmSummary,
       "siteV1Event": siteV1Event,
       "siteV1EventNumber": siteV1EventNumber,
       "siteV1EventTable": siteV1EventTable,
       "siteV1EventEntry": siteV1EventEntry,
       "siteV1EventIndex": siteV1EventIndex,
       "siteV1EventId": siteV1EventId,
       "siteV1EventName": siteV1EventName,
       "siteV1EventDateTime": siteV1EventDateTime,
       "siteV1EventSeverityType": siteV1EventSeverityType,
       "siteV1EventSeverityLevel": siteV1EventSeverityLevel,
       "siteV1EventEntryStatus": siteV1EventEntryStatus,
       "siteV1Data": siteV1Data,
       "siteV1DataNumber": siteV1DataNumber,
       "siteV1DataTable": siteV1DataTable,
       "siteV1DataEntry": siteV1DataEntry,
       "siteV1DataIndex": siteV1DataIndex,
       "siteV1DataName": siteV1DataName,
       "siteV1DataValue": siteV1DataValue,
       "siteV1DataEntryStatus": siteV1DataEntryStatus,
       "siteV1DataList": siteV1DataList,
       "siteV1DataNetworkCurrentIPAddress": siteV1DataNetworkCurrentIPAddress,
       "siteV1DataNetworkCurrentIPMask": siteV1DataNetworkCurrentIPMask,
       "siteV1DataNetworkCurrentMACAddress": siteV1DataNetworkCurrentMACAddress,
       "siteV1DataControllerLicensedOptions": siteV1DataControllerLicensedOptions,
       "siteV1DataTimeDateAndTimeLocal": siteV1DataTimeDateAndTimeLocal,
       "siteV1DataTimeDateAndTimeUTC": siteV1DataTimeDateAndTimeUTC,
       "siteV1DataControllerMonitoringMemoryUsed": siteV1DataControllerMonitoringMemoryUsed,
       "siteV1DataControllerCPUPercentageUsage": siteV1DataControllerCPUPercentageUsage,
       "siteV1DataControllerFreeFlashMemorySpace": siteV1DataControllerFreeFlashMemorySpace,
       "siteV1DataControllerFTPServerStatus": siteV1DataControllerFTPServerStatus,
       "siteV1DataDataRecordsTotalFifoSizeOfSecondRecords": siteV1DataDataRecordsTotalFifoSizeOfSecondRecords,
       "siteV1DataDataRecordsTotalFifoSizeOfMinuteRecords": siteV1DataDataRecordsTotalFifoSizeOfMinuteRecords,
       "siteV1DataDataRecordsTotalFifoSizeOfHourRecords": siteV1DataDataRecordsTotalFifoSizeOfHourRecords,
       "siteV1DataDataRecordsTotalFifoSizeOfDayRecords": siteV1DataDataRecordsTotalFifoSizeOfDayRecords,
       "siteV1DataInventoryCANBusNodeIDs": siteV1DataInventoryCANBusNodeIDs,
       "siteV1DataCloudLinkCloudLinkState": siteV1DataCloudLinkCloudLinkState,
       "siteV1Config": siteV1Config,
       "siteV1ConfigNumber": siteV1ConfigNumber,
       "siteV1ConfigTable": siteV1ConfigTable,
       "siteV1ConfigEntry": siteV1ConfigEntry,
       "siteV1ConfigIndex": siteV1ConfigIndex,
       "siteV1ConfigName": siteV1ConfigName,
       "siteV1ConfigValue": siteV1ConfigValue,
       "siteV1ConfigEntryStatus": siteV1ConfigEntryStatus,
       "siteV1ConfigList": siteV1ConfigList,
       "siteV1CfgNetworkDHCPEnabled": siteV1CfgNetworkDHCPEnabled,
       "siteV1CfgNetworkIPAddressIfStatic": siteV1CfgNetworkIPAddressIfStatic,
       "siteV1CfgNetworkSubnetMaskIfStatic": siteV1CfgNetworkSubnetMaskIfStatic,
       "siteV1CfgNetworkDefaultGatewayIfStatic": siteV1CfgNetworkDefaultGatewayIfStatic,
       "siteV1CfgNetworkDNSIfStatic": siteV1CfgNetworkDNSIfStatic,
       "siteV1CfgNetworkMaxTransmissionUnit": siteV1CfgNetworkMaxTransmissionUnit,
       "siteV1CfgTimeSNTPTimeServer": siteV1CfgTimeSNTPTimeServer,
       "siteV1CfgTimeTimeZoneName": siteV1CfgTimeTimeZoneName,
       "siteV1CfgTimeSNTPTimeRefresh": siteV1CfgTimeSNTPTimeRefresh,
       "siteV1CfgTimeSNTPTimeRecoveryRefresh": siteV1CfgTimeSNTPTimeRecoveryRefresh,
       "siteV1CfgWebServerWebServerSecurityEnabled": siteV1CfgWebServerWebServerSecurityEnabled,
       "siteV1CfgWebServerWebServerPort": siteV1CfgWebServerWebServerPort,
       "siteV1CfgWebServerWebAuthenticationMethod": siteV1CfgWebServerWebAuthenticationMethod,
       "siteV1CfgWebServerHttpsWebServerPort": siteV1CfgWebServerHttpsWebServerPort,
       "siteV1CfgWebServerDefaultPage": siteV1CfgWebServerDefaultPage,
       "siteV1CfgXMLXMLEventPostingActivated": siteV1CfgXMLXMLEventPostingActivated,
       "siteV1CfgXMLXMLEventPostingRefreshTime": siteV1CfgXMLXMLEventPostingRefreshTime,
       "siteV1CfgXMLXMLEventPostingTimeout": siteV1CfgXMLXMLEventPostingTimeout,
       "siteV1CfgXMLXMLEventPostingToSecOnlyIfPrimFail": siteV1CfgXMLXMLEventPostingToSecOnlyIfPrimFail,
       "siteV1CfgXMLXMLTablesToPostOnXMLEvent": siteV1CfgXMLXMLTablesToPostOnXMLEvent,
       "siteV1CfgXMLXMLHeartbeatTime": siteV1CfgXMLXMLHeartbeatTime,
       "siteV1CfgSNMPSNMPActivated": siteV1CfgSNMPSNMPActivated,
       "siteV1CfgSNMPSNMPTrapVersion": siteV1CfgSNMPSNMPTrapVersion,
       "siteV1CfgSNMPSNMPGETMinSecurityLevel": siteV1CfgSNMPSNMPGETMinSecurityLevel,
       "siteV1CfgSNMPSNMPSETMinSecurityLevel": siteV1CfgSNMPSNMPSETMinSecurityLevel,
       "siteV1CfgSNMPSNMPV3AuthAlgorithm": siteV1CfgSNMPSNMPV3AuthAlgorithm,
       "siteV1CfgSNMPSNMPV3PrivacyAlgorithm": siteV1CfgSNMPSNMPV3PrivacyAlgorithm,
       "siteV1CfgSNMPSNMPV3PrivacyPassword": siteV1CfgSNMPSNMPV3PrivacyPassword,
       "siteV1CfgSNMPSNMPV3EngineID": siteV1CfgSNMPSNMPV3EngineID,
       "siteV1CfgSNMPSNMPV3TrapAuthAlgorithm": siteV1CfgSNMPSNMPV3TrapAuthAlgorithm,
       "siteV1CfgSNMPSNMPV3TrapPrivacyAlgorithm": siteV1CfgSNMPSNMPV3TrapPrivacyAlgorithm,
       "siteV1CfgSNMPSNMPV3TrapUsername": siteV1CfgSNMPSNMPV3TrapUsername,
       "siteV1CfgSNMPSNMPV3TrapAuthPassword": siteV1CfgSNMPSNMPV3TrapAuthPassword,
       "siteV1CfgSNMPSNMPV3TrapPrivacyPassword": siteV1CfgSNMPSNMPV3TrapPrivacyPassword,
       "siteV1CfgSNMPSiteDescriptionIdsIncludedInTraps": siteV1CfgSNMPSiteDescriptionIdsIncludedInTraps,
       "siteV1CfgGenericGenerateEventOnConfChanges": siteV1CfgGenericGenerateEventOnConfChanges,
       "siteV1CfgDataRecordsAutoArchivePeriodDataRecord": siteV1CfgDataRecordsAutoArchivePeriodDataRecord,
       "siteV1CfgGenericGenerateEventOnControlExecution": siteV1CfgGenericGenerateEventOnControlExecution,
       "siteV1CfgGenericGenerateEventOnAlarmAcknowledge": siteV1CfgGenericGenerateEventOnAlarmAcknowledge,
       "siteV1CfgInventoryRequiredCANBusNodeIDs": siteV1CfgInventoryRequiredCANBusNodeIDs,
       "siteV1CfgInventoryLSSCANidrange": siteV1CfgInventoryLSSCANidrange,
       "siteV1CfgInventorySystemNodesDefinition": siteV1CfgInventorySystemNodesDefinition,
       "siteV1CfgInventoryLSSCANOpenSavedConf": siteV1CfgInventoryLSSCANOpenSavedConf,
       "siteV1CfgUsersAdministratorLoginPassword": siteV1CfgUsersAdministratorLoginPassword,
       "siteV1CfgUsersUser1LoginPassword": siteV1CfgUsersUser1LoginPassword,
       "siteV1CfgUsersUser2LoginPassword": siteV1CfgUsersUser2LoginPassword,
       "siteV1CfgUsersUser3LoginPassword": siteV1CfgUsersUser3LoginPassword,
       "siteV1CfgUsersUser4LoginPassword": siteV1CfgUsersUser4LoginPassword,
       "siteV1CfgUsersUser5LoginPassword": siteV1CfgUsersUser5LoginPassword,
       "siteV1CfgRadiusAuthenticationRadiusServer": siteV1CfgRadiusAuthenticationRadiusServer,
       "siteV1CfgRadiusAuthenticationRadiusPort": siteV1CfgRadiusAuthenticationRadiusPort,
       "siteV1CfgRadiusAuthenticationRadiusSecret": siteV1CfgRadiusAuthenticationRadiusSecret,
       "siteV1CfgEmailEnableEmailFeature": siteV1CfgEmailEnableEmailFeature,
       "siteV1CfgEmailSmtpServer": siteV1CfgEmailSmtpServer,
       "siteV1CfgEmailSmtpDomain": siteV1CfgEmailSmtpDomain,
       "siteV1CfgEmailSmtpUserLoginPassword": siteV1CfgEmailSmtpUserLoginPassword,
       "siteV1CfgEmailMailSender": siteV1CfgEmailMailSender,
       "siteV1CfgEmailMailRecipients": siteV1CfgEmailMailRecipients,
       "siteV1CfgEmailMinimalSeverityTypeToSendMail": siteV1CfgEmailMinimalSeverityTypeToSendMail,
       "siteV1CfgControllerAutomaticReboot": siteV1CfgControllerAutomaticReboot,
       "siteV1CfgCloudLinkCloudEnabled": siteV1CfgCloudLinkCloudEnabled,
       "siteV1CfgCloudLinkCloudServer": siteV1CfgCloudLinkCloudServer,
       "siteV1CfgCloudLinkCloudPort": siteV1CfgCloudLinkCloudPort,
       "siteV1CfgCloudLinkCloudCredential": siteV1CfgCloudLinkCloudCredential,
       "siteV1CfgCloudLinkCloudCluster": siteV1CfgCloudLinkCloudCluster,
       "siteV1CfgInventoryRS485ExtensionsConf": siteV1CfgInventoryRS485ExtensionsConf,
       "siteV1CfgInventoryEthernetExtensionsConf": siteV1CfgInventoryEthernetExtensionsConf,
       "siteV1CfgScriptingEnabledscripts": siteV1CfgScriptingEnabledscripts,
       "siteV1CfgScriptingNumberofErrorsbeforetriggeringalarm": siteV1CfgScriptingNumberofErrorsbeforetriggeringalarm,
       "siteV1CfgGenericReadAccessUserNumbers": siteV1CfgGenericReadAccessUserNumbers,
       "siteV1CfgGenericWriteAccessUserNumbers": siteV1CfgGenericWriteAccessUserNumbers,
       "siteV1CfgGenericEventTableLength": siteV1CfgGenericEventTableLength,
       "siteV1CfgSNMPSNMPTrapTargetsIP": siteV1CfgSNMPSNMPTrapTargetsIP,
       "siteV1CfgSNMPMinimalEventSeverityForTraps": siteV1CfgSNMPMinimalEventSeverityForTraps,
       "siteV1CfgXMLXMLEventsPrimPostURL": siteV1CfgXMLXMLEventsPrimPostURL,
       "siteV1CfgXMLXMLEventsPrimPostLogin": siteV1CfgXMLXMLEventsPrimPostLogin,
       "siteV1CfgXMLXMLEventsPrimPostPassword": siteV1CfgXMLXMLEventsPrimPostPassword,
       "siteV1CfgXMLXMLEventsSecPostURL": siteV1CfgXMLXMLEventsSecPostURL,
       "siteV1CfgXMLXMLEventsSecPostLogin": siteV1CfgXMLXMLEventsSecPostLogin,
       "siteV1CfgXMLXMLEventsSecPostPassword": siteV1CfgXMLXMLEventsSecPostPassword,
       "siteV1CfgPLCNumberOfPLCData": siteV1CfgPLCNumberOfPLCData,
       "siteV1CfgPLCNumberOfPLCAlarm": siteV1CfgPLCNumberOfPLCAlarm,
       "siteV1Control": siteV1Control,
       "siteV1ControlNumber": siteV1ControlNumber,
       "siteV1ControlTable": siteV1ControlTable,
       "siteV1ControlEntry": siteV1ControlEntry,
       "siteV1ControlIndex": siteV1ControlIndex,
       "siteV1ControlName": siteV1ControlName,
       "siteV1ControlValue": siteV1ControlValue,
       "siteV1ControlEntryStatus": siteV1ControlEntryStatus,
       "siteV1ControlList": siteV1ControlList,
       "siteV1CtrlControllerRebootController": siteV1CtrlControllerRebootController,
       "siteV1CtrlControllerSaveConfAndRebootController": siteV1CtrlControllerSaveConfAndRebootController,
       "siteV1CtrlControllerRebootControllerWithoutSavingRecords": siteV1CtrlControllerRebootControllerWithoutSavingRecords,
       "siteV1CtrlNetworkApplyNetworkConf": siteV1CtrlNetworkApplyNetworkConf,
       "siteV1CtrlTimeForceSNTPTimeRefresh": siteV1CtrlTimeForceSNTPTimeRefresh,
       "siteV1CtrlTimeSetLocalTime": siteV1CtrlTimeSetLocalTime,
       "siteV1CtrlTimeSetUTCTime": siteV1CtrlTimeSetUTCTime,
       "siteV1CtrlTimeResetUptime": siteV1CtrlTimeResetUptime,
       "siteV1CtrlControllerCleanandSaveXMLUserConf": siteV1CtrlControllerCleanandSaveXMLUserConf,
       "siteV1CtrlControllerSaveXMLUserConf": siteV1CtrlControllerSaveXMLUserConf,
       "siteV1CtrlControllerSaveInventory": siteV1CtrlControllerSaveInventory,
       "siteV1CtrlDataRecordsSaveDataRecords": siteV1CtrlDataRecordsSaveDataRecords,
       "siteV1CtrlDataRecordsExportDataRecordsinCSV": siteV1CtrlDataRecordsExportDataRecordsinCSV,
       "siteV1CtrlDataRecordsArchiveDataRecords": siteV1CtrlDataRecordsArchiveDataRecords,
       "siteV1CtrlDataRecordsDeleteAllDataRecords": siteV1CtrlDataRecordsDeleteAllDataRecords,
       "siteV1CtrlControllerEmulateRecords": siteV1CtrlControllerEmulateRecords,
       "siteV1CtrlControllerReloadTranslations": siteV1CtrlControllerReloadTranslations,
       "siteV1CtrlControllerReloadLicense": siteV1CtrlControllerReloadLicense,
       "siteV1CtrlControllerManageFTPServer": siteV1CtrlControllerManageFTPServer,
       "siteV1CtrlInventoryRemoveAbsentEquipments": siteV1CtrlInventoryRemoveAbsentEquipments,
       "siteV1CtrlInventoryResetCANBusNode": siteV1CtrlInventoryResetCANBusNode,
       "siteV1CtrlInventorySaveCANOpenLSSConf": siteV1CtrlInventorySaveCANOpenLSSConf,
       "siteV1CtrlInventoryStartNewInventory": siteV1CtrlInventoryStartNewInventory,
       "siteV1CtrlInventoryUpgradeNodeFirmware": siteV1CtrlInventoryUpgradeNodeFirmware,
       "siteV1CtrlInventoryCancelFirmwareUpgrade": siteV1CtrlInventoryCancelFirmwareUpgrade,
       "siteV1CtrlFilesFlashBinary": siteV1CtrlFilesFlashBinary,
       "siteV1CtrlFilesDownloadFileFromUrl": siteV1CtrlFilesDownloadFileFromUrl,
       "siteV1CtrlFilesDeleteUserUploadedFile": siteV1CtrlFilesDeleteUserUploadedFile,
       "siteV1CtrlFilesMoveUserUploadedFile": siteV1CtrlFilesMoveUserUploadedFile,
       "siteV1CtrlFilesExtractZipFileinuserupload": siteV1CtrlFilesExtractZipFileinuserupload,
       "siteV1CtrlEmailSendSummaryEmail": siteV1CtrlEmailSendSummaryEmail,
       "siteV1CtrlScriptingControlLuaScript": siteV1CtrlScriptingControlLuaScript,
       "siteV1CtrlControllerAdvancedFunctionGenericCommandExecution": siteV1CtrlControllerAdvancedFunctionGenericCommandExecution,
       "siteV1CtrlGenericClearMyEvents": siteV1CtrlGenericClearMyEvents,
       "siteV1CtrlGenericClearAllEvents": siteV1CtrlGenericClearAllEvents,
       "siteV1CtrlGenericAddEvent": siteV1CtrlGenericAddEvent,
       "siteV1CtrlGenericAddMajorEvent": siteV1CtrlGenericAddMajorEvent,
       "siteV1CtrlGenericResetDefaultNamesAndGroups": siteV1CtrlGenericResetDefaultNamesAndGroups,
       "siteV1CtrlGenericResetDefaultNamesAndGroupsRecursive": siteV1CtrlGenericResetDefaultNamesAndGroupsRecursive,
       "siteV1Notifications": siteV1Notifications,
       "siteV1NotificationPrefix": siteV1NotificationPrefix,
       "siteV1NotificationOfEvent": siteV1NotificationOfEvent,
       "siteV1Compliance": siteV1Compliance,
       "siteV1ComplianceGroups": siteV1ComplianceGroups,
       "siteV1GlobalGroup": siteV1GlobalGroup,
       "siteV1NotificationGroup": siteV1NotificationGroup,
       "siteV1FullCompliance": siteV1FullCompliance,
       "energySystems": energySystems,
       "es1": es1,
       "es1GlobalStatus": es1GlobalStatus,
       "es1GlobalAlarmSeverityType": es1GlobalAlarmSeverityType,
       "es1GlobalAlarmSeverityLevel": es1GlobalAlarmSeverityLevel,
       "es1GlobalAlarmSeverityTypeInt": es1GlobalAlarmSeverityTypeInt,
       "es1Description": es1Description,
       "es1DescriptionNumber": es1DescriptionNumber,
       "es1DescriptionTable": es1DescriptionTable,
       "es1DescriptionEntry": es1DescriptionEntry,
       "es1DescriptionIndex": es1DescriptionIndex,
       "es1DescriptionName": es1DescriptionName,
       "es1DescriptionValue": es1DescriptionValue,
       "es1DescriptionEntryStatus": es1DescriptionEntryStatus,
       "es1DescriptionList": es1DescriptionList,
       "es1DescDescriptionDescription": es1DescDescriptionDescription,
       "es1DescDescriptionReference": es1DescDescriptionReference,
       "es1Alarm": es1Alarm,
       "es1AlarmNumber": es1AlarmNumber,
       "es1AlarmTable": es1AlarmTable,
       "es1AlarmEntry": es1AlarmEntry,
       "es1AlarmIndex": es1AlarmIndex,
       "es1AlarmName": es1AlarmName,
       "es1AlarmActive": es1AlarmActive,
       "es1AlarmSeverityType": es1AlarmSeverityType,
       "es1AlarmSeverityLevel": es1AlarmSeverityLevel,
       "es1AlarmStartTime": es1AlarmStartTime,
       "es1AlarmStopTime": es1AlarmStopTime,
       "es1AlarmEntryStatus": es1AlarmEntryStatus,
       "es1AlarmSummary": es1AlarmSummary,
       "es1Event": es1Event,
       "es1EventNumber": es1EventNumber,
       "es1EventTable": es1EventTable,
       "es1EventEntry": es1EventEntry,
       "es1EventIndex": es1EventIndex,
       "es1EventId": es1EventId,
       "es1EventName": es1EventName,
       "es1EventDateTime": es1EventDateTime,
       "es1EventSeverityType": es1EventSeverityType,
       "es1EventSeverityLevel": es1EventSeverityLevel,
       "es1EventEntryStatus": es1EventEntryStatus,
       "es1Data": es1Data,
       "es1DataNumber": es1DataNumber,
       "es1Config": es1Config,
       "es1ConfigNumber": es1ConfigNumber,
       "es1ConfigTable": es1ConfigTable,
       "es1ConfigEntry": es1ConfigEntry,
       "es1ConfigIndex": es1ConfigIndex,
       "es1ConfigName": es1ConfigName,
       "es1ConfigValue": es1ConfigValue,
       "es1ConfigEntryStatus": es1ConfigEntryStatus,
       "es1ConfigList": es1ConfigList,
       "es1CfgEnergyMeterNumberOfGenericPulseEnergyCounter": es1CfgEnergyMeterNumberOfGenericPulseEnergyCounter,
       "es1Control": es1Control,
       "es1ControlNumber": es1ControlNumber,
       "es1ControlTable": es1ControlTable,
       "es1ControlEntry": es1ControlEntry,
       "es1ControlIndex": es1ControlIndex,
       "es1ControlName": es1ControlName,
       "es1ControlValue": es1ControlValue,
       "es1ControlEntryStatus": es1ControlEntryStatus,
       "es1ControlList": es1ControlList,
       "es1CtrlGenericClearMyEvents": es1CtrlGenericClearMyEvents,
       "es1CtrlGenericClearAllEvents": es1CtrlGenericClearAllEvents,
       "es1CtrlGenericAddEvent": es1CtrlGenericAddEvent,
       "es1CtrlGenericAddMajorEvent": es1CtrlGenericAddMajorEvent,
       "es1CtrlGenericResetDefaultNamesAndGroups": es1CtrlGenericResetDefaultNamesAndGroups,
       "es1CtrlGenericResetDefaultNamesAndGroupsRecursive": es1CtrlGenericResetDefaultNamesAndGroupsRecursive,
       "es1Notifications": es1Notifications,
       "es1NotificationPrefix": es1NotificationPrefix,
       "es1NotificationOfEvent": es1NotificationOfEvent,
       "es1Compliance": es1Compliance,
       "es1ComplianceGroups": es1ComplianceGroups,
       "es1GlobalGroup": es1GlobalGroup,
       "es1NotificationGroup": es1NotificationGroup,
       "es1FullCompliance": es1FullCompliance,
       "es1DCSystems": es1DCSystems,
       "es1dc1": es1dc1,
       "es1dc1GlobalStatus": es1dc1GlobalStatus,
       "es1dc1GlobalAlarmSeverityType": es1dc1GlobalAlarmSeverityType,
       "es1dc1GlobalAlarmSeverityLevel": es1dc1GlobalAlarmSeverityLevel,
       "es1dc1GlobalAlarmSeverityTypeInt": es1dc1GlobalAlarmSeverityTypeInt,
       "es1dc1Description": es1dc1Description,
       "es1dc1DescriptionNumber": es1dc1DescriptionNumber,
       "es1dc1DescriptionTable": es1dc1DescriptionTable,
       "es1dc1DescriptionEntry": es1dc1DescriptionEntry,
       "es1dc1DescriptionIndex": es1dc1DescriptionIndex,
       "es1dc1DescriptionName": es1dc1DescriptionName,
       "es1dc1DescriptionValue": es1dc1DescriptionValue,
       "es1dc1DescriptionEntryStatus": es1dc1DescriptionEntryStatus,
       "es1dc1DescriptionList": es1dc1DescriptionList,
       "es1dc1DescDescriptionDescription": es1dc1DescDescriptionDescription,
       "es1dc1DescDescriptionReference": es1dc1DescDescriptionReference,
       "es1dc1DescDescriptionProductName": es1dc1DescDescriptionProductName,
       "es1dc1DescDescriptionHardwareReference": es1dc1DescDescriptionHardwareReference,
       "es1dc1DescDescriptionSoftwareReference": es1dc1DescDescriptionSoftwareReference,
       "es1dc1DescDescriptionSerialNumber": es1dc1DescDescriptionSerialNumber,
       "es1dc1DescDescriptionManufacturingDate": es1dc1DescDescriptionManufacturingDate,
       "es1dc1DescDescriptionDistributionModuleProductName": es1dc1DescDescriptionDistributionModuleProductName,
       "es1dc1DescDescriptionDistributionModuleHardwareReference": es1dc1DescDescriptionDistributionModuleHardwareReference,
       "es1dc1DescDescriptionDistributionModuleSoftwareReference": es1dc1DescDescriptionDistributionModuleSoftwareReference,
       "es1dc1DescDescriptionDistributionModuleSerialNumber": es1dc1DescDescriptionDistributionModuleSerialNumber,
       "es1dc1DescDescriptionDistributionModuleManufacturingDate": es1dc1DescDescriptionDistributionModuleManufacturingDate,
       "es1dc1Alarm": es1dc1Alarm,
       "es1dc1AlarmNumber": es1dc1AlarmNumber,
       "es1dc1AlarmTable": es1dc1AlarmTable,
       "es1dc1AlarmEntry": es1dc1AlarmEntry,
       "es1dc1AlarmIndex": es1dc1AlarmIndex,
       "es1dc1AlarmName": es1dc1AlarmName,
       "es1dc1AlarmActive": es1dc1AlarmActive,
       "es1dc1AlarmSeverityType": es1dc1AlarmSeverityType,
       "es1dc1AlarmSeverityLevel": es1dc1AlarmSeverityLevel,
       "es1dc1AlarmStartTime": es1dc1AlarmStartTime,
       "es1dc1AlarmStopTime": es1dc1AlarmStopTime,
       "es1dc1AlarmEntryStatus": es1dc1AlarmEntryStatus,
       "es1dc1AlarmSummary": es1dc1AlarmSummary,
       "es1dc1Event": es1dc1Event,
       "es1dc1EventNumber": es1dc1EventNumber,
       "es1dc1EventTable": es1dc1EventTable,
       "es1dc1EventEntry": es1dc1EventEntry,
       "es1dc1EventIndex": es1dc1EventIndex,
       "es1dc1EventId": es1dc1EventId,
       "es1dc1EventName": es1dc1EventName,
       "es1dc1EventDateTime": es1dc1EventDateTime,
       "es1dc1EventSeverityType": es1dc1EventSeverityType,
       "es1dc1EventSeverityLevel": es1dc1EventSeverityLevel,
       "es1dc1EventEntryStatus": es1dc1EventEntryStatus,
       "es1dc1Data": es1dc1Data,
       "es1dc1DataNumber": es1dc1DataNumber,
       "es1dc1DataTable": es1dc1DataTable,
       "es1dc1DataEntry": es1dc1DataEntry,
       "es1dc1DataIndex": es1dc1DataIndex,
       "es1dc1DataName": es1dc1DataName,
       "es1dc1DataValue": es1dc1DataValue,
       "es1dc1DataEntryStatus": es1dc1DataEntryStatus,
       "es1dc1DataList": es1dc1DataList,
       "es1dc1DataSystemDCMode": es1dc1DataSystemDCMode,
       "es1dc1DataSystemPreviousDCMode": es1dc1DataSystemPreviousDCMode,
       "es1dc1DataSystemNiMHChargeMode": es1dc1DataSystemNiMHChargeMode,
       "es1dc1DataDCBusBusVoltage": es1dc1DataDCBusBusVoltage,
       "es1dc1DataSystemRatioDeliveredOnAvailablePower": es1dc1DataSystemRatioDeliveredOnAvailablePower,
       "es1dc1DataACBusMinutesSinceLastACFailBegin": es1dc1DataACBusMinutesSinceLastACFailBegin,
       "es1dc1DataACBusMinutesSinceLastACFailEnd": es1dc1DataACBusMinutesSinceLastACFailEnd,
       "es1dc1DataRectifiersRectifiersOutPower": es1dc1DataRectifiersRectifiersOutPower,
       "es1dc1DataRectifiersRectifiersOutCurrent": es1dc1DataRectifiersRectifiersOutCurrent,
       "es1dc1DataRectifiersRectifiersOutPowerMax": es1dc1DataRectifiersRectifiersOutPowerMax,
       "es1dc1DataRectifiersRectifiersOutCurrentMax": es1dc1DataRectifiersRectifiersOutCurrentMax,
       "es1dc1DataRectifiersNumberOfRectifierMax": es1dc1DataRectifiersNumberOfRectifierMax,
       "es1dc1DataRectifiersNumberOfPresentRectifier": es1dc1DataRectifiersNumberOfPresentRectifier,
       "es1dc1DataRectifiersNumberOfAbsentRectifier": es1dc1DataRectifiersNumberOfAbsentRectifier,
       "es1dc1DataRectifiersNumberOfActiveRectifier": es1dc1DataRectifiersNumberOfActiveRectifier,
       "es1dc1DataRectifiersNumberOfACFailRectifier": es1dc1DataRectifiersNumberOfACFailRectifier,
       "es1dc1DataRectifiersNumberOfDCFailRectifier": es1dc1DataRectifiersNumberOfDCFailRectifier,
       "es1dc1DataRectifiersNumberOfRemoteOffRectifier": es1dc1DataRectifiersNumberOfRemoteOffRectifier,
       "es1dc1DataRectifiersNumberOfOverTempRectifier": es1dc1DataRectifiersNumberOfOverTempRectifier,
       "es1dc1DataLoadLoadPower": es1dc1DataLoadLoadPower,
       "es1dc1DataLoadLoadCurrent": es1dc1DataLoadLoadCurrent,
       "es1dc1DataBatBatInputCurrent": es1dc1DataBatBatInputCurrent,
       "es1dc1DataBatBatInputPower": es1dc1DataBatBatInputPower,
       "es1dc1DataBatBatTemp": es1dc1DataBatBatTemp,
       "es1dc1DataBatBatTestState": es1dc1DataBatBatTestState,
       "es1dc1DataBatLastBatTestDischargedCapacityRatio": es1dc1DataBatLastBatTestDischargedCapacityRatio,
       "es1dc1DataBatLastBatTestDischargedCapacity": es1dc1DataBatLastBatTestDischargedCapacity,
       "es1dc1DataBatLastBatTestFinalVoltage": es1dc1DataBatLastBatTestFinalVoltage,
       "es1dc1DataBatBatTestDuration": es1dc1DataBatBatTestDuration,
       "es1dc1DataBatPreviousBatTestDischargedCapacityRatio": es1dc1DataBatPreviousBatTestDischargedCapacityRatio,
       "es1dc1DataBatPreviousBatTestDischargedCapacity": es1dc1DataBatPreviousBatTestDischargedCapacity,
       "es1dc1DataBatPreviousBatTestFinalVoltage": es1dc1DataBatPreviousBatTestFinalVoltage,
       "es1dc1DataBatPreviousBatTestDuration": es1dc1DataBatPreviousBatTestDuration,
       "es1dc1DataBatPreviousBatTestState": es1dc1DataBatPreviousBatTestState,
       "es1dc1DataBatMinutesSinceLastTestBat": es1dc1DataBatMinutesSinceLastTestBat,
       "es1dc1DataBatNextScheduledBatTest": es1dc1DataBatNextScheduledBatTest,
       "es1dc1DataBatBatChargeCapacity": es1dc1DataBatBatChargeCapacity,
       "es1dc1DataBatCalculatedAutonomy": es1dc1DataBatCalculatedAutonomy,
       "es1dc1DataBatBatCurrentIntegration": es1dc1DataBatBatCurrentIntegration,
       "es1dc1DataLVDLVDState": es1dc1DataLVDLVDState,
       "es1dc1DataRelsRel1State": es1dc1DataRelsRel1State,
       "es1dc1DataRelsRel2State": es1dc1DataRelsRel2State,
       "es1dc1DataRelsRel3State": es1dc1DataRelsRel3State,
       "es1dc1DataRelsRel4State": es1dc1DataRelsRel4State,
       "es1dc1DataSmartEnergyEfficiencyOptimizedNumberOfRectifier": es1dc1DataSmartEnergyEfficiencyOptimizedNumberOfRectifier,
       "es1dc1DataSmartEnergySystemLossWithoutOptimisation": es1dc1DataSmartEnergySystemLossWithoutOptimisation,
       "es1dc1DataSmartEnergySystemLossWithOptimisation": es1dc1DataSmartEnergySystemLossWithOptimisation,
       "es1dc1DataSmartEnergyRectifierModelUsedForCalculation": es1dc1DataSmartEnergyRectifierModelUsedForCalculation,
       "es1dc1DataSmartEnergySmartEnergySavings": es1dc1DataSmartEnergySmartEnergySavings,
       "es1dc1DataSensorsAmbientTemp": es1dc1DataSensorsAmbientTemp,
       "es1dc1DataSensorsPulseCounter4": es1dc1DataSensorsPulseCounter4,
       "es1dc1Config": es1dc1Config,
       "es1dc1ConfigNumber": es1dc1ConfigNumber,
       "es1dc1ConfigTable": es1dc1ConfigTable,
       "es1dc1ConfigEntry": es1dc1ConfigEntry,
       "es1dc1ConfigIndex": es1dc1ConfigIndex,
       "es1dc1ConfigName": es1dc1ConfigName,
       "es1dc1ConfigValue": es1dc1ConfigValue,
       "es1dc1ConfigEntryStatus": es1dc1ConfigEntryStatus,
       "es1dc1ConfigList": es1dc1ConfigList,
       "es1dc1CfgDCBusDCBusFloatVoltageat25degC": es1dc1CfgDCBusDCBusFloatVoltageat25degC,
       "es1dc1CfgDCBusDCBusVoltageExtraLow": es1dc1CfgDCBusDCBusVoltageExtraLow,
       "es1dc1CfgDCBusDCBusVoltageExtraLowHysteresis": es1dc1CfgDCBusDCBusVoltageExtraLowHysteresis,
       "es1dc1CfgDCBusDCBusVoltageLow": es1dc1CfgDCBusDCBusVoltageLow,
       "es1dc1CfgDCBusDCBusVoltageLowHysteresis": es1dc1CfgDCBusDCBusVoltageLowHysteresis,
       "es1dc1CfgDCBusDCBusVoltageHigh": es1dc1CfgDCBusDCBusVoltageHigh,
       "es1dc1CfgDCBusDCBusVoltageHighHysteresis": es1dc1CfgDCBusDCBusVoltageHighHysteresis,
       "es1dc1CfgDCBusDCBusVoltageExtraHigh": es1dc1CfgDCBusDCBusVoltageExtraHigh,
       "es1dc1CfgDCBusDCBusVoltageExtraHighHysteresis": es1dc1CfgDCBusDCBusVoltageExtraHighHysteresis,
       "es1dc1CfgLVDLVDDisconnectVoltage": es1dc1CfgLVDLVDDisconnectVoltage,
       "es1dc1CfgLVDLVDDisconnectDelay": es1dc1CfgLVDLVDDisconnectDelay,
       "es1dc1CfgBatTempCompensationSlope": es1dc1CfgBatTempCompensationSlope,
       "es1dc1CfgBatMaxPosTempCompensation": es1dc1CfgBatMaxPosTempCompensation,
       "es1dc1CfgBatMaxNegTempCompensation": es1dc1CfgBatMaxNegTempCompensation,
       "es1dc1CfgRectifiersMinimalNumberOfPresentRectifiers": es1dc1CfgRectifiersMinimalNumberOfPresentRectifiers,
       "es1dc1CfgRectifiersRectifierModel": es1dc1CfgRectifiersRectifierModel,
       "es1dc1CfgRectifiersForcedRemoteOffRectifers": es1dc1CfgRectifiersForcedRemoteOffRectifers,
       "es1dc1CfgBatBatChargeCurrentLimit": es1dc1CfgBatBatChargeCurrentLimit,
       "es1dc1CfgBatBatStringCapacity": es1dc1CfgBatBatStringCapacity,
       "es1dc1CfgBatBatTempLow": es1dc1CfgBatBatTempLow,
       "es1dc1CfgBatBatTempHigh": es1dc1CfgBatBatTempHigh,
       "es1dc1CfgBatBatTempHysteresis": es1dc1CfgBatBatTempHysteresis,
       "es1dc1CfgBatMinimalCurrentForDischargingAlarm": es1dc1CfgBatMinimalCurrentForDischargingAlarm,
       "es1dc1CfgBatCurrentHysteresisForDischargingAlarm": es1dc1CfgBatCurrentHysteresisForDischargingAlarm,
       "es1dc1CfgBatPeukertNumber": es1dc1CfgBatPeukertNumber,
       "es1dc1CfgBatMaxDepthOfDischargeforAutonomyEstimation": es1dc1CfgBatMaxDepthOfDischargeforAutonomyEstimation,
       "es1dc1CfgBatBoostAutomatic": es1dc1CfgBatBoostAutomatic,
       "es1dc1CfgBatBoostActivationLowVoltage": es1dc1CfgBatBoostActivationLowVoltage,
       "es1dc1CfgBatBoostTerminationVoltage": es1dc1CfgBatBoostTerminationVoltage,
       "es1dc1CfgBatBoostTerminationCurrent": es1dc1CfgBatBoostTerminationCurrent,
       "es1dc1CfgBatBoostTerminationTime": es1dc1CfgBatBoostTerminationTime,
       "es1dc1CfgBatBatTestType": es1dc1CfgBatBatTestType,
       "es1dc1CfgBatBatTestEndVoltage": es1dc1CfgBatBatTestEndVoltage,
       "es1dc1CfgBatBatTestDischargeRatio": es1dc1CfgBatBatTestDischargeRatio,
       "es1dc1CfgBatBatTestInterval": es1dc1CfgBatBatTestInterval,
       "es1dc1CfgBatBatTestDischargeCurrent": es1dc1CfgBatBatTestDischargeCurrent,
       "es1dc1CfgBatBatTestMinimalDischargeCurrent": es1dc1CfgBatBatTestMinimalDischargeCurrent,
       "es1dc1CfgBatBatTestDuration": es1dc1CfgBatBatTestDuration,
       "es1dc1CfgBatBatTestRequMinutesWithoutMainsFail": es1dc1CfgBatBatTestRequMinutesWithoutMainsFail,
       "es1dc1CfgBatBatTestSchedulerCronRule": es1dc1CfgBatBatTestSchedulerCronRule,
       "es1dc1CfgSmartEnergySmartEnergyBooleanCond": es1dc1CfgSmartEnergySmartEnergyBooleanCond,
       "es1dc1CfgLVDBatLVDNodeId": es1dc1CfgLVDBatLVDNodeId,
       "es1dc1CfgDigInputsDigInput1Name": es1dc1CfgDigInputsDigInput1Name,
       "es1dc1CfgDigInputsDigInput1NormallyClosed": es1dc1CfgDigInputsDigInput1NormallyClosed,
       "es1dc1CfgDigInputsDigInput2Name": es1dc1CfgDigInputsDigInput2Name,
       "es1dc1CfgDigInputsDigInput2NormallyClosed": es1dc1CfgDigInputsDigInput2NormallyClosed,
       "es1dc1CfgDigInputsDigInput3Name": es1dc1CfgDigInputsDigInput3Name,
       "es1dc1CfgDigInputsDigInput3NormallyClosed": es1dc1CfgDigInputsDigInput3NormallyClosed,
       "es1dc1CfgDigInputsDigInput4Name": es1dc1CfgDigInputsDigInput4Name,
       "es1dc1CfgDigInputsDigInput4NormallyClosed": es1dc1CfgDigInputsDigInput4NormallyClosed,
       "es1dc1CfgDigInputsDigInput5Name": es1dc1CfgDigInputsDigInput5Name,
       "es1dc1CfgDigInputsDigInput5NormallyClosed": es1dc1CfgDigInputsDigInput5NormallyClosed,
       "es1dc1CfgDigInputsDigInput6Name": es1dc1CfgDigInputsDigInput6Name,
       "es1dc1CfgDigInputsDigInput6NormallyClosed": es1dc1CfgDigInputsDigInput6NormallyClosed,
       "es1dc1CfgRelsDryAlarm1AlternativeBooleanCond": es1dc1CfgRelsDryAlarm1AlternativeBooleanCond,
       "es1dc1CfgRelsDryAlarm2AlternativeBooleanCond": es1dc1CfgRelsDryAlarm2AlternativeBooleanCond,
       "es1dc1CfgRelsDryAlarm3AlternativeBooleanCond": es1dc1CfgRelsDryAlarm3AlternativeBooleanCond,
       "es1dc1CfgRelsDryAlarm4AlternativeBooleanCond": es1dc1CfgRelsDryAlarm4AlternativeBooleanCond,
       "es1dc1CfgSensorsAmbientTempLow": es1dc1CfgSensorsAmbientTempLow,
       "es1dc1CfgSensorsAmbientTempHigh": es1dc1CfgSensorsAmbientTempHigh,
       "es1dc1CfgSensorsAmbientTempHysteresis": es1dc1CfgSensorsAmbientTempHysteresis,
       "es1dc1CfgGenericReadAccessUserNumbers": es1dc1CfgGenericReadAccessUserNumbers,
       "es1dc1CfgGenericWriteAccessUserNumbers": es1dc1CfgGenericWriteAccessUserNumbers,
       "es1dc1CfgGenericEventTableLength": es1dc1CfgGenericEventTableLength,
       "es1dc1CfgGenericEventTableLengthByRectifier": es1dc1CfgGenericEventTableLengthByRectifier,
       "es1dc1CfgPLCNumberOfPLCData": es1dc1CfgPLCNumberOfPLCData,
       "es1dc1CfgPLCNumberOfPLCAlarm": es1dc1CfgPLCNumberOfPLCAlarm,
       "es1dc1Control": es1dc1Control,
       "es1dc1ControlNumber": es1dc1ControlNumber,
       "es1dc1ControlTable": es1dc1ControlTable,
       "es1dc1ControlEntry": es1dc1ControlEntry,
       "es1dc1ControlIndex": es1dc1ControlIndex,
       "es1dc1ControlName": es1dc1ControlName,
       "es1dc1ControlValue": es1dc1ControlValue,
       "es1dc1ControlEntryStatus": es1dc1ControlEntryStatus,
       "es1dc1ControlList": es1dc1ControlList,
       "es1dc1CtrlSystemBackToFloat": es1dc1CtrlSystemBackToFloat,
       "es1dc1CtrlSystemStartBatTest": es1dc1CtrlSystemStartBatTest,
       "es1dc1CtrlSystemForceBatTest": es1dc1CtrlSystemForceBatTest,
       "es1dc1CtrlSystemStartBoostMode": es1dc1CtrlSystemStartBoostMode,
       "es1dc1CtrlLVDOpenTheLVD": es1dc1CtrlLVDOpenTheLVD,
       "es1dc1CtrlLVDCloseTheLVD": es1dc1CtrlLVDCloseTheLVD,
       "es1dc1CtrlBatCorrectBatCurrentOffset": es1dc1CtrlBatCorrectBatCurrentOffset,
       "es1dc1CtrlBatResetLastBatTestState": es1dc1CtrlBatResetLastBatTestState,
       "es1dc1CtrlSaveSaveConfInMCU": es1dc1CtrlSaveSaveConfInMCU,
       "es1dc1CtrlAdvancedSetMCUSpecificConfId": es1dc1CtrlAdvancedSetMCUSpecificConfId,
       "es1dc1CtrlDigInputsSetDigInput4CounterValue": es1dc1CtrlDigInputsSetDigInput4CounterValue,
       "es1dc1CtrlRelsInvertRel1StateForXSeconds": es1dc1CtrlRelsInvertRel1StateForXSeconds,
       "es1dc1CtrlRelsInvertRel2StateForXSeconds": es1dc1CtrlRelsInvertRel2StateForXSeconds,
       "es1dc1CtrlRelsInvertRel3StateForXSeconds": es1dc1CtrlRelsInvertRel3StateForXSeconds,
       "es1dc1CtrlRelsInvertRel4StateForXSeconds": es1dc1CtrlRelsInvertRel4StateForXSeconds,
       "es1dc1CtrlGenericClearMyEvents": es1dc1CtrlGenericClearMyEvents,
       "es1dc1CtrlGenericClearAllEvents": es1dc1CtrlGenericClearAllEvents,
       "es1dc1CtrlGenericAddEvent": es1dc1CtrlGenericAddEvent,
       "es1dc1CtrlGenericAddMajorEvent": es1dc1CtrlGenericAddMajorEvent,
       "es1dc1CtrlGenericResetDefaultNamesAndGroups": es1dc1CtrlGenericResetDefaultNamesAndGroups,
       "es1dc1CtrlGenericResetDefaultNamesAndGroupsRecursive": es1dc1CtrlGenericResetDefaultNamesAndGroupsRecursive,
       "es1dc1Notifications": es1dc1Notifications,
       "es1dc1NotificationPrefix": es1dc1NotificationPrefix,
       "es1dc1NotificationOfEvent": es1dc1NotificationOfEvent,
       "es1dc1Compliance": es1dc1Compliance,
       "es1dc1ComplianceGroups": es1dc1ComplianceGroups,
       "es1dc1GlobalGroup": es1dc1GlobalGroup,
       "es1dc1NotificationGroup": es1dc1NotificationGroup,
       "es1dc1FullCompliance": es1dc1FullCompliance,
       "es1InverterSystems": es1InverterSystems,
       "es1RemotePowerFeedingSystems": es1RemotePowerFeedingSystems,
       "extensions": extensions}
)
