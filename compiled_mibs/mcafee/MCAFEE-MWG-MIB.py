# SNMP MIB module (MCAFEE-MWG-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\mcafee\MCAFEE-MWG-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 12:10:26 2025
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

(mcafeeGATEWAY,) = mibBuilder.importSymbols(
    "MCAFEE-SMI",
    "mcafeeGATEWAY")

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
 iso,
 mib_2) = mibBuilder.importSymbols(
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
    "iso",
    "mib-2")

(DisplayString,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

mwg = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 1230, 2, 7)
)
if mibBuilder.loadTexts:
    mwg.setRevisions(
        ("2014-11-10 00:00",
         "2014-10-07 00:00",
         "2013-05-21 00:00",
         "2011-12-01 00:00",
         "2011-01-11 00:00",
         "2010-04-26 00:00",
         "2010-02-19 00:00",
         "2009-10-13 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_MwgInfo_ObjectIdentity = ObjectIdentity
mwgInfo = _MwgInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1230, 2, 7, 1)
)


class _KProductName_Type(DisplayString):
    """Custom type kProductName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_KProductName_Type.__name__ = "DisplayString"
_KProductName_Object = MibScalar
kProductName = _KProductName_Object(
    (1, 3, 6, 1, 4, 1, 1230, 2, 7, 1, 1),
    _KProductName_Type()
)
kProductName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    kProductName.setStatus("current")


class _KCompanyName_Type(DisplayString):
    """Custom type kCompanyName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 20),
    )


_KCompanyName_Type.__name__ = "DisplayString"
_KCompanyName_Object = MibScalar
kCompanyName = _KCompanyName_Object(
    (1, 3, 6, 1, 4, 1, 1230, 2, 7, 1, 2),
    _KCompanyName_Type()
)
kCompanyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kCompanyName.setStatus("current")


class _KProductVersion_Type(DisplayString):
    """Custom type kProductVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_KProductVersion_Type.__name__ = "DisplayString"
_KProductVersion_Object = MibScalar
kProductVersion = _KProductVersion_Object(
    (1, 3, 6, 1, 4, 1, 1230, 2, 7, 1, 3),
    _KProductVersion_Type()
)
kProductVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kProductVersion.setStatus("current")
_KMajorVersion_Type = Integer32
_KMajorVersion_Object = MibScalar
kMajorVersion = _KMajorVersion_Object(
    (1, 3, 6, 1, 4, 1, 1230, 2, 7, 1, 4),
    _KMajorVersion_Type()
)
kMajorVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kMajorVersion.setStatus("current")
_KMinorVersion_Type = Integer32
_KMinorVersion_Object = MibScalar
kMinorVersion = _KMinorVersion_Object(
    (1, 3, 6, 1, 4, 1, 1230, 2, 7, 1, 5),
    _KMinorVersion_Type()
)
kMinorVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kMinorVersion.setStatus("current")
_KMicroVersion_Type = Integer32
_KMicroVersion_Object = MibScalar
kMicroVersion = _KMicroVersion_Object(
    (1, 3, 6, 1, 4, 1, 1230, 2, 7, 1, 6),
    _KMicroVersion_Type()
)
kMicroVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kMicroVersion.setStatus("current")
_KHotfixVersion_Type = Integer32
_KHotfixVersion_Object = MibScalar
kHotfixVersion = _KHotfixVersion_Object(
    (1, 3, 6, 1, 4, 1, 1230, 2, 7, 1, 7),
    _KHotfixVersion_Type()
)
kHotfixVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kHotfixVersion.setStatus("current")
_KCustomVersion_Type = Integer32
_KCustomVersion_Object = MibScalar
kCustomVersion = _KCustomVersion_Object(
    (1, 3, 6, 1, 4, 1, 1230, 2, 7, 1, 8),
    _KCustomVersion_Type()
)
kCustomVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kCustomVersion.setStatus("current")


class _KRevision_Type(DisplayString):
    """Custom type kRevision based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 20),
    )


_KRevision_Type.__name__ = "DisplayString"
_KRevision_Object = MibScalar
kRevision = _KRevision_Object(
    (1, 3, 6, 1, 4, 1, 1230, 2, 7, 1, 9),
    _KRevision_Type()
)
kRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kRevision.setStatus("current")
_KBuildNumber_Type = Integer32
_KBuildNumber_Object = MibScalar
kBuildNumber = _KBuildNumber_Object(
    (1, 3, 6, 1, 4, 1, 1230, 2, 7, 1, 10),
    _KBuildNumber_Type()
)
kBuildNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kBuildNumber.setStatus("current")
_MwgEngineVersions_ObjectIdentity = ObjectIdentity
mwgEngineVersions = _MwgEngineVersions_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1230, 2, 7, 1, 20)
)


class _PAMEngineVersion_Type(DisplayString):
    """Custom type pAMEngineVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 20),
    )


_PAMEngineVersion_Type.__name__ = "DisplayString"
_PAMEngineVersion_Object = MibScalar
pAMEngineVersion = _PAMEngineVersion_Object(
    (1, 3, 6, 1, 4, 1, 1230, 2, 7, 1, 20, 1),
    _PAMEngineVersion_Type()
)
pAMEngineVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pAMEngineVersion.setStatus("current")


class _PAMSignatureVersion_Type(DisplayString):
    """Custom type pAMSignatureVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 20),
    )


_PAMSignatureVersion_Type.__name__ = "DisplayString"
_PAMSignatureVersion_Object = MibScalar
pAMSignatureVersion = _PAMSignatureVersion_Object(
    (1, 3, 6, 1, 4, 1, 1230, 2, 7, 1, 20, 2),
    _PAMSignatureVersion_Type()
)
pAMSignatureVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pAMSignatureVersion.setStatus("current")


class _PMFEEngineVersion_Type(DisplayString):
    """Custom type pMFEEngineVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 20),
    )


_PMFEEngineVersion_Type.__name__ = "DisplayString"
_PMFEEngineVersion_Object = MibScalar
pMFEEngineVersion = _PMFEEngineVersion_Object(
    (1, 3, 6, 1, 4, 1, 1230, 2, 7, 1, 20, 3),
    _PMFEEngineVersion_Type()
)
pMFEEngineVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pMFEEngineVersion.setStatus("current")


class _PMFEDATVersion_Type(DisplayString):
    """Custom type pMFEDATVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 20),
    )


_PMFEDATVersion_Type.__name__ = "DisplayString"
_PMFEDATVersion_Object = MibScalar
pMFEDATVersion = _PMFEDATVersion_Object(
    (1, 3, 6, 1, 4, 1, 1230, 2, 7, 1, 20, 4),
    _PMFEDATVersion_Type()
)
pMFEDATVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pMFEDATVersion.setStatus("current")


class _PAMProactiveVersion_Type(DisplayString):
    """Custom type pAMProactiveVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 20),
    )


_PAMProactiveVersion_Type.__name__ = "DisplayString"
_PAMProactiveVersion_Object = MibScalar
pAMProactiveVersion = _PAMProactiveVersion_Object(
    (1, 3, 6, 1, 4, 1, 1230, 2, 7, 1, 20, 5),
    _PAMProactiveVersion_Type()
)
pAMProactiveVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pAMProactiveVersion.setStatus("current")


class _PTSDBVersion_Type(DisplayString):
    """Custom type pTSDBVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 20),
    )


_PTSDBVersion_Type.__name__ = "DisplayString"
_PTSDBVersion_Object = MibScalar
pTSDBVersion = _PTSDBVersion_Object(
    (1, 3, 6, 1, 4, 1, 1230, 2, 7, 1, 20, 6),
    _PTSDBVersion_Type()
)
pTSDBVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pTSDBVersion.setStatus("current")
_MwgStatistics_ObjectIdentity = ObjectIdentity
mwgStatistics = _MwgStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1230, 2, 7, 2)
)
_MwgContent_ObjectIdentity = ObjectIdentity
mwgContent = _MwgContent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1230, 2, 7, 2, 1)
)
_StBadReputation_Type = Counter64
_StBadReputation_Object = MibScalar
stBadReputation = _StBadReputation_Object(
    (1, 3, 6, 1, 4, 1, 1230, 2, 7, 2, 1, 1),
    _StBadReputation_Type()
)
stBadReputation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stBadReputation.setStatus("obsolete")
_StMalwareDetected_Type = Counter64
_StMalwareDetected_Object = MibScalar
stMalwareDetected = _StMalwareDetected_Object(
    (1, 3, 6, 1, 4, 1, 1230, 2, 7, 2, 1, 2),
    _StMalwareDetected_Type()
)
stMalwareDetected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stMalwareDetected.setStatus("current")
_StConnectionsLegitimate_Type = Counter64
_StConnectionsLegitimate_Object = MibScalar
stConnectionsLegitimate = _StConnectionsLegitimate_Object(
    (1, 3, 6, 1, 4, 1, 1230, 2, 7, 2, 1, 3),
    _StConnectionsLegitimate_Type()
)
stConnectionsLegitimate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stConnectionsLegitimate.setStatus("current")
_StBlockedByAntiMalware_Type = Counter64
_StBlockedByAntiMalware_Object = MibScalar
stBlockedByAntiMalware = _StBlockedByAntiMalware_Object(
    (1, 3, 6, 1, 4, 1, 1230, 2, 7, 2, 1, 4),
    _StBlockedByAntiMalware_Type()
)
stBlockedByAntiMalware.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stBlockedByAntiMalware.setStatus("current")
_StConnectionsBlocked_Type = Counter64
_StConnectionsBlocked_Object = MibScalar
stConnectionsBlocked = _StConnectionsBlocked_Object(
    (1, 3, 6, 1, 4, 1, 1230, 2, 7, 2, 1, 5),
    _StConnectionsBlocked_Type()
)
stConnectionsBlocked.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stConnectionsBlocked.setStatus("current")
_StBlockedByMediaFilter_Type = Counter64
_StBlockedByMediaFilter_Object = MibScalar
stBlockedByMediaFilter = _StBlockedByMediaFilter_Object(
    (1, 3, 6, 1, 4, 1, 1230, 2, 7, 2, 1, 6),
    _StBlockedByMediaFilter_Type()
)
stBlockedByMediaFilter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stBlockedByMediaFilter.setStatus("current")
_StBlockedByURLFilter_Type = Counter64
_StBlockedByURLFilter_Object = MibScalar
stBlockedByURLFilter = _StBlockedByURLFilter_Object(
    (1, 3, 6, 1, 4, 1, 1230, 2, 7, 2, 1, 7),
    _StBlockedByURLFilter_Type()
)
stBlockedByURLFilter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stBlockedByURLFilter.setStatus("current")
_StMimeType_Type = Counter64
_StMimeType_Object = MibScalar
stMimeType = _StMimeType_Object(
    (1, 3, 6, 1, 4, 1, 1230, 2, 7, 2, 1, 8),
    _StMimeType_Type()
)
stMimeType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stMimeType.setStatus("current")
_StCategories_Type = Counter64
_StCategories_Object = MibScalar
stCategories = _StCategories_Object(
    (1, 3, 6, 1, 4, 1, 1230, 2, 7, 2, 1, 9),
    _StCategories_Type()
)
stCategories.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stCategories.setStatus("current")
_StCategoriesTable_Object = MibTable
stCategoriesTable = _StCategoriesTable_Object(
    (1, 3, 6, 1, 4, 1, 1230, 2, 7, 2, 1, 10)
)
if mibBuilder.loadTexts:
    stCategoriesTable.setStatus("current")
_StCategoriesEntry_Object = MibTableRow
stCategoriesEntry = _StCategoriesEntry_Object(
    (1, 3, 6, 1, 4, 1, 1230, 2, 7, 2, 1, 10, 1)
)
stCategoriesEntry.setIndexNames(
    (0, "MCAFEE-MWG-MIB", "stCategoryName"),
)
if mibBuilder.loadTexts:
    stCategoriesEntry.setStatus("current")


class _StCategoryName_Type(DisplayString):
    """Custom type stCategoryName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_StCategoryName_Type.__name__ = "DisplayString"
_StCategoryName_Object = MibTableColumn
stCategoryName = _StCategoryName_Object(
    (1, 3, 6, 1, 4, 1, 1230, 2, 7, 2, 1, 10, 1, 1),
    _StCategoryName_Type()
)
stCategoryName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stCategoryName.setStatus("current")
_StCategoryCount_Type = Counter64
_StCategoryCount_Object = MibTableColumn
stCategoryCount = _StCategoryCount_Object(
    (1, 3, 6, 1, 4, 1, 1230, 2, 7, 2, 1, 10, 1, 2),
    _StCategoryCount_Type()
)
stCategoryCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stCategoryCount.setStatus("current")
_MwgHttp_ObjectIdentity = ObjectIdentity
mwgHttp = _MwgHttp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1230, 2, 7, 2, 2)
)
_StHttpRequests_Type = Counter64
_StHttpRequests_Object = MibScalar
stHttpRequests = _StHttpRequests_Object(
    (1, 3, 6, 1, 4, 1, 1230, 2, 7, 2, 2, 1),
    _StHttpRequests_Type()
)
stHttpRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stHttpRequests.setStatus("current")
_StHttpTraffic_Type = Counter64
_StHttpTraffic_Object = MibScalar
stHttpTraffic = _StHttpTraffic_Object(
    (1, 3, 6, 1, 4, 1, 1230, 2, 7, 2, 2, 2),
    _StHttpTraffic_Type()
)
stHttpTraffic.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stHttpTraffic.setStatus("current")
_StHttpBytesFromClient_Type = Counter64
_StHttpBytesFromClient_Object = MibScalar
stHttpBytesFromClient = _StHttpBytesFromClient_Object(
    (1, 3, 6, 1, 4, 1, 1230, 2, 7, 2, 2, 3),
    _StHttpBytesFromClient_Type()
)
stHttpBytesFromClient.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stHttpBytesFromClient.setStatus("current")
_StHttpBytesFromServer_Type = Counter64
_StHttpBytesFromServer_Object = MibScalar
stHttpBytesFromServer = _StHttpBytesFromServer_Object(
    (1, 3, 6, 1, 4, 1, 1230, 2, 7, 2, 2, 4),
    _StHttpBytesFromServer_Type()
)
stHttpBytesFromServer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stHttpBytesFromServer.setStatus("current")
_StHttpBytesToClient_Type = Counter64
_StHttpBytesToClient_Object = MibScalar
stHttpBytesToClient = _StHttpBytesToClient_Object(
    (1, 3, 6, 1, 4, 1, 1230, 2, 7, 2, 2, 5),
    _StHttpBytesToClient_Type()
)
stHttpBytesToClient.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stHttpBytesToClient.setStatus("current")
_StHttpBytesToServer_Type = Counter64
_StHttpBytesToServer_Object = MibScalar
stHttpBytesToServer = _StHttpBytesToServer_Object(
    (1, 3, 6, 1, 4, 1, 1230, 2, 7, 2, 2, 6),
    _StHttpBytesToServer_Type()
)
stHttpBytesToServer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stHttpBytesToServer.setStatus("current")
_MwgHttps_ObjectIdentity = ObjectIdentity
mwgHttps = _MwgHttps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1230, 2, 7, 2, 3)
)
_StHttpsRequests_Type = Counter64
_StHttpsRequests_Object = MibScalar
stHttpsRequests = _StHttpsRequests_Object(
    (1, 3, 6, 1, 4, 1, 1230, 2, 7, 2, 3, 1),
    _StHttpsRequests_Type()
)
stHttpsRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stHttpsRequests.setStatus("current")
_StHttpsTraffic_Type = Counter64
_StHttpsTraffic_Object = MibScalar
stHttpsTraffic = _StHttpsTraffic_Object(
    (1, 3, 6, 1, 4, 1, 1230, 2, 7, 2, 3, 2),
    _StHttpsTraffic_Type()
)
stHttpsTraffic.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stHttpsTraffic.setStatus("current")
_StHttpsBytesFromClient_Type = Counter64
_StHttpsBytesFromClient_Object = MibScalar
stHttpsBytesFromClient = _StHttpsBytesFromClient_Object(
    (1, 3, 6, 1, 4, 1, 1230, 2, 7, 2, 3, 3),
    _StHttpsBytesFromClient_Type()
)
stHttpsBytesFromClient.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stHttpsBytesFromClient.setStatus("current")
_StHttpsBytesFromServer_Type = Counter64
_StHttpsBytesFromServer_Object = MibScalar
stHttpsBytesFromServer = _StHttpsBytesFromServer_Object(
    (1, 3, 6, 1, 4, 1, 1230, 2, 7, 2, 3, 4),
    _StHttpsBytesFromServer_Type()
)
stHttpsBytesFromServer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stHttpsBytesFromServer.setStatus("current")
_StHttpsBytesToClient_Type = Counter64
_StHttpsBytesToClient_Object = MibScalar
stHttpsBytesToClient = _StHttpsBytesToClient_Object(
    (1, 3, 6, 1, 4, 1, 1230, 2, 7, 2, 3, 5),
    _StHttpsBytesToClient_Type()
)
stHttpsBytesToClient.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stHttpsBytesToClient.setStatus("current")
_StHttpsBytesToServer_Type = Counter64
_StHttpsBytesToServer_Object = MibScalar
stHttpsBytesToServer = _StHttpsBytesToServer_Object(
    (1, 3, 6, 1, 4, 1, 1230, 2, 7, 2, 3, 6),
    _StHttpsBytesToServer_Type()
)
stHttpsBytesToServer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stHttpsBytesToServer.setStatus("current")
_MwgFTP_ObjectIdentity = ObjectIdentity
mwgFTP = _MwgFTP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1230, 2, 7, 2, 4)
)
_StFtpTraffic_Type = Counter64
_StFtpTraffic_Object = MibScalar
stFtpTraffic = _StFtpTraffic_Object(
    (1, 3, 6, 1, 4, 1, 1230, 2, 7, 2, 4, 1),
    _StFtpTraffic_Type()
)
stFtpTraffic.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stFtpTraffic.setStatus("current")
_StFtpBytesFromClient_Type = Counter64
_StFtpBytesFromClient_Object = MibScalar
stFtpBytesFromClient = _StFtpBytesFromClient_Object(
    (1, 3, 6, 1, 4, 1, 1230, 2, 7, 2, 4, 2),
    _StFtpBytesFromClient_Type()
)
stFtpBytesFromClient.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stFtpBytesFromClient.setStatus("current")
_StFtpBytesFromServer_Type = Counter64
_StFtpBytesFromServer_Object = MibScalar
stFtpBytesFromServer = _StFtpBytesFromServer_Object(
    (1, 3, 6, 1, 4, 1, 1230, 2, 7, 2, 4, 3),
    _StFtpBytesFromServer_Type()
)
stFtpBytesFromServer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stFtpBytesFromServer.setStatus("current")
_StFtpBytesToClient_Type = Counter64
_StFtpBytesToClient_Object = MibScalar
stFtpBytesToClient = _StFtpBytesToClient_Object(
    (1, 3, 6, 1, 4, 1, 1230, 2, 7, 2, 4, 4),
    _StFtpBytesToClient_Type()
)
stFtpBytesToClient.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stFtpBytesToClient.setStatus("current")
_StFtpBytesToServer_Type = Counter64
_StFtpBytesToServer_Object = MibScalar
stFtpBytesToServer = _StFtpBytesToServer_Object(
    (1, 3, 6, 1, 4, 1, 1230, 2, 7, 2, 4, 5),
    _StFtpBytesToServer_Type()
)
stFtpBytesToServer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stFtpBytesToServer.setStatus("current")
_MwgMiscellaneous_ObjectIdentity = ObjectIdentity
mwgMiscellaneous = _MwgMiscellaneous_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1230, 2, 7, 2, 5)
)
_StCPULoad_Type = Counter64
_StCPULoad_Object = MibScalar
stCPULoad = _StCPULoad_Object(
    (1, 3, 6, 1, 4, 1, 1230, 2, 7, 2, 5, 1),
    _StCPULoad_Type()
)
stCPULoad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stCPULoad.setStatus("current")
_StClientCount_Type = Counter64
_StClientCount_Object = MibScalar
stClientCount = _StClientCount_Object(
    (1, 3, 6, 1, 4, 1, 1230, 2, 7, 2, 5, 2),
    _StClientCount_Type()
)
stClientCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stClientCount.setStatus("current")
_StConnectedSockets_Type = Counter64
_StConnectedSockets_Object = MibScalar
stConnectedSockets = _StConnectedSockets_Object(
    (1, 3, 6, 1, 4, 1, 1230, 2, 7, 2, 5, 3),
    _StConnectedSockets_Type()
)
stConnectedSockets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stConnectedSockets.setStatus("current")
_StCPULoadRaw_Type = Counter64
_StCPULoadRaw_Object = MibScalar
stCPULoadRaw = _StCPULoadRaw_Object(
    (1, 3, 6, 1, 4, 1, 1230, 2, 7, 2, 5, 4),
    _StCPULoadRaw_Type()
)
stCPULoadRaw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stCPULoadRaw.setStatus("current")
_StCPUIOWait_Type = Counter64
_StCPUIOWait_Object = MibScalar
stCPUIOWait = _StCPUIOWait_Object(
    (1, 3, 6, 1, 4, 1, 1230, 2, 7, 2, 5, 5),
    _StCPUIOWait_Type()
)
stCPUIOWait.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stCPUIOWait.setStatus("current")
_StResolveHostViaDNS_Type = Counter64
_StResolveHostViaDNS_Object = MibScalar
stResolveHostViaDNS = _StResolveHostViaDNS_Object(
    (1, 3, 6, 1, 4, 1, 1230, 2, 7, 2, 5, 6),
    _StResolveHostViaDNS_Type()
)
stResolveHostViaDNS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stResolveHostViaDNS.setStatus("current")
_StTimeConsumedByRuleEngine_Type = Counter64
_StTimeConsumedByRuleEngine_Object = MibScalar
stTimeConsumedByRuleEngine = _StTimeConsumedByRuleEngine_Object(
    (1, 3, 6, 1, 4, 1, 1230, 2, 7, 2, 5, 7),
    _StTimeConsumedByRuleEngine_Type()
)
stTimeConsumedByRuleEngine.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stTimeConsumedByRuleEngine.setStatus("current")
_StTimeForTransaction_Type = Counter64
_StTimeForTransaction_Object = MibScalar
stTimeForTransaction = _StTimeForTransaction_Object(
    (1, 3, 6, 1, 4, 1, 1230, 2, 7, 2, 5, 8),
    _StTimeForTransaction_Type()
)
stTimeForTransaction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stTimeForTransaction.setStatus("current")
_StHandleConnectToServer_Type = Counter64
_StHandleConnectToServer_Object = MibScalar
stHandleConnectToServer = _StHandleConnectToServer_Object(
    (1, 3, 6, 1, 4, 1, 1230, 2, 7, 2, 5, 9),
    _StHandleConnectToServer_Type()
)
stHandleConnectToServer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stHandleConnectToServer.setStatus("current")
_StFirstSentFirstReceivedClient_Type = Counter64
_StFirstSentFirstReceivedClient_Object = MibScalar
stFirstSentFirstReceivedClient = _StFirstSentFirstReceivedClient_Object(
    (1, 3, 6, 1, 4, 1, 1230, 2, 7, 2, 5, 10),
    _StFirstSentFirstReceivedClient_Type()
)
stFirstSentFirstReceivedClient.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stFirstSentFirstReceivedClient.setStatus("current")
_StLastSentLastReceivedClient_Type = Counter64
_StLastSentLastReceivedClient_Object = MibScalar
stLastSentLastReceivedClient = _StLastSentLastReceivedClient_Object(
    (1, 3, 6, 1, 4, 1, 1230, 2, 7, 2, 5, 11),
    _StLastSentLastReceivedClient_Type()
)
stLastSentLastReceivedClient.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stLastSentLastReceivedClient.setStatus("current")
_StFirstSentFirstReceivedServer_Type = Counter64
_StFirstSentFirstReceivedServer_Object = MibScalar
stFirstSentFirstReceivedServer = _StFirstSentFirstReceivedServer_Object(
    (1, 3, 6, 1, 4, 1, 1230, 2, 7, 2, 5, 12),
    _StFirstSentFirstReceivedServer_Type()
)
stFirstSentFirstReceivedServer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stFirstSentFirstReceivedServer.setStatus("current")
_StLastSentLastReceivedServer_Type = Counter64
_StLastSentLastReceivedServer_Object = MibScalar
stLastSentLastReceivedServer = _StLastSentLastReceivedServer_Object(
    (1, 3, 6, 1, 4, 1, 1230, 2, 7, 2, 5, 13),
    _StLastSentLastReceivedServer_Type()
)
stLastSentLastReceivedServer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stLastSentLastReceivedServer.setStatus("current")
_StLastSentFirstReceivedServer_Type = Counter64
_StLastSentFirstReceivedServer_Object = MibScalar
stLastSentFirstReceivedServer = _StLastSentFirstReceivedServer_Object(
    (1, 3, 6, 1, 4, 1, 1230, 2, 7, 2, 5, 14),
    _StLastSentFirstReceivedServer_Type()
)
stLastSentFirstReceivedServer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stLastSentFirstReceivedServer.setStatus("current")
_StMemConsumed_Type = Counter64
_StMemConsumed_Object = MibScalar
stMemConsumed = _StMemConsumed_Object(
    (1, 3, 6, 1, 4, 1, 1230, 2, 7, 2, 5, 15),
    _StMemConsumed_Type()
)
stMemConsumed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stMemConsumed.setStatus("current")
_MwgTraps_ObjectIdentity = ObjectIdentity
mwgTraps = _MwgTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1230, 2, 7, 4)
)
_MwgTrapVariables_ObjectIdentity = ObjectIdentity
mwgTrapVariables = _MwgTrapVariables_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1230, 2, 7, 4, 10)
)
_NotifyOrigin_Type = Integer32
_NotifyOrigin_Object = MibScalar
notifyOrigin = _NotifyOrigin_Object(
    (1, 3, 6, 1, 4, 1, 1230, 2, 7, 4, 10, 1),
    _NotifyOrigin_Type()
)
notifyOrigin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    notifyOrigin.setStatus("current")
_NotifyOriginName_Type = OctetString
_NotifyOriginName_Object = MibScalar
notifyOriginName = _NotifyOriginName_Object(
    (1, 3, 6, 1, 4, 1, 1230, 2, 7, 4, 10, 2),
    _NotifyOriginName_Type()
)
notifyOriginName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    notifyOriginName.setStatus("current")


class _NotifySeverity_Type(Integer32):
    """Custom type notifySeverity based on Integer32"""
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
              7)
        )
    )
    namedValues = NamedValues(
        *(("emergency", 0),
          ("alert", 1),
          ("critical", 2),
          ("error", 3),
          ("warning", 4),
          ("notice", 5),
          ("info", 6),
          ("debug", 7))
    )


_NotifySeverity_Type.__name__ = "Integer32"
_NotifySeverity_Object = MibScalar
notifySeverity = _NotifySeverity_Object(
    (1, 3, 6, 1, 4, 1, 1230, 2, 7, 4, 10, 3),
    _NotifySeverity_Type()
)
notifySeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    notifySeverity.setStatus("current")
_NotifyReason_Type = Integer32
_NotifyReason_Object = MibScalar
notifyReason = _NotifyReason_Object(
    (1, 3, 6, 1, 4, 1, 1230, 2, 7, 4, 10, 4),
    _NotifyReason_Type()
)
notifyReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    notifyReason.setStatus("current")
_NotifyReasonString_Type = OctetString
_NotifyReasonString_Object = MibScalar
notifyReasonString = _NotifyReasonString_Object(
    (1, 3, 6, 1, 4, 1, 1230, 2, 7, 4, 10, 5),
    _NotifyReasonString_Type()
)
notifyReasonString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    notifyReasonString.setStatus("current")
_NotifyAffectedHost_Type = IpAddress
_NotifyAffectedHost_Object = MibScalar
notifyAffectedHost = _NotifyAffectedHost_Object(
    (1, 3, 6, 1, 4, 1, 1230, 2, 7, 4, 10, 6),
    _NotifyAffectedHost_Type()
)
notifyAffectedHost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    notifyAffectedHost.setStatus("current")
_NotifyAdditional_Type = OctetString
_NotifyAdditional_Object = MibScalar
notifyAdditional = _NotifyAdditional_Object(
    (1, 3, 6, 1, 4, 1, 1230, 2, 7, 4, 10, 7),
    _NotifyAdditional_Type()
)
notifyAdditional.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    notifyAdditional.setStatus("current")

# Managed Objects groups


# Notification objects

trSystem = NotificationType(
    (1, 3, 6, 1, 4, 1, 1230, 2, 7, 4, 1)
)
trSystem.setObjects(
      *(("MCAFEE-MWG-MIB", "notifyOrigin"),
        ("MCAFEE-MWG-MIB", "notifyOriginName"),
        ("MCAFEE-MWG-MIB", "notifySeverity"),
        ("MCAFEE-MWG-MIB", "notifyReason"),
        ("MCAFEE-MWG-MIB", "notifyReasonString"),
        ("MCAFEE-MWG-MIB", "notifyAffectedHost"),
        ("MCAFEE-MWG-MIB", "notifyAdditional"))
)
if mibBuilder.loadTexts:
    trSystem.setStatus(
        "current"
    )

trApplication = NotificationType(
    (1, 3, 6, 1, 4, 1, 1230, 2, 7, 4, 2)
)
trApplication.setObjects(
      *(("MCAFEE-MWG-MIB", "notifyOrigin"),
        ("MCAFEE-MWG-MIB", "notifyOriginName"),
        ("MCAFEE-MWG-MIB", "notifySeverity"),
        ("MCAFEE-MWG-MIB", "notifyReason"),
        ("MCAFEE-MWG-MIB", "notifyReasonString"),
        ("MCAFEE-MWG-MIB", "notifyAffectedHost"),
        ("MCAFEE-MWG-MIB", "notifyAdditional"))
)
if mibBuilder.loadTexts:
    trApplication.setStatus(
        "current"
    )

trUser = NotificationType(
    (1, 3, 6, 1, 4, 1, 1230, 2, 7, 4, 3)
)
trUser.setObjects(
      *(("MCAFEE-MWG-MIB", "notifyReason"),
        ("MCAFEE-MWG-MIB", "notifyReasonString"),
        ("MCAFEE-MWG-MIB", "notifyAffectedHost"),
        ("MCAFEE-MWG-MIB", "notifyAdditional"))
)
if mibBuilder.loadTexts:
    trUser.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "MCAFEE-MWG-MIB",
    **{"mwg": mwg,
       "mwgInfo": mwgInfo,
       "kProductName": kProductName,
       "kCompanyName": kCompanyName,
       "kProductVersion": kProductVersion,
       "kMajorVersion": kMajorVersion,
       "kMinorVersion": kMinorVersion,
       "kMicroVersion": kMicroVersion,
       "kHotfixVersion": kHotfixVersion,
       "kCustomVersion": kCustomVersion,
       "kRevision": kRevision,
       "kBuildNumber": kBuildNumber,
       "mwgEngineVersions": mwgEngineVersions,
       "pAMEngineVersion": pAMEngineVersion,
       "pAMSignatureVersion": pAMSignatureVersion,
       "pMFEEngineVersion": pMFEEngineVersion,
       "pMFEDATVersion": pMFEDATVersion,
       "pAMProactiveVersion": pAMProactiveVersion,
       "pTSDBVersion": pTSDBVersion,
       "mwgStatistics": mwgStatistics,
       "mwgContent": mwgContent,
       "stBadReputation": stBadReputation,
       "stMalwareDetected": stMalwareDetected,
       "stConnectionsLegitimate": stConnectionsLegitimate,
       "stBlockedByAntiMalware": stBlockedByAntiMalware,
       "stConnectionsBlocked": stConnectionsBlocked,
       "stBlockedByMediaFilter": stBlockedByMediaFilter,
       "stBlockedByURLFilter": stBlockedByURLFilter,
       "stMimeType": stMimeType,
       "stCategories": stCategories,
       "stCategoriesTable": stCategoriesTable,
       "stCategoriesEntry": stCategoriesEntry,
       "stCategoryName": stCategoryName,
       "stCategoryCount": stCategoryCount,
       "mwgHttp": mwgHttp,
       "stHttpRequests": stHttpRequests,
       "stHttpTraffic": stHttpTraffic,
       "stHttpBytesFromClient": stHttpBytesFromClient,
       "stHttpBytesFromServer": stHttpBytesFromServer,
       "stHttpBytesToClient": stHttpBytesToClient,
       "stHttpBytesToServer": stHttpBytesToServer,
       "mwgHttps": mwgHttps,
       "stHttpsRequests": stHttpsRequests,
       "stHttpsTraffic": stHttpsTraffic,
       "stHttpsBytesFromClient": stHttpsBytesFromClient,
       "stHttpsBytesFromServer": stHttpsBytesFromServer,
       "stHttpsBytesToClient": stHttpsBytesToClient,
       "stHttpsBytesToServer": stHttpsBytesToServer,
       "mwgFTP": mwgFTP,
       "stFtpTraffic": stFtpTraffic,
       "stFtpBytesFromClient": stFtpBytesFromClient,
       "stFtpBytesFromServer": stFtpBytesFromServer,
       "stFtpBytesToClient": stFtpBytesToClient,
       "stFtpBytesToServer": stFtpBytesToServer,
       "mwgMiscellaneous": mwgMiscellaneous,
       "stCPULoad": stCPULoad,
       "stClientCount": stClientCount,
       "stConnectedSockets": stConnectedSockets,
       "stCPULoadRaw": stCPULoadRaw,
       "stCPUIOWait": stCPUIOWait,
       "stResolveHostViaDNS": stResolveHostViaDNS,
       "stTimeConsumedByRuleEngine": stTimeConsumedByRuleEngine,
       "stTimeForTransaction": stTimeForTransaction,
       "stHandleConnectToServer": stHandleConnectToServer,
       "stFirstSentFirstReceivedClient": stFirstSentFirstReceivedClient,
       "stLastSentLastReceivedClient": stLastSentLastReceivedClient,
       "stFirstSentFirstReceivedServer": stFirstSentFirstReceivedServer,
       "stLastSentLastReceivedServer": stLastSentLastReceivedServer,
       "stLastSentFirstReceivedServer": stLastSentFirstReceivedServer,
       "stMemConsumed": stMemConsumed,
       "mwgTraps": mwgTraps,
       "trSystem": trSystem,
       "trApplication": trApplication,
       "trUser": trUser,
       "mwgTrapVariables": mwgTrapVariables,
       "notifyOrigin": notifyOrigin,
       "notifyOriginName": notifyOriginName,
       "notifySeverity": notifySeverity,
       "notifyReason": notifyReason,
       "notifyReasonString": notifyReasonString,
       "notifyAffectedHost": notifyAffectedHost,
       "notifyAdditional": notifyAdditional}
)
